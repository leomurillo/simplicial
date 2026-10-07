# Audit π Settlement — Minisuperspace Identification

**Audit anchor:** [Paper 46 §8.7](46_hartle_hawking_signature.md) (specified 2026-05-21). Forced-identification check between the V-Lorentzian (1, 3) sub-bundle on `D(ℂ⁶)` at `ρ_*` and the DeWitt supermetric on a 4-dim peer-reviewed minisuperspace candidate (Halliwell-style closed Bianchi I + scalar field).

**Status:** **SETTLED — joint-on-disjoint** under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule. **K-branch realized at the tangent-quadratic-form level**: the two 4-dim flat Lorentzian inner product spaces are isometric up to sign convention and overall scale factor 2. **Joint-on-disjoint at the manifold-level extension**: the DeWitt supermetric carries an `Ω`-dependent conformal factor `e^(3Ω)` that introduces curvature off the reference point, while the V-Lorentzian sub-bundle as currently defined by [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md) is a Hessian at the single point `ρ_*` and does not see Ω-curvature. The K-tangent match is unambiguous; the manifold-level extension is a structurally meaningful queued sub-audit (audit π′).

**Cosmological correspondence tier promotion:** **[C, reduced] structural shape → [A] partial mathematical identification at the tangent-quadratic-form tier**. The Tier-1 lift-candidate of [Paper 46 §8.7](46_hartle_hawking_signature.md) realizes partial K; the L-branch (alternative-anchor rotation to LQC, CDT, topos-theoretic QG) does NOT fire because Halliwell-style Bianchi I + scalar field provides a literal isometric tangent match. The cosmological *claim itself* (Tier 2: forced dimensional prediction; Tier 3: external replication; Tier 4: physical-mechanism) remains at [C, reduced]; §11.2 firewall not lifted by audit π.

**Method:** pure mathematics; closed-form derivations on both sides; no compute. Reference to existing [`empirical/paper32_13_2B_fourth_order_casimir_audit.py`](empirical/paper32_13_2B_fourth_order_casimir_audit.py) for the V-Lorentzian Hessian's numerical confirmation.

**Prepared:** 2026-05-21 · Author: Leonardo Murillo Montero (team Leo)

---

## 0. The pre-claimed three-outcome branches (from Paper 46 §8.7)

Per [v2insert-04](v2insert-04.md) §3.1, the audit pre-claims:

- **K-branch.** Literal manifold match + metric isometry up to overall scale. Cosmological correspondence promotes from [C, reduced] *structural shape* to **[A] *mathematical identification*** — "V-Lorentzian sub-bundle on `D(ℂ⁶)` IS the named minisuperspace."

- **L-branch.** Manifolds not diffeomorphic, or metrics not isometric. Cosmological correspondence stays at [C, reduced]. Rotation to alternative peer-reviewed anchors (LQC — Bojowald 2005; CDT — Ambjørn et al. 2004; topos-theoretic QG — Doering–Isham 2008).

- **Joint-on-disjoint.** Partial match — same diffeomorphism class but non-isometric metrics, or same metric up to scale but different boundary structure, or matching on a sub-region of V but not the full block. Cosmological correspondence promotes to [A] partial; the partial-match locus characterized.

**Realized branch:** **joint-on-disjoint**, with the locus identified as the *manifold-level vs tangent-quadratic-form-level* distinction. K-branch is unambiguous at the tangent-quadratic-form level; the manifold-level extension is structurally meaningful and queued.

---

## 1. The candidate minisuperspace and its DeWitt supermetric

### 1.1 Halliwell-style closed Bianchi I + scalar field

Following Halliwell 1989 (*A bibliography of papers on quantum cosmology*, NSF-ITP-89-162) and the standard derivation in Kiefer 2012 (*Quantum Gravity*, 3rd ed., Ch. 8 §8.2), the Bianchi I cosmology with metric

