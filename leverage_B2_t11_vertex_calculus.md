# Leverage B2 — T11 Apex Vertex Calculus ↔ Paper III (and II, IV)

**Assessment of the clarifying lenses Papers II–III–IV provide for T11.**
Working note, not a manuscript edit. No existing paper is modified.

Author of record: Leonardo Murillo Montero. Analysis prepared as a leverage probe.

---

## 0. One-paragraph verdict

T11 is the **arithmetic twin** of Paper III's cumulant tower: T11's
character-conservation vertex `V_n(a₁,…,aₙ;c) = 1[a₁+…+aₙ ≡ c (mod N)]`
is exactly the additive selection rule that Paper III/T3 reads off the
Amari–Chentsov cubic `T = ∇³Φ`, promoted from `n=3` to all orders, and
T11's connected-diagram (Möbius) rule is the finite-Fourier image of the
same moment→cumulant inversion that defines Paper III's tower. The mapping
in **(1)** below is a **genuine structural correspondence** — tier **EXACT**.
The cert nails this empirically: T11's connected quartic vertex `V₄^conn`
reproduces **Paper 21's hand-computed ℤ/30 Wick atlas exactly** (1202 / 120 /
1082 quadruples and the **914** three-prime connected vertices), with zero
new input — the single most concrete payoff of this leverage.

The central question — is Paper II's gauge-Hodge **harmonic sector** a model
for T11's **conductor-fusion boundary / projection leakage** — has a split
answer that I hold honestly. The correspondence is **real in one precise
abstract sense and loose in another**:

* **Real (abstract cokernel):** T11's leakage support `∂ₙS` is a harmonic
  class in the exact sense of Paper II Theorem 7.1 — it is the part of the
  projected interaction that the retained sector cannot represent, the
  cokernel `(1−Π_S)(u₁⋯uₙ)`, the "leftover that cannot be written inside the
  sub-theory." That is structurally the same role `h` plays in
  `F = grad f + curl A + h`. This is a faithful analogy, and it sharpens
  both objects.
* **Loose (the specific Hodge harmonic numbers):** `∂ₙS` is **not** the
  harmonic sector of the same complete-complex Hodge Laplacian. Its
  dimension is `∑_{d∈∂ₙS} φ(d)`, a **divisor/order-axis** quantity, whereas
  the Paper II/IV Hodge harmonic numbers are the **degree-axis** quantities
  `dim H⁰ = 1` and `b₁(K_N) = C(N−1,2)`. These do not coincide except at the
  one shared object: the **gauge line** `H₁ = span{𝟙} = H⁰(K_N)`.

