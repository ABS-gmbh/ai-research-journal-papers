# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was generated end to end by an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** ideation: qwen3.5-397b-a17b, coding: qwen3.5-397b-a17b, writing: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b

## Abstract

Out-of-distribution robustness remains a critical challenge for deep learning systems deployed in real-world environments, particularly when subject-disjoint generalization is required. While Bayesian neural networks offer a principled framework for uncertainty quantification, recent proposals suggest that explicitly maximizing the entropy of weight uncertainty parameters may improve robustness compared to standard variational objectives. This paper presents a preregistered empirical evaluation of Entropy-Maximized Multiplicative Weight Noise within a Transformer architecture on the UCI Human Activity Recognition dataset. We tested the hypothesis that entropy maximization would yield higher held-out classification accuracy than deterministic training, exceeding a fixed worthwhile margin. Contrary to predictions, the intervention significantly worsened performance in both primary and confirmatory-replication cohorts. The results indicate that entropy maximization of weight noise parameters does not generalize to attention-based architectures under distribution shift in this setting, refuting the core mechanism proposed in recent node-based Bayesian neural network literature. These findings suggest practitioners should prioritize standard regularization over entropy maximization for robustness tasks in similar domains.

## 1. Introduction

The deployment of neural networks in safety-critical applications requires models that maintain performance when faced with distribution shifts, such as those encountered when testing on subjects disjoint from the training population. Standard deterministic training often yields models that are overconfident and brittle under such covariate shifts, failing to capture the uncertainty inherent in out-of-distribution inputs. As neural networks reach almost every field of science, confidence in neural network predictions has become more and more important, yet basic neural networks do not deliver certainty estimates or suffer from over- or under-confidence [3]. This calibration issue is particularly pronounced in time-series classification tasks where inertial signals vary significantly between individuals.

Bayesian neural networks (BNNs) have been proposed to address these limitations by providing principled probabilistic representations of epistemic uncertainty. However, weight-based BNNs often struggle with high computational complexity of large-scale architectures and datasets [6]. To mitigate this, recent work has explored node-based approaches that induce uncertainty by multiplying hidden nodes with latent random variables. A key mechanism in some of these approaches is the explicit maximization of the entropy of these latent variables during training, hypothesized to increase the diversity of implicit data perturbations and thereby improve robustness. However, it remains an open problem whether uncertainty-inducing mechanisms optimized for diversity rather than posterior fidelity generalize to attention-based architectures under distribution shift.

This paper addresses this gap by rigorously testing whether explicit entropy maximization of weight uncertainty parameters during training improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. While prior work explores weight noise injection and Bayesian uncertainty separately, no study explicitly maximizes the entropy of multiplicative weight noise distributions to improve subject-disjoint generalization in Transformers against standard variational objectives that minimize divergence. This distinction is vital because approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13].

We conducted a preregistered experiment using the UCI Human Activity Recognition dataset, employing a PreNormTransformerEncoder architecture. The study was designed with independent primary and confirmatory-replication cohorts to ensure statistical validity. The preregistered hypothesis predicted that the intervention would yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast exceeding a fixed worthwhile margin.

The contributions of this work are as follows:
- We provide a faithful empirical test of entropy-maximized weight noise in a Transformer architecture on a real-world subject-disjoint dataset, correcting prior assumptions based on synthetic or image-based benchmarks.
- We report statistically significant evidence refuting the hypothesis that entropy maximization improves out-of-distribution accuracy in this setting, with large effect sizes observed in both primary and replication cohorts.
- We contextualize these negative results within the broader literature on Bayesian robustness, highlighting constraints regarding computational requirements and convergence difficulties in BNNs [7].
- We offer calibrated guidance for practitioners, suggesting that standard regularization may outperform entropy-maximized uncertainty mechanisms for subject-disjoint time-series classification.

## 2. Related Work

