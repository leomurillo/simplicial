# 50. The Closure Certificate: A Schema for Projection-Validity on Finite Conductor Lattices

**From a Six-Slot Definition to a Composable, Falsifier-Typed Object**

**Leonardo Murillo Montero**
*leonardo.murillo@gmail.com*

*Draft 0.0 — 2026-05-21*

**Tier tags.** [D] for the schema-formalization itself (Definitions 4.1–4.7, Sections 5–7): this paper does not add new audited facts; it promotes already-defined material from Paper 31 §5 to a typed composable object and proves the schema-level identities that follow from already-settled audits. [P] for the schema-instance settlements imported from already-settled audits (α/η, δ, θ, ι, ξ, χ, μ_30, λ; FEP-3 sector-resolution audit, 2026-05-20) wherever a schema-instance appears in the worked-example appendices. [A] for the closure-certificate naturality and functoriality propositions of §6: their *statements* are formal consequences of [P]-anchored audits but their *proofs* in full generality are research gates explicitly inherited from Paper 31 §16 (Gates M1, M2, M5). [C, reduced] for the three external-correspondence appendices of §8 (cosmology / AI / FEP-3): they are imported as instances of the schema, *not* re-derived; tier discipline tracks the source paper (Paper 46 [P] for HH signature on `ℤ/6`; Paper 34 [P] for the conductor blind spot on `ℤ/N`; Insert 15 FEP-3 audit [P] for the gradient-vs-least-action sector resolution on `ℤ/6`). The arrow-of-time, holographic-bound, and hallucination-mechanism readings remain at the tier in which they live in their source papers (Paper 49 §4); this paper does *not* upgrade them.

**Anchor papers (binding).** Paper 29 *Participation Metrics and Identity-as-Participation* (the participation side: `SN_W(A,B)` as the source of the `𝖯` slot). Paper 30 *Constrained Overflow and Incompatibility Budgets* (the residual side: the typed tuple `R_W` as the source of the `𝖱` slot). Paper 31 *Projection-Closure Theory* (the closure certificate `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)`, Definitions 5.1–5.2, Proposition 5.4, Conjecture 15.1, Research Gates M1–M8). Paper 32 §6.2 Lemma 6.1a–c, §13.2B (the load-bearing arithmetic substrate for every worked example: Pontryagin character orthogonality on `ℤ/6`). Paper 47 *Arithmetic Decoupling Theorem* (the row-stability of V ⊥ M used by `𝖲` in §5). Paper 48 *Conductor Capacity Bound* (the explicit `𝖡` budget used by §6). Paper 49 *Arithmetic Decoupling of Projection-Closure Overflows* (the synthesis voice this paper is deliberately *not* in: §1.3 below).

<!--
NOTE TO SELF (draft 0.0): This paper occupies a niche that Paper 31 and Paper 49 together leave open. Paper 31 introduces the closure certificate as a tuple of definitions with one worked example (its §5.5 on ℤ/6). Paper 49 uses the certificate as load-bearing vocabulary for a three-domain synthesis. Neither paper treats the certificate as a *formal object that has an algebra* — that can be composed, refined, restricted, and pulled back along projection morphisms, and that supports schema-level theorems independent of any one instance.

The gap is exactly what a IMO-trained research director would notice: Paper 31 stated definitions but never wrote down the closure-certificate category. This paper writes down that category, proves the schema-level identities that are forced by already-settled audits (row-stability, capacity-monotonicity, naturality under refinement), and stages the rest as gates inherited from Paper 31 §16.

DISCIPLINE: do NOT inflate. The schema-formalization is the [D]-tier contribution; the worked examples are [P]/[C, reduced] inherited from their source papers WITHOUT upgrade. The point of Paper 50 is to make the closure certificate a first-class formal object in the program, not to re-prove anything. The reader should be able to leave §7 with a working notion of how to *write* a closure certificate for a new projection (including F-slot pre-claim), then read §8 only as appendices.

OPEN: a category-theoretic treatment of the F-slot (falsifier as functor into the truth-value lattice, or as morphism into a pre-claim category) would be the natural next step. Held for Paper 51 or a §6.4 stub.
-->

---

## Abstract

Paper 31 introduced the closure certificate `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` as the validity object for a projection `Π` from a richer whole `W` under a declared task `T`, horizon `H`, and cutoff `K`. The introduction was tuple-valued: six slots with prose definitions and one worked example on `ℤ/6`. Paper 49 used the same certificate as load-bearing vocabulary for a three-domain synthesis (cosmology, deep learning, active inference). Neither paper treated the certificate as a *formal object with an algebra*.

The present paper does that. We promote the closure certificate from a tuple of definitions to a *typed composable schema* on the category of conductor-lattice projections. Each slot becomes a typed object: participation `𝖯` lives in the participation-functor image of Paper 29's `SN_W`; the residual `𝖱` lives in the typed-residual tuple of Paper 30; the bound `𝖡` lives in a partial-order of capacity functions controlled by Paper 48; the stability `𝖲` lives in a recurrence-functor over the primorial-row inclusion semigroup; the time-translation/Noether slot `𝖤` lives in a Noether-defect lattice; and the falsifier `𝖥` lives in a pre-claim category with explicit positive, negative, and joint-on-disjoint branches. Schema morphisms — refinement (under finer projection), composition (under chained projection), restriction (under task narrowing), product (under joint projection), and row-extension (under primorial inclusion) — are then well-typed.

With this typing, three schema-level identities become provable from already-settled audits without any new empirical input:

1. **(Row-stability functoriality, [P] from audits α/η + θ + ξ + χ).** The `𝖡` slot is functorial under the primorial-row inclusion `ℤ/6 ↪ ℤ/30 ↪ ℤ/210 ↪ ⋯ ↪ ℤ/510510`: the V-sector capacity decreases monotonically along the ladder, and the M-sector budget extends by complement at each rung.
2. **(Refinement monotonicity, [P]-spirit, partial — Gate M1 from Paper 31).** Under a refinement `Π' ⊑ Π` (finer projection retaining more participation), the `𝖱` slot's typed components grow or stay flat in support, and the `𝖡` slot's per-type bounds tighten or stay flat. Equality on all six slots is the closure-certificate naturality criterion.
3. **(F-slot sufficiency, [D]).** The falsifier slot `𝖥` is a *sufficiency* slot, not a necessity slot: passing all declared falsifiers establishes closure-validity *for the declared task and horizon*, not for refinements of the task or extensions of the horizon. A new task or longer horizon requires a new certificate; it does not reopen the old one.

We catalogue four worked-example schemas in the appendices, each instantiating the same six slots on the same arithmetic substrate (`ℤ/6` and its primorial extensions): the cubic Amari–Chentsov projection of Papers 30 and 31; the Hartle–Hawking V-Lorentzian / M-Euclidean projection of Paper 46; the conductor-blind-spot projection of Paper 34; and the FEP-3 sector-resolution projection of Insert 15. Each appendix fills the six slots from its source paper *without re-derivation*. The point is not the manifestations; the point is that they all fit one schema.

The contribution is one [D]-tier object — the closure-certificate schema — and three [P]-anchored schema-level identities that follow from already-settled audits. The paper does not derive physical gravity, hallucination mechanism, or biological time. It does not extend Paper 47's row-stability theorem or Paper 48's capacity bound. It does specify what an instance of the schema *is*, what its morphisms *are*, and what completing the F-slot for a new projection *requires*.

**Keywords:** closure certificate, projection-closure theory, categorical simplex, conductor lattice, Pontryagin character orthogonality, schema-formalization, falsifier discipline, three-outcome pre-claim, F-slot, conductor-capacity functoriality.

**MSC 2020:** 03B70 (logic of computability and information), 11L03 (trigonometric and exponential sums), 18A99 (general theory of categories), 18C50 (categorical semantics of formal languages), 62B11 (information geometry), 68T07 (artificial neural networks and deep learning).

---

## 1. Introduction

### 1.1 The schema-formalization gap

The simplicial program reached a five-paper synthesis (Papers 30, 31, 46, 47, 48, 49) in which a single arithmetic substrate — Pontryagin character orthogonality on the conductor lattice of a primorial row — supports a typed decomposition of cubic information-geometric structure into a kinematic sector V and a cross-prime residual sector M. The validity of any projection onto V (with M as overflow) is checked by a six-slot closure certificate, introduced in Paper 31 §5 as Definition 5.1:

> `𝒞_W(Π; T, H, K) = (𝖯_W^Π, 𝖱_W^Π, 𝖡_W^Π, 𝖲_W^Π, 𝖤_W^Π, 𝖥_W^Π)`.

Paper 31 stated each slot as a prose definition and gave one worked example (its §5.5 on `ℤ/6`). Paper 49 used the same certificate as the load-bearing vocabulary for a three-domain synthesis (its §4: cosmology, deep learning, active inference). Between Paper 31's definitions and Paper 49's synthesis there is a gap: the certificate has never been treated as a *formal object*. It has no declared morphism class. It has no schema-level theorems. Its falsifier slot `𝖥` is a free-text list, not a typed pre-claim. The "open F-slot" pattern of Paper 31 §14 (the worked DCD example) is described informally, not as an instance of a general schema operation.

The present paper writes down that schema. It is a [D]-tier paper — a definitional / formal paper — that re-frames already-existing material without adding new audits. Its contribution is one object (the closure-certificate schema), one algebra of morphisms on that object (Definitions 5.1–5.5), and three schema-level identities that follow from already-settled audits (§6).

### 1.2 What this paper is *not*

This paper is deliberately *not*:

- *A new synthesis.* Paper 49 already states the universal-overflow synthesis across cosmology, deep learning, and active inference, with the tier discipline calibrated per manifestation. Paper 50 imports each manifestation as a schema instance in the appendices without re-deriving any of Paper 49's structural correspondences.
- *A new arithmetic-substrate theorem.* Paper 47 (V ⊥ M as Hilbert subspaces, all orders by audit δ) and Paper 48 (V-capacity decay along the primorial ladder) are the binding arithmetic-substrate theorems. Paper 50 imports them; it does not extend them.
- *A philosophical paper.* The schema is a formal object. Its purpose is to make new closure-certificate instances writable in a uniform way, with the F-slot promoted from a free-text list to a typed pre-claim with declared positive, negative, and joint-on-disjoint branches.
- *A bid for a closure-certificate theorem.* Paper 31 Conjecture 15.1 (bounded projection closure) remains open. This paper does not attempt that theorem. It does establish that three of its sub-claims (row-stability functoriality, refinement monotonicity, F-slot sufficiency) follow from already-settled audits at the *schema* level.

