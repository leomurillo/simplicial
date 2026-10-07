# Map of Meaningful New Information — Simplicial + CBS Programs

Date: 2026-06-12. Tier tags: [P] proved (exact-arithmetic certificate or referee-grade
proof in text), [A] argued/conditional, [C] conjectural. Each item names its source
manuscript(s). This map lists only information judged *new relative to the literature* —
either a new theorem/identity, a new exact form of something previously known only
heuristically or asymptotically, or a new no-go that closes a route others still chase.

---

## A. The arithmetic spine (RH direction)

**A1. Apex unitary family and determinant.** [P] (N1, N2)
det U_N = i^(−C(N−1,2)), period 8 in N; U_N intertwines Helmert and Fourier frames on the
mean-zero hyperplane; entries in the compositum of multiquadratic and cyclotomic fields.
New: explicit closed form for an arithmetic-geometric object encoding the finite
character group.

**A2. Apex = archimedean operator identification.** [P] (N4, N5)
The edge operator (A−I)Φ is the Connes–Consani archimedean operator (5 exact matches);
Mellin symbol k̃(s) = [s/(1−s)]·(2π)^(−s)·e^(iπs/2)·Γ(s); reflection product
k̃(s)·k̃(1−s) = i/(2 sin πs) (Euler reflection, metaplectic quarter-turn). Even-sector
multiplier = e^(2iθ(t)) (Riemann–Siegel phase). New: a finite simplicial object
*generates* the archimedean place; the Γ-factor is not adjoined, it emerges.

**A3. Canonical de Branges target with five equivalent readings.** [P] (N6)
E_B = Ξ + iΞ′; RH ⟺ m_B = −Ξ′/Ξ Herglotz ⟺ u_B ≥ 0 ⟺ Li λ_n ≥ 0 ⟺ apex no-crossing
δ_max < 1/8. New: consolidates five program lines into one object; the 1/8-turn
threshold ( = √i = ζ₈, absorbed into ℤ[ζ₈], N4 Rem 4.3) is a finite cyclotomic landmark.

**A4. Cross-prime fusion criterion (Davenport–Heilbronn filter).** [P] (N9)
The invariant separating RH-true families from DH-type counterexamples is cross-prime
multiplicativity (Euler product), not the functional equation; DH fusion defect ≈ 1.081,
exact rank-1-vs-negative-square signature realized. New: names the exact structural
invariant any RH proof must use (necessary-not-sufficient; the "DH-sighted" criterion).

**A5. Pick kernel = resolvent Gram; index = off-line count.** [P] (N10)
P_B ⪰ 0 ⟺ RH; the Kreĭn–Langer negative-square count κ(P_B) = #{off-line zeros}. New:
exact index identification; kills fixed-signature (Castelnuovo–Hodge-style) arguments
over ℚ.

**A6. Non-normality = the archimedean phase; arrow = place.** [P] (N11 §5)
|k̃(½−it)|/|k̃(½+it)| = e^(πt) exactly; removing e^(iπs/2) restores normality. The
operator's antisymmetric part (the arrow) IS the archimedean place. New: pinpoints the
source of non-normality; explains why symmetric/order-2 instruments are blind to it
(bridge to CBS axis, item C4).

**A7. Boundary-condition no-go for Hilbert–Pólya.** [P] (N11 §5)
Cutoff dilation generator has deficiency indices (1,1) → arithmetic-progression
eigenvalues; no self-adjoint-extension phase can produce the log-growing zero density.
New: the HP realization must carry the archimedean potential, not boundary conditions.

**A8. Exact all-order transfer τ_n = (−1)^n.** [P] (N5 Thm 6.2; T2 Prop 6.2)
On block (ℤ/p)^×: apex cumulants κ_n = (−1)^(n−1)(n−1)!·a^n vs Hardy–Littlewood
connected weights −(n−1)!·a^n, a = 1/φ(p); transfer magnitude exactly 1, sign (−1)^n =
explicit-formula prime minus = Amari e↔m dual involution. New: closed form at ALL
orders where the literature has order-2 heuristics.

