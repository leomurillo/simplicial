# Quantum Non-Reversible Resolvent Sweep Summary

All rows below use `Z30`, a mean-field diagonal dissipator, and the full
projected non-symmetric resolvent on `M_30(C)`.

| run | H pairs | Gamma unit fourth | diagonal R2 | projected R2 | Schur relative error |
|---|---:|---:|---:|---:|---:|
| `hscale4_h3_g5_real` | 44 | 2.800000 | -0.005992 | 0.879732 | 8.16e-16 |
| `hscale4_h3_g2_real` | 44 | 2.800000 | -0.005992 | 0.852222 | 1.56e-15 |
| `hscale4_h3_g1_real` | 44 | 2.800000 | -0.005992 | 0.849320 | 8.09e-16 |
| `hscale4_h5_g05_real` | 44 | 2.800000 | -0.005992 | 0.840849 | 2.13e-15 |
| `hscale4_h3_g10_real` | 44 | 2.800000 | -0.005992 | 0.832442 | 1.54e-15 |
| `hscale8_default` | 281 | 2.800000 | -0.005992 | 0.047736 | 2.49e-16 |

Interpretation: the diagonal Gamma shadow remains mean-field and nonlocal in
all listed runs.  The projected Green kernel can nevertheless become strongly
`1/r`-like on `Z30` when the coherent Hamiltonian support is mid-radius and the
Schur correction dominates.  The full projected resolvent and Schur-complement
resolvent agree to machine precision, so the signal is genuinely carried by
`L_PQ L_QQ^{-1} L_QP`, not by a diagonal Gamma computation.

This is a finite positive signal for the coherent non-equilibrium route, not a
continuum theorem.  The next required audit is refinement: build a sparse or
structured Schur solver for `Z210` and test whether the projected R2 and shell
isotropy improve, persist, or collapse under conductor-compatible scaling.
