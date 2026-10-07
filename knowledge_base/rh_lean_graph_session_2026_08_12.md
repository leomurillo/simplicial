# RH → Lean Graph: Session Record 2026-08-11/12

Created: 2026-08-12
Status: control-layer record. Companion to `claim_graph.md`; same skeptical rules.

This session moved the program from informal RH-adjacent mathematics toward a
**Lean-driven, traceable** mapping. It also produced one publicly released result
and a large body of *verified negatives*, which are the scarcer asset.

---

## 0. Artifacts and where they live

| artifact | path / URL | state |
| --- | --- | --- |
| Public paper + code | `https://github.com/leomurillo/zeta-moment-ladder` | released, MIT, 12/12 tests |
| Lean project | `C:\Projects\simplicial\lean\rhgraph\` | Lean 4.33.0, Mathlib v4.33.0 (8690 cached) |
| RH graph file | `lean\rhgraph\Rhgraph\Surface.lean` | compiles, 9 `sorry`, audit shows `sorryAx` |
| Upstream artifact | `https://github.com/anthropics/zeta-23-lean` | sorry-free, 3 standard axioms |

Toolchain installed this session: `elan`, Lean 4.33.0, lake 5.0.0. Same series as
zeta-23 (v4.33.0-rc2), so that repo should build here.

---

## 1. New exact results [C]

Sine-kernel Gram moments, extending §7.5(f) of [CLAUDE2026] which stops at `m_4`:

```
m_k(1), k=0..6 :  1, 1, 4/3, 2, 13/4, 101/18, 640/63
                                      └── new ──┘
```

- **RH-L1** `m_5(1) = 101/18` — computed 5.611111111017404, diff 9.4e-11
- **RH-L2** `m_6(1) = 640/63` — computed 10.15873015858979, diff 1.4e-10
- **RH-L3** Conversion rule (not stated in [CLAUDE2026], reconstructed here):
  `HL*(2m,λ) ⟹ liminf N₀ˢ/N ≥ 1 − 2Λ_m(0)`, Λ_m the Christoffel function of the
  moment sequence at 0. **Pinned** by reproducing the paper's own `Λ₂ = 5/36`
  and `13/18`.
- **RH-L4** `Λ₃(0) = 247/2519`, so **HL\*(6) ⟹ proportion ≥ 2025/2519 = 0.803890433…**
- **RH-L5** General-λ closed forms: `m₂(λ)=λ+λ³/3`, `m₃(λ)=λ+λ³`,
  `m₄(λ)=λ+2λ³+λ⁵/4`; `A_{k,0}=1`, `A_{k,1}=C(k,2)/3` for all k.

**Tier caveat:** RH-L1/L2 are *numerically certain, symbolically unproven* —
floating-point box-spline evaluation validated to ≤6e-11 against all four
published moments and cross-checked by CUE (z = −0.71, −0.90), then recognised as
rationals. Exact-arithmetic version specified in the repo's `docs/method.md#exactness`.

### Method (reusable)
Determinantal expansion of `tr G^k` over set partitions; every term is the density
at the origin of a sum of independent uniforms along the incidence-matrix columns
— i.e. **a box spline value**, evaluated by de Boor–Höllig recursion.
**Trap:** the evaluation point is the zonotope *centre*, exactly on a mesh
boundary where the half-open basis convention returns a wrong one-sided value
(smallest instance: `Ξ={e₁,e₂,e₁+e₂}` at `(1,1)` gives 1/3, truth is 1). Since the
trace cycle connects every block, `n−d ≥ 1` and the spline is continuous, so
evaluate along a generic ray and extrapolate the offset to zero.

**Refuted:** the pairing ("free Wick") expansion. Valid for ≤1 pair; at k=4 it
gives `49/15 = 3.2667` against the true `13/4`. CUE separates decisively
(3.25164 ± 0.00312; z=+0.52 vs 13/4, z=−4.82 vs 49/15).

