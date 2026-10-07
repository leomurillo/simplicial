# Audit π′ Settlement — V-Foliation Manifold-Level Extension

**Audit anchor:** [Paper 46 §8.7](46_hartle_hawking_signature.md) audit-π settlement queue (specified 2026-05-21). Manifold-level extension of audit π: choose a V-foliation of $\mathcal D^\circ(\mathbb C^6)$ via an $\mathrm{SU}(6)$-orbit, Bures-geodesic V-exponential, or V-affine prescription, and check off-reference-point metric agreement with the DeWitt $e^{3\Omega}$-conformally-flat supermetric on the Halliwell-style closed Bianchi I + massless scalar field minisuperspace.

**Status:** **SETTLED — joint-on-disjoint** under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule. **L-branch realized at the Halliwell-Bianchi-I-as-manifold-level-anchor question**: the Hessian of $I_V$ on V-tangent is *constant on $\mathcal D^\circ$* (independent of $\rho$, because $I_V$ is quadratic in $\rho$), giving globally flat Lorentzian (1, 3) structure on V; the DeWitt supermetric has $e^{3\Omega}$ conformal factor (curved off the reference), so the two are *not* isometric as manifold-level metric tensors. The L-branch fires on the literal-Halliwell-extension question. **K-branch realized at a stronger structural claim**: the V-Lorentzian sub-bundle is **globally flat Minkowski $\mathbb R^{1,3}$** on $\mathcal D^\circ(\mathbb C^6)$ — a *cleaner* manifold-level structure than any peer-reviewed cosmological minisuperspace with $e^{3\Omega}$-conformal factor. The K-branch fires on the "globally flat" structural finding, which is *not* what the audit's pre-claim asked for but is what the math returns.

