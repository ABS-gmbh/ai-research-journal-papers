# Preregistration

> 🤖 This record was written by the autonomous pipeline at the DESIGN stage,
> BEFORE the experiment was executed, and committed unchanged. It fixes the
> hypothesis, the predicted effect, the metrics, and the analysis plan in advance
> so the reported findings cannot be retrofitted to the results (HARKing).

- **Registered at:** 2026-10-14T22:26:38.493599+00:00
- **Experiment:** Replication: Cross-Layer Query Consistency Loss for Subject-Disjoint Generalization in Time-Series Transformers
- **Research question:** Does enforcing cross-layer consistency in attention query projections, where deeper layer weights are regularized toward shallower layer weights, improve subject-disjoint generalization in time-series transformers?
- **Study type:** replication research

Replication research of Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers. Original protocol: https://github.com/ABS-gmbh/ai-research-journal-papers/tree/80ff8c2d68c28c765b1bbc35d7bf30e2b8ac042d/papers/e5c7eb4e-f542-4c7d-bcd0-6ceff9b99e91 at commit 80ff8c2d68c28c765b1bbc35d7bf30e2b8ac042d; sha256:74440f5a36e0e5f2612524f1eae42c8ab490029cc32a18634ae6e1af274d0801. Reason (independent_confirmation): Inquiry selected this independently seeded exact replication from the current Episteme evidence state. It tests whether the registered conclusion remains stable under fresh sampling, accounting for possible flaws in a single study. All prior outcomes are disclosed and every valid outcome will be reported. The selection is exploratory; its value is sensitive to the stated flaw-rate assumption. It makes no claim of an original discovery. This is a new preregistered independent test, not an original discovery. The prior outcomes, including invalid or retracted evidence, are disclosed in replication.json and the preregistration.

- **Primary metric:** held-out classification accuracy
- **Metrics:** held-out classification accuracy
- **Baselines:** Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (loss term). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.
- **Publication policy:** publish_all_valid_outcomes
- **Publishable valid outcomes:** direction_supported, direction_refuted, inconclusive
- **Seeds per condition:** 43
- **Primary seed IDs:** 1283456944311395052, 3089827065251130706, 3820704350825163869, 21236671524869010, 3415510045131152228, 2471081763373673405, 2374229508893286820, 2544941384231390184, 1567606677881050665, 2053777282625161573, 1221184456753876155, 3840525734538224513, 3504834781713389789, 77032002028652062, 4286278862225646279, 52245002576694452, 3986941535421188655, 4071087587955586190, 3260374718512374155, 4461885864847931220, 491323389332414539, 496860537829936944, 1932727500076940062, 3540548724348848006, 2513328952985036215, 609131993201635141, 4204928448906752539, 170530799314395416, 4086858104574164556, 2837886427063813598, 524975045864782648, 1034243053804099323, 2213998415094885164, 4277462776836849410, 369187523183942457, 2922011945439219839, 4356023442558125597, 3546063947330525743, 823309675197582790, 2178248810602791538, 1462835975243560544, 3406899122066815415, 2216116664296627259
- **Executed confirmatory-replication seed IDs:** 977459171940437340, 4488684769213213828, 1946600601137041155, 3416445909951360620, 94015168479249032, 245818450391945052, 4163063857117823088, 2717512241999814344, 3272748125613112133, 2370826470989774210, 1246227564208053654, 1763313708890820020, 4237763328141452310, 189961628016980323, 3945708179936401034, 469354882092208534, 2362016536193918241, 159255973982391164, 4365608024907845659, 387604714248465277, 745895122294483880, 46716666623954822, 4499449375448926851, 3008410952988380379, 2884677716462523534, 989949122925515117, 778369360471311952, 2224210984340661255, 2176941969250537915, 3008498851693170318, 2776754912777002994, 1890870248134977771, 882560239534186207, 297046870819713949, 1418335113356987113, 1214865161567177267, 4237397377132919006, 1869765722857981507, 448793344464843120, 1346906245604336130, 816203111240928895, 1477596452365914441, 4367633781936564098

## Hypothesis

The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion.

## Predicted direction / effect

The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion. Specifically, we predict: The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion.

## Fixed operational specification

