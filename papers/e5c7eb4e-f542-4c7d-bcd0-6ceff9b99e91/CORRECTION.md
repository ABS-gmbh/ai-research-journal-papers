# Editorial correction

Version 2. The negative control is an active penalty toward a fixed random matrix, not a passive arm, and it is a diagnostic for the cross-layer reference rather than evidence that the harness is unbiased. Only accuracy was measured, so mechanisms are now stated as untested hypotheses; the margin is a calibration-derived threshold, and the mismatch between the preregistered power and the support rule is disclosed. The title no longer describes the study as a test of attention stability, and the preregistered pseudocode is rendered with its registered names. Both registered decisions are inconclusive, as before. This version replaces the AI-generation disclosure with one composed from the recorded editorial history, corrects 8 sentences in the Abstract section in this editorial correction, corrects 4 sentences in the Conclusion section in this editorial correction, corrects 17 sentences in the Discussion section in this editorial correction, corrects 8 sentences in the Experimental Setup section in this editorial correction, corrects 12 sentences in the Introduction section in this editorial correction, corrects 8 sentences in the Limitations section in this editorial correction, corrects 25 sentences in the Method section in this editorial correction, corrects 14 sentences in the Related Work section in this editorial correction, corrects 15 sentences in the Results section in this editorial correction, corrects 1 sentence in the Title section in this editorial correction, and removes 28 references and corrects the bibliographic details of four references. No other section, reference, figure or table differs from the previous version; CORRECTION.md shows every changed sentence.

Previous version: 1; commit `1de5e7bdc4bdff944106d0af84fa1aa3ba9e8826`. The text was corrected by an AI assistant (Claude, Anthropic), at the direction of the journal's editor; the experiment, its execution, the registered analysis, the preregistration and the reproduction evidence are unchanged, and the corrected manuscript was reviewed again by the ordinary automated checks.

## title

```diff
--- published/title
+++ corrected/title
@@ -1 +1 @@
-Cross-Layer Query Consistency Loss Tests Whether Attention Stability Across Depth Improves Subject-Disjoint Generalization in Time-Series Transformers
+Cross-Layer Query-Weight Consistency Loss in a Two-Block Time-Series Transformer: A Preregistered Test on Subject-Disjoint Activity Recognition
```

## abstract

```diff
--- published/abstract
+++ corrected/abstract
@@ -1,11 +1,8 @@
-Transformers have become prominent in time-series analysis, yet whether architectural inductive biases improve subject-disjoint generalization remains unclear.
-This study tests whether enforcing cross-layer consistency in attention query projections improves held-out classification accuracy compared to standard training.
-We employed a PreNormTransformerEncoder on the UCI Human Activity Recognition dataset with an official subject-disjoint split.
-The intervention added a Frobenius norm consistency loss regularizing deeper block projections toward earlier blocks.
-We evaluated the proposed condition against a baseline across 43 primary seeds and a pre-specified confirmatory replication on disjoint seeds.
-In the primary cohort, the proposed condition improved accuracy by 0.00133 (95% CI [-0.00315, 0.0056], p=0.546).
-In the replication cohort, the proposed condition worsened accuracy by -0.00157 (95% CI [-0.00487, 0.00182], p=0.372).
-Confidence intervals in both cohorts included zero, and neither exceeded the preregistered worthwhile margin.
-Variation across observations is attributed to the seeds that produced them.
-The results are inconclusive.
-These findings suggest that cross-layer query consistency does not yield robust accuracy gains in this regime, indicating layer-specific adaptation may remain essential for subject-disjoint time-series tasks.
+Whether constraining how a transformer's weights relate across depth helps it generalize to unseen people is not settled for time-series classification.
+This preregistered study tests whether a cross-layer consistency loss on the query projection weights of the second of two attention blocks improves held-out classification accuracy over standard training in a two-block pre-norm transformer trained on the UCI Human Activity Recognition dataset and evaluated on its official subject-disjoint split.
+The loss adds 0.01 times the squared Frobenius distance between the second block's query projection weights and a detached copy of the first block's to the classification objective.
+We compared the proposed condition with a paired baseline on 43 primary seeds and on 43 disjoint confirmatory-replication seeds that reuse the same subjects and split.
+In the primary cohort the paired contrast was 0.00133, or 0.13 percentage points (95% CI [-0.00315, 0.0056], p=0.546); in the replication cohort it was -0.00157, or -0.16 percentage points (95% CI [-0.00487, 0.00182], p=0.372).
+Both intervals include zero and lie entirely below the preregistered threshold of 0.0125098 (1.251 percentage points), so neither cohort supports an improvement of that size, and both are classified as inconclusive under the preregistered rule.
+An active negative control, which pulls the same weights toward a fixed random matrix instead, reached mean accuracies of 0.908 and 0.907.
+Only accuracy was measured, so the study identifies no mechanism.
```

## introduction

