# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was produced end to end by ABS AI RSE, an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** ideation: qwen3.5-397b-a17b, coding: qwen3.5-397b-a17b, writing: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b

## Abstract

This preregistered study evaluates whether explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. While prior work suggests uncertainty-inducing mechanisms may enhance robustness under distribution shift, empirical validation in modern attention-based architectures remains limited. We implemented an Entropy-Maximized Multiplicative Weight Noise operator within a Transformer encoder and evaluated it on the UCI Human Activity Recognition Using Smartphones dataset, utilizing the official subject-disjoint split. The experiment comprised primary and confirmatory-replication cohorts, each with 43 seeds, comparing the proposed condition against a deterministic baseline and two negative controls. Contrary to the preregistered hypothesis, the proposed condition yielded lower held-out classification accuracy than the baseline in both cohorts. In the primary cohort, the proposed condition achieved 0.8604 accuracy versus 0.9085 for the baseline, a significant negative contrast. The confirmatory replication cohort corroborated this finding. These results indicate that entropy maximization on weight noise parameters does not confer robustness benefits in this setting and may impair generalization. The findings suggest practitioners should prioritize standard regularization over entropy-maximized weight noise for subject-disjoint robustness in Transformers.

## 1. Introduction

Deep neural networks are increasingly deployed in settings where input distributions differ between training and deployment, such as wearable sensor analysis where user physiology varies significantly. In these subject-disjoint scenarios, models face covariate shift that can degrade performance despite high training accuracy. Robustness to such shifts is critical for reliability, yet standard deterministic training often fails to generalize beyond the training population. Uncertainty quantification has been proposed as a mechanism to improve robustness, under the hypothesis that models aware of their own uncertainty may resist overfitting to spurious training features. However, basic neural networks do not deliver certainty estimates or suffer from calibration issues, limiting their utility in safety-critical applications [1]. Bayesian neural networks (BNNs) offer a formalism to quantify uncertainty, potentially addressing the black-box nature of deep learning where uncertainty is challenging to quantify [5]. Theoretical work suggests that characterizing uncertainty due to the network itself distinguishes model-related features from data observation noise [2]. Furthermore, standard backpropagation lacks calibrated probabilistic predictions and tends to overfit, disadvantages the Bayesian approach aims to resolve [7]. Despite these theoretical benefits, practical implementation often struggles with computational complexity, particularly in weight-based BNNs [3]. Recent advances propose node-based uncertainty mechanisms that induce epistemic uncertainty via latent random variables, showing improved performance under covariate shift due to input corruptions [3]. However, whether explicit entropy maximization of weight uncertainty parameters generalizes to attention-based architectures under subject-disjoint shift remains an open empirical question. Current literature identifies a gap regarding whether uncertainty-inducing mechanisms optimized for diversity via entropy maximization, rather than posterior fidelity via KL minimization, generalize to Transformers. While weight noise injection has been proposed to achieve robustness by making weights insensitive to modest changes [6], the specific effect of maximizing the entropy of multiplicative weight noise distributions during training is untested in this domain. This work addresses whether such explicit entropy maximization improves out-of-distribution accuracy compared to standard deterministic training. This paper presents a rigorous, preregistered negative result evaluating Entropy-Maximized Multiplicative Weight Noise. We report the following contributions:
- We implement a custom EntropyMaxWeightNoise operator within a PreNormTransformerEncoder and evaluate it on real declared datasets (UCI HAR) using an official subject-disjoint split. - We conduct a primary experiment and a confirmatory-replication cohort, each with 43 seeds, ensuring statistical power to detect the preregistered worthwhile margin. - We provide honest reporting against the preregistered hypothesis, demonstrating that the intervention refuted the predicted accuracy gain and instead significantly reduced held-out performance.

## 2. Related Work

