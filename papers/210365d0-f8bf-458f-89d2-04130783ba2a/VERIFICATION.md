# Reproducibility verification — Row-Norm Variance Regularization of the First Block's Feed-Forward Weights in a Small Time-Series Transformer: A Preregistered Test of Subject-Disjoint Accuracy

> 🤖 This report was produced by independently re-running the experiment from the
> committed bundle ALONE (recorded code, container reference, seeds, and datasets)
> and comparing the reproduced metrics to the ones the paper reports.

✅ DECISIONS REPRODUCED — the independent re-run reached the same registered decisions and its condition means met the stated criterion; the per-seed values were not numerically identical.

- **Status:** `verified`
- **Metrics matched:** 6 / 6
- **Relative tolerance:** 0.05
- **Verification compute job id:** `16883125`
- **Verified at:** 2026-10-27T15:51:52.763188+00:00

Independent re-run reproduced all 6 reported metric(s) within tolerance (relative tolerance 0.05; reproduced means inside the published 95% CI or within tolerance).

## Metric comparison

| Metric | Published | Reproduced | 95% CI | Rel. error | Match |
| --- | --- | --- | --- | --- | --- |
| primary / baseline_1 / held-out classification accuracy | 0.9059 | 0.9059 | [0.903, 0.909] | 7.84e-05 | ✓ |
| primary / negative_control_1 / held-out classification accuracy | 0.9057 | 0.9048 | [0.901, 0.91] | 0.000967 | ✓ |
| primary / proposed / held-out classification accuracy | 0.9059 | 0.9052 | [0.902, 0.91] | 0.000732 | ✓ |
| replication / baseline_1 / held-out classification accuracy | 0.9052 | 0.9058 | [0.901, 0.909] | 0.000593 | ✓ |
| replication / negative_control_1 / held-out classification accuracy | 0.9074 | 0.9064 | [0.904, 0.911] | 0.00114 | ✓ |
| replication / proposed / held-out classification accuracy | 0.9062 | 0.9077 | [0.903, 0.909] | 0.00164 | ✓ |

## What this reproduction establishes

The criterion above compares condition means only (inside the published 95% CI, or within the relative tolerance). It does not compare contrasts or decisions, which are reported here from the registered analysis applied to the reproduced metrics.

- **Original execution:** compute job `16881595`, one NVIDIA A100-SXM4-40GB GPU
- **Reproduction:** compute job `16883125`, one NVIDIA H100 GPU
- **Per-seed values identical:** between 1 and 2 of 43 seeds per condition and cohort

| Cohort | Original contrast | Reproduced contrast | Original decision | Reproduced decision |
| --- | --- | --- | --- | --- |
| primary | -0.00008 [-0.00217, 0.00214] | -0.00067 [-0.00327, 0.00200] | inconclusive | inconclusive |
| replication | +0.00094 [-0.00180, 0.00387] | +0.00189 [-0.00010, 0.00402] | inconclusive | inconclusive |

The cause of the numerical differences has not been determined.
