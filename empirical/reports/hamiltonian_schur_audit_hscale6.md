# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Hidden coordinate dimension: 29
- Phase-space dimension: 118
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Target radius: 1.930979e+00
- Target-local pairs: 118
- Target graph components: 2
- Complete stiffness alpha: 1.875000e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.800000e+00 | 2.461964e-01 | -3.926251e-18 | 4.597866e-16 | 5.333333e-02 |
| K_target | 8.038348e-01 | 7.027353e-01 | 2.312209e+15 | 1.447792e-16 | 7.779497e+14 |
| K_eff_schur | 8.038348e-01 | 7.027353e-01 | 5.844617e+12 | 3.125588e-15 | 1.966439e+12 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 3.730349e-14
- relative |K_eff - K_target|: 1.974729e-15
- min eig(K_PP-K_target): -3.336723e-16
- min eig(K_full): -7.198744e-15
- second min eig(K_eff): 3.312232e-14
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 5.601354e-08

## Interpretation

This is a conservative existence completion.  The audit builds a
Hamiltonian linear system L=JK whose hidden-coordinate Schur
complement exactly recovers the target-local stiffness, while the
uneliminated physical block K_PP is mean-field.  Therefore the
Schur localization mechanism is compatible with conservative
Hamiltonian algebra in finite row.

The caveat is essential: K_PQ is chosen by spectral factorization of
K_PP-K_target.  This proves finite Hamiltonian realizability, not
that CRT/Bures structure naturally supplies this coupling or that it
comes from K^CH(Deta v,Deta v).
