# Reporting correction

Version 2. It discloses the independent reproduction: the re-run on different GPU hardware confirmed both registered inconclusive decisions, its per-seed results were not numerically identical, and its confirmatory-replication interval excludes zero. No registered result changed. This version adds a reproduction disclosure to the Limitations section, and corrects 2 sentences in the Related Work section so that each citation is attributed to the work that supports it. No other section, reference, figure or table differs from the previous version; CORRECTION.md shows every changed sentence.

Previous version: 1; commit `6e998276f94d5e3f6b99ed95d2633e9a485ac6a7`. Only the sections below changed; every other section is the published text. The original execution, analysis, preregistration and reproduction evidence are preserved.

## related_work

```diff
--- published/related_work
+++ corrected/related_work
@@ -3 +3 @@
-Specific applications include biosignal data augmentation in *TTS-CGAN: A Transformer Time-Series Conditional GAN for Biosignal Data Augmentation* and representing multivariate series as graphs in *Expressing Multivariate Time Series as Graphs with Time Series Attention Transformer* [7, 11].
+Specific applications include representing multivariate series as graphs in *Expressing Multivariate Time Series as Graphs with Time Series Attention Transformer* and biosignal data augmentation in *TTS-CGAN: A Transformer Time-Series Conditional GAN for Biosignal Data Augmentation* [7, 11].
@@ -18 +18 @@
-Surveys such as *A Survey on Vision Transformer*, *Transformers in Vision: A Survey*, and *A survey of transformers* document the application of Transformers across vision, NLP, and audio [6, 12, 21].
+Surveys such as *A Survey on Vision Transformer* [6] and *Transformers in Vision: A Survey* [12] document the application of Transformers in computer vision, while *A survey of transformers* [21] documents the application of Transformers across vision, NLP, and audio.
```

## limitations

```diff
--- published/limitations
+++ corrected/limitations
@@ -8,0 +9,10 @@
+Reproduction disclosure.
+The registered experiment ran as compute job 16678400 on one NVIDIA H100 GPU, and the independent reproduction ran as compute job 16726777 on one NVIDIA A100-SXM4-80GB GPU.
+The reproduction record verifies that the re-run used the committed replay packet, whose inputs equal the original execution's frozen code, conditions and configuration, and the same 43 primary and 43 confirmatory seed identities in registered order.
+The reproduced per-seed accuracies were not identical to the original ones: between one and three of the 43 seeds per condition and cohort gave exactly the same value.
+In the registered analysis of the original execution, the primary contrast was +0.00077 (95% CI [-0.00271, 0.00436]) and the confirmatory-replication contrast was +0.00196 (95% CI [-0.00196, 0.00571]).
+In the reproduction, the reproduced primary contrast was +0.00095 (95% CI [-0.00192, 0.00406]) and the reproduced confirmatory-replication contrast was +0.00615 (95% CI [0.00125, 0.01208]).
+The reproduced confirmatory-replication interval excludes zero; the original confirmatory-replication interval includes zero, and the statements in this paper about whether the intervals include zero describe the registered analysis of the original execution.
+The registered decision rule classifies a cohort as inconclusive unless its whole 95% interval lies above the worthwhile margin of 0.0125098 or at or below zero; both reproduced cohorts are inconclusive under this rule, the same decision as each registered cohort.
+The reproduction criterion compares each condition's mean with its published 95% interval or a 5% relative tolerance (five of six reproduced means fell inside the interval and one passed on the tolerance alone); it does not compare contrasts or decisions.
+The reproduction therefore confirms the registered decisions, not that the per-seed results are numerically reproducible across these two executions, and the cause of the numerical differences has not been determined.
```
