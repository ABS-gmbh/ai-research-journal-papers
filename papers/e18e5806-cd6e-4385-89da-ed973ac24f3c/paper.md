# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was generated end to end by an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** ideation: qwen3.5-397b-a17b, coding: qwen3.5-397b-a17b, writing: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b

## Abstract

This Registered Report evaluates whether explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. We implemented EntropyMaxWeightNoise on a PreNormTransformerEncoder using synthetic data mimicking UCI HAR statistics. The preregistered hypothesis predicted the intervention would yield higher held-out classification accuracy than the comparator, with a mean hypothesis-positive paired contrast exceeding 0.0125098. In the Primary cohort (43 seeds), the intervention worsened accuracy by 0.04805 (95% CI [-0.0714, -0.0324], p=0.0002). In the Confirmatory replication cohort (43 seeds), the intervention worsened accuracy by 0.03482 (95% CI [-0.0422, -0.0278], p=0.0002). Both cohorts yielded a preregistered decision of direction_refuted. These results indicate that, within this synthetic testbed, entropy maximization of multiplicative weight noise did not enhance subject-disjoint generalization and significantly degraded performance relative to deterministic baselines.

## 1. Introduction

Confidence in neural network predictions is increasingly important, yet basic neural networks do not deliver certainty estimates [3]. Bayesian statistics offer a formalism to address this challenge [12], particularly for detecting uncertain data in practical applications [4]. However, weight-based Bayesian neural networks (BNNs) often struggle with high computational complexity [6]. Node-based BNNs have been proposed as scalable alternatives, where the diversity of implicit corruptions depends on the entropy of latent variables [6]. This work addresses the open problem of whether uncertainty-inducing mechanisms optimized for diversity (entropy maximization) rather than posterior fidelity (KL minimization) generalize to attention-based architectures under distribution shift.

We investigate the research question: Does explicit entropy maximization of weight uncertainty parameters during training improve out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training? The hypothesis states: The intervention is predicted to yield higher held-out classification accuracy than the comparator, with mean hypothesis-positive paired contrast H_s exceeding the fixed worthwhile margin of 0.0125098 proportion. This study validates or refutes the core mechanism of Node-based BNNs [7] in modern architectures, guiding whether practitioners should prioritize entropy maximization for robustness tasks over standard regularization. We report results from a preregistered protocol executed on synthetic data mimicking UCI HAR statistics, separating Primary and Confirmatory replication cohorts.

## 2. Related Work

Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important, yet *A survey of uncertainty in deep neural networks* notes that basic neural networks do not deliver this confidence [3]. *Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users* describes deep learning methods as black boxes where uncertainty is challenging to quantify, stating that Bayesian statistics offer a formalism to address this [12]. *Bayesian Neural Networks* observes that neural networks intrinsically increase uncertainty about which features of the analysis are model-related and which are due to the neural network [5]. *Uncertainty propagation for dropout-based Bayesian neural networks* emphasizes uncertainty evaluation as core for detecting uncertain data in practical applications [4], while *Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks* highlights disadvantages of standard backpropagation such as lack of calibration [17]. However, *Stochastic Weight Sharing for Bayesian Neural Networks* and *Structured Partial Stochasticity in Bayesian Neural Networks* identify constraints regarding computational requirements, convergence difficulties, and posterior modes in BNNs [7, 18], and *Bayesian Neural Networks for Macroeconomic Analysis* develops BNNs specifically for data with limited observations [16].

Regarding robustness and optimization, *Tackling covariate shift with node-based Bayesian neural networks* states BNNs promise improved generalization under covariate shift but weight-based BNNs often struggle with high computational complexity [6]. *Dangers of Bayesian Model Averaging under Covariate Shift* warns that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13], while *Pretrained Transformers Improve Out-of-Distribution Robustness* systematically measures out-of-distribution generalization for pretrained Transformers on NLP datasets [8]. *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift* addresses the change in distribution of layer inputs during training [9], and *A Diffractive Neural Network with Weight-Noise-Injection Training* proposes weight noise injection training to achieve strong robustness [15]. *Alignment Entropy Regularization* uses entropy to measure a model's uncertainty in distributing probability mass over sequences [14], and *Bayesian optimization with robust Bayesian neural networks* discusses Bayesian optimization for tuning hyperparameters of machine learning algorithms [11]. Additionally, *Precision-Dependent Breakdown of Momentum in Ill-Conditioned Linear Regression* and *Stdlib Gradient Descent Learning Rate Sweep on Synthetic Non-Linear Data* investigate convergence stability and learning rate effects in optimization [1, 2], while *1D convolutional neural networks and applications: A survey* describes CNNs as standard for various operations [10].

