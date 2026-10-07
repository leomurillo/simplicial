# Audit π′′′ Settlement — Alternative-Anchor Candidate-Survey for Globally-Flat Lorentzian Configuration Space

**Audit anchor:** [Paper 46 §8.8](46_hartle_hawking_signature.md) (specified 2026-05-21). Alternative-anchor candidate-survey for the V-Lorentzian sub-bundle's manifold-level structure, opened by audit π′ ([`audit_pi_prime_v_foliation_manifold_extension_settlement.md`](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md)) after the Halliwell-Bianchi-I manifold-level anchor was foreclosed. Question: does any peer-reviewed mathematical-physics framework with globally-flat Lorentzian (1, 3) configuration space match the V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}} \subset \mathcal D^\circ(\mathbb C^6)$ at the manifold level?

**Status:** **SETTLED — joint-on-disjoint** under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule. **L-branch realized on every peer-reviewed cosmological-minisuperspace and alternative-Lorentzian-configuration-space candidate**: none has the 4-dim globally-flat Lorentzian (1, 3) configuration space with Hilbert-space-spectral-positivity boundary structure of $\Sigma_V^{\mathrm{aff}}$. **K-branch realized on a structural sub-observation that is informative but trivial**: the V-Lorentzian sub-bundle's globally-flat manifold-level structure is *Minkowski-as-Lorentzian-manifold* by the uniqueness of 4-dim globally-flat Lorentzian manifolds up to isometry; but this identification is *tautological* (every globally-flat 4-dim Lorentzian manifold IS Minkowski) and does not promote the cosmological correspondence to a substantive Tier-1.75 mathematical identification with a peer-reviewed cosmological-minisuperspace framework.

**Lift-chain consequence:** **Tier 1.75 ([A] mathematical-identification at manifold-level via alternative-anchor) is foreclosed.** The lift chain is now sharply bounded: Tier 0 [C, reduced] → Tier 1 [P]-tangent-isometry (audit π) → Tier 1.5 [P]-globally-flat-Minkowski-structural-finding (audit π′ K-on-different-question) → **Tier 1.75 closed (audit π′′′ L on every candidate)**. The cosmological correspondence cannot promote beyond [P]-tangent-isometry at the peer-reviewed-mathematical-physics-framework-identification question; the manifold-level structure of $\Sigma_V^{\mathrm{aff}}$ is internal to the categorical-simplex program and lacks a literal peer-reviewed name.

**Method:** pure mathematics + literature-survey. No compute.

**Prepared:** 2026-05-21 · Author: Leonardo Murillo Montero (team Leo)

---

## 0. The pre-claimed three-outcome branches (from Paper 46 §8.8)

Per [v2insert-04](v2insert-04.md) §3.1:

- **K-branch.** A specific peer-reviewed mathematical-physics framework matches the V-affine V-sub-manifold at the manifold level. Cosmological correspondence promotes to [A] partial mathematical identification under that anchor; the lift chain reaches Tier 1.75.

- **L-branch.** No peer-reviewed mathematical-physics framework matches. V-Lorentzian sub-bundle's manifold-level structure is *internal* to the program; lift chain stops at Tier 1.5.

- **Joint-on-disjoint.** Partial match — some candidate has signature + dim correct but boundary structure wrong, or vice versa; the partial-match locus is characterized.

**Realized branch:** **joint-on-disjoint at the framework-substantivity tier.** L on every candidate's substantive identification; K-trivial on the Minkowski-as-flat-Lorentzian-manifold tautology; the joint-on-disjoint locus is the *gap between the program's specific structural object (bounded-convex Minkowski region with spectral-positivity boundary) and any peer-reviewed cosmological-or-foundational mathematical-physics framework*.

---

## 1. The V-affine V-sub-manifold's specific structure

From [audit π′ settlement §2](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md), the V-affine prescription gives

$$
\Sigma_V^{\mathrm{aff}} = \bigl\{ \rho_* + X : X \in V, \ \rho_* + X \succ 0,\ \mathrm{tr}(\rho_* + X) = 1 \bigr\} \subset \mathcal D^\circ(\mathbb C^6),
$$

where $V = \mathrm{span}_{\mathbb R}\{H, P_1, P_2, P_3\}$ is the 4-dim V-supported orthonormal Hermitian basis ([Paper 32 §6.2](32_one_functional_four_forces_v0.2%20(2).md) [P]). The trace constraint is automatic since $V \subset \mathrm{Herm}_0$. The positivity constraint cuts out a bounded open subset of $V$:

