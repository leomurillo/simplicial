# Reviewer Y — Structural & Narrative Audit — Cycle 1
**Scope:** §4 Gauge-Compatibility and Descent to the Zero-Sum Quotient
**Reviewer:** Reviewer Y (structure, readability, literature positioning)
**Date:** 2026-04-20

## Critical
- None.

## High
- **[N-H-1] Domain mismatch / missing signpost in Theorem 4.1(ii)** — Line 280 restricts the axis $u$ to "each zero-sum unit axis," but the clause concludes by evaluating $K$ on the gauge direction: "$K(\mathbf{1}) = 0$". Since $\mathbf{1}$ is neither zero-sum nor a unit axis, this relies on the formal linear extension. This leap must be explicitly signposted (e.g., referencing Remark 3.2) to avoid confusing readers tracking the domain.
- **[N-H-2] Awkward hedge in opening paragraph** — Line 275 uses "(presently) the exponential map" to signal that the exponential map is not fully constructed yet. This parenthetical is clunky and ambiguous. It should be replaced with a clear forward reference, such as "and the exponential map (constructed in §5)".

## Medium
- **[N-M-1] Redundant scope disclaimers** — The scope limitation ("we address the algebraic layer… differential operators are not developed here") is stated fully at line 275 and then repeated almost verbatim at the end of Remark 4.2 (line 287). The repetition reads as defensive padding; one clear iteration in the opening paragraph is sufficient.
- **[N-M-2] Ungrounded "rigid-body" framing** — Remark 4.2 introduces "classical rigid-body mechanics" as an interpretive lens. While helpful for intuition, adding an authoritative citation (e.g., Arnold, *Mathematical Methods of Classical Mechanics*, or Marsden–Ratiu) would anchor this framing in the literature.
- **[N-M-3] Syntax overload in Remark 4.2** — Line 287 uses a long, em-dash-enclosed clause ("— once the simplicial Gram data… Cartesian embedding —") immediately following a section reference. This breaks the flow and makes the sentence heavy to read.

## Low
- **[N-L-1] Theorem list formatting** — Lines 279–281 use both markdown bullets and italicized roman numerals (`- *(i) ...*`). Consider standardizing to either just numerals or just bullets to reduce visual clutter.
- **[N-L-2] Descent context** — A brief callback to the structural parallels established in §2.2.1 (where this quotient is central in information geometry and CRNT) could enrich the narrative positioning of the descent claim.

## Summary
Section 4 successfully consolidates the algebraic properties and maintains the rigorously narrowed scope of the preceding sections. Resolving the domain leap in Theorem 4.1(ii) and removing redundant phrasing will bring the narrative flow up to standard.

STATUS: AMBER
