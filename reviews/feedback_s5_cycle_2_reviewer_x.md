# Reviewer X — Formalism & Logic Audit — Cycle 2
**Scope:** §5 Closed-Form Rotation via the Exponential Map
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Verification of Cycle 1 resolutions
- **[F-H-1]** **RESOLVED.** The revised §5.1 now supplies the missing plane-geometry justifications. The orthogonality chain is correct: simplicial skew-adjointness gives
  $$\langle KP, K^2P\rangle_s = -\langle P, K^3 P\rangle_s = \langle P, KP\rangle_s = -\langle KP, P\rangle_s,$$
  hence the quantity equals its own negative and is therefore zero. The equal-norm argument is also correct: once $P = P_\parallel + P_\perp$ with $P_\parallel \in \mathrm{span}(u)$, $P_\perp \in u^\perp \cap H$, one has $KP = KP_\perp$, and Corollary 3.4 gives $K^2 = -I$ on $u^\perp \cap H$; thus
  $$\|KP\|_s^2 = -\langle P, K^2 P\rangle_s = \langle P, P_\perp\rangle_s = \|P_\perp\|_s^2.$$
  The axial degenerate case is now handled explicitly. Since $u^\perp \cap H$ is 2-dimensional, $P_\perp \neq 0$ off-axis, and $\|KP\|_s = \|P_\perp\|_s \neq 0$, the claim that $\{P_\perp, KP\}$ is a simplicially orthogonal basis is now supported.

- **[F-H-2]** **RESOLVED.** The Lie-algebra framing is now cleanly restricted to $H$: the manuscript states $\mathfrak{so}(H, \langle\cdot,\cdot\rangle_s) \cong \mathfrak{so}(3)$, distinguishes the $4 \times 4$ lift to $\mathbb{R}^4$, and includes the needed bridge sentence that $G|_H = \tfrac{4}{3} I_H$, so simplicial and ambient-Euclidean skew-adjointness coincide after restriction.

- **[F-H-3]** **RESOLVED.** The §5.3 parenthetical now assigns the structural roles correctly: $I$ is the identity, $K$ is the in-plane quarter-turn, $-K^2$ is the perpendicular projector, and $I + K^2$ is the parallel projector.

- **[N-H-1]** **RESOLVED.** The classical Rodrigues / Lie-exponential discussion now cites existing bibliography entries `[Arnold]` and `[Hall]`, and both entries are present in the References section.

- **[E-Conv-1]** **RESOLVED IN SUBSTANCE.** The orientation/chirality issue is no longer tacit: §2.5 now warns the reader forward to Remark 5.1, and Remark 5.1 states the left-handedness of the simplicial rotation relative to the fixed right-handed Cartesian embedding. The sign conclusion is consistent with the added remark. A residual notation issue in the displayed intertwining formula is logged below as a new Medium item, but the convention-level gap itself has been addressed.

- **[F-M-1]–[F-M-5]** **RESOLVED on spot-check.** The boxed-operator scope ambiguity is repaired by the sentence after Eq. (5.1); the positive-angle convention is now tied back to §2.5 / §3.4; "unit skew operators" has been replaced by a precise cubic/quarter-turn characterization; and the §9 forward reference is now correctly softened to match §9.2's actual "future work" status. I see no regression in these Cycle 1 Medium items.

## New findings (Cycle 2)

### Critical
- None.

### High
- None.

### Medium
- **[F-M-6] Notation in Remark 5.1 conflates transpose with inverse/adjoint.** The chirality conclusion of Remark 5.1 is correct, but the displayed formula is not fully clean as written. If $V\colon (H, \langle\cdot,\cdot\rangle_s) \to \mathbb{R}^3$ is the stated simplicial-to-Cartesian isometry, then the natural intertwining statement is
  $$V K(u) V^{-1} = -[Vu]_\times$$
  (equivalently with the simplicial adjoint $V^*$). Writing $V^\top$ suggests ordinary Euclidean transpose, but for the tetrahedral map one has $V^\top V = G$ on $H$, so raw transpose is not literally the inverse unless an adjoint convention is declared. The restriction marker `|_H` is also not the natural repair: if $V$ is already defined with domain $H$, no extra restriction is needed on the left-hand side. This is a notation-level rigor issue, not a defect in the sign conclusion.

### Low
- None.

## Summary
All Cycle 1 High findings in §5 are now resolved. The revised section is materially stronger: the geometric derivation now justifies its plane basis, the Lie-algebra framing is properly scoped to $H$, the projection roles are correctly stated, the §9 forward reference now matches the actual higher-dimensional discussion, and the Arnold/Hall citations are in place. I find no new Critical or High formalism defects in §5, §3, §4, §9, or §10; the only residual issue is a notation-level transpose/adjoint slippage in Remark 5.1.

STATUS: GREEN