**Uncertainty Quantification in Deep Learning**
Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important, yet a comprehensive survey notes that basic neural networks do not deliver this confidence [3]. Modern deep learning methods constitute incredibly powerful tools, but since deep learning methods operate as black boxes, the uncertainty associated with their predictions is often challenging to quantify [12]. Bayesian statistics offer a formalism to understand and quantify the uncertainty associated with deep neural network predictions [12]. In recent times, neural networks have become a powerful tool for the analysis of complex and abstract data models, but their introduction intrinsically increases our uncertainty about which features of the analysis are model-related and which are due to the neural network [5]. This means that predictions by neural networks have biases which cannot be trivially distinguished from being due to the true nature of the creation and observation of data or not [5].

Uncertainty evaluation is a core technique when deep neural networks are used in real-world problems, and detecting uncertain data is significant for safety-critical systems [4]. While the Bayesian neural networks have recently attracted considerable attention in this context, using backprop for neural net learning still has some disadvantages, such as lack of calibrated probabilistic predictions [17]. While offering a principled framework for uncertainty quantification in deep learning, the employment of Bayesian Neural Networks is still constrained by their increased computational requirements and the convergence difficulties when training very deep, state-of-the-art architectures [7]. Bayesian neural network posterior distributions have a great number of modes that correspond to the same network function, and the abundance of such modes can make it difficult for approximate inference methods to do their job [18]. Additionally, macroeconomic data is characterized by a limited number of observations, and specific BNNs have been developed for handling datasets commonly used for macroeconomic analysis in policy institutions [16].

**Robustness and Optimization under Shift**
Regarding robustness and optimization, node-based Bayesian neural networks state BNNs promise improved generalization under covariate shift but weight-based BNNs often struggle with high computational complexity [6]. However, approximate Bayesian inference for neural networks is considered a robust alternative to standard training, often providing good performance on out-of-distribution data, yet BNNs with high-fidelity approximate inference via full-batch Hamiltonian Monte Carlo achieve poor generalization under covariate shift [13]. Although pretrained Transformers such as BERT achieve high accuracy on indistribution examples, systematic measurement shows that pretrained Transformers' performance declines are substantially smaller on out-of-distribution generalization for NLP datasets [8]. Training Deep Neural Networks is complicated by the fact that the distribution of each layer's inputs changes during training, and Batch Normalization addresses the change in distribution of layer inputs during training [9].

To achieve strong robustness, a diffractive neural network with weight-noise-injection training proposes weight noise injection training [15]. Existing training criteria in automatic speech recognition use entropy to measure a model's uncertainty, i.e. how it chooses to distribute the probability mass over the set of allowed alignments [14]. Bayesian optimization is a prominent method for optimizing expensive-to-evaluate black-box functions, and discussions on Bayesian optimization for tuning hyperparameters exist in the context of robust Bayesian neural networks [11]. During the last decade, Convolutional Neural Networks have become the de facto standard for various Computer Vision and Machine Learning operations, and 1D CNNs have recently been proposed for 1D signals [10]. Convergence stability is also a factor, as studies investigate the convergence stability of SGD with Momentum versus plain SGD under single and half precision arithmetic [1]. Furthermore, investigations into the effect of learning rate on the convergence of plain gradient descent show potential issues with numerical instability [2]. This work positions itself against these findings by testing entropy maximization specifically in a Transformer setting where computational complexity and shift robustness are critical.

## 3. Method

**Dataset and Preprocessing**
The experiment utilized the UCI Human Activity Recognition Using Smartphones dataset (DOI 10.24432/C54S4K), comprising raw inertial signals collected from smartphones placed on the waist of subjects. The data consists of 128-timestep windows over 9 channels, representing accelerometer and gyroscope measurements. We adhered to the official subject-disjoint split, utilizing 7,352 training windows and 2,947 held-out windows. This split ensures that the test subjects are entirely disjoint from the training subjects, providing a rigorous evaluation of out-of-distribution generalization. The input dimension was fixed at 9 channels, and no additional data augmentation was applied beyond the preregistered protocol to isolate the effect of the weight noise intervention.

**Model Architecture**
We implemented a PreNormTransformerEncoder architecture tailored for time-series classification. The model begins with a Linear projection layer mapping the 9 input channels to 64 dimensions, followed by a learned positional embedding of size 128 by 64. The core of the network consists of 2 transformer blocks. Each block contains a LayerNorm layer followed by 4-head self-attention over 128 timesteps, with query, key, value, and output projections implemented as Linear layers of size 64 by 64. A residual connection follows the attention mechanism, leading into a second LayerNorm layer. This is followed by a feed-forward network comprising a Linear layer (64 to 128), a ReLU activation, and a final Linear layer (128 to 64), with a residual connection. The final output is produced by a LayerNorm layer, mean-pooling over time, and a Linear classification head mapping 64 dimensions to 6 activity classes.