**A9. Per-prime keystone scaling identity.** [P, exact-certified] (probe_hl_apex_keystone)
HL connected n-tuple singular-series weight = apex conductor n-th cumulant, both
~ 1/φ(p)^n on squarefree support; order 2 EXACT (Fisher off-diagonal = twin-prime local
factor 1/(p−1)², numerator 1=1); order 3 magnitude exact with dual-connection sign.
New: the n-level-density arithmetic weight is *generated* by the conductor-block
dimension φ — the sharpest quantitative bridge from the program to mainstream
Rudnick–Sarnak / Bogomolny–Keating.

**A10. Apex generates the Li tower exactly.** [P, certified 2.3e-41] (probe_apex_generates_li)
λ_n = λ_n^arch (closed form, digamma) + λ_n^cond (pole + von Mangoldt); λ₁ =
−0.55412 + γ_E = 0.023096 (Keiper–Li). λ_n^arch > 0 for all n ≥ 8 → explicit zero-free
regions. New: an operator realization of Li's criterion in which positivity is manifest
per-zero (4 sin² ≥ 0, Bochner); primes enter additively.

**A11. Unconditional cubic positivity pieces.** [P] (diez, Unconditional-Positivity-Synthesis)
[A1′] the cubic Fejér class is non-empty (Beurling sampling construction); [A2′] an
off-line zero forces cluster sign c₂ ≤ −C* < 0 with explicit constant anchored by
L(½,χ₃) = 0.4808… (Iwaniec–Sarnak, LMFDB); U1–U6 unconditional positivity facts. New:
the first unconditional off-line "teeth" of the cubic Weil route.

**A12. Primorial Bombieri–Vinogradov schedule.** [C, partial [P]] (diez §3, N0 §6, Paper 43, Pascadi assessment)
θ₀(p_n) = 1 − C*/n, C* ≤ 2.80 (V/M crossover); classical BV discharges n ≤ 3 (θ=1/2);
Pascadi bilinear Kloosterman (arXiv 2511.08445, c^(−1/12)) lifts the unconditional level
to ≈ 0.583, discharging ≈ n ≤ 6; the θ₀ → 1 tail = primorial Elliott–Halberstam, open
for all current technology. New: an exact primorial-indexed schedule replacing
asymptotic level-of-distribution statements; CRT-cap [P] (smooth part = level 1/2 exact).

**A13. CCM open step pinned + Lemma 7.2 rate derived.** [P rate / RH-equivalent limit]
(CCM-2511-ConvergenceOpenStep, CCM-Lemma72-ProlateRate)
Connes–Consani–Moscovici 2511.22755: approximant positivity PROVEN (Carathéodory–Fejér);
RH ⟺ μ_λ ↓ 0 (one decreasing scalar). Their stated "main remaining obstacle"
(Lemma 7.2, prolate eigenfunction estimate ≤ c·λ^(−2)) is DERIVED here: bandwidth
c = 2πλ², harmonic-oscillator perturbation gives the λ^(−2) bulk rate, verified
(p = −2.004/−2.007/−2.010, err·c constant < 1%). Relocation: μ_λ = the Weil functional
on the prolate trial vector; the rate is the *precision*, not the difficulty. New: a
stated open lemma of a live mainstream program, closed at the bulk-rate level.

**A14. No-go theorems (routes closed).** [P]
(i) Tower theorem: additive/definite forms over ℚ are vacuous for RH (unique escape:
order 2 / 𝔽_q). (ii) No backward-entropy monotone for Λ ≤ 0 (de Bruijn–Newman). (iii) No
finite modular witness: [log Δ, P] = 2πiP forces P = 0 in finite dimension (P∞-A
Prop 8.3a). (iv) Prime side alone indefinite (T28: r_kρ_k > 1 all k ≥ 2). (v) The
(GBP)-as-identity is FALSE (|Σ|²/2π ≠ u_B; Bures geometry is zero-blind). (vi) Bulk
holonomy trivial per place (N13). (vii) Finite witnesses necessary-not-sufficient.
New: each closes a route the field still circles; (iii) is a quantized-commutator
obstruction with independent operator-algebra interest.

