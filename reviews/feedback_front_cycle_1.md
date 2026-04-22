# Front-Matter Cycle 1 — Synthesis

**Date.** 2026-04-21
**Scope.** Abstract + Keywords + MSC 2020 + "A Note on the Use of AI Tools" + §1 Introduction (§§1.1–1.3) of `simplicial_vector_calculus.md`. First harmonization pass against the now-stabilized body (§§3–9 all GREEN).

## Inputs

- Reviewer X (formalism): `reviews/feedback_front_cycle_1_reviewer_x.md` — **STATUS: AMBER** (0C / 0H / 4M / 7L).
- Reviewer Y (narrative): `reviews/feedback_front_cycle_1_reviewer_y.md` — **STATUS: AMBER** (0C / 3H / 1M / 3L).

## Outcome

**Double AMBER.** No Critical findings. Reviewer X flags no formalism Highs; Reviewer Y flags three narrative Highs, all paragraph-level rewrites (none touches a theorem). The two reports are convergent on three items (§1.2 item 3 two-slot upgrade; Keywords revision; Abstract tone/structure issues) and orthogonal on the rest, each catching concerns in their respective lane.

## Convergent findings (both reviewers)

| Convergence | Reviewer X | Reviewer Y | Disposition |
|---|---|---|---|
| §1.2 item 3 two-slot gauge-invariance upgrade (finally landing `[L-2-1]`) | `[F1-M-2]` Medium | `[F1-Y-L-1]` Low | Take the stronger — treat as Medium; upgrade to Theorem 4.1(1) form; mark `[L-2-1]` RESOLVED. |
| Keywords need revision | `[F1-L-5]` concrete list emphasizing `gauge direction`, `Hodge dual`, `wedge product` | `[F1-Y-L-2]` concrete list emphasizing `overcomplete coordinates`, `gauge redundancy` | Merge both proposals into one revised list (below). |
| Abstract line 21 higher-$N$ sentence lands weakly | `[F1-L-1]` stylistic verb repetition ("admits") | `[F1-Y-H-2]` closing-sentence dilution | Reviewer Y's fix is stronger; take that (move higher-$N$ into parenthetical, close on $N=4$ achievement). Incidentally resolves `[F1-L-1]`. |

## Reviewer X — summary (formalism)

- **`[F1-M-1]`** Abstract line 21 "unique case" sentence drops the "within the simplicial wedge–Hodge framework" hedge carried by §1.2 item 6, §8.1, §9. Regression of the `[S9-M-2]` pattern, now at the Abstract level. Add the hedge verbatim.
- **`[F1-M-2]`** §1.2 item 3 one-slot shorthand (long-deferred `[L-2-1]`) → upgrade to two-slot Theorem 4.1(1) form.
- **`[F1-M-3]`** Abstract item 2 line 18 uses "unit vector" where Def 3.1 + Theorem 3.3 require "zero-sum unit axis" (both conditions needed for $K^3 = -K$). A careful reader applying the Abstract claim to a generic unit vector would fall out of the theorem's hypotheses.
- **`[F1-M-4]`** §1.3 does not anchor the "autonomous *presentation*" framing that §4 Remark 4.2 and §9 use as the headline descriptor. Add a one-sentence gloss.
- Lows: stylistic `admits` repetition; optional $R$/$K$ argument parity in display; "without requiring" → "without invoking" for §9 parity; §1.2 item 6 hedge wording alignment; Keywords additions; MSC 2020 revision (add **15A75** Exterior algebra; consider 22E60 vs 22E70); §1.3 boldface cosmetic.
- **Proposed MSC 2020:** `15A72, 15A75 (NEW), 22E60 (replaces 22E70), 53A45, 65D18`.
- **Proposed Keywords (X):** `simplicial coordinates, Quadray coordinates, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues formula, Lie algebra, rotation`.

## Reviewer Y — summary (narrative)

