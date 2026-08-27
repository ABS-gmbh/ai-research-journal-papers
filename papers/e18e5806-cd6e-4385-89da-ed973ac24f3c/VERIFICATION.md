# Reproducibility verification — Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 This report was produced by independently re-running the experiment from the
> committed bundle ALONE (recorded code, container reference, seeds, and datasets)
> and comparing the reproduced metrics to the ones the paper reports.

✅ REPRODUCED — the independent re-run matched the published results.

- **Status:** `verified`
- **Metrics matched:** 8 / 8
- **Relative tolerance:** 0.05
- **Verification Slurm job id:** `15547227`
- **Verified at:** 2026-08-27T10:58:20.536076+00:00

Independent re-run reproduced all 8 reported metric(s) within tolerance (relative tolerance 0.05; reproduced means inside the published 95% CI or within tolerance).

## Metric comparison

| Metric | Published | Reproduced | 95% CI | Rel. error | Match |
| --- | --- | --- | --- | --- | --- |
| primary / proposed / held-out classification accuracy | 0.8604 | 0.8604 | [0.837, 0.877] | 0 | ✓ |
| primary / baseline_1 / held-out classification accuracy | 0.9085 | 0.9085 | [0.905, 0.912] | 0 | ✓ |
| primary / negative_control_1 / held-out classification accuracy | 0.9082 | 0.9082 | [0.905, 0.911] | 0 | ✓ |
| primary / negative_control_2 / held-out classification accuracy | 0.909 | 0.909 | [0.906, 0.912] | 0 | ✓ |
| replication / proposed / held-out classification accuracy | 0.8717 | 0.8717 | [0.865, 0.877] | 0 | ✓ |
| replication / baseline_1 / held-out classification accuracy | 0.9065 | 0.9065 | [0.903, 0.91] | 0 | ✓ |
| replication / negative_control_1 / held-out classification accuracy | 0.908 | 0.908 | [0.904, 0.912] | 0 | ✓ |
| replication / negative_control_2 / held-out classification accuracy | 0.9088 | 0.9088 | [0.905, 0.912] | 0 | ✓ |
