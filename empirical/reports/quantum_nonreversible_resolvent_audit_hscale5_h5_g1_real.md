# Quantum Non-Reversible Projected Resolvent Audit

- Claim tested: non-reversible coherent sector contribution to projected Green kernel
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Operator dimension: 900
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Dissipator: `mean_field`
- Target radius: 1.609149e+00
- Target-local H pairs: 94

## Diagonal Gamma Shadow

- Gamma anisotropy: 6.546615e-15
- Gamma normalized q4: 1.353333e+00
- Gamma unit-symbol fourth: 2.800000e+00
- H-support unit-symbol fourth: 5.892019e-01

## Block Coupling

- ||L_PP||: 5.570860e+00
- ||L_PQ||: 3.872983e+01
- ||L_QP||: 3.872983e+01
- ||L_QQ||: 2.132604e+02
- ||Schur correction|| / ||L_PP||: 3.940532e+00

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_full | 6.250723e-01 | 1.481021e-01 | 1.768885e-02 | 1.181007e-16 | 2.388659e-01 |
| schur | 6.250723e-01 | 1.481021e-01 | 1.768885e-02 | 3.297795e-17 | 2.388659e-01 |
| projected_minus_diagonal | 6.250723e-01 | 1.481021e-01 | 6.147132e-03 | 1.181007e-16 | 7.854567e-01 |

## Schur Consistency

- max |projected full - Schur|: 1.836701e-16
- relative |projected full - Schur|: 1.417148e-15
- relative |projected full - diagonal only|: 7.927857e-01

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
