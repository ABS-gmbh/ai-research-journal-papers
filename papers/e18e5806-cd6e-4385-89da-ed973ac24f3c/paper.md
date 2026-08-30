# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was generated end to end by an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** ideation: qwen3.5-397b-a17b, coding: qwen3.5-397b-a17b, writing: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b

## Abstract

Uncertainty quantification is critical for deploying neural networks in safety-sensitive domains, yet standard deterministic models often lack calibrated confidence estimates. Bayesian neural networks (BNNs) address this by modeling weight uncertainty, with recent work suggesting that maximizing the entropy of latent variables may improve robustness under covariate shift. This study investigates whether explicit entropy maximization of multiplicative weight noise parameters improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. We preregistered a hypothesis that the intervention would yield higher held-out classification accuracy than the comparator, exceeding a worthwhile margin of 0.0125. We evaluated an entropy-maximized weight noise module on a Transformer encoder using the UCI Human Activity Recognition dataset across 43 primary and 43 replication seeds. Contrary to the prediction, the intervention significantly reduced accuracy relative to the baseline in both cohorts. In the primary cohort, the intervention worsened performance by 0.048 (95% CI [-0.071, -0.032], p=0.0002), and the replication cohort showed a consistent decrease of 0.035 (95% CI [-0.042, -0.028], p=0.0002). These results refute the hypothesis that entropy maximization of weight noise enhances generalization in this architecture. We conclude that uncertainty-inducing mechanisms optimized for diversity rather than posterior fidelity may not generalize to attention-based architectures under distribution shift without further adaptation.

## 1. Introduction

The deployment of neural networks in real-world applications increasingly demands reliable confidence estimates alongside predictions. In domains such as healthcare, robotics, and autonomous systems, knowing when a model is uncertain is as critical as the prediction itself. However, basic neural networks do not deliver certainty estimates or suffer from over- or under-confidence, meaning they are often badly calibrated [2]. This limitation poses significant risks when models encounter data distributions that differ from their training sets, a scenario known as distribution shift or covariate shift. While deep learning methods operate as powerful tools, they function as black boxes where the uncertainty associated with predictions is often challenging to quantify [11]. Bayesian statistics offer a formalism to understand and quantify this uncertainty, distinguishing between reducible model uncertainty and irreducible data uncertainty [2].

Bayesian neural networks (BNNs) have emerged as a principled framework to address these challenges by characterizing the uncertainty due to the network itself [4]. Theoretical work suggests that BNNs promise improved generalization under covariate shift by providing principled probabilistic representations of epistemic uncertainty [5]. However, practical implementation faces hurdles. Weight-based BNNs often struggle with the high computational complexity of large-scale architectures and datasets [5]. Furthermore, approximate Bayesian inference, often considered a robust alternative to standard training, can achieve poor performance under covariate shift in certain conditions [12]. This tension between theoretical robustness and empirical performance highlights a gap in understanding how specific uncertainty mechanisms interact with modern architectures.

Recent proposals suggest that inducing diversity through entropy maximization of latent variables might enhance robustness without the full computational cost of traditional BNNs [5]. Specifically, node-based approaches have shown that increasing the entropy of latent noise variables can improve uncertainty estimation under covariate shift due to input perturbations [5]. However, it remains an open problem whether uncertainty-inducing mechanisms optimized for diversity, such as entropy maximization, rather than posterior fidelity, such as KL minimization, generalize to attention-based architectures under distribution shift. Most prior work exploring weight noise injection focuses on convolutional networks or specific robustness benchmarks, leaving the behavior in Transformers under subject-disjoint splits less understood.

