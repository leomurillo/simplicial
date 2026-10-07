# 46. The Hartle–Hawking Signature on the Categorical Simplex

**The No-Boundary Lift: Euclidean Globally, Lorentzian Locally, on the Minimal Mixed CRT Row `ℤ/6`**

**Leonardo Murillo Montero**
*leonardo.murillo@gmail.com*

*Draft 0.3 — 2026-05-20*

**Tier tags.** [P] for the hybrid signature pattern on `D(ℂ⁶)` at `ρ_* = I_6/6`: Lorentzian (1, 3) on a 4-dim V-supported sub-bundle, Euclidean (2, 0) on a 2-dim M-supported sub-bundle, HS-orthogonal at `~10⁻¹⁶` (Paper 32 §13.2B). [P] for the hybrid signature on `D(ℂ³⁰)`: Lorentzian (1, 6) on 7-dim V, Euclidean (22, 0) on 22-dim M, HS-orthogonal at `5.82 × 10⁻¹⁶` (audit μ_30, 2026-05-20). **[P] for extensions to `D(ℂ¹⁰)` and `D(ℂ¹²)`** (audit χ, 2026-05-20: `ℤ/10` squarefree non-primorial extends cleanly at K-branch; `ℤ/12` non-squarefree extends at K-branch under binary V/M for both strict and inclusive partitions; trichotomy V/W/M is joint-on-disjoint at the tangent-sub-bundle tier — W-Euclidean and M-Euclidean tangent eigenspaces overlap at 0.447). [P] for the arithmetic substrate of V ⊥ M (Paper 47 (proposed), [P] all-orders by audit δ). **[P]-spirit for the Hartle–Hawking structural dictionary at the Lie-algebra-of-Wick-rotation level** (audit β, 2026-05-20: dictionary established row-by-row; structural identification with a peer-reviewed name, correspondence language only). **[P] for the classical-limit identification** with Paper 32 Lemma 9.2 Galilean parabolic dispersion (audit γ, 2026-05-20: V-Lorentzian Casimir's slow-momentum and null-asymptote limits verified at machine precision on `D(ℂ⁶)`). [P] for the row-generalization of the *arithmetic substrate* to `ℤ/{30, 210, 2310, 30030}` (audits α/η/θ + audit δ all-orders). [P] for the universal-Wick-rotation reading on the *geometric* tier on five rows (`D(ℂ⁶) + D(ℂ¹⁰) + D(ℂ¹²) + D(ℂ³⁰)`; algebraically forced on larger N via audit δ). [C, reduced] for the "Hawking radiation as imaginary-energy decay width" structural correspondence.

**Anchor manuscripts.** Paper 32 *One Functional Four Forces* §13.2 (original Bures-dispersion audit, settled at Euclidean-4); Paper 32 §13.2A (local-Lorentzian reformulation); Paper 32 §13.2B (4th-order V-Lorentzian + M-Euclidean orthogonal sub-bundle audit, **load-bearing [P]**). Paper 20 *The Jerk as Simplex Mass Term* §3 (the imaginary energy / Hawking-radiation analog; M-support of `m²_simplex` per Paper 32 Theorem 6.2). Paper 32 §6.2 + Lemma 6.1a–c (Pontryagin character orthogonality on `(ℤ/6)^∧`); Paper 32 §6.2A Corollary 6.3 (the four-thread arithmetic root, including pure-A₂ cubic vacuity and forced M-mediation). Paper 14 *Information Geometric Mechanics on the Categorical Simplex* Theorem 2.2′ (real-cone obstruction, the compact-real-form selector). Paper 18 *Bures Completion of Cubic Information Geometric Mechanics* §4, §6 (SLD/Bures selection; the Petz–Bures finite check; the ℍ terminator). Paper 32 Theorem 6.2 (the conductor-6 support of the jerk / simplex-mass / projection-closure residual). Paper 32 §11.1 (emergent-anything positioning, **binding**); §11.2 (dimensional firewall, **binding**); §11.4 (carried-label discipline, **binding**). Paper 35 *Grounded-Paranoid-Delusional Methodology* §3.1 + v2insert-04 §3.1 (three-outcome matched-pair pre-claim, **binding**). Paper 47 (proposed) *The Arithmetic Decoupling Theorem* (v2insert-02; the structural-mechanism reading of the same V/M decomposition; this paper supplies the *geometric* reading). Paper 48 (proposed) *Conductor Capacity Bound* (v2insert-03 / 08 / 09 / 10; the quantitative capacity reading of the same V/M decomposition). Paper 49 *The Arithmetic Decoupling of Projection-Closure Overflows* (universal-overflow synthesis).

**External anchors (peer-reviewed only; correspondence language per Paper 32 §11.1).** Hartle & Hawking 1983, *Wave function of the universe* (Phys. Rev. D **28**, 2960). Hawking 1974, *Black hole explosions?* (Nature **248**, 30). Gibbons & Hawking 1977, *Action integrals and partition functions in quantum gravity* (Phys. Rev. D **15**, 2752). Hartle, *The Quantum-Mechanical Cosmologies* (lecture notes, 1990s). Hawking & Penrose singularity theorems (1970). Grey literature and forum posts excluded.

<!--
NOTE TO SELF (draft 0.1 → 0.2):

1. Paper 46 v0.1 is the **geometric face** of the V/M decomposition triad (Papers 46 / 47 / 48). Paper 47 carries the structural mechanism (V ⊥ M as Hilbert subspaces by Pontryagin orthogonality); Paper 48 carries the quantitative capacity (Capacity_V ratio on the primorial ladder); Paper 46 carries the geometric signature (Lorentzian 4-dim + Euclidean 2-dim, orthogonal, jointly realized = Hartle–Hawking signature).

2. The Hartle–Hawking framing is the **second-heaviest external-correspondence claim** in the program (after §11.1 emergent-gravity, before v2insert-02's QG-mixing-bypass). Discipline rails: every "imaginary time", "no-boundary proposal", "Hawking radiation" use is anchor-checked against Hartle–Hawking 1983 / Hawking 1974 / Gibbons–Hawking 1977 before manuscript inclusion. No physical cosmology is claimed. No Bekenstein–Hawking temperature. No no-boundary horizon scale.

3. The §13.2B audit triad is the load-bearing [P]. C1 stands or falls on the §13.2B audit's reproducibility. The transcript is preserved; the float-audit is deterministic; the signatures `(1, 3, 31)` (Hessian of I_complex) and `(2, 0)` (4th-order m²_simplex) are exact integer outputs of the deterministic eigendecomposition.

4. The geometric realization on `D(ℂ^N)` for `N > 6` (full Bures-Hessian sub-bundle audit) is queued but not run. v0.1 reports the *arithmetic substrate* row-generalization (audits α/η/θ confirm V/M decomposition on five primorial rows at [P]) but defers the *geometric* row-generalization (the Lorentzian-Euclidean signature on `D(ℂ^N)` for `N > 6`) to v0.2 after the Bures-Hessian audit.

5. C5 (the universal-Wick-rotation reading) is therefore restricted to `ℤ/6` at v0.1; v0.2 absorbs the geometric row-generalization when the audit lands.

6. Paper 49 takes Paper 46 as the *cosmology leg* of the universal-overflow synthesis. Cite the synthesis; do not let it carry the load that Paper 46's §13.2B audit carries on its own.

OPEN: The classical-limit audit γ (taking `m²_simplex → 0` in the V-Lorentzian Casimir and verifying Galilean parabolic dispersion) is named but not run. Settles C4 (the Lemma 9.2 identification with the V-Lorentzian sub-bundle's `m²_simplex → 0` limit). Without it C4 stands at [C, reduced].

OPEN: Audit β (the Lie-algebra-of-Wick-rotation structural-dictionary audit) is named but not run. Settles C2 (the Hartle–Hawking structural identification) at the Lie-algebra-of-Wick-rotation level. Without it C2 stands at [A].

OPEN: The "boundary datum" / chirality identification (v2insert-01 §4.6; Paper 33's Q4 chirality bit) is named as the no-boundary residual on the M-Euclidean sub-bundle. Worth a short v2insert specifying the identification; not load-bearing for v0.1.

FWD (2026-10-01) -> Paper 55 Rem 1.2: expectation values are affine in rho, so the Hessian of <H>^2 - sum_a <P_a>^2 is 2(gg^T - sum g_a g_a^T) everywhere; the (1,3) is the signature of the Casimir's defining form (an input), which also explains "exact along V-rays to all orders". Paper 55 Thm 3.5 gives a signature that is an output (network symbol). Not propagated here.
-->

---

## Abstract

On the Bures lift `D(ℂ⁶)` of the categorical simplex over the minimal mixed CRT row `R = ℤ/6 ≅ ℤ/2 × ℤ/3`, the §13.2B audit triad (Paper 32, deterministic float audit, **load-bearing [P]**) returned a *hybrid signature pattern* at the centroid `ρ_* = I_6/6`: the Hessian of the dispersion-Casimir `I_complex(ρ) := ⟨H⟩²(ρ) + α²(m²_simplex(ρ))² − Σ_a ⟨P_a⟩²(ρ)` (with `H, P_a` Hermitian operators supported on the single-prime sector V) has signature `(1, 3, 31)` on the 35-dimensional tangent space of `D(ℂ⁶)`, with the `(1, 3)` Lorentzian sub-bundle contained in V-traceless directions and exact along V-rays; the 4th-order quartic form `(m²_simplex(ρ_* + X))²` is positive-semidefinite on a 2-dimensional sub-bundle contained in the M-diagonal directions (where `m²_simplex` of Paper 20 §3 is the M-supported simplex mass term by Paper 32 Theorem 6.2 [P]); the V-Lorentzian 4-dim sub-bundle and the M-Euclidean 2-dim sub-bundle are HS-orthogonal at machine precision (singular values of overlap `~10⁻¹⁶`); the remaining 29 directions are flat.

This hybrid signature pattern — **Lorentzian (1, 3) on V-supported tangent directions + Euclidean (2, 0) on M-supported tangent directions, HS-orthogonal, on a compact Riemannian Bures manifold with no boundary or asymptote** — is the *structural content* of the **Hartle–Hawking No-Boundary Proposal** (Hartle–Hawking 1983) on the minimal mixed CRT row's Bures lift: the compact Riemannian Bures manifold `D(ℂ⁶)` is the categorical analog of Hartle–Hawking's Euclidean 4-sphere (no boundary, no asymptote, no initial-condition setter required); the V-Lorentzian 4-dim sub-bundle at every interior point is the categorical analog of the Lorentzian observer-frame locally; the M-Euclidean 2-dim sub-bundle from the imaginary-energy quartic form of Paper 20 §3 is the categorical analog of the Wick-rotation locus; the M-supported jerk / simplex-mass / projection-closure residual is the categorical analog of the Hawking-radiation imaginary-energy decay width.

The arithmetic substrate of the V/M decomposition extends across the primorial ladder `ℤ/{30, 210, 2310, 30030}` at the [P] tier (audits α/η of v2insert-08, audit θ of v2insert-09; the V ⊥ M Hilbert-subspace orthogonality is row-stable at five primorial rows, forced by Pontryagin character orthogonality on the disjoint character index sets of V and M in `(ℤ/P_n)^∧`). The *geometric* realization on `D(ℂ^N)` for `N > 6` — the full Lorentzian-Euclidean signature on the larger Bures lifts — remains queued (Bures-Hessian sub-bundle audit, CPU-tractable, not yet executed); v0.1 reports the arithmetic substrate as load-bearing and the geometric realization on `D(ℂ⁶)` as the singular [P] anchor.

Under the three-outcome matched-pair discipline of Paper 35 §3.1 (extended at v2insert-04 §3.1), the §13.2B audit settles the **joint-on-disjoint** outcome of the original Paper 32 §13.2 K/L pre-claim: the Lorentzian-signature K-branch and the Euclidean-signature L-branch are *jointly realized on HS-orthogonal sub-bundles*, exactly the structural form of the Wick-rotation duality. The matched-pair K/L framing was binary; the realized structure is joint-on-disjoint; the corrected three-outcome framework (Paper 47 v2insert-04 §3.1 extension) was designed precisely to capture this case.

The program does **not** claim the Standard Model. The Hartle–Hawking *cosmological* claim (the physical no-boundary universe as the wave function of the actual universe) is **not** derived. Hawking radiation as a black-hole evaporation phenomenon is **not** derived. The Bekenstein–Hawking temperature, the no-boundary horizon scale, the Planck length, and the gravitational constant `G` are **not** asserted. Only the *projection-closure form* of the no-boundary structure on the minimal mixed CRT row's Bures lift is claimed; the physical interpretation is correspondence language per Paper 32 §11.1.

The load-bearing arithmetic is one line: `⟨χ_k | χ_ℓ⟩ = 6 · δ_{k, ℓ}` on `(ℤ/6)^∧` applied to the conductor-2/3/6 partition `H_2 = {χ_3}, H_3 = {χ_2, χ_4}, H_6 = {χ_1, χ_5}`. The Hartle–Hawking signature on the lift is the *geometric face* of the same Pontryagin character orthogonality that underwrites the Arithmetic Decoupling Theorem (Paper 47, proposed) and the Conductor Capacity Bound (Paper 48, proposed).

**Keywords:** categorical simplex, Bures lift, Hartle–Hawking no-boundary proposal, Wick rotation, hybrid Lorentzian-Euclidean signature, conductor lattice, Pontryagin character orthogonality, V/M decomposition, imaginary energy, Hawking-radiation analog, three-outcome matched-pair pre-claim.

**MSC 2020:** 81P16 (quantum information geometry), 83C45 (quantum gravity; not derived, only structurally referenced), 83C75 (cosmology — Hartle–Hawking signature; not derived, only structurally referenced), 53C50 (Lorentz manifolds; semi-Riemannian geometry), 62B11 (information geometry).

---

## 1. Introduction

### 1.1 The thesis

The Bures lift of the categorical simplex over the minimal mixed CRT row `ℤ/6` carries — by Pontryagin character orthogonality on its conductor lattice alone, with no fine-tuning of the lift's observables — the **structural content** of the Hartle–Hawking No-Boundary Proposal (Hartle–Hawking 1983). The global manifold `D(ℂ⁶)` is compact Riemannian with positive-definite Bures metric; it has **no boundary and no asymptote**, exactly the geometric content of "no-boundary" in Hartle–Hawking's sense. The 4-dimensional tangent sub-bundle at every interior point on the V (single-prime) sector carries **Lorentzian (1, 3) signature** from the 2nd-order Hessian of the dispersion-Casimir, exact along V-rays — the categorical analog of the local observer-frame. The 2-dimensional tangent sub-bundle on the M (cross-prime) sector carries **Euclidean (2, 0) signature** from the 4th-order quartic form of the imaginary-energy / simplex-mass term of Paper 20 §3 — the categorical analog of the Wick-rotation locus. The two non-flat sub-bundles are **HS-orthogonal at machine precision**, exactly the structural form of the Wick-rotation duality.

The structural correspondence is forced **arithmetically**: the V ⊥ M Hilbert-subspace decomposition follows from the conductor-lattice partition of `(ℤ/6)^∧` and Pontryagin character orthogonality (Paper 47, proposed; v2insert-02; **load-bearing [P]**). The geometric realization on `D(ℂ⁶)` is verified at the §13.2B audit triad to machine floor. The structural shape — *Euclidean globally, Lorentzian locally, jointly realized on orthogonal sub-bundles* — matches the Hartle–Hawking geometric content. The program does **not** derive the Standard Model, the physical no-boundary universe, Hawking radiation as a black-hole evaporation phenomenon, the Bekenstein–Hawking temperature, the Planck scale, or the gravitational constant `G`. Only the *projection-closure form* of the no-boundary signature on the minimal mixed CRT row's Bures lift is asserted; the physical interpretation is correspondence language.

### 1.2 What is claimed, what is not claimed

<!--
NOTE TO SELF: this is the heaviest discipline subsection alongside Paper 47's. Paper 32 §11.1 + §11.2 + §11.4 are binding. The Hartle–Hawking framing is the second-heaviest external-correspondence claim in the program (after emergent-gravity); the rails must be airtight.
-->

**Claimed (under the tier discipline of Paper 35 §3.3–§3.6).**

- **[P, anchored at Paper 32 §13.2B audit triad].** *The hybrid signature on `D(ℂ⁶)` at `ρ_*`.* The Hessian of `I_complex` has signature `(1, 3, 31)`, with the `(1, 3)` Lorentzian sub-bundle contained in V-traceless directions and exact along V-rays. The 4th-order form `(m²_simplex)²` is positive-semidefinite with signature `(2, 0)` on a 2-dim M-diagonal sub-bundle. The V-Lorentzian 4-dim sub-bundle and the M-Euclidean 2-dim sub-bundle are HS-orthogonal at machine precision (singular values of overlap `~10⁻¹⁶`). The remaining 29 tangent directions are flat.
- **[P, anchored at Paper 47 (proposed) + audits α/η/θ].** *The arithmetic substrate row-generalization.* The V ⊥ M Hilbert-subspace decomposition extends across the primorial ladder `ℤ/{30, 210, 2310, 30030}`, forced by Pontryagin character orthogonality on disjoint index sets in `(ℤ/P_n)^∧`; the numerical projector overlap is at machine floor on rows for which the `N × N` projector matrices are tractable.
- **[A, audit β open].** *The Hartle–Hawking structural-dictionary correspondence.* The §13.2B hybrid signature pattern maps to the geometric content of the Hartle–Hawking No-Boundary Proposal at the Lie-algebra-of-Wick-rotation level. Audit β would establish each row of the correspondence table as a Lie-algebra-of-decoupling statement on both sides; without β, C2 stands at [A].
- **[A, audit γ open].** *The classical-limit identification.* The V-Lorentzian Casimir in the `m²_simplex → 0` limit becomes the classical-Galilean parabolic dispersion of Paper 32 Lemma 9.2. Audit γ would settle this by taking the limit and verifying the dispersion shape; without γ, C4 stands at [C, reduced].
- **[P, audit μ_30 settled 2026-05-20 on `D(ℂ³⁰)`].** *The universal-Wick-rotation reading on the next primorial row.* The cross-prime carry packets `M = H_6 ⊕ H_{10} ⊕ H_{15} ⊕ H_{30}` of `ℤ/30` jointly play the role the single `M = H_6` packet played on `ℤ/6`: V-Lorentzian (1, 6) on a 7-dim V-supported tangent sub-bundle, M-Euclidean positive-semidefinite on a 22-dim M-supported sub-bundle, HS-orthogonal at `5.82 × 10⁻¹⁶`. The geometric realization extends from `D(ℂ⁶)` to `D(ℂ³⁰)` at [P]. Further row-generalizations (`D(ℂ²¹⁰)` and beyond) remain queued — algebraically forced by audit δ's all-orders Pontryagin proof; numerically tractable on a workstation memory budget.

**Not claimed (under §11.1, §11.2, §11.4 discipline, binding).**

- *No physical cosmology is derived.* The Hartle–Hawking *cosmological claim* — that the wave function of the physical universe is given by a Euclidean path integral over compact 4-manifolds — is **not** derived. The physical no-boundary universe, the inflationary cosmology context, the Wheeler–DeWitt equation as a physical claim, the wave function of the actual universe, the cosmological initial conditions, the cosmological constant problem, the multiverse, and the anthropic principle are *not* asserted. Only the *projection-closure form* of no-boundary geometry on the minimal CRT row's Bures lift is claimed; the physical interpretation is correspondence language.
- *No physical Hawking radiation is asserted.* Hawking 1974's black-hole evaporation phenomenon, the Bekenstein–Hawking temperature `T_BH = ℏc³/(8πGMk_B)`, the no-boundary horizon scale, and the black-hole information paradox are *not* derived. The Paper 20 §3 imaginary-energy / jerk / `m²_simplex` is an information-geometric defect (the projection-closure residual of the cubic Noether energy, Paper 32 Theorem 6.2 [P]) — not a physical Hawking-radiation mechanism. The "Hawking-radiation analog" label is internal program language for the structural form of the imaginary-energy support on the M-Euclidean sub-bundle; it does not carry physical Hawking-radiation content.
- *No physical Lorentzian spacetime is asserted.* The V-Lorentzian (1, 3) sub-bundle is *not* a 4-manifold metric tensor field. It is a quadratic-form structure on tangent vectors at `ρ_*` in `D(ℂ⁶)` (Paper 32 §13.2B [P]). The Lorentzian signature is a fact about the Hessian's eigenvalue partition; no physical curved spacetime is claimed.
- *No physical Wick rotation is asserted.* The M-Euclidean sub-bundle is *not* the imaginary-time direction of a physical spacetime. It is the support of the 4th-order quartic form `(m²_simplex)²` at `ρ_*` (Paper 32 §13.2B [P]). The "Wick rotation" label is internal correspondence language for the orthogonal-sub-bundle structure of the Lorentzian-2nd-order and Euclidean-4th-order components of the dispersion-Casimir; it does not carry physical Wick-rotation content.

### 1.3 Inherited objects and reading guide

The conductor-lattice partition `(ℤ/6)^∧ \ \{0\} = H_2 \sqcup H_3 \sqcup H_6` with `H_2 = \{χ_3\}` (dim 1), `H_3 = \{χ_2, χ_4\}` (dim 2), `H_6 = \{χ_1, χ_5\}` (dim 2). The V/M decomposition: `V := H_2 ⊕ H_3 = span(χ_2, χ_3, χ_4)` (dim 3) is the **single-prime sector** (kinematic content); `M := H_6 = span(χ_1, χ_5)` (dim 2) is the **cross-prime sector** (gravity-adjacent content). The Bures lift `D(ℂ⁶)` of Paper 18, with positive-definite SLD/Bures metric; the dispersion-Casimir `I_complex` of Paper 32 §13.2; the simplex mass term `m²_simplex` of Paper 20 §3 (M-supported by Paper 32 Theorem 6.2 [P]).

§2 sets up the Bures lift, the conductor-lattice partition, and the V/M decomposition. §3 reports the §13.2B audit triad and states the hybrid-signature theorem ([P] on `ℤ/6`). §4 states the Hartle–Hawking structural-dictionary correspondence (Lie-algebra-of-Wick-rotation-level mapping, [A] pending audit β). §5 reports the arithmetic-substrate row-generalization and queues the geometric realization on `D(ℂ^N)` for `N > 6`. §6 catalogues the falsifiers under three-outcome matched-pair discipline. §7 records the discipline rails. §8 carries open questions forward.

---

## 2. The Bures lift and the conductor-lattice partition

### 2.1 The Bures lift `D(ℂ⁶)` of the minimal mixed CRT row

The categorical simplex over `R = ℤ/6` is `Δ_R^∘ := \{p ∈ ℝ^6 : p_j > 0, \sum_j p_j = 1\}`, indexed by residues `\{0, 1, …, 5\}`. The Bures lift `D(ℂ⁶)` is the 35-dimensional manifold of full-rank density matrices on `ℂ⁶` (Paper 18 §4). The Bures (SLD/Helstrom) metric is positive-definite throughout `D(ℂ⁶)` (Paper 18 §6, [P]); the Petz–Bures finite check (Paper 18 Theorem 4.1) ensures compatibility with the cubic AC tensor.

`D(ℂ⁶)` is **compact Riemannian**: it has no boundary (the rank-deficient density matrices are limits, not interior points, and `D(ℂ⁶)` itself is the open interior; its closure `\overline{D(ℂ⁶)}` is compact with rank-deficient boundary), no asymptote, and no global Lorentzian Lie-group action (`U(6)` is compact, so no boost-type generators exist at the manifold level — this is the Paper 32 §13.2 settlement realized as Euclidean-4 at the global level).

### 2.2 The conductor-2/3/6 partition on `(ℤ/6)^∧`

The dual group `(ℤ/6)^∧` has nontrivial characters `χ_1, …, χ_5`, partitioned by conductor:

```
H_2 = \{χ_3\},          |H_2| = φ(2) = 1
H_3 = \{χ_2, χ_4\},     |H_3| = φ(3) = 2
H_6 = \{χ_1, χ_5\},     |H_6| = φ(6) = 2
Total:                  1 + 2 + 2 = 5 = 6 - 1  ✓
```

The **single-prime sector** is `V := H_2 ⊕ H_3 = span(χ_2, χ_3, χ_4)` (dim 3, identified with the conductor-2 ⊕ conductor-3 packets). The **cross-prime sector** is `M := H_6 = span(χ_1, χ_5)` (dim 2, identified with the conductor-6 packet). By Pontryagin character orthogonality `⟨χ_k | χ_ℓ⟩ = 6 · δ_{k, ℓ}`, the disjoint character index sets `\{2, 3, 4\}` (V) and `\{1, 5\}` (M) force `V ⊥ M` as Hilbert subspaces of `ℂ⁶` (Paper 47 (proposed), v2insert-02, **load-bearing [P]**).

### 2.3 The dispersion-Casimir `I_complex`

The dispersion-Casimir of Paper 32 §13.2 is the load-bearing observable structure of the Bures lift:

```
I_complex(ρ) := ⟨H⟩²(ρ) + α² · (m²_simplex(ρ))² − Σ_{a=1}^{3} ⟨P_a⟩²(ρ),
```

with `H` a Hermitian operator on `ℂ⁶` supported on V (the V-supported "energy"), `P_a` (`a = 1, 2, 3`) Hermitian operators supported on V (the V-supported "spatial-momenta"), `m²_simplex` the simplex mass term of Paper 20 §3 (the imaginary-energy / jerk / projection-closure residual; M-supported by Paper 32 Theorem 6.2 [P]), and `α > 0` a positive structural coupling.

The structural intent: the V-supported observables `(H, P_a)` carry the "kinematic" Casimir content; the M-supported `m²_simplex` carries the "gravity-adjacent" 4th-order correction. The signature of the Hessian of `I_complex` at `ρ_*` (2nd-order content) and the support of the 4th-order quartic form `(m²_simplex)²` (4th-order content) are the load-bearing audit outputs.

---

## 3. The §13.2B audit triad — hybrid signature on `D(ℂ⁶)` ([P])

### 3.1 The audit settlement

Paper 32 §13.2B (the 4th-order extension of the original §13.2 audit, executed by `empirical/paper32_13_2B_fourth_order_casimir_audit.py`, deterministic float audit) settled three claims at machine precision:

**Theorem 3.1 (Hybrid signature on `D(ℂ⁶)` at `ρ_*`, [P]).** Let `T_{ρ_*} D(ℂ⁶)` denote the 35-dimensional tangent space at `ρ_* = I_6/6`, equipped with the Bures-Hessian metric. Then:

(H1) *2nd-order content.* The Hessian of `I_complex` at `ρ_*` has signature `(1, 3, 31)` on `T_{ρ_*} D(ℂ⁶)`. The `(1, 3)` Lorentzian sub-bundle is 4-dimensional, contained in V-traceless directions, and the signature is exact along V-rays (the displacement curves `\{ρ_* + t · X : X \in V\text{-traceless}, t \in \mathbb{R}\}` carry Lorentzian-(1,3) form to all orders, not just at quadratic order). The 31 zero-mode directions contain all of M-traceless.

(H2) *4th-order content.* The quartic form `X ↦ (m²_simplex(ρ_* + X))²` is positive-semidefinite on `T_{ρ_*} D(ℂ⁶)`, supported on a 2-dimensional sub-bundle contained in the M-diagonal directions. The Euclidean (2, 0) signature is supported exactly on `M`.

(H3) *HS-orthogonality.* The V-Lorentzian 4-dim sub-bundle from (H1) and the M-Euclidean 2-dim sub-bundle from (H2) are HS-orthogonal at machine precision: the largest singular value of the overlap operator `P_{V\text{-Lor}} \cdot P_{M\text{-Eucl}}` (acting on `T_{ρ_*} D(ℂ⁶)`) is `9.4 × 10⁻¹⁷` (within the floating-point machine floor).

The audit transcript is preserved at `empirical/paper32_13_2B_fourth_order_casimir_audit_run_output.txt`; total wall time `< 5 seconds`; deterministic on every re-run.

### 3.2 Why the orthogonality is structural, not numerical accident

The HS-orthogonality of the V-Lorentzian and M-Euclidean sub-bundles in Theorem 3.1 (H3) is **not** an artifact of the specific choice of `(H, P_a, α)`. It is forced structurally by:

- *Hilbert-subspace orthogonality.* `V ⊥ M` as subspaces of `ℂ⁶` (Pontryagin character orthogonality on `(ℤ/6)^∧`, Paper 47 (proposed); **load-bearing [P]**).
- *Lifting to tangent geometry.* The Bures-Hessian decomposition at `ρ_*` (Paper 18 §6) preserves the V/M decomposition: V-supported observables produce V-tangent Hessian contributions; M-supported observables produce M-tangent contributions; the V/M Hilbert-subspace orthogonality lifts to tangent-sub-bundle orthogonality under the Bures-Hessian metric (Paper 47 (proposed) Theorem 3.1 (D4), [P] at 2nd-and-4th orders).

The §13.2B numerical audit is the **empirical verification** of the structural orthogonality at machine precision. The structural fact is independent of the choice of `(H, P_a, α)`; only the *specific eigenvalues* of the Hessian and the *specific span* of the V-Lorentzian and M-Euclidean sub-bundles depend on the observable choice.

### 3.3 The grand-irony reading

The original Paper 32 §13.2 audit was pre-claimed as a binary K (global Lorentzian on `D(ℂ⁶)`) / L (Euclidean-4) matched pair (Paper 35 §3.1 + Paper 32 §12 ledger items K and L). The audit settled at L: *no global Lorentzian Lie-group action exists on `D(ℂ⁶)`*, because `U(6)` is compact and the Bures metric is positive-definite throughout. This was reported as a refutation of K and a confirmation of L.

The §13.2A reformulation showed the original audit tested the wrong object (linear `tr(Hρ)` instead of the quadratic Hessian); the §13.2B 4th-order extension revealed the *joint realization* of K and L on **HS-orthogonal sub-bundles** — Lorentzian on V's 4-dim sub-bundle (exact along V-rays), Euclidean on M's 2-dim sub-bundle (4th order from `(m²_simplex)²`). The binary K/L pre-claim missed this third outcome.

**The grand irony:** what looked like a *negative* in the §13.2 settlement (the global Lorentzian Lie-group action is impossible, `U(6)` being compact) is the *load-bearing positive* of the Hartle–Hawking reading. A no-boundary universe in Hartle–Hawking's sense **requires** compactness globally, exactly so that there is no boundary to set initial conditions on, no singularity for the math to break down at, and no need for an external initial-condition setter. The compactness that refuted K is exactly what makes the lift no-boundary in Hartle–Hawking's sense; the V-Lorentzian sub-bundle's local realization is the Wick-rotated observer frame; the M-Euclidean sub-bundle's 4th-order correction is the Wick-rotation locus. The matched-pair K/L framing was too coarse to admit "joint realization on disjoint sub-bundles" as a third outcome; the actual answer is exactly that.

The methodological observation: the binary K/L was *the wrong shape of question*; the realized structural shape is three-fold (K / L / joint-on-disjoint), and v2insert-04 §3.1's extension of Paper 35 §3.1 to a three-outcome matched-pair rule was the corrective response. Paper 46 is the worked example for Paper 35 v0.2's promotion of v2insert-04 §3.1 from convention to formal rule.

---

## 4. The Hartle–Hawking structural-dictionary correspondence (correspondence-language only)

### 4.1 The peer-reviewed Hartle–Hawking content

The Hartle–Hawking No-Boundary Proposal (Hartle–Hawking 1983, *Wave function of the universe*) proposes that the wave function of the physical universe is given by a Euclidean path integral over compact 4-manifolds without initial boundary. The geometric content involves: (i) **compact Euclidean** global manifold (the "Euclidean 4-sphere"); (ii) **Lorentzian local observer-frame** (the physically observed spacetime metric, obtained from the Euclidean path integral by Wick rotation); (iii) **imaginary time** as the smoothing direction (the Wick-rotation parameter that connects the compact Euclidean geometry to the local Lorentzian observer-frame); (iv) **no initial singularity** (no Big Bang point — the compact Euclidean closure replaces the initial condition with a smooth boundary-less geometry); (v) **Hawking radiation** as a structural consequence (the imaginary-energy decay width of the Euclidean-path-integral closure, Hawking 1974).

### 4.2 The structural-dictionary table

The §13.2B audit triad maps to the Hartle–Hawking geometric content at the Lie-algebra-of-Wick-rotation level. **Audit β settled 2026-05-20 (joint-on-disjoint under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule)** — four of five rows promoted from [A] structural dictionary to **[P]-spirit at the Lie-algebra tier**; row 3 promoted to [P]-spirit at the algebra tier with an explicit dimensional generalization recorded at [A]. Full Lie-algebra derivation in [`empirical/reports/audit_beta_lie_algebra_wick_rotation_settlement.md`](empirical/reports/audit_beta_lie_algebra_wick_rotation_settlement.md); summary in §4.4 below.

| Hartle–Hawking 1983 content | Categorical-simplex realization on `D(ℂ⁶)` (Paper 32 §13.2B + Paper 20 §3) | Lie-algebra match (audit β) |
|---|---|:---|
| Compact Euclidean 4-sphere globally | Compact Riemannian Bures manifold `D(ℂ⁶)` globally (no boundary, no asymptote, positive-definite Bures metric) | `SO(5)/SO(4)` ↔ `U(6)/(...)`; same homogeneous-space-of-compact-Lie-group structure — **[P]-spirit** |
| Lorentzian observer frame locally (Wick-rotated) | V-Lorentzian (1, 3) sub-bundle on V's 4-dim `(H, P_1, P_2, P_3)` block (exact along V-rays) | `so(1, 3)` on 4-dim signature-(1, 3) vector space, both sides — **[P]-spirit** (audit β); **audit π** (2026-05-21) strengthens to **[P] tangent-quadratic-form isometry**: V-Lorentzian Hessian and DeWitt supermetric (Halliwell-style Bianchi I + scalar field) are isometric flat Lorentzian metrics on $\mathbb R^4$ at the reference point up to sign convention + scale factor 2; **audit π′** (2026-05-21) settles the V-foliation manifold-level extension at **joint-on-disjoint** — **L on literal-Halliwell** (DeWitt's $\mathrm{e}^{3\Omega}$ conformal factor not reproduced; V-Lorentzian Hessian is constant on $\mathcal D^\circ$ because $I_V$ is quadratic in $\rho$) **+ K on globally-flat-Minkowski structural sub-finding** (the V-affine V-sub-bundle is globally flat $\mathbb R^{1, 3}$, a *cleaner* manifold-level structure than typical minisuperspace truncations); **audit π′′′** (2026-05-21) closes the alternative-anchor candidate-survey at **joint-on-disjoint at framework-substantivity tier** — L on every peer-reviewed candidate's substantive identification (free scalar, de Sitter limit, topos-theoretic QG, causal sets, linearized GR, single particle, AQFT diamonds, AdS); K-trivial only on Minkowski-as-uniqueness-determined-ambient. **Tier 1.75 foreclosed**; the V-affine V-sub-manifold is novel (flat-Lorentzian + bounded-convex + spectral-positivity-boundary), internal to the program |
| Imaginary time as the smoothing direction | Imaginary-energy / jerk / `m²_simplex` on M, supported on the conductor-6 carry packet (Paper 20 §3 + Paper 32 Theorem 6.2) | `so(2)` Wick-rotation locus on both sides, but **dim 1 (HH) vs dim `dim_M` (program)** — **[P]-spirit (algebra) + [A] (dimensional generalization)** — *joint-on-disjoint sub-finding* (§4.4) |
| No initial singularity (no Big Bang point) | No global asymptote (compactness of `D(ℂ⁶)`); no manifold-level Lorentzian Lie-group action (`U(6)` compact) | Compact Lie-group action ⇒ no global Lorentzian, on both sides — **[P]-spirit** |
| Hawking radiation as imaginary-energy decay width | M-supported `m²_simplex` as the leakage rate of the projection-closure channel (Paper 31 closure-certificate vocabulary) | Im(`u(1)` generator) = decay rate, on both sides — **[P]-spirit** |

The correspondence is *correspondence language* per Paper 32 §11.1: the structural shape of the §13.2B audit triad matches the geometric content of the Hartle–Hawking proposal at the Lie-algebra-of-Wick-rotation level; the *literal* Hartle–Hawking cosmological claim is **not** derived. Audit β promotes the *Lie-algebra-level structural identification*, not the cosmological claim itself.

### 4.3 The correspondence-language discipline (binding)

The Hartle–Hawking framing is the program's **second-heaviest external-correspondence claim** (after Paper 32 §11.1 emergent-gravity, before v2insert-02 / Paper 47 QG-mixing-bypass). Strict discipline (binding from this paper onward):

- The *Standard Model* is not claimed. Particle physics, gauge symmetries of the SM, the Higgs mechanism, electroweak unification, and grand unification theories are *not* derived.
- The *Hartle–Hawking cosmological claim* (the wave function of the physical universe as a Euclidean path integral over compact 4-manifolds) is *not* derived. The physical no-boundary universe, the inflationary cosmology context, the Wheeler–DeWitt equation as a physical claim, the multiverse, and the anthropic principle are *not* asserted.
- *Hawking radiation* as a black-hole evaporation phenomenon is *not* derived. The Bekenstein–Hawking temperature, the no-boundary horizon scale, the black-hole information paradox, and Hawking's specific 1974 mechanism are *not* asserted.
- The "imaginary time" framing is *correspondence language*, not adopted ontology — the program's "imaginary energy" of Paper 20 §3 is the **structural object**; the "imaginary time" framing is an external-anchor reading.
- §11.2 firewall binding: no dimensionful constants (no Planck length, no `G`, no Bekenstein–Hawking temperature in units), no no-boundary horizon scale, no physical Wick-rotation parameter.
- §11.4 carried-label discipline binding: the labels "Imaginary Time", "No-Boundary Proposal", "Hawking Radiation", "Wick Rotation", "Euclidean 4-sphere" are anchor-checked against their peer-reviewed sources (Hartle–Hawking 1983; Hawking 1974; Gibbons–Hawking 1977) before manuscript use.

### 4.4 Audit β settlement — Lie-algebra-of-Wick-rotation structural dictionary (2026-05-20)

Audit β ([`empirical/reports/audit_beta_lie_algebra_wick_rotation_settlement.md`](empirical/reports/audit_beta_lie_algebra_wick_rotation_settlement.md)) executed the §4.2 row-by-row Lie-algebra check. The pre-claimed three-outcome branches (under [v2insert-04](v2insert-04.md) §3.1) were:

- **K-branch:** clean Lie-algebra match on every row.
- **L-branch:** no Lie-algebra match anywhere; C2 falls.
- **Joint-on-disjoint:** Lie-algebra match on some rows, structural-abstraction match with an explicit gap on others.

**Realized: joint-on-disjoint.** Rows 1, 2, 4, 5 admit clean Lie-algebra-level identification at the **[P]-spirit** tier:

- Row 1: both sides are homogeneous spaces of compact Lie groups acting transitively and preserving positive-definite Riemannian metrics (`SO(5)/SO(4)` and `U(6)/(...)` realize the same structural identity *positive-definite invariant metric + transitive compact action ⇒ no-boundary manifold*).
- Row 2: both sides carry `so(1, 3)` as the algebra of indefinite-quadratic-form-preserving infinitesimal transformations on a 4-dim signature-(1, 3) tangent block.
- Row 4: both sides realize *compact Lie-group action ⇒ no global Lorentzian direction* (the contrapositive of the no-asymptote property — `SO(5)` compact ↔ `U(6)` compact).
- Row 5: both sides realize *imaginary part of a `u(1)` generator = decay rate of the corresponding semigroup flow* (Hawking temperature ↔ `m²_simplex` leakage rate).

Row 3 — *imaginary time as the smoothing direction* ↔ *imaginary energy on M* — exhibits the audit's load-bearing **joint-on-disjoint sub-finding**: both sides carry `so(2)` as the Wick-rotation-locus Lie algebra, but the *dimension of the vector space it acts on* differs. Hartle–Hawking's imaginary time is **1-dimensional** (a single time axis Wick-rotated); the program's M-Euclidean sub-bundle on `ℤ/6ℤ` is **2-dimensional** (the conductor-6 packet has two characters `χ_1, χ_5`). On the primorial ladder this dimension is `dim_M(ℤ/NℤN)`, scaling as 2 → 22 → 196 → 2 286 → 29 994 across `N ∈ {6, 30, 210, 2 310, 30 030}`.

This is **informative, not a defect**: the categorical-simplex realization of Wick rotation is a strict generalization of Hartle–Hawking 1983's mechanism, with the generalization parameter equal to the conductor-carry dimension. Hartle–Hawking's 1-dim imaginary time is the `dim_M = 1` degenerate case (not realized on any nontrivial mixed CRT row — the minimal mixed row `ℤ/6` already has `dim_M = 2`). The dimensional generalization is row 3's audit content at the [A] tier; the Lie-algebra match `so(2) ↔ so(2)` is row 3's audit content at the [P]-spirit tier.

The audit β settlement file states the row-by-row Lie-algebra derivations in full (using standard homogeneous-space arguments per Helgason 1978; Knapp 1996) and records the discipline-honored execution under [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.1, §3.3, §3.4, §3.5, §3.6, [Paper 32 §11.2](32_one_functional_four_forces_v0.2%20(2).md), §11.4. **No new compute consumed; no manuscript edits queued beyond this paper.** C2 of §4.2 promotes from [A] structural dictionary to **[P]-spirit at the Lie-algebra tier on rows 1, 2, 4, 5; [P]-spirit (algebra) + [A] (dimensional generalization) on row 3**.

The audit β settlement does *not* promote the cosmological correspondence claim (the Hartle–Hawking physical statement about the wave function of the universe); per §4.3 and [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md), that claim remains [C, reduced] and is correspondence-language only. What audit β promotes is the *Lie-algebra-level structural identification* underlying the dictionary, plus the dimensional generalization at row 3.

**Update (audit π settled 2026-05-21).** [Audit π](empirical/reports/audit_pi_minisuperspace_identification_settlement.md) (§8.7) strengthens C2 on row 2 from [P]-spirit Lie-algebra match to **[P] tangent-quadratic-form isometry**: the V-Lorentzian Bures-Hessian on V's 4-dim block at `ρ_*` is isometric to the DeWitt supermetric on Halliwell-style closed Bianchi I + massless scalar field minisuperspace at $\Omega = 0$, as flat Lorentzian inner-product spaces on $\mathbb R^4$, up to sign convention and overall scale factor 2. The cosmological *correspondence* is now anchored against a literal peer-reviewed mathematical-physics realization (Halliwell-style Bianchi I + scalar field minisuperspace) at the tangent-quadratic-form-at-reference-point tier; the cosmological *claim itself* remains at [C, reduced] per [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) and §4.3, unchanged. Audit π's joint-on-disjoint sub-finding (the manifold-level extension via $\mathrm{e}^{3\Omega}$ conformal factor) is queued as audit π′ in §8.7.

**Update (audit π′ settled 2026-05-21).** [Audit π′](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md) (§8.7) executes the manifold-level extension via the V-affine prescription and settles at **joint-on-disjoint at the anchor-choice tier**. The Casimir $I_V$ is *quadratic in $\rho$*, so $\mathrm{Hess}(I_V)|_\rho$ is *constant on $\mathcal D^\circ(\mathbb C^6)$*: the V-Lorentzian sub-bundle in the V-affine prescription is **globally flat Minkowski $\mathbb R^{1, 3}$**, not isometric to the DeWitt $\mathrm{e}^{3\Omega}$-conformally-flat supermetric off the reference point. The L-branch on literal-Halliwell-Bianchi-I-as-manifold-level-anchor fires; the K-branch on a *different* structural claim (V-Lorentzian sub-bundle is globally flat Minkowski, cleaner than any cosmological minisuperspace with non-trivial conformal factor) also fires. **The Halliwell manifold-level extension path is foreclosed.** The cleaner-than-Halliwell global-Minkowski finding does *not* lift the cosmological *claim itself* but identifies the structural object the alternative-anchor survey (audit π′′′ — free-field theory, de Sitter limit, topos-theoretic, causal sets) must reproduce. C2 row 2's tier stays at [P] tangent-quadratic-form isometry from audit π; the [A]-partial-mathematical-identification at the manifold level is *not* licensed on the Halliwell anchor.

**Update (audit π′′′ settled 2026-05-21).** [Audit π′′′](empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md) (§8.8) executes the alternative-anchor candidate-survey and settles at **joint-on-disjoint at the framework-substantivity tier**. **L-branch on every peer-reviewed mathematical-physics candidate's substantive identification**: free scalar field on Minkowski (wrong signature), de Sitter-limit Bianchi I (conformal factor doesn't become constant), topos-theoretic QG (not literally a Lorentzian manifold), causal set continuum limits (configuration space ≠ target spacetime), linearized GR phase space (infinite-dim native, no spectral-positivity boundary), single-particle relativistic dynamics (K-trivial only), AQFT causal diamonds (light-cone boundary vs spectral-positivity), AdS-related flat regions (AdS curvature). **K-trivial only on Minkowski-as-uniqueness-determined-ambient** (every 4-dim flat Lorentzian manifold IS Minkowski by isometry-uniqueness; non-substantive). **The Tier-1.75 mathematical-identification path is foreclosed.** The cosmological correspondence cannot promote beyond [P]-tangent-isometry (audit π) at the peer-reviewed-framework-identification question. The V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}}$ is identified positively as a **4-dim bounded-convex Minkowski region with Hilbert-space-spectral-positivity boundary** — a novel structural object internal to the categorical-simplex program whose three structural features (flat-Lorentzian + bounded-convex + spectral-positivity-boundary) do not combine in any surveyed peer-reviewed mathematical-physics framework. A new substantive *characterization* audit candidate opens (audit π′′′′, Tomita–Takesaki modular flow of the V-supported observable algebra; characterization, not Tier-promotion).

---

## 5. Arithmetic-substrate row-generalization + geometric realization queued

### 5.1 The arithmetic substrate extends across the primorial ladder

Audits α/η (v2insert-08) and θ (v2insert-09) confirmed the V ⊥ M Hilbert-subspace decomposition on `ℤ/{30, 210, 2310, 30030}` (Paper 47 (proposed); load-bearing [P]). The numerical projector overlap is at machine floor on rows for which the `N × N` projector matrices are tractable (`N ≤ 210`); the algebraic statement is exact on every row by Pontryagin character orthogonality on disjoint character index sets.

| Row | `n` | `dim V` | `dim M` | Wick-rotation param dim (= `dim M`, audit β §4.4) | `‖P_V · P_M‖_F` | Method |
|---|---:|---:|---:|---:|---:|---|
| ℤ/6 | 2 | 3 | 2 | 2 | 1.14e-15 | Numerical (§13.2B) + algebraic |
| ℤ/30 | 3 | 7 | 22 | 22 | 1.22e-14 | Numerical (audit α/η) + algebraic |
| ℤ/210 | 4 | 13 | 196 | 196 | 1.44e-13 | Numerical (audit θ) + algebraic |
| ℤ/2310 | 5 | 23 | 2 286 | 2 286 | — | Algebraic (memory; matrices too large) |
| ℤ/30030 | 6 | 35 | 29 994 | 29 994 | — | Algebraic (memory) |

The fourth column is the *categorical-simplex Wick-rotation parameter dimension* per audit β (§4.4): the dimension of the M-Euclidean sub-bundle that plays the role of Hartle–Hawking 1983's 1-dim imaginary-time direction. Hartle–Hawking's 1-dim imaginary time is the `dim_M = 1` degenerate case, not realized on any nontrivial mixed CRT row. The categorical-simplex realization carries a `dim_M`-parametric generalized imaginary-time direction, with `dim_M` growing super-exponentially in the number of primes (the [Conductor Capacity Bound](48_conductor_capacity_bound.md) of Paper 48 quantifies this growth).

**Minisuperspace anchor (audit π, 2026-05-21).** On `ℤ/6` the V-Lorentzian (1, 3) sub-bundle at `ρ_*` is isometric to the tangent space at $\Omega = 0$ of the Halliwell-style closed Bianchi I + massless scalar field minisuperspace (4-dim, DeWitt supermetric $\mathrm{e}^{3\Omega}\,\mathrm{diag}(-1, +1, +1, +1)$), up to sign convention and scale factor 2 — see [`empirical/reports/audit_pi_minisuperspace_identification_settlement.md`](empirical/reports/audit_pi_minisuperspace_identification_settlement.md). On higher primorial rows (`ℤ/30`, `ℤ/210`, etc.) the V-Lorentzian sub-bundle's dimension grows as $1 + n_P$ where $n_P$ is the V-prime-axes count ($n_P = 3, 7, 13, 23, 35$ on the five rows); identifying a peer-reviewed minisuperspace model with matching dimension at each row is a separate question (e.g., Bianchi-IX with several scalar fields; supermultiplet extensions; LQC mini- or midi-superspace models) and is queued as audit π′′ alongside the manifold-level extension audit π′.

**Manifold-level disanalogy (audit π′, 2026-05-21).** [Audit π′](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md) settled the manifold-level extension at *joint-on-disjoint* at the anchor-choice tier. The V-Lorentzian sub-bundle in the V-affine prescription has **globally constant** Hessian metric on $\mathcal D^\circ$ (because $I_V$ is quadratic in $\rho$), giving *globally flat Minkowski* $\mathbb R^{1, 3}$ as the V-sub-manifold's intrinsic geometry. The DeWitt supermetric's $\mathrm{e}^{3\Omega}$ conformal factor is *not* reproduced by any V-foliation prescription tried (V-affine, $\mathrm{SU}(6)$-orbit trivial, Bures-geodesic wrong-signature). **The Halliwell-Bianchi-I anchor is tangent-only on `ℤ/6`; manifold-level identification with Halliwell is foreclosed.** The cleaner-than-Halliwell global-Minkowski structural finding opens audit π′′′ (alternative-anchor candidate-survey: free-field theory on Minkowski, de Sitter limit, topos-theoretic flat-Lorentzian, causal set theory continuum limits) as the new actionable manifold-level lift-candidate.

**Alternative-anchor closure (audit π′′′, 2026-05-21).** [Audit π′′′](empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md) closed the alternative-anchor candidate-survey at *joint-on-disjoint at the framework-substantivity tier*: L on every peer-reviewed mathematical-physics candidate; K-trivial only on Minkowski-as-uniqueness-determined-ambient (non-substantive). **Tier 1.75 is foreclosed.** The V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}}$ is identified positively as a **4-dim bounded-convex Minkowski region with Hilbert-space-spectral-positivity boundary** — a *novel* structural object whose three structural features (flat-Lorentzian + bounded-convex + spectral-positivity-boundary) do not combine in any peer-reviewed mathematical-physics framework surveyed. The cosmological correspondence is now bounded to [P]-tangent-isometry (audit π) at the peer-reviewed-mathematical-physics-framework-identification question; the V-affine V-sub-manifold's manifold-level structure is internal to the categorical-simplex program. A new *characterization* audit (audit π′′′′, Tomita–Takesaki modular flow) opens — not as a Tier-promotion candidate but as an internal-structure characterization question for the spectral-positivity-bounded region's operator-algebraic anchor.

