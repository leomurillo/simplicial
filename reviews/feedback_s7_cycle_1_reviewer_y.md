# Reviewer Y — Section 7 cycle-1 narrative & structural audit

**Scope:** §7 "Computational Kernel: The 9-Multiplication Apply".
**Target:** `c:\Projects\simplicial\simplicial_vector_calculus.md`.

## Overall assessment

Section 7 successfully translates the abstract algebraic construction of the previous sections into a concrete, computationally competitive algorithm. The preamble perfectly motivates the section, directly connecting the 16 → 12 → 9 multiplication reduction to the core narrative promise of matching quaternion performance. The signposting through the reductions (§7.1 and §7.2) is logical and easy to follow. Narrative consistency with §1.2 item 5 and §9 is airtight, particularly regarding the "$S^3$ double cover" claims.

Two structural and pacing issues, both in §7.4 and around Theorem 7.1, are worth addressing; neither blocks loop termination under the severity ladder.

## Findings

- **`[Y-M-1]` Theorem 7.1 lacks structural closure.** (Medium)
  *Location:* End of §7.2.
  *Issue:* The theorem is stated mid-flow and serves as a summary of the preceding two subsections, but it lacks a formal proof marker. It currently feels swallowed by the surrounding prose.
  *Recommendation:* Add a brief proof block immediately following the theorem statement to provide closure. For example: *"Proof.* The construction of $\tilde{R}$ in §§7.1–7.2 supplies the explicit 9-multiplication algorithm. $\square$"

- **`[Y-M-2]` §7.4 renormalization paragraph is a wall of text.** (Medium)
  *Location:* Final paragraph of §7.4.
  *Issue:* Following the recent spot-patches (`[P-H-B4]`, `[V-L-1]`), this paragraph now merges two distinct topics: (1) the qualitative structural comparison (no $S^3$ double cover, no Hamilton products) and (2) the technical floating-point renormalization recipe (drift, why QR-on-$\tilde R$ fails, the Gram–Schmidt lift). The numerical realities crowd the theoretical selling point.
  *Recommendation:* Split into two paragraphs. Paragraph 1: the qualitative / theoretical comparison (up to "…hypercomplex algebra of Hamilton products."). Paragraph 2: the numerical realities and renormalization recipe, beginning "As with any matrix representation of rotations in floating-point arithmetic…".

- **`[Y-L-1]` Missing citation for quaternion costs.** (Low)
  *Location:* §7.4 comparison table and surrounding text.
  *Issue:* The 15 and 9 multiplication counts for quaternion pipelines are standard knowledge in computer graphics, but the absence of a citation leaves a slight narrative hole in an otherwise rigorously cited paper.
  *Recommendation:* Add a citation to a standard reference (e.g., Shoemake's original *SIGGRAPH* quaternion paper, or a standard 3D-math text) to ground these numbers.

- **`[Y-L-2]` §7.3 conceptual weight vs. length.** (Low)
  *Location:* §7.3.
  *Issue:* Two sentences. Carries significant conceptual weight — bridging the algebraic trick of §§7.1–7.2 with the geometric comparison of §7.4 — but feels rushed.
  *Recommendation:* Expand by one sentence to explicitly connect "absorbing the fourth coordinate" to the reduction of the 4D overcomplete space to the 3D hyperplane, giving the reader a firmer conceptual anchor before diving into the quaternion comparison.

- **`[Y-L-3]` Table footnote formatting.** (Low)
  *Location:* Text immediately following the §7.4 table.
  *Issue:* The sentence beginning *"The 'multiplications / apply' column reports…"* acts as a table footnote but is formatted as body text.
  *Recommendation:* Either format this as a proper footnote attached to the table, or integrate it more smoothly into the introductory prose of the subsequent paragraph.

## Summary of findings

- Critical: none.
- High: none.
- Medium: `[Y-M-1]` (Theorem 7.1 lacks proof marker); `[Y-M-2]` (§7.4 final paragraph needs splitting).
- Low: `[Y-L-1]`, `[Y-L-2]`, `[Y-L-3]`.

STATUS: AMBER
