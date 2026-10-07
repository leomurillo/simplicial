# Helmert Local Rotation Obstruction

This diagnostic rotates the conductor flag by tiny cross-packet plane
rotations.  A boundary obstruction is present when the unpriced
one-point ledger \(J_0\) has a nonzero first derivative while packet
impurity is quadratic.  Then the break-even frame price scales like
`1/|theta|` near the conductor flag.

## Config

- `rows`: `['f2-u2']`
- `amplitudes`: `[0.35]`
- `thetas`: `[1e-06, 3e-06, 1e-05, 3e-05, 0.0001]`
- `epsilon`: `1e-07`
- `skip_lowest`: `True`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`

## Summary

| row | packet | amplitude | active dim | pairs | singular pairs | max lambda on grid | best pair | best theta | dJ0(0) | impurity theta^2 coeff | singular constant | max mu* (first-order cure) |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| F_2[u]/(u^2) | u^2 | 0.35 | 3 | 2 | 2 | 17425 | [0, 1] | 1e-06 | -0.0464663 | 2.66667 | 0.0174249 | 0.0232332 |

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