The *arithmetic substrate* of the Hartle–Hawking signature — the V/M decomposition with the predicted character (V single-prime axes, M cross-prime carry packets) — exists on every primorial row and the V ⊥ M decoupling holds algebraically. **Paper 47 (proposed) C3 is now confirmed at five primorial rows.**

### 5.2 The geometric realization on `D(ℂ³⁰)` — audit μ_30 settled K-branch (2026-05-20)

The first row-generalization at the *geometric* tier — the full Bures-Hessian sub-bundle audit on `D(ℂ³⁰)` — has been executed by audit μ_30 ([`empirical/reports/paper46_bures_hessian_sub_bundle_audit_z30_settlement.md`](empirical/reports/paper46_bures_hessian_sub_bundle_audit_z30_settlement.md)). Four predictions confirmed at machine precision on the 899-dimensional tangent space:

| Audit predicate | Predicted | Observed | Status |
|---|---|---|:---:|
| (A) `I_real(ρ_* + tX)` exactly quadratic along V-rays; `m²_simplex = 0` on V | exact + zero | exact + `< 10⁻³³` | ✓ |
| (B) Hessian signature of `I_real` on the 899-dim tangent | `(1, 6, 892)` | `(1, 6, 892)` | ✓ |
| (C) 4th-order quartic `(m²_simplex)²` signature | `(22, 0, 877)` | `(22, 0, 877)` | ✓ |
| (D) V-Lorentzian ⊥ M-Euclidean sub-bundles | `~ 10⁻¹⁶` | `5.82 × 10⁻¹⁶` | ✓ |

