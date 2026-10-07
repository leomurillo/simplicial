# E14 Governance Risk Falsifier

- timestamp: `2026-06-03T23:39:06.647246+00:00`
- seed: `20260603`
- main forbidden mix: `0.4`
- risk/bait share: `0.35` / `0.35`
- route/null trials: `900` / `450`
- alpha: `0.05`
- finding: **RISK_FITS_BUT_GATE_RECOVERS_REFUSAL**

## Claim Tested

E14 tests whether governance/refusal survives a strong continuous
risk/preference rival. The rival sees competence, action value, ordinary
risk, preference conflict, policy cost, and train-side rule pressure. The
governance gate sees held-out rule/sanction persistence calibrated on
non-forbidden worlds.

The probe scores two jobs separately: predicting graded behavioral
inhibition and admitting governed refusal.

## Main Decision Quantities

| quantity | value |
|---|---|
| continuous inhibition RMSE | 0.209 |
| gate inhibition RMSE | 0.283 |
| hybrid inhibition RMSE | 0.096 |
| continuous false refusal | 0.196 |
| gate false refusal | 0.000 |
| governed false refusal | 0.000 |
| continuous refusal detection | 0.969 |
| gate refusal detection | 1.000 |
| governed refusal detection | 1.000 |
| continuous bait false | 0.990 |
| gate bait false | 0.000 |
| continuous risk false | 0.000 |
| gate risk false | 0.000 |
| conformal governance gate | 0.368 |

## Model Summary

| model | inhibition RMSE | inhibition R2 | refusal RMSE | refusal acc | refusal detect | nonforbid FA | risk FA | bait FA | allowed FA |
|---|---|---|---|---|---|---|---|---|---|
| scalar | 0.319 | -0.002 | 0.426 | 0.739 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| continuous_risk | 0.209 | 0.570 | 0.302 | 0.847 | 0.969 | 0.196 | 0.000 | 0.990 | 0.000 |
| governance_gate | 0.283 | 0.214 | 0.087 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| governed_risk_gate | 0.098 | 0.905 | 0.083 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| hybrid_risk_governance | 0.096 | 0.910 | 0.072 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Source Means

| source | scalar | competence | action value | risk | pref conflict | train rule | heldout rule | governance score | target inhibit | target refusal |
|---|---|---|---|---|---|---|---|---|---|---|
| forbidden_world | 0.999 | 0.859 | 0.858 | 0.311 | 0.306 | 0.873 | 0.873 | 0.853 | 0.950 | 1.000 |
| risk_world | 0.998 | 0.872 | 0.875 | 0.876 | 0.771 | 0.139 | 0.148 | 0.284 | 0.981 | 0.000 |
| bait_world | 1.000 | 0.857 | 0.875 | 0.318 | 0.291 | 0.879 | 0.148 | 0.272 | 0.315 | 0.000 |
| allowed_world | 0.997 | 0.861 | 0.879 | 0.135 | 0.118 | 0.112 | 0.109 | 0.246 | 0.069 | 0.000 |
| no_signal_world | 1.000 | 0.098 | 0.102 | 0.133 | 0.120 | 0.104 | 0.101 | 0.093 | 0.748 | 0.000 |

## Phase Sweep

| forbidden mix | inhibition winner | refusal winner | cont inhib | gate inhib | hybrid inhib | cont FA | gate FA | gate detect | cont bait FA | cont risk FA |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.000 | continuous_risk | scalar | 0.079 | 0.352 | 0.079 | 0.000 | 0.000 | nan | 0.000 | 0.000 |
| 0.200 | hybrid_risk_governance | hybrid_risk_governance | 0.191 | 0.316 | 0.089 | 0.002 | 0.000 | 1.000 | 0.010 | 0.000 |
| 0.400 | hybrid_risk_governance | hybrid_risk_governance | 0.212 | 0.286 | 0.093 | 0.195 | 0.000 | 1.000 | 0.993 | 0.000 |
| 0.700 | hybrid_risk_governance | hybrid_risk_governance | 0.175 | 0.213 | 0.100 | 0.113 | 0.000 | 1.000 | 1.000 | 0.000 |
| 1.000 | hybrid_risk_governance | hybrid_risk_governance | 0.062 | 0.066 | 0.062 | 0.000 | 0.003 | 1.000 | nan | nan |

## Interpretation

Continuous risk/preference variables win the graded inhibition
problem, but train-side rule pressure confuses local bait and
ordinary risk with governed refusal. The held-out governance gate
recovers represented-but-blocked competence while controlling
false refusal. E14 therefore supports governed risk control:
risk explains inhibition, while rule persistence decides refusal.

## Anti-Tautology Checks

- scalar surprise is matched by construction;
- risk worlds suppress action but are not governed refusals;
- bait worlds have high train-side rule pressure but low held-out rule persistence;
- forbidden worlds preserve competence and held-out rule violation;
- the continuous rival sees risk/preference variables but not held-out governance persistence;
- the governance gate is calibrated on held-out non-forbidden scores.
