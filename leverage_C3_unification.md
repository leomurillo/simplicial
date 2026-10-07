# Leverage Assessment C3 — Simplicial Frame Series → Unification Physics (Papers 30 / 32 / 32.1 / 46)

**Skeptical plug-in audit. Item C3 (unification physics, aesthetic-to-moderate).**
**Author of assessment: subagent C3. Date: 2026-06-23.**
**Scope: does Paper II (`01b`, vector calculus) serve as a differential substrate, and does Paper IV (`01d`, orientation gauge) serve as a gauge model, for the "one functional four forces" line? Plus the explicit K=1/4 vs κ=1/4 verdict.**

> **WRITE-ONLY note.** This file is the sole artifact. No existing manuscript was edited. All claims below were checked against the target papers' text before assertion; the central negative findings (the physics papers contain *zero* spatial differential operators; the program itself never bridges the two lines) are grep-verified, not inferred.

---

## (a) What the unification papers actually claim (brief, and skeptically)

The four target papers form one cluster with a single substrate and an explicit firewall.

- **Paper 32 (`One Functional, Four Forces`, v0.2.5/0.3).** Thesis: the cumulant tower of the categorical log-partition `Φ = log Z` on the finite simplex `Δ_R°`, `R = ℤ/6`, *is* a categorical effective action. Its first four covariant derivatives (information-geometric / Amari connections) are read as position, the Fisher metric (= space = inertia), the Amari–Chentsov cubic (force), and the time-translation closure defect (gravity-adjacent). The load-bearing technical core (§5) is an **exact arithmetic selection rule** `T_{klm} ≠ 0 ⟺ k+l+m ≡ 0 (mod 6)` (Pontryagin duality on `(ℤ/6)^∧`), which splits the cubic interaction into a closure-valid single-prime block `A_2 ⊕ A_3` (the Cartan `u(1)²`) and a residual supported exactly on the cross-prime carry packet `M = {χ_1, χ_5}` (conductor 6, the units). Standard-Model by-products (tree Weinberg angle `3/8`, one-generation hypercharge spectrum) come from the `E = ℂ²⊕ℂ³`, `Y = ½P_2 − ⅓P_3`, `Λ²E ⊕ E*` construction on `ℤ/6`. A **dimensional firewall theorem** (§12) proves every finite-RG quantity lives on the dimensionless conductor lattice `𝒟_N` — so `G`, `ħ`, `c` (in units), `α`, masses are *permanently* out of scope. Honesty posture is high: the Bures-dispersion audit (§14.2) **refuted** the global-Lorentzian conjecture (Euclidean-4 at the manifold level); the Yang–Mills negative (§11.3) is stated as a contribution.

- **Paper 32.1 (`The Bekenstein Sphere`).** The Hellinger map `p ↦ 2√p` embeds the row as a **literal** constant-curvature sphere sector: curvature `K = 1/4`, radius 2, solid-angle fraction `1/2^Q`. Capacity `S_max = log Q` saturated at the centroid = finite Bekenstein bound. The gravitating residual is boundary-localized on `M = (ℤ/N)^×`; the boundary's conductor share `→ ζ(6)/(ζ(2)ζ(3)) ≈ 0.515` (= reciprocal of Landau's totient constant). Eight exact numpy/sympy audits.

- **Paper 46 (`The Hartle–Hawking Signature`).** On the Bures lift `D(ℂ⁶)` the dispersion-Casimir Hessian has signature `(1,3,31)` — a Lorentzian `(1,3)` sub-bundle on the V (single-prime) sector and a Euclidean `(2,0)` sub-bundle on the M (cross-prime) sector, HS-orthogonal at `~10⁻¹⁶`. Read as the Hartle–Hawking "Euclidean globally, Lorentzian locally" no-boundary signature. The orthogonality is forced by Pontryagin character orthogonality `⟨χ_k|χ_ℓ⟩ = 6δ_{kℓ}` on disjoint index sets V = {2,3,4}, M = {1,5}.

- **Paper 30 (`Constrained Overflow and Incompatibility Budgets`).** Promotes the residual side to its own object: a *typed residual calculus* `R_W(A,B)` for "overflow" (the part of a whole exceeding a projection), kept typed/bounded/falsifiable. This is the corpus's explicit statement of the **finite-grid + designated-leakage-channel** thesis. `T30-PhysicsLink-…` is the umbrella overview tying all of the above to T0–T19.

