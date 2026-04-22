# §9 Cycle 2 — Author triage record

**Scope.** Human-authorized Option A: clear both Cycle 1 narrative Highs, all three Mediums, and take the cheap Lows in a single compact rewrite of §9 "Conclusion" (was lines 487–491 of `simplicial_vector_calculus.md`).

**File edited:** `simplicial_vector_calculus.md` §9. No References changes, no theorem numbers moved, no proofs touched. All retained cross-references (§§1.1, 2.5, 3.1, 3.4, 4, 7, 8) resolve correctly in the current body.

---

## Highs landed (both)

### `[S9-Y-H-1]` — Redundancy with the Abstract (Reviewer Y, High)

**Landed.** Paragraph 1 of the old §9 (a near-verbatim restatement of the Abstract's final paragraph — operators, $K^3=-K$, Rodrigues, gauge fixation, 9-mult kernel) has been deleted wholesale. The rewrite replaces the mechanical re-listing with a different logical move: open on the *autonomous presentation* thesis (the interpretive content), use Theorem 4.1 to land the scalar/vector precision, and only then cite the $N = 4$ specifics — each for a structural reason (cubic identity → Rodrigues formula → orthogonality + 9-mult), not as a summary of theorems.

Net effect: no sentence in rewritten §9 is a near-duplicate of any Abstract sentence. The Abstract lists what was done; §9 tells the reader what it adds up to.

### `[S9-Y-H-2]` — Weak closing sentence / §8 duplication (Reviewer Y, High)

**Landed (preferred form).** The final "Higher-$N$ generalizations exist via Hodge duals of wedge products and open a program of simplicial exterior calculus that we leave to future work" sentence has been removed as a standalone sentence. Its content is preserved only as a *parenthetical aside* inside the structural-significance sentence of paragraph 2:

> (higher-$N$ generalizations, via Hodge duals of wedge products of arity $N - 3$, are discussed in §8)

The new closing sentence lands the paper's $N = 4$ achievement with a §1.1-loop-closing flourish:

> This answers the motivating question of §1.1 affirmatively for $N = 4$: the algebraic layer of 3D Euclidean vector calculus is self-contained on the zero-sum hyperplane of the simplicial coordinate frame, with no recourse to a Cartesian basis required at any stage.

The reader's last impression is the $N = 4$ achievement, framed as the answer to §1.1's motivating question — not future work. The closing "closes the loop" that Reviewer Y praised in the assessment's first sentence.

---

## Mediums landed (all three)

### `[S9-M-1]` — three-clause precision restored (Reviewer X, Medium)

**Landed.** The summary phrase "close on the hyperplane and commute with the gauge action" is gone. Replaced by an explicit three-clause statement naming Theorem 4.1:

> Theorem 4.1 makes this precise in three clauses — the inner product is scalar-valued and gauge-invariant in both arguments, while the cross product $K(u)$ and the rotation $R(u,\theta) := \exp(\theta K(u))$ are vector-valued, preserve $H$, and respectively annihilate and fix the gauge direction $\mathbf{1}$.

This mirrors the Abstract's post-`[F-M-7]` phrasing and Theorem 4.1's structure, in a form compact enough not to bloat a Conclusion. The scalar/vector distinction is explicitly carried; the vector-valued operators are named individually with their distinct invariance properties (annihilate vs. fix); and the statement is bound to Theorem 4.1 by name.

### `[S9-M-2]` — framework hedge on the $N = 4$ uniqueness claim (Reviewer X, Medium)

**Landed (italicized long form).** The structural-significance sentence now reads:

> The $N = 4$ case is distinguished, *within the simplicial wedge–Hodge framework developed here*, by the coincidence $\dim \mathfrak{so}(3) = 3$, which permits a binary cross product and closed-form exponential …

The italicized hedge matches the phrasing established in §1.2 item 6 and in §8.1's second paragraph (`feedback_s8_cycle_2_author_triage.md` `[S8-M-1]` RESOLVED). No separate Eckmann/octonion disclaimer is inserted at this depth — §9 is a Conclusion, not a uniqueness exposition — and the hedge alone is sufficient to block the adversarial "pan-dimensional implication" read. §1.2 item 6 and §8.1 carry the explicit Eckmann context for readers who follow up.

### `[S9-M-3]` — novelty list expanded to include Theorem 4.1 (Reviewer X, Medium)

**Landed, expansion form (reviewer-preferred).** The old three-item list "(a) the explicit cyclic-difference form of $K(u)$, (b) the gauge-compatible $4 \times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, and (c) the 9-multiplication apply kernel" has been expanded to four items, with Theorem 4.1 placed first as the organizing result:

> the principal technical novelties are the joint gauge-compatibility theorem of §4, the explicit cyclic-difference form of $K(u)$ (§3.1), the gauge-compatible $4 \times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, and the 9-multiplication apply kernel of §7.

Two secondary changes folded in:

- **Softened framing.** "The novelty lies in" → "the principal technical novelties are." No longer implicitly exhaustive — but the list is more complete anyway.
- **Section pointers added** (§3.1, §7) for traceability, matching the §4 reference that was already load-bearing.

The framework-internal uniqueness item (§1.2 item 6) is *not* added as a fifth novelty, because §9's paragraph 2 already carries it as the structural-significance sentence; adding it to the list as well would be redundant.

---

## Lows taken (three of five)

### `[S9-L-3]` — displayed formula in $R(u,\theta)$ / $K(u)$ form (taken)

**Landed.** The display now reads

> $$R(u, \theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2$$

matching §5 eq (5.1) and §5.3 argument conventions. The surrounding prose also uses $K(u)^3 = -K(u)$ and $R(u,\theta)$ consistently.

### `[S9-L-4]` — "(after restriction to $H$)" clarifier in the $V$-conjugacy sentence (taken)

**Landed.** The sentence now reads:

> Under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4), these operators are carried (after restriction to $H$) to their classical $\mathbb{R}^3$ counterparts …

Removes the tacit-restriction ambiguity Reviewer X flagged, in one parenthetical.

### `[S9-L-1]` — drop "complete" (taken)

**Landed.** The old opening "supports a complete intrinsic *algebraic* vector calculus" is gone; the new opening is "supports an autonomous *presentation* of the algebraic layer …" (which was previously the paragraph 2 thesis sentence). The closing sentence uses "self-contained" in the §1.1-loop landing, which is the `[S9-L-1]`-recommended replacement. §8.3's open rotation-composition question is no longer contradicted by a "complete" overclaim anywhere in §9.

---

## Lows not taken (two — moot)

### `[S9-L-5]` — arity $N - 3$ qualifier on Hodge-duals-of-wedge-products

**Not separately taken — but covered.** The rewrite *did* retain the qualifier in the parenthetical aside ("higher-$N$ generalizations, via Hodge duals of wedge products of arity $N - 3$, are discussed in §8"), so the Abstract/§9 consistency Reviewer X wanted is preserved. Logged here rather than as "Not taken" because the substance of the finding *is* cleared; the Low is no longer an independent item.

### `[S9-L-2]` — replace "simplicial exterior calculus" with §8-consistent phrasing

**Not separately taken — but covered.** The coinage "program of simplicial exterior calculus" does not appear in the rewrite at all. The framework hedge `[S9-M-2]` uses the §8.1/§8.2-consistent "*simplicial wedge–Hodge framework*" phrasing, and the higher-$N$ parenthetical refers to §8 by number rather than re-naming the program. DEC-collision risk eliminated at the source.

---

## Shape and scope

- **Length.** Two paragraphs — P1 (4 sentences + 1 displayed formula) / P2 (2 sentences). Tighter than the Cycle 1 version (roughly P1: 5 sentences / P2: 4 sentences). Synthesis, not padding.
- **Structural arc (per `[S9-Y-M-1]`).** P1: autonomous-presentation thesis → Theorem 4.1 three-clause precision → $N = 4$ computational viability (cubic identity → Rodrigues → 9-mult kernel) → isometry-to-$\mathbb{R}^3$ + principal novelties. P2: structural significance of the $N = 4$ coincidence (with framework hedge and parenthetical higher-$N$ pointer) → §1.1-loop landing.
- **No repetitive thesis opening between paragraphs.** P1 opens on "autonomous *presentation* of the algebraic layer of 3D Euclidean vector calculus"; P2 opens on "The $N = 4$ case is distinguished, *within the simplicial wedge–Hodge framework developed here*, by …" — distinct roles, no stutter.

## Propagation edits

- **No cross-section edits required.** The rewrite's cross-references (§§1.1, 2.5, 3.1, 3.4, 4, 7, 8) all resolve to existing, content-correct locations. Remark 4.2 — which forward-refers to §9 for the precise sense of "autonomous *presentation*" — remains consistent (§9 still opens on that exact framing).
- **No Abstract / §1 edits required.** §9 is now less redundant with the Abstract *by virtue of the rewrite alone*; no reciprocal tightening of Abstract or §1 is needed for Cycle 2 scope.
- **No `open-issues.md` entries added.** All Cycle 1 findings cleared in this single pass; nothing to carry forward.

## Cycle status

All Cycle 1 findings closed in one pass: 2 Highs + 3 Mediums landed, 3 Lows taken directly, 2 Lows moot (covered by the H/M rewrites). §9 is ready for Cycle 2 re-review. Expectation: double GREEN, mirroring the §8 Cycle 2 pattern.