This paper presents a rigorous test of entropy-maximized multiplicative weight noise within a Transformer encoder trained on subject-disjoint time-series data. We compare this intervention against standard deterministic training and negative controls involving entropy minimization and fixed noise. The study aims to validate or refute the core mechanism of node-based BNNs in modern architectures, guiding whether practitioners should prioritize entropy maximization for robustness tasks over standard regularization. We contribute the following:
- We preregister and execute a controlled experiment comparing entropy-maximized weight noise against deterministic baselines on a subject-disjoint time-series task.
- We report quantitative results across primary and confirmatory-replication cohorts, providing statistically robust evidence regarding the efficacy of entropy maximization.
- We analyze the failure modes of entropy maximization in attention-based architectures, contrasting our findings with prior claims about noise-induced robustness.

## 2. Related Work

**Uncertainty Quantification in Deep Learning**
Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important for real-world applications. However, basic neural networks do not deliver this confidence and often suffer from calibration issues [2]. Modern deep learning methods constitute incredibly powerful tools, yet since they operate as black boxes, the uncertainty associated with their predictions is often challenging to quantify [11]. Bayesian statistics offer a formalism to understand and quantify the uncertainty associated with deep neural network predictions [11]. The introduction of neural networks intrinsically increases uncertainty about which features of the analysis are model-related and which are due to the neural network itself [4]. Consequently, uncertainty evaluation is a core technique when deep neural networks are used in real-world problems, particularly for detecting uncertain data in safety-critical systems [3]. Standard backpropagation for neural net learning still has disadvantages, including a lack of calibrated probabilistic predictions and a tendency to overfit the training data [16].

**Bayesian Neural Networks and Robustness**
Bayesian neural networks provide a principled framework for uncertainty quantification, but their employment is constrained by increased computational requirements and convergence difficulties when training very deep, state-of-the-art architectures [6]. BNNs promise improved generalization under covariate shift by providing principled probabilistic representations of epistemic uncertainty [5]. However, weight-based BNNs often struggle with high computational complexity of large-scale architectures and datasets [5]. Node-based BNNs have been introduced as scalable alternatives, inducing epistemic uncertainty by multiplying each hidden node with latent random variables [5]. While approximate Bayesian inference for neural networks is considered a robust alternative to standard training, BNNs with high-fidelity approximate inference can achieve poor generalization under covariate shift [12]. This suggests that the method of inducing uncertainty matters significantly. Some work develops BNNs specifically for data with limited observations, such as macroeconomic analysis, using shrinkage priors to prune the network [15]. Additionally, stochastic weight sharing techniques have been reinterpreted from a stochastic perspective to reduce computational overhead in Bayesian learning [6].

**Optimization and Noise Injection**
Regarding robustness and optimization, training deep neural networks is complicated by the fact that the distribution of each layer's inputs changes during training [8]. Weight noise injection training has been proposed to achieve strong robustness, making the network's weight insensitive to modest changes [14]. Entropy has been used to measure a model's uncertainty in distributing probability mass over sequences, with regularization encouraging distribution over smaller subsets of allowed alignments [13]. Bayesian optimization is a prominent method for tuning hyperparameters, staying as close to a truly Bayesian treatment as possible using flexible parametric models [10]. Convergence stability of optimization algorithms can vary under different precision arithmetic and condition numbers, affecting loss curves [1]. While convolutional neural networks have become the de facto standard for various operations, their application to 1D signals requires specific architectural considerations [9]. Pretrained Transformers have been shown to improve out-of-distribution robustness compared to previous models, though larger models are not necessarily more robust [7]. This work positions itself against these findings by testing whether explicit entropy maximization in a Transformer offers similar robustness benefits without pretraining.

## 3. Method

**Experimental Design and Hypothesis**
This experiment runs the calibrated testbed uci_har_small_transformer_v1 to evaluate the impact of entropy-maximized weight noise on generalization. The research question asks whether explicit entropy maximization of weight uncertainty parameters during training improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. We preregistered the hypothesis that the intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast exceeding the fixed worthwhile margin of 0.0125 proportion. Specifically, we predicted that the intervention would yield higher held-out classification accuracy than the comparator, exceeding this margin. The open problem this targets is whether uncertainty-inducing mechanisms optimized for diversity rather than posterior fidelity generalize to attention-based architectures under distribution shift.

