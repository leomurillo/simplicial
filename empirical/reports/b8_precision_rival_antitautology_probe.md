# B8 Precision-Rival Anti-Tautology Probe

- timestamp: `2026-06-03T21:55:03.412090+00:00`
- seed: `20260603`
- trials per kind: `260`
- calibration trials per kind: `260`
- evidence train/test: `96` / `96`
- distractors per episode: `16`
- lookup keys: `48`
- noise scale: `0.35`
- alpha: `0.05`
- finding: **RIVAL_MATCH_BUCKET_NOT_UNIQUE**

## Claim Tested

B8 asks whether the B-series bucket router still has unique operational bite
after semantic channel labels are removed. Agents see shuffled candidate
affordances, held-out predictive gains, costs, and governance ports. They do
not receive the true episode bucket.

## Costs

| port | cost |
|---|---|
| retained | 0.030 |
| internal | 0.080 |
| active | 0.140 |
| external | 0.160 |
| forbidden | 0.060 |

## Conformal / Precision Thresholds

| threshold | value |
|---|---|
| scalar | 1.000 |
| aggregate_precision | -0.629 |
| train_precision_value | 0.919 |
| family_margin | 0.023 |

| port | value threshold |
|---|---|
| retained | 0.001 |
| internal | -0.046 |
| active | -0.106 |
| external | -0.121 |
| forbidden | -0.025 |

## Agent Summary

| agent | routing accuracy | noise false admission | reweight | close | act | externalize | inhibit |
|---|---|---|---|---|---|---|---|
| scalar | 0.167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| train_precision | 0.163 | 0.054 | 0.000 | 0.031 | 0.000 | 0.000 | 0.000 |
| full_precision_matrix | 0.189 | 0.042 | 0.092 | 0.085 | 0.000 | 0.000 | 0.000 |
| precision_active_inference | 0.967 | 0.062 | 1.000 | 0.904 | 1.000 | 1.000 | 0.958 |
| bucket_router_unlabeled | 0.995 | 0.027 | 1.000 | 1.000 | 1.000 | 1.000 | 0.996 |
| oracle | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

## Accuracy by Episode Kind

| kind | true op | scalar | train precision | full precision matrix | precision active inference | bucket router unlabeled | oracle |
|---|---|---|---|---|---|---|---|
| retained | reweight | 0.000 | 0.000 | 0.092 | 1.000 | 1.000 | 1.000 |
| packet | close | 0.000 | 0.031 | 0.085 | 0.904 | 1.000 | 1.000 |
| action | act | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| tool | externalize | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| forbidden | inhibit | 0.000 | 0.000 | 0.000 | 0.958 | 0.996 | 1.000 |
| noise | suppress | 1.000 | 0.946 | 0.958 | 0.938 | 0.973 | 1.000 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_non_noise_vs_noise | 0.350 |
| aggregate_precision_non_noise_vs_noise | 0.589 |
| best_heldout_non_noise_vs_noise | 1.000 |
| train_bait_train_vs_heldout | 0.509 |

## Mean Scores by Kind

| kind | scalar | aggregate precision | best heldout | bait train | bait heldout |
|---|---|---|---|---|---|
| retained | 1.000 | -0.922 | 0.893 | 0.998 | -0.994 |
| packet | 1.000 | -0.919 | 0.893 | 0.998 | -0.986 |
| action | 1.000 | -0.944 | 0.892 | 0.998 | -1.017 |
| tool | 1.000 | -0.933 | 0.894 | 0.998 | -1.005 |
| forbidden | 1.000 | -0.923 | 0.892 | 0.998 | -0.995 |
| noise | 1.000 | -0.993 | 0.025 | 0.998 | -0.992 |

## Cost Sweep

| cost multiplier | precision active acc | bucket acc | precision active noise FA | bucket noise FA |
|---|---|---|---|---|
| 0.000 | 0.974 | 0.995 | 0.150 | 0.027 |
| 0.500 | 0.969 | 0.995 | 0.108 | 0.027 |
| 1.000 | 0.967 | 0.995 | 0.062 | 0.027 |
| 1.500 | 0.963 | 0.995 | 0.046 | 0.027 |
| 2.000 | 0.962 | 0.995 | 0.042 | 0.027 |
| 3.000 | 0.962 | 0.995 | 0.042 | 0.027 |

## Anti-Tautology Checks

| check | result |
|---|---|
| semantic_labels_removed | yes |
| train_bait_penalizes_train_precision | yes |
| scalar_still_blind | yes |
| continuous_rival_matches_bucket | yes |
| bucket_uniqueness_not_established | yes |
| bucket_controls_noise | yes |

## Interpretation

The key quantity is not whether the bucket router scores well. The key quantity
is whether it beats a continuous precision-active rival once labels are removed.

Here, **RIVAL_MATCH_BUCKET_NOT_UNIQUE**. If the precision-active rival matches the
unlabeled bucket router, B8 does not support bucket uniqueness. It supports the
weaker and safer claim that bucket language is an operational discretization of
a continuous precision/cost control problem.

This is exactly the uncomfortable outcome B8 was built to detect.
