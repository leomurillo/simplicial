# §5 — Cycle 1 Synthesis Triage
**Scope:** §5 Closed-Form Rotation via the Exponential Map
**Cycle:** 1 of max 3
**Date:** 2026-04-20
**Orchestrator:** Author sub-role

## Overall Cycle 1 status

| Reviewer | Critical | High | Medium | Low | Status |
|---|---|---|---|---|---|
| Reviewer X (formalism) | 0 | 3 | 5 | 1 | AMBER |
| Reviewer Y (narrative) | 0 | 2 | 6 | 5 | AMBER |
| Empirical Skeptical (Rodrigues) | — | — | — | — | AMBER (Cartesian chirality, not a proof defect) |
| Empirical Reviewer QA | 0 | 0 | 5 | 4 | **GREEN** — Skeptical's conclusions safe to feed to Author |

**Terminal status for §5, Cycle 1: AMBER.** Three formalism High items and two narrative High items plus a non-trivial convention-level empirical finding mandate a revision pass.

## Critical findings
None.

## High findings (blocking, must be resolved in Cycle 1 revision)

### [F-H-1 / N-H-2] Unsupported plane-basis claims + degenerate case (§5.1)
- Reviewer X and Reviewer Y both flag line 303–307. `{P_\perp, KP}` is asserted to be a simplicially orthogonal basis of the rotation plane with equal simplicial norms, without proof or backward reference. The proofs are short (using simplicial skew-adjointness `GK = -K^\top G` and `K^3 = -K` for orthogonality; `K^2|_{u^\perp \cap H} = -I` from Cor 3.4 for equal norms) but must be stated.
- Separately, the degenerate case `P \in \mathrm{span}(u)` (where `P_\perp = KP = 0`) is unhandled; the formula still gives `P' = P` correctly, but the derivation should note the case or argue by continuity.
- **Action:** insert (i) a short paragraph after line 303 proving `\langle KP, P_\perp\rangle_s = 0` and `\|KP\|_s = \|P_\perp\|_s`, and (ii) an explicit handling of the axial case.

### [F-H-2] Lie-algebra framing imprecise (§5.2 lines 325–331)
- "Skew-symmetric operators on H that annihilate 1" is formally ill-posed because `1 \notin H`. "Skew-symmetric" is also ambiguous (simplicial vs ambient).
- The identification with $\mathfrak{so}(3)$ is correct in substance, but needs the explicit bridge: `G|_H = \tfrac{4}{3} I_H`, so simplicial and ambient skew-adjointness agree after restriction.
- **Action:** rewrite lines 325–327 per Reviewer X's proposed fix (restrict to $H$, identify $\mathfrak{so}(H, \langle\cdot,\cdot\rangle_s) \cong \mathfrak{so}(3)$, mention the 4×4 lift satisfies $K(u)\mathbf{1} = 0$).

### [F-H-3 / N-M-5] Structural-role parenthetical misattributes projections (§5.3 line 347)
- Pre-flagged by the orchestrator and independently confirmed by Reviewer X (High) and Reviewer Y (Medium). In the Rodrigues decomposition, the parallel projector is `I + K^2`, not `I`; the perpendicular projector is `-K^2`, not `K^2`. `I` is simply the identity; `K` is the in-plane quarter-turn.
- **Action:** replace the parenthetical per Reviewer X's fix: "as identity, in-plane quarter-turn, and negative perpendicular projection respectively; hence $I + K^2$ is the parallel projector and $-K^2$ the perpendicular projector."

### [N-H-1] Missing citations for classical results
- Classical Rodrigues formula and exponentiation of $\mathfrak{so}(3)$ via $K^3 = -K$ are standard; need citations to avoid implicitly claiming novelty for the formulas themselves.
- **Action:** cite appropriate classical references at or near lines 319, 331, and 343. Existing references Arnold, Marsden-Ratiu are candidates; Hall (*Lie Groups, Lie Algebras, and Representations*) is also appropriate and may need to be added to the References list.

### [E-Conv-1] Orientation convention annotation (§5, §3.1, §2.5 — joint slack)
- The Empirical Reviewer analytically confirmed: $V K(u) V^\top|_H = -[Vu]_\times$ exactly, where $V$ is the §2.5 isometry to $\mathbb R^3$. Hence $V R(u,\theta) V^\top|_H = R_{\text{cart}}(Vu, -\theta)$: the simplicial rotation is left-handed relative to §2.5's right-handed Cartesian embedding.
- This is **not** a proof defect — all internal simplicial properties of $R$ hold to machine precision — but a tacit-convention gap: §2.5 declares ambient right-handedness but does not pin down whether the labelling $(l,n,m,p) \mapsto (\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4)$ is positively or negatively oriented as a 4-tuple.
- Three equivalent fixes are possible: (a) permute a §2.5 vertex pair, (b) flip the overall sign of $\tilde K$ in §3.1, (c) add an explicit "Orientation convention" remark.
- **Action (least invasive, recommended):** option (c). §3 is already GREEN; modifying Def 3.1 at this stage would retrocede §3 and force downstream re-verification of Theorem 3.3, Corollary 3.4, §4 Theorem 4.1, Appendix A, and Appendix B. Instead, add a brief *Orientation convention* Remark at the end of §5 (or tacked onto §5.3) stating the identity $V R(u,\theta) V^\top|_H = R_{\text{cart}}(Vu, -\theta)$ and the resulting left-handedness relative to the §2.5 embedding. Cross-scope propagation: log to `open-issues.md` a §8 pre-check requirement, since §8's quaternion / circulant comparison must be sign-aware.