```json
{
  "alternative_hypotheses": [
    "Cross-layer consistency limits model capacity, reducing both training and test accuracy",
    "Effect only appears in deeper transformers (>2 blocks), not visible in 2-block architecture",
    "Consistency helps early training but harms convergence, yielding mixed effects on final accuracy"
  ],
  "boundary_conditions": [
    "Only tested on 2-block PreNormTransformerEncoder; effect may differ with more depth",
    "Only tested on UCI HAR inertial sensor data; may not generalize to other time-series modalities",
    "Coefficient 0.01 fixed; different values may yield different effects",
    "Only query projections tested; key/value/output projections may show different patterns",
    "For each seed, both conditions use identical initialization, data split/order, stochastic draws, hyperparameters, tuning, update count, and compute budget.",
    "Model and optimizer state are reset independently for each condition; no trained state is carried between paired runs.",
    "Scope (server-owned): single calibrated testbed uci_har_small_transformer_v1 \u2014 UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows); model PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)); evaluated as the official UCI HAR test split \u2014 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning"
  ],
  "calibration_record_id": "ef4188ff-a4a8-4720-a3a7-f59d889d0c94",
  "canonical_hypothesis": "The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion.",
  "comparator": "Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step \u2014 the same forward pass, the same classification objective, the same backward pass and the same optimizer update \u2014 and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (loss term). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.",
  "decision_consequence": "If supported: Cross-layer attention consistency should be tested as a regularization option for PreNormTransformerEncoder architectures on subject-disjoint UCI HAR-like time-series tasks. If the preregistered primary contrast refutes the hypothesis, discouraging consistency constraints in this setting. If inconclusive: Effect may exist but requires different coefficient values, more training epochs, or larger model capacity to detect in this testbed.",
  "decision_value": "Using the two-sided paired-bootstrap 95% CI for mean(H_s), support the preregistered directional effect only when CI_low > 0.0125098; refute that directional effect when CI_high <= 0; otherwise report inconclusive. The paired sign-flip p-value is descriptive and does not replace this decision rule. Decision consequence: If supported: Cross-layer attention consistency should be tested as a regularization option for PreNormTransformerEncoder architectures on subject-disjoint UCI HAR-like time-series tasks. If the preregistered primary contrast refutes the hypothesis, discouraging consistency constraints in this setting. If inconclusive: Effect may exist but requires different coefficient values, more training epochs, or larger model capacity to detect in this testbed.",
  "estimand": "Hypothesis-positive paired contrast H_s = outcome_intervention - outcome_comparator; estimand = arithmetic mean of H_s over the preregistered primary seed IDs.",
  "failure_handling": "A non-finite outcome is never a data point: the harness raises on any non-finite value for either condition in that seed pair, so the job fails and reports nothing rather than a value it did not measure. No preregistered seed is discarded, skipped, or rerun, and no outcome is imputed.",
  "falsification_criteria": [
    "Refute the preregistered directional effect when the two-sided paired-bootstrap 95% CI upper endpoint for mean(H_s) is <= 0.",
    "Do not claim a worthwhile directional effect unless that CI's lower endpoint exceeds the fixed margin 0.0125098 proportion."
  ],
  "hypothesis_positive_multiplier": 1,
  "hypothesized_direction": "intervention_better",
  "intervention": "Server-bound target blocks.1.attn.q_proj.weight has stored tensor shape (64, 64). Add loss term that applies Frobenius norm consistency regularization to blocks.1.attn.q_proj.weight",
  "intervention_protocol": {
    "application_timing": "Executed lifecycle (server-owned): the operator is invoked during loss computation of every optimization step: the operator's term is added to the classification objective inside the autograd graph, so the combined objective is what is differentiated and every operator-owned parameter is trained by it.",
    "execution_phases": [
      "loss_term"
    ],
    "invariants": [
      "Reference weights from block 0 are detached and receive no gradients",
      "Loss term is differentiable with respect to target parameters only",
      "Coefficient is fixed across all steps and seeds"
    ],
    "learns_parameters": false,
    "normalization_rule": "No normalization; raw Frobenius norm squared scaled by fixed coefficient",
    "numerical_safeguards": "Coefficient 0.01 prevents loss_term from dominating classification objective; diff computation uses standard floating-point subtraction",
    "operator_name": "CrossLayerQueryConsistency",
    "ordering_rule": "Element-wise subtraction then sum; order-invariant due to commutativity of addition",
    "pseudocode": [
      "Retrieve reference_weights from model.blocks[0].attn.q_proj.weight",
      "Detach reference_weights from gradient graph to prevent gradients flowing to block 0",
      "Compute diff = target - reference_weights",
      "Compute squared_elements = diff * diff (element-wise)",
      "Compute loss_raw = sum(squared_elements) over all elements",
      "Set consistency_coefficient = 0.01",
      "Compute loss_term = consistency_coefficient * loss_raw",
      "Store loss_term in scratch dict for harness aggregation",
      "Return loss_term to harness for addition to training objective",
      "Scope (server-owned): control arm. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (loss term). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. If the condition the harness passes in is a control condition, return here: add no term to the training objective, and leave the registered target parameter and that parameter's optimizer momentum buffer exactly as received. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study."
    ],
    "tensor_axis_or_scope": "Full weight matrix [64, 64] treated as flat parameter space"
  },
  "intervention_target": "blocks.1.attn.q_proj.weight",
  "intervention_target_shape": [
    64,
    64
  ],
  "leakage_risks": [
    "Reference weights from block 0 could indirectly encode subject-specific information if block 0 overfits; consistency would then propagate this to block 1",
    "Loss term computation must not access test data or subject identifiers",
    "Random matrix for negative control must be generated once at training start and fixed, not regenerated per-step"
  ],
  "mechanistic_rationale": "Cross-layer query consistency encourages the second transformer block to attend to similar temporal patterns as the first block, potentially learning more stable, subject-invariant attention mechanisms. If subject-specific variations cause layers to diverge in what they attend to, consistency regularization may prevent overfitting to idiosyncratic temporal features. However, if deeper layers need to refine attention patterns based on first-layer outputs, consistency may limit representational capacity.",
  "negative_controls": [
    "Add loss term penalizing difference between blocks.1.attn.q_proj.weight and a fixed random matrix with same shape and norm as block 0's weights, destroying the meaningful cross-layer relationship while matching compute"
  ],
  "outcome_formula": "number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split",
  "outcome_higher_is_better": true,
  "outcome_name": "held-out classification accuracy",
  "outcome_range_max": 1.0,
  "outcome_range_min": 0.0,
  "outcome_unit": "proportion",
  "planning_sd": 0.025019595493970412,
  "planning_sd_basis": "Immutable calibration record ef4188ff-a4a8-4720-a3a7-f59d889d0c94; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155.",
  "population": "Training runs on UCI HAR subject-disjoint split with PreNormTransformerEncoder architecture under fixed SGD optimization",
  "primary_outcome": "held-out classification accuracy: number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split; unit=proportion; range=[0, 1]; computed once per seeded run; higher is better; failure handling: A non-finite outcome is never a data point: the harness raises on any non-finite value for either condition in that seed pair, so the job fails and reports nothing rather than a value it did not measure. No preregistered seed is discarded, skipped, or rerun, and no outcome is imputed.",
  "replication_plan": "Independently repeat the same paired protocol using both conditions for every disjoint replication seed ID [977459171940437340, 4488684769213213828, 1946600601137041155, 3416445909951360620, 94015168479249032, 245818450391945052, 4163063857117823088, 2717512241999814344, 3272748125613112133, 2370826470989774210, 1246227564208053654, 1763313708890820020, 4237763328141452310, 189961628016980323, 3945708179936401034, 469354882092208534, 2362016536193918241, 159255973982391164, 4365608024907845659, 387604714248465277, 745895122294483880, 46716666623954822, 4499449375448926851, 3008410952988380379, 2884677716462523534, 989949122925515117, 778369360471311952, 2224210984340661255, 2176941969250537915, 3008498851693170318, 2776754912777002994, 1890870248134977771, 882560239534186207, 297046870819713949, 1418335113356987113, 1214865161567177267, 4237397377132919006, 1869765722857981507, 448793344464843120, 1346906245604336130, 816203111240928895, 1477596452365914441, 4367633781936564098]; reset all state and apply the identical hypothesis-positive contrast and fixed CI decision rule.",
  "replication_seed_ids": [
    977459171940437340,
    4488684769213213828,
    1946600601137041155,
    3416445909951360620,
    94015168479249032,
    245818450391945052,
    4163063857117823088,
    2717512241999814344,
    3272748125613112133,
    2370826470989774210,
    1246227564208053654,
    1763313708890820020,
    4237763328141452310,
    189961628016980323,
    3945708179936401034,
    469354882092208534,
    2362016536193918241,
    159255973982391164,
    4365608024907845659,
    387604714248465277,
    745895122294483880,
    46716666623954822,
    4499449375448926851,
    3008410952988380379,
    2884677716462523534,
    989949122925515117,
    778369360471311952,
    2224210984340661255,
    2176941969250537915,
    3008498851693170318,
    2776754912777002994,
    1890870248134977771,
    882560239534186207,
    297046870819713949,
    1418335113356987113,
    1214865161567177267,
    4237397377132919006,
    1869765722857981507,
    448793344464843120,
    1346906245604336130,
    816203111240928895,
    1477596452365914441,
    4367633781936564098
  ],
  "sample_size_rationale": "Prospective paired normal approximation with two-sided alpha=0.05: planning SD(H_s)=0.0250196 proportion, worthwhile effect=0.0125098, target power=0.90, required n=43; fixed n=43. Planning-SD basis: Immutable calibration record ef4188ff-a4a8-4720-a3a7-f59d889d0c94; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155. Worthwhile-effect basis: Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).",
  "seed_ids": [
    1283456944311395052,
    3089827065251130706,
    3820704350825163869,
    21236671524869010,
    3415510045131152228,
    2471081763373673405,
    2374229508893286820,
    2544941384231390184,
    1567606677881050665,
    2053777282625161573,
    1221184456753876155,
    3840525734538224513,
    3504834781713389789,
    77032002028652062,
    4286278862225646279,
    52245002576694452,
    3986941535421188655,
    4071087587955586190,
    3260374718512374155,
    4461885864847931220,
    491323389332414539,
    496860537829936944,
    1932727500076940062,
    3540548724348848006,
    2513328952985036215,
    609131993201635141,
    4204928448906752539,
    170530799314395416,
    4086858104574164556,
    2837886427063813598,
    524975045864782648,
    1034243053804099323,
    2213998415094885164,
    4277462776836849410,
    369187523183942457,
    2922011945439219839,
    4356023442558125597,
    3546063947330525743,
    823309675197582790,
    2178248810602791538,
    1462835975243560544,
    3406899122066815415,
    2216116664296627259
  ],
  "smallest_worthwhile_effect": "0.0125098 proportion on H_s",
  "smallest_worthwhile_effect_basis": "Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).",
  "smallest_worthwhile_effect_value": 0.012509797746985206,
  "target_power": 0.9,
  "testbed_id": "uci_har_small_transformer_v1",
  "unit_of_analysis": "One seeded training run (intervention and comparator paired by seed)"
}
```

