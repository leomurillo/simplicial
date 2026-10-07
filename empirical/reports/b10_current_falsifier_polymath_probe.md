# B10 Current Falsifier Polymath Probe

- timestamp: `2026-06-03T22:16:24.118890+00:00`
- seed: `20260603`
- main bucket mix: `0.5`
- route/null trials: `900` / `450`
- alpha: `0.05`
- finding: **FLOW_FITS_BUT_GATE_GOVERNS_FALSE_ADMISSION**

## Claim Tested

B10 asks whether the current bucket survives a fair continuous
solenoidal rival. The synthetic generator can be smooth-flow,
discrete-gate, or mixed. If the model-selection result always favors
the bucket, the experiment is suspicious. If the winner changes with
the generating world, the probe is doing real falsifier work.

## Main Decision Quantities

| quantity | value |
|---|---|
| continuous RMSE | 0.378 |
| bucket RMSE | 0.467 |
| governed flow-gate RMSE | 0.467 |
| hybrid RMSE | 0.377 |
| hybrid gain over continuous | 0.000 |
| bucket penalty vs continuous | 0.089 |
| bucket null false action | 0.036 |
| continuous null false action | 0.358 |
| governed null false action | 0.036 |
| conformal current gate | 0.200 |

## Main Model Summary

| model | RMSE observed | RMSE clean | R2 observed | route acc | null false action |
|---|---|---|---|---|---|
| scalar | 0.613 | 0.607 | 0.000 | 0.511 | 0.000 |
| symmetric | 0.613 | 0.607 | 0.000 | 0.511 | 0.000 |
| continuous_solenoidal | 0.378 | 0.368 | 0.620 | 0.696 | 0.358 |
| bucket_current | 0.467 | 0.458 | 0.419 | 0.693 | 0.036 |
| governed_flow_gate | 0.467 | 0.458 | 0.419 | 0.693 | 0.036 |
| hybrid_flow_gate | 0.377 | 0.368 | 0.621 | 0.699 | 0.349 |

## Source-Level Summary

| source | model | RMSE observed | route acc | action rate pred |
|---|---|---|---|---|
| bucket_world | scalar | 0.730 | 0.481 | 0.000 |
| bucket_world | symmetric | 0.730 | 0.481 | 0.000 |
| bucket_world | continuous_solenoidal | 0.415 | 0.733 | 0.703 |
| bucket_world | bucket_current | 0.521 | 0.739 | 0.321 |
| bucket_world | governed_flow_gate | 0.521 | 0.739 | 0.321 |
| bucket_world | hybrid_flow_gate | 0.414 | 0.735 | 0.694 |
| continuous_world | scalar | 0.766 | 0.057 | 0.000 |
| continuous_world | symmetric | 0.766 | 0.057 | 0.000 |
| continuous_world | continuous_solenoidal | 0.416 | 0.714 | 0.699 |
| continuous_world | bucket_current | 0.592 | 0.378 | 0.321 |
| continuous_world | governed_flow_gate | 0.598 | 0.378 | 0.321 |
| continuous_world | hybrid_flow_gate | 0.418 | 0.712 | 0.692 |
| null_world | scalar | 0.076 | 1.000 | 0.000 |
| null_world | symmetric | 0.076 | 1.000 | 0.000 |
| null_world | continuous_solenoidal | 0.289 | 0.642 | 0.358 |
| null_world | bucket_current | 0.175 | 0.964 | 0.036 |
| null_world | governed_flow_gate | 0.157 | 0.964 | 0.036 |
| null_world | hybrid_flow_gate | 0.284 | 0.651 | 0.349 |

## Main Test Means

| source | mean strength | mean abs target | scalar | symmetric | abs current_hat | length |
|---|---|---|---|---|---|---|
| bucket_world | 0.146 | 0.519 | 1.092 | 0.720 | 0.159 | 96.742 |
| continuous_world | 0.146 | 0.729 | 1.092 | 0.721 | 0.154 | 97.582 |
| null_world | 0.000 | 0.000 | 1.092 | 0.720 | 0.075 | 97.000 |

## Phase Sweep

| bucket mix | winner | continuous RMSE | bucket RMSE | governed RMSE | hybrid RMSE | hybrid gain | bucket penalty | bucket null FA |
|---|---|---|---|---|---|---|---|---|
| 0.000 | continuous_solenoidal | 0.351 | 0.462 | 0.465 | 0.351 | -0.000 | 0.111 | 0.034 |
| 0.250 | hybrid_flow_gate | 0.368 | 0.454 | 0.456 | 0.367 | 0.001 | 0.086 | 0.040 |
| 0.500 | continuous_solenoidal | 0.365 | 0.468 | 0.467 | 0.365 | -0.000 | 0.103 | 0.026 |
| 0.750 | hybrid_flow_gate | 0.373 | 0.420 | 0.418 | 0.367 | 0.006 | 0.047 | 0.046 |
| 1.000 | hybrid_flow_gate | 0.354 | 0.381 | 0.366 | 0.346 | 0.008 | 0.027 | 0.060 |

## Interpretation

The continuous solenoidal rival fits directional vigor better,
but it produces too many false actions on null worlds. The
bucket gate does not win magnitude prediction; it wins admission
control. B10 therefore supports a governed-flow hypothesis:
continuous temporal current supplies the variable, while a
conformal-style gate decides when the current is actionable.

## Anti-Tautology Checks

- the continuous rival receives signed current magnitude and precision;
- the bucket model receives only a conformal admission gate and sign;
- null worlds calibrate false current admission;
- the phase sweep includes worlds where the bucket should lose;
- the reported finding can weaken, not only confirm, the B-series.