### 1.3 Relation to Papers 31 and 49

The relation is summarized by:

| Object | Paper 31 (introduces) | Paper 49 (uses) | Paper 50 (formalizes) |
|---|---|---|---|
| Closure certificate `𝒞_W(Π; T, H, K)` | Definition 5.1 (tuple of prose definitions) | Load-bearing vocabulary in §4 (one instance per manifestation) | Typed composable schema with algebra of morphisms (Section 4) |
| Participation slot `𝖯` | Prose; pointer to Paper 29 `SN_W` | Read off per manifestation | Typed: image of the participation functor `Π_*: SN_W → 𝖯_W^Π` (Definition 4.1) |
| Residual slot `𝖱` | Prose; pointer to Paper 30 typed tuple | Read off per manifestation as V/M decomposition | Typed: image of the residual functor `Π^*: R_W → 𝖱_W^Π` with explicit type signature (Definition 4.2) |
| Bound slot `𝖡` | Prose; per-slot prescription (norm, packet-support, lift-recovery, finite-jet, Noether, Filippov, prediction-horizon) | Per manifestation, ad-hoc | Typed: element of a partial order of capacity functions controlled by Paper 48 (Definition 4.3) |
| Stability slot `𝖲` | Prose; controls + feedback + recurrence | Per manifestation, ad-hoc | Typed: element of a recurrence-functor lattice over the primorial-row inclusion semigroup (Definition 4.4) |
| Time/Noether slot `𝖤` | Prose; Noether energy + Filippov defect | Per manifestation, ad-hoc | Typed: element of the Noether-defect lattice with Filippov-defect sub-slot (Definition 4.5) |
| Falsifier slot `𝖥` | Free-text list (Paper 31 §17 F1–F8) | Free-text per manifestation; three-outcome pre-claim language (v2insert-04 §3.1) | Typed: pre-claim object in the matched-pair category with positive, negative, and joint-on-disjoint branches (Definition 4.6) |
| Worked example | One: `ℤ/6` (Paper 31 §5.5) | Three: cosmology, AI, FEP-3 (Paper 49 §4) | Four (Appendices A–D): the same three plus the canonical Z/6 cubic Amari–Chentsov projection of Papers 30 §9.6 + 31 §5.5 |

The dependency direction is: Paper 31 introduces the certificate object; Paper 49 uses it; Paper 50 formalizes it. Paper 50 has *no* downstream papers as a strict dependency at draft 0.0.

### 1.4 Reading guide

§2 fixes the arithmetic-substrate vocabulary by importing the load-bearing definitions from Papers 30, 31, 32. §3 imports the closure-certificate definition from Paper 31 §5 verbatim and identifies its formal-object gap. §4 promotes each of the six slots from a prose definition to a typed object. §5 defines the schema morphisms (refinement, composition, restriction, product, row-extension). §6 states the three schema-level identities ([P]-anchored from existing audits) and identifies which Paper 31 research gates they partially settle. §7 specifies the F-slot type signature and the open-F-slot pattern in formal language; this is the most useful section for writing new closure certificates. §8 collects the four worked-example schemas in appendix form. §9 lists schema-level research gates (deferred to Paper 51 or later). §10 closes with the schema's own falsifiers. References follow.

---

## 2. Arithmetic Substrate

This paper does not re-derive the arithmetic substrate. It imports the load-bearing objects from Papers 30, 31, 32 and re-states them in a uniform notation for the schema-formalization.

### 2.1 The conductor lattice on `ℤ/N`

Let `N ≥ 2` and let `R = ℤ/Nℤ`. The dual group `R^∧` consists of additive characters `χ_k(j) = exp(2πi · k · j / N)` for `k ∈ ℤ/N`. The *conductor* of `χ_k` is `c(k) := N / gcd(k, N)`. The *conductor packet* `H_d` of conductor `d | N` is the span of all characters with conductor exactly `d`:

```
H_d := span_ℂ{χ_k : c(k) = d},  dim_ℂ H_d = φ(d).
```

The non-trivial conductor packets partition the orthogonal complement of `ℂ𝟙 = H_1` into `Σ_{d | N, d > 1} φ(d) = N - 1` dimensions. The *conductor lattice* of `ℤ/N` is the partial order of packets indexed by `d | N` with `d > 1`.

### 2.2 The V/M decomposition

For a squarefree primorial row `N = p_1 · p_2 · ⋯ · p_n`, the V/M decomposition (Paper 47 Theorem 3.1) is the binary partition of the conductor lattice:

```
V := ⊕_{p | N, p prime} H_p,    M := ⊕_{d | N, d composite} H_d.
```

V is the *single-prime* (or *prime-power*) sector; M is the *cross-prime carry* sector. The two are Hilbert-subspace orthogonal in `ℂ^N` (Paper 47 Theorem 3.1, [P] all-orders by audit δ); they remain so under the primorial inclusion `ℤ/p_1 ⋯ p_n ↪ ℤ/p_1 ⋯ p_{n+1}` (Paper 47 §3.6, [P] by audits α/η + θ + ξ).

For the minimal mixed row `N = 6 = 2 · 3` (Paper 31 §5.5 + Paper 32 §6.2 + Paper 47 §3.2), the V/M decomposition is:

```
V = A_2 ⊕ A_3,    A_2 = H_2 = span⟨χ_3⟩,    A_3 = H_3 = span⟨χ_2, χ_4⟩,
M = H_6 = span⟨χ_1, χ_5⟩.
```

The load-bearing arithmetic on this row is the cubic-vacuity computation of Paper 32 Lemma 6.1a:

```
3 + 3 + 3 = 9 ≡ 3 ≢ 0 (mod 6).
```

The pure-A_2 cubic closure fails on `ℤ/6` because the closing-triple selection rule `k + ℓ + m ≡ 0 (mod 6)` cannot be satisfied with three copies of the only A_2 index `k = 3`. The A_3 sector closes purely through `(2,2,2)` and `(4,4,4)`. Every A_2 ↔ A_3 cubic transfer requires routing through M: e.g. `3 + 2 + 1 ≡ 0 (mod 6)` and `3 + 4 + 5 ≡ 0 (mod 6)`.

### 2.3 The cubic Amari–Chentsov tensor

On the categorical simplex `Δ_R^∘`, the cubic Amari–Chentsov tensor at the centroid `p_* = (1/N, …, 1/N)` is, in the character basis (Paper 32 §6.2 + Paper 47 Remark 3.4):

```
T^(AC)_{k ℓ m}(p_*) = c_N · 𝟙[k + ℓ + m ≡ 0 (mod N)].
```

This is the abelian-BF 3-vertex amplitude on the finite group `ℤ/N` in the character basis (Paper 47 Remark 3.4; one-line Fourier derivation via character orthogonality). The V-supported component of `T^(AC)` lies in `V^⊗3 ∩ {closing triples}`; the M-supported component is its orthogonal complement inside the closing-triple-supported subspace.

### 2.4 Notation for the rest of the paper

We fix the following notation throughout:

- `W` is a *whole*: the eight-tuple `(𝒳, 𝒪, 𝒯, 𝒬, 𝓛, 𝒦, ℋ, 𝒩)` of Paper 31 Definition 4.1.
- `Π` is a *projection*: a map or model-class `Π : 𝒳 → 𝒴` (Paper 31 Definition 4.2).
- `T` is a *task*; `H` is a *horizon*; `K` is a *cutoff* (Paper 31 Definition 5.1).
- `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` is the closure certificate (Paper 31 Definition 5.1). Subscripts `_W^Π` are suppressed when context fixes them.
- `Π_V : ℂ^N ↠ V` is the V-projection; `Π_M : ℂ^N ↠ M` is the M-projection. Either may serve as `Π` in a closure certificate.
- `𝒞at_W` is the category of conductor-lattice projections on `W` (objects: projections `Π`; morphisms: see §5). `𝒞ert_W` is the category of closure certificates on `W` (objects: certificates `𝒞_W(Π; T, H, K)`; morphisms: see §5).

---

## 3. The Closure Certificate: Importing the Object

This section imports Paper 31 Definition 5.1 verbatim and identifies the formal-object gap that motivates §4.

### 3.1 Closure certificate (Paper 31 Definition 5.1)

> For a projection `Π`, task `T`, horizon `H`, and cutoff `K`, define
> ```
> 𝒞_W(Π; T, H, K) = (𝖯_W^Π, 𝖱_W^Π, 𝖡_W^Π, 𝖲_W^Π, 𝖤_W^Π, 𝖥_W^Π).
> ```
> The entries are:
> 1. `𝖯_W^Π`: participation retained by the projection;
> 2. `𝖱_W^Π`: typed residuals created by the projection;
> 3. `𝖡_W^Π`: residual bounds or explicitly unbounded entries;
> 4. `𝖲_W^Π`: stability conditions under recurrence, feedback, controls, perturbations, or horizon extension;
> 5. `𝖤_W^Π`: time-translation and Noether-energy closure, or the typed residual marking its failure;
> 6. `𝖥_W^Π`: falsifiers and controls.

### 3.2 Closure-valid projection (Paper 31 Definition 5.2)

> A projection `Π` is *closure-valid* for `(W, T, H, K)` if:
> 1. all task-required participation components survive `Π`;
> 2. all forbidden residuals vanish;
> 3. all allowed residuals are bounded by the declared tolerance on `H`;
> 4. residuals remain stable under the declared controls and feedback protocol;
> 5. time-translation closure is preserved for the admitted Noether energy, current, or form, or its failure is typed and bounded;
> 6. any declared Nambu-Fisher bracket preserves its fundamental/Filippov identity, or the projected defect is typed and bounded;
> 7. the falsifiers in `𝖥_W^Π` are passed;
> 8. unobserved residual entries are marked unobserved, not silently set to zero.

We write `Π ∈ ClValid(W, T, H, K)`.

### 3.3 What is missing

Paper 31 §5 supplies the *object*. It does not supply:

