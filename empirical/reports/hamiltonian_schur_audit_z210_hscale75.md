# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 210 with primes `(2, 3, 5, 7)`
- State count: 210
- Hidden coordinate dimension: 209
- Phase-space dimension: 838
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- Target radius: 1.589760e+00
- Target-local pairs: 5457
- Target graph components: 1
- Complete stiffness alpha: 1.141421e+02

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.883333e+00 | -6.623525e-02 | 1.006323e-20 | 1.355789e-15 | 8.761007e-03 |
| K_target | 6.388115e-01 | 7.722757e-01 | 1.119305e-03 | 6.290696e-02 | 1.154753e-02 |
| K_eff_schur | 6.388115e-01 | 7.722757e-01 | 1.119305e-03 | 6.290696e-02 | 1.154753e-02 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 9.947598e-14
- relative |K_eff - K_target|: 2.376418e-15
- min eig(K_PP-K_target): 5.684342e-14
- min eig(K_full): 1.369391e-13
- second min eig(K_eff): 1.112581e+01
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 1.437775e-07

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
