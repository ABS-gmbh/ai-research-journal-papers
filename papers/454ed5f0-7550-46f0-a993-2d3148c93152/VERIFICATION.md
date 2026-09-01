# Reproducibility verification — Spectral Entropy Minimization of Input Projections for Temporal Feature Learning

> 🤖 This report was produced by independently re-running the experiment from the
> committed bundle ALONE (recorded code, container reference, seeds, and datasets)
> and comparing the reproduced metrics to the ones the paper reports.

✅ REPRODUCED — the independent re-run matched the published results.

- **Status:** `verified`
- **Metrics matched:** 8 / 8
- **Relative tolerance:** 0.05
- **Verification compute job id:** `15688882`
- **Verified at:** 2026-09-01T22:13:48.547679+00:00

Independent re-run reproduced all 8 reported metric(s) within tolerance (relative tolerance 0.05; reproduced means inside the published 95% CI or within tolerance).

## Metric comparison

| Metric | Published | Reproduced | 95% CI | Rel. error | Match |
| --- | --- | --- | --- | --- | --- |
| primary / proposed / held-out classification accuracy | 0.9053 | 0.9047 | [0.902, 0.908] | 0.000715 | ✓ |
| primary / baseline_1 / held-out classification accuracy | 0.9049 | 0.9057 | [0.901, 0.908] | 0.000855 | ✓ |
| primary / negative_control_1 / held-out classification accuracy | 0.9049 | 0.9057 | [0.901, 0.908] | 0.000855 | ✓ |
| primary / negative_control_2 / held-out classification accuracy | 0.9049 | 0.9057 | [0.901, 0.908] | 0.000855 | ✓ |
| replication / proposed / held-out classification accuracy | 0.9087 | 0.9049 | [0.906, 0.912] | 0.00413 | ✓ |
| replication / baseline_1 / held-out classification accuracy | 0.9061 | 0.9083 | [0.902, 0.91] | 0.00244 | ✓ |
| replication / negative_control_1 / held-out classification accuracy | 0.9061 | 0.9083 | [0.902, 0.91] | 0.00244 | ✓ |
| replication / negative_control_2 / held-out classification accuracy | 0.9061 | 0.9083 | [0.902, 0.91] | 0.00244 | ✓ |
