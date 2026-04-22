# §9 Cycle 1 — Reviewer X (Formalism audit)

**Date.** 2026-04-21
**Scope.** `simplicial_vector_calculus.md` §9 "Conclusion" (lines 487–491).
**Cross-references.** Abstract (lines 11–26), §1.2 items 3 and 6, §2.4 (Gram), §2.5 (isometry $V$), §3.1 Def 3.1, §3.4, §4 Theorem 4.1 + Remark 4.2, §5 (Rodrigues derivation), §6 Proposition 6.1, §7 Theorem 7.1 and §7.4 table, §8.1/§8.2; prior output in `reviews/feedback_s8_cycle_2.md` and `reviews/open-issues.md`.

## Overall status

**STATUS: AMBER.** No Critical, no High. Three Medium findings, all concerning loss of precision relative to body-text statements that the paper specifically revised to make precise in earlier cycles. Five Lows.

| Severity | Count | IDs |
|---|---|---|
| Critical | 0 | — |
| High | 0 | — |
| Medium | 3 | `[S9-M-1]`, `[S9-M-2]`, `[S9-M-3]` |
| Low | 5 | `[S9-L-1]` … `[S9-L-5]` |

## Claim-by-claim audit (factual correctness)

Each core factual claim in §9 was matched to a body-text source. With the caveats flagged below, no claim is *literally false*. The issues are precision and consistency with hedges the body was specifically rewritten to carry.

| § 9 claim | Source | Verdict |
|---|---|---|
| Three core operators constructed — inner product, cross product, rotation | §1.2 items 2–4; §§3, 5 | Correct. |
| "Close on the hyperplane and commute with the gauge action" | Theorem 4.1 (1)/(2)/(3) | **Imprecise** — see `[S9-M-1]`. |
| For $N=4$, $K(u)$ satisfies $K^3 = -K$ | Theorem 3.3; Appendix B | Correct. |
| Rodrigues formula $R = I + \sin\theta K + (1-\cos\theta)K^2$ follows by exponentiation | §5 eq (5.1); §5.2 Lie derivation | Correct. |
| $R$ fixes the gauge direction | Proposition 6.1(2); Theorem 4.1(3) | Correct. |
| $R$ is Euclidean orthogonal with $\det = +1$ | Proposition 6.1(1), 6.1(4) | Correct. |
| 9-mult apply kernel for zero-sum inputs | Theorem 7.1 | Correct. |
| "matching quaternion-to-matrix performance" | §7.4 table (row: Quaternion → 3×3 matrix: 9 mults) | Correct, matches the agreed phrasing. |
| "without invoking the $S^3$ double cover" | §7.4 para after table; §1.2 item 5 | Correct; a factual property of the construction, not a superiority claim. |
| "Under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4), the ... operators ... are carried to their classical $\mathbb{R}^3$ counterparts" | §2.5 ($VK(u)V^{-1} = [Vu]_\times$, metric-preserving); §3.4 | Correct; minor tacit restriction-to-$H$, see `[S9-L-4]`. |
| Novelty = cyclic-difference $K(u)$, $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$ lift, 9-mult kernel | §3.1, §1.2 item 4, §7 | Narrower than §1.2 — see `[S9-M-3]`. |
| "$N=4$ distinguished by $\dim \mathfrak{so}(3) = 3$, which permits a binary cross product and closed-form exponential" | §1.2 item 6; §8.1 uniqueness paragraph | Missing framework hedge — see `[S9-M-2]`. |
| "Higher-$N$ generalizations exist via Hodge duals of wedge products" | §8.2; Abstract paragraph 2 | Correct; arity qualifier dropped — see `[S9-L-5]`. |
| "program of simplicial exterior calculus" | New in §9 | Potential collision with DEC — see `[S9-L-2]`. |

## Findings

### Medium

**`[S9-M-1]` — "close on the hyperplane and commute with the gauge action" collapses the scalar/vector distinction** — line 489.

*Problem.* §9's summary bundles the inner product with $K$ and $R$ under the single verb-pair "close on the hyperplane and commute with the gauge action." Strictly:

- The inner product is **scalar-valued and gauge-invariant in both arguments**; "closes on $H$" is not the right description for a bilinear form.
- $K(u)$ is **vector-valued**: preserves $H$ and *annihilates* $\mathbf{1}$.
- $R(u,\theta)$ is **vector-valued**: preserves $H$ and *fixes* $\mathbf{1}$.

Theorem 4.1 is structured in three clauses precisely to keep this distinction, and the Abstract was rewritten in the post-AMBER spot-patch of 2026-04-20 to match (`open-issues.md`, `[F-M-7]` RESOLVED). §9's phrasing is a regression from that precision.

*Proposed fix.* Mirror Theorem 4.1's three-clause structure. For example:

> "We constructed the three core operators — inner product, cross product, and rotation via exponential map — and established that the inner product is gauge-invariant as a scalar, while the cross product and rotation preserve the zero-sum hyperplane and respectively annihilate and fix the gauge direction."

**`[S9-M-2]` — "distinguished by $\dim \mathfrak{so}(3) = 3$ ... permits a binary cross product" lacks the framework hedge** — line 491.

*Problem.* The sentence reads as a clean universal implication: coincidence of dimensions ⇒ binary cross product. That universal implication is false globally — Eckmann's classification admits $n \in \{0,1,3,7\}$, and the $n=7$ (octonion) binary cross product is *not* explained by $\dim\mathfrak{so}(3) = 3$. §1.2 item 6 and §8.1 were explicitly rewritten (§8 Cycle 1 `[S8-M-1]`, CLOSED via `feedback_s8_cycle_2.md`) to carry an italicized "*within the simplicial wedge–Hodge framework developed here*" hedge. §9 drops the hedge.

