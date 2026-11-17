# Reproducibility verification — Momentum-Orthogonal Projection Tests Whether Optimizer-State Geometry Improves Subject-Disjoint Generalization

> 🤖 This report was produced by independently re-running the experiment from the
> committed bundle ALONE (recorded code, container reference, seeds, and datasets)
> and comparing the reproduced metrics to the ones the paper reports.

✅ REPRODUCED EXACTLY — every per-seed value of the independent re-run equals the published one.

- **Status:** `verified`
- **Metrics matched:** 6 / 6
- **Relative tolerance:** 0.05
- **Verification compute job id:** `17343557`
- **Verified at:** 2026-11-16T14:03:07.112750+00:00

Independent re-run reproduced all 6 reported metric(s) within tolerance (relative tolerance 0.05; reproduced means inside the published 95% CI or within tolerance). Both cohorts reproduced their registered decision, and each execution's primary contrast lies inside the other's 95% interval.

## Metric comparison

| Metric | Published | Reproduced | 95% CI | Rel. error | Match |
| --- | --- | --- | --- | --- | --- |
| primary / baseline_1 / held-out classification accuracy | 0.9068 | 0.9068 | [0.903, 0.91] | 0 | ✓ |
| primary / negative_control_1 / held-out classification accuracy | 0.8898 | 0.8898 | [0.886, 0.893] | 0 | ✓ |
| primary / proposed / held-out classification accuracy | 0.8951 | 0.8951 | [0.891, 0.899] | 0 | ✓ |
| replication / baseline_1 / held-out classification accuracy | 0.9081 | 0.9081 | [0.904, 0.912] | 0 | ✓ |
| replication / negative_control_1 / held-out classification accuracy | 0.8868 | 0.8868 | [0.882, 0.891] | 0 | ✓ |
| replication / proposed / held-out classification accuracy | 0.8906 | 0.8906 | [0.887, 0.895] | 0 | ✓ |

## Contrast and decision agreement

Criterion: per cohort: the registered decision of the reproduced execution equals the original's, the reproduced primary contrast lies inside the original's 95% interval, and the original primary contrast lies inside the reproduced 95% interval. Verdict: **holds**.

| Cohort | Decision reproduced | Reproduced in original CI | Original in reproduced CI | Per-seed identical |
| --- | --- | --- | --- | --- |
| primary | ✓ (direction_refuted → direction_refuted) | ✓ | ✓ | 129 / 129 (100%) |
| replication | ✓ (direction_refuted → direction_refuted) | ✓ | ✓ | 129 / 129 (100%) |


## What this reproduction establishes

The criterion above compares condition means only (inside the published 95% CI, or within the relative tolerance). It does not compare contrasts or decisions, which are reported here from the registered analysis applied to the reproduced metrics.

- **Original execution:** compute job `17338534`, one NVIDIA A100-SXM4-80GB GPU
- **Reproduction:** compute job `17343557`, one NVIDIA A100-SXM4-80GB GPU
- **Per-seed values identical:** between 43 and 43 of 43 seeds per condition and cohort

| Cohort | Original contrast | Reproduced contrast | Original decision | Reproduced decision |
| --- | --- | --- | --- | --- |
| primary | -0.01171 [-0.01744, -0.00664] | -0.01171 [-0.01744, -0.00664] | direction_refuted | direction_refuted |
| replication | -0.01757 [-0.02181, -0.01299] | -0.01757 [-0.02181, -0.01299] | direction_refuted | direction_refuted |

The cause of the numerical differences has not been determined.
