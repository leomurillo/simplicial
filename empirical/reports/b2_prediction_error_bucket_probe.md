# B2 Prediction-Error Bucket Probe

- timestamp: `2026-06-03T18:51:47.498010+00:00`
- seed: `20260603`
- trials per kind: `240`
- calibration episodes: `800`
- evidence train/test: `64` / `64`
- alpha: `0.05`

## Claim Tested

B2's STAR says that a brain-like agent should route prediction errors by
bucket, not by scalar surprise alone. This probe constructs matched-surprise
episodes for nine true buckets and compares scalar routing, T17 gain-only
routing, post-CBS bucket routing, and T18 conformal bucket routing.

## Conformal Null Thresholds

| score | threshold |
|---|---|
| alpha | 0.050 |
| scalar | 1.000 |
| retained | 0.020 |
| chart | 0.022 |
| current | 0.025 |
| forbidden | 0.026 |
| packet | 0.061 |
| route | 0.065 |
| ledger | 0.500 |
| family_gate | 1.209 |
| raw_capacity_threshold | 0.120 |

## Agent Summary

| agent | routing accuracy | noise false admission | current success | ledger success |
|---|---|---|---|---|
| scalar | 0.112 | 0.025 | 0.000 | 0.000 |
| t17_gain | 0.212 | 0.087 | 0.000 | 0.000 |
| post_cbs_bucket | 0.955 | 0.013 | 1.000 | 1.000 |
| t18_conformal_bucket | 0.746 | 0.050 | 0.929 | 1.000 |

## Accuracy by Episode Kind

| kind | true op | scalar | T17 gain | post-CBS bucket | T18 conformal bucket |
|---|---|---|---|---|---|
| retained | reweight | 0.033 | 0.000 | 0.996 | 0.629 |
| chart | rechart | 0.000 | 0.000 | 1.000 | 0.867 |
| packet | close | 0.000 | 1.000 | 0.971 | 0.475 |
| current | predict | 0.000 | 0.000 | 1.000 | 0.929 |
| ambiguity | sample | 0.000 | 0.000 | 0.754 | 0.417 |
| capacity | compress | 0.000 | 0.000 | 0.883 | 0.567 |
| noise | suppress | 0.975 | 0.912 | 0.988 | 0.950 |
| governance | inhibit | 0.000 | 0.000 | 1.000 | 0.879 |
| ledger | recalibrate | 0.000 | 0.000 | 1.000 | 1.000 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_vs_noise | 0.494 |
| max_packet_gain_vs_noise | 0.699 |
| current_gain_current_vs_noise | 1.000 |
| ledger_shift_ledger_vs_noise | 1.000 |

## Mean Scores by Kind

| kind | scalar | retained | chart | current | packet | ledger |
|---|---|---|---|---|---|---|
| retained | 1.000 | 0.894 | -0.014 | -0.015 | 0.040 | 0.403 |
| chart | 1.000 | -0.016 | 0.894 | -0.015 | 0.024 | 0.334 |
| packet | 1.000 | -0.044 | -0.017 | -0.018 | 0.892 | 0.426 |
| current | 1.000 | -0.014 | -0.015 | 0.893 | 0.024 | 0.335 |
| ambiguity | 1.000 | -0.015 | -0.015 | -0.018 | 0.471 | 0.374 |
| capacity | 1.000 | -0.022 | -0.019 | -0.019 | 0.268 | 0.360 |
| noise | 1.000 | -0.013 | -0.015 | -0.016 | 0.026 | 0.345 |
| governance | 1.000 | -0.018 | -0.014 | -0.018 | 0.026 | 0.367 |
| ledger | 1.000 | -0.047 | -0.014 | -0.013 | 0.026 | 1.889 |

## Interpretation

This is a pass for the STAR if scalar surprise stays uninformative under
matched residual energy, T17 gain identifies structure but collapses distinct
structural operations, post-CBS features separate chart/current/packet buckets,
and T18 conformal routing keeps noise false admission near the declared alpha.

The synthetic setting is intentionally small. Its job is to expose whether the
nine buckets are operationally separable before we try to map them onto neural
recordings.