**Uncertainty Quantification in Deep Learning**
Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important for reliable deployment. However, basic neural networks do not deliver certainty estimates or suffer from over- or under-confidence, meaning they are badly calibrated [1]. Modern deep learning methods operate as black boxes where the uncertainty associated with predictions is often challenging to quantify [5]. Bayesian statistics offer a formalism to understand and quantify this uncertainty, categorizing it in terms of ingrained randomness in data observation and lack of knowledge about data creation [2]. This distinction is crucial because neural networks intrinsically increase uncertainty about which features of the analysis are model-related and which are due to the neural network itself [2]. While the Bayesian approach theoretically avoids disadvantages of standard backpropagation such as lack of calibrated probabilistic predictions and overfitting, existing techniques often lack scalability to large dataset and network sizes [7]. Consequently, practitioners face a trade-off between theoretical robustness and computational feasibility. **Robustness and Covariate Shift**
Regarding robustness and optimization, distribution shift remains a primary challenge for generalization. Training Deep Neural Networks is complicated by the fact that the distribution of each layer's inputs changes during training, a phenomenon referred to as internal covariate shift [4]. External covariate shift, such as that induced by subject disjointness, requires models to generalize beyond the training distribution. Bayesian neural networks promise improved generalization under covariate shift by providing principled probabilistic representations of epistemic uncertainty [3]. However, weight-based BNNs often struggle with high computational complexity of large-scale architectures and datasets [3]. Node-based BNNs have been introduced as scalable alternatives, inducing epistemic uncertainty by multiplying each hidden node with latent random variables while learning a point-estimate of the weights [3]. These methods interpret latent noise variables as implicit representations of domain-agnostic data perturbations, performing well under covariate shift due to input corruptions [3]. Crucially, the diversity of these implicit corruptions depends on the entropy of the latent variables, suggesting entropy maximization may aid robustness [3]. **Noise Injection and Regularization**
Alternative approaches to robustness involve direct noise injection during training. Weight noise injection training has been proposed to achieve strong robustness by making the network's weight insensitive to modest changes [6]. This method reduces the impact of external interference on inference results, verifying that networks maintain higher accuracy under serious noise compared to standard training [6]. However, most existing work focuses on convolutional architectures or specific optical-based classifications, leaving the effect on Transformer-based time-series models underexplored. While some literature discusses Bayesian optimization for tuning hyperparameters in robust Bayesian neural networks, the direct impact of entropy-maximized weight noise on accuracy under subject-disjoint shift is not established in the provided references. This work positions itself against these findings by testing whether the entropy mechanism identified in node-based systems [3] translates to multiplicative weight noise in Transformers, or if the robustness benefits observed in diffractive networks [6] fail to materialize in this architecture.

## 3. Method

The core intervention implements an Entropy-Maximized Multiplicative Weight Noise operator designed to explicitly maximize the entropy of weight uncertainty parameters during training. This operator wraps the query projection layer of the attention mechanism. For each forward pass, the operator samples a noise mask from a parameterized distribution and multiplies it with the weight matrix. Unlike standard variational objectives that minimize divergence to a prior, this method optimizes the entropy of the noise distribution directly. The entropy maximization objective encourages the noise parameters to maintain a high degree of uncertainty, theoretically preventing the model from collapsing to a deterministic state. The operator computes the entropy of the multiplicative noise distribution at each step and adds this term to the loss function with a scaling coefficient. This contrasts with standard Bayesian approaches that seek posterior fidelity. The hypothesis posits that this diversity in weight configurations acts as a regularizer, improving generalization to unseen subjects. The implementation utilizes a custom PyTorch module. For each seed, identical model weights are initialized to ensure comparability across conditions. The operator is applied only during training; inference uses the expected value of the weights to ensure deterministic output. The loss function combines the standard classification cross-entropy with the entropy regularization term. The optimization proceeds via stochastic gradient descent. The method does not alter the architecture's depth or width but modifies the parameter update dynamics. By targeting the query projection, the intervention focuses on the attention mechanism's ability to weigh temporal features, which is critical for activity recognition. The design assumes that preventing weight certainty will force the model to rely on more robust features shared across subjects.

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