On a charitable contextual read, "The $N=4$ case" refers implicitly to the construction of this paper, and the hedge is carried by context; on an adversarial read, the sentence looks like a pan-dimensional claim.

*Proposed fix.* Add an inline hedge, e.g.:

> "The $N = 4$ case is distinguished *within the wedge–Hodge framework developed here* by the coincidence $\dim \mathfrak{so}(3) = 3$, which permits a binary cross product and closed-form exponential; the octonion $n = 7$ binary cross product admitted by Eckmann's classification arises outside this framework (§1.2 item 6, §8.1)."

A shorter alternative is to change "permits" to "permits, within this construction,".

**`[S9-M-3]` — "the novelty lies in" lists three items; §1.2 claims six contributions** — line 491.

*Problem.* §9 writes "the novelty lies in (a) the explicit cyclic-difference form of $K(u)$, (b) the gauge-compatible $4\times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, and (c) the 9-multiplication apply kernel of §7." The definite "the novelty lies in" reads as exhaustive. §1.2 enumerates six contributions, three of which (gauge *terminology* item 1; the joint gauge-compatibility theorem item 3 = Theorem 4.1; and the framework-internal uniqueness item 6) are missing here. Most substantively, Theorem 4.1 itself — presented prominently in §1.2 and in Remark 4.2 as the organizing theorem — is not in §9's novelty list.

*Proposed fix.* Either (a) expand the list to match §1.2 (adding the joint gauge-compatibility theorem of §4 and the framework-internal uniqueness of §8.1), or (b) soften to "the novelties include..." / "the principal technical novelties are...". Option (a) is preferred because it is consistent with the earlier contribution list and restores the structural-theorem visibility of §4.

### Low

**`[S9-L-1]` — "complete intrinsic *algebraic* vector calculus"** — line 489.

"Complete" is strong. §8.3 explicitly leaves rotation composition formulas — arguably an algebraic-layer question — as future work. Consider dropping "complete" or replacing with "self-contained" / "closed-form".

**`[S9-L-2]` — "program of simplicial exterior calculus" as new terminology** — line 491.

§1.3 carefully distinguishes the present work from the *discrete exterior calculus* (DEC) of Desbrun–Hirani–Leok–Marsden and the *finite element exterior calculus* of Arnold–Falk–Winther. Introducing a new umbrella "*simplicial exterior calculus*" only in §9 — and only for future work — risks collision with the DEC tradition and undoes some of §1.3's terminological hygiene. Propose aligning with the §8.1/§8.2 phrasing "simplicial wedge–Hodge construction" or "higher-$N$ wedge–Hodge calculus on simplicial coordinates."

**`[S9-L-3]` — notation drift: $R$ vs $R(u,\theta)$, $K$ vs $K(u)$ in the displayed formula** — line 489.

The body uses $R(u,\theta)$ and $K(u)$ uniformly; §9's displayed equation uses $R$ and $K$ without arguments. Acceptable in a trigonometric identity, but for consistency with §5 eq (5.1) and §5.3, write $R(u,\theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2$.

**`[S9-L-4]` — implicit restriction-to-$H$ in the $V$-conjugacy sentence** — line 491.

"Under the hyperplane isometry $V: H \to \mathbb{R}^3$ ... the inner product, cross product, and rotation operators constructed here are carried to their classical $\mathbb{R}^3$ counterparts" compresses the fact that the $4\times 4$ matrices $K(u)$ and $R(u,\theta)$ are carried to their $3\times 3$ Cartesian counterparts *after restriction to $H$* (§2.5's "$V K(u) V^{-1} = [Vu]_\times$" and the Proposition 6.1 restricted trace). An explicit "(restricted to $H$)" would remove the ambiguity for an out-of-context reader. Not blocking.

**`[S9-L-5]` — "Hodge duals of wedge products" drops the arity-$N-3$ qualifier present in the Abstract** — line 491.

The Abstract (line 21) writes "Hodge duals of wedge products of arity $N - 3$," flagging that the higher-$N$ operators are $(N-3)$-ary rather than binary. §8.2 makes the same point. §9's summary drops the arity qualifier, which a casual reader might misread as a claim that binary cross products extend to all $N$. Propose restoring: "Hodge duals of wedge products *of arity $N - 3$*."

## Cross-section coherence check

- **Abstract vs §9.** Factual claims agree. Abstract's "analogous construction via Hodge duals of wedge products of arity $N-3$, which we leave to future work" and §9's "Higher-$N$ generalizations exist via Hodge duals of wedge products ... we leave to future work" are consistent modulo `[S9-L-5]`.
- **§1.2 vs §9.** Contributions item 3 (joint gauge-compatibility theorem) and item 6 (framework-internal uniqueness) are under-represented in §9's explicit "novelty" list — see `[S9-M-3]`. The hedge wording of §1.2 item 6 is not reflected in §9 — see `[S9-M-2]`.
- **§2.5 / §3.4 / §7 references.** All numeric cross-references in §9 (§§2.5, 3.4, 7) resolve correctly in the current body.
- **§8 coherence (just certified GREEN).** §9's "Higher-$N$ generalizations ... via Hodge duals of wedge products" is consistent with the updated §8.1/§8.2 (blade generators remain rank-2; the obstruction to single-axis closed-form exponentiation is Lie-theoretic), provided `[S9-L-5]` is addressed to avoid misreading.
- **`open-issues.md` relevance.** The `[L-2-1]` §1.2 item 3 shorthand note is *not* a §9 issue per se, but the `[S9-M-1]` regression is the same family of concern (scalar-vs-vector precision) and should be resolved at the same time as any future §1 harmonization pass.
