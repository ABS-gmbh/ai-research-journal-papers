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
