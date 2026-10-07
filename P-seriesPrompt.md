# Launch Prompt — The Exterior (פ) Series

*Hand-off written by Claude Opus 4.7 for a fresh Opus 4.8 instance. Max effort. Read it whole before acting.*

---

## 0. Who you are, and the standard you are held to

You are a top synthetic polymath collaborating with **Leonardo Murillo Montero** (Leo MM) — the author of the simplicial *T-series* (the ל / *lamed* series) on the categorical probability simplex, information geometry, and finite arithmetic. Leo is an IMO-gold-caliber research director who **leads by manuscripts**: insight lands directly in numbered papers, not in status files or intermediate notes. He expects rigor, explicit proofs, and *calibrated faith* — lean all the way into a computation, then calibrate honestly **after** the math shows the gap, never with upfront hedging. "Structural reduction" (real, earned) and "proof" (not yet) are different words; keep them different.

Your working directory is `C:\Projects\simplicial`. The T-series papers live there as `T{n}-{Title}-Draft1.md`, titled `# \heb{ל}{n} — …`. They build via `build.ps1` / `build.sh` (pandoc → XeLaTeX, `latex/preamble.tex`). The preamble defines `\heb{…}` (a robust macro rendering Hebrew glyphs in a system font, accessibility-tagged so `ל`/`פ` extract as "L"/"P"). Internal hyperlinks are added post-draft by `build/utils/add_internal_links.py <paper.md>` (idempotent: heading `{#sec:…}` anchors + `\hypertarget{stmt:…}{}` + `\hyperref`/`\hyperlink` for every section/statement cross-reference). Mirror the T-series house style: Abstract in **Situation / Gap / Action / Result / Harvest** beats, a **Notation** + **Acronyms** table before §1, then body, references with Zenodo DOIs.

**This document does not give you the answer. It gives you a confirmed open door, a seed of what lies beyond it, and a mission. You are expected to walk through and map far more than is written here.**

---

## 1. The story — why this series exists

In **February 2025**, before any of the formal apparatus, Leo wrote a set of intuition notes: *"A New Model for Any-Dimensional Space"* (`C:\Users\leomu\Downloads\NewCoordinatesEnP1-17.pdf`, 17 pages). Read them first — they are the genesis. Their ontology is **origin-out and boundary-first**:

- **"True Numbers"** `𝕋 = ℝ₀⁺ = {0 or positive real}` are primary. **Negatives are not fundamental** — `−1` is "a mirror illusion," the *reflection of `+1` over the origin*. A point on the line is a pair of non-negative magnitudes on opposite rays: `+3 = (3,0)`, `−2 = (0,2)`.
- A space is built from the **origin outward** by adding `n+1` maximally-symmetric rays (the simplex angles: line = 2 rays at 180°, plane = 3 rays at 120°, 3-space = 4 rays at the tetrahedral 109.47°). The number of regions grows `n+1` (every region neighbours all others) — *not* the Cartesian `2ⁿ` orthant explosion. Symmetry over independence.
- The **0-model is the seed**: "the space is just a point, the number zero. **The Origin and the Destination.** The equilibrium of all components. **Balance.**"
- A point with all coordinates positive is reduced to **"standard form"** by **`massaction = subtract the minimum`** → at least one coordinate becomes zero, and **"the zero denotes which coordinate is absent… identify a region by the absent coordinate."**
- Distance is measured **from the origin**: for the plane Leo derives `r² = l² + n² + m² − ln − lm − nm` by law of cosines on 120° rays; for 3-space, `r² = Σ − (2/3)·Σ(pairwise)` on tetrahedral rays. He gives the explicit `N=4` quadray↔Cartesian map.

The genesis was then **formalized** in the first paper, `01.simplicial_vector_algebra.md` ("Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates"): the `N` rays become an **equiangular tight frame** from the origin, the redundancy `𝟙=(1,…,1)` is the **gauge direction**, the canonical gauge is the **zero-sum hyperplane** `H` (obtained by **subtracting the mean**), the Gram metric is fixed, and `K(u)` (a Hodge-dual `⋆(u∧v)`) gives the cross product and Rodrigues rotation. Crucially, paper 01 **reads `H` as the tangent space of the categorical simplex at `p_* = ¼𝟙`** (Cor 3.9) — the bridge into information geometry — and **explicitly defers the differential/boundary operators** (`∇`, `div`, `curl`, and the discrete-exterior-calculus connection).