```diff
--- published/introduction
+++ corrected/introduction
@@ -1,22 +1,11 @@
-Time-series classification using deep learning has advanced significantly with the adoption of Transformer architectures, which offer the ability to capture long-range dependencies and interactions within sequential data [6].
-In domains such as human activity recognition, models must generalize across subjects who exhibit different movement styles, sensor characteristics, and execution speeds.
-This subject-disjoint generalization is critical for deploying models in real-world settings where training data cannot cover all potential users.
-While Transformers have achieved superior performances in natural language processing and computer vision, their application to time series involves distinct challenges regarding temporal ordering and distribution shift [4].
-Standard deterministic training often fails to provide calibrated confidence under distribution shift, prompting investigation into architectural inductive biases that might enhance robustness.
-Existing literature addresses time-series transformer architectures and general regularization techniques, but no provided work specifically tests whether a cross-layer query consistency loss regularizing deeper block projections toward earlier blocks improves subject-disjoint generalization.
-Some works propose tackling forecasting problems with Transformers, demanding high prediction capacity to capture precise long-range dependency coupling [10].
-Others enhance locality to break memory bottlenecks [11], or propose efficient designs based on segmentation of time series into subseries-level patches [9].
-However, the validity of Transformer-based solutions for time series analysis tasks is questioned by findings that simple linear models can outperform sophisticated architectures in certain forecasting regimes [4].
-Furthermore, time series analysis is fundamentally different in nature to either vision or natural language processing with respect to self-supervised learning tasks, suggesting that mechanisms successful in other domains may not transfer directly [27].
-This gap matters because answering it clarifies whether transformer depth should encode progressively refined or consistently stable attention patterns for out-of-distribution time-series tasks.
-A positive result would justify testing whether cross-layer consistency transfers to other subject-disjoint time-series benchmarks.
-A negative result would indicate layer-specific adaptation is essential for this architecture class.
-Current regularization designs for temporal feature learning often assume specific weight geometries facilitate generalization, yet recent studies testing spectral entropy minimization of input projections reported inconclusive results and null accuracy gains over standard weight decay [2].
-Similarly, investigations into entropy maximization of multiplicative weight noise parameters carry retracted notices and cannot be relied upon for mechanistic conclusions [1].
-This paper reports a calibrated testbed experiment evaluating cross-layer query consistency loss.
-We adhere to a preregistered design to ensure honest reporting of outcomes.
-Our contributions are:
-- We implement a cross-layer query consistency loss that penalizes differences between block query projection weights in a time-series transformer.
-- We evaluate this intervention against a baseline and negative control on the UCI Human Activity Recognition dataset using an official subject-disjoint split.
-- We report results from both a primary cohort and a pre-specified confirmatory replication on disjoint seeds, attributing variation to the seeds that produced them.
-- We provide inconclusive evidence regarding the efficacy of cross-layer consistency for subject-disjoint generalization in this regime.
+Time-series classification using deep learning has advanced with the adoption of Transformer architectures, which can capture long-range dependencies and interactions within sequential data [5].
+In human activity recognition, models must generalize across subjects who differ in movement style, sensor placement and execution speed, which matters for deployment because training data cannot cover all potential users.
+Applying Transformers to time series raises distinct challenges, among them preserving temporal ordering [3].
+Prior work has proposed Transformer designs for long-sequence forecasting, a task that demands high prediction capacity to capture long-range dependency coupling [9], that enhance locality to break memory bottlenecks [10], or that segment time series into subseries-level patches [8].
+At the same time, simple linear models can outperform sophisticated Transformer architectures in some forecasting regimes [3], and time series analysis differs in nature from vision and natural language processing with respect to self-supervised learning tasks [12], so mechanisms that help in other domains may not transfer.
+On the same testbed as this study, a test of spectral entropy minimization of input projections reported inconclusive results, with no gain exceeding its preregistered margin and confidence intervals that included zero [2], and a study of entropy-maximized multiplicative weight noise carries a retraction notice, so its conclusions cannot be relied on [1].
+In the cited literature we found no test of whether a loss that pulls a deeper block's attention query weights toward an earlier block's improves subject-disjoint accuracy.
+This paper reports a preregistered test of that question on one calibrated testbed: a two-block pre-norm transformer encoder trained on the UCI Human Activity Recognition dataset and evaluated on its official subject-disjoint split.
+The intervention adds a cross-layer query-weight consistency penalty to the classification objective; it is compared with a paired baseline that adds nothing, and an active negative control pulls the same weights toward a fixed random matrix instead.
+A clear improvement would have motivated testing the penalty on other subject-disjoint benchmarks; an inconclusive result bounds the size of any benefit in this setting without identifying why.
+We evaluate the penalty against the baseline and the negative control on 43 primary seeds and on 43 disjoint confirmatory-replication seeds.
@@ -24 +13 @@
-We report the observed results against this prediction without alteration.
+We report the observed results against this prediction without alteration: both cohorts are inconclusive, and neither supports an improvement of the registered size.
```

## related_work