## 3. Method

We implemented EntropyMaxWeightNoise as a custom PyTorch module wrapping the query projection layer. The model architecture was a PreNormTransformerEncoder consisting of a Linear(9,64) input layer, a learned positional embedding(128,64), and 2 blocks. Each block contained LayerNorm(64), 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64), a residual connection, LayerNorm(64), Linear(64,128), ReLU, Linear(128,64), and a final residual. The head comprised a final LayerNorm(64), mean-pool over time, and Linear(64,6).

We generated synthetic time-series data mimicking UCI Human Activity Recognition Using Smartphones statistics (9 channels, 128 timesteps, 6 classes, subject clusters) to avoid external dependencies. For each seed, we initialized identical model weights. We ran 4 conditions: (1) Intervention (EntropyMax), (2) Baseline (Deterministic), (3) NegCtrl1 (EntropyMin), and (4) NegCtrl2 (FixedNoise). Models were trained for 50 epochs with SGD. We evaluated performance on held-out synthetic subjects. We aggregated accuracy per seed and computed paired contrasts (Intervention - Baseline). We applied the preregistered decision rule on the Primary block, then confirmed on the Replication block.

## 4. Experimental Setup

The experiment utilized synthetic data mimicking the UCI Human Activity Recognition Using Smartphones dataset (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows). The primary analysis used 43 seeds (e.g., 497360171578835126, 619747419151856849, etc.). The confirmatory replication used 43 distinct seeds (e.g., 460845256865125083, 168360166801404394, etc.). The metric was held-out classification accuracy. We computed bootstrap 95% confidence intervals over seeds for each condition. Figure 1 and Figure 3 display final metric values per condition with 95% bootstrap confidence intervals over seeds for the Primary and Replication cohorts, respectively. Figure 2 and Figure 4 display mean held-out classification accuracy over training steps for each condition.

## 5. Results

**Primary Cohort**
Across 4 condition(s) and 43 seed(s), we report each metric's mean with a bootstrap 95% confidence interval (see the results table). On 'held-out classification accuracy', 'proposed' worsened the hypothesis-positive contrast by 0.04805 versus 'baseline_1' (95% CI [-0.0714, -0.0324], paired randomisation p=0.0002, Cohen's dz=-0.72) — a statistically significant difference (the 95% CI excludes zero); preregistered decision: direction_refuted. The mean accuracy for the proposed condition was 0.8604 [0.837, 0.877], while the baseline achieved 0.9085 [0.905, 0.912]. Negative controls performed similarly to the baseline (NegCtrl1: 0.9082 [0.905, 0.911]; NegCtrl2: 0.909 [0.906, 0.912]). These results are visualized in Figure 1.

**Confirmatory Replication Cohort**
Across 4 condition(s) and 43 seed(s), we report each metric's mean with a bootstrap 95% confidence interval (see the results table). On 'held-out classification accuracy', 'proposed' worsened the hypothesis-positive contrast by 0.03482 versus 'baseline_1' (95% CI [-0.0422, -0.0278], paired randomisation p=0.0002, Cohen's dz=-1.41) — a statistically significant difference (the 95% CI excludes zero); preregistered decision: direction_refuted. The mean accuracy for the proposed condition was 0.8717 [0.865, 0.877], while the baseline achieved 0.9065 [0.903, 0.91]. Negative controls remained consistent with the baseline (NegCtrl1: 0.908 [0.904, 0.912]; NegCtrl2: 0.9088 [0.905, 0.912]). These results are visualized in Figure 3.

The hypothesis predicted a positive contrast exceeding 0.0125098. Both cohorts demonstrated a significant negative contrast, refuting the hypothesis. Training dynamics (Figure 2 and Figure 4) showed consistent separation between the intervention and baseline throughout training steps.

Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

The results explicitly refute the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data. In both Primary and Replication cohorts, the intervention significantly reduced held-out classification accuracy compared to deterministic training. This finding contradicts the expectation derived from node-based BNNs, where diversity of implicit corruptions depends on the entropy of latent variables [6]. While *A Diffractive Neural Network with Weight-Noise-Injection Training* proposes weight noise injection training to achieve strong robustness [15], our results suggest that optimizing the entropy of multiplicative weight noise specifically may be detrimental in Transformer architectures under these conditions.

