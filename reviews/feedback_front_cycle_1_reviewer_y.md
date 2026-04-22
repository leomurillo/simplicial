# Front Matter Cycle 1 — Reviewer Y (Narrative & Structure)

**Date:** 2026-04-21
**Target:** `simplicial_vector_calculus.md` (Title, Abstract, Keywords, MSC, AI Note, §1)
**Context:** §§3–9 are GREEN. Harmonizing front matter with the stabilized body.

## Overall Status: AMBER

The front matter is structurally sound and sets up the paper's thesis well, but requires a few narrative harmonization passes to match the polish of the stabilized body. The most prominent issues are a verbatim redundancy in the Abstract, a duplicated AI disclosure, and a closing Abstract sentence that dilutes the main $N=4$ achievement (mirroring a flaw previously fixed in §9).

| Severity | Count | IDs |
|---|---|---|
| Critical | 0 | — |
| High | 3 | `[F1-Y-H-1]`, `[F1-Y-H-2]`, `[F1-Y-H-3]` |
| Medium | 1 | `[F1-Y-M-1]` |
| Low | 3 | `[F1-Y-L-1]`–`[F1-Y-L-3]` |

## High Findings

### [F1-Y-H-1] Abstract redundancy (Paragraph 2 vs Paragraph 4)
- **Location:** Abstract, lines 15–16 vs line 21.
- **Observation:** The sentence introducing the list ("We develop an intrinsic algebraic vector calculus … Once the simplicial Gram data is fixed, their formulas require no ongoing reference to a Cartesian frame") is almost verbatim repeated in the paragraph following the list ("Together these operators constitute an intrinsic algebraic calculus … once the simplicial Gram data is fixed, all formulas are expressible without further reference to a Cartesian frame.").
- **Proposed Fix:** Delete the redundant restatement at the start of the final paragraph. Let the final paragraph begin directly with the specific $N=4$ achievements: "For $N=4$, we prove $K^3 = -K$ and derive…"

### [F1-Y-H-2] Abstract closing sentence dilutes impact
- **Location:** Abstract, line 21 ("Higher $N$ admits the analogous construction …").
- **Observation:** Just as in the pre-revision §9, ending the Abstract on "future work" for higher $N$ dilutes the impact of the $N=4$ closed-form achievement. The Abstract should land on the paper's primary contribution.
- **Proposed Fix:** Move the higher-$N$ Hodge dual mention earlier in the paragraph (perhaps as a parenthetical or subordinate clause when discussing the uniqueness of $N=4$), and end the Abstract on the 9-multiplication kernel or the Lie-algebra isomorphism reflection.

### [F1-Y-H-3] Duplicated AI Disclosure
- **Location:** Lines 29–31 ("A Note on the Use of AI Tools") vs. Acknowledgments (~lines 497–501).
- **Observation:** The AI disclosure is printed twice in the manuscript. While transparent, placing a dedicated section between the Abstract and Introduction is non-standard for arXiv/journal submissions and disrupts the narrative flow into §1.
- **Proposed Fix:** Delete the standalone "A Note on the Use of AI Tools" section (lines 29–33). The disclosure in the Acknowledgments is perfectly calibrated, standard in placement, and sufficient.

## Medium Findings

### [F1-Y-M-1] §1.3 Grab-bag structure
- **Location:** §1.3 (lines 63–76).
- **Observation:** The sub-paragraphs feel slightly disjointed. In particular, "Finite element exterior calculus" (line 67) is a single sentence that logically belongs with the preceding paragraph on "Relation to discrete exterior calculus" (lines 65–66).
- **Proposed Fix:** Merge the FEEC paragraph into the DEC paragraph to create a single coherent block on "Relation to exterior calculus."

## Low Findings

### [F1-Y-L-1] §1.2 item 3 shorthand upgrade
- **Location:** §1.2 item 3 (line 53).
- **Observation:** As noted in `open-issues.md` `[L-2-1]`, the parenthetical "(values unchanged under $x \mapsto x + t\mathbf{1}$)" uses a one-slot shorthand for the inner product's gauge invariance. (Reviewer X raises the same at Medium severity [F1-M-2]; converge on the stronger.)
- **Proposed Fix:** Upgrade to the two-slot form to match Theorem 4.1: "(values unchanged under $x \mapsto x + k\mathbf{1}$ and $y \mapsto y + m\mathbf{1}$)".

### [F1-Y-L-2] Keywords granularity
- **Location:** Line 23.
- **Observation:** Adding "overcomplete coordinates" or "gauge redundancy" would better capture the structural theme of the paper for indexers.
- **Proposed Fix:** Update to: `simplicial coordinates, Quadray, overcomplete coordinates, gauge redundancy, cross product, Rodrigues formula, Lie algebra, zero-sum hyperplane, rotation.` (Reviewer X proposes a complementary set emphasizing "gauge direction", "Hodge dual", "wedge product"; converge on the Author's pass.)

### [F1-Y-L-3] Abstract orphan terminology
- **Location:** Abstract, line 21 ("… admits a 9-multiplication kernel for apply operations …").
- **Observation:** "Apply operations" is slightly jarring computer-science jargon in a math-heavy abstract.
- **Proposed Fix:** Change to "for applying rotations to zero-sum inputs" or simply "a 9-multiplication computational kernel".