---

## 2. Correction to a prior program record [C]

`empirical_leverage/HL_cumulant_order4_RESULT.md` records
`C_n(p) = −(n−1)!/φ(p)ⁿ` as an all-orders identity. **It is one as rational
functions in p; as arithmetic it holds only for `p > n`** — the s-distinct-residues
stratum is empty when `p < s` (at p=2, s=4 the formula returns −8).

New closed form: the local moment generating function is elementary,
`Σ_s M_s(p) z^s/s! = e^{pz/φ(p)}(1 − z/φ(p))`, so the cumulant generating function
is `log(1 − z/φ(p))` up to a linear term — factorials over totient powers are just
the Taylor coefficients of a logarithm at its branch point. All strata reduce:
`(1−ν/p)/(1−1/p)^s = M_ν(p)·(p/φ(p))^{s−ν}`.

**Consequence:** the keystone describes the *tail* of the Euler product and says
nothing about the small primes, where parity lives.

---

## 3. Verified negatives — the main yield

Four dissimilar agents; every load-bearing numeric independently re-derived by the
coordinator before acceptance.

**N1 [C] Mollifier counts can never bind.** Exact vertex LP on (x₁ simple on-line,
u multiple on-line, v simple off-line pairs, w multiple off-line pairs) with mass
≤1 and inertia ≥8/3: `min x₁ = 2/3` exactly, at (2/3, 0, 1/6, 0). Levinson-shape
`x₁+u ≥ κ` is **non-binding through κ = 5/6** (record is 5/12); CGG-shape
`x₁+2v ≥ c` is **non-binding for all c ≤ 1**, i.e. even given "every zero simple".
Mechanism: an off-line pair at depth d→0 and an on-line double zero are the *same
matrix* (cost 4.000000 either way).

**N2 [C] The union idea is a conservation law.** On the extremal family,
`N_on + N_simple ≡ (1+H)·N` for every λ, so `N₀ˢ ≥ N_on + N_simple − N` returns
**exactly H** — the constant you started with. Verified at H = 2/3 and 0.6725007.

**N3 [A] The real fourth path, and where it dies.** Bui–Heath-Brown's
`19/27 = 0.7037` is unconditional *except* at the single step the 2026 paper exists
to remove ("this is the only place we need RH"). Block structure transfers and is
*sharper* (ζ′(ρ)=0 at multiple zeros ⟹ rank P ≤ s₁). **Dies on `tr H²`** — a
mollified pair correlation of ζ′, Hardy–Littlewood strength, unknown even under RH,
and necessarily ≍N² terms since rank P ≥ cN forces d ≥ cN.

**N4 [C] The off-line count has dual variable identically zero** — including at
Q=0, which *is* RH. So no hypothesis about off-line zero location beats 0.6725.
Corroborated by the paper's own abstract: 2/3 and 0.6725 are **Montgomery's and
Montgomery–Taylor's constants under RH**. The 2026 unconditional constants equal
the RH-conditional ones to every printed digit — *RH was never buying anything in
that functional.*

**N5 [C] Zero-density estimates are dominated.** Huxley and Guth–Maynard are worse
than trivial at σ=1/2. The certificate's own second moment already encodes a
Density-Hypothesis-shaped bound (slope 2) unconditionally; at d=1, T=10³⁰ it is
3.3e6× stronger than Ingham.

**N6 [C] Inertia is cardinal, by Sylvester.** Inertia is a *complete* congruence
invariant, so any certificate depending only on the congruence class is blind to
density-zero sets — a theorem, not a shortfall. Ordinal content needs a module
(H,A) whose invariant is the Gohberg–Lancaster–Rodman sign characteristic.

