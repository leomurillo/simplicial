# Bures Hamiltonian Split Audit

- Claim tested: G_split gate for conservative Bures Hamiltonian Schur reduction
- Row: 30 with primes `(2, 3, 5)`
- State count: 30
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- Target radius: 2.252809e+00
- Target-local pairs: 169

## G_eq / G_J

- unitary orbit real dimension: 870
- matrix-unit pairs: 435
- rho condition: 1.433825e+01
- min |KKS weight|: 1.342136e-05
- max |KKS weight|: 1.012665e-01
- equilibrium residual ||-i[H_eq,rho]||: 0.000000e+00
- skew defect max |J+J^T|: 0.000000e+00
- rank J: 870

## G_split

| split | status | dim P | rank J_PP | cross/J | invariance defect |
|---|---|---:|---:|---:|---:|
| diagonal_readout | INVALID_EMPTY_OR_NOT_TANGENT | 0 | 0 | nan | nan |
| target_q_only | FAIL_SPLIT | 169 | 0 | 4.781582e-01 | 1.000000e+00 |
| target_symplectic_pairs | PASS_SYMPLECTIC_BLOCK | 338 | 338 | 0.000000e+00 | 0.000000e+00 |
| xi_q | FAIL_SPLIT | 3 | 0 | 6.415590e-02 | 1.000000e+00 |
| xi_once_closure | FAIL_SPLIT | 6 | 6 | 7.749945e-02 | 6.494896e-01 |

## Interpretation

The clean Hamiltonian Schur factorization is available only for a
nondegenerate J-invariant P sector.  Diagonal population readout is
not tangent to the unitary orbit.  Q-only or coordinate-only
readouts fail because their conjugate partners live in Q.  A split
made from complete matrix-unit quadrature pairs passes because it is
symplectically block-compatible by construction.

A PASS here does not prove localization or CRT canonicity.  It only
says the proposed P/Q split is eligible for a conservative Schur
stiffness audit.