$$
\mathrm{d}s^2 = -N(t)^2 \mathrm{d}t^2 + a(t)^2 \bigl( \mathrm{e}^{2\beta_+ + 2\sqrt{3}\beta_-} \mathrm{d}x^2 + \mathrm{e}^{2\beta_+ - 2\sqrt{3}\beta_-} \mathrm{d}y^2 + \mathrm{e}^{-4\beta_+} \mathrm{d}z^2 \bigr)
$$

reduces (via the standard Einstein–Hilbert plus minimally-coupled massless scalar field action) to the minisuperspace Lagrangian in Misner variables $\Omega = \log a$, $\beta_+$, $\beta_-$, and scalar field $\phi$:

$$
L_{\mathrm{kin}} = \mathrm{e}^{3\Omega} \bigl( -\dot{\Omega}^2 + \dot{\beta}_+^2 + \dot{\beta}_-^2 + \dot{\phi}^2 \bigr) \big/ N(t)
$$

(setting Newton's constant and the scalar-field normalization to unit values; the dimensional choice is irrelevant for the metric-comparison question, per [Paper 32 §11.2](32_one_functional_four_forces_v0.2%20(2).md) firewall — the audit asks about *isometry up to scale*, not absolute scale).

### 1.2 The DeWitt supermetric

The Wheeler–DeWitt supermetric on the 4-dimensional minisuperspace $(\Omega, \beta_+, \beta_-, \phi)$ is, by the standard definition $G^{\mathrm{DeWitt}}_{AB} = \tfrac{\partial^2 L_{\mathrm{kin}}}{\partial \dot{q}^A \partial \dot{q}^B}$ at fixed $N$ (DeWitt 1967, *Quantum theory of gravity I*, Phys. Rev. **160**):

$$
G^{\mathrm{DeWitt}}(\Omega) = \mathrm{e}^{3\Omega} \cdot \mathrm{diag}(-1, +1, +1, +1)
$$

in the coordinate basis $(\Omega, \beta_+, \beta_-, \phi)$. Signature **(1, 3) Lorentzian** with the timelike direction being $\Omega$ (the "conformal mode" of the scale factor — physically, the cosmological-volume direction).

### 1.3 The reference point and the flat tangent

At the reference point $\Omega = 0$ (equivalently $a = 1$, *de Sitter–like* unit volume), the supermetric reduces to

$$
G^{\mathrm{DeWitt}}(0) = \mathrm{diag}(-1, +1, +1, +1) = \eta_{\mu\nu}^{\mathrm{Mink}}
$$

i.e., the **flat Minkowski metric on $\mathbb R^4$**. At points $\Omega \neq 0$, the conformal factor $\mathrm{e}^{3\Omega}$ introduces curvature: the metric remains conformally flat (Weyl tensor vanishes by inspection), but the Ricci tensor is nonzero by virtue of the $\Omega$-derivatives of the conformal factor.

The DeWitt supermetric is therefore **flat at the reference point and conformally flat globally** on the minisuperspace.

---

## 2. The V-Lorentzian Bures-Hessian metric

### 2.1 The dispersion Casimir on V's 4-dim block

From [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md) ([P]) and [Paper 46 §2.3](46_hartle_hawking_signature.md), the dispersion Casimir at $\rho_* = I_6/6$ is

$$
I_{\mathrm{complex}}(\rho) = \langle H \rangle^2(\rho) + \alpha^2 \cdot \bigl(m^2_{\mathrm{simplex}}(\rho)\bigr)^2 - \sum_{a = 1}^3 \langle P_a \rangle^2(\rho)
$$

where $H, P_1, P_2, P_3$ are an orthonormal basis (under the Hilbert–Schmidt inner product $\langle A, B \rangle_{\mathrm{HS}} = \mathrm{tr}(A^\dagger B)$) of V-supported traceless Hermitian operators on $\mathbb C^6$ ([Paper 32 §6.2](32_one_functional_four_forces_v0.2%20(2).md), $V = A_2 \oplus A_3$ on $\mathbb Z/6\mathbb Z$). Restricting to V's 4-dim block — dropping the quartic $\alpha^2 (m^2_{\mathrm{simplex}})^2$ term, which is M-supported and vanishes on V-rays per [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md) [P] — gives

$$
I_V(\rho) := \langle H \rangle^2(\rho) - \sum_{a = 1}^3 \langle P_a \rangle^2(\rho).
$$

### 2.2 The Hessian at the centroid

Let $X \in T_{\rho_*} \mathcal{D}^\circ(\mathbb C^6)$ be a V-supported traceless Hermitian tangent vector with V-block decomposition

$$
X = x_H H + x_1 P_1 + x_2 P_2 + x_3 P_3.
$$

Using $\mathrm{tr}(H^2) = \mathrm{tr}(P_a P_b) = \delta_{ab}$ (orthonormal V-basis), $\mathrm{tr}(H P_a) = 0$ (orthogonality between $H$ and $P_a$), and $\mathrm{tr}(H) = \mathrm{tr}(P_a) = 0$ (tracelessness):

$$
\langle H \rangle(\rho_* + t X) = \mathrm{tr}\bigl(H (\rho_* + tX)\bigr) = \mathrm{tr}(H \rho_*) + t \cdot \mathrm{tr}(HX) = 0 + t \cdot x_H = t \cdot x_H
$$

(the $\mathrm{tr}(H\rho_*) = \mathrm{tr}(H) / 6 = 0$ vanishes because $H$ is traceless), and similarly

$$
\langle P_a \rangle(\rho_* + tX) = t \cdot x_a.
$$

Substituting:

$$
I_V(\rho_* + tX) = t^2 \bigl( x_H^2 - x_1^2 - x_2^2 - x_3^2 \bigr) + O(t^4).
$$

The Hessian at $\rho_*$ on V's 4-dim block in the basis $(H, P_1, P_2, P_3)$ is the matrix of second derivatives at $t = 0$:

$$
\boxed{\,\mathrm{Hess}(I_V)\big|_{\rho_*} = 2 \cdot \mathrm{diag}(+1, -1, -1, -1)\quad \text{on } V \cong \mathbb R^4.\,}
$$

Signature **(1, 3) Lorentzian**, with the "+1" eigenvalue on the $H$-direction (the "energy" / single-operator direction) and "-1" eigenvalues on the $P_a$-directions (the "momentum" / probe-operator directions). The matrix is constant-diagonal — the V-Lorentzian sub-bundle is **flat as a quadratic form on $\mathbb R^4$**.

### 2.3 Numerical anchor

The Hessian's signature and eigenvalue structure are confirmed by [`empirical/paper32_13_2B_fourth_order_casimir_audit.py`](empirical/paper32_13_2B_fourth_order_casimir_audit.py) (signature `(1, 3, 31)` on the full 35-dim tangent at $\rho_*$, with the (1, 3) Lorentzian sub-bundle on V's 4-dim block; eigenvalues $\pm 2$ at machine floor in the orthonormal V-basis). No new compute is consumed by audit π; the existing §13.2B numerical run is the load-bearing artifact.

