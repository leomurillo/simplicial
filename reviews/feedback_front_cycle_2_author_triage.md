# Front-Matter Cycle 2 — Author triage record

**Scope.** Human-authorized Option A: clear all convergent Cycle 1 findings in a single pass across the Title + Abstract + Keywords + MSC 2020 + AI-Note block + §1 (§§1.1–1.3) of `simplicial_vector_calculus.md`.

**File edited:** `simplicial_vector_calculus.md` front matter (lines 1 through end of §1.3). Additionally: `reviews/open-issues.md` updated to mark `[L-2-1]` RESOLVED. No theorem numbers moved, no proofs touched, no References changes.

---

## Convergent findings landed (both reviewers)

### `[F1-M-2]` + `[F1-Y-L-1]` — §1.2 item 3 two-slot gauge-invariance upgrade (closes `[L-2-1]`)

**Landed, Theorem 4.1(1)-verbatim form.** The parenthetical in §1.2 item 3 now reads:

> the inner product is gauge-invariant as a scalar in both arguments ($\langle a + k\mathbf{1}, b + m\mathbf{1}\rangle = \langle a, b\rangle$)

This is the Theorem 4.1(1)-verbatim form (not the longer "$x \mapsto x + k\mathbf{1}$ and $y \mapsto y + m\mathbf{1}$" periphrastic form), trading a clause for a displayed equation: the scalar-valued, two-slot invariance is now readable at a glance. `[L-2-1]` is marked RESOLVED in `open-issues.md` with a pointer back to this triage.

### `[F1-L-5]` + `[F1-Y-L-2]` — Keywords revision (plus user-directed `barycentric coordinates`)

**Landed.** The new Keywords line reads:

> **Keywords:** simplicial coordinates, Quadray coordinates, barycentric coordinates, overcomplete coordinates, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues formula, Lie algebra, rotation.

**Rationale:** the 12-item list merges Reviewer X's structural-vocabulary additions (`gauge direction`, `Hodge dual`, `wedge product`) with Reviewer Y's overcompleteness framing (`overcomplete coordinates`), drops the bare `Quadray` in favor of `Quadray coordinates` (§1.1 parity), and adds the user-directed `barycentric coordinates` as the mainstream synonym for discoverability on arXiv — the paper's construction is related to but not identical with barycentric, and the keyword aids search independently of any body-text rename. `gauge redundancy` (Y's secondary suggestion) is omitted because `gauge direction` is the paper's canonical term and the two together would be redundant at keyword granularity.

### `[F1-L-1]` + `[F1-Y-H-2]` — Abstract paragraph 4 structural rewrite

**Landed.** The old paragraph 4 opened on a near-verbatim restatement of paragraph 2's thesis, closed on "future work" for higher $N$, and repeated `admits` stylistically. The rewrite:

- Deletes the redundant opening sentence outright (paragraph 4 now begins "For $N = 4$ we prove $K^3 = -K$ and derive the scaling constant $1/\sqrt{3}$ from first principles …").
- Moves the higher-$N$ Hodge-dual mention into a parenthetical aside on the uniqueness sentence ("higher $N$ proceeds via Hodge duals of wedge products of arity $N - 3$, sketched in §8").
- Lands on the $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ Lie-algebra-isomorphism reflection — the paper's structural punchline — rather than on a future-work disclaimer.
- Resolves the `admits` stylistic repetition (`[F1-L-1]`) as a side effect: the old "admits a 9-multiplication kernel … admits the analogous construction" is now "supplies a 9-multiplication kernel … proceeds via Hodge duals …".
- Replaces the mild CS jargon "apply operations" (`[F1-Y-L-3]`) with "applying rotations to zero-sum inputs".

Net effect: 4 paragraphs (context → compatibility framework → enumerated operators → $N = 4$ synthesis landing), tighter than before, no near-duplication either within the Abstract or with the §9 closing.

## Reviewer X findings landed (Mediums)

### `[F1-M-1]` — Abstract hedge on the $N = 4$ uniqueness sentence

**Landed.** The Abstract uniqueness sentence now reads:

> We identify $N = 4$ as the unique case *within the simplicial wedge–Hodge framework developed here* in which the construction yields a binary cross product and closed-form exponential …

