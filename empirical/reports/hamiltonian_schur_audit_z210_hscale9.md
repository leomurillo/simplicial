# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 210 with primes `(2, 3, 5, 7)`
- State count: 210
- Hidden coordinate dimension: 209
- Phase-space dimension: 838
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- Target radius: 1.907712e+00
- Target-local pairs: 7177
- Target graph components: 1
- Complete stiffness alpha: 1.631939e+02

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.883333e+00 | -3.607170e-02 | -1.580911e-20 | 1.342728e-15 | 6.127680e-03 |
| K_target | 7.831359e-01 | 4.808817e-01 | 4.534776e-04 | 4.278511e-02 | 7.897970e-03 |
| K_eff_schur | 7.831359e-01 | 4.808817e-01 | 4.534776e-04 | 4.278511e-02 | 7.897970e-03 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 1.989520e-13
- relative |K_eff - K_target|: 2.644612e-15
- min eig(K_PP-K_target): -5.684342e-14
- min eig(K_full): -2.483600e-13
- second min eig(K_eff): 1.950022e+01
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 2.675637e-14

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
