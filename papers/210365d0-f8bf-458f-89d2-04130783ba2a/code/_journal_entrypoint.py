#!/usr/bin/env python3
"""Generic experiment entrypoint baked into the experiment image at /opt/journal.

Runs an arbitrary experiment module (staged separately and bind-mounted) and writes a
reproducibility bundle to the results dir:

  - metadata.json : seeds, git sha, args, timings, versions, gpu, host, status
  - metrics.json  : whatever the experiment's ``run(results_dir, **kwargs)`` returns

Convention: the experiment module defines ``run(results_dir, **kwargs) -> dict | None``.

This file is intentionally self-contained (stdlib only at its core; numpy/torch are
optional) so it runs both inside the CUDA image and in plain unit tests.

    python entrypoint.py --code-dir DIR --entrypoint MODULE --results-dir DIR \
        [--seed N] [--git-sha SHA] [--args-json '{"size": 4096}'] \
        [--datasets-json '{"wikitext-2": "/work/datasets/<sha>/wikitext-2.zip"}']

Datasets (staged on the login node into the bind-mounted cache; see app/experiment/
datasets.py) are passed to the experiment as a ``datasets`` kwarg (a name -> local path
mapping) and exported as the ``JOURNAL_DATASETS`` env var. They are injected only when
non-empty, so experiments that use synthetic data (and the demo toy) are unaffected.
"""

from __future__ import annotations

# When this file is executed directly from ``app/experiment``, Python places that directory
# first on sys.path and its ``types.py`` can shadow the standard-library ``types`` module.
# Remove only the script-directory entry before importing the rest of the stdlib.
import sys

if sys.path:
    sys.path.pop(0)

import argparse
import datetime as _dt
import importlib
import json
import math
import os
import platform
import socket
import time
import traceback


def _now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat()


def set_seeds(seed: int) -> dict:
    """Seed Python / numpy / torch (whichever are importable). Returns what was seeded."""
    seeded: dict[str, object] = {"python": seed, "PYTHONHASHSEED": str(seed)}
    import random

    random.seed(seed)

    try:
        import numpy as np

        np.random.seed(seed)
        seeded["numpy"] = seed
    except Exception:  # noqa: BLE001 - numpy is optional
        seeded["numpy"] = None

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
        seeded["torch"] = seed
    except Exception:  # noqa: BLE001 - torch is optional
        seeded["torch"] = None

    return seeded


def collect_versions() -> dict:
    versions = {"python": platform.python_version()}
    for name in ("numpy", "torch", "pandas", "sklearn", "matplotlib"):
        try:
            module = importlib.import_module(name)
            versions[name] = getattr(module, "__version__", "unknown")
        except Exception:  # noqa: BLE001
            versions[name] = None
    return versions


def gpu_info() -> dict:
    try:
        import torch

        if torch.cuda.is_available():
            return {
                "cuda_available": True,
                "device_count": torch.cuda.device_count(),
                "devices": [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())],
            }
        return {"cuda_available": False}
    except Exception:  # noqa: BLE001
        return {"cuda_available": None}


def _write_json(path: str, data: object) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, default=str)


def _call_experiment(module, results_dir: str, kwargs: dict):
    if hasattr(module, "run"):
        return module.run(results_dir, **kwargs)
    raise AttributeError(
        f"experiment module {module.__name__!r} must define run(results_dir, **kwargs)"
    )


def _validate_cohort(
    name: str,
    cohort: object,
    expected_ids: list,
    *,
    smoke: bool,
    required_condition_ids: list[str] | None = None,
) -> None:
    if not isinstance(cohort, dict):
        raise ValueError(f"result.{name} must be an object")
    returned_ids = cohort.get("seed_ids")
    if not isinstance(returned_ids, list) or not returned_ids:
        raise ValueError(f"result.{name}.seed_ids must be a non-empty list")
    required_ids = expected_ids[: len(returned_ids)] if smoke else expected_ids
    if returned_ids != required_ids or (smoke and len(returned_ids) != 1):
        mode = "the first preregistered ID" if smoke else "the exact preregistered IDs"
        raise ValueError(f"result.{name}.seed_ids must equal {mode} in order")
    conditions = cohort.get("conditions")
    if not isinstance(conditions, dict) or len(conditions) < 2:
        raise ValueError(f"result.{name}.conditions must contain proposed and baseline")
    if required_condition_ids is not None and set(conditions) != set(required_condition_ids):
        raise ValueError(
            f"result.{name}.conditions must contain exactly the registered condition ids"
        )
    for condition, metrics in conditions.items():
        if not isinstance(metrics, dict) or not metrics:
            raise ValueError(f"result.{name}.conditions.{condition} must contain metrics")
        for metric, values in metrics.items():
            if not isinstance(values, list) or len(values) != len(returned_ids):
                raise ValueError(
                    f"result.{name}.conditions.{condition}.{metric} must have one value per seed"
                )
            if any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(float(value))
                for value in values
            ):
                raise ValueError(
                    f"result.{name}.conditions.{condition}.{metric} must be finite numeric values"
                )