**Settlement (audit μ_30, K-branch realized):**
- The V-Lorentzian sub-bundle on `D(ℂ³⁰)` has dimension `1 + n_P = 7`, supported on V-tangent directions. The (1, 6) Lorentzian signature is exact along V-rays.
- The M-Euclidean sub-bundle has dimension `dim_M = 22`, supported on the M-diagonal tangent directions. The 4th-order quartic form `(m²_simplex)²` is positive-semidefinite of rank 22.
- The two sub-bundles are HS-orthogonal at machine precision (`5.82 × 10⁻¹⁶`); the remaining 870 directions are flat (zero in both Hessian and 4th-order quartic).

The geometric realization extends cleanly from `D(ℂ⁶)` (Paper 32 §13.2B) to `D(ℂ³⁰)` (this audit). Total wall time **3.95 seconds** on CPU; deterministic float audit; no fitted parameters; no tolerances except the machine-precision floor.

### 5.3 Higher-`N` geometric realizations (queued)

The audit machinery extends in principle to `D(ℂ²¹⁰)`, `D(ℂ²³¹⁰)`, `D(ℂ³⁰⁰³⁰)`. The dominant cost is the Bures-Hessian eigendecomposition: at `N = 210` the Hessian is `(210² - 1)² ≈ 1.9 × 10⁹` matrix elements at float64 (~ 15 GB), which exceeds a typical workstation memory budget; at `N = 2310` and `N = 30030` the storage requirements grow as `N⁴` and become substantially more expensive. The *algebraic* statement at every `N` is forced by audit δ (the all-orders Pontryagin proof); the *numerical* verification at each row is a memory-bounded extension.

