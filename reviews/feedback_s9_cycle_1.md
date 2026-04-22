# §9 Cycle 1 — Synthesis

**Date.** 2026-04-21
**Scope.** Initial review cycle for `simplicial_vector_calculus.md` §9 "Conclusion" (lines 487–491, two paragraphs).

## Inputs

- Reviewer X (formalism): `reviews/feedback_s9_cycle_1_reviewer_x.md` — **STATUS: AMBER** (0C / 0H / 3M / 5L).
- Reviewer Y (narrative): `reviews/feedback_s9_cycle_1_reviewer_y.md` — **STATUS: AMBER** (0C / 2H / 1M / 0L).

## Outcome

**§9 Cycle 1: AMBER (double).** §9 is factually accurate and every numerical cross-reference resolves, but both auditors flag non-trivial regressions from precision/tone the body was specifically rewritten to carry.

- **Reviewer X (formalism):** Three Mediums — the summary phrase "close on the hyperplane and commute with the gauge action" collapses the scalar-vs-vector distinction that the Abstract, §1.2 item 3, and Theorem 4.1 now keep precise; the "$N=4$ distinguished by $\dim\mathfrak{so}(3)=3$ … permits a binary cross product" sentence drops the *within the wedge–Hodge framework* hedge that §1.2 item 6 and §8.1 carry; and "the novelty lies in" lists three items, omitting Theorem 4.1 (the joint gauge-compatibility theorem).
- **Reviewer Y (narrative):** Two Highs — paragraph 1 is near-verbatim with the Abstract (redundancy failure mode), and the final sentence duplicates §8's "future work" signposting, ending the paper away from its own $N=4$ achievement rather than landing it.

No Critical findings. No Highs on the formalism side. The two narrative Highs are both single-paragraph rewrites (not proof-level issues), so the Cycle 2 Author pass should be compact.

## Convergent / compatible findings

`[S9-Y-H-1]` (Abstract redundancy) and `[S9-M-1]` (scalar-vs-vector precision regression) are mutually reinforcing: both point at paragraph 1, and the cleanest fix is a single rewrite that both (a) condenses the mechanical summary and (b) restores the three-clause structure matching Theorem 4.1.

`[S9-Y-H-2]` (weak closing sentence / §8 duplication) and `[S9-L-5]` (dropped arity-$N-3$ qualifier) and `[S9-L-2]` ("simplicial exterior calculus" DEC-collision terminology) all target the final sentence. Either drop the sentence (per Y-H-2's strong form) or — if retained — shorten and fix its terminology (per L-2) and restore the arity qualifier (per L-5).

`[S9-Y-M-1]` (repetitive framing between paragraphs) suggests merging the two paragraphs into a single arc: "autonomous *presentation* thesis → computational viability → structural significance of the $N=4$ coincidence." This naturally carries `[S9-M-2]`'s hedge rewrite and `[S9-M-3]`'s novelty-list expansion as well.

## Recommendation

The cleanest Cycle 2 Author pass is a **wholesale rewrite of §9** that:

1. Merges paragraphs 1 and 2 into one (or two cleanly distinct) paragraphs with the structure Reviewer Y proposes: autonomous presentation → what makes it computationally viable → structural significance of $N=4$.
2. Restores the scalar-vs-vector three-clause precision of Theorem 4.1 in the summary phrase (`[S9-M-1]`).
3. Adds the "within our framework" hedge to the $N=4$ uniqueness sentence, matching §1.2 item 6 and §8.1 (`[S9-M-2]`).
4. Expands the "novelty" list to include Theorem 4.1 (the joint gauge-compatibility theorem) alongside the cyclic-difference $K(u)$, the $\mathrm{SO}(4)\cap\mathrm{Stab}(\mathbf{1})$ lift, and the 9-mult kernel (`[S9-M-3]`).
5. Drops the final "leave to future work" sentence (or moves it earlier as a one-clause nod), and writes a new closing sentence that lands the paper's $N=4$ achievement (`[S9-Y-H-2]`).
6. Takes the cheap Lows while the paragraph is open: displayed formula in explicit $R(u,\theta) = \dots$ form (`[S9-L-3]`); "restricted to $H$" clarifier (`[S9-L-4]`); arity-$N-3$ qualifier if the higher-$N$ sentence is retained (`[S9-L-5]`); replace "simplicial exterior calculus" with the §8-consistent "simplicial wedge–Hodge" phrasing (`[S9-L-2]`); drop or replace "complete" (`[S9-L-1]`).

Expected Cycle 2 output: §9 shrinks to one tighter paragraph (or two lean paragraphs), with every Cycle 1 finding closed in one pass. All issues are copy-edit-depth — no theorem numbers move, no proofs touched.

## Options for the user

- **Option A (recommended).** Launch §9 Cycle 2 Author pass now with the combined directive above. Expect clean double-GREEN on verification. Mirror of the §8 Cycle 2 pattern.
- **Option B.** Defer §9 Cycle 2 to the Abstract + §1 harmonization pass (since `[S9-M-1]` and `[S9-M-2]` are the same precision/hedge family that the Abstract/§1 harmonization will audit). Trade-off: §9 remains open for slightly longer.
- **Option C.** Apply a surgical spot-patch on the two narrative Highs only, leave the Mediums for the harmonization pass. Fastest path to "Conclusion is not embarrassing for a pre-print," but leaves the precision regressions in place.
