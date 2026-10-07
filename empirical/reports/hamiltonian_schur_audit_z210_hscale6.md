# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 210 with primes `(2, 3, 5, 7)`
- State count: 210
- Hidden coordinate dimension: 209
- Phase-space dimension: 838
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- Target radius: 1.271808e+00
- Target-local pairs: 2437
- Target graph components: 1
- Complete stiffness alpha: 5.020266e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.883333e+00 | -1.989288e-02 | -1.074262e-19 | 1.305994e-15 | 1.991926e-02 |
| K_target | 3.819249e-01 | 3.118859e-01 | 4.346833e-03 | 7.472564e-01 | 3.308675e-02 |
| K_eff_schur | 3.819249e-01 | 3.118859e-01 | 4.346833e-03 | 7.472564e-01 | 3.308675e-02 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 5.329071e-14
- relative |K_eff - K_target|: 2.164023e-15
- min eig(K_PP-K_target): -2.131628e-14
- min eig(K_full): 5.250638e-14
- second min eig(K_eff): 2.000000e+00
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 6.994405e-15

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
