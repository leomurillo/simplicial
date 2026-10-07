# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: PASS_LINEAR_SYMBOL
- Finest row: 30030
- Finest diagonal anisotropy: 2.000000e-01
- Finest Bures anisotropy: 4.810596e-13
- Finest global-complete control anisotropy: skipped
- Finest diagonal normalized fourth moment: 3.437500e-01
- Finest Bures normalized fourth moment: 7.777778e-01
- Kills/inconclusive flags: []

## Pre-registered Models

- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.
- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.
- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.

## Row Results

| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |
|---:|---|---:|---:|---:|---:|---:|
| 6 | `['p2:h1', 'p3:h1', 'p3:h2']` | 2.000000e-01 | 1.110223e-16 | 2.220446e-16 | 3.437500e-01 | 8.888889e-01 |
| 30 | `['p2:h1', 'p3:h1', 'p5:h1']` | 2.000000e-01 | 4.996004e-16 | 3.885781e-15 | 3.437500e-01 | 7.777778e-01 |
| 210 | `['p2:h1', 'p3:h1', 'p5:h1']` | 2.000000e-01 | 4.996004e-16 | 7.438494e-14 | 3.437500e-01 | 7.777778e-01 |
| 2310 | `['p2:h1', 'p3:h1', 'p5:h1']` | 2.000000e-01 | 6.328271e-15 | skipped | 3.437500e-01 | 7.777778e-01 |
| 30030 | `['p2:h1', 'p3:h1', 'p5:h1']` | 2.000000e-01 | 4.810596e-13 | skipped | 3.437500e-01 | 7.777778e-01 |

## Banded Sweep

| row | bandwidth | A | q4 | edges |
|---:|---|---:|---:|---:|
| 6 | `1` | 1.110223e-16 | 8.888889e-01 | 9 |
| 6 | `2` | 1.110223e-16 | 8.888889e-01 | 9 |
| 6 | `sqrt` | 1.110223e-16 | 8.888889e-01 | 9 |
| 6 | `complete` | 1.110223e-16 | 8.888889e-01 | 9 |
| 30 | `1` | 2.500000e-01 | 9.615385e-01 | 75 |
| 30 | `2` | 4.996004e-16 | 7.777778e-01 | 105 |
| 30 | `sqrt` | 4.996004e-16 | 7.777778e-01 | 105 |
| 30 | `complete` | 4.996004e-16 | 7.777778e-01 | 105 |
| 210 | `1` | 2.500000e-01 | 9.615385e-01 | 735 |
| 210 | `2` | 4.996004e-16 | 7.777778e-01 | 1155 |
| 210 | `sqrt` | 4.996004e-16 | 7.777778e-01 | 1155 |
| 210 | `complete` | 4.996004e-16 | 7.777778e-01 | 1365 |
| 2310 | `1` | 2.500000e-01 | 9.615385e-01 | 10395 |
| 2310 | `2` | 6.328271e-15 | 7.777778e-01 | 17325 |
| 2310 | `sqrt` | 6.328271e-15 | 7.777778e-01 | 19635 |
| 2310 | `complete` | 6.328271e-15 | 7.777778e-01 | 26565 |
| 30030 | `1` | 2.500000e-01 | 9.615385e-01 | 165165 |
| 30030 | `2` | 4.810596e-13 | 7.777778e-01 | 285285 |
| 30030 | `sqrt` | 4.810596e-13 | 7.777778e-01 | 345345 |
| 30030 | `complete` | 4.810596e-13 | 7.777778e-01 | 525525 |

## Interpretation

A pass here is only a finite linear-symbol pass.  It does not prove
Mosco convergence.  A failure here is more serious: if the Bures
anisotropy does not improve before the limit, the Green-kernel program
cannot recover the isotropic Laplace principal symbol.  The normalized
fourth moment is reported separately because an all-pairs Bures graph
can make the second symbol scalar while still being too nonlocal for
a diffusion limit.
