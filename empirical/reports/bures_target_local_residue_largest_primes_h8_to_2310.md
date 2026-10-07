# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: KILL_OR_INCONCLUSIVE
- Finest row: 2310
- Finest diagonal anisotropy: 3.333333e-01
- Finest Bures anisotropy: 2.564615e-14
- Finest global-complete control anisotropy: skipped
- Finest diagonal normalized fourth moment: 8.327160e-01
- Finest Bures normalized fourth moment: 7.905556e-01
- Finest target-local support residual: 9.727629e-01
- Finest target-local class-cone residual: 9.767551e-01
- Kills/inconclusive flags: ['Bures normalized fourth moment increased along the tested refinement']

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

## Target-Local Kernel

| row | radius | target edges | A | q4 | support residual | class residual | admissible fraction |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 2.574638e+00 | 281 | 1.689008e-01 | 6.637604e-02 | 8.047899e-01 | 8.153335e-01 | 3.523132e-01 |
| 210 | 1.695744e+00 | 5841 | 1.088986e-01 | 2.180711e-02 | 9.114163e-01 | 9.346629e-01 | 1.693203e-01 |
| 2310 | 1.099689e+00 | 271959 | 5.294703e-03 | 5.083107e-03 | 9.727629e-01 | 9.767551e-01 | 5.373236e-02 |

## Interpretation

The complete leg-local Bures model is the isotropic mean-field
endpoint; its normalized fourth moment is therefore the locality
obstruction.  The banded sweep exposes the source-local tradeoff:
narrow bands preserve some locality but remain anisotropic, while
isotropizing bands fall back to the complete-leg fourth-moment floor.
When `--target-local` is enabled, the final columns measure the new
bridge: distance from a target-local pushed kernel to the diagonal
shadow cone of Bures-admissible leg matrix units.