---

## 3. The comparison — three predicates

### 3.1 Predicate 1: same diffeomorphism class

The DeWitt supermetric on $(\Omega, \beta_+, \beta_-, \phi)$ at the reference point $\Omega = 0$ is the Minkowski metric on $\mathbb R^4$. The V-Lorentzian Bures-Hessian on $(H, P_1, P_2, P_3) \cong \mathbb R^4$ is a constant-coefficient flat Lorentzian metric on $\mathbb R^4$.

Both are flat 4-dim Lorentzian manifolds of signature $(1, 3)$. The diffeomorphism class is **$\mathbb R^4$ with the standard differentiable structure**. **Match: [P]**.

The local invariants confirm flatness:
- Ricci scalar $R(g)$: zero on both sides at the reference point (constant-coefficient metric).
- Kretschmann scalar $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$: zero on both sides at the reference point.

### 3.2 Predicate 2: metric isometry up to overall scale

The two metrics at the reference point:

| | DeWitt at $\Omega = 0$ | V-Lorentzian at $\rho_*$ |
|---|---|---|
| Coordinate basis | $(\Omega, \beta_+, \beta_-, \phi)$ | $(H, P_1, P_2, P_3)$ |
| Signature | $(1, 3)$, $(-, +, +, +)$ | $(1, 3)$, $(+, -, -, -)$ |
| Matrix | $\mathrm{diag}(-1, +1, +1, +1)$ | $2 \cdot \mathrm{diag}(+1, -1, -1, -1)$ |

