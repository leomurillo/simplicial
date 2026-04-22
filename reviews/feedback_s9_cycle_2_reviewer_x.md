# §9 Cycle 2 — Reviewer X (Formalism verification)

**Date.** 2026-04-21
**Scope.** `simplicial_vector_calculus.md` §9 "Conclusion" after the Cycle 2 rewrite.
**Inputs.** `reviews/feedback_s9_cycle_1_reviewer_x.md` (Cycle 1 findings); `reviews/feedback_s9_cycle_2_author_triage.md` (Author landing notes).
**Cross-references re-verified.** Abstract (lines 11–26), §1.1, §1.2 item 3 and item 6, §3.1 and Definition 3.1 in §3.2, Theorem 3.3, Theorem 4.1 + Remark 4.2, §7 and §7.4, §8.1, §8.2.

## Overall status

**STATUS: GREEN.** All three Cycle 1 Mediums CLOSED. All five Cycle 1 Lows CLOSED (three taken directly, two cleared by the Medium/High rewrites). No new Critical, High, or Medium findings. One optional Low observation (`[S9-V-L-1]`) on a pointer-granularity choice; non-blocking.

| Severity | Count | IDs |
|---|---|---|
| Critical | 0 | — |
| High | 0 | — |
| Medium | 0 | — |
| Low (new, optional) | 1 | `[S9-V-L-1]` |

## Per-finding verdicts

### `[S9-M-1]` — three-clause scalar/vector precision for closure/invariance — CLOSED

Cycle 2 §9 now states:

> Theorem 4.1 makes this precise in three clauses — the inner product is scalar-valued and gauge-invariant in both arguments, while the cross product $K(u)$ and the rotation $R(u,\theta) := \exp(\theta K(u))$ are vector-valued, preserve $H$, and respectively annihilate and fix the gauge direction $\mathbf{1}$.

Cross-check against Theorem 4.1:
- Clause (1) "Scalar invariance" — matches §9's "scalar-valued and gauge-invariant in both arguments." ✓
- Clause (2) hyperplane closure + gauge annihilation for $K$ — matches §9's "preserve $H$" and "annihilate … $\mathbf{1}$." ✓
- Clause (3) hyperplane closure + gauge fixing for $R$ — matches §9's "preserve $H$" and "fix … $\mathbf{1}$." ✓

Scalar/vector distinction explicit; operators named individually with their distinct invariance properties; anchored to Theorem 4.1 by name. Matches the Abstract's post-`[F-M-7]` phrasing.

### `[S9-M-2]` — framework hedge on the $N = 4$ uniqueness claim — CLOSED

Cycle 2 §9:

> The $N = 4$ case is distinguished, *within the simplicial wedge–Hodge framework developed here*, by the coincidence $\dim \mathfrak{so}(3) = 3$, which permits a binary cross product and closed-form exponential …

Verbatim match with §8.1's hedge phrasing. Consistent with §1.2 item 6. Italicization and mid-sentence placement block the adversarial "pan-dimensional implication" read. The absence of a separate Eckmann/octonion disclaimer inside §9 is acceptable for a Conclusion — §1.2 item 6 and §8.1 carry the explicit $n = 7$ out-of-framework context.

### `[S9-M-3]` — novelty inventory includes Theorem 4.1 — CLOSED

Cycle 2 §9:

> the principal technical novelties are the joint gauge-compatibility theorem of §4, the explicit cyclic-difference form of $K(u)$ (§3.1), the gauge-compatible $4 \times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, and the 9-multiplication apply kernel of §7.

Theorem 4.1 is present, placed first as the organizing result, labelled "the joint gauge-compatibility theorem of §4" — matching §1.2 item 3. Framing softened from definite "the novelty lies in" to "the principal technical novelties are," removing the implicit exhaustiveness. Sub-pointers to §3.1, §4, §7 add traceability.