```diff
--- published/related_work
+++ corrected/related_work
@@ -1,22 +1,14 @@
-Transformers have triggered great interest in the time series community due to the ability to capture long-range dependencies and interactions [6].
-Several works propose tackling forecasting problems with Transformers, such as those demanding high prediction capacity to capture precise long-range dependency coupling [10].
-Others focus on enhancing locality and breaking the memory bottleneck of Transformer on time series forecasting by addressing locality-agnostics and memory costs [11].
-Efficient designs based on segmentation of time series into subseries-level patches have been proposed to retain local semantic information while reducing computation [9].
-However, research questions the validity of this line of research despite growing performance, noting that simple linear models can outperform Transformer-based solutions in long-term forecasting tasks [4].
-Regarding architectural mechanisms, the original Transformer architecture connects the encoder and decoder through an attention mechanism, dispensing with recurrence and convolutions entirely [7].
-Subsequent work introduces parameter-free changes to the standard attention mechanism which reduces attention to unneeded elements, consistently improving performance in various model sizes [8].
-Investigations into mechanisms underlying the ability for compositional generalization reformulate multi-head attention as a hypernetwork, revealing latent codes that specify key-query specific operations [33].
-In terms of position encoding, transformers require effective position encoding to capture the ordering of the time series data, yet the efficacy of absolute versus relative encoding remains controversial [5].
-Self-supervised representation learning for time series argues that the domain is fundamentally different in nature to either vision or natural language processing with respect to meaningful tasks [27].
-Large pre-trained time series models observe that tackling time-series analysis tasks usually involves designing and training a separate model, proposing adaptive segmentation to identify optimal dataset-specific strategies [18].
-However, citation audits require careful alignment between claims and abstract content; for instance, some papers focus on shape analysis for time series by representing data as deformations of a reference, rather than architectural inductive biases broadly [19].
-Similarly, clustering stability evaluation approaches extend mutual influence ideas using membership degrees, distinct from weight-space regularization comparisons [20].
-Regularization for temporal feature learning often assumes specific weight geometries facilitate generalization under distribution shift.
-One study tests whether enforcing a low-entropy singular value spectrum on input projection weights enhances held-out classification accuracy, reporting inconclusive results where neither estimate exceeded the preregistered margin and confidence intervals included zero [2].
-Another study investigates whether explicitly maximizing the entropy of multiplicative weight noise parameters improves out-of-distribution accuracy, but carries a retracted notice from the journal that published it due to implementation mismatches with the preregistered intervention [1].
-These findings suggest that spectral entropy minimization of input projections does not yield robust accuracy gains over standard weight decay in this regime.
-Uncertainty estimates are agreed to be missing from standard networks and Bayesian formalisms are the usual answer, but the same literature reports that the approximations needed to make them tractable are where the guarantees are lost — precisely the regime this study operates in.
-The present work positions itself against this background by testing a specific cross-layer consistency bias.
-Unlike weight-space regularization that targets input projections [2], our intervention targets attention query projections across depth.
-Unlike segmentation-based approaches that modify input tokens [9], we modify the training objective to encourage stability across layers.
-This distinction is critical because layer-specific adaptation may be essential for architectures processing inertial signals where subject variability manifests in temporal dynamics rather than just input distribution.
+Transformers have attracted wide interest in the time series community because they capture long-range dependencies and interactions [5].
+Several works tackle forecasting problems with Transformers, including designs for long-sequence forecasting, a task that demands high prediction capacity to capture precise long-range dependency coupling [9], designs that enhance locality and break the memory bottleneck on time series forecasting [10], and designs that segment time series into subseries-level patches to retain local semantic information while reducing computation [8].
+Other work questions this line of research, finding that simple linear models can outperform Transformer-based solutions in long-term forecasting [3].
+Regarding architectural mechanisms, the original Transformer is based solely on attention mechanisms, dispensing with recurrence and convolutions entirely [6].
+Subsequent work introduces parameter-free changes to the standard attention mechanism that reduce attention to unneeded elements and improve performance across model sizes [7].
+Work on compositional generalization reformulates multi-head attention as a hypernetwork, revealing latent codes that specify key-query specific operations [13].
+Transformers also require position encoding to capture the ordering of time series data, and the efficacy of absolute versus relative encoding remains controversial [4].
+Self-supervised representation learning for time series argues that the domain differs in nature from vision and natural language processing [12], and large pre-trained time series models address the need to design and train a separate model for each analysis task by learning dataset-specific segmentation strategies [11].
+Two earlier studies used the same testbed.
+One tested whether enforcing a low-entropy singular value spectrum on input projection weights improves held-out classification accuracy and reported inconclusive results, with neither cohort's estimate exceeding the preregistered margin and both confidence intervals including zero [2].
+Another investigated whether maximizing the entropy of multiplicative weight noise improves out-of-distribution accuracy, but it carries a retraction notice because the executed intervention did not implement the preregistered one [1].
+The present study is a narrow, preregistered evaluation on one human activity recognition testbed.
+Unlike regularization that targets input projections [2], it targets the attention query projection of the second block and relates it to the first block's; unlike segmentation-based approaches that change the input tokens [8], it changes only the training objective.
+Whether deeper blocks need layer-specific query weights in this architecture is the question the intervention probes; the study does not measure that property directly.
```

## method