These are isometric as flat Lorentzian inner-product spaces on $\mathbb R^4$:

- **Sign convention.** Replace the timelike direction $\Omega \mapsto -\Omega$ (or equivalently $H \mapsto -H$); the signature convention $(-, +, +, +)$ vs $(+, -, -, -)$ is purely conventional in the mathematical-physics literature (Hartle–Hawking 1983 uses $(-, +, +, +)$ for the cosmological context; the categorical-simplex program uses $(+, -, -, -)$ following the [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md) Casimir form $\langle H \rangle^2 - \sum \langle P_a \rangle^2$). The two are related by an obvious isomorphism.
- **Scale.** The overall factor of 2 in the V-Lorentzian Hessian (from differentiating the quadratic squared-operator form twice) versus 1 in the DeWitt supermetric (at $\Omega = 0$, with the Newton-constant choice that absorbs the normalization). The metrics agree **up to overall constant scale**.

Explicit isometry map $(H, P_1, P_2, P_3) \to (-\Omega, \beta_+, \beta_-, \phi)$ with scale $\sqrt{2}$:

$$
\Psi : (x_H, x_1, x_2, x_3) \mapsto \tfrac{1}{\sqrt{2}} \cdot (-x_H, x_1, x_2, x_3).
$$

Under $\Psi$:

$$
G^{\mathrm{DeWitt}}\bigl(\Psi(X), \Psi(Y)\bigr) = \tfrac{1}{2} \cdot \mathrm{diag}(-1, +1, +1, +1)(X', Y') = \tfrac{1}{2} \cdot \mathrm{Hess}(I_V)(X, Y),
$$

so $\mathrm{Hess}(I_V) = 2 \cdot \Psi^* G^{\mathrm{DeWitt}}$, an isometry up to overall scale 2. **Match: [P]** at the tangent-quadratic-form level.

### 3.3 Predicate 3: extension beyond the reference point

Here the audit's joint-on-disjoint sub-finding emerges.

The **DeWitt supermetric** is defined on the **full minisuperspace manifold** $(\Omega, \beta_+, \beta_-, \phi)$. At $\Omega \neq 0$ the conformal factor $\mathrm{e}^{3\Omega}$ takes nontrivial values, introducing curvature: the metric is conformally flat (Weyl tensor vanishes) but the Ricci tensor is nonzero (computable from the $\Omega$-derivatives of the conformal factor). The DeWitt supermetric is a **curved manifold-level structure**, flat only at the reference point $\Omega = 0$.

The **V-Lorentzian sub-bundle**, as currently defined by [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md), is the *Hessian of $I_{\mathrm{complex}}$ at the single point $\rho_*$*. It is a quadratic form on the tangent space $T_{\rho_*} \mathcal{D}^\circ(\mathbb C^6)$ — a tangent-space-at-a-point structure, not a manifold structure. There is no "V-Lorentzian metric at $\rho \neq \rho_*$" defined by [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md).

To extend the V-Lorentzian sub-bundle to a 4-dimensional sub-manifold of $\mathcal{D}^\circ(\mathbb C^6)$ with a well-defined off-$\rho_*$ metric requires structural additions not present in the program:

1. **A V-foliation prescription.** Choose a 4-dimensional sub-manifold $\Sigma_V \subset \mathcal{D}^\circ(\mathbb C^6)$ tangent to V at $\rho_*$ and extended via some prescription (e.g., the integral surface of the V-supported left-invariant vector fields under the $\mathrm U(6)$ action, or the geodesic exponential map of the Bures metric restricted to V). The Bures metric on $\mathcal{D}^\circ$ restricts to a metric on $\Sigma_V$.

2. **A V-connection.** Equivalently, choose a Levi-Civita-like connection on V-tangent directions that allows parallel-transporting V's basis $(H, P_1, P_2, P_3)$ away from $\rho_*$. The induced metric on V-orbits then defines a manifold-level analog of the V-Lorentzian sub-bundle.

Either choice is a substantive structural addition not in [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md) or any v0.1–v0.4 paper. The natural V-foliation candidate is the $\mathrm{SU}(6)$-orbit of $\rho_*$ restricted to V-tangent directions, but its explicit form requires a derivation.

**Match: [A] partial.** The manifold-level extension is structurally meaningful, conceptually clean, but not yet executed. The DeWitt supermetric's $\mathrm{e}^{3\Omega}$ conformal factor is the explicit object the extension must reproduce; whether the categorical-simplex program's V-foliation does reproduce it is the question audit π′ would settle.

---

## 4. The three-outcome adjudication

| Pre-claimed branch (Paper 46 §8.7) | Outcome | Locus |
|---|:---:|---|
| **K-branch** (literal manifold match + isometry up to scale) | **Realized at tangent-quadratic-form level** | Predicate 1 (diffeomorphism: both flat $\mathbb R^4$) + Predicate 2 (isometry up to scale 2 and sign convention) |
| **L-branch** (manifolds don't match or metrics don't match) | **Did not fire** | Bianchi I + scalar field provides a literal isometric tangent match; alternative anchors (LQC, CDT, topos-theoretic QG) not needed at this tier |
| **Joint-on-disjoint** (partial match) | **Realized at manifold-level extension tier** | Predicate 3: DeWitt is a curved manifold-level structure (conformally flat with nonzero Ricci off $\Omega = 0$); V-Lorentzian is currently a Hessian at $\rho_*$ only; the off-reference-point comparison requires a V-foliation choice (queued as audit π′) |

**Realized branch: joint-on-disjoint.** The K-tangent identification is unambiguous and structurally significant; the manifold-level extension is the audit's queued sub-finding.

This is the **sixth named joint-on-disjoint outcome** of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule (joining audits θ at exponent, ι at corrections, β at row-3 dimensional generalization, χ at V/W/M trichotomy, ν at abstract-vs-literal natural-transformation levels).

The pattern of joint-on-disjoint sub-findings emerging from the program's external-correspondence audits is itself worth recording: in each case, the binary K/L pre-claim was insufficient to capture the structural reality, and the three-outcome rule's third branch captured the partial-match locus. Audit π's manifold-level extension is the cosmology-side analog of audit β's row-3 dimensional generalization — both are "partial matches with a substantive open sub-audit."

---

## 5. Implications for the cosmological-claim lift tiers

Per [Paper 46 §8.7](46_hartle_hawking_signature.md)'s tier framework (also restated in the chat-level discussion of "what would it take to lift the physical claim"):

- **Tier 0 → Tier 1 partial.** The cosmological correspondence has a *literal isometric mathematical-identification* at the tangent-quadratic-form-at-reference-point level. The V-Lorentzian sub-bundle at $\rho_*$ IS the Bianchi I + scalar field minisuperspace tangent at $\Omega = 0$, up to sign convention and scale factor 2. The correspondence is no longer purely "shape-match" with Hartle–Hawking — it is a literal isometric identification of one specific peer-reviewed minisuperspace model's tangent space.

- **Tier 1 full pending.** The manifold-level extension requires audit π′ (choose V-foliation and compare off-reference-point metric to the DeWitt $\mathrm{e}^{3\Omega}$-conformally-flat supermetric). This is a substantive open question, not a forced consequence of audit π.

