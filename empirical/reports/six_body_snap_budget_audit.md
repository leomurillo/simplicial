# Six-Body Snap Budget Audit

This is a controlled Paper 28 scaffold, not a claim about real gravitation.
Replay state is tracked as position and momentum. Residual derivatives are
tracked in force units: `R`, `M^-1 dR/dt` (jerk), and `M^-1 d2R/dt2` (snap).

## Configuration

- trials: `10`
- steps: `850`
- dt: `0.0015`
- sample_stride: `25`
- replay_steps: `850`
- masses: `[1.0, 1.12, 0.94, 1.07, 0.89, 1.16]`
- gravity: `0.18`
- softening: `0.3`
- kappa_23: `0.006`
- jerk_scale: `0.01`
- position_tolerance: `0.001`

## Short-Horizon Fit

| model | rank | force test R2 | force test RMSE | jerk test R2 | snap test R2 |
|---|---:|---:|---:|---:|---:|
| lower_force_only | 125 | 0.982147 | 0.00612844 | 0.950715 | 0.817156 |
| lower_jerk_aware | 125 | 0.97822 | 0.00676912 | 0.919409 | 0.685066 |
| carry23_one_coeff | 1 | 1 | 3.494810e-17 | 1 | 1 |

## Long-Horizon Replay

| model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |
|---|---:|---:|---:|---:|
| pairwise_null | 0.0139568 | 0.0139568 | 0.0513224 | 0.0513224 |
| lower_force_only | 0.00225486 | 0.00225486 | 0.00476544 | 0.00476544 |
| lower_jerk_aware | 0.00190917 | 0.00190917 | 0.00461584 | 0.00461584 |
| recovered_carry23 | 6.542052e-18 | 6.542052e-18 | 5.932857e-17 | 5.932857e-17 |

## Snap Budget

| model | acc term | jerk term | snap term | total budget | snap/tol | total/tol |
|---|---:|---:|---:|---:|---:|---:|
| lower_force_only | 0.00566937 | 0.0278052 | 0.10947 | 0.142944 | 109.47 | 142.944 |
| lower_jerk_aware | 0.00617443 | 0.0304889 | 0.121451 | 0.158115 | 121.451 | 158.115 |
| recovered_carry23 | 3.762065e-17 | 3.018843e-15 | 2.255426e-12 | 2.258483e-12 | 2.255426e-09 | 2.258483e-09 |

## Invariants

| trajectory | max |P| | max angular drift | max relative energy drift |
|---|---:|---:|---:|
| truth | 2.294467e-15 | 1.262211e-15 | 1.560884e-06 |
| pairwise_null | 2.631845e-15 | 9.255819e-16 | 2.596709e-07 |
| recovered_carry23 | 2.300073e-15 | 1.239579e-15 | 1.560884e-06 |
| lower_force_only | 1.897005e-13 | 4.570702e-14 | nan |
| lower_jerk_aware | 1.219282e-13 | 1.070192e-13 | nan |

## Reading

A lower-arity model may score well on force and jerk while still losing
long-horizon replay. Snap becomes a must-track residual when the snap term
exceeds the declared position tolerance or materially dominates the budget.
