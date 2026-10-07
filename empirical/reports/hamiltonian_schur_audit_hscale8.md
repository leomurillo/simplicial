# Hamiltonian L=JK Schur Audit

- Claim tested: conservative Hamiltonian Schur completion for Green-kernel localization
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- Hidden coordinate dimension: 29
- Phase-space dimension: 118
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Target radius: 2.574638e+00
- Target-local pairs: 281
- Target graph components: 1
- Complete stiffness alpha: 3.296765e+01

## Kernel Fits

| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |
|---|---:|---:|---:|---:|---:|
| K_PP_complete | 2.800000e+00 | -4.361371e-02 | -4.011279e-19 | 4.933801e-16 | 3.033276e-02 |
| K_target | 1.649076e+00 | 2.492773e-01 | 5.479649e-04 | 3.363427e-02 | 4.129850e-02 |
| K_eff_schur | 1.649076e+00 | 2.492773e-01 | 5.479649e-04 | 3.363427e-02 | 4.129850e-02 |

## Schur And Hamiltonian Checks

- max |K_eff - K_target|: 2.486900e-14
- relative |K_eff - K_target|: 1.065205e-15
- min eig(K_PP-K_target): -5.756090e-15
- min eig(K_full): 6.661338e-16
- second min eig(K_eff): 9.806332e+00
- max |J+J^T|: 0.000000e+00
- max |H-H^T|: 0.000000e+00
- max |L^T H + H L|: 0.000000e+00
- max |Re eig(L)|: 4.952852e-08

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
