# Cycle 1 Synthesis — §2 Simplicial Coordinates: Setup
**Scope:** §2 (lines 77–156 of `simplicial_vector_calculus.md`)
**Cycle:** 1 of up to 3
**Reviewers:** Reviewer X (formalism), Reviewer Y (narrative)
**Status (joint):** AMBER (Reviewer X: AMBER, Reviewer Y: AMBER)
**Date:** 2026-04-20

Per-reviewer files:
- [`feedback_s2_cycle_1_reviewer_x.md`](./feedback_s2_cycle_1_reviewer_x.md) — 0 Critical, 2 High, 3 Medium, 2 Low.
- [`feedback_s2_cycle_1_reviewer_y.md`](./feedback_s2_cycle_1_reviewer_y.md) — 1 Critical, 2 High, 3 Medium, 2 Low.

## Convergent findings (both reviewers independently flagged)
Both reviewers independently flagged **Remark 2.1**'s "the structures are formally the same" as blocking. This is a cross-cycle regression against the §1.2 item 1 Cycle 1 resolution ("structurally analogous... not as a formal equivalence of categories"). The §1 edits in Cycle 1 did not propagate to §2's remark, and the inconsistency must be repaired.

## Loop-blocking findings (Critical + High)

Five distinct blockers (with the Remark 2.1 issue double-counted as [N-C-1] = [F-H-1]):

1. **[N-C-1] / [F-H-1]** Remark 2.1 line 105 — replace "the structures are formally the same" with language consistent with §1.2 item 1 ("structurally analogous," "interpretive motivation, not a formal equivalence of categories"). Reviewer Y rated Critical because it contradicts a previously adjudicated consensus; Reviewer X rated High. Treat as blocking regardless.

2. **[F-H-2]** §2.1 lines 79–93 — the overcomplete family $\{\mathbf{v}_i\}_{i=1}^N$ is called a "basis" / "basis vectors" throughout §2, but it is explicitly linearly dependent in $\mathbb{R}^{N-1}$. Standard terminology is "spanning family" or "frame." Audit every use of "basis" in §2 and rename where strictly appropriate, or explicitly acknowledge the terminological abuse at first use with a footnote or parenthetical (e.g., "we retain the classical Quadray/4t terminology of 'basis' for $\{\mathbf{v}_i\}$, with the understanding that the family is overcomplete as a frame in $\mathbb{R}^{N-1}$").

3. **[N-H-1]** §2.2–§2.3 motivation trails definitions — Add a 1–2 sentence opening to §2.2 explaining *why* the gauge direction matters (the redundancy of overcomplete coordinates and the operational need to factor it out) before introducing $\mathbf{1}$ and the equivalence. Same treatment for §2.3.

4. **[N-H-2]** Remark 2.1 length and positioning — the remark is a full paragraph covering CRNT, mass-action kinetics, and information geometry; it interrupts the formal setup at exactly the most pedagogically fragile point. Promote to its own subsection (e.g., "§2.2.1 Structural parallels across disciplines") or demote to a footnote; either is acceptable, but the current mid-flow remark placement is not.

## Non-blocking findings (Author discretion)

- **[F-M-1]** Quotient vs canonical section language — introduce "$H$ is a canonical section of $\mathbb{R}^N/\langle\mathbf{1}\rangle$" at §2.3, not first at §4.
- **[F-M-2]** §2.3 line 119 "inner product preserves $H$" conflates scalar and vector operators (the same shape as the Cycle 2 [F-H-4] Abstract issue; Reviewer X rated Medium in §2, but the Author may want to upgrade given the Cycle 2 precedent). Fix: split into scalar gauge-invariance vs. vector hyperplane-closure/fixing.
- **[F-M-3]** §2.5 orientation/chirality convention not explicit — add one sentence stating the orientation of $\mathbb{R}^3$ induced by the $(l, n, m, p)$ ordering.
- **[N-M-1]** §2 opens with "Let $N \geq 3$" — add a brief connective sentence from §1.3.
- **[N-M-2]** $I$ in §2.4 line 129 is not defined as the $N \times N$ identity matrix.
- **[N-M-3]** §2.3 line 119 lacks forward refs (§3, §5, §7).
- **[F-L-1]** §2.3 uniqueness of zero-sum representative not justified — add a one-line argument.
- **[F-L-2]** §2 does not remind that $N=1, 2$ are excluded.
- **[N-L-1]** §2.4 presentation order of $G$ — derive element-wise from basis inner products, then state the matrix form.
- **[N-L-2]** §2.5 $(l, n, m, p)$ vs. $(c_1, c_2, c_3, c_4)$ — link the two labelings explicitly.

