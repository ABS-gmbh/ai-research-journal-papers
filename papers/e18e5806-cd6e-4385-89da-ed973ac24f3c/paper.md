# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was generated end to end by an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** coding: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b, writing: qwen3.5-397b-a17b, ideation: qwen3.5-397b-a17b

## Abstract

Uncertainty quantification in deep learning aims to improve model robustness under distribution shift, yet the optimal mechanism for inducing uncertainty remains debated. This study investigates whether explicit entropy maximization of weight uncertainty parameters during training improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. We preregistered a hypothesis that an entropy-maximized multiplicative weight noise intervention would yield higher held-out classification accuracy than a deterministic baseline, exceeding a fixed worthwhile margin. We evaluated this using a PreNormTransformerEncoder on the UCI Human Activity Recognition dataset across 43 primary and 43 confirmatory-replication seeds. Contrary to the prediction, the intervention significantly worsened accuracy in both cohorts. In the primary cohort, the hypothesis-positive contrast was -0.04805 (95% CI [-0.0714, -0.0324], p=0.0002). The confirmatory replication cohort showed a contrast of -0.03482 (95% CI [-0.0422, -0.0278], p=0.0002). The preregistered direction was refuted. These results suggest that entropy maximization of weight noise does not generalize to attention-based architectures for subject-disjoint robustness, aligning with warnings that Bayesian methods can fail under covariate shift.

## 1. Introduction

Deep neural networks are increasingly deployed in safety-critical applications where confidence in predictions is paramount. However, basic neural networks do not deliver certainty estimates and often suffer from over- or under-confidence, meaning they are badly calibrated [3]. This limitation is particularly acute when models face distribution shifts, such as when test data originates from subjects not seen during training. In such subject-disjoint settings, the model must generalize beyond the specific statistical regularities of the training population. Bayesian neural networks (BNNs) offer a formalism to address this by quantifying uncertainty, yet deep learning methods often operate as black boxes where uncertainty is challenging to quantify [12].

While prior work explores weight noise injection and Bayesian uncertainty separately, no study explicitly maximizes the entropy of multiplicative weight noise distributions to improve subject-disjoint generalization in Transformers against standard variational objectives that minimize divergence. Node-based BNNs have shown promise in this area, where increasing the entropy of latent variables improved uncertainty estimation under covariate shift [6]. However, weight-based BNNs often struggle with high computational complexity, and approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13]. This creates an open problem: whether uncertainty-inducing mechanisms optimized for diversity via entropy maximization rather than posterior fidelity via KL minimization generalize to attention-based architectures under distribution shift.

This matter is significant because validating or refuting the core mechanism of node-based BNNs in modern architectures guides whether practitioners should prioritize entropy maximization for robustness tasks over standard regularization. If entropy maximization fails in Transformers despite success in node-based networks, it suggests architectural interactions limit the transferability of uncertainty mechanisms. Pretrained Transformers improve out-of-distribution robustness compared to previous models, exhibiting substantially smaller performance declines under realistic distribution shifts [8]. Nevertheless, understanding how to further enhance this robustness through training objectives remains critical.

This paper reports a preregistered experiment testing the impact of entropy-maximized weight noise on subject-disjoint generalization. We implemented an EntropyMaxWeightNoise module wrapping the query projection layer of a Transformer encoder. We compared this intervention against a deterministic baseline and negative controls. The preregistered hypothesis stated that the intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast exceeding a fixed worthwhile margin. We report the results honestly against this prediction, separating primary and confirmatory-replication cohorts.

Our contributions are as follows:
- We provide a rigorous test of entropy maximization for weight uncertainty in Transformers under subject-disjoint shift.
- We report a statistically significant refutation of the hypothesis that entropy maximization improves accuracy in this setting.
- We replicate the negative finding in a disjoint confirmatory cohort, ensuring the result is not a seed-specific artifact.
- We contextualize the negative result within existing literature on Bayesian robustness and covariate shift.

## 2. Related Work