**A15. Lorentzian intersection metric / arithmetic causality.** [P over 𝔽_q; A over ℚ] (P∞)
The multiplicative second-order invariant is the intersection form, signature (1, ρ−1)
— Lorentzian, not Fisher; archimedean = timelike, primes = spacelike; RH = the
dominant-energy condition |a| ≤ 2√q; Λ = the metric tilt. New: explains the tower
theorem geometrically; opens "arithmetic energy condition" as an instrument class.

**A16. Archimedean Weil positivity = relative entropy.** [P] (N14, N15)
W_∞ ≥ 0 is the Gibbs/Fenchel–Young inequality of a log-convex log-partition (Γ);
prime side = log ζ (Euler = separable convex); the Weil form is difference-of-convex;
the global residue = Montgomery form factor at τ = 1. New: a conceptual answer to
Connes' Open Question 1 (why archimedean positivity holds), cited-theorems-only spine.

**A17. Place-completion keystone.** [P shadows] (P0)
ι = F² (involution = Fourier squared); tr(F) = Gauss sum (the naive "always √N" is
falsified — Gauss mod-4 trichotomy); finite positivity is free (F*F = I); over function
fields axioms A1–A5 are theorems and RH holds — the gap is exactly the archimedean
place. New: finite-adelic skeleton with the missing piece isolated by construction.

**A18. Smooth primorial family.** [P] (T33)
Unique canonical analytic interpolation of n ↦ P_n via Bohr–Mollerup log-convexity +
Wielandt; divisor-lattice constant tower recovers γ, ζ(k), log 2π; smooth Mertens
constant γ̃* ≈ 0.612 ≠ γ with bias = a Riemann-error integral. New: closes the
"Γ-function for primorials" gap (factorial:Γ :: primorial:this).

**A19. GUE / form-factor localization.** [P measured; localization] (probes; master state)
With 250 real zeros: pair-correlation hole, flat number variance, ramp→plateau form
factor; the open arithmetic content localized to the single point τ = 1 (diagonal /
off-diagonal boundary); ramp (τ<1) is free/unconditional. New: the program's open step
and Montgomery's conjectural region are the SAME point, stated operator-side.

---

## B. Interior tower (information geometry, finite mechanics)

**B1. Cumulant tower as effective action.** [P] (T2)
Φ = log Z generates: ∇Φ = position, ∇²Φ = Fisher metric ( = inertia), ∇³Φ =
Amari–Chentsov tensor ( = force/interaction), ∇⁴Φ = closure defect ( = mass/leakage).
New: one functional unifying the geometric objects; order 3 = first invariant invisible
to Riemannian geometry.

**B2. Cubic Noether theorem + forced gauge completion.** [P] (17, 18)
Exact conserved cubic energy on the categorical simplex; on the real simplex only the
Cartan u(1)² survives; the Bures/density-matrix lift of ℂ[ℤ/6] ≅ ℂ²⊗ℂ³ forces
su(2)⊕su(3) (Petz–Sudár SLD rigidity + CRT leg dimensions). New: nonabelian gauge
structure is *forced* by metric-algebraic rigidity, not chosen.

**B3. Quartic obstruction / Wick bifurcation.** [P] (21)
Order 4 is the first cumulant order with Gaussian (Wick-pairing) subtractions; exact
count of genuinely 3-prime connected quartic vertices on ℤ/30 (914). New: the n = 4
obstruction is structural, locating where pairwise machinery provably stops.

**B4. Conductor probe obstruction (Pontryagin divisor rule).** [P] (26)
A readout factoring through quotient C_N → C_k retains exactly conductor packets H_d,
d | k, and annihilates d ∤ k — sharp, no compromise. New: an exact "what a quotient
readout can ever see" law; the foundation of the CBS audit family.