The framework-internal uniqueness of §1.2 item 6 is not added as a fifth list item, but is carried in paragraph 2's structural-significance sentence. Reasonable compromise: the list now reads as "principal technical novelties" (four structural/computational theorems) while paragraph 2 lands the interpretive uniqueness.

### `[S9-L-1]` — "complete" removed / replaced — CLOSED

"complete intrinsic *algebraic* vector calculus" is gone. The opening sentence now uses "autonomous *presentation* of the algebraic layer of 3D Euclidean vector calculus"; the closing sentence uses "self-contained on the zero-sum hyperplane." §8.3's open rotation-composition question is no longer at risk of contradiction.

### `[S9-L-2]` — "simplicial exterior calculus" coinage removed — CLOSED

The phrase "program of simplicial exterior calculus" does not appear. The `[S9-M-2]` hedge uses the §8.1/§8.2-consistent "simplicial wedge–Hodge framework" phrasing; the higher-$N$ parenthetical refers to §8 by number without renaming. DEC/AFW collision risk eliminated at the source.

### `[S9-L-3]` — displayed formula uses $R(u,\theta)$ / $K(u)$ explicitly — CLOSED

Cycle 2 display:

$$R(u, \theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2$$

Matches §5 eq (5.1) and §5.3 argument conventions. Surrounding prose consistent.

### `[S9-L-4]` — "(after restriction to $H$)" now explicit in the $V$-conjugacy sentence — CLOSED

Cycle 2 §9: "these operators are carried (after restriction to $H$) to their classical $\mathbb{R}^3$ counterparts." Parenthetical resolves the tacit-restriction ambiguity flagged in Cycle 1.

### `[S9-L-5]` — arity-$N-3$ qualifier preserved in higher-$N$ pointer — CLOSED

Cycle 2 §9: "(higher-$N$ generalizations, via Hodge duals of wedge products of arity $N - 3$, are discussed in §8)." Qualifier retained; blocks "casual reader infers binary cross products extend to all $N$" misread. Consistent with Abstract and §8.

## Cross-section coherence

- **Abstract vs §9.** No sentence duplicates an Abstract sentence. The Abstract lists what was done; §9 synthesizes what it adds up to. Same technical claims, same framework hedge — factual agreement, no rhetorical stutter.
- **§1.2 vs §9.** Items 2–5 represented explicitly in the novelty list; item 6 in the structural-significance sentence; item 1 (gauge terminology) omitted, consistent with "principal technical novelties."
- **§1.2 item 6 ↔ §8.1 ↔ §9 hedge.** All three carry the "*within the … framework developed here*" scoping. §9 matches §8.1 verbatim.
- **§4 Remark 4.2 ↔ §9 paragraph 1 sentence 1.** Remark 4.2's forward reference to §9 for "autonomous *presentation*" now resolves.
- **§1.1 motivating question ↔ §9 closing sentence.** §1.1 asks whether the coordinate description supports an intrinsic vector calculus; §9's closing sentence answers this precise question for the algebraic layer at $N=4$. Loop closes correctly.
- **Numeric cross-references.** §§1.1, 2.5, 3.1, 3.4, 4, 7, 8 all resolve.

## New findings

### Low (optional)

**`[S9-V-L-1]` — "(§3.1)" pointer granularity for the cyclic-difference form.**
The cyclic-difference form of $K(u)$ is *introduced and displayed* in §3.1 and *formally defined* in Definition 3.1 of §3.2. A pedantic reader could prefer "(§3.1–3.2)" or "(Definition 3.1)." Substantively the §3.1 pointer is correct. Non-blocking; flagged for the record.

## Certification

All Cycle 1 Mediums (`[S9-M-1]`, `[S9-M-2]`, `[S9-M-3]`) CLOSED. All Cycle 1 Lows (`[S9-L-1]`–`[S9-L-5]`) CLOSED. No new Highs or Mediums introduced.

**STATUS: GREEN.**
