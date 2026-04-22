# Reviewer X — Formalism Audit — Cycle 1
**Scope:** §1 Introduction (lines 35–68 of simplicial_vector_calculus.md)
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Findings

### Critical
- None.

### High
- [F-H-1] `§1.2 item 3` (line 53) and `§1.1` (line 45) — The phrase "complete intrinsic 3D Euclidean vector calculus" is formally overstated as written. What the paper actually advertises and later develops are an inner product, a binary cross-product operator, and a rotation/exponential map on the zero-sum hyperplane. In standard mathematical usage, "vector calculus" ordinarily includes differential operators ($\nabla$, divergence, curl, etc.), none of which are part of the claimed construction in §1. Without an explicit narrowing of what "vector calculus" means here, the introduction promises a materially broader theory than is specified.
- [F-H-2] `§1.2 item 3` (line 53) and `§1.3` (line 65) — The claim "independent of any Cartesian embedding" is not well-posed in the present introduction. The manuscript's setup is built from a regular simplex realized by vectors in $\mathbb{R}^{N-1}$ and from the induced Gram matrix; thus some ambient Euclidean structure is used to define the metric data in the first place. If the intended claim is only that the final formulas do not require ongoing reference to Cartesian coordinates once the simplicial metric structure is fixed, that must be stated. As written, the claim reads stronger than the formal setup warrants.
- [F-H-3] `§1.2 item 7` (line 61) — "We identify $N = 4$ as the unique case in which the construction yields a binary cross product and admits closed-form exponentiation via $K^3 = -K$" is too absolute without an explicit scope restriction. The downstream discussion supports uniqueness only for the specific simplicial/Hodge-dual, axis-to-skew-operator framework under consideration; it does not establish uniqueness among all conceivable simplicial binary operations or all notions of "closed-form exponentiation." As stated, the sentence overclaims a universality theorem that §1 does not formulate precisely.

### Medium
- [F-M-1] `§1.2 item 2` (line 51) and `§1.2 item 4` (line 55) — The term "zero-sum unit axis" is used before the relevant norm is specified. Later sections make clear that "unit" means unit with respect to the simplicial inner product, not the standard Euclidean norm on $\mathbb{R}^4$. Because the identities $K^3 = -K$ and the Rodrigues formula depend on that normalization, the introductory claims carry a hidden metric precondition.
- [F-M-2] `§1.1` (line 45) and `§1.2 item 3` (line 53) — The sentence grouping "inner product, cross product, exponential" under the claim that the three "close on the zero-sum hyperplane and commute with the gauge action" is formally sloppy. The inner product is scalar-valued, so it does not "close on the hyperplane" in the same sense as the vector-valued operators; what is meant is gauge-invariance of the scalar and hyperplane-preservation for the vector-valued maps. This is not false, but the introduction compresses distinct invariance statements into one slogan.
- [F-M-3] `§1.2 item 4` (line 55) — The item blurs two different roles of $R$: as a $4 \times 4$ orthogonal matrix on the overcomplete coordinate space and as the actual rotation acting on the zero-sum hyperplane. Saying that $R$ "rotates zero-sum vectors about an arbitrary zero-sum unit axis" and then immediately asserting $R\mathbf{1}=\mathbf{1}$, row sums, and column sums mixes the hyperplane action with its gauge-compatible extension on all of $\mathbb{R}^4$. The distinction matters formally and should not be left implicit in a contribution claim.
- [F-M-4] `§1.2 item 1` (line 49) — The cross-disciplinary claim that the same formal structure appears in gauge theory, stoichiometric compatibility classes, and the probability simplex is stated as if it were a proved structural identification, but §1 only offers an interpretive analogy. Unless the paper gives an explicit equivalence of structures and maps preserving the relevant operations, the introduction should present this as motivation or analogy, not as a formal reframing theorem.
- [F-M-5] `§1.1` (lines 39–45) and `§1.2 item 7` (line 61) — The introduction moves between the general $N$-simplex family and the exceptional $N=4$ case without cleanly walling off degenerate low-dimensional cases. A reader is told that the family exists for general $N$, sees examples $N=3$ and $N=4$, and is later told $N=4$ is unique for the binary cross-product phenomenon, but there is no explicit statement of what fails for $N=1,2,3$. For an introduction foregrounding uniqueness and dimensional exceptionality, that omission is a rigor gap.

### Low
- [F-L-1] `§1.3` (line 65) — "We reserve the unmarked term 'Rodrigues formula' for the closed-form exponential derived here" is terminological policy, not a mathematical statement. In a formal introduction this is harmless, but it sits next to substantive definitional claims and slightly blurs the boundary between notation governance and theorem-level content.
- [F-L-2] `§1.1` (line 45) — "This paper closes that gap" is rhetorically stronger than the surrounding formal register. For a proof-oriented manuscript, the introduction should prefer a precise statement of which gap is closed and under what hypotheses, rather than a broad closure slogan.

## Summary
§1 is directionally coherent, and the later manuscript does support many of its advertised constructions, but the introduction currently overstates scope at exactly the points where a formal reader will press hardest: what "vector calculus" means here, what "intrinsic" excludes, and in what sense $N=4$ is "unique." The quantitative claims are mostly defensible once later hypotheses are imported, but §1 does not state those preconditions cleanly enough to be formalism-ready.

STATUS: AMBER