## Medium findings (address where cheap; defer non-mechanical items)

- **[F-M-1]** Clarify scope of boxed $R(u,\theta)$ at line 319: operator on $H$ vs 4×4 lift on $\mathbb R^4$. Add one sentence.
- **[F-M-2]** Tie positive-angle convention at line 307 back to §2.5 orientation. Add half-sentence.
- **[F-M-3]** Replace "unit skew operators" at line 327 with a precise phrasing ("$K(u)$ with $K^3 = -K$" or "whose restriction to $u^\perp \cap H$ acts as quarter-turn").
- **[F-M-4]** Justify `\mathrm{SO}(3)` at line 331 via `\det \exp X = e^{\mathrm{tr} X} = 1`. One clause.
- **[F-M-5]** Soften the §9 forward reference at line 347: the analog of $K^3 = -K$ and closed-form exponentiation are *not* established in §9, only the wedge-Hodge construction.
- **[N-M-1]** Add a one-paragraph roadmap at the top of §5 (after the heading, before §5.1).
- **[N-M-2]** Consolidate the choppy paragraphs in §5.1 (lines 297–315).
- **[N-M-3]** Overlaps with [F-M-3]; addressed there.
- **[N-M-4]** §5.3 section title is over-promising. Rename to "Comparison of the two derivations" or fold into §5.2.
- **[N-M-5]** Overlaps with [F-H-3]; addressed there.
- **[N-M-6]** Add reminder that $K$ is shorthand for $K(u)$.

## Low findings (polish; defer to final pass unless mechanical)

- **[F-L-1]** One-line formal statement of equivalence in §5.3 (nice-to-have).
- **[N-L-1]** Drop the box around the Rodrigues formula (line 319). Boxing is not used elsewhere. *Mechanical, address now.*
- **[N-L-2]** Rephrase "Grouping odd and even powers ≥ 1" (line 337). *Mechanical, address now.*
- **[N-L-3]** Explicit "see §9" forward reference (subsumed by [F-M-5] fix).
- **[N-L-4]** Note that $u \in H$ is WLOG by §4 gauge invariance (line 297). *Mechanical, address now.*
- **[N-L-5]** "intrinsic to the algebraic layer of the simplicial system" at line 343. *Mechanical, address now.*

## Empirical Reviewer — script polish items (defer to a cleanup pass)

- **[E-M-1, E-L-4]** Test 1 wording overstates one-point verification. Fix the report and, ideally, extend to multi-axis symbolic identity.
- **[E-M-2]** Add `assert` statements with tolerance thresholds (consistent with post-Appendix B policy).
- **[E-M-3]** Seed all tests and loop over multiple seeds.
- **[E-M-4]** Add vertex-permutation control (swap $\mathbf v_3 \leftrightarrow \mathbf v_4$) to localize orientation joint mismatch.
- **[E-M-5, E-L-1 through E-L-3]** Style polish.

*These do not change the headline empirical conclusion. They should be addressed in an Empirical cleanup task logged to `open-issues.md`, not in the Author's §5 Cycle 1 revision.*

## Cross-scope propagation check plan

1. **[E-Conv-1] orientation remark:** the remark itself is in §5; the consequential follow-up is that §8 must be audited for sign consistency against Def 3.1 when §8 comes under review. **Log to `open-issues.md` as a §8 pre-check item.**
2. **No other retiring or narrowing of phrasings** is triggered by the Cycle 1 resolutions above. The Rodrigues formula, $K$ cubic identity, and $R$ isometry statements are unchanged — only clarified or justified.

## Cycle 1 revision directive (for Author)

Address all Critical and High findings above, plus the mechanical Low items, in a single coherent §5 revision. Defer Medium narrative items if they would bloat the section or drift into §6 territory; address the formalism Mediums ([F-M-1] through [F-M-5]) which are short and directly repair rigour. Structure:

1. Add a short **opening paragraph** to §5 (roadmap), implementing [N-M-1].
2. In **§5.1**:
   - Address [F-H-1]/[N-H-2]: prove the plane-basis claims, handle the degenerate axial case.
   - Address [F-M-1], [F-M-2], [N-M-2], [N-L-1], [N-L-4], [N-M-6] as cheap local edits.
3. In **§5.2**:
   - Address [F-H-2]: rewrite the Lie-algebra framing.
   - Address [F-M-3], [F-M-4], [N-L-2], [N-L-5] as cheap local edits.
4. In **§5.3**:
   - Address [F-H-3]: fix the structural-roles parenthetical.
   - Address [F-M-5]: soften the §9 forward reference.
   - Consider renaming (or folding into §5.2) per [N-M-4]. Author's discretion.
5. **New Remark at the end of §5** (after §5.3): implement [E-Conv-1] option (c) — the *Orientation convention* annotation.
6. **References**: add citations per [N-H-1].

## Status line

```
STATUS: AMBER — Cycle 1 revision required. Next milestone: Cycle 2 audits after Author revision.
```