```diff
--- published/method
+++ corrected/method
@@ -1,17 +1,15 @@
-The core operator is a Cross-Layer Query Consistency Loss added to the training objective.
-This intervention regularizes deeper block query projection weights toward shallower block weights.
-Specifically, a Frobenius norm consistency regularization term is added during training that penalizes the difference between block 1's query projection weights and block 0's query projection weights (detached).
-The loss term is computed as 0.01 * ||W_q1 - detach(W_q0)||_F^2, added to the classification objective.
-Gradients flow only to block 1's weights.
-This design tests the hypothesis that enforcing stability across depth improves generalization.
-The comparator is the baseline condition.
-Both intervention and baseline conditions use identical seeds, data ordering, initialization, and training steps.
-The only difference is whether the consistency loss term is added.
-The control arm is defined by what the harness guarantees rather than by a description of the intervention.
-Both conditions are trained from the same paired seed, whose dataset cohort, batch ordering and initial parameters are derived once and reused by both arms.
-Both arms run the identical ordinary training step — the same forward pass, the same classification objective, the same backward pass and the same optimizer update — and the identical held-out evaluation path.
-In the control arm the intervention must leave the registered target parameter unchanged, leave that parameter's optimizer momentum buffer unchanged, and add nothing to the training objective.
-The harness records what the intervention actually did at each lifecycle point, for every seed and every condition, and refuses to return results in which the control arm acted at any of them.
-A final LayerNorm(64) precedes mean-pool over time and a Linear(64,6) classification head.
-This architecture is selected to be large enough to learn temporal representations but small enough to train across many seeds for statistical power.
-The intervention targets the query projection weights within the self-attention modules, as these determine how temporal tokens attend to one another.
+The core operator is a cross-layer query consistency loss added to the training objective.
+It pulls the query projection weights of the second transformer block (block 1) toward those of the first (block 0).
+The added term is 0.01 * ||W_q1 - detach(W_q0)||_F^2, summed with the classification objective.
+Because block 0's weights are detached inside the penalty, the penalty's gradient reaches only block 1's query weights; block 0's query weights are still trained by the classification loss but receive no gradient from the penalty.
+The intervention is designed to change the relationship between the two blocks' query weights; no manipulation check was run, and the study does not measure attention patterns, weight distances during training, or gradient contributions.
+The comparator is the baseline condition, which adds nothing to the objective.
+Both conditions use identical seeds, data ordering, initialization and training steps; the only difference is whether the consistency term is added.
+In the server-written specification below, "control arm" denotes this baseline; the negative control described next is a separate, active condition.
+The registered negative control is active, not passive.
+It adds 0.01 * ||W_q1 - R||_F^2, where R is a random matrix drawn once per seed from the operator's own random stream, rescaled to the Frobenius norm of block 0's query weights when it is drawn, and then held fixed.
+It matches the proposed condition's form and coefficient but replaces the cross-layer reference with an unrelated fixed one, so it is a diagnostic for whether the specific cross-layer reference matters.
+Unlike the proposed reference, which moves as block 0 is trained, R does not change during training.
+The harness recorded the negative control acting on every training step of every seed.
+The model is a pre-norm transformer encoder: a linear input projection with a learned positional embedding, two blocks of four-head self-attention and a feed-forward network, a final LayerNorm(64), mean pooling over time and a Linear(64,6) classification head.
+The intervention targets the query projection weights within the self-attention modules, which determine how temporal tokens attend to one another.
@@ -19,5 +17,5 @@
-The preregistered decision rule compares the mean H_s against a fixed worthwhile margin of 0.0125098 proportion.
-If the lower bound of the 95% confidence interval exceeds this margin, the hypothesis is supported.
-If the interval includes zero, the result is inconclusive.
-This margin was set to reflect a practically significant improvement in activity recognition accuracy.
-The method isolates the effect of the consistency loss by pairing every condition on one seed, buying control over initialization variance at the cost of computational doubling per seed.
+The preregistered decision rule compares H_s with a fixed worthwhile margin of 0.0125098 proportion (1.251 percentage points): a cohort supports the hypothesis only if the lower bound of its 95% confidence interval exceeds the margin, and it is inconclusive unless its whole interval lies above the margin or at or below zero.
+The margin is derived from the calibration's measurement noise; it is not a judgment of practical significance.
+The preregistered 90% power refers to rejecting a zero effect when the true effect equals the margin; under the support rule, an effect exactly equal to the margin would give a lower bound above the margin only about one time in forty.
+We disclose this mismatch and keep the registered classification unchanged.
+The preregistered safeguard below states that the coefficient 0.01 keeps the term from dominating the classification objective; that was not checked during the run.
@@ -28 +26 @@
-- Applied: the operator is invoked during loss computation of every optimization step: the operator's term is added to the classification objective inside the autograd graph, so the combined objective is what is differentiated and every operator-owned parameter is trained by it..
+- Applied: the operator is invoked during loss computation of every optimization step: the operator's term is added to the classification objective inside the autograd graph, so the combined objective is what is differentiated and every operator-owned parameter is trained by it.
@@ -31 +29 @@
-- Numerical safeguards: Coefficient 0.01 prevents in the training objective from dominating classification objective; diff computation uses standard floating-point subtraction.
+- Numerical safeguards: Coefficient 0.01 prevents loss_term from dominating classification objective; diff computation uses standard floating-point subtraction.
@@ -46 +44 @@
-Compute in the training objective = consistency_coefficient * loss_raw
+Compute loss_term = consistency_coefficient * loss_raw
@@ -48 +46 @@
-Store in the training objective in scratch dict for harness aggregation
+Store loss_term in scratch dict for harness aggregation
@@ -50 +48 @@
-Return in the training objective to harness for addition to training objective
+Return loss_term to harness for addition to training objective
```

