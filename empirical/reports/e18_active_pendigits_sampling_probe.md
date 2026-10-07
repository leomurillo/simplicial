# E18 Active PenDigits Sampling Probe

- timestamp: `2026-06-04T03:10:29.149677+00:00`
- dataset: `UCI Pen-Based Recognition of Handwritten Digits`
- dataset URL: `https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits`
- train/calibration/test: `5620` / `1874` / `3498`
- early/gate/full points: `2` / `[4, 5, 6]` / `8`
- observation cost: `0.025`
- alpha: `0.05`
- finding: **ACTIVE_HYBRID_SAMPLING_GATE_NEEDED**

## Claim Tested

E18 turns E17 into an active decision problem. At an early trajectory
prefix, the agent can commit now or pay to request more of the stroke.
The probe separates graded sampling value from safe commit admission.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous sampling RMSE | 0.077 |
| gate sampling RMSE | 0.082 |
| governed sampling RMSE | 0.077 |
| hybrid sampling RMSE | 0.046 |
| continuous commit RMSE | 0.409 |
| gate commit RMSE | 0.438 |
| governed commit RMSE | 0.408 |
| hybrid commit RMSE | 0.293 |
| continuous false commit | 0.074 |
| gate false commit | 0.045 |
| governed false commit | 0.076 |
| continuous commit detection | 0.376 |
| gate commit detection | 0.180 |
| continuous request detection | 0.926 |
| gate request detection | 0.955 |
| continuous bait false commit | 0.078 |
| gate bait false commit | 0.054 |
| gate threshold | 0.021 |
| bait threshold | 0.024 |

## Split Summary

| split | n | early acc | full acc | commit rate | request rate | sampling | request gain | gate score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| train | 5620 | 0.477 | 0.879 | 0.270 | 0.730 | 0.555 | 0.014 | 0.010 |
| calibration | 1874 | 0.475 | 0.878 | 0.280 | 0.720 | 0.553 | 0.013 | 0.010 |
| test | 3498 | 0.457 | 0.820 | 0.324 | 0.676 | 0.542 | 0.011 | 0.010 |

## Model Summary

| model | sampling RMSE | sampling R2 | commit RMSE | commit acc | commit detect | false commit | request detect | bait false | bait n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar | 0.085 | 0.033 | 0.455 | 0.688 | 0.047 | 0.005 | 0.995 | 0.017 | 702 |
| continuous_sampling | 0.077 | 0.212 | 0.409 | 0.748 | 0.376 | 0.074 | 0.926 | 0.078 | 702 |
| temporal_commit_gate | 0.082 | 0.097 | 0.438 | 0.704 | 0.180 | 0.045 | 0.955 | 0.054 | 702 |
| governed_sampling | 0.077 | 0.214 | 0.408 | 0.747 | 0.378 | 0.076 | 0.924 | 0.085 | 702 |
| hybrid_full | 0.046 | 0.719 | 0.293 | 0.878 | 0.731 | 0.052 | 0.948 | 0.058 | 702 |

## Cost Sweep

| cost | commit rate | request rate | sampling winner | commit winner | cont sampling | gate sampling | cont false commit | gate false commit | cont commit detect | gate commit detect | cont bait false | gate bait false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.043 | 0.957 | hybrid_full | hybrid_full | 0.078 | 0.083 | 0.002 | 0.000 | 0.033 | 0.000 | 0.003 | 0.000 |
| 0.010 | 0.143 | 0.857 | hybrid_full | hybrid_full | 0.077 | 0.083 | 0.013 | 0.000 | 0.062 | 0.000 | 0.014 | 0.000 |
| 0.025 | 0.324 | 0.676 | hybrid_full | hybrid_full | 0.077 | 0.082 | 0.074 | 0.045 | 0.376 | 0.180 | 0.078 | 0.054 |
| 0.050 | 0.727 | 0.273 | hybrid_full | hybrid_full | 0.076 | 0.082 | 0.482 | 0.711 | 0.840 | 0.903 | 0.562 | 0.576 |
| 0.100 | 1.000 | 0.000 | hybrid_full | scalar | 0.075 | 0.083 | 1.000 | 1.000 | 1.000 | 1.000 | nan | nan |

## Interpretation

The governed/hybrid active policy is needed. The pure gate does not
win alone, but persistence improves commit control when combined
with early sampling evidence.

## Anti-Tautology Checks

- the dataset is external pen-trajectory digit data;
- early evidence uses only the first trajectory points;
- requesting more has an explicit cost, so the target is not always-sample;
- the gate is label-free and uses middle trajectory persistence;
- the commit target is evaluated from early utility versus full-trajectory utility;
- calibration thresholds are estimated on calibration examples and scored on the held-out test file;
- the cost sweep tests whether the active result depends on the sampling cost.
