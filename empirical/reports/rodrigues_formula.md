# Empirical Validation Report: Rodrigues Formula

**Label:** Rodrigues Formula (§5)
**Status:** `STATUS: GREEN`
**Last updated:** 2026-04-21 (after §2.5 vertex swap re-run)

This report validates the geometric and Lie-algebraic derivations of the intrinsic simplicial Rodrigues rotation formula $R(u, \theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2$ presented in §5 of `simplicial_vector_calculus.md`.

## Summary of Findings

1. **Test 1 (Symbolic Series):** The $\theta$-expansion of the matrix exponential $\exp(\theta K)$ truncated at order $\theta^8$ matches the expansion of $I + \sin\theta K + (1 - \cos\theta)K^2$ for the $l$-axis basis-axis specialization, verifying the Lie-algebraic regrouping logic on that fibre.
2. **Test 2 (Geometric Derivation):** The decomposition $P = P_\parallel + P_\perp$ via the squared cross-product operator $K^2$ holds to machine precision. The geometric properties of the projection ($\langle P_\perp, u \rangle_s = 0$, $\langle P_\perp, KP \rangle_s = 0$, and $\|P_\perp\|_s = \|KP\|_s$) are fully validated.
3. **Test 3 (Rotation Correctness):** The closed-form operator $R(u, \theta)$ exactly produces the matrix exponential of $\theta K$. It is a rigorous simplicial isometry ($R^\top G R = G$), preserves the ambient Euclidean inner product ($R^\top R = I$), and acts as a proper rotation mapping the zero-sum hyperplane $H$ to itself while fixing the axis $u$ and the gauge direction $\mathbf{1}$. Composition $R(\alpha) R(\beta) = R(\alpha + \beta)$ holds to machine precision.
4. **Test 4 (Cartesian Comparison):** Under the §2.5 basis convention $\mathbf v_1, \mathbf v_2, \mathbf v_3, \mathbf v_4$ (with the $\mathbf v_3 \leftrightarrow \mathbf v_4$ labelling introduced on 2026-04-21), the simplicial rotation exactly matches the standard right-handed Cartesian rotation: $V K(u) V^{-1} = +[Vu]_\times$ and $V R(u,\theta) V^{-1} = R_{\text{cart}}(Vu, \theta)$, to machine precision.

**STATUS: GREEN.** The simplicial Rodrigues formula (§5) is numerically and symbolically validated. Under the §2.5 vertex labelling chosen in the manuscript, the simplicial system is right-handed relative to the standard right-handed Cartesian embedding; no orientation remark is required in the paper.

---

## Detailed Execution Log

### Test 1: Symbolic Series Equivalence
Constructed symbolic matrices $\tilde{K}(u)$ and truncated the formal power series $\exp(\theta K)$ up to $O(\theta^8)$.
The polynomial difference $P_{\text{exp}}(\theta) - P_{\text{RHS}}(\theta)$ was evaluated symbolically. Due to the high computational cost of full symbolic expansion of the norm constraint $\tfrac{4}{3}\sum u_i^2 = 1$, the exact cancellation was verified on the exact symbolic $l$-axis.
- **Result:** Difference vanishes identically. Regrouping identity verified on this fibre.

### Test 2: Geometric Derivation (Numerical)
Validated on randomly generated zero-sum vectors $P$ and zero-sum unit axes $u$.
- **$P = P_\parallel + P_\perp$ residual:** 1.11e-16
- **$P_\parallel \in \operatorname{span}(u)$ residual:** 1.94e-16
- **$P_\perp \in H$ residual:** 1.11e-16
- **$P_\perp \perp u$ residual:** 1.11e-16
- **$\langle P_\perp, KP\rangle_s = 0$ residual:** 1.39e-16
- **$\|P_\perp\|_s = \|KP\|_s$ residual:** 4.44e-16

### Test 3: Rotation Correctness (Numerical)
- **$R - \operatorname{expm}(\theta K)$ residual:** 1.11e-16
- **Simplicial isometry $R^\top G R = G$ residual:** 1.11e-16
- **Ambient orthogonality $R^\top R = I$ residual:** 2.22e-16
- **Determinant $\det R$:** 1.0000
- **Axis-fixing $Ru = u$ residual:** 2.78e-17
- **Gauge-fixing $R\mathbf{1} = \mathbf{1}$ residual:** 0.00e+00
- **Hyperplane closure $\sum(RP)_i = 0$ residual:** 1.67e-16
- **Composition $R(\alpha)R(\beta) = R(\alpha+\beta)$ residual:** 1.11e-16

### Test 4: Cartesian Comparison (post-swap)
Created the $3 \times 4$ isometry matrix $V$ using the §2.5 tetrahedral vertices, with $\mathbf v_3 = \tfrac{1}{\sqrt 3}(+1, -1, -1)$ and $\mathbf v_4 = \tfrac{1}{\sqrt 3}(-1, +1, -1)$ (i.e.\ the odd permutation of the 2026-04-20 labelling).
Compared $V (R_{\text{simp}} P)$ with $R_{\text{cart}} (V P)$.
- **Cartesian rotation match residual (positive $\theta$):** 4.44e-16 ✓
- **Cartesian rotation match residual (negative $\theta$, should be large):** 2.31e+00 ✓

**Conclusion on Test 4:** After the §2.5 vertex swap, the simplicial cross product $K(u)$ (Definition 3.1) and the isometry $V$ jointly induce a right-handed orientation: $V K(u) V^{-1} = +[Vu]_\times$. The former chirality mismatch (residual 2.31 at positive $\theta$) was a purely conventional artefact of the previous vertex labelling and is now eliminated without any change to the intrinsic simplicial mathematics.

## Resolution of [E-Conv-1]

The Empirical Skeptical + Empirical Reviewer finding that motivated Remark 5.1 (§5 Cycle 1) has been closed by relabelling, not by adding a sign caveat to the paper. Remark 5.1 has consequently been deleted from the manuscript.
