# Reproducibility verification — Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers

> 🤖 This report was produced by independently re-running the experiment from the
> committed bundle ALONE (recorded code, container reference, seeds, and datasets)
> and comparing the reproduced metrics to the ones the paper reports.

✅ REPRODUCED — the independent re-run matched the published results.

- **Status:** `verified`
- **Metrics matched:** 6 / 6
- **Relative tolerance:** 0.05
- **Verification compute job id:** `16233356`
- **Verified at:** 2026-09-24T19:59:33.944318+00:00

Independent re-run reproduced all 6 reported metric(s) within tolerance (relative tolerance 0.05; reproduced means inside the published 95% CI or within tolerance).

## Metric comparison

| Metric | Published | Reproduced | 95% CI | Rel. error | Match |
| --- | --- | --- | --- | --- | --- |
| primary / baseline_1 / held-out classification accuracy | 0.9051 | 0.9051 | [0.902, 0.909] | 0 | ✓ |
| primary / negative_control_1 / held-out classification accuracy | 0.9076 | 0.9076 | [0.904, 0.911] | 0 | ✓ |
| primary / proposed / held-out classification accuracy | 0.9065 | 0.9065 | [0.902, 0.911] | 0 | ✓ |
| replication / baseline_1 / held-out classification accuracy | 0.9076 | 0.9076 | [0.904, 0.911] | 0 | ✓ |
| replication / negative_control_1 / held-out classification accuracy | 0.9067 | 0.9067 | [0.903, 0.91] | 0 | ✓ |
| replication / proposed / held-out classification accuracy | 0.9061 | 0.9061 | [0.902, 0.909] | 0 | ✓ |