**Skeptical read of the cluster.** The genuinely load-bearing content is *arithmetic*: one congruence mod 6, character orthogonality, and exact finite linear algebra. The "physics" is a **dictionary / correspondence** laid over that arithmetic, fenced by a firewall that (commendably) forbids the dictionary from cashing out as any dimensionful prediction. The papers are internally honest about this (correspondence language, forced-match guards, pre-registered audits, retained negatives).

---

## (b) Honest plug-in assessment

### (b.1) Paper II as differential substrate — **mostly NOTATIONAL; one real but narrow win**

**The decisive finding (grep-verified):** Paper 32, Paper 32.1, Paper 46, and Paper 30 contain **zero** occurrences of `curl`, `divergence`, `Laplacian`, `Helmholtz`, `Hodge decomposition`, `wave equation`, or `de Rham`. The word "gradient" in Paper 32 means **gradient descent / gradient-of-entropy on the statistical manifold** (`∇F_M`, the natural-gradient leakage flow), not the spatial `grad` of Paper II.

This matters a lot. **The unification dynamics are not built from spatial vector calculus at all.** Every "derivative" in the physics line is an *information-geometric covariant derivative* `∇^(n)Φ` of the log-partition — Amari `α`-connections on the probability simplex, with the Amari–Chentsov cubic as the third one. These are a *different differential structure* from Paper II's `grad/div/curl/Laplacian` on the zero-sum hyperplane `H ≅ ℝ³`:

| | Paper II (`01b`) | Unification line (Paper 32/46) |
|---|---|---|
| Manifold | one regular simplex's tangent `H ≅ ℝ³`, **N = 4** | categorical simplex `Δ_R°`, **R = ℤ/6** (Q = 6, dim 5); Bures lift `D(ℂ^N)` |
| "Derivative" | exterior `d`, `grad`, `div`, `curl`, Hodge | Amari `∇^(α)`, cumulant tower `∇^(n)Φ`, SLD/Bures Hessian |
| Cubic object | `K(∇)` (cyclic-difference curl) | `T = Amari–Chentsov`, structure constant `216·𝟙[Σ≡0 mod 6]` |
| What's selected | rotation axes, `b_1 = 3` currents | conductor packets `A_2 ⊕ A_3 ⊕ M` |

The two share the *substrate* (a zero-sum hyperplane with a Fisher metric at the centroid) and a *slogan* ("everything is one cyclic-difference / one functional"), but the operators Paper 32 actually needs (`∇^(2)Φ = g`, `∇^(3)Φ = T`, the Bures Hessian) are **not** Paper II's `grad/div/curl`. Pouring Paper II's wave/heat/Poisson "doors" onto the physics line would be *re-notating* the same hyperplane, not supplying a missing engine. **Verdict for the EM-wave / heat / Poisson / fluid / rotation doors: notational with respect to unification.** They are real, exact, and useful *for* Paper II's own program (spatial PDEs in quadray coordinates) — but Papers 30/32/32.1/46 never ask for a spatial curl or a wave operator, so there is no socket for them to plug into.

**The one genuine (non-aesthetic) win — the S+A / curvature-current split.** Paper II §7.3 (Prop 7.3) and Paper IV §5 (Thm 5.1) establish that the field Jacobian / 1-cochain space splits as `S + A` = (symmetric, curvature, `grad`, `A=0`) ⊕ (antisymmetric, current, `curl`, `tr S = 0`), with `Ã = ½K̃(curl F)` as the antisymmetric↔curl dictionary and the harmonic/topological current of dimension `b_1`. **Paper 32 independently builds the identical split** in its FEP-3 audit (line 270): the metriplectic decomposition `F = F_V + F_M` with `F_V = I_real` Hamiltonian (V-supported, **reversible**) and `F_M = α²(m²_simplex)²` gradient-of-entropy (M-supported, **monotone/irreversible**), cross-coupling zero, "the arrow of time … is the direction of `∇F_M`." Paper IV §5 even names this as the program's "**reversibility blind spot**: a self-adjoint instrument is blind to the antisymmetric current; a two-sided predictor recovers it."

