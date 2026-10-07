# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Hidden coordinate dimension: 29
- Phase-space dimension: 118
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Target radius: 2.896468e+00
- Target-local pairs: 323
- Target graph components: 1
- Complete stiffness alpha: 3.750000e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.800000e+00 | 1.774809e-01 | -1.630541e-18 | 5.078066e-16 | 2.666667e-02 |
| K_target | 1.856912e+00 | -1.448276e-01 | 9.338116e-19 | 4.310771e-16 | 3.333333e-02 |
| K_eff_schur | 1.856912e+00 | 1.873514e-01 | 1.211943e-17 | 3.113138e-15 | 3.333333e-02 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 3.552714e-14
- relative |K_eff - K_target|: 1.192901e-15
- min eig(K_PP-K_target): -3.552714e-15
- min eig(K_full): 7.105427e-15
- second min eig(K_eff): 1.379746e+01
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 1.189552e-08

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
