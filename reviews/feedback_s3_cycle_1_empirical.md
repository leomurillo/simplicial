# Empirical Validation — Appendix B Constants — Cycle 1
**Scope:** symbolic verification of trace/spectrum/minimal polynomial constants in Appendix B and §3.1
**Skeptical:** empirical-skeptical (composer-2-fast)
**Reviewer:** empirical-reviewer (claude-opus-4-7-thinking-high)
**Artifacts:** `empirical/verify_appendix_b_constants.py`, `empirical/reports/appendix_b_constants.md`
**Date:** 2026-04-20

## Why this was run

Reviewer X's Cycle 1 finding [F-C-1] alleged an arithmetic error in Appendix B (sum of squared entries of `\tilde K` should be `8·sum(u_i^2)`, not the manuscript's `6·sum(u_i^2)`), which if correct cascades into the unscaled cubic constant claimed on line 205 and Remark B.1 (`c^2 = 3/4` and `\tilde K^3 = -(3/4)\tilde K`). Per the global rule that "All code generated for empirical validation must be explicitly reviewed before its conclusions are fed back to the Author," the Skeptical built a SymPy verification and the Empirical Reviewer audited it before its conclusions were used to brief the Author.

## Symbolic findings (Skeptical: STATUS AMBER on the manuscript; GREEN on the script)

Polynomial identities verified on the zero-sum hyperplane:

1. **Sum of squared entries of `\tilde K(u) = 8·sum(u_i^2)`** (not `6·sum(u_i^2)`). Confirmed via `simplify(S_sub - 8·u_sq_sum) == 0` where `S_sub` is the substituted entrywise sum.
2. **Characteristic polynomial of `\tilde K(u)` is `lambda^2 (lambda^2 + 4·sum(u_i^2))`**; spectrum `{0, 0, ±i·sqrt(4·sum(u_i^2))} = {0, 0, ±i·sqrt 3}` at the unit-axis condition `sum(u_i^2) = 3/4`.
3. **Unscaled cubic identity `\tilde K(u)^3 = -3·\tilde K(u)`** at the unit axis (manuscript: `-(3/4)\tilde K`).
4. **Scaled cubic identity `K(u)^3 = -K(u)` for `K = \tilde K / sqrt 3` is preserved.** The normalization factor `1/sqrt 3` in Definition 3.1 is correct; Theorem 3.3 itself stands.

Numerical spot-check at `u = (3,-1,-1,-1)/4` (verified zero-sum and `(4/3)·sum(u_i^2) = 1`): both `\tilde K^3 + 3\tilde K` and `K^3 + K` evaluate to zero within machine precision.

## Empirical Reviewer verdict: STATUS GREEN

The script correctly implements Definition 3.1, applies the zero-sum constraint uniformly, computes sum-of-squares symbolically (not numerically), and derives the characteristic polynomial directly. The spot-check uses a genuinely simplicial-unit axis. Medium hardening suggestions (symbolic minimal-polynomial assertion; tolerance thresholds in the spot-check) are documented but do not block feeding the conclusions to the Author.

## Required manuscript edits (Author action items)

- **§3.1 line 205** — `c^2 = 3/4` → `c^2 = 3`, and `\tilde K(u)^3 = -(3/4)·\tilde K(u)` → `\tilde K(u)^3 = -3·\tilde K(u)`.
- **§3.1 lines 207–209** — the `1/sqrt(3/4) · 1/2` construction is a Rube-Goldberg presentation of `1/sqrt 3` that was anchored to the wrong `c^2`. After the correction, `K := \tilde K / sqrt(c^2) = \tilde K / sqrt 3` is the clean derivation.
- **Appendix B line 614** — remove the reference to an "online supplementary computation file"; complete the trace computation in-text.
- **Appendix B line 618** — `6·sum(u_i^2)` → `8·sum(u_i^2)`. Replace the explanatory parenthetical with a correct combinatorial count (each of the six pairwise differences `u_i - u_j` appears squared exactly twice, and `sum_{i<j}(u_i - u_j)^2 = N·sum(u_i^2) = 4·sum(u_i^2)` on the zero-sum hyperplane, giving `2·4·sum(u_i^2) = 8·sum(u_i^2)` total).
- **Appendix B lines 622–630** — replace the elliptical and hand-wavy arithmetic with the clean one-liner `tr(K^2) = (1/3)·tr(\tilde K^2) = -(1/3)·8·sum(u_i^2) = -(8/3)·(3/4) = -2`, so `c = 1` for the scaled operator.
- **Appendix B line 638 (Remark B.1)** — unscaled spectrum `{0, 0, ±sqrt(3/4)·i}` → `{0, 0, ±i·sqrt 3}`; minimal polynomial `\tilde K^3 = -(3/4)\tilde K` → `\tilde K^3 = -3\tilde K`.

STATUS: AMBER (manuscript requires arithmetic corrections; Theorem 3.3 itself is empirically preserved).