**Uncertainty Quantification Necessity and Challenges**
Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important, yet basic neural networks do not deliver this confidence [3]. Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users describes deep learning methods as black boxes where uncertainty is challenging to quantify, stating that Bayesian statistics offer a formalism to address this [12]. Bayesian Neural Networks observes that neural networks intrinsically increase uncertainty about which features of the analysis are model-related and which are due to the neural network [5]. Uncertainty propagation for dropout-based Bayesian neural networks emphasizes uncertainty evaluation as core for detecting uncertain data in practical applications [4]. Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks highlights disadvantages of standard backpropagation such as lack of calibration [17]. However, Stochastic Weight Sharing for Bayesian Neural Networks and Structured Partial Stochasticity in Bayesian Neural Networks identify constraints regarding computational requirements, convergence difficulties, and posterior modes in BNNs [7, 18]. Bayesian Neural Networks for Macroeconomic Analysis develops BNNs specifically for data with limited observations [16].

**Robustness and Optimization under Distribution Shift**
Regarding robustness and optimization, Tackling covariate shift with node-based Bayesian neural networks states BNNs promise improved generalization under covariate shift but weight-based BNNs often struggle with high computational complexity [6]. Dangers of Bayesian Model Averaging under Covariate Shift warns that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13]. Pretrained Transformers Improve Out-of-Distribution Robustness systematically measures out-of-distribution generalization for pretrained Transformers on NLP datasets [8]. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift addresses the change in distribution of layer inputs during training [9]. A Diffractive Neural Network with Weight-Noise-Injection Training proposes weight noise injection training to achieve strong robustness [15]. Alignment Entropy Regularization uses entropy to measure a model's uncertainty in distributing probability mass over sequences [14]. Bayesian optimization with robust Bayesian neural networks discusses Bayesian optimization for tuning hyperparameters in the context of robust Bayesian neural networks [11]. Additionally, Precision-Dependent Breakdown of Momentum in Ill-Conditioned Linear Regression and Stdlib Gradient Descent Learning Rate Sweep on Synthetic Non-Linear Data investigate convergence stability and learning rate effects in optimization [1, 2]. 1D convolutional neural networks are standard for various operations including structural health monitoring [10].

**Positioning This Work**
This work positions itself against the promise of node-based BNNs [6] by testing the entropy mechanism in a Transformer architecture. While weight noise injection has been proposed for robustness [15], the specific optimization of entropy maximization versus divergence minimization remains under-explored in attention models. The warning that Bayesian methods can fail under covariate shift [13] provides a critical counterpoint to the hypothesis that entropy maximization will improve generalization. By separating primary and replication cohorts, we address the convergence stability concerns noted in optimization literature [1].

## 3. Method

The experiment runs the calibrated testbed uci_har_small_transformer_v1. The dataset consists of raw inertial signals formatted as 128-timestep windows over 9 channels, with an official subject-disjoint split of 7,352 training and 2,947 held-out windows. The model architecture is a PreNormTransformerEncoder comprising a Linear projection from 9 to 64 dimensions and a learned positional embedding of 128 timesteps to 64 dimensions. The encoder contains 2 blocks, each consisting of LayerNorm followed by 4-head self-attention over 128 timesteps with query, key, value, and output Linear layers of 64 dimensions, followed by a residual connection. This is followed by LayerNorm, a Linear layer to 128 dimensions, ReLU activation, a Linear layer back to 64 dimensions, and a residual connection. A final LayerNorm precedes mean-pooling over time and a Linear projection to 6 output classes.

Training proceeds for 12 epochs with a batch size of 128 using SGD with a learning rate of 0.05 and momentum of 0.9. Evaluation is performed as the number of correct activity predictions divided by 2,947 windows in the official subject-disjoint test split. We implement EntropyMaxWeightNoise as a custom module wrapping the query projection layer. For each seed, we initialize identical model weights to ensure comparability.

