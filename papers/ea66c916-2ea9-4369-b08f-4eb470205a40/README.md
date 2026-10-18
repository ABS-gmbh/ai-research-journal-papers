# Replication: Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers

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


- **Random seeds:** `{'primary': [1283456944311395052, 3089827065251130706, 3820704350825163869, 21236671524869010, 3415510045131152228, 2471081763373673405, 2374229508893286820, 2544941384231390184, 1567606677881050665, 2053777282625161573, 1221184456753876155, 3840525734538224513, 3504834781713389789, 77032002028652062, 4286278862225646279, 52245002576694452, 3986941535421188655, 4071087587955586190, 3260374718512374155, 4461885864847931220, 491323389332414539, 496860537829936944, 1932727500076940062, 3540548724348848006, 2513328952985036215, 609131993201635141, 4204928448906752539, 170530799314395416, 4086858104574164556, 2837886427063813598, 524975045864782648, 1034243053804099323, 2213998415094885164, 4277462776836849410, 369187523183942457, 2922011945439219839, 4356023442558125597, 3546063947330525743, 823309675197582790, 2178248810602791538, 1462835975243560544, 3406899122066815415, 2216116664296627259], 'replication': [977459171940437340, 4488684769213213828, 1946600601137041155, 3416445909951360620, 94015168479249032, 245818450391945052, 4163063857117823088, 2717512241999814344, 3272748125613112133, 2370826470989774210, 1246227564208053654, 1763313708890820020, 4237763328141452310, 189961628016980323, 3945708179936401034, 469354882092208534, 2362016536193918241, 159255973982391164, 4365608024907845659, 387604714248465277, 745895122294483880, 46716666623954822, 4499449375448926851, 3008410952988380379, 2884677716462523534, 989949122925515117, 778369360471311952, 2224210984340661255, 2176941969250537915, 3008498851693170318, 2776754912777002994, 1890870248134977771, 882560239534186207, 297046870819713949, 1418335113356987113, 1214865161567177267, 4237397377132919006, 1869765722857981507, 448793344464843120, 1346906245604336130, 816203111240928895, 1477596452365914441, 4367633781936564098]}`
- **compute job id:** `16678400`
- **Partition:** `[redacted]`
- **Container image:** `pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`
- **Apptainer SIF SHA-256:** `b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e`
- **Preregistration SHA-256:** `3fa882f2397b6cfcac4afc254478687fa882ff6d9edcc3f13db71ad8f246bdd5`
- **Preregistration anchor commit:** `bea539157523b78270c8035380f0740f7d4c8695`

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

## Public history rewrite (2026-11-16)

This repository's history was rewritten on 2026-11-16 to remove the journal's platform source
code and prompts, which are not open source. Files and records are otherwise unchanged, and
author dates and messages are preserved. Commit identifiers recorded inside files before that
date (for example the preregistration anchor commit above) name commits of the ORIGINAL
history, which the journal keeps privately; `HISTORY_REWRITE.json` at the repository root maps
each original commit to its rewritten counterpart.