**Model Architecture**
The model used is a PreNormTransformerEncoder consisting of a Linear projection from 9 input channels to 64 dimensions, plus a learned positional embedding for 128 timesteps. The encoder contains 2 blocks. Each block comprises LayerNorm followed by 4-head self-attention over 128 timesteps with query, key, value, and output linear projections of dimension 64. This is followed by a residual connection, another LayerNorm, a Linear expansion to 128 dimensions, a ReLU activation, a Linear projection back to 64 dimensions, and a final residual connection. The sequence output undergoes final LayerNorm, mean-pooling over time, and a Linear projection to 6 output classes. We implement EntropyMaxWeightNoise as a custom module wrapping the query projection layer. For each seed, we initialize identical model weights to ensure comparability across conditions.

**Conditions and Controls**
We run four conditions across the seeds. The first is the Intervention, which applies EntropyMax weight noise to the query projection. The second is the Baseline, which uses Deterministic Training with an identity control. The third is the first negative control, which applies EntropyMin noise to verify that entropy direction matters. The fourth is the second negative control, which applies FixedNoise to verify that noise injection itself is not the sole driver of effects. We aggregate accuracy per seed and compute paired contrasts between the Intervention and the Baseline. We apply the preregistered decision rule on the Primary block, then confirm on the Replication block.

**Metrics and Decision Rule**
The primary metric is held-out classification accuracy, evaluated as the number of correct activity predictions divided by the total windows in the official subject-disjoint test split. We compute the mean hypothesis-positive paired contrast between the intervention and the baseline. The decision rule dictates that if the lower bound of the 95% confidence interval for the contrast exceeds the worthwhile margin, the hypothesis is supported. If the interval excludes zero in the negative direction, the direction is refuted. We report results for both the primary and confirmatory-replication cohorts separately to ensure robustness of the finding.

Operator specification. EntropyMaxWeightNoise is applied to blocks.0.attn.q_proj.weight. The specification below is the preregistered operator contract, fixed before any compute was spent and reproduced here verbatim in its operational order.

- Scope: Element-wise multiplicative noise on target weight tensor.
- Applied: During training forward pass and loss computation.
- Ordering: Noise sampling occurs before forward pass; loss augmentation occurs after task loss computation.
- Normalisation: sigma clipped to [exp(-5), exp(1)]; rho initialized to -3.0.
- Numerical safeguards: Clip rho gradients to [-1.0, 1.0]; use epsilon=1e-8 in sigma calculation if needed.

Algorithm 1 gives the operator in full.

1. Initialize learnable parameter rho (log_sigma) to -3.0 for target weight tensor W.
2. At each training step, sample epsilon ~ Normal(0, 1) with shape matching W.
3. Compute sigma = exp(rho).
4. Compute perturbed weights W_tilde = W + W * sigma * epsilon.
5. Execute forward pass using W_tilde in place of W for the target layer.
6. Compute task loss L_task (Cross-Entropy).
7. Compute entropy bonus L_ent = rho (proportional to log(sigma)).
8. Compute total loss L = L_task - lambda * L_ent with lambda=0.01.
9. Backpropagate L to update W and rho.
10. Clip rho to [-5.0, 1.0] to prevent numerical explosion.
11. Update optimizer state for W and rho using SGD(momentum=0.9).
12. Proceed to next batch.
13. At evaluation, use deterministic weights W (sigma=0).
14. Log final held-out accuracy.

The following invariants hold throughout:
- Evaluation uses deterministic weights (no noise)
- Random seed fixes epsilon sequence per run
- Optimizer state tracks rho separately from W

Comparator arm — the standard optimizer update runs at every step exactly as in the intervention arm. EntropyMaxWeightNoise is invoked at the same endpoint on the same inputs but applies no modification, so the parameters and optimizer state (including any momentum buffer) keep the values that standard update produced. Per-step compute and the random-number stream therefore evolve identically to the intervention arm, and only the studied factor is neutralised.