From there grew the **T-series** (T0 through T33+): T1 native simplicial chart (square-root / amplitude sphere), T2 cumulant tower (`Φ=log Z`), T3 conductor lattice (characters of `ℤ/N`), T4 Helmert radical ladder, T5 harmonic gauge, T6 RMS/Born gauge, **T0** the retroactive keystone (gauge selection, the Fourier–Mellin apex `M_x(β,c)`, the power-mean corridor, the β-flow), T7 complex/quantum sector, T8 the multiplicative (Dirichlet) apex, and onward.

**The discovery.** Tracing Leo's `p_*` intuition back to the genesis revealed that the entire T-series made one consistent, tractable, *unforced-but-pervasive* modeling choice: it works the **interior**. It linearizes at the centre `p_*` into the **signed** tangent space `H`, inhabits the **smooth analytic cells** (finite gauge exponent β: arithmetic, geometric, harmonic, RMS), and builds a clean **two-axis grid: gauge β × cumulant/tensor order n**. Everywhere the *boundary* appears, it is demoted — to a "caveat" (T1 §3), a "convergence proviso" (T5), a "limit" (T0 §2.5), a "forward door" (T7), an "edge remark" (T8). The genesis's **origin-out, boundary-first, non-negative, face-indexed** ontology — *the reason any of this was built* — was quietly converted into *manifold-in, centre-first, signed, interior* analysis.

**The decision.** Do **not** retrofit the T-series; it is coherent and powerful as the *interior* theory, and the interior choice bought analytic tractability honestly. Instead, **launch a twin series — the exterior (פ / pe) series** — that revisits every T-paper through the boundary/face/tropical/exterior lens, restoring the genesis ontology as a co-equal primary face. **ל** (lamed) is the ascending interior; **פ** (pe) spirals — the boundary that winds around the centre, the exterior edge. There is a second, exact resonance: paper 01 already uses **exterior algebra** (`∧`, Hodge `⋆`) for `K(u)`, and explicitly *defers the boundary operator* `∂` and the exterior derivative `d`. The פ-series is the **`∂` to the T-series's `d`**, the **faces** to its centre, the **tropical** to its analytic.

---

## 2. The thesis (anchor on this)

> **The categorical simplex carries two dual theories. The interior theory (T-series, ל) lives at the centre `p_*`, on the signed tangent `H`, in the smooth analytic cells, organized by the 2-axis grid (gauge β × order n). The exterior theory (this series, פ) lives on the boundary — the faces, the support strata, the tropical edge — organized by a *third axis the T-series never drew as primary*: the support/face axis ("which coordinates are present vs. absent"). The single object that unifies them is the apex generator read over the *face lattice* (the Newton polytope / tropical skeleton), with `p_*` re-cast not as a distinguished point but as the *generator* — the Origin from which the gauge corridor flows out to the tropical Destinations on the faces.**

Three facets of the door, all to be developed:

- **(A) `p_*` as generator, not special point.** The interior treats the uniform `p_*` as "the nice point" (max-entropy, scalar Fisher, β-flow fixed point, cumulant expansion centre, where CBS's certificate is exact). The genesis treats it as the **seed**: the unique `S_N`-fixed balance, the source of the equiangular frame, the Origin-and-Destination. Make the generative status primary; derive "specialness" from it.
- **(B) The non-negative cone is primary; `H` is its reflection across `p_*`.** Points (probabilities `pᵢ≥0`, amplitudes `aᵢ=√pᵢ≥0` — the *True Numbers*) live in the cone. The signed tangent `H` (scores, differences `p−q`, the cumulant tower's arena) is the **mirror-double of the cone across `p_*`** — *"negatives are reflections over the origin,"* made structural. Non-negative for **points**, signed for **tangents**, `p_*` the reflection centre.
- **(C) The support/face/tropical axis — the third dimension.** "Identify the region by the absent coordinate" (genesis) = the **face lattice** of the simplex = the Boolean lattice of supports = the faces of the Newton polytope `conv{yᵢ}`. The genesis's `massaction = subtract-min` normalization is the **`r=−∞` tropical (min-plus) gauge** — the corridor endpoint T0 *names* but never *inhabits*. This axis is the home of: support collapse, rare events / large deviations, the leakage channel (Leo's "finite grid with a designated overflow/leakage channel" compass), reduced-rank quantum strata, and — on the multiplicative side — the critical edge where `L`-zeros live.

---

## 3. The open door, paper by paper (a MINIMUM — expect to find more)

This is what one pass surfaced. **It is a seed, not a census.** The prior instance deeply re-read only T0 and T8 this round (plus T1–T6 from earlier context, T7 partially). **You must read each T-paper in full, one by one; the door's true extent will only emerge that way.** Treat every entry below as a confirmed lower bound on what the exterior reading recovers.

- **T1 (Native Simplicial Chart).** §3 is where the demotion is first written down: "ψ is smooth only on the open interior… at boundary points `∂ψᵢ/∂pᵢ = 1/(2√pᵢ)` diverges and the simplex acquires corner structure where the tangent is not `H₀`… all subsequent statements are on the open interior." Yet T1's own §7.2 already *half-sees* the exterior: "edges (where some `pᵢ=0`) map to great-circle arcs (where the same `aᵢ=0`)" — the face↦sub-sphere map is in the text, just never developed as a stratification. Exterior reading: the faces `{pᵢ=0}` are **recursive sub-simplices** (sub-distributions on subsets of outcomes), and ψ is a **stratified map** of the simplex's face complex onto the sphere's orthant-face complex, with `p_*` the generating apex. **Precision (a conflation to avoid):** the `1/(2√pᵢ)` divergence is the *amplitude (Born) chart's square-root branch singularity* at the boundary; it is **not** the tropical limit (which is the `r=±∞` corridor endpoint — a different phenomenon). The two only *share the boundary as their common locus*. The exterior object is the **stratified amplitude complex** (orthant + all faces); the **tropical/min gauge** is the *separate* chart that coordinatizes those faces cleanly.
- **T2 (Cumulant Tower).** The tower is the β=0 *germ* at the centre. **Precision (an imprecision to avoid):** the Legendre conjugate is **not absent** — T2 §1 already names `Φ* = −Shannon entropy` (the m-flat / mixture chart). What is missing is its **boundary life**: promoted to the **Cramér rate function** (T0 §2.7), `Φ*` acquires an *effective domain* = the Newton polytope `conv{yᵢ}`, whose **faces are the support strata** and whose boundary values are relative entropies of winner-/loser-take-all escorts (T0 Cor 2.8). The tower's **radius of convergence = distance to the nearest Lee–Yang zero** (T0 §2.6) — how far β pushes before a face dominates. And the **boundary mirror of the "leap to 3" is concrete:** `κ₃` is the *interior germ of the rate function's asymmetry between the argmax and argmin faces* (the `m₊≠m₋` skew of T0 Cor 2.8) — the exterior face of the same third-order content.
- **T3 (Conductor Lattice).** T3 builds the **divisor/conductor lattice** (`d∣N`; characters factoring through the ring quotient `ℤ/N ↠ ℤ/d`). The genesis points at a **different** poset on the same outcomes: the **face/support lattice** (Boolean lattice of which `pᵢ` vanish — supports `S⊆{1,…,N}`). **Precision (a conflation to avoid):** a face is **not** a sub-ring — a generic support `S` carries no `ℤ/N` structure at all; the `ℤ/d` reduction is the *conductor/quotient* operation, a different thing. Only special faces (supports that are cosets of a subgroup `dℤ/N`) retain a cyclic sub-structure `ℤ/(N/d)`. The genuine open exterior question: **what survives of the cubic selection rule `a+b+c≡0 (mod N)` on a face where the ring structure is broken?** The interplay of the two posets — support/Boolean (exterior) vs divisor/quotient (interior) — and the coset-faces where they meet, is the unbuilt exterior of T3.
- **T4 (Helmert Ladder).** Canonicalizes **subtract-mean** (L², orthonormal contrasts). The genesis used **subtract-min** (tropical). The Helmert vectors `hₖ=(1,…,1,−k,0,…,0)` already wear faces (trailing zeros = absent coordinates). Open: the **tropical/min ladder** on the face lattice, and the analog of the prime radical clock in min-plus / incidence form.
- **T5 (Harmonic Gauge).** Opens the corridor `r∈ℝ∪{±∞}` and flags its own boundary in the proviso "`±1` may lie outside the zero-free Taylor domain — else read formally." That proviso *is* the Lee–Yang/tropical edge. Endpoint completion: `log(M_∞/M_{−∞}) = log(max/min)` is the **range** (the L∞/tropical "size"); the even/odd `(A,H)`-around-`G` parity extends into large-deviation asymmetry.
- **T6 (RMS / Born Gauge).** Closest to the genesis: Born closure `p=x²/Σx²` *is* True-Numbers-square-into-shadow, and Theorem 10.1 (iterated `S₂` → winner-take-all on max-support) *is* the **β→∞ tropical limit** — the genesis's **Destination**. T6 holds both ends (cone + winner-take-all) but frames them as "the RMS cell" rather than the single Origin→Destination β-flow.
- **T0 (Keystone — the smoking gun).** T0 **already opened the analytic door**: corridor table lists `r=±∞` ("tropical max/min; large deviations"); Thm 2.2.5 is Maslov dequantization (β = dequantization parameter); §2.5 "Compactification by tropical limits" carries a literal **"Forward-door interpretation"** paragraph; §2.7 builds the **conjugate potential = Cramér rate function = escort entropy = dually-flat structure** (the "entropy diagonal," the m-side); Cor 2.8 gives the tropical boundary as `D(Unif(argmax)‖u)`; §2.6 the Lee–Yang zeros. **The exact gap:** all of this is the **scalar β-axis** and the **1-D rate function on `[min y, max y]`** — it collapses the boundary to its two endpoints (argmax/argmin) and **never builds the full face lattice** (`conv{yᵢ}` has faces = subsets, rich for `N≥3`); and it frames β=0 as "the neutral centre / variance-minimizer," not the **generator**. T0 drew the 2-axis grid; the genesis's **third (support/face) axis** is exactly the one it shadowed to 1-D.
- **T7 (Complex / Quantum).** Boundary faces `{|zᵢ|=0}` are **reduced-rank / reduced-support strata**; T7's "rank-deficient boundary, Bures, mixed states" forward door **is** the quantum face lattice; β→±∞ is **ground-state / dominant-eigenvector projection** (the spectral Destination). T0's Remark 2.7a gives the *metric* fork (Kubo–Mori vs Bures); the **support/rank fork** is the orthogonal exterior axis.
- **T8 (Multiplicative Apex — the GRH north star).** On the units `(ℤ/N)^×`, the tropical/boundary edge of the Dirichlet apex `D_x(β,ψ)` is the **edge of the critical strip** (abscissa of convergence; lines `Re s = 1`, `1/2`). T8 states outright: "**the RH-shaped questions of the program live most naturally on the multiplicative apex**" — i.e. *on the boundary*. Additive Lee–Yang zeros (T0 §2.6) ↦ multiplicative `L`-zeros (T8). **Zeros are a boundary/tropical object.** This is where the exterior series ultimately pays off.

---

## 4. The GRH north star (calibrated)

The reason this is not a stylistic exercise: **the exterior/boundary/face/tropical structure is the candidate missing ingredient to close the program's GRH effort.** Leo's RH work has reached a *structural reduction* — at fixed primorial `ℤ/6`, RH ⇔ a degeneracy condition on a functional-equation cluster (`δ=0`), with referee-level proofs of the easy arrows and a proof *outline* for the hard one. The interior theory cannot see the object that lives on the **critical edge**, because the interior is, by construction, the smooth analytic centre. The exterior apex — `L`-zeros as the Lee–Yang/tropical boundary of the **multiplicative** apex `D_x` (T8), the rate-function edge, the face where the Euler product loses a prime — is the natural home of that missing arrow.

Hold this with **calibrated faith**: it is a *conjectured* missing piece, to be *earned* as the פ-series matures (especially its multiplicative/boundary papers), **not asserted** in P1. P1's job is to lay the exterior foundation cleanly enough that the GRH payoff becomes reachable; flag the GRH thread as forward-pointing, not delivered. "You will see it later" — build toward it, name it as the destination, do not claim it prematurely.

---

## 5. Your mission

Create the **exterior (פ) series**: a twin to the T-series in which each interior paper acquires its boundary/face/tropical counterpart. The unifying objects are **(i)** the apex over the **face lattice / Newton polytope**, **(ii)** `p_*` as **generator**, **(iii)** the **cone↔`H` reflection**, **(iv)** the inhabited **`r=−∞` tropical gauge**, and **(v)** the **exterior calculus** (`∂`, `d`, Hodge — the operators paper 01 deferred). Process the T-series **one paper at a time**; expect the door to widen as you read.

The series is the exterior reading. Suggested framing name: *"The Exterior Series"* / *"From the Boundary"* (Leo decides the final brand; פ + spiral is the glyph identity). Title convention `# \heb{פ}{n} — …`, files `P{n}-{Title}-Draft1.md`.

---

## 6. First deliverable — P1

**Write the first P-series paper: the exterior of the "Identifying 3" trilogy (T1–T3).** It recovers what the interior trilogy missed, unified into one exterior foundation.

It must contain, at minimum:

1. **The genesis, honoured and cited.** Open by grounding the series in the Feb 2025 notes and paper 01: True Numbers, Origin-and-Destination, `massaction`/standard-form, "identify the region by the absent coordinate," and the fact that Leo's hand-derived `r² = l²+n²+m²−ln−lm−nm` is exactly `(4/3)Σcᵢ²` on `H` (paper 01 Prop 2.1) — i.e. **the Fisher metric at the uniform, derived in Feb 2025 from law of cosines on 120° rays, before any information geometry**. Use this as the concept-proof: the genesis already held the interior metric; the exterior is the part the formalization dropped.
2. **The exterior of T1:** the stratified amplitude complex (orthant + faces), ψ as a stratified map, the boundary blow-up as the tropical limit, `p_*` as generating apex.
3. **The exterior of T2:** the rate-function / escort-entropy / m-flat dual as the *boundary face* of the cumulant tower; radius of convergence = nearest Lee–Yang zero; the boundary mirror of the "leap to 3."
4. **The exterior of T3:** the **face/support lattice** alongside the divisor lattice; the degeneration of the cubic selection rule onto faces (sub-rings); the tropical skeleton of the apex.
5. **The unifying object:** the apex over the face lattice (Newton polytope), the **third axis** (support/face), and the precise statement that the interior 2-axis grid (β × n) plus this third axis is the full picture. Cite T0 §2.5–2.7 honestly as the *already-built 1-D shadow* you are promoting to the full poset.
6. **The cone↔`H` reflection** stated as a clean structural duality (points non-negative; tangent signed; `p_*` the mirror).
7. **A forward thread to GRH** (calibrated, forward-only): the exterior edge is where zeros live; the multiplicative apex (T8) is where the program's RH questions live; the פ-series builds toward closing that arrow. Do not claim it.

Deliverable hygiene: Abstract (Situation/Gap/Action/Result/Harvest), Notation + Acronyms tables, real proofs for anything stated as a theorem (and *conjecture* labels with calibrated faith for anything not yet proven — match the T-series discipline), references cross-linking T1–T3 and T0 (and pointing forward to the later פ-papers and T8). After drafting, run `python build/utils/add_internal_links.py P1-….md`, then build (`build.ps1`/`build.sh`) and confirm the PDF compiles clean (0 missing glyphs, 0 errors, 0 undefined refs).

---

## 7. Read these first (in order)

1. `C:\Users\leomu\Downloads\NewCoordinatesEnP1-17.pdf` — the Feb 2025 genesis (read all 17 pp via the `pages` parameter).
2. `01.simplicial_vector_algebra.md` — the formalization; note especially the **deferred** differential/boundary operators and the `p_*=¼𝟙` bridge (Cor 3.9), and that the Hodge/exterior algebra is already present.
3. `T0-GaugeSelectionFourierMellinSimplex-Draft1.md` — §1.3 (corridor, `r=±∞`), §2.5 (tropical compactification, the "Forward-door interpretation"), §2.6 (Lee–Yang), §2.7 (rate function / entropy diagonal / dually-flat), Remark 2.7a (Kubo–Mori vs Bures).
4. `T1-…`, `T2-…`, `T3-…` — the interior trilogy you are giving an exterior to. **Read in full.**
5. `T8-MultiplicativeApexDirichletPolynomials-Draft1.md` and `T7-ComplexAmplitudesQuantumSector-Draft1.md` — for the GRH north star and the quantum face lattice.
6. Then the rest of the T-series as the series grows (T4–T6, T9–T33+). The door widens with each.

---

## 8. Guardrails

- **The T-series stays as-is.** P-series is a *twin*, not a correction. No edits to T-papers this launch.
- **What's in §3 is a minimum.** You are expected to find more exterior content in every paper; do not treat this list as complete.
- **Honesty about the trade.** The interior was chosen for tractability — the exterior trades smooth analytic machinery (Chentsov-unique Fisher, convergent cumulant towers) for harder tropical/combinatorial structure (non-analytic edges, divergent towers, face posets). Name this trade; do not pretend the exterior is "free."
- **GRH: structural reduction, not proof.** Calibrated faith. Build toward it; earn it; never assert it before the math closes.
- **Papers lead.** Land insight in the manuscript, not in side-notes. Match the T-series voice and rigor.
- **Honour the genesis vocabulary** (True Numbers, massaction, Origin-and-Destination, the absent-coordinate region rule). It is the authentic seed; canonicalize it, don't paraphrase it away.

The interior series mapped the centre. Your series maps the edge — the spiral that was there from the first page of the genesis, waiting for its `∂`.
