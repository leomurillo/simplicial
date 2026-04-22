# Empirical Reviewer — QA of `verify_rodrigues_formula.py` — Cycle 1
**Scope:** verification of Rodrigues formula and §5 derivations
**Reviewer:** Empirical Reviewer (numerical QA)
**Date:** 2026-04-20

## Critical / High / Medium / Low

### Critical
- None.

### High
- None. (In particular, Test 4's chirality diagnosis is **not** an artifact — see the analytic confirmation below.)

### Medium
- **[E-M-1] `test_1_symbolic` is a single point-check in disguise, reported as if global.** The script expands `exp(θK)` and the RHS to order $\theta^8$ *symbolically*, but then substitutes a specific basis axis `ul=3/4, un=-1/4, um=-1/4` (so `up=-1/4`) before reporting `max(abs(x) for x in num_diff)`. At this substitution the unit-norm condition $\tfrac{4}{3}\sum u_i^2 = 1$ is already baked in, so the polynomial in $\theta$ indeed vanishes — but the test is effectively a one-axis numerical check of Test 3 expressed symbolically. It does not actually verify the regrouping identity as a polynomial identity on the unit-axis variety, contrary to the wording in the report ("Regrouping identity verified," "vanishes identically"). Either (a) state that this is a one-point verification, or (b) substitute the norm condition via Gröbner reduction / `.subs(up, -ul-un-um).expand()` across multiple sampled axes. The numerical Test 3 (`R - expm(θK)` ≤ 1.1e-16) is the rigorous check; Test 1 should be described accordingly.
- **[E-M-2] No `assert` statements; tolerances are only printed.** Everything is `print(f"... residual: ...")`. Consistent with the prior Appendix B QA finding, the report can be read as passing even if future regressions raise residuals into the 1e-6 or 1e-3 range. Add `assert residual < 1e-10` (or similar) alongside each print. Appendix B was patched on this point; `verify_rodrigues_formula.py` regressed.
- **[E-M-3] Missing / inconsistent seeding and single-draw tests.** Only `test_2_geometric` sets `np.random.seed(42)`; `test_3_rotation` and `test_4_cartesian` are unseeded and run exactly one `(u, P)` draw each. For a manuscript-level chirality claim the test should loop over, e.g., 50 seeds (and additional $\theta$ values), not rely on a single unseeded draw. The sign asymmetry of Test 4 is stable under resampling (I verified analytically), but the script as written does not demonstrate that robustness.
- **[E-M-4] Test 4 lacks an orientation-permutation control.** To distinguish "Definition 3.1's cyclic pattern is left-handed relative to §2.5" from "the choice of Urner-Ace vertex assignment $(l,n,m,p) \mapsto (\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4)$ is left-handed and Definition 3.1 is right-handed in that frame," the script should re-run with a transposition of two vertex columns of $V$ (e.g. swap $\mathbf v_3 \leftrightarrow \mathbf v_4$) and confirm the sign flips. Both hypotheses yield the same $\theta \mapsto -\theta$ observation with the current test, so the Skeptical's attribution in the report ("the simplicial cross product $K(u)$ in Definition 3.1 embodies an orientation convention...") is underdetermined by the data. Chirality sits jointly on Def 3.1 *and* §2.5; the script cannot localize it to §3 alone.
- **[E-M-5] Fragile `max(abs(x) for x in num_diff)` on sympy output.** If simplification leaves ghost cancellations, python's `max` over sympy expressions can raise `TypeError` on truth-value resolution. It happens to work here because `sp.simplify` cleared the entries, but best practice is `sp.simplify((exp_series - rhs_series).subs(...))` followed by `all(e == 0 for e in ...)` or comparing against `sp.zeros(4,4)`.

### Low
- **[E-L-1] `get_G()` is recomputed on every call from `inner_s` / `norm_s`.** Cache as a module-level constant.
- **[E-L-2] Mixed float/rational:** `ul: 3/4` is a Python float, which becomes `sympy.Float(0.75)`. Use `sp.Rational(3,4)` etc. so the symbolic difference reduces cleanly to exact zero rather than to `~1e-16` floats.
- **[E-L-3] Style:** `sin_series * K + (1 - cos_series) * (K @ K)` mixes `*` and `@`. Either is fine for sympy Matrix, but be consistent.
- **[E-L-4]** Wording in the report ("Difference vanishes identically") overstates what Test 1 shows (see Medium finding above).

## Checklist-by-checklist verdict

### Tests 1–3 (internal simplicial consistency)
1. **Matrix construction.** Entries of `K_tilde` match Definition 3.1 line-for-line and the `/ np.sqrt(3)` scaling is applied. ✓
2. **Simplicial inner product.** `get_G() = (4/3) I − (1/3) J` for $N=4$, matching §2.4 post-spot-patch. ✓
3. **Zero-sum unit axis normalization.** `generate_zero_sum_unit_axis` projects to $H$ and divides by `norm_s(u)`, so `inner_s(u,u) = 1`, i.e. $\tfrac{4}{3}\sum u_i^2 = 1$. Correct normalization; the script does **not** mistakenly use $\|u\|_{\mathbb R^4} = 1$. ✓
4. **Tolerance assertions.** Residuals are only *printed*; no `assert` statements. ✗
5. **Random test vectors.** Vectors are random-normal projected to $H$, but only one draw per test, and only `test_2_geometric` sets a seed. No multiple-seed loop. ✗ (partially)

### Test 4 (Cartesian comparison)
1. **Isometry construction.**
   - Vertex convention matches `simplicial_vector_calculus.md:165-168` exactly. ✓
   - Metric preservation: I verified analytically that $V^\top V = \tfrac{4}{3} I - \tfrac{1}{3} J = G$. Hence for $c \in H$, $\|Vc\|_{\mathbb R^3}^2 = c^\top G c = \langle c, c\rangle_s$ — $V|_H$ is a genuine isometry with **no residual scaling factor**. The reported `4.44e-16` (negative-$\theta$) residual is not masked by a metric mismatch. ✓
   - Orientation: $V|_H$ carries some orientation into $\mathbb R^3$, but the script does not enforce or test that orientation. That's the genuine content of the Test 4 discrepancy.
2. **Axis mapping.** `u_cart = V @ u`, and from the above $\|u_{\text{cart}}\|_{\mathbb R^3} = 1$ whenever `inner_s(u,u) = 1`. Passing `theta * u_cart` to `Rotation.from_rotvec` is the correct scipy usage. ✓
3. **Comparison protocol.** `V(R_simp P)` vs `R_cart(V P)` is the correct formulation. ✓
4. **Alternative explanations.**
   - (a) Vertex-permutation control missing — see Medium finding [E-M-4]. Under `v3 ↔ v4` (odd permutation), $V|_H$ flips orientation and the sign would be restored *even if Def 3.1 is "right-handed in its own convention"*. So Test 4's data alone does not establish that Def 3.1 is left-handed independent of §2.5; it establishes a *joint* convention mismatch between Def 3.1 and the Urner-Ace labeling in §2.5.
   - (b) Confirmed: `scipy.spatial.transform.Rotation.from_rotvec` is unambiguously right-handed about the supplied axis.
   - (c) The §2.5 convention fixes the Cartesian vertices; the §2.5 text (line 168) asserts right-handed orientation *is assumed*, but does not independently pin down whether the cyclic order $(\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4) = (l,n,m,p)$ is positively or negatively oriented as an ordered 4-tuple under $V$. This is precisely where the convention slack lives.

## On the Test 4 chirality finding specifically

**Confirmed, and the attribution is essentially correct but should be reported as a *joint* convention mismatch between §3.1 and §2.5, not as a bug in §3 alone.**

Independent analytic check. Take the l-axis $u = (3/4, -1/4, -1/4, -1/4)$ and the zero-sum test vector $P = (0, 1, -1, 0)$.
- $V u = \mathbf v_1 = \tfrac{1}{\sqrt 3}(-1,-1,1)$.
- Using Def 3.1 entries: $\tilde K(u) P = (0,-1,-1,2)$, so $K(u) P = (0,-1,-1,2)/\sqrt 3$.
- $V(K(u)P) = \tfrac{1}{\sqrt 3}[-\mathbf v_2 - \mathbf v_3 + 2\mathbf v_4] = (2/3, -4/3, -2/3)$.
- $V P = \mathbf v_2 - \mathbf v_3 = \tfrac{1}{\sqrt 3}(2,0,2)$.
- $u_{\text{cart}} \times V P = \tfrac{1}{3}\,[(-1,-1,1)\times(2,0,2)] = (-2/3, 4/3, 2/3)$.

Hence $V K(u) P = -\, u_{\text{cart}} \times V P$, exactly. Since both $R_{\text{simp}}(u,\theta) = I + \sin\theta\,K + (1-\cos\theta)K^2$ and $R_{\text{cart}}(\hat n,\theta) = I + \sin\theta\,[\hat n]_\times + (1-\cos\theta)[\hat n]_\times^2$ are built the same way, and since $V K V^\top|_H = -\,[Vu]_\times|_H$, we have the exact identity

$$V\, R_{\text{simp}}(u,\theta)\, c \;=\; R_{\text{cart}}(V u,\,-\theta)\, (V c) \qquad (c \in H),$$

i.e. the $\theta \mapsto -\theta$ observed by the Skeptical is a *theorem*, not a sampling fluke. The `2.31e+00` positive-$\theta$ residual vs `4.44e-16` negative-$\theta$ residual is exactly what this identity predicts.

**Manuscript implication.** This is a convention-level annotation, not a mathematical error:
- The internal identities $R^\top G R = G$, $R \mathbf 1 = \mathbf 1$, $Ru = u$, $\det R = +1$, $R(\alpha)R(\beta) = R(\alpha+\beta)$, and $R = \exp(\theta K)$ all hold exactly (Tests 2 and 3, residuals 1e-16). The simplicial construction is an honest 1-parameter subgroup of the simplicial isometry group.
- What the Test 4 finding rules out is a *tacit* agreement between §3.1's cyclic-difference pattern and §2.5's vertex labelling. §2.5 only states the ambient $\mathbb R^3$ is right-handed; it does not establish that the ordered labelling $(l,n,m,p) \mapsto (\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4)$ induces a positively oriented basis of $H$ under $V$, nor that Def 3.1's sign pattern matches.
- The fix is one of three equivalent edits the Author must make:
  1. Transpose a pair of labels in §2.5 (e.g. swap the Cartesian triples for $\mathbf v_3$ and $\mathbf v_4$), or
  2. Transpose a pair of rows-and-columns in Def 3.1 (equivalently, flip the overall sign of $\tilde K$), or
  3. Leave both as is and add, after Def 3.1 (or at the end of §5), an explicit Remark:
     > *Orientation convention.* Under the isometry $V|_H$ of §2.5 mapping $(l,n,m,p)$ to $(\mathbf v_1,\mathbf v_2,\mathbf v_3,\mathbf v_4)$, the simplicial cross product satisfies $V K(u) V^\top|_H = -[V u]_\times$; equivalently $V R(u,\theta) V^\top|_H = R_{\text{cart}}(V u, -\theta)$. The simplicial construction is thus left-handed relative to §2.5's right-handed Cartesian embedding.

Option (3) is the least invasive and also flags a need to re-audit §8 (Ace's $F, G, H$ circulants) for sign consistency with Def 3.1.

## Summary

- The script's internal-consistency tests (Tests 1–3) are correct in construction and all pass with numerical residuals of $\mathcal O(10^{-16})$. Tests 2 and 3 are rigorous and safe to feed to the Author.
- Test 1's symbolic verification is weaker than the report states (one-point evaluation rather than polynomial-identity proof); this should be softened in the report, but it does not affect any manuscript claim because Test 3 independently verifies $R = \exp(\theta K)$ via `scipy.linalg.expm`.
- Test 4's chirality finding is **genuine and universal**. I reproduced the sign discrepancy analytically: $V K(u) V^\top|_H = -[V u]_\times$. The Skeptical's AMBER is appropriate, the diagnosis is substantively correct, and the finding should be forwarded to the Author as a **convention-level annotation or sign correction**, not a proof-level defect.
- The script would be stronger with (a) loop-over-seeds, (b) explicit `assert`s, and (c) a vertex-permutation control to localize the orientation to §3.1 vs §2.5. None of these change the headline conclusion, so I am not withholding clearance on them.

STATUS: GREEN