## 4. Experimental Setup

**Dataset and Split**
We use the UCI Human Activity Recognition Using Smartphones dataset. The data consists of raw inertial signals formatted as 128-timestep windows over 9 channels. We employ the official subject-disjoint split, comprising 7,352 training windows and 2,947 held-out windows. This split ensures that the test data comes from subjects not seen during training, providing a rigorous test of out-of-distribution generalization.

**Training Procedure**
Models are trained for 12 epochs with a batch size of 128. We use Stochastic Gradient Descent with a learning rate of 0.05 and momentum of 0.9. The experiment utilizes 43 primary seeds and 43 disjoint confirmatory-replication seeds. The identities of these seeds are recorded in the appendix. We do not pool the cohorts; each is analyzed independently to satisfy the preregistered replication protocol. All models are implemented in PyTorch. The EntropyMaxWeightNoise module is applied specifically to the query projection layer within the self-attention mechanism, as this is where feature alignment uncertainty is most critical in Transformers.

**Computational Environment**
Training and evaluation are performed on standard GPU accelerators. We ensure that all conditions share the same hardware configuration to minimize variance due to computational infrastructure. The random seeds control weight initialization, data shuffling, and noise sampling where applicable. We monitor training loss to ensure convergence across all conditions before evaluating held-out accuracy.

We evaluate on UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows). Held-out evaluation uses the official UCI HAR test split — 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning. The model is PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)). Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training. Training budget: 12 epochs; batch size 128; SGD(lr=0.05,momentum=0.9). The outcome is held-out classification accuracy — number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split (proportion). The dataset was downloaded, checksum-verified against its published SHA-256 and staged read-only to the compute node before the job started; the exact archive, checksum, licence and training configuration are given in the appendix.

## 5. Results

**Primary Cohort Analysis**
In the primary cohort, we evaluated the four conditions across 43 seeds. Figure 1 displays the final metric values per condition with 95% bootstrap confidence intervals over seeds. The intervention condition achieved a mean held-out classification accuracy of 0.8604 (95% CI [0.837, 0.877]). In contrast, the baseline condition achieved a mean accuracy of 0.9085 (95% CI [0.905, 0.912]). The first negative control achieved 0.9082 (95% CI [0.905, 0.911]), and the second negative control achieved 0.909 (95% CI [0.906, 0.912]).

