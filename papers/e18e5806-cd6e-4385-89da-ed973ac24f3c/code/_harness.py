"""Server-owned experiment driver. Staged into every harness bundle; never model-written.

This owns everything the recipe already determines — the paired cohort loops over the
preregistered seed lists, one RNG per seed with precomputed epoch permutations, every
registered condition, curve logging, the smoke path, the non-finite policy and the results
schema. The generated code contributes exactly one function, ``apply_operator(ctx)``.

Why: two A100 jobs (the scheduler 15504724 / 15504898) and sixteen codegen attempts were lost to code
that had to re-derive this scaffolding from prose — a tensor name, an archive member, a
writable directory. None of that is science, and all of it is already known here.

The module imports torch lazily so the orchestration logic stays importable (and testable)
without it.
"""

from __future__ import annotations

CURVE_POINTS = 12


class OperatorContext:
    """What the generated operator may see and touch.

    The operator gets its own ``rng``: drawing from the training stream would unpair the
    conditions, and the analysis is a per-seed paired difference. Making that structurally
    impossible is the point of passing it in.

    ``state`` is a plain dict that persists across every step of one (seed, condition) run and
    is discarded between them. An operator with a threshold fixed at initialisation, a counter,
    or any other carried quantity keeps it there — a fresh context is constructed per step, so
    an attribute set on the context itself would silently vanish.
    """

    __slots__ = (
        "condition", "step", "epoch", "total_steps", "model", "optimizer",
        "target", "target_name", "momentum_buffer", "rng", "torch", "state",
        "_generator",
    )

    def __init__(self, **fields) -> None:
        for name in self.__slots__:
            setattr(self, name, fields.get(name))

    # Tensor-valued randomness MUST come from these, not from ``rng``. The target lives on the
    # GPU during a real run and on the CPU in the preflight sandbox, so a numpy array folded
    # into a CUDA tensor raises "can't convert cuda:0 device type tensor to numpy" — on the
    # GPU only. That is invisible to the dry-run by construction, and it killed compute job
    # 15539746. These draw from the operator's own generator on the tensor's own device, so
    # the paired contract holds and the device is right without the author thinking about it.
    def randn_like(self, tensor):
        return self.torch.randn(
            tensor.shape, generator=self._generator, device=tensor.device, dtype=tensor.dtype
        )

    def rand_like(self, tensor):
        return self.torch.rand(
            tensor.shape, generator=self._generator, device=tensor.device, dtype=tensor.dtype
        )

    @property
    def is_proposed(self) -> bool:
        return self.condition == "proposed"

    @property
    def is_baseline(self) -> bool:
        return self.condition.startswith("baseline_")

    @property
    def is_negative_control(self) -> bool:
        return self.condition.startswith("negative_control_")


def downsample(points, limit=CURVE_POINTS):
    """Even-spaced subsample of [[step, value], ...] keeping the first and last points."""

    if len(points) <= limit:
        return [[int(s), float(v)] for s, v in points]
    stride = (len(points) - 1) / (limit - 1)
    picked = [points[min(len(points) - 1, int(round(i * stride)))] for i in range(limit)]
    return [[int(s), float(v)] for s, v in picked]


def mean_curves(per_seed_curves, limit=CURVE_POINTS):
    """Mean over seeds at each logged step (curves share a step grid by construction)."""

    if not per_seed_curves:
        return []
    length = min(len(c) for c in per_seed_curves)
    merged = []
    for i in range(length):
        step = per_seed_curves[0][i][0]
        merged.append([step, sum(c[i][1] for c in per_seed_curves) / len(per_seed_curves)])
    return downsample(merged, limit)


def cohort_seed_ids(seed_ids, smoke):
    """Smoke mode uses the FIRST seed of the cohort — never a different or renumbered one."""

    ids = [int(s) for s in seed_ids]
    return ids[:1] if smoke else ids