**N7 [A] A second instrument exists and is dominated.** τ-Li moments
(Freitas; Palojärvi effective version) are **not subsumed** — Davenport–Heilbronn
separates them, since a single off-line zero flips λₙ. But detection needs
`n* ≍ (γ²/δ)·log(γ²/δ)`; at T=3×10¹² that is ~10²⁶ coefficients at ~10²⁶ digits,
i.e. **dominated by direct zero-verification by roughly a cube.**

**N8 [C] de Branges positivity is FALSE for ζ.** Conrey–Li; reproduced
independently at the **34th zero** ρ = ½ + 111.0295355431696745i, value
−5.389100507182945e−69 (matching to 16 digits once the ξ normalisation factor 4 is
accounted). Also verified Conrey–Li (3.4) exactly.

**N9 [A] Krein–Langer blocked at entry** — Pontryagin Π_κ needs κ < ∞;
unconditionally we have only density zero. **N10 [C] Turán's condition refuted**
(Montgomery 1983). **N11 [A] Faltings–Hriljac structurally incapable** — finite
Picard rank cannot host a multiset counted by (T/2π)log T.

**N12 [A] The discriminator.** ζ has "no zeros right of the pole"; on the
periodic-coefficient class where the counterexamples live this is *equivalent* to
the Euler product (Saias–Weingartner). It is already inside the certificate, worth
**exactly one factor of log X**, buying `o(1)` beyond 2/3. Signal/noise for seeing
β>½ through the prime side is `X^{−1/2}·log X → 0`; the detection threshold sits at
β=1, where de la Vallée Poussin already put it.

**N13 [C] ainta's certificate is essentially TIGHT.** True minimum of their F6 is
≈0.003826231 against a certified 19/5000 = 0.0038 (0.68% margin); α = 1/3000 is at
the peak of the α curve; m = 269 is *forced* by their Lemma's `A₀ = β(m−6) < 1`.
Total available: **+1.7e-5**.

> **Recorded error:** the coordinator first claimed +0.00059 was available and was
> about to publish it. It was wrong — the optimiser never entered the true basin,
> and ainta's own verifier found the correct region. Cause: a search that wanted a
> result. This is why every numeric in this file was re-derived before acceptance.

---

## 4. Lean state

**Terminal node exists:** `RiemannHypothesis` is in Mathlib
(`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`, line 185).

**Critical structural fact: `RiemannHypothesis` has degree zero in the proved
graph.** Mathlib contains no theorem of the form `P ↔ RiemannHypothesis`. Every
known equivalence (Robin, Lagarias, Li, Nyman–Beurling, Weil, Speiser) is a
*claimed* edge. Until one is formalised, RH cannot be approached from the backward
side at all.

`Surface.lean` currently holds:

| face | nodes | edges |
| --- | --- | --- |
| RH=true | Lagarias, Li, Chebyshev, Weil, Speiser | 9 `sorry` |
| RH=false | LiNegative, LagariasViolation | **derived** by contraposition |
| in-edges from axioms | — | **zero** |

**Mathlib surface discovered by asking the library, not by recall:**
- `Chebyshev.psi` **exists** (`NumberTheory/Chebyshev.lean`) with ~20 lemmas. A
  hand-rolled `∑ n ∈ Finset.Icc 1 ⌊x⌋₊, Λ n` typechecks, denotes the same
  function, and is **off the blanket** — unreachable from all of them. Now rewired.
- `riemannZetaZeros : Set ℂ` **exists** (`LSeries/ZetaZeros.lean`) with closedness,
  discreteness, compact-finiteness. My earlier claim that no zero-set API exists
  was wrong; the zero-sum form of Li's criterion should be re-examined.
- `deriv riemannZeta` available (`LSeries/Deriv.lean`) — anchors **Speiser**, a node
  never on the informal list, and zeta-23's `XiPrime/` has adjacent unconditional
  results.

**Collapse criterion (the measurement device):**
> CLOSED ⟺ a term of type `RiemannHypothesis` (or its negation) **with no
> hypotheses**, whose `#print axioms` lists only `propext, Classical.choice,
> Quot.sound`. OPEN ⟺ `sorryAx` appears **or the theorem binds a hypothesis.**