So the reversible/irreversible (Hamiltonian/gradient) dichotomy is a *shared structural object* across the two lines. **But be skeptical about how tight the correspondence is:**
- Paper II/IV split the field Jacobian by **Hodge cochain degree** (`im d₀` exact vs `im d₁ᵀ` coexact on `K_4`). The arrow is `b_1` (topology of the complex).
- Paper 32 splits the Nambu–Fisher free energy by **conductor packet** (single-prime V reversible vs cross-prime-units M irreversible). The arrow is `∇F_M` (the cross-prime carry).
These are *both* instances of "split a dynamics into a reversible symmetric part and an irreversible antisymmetric part," but they partition *different objects along different axes*. The match is at the level of the **organizing dichotomy**, not a term-by-term operator identity. That is real conceptual leverage (it says the two lines are detecting the same reversibility structure twice) but it is **moderate, not a substrate-supplies-the-engine result**.

**Net (b.1):** differential-substrate claim is **mostly notational**; the curvature/current (S+A) reading is a **genuine moderate** structural correspondence — already present *independently* in both lines, so the leverage is "these are the same idea," not "Paper II provides what Paper 32 lacked."

### (b.2) Paper IV's discrete gauge theory as the gauge model for Paper 32 — **LOOSE; a letter-collision trap to avoid**

Paper IV's gauge result (Thm 6.1/6.2): the continuous abelian `ℝ𝟙` connection is **curvature-trivial** (`𝓕 = dA ≡ 0`, because `S_4` fixes `𝟙` and mean-subtraction is a global section); the genuine gauge content is the **discrete orientation field** `ℤ/2 = S_4/A_4` with plaquette holonomy = first Stiefel–Whitney class `w_1` (orientability obstruction), the frame bundle being a flat `S_4` bundle.

Does this model Paper 32's gauge/units structure? **No, or only very loosely.** Three reasons, in increasing severity:

1. **Different N, different group, different role.** Paper IV is `N = 4` (one regular simplex; the relabeling group is `S_4`, orientation `S_4/A_4 = ℤ/2`). Paper 32's gauge/units structure is `M = (ℤ/6)^×` (multiplicative units of a *primorial modulus*), with the SM gauge content `SU(2)×SU(3)×U(1)_Y` arising from the CRT factorization `ℤ/6 = ℤ/2 × ℤ/3` and Kummer-cover deck groups (`μ_6/μ_2 ≅ ℤ/3` colors, `μ_6/μ_3 ≅ ℤ/2` chirality). The `4` of Paper IV and the `6` of Paper 32 are different moduli; `S_4` (frame relabeling) and `(ℤ/6)^×` (arithmetic units) are different groups doing different jobs. There is no map `S_4/A_4 → (ℤ/6)^×` that the program uses or that the structures suggest.

2. **The "M" letter-collision is a trap, not a bridge.** Paper IV writes `M = M_N = NI − J` for the **metric / graph Laplacian**. Paper 32/46/32.1 write `M = (ℤ/N)^× = {χ_1, χ_5}` for the **cross-prime carry packet (units / gravity-adjacent leakage)**. **Same letter, unrelated objects.** Any "M ↔ M" pattern-match here would be a pure notational coincidence and should be flagged as such. (Flagging it pre-emptively so it does not get mistaken for a correspondence.)

3. **The genuinely interesting echo is `ℤ/2`-chirality, and even that is loose.** The one place the two `ℤ/2`s *gesture* at each other: Paper IV's orientation `ℤ/2 = S_4/A_4` with `w_1` (transporting `K̃` around a net-odd loop returns it negated, `K̃ ↦ −K̃`), and Paper 32's chirality `ℤ/2` (the `γ⁵` lock; Face E `= μ_6/μ_3`; the single external KO-real-structure bit that "no real-cone-preserving Bures lift produces," color-protected by the `3+3+3 ≢ 0` root). Both are "an orientation/parity `ℤ/2` that obstructs global trivialization." **But the mechanisms differ:** Paper IV's is the *geometric orientability* of a frame mesh (Stiefel–Whitney, real topology); Paper 32's is an *arithmetic/spectral-triple* chirality bit (KO-dimension, Kummer deck group). They are both `ℤ/2` obstructions, which is suggestive, but `ℤ/2` is the smallest nontrivial group and "a parity that won't trivialize" is ubiquitous. Calling them the same would be over-reaching on present evidence. **At most: a flagged, testable analogy** — *is Paper 32's external chirality bit realizable as a `w_1`-type holonomy of an orientation field on a varying-frame simplicial mesh?* That is a real open question (see follow-ups), not a present correspondence.

