# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** ideation: qwen3.5-397b-a17b, coding: qwen3.5-397b-a17b, writing: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b

## Abstract

Uncertainty quantification in deep learning is critical for safety-critical applications, yet standard neural networks often lack calibrated confidence estimates. This study investigates whether explicit entropy maximization of weight uncertainty parameters during training improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. We implemented an Entropy-Maximized Multiplicative Weight Noise operator within a Transformer encoder and evaluated it on the UCI Human Activity Recognition dataset using an official subject-disjoint split. The preregistered hypothesis predicted that the intervention would yield higher held-out classification accuracy than the baseline, exceeding a fixed worthwhile margin. Contrary to this prediction, the intervention significantly worsened performance in both the primary and confirmatory-replication cohorts. The mean accuracy difference was negative with tight confidence intervals excluding zero, leading to a refutation of the preregistered direction. These findings suggest that entropy maximization of weight noise parameters does not generalize to attention-based architectures under distribution shift in this setting and may actively degrade performance compared to deterministic training. Practitioners should prioritize standard regularization over entropy-maximized weight uncertainty for similar robustness tasks until further evidence supports otherwise.

## 1. Introduction

Neural networks have become ubiquitous in scientific and real-world applications, yet confidence in their predictions remains a significant challenge. Basic neural networks do not deliver certainty estimates and often suffer from over- or under-confidence, meaning they are badly calibrated [1]. As deep learning methods operate as black boxes, the uncertainty associated with their predictions is often challenging to quantify [10]. This lack of calibrated probabilistic predictions is a known disadvantage of standard backpropagation [15]. In practical applications, detecting uncertain data is significant for safety-critical systems, making uncertainty evaluation a core technique [2]. However, the introduction of neural networks intrinsically increases uncertainty about which features of the analysis are model-related and which are due to the network itself [3]. Bayesian neural networks (BNNs) offer a formalism to address this by characterizing uncertainty due to the network [3]. Weight-based BNNs promise improved generalization under covariate shift by providing principled probabilistic representations of epistemic uncertainty [4]. However, they often struggle with high computational complexity and convergence difficulties in large-scale architectures [5]. Recent work has explored node-based alternatives where diversity depends on the entropy of latent variables, proposing approaches to increase this entropy during training to improve uncertainty estimation under covariate shift [4]. Yet, it remains an open problem whether uncertainty-inducing mechanisms optimized for diversity via entropy maximization, rather than posterior fidelity via KL minimization, generalize to attention-based architectures under distribution shift. This Registered Report presents a rigorous, preregistered study addressing this gap. We test whether explicit entropy maximization of multiplicative weight noise distributions improves subject-disjoint generalization in Transformers against standard variational objectives. The research question is whether this intervention yields higher held-out classification accuracy than standard deterministic training. The preregistered hypothesis predicted that the intervention would exceed the comparator by a fixed worthwhile margin. This work matters because it validates or refutes the core mechanism of node-based BNNs [4] in modern architectures, guiding whether practitioners should prioritize entropy maximization for robustness tasks over standard regularization. The contributions of this paper are:
- We implement and evaluate an Entropy-Maximized Multiplicative Weight Noise operator within a Transformer encoder on a subject-disjoint time-series benchmark. - We report a preregistered negative finding where the intervention significantly worsened accuracy compared to the baseline, refuting the hypothesis in both primary and replication cohorts. - We contextualize these results against prior work on weight noise and covariate shift, clarifying the limitations of entropy maximization in this architectural context.

## 2. Related Work

Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important, yet basic neural networks do not deliver this confidence [1]. Deep learning methods operate as black boxes where uncertainty is challenging to quantify, and Bayesian statistics offer a formalism to address this [10]. Neural networks intrinsically increase uncertainty about which features of the analysis are model-related and which are due to the neural network [3]. Uncertainty evaluation is core for detecting uncertain data in practical applications [2]. Standard backpropagation has disadvantages such as lack of calibration [15]. However, constraints exist regarding computational requirements, convergence difficulties, and posterior modes in BNNs [5, 16]. Some developments focus on data with limited observations [14]. Regarding robustness and optimization, BNNs promise improved generalization under covariate shift but weight-based BNNs often struggle with high computational complexity [4]. Approximate Bayesian inference considered robust can achieve poor performance under covariate shift [11]. Pretrained Transformers improve out-of-distribution robustness in NLP datasets, though larger models are not necessarily more robust [6]. Internal covariate shift, the change in distribution of layer inputs during training, is addressed by normalization techniques [7]. Weight noise injection training is proposed to achieve strong robustness in specific physical implementations [13]. Entropy is used to measure a model's uncertainty in distributing probability mass over sequences in speech recognition [12]. Bayesian optimization discusses tuning hyperparameters in the context of robust Bayesian neural networks [9]. Additionally, 1D convolutional neural networks have become standard for various operations on 1D signals [8]. This work positions itself against these findings by testing entropy maximization specifically in a Transformer architecture under subject-disjoint shift. While node-based approaches have shown success with entropy increases [4], weight-based mechanisms in attention models remain under-explored. The warning that Bayesian model averaging can be problematic under covariate shift [11] suggests caution is warranted. We extend the investigation of weight noise injection [13] to modern attention mechanisms, testing whether the robustness observed in other contexts holds here.

