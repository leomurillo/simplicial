# Quantum Non-Reversible Projected Resolvent Audit

- Claim tested: non-reversible coherent sector contribution to projected Green kernel
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Operator dimension: 900
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Dissipator: `mean_field`
- Target radius: 1.287319e+00
- Target-local H pairs: 44

## Diagonal Gamma Shadow

- Gamma anisotropy: 6.546615e-15
- Gamma normalized q4: 1.353333e+00
- Gamma unit-symbol fourth: 2.800000e+00
- H-support unit-symbol fourth: 4.047619e-01

## Block Coupling

- ||L_PP||: 5.570860e+00
- ||L_PQ||: 2.323790e+01
- ||L_QP||: 2.323790e+01
- ||L_QQ||: 3.469726e+02
- ||Schur correction|| / ||L_PP||: 1.589025e+00

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_full | 8.324423e-01 | 1.566860e-01 | 2.345620e+00 | 0.000000e+00 | 3.932011e-01 |
| schur | 8.324423e-01 | 1.566860e-01 | 2.345620e+00 | 0.000000e+00 | 3.932011e-01 |
| projected_minus_diagonal | 8.324423e-01 | 1.566860e-01 | 6.879927e-02 | 0.000000e+00 | 6.548124e-01 |

## Schur Consistency

- max |projected full - Schur|: 4.996004e-16
- relative |projected full - Schur|: 1.539187e-15
- relative |projected full - diagonal only|: 6.317616e-01

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