We run four conditions. The Intervention condition applies EntropyMax weight noise. The Baseline condition uses Deterministic Training (Identity Control). The first negative control applies EntropyMin weight noise. The second negative control applies FixedNoise. We aggregate accuracy per seed and compute paired contrasts between the Intervention and Baseline conditions. We apply the preregistered decision rule on the Primary block, then confirm on the Replication block. The metric is held-out classification accuracy. We use 43 primary seeds and 43 disjoint confirmatory-replication seeds. The identities of these seeds are recorded in the appendix. We do not pool the cohorts; each is analyzed separately to maintain the integrity of the preregistered decision rule.

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

The dataset used is the UCI Human Activity Recognition Using Smartphones, available via DOI 10.24432/C54S4K. The data comprises raw inertial signals from smartphones, segmented into 128-timestep windows across 9 channels. The official split ensures subject disjointness, with 7,352 windows for training and 2,947 windows for held-out testing. This split is critical for evaluating generalization to unseen subjects, representing a realistic distribution shift scenario.

The model implementation uses PyTorch. The PreNormTransformerEncoder is configured with 64-dimensional embeddings and 2 attention blocks. The EntropyMaxWeightNoise module modifies the query projection layer by introducing multiplicative noise parameters optimized to maximize entropy during the training loop. Hyperparameters were fixed prior to the experiment: 12 epochs, batch size 128, SGD optimizer with learning rate 0.05 and momentum 0.9. No learning rate scheduling was applied.

We executed the experiment across two disjoint blocks of seeds. The primary cohort consisted of 43 seeds. The confirmatory-replication cohort consisted of 43 disjoint seeds. All conditions (Intervention, Baseline, the first negative control, the second negative control) were run for every seed in both cohorts. This design allows for paired contrasts within seeds, reducing variance due to initialization. The computational setup ensured identical initialization for all conditions within a seed to isolate the effect of the noise mechanism. Training loss and final accuracy were recorded for every run.

We evaluate on UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows). Held-out evaluation uses the official UCI HAR test split — 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning. The model is PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)). Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training. Training budget: 12 epochs; batch size 128; SGD(lr=0.05,momentum=0.9). The outcome is held-out classification accuracy — number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split (proportion). The dataset was downloaded, checksum-verified against its published SHA-256 and staged read-only to the compute node before the job started; the exact archive, checksum, licence and training configuration are given in the appendix.

## 5. Results

We report the results for the primary and confirmatory-replication cohorts separately, adhering to the preregistered analysis plan. Figure 1 displays the final metric values per condition with 95% bootstrap confidence intervals over seeds for the primary cohort. Table 1 summarizes the held-out classification accuracy for the primary cohort.

In the primary cohort, across 4 conditions and 43 seeds, the proposed condition worsened the hypothesis-positive contrast by 0.04805 versus the baseline 1 condition. The 95% confidence interval for this contrast was [-0.0714, -0.0324]. The paired randomisation p-value was 0.0002, and Cohen's dz was -0.72. This is a statistically significant difference as the 95% confidence interval excludes zero. The mean accuracy for the Proposed condition was 0.8604 (95% CI [0.837, 0.877]), while the Baseline 1 condition achieved 0.9085 (95% CI [0.905, 0.912]). The negative controls performed similarly to the baseline, with Negative control 1 at 0.9082 and Negative control 2 at 0.909. The preregistered decision was that the preregistered direction was refuted.

Figure 2 shows the mean training loss over training steps for each condition in the primary cohort. The loss curves indicate stable convergence for all conditions, suggesting the performance difference is not due to optimization failure but rather the effect of the noise mechanism on generalization.

In the confirmatory replication cohort, across 4 conditions and 43 seeds, the proposed condition worsened the hypothesis-positive contrast by 0.03482 versus the baseline 1 condition. The 95% confidence interval was [-0.0422, -0.0278]. The paired randomisation p-value was 0.0002, and Cohen's dz was -1.41. This is a statistically significant difference as the 95% confidence interval excludes zero. The mean accuracy for the Proposed condition was 0.8717 (95% CI [0.865, 0.877]), while the Baseline 1 condition achieved 0.9065 (95% CI [0.903, 0.91]). Negative control 1 achieved 0.908 and Negative control 2 achieved 0.9088. The preregistered decision was that the preregistered direction was refuted.

