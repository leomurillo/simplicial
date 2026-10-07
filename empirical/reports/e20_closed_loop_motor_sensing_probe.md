# E20 Closed-Loop Motor-Sensing Probe

- timestamp: `2026-06-04T04:35:03.177583+00:00`
- dataset: `Synthetic closed-loop motor-sensing field`
- train/calibration/test episodes: `7000` / `2400` / `3600`
- actions: `['commit', 'hold', 'aim_0', 'aim_1', 'aim_2', 'aim_3']`
- aim/hold cost: `0.04` / `0.018`
- alpha: `0.05`
- finding: **CLOSED_LOOP_HYBRID_GOVERNANCE_NEEDED**

## Claim Tested

E20 tests whether boundary governance reappears when action
changes the future state, instead of selecting an offline glimpse.
Each candidate control is applied to the early state and produces
a different post-action state before utility is scored.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous value rmse | 0.310 |
| gate value rmse | 0.418 |
| governed value rmse | 0.310 |
| hybrid value rmse | 0.302 |
| continuous action accuracy | 0.644 |
| gate action accuracy | 0.368 |
| governed action accuracy | 0.709 |
| hybrid action accuracy | 0.720 |
| continuous regret | 0.242 |
| gate regret | 0.591 |
| governed regret | 0.177 |
| hybrid regret | 0.164 |
| continuous unnecessary unsafe | 0.243 |
| gate unnecessary unsafe | 0.577 |
| hybrid unnecessary unsafe | 0.172 |
| continuous missed control | 0.033 |
| gate missed control | 0.058 |
| hybrid missed control | 0.060 |
| gate threshold | 0.800 |

## Split Summary

| split | episodes | packets | mean utility | mean gate | mean unsafe | optimal actions |
| --- | --- | --- | --- | --- | --- | --- |
| train | 7000 | 42000 | 0.321 | 0.255 | 0.596 | commit:1622, hold:740, aim_0:1193, aim_1:1171, aim_2:1140, aim_3:1134 |
| calibration | 2400 | 14400 | 0.323 | 0.249 | 0.595 | commit:521, hold:294, aim_0:393, aim_1:365, aim_2:409, aim_3:418 |
| test | 3600 | 21600 | 0.322 | 0.253 | 0.596 | commit:836, hold:385, aim_0:588, aim_1:641, aim_2:537, aim_3:613 |

## Model Summary

| model | value RMSE | value R2 | action acc | regret | p90 regret | false commit | missed control | wrong control | unsafe choice | unnecessary unsafe | row detect | row false |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar | 0.366 | 0.424 | 0.564 | 0.343 | 1.088 | 0.122 | 0.085 | 0.243 | 0.339 | 0.337 | 0.000 | 0.000 |
| continuous_transition_value | 0.310 | 0.585 | 0.644 | 0.242 | 1.018 | 0.040 | 0.033 | 0.149 | 0.246 | 0.243 | 0.047 | 0.003 |
| conformal_transition_gate | 0.418 | 0.247 | 0.368 | 0.591 | 1.125 | 0.079 | 0.058 | 0.454 | 0.579 | 0.577 | 0.219 | 0.016 |
| governed_transition | 0.310 | 0.586 | 0.709 | 0.177 | 0.959 | 0.078 | 0.057 | 0.113 | 0.185 | 0.183 | 0.261 | 0.018 |
| hybrid_full | 0.302 | 0.608 | 0.720 | 0.164 | 0.948 | 0.079 | 0.060 | 0.109 | 0.174 | 0.172 | 0.354 | 0.024 |

## Aim-Cost Sweep

| aim cost | optimal actions | cont acc | gate acc | hybrid acc | cont regret | gate regret | hybrid regret | cont unsafe | gate unsafe | hybrid unsafe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | commit:368, hold:18, aim_0:794, aim_1:842, aim_2:754, aim_3:824 | 0.729 | 0.277 | 0.706 | 0.159 | 0.607 | 0.186 | 0.163 | 0.591 | 0.192 |
| 0.040 | commit:836, hold:385, aim_0:588, aim_1:641, aim_2:537, aim_3:613 | 0.644 | 0.368 | 0.720 | 0.242 | 0.591 | 0.164 | 0.243 | 0.577 | 0.172 |
| 0.100 | commit:960, hold:749, aim_0:467, aim_1:502, aim_2:433, aim_3:489 | 0.638 | 0.402 | 0.720 | 0.267 | 0.233 | 0.191 | 0.277 | 0.261 | 0.206 |

## Interpretation

The hybrid policy wins on the closed-loop intervention task.
Continuous value sees rich pre/post evidence, but the gate adds
boundary-persistence information that improves action choice.

## Anti-Tautology Checks

- actions intervene on the future state before utility is scored;
- every episode enumerates the same starting state under multiple controls;
- wrong controls can rupture or deform the post-action evidence;
- policy metrics choose one action per held-out episode and score regret;
- continuous features include rich post-action evidence, so gate gains are not automatic;
- the aim-cost sweep checks cheap, main, and expensive control regimes.