**Net (b.2):** Paper IV is **not** a model of Paper 32's gauge/units structure. The abelian-trivial result is generic; the `S_4`-orientation `w_1` content lives at the wrong N and the wrong group. The `ℤ/2`-chirality echo is the only non-vacuous link and it is **loose / flagged-analogy tier**, with a `ℤ/2`-ubiquity caveat.

---

## (c) Explicit verdict on K = 1/4 (Paper 32.1) vs κ = 1/4 (Paper II) — **COINCIDENCE, no mechanism**

This is the headline instruction, so it gets a full adjudication.

**The two `1/4`s, precisely:**
- **Paper II `κ = 1/4`** (`01b` Appendix A, T5.3; Def 3.2/5.1): the **curl-conjugacy / gradient normalization constant**. It arises because the raw cyclic-difference matrix `K̃` over-counts relative to the Cartesian curl by the factor `Ŝ Ŝᵀ = 4 I_3`, so `grad = ¼ d`, `curl = ¼ K̃(d)`. The `4` is literally `N = 4` (the number of simplex rays); `κ = 1/4 = 1/N`. Under the ETF metric `G` it is instead `3/4`. **It is metric-normalization-dependent and equals `1/N`.**
- **Paper 32.1 `K = 1/4`** (Thm 3.1): the **Gaussian/sectional curvature** of the Hellinger sphere. It arises because the Hellinger map `p ↦ 2√p` lands on a sphere of **radius 2**, and a radius-`r` sphere has curvature `1/r² = 1/4`. The `2` is the Hellinger/Fisher-vs-Fubini-Study factor-of-2 (`d_FS = ½ d_FR`); `K = 1/4 = 1/2² = 1/(radius)²`. **It is `Q`-independent and equals `1/(Hellinger radius)²`.**

**Are they the same `1/4`? No. Different origins, different scalings, different invariance.**

| | Paper II `κ = 1/4` | Paper 32.1 `K = 1/4` |
|---|---|---|
| Type | normalization constant (dimensionless ratio) | sectional curvature |
| Source of the value | `1/N` with `N = 4` rays (`ŜŜᵀ = 4I`) | `1/r²` with Hellinger radius `r = 2` |
| Depends on | metric normalization (`M` vs `G` → `¼` vs `¾`) | nothing — `Q`-independent pure number |
| Changes if N≠4? | yes: `κ = 1/N` (Paper IV §2, general-N: `grad = (1/N)d`) | **no**: still `1/4` for every `Q` (radius stays 2) |

The cleanest disproof of a mechanism: **vary N.** Paper IV §2 ("General-`N` calculus") states the curl/grad normalization is `1/N` for all `N` — so the curl `κ` is `1/5, 1/6, …` on the 5-, 6-ray frames. Meanwhile the Hellinger curvature `K = 1/4` is **`Q`-independent** (Paper 32.1 §3: "radius (2) and curvature (1/4) are `Q`-independent pure numbers"). They agree at `N = Q-ray = 4` *only because `1/N` happens to hit `1/4` there*, and they immediately disagree for every other row. A shared mechanism would force them to co-vary; they do the opposite.

**The program already declined the adjacent identification — and I concur.** Paper 32.1 §10.1 ("The factor `1/4` — a guarded echo") *explicitly refuses* to identify its `K = 1/4` with the Bekenstein–Hawking `S = A/4` coefficient, citing the firewall (the area-law magnitude is external) and the §16.4 cautionary precedent (the packet central-charge "6" that "looked intrinsic and proved a terminated coincidence"). The program's own discipline is to flag, not assert, `1/4` echoes. **The κ-vs-K coincidence is one notch weaker than the one the program already declined** (κ is a *different paper's* normalization constant, not even a curvature), so it should be declined a fortiori.

**Verdict: NUMERICAL COINCIDENCE.** `1/4` is ubiquitous (`1/N` at `N=4`; `1/r²` at `r=2`; the `½`-squared of any half-angle / spin-½ doubling; the Bekenstein–Hawking quarter; quadratic-form minima). There is **no mechanism** linking Paper II's curl normalization to Paper 32.1's Hellinger curvature; they coincide at one frame size by arithmetic accident and diverge everywhere else. Do not build on it. (If anything is shared it is the upstream factor-of-2 between Fisher and the embedded/Fubini–Study geometry — but that produces `K`'s radius-2, not `κ`'s `1/N`, so it is not even a common cause.)

---

## (d) Tier verdict — **DOWNGRADE to "aesthetic, with one moderate thread"**

The prompt offered "aesthetic-to-moderate" and asked me to downgrade ruthlessly if it is only aesthetic. My honest call:

- **Differential substrate (Paper II → unification dynamics): AESTHETIC.** The physics line uses information-geometric `∇^(n)Φ`, not spatial `grad/div/curl`; there is literally no operator socket. Re-notating is not leverage.
- **Gauge model (Paper IV → Paper 32 units): AESTHETIC-to-LOOSE.** Wrong N, wrong group, `M`-letter collision; only the `ℤ/2`-chirality echo survives, and it is a flagged analogy with a `ℤ/2`-ubiquity caveat.
- **K=1/4 vs κ=1/4: COINCIDENCE** (explicitly, see (c)).
- **The S+A / reversibility split (Paper II §7.3 + Paper IV §5 ↔ Paper 32 FEP-3 `F_V+F_M`): MODERATE.** This is the *only* item that rises above aesthetic, and it earns "moderate" only as a *shared organizing dichotomy independently present in both lines* — not as substrate-supplies-engine.

**Overall C3 tier: AESTHETIC, with a single MODERATE thread (the reversibility/curvature-current split).** This is a downgrade from the optimistic end of the offered band. The cluster's real strength is its internal arithmetic and its firewall discipline; the simplicial-frame series (II/IV) does not supply a missing differential or gauge engine to it. The program's own posture (forced-match guards, declined `1/4` identification) is consistent with this conservative reading.

---

## (e) Cross-pollination notes (connections to other batch items)

- **A2 (Paper 21, quartic obstruction / `N=4` force law).** Paper 32 §7.3/§9.6 hangs the Einstein-like sourcing and the Higgs mass term on the **quartic** `T^(4) = m²_simplex` (the jerk / order-4 cumulant defect, M-supported). Paper II/IV's cubic `K̃` (`K³ = −K`) is order-3 only; the order-4 self-coupling is exactly where the frame series stops (Paper IV §7: "the cubic's cross-product factorization does not [exist for all N]; the metric does"). So **A2's quartic obstruction is the order-axis rung above where Paper II's `K`-algebra lives** — the frame series gives orders ≤3 cleanly, Paper 21/32 need order 4. Connection is real and *complementary* (II/IV floor, 21/32 ceiling), not redundant.

- **B1 (mechanics).** Paper 32 *is* the information-geometric-mechanics capstone (`Φ = log Z` as categorical effective action, Nambu–Fisher bracket, Filippov identity). Paper II §10.2/C3 explicitly flags "moving information geometry" (α-connections, Amari–Chentsov pointwise) as "the floor under the program's mechanics-on-the-categorical-simplex line." **So Paper II's open problem C3 is the differential floor that the mechanics line (B1) builds on** — but note it is the *information-geometric* differential structure (α-connections), again **not** the spatial grad/div/curl. The mechanics line wants C3, not the §8 PDE doors.

- **B2 (T11 overflow/leakage — the finite-grid/overflow thesis).** **Strongest cross-pollination.** Paper 30 (`Constrained Overflow`) is the corpus's explicit "finite grid + designated leakage channel" object: a typed residual calculus `R_W` where overflow is "the part of a whole that exceeds a projection," kept typed/bounded/falsifiable. Paper 32's `M` packet (cross-prime carry = gravity-adjacent leakage = `T^(4)|_M`) **is** that designated channel, instantiated arithmetically. And Paper II/IV give the *geometric* face of the same idea: the gauge line `𝟙` / harmonic sector is the "designated inert/overflow direction" the differential complex respects (Paper II §7.2, Poisson Fredholm obstruction = the gauge line; Paper IV `H^0 = ker L_0`). So three readings of one thesis: **B2/T11 (the abstract overflow), Paper 30 (typed residual calculus), Paper 32 `M`-packet (arithmetic instance), Paper II/IV gauge-line (geometric instance).** This is where the finite-grid/overflow compass genuinely unifies — and it does so *without* needing the κ=K coincidence or the curl doors.

- **C1 (RH apex).** Paper 32 §7 ties non-tachyonicity of the M-residual to **Paper 22 Weil positivity at the `P_2 = 2·3` row** (cubic order [P]; all-order [C] = RH). Paper 32.1's boundary constant `ζ(6)/(ζ(2)ζ(3))` is a zeta-ratio (Landau totient). So the unification line's residual *is* the RH-apex object at cubic order. **But:** Paper IV §E2 explicitly warns "the finite complete-complex spectrum supports no archimedean/apex structure by itself" — i.e., the frame series (II/IV) is finite and **cannot** reach the apex/archimedean limit where RH lives. So C1 connects to *Paper 32's* residual, not to Paper II/IV. Keep that boundary sharp.