1. **Type signatures.** Each slot is described in prose. There is no declared codomain for `𝖯`, `𝖱`, `𝖡`, `𝖲`, `𝖤`, `𝖥` as objects in some category. Without type signatures, "what is a closure certificate, formally?" has no answer beyond "a tuple of six things, each defined ad hoc per use."
2. **Morphisms.** Paper 31 §15 (Conjecture 15.1) bundles closure-validity into a single propositional fact about a tuple. It does not describe how closure certificates *transform* under refinement of `Π`, composition of `Π`'s, restriction of `T`, joint product of `Π`'s, or extension of `W` along the primorial-row inclusion. Yet Paper 47 §3.6 and Paper 48 §6 already establish row-stability — i.e., the row-extension morphism exists and is well-behaved — at the level of the underlying audits. The schema-level formulation is missing.
3. **F-slot typing.** Paper 31 §17 lists eight free-text falsifiers (F1–F8) for the whole framework, and Paper 31 §5.5 lists three free-text falsifiers for the `ℤ/6` worked example. Paper 49 uses the three-outcome matched-pair pre-claim language (v2insert-04 §3.1) per manifestation. Neither paper writes down the *type* of an F-slot entry — specifically, neither says what it means for a falsifier to be "declared in advance" as opposed to "noticed in retrospect" in formal terms.
4. **An algebra over instances.** Paper 31 §5.5 gives one `ℤ/6` instance. Paper 49 §4 gives three more. There is no formal statement of which schema-level identities hold between them — even though Paper 47 §3.6 and Paper 48 §6 jointly imply that several do.

§4 supplies the type signatures. §5 supplies the morphisms. §6 proves the three schema-level identities that already follow from settled audits. §7 supplies the F-slot type signature. §8 reconciles the four worked examples under one schema.

---

## 4. Each Slot as a Typed Object

This section promotes each of the six slots from a prose definition to a typed object. The promotion is forced: each slot already has a precise underlying object in Papers 29, 30, 32, 47, 48; the promotion only names the codomain.

### 4.1 Participation `𝖯` as functor image

**Definition 4.1 (Participation slot, typed).**
Let `Part_W : 𝒞at_W → Set` be the participation functor of Paper 29 (sending a projection `Π` to the participation object `SN_W(·, ·; Π)`). The participation slot is the image:
```
𝖯_W^Π := Part_W(Π) ⊂ Π(𝒳) × Π(𝒳)
```
with elements typed by the conductor-packet decomposition of Π(𝒳) when `Π` is a conductor-respecting projection on `Δ_R^∘`. Specifically, for `Π = Π_V : ℂ^N ↠ V`, `𝖯_W^{Π_V}` decomposes as `⊕_{p | N, p prime} 𝖯|_{H_p}` with each summand a Hellinger/Fisher participation object on the single-prime axis `H_p`.

**Remark 4.1.1.** This typing makes `𝖯` *not* a set of prose claims but an object in the participation-functor image. Two projections `Π, Π'` with identical participation images have *the same* `𝖯`-slot; "loss of participation" under refinement is then expressible as set-inclusion `𝖯_W^Π ⊂ 𝖯_W^{Π'}`.

### 4.2 Residual `𝖱` as residual-functor image

**Definition 4.2 (Residual slot, typed).**
Let `Res_W : 𝒞at_W → R_W` be the residual functor of Paper 30 (sending a projection `Π` to the seven-tuple residual object `R_W(·, ·; Π)` of Paper 30 §5.2). The residual slot is the image:
```
𝖱_W^Π := Res_W(Π)
       = (R_{quotient}, R_{Cartan}, R_{Bures/dephase}, R_{Ext_CH},
          R_{cubic}, R_{hc}^≥4, R_{recursive})_W^Π.
```
Each component is typed by its source paper:
- `R_{quotient}` ∈ packet-support functions on the divisor lattice of `N` (Paper 30 Def 6.1; Paper 26 exact divisor rule).
- `R_{Cartan}` ∈ admissible-algebra quotient `G_{full}/G_{real}` (Paper 30 Def 7.1; Papers 14, 24).
- `R_{Bures/dephase}` ∈ HS-distance on `𝒟(ℂ^N)` (Paper 30 Def 7.2; Papers 15, 18).
- `R_{Ext_CH}` ∈ filtered-carry class modulo section coboundaries (Paper 30 Def 8.1; Papers 10, 11, 13).
- `R_{cubic}` ∈ cubic-closure defect (Paper 30 Def 9.1; Papers 17, 24).
- `R_{hc}^≥4` ∈ higher-cumulant residual tower (Paper 30 Def 9.2).
- `R_{recursive}` ∈ prediction/update mismatch (Paper 30 §5.2; Paper 29 §recursive).

For `Π = Π_V : ℂ^N ↠ V` on a squarefree primorial row `N`, the residual is concentrated in `R_{cubic}` with M-supported value (Paper 47 §3, [P] all-orders by audit δ):
```
𝖱_W^{Π_V}|_{R_{cubic}} = P_M T^(AC)_{k ℓ m} = T^(AC)|_{closing triples with ≥1 M-leg}.
```
All other typed components are either zero (e.g. `R_{quotient}` if no quotient is taken), unobserved (e.g. `R_{Bures/dephase}` if `W` does not declare a Bures lift), or inherited from the source paper's audit.

**Remark 4.2.1.** The typing makes "what kind of residual?" answerable without prose: it is a function on the divisor lattice (quotient), a coset of admissible algebras (Cartan), a HS-distance on density matrices (Bures), and so on. The typed residual tuple is *the* invariant datum; scalar aggregation requires task-weights (Paper 30 Guardrail 5.4).

### 4.3 Bound `𝖡` as element of a capacity partial order

**Definition 4.3 (Bound slot, typed).**
Let `𝓑_W` be the partial order of *capacity functions* on the conductor lattice of `W`: functions `b : DivisorLattice(N) → ℝ_≥0 ∪ {∞}` ordered by pointwise inequality. The bound slot is an element:
```
𝖡_W^Π ∈ 𝓑_W,    𝖡_W^Π(d) = bound on the d-conductor-packet component of the residual.
```
For `Π = Π_V : ℂ^N ↠ V`, the bound is read off Paper 48 §3 (the V-capacity count):
```
𝖡_W^{Π_V}(d) = {
    0                                           if d | N and d is a prime power,
    |closing triples on H_d with ≥1 M-leg|      if d | N and d is composite,
    +∞ (i.e., unbounded — Π_V kills this packet) otherwise.
}
```
For `N = 6` (Paper 48 §3.2):
- V-pure closing triples: `(2,2,2)` and `(4,4,4)`, total `T_pure_V = 2`.
- Total closing triples on `ℤ/6`: `T_total = 6` (Paper 48 Table 3.1).
- `Capacity_V(6) = T_pure_V / T_total = 1/3`.
- Bound `𝖡_W^{Π_V}(6) = (T_total − T_pure_V) / T_total = 2/3`.

For the primorial ladder `N ∈ {6, 30, 210, 2310, 30030, 510510}` (Paper 48 §5 audit ξ, [P] settled):
```
𝖡_W^{Π_V}(N) = {2/3, 24/25, 524/525, 26156/26157, 2424195/2424196, 43436743240/43436743350}.
```

**Remark 4.3.1.** Typed bounds compose: under primorial inclusion `ℤ/6 ↪ ℤ/30`, the bound function extends by the audit-θ-confirmed monotone-decrease law (Paper 48 §5, [P]):
```
𝖡_W^{Π_V}(p_1 ⋯ p_n) ↘ 1   as   n → ∞   (M-budget saturates the unit interval).
```
This is the *capacity functoriality* under row-extension. Section 6.1 makes the functoriality statement schema-level.

### 4.4 Stability `𝖲` as recurrence-functor lattice element

**Definition 4.4 (Stability slot, typed).**
Let `𝒮_W` be the recurrence-functor lattice over the primorial-row inclusion semigroup `Pr := (ℤ/6 ↪ ℤ/30 ↪ ℤ/210 ↪ ⋯)`. Elements of `𝒮_W` are commuting diagrams
```
𝖱_W^{Π}|_{ℤ/N} ──row-ext──▶ 𝖱_W^{Π}|_{ℤ/Np_{n+1}}
       │                              │
   𝖡_W^Π|_{ℤ/N}                𝖡_W^Π|_{ℤ/Np_{n+1}}
       │                              │
       ▼                              ▼
     bound at row N      ──monotone──▶     bound at row Np_{n+1}
```
ordered by refinement of the commuting square. The stability slot is the element:
```
𝖲_W^Π ∈ 𝒮_W,
```
declaring which row-extensions, control families, and feedback protocols the residual tuple survives.

For `Π = Π_V : ℂ^N ↠ V` on the primorial ladder, the stability slot is read off audits α/η + θ + ξ + χ (Papers 47 §3.6, 48 §5, [P] settled at five primorial rows + non-squarefree extensions `ℤ/10`, `ℤ/12`):
```
𝖲_W^{Π_V} = ⟨V ⊥ M Pontryagin character orthogonality on disjoint index sets,
              row-stable on the primorial ladder up to ℤ/510510,
              binary-V/M extension to non-squarefree rows ℤ/10 and ℤ/12⟩.
```

**Remark 4.4.1.** The typed stability slot answers the question "what changes if I extend the row?" with a typed morphism (the row-extension functor) rather than a prose claim. Audits α/η + θ + ξ + χ jointly establish that this morphism is the *identity on the V/M typing* and *monotone on the bound* — exactly the typed content of `𝖲_W^{Π_V}`.

### 4.5 Time-translation/Noether slot `𝖤` as Noether-defect lattice element

**Definition 4.5 (Noether slot, typed).**
Let `𝓝_W` be the Noether-defect lattice of `W`: the lattice of pairs `(Q, R^Π_Q)` where `Q` is an admissible conserved Noether charge (energy, current, or form) of the autonomous dynamics on `𝒳` and `R^Π_Q` is the projected Noether defect of `Q` under `Π`. If `W` carries a Nambu-Fisher bracket, `𝓝_W` carries a sub-slot for the Filippov-defect `R_{Filippov}^Π` (Paper 31 §9, Paper 30 Guardrail 9.4). The Noether slot is the element:
```
𝖤_W^Π = (Q, R^Π_Q, R_{Filippov}^Π) ∈ 𝓝_W.
```
Closure-validity (Paper 31 Definition 5.2 condition 5) requires `R^Π_Q` and `R_{Filippov}^Π` to be zero or typed and bounded.

For `Π = Π_V : ℂ^N ↠ V` on `ℤ/6`, the Noether slot is (Paper 31 §5.5 + Paper 17):
```
𝖤_W^{Π_V} = (
    cubic Noether energy of A_3 closure: preserved (the (2,2,2) and (4,4,4) closures
                                          are exact Noether-closed),
    A_2-self Noether defect: zero by inertness (3+3+3 ≢ 0),
    A_2 ↔ A_3 transfer Noether defect: lifted to M as the cubic residual R_{cubic}|_M,
    Filippov defect (if Nambu-Fisher bracket declared): typed as R_{Filippov}^{Π_V} ∈ M
).
```

### 4.6 Falsifier slot `𝖥` as pre-claim object

