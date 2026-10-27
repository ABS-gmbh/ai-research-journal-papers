# Scientific contract (SemLock)

> Compiled deterministically from the preregistered specification, the calibrated
> testbed recipe and the server-owned harness, and locked (append-only) before any
> experiment code was accepted. Every code version, repair, runtime record and analysis
> was checked against it. Findings are typed **verified**, **violated** or
> **unverified**; an unverified property is never reported as verified.

- **Invariant hash:** `51d4b1653f393324efcfeec8c68d8ddd8c69a843ea6e06504b798ddaa10fe316`
- **Contract version:** 1
- **Enforced:** yes
- **Server-owned harness:** yes

## Clauses

| id | clause | authority | statement |
| --- | --- | --- | --- |
| Q1 | Research question, hypothesis and direction | typed_registration | Test whether the intervention intervention better on 'held-out classification accuracy'; the analysed contrast is multiplied by 1 so a positive value supports the registered direction. |
| P1 | Population, dataset and model | server_bound | Units: Seeded training run drawn from Training runs of PreNormTransformerEncoder on UCI HAR with subject-disjoint split; calibrated testbed uci_har_small_transformer_v1 (recipe 94f3ad0aa281). |
| S1 | Seed identities and cohorts | typed_registration | 43 primary and 43 disjoint replication seeds, each executed exactly once per condition and never pooled. |
| S2 | Paired-seed contract and operator randomness | derived | Only the operator differs within a seed's pair; it draws randomness only from its own harness-owned stream and carries no state between runs. |
| C1 | Registered experimental conditions | server_bound | Exactly the conditions ['proposed', 'baseline_1', 'negative_control_1'], executed in both cohorts. |
| A1 | Treatment and comparator assignment | derived | Only 'proposed' receives the intervention; every baseline is the same program with the operator applying no modification. |
| N1 | Negative controls | typed_registration | Each declared control executes its registered transform: it acts, and it is neither the comparator nor the treatment under another name. |
| I1 | Intervention lifecycle | typed_registration | The proposed arm acts in exactly ['loss_term']. |
| I2 | Intervention scope (target confinement) | server_bound | The operator modifies only blocks.0.fc1.weight (and its momentum buffer or parameters it owns); nothing else it adds is trained by its terms. |
| I3 | Registered treatment constants | typed_registration | Registered magnitudes [1e-08] are part of the intervention. |
| I4 | Intervention computation | typed_registration | The operator computes the registered transform. Whether arbitrary Python realises the pseudocode is NOT machine-decidable: independent review judges it, and once code is accepted every later repair must preserve its measured behaviour on fixed probe inputs. |
| O1 | Primary outcome and metric | server_bound | The primary outcome is 'held-out classification accuracy' (proportion), analysed under the metric key 'held-out classification accuracy'. |
| E1 | Estimand and decision rule | typed_registration | Mean hypothesis-positive paired difference proposed − baseline_1 over each cohort's seeds; supported only if CI_low > 0.0125098, refuted if CI_high ≤ 0. |
| D1 | Held-out split and leakage | server_bound | Training never reads the held-out cohort; it is used only to measure the outcome. |

## Verification by checkpoint

- **design** — accepted: 7/7 essential clauses verified, 0 violated, 0 unverified.
- **execution** — accepted: 12/12 essential clauses verified, 0 violated, 0 unverified.
- **code:static** — accepted: 8/10 essential clauses verified, 0 violated, 2 unverified.
- **publication** — accepted: 8/8 essential clauses verified, 0 violated, 0 unverified.
- **code:runtime** — accepted: 8/10 essential clauses verified, 0 violated, 2 unverified.

## Not machine-verifiable (independent review only)

No deterministic method can decide these; they rest on the independent code review
and are disclosed here as residual risk:

- N1: a control implements its declared transform (independent review)
- I4: the code realises the pseudocode, axis, ordering, normalisation, safeguards and invariants (independent review)

## Changes that would require a new experiment

- which arm receives the intervention, or adding, removing or exchanging an arm [C1, A1, N1]
- the intervention target, or touching any other parameter, optimizer state or optimizer hyperparameter [I2]
- the registered lifecycle phases or the learnable-parameter mechanism [I1]
- a registered treatment constant (coefficient, scale, threshold) [I3]
- the computation of the intervention or of a negative control beyond the allowed implementation changes [I4, N1]
- the primary outcome, its metric, unit, range or desirability [O1, Q1]
- the estimand, contrast direction, worthwhile margin, interval or decision rule [E1, Q1]
- seed identities, cohorts, pairing or failure handling [S1, S2]
- the dataset, preprocessing or held-out split, or any training-time use of the held-out cohort [P1, D1]

## Implementation changes that remain allowed

- renaming variables, restructuring control flow, extracting helper functions, comments and formatting
- numerical safeguards that leave values unchanged on non-degenerate inputs (an epsilon in a denominator, clamping a value the protocol says cannot occur)
- device and dtype placement, and moving the operator's randomness between the harness-owned operator streams (ctx.rng, ctx.rand_like, ctx.randn_like) provided the drawn distribution is unchanged
- performance changes (vectorisation, caching a fixed quantity in ctx.state for the current run)