- **C2 (quantum).** Paper 32 Face C / §6.3 builds QM as the canonical lift to `ℂP^{N-1}` (complex structure `J² = −I`, Born rule = toric moment map, `ħ` = Bures distinguishability rate). Paper 46 lives on the Bures lift `D(ℂ⁶)`. Paper II/IV touch this only at the centroid-Fisher / Hopf factor-of-2 (`d_FS = ½ d_FR`, the spin-½ angle doubling, Paper 32 §11.1). **The factor-of-2 is the one shared primitive** between the frame series and the quantum face — and notably it is the *same* factor of 2 that gives Paper 32.1 its radius-2 Hellinger sphere (hence `K=1/4`). So if there is any non-coincidental thread near the `1/4`, it is this upstream Fisher/Fubini-Study 2 — but as shown in (c) it produces `K`, not `κ`, so it does **not** rescue the κ=K coincidence.

---

## (f) Open follow-ups (ranked; honest about which are worth it)

1. **[Worth it — moderate] Formalize the reversibility/curvature-current correspondence.** Make precise the claim that Paper II §7.3 / Paper IV §5 `S+A` (Hodge-degree split, arrow `= b_1`) and Paper 32 FEP-3 `F = F_V + F_M` (conductor-packet split, arrow `= ∇F_M`) are two projections of one reversibility structure. Concretely: is the M-packet (cross-prime units) the harmonic/`b_1` sector of some complex on `ℤ/6`? If yes, the two splits are the same object; if no, they are parallel-but-distinct and the leverage stays at "shared dichotomy." This is the highest-value follow-up because it is the one non-aesthetic thread.

2. **[Worth it — testable] The `ℤ/2`-chirality vs `w_1`-orientation question.** Is Paper 32's external chirality bit (Face E, `μ_6/μ_3`, the KO `γ⁵` lock) realizable as a Stiefel–Whitney `w_1` holonomy of an orientation field over a varying-frame simplicial mesh (Paper IV §6, open problem C5)? A clean yes would upgrade (b.2) from loose to moderate; a clean no closes a tempting-but-empty door. Either way it is decidable. Caveat: respect the `ℤ/2`-ubiquity prior — demand a *mechanism*, not a coincidence of order.

3. **[Low priority — likely empty] Spatial-PDE doors on the lift.** One could ask whether Paper II's wave/heat/Poisson doors have any role on the Bures lift `D(ℂ⁶)` of Paper 46. Expectation: **no** — the lift's dynamics are unitary/Bures-geodesic, not governed by a spatial Laplacian on `H`. Recorded for completeness; do not invest unless a specific operator need surfaces.

4. **[Do not pursue] Any K=1/4 ↔ κ=1/4 construction.** Settled as coincidence in (c). The program already declined the stronger Bekenstein `1/4` echo; this weaker one should stay declined. Flag if it resurfaces.

---

### One-paragraph bottom line

The unification cluster (30/32/32.1/46) is an *arithmetic* program wearing a *physics* dictionary under a strict dimensional firewall; its dynamics run on information-geometric cumulant derivatives `∇^(n)Φ`, **not** on Paper II's spatial `grad/div/curl` — which the physics papers never invoke (grep-verified zero hits). So **Paper II is a differential substrate only notationally**, and the EM-wave/heat/Poisson/fluid/rotation doors have no socket in this line. **Paper IV is not a model of Paper 32's `(ℤ/6)^×` units gauge** — wrong N, wrong group, and a misleading `M`-letter collision; only a loose, flagged `ℤ/2`-chirality echo survives. The **K=1/4 vs κ=1/4 coincidence has no mechanism** (`κ = 1/N` at N=4 vs `K = 1/radius²` at radius 2; they diverge for every other row) and is declined a fortiori, consistent with the program already declining the stronger Bekenstein `1/4` echo. The **single thread above aesthetic** is the reversible/irreversible (curvature/current, `S+A`) split, which both lines build independently — moderate leverage as a shared organizing dichotomy. Tier: **aesthetic, with one moderate thread.** The real unifier across batch items is not the frame calculus but the **finite-grid/overflow thesis (B2)**, of which Paper 30's typed-residual calculus and Paper 32's `M`-packet are the two instances that matter.