## experimental_setup

```diff
--- published/experimental_setup
+++ corrected/experimental_setup
@@ -1,10 +1,6 @@
-A subject-disjoint split tests what this question asks because it evaluates generalization to unseen subjects, whereas a random split would have hidden subject-specific overfitting.
-This design choice ensures that accuracy gains reflect robustness to inter-individual variability in movement styles and sensor characteristics rather than memorization of subject identities.
-We employed 43 primary seeds and 43 disjoint confirmatory-replication seeds.
-The identities are recorded in the appendix.
-We refer to the counts, never list them.
-Using this many seeds allows us to estimate the variation attributable to the seeds that produced them, rather than attributing variation to subjects.
-Each observation is one seed.
-Pairing every condition on one seed buys control over random initialization and batch ordering variance.
-The negative control rules out effects from the harness lifecycle machinery itself; without it, changes in evaluation paths would be indistinguishable from intervention effects.
-The first negative control uses the same harness but without the loss term active, ensuring the baseline is truly passive.
+A subject-disjoint split matches the question because it evaluates accuracy on subjects who appear nowhere in training, whereas a random split could hide subject-specific overfitting.
+We used 43 primary seeds and 43 disjoint confirmatory-replication seeds; their identities are recorded in the appendix.
+Each observation is one seed, and every condition is trained on the same seed, which controls for random initialization and batch ordering.
+The confirmatory replication reuses the same subjects, the same split and the same pipeline with new seeds, so it measures repeatability over training seeds, not replication on a new population.
+The active negative control, described in the Method, pulls the second block's query weights toward a fixed random matrix with the same coefficient; comparing it with the proposed condition indicates whether the cross-layer reference specifically matters, and comparing it with the baseline indicates whether a penalty of this form and size changes accuracy at all.
+It is a diagnostic; it is not evidence that the harness is unbiased, and no contrast involving it was registered.
@@ -13,10 +9,2 @@
-The analysis computes bootstrap 95% confidence intervals for mean accuracy and mean difference.
-We report both primary and confirmatory-replication cohorts separately.
-We never pool them or call a primary-only result replicated.
-The pre-specified confirmatory replication on disjoint seeds provides a second estimate of the effect size under identical design conditions but independent randomization.
-This setup justifies the design by ensuring that any observed difference is due to the consistency loss and not data split variance.
-The subject-disjoint split is the critical constraint; if we used a random split, the generalization claim would not hold for unseen subjects.
-The seed pairing ensures that the paired contrast H_s removes seed-specific noise.
-The negative control confirms that the harness does not introduce bias.
-The replication cohort confirms whether the primary result was a false positive or stable.
-Variation across observations is attributed to the seeds that produced them, as each seed generates one paired observation of proposed and baseline accuracy.
+The analysis computes bootstrap 95% confidence intervals over seeds for each condition's mean accuracy and for the mean paired difference, and reports the primary and confirmatory-replication cohorts separately without pooling them.
+Conclusions are scoped to this architecture, the coefficient 0.01, the calibrated training budget and this split.
```

## results

