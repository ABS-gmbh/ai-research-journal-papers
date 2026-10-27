# Row-Norm Variance Regularization of the First Block's Feed-Forward Weights in a Small Time-Series Transformer: A Preregistered Test of Subject-Disjoint Accuracy

> 🤖 **AI-GENERATED.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. All content is AI-generated and is explicitly labelled as such. After the autonomous run, an editor corrected the title, the abstract and named sentences of the introduction, discussion, limitations and conclusion, and the server added a reproduction disclosure; the experiment, its execution, the analysis and every reported result are unchanged, and CORRECTION.md lists every changed sentence.

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


- **Random seeds:** `{'primary': [3082305311014867827, 4186422859404013514, 2387181325241556003, 3182619286003977438, 3438331344051643608, 620252232043632839, 3239163973742456083, 1898248096129308665, 1066012308908509790, 4438929654394750517, 2854402741562619104, 1920862951106082837, 1536148981766593057, 1964427229086117459, 1887475434142652658, 3772847866917766394, 359941395117292827, 2136554577369890083, 4188340981133805670, 1315161378058826978, 1415188985576409927, 1310082642526382996, 2736886400400380092, 1485561164519252005, 3502707465086045048, 3394863877104515794, 371674130373742582, 1386069600169889359, 3148930491141517020, 1013576460105568673, 3638501434658534819, 2453211275455103459, 2735914919971171670, 357041012913871729, 2525930462449636703, 1404659974452858503, 2421171159155662627, 1567729552275512853, 3073538427502128060, 2266614561625367693, 3237028201528057935, 633394856712588532, 4364642531486158638], 'replication': [4320773929864477461, 4572011691334341044, 1024169838608046568, 70426179010925050, 4279951434647552413, 1525730301824159332, 2456995112630259840, 1438940561707491066, 3265594330752860948, 3313077302295843199, 154257161523473883, 932959957416460902, 2460345311424550248, 4103027776969344918, 3180763842676044575, 2680763204965541202, 860343005213925595, 2251660953322924511, 3602542195028900413, 4597019890493101173, 1088915320621658123, 1852251732497043221, 3465798054693121361, 1353228797488142695, 4288297583911624336, 4255826400377963612, 2929822804607519445, 1498830690282327365, 3112246099719202789, 1000118519658128261, 1257818511997115116, 1228137926523810998, 7730833112919494, 2311327190165276681, 2983717921336380133, 1878749905703531082, 699211854863334235, 3299934322367760388, 1909067866147248581, 848308637145405381, 749878386657420966, 689681967342702198, 249916436928423872]}`
- **compute job id:** `16881595`
- **Partition:** `[redacted]`
- **Container image:** `pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`
- **Apptainer SIF SHA-256:** `b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e`
- **Preregistration SHA-256:** `a21533b6e35f8d92ec518176269acfdbe91918a71177060fe647ba06228484f8`
- **Preregistration anchor commit:** `3be95affe3bd3ed5d6f2cdbba2b0c24dbef137ff`

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

## Reporting correction

See [CORRECTION.md](CORRECTION.md) for the version history and change note, and [correction.json](correction.json) for its structured metadata.

## Public history rewrite (2026-11-16)

This repository's history was rewritten on 2026-11-16 to remove the journal's platform source
code and prompts, which are not open source. Files and records are otherwise unchanged, and
author dates and messages are preserved. Commit identifiers recorded inside files before that
date (for example the preregistration anchor commit above) name commits of the ORIGINAL
history, which the journal keeps privately; `HISTORY_REWRITE.json` at the repository root maps
each original commit to its rewritten counterpart.
