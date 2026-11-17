# Preregistration

> 🤖 This record was written by the autonomous pipeline at the DESIGN stage,
> BEFORE the experiment was executed, and committed unchanged. It fixes the
> hypothesis, the predicted effect, the metrics, and the analysis plan in advance
> so the reported findings cannot be retrofitted to the results (HARKing).

- **Registered at:** 2026-11-16T07:32:41.521674+00:00
- **Experiment:** Momentum-Orthogonal Projection Tests Whether Optimizer-State Geometry Improves Subject-Disjoint Generalization
- **Research question:** Does dynamic regularization based on optimizer state geometry improve generalization where static weight regularizers fail?
- **Primary metric:** held-out classification accuracy
- **Metrics:** held-out classification accuracy
- **Baselines:** Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (post step). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.
- **Publication policy:** publish_all_valid_outcomes
- **Publishable valid outcomes:** direction_supported, direction_refuted, inconclusive
- **Seeds per condition:** 43
- **Primary seed IDs:** 3997813737653302303, 3309792543465967669, 898169320913783714, 3964896538127092764, 3171176783835818082, 2125254381612812340, 164463215743309073, 4607537401135060359, 4371816041976198247, 4375509884083495539, 56571881961416109, 3186175054496708162, 3135712612105761914, 2917419308223782333, 756296250425846271, 3664668516161228860, 1952755448443270368, 3643410946486515578, 3644367669275750018, 1309667764697542987, 1441715280992064684, 3511410770844740244, 4133809473348287269, 1725100179333995995, 1053041997813283501, 3088030652051418133, 4107816827218925227, 565566558421734252, 275805123457331965, 2680573877972736630, 157765648583704381, 4421031413392467556, 1552854591870605401, 2364009805729299393, 1904461708440649292, 1120772267680505117, 1092494605915433619, 2229838033419613320, 2059267624277869210, 510733906447812518, 1071007686057160105, 3808697128436486247, 4532370378841381999
- **Executed confirmatory-replication seed IDs:** 2354976006981955819, 4324660935519791914, 831562771514012917, 2751327354233951026, 1512451331433289100, 2339623576096759615, 942097766754537929, 299423626648925212, 1613961540201361027, 2495779494466921665, 3286046173524442755, 1226876407126695882, 2822438373310273476, 3359112155736441787, 4589841592586339548, 2174476099861496296, 4400594877164728163, 1473987275448740522, 3560021299613277498, 1963134501751537655, 3857100197921599726, 1946187660472806283, 534240155361867711, 2257819899425946518, 1857067766385637398, 1542467500088558298, 2565902916065722756, 4469043849214490585, 2459162917649737361, 2486378516630103661, 285328054388411115, 2406669371174695006, 446452795583064019, 4179188943919088022, 493150260764163842, 3754155167337633593, 2778791489195799033, 1918504031098073709, 3156095766939290846, 1998442627702540335, 2669942370954230662, 427097415724880873, 1648269874916305333

## Hypothesis

The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion.

## Predicted direction / effect

The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion. Specifically, we predict: The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion.

## Fixed operational specification

