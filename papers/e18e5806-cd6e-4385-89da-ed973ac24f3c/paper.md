# Entropy-Maximized Multiplicative Weight Noise for Subject-Disjoint Robustness

> 🤖 **AI-generated.** This paper — its topic, literature review, experiment code, execution, analysis, and text — was generated end to end by an autonomous AI research system. All content is AI-generated and is explicitly labelled as such.

**Keywords:** Bayesian Neural Networks, Covariate Shift, Weight Noise, Entropy Regularization, Transformer Robustness

**Model credits:** coding: qwen3.5-397b-a17b, review: qwen3.5-122b-a10b, writing: qwen3.5-397b-a17b, ideation: qwen3.5-397b-a17b

## Abstract

This study investigates whether explicit entropy maximization of weight uncertainty parameters during training improves out-of-distribution accuracy on subject-disjoint time-series data compared to standard deterministic training. We implemented an EntropyMaxWeightNoise module within a PreNormTransformerEncoder and evaluated performance on the UCI Human Activity Recognition Using Smartphones dataset, utilizing the official subject-disjoint split. Training proceeded for 12 epochs across 43 primary seeds and 43 confirmatory replication seeds. The preregistered hypothesis predicted that the intervention would yield higher held-out classification accuracy than the baseline, exceeding a fixed margin of 0.0125098. In the primary cohort, the intervention worsened the hypothesis-positive contrast by 0.04805 (95% CI [-0.0714, -0.0324], p=0.0002, Cohen's dz=-0.72). In the confirmatory replication cohort, the intervention worsened the contrast by 0.03482 (95% CI [-0.0422, -0.0278], p=0.0002, Cohen's dz=-1.41). Both cohorts resulted in a preregistered decision of direction_refuted. These findings suggest that entropy maximization of multiplicative weight noise does not generalize to attention-based architectures under distribution shift in this setting, contradicting promises of improved generalization in prior Bayesian neural network literature.

## 1. Introduction

Confidence in neural network predictions is increasingly important as models deploy in real-world applications, yet basic neural networks do not deliver certainty estimates [3]. Deep learning methods often operate as black boxes where uncertainty is challenging to quantify, though Bayesian statistics offer a formalism to address this [12]. Specifically, neural networks intrinsically increase uncertainty about which features of the analysis are model-related and which are due to the network itself [5]. While uncertainty evaluation is core for detecting uncertain data in practical applications [4], standard backpropagation retains disadvantages such as a lack of calibrated probabilistic predictions [17].

This work addresses whether uncertainty-inducing mechanisms optimized for diversity (entropy maximization) rather than posterior fidelity (KL minimization) generalize to attention-based architectures under distribution shift. While prior work explores weight noise injection and Bayesian uncertainty separately, no study explicitly maximizes the entropy of multiplicative weight noise distributions to improve subject-disjoint generalization in Transformers against standard variational objectives that minimize divergence. Validating or refuting this mechanism guides whether practitioners should prioritize entropy maximization for robustness tasks over standard regularization. We preregistered the hypothesis that the intervention would yield higher held-out classification accuracy than the comparator, with a mean hypothesis-positive paired contrast exceeding 0.0125098. We report the results of the executed experiment honestly against this prediction.

## 2. Related Work

Research into uncertainty quantification establishes that confidence in neural network predictions is increasingly important, yet *A survey of uncertainty in deep neural networks* notes that basic neural networks do not deliver this confidence [3]. *Hands-On Bayesian Neural Networks—A Tutorial for Deep Learning Users* describes deep learning methods as black boxes where uncertainty is challenging to quantify, stating that Bayesian statistics offer a formalism to address this [12]. *Bayesian Neural Networks* observes that neural networks intrinsically increase uncertainty about which features of the analysis are model-related and which are due to the neural network [5]. *Uncertainty propagation for dropout-based Bayesian neural networks* emphasizes uncertainty evaluation as core for detecting uncertain data in practical applications [4], while *Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks* highlights disadvantages of standard backpropagation such as lack of calibration [17]. However, *Stochastic Weight Sharing for Bayesian Neural Networks* and *Structured Partial Stochasticity in Bayesian Neural Networks* identify constraints regarding computational requirements, convergence difficulties, and posterior modes in BNNs [7, 18], and *Bayesian Neural Networks for Macroeconomic Analysis* develops BNNs specifically for data with limited observations [16].