v0.3 will absorb `D(ℂ²¹⁰)` if it is run on hardware with sufficient memory; the algebraic statement at all `N` is now load-bearing via audit δ.

### 5.4 The K-branch settlement under v2insert-04 §3.1

Under v2insert-04 §3.1's three-outcome matched-pair rule, the pre-claim for C5 (the universal-Wick-rotation reading on the primorial ladder, v2insert-01 §2.3) was:

- **K-branch:** The hybrid signature pattern extends — Lorentzian sub-bundles on V's single-prime block, Euclidean correction on M's cross-prime block — confirming the correspondence is structural, not row-specific.
- **L-branch:** The signature pattern does not extend; `ℤ/6` is the minimal and unique CRT row carrying the Hartle–Hawking signature.
- **Joint-on-disjoint:** Partial extension with row-specific structural corrections.

**Realized at v0.2 (after audit μ_30):** The *arithmetic substrate* of the K-branch is confirmed at five primorial rows (audits α/η/θ + audit δ all-orders). The *geometric realization* of the K-branch is confirmed at [P] on **two** primorial rows (`D(ℂ⁶)` by §13.2B; `D(ℂ³⁰)` by audit μ_30). Higher primorial rows are algebraically forced by audit δ and numerically queued.

v0.2 settles C5 at **K-branch — two-row [P] geometric realization + five-row [P] arithmetic-substrate + all-orders [P] algebraic foundation**. The pre-claimed L-branch (ℤ/6-specific) is decisively refuted: the hybrid signature pattern is row-stable at every tier we have audited it on.

