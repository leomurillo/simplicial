# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Hidden coordinate dimension: 29
- Phase-space dimension: 118
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Target radius: 2.252809e+00
- Target-local pairs: 169
- Target graph components: 1
- Complete stiffness alpha: 2.438776e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.800000e+00 | 2.006764e-01 | -9.180223e-19 | 4.976531e-16 | 4.100418e-02 |
| K_target | 1.126488e+00 | 6.782634e-01 | 2.499335e-02 | 6.444480e-02 | 6.609793e-02 |
| K_eff_schur | 1.126488e+00 | 6.782634e-01 | 2.499335e-02 | 6.444480e-02 | 6.609793e-02 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 1.776357e-14
- relative |K_eff - K_target|: 1.650109e-15
- min eig(K_PP-K_target): -6.217249e-15
- min eig(K_full): 1.021405e-14
- second min eig(K_eff): 3.716012e+00
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 1.779973e-08

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