This split ensures that no subject appears in both training and testing, enforcing a robustness requirement beyond random splitting. The encoder contains 2 blocks, each with LayerNorm, 4-head self-attention over 128 timesteps (q/k/v/out Linear 64 to 64), residual connections, and a feed-forward network (Linear 64 to 128, ReLU, Linear 128 to 64). A final LayerNorm and mean-pool over time precede the classification head (Linear 64 to 6). The design includes four conditions: the proposed condition (EntropyMax), the baseline (Deterministic), the first negative control (EntropyMin), and the second negative control (FixedNoise). We aggregated accuracy per seed and computed paired contrasts. The experiment utilized 43 primary seeds and 43 disjoint confirmatory-replication seeds. This pairing allows us to rule out seed-specific artifacts and confirm whether the effect holds across independent runs. The subject-disjoint split was chosen to strictly test generalization to new users, which is the primary failure mode for wearable activity recognition systems. Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training. The dataset was downloaded, checksum-verified against its published SHA-256 and staged read-only to the compute node before the job started; the exact archive, checksum, licence and training configuration are given in the appendix.

## 5. Results

We report results for the primary and confirmatory-replication cohorts separately, adhering to the preregistered analysis plan. Table 1 presents the final metric values per condition with 95% bootstrap confidence intervals over seeds for the primary cohort. On held-out classification accuracy, the proposed condition achieved a mean of 0.8604 [0.837, 0.877], while the baseline achieved 0.9085 [0.905, 0.912]. The first negative control scored 0.9082 [0.905, 0.911], and the second negative control scored 0.909 [0.906, 0.912]. The hypothesis-positive paired contrast (Intervention minus Baseline) was -0.04805 (95% CI [-0.0714, -0.0324], paired randomisation p=0.0002, Cohen's dz=-0.72). This difference is statistically significant as the 95% CI excludes zero. The preregistered decision was that the preregistered direction was refuted. The proposed condition worsened accuracy relative to the baseline by a substantial margin, exceeding the fixed worthwhile margin in the negative direction. Figure 1 visualizes these final metric values, showing clear separation between the proposed condition and the controls. Figure 2 displays the mean training loss over training steps, indicating that the proposed condition converged to a higher loss than the baseline. Table 2 presents the results for the confirmatory replication cohort. The proposed condition achieved 0.8717 [0.865, 0.877] accuracy, compared to 0.9065 [0.903, 0.91] for the baseline. The first negative control scored 0.908 [0.904, 0.912], and the second negative control scored 0.9088 [0.905, 0.912]. The hypothesis-positive paired contrast was -0.03482 (95% CI [-0.0422, -0.0278], paired randomisation p=0.0002, Cohen's dz=-1.41). This result is also statistically significant. The preregistered decision was that the preregistered direction was refuted. Figure 3 and Figure 4 corroborate the primary cohort findings, showing consistent underperformance of the proposed condition across both blocks. The negative controls performed comparably to the baseline, suggesting the degradation is specific to the entropy maximization objective rather than noise injection generally. Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

