# Cycle 2 Synthesis — §1 Introduction
**Scope:** §1 Introduction (lines 35–76), plus manuscript-level scope harmonization (Abstract + §4)
**Cycle:** 2 of up to 3
**Reviewers:** Reviewer X (formalism), Reviewer Y (narrative)
**Status (joint):** AMBER  (Reviewer X: AMBER, Reviewer Y: GREEN)
**Date:** 2026-04-20

Per-reviewer files:
- [`feedback_cycle_2_reviewer_x.md`](./feedback_cycle_2_reviewer_x.md) — Cycle 1 findings: 1 RESOLVED, 2 PARTIALLY RESOLVED; 1 new High, 1 new Medium.
- [`feedback_cycle_2_reviewer_y.md`](./feedback_cycle_2_reviewer_y.md) — All 3 Cycle 1 findings RESOLVED; 0 new findings. GREEN.

## Loop-blocking findings (Critical + High) remaining after Cycle 2

Reviewer Y is clean. Only Reviewer X has High findings open.

1. **[F-H-4] (NEW)** Abstract and §4 still use the broader, less precise language that §1 was narrowed away from in Cycle 1. The Abstract advertises a "complete intrinsic calculus"; §4 Remark 4.2 claims the construction is defined "without reference to a coordinate frame." Either the Abstract and §4 must be harmonized with the tightened §1 scope (preferred), or §1 must be loosened back. The former is strictly better for the paper.

2. **[F-H-1 / F-H-2] PARTIAL** — the unresolved half of these two findings reduces to the same harmonization: make sure the Abstract and §4 use the qualified scope (simplicial / Gram-fixed) and the carved-out operator set (inner product, binary cross product, rotation — not differential operators).

## Non-blocking findings

- **[F-M-6]** §1.2 item 3 forward-references §4 as "Joint gauge-compatibility theorem," but §4's current heading and Theorem 4.1 use closure-style language. Align signposting: either update §4's heading and Theorem 4.1 framing to the quotient/descent language, or soften §1.2 item 3's forward reference to match §4's existing language.

## Proposed Author triage for Cycle 2

Widen scope strictly to:
- **Abstract** (lines 11–25): harmonize the scope language with §1 (carve out differential operators; qualify "intrinsic" to mean once simplicial Gram data is fixed).
- **§4** (lines 244–253 or thereabouts): harmonize heading, Theorem 4.1 framing (to match §1.2 item 3's forward reference), and Remark 4.2 scope claim.
- Leave everything else untouched.

This is a surgical harmonization pass, not a rewrite. If the Author judges that §4's current framing is in fact the right one and §1.2 item 3 should be softened instead, that is an acceptable alternative route to resolving [F-M-6]; both lead to a consistent manuscript.

## Author triage (cycle 2)

**Overall route for [F-M-6]:** Option A (preferred). §4's heading and Theorem 4.1 have been reframed in the quotient / descent / joint-gauge-compatibility language already used in §1.2 item 3, tying the harmonization of Abstract, §1, and §4 together in a single coherent mathematical story rather than softening §1.2's forward reference. This also makes Theorem 4.1 state something strictly sharper (per-operator invariance clauses + descent) than the prior closure-style statement.

- **[F-H-4] Accepted.** Abstract scope language and §4 heading / Theorem 4.1 / Remark 4.2 harmonized with the tightened §1.
  - Abstract: the paragraph introducing the three operators (formerly "each defined without reference to a Cartesian frame") now carves out differential operators and qualifies intrinsicness as "once the simplicial Gram data is fixed, their formulas require no ongoing reference to a Cartesian frame." The concluding paragraph ("Together these operators constitute a complete intrinsic calculus…") has been rephrased as "an intrinsic algebraic calculus — inner product, binary cross product, and rotation, with differential operators deferred to future work" with the same Gram-fixed qualifier.
  - §4: heading renamed to **"Gauge-Compatibility and Descent to the Zero-Sum Quotient."** Intro paragraph no longer claims a "complete realization of 3D Euclidean vector calculus"; instead it names the algebraic scope explicitly and flags that differential operators are out of scope. Theorem 4.1 is now **"Joint gauge-compatibility and descent,"** stated as three clauses (scalar invariance; hyperplane closure + gauge annihilation for $K(u)$; hyperplane closure + gauge fixing for $R(u,\theta)$) with an explicit descent statement to $\mathbb{R}^N / \langle \mathbf{1}\rangle \cong \mathbb{R}^{N-1}$. Proof sketch updated to match the three-clause structure. Remark 4.2 rewritten to remove "without reference to a coordinate frame" and "exist natively," replacing them with the §1.2-item-3-grounded qualifier and an explicit "algebraic" restriction.

- **[F-H-1] (partially unresolved half) Accepted.** The half that concerned the Abstract / §4 advertising a "complete intrinsic calculus" is closed by the [F-H-4] edits above; the scope now carves out differential operators manuscript-wide.

- **[F-H-2] (partially unresolved half) Accepted.** The half that concerned the Abstract / §4 Remark 4.2 claiming the construction is defined "without reference to a Cartesian frame" is closed by the [F-H-4] edits above; both now use the Gram-fixed qualifier consistent with §1.

- **[F-M-6] Accepted with modification (Option A).** Rather than softening §1.2 item 3's forward reference, §4's heading and Theorem 4.1 have been renamed and reframed to match §1.2 item 3's "Joint gauge-compatibility theorem" language. §4's heading is now "Gauge-Compatibility and Descent to the Zero-Sum Quotient" and Theorem 4.1 is now "Joint gauge-compatibility and descent," stated in the scalar / vector / rotation per-clause form with explicit descent to the quotient. The modification relative to the proposed title ("Gauge-Compatibility and Closure on the Zero-Sum Quotient") is to use "Descent" rather than "Closure," which more precisely advertises what the theorem delivers (descent to $\mathbb{R}^{N-1}$).

**Coherence check (Abstract → §1 → §4).** I have re-read Abstract (lines 11–25), §1 (lines 37–73), and §4 (lines 244–258) in sequence. Confirmed:
- No phrase in the Abstract or §4 now advertises a "complete" vector calculus; both explicitly restrict to the algebraic layer and explicitly defer differential operators.
- No phrase in the Abstract or §4 now claims the construction is defined "without reference to a Cartesian frame" in the unqualified form; both use the Gram-fixed qualifier from §1.
- §4's heading ("Gauge-Compatibility and Descent to the Zero-Sum Quotient") and Theorem 4.1 name ("Joint gauge-compatibility and descent") now align with the §1.2 item 3 forward reference.
- No scope-related phrase in the Abstract or §4 is now broader than its §1 counterpart.

**Disposition counts.** Accepted: 3 ([F-H-4], [F-H-1] partial, [F-H-2] partial). Accepted with modification: 1 ([F-M-6]). Rejected: 0.

**Out-of-scope changes.** None. Sections 2, 3, 5–10, all appendices, and the "Note on the Use of AI Tools" section were not edited. §1.2 item 3 was left unchanged because Option A made its existing forward reference consistent with §4 without modification.
