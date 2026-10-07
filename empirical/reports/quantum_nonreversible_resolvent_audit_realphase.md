# Quantum Non-Reversible Projected Resolvent Audit

- Claim tested: non-reversible coherent sector contribution to projected Green kernel
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Operator dimension: 900
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Dissipator: `mean_field`
- Target radius: 2.574638e+00
- Target-local H pairs: 281

## Diagonal Gamma Shadow

- Gamma anisotropy: 6.546615e-15
- Gamma normalized q4: 1.353333e+00
- Gamma unit-symbol fourth: 2.800000e+00
- H-support unit-symbol fourth: 1.649076e+00

## Block Coupling

- ||L_PP||: 5.570860e+00
- ||L_PQ||: 7.745967e+00
- ||L_QP||: 7.745967e+00
- ||L_QQ||: 9.751923e+01
- ||Schur correction|| / ||L_PP||: 3.318622e-01

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_full | 1.412868e-01 | 1.655651e-03 | 1.112161e-02 | 1.428678e-17 | 7.229087e-01 |
| schur | 1.412868e-01 | 1.655651e-03 | 1.112161e-02 | 7.197982e-18 | 7.229087e-01 |
| projected_minus_diagonal | 1.412868e-01 | 1.655651e-03 | 3.589987e-02 | 1.428678e-17 | 2.478837e-01 |

## Schur Consistency

- max |projected full - Schur|: 2.290306e-16
- relative |projected full - Schur|: 4.142692e-16
- relative |projected full - diagonal only|: 2.538471e-01

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
