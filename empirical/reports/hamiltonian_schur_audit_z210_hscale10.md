# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 210 with primes `(2, 3, 5, 7)`
- State count: 210
- Hidden coordinate dimension: 209
- Phase-space dimension: 838
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- Target radius: 2.119680e+00
- Target-local pairs: 9053
- Target graph components: 1
- Complete stiffness alpha: 2.226810e+02

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.883333e+00 | -1.271105e-02 | 1.303597e-21 | 1.368857e-15 | 4.490728e-03 |
| K_target | 9.763077e-01 | 2.883754e-01 | -2.014076e-05 | 1.046692e-01 | 5.736790e-03 |
| K_eff_schur | 9.763077e-01 | 2.883754e-01 | -2.014076e-05 | 1.046692e-01 | 5.736790e-03 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 4.263256e-13
- relative |K_eff - K_target|: 3.215518e-15
- min eig(K_PP-K_target): 1.136868e-13
- min eig(K_full): -3.167746e-13
- second min eig(K_eff): 2.970614e+01
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 1.088019e-14

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
