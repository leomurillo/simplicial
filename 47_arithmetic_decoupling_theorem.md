# 47. The Arithmetic Decoupling Theorem

**Character Orthogonality as Gravity-Kinematics Quarantine on the Categorical Simplex**

**Leonardo Murillo Montero**
*leonardo.murillo@gmail.com*

*Draft 0.3 — 2026-05-20*

**Tier tags.** [P] for the V ⊥ M Hilbert-subspace decomposition of `ℂ^N` on every squarefree primorial row `N = P_n` (Pontryagin character orthogonality on `(ℤ/N)^∧`). [P] for the HS-orthogonality of the V-Lorentzian (1,3) and M-Euclidean (2,0) sub-bundles of `D(ℂ⁶)`'s tangent at the centroid at 2nd and 4th orders (Paper 32 §13.2B audit triad, machine-floor overlap `~10⁻¹⁵`). [P] for the row-generalization to `ℤ/{30, 210, 2310, 30030}` (audits α/η of v2insert-08, audit θ of v2insert-09). [P] for the all-orders extension on every squarefree primorial row (audit δ, 2026-05-20). [P] for the geometric realization on `D(ℂ³⁰)` (audit μ_30, 2026-05-20). **[P] for the extension to ℤ/10 (squarefree non-primorial) and ℤ/12 (non-squarefree)** at the Bures-Hessian sub-bundle tier (audit χ, 2026-05-20: K-branch on `D(ℂ¹⁰)`; K-branch on `D(ℂ¹²)` for both strict and inclusive V/M; **joint-on-disjoint** on the V/W/M trichotomy at the tangent tier with W ⊥ M overlap 0.447). **[P]-spirit for the QG-mixing-bypass structural-dictionary correspondence** at the Lie-algebra-of-decoupling level (audit ε, 2026-05-20: dictionary established row-by-row; correspondence language per Paper 32 §11.1).

**Anchor manuscripts.** Paper 32 *One Functional Four Forces* §6.2 Lemma 6.1a–c (load-bearing [P] for the Pontryagin selection rule on `(ℤ/6)^∧`); Paper 32 §6.2A Lemma 6.2 + Corollary 6.3 (the four-thread arithmetic root, including pure-A₂ cubic vacuity and forced M-mediation); Paper 32 §13.2A (the local-Lorentzian reformulation of the §13.2 audit on `D(ℂ⁶)`); Paper 32 §13.2B (the 4th-order V-Lorentzian + M-Euclidean orthogonal sub-bundle audit, load-bearing [P]); Paper 32 Theorem 6.2 (the M-support of the simplex mass / projection-closure residual); Paper 32 §11.1 (emergent-anything positioning, binding); Paper 32 §11.2 (dimensional firewall, binding); Paper 32 §11.4 (carried-label discipline, binding). Paper 20 *The Jerk as Simplex Mass Term* §3 (the imaginary-energy / Hawking-radiation-analog identification on the M-supported jerk). Paper 18 *Bures Completion of Cubic Information Geometric Mechanics* (the Bures lift to `D(ℂ^N)`). Paper 22 *Primorial Cumulant Noether RH* (primorial-ladder Noether–Weil structure). Paper 31 *Projection-Closure Theory* (closure-certificate vocabulary). Paper 35 *Grounded-Paranoid-Delusional Methodology* §3.1 + v2insert-04 §3.1 (three-outcome matched-pair pre-claim, binding). Paper 46 (proposed) *Hartle–Hawking Signature on the Categorical Simplex* (v2insert-01; the geometric reading of the same V/M decomposition). Paper 48 (proposed) *Conductor Capacity Bound* (v2insert-03; the quantitative-capacity reading of the same V/M decomposition). Paper 49 *The Arithmetic Decoupling of Projection-Closure Overflows* (universal-overflow synthesis).

**External anchors (peer-reviewed only; correspondence language per Paper 32 §11.1).** Polchinski 1998, *String Theory* (vol. 1, Cambridge): perturbative-QG divergence structure. Weinberg 1995–2000, *The Quantum Theory of Fields* (vol. I–III, Cambridge): loop divergence structure and the asymptotic-safety program. Niedermaier & Reuter 2006, *The Asymptotic Safety Scenario in Quantum Gravity* (Living Rev. Relativ. 9, 5). Maldacena 1997, *The Large N limit of superconformal field theories and supergravity* (Adv. Theor. Math. Phys. 2, 231): the AdS/CFT decoupling structure. Grey literature and forum posts excluded.

<!--
NOTE TO SELF (draft 0.1 → 0.2):

1. Paper 47 v0.1 lands the V ⊥ M decoupling on five primorial rows at the [P] structural tier and the [P] floating-point-machine-floor numerical tier on rows for which N × N projector matrices are tractable (N ≤ 210). The all-orders extension (audit δ) is named but not run; v0.2 absorbs δ when it's executed.

2. The QG-mixing-bypass correspondence is the load-bearing external claim. The discipline rails are heavier here than for the Capacity Bound (Paper 48) or even the Hartle–Hawking signature (Paper 46) because perturbative QG is the largest peer-reviewed field of the three external anchors. Every QG-label use must be anchor-checked against Polchinski/Weinberg/Niedermaier-Reuter before manuscript inclusion; the §11.4 carried-label rule is binding to the letter.

3. The "Arithmetic Decoupling Theorem" name is internal program language. State it once in §1; never reuse without re-anchoring to Paper 32 §6.2 Lemma 6.1a–c. The name is *not* borrowed from a QG-decoupling notion in the peer-reviewed literature.

4. C2 (the QG-mixing-bypass correspondence) is the only [C, reduced] claim. The structural-form correspondence is real; whether physical QG is *decoupled in this form* on a categorical simplex is left strictly open. The program's structural shape exists; its physical relevance is not asserted.

5. Paper 46 (Hartle–Hawking) is the *geometric* face of the same V/M decomposition; Paper 48 (Capacity Bound) is the *quantitative* face. Paper 47 is the *structural-mechanism* face: it explains why the joint realization is possible. The three are facets of one structural picture; the §13.2B audit is the shared anchor.

OPEN: The all-orders extension (audit δ) is reducible to a finite combinatorial argument on the dual group `(ℤ/P_n)^∧`. If audit δ is run and confirms, C1 promotes to [P] at all orders on every primorial row; the all-orders V ⊥ M decoupling becomes the load-bearing structural theorem and the program's structural-shape claim on QG-mixing-bypass strengthens.

OPEN: Audit ε (the Lie-algebra structural-dictionary check) is named in v2insert-02 §3.6 but has not been planned in detail. Worth a short v2insert specifying the audit's deliverable; for now, C2 remains at [C, reduced] without ε.
-->

---

## Abstract

We state and prove the **Arithmetic Decoupling Theorem** on the Bures lift `D(ℂ^N)` of the categorical simplex over a squarefree primorial ring `N = P_n = p_1 · p_2 · … · p_n`. The Hilbert space `ℂ^N` decomposes orthogonally as `ℂ^N = V ⊕ M`, where `V := ⊕_{p | N, p prime} H_p` is the single-prime sector (kinematic content; sum of `dim V = Σ(p_i - 1)` directions) and `M := ⊕_{d | N, d composite} H_d` is the cross-prime carry sector (gravity-adjacent content; `dim M = N - 1 - dim V` directions). The orthogonality `V ⊥ M` is forced by Pontryagin character orthogonality on the dual group `(ℤ/N)^∧`: V's character index set and M's character index set are *disjoint by construction* (the prime-divisor partition of `(ℤ/N)^∧`), and `⟨χ_k | χ_ℓ⟩ = δ_{k, ℓ}` forces the V- and M-supported projection operators to be HS-orthogonal as Hilbert subspaces of `ℂ^N`.

