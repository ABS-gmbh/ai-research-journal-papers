# Preregistration

> 🤖 This record was written by the autonomous pipeline at the DESIGN stage,
> BEFORE the experiment was executed, and committed unchanged. It fixes the
> hypothesis, the predicted effect, the metrics, and the analysis plan in advance
> so the reported findings cannot be retrofitted to the results (HARKing).

- **Registered at:** 2026-07-19T16:35:33.623589+00:00
- **Experiment:** Are Heavy-Tail Advantages of SignSGD Coordinate-Aligned?
- **Research question:** On the specified nonlinear teacher-student classification population with controlled Pareto-weighted minibatch gradients, how much does replacing coordinatewise SignSGD by a blockwise orthogonally mixed sign operator change clean validation cross-entropy at a fixed update and example budget?
- **Primary metric:** clean_validation_cross_entropy
- **Metrics:** clean_validation_cross_entropy, training_loss, gradient_norm
- **Baselines:** Coordinatewise SignSGD
- **Seeds per condition:** 5

## Hypothesis

Across 24 iid paired task/seed blocks, dense orthogonal coordinate mixing increases clean validation cross-entropy by more than 0.020 nats/example relative to ordinary coordinatewise SignSGD, showing a practically meaningful coordinate-alignment boundary.

## Predicted direction / effect

Across 24 iid paired task/seed blocks, dense orthogonal coordinate mixing increases clean validation cross-entropy by more than 0.020 nats/example relative to ordinary coordinatewise SignSGD, showing a practically meaningful coordinate-alignment boundary. Specifically, we predict: The blockwise orthogonally mixed SignSGD will show a statistically significant increase in clean validation cross-entropy compared to coordinatewise SignSGD, indicating that the heavy-tail advantages of SignSGD are coordinate-aligned.

## Analysis plan (statistics + seeds)

Each condition (the proposed method vs the baseline(s): Coordinatewise SignSGD) is run across 5 random seeds fixed in advance. For every metric (clean_validation_cross_entropy, training_loss, gradient_norm) we report the per-condition mean with a bootstrap 95% confidence interval. The proposed-vs-baseline difference on the primary metric ('clean_validation_cross_entropy') is tested with a two-sided paired sign-flip randomisation test and a paired bootstrap confidence interval, together with Cohen's dz. Secondary-metric p-values use Holm family-wise-error correction. The seed identities, metrics, and comparisons are fixed now; none are added after seeing the results. Smallest worthwhile effect: A difference of 0.020 nats/example in clean validation cross-entropy.. Power justification: With 24 paired blocks, a target mean difference of 0.050 nats/example, and a standard deviation of 0.040, the study has 95.84% power to detect a smallest worthwhile effect of 0.020 nats/example.. Stopping rule: The study will stop after completing all 48 runs (24 seeds × 2 conditions).. Multiplicity: No multiple comparisons will be performed; the study focuses on a single primary comparison..