**B5. Finite apex determinacy.** [P] (T12)
The infinite moment/cumulant tower ≅ ℝ[t]/(P_x): finite spectral data, Hankel rank
stabilizes at the number of distinct levels. New: finite perturbation theory with exact
closure — "finite arithmetic perturbation theory."

**B6. Exact simplicial renormalization.** [P] (T13)
RG flow = fusion-closure boundary adjunction; boundary integration = exact Schur
complement; fixed points = fusion-closed sectors. New: exact finite Wilsonian RG, no
perturbation series.

**B7. CRT tensor factorization: interaction information = entanglement.** [P] (T23)
For coprime N = N₁N₂, cross-prime interaction information vanishes ⟺ the state is a
tensor product in the CRT basis. New: identifies a classical (ANOVA) and a quantum
(entanglement) quantity exactly, in a fixed frame.

**B8. Monotone-metric fork.** [P-synthesis] (T24)
The quantum continuation of "what is additive?" is "which Petz monotone metric?";
Kubo–Mori is the unique dually-flat/additive member (not Bures). New: a selection
*criterion* (additivity/dual flatness) layered on the known Morozova–Chentsov–Petz
classification, with the fork located concretely in the apex generator's operator
ordering.

**B9. Projection-closure theory + typed residual calculus.** [framework, P examples] (31, 30, 29)
Closure-valid projections, typed overflow budgets, participation metrics; classicality
= commutative projection closure. New: a single quantitative frame for
classical/quantum/N-ary model validity.

**B10. Canonical involution + finite→archimedean Noether limits.** [P under PC1–PC4] (27)
Anti-unitary ι(ρ) = JρJ* implements s ↔ 1−s on the density-matrix manifold, Bures
isometry; finite Noether energies converge to the explicit-formula prime sum + R_∞.
New: spectral inversion realized finitely; the archimedean limit isolated as the
single analytic obligation.

---

## C. CBS / ML cluster

**C1. Conductor Blind Spot theorem.** [P] (ConductorBlindSpot.md, 34)
Fisher is block-diagonal across conductor packets while the cubic couples packets
exactly on k+ℓ+m ≡ 0 (mod n): every purely second-order instrument (K-FAC, natural
gradient, empirical Fisher, gradient attribution) is provably blind to cross-packet
structure. New: an exact finite *theorem* where the field has empirics; published
siblings now recognized (Amaral 2025 R(N=2)=0; LeJEPA Gaussian-uniqueness = order-2
corner; Neural LoFi §3.3; vec2vec/Strong-PRH 2505.12540 = deployed order-2, VSP=Gram, instance).

**C2. Apex identifiability tower (LeJEPA generalization).** [P] (CBS + apex_recovery suite)
Matching the cumulant tower (not an isotropic Gaussian) recovers a rank-r world at
order r; LeJEPA's Gaussian-uniqueness theorem (Klindt/LeCun/Balestriero 2605.26379) is
the rank-2/β=2 corner. Exact + approximate theorems harvested; empirical suite green.
New: extends the flagship SSL identifiability result one full axis (order), with exact
finite certificates. Constructive in-the-wild instance: vec2vec (Jha/Shmatikov/Morris
2505.12540) learns the universal latent unsupervised (their Strong PRH) from order-2
geometry alone (VSP = Gram); its perfect 8000-way matching vs sub-1 cosine fidelity is
this tower's order-2 floor made visible — existence-proof for C2, lossy residual for C1.

**C3. Gaussian boundary theorem.** [P] (CurvatureAndCurrent §3.2)
For a reversible diffusion the slow eigenfunction is affine ⟺ the latent law is
Gaussian; off-Gaussian, linear probes are lossy by exactly the eigenfunction curvature,
with measured bridge ν_D ∝ κ̃₃² (c = 0.0555). New: exact characterization of when
*linear* identifiability holds.