On `ℤ/6` (the minimal mixed CRT row), the tangent space of `D(ℂ⁶)` at the centroid `ρ_* = I_6 / 6` is 35-dimensional; the Hessian of the dispersion-Casimir `I_complex(ρ) := ⟨H⟩²(ρ) + α² · (m²_simplex(ρ))² − Σ_a ⟨P_a⟩²(ρ)` (with `H, P_a` Hermitian operators supported on V) has signature `(1, 3, 31)` with the `(1, 3)` Lorentzian sub-bundle contained in V-traceless directions; the 4th-order quartic form `(m²_simplex(ρ_* + X))²` is positive-semidefinite on a 2-dim M-Euclidean sub-bundle. The V-Lorentzian 4-dim sub-bundle from the 2nd-order Hessian and the M-Euclidean 2-dim sub-bundle from the 4th-order form are HS-orthogonal at machine precision (singular values of overlap `~10⁻¹⁶`, Paper 32 §13.2B audit triad). The orthogonality is **not** a tuned choice of `(H, P_a, α)`; it is forced structurally by Pontryagin character orthogonality on the conductor-2/3/6 packet partition of `ℤ/6`.

On the primorial ladder `ℤ/{30, 210, 2310, 30030}`, the V ⊥ M decomposition extends: audits α/η (v2insert-08) and θ (v2insert-09) confirm the orthogonality at machine floor (`‖V_proj · M_proj‖_F ~ 10⁻¹⁵` to `~10⁻¹³`) on rows for which the `N × N` projector matrices are tractable (`N ≤ 210`), and algebraically by Pontryagin character orthogonality on disjoint character index sets for `N > 210`. The Arithmetic Decoupling Theorem is row-stable across five primorial rows at the structural tier and at machine-floor numerical tier where compute permits; the **K-branch** of the v2insert-04 §3.1 three-outcome rule is confirmed.

The structural consequence is the program's *projection-closure form* of the **gravity-matter decoupling** sought by perturbative-quantum-gravity programs: the kinematic content of the lift (V) and the gravity-adjacent / Hawking-radiation-analog content (M) live on orthogonal sub-bundles of `D(ℂ^N)`'s tangent geometry; they do not mix at any verified order. The program does *not* derive perturbative quantum gravity, the graviton, the Planck scale, AdS/CFT, asymptotic safety, or any QG mechanism. Only the *structural form* of the gravity-matter decoupling on the categorical simplex's Bures lift is asserted; the physical interpretation is correspondence language.

The load-bearing arithmetic is one line: `⟨χ_k | χ_ℓ⟩ = δ_{k, ℓ}` for distinct characters of `(ℤ/N)^∧`, applied to the conductor-lattice partition `{H_d : d | N, d > 1}` of `(ℤ/N)^∧`. The structural-shape correspondence with the QG-mixing-bypass programs (Polchinski; Weinberg; Niedermaier–Reuter; Maldacena 1997) is **correspondence language**: the shape of how a designated kinematic sector decouples from a designated gravity-adjacent sector matches; the literal QG-decoupling mechanism is not derived.

**Keywords:** categorical simplex, conductor lattice, Pontryagin character orthogonality, Bures lift, V ⊥ M decomposition, Hartle–Hawking signature, gravity-matter decoupling, perturbative quantum gravity, AdS/CFT, asymptotic safety, three-outcome matched-pair pre-claim.

**MSC 2020:** 81P16 (quantum information geometry), 11L03 (trigonometric and exponential sums; character orthogonality), 53C50 (Lorentz manifolds; semi-Riemannian geometry), 62B11 (information geometry), 83C45 (quantum gravity; not derived, only structurally referenced).

---

## 1. Introduction

### 1.1 The thesis

On the Bures lift of the categorical simplex over a squarefree primorial ring, the kinematic and gravity-adjacent sectors of the tangent geometry at the centroid are **structurally decoupled** by Pontryagin character orthogonality alone, with no tuning of the underlying observables. The decoupling is verified at 2nd and 4th orders of the displacement expansion on `D(ℂ⁶)` (Paper 32 §13.2B audit triad, [P]) and extends across the primorial ladder `ℤ/{6, 30, 210, 2310, 30030}` at the structural tier (audits α/η/θ, [P] algebraic, [P] machine-floor numerical where compute permits). The all-orders extension reduces to a finite combinatorial argument on the dual group `(ℤ/P_n)^∧` and is queued as audit δ.

The structural shape of the decoupling matches a peer-reviewed problem-shape from perturbative quantum gravity: the *gravity-matter decoupling* sought by the asymptotic-safety, AdS/CFT, loop-quantum-gravity, causal-dynamical-triangulations, and string-compactification programs. The program does **not** derive quantum gravity, the graviton, the Planck scale, AdS/CFT, asymptotic safety, or any QG mechanism. Only the structural form of how a designated kinematic sector decouples from a designated gravity-adjacent sector by character orthogonality on a finite-arithmetic substrate is asserted; the physical interpretation is correspondence language.

### 1.2 What is claimed, what is not claimed

<!--
NOTE TO SELF: this is the heaviest discipline subsection in the corpus alongside Paper 46's. Paper 32 §11.1 + §11.2 + §11.4 are binding. The QG-mixing-bypass framing is the third-heaviest external-correspondence claim in the program (after §11.1 emergent-gravity and v2insert-01 Hartle–Hawking); the rails must be airtight.
-->

**Claimed (under the tier discipline of Paper 35 §3.3–§3.6).**