## 3. Method

The experiment tests the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy. The core operator is EntropyMaxWeightNoise, a custom module wrapping the query projection layer of the Transformer. This operator injects multiplicative noise into the weights during training, with the noise parameters optimized to maximize entropy. This design choice reflects the hypothesis that increasing the diversity of the implicit weight distributions will enhance robustness to distribution shift, aligning with observations that diversity depends on the entropy of latent variables in node-based models [4]. The comparator is the baseline condition, which uses standard deterministic training without weight noise. This neutralises the effect of the noise injection itself, isolating the impact of the entropy maximization objective. To ensure that any observed effects are due to the entropy direction rather than the presence of noise, we include two negative controls. The first negative control uses entropy minimization on the same noise parameters, testing whether reducing diversity harms performance as much as maximizing it helps. The second negative control uses fixed noise without entropy optimization, ruling out the possibility that any noise injection is beneficial regardless of the objective. The operator is the right expression of the hypothesis because it directly targets the mechanism proposed in prior work where increasing entropy improved uncertainty estimation under covariate shift [4]. By applying this to the weight parameters rather than node activations, we test the generalizability of the mechanism to weight-based uncertainty. The comparator neutralises the confounding variable of stochastic training dynamics, ensuring that differences in accuracy are attributable to the entropy objective. The negative controls rule out alternative explanations such as regularization effects from noise alone. The analysis computes paired contrasts between the intervention and the baseline for each seed. This paired design controls for seed-specific variance, increasing the power to detect the predicted effect. The preregistered decision rule applies a fixed worthwhile margin to the mean contrast. If the lower bound of the confidence interval exceeds this margin, the hypothesis is supported. If the interval excludes zero in the opposite direction, the direction is refuted. This rigorous decision process ensures that claims about robustness are grounded in statistically significant evidence rather than anecdotal improvement.

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

The design employs a subject-disjoint split to test generalization to unseen individuals, which is critical for activity recognition where sensor characteristics vary between users. A random split would have hidden this distribution shift, potentially inflating accuracy estimates and failing to test the robustness claim. By holding out entire subjects, we ensure the evaluation measures true out-of-distribution performance rather than memorization of subject-specific patterns. This aligns with the goal of validating robustness under covariate shift [4]. We use 43 primary seeds and 43 disjoint confirmatory-replication seeds to ensure statistical power and reproducibility. This number of seeds allows for precise estimation of the confidence intervals around the mean accuracy, reducing the risk of false positives due to random initialization. Pairing every condition on one seed buys control over initialization variance, ensuring that the paired contrast isolates the effect of the training condition. The cost is increased computational load, but this is necessary for a rigorous test of the hypothesis. Each negative control rules out specific confounds. Without the first negative control, we could not distinguish whether entropy maximization was beneficial or if any deviation from deterministic training was harmful. Without the second negative control, we could not determine if the optimization of the noise parameters was necessary or if fixed noise sufficed. These controls make the attribution of effects to the entropy objective distinct from general noise injection effects [13]. The analysis aggregates accuracy per seed and computes paired contrasts, applying the preregistered decision rule on the Primary block before confirming on the Replication block. This two-stage process protects against overfitting to the primary sample and ensures the finding is stable across disjoint data realizations. Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training. The dataset was downloaded, checksum-verified against its published SHA-256 and staged read-only to the compute node before the job started; the exact archive, checksum, licence and training configuration are given in the appendix.

## 5. Results

