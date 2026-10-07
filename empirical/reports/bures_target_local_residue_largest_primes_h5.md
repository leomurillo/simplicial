# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: KILL_OR_INCONCLUSIVE
- Finest row: 30030
- Finest diagonal anisotropy: 2.727273e-01
- Finest Bures anisotropy: 1.183165e-12
- Finest global-complete control anisotropy: skipped
- Finest diagonal normalized fourth moment: 1.280693e+00
- Finest Bures normalized fourth moment: 7.953175e-01
- Finest target-local support residual: 9.774950e-01
- Finest target-local class-cone residual: 9.781508e-01
- Kills/inconclusive flags: ['Bures anisotropy increased along the tested refinement', 'Bures normalized fourth moment increased along the tested refinement']

## Pre-registered Models

- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.
- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.
- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.

## Row Results

| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |
|---:|---|---:|---:|---:|---:|---:|
| 30 | `['p5:res', 'p3:res', 'p2:res']` | 2.000000e-01 | 1.665335e-16 | 2.553513e-15 | 3.520408e-01 | 7.333333e-01 |
| 210 | `['p7:res', 'p5:res', 'p3:res']` | 3.333333e-01 | 2.220446e-15 | 5.262457e-14 | 4.511834e-01 | 7.750000e-01 |
| 2310 | `['p11:res', 'p7:res', 'p5:res']` | 3.333333e-01 | 2.564615e-14 | skipped | 8.327160e-01 | 7.905556e-01 |
| 30030 | `['p13:res', 'p11:res', 'p7:res']` | 2.727273e-01 | 1.183165e-12 | skipped | 1.280693e+00 | 7.953175e-01 |

## Banded Sweep

| row | bandwidth | A | q4 | edges |
|---:|---|---:|---:|---:|
| 30 | `1` | 4.285714e-01 | 9.635417e-01 | 75 |
| 30 | `2` | 1.665335e-16 | 7.333333e-01 | 105 |
| 30 | `sqrt` | 1.665335e-16 | 7.333333e-01 | 105 |
| 30 | `complete` | 1.665335e-16 | 7.333333e-01 | 105 |
| 210 | `1` | 6.470588e-01 | 1.680926e+00 | 735 |
| 210 | `2` | 2.727273e-01 | 9.495370e-01 | 1155 |
| 210 | `sqrt` | 2.727273e-01 | 9.495370e-01 | 1155 |
| 210 | `complete` | 2.220446e-15 | 7.750000e-01 | 1365 |
| 2310 | `1` | 6.296296e-01 | 5.115614e+00 | 10395 |
| 2310 | `2` | 5.942029e-01 | 1.496736e+00 | 17325 |
| 2310 | `sqrt` | 3.580247e-01 | 1.322206e+00 | 19635 |
| 2310 | `complete` | 2.564615e-14 | 7.905556e-01 | 26565 |
| 30030 | `1` | 5.294118e-01 | 1.130549e+01 | 165165 |
| 30030 | `2` | 5.072464e-01 | 3.312970e+00 | 285285 |
| 30030 | `sqrt` | 2.380952e-01 | 2.257314e+00 | 345345 |
| 30030 | `complete` | 1.183165e-12 | 7.953175e-01 | 525525 |

## Target-Local Kernel

| row | radius | target edges | A | q4 | support residual | class residual | admissible fraction |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 1.609149e+00 | 94 | 1.000000e+00 | 1.867189e-01 | 5.834600e-01 | 7.341710e-01 | 6.595745e-01 |
| 210 | 1.059840e+00 | 1677 | 1.000000e+00 | 7.825987e-02 | 8.002683e-01 | 8.374691e-01 | 3.595707e-01 |
| 2310 | 6.873054e-01 | 63195 | 1.000000e+00 | 2.309192e-02 | 9.223341e-01 | 9.293195e-01 | 1.492998e-01 |
| 30030 | 4.998334e-01 | 3598035 | 1.000000e+00 | 5.323309e-03 | 9.774950e-01 | 9.781508e-01 | 4.450346e-02 |

## Interpretation

A pass here is only a finite linear-symbol pass.  It does not prove
Mosco convergence.  A failure here is more serious: if the Bures
anisotropy does not improve before the limit, the Green-kernel program
cannot recover the isotropic Laplace principal symbol.  The normalized
fourth moment is reported separately because an all-pairs Bures graph
can make the second symbol scalar while still being too nonlocal for
a diffusion limit.
