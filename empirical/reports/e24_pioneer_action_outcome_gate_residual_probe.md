# E24 Pioneer Action-Outcome Gate-Residual Probe

- timestamp: `2026-06-04T05:56:19.519315+00:00`
- dataset: `UCI KDD Pioneer-1 Mobile Robot Data`
- dataset page: `https://kdd.ics.uci.edu/databases/pioneer/pioneer.html`
- description page: `https://kdd.ics.uci.edu/databases/pioneer/pioneer.data.html`
- trials/files: `144` / `['move.data.gz', 'turn.data.gz']`
- rows per trial: `{'min': 39, 'max': 80, 'mean': 58.701388888888886}`
- split strategy: `stratified`
- min prefix / stride: `8` / `3`
- gate threshold: `0.002`
- finding: **PIONEER_MLP_ABSORBS_GATE**

## Claim Tested

E24 asks whether a label-free temporal gate adds residual value
after a trained no-gate MLP learns qualitative action outcomes
from external Pioneer-1 robot experiences.

## Dataset Audit

| quantity | value |
| --- | --- |
| outcome trials | {'clear_visible': 36, 'vanish': 16, 'discover': 22, 'obstructed': 30, 'push': 40} |
| outcome rows | {'clear_visible': 2040, 'vanish': 886, 'discover': 1383, 'obstructed': 1645, 'push': 2499} |
| action families | {'move': 76, 'retr': 26, 'turn': 42} |
| split trials | {'train': {'trials': 86, 'outcomes': {'clear_visible': 21, 'vanish': 10, 'discover': 13, 'obstructed': 18, 'push': 24}, 'action_families': {'retr': 15, 'move': 46, 'turn': 25}}, 'calibration': {'trials': 30, 'outcomes': {'clear_visible': 8, 'vanish': 3, 'discover': 5, 'obstructed': 6, 'push': 8}, 'action_families': {'move': 16, 'retr': 5, 'turn': 9}}, 'test': {'trials': 28, 'outcomes': {'clear_visible': 7, 'vanish': 3, 'discover': 4, 'obstructed': 6, 'push': 8}, 'action_families': {'retr': 6, 'move': 14, 'turn': 8}}} |
| prefix counts | {'train': 1490, 'calibration': 517, 'test': 467} |
| probe accuracy | {'train': 1.0, 'calibration': 0.5764023210831721, 'test': 0.6638115631691649} |
| majority accuracy | {'train': 0.3046979865771812, 'calibration': 0.2804642166344294, 'test': 0.29978586723768735} |
| probe model | {'raw_feature_count': 259, 'expanded_feature_count': 519} |

## Main Decision Quantities

| quantity | value |
| --- | --- |
| scalar accuracy | 0.668 |
| continuous accuracy | 0.672 |
| hybrid accuracy | 0.662 |
| scalar regret | 0.392 |
| continuous regret | 0.388 |
| hybrid regret | 0.399 |
| continuous unsafe wrong | 0.103 |
| hybrid unsafe wrong | 0.099 |
| continuous severe miss | 0.049 |
| hybrid severe miss | 0.041 |
| continuous select rmse | 0.379 |
| hybrid select rmse | 0.342 |

## Split Summary

| split | episodes | packets | mean utility | mean gate | mean unsafe proxy | optimal outcomes |
| --- | --- | --- | --- | --- | --- | --- |
| train | 1490 | 7450 | 0.060 | 0.003 | 0.400 | clear_visible:348, obstructed:288, discover:242, vanish:158, push:454 |
| calibration | 517 | 2585 | 0.059 | 0.002 | 0.402 | clear_visible:136, obstructed:99, discover:88, vanish:49, push:145 |
| test | 467 | 2335 | 0.060 | 0.002 | 0.400 | clear_visible:108, obstructed:91, discover:78, vanish:50, push:140 |

## Model Summary

| model | features | value RMSE | select RMSE | action acc | regret | p90 regret | unsafe wrong | severe miss | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar_mlp | 7 | 0.421 | 0.352 | 0.668 | 0.392 | 1.280 | 0.103 | 0.041 | 0.653 | 0.086 |
| continuous_mlp | 276 | 0.420 | 0.379 | 0.672 | 0.388 | 1.280 | 0.103 | 0.049 | 0.375 | 0.095 |
| hybrid_mlp | 281 | 0.424 | 0.342 | 0.662 | 0.399 | 1.210 | 0.099 | 0.041 | 0.655 | 0.075 |

## Interpretation

The trained no-gate MLP absorbs the temporal gate on Pioneer-1 outcomes.

## Anti-Tautology Checks

- the dataset is external UCI KDD Pioneer-1 robot experience data;
- splits are by trial, not by row;
- the default split is stratified by file and outcome to keep rare outcomes represented;
- outcome markers are used only as targets, not predictor features;
- continuous_mlp receives no gate score or gate bit;
- hybrid_mlp has the same architecture plus gate features;
- the outcome utility is a proxy over qualitative descriptions, not a measured reward.