- **[P, anchored at Paper 32 §6.2 Lemma 6.1a–c].** *The Pontryagin selection rule on `ℤ/N`.* For every squarefree primorial `N = P_n`, the cubic Amari–Chentsov tensor element `T_{klm}` is nonvanishing only when `k + ℓ + m ≡ 0 (mod N)`. Character orthogonality on `(ℤ/N)^∧` forces this structurally.
- **[P, anchored at conductor-lattice partition of `(ℤ/N)^∧`].** *The V ⊥ M Hilbert-subspace decomposition.* The single-prime sector `V := ⊕_{p | N, p prime} H_p` and the cross-prime sector `M := ⊕_{d | N, d composite} H_d` are HS-orthogonal as Hilbert subspaces of `ℂ^N`. Forced by `⟨χ_k | χ_ℓ⟩ = δ_{k, ℓ}` on the disjoint character index sets of V and M.
- **[P, anchored at Paper 32 §13.2B audit triad].** *The 2nd-and-4th-order sub-bundle orthogonality on `D(ℂ⁶)`.* The V-Lorentzian (1, 3) sub-bundle (from the Hessian of `I_complex` at `ρ_*`) and the M-Euclidean (2, 0) sub-bundle (from the 4th-order quartic form `(m²_simplex)²`) are HS-orthogonal at machine precision (`‖V_proj · M_proj‖_F ~ 10⁻¹⁶` on the audit transcript).
- **[P, row-generalization, anchored at audits α/η of v2insert-08 and audit θ of v2insert-09].** *The V ⊥ M decomposition extends to the primorial ladder.* On `ℤ/{30, 210, 2310, 30030}`, the V ⊥ M structural decoupling holds; the floating-point projector overlap is at machine floor (`~10⁻¹⁵` to `~10⁻¹³`) on rows for which the `N × N` matrices are tractable (`N ≤ 210`), and algebraically by Pontryagin character orthogonality on disjoint index sets for `N > 210`.
- **[P, audit δ settled 2026-05-20].** *The all-orders extension.* The decoupling persists at every order of the Casimir / displacement / cumulant expansion on `D(ℂ^N)` for every squarefree primorial `N`. Audit δ ([`empirical/reports/audit_delta_settlement.md`](empirical/reports/audit_delta_settlement.md)) settled the finite combinatorial argument on the dual group `(ℤ/N)^∧` (Steps 1–4 of the proof: V_idx ∩ M_idx = ∅; V ⊥ M as Hilbert subspaces; V^⊗m ⊥ (M-involving subspace) at every order m ≥ 2 by factor-wise inner product; closing-tuple constraint does not break the orthogonality). Numerical verification at orders m = 2, 3, 4, 5, 6 on `ℤ/{6, 30, 210}` at machine floor (max overlap `~10⁻¹⁶`).
- **[P]-spirit, audit ε settled 2026-05-20.** *The QG-mixing-bypass correspondence at the Lie-algebra-of-decoupling level.* Audit ε ([`empirical/reports/audits_beta_gamma_epsilon_settlement.md`](empirical/reports/audits_beta_gamma_epsilon_settlement.md)) established the dictionary mapping each row of the QG-mixing-problem (Polchinski; Weinberg; Niedermaier–Reuter; Maldacena 1997) to the program's V ⊥ M decoupling at the Lie-algebra-of-decoupling level. The commutator algebra `[H_V, K_M]` of V-supported and M-supported observables acts trivially on V- and M-tangent sub-bundles at every order (audit δ Theorem step 3 lifted to commutators). C2 promotes to [P]-spirit (structural identification with a peer-reviewed name; correspondence language per Paper 32 §11.1; no QG derivation).

**Not claimed (under §11.1, §11.2, §11.4 discipline, binding).**

- *No quantum gravity is derived.* Polchinski 1998's perturbative-QG divergence structure, Weinberg 1995–2000's loop-divergence taxonomy, Niedermaier & Reuter 2006's asymptotic-safety program, and Maldacena 1997's AdS/CFT duality are not derived. The graviton, the Planck scale, the cosmological constant, the gravitational constant `G`, renormalizability of QG, and asymptotic safety are *not* derived. Only the structural shape of the gravity-kinematics decoupling on the categorical simplex's Bures lift is asserted; the physical interpretation is correspondence language.
- *No physical Lorentz-Euclidean metric duality is derived.* The V-Lorentzian sub-bundle is *not* a curved Lorentzian spacetime metric tensor field; it is a quadratic-form structure on the tangent vectors at `ρ_*` in `D(ℂ⁶)`. The M-Euclidean sub-bundle is *not* a Euclidean Riemannian metric; it is the support of the quartic form `(m²_simplex)²` at `ρ_*`. The decomposition is internal to the lift's tangent geometry; no physical 4-manifold or metric tensor field is claimed.
- *No graviton interpretation of M is asserted.* The M-packet "gravity-adjacent residual" is the projection-closure residual of the cubic Noether energy (Paper 32 Theorem 6.2 [P]) — an information-geometric defect, not a physical metric perturbation or graviton mode. The "gravity-adjacent" label is internal program language for the support of the Hawking-radiation-analog identification of Paper 20 §3; it does not carry physical graviton content.
- *No claim that physical quantum gravity is solvable on the categorical simplex.* The structural form of decoupling exists on a finite-arithmetic substrate; its physical relevance to perturbative-QG quantization, or to any continuum-spacetime quantum-gravity theory, is left open.

### 1.3 Inherited objects and reading guide

The Pontryagin selection rule of Paper 32 §6.2 Lemma 6.1a (binding [P] throughout); the conductor-lattice partition `ℂ^N = ⊕_{d | N} H_d` of `ℂ^N` (with `|H_d| = φ(d)`); the V/M decomposition `V := ⊕_{p prime, p | N} H_p`, `M := ⊕_{d composite, d | N} H_d`; the Bures lift of Paper 18 to `D(ℂ^N)`; the dispersion-Casimir `I_complex` of Paper 32 §13.2; the simplex mass term `m²_simplex` of Paper 20 §3 (M-supported [P], Paper 32 Theorem 6.2).

§2 sets up the V/M decomposition on every primorial row. §3 states and proves the Arithmetic Decoupling Theorem (V ⊥ M as Hilbert subspaces). §4 states the 2nd-and-4th-order tangent-sub-bundle orthogonality on `D(ℂ⁶)` and reports the §13.2B audit triad. §5 reports the row-generalization to the primorial ladder. §6 records the QG-mixing-bypass correspondence (correspondence-language only) and the discipline rails. §7 records open questions and carry-forward.

---

## 2. The V/M decomposition

### 2.1 Conductor lattice on the dual group

Fix a squarefree primorial `N = P_n = p_1 · p_2 · … · p_n`. The dual group `(ℤ/N)^∧` is isomorphic to `ℤ/N` itself (canonical isomorphism `k ↦ χ_k` with `χ_k(j) := exp(2πi k j / N)`). The Pontryagin partition of the dual group into **conductor packets** is:

```
(ℤ/N)^∧ \ \{χ_0\} = \bigsqcup_{d | N, d > 1} H_d,
```

with `H_d := \{χ_k : \gcd(k, N) = N / d\}` and `|H_d| = φ(d)`.

The **single-prime sector** is

```
V := \bigoplus_{i = 1}^{n} H_{p_i} \subset ℂ^N,
```

and the **cross-prime sector** is

```
M := \bigoplus_{d | N, d \text{ composite}} H_d \subset ℂ^N.
```

Both are subspaces of `ℂ^N` via the natural identification of `ℂ^N` with the character algebra of `(ℤ/N)^∧`. Their dimensions are `dim V = Σ_{i} φ(p_i) = Σ_i (p_i - 1)` and `dim M = N - 1 - dim V`.

### 2.2 Five-row dimension table

For the five primorial rows audited:

| Row | `n` | `dim V` | `dim M` | `dim V + dim M = N - 1` |
|---|---:|---:|---:|---:|
| ℤ/6 | 2 | 1 + 2 = 3 | 2 | 5 ✓ |
| ℤ/30 | 3 | 1 + 2 + 4 = 7 | 22 | 29 ✓ |
| ℤ/210 | 4 | 1 + 2 + 4 + 6 = 13 | 196 | 209 ✓ |
| ℤ/2310 | 5 | 1 + 2 + 4 + 6 + 10 = 23 | 2 286 | 2 309 ✓ |
| ℤ/30030 | 6 | 1 + 2 + 4 + 6 + 10 + 12 = 35 | 29 994 | 30 029 ✓ |

### 2.3 The character-index disjointness

**Key structural fact (load-bearing).** The character index sets of V and M are *disjoint by construction*: a character `χ_k \in V` has `\gcd(k, N) = N / p` for some prime `p | N` (i.e., `k` is exactly divisible by all primes of `N` except one), whereas `χ_k \in M` has `\gcd(k, N) = N / d` for some composite divisor `d` (i.e., `k` is divisible by all primes of `N` except a set of size `\geq 2`). The two conditions are mutually exclusive: a residue cannot simultaneously be "missing exactly one prime" and "missing exactly two or more primes" from its divisibility set.