```diff
--- published/results
+++ corrected/results
@@ -1 +1 @@
-We walk through the evidence from the primary and replication cohorts.
+We report the primary and confirmatory-replication cohorts separately.
@@ -3,28 +3,14 @@
-In the primary cohort, we report each metric's mean with a bootstrap 95% confidence interval (Table 1).
-On held-out classification accuracy, the proposed condition mean was 0.906 (95% CI [0.9022, 0.9106]) and the baseline mean was 0.905 (95% CI [0.9016, 0.9086]).
-The proposed condition improved the contrast in the hypothesised direction by 0.00133 versus the baseline condition (95% CI [-0.00315, 0.0056], paired randomisation p=0.546, Cohen's dz=0.09).
-Figure 2 displays these means with error bars.
-The 95% CI includes zero, indicating no statistically significant difference.
-The preregistered decision was inconclusive.
-Figure 3 plots the paired mean difference over 43 paired seeds for the primary cohort.
-Zero is the value the preregistered direction is tested against.
-The 43 individual paired differences are plotted behind the interval at their exact values.
-The distribution centers near zero, consistent with the mean difference of 0.00133.
-Figure 4 shows mean held-out classification accuracy over training steps for the proposed, baseline and negative control 1 conditions in the primary cohort.
-Each line is the mean over 43 seeds.
-The curves coincide closely, distinguished by marker shape and dash pattern.
-This suggests the consistency loss did not alter training dynamics substantially.
-In the pre-specified confirmatory replication on disjoint seeds, we report results separately (Table 3).
-On held-out classification accuracy, the proposed condition mean was 0.906 (95% CI [0.902, 0.909]) and the baseline mean was 0.908 (95% CI [0.904, 0.911]).
-The proposed condition worsened the contrast in the hypothesised direction by -0.00157 versus the baseline condition (95% CI [-0.00487, 0.00182], paired randomisation p=0.372, Cohen's dz=-0.14).
-Table 4 details this outcome.
-The 95% CI includes zero, and the direction reversed compared to the primary cohort.
-The preregistered decision was inconclusive.
-Figure 5 displays the replication cohort means.
-Figure 6 plots the paired mean difference for the replication cohort, showing the distribution of the 43 individual paired differences behind the interval.
-Figure 7 shows accuracy over training steps for the replication cohort, where curves again coincide.
-Variation across observations is attributed to the seeds that produced them.
-The primary cohort showed a negligible positive shift, while the replication cohort showed a negligible negative shift.
-Neither estimate exceeded the preregistered margin of 0.0125098 proportion.
-The negative control 1 condition achieved 0.908 in the primary cohort and 0.907 in the replication cohort, confirming the harness did not introduce bias.
-The results do not support the hypothesis that cross-layer consistency improves subject-disjoint generalization in this regime.
+In the primary cohort (Table 1), mean held-out classification accuracy was 0.906 (95% CI [0.9022, 0.9106]) for the proposed condition and 0.905 (95% CI [0.9016, 0.9086]) for the baseline.
+The paired contrast in the hypothesised direction was 0.00133, or 0.13 percentage points (95% CI [-0.00315, 0.0056], paired randomisation p=0.546, Cohen's dz=0.09; Table 2).
+Figure 2 displays the condition means with their intervals.
+The interval includes zero and its upper bound lies below the margin of 0.0125098, so the preregistered decision was inconclusive: no improvement of the registered size is supported.
+Figure 3 plots the 43 individual paired differences behind the interval at their exact values; zero is the value the preregistered direction is tested against.
+Figure 4 shows mean held-out classification accuracy over training steps for the proposed, baseline and negative control conditions in the primary cohort; each line is the mean over 43 seeds, and the curves coincide closely, distinguished by marker shape and dash pattern.
+In the confirmatory replication (Table 3), mean accuracy was 0.906 (95% CI [0.902, 0.909]) for the proposed condition and 0.908 (95% CI [0.904, 0.911]) for the baseline.
+The paired contrast was -0.00157, or -0.16 percentage points (95% CI [-0.00487, 0.00182], paired randomisation p=0.372, Cohen's dz=-0.14); Table 4 details it.
+The interval includes zero, the point estimate has the opposite sign to the primary cohort's, and the preregistered decision was again inconclusive.
+Figure 5 shows the replication cohort's condition means with their intervals, which overlap; Figure 6 shows its 43 paired differences, which straddle zero, so the replication supports no improvement either; Figure 7 shows mean held-out accuracy over training steps, where the curves again coincide.
+Table 5 sets the two cohorts' condition means side by side without pooling them, so the reader can compare cohorts without a combined estimate the design does not license.
+The active negative control reached mean accuracies of 0.908 in the primary cohort and 0.907 in the replication cohort, close to both the baseline and the proposed condition.
+The harness recorded it acting on every training step, so it ran as registered; no contrast involving it was registered or tested.
+Neither cohort's estimate approached the margin: both 95% intervals lie entirely below 0.0125098 (1.251 percentage points).
```

## discussion