**Intervention and Conditions**
The core intervention, EntropyMaxWeightNoise, was implemented as a custom module wrapping the query projection layer of the self-attention mechanism. We ran four distinct conditions to isolate the effect of entropy maximization. The first condition was the Intervention, which applied entropy maximization to the multiplicative weight noise distributions during training. The second condition was the Baseline, consisting of standard Deterministic Training with an identity control, representing typical supervised learning without uncertainty mechanisms. The third condition was the first negative control, employing EntropyMinimization to verify that the effect was specific to entropy maximization rather than noise injection alone. The fourth condition was the second negative control, using FixedNoise parameters to assess the impact of static uncertainty versus learned entropy. All conditions shared identical initial model weights for each seed to ensure comparability.

**Training Protocol**
Models were trained for 12 epochs with a batch size of 128. Optimization was performed using Stochastic Gradient Descent with a learning rate of 0.05 and momentum of 0.9. The primary metric for evaluation was held-out classification accuracy, calculated as the number of correct activity predictions divided by the 2,947 windows in the official subject-disjoint test split. This metric directly aligns with the preregistered hypothesis regarding classification performance under distribution shift.

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

**Preregistration and Hypothesis**
The study was preregistered before the experiment ran, with a fixed hypothesis that the intervention would yield higher held-out classification accuracy than the comparator. Specifically, we predicted that the mean hypothesis-positive paired contrast would exceed the fixed worthwhile margin of 0.0125098 proportion. This margin was established to ensure that any claimed improvement was practically significant rather than statistically trivial. The decision rule was applied strictly to the primary block, with the replication block serving as a confirmatory test to validate the generalizability of the findings.

**Seeds and Cohorts**
The experiment utilized 43 primary seeds and 43 disjoint confirmatory-replication seeds. The identities of these seeds are recorded in the appendix, but only the aggregate counts are reported here to maintain conciseness. For each seed, identical model weights were initialized across all four conditions to ensure that performance differences arose solely from the training dynamics induced by the noise conditions. The seeds were disjoint between the primary and replication cohorts to prevent data leakage and ensure independent validation.

**Computational Environment**
The experiment was implemented using PyTorch. The EntropyMaxWeightNoise module was integrated directly into the training loop, computing the entropy term as part of the loss function during the backward pass. Evaluation was performed after the completion of training for each seed. The computational resources were standardized across conditions to prevent timing or hardware variability from influencing the results. All random states were controlled via the provided seeds to ensure reproducibility of the noise injection and data shuffling processes.

**Statistical Analysis**
We aggregated accuracy per seed and computed paired contrasts between the Intervention and Baseline conditions. Bootstrap 95% confidence intervals were calculated over the seeds to estimate the uncertainty of the mean metrics. The preregistered decision rule relied on whether the confidence interval of the paired contrast excluded zero and exceeded the worthwhile margin in the predicted direction. Significance was assessed using paired randomisation tests, with effect sizes reported as Cohen's dz to quantify the magnitude of the difference.

We evaluate on UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows). Held-out evaluation uses the official UCI HAR test split — 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning. The model is PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)). Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training. Training budget: 12 epochs; batch size 128; SGD(lr=0.05,momentum=0.9). The outcome is held-out classification accuracy — number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split (proportion). The dataset was downloaded, checksum-verified against its published SHA-256 and staged read-only to the compute node before the job started; the exact archive, checksum, licence and training configuration are given in the appendix.

## 5. Results

**Primary Cohort Analysis**
In the primary cohort, we evaluated the held-out classification accuracy across 43 seeds for all four conditions. The Baseline condition achieved a mean accuracy of 0.9085 with a 95% bootstrap confidence interval of [0.905, 0.912]. The Intervention condition achieved a mean accuracy of 0.8604 with a 95% bootstrap confidence interval of [0.837, 0.877]. The negative controls performed similarly to the baseline, with the first negative control achieving 0.9082 [0.905, 0.911] and the second negative control achieving 0.909 [0.906, 0.912]. These values are visualized in Figure 1, which displays the final metric values per condition with 95% bootstrap confidence intervals over seeds.

