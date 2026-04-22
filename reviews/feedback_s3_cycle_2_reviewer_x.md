# Reviewer X — Formalism & Logic Audit — Cycle 2
**Scope:** §3 The Intrinsic Cross Product + Appendix A + Appendix B
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Resolution of Cycle 1 findings

- **[F-C-1]** RESOLVED — Appendix B Step 2 now correctly states that the off-diagonal entries of $\tilde K(u)$ are the six signed pairwise differences, each appearing twice (lines 190–195, 637–639), derives $\sum_{i<j}(u_i-u_j)^2 = (N-1)\sum_i u_i^2 - 2\sum_{i<j}u_i u_j$ and, using $\sum_i u_i = 0$, concludes $\sum_{i<j}(u_i-u_j)^2 = 4\sum_i u_i^2$ for $N=4$ (lines 641–647). Hence sum of squared entries is $8\sum_i u_i^2$, and $\mathrm{tr}(\tilde K^2) = -8\sum_i u_i^2$, $\mathrm{tr}(K^2) = \tfrac{1}{3}\mathrm{tr}(\tilde K^2) = -\tfrac{8}{3}\sum_i u_i^2 = -\tfrac{8}{3}\cdot\tfrac{3}{4} = -2$ is written out explicitly (lines 649–657).
- **[F-C-2]** RESOLVED — §3.1 line 205 states $c^2 = 3$; lines 207–209 derive $K = \tilde K/\sqrt{3}$ cleanly. Remark B.1 (line 663) gives the corrected unscaled spectrum $\{0,0,\pm i\sqrt{3}\}$ and $\tilde K^3 = -3\tilde K$.
- **[F-H-1]** RESOLVED — no "online supplementary computation file" or similar external dependency remains; the trace computation is fully in-text at lines 631–657.
- **[F-H-2]** RESOLVED — Corollary 3.4 now has an explicit proof at line 253: shows $\mathrm{im}\,K(u)|_H \subseteq u^\perp \cap H$ by simplicial skew-adjointness and $K(u)u = 0$, uses zero-sum preservation to keep the image in $H$, matches dimensions by rank-nullity on $H$, decomposes $P = \alpha u + P_\perp$, and applies Theorem 3.3 to obtain $K(u)^2 P = -P_\perp$. (The proof cites Corollary 3.5 for $K(u)v \in H$ rather than rederiving row/column-sum-zero; acceptable.)
- **[F-M-1]** RESOLVED — Appendix B Step 1 includes the explicit first-row computation of $K(u)u = 0$ and states the other rows follow by cyclic permutation (lines 623–627).
- **[F-M-2]** RESOLVED — Step 3 invokes that real skew matrices are normal and hence unitarily diagonalizable over $\mathbb{C}$, justifying the minimal-polynomial step (lines 659–661).
- **[F-M-3]** RESOLVED — Remark 3.2 separates the ambient $\mathbb{R}^4$ simplicial skew-symmetry claim from the zero-sum-unit-axis restrictions needed for the cubic identity (lines 232–237).
- **[F-M-4]** RESOLVED — §3.4 identifies $(H, \langle\cdot,\cdot\rangle)$ as a 3-dim oriented inner-product space, non-canonically *isometric* to $\mathbb{R}^3$, with the simplicial scaling absorbed into the form/normalization data (lines 261–269).
- **[F-L-1]** RESOLVED — §3.1 line 203 uses "spectral/trace computation"; Theorem 3.3's lead-in matches (line 245).

## Propagation check verification

Independent manuscript-wide sweep:

- `c^2 = 3/4` / unscaled wrong constant — no match; only corrected usages at lines 205, 207, 209, 245, 515, 631, 657.
- `\sqrt{3/4}` / `sqrt(3/4)` — no matches.
- `6 \sum`, `6\sum` in the Appendix B trace sense — no matches.
- `online supplementary` / `supplementary computation file` — no matches.
- Residual `3/4` occurrences are legitimate: unit-axis value $\sum u_i^2 = 3/4$ (line 653), and Appendix E's concrete $l$-axis example (lines 759, 761, 767, 768).

## New findings (Cycle 2)

### Critical / High / Medium
None.

### Low
- **[F-L-2] Out-of-scope wording lag in §1.2** — Contributions item 2 (line 51) still says the $1/\sqrt{3}$ scaling is derived "via the characteristic polynomial of the underlying rank-2 skew generator," but the revised manuscript consistently presents Appendix B as a spectral/trace computation (lines 203, 245). Propagation residue from the [F-L-1] rewording.

## Summary
All Cycle 1 Critical and High formalism findings are resolved. Appendix B is self-contained and correct, the unscaled constant is repaired consistently, and Corollary 3.4 now has the missing argument. One Low-severity out-of-scope propagation residue remains in §1.2 line 51.

STATUS: GREEN
