# T19 Minimal Conscious Agent Experiment

- timestamp: `2026-05-27T05:04:19.192449+00:00`
- seed: `1901`
- alpha: `0.05`
- closure cost: `0.0`
- action cost: `0.05`

## Claim Tested

Scalar surprise is matched between structural and noise episodes, but only structural episodes contain a stable boundary packet that should enter the conscious content set.

## Results

| d | evidence | scalar AUC | boundary AUC | gain AUC | structural gain | noise gain | T19 TPR | T19 FPR | T19 structural reward | T19 noise reward |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 8 | 0.496 | 0.762 | 0.992 | 1.252 | -0.563 | 0.984 | 0.059 | 0.938 | 0.495 |
| 16 | 16 | 0.497 | 0.980 | 1.000 | 1.134 | -0.321 | 0.999 | 0.056 | 0.949 | 0.498 |
| 16 | 32 | 0.492 | 1.000 | 1.000 | 1.063 | -0.152 | 1.000 | 0.050 | 0.950 | 0.498 |
| 16 | 64 | 0.506 | 1.000 | 1.000 | 1.033 | -0.072 | 1.000 | 0.037 | 0.950 | 0.498 |
| 64 | 8 | 0.516 | 0.612 | 0.983 | 1.211 | -0.659 | 0.972 | 0.044 | 0.934 | 0.498 |
| 64 | 16 | 0.493 | 0.954 | 1.000 | 1.128 | -0.431 | 0.999 | 0.021 | 0.949 | 0.497 |
| 64 | 32 | 0.525 | 1.000 | 1.000 | 1.068 | -0.233 | 1.000 | 0.041 | 0.950 | 0.498 |
| 64 | 64 | 0.496 | 1.000 | 1.000 | 1.031 | -0.113 | 1.000 | 0.046 | 0.950 | 0.500 |

## Agent Comparison

### d=16, evidence=8

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 0.984 | 0.938 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 0.984 | 0.938 | 0.450 |
| t17_gain_only | 0.985 | 0.092 | 0.984 | 0.938 | 0.493 |
| t19_conformal_conscious | 0.984 | 0.059 | 0.984 | 0.938 | 0.495 |

### d=16, evidence=16

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 0.999 | 0.949 | 0.451 |
| boundary_score_raw | 1.000 | 1.000 | 0.999 | 0.949 | 0.451 |
| t17_gain_only | 1.000 | 0.056 | 0.999 | 0.949 | 0.498 |
| t19_conformal_conscious | 1.000 | 0.056 | 0.999 | 0.949 | 0.498 |

### d=16, evidence=32

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| t17_gain_only | 1.000 | 0.097 | 1.000 | 0.950 | 0.495 |
| t19_conformal_conscious | 1.000 | 0.050 | 1.000 | 0.950 | 0.498 |

### d=16, evidence=64

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| t17_gain_only | 1.000 | 0.159 | 1.000 | 0.950 | 0.492 |
| t19_conformal_conscious | 1.000 | 0.037 | 1.000 | 0.950 | 0.498 |

### d=64, evidence=8

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 0.972 | 0.932 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 0.972 | 0.932 | 0.450 |
| t17_gain_only | 0.973 | 0.061 | 0.972 | 0.934 | 0.497 |
| t19_conformal_conscious | 0.972 | 0.044 | 0.972 | 0.934 | 0.498 |

### d=64, evidence=16

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 0.999 | 0.949 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 0.999 | 0.949 | 0.450 |
| t17_gain_only | 0.999 | 0.021 | 0.999 | 0.949 | 0.497 |
| t19_conformal_conscious | 0.999 | 0.021 | 0.999 | 0.949 | 0.497 |

### d=64, evidence=32

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| t17_gain_only | 1.000 | 0.041 | 1.000 | 0.950 | 0.498 |
| t19_conformal_conscious | 1.000 | 0.041 | 1.000 | 0.950 | 0.498 |

### d=64, evidence=64

| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |
|---|---:|---:|---:|---:|---:|
| scalar_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| boundary_score_raw | 1.000 | 1.000 | 1.000 | 0.950 | 0.450 |
| t17_gain_only | 1.000 | 0.104 | 1.000 | 0.950 | 0.496 |
| t19_conformal_conscious | 1.000 | 0.046 | 1.000 | 0.950 | 0.500 |

## Interpretation

A pass has scalar-surprise AUC near 0.5, boundary-gain AUC near 1.0, T19 false conscious admission near the finite-rank alpha level, and T19 structural admission near oracle performance.

The conscious content set in this MVP has capacity one, so a successful T19 episode has `C_t = {z0*z1}` in the structural condition and `C_t = empty` in the noise condition.