These results refute the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data. Both primary and replication cohorts demonstrated statistically significant accuracy degradation relative to the deterministic baseline. This finding contrasts with prior work suggesting entropy-related mechanisms aid robustness. Specifically, node-based BNNs improve uncertainty estimation under covariate shift due to input perturbations by increasing the entropy of latent variables [3]. However, our results indicate this mechanism does not translate to multiplicative weight noise in Transformers. The distinction may lie in the locus of uncertainty: node-based methods perturb activations, whereas our operator perturbs weights. Weight noise injection has been shown to improve noise resistance in diffractive networks [6], but our data suggests this does not hold for subject-disjoint generalization in attention models. The negative controls performed equivalently to the baseline, indicating that the presence of noise itself was not the cause of failure. Rather, the entropy maximization objective actively harmed optimization. This aligns with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift, though our result is specific to the entropy objective rather than inference approximation generally. The results suggest that maximizing entropy of weight distributions conflicts with the gradient descent dynamics required to fit the signal in this dataset. While Bayesian approaches theoretically avoid overfitting [7], the explicit entropy term may have prevented the model from settling into a sharp minimum necessary for high accuracy on this task. Relating back to the literature, our findings contradict the implication that diversity of implicit corruptions depends on entropy in a way that benefits all architectures [3]. The subject-disjoint shift in UCI HAR may differ fundamentally from the input corruptions evaluated in prior node-based work [3]. Consequently, practitioners should not prioritize entropy maximization for robustness tasks over standard regularization in this domain. The study validates the need for architecture-specific robustness mechanisms rather than ass[redacted]g transferability from node-based or optical network results [6].

## 7. Limitations

This study has several limitations. First, we report held-out classification accuracy only and do not include calibration metrics. While the introduction frames the study around robustness regularization, the absence of uncertainty quantification metrics limits claims about the quality of the uncertainty estimates themselves. Second, the experiment is limited to a single dataset (UCI HAR) and a specific Transformer architecture. Generalization to other time-series domains or larger models remains unverified. Third, the entropy maximization coefficient was fixed; adaptive scheduling might yield different results. Finally, the subject-disjoint split, while rigorous, represents one type of distribution shift; performance under other shift types (e.g., sensor drift) is unknown. These limitations suggest future work should explore calibration metrics and diverse architectures before ruling out entropy-based regularization entirely. Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.0125098 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

This preregistered study evaluated Entropy-Maximized Multiplicative Weight Noise for subject-disjoint robustness in Transformers. Using real data from the UCI HAR dataset across primary and replication cohorts, we found that the intervention significantly reduced held-out classification accuracy compared to deterministic training. The preregistered hypothesis was refuted in both blocks. These results indicate that explicit entropy maximization of weight noise parameters is not a viable strategy for improving robustness in this setting. Future work should investigate alternative regularization methods that do not conflict with optimization dynamics in attention-based architectures.

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
2. Tom Charnock, Laurence Perreault-Levasseur, François Lanusse Bayesian Neural Networks (2020). 2006.01490
3. Trung Trinh, Markus Heinonen, Luigi Acerbi et al. Tackling covariate shift with node-based Bayesian neural networks (2022). 2206.02435
4. Sergey Ioffe, Christian Szegedy Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (2015). 10.48550/arxiv.1502.03167
5. Laurent Valentin Jospin, Hamid Laga, Farid Boussaïd et al. Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users (2022). 10.1109/mci.2022.3155327
6. Jiashuo Shi A Diffractive Neural Network with Weight-Noise-Injection Training (2020). 2006.04462
7. José Miguel Hernández-Lobato, Ryan P. Adams Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks (2015). 10.48550/arxiv.1502.05336

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

All results were produced by an automated pipeline running the experiment on containerised GPU compute. This study was preregistered before the experiment ran: the hypothesis, the predicted direction, the metrics, and the analysis plan (statistics + seeds) were fixed in advance and committed to the artifact repository (PREREGISTRATION.md). The experiment ran over 43 preregistered primary seeds and 43 disjoint confirmatory-replication seeds; the seed identities are listed in the appendix. Slurm job id: 15540577. Container image: pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755. Walltime: 01:30:00. The exact code, container reference, seeds, run logs, Slurm job id, and the agent's full reasoning trace (including failed attempts) are in the artifact repository: https://github.com/ABS-gmbh/ai-research-journal-papers.

## Ethics

This is a small-scale computational study on publicly released data used under its published licence: uci_har_smartphones (CC BY 4.0). The data are publicly released, de-identified recordings of human volunteers collected and consented under the original data collection; no personal identifiers were accessed and no new data were collected from human subjects for this study. It poses no foreseeable ethical or dual-use risks. Compute use was deliberately minimal.