Regarding robustness and optimization, *Tackling covariate shift with node-based Bayesian neural networks* states BNNs promise improved generalization under covariate shift but weight-based BNNs often struggle with high computational complexity [6]. *Dangers of Bayesian Model Averaging under Covariate Shift* warns that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13], while *Pretrained Transformers Improve Out-of-Distribution Robustness* systematically measures out-of-distribution generalization for pretrained Transformers on NLP datasets [8]. *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift* addresses the change in distribution of layer inputs during training [9], and *A Diffractive Neural Network with Weight-Noise-Injection Training* proposes weight noise injection training to achieve strong robustness [15]. *Alignment Entropy Regularization* uses entropy to measure a model's uncertainty in distributing probability mass over sequences [14], and *Bayesian optimization with robust Bayesian neural networks* discusses Bayesian optimization for tuning hyperparameters of machine learning algorithms [11]. Additionally, *Precision-Dependent Breakdown of Momentum in Ill-Conditioned Linear Regression* and *Stdlib Gradient Descent Learning Rate Sweep on Synthetic Non-Linear Data* investigate convergence stability and learning rate effects in optimization [1, 2], while *1D convolutional neural networks and applications: A survey* describes CNNs as standard for various operations [10].

## 3. Method

We implemented EntropyMaxWeightNoise as a custom PyTorch module wrapping the query projection layer of a PreNormTransformerEncoder. The model architecture consisted of a Linear(9,64) input projection, learned positional embedding(128,64), and 2 transformer blocks. Each block contained LayerNorm(64), 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64), residual connections, LayerNorm(64), Linear(64,128), ReLU, Linear(128,64), and a final residual. The head comprised final LayerNorm(64), mean-pool over time, and Linear(64,6).

We evaluated performance on the UCI Human Activity Recognition Using Smartphones dataset (DOI 10.24432/C54S4K), using raw inertial signals formatted as 128-timestep windows over 9 channels. We utilized the official subject-disjoint split of 7,352 training and 2,947 held-out windows. For each seed, we initialized identical model weights. We ran 4 conditions: (1) Intervention (EntropyMax), (2) Baseline (Deterministic), (3) NegCtrl1 (EntropyMin), and (4) NegCtrl2 (FixedNoise). Training proceeded for 12 epochs with SGD. We evaluated on held-out subjects and aggregated accuracy per seed. We computed paired contrasts (Intervention - Baseline) and applied the preregistered decision rule on the Primary block, then confirmed on the Replication block.

## 4. Experimental Setup

