# Momentum-Orthogonal Projection Tests Whether Optimizer-State Geometry Improves Subject-Disjoint Generalization

> 🤖 **AI-GENERATED.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

This repository is the reproducibility bundle for an automatically generated research
paper: the study's own experiment code, SHA-256 digests of the platform components that ran,
the real results, run logs, random seeds, the compute job id, the agent's reasoning trace
(including failed attempts) and the paper itself (Markdown + PDF).

## Reproduction

The experiment was run by the journal on its own compute. This bundle publishes the parts of
the experiment that are specific to this study and identifies the rest by hash:

- **Public:** the generated operator (`code/operator_hook.py`), the run's protocol constants
  (`code/_protocol.py`), the recorded invocation (seeds, arguments, datasets, resources), the
  container image and its SHA-256, the results, the run logs and the agent's reasoning trace.
- **Identified by SHA-256 only:** the journal's own platform components (the experiment
  harness, the generic runner, the testbed, the runtime monitor and the harness wrapper),
  listed in [`PLATFORM_COMPONENTS.sha256`](PLATFORM_COMPONENTS.sha256) and in `reproduction.json`. The platform is not open source, so their text is not published.
- **Prompts:** every message the platform sent to a model is replaced in `trace.json` by the
  SHA-256 of the original text, and so is the model provider's reasoning, which restates those
  messages; the model's answers, decisions, usage and timings are unchanged.

An independent re-run is performed by the journal from the complete frozen input packet, which is archived privately (its SHA-256 is `packet_sha256` in `reproduction.json`); when one has run, its result
is reported in `VERIFICATION.md`. Reproducing the experiment outside the journal requires the
platform components, so contact the journal to arrange it.

- **Entrypoint module:** `experiment`
- **Run arguments:** recorded in `metadata.json` and `reproduction.json`
- **Datasets:** `uci_har_smartphones` (sha256 `c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031`)
- **Random seeds:** `{'primary': [3997813737653302303, 3309792543465967669, 898169320913783714, 3964896538127092764, 3171176783835818082, 2125254381612812340, 164463215743309073, 4607537401135060359, 4371816041976198247, 4375509884083495539, 56571881961416109, 3186175054496708162, 3135712612105761914, 2917419308223782333, 756296250425846271, 3664668516161228860, 1952755448443270368, 3643410946486515578, 3644367669275750018, 1309667764697542987, 1441715280992064684, 3511410770844740244, 4133809473348287269, 1725100179333995995, 1053041997813283501, 3088030652051418133, 4107816827218925227, 565566558421734252, 275805123457331965, 2680573877972736630, 157765648583704381, 4421031413392467556, 1552854591870605401, 2364009805729299393, 1904461708440649292, 1120772267680505117, 1092494605915433619, 2229838033419613320, 2059267624277869210, 510733906447812518, 1071007686057160105, 3808697128436486247, 4532370378841381999], 'replication': [2354976006981955819, 4324660935519791914, 831562771514012917, 2751327354233951026, 1512451331433289100, 2339623576096759615, 942097766754537929, 299423626648925212, 1613961540201361027, 2495779494466921665, 3286046173524442755, 1226876407126695882, 2822438373310273476, 3359112155736441787, 4589841592586339548, 2174476099861496296, 4400594877164728163, 1473987275448740522, 3560021299613277498, 1963134501751537655, 3857100197921599726, 1946187660472806283, 534240155361867711, 2257819899425946518, 1857067766385637398, 1542467500088558298, 2565902916065722756, 4469043849214490585, 2459162917649737361, 2486378516630103661, 285328054388411115, 2406669371174695006, 446452795583064019, 4179188943919088022, 493150260764163842, 3754155167337633593, 2778791489195799033, 1918504031098073709, 3156095766939290846, 1998442627702540335, 2669942370954230662, 427097415724880873, 1648269874916305333]}`
- **compute job id:** `17338534`
- **Partition:** `[redacted]`
- **Container image:** `docker.io/pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`
- **Apptainer SIF SHA-256:** `b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e`
- **Preregistration SHA-256:** `23c30c0abe523a9dfc9eae304ec9bd0cac7dfa83a1f6f4a717da364cfec2b467`
- **Preregistration anchor commit:** `3d0ad11bbdbe04409d0df78923e0a7ae53821e0f`

## Contents

| Path | What |
| --- | --- |
| `paper.md` / `paper.pdf` | the paper |
| `paper.json` | the structured paper (schema) |
| `code/` | the study's own code: the generated operator and the run's protocol constants |
| `PLATFORM_COMPONENTS.sha256` | SHA-256 of every platform component that ran (text not published) |
| `reproduction.json` | public form of the frozen inputs: invocation, container checksum, dataset inputs, the study's code, the SHA-256 of every code file, and the reference outputs |
| `REPRODUCTION_SOURCE.json` | the private archive of the complete frozen packet the journal re-runs from, and its checksum |
| `metrics.json` | the real results |
| declared `*.png` figures | every figure referenced by the paper, with available SVG copies |
| `seeds.json` | random seeds |
| `PREREGISTRATION.md` / `preregistration.json` | hypothesis + analysis plan, fixed before the experiment ran |
| `SEMANTIC_LOCK.md` / `semantic_contract.json` | the locked scientific contract and what was machine-verified against it |
| `EXPERIMENT_SELECTION.md` / `experiment_selection.json` | why this study was selected: its expected information and cost, and the prior evidence it responds to (fixed before the experiment ran) |
| `CLAIMS.md` / `claim_ledger.json` | every material claim in the paper, checked against the run's own records |
| `datasets.json` | staged dataset provenance (source, sha256, paths) |
| `logs/run.log` | compute run logs |
| `trace.json` | the agent's reasoning trace (incl. failures); platform prompts replaced by their SHA-256 |
| `metadata.json` | run id, job id, image, timings |
| `MANIFEST.sha256` | SHA-256 of every bundle file |
| `VERIFICATION.md` / `verification.json` | independent reproduction re-run report (if verified) |

## Staging provenance

Everything this study produced before the editor approved publication — the preregistration
anchor, committed before any experiment compute was submitted, and the frozen reproduction
inputs and reference outputs, committed before the independent re-run — was committed to the
journal's private staging repository, and nothing was public until this bundle was. The
preregistration files are copied here (`staging/preregistration/`); the frozen reproduction
packet stays private because it contains the platform's source, and `reproduction.json` is its
public form. 
[`STAGING_PROVENANCE.json`](STAGING_PROVENANCE.json) records the staging commit SHAs, the
timestamps GitHub assigned them, the SHA-256 of every staged file and when the first experiment
job was submitted, so the order of registration, compute and approval can be checked; those
commits stay private, so their timestamps are the journal's record of them rather than
something a reader can fetch.
