# E25 Robot Failure Refusal Gate Probe

- timestamp: `2026-06-04T18:04:03.517513+00:00`
- dataset: `UCI Robot Execution Failures`
- dataset page: `https://archive.ics.uci.edu/dataset/138/robot+execution+failures`
- KDD page: `https://kdd.ics.uci.edu/databases/robotfailure/robotfailure.html`
- instances safe/failure: `129` / `334`
- prefix lengths: `[3, 6, 9, 12, 15]`
- gate threshold: `0.001`
- finding: **ROBOT_FAILURE_MLP_ABSORBS_GATE_WITH_SAFETY_HINT**

## Claim Tested

E25 asks whether a label-free failure/refusal gate adds residual
policy value after a trained no-gate MLP sees force/torque
prefixes from external robot execution failures.

## Dataset Audit

| quantity | value |
| --- | --- |
| files | {'lp1': {'path': 'C:\\Projects\\simplicial\\empirical\\data\\robot_execution_failures\\lp1.data', 'bytes': 27345, 'instances': 88, 'labels': {'normal': 21, 'collision': 17, 'obstruction': 34, 'fr_collision': 16}, 'safe': 21, 'failure': 67}, 'lp2': {'path': 'C:\\Projects\\simplicial\\empirical\\data\\robot_execution_failures\\lp2.data', 'bytes': 14606, 'instances': 47, 'labels': {'normal': 20, 'back_col': 7, 'front_col': 6, 'right_col': 5, 'left_col': 9}, 'safe': 20, 'failure': 27}, 'lp3': {'path': 'C:\\Projects\\simplicial\\empirical\\data\\robot_execution_failures\\lp3.data', 'bytes': 14512, 'instances': 47, 'labels': {'ok': 20, 'moved': 15, 'slightly_moved': 9, 'lost': 3}, 'safe': 20, 'failure': 27}, 'lp4': {'path': 'C:\\Projects\\simplicial\\empirical\\data\\robot_execution_failures\\lp4.data', 'bytes': 33619, 'instances': 117, 'labels': {'normal': 24, 'collision': 72, 'obstruction': 21}, 'safe': 24, 'failure': 93}, 'lp5': {'path': 'C:\\Projects\\simplicial\\empirical\\data\\robot_execution_failures\\lp5.data', 'bytes': 49158, 'instances': 164, 'labels': {'normal': 44, 'collision_in_tool': 26, 'collision_in_part': 47, 'bottom_obstruction': 21, 'bottom_collision': 26}, 'safe': 44, 'failure': 120}} |
| labels | {'normal': 109, 'collision': 89, 'obstruction': 55, 'fr_collision': 16, 'back_col': 7, 'front_col': 6, 'right_col': 5, 'left_col': 9, 'ok': 20, 'moved': 15, 'slightly_moved': 9, 'lost': 3, 'collision_in_tool': 26, 'collision_in_part': 47, 'bottom_obstruction': 21, 'bottom_collision': 26} |
| split instances | {'train': {'instances': 277, 'safe': 77, 'failure': 200, 'problems': {'lp1': 53, 'lp2': 28, 'lp3': 28, 'lp4': 70, 'lp5': 98}, 'labels': {'normal': 65, 'obstruction': 27, 'fr_collision': 11, 'collision': 58, 'left_col': 5, 'front_col': 5, 'back_col': 4, 'right_col': 2, 'ok': 12, 'slightly_moved': 7, 'lost': 2, 'moved': 7, 'collision_in_tool': 13, 'collision_in_part': 28, 'bottom_obstruction': 12, 'bottom_collision': 19}}, 'calibration': {'instances': 94, 'safe': 26, 'failure': 68, 'problems': {'lp1': 18, 'lp2': 10, 'lp3': 10, 'lp4': 23, 'lp5': 33}, 'labels': {'normal': 22, 'fr_collision': 3, 'obstruction': 14, 'collision': 15, 'left_col': 2, 'right_col': 2, 'back_col': 2, 'ok': 4, 'slightly_moved': 1, 'moved': 5, 'bottom_obstruction': 5, 'collision_in_part': 9, 'collision_in_tool': 6, 'bottom_collision': 4}}, 'test': {'instances': 92, 'safe': 26, 'failure': 66, 'problems': {'lp1': 17, 'lp2': 9, 'lp3': 9, 'lp4': 24, 'lp5': 33}, 'labels': {'normal': 22, 'obstruction': 14, 'fr_collision': 2, 'collision': 16, 'front_col': 1, 'left_col': 2, 'back_col': 1, 'right_col': 1, 'ok': 4, 'moved': 3, 'slightly_moved': 1, 'lost': 1, 'collision_in_part': 10, 'bottom_obstruction': 4, 'bottom_collision': 3, 'collision_in_tool': 7}}} |
| prefix counts | {'train': 1385, 'calibration': 470, 'test': 460} |
| probe accuracy | {'train': 0.9270758122743682, 'calibration': 0.9, 'test': 0.8978260869565218} |
| majority accuracy | {'train': 0.7220216606498195, 'calibration': 0.723404255319149, 'test': 0.717391304347826} |
| probe model | {'raw_feature_count': 55, 'expanded_feature_count': 111} |

## Main Decision Quantities

| quantity | value |
| --- | --- |
| scalar accuracy | 0.909 |
| continuous accuracy | 0.948 |
| hybrid accuracy | 0.946 |
| scalar regret | 0.155 |
| continuous regret | 0.080 |
| hybrid regret | 0.081 |
| continuous unsafe continue | 0.022 |
| hybrid unsafe continue | 0.020 |
| continuous false refusal | 0.030 |
| hybrid false refusal | 0.035 |
| continuous select rmse | 0.222 |
| hybrid select rmse | 0.301 |

## Split Summary

| split | episodes | packets | mean utility | mean gate | unsafe continue | false refusal | optimal actions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| train | 1385 | 2770 | 0.075 | 0.094 | 0.361 | 0.139 | continue:385, refuse_recover:1000 |
| calibration | 470 | 940 | 0.075 | 0.107 | 0.362 | 0.138 | continue:130, refuse_recover:340 |
| test | 460 | 920 | 0.077 | 0.079 | 0.359 | 0.141 | continue:130, refuse_recover:330 |

## Model Summary

| model | features | value RMSE | select RMSE | action acc | regret | p90 regret | unsafe continue | false refusal | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar_mlp | 4 | 0.492 | 0.280 | 0.909 | 0.155 | 0.000 | 0.061 | 0.030 | 0.902 | 0.089 |
| continuous_mlp | 64 | 0.401 | 0.222 | 0.948 | 0.080 | 0.000 | 0.022 | 0.030 | 0.946 | 0.061 |
| hybrid_mlp | 69 | 0.432 | 0.301 | 0.946 | 0.081 | 0.000 | 0.020 | 0.035 | 0.937 | 0.065 |

## Interpretation

The trained no-gate MLP absorbs the gate on the primary metrics,
but the hybrid keeps a small unsafe-continue safety hint.

## Anti-Tautology Checks

- the dataset is external robot execution failure data;
- normal/ok labels define continue; every other label defines refuse/recover;
- splits are by instance, not by prefix;
- continuous_mlp receives no gate score or gate bit;
- hybrid_mlp has the same architecture plus gate features;
- refusal utility includes explicit unsafe-continue and false-refusal costs;
- failure cost is still a proxy over labels, not a measured reward.
