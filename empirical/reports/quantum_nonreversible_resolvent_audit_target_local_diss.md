# Quantum Non-Reversible Projected Resolvent Audit

- Claim tested: non-reversible coherent sector contribution to projected Green kernel
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Operator dimension: 900
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Dissipator: `target_local`
- Target radius: 2.574638e+00
- Target-local H pairs: 281

## Diagonal Gamma Shadow

- Gamma anisotropy: 1.689008e-01
- Gamma normalized q4: 6.637604e-02
- Gamma unit-symbol fourth: 1.649076e+00
- H-support unit-symbol fourth: 1.649076e+00

## Block Coupling

- ||L_PP||: 1.070887e+02
- ||L_PQ||: 7.745967e+00
- ||L_QP||: 7.745967e+00
- ||L_QQ||: 6.172180e+02
- ||Schur correction|| / ||L_PP||: 4.964487e-03

## Kernel Fits

| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |
|---|---:|---:|---:|---:|---:|
| diagonal_only | 2.492773e-01 | 5.479649e-04 | 3.363427e-02 | 0.000000e+00 | 4.129850e-02 |
| projected_full | 2.474078e-01 | 5.451326e-04 | 3.409210e-02 | 7.194510e-22 | 4.111434e-02 |
| schur | 2.474078e-01 | 5.451326e-04 | 3.409210e-02 | 4.710386e-22 | 4.111434e-02 |
| projected_minus_diagonal | 2.594980e-01 | -2.832317e-06 | 1.376090e-01 | 7.194510e-22 | 1.843152e-04 |

## Schur Consistency

- max |projected full - Schur|: 1.387779e-17
- relative |projected full - Schur|: 3.838894e-16
- relative |projected full - diagonal only|: 4.421839e-03

## Interpretation

This audit measures the non-symmetric resolvent projected back to the
diagonal physical readout.  A coherent-sector localization signal
would appear as a strong 1/r fit in `projected_full` and `schur` while
the diagonal Gamma shadow remains nonlocal.  Agreement between
`projected_full` and `schur` verifies that any effect is carried by
the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma
calculation on diagonal observables.
