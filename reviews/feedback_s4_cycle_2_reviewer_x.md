# Reviewer X — Formalism & Logic Audit — Cycle 2
**Scope:** §4 Gauge-Compatibility and Descent to the Zero-Sum Quotient
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Resolution of Cycle 1 findings

- **[F-H-1]** RESOLVED — Clause (1) now states full two-slot invariance $\langle a + k\mathbf{1},\, b + m\mathbf{1}\rangle = \langle a, b\rangle$ at line 279, and the proof sketch expands the correct four-term bilinear expression at lines 285–286, with the three non-$a^\top G b$ terms killed via $G\mathbf{1} = 0$ and $\mathbf{1}^\top G = (G\mathbf{1})^\top = 0$. The §2.4 propagation sweep is also in place at line 153, where the same two-slot formula is now stated explicitly.
- **[F-H-2]** RESOLVED — Clause (2) now states axis-class independence of the cross-product generator, $K(u + k\mathbf{1}) = K(u)$, at line 280; clause (3) states $R(u + k\mathbf{1}, \theta) = R(u, \theta)$ at line 281. The proof sketch at line 287 gives the derivation $K(u + k\mathbf{1}) = K(u) + kK(\mathbf{1}) = K(u)$, and Remark 3.2 supplies the linearity and $K(\mathbf{1}) = 0$.
- **[F-M-1]** RESOLVED — The proof sketch now explicitly closes the power-series argument: each partial sum lies in $H$, and $H$ is stated to be a closed finite-dimensional subspace, so the limit remains in $H$ (line 287).
- **[F-M-2]** RESOLVED — The proof sketch now foregrounds the intrinsic simplicial isometry $R^\top G R = G$ as the descent-relevant statement, and cites commutation $GK(u) = K(u)G$ via Remark 3.2(1). The ambient Euclidean facts $R^\top R = I$ and $\det R = +1$ are explicitly demoted to §§5–6 (line 287).
- **[F-M-3]** RESOLVED — Clause (2) now says $K$ is linear in its axis argument, not bilinear (line 280); no remaining manuscript occurrence of "bilinear in its axis argument" found.
- **[F-L-1]** RESOLVED — The descent sentence now recalls the canonical realization by the zero-sum hyperplane $H$ of §2.3 at line 283.
- **[F-L-2]** RESOLVED — The descent sentence now distinguishes "the simplicial bilinear form, cross-product operator, and rotation" at line 283, eliminating the earlier terminological slippage.

## Propagation check verification

- `(presently)` — zero manuscript matches.
- `bilinear in its axis argument` — zero manuscript matches.
- No remaining explicit one-slot symbolic inner-product invariance claim in the manuscript; both relevant symbolic statements (§2.4 line 153 and §4 line 279) are now two-slot.
- **Out-of-scope residue:** §1.2 item 3 line 53 still summarizes scalar gauge invariance in one-variable shorthand as "values unchanged under $x \mapsto x + t\mathbf{1}$." This is not false, but it is weaker than the two-slot form now proved. Flagged below as Low-severity [L-2-1].

## New findings (Cycle 2)

### Critical / High / Medium
None.

### Low
- **[L-2-1] Introductory shorthand understates the final two-slot statement** — In §1.2 item 3 line 53, the phrase "values unchanged under $x \mapsto x + t\mathbf{1}$" compresses scalar gauge invariance into a one-variable shorthand. Since the manuscript now proves and relies on two-slot well-definedness of the descended bilinear form (lines 153, 279, 283, 285–286), this roadmap sentence is slightly under-specified. Low severity only: the formal theorem/proof layer is correct.

## Summary
All Cycle 1 High findings are now formally resolved in the revised §4, and the §2.4 sweep is correctly carried out. The proof sketch's key additions are logically adequate: the four-term expansion for clause (1) is correct, the axis-class independence of $K$ is explicitly derived from Remark 3.2, and the simplicial orthogonality statement is properly foregrounded. No new Critical or High issues in scope.

STATUS: GREEN
