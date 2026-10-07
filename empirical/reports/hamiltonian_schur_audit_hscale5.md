# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Hidden coordinate dimension: 29
- Phase-space dimension: 118
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Target radius: 1.609149e+00
- Target-local pairs: 94
- Target graph components: 2
- Complete stiffness alpha: 1.412847e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.800000e+00 | 8.779762e-02 | -3.804428e-19 | 6.013420e-16 | 7.077907e-02 |
| K_target | 5.892019e-01 | 7.027353e-01 | 3.059548e+15 | 1.423337e-16 | 1.029394e+15 |
| K_eff_schur | 5.892019e-01 | 7.027353e-01 | -1.419414e+13 | 9.912330e-16 | 4.775663e+12 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 1.421085e-14
- relative |K_eff - K_target|: 1.638755e-15
- min eig(K_PP-K_target): 8.850537e-16
- min eig(K_full): 9.488030e-17
- second min eig(K_eff): 1.181319e-14
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 4.198622e-08

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
