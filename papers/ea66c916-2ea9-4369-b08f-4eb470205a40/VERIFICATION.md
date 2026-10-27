# Reproducibility verification — Replication: Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers

> 🤖 This report was produced by independently re-running the experiment from the
> committed bundle ALONE (recorded code, container reference, seeds, and datasets)
> and comparing the reproduced metrics to the ones the paper reports.

✅ REPRODUCED — the independent re-run matched the published results.

- **Status:** `verified`
- **Metrics matched:** 6 / 6
- **Relative tolerance:** 0.05
- **Verification compute job id:** `16726777`
- **Verified at:** 2026-10-18T04:50:13.653897+00:00

Independent re-run reproduced all 6 reported metric(s) within tolerance (relative tolerance 0.05; reproduced means inside the published 95% CI or within tolerance).

## Metric comparison

| Metric | Published | Reproduced | 95% CI | Rel. error | Match |
| --- | --- | --- | --- | --- | --- |
| primary / baseline_1 / held-out classification accuracy | 0.9054 | 0.9045 | [0.902, 0.909] | 0.00105 | ✓ |
| primary / negative_control_1 / held-out classification accuracy | 0.9051 | 0.9055 | [0.902, 0.909] | 0.000436 | ✓ |
| primary / proposed / held-out classification accuracy | 0.9062 | 0.9054 | [0.903, 0.909] | 0.000853 | ✓ |
| replication / baseline_1 / held-out classification accuracy | 0.9035 | 0.8995 | [0.9, 0.907] | 0.00445 | ✓ |
| replication / negative_control_1 / held-out classification accuracy | 0.9043 | 0.9058 | [0.9, 0.908] | 0.00161 | ✓ |
| replication / proposed / held-out classification accuracy | 0.9055 | 0.9057 | [0.902, 0.909] | 0.000183 | ✓ |

## What this reproduction establishes

The criterion above compares condition means only (inside the published 95% CI, or within the relative tolerance). It does not compare contrasts or decisions, which are reported here from the registered analysis applied to the reproduced metrics.

- **Original execution:** compute job `16678400`, one NVIDIA H100 GPU
- **Reproduction:** compute job `16726777`, one NVIDIA A100-SXM4-80GB GPU
- **Per-seed values identical:** between 1 and 3 of 43 seeds per condition and cohort
- **Passed on the tolerance alone (outside the published CI):** `replication / baseline_1 / held-out classification accuracy`

| Cohort | Original contrast | Reproduced contrast | Original decision | Reproduced decision |
| --- | --- | --- | --- | --- |
| primary | +0.00077 [-0.00271, 0.00436] | +0.00095 [-0.00192, 0.00406] | inconclusive | inconclusive |
| replication | +0.00196 [-0.00196, 0.00571] | +0.00615 [0.00125, 0.01208] | inconclusive | inconclusive |

The reproduced interval changed its relationship to zero for: replication. The registered decisions are unchanged.
The cause of the numerical differences has not been determined.
