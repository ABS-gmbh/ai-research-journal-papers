# Preregistration

> 🤖 This record was written by the autonomous pipeline at the DESIGN stage,
> BEFORE the experiment was executed, and committed unchanged. It fixes the
> hypothesis, the predicted effect, the metrics, and the analysis plan in advance
> so the reported findings cannot be retrofitted to the results (HARKing).

- **Registered at:** 2026-09-12T01:33:38.353362+00:00
- **Experiment:** Cross-Layer Query Consistency Loss for Subject-Disjoint Generalization in Time-Series Transformers
- **Research question:** Does enforcing cross-layer consistency in attention query projections, where deeper layer weights are regularized toward shallower layer weights, improve subject-disjoint generalization in time-series transformers?
- **Primary metric:** held-out classification accuracy
- **Metrics:** held-out classification accuracy
- **Baselines:** Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (loss term). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.
- **Publication policy:** publish_all_valid_outcomes
- **Publishable valid outcomes:** direction_supported, direction_refuted, inconclusive
- **Seeds per condition:** 43
- **Primary seed IDs:** 2615122547193570606, 252200600861128310, 634766601307347027, 2289833669515924996, 1075721894937126869, 2219905518708798979, 1472572688149772095, 3154489071090469597, 2567160067431731676, 375878476100283907, 3680443165500893007, 2412595240837917458, 2601790489635802822, 1913826313556203271, 710938911890137278, 4578385222592080447, 3998799165023144543, 3601994374998462166, 517409047000623439, 3812347621373549969, 3406080211412548461, 772595819596432589, 3615834778985602079, 1415494652153299218, 2062219541250864404, 142389970181333221, 4434070341016929754, 1135820606004933817, 3780975103128256366, 4407244770048434366, 4376044843392817728, 3255929081425547334, 3574102472552171439, 19016511533479923, 2933058706039751666, 3462839959629419857, 4607211731052019561, 2779871998158610606, 1485808255187976782, 3471275713396068135, 4429899216283540008, 1385236021301736380, 1330453660667172384
- **Executed confirmatory-replication seed IDs:** 2340648136914159678, 4191649941990144526, 914975885928187538, 3493291245950488, 3092035777930482330, 3033986887553884854, 1948116001888441515, 3721334120068172834, 1629568842510008, 3605262731553156275, 3904049989082932630, 892823242471123166, 3725427329689760378, 3555864911429215929, 3606907749333550835, 2155528049710964782, 2789562881046154133, 1853921749424354694, 1745680992267274019, 841184256946095993, 3464957341317932123, 775787681821570599, 3309282745006621851, 146154474434366067, 2391332672707033902, 706889780011171718, 2426763361766452408, 3736121309580882765, 479020209906455928, 1963761814288298963, 2233713330617425866, 2745262338024609657, 2296843351460209463, 2142392810908805088, 1468658092695416100, 2052272999620538285, 3506933794820522738, 351506867199205715, 4557863017481180823, 2654635865597404598, 3394110221015017757, 3791841174141345598, 3513984727252394996

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
    "Scope (server-owned): single calibrated testbed uci_har_small_transformer_v1 \u2014 UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows); model PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)); evaluated as the official UCI HAR test split \u2014 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning",
    "For each seed, both conditions use identical initialization, data split/order, stochastic draws, hyperparameters, tuning, update count, and compute budget.",
    "Model and optimizer state are reset independently for each condition; no trained state is carried between paired runs."
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
  "replication_plan": "Independently repeat the same paired protocol using both conditions for every disjoint replication seed ID [2340648136914159678, 4191649941990144526, 914975885928187538, 3493291245950488, 3092035777930482330, 3033986887553884854, 1948116001888441515, 3721334120068172834, 1629568842510008, 3605262731553156275, 3904049989082932630, 892823242471123166, 3725427329689760378, 3555864911429215929, 3606907749333550835, 2155528049710964782, 2789562881046154133, 1853921749424354694, 1745680992267274019, 841184256946095993, 3464957341317932123, 775787681821570599, 3309282745006621851, 146154474434366067, 2391332672707033902, 706889780011171718, 2426763361766452408, 3736121309580882765, 479020209906455928, 1963761814288298963, 2233713330617425866, 2745262338024609657, 2296843351460209463, 2142392810908805088, 1468658092695416100, 2052272999620538285, 3506933794820522738, 351506867199205715, 4557863017481180823, 2654635865597404598, 3394110221015017757, 3791841174141345598, 3513984727252394996]; reset all state and apply the identical hypothesis-positive contrast and fixed CI decision rule.",
  "replication_seed_ids": [
    2340648136914159678,
    4191649941990144526,
    914975885928187538,
    3493291245950488,
    3092035777930482330,
    3033986887553884854,
    1948116001888441515,
    3721334120068172834,
    1629568842510008,
    3605262731553156275,
    3904049989082932630,
    892823242471123166,
    3725427329689760378,
    3555864911429215929,
    3606907749333550835,
    2155528049710964782,
    2789562881046154133,
    1853921749424354694,
    1745680992267274019,
    841184256946095993,
    3464957341317932123,
    775787681821570599,
    3309282745006621851,
    146154474434366067,
    2391332672707033902,
    706889780011171718,
    2426763361766452408,
    3736121309580882765,
    479020209906455928,
    1963761814288298963,
    2233713330617425866,
    2745262338024609657,
    2296843351460209463,
    2142392810908805088,
    1468658092695416100,
    2052272999620538285,
    3506933794820522738,
    351506867199205715,
    4557863017481180823,
    2654635865597404598,
    3394110221015017757,
    3791841174141345598,
    3513984727252394996
  ],
  "sample_size_rationale": "Prospective paired normal approximation with two-sided alpha=0.05: planning SD(H_s)=0.0250196 proportion, worthwhile effect=0.0125098, target power=0.90, required n=43; fixed n=43. Planning-SD basis: Immutable calibration record ef4188ff-a4a8-4720-a3a7-f59d889d0c94; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155. Worthwhile-effect basis: Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).",
  "seed_ids": [
    2615122547193570606,
    252200600861128310,
    634766601307347027,
    2289833669515924996,
    1075721894937126869,
    2219905518708798979,
    1472572688149772095,
    3154489071090469597,
    2567160067431731676,
    375878476100283907,
    3680443165500893007,
    2412595240837917458,
    2601790489635802822,
    1913826313556203271,
    710938911890137278,
    4578385222592080447,
    3998799165023144543,
    3601994374998462166,
    517409047000623439,
    3812347621373549969,
    3406080211412548461,
    772595819596432589,
    3615834778985602079,
    1415494652153299218,
    2062219541250864404,
    142389970181333221,
    4434070341016929754,
    1135820606004933817,
    3780975103128256366,
    4407244770048434366,
    4376044843392817728,
    3255929081425547334,
    3574102472552171439,
    19016511533479923,
    2933058706039751666,
    3462839959629419857,
    4607211731052019561,
    2779871998158610606,
    1485808255187976782,
    3471275713396068135,
    4429899216283540008,
    1385236021301736380,
    1330453660667172384
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

Each condition (the proposed method vs the baseline(s): Control arm, defined by what the harness guarantees rather than by a description of the intervention. Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms. Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path. The harness invokes the registered lifecycle machinery in both arms, so the control arm reaches every registered point on the same inputs (loss term). One intervention implementation serves every arm: the harness tells it which condition it is running in, so the pseudocode describes the intervention arm and the control arm is the same code taking its control branch. In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective. The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them, so the control's recorded activity is zero or the experiment yields no result at all. Held-out evaluation reads the trained base parameters in both arms, and there is no evaluation-time lifecycle point, so no intervention state can reach evaluation. Per-step computational cost is deliberately not held equal between the arms and is not an outcome of this study.) is first run across the 43 primary random seeds fixed in advance with exact IDs [2615122547193570606, 252200600861128310, 634766601307347027, 2289833669515924996, 1075721894937126869, 2219905518708798979, 1472572688149772095, 3154489071090469597, 2567160067431731676, 375878476100283907, 3680443165500893007, 2412595240837917458, 2601790489635802822, 1913826313556203271, 710938911890137278, 4578385222592080447, 3998799165023144543, 3601994374998462166, 517409047000623439, 3812347621373549969, 3406080211412548461, 772595819596432589, 3615834778985602079, 1415494652153299218, 2062219541250864404, 142389970181333221, 4434070341016929754, 1135820606004933817, 3780975103128256366, 4407244770048434366, 4376044843392817728, 3255929081425547334, 3574102472552171439, 19016511533479923, 2933058706039751666, 3462839959629419857, 4607211731052019561, 2779871998158610606, 1485808255187976782, 3471275713396068135, 4429899216283540008, 1385236021301736380, 1330453660667172384], then independently rerun across the disjoint confirmatory-replication IDs [2340648136914159678, 4191649941990144526, 914975885928187538, 3493291245950488, 3092035777930482330, 3033986887553884854, 1948116001888441515, 3721334120068172834, 1629568842510008, 3605262731553156275, 3904049989082932630, 892823242471123166, 3725427329689760378, 3555864911429215929, 3606907749333550835, 2155528049710964782, 2789562881046154133, 1853921749424354694, 1745680992267274019, 841184256946095993, 3464957341317932123, 775787681821570599, 3309282745006621851, 146154474434366067, 2391332672707033902, 706889780011171718, 2426763361766452408, 3736121309580882765, 479020209906455928, 1963761814288298963, 2233713330617425866, 2745262338024609657, 2296843351460209463, 2142392810908805088, 1468658092695416100, 2052272999620538285, 3506933794820522738, 351506867199205715, 4557863017481180823, 2654635865597404598, 3394110221015017757, 3791841174141345598, 3513984727252394996]. For every metric (held-out classification accuracy) we report the per-condition mean with a bootstrap 95% confidence interval separately in each block. The proposed-vs-baseline difference on the primary metric ('held-out classification accuracy') is tested with a two-sided paired sign-flip randomisation test and a paired bootstrap confidence interval, together with Cohen's dz, applying the identical preregistered decision rule independently to primary and replication without pooling. Secondary-metric p-values use Holm family-wise-error correction. Every declared negative control is executed in both seed blocks under its registered condition ID and reported descriptively, but is excluded from the primary decision. The seed identities, metrics, and comparisons are fixed now; none are added after seeing the results. Smallest worthwhile effect: 0.0125098 proportion on H_s. Power justification: Prospective paired normal approximation with two-sided alpha=0.05: planning SD(H_s)=0.0250196 proportion, worthwhile effect=0.0125098, target power=0.90, required n=43; fixed n=43. Planning-SD basis: Immutable calibration record ef4188ff-a4a8-4720-a3a7-f59d889d0c94; baseline-only paired-null bootstrap UCL80 under recipe sha256:94f3ad0aa281d8b6845da79f0abcea1cd604a36c8b00ffcce5861e16cc4ff155. Worthwhile-effect basis: Versioned policy accuracy_fraction_v1 in proportion: max(absolute floor 0.005, fixed SD multiplier).. Stopping rule: Run every preregistered primary and replication seed exactly once per condition for the fixed training/evaluation budget; analyze the two blocks separately with no outcome-dependent stopping, pooling, or seed replacement.. Multiplicity: Primary hypothesis tested only on primary block with fixed decision rule. Replication block analyzed separately with same frozen rule, not pooled. Ablations and robustness checks are exploratory with Bonferroni correction (alpha/number of ablation conditions). Family-wise error rate controlled at 0.05 for primary contrast..