The italicized hedge is verbatim with the canonical §1.2 item 6 / §8.1 / §9 phrasing. The regression-of-`[S9-M-2]`-at-the-Abstract-level concern is cleared.

### `[F1-M-3]` — "unit vector" → "zero-sum unit axis" in Abstract item 2

**Landed.** Abstract item 2 now reads: "… satisfying the Lie-algebraic identity $K^3 = -K$ when $u$ is a zero-sum unit axis." This matches Def 3.1 and Theorem 3.3 exactly; a reader applying the Abstract claim to a generic Euclidean unit vector no longer falls out of the theorem's hypotheses. The short form was chosen over the long parenthetical expansion in the interest of Abstract economy.

### `[F1-M-4]` — "autonomous *presentation*" gloss in §1.3

**Landed.** A new sentence has been appended to the "simplicial / Quadray / zero-sum hyperplane / intrinsic" terminology paragraph in §1.3 (immediately before the "(mass-action ray)" parenthetical):

> Section 4 and the Conclusion additionally describe the resulting calculus as an *autonomous presentation* of the algebraic layer of 3D Euclidean vector calculus: *autonomous* in the sense that, once the simplicial Gram data of §2 is fixed, the construction proceeds without recourse to a Cartesian frame; *presentation* rather than "theory" because it is isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5.

This anchors the phrasing used in Remark 4.2 and §9 at §1.3 — §1 now previews the framing rather than introducing it twice later in the paper without antecedent.

## Reviewer Y findings landed (Highs + Medium)

### `[F1-Y-H-1]` — Abstract paragraph 2/4 near-verbatim redundancy

**Landed.** Absorbed into the `[F1-Y-H-2]` structural rewrite above: the old paragraph 4 opening "Together these operators constitute an intrinsic algebraic calculus … once the simplicial Gram data is fixed, all formulas are expressible without further reference to a Cartesian frame." (near-verbatim with paragraph 2 lines 15–16) has been deleted outright. Paragraph 4 now opens directly on the $N = 4$ specifics.

### `[F1-Y-H-3]` — Duplicated AI disclosure

**Landed.** The standalone "## A Note on the Use of AI Tools" section (former lines ~27–33) has been deleted in its entirety. The disclosure in Acknowledgments (~line 499) is retained unchanged and is now the sole placement, which is the standard convention. The front-matter flow is now Abstract → Keywords → MSC → `---` → `## 1. Introduction` (one `---` separator retained, not two).

### `[F1-Y-M-1]` — §1.3 DEC + FEEC merge

**Landed.** The single-sentence "**Finite element exterior calculus.**" paragraph (former line 67) has been folded into the "**Relation to discrete exterior calculus.**" paragraph as its final sentence, with the boldface label relabeled to "**Relation to exterior calculus.**" to reflect the merged scope. Both [Arnold-Falk-Winther] references are preserved in place; no citations were dropped.

## Reviewer X Lows taken (four of seven)

### `[F1-L-3]` — §1.2 item 5: "requiring" → "invoking"

**Landed.** Single-token harmonization; §1.2 item 5 now reads "without invoking the $S^3$ double cover" matching §7.4 and §9.

### `[F1-L-4]` — §1.2 item 6: hedge-wording harmonization

**Landed.** Replaced "Within the simplicial / Hodge-dual / axis-to-skew-operator framework developed here" with the italicized canonical "*Within the simplicial wedge–Hodge framework developed here*" matching §8.1 / §9. Semantically equivalent, stylistically harmonized across all four appearances (§1.2, §8.1, §9, Abstract).

### `[F1-L-5]` — Keywords revision

**Landed** — covered by the convergent section above.

### `[F1-L-6]` — MSC 2020 revision

**Landed.** The new MSC line reads:

> **MSC 2020:** 15A72 (multilinear algebra), 15A75 (exterior algebra, Grassmann algebras), 22E60 (Lie algebras of Lie groups), 53A45 (differential geometric aspects in vector and tensor analysis), 65D18 (numerical aspects of computer graphics).

**Change log:** **added** `15A75 (exterior algebra, Grassmann algebras)` to classify the §3.4 / §8 wedge–Hodge construction; **replaced** `22E70 (applications of Lie groups to physical sciences)` with `22E60 (Lie algebras of Lie groups)` which more accurately classifies the $\mathfrak{so}(3)$ / $K^3 = -K$ / exponential-map material of §§3–5; **kept** `15A72`, `53A45`, `65D18` unchanged.

