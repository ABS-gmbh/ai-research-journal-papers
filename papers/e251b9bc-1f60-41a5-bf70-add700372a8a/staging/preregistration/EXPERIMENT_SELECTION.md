# Why this study was selected

Recorded before any compute and anchored with the preregistration. The preregistration alone defines the confirmatory test; this record discloses the prior evidence the study responds to and the uncertainty it was expected to resolve. It cannot change after results exist.

- Study: Momentum-Orthogonal Projection Tests Whether Optimizer-State Geometry Improves Subject-Disjoint Generalization
- Contrast: MomentumOrthogonalProjection on blocks.0.attn.q_proj.weight [uci_har_small_transformer_v1]
- Belief state: revision 7 (sha256 `41e695f424f0b9e5`)
- Planner mode: advisory
- Expected information: 0.701 bits [0.532, 0.825] (undetected-flaw rate 0-0.15 (point 0.05); failure rate 0.400 applied exactly)
- Expected cost: 1.24 GPU-h [1.14, 1.34] (measured; 8.64 GPU-seconds per training measured on 8 completed job(s) of uci_har_small_transformer_v1; 258 trainings per job x 2 job(s) (incl. the mandatory pre-publication reproduction); 90% prediction interval from 8 jobs (t, df=7); wall-clock adds the queue wait measured from the scheduler's start time on 4 of 8 job(s); the rest submission-to-settlement minus runtime, which includes polling)
- Expected to resolve: which effect region holds for MomentumOrthogonalProjection on blocks.0.attn.q_proj.weight [uci_har_small_transformer_v1], which has no evidence yet

## Prior evidence disclosed

- none: no registered result bears on this contrast yet

## Candidates considered

- [0] Frobenius Scale-Regularization of Output Projections Tests Whether Weight Magnitude Constraints Improve Generalization in Small MLPs: 0.701 bits, —
- [1] Momentum-Orthogonal Projection Tests Whether Optimizer-State Geometry Improves Subject-Disjoint Generalization: 0.701 bits, 1.24 GPU-h

## Assumptions

- undetected-flaw rate 0.05 (sensitivity 0-0.15), a planning assumption
- failure rate 0.400: 1 of 3 executed registered studies ended without a publishable outcome; Beta(1,1) posterior mean
- Episteme's effect model A1-A4; information is expected reduction in entropy (bits)