## Proposed Author triage

**Accept (blocking):** all five items above — 1 cross-cycle regression fix, 1 terminology repair, 2 narrative reorganizations.

**Strongly recommended (non-blocking but cheap):** [F-M-2] scalar/vector split, [N-M-1] transition sentence, [N-M-2] define $I$, [N-M-3] forward signposting. These are one-line fixes.

**Open question on the §2 Cycle 1 regression:** [N-C-1] / [F-H-1] is a *cross-cycle regression* — §1 Cycle 1 fixed the language in §1.2 but the same language appears in §2's Remark 2.1 and was not swept. The protocol currently has no "cross-scope propagation check" step. Consider adding one: when the Author edits terminology or claims in a closed scope, the orchestrator should grep the rest of the manuscript for the old language and flag sites that may need parallel edits. This would have caught Remark 2.1 at Cycle 1 §1 synthesis time. *Recommendation: add a small "propagation pass" clause to the authorship skill before Cycle 2 on §2, so future scopes don't repeat this class of drift.*

## Author triage (cycle 1)

**Date:** 2026-04-20
**Author:** Lead author (Opus 4.7)
**Cycle outcome:** all 5 loop-blocking findings accepted; manuscript revised in place.

### Blocking findings

- **[N-C-1] / [F-H-1] Remark 2.1 cross-cycle regression — Accepted.** The old Remark 2.1 (line 105) was rewritten and promoted to a new subsection §2.2.1 "Structural parallels across disciplines." The phrase "the structures are formally the same" and "not accidental" wording are removed. The new subsection opens with an explicit alignment to §1.2 item 1 ("structural analogies offered for interpretive motivation, not as a formal equivalence of categories") and states that "no functorial identification is constructed here." Each of the two cross-disciplinary threads (CRNT, information geometry) is explicitly qualified as "structural" / "not a formal identification." Resolves both [N-C-1] (Reviewer Y, Critical) and [F-H-1] (Reviewer X, High).

- **[F-H-2] "basis" vs. "frame" terminology — Accepted with modification (Option B).** Chose Option B (explicit terminological abuse acknowledged at first use) over Option A (terminology sweep). Rationale: "basis," "basis vectors," and especially "basis axis" (as in "rotation about a basis axis") are pervasive in §§3, 5, 7, 8, 9 and are the canonical terms in the cited Quadray / 4t literature (Urner, Ace, Thomson); a global rename to "frame" or "spanning-family" would read as idiosyncratic, obscure references to Ace's and Thomson's work, and conflict with the distinct technical use of "basis" in §7.3 (where a genuine basis of $H$ is constructed). Edit: §2.1 (now lines 83–84) explicitly states that the family is strictly a spanning family (frame) for $\mathbb{R}^{N-1}$, notes that no linear independence is claimed, and forward-refers to §7.3 for the genuine-basis case. No out-of-§2 edits required.

- **[N-H-1] Motivation trailing definitions in §2.2 and §2.3 — Accepted.** Added a two-sentence opening paragraph to §2.2 (line 99) motivating the gauge direction as a redundancy to be factored out before any linear-algebraic operation. Added a similar paragraph opening §2.3 (line 119) motivating the zero-sum representative as a canonical section of the quotient projection, ahead of the formal definitions.

- **[N-H-2] Remark 2.1 length and positioning — Accepted (Option A).** Chose Option A (promote to subsection §2.2.1) over B (footnote) or C (trim). Rationale: the cross-disciplinary material is substantive enough (two distinct parallels, each with citations) that a footnote would compress it beyond usefulness, and trimming to ~2 sentences would lose the CRNT/info-geometry distinction that §9 Discussion explicitly returns to. A subsection between §2.2 and §2.3 preserves the formal flow (gauge direction → zero-sum hyperplane) while signalling to a time-pressed reader that the disciplinary parallels can be skipped without loss of formal content.

- **[F-M-2] §2.3 line 119 scalar/vector conflation — Accepted (upgraded from Medium).** The old sentence "Matrix operators that respect the gauge (rotations, the cross product, the inner product) all preserve $H$" was replaced (now line 131) by an explicit split: the inner product of §2.4 is gauge-invariant as a scalar; the vector-valued operators $K(u)$ (§3) and $R(u,\theta)$ (§5) preserve $H$ and annihilate / fix the gauge direction. This is the exact shape of the Cycle 2 [F-H-4] Abstract fix, applied to §2. (Note: this finding was listed as non-blocking [F-M-2] in the Reviewer X file, but I treated it as effectively blocking under the Cycle 2 precedent, as suggested by Reviewer X himself.)