**Definition 4.6 (Falsifier slot, typed — the most consequential definition of this paper).**
Let `𝒫reClaim_W` be the category whose objects are *three-outcome matched-pair pre-claims* in the sense of v2insert-04 §3.1 (Paper 35 §3.1, extended), and whose morphisms are refinements of the pre-claim (narrower task, tighter horizon, stronger control). An object of `𝒫reClaim_W` is a tuple:
```
F = (F_+, F_−, F_⋈, F_meta)
```
where:
- `F_+` is the *positive-branch* pre-claim: what the projection would establish if the test fires positively.
- `F_−` is the *negative-branch* pre-claim: what the projection would establish if the test fires negatively (this branch is what makes the pre-claim a *falsifier*; it must be non-trivial).
- `F_⋈` is the *joint-on-disjoint* branch: what the projection would establish if positive and negative outcomes appear on disjoint sub-domains. (For the V/M schema, this is the K-branch versus L-branch outcome of v2insert-04 §3.1.)
- `F_meta` is the *meta-discipline*: declaration of which controls rule out frame artifacts, which audits the pre-claim depends on, and which research gates would have to settle to lift `F` from `[A]` or `[C, reduced]` to `[P]`.

The falsifier slot is a finite list:
```
𝖥_W^Π = (F_1, F_2, …, F_m) ∈ List(𝒫reClaim_W),
```
each `F_i` typed by Definition 4.6.

**Remark 4.6.1 (the F-slot type discipline).** A free-text falsifier is *not* an F-slot entry until it has been typed as `(F_+, F_−, F_⋈, F_meta)`. The "open F-slot" pattern of Paper 31 §14 (DCD example) corresponds to a closure-certificate instance whose `𝖥` slot has not yet been populated with a typed pre-claim; the closure certificate is then *not* closure-valid until the F-slot is filled. The three-outcome matched-pair pre-claim discipline is the *minimum* type for an F-slot entry. A two-outcome (yes/no) falsifier is degenerate (`F_⋈` collapsed); a one-outcome (assertion) falsifier is a non-falsifier (`F_−` empty) and does not type-check.

**Remark 4.6.2 (why the F-slot type signature matters).** Paper 31 §17 lists F1–F8 as free-text falsifiers for the whole projection-closure framework. Each can now be typed as a `𝒫reClaim_W` object. For example, F2 ("residual types are frame artifacts") types as:
- `F_+`: residuals are invariant under reasonable equivalent frames; the typed residual tuple `𝖱` is well-defined.
- `F_−`: residuals vary wildly under frame change without invariant content; the typing must be weakened.
- `F_⋈`: residuals are frame-invariant on a sub-domain (e.g. squarefree primorial rows) and frame-variant on the complement (e.g. non-squarefree rows); the typing must restrict to the invariant sub-domain.
- `F_meta`: depends on frame audits (Paper 30 Gate M3); promotes from `[A]` to `[P]` if frame-comparison audits settle on every row.

Section 7 develops the F-slot type signature further.

### 4.7 The closure certificate as typed product

**Definition 4.7 (Closure certificate, typed).**
The closure certificate is the typed product:
```
𝒞_W(Π; T, H, K) ∈ Part_W × Res_W × 𝓑_W × 𝒮_W × 𝓝_W × List(𝒫reClaim_W).
```
where each factor is the codomain of Definitions 4.1–4.6 respectively. Closure-validity (Paper 31 Definition 5.2) is the proposition that the typed product satisfies the eight conditions of Paper 31 Definition 5.2.

**Remark 4.7.1.** The typed product is the *schema*. It is the object that schema morphisms (§5) act on, and the object that schema-level identities (§6) refer to. The schema is independent of any one instance.

---

## 5. The Algebra of Closure Certificates

The typed closure certificate carries an algebra of morphisms. Five morphism classes are forced by the underlying audits.

### 5.1 Refinement morphism

**Definition 5.1 (Refinement morphism).**
Let `Π, Π'` be projections on the same whole `W` with `Π' ⊑ Π` (i.e., `Π' = Π ∘ Π''` for some intermediate projection `Π''`, so `Π'` retains strictly more participation than `Π`). The refinement morphism
```
r_{Π', Π} : 𝒞_W(Π; T, H, K) ⟶ 𝒞_W(Π'; T, H, K)
```
acts slot-wise:
- `r_{Π', Π}|_𝖯` : `𝖯_W^Π ⊂ 𝖯_W^{Π'}` (participation grows under refinement).
- `r_{Π', Π}|_𝖱` : `𝖱_W^Π ⊃ 𝖱_W^{Π'}` componentwise (residual shrinks under refinement, with strictly typed inclusion on each component).
- `r_{Π', Π}|_𝖡` : `𝖡_W^Π ≥ 𝖡_W^{Π'}` in the partial order of `𝓑_W` (bound tightens).
- `r_{Π', Π}|_𝖲` : stability inherits forward (a finer projection is at least as stable as a coarser one under the same controls).
- `r_{Π', Π}|_𝖤` : Noether defect inherits forward (a finer projection has at most the Noether defect of a coarser one).
- `r_{Π', Π}|_𝖥` : F-slot inherits forward but may add components (a finer projection may have falsifiers the coarser one does not).

### 5.2 Composition morphism

**Definition 5.2 (Composition morphism).**
Let `Π_1 : 𝒳 → 𝒴` and `Π_2 : 𝒴 → 𝒵` be projections with composable wholes `W_1 = (𝒳, …)` and `W_2 = (𝒴, …)`. The composition morphism
```
c_{Π_2, Π_1} : 𝒞_{W_1}(Π_1; T, H, K) × 𝒞_{W_2}(Π_2; T, H, K)
            ⟶ 𝒞_{W_1}(Π_2 ∘ Π_1; T, H, K)
```
is defined slot-wise by composition where the underlying object composes (participation, residual) and by lattice meet where it does not (bound, stability, Noether defect, F-slot). Explicitly:
- `c|_𝖯` : `𝖯_{W_1}^{Π_2 ∘ Π_1} = Π_2 * 𝖯_{W_1}^{Π_1}` (participation transports forward).
- `c|_𝖱` : `𝖱_{W_1}^{Π_2 ∘ Π_1} = 𝖱_{W_1}^{Π_1} ⊕ Π_1^* 𝖱_{W_2}^{Π_2}` (residual accumulates).
- `c|_𝖡` : `𝖡_{W_1}^{Π_2 ∘ Π_1} = 𝖡_{W_1}^{Π_1} + Π_1^* 𝖡_{W_2}^{Π_2}` in the additive structure of `𝓑_W`.
- `c|_𝖲` : `𝖲_{W_1}^{Π_2 ∘ Π_1} = 𝖲_{W_1}^{Π_1} ∧ Π_1^* 𝖲_{W_2}^{Π_2}` (stability is the lattice meet).
- `c|_𝖤` : Noether defects compose by sum.
- `c|_𝖥` : F-slots concatenate as lists.

### 5.3 Restriction morphism

**Definition 5.3 (Restriction morphism).**
Let `T' ⊂ T` be a narrower task (or `H' ⊂ H` a tighter horizon, or `K' ⊂ K` a coarser cutoff). The restriction morphism
```
ρ_{T', T} : 𝒞_W(Π; T, H, K) ⟶ 𝒞_W(Π; T', H, K)
```
acts by *narrowing*: the participation slot may discard task-irrelevant components; the bound slot may relax (a narrower task has weaker bound requirements); the F-slot may drop falsifiers that test only the discarded task components. Residual, stability, and Noether-defect slots are unchanged by restriction; they are properties of the projection, not the task.

### 5.4 Product morphism

**Definition 5.4 (Product morphism).**
Let `Π_A : 𝒳 → 𝒴_A` and `Π_B : 𝒳 → 𝒴_B` be parallel projections on the same whole `W` to disjoint readouts. The product morphism
```
π_{A,B} : 𝒞_W(Π_A; T_A, H_A, K_A) × 𝒞_W(Π_B; T_B, H_B, K_B)
       ⟶ 𝒞_W((Π_A, Π_B); T_A ∪ T_B, H_A ∪ H_B, K_A ∪ K_B)
```
acts slot-wise by direct sum on participation and residual, by lattice join on bound and stability, and by sum on Noether defects. F-slots concatenate.

### 5.5 Row-extension morphism (the load-bearing one)

