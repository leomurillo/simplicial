# E22 Trained-MLP Closed-Loop Probe

- timestamp: `2026-06-04T05:08:57.852451+00:00`
- dataset: `Synthetic closed-loop motor-sensing field`
- train/calibration/test episodes: `2400` / `900` / `1600`
- aim/hold cost: `0.04` / `0.018`
- hidden layers: `[64, 32]`
- epochs/patience: `55` / `8`
- alpha: `0.05`
- gate threshold: `0.811`
- finding: **TRAINED_MLP_ABSORBS_GATE**

## Claim Tested

E22 replaces E21's random-feature absorber with a genuinely
trained NumPy MLP. The simulator is unchanged from E20/E21.
The decisive comparison is continuous_mlp versus hybrid_mlp.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| pairwise regret | 0.154 |
| continuous mlp regret | 0.128 |
| hybrid mlp regret | 0.128 |
| pairwise accuracy | 0.738 |
| continuous mlp accuracy | 0.805 |
| hybrid mlp accuracy | 0.806 |
| pairwise unnecessary unsafe | 0.161 |
| continuous mlp unnecessary unsafe | 0.131 |
| hybrid mlp unnecessary unsafe | 0.131 |
| continuous mlp value rmse | 0.256 |
| hybrid mlp value rmse | 0.255 |

## Split Summary

| split | episodes | packets | mean utility | mean gate | mean unsafe | optimal actions |
| --- | --- | --- | --- | --- | --- | --- |
| train | 2400 | 14400 | 0.325 | 0.254 | 0.592 | commit:561, hold:253, aim_0:447, aim_1:390, aim_2:386, aim_3:363 |
| calibration | 900 | 5400 | 0.324 | 0.256 | 0.596 | commit:228, hold:86, aim_0:151, aim_1:140, aim_2:133, aim_3:162 |
| test | 1600 | 9600 | 0.328 | 0.257 | 0.589 | commit:388, hold:182, aim_0:242, aim_1:259, aim_2:263, aim_3:266 |

## Model Summary

| model | basis | raw features | expanded/hidden | value RMSE | value R2 | select RMSE | action acc | regret | p90 regret | unsafe choice | unnecessary unsafe | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| continuous_pairwise_ridge | pairwise | 43 | 990 | 0.268 | 0.692 | 0.272 | 0.738 | 0.154 | 0.954 | 0.162 | 0.161 | 0.617 | 0.044 |
| continuous_mlp | trained_mlp | 43 | [64, 32] | 0.256 | 0.719 | 0.244 | 0.805 | 0.128 | 0.946 | 0.132 | 0.131 | 0.724 | 0.048 |
| hybrid_mlp | trained_mlp | 54 | [64, 32] | 0.255 | 0.721 | 0.242 | 0.806 | 0.128 | 0.949 | 0.132 | 0.131 | 0.726 | 0.046 |

## Interpretation

The trained no-gate continuous MLP absorbs the gate-aware hybrid.
This means the gate residual is not irreducible in this simulator.

## Anti-Tautology Checks

- the task and simulator are inherited from E20/E21;
- continuous_mlp has no gate features;
- hybrid_mlp has the same architecture plus gate features;
- both MLPs are trained by minibatch Adam with validation early stopping;
- continuous_pairwise_ridge is retained as the E21 absorber reference;
- policy metrics choose one action per held-out episode and score regret.