The experiment utilized 43 seeds for the primary cohort and 43 seeds for the confirmatory replication cohort. The primary seeds were [497360171578835126, 619747419151856849, 4359311500859520721, 3900812323465083926, 1516445550462428226, 1630043136886007277, 1835401958502649079, 4224212089476219622, 2975544019134720152, 3507764674343915068, 4004663391355442268, 1509823930515868492, 3483967100743641674, 2225936250788509260, 1957754086644492888, 4154286735266072875, 3813494016017719200, 690472406820790188, 3813916678459859089, 4090465763900842853, 1844212296145829516, 3081923774287884327, 3477292413922411937, 726925812904865219, 4400454224498690158, 1309720931756809616, 3670000523134785215, 1572470746349086798, 5569990145947559, 2855297384752490100, 3166602034212987559, 4221459448664290905, 2934143650096726109, 1462463051419223747, 4363375170763905339, 3648570110071838823, 258115887333994485, 2427086170940110629, 4084426303853737760, 2996901096067535381, 2815367292871095378, 4593572677630054665, 3754669615394449950]. The confirmatory replication seeds were [460845256865125083, 168360166801404394, 4330504984584448312, 2288886165882978077, 1436023229729468928, 3075137203164680509, 1264378101010998013, 2924740817759706416, 1407030776384369816, 3476452012804091485, 413443216560218742, 3744310097398416000, 611732904494353021, 3048141337216032385, 3348171016926346274, 182544617978886718, 2236541698554417841, 316787348038406038, 2542361651984418572, 2578784020613117302, 2827919878303280846, 50058912656477012, 2277661776842494339, 4538007595258168616, 2319057271103286511, 2045154589577734854, 2155395884799988780, 4226716155317983348, 1618031700484817618, 2260344274002574536, 2384851163006458576, 926629052757699259, 3894402378906575006, 299845134544061382, 460921128077554766, 3639277473403927291, 370580726517054298, 3492117404588741396, 3679724535907974316, 808192457140985599, 4061812732870876608, 820537500989758760, 2718212184032681684]. The primary metric was held-out classification accuracy. We computed bootstrap 95% confidence intervals over seeds for all metrics. The preregistered decision rule required the mean hypothesis-positive paired contrast to exceed 0.0125098 to support the hypothesis.

Executed configuration (server-recorded): the reported run executed the calibrated testbed `uci_har_small_transformer_v1` exactly as registered:
- Data: UCI Human Activity Recognition Using Smartphones (DOI 10.24432/C54S4K; raw inertial signals, 128-timestep windows over 9 channels; official subject-disjoint split of 7,352 training and 2,947 held-out windows). This is real recorded data, not synthetic or simulated: it was downloaded, checksum-verified and staged read-only to the compute node before the job started.
  - `uci_har_smartphones` — https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip (SHA-256 c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031, 61005872 bytes, CC BY 4.0)
- Preprocessing: standardise each of the 9 inertial channels by subtracting that channel's mean and dividing by its standard deviation (floored at 1e-6) computed over the TRAINING split only, so no held-out statistic reaches training.
- Model: PreNormTransformerEncoder(Linear(9,64) + learned positional embedding(128,64); 2 blocks, each LayerNorm(64) -> 4-head self-attention over 128 timesteps with q/k/v/out Linear(64,64) -> residual -> LayerNorm(64) -> Linear(64,128) -> ReLU -> Linear(128,64) -> residual; final LayerNorm(64), mean-pool over time, Linear(64,6)).
- Training budget: 12 epochs; batch size 128; SGD(lr=0.05,momentum=0.9).
- Held-out evaluation: the official UCI HAR test split — 2,947 windows recorded from 9 subjects who appear in no training window, so the held-out cohort is subject-disjoint rather than a random row split, and is never used for training or tuning.
- Outcome: held-out classification accuracy — number of correct activity predictions / 2947 windows in the official subject-disjoint UCI HAR test split (proportion).

## 5. Results