def run_experiment(
    results_dir,
    *,
    testbed,
    apply_operator,
    seed_ids,
    replication_seed_ids,
    required_condition_ids,
    target_name,
    datasets=None,
    smoke=False,
):
    """Drive every cohort × condition × seed and return the structured result.

    ``testbed`` supplies the data and model (server-owned, per recipe); ``apply_operator`` is
    the generated hook. Everything between them is fixed here.
    """

    import json
    import os

    conditions = list(required_condition_ids)
    if not conditions:
        raise ValueError("no condition ids were supplied")

    if smoke:
        data = testbed.synthetic_cohorts()
        epochs, batch_size = 1, testbed.SMOKE_BATCH_SIZE
        max_steps = testbed.SMOKE_STEPS
    else:
        staged = (datasets or {}).get(testbed.DATASET_NAME)
        if not staged:
            raise ValueError(
                f"staged dataset {testbed.DATASET_NAME!r} was not provided; the full run "
                "must not fabricate data"
            )
        data = testbed.load_cohorts(staged)
        epochs, batch_size = testbed.EPOCHS, testbed.BATCH_SIZE
        max_steps = None

    result = {}
    for cohort_name, ids in (
        ("primary", seed_ids), ("replication", replication_seed_ids)
    ):
        cohort_ids = cohort_seed_ids(ids, smoke)
        metrics = {condition: {testbed.OUTCOME_NAME: []} for condition in conditions}
        curves = {condition: [] for condition in conditions}
        operator_activations = {condition: [] for condition in conditions}

        for seed in cohort_ids:
            # One RNG per seed, drawn ONCE: initial parameters, the train/eval order and every
            # epoch permutation come from it and are reused by every condition in this seed's
            # pair. Only apply_operator differs between conditions.
            shared = testbed.derive_seed_artifacts(
                int(seed), data, epochs=epochs, batch_size=batch_size, max_steps=max_steps
            )
            for condition in conditions:
                accuracy, curve, activations = _train_one_condition(
                    testbed=testbed, shared=shared, data=data, condition=condition,
                    apply_operator=apply_operator, target_name=target_name, seed=int(seed),
                )
                if accuracy != accuracy or accuracy in (float("inf"), float("-inf")):
                    raise ValueError(
                        f"non-finite {testbed.OUTCOME_NAME} for condition {condition!r} "
                        f"at seed {seed} — the run cannot report it as a result"
                    )
                metrics[condition][testbed.OUTCOME_NAME].append(float(accuracy))
                curves[condition].append(curve)
                operator_activations[condition].append(int(activations))

        result[cohort_name] = {
            "seed_ids": cohort_ids,
            "conditions": metrics,
            "curves": {
                condition: {testbed.OUTCOME_NAME: mean_curves(curves[condition])}
                for condition in conditions
            },
            # Steps on which the operator changed the target or its momentum buffer, per seed.
            # All zero for an arm means the operator never fired in that arm.
            "operator_activations": operator_activations,
        }

    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, "results.json"), "w") as handle:
        json.dump(result, handle, indent=2)
    return result


def _train_one_condition(
    *, testbed, shared, data, condition, apply_operator, target_name, seed
):
    """One condition's training run over this seed's shared artifacts."""

    import numpy as np
    import torch

    model = testbed.build_model()
    model.load_state_dict(shared["init_state"])
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    state = model.state_dict()
    if target_name not in state:
        raise KeyError(
            f"operator target {target_name!r} is not a parameter of this model; "
            f"available: {sorted(state)}"
        )
    target = dict(model.named_parameters())[target_name]

    optimizer = testbed.build_optimizer(model)
    # The operator's randomness is its own, so it cannot shift the training stream and
    # unpair the conditions. Two views of the SAME dedicated stream: numpy for scalar
    # decisions, and a torch generator on the training device for tensor-valued draws.
    operator_seed = (int(seed) * 2_654_435_761 + 1_013_904_223) % (2**31 - 1)
    operator_rng = np.random.default_rng(operator_seed)
    operator_generator = torch.Generator(device=device)
    operator_generator.manual_seed(operator_seed)

    curve = []
    total_steps = len(shared["batches"])
    # One scratch dict for the whole run: the operator's carried state (a threshold fixed at
    # initialisation, a counter) has to outlive the per-step context object.
    operator_state = {}
    # How often the operator actually changed something. An operator whose activation condition
    # is never met makes its arm bit-identical to the comparator, and the run then LOOKS like a
    # clean null while having measured nothing at all. Counting here turns that from a mystery
    # inferred off identical metrics into a recorded fact. Counted on-device; synced once.
    activations = 0
    for index, (epoch, batch_index) in enumerate(shared["batches"]):
        loss = testbed.training_step(model, optimizer, data, shared, epoch, batch_index, device)
        buffer = optimizer.state.get(target, {}).get("momentum_buffer")
        before_target = target.detach().clone()
        before_buffer = buffer.detach().clone() if buffer is not None else None
        apply_operator(OperatorContext(
            condition=condition, step=index, epoch=epoch, total_steps=total_steps,
            model=model, optimizer=optimizer, target=target, target_name=target_name,
            momentum_buffer=buffer,
            rng=operator_rng, torch=torch, state=operator_state,
            _generator=operator_generator,
        ))
        changed = not torch.equal(before_target, target)
        if not changed and before_buffer is not None:
            changed = not torch.equal(before_buffer, buffer)
        activations += int(changed)
        if index % max(1, total_steps // testbed.CURVE_SAMPLES) == 0 or index == total_steps - 1:
            curve.append([index, float(loss)])

    accuracy = testbed.evaluate(model, data, device)
    return accuracy, curve, activations
