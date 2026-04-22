# Reviewer X — Formalism Audit — Cycle 3
**Scope:** §1 Introduction + Abstract + §4 (post-Cycle-2 revision)
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Resolution of Cycle 2 findings

- **[F-H-4] RESOLVED** — The Abstract and §4 now match §1's narrowed manuscript-level claim: the paper is about the algebraic layer only, and intrinsicness is explicitly qualified by prior fixation of the simplicial Gram data.
- **[F-H-1] partial RESOLVED** — In the reviewed regions, the manuscript now consistently excludes differential operators and no longer advertises a full vector-calculus package.
- **[F-H-2] partial RESOLVED** — The Abstract and Remark 4.2 no longer make the old unqualified "without Cartesian frame" claim, and now use the same Gram-fixed qualifier as §1.
- **[F-M-6] RESOLVED** — §1.2 item 3 now forward-references a §4 whose heading and theorem statement genuinely use the gauge-compatibility/descent language it advertises.

## New findings

### Critical
- None.

### High
- **[F-H-5]** The Abstract (line 17) and §1.2 item 2 (line 51) misidentify the simplicial Gram matrix as $G = I - \tfrac{1}{N}J$, whereas §2.4 (line 129) defines the Gram matrix as $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$. The matrix $I - \tfrac{1}{N}J$ is the orthogonal projector onto the zero-sum hyperplane, not the ambient simplex Gram matrix. This is not a cosmetic notation slip: it changes the normalization of the simplicial norm and makes the scoped summary formally inconsistent with the paper's actual setup. (Abstract, item 1; §1.2 item 2; §2.4.)

### Medium
- **[F-M-7]** The Abstract's sentence "The three operators are constructed and shown to close on the hyperplane and commute with the gauge action" is not formally well-matched to Theorem 4.1, which carefully distinguishes scalar gauge-invariance of the inner product from hyperplane-closure / gauge-annihilation / gauge-fixing for the vector-valued operators; as written, the Abstract blurs precisely the distinction that §4 was revised to make explicit. (Abstract, second paragraph; Theorem 4.1.)
- **[F-M-8]** Theorem 4.1(ii) uses $K(\mathbf{1}) = 0$ as part of the descent story, but Definition 3.1 defines $K(u)$ only for zero-sum unit axes; the paper is clearly relying on the entrywise linear formula to extend $K$ beyond that domain, yet that extension is not stated as a formal definition before it is used in the theorem. (Theorem 4.1(ii); Definition 3.1; Remark 3.2.)

### Low
- None.

## Summary
The Cycle 2 harmonization succeeded on the issue it was meant to solve: Abstract, §1, and §4 now tell the same narrower story about algebraic operators and qualified intrinsicness. I cannot, however, issue formal clearance because the reviewed front matter now contains a new foundational inconsistency about what the Gram matrix actually is, and that error sits directly inside the scoped summary of the paper's setup.

STATUS: AMBER
