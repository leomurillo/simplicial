# Reviewer Y — Structural & Narrative Audit — Cycle 1
**Scope:** §5 Closed-Form Rotation via the Exponential Map
**Reviewer:** Reviewer Y (structure, readability, literature positioning)
**Date:** 2026-04-20

## Critical
*(None. The section respects the scope narrowings from §1 and §4, and introduces no core narrative errors or contradictions to established conventions.)*

## High
- **[N-H-1] Missing citations for classical results** — The classical Rodrigues formula (line 343) and the exponentiation of $\mathfrak{so}(3)$ via $K^3 = -K$ (lines 325–331) are standard exercises in Lie theory and rigid-body mechanics. While their realization in the simplicial setting is the paper's contribution, failing to cite standard texts (e.g., Arnold, Marsden-Ratiu, or Hall) risks giving the impression that the paper claims novelty for the formulas themselves. Add citations near line 319, 331, or 343.
- **[N-H-2] Ambiguous geometric claims in §5.1** — At line 303, the sentence "The cross product $KP$ produces a vector in the plane perpendicular to $u$, orthogonal to $P_\perp$ within that plane, and of the same simplicial length as $P_\perp$" packs three non-trivial geometric properties into one unreferenced claim. For a reader following the narrative, this is a large leap of faith. Unpack this statement or add a direct backward reference to the specific lemma in §3 where these properties are proven.

## Medium
- **[N-M-1] Missing section roadmap** — §5 begins abruptly at line 295 with the geometric derivation. A one-paragraph roadmap immediately after the §5 heading would greatly improve the transition, signposting that the section will provide two equivalent derivations (geometric and Lie-algebraic) of the simplicial Rodrigues formula and position it as the intrinsic realization of the rotation operator.
- **[N-M-2] Choppy paragraphing in §5.1** — The derivation in §5.1 is broken into single-sentence paragraphs around every equation (lines 297–315). This creates a disjointed reading experience. Consolidate the text into cohesive paragraphs.
- **[N-M-3] Clarify "unit skew operators" and Lie algebra** — At line 327, the phrase "unit skew operators" is slightly jargon-heavy; clarify that this implies the scaling required to satisfy $K^3 = -K$. Additionally, a brief hat-map ($\mathbb{R}^3 \to \mathfrak{so}(3)$) reminder or explicit reference may help readers from applied backgrounds comfortably bridge the gap to Lie theory.
- **[N-M-4] Over-promising section title (§5.3)** — "Equivalence of the two derivations" is a heavy title for a three-sentence observation. Consider renaming to "Comparison of derivations" or simply folding these sentences into the end of §5.2 to improve structural flow.
- **[N-M-5] Loose structural labels in §5.3** — The parenthetical at line 347 describing "$I, K, K^2$ as parallel projection, in-plane orthogonal rotation, and negative perpendicular projection" provides valuable intuition, but is technically loose ($I$ is the identity, whereas $I + K^2$ is the parallel projection). Refine this phrasing so the intuition remains but the terminology is formally accurate.
- **[N-M-6] Notation consistency for $K(u)$ vs $K$** — Lines 299–315 use $K$ interchangeably with $K(u)$. Reminding the reader early in §5.1 that $K$ is shorthand for the axis-dependent operator $K(u)$ will prevent confusion and ensure notation is harmonized with §3.

## Low
- **[N-L-1] Remove box around formula (line 319)** — The boxed formula is visually over-emphatic given that boxes are not used elsewhere in the manuscript. Standard display math is sufficient and more consistent with the paper's aesthetic.
- **[N-L-2] Rephrase grouping step (line 337)** — "Grouping odd and even powers $\geq 1$" is slightly awkward. Consider phrasing like "Regrouping by parity of the exponent" or similar.
- **[N-L-3] Forward reference to §9 (line 347)** — The reference to higher dimensions is good, but could be made explicitly clear ("See §9 for a discussion of the Hodge dual analog") to better preview the content.
- **[N-L-4] Axis-argument scope (line 297)** — The text specifies rotating "around a zero-sum unit axis $u$". A minor note that assuming $u \in H$ is without loss of generality (due to the gauge invariance established in §4) would tie the narrative together more elegantly.
- **[N-L-5] "Intrinsic" rhetoric (line 343)** — Calling the formula "intrinsic to the simplicial system" is acceptable, but tweaking it to "intrinsic to the algebraic layer of the simplicial system" would strictly respect the scope narrowing established in §1 and §4.

## Summary
The dual-derivation structure of §5 is conceptually strong and clearly demonstrates the simplicial Rodrigues formula. However, the narrative is hindered by choppy paragraphing, a lack of an introductory roadmap, and missing citations for classical Lie-algebraic and rigid-body mechanics results, which are necessary to appropriately situate the work in the literature.

STATUS: AMBER
