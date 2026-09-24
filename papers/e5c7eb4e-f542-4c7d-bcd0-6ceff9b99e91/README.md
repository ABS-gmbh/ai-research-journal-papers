# Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers

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


- **Random seeds:** `{'primary': [2615122547193570606, 252200600861128310, 634766601307347027, 2289833669515924996, 1075721894937126869, 2219905518708798979, 1472572688149772095, 3154489071090469597, 2567160067431731676, 375878476100283907, 3680443165500893007, 2412595240837917458, 2601790489635802822, 1913826313556203271, 710938911890137278, 4578385222592080447, 3998799165023144543, 3601994374998462166, 517409047000623439, 3812347621373549969, 3406080211412548461, 772595819596432589, 3615834778985602079, 1415494652153299218, 2062219541250864404, 142389970181333221, 4434070341016929754, 1135820606004933817, 3780975103128256366, 4407244770048434366, 4376044843392817728, 3255929081425547334, 3574102472552171439, 19016511533479923, 2933058706039751666, 3462839959629419857, 4607211731052019561, 2779871998158610606, 1485808255187976782, 3471275713396068135, 4429899216283540008, 1385236021301736380, 1330453660667172384], 'replication': [2340648136914159678, 4191649941990144526, 914975885928187538, 3493291245950488, 3092035777930482330, 3033986887553884854, 1948116001888441515, 3721334120068172834, 1629568842510008, 3605262731553156275, 3904049989082932630, 892823242471123166, 3725427329689760378, 3555864911429215929, 3606907749333550835, 2155528049710964782, 2789562881046154133, 1853921749424354694, 1745680992267274019, 841184256946095993, 3464957341317932123, 775787681821570599, 3309282745006621851, 146154474434366067, 2391332672707033902, 706889780011171718, 2426763361766452408, 3736121309580882765, 479020209906455928, 1963761814288298963, 2233713330617425866, 2745262338024609657, 2296843351460209463, 2142392810908805088, 1468658092695416100, 2052272999620538285, 3506933794820522738, 351506867199205715, 4557863017481180823, 2654635865597404598, 3394110221015017757, 3791841174141345598, 3513984727252394996]}`
- **compute job id:** `16152821`
- **Partition:** `[redacted]`
- **Container image:** `pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`
- **Apptainer SIF SHA-256:** `b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e`
- **Preregistration SHA-256:** `74440f5a36e0e5f2612524f1eae42c8ab490029cc32a18634ae6e1af274d0801`
- **Preregistration anchor commit:** `80ff8c2d68c28c765b1bbc35d7bf30e2b8ac042d`

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
| `metrics.png` | results figure |
| `seeds.json` | random seeds |
| `PREREGISTRATION.md` / `preregistration.json` | hypothesis + analysis plan, fixed before the experiment ran |
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
