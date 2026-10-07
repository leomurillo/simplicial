# Four-Body Snap Budget Audit

This is a controlled Paper 28 scaffold, not a claim about real gravitation.
The admitted tetrahedral feature is tested against lower edge-plus-face shadows.

## Configuration

- trials: `16`
- steps: `1400`
- dt: `0.0015`
- sample_stride: `20`
- replay_steps: `1400`
- masses: `[1.0, 1.18, 0.9, 1.07]`
- gravity: `0.38`
- softening: `0.18`
- beta: `0.08`
- gamma: `1.0`
- jerk_scale: `0.01`
- position_tolerance: `1e-06`

## Short-Horizon Fit

| model | rank | force test R2 | force test RMSE | jerk test R2 | snap test R2 |
|---|---:|---:|---:|---:|---:|
| lower_force_only | 40 | 0.35115 | 0.000397958 | 0.129112 | -0.0697014 |
| lower_jerk_aware | 40 | 0.357354 | 0.000396051 | 0.135436 | -0.0541251 |
| tetra_one_coeff | 1 | 1 | 6.890280e-17 | 1 | 1 |

## Long-Horizon Replay

| model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |
|---|---:|---:|---:|---:|
| pairwise_null | 0.000623707 | 0.000623707 | 0.00114862 | 0.00177716 |
| lower_force_only | 0.000223834 | 0.000223834 | 0.000543259 | 0.00060992 |
| lower_jerk_aware | 0.000213593 | 0.000213593 | 0.000533922 | 0.000566606 |
| recovered_tetra | 0 | 0 | 0 | 4.006172e-18 |

## Snap Budget

| model | acc term | jerk term | snap term | total budget | snap/tol | total/tol |
|---|---:|---:|---:|---:|---:|---:|
| lower_force_only | 0.000832562 | 0.0058062 | 0.0688825 | 0.0755213 | 68882.5 | 75521.3 |
| lower_jerk_aware | 0.000831244 | 0.00577362 | 0.0677726 | 0.0743775 | 67772.6 | 74377.5 |
| recovered_tetra | 2.311905e-17 | 7.563061e-15 | 9.265725e-12 | 9.273311e-12 | 9.265725e-06 | 9.273311e-06 |

## Reading

If the admitted tetrahedral model keeps snap/tolerance near numerical zero,
snap is not mandatory after the correct 4-ary coordinate is admitted.