- **`[F1-Y-H-1]`** Abstract paragraph 2 and paragraph 4 near-verbatim repeat the "intrinsic algebraic vector calculus … once the simplicial Gram data is fixed, …" framing. Delete the restatement in paragraph 4; open paragraph 4 directly with the $N=4$ achievements.
- **`[F1-Y-H-2]`** Abstract closes on "future work" for higher $N$, mirroring the exact narrative flaw fixed in §9. Move higher-$N$ Hodge dual to a parenthetical and end on the paper's actual contribution.
- **`[F1-Y-H-3]`** Duplicated AI disclosure (lines 29–31 + Acknowledgments). Delete the standalone section; keep the Acknowledgments disclosure (which is the standard placement).
- **`[F1-Y-M-1]`** §1.3 sub-paragraph structure is a mild grab-bag. The one-sentence "Finite element exterior calculus" paragraph belongs merged with the "Relation to discrete exterior calculus" paragraph.
- Lows: §1.2 item 3 upgrade (also X); Keywords granularity (also X); "apply operations" is mild CS jargon in a math Abstract.
- **Proposed Keywords (Y):** adds `overcomplete coordinates, gauge redundancy` to the existing list.

## Combined Keywords proposal

Merging Reviewer X's and Reviewer Y's suggestions:

> **Keywords:** simplicial coordinates, Quadray coordinates, overcomplete coordinates, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues formula, Lie algebra, rotation.

Rationale: drop bare `Quadray` in favor of `Quadray coordinates` (parity with §1.1); add `overcomplete coordinates` (captures §1.1's central structural theme); add `gauge direction` (the paper's principal terminological move, §1.2 item 1); add `Hodge dual` and `wedge product` (§3.4, §8.1–8.2, and §9 novelty list). Drop `gauge redundancy` from Y's list because `gauge direction` is the paper's canonical term and the two together would be redundant-with-each-other at the keyword level. Keep the existing seven keywords. Net: 11 keywords — on the high side but each has a clear discovery-path rationale.

## Combined MSC 2020 proposal

Per Reviewer X:

> **MSC 2020:** 15A72 (multilinear algebra), 15A75 (exterior algebra, Grassmann algebras), 22E60 (Lie algebras of Lie groups), 53A45 (vector and tensor analysis), 65D18 (numerical aspects of computer graphics).

## Recommendation

The total scope is four Mediums + three narrative Highs + seven Lows, but they're all paragraph-level rewrites with heavy overlap between findings. A single Author Cycle 2 pass is sufficient. Expected landing surface:

- Abstract: 4 edits (delete paragraph 4 restatement; restructure closing to land on $N=4$; insert hedge in line 21 uniqueness sentence; replace "unit vector" with "zero-sum unit axis"; optional "apply operations" → "applying rotations to zero-sum inputs").
- Keywords: 1 edit (new list).
- MSC 2020: 1 edit (new list).
- "A Note on the Use of AI Tools" block: 1 deletion.
- §1.2 item 3: 1 two-slot upgrade, close `[L-2-1]`.
- §1.2 item 5: 1 single-token harmonization ("requiring" → "invoking").
- §1.2 item 6: 1 hedge-wording harmonization (match §8.1/§9).
- §1.3: add "autonomous *presentation*" gloss; merge the FEEC paragraph into the DEC paragraph.

Target: double-GREEN Cycle 2 verification, matching the §7, §8, §9 Cycle 2 pattern.

## Options

- **Option A (recommended).** Launch Front-Matter Cycle 2 Author pass now with the combined directive above. Expect double-GREEN verification.
- **Option B.** Split: take the Highs (Abstract restructure + AI-note dedup) now as a fast pre-publication pass; defer the Mediums + Lows to the pre-submission polish sweep. Trade-off: leaves the `[L-2-1]`, `[F1-M-1]`, `[F1-M-3]`, `[F1-M-4]` Mediums open.
- **Option C.** Do everything except the MSC / Keywords edits, then re-poll the user on those (since the classifications have external-facing consequences for indexing and some authors prefer to own those choices directly).

**Recommendation:** **Option A**. All findings are well-understood and the fixes are non-controversial; no reason to split.