```diff
--- published/discussion
+++ corrected/discussion
@@ -1,18 +1,17 @@
-The principal finding is that enforcing cross-layer consistency in attention query projections did not improve held-out classification accuracy on the UCI HAR dataset.
-The mean difference was 0.00133 in the primary cohort and -0.00157 in the replication cohort, with confidence intervals including zero in both cases.
-This suggests that transformer depth does not benefit from query weight stability across blocks for this task.
-The result is consistent with literature reporting that approximations needed to make regularization tractable are where guarantees are lost.
-It aligns with findings that spectral entropy minimization of input projections does not yield robust accuracy gains over standard weight decay in this regime [2].
-What this design does establish is that the intervention was implemented correctly, as confirmed by the negative control and harness logs.
-What it does not establish is that cross-layer consistency is useless for all time-series tasks; the UCI HAR setting involves short windows (128 timesteps) where deep hierarchical processing may not be required.
-A mechanism that would produce the observed result is that layer-specific adaptation is essential for this architecture class, allowing deeper blocks to refine attention patterns for complex temporal features rather than copying shallow projections.
-An alternative mechanism is that the regularization strength (0.01 coefficient) was too weak to constrain weights meaningfully, or too strong to allow necessary divergence.
-The pre-specified confirmatory replication on disjoint seeds adds confidence that the primary result was not a false positive, as the effect did not replicate in direction or magnitude.
-Variation across observations is attributed to the seeds that produced them, not subjects, because each observation is one seed.
-This distinction matters for generalization claims; we evaluated on people who appear nowhere in training, supporting a claim about unseen subjects, but not evidence about a different corpus, sensor, task or deployment distribution.
-The finding stands against specific cited papers by extending the null regularization results observed for input projections [2] to attention query projections.
-It agrees with work questioning the validity of Transformer-based solutions for time series analysis tasks where simpler models suffice [4].
-Future work would settle the question by testing deeper architectures where layer hierarchy is more critical, or by varying the consistency coefficient.
-It would also test whether consistency helps in low-data regimes where overfitting is more severe.
-The inconclusive outcome owes the reader every one of those interpretations and is never rewritten as a positive finding.
-The results clarify that for standard 2-block transformers on human activity recognition, cross-layer query consistency is not a sufficient inductive bias for subject-disjoint generalization.
+The principal finding is that the cross-layer consistency loss on attention query weights did not produce a detectable improvement in held-out classification accuracy on UCI HAR.
+The paired contrast was 0.00133 in the primary cohort and -0.00157 in the replication cohort; both intervals include zero, and both lie entirely below the margin of 0.0125098.
+Neither cohort supports a positive improvement of the registered size, both remain inconclusive under the preregistered rule, and the study identifies no mechanism.
+The result sits alongside the earlier inconclusive test of spectral entropy minimization of input projections on the same testbed [2].
+The harness records show the penalty acting at the registered point on every step in the proposed and negative-control conditions and never in the baseline.
+On this testbed, neither cohort shows an accuracy gain as large as the margin.
+The design does not establish that cross-layer consistency is ineffective in general.
+UCI HAR uses short windows of 128 timesteps and the model has two blocks, a setting in which deep hierarchical processing may not be needed.
+Several explanations are compatible with the result, and none was tested.
+Deeper blocks may need layer-specific query weights in this architecture, so pulling them toward the first block may remove useful adaptation.
+The coefficient 0.01 may be too small to change the weights meaningfully, or the penalty may not change accuracy at this scale whatever its size.
+Because only accuracy was measured, not attention patterns, weight distances or gradient contributions, the study cannot separate these explanations.
+The active negative control, which uses an unrelated fixed reference, reached similar accuracy; this is consistent with the specific cross-layer reference not mattering here, but no contrast with it was registered.
+The confirmatory replication used new seeds with the same subjects, split and pipeline, so it shows that the inconclusive outcome repeats across training seeds; it is not a replication on a new population.
+The evaluation covers people who appear nowhere in training, which supports a statement about unseen subjects in this dataset only.
+The result is also compatible with work questioning Transformer-based solutions for time series where simpler models suffice [3].
+A decisive follow-up would measure the targeted property directly, for example the distance between the two blocks' query weights during training, and vary the coefficient.
```

## limitations

```diff
--- published/limitations
+++ corrected/limitations
@@ -2,7 +2,8 @@
-First, we evaluated on a single dataset (UCI HAR) with short sequence lengths.
-Results may differ on longer time series where deep hierarchical processing is more beneficial.
-Second, the architecture was limited to 2 blocks; cross-layer consistency might matter more in deeper networks where divergence between layers is greater.
-Third, we tested only query projection consistency; key, value, or output projections might behave differently.
-Fourth, the regularization coefficient was fixed at 0.01; a hyperparameter search might find a regime where consistency helps.
-Finally, while we used subject-disjoint splits, we did not test cross-domain generalization (e.g., different sensor types).
-These limitations constrain the generalizability of the null result to other time-series benchmarks.
+First, we evaluated a single dataset (UCI HAR) with short sequences; results may differ on longer time series, where deep hierarchical processing may be more beneficial.
+Second, the architecture has two blocks; cross-layer consistency might matter more in deeper networks, where layers may diverge more.
+Third, only query projection consistency was tested; key, value or output projections might behave differently.
+Fourth, the coefficient was fixed at 0.01, and the preregistered statement that this coefficient keeps the penalty from dominating the classification objective was not checked during the run.
+Fifth, held-out accuracy was the only outcome recorded, so every mechanism discussed above is an untested hypothesis.
+Sixth, the confirmatory replication reuses the same subjects and split, so it assesses repeatability over training seeds rather than generalization to a new population.
+Seventh, under the preregistered support rule a true effect equal to the margin would be declared supported only about one time in forty, although the preregistered power analysis assumed 90% power at that effect for rejecting zero; the classification is kept as registered.
+Finally, we did not test cross-domain generalization, such as different sensor types.
```

## conclusion

