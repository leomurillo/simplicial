# E12 Ambiguity EIG Falsifier

- timestamp: `2026-06-03T22:47:33.809088+00:00`
- seed: `20260603`
- main ambiguity mix: `0.5`
- route/null trials: `900` / `450`
- alpha: `0.05`
- finding: **EIG_FITS_BUT_GATE_RECOVERS_AMBIGUITY**

## Claim Tested

E12 tests whether ambiguity/sampling survives a strong continuous
expected-information-gain rival. The rival sees EIG, entropy, value,
sampling cost, precision, and train-side candidate multiplicity. The
ambiguity gate sees held-out candidate-set persistence calibrated on
nonambiguity worlds.

The probe scores two jobs separately: predicting graded sampling effort
and admitting persistent ambiguity.

## Main Decision Quantities

| quantity | value |
|---|---|
| continuous effort RMSE | 0.093 |
| bucket effort RMSE | 0.247 |
| hybrid effort RMSE | 0.052 |
| continuous false ambiguity | 0.178 |
| bucket false ambiguity | 0.000 |
| governed false ambiguity | 0.000 |
| continuous ambiguity detection | 0.565 |
| bucket ambiguity detection | 1.000 |
| governed ambiguity detection | 1.000 |
| conformal ambiguity gate | 0.554 |

## Model Summary

| model | effort RMSE | effort R2 | ambiguity RMSE | ambiguity acc | ambiguity detect | nonambig FA | EIG FA | no-sample FA |
|---|---|---|---|---|---|---|---|---|
| scalar | 0.324 | -0.000 | 0.465 | 0.653 | 0.000 | 0.000 | 0.000 | 0.000 |
| continuous_eig | 0.093 | 0.917 | 0.391 | 0.733 | 0.565 | 0.178 | 0.364 | 0.000 |
| ambiguity_set_gate | 0.247 | 0.419 | 0.092 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 |
| governed_eig_gate | 0.061 | 0.964 | 0.093 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 |
| hybrid_eig_ambiguity | 0.052 | 0.974 | 0.074 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 |

## Source Means

| source | scalar | train EIG | heldout EIG | train entropy | heldout entropy | train set | heldout set | ambiguity score | target effort | target ambiguity |
|---|---|---|---|---|---|---|---|---|---|---|
| ambiguity_world | 0.999 | 0.526 | 0.526 | 0.797 | 0.808 | 4.724 | 4.817 | 1.276 | 0.896 | 1.000 |
| eig_world | 1.002 | 0.596 | 0.468 | 0.797 | 0.223 | 4.661 | 1.430 | 0.445 | 0.757 | 0.000 |
| no_sample_world | 0.999 | -0.150 | -0.150 | 0.164 | 0.138 | 1.339 | 1.299 | 0.356 | 0.183 | 0.000 |

## Phase Sweep

| ambiguity mix | effort winner | ambiguity winner | cont effort | bucket effort | hybrid effort | cont FA | bucket FA | bucket detect |
|---|---|---|---|---|---|---|---|---|
| 0.000 | hybrid_eig_ambiguity | scalar | 0.056 | 0.289 | 0.049 | 0.000 | 0.000 | nan |
| 0.250 | hybrid_eig_ambiguity | hybrid_eig_ambiguity | 0.084 | 0.271 | 0.051 | 0.001 | 0.000 | 0.994 |
| 0.500 | hybrid_eig_ambiguity | hybrid_eig_ambiguity | 0.092 | 0.253 | 0.051 | 0.208 | 0.000 | 1.000 |
| 0.750 | hybrid_eig_ambiguity | hybrid_eig_ambiguity | 0.084 | 0.202 | 0.054 | 0.306 | 0.000 | 1.000 |
| 1.000 | hybrid_eig_ambiguity | hybrid_eig_ambiguity | 0.064 | 0.112 | 0.054 | 0.000 | 0.060 | 1.000 |

## Interpretation

The continuous EIG family wins the graded sampling-effort
problem: plain EIG beats the bucket on effort, and the hybrid
EIG-plus-heldout model is strongest overall. Plain EIG does not
recover persistent ambiguity as well as the held-out candidate-set
gate. E12 therefore supports governed sampling: continuous EIG
explains how hard to sample, while candidate-set persistence
decides when a multihypothesis state must remain open.

## Anti-Tautology Checks

- scalar surprise is matched by construction;
- high-EIG worlds and ambiguity worlds both contain train-side multihypothesis bait;
- the continuous rival sees EIG, cost, entropy, and train candidate multiplicity;
- the ambiguity gate is calibrated on held-out nonambiguity scores;
- the phase sweep includes worlds where EIG-family effort models should win cleanly.