$$
\Sigma_V^{\mathrm{aff}} \cong \bigl\{ X \in V : \lambda_{\min}(\rho_* + X) > 0 \bigr\} = \bigl\{ X \in V \cong \mathbb R^4 : \lambda_{\min}(I_6/6 + X) > 0 \bigr\}.
$$

This is a **convex open subset of $\mathbb R^4$** (positivity is preserved under convex combinations of Hermitian matrices); the boundary is the locus $\{\lambda_{\min}(I_6/6 + X) = 0\}$, a piecewise-algebraic hypersurface in $\mathbb R^4$ determined by the smallest eigenvalue of $\rho_* + X$ vanishing.

Equipped with the V-Lorentzian Hessian-of-$I_V$ metric ([audit π′ §2.3](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md)), $\Sigma_V^{\mathrm{aff}}$ is a **bounded convex subset of $\mathbb R^4$ with constant Lorentzian (1, 3) metric and Hilbert-space-spectral-positivity boundary**.

The audit's question: does any peer-reviewed mathematical-physics framework's configuration space have this specific structural profile?

---

## 2. The candidate-by-candidate survey

### 2.1 Free massless scalar field on Minkowski background

**Framework.** Configuration space = field configurations $\phi: \mathbb R^{1, 3} \to \mathbb R$ with kinetic action $\frac{1}{2}\int (\partial_\mu \phi)(\partial^\mu \phi) \mathrm d^4 x$. Standard reference: any QFT textbook (Peskin–Schroeder; Weinberg, *Quantum Theory of Fields* vol. 1, Ch. 7).

**Signature check.** The natural inner product on field perturbations $\delta \phi$ at a fixed $\phi$ is the $L^2$ inner product $\int (\delta\phi)^2 \mathrm d^4 x$, *positive-definite*. The Lorentzian signature on the background spacetime $\mathbb R^{1, 3}$ does *not* transfer to a Lorentzian inner product on configuration space; it transfers to the *equations of motion* (wave equation), not the metric on field space. **Wrong signature: Euclidean (∞, 0), not Lorentzian (1, 3).**

**Dimension check.** Configuration space is infinite-dimensional. Mode-truncation to a 4-mode subspace gives 4-dim, but the truncation is artificial and does not change the wrong-signature problem (each mode has positive-definite kinetic energy).

**Boundary check.** Free-scalar-field configuration space has no natural finite boundary (the wave equation admits unbounded field configurations). No spectral-positivity-boundary analog.

**Verdict: L on all three checks.** Free scalar field on Minkowski has Riemannian (Euclidean) infinite-dim configuration space with no natural boundary — three structural mismatches with the V-affine sub-manifold.

### 2.2 de Sitter-limit truncation of Bianchi I

**Framework.** The Halliwell-Bianchi-I + scalar field minisuperspace with the limit $\Omega \to \infty$ (large spatial volume, de Sitter-like expansion). Standard reference: Halliwell 1989; Kiefer 2012 Ch. 8 §8.3.

**Signature check.** Throughout the $\Omega \to \infty$ limit, the supermetric $G^{\mathrm{DeWitt}}(\Omega) = e^{3\Omega} \cdot \mathrm{diag}(-1, +1, +1, +1)$ retains signature $(1, 3)$ — the prefactor $e^{3\Omega}$ rescales but does not change signature. **Signature OK.**

**Globally-flat check.** The conformal factor $e^{3\Omega}$ blows up as $\Omega \to \infty$; the metric is *not* asymptotically constant. The Ricci tensor remains non-zero throughout the limit (per [audit π′ §3.2](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md)). **Not globally flat.**

**Alternative: constant-$\Omega$ slice.** Restricting to $\Omega = \Omega_0 = \mathrm{const}$ gives a 3-dim sub-slice with metric $e^{3\Omega_0} \cdot \mathrm{diag}(+1, +1, +1)$ — *Euclidean* (positive-definite). The Lorentzian signature is lost because $\Omega$ was the timelike direction. **Wrong signature + wrong dim.**

**Verdict: L.** No $\Omega \to \infty$ or constant-$\Omega$ limit of Halliwell-Bianchi-I produces a 4-dim globally-flat Lorentzian configuration space.

### 2.3 Topos-theoretic flat-Lorentzian quantum gravity

**Framework.** Doering & Isham 2008, *A Topos Foundation for Theories of Physics* (J. Math. Phys. 49). The state space and the configuration space are replaced by objects in a topos $\tau$; "configurations" are points in topos $\tau$, not points in a smooth manifold.

