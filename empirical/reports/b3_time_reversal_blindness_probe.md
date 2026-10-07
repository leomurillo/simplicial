# B3 Time-Reversal Blindness Probe

- timestamp: `2026-06-03T19:58:04.740478+00:00`
- seed: `20260603`
- states: `17`
- episode length: `256`
- trials per kind: `600`
- calibration trials per kind: `700`
- drift/counter/stay: `0.56` / `0.16` / `0.28`
- alpha: `0.05`

## Claim Tested

B3-E1 tests whether the current bucket is operationally distinct from scalar
surprise and symmetric boundary geometry. The forward, reverse, and null worlds
share a uniform stationary distribution and the same symmetrized transition
backbone. The only difference between forward and reverse is the sign of the
antisymmetric current.

## Conformal Current Gate

| threshold | value |
|---|---|
| alpha | 0.050 |
| current_abs_null_gate | 0.117 |
| current_abs_null_quantile | 0.975 |

## Agent Summary

| agent | direction accuracy | forward acc | reverse acc | current detection | null false admission |
|---|---|---|---|---|---|
| scalar | 0.502 | 0.410 | 0.595 | 0.420 | 0.375 |
| symmetric | 0.503 | 0.423 | 0.583 | 0.420 | 0.375 |
| unsigned_packet | 0.488 | 0.222 | 0.755 | 1.000 | 0.000 |
| current_signed | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| t18_conformal_current | 1.000 | 1.000 | 1.000 | 1.000 | 0.028 |

## Direction Classifier Fits

| agent | score | threshold | high label | train accuracy |
|---|---|---|---|---|
| scalar | scalar_score | 1.094 | 1 | 0.521 |
| symmetric | symmetric_score | 0.952 | 1 | 0.519 |
| unsigned_packet | packet_unsigned_score | 0.436 | 1 | 0.518 |
| current_signed | current_score | -0.025 | 1 | 1.000 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_current_presence | 0.527 |
| symmetric_current_presence | 0.528 |
| unsigned_packet_current_presence | 1.000 |
| current_abs_current_presence | 1.000 |
| scalar_forward_vs_reverse | 0.518 |
| symmetric_forward_vs_reverse | 0.518 |
| unsigned_packet_forward_vs_reverse | 0.495 |
| current_signed_forward_vs_reverse | 1.000 |

## Mean Scores by Kind

| kind | scalar | symmetric | unsigned packet | signed current | beta |
|---|---|---|---|---|---|
| forward | 1.092 | 0.952 | 0.400 | 0.400 | 0.145 |
| reverse | 1.092 | 0.951 | 0.400 | -0.400 | -0.145 |
| null | 1.092 | 0.951 | 0.043 | -0.002 | -0.001 |

## Mean Step Counts by Kind

| kind | forward steps | reverse steps | stay steps |
|---|---|---|---|
| forward | 143.193 | 40.667 | 72.140 |
| reverse | 40.858 | 143.360 | 71.782 |
| null | 92.073 | 92.550 | 71.377 |

## Pass Checks

| check | result |
|---|---|
| scalar_direction_blind | pass |
| symmetric_direction_blind | pass |
| unsigned_packet_direction_blind | pass |
| current_signed_recovers_arrow | pass |
| conformal_recovers_arrow | pass |
| conformal_false_current_controlled | pass |

Overall: **PASS**

## Interpretation

This is a pass if scalar and symmetric agents remain near chance on
forward-versus-reverse direction, unsigned packet evidence detects that a
current exists but cannot name its arrow, signed current recovers the arrow,
and the conformal current gate keeps detailed-balance false admission below
alpha.

This would falsify the B-series current bucket if scalar surprise, symmetric
geometry, or unsigned packet magnitude recovered the time direction as well as
the signed current statistic under these matched-backbone controls.