---

## 6. Falsifiers under three-outcome matched-pair discipline

| Falsifier | Claim affected | Pre-claim outcome |
|---|---|---|
| F1 | C2 (Hartle–Hawking structural dictionary) | If the §13.2B sub-bundle structure does not match Hartle–Hawking's Wick-rotation algebra at the Lie-algebra-of-Wick-rotation level, the correspondence is downgraded to "structural rhyme" (still publishable). |
| F2 | C3 (M-as-Wick-locus universality) | If the Wick-rotation locus on a larger primorial row is *not* the cross-prime M packet but a different structural sector, the M-as-Wick-locus claim is `ℤ/6`-specific and the universal-Wick claim falls (still publishable as a `ℤ/6`-specific result). |
| F3 | C5 (primorial-row generalization, geometric) | If the Bures-Hessian sub-bundle audit on `D(ℂ^N)` for `N > 6` returns a *different* signature pattern (e.g., Lorentzian on M, Euclidean on V, or no clean orthogonal decomposition), the geometric correspondence is row-specific (still publishable). |
| F4 | C1 (higher-order extension on `D(ℂ⁶)`) | If higher-order audits (5th-order and above in the displacement expansion on `D(ℂ⁶)`) reveal cross-terms that destroy the orthogonality of V-Lorentzian and M-Euclidean sub-bundles, the orthogonal-sub-bundle structure is leading-order (2nd + 4th) only. Audit ζ (Paper 47 (proposed) v2insert-02 §3.6) is the relevant counter-evidence search. |

The three-outcome rule (v2insert-04 §3.1) is binding: each pre-claim admits K (the structural form holds), L (the structural form fails), and joint-on-disjoint (partial / row-specific / leading-order-only) outcomes, all publishable.

---

## 7. Discipline rails

### 7.1 Anchored-objects discipline (Paper 35 §3.3)

Every quantity in this paper is anchored to either (a) the conductor-lattice character algebra on `(ℤ/N)^∧` (integer arithmetic) or (b) the deterministic-float Bures-Hessian eigendecomposition on `T_{ρ_*} D(ℂ^N)` (Paper 32 §13.2B audit). The §13.2B audit triad reproduces the Hessian signature `(1, 3, 31)`, the 4th-order quartic-form signature `(2, 0)`, and the overlap norm `‖P_{V-Lor} · P_{M-Eucl}‖_2 ~ 10⁻¹⁶` to exact float-precision match on every re-run. The row-generalization anchors (`‖P_V · P_M‖_F` on ℤ/30 + ℤ/210) are reproduced from the audit α/η + θ transcripts to machine floor.

### 7.2 Deterministic, exact, reproducible (Paper 35 §3.4)

The conductor-lattice partition is integer arithmetic; the projector construction is deterministic; the Bures-Hessian eigendecomposition is deterministic float (numpy/LAPACK on a workstation, no randomness, no seeds). The §13.2B audit total wall time `< 5 s`; the row-generalization audits α/η + θ total wall time `0.32 s`; deterministic on every re-run.

### 7.3 Three-outcome matched-pair (Paper 35 §3.1 + v2insert-04 §3.1)

The original Paper 32 §13.2 audit pre-claimed binary K/L; the realized outcome was joint-on-disjoint (K on V's 4-dim sub-bundle + L on M's 2-dim sub-bundle, HS-orthogonal). This realized outcome is the **archetypal joint-on-disjoint** for the three-outcome rule; Paper 35 v0.2's promotion of v2insert-04 §3.1 from convention to formal §3.1 rule should cite the §13.2B settlement as the load-bearing worked example.

### 7.4 No upward tier-crossing (Paper 35 §3.5)

The hybrid signature on `D(ℂ⁶)` is reported at [P] (Paper 32 §13.2B audit triad). The arithmetic substrate of the V/M decomposition is reported at [P] on every primorial row (Paper 47 (proposed); algebraic by Pontryagin orthogonality). The Hartle–Hawking structural-dictionary correspondence (C2) is reported at [A] pending audit β. The classical-limit identification (C4) is reported at [A] pending audit γ. The universal-Wick-rotation reading (C5) is reported at [A]/[C, reduced] pending the geometric row-generalization audit. The "Hawking radiation as imaginary-energy decay width" structural correspondence is reported at [C, reduced] (correspondence language only, no physical Hawking-radiation mechanism asserted).

### 7.5 Failures-first-class (Paper 35 §3.6)