**Manifold check.** The framework explicitly replaces the smooth-manifold configuration space with a *topos object* — neither a 4-dim Riemannian manifold nor a Lorentzian one. Identifying the V-affine sub-manifold $\Sigma_V^{\mathrm{aff}}$ (a literal 4-dim smooth manifold with Lorentzian metric) with a topos object would require a *forgetful functor* discarding the smooth-manifold structure. **Wrong category: topos vs smooth-manifold.**

**Internal-locale check.** Some topoi admit *internal locales* with Riemannian or Lorentzian-like structures; in principle, an internal locale could host a globally-flat Lorentzian (1, 3) structure. This is structurally possible but is *not* the literal "globally-flat Lorentzian configuration manifold" the candidate-survey is asking about. The match would be metaphorical, not literal.

**Verdict: L on the literal-Lorentzian-manifold question.** Topos-theoretic QG does not provide a concrete 4-dim Lorentzian-manifold configuration space; matching with the program's V-affine sub-manifold would require category-level translation that defeats the comparison.

### 2.4 Causal set theory continuum limits

**Framework.** Bombelli, Lee, Meyer, Sorkin 1987, *Spacetime as a causal set* (Phys. Rev. Lett. 59); modern review Sorkin 2003. Configuration space = the space of causal sets (locally finite partially ordered sets); dynamics is the sum-over-causal-sets.

**Configuration-space-vs-target-spacetime check.** The configuration space of causal-set QG is the space of *causal sets*, a discrete combinatorial object. The *target spacetime* in the continuum limit is a Lorentzian manifold — Minkowski for the random Lorentz-invariant sprinkling, more general spacetimes for other prescriptions. The two are at *different conceptual levels*: the configuration space is the variation space; the target spacetime is the emergent geometry.

**Identification with V-affine sub-manifold.** $\Sigma_V^{\mathrm{aff}}$ is a literal 4-dim Lorentzian manifold (in V-affine coordinates with constant Lorentzian metric). It is NOT a space of causal sets. The structural identification with causal-set theory would have to be at the *target-spacetime* level (V-affine sub-manifold ≅ continuum-limit Minkowski region from a specific causal-set sprinkling), not at the *configuration-space* level.

At the target-spacetime level, the V-affine sub-manifold is a bounded convex region of Minkowski — and continuum-limit causal sets of bounded regions of Minkowski exist (e.g., sprinkling into a finite causal diamond). But this is again a *trivial* identification (any bounded convex Minkowski region is a possible continuum-limit target), not a substantive structural match.