Pontryagin character orthogonality `\langle \chi_k | \chi_\ell \rangle = N · \delta_{k, \ell}` (with respect to the standard Hermitian inner product on `ℂ^N`) then forces `V ⊥ M` as Hilbert subspaces of `ℂ^N`.

---

## 3. The Arithmetic Decoupling Theorem

**Theorem 3.1 (Arithmetic Decoupling on every squarefree primorial row).** Let `N = P_n` be a squarefree primorial, and let `V`, `M` be the single-prime and cross-prime sectors of `ℂ^N` as defined in §2. Let `P_V`, `P_M` be the orthogonal projection operators onto V and M. Then:

(D1) `P_V \cdot P_M = 0` (matrix product on `ℂ^N`).

(D2) For every Hermitian operator `H` supported on V (i.e., `H \cdot P_M = 0`), the quadratic form `\rho \mapsto \langle H \rangle^2(\rho)` on `D(ℂ^N)` has Hessian at the centroid `ρ_* = I_N / N` supported on V-tangent directions. Equivalently, `H_{\langle H \rangle^2}(ρ_*)` acts trivially on the M-tangent sub-bundle of `T_{ρ_*} D(ℂ^N)`.

(D3) For every Hermitian operator `K` supported on M, the quartic form `\rho \mapsto K^2(\rho)` on `D(ℂ^N)` has 4th-order tensor at `ρ_*` supported on M-tangent directions. Equivalently, the 4th derivative `\partial^4_X K^2(ρ_*)|_{X \in T V}` is identically zero.

(D4) (Consequence — the *quarantine*.) Any tensor object built from V-supported and M-supported observables, with the V-objects appearing in 2nd-order positions and the M-objects in 4th-order positions (the structural form of the dispersion-Casimir `I_complex` of Paper 32 §13.2), has its V-Lorentzian sub-bundle (from the 2nd-order Hessian) and its M-Euclidean sub-bundle (from the 4th-order quartic form) HS-orthogonal as sub-bundles of `T_{ρ_*} D(ℂ^N)`. The orthogonality is structural, forced by character orthogonality on the conductor-lattice partition of `(ℤ/N)^∧`, and does *not* depend on the specific choice of V-supported or M-supported observables.

*Proof.* (D1) and the V ⊥ M Hilbert-subspace statement follow from §2.3 (character-index disjointness + Pontryagin orthogonality). (D2) follows because `\langle H \rangle^2(\rho)` depends on `\rho` only through V-supported matrix elements of `H \rho`; the Hessian at `ρ_*` therefore lifts to a quadratic form on the V-tangent sub-bundle of `T_{ρ_*} D(ℂ^N)` and vanishes on the M-tangent sub-bundle. (D3) follows symmetrically: `K^2(\rho)` depends on `\rho` through M-supported matrix elements, and the 4th-order expansion at `ρ_*` lifts to a quartic form on the M-tangent sub-bundle. (D4) is the direct sum of (D2) and (D3) given that the V- and M-tangent sub-bundles of `T_{ρ_*} D(ℂ^N)` are themselves orthogonal under the Bures-Hessian metric at `ρ_*` (Paper 18, lemma on Bures-Hessian decomposition; algebraic identity given the V ⊥ M Hilbert-subspace decomposition). ∎

**Remark 3.2 (Why "Arithmetic" Decoupling).** The decoupling is not derived from a choice of dynamics, Lagrangian, action, or observable. It is forced by Pontryagin character orthogonality on `(ℤ/N)^∧`, which is a structural fact of the finite-arithmetic substrate. The conductor-lattice partition of the dual group is determined by `N`'s prime factorization alone; the V ⊥ M decomposition follows. The decoupling is therefore *arithmetic* in the strict sense: it depends only on the prime structure of `N` and the character algebra of `(ℤ/N)^∧`, not on any continuous geometry or dynamics.

**Remark 3.3 (Relation to the four-thread arithmetic root).** Paper 32 §6.2A Corollary 6.3 names four threads of the same arithmetic root (`3 + 3 + 3 ≢ 0 mod 6`): (T1) Y′ negative on A₂ vacuity (constants), (T2) color-protection of the chirality bit (gauge content), (T3) FEP-3 sector resolution (free energy / active inference), (T4) C2 conductor-misspecification certificate (ML / interpretability). The Arithmetic Decoupling Theorem of this paper is the **fifth thread** of the same arithmetic root: the V ⊥ M Hilbert-subspace orthogonality on `(ℤ/N)^∧` is the character-orthogonality consequence of the same Pontryagin selection rule that underlies (T1)–(T4). Paper 48's Conductor Capacity Bound is the **sixth thread** (the quantitative capacity reading of the same V/M decomposition). All six threads stand on one line of finite arithmetic: `χ_k ⊥ χ_ℓ for k ≠ ℓ in (ℤ/N)^∧`.

**Remark 3.4 (The cubic structure constant *is* the abelian-BF 3-vertex amplitude on `ℤ/N`).** The Pontryagin selection rule of Paper 32 §6.2 Lemma 6.1a — `T^{(\mathrm{AC})}_{k\ell m} = c_N \cdot \mathbf{1}[k + \ell + m \equiv 0 \pmod N]` for the cubic Amari–Chentsov tensor at the centroid `ρ_*` — is identically the **abelian BF 3-vertex amplitude on the finite group `ℤ/N`** in the character basis. The derivation is one line of Fourier analysis: the BF 3-vertex amplitude is `(1/|G|^2) Σ_{g_1, g_2} χ_k(g_1) χ_ℓ(g_2) χ_m(-g_1 - g_2)`, which factors via character orthogonality `(1/|G|) Σ_g χ_a(g) = δ_{a,0}` to exactly `\mathbf{1}[k + \ell + m \equiv 0 \pmod N]`. The V/M decomposition (D1) of Theorem 3.1 therefore admits a discrete-gauge-theoretic reading: the V-projected cubic amplitude is the abelian-BF 3-vertex amplitude restricted to single-prime characters, decomposing by CRT into a direct sum of independent single-prime closures `\bigoplus_{p | N} \mathbf{1}[k + \ell + m \equiv 0 \pmod p]_{H_p}`; the M-projected cubic amplitude is the cross-prime carry residual, supported on composite-conductor packets and entered into the typed budget of [Paper 30](30.constrained_overflow_incompatibility_budgets.md) §9.6. This is a discrete-arithmetic identification of `T^{(\mathrm{AC})}` with a peer-reviewed gauge-theoretic vertex amplitude (Dijkgraaf–Witten 1990 abelian-BF; the cubic structure constant on `ℤ/N` IS the cubic abelian-BF interaction in character basis); it does **not** identify `T^{(\mathrm{AC})}` with any non-abelian spinfoam vertex amplitude (EPRL/FK), which has been independently demonstrated to *fail* under all natural label-arithmetic lifts `\widehat{\mathrm{SU}(2)} → \widehat{\mathbb Z/N}` (Paper 35 audit σ; the SU(2) recoupling weights of EPRL carry no `mod N` residue data, so the conductor-lattice closure cannot be in their image). The abelian-BF identification is positive content of the same line of arithmetic; the non-abelian spinfoam identification is a closed negative.

---