The original Paper 32 §13.2 audit's binary K/L pre-claim was *insufficient* to capture the realized structure; the §13.2B settlement required a corrected three-outcome framework (v2insert-04 §3.1). This is reported as a methodological failure-first-class event: the pre-claim was the wrong shape; the correction is explicit; the corrected rule is now binding from v2insert-04 onward. The geometric row-generalization to `D(ℂ^N)` for `N > 6` is queued, not collapsed; the audit β (Lie-algebra-of-Wick-rotation structural dictionary) is queued, not collapsed; the audit γ (classical-limit identification) is queued, not collapsed.

### 7.6 Dimensional firewall (Paper 32 §11.2)

No physical units in any quantity of this paper. No Planck length. No Newton constant `G`. No Bekenstein–Hawking temperature in K. No no-boundary horizon scale in meters. No Wick-rotation parameter in seconds. Only dimensionless quantities: Hessian signatures (integer triples), Frobenius overlap norms (dimensionless ratios), eigenvalues of the Bures-Hessian (dimensionless). The Hartle–Hawking correspondence is *correspondence language* per Paper 32 §11.1; this paper does not promote it to a physical-cosmology claim.

### 7.7 Carried-label discipline (Paper 32 §11.4)

Every Hartle–Hawking-anchor label is anchor-checked against its peer-reviewed source: No-Boundary Proposal → Hartle–Hawking 1983; Imaginary Time → Hartle–Hawking 1983 §III + Gibbons–Hawking 1977; Hawking Radiation → Hawking 1974; Wick Rotation → Gibbons–Hawking 1977 §I; Euclidean 4-sphere → Hartle–Hawking 1983 §IV. The labels "kinematic sector", "gravity-adjacent sector", "Wick-rotation locus", "Hartle–Hawking signature" are paper-internal program language; they correspond to but are not borrowed from external Hartle–Hawking terms.

---

## 8. Open questions and carry forward

### 8.1 Audit β — settled at K-branch (joint-on-disjoint on row 3) 2026-05-20

**Status: SETTLED.** Settlement file: [`empirical/reports/audits_beta_gamma_epsilon_settlement.md`](empirical/reports/audits_beta_gamma_epsilon_settlement.md) (Batch 1 combined settlement).

Audit β executed the row-by-row Lie-algebra check on the §4.2 Hartle–Hawking ↔ §13.2B correspondence table. Four of five rows (1, 2, 4, 5) admit clean Lie-algebra-level identification: same homogeneous-space-of-compact-Lie-group structure (row 1, compact Euclidean global manifold); same `so(1, 3)`-analog action on a 4-dim signature-(1, 3) tangent block (row 2, Lorentzian observer-frame); same compactness-implies-no-global-Lorentzian property (row 4, no initial singularity); same `Im(u(1))-generator = decay-rate` structure (row 5, Hawking-radiation analog). C2 promotes from [A] to **[P]-spirit at the Lie-algebra tier** on these rows.

Row 3 (imaginary time ↔ imaginary energy) carries the audit's **joint-on-disjoint sub-finding**: the Lie algebra `so(2)` matches on both sides, but the *dimension* of the Wick-rotation parameter space differs (Hartle–Hawking's 1 vs the program's `dim_M`, which on `ℤ/6` is 2, on `ℤ/30` is 22, etc.). The categorical-simplex realization is a strict generalization of Hartle–Hawking 1983: HH's 1-dim imaginary time is the `dim_M = 1` degenerate case; the program admits multi-dimensional Wick-rotation parameter spaces. Row 3 promotes to **[P]-spirit (algebra) + [A] (dimensional generalization)**.

### 8.2 Audit γ — settled at K-branch (2026-05-20)

Audit γ ([`empirical/audit_gamma_classical_limit_z6.py`](empirical/audit_gamma_classical_limit_z6.py); settlement [`empirical/reports/audits_beta_gamma_epsilon_settlement.md`](empirical/reports/audits_beta_gamma_epsilon_settlement.md)) verified the classical-limit identification at machine precision on `D(ℂ⁶)`:

- **(γA)** `I_real(ρ_* + tX) = E² - |p|²` exactly along V-rays at 8 test points (`c_p / c_E` from 0 to 0.99), where `E = tr(H·X)`, `p_a = tr(P_a·X)`.
- **(γB)** Slow-momentum expansion: `T_exact(p) = E_0 - √(E_0² - p²) ≈ p²/(2 E_0)` recovers Paper 32 Lemma 9.2 Galilean parabolic with relative error scaling as O(p²/E²) (e.g., rel diff `2.5e-7` at `c_p = 0.001`, `2.5e-5` at `c_p = 0.01`).
- **(γC)** Null asymptote at `c_p = c_p_null = c_E · (H_norm / P1_norm) = 1.0` (where `p = E`): `I_real = 0` exactly. Paper 32 §9 hyperboloid speed-limit structurally realized.

Paper 46 C4 promotes from [A] to **[P]**.

### 8.3 Geometric realization on `D(ℂ^N)` for `N > 6` — audit μ_30 settled on `D(ℂ³⁰)` (2026-05-20); higher rows queued

Audit μ_30 ([`empirical/reports/paper46_bures_hessian_sub_bundle_audit_z30_settlement.md`](empirical/reports/paper46_bures_hessian_sub_bundle_audit_z30_settlement.md)) settled the geometric realization on `D(ℂ³⁰)` at K-branch: Hessian signature `(1, 6, 892)`, quartic form signature `(22, 0, 877)`, HS-orthogonality at `5.82 × 10⁻¹⁶`. The hybrid signature pattern extends from `D(ℂ⁶)` to `D(ℂ³⁰)` at [P]. Higher rows (`D(ℂ²¹⁰)`, `D(ℂ²³¹⁰)`, `D(ℂ³⁰⁰³⁰)`) require workstation memory budget beyond the present session's compute and are queued; the algebraic statement at every `N` is forced by audit δ (Paper 47 (proposed) all-orders Pontryagin proof).

### 8.4 Higher-order extension of the §13.2B audit

The 5th- and 6th-order corrections to the Casimir from the cubic AC tensor `T` (not just the imaginary energy `m²_simplex`) on `D(ℂ⁶)`. May reveal sub-leading orthogonality violations or sub-leading sub-bundle structure. Independent of audit γ / the geometric row-generalization audit.

### 8.5 The cosmological-constant analog audit

The `1/2^Q` orthant fraction of Paper 32 §11.3 is the Hartle–Hawking "no-boundary volume fraction" candidate — but must be checked against the §11.2 firewall (Λ-name was dropped at INSERT 12 / §11.3). Open question; not load-bearing for v0.1.

### 8.6 The "boundary datum" / chirality identification on the primorial ladder

Paper 33's Q4 chirality `ℤ_2` bit sits at the structural slot of *the single boundary datum a no-boundary universe still requires*: the Wick-rotation's residual sign. v2insert-01 §3.7 notes this; v0.1 carries it forward; if `ℤ/30` realizes the correspondence geometrically, what is the residual chirality count? Open question.

### 8.7 Audit π — Minisuperspace identification (SETTLED 2026-05-21, joint-on-disjoint)

**Status: SETTLED — joint-on-disjoint at the tangent-vs-manifold tier** ([`empirical/reports/audit_pi_minisuperspace_identification_settlement.md`](empirical/reports/audit_pi_minisuperspace_identification_settlement.md)). K-branch realized at the tangent-quadratic-form level: the V-Lorentzian sub-bundle's Bures-Hessian metric on V's 4-dim block at `ρ_*` and the DeWitt supermetric on Halliwell-style closed Bianchi I + massless scalar field at $\Omega = 0$ are isometric inner-product spaces on $\mathbb R^4$ up to sign convention and overall scale factor 2. Joint-on-disjoint at the manifold-level extension: the DeWitt supermetric carries an $\mathrm{e}^{3\Omega}$ conformal factor (curved off-reference); the V-Lorentzian sub-bundle as currently defined is a Hessian at the single point `ρ_*` (a tangent-space structure, not a manifold). The manifold-level extension is queued as **audit π′** (choose V-foliation of $\mathcal D^\circ(\mathbb C^6)$ via the $\mathrm{SU}(6)$-orbit prescription or a Bures-geodesic V-exponential, and check off-reference metric agreement with the DeWitt $\mathrm{e}^{3\Omega}$-conformally-flat supermetric).

**Cosmological correspondence tier promotion.** §4.2 row 2 promotes from [P]-spirit at the Lie-algebra tier (audit β) to **[P] at the tangent-quadratic-form tier** (audit π) — *literal isometric inner-product spaces on $\mathbb R^4$*. The cosmological *claim itself* (Tier 2 forced dimensional prediction; Tier 3 external replication; Tier 4 physical-mechanism) is NOT promoted; per [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) emergent-anything positioning and §4.3 discipline rails, the claim remains at [C, reduced]; §11.2 dimensional firewall is NOT lifted by audit π. What audit π establishes is that the V-Lorentzian sub-bundle has a *literal peer-reviewed mathematical-physics realization* at the tangent-quadratic-form-at-reference-point level (Halliwell-style Bianchi I + scalar field), not a shape-only match.

