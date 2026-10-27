# Row-Norm Variance Regularization of the First Block's Feed-Forward Weights in a Small Time-Series Transformer: A Preregistered Test of Subject-Disjoint Accuracy

> 🤖 **AI-GENERATED.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. After the autonomous run, a human editor corrected parts of the text before publication: the editor rewrote the title, the abstract and the Figure 1 caption, revised sentences in the Introduction, Related Work, Results, Discussion, Limitations and Conclusion, and added one paragraph to the Limitations; the server added a reproduction disclosure, composed from the reproduction record, to the Limitations. Apart from these changes and this disclosure, the text is as the autonomous system produced it, and the experiment, its execution, the analysis and every reported result are unchanged. CORRECTION.md lists every changed sentence.

This repository is the full, reproducible bundle for an automatically generated research
paper: the exact experiment code, the real results, run logs, random seeds, the compute job
id, the agent's complete reasoning trace (including failed attempts), and the paper itself
(Markdown + PDF).

## Reproduce

```bash
# 1) Convert the container image to Apptainer on a cluster login node
apptainer build experiment.sif docker://pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755

# Verify the original container bytes before running
printf '%s  experiment.sif\n' b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e | sha256sum -c -

# 2) Run the experiment (the generic entrypoint is in code/)
mkdir -p results
apptainer exec --nv --containall --cleanenv --no-home \
  --env CUBLAS_WORKSPACE_CONFIG=:4096:8 \
  --bind ./code:/work/code:ro --bind ./results:/work/results --pwd /work/results \
  --bind ./datasets:/work/datasets:ro \
  experiment.sif \
  python /work/code/_journal_entrypoint.py \
    --code-dir /work/code --entrypoint experiment \
    --results-dir /work/results --seed 1234 --args-json '{"replication_seed_ids": [4320773929864477461, 4572011691334341044, 1024169838608046568, 70426179010925050, 4279951434647552413, 1525730301824159332, 2456995112630259840, 1438940561707491066, 3265594330752860948, 3313077302295843199, 154257161523473883, 932959957416460902, 2460345311424550248, 4103027776969344918, 3180763842676044575, 2680763204965541202, 860343005213925595, 2251660953322924511, 3602542195028900413, 4597019890493101173, 1088915320621658123, 1852251732497043221, 3465798054693121361, 1353228797488142695, 4288297583911624336, 4255826400377963612, 2929822804607519445, 1498830690282327365, 3112246099719202789, 1000118519658128261, 1257818511997115116, 1228137926523810998, 7730833112919494, 2311327190165276681, 2983717921336380133, 1878749905703531082, 699211854863334235, 3299934322367760388, 1909067866147248581, 848308637145405381, 749878386657420966, 689681967342702198, 249916436928423872], "required_condition_ids": ["proposed", "baseline_1", "negative_control_1"], "seed_ids": [3082305311014867827, 4186422859404013514, 2387181325241556003, 3182619286003977438, 3438331344051643608, 620252232043632839, 3239163973742456083, 1898248096129308665, 1066012308908509790, 4438929654394750517, 2854402741562619104, 1920862951106082837, 1536148981766593057, 1964427229086117459, 1887475434142652658, 3772847866917766394, 359941395117292827, 2136554577369890083, 4188340981133805670, 1315161378058826978, 1415188985576409927, 1310082642526382996, 2736886400400380092, 1485561164519252005, 3502707465086045048, 3394863877104515794, 371674130373742582, 1386069600169889359, 3148930491141517020, 1013576460105568673, 3638501434658534819, 2453211275455103459, 2735914919971171670, 357041012913871729, 2525930462449636703, 1404659974452858503, 2421171159155662627, 1567729552275512853, 3073538427502128060, 2266614561625367693, 3237028201528057935, 633394856712588532, 4364642531486158638]}' \
    --datasets-json '{"uci_har_smartphones": "/work/datasets/c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031/uci-har-smartphones.zip"}'
```

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
| `code/` | the exact experiment code |
| `reproduction.json` | frozen runner, code, invocation, container checksum, dataset inputs and reference outputs |
| `REPRODUCTION_SOURCE.json` | immutable commit and checksum used by independent verification |
| `metrics.json` | the real results |
| declared `*.png` figures | every figure referenced by the paper, with available SVG copies |
| `seeds.json` | random seeds |
| `PREREGISTRATION.md` / `preregistration.json` | hypothesis + analysis plan, fixed before the experiment ran |
| `SEMANTIC_LOCK.md` / `semantic_contract.json` | the locked scientific contract and what was machine-verified against it |
| `EXPERIMENT_SELECTION.md` / `experiment_selection.json` | why this study was selected: its expected information and cost, and the prior evidence it responds to (fixed before the experiment ran) |
| `CLAIMS.md` / `claim_ledger.json` | every material claim in the paper, checked against the run's own records |
| `datasets.json` | staged dataset provenance (source, sha256, paths) |
| `logs/run.log` | compute run logs |
| `trace.json` | the agent's full reasoning trace (incl. failures) |
| `metadata.json` | run id, job id, image, timings |
| `MANIFEST.sha256` | SHA-256 of every bundle file |
| `VERIFICATION.md` / `verification.json` | independent reproduction re-run report (if verified) |

## Reporting correction

See [CORRECTION.md](CORRECTION.md) for the version history and change note, and [correction.json](correction.json) for its structured metadata.