```diff
--- published/conclusion
+++ corrected/conclusion
@@ -1,5 +1,4 @@
-This study tested whether cross-layer query consistency loss improves subject-disjoint generalization in time-series transformers.
-The results were inconclusive: the proposed condition did not exceed the preregistered worthwhile margin in either the primary or replication cohorts.
-Variation across observations is attributed to the seeds that produced them.
-For someone choosing between these methods, the evidence suggests standard training is sufficient for 2-block transformers on UCI HAR, as consistency loss adds complexity without accuracy gains.
-Future work should test deeper architectures and varying regularization strengths to settle whether layer-specific adaptation is essential or if consistency benefits other regimes.
+This study tested whether a cross-layer consistency loss on attention query weights improves subject-disjoint accuracy in a two-block time-series transformer on UCI HAR.
+Neither cohort supports a positive improvement: the paired contrasts were 0.00133 and -0.00157 (0.13 and -0.16 percentage points), both 95% intervals lie below the threshold of 0.0125098 (1.251 percentage points), and both cohorts remain inconclusive under the preregistered rule.
+Only accuracy was measured, so the study identifies no mechanism.
+Within this architecture, coefficient, training budget and split, the penalty offers no detectable accuracy benefit over standard training; whether it helps in deeper networks, at other strengths or under other distribution shifts remains open.
```

## ai_generated_disclosure

```diff
--- published/ai_generated_disclosure
+++ corrected/ai_generated_disclosure
@@ -2 +2,3 @@
-All content is AI-generated and is explicitly labelled as such.
+After the autonomous run, the text was corrected at the direction of the journal's editor; the correcting text was drafted by an AI assistant (Claude, Anthropic), not written by a human: the correction rewrote the title, the abstract, the Related Work, the Discussion and the Conclusion, revised sentences in the Introduction, Method, Experimental Setup, Results and Limitations, added two paragraphs to the Introduction, three paragraphs to the Method and one paragraph to the Results, and corrected the reference list.
+Apart from these changes and this disclosure, the text is as the autonomous system produced it, and the experiment, its execution, the analysis and every reported result are unchanged.
+CORRECTION.md lists every changed sentence.
```

## references

```diff
- [3] Transformer in Transformer (removed)
- [7] Attention Is All You Need: arxiv_id None
+ [7] Attention Is All You Need: arxiv_id '1706.03762'
- [7] Attention Is All You Need: doi '10.65215/2q58a426'
+ [7] Attention Is All You Need: doi None
- [7] Attention Is All You Need: url 'https://openalex.org/W2626778328'
+ [7] Attention Is All You Need: url 'https://arxiv.org/abs/1706.03762'
- [7] Attention Is All You Need: venue None
+ [7] Attention Is All You Need: venue 'Advances in Neural Information Processing Systems 30 (NeurIPS 2017)'
- [7] Attention Is All You Need: year 2025
+ [7] Attention Is All You Need: year 2017
- [8] Selective Attention Improves Transformer: arxiv_id None
+ [8] Selective Attention Improves Transformer: arxiv_id '2410.02703'
- [12] Spatial-Spectral Transformer for Hyperspectral Image Classification (removed)
- [13] CSWin Transformer: A General Vision Transformer Backbone with Cross-Shaped Windows (removed)
- [14] Swin-Transformer-Enabled YOLOv5 with Attention Mechanism for Small Object Detection on Satellite Images (removed)
- [15] Learning Graph Structures with Transformer for Multivariate Time Series Anomaly Detection in IoT (removed)
- [16] MSA Transformer (removed)
- [17] TransFG: A Transformer Architecture for Fine-Grained Recognition (removed)
- [18] Large Pre-trained time series models for cross-domain Time series analysis tasks: arxiv_id None
+ [18] Large Pre-trained time series models for cross-domain Time series analysis tasks: arxiv_id '2311.11413'
- [19] Shape analysis for time series (removed)
- [20] Fuzzy Clustering Stability Evaluation of Time Series (removed)
- [21] PCT: Point cloud transformer (removed)
- [22] RT-1: Robotics Transformer for Real-World Control at Scale (removed)
- [23] An End-to-End Model for Question Answering over Knowledge Base with Cross-Attention Combining Global Knowledge (removed)
- [24] Occlusion Aware Facial Expression Recognition Using CNN With Attention Mechanism (removed)
- [25] Transformers in Remote Sensing: A Survey (removed)
- [26] Transformer Architecture and Attention Mechanisms in Genome Data Analysis: A Comprehensive Review (removed)
- [28] Attention mechanisms in computer vision: A survey (removed)
- [29] Anomaly Transformer: Time Series Anomaly Detection with Association Discrepancy (removed)
- [30] Neural Speech Synthesis with Transformer Network (removed)
- [31] Cross-Attention Transformer for Coherent Detection in Radar Under Low-SNR Conditions (removed)
- [32] Multivariate Time Series Anomaly Detection with Fourier Time Series Transformer (removed)
- [33] Attention as a Hypernetwork: arxiv_id None
+ [33] Attention as a Hypernetwork: arxiv_id '2406.05816'
- [34] Transformers in medical image analysis (removed)
- [35] Contrastive Time-Series Anomaly Detection (removed)
- [36] Retrieval Augmented Time Series Forecasting (removed)
- [37] TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation (removed)
- [38] An R-Transformer_BiLSTM Model Based on Attention for Multi-label Text Classification (removed)
- [39] Automatic change-point detection in time series via deep learning (removed)
- [40] Semantically Tied Paired Cycle Consistency for Zero-Shot Sketch-Based Image Retrieval (removed)
- [41] TransHSI: A Hybrid CNN-Transformer Method for Disjoint Sample-Based Hyperspectral Image Classification (removed)
```