In the primary cohort, across 4 conditions and 43 seeds, the intervention (EntropyMax) achieved a mean held-out classification accuracy of 0.8604 (95% CI [0.837, 0.877]). The baseline (Deterministic) achieved 0.9085 (95% CI [0.905, 0.912]). The negative control 1 (EntropyMin) achieved 0.9082 (95% CI [0.905, 0.911]), and negative control 2 (FixedNoise) achieved 0.909 (95% CI [0.906, 0.912]). On held-out classification accuracy, the proposed intervention worsened the hypothesis-positive contrast by 0.04805 versus the baseline (95% CI [-0.0714, -0.0324], paired randomisation p=0.0002, Cohen's dz=-0.72). This was a statistically significant difference as the 95% CI excluded zero. The preregistered decision was direction_refuted.

In the confirmatory replication cohort, across 4 conditions and 43 seeds, the intervention achieved a mean held-out classification accuracy of 0.8717 (95% CI [0.865, 0.877]). The baseline achieved 0.9065 (95% CI [0.903, 0.91]). The negative control 1 achieved 0.908 (95% CI [0.904, 0.912]), and negative control 2 achieved 0.9088 (95% CI [0.905, 0.912]). On held-out classification accuracy, the proposed intervention worsened the hypothesis-positive contrast by 0.03482 versus the baseline (95% CI [-0.0422, -0.0278], paired randomisation p=0.0002, Cohen's dz=-1.41). This was a statistically significant difference as the 95% CI excluded zero. The preregistered decision was direction_refuted. Figure 1 and Figure 3 display the final metric values per condition with 95% bootstrap confidence intervals over seeds for the primary and replication cohorts, respectively. Figure 2 and Figure 4 show the mean held-out classification accuracy over training steps for each condition.

Registered-report decision: the primary cohort was classified as **preregistered direction refuted** and the independent confirmatory replication was classified as **preregistered direction refuted** under the preregistered confidence-interval rule. These cohorts were not pooled, and this outcome is reported regardless of direction.

## 6. Discussion

The results consistently refute the hypothesis that explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data. In both primary and replication cohorts, the intervention significantly reduced held-out classification accuracy compared to deterministic training. This finding contradicts the promise noted in prior work that BNNs improve generalization under covariate shift [6]. Instead, our results align with warnings that approximate Bayesian inference considered robust can achieve poor performance under covariate shift [13].

The failure of the entropy-maximized weight noise mechanism suggests that optimizing for diversity rather than posterior fidelity may be detrimental in attention-based architectures under this specific distribution shift. While weight noise injection training has been proposed to achieve strong robustness in other contexts [15], our results indicate it does not transfer to subject-disjoint generalization in Transformers when optimized via entropy maximization. We distinguish this finding from optimization stability issues related to momentum breakdown under precision arithmetic [1]; the observed performance degradation is specific to the weight-noise mechanism rather than general convergence instability.

The negative controls (EntropyMin and FixedNoise) performed comparably to the deterministic baseline, suggesting that the performance drop is specific to the entropy maximization objective rather than noise injection per se. This extends the understanding of entropy regularization, which has been used to measure a model's uncertainty in distributing probability mass [14], by showing that maximizing this entropy in weight parameters does not yield robustness benefits in this setting. The results guide practitioners away from prioritizing entropy maximization for robustness tasks over standard regularization in similar architectures.

## 7. Limitations

This study is limited to the UCI Human Activity Recognition Using Smartphones dataset and a specific PreNormTransformerEncoder architecture. The training budget was fixed at 12 epochs, which may not reflect optimal convergence for all conditions. While we used 43 seeds per cohort to ensure statistical power, the findings may not generalize to other modalities or larger-scale transformer models. The investigation focused on subject-disjoint shifts; other forms of distribution shift may interact differently with entropy-maximized weight noise.

Declared scope. This is a preregistered, single-testbed registered report: every claim in this paper is scoped to the calibrated testbed uci_har_small_transformer_v1 and to the preregistered smallest worthwhile effect of 0.012509797746985206 proportion on held-out classification accuracy, a margin derived from the calibration's measurement noise (it reflects measurement precision, not scientific importance). Generalisation beyond this testbed and margin is explicitly out of scope and untested here.

## 8. Conclusion

We evaluated whether explicit entropy maximization of weight uncertainty parameters improves out-of-distribution accuracy on subject-disjoint time-series data. Using the UCI HAR dataset and a Transformer architecture, we found that the intervention significantly worsened held-out classification accuracy compared to deterministic training in both primary and replication cohorts. The preregistered hypothesis was refuted. These results contradict prior suggestions that Bayesian mechanisms inherently improve generalization under covariate shift and indicate that entropy maximization of weight noise is not a viable strategy for robustness in this context.

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
