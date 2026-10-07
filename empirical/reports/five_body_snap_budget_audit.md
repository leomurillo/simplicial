# Five-Body Snap Budget Audit

This is a controlled Paper 28 scaffold, not a claim about real gravitation.
The admitted five-body feature is tested against lower <=4 shadows.

## Configuration

- trials: `12`
- steps: `850`
- dt: `0.0015`
- sample_stride: `25`
- replay_steps: `850`
- masses: `[1.0, 1.12, 0.94, 1.07, 0.89]`
- gravity: `0.22`
- softening: `0.28`
- chi: `0.05`
- lam: `1.0`
- channel: `attached`
- jerk_scale: `0.01`
- position_tolerance: `1e-06`
- recovered_five_coeff: `0.05`

## Short-Horizon Fit

| model | rank | force test R2 | force test RMSE | jerk test R2 | snap test R2 |
|---|---:|---:|---:|---:|---:|
| lower_force_only | 75 | 0.983445 | 2.486272e-05 | 0.892089 | 0.160553 |
| lower_jerk_aware | 75 | 0.980919 | 2.669241e-05 | 0.836503 | -0.541994 |
| five_one_coeff | 1 | 1 | 1.078729e-17 | 1 | 1 |

## Long-Horizon Replay

| model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |
|---|---:|---:|---:|---:|
| pairwise_null | 0.000119433 | 0.000119433 | 0.000243144 | 0.000243144 |
| lower_force_only | 1.042675e-05 | 1.042675e-05 | 2.037369e-05 | 2.037369e-05 |
| lower_jerk_aware | 1.039414e-05 | 1.039414e-05 | 2.153515e-05 | 2.153515e-05 |
| recovered_five | 0 | 0 | 8.958074e-19 | 8.958074e-19 |

## Snap Budget

| model | acc term | jerk term | snap term | total budget | snap/tol | total/tol |
|---|---:|---:|---:|---:|---:|---:|
| lower_force_only | 1.922542e-05 | 4.697310e-05 | 0.000192492 | 0.00025869 | 192.492 | 258.69 |
| lower_jerk_aware | 2.085448e-05 | 6.221504e-05 | 0.000272129 | 0.000355198 | 272.129 | 355.198 |
| recovered_five | 2.303708e-18 | 4.614118e-16 | 3.335824e-13 | 3.340461e-13 | 3.335824e-07 | 3.340461e-07 |

## Reading

The default `attached` channel is a five-body circuit coordinate, not the
older double-square `i5` scaffold.  The `stress_zero` channel is kept as a
control because the bilinear affine-circuit stress expression collapses by
the affine-dependence identity.

In this run the admitted five-body coordinate recovers the planted
coefficient and drives the snap budget to numerical zero.  Lower <=4
shadows can fit short-horizon force surprisingly well, but their snap
budget exceeds the declared position tolerance, so they are not legitimate
long-horizon substitutes for the admitted five-body channel.
