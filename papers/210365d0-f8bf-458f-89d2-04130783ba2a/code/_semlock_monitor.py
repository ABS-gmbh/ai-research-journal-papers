"""SemLock runtime monitor. Server-owned; staged into every harness bundle beside ``_harness.py``.

The harness records WHICH lifecycle phases the operator acted in (``check_conformance``). What
it never observed — ``app/experiment/harness/comparator.py`` lists it as deliberately not
enforced — is everything else an operator can reach: model parameters other than the
registered target, optimizer state other than that target's momentum buffer, the optimizer's
hyperparameters, the global random streams, and whether training depends on the held-out
cohort. Each is a way for code that passes every phase check to perform a different experiment
from the one registered:

* writing a non-target parameter, or adding a loss term or reparameterization whose gradient
  reaches one, changes WHAT is intervened on (scope);
* drawing from a global stream couples the arms' randomness (pairing);
* a training trajectory that changes when only the held-out cohort changes is leakage (split;
  that probe lives in ``_harness.heldout_isolation_probe`` because it needs whole runs).

This module observes those properties and returns a record; the verdict is the server's
(``app/semlock/runtime_checks.py``). It never changes a value the run computes: it reads
version counters, RNG states and detached copies, and computes gradients with
``torch.autograd.grad``, which accumulates into nothing. A run with and without the monitor
produces bit-identical results (``tests/test_semlock_runtime.py``).

Coverage is stated, not implied. On every operator call: version counters of every other
parameter, the optimizer's hyperparameters and its other momentum buffers, and the torch
random streams. On sampled steps — the first ``FULL_CHECK_STEPS`` of every (seed, condition)
run, every ``FULL_CHECK_STRIDE``-th after that, and EVERY step of a smoke run — additionally
value comparisons of every other parameter (which catches a write through ``.data``), the
NumPy and Python global streams, parameter-inventory changes and the gradient footprints. A
``.data`` write on an unsampled step of a full run is therefore NOT observed; the record
carries the counts so the server can say exactly what was checked.

Imports nothing at module level, like ``_harness.py``, so it stays importable without torch.
"""

from __future__ import annotations

FULL_CHECK_STEPS = 2
FULL_CHECK_STRIDE = 50
MAX_EVENTS = 8
FINGERPRINT_POINTS = 16
RECORD_VERSION = 1

PRE_FORWARD = "pre_forward"
LOSS_TERM = "loss_term"
POST_STEP = "post_step"

_EVENT_KEYS = (
    "foreign_mutations",
    "foreign_optimizer_state",
    "optimizer_hyperparameters",
    "structure_changes",
    "global_rng_draws",
    "gradient_footprint",
    "detached_reparameterization",
)
_COUNT_KEYS = ("calls", "full_checks", "footprint_checks", "stochastic_calls")


def _add_event(summary, key, event):
    events = summary[key]
    if len(events) < MAX_EVENTS and event not in events:
        events.append(event)


def _freeze(value):
    if isinstance(value, (bool, int, float, str, type(None))):
        return value
    return repr(value)


def _python_random_state():
    import random

    return random.getstate()


def _numpy_global_state():
    try:
        import numpy as np
    except ImportError:  # pragma: no cover - numpy ships in every experiment image
        return None
    state = np.random.get_state()
    return (state[0], state[1].tobytes(), state[2], state[3], state[4])


def tensor_stats(torch, delta, reference):
    """Scale-free summary of a change. Deterministic for a deterministic operator."""

    delta = delta.detach().double().flatten()
    reference = reference.detach().double().flatten()
    ref_norm = float(reference.norm())
    delta_norm = float(delta.norm())
    cos = 0.0
    if ref_norm > 0 and delta_norm > 0:
        cos = float(torch.dot(delta, reference) / (delta_norm * ref_norm))
    return {
        "rel_norm": delta_norm / ref_norm if ref_norm > 0 else delta_norm,
        "mean": float(delta.mean()) if delta.numel() else 0.0,
        "std": float(delta.std()) if delta.numel() > 1 else 0.0,
        "cos": cos,
    }


def empty_record():
    return {
        "version": RECORD_VERSION,
        "runs": 0,
        **{key: 0 for key in _COUNT_KEYS},
        **{key: [] for key in _EVENT_KEYS},
        "fingerprint": None,
    }


