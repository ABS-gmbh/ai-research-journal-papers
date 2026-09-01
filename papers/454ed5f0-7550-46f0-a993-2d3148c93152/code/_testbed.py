"""Server-owned data + model for ``uci_har_small_transformer_v1``.

Ported from the committed, human-reviewed ``CALIBRATION_SOURCES`` entry that produced this
testbed's registered baseline on an A100 (the scheduler 15446009). Keeping it here — rather than asking
the generator to re-derive it from the recipe's prose — is the whole point of the harness: the
archive's member layout, the per-channel standardisation axis and the parameter names in
``operator_targets`` are facts this server already knows, and every one of them has cost either
a codegen attempt or a GPU job when a model guessed at it instead.

The cohorts are parsed once per process: np.loadtxt over 18 signal files dominates a short run
and the arrays are identical every time, so per-seed determinism is unaffected.
"""

from __future__ import annotations

DATASET_NAME = "uci_har_smartphones"
OUTCOME_NAME = "held-out classification accuracy"

SEQ_LEN = 128
CHANNELS = 9
CLASSES = 6
D_MODEL = 64
N_HEAD = 4
N_LAYERS = 2
D_FF = 128
EPOCHS = 12
BATCH_SIZE = 128
LR = 0.05
MOMENTUM = 0.9

SMOKE_BATCH_SIZE = 8
SMOKE_STEPS = 3
CURVE_SAMPLES = 12

#: The model's full parameter inventory, as the recipe's ``operator_targets`` names them. The
#: runtime checks the built model against this before training, so a naming drift fails in the
#: dry-run with a precise message instead of as a KeyError inside a GPU job.
PARAMETER_SHAPES = {
    "input_proj.weight": (D_MODEL, CHANNELS),
    "blocks.0.attn.q_proj.weight": (D_MODEL, D_MODEL),
    "blocks.0.attn.out_proj.weight": (D_MODEL, D_MODEL),
    "blocks.0.fc1.weight": (D_FF, D_MODEL),
    "blocks.1.attn.q_proj.weight": (D_MODEL, D_MODEL),
    "blocks.1.attn.out_proj.weight": (D_MODEL, D_MODEL),
    "blocks.1.fc1.weight": (D_FF, D_MODEL),
}

_CHANNEL_NAMES = (
    "body_acc_x", "body_acc_y", "body_acc_z",
    "body_gyro_x", "body_gyro_y", "body_gyro_z",
    "total_acc_x", "total_acc_y", "total_acc_z",
)
_CACHE = {}


def load_cohorts(dataset_path):
    """Read the official subject-disjoint split straight out of the staged archive.

    The container mounts the dataset read-only, so the nested zip is read through BytesIO
    rather than unpacked — the failure that killed compute job 15504724.
    """

    import io
    import zipfile

    import numpy as np

    if "data" in _CACHE:
        return _CACHE["data"]
    with zipfile.ZipFile(dataset_path) as outer:
        inner = zipfile.ZipFile(io.BytesIO(outer.read("UCI HAR Dataset.zip")))

    def _split(name):
        channels = []
        for channel in _CHANNEL_NAMES:
            member = f"UCI HAR Dataset/{name}/Inertial Signals/{channel}_{name}.txt"
            with inner.open(member) as handle:
                channels.append(np.loadtxt(handle, dtype=np.float32))
        features = np.stack(channels, axis=-1)
        with inner.open(f"UCI HAR Dataset/{name}/y_{name}.txt") as handle:
            labels = np.loadtxt(handle, dtype=np.int64) - 1
        return features, labels

    x_train, y_train = _split("train")
    x_test, y_test = _split("test")
    # Standardise per channel using TRAINING statistics only.
    mean = x_train.mean(axis=(0, 1), keepdims=True)
    sd = np.maximum(x_train.std(axis=(0, 1), keepdims=True), 1e-6)
    _CACHE["data"] = {
        "x_train": ((x_train - mean) / sd).astype(np.float32), "y_train": y_train,
        "x_test": ((x_test - mean) / sd).astype(np.float32), "y_test": y_test,
    }
    return _CACHE["data"]


def synthetic_cohorts():
    """Tiny in-memory stand-in with the real shapes/dtypes — the preflight sandbox stages
    no dataset, so the smoke path may never touch ``load_cohorts``."""

    import numpy as np

    rng = np.random.default_rng(0)
    return {
        "x_train": rng.standard_normal((32, SEQ_LEN, CHANNELS), dtype=np.float32),
        "y_train": rng.integers(0, CLASSES, size=32, dtype=np.int64),
        "x_test": rng.standard_normal((16, SEQ_LEN, CHANNELS), dtype=np.float32),
        "y_test": rng.integers(0, CLASSES, size=16, dtype=np.int64),
    }