We report the evidence for the primary and confirmatory-replication cohorts separately. In the primary cohort, across 4 conditions and 43 seeds, we report each metric's mean with a bootstrap 95% confidence interval. On held-out classification accuracy, the proposed condition achieved a mean of 0.8604 [0.837, 0.877]. The baseline condition achieved 0.9085 [0.905, 0.912]. The proposed condition worsened the contrast in the hypothesised direction by 0.04805 versus the baseline condition (95% CI [-0.0714, -0.0324], paired randomisation p=0.0002, Cohen's dz=-0.72). This is a statistically significant difference as the 95% CI excludes zero. The preregistered decision was that the preregistered direction was refuted. Figure 1 displays the final metric values per condition with 95% bootstrap confidence intervals over seeds, illustrating the separation between the proposed condition and the baseline. In the confirmatory replication cohort, across 4 conditions and 43 seeds, we report each metric's mean with a bootstrap 95% confidence interval. On held-out classification accuracy, the proposed condition achieved a mean of 0.8717 [0.865, 0.877]. The baseline condition achieved 0.9065 [0.903, 0.91]. The proposed condition worsened the contrast in the hypothesised direction by 0.03482 versus the baseline condition (95% CI [-0.0422, -0.0278], paired randomisation p=0.0002, Cohen's dz=-1.41). This is a statistically significant difference as the 95% CI excludes zero. The preregistered decision was that the preregistered direction was refuted. Figure 3 displays the final metric values for the replication cohort, confirming the trend observed in the primary block. The negative controls performed similarly to the baseline. The first negative control achieved 0.9082 [0.905, 0.911] in the primary cohort and 0.908 [0.904, 0.912] in the replication cohort. The second negative control achieved 0.909 [0.906, 0.912] in the primary cohort and 0.9088 [0.905, 0.912] in the replication cohort. Table 1 and Table 2 summarize the held-out classification accuracy for all conditions in the primary and replication cohorts respectively. Figure 2 and Figure 4 show the mean training loss over training steps for each condition, indicating that the proposed condition did not converge to a lower loss despite the entropy objective. The consistency of the negative result across both cohorts strengthens the conclusion that the intervention harms performance in this setting. Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

The results explicitly refute the hypothesis that entropy maximization of weight uncertainty improves subject-disjoint generalization in Transformers. The intervention significantly worsened accuracy compared to the baseline in both cohorts. This finding contradicts the expectation derived from node-based BNNs where increasing entropy of latent variables improved uncertainty estimation under covariate shift [4]. It suggests that the mechanism does not transfer directly to weight-based uncertainty in attention architectures. The negative effect was robust, with large effect sizes (dz=-0.72 and dz=-1.41), indicating this is not a marginal failure but a substantial degradation. This aligns with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [11]. Our results extend this observation to entropy-maximized weight noise, showing that not all uncertainty-inducing mechanisms confer robustness. While weight noise injection training has achieved strong robustness in diffractive neural networks [13], our findings indicate this does not generalize to Transformer-based time-series classification without careful tuning or architectural adaptation. The negative controls performed near the baseline, suggesting that the harm is specific to the entropy maximization objective rather than noise injection per se. The findings matter for practitioners choosing between these methods. Prior work describes CNNs as standard for various operations on 1D signals [8], and Transformers are increasingly used for time-series data. However, our results suggest that adding entropy-maximized weight noise to such Transformers is detrimental. This clarifies the limitations of the specific testbed without overgeneralizing to broader Bayesian contexts. It confirms that weight-based BNNs can struggle with computational complexity and convergence [5], manifesting here as reduced accuracy. Future work should investigate whether different entropy regularizers or architectural modifications can recover the benefits seen in node-based models [4].

## 7. Limitations

This study is limited to a single dataset and architecture. The UCI Human Activity Recognition dataset involves inertial signals, which may not represent all time-series domains. The Transformer architecture used is specific, with two blocks and 64-dimensional embeddings, and results may differ in larger models. The subject-disjoint split tests generalization to new users but does not cover all forms of distribution shift, such as sensor drift or environmental changes. The entropy maximization operator was applied only to the query projection layer; applying it to other layers might yield different results. Finally, the training budget was fixed at 12 epochs; longer training might allow the entropy objective to converge differently, though the replication cohort suggests the effect is stable. Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.0125098 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

