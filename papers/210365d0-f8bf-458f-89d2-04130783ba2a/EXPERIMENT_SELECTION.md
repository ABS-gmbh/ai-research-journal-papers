# Why this study was selected

Recorded before any compute and anchored with the preregistration. The preregistration alone defines the confirmatory test; this record discloses the prior evidence the study responds to and the uncertainty it was expected to resolve. It cannot change after results exist.

- Study: FFN Neuron Capacity Balancing Tests Whether Weight Norm Uniformity Improves Subject-Disjoint Generalization in Time-Series Transformers
- Contrast: FFNRowNormVarianceRegularization on blocks.0.fc1.weight [uci_har_small_transformer_v1]
- Belief state: revision 5 (sha256 `911e228b2adf399d`)
- Planner mode: advisory
- Expected information: 0.834 bits [0.633, 0.982] (undetected-flaw rate 0-0.15 (point 0.05); failure rate 0.286 applied exactly)
- Expected cost: 1.16 GPU-h [1.04, 1.29] (measured; 8.12 GPU-seconds per training measured on 9 completed job(s) of uci_har_small_transformer_v1; 258 trainings per job x 2 job(s) (incl. the mandatory pre-publication reproduction); 90% prediction interval from 9 jobs (t, df=8); wall-clock adds the queue wait measured from the scheduler's start time on 2 of 9 job(s); the rest submission-to-settlement minus runtime, which includes polling)
- Expected to resolve: which effect region holds for FFNRowNormVarianceRegularization on blocks.0.fc1.weight [uci_har_small_transformer_v1], which has no evidence yet

## Prior evidence disclosed

- none: no registered result bears on this contrast yet

## Candidates considered

- [0] FFN Neuron Capacity Balancing Tests Whether Weight Norm Uniformity Improves Subject-Disjoint Generalization in Time-Series Transformers: 0.834 bits, 1.16 GPU-h
- [1] Post-Step Angular Separation of Hidden Unit Weights Tests Whether Directional Diversity in First-Layer Representations Improves Generalization in Small MLPs: 0.834 bits, —

## Assumptions

- undetected-flaw rate 0.05 (sensitivity 0-0.15), a planning assumption
- failure rate 0.286: 1 of 5 executed registered studies ended without a publishable outcome; Beta(1,1) posterior mean
- Episteme's effect model A1-A4; information is expected reduction in entropy (bits)