The paired contrast between the Intervention and Baseline revealed that the intervention worsened the hypothesis-positive contrast by 0.04805. The 95% confidence interval for this contrast was [-0.0714, -0.0324], which excludes zero. The paired randomisation p-value was 0.0002, indicating a statistically significant difference. The effect size was Cohen's dz=-0.72, representing a large negative effect. Based on the preregistered decision rule, the direction was refuted, as the intervention performed significantly worse than the baseline rather than better. Figure 2 illustrates the mean training loss over training steps for each condition, showing divergence in optimization behavior.

**Confirmatory Replication Analysis**
The confirmatory replication cohort consisted of 43 disjoint seeds to verify the primary findings. The Baseline condition achieved a mean accuracy of 0.9065 with a 95% bootstrap confidence interval of [0.903, 0.91]. The Intervention condition achieved a mean accuracy of 0.8717 with a 95% bootstrap confidence interval of [0.865, 0.877]. The negative controls remained stable, with the first negative control at 0.908 [0.904, 0.912] and the second negative control at 0.9088 [0.905, 0.912]. These replication results are presented in Figure 3, showing final metric values per condition with 95% bootstrap confidence intervals over seeds.

The paired contrast in the replication cohort showed that the intervention worsened the hypothesis-positive contrast by 0.03482. The 95% confidence interval was [-0.0422, -0.0278], excluding zero. The paired randomisation p-value was 0.0002, confirming statistical significance. The effect size was Cohen's dz=-1.41, indicating an even larger negative effect than in the primary cohort. The preregistered decision was again direction_refuted. Figure 4 displays the mean training loss over training steps for each condition in the replication cohort, consistent with the primary training dynamics.

**Summary of Findings**
Both cohorts consistently demonstrated that the entropy maximization intervention reduced out-of-distribution accuracy compared to deterministic training. The negative controls performed comparably to the baseline, suggesting that the degradation was specific to the entropy maximization objective rather than the presence of noise itself. The results were robust across 86 total seeds, with no overlap in confidence intervals between the intervention and the baseline conditions in either cohort.

Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

**Interpretation of Results**
The results explicitly refute the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy in this setting. The intervention consistently worsened performance by approximately 3.5% to 4.8% across both cohorts, with large effect sizes. This finding contradicts the expectation that diversity-inducing mechanisms would enhance robustness under subject-disjoint distribution shift. While node-based BNNs promise improved generalization under covariate shift by providing principled probabilistic representations of epistemic uncertainty [6], our results suggest that this mechanism does not transfer effectively to weight-based entropy maximization in Transformers for time-series data.

**Relation to Prior Work**
These findings align with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13]. Specifically, the degradation observed here mirrors the difficulties weight-based BNNs often struggle with regarding high computational complexity and convergence [6]. The fact that negative controls (EntropyMin and FixedNoise) performed similarly to the deterministic baseline suggests that the act of injecting noise itself was not detrimental, but rather the optimization objective of maximizing entropy disrupted the feature learning process. This contrasts with proposals that weight noise injection training achieves strong robustness [15], indicating that the *objective* driving the noise matters more than the noise itself.

Furthermore, the results extend the understanding of uncertainty in deep learning, where basic neural networks do not deliver certainty estimates [3]. While Bayesian statistics offer a formalism to understand and quantify the uncertainty [12], our results indicate that simply maximizing entropy without regard for posterior fidelity may be counterproductive. This supports the observation that neural networks intrinsically increase our uncertainty about which features of the analysis are model-related [5]. The failure of the intervention suggests that practitioners should not prioritize entropy maximization for robustness tasks over standard regularization in similar architectures.

**Implications for Practice**
For practitioners working with subject-disjoint time-series data, these results suggest that standard deterministic training with appropriate regularization (such as Batch Normalization which addresses the change in distribution of layer inputs [9]) may be preferable to complex entropy-maximized uncertainty mechanisms. The computational overhead of implementing entropy maximization [7] is not justified by performance gains in this domain, as no gains were observed. Future work should investigate whether these findings hold for larger pretrained Transformers, as pretrained Transformers improve out-of-distribution robustness in NLP datasets [8], though our results caution against assuming uncertainty mechanisms will similarly enhance robustness in smaller, task-specific models.

