# Quantum Non-Reversible Projected Resolvent Audit

- Claim tested: non-reversible coherent sector contribution to projected Green kernel
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Operator dimension: 900
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Dissipator: `mean_field`
- Target radius: 4.827447e-01
- Target-local H pairs: 0

## Diagonal Gamma Shadow

- Gamma anisotropy: 6.546615e-15
- Gamma normalized q4: 1.353333e+00
- Gamma unit-symbol fourth: 2.800000e+00
- H-support unit-symbol fourth: 0.000000e+00

## Block Coupling

- ||L_PP||: 5.570860e+00
- ||L_PQ||: 0.000000e+00
- ||L_QP||: 0.000000e+00
- ||L_QQ||: 8.848729e+01
- ||Schur correction|| / ||L_PP||: 0.000000e+00

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_full | 3.687500e-02 | 2.209599e-17 | 9.324711e-16 | 0.000000e+00 | 9.666667e-01 |
| schur | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_minus_diagonal | 9.352128e-04 | 2.211475e-17 | 5.408333e-05 | 0.000000e+00 | 4.996004e-16 |

## Schur Consistency

- max |projected full - Schur|: 4.996004e-16
- relative |projected full - Schur|: 5.256633e-16
- relative |projected full - diagonal only|: 5.256633e-16

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
