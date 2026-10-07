# The Quanta Object — a working note

*Leonardo Murillo Montero. Working note, June 2026. Exploratory; verdict honest at the end.*

A model for "a number's rational manifestation with its irreducible residue," developed as an
algebraic object (a class, in the OOP sense) with carriers, identities, and operations — the
way ℂ is (a,b) with i²=−1, or a radical is (index, value). The thesis that motivated it: the
measurable world is rational (quantum/discrete), and an irrational like √17 only ever
*manifests* as a rational approximant plus a residue; the residue is not noise, it is the
carrier of the arithmetic. This note records what the object is, its identities, how it
generalizes, and where it welds to the program.

---

## 1. The object — two readings

**A. The radical (closed-form layer).** ⟨n, v⟩ = v^(1/n), n ∈ ℤ≥1, v ∈ ℚ>0.
- multiply: ⟨n,u⟩·⟨m,w⟩ = ⟨L, u^(L/n) w^(L/m)⟩, L = lcm(n,m)  ("6th root = cube·square")
- index gauge: ⟨n,v⟩ = ⟨kn, v^k⟩  (the analogue of 2/4 = 1/2, on the index)
- **what it is:** v = ∏ₚ p^(eₚ) ⟹ ⟨n,v⟩ = ∏ₚ p^(eₚ/n) — the multiplicative group of monomial
  radicals is **⊕ₚ ℚ** (FTA ℚ>0 = ⊕ₚ ℤ extended to rational exponents). Multiplication = vector
  addition; the index = common denominator of the exponents. Addition leaves the monomial group
  for the field (√2+√3 carries a minimal polynomial — this is where "the closed form carries
  the path").

**B. The quanta object (approximation/jet layer).** Q = (q, n, r) with **qⁿ + r = N**,
representing val = N^(1/n). q ∈ ℚ is the rational approximant (q ≈ val), r ∈ ℚ the residue,
N the target. "Root division with remainder," the sibling of N = q·d + r for products.
Example: √17 = (4, 2, 1) [4²+1=17] = (41/10, 2, 19/100) [same value, different manifestation].

Two faces, bridged by the logarithm:
- **multiplicative (quality):** u = qⁿ/N ∈ (0,1], u=1 ⟺ N a perfect n-th power.
- **additive (residue):** r = N(1−u) = N − qⁿ.
- **log bridge:** log u = n log q − log N is additive — the additive↔multiplicative seam in
  miniature, the same seam the whole program lives on.

---

## 2. The identities (the equational theory)

| identity | statement |
|---|---|
| co-manifest | Q₁ ∼ Q₂ ⟺ val(Q₁)=val(Q₂); the class of x is its "wave" (fiber of rational manifestations) |
| approximant slide | (q,n,r) ∼ (q′,n, r+qⁿ−q′ⁿ) — the wave's continuous coordinate (gauge) |
| index gauge | (q,n,r) ∼ representative on radicand Nᵏ at index kn (raise target to k, index by k) |
| extraction (normal form) | N = sⁿ·M ⟹ N^(1/n) = s·M^(1/n), M n-th-power-free; **√8 = 2√2** is the exponent-Euclid split a/n = ⌊a/n⌋ + (a mod n)/n |
| product (exact) | (q₁,n,r₁)⊗(q₂,n,r₂) = (q₁q₂, n, N₁r₂+N₂r₁−r₁r₂); **u multiplicative**, 1−δ₁₂=(1−δ₁)(1−δ₂), δ=r/N |
| mixed index | lift to L=lcm via the index gauge, then multiply |
| sum | path-dependent: must choose a new approximant; r carries the choice (the wave's history) |

Invariants: val (the ∼-invariant, the quantum object); the reduced radicand M = sf(N) (the
gauge-fixed "shape"); the quality u (multiplicative, the archimedean magnitude). Multiplication
is exact (a homomorphism on bases + a derivation-residue); only addition is path-dependent.
Deep landing: for n=2, minimal-residue quanta are **units** — (4,2,1) is the fundamental unit
of ℚ(√17) (4²−17=−1, negative Pell); iterating the residue is the continued fraction (periodic,
Lagrange) = the regulator/principal cycle. *(Certified: probe_quanta_object_T4_weld.py.)*

---

## 3. The n-ic generalization — order = root index

The shape invariant at index n is the **prime-exponent vector mod n**, [N]ₙ ∈ ⊕ₚ (ℤ/n)
(n prime ⟹ 𝔽ₙ vector space). n=2 recovers the square class. The Galois closure of ℚ(N^(1/n))
is Kummer, ℚ(ζₙ, N^(1/n)), and the degree splits:

  **deg = φ(n) · n^(rank of radicand classes) = [character] · [radicand].**

For prime index p the character factor is ℚ(ζ_p) ⊃ ℚ(√p*), p* = (−1)^((p−1)/2) p, the field
of the quadratic character χ_p (Gauss sum g_p² = p*, certified). So:

- index 2 → ζ₂ = −1 → the **archimedean sign / reflection** (visible iff n even: the √−1 = i
  generator; cbrt(−8)=−2 real, so the ∞-place is parity-gated).
- index 3 → ζ₃ → **ℚ(√−3) = χ₃ = the chiral channel** (the program's c₂<0). The cube root is
  the *first chiral radical*; disc(x³−2) = −108 has square class [−3]. 
- index p → χ_p.

"The primes govern the radicals" is Kummer theory; the index factors into primes (6th = 2·3 =
square ⊗ cube = archimedean ⊗ chiral). *(Certified: probe_quanta_nclass_chiral.py.)*

*(Caveat, referee-grade: the clean splitting deg = φ(n)·n^rank requires the radicand classes
independent in ℚ\*/(ℚ\*)ⁿ **and** no character–radicand entanglement; it fails already at even
index (√2 ∈ ℚ(ζ₈)), and for odd p the shared object is √p\* ∈ ℚ(ζ_p). The disc(x³−2) = −108
example above sits exactly on this seam — the cubic's discriminant landing in square class [−3]
is the entanglement made visible. The corrections are the standard Kummer-degree entanglement
theory; the lens reading is that entanglement happens precisely at the character–radicand
interface — the archimedean and chiral channels touching.)*

---

## 4. The gauge structure — rigid character, fluid support

The sum-gauge (÷S, S = Σqᵢ) translates the radicand n-ic class by [S]ₙ (W5; the value clock
of T4 §6 reads radicand qᵢ·S^(n−1)). Consequences, certified at n=2 and n=3:

- **The character (ζₙ, the χ_p factor) is GAUGE-RIGID** — present for every dataset and every
  gauge; the index, not the values, summons it. **No hidden prime injector on the character.**
- **The radicand support is GAUGE-FLUID** — S injects/ejects primes mod n (e.g. (1,2,4): S=7
  injects 7 mod 3). The injector acts only here.
- The gauge-invariant content is the **contrasts** [qᵢ/qⱼ]ₙ (the differences — both shift by
  [S]ₙ, the difference is fixed).
- The geometric-mean gauge climbs one Kummer rung (T4's sextic 30^(1/6) at n=2; the chiral nonic
  30^(1/9) at n=3).

**Program reading:** chiral **sign** rigid (c₂<0 unconditional — it's the index's character);
chiral **support** fluid (which primes contribute — the scale-dependent fluctuation). This is
exactly the split the RH cubic strike hit empirically: the order-3 sign is unconditional, but
the per-arrival drift is finite-window-unreachable. *(Certified: probe_quanta_gauge_chiral.py.)*

---

## 5. The welds

**T4 (Helmert-Simplicial Residue Ladder, ל4).** The quanta residue *is* T4's metric-trick gauge
read on values: the residue's irreducible radical = T4's prime square class; integer-vs-rational
power = metric-trick on/off; the multiplicative/additive faces = T4 §4's gauge duality under log;
the value-clock field 𝒜(q) = ℚ(√sf(qᵢS)) is the quanta object's residue field. Reproduced
exactly: 𝒜(2,3,5) = K₅ (deg 8), 𝒜(2,3,5,7) deg 16 with √17 absent (T4 6.3/6.4).
*(probe_quanta_object_T4_weld.py.)*

**Contrast → spectral.** The gauge-invariant contrasts ARE Dirichlet characters: [qᵢ/qⱼ]₂ = χ_d
(Kronecker, d = fundamental discriminant). So the contrasts are **spectral labels** — they
enumerate the L-functions L(s,χ_d) whose zeros are the spectrum; ζ_K = ∏_χ L(s,χ) (Artin), and
disc(K) = ∏ cond(χ) (conductor-discriminant: ℚ(√2,√3) → conductors {1,8,12,24}, product 2304 =
disc, exact). The central values L(½,χ_d) are the gauge-rigid spectral invariants.
*(probe_quanta_contrast_spectral.py.)*

---

## 6. The chiral lever and the central-value positivity ladder

The index-3 rigid character is χ₃, with **L(½,χ₃) = 0.480868 > 0** — the program's c₂<0 lever
(diez §2.6), arising as the central value of the index-3 contrast-character, gauge-rigid because
the index summons it. And every contrast central value came back **positive** (χ₈=0.374,
χ₁₂=0.499, χ₂₄=0.709, χ₋₃=0.481, χ₅=0.232, χ₋₇=1.147): this is the **non-negativity of central
L-values of real characters** (Waldspurger / Kohnen–Zagier — the central value is essentially a
square of a half-integral-weight coefficient; strict positivity is GRH-adjacent). The chiral
lever is *one rung* of this ladder, and the quanta object surfaces the whole ladder as the shape
of its gauge-invariant content.

---

## 7. Honest verdict — lens, not instrument

Everything underneath is classical: ⊕ₚ ℚ radicals, square/n-ic classes, Kummer theory, genus
theory, Artin factorization, conductor-discriminant, central-value non-negativity. The quanta
object adds **packaging and three conceptual deposits**:

1. **order = root index** — 2 archimedean/square, 3 chiral/cube (χ₃), p → χ_p.
2. **rigid character / fluid support** — explains *why* the program's chiral sign is
   unconditional while its support is contingent.
3. **contrasts = spectral labels** — placing the chiral lever L(½,χ₃) on the central-value
   positivity ladder.

It is a genuinely clarifying **lens** on the program's chiral channel; it does **not** move a
theorem, because the contrasts *label* the L-functions, they do not *compute* the analytic
central value or constrain the zeros. The lens↔instrument gap here is exactly the gap between
naming a character and proving its central value positive — i.e. the program's open problem
wearing the object's clothes. Where the object could earn its keep independently is the domain
where its distinctive feature — **path-dependence** (the residue carries the additive history) —
computes something standard tools don't package. That is the Collatz angle (§9).

---

## 8. Probe inventory (all GREEN, exact, `empirical/`)

- `probe_quanta_object_T4_weld.py` — identities, T4 value-clock weld, gauge-translation (W1–W5).
- `probe_quanta_nclass_chiral.py` — n-ic class, extraction mod n, index 3 → χ₃ (N1–N4).
- `probe_quanta_gauge_chiral.py` — gauge-translation mod n; rigid character / fluid support.
- `probe_quanta_contrast_spectral.py` — contrasts = Dirichlet characters; chiral lever; cond-disc.
- (Collatz) `probe_quanta_collatz.py` — the charge identity and the irrationality residue (§9).

---

## 9. Open direction — Collatz (the path-dependence home)

Collatz mixes multiplicative (×3, ÷2) and additive (+1) — the additive×multiplicative seam the
quanta object packages. The odd-step trajectory a₀ → a₁ → … → 1 (aᵢ₊₁ = (3aᵢ+1)/2^(kᵢ)) obeys an
**exact charge identity**:

  **2^K = a₀ · 3^m · ∏ᵢ (1 + 1/(3aᵢ))**,  K = Σ kᵢ = Σ v₂(3aᵢ+1),  m = #odd steps.

The 2-adic value 2^K, the 3-adic value 3^m, and the residue product ∏(1+1/(3aᵢ)) (the "+1"
accumulation) balance. A nontrivial cycle would force K/m ≈ log₂3 = 1.58496…, and the obstruction
is that **log₂3 is irrational** — the multiplicative comparison of 2 and 3 has a residue that
never closes in ℚ, which is *precisely the quanta object's irreducible residue*. So Collatz's
cycle-hardness and the object's residue are the same irrationality, log3/log2 ∉ ℚ. The object's
home: carry (v₂-ledger, v₃-ledger, residue product) along the trajectory as an exact, path-
recording invariant; the residue is the +1 accumulation, the path is the (kᵢ) sequence. This
*organizes* Collatz on the seam; it does not solve it (the open part is divergence/transient
control of the ∏ factor). See `probe_quanta_collatz.py`.