def _validate_confirmatory_result(result: object, run_kwargs: dict) -> None:
    """Enforce executed primary + independent replication cohorts when preregistered."""

    primary_ids = run_kwargs.get("seed_ids")
    replication_ids = run_kwargs.get("replication_seed_ids")
    if primary_ids is None and replication_ids is None:  # legacy/demo result contract
        return
    if not isinstance(primary_ids, list) or not isinstance(replication_ids, list):
        raise ValueError("seed_ids and replication_seed_ids must both be runner-provided lists")
    if not isinstance(result, dict):
        raise ValueError("experiment result must be an object")
    smoke = bool(run_kwargs.get("smoke"))
    required_condition_ids = run_kwargs.get("required_condition_ids")
    if required_condition_ids is not None and (
        not isinstance(required_condition_ids, list)
        or not required_condition_ids
        or any(not isinstance(item, str) or not item for item in required_condition_ids)
    ):
        raise ValueError("required_condition_ids must be a non-empty runner-provided list")
    _validate_cohort(
        "primary",
        result.get("primary"),
        primary_ids,
        smoke=smoke,
        required_condition_ids=required_condition_ids,
    )
    _validate_cohort(
        "replication",
        result.get("replication"),
        replication_ids,
        smoke=smoke,
        required_condition_ids=required_condition_ids,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generic experiment runner.")
    parser.add_argument("--code-dir", required=True)
    parser.add_argument("--entrypoint", required=True, help="experiment module name")
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--git-sha", default="unknown")
    parser.add_argument("--args-json", default="{}")
    parser.add_argument("--datasets-json", default="{}", help="name -> staged path mapping")
    args = parser.parse_args(argv)

    os.makedirs(args.results_dir, exist_ok=True)
    try:
        run_kwargs = json.loads(args.args_json) or {}
    except json.JSONDecodeError as exc:
        print(f"invalid --args-json: {exc}", file=sys.stderr)
        return 2
    try:
        datasets = json.loads(args.datasets_json) or {}
    except json.JSONDecodeError as exc:
        print(f"invalid --datasets-json: {exc}", file=sys.stderr)
        return 2
    # Expose staged datasets to the experiment, but only when present — keep synthetic-data
    # experiments (and the stdlib demo toy) byte-for-byte unchanged.
    if datasets:
        os.environ["JOURNAL_DATASETS"] = json.dumps(datasets)
        run_kwargs.setdefault("datasets", datasets)

    seeds = set_seeds(args.seed)
    metadata = {
        "status": "running",
        "entrypoint": args.entrypoint,
        "code_dir": args.code_dir,
        "seed": args.seed,
        "seeds": seeds,
        "git_sha": args.git_sha,
        "args": run_kwargs,
        "datasets": datasets,
        "hostname": socket.gethostname(),
        "slurm_job_id": os.environ.get("SLURM_JOB_ID"),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
        "versions": collect_versions(),
        "gpu": gpu_info(),
        "started_at": _now_iso(),
    }
    metadata_path = os.path.join(args.results_dir, "metadata.json")
    _write_json(metadata_path, metadata)  # partial, survives a crash

    start = time.time()
    exit_code = 0
    try:
        sys.path.insert(0, args.code_dir)
        module = importlib.import_module(args.entrypoint)
        result = _call_experiment(module, args.results_dir, run_kwargs)
        _validate_confirmatory_result(result, run_kwargs)
        metadata["status"] = "completed"
        _write_json(os.path.join(args.results_dir, "metrics.json"), result or {})
        print(f"experiment completed; metrics={result!r}")
    except Exception:  # noqa: BLE001 - record any failure into the bundle
        metadata["status"] = "error"
        metadata["error"] = traceback.format_exc()
        print(metadata["error"], file=sys.stderr)
        exit_code = 1
    finally:
        end = time.time()
        metadata["finished_at"] = _now_iso()
        metadata["duration_seconds"] = round(end - start, 4)
        _write_json(metadata_path, metadata)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
