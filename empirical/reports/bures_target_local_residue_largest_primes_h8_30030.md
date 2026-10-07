# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: PASS_LINEAR_SYMBOL
- Finest row: 30030
- Finest diagonal anisotropy: 2.727273e-01
- Finest Bures anisotropy: 1.183165e-12
- Finest global-complete control anisotropy: skipped
- Finest diagonal normalized fourth moment: 1.280693e+00
- Finest Bures normalized fourth moment: 7.953175e-01
- Finest target-local support residual: 9.933233e-01
- Finest target-local class-cone residual: 9.937966e-01
- Kills/inconclusive flags: []

## Pre-registered Models

- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.
- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.
- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.

## Row Results

| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |
|---:|---|---:|---:|---:|---:|---:|
| 30030 | `['p13:res', 'p11:res', 'p7:res']` | 2.727273e-01 | 1.183165e-12 | skipped | 1.280693e+00 | 7.953175e-01 |

## Banded Sweep

| row | bandwidth | A | q4 | edges |
|---:|---|---:|---:|---:|
| 30030 | `1` | 5.294118e-01 | 1.130549e+01 | 165165 |
| 30030 | `2` | 5.072464e-01 | 3.312970e+00 | 285285 |
| 30030 | `sqrt` | 2.380952e-01 | 2.257314e+00 | 345345 |
| 30030 | `complete` | 1.183165e-12 | 7.953175e-01 | 525525 |

## Target-Local Kernel

| row | radius | target edges | A | q4 | support residual | class residual | admissible fraction |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30030 | 7.997335e-01 | 17720835 | 1.438637e-01 | 1.022762e-03 | 9.933233e-01 | 9.937966e-01 | 1.330891e-02 |

## Interpretation

The complete leg-local Bures model is the isotropic mean-field
endpoint; its normalized fourth moment is therefore the locality
obstruction.  The banded sweep exposes the source-local tradeoff:
narrow bands preserve some locality but remain anisotropic, while
isotropizing bands fall back to the complete-leg fourth-moment floor.
When `--target-local` is enabled, the final columns measure the new
bridge: distance from a target-local pushed kernel to the diagonal
shadow cone of Bures-admissible leg matrix units.
