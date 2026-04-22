# Reviewer Y — Structural & Narrative Audit — Cycle 2
**Scope:** §5 Closed-Form Rotation via the Exponential Map
**Reviewer:** Reviewer Y (structure, readability, literature positioning)
**Date:** 2026-04-20

## Verification of Cycle 1 resolutions
- **[N-H-1] Missing citations for classical results** — RESOLVED. The text now clearly situates the Rodrigues formula and the Lie-algebraic exponentiation by citing standard texts `[Arnold]` and `[Hall]`. Both texts correctly appear in the References list, and their inclusion correctly attributes the classical results without claiming undue novelty.
- **[N-H-2] Ambiguous geometric claims in §5.1** — RESOLVED. The previously compressed geometric claim has been thoroughly unpacked into a rigorous derivation. The addition of clearly signposted sub-proofs (*Orthogonality*, *Equal norms*, *Axial degenerate case*) eliminates the narrative "leap of faith".
- **[N-M-1] Missing section roadmap** — RESOLVED. The new paragraph at line 295 provides a clear, substantive forecast for §5.1, §5.2, §5.3, and Remark 5.1, smoothing the transition into the mathematics.
- **[N-M-2] Choppy paragraphing in §5.1** — RESOLVED. The text from lines 297–324 has been grouped into logical, cohesive paragraphs and sub-headed arguments, greatly improving the reading experience.
- **[N-M-3] Clarify "unit skew operators" and Lie algebra** — RESOLVED. The jargon was removed in favor of a precise mathematical characterization (satisfying $K(u)^3 = -K(u)$). The explicit reference to the classical hat-map elegantly bridges the gap to Cartesian rigid-body mechanics.
- **[N-M-4] Over-promising section title (§5.3)** — RESOLVED. "Comparison of the two derivations" is an accurate, measured title.
- **[N-M-5] Loose structural labels in §5.3** — RESOLVED. The text now formally and correctly identifies $I+K^2$ as the parallel projector and $-K^2$ as the perpendicular projector.
- **[N-M-6] Notation consistency for $K(u)$ vs $K$** — RESOLVED. The explicit reminder at line 299 ensures the shorthand is clear and prevents confusion.
- **[N-L-1] Remove box around formula** — RESOLVED. The `\boxed{}` formatting was removed and replaced with standard display math and the label (5.1).
- **[N-L-2] Rephrase grouping step** — RESOLVED. "Regrouping by parity of the exponent" reads professionally.
- **[N-L-4] Axis-argument scope** — RESOLVED. The WLOG assumption for $u \in H$ is clearly stated at line 299.
- **[N-L-5] "Intrinsic" rhetoric softening** — RESOLVED. The phrasing "intrinsic to the algebraic layer of the simplicial system" appropriately respects the established scope boundaries from §1.

## New findings (Cycle 2)

### Critical
*(None)*

### High
*(None)*

### Medium
*(None)*

### Low
- **[N-L-6] Equation formatting in §5.2:** The Taylor series expansion and the subsequent regrouped equations (lines 340–346) are separated by a single line of text ("Regrouping by parity of the exponent and using the closure identity,"), causing a slight visual stutter. Consider shifting the text to precede the math block entirely, and merging the equations into a single `\begin{aligned} ... \end{aligned}` block. This is purely a cosmetic suggestion for typography.

## Summary
The Author's Cycle 1 revisions have fully resolved all structural and narrative concerns for §5. The geometric derivation is now rigorous and readable, the citations firmly ground the work in the existing literature, and Remark 5.1 manages the orientation convention gracefully without detracting from the section's main arc. The narrative flows smoothly and is ready for publication.

STATUS: GREEN