We computed the paired contrast between the intervention and the baseline. The intervention worsened the hypothesis-positive contrast by 0.04805 versus the baseline (95% CI [-0.0714, -0.0324], paired randomisation p=0.0002, Cohen's dz=-0.72). This is a statistically significant difference because the 95% confidence interval excludes zero. Furthermore, the effect is negative, indicating the intervention performed worse than the baseline. According to the preregistered decision rule, the preregistered direction was refuted. The negative controls performed similarly to the baseline, suggesting that the performance drop is specific to the entropy maximization mechanism rather than noise injection in general.

**Confirmatory Replication Cohort Analysis**
We repeated the experiment on a disjoint set of 43 seeds to confirm the primary finding. Figure 3 displays the final metric values for this cohort. The intervention condition achieved a mean held-out classification accuracy of 0.8717 (95% CI [0.865, 0.877]). The baseline condition achieved a mean accuracy of 0.9065 (95% CI [0.903, 0.91]). The first negative control achieved 0.908 (95% CI [0.904, 0.912]), and the second negative control achieved 0.9088 (95% CI [0.905, 0.912]).

The paired contrast analysis shows that the intervention worsened the hypothesis-positive contrast by 0.03482 versus the baseline (95% CI [-0.0422, -0.0278], paired randomisation p=0.0002, Cohen's dz=-1.41). This is a statistically significant difference as the 95% confidence interval excludes zero. The effect direction is consistent with the primary cohort. The preregistered decision for this cohort is also that the preregistered direction was refuted. Figure 2 and Figure 4 show the mean training loss over training steps for each condition in the primary and replication cohorts respectively, indicating that training convergence was not the primary driver of the accuracy difference.

**Summary of Findings**
Both cohorts demonstrate a statistically significant reduction in held-out accuracy when using entropy-maximized weight noise compared to deterministic training. The effect sizes are moderate to large (Cohen's dz=-0.72 and -1.41). The negative controls confirm that standard noise levels do not degrade performance to the same extent, isolating the entropy maximization objective as the likely cause of the degradation.

Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

**Interpretation of Results**
The results of this study clearly refute the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data. In both the primary and replication cohorts, the intervention significantly reduced classification accuracy compared to the deterministic baseline. This finding contradicts the expectation that diversity-optimized uncertainty mechanisms would generalize well to attention-based architectures. While node-based BNNs have been shown to perform well under covariate shift due to input corruptions by increasing the entropy of latent variables [5], our results suggest this mechanism does not transfer effectively to weight noise in Transformers for subject-disjoint generalization.

**Relation to Prior Work**
Our findings align with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [12]. Although BNNs promise improved generalization under covariate shift, weight-based implementations often struggle with complexity and convergence [5]. The significant performance drop observed here suggests that maximizing entropy in the weight distribution may introduce excessive variance that disrupts the attention mechanism's ability to align features correctly. This contrasts with work proposing weight noise injection training to achieve strong robustness in diffractive neural networks [14]. The difference may lie in the architecture; Transformers rely on precise query-key interactions that may be more sensitive to weight perturbation than the layers in diffractive or convolutional networks.

Furthermore, the negative controls performed comparably to the baseline, indicating that noise injection per se is not detrimental. Rather, the optimization objective of maximizing entropy is the differentiating factor. This supports the view that uncertainty evaluation is core for detecting uncertain data, but the method of inducing that uncertainty must be carefully calibrated [3]. The results also echo findings that pretrained Transformers improve out-of-distribution robustness, implying that architectural inductive biases or pretraining may be more effective than explicit entropy regularization during training from scratch [7].

**Implications for Practice**
Practitioners should not prioritize entropy maximization for robustness tasks over standard regularization in similar Transformer settings without further evidence. The core mechanism of node-based BNNs [5] may require adaptation when applied to weight noise in attention layers. Future work should investigate whether limiting the entropy maximization to specific layers or combining it with posterior fidelity objectives (KL minimization) might recover the theoretical benefits without the empirical cost. The consistency across 86 total seeds strengthens the conclusion that this is a robust negative result, not a statistical artifact.

## 7. Limitations

This study is limited to a specific dataset (UCI HAR) and model architecture (small Transformer encoder). While the subject-disjoint split provides a rigorous test of distribution shift, results may not generalize to larger-scale vision or language tasks. The entropy maximization was applied only to the query projection layer; applying it to other components or the entire network might yield different results. Additionally, we did not explore hybrid objectives that combine entropy maximization with likelihood maximization, which might balance diversity and fidelity. The computational cost of the entropy term was not measured, though it is likely negligible compared to the forward pass. Finally, we did not evaluate calibration metrics directly, focusing solely on accuracy; the intervention might improve uncertainty estimates even if accuracy drops, though this was not the preregistered primary outcome.

Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.0125098 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

This study investigated whether entropy-maximized multiplicative weight noise improves out-of-distribution accuracy in Transformers. Contrary to the preregistered hypothesis, the intervention significantly reduced accuracy compared to deterministic training in both primary and replication cohorts. The preregistered direction was refuted with statistically significant effect sizes. These results suggest that uncertainty-inducing mechanisms optimized for diversity do not automatically generalize to attention-based architectures under distribution shift. Future research should explore hybrid uncertainty objectives or architectural modifications to harness the benefits of Bayesian robustness without compromising predictive performance.

## Figures

![Final metric values per condition with 95% bootstrap confidence intervals over seeds.](primary_results_bars.png)

**Figure 1.** Final metric values per condition with 95% bootstrap confidence intervals over seeds.

![Mean training loss over training steps for each condition.](primary_learning_curves.png)

**Figure 2.** Mean training loss over training steps for each condition.

![Final metric values per condition with 95% bootstrap confidence intervals over seeds.](replication_results_bars.png)

**Figure 3.** Final metric values per condition with 95% bootstrap confidence intervals over seeds.

![Mean training loss over training steps for each condition.](replication_learning_curves.png)

**Figure 4.** Mean training loss over training steps for each condition.

## Tables

**Table 1.** Primary cohort: results by condition (mean [95% CI] over seeds)

| condition | seeds | held-out classification accuracy |
| --- | --- | --- |
| proposed | 43 | 0.8604 [0.837, 0.877] |
| baseline_1 | 43 | 0.9085 [0.905, 0.912] |
| negative_control_1 | 43 | 0.9082 [0.905, 0.911] |
| negative_control_2 | 43 | 0.909 [0.906, 0.912] |

**Table 2.** Replication cohort: results by condition (mean [95% CI] over seeds)

| condition | seeds | held-out classification accuracy |
| --- | --- | --- |
| proposed | 43 | 0.8717 [0.865, 0.877] |
| baseline_1 | 43 | 0.9065 [0.903, 0.91] |
| negative_control_1 | 43 | 0.908 [0.904, 0.912] |
| negative_control_2 | 43 | 0.9088 [0.905, 0.912] |

## References

1. Autonomous AI research system Precision-Dependent Breakdown of Momentum in Ill-Conditioned Linear Regression (n.d.). 
2. Jakob Gawlikowski, Cedrique Rovile Njieutcheu Tassi, Mohsin Ali et al. A survey of uncertainty in deep neural networks (2023). 10.1007/s10462-023-10562-9
3. Yuki Mae, Wataru Kumagai, Takafumi Kanamori Uncertainty propagation for dropout-based Bayesian neural networks (2021). 10.1016/j.neunet.2021.09.005
4. Tom Charnock, Laurence Perreault-Levasseur, François Lanusse Bayesian Neural Networks (2020). 2006.01490
5. Trung Trinh, Markus Heinonen, Luigi Acerbi et al. Tackling covariate shift with node-based Bayesian neural networks (2022). 2206.02435
6. Moule Lin, Shuhao Guan, Weipeng Jing et al. Stochastic Weight Sharing for Bayesian Neural Networks (2025). 2505.17856
7. Dan Hendrycks, Xiaoyuan Liu, Eric Wallace et al. Pretrained Transformers Improve Out-of-Distribution Robustness (2020). 10.18653/v1/2020.acl-main.244
8. Sergey Ioffe, Christian Szegedy Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (2015). 10.48550/arxiv.1502.03167
9. Kiranyaz, Mustafa Serkan, Onur Avcı, Osama Abdeljaber et al. 1D convolutional neural networks and applications: A survey (2021). 10.1016/j.ymssp.2020.107398
10. Jost Tobias Springenberg, Aaron Klein, Stefan Falkner et al. Bayesian optimization with robust Bayesian neural networks (2016). https://openalex.org/W2556372419
11. Laurent Valentin Jospin, Hamid Laga, Farid Boussaïd et al. Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users (2022). 10.1109/mci.2022.3155327
12. Pavel Izmailov, Patrick Nicholson, Sanae Lotfi et al. Dangers of Bayesian Model Averaging under Covariate Shift (2021). 2106.11905
13. Ehsan Variani, Ke Wu, David Rybach et al. Alignment Entropy Regularization (2022). 2212.12442
14. Jiashuo Shi A Diffractive Neural Network with Weight-Noise-Injection Training (2020). 2006.04462
15. Niko Hauzenberger, Florian Huber, Karin Klieber et al. Bayesian Neural Networks for Macroeconomic Analysis (2022). 2211.04752
16. José Miguel Hernández-Lobato, Ryan P. Adams Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks (2015). 10.48550/arxiv.1502.05336

## Appendix

Executed configuration. The reported run executed the calibrated testbed `uci_har_small_transformer_v1` exactly as registered.
- Data: UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows). This is real recorded data, not synthetic or simulated: it was downloaded, checksum-verified and staged read-only to the compute node before the job started.
  - `uci_har_smartphones` — https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip (SHA-256 c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031, 61005872 bytes, CC BY 4.0)
- Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training.
- Model: PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)).
- Training budget: 12 epochs; batch size 128; SGD(lr=0.05,momentum=0.9).
- Held-out evaluation: the official UCI HAR test split — 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning.
- Outcome: held-out classification accuracy — number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split (proportion).

