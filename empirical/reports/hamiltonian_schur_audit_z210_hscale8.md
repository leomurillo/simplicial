# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 210 with primes `(2, 3, 5, 7)`
- State count: 210
- Hidden coordinate dimension: 209
- Phase-space dimension: 838
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- Target radius: 1.695744e+00
- Target-local pairs: 5841
- Target graph components: 1
- Complete stiffness alpha: 1.239239e+02

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.883333e+00 | -3.266106e-04 | -1.471619e-20 | 1.364834e-15 | 8.069465e-03 |
| K_target | 6.691668e-01 | 7.342419e-01 | 9.164851e-04 | 3.228602e-02 | 1.055444e-02 |
| K_eff_schur | 6.691668e-01 | 7.342419e-01 | 9.164851e-04 | 3.228602e-02 | 1.055444e-02 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 1.181277e-13
- relative |K_eff - K_target|: 2.523105e-15
- min eig(K_PP-K_target): 1.421085e-14
- min eig(K_full): -2.273737e-13
- second min eig(K_eff): 1.333063e+01
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 2.087219e-14

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
