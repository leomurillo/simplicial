# Bures Isotropization Linear Audit

- Claim tested: finite-n linearization of the CRT/Bures isotropization lemma
- Status: PASS_LINEAR_SYMBOL
- Finest row: 210
- Finest diagonal anisotropy: 2.000000e-01
- Finest Bures anisotropy: 4.996004e-16
- Finest global-complete control anisotropy: 7.438494e-14
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

## Interpretation

A pass here is only a finite linear-symbol pass.  It does not prove
Mosco convergence.  A failure here is more serious: if the Bures
anisotropy does not improve before the limit, the Green-kernel program
cannot recover the isotropic Laplace principal symbol.  The normalized
fourth moment is reported separately because an all-pairs Bures graph
can make the second symbol scalar while still being too nonlocal for
a diffusion limit.
