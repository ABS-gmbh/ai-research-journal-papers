# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-GENERATED.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

This repository is the full, reproducible bundle for an automatically generated research
paper: the exact experiment code, the real results, run logs, random seeds, the compute job
id, the agent's complete reasoning trace (including failed attempts), and the paper itself
(Markdown + PDF).

## Reproduce

```bash
# 1) Convert the container image to Apptainer on a cluster login node
apptainer build experiment.sif docker://pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755

# 2) Run the experiment (the generic entrypoint is in code/)
apptainer exec --nv --containall --cleanenv --no-home \
  --bind ./code:/work/code:ro --bind ./results:/work/results --pwd /work/results \
  --bind ./datasets:/work/datasets:ro \
  experiment.sif \
  python /work/code/_journal_entrypoint.py \
    --code-dir /work/code --entrypoint experiment \
    --results-dir /work/results --seed 1234 --args-json '{"seed_ids": [497360171578835126, 619747419151856849, 4359311500859520721, 3900812323465083926, 1516445550462428226, 1630043136886007277, 1835401958502649079, 4224212089476219622, 2975544019134720152, 3507764674343915068, 4004663391355442268, 1509823930515868492, 3483967100743641674, 2225936250788509260, 1957754086644492888, 4154286735266072875, 3813494016017719200, 690472406820790188, 3813916678459859089, 4090465763900842853, 1844212296145829516, 3081923774287884327, 3477292413922411937, 726925812904865219, 4400454224498690158, 1309720931756809616, 3670000523134785215, 1572470746349086798, 5569990145947559, 2855297384752490100, 3166602034212987559, 4221459448664290905, 2934143650096726109, 1462463051419223747, 4363375170763905339, 3648570110071838823, 258115887333994485, 2427086170940110629, 4084426303853737760, 2996901096067535381, 2815367292871095378, 4593572677630054665, 3754669615394449950], "replication_seed_ids": [460845256865125083, 168360166801404394, 4330504984584448312, 2288886165882978077, 1436023229729468928, 3075137203164680509, 1264378101010998013, 2924740817759706416, 1407030776384369816, 3476452012804091485, 413443216560218742, 3744310097398416000, 611732904494353021, 3048141337216032385, 3348171016926346274, 182544617978886718, 2236541698554417841, 316787348038406038, 2542361651984418572, 2578784020613117302, 2827919878303280846, 50058912656477012, 2277661776842494339, 4538007595258168616, 2319057271103286511, 2045154589577734854, 2155395884799988780, 4226716155317983348, 1618031700484817618, 2260344274002574536, 2384851163006458576, 926629052757699259, 3894402378906575006, 299845134544061382, 460921128077554766, 3639277473403927291, 370580726517054298, 3492117404588741396, 3679724535907974316, 808192457140985599, 4061812732870876608, 820537500989758760, 2718212184032681684], "required_condition_ids": ["proposed", "baseline_1", "negative_control_1", "negative_control_2"]}' \
    --datasets-json '{"uci_har_smartphones": "/work/datasets/c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031/uci-har-smartphones.zip"}'
```

- **Random seeds:** `None`
- **compute job id:** `15540577`
- **Partition:** `[redacted]`
- **Container image:** `pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755`
- **Apptainer SIF SHA-256:** `b04db4d9ba8a7e95505a053162340badfc283d7cb408bc7ec62ec60eb48fb02e`
- **Preregistration SHA-256:** `1158469e650cb006fca4a8faea52c17fa22a422927a852c09eb291716afadca1`
- **Preregistration anchor commit:** `304e0111389ccccee1e6ef854dfe430a3f0b153d`

## Contents

| Path | What |
| --- | --- |
| `paper.md` / `paper.pdf` | the paper |
| `paper.json` | the structured paper (schema) |
| `code/` | the exact experiment code |
| `metrics.json` | the real results |
| `metrics.png` | results figure |
| `seeds.json` | random seeds |
| `PREREGISTRATION.md` / `preregistration.json` | hypothesis + analysis plan, fixed before the experiment ran |
| `datasets.json` | staged dataset provenance (source, sha256, paths) |
| `logs/run.log` | compute run logs |
| `trace.json` | the agent's full reasoning trace (incl. failures) |
| `metadata.json` | run id, job id, image, timings |
| `MANIFEST.sha256` | SHA-256 of every bundle file |
| `VERIFICATION.md` / `verification.json` | independent reproduction re-run report (if verified) |