**Verdict: L on the literal-configuration-space identification.** At the target-spacetime level a trivial K is available but not substantive (causal-set theory's continuum-limit target is Minkowski generically, which matches anything Minkowski-like).

### 2.5 Symplectic-reduction Lorentzian phase spaces

**Framework.** Hamiltonian formulation of GR + matter with constraint structure; symplectic reduction by constraints gives reduced phase spaces of various dimensions. Standard reference: Henneaux–Teitelboim, *Quantization of Gauge Systems* (1992); Kuchar's parameterized dynamics literature.

**Linearized-GR sub-candidate.** Linearized GR around Minkowski has configuration space = the space of metric perturbations $h_{\mu\nu}$ on flat background. After diffeomorphism gauge-fixing and constraint reduction, the physical configuration space is the space of two transverse-traceless polarizations × infinite Fourier modes. *Infinite-dimensional.* A 4-mode truncation gives 4-dim, but the truncation is artificial.

**Signature of linearized configuration space.** The kinetic term in the linearized Einstein–Hilbert action is quadratic in $\dot{h}_{\mu\nu}$. The natural inner product on metric perturbations (the *DeWitt supermetric of linearized GR*) is *Lorentzian* (similar to the nonlinear DeWitt, with one negative direction from the conformal mode and remaining positive directions from the trace-free perturbations). **Signature OK in principle for some truncations.**

**Globally-flat check.** Linearized GR's configuration space inherits its metric from the *quadratic-in-perturbation* part of the Einstein–Hilbert action. This metric is *constant* (the perturbation theory is quadratic by construction). For a 4-mode truncation, the configuration space IS globally-flat Lorentzian (1, 3) up to the truncation choice. **Globally-flat OK in principle for some truncations.**

**Boundary structure.** Linearized-GR configuration space has no natural finite boundary (perturbations $h_{\mu\nu}$ can take any real value). No spectral-positivity-boundary analog.

**Verdict: K on signature + globally-flat for some artificial 4-mode truncations; L on boundary structure (no Hilbert-spectral-positivity analog) and L on natural dimension (infinite-dim native). The K-component is fragile (artificial truncation) and does not match the spectral-positivity-bounded V-affine sub-manifold.**

### 2.6 Single-particle relativistic dynamics

**Framework.** Configuration space of a relativistic point particle on Minkowski: position $x^\mu \in \mathbb R^{1, 3}$. Standard reference: any classical mechanics textbook treating relativistic particle (Goldstein, *Classical Mechanics*).

**Dim + signature + globally-flat check.** Configuration space IS literally Minkowski $\mathbb R^{1, 3}$ — 4-dim, signature $(1, 3)$, globally flat. **All three OK.**

**Boundary check.** No natural finite boundary (a particle's position can take any value in Minkowski). **L on boundary structure.**

**Substantivity check.** "Particle on Minkowski has Minkowski as configuration space" is a *tautology* (the particle moves in spacetime, so its configuration is spacetime-valued). The identification is degenerate: it does not say anything specific about the program's V-affine sub-manifold beyond "V-affine is Minkowski-like."

**Verdict: K-trivial on configuration-space-=-Minkowski; L on boundary structure and substantivity.** This candidate is the closest match at the manifold level *trivially*, but offers no substantive structural identification beyond "Minkowski = unique 4-dim globally-flat Lorentzian manifold."

### 2.7 Algebraic QFT bounded regions (Reeh–Schlieder, Bisognano–Wichmann)

**Framework.** Haag–Kastler nets of algebras on bounded regions of Minkowski; Reeh–Schlieder spaces; modular automorphisms of bounded regions (Bisognano–Wichmann theorem). Standard reference: Haag, *Local Quantum Physics* (1992).

**Region-shape check.** AQFT's bounded regions are typically *causal diamonds* (the intersection of forward and backward light cones from two endpoints) or *wedge regions* (one-sided complement of a causal diamond). The boundary of a causal diamond is *light-cone-determined* — null hypersurfaces. The boundary of the V-affine sub-manifold $\Sigma_V^{\mathrm{aff}}$ is *spectral-positivity-determined* — a piecewise-algebraic hypersurface in $V$ defined by the smallest eigenvalue of $\rho_* + X$ vanishing. **Boundary shape mismatch: light-cone vs spectral-positivity.**

**Lorentzian metric check.** Both AQFT regions and $\Sigma_V^{\mathrm{aff}}$ carry the (constant) Lorentzian metric of their ambient Minkowski. **Match.**

**Verdict: L on boundary structure (light-cone vs spectral-positivity); K on Lorentzian-metric structure.** The mismatch is the boundary; the V-affine sub-manifold is not a causal-diamond AQFT region.

### 2.8 AdS/CFT-related flat Lorentzian regions

**Framework.** Maldacena 1997 et seq.; the Poincaré patch of $\mathrm{AdS}_{d+1}$, certain near-horizon geometries of black branes, and flat-limit AdS truncations. Standard reference: Aharony, Gubser, Maldacena, Ooguri, Oz, *Large N field theories, string theory and gravity* (Phys. Rep. 323).

**Globally-flat check.** AdS$_{d+1}$ has constant negative curvature, *not* globally flat. The flat limit (radius → ∞) gives Minkowski, but this is a degenerate limit. No truncation of AdS gives a globally-flat 4-dim Lorentzian configuration with spectral-positivity boundary.

**Verdict: L.** AdS-based frameworks are constant-negative-curvature, not globally flat.

---

## 3. Summary table of the candidate survey

| Candidate | Sig | Dim | Globally flat | Boundary | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|
| Free scalar on Minkowski | ✗ Euclidean | ✗ ∞ | ✓ | ✗ none | **L** |
| de Sitter Bianchi I | ✓ (1, 3) | ✓ 4 | ✗ conformal | ✗ none | **L** |
| Topos-theoretic QG | ✗ not manifold | — | — | — | **L** |
| Causal sets continuum | ✗ not configuration-space | — | — | — | **L** |
| Linearized-GR 4-mode | ✓ (1, 3) artificial trunc | ✗ ∞ native | ✓ for trunc | ✗ none | **L (substantive)** |
| Single-particle on Minkowski | ✓ (1, 3) | ✓ 4 | ✓ | ✗ none | **K-trivial** (Minkowski = ambient) |
| AQFT causal diamond | ✓ (1, 3) | ✓ 4 | ✓ (in ambient) | ✗ light-cone | **L** (boundary mismatch) |
| AdS-related flat | — | — | ✗ AdS curvature | — | **L** |

**Aggregate: L on every substantive identification.** The only K-branch is the *trivial* identification of Minkowski-as-Lorentzian-manifold with the V-affine sub-manifold's ambient space — but this is a tautology by the uniqueness of 4-dim globally-flat Lorentzian manifolds up to isometry, and does not connect the V-affine sub-manifold's *specific* structure (bounded convex with spectral-positivity boundary) to any peer-reviewed cosmological or foundational mathematical-physics framework.

---

## 4. The three-outcome adjudication

| Pre-claimed branch (Paper 46 §8.8) | Outcome | Locus |
|---|:---:|---|
| **K-branch** at substantive peer-reviewed framework identification | **Did not fire** | Every candidate fails at one or more of signature / dim / globally-flat / boundary-structure checks |
| **L-branch** at "no peer-reviewed framework matches" | **Realized** | All 8 surveyed candidates return L on substantive identification |
| **Joint-on-disjoint** at framework-substantivity tier | **Realized** | A trivial K is available (Minkowski-as-ambient-spacetime, by uniqueness of 4-dim flat Lorentzian manifolds), but it is not substantive — it does not connect the V-affine sub-manifold's specific bounded-convex-with-spectral-positivity-boundary structure to any peer-reviewed cosmological or foundational framework |

**Realized branch: joint-on-disjoint at the framework-substantivity tier.** L on substantive identification; K-trivial on Minkowski-as-uniqueness-determined-ambient. The joint-on-disjoint locus is the *gap* between the program's specific 4-dim bounded-convex-Lorentzian-with-spectral-positivity-boundary structure and any peer-reviewed mathematical-physics framework's standard objects.

This is the **eighth named joint-on-disjoint outcome** of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule (joining audits θ at exponent, ι at corrections, β at row-3 dimensional generalization, χ at V/W/M trichotomy, ν at abstract-vs-literal natural-transformation levels, π at tangent-vs-manifold, and π′ at anchor-choice).

---

## 5. Lift-chain consequence

**Tier 1.75 ([A] mathematical-identification at manifold-level via alternative anchor) is foreclosed.**

The lift chain is now sharply bounded:

| Tier | Status after audit π′′′ | Anchor |
|---|---|---|
| Tier 0 [C, reduced] | Cosmological *claim itself* | Locked by §11.1 + §11.2 |
| Tier 1 [P]-tangent-isometry | Settled (audit π) | Halliwell-Bianchi-I + scalar field at $\Omega = 0$, up to sign + scale 2 |
| Tier 1.5 [P]-globally-flat-Minkowski-structural-finding | Settled (audit π′ K-on-different-question) | V-affine V-sub-manifold is globally flat $\mathbb R^{1, 3}$, $\mathrm{Hess}(I_V)$ constant on $\mathcal D^\circ$ |
| **Tier 1.75 [A]-manifold-level identification on alternative anchor** | **FORECLOSED (audit π′′′)** | No peer-reviewed mathematical-physics framework matches; only Minkowski-as-uniqueness-determined-ambient is available, which is trivial |
| Tier 2 dimensional-firewall lift | Locked, no precondition met | Required Tier 1.75 K-branch as precondition; precondition fails |
| Tier 3 external replication | Locked, independent of program | — |
| Tier 4 physical-mechanism claim | Locked by §11.1 | — |

**The cosmological correspondence cannot promote beyond [P]-tangent-isometry at the peer-reviewed-mathematical-physics-framework-identification question.** The V-affine sub-manifold's manifold-level structure is internal to the categorical-simplex program and lacks a literal peer-reviewed name. The cosmological *claim itself* remains at [C, reduced]; §11.2 firewall not lifted; Tier 2 / Tier 3 / Tier 4 unchanged.

---

## 6. The structural sub-finding — what $\Sigma_V^{\mathrm{aff}}$ actually is

Audit π′′′'s L-branch survey clarifies what the V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}}$ is *not*:

- *Not* a cosmological minisuperspace (Halliwell-Bianchi-I; audit π′ L).
- *Not* a free-field configuration space (audit π′′′ §2.1 L).
- *Not* a de-Sitter-limit (audit π′′′ §2.2 L).
- *Not* a topos-theoretic configuration object (audit π′′′ §2.3 L).
- *Not* a causal-set configuration space (audit π′′′ §2.4 L).
- *Not* a linearized-GR phase space (audit π′′′ §2.5 L on substantive).
- *Not* a relativistic-particle configuration space (audit π′′′ §2.6 K-trivial only).
- *Not* a causal-diamond AQFT region (audit π′′′ §2.7 L on boundary).
- *Not* an AdS-related flat region (audit π′′′ §2.8 L).

What audit π′′′ identifies *positively*: $\Sigma_V^{\mathrm{aff}}$ is a 4-dim **bounded convex subset of Minkowski** whose **boundary is determined by Hilbert-space spectral positivity** (the constraint $\lambda_{\min}(\rho_* + X) > 0$ on the smallest eigenvalue of $\rho_* + X$). This combination — flat Lorentzian + bounded convex + spectral-positivity boundary — is **novel** and **internal to the categorical-simplex program**.

This is structurally distinctive. The closest peer-reviewed cousins are:

- **AQFT causal diamonds** share the bounded-convex-Minkowski-region property but have *light-cone* boundaries (not spectral-positivity).
- **Algebraic-geometric semialgebraic regions** of $\mathbb R^4$ share the *piecewise-algebraic-boundary* property but don't typically carry an intrinsic Lorentzian metric.
- **Coadjoint orbits of $\mathrm U(6)$** share the *spectral-positivity-determined* property but are typically *Kähler* (positive-definite Riemannian + complex structure), not Lorentzian.

The intersection of all three properties — flat-Lorentzian + bounded-convex + spectral-positivity-boundary — does not appear to be a standard object in the peer-reviewed mathematical-physics literature. It is the categorical-simplex program's own structural object.

**This is the eighth joint-on-disjoint sub-finding's positive content**: $\Sigma_V^{\mathrm{aff}}$ is a *novel* 4-dim Lorentzian region whose specification involves three independent structural features that no peer-reviewed cosmological or foundational framework combines.

---

## 7. Discipline check ([Paper 35](35_grounded_paranoid_delusional_methodology.md) §3 honored)

- **Anchored objects (§3.3).** Every candidate framework anchored against peer-reviewed sources cited in §2 (Halliwell 1989; Kiefer 2012; Doering–Isham 2008; Bombelli–Lee–Meyer–Sorkin 1987; Sorkin 2003; Haag 1992; Maldacena 1997; Aharony et al. *Large N* 2000; Henneaux–Teitelboim 1992; Peskin–Schroeder; Weinberg vol. 1; Goldstein). Every program object anchored against [Paper 32 §6.2 + §13.2B](32_one_functional_four_forces_v0.2%20(2).md), [Paper 46](46_hartle_hawking_signature.md), [Audit π](empirical/reports/audit_pi_minisuperspace_identification_settlement.md), [Audit π′](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md), at [P] tier.

- **Deterministic, exact, reproducible (§3.4).** Pure-mathematics survey + literature anchor-checks. No new compute consumed.

- **No upward tier-crossing (§3.5).** The cosmological correspondence is *bounded* by audit π′′′ to [P]-tangent-isometry (audit π) + [P]-globally-flat-Minkowski-structural-finding (audit π′ K-on-different-question). The Tier-1.75 promotion path is *foreclosed*; no upward crossing to [A] manifold-level mathematical identification is licensed.

- **Three-outcome matched-pair (§3.1 + [v2insert-04](v2insert-04.md) §3.1).** K/L/joint-on-disjoint pre-claimed in §0; realized branch is joint-on-disjoint at the framework-substantivity tier. The L on every substantive candidate is honest; the K-trivial on Minkowski-as-uniqueness-determined-ambient is recorded as non-substantive.

- **Failures-first-class (§3.6).** Every candidate's L-verdict is recorded explicitly with the specific structural mismatch identified. The K-trivial Minkowski match is *not* re-labeled as a substantive K; the audit reports honestly that no substantive K-branch fires on any peer-reviewed framework.

- **Dimensional firewall ([Paper 32 §11.2](32_one_functional_four_forces_v0.2%20(2).md)).** No physical constants. No Planck length, no $G$, no $\hbar$, no $c$, no Hubble constant. All quantities are dimensionless structural tags: signature, dim, globally-flat, boundary shape.

- **Carried-label discipline ([Paper 32 §11.4](32_one_functional_four_forces_v0.2%20(2).md)).** Carried labels — *Minkowski*, *Bianchi I*, *de Sitter*, *Halliwell minisuperspace*, *Wheeler–DeWitt*, *topos*, *causal set*, *Reeh–Schlieder*, *Bisognano–Wichmann*, *AdS/CFT*, *AdS*, *AQFT*, *linearized GR*, *graviton*, *symplectic reduction*, *Kuchar parameterized dynamics*, *Henneaux–Teitelboim*, *Haag–Kastler net* — anchored against peer-reviewed sources per §3.3 above before each use.

---

## 8. Implications for Papers 46 and 49 (manuscript-edit absorption)

1. **[Paper 46 §8.8](46_hartle_hawking_signature.md) — mark audit π′′′ settled** at joint-on-disjoint at the framework-substantivity tier. The Tier-1.75 lift path is foreclosed. Reference this settlement file.

2. **[Paper 46 §4.2](46_hartle_hawking_signature.md) row 2 — augment with the foreclosure.** Add: "Audit π′′′ (2026-05-21) — alternative-anchor candidate-survey settled at joint-on-disjoint at the framework-substantivity tier. L on every peer-reviewed candidate's substantive identification; K-trivial only on Minkowski-as-uniqueness-determined-ambient. The Tier-1.75 mathematical-identification path is foreclosed; the cosmological correspondence is bounded to [P]-tangent-isometry (audit π) at the peer-reviewed-framework-identification question."

3. **[Paper 46 §4.4](46_hartle_hawking_signature.md) — add audit π′′′ summary** noting that the lift chain stops at [P]-tangent-isometry; no peer-reviewed mathematical-physics framework matches the V-affine V-sub-manifold's specific structure at the manifold level.

4. **[Paper 46 §5.1](46_hartle_hawking_signature.md) — note structural-internal-to-program reading.** $\Sigma_V^{\mathrm{aff}}$'s combination of (flat-Lorentzian) + (bounded-convex) + (spectral-positivity-boundary) is novel and internal to the categorical-simplex program; no peer-reviewed cosmological-minisuperspace or foundational framework has this combination.

5. **[Paper 46 §8](46_hartle_hawking_signature.md) carry-forward — close audit π′′′ as settled.** Update audit π′′′ section to reflect L-on-substantive realization; close the alternative-anchor candidate-survey thread.

6. **Add a new open-audit candidate** in [Paper 46 §8](46_hartle_hawking_signature.md): **audit π′′′′ — Tomita–Takesaki modular flow audit**. The categorical-simplex program's Bures-manifold $\mathcal D^\circ(\mathbb C^6)$ has natural Tomita–Takesaki modular automorphisms (the cyclic-and-separating vector structure of finite-dim quantum systems). Audit π′′′′ would ask whether the V-affine V-sub-manifold's spectral-positivity boundary is related to a Tomita–Takesaki modular flow of the V-supported algebra of observables. This is a substantive cross-program audit candidate but is *not* claimed to be a Tier-1.75 lift candidate — its purpose is to characterize the V-affine sub-manifold's internal structure further, not to lift the cosmological correspondence.

7. **Reproducibility artifacts — add this settlement record.**

8. **[Paper 49 §4.1](49_arithmetic_decoupling_of_projection_closure_overflows.md) lift-candidate paragraph — close the alternative-anchor branch.** Update to reflect that the cosmological correspondence's manifold-level extension is foreclosed at the peer-reviewed-framework-identification question; the V-Lorentzian sub-bundle's manifold-level structure is *internal* to the categorical-simplex program.

---

## 9. The eight joint-on-disjoint outcomes — pattern continuation

Audit π′′′ becomes the **eighth** named joint-on-disjoint outcome of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule:

1. **Audit θ** at exponent.
2. **Audit ι** at corrections.
3. **Audit β** at row 3 (dimensional generalization).
4. **Audit χ** at tangent trichotomy (V/W/M).
5. **Audit ν** at abstract-vs-literal natural-transformation.
6. **Audit π** at tangent-vs-manifold.
7. **Audit π′** at anchor-choice tier.
8. **Audit π′′′** at framework-substantivity tier (this audit) — L on every substantive candidate + K-trivial on Minkowski-uniqueness-ambient.

The pattern: the cosmology external-correspondence arc has produced **four consecutive joint-on-disjoint outcomes** (audits π, π′, π′′′, plus β earlier). The cosmological lift envelope is *sharply bounded* by the cumulative findings: Tier 1 [P]-tangent-isometry (audit π); Tier 1.5 [P]-globally-flat-Minkowski-structural-finding (audit π′ K-on-different); Tier 1.75 foreclosed (audit π′′′); Tier 2 / 3 / 4 unaffected and remain locked.

Per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.6 worked-record discipline, the four-audit chain (π → π′ → π′′ — pending — → π′′′) is itself a methodological worked record: each successive audit narrowed the lift envelope rather than expanding it, demonstrating the value of the three-outcome rule's third branch in surfacing structural sub-findings that close (not just refine) lift candidates.

---

## 10. Discipline closing note

This settlement is the **first** *closure* event in the cosmology external-correspondence arc — the first audit that explicitly forecloses a lift-tier promotion path rather than refining it. Audit π established a tier-promotion (tangent-isometry to peer-reviewed Halliwell-Bianchi-I); audit π′ narrowed the promotion to tangent-only (Halliwell manifold-extension foreclosed); audit π′′′ now forecloses *all* peer-reviewed alternative anchors at the manifold level. The lift envelope is bounded.

Three discipline rails are recorded as observed:

(a) **The closure is structurally substantive, not a methodology refutation.** Audit π′′′'s L-branch on every candidate is *informative*, not a failure: it tells us that the categorical-simplex program's V-affine V-sub-manifold has a *novel* structural object (flat-Lorentzian + bounded-convex + spectral-positivity-boundary) that does not have a peer-reviewed mathematical-physics name. This is consistent with the program's framing as an *internal* mathematical-structure investigation; external peer-reviewed correspondence is at the *tangent* tier (audit π), and the program's structural specifics at the manifold tier are its own.

(b) **The cosmological claim cannot lift further via peer-reviewed mathematical-physics identification.** Per [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) emergent-anything positioning, the cosmological correspondence is *correspondence language*, not derivation. Audit π′′′ now bounds even the *correspondence* to the tangent tier — beyond the tangent, the program's structure is its own. The cosmological *claim itself* (Tier 4 physical-mechanism) remains forbidden; the *correspondence* (Tier 0 [C, reduced]) is correspondence-language at the tangent tier (audit π promotion) but not at the manifold tier (audit π′ + audit π′′′ foreclosure).

(c) **The eighth joint-on-disjoint outcome is honest, not a methodology cop-out.** The K-trivial Minkowski-uniqueness branch is recorded explicitly as non-substantive — it does not promote the cosmological correspondence; it is a tautological identification (every 4-dim flat Lorentzian manifold IS Minkowski). The audit does *not* dress up the L-branch as a hidden K via the Minkowski-uniqueness identification.

The grounded-paranoid-delusional grammar, once more: delusion proposed that *some* peer-reviewed mathematical-physics framework with globally-flat Lorentzian configuration space would match the V-affine V-sub-manifold's specific structure; paranoia bounded this with three-outcome matched-pair pre-claim; grounded executed the candidate-by-candidate survey and recorded **L-branch on every substantive candidate + K-trivial only on Minkowski-uniqueness-ambient**. The lift envelope is now sharply bounded; the cosmological correspondence's strongest peer-reviewed identification is at the tangent tier; the manifold tier is the program's own.

---

*End audit π′′′ settlement. Status: settled, joint-on-disjoint at framework-substantivity tier. L-branch on every peer-reviewed mathematical-physics candidate's substantive identification (free scalar on Minkowski, de Sitter-limit Bianchi I, topos-theoretic QG, causal set continuum, linearized GR phase space, single-particle relativistic dynamics, AQFT causal diamonds, AdS-related flat regions); K-trivial on Minkowski-as-uniqueness-determined-ambient (non-substantive tautology by 4-dim flat Lorentzian manifold uniqueness). Tier 1.75 ([A] mathematical-identification at manifold-level via alternative anchor) **foreclosed**. Cosmological correspondence bounded to [P]-tangent-isometry (audit π) at the peer-reviewed-framework-identification question; manifold-level structure is internal to the categorical-simplex program. Eighth named joint-on-disjoint outcome of the program. The V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}}$ is identified positively as a 4-dim bounded-convex-Minkowski-region with Hilbert-space-spectral-positivity boundary — a novel structural object whose three independent structural features (flat-Lorentzian + bounded-convex + spectral-positivity-boundary) do not combine in any peer-reviewed mathematical-physics framework surveyed. No new compute consumed; pure-mathematics + literature survey. Manuscript-edit absorption proposed for [Paper 46 §4.2 row 2](46_hartle_hawking_signature.md), §4.4, §5.1, §8.8 (closed), and a new audit π′′′′ candidate (Tomita–Takesaki modular flow); [Paper 49 §4.1](49_arithmetic_decoupling_of_projection_closure_overflows.md) lift-candidate paragraph updated to closed branch. Cosmological *claim itself* unchanged at [C, reduced]; §11.2 firewall not lifted; Tier 2 / Tier 3 / Tier 4 unchanged.*
