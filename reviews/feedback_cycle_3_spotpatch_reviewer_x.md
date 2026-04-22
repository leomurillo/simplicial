# Reviewer X — Post-AMBER Spot-Verification
**Scope:** spot-check of surgical patch for [F-H-5], [F-M-7], [F-M-8] (+ consequential Theorem 4.1 update)
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Verification per finding

- **[F-H-5] RESOLVED** — The Abstract and §1.2 item 2 now both use the correct simplicial Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$, and the Abstract's collapsed quadratic form $\langle c,c\rangle = \tfrac{N}{N-1}\sum_i c_i^2$ matches §2.4 and Appendix A.
- **[F-M-7] RESOLVED** — The revised Abstract now cleanly separates scalar gauge-invariance of the inner product from hyperplane-closure plus gauge-annihilation/fixing for the vector-valued operators, and it does not revert to the earlier blurred "close on the hyperplane and commute with the gauge action" wording.
- **[F-M-8] RESOLVED** — Remark 3.2 now states, in the correct order before Theorem 4.1, that Definition 3.1's entrywise formula extends to every $u \in \mathbb{R}^4$, that this extension is linear, and that $K(\mathbf{1}) = 0$.
- **Theorem 4.1 follow-through ACCEPTABLE** — The added $K(\mathbf{1}) = 0$ sentence in Theorem 4.1(ii) / its proof sketch is consistent with Remark 3.2, functioning as a downstream use of the prior formal extension rather than a competing definition.

## New concerns

None.

## Summary

The surgical patch resolves all three targeted Cycle 3 findings within the authorized scope. I do not see any new Critical or High formalism issue introduced by these specific changes.

STATUS: GREEN