The consistency of the negative result across both cohorts indicates that the entropy maximization mechanism systematically reduces accuracy in this setting. The effect size was large in both cohorts (dz=-0.72 and dz=-1.41), reinforcing the robustness of the refutation.

Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

The results explicitly refute the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data. In both primary and replication cohorts, the intervention significantly reduced held-out classification accuracy compared to deterministic training. This finding contrasts with the success of node-based BNNs where increasing entropy of latent variables improved uncertainty estimation under covariate shift [6]. The discrepancy suggests that the mechanism effective for node-based uncertainty does not transfer to multiplicative weight noise in Transformer query projections.

This negative outcome aligns with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13]. Specifically, Bayesian model averaging can be problematic under covariate shift when linear dependencies in input features cause a lack of posterior contraction [13]. While our method did not perform full Bayesian averaging, the introduction of entropy-maximized noise may have similarly disrupted the model's ability to contract onto robust features under subject-disjoint shift. The result also contextualizes the claim that pretrained Transformers exhibit substantially smaller performance declines under realistic distribution shifts [8]; our intervention appears to interfere with this inherent robustness rather than enhance it.

The failure of entropy maximization here suggests that diversity in weight space, when optimized directly via entropy, may conflict with the feature learning required for subject-disjoint generalization in attention architectures. Standard regularization or deterministic training may preserve the specific feature alignments necessary for this task better than noise-induced diversity. This supports the view that uncertainty-inducing mechanisms optimized for diversity rather than posterior fidelity may not generalize to all architectures. The negative controls performing similarly to the baseline confirms that the degradation is specific to the entropy maximization objective, not merely the presence of noise.

These findings guide practitioners away from prioritizing entropy maximization for robustness tasks in this specific Transformer setting. Instead, standard regularization or architectures designed specifically for covariate shift should be preferred. The result validates the importance of empirical testing of uncertainty mechanisms in modern architectures, as theoretical benefits observed in node-based networks do not guarantee transferability.

## 7. Limitations

This study is limited to a single dataset, UCI Human Activity Recognition, and a specific Transformer architecture. While the subject-disjoint split provides a rigorous test of distribution shift, results may not generalize to other domains such as natural language processing or image classification. The model size was relatively small (2 attention blocks), and entropy maximization effects might differ in larger pretrained models. Additionally, we focused on multiplicative weight noise on the query projection; other layers or noise types might yield different results. The experiment did not evaluate uncertainty calibration metrics, focusing solely on accuracy, so the effect on uncertainty quality remains unknown.

Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.0125098 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

We conducted a preregistered experiment to test whether entropy-maximized multiplicative weight noise improves subject-disjoint robustness in Transformers. The hypothesis was refuted in both primary and confirmatory-replication cohorts, with the intervention significantly reducing accuracy compared to deterministic training. This negative result highlights that entropy maximization mechanisms successful in node-based BNNs do not necessarily transfer to attention-based architectures. Practitioners should prioritize standard regularization over entropy maximization for this task until further evidence suggests otherwise.

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
| Proposed | 43 | 0.8604 [0.837, 0.877] |
| Baseline 1 | 43 | 0.9085 [0.905, 0.912] |
| Negative control 1 | 43 | 0.9082 [0.905, 0.911] |
| Negative control 2 | 43 | 0.909 [0.906, 0.912] |

**Table 2.** Replication cohort: results by condition (mean [95% CI] over seeds)

| condition | seeds | held-out classification accuracy |
| --- | --- | --- |
| Proposed | 43 | 0.8717 [0.865, 0.877] |
| Baseline 1 | 43 | 0.9065 [0.903, 0.91] |
| Negative control 1 | 43 | 0.908 [0.904, 0.912] |
| Negative control 2 | 43 | 0.9088 [0.905, 0.912] |

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
