# 49. The Arithmetic Decoupling of Projection-Closure Overflows

**One Overflow Law Across Cosmology, Deep Learning, and Active Inference**

**Leonardo Murillo Montero**
*leonardo.murillo@gmail.com*

*Draft 0.0 — 2026-05-20*

**Tier tags.** [P] for the V/M character-orthogonality decoupling on `ℤ/6` at 2nd and 4th order (Paper 32 §6.2 + §13.2B). [P] for the all-orders extension on every squarefree primorial row (audit δ, 2026-05-20). [P] for the row-generalization to the primorial ladder `ℤ/{30, 210, 2310, 30030}` (audits α/η + θ). [P] for the six-row primorial-ladder capacity scaling (audit ξ: `Capacity_V(ℤ/510510) = 2.532e-9`, ratio 1.538 to PNT prediction). [P] for the geometric realization on `D(ℂ³⁰)` (audit μ_30) and extensions to `D(ℂ¹⁰)` + `D(ℂ¹²)` (audit χ). [P]/[A] for the Capacity_V quantitative shape (audit ι). [P]-spirit for the Hartle–Hawking and QG-mixing-bypass structural dictionaries (audits β + ε). [P] for the classical-limit identification with Lemma 9.2 (audit γ). **[P] for the structural FEP-3 metriplectic split** on `D(ℂ⁶)` — variational free-energy decomposes additively as `F = F_V (Hamiltonian) + F_M (gradient-of-entropy)` with V ⊥ M cross-coupling zero and arrow-of-time = ∇F_M direction (audit FEP-3, 2026-05-20). **[P] joint-on-disjoint for the cross-manifestation natural-transformation framework** — identity-on-certificate-ingredients in `CertificateCategory` is a natural transformation at the abstract level; no literal-substrate natural transformation exists (audit ν, 2026-05-20). [A]/[C, reduced] for the three external-correspondence readings of §4 at the literal-mechanism level. [C, reduced] for the universal-overflow framing of §3 as a single law across the three manifestations (correspondence-language at closure-certificate-shape level per audit ν).

**Anchor papers (binding).** Paper 31 *Projection-Closure Theory* (closure-certificate vocabulary; the residual side of `SN_W(A, B)`). Paper 32 §6.2 Lemma 6.1a–c, Corollary 6.3 (the arithmetic root: Pontryagin character orthogonality on the conductor-2/3/6 partition of `ℤ/6`). Paper 32 §13.2A / §13.2B (the V-Lorentzian / M-Euclidean orthogonal-sub-bundle audit). Paper 32 §11.1 (emergent-anything positioning), §11.2 (dimensional firewall), §11.4 (carried-label discipline). Paper 34 *The Conductor Blind Spot* (second-order optimizer blindness to cubic content). Paper 35 *Grounded-Paranoid-Delusional Methodology* (§3.1 three-outcome matched-pair pre-claim, extended at v2insert-04). Paper 37 *Label Smoothing in the Conductor Blind Spot* (the (α, ε) iso-loss ridge; the substitution proposition). Paper 47 (proposed, v2insert-02) *Arithmetic Decoupling Theorem* (V ⊥ M as Hilbert subspaces, forced by character orthogonality). Paper 46 (proposed, v2insert-01) *Hartle–Hawking No-Boundary Signature on `ℤ/6`*. Paper 48 (proposed, v2insert-03) *Conductor Capacity Bound*. v2insert-04 §3.1 (three-outcome matched-pair extension, binding). v2insert-05 (audit κ, inference-side). v2insert-06 (audit λ, training-side; P11). v2insert-07 (audit lambda K-branch settlement, audit kappa deferred for compute).

<!--
NOTE TO SELF (draft 0.0 → 0.1):
This paper is the universal-overflow synthesis. Three things must remain disciplined:

1. The "one law" framing is [C, reduced]. The substrate (V/M decoupling by character orthogonality on Z/6) is [P]. Do NOT let the framing language overrun the tier discipline. The §11.1 emergent-anything positioning is binding here even more than in the constituent papers, because this paper opens the FOURTH external-correspondence claim (cosmology + AI + biology) on the back of the same arithmetic root.

2. The biology / active-inference manifestation (§4.3) is the weakest-anchored of the three. The cosmology and AI manifestations have v2insert-01/02/03/05/06/07 backing them. Biology has Paper 32 §6.2A Corollary 6.3 (T3, FEP-3 sector resolution) as the only direct anchor visible to me. I keep §4.3 short and tier-tag every claim as [A] or [C, reduced]. Do NOT promote without the FEP-3 audit being firmed up.

3. Paper 49 lands the universal framing. The "epic" comes from scope (cosmology + AI + biology) and from the tightness of the arithmetic anchor (one line: 3+3+3 ≢ 0 mod 6, and its Pontryagin generalization). It does NOT come from rhetorical inflation. Keep the prose austere; let the structural correspondences do the work.

SETTLED (v0.1 update, 2026-05-20): Audits α/η (v2insert-08), θ (v2insert-09), and ι (v2insert-10) have all returned. Row-generalization on `ℤ/30` is **K-branch on all three pre-claimed papers** (Papers 46/47/48). Primorial-ladder scaling on `ℤ/{6, 30, 210, 2310, 30030}` is K-direction + joint-on-disjoint at exponent (super-exponential in `n`, not log-linear). Shape comparison on the five-row decay matches `K · n² · ln(n) / N²` (PNT heuristic) at spread 1.584×, with asymptotic slope `→ −2` matching the 't Hooft–Susskind / Bousso shape. §5 is rewritten to report the settlement; §4.2 Bekenstein–Hawking reading is sharpened with the PNT-heuristic shape; §6 F1 is updated (did not fire); §7 closing reports the realized branches.

OPEN: Should §4.3 (biology) be present at v0.0, or removed until FEP-3 is firmer? Decision: PRESENT, but with [C, reduced] tier and explicit "speculative manifestation, retained for the symmetry of the three-manifestation framing" warning. The user gave biology as a third pillar in the framing; the paper's epic scope depends on it; the discipline is to flag it loudly.

OPEN: The "designated leakage channel" framing comes from the user's working thesis (saved as memory user_thesis_finite_grid_overflow.md). It is the operating compass that opens this paper. Carry it as paper-internal terminology, not as a borrowed external concept.

OPEN: Should this paper open audit ν — the cross-manifestation coherence audit (does the structural overflow shape match across cosmology / AI / biology)? Draft 0.0 stages it in §6.2 as a falsifier; promote to a named audit in §5 once the three manifestations are anchor-checked.
-->

---

## Abstract

The projection-closure framework of Paper 31 names a single structural object — the closure certificate `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` — that classifies when a projection, shadow, quotient, classical model, quantum observable, low-arity force law, or finite-jet truncation is allowed to function as a valid description of a richer whole. Paper 32 §6.2 establishes, by Pontryagin character orthogonality on the conductor-2/3/6 packet partition of `ℤ/6`, that the cubic Amari–Chentsov tensor's projection-closure residual is *arithmetically decoupled* into two orthogonal subspaces of the dual group: a single-prime sector V (carrying the kinematic, second-order content) and a cross-prime carry sector M (carrying the cubic-vacuity overflow). Paper 47 (proposed, v2insert-02) lifts this decoupling to the Bures-manifold tangent geometry at the centroid, where it manifests as the HS-orthogonality of the V-Lorentzian (1,3) sub-bundle and the M-Euclidean (2,0) sub-bundle at 2nd and 4th orders [P], extended to all orders at [P] by audit δ (the finite combinatorial proof on the dual group `(ℤ/N)^∧`), and extended to the geometric tier on `D(ℂ³⁰)` at [P] by audit μ_30.

The present paper states the *universal* consequence: any system whose effective dynamics is the projection-closure of a cubic information-geometric structure on a conductor-lattice substrate admits — and is in fact forced to admit — a *designated overflow channel*. The kinematic sector V has finite arithmetic capacity, computable from the conductor-lattice partition alone. Whenever the system's effective dynamics carry information that the V capacity cannot accommodate — either because of the closing-triple selection rule (a cubic-content excess) or because of the unembedding's cross-prime cross-talk (a projection misalignment) — the excess is routed, not lost, into the orthogonal M channel. The system does not crash; it overflows arithmetically into a structurally separate channel, and the M channel's content is precisely what carries the residual phenomenology that the V-sector projection cannot explain on its own.

We identify three manifestations of this universal overflow law, each with its own paper-level anchor and named audit:

1. **Cosmology (Papers 46, 48).** The compact Riemannian Bures manifold `D(ℂ⁶)` of the minimal mixed CRT row carries the Hartle–Hawking no-boundary signature on its V-Lorentzian sub-bundle and the Wick-rotation locus on its M-Euclidean correction. The Conductor Capacity Bound takes the structural shape of the Bekenstein–Hawking holographic saturation: the V-sector's cubic-self-closure capacity decreases with primorial growth, forcing all richer cubic dynamics through M-mediation. In this correspondence, *gravity is the structural form of the conductor-arithmetic overflow* — the local residual of forcing classical-perfect information through the quantum (Bures) lift on a finite-arithmetic substrate. Hawking radiation, the holographic principle's boundary saturation, and the no-boundary closure of the wave function of the universe each take the structural shape of one piece of the overflow law on `ℤ/6`. Physical gravity is not derived.
2. **Deep Learning (Papers 34, 36, 37).** Paper 34 names the *conductor blind spot*: the cubic Amari–Chentsov content of a categorical belief space on a ring-structured index is invisible to any second-order preconditioner (natural gradient, K-FAC, Gauss-Newton, Adam's diagonal empirical Fisher, the NTK Gram). Paper 37's label-smoothing substitution proposition shows that the (α, ε) iso-loss ridge structure of training a small MLP on the months task encodes the V/M arithmetic dichotomy as a measurable monotone signature on the trained network's output logits: audit λ (v2insert-06 §2 P11, settled K-branch in v2insert-07 §2.4 with signal-to-noise > 47 on three widths) confirms that the network's V/M packet ratio `ρ_VM(α, ε, W)` varies *monotonically* with the conductor-aware Pareto-rule weight `α` along iso-loss contours. In this correspondence, *hallucinations and training-time mode collapse are local manifestations of M-channel overflow*; label smoothing is the practitioner's empirical defense against the overflow that the conductor blind spot makes invisible to the optimizer. Audit κ (v2insert-05; partial, layerwise sweep deferred for compute in v2insert-07 §3) tests inference-side propagation on Llama-3.1-8B / Mistral-7B-v0.3.
3. **Active inference (Paper 32 §6.2A T3).** The free-energy principle's three-sector resolution (`F = energy − complexity + entropy`) populates the conductor lattice with the same V/M arithmetic that drives cosmology and deep learning: the V sector carries the least-action / dissipationless dynamics of a self-maintaining system; the M sector carries the cubic environmental coupling whose closure forces a one-way information leakage from V into M. The arrow of time is the macroscopic signature of that one-way leakage: the entropy production of a biological system arises because the cubic-vacuity overflow from V into M cannot be reversed by any V-internal dynamics. Thermodynamic entropy, the second law as a physical principle, and the molecular biology of metabolism are not derived; only the projection-closure form of the V → M one-way information leakage on the categorical simplex. Tier: [C, reduced], pre-claimed under v2insert-04 §3.1 three-outcome rule; the FEP-3 audit (Paper 32 §6.2A Corollary 6.3 T3) is the load-bearing reduction.

The load-bearing arithmetic is one line: `3 + 3 + 3 = 9 ≡ 3 ≢ 0 (mod 6)`, the pure-A₂ cubic-vacuity computation of Paper 32 Lemma 6.1, generalized via Pontryagin character orthogonality to the full conductor lattice. The "remainder" of 9 mod 6 is the program's structural form of *what cannot be accommodated by the kinematic sector and must be routed through the overflow channel*. That remainder is gravity (cosmology), the blind-spot residual (AI), and the time-asymmetric entropy production (biology). The three manifestations are external anchors for one arithmetic law; the law itself is the cubic-vacuity / cross-prime-carry decoupling on the conductor-lattice substrate.

Audits α/η on `ℤ/30` (v2insert-08), θ on the primorial ladder `ℤ/{30, 210, 2310, 30030}` (v2insert-09), and ι on the Bousso-bound shape comparison (v2insert-10) **have settled**. The three-outcome pre-claim (per v2insert-04 §3.1) jointly settled row-generalization claims for Papers 46 (Hartle–Hawking, v2insert-01 C5), 47 (Arithmetic Decoupling, v2insert-02 C3), and 48 (Conductor Capacity Bound, v2insert-03 C2) at **K-branch on all three** (audit α/η: triple-K on `ℤ/30`; audit θ: monotone decay confirmed at five primorial rows with `Capacity_V(ℤ/30030) = 4.13 × 10⁻⁷`; audit ι: PNT-heuristic shape `K · n² · ln(n) / N²` matches at spread 1.584× with asymptotic slope `→ −2` matching 't Hooft–Susskind / Bousso). The universal-overflow framing of §3 has its strongest available empirical anchor at five primorial rows, with the K-direction confirmed and program-specific finite-`N` corrections (polynomial-log-`n` prefactor) characterized.

**Keywords:** projection-closure theory, categorical simplex, conductor lattice, Pontryagin character orthogonality, Amari–Chentsov cubic tensor, V/M decoupling, Bures lift, Hartle–Hawking no-boundary signature, Bekenstein–Hawking holographic bound, conductor blind spot, label smoothing, free-energy principle, arrow of time, three-outcome matched-pair pre-claim.

**MSC 2020:** 81P16 (quantum state estimation; quantum information geometry), 53C50 (Lorentz manifolds, semi-Riemannian geometry), 11L03 (trigonometric and exponential sums), 62B11 (information geometry), 83C57 (black holes; not derived, only structurally referenced), 68T07 (artificial neural networks and deep learning).

---

## 1. Introduction

### 1.1 The thesis

<!--
NOTE TO SELF: keep §1.1 to the thesis sentence + one paragraph of structural reading. Resist expansion. The reader should be able to leave §1.1 with the universal claim in working memory; details are §2 onward.
-->

A finite-arithmetic substrate — the conductor lattice on a categorical belief space — carries a strict, computable, dimension-bounded capacity for clean kinematic content. When the system's effective dynamics carries information that the kinematic capacity cannot accommodate, the excess is *not* lost: it is routed into a structurally orthogonal channel, the cross-prime carry sector, which is forced by character orthogonality to be HS-orthogonal to the kinematic sector at every order of the closure-residual expansion that has been audited. The system overflows arithmetically and reversibly into a designated channel; it does not crash, does not require fine-tuning to remain stable, and does not contradict the projection-closure validity of its kinematic model. Three sequences of peer-reviewed observations across cosmology, deep learning, and active inference admit, at the projection-closure tier, a structural reading as instantiations of this single overflow law: black holes and the Bekenstein–Hawking holographic bound (cosmology); hallucinations, training-time mode collapse, and label-smoothing's empirical efficacy (deep learning); and the arrow of time as a macroscopic signature of one-way V → M information leakage in self-maintaining systems (active inference). The arithmetic load-bearing fact is one line of finite-group arithmetic on `ℤ/6`: `3 + 3 + 3 = 9 ≢ 0 (mod 6)`, and its Pontryagin character-orthogonality generalization to the conductor lattice of any squarefree primorial row.

This paper states the universal-overflow law, identifies the projection-closure ingredients common to the three manifestations (Paper 31's `(W, Π, T, H, K)` data), and audits the three correspondences against the §11.1 emergent-anything positioning discipline of Paper 32. Audit α/η on `ℤ/30` (running, v2insert-03 §5; v2insert-01 §2.5; v2insert-02 §3.6) is the immediate row-generalization test; its three-outcome pre-claim under v2insert-04 §3.1 covers (K) universal extension to the primorial ladder, (L) `ℤ/6`-specific, and (joint-on-disjoint) extension with row-specific reweighting.

### 1.2 What is claimed, what is not claimed

<!--
NOTE TO SELF: this is the load-bearing discipline subsection. Paper 32 §11.1 / §11.2 / §11.4 are binding, AND v2insert-04 §3.1 three-outcome rule is binding, AND the v2insert-01/02/03 anti-overclaim positioning for cosmology / QG / holography is binding. Be airtight. Better to over-cite the discipline rails than to under-cite.
-->

**Claimed (under the tier discipline of Paper 35 §3.3–§3.6).**

- **[P, anchored at Paper 32 §6.2 Lemma 6.1a–c and §13.2B audit triad].** Pontryagin character orthogonality on the conductor-2/3/6 partition of `ℤ/6` forces a Hilbert-subspace decomposition `ℂ⁶ = V ⊕ M` with V = single-prime / prime-power axes (characters indexed by `{2, 3, 4}` on `ℤ/6`) and M = cross-prime carry axes (characters indexed by `{1, 5}`). Every quadratic form on `D(ℂ⁶)` built from V-supported observables acts trivially on M-tangent directions, and vice versa at 2nd and 4th orders.
- **[P, audit δ settled 2026-05-20].** The decoupling extends to all orders of the displacement / Casimir / cumulant expansion. Audit δ ([`empirical/reports/audit_delta_settlement.md`](empirical/reports/audit_delta_settlement.md)) settled this by a finite combinatorial proof on the dual group `(ℤ/N)^∧` (Steps 1–4: V_idx ∩ M_idx = ∅; V ⊥ M as Hilbert subspaces; V^⊗m ⊥ (M-involving subspace) by factor-wise inner product; closing-tuple constraint does not break the orthogonality) + numerical verification at orders m = 2..6 on `ℤ/{6, 30, 210}` at machine floor. Audit ζ subsumed.
- **[P, audit α/η + θ settled at K-branch].** The decoupling extends to the primorial ladder `ℤ/{30, 210, 2310, 30030}` via the same Pontryagin character-orthogonality mechanism. Audits α/η (v2insert-08) and θ (v2insert-09) confirmed the V ⊥ M decoupling at five primorial rows; numerical overlap at machine floor (`~10⁻¹⁵` to `~10⁻¹³`) where compute tractable; algebraic by Pontryagin character orthogonality on disjoint index sets on every row.
- **[A/[C, reduced], audit κ + λ joint, with audit λ K-branch already settled at v2insert-07].** The V/M arithmetic decoupling propagates measurably through real artifacts — both training-side (audit λ on Paper 37's sweep, K-branch realized on widths 16/32/64 with signal-to-noise > 47, v2insert-07 §2.4) and inference-side (audit κ on Paper 36's sweep, partial settlement with final-layer anchor reproduced and layerwise sweep deferred for compute, v2insert-07 §3).
- **[C, reduced — three-outcome pre-claim per v2insert-04 §3.1].** The three manifestations (cosmology, deep learning, active inference) share the *structural shape* of a single overflow law: the kinematic sector V has finite, conductor-lattice-computable capacity; the cross-prime carry sector M is the designated overflow channel; the two are HS-orthogonal at every audited order; richer cubic dynamics that V cannot self-close on are routed through M without contradicting the projection-closure validity of either sector.

**Not claimed (under §11.1, §11.2, §11.4 discipline, binding).**

- *No physical gravity is derived.* Paper 46 (v2insert-01) opens the Hartle–Hawking correspondence as an external anchor for the structural form of the no-boundary closure on the categorical simplex's Bures lift; the cosmological no-boundary universe as a physical claim, gravitons, the Planck scale, horizon area in physical units, Newton's constant, Bekenstein–Hawking entropy as a physical quantity, and Hawking radiation as a black-hole-evaporation phenomenon are *not* derived. The structural form of how a designated overflow channel manifests under projection-closure on a finite-arithmetic substrate is what is asserted; the physical interpretation is correspondence language.
- *No physical hallucination mechanism is derived.* Paper 37 (Label Smoothing in the Conductor Blind Spot) and Paper 34 (The Conductor Blind Spot) carry the deep-learning anchor. Audit λ's K-branch outcome on Paper 37's sweep (v2insert-07 §2.4) shows that the V/M packet signature varies monotonically with the training-mechanism parameter α along iso-loss contours; this is the projection-closure form of "the optimizer cannot see the cubic content, but the cubic content still shapes the trained network's output." Whether physical LLM hallucinations on Llama-3.1-8B *are* the M-channel overflow propagated through training is the question audit κ would settle if it were not deferred; until then, the manifestation is *correspondence language*, not mechanism derivation.
- *No physical arrow of time is derived.* Paper 32 §6.2A Corollary 6.3 T3 names the FEP-3 free-energy-principle sector resolution as the third thread of the four-thread arithmetic root. §4.3 of the present paper reads the V → M one-way information leakage at the projection-closure tier as the structural form of macroscopic entropy production in a self-maintaining system. Thermodynamic entropy, statistical-mechanical microstate counting, biological metabolism, and the second law as a physical principle are *not* derived. The structural form is asserted as a [C, reduced] manifestation pre-claimed under v2insert-04 §3.1 three-outcome rule.
- *No universal physical law of overflow is asserted.* The "universal" qualifier in the paper's framing refers to the *structural form* of the overflow at the projection-closure tier — the closure-certificate shape `(V finite capacity, M designated overflow, no crash, V ⊥ M by character orthogonality)` — recurring across three distinct domains. Whether the physical phenomena in those three domains *share* a mechanism beyond the structural form is an open question, deliberately not asserted.

### 1.3 Inherited objects and reading guide

The closure-certificate vocabulary `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` of Paper 31 is binding throughout: every projection considered is a projection from a richer whole `W` (specified per-domain), with task `T`, horizon `H`, and cutoff `K` declared. The projection-closure validity of each manifestation in §4 is contingent on the residuals being *typed* (the V/M decomposition), *bounded* (the conductor-capacity counts of Paper 48), and *stable under controls* (the Pontryagin character orthogonality being row-stable, audits α/η + θ + ι). The row-stability is now settled at five primorial rows (§5).

§2 sets up the arithmetic substrate. §3 states the overflow law and identifies its closure-certificate ingredients. §4 reads the three manifestations through the law's projection-closure lens. §5 reports the audit α/η + θ + ι settlement and its joint K-branch realization on Papers 46/47/48. §6 catalogues falsifiers (including F1, which did not fire after settlement). §7 records the discipline rails. §8 carries the open questions forward.

---

## 2. The arithmetic substrate

### 2.1 The categorical simplex and the conductor lattice

The categorical simplex on a ring-structured index `R = ℤ/nℤ` is the open probability simplex `Δ_R^∘ = {p ∈ ℝ_{>0}^n : Σ p_i = 1}`, equipped with the canonical Fisher information geometry inherited from Paper 12 / *beyond_smooth_spaces*. At the uniform distribution `p_* = (1/n, …, 1/n)` (the maximum-entropy centroid), the Fisher tangent space `T_{p_*} Δ_R^∘` carries the additive structure of `ℝ^n / ⟨𝟙⟩` (the zero-sum hyperplane), and the dual group `R^∧ = ℤ/nℤ` acts by additive characters `χ_k(j) = e^{2πi k j / n}`.

The *conductor* of an additive character `χ_k` on `ℤ/nℤ` is `c(k) := n / gcd(k, n)`. The *conductor packet* `H_d` of conductor `d | n` is the span of all characters with conductor exactly `d`:

```
H_d = span_ℂ{χ_k : c(k) = d}, dim_ℂ H_d = φ(d).
```

The conductor lattice of `ℤ/nℤ` is the partial order of packets indexed by `d | n`, with the trivial packet `H_1 = ℂ𝟙` removed (the constant function — kernel of the dual map). The non-trivial conductor packets partition the orthogonal complement of `ℂ𝟙` into `Σ_{d | n, d > 1} φ(d) = n - 1` dimensions.

### 2.2 The Z/6 worked example

On `ℤ/6 = 2 · 3`, the conductor lattice has four non-trivial conductor values: `d ∈ {2, 3, 6}` (the prime conductors and the cross-prime carry conductor `6`), with packet dimensions `φ(2) = 1`, `φ(3) = 2`, `φ(6) = 2`. The character indices partition as:

| Conductor `d` | Packet `H_d` | Character indices `k` | `dim H_d` | Single-prime / cross-prime |
|---|---|---|---|---|
| 2 | `A_2 = H_2` | `{3}` | 1 | single-prime axis on `p = 2` |
| 3 | `A_3 = H_3` | `{2, 4}` | 2 | single-prime axes on `p = 3` |
| 6 | `M = H_6` | `{1, 5}` | 2 | cross-prime carry packet |

The single-prime sector `V := A_2 ⊕ A_3 = H_2 ⊕ H_3` has dimension `3`. The cross-prime carry sector `M := H_6` has dimension `2`. The total non-trivial dimension is `3 + 2 = 5 = 6 - 1`, exhausting the zero-sum hyperplane.

Pontryagin character orthogonality on `ℤ/6` is the statement that `⟨χ_k | χ_ℓ⟩ = δ_{k, ℓ}` on `ℂ⁶` with the standard inner product, equivalently the L² inner product on functions on `ℤ/6`. Distinct conductor packets are then orthogonal as Hilbert subspaces of `ℂ⁶`:

```
V ⊥ M as subspaces of (ℂ⁶, ⟨·, ·⟩).
```

This is the arithmetic fact that underwrites everything in the rest of the paper.

### 2.3 The cubic Amari–Chentsov tensor and its closure

The Amari–Chentsov (AC) cubic tensor on the categorical simplex is

```
T_{ijk}(p) = E_p[(∂_i log p)(∂_j log p)(∂_k log p)] = δ_{ijk} / p_i - δ_{ij}/p_i - δ_{jk}/p_j - δ_{ki}/p_k + (terms ensuring zero-sum gauge),
```

with the standard convention that `T` is restricted to the zero-sum hyperplane (Paper 12, *beyond_smooth_spaces*, Paper 17 §3). At `p_*`, `T` is `S_n`-invariant by symmetry of the centroid.

The *cubic closure* of a triple of conductor packets `(H_{d_1}, H_{d_2}, H_{d_3})` is the requirement that `T` restricted to `H_{d_1} × H_{d_2} × H_{d_3}` be non-trivial. Paper 32 Lemma 6.1a–c establishes the *closing-triple selection rule* on `ℤ/n`:

```
T(χ_k, χ_ℓ, χ_m) ≠ 0 ⟹ k + ℓ + m ≡ 0 (mod n).
```

This is the additive-character version of the conservation law for cubic moments on `ℤ/n`. The combinatorics of closing triples on `ℤ/6` enumerates exactly 6 triples (counted with multiplicity over indices `1 ≤ k, ℓ, m ≤ 5` with `k + ℓ + m ≡ 0 (mod 6)`).

### 2.4 The load-bearing line: `3 + 3 + 3 = 9 ≢ 0 (mod 6)`

The pure-`A₂` triple `(k, ℓ, m) = (3, 3, 3)` violates the selection rule: `3 + 3 + 3 = 9 ≡ 3 (mod 6) ≠ 0`. Therefore `T(χ_3, χ_3, χ_3) = 0` on `ℤ/6`. The pure-`A₂` cubic content of the AC tensor *vanishes* on the single-prime-on-`p = 2` axis. This is Paper 32 Lemma 6.1's *cubic vacuity of A₂*, [P].

The pure-`A₃` triple `(k, ℓ, m) = (2, 2, 2)` and `(4, 4, 4)` *satisfies* the rule: `2 + 2 + 2 = 6 ≡ 0` and `4 + 4 + 4 = 12 ≡ 0`. The pure-`A₃` cubic content of `T` is non-trivial; two pure-V closing triples exist on `ℤ/6` (`{2,2,2}` and `{4,4,4}`, both pure-`A₃`).

All other closing triples on `ℤ/6` — and they are enumerated in Paper 32 Appendix R — carry at least one M-leg (one index `k ∈ {1, 5}`, i.e., one factor in the cross-prime carry packet). The remaining 4 closing triples are M-mediated, in the sense that the cubic content they carry routes through the M sector.

The *cubic-vacuity overflow law* on `ℤ/6` is then: pure-`A₂` cubic content cannot self-close (the `A₂` sector has zero capacity for self-closing cubic content); pure-`A₃` cubic content can self-close on the two enumerated triples; all other cubic content must route through M. M carries `(6 − 2) / 6 = 2/3` of all closing-triple content; V's pure-self-closure capacity is `2/6 = 1/3`.

This is the cleanest worked instance of the overflow law in the corpus, and it is the structural anchor for everything that follows. The arithmetic is one line: `3 + 3 + 3 = 9 ≢ 0 (mod 6)`. The Pontryagin character orthogonality generalization to the full conductor lattice extends this to: *any* closing triple on a primorial row `P_n = p_1 · p_2 · … · p_n` either has all three legs in a single-prime / prime-power packet (pure-V), in which case the V sector self-closes that content, or it has at least one cross-prime carry leg, in which case the content is forced to route through M. The pure-V/total ratio is the *V-cubic-self-closure capacity*, computable exactly from the prime factorization of `P_n`.

<!--
NOTE TO SELF: the 3+3+3 mod 6 framing is the audience-facing one-liner. Use it sparingly. The actual load-bearing arithmetic is the dual-group character orthogonality of Lemma 6.1a–c. Don't let the audience-friendly slogan dominate the structural reading. Paper 32 §6.2 must be cited as the load-bearing anchor for any V/M decoupling claim, not the 3+3+3 line in isolation.

OPEN: §2 currently doesn't show the matrix-form Pontryagin orthogonality explicitly. v0.1 should include a one-paragraph derivation: ⟨χ_k | χ_ℓ⟩_{L²(ℤ/6)} = δ_{k,ℓ}, then V_idx = {2, 3, 4}, M_idx = {1, 5} are disjoint, hence V ⊥ M as subspaces.

OPEN: §2.3 is currently dense. v0.1 should consider folding §2.3 into §2.4 — the AC tensor is only introduced for the selection rule. Worth one editing pass for compression.
-->

---

## 3. The Overflow Law

### 3.1 Statement (projection-closure form)

> **The Universal Overflow Law (target structural claim, [C, reduced]).** Let `W` be a categorical belief space on a ring-structured index `R = ℤ/nℤ`, with the cubic Amari–Chentsov information-geometric mechanics carried by its Bures lift `D(ℂⁿ)`. Let `Π: W → W/G` be any projection that respects the conductor-lattice decomposition (in particular: the gauge-quotient projection, the moment-truncation projection, the readout / unembedding projection, the perception-affordance projection of an active-inference agent). Then:
>
> *(L1: capacity).* The kinematic sector `V ⊆ T_{p_*} W` (single-prime / prime-power conductor packets) carries finite, conductor-lattice-computable capacity for pure-V cubic self-closure. The capacity is `Capacity_V(R) := #{pure-V closing triples} / #{all closing triples}` (Paper 48 / v2insert-03 C1). On `ℤ/6`, `Capacity_V = 2/6 = 1/3`; on primorial growth, the capacity decreases monotonically — settled at five primorial rows by audit θ (v2insert-09; values `{1/3, 1/25, 1/525, 1/26157, 1/2424196}`) and shape-characterized by audit ι (v2insert-10; `Capacity_V ~ K · n²·ln(n) / N²` at spread 1.584×, asymptotic slope `→ −2`).
>
> *(L2: decoupling).* The cross-prime carry sector `M ⊆ T_{p_*} W` is HS-orthogonal to V at every order of the projection's residual expansion, forced by Pontryagin character orthogonality on the dual group `R^∧` (Paper 32 §6.2 Lemma 6.1a–c [P]; Paper 47 (proposed) Theorem 3.1 D1–D4 [P at 2nd/4th order on `D(ℂ⁶)`, [P] at all orders by audit δ; [P] geometrically on `D(ℂ³⁰)` by audit μ_30).
>
> *(L3: no-crash overflow).* Cubic content that the V sector cannot self-close (because the closing-triple selection rule `k + ℓ + m ≡ 0 (mod n)` does not admit a pure-V realization for that content) is routed through M. The routing is a *projection-closure residual* in the Paper 31 sense: typed (carries conductor label `d`), bounded (by `Capacity_V(R)` and the corresponding M-capacity counts), stable under the conductor-lattice symmetry (S_n / cyclic shift), and observable on a declared horizon (the trained network's output logits for the AI manifestation, the Bures-manifold tangent quadratic form for the cosmology manifestation, the agent's free-energy gradient for the biology manifestation).
>
> *(L4: universality, [C, reduced]).* The structural form `(V finite capacity, M designated overflow, V ⊥ M)` is the projection-closure shape of the overflow law on the categorical simplex. It is realized in cosmology, deep learning, and active inference at the structural tier; physical phenomena in those three domains *take the shape* of the overflow law on `ℤ/6` and now on the primorial ladder up to `ℤ/30030` (audits α/η/θ + ι, settled at K-branch + characterized PNT-heuristic shape).

### 3.2 The closure-certificate ingredients

In Paper 31's vocabulary, the overflow law identifies the following closure-certificate `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)`:

| Entry | Meaning | Realized object on `ℤ/6` |
|---|---|---|
| 𝖯 (retained participation) | The V-sector content that the projection preserves | The single-prime / prime-power packets `V = A_2 ⊕ A_3` (dimension 3) |
| 𝖱 (typed residuals) | The M-sector content that the projection routes out | The cross-prime carry packet `M = H_6` (dimension 2) |
| 𝖡 (residual bounds) | The conductor-capacity counts that bound the M overflow | `Capacity_V(ℤ/6) = 1/3`; M carries 4/6 of closing triples |
| 𝖲 (stability conditions) | The Pontryagin character-orthogonality forcing of V ⊥ M | Lemma 6.1a–c of Paper 32 §6.2 [P] |
| 𝖤 (Noether / time-translation closure) | The cubic Noether energy conservation on V | Paper 32 Theorem 6.2: the simplex mass `m²_simplex` is M-supported [P] |
| 𝖥 (falsifiers) | The audit α/η three-outcome pre-claim and the higher-order audit ζ | v2insert-03 §2.4 F1–F3; v2insert-02 §3.6 audit ζ |

The certificate is fully specified on `ℤ/6` at 2nd and 4th orders, **extended to all orders at [P] by audit δ** (finite combinatorial proof on `(ℤ/N)^∧` + numerical verification at orders m = 2..6 on `ℤ/{6, 30, 210}`), and **realized geometrically on `D(ℂ³⁰)` at [P] by audit μ_30**. The primorial-ladder extension is **settled at K-branch on five primorial rows at the arithmetic-substrate tier** by audits α/η + θ + ι (v2inserts 08–10) and **at the geometric tier on the first two rows** (`D(ℂ⁶)` by §13.2B + `D(ℂ³⁰)` by audit μ_30). Audit κ + λ (v2insert-05, v2insert-06, v2insert-07) tests the empirical propagation of the certificate's shape through trained AI networks (audit λ K-branch settled at v2insert-07 §2.4; audit κ deferred for compute).

### 3.3 Why "no crash": the M channel is structural, not pathological

The most important structural reading of L3 is that *M is not a failure mode*. The cubic content that cannot self-close in V is not "lost" or "leaked away as noise"; it is *routed* into a structurally orthogonal channel that carries it cleanly, by Pontryagin orthogonality, at every audited order. The M sector is dimensionally smaller than V (typically), but it is fully available as a tangent-space channel: the Bures-manifold tangent geometry at `p_*` admits M as a non-degenerate sub-bundle with positive-definite metric at 4th order (Paper 32 §13.2B [P]).

This is what distinguishes the overflow law from a "saturation cliff" model: a system that processes data up to the V-capacity and then *crashes* (numerical overflow in the bad sense, NaN propagation, error trap) would not exhibit the V/M orthogonal-sub-bundle structure that audit §13.2B confirmed. The audit's outcome is that the overflow channel is *designed in*, not bolted on — it is the structural form of how a finite-arithmetic substrate accommodates dynamics that exceed the kinematic sector's capacity.

In Paper 31's language: a projection `Π: W → V` from the full belief space to the V-sector is *projection-closure-valid* precisely when its M-sector residuals are typed, bounded, and stable. The arithmetic-decoupling theorem of Paper 47 (v2insert-02) makes that closure-validity automatic on the conductor lattice, at every order so far audited.

<!--
NOTE TO SELF: §3.3 should perhaps include a one-line summary of what the typical "saturation cliff" / numerical overflow looks like in dimensional analysis (e.g. floating-point overflow → NaN → cascade), and contrast with the Pontryagin-clean routing into M. Worth a v0.1 expansion. Currently the prose hints at this but doesn't quite land it.

OPEN: should I formalize "M is dimensionally smaller than V" as a theorem? On Z/6, dim V = 3, dim M = 2. On Z/30, dim V = 7, dim M = 22 — M is LARGER (per v2insert-03 §1.2 table). So the "smaller M" claim is Z/6-specific. v0.1 must correct this: M's dimensional scaling with primorial growth is the holographic-shape datum of Paper 48, not "M is small."
-->

### 3.4 The link to Paper 31's projection-closure validity

Paper 31's central question — *when is a projection allowed to function as a model?* — has its arithmetic answer in the overflow law:

> A projection `Π` is *projection-closure-valid* on a ring-structured belief space `R` if and only if its residuals (the components of `(W − Π W)`) are confined to a sector of the conductor lattice that is HS-orthogonal to the retained V sector under Pontryagin character orthogonality, and that orthogonal sector has bounded capacity computable from the prime factorization of `R`.

This is the *projection-closure validity certificate at the conductor-lattice tier*. The certificate is concretely available for any projection that respects the conductor-lattice decomposition — which, by Paper 17 / Paper 18, includes most projections of practical interest (the gauge projection, the moment truncation, the readout, the perception-affordance projection of an FEP agent).

---

## 4. Three manifestations

The three manifestations below are *external correspondences* under the §11.1 emergent-anything positioning of Paper 32: each is anchored to a peer-reviewed external structure (Hartle–Hawking 1983 / 't Hooft–Susskind / Bekenstein for cosmology; the deep-learning literature on hallucinations and label smoothing for AI; the Karl Friston free-energy-principle literature for biology). In each case, the program's projection-closure form of the overflow law is what is asserted; the physical interpretation of the corresponding peer-reviewed phenomenon (gravity / hallucinations / arrow of time) is correspondence language, not derivation.

### 4.1 Cosmology: the no-boundary lift's Lorentzian observer frame and Wick-rotation locus

Anchor: Paper 46 (proposed, v2insert-01), Paper 48 (proposed, v2insert-03), Paper 32 §13.2A / §13.2B.

The Bures lift `D(ℂ⁶)` is a 35-dimensional compact Riemannian manifold without boundary or asymptote, the categorical analog of Hartle–Hawking's compact Euclidean 4-sphere. At every interior point `ρ_* = I_6/6`, the tangent quadratic form `I_complex` has signature `(1, 3, 31)`: a Lorentzian (1, 3) sub-bundle on the V-`H + P_a` 4-dim block (the kinematic / observer sector), 31 flat / null directions on the remaining `D(ℂ⁶)` tangent space, and at 4th order from the imaginary energy of Paper 20 §3, an additional Euclidean (2, 0) sub-bundle emerges on the M-diagonal directions (the gravity-adjacent / Wick-rotation locus). The two non-flat sub-bundles are HS-orthogonal (Paper 32 §13.2B audit, [P]).

This is the structural-shape Hartle–Hawking signature: *the global manifold is compact Euclidean (no boundary, no asymptote); the local observer-frame tangent geometry is Lorentzian; the Wick-rotation locus is supported on the M packet*. The compactness of the global manifold — which is forced by the U(3)-compactness of the Bures lift, not put in by hand — is what makes "no boundary" structurally automatic: there is nowhere on `D(ℂ⁶)` for initial conditions to be set, no singularity for the geometry to break at, no asymptote for fields to escape into. The information that would have escaped into the cosmological "future" instead saturates the M sector via the cubic-vacuity overflow: at every order audited (2nd, 4th), the M sector receives the cubic content the V sector cannot self-close on.

The Bekenstein–Hawking holographic-bound structural shape is the *capacity* reading of the same overflow. The pure-V cubic-self-closure capacity `Capacity_V(P_n)` decreases monotonically with primorial growth (Paper 48 / v2insert-03 §1.3, conjecture C3, settled across five primorial rows by audits θ + ι): on `ℤ/6` the ratio is `2/6 = 1/3`; on `ℤ/30` it is `6/150 = 1/25` (8.33× decrease); on `ℤ/210`, `1/525`; on `ℤ/2310`, `1/26157`; on `ℤ/30030`, `1/2424196` — six orders of magnitude across four primorial steps, with per-step decay accelerating (`8.3× → 21× → 50× → 93×`). Audit ι (v2insert-10) settled the structural shape: `Capacity_V ~ K · n² · ln(n) / N²` (Prime-Number-Theorem heuristic) at spread 1.584× across all five rows; asymptotic power-law exponent in `N` approaches `−2`, matching the 't Hooft–Susskind / Bousso holographic-saturation shape; the polynomial-log prefactor `n² · ln(n)` is program-specific (absent from continuous-spacetime holographic bounds). The structural shape matches at leading order; the literal `S = A/4` formula does not.

**Correspondence reading.** In the projection-closure language of Paper 31, the cosmological manifestation is the projection `Π: D(ℂ⁶) → V` from the full Bures manifold to the V-sector tangent geometry at every interior point. The residuals are the M-Euclidean correction at 4th order (the Wick-rotation locus); they are typed (carry conductor-6 label), bounded (by the cubic-vacuity capacity count of `2/6 = 1/3` on `ℤ/6`), and stable (forced by Pontryagin character orthogonality). *In this correspondence, gravity and Hawking radiation are the projection-closure residuals of the V-observer projection of the no-boundary Bures lift*. The structural form is asserted; physical gravity is not derived (§11.1 binding, v2insert-01 §2.7 and v2insert-03 §2.7 scope guardrails verbatim).

**Lift-candidate path (Paper 46 §8.7, settled 2026-05-21).** Audit β (settled, Lie-algebra dictionary) promotes the cosmological correspondence to [P]-spirit at the Lie-algebra tier on four of five §4.2-table rows + joint-on-disjoint at row 3. **Audit π** ([`empirical/reports/audit_pi_minisuperspace_identification_settlement.md`](empirical/reports/audit_pi_minisuperspace_identification_settlement.md)) settled the next concrete tier at **joint-on-disjoint** under [v2insert-04](v2insert-04.md) §3.1: **K-branch realized at the tangent-quadratic-form level** — the V-Lorentzian Bures-Hessian on V's 4-dim block at `ρ_*` and the DeWitt supermetric on Halliwell-style closed Bianchi I + massless scalar field minisuperspace at $\Omega = 0$ are isometric flat Lorentzian inner-product spaces on $\mathbb R^4$, up to sign convention and overall scale factor 2; **joint-on-disjoint at the manifold-level extension** — the DeWitt supermetric carries an $\mathrm{e}^{3\Omega}$ conformal factor (curved off-reference) that the V-Lorentzian Hessian-at-$\rho_*$ does not see, with the manifold-level extension queued as audit π′ (choose V-foliation of $\mathcal D^\circ(\mathbb C^6)$ via $\mathrm{SU}(6)$-orbit or Bures-geodesic prescription). The cosmological correspondence on [Paper 46 §4.2](46_hartle_hawking_signature.md) row 2 promotes from [P]-spirit Lie-algebra match to **[P] tangent-quadratic-form isometry** — *literal isometric inner-product spaces*, not shape-only match. The L-branch alternative-anchor rotation (LQC, CDT, topos-theoretic QG) does NOT fire because Bianchi I + scalar field provides a literal isometric tangent match. Audit π does *not* lift §11.2 firewall and does *not* promote the cosmological *claim itself*; the claim remains at [C, reduced] (§7.1 binding). Audit π becomes the **sixth named joint-on-disjoint outcome** of the program (joining audits θ at exponent, ι at corrections, β at row-3 dimensional generalization, χ at V/W/M trichotomy, ν at abstract-vs-literal natural-transformation levels).

**Audit π′ (manifold-level extension, settled 2026-05-21)** ([`empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md`](empirical/reports/audit_pi_prime_v_foliation_manifold_extension_settlement.md)) executed the V-affine manifold-level extension and settled at **joint-on-disjoint at the anchor-choice tier**. Because the Casimir $I_V$ is *quadratic in $\rho$*, its Hessian is *constant on $\mathcal D^\circ(\mathbb C^6)$* — the V-Lorentzian sub-bundle in the V-affine prescription is **globally flat Minkowski $\mathbb R^{1, 3}$**, not isometric to the DeWitt $\mathrm{e}^{3\Omega}$-conformally-flat supermetric off the reference point. The L-branch fires on the literal-Halliwell manifold-level anchor (foreclosed); the K-branch fires on a different structural claim (the V-Lorentzian sub-bundle has a *cleaner* manifold-level structure than any peer-reviewed cosmological minisuperspace with non-trivial volume-conformal factor). **Halliwell manifold-level extension is foreclosed**; alternative-anchor survey is opened as **audit π′′′** ([Paper 46 §8.8](46_hartle_hawking_signature.md): free-field theory, de Sitter limit, topos-theoretic flat-Lorentzian, causal set theory continuum limits). Cosmological correspondence stays at [P] tangent-quadratic-form isometry; the [A]-partial-mathematical-identification at the manifold level is *not* licensed on the Halliwell anchor. Audit π′ is the **seventh named joint-on-disjoint outcome** of the program. Cosmological *claim itself* unchanged at [C, reduced]; §11.2 firewall not lifted.

**Audit π′′′ (alternative-anchor candidate-survey, settled 2026-05-21)** ([`empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md`](empirical/reports/audit_pi_triple_prime_alternative_anchor_survey_settlement.md)) closed the alternative-anchor candidate-survey at **joint-on-disjoint at the framework-substantivity tier**. **L-branch on every peer-reviewed mathematical-physics candidate's substantive identification**: free scalar field on Minkowski (wrong signature), de Sitter-limit Bianchi I (conformal factor doesn't become constant), topos-theoretic QG (not literally a Lorentzian manifold), causal set continuum limits (configuration space ≠ target spacetime), linearized GR phase space (infinite-dim native, no spectral-positivity boundary), single-particle relativistic dynamics (K-trivial only), AQFT causal diamonds (light-cone vs spectral-positivity boundary), AdS-related flat regions (AdS curvature). **K-trivial only on Minkowski-as-uniqueness-determined-ambient** (every 4-dim flat Lorentzian manifold IS Minkowski by isometry-uniqueness; non-substantive). **The Tier-1.75 mathematical-identification path is FORECLOSED.** The cosmological correspondence cannot promote beyond [P]-tangent-isometry at the peer-reviewed-framework-identification question; the V-affine V-sub-manifold $\Sigma_V^{\mathrm{aff}}$ is identified positively as a **4-dim bounded-convex Minkowski region with Hilbert-space-spectral-positivity boundary** — a *novel* structural object internal to the categorical-simplex program. Audit π′′′ is the **eighth named joint-on-disjoint outcome**. A *characterization* audit candidate (audit π′′′′, Tomita–Takesaki modular flow of the V-supported observable algebra) opens as the next substantive structural-internal investigation, *not* as a Tier-promotion candidate. Cosmological *claim itself* unchanged at [C, reduced]; §11.2 firewall not lifted; Tier 2 / Tier 3 / Tier 4 unchanged. The cosmology-arc lift envelope is now *sharply bounded* — four consecutive joint-on-disjoint outcomes (β, π, π′, π′′′) have collectively narrowed the manifold-level structural identification to "internal to the program."

<!--
NOTE TO SELF: §4.1 currently asserts "the V-Lorentzian sub-bundle is the local observer frame" without re-deriving it from Paper 32 §13.2B. v0.1 should add a one-paragraph summary of the audit-triad outcome: §13.2 returned what looked like L; §13.2A reformulated to the Hessian of a quadratic Casimir; §13.2B confirmed the V-Lorentzian + M-Euclidean joint realization on orthogonal sub-bundles. This is the §13.2B-as-positive-finding framing that v2insert-01 §1 closes on, and it deserves a few sentences here.

OPEN: should "gravity" appear in §4.1 prose at all, or only in the closing correspondence reading? Currently it appears once in the correspondence reading. Decision: keep it where it is (one mention, in correspondence-reading context, explicitly correspondence language). Don't promote it elsewhere.
-->

### 4.2 Deep learning: the conductor blind spot and the M-overflow signature in trained networks

Anchor: Paper 34 (The Conductor Blind Spot), Paper 36 (Layerwise Packet Spectroscopy), Paper 37 (Label Smoothing in the Conductor Blind Spot), v2insert-05 (audit κ, inference-side), v2insert-06 (audit λ, training-side), v2insert-07 (audit λ settlement: K-branch realized on widths 16/32/64 with signal-to-noise > 47; audit κ partial settlement, layerwise sweep deferred).

The conductor blind spot of Paper 34 is the structural statement that any second-order preconditioner — natural gradient, K-FAC, Gauss-Newton, Adam's diagonal empirical Fisher, the NTK Gram — sees only the quadratic Fisher metric on a categorical belief space and therefore *cannot represent* the cubic Amari–Chentsov content. In particular, the cross-packet content forced by the closing-triple selection rule of Paper 32 Lemma 6.1 (the cubic-vacuity overflow of §2.4 above) is invisible to a second-order optimizer. Yet that content is not vanishing in the network's effective dynamics — by Pontryagin character orthogonality, it is carried by the M-sector tangent directions, which the optimizer cannot see but which the network's representation still encodes.

**Attention-scoring scoping ([Paper 34](34_the_conductor_blind_spot.md) Remark 3.6).** The conductor blind spot's content reaches the *attention-scoring layer* via a structural identity: spread-based attention scoring `s(q, k) = 1 − (q · k)² / (Q(q) Q(k))` (Thomson 2026 §4.1, ARTexplorer) discards `sgn(q · k)` by squaring, and the sign-pair structure of real-valued `ℤ/n` characters `(χ_k, χ_{−k})` makes the *unsigned* cubic mass `|T_{p_*}(χ_k, χ_ℓ, χ_m)|²` invariant under simultaneous character inversion while the *signed* cross-packet orientation is precisely what squaring destroys. The sign information lost by spread scoring is therefore the cross-packet cubic orientation that Theorem 3.4 already identifies as missing from any quadratic preconditioner — same content, different layer. A `ℤ₂` polarity bit (Thomson §6.5 *Janus*) restores this orientation as a typed Cartan-slot channel in the sense of [Paper 30](30.constrained_overflow_incompatibility_budgets.md)'s typed residual tuple. Paper 34 Remark 3.6's pre-registered correlation conjecture — `gain_{ℤ₂}(R) ~ ρ_x(R)` across rings — is the per-task settlement test for whether spread-attention's blind-spot is the same M-channel overflow the conductor blind spot identifies at the curvature tier.

Paper 37's label-smoothing substitution proposition says: the empirically successful technique of label smoothing (`α`) in classification training and the Pareto-rule conductor-aware update projection (`α'`) of Paper 12 are *partially substitutable* mechanisms with overlapping effect on the iso-loss ridge. v2insert-06 §1 sharpens this: *Paper 37's α-mechanism is, in v2insert-02 vocabulary, the direct M-injection lever*. At `α = 1`, the applied update is entirely in M-supported directions; at `α = 0`, the unprojected Adam direction is used. The conductor-aware support `S ∈ {{12}, {6, 12}}` of Paper 37's training scheme is *exactly* the M-projection (or a sub-projection of M) on `ℤ/12`.

Audit λ of v2insert-06 then asks: along Paper 37's pre-committed iso-loss ridge in `(α, ε)` space, does the V/M packet ratio `ρ_VM(α, ε, W)` of the trained network's output logits vary monotonically with `α`, or is it iso-loss-invariant (mechanisms A and B are fully substitutable)? The audit was settled in v2insert-07 §2.4: **K-branch realized on all three widths (16, 32, 64) with signal-to-noise ratios 48 to 119**. At every fixed `ε ∈ {0, 0.03, 0.06, 0.10, 0.15, 0.20}` and every width, `ρ_VM(α = 0, ε)` ranges from 0.65 to 0.87 and falls strictly monotonically to `ρ_VM(α = 1, ε) = 0.00` — the latter forced to zero by the structural identity `S = {12} ⊆ M`, which makes the `α = 1` boundary the V/M = 0 boundary. The seed-noise scale is ~0.01 against a signal of ~0.7; the V/M decoupling of Paper 47 *correctly predicts* a measurable, monotone, large-signal dependence of the trained MLP's output-logit packet ratio on the conductor-aware training parameter.

**Correspondence reading.** In Paper 31's vocabulary, the deep-learning manifestation is the projection `Π: W → V_logit` from the network's full representational space to the readout-projected logit space, with `K = 2` (the cutoff at second order, the order the optimizer sees). The residuals — the cubic content the optimizer cannot represent — are typed by the M-conductor packet, bounded by `Capacity_V(ℤ/12)`, and stable under the Pareto-rule's `S`-support choice. *In this correspondence, hallucinations and training-time mode collapse are the visible behavioral signatures of M-channel overflow propagated through training to the readout*. Label smoothing is the practitioner's empirical defense against this overflow — by adding a small additive `ε` to all logits, it shrinks the off-centroid contribution of every conductor packet, including M, thereby reducing the M-channel's effective amplitude at the readout. The conductor-aware Pareto projection of Paper 12 is the structurally cleaner defense: it directly injects M-supported content into the update, allowing the optimizer to see (and therefore train against) what the conductor blind spot would otherwise hide.

The inference-side audit κ on Llama-3.1-8B / Mistral-7B-v0.3 (v2insert-05, layerwise sweep) tests whether the same V/M propagation signature is present in residual streams of large pretrained transformers. v2insert-07 §3 records the partial settlement: the final-layer anchor of Paper 26 / Paper 36 P2 is reproduced exactly (`f_{12, final} = 0.657415` to six digits, matching the band `[0.62, 0.69]` of Paper 36 P2); the per-layer residual-stream capture is deferred for absence of HuggingFace credentials and GPU access in the present environment. The audit kappa deferred state is a first-class outcome per Paper 35 §3.6; the final-layer anchor confirms the lens-arm implementation matches the published Paper 26 baseline.

**External anchor for the AI-side V⊥M signature: smooth Jaccard ridge across mixed-task circuit discovery.** Rai, Geva & Yao 2026, "Data-driven Circuit Discovery for Interpretability of Language Models" ([arXiv:2605.09129](https://arxiv.org/abs/2605.09129)), report on GPT-2 / Qwen2.5-7B-Instruct / Llama-3.1-8B-Instruct that hypothesis-driven circuit discovery (EAP, EAP-IG, ACDC, E-ACT) on a mixed dataset returns a single circuit reaching $87\%$ faithfulness on two structurally distinct mechanisms at $10\%$ mixture injection (an $81.3$-point jump). Across mixture ratios $\alpha_{\text{mix}} \in \{0.0, 0.1, …, 1.0\}$, the pairwise Jaccard similarity of the discovered top-5% edge sets at adjacent ratios is $0.79$–$0.89$ and falls smoothly to $0.26$ at the extreme endpoints (their Fig 3c). Read in the present manuscript's vocabulary: the stable $0.79$–$0.89$ overlap across adjacent mixture ratios is the *V-sector* survival — the single-prime-packet content of the attribution vector that is invariant under the mixture-ratio displacement of the centered logit; the smooth $0.79 \to 0.26$ falloff across the full mixture range is the *M-sector* activation — the cross-prime cubic content that the second-order EAP-IG attribution cannot couple at $p_*$ ([Paper 34](34_the_conductor_blind_spot.md) Corollary 3.11), so the apparent mechanism mixing is M-channel overflow propagated to the attribution layer. This is the production-LLM, peer-reviewable inference-side measurement of the V⊥M decoupling theorem of Paper 47 applied to the AI substrate, at frontier-model scale (Llama-3.1-8B), with the same structural shape as the audit-λ trained-MLP measurement reported above. It is also the most direct external corroboration available of the "hallucinations and mode collapse as M-channel overflow" claim of this subsection's *Correspondence reading*: the $87\%$ mixed-faithfulness number is not a coherent mechanism, it is the second-order attribution's aggregate of multiple packet-distinct mechanisms, and the smooth Jaccard ridge across mixture ratios is the off-centroid Fourier activation rule of Paper 34 Theorem 5.2 measured at the attribution layer of a frontier checkpoint.

<!--
NOTE TO SELF: §4.2 is the strongest-anchored manifestation right now, because audit λ has K-confirmed at v2insert-07 with signal/noise > 47. Let it do the heaviest narrative lifting in the three-manifestation structure. The numbers in §4.2 (0.65–0.87, S/N 48–119) are load-bearing for the deep-learning correspondence's plausibility; cite v2insert-07 §2.4 verbatim if any tightening is needed.

OPEN: should §4.2 spell out the connection between Paper 47's V/M decoupling theorem (a lift-tangent structural claim, internal to the program's arithmetic) and the empirical V/M packet signature of audit λ (a measurement on trained MLP output logits)? v2insert-06 §7(a) calls this "correspondence-language, not derivation" — the audit shows that the V/M arithmetic correctly predicts the *direction* of a measurable training-mechanism signal, not that the MLP is doing the program's arithmetic decoupling. v0.1 should make this distinction visible in §4.2's correspondence-reading paragraph.

OPEN: the "hallucinations are M-channel overflow" claim is the most popularly relevant in the paper. It is also the loosest at the v0.0 tier — audit λ tested a small MLP on the months task, not a frontier model on free-form generation. The correspondence is structural; the literal claim about LLM hallucinations is the v2insert-07 §3 deferred kappa territory. v0.1 should explicitly flag this gap, OR delete the hallucination framing and leave only the audit-λ-anchored claim. Decision: KEEP the framing but tier-tag it explicitly as [C, reduced] correspondence-language; the v2insert-07 partial-deferred kappa is what the reader is owed.

OPEN: §4.2 currently doesn't cite Paper 38 (multi-head attention as frame-cost minimization), Paper 41 (cubic-Noether-budgeted decoding), or Paper 45 (conductor-certified sparse autoencoders). v0.1 should weave these in as additional cubic-aware practitioner-side defenses that the conductor framework predicts, to round out the deep-learning manifestation's spine.
-->

### 4.3 Active inference: the FEP-3 sector resolution and the arrow of time

Anchor: Paper 32 §6.2A Corollary 6.3 thread T3 (FEP-3 sector resolution); INSERT 15 (FEP-3 gradient-vs-least-action audit, present in the empirical/ directory as `insert15_fep3_audit_run_output.txt`).

The free-energy principle (Friston 2010 and successors) decomposes a self-maintaining biological system's effective dynamics as the gradient descent of a *variational free energy* `F = energy − complexity + entropy`. The three additive terms admit, at the projection-closure tier, a partition by conductor-lattice content: the *least-action* term (the dissipationless V-internal dynamics that a perfect kinematic agent would follow) lives in the V sector; the *complexity* term (the cubic environmental coupling that arises when the agent's internal model must close on its environmental observations) is forced to route through M by the closing-triple selection rule; the *entropy* term (the thermodynamic cost of processing environmental data) is the asymptotic accumulation of M-channel content over the agent's lifetime.

Paper 32 §6.2A Corollary 6.3 records this as the third thread of the four-thread arithmetic root (T3, the FEP-3 sector resolution). The structural reading: an active-inference agent that maintains its V-internal structure under environmental coupling exhibits a *one-way information leakage* from V into M, because the M-channel content (the cubic environmental cross-talk) is structurally inaccessible to the agent's V-internal dynamics — the agent's gauge / projection / least-action machinery is V-supported by construction, and M is HS-orthogonal to V. The macroscopic signature of this one-way leakage is *the arrow of time*: V's dissipationless dynamics admit time-reversal symmetry; M's environmental-coupling residual does not, because the M-channel accumulates content the V-channel cannot retrieve.

**Correspondence reading.** In Paper 31's vocabulary, the active-inference manifestation is the projection `Π: W → V_agent` from the full environment-coupled belief space to the agent's V-internal sector. The residuals are M-mediated and irreversible (cannot be undone by V-internal dynamics). The horizon `H` is the agent's predictive timescale; the cutoff `K` is the order at which the agent's variational free energy is truncated. *In this correspondence, the arrow of time and the thermodynamic entropy production of a biological system are the macroscopic projection-closure signatures of the V → M one-way information leakage on the categorical simplex's Bures lift*. Physical thermodynamics, statistical-mechanical microstate counting, metabolism, and the second law as a physical principle are not derived; only the structural form of how a finite-arithmetic substrate accommodates the one-way V → M leakage under projection-closure validity.

**Settled by audit FEP-3 (2026-05-20)** ([`empirical/reports/audit_fep3_settlement.md`](empirical/reports/audit_fep3_settlement.md)). The variational free-energy on `D(ℂ⁶)` decomposes additively as `F = F_V + F_M`:

- **F_V = I_real** (V-supported Lorentzian Casimir): Hamiltonian invariant; reversible / kinematic / least-action.
- **F_M = α² · (m²_simplex)²** (M-supported quartic): entropy functional; monotone-increasing under M-component flow; irreversible / dissipative.

Four predicates verified at machine precision: (A) V-rays preserve `F_V` and vanish m²_simplex (Hamiltonian); (B) M-rays accumulate m²_simplex monotonically and vanish `F_V` (gradient-of-entropy); (C) V ⊥ M cross-coupling zero at every order (audit δ specialized); (D) `F = F_V + F_M` additive, no interaction term.

This is the **metriplectic split** of Morrison 1986 / Grmela–Oettinger 1997 GENERIC, structurally realized on the categorical simplex's conductor lattice. The **arrow of time** is the direction of `∇F_M`: V-flow admits time-reversal symmetry; M-gradient-flow does not (M is fundamentally one-way).

Friston 2010 free-energy decomposition `F = E − C + S` maps to the V/M sector resolution at the Lie-algebra-of-decoupling level: E ↔ V-sector (kinematic / least-action); C ↔ V/M decoupling (Pontryagin orthogonality forces zero complexity cost); S ↔ M-sector (entropy / dissipation).

**Tier promotion (audit FEP-3 settled).** Paper 32 §6.2A Corollary 6.3 T3 settles at K-branch **[P]** for the structural FEP-3 sector resolution. §4.3 biology manifestation settles at:
- **[P] for the structural substrate** (V/M metriplectic split on the conductor lattice).
- **[C, reduced] for the empirical biological-system applicability** (no ground-truth active-inference data audited; remains deferred).

<!--
NOTE TO SELF: §4.3 is the weakest-anchored of the three manifestations at v0.0. The FEP-3 thread (T3 of Corollary 6.3) is the only direct anchor visible to me. The "least-action V dynamics" + "M-mediated complexity" + "one-way leakage = arrow of time" reading is the v2insert-04 §3.1 three-outcome pre-claim I'm staging here.

If we are to lift §4.3 to [A] or [P] in a later draft, the cleanest path is:

(i) Run an empirical audit of FEP-3 on a toy active-inference agent (a Karl-Friston-style discrete generative model on a small `ℤ/n` index), measuring whether the variational free-energy gradient decomposes into V-internal + M-environmental components in the predicted way.

(ii) Anchor the "arrow of time" framing against INSERT 06 (causal_structure_arrow_of_time.md, present in the repo at C:\Projects\simplicial\). I have not read INSERT 06 yet at v0.0 drafting — v0.1 should incorporate its structural content if it aligns. If it conflicts, §4.3 must be revised before promotion.

(iii) Cite Rosas 2025 / Rosas_2025_conductor_lattice_bridge.md, which appears in the repo. I haven't read it at v0.0 either — v0.1 should incorporate.

OPEN: Should §4.3 be removed at v0.0 and reinstated at v0.1 after the FEP-3 audit firms up? Decision at v0.0: KEEP, but flag prominently as [C, reduced] and as the manifestation most exposed to refutation. The paper's epic scope depends on the three-manifestation framing; removing §4.3 would collapse it to "cosmology + AI", which is already what Papers 46/47/48 cover. The universal-overflow law's value-add over v2insert-01/02/03 is the *third* manifestation.

OPEN: §4.3 mentions "Friston 2010 and successors" without a specific citation. v0.1 must anchor against the Friston canonical FEP paper. The carried-label discipline (§11.4) applies: "free-energy principle", "active inference", "Markov blanket" are all carried labels that must be anchor-checked before manuscript use. v0.0 has flagged the discipline; v0.1 must execute it.

OPEN: the "arrow of time" framing is the second-heaviest external-correspondence claim in this paper (after the cosmology / Hartle–Hawking / Bekenstein–Hawking triad of §4.1). The §11.1 emergent-anything positioning is binding: do NOT claim to derive the physical arrow of time, statistical-mechanical entropy, or the second law. Only the structural form of the V → M one-way leakage.
-->

### 4.4 What the three manifestations share, what they don't

The three manifestations share the *structural form* of the closure-certificate `𝒞_W(Π; T, H, K)`:

| Manifestation | W (whole) | Π (projection) | T (task) | V (clean channel) | M (overflow channel) | Audit |
|---|---|---|---|---|---|---|
| Cosmology | Bures manifold `D(ℂ⁶)` | V-observer projection | local Lorentzian dynamics | V-`H + P_a` 4-dim sub-bundle | M-diagonal 2-dim Euclidean correction | α, η, θ, ι |
| Deep learning | network's representational space | readout (unembedding) | next-token prediction | V_logit packets | M_logit packets | κ, λ |
| Active inference | environment-coupled belief space | V-internal agent projection | self-maintenance / homeostasis (variational free-energy minimization) | V-Hamiltonian (F_V = I_real, reversible) | M-gradient-of-entropy (F_M = α²·(m²_simplex)², irreversible, arrow of time) | T3 thread + FEP-3 (settled K-branch, 2026-05-20) |

What the three manifestations do *not* share — and what the universal framing of §3 deliberately does *not* assert — is a *common physical mechanism*. The cosmology manifestation operates on the Bures-manifold tangent geometry at machine precision in HS-norm; the deep-learning manifestation operates on trained-network output logits with empirical seed-noise scales; the biology manifestation operates on macroscopic biological timescales and degrees of freedom. There is no claim that gravity, hallucinations, and the arrow of time *are the same physical thing*. The claim is structural: each of the three takes the *closure-certificate shape* of the overflow law on the categorical simplex's conductor lattice.

**Audit ν (settled 2026-05-20, joint-on-disjoint)** ([`empirical/reports/audit_nu_cross_manifestation_settlement.md`](empirical/reports/audit_nu_cross_manifestation_settlement.md)) sharpens this distinction to the natural-transformation level: at the **abstract closure-certificate level**, the identity-on-certificate-ingredients is a natural transformation between any two of the manifestations' closure-certificate functors in `CertificateCategory` (the universal-overflow framing has functorial content at this level). At the **literal-domain level**, no natural transformation exists — `D(ℂ⁶)`, transformer residual streams, and active-inference belief manifolds are different categories with no faithful inter-substrate maps. The structural shape is shared functorially; the substrate is not.

<!--
NOTE TO SELF: §4.4 is the crucial discipline anchor for the universal framing. The paper's epic scope is real if §4.4 is honest about what's shared and what's not. The temptation is to wave hands at "one law, three appearances" and let the audience infer mechanism unification. Resist that temptation explicitly: §4.4 is where the discipline rails of §7 are pre-staged.

OPEN: should §4.4 add a fourth row to the table for the row-generalization audit α/η on ℤ/30 (which is technically not a "manifestation" but a structural extension of the framework)? Decision: NO; α/η is the row-stability audit, addressed in §5, not a manifestation.
-->

---

## 5. The audit α/η + θ + ι settlement: row-generalization across five primorial rows

### 5.1 The settlement, at a glance

Three audits have settled, in a single deterministic compute pass each, the row-generalization of the universal-overflow framing:

| Audit | Scope | Settlement |
|---|---|---|
| **α/η on `ℤ/30`** (v2insert-08) | Triple-test of Papers 46 C5 / 47 C3 / 48 C2 on the next primorial row | **Triple-K-branch realized.** `Capacity_V(ℤ/30) = 6/150 = 1/25` (8.3× decrease from `ℤ/6`'s 1/3); `‖V_proj · M_proj‖_F = 1.22e-14` at machine floor on the 30 × 30 projectors; the Hartle–Hawking V/M decomposition with the predicted character exists on `ℤ/30`. |
| **θ on the primorial ladder** (v2insert-09) | Five-row scaling of `Capacity_V` on `ℤ/{6, 30, 210, 2310, 30030}` | **K-direction + joint-on-disjoint at exponent.** Monotone decay confirmed at all four pairwise inequalities; `Capacity_V(ℤ/30030) = 62/150300150 = 4.13 × 10⁻⁷` (six orders of magnitude below `ℤ/6`); per-step decay accelerating (`8.3× → 21× → 50× → 93×`), inconsistent with clean log-linear and consistent with super-exponential decay in `n` (the joint-on-disjoint sub-finding). |
| **ι on Bousso-bound shape** (v2insert-10) | Five-row decay-shape comparison against canonical holographic shapes | **K-leading + joint-on-disjoint at corrections.** PNT-heuristic shape `K · n² · ln(n) / N²` matches at spread 1.584× across all five rows; asymptotic power-law slope `→ −2` matching 't Hooft–Susskind / Bousso; Bekenstein `1/N` refuted at spread 161×; the program's decay has the *shape* of holographic saturation at asymptotic order but carries finite-arithmetic-specific corrections (polynomial-log-`n` prefactor) absent from continuous-spacetime bounds. |

The three audits jointly settle:

| Paper | Claim audited | Realized branch |
|---|---|---|
| Paper 46 (v2insert-01) C5 | Hartle–Hawking signature extends to `ℤ/30` and beyond | **K (arithmetic substrate)** at five primorial rows; geometric realization on `D(ℂ^N)` for `N > 6` remains queued (Bures-Hessian sub-bundle audit) |
| Paper 47 (v2insert-02) C3 | Arithmetic Decoupling Theorem extends to `ℤ/30` and beyond | **K** at five primorial rows; numerical at machine floor on `N ≤ 210`, algebraic by Pontryagin character orthogonality on disjoint index sets for `N > 210` |
| Paper 48 (v2insert-03) C2/C3/C4 | Conductor Capacity Bound monotonically decreases; structural shape matches a peer-reviewed holographic bound | **K-direction + joint-on-disjoint** — monotone decay confirmed (C2 + C3); PNT-heuristic shape matches at spread 1.584× with asymptotic slope `→ −2` matching 't Hooft–Susskind / Bousso (C4 K-leading); polynomial-log correction is program-specific (C4 joint-on-disjoint at corrections) |

### 5.2 Headline numerical anchors

The five-row capacity table (v2insert-09 §1):

| Row | `n` | `dim V` | `dim M` | `T_total` | `pure_V` | `Capacity_V` | `log₁₀` | Per-step decay |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `ℤ/6` | 2 | 3 | 2 | 6 | 2 | **1/3 = 0.3333** | −0.48 | — |
| `ℤ/30` | 3 | 7 | 22 | 150 | 6 | **1/25 = 0.0400** | −1.40 | **8.33×** |
| `ℤ/210` | 4 | 13 | 196 | 7 350 | 14 | **1/525 = 0.001905** | −2.72 | **21.0×** |
| `ℤ/2310` | 5 | 23 | 2 286 | 889 350 | 34 | **3.82e-5** | −4.42 | **49.8×** |
| `ℤ/30030` | 6 | 35 | 29 994 | 150 300 150 | 62 | **4.13e-7** | −6.38 | **92.7×** |

The five `Capacity_V` values are exact rationals at [P] (integer arithmetic in every membership and closing decision; closed-form orbit-counting verified against full O(N²) enumeration for `N ≤ 210`).

### 5.3 The structural-shape settlement

Audit ι (v2insert-10) compared the five-row decay against five candidate shapes:

| Candidate shape | Predictor | Spread | Verdict |
|---|---|---:|---|
| Bekenstein-like | `K / N` | 161.45× | NO MATCH |
| 't Hooft–Susskind / Bousso literal | `K / N²` | 31.00× | POOR (alone) |
| Random-uniform pair baseline | `K · (\|V\|/N)²` | 4.39× | PARTIAL |
| Random-uniform triple baseline | `K · (\|V\|/N)³` | 97.71× | POOR |
| **PNT heuristic** | **`K · n² · ln(n) / N²`** | **1.584×** | **BEST** |

The PNT-heuristic shape captures both pieces in one quantity:
- *Leading order `1/N²`* — matches 't Hooft–Susskind / Bousso asymptotic shape (`α → −2` confirmed by local-slope analysis: `−1.32, −1.56, −1.63, −1.77` across the four primorial transitions).
- *Polynomial-log prefactor `n² · ln(n)`* — program-specific finite-arithmetic feature, absent from continuous-spacetime holographic bounds; matches the Prime-Number-Theorem heuristic derivation `|V| ~ Σ p_i ~ n²·ln(n)/2`.

The structural shape matches a peer-reviewed holographic bound at the **asymptotic-exponent level**; the literal formula does not match because the program's finite-arithmetic substrate carries the polynomial-log correction that continuous-spacetime invariance forbids.

### 5.4 Reproducibility

All three audits are deterministic, reproducible, and CPU-only. Total wall time:

- Audit α/η on `ℤ/30`: **0.06 seconds** (v2insert-08).
- Audit θ on the full primorial ladder: **0.26 seconds** (v2insert-09).
- Audit ι on shape comparison: **< 1 second** (v2insert-10).

Reproducibility artifacts:
- [`empirical/audits_alpha_eta_z30_primorial_generalization.py`](empirical/audits_alpha_eta_z30_primorial_generalization.py) + transcript + [`empirical/reports/audits_alpha_eta_z30_settlement.md`](empirical/reports/audits_alpha_eta_z30_settlement.md).
- [`empirical/audit_theta_capacity_scaling_primorial_ladder.py`](empirical/audit_theta_capacity_scaling_primorial_ladder.py) + transcript + [`empirical/reports/audit_theta_settlement.md`](empirical/reports/audit_theta_settlement.md).
- [`empirical/audit_iota_bousso_bound_shape_comparison.py`](empirical/audit_iota_bousso_bound_shape_comparison.py) + transcript + [`empirical/reports/audit_iota_settlement.md`](empirical/reports/audit_iota_settlement.md).

The settlement record convention follows Paper 35 §3.4 (deterministic exact reproducible) and v2insert-07 §1 (single-driver, single-script-version, audit-specific report path).

---

## 6. Falsifiers

The matched-pair-extended-to-three-outcome falsifier discipline (v2insert-04 §3.1) is binding for every claim in the paper. The named falsifiers below are the load-bearing ones; the more granular per-section falsifiers are inherited from the anchor papers and v2inserts.

### 6.1 F1 — audit α/η + θ + ι row-generalization falsifier (did not fire)

The original F1 falsifier (v0.0): if `Capacity_V(ℤ/30) ≥ 1/3`, the Conductor Capacity Bound monotonicity hypothesis is refuted, and the universal-overflow framing of §3 is bounded to `ℤ/6`. **F1 did not fire**: `Capacity_V(ℤ/30) = 1/25 = 0.04 < 1/3 = 0.333` (v2insert-08); the monotonic-decrease holds at all four pairwise inequalities across the primorial ladder (v2insert-09); the structural shape matches a peer-reviewed holographic-bound shape at leading order (v2insert-10). The K-branch is realized across all five primorial rows; the universal-overflow framing's row-generalization remains at [C, reduced] (no demotion).

The strengthened F1 (v0.1): the universal-overflow framing now carries a quantitative prediction for the next primorial row. From audit ι's PNT-heuristic shape `Capacity_V(P_n) ≈ 4.5 · n² · ln(n) / N²`:

```
Capacity_V(ℤ/510510) ≈ 4.5 · 7² · ln(7) / 510510² ≈ 1.7 × 10⁻⁹
```

The strengthened falsifier: if extension of audit θ to `ℤ/510510 = 2·3·5·7·11·13·17` returns `Capacity_V(ℤ/510510)` that fails the PNT-heuristic shape by more than a factor of 2, the joint-on-disjoint settlement of v2insert-10 is row-specific to `ℤ/{6, 30, 210, 2310, 30030}` and the asymptotic-shape claim weakens. Audit θ extension is trivial (~0.05 s additional compute) and is named as the next concrete carry-forward item (§9.2).

### 6.2 F2 — cross-manifestation coherence audit (audit ν, opened)

**Audit ν — settled 2026-05-20 at joint-on-disjoint** ([`empirical/reports/audit_nu_cross_manifestation_settlement.md`](empirical/reports/audit_nu_cross_manifestation_settlement.md)).

For each pair of manifestations (cosmology / AI; cosmology / biology; AI / biology), audit ν specified the closure-certificate ingredients `(W, Π, T, H, K, V, M, 𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` at the [P]-spirit tier and analyzed the natural-transformation status at two abstraction levels:

- **At the abstract closure-certificate level (K-branch realized).** All three manifestations are objects in `CertificateCategory` (the category whose objects are tuples `(V finite-capacity, M designated-overflow, V ⊥ M, no-crash, certificate-ingredients inhabited)`). The **identity on certificate ingredients** is a trivial natural transformation between any pair of manifestation-functors. The universal-overflow framing has *functorial content* at the closure-certificate-shape level.
- **At the literal-domain level (L-branch realized).** No literal natural transformation exists between the substrates: `D(ℂ⁶)` (cosmology, 35-dim Bures lift), transformer residual streams (AI, model-dependent dimension), and active-inference belief manifolds (biology, `(R-1)`-dim simplex) are different categories with no faithful inter-substrate maps.

**Joint-on-disjoint realized:** the *structural shape* of the closure certificate is functorially shared across manifestations; the *substrate* is not. This is the universal-overflow framing's *correspondence-language content* (Paper 32 §11.1) sharpened to the natural-transformation level: structural-shape sharing at [P]-abstract; no literal-mechanism sharing at [L-branch].

This makes audit ν **the fifth named joint-on-disjoint outcome** of the 2026-05-20 session under v2insert-04 §3.1 three-outcome rule (joining audits θ, ι, β-row-3, χ-trichotomy).

### 6.3 F3 — audit ζ surfaces V/M mixing at higher orders

**Audit ζ is subsumed by audit δ (settled 2026-05-20).** The all-orders V/M decoupling extension is at [P] by the finite combinatorial proof on the dual group `(ℤ/N)^∧`: any V-supported observable acts on a subspace V^⊗m of `(ℂ^N)^⊗m` that is HS-orthogonal to the M-involving complement, at every order m ≥ 2. No higher-order observable on `D(ℂ⁶)` built from V-supported operators can have non-trivial action on the M-Euclidean sub-bundle; audit ζ's counter-example search is structurally foreclosed.

### 6.4 F4 — audit κ inference-side refutation

The currently-deferred audit κ on Llama-3.1-8B / Mistral-7B-v0.3 (v2insert-05) tests whether the V/M arithmetic propagates through transformer pretraining to leave a measurable signal in the residual stream. If, when audit κ is finally run with HuggingFace + GPU access, the depth-normalized saturation indices `σ_V` and `σ_M` are statistically indistinguishable on both digits (`ℤ/10`) and months (`ℤ/12`) across both models, the AI manifestation's *inference-side* propagation claim is refuted (the L-branch of v2insert-05 P8 / P9). The training-side audit λ's K-branch outcome (v2insert-07 §2.4) is unaffected; the AI manifestation retains training-mechanism sensitivity but loses inference-side propagation.

### 6.5 F5 — FEP-3 audit, settled at structural tier 2026-05-20

**Audit FEP-3 (structural) settled at K-branch** ([`empirical/reports/audit_fep3_settlement.md`](empirical/reports/audit_fep3_settlement.md), 2026-05-20).

On `D(ℂ⁶)` at the centroid `ρ_*`, the variational free-energy decomposes additively as `F(ρ) = F_V(ρ) + F_M(ρ)` with:
- `F_V = I_real`: V-supported Lorentzian Casimir, **Hamiltonian** (reversible, conserved by V-flow).
- `F_M = α² · (m²_simplex)²`: M-supported quartic, **gradient-of-entropy** (monotone-increasing under M-component flow, irreversible).

Four predicates verified at machine precision:
- **(A)** V-rays preserve `I_real` and vanish `m²_simplex` (V-Hamiltonian).
- **(B)** M-rays accumulate `m²_simplex` monotonically and vanish `I_real` (M-gradient-of-entropy).
- **(C)** V ⊥ M cross-coupling is zero at machine precision (audit δ all-orders specialized).
- **(D)** `F(ρ) = F_V(ρ) + F_M(ρ)` exactly, no interaction term.

**Arrow of time** = direction of `∇F_M`. Time-reversal of V-flow preserves `F_V` (no time-asymmetry from V); time-reversal of M-gradient-flow flips the sign of `∇F_M`. The arrow of time on the categorical simplex's conductor lattice = the M-sector gradient flow direction.

Friston 2010 free-energy `F = E − C + S` maps to the V/M sector resolution at the Lie-algebra-of-decoupling level: E ↔ V-sector (kinematic / least-action); C ↔ V/M decoupling (Pontryagin orthogonality forces zero complexity cost); S ↔ M-sector (entropy / dissipation). The metriplectic structure of Morrison 1986 / Grmela–Oettinger 1997 GENERIC is structurally realized on the categorical simplex.

**Settlement tiers:** Paper 32 §6.2A Corollary 6.3 T3 settles at K-branch [P] for the structural FEP-3 sector resolution. Paper 49 §4.3 biology manifestation settles at:
- **[P] for the structural substrate** (V/M sector resolution of variational free-energy on the conductor lattice).
- **[C, reduced] for the empirical biological-system applicability** (no real active-inference data audited; remains deferred for ground-truth predictive-coding / active-inference datasets).

F5 is therefore **partially settled**: the analytical-substrate half is K-branch [P]; the empirical-biology half remains an open falsifier for future audits with ground-truth biological data.

---

## 7. Discipline rails

### 7.1 §11.1 emergent-anything positioning (Paper 32, binding)

This paper opens the program's *fourth* external-correspondence claim, after §11.1 emergent-gravity (Paper 32), v2insert-01 Hartle–Hawking (Paper 46), v2insert-02 QG-mixing-bypass (Paper 47), and v2insert-03 Bekenstein–Hawking holographic bound (Paper 48). The four-correspondence stack adds active-inference / arrow-of-time as the fourth.

Discipline binding throughout: *external anchor, not adopted ontology*. The program does not derive physical gravity, hallucinations, biological metabolism, or the second law. Only the closure-certificate shape of the overflow law on the categorical simplex's conductor lattice. Each manifestation in §4 makes this explicit in its closing correspondence-reading paragraph; the §1.2 "what is not claimed" subsection records it at the paper level.

### 7.2 §11.2 dimensional firewall (Paper 32, binding)

No physical quantity is named with physical units. No Planck scale, no Newton's constant `G`, no speed of light `c`, no Hubble constant, no Boltzmann constant `k_B`, no fundamental charge `e`, no Compton wavelength, no Bekenstein–Hawking temperature, no horizon area in physical units. All quantities reported are dimensionless structural ratios: capacity ratios `Capacity_V(R)`, packet fractions `f_d`, V/M ratios `ρ_VM`, depth-normalized saturation indices `σ_d`, test cross-entropy `G_IID`, ECE, leakage, gen-gap.

### 7.3 §11.4 carried-label discipline (Paper 32, binding)

Every external-correspondence label used in the paper must be anchor-checked against its peer-reviewed source before manuscript use:

- "Hartle–Hawking no-boundary proposal", "Wick rotation", "imaginary time": Hartle & Hawking, *Wave function of the universe* (Phys. Rev. D 28, 1983).
- "Bekenstein bound": Bekenstein, *Black holes and entropy* (Phys. Rev. D 7, 1973).
- "Holographic principle": 't Hooft, *Dimensional reduction in quantum gravity* (1993); Susskind, *The world as a hologram* (J. Math. Phys. 36, 1995).
- "Bousso bound": Bousso, *A covariant entropy conjecture* (JHEP 7, 1999).
- "AdS/CFT": Maldacena, *The Large N limit of superconformal field theories and supergravity* (1997).
- "Conductor blind spot", "label smoothing in the conductor blind spot": Paper 34 (anchored, internal); Paper 37 (anchored, internal).
- "Free-energy principle", "active inference", "Markov blanket": Friston, *The free-energy principle: a unified brain theory?* (Nature Rev. Neurosci. 11, 2010) and successors; for the formal-mathematical FEP, Friston et al. *Mathematical foundations of active inference* (Entropy 2022).
- "Arrow of time": Eddington, *The Nature of the Physical World* (1928); modern reviews include Zeh, *The Physical Basis of the Direction of Time* (Springer, 5th ed. 2007).
- "Hallucination" (in the deep-learning sense): the LLM hallucination literature; for a representative reference, see surveys post-2020. Carried label; specific citation required at v0.1.

The labels "Universal Overflow Law" and "Arithmetic Decoupling of Projection-Closure Overflows" are *internal program language*, not borrowed external concepts. They are defined once in §1 and §3 of this paper; they are not re-used elsewhere without re-anchoring.

### 7.4 v2insert-04 §3.1 three-outcome matched-pair rule (binding)

Every matched-pair claim in this paper pre-claims three branches, never two. Audit α/η of §5 pre-claims K / L / joint-on-disjoint; audit ν of §6.2 pre-claims K / L / joint-on-disjoint; audit ζ of §6.3 retains its v2insert-02 three-outcome pre-claim; audit κ of §6.4 retains its v2insert-05 three-outcome pre-claim; the FEP-3 audit of §6.5 is staged as three-outcome at the moment of its concrete specification.

### 7.5 Method-improvement-event tracking

Audits α/η + θ + ι (v2inserts 08–10) returned **K-branch on the headline claims with joint-on-disjoint sub-findings at the exponent (θ) and at the corrections (ι)**. The present paper has been updated to a v0.1 incorporating the realized settlements (§5); the method-improvement events at the joint-on-disjoint level are recorded honestly under v2insert-04 §3.1's binding three-outcome rule, mirroring the v2insert-02 → v2insert-04 → Paper 35 §3.1 pattern of self-improvement under empirical pressure.

---

## 8. Open questions / next-attack vectors

Carried forward (per Paper 32 §11.4 carried-label discipline + v2insert-04 §3.1 three-outcome rule):

1. **Audit α/η — `ℤ/30` capacity enumeration (running).** Highest priority. Settles row-generalization for Papers 46/47/48 jointly and tests §3's universal framing at the first primorial row beyond `ℤ/6`.

2. **Audit δ — settled at K-branch (2026-05-20).** Finite combinatorial proof on `(ℤ/N)^∧` + numerical verification at orders m = 2..6 on `ℤ/{6, 30, 210}`. Promotes Paper 47 (proposed) C1 from [P at 2nd/4th] to [P at all orders] on every squarefree primorial row. The universal-overflow framing's L2 (decoupling) clause now stands at [P] at every order. Audit ζ subsumed. **Audit μ_30 — geometric realization on `D(ℂ³⁰)` (settled 2026-05-20).** Hessian signature `(1, 6, 892)` + quartic signature `(22, 0, 877)` + HS-orthogonality at `5.82 × 10⁻¹⁶`. Promotes Paper 46 (proposed) C5 from [A] to [P] on the first two primorial rows (`D(ℂ⁶) + D(ℂ³⁰)`).

3. **Audit θ + ι — settled (v2inserts 09 + 10).** Capacity scaling across the primorial ladder `ℤ/{6, 30, 210, 2310, 30030}` returned K-direction at five rows with PNT-heuristic shape match `Capacity_V ~ K · n²·ln(n) / N²` at spread 1.584× and asymptotic slope `→ −2` matching 't Hooft–Susskind / Bousso. Bekenstein literal `1/N` refuted at spread 161×. Carry-forward item: extend audit θ to `ℤ/510510` (~0.05 s additional compute); the PNT-heuristic shape predicts `Capacity_V(ℤ/510510) ≈ 1.7 × 10⁻⁹` — a direct test of the joint-on-disjoint settlement.

4. **Audit ι — Bousso-shape comparison (open, v2insert-03 §6).** Identifies which (if any) peer-reviewed holographic shape `Capacity_V` decay matches. Distinct from §11.1 emergent-gravity positioning: it is a structural shape-comparison audit, not a physical-gravity claim.

5. **Audit κ — inference-side V/M propagation on Llama-3.1-8B / Mistral-7B-v0.3 (deferred for compute, v2insert-05; partial settlement v2insert-07 §3).** Restoring HuggingFace + GPU access settles P8 (digits), P9 (months), P10 (weekdays control) at the layerwise resolution Paper 36 §2.3 specifies.

6. **Audit ν — cross-manifestation natural-transformation structure (settled 2026-05-20 at joint-on-disjoint).** Identity-on-certificate-ingredients is a natural transformation between any pair of manifestations' closure-certificate functors in `CertificateCategory` (abstract level [P]); no literal-substrate natural transformation exists (literal level [L-branch realized]). The universal-overflow framing has functorial content at the closure-certificate-shape level; no literal-mechanism functoriality across substrates. Fifth named joint-on-disjoint outcome of the 2026-05-20 session.

7. **FEP-3 sector-resolution audit (Paper 32 §6.2A Corollary 6.3 T3, settled 2026-05-20 at K-branch [P] structural).** Variational free-energy on `D(ℂ⁶)` decomposes additively as `F = F_V + F_M` with F_V Hamiltonian (V-supported, reversible) and F_M gradient-of-entropy (M-supported, irreversible). Four predicates verified at machine precision: V-rays Hamiltonian; M-rays gradient-of-entropy; V ⊥ M cross-coupling zero; F = F_V + F_M additive. Arrow of time = direction of ∇F_M. Friston FEP `F = E - C + S` ↔ V/M sector resolution at Lie-algebra-of-decoupling level. Empirical biological-system applicability remains [C, reduced] (deferred for ground-truth active-inference data).

8. **The unified Paper 36 + Paper 37 + Paper 47 + Paper 48 + Paper 49 figure (v2insert-06 §8 point 3).** Producible once audit κ is restored. A single overlay figure showing: (a) the V/M packet ratio heatmap from audit λ; (b) the depth-normalized saturation indices from audit κ; (c) the capacity-decay curve from audits η + θ; (d) the structural-shape comparison from audit ι. Five papers, one figure, one arithmetic root.

9. **Audit λ cross-task extension (digits, weekdays; v2insert-06 §8 point 2).** Currently audit λ tests on `ℤ/12` months only. Extension to digits (`ℤ/10`, two-prime squarefree) and weekdays (`ℤ/7`, prime negative control) provides a 3-task × 2-audit-type (training + inference) test matrix.

10. **The connection to Paper 47's row-generalization (audit α / `ℤ/30`) on the training side (v2insert-06 §8 point 4).** If audit λ K-confirms on `ℤ/30`-trained MLPs, the row-generalization claim of Paper 49 §3 strengthens at the empirical AI tier as well.

---

## 9. Discipline closing note

This paper is the program's strongest external-correspondence synthesis to date. Five discipline rails are binding from v0.0 forward:

(a) **The universal-overflow framing is correspondence language, not derivation.** Every section makes this visible; §1.2 records it at the paper level; the closing correspondence-reading paragraphs of §4.1, §4.2, §4.3 reiterate it for each manifestation; §7 makes it a discipline rail.

(b) **The §11.1 / §11.2 / §11.4 disciplines of Paper 32 are binding verbatim** at the same heaviness as the constituent v2insert-01 / v2insert-02 / v2insert-03 / Paper 47 / Paper 48 disciplines. No physical gravity, no physical thermodynamics, no physical hallucination mechanism, no dimensionful constants, no carried label without anchor-check.

(c) **The three-outcome matched-pair rule (v2insert-04 §3.1) is binding throughout.** Every matched-pair pre-claim has three branches. The audit-α/η outcome (K / L / joint-on-disjoint), the audit-ν outcome (K / L / joint-on-disjoint), and the FEP-3 audit outcome (currently unspecified) all admit the third "joint realization on disjoint sub-structures" branch as a publishable result.

(d) **Tier discipline is honest.** [P] is reserved for what is audited at the order claimed; [A] for what is audit-pending; [C, reduced] for structural correspondence with peer-reviewed external phenomena. The universal-overflow framing of §3 is [C, reduced]; the V/M decoupling on `ℤ/6` at 2nd/4th order is [P]; the row-generalization is settled at [P] by audits α/η/θ on five primorial rows with structural shape characterized at [A] by audit ι.

(e) **The "epic" framing of the paper comes from structural scope and arithmetic tightness, not rhetorical inflation.** The one-line arithmetic anchor (`3 + 3 + 3 = 9 ≢ 0 (mod 6)`) supports the three-manifestation synthesis at the projection-closure tier; the synthesis is publishable, falsifiable, and tier-tagged. Resist any move toward more grandiose framing in subsequent revisions.

The pattern echoes the program's standing structural unification grammar: delusion proposes the universal-overflow correspondence across cosmology / AI / biology; paranoia bounds it with falsifiers, three-outcome pre-claims, and the §11.1/§11.2/§11.4 disciplines binding verbatim; grounded executes via audits α/η/θ/ι across the primorial ladder (now settled at K-branch on five rows), audit δ (now settled at K-branch — all orders at [P] on every squarefree primorial row), audit μ_30 (now settled at K-branch — geometric realization on `D(ℂ³⁰)` at [P]), audit κ for inference-side propagation (deferred for compute), and the FEP-3 audit for biology (open). The remaining open audits (β, γ, ε, κ, FEP-3) and the cross-manifestation natural-transformation audit ν are the concrete next compute / structural work.

The load-bearing arithmetic remains one line. `3 + 3 + 3 = 9 ≢ 0 (mod 6)`. The remainder is the overflow. The overflow is structural. The structure is the conductor lattice. The conductor lattice is the categorical simplex's discrete information-geometric substrate. And on that substrate, by Pontryagin character orthogonality alone, the kinematic channel V is forced to be HS-orthogonal to the overflow channel M at every order audited — the same arithmetic fact underwrites (a) the V-Lorentzian / M-Euclidean joint realization on the no-boundary Bures lift (cosmology), (b) the V/M packet signature's monotonic dependence on the conductor-aware Pareto-rule weight along Paper 37's iso-loss ridge (deep learning, K-confirmed at audit λ), and (c) the V → M one-way information leakage that takes the structural form of the arrow of time (biology, [C, reduced]). One arithmetic law, three manifestations, four open audits, and the discipline to call the framing what it is: a correspondence across domains that takes its load-bearing weight from the conductor-lattice substrate, not from an asserted physical mechanism.

---

*End Paper 49 v0.4. Status: the program's core arithmetic line is **structurally complete**. Settled audits as of 2026-05-20: α/η (`ℤ/30` row-generalization, K), θ (5-row primorial ladder, K + joint-on-disjoint at exponent), ι (Bousso shape, K-leading + joint-on-disjoint at corrections), δ (all-orders Pontryagin, [P] all orders all primorial rows), μ_30 (geometric realization on `D(ℂ³⁰)`, K), ξ (6-row capacity to `ℤ/510510`, K with K-drift), χ (non-squarefree extension to `ℤ/10` + `ℤ/12`, K on binary V/M, joint-on-disjoint on V/W/M trichotomy), β (Hartle–Hawking Lie-algebra dictionary, K + row-3 dimensional generalization), γ (classical-limit identification with Lemma 9.2, [P]), ε (QG-mixing-bypass Lie-algebra dictionary, [P]-spirit), λ (training-side V/M propagation, K), **ν (cross-manifestation natural-transformation, joint-on-disjoint at abstract-vs-literal levels)**, and **FEP-3 (variational-free-energy metriplectic split on D(ℂ⁶), K [P])**. The universal-overflow framing of §3 has [P] anchors at every tier: the arithmetic substrate ([P] all-orders on every squarefree primorial row + extensions to ℤ/10 + ℤ/12), the geometric realization (D(ℂ⁶) + D(ℂ¹⁰) + D(ℂ¹²) + D(ℂ³⁰)), the quantitative-capacity tier (six primorial rows), the classical-limit recovery (Lemma 9.2), the external-correspondence dictionaries ([P]-spirit: Hartle–Hawking + QG-mixing-bypass + Friston FEP at Lie-algebra level), and the **functorial-framework level** (audit ν: identity-on-certificate-ingredients is a natural transformation in CertificateCategory; literal-substrate functoriality does not exist). The three-outcome matched-pair rule (v2insert-04 §3.1) has now produced **five named joint-on-disjoint outcomes**: audit θ at exponent (super-exponential in n); audit ι at corrections (polynomial-log prefactor); audit β at row 3 (dimensional generalization of HH's imaginary time); audit χ at tangent trichotomy (W ⊥ M overlap on ℤ/12); audit ν at abstract-vs-literal natural-transformation levels (structural shape shared, substrate not). Remaining open audits: μ_210 + higher (geometric realization on D(ℂ²¹⁰) and beyond, memory-bounded); κ (real-transformer V/M propagation, deferred for GPU + HuggingFace); FEP-3 empirical (active-inference biology data, deferred for ground-truth datasets). The proposed-paper triad (Papers 46 / 47 / 48) is now at v0.3 incorporating thirteen settled audits.*

<!--
NOTE TO SELF (drafting closure, 2026-05-20):

DELIVERABLES TRACKED FOR V0.1:
- Verify §5.2 V_idx / M_idx specification against compute_z30_atlas.py output.
- Verify §5.2 dimensional counts of v2insert-03 §1.2 table (V dim 7, M dim 22 on ℤ/30) against actual character-conductor enumeration.
- Read INSERT 06 (causal_structure_arrow_of_time.md) and integrate into §4.3 if aligned.
- Read Rosas_2025_conductor_lattice_bridge.md and cite in §4.3.
- Specify FEP-3 audit (§6.5) concrete numerical protocol OR mark §4.3 + §6.5 as structural-reading-only.
- Decide §6.2 audit ν: concrete protocol or downgrade to "open structural question."
- §4.2: weave in Papers 38, 41, 45 as additional cubic-aware practitioner-side defenses.
- §4.2: explicitly mark "hallucinations as M-channel overflow" as [C, reduced] correspondence-language pending audit κ restoration.
- §2.3: consider folding §2.3 into §2.4 for compression.
- §3.3: clarify that "M dimensionally smaller than V" is Z/6-specific (false on Z/30 per v2insert-03 §1.2).
- §1.1: a one-paragraph contrast between "saturation cliff" (numerical overflow → NaN cascade) and "Pontryagin-clean routing into M" worth adding.
- §7.3 carried-label list: confirm Wurgaft 2026 / Rosas 2025 references against the repo's reference set.
- Final-pass tier audit: ensure no claim is asserted at higher tier than its anchor supports.

OPEN AUDIT DEPENDENCIES (to be settled before v1.0):
- Audit α/η (running): settles row-generalization for §3 universal claim.
- Audit δ (open): settles all-orders V/M decoupling for §3 L2 clause.
- Audit ζ (open): settles all-orders observable mixing for §6.3 falsifier.
- Audit κ (deferred): settles inference-side AI propagation for §4.2 + §6.4.
- FEP-3 audit (unspecified): settles biology manifestation for §4.3 + §6.5.

OPEN STRUCTURAL QUESTIONS (carried forward):
- Cross-manifestation natural-transformation structure (audit ν, §6.2).
- Capacity-decay shape vs Bousso bound (v2insert-03 audit ι; §8 point 4).
- Whether the §3 "universal" qualifier survives the cross-manifestation audit ν (audits α/η/θ/ι have settled the row-generalization at K-branch; ν remains open).

DISCIPLINE-RAIL SELF-CHECK (Paper 35 §3.4):
- All [P] claims in this draft are anchored to v2insert-01/-02/-03/-04/-05/-06/-07 + Paper 32/34/35/36/37 sections cited verbatim. Verify each citation lands at v0.1.
- All [A] and [C, reduced] claims are tier-tagged honestly.
- All falsifiers are pre-claimed under v2insert-04 §3.1 three-outcome rule.
- The paper does not introduce any new tier-tag conventions; it uses the existing [P]/[A]/[C, reduced] discipline of Paper 35 §3.4 verbatim.
- No status flags ([DEPENDS ON X], [REVISION REQUIRED]) anywhere in the body — only HTML notes-to-self for drafting iteration, which are clearly delimited.

WORDS TO AVOID (carried-label-style risk):
- "Theory of everything" (never used; do not introduce).
- "Unified" (used once in v2insert-01 §3 narrative; in this paper restricted to v2insert-1-style "unified structural picture" reading, not asserted as a derivation).
- "Final" (never used).
- "Necessarily" (used once in §3.4; check at v0.1 for tier-discipline coherence).
- "Proof of" (used only where audit δ etc. is referenced; do not extend).

TARGET LENGTH AT V1.0: ~800-1200 lines, after expansion of §4.3 + §6.2 + integration of audit α/η outcome. Current draft is ~600 lines. Acceptable for v0.0.
-->