```json
{
  "alternative_hypotheses": [
    "The effect is due to effective weight decay induced by projection.",
    "The effect is due to breaking momentum symmetry rather than orthogonality."
  ],
  "boundary_conditions": [
    "Fails if momentum is zero (initial steps).",
    "May harm plasticity if momentum signal is clean.",
    "Scope (server-owned): single calibrated testbed uci_har_small_transformer_v1 \u2014 UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows); model PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)); evaluated as the official UCI HAR test split \u2014 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning",
    "For each seed, both conditions use identical initialization, data split/order, stochastic draws, hyperparameters, tuning, update count, and compute budget.",
    "Model and optimizer state are reset independently for each condition; no trained state is carried between paired runs."
  ],
  "calibration_record_id": "4aad7be5-2893-4878-b5b0-ed773e8cbb5c",
  "canonical_hypothesis": "The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion.",
  "comparator": "Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step \u2014 the same forward pass, the same classification objective, the same backward pass and the same optimizer update \u2014 and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (post step). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.",
  "decision_consequence": "If supported, mandate Momentum-Orthogonal Projection for the uci_har_small_transformer_v1 baseline configuration. If refuted, exclude optimizer-state geometric constraints from the regularization search space for this architecture and data regime.",
  "decision_value": "Using the two-sided paired-bootstrap 95% CI for mean(H_s), support the preregistered directional effect only when CI_low > 0.0125098; refute that directional effect when CI_high <= 0; otherwise report inconclusive. The paired sign-flip p-value is descriptive and does not replace this decision rule. Decision consequence: If supported, mandate Momentum-Orthogonal Projection for the uci_har_small_transformer_v1 baseline configuration. If refuted, exclude optimizer-state geometric constraints from the regularization search space for this architecture and data regime.",
  "estimand": "Hypothesis-positive paired contrast H_s = outcome_intervention - outcome_comparator; estimand = arithmetic mean of H_s over the preregistered primary seed IDs.",
  "failure_handling": "A non-finite outcome is never a data point: the harness raises on any non-finite value for either condition in that seed pair, so the job fails and reports nothing rather than a value it did not measure. No preregistered seed is discarded, skipped, or rerun, and no outcome is imputed.",
  "falsification_criteria": [
    "Refute the preregistered directional effect when the two-sided paired-bootstrap 95% CI upper endpoint for mean(H_s) is <= 0.",
    "Do not claim a worthwhile directional effect unless that CI's lower endpoint exceeds the fixed margin 0.0125098 proportion."
  ],
  "hypothesis_positive_multiplier": 1,
  "hypothesized_direction": "intervention_better",
  "intervention": "Server-bound target blocks.0.attn.q_proj.weight has stored tensor shape (64, 64). Momentum-Orthogonal Projection post-step operator",
  "intervention_protocol": {
    "application_timing": "Executed lifecycle (server-owned): the operator is invoked after the optimizer step of every optimization step: the operator modifies the parameters or optimizer state the standard update just produced, so the modification persists into subsequent steps and into the evaluated weights.",
    "execution_phases": [
      "post_step"
    ],
    "invariants": [
      "W row norm decreases or stays same",
      "W becomes orthogonal to M on valid rows"
    ],
    "learns_parameters": false,
    "normalization_rule": "none",
    "numerical_safeguards": "epsilon 1e-12 on denominator; skip if M norm zero",
    "operator_name": "MomentumOrthogonalProjection",
    "ordering_rule": "parallel across rows",
    "pseudocode": [
      "1. Receive target parameter tensor W.",
      "2. Receive optimizer momentum buffer M.",
      "3. Receive condition flag.",
      "4. If condition flag equals 'control', terminate without modifying W.",
      "5. Compute row-wise squared norms of M: norm_M_sq = sum(M * M, dim=1).",
      "6. Create mask valid_rows = (norm_M_sq > 1e-12).",
      "7. If no valid_rows exist, terminate without modifying W.",
      "8. Compute row-wise dot products: dot = sum(W * M, dim=1).",
      "9. Compute projection scalars: alpha = dot / (norm_M_sq + 1e-12).",
      "10. Broadcast alpha to match W shape: alpha_expanded = alpha.unsqueeze(1).",
      "11. Compute projection update: delta = alpha_expanded * M.",
      "12. Apply orthogonal projection: W[valid_rows, :] = W[valid_rows, :] - delta[valid_rows, :].",
      "13. Ensure W modification is in-place.",
      "14. Return.",
      "Scope (server-owned): control arm. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (post step). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. If the condition the harness passes in is a control condition, return here: add no term to the training objective, and leave the registered target parameter and that parameter's optimizer momentum buffer exactly as received. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study."
    ],
    "tensor_axis_or_scope": "row"
  },
  "intervention_target": "blocks.0.attn.q_proj.weight",
  "intervention_target_shape": [
    64,
    64
  ],
  "leakage_risks": [
    "None beyond standard training leakage; momentum is internal state."
  ],
  "mechanistic_rationale": "Momentum accumulates gradient history; on noisy small data, this history may point away from the generalizable minimum. Orthogonalizing weights against momentum prevents the model from 'coasting' into sharp minima aligned with noise, forcing reliance on current batch gradients.",
  "negative_control_roles": [
    "validity_condition"
  ],
  "negative_controls": [
    "Sign-Randomized Momentum Projection"
  ],
  "outcome_formula": "number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split",
  "outcome_higher_is_better": true,
  "outcome_name": "held-out classification accuracy",
  "outcome_range_max": 1.0,
  "outcome_range_min": 0.0,
  "outcome_unit": "proportion",
  "planning_sd": 0.025019595493970412,
  "planning_sd_basis": "Immutable calibration record 4aad7be5-2893-4878-b5b0-ed773e8cbb5c; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155.",
  "population": "Seeded training runs of the UCI HAR Small Transformer on the fixed training cohort.",
  "primary_outcome": "held-out classification accuracy: number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split; unit=proportion; range=[0, 1]; computed once per seeded run; higher is better; failure handling: A non-finite outcome is never a data point: the harness raises on any non-finite value for either condition in that seed pair, so the job fails and reports nothing rather than a value it did not measure. No preregistered seed is discarded, skipped, or rerun, and no outcome is imputed.",
  "replication_plan": "Independently repeat the same paired protocol using both conditions for every disjoint replication seed ID [2354976006981955819, 4324660935519791914, 831562771514012917, 2751327354233951026, 1512451331433289100, 2339623576096759615, 942097766754537929, 299423626648925212, 1613961540201361027, 2495779494466921665, 3286046173524442755, 1226876407126695882, 2822438373310273476, 3359112155736441787, 4589841592586339548, 2174476099861496296, 4400594877164728163, 1473987275448740522, 3560021299613277498, 1963134501751537655, 3857100197921599726, 1946187660472806283, 534240155361867711, 2257819899425946518, 1857067766385637398, 1542467500088558298, 2565902916065722756, 4469043849214490585, 2459162917649737361, 2486378516630103661, 285328054388411115, 2406669371174695006, 446452795583064019, 4179188943919088022, 493150260764163842, 3754155167337633593, 2778791489195799033, 1918504031098073709, 3156095766939290846, 1998442627702540335, 2669942370954230662, 427097415724880873, 1648269874916305333]; reset all state and apply the identical hypothesis-positive contrast and fixed CI decision rule.",
  "replication_seed_ids": [
    2354976006981955819,
    4324660935519791914,
    831562771514012917,
    2751327354233951026,
    1512451331433289100,
    2339623576096759615,
    942097766754537929,
    299423626648925212,
    1613961540201361027,
    2495779494466921665,
    3286046173524442755,
    1226876407126695882,
    2822438373310273476,
    3359112155736441787,
    4589841592586339548,
    2174476099861496296,
    4400594877164728163,
    1473987275448740522,
    3560021299613277498,
    1963134501751537655,
    3857100197921599726,
    1946187660472806283,
    534240155361867711,
    2257819899425946518,
    1857067766385637398,
    1542467500088558298,
    2565902916065722756,
    4469043849214490585,
    2459162917649737361,
    2486378516630103661,
    285328054388411115,
    2406669371174695006,
    446452795583064019,
    4179188943919088022,
    493150260764163842,
    3754155167337633593,
    2778791489195799033,
    1918504031098073709,
    3156095766939290846,
    1998442627702540335,
    2669942370954230662,
    427097415724880873,
    1648269874916305333
  ],
  "sample_size_rationale": "Prospective paired normal approximation with two-sided alpha=0.05: planning SD(H_s)=0.0250196 proportion, worthwhile effect=0.0125098, target power=0.90, required n=43; fixed n=43. Planning-SD basis: Immutable calibration record 4aad7be5-2893-4878-b5b0-ed773e8cbb5c; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155. Worthwhile-effect basis: Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).",
  "seed_ids": [
    3997813737653302303,
    3309792543465967669,
    898169320913783714,
    3964896538127092764,
    3171176783835818082,
    2125254381612812340,
    164463215743309073,
    4607537401135060359,
    4371816041976198247,
    4375509884083495539,
    56571881961416109,
    3186175054496708162,
    3135712612105761914,
    2917419308223782333,
    756296250425846271,
    3664668516161228860,
    1952755448443270368,
    3643410946486515578,
    3644367669275750018,
    1309667764697542987,
    1441715280992064684,
    3511410770844740244,
    4133809473348287269,
    1725100179333995995,
    1053041997813283501,
    3088030652051418133,
    4107816827218925227,
    565566558421734252,
    275805123457331965,
    2680573877972736630,
    157765648583704381,
    4421031413392467556,
    1552854591870605401,
    2364009805729299393,
    1904461708440649292,
    1120772267680505117,
    1092494605915433619,
    2229838033419613320,
    2059267624277869210,
    510733906447812518,
    1071007686057160105,
    3808697128436486247,
    4532370378841381999
  ],
  "smallest_worthwhile_effect": "0.0125098 proportion on H_s",
  "smallest_worthwhile_effect_basis": "Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).",
  "smallest_worthwhile_effect_value": 0.012509797746985206,
  "target_power": 0.9,
  "testbed_id": "uci_har_small_transformer_v1",
  "unit_of_analysis": "Seeded training run"
}
```

