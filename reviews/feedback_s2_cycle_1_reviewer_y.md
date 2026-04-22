# Reviewer Y — Structural & Narrative Audit — Cycle 1
**Scope:** §2 Simplicial Coordinates: Setup (lines 77–156 of simplicial_vector_calculus.md)
**Reviewer:** Reviewer Y (structure, readability, literature positioning)
**Date:** 2026-04-20

## Findings

### Critical
- **[N-C-1]** Contradiction of Cycle 1 resolution in Remark 2.1: Line 105 explicitly states "the structures are formally the same". This directly violates the Cycle 1 agreement that these cross-disciplinary connections must be presented as "structurally analogous... not as a formal equivalence of categories."

### High
- **[N-H-1]** Motivation trailing definitions: In §2.2 (line 97) and §2.3 (line 107), formal objects (gauge direction, zero-sum hyperplane) are defined mathematically before their geometric or operational purpose is explained. For example, the critical operational motivation for $H$ appears at the very end of §2.3 (line 119) rather than opening the section to orient the reader.
- **[N-H-2]** Excessive length and positioning of Remark 2.1: The remark (lines 105–106) breaks the narrative flow of the formal mathematical setup by diving into a long cross-disciplinary tangent. It should be promoted to its own subsection (e.g., "§2.2.1 Structural parallels across disciplines") or moved out of the main flow into an appendix or footnote.

### Medium
- **[N-M-1]** Abrupt section transition: Section 2 (line 77) begins immediately with "Let $N \geq 3$" without any framing or connective tissue linking it to the end of §1.3. A brief introductory sentence outlining the purpose of the section is needed.
- **[N-M-2]** Missing explicit definition of $I$: In §2.4 (line 129), the matrix $I$ is used in the Gram matrix formula without being explicitly defined as the $N \times N$ identity matrix, whereas $J$ is explicitly defined in the same sentence.
- **[N-M-3]** Insufficient forward signposting: Line 119 mentions that matrix operators preserve $H$, but fails to explicitly signpost the reader to the specific later sections (§3, §5, §7) where these tools will be heavily utilized.

### Low
- **[N-L-1]** Presentation order of the Gram matrix: In §2.4, the block matrix formula for $G$ (line 129) is asserted before its element-wise definition (line 133). Reversing this order would clarify that $G$ is derived directly from the inner products $\mathbf{v}_i \cdot \mathbf{v}_j$ shown in §2.1.
- **[N-L-2]** Disconnected coordinate labels: In §2.5 (line 154), the coordinates $(l, n, m, p)$ are introduced without explicitly linking them back to the general coordinate notation $(c_1, c_2, c_3, c_4)$.

## Summary
Section 2 effectively establishes the core mathematical notation for the manuscript, but struggles with pacing and structural flow. The most urgent issue is Remark 2.1, which both contradicts the established Cycle 1 consensus on "formal equivalence" and derails the section's focus. Additionally, the Author should reorganize the narrative to ensure geometric motivations and forward signposting precede dense formal definitions.

STATUS: AMBER
