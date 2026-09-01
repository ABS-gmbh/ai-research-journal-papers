"""Server-owned experiment driver. Staged into every harness bundle; never model-written.

This owns everything the recipe already determines — the paired cohort loops over the
preregistered seed lists, one RNG per seed with precomputed epoch permutations, every
registered condition, curve logging, the smoke path, the non-finite policy and the results
schema. The generated code contributes exactly one function, ``apply_operator(ctx)``.

Why: two A100 jobs (the scheduler 15504724 / 15504898) and sixteen codegen attempts were lost to code
that had to re-derive this scaffolding from prose — a tensor name, an archive member, a
writable directory. None of that is science, and all of it is already known here.

**The operator lifecycle.** The driver used to offer exactly one hook, after the optimizer
step. The journal's first paper preregistered an intervention that perturbs the target before
the forward pass, adds a term to the training objective, and learns its noise scale by
backpropagation — none of which that hook can express — so the generated operator did the only
thing available: it mutated the live parameter in place under ``no_grad`` after the update,
advanced the "learnable" scale with hand-written arithmetic the loss never touched, and let the
perturbation accumulate into the evaluated weights. The numbers reproduced exactly. They
reproduced the wrong experiment. The driver now invokes the operator at each of the three
phases the protocol may register (``pre_forward`` / ``loss_term`` / ``post_step``), and RECORDS
which of them the operator actually realized so the entrypoint can refuse results whose
execution does not match the registration.

``pre_forward`` is a differentiable *reparameterization*, not an in-place write: the operator
returns a function of the target, the forward and backward passes see its output, and the base
parameter is restored — untouched — before the optimizer step. That makes three of the
invariants structural rather than asserted: an operator-owned parameter gets a real gradient
from the real loss, the base weight never accumulates the perturbation, and the held-out
evaluation reads clean deterministic weights.

The module imports torch lazily so the orchestration logic stays importable (and testable)
without it.
"""

from __future__ import annotations

CURVE_POINTS = 12

#: What the per-step curve actually IS: the CLASSIFICATION objective, before any operator term
#: is added, so the series means the same thing in every arm. Filing it under the outcome's name
#: made every figure claim to plot "held-out classification accuracy" while showing a loss
#: falling from 1.85 to 0.1 — a false axis on a published figure. Name the series for what it is
#: and the label follows.
CURVE_SERIES = "training loss"

PRE_FORWARD = "pre_forward"
LOSS_TERM = "loss_term"
POST_STEP = "post_step"
PHASES = (PRE_FORWARD, LOSS_TERM, POST_STEP)


class ConformanceError(AssertionError):
    """The executed operator does not realize the protocol that was registered."""