So the honest tier for the gauge-Hodge↔leakage bridge is **CLARIFYING**
(confirming the plan's label), upgraded to **EXACT only on the gauge line**.
The clean way to say it, in the program's own Paper IV vocabulary: **T11 is
the order-axis refinement of the bicomplex `Pₙ Λᵏ`; the Hodge/Helmholtz
harmonic sector is the degree-axis one; they are two different harmonic
sectors of two different differentials, meeting only at the corner
`(n,k)=(·,0)` gauge line.** The "designated overflow channel" of the
program's finite-grid thesis is precisely that shared gauge line, and T11
gives it a second, finer life as the unit packet `H_N = (ℤ/N)ˣ` on the
squarefree primorials.

---

## 1. What T11 actually proves

T11 ("The Apex Vertex Calculus — Finite Feynman Rules for the
Cumulant-Gauge Tower") works over `G = ℤ/N` with characters
`χ_a(s)=e^{2πi a s/N}`, the structured apex
`M_x(β,c) = (1/N)∑_s e^{βy_s} \overline{χ_c(s)} = \widehat{e^{βy}}_c`, the
additive conductor `cond(a)=N/gcd(a,N)` (`cond(0)=1`), and conductor packets
`H_d = span{χ_a : cond(a)=d}`. Three structure theorems:

**Theorem 2.1 (Apex Feynman Rule).** Every Taylor jet and every integer
closure sample of the apex is computed by finite character-conservation
vertices:
```
∂_β^n M_x(0,c) = ∑_{a₁+…+aₙ ≡ c} ŷ_{a₁}⋯ŷ_{aₙ},
  i.e.  V_n(a₁,…,aₙ;c) = 1[a₁+…+aₙ ≡ c (mod N)].
```
Moments are all finite diagrams; cumulants are their connected parts by
Möbius inversion on the partition lattice `Πₙ`, giving the connected vertex
`V_n^conn = ∑_{π∈Πₙ}(−1)^{|π|−1}(|π|−1)! ∏_{B∈π} 1[∑_{i∈B} a_i ≡ 0]`.
Corollary 2.2 ("birth of closure defect"): since `ŷ₀=0`, singletons vanish;
`n=3` is the first interacting odd vertex; `n=4` is the first order where
disconnected pairings must be subtracted (the quartic).

**Theorem 3.1 (Conductor Fusion).** Writing `α_{i,p}=v_p(d_i)`,
`B_p=max_i α_{i,p}`, `m_p=#{i:α_{i,p}=B_p}`, the output packet
`d=∏_p p^{γ_p}` is fixed prime-locally:
```
γ_p ∈  {0}            if B_p=0
       {B_p}          p odd, m_p=1
       {0,…,B_p}      p odd, m_p≥2
       {B_p}          p=2,  m_p odd
       {0,…,B_p−1}    p=2,  m_p even
```
with the global support the CRT product of locally allowed exponents.
Reading: fusion is controlled by the highest-depth leg; uniqueness of the
top leg makes it survive, multiplicity allows cancellation, and **p=2 is
special** because parity blocks cancellation when the number of top odd
units is odd. (This is the structural reason `N=6` is asymmetric between the
2-axis and the 3-axis.)

**Theorem 4.1 (Projection-Closure).** For `H_S=⊕_{d∈S}H_d`, the projected
`n`-vertex closes on `H_S` iff `S` is fusion-closed
(`d₁,…,dₙ∈S ⇒ Fuse(d₁,…,dₙ)⊆S∪{1}`). If it fails, the **universal residual
support** of the projected interaction is the **conductor-fusion boundary**
```
∂ₙS = ⋃_{d₁,…,dₙ∈S} Fuse(d₁,…,dₙ) \ (S∪{1}),
```
attained exactly (every boundary packet occurs for some character input).
Corollary 5.2 gives the minimal fusion completion `Cl_n(S)` (smallest closed
sector), and fusion-closed sets form a meet-semilattice.

The headline:
> every projected simplex theory leaks exactly through its conductor-fusion
> boundary.

T11 explicitly disclaims any physical/spacetime/Bures content (§8); it is
"the lamed-series has a finite arithmetic perturbation theory."

---

## 2. The mapping to Paper III (and the additive selection rule)

This is the strong, exact half.

| Paper III (geometric tower) | T11 (arithmetic tower) | status |
|---|---|---|
| `T^{(n)} = ∇ⁿφ` cumulant tower (entropy chart, diagonal) | `∂_β^n M_x(0,c)` apex Taylor jets | both are the `n`-th rung of one scalar generator |
| moment→cumulant Möbius inversion on `Πₙ` (Paper III/T2) | `V_n^conn` via Möbius on `Πₙ` (Thm 2.1) | **identical combinatorics**, T11 in the character basis |
| order-2 = Fisher metric `g=∇²φ` | `n=2` propagator, scalar in character basis (T3) | self-dual rung; "arithmetic silent at order 2" |
| **order-3 = Amari–Chentsov cubic `T=∇³φ`** | **`V₃(a,b,c) = 1[a+b+c ≡ 0]`** | **EXACT**: T3's selection rule `a+b+c≡0` *is* the AC cubic's nonzero pattern |
| order-4 quartic obstruction = `2+2` Wick block of `∇⁴Φ` (Paper III §7) | `n=4` first order needing disconnected-pairing subtraction (Cor 2.2) | both localize the quartic as the first genuinely-connected correction |
| `α↦−α` Legendre involution `φ↔Φ`, sign-flip per order | additive vs multiplicative apex (T11 §7); `(−1)ⁿ` transfer (T2 Prop 6.2) | the even/chiral channel split |

**The load-bearing identification.** Paper III's Proposition 7.x and T2/T3
say the Amari–Chentsov cubic, read in the `ℤ/N` character basis, is nonzero
exactly on `a+b+c≡0 (mod N)`. T11 Theorem 2.1 at `n=3, c=0` is *literally
this line*, now derived as one case of the all-orders apex Feynman rule.
T11's own §1 says the cubic proof "did not use anything special about 3" —
only that characters multiply by adding indices and orthogonality kills
nontrivial total index. So:

> **T11 is the promotion of Paper III's order-3 selection rule to a full
> finite vertex calculus, and Paper III is the order-2/order-3 information-
> geometric content of T11's tower read on the entropy chart.**

The lens runs both ways and is exact. Paper III contributes three
clarifications back to T11:

1. **Why the tower is a *cumulant* tower, not just a moment tower** — Paper
   III's `Φ = log Z` effective-action framing (T2) is the generating
   functional T11 Theorem 2.1 differentiates; the connected/Möbius step is
   the same `log` that turns `Z` into `K=log Z`.
2. **The chart dichotomy.** Paper III proves the *entropy*-chart tower
   `∇ⁿφ` is purely diagonal and therefore **cannot host the quartic
   `2+2` obstruction**, which lives in the conjugate *exponential* chart
   `∇ⁿΦ`. T11's vertices `V_n` are character-basis (exponential-side)
   objects — so T11 is computing on **exactly the chart where Paper III
   proves the obstruction lives**. This is a clean consistency check: the
   conductor-fusion boundary (T11's obstruction) is an `e`-chart phenomenon,
   matching Paper III Prop 7.2.
3. **`p=2` ≠ odd-prime asymmetry has a geometric echo.** T11 Thm 3.1 makes
   `p=2` special by parity; Paper III/T2 §4 note the `N=2` Bernoulli cubic
   *vanishes at the centroid* by `p↔1−p` symmetry. Both are the same
   statement that the 2-axis carries no odd (cubic) closure — T11 derives it
   as "three conductor-2 legs have odd 2-maximal multiplicity, so they
   remain conductor 2 and cannot close."

---

## 3. The central question: gauge-Hodge harmonic ↔ fusion boundary

### 3.1 The two objects, precisely

**Paper II harmonic sector.** On `H = {c:∑c_i=0} = ℝᴺ/⟨𝟙⟩`, the gauge-Hodge
(Helmholtz) decomposition (Thm 7.1) is
`F = grad f + curl A + h`, with the harmonic `h` annihilated by both `curl`
and `div` — the "leftover that cannot be written as a gradient or a curl."
Paper II/IV pin the relevant complex as the complete graph/complex `K_N`:

* the **distinguished** harmonic/gauge class is `H⁰(K_N) = ker d₀ = span{𝟙}`,
  dimension `1` (Paper II Prop 7.2; Paper IV Thm 2.1);
* the **1-form** harmonic/current sector is `ker L₁`, dimension
  `b₁(K_N) = C(N−1,2)` (Paper IV Thm 5.1; for `K_4`, `b₁=3`).

**T11 leakage.** For a retained sector `H_S`, the projected `n`-vertex's
universal residual is `(1−Π_S)(u₁⋯uₙ)`, supported on the conductor-fusion
boundary `∂ₙS = ⋃ Fuse \ (S∪{1})` (Thm 4.1). It is a sum of conductor
packets `⊕_{d∈∂ₙS} H_d`, dimension `∑_{d∈∂ₙS} φ(d)`.

### 3.2 Where they genuinely match (REAL)

Three structural features line up and are not coincidental:

1. **Both are cokernels of a closure map.** `h` is what survives after you
   remove everything in the image of `grad` and `curl`; `∂ₙS` is what
   survives after you remove everything `Π_S` can represent. In each case
   the object is *defined* as "the part the sub-theory cannot account for,"
   and in each case it is the **exact universal residual**, not a worst-case
   bound. Paper II's Thm 7.1 orthogonal-complement statement and T11's
   "attained by some character input" statement are the same shape of claim.

2. **Both are where the program's "blind spot" obstruction lives.** Paper IV
   §4 maps the two program blind spots onto the bicomplex: the *conductor*
   blind spot is the failure to climb the **order axis** past `n=2`; the
   *irreversible* blind spot is the failure to leave the **degree-0
   symmetric column**. T11's `∂ₙS` is the **explicit, computable name** of
   the conductor-blind-spot obstruction: the residual a low-order/low-sector
   truncation must carry. It is the order-axis cousin of the degree-axis
   harmonic `b₁`.

3. **Both carry the gauge line as the distinguished class.** T11's trivial
   packet `H₁ = span{χ₀} = span{𝟙}` is dropped "when working in the
   mean-zero tangent space" (Thm 4.1) — which is **exactly** Paper II/IV's
   `H⁰(K_N) = span{𝟙}`, the gauge/overflow direction. On this one object the
   two pictures are literally equal.

### 3.3 Where the analogy is loose (NOT the same Hodge sector)

The tempting overclaim would be "leakage support = a harmonic/cohomology
class of `K_N`." That is **false as stated**, and the cert makes the failure
quantitative:

* **Dimensions don't match.** For `K_N`, the Hodge harmonic numbers are
  `dim H⁰=1` and `b₁=C(N−1,2)` (e.g. `N=6`: `1` and `10`; `N=30`: `1` and
  `406`). T11's cubic leakage of the canonical proper sector is a sum of
  `φ(d)` over divisor packets (e.g. `N=6`, proper `S={2,3}` ⇒ `∂₃S={6}`,
  leak-dim `φ(6)=2`). `2 ≠ 1` and `2 ≠ 10`. There is no `N` for which the
  two families agree beyond the gauge line.
* **Different differential, different axis.** Hodge harmonic is `ker L_k` on
  the **degree axis** (`d`, antisymmetric forms). T11's boundary is indexed
  by **conductor `d | N`** — a refinement of the **order axis** (`n`,
  symmetric cumulants). In Paper IV's bicomplex `Pₙ Λᵏ` these are
  orthogonal directions; the universal eigenvalue `N` lives on the degree
  axis and the cumulants grow on the order axis, and the towers "meet only
  at the corner `(2,0)`." T11 sits on the **order/conductor side** and
  decorates it with the divisor lattice — which the Hodge tower does not
  see at all.
* **`∂ₙS` is not closed under a coboundary.** A Hodge harmonic class is
  `ker d ∩ ker d*`. `∂ₙS` has no `d`/`d*` annihilation property; it is
  closed (as a completion target) under **fusion** `Cl_n`, an
  order-`n`-dependent, arithmetic closure, not a topological one. The
  semilattice of fusion-closed sets (Cor 5.2) is the divisor-lattice analog
  of the Hodge decomposition's orthogonal sectors, but it is a **different
  lattice** (divisors of `N` graded by conductor) from the Hodge
  decomposition's (form degree `0,1,…`).

### 3.4 The honest synthesis

The correct statement, which I would stand behind in a manuscript, is:

> **T11's conductor-fusion boundary and Paper II's gauge-Hodge harmonic
> sector are the *order-axis* and *degree-axis* instances of one idea —
> "the residual a projection cannot represent is an exact, attained,
> closure-defined class" — inside Paper IV's FEEC bicomplex `Pₙ Λᵏ`. They
> are genuinely the same *kind* of object (a cokernel-of-closure / harmonic
> class), they share the *same ambient* `H = ℝᴺ/⟨𝟙⟩` and the *same
> distinguished gauge line* `span{𝟙} = H⁰(K_N) = H₁`, but they are *not the
> same sector*: the Hodge harmonic is `ker L_k` (degree, dimension `b_k`),
> while the fusion boundary is `⊕_{d∈∂ₙS} H_d` (conductor/order, dimension
> `∑φ(d)`). The analogy is structural and clarifying, not an isomorphism.**

This is a *strengthening* of T11, not a deflation: it places T11's
Projection-Closure Theorem as the order-axis half of a decomposition whose
degree-axis half (Hodge/Helmholtz, with `b₁` as the topological arrow) is
already proved in Papers II/IV. The program gains a clean two-axis picture
of "what a projection leaks": **degree-leak = harmonic current = `b₁`**
(reversibility blind spot); **order/conductor-leak = fusion boundary `∂ₙS`**
(conductor blind spot). Paper IV §4 already asserts these are distinct moves
in one bicomplex; T11 supplies the explicit arithmetic of the order-axis
move, and this leverage note is the bridge that says so.

---

## 4. Connection to the finite-grid + designated-overflow thesis

The user's unifying thesis — *finite categorical-simplex grid, strict
arithmetic capacity on clean data, non-crashing overflow into a designated
leakage channel* — maps onto T11 cleanly, and T11 sharpens it:

* **Finite grid:** `ℤ/N`, the conductor lattice.
* **Strict arithmetic capacity:** the retained sector `H_S` (a fusion-closed
  packet set is a sector that *can* hold a closed order-`n` theory).
* **Designated overflow channel:** at the coarsest level, the gauge line
  `span{𝟙} = H₁` — exactly the thesis's `ℝ𝟙` overflow direction, and the
  one place the Hodge and fusion pictures agree. But T11 reveals the
  overflow is **finer than a single channel**: a non-closed sector overflows
  into a *specific computable packet set* `∂ₙS`, and on the **squarefree
  primorial** the cubic overflow of the full non-unit sector lands exactly
  on the **unit packet** `H_N = (ℤ/N)ˣ` (`N=6 → {1,5}`). This is the thesis
  made into a theorem with an address: the overflow is non-crashing
  (`H_S ⊕ ∂ₙS` is still inside `H`), typed (by conductor), and bounded
  (finite divisor lattice). T11 is, in the thesis's own words, the law that
  says *where* the excess goes when a sector "tries to process more than its
  arithmetic capacity allows."

The one caution the thesis-memory itself flags — do not inject the
metaphysical framing into the technical manuscripts — is respected here:
this note is the framing bridge, kept separate from the proofs.

---

## 5. Certificate

`empirical_leverage/B2/cert_fusion_boundary.py` (sympy, deterministic, exact
integer arithmetic; `py -3.13`). Four blocks:

* **(A)** Conductor Fusion Theorem 3.1 prime-local rule verified against
  direct enumeration of conductors of index-sums: **full** brute force for
  `N=6,12,30` (covers `p=2` odd/even max-multiplicity, an odd prime with
  single/multiple top legs, and the 3-prime CRT product), cubic and quartic;
  **sampled-subset** check for `N=210`.
* **(B)** T11 `N=6` worked example reproduced exactly: the six closing cubic
  multisets `{222,444,114,255,123,345}`, the `3+3+3=9≡3≠0` failure of the
  pure `A₂` triple, and `∂₃{2,3}={6}` with leak-dim `φ(6)=2`.
* **(C)** Cubic/quartic fusion boundaries and leak-dimensions
  (`∑φ(d)`) for the proper non-unit sector on `N=6,30,210`.
* **(E)** Cross-pollination A2: T11's connected quartic vertex `V₄^conn`
  reproduces **Paper 21's entire ℤ/30 Wick atlas** — 1202 total / 120
  Wick-reducible / 1082 connected, and the three-prime span counts
  `{5}:4, {2,3}:6, {2,5}:32, {3,5}:126, {2,3,5}:914` — exactly.
* **(D)** Side-by-side table of the gauge-Hodge harmonic numbers
  (`H⁰=1`, `b₁=C(N−1,2) = 10, 406, 21736`) vs the T11 cubic leak-dimensions
  (`2, 8, 48`), demonstrating §3.3's claim that they differ except on the
  gauge line; and the assertion that the proper-sector cubic boundary equals
  the unit packet `H_N` for `N=6,30,210` (the overflow-to-units claim).

**Status: GREEN — all exact checks pass (`py -3.13`, exit 0).** Key results:

| check | result |
|---|---|
| Thm 3.1 prime-local rule = brute force (N=6,12,30, cubic+quartic) | 0 mismatches |
| N=6 worked example (6 closing multisets, `3+3+3≡3≠0`, `∂₃{2,3}={6}`) | exact match |
| proper-sector cubic boundary = unit packet `H_N` (N=6,30,210) | True |
| `b₁(K_N)` vs T11 leak-dim (10/2, 406/8, 21736/48) | differ (as predicted) |
| **T11 `V₄^conn` vs Paper 21 ℤ/30 atlas (1202/120/1082, 914)** | **exact match** |

Run log: `empirical_leverage/B2/run_b2.log`.

---

## 6. Cross-pollination notes

* **A2 (Paper 21 quartic / Wick) — VERIFIED EQUAL, not just analogous.**
  T11 Cor 2.2 ("`n=4` is the first order where disconnected pairings must be
  subtracted from a nontrivial moment") is the **arithmetic statement of the
  `2+2` Wick obstruction** that Paper III §7 / Paper 21 locate in the
  exponential chart. T11's connected vertex
  `V₄^conn(a,b,c,d) = 1[a+b+c+d≡0] − 1[a+b≡0]1[c+d≡0] − 1[a+c≡0]1[b+d≡0] −
  1[a+d≡0]1[b+c≡0]` is, **term for term**, Paper 21's quartic selection rule
  `Q|_u` (its boxed eq. in §5.1). Cert block **(E)** reproduces Paper 21's
  ℤ/30 atlas exactly from T11's `V₄^conn`: of the **1202** unordered
  quadruples in `{1..29}` summing to `0 mod 30`, **120** are Wick-reducible
  (Gaussian floor) and **1082** are connected; classified by conductor-prime
  span, the genuine three-prime connected vertices number **914**. So
  **Paper 21's `N4` obstruction count *is* T11's connected-quartic vertex
  count** — T11 supplies the finite combinatorial skeleton Paper 21's atlas
  is an instance of, and the surviving connected part on a fusion-non-closed
  sector is the quartic leakage `∂₄S` (cert block C). This is the cleanest
  win of the leverage: a number Paper 21 computed by hand (914) falls out of
  T11's Möbius-connected vertex with zero new input.
* **B1 (mechanics floor / α-collapse).** Paper III §6 collapses the whole
  `α`-connection family to one cubic `Γ^{(α)}=−(1+α)/2 · T`. T11 says that
  cubic's nonzero pattern is `V₃`. So the **mechanics floor's force law is
  T11's `n=3` vertex**; the "α-collapse" is the statement that all
  connection content lives at the order-3 rung, which T11 then resolves into
  conductor packets. B1's cubic mechanics inherits T11's fusion boundary as
  its **closure obstruction** — the dynamics generated by `T` fails to close
  exactly on `∂₃S`.
* **C1 (RH apex N14/N15).** T2 Prop 6.2 (already in the corpus) ties the
  apex cumulant tower to the Hardy–Littlewood connected `n`-tuple weight via
  `κ_n^{HL}=(−1)ⁿκ_n^{apex}` on the conductor block `(ℤ/p)ˣ`. T11 is the
  vertex-calculus substrate of that transfer: `V_n` on `(ℤ/p)ˣ` is the
  multiplicative selection `ψ₁⋯ψₙ=ψ` (§7), and the `(−1)ⁿ` is the
  `α↦−α`/`φ↔Φ` involution. **The fusion boundary on `(ℤ/p)ˣ` is the
  arithmetic-side residual that the explicit-formula transfer must carry** —
  worth checking against N14/N15's "primes = Legendre minus" residual.
* **C2 (quantum Bures).** T11 §8 explicitly does *not* claim a Bures result;
  Paper III D4 flags the monotone-metric (Bures vs Kubo–Mori) fork as the
  quantum continuation. **Clean division of labor:** T11 is the classical
  (commutative `ℤ/N`) vertex calculus; the quantum lift replaces the
  additive selection `V_n` with a non-commutative fusion (Clebsch–Gordan-like)
  rule, and the fusion boundary becomes the incompatibility budget of Paper
  31's `Γ+iΩ⪰0`. T11's meet-semilattice of fusion-closed sectors is the
  *commutative shadow* of the quantum projection-closure lattice.
* **C3 (unification).** The single most unifying sentence this leverage
  yields: **Paper IV's bicomplex `Pₙ Λᵏ` has the Hodge/Helmholtz harmonic
  on its degree axis (the reversibility arrow `b₁`) and T11's conductor-
  fusion boundary on its order axis (the conductor obstruction `∂ₙS`); both
  are exact closure-cokernels sharing the gauge line `span{𝟙}`.** This is
  the bridge that makes "the two blind spots are two moves in one bicomplex"
  (Paper IV §4) concrete on both axes at once.

---

## 7. Open follow-ups

1. **Does `∂₄S` = Paper 21's `N4` obstruction tensor** on the primorial
   sector? If yes, T11 is the combinatorial floor under A2. (Tractable,
   exact, sympy.)
2. **Multiplicative fusion boundary on `(ℤ/p)ˣ`** (T11 §7 forward door)
   written out, and compared to the N14/N15 explicit-formula residual
   (C1). Needs the T8 multiplicative-conductor strata.
3. **Quantum fusion** — replace `V_n=1[∑a≡c]` by an `su` Clebsch–Gordan /
   Bures fusion and ask whether the projection-closure boundary becomes the
   `Γ+iΩ⪰0` incompatibility budget (C2). Speculative, highest ceiling.
4. **Order-axis ↔ degree-axis pairing.** Paper IV E3 asks whether the degree
   axis past `k=1` reads on the order axis past `n=3`. T11's `∂ₙS` for `n≥4`
   is the order-axis data; does a `b₂`-type current pair with the quartic
   fusion boundary? This is the precise form of the bicomplex's off-corner
   structure.