The second disjunct is what exposes the circulating "machine-checked RH" preprints
(e.g. `RiemannHypothesis_mathlib_from_pinch_ext_assign`): sorry-free, three-axiom
clean, and vacuous, because the analytic heart sits in an un-instantiated
"statement-only interface". Current reading on our own file: `sorryAx` on all four
probed edges — honestly open.

---

## 5. Method notes (transferable)

**Dissimilar-arm ensemble ("salts").** Verifier-gated portfolio search:
(1) conditioning diversity, (2) *target* diversity, (3) shared negative cache,
(4) verifier-gated acceptance, (5) independent adjudication. Component (3) did more
work than (1). Nearest literature: N-version dissimilar redundancy, algorithm
portfolios, Luby restarts, quality-diversity, FunSearch/AlphaEvolve.

**Markov blanket correction.** Logically equivalent propositions are the *same node*
only in the proposition graph. In a *search* graph a node is individuated by its
blanket — the neighbours through which proof can reach it. Lagarias, Li, Weil,
Chebyshev and Speiser have nearly disjoint blankets. So: **condense the SCC for
truth, never for search.** "One node in many costumes" was a real error.

**Engulfment, not tunnel.** A node is determined by its blanket, so RH falls when
the proved frontier *covers a sufficient blanket* of some member, not when a path
arrives. Consequences: partial coverage compounds (partial tunnels are worthless);
grow at **blanket overlap**, since one proved node serves several blankets; rank by
**uncovered deficit**, not distance (distance is zero for every equivalence).

**The RH=false face is the mirror, not a singleton.** If `P ↔ RH` then `¬P → ¬RH`,
so every equivalence supplies a disproof route. `∃n, λₙ < 0` is computationally
probeable (literature reaches n≈3300; program note #19 says the additive encoding
breaks at n≈157 for an off-line zero).

---

## 6. Process lessons (cost real time this session)

1. **One `lake` at a time.** Concurrent invocations corrupt the shared Mathlib
   cache (`failed to read … .olean`). Happened twice, the second time immediately
   after diagnosing it. Looks like a broken import; is not.
2. **`lake new … math` leaves new files orphaned** — the root imports only `Basic`,
   so an unbuilt file is indistinguishable from a passing one.
3. **~1000 s per compile** with `import Mathlib`. Narrowing imports is the single
   highest-leverage fix before further iteration.
4. **A statement can typecheck and still be wrong for the graph** (the `psi` case).
   Typechecking proves well-formedness, not blanket membership.
5. Confidence and accuracy were uncorrelated on Mathlib names: `σ` failed as
   expected, `iteratedDeriv` on ℂ succeeded against expectation, and
   `riemannCompletedZeta` — the name I had no doubt about — is spelled
   `completedRiemannZeta`.

---

## 7. Open, ranked

1. **First proved edge adjacent to RH.** Nothing else unblocks backward search.
   Cheapest by statement: Lagarias. Best-connected blanket: Li (program #19
   realises the tower to 2.3e-41). Best *overlap*: Speiser (Mathlib `deriv` +
   zeta-23 `XiPrime`).
2. **Exact m₅, m₆** — replace floating-point box-spline with exact rational
   recursion and exact polynomial extrapolation from n−d+1 rational offsets in one
   cell. Upgrades RH-L1/L2 from [C-numeric] to [C-symbolic].
3. **MRT I extended to (Λ∗Λ)×(Λ∗Λ)** — the only live door to an unconditional
   gain. Range is comfortable (need H = N^{1/2}; MRT reach N^{8/33}); gap is
   function class. MRT treat Λ and d_k "in a largely unified fashion" via
   Linnik/Heath-Brown, so the (ζ′/ζ)² worry is **not** the obstruction.
4. **Trace layer**: MD → Lean coverage (see next-session brief).