class OperatorContext:
    """What the generated operator may see and touch.

    The operator gets its own ``rng``: drawing from the training stream would unpair the
    conditions, and the analysis is a per-seed paired difference. Making that structurally
    impossible is the point of passing it in.

    ``state`` is a plain dict that persists across every step of one (seed, condition) run and
    is discarded between them. An operator with a threshold fixed at initialisation, a counter,
    or any other carried quantity keeps it there — a fresh context is constructed per phase, so
    an attribute set on the context itself would silently vanish.

    ``phase`` names where in the step the operator is being invoked. Branch on it exactly as on
    ``condition``: the harness calls the operator at every phase and does whatever the operator
    does in each.
    """

    __slots__ = (
        "condition", "phase", "step", "epoch", "total_steps", "model", "optimizer",
        "target", "target_name", "momentum_buffer", "rng", "torch", "state",
        "_generator", "_record",
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

    # --- the three phases ------------------------------------------------------------------ #

    def reparameterize(self, function):
        """``pre_forward`` only: use ``function(target)`` in place of the target this step.

        The returned tensor is what the forward and backward passes see. The base parameter is
        never written to, so the perturbation cannot accumulate across steps, the optimizer
        updates the clean weights, and the held-out evaluation reads them. Because the
        reparameterization is an ordinary differentiable expression, any parameter it closes
        over receives the true gradient of the true loss.
        """

        if self.phase != PRE_FORWARD:
            raise ConformanceError(
                f"ctx.reparameterize() is only valid in the {PRE_FORWARD!r} phase "
                f"(called in {self.phase!r})"
            )
        if self._record["reparameterization"] is not None:
            raise ConformanceError("the operator reparameterized the target twice in one step")
        if not callable(function):
            raise ConformanceError("ctx.reparameterize() takes a callable of the target tensor")
        self._record["reparameterization"] = function

    def add_loss(self, term):
        """``loss_term`` only: add ``term`` to this step's training objective.

        The term is summed into the loss BEFORE the backward pass, inside the autograd graph,
        so it is genuinely part of what is differentiated.
        """

        if self.phase != LOSS_TERM:
            raise ConformanceError(
                f"ctx.add_loss() is only valid in the {LOSS_TERM!r} phase "
                f"(called in {self.phase!r})"
            )
        self._record["loss_terms"].append(term)

    def parameter(self, name, init):
        """An operator-owned scalar parameter, trained by the objective.

        Created once per (seed, condition) run and registered into the optimizer with the
        model's own hyperparameters, so it is updated by the same optimizer, from the gradient
        of the same loss, as every other parameter. This is the only way an operator may carry
        a learnable quantity: a scalar advanced by hand-written arithmetic is a schedule, and
        the experiment would not be measuring what it registered.
        """

        owned = self.state.setdefault("_operator_parameters", {})
        if name not in owned:
            tensor = self.torch.tensor(
                float(init), device=self.target.device, dtype=self.target.dtype,
                requires_grad=True,
            )
            group = {k: v for k, v in self.optimizer.param_groups[0].items() if k != "params"}
            group["params"] = [tensor]
            self.optimizer.add_param_group(group)
            owned[name] = tensor
            self._record["parameters"].setdefault(name, {"received_gradient": False})
        return owned[name]

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


def _owning_module(model, target_name):
    """The module holding ``target_name`` and the attribute it holds it under."""

    path, _, attribute = target_name.rpartition(".")
    module = model.get_submodule(path) if path else model
    if attribute not in getattr(module, "_parameters", {}):
        raise KeyError(
            f"{target_name!r} is not a direct parameter of {type(module).__name__}; "
            "the harness cannot reparameterize it"
        )
    return module, attribute


def check_conformance(realized, registered_phases, *, learns_parameters=False):
    """Compare what the operator DID against what the protocol registered.

    ``realized`` is the per-condition summary the driver builds. This is the layer that was
    missing: reproducibility proved the archived program reproduces its archived numbers, and
    nothing proved the archived program performs the registered intervention.
    """

    registered = [phase for phase in PHASES if phase in set(registered_phases or ())]
    problems = []
    proposed = realized.get("proposed")
    if proposed is None:
        return problems  # no proposed arm in this run (not a registered-report execution)
    if registered:
        missing = [phase for phase in registered if phase not in proposed["phases"]]
        extra = [phase for phase in proposed["phases"] if phase not in registered]
        if missing:
            problems.append(
                f"the proposed arm never acted in registered phase(s) {missing}; the "
                "experiment did not perform the intervention it preregistered"
            )
        if extra:
            problems.append(
                f"the proposed arm acted in unregistered phase(s) {extra}; the experiment "
                "performed an intervention it did not preregister"
            )
    if learns_parameters:
        parameters = proposed["parameters"]
        if not parameters:
            problems.append(
                "the protocol registers an operator-owned learnable parameter but the operator "
                "created none via ctx.parameter()"
            )
        ungraded = sorted(n for n, info in parameters.items() if not info["received_gradient"])
        if ungraded:
            problems.append(
                f"operator parameter(s) {ungraded} never received a gradient from the "
                "objective, so they were not learned by the experiment"
            )
    for condition, summary in sorted(realized.items()):
        if condition.startswith("baseline_") and summary["phases"]:
            problems.append(
                f"the comparator arm {condition!r} acted in {summary['phases']}; the "
                "registered comparator is the same program with the operator applying no "
                "modification, so the contrast is not the operator alone"
            )
        problems.extend(summary["violations"])
    return problems


def run_experiment(
    results_dir,
    *,
    testbed,
    apply_operator,
    seed_ids,
    replication_seed_ids,
    required_condition_ids,
    target_name,
    registered_phases=(),
    learns_parameters=False,
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
    realized = {}
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
                accuracy, curve, activations, record = _train_one_condition(
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
                _merge_conformance(realized, condition, record)

        result[cohort_name] = {
            "seed_ids": cohort_ids,
            "conditions": metrics,
            "curves": {
                condition: {
                    series: mean_curves([per_seed[series] for per_seed in curves[condition]])
                    for series in (CURVE_SERIES, testbed.OUTCOME_NAME)
                }
                for condition in conditions
            },
            # Steps on which the operator changed the target, its momentum buffer, the forward
            # pass or the objective, per seed. All zero for an arm means the operator never
            # fired in that arm.
            "operator_activations": operator_activations,
        }

    problems = check_conformance(
        realized, registered_phases, learns_parameters=learns_parameters
    )
    if problems:
        raise ConformanceError(
            "the executed operator does not realize the registered protocol: "
            + "; ".join(problems)
        )
    result["conformance"] = {
        "registered_phases": [p for p in PHASES if p in set(registered_phases or ())],
        "learns_parameters": bool(learns_parameters),
        "realized": {
            condition: {
                "phases": summary["phases"],
                "parameters": summary["parameters"],
            }
            for condition, summary in sorted(realized.items())
        },
    }

    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, "results.json"), "w") as handle:
        json.dump(result, handle, indent=2)
    return result


def _merge_conformance(realized, condition, record):
    """Fold one (seed, condition) run's record into the per-condition summary."""

    summary = realized.setdefault(
        condition, {"phases": [], "parameters": {}, "violations": []}
    )
    for phase in PHASES:
        if phase in record["phases"] and phase not in summary["phases"]:
            summary["phases"].append(phase)
    summary["phases"].sort(key=PHASES.index)
    for name, info in record["parameters"].items():
        merged = summary["parameters"].setdefault(name, {"received_gradient": False})
        merged["received_gradient"] = merged["received_gradient"] or info["received_gradient"]
    for violation in record["violations"]:
        if violation not in summary["violations"]:
            summary["violations"].append(violation)


def _new_record():
    return {
        "phases": set(),
        "parameters": {},
        "violations": [],
        "reparameterization": None,
        "loss_terms": [],
    }


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
    owner, attribute = _owning_module(model, target_name)

    optimizer = testbed.build_optimizer(model)
    # The operator's randomness is its own, so it cannot shift the training stream and
    # unpair the conditions. Two views of the SAME dedicated stream: numpy for scalar
    # decisions, and a torch generator on the training device for tensor-valued draws.
    operator_seed = (int(seed) * 2_654_435_761 + 1_013_904_223) % (2**31 - 1)
    operator_rng = np.random.default_rng(operator_seed)
    operator_generator = torch.Generator(device=device)
    operator_generator.manual_seed(operator_seed)

    curve = []
    outcome_curve = []
    total_steps = len(shared["batches"])
    # One scratch dict for the whole run: the operator's carried state (a threshold fixed at
    # initialisation, a counter) has to outlive the per-step context object.
    operator_state = {}
    run_record = {"phases": set(), "parameters": {}, "violations": []}
    # How often the operator actually changed something. An operator whose activation condition
    # is never met makes its arm bit-identical to the comparator, and the run then LOOKS like a
    # clean null while having measured nothing at all. Counting here turns that from a mystery
    # inferred off identical metrics into a recorded fact.
    activations = 0

    def context(phase, step, epoch, record):
        return OperatorContext(
            condition=condition, phase=phase, step=step, epoch=epoch,
            total_steps=total_steps, model=model, optimizer=optimizer, target=target,
            target_name=target_name,
            momentum_buffer=optimizer.state.get(target, {}).get("momentum_buffer"),
            rng=operator_rng, torch=torch, state=operator_state,
            _generator=operator_generator, _record=record,
        )

    for index, (epoch, batch_index) in enumerate(shared["batches"]):
        record = _new_record()
        acted = False

        # --- pre_forward: a differentiable reparameterization, never an in-place write ------
        clean = target.detach().clone()
        apply_operator(context(PRE_FORWARD, index, epoch, record))
        if not torch.equal(clean, target.detach()):
            record["violations"].append(
                f"the operator wrote to the base parameter {target_name!r} during the "
                f"{PRE_FORWARD!r} phase; a transient perturbation must be expressed with "
                "ctx.reparameterize(fn) so the base weights, the optimizer update and the "
                "held-out evaluation stay clean"
            )
            with torch.no_grad():
                target.copy_(clean)
        reparameterization = record["reparameterization"]
        installed = False
        if reparameterization is not None:
            substitute = reparameterization(target)
            if not torch.is_tensor(substitute) or substitute.shape != target.shape:
                raise ConformanceError(
                    "ctx.reparameterize(fn) must return a tensor with the target's shape "
                    f"{tuple(target.shape)}"
                )
            del owner._parameters[attribute]
            owner.__dict__[attribute] = substitute
            installed = True
            record["phases"].add(PRE_FORWARD)
            acted = True

        try:
            # --- the forward pass and the objective ---------------------------------------
            loss = testbed.forward_loss(model, optimizer, data, shared, epoch, batch_index, device)
            reported = float(loss.detach().cpu())

            # --- loss_term: added inside the autograd graph, before backward ---------------
            apply_operator(context(LOSS_TERM, index, epoch, record))
            for term in record["loss_terms"]:
                if torch.is_tensor(term) and term.requires_grad:
                    record["phases"].add(LOSS_TERM)
                    acted = True
                elif condition == "proposed":
                    record["violations"].append(
                        "the operator added a loss term that carries no gradient, so it "
                        "cannot change the optimization; build the term from ctx.parameter() "
                        "or from the target itself"
                    )
                loss = loss + term

            loss.backward()
        finally:
            # Restore the base parameter before the optimizer step, always. Its gradient — the
            # gradient of the loss the reparameterized forward produced — is what the standard
            # update then applies to the clean weights.
            if installed:
                owner.__dict__.pop(attribute, None)
                owner._parameters[attribute] = target

        for name, tensor in operator_state.get("_operator_parameters", {}).items():
            info = record["parameters"].setdefault(name, {"received_gradient": False})
            grad = tensor.grad
            if grad is not None and bool(torch.isfinite(grad).all()) and bool((grad != 0).any()):
                info["received_gradient"] = True

        optimizer.step()

        # --- post_step: persistent modification of what the update just produced -----------
        before_target = target.detach().clone()
        buffer = optimizer.state.get(target, {}).get("momentum_buffer")
        before_buffer = buffer.detach().clone() if buffer is not None else None
        apply_operator(context(POST_STEP, index, epoch, record))
        changed = not torch.equal(before_target, target.detach())
        if not changed and before_buffer is not None:
            buffer = optimizer.state.get(target, {}).get("momentum_buffer")
            changed = buffer is not None and not torch.equal(before_buffer, buffer)
        if changed:
            record["phases"].add(POST_STEP)
            acted = True

        activations += int(acted)
        run_record["phases"].update(record["phases"])
        for name, info in record["parameters"].items():
            merged = run_record["parameters"].setdefault(name, {"received_gradient": False})
            merged["received_gradient"] = merged["received_gradient"] or info["received_gradient"]
        for violation in record["violations"]:
            if violation not in run_record["violations"]:
                run_record["violations"].append(violation)

        if index % max(1, total_steps // testbed.CURVE_SAMPLES) == 0 or index == total_steps - 1:
            curve.append([index, reported])
            # The OUTCOME over training, not only the loss. A results section's learning curve
            # is meant to show the reported metric developing; logging only a loss meant the
            # only way to have a curve "for the primary metric" was to file the loss under its
            # name, which is exactly the false axis this pass removed. `evaluate` is a
            # deterministic no_grad pass over a fixed-order held-out cohort that restores train
            # mode, so it draws nothing from the training stream and the conditions stay paired.
            outcome_curve.append([index, float(testbed.evaluate(model, data, device))])

    # Evaluation reads the parameters the optimizer produced. A pre_forward reparameterization
    # is never written back, so "the evaluated weights carry no residual perturbation" holds by
    # construction rather than by inspection.
    accuracy = testbed.evaluate(model, data, device)
    run_record["phases"] = [p for p in PHASES if p in run_record["phases"]]
    return accuracy, {CURVE_SERIES: curve, testbed.OUTCOME_NAME: outcome_curve}, activations, run_record