class OperatorMonitor:
    """Observes the operator calls of one (seed, condition) training run."""

    def __init__(
        self,
        *,
        torch,
        model,
        optimizer,
        target,
        target_name,
        operator_rng=None,
        operator_generator=None,
        smoke=False,
    ):
        self.torch = torch
        self.model = model
        self.optimizer = optimizer
        self.target = target
        self.target_name = target_name
        self.operator_rng = operator_rng
        self.operator_generator = operator_generator
        self.smoke = bool(smoke)
        # Held by reference: during loss_term the target is swapped out of its module's
        # _parameters, so named_parameters() would not list it; these lists never change.
        self._others = [
            (name, parameter)
            for name, parameter in model.named_parameters()
            if parameter is not target
        ]
        self._other_names = {id(parameter): name for name, parameter in self._others}
        self._inventory = frozenset(name for name, _ in model.named_parameters()) - {target_name}
        self._initial_groups = len(optimizer.param_groups)
        self.summary = {
            "version": RECORD_VERSION,
            **{key: 0 for key in _COUNT_KEYS},
            **{key: [] for key in _EVENT_KEYS},
            "fingerprint": {},
        }

    # --- sampling policy ------------------------------------------------------------------ #

    def full(self, step):
        return self.smoke or step < FULL_CHECK_STEPS or step % FULL_CHECK_STRIDE == 0

    # --- snapshots ------------------------------------------------------------------------- #

    def _hyperparameters(self):
        return tuple(
            tuple((key, _freeze(group[key])) for key in sorted(group) if key != "params")
            for group in self.optimizer.param_groups[: self._initial_groups]
        )

    def _optimizer_state(self, full):
        state = {}
        for parameter, slots in self.optimizer.state.items():
            if id(parameter) not in self._other_names or not isinstance(slots, dict):
                continue
            buffer = slots.get("momentum_buffer")
            if buffer is None:
                continue
            state[id(parameter)] = (
                id(buffer),
                buffer._version,
                buffer.detach().clone() if full else None,
            )
        return state

    def _rng_state(self, full):
        torch = self.torch
        state = {"torch_cpu": torch.get_rng_state()}
        if torch.cuda.is_available() and torch.cuda.is_initialized():
            state["torch_cuda"] = torch.cuda.get_rng_state()
        if full:
            state["numpy_global"] = _numpy_global_state()
            state["python_random"] = _python_random_state()
        return state

    def _operator_stream(self):
        stream = []
        if self.operator_generator is not None:
            stream.append(self.operator_generator.get_state())
        if self.operator_rng is not None:
            stream.append(repr(self.operator_rng.bit_generator.state))
        return stream

    def _snapshot(self, full):
        return {
            "full": full,
            "versions": [parameter._version for _, parameter in self._others],
            "values": (
                [parameter.detach().clone() for _, parameter in self._others] if full else None
            ),
            "hyperparameters": self._hyperparameters(),
            "optimizer_state": self._optimizer_state(full),
            "rng": self._rng_state(full),
            "operator_stream": self._operator_stream(),
        }

    # --- monitored calls ------------------------------------------------------------------- #

    def call(self, apply_operator, ctx, *, phase, step):
        """Invoke ``apply_operator(ctx)`` and record what it touched besides its target."""

        target_before = (
            self.target.detach().clone() if self.smoke and phase == POST_STEP else None
        )
        self.invoke(apply_operator, ctx, phase=phase, step=step)
        if target_before is not None and not self.torch.equal(target_before, self.target.detach()):
            self._fingerprint(
                phase,
                step,
                tensor_stats(self.torch, self.target.detach() - target_before, target_before),
            )

    def invoke(self, function, *args, phase, step):
        """Call ``function(*args)`` under observation; return its result.

        Used for the operator itself and for a ``pre_forward`` reparameterization, which the
        harness evaluates AFTER the operator returns — anything that function touches is the
        operator's doing too.
        """

        full = self.full(step)
        before = self._snapshot(full)
        result = function(*args)
        self.summary["calls"] += 1
        if full:
            self.summary["full_checks"] += 1
        self._compare(before, phase=phase, step=step)
        return result

    def _compare(self, before, *, phase, step):
        torch = self.torch
        step = int(step)
        for index, (name, parameter) in enumerate(self._others):
            changed = parameter._version != before["versions"][index]
            kind = "in-place write"
            if not changed and before["values"] is not None:
                changed = not torch.equal(before["values"][index], parameter.detach())
                kind = "value change"
            if changed:
                _add_event(
                    self.summary,
                    "foreign_mutations",
                    {"name": name, "phase": phase, "step": step, "kind": kind},
                )
        if self._hyperparameters() != before["hyperparameters"]:
            _add_event(self.summary, "optimizer_hyperparameters", {"phase": phase, "step": step})
        after_state = self._optimizer_state(before["full"])
        for key, (buffer_id, version, values) in before["optimizer_state"].items():
            current = after_state.get(key)
            changed = current is None or current[0] != buffer_id or current[1] != version
            if not changed and values is not None and current[2] is not None:
                changed = not torch.equal(values, current[2])
            if changed:
                _add_event(
                    self.summary,
                    "foreign_optimizer_state",
                    {"name": self._other_names.get(key, "?"), "phase": phase, "step": step},
                )
        if before["full"]:
            inventory = frozenset(name for name, _ in self.model.named_parameters()) - {
                self.target_name
            }
            if inventory != self._inventory:
                _add_event(
                    self.summary,
                    "structure_changes",
                    {
                        "phase": phase,
                        "step": step,
                        "added": sorted(inventory - self._inventory)[:4],
                        "removed": sorted(self._inventory - inventory)[:4],
                    },
                )
        rng_after = self._rng_state(before["full"])
        for stream, state in before["rng"].items():
            current = rng_after.get(stream)
            if stream.startswith("torch"):
                same = current is not None and torch.equal(state, current)
            else:
                same = state == current
            if not same:
                _add_event(
                    self.summary,
                    "global_rng_draws",
                    {"stream": stream, "phase": phase, "step": step},
                )
        stream_after = self._operator_stream()
        for previous, current in zip(before["operator_stream"], stream_after, strict=False):
            moved = (
                not torch.equal(previous, current)
                if torch.is_tensor(previous)
                else previous != current
            )
            if moved:
                self.summary["stochastic_calls"] += 1
                break

    # --- gradient footprints --------------------------------------------------------------- #

    def _foreign_gradient(self, output, *, step, phase, grad_outputs=None):
        parameters = [parameter for _, parameter in self._others]
        if not parameters:
            return
        gradients = self.torch.autograd.grad(
            output,
            parameters,
            grad_outputs=grad_outputs,
            retain_graph=True,
            allow_unused=True,
        )
        self.summary["footprint_checks"] += 1
        foreign = sorted(
            name
            for (name, _), gradient in zip(self._others, gradients, strict=False)
            if gradient is not None and bool((gradient != 0).any())
        )
        if foreign:
            _add_event(
                self.summary,
                "gradient_footprint",
                {"phase": phase, "step": int(step), "foreign": foreign[:6]},
            )

    def loss_terms(self, terms, *, step):
        """``loss_term``: which parameters the objective the operator added would train."""

        torch = self.torch
        graded = [term for term in terms if torch.is_tensor(term) and term.requires_grad]
        if not graded:
            return
        total = graded[0]
        for term in graded[1:]:
            total = total + term
        if total.numel() != 1:
            return  # the harness's own backward() reports a non-scalar objective
        if self.smoke:
            target_gradient = torch.autograd.grad(
                total, [self.target], retain_graph=True, allow_unused=True
            )[0]
            self._fingerprint(
                LOSS_TERM,
                step,
                {
                    "value": float(total.detach()),
                    "target_grad_norm": (
                        0.0 if target_gradient is None else float(target_gradient.norm())
                    ),
                },
            )
        if self.full(step):
            self._foreign_gradient(total, step=step, phase=LOSS_TERM)

    def reparameterization(self, substitute, *, step):
        """``pre_forward``: what the tensor the forward pass will see depends on."""

        torch = self.torch
        if not substitute.requires_grad:
            # The target then receives no gradient this step: it is frozen, not reparameterized.
            _add_event(self.summary, "detached_reparameterization", {"step": int(step)})
        elif self.full(step):
            self._foreign_gradient(
                substitute,
                step=step,
                phase=PRE_FORWARD,
                grad_outputs=torch.ones_like(substitute),
            )
        if self.smoke:
            self._fingerprint(
                PRE_FORWARD,
                step,
                tensor_stats(torch, substitute.detach() - self.target.detach(), self.target),
            )

    # --- fingerprint ----------------------------------------------------------------------- #

    def _fingerprint(self, phase, step, stats):
        series = self.summary["fingerprint"].setdefault(phase, [])
        if len(series) < FINGERPRINT_POINTS:
            series.append({"step": int(step), **{key: float(v) for key, v in stats.items()}})


def merge(records, condition, summary):
    """Fold one (seed, condition) monitor summary into the per-condition record."""

    merged = records.setdefault(condition, empty_record())
    merged["runs"] += 1
    for key in _COUNT_KEYS:
        merged[key] += int(summary.get(key, 0))
    for key in _EVENT_KEYS:
        for event in summary.get(key, []):
            _add_event(merged, key, event)
    # The fingerprint of the FIRST run of each condition only: every condition's first run
    # shares one seed's initialization and batch order, so fingerprints are comparable across
    # arms and across code versions; later seeds would only add noise to that comparison.
    if merged["fingerprint"] is None and summary.get("fingerprint"):
        merged["fingerprint"] = summary["fingerprint"]
    return merged