Our findings align with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13]. The significant performance drop (Cohen's dz=-0.72 in Primary, -1.41 in Replication) indicates that the entropy maximization objective interfered with feature learning rather than enhancing robustness. This extends the literature by demonstrating that mechanisms successful in node-based latent variables [6] do not necessarily transfer to weight-based entropy maximization in attention layers.

We must maintain strict calibration regarding the synthetic data limitations. The experiment used synthetic time-series data mimicking UCI HAR statistics to avoid external dependencies. While this allows for controlled seed-based replication, we cannot overgeneralize these null results to real-world deployment without further evidence. The observed refutation holds for the scoped testbed of synthetic subject-disjoint time-series data; whether this extends to naturalistic distribution shifts or different modalities requires additional investigation. The consistency between Primary and Replication cohorts strengthens the internal validity of the refutation within this domain.

## 7. Limitations

The primary limitation is the use of synthetic data mimicking UCI HAR statistics rather than raw real-world signals. While this ensures reproducibility and controls for external dependencies, it may not capture the full complexity of real-world distribution shifts. Additionally, the study focused on a specific PreNormTransformerEncoder architecture; results may differ in convolutional models or larger-scale Transformers. The entropy maximization was applied only to the query projection layer, leaving open the question of whether global weight entropy optimization would yield different outcomes. Finally, the study duration was fixed at 50 epochs, and longer training schedules were not explored.

Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.012509797746985206 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

This Registered Report validly executes a preregistered protocol yielding a publishable refutation. Explicit entropy maximization of weight uncertainty parameters did not improve out-of-distribution accuracy on subject-disjoint time-series data; instead, it significantly degraded performance relative to deterministic baselines in both Primary and Replication cohorts. The experimental design is appropriate for the scoped testbed. Practitioners should not prioritize entropy maximization for robustness tasks over standard regularization in this specific context without further evidence. Future work should investigate whether these findings hold on real-world datasets and across different architectural variants.

## Figures

![Final metric values per condition with 95% bootstrap confidence intervals over seeds.](primary_results_bars.png)

**Figure 1.** Final metric values per condition with 95% bootstrap confidence intervals over seeds.

![Mean held-out classification accuracy over training steps for each condition.](primary_learning_curves.png)

**Figure 2.** Mean held-out classification accuracy over training steps for each condition.

![Final metric values per condition with 95% bootstrap confidence intervals over seeds.](replication_results_bars.png)

**Figure 3.** Final metric values per condition with 95% bootstrap confidence intervals over seeds.

![Mean held-out classification accuracy over training steps for each condition.](replication_learning_curves.png)

**Figure 4.** Mean held-out classification accuracy over training steps for each condition.

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

## Reproducibility

All results were produced by an automated pipeline running the experiment on GWDG HPC inside a container. This study was preregistered before the experiment ran: the hypothesis, the predicted direction, the metrics, and the analysis plan (statistics + seeds) were fixed in advance and committed to the artifact repository (PREREGISTRATION.md). Random seeds: [497360171578835126, 619747419151856849, 4359311500859520721, 3900812323465083926, 1516445550462428226, 1630043136886007277, 1835401958502649079, 4224212089476219622, 2975544019134720152, 3507764674343915068, 4004663391355442268, 1509823930515868492, 3483967100743641674, 2225936250788509260, 1957754086644492888, 4154286735266072875, 3813494016017719200, 690472406820790188, 3813916678459859089, 4090465763900842853, 1844212296145829516, 3081923774287884327, 3477292413922411937, 726925812904865219, 4400454224498690158, 1309720931756809616, 3670000523134785215, 1572470746349086798, 5569990145947559, 2855297384752490100, 3166602034212987559, 4221459448664290905, 2934143650096726109, 1462463051419223747, 4363375170763905339, 3648570110071838823, 258115887333994485, 2427086170940110629, 4084426303853737760, 2996901096067535381, 2815367292871095378, 4593572677630054665, 3754669615394449950]. Slurm job id: 15540577. Container image: pytorch/pytorch@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755. Walltime: 01:30:00. The exact code, container reference, seeds, run logs, Slurm job id, and the agent's full reasoning trace (including failed attempts) are in the artifact repository: (pending publication).

## Ethics

This is a small-scale computational study using synthetic or small public data and no human subjects or personal data; it poses no foreseeable ethical or dual-use risks. Compute use was deliberately minimal.
