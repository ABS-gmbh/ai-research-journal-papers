# Spectral Entropy Minimization of Input Projections for Temporal Feature Learning

> 🤖 **AI-GENERATED.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. After the autonomous run, the text was corrected at the direction of the journal's editor; the correcting text was drafted by an AI assistant (Claude, Anthropic), not written by a human: the correction revised sentences in the Abstract, Introduction, Related Work, Method, Experimental Setup, Results, Discussion, Limitations and Conclusion, added two paragraphs to the Method, and corrected the reference list. Apart from these changes and this disclosure, the text is as the autonomous system produced it, and the experiment, its execution, the analysis and every reported result are unchanged. CORRECTION.md lists every changed sentence.

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
  listed in [`PLATFORM_COMPONENTS.sha256`](PLATFORM_COMPONENTS.sha256). The platform is not open source, so their text is not published.
- **Prompts:** every message the platform sent to a model is replaced in `trace.json` by the
  SHA-256 of the original text, and so is the model provider's reasoning, which restates those
  messages; the model's answers, decisions, usage and timings are unchanged.

An independent re-run is performed by the journal from its private archive of the complete original code; when one has run, its result
is reported in `VERIFICATION.md`. Reproducing the experiment outside the journal requires the
platform components, so contact the journal to arrange it.

- **Entrypoint module:** `experiment`
- **Run arguments:** recorded in `metadata.json` and `reproduction.json`
- **Datasets:** `uci_har_smartphones` (sha256 `c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031`)
- **Random seeds:** `{'primary': [2123072646313131395, 2876870697341558572, 1626188215202879716, 1510276966388459924, 731046012090665773, 3260383066045027195, 3095946781025322130, 4381965775545884727, 2805598060171360936, 1017958683207416740, 4042020326231746635, 4023539511489529628, 1871502529958763706, 2254279501808974253, 1144235192351947965, 3712892738658554895, 3406089707180909076, 4440012577721720143, 3980041306974201770, 3346735451993638316, 865312341983968708, 2639610289791772578, 1334636369082240328, 2743053750536161936, 2454452483814521952, 4376507013480164420, 3378328928367937002, 2235759430064723176, 335095552699722741, 3582843840639648566, 1697868845032105404, 2064913684831631250, 558052755835398650, 2501126167359087503, 2998282804321717818, 3159482636166201431, 4144105613280466035, 328700485333559270, 3987679676988384734, 1291110757824769602, 4442649950213859983, 54147398821064359, 1514398810589347120], 'replication': [2760814681199202148, 4276509618210360377, 4507730695268138586, 1775243207192301356, 4402558683031212456, 1914937847910204359, 4447932364116798623, 3266695852116340762, 2639495877875133721, 684166292893318705, 763076020713057821, 2284212100604222399, 623189800426898552, 1123976993867976454, 4384758150021590169, 4172343417179275050, 4013643719985881790, 3322921880621971031, 4392335637682857782, 1139371421315206809, 1501434226905974955, 1402960692633542134, 1690201651464576548, 784607708796821782, 4022028640566973239, 1679480667235915961, 1260732336854904037, 1879607340802654956, 3030884773609833226, 658532294107441849, 1198846548640802872, 524796093625990818, 620846012044359089, 3920508414082679309, 731968606963389284, 3744371430145846942, 3914696473985276147, 983119102059608204, 3521400878800560280, 1161765677263725251, 4540894300136491864, 2010139038338001362, 165483925685987617]}`
- **compute job id:** `15688229`
- **Partition:** `[redacted]`
- **Container image:** `pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`
- **Apptainer SIF SHA-256:** `b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e`
- **Preregistration SHA-256:** `a0416c6b505389511bdee9a5c532d8bad40df6418af680a7c65f2c575c531ec0`
- **Preregistration anchor commit:** `2c246d256841579152aa0d95a81805b9c14e2653`

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
