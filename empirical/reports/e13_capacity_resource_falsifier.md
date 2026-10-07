# E13 Capacity Resource-Rational Falsifier

- timestamp: `2026-06-03T22:55:21.195240+00:00`
- seed: `20260603`
- main tool mix: `0.5`
- compress share: `0.45`
- route/null trials: `900` / `450`
- alpha: `0.05`
- finding: **RESOURCE_FITS_BUT_GATE_RECOVERS_EXTERNALIZATION**

## Claim Tested

E13 tests whether capacity/compression/tool-use survives a strong
continuous resource-rational rival. The rival sees memory load,
capacity pressure, compression value, train-side tool value, tool cost,
and action cost. The externalization gate sees held-out tool persistence
calibrated on non-tool worlds.

The probe scores two jobs separately: predicting graded resource effort
and admitting a persistent external tool route.

## Main Decision Quantities

| quantity | value |
|---|---|
| continuous effort RMSE | 0.051 |
| gate effort RMSE | 0.250 |
| hybrid effort RMSE | 0.049 |
| continuous false externalize | 0.177 |
| gate false externalize | 0.000 |
| governed false externalize | 0.000 |
| continuous externalize detection | 0.923 |
| gate externalize detection | 1.000 |
| governed externalize detection | 1.000 |
| continuous bait false | 0.667 |
| gate bait false | 0.000 |
| conformal tool gate | 0.226 |

## Model Summary

| model | effort RMSE | effort R2 | external RMSE | external acc | tool detect | non-tool FA | bait FA | compress FA | no-cap FA |
|---|---|---|---|---|---|---|---|---|---|
| scalar | 0.324 | -0.000 | 0.456 | 0.671 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| continuous_resource | 0.051 | 0.975 | 0.312 | 0.856 | 0.923 | 0.177 | 0.667 | 0.000 | 0.000 |
| external_tool_gate | 0.250 | 0.405 | 0.091 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| governed_resource_gate | 0.050 | 0.977 | 0.084 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| hybrid_resource_tool | 0.049 | 0.977 | 0.071 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Source Means

| source | scalar | memory load | capacity | train tool | heldout tool | train rel | heldout rel | heldout compress | tool score | target effort | target external |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tool_world | 0.999 | 0.870 | 0.877 | 0.882 | 0.864 | 0.858 | 0.855 | 0.218 | 0.811 | 0.960 | 1.000 |
| compress_world | 1.000 | 0.552 | 0.455 | 0.229 | 0.209 | 0.357 | 0.327 | 0.769 | 0.143 | 0.693 | 0.000 |
| bait_world | 1.000 | 0.860 | 0.869 | 0.881 | 0.186 | 0.857 | 0.215 | 0.212 | 0.077 | 0.907 | 0.000 |
| no_capacity_world | 0.999 | 0.185 | 0.127 | 0.064 | 0.059 | 0.196 | 0.183 | 0.091 | -0.005 | 0.225 | 0.000 |

## Phase Sweep

| tool mix | effort winner | external winner | cont effort | gate effort | hybrid effort | cont FA | gate FA | gate detect | cont bait FA |
|---|---|---|---|---|---|---|---|---|---|
| 0.000 | hybrid_resource_tool | scalar | 0.051 | 0.291 | 0.051 | 0.000 | 0.000 | nan | 0.000 |
| 0.250 | hybrid_resource_tool | hybrid_resource_tool | 0.052 | 0.275 | 0.050 | 0.014 | 0.000 | 1.000 | 0.041 |
| 0.500 | hybrid_resource_tool | hybrid_resource_tool | 0.051 | 0.260 | 0.049 | 0.240 | 0.000 | 1.000 | 0.816 |
| 0.750 | hybrid_resource_tool | hybrid_resource_tool | 0.049 | 0.206 | 0.048 | 0.192 | 0.000 | 1.000 | 0.990 |
| 1.000 | hybrid_resource_tool | hybrid_resource_tool | 0.046 | 0.074 | 0.046 | 0.000 | 0.000 | 1.000 | nan |

## Interpretation

Continuous resource-rational variables win the graded effort
problem, but train-side utility alone confuses stable tools with
bait. The held-out externalization gate recovers persistent tool
use while controlling false admission. E13 therefore supports
governed resource control: resource rationality explains load,
while tool persistence decides when cognition should externalize.

## Anti-Tautology Checks

- scalar surprise is matched by construction;
- tool worlds and bait worlds both have high train-side tool value;
- compression worlds provide an internal resource competitor;
- the continuous rival sees cost and train utility, but not held-out tool persistence;
- the tool gate is calibrated on held-out non-tool scores;
- the phase sweep includes worlds where resource rationality should win.
