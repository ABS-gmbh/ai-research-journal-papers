"""Bundle entrypoint for a harness run. Server-owned; the model contributes only the operator.

The generic journal entrypoint calls ``run(results_dir, **kwargs)`` here. This module wires the
run's protocol constants to the server's testbed definition and the generated operator hook,
verifies the model's parameter inventory before spending any compute, and hands control to the
driver in ``_harness``.
"""

from __future__ import annotations

import _harness
import _protocol
import _testbed
# NOT `operator` — that is a standard-library module, and shadowing it breaks numpy/torch.
from operator_hook import apply_operator


def _verify_parameter_inventory() -> None:
    """Fail here, precisely, rather than as a KeyError inside a queued GPU job.

    Slurm job 15504898 died deep in training on a tensor name that did not exist. The dry-run
    builds this same model, so the check runs in preflight and that class cannot reach HPC.
    """

    state = _testbed.build_model().state_dict()
    problems = []
    for name, shape in _testbed.PARAMETER_SHAPES.items():
        if name not in state:
            problems.append(f"{name} is missing (model has {sorted(state)})")
        elif tuple(state[name].shape) != tuple(shape):
            problems.append(f"{name} has shape {tuple(state[name].shape)}, expected {tuple(shape)}")
    if problems:
        raise AssertionError("testbed parameter inventory does not match the recipe: " + "; ".join(problems))
    if _protocol.TARGET_NAME not in state:
        raise AssertionError(
            f"operator target {_protocol.TARGET_NAME!r} is not a parameter of this model; "
            f"available: {sorted(state)}"
        )


def run(results_dir, *, seed_ids, replication_seed_ids, required_condition_ids,
        datasets=None, smoke=False, **kwargs):
    _verify_parameter_inventory()
    return _harness.run_experiment(
        results_dir,
        testbed=_testbed,
        apply_operator=apply_operator,
        seed_ids=seed_ids,
        replication_seed_ids=replication_seed_ids,
        required_condition_ids=required_condition_ids,
        target_name=_protocol.TARGET_NAME,
        datasets=datasets,
        smoke=smoke,
    )
