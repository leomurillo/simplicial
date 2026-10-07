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
- ||L_PQ||: 3.872983e+01
- ||L_QP||: 3.872983e+01
- ||L_QQ||: 2.096604e+02
- ||Schur correction|| / ||L_PP||: 8.008888e+00

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_full | 8.408489e-01 | 1.825195e-01 | 8.920579e-02 | 0.000000e+00 | 1.847696e-01 |
| schur | 8.408489e-01 | 1.825195e-01 | 8.920579e-02 | 0.000000e+00 | 1.847696e-01 |
| projected_minus_diagonal | 8.408489e-01 | 1.825195e-01 | 3.871542e-02 | 0.000000e+00 | 8.512936e-01 |

## Schur Consistency

- max |projected full - Schur|: 1.665335e-16
- relative |projected full - Schur|: 2.133201e-15
- relative |projected full - diagonal only|: 8.525196e-01

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
