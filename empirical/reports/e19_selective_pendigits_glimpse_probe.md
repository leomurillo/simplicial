# E19 Selective PenDigits Glimpse Probe

- timestamp: `2026-06-04T04:29:56.624627+00:00`
- dataset: `UCI Pen-Based Recognition of Handwritten Digits`
- dataset URL: `https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits`
- train/calibration/test: `5620` / `1874` / `3498`
- early points: `2`
- actions: `['commit', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']`
- base/distance cost: `0.01` / `0.003`
- alpha: `0.05`
- finding: **SELECTIVE_SAMPLING_CONTINUOUS_ACTION_VALUE_ABSORBS_GATE**

## Claim Tested

E19 moves from request-more to choose-where-to-sample. Each action
packet is either commit now or inspect one future trajectory point.
The model must pick one action per trajectory, so policy regret is the
main score.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous value RMSE | 0.017 |
| gate value RMSE | 0.018 |
| governed value RMSE | 0.017 |
| hybrid value RMSE | 0.016 |
| continuous action accuracy | 0.822 |
| gate action accuracy | 0.523 |
| governed action accuracy | 0.826 |
| hybrid action accuracy | 0.829 |
| continuous regret | 0.001 |
| gate regret | 0.003 |
| governed regret | 0.001 |
| hybrid regret | 0.001 |
| continuous false commit | 0.069 |
| gate false commit | 0.477 |
| hybrid false commit | 0.063 |
| continuous wrong sample | 0.036 |
| gate wrong sample | 0.000 |
| hybrid wrong sample | 0.039 |
| gate threshold | 0.003 |

## Split Summary

| split | episodes | packets | mean utility | mean gate | optimal actions |
| --- | --- | --- | --- | --- | --- |
| train | 5620 | 39340 | 0.107 | 0.001 | commit:2818, p3:1018, p4:327, p5:578, p6:348, p7:125, p8:406 |
| calibration | 1874 | 13118 | 0.107 | 0.001 | commit:933, p3:341, p4:107, p5:195, p6:122, p7:55, p8:121 |
| test | 3498 | 24486 | 0.105 | 0.001 | commit:1829, p3:576, p4:157, p5:418, p6:183, p7:81, p8:254 |

## Model Summary

| model | value RMSE | value R2 | action acc | regret | p90 regret | false commit | false sample | wrong sample | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar | 0.016 | 0.367 | 0.523 | 0.003 | 0.011 | 0.477 | 0.000 | 0.000 | 0.300 | 0.032 |
| continuous_action_value | 0.017 | 0.220 | 0.822 | 0.001 | 0.002 | 0.069 | 0.073 | 0.036 | 0.732 | 0.032 |
| conformal_action_gate | 0.018 | 0.209 | 0.523 | 0.003 | 0.011 | 0.477 | 0.000 | 0.000 | 0.011 | 0.000 |
| governed_action | 0.017 | 0.272 | 0.826 | 0.001 | 0.002 | 0.064 | 0.070 | 0.040 | 0.736 | 0.031 |
| hybrid_full | 0.016 | 0.314 | 0.829 | 0.001 | 0.002 | 0.063 | 0.069 | 0.039 | 0.738 | 0.031 |

## Cost Sweep

| base cost | optimal actions | cont acc | gate acc | hybrid acc | cont regret | gate regret | hybrid regret | cont false commit | gate false commit | hybrid false commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | commit:509, p3:894, p4:401, p5:750, p6:417, p7:121, p8:406 | 0.755 | 0.321 | 0.758 | 0.002 | 0.006 | 0.002 | 0.040 | 0.000 | 0.046 |
| 0.005 | commit:1022, p3:772, p4:247, p5:602, p6:369, p7:102, p8:384 | 0.777 | 0.395 | 0.783 | 0.002 | 0.005 | 0.002 | 0.054 | 0.572 | 0.059 |
| 0.010 | commit:1829, p3:576, p4:157, p5:418, p6:183, p7:81, p8:254 | 0.822 | 0.523 | 0.829 | 0.001 | 0.003 | 0.001 | 0.069 | 0.477 | 0.063 |
| 0.020 | commit:3061, p3:145, p4:105, p5:74, p6:32, p7:20, p8:61 | 0.912 | 0.875 | 0.914 | 0.000 | 0.001 | 0.000 | 0.079 | 0.125 | 0.074 |
| 0.040 | commit:3496, p3:0, p4:2, p5:0, p6:0, p7:0, p8:0 | 0.999 | 0.999 | 0.998 | 0.000 | 0.000 | 0.000 | 0.001 | 0.001 | 0.001 |

## Interpretation

The continuous action-value policy absorbs the action gate on this
selective-sampling proxy. That would make E19 a negative anchor
for the governance claim.

## Anti-Tautology Checks

- the dataset is external pen-trajectory digit data;
- the agent sees only the first two trajectory points before action packets;
- each sample action exposes a different future point, so action changes which evidence arrives;
- action utility is computed from true-label support minus action cost;
- the conformal gate is calibrated on non-optimal action packets;
- policy metrics choose one action per held-out trajectory and score regret;
- the cost sweep tests whether the result depends on sampling cost.