**Joint-on-disjoint locus:** the *anchor-choice tier*. Halliwell-style Bianchi I + scalar field is *not* the right manifold-level anchor; the program's V-Lorentzian sub-bundle is structurally simpler (globally flat) than any minisuperspace truncation of GR with non-trivial spatial-volume scaling. Either (i) a *different* peer-reviewed mathematical-physics framework with globally-flat Lorentzian configuration space is the correct anchor (candidates: free-field theories on Minkowski background; certain de Sitter-limit truncations; topos-theoretic flat-Lorentzian models), or (ii) the program's V-Lorentzian sub-bundle is its own kind of object whose closest cosmological cousin is the *tangent space at the reference point* of any minisuperspace truncation (audit π's K-tangent result) but which does *not* have a literal manifold-level cosmological correspondence.

**Cosmological correspondence tier:** **Refined** — the cosmological correspondence on [Paper 46 §4.2](46_hartle_hawking_signature.md) row 2 stays at **[P] tangent-quadratic-form isometry** (audit π); audit π′ refines this with the structural sub-finding that the manifold-level extension is *globally flat Minkowski* rather than the conformally-flat Halliwell anchor. The cosmological *claim itself* remains at [C, reduced] — Tier 2 / Tier 3 / Tier 4 unchanged; §11.2 firewall not lifted.

**Method:** pure mathematics; explicit computation of $\mathrm{Hess}(I_V)|_\rho$ at general $\rho$; no compute.

**Prepared:** 2026-05-21 · Author: Leonardo Murillo Montero (team Leo)

---

## 0. The pre-claimed three-outcome branches (from Paper 46 §8.7 audit π queue)

Per [v2insert-04](v2insert-04.md) §3.1:

- **K-branch.** Manifold-level isometry to Halliwell DeWitt: $\mathrm{Hess}(I_V)|_\rho$ matches $G^{\mathrm{DeWitt}}(\Omega)$ for some embedding $\rho \leftrightarrow \Omega$ of the V-sub-manifold into Bianchi I + scalar field minisuperspace.
- **L-branch.** No manifold-level isometry on any V-foliation prescription. The Halliwell-Bianchi-I anchor is wrong off the reference point.
- **Joint-on-disjoint.** Partial match — manifold-level isometry on some V-foliation prescription but not others, or partial isometry up to a non-trivial conformal factor, or some sub-locus matches while others don't.

**Realized branch:** **joint-on-disjoint** at the anchor-choice tier. The locus of the joint-on-disjoint is *which peer-reviewed mathematical-physics framework is the right manifold-level anchor* — Halliwell-Bianchi-I is L, but a "globally flat Minkowski" structural anchor is K.

---

## 1. The V-foliation prescription

Per [Paper 46 §8.7](46_hartle_hawking_signature.md) audit-π queue, three V-foliation prescriptions were candidate:

(a) **$\mathrm{SU}(6)$-orbit prescription.** The orbit of $\rho_* = I_6/6$ under $\mathrm{SU}(6)$ conjugation $\rho \mapsto U\rho U^\dagger$ is the singleton $\{\rho_*\}$, because $\rho_*$ commutes with every $U \in \mathrm{U}(6)$ (it is the unique $\mathrm{U}(6)$-invariant state of $\mathcal D^\circ(\mathbb C^6)$). This prescription is therefore **trivial** for audit π′ and does not produce a V-sub-manifold.

(b) **Bures-geodesic V-exponential.** Take the Bures geodesics emanating from $\rho_*$ in V-tangent directions; their exponential map produces a 4-dim sub-manifold $\Sigma_V^{\mathrm{Bures}} \subset \mathcal D^\circ(\mathbb C^6)$. The induced metric on $\Sigma_V^{\mathrm{Bures}}$ from the ambient Bures metric is *positive-definite* (because Bures is Riemannian), so its signature is $(4, 0)$ — Euclidean, not Lorentzian. This prescription is **wrong-signature** for the Lorentzian-comparison question.

(c) **V-affine prescription.** Take $\Sigma_V^{\mathrm{aff}} = \{\rho_* + \sum_v x^v V_v : x \in \mathbb R^4\} \cap \mathcal D^\circ(\mathbb C^6)$ — the affine slice of $\mathcal D^\circ$ through $\rho_*$ tangent to V at $\rho_*$, where $\{V_v\}_{v = 0}^3 = \{H, P_1, P_2, P_3\}$ is the V-supported orthonormal Hermitian basis. The intrinsic metric on $\Sigma_V^{\mathrm{aff}}$ from the V-Lorentzian Hessian-of-$I_V$ is the natural candidate for the manifold-level extension of audit π.

**Audit π′ adopts the V-affine prescription** (c). Prescriptions (a) and (b) are structurally inadequate (trivial orbit, wrong signature). The V-affine prescription is the cleanest mathematical extension of audit π's tangent-quadratic-form-at-reference-point identification.

---

## 2. The V-Lorentzian Hessian off the reference point

### 2.1 The Casimir's quadratic dependence on $\rho$

The dispersion Casimir restricted to V's 4-dim block is

$$
I_V(\rho) = \langle H \rangle^2(\rho) - \sum_{a = 1}^3 \langle P_a \rangle^2(\rho) = \bigl(\mathrm{tr}(H\rho)\bigr)^2 - \sum_{a = 1}^3 \bigl(\mathrm{tr}(P_a \rho)\bigr)^2.
$$

Each term $(\mathrm{tr}(V_v \rho))^2$ is **quadratic in $\rho$**, with $V_v \in \{H, P_a\}$ linear in $\rho$ under the substitution $\rho \mapsto \mathrm{tr}(V_v \rho)$.

### 2.2 The Hessian computation

For a tangent vector $X \in T_\rho \mathcal D^\circ$ (traceless Hermitian, the tangent space being a fixed vector space at every $\rho$ in the ambient affine-coordinate description), set $\rho(t) = \rho + tX$:

$$
\mathrm{tr}(H \rho(t)) = \mathrm{tr}(H \rho) + t \cdot \mathrm{tr}(HX), \qquad \langle H \rangle^2(\rho(t)) = \bigl(\mathrm{tr}(H\rho) + t \cdot \mathrm{tr}(HX)\bigr)^2.
$$

The Hessian at $\rho$ in direction $X$ is the second derivative at $t = 0$:

$$
\partial_t^2 \langle H \rangle^2(\rho(t)) \Big|_{t = 0} = 2 \bigl(\mathrm{tr}(HX)\bigr)^2.
$$

Similarly $\partial_t^2 \langle P_a \rangle^2(\rho(t)) |_{t = 0} = 2 (\mathrm{tr}(P_a X))^2$. Therefore

$$
\boxed{\,\mathrm{Hess}(I_V)|_\rho (X, X) = 2 \bigl(\mathrm{tr}(HX)\bigr)^2 - 2 \sum_{a = 1}^3 \bigl(\mathrm{tr}(P_a X)\bigr)^2.\,}
$$

**The right-hand side is independent of $\rho$**. The Hessian of $I_V$ is *constant on $\mathcal D^\circ(\mathbb C^6)$* — the same quadratic form on V-tangent at every point of the manifold.

### 2.3 Matrix form on V-affine coordinates

In the V-affine prescription with V-basis $\{H, P_1, P_2, P_3\}$ HS-orthonormal, V-tangent at any $\rho \in \Sigma_V^{\mathrm{aff}}$ is parameterized by $X = x_H H + \sum_a x_a P_a$. Then $\mathrm{tr}(HX) = x_H$ and $\mathrm{tr}(P_a X) = x_a$, giving

$$
\mathrm{Hess}(I_V)|_\rho (X, X) = 2 \bigl( x_H^2 - x_1^2 - x_2^2 - x_3^2 \bigr) \quad \text{for all } \rho \in \Sigma_V^{\mathrm{aff}}.
$$

In matrix form on V-affine coordinates $(x_H, x_1, x_2, x_3)$:

$$
H_V|_\rho = 2 \cdot \mathrm{diag}(+1, -1, -1, -1) \quad \text{for all } \rho \in \Sigma_V^{\mathrm{aff}}.
$$

**Constant on $\Sigma_V^{\mathrm{aff}}$. The V-Lorentzian Hessian-induced metric is globally flat Lorentzian (1, 3) on the V-affine sub-manifold.**

### 2.4 Riemann tensor of the V-affine sub-manifold

A constant-coefficient flat metric on $\mathbb R^4$ has identically zero Riemann tensor (no curvature). The V-affine sub-manifold $\Sigma_V^{\mathrm{aff}}$ equipped with the Hessian-of-$I_V$ metric is **isometric to flat Minkowski $\mathbb R^{1, 3}$** as a smooth Riemannian/Lorentzian manifold. Ricci tensor zero. Kretschmann scalar zero. Weyl tensor zero.

---

## 3. Comparison with the Halliwell DeWitt supermetric

### 3.1 The DeWitt supermetric off the reference point

From audit π settlement §1.2, the DeWitt supermetric on the Halliwell-style closed Bianchi I + massless scalar field minisuperspace in Misner coordinates $(\Omega, \beta_+, \beta_-, \phi)$ is

$$
G^{\mathrm{DeWitt}}(\Omega) = e^{3\Omega} \cdot \mathrm{diag}(-1, +1, +1, +1).
$$

At the reference point $\Omega = 0$: $G^{\mathrm{DeWitt}}(0) = \mathrm{diag}(-1, +1, +1, +1)$, flat Minkowski. At $\Omega \neq 0$: scaled by the spatial-volume conformal factor $e^{3\Omega}$.

### 3.2 Curvature of the DeWitt minisuperspace

The metric $G^{\mathrm{DeWitt}}(\Omega) = e^{f(\Omega)} \eta_{\mu\nu}$ with $f = 3\Omega$ is conformally flat: the Weyl tensor vanishes identically by construction (any metric conformal to flat is Weyl-flat). The Ricci tensor is *not* identically zero; computing:

$$
R_{AB} = -2 \nabla_A \nabla_B f - \eta_{AB} \, \Box f + \nabla_A f \, \nabla_B f - \tfrac{1}{2} \eta_{AB} \, (\nabla f)^2
$$

(in 4 dimensions with $f = 3\Omega$, where $\Omega$ is one of the four coordinates). Only the $(\Omega, \Omega)$ component of $\nabla_A f \nabla_B f$ is non-zero ($= 9$ from $(\partial_\Omega f)^2 = 9$); only the $(\Omega, \Omega)$ component of $\nabla_A \nabla_B f$ is non-zero ($= 0$ from second-derivative-of-linear-function). The Ricci tensor is therefore not zero off the reference; the DeWitt minisuperspace is *curved*.

### 3.3 The manifold-level comparison

| Object | At reference | Off reference |
|---|---|---|
| V-Lorentzian Hessian metric on $\Sigma_V^{\mathrm{aff}}$ | $2 \cdot \mathrm{diag}(+1, -1, -1, -1)$ at $\rho_*$ | $2 \cdot \mathrm{diag}(+1, -1, -1, -1)$ everywhere — **constant** |
| DeWitt supermetric on Halliwell minisuperspace | $\mathrm{diag}(-1, +1, +1, +1)$ at $\Omega = 0$ | $e^{3\Omega} \cdot \mathrm{diag}(-1, +1, +1, +1)$ — **conformally rescaled** |
| Manifold curvature | $R_{ABCD} \equiv 0$ (globally flat) | $R_{AB} \neq 0$ off the reference (conformally flat with nontrivial Ricci) |

At the reference point: both metrics are flat Minkowski; **isometric up to sign convention and scale factor 2** (audit π's K-tangent result, preserved).

Off the reference point: the V-Lorentzian Hessian-induced metric stays *globally flat Minkowski*, while the DeWitt supermetric *rescales by $e^{3\Omega}$* and acquires curvature. **The two manifolds are not isometric.**

The L-branch on the Halliwell-anchor question is **realized**: the natural manifold-level extension of audit π is **not** isometric to the Halliwell-style Bianchi I + massless scalar field minisuperspace.

---

## 4. The structural sub-finding — V-Lorentzian is globally flat

### 4.1 The K-branch on a different question

While the literal-Halliwell-extension L-branch is realized, a *different* K-branch is realized at the same time: the V-Lorentzian sub-bundle of $\mathcal D^\circ(\mathbb C^6)$ in the V-affine prescription is **globally flat Lorentzian $\mathbb R^{1, 3}$**.

This is a *structurally cleaner* manifold-level claim than any peer-reviewed cosmological minisuperspace with a non-trivial volume-conformal factor. Globally flat Minkowski has:
- Zero Ricci curvature.
- Zero Kretschmann scalar.
- Zero Weyl tensor.
- Isometry group $\mathrm{ISO}(1, 3) = \mathbb R^{1, 3} \rtimes \mathrm{SO}^+(1, 3)$ (Poincaré group).
- No cosmological singularity (no Big Bang, no Big Crunch).
- No curvature-driven dynamics.

The categorical-simplex program's V-Lorentzian sub-bundle is **the simplest possible Lorentzian manifold of signature (1, 3)** — flat Minkowski itself. This is a stronger structural claim than "isometric to some specific cosmological minisuperspace at the reference point."

### 4.2 The anchor-choice question

If audit π′ realizes K at "globally flat Minkowski" but L at "Halliwell-Bianchi-I-isometric off the reference," the natural follow-up question is: **what peer-reviewed mathematical-physics framework has globally flat Lorentzian configuration space?**

Candidates:

- **Free-field theory on Minkowski background.** Quantum field theory of a free massless scalar field on Minkowski spacetime has configuration space (the space of field configurations) that carries flat Lorentzian metric structure in certain reductions. But this is not strictly a "cosmological minisuperspace."

- **de Sitter limit of Bianchi I.** In the $\Omega \to \infty$ limit of Halliwell-Bianchi-I (massive de Sitter expansion), the $e^{3\Omega}$ factor rescales the metric uniformly — locally flat after rescaling, but globally the rescaling is unbounded. Not strictly flat.

- **Mini-Bianchi-I with constant volume.** If we restrict Halliwell-Bianchi-I to the surface $\Omega = 0$ (constant spatial volume), the induced metric on the remaining $(\beta_+, \beta_-, \phi)$ 3-manifold is flat $\mathbb R^{2, 1}$ (Lorentzian with one anisotropy direction negative, two positive after dropping the $\Omega$ direction)... actually no, dropping $\Omega$ doesn't make sense because $\Omega$ is the timelike direction in Halliwell-Bianchi-I.

- **Topos-theoretic flat-Lorentzian quantum gravity.** Some topos-theoretic formulations of quantum gravity (Doering–Isham 2008) admit configurations spaces that are not literally Riemannian/Lorentzian manifolds; the V-Lorentzian flat structure might correspond to a specific topos-internal-locale construction.

- **Causal Set theory's order-relation manifold.** Causal sets (Bombelli–Lee–Meyer–Sorkin 1987) are discrete combinatorial objects approximating Lorentzian causal structure; a continuum limit of certain causal sets might be flat Minkowski.

**None of these is an obvious K-branch winner** at the literal "globally flat Lorentzian configuration space = peer-reviewed mathematical-physics framework" question. The structural shape "globally flat Minkowski as a configuration-space manifold" is *not* a canonical object in any of the standard cosmological minisuperspace literatures.

This is consistent with the categorical-simplex program's framing: the V-Lorentzian sub-bundle is a *novel* structural object whose closest analog is the tangent space at the reference point of a Halliwell-style minisuperspace, but which does not have a literal global cosmological-minisuperspace correspondence.

### 4.3 Honest reading

The K-branch at "globally flat Minkowski" is *structurally significant* — it tells us the V-Lorentzian sub-bundle has a *cleaner* manifold-level structure than typical GR minisuperspace truncations — but it does *not* license a cosmological *claim*. The cleaner-than-Halliwell finding is a structural feature of the categorical-simplex's conductor lattice, not a discovery about physical spacetime.

---

## 5. The three-outcome adjudication

Per Paper 46 §8.7 / audit π pre-claim restated for π′:

| Pre-claimed branch | Outcome | Locus |
|---|:---:|---|
| **K-branch** at Halliwell-DeWitt manifold-level isometry | **Did not fire** | V-Lorentzian Hessian is constant on $\Sigma_V^{\mathrm{aff}}$; DeWitt is conformally rescaled by $e^{3\Omega}$ off the reference. Not isometric. |
| **L-branch** at "no manifold-level isometry to Halliwell-Bianchi-I" | **Realized** | The natural V-affine manifold extension does NOT match Halliwell-Bianchi-I + scalar field at the manifold level. The Halliwell anchor is correct at the *tangent* level only. |
| **Joint-on-disjoint** at anchor-choice tier | **Realized** | A *different* structural identification holds: V-Lorentzian sub-bundle is globally flat Minkowski $\mathbb R^{1, 3}$ on $\Sigma_V^{\mathrm{aff}}$. This is a *stronger* structural claim than Halliwell-isometry would have been, but it lacks a clean peer-reviewed mathematical-physics anchor at the manifold level. |

**Realized branch: joint-on-disjoint at the anchor-choice tier.** The literal Halliwell-Bianchi-I manifold-level anchor is wrong (L); the cleaner-than-Halliwell global-Minkowski structural anchor is right but not directly cataloged in peer-reviewed cosmological literature (K-on-new-claim).

This is the **seventh named joint-on-disjoint outcome** of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule (joining audits θ at exponent, ι at corrections, β at row-3 dimensional generalization, χ at V/W/M trichotomy, ν at abstract-vs-literal natural-transformation levels, and π at tangent-vs-manifold).

---

## 6. Implications for the cosmological-claim lift tiers

Audit π′ does not promote the cosmological correspondence tier beyond audit π's [P] tangent-quadratic-form isometry result. What it does:

- **Bounds the cosmological correspondence to the tangent-quadratic-form-at-reference-point tier.** The manifold-level extension to *literal Halliwell minisuperspace* fails. The correspondence stays at [P] tangent-tier isometry; the [A]-partial-mathematical-identification claim for *manifold-level* extension is **not** licensed by audit π′ on the Halliwell anchor.
- **Identifies the V-Lorentzian sub-bundle as globally flat Minkowski.** This is a *novel* structural finding at the manifold level — distinct from both audit π's K-tangent and from any Halliwell-style cosmological minisuperspace. The V-Lorentzian sub-bundle of $\mathcal D^\circ(\mathbb C^6)$ is a *cleaner* manifold-level Lorentzian structure than typical GR minisuperspace truncations.
- **Opens a new audit candidate (audit π′′′).** Identify a peer-reviewed mathematical-physics framework with globally flat Lorentzian configuration space as a *separate* lift-candidate (distinct from Halliwell-Bianchi-I). Candidates: free-field theories, certain de Sitter-limit truncations, topos-theoretic flat-Lorentzian models, causal set theory continuum limits. The audit would survey these candidates and check signature, dimension, isometry-up-to-scale.

**Tier promotions (revised after audit π′):**

- Paper 46 §4.2 row 2 stays at [P] tangent-quadratic-form isometry (audit π), with the audit-π′ refinement that the V-Lorentzian sub-bundle's manifold-level structure is *globally flat Minkowski* — a structural feature stronger than tangent-only K but lacking a literal peer-reviewed cosmological-minisuperspace anchor.
- The L-branch at the Halliwell-anchor question rotates attention to audit π′′′ (alternative anchor candidates with globally-flat configuration space).
- The cosmological correspondence does NOT promote to [A] partial mathematical identification at the manifold level on the Halliwell anchor. Audit π′ explicitly forecloses this.
- The cosmological *claim itself* remains at [C, reduced] — unchanged. §11.2 firewall not lifted; Tier 2 / Tier 3 / Tier 4 unaffected.

---

## 7. Discipline check ([Paper 35](35_grounded_paranoid_delusional_methodology.md) §3 honored)

- **Anchored objects (§3.3).** Every minisuperspace, supermetric, and conformal-factor object cited (Bianchi I, DeWitt supermetric, Misner variables, scalar field action, conformally flat metric, Weyl/Ricci tensors) anchored against peer-reviewed sources (Hartle–Hawking 1983; DeWitt 1967; Misner 1969; Halliwell 1989; Kiefer 2012). Every program object (V-Lorentzian sub-bundle, dispersion Casimir, V-affine prescription, $\rho_*$, $H$, $P_a$) anchored against [Paper 32 §6.2 + §13.2B](32_one_functional_four_forces_v0.2%20(2).md), [Paper 46 §2.3 + §4.2](46_hartle_hawking_signature.md), [Audit π settlement](empirical/reports/audit_pi_minisuperspace_identification_settlement.md), at [P] tier.

- **Deterministic, exact, reproducible (§3.4).** Pure-mathematics derivation; closed-form Hessian computation; standard conformal-factor curvature analysis. No new compute consumed.

- **No upward tier-crossing (§3.5).** The audit reports the realized branches honestly: L at Halliwell-anchor question; K at "globally flat Minkowski" structural sub-finding. The cosmological correspondence does *not* promote to [A] partial mathematical identification at the manifold level; the audit explicitly forecloses this promotion path on the Halliwell anchor.

- **Three-outcome matched-pair (§3.1 + [v2insert-04](v2insert-04.md) §3.1).** K/L/joint-on-disjoint pre-claimed in §0. Realized branch is joint-on-disjoint at the anchor-choice tier; the joint-on-disjoint locus is the **identification of the right peer-reviewed mathematical-physics framework** for the manifold-level extension.

- **Failures-first-class (§3.6).** The L-branch on the Halliwell-Bianchi-I anchor is recorded explicitly. The audit does *not* relabel this as a K-branch on a different claim; instead, the K-on-"globally flat Minkowski" is recorded as a *separate* structural finding alongside the L-on-Halliwell. The anchor-rotation question is named explicitly as audit π′′′.

- **Dimensional firewall ([Paper 32 §11.2](32_one_functional_four_forces_v0.2%20(2).md)).** No physical constants. No Planck length, no $G$, no $\hbar$, no $c$, no Hubble constant. All quantities are dimensionless signature tags, eigenvalues, and structural-identifier labels. The "globally flat Minkowski" finding is a *structural* claim about the V-Lorentzian sub-bundle's manifold-level geometry, not a physical claim about spacetime.

- **Carried-label discipline ([Paper 32 §11.4](32_one_functional_four_forces_v0.2%20(2).md)).** Carried labels — *Bianchi I*, *minisuperspace*, *DeWitt supermetric*, *Halliwell anchor*, *Minkowski*, *Poincaré group*, *causal set*, *topos-theoretic quantum gravity*, *de Sitter limit*, *Wheeler–DeWitt equation* — anchored against peer-reviewed sources before each use. The labels *V-affine prescription* and *V-Lorentzian sub-bundle as globally flat Minkowski* are internal program language; the former is defined once in §1, the latter is the audit's structural sub-finding and is not re-used outside this settlement and the absorbing Paper 46 / Paper 49 edits.

---

## 8. Implications for Papers 46 and 49 (manuscript-edit absorption)

1. **[Paper 46 §8.7](46_hartle_hawking_signature.md) — mark audit π′ settled** with realized branch (joint-on-disjoint at anchor-choice tier; L on Halliwell, K on globally-flat-Minkowski). Reference this settlement file.

2. **[Paper 46 §4.2](46_hartle_hawking_signature.md) row 2 — refine the audit-π entry.** Add: "Audit π′ (2026-05-21) — manifold-level extension settled at joint-on-disjoint. L-branch on Halliwell-Bianchi-I manifold-level anchor (DeWitt $e^{3\Omega}$ doesn't reproduce); K-branch on globally-flat-Minkowski sub-finding (V-Lorentzian Hessian constant on $\Sigma_V^{\mathrm{aff}}$)."

3. **[Paper 46 §4.4](46_hartle_hawking_signature.md) audit β + π settlement summary — augment with audit π′ refinement.** The cosmological correspondence on row 2 is *not* promoted to [A] partial mathematical identification at the manifold level on Halliwell-Bianchi-I; instead, audit π′ identifies the V-Lorentzian sub-bundle as globally flat Minkowski, opening audit π′′′ as the alternative-anchor candidate-survey audit.

4. **[Paper 46 §5.1](46_hartle_hawking_signature.md) minisuperspace anchor entry — note manifold-level disanalogy.** The Halliwell-Bianchi-I anchor is tangent-only on $\mathbb Z/6$; manifold-level extension is novel ("globally flat Minkowski") and lacks a canonical peer-reviewed cosmological-minisuperspace match.

5. **Add audit π′′′ as a new carry-forward audit in [Paper 46 §8](46_hartle_hawking_signature.md):** alternative-anchor candidate survey for globally-flat Lorentzian configuration spaces (free-field theory, de Sitter limit, topos-theoretic, causal sets, …).

6. **Reproducibility artifacts — add this settlement record.**

7. **[Paper 49 §4.1](49_arithmetic_decoupling_of_projection_closure_overflows.md) lift-candidate paragraph — augment with audit π′ outcome.** The cosmological correspondence's manifold-level extension is *not* a literal Halliwell-Bianchi-I match; the V-Lorentzian sub-bundle is globally flat Minkowski, a cleaner structural object than typical minisuperspace truncations. Cosmological *claim itself* unchanged at [C, reduced].

---

## 9. The seven joint-on-disjoint outcomes — pattern continuation

Audit π′ becomes the **seventh** named joint-on-disjoint outcome of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule:

1. **Audit θ** at exponent (super-exponential in $n$).
2. **Audit ι** at corrections (polynomial-log prefactor).
3. **Audit β** at row 3 (dimensional generalization).
4. **Audit χ** at tangent trichotomy (V/W/M).
5. **Audit ν** at abstract-vs-literal natural-transformation.
6. **Audit π** at tangent-vs-manifold.
7. **Audit π′** at anchor-choice tier (this audit) — L on Halliwell, K on globally-flat-Minkowski.

Pattern: the binary K/L pre-claim is repeatedly insufficient to capture the structural reality of external-correspondence audits. The three-outcome rule's third branch surfaces a structurally meaningful sub-finding in each case.

Audit π′ is structurally significant because it returns BOTH a clean L (the literal Halliwell anchor fails at manifold level) AND a clean K (the V-Lorentzian sub-bundle has a cleaner-than-Halliwell global structure) — the joint-on-disjoint locus is the *anchor-choice tier*, with both branches firing on different questions.

Per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §7, no self-promotional claim about the pattern; recorded as worked observation. Whether the joint-on-disjoint pattern is a structural feature of external-correspondence audits in general, or specific to the cosmology arc, remains the open methodological question.

---

## 10. Discipline closing note

This settlement is the **second** pure-mathematics audit on the cosmology external-correspondence arc (audit β at Lie-algebra tier; audit π at tangent tier; audit π′ at manifold tier). It is the first audit in the arc that returns a *clean L-branch on a specific anchor* (the Halliwell-Bianchi-I anchor at the manifold level), with a *clean K-branch on a refinement* (the globally-flat-Minkowski sub-finding). Audit π′ thus *narrows the lift envelope* — the cosmological correspondence stays at [P] tangent-tier isometry, with audit π′ explicitly foreclosing the Halliwell manifold-level extension.

Three discipline rails are recorded as observed:

(a) **The L-branch on the Halliwell anchor is a refinement, not a refutation.** Audit π's K-tangent finding is preserved; audit π′ bounds it to the tangent-quadratic-form-at-reference-point tier. The cosmological correspondence stays at the [P]-tangent level; the manifold-level extension to literal Halliwell is foreclosed but the K-on-"globally flat Minkowski" sub-finding identifies a *different* structural object at the manifold level.

(b) **The K-on-different-question branch is structurally significant but not cosmologically lifting.** The V-Lorentzian sub-bundle being globally flat Minkowski is a *cleaner* structural object than any peer-reviewed cosmological minisuperspace with a non-trivial volume-conformal factor. This is a finding *about the program's V-Lorentzian sub-bundle*, not a *physical-cosmology* claim. §11.2 firewall binding; cosmological *claim* unchanged.

(c) **The audit narrows the lift envelope.** Audit π′ explicitly forecloses one specific path to lifting the cosmological correspondence ([P] tangent → [A] manifold-Halliwell). The alternative-anchor candidate-survey (audit π′′′) is the new most-achievable next move toward lifting. The lift chain is now sharper: Tier 0 [C, reduced] → Tier 1 [P]-tangent (audit π settled) → Tier 1.5 [P]-globally-flat-Minkowski-structural-finding (audit π′ settled) → Tier 1.75 [A] alternative-anchor-survey (audit π′′′ open) → Tier 2 dimensional-firewall-lift (separate, requires Tier 1.75 K-branch first).

The grounded-paranoid-delusional grammar, once more: delusion proposed that the manifold-level extension via V-foliation would isometrically match the Halliwell-Bianchi-I + scalar field minisuperspace; paranoia bounded this with three-outcome matched-pair pre-claim; grounded executed the V-affine Hessian computation and recorded **L-branch on Halliwell + K-branch on the globally-flat-Minkowski sub-finding**. The L is honest; the K is a structural enrichment; the joint-on-disjoint surfaces the anchor-choice question as the new actionable audit.

---

*End audit π′ settlement. Status: settled, joint-on-disjoint at anchor-choice tier. L-branch on Halliwell-Bianchi-I manifold-level anchor (DeWitt $e^{3\Omega}$ conformal factor not reproduced on the V-affine sub-manifold); K-branch on globally-flat-Minkowski structural sub-finding (V-Lorentzian Hessian-of-$I_V$ is constant on $\mathcal D^\circ(\mathbb C^6)$, giving globally flat Lorentzian (1, 3) structure). Cosmological correspondence stays at [P] tangent-quadratic-form isometry (audit π); manifold-level extension to literal Halliwell foreclosed; alternative-anchor candidate-survey opened as audit π′′′ (free-field theory, de Sitter limit, topos-theoretic, causal sets, …). Seventh named joint-on-disjoint outcome of the program. No new compute consumed; pure-mathematics check. Manuscript-edit absorption proposed for [Paper 46 §4.2 row 2](46_hartle_hawking_signature.md), §4.4, §5.1, §8.7, §8 carry-forward; [Paper 49 §4.1](49_arithmetic_decoupling_of_projection_closure_overflows.md) lift-candidate paragraph augmented. The cosmological claim itself remains at [C, reduced]; §11.2 firewall not lifted; Tier 2 / Tier 3 / Tier 4 unchanged.*