def build_model():
    import math

    import torch

    class Attention(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.q_proj = torch.nn.Linear(D_MODEL, D_MODEL)
            self.k_proj = torch.nn.Linear(D_MODEL, D_MODEL)
            self.v_proj = torch.nn.Linear(D_MODEL, D_MODEL)
            self.out_proj = torch.nn.Linear(D_MODEL, D_MODEL)

        def forward(self, x):
            batch, steps, _ = x.shape
            head_dim = D_MODEL // N_HEAD

            def _heads(projection):
                return projection(x).view(batch, steps, N_HEAD, head_dim).transpose(1, 2)

            query, key, value = _heads(self.q_proj), _heads(self.k_proj), _heads(self.v_proj)
            scores = (query @ key.transpose(-2, -1)) / math.sqrt(head_dim)
            attended = torch.softmax(scores, dim=-1) @ value
            merged = attended.transpose(1, 2).reshape(batch, steps, D_MODEL)
            return self.out_proj(merged)

    class Block(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.ln1 = torch.nn.LayerNorm(D_MODEL)
            self.attn = Attention()
            self.ln2 = torch.nn.LayerNorm(D_MODEL)
            self.fc1 = torch.nn.Linear(D_MODEL, D_FF)
            self.fc2 = torch.nn.Linear(D_FF, D_MODEL)

        def forward(self, x):
            x = x + self.attn(self.ln1(x))
            return x + self.fc2(torch.relu(self.fc1(self.ln2(x))))

    class Encoder(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.input_proj = torch.nn.Linear(CHANNELS, D_MODEL)
            self.pos_embed = torch.nn.Parameter(torch.zeros(1, SEQ_LEN, D_MODEL))
            self.blocks = torch.nn.ModuleList([Block() for _ in range(N_LAYERS)])
            self.ln_f = torch.nn.LayerNorm(D_MODEL)
            self.head = torch.nn.Linear(D_MODEL, CLASSES)

        def forward(self, x):
            hidden = self.input_proj(x) + self.pos_embed
            for block in self.blocks:
                hidden = block(hidden)
            return self.head(self.ln_f(hidden).mean(dim=1))

    return Encoder()


def build_optimizer(model):
    import torch

    return torch.optim.SGD(model.parameters(), lr=LR, momentum=MOMENTUM)


def derive_seed_artifacts(seed, data, *, epochs, batch_size, max_steps=None):
    """Everything this seed's conditions SHARE, drawn once from the seed alone.

    Initial parameters and the full list of per-epoch batch permutations are computed here and
    reused by every condition, so the only difference within a seed's pair is the operator.
    """

    import torch

    torch.manual_seed(int(seed % (2**63 - 1)))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed % (2**63 - 1)))
    torch.use_deterministic_algorithms(True)

    init_state = {k: v.clone() for k, v in build_model().state_dict().items()}
    generator = torch.Generator(device="cpu").manual_seed(int(seed % (2**63 - 1)))
    count = len(data["x_train"])
    orders, batches = [], []
    for epoch in range(epochs):
        order = torch.randperm(count, generator=generator)
        orders.append(order)
        for batch_index, _start in enumerate(range(0, count, batch_size)):
            batches.append((epoch, batch_index))
    if max_steps is not None:
        batches = batches[:max_steps]
    return {
        "init_state": init_state, "orders": orders, "batches": batches,
        "batch_size": batch_size,
    }


def forward_loss(model, optimizer, data, shared, epoch, batch_index, device):
    """This step's classification objective, as a live autograd tensor.

    The backward pass and the optimizer step belong to the driver, not here: an operator may
    reparameterize the target for this forward pass or add a term to this objective, and both
    have to happen between the forward and the backward. Returning a float — which is what this
    function did while it also owned backward+step — made those interventions unrepresentable.
    """

    import torch

    batch_size = shared["batch_size"]
    order = shared["orders"][epoch]
    start = batch_index * batch_size
    ids = order[start:start + batch_size]
    xb = torch.from_numpy(data["x_train"])[ids].to(device)
    yb = torch.from_numpy(data["y_train"])[ids].to(device)
    optimizer.zero_grad(set_to_none=True)
    return torch.nn.functional.cross_entropy(model(xb), yb)


def evaluate(model, data, device):
    import numpy as np
    import torch

    model.eval()
    with torch.no_grad():
        predictions = []
        for start in range(0, len(data["x_test"]), 512):
            xb = torch.from_numpy(data["x_test"][start:start + 512]).to(device)
            predictions.append(model(xb).argmax(dim=1).cpu().numpy())
    model.train()
    correct = (np.concatenate(predictions) == data["y_test"]).sum()
    return float(correct / len(data["y_test"]))