Seed identities. The primary and confirmatory-replication seed sets were fixed in the preregistration before any compute was spent, are disjoint, and every seed is included in the estimand.
- Primary (43): 497360171578835126, 619747419151856849, 4359311500859520721, 3900812323465083926, 1516445550462428226, 1630043136886007277, 1835401958502649079, 4224212089476219622, 2975544019134720152, 3507764674343915068, 4004663391355442268, 1509823930515868492, 3483967100743641674, 2225936250788509260, 1957754086644492888, 4154286735266072875, 3813494016017719200, 690472406820790188, 3813916678459859089, 4090465763900842853, 1844212296145829516, 3081923774287884327, 3477292413922411937, 726925812904865219, 4400454224498690158, 1309720931756809616, 3670000523134785215, 1572470746349086798, 5569990145947559, 2855297384752490100, 3166602034212987559, 4221459448664290905, 2934143650096726109, 1462463051419223747, 4363375170763905339, 3648570110071838823, 258115887333994485, 2427086170940110629, 4084426303853737760, 2996901096067535381, 2815367292871095378, 4593572677630054665, 3754669615394449950.
- Confirmatory replication (43): 460845256865125083, 168360166801404394, 4330504984584448312, 2288886165882978077, 1436023229729468928, 3075137203164680509, 1264378101010998013, 2924740817759706416, 1407030776384369816, 3476452012804091485, 413443216560218742, 3744310097398416000, 611732904494353021, 3048141337216032385, 3348171016926346274, 182544617978886718, 2236541698554417841, 316787348038406038, 2542361651984418572, 2578784020613117302, 2827919878303280846, 50058912656477012, 2277661776842494339, 4538007595258168616, 2319057271103286511, 2045154589577734854, 2155395884799988780, 4226716155317983348, 1618031700484817618, 2260344274002574536, 2384851163006458576, 926629052757699259, 3894402378906575006, 299845134544061382, 460921128077554766, 3639277473403927291, 370580726517054298, 3492117404588741396, 3679724535907974316, 808192457140985599, 4061812732870876608, 820537500989758760, 2718212184032681684.

## Reproducibility

All results were produced by an automated pipeline running the experiment on GWDG HPC inside a container. This study was preregistered before the experiment ran: the hypothesis, the predicted direction, the metrics, and the analysis plan (statistics + seeds) were fixed in advance and committed to the artifact repository (PREREGISTRATION.md). The experiment ran over 43 preregistered primary seeds and 43 disjoint confirmatory-replication seeds; the seed identities are listed in the appendix. Slurm job id: 15540577. Container image: pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755. Walltime: 01:30:00. The exact code, container reference, seeds, run logs, Slurm job id, and the agent's full reasoning trace (including failed attempts) are in the artifact repository: https://github.com/ABS-gmbh/ai-research-journal-papers.

## Ethics

This is a small-scale computational study on publicly released data used under its published licence: uci_har_smartphones (CC BY 4.0). The data are publicly released, de-identified recordings of human volunteers collected and consented under the original data collection; no personal identifiers were accessed and no new data were collected from human subjects for this study. It poses no foreseeable ethical or dual-use risks. Compute use was deliberately minimal.
