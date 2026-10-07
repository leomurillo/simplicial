# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: KILL_OR_INCONCLUSIVE
- Finest row: 30
- Finest diagonal anisotropy: 1.428571e-01
- Finest Bures anisotropy: 4.285714e-01
- Finest global-complete control anisotropy: 3.197442e-15
- Finest diagonal normalized fourth moment: 2.600000e-01
- Finest Bures normalized fourth moment: 2.450000e-01
- Kills/inconclusive flags: ['Bures anisotropy increased along the tested refinement', 'Bures anisotropy is not below diagonal anisotropy on the finest tested row', 'Bures principal-symbol anisotropy exceeds tolerance on the finest tested row']

## Pre-registered Models

- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.
- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.
- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.

## Row Results

| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |
|---:|---|---:|---:|---:|---:|---:|
| 6 | `['p2:h1', 'p3:h1', 'p3:h2']` | 1.428571e-01 | 2.000000e-01 | 7.401487e-17 | 2.600000e-01 | 3.437500e-01 |
| 30 | `['p2:h1', 'p3:h1', 'p5:h1']` | 1.428571e-01 | 4.285714e-01 | 3.197442e-15 | 2.600000e-01 | 2.450000e-01 |

## Interpretation

A pass here is only a finite linear-symbol pass.  It does not prove
Mosco convergence.  A failure here is more serious: if the Bures
anisotropy does not improve before the limit, the Green-kernel program
cannot recover the isotropic Laplace principal symbol.  The normalized
fourth moment is reported separately because an all-pairs Bures graph
can make the second symbol scalar while still being too nonlocal for
a diffusion limit.
