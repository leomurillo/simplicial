# E23 External Wall-Following Gate-Residual Probe

- timestamp: `2026-06-04T05:34:08.871943+00:00`
- dataset: `UCI Wall-Following Robot Navigation Data`
- dataset page: `https://archive-beta.ics.uci.edu/dataset/194/wall+following+robot+navigation+data`
- DOI: `https://doi.org/10.24432/C57C8W`
- rows/features: `5456` / `24`
- history/stability: `5` / `7`
- train/cal/test windows: `3270` / `1087` / `1087`
- command change rate: `0.072`
- gate threshold: `0.000`
- finding: **EXTERNAL_MLP_ABSORBS_GATE_WITH_WEAK_HYBRID_EDGE**

## Claim Tested

E23 asks whether a label-free temporal gate adds residual policy
value after a trained no-gate MLP has learned command selection
from external sequential robot sensor data.

This is an imitation/control-label benchmark, not a causal
intervention log.

## Dataset Audit

| quantity | value |
| --- | --- |
| labels | {'Move-Forward': 2205, 'Slight-Left-Turn': 328, 'Slight-Right-Turn': 826, 'Sharp-Right-Turn': 2097} |
| split bounds | {'train': [0, 3274], 'calibration': [3274, 4365], 'test': [4365, 5456]} |
| probe accuracy | {'train': 0.9113149847094801, 'calibration': 0.8610855565777369, 'test': 0.8454461821527139} |
| majority accuracy | {'train': 0.39235474006116206, 'calibration': 0.45446182152713893, 'test': 0.39006439742410304} |
| probe features | {'raw_feature_count': 241, 'expanded_feature_count': 483} |

## Main Decision Quantities

| quantity | value |
| --- | --- |
| scalar accuracy | 0.857 |
| continuous accuracy | 0.861 |
| hybrid accuracy | 0.869 |
| scalar regret | 0.176 |
| continuous regret | 0.171 |
| hybrid regret | 0.161 |
| continuous unsafe wrong | 0.091 |
| hybrid unsafe wrong | 0.086 |
| continuous boundary error | 0.069 |
| hybrid boundary error | 0.063 |
| continuous select rmse | 0.236 |
| hybrid select rmse | 0.224 |

## Split Summary

| split | episodes | packets | mean utility | mean gate | mean unsafe proxy | optimal actions |
| --- | --- | --- | --- | --- | --- | --- |
| train | 3270 | 13080 | 0.104 | 0.003 | 0.416 | Move-Forward:1283, Slight-Left-Turn:183, Slight-Right-Turn:561, Sharp-Right-Turn:1243 |
| calibration | 1087 | 4348 | 0.112 | 0.003 | 0.395 | Move-Forward:494, Slight-Left-Turn:38, Slight-Right-Turn:109, Sharp-Right-Turn:446 |
| test | 1087 | 4348 | 0.101 | 0.003 | 0.427 | Move-Forward:424, Slight-Left-Turn:107, Slight-Right-Turn:148, Sharp-Right-Turn:408 |

## Model Summary

| model | features | value RMSE | select RMSE | action acc | regret | p90 regret | unsafe wrong | boundary error | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar_mlp | 6 | 0.303 | 0.223 | 0.857 | 0.176 | 1.000 | 0.095 | 0.076 | 0.858 | 0.050 |
| continuous_mlp | 256 | 0.313 | 0.236 | 0.861 | 0.171 | 1.000 | 0.091 | 0.069 | 0.842 | 0.041 |
| hybrid_mlp | 261 | 0.309 | 0.224 | 0.869 | 0.161 | 1.000 | 0.086 | 0.063 | 0.857 | 0.034 |

## Interpretation

The hybrid MLP keeps a small edge, but the gain is below the
configured survival margins. This counts as absorption with a
weak hybrid hint rather than a gate residual.

## Anti-Tautology Checks

- the dataset is external UCI robot navigation data;
- splits are chronological, not random;
- continuous_mlp has no gate score or gate bit;
- hybrid_mlp has the same architecture plus gate features;
- the gate is calibrated on non-selected calibration command packets;
- unsafe-command is only a proxy derived from command mismatch severity;
- this is command imitation, not causal intervention evidence.
