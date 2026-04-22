# Synthesis — §4 Cycle 2 (TERMINAL — GREEN)
**Scope:** §4 Gauge-Compatibility and Descent to the Zero-Sum Quotient (lines 273–289)
**Date:** 2026-04-20
**Status:** GREEN

## Inputs
- `feedback_s4_cycle_2_reviewer_x.md` — all Cycle 1 findings RESOLVED; 0 new Critical/High/Medium; 1 Low (out-of-scope §1.2 shorthand) → STATUS: GREEN
- `feedback_s4_cycle_2_reviewer_y.md` — all Cycle 1 findings RESOLVED; 0 new Critical/High; 1 Medium (proof-sketch formatting, non-blocking); 1 Low (§10 Conclusion scope) → STATUS: GREEN

## What got done in Cycle 1 revision

**Descent-logic tightening (blocking):**
- Clause (1): two-slot inner-product invariance $\langle a + k\mathbf 1, b + m\mathbf 1\rangle = \langle a, b\rangle$ with explicit four-term expansion in the proof sketch.
- Clause (2): axis-class independence $K(u + k\mathbf 1) = K(u)$ with explicit Remark 3.2 pointer for the formal linear extension (resolves both [F-H-2] and [N-H-1]).
- Clause (3): axis-class independence of $R$ via $R(u + k\mathbf 1, \theta) = R(u, \theta)$.
- Proof sketch: closed-subspace limit argument for $R(H) \subseteq H$.
- Proof sketch: simplicial orthogonality $R^\top G R = G$ foregrounded (using $GK = KG$ from Remark 3.2(1)), with ambient $R^\top R = I$ demoted to §§5–6 forward reference.
- "(presently)" hedge replaced with "(constructed in §5)".

**Narrative polish (strongly recommended, all accepted):**
- Remark 4.2 trimmed of redundant scope disclaimer; em-dash clause split into two sentences.
- "Rigid-body mechanics" framing anchored with Arnold and Marsden-Ratiu citations (new References entries at lines 567 and 585).
- Theorem-clause formatting standardized to numbered list with italic titles.
- "Bilinear in its axis argument" corrected to "linear in its axis argument" (the object $u \mapsto K(u)$ is linear; the joint $(u, P) \mapsto K(u) P$ is bilinear).
- Descent line recalls zero-sum hyperplane $H$ from §2.3 as the canonical quotient representative.
- Descent line distinguishes "simplicial bilinear form, cross-product operator, and rotation".
- Descent paragraph adds §2.2.1 callback (information geometry / CRNT).

**Cross-scope propagation sweep (Author, Cycle 1):**
- §2.4 line 153 upgraded from one-slot to two-slot inner-product invariance statement (mechanical propagation of [F-H-1]).

**Cross-scope propagation sweep (Orchestrator, post-Cycle 2):**
- §10 Conclusion line 547 edited from "complete intrinsic vector calculus" to "complete intrinsic *algebraic* vector calculus" (mechanical propagation of §4's narrowed scope; resolves Reviewer Y's [N-L-3]).
- §10 Conclusion line 549 rephrased from "3D Euclidean vector calculus can be formulated intrinsically" to "the algebraic layer of 3D Euclidean vector calculus (inner product, binary cross product, rotation) can be formulated intrinsically" (same sweep).

## Non-blocking residues

- **[N-M-4] Proof sketch readability** (Medium, Reviewer Y) — the proof sketch is a dense paragraph; breaking it into (1)/(2)/(3) sub-paragraphs matching the theorem's list would improve readability. Not swept here because it is non-mechanical (a reformatting choice); deferred to a future §4 Author pass or pre-submission polish.
- **[L-2-1] §1.2 item 3 one-slot shorthand** (Low, Reviewer X) — line 53's parenthetical "values unchanged under $x \mapsto x + t\mathbf 1$" uses one-slot shorthand. The formal claims elsewhere are correct and precise; logged to `reviews/open-issues.md` as a note for the next §1 pass rather than swept here (a substantive rephrasing, not a one-word fix).

## Propagation check (both cycles)

Full-manuscript sweeps yielded:
- `(presently)` as hedge — zero matches.
- `bilinear in its axis argument` — zero matches.
- Single-slot inner-product invariance symbolic claim — zero matches at the theorem-level (only in §1.2 roadmap shorthand, logged).
- `complete intrinsic vector calculus` (without "algebraic") — zero matches after the §10 sweep.
- `formally the same as classical vector calculus` — zero matches.

## Terminal status

§4 reached GREEN at Cycle 2 (inside the 3-cycle cap). One open-issues entry logged; no blocking residues.

STATUS: GREEN