This study found that explicit entropy maximization of weight uncertainty parameters significantly worsened out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. The preregistered hypothesis was refuted in both primary and replication cohorts with statistically significant negative contrasts. This changes the recommendation for practitioners choosing between these methods: entropy-maximized weight noise should not be prioritized for robustness tasks in this architectural context. Standard regularization remains preferable. To settle the question next, future work should test whether node-based entropy mechanisms [4] can be adapted to weight parameters without degrading accuracy, or whether alternative uncertainty objectives provide the intended robustness under covariate shift [11].

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
| Baseline | 43 | 0.9085 [0.905, 0.912] |
| Negative control 1 | 43 | 0.9082 [0.905, 0.911] |
| Negative control 2 | 43 | 0.909 [0.906, 0.912] |

**Table 2.** Replication cohort: results by condition (mean [95% CI] over seeds)

| condition | seeds | held-out classification accuracy |
| --- | --- | --- |
| Proposed | 43 | 0.8717 [0.865, 0.877] |
| Baseline | 43 | 0.9065 [0.903, 0.91] |
| Negative control 1 | 43 | 0.908 [0.904, 0.912] |
| Negative control 2 | 43 | 0.9088 [0.905, 0.912] |

## References

1. Jakob Gawlikowski, Cedrique Rovile Njieutcheu Tassi, Mohsin Ali et al. A survey of uncertainty in deep neural networks (2023). 10.1007/s10462-023-10562-9
2. Yuki Mae, Wataru Kumagai, Takafumi Kanamori Uncertainty propagation for dropout-based Bayesian neural networks (2021). 10.1016/j.neunet.2021.09.005
3. Tom Charnock, Laurence Perreault-Levasseur, François Lanusse Bayesian Neural Networks (2020). 2006.01490
4. Trung Trinh, Markus Heinonen, Luigi Acerbi et al. Tackling covariate shift with node-based Bayesian neural networks (2022). 2206.02435
5. Moule Lin, Shuhao Guan, Weipeng Jing et al. Stochastic Weight Sharing for Bayesian Neural Networks (2025). 2505.17856
6. Dan Hendrycks, Xiaoyuan Liu, Eric Wallace et al. Pretrained Transformers Improve Out-of-Distribution Robustness (2020). 10.18653/v1/2020.acl-main.244
7. Sergey Ioffe, Christian Szegedy Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (2015). 10.48550/arxiv.1502.03167
8. Kiranyaz, Mustafa Serkan, Onur Avcı, Osama Abdeljaber et al. 1D convolutional neural networks and applications: A survey (2021). 10.1016/j.ymssp.2020.107398
9. Jost Tobias Springenberg, Aaron Klein, Stefan Falkner et al. Bayesian optimization with robust Bayesian neural networks (2016). https://openalex.org/W2556372419
10. Laurent Valentin Jospin, Hamid Laga, Farid Boussaïd et al. Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users (2022). 10.1109/mci.2022.3155327
11. Pavel Izmailov, Patrick Nicholson, Sanae Lotfi et al. Dangers of Bayesian Model Averaging under Covariate Shift (2021). 2106.11905
12. Ehsan Variani, Ke Wu, David Rybach et al. Alignment Entropy Regularization (2022). 2212.12442
13. Jiashuo Shi A Diffractive Neural Network with Weight-Noise-Injection Training (2020). 2006.04462
14. Niko Hauzenberger, Florian Huber, Karin Klieber et al. Bayesian Neural Networks for Macroeconomic Analysis (2022). 2211.04752
15. José Miguel Hernández-Lobato, Ryan P. Adams Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks (2015). 10.48550/arxiv.1502.05336
16. Tommy Rochussen Structured Partial Stochasticity in Bayesian Neural Networks (2024). 2405.17666

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

All results were produced by an automated pipeline running the experiment on containerised GPU compute. This study was preregistered before the experiment ran: the hypothesis, the predicted direction, the metrics, and the analysis plan (statistics + seeds) were fixed in advance and committed to the artifact repository (PREREGISTRATION.md). The experiment ran over 43 preregistered primary seeds and 43 disjoint confirmatory-replication seeds; the seed identities are listed in the appendix. Compute job id: 15540577. Container image: pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755. Walltime: 01:30:00. The exact code, container reference, seeds, run logs, job id, and the agent's full reasoning trace (including failed attempts) are in the artifact repository: https://github.com/ABS-gmbh/ai-research-journal-papers.

## Ethics

This is a small-scale computational study on publicly released data used under its published licence: uci_har_smartphones (CC BY 4.0). The data are publicly released, de-identified recordings of human volunteers collected and consented under the original data collection; no personal identifiers were accessed and no new data were collected from human subjects for this study. It poses no foreseeable ethical or dual-use risks. Compute use was deliberately minimal.