- **Tier 2 not addressed.** The §11.2 dimensional firewall is NOT lifted by audit π. The overall scale factor 2 between DeWitt and V-Lorentzian remains a dimensionless ratio at this audit; lifting §11.2 at the scale ratio would be a separate audit (Tier-2), requiring audit π′'s K-branch as its precondition.

- **Tier 3 not addressed.** External peer-reviewed mathematical-physics replication remains the open §6.4 question of [Paper 35](35_grounded_paranoid_delusional_methodology.md).

- **Tier 4 not addressed.** Physical-mechanism claim ("the universe IS the Bures lift of $\mathbb Z/6\mathbb Z$") remains forbidden by [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) emergent-anything positioning.

**The cosmological *correspondence* is promoted; the cosmological *claim itself* is not.** Audit π establishes that the V-Lorentzian sub-bundle has a literal peer-reviewed mathematical-physics realization at the tangent level. It does not establish that physical spacetime *is* this realization. The latter remains [C, reduced] correspondence-language pending Tier-2 + Tier-3 + Tier-4 work that is far outside audit π's scope.

---

## 6. Discipline check ([Paper 35](35_grounded_paranoid_delusional_methodology.md) §3 honored)

- **Anchored objects (§3.3).** Every minisuperspace object cited (Bianchi I metric, Misner variables, DeWitt supermetric, Wheeler–DeWitt equation, scalar field action) anchored against peer-reviewed sources (Hartle–Hawking 1983; DeWitt 1967; Misner 1969; Halliwell 1989; Kiefer 2012). Every program object (V-Lorentzian sub-bundle, dispersion Casimir, $\rho_*$, $H$, $P_a$, V/M decomposition) anchored against [Paper 32 §6.2](32_one_functional_four_forces_v0.2%20(2).md), [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md), [Paper 46 §2.3](46_hartle_hawking_signature.md), at [P] tier.

- **Deterministic, exact, reproducible (§3.4).** Pure-mathematics derivation; closed-form Hessian computation; standard minisuperspace Lagrangian reduction. Reference numerical anchor in [`empirical/paper32_13_2B_fourth_order_casimir_audit.py`](empirical/paper32_13_2B_fourth_order_casimir_audit.py). No new compute consumed.

- **No upward tier-crossing (§3.5).** The audit promotes the *Lie-algebra-tier* (audit β) settled structural identification to a *tangent-quadratic-form-tier* literal isometric identification on row 2 of the [Paper 46 §4.2](46_hartle_hawking_signature.md) dictionary table. The cosmological *claim itself* (Tier 2 / Tier 3 / Tier 4 in the lift framework) is NOT promoted — it remains [C, reduced] per [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) emergent-anything positioning and the §4.3 discipline-rail framework of Paper 46.