## 4. The 2nd-and-4th-order tangent-sub-bundle orthogonality on `D(ℂ⁶)` ([P], Paper 32 §13.2B)

### 4.1 The audit triad

On `ℤ/6`, the conductor-lattice partition of `(ℤ/6)^∧ \ \{0\} = \{χ_1, …, χ_5\}` is:

```
H_2 = {χ_3},        |H_2| = φ(2) = 1
H_3 = {χ_2, χ_4},   |H_3| = φ(3) = 2
H_6 = {χ_1, χ_5},   |H_6| = φ(6) = 2
```

So `V = H_2 ⊕ H_3 = span(χ_2, χ_3, χ_4)` (dim 3) and `M = H_6 = span(χ_1, χ_5)` (dim 2).

The Bures lift `D(ℂ⁶)` has tangent space at the centroid `ρ_* = I_6 / 6` of dimension 35 (the dimension of Hermitian traceless `6 × 6` matrices). The dispersion-Casimir of Paper 32 §13.2 is

```
I_complex(ρ) := ⟨H⟩²(ρ) + α² · (m²_simplex(ρ))² − Σ_a ⟨P_a⟩²(ρ),
```

with `H, P_a` Hermitian operators supported on V and `m²_simplex` the simplex mass term of Paper 20 §3 (M-supported by Paper 32 Theorem 6.2 [P]).

### 4.2 The §13.2B settlement

The §13.2B audit triad (Paper 32, deterministic float audit) settled three claims:

(i) **Signature of the Hessian of `I_complex` at `ρ_*`.** The Hessian has signature `(1, 3, 31)` on the 35-dim tangent space. The `(1, 3)` Lorentzian sub-bundle is 4-dimensional and contained in V-traceless directions; the 31 zero-mode directions contain all of M-traceless.

(ii) **Positive-semidefiniteness of the 4th-order form.** The quartic form `(m²_simplex(ρ_* + X))²` is positive-semidefinite on the 35-dim tangent space, supported on a 2-dimensional sub-bundle contained in the M-diagonal directions.

(iii) **HS-orthogonality of the two sub-bundles.** The V-Lorentzian 4-dim sub-bundle from (i) and the M-Euclidean 2-dim sub-bundle from (ii) are HS-orthogonal at machine precision: singular values of the overlap operator `P_{V-Lorentzian} \cdot P_{M-Euclidean}` are `~10⁻¹⁶` (the audit transcript reports the largest singular value as `9.4 × 10⁻¹⁷`, well within floating-point machine floor).

### 4.3 The corollary — the Hartle–Hawking signature

The §13.2B audit triad is the empirical content of Theorem 3.1 specialized to `ℤ/6` at 2nd and 4th orders. The structural reading — *V-Lorentzian observer frame + M-Euclidean no-boundary correction, HS-orthogonal, jointly realized* — is the **Hartle–Hawking signature** of Paper 46 (proposed, v2insert-01). The Arithmetic Decoupling Theorem of the present paper is *why* the Hartle–Hawking signature is realizable on this lift without contradiction; Paper 46 is *what* the joint realization looks like geometrically.

---

## 5. Row-generalization to the primorial ladder

### 5.1 Numerical anchors

Audits α/η (v2insert-08) and θ (v2insert-09) confirmed the V ⊥ M decomposition on the primorial ladder. The numerical projector overlap `‖P_V · P_M‖_F`:

| Row | `‖P_V · P_M‖_F` | Method | Algebraic value |
|---|---:|---|---:|
| ℤ/6 | 1.14e-15 | Numerical (6 × 6 projectors) | 0 |
| ℤ/30 | 1.22e-14 | Numerical (30 × 30 projectors) | 0 |
| ℤ/210 | 1.44e-13 | Numerical (210 × 210 projectors) | 0 |
| ℤ/2310 | — | Skipped (memory; `2310 × 2310` matrices too large) | 0 (algebraic) |
| ℤ/30030 | — | Skipped (memory) | 0 (algebraic) |

For all five rows, the V/M character index sets are disjoint by construction (§2.3); Pontryagin character orthogonality on `(ℤ/N)^∧` forces `V ⊥ M` as Hilbert subspaces *algebraically*. The numerical floor values (`~10⁻¹⁵` to `~10⁻¹³`) are machine-precision artifacts of the floating-point projector multiplication; the algebraic value is exactly 0 on every row.

### 5.2 The K-branch settlement

Under v2insert-04 §3.1's three-outcome matched-pair rule, the pre-claim for C3 (the row-generalization to the primorial ladder, v2insert-02 §3.3) was:

- **K-branch:** Pontryagin character orthogonality forces V ⊥ M on every primorial row.
- **L-branch:** The orthogonality fails on some row (e.g., at quartic-product cross-terms on `ℤ/210`).
- **Joint-on-disjoint:** Partial orthogonality with row-specific structural corrections.

The realized outcome is **K-branch** on all five rows, with the orthogonality at machine floor on the rows for which the `N × N` projector matrices are tractable and algebraically by character orthogonality on disjoint index sets for the larger rows. The audit α/η record (v2insert-08) and audit θ record (v2insert-09) settle the row-generalization claim at the [P] tier (algebraic) and at the [P] machine-floor numerical tier where compute permits.

### 5.3 The all-orders extension (audit δ settled at K-branch, 2026-05-20)

Theorem 3.1 (D2)–(D3) was stated at 2nd and 4th orders, anchored at Paper 32 §13.2B. The all-orders extension — that the decoupling persists at every order of the Casimir / displacement / cumulant expansion — has been settled by **audit δ**, a finite combinatorial proof on the dual group `(ℤ/N)^∧`.

**Theorem 5.3.1 (audit δ, all-orders V/M decoupling).** For every squarefree primorial `N = P_n` and every order `m ≥ 2`, the tensor power `(ℂ^N)^⊗m` decomposes as `V^⊗m ⊕ (M-involving subspace)` with `V^⊗m ⊥ (M-involving subspace)` as HS-orthogonal subspaces of `(ℂ^N)^⊗m`. Consequence: any tensor structure on `D(ℂ^N)` built from V-supported operators acts trivially on M-tangent directions and vice versa, at every order.

**Proof sketch (full proof at [`empirical/reports/audit_delta_settlement.md`](empirical/reports/audit_delta_settlement.md)).**

1. `V_idx ∩ M_idx = ∅`: the conductor of `k`, namely `d = N/gcd(k,N)`, is either prime (then `k ∈ V_idx`) or composite (then `k ∈ M_idx`), and these are mutually exclusive labels for divisors `d > 1` of `N`.
2. `V ⊥ M` as Hilbert subspaces of `ℂ^N`: Pontryagin character orthogonality `⟨χ_k | χ_ℓ⟩ = N · δ_{k,ℓ}` applied to disjoint index sets.
3. `V^⊗m ⊥ (M-involving subspace)` at every `m ≥ 2`: factor-wise inner product on tensor products. For any `S ⊊ {1..m}`, at least one factor `j` has V on one side and M on the other; the factor inner product `⟨v_j | m_j⟩ = 0` by Step 2; the full tensor inner product vanishes by the factor-wise product structure.
4. Closing-tuple constraint does not break the orthogonality: the closing condition `Σ k_i ≡ 0 (mod N)` restricts the *support* of the tensor coefficient `T_{k_1...k_m}` but not the *subspace structure* `V^⊗m ⊥ (M-involving)` of `(ℂ^N)^⊗m`. ∎