## Analysis plan (statistics + seeds)

Each condition (the proposed method vs the baseline(s): Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (loss term). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.) is first run across the 43 primary random seeds fixed in advance with exact IDs [1283456944311395052, 3089827065251130706, 3820704350825163869, 21236671524869010, 3415510045131152228, 2471081763373673405, 2374229508893286820, 2544941384231390184, 1567606677881050665, 2053777282625161573, 1221184456753876155, 3840525734538224513, 3504834781713389789, 77032002028652062, 4286278862225646279, 52245002576694452, 3986941535421188655, 4071087587955586190, 3260374718512374155, 4461885864847931220, 491323389332414539, 496860537829936944, 1932727500076940062, 3540548724348848006, 2513328952985036215, 609131993201635141, 4204928448906752539, 170530799314395416, 4086858104574164556, 2837886427063813598, 524975045864782648, 1034243053804099323, 2213998415094885164, 4277462776836849410, 369187523183942457, 2922011945439219839, 4356023442558125597, 3546063947330525743, 823309675197582790, 2178248810602791538, 1462835975243560544, 3406899122066815415, 2216116664296627259], then independently rerun across the disjoint confirmatory-replication IDs [977459171940437340, 4488684769213213828, 1946600601137041155, 3416445909951360620, 94015168479249032, 245818450391945052, 4163063857117823088, 2717512241999814344, 3272748125613112133, 2370826470989774210, 1246227564208053654, 1763313708890820020, 4237763328141452310, 189961628016980323, 3945708179936401034, 469354882092208534, 2362016536193918241, 159255973982391164, 4365608024907845659, 387604714248465277, 745895122294483880, 46716666623954822, 4499449375448926851, 3008410952988380379, 2884677716462523534, 989949122925515117, 778369360471311952, 2224210984340661255, 2176941969250537915, 3008498851693170318, 2776754912777002994, 1890870248134977771, 882560239534186207, 297046870819713949, 1418335113356987113, 1214865161567177267, 4237397377132919006, 1869765722857981507, 448793344464843120, 1346906245604336130, 816203111240928895, 1477596452365914441, 4367633781936564098]. For every metric (held-out classification accuracy) we report the per-condition mean with a bootstrap 95% confidence interval separately in each block. The proposed-vs-baseline difference on the primary metric ('held-out classification accuracy') is tested with a two-sided paired sign-flip randomisation test and a paired bootstrap confidence interval, together with Cohen's dz, applying the identical preregistered decision rule independently to primary and replication without pooling. Secondary-metric p-values use Holm family-wise-error correction. Every declared negative control is executed in both seed blocks under its registered condition ID and reported descriptively, but is excluded from the primary decision. The seed identities, metrics, and comparisons are fixed now; none are added after seeing the results. Smallest worthwhile effect: 0.0125098 proportion on H_s. Power justification: Prospective paired normal approximation with two-sided alpha=0.05: planning SD(H_s)=0.0250196 proportion, worthwhile effect=0.0125098, target power=0.90, required n=43; fixed n=43. Planning-SD basis: Immutable calibration record ef4188ff-a4a8-4720-a3a7-f59d889d0c94; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155. Worthwhile-effect basis: Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).. Stopping rule: Run every preregistered primary and replication seed exactly once per condition for the fixed training/evaluation budget; analyze the two blocks separately with no outcome-dependent stopping, pooling, or seed replacement.. Multiplicity: Primary analysis: one hypothesis test per block (primary, replication) on mean(H_s) with paired-bootstrap 95% CI. No correction across blocks as they are independent confirmatory tests. Ablations and robustness checks are exploratory with descriptive statistics only, not used for primary decision. Negative controls tested with same CI rule but not part of primary hypothesis..