**C4. Irreversible Blind Spot theorem.** [P] (IrreversibleBlindSpot.md)
Single-encoder whitened-alignment objectives are functionals of S = (T+T*)/2 only; the
current A (arrow of time) is in the kernel — a world and its time-reverse have
identical loss landscapes. The two-encoder predictor objective's optimum is the SVD of
T and recovers the arrow; irreversibility gap Δ = Σσ − Σλ(S) ≥ 0 with equality iff
detailed balance. New: explains the BYOL/SimSiam predictor head as the *minimal* device
lifting a structural blind spot; gives a computable detailed-balance certificate.

**C5. Topological dimension of the arrow.** [P] (IBS §3.3–3.4)
The current space invisible to symmetric objectives has dimension = cycle rank β₁(G)
(graphs) / first Betti number b₁(M) (manifolds, via Hodge). New: exact topological
count of learnable cyclic/periodic latent content.

**C6. Curvature–current orthogonality.** [P] (CurvatureAndCurrent §5)
The CBS (curvature, cumulant) axis and the IBS (current, reversibility) axis are
independent components of T = S + A — zero cross-talk at machine precision. New: the
two blind spots are a complete two-axis audit, not one phenomenon.

**C7. Exact Stuart–Landau / cubic identity.** [P] (CurvatureAndCurrent §3.4)
γ = −(1/8)·[spin-3 part of the Amari–Chentsov cubic] — the symmetry-breaking
coefficient of the limit cycle is an exact contraction of ∇³Φ. New: exact constant
where bifurcation theory has scaling heuristics; bridges CBS ↔ simplicial interior.

**C8. Audit family.** [P theorems + C pre-registered] (36, 40, 45, 47, T16)
Base-N shortcut audit (survival ratio σ lower-bounds algebra-mediated computation;
Llama-3.1-8B anchor σ = 0.458); CCSAE (packet-pure SAE features, reconstruction cost
gap = exactly the Paper-26 obstruction); layerwise packet spectroscopy; arithmetic
decoupling V ⊥ M at all orders [P]. New: retraining-free, certificate-grade
interpretability/safety audits derived from exact theorems.

**C9. Poole-OTG bridge theorems.** [P] (Poole-OTG-Bridge-Theorem)
Channel lift, reversible dilation, exact closure/leakage test, current audit,
dimensionless firewall — deterministic CA dynamics lifted to quantum language with
exact certificates. New: rigorous classical→quantum bridge with falsifiers.

---

## D. Exterior / physics-facing

**D1. One functional, four forces (interior [P] core).** (32-v0.3)
Space = mass theorem (second cumulant is simultaneously ruler and inertia);
time/energy/gravity = one Noether structure (gravity = closure defect under
projection); exact ℤ/6 closure certificate (A₂ cubically isolated; residual exactly on
the mixed conductor-6 packet M); tree-level sin²θ_W = 3/8 and one-generation
hypercharge spectrum Y = P₂/2 − P₃/3 [A/C]; dimensional selection Q = 4 by two routes
[A]. New: a finite categorical substrate generating Lagrangian-field-theory structure,
with a strict dimensional firewall (pure numbers only).

**D2. Hartle–Hawking signature as V⊥M shadow.** [P finite model] (46, 47)
The Lorentzian-V / Euclidean-M sub-bundle split on D(ℂ⁶) realizes the no-boundary
signature structure at 3.2e-16 precision. New: first finite-arithmetic model of the
signature phenomenon (correspondence-grade, firewalled).

---

## E. Methodology (cross-cutting, exportable)

**E1. GPD operating procedure.** (35) Fenced "delusional" generation → pre-registered
matched-pair falsifiers (Davenport–Heilbronn as the canonical matched pair) →
deterministic exact-arithmetic settlement; tier hygiene [P]/[A]/[C]; failures retained.

**E2. Signature-not-conditioning lesson.** [P] Exact Sylvester-invariant signature
computations (sympy ℚ/ℚ(ζ_N)) versus float conditioning: the "marginality wall" was a
float artifact; all RH probes now run exact. Exportable to any positivity-adjacent
computation.

**E3. Matched-pair falsifier design.** The DH-filter (a family sharing every soft
property but failing the conclusion) as a *requirement* on any proposed mechanism —
this is what repeatedly localized the open step and killed forced bridges.