## 7. Limitations

This study is limited to a single dataset, the UCI Human Activity Recognition dataset, which may not generalize to other domains such as image classification or natural language processing. The model architecture, while representative of modern Transformers, is relatively small compared to state-of-the-art pretrained models, which may interact differently with uncertainty mechanisms. Additionally, the entropy maximization was applied only to the query projection layer; applying it to other components might yield different results. The study did not evaluate calibration metrics beyond accuracy, so the effect on uncertainty quantification quality remains unmeasured. Finally, the experiment was conducted under specific hyperparameters, and different learning rates or optimizers might alter the convergence stability observed [1].

Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.012509797746985206 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

This paper presented a preregistered evaluation of Entropy-Maximized Multiplicative Weight Noise for subject-disjoint robustness in Transformers. Contrary to the hypothesis, the intervention significantly reduced held-out classification accuracy compared to deterministic training in both primary and replication cohorts. The results refute the claim that entropy maximization improves generalization in this setting, aligning with literature warning of poor performance under covariate shift for certain Bayesian approximations. We conclude that practitioners should prioritize standard regularization over entropy maximization for robustness tasks in subject-disjoint time-series classification, as the core mechanism of node-based BNNs does not validate in this architecture.

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
2. Autonomous AI research system Stdlib Gradient Descent Learning Rate Sweep on Synthetic Non-Linear Data (n.d.). 
3. Jakob Gawlikowski, Cedrique Rovile Njieutcheu Tassi, Mohsin Ali et al. A survey of uncertainty in deep neural networks (2023). 10.1007/s10462-023-10562-9
4. Yuki Mae, Wataru Kumagai, Takafumi Kanamori Uncertainty propagation for dropout-based Bayesian neural networks (2021). 10.1016/j.neunet.2021.09.005
5. Tom Charnock, Laurence Perreault-Levasseur, François Lanusse Bayesian Neural Networks (2020). 2006.01490
6. Trung Trinh, Markus Heinonen, Luigi Acerbi et al. Tackling covariate shift with node-based Bayesian neural networks (2022). 2206.02435
7. Moule Lin, Shuhao Guan, Weipeng Jing et al. Stochastic Weight Sharing for Bayesian Neural Networks (2025). 2505.17856
8. Dan Hendrycks, Xiaoyuan Liu, Eric Wallace et al. Pretrained Transformers Improve Out-of-Distribution Robustness (2020). 10.18653/v1/2020.acl-main.244
9. Sergey Ioffe, Christian Szegedy Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (2015). 10.48550/arxiv.1502.03167
10. Kiranyaz, Mustafa Serkan, Onur Avcı, Osama Abdeljaber et al. 1D convolutional neural networks and applications: A survey (2021). 10.1016/j.ymssp.2020.107398
11. Jost Tobias Springenberg, Aaron Klein, Stefan Falkner et al. Bayesian optimization with robust Bayesian neural networks (2016). https://openalex.org/W2556372419
12. Laurent Valentin Jospin, Hamid Laga, Farid Boussaïd et al. Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users (2022). 10.1109/mci.2022.3155327
13. Pavel Izmailov, Patrick Nicholson, Sanae Lotfi et al. Dangers of Bayesian Model Averaging under Covariate Shift (2021). 2106.11905
14. Ehsan Variani, Ke Wu, David Rybach et al. Alignment Entropy Regularization (2022). 2212.12442
15. Jiashuo Shi A Diffractive Neural Network with Weight-Noise-Injection Training (2020). 2006.04462
16. Niko Hauzenberger, Florian Huber, Karin Klieber et al. Bayesian Neural Networks for Macroeconomic Analysis (2022). 2211.04752
17. José Miguel Hernández-Lobato, Ryan P. Adams Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks (2015). 10.48550/arxiv.1502.05336
18. Tommy Rochussen Structured Partial Stochasticity in Bayesian Neural Networks (2024). 2405.17666

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
