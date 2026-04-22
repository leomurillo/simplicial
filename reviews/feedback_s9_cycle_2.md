# §9 Cycle 2 — Synthesis

**Date.** 2026-04-21
**Scope.** Verification re-audit of `simplicial_vector_calculus.md` §9 "Conclusion" following the Author's Cycle 2 rewrite.

## Inputs

- Author triage: `reviews/feedback_s9_cycle_2_author_triage.md`
- Reviewer X verification: `reviews/feedback_s9_cycle_2_reviewer_x.md` — **STATUS: GREEN**
- Reviewer Y verification: `reviews/feedback_s9_cycle_2_reviewer_y.md` — **STATUS: GREEN**

## Outcome

**§9 Cycle 2: GREEN (double).** All Cycle 1 findings CLOSED in a single Author pass — both narrative Highs, all three formalism Mediums, and all five Lows (three taken directly, two cleared by the H/M rewrites). No new Highs or Mediums introduced. One non-blocking Low (`[S9-V-L-1]`) logged for pre-submission polish.

### Highs — all CLOSED

| ID | Cycle 1 finding | Disposition |
|---|---|---|
| `[S9-Y-H-1]` | Paragraph 1 near-verbatim with Abstract | CLOSED — paragraph 1 now synthesizes via the "autonomous presentation" thesis + Theorem 4.1 three-clause precision, no sentence-level duplication |
| `[S9-Y-H-2]` | Paper ended on "future work," diluting the $N=4$ achievement | CLOSED — higher-$N$ signpost demoted to a parenthetical; new closing sentence answers §1.1's motivating question and lands on the $N=4$ achievement |

### Mediums — all CLOSED

| ID | Cycle 1 finding | Disposition |
|---|---|---|
| `[S9-M-1]` | "close on the hyperplane and commute with the gauge action" collapsed scalar/vector distinction | CLOSED — §9 now explicitly restates Theorem 4.1's three clauses (scalar gauge-invariance for inner product; $H$-preservation + respectively annihilating/fixing $\mathbf{1}$ for $K$ and $R$) |
| `[S9-M-2]` | Uniqueness claim lacked "within our framework" hedge | CLOSED — italicized "*within the simplicial wedge–Hodge framework developed here*" verbatim-matches §8.1 |
| `[S9-M-3]` | Novelty list omitted Theorem 4.1 | CLOSED — list expanded to four items with "the joint gauge-compatibility theorem of §4" placed first; framing softened from "the novelty lies in" to "the principal technical novelties are" |
| `[S9-Y-M-1]` | Two paragraphs both opened with the same thesis | CLOSED — paragraph 1 handles synthesis + novelties, paragraph 2 handles structural significance of $N=4$ and §1.1-loop closure |

### Lows

**Taken directly:** `[S9-L-1]` ("complete" → "autonomous"/"self-contained"), `[S9-L-3]` (displayed formula uses $R(u,\theta)$, $K(u)$), `[S9-L-4]` ("(after restriction to $H$)" explicit).

**Cleared by H/M rewrites:** `[S9-L-2]` ("simplicial exterior calculus" coinage replaced with the §8-consistent "simplicial wedge–Hodge framework"), `[S9-L-5]` (arity-$N-3$ qualifier preserved in the retained higher-$N$ parenthetical).

**New (logged to `open-issues.md`):** `[S9-V-L-1]` — "(§3.1)" pointer for the cyclic-difference form could be sharpened to "(Definition 3.1)" or "(§3.1–3.2)" since Definition 3.1 is in §3.2. Non-blocking; pedantic pointer-granularity preference.

## Cross-section coherence

- **Abstract vs §9.** No sentence-level duplication remaining. The Abstract lists *what was done*; §9 synthesizes *what it adds up to*.
- **§1.2 vs §9.** Items 2–5 appear in §9's novelty list; item 6 carried by paragraph 2's structural-significance sentence.
- **§1.2 item 6 ↔ §8.1 ↔ §9.** All three carry the matching "*within the … framework developed here*" hedge.
- **§4 Remark 4.2 ↔ §9 opening sentence.** Remark 4.2's forward reference to §9 for "autonomous *presentation*" now resolves.
- **§1.1 motivating question ↔ §9 closing sentence.** Loop closes cleanly: §9's final sentence explicitly answers §1.1's question for $N=4$.
- **Numeric cross-references.** §§1.1, 2.5, 3.1, 3.4, 4, 7, 8 all resolve.

## Paper-level status

All body sections (§§3–9) are now GREEN. The paper is publication-grade modulo deferred Lows tracked in `reviews/open-issues.md` and any issues that surface during the Abstract + §1 harmonization pass.

## Recommended next step

- **Option A — Abstract + §1 harmonization pass.** With the entire body stabilized, re-audit the Abstract and §1 Introduction against the now-settled §§3–9. This is the natural place to:
  - Check the Abstract's headline claims still match the final body language.
  - Land `[L-2-1]` (§1.2 item 3 two-slot gauge-invariance upgrade).
  - Sweep for cross-section notational consistency one last time.
- **Option B — Empirical cleanup batch.** Clear `[E-Polish-1]`, `[E-Theorem-7-1-Polish]`, `[E-Proposition-6-1-Polish]` script-hardening items in one pass. Independent of the manuscript loop; can run in parallel with Option A or be deferred to the pre-submission sweep.
- **Option C — Pre-submission polish sweep.** Batch-apply all deferred Lows from `open-issues.md` across the whole manuscript in one pass (hyphenation, WLOG asides, footnote/LaTeX-conversion items, clr/ilr vs Fisher up-to-scalar qualifiers, etc.).

**Recommendation:** **Option A** to lock down the front matter against the stabilized body. Option B can run in parallel. Option C is most efficient just before the first arXiv submission.