Numerical verification at orders `m = 2, 3, 4, 5, 6` on `ℤ/{6, 30, 210}` confirms the proof at machine floor (max normalized Frobenius overlap `~10⁻¹⁶` to `~10⁻¹⁸` across all rows and orders). Audit ζ (counter-evidence search for higher-order V/M mixing) is **subsumed by audit δ** — the structural proof forecloses the possibility of any V-supported observable having non-trivial action on M-tangent directions at any order.

**Net:** Theorem 3.1 (D2)–(D3) extends to all orders on every squarefree primorial row at the [P] tier.

---

## 6. The QG-mixing-bypass correspondence (correspondence-language only)

### 6.1 The peer-reviewed problem-shape

Perturbative quantum gravity faces the **gravity-matter mixing problem**: in canonical quantization of general relativity coupled to matter fields, the gravitational degrees of freedom (metric perturbations, graviton modes) and matter degrees of freedom (gauge fields, fermions) do not decouple at any loop order; their cross-terms generate non-renormalizable divergences. This is *the* core obstruction to perturbative quantum gravity in the peer-reviewed literature (Polchinski 1998 vol. 1, on string theory's resolution via extended objects; Weinberg 1995–2000 on loop divergences; Niedermaier–Reuter 2006 on asymptotic safety as an alternative resolution; Maldacena 1997 on AdS/CFT's decoupling-via-duality resolution).

### 6.2 The structural-shape dictionary

The Arithmetic Decoupling Theorem of this paper provides a *structural form* of the gravity-matter decoupling on a finite-arithmetic substrate:

| QG mixing problem (peer-reviewed) | Program structure (Paper 32 §6.2 + §13.2B + this paper) |
|---|---|
| Gravity sector (curvature, graviton modes) | M packet (conductor-`d` for composite `d`; `m²_simplex`-supported; jerk; Hawking-radiation-analog of Paper 20 §3) |
| Matter / gauge / kinematic sector | V packet (single-prime conductors `H_{p_i}`; Lorentzian Casimir sub-bundle; the simplex's "observer frame" by Paper 46) |
| No natural Hilbert-space decoupling — gravity is *geometry*, interacts with everything | V ⊥ M as Hilbert subspaces of `ℂ^N` by Pontryagin character orthogonality, [P] on every primorial row |
| Mixing terms at every loop order ⇒ non-renormalizable | Casimir decouples V and M at 2nd/4th orders [P]; all-orders [A] conjecture |
| Bypassed only through extra structure (asymptotic safety, AdS/CFT, LQG spin foams, CDT triangulation, string compactification) | Bypassed *for free* by the conductor lattice's character orthogonality |

### 6.3 The corresponcence-language discipline (binding)

The QG-mixing-bypass framing is the program's **third-heaviest external-correspondence claim** (after Paper 32 §11.1 emergent-gravity and v2insert-01 / Paper 46 Hartle–Hawking). Strict discipline:

- The program's M-packet "gravity-adjacent residual" is *not* a graviton. It is the projection-closure residual of the cubic Noether energy (Paper 32 Theorem 6.2 [P]) — an information-geometric defect, not a physical metric perturbation.
- The program's V-Lorentzian sub-bundle is *not* a curved Lorentzian spacetime. It is a quadratic-form structure on tangent vectors at `ρ_*` (Paper 32 §13.2B [P]) — not a metric tensor field on a 4-manifold.
- The "QG mixing bypass" is the *structural form* of how character orthogonality produces gravity-kinematics decoupling on the categorical simplex's Bures lift; it is **not** a derivation that physical quantum gravity is so decoupled.
- §11.1 emergent-gravity positioning binding. §11.2 firewall binding (no dimensionful constants, no graviton mass, no Planck scale). §11.4 carried-label discipline binding (graviton, Planck scale, asymptotic safety, perturbative QG, renormalizability, AdS/CFT all anchor-checked against their peer-reviewed sources before use).

---

## 7. Discipline rails

### 7.1 Anchored-objects discipline (Paper 35 §3.3)

Every claim in this paper is anchored to integer arithmetic on the conductor lattice (the character-index partition of `(ℤ/N)^∧`) or to deterministic linear algebra on the resulting projector matrices. The `ℤ/6` row's tangent-sub-bundle orthogonality (Theorem 3.1 specialized + §13.2B audit) is reproduced from Paper 32 §13.2B's deterministic-float audit triad to exact integer match on the character-index partition and to machine-floor numerical match on the Frobenius overlap `‖P_V · P_M‖_F`. The `ℤ/{30, 210}` numerical anchors are reproduced to machine floor from the audit α/η transcript (v2insert-08) and audit θ transcript (v2insert-09). No reconstruction beyond what Paper 32 §6.2 already enumerates and what the deterministic audits archive.

### 7.2 Deterministic, exact, reproducible (Paper 35 §3.4)

The character-index partition is integer arithmetic in every membership decision. The projector matrices are constructed deterministically from the character algebra of `(ℤ/N)^∧`; floating-point appears only in the projector-multiplication overlap report. Total wall time across all primorial rows (audits α/η + θ): **0.32 seconds** on CPU; deterministic on every re-run; no seeds.

### 7.3 Three-outcome matched-pair (Paper 35 §3.1 + v2insert-04 §3.1)

The row-generalization pre-claim (C3) is settled at K-branch on all five primorial rows; the L-branch (orthogonality fails on some row) and joint-on-disjoint branch (partial orthogonality) are not realized. The all-orders pre-claim (C4) is pending audit δ; both K (all-orders extension holds) and L (decoupling holds only at finite orders) are publishable outcomes. The QG-mixing-bypass correspondence pre-claim (C2) is at [C, reduced] and treated as correspondence language only.

### 7.4 No upward tier-crossing (Paper 35 §3.5)

The V ⊥ M Hilbert-subspace decomposition is reported at [P] on every row (algebraic by Pontryagin character orthogonality). The 2nd-and-4th-order tangent-sub-bundle orthogonality on `D(ℂ⁶)` is reported at [P] (Paper 32 §13.2B audit triad). The row-generalization at the structural tier is [P] (algebraic); at the machine-floor numerical tier it is [P] (verified on `N ≤ 210`); for `N > 210` only the algebraic statement is [P], the numerical verification is deferred for compute. The all-orders extension is reported at [A]. The QG-mixing-bypass correspondence is reported at [A]/[C, reduced] (correspondence language only).

### 7.5 Failures-first-class (Paper 35 §3.6)

The numerical verification of `‖P_V · P_M‖_F` is skipped for `N > 210` due to memory constraints (the `2310 × 2310` and `30030 × 30030` complex projector matrices exceed the audit's per-row budget). This scope boundary is stated explicitly, not hidden; the algebraic statement on disjoint character index sets is the load-bearing claim for the larger rows. Audit δ (the all-orders extension) is named explicitly as the natural sequel; until executed, the all-orders extension stands at [A] without promotion. Audit ε (the QG-correspondence Lie-algebra check) is named in v2insert-02 §3.6 but not yet planned in detail; the QG-mixing-bypass correspondence remains at [C, reduced] without it.

### 7.6 Dimensional firewall (Paper 32 §11.2)

No physical units in any quantity of this paper. No Planck scale. No Newton constant `G`. No graviton mass. No cosmological constant. Only dimensionless quantities: character-index sets, projector matrix elements, Frobenius overlap norms (dimensionless ratios), Hessian signatures (integer triples `(p, q, r)`). The QG-mixing-bypass correspondence is *correspondence language* per Paper 32 §11.1; this paper does not promote it to a physical-QG-mechanism claim.

### 7.7 Carried-label discipline (Paper 32 §11.4)

Every QG label anchor-checked against its peer-reviewed source: graviton → Polchinski 1998 vol. 1, ch. 1; Planck scale → Weinberg 1995 vol. 1, eq. 5.7.11; asymptotic safety → Niedermaier & Reuter 2006, §1; renormalizability → Weinberg 1995 vol. 1, ch. 12; AdS/CFT → Maldacena 1997. The labels "kinematic sector", "gravity-adjacent sector", "designated overflow channel", "V/M decoupling", "Arithmetic Decoupling Theorem" are paper-internal program language; they correspond to but are not borrowed from external QG terms.

---

## 8. Open questions and carry forward

### 8.1 Audit δ — settled at K-branch (2026-05-20)

Audit δ ([`empirical/reports/audit_delta_settlement.md`](empirical/reports/audit_delta_settlement.md)) **settled** the all-orders extension at K-branch by a finite combinatorial proof on `(ℤ/N)^∧`: V_idx and M_idx are disjoint subsets of the dual group; V ⊥ M as Hilbert subspaces of `ℂ^N` by Pontryagin character orthogonality; the tensor power V^⊗m ⊥ (M-involving subspace) at every order m ≥ 2 by factor-wise inner product on tensor products; the closing-tuple constraint does not break the subspace orthogonality. Numerical verification at orders m = 2..6 on `ℤ/{6, 30, 210}` confirms at machine floor (max normalized Frobenius overlap `~10⁻¹⁶`). Audit ζ (counter-evidence search for higher-order V/M mixing) is **subsumed by audit δ**. Theorem 3.1 (D2)–(D3) extends to all orders on every primorial row at [P].

### 8.2 Audit ε — settled at K-branch (2026-05-20)

Audit ε ([`empirical/reports/audits_beta_gamma_epsilon_settlement.md`](empirical/reports/audits_beta_gamma_epsilon_settlement.md)) established the dictionary mapping each row of the QG-mixing-bypass correspondence (Polchinski 1998, Weinberg 1995–2000, Niedermaier–Reuter 2006, Maldacena 1997) to the program's V ⊥ M decoupling at the Lie-algebra-of-decoupling level. The load-bearing Lie-algebra statement: for any V-supported Hermitian `H_V` and M-supported Hermitian `K_M`, the commutator `[H_V, K_M]` acts trivially on both V- and M-tangent sub-bundles of `T_{ρ_*} D(ℂ^N)` at every order of the cumulant expansion (consequence of audit δ Step 3 lifted to commutators via factor-wise inner product on tensor powers).

Five rows of the §6.2 dictionary established at Lie-algebra precision: gravity sector ↔ M packet; matter / kinematic sector ↔ V packet; no natural Hilbert-space decoupling ↔ Pontryagin character orthogonality forces V ⊥ M; mixing at every loop order ⇒ non-renormalizable ↔ all-orders decoupling at [P] via audit δ; bypassed via extra structure (asymptotic safety, AdS/CFT, LQG, CDT, strings) ↔ bypassed *for free* by conductor-lattice arithmetic.

Paper 47 C2 promotes from [A]/[C, reduced] to **[P]-spirit** (structural identification with a peer-reviewed name; correspondence language per Paper 32 §11.1; the QG mechanism, the graviton, Planck scale, AdS/CFT, asymptotic safety, renormalizability are *not* derived).

### 8.3 Higher-order observable counter-evidence (audit ζ — subsumed by audit δ)

Audit ζ (originally named in v2insert-02 §3.6) was a counter-evidence search for explicit higher-order tensor observables on `D(ℂ⁶)` built from V-supported operators having non-trivial action on the M-Euclidean sub-bundle. **Audit δ's structural proof forecloses the possibility of any such counter-example** at any order on any squarefree primorial row: the V ⊥ M Hilbert-subspace orthogonality lifts to V^⊗m ⊥ (M-involving) at every m ≥ 2, so any tensor structure built from V-supported operators is, by construction, supported on V^⊗m and therefore HS-orthogonal to the M-involving complement. Audit ζ is no longer load-bearing.

### 8.4 Non-squarefree conductors — partially settled by audit χ (2026-05-20)

Audit χ ([`empirical/reports/audits_xi_chi_settlement.md`](empirical/reports/audits_xi_chi_settlement.md)) extended the Bures-Hessian sub-bundle audit to `D(ℂ¹⁰)` (squarefree non-primorial `ℤ/10 = 2·5`) and `D(ℂ¹²)` (non-squarefree `ℤ/12 = 2²·3`).

**On `ℤ/10` (squarefree non-primorial):** The V/M decomposition extends cleanly at K-branch. V_idx = `{2, 4, 5, 6, 8}` (`H_2 ⊕ H_5`, dim 5), M_idx = `{1, 3, 7, 9}` (`H_{10}`, dim 4). Hessian signature `(1, 4, 94)`, quartic signature `(4, 0, 95)`, V ⊥ M at `3.20 × 10⁻¹⁶`. The Arithmetic Decoupling Theorem extends to **every squarefree ring**, not just primorial rows.

**On `ℤ/12` (non-squarefree):** Three candidate decompositions audited at the Bures-Hessian tangent-sub-bundle tier:
- *Strict V/M* (V = `H_2 + H_3` dim 3; M includes `H_4 + H_6 + H_{12}` dim 8): K-branch, Hessian `(1, 2, 140)`, quartic `(8, 0, 135)`, V ⊥ M at `3.70 × 10⁻¹⁶`.
- *Inclusive V/M* (V = `H_2 + H_3 + H_4` dim 5; M = `H_6 + H_{12}` dim 6): K-branch, Hessian `(1, 4, 138)`, quartic `(6, 0, 137)`, V ⊥ M at `2.83 × 10⁻¹⁶`.
- *Trichotomy V/W/M* (V = `H_2 + H_3`; W = `H_4`; M = `H_6 + H_{12}`): **joint-on-disjoint** at tangent tier. V ⊥ W and V ⊥ M at machine floor, but **W ⊥ M overlap = 0.447** at the 4th-order quartic-form eigenspace level. The W-Euclidean and M-Euclidean tangent sub-bundles share tangent directions because off-diagonal-in-standard-basis tangent vectors have character-basis-diagonal entries spread across multiple `k` indices simultaneously.

**Settlement:** Theorem 3.1 (D1)–(D4) extends to non-squarefree rings under the **binary V/M decomposition** (either strict or inclusive); the trichotomy V/W/M is *not* a clean tangent-tier structural choice. For the AI manifestation on `ℤ/12` (Paper 36 / Paper 37 months task), the **inclusive V/M** (H_4 ∈ V) is the natural convention.

### 8.5 The composition with Papers 46 and 48

Paper 46 (proposed) load-bears the Hartle–Hawking signature on `ℤ/6` via the V-Lorentzian + M-Euclidean orthogonal sub-bundle decomposition. Paper 48 (proposed) load-bears the *quantitative capacity* of the V sector for cubic self-closure. Paper 47 (this paper) load-bears the V ⊥ M Hilbert-subspace decoupling — *why* the Hartle–Hawking signature is realizable on the lift and *why* the cubic self-closure capacity has a structural ceiling. The three are facets of one structural picture:

- **Paper 46** asks *what* the V/M decomposition looks like geometrically.
- **Paper 47** asks *why* the V/M decomposition is forced.
- **Paper 48** asks *how much* pure-V dynamics the system can host.

The single audit α/η on `ℤ/30` (v2insert-08) settled all three papers' row-generalization claims simultaneously; audits θ (v2insert-09) and ι (v2insert-10) extended the quantitative scaling. The proposed-paper triad now has *five empirical anchor points* across the primorial ladder.

### 8.6 The composition with Paper 49

Paper 49 (Draft 0.0) *The Arithmetic Decoupling of Projection-Closure Overflows* takes the V/M decoupling of this paper as the load-bearing arithmetic substrate for its universal-overflow framing across cosmology, deep learning, and active inference. Paper 47 is the *theorem statement*; Paper 49 is the *correspondence-readings synthesis*. Paper 49's universal-shape framing is [C, reduced] per its own discipline rails; Paper 47's structural decoupling theorem is [P] at 2nd/4th order on `ℤ/6` and [P] structurally (algebraically) on every primorial row.

---

## 9. Conclusion

The Arithmetic Decoupling Theorem is a structural fact of the categorical simplex on a primorial ring: the Hilbert space `ℂ^N` decomposes orthogonally as `V ⊕ M` where `V` collects the single-prime characters and `M` collects the cross-prime carry characters, and the decomposition is forced by Pontryagin character orthogonality on the dual group `(ℤ/N)^∧`. The induced 2nd-and-4th-order tangent-sub-bundle decomposition of `D(ℂ⁶)` at the centroid `ρ_*` separates the V-Lorentzian (1, 3) sub-bundle from the M-Euclidean (2, 0) sub-bundle at machine precision (Paper 32 §13.2B audit triad, [P]); the row-generalization to `ℤ/{30, 210, 2310, 30030}` is confirmed at the algebraic [P] tier and at the machine-floor numerical [P] tier where compute permits (audits α/η/θ).

The load-bearing arithmetic is one line: `⟨χ_k | χ_ℓ⟩ = N · δ_{k, ℓ}` for distinct characters of `(ℤ/N)^∧`. The structural-shape correspondence with the gravity-matter decoupling problem-shape of perturbative quantum gravity (Polchinski; Weinberg; Niedermaier–Reuter; Maldacena 1997) is **correspondence language**: the structural shape of how a kinematic sector decouples from a gravity-adjacent sector by Hilbert-space orthogonality matches the QG-program structural problem-shape; the literal QG mechanism, the graviton, the Planck scale, AdS/CFT, asymptotic safety, and renormalizability are *not* derived.

The discipline rails of Paper 32 §11.1 / §11.2 / §11.4 are binding throughout. The "QG-mixing-bypass" framing is correspondence language at the [C, reduced] tier; the V ⊥ M Hilbert-subspace decomposition is at the [P] tier on every primorial row; the all-orders extension is at the [A] tier pending audit δ. The three-outcome matched-pair rule (Paper 35 §3.1 + v2insert-04 §3.1) is binding: the row-generalization is K-branch on all five anchored rows; the all-orders extension and the QG-correspondence are pre-claimed three-outcome.

---

## Reproducibility artifacts

- [`empirical/paper32_13_2_bures_dispersion_audit.py`](empirical/paper32_13_2_bures_dispersion_audit.py) — Paper 32 §13.2 original audit; deterministic; signatures and overlaps to machine floor.
- [`empirical/paper32_13_2_reformulated_casimir_audit.py`](empirical/paper32_13_2_reformulated_casimir_audit.py) — Paper 32 §13.2A reformulation audit.
- [`empirical/paper32_13_2B_fourth_order_casimir_audit.py`](empirical/paper32_13_2B_fourth_order_casimir_audit.py) — Paper 32 §13.2B 4th-order extension audit; the load-bearing [P] for 2nd-and-4th-order V ⊥ M decoupling on `D(ℂ⁶)`.
- [`empirical/audits_alpha_eta_z30_primorial_generalization.py`](empirical/audits_alpha_eta_z30_primorial_generalization.py) — `ℤ/30` row-generalization; deterministic.
- [`empirical/audit_theta_capacity_scaling_primorial_ladder.py`](empirical/audit_theta_capacity_scaling_primorial_ladder.py) — primorial-ladder row-generalization; deterministic.
- [`empirical/reports/audits_alpha_eta_z30_settlement.md`](empirical/reports/audits_alpha_eta_z30_settlement.md) — settlement record for the `ℤ/30` row-generalization.
- [`empirical/reports/audit_theta_settlement.md`](empirical/reports/audit_theta_settlement.md) — settlement record for the primorial-ladder row-generalization.

---

## References

Maldacena, J. 1997. *The Large N limit of superconformal field theories and supergravity.* Adv. Theor. Math. Phys. **2**, 231–252.

Niedermaier, M.; Reuter, M. 2006. *The Asymptotic Safety Scenario in Quantum Gravity.* Living Rev. Relativ. **9**, 5.

Polchinski, J. 1998. *String Theory*, vol. 1. Cambridge University Press.

Weinberg, S. 1995–2000. *The Quantum Theory of Fields*, vols. I–III. Cambridge University Press.

Murillo Montero, L. 2026a. *One Functional, Four Forces.* Paper 32 of the categorical-simplex program, Draft 0.2.

Murillo Montero, L. 2026b. *The Jerk as Simplex Mass Term.* Paper 20 of the categorical-simplex program.

Murillo Montero, L. 2026c. *Bures Completion of Cubic Information Geometric Mechanics.* Paper 18 of the categorical-simplex program.

Murillo Montero, L. 2026d. *Grounded-Paranoid-Delusional Methodology.* Paper 35 of the categorical-simplex program.

Murillo Montero, L. 2026e (proposed). *Hartle–Hawking Signature on the Categorical Simplex.* Paper 46 of the categorical-simplex program (v2insert-01).

Murillo Montero, L. 2026f (proposed). *The Conductor Capacity Bound.* Paper 48 of the categorical-simplex program (v2insert-03 / 08 / 09 / 10).

Murillo Montero, L. 2026g. *The Arithmetic Decoupling of Projection-Closure Overflows.* Paper 49 of the categorical-simplex program, Draft 0.0.

---

*Paper 47 v0.3 — drafted 2026-05-20. Absorbs v2inserts 02 (theorem statement), 08 (`ℤ/30` row-generalization K-branch), 09 (primorial-ladder row-generalization K-branch), audit δ (all-orders Pontryagin proof, K-branch 2026-05-20), audit ε (QG-correspondence Lie-algebra dictionary, K-branch 2026-05-20), and audit χ (non-squarefree extension to `ℤ/10` + `ℤ/12`, K-branch at binary V/M, joint-on-disjoint at V/W/M trichotomy 2026-05-20). C1 [P] all-orders on every squarefree primorial row. C2 [P]-spirit (QG-mixing-bypass at Lie-algebra-of-decoupling level). C3 extends to non-squarefree rings under binary V/M (K-branch on ℤ/12 strict + inclusive); V/W/M trichotomy joint-on-disjoint at tangent tier (W ⊥ M overlap 0.447). C4 [P] (all-orders extension on `D(ℂ⁶)`); audit ζ subsumed by audit δ. Paper 32 §11.1 / §11.2 / §11.4 discipline rails binding throughout.*