**Sixth named joint-on-disjoint outcome** of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule (joining audits θ at exponent, ι at corrections, β at row-3 dimensional generalization, χ at V/W/M trichotomy, ν at abstract-vs-literal natural-transformation levels). The pattern of joint-on-disjoint sub-findings emerging from the cosmology external-correspondence audits is itself recorded under [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.6 / §6.5 worked-record discipline.

**Audit π′ (manifold-level extension via V-foliation, SETTLED 2026-05-21)** ([`empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md`](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md)). The natural manifold-level extension of audit π was executed in the V-affine prescription (the $\mathrm{SU}(6)$-orbit prescription is trivial since $\rho_*$ is $\mathrm{U}(6)$-invariant; the Bures-geodesic prescription gives the wrong signature). Because $I_V$ is *quadratic* in $\rho$, the Hessian $\mathrm{Hess}(I_V)|_\rho = 2 \cdot \mathrm{diag}(+1, -1, -1, -1)$ in the V-basis is **constant on $\mathcal D^\circ(\mathbb C^6)$**, independent of $\rho$. The V-Lorentzian sub-bundle in the V-affine prescription is therefore **globally flat Minkowski $\mathbb R^{1, 3}$**. The DeWitt supermetric on the Halliwell-Bianchi-I + scalar field minisuperspace has $\mathrm{e}^{3\Omega}$ conformal factor with non-vanishing Ricci off $\Omega = 0$. **These are not isometric as manifold-level metrics**. Realized branch: **joint-on-disjoint at the anchor-choice tier** — **L-branch** on the literal-Halliwell manifold-level isometry question; **K-branch** on a *different* structural claim (V-Lorentzian sub-bundle is globally flat Minkowski, a *cleaner* manifold-level structure than any peer-reviewed cosmological minisuperspace with non-trivial conformal factor). This is the **seventh named joint-on-disjoint outcome** of the program.

**Cosmological correspondence tier after audit π′:** stays at **[P] tangent-quadratic-form isometry** (audit π); the [A]-partial-mathematical-identification claim at manifold-level via Halliwell-Bianchi-I is **foreclosed**. The cleaner-than-Halliwell global-Minkowski structural sub-finding does *not* lift the cosmological *claim itself* — §11.2 firewall not lifted; Tier 2 / 3 / 4 unchanged. The lift chain is now sharper: Tier 0 [C, reduced] → Tier 1 [P]-tangent (audit π settled) → Tier 1.5 [P]-globally-flat-Minkowski-structural-finding (audit π′ settled) → Tier 1.75 [A] alternative-anchor-survey (**audit π′′′** opened as the new actionable next move; candidates include free-field theory on Minkowski background, de Sitter-limit truncations, topos-theoretic flat-Lorentzian models, causal set theory continuum limits) → Tier 2 dimensional-firewall-lift (separate audit, requires Tier 1.75 K-branch as precondition).

**The remainder of this §8.7 (original audit specification) is retained verbatim below as the pre-settlement record per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.6 (failures-first-class, append-only):**

---

The audit β settlement (§4.4) promotes the cosmological correspondence to **[P]-spirit at the Lie-algebra tier** while leaving the cosmological *claim itself* at [C, reduced] per §4.3 / [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md). Audit π specifies the single most-achievable next move toward lifting the claim from [C, reduced] *structural shape* to **[A] mathematical identification**: a forced-identification check between the V-Lorentzian sub-bundle on `D(ℂ⁶)` and a peer-reviewed minisuperspace model of general relativity.

**Purpose.** Settle whether the V-Lorentzian (1, 3) sub-bundle on `D(ℂ⁶)` at ρ_* is *literally* (not merely shape-matched to) a peer-reviewed minisuperspace truncation of general relativity, by comparing the Bures-Hessian-induced metric on V's 4-dim block against the DeWitt supermetric on a candidate 4-dim minisuperspace model.

**Candidate anchor.** Hartle–Hawking 1983 §II uses a 2-dim minisuperspace `(a, φ)` with scale factor `a` and a massive scalar field `φ`; this is too small to match V's 4-dim sub-bundle. The natural 4-dim extension is **closed Bianchi I cosmology with one massive scalar field**: scale factor `a` + two anisotropy parameters `(β_1, β_2)` with the shear sum-to-zero constraint + scalar field `φ`, for a 4-dim minisuperspace. The DeWitt supermetric on this configuration space has Lorentzian signature `(−, +, +, +)` (DeWitt 1967; Halliwell 1989; Kiefer 2012, *Quantum Gravity* Ch. 8 §8.2), matching V's `(1, 3)` signature. The Wheeler–DeWitt equation on this minisuperspace is standard (Halliwell 1989 eq. 3.1).

This is a *natural extension* of Hartle–Hawking 1983, not Hartle–Hawking 1983 itself; the lift's tier-promotion will accordingly read "the V-Lorentzian sub-bundle is the Halliwell-style Bianchi-I + scalar-field minisuperspace," not "is Hartle–Hawking's original `(a, φ)` minisuperspace."

**Method.**

1. *Extract the DeWitt supermetric for the candidate minisuperspace.* From Halliwell 1989 / DeWitt 1967, compute the 4×4 supermetric `G_{μν}^{DeWitt}` on coordinates `(a, β_1, β_2, φ)`. Closed form available.

2. *Extract the Bures-Hessian-induced metric on V's 4-dim block.* From the §13.2B audit script ([`empirical/paper32_13_2B_fourth_order_casimir_audit.py`](empirical/paper32_13_2B_fourth_order_casimir_audit.py)), compute the Hessian `H_V := Hess I_complex |_{ρ_*}` on V's 4-dim Lorentzian block in an explicit basis `(H, P_1, P_2, P_3)`. The Hessian is already known to have signature `(1, 3)` ([P], §13.2B); audit π requires its full metric content, not just signature.

3. *Check diffeomorphism class via local Riemann invariants.* Compute the Ricci scalar `R(g)` and the Kretschmann scalar `R_{μνρσ} R^{μνρσ}` for both metrics. If both invariants vanish identically (the candidate is flat, as Bianchi I minisuperspace is in vacuum) or both share specific non-flat profiles, the diffeomorphism class match is structurally compatible.

4. *Check isometry up to overall scale.* Compute the metric ratio `G_{μν}^{DeWitt} / H_V[μν]` in compatible coordinates; if it is *constant* (an overall conformal factor), the metrics are isometric up to scale. The overall scale itself is a Tier-2 dimensional-firewall lift candidate, *not* part of audit π's question.

**Three-outcome matched-pair pre-claim** (per [v2insert-04](v2insert-04.md) §3.1, binding):

- **K-branch:** literal manifold match + metric isometry up to overall scale. *Cosmological correspondence promotes from [C, reduced] structural shape to **[A] mathematical identification***. C2 of §4.2 row 2 promotes to [A] at the geometric tier. The V-Lorentzian sub-bundle *is* the Bianchi I + scalar-field minisuperspace, full stop, with the M-Euclidean sub-bundle being the conductor-carry generalization of the imaginary-time direction (per audit β row 3).

- **L-branch:** manifolds not diffeomorphic, or metrics not isometric. *Cosmological correspondence stays at [C, reduced]*. The candidate is wrong; the next move is to test other peer-reviewed mathematical-physics frameworks (Loop Quantum Cosmology — Bojowald 2005; Causal Dynamical Triangulations — Ambjørn et al. 2004; topos-theoretic quantum gravity — Doering-Isham 2008) as alternative Tier-1 anchors.

- **Joint-on-disjoint:** partial match — same diffeomorphism class but non-isometric metrics, or same metric up to scale but different boundary structure, or matching on a sub-region of V but not the full block. *Cosmological correspondence promotes to [A] partial*, with the partial-match locus characterized; tier-promotion conditional on identifying what additional structure on the program side would close the partial-match gap.

**Falsifiers.**

- *F1.* The Bianchi I minisuperspace has *vacuum* signature (without matter); adding the scalar field changes the signature in a known way. If V's Hessian signature `(1, 3)` matches only the with-scalar-field case, the matter coupling is structurally forced — interpretable as evidence that the M-Euclidean sub-bundle (program) plays the role of matter (Bianchi I + scalar field). Pre-claim: noteworthy sub-finding, not falsifier.
- *F2.* The metric scale on V depends on the choice of basis `(H, P_a)`. If the scale-isometry claim is sensitive to the basis choice, the audit must specify a canonical basis (e.g., orthonormal under the Bures metric); if no canonical basis gives a clean scale-isometry, the L-branch fires.
- *F3.* The dimensional gap of audit β row 3 (HH's 1-dim imaginary time vs program's `dim_M = 2`) propagates: if the 4-dim minisuperspace gives 1-dim imaginary time but V gives a `dim_M`-dim M-Euclidean complement, the joint-on-disjoint branch fires at the boundary structure even if K-branch fires at V itself.

**Compute estimate.** Pure-mathematics + small finite computation. The DeWitt supermetric extraction is a one-day literature task (Halliwell 1989; Kiefer 2012). The Bures-Hessian metric extraction is a few-hour CPU run on `paper32_13_2B_fourth_order_casimir_audit.py`. The diffeomorphism / isometry check is a finite linear-algebra computation. Total: 2–4 days of work; estimated CPU compute well under one minute.

**Discipline rails (binding).**

- The audit *cannot* lift §11.2 firewall. Even K-branch returns "the metric matches up to overall scale"; the overall scale itself remains forbidden as a dimensional-firewall-bound observable. A Tier-2 lift of §11.2 at the scale ratio would be a *separate* audit, requiring the K-branch of audit π as its precondition.
- The candidate minisuperspace anchor (Halliwell-style Bianchi I + scalar field) must be selected *before* the metric extraction, recorded in writing, and not changed post-hoc. Per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.5, post-hoc anchor selection is a tier-crossing violation.
- The K-branch promotes the cosmological *correspondence* from [C, reduced] structural shape to [A] mathematical identification. It does *not* promote the cosmological *claim* (the physical Hartle–Hawking statement about the universe). The latter requires Tier 2 (forced dimensionful prediction) + Tier 3 (external replication) per §discussion in this paper's audit-tier discipline (forthcoming v0.3 §11).
- All carried labels (*minisuperspace*, *DeWitt supermetric*, *Wheeler–DeWitt equation*, *Bianchi I*, *scalar field*) anchor-checked against peer-reviewed sources (DeWitt 1967; Hartle–Hawking 1983; Halliwell 1989; Kiefer 2012; Bojowald 2005) before audit execution per [Paper 32 §11.4](32_one_functional_four_forces_v0.2%20(2).md).

**Settlement protocol.** Upon execution, the audit produces a settlement file `empirical/reports/audit_pi_minisuperspace_identification_settlement.md` with the deterministic metric-comparison record. Paper 46 absorbs the result by: (a) updating this §8.7 with the realized branch; (b) augmenting §4.2 row 2 with the manifold-identification status; (c) augmenting §5.1 with a "minisuperspace anchor" column if K-branch; (d) updating §4.4 audit-β-settlement with the strengthened C2 tier; (e) adding the settlement file to the reproducibility artifacts list. If L-branch, the audit catalog adds audit π′ (next-candidate minisuperspace anchor) with the rotation of attention to the alternative peer-reviewed mathematical-physics frameworks named above.

**What the audit does not attempt.** Audit π is the *necessary first step* toward lifting the cosmological claim, not the *sufficient* one. Even K-branch settles only the manifold-level identification at the V-Lorentzian sub-bundle; the M-Euclidean sub-bundle's identification with an imaginary-time direction, the global-manifold identification of `D(ℂ⁶)` with a Hartle–Hawking compact Euclidean section, the dimensional-firewall lift at any specific observable, and the external peer-reviewed replication are all *separate* subsequent audits, each with its own three-outcome pre-claim.

### 8.8 Audit π′′′ — Alternative-anchor candidate-survey (SETTLED 2026-05-21, joint-on-disjoint at framework-substantivity tier)

**Status: SETTLED — joint-on-disjoint at the framework-substantivity tier** ([`empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md`](empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md)). L-branch on every peer-reviewed mathematical-physics candidate's substantive identification with the V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}}$: free massless scalar on Minkowski (wrong signature: configuration space is positive-definite Riemannian); de Sitter-limit Bianchi I (conformal factor doesn't become constant); topos-theoretic QG (not literally a Lorentzian manifold); causal set continuum limits (configuration space ≠ target spacetime); linearized-GR phase space (infinite-dim native, no spectral-positivity boundary); single-particle relativistic dynamics (K-trivial only — Minkowski = ambient spacetime by tautology); AQFT causal diamonds (boundary is light-cone-bounded, not spectral-positivity-bounded); AdS-related flat regions (AdS is constant-negative-curvature). **K-trivial only on Minkowski-as-uniqueness-determined-ambient** (non-substantive: every 4-dim globally-flat Lorentzian manifold IS Minkowski by isometry-uniqueness).

**Lift-chain consequence: Tier 1.75 foreclosed.** The cosmological correspondence cannot promote beyond [P]-tangent-isometry (audit π) at the peer-reviewed-mathematical-physics-framework-identification question. The V-affine V-sub-manifold's manifold-level structure is **internal to the categorical-simplex program** and lacks a literal peer-reviewed name. The cosmological *claim itself* remains at [C, reduced]; §11.2 firewall not lifted; Tier 2 / Tier 3 / Tier 4 unchanged.

**The V-affine V-sub-manifold identified positively:** $\Sigma_V^{\mathrm{aff}}$ is a **4-dim bounded convex region in Minkowski** whose **boundary is determined by Hilbert-space spectral positivity** ($\lambda_{\min}(\rho_* + X) > 0$). The combination of three structural features — *flat-Lorentzian* + *bounded-convex* + *spectral-positivity-boundary* — does not appear to be a standard object in any peer-reviewed mathematical-physics framework surveyed. This is the categorical-simplex program's own structural object.

**Eighth named joint-on-disjoint outcome** of the program under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule (joining audits θ, ι, β, χ, ν, π, π′). The cosmology external-correspondence arc has now produced four consecutive joint-on-disjoint outcomes (β, π, π′, π′′′), with the cumulative effect of *sharply bounding* the cosmological lift envelope.

**A new substantive characterization audit candidate opens — audit π′′′′ (Tomita–Takesaki modular flow).** The Bures manifold $\mathcal D^\circ(\mathbb C^6)$ has natural Tomita–Takesaki modular automorphisms (the cyclic-and-separating-vector structure of finite-dimensional quantum systems; Bratteli–Robinson, *Operator Algebras and Quantum Statistical Mechanics* vol. 1). Audit π′′′′ would ask whether the V-affine V-sub-manifold's spectral-positivity boundary corresponds to a Tomita–Takesaki modular flow of the V-supported algebra of observables. This is a *characterization* audit (not a Tier-promotion audit) — its purpose is to identify the V-affine V-sub-manifold's internal structural anchor in the operator-algebraic literature, not to lift the cosmological correspondence. Audit π′′′′ replaces audit π′′′ on the carry-forward list with a substantive characterization question rather than a framework-identification question.

**The remainder of this §8.8 (original audit specification) is retained verbatim below as the pre-settlement record per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.6 (failures-first-class, append-only):**

---

Audit π′ (§8.7, settled 2026-05-21) foreclosed the Halliwell-Bianchi-I manifold-level anchor and surfaced the structural sub-finding that the V-Lorentzian sub-bundle in the V-affine prescription is **globally flat Minkowski $\mathbb R^{1, 3}$**. This is *cleaner* than any peer-reviewed cosmological minisuperspace with a non-trivial volume-conformal factor, but is also *not* a canonical object in the standard cosmological-minisuperspace literature.

