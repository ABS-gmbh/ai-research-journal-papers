# Why this study was selected

Recorded before any compute and anchored with the preregistration. The preregistration alone defines the confirmatory test; this record discloses the prior evidence the study responds to and the uncertainty it was expected to resolve. It cannot change after results exist.

- Study: Replication: Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers
- Contrast: CrossLayerQueryConsistency on blocks.1.attn.q_proj.weight [uci_har_small_transformer_v1]
- Belief state: revision 3 (sha256 `1f4c33ca44fead2d`)
- Planner mode: seeded
- Expected information: 0.106 bits [0.000, 0.197] (undetected-flaw rate 0-0.15 (point 0.05); failure rate 0.333 applied exactly)
- Expected cost: 1.14 GPU-h [1.01, 1.26] (measured; 7.93 GPU-seconds per training measured on 7 completed job(s) of uci_har_small_transformer_v1; 258 trainings per job x 2 job(s) (incl. the mandatory pre-publication reproduction); 90% prediction interval from 7 jobs (t, df=6); wall-clock adds the measured submission-to-settlement overhead per job)
- Expected to resolve: which effect region holds for CrossLayerQueryConsistency on blocks.1.attn.q_proj.weight [uci_har_small_transformer_v1] (existing evidence)
- The planner's own top study: Register a new study of CrossLayerQueryConsistency on blocks.1.attn.q_proj.weight [uci_har_small_transformer_v1] — this study implements it

## Prior evidence disclosed

- `ev:e5c7eb4e-f542-4c7d-bcd0-6ceff9b99e91` (run e5c7eb4e-f542-4c7d-bcd0-6ceff9b99e91): CrossLayerQueryConsistency on blocks.1.attn.q_proj.weight [uci_har_small_transformer_v1]; primary inconclusive, replication inconclusive; valid: weighs in the posterior

## Candidates considered

- [0] Replication: Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers: 0.106 bits, 1.14 GPU-h

## Assumptions

- undetected-flaw rate 0.05 (sensitivity 0-0.15), a planning assumption
- failure rate 0.333: 1 of 4 executed registered studies ended without a publishable outcome; Beta(1,1) posterior mean
- Episteme's effect model A1-A4; information is expected reduction in entropy (bits)
