# E11 Noise-Structure Uncertainty Falsifier

- timestamp: `2026-06-03T22:28:19.284365+00:00`
- seed: `20260603`
- main structure mix: `0.5`
- route/null trials: `900` / `450`
- alpha: `0.05`
- finding: **UNCERTAINTY_FITS_BUT_GATE_RECOVERS_STRUCTURE**

## Claim Tested

E11 tests whether the noise-versus-structure bucket survives a strong
continuous uncertainty rival. The rival receives expected uncertainty,
unexpected uncertainty, volatility, precision, and train-side gain. The
bucket gate receives held-out structural gain calibrated on nonstructure
worlds.

The probe scores two jobs separately: predicting graded precision response
and controlling false structural admission.

## Main Decision Quantities

| quantity | value |
|---|---|
| continuous precision RMSE | 0.065 |
| bucket precision RMSE | 0.165 |
| hybrid precision RMSE | 0.064 |
| continuous false structure | 0.000 |
| bucket false structure | 0.050 |
| governed false structure | 0.050 |
| continuous structure detection | 0.818 |
| bucket structure detection | 0.949 |
| governed structure detection | 0.949 |
| conformal structure gate | 0.044 |

## Model Summary

| model | precision RMSE | precision R2 | structure RMSE | structure acc | structure detect | nonstructure FA | uncertainty FA | noise FA |
|---|---|---|---|---|---|---|---|---|
| scalar | 0.195 | -0.000 | 0.458 | 0.663 | 0.000 | 0.000 | 0.000 | 0.000 |
| continuous_uncertainty | 0.065 | 0.890 | 0.229 | 0.939 | 0.818 | 0.000 | 0.000 | 0.000 |
| bucket_structure_gate | 0.165 | 0.283 | 0.194 | 0.950 | 0.949 | 0.050 | 0.047 | 0.053 |
| governed_uncertainty_gate | 0.064 | 0.893 | 0.188 | 0.950 | 0.949 | 0.050 | 0.047 | 0.053 |
| hybrid_uncertainty_structure | 0.064 | 0.893 | 0.188 | 0.950 | 0.949 | 0.050 | 0.047 | 0.053 |

## Source Means

| source | scalar | expected U | unexpected U | volatility | train gain | heldout gain | target precision | target structure |
|---|---|---|---|---|---|---|---|---|
| structure_world | 1.000 | 0.493 | 0.788 | 0.922 | 0.999 | 0.218 | 0.795 | 1.000 |
| uncertainty_world | 1.000 | 0.505 | 0.770 | 0.881 | 0.999 | 0.018 | 0.723 | 0.000 |
| noise_world | 1.000 | 0.754 | 0.127 | 0.443 | 0.999 | 0.018 | 0.378 | 0.000 |

## Phase Sweep

| structure mix | precision winner | structure winner | cont precision | bucket precision | hybrid precision | cont FA | bucket FA | bucket detect |
|---|---|---|---|---|---|---|---|---|
| 0.000 | continuous_uncertainty | scalar | 0.059 | 0.178 | 0.059 | 0.000 | 0.000 | nan |
| 0.250 | continuous_uncertainty | continuous_uncertainty | 0.064 | 0.174 | 0.064 | 0.000 | 0.009 | 0.913 |
| 0.500 | governed_uncertainty_gate | continuous_uncertainty | 0.066 | 0.170 | 0.065 | 0.000 | 0.059 | 0.963 |
| 0.750 | governed_uncertainty_gate | scalar | 0.064 | 0.151 | 0.063 | 0.019 | 0.046 | 0.934 |
| 1.000 | governed_uncertainty_gate | continuous_uncertainty | 0.065 | 0.110 | 0.062 | 0.000 | 0.049 | 0.957 |

## Interpretation

The continuous uncertainty rival wins the graded precision-response
problem and remains conservative on false structural admission,
but it misses too many real structures. The conformal held-out gate
recovers structural sensitivity at approximately calibrated false
admission. E11 therefore supports governed uncertainty: continuous
expected/unexpected uncertainty explains gain, while held-out
boundary evidence decides when a residual becomes structure.

## Anti-Tautology Checks

- scalar surprise is approximately matched by standardizing residuals;
- train-only bait creates high train gain in all worlds;
- the continuous rival sees uncertainty and train-side gain, but not held-out gain;
- the structural gate is calibrated only on nonstructure held-out gains;
- the phase sweep includes worlds where continuous uncertainty should win.