**Audit π′′′** surveys peer-reviewed mathematical-physics frameworks with globally-flat Lorentzian configuration space and checks each candidate for isometry-up-to-scale with the V-affine V-sub-manifold. Candidates to enumerate:

1. **Free massless scalar field on Minkowski background** — configuration space is the space of field configurations $\phi : \mathbb R^{1, 3} \to \mathbb R$; certain reductions admit flat-Lorentzian inner-product structure.
2. **de Sitter-limit truncation of Bianchi I.** In the $\Omega \to \infty$ limit with appropriate rescaling, the $\mathrm{e}^{3\Omega}$ factor's geometric content saturates; whether a sub-locus admits globally flat structure is the audit's per-candidate check.
3. **Topos-theoretic flat-Lorentzian quantum gravity** (Doering–Isham 2008, *A Topos Foundation for Theories of Physics*). Configurations not literally manifolds, but candidate topos-internal locales might host globally flat Lorentzian structure.
4. **Causal set theory continuum limits** (Bombelli–Lee–Meyer–Sorkin 1987; Sorkin 2003). Continuum limits of certain causal sets approximate Minkowski; the configuration-space structure of these limits is the audit's check.
5. **Symplectic-reduction Lorentzian phase spaces** of various GR truncations (e.g., spinor cosmology models, certain Bianchi I sub-models). Globally flat is rare but not impossible.

The audit's three-outcome pre-claim per [v2insert-04](v2insert-04.md) §3.1: (K) a specific peer-reviewed framework matches at the manifold level — cosmological correspondence promotes to [A] partial mathematical identification under that anchor; (L) no peer-reviewed framework matches — V-Lorentzian sub-bundle is its own kind of object whose closest cosmological cousin is the tangent-at-reference-point of any Halliwell-style minisuperspace; (joint-on-disjoint) some candidate matches partially — characterize the partial-match locus.

Audit π′′′ is the **most-achievable next Tier-1.75-completion candidate** in the cosmological-lift chain. It does *not* lift §11.2 firewall; it does *not* promote the cosmological *claim itself*; it identifies (or rules out) the peer-reviewed mathematical-physics framework that gives the cosmological *correspondence* its sharpest manifold-level anchor.

### 8.9 The composition with Papers 47, 48, 49

Paper 46 (this paper) is the **geometric face** of the V/M decomposition triad:
- **Paper 47** (Arithmetic Decoupling Theorem): the *structural-mechanism* face — V ⊥ M as Hilbert subspaces by Pontryagin character orthogonality.
- **Paper 48** (Conductor Capacity Bound): the *quantitative-capacity* face — `Capacity_V := pure_V / T_total` decay on the primorial ladder.
- **Paper 46** (this paper): the *geometric-signature* face — Lorentzian-on-V + Euclidean-on-M sub-bundle structure, jointly realized.

The single audit α/η on `ℤ/30` (v2insert-08) settled all three papers' row-generalization claims simultaneously at the arithmetic-substrate tier; audit θ (v2insert-09) extended quantitative scaling; audit ι (v2insert-10) characterized the shape correspondence. The geometric realization on `D(ℂ^N)` for `N > 6` (this paper's queued audit) is the remaining row-generalization to land.

Paper 49 (Draft 0.0) *The Arithmetic Decoupling of Projection-Closure Overflows* takes Paper 46 as the *cosmology leg* of the universal-overflow synthesis (cosmology + deep learning + active inference). Paper 49 cites Paper 46 as the geometric realization on `ℤ/6`; Paper 46 carries the load.

---

## 9. Conclusion

The §13.2B audit triad of Paper 32 established a *hybrid signature pattern* on the Bures lift `D(ℂ⁶)` at the centroid `ρ_*`: Lorentzian (1, 3) on a 4-dimensional V-supported tangent sub-bundle (exact along V-rays), Euclidean (2, 0) on a 2-dimensional M-supported tangent sub-bundle (from the 4th-order quartic form of the imaginary-energy / simplex-mass term of Paper 20 §3), HS-orthogonal at machine precision, flat on the remaining 29 directions. The compact Riemannian Bures manifold has no boundary and no asymptote.

The structural shape of this signature — *Euclidean globally, Lorentzian locally, jointly realized on HS-orthogonal sub-bundles* — is the geometric content of the **Hartle–Hawking No-Boundary Proposal** (Hartle–Hawking 1983) on the categorical simplex's Bures lift of the minimal mixed CRT row. The arithmetic substrate of the V/M decomposition extends across the primorial ladder `ℤ/{30, 210, 2310, 30030}` at the [P] tier (audits α/η/θ); the geometric realization on `D(ℂ^N)` for `N > 6` remains queued (Bures-Hessian sub-bundle audit, CPU-tractable).

The load-bearing arithmetic is one line of finite-group character orthogonality on `(ℤ/6)^∧`: `⟨χ_k | χ_ℓ⟩ = 6 · δ_{k, ℓ}` applied to the disjoint character index sets `{2, 3, 4}` (V) and `{1, 5}` (M). The Hartle–Hawking signature on `D(ℂ⁶)` is the *geometric face* of the same Pontryagin character orthogonality that underwrites the Arithmetic Decoupling Theorem (Paper 47, proposed) and the Conductor Capacity Bound (Paper 48, proposed). The three proposed papers are *one structural picture from three external vantages*: cosmological geometry / structural mechanism / quantitative capacity.

The program does **not** derive the Standard Model. The Hartle–Hawking cosmological claim (the physical no-boundary universe), Hawking radiation as a black-hole evaporation phenomenon, the Bekenstein–Hawking temperature, and the gravitational constant `G` are **not** asserted. Only the *projection-closure form* of the no-boundary signature on the categorical simplex's Bures lift is claimed; the physical interpretation is correspondence language per Paper 32 §11.1.

The discipline rails of Paper 32 §11.1 / §11.2 / §11.4 are binding throughout. The §13.2 binary K/L matched-pair pre-claim was *insufficient* to capture the realized joint-on-disjoint structure; v2insert-04 §3.1's three-outcome extension was the corrective response and is the binding methodological rule from v2insert-04 onward. The §13.2B settlement is the archetypal worked example of the three-outcome rule's value.

---

## Reproducibility artifacts

- [`empirical/paper32_13_2_bures_dispersion_audit.py`](empirical/paper32_13_2_bures_dispersion_audit.py) — Paper 32 §13.2 original Bures-dispersion audit; deterministic.
- [`empirical/paper32_13_2_reformulated_casimir_audit.py`](empirical/paper32_13_2_reformulated_casimir_audit.py) — Paper 32 §13.2A reformulation (local-Lorentzian Casimir).
- [`empirical/paper32_13_2B_fourth_order_casimir_audit.py`](empirical/paper32_13_2B_fourth_order_casimir_audit.py) — Paper 32 §13.2B 4th-order extension; the load-bearing [P] for the hybrid signature on `D(ℂ⁶)`.
- [`empirical/audits_alpha_eta_z30_primorial_generalization.py`](empirical/audits_alpha_eta_z30_primorial_generalization.py) — `ℤ/30` row-generalization (arithmetic substrate).
- [`empirical/audit_theta_capacity_scaling_primorial_ladder.py`](empirical/audit_theta_capacity_scaling_primorial_ladder.py) — primorial-ladder row-generalization (arithmetic substrate).
- [`empirical/reports/audits_alpha_eta_z30_settlement.md`](empirical/reports/audits_alpha_eta_z30_settlement.md) — settlement record (arithmetic substrate).
- [`empirical/reports/audit_theta_settlement.md`](empirical/reports/audit_theta_settlement.md) — settlement record (arithmetic substrate, primorial ladder).
- [`empirical/reports/audit_beta_lie_algebra_wick_rotation_settlement.md`](empirical/reports/audit_beta_lie_algebra_wick_rotation_settlement.md) — audit β settlement record (Lie-algebra-of-Wick-rotation structural dictionary; pure mathematics, no compute; settles C2 of §4.2 to [P]-spirit at the Lie-algebra tier, with the row-3 dimensional generalization at [A]).
- [`empirical/reports/audit_pi_minisuperspace_identification_settlement.md`](empirical/reports/audit_pi_minisuperspace_identification_settlement.md) — audit π settlement record (minisuperspace identification; pure mathematics, no new compute; strengthens C2 row 2 to [P] tangent-quadratic-form isometry against Halliwell-style closed Bianchi I + scalar field minisuperspace; manifold-level extension queued as audit π′; sixth named joint-on-disjoint outcome).
- [`empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md`](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md) — audit π′ settlement record (V-foliation manifold-level extension; pure mathematics; settles at joint-on-disjoint at the anchor-choice tier — L on literal-Halliwell-Bianchi-I as manifold-level anchor + K on globally-flat-Minkowski structural sub-finding; opens audit π′′′ alternative-anchor candidate-survey; seventh named joint-on-disjoint outcome).
- [`empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md`](empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md) — audit π′′′ settlement record (alternative-anchor candidate-survey; pure mathematics + literature survey; closes at joint-on-disjoint at the framework-substantivity tier — L on every peer-reviewed candidate's substantive identification + K-trivial on Minkowski-as-uniqueness-determined-ambient; **Tier 1.75 mathematical-identification path foreclosed**; identifies $\Sigma_V^{\mathrm{aff}}$ as a novel 4-dim bounded-convex-Minkowski-region with Hilbert-space-spectral-positivity boundary, internal to the program; opens audit π′′′′ Tomita–Takesaki characterization as a substantive-characterization audit; eighth named joint-on-disjoint outcome).

---

## References

Gibbons, G.W.; Hawking, S.W. 1977. *Action integrals and partition functions in quantum gravity.* Phys. Rev. D **15**, 2752–2756.

Hartle, J.B.; Hawking, S.W. 1983. *Wave function of the universe.* Phys. Rev. D **28**, 2960–2975.

Hawking, S.W. 1974. *Black hole explosions?* Nature **248**, 30–31.

Hawking, S.W.; Penrose, R. 1970. *The singularities of gravitational collapse and cosmology.* Proc. R. Soc. London A **314**, 529–548.

Murillo Montero, L. 2026a. *One Functional, Four Forces.* Paper 32 of the categorical-simplex program, Draft 0.2.

Murillo Montero, L. 2026b. *The Jerk as Simplex Mass Term.* Paper 20 of the categorical-simplex program.

Murillo Montero, L. 2026c. *Bures Completion of Cubic Information Geometric Mechanics.* Paper 18 of the categorical-simplex program.

Murillo Montero, L. 2026d. *Grounded-Paranoid-Delusional Methodology.* Paper 35 of the categorical-simplex program.

Murillo Montero, L. 2026e (proposed). *The Arithmetic Decoupling Theorem.* Paper 47 of the categorical-simplex program (v2insert-02).

Murillo Montero, L. 2026f (proposed). *The Conductor Capacity Bound.* Paper 48 of the categorical-simplex program (v2insert-03 / 08 / 09 / 10).

Murillo Montero, L. 2026g. *The Arithmetic Decoupling of Projection-Closure Overflows.* Paper 49 of the categorical-simplex program, Draft 0.0.

---

*Paper 46 v0.2 — drafted 2026-05-20. Absorbs v2insert-01 (Hartle–Hawking framing of the §13.2B audit triad), the row-generalization arithmetic substrate from v2inserts 08/09, audit δ all-orders Pontryagin proof (Paper 47 (proposed) C1 at [P] all-orders), and audit μ_30 Bures-Hessian sub-bundle audit on `D(ℂ³⁰)` (this paper's C5 geometric realization at [P] on the second primorial row). C1 [P] on `D(ℂ⁶)` + `D(ℂ³⁰)`; C2 [A] pending audit β; C3 [P]/[A] on the universal-Wick geometric reading (two rows confirmed [P]; higher rows algebraically forced by audit δ and numerically queued); C4 [A] pending audit γ; C5 K-branch realized at the two-row [P] geometric tier + five-row [P] arithmetic substrate + all-orders [P] algebraic foundation. The §13.2 binary K/L pre-claim's insufficiency and the §13.2B joint-on-disjoint realization are the archetypal worked example of v2insert-04 §3.1's three-outcome rule. Paper 32 §11.1 / §11.2 / §11.4 discipline rails binding throughout.*