- **Three-outcome matched-pair (§3.1 + [v2insert-04](v2insert-04.md) §3.1).** K/L/joint-on-disjoint pre-claimed in §0. Realized branch is joint-on-disjoint; the joint-on-disjoint locus identified as the *manifold-level extension* (sub-finding analogous to audit β's row-3 dimensional generalization).

- **Failures-first-class (§3.6).** The manifold-level extension's incompleteness is recorded explicitly as a queued sub-audit (audit π′), not absorbed into the K-branch or relabeled as an L-branch refutation. The sub-audit is named with a specific structural prescription (choose V-foliation or V-connection) so it is concretely actionable.

- **Dimensional firewall ([Paper 32 §11.2](32_one_functional_four_forces_v0.2%20(2).md)).** No physical constants. No Newton's $G$, no Planck length, no $\hbar$, no $c$, no Hubble constant, no Bekenstein–Hawking temperature. The "scale factor 2" between DeWitt and V-Lorentzian is a dimensionless ratio reported as such; lifting §11.2 at this ratio would be a separate Tier-2 audit not in audit π's scope.

- **Carried-label discipline ([Paper 32 §11.4](32_one_functional_four_forces_v0.2%20(2).md)).** The labels *minisuperspace*, *Wheeler–DeWitt equation*, *DeWitt supermetric*, *Misner variables*, *Bianchi I*, *scalar field*, *Hartle–Hawking minisuperspace* are anchored to peer-reviewed sources (Hartle–Hawking 1983, DeWitt 1967, Misner 1969, Halliwell 1989, Kiefer 2012) before each use. The label *V-foliation* is internal program language and is defined once here for the audit π′ specification; it is not re-used elsewhere without re-anchoring.

---

## 7. Implications for Paper 46 and Paper 49 (manuscript-edit absorption)

Per the [Paper 46 §8.7](46_hartle_hawking_signature.md) settlement protocol:

1. **§8.7 update — mark settled.** Replace the audit-π-open spec with audit-π-settled summary; reference this settlement file.

2. **§4.2 row 2 augmentation.** The Lie-algebra match column ([P]-spirit at the Lie-algebra tier from audit β) augmented with the tangent-isometry match ([P] at the tangent-quadratic-form tier from audit π); the manifold-level extension is recorded at [A] (queued audit π′).

3. **§4.4 audit β settlement — note strengthened C2 tier.** Audit β established [P]-spirit Lie-algebra match on row 2; audit π strengthens this to [P] tangent-isometry match (literal isometric inner-product spaces on $\mathbb R^4$).

4. **§5.1 — augment with minisuperspace anchor entry on `ℤ/6`.** The five-row primorial-ladder table now carries an "audited minisuperspace anchor" entry for `ℤ/6`: Halliwell-style Bianchi I + massless scalar field. Higher rows (`ℤ/30`, `ℤ/210`, etc.) are queued — their V-Lorentzian sub-bundle dimensions are $1 + n_P$ (one $H$ direction + $n_P = \pi(\sqrt{N})$ single-prime $P_a$ directions per row); identifying a peer-reviewed minisuperspace model with matching dimension at each row is a separate question and is queued as audit π′′ alongside audit π′.

5. **§8.7 carry-forward — add audit π′ to the open-audit list.** "Manifold-level extension of audit π: choose V-foliation of $\mathcal{D}^\circ(\mathbb C^6)$ and check off-reference-point metric agreement with the DeWitt $\mathrm{e}^{3\Omega}$-conformally-flat supermetric."

6. **Reproducibility artifacts — add this settlement record.**

For [Paper 49 §4.1](49_arithmetic_decoupling_of_projection_closure_overflows.md) (cosmology manifestation):

7. **Lift-candidate path paragraph update.** Replace the "audit π specified, not yet executed" with "audit π settled at K-tangent + joint-on-disjoint-at-manifold; cosmological correspondence promoted to [A] partial at the tangent-quadratic-form tier."

---

## 8. The six joint-on-disjoint outcomes — pattern observation

Audit π becomes the sixth named joint-on-disjoint outcome of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule:

1. **Audit θ** at exponent (super-exponential in $n$, not log-linear).
2. **Audit ι** at corrections (polynomial-log prefactor, finite-arithmetic-specific).
3. **Audit β** at row 3 (dimensional generalization of HH's imaginary time to $\dim_M$-dim Wick-rotation locus).
4. **Audit χ** at tangent trichotomy (W-Euclidean and M-Euclidean overlap on `ℤ/12`).
5. **Audit ν** at abstract-vs-literal natural-transformation levels.
6. **Audit π** at tangent-vs-manifold (this audit) — K at flat-tangent identification, joint-on-disjoint at manifold-level extension (queued as audit π′).

The pattern: each external-correspondence audit's binary K/L pre-claim has been insufficient to capture a structural sub-finding that the three-outcome rule's third branch makes visible. Per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §4 / [v2insert-04](v2insert-04.md) §4 method-improvement events, this is consistent with the methodology improving itself under empirical pressure — the wrong-shape-of-question failure (§6.5 of Paper 35) is now a recurring structural sub-finding across the cosmology audit arc, validating the [v2insert-04](v2insert-04.md) §3.1 extension's value.

Per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §7 (no self-promotional claims), the pattern's significance is not asserted here as a methodological discovery; it is recorded as a worked observation. Whether the joint-on-disjoint pattern is itself a structural feature of external-correspondence audits or an artifact of the binary K/L framing's expressive insufficiency is the kind of meta-question the methodology paper's §6.4 open empirical-replication question is calibrated to defer.

---

## 9. Discipline closing note

This settlement is the **first** pure-mathematics row-generalization audit at the **tangent-isometry tier** in the program's external-correspondence layer. Audit β established Lie-algebra-of-Wick-rotation structural identification; audit π extends this to literal isometric identification at the tangent-quadratic-form level. The combined audit-β + audit-π settlement is, by tier, the cleanest structural-mathematics claim the cosmological correspondence has had since the §13.2B audit triad established the hybrid signature on `D(ℂ⁶)`.

Three discipline rails are recorded as observed:

(a) **The audit promotes the correspondence tier, not the cosmological claim.** Per [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) emergent-anything positioning, what audit π establishes is a *literal isometric mathematical identification* between two 4-dim flat Lorentzian inner-product spaces on $\mathbb R^4$ — the V-Lorentzian sub-bundle at $\rho_*$ and the Bianchi I + scalar field minisuperspace tangent at $\Omega = 0$. The cosmological *claim* (Tier 2 forced dimensional prediction; Tier 3 external replication; Tier 4 physical-mechanism) is not promoted.

(b) **The joint-on-disjoint sub-finding is the load-bearing positive content of the audit.** The K-branch alone would not have revealed that the manifold-level extension is a substantive open question; the three-outcome rule's third branch surfaced it as audit π′. Audit π′ is now the sharpest Tier-1-completion candidate available in the program's external-correspondence layer.

(c) **The dimensional firewall is honored throughout.** All quantities are dimensionless: signatures $(1, 3)$, integer eigenvalues $\pm 1, \pm 2$, the dimensionless ratio "scale factor 2." No Planck-scale identification, no $G$, no $\hbar$, no $c$. §11.2 binding.

The grounded-paranoid-delusional grammar, once more: delusion proposed that the V-Lorentzian sub-bundle on $\mathcal{D}^\circ(\mathbb C^6)$ is *literally* a peer-reviewed minisuperspace truncation of GR; paranoia bounded this with three-outcome matched-pair pre-claim under [v2insert-04](v2insert-04.md) §3.1; grounded executed the row-by-row metric check and recorded **K at tangent-quadratic-form level + joint-on-disjoint at manifold-level extension**. The realized outcome is structurally substantive — the cosmological correspondence is no longer a Lie-algebra match (audit β) but a tangent-level isometric identification (audit π) — while honestly recording the manifold-level extension's incompleteness as the queued audit π′.

---

*End audit π settlement. Status: settled, joint-on-disjoint. Cosmological correspondence on [Paper 46 §4.2](46_hartle_hawking_signature.md) row 2 promoted from [P]-spirit at the Lie-algebra tier (audit β) to [P] at the tangent-quadratic-form tier (audit π) — literal isometric inner-product spaces on $\mathbb R^4$; manifold-level extension queued as audit π′. No new compute consumed; pure-mathematics check anchored at [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md) [P] numerical run and Halliwell 1989 / Kiefer 2012 / DeWitt 1967 minisuperspace literature. Manuscript-edit absorption proposed for [Paper 46 §8.7](46_hartle_hawking_signature.md) (mark settled), §4.2 row 2 (add tangent-isometry status), §4.4 (note strengthened C2 tier), §5.1 (minisuperspace anchor entry on `ℤ/6`); for [Paper 49 §4.1](49_arithmetic_decoupling_of_projection_closure_overflows.md) (lift-candidate paragraph updated to settled). Sixth named joint-on-disjoint outcome of the program; audit π′ (manifold-level extension via V-foliation choice) opens as the next concrete Tier-1-completion audit.*
