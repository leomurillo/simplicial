# Quantum Non-Reversible Projected Resolvent Audit

- Claim tested: non-reversible coherent sector contribution to projected Green kernel
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Operator dimension: 900
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Dissipator: `leg_complete`
- Target radius: 2.574638e+00
- Target-local H pairs: 281

## Diagonal Gamma Shadow

- Gamma anisotropy: 4.285714e-01
- Gamma normalized q4: 2.250000e-01
- Gamma unit-symbol fourth: 1.500000e+00
- H-support unit-symbol fourth: 1.649076e+00

## Block Coupling

- ||L_PP||: 4.098780e+01
- ||L_PQ||: 7.745967e+00
- ||L_QP||: 7.745967e+00
- ||L_QQ||: 2.686075e+02
- ||Schur correction|| / ||L_PP||: 2.982564e-02

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | 6.079459e-01 | 7.670065e-02 | 7.624611e-01 | 0.000000e+00 | 1.801190e-01 |
| projected_full | 6.095128e-01 | 6.905599e-02 | 8.089739e-01 | 1.104218e-19 | 1.700135e-01 |
| schur | 6.095128e-01 | 6.905599e-02 | 8.089739e-01 | 1.010512e-19 | 1.700135e-01 |
| projected_minus_diagonal | 5.799107e-01 | -7.644661e-03 | 6.789409e-01 | 1.104218e-19 | 1.055117e-02 |

## Schur Consistency

- max |projected full - Schur|: 2.775638e-17
- relative |projected full - Schur|: 3.195567e-16
- relative |projected full - diagonal only|: 6.702506e-02

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
