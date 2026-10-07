# B4 Curvature Versus Closure Probe

- timestamp: `2026-06-03T20:10:07.167674+00:00`
- seed: `20260603`
- trials per kind: `260`
- calibration episodes: `900`
- evidence train/test: `72` / `72`
- latent coordinates: `6`
- noise scale: `0.35`
- alpha: `0.05`

## Claim Tested

B4-E1 asks whether a brain-like prediction-error router distinguishes a bad
chart from a missing packet. Chart episodes are one-coordinate nonlinear warps.
Packet episodes are true cross-coordinate interactions. Scalar residual energy
is matched by construction.

## Conformal Null Thresholds

| score | threshold |
|---|---|
| alpha | 0.050 |
| scalar | 1.000 |
| retained | 0.028 |
| chart | 0.066 |
| all_packet | 0.067 |
| cross_packet | 0.062 |
| route | 0.076 |
| family_gate | 1.788 |
| fixed_gain | 0.120 |

## Agent Summary

| agent | routing accuracy | noise false admission | retained success | chart success | packet success | chart as fake closure |
|---|---|---|---|---|---|---|
| scalar | 0.263 | 0.023 | 0.073 | 0.000 | 0.000 | 0.000 |
| retained_only | 0.500 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 |
| chart_only_reparameterizer | 0.493 | 0.004 | 0.000 | 0.977 | 0.000 | 0.000 |
| packet_only_closure | 0.500 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 |
| post_cbs_bucket | 0.993 | 0.004 | 1.000 | 0.977 | 1.000 | 0.008 |
| t18_conformal_bucket | 0.990 | 0.015 | 1.000 | 0.977 | 1.000 | 0.008 |

## Accuracy by Episode Kind

| kind | true op | scalar | retained only | chart only | packet only | post-CBS bucket | T18 conformal bucket |
|---|---|---|---|---|---|---|---|
| retained | reweight | 0.073 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 |
| chart | rechart | 0.000 | 0.000 | 0.977 | 0.000 | 0.977 | 0.977 |
| packet | close | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| noise | suppress | 0.977 | 1.000 | 0.996 | 1.000 | 0.996 | 0.985 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_non_noise_vs_noise | 0.530 |
| retained_gain_retained_vs_noise | 1.000 |
| chart_gain_chart_vs_noise | 0.990 |
| cross_packet_gain_packet_vs_noise | 1.000 |
| chart_gain_chart_vs_packet | 0.989 |
| cross_packet_gain_packet_vs_chart | 1.000 |
| all_packet_gain_chart_or_packet_vs_noise | 1.000 |

## Mean Scores by Kind

| kind | scalar | retained | chart | all packet | self packet | cross packet | chart minus cross |
|---|---|---|---|---|---|---|---|
| retained | 1.000 | 0.884 | 0.026 | 0.064 | 0.029 | 0.053 | -0.028 |
| chart | 1.000 | -0.148 | 0.803 | 0.555 | 0.555 | 0.082 | 0.721 |
| packet | 1.000 | -0.137 | 0.026 | 0.892 | 0.031 | 0.892 | -0.866 |
| noise | 1.000 | -0.096 | 0.014 | 0.033 | 0.017 | 0.028 | -0.014 |

## Pass Checks

| check | result |
|---|---|
| scalar_surprise_matched | pass |
| scalar_fails_routing | pass |
| packet_only_overcloses_chart | pass |
| chart_only_fails_packet | pass |
| post_cbs_separates_chart_packet | pass |
| conformal_separates_chart_packet | pass |
| conformal_false_admission_controlled | pass |

Overall: **PASS**

## Interpretation

This is a pass if scalar surprise stays matched, packet-only closure mistakes
chart curvature for a fake packet, chart-only routing fails true packets, and
the bucket routers separate rechart from close while T18 conformal gating keeps
noise admission below alpha.

This would falsify the curvature bucket if closure alone separated the cases,
or if chart and packet evidence collapsed under matched surprise.
