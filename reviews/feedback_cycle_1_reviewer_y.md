# Reviewer Y — Structural & Narrative Audit — Cycle 1
**Scope:** §1 Introduction (lines 35–68 of simplicial_vector_calculus.md)
**Reviewer:** Reviewer Y (structure, readability, literature positioning)
**Date:** 2026-04-20

## Findings

### Critical
- [N-C-1] §1.2 Item 7 — The text claims uniqueness for $N=4$ and references "Hodge duals of wedge products" for higher $N$, but provides no citations to the existing mathematical literature on generalized cross products (e.g., Eckmann, Massey). Missing these citations breaks the paper's positioning for a differential geometry audience, making the authors appear unaware of classical results on cross products in $\mathbb{R}^n$.

### High
- [N-H-1] §1.1 & §1.2 — The introduction lists major contributions (intrinsic cross product, Rodrigues formula, 9-multiplication kernel) but completely fails to forward-reference the sections where they appear. Readers are left hunting for the proofs; standard academic signposting (e.g., "In Section 3, we...") is missing.
- [N-H-2] §1.2 Item 3 — "Vector calculus completeness" is highly redundant with Items 2 and 4, restating closure and gauge-commutation without adding distinct claims. This dilutes the contribution list and should be merged or refocused to highlight a specific theorem.

### Medium
- [N-M-1] §1.1 — Mentions "barycentric coordinates... used ubiquitously in finite element analysis" but provides zero citations to standard FEA or barycentric calculus literature.
- [N-M-2] §1.2 Item 4 — Uses the notation $\mathbf{1}$ in the equation $R\mathbf{1} = \mathbf{1}$ without defining it in the Introduction. While defined in the Abstract, the introduction should be self-contained.
- [N-M-3] §1.3 — The justification for retiring "mass-action ray" is placed in the terminological notes, but the term is already brought up and reframed in §1.2 Item 1. This creates a slight disjoint in narrative flow.

### Low
- [N-L-1] §1.1 — Citing Fuller's synergetics [Fuller] alongside formal math may read unusually to an arXiv audience; consider clarifying that it serves as historical/philosophical inspiration rather than mathematical authority.

## Summary
The introduction strongly motivates the problem and clearly articulates the gap in the simplicial coordinate literature. However, it suffers from a lack of forward-referencing to specific sections, some redundancy in the contributions list, and missing citations for its connections to broader mathematical fields like exterior calculus and FEA.

STATUS: AMBER
