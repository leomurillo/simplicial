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
- ||L_PQ||: 7.745967e+01
- ||L_QP||: 7.745967e+01
- ||L_QQ||: 4.141014e+02
- ||Schur correction|| / ||L_PP||: 2.068430e+01

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | -5.992011e-03 | -7.925476e-18 | 2.610919e-15 | 0.000000e+00 | 9.666667e-01 |
| projected_full | 8.131115e-01 | 1.887682e-01 | 8.741459e-02 | 0.000000e+00 | 1.382075e-01 |
| schur | 8.131115e-01 | 1.887682e-01 | 8.741459e-02 | 0.000000e+00 | 1.382075e-01 |
| projected_minus_diagonal | 8.131115e-01 | 1.887682e-01 | 3.954326e-02 | 0.000000e+00 | 9.004583e-01 |

## Schur Consistency

- max |projected full - Schur|: 9.020562e-17
- relative |projected full - Schur|: 1.070218e-15
- relative |projected full - diagonal only|: 9.031000e-01

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
