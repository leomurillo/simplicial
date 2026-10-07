# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: PASS_LINEAR_SYMBOL
- Finest row: 30030
- Finest diagonal anisotropy: 5.807929e-01
- Finest Bures anisotropy: 3.086420e-13
- Finest global-complete control anisotropy: skipped
- Finest diagonal normalized fourth moment: 6.067441e-01
- Finest Bures normalized fourth moment: 1.361111e+00
- Kills/inconclusive flags: []

## Pre-registered Models

- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.
- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.
- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.

## Row Results

| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |
|---:|---|---:|---:|---:|---:|---:|
| 30 | `['p5:f1c', 'p5:f1s', 'p5:f2c']` | 4.472136e-01 | 2.220446e-16 | 1.110223e-16 | 5.803482e-01 | 1.361111e+00 |
| 210 | `['p7:f1c', 'p7:f1s', 'p7:f2c']` | 5.290771e-01 | 1.665335e-16 | 2.620126e-14 | 5.957371e-01 | 1.361111e+00 |
| 2310 | `['p11:f1c', 'p11:f1s', 'p11:f2c']` | 5.728784e-01 | 8.826273e-15 | skipped | 6.049898e-01 | 1.361111e+00 |
| 30030 | `['p13:f1c', 'p13:f1s', 'p13:f2c']` | 5.807929e-01 | 3.086420e-13 | skipped | 6.067441e-01 | 1.361111e+00 |

## Banded Sweep

| row | bandwidth | A | q4 | edges |
|---:|---|---:|---:|---:|
| 30 | `1` | 4.472136e-01 | 2.901741e+00 | 75 |
| 30 | `2` | 2.220446e-16 | 1.361111e+00 | 105 |
| 30 | `3` | 2.220446e-16 | 1.361111e+00 | 105 |
| 30 | `sqrt` | 2.220446e-16 | 1.361111e+00 | 105 |
| 30 | `pow:0.5` | 2.220446e-16 | 1.361111e+00 | 105 |
| 30 | `pow:0.75` | 2.220446e-16 | 1.361111e+00 | 105 |
| 30 | `frac:0.25` | 4.472136e-01 | 2.901741e+00 | 75 |
| 30 | `complete` | 2.220446e-16 | 1.361111e+00 | 105 |
| 210 | `1` | 5.290771e-01 | 4.170160e+00 | 735 |
| 210 | `2` | 3.228061e-01 | 2.219768e+00 | 1155 |
| 210 | `3` | 1.665335e-16 | 1.361111e+00 | 1365 |
| 210 | `sqrt` | 3.228061e-01 | 2.219768e+00 | 1155 |
| 210 | `pow:0.5` | 3.228061e-01 | 2.219768e+00 | 1155 |
| 210 | `pow:0.75` | 1.665335e-16 | 1.361111e+00 | 1365 |
| 210 | `frac:0.25` | 5.290771e-01 | 4.170160e+00 | 735 |
| 210 | `complete` | 1.665335e-16 | 1.361111e+00 | 1365 |
| 2310 | `1` | 5.728784e-01 | 6.654888e+00 | 10395 |
| 2310 | `2` | 5.015843e-01 | 4.091776e+00 | 17325 |
| 2310 | `3` | 3.801890e-01 | 2.620054e+00 | 21945 |
| 2310 | `sqrt` | 3.801890e-01 | 2.620054e+00 | 19635 |
| 2310 | `pow:0.5` | 3.801890e-01 | 2.620054e+00 | 19635 |
| 2310 | `pow:0.75` | 8.826273e-15 | 1.361111e+00 | 26565 |
| 2310 | `frac:0.25` | 5.015843e-01 | 4.091776e+00 | 12705 |
| 2310 | `complete` | 8.826273e-15 | 1.361111e+00 | 26565 |
| 30030 | `1` | 5.807929e-01 | 7.887673e+00 | 165165 |
| 30030 | `2` | 5.315262e-01 | 4.993148e+00 | 285285 |
| 30030 | `3` | 4.498068e-01 | 3.306796e+00 | 375375 |
| 30030 | `sqrt` | 4.498068e-01 | 3.306796e+00 | 345345 |
| 30030 | `pow:0.5` | 4.498068e-01 | 3.306796e+00 | 345345 |
| 30030 | `pow:0.75` | 3.086420e-13 | 1.361111e+00 | 525525 |
| 30030 | `frac:0.25` | 4.498068e-01 | 3.306796e+00 | 255255 |
| 30030 | `complete` | 3.086420e-13 | 1.361111e+00 | 525525 |

## Interpretation

A pass here is only a finite linear-symbol pass.  It does not prove
Mosco convergence.  A failure here is more serious: if the Bures
anisotropy does not improve before the limit, the Green-kernel program
cannot recover the isotropic Laplace principal symbol.  The normalized
fourth moment is reported separately because an all-pairs Bures graph
can make the second symbol scalar while still being too nonlocal for
a diffusion limit.