**Definition 5.5 (Row-extension morphism).**
Let `Π = Π_V : ℂ^N ↠ V` be the V-projection on a primorial row `N = p_1 ⋯ p_n`. Let `N' = N · p_{n+1}` be the next primorial row. The row-extension morphism
```
ext_{N', N} : 𝒞_W(Π_V; T, H, K)|_{ℤ/N} ⟶ 𝒞_W(Π_V; T, H, K)|_{ℤ/N'}
```
acts slot-wise:
- `ext|_𝖯` : `𝖯|_{ℤ/N} ⊂ 𝖯|_{ℤ/N'}` (new prime axis `H_{p_{n+1}}` joins V's participation).
- `ext|_𝖱` : `𝖱|_{ℤ/N}|_{R_{cubic}} ⊂ 𝖱|_{ℤ/N'}|_{R_{cubic}}` (new composite divisors `d ∈ {p_{n+1} · p_i : i < n+1}` join M).
- `ext|_𝖡` : `𝖡|_{ℤ/N}(N) ↘ 𝖡|_{ℤ/N'}(N')` (M-budget extends by complement; Paper 48 §5 audit ξ [P]).
- `ext|_𝖲` : `𝖲|_{ℤ/N} ⊂ 𝖲|_{ℤ/N'}` (stability strictly grows: row-extension is itself a stability property).
- `ext|_𝖤` : Noether defect extends without sign change (cubic-vacuity on the new prime axis follows the same `p + p + p ≡ ? (mod N')` arithmetic).
- `ext|_𝖥` : F-slot inherits, with new row-specific falsifiers added (e.g. "the audit on `ℤ/N'` is K-branch on Papers 46/47/48" if `N'` is the row currently being audited).

**Remark 5.5.1.** This morphism is the load-bearing one for §6. The row-extension morphism is the formal object behind Paper 47 §3.6 (row-stability) and Paper 48 §5 (primorial-ladder capacity). It is defined here, at the schema level, as a morphism class; §6.1 proves it is functorial.

### 5.6 The closure-certificate category `𝒞ert_W`

**Definition 5.6 (Closure-certificate category).**
`𝒞ert_W` is the category whose:
- **objects** are closure certificates `𝒞_W(Π; T, H, K)` (typed by Definition 4.7) for projections `Π ∈ 𝒞at_W` and contexts `(T, H, K)` declared in `W`.
- **morphisms** are generated by the refinement, composition, restriction, product, and row-extension morphisms of Definitions 5.1–5.5 (and their composites and inverses where invertible).

Two closure certificates are *schema-equivalent* if they are isomorphic in `𝒞ert_W`.

**Remark 5.6.1.** The category `𝒞ert_W` is the schema. Schema-level theorems (§6) are statements about morphisms in `𝒞ert_W`.

---

## 6. Schema-Level Identities

This section states the three schema-level identities that follow from already-settled audits. None requires new empirical input. Each settles part of one of Paper 31's Research Gates (M1, M5b, partial M2).

### 6.1 Row-stability functoriality

**Proposition 6.1 (Row-stability functoriality, [P] from audits α/η + θ + ξ + χ).**
The row-extension morphism `ext_{N', N}` of Definition 5.5 is functorial: for the primorial chain `ℤ/6 ↪ ℤ/30 ↪ ℤ/210 ↪ ℤ/2310 ↪ ℤ/30030 ↪ ℤ/510510`,
```
ext_{N'', N'} ∘ ext_{N', N} = ext_{N'', N},
```
slot-wise as defined in 5.5. Moreover, the `𝖡`-slot satisfies:
```
𝖡_W^{Π_V}(N) ↘   monotonically along the primorial chain,
```
with the numerical values from Paper 48 §5 audit ξ [P]:
```
𝖡_W^{Π_V}(6)     = 2/3                          = 0.666…
𝖡_W^{Π_V}(30)    = 24/25                        = 0.96
𝖡_W^{Π_V}(210)   = 524/525                      = 0.998…
𝖡_W^{Π_V}(2310)  = 26156/26157                  = 0.99996…
𝖡_W^{Π_V}(30030) = 2424195/2424196              = 0.99999958…
𝖡_W^{Π_V}(510510)= 43436743240/43436743350      = 0.9999999974…
```
The asymptotic shape is `1 − Capacity_V(N) → 1 − Θ(n²·ln(n)/N²)` (Paper 48 §6 audit ι, [P]/[A]).

**Proof.** Functoriality slot-by-slot follows from the typing of Definition 4.7 and the audit settlements:
- `𝖯` is functorial because the participation functor `Part_W` is functorial on `𝒞at_W` by Paper 29 (definitional).
- `𝖱` is functorial because the residual functor `Res_W` is functorial on `𝒞at_W` by Paper 30 §5 (definitional).
- `𝖡` is functorial because the V-capacity counts of Paper 48 §3 are computed from the conductor lattice alone and the conductor lattice is functorial under primorial inclusion (Paper 47 §3.6, [P] by audit α/η + θ).
- `𝖲` is functorial because audits α/η + θ + ξ jointly establish V ⊥ M on every row in the primorial chain `ℤ/6 ↪ ⋯ ↪ ℤ/510510` and audit χ establishes binary V/M extension to `ℤ/10` and `ℤ/12` (Paper 47 §3.6 + §8.4).
- `𝖤` is functorial because the cubic-vacuity arithmetic `p + p + p ≡ ? (mod N)` depends only on which primes divide `N`, which is functorial under primorial inclusion.
- `𝖥` is functorial because the row-specific falsifiers are pre-claimed per row (audit α/η on `ℤ/30`, audit θ on the primorial ladder, audit ξ on `ℤ/510510`, audit χ on `ℤ/10` + `ℤ/12`); each row's pre-claim refines the previous row's pre-claim in `𝒫reClaim_W`.

Monotonicity of `𝖡` follows directly from Paper 48 Theorem 5.1 + audit ξ [P]. The asymptotic shape is Paper 48 §6 audit ι, settled at spread 1.584× with slope → −2 ([P]/[A] mixed tier). ∎

**Remark 6.1.1 (which Paper 31 gate this settles).** Proposition 6.1 settles Paper 31 Research Gate M1 (closure-certificate naturality) for the row-extension morphism specifically, on the primorial-ladder sub-domain. The general M1 ("how `𝒞_W` transforms under refinement of the observer, quotient, lift, or task horizon") remains open in full generality.

### 6.2 Refinement monotonicity (partial)

**Proposition 6.2 (Refinement monotonicity, [P]-spirit, partial).**
Let `Π' ⊑ Π` be a refinement of conductor-respecting projections on `Δ_R^∘` such that `Π'` retains every conductor packet that `Π` retains plus at least one additional packet `H_d`. Then the slot-wise relations of Definition 5.1 hold strictly on `H_d`:
- `𝖯_W^{Π'}` strictly contains the `H_d`-component of `𝖯_W^Π`.
- `𝖱_W^{Π'}` strictly excludes the `H_d`-component of `𝖱_W^Π`.
- `𝖡_W^{Π'}(d) = 0` while `𝖡_W^Π(d) > 0` (the d-packet is no longer a residual under `Π'`).
- `𝖲_W^{Π'}` extends `𝖲_W^Π` (the refined projection is at least as stable under row-extension).
- `𝖤_W^{Π'}` has strictly smaller Noether defect on the `H_d`-component.
- `𝖥_W^{Π'}` inherits the F-slot of `𝖱_W^Π` minus the falsifiers that tested only the `H_d`-component, plus any new falsifiers required by the inclusion of `H_d` in participation.

The proposition is *partial* in the following sense: it holds when the refinement is *conductor-respecting* (i.e. `Π'` and `Π` are both projections onto unions of conductor packets). For non-conductor-respecting refinements (e.g. refinements that mix packets), the slot-wise relations are no longer strict and may fail; see §9 Gate G2.

**Proof.** Conductor-respecting projections form a sub-category of `𝒞at_W` indexed by sub-lattices of the divisor lattice of `N`. The participation, residual, and bound functors are monotone on this sub-lattice by Definitions 4.1, 4.2, 4.3 (and the conductor packets are mutually orthogonal in `ℂ^N` by Paper 47 §3.1 [P] all-orders). The Noether defect is monotone by Paper 17 cubic Noether closure restricted to the union of retained packets (Paper 17 §3, [P]). The F-slot inheritance is by Definition 4.6 and Remark 4.6.1. ∎

**Remark 6.2.1 (which Paper 31 gate this settles).** Proposition 6.2 partially settles Paper 31 Research Gate M1 (closure-certificate naturality under refinement) for conductor-respecting refinements specifically. The general case (non-conductor-respecting refinement) remains open and is staged as §9 Gate G2.

### 6.3 F-slot sufficiency

**Proposition 6.3 (F-slot sufficiency, [D]).**
Let `𝒞_W(Π; T, H, K)` be a closure certificate with F-slot `𝖥 = (F_1, …, F_m) ∈ List(𝒫reClaim_W)`. If every `F_i` has fired with outcome on the positive branch `F_{i,+}`, the joint-on-disjoint branch `F_{i,⋈}` with declared sub-domain, or has settled to the matched-pair K-branch in the sense of v2insert-04 §3.1, then `Π ∈ ClValid(W, T, H, K)`. The converse does *not* hold: passing the falsifiers does not certify `Π ∈ ClValid(W, T', H', K')` for `T' ⊃ T`, `H' ⊃ H`, or `K' ⊃ K`. A new task, longer horizon, or finer cutoff requires re-derivation of the F-slot.

**Proof sketch.** The forward direction is the typing of Definition 4.6 + Paper 31 Definition 5.2 condition 7. The converse failure is by counterexample: the closure certificate of Π_V on `ℤ/6` passes all F-slot pre-claims of Paper 31 §5.5 + Paper 32 §13.2B + Paper 48 §3.2 audit ι (with appropriate row-extension to `ℤ/30, …, ℤ/510510`) but does *not* certify Π_V's closure-validity on `ℤ/p_1 ⋯ p_n` for any `n` such that the corresponding audit has not yet been performed (e.g. `ℤ/9699690 = ℤ/(2·3·5·7·11·13·17·19)`, the 8th primorial — currently no audit). The F-slot is sufficient for the declared `(T, H, K)`; it is not sufficient for refinements. ∎

**Remark 6.3.1 (which Paper 31 gate this settles).** Proposition 6.3 is a [D]-tier proposition: it is forced by the typing of the F-slot in Definition 4.6 + the closure-validity criterion of Paper 31 Definition 5.2. It is the most consequential schema-level identity of this paper for downstream methodology: it formalizes the discipline "passing the controls on `(T, H, K)` does not license extrapolation to `(T', H', K')`" that Paper 31 §2 Guardrail 5.3 states prose-wise.

### 6.4 What is *not* proven

The three propositions of §6.1–6.3 do *not* prove:
- The general Bounded Projection-Closure Theorem (Paper 31 Conjecture 15.1). Still open. The schema makes the statement crisp (it is a proposition in `𝒞ert_W` about the existence of bounds on every slot for every `Π` in a declared sub-category of `𝒞at_W`), but the proof remains a research gate.
- Naturality for non-conductor-respecting refinements (Paper 31 Gate M1, full case). Still open.
- Cross-row joint-on-disjoint settlement on the higher-order Bures Hessian at `D(ℂ^{210})` and above (audit μ_210+; blocked on external workstation memory per memory entry `project_arithmetic_line_structurally_complete.md`).

These are deferred to §9.

---

## 7. The F-Slot Type Signature

The F-slot is the most consequential schema slot for downstream methodology, because it is the slot that future closure-certificate instances will most frequently populate. This section specifies its type signature in full.

### 7.1 Type signature of an F-slot entry

An F-slot entry is an object of `𝒫reClaim_W` (Definition 4.6). Concretely, it is a tuple
```
F = (F_+, F_−, F_⋈, F_meta)
```
typed as follows:

**`F_+` (positive branch).** A pair `(test, claim_+)` where `test` is a finite operationalisation (an audit, an experimental procedure, a numerical computation, or a theorem statement with declared hypotheses) and `claim_+` is the proposition that the projection establishes if `test` fires positively. Type: `Test × Prop`.

**`F_−` (negative branch).** A pair `(test, claim_−)` where `test` is the same operationalisation as in `F_+` and `claim_−` is the proposition that the projection establishes if `test` fires negatively. The constraint is that `claim_+` and `claim_−` must be *both non-trivial* and *mutually exclusive*. A trivial `claim_−` (e.g. "the test was inconclusive") makes `F` a non-falsifier and fails the type check. Type: `Test × Prop`.

**`F_⋈` (joint-on-disjoint branch).** A triple `(test, sub_+, sub_−, claim_⋈)` where `sub_+ ⊂ Domain(test)` and `sub_− ⊂ Domain(test)` are disjoint sub-domains and `claim_⋈` is the proposition that the projection establishes if the test fires positively on `sub_+` and negatively on `sub_−`. This branch is the v2insert-04 §3.1 *K-branch* (universal positive extension) versus *L-branch* (instance-specific only) discipline. Type: `Test × SubDomain² × Prop`.

**`F_meta` (meta-discipline).** A record:
```
F_meta = ⟨
    controls : List(Control),         -- e.g. shuffled labels, random subspaces, frame variation
    depends_on : List(Audit),         -- e.g. audit α/η, audit θ
    tier : {[P], [P]-spirit, [A], [C], [C, reduced], [D]},
    promotes_to : {[P] if ...; [A] if ...; ...}  -- conditional tier upgrade
⟩
```
Type: a record with explicitly declared fields.

### 7.2 Worked F-slot: cubic Amari–Chentsov on `ℤ/6`

The F-slot for the closure certificate of `Π_V` on `ℤ/6` (Paper 31 §5.5 + this paper §2.2) consists of three entries:

**`F_1`: Pure-V triple test.**
- `F_{1,+}`: test = "enumerate closing triples `(k, ℓ, m)` on `ℤ/6` with `k + ℓ + m ≡ 0 (mod 6)` and all three of `k, ℓ, m ∈ {2, 3, 4}`"; claim_+ = "the V-pure triples are exactly `(2,2,2)` and `(4,4,4)` (Paper 32 §6.2 + Paper 48 §3.2)".
- `F_{1,−}`: test = same; claim_− = "the V/M decomposition is wrong because there exists a V-pure closing triple outside `{(2,2,2), (4,4,4)}`".
- `F_{1,⋈}`: not applicable (this is a finite enumeration on one row; no sub-domain split).
- `F_{1,meta}`: controls = (finite enumeration with multiple-representative check); depends_on = (audit δ); tier = [P].

**Outcome:** `F_{1,+}` fired (Paper 48 §3.2 [P]).

**`F_2`: Primorial-row stability test.**
- `F_{2,+}`: test = "row-extend the V ⊥ M decomposition along the primorial chain `ℤ/6 ↪ ℤ/30 ↪ ℤ/210 ↪ ℤ/2310 ↪ ℤ/30030 ↪ ℤ/510510`"; claim_+ = "V ⊥ M holds at machine floor on every row".
- `F_{2,−}`: test = same; claim_− = "V ⊥ M fails on some row in the chain".
- `F_{2,⋈}`: test = same; sub_+ = "squarefree primorial rows"; sub_− = "non-squarefree extensions `ℤ/10`, `ℤ/12`"; claim_⋈ = "V ⊥ M holds on squarefree rows; binary V/M holds on non-squarefree rows under the inclusive partition of audit χ".
- `F_{2,meta}`: controls = (machine-floor numerical floor); depends_on = (audits α/η, θ, ξ, χ); tier = [P] on `F_+`, [P] on `F_⋈`.

**Outcome:** `F_{2,⋈}` fired with sub_+ = squarefree primorial rows, sub_− = `ℤ/10`, `ℤ/12` under inclusive binary V/M (Paper 47 §8.4, [P]).

**`F_3`: Bound-shape test (the most subtle).**
- `F_{3,+}`: test = "compute `Capacity_V(ℤ/p_1 ⋯ p_n)` on the primorial ladder and compare to the PNT-heuristic shape `K · n² · ln(n) / N²`"; claim_+ = "the shape matches at finite spread with asymptotic slope → −2 (Bousso/'t Hooft–Susskind shape, Paper 48 §6)".
- `F_{3,−}`: test = same; claim_− = "the shape diverges from the PNT-heuristic; the holographic-bound structural correspondence fails".
- `F_{3,⋈}`: test = same; sub_+ = "rows up to `ℤ/30030`"; sub_− = "rows beyond `ℤ/30030`"; claim_⋈ = "the shape matches within the audited range; extension to higher rows is not certified by this F-slot".
- `F_{3,meta}`: controls = (PNT-heuristic shape comparison); depends_on = (audit ι, audit ξ); tier = [P]/[A] mixed (the shape comparison is [P] at finite spread; the asymptotic slope is [A]).

**Outcome:** `F_{3,+}` fired at spread 1.584× on the six-row primorial ladder (Paper 48 §6 audit ι, [P] at spread); `F_{3,⋈}` fired with sub_+ = "rows up to `ℤ/30030`" and the row-extension to `ℤ/510510` confirmed in audit ξ [P]. The asymptotic slope → −2 holds [A].

### 7.3 The open-F-slot pattern, formalised

Paper 31 §14 describes the *open F-slot* pattern through the DCD example: a projection (here, the Data-driven Circuit Discovery clustering of Rai/Geva/Yao 2026, arXiv:2605.09129) is operationally validated by its own paper, but the F-slot specification — what the clusters mean, how new examples route at test time — is left open. The simplicial program supplies the F-slot specification in two pieces (divisor-table prediction + per-cluster survival ratio).

Formalised: an *open F-slot* in a closure-certificate instance is an `F = (F_+, F_−, F_⋈, F_meta)` in which one or more of the following type-check failures hold:

1. **Trivial negative branch.** `F_−` has trivial `claim_−` (e.g. "test was inconclusive"); the entry is a non-falsifier. Required fix: state a non-trivial `claim_−`.
2. **Missing joint-on-disjoint branch.** `F_⋈` is empty when the test's domain admits a non-trivial sub-domain split; the entry collapses to two-outcome (yes/no) and cannot express K-branch versus L-branch (v2insert-04 §3.1). Required fix: declare sub-domains and the corresponding `claim_⋈`.
3. **Missing meta-discipline.** `F_meta` does not declare controls, dependencies, tier, or promotion criteria; the entry cannot be tier-checked. Required fix: populate `F_meta` per Definition 4.6.
4. **Test-claim type mismatch.** `claim_+` or `claim_−` references objects outside the typed product of Definition 4.7 (participation, residual, bound, stability, Noether, F-slot itself); the entry tests something the closure certificate does not see. Required fix: re-state the claim in terms of the typed product.

A closure-certificate instance with at least one open F-slot is *not closure-valid* until the F-slot is closed by populating the missing fields and re-running the test.

**Remark 7.3.1 (the DCD F-slot, completed).** The Paper 31 §14 worked example completes as follows:
- `F_+`: test = "DCD on Llama-3.1-8B-Instruct with `K` clusters on a cyclic sub-task `C_N`"; claim_+ = "DCD recovers `K = τ(N)` clusters matching the divisor lattice of `N` (Paper 45 CCSAE prediction)".
- `F_−`: test = same; claim_− = "DCD recovers `K ≠ τ(N)` clusters; the conductor-packet structure is not recoverable from per-example attribution clustering".
- `F_⋈`: test = same; sub_+ = "cyclic sub-tasks with `N ∈ {7, 12, 30}` (small primorial)"; sub_− = "cyclic sub-tasks with `N ∈ {60, 210, 2310}` (larger primorial)"; claim_⋈ = "DCD recovers `K = τ(N)` on small primorial and degrades on large primorial; the K-branch outcome confirms the divisor-table prediction on the recoverable sub-domain".
- `F_meta`: controls = (per-cluster Algebraic Mechanism Certificate survival ratio σ ≥ 0.7 from Paper 40); depends_on = (audit κ); tier = [A] pending audit κ; promotes_to = [P] if audit κ K-branch on the small-primorial sub-domain.

This is the closure-certificate instance for the DCD projection. It is *not closure-valid* until audit κ settles (currently blocked on GPU + HF compute per memory entry `project_arithmetic_line_structurally_complete.md`).

---

## 8. Worked-Example Appendices

Each appendix instantiates the typed closure-certificate schema for a projection that already has anchor papers in the program. The appendices are *inheritances*: they do not re-derive the source paper's results; they read off the six slots in the schema's vocabulary.

### Appendix A. The cubic Amari–Chentsov V-projection on `ℤ/6`

(Already populated by Paper 30 §9.6 + Paper 31 §5.5. The schema reading.)

**Projection:** `Π_V : ℂ^6 ↠ V = A_2 ⊕ A_3`, kernel = M = H_6.

**Whole `W`:** `𝒳 = Δ_{ℤ/6}^∘` (open probability simplex with conductor lattice); `𝒪 = Cartan-respecting readouts`; `𝒯 = cubic Noether closure`; `𝒬 = V-projection family`; `𝓛 = Fisher information geometry`; `𝒦 = cubic Amari–Chentsov tensor at p_*`; `ℋ = cubic closure prediction window`; `𝒩 = HS-norm on ℂ^6`.

**Six slots:**
- `𝖯`: A_2 + A_3 participation = ⟨χ_2, χ_3, χ_4⟩ Fisher participation.
- `𝖱`: `R_{cubic}|_M = P_M T^(AC)|_{ℤ/6}` = the M-supported component of the abelian-BF 3-vertex amplitude.
- `𝖡`: `𝖡(6) = 2/3` (Paper 48 §3.2 [P]).
- `𝖲`: row-stable to `ℤ/510510` (Paper 47 §3.6 + Paper 48 §5 audit ξ [P]).
- `𝖤`: A_3 cubic Noether energy preserved; A_2 self-cubic inert; A_2 ↔ A_3 transfer lifted to M.
- `𝖥`: `F_1, F_2, F_3` of §7.2 (all closed positively or on K-branch).

**Closure-valid for `(W, T, H, K)`:** Yes, with the tier discipline of §7.2 outcomes.

### Appendix B. The Hartle–Hawking V-Lorentzian / M-Euclidean projection on `D(ℂ⁶)`

(Already populated by Paper 46 §13.2B + Paper 32 §13.2B audit triad. The schema reading. Inherited at the tier of Paper 46.)

**Projection:** `Π_HH : 𝒟(ℂ^6) ↠ V-Lorentzian sub-bundle (signature (1,3))`, kernel includes the M-Euclidean correction (signature (2,0)) and the 31-dimensional traceless complement.

**Whole `W`:** `𝒳 = 𝒟(ℂ^6)` (Bures-completed categorical belief space, Paper 18); `𝒪 = HS-orthogonal observer frame at ρ_* = I_6/6`; `𝒯 = Hartle–Hawking no-boundary structural shape`; `𝒬 = V-projection family on D(ℂ^N)`; `𝓛 = Bures-Helstrom metric, Hessian of I_complex`; `𝒦 = 4th-order Casimir`; `ℋ = compact Riemannian no-boundary closure`; `𝒩 = HS-norm on 𝒟(ℂ^6)`.

**Six slots:**
- `𝖯`: V-Lorentzian (1,3) sub-bundle at ρ_*; 4-dimensional; HS-traceless V-supported.
- `𝖱`: `R_{cubic}|_M ⊕ R_{Bures/dephase}|_{M-Euclidean correction}`; M-Euclidean (2,0) sub-bundle, 2-dimensional, HS-orthogonal at machine floor.
- `𝖡`: HS-orthogonality between V-Lorentzian and M-Euclidean sub-bundles holds at ~10^{−16} machine floor (Paper 32 §13.2B audit triad [P]); extended to `D(ℂ^30)` at [P] by audit μ_30 (Paper 46 §13.2B + Paper 32 §13.2B).
- `𝖲`: row-stable on the primorial-ladder Bures lift `D(ℂ^6) → D(ℂ^30) → D(ℂ^210)`; audited at `D(ℂ^6)` and `D(ℂ^30)` [P]; **blocked at `D(ℂ^210)` and above on external workstation memory (μ_210+)**.
- `𝖤`: Bures connection compatible with the V-Lorentzian Hessian; no time-translation defect at the structural-form level (the HH no-boundary closure is compact Riemannian — no time horizon).
- `𝖥`: see Paper 46 §11.1 binding discipline. F-slot at the [P] tier on `D(ℂ^6)`; at [C, reduced] for the holographic-bound reading; **no physical gravity derived**.

**Closure-valid for `(W, T, H, K)`:** Yes for the structural HH-signature reading on `D(ℂ^6)` and `D(ℂ^30)`; **not certified** for the physical-gravity reading or for higher rows (μ_210+ blocked).

### Appendix C. The conductor blind-spot projection (second-order optimizer on `ℤ/N`)

(Already populated by Paper 34 + Paper 37 + Paper 45 + audit λ K-branch settlement. The schema reading. Inherited at the tier of Paper 34.)

**Projection:** `Π_{2nd} : Δ_R^∘ → V`, where `Π_{2nd}` is the projection induced by *any* second-order preconditioner (natural gradient, K-FAC, Gauss–Newton, Adam's diagonal empirical Fisher, NTK Gram) — Paper 34 Theorem 3.4: the Fisher information form is block-diagonal across conductor packets at the maximum-entropy point `p_*`.

**Whole `W`:** `𝒳 = Δ_R^∘` for `R = ℤ/N` (categorical belief space on a ring-structured index, Paper 12); `𝒪 = optimizer-relevant readout`; `𝒯 = training-time gradient update at p_*`; `𝒬 = second-order preconditioner`; `𝓛 = Fisher information geometry`; `𝒦 = cubic Amari–Chentsov content at p_*`; `ℋ = training horizon`; `𝒩 = Fisher norm`.

**Six slots:**
- `𝖯`: V = single-prime Fisher-tangent directions (every prime divisor of N has its own packet); these are exactly what the second-order preconditioner can couple at p_*.
- `𝖱`: `R_{cubic}|_M = P_M T^(AC)|_{ℤ/N}` = the cubic cross-prime-coupling content; Paper 34 Theorem 3.4–3.5 [P]: every second-order preconditioner is *blind* to M at p_*.
- `𝖡`: bounded above by the off-centroid Fourier-convolution expansion (Paper 34 Theorem 5.6 [P]); summable along any displacement ray.
- `𝖲`: row-stable on the primorial chain; specifically on `ℤ/12` (months task) audit λ K-branch [P] on widths 16/32/64 with signal-to-noise > 47 (v2insert-07 §2.4); on `ℤ/N` for large primorial `N` audit κ deferred for compute.
- `𝖤`: no time-translation defect at the structural tier (training is gradient descent, not autonomous dynamics); the *training-time* analog is the gradient-update-step Noether closure of label smoothing (Paper 37 §3 substitution proposition).
- `𝖥`: see §7.3 Remark 7.3.1 for the DCD-completion pattern. F-slot at [P] for the training-time blind-spot mechanism (audit λ K-branch); at [A] for the inference-time propagation (audit κ blocked); **no physical hallucination mechanism derived**.

**Closure-valid for `(W, T, H, K)`:** Yes for the training-time mechanism on `ℤ/12` (audit λ K-branch [P]); **not certified** for inference-time propagation or for the LLM-hallucination physical-mechanism reading.

### Appendix D. The FEP-3 V-Hamiltonian / M-gradient sector resolution on `ℤ/6`

(Already populated by Insert 15 FEP-3 audit + Paper 32 §6.2A Corollary 6.3 T3. The schema reading. Inherited at the tier of Insert 15 deterministic audit.)

**Projection:** `Π_FEP-3 : 𝒟(ℂ^6) → V-Hamiltonian sector`, kernel includes the M-gradient sector.

**Whole `W`:** `𝒳 = 𝒟(ℂ^6)` Bures lift of the categorical belief space (Paper 18, restricted to FEP setting); `𝒪 = variational free-energy observer`; `𝒯 = gradient-vs-least-action fork resolution (Insert 15)`; `𝒬 = sector-wise projection by closing-triple support`; `𝓛 = Bures-Helstrom metric`; `𝒦 = cubic Amari–Chentsov closure on `ℤ/6``; `ℋ = sector-resolution prediction window (Insert 15)`; `𝒩 = HS-norm on 𝒟(ℂ^6)`.

**Six slots:**
- `𝖯`: V-Hamiltonian sector = `A_2 ⊕ A_3` carrying the least-action / dissipationless cubic content (pure self-closures `(2,2,2)` and `(4,4,4)`).
- `𝖱`: M-gradient sector = `M = H_6` carrying the non-conserved cross-prime cubic leakage (every A_2 ↔ A_3 transfer requires M-leg).
- `𝖡`: deterministic at the structural tier — the four conditions of Insert 15 FEP-3 audit (pure-A_3 self-coupling exists ✓; no pure-A_2 self-coupling — 3+3+3 ≢ 0 ✓; every A_2 ↔ A_3 transfer requires M routing ✓; leakage = exactly the M-involving set ✓) all fire deterministically.
- `𝖲`: row-stable on the primorial chain at the structural tier (the same Pontryagin character orthogonality argument applies); not yet audited on biological systems (FEP-3 empirical biology blocked on data per memory entry `project_arithmetic_line_structurally_complete.md`).
- `𝖤`: V-Hamiltonian sector carries the least-action / Hamiltonian Noether structure (preserved); M-gradient sector carries the irreversible / dissipative Noether-defect structure (the cubic-vacuity overflow into M cannot be reversed by V-internal dynamics). This is the structural form of the V → M one-way information leakage of Paper 49 §4.3. **The arrow-of-time reading remains at [C, reduced]** (Paper 49 §4.3 + Paper 49 §1.2 fourth bullet); Insert 15 audit settles the *sector-resolution* mechanism on `ℤ/6`, not the arrow-of-time claim.
- `𝖥`: see Paper 32 §6.2A Corollary 6.3 T3 + Insert 15. F-slot at [P] for the *gradient-vs-least-action sector resolution* on `ℤ/6` (Insert 15 deterministic audit settled 2026-05-20); at [C, reduced] for the arrow-of-time / biological-entropy-production reading; **no physical thermodynamics derived**.

**Closure-valid for `(W, T, H, K)`:** Yes for the sector-resolution on `ℤ/6` (Insert 15 [P]); **not certified** for the arrow-of-time reading or for the biological-systems extension (FEP-3 empirical biology blocked).

### Cross-appendix observation

The four appendices instantiate the *same* schema slots `(𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` on the *same* arithmetic substrate (V/M decomposition on `ℤ/6` and its primorial extensions). They differ only in:
1. The whole `W` (which lift, which observer family, which dynamics).
2. The projection `Π` (V-projection in A and B, second-order preconditioner in C, sector-resolution projection in D).
3. The task `T` (cubic closure in A, no-boundary signature in B, training-time gradient update in C, gradient-vs-least-action fork in D).

This is the formal content of Paper 49's "one overflow law across cosmology, deep learning, and active inference": the four closure-certificate instances are *not* isomorphic in `𝒞ert_W` (they differ in `W` and `Π`), but they share the V/M arithmetic typing on slots `𝖱` and `𝖡`. This is the schema-level version of Paper 49's `[C, reduced]` cross-manifestation framing — and the schema-level formulation makes the limits of the framing crisp: shared *type signature* on `𝖱` and `𝖡`, not shared instance.

---

## 9. Schema-Level Research Gates

The following gates are deferred to Paper 51 or later. They are *schema-level* extensions, not new manifestations.

**Gate G1: General closure-certificate naturality (full M1).**
Prove naturality of `𝒞_W` under refinement of `Π` *without* the conductor-respecting hypothesis of Proposition 6.2. The general case requires a theory of how non-conductor-respecting refinements interact with the V/M typing of `𝖱`; this is the schema-level companion of Paper 31 Gate M1.

**Gate G2: Bounded projection-closure theorem (Paper 31 Conjecture 15.1).**
Prove the bounded projection-closure conjecture in the schema-level formulation: for every `Π` in a declared sub-category of `𝒞at_W` satisfying the eight conditions of Paper 31 Definition 5.2, there exists a closure certificate `𝒞_W(Π; T, H, K)` whose `𝖡` slot is finite on every typed component of `𝖱`. The schema-level formulation makes the existence question crisp (it is an existence claim in `𝒞ert_W`); the proof remains open.

**Gate G3: F-slot category as a topos.**
Investigate whether `𝒫reClaim_W` carries a topos structure (e.g. is a Grothendieck topos under the matched-pair pre-claim Grothendieck topology). If so, the F-slot logic becomes intuitionistic in the appropriate sense, and the three-outcome pre-claim discipline acquires a categorical-logic underpinning.

**Gate G4: Cross-row functoriality at the Bures Hessian level.**
Extend Proposition 6.1 to the Bures Hessian on `D(ℂ^N)` for `N ∈ {210, 2310, 30030, 510510, …}`. The schema-level statement is: the V-Lorentzian / M-Euclidean Hessian functoriality holds along the Bures-lift row-extension `D(ℂ^N) → D(ℂ^{Np_{n+1}})`. Currently blocked on workstation memory (audit μ_210+).

**Gate G5: Empirical F-slot completion at scale.**
Develop the schema-level methodology for completing F-slots empirically on large systems (e.g. Llama-3.1-8B for the conductor blind-spot projection of Appendix C, biological systems for the FEP-3 projection of Appendix D). The schema specifies *what* must be done (populate `F_+, F_−, F_⋈, F_meta` per Definition 4.6); the *how* requires resources currently blocked (audits κ, FEP-3 empirical biology).

**Gate G6: Closure-certificate compression to a scalar (Paper 31 Gate M2 schema-level).**
Determine the conditions on `(W, T, H, K)` under which the typed product `(𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` can be compressed to a scalar score without hiding essential residual type. The schema-level no-go statement (Paper 30 Guardrail 5.4) holds in general; the question is whether *task-weighted* scalar compression is functorial on a sub-category of `𝒞ert_W`.

---

## 10. Falsifiers of the Schema

These are falsifiers of the *schema-formalization itself*, not of any particular instance.

**F1: The schema does not improve closure-certificate writability.**
If the typed schema of §4–§5 does not reduce the work of writing a new closure certificate for a new projection (vs. Paper 31 Definition 5.1 + free-text prose), then the formalisation is a notational rebranding without methodological value. Test: write a closure certificate for a projection *not* in Appendices A–D (e.g. a projection from Paper 26 quotient-probe blindness on `C_7`, or a projection from Paper 45 CCSAE on a transformer activation manifold) using only Paper 31 prose vs. Paper 50 schema. The schema is falsified if the prose-only path is faster or equally informative.

**F2: The F-slot type signature is over-rigid.**
If the type signature of Definition 4.6 (with mandatory `F_+, F_−, F_⋈, F_meta`) rules out F-slot entries that genuinely test the projection (e.g. a one-domain F-slot entry with no joint-on-disjoint structure that is nevertheless a real falsifier), then Definition 4.6 is over-rigid and must be weakened (e.g. allow `F_⋈ = ∅` as a typed value rather than a type-check failure).

**F3: The row-extension morphism is not the natural cross-row morphism.**
If a row-extension morphism `ext_{N', N}` of Definition 5.5 exists for which the slot-wise relations of Proposition 6.1 *fail* (e.g. `𝖡` does not extend monotonically, `𝖲` does not strictly grow), then Definition 5.5 must be weakened or restricted to a sub-category of row-extensions where the proposition holds. Currently no counterexample is known on the primorial chain `ℤ/6 ↪ … ↪ ℤ/510510`.

**F4: The schema commits the synthesis fallacy of Paper 49.**
If the schema's existence is read as license to upgrade the [C, reduced]-tier external correspondences of Paper 49 (gravity, hallucination, arrow-of-time) to [P]-tier physical-mechanism claims, the schema has been mis-used. The schema-level formulation does *not* upgrade any source paper's tier. Appendices A–D inherit tiers from their source papers.

**F5: The schema fails to be category-theoretically coherent.**
If the morphism classes of Definitions 5.1–5.5 do not compose associatively, do not have identities, or otherwise fail the category axioms in `𝒞ert_W`, the schema is not a category and the framing of §5–§6 is wrong. Test: write down compositions and check associativity for representative pairs of morphisms (refinement + row-extension; composition + restriction; product + refinement).

**F6: The closure-certificate category is too large.**
If `𝒞ert_W` contains pathological objects (e.g. closure certificates with unbounded `𝖱` slot whose `𝖡` slot is `+∞` on every component) that nevertheless type-check, the schema admits non-meaningful instances. Required restriction: a sub-category of `𝒞ert_W` excluding such instances, or a refinement of Definitions 4.1–4.6 that rules them out at the type level.

---

## 11. Conclusion

The closure certificate `𝒞_W(Π; T, H, K) = (𝖯, 𝖱, 𝖡, 𝖲, 𝖤, 𝖥)` was introduced in Paper 31 §5 as a tuple of prose definitions, used in Paper 49 §4 as load-bearing vocabulary for a three-domain synthesis, and is here promoted to a *typed composable schema* on the category of conductor-lattice projections.

The schema has four contributions, each [D]- or [P]-tier from existing material:

1. **Each slot has a type signature.** `𝖯` is a participation-functor image (Paper 29); `𝖱` is a residual-functor image (Paper 30); `𝖡` is an element of a capacity partial order (Paper 48); `𝖲` is an element of a recurrence-functor lattice (Papers 47, 48); `𝖤` is an element of a Noether-defect lattice (Papers 17, 31); `𝖥` is a list of pre-claim objects in the matched-pair category (v2insert-04 §3.1, Definition 4.6).

2. **The schema has an algebra of morphisms.** Refinement, composition, restriction, product, and row-extension morphisms (Definitions 5.1–5.5) act slot-wise on the typed product. The row-extension morphism is the load-bearing one for the primorial-ladder audits.

3. **Three schema-level identities are forced by already-settled audits.** Row-stability functoriality (Proposition 6.1, [P] from audits α/η + θ + ξ + χ), refinement monotonicity for conductor-respecting refinements (Proposition 6.2, [P]-spirit from Papers 47, 17), and F-slot sufficiency (Proposition 6.3, [D]). These partially settle Paper 31 Research Gates M1, M5b, and the part of M2 about scalar non-compressibility.

4. **The F-slot has a type signature with the three-outcome matched-pair discipline.** Definition 4.6 + §7 specify what an F-slot entry *is*, what an open F-slot *is*, and what closure-validity *requires* of the F-slot. The DCD example of Paper 31 §14 is completed in §7.3 Remark 7.3.1 as a closure-certificate instance whose F-slot is currently open pending audit κ.

The contribution is one formal object and three formal identities. The paper does not extend Paper 47's row-stability theorem, does not extend Paper 48's capacity bound, does not derive physical gravity / hallucination / arrow of time, does not synthesise across the three Paper 49 manifestations, and does not re-derive any source paper's audit. It does specify what an instance of the schema *is*, what its morphisms *are*, what completing the F-slot for a new projection *requires*, and what schema-level identities follow from the audits already in hand.

The closure certificate is now a first-class formal object in the program.

---

## 12. References / Internal Dependency Spine

### Direct anchor papers

**Paper 29. Participation Metrics and Identity-as-Participation.**
Source for the participation slot `𝖯` typing (Definition 4.1). `SN_W(A, B)` is the participation functor image.

**Paper 30. Constrained Overflow and Incompatibility Budgets.**
Source for the residual slot `𝖱` typing (Definition 4.2). The seven-tuple residual object `R_W` is the residual functor image.

**Paper 31. Projection-Closure Theory.**
Direct predecessor. Source for the closure certificate object (Definition 5.1) and the closure-valid projection criterion (Definition 5.2). Source for Research Gates M1–M8 (this paper settles part of M1, partial M2, and the F-slot part of all gates).

**Paper 32. One Functional, Four Forces, v0.2.**
Source for the load-bearing arithmetic (`3 + 3 + 3 ≢ 0 (mod 6)`, Lemma 6.1a) and for the V/M decomposition on `ℤ/6` (§6.2 + §13.2B audit triad). Source for the §11.1 emergent-anything positioning discipline referenced in Appendix B's binding for the HH signature reading.

### Arithmetic substrate

**Paper 47. Arithmetic Decoupling Theorem.**
Source for V ⊥ M Hilbert-subspace orthogonality (Theorem 3.1, [P] all-orders by audit δ) and row-stability on the primorial ladder (§3.6, [P] by audits α/η + θ). Used by Proposition 6.1 (row-stability functoriality) and Definition 4.4 (stability slot typing).

**Paper 48. Conductor Capacity Bound.**
Source for the V-capacity counts on the primorial ladder (Table 5.1 + audit ξ, [P]) and the PNT-heuristic shape `K · n² · ln(n) / N²` (§6 audit ι, [P]/[A]). Used by Definition 4.3 (bound slot typing) and Proposition 6.1.

**Paper 17. The Cubic Noether Theorem.**
Source for the cubic Noether closure underlying the Noether defect slot `𝖤` typing (Definition 4.5) and the Appendix A + D Noether-slot entries.

**Paper 18. Bures Completion of Cubic Information-Geometric Mechanics.**
Source for the Bures lift `𝒟(ℂ^N)` underlying Appendix B (HH signature) and Appendix D (FEP-3 sector resolution).

**Paper 26. Conductor Probe-Obstruction Theorem.**
Source for the exact quotient divisor rule (`H_d` survives `C_N → C_k` iff `d | k`) referenced in Definition 4.2 (the quotient component of `𝖱`).

### Worked-example anchor papers

**Paper 34. The Conductor Blind Spot.**
Source paper for Appendix C. Schema-instance inherited at Paper 34's tier ([P] for the second-order optimizer blindness mechanism at `p_*`).

**Paper 37. Label Smoothing in the Conductor Blind Spot.**
Source paper for Appendix C's training-time substitution mechanism. Schema-instance inherited at audit λ K-branch tier ([P] on widths 16/32/64, v2insert-07 §2.4).

**Paper 45. Conductor-Certified Sparse Autoencoders.**
Source paper for the F-slot completion pattern referenced in §7.3 Remark 7.3.1 (DCD F-slot completion).

**Paper 46. Hartle–Hawking Signature.**
Source paper for Appendix B. Schema-instance inherited at Paper 46's tier ([P] for the structural HH signature on `D(ℂ^6)` and `D(ℂ^30)`; [C, reduced] for the holographic-bound reading).

**Paper 49. Arithmetic Decoupling of Projection-Closure Overflows.**
Synthesis paper this paper is deliberately *not* in. Source for the three-manifestation framing of the cross-appendix observation in §8 (without re-derivation). Source for the tier discipline that Appendices B, C, D inherit.

**Insert 15 FEP-3 audit (insert15_fep3_gradient_vs_least_action_audit.py + run output, 2026-05-20).**
Source paper for Appendix D. Schema-instance inherited at Insert 15 deterministic-audit tier ([P] for the gradient-vs-least-action sector resolution on `ℤ/6`).

### Discipline and methodology

**Paper 35. Grounded-Paranoid-Delusional Methodology.**
Source for the tier discipline ([P], [P]-spirit, [A], [C], [C, reduced], [D]) used throughout. Source for the three-outcome matched-pair pre-claim discipline (§3.1, extended at v2insert-04 §3.1) that types the F-slot in Definition 4.6.

**v2insert-04 §3.1 (three-outcome matched-pair extension).**
Source for the joint-on-disjoint branch `F_⋈` in Definition 4.6. Source for the K-branch / L-branch / joint-on-disjoint outcome classification used in §7.2 and Appendix A.

### Memory anchor

**Memory `project_arithmetic_line_structurally_complete.md` (2026-05-20).**
Source for the three currently-blocked external-resource gates referenced in Appendices B–D and Gates G4–G5: μ_210+ (workstation memory for higher Bures rows), κ (GPU + HF compute for inference-side conductor-blind-spot propagation), FEP-3 empirical biology (data for biological-systems extension of the FEP-3 sector resolution). The schema-formalization of this paper does not unblock any of the three; it does specify what completing the F-slot for each would require.
