# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 210 with primes `(2, 3, 5, 7)`
- State count: 210
- Hidden coordinate dimension: 209
- Phase-space dimension: 838
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- Target radius: 1.059840e+00
- Target-local pairs: 1677
- Target graph components: 3
- Complete stiffness alpha: 3.212178e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.883333e+00 | -4.603204e-03 | -1.152593e-19 | 1.349963e-15 | 3.113152e-02 |
| K_target | 2.459596e-01 | 1.540405e-02 | 5.612590e+14 | 8.852202e+14 | 1.028245e+15 |
| K_eff_schur | 2.459596e-01 | 4.022561e-02 | 3.988616e+11 | 5.419228e+13 | 4.365287e+11 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 4.973799e-14
- relative |K_eff - K_target|: 2.190332e-15
- min eig(K_PP-K_target): 0.000000e+00
- min eig(K_full): -9.010615e-14
- second min eig(K_eff): 4.099393e-14
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 6.033959e-08

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