### Non-blocking findings addressed

- **[N-M-1] §2 opening transition — Accepted.** Added a connective opening paragraph to §2 (line 79) stating the section's purpose and linking to §1.3 for low-$N$ degeneracies.
- **[N-M-2] Define $I$ — Accepted.** §2.4 (line 147) now explicitly defines $I$ as the $N \times N$ identity matrix alongside the existing $J$ definition.
- **[N-M-3] Forward references — Accepted.** §2.3 (line 131) now signposts §3, §5, §7 explicitly at the hyperplane-closure claim, and §2.3 (line 119) forward-refs §2.4 at the canonical-section motivation.
- **[F-M-1] Quotient vs canonical section — Accepted.** §2.3 (lines 119, 129) now explicitly introduces $H$ as a canonical linear section of $\mathbb{R}^N / \langle \mathbf{1} \rangle$, not deferred to §4.
- **[F-M-3] Orientation / chirality convention — Accepted.** §2.5 (line 168) now fixes the standard right-handed orientation of the ambient $\mathbb{R}^3$ and notes that the chirality conventions of §3, §5, §8 are all with respect to this orientation.
- **[F-L-1] Uniqueness of zero-sum representative — Accepted.** §2.3 (line 121) now includes the one-line uniqueness argument: $c' = c + k\mathbf{1}$ zero-sum forces $k = -\tfrac{1}{N}\sum c_i$.
- **[F-L-2] $N = 1, 2$ exclusion reminder — Accepted.** Folded into the §2 opening paragraph (line 79), which explicitly notes the degeneracy of low $N$ and cross-refs §1.3.
- **[N-L-1] Gram matrix presentation order — Accepted.** §2.4 (lines 139–147) now presents $G_{ij}$ element-wise from the basis inner products of §2.1 first, then states the closed matrix form $G = \tfrac{N}{N-1} I - \tfrac{1}{N-1} J$.
- **[N-L-2] $(l, n, m, p)$ vs $(c_1, c_2, c_3, c_4)$ — Accepted.** §2.5 (line 168) now writes $(l, n, m, p) := (c_1, c_2, c_3, c_4)$ explicitly.

### Disposition counts

- Accepted: 13 (5 blocking + 8 non-blocking)
- Accepted with modification: 1 ([F-H-2], Option B chosen over Option A)
- Rejected: 0

### Propagation check

The two propagation vectors to check were:

1. **"Formally the same" / formal-equivalence language outside §2.** Grep for `formally the same`, `formal equivalence`, `same structure`, `structurally` across the whole manuscript returned:
   - Line 41 (§1.1): "Barycentric coordinates … are the same structure with a different normalization." — *No change needed.* This is a strict mathematical identification of barycentric and simplicial coordinate systems (they are the same object up to normalization), not the disputed gauge-class / CRNT parallel. Reading it in context confirms no overclaim.
   - Line 41 (§1.1): "All are facets of the same underlying object." — *No change needed.* Refers to the coordinate-system identification (Quadray / 4t / barycentric / probability simplex), which is mathematically defensible at the level claimed.
   - Line 49 (§1.2 item 1): Already correctly softened in §1 Cycle 1 ("structurally analogous … interpretive motivation, not as a formal equivalence of categories"). The new §2.2.1 language is modelled directly on this passage.
   - Line 67 (§1.3): No formal-equivalence claim.
   - Line 516 (§9 Discussion): "exhibit the gauge-direction plus zero-sum-hyperplane structure described here" — *No change needed.* Uses "exhibit the structure," not "are formally the same." Already consistent with §1.2 item 1.
   - §10 Conclusion (lines 522–524): No cross-disciplinary formal-equivalence language present.

   **Conclusion of propagation check for [N-C-1] / [F-H-1]: the regression was isolated to Remark 2.1. No out-of-§2 edits required.**

2. **"Basis" terminology sweep.** Not applicable — Option B was chosen, so no sweep was performed. The parenthetical acknowledgement at §2.1 (lines 83–84) is the entire treatment. **No out-of-§2 edits required.**

### Sites touched outside §2

*None.* All edits are confined to §2 (lines 77–168 of the revised manuscript).