## Reviewer X Lows deferred (three of seven)

### `[F1-L-1]` — stylistic `admits` repetition

**Covered — not taken as a separate edit.** The Abstract paragraph 4 rewrite eliminates the duplicate `admits` as a side effect. The word `admits` no longer appears anywhere in the rewritten Abstract paragraph 4.

### `[F1-L-2]` — Rodrigues display with explicit $R(u,\theta)$ / $K(u)$ arguments in the Abstract

**Not taken.** The Abstract item 3 display was left as `$R = I + \sin\theta\, K + (1 - \cos\theta)\, K^2$` for Abstract economy, since the full-argument form is displayed both in §1.2 item 4 and in §1.3's "**Rodrigues formula.**" paragraph (the latter appearing 20 lines later). Reviewer X flagged as "log-only, acceptable either way"; I agree. No open-issues entry needed.

### `[F1-L-7]` — §1.3 paragraph-boldface consistency cosmetic

**Not taken.** Defer to the LaTeX-conversion polish pass, where a uniform paragraph-label convention can be imposed via macro. Cosmetic only.

## Reviewer Y Lows taken

### `[F1-Y-L-1]` — §1.2 item 3 upgrade

**Landed** — convergent with Reviewer X, covered in the Convergent findings section above.

### `[F1-Y-L-2]` — Keywords granularity

**Landed** — convergent with Reviewer X, covered in the Convergent findings section above.

### `[F1-Y-L-3]` — "apply operations" → "applying rotations to zero-sum inputs"

**Landed.** Resolved as part of the Abstract paragraph 4 rewrite. The mild CS jargon is gone; the replacement phrasing reads naturally in a math-heavy Abstract.

---

## Shape and scope of the rewritten front matter

- **Abstract:** 4 paragraphs — (1) context + gauge direction + hyperplane isometry, (2) framework statement + scalar-vs-vector compatibility distinction, (3) enumerated operators 1–3, (4) $N = 4$ synthesis landing on the 9-mult kernel + $\mathfrak{so}(3)$ reflection. Length slightly tighter than Cycle 1 (synthesis, not padding). No near-verbatim repetitions between paragraph 2 and paragraph 4; no near-duplication of §9's closing.
- **Keywords:** 12 items, all with a discovery-path rationale.
- **MSC 2020:** 5 codes, ordered numerically.
- **Front-matter flow:** Abstract → Keywords → MSC → `---` → `## 1. Introduction`. The standalone AI-note section is gone; Acknowledgments retains the disclosure.
- **§1 flow:** §1.1 Motivation → §1.2 Contributions (6 items, hedge on item 6, two-slot gauge-invariance on item 3) → §1.3 Terminological notes and low-$N$ degeneracies. §1.3 now opens with a single merged "**Relation to exterior calculus.**" paragraph (was two paragraphs), continues with the terminology paragraph (now including the "autonomous *presentation*" gloss), and closes with **Rodrigues formula.** + **Low-$N$ degeneracies.** paragraphs unchanged.
- **Propagation:** no cross-section edits required. All cross-references (Theorem 4.1, Remark 4.2, §2.4, §2.5, §3.4, §7, §8, §9) remain valid.
- **No new `open-issues.md` entries added.** `[L-2-1]` marked RESOLVED.

## Cycle status

All convergent and loop-blocking Cycle 1 findings landed in one pass:

- Reviewer X: **0C / 0H / 4M / 7L** — all 4 Mediums landed; 4 of 7 Lows taken; 3 Lows deferred or covered (log-only).
- Reviewer Y: **0C / 3H / 1M / 3L** — all 3 Highs landed; the Medium landed; all 3 Lows landed.

Front matter is ready for Cycle 2 re-review. Expectation: double GREEN, mirroring the §7 / §8 / §9 Cycle 2 pattern.

## Terminology note (deferred, out of scope)

Per directive, the open question on whether to replace "simplicial" with "barycentric" globally across the body is being adjudicated by both reviewers in parallel. The Keywords line now contains both `simplicial coordinates` and `barycentric coordinates` regardless of the outcome of that adjudication; if the rename lands, it will propagate to the §1 text edited in this pass via a separate script pass, not by the Author.
