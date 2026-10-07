# E21 Strong-Absorber Closed-Loop Probe

- timestamp: `2026-06-04T04:47:02.795545+00:00`
- dataset: `Synthetic closed-loop motor-sensing field`
- train/calibration/test episodes: `5200` / `1800` / `3000`
- aim/hold cost: `0.04` / `0.018`
- random hidden features: `384`
- alpha: `0.05`
- gate threshold: `0.803`
- finding: **E20_CAPACITY_CONFOUND_WITH_HYBRID_EDGE**

## Claim Tested

E21 asks whether the E20 hybrid win survives stronger no-gate
continuous absorbers. The task and simulator are inherited from
E20; only model capacity is changed.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous lite regret | 0.257 |
| continuous pairwise regret | 0.148 |
| continuous random regret | 0.166 |
| hybrid lite regret | 0.167 |
| hybrid random regret | 0.146 |
| best strong continuous regret | 0.148 |
| best hybrid regret | 0.146 |
| continuous lite accuracy | 0.636 |
| continuous pairwise accuracy | 0.763 |
| continuous random accuracy | 0.728 |
| hybrid lite accuracy | 0.723 |
| hybrid random accuracy | 0.784 |
| best strong continuous accuracy | 0.763 |
| best hybrid accuracy | 0.784 |
| continuous lite unnecessary unsafe | 0.260 |
| continuous pairwise unnecessary unsafe | 0.155 |
| continuous random unnecessary unsafe | 0.172 |
| hybrid lite unnecessary unsafe | 0.175 |
| hybrid random unnecessary unsafe | 0.152 |
| best strong continuous unnecessary unsafe | 0.155 |
| best hybrid unnecessary unsafe | 0.152 |
| best strong continuous | continuous_pairwise |
| best hybrid | hybrid_random_absorber |

## Split Summary

| split | episodes | packets | mean utility | mean gate | mean unsafe | optimal actions |
| --- | --- | --- | --- | --- | --- | --- |
| train | 5200 | 31200 | 0.324 | 0.253 | 0.593 | commit:1232, hold:548, aim_0:918, aim_1:861, aim_2:839, aim_3:802 |
| calibration | 1800 | 10800 | 0.322 | 0.253 | 0.597 | commit:416, hold:185, aim_0:297, aim_1:282, aim_2:293, aim_3:327 |
| test | 3000 | 18000 | 0.325 | 0.254 | 0.591 | commit:709, hold:322, aim_0:499, aim_1:518, aim_2:457, aim_3:495 |

## Model Summary

| model | basis | expanded | value RMSE | value R2 | action acc | regret | p90 regret | unsafe choice | unnecessary unsafe | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar_lite | lite | 17 | 0.362 | 0.436 | 0.542 | 0.362 | 1.096 | 0.360 | 0.358 | 0.000 | 0.000 |
| gate_lite | lite | 27 | 0.417 | 0.252 | 0.374 | 0.577 | 1.124 | 0.569 | 0.568 | 0.224 | 0.017 |
| continuous_lite | lite | 87 | 0.308 | 0.593 | 0.636 | 0.257 | 1.022 | 0.261 | 0.260 | 0.049 | 0.005 |
| continuous_pairwise | pairwise | 990 | 0.264 | 0.700 | 0.763 | 0.148 | 0.947 | 0.156 | 0.155 | 0.640 | 0.042 |
| continuous_random_absorber | random | 471 | 0.273 | 0.680 | 0.728 | 0.166 | 0.973 | 0.173 | 0.172 | 0.556 | 0.037 |
| hybrid_lite | lite | 109 | 0.299 | 0.615 | 0.723 | 0.167 | 0.952 | 0.176 | 0.175 | 0.357 | 0.026 |
| hybrid_random_absorber | random | 493 | 0.266 | 0.695 | 0.784 | 0.146 | 0.961 | 0.153 | 0.152 | 0.607 | 0.036 |

## Interpretation

A stronger continuous absorber erases most of the original
hybrid-lite advantage, so E20 was capacity-sensitive. A
capacity-matched hybrid still keeps a small accuracy edge, but
the regret gap is too small for a strong survival claim.

## Anti-Tautology Checks

- the simulator and task are inherited from E20;
- no-gate continuous models receive pairwise and random nonlinear absorbers;
- hybrid_random_absorber receives comparable random-feature capacity;
- policy metrics choose one action per held-out episode and score regret;
- a governance win is counted only against the best strong continuous baseline.