## Analysis plan (statistics + seeds)

Each condition (the proposed method vs the baseline(s): Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (post step). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.) is first run across the 43 primary random seeds fixed in advance with exact IDs [3997813737653302303, 3309792543465967669, 898169320913783714, 3964896538127092764, 3171176783835818082, 2125254381612812340, 164463215743309073, 4607537401135060359, 4371816041976198247, 4375509884083495539, 56571881961416109, 3186175054496708162, 3135712612105761914, 2917419308223782333, 756296250425846271, 3664668516161228860, 1952755448443270368, 3643410946486515578, 3644367669275750018, 1309667764697542987, 1441715280992064684, 3511410770844740244, 4133809473348287269, 1725100179333995995, 1053041997813283501, 3088030652051418133, 4107816827218925227, 565566558421734252, 275805123457331965, 2680573877972736630, 157765648583704381, 4421031413392467556, 1552854591870605401, 2364009805729299393, 1904461708440649292, 1120772267680505117, 1092494605915433619, 2229838033419613320, 2059267624277869210, 510733906447812518, 1071007686057160105, 3808697128436486247, 4532370378841381999], then independently rerun across the disjoint confirmatory-replication IDs [2354976006981955819, 4324660935519791914, 831562771514012917, 2751327354233951026, 1512451331433289100, 2339623576096759615, 942097766754537929, 299423626648925212, 1613961540201361027, 2495779494466921665, 3286046173524442755, 1226876407126695882, 2822438373310273476, 3359112155736441787, 4589841592586339548, 2174476099861496296, 4400594877164728163, 1473987275448740522, 3560021299613277498, 1963134501751537655, 3857100197921599726, 1946187660472806283, 534240155361867711, 2257819899425946518, 1857067766385637398, 1542467500088558298, 2565902916065722756, 4469043849214490585, 2459162917649737361, 2486378516630103661, 285328054388411115, 2406669371174695006, 446452795583064019, 4179188943919088022, 493150260764163842, 3754155167337633593, 2778791489195799033, 1918504031098073709, 3156095766939290846, 1998442627702540335, 2669942370954230662, 427097415724880873, 1648269874916305333]. For every metric (held-out classification accuracy) we report the per-condition mean with a bootstrap 95% confidence interval separately in each block. The proposed-vs-baseline difference on the primary metric ('held-out classification accuracy') is tested with a two-sided paired sign-flip randomisation test and a paired bootstrap confidence interval, together with Cohen's dz, applying the identical preregistered decision rule independently to primary and replication without pooling. Secondary-metric p-values use Holm family-wise-error correction. Every declared negative control is executed in both seed blocks under its registered condition ID and reported descriptively, but is excluded from the primary decision. The seed identities, metrics, and comparisons are fixed now; none are added after seeing the results. Smallest worthwhile effect: 0.0125098 proportion on H_s. Power justification: Prospective paired normal approximation with two-sided alpha=0.05: planning SD(H_s)=0.0250196 proportion, worthwhile effect=0.0125098, target power=0.90, required n=43; fixed n=43. Planning-SD basis: Immutable calibration record 4aad7be5-2893-4878-b5b0-ed773e8cbb5c; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155. Worthwhile-effect basis: Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).. Stopping rule: Run every preregistered primary and replication seed exactly once per condition for the fixed training/evaluation budget; analyze the two blocks separately with no outcome-dependent stopping, pooling, or seed replacement.. Multiplicity: No multiplicity: single primary contrast per block; decision based on one 95% CI.. Negative control(s) negative_control_1 are registered as validity conditions for the primary inference: if such a control acts on no seed of the primary block or on no seed of the replication block, the primary inference is invalid and is not reported as a result.
