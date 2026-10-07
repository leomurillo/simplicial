# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: KILL_OR_INCONCLUSIVE
- Finest row: 30030
- Finest diagonal anisotropy: 5.334772e-01
- Finest Bures anisotropy: 6.300516e-13
- Finest global-complete control anisotropy: skipped
- Finest diagonal normalized fourth moment: 3.198660e-01
- Finest Bures normalized fourth moment: 7.500000e-01
- Kills/inconclusive flags: ['Bures normalized fourth moment increased along the tested refinement']

## Pre-registered Models

- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.
- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.
- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.

## Row Results

| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |
|---:|---|---:|---:|---:|---:|---:|
| 30 | `['p5:f1c', 'p3:f1c', 'p2:f1r']` | 3.692484e-01 | 5.551115e-17 | 1.887379e-15 | 2.991045e-01 | 7.222222e-01 |
| 210 | `['p7:f1c', 'p5:f1c', 'p3:f1c']` | 5.987123e-01 | 1.165734e-15 | 1.521561e-13 | 3.264421e-01 | 7.500000e-01 |
| 2310 | `['p11:f1c', 'p7:f1c', 'p5:f1c']` | 6.263600e-01 | 4.457545e-14 | skipped | 3.214239e-01 | 7.500000e-01 |
| 30030 | `['p13:f1c', 'p11:f1c', 'p7:f1c']` | 5.334772e-01 | 6.300516e-13 | skipped | 3.198660e-01 | 7.500000e-01 |

## Banded Sweep

| row | bandwidth | A | q4 | edges |
|---:|---|---:|---:|---:|
| 30 | `1` | 5.669153e-01 | 8.754350e-01 | 75 |
| 30 | `2` | 5.551115e-17 | 7.222222e-01 | 105 |
| 30 | `3` | 5.551115e-17 | 7.222222e-01 | 105 |
| 30 | `sqrt` | 5.551115e-17 | 7.222222e-01 | 105 |
| 30 | `pow:0.5` | 5.551115e-17 | 7.222222e-01 | 105 |
| 30 | `pow:0.75` | 5.551115e-17 | 7.222222e-01 | 105 |
| 30 | `frac:0.25` | 5.669153e-01 | 8.754350e-01 | 75 |
| 30 | `complete` | 5.551115e-17 | 7.222222e-01 | 105 |
| 210 | `1` | 8.057479e-01 | 1.355996e+00 | 735 |
| 210 | `2` | 3.728098e-01 | 8.616823e-01 | 1155 |
| 210 | `3` | 1.165734e-15 | 7.500000e-01 | 1365 |
| 210 | `sqrt` | 3.728098e-01 | 8.616823e-01 | 1155 |
| 210 | `pow:0.5` | 3.728098e-01 | 8.616823e-01 | 1155 |
| 210 | `pow:0.75` | 1.165734e-15 | 7.500000e-01 | 1365 |
| 210 | `frac:0.25` | 8.057479e-01 | 1.355996e+00 | 735 |
| 210 | `complete` | 1.165734e-15 | 7.500000e-01 | 1365 |
| 2310 | `1` | 8.108933e-01 | 2.077707e+00 | 10395 |
| 2310 | `2` | 7.618799e-01 | 1.203918e+00 | 17325 |
| 2310 | `3` | 4.893754e-01 | 9.029008e-01 | 21945 |
| 2310 | `sqrt` | 4.893754e-01 | 1.051952e+00 | 19635 |
| 2310 | `pow:0.5` | 4.893754e-01 | 1.051952e+00 | 19635 |
| 2310 | `pow:0.75` | 4.457545e-14 | 7.500000e-01 | 26565 |
| 2310 | `frac:0.25` | 4.396696e-01 | 1.659850e+00 | 12705 |
| 2310 | `complete` | 4.457545e-14 | 7.500000e-01 | 26565 |
| 30030 | `1` | 7.184881e-01 | 2.976907e+00 | 165165 |
| 30030 | `2` | 6.891568e-01 | 1.853943e+00 | 285285 |
| 30030 | `3` | 6.401835e-01 | 1.200772e+00 | 375375 |
| 30030 | `sqrt` | 3.511913e-01 | 1.330527e+00 | 345345 |
| 30030 | `pow:0.5` | 3.511913e-01 | 1.330527e+00 | 345345 |
| 30030 | `pow:0.75` | 6.300516e-13 | 7.500000e-01 | 525525 |
| 30030 | `frac:0.25` | 3.419526e-01 | 1.804837e+00 | 255255 |
| 30030 | `complete` | 6.300516e-13 | 7.500000e-01 | 525525 |

## Interpretation

A pass here is only a finite linear-symbol pass.  It does not prove
Mosco convergence.  A failure here is more serious: if the Bures
anisotropy does not improve before the limit, the Green-kernel program
cannot recover the isotropic Laplace principal symbol.  The normalized
fourth moment is reported separately because an all-pairs Bures graph
can make the second symbol scalar while still being too nonlocal for
a diffusion limit.
