# Helmert Local Rotation Obstruction

This diagnostic rotates the conductor flag by tiny cross-packet plane
rotations.  A boundary obstruction is present when the unpriced
one-point ledger \(J_0\) has a nonzero first derivative while packet
impurity is quadratic.  Then the break-even frame price scales like
`1/|theta|` near the conductor flag.

## Config

- `rows`: `['f2-u2', 'f2-u3', 'f4-u2']`
- `amplitudes`: `[0.1, 0.35, 0.5]`
- `thetas`: `[1e-05, 3e-05, 0.0001, 0.0003, 0.001, 0.003, 0.01]`
- `epsilon`: `1e-06`
- `skip_lowest`: `True`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`

## Summary

| row | packet | amplitude | active dim | pairs | singular pairs | max lambda on grid | best pair | best theta | dJ0(0) | impurity theta^2 coeff | singular constant | max mu* (first-order cure) |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| F_2[u]/(u^2) | u^2 | 0.1 | 3 | 2 | 2 | 32.7485 | [0, 1] | 1e-05 | -0.000873063 | 2.66667 | 0.000327398 | 0.000436543 |
| F_2[u]/(u^2) | u^2 | 0.35 | 3 | 2 | 2 | 1742.61 | [0, 1] | 1e-05 | -0.0464663 | 2.66667 | 0.0174249 | 0.0232333 |
| F_2[u]/(u^2) | u^2 | 0.5 | 3 | 2 | 2 | 6702.41 | [0, 1] | 1e-05 | -0.178722 | 2.66667 | 0.0670208 | 0.0893615 |
| F_2[u]/(u^3) | u^2 | 0.1 | 3 | 14 | 14 | 76.4131 | [0, 1] | 1e-05 | -0.000873063 | 1.14286 | 0.00076393 | 0.000436543 |
| F_2[u]/(u^3) | u^2 | 0.35 | 3 | 14 | 14 | 4066.1 | [0, 1] | 1e-05 | -0.0464663 | 1.14286 | 0.040658 | 0.0232333 |
| F_2[u]/(u^3) | u^2 | 0.5 | 3 | 14 | 14 | 15639 | [0, 1] | 1e-05 | -0.178722 | 1.14286 | 0.156382 | 0.0893615 |
| F_2[u]/(u^3) | u^3 | 0.1 | 7 | 14 | 14 | 57.3017 | [0, 3] | 1e-05 | -0.000654797 | 1.14286 | 0.000572947 | 0.000327403 |
| F_2[u]/(u^3) | u^3 | 0.35 | 7 | 14 | 14 | 3049.45 | [0, 3] | 1e-05 | -0.0348497 | 1.14286 | 0.0304935 | 0.0174249 |
| F_2[u]/(u^3) | u^3 | 0.5 | 7 | 14 | 14 | 11728.9 | [0, 3] | 1e-05 | -0.134042 | 1.14286 | 0.117286 | 0.0670209 |
| F_4[u]/(u^2) | u^2 | 0.1 | 15 | 36 | 36 | 2413.37 | [0, 3] | -1e-05 | 0.0128712 | 0.533333 | 0.0241335 | 0.00643561 |
| F_4[u]/(u^2) | u^2 | 0.35 | 15 | 36 | 36 | 20412.8 | [0, 13] | -1e-05 | 0.108868 | 0.533333 | 0.204128 | 0.054434 |
| F_4[u]/(u^2) | u^2 | 0.5 | 15 | 36 | 36 | 42902.4 | [0, 3] | -1e-05 | 0.228813 | 0.533333 | 0.429025 | 0.114407 |

## Reading

If `singular pairs` is nonzero, the conductor flag is not stationary for
the unpriced one-point objective in at least one cross-packet direction.
Because packet impurity is quadratic at the conductor flag, the sampled
frame-price frontier can become arbitrarily large near that direction
(Theorem 3.3 of paper 25).  The rightmost column `max mu* (first-order
cure)` is the per-row maximum of (one-sided descent rate of J0) / nu(A)
over sampled plane directions, where nu(A)=2 for cross-packet plane
rotations.  Only pairs with an actual descent direction contribute;
kinky pairs whose central derivative is nonzero but whose one-sided
rate is nonpositive in both directions contribute 0.  By Theorem 3.5
of paper 25, augmenting the ledger with the first-order packet cost
N(Q)=sum_{a!=b}||P_a Q P_b||_F at weight mu >= max mu* restores local
minimality at the conductor flag with bounded required price.  This
refines the theorem by excluding or separately pricing one-point local
diagonalizers.  Compare: under quadratic-only impurity, the sampled
max lambda diverges (column `max lambda on grid` blows up as theta
shrinks); under first-order impurity, mu* remains finite.
