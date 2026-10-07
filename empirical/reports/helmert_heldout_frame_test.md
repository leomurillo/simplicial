# Helmert Held-Out Frame Test

This audit tests whether mixed flags that can beat conductor on one
Fourier-pure displacement remain competitive when reused on held-out
Fourier directions in the same conductor support.

## Config

- `rows`: `['f2-u2', 'f2-u3', 'f4-u2']`
- `flags`: `500`
- `holdouts`: `25`
- `seed`: `20260515`
- `amplitude_fraction`: `0.35`
- `support`: `prefix`
- `skip_lowest`: `True`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`

## Summary

| row | packet | active dim | train wins | held-out wins | train wins that hold out | held-out lambda max | train margin median | hold-out margin median |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| F_2[u]/(u^2) | u^2 | 3 | 72/500 | 47/500 | 40/500 | 2773.2 | 0.269734 | 0.292809 |
| F_2[u]/(u^3) | u^2 | 3 | 0/500 | 0/500 | 0/500 | 0 | 2.22252 | 2.22906 |
| F_2[u]/(u^3) | u^3 | 7 | 0/500 | 0/500 | 0/500 | 0.270093 | 0.500582 | 0.556258 |
| F_4[u]/(u^2) | u^2 | 15 | 8/500 | 1/500 | 1/500 | 1.40442 | 0.161203 | 0.162579 |

## Reading

Negative margins mean the sampled mixed flag beats conductor.  If many
training wins disappear on held-out displacements, the mixed flags are
acting like one-point diagonalizers.  If they continue to win on held-out
directions, the current arithmetic ledger is missing a real reusable-frame
cost or the conductor claim must be narrowed further.
