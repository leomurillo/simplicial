# Survey: Open Problems Addressable by the Program's New Information

Date: 2026-06-12. Cross-references `01_NewInformationMap.md` items (A1–A19, B1–B10,
C1–C9, D1–D2, E1–E3). Each entry: the problem, its status in the literature, which new
information bears on it, what "closing" would mean, and an honest verdict.

Verdict classes:
- **CLOSED-PENDING-WRITEUP** — the mathematical content is in hand at [P]; remaining
  work is hardening/refereeing.
- **CLOSABLE** — a sharply posed target our levers genuinely address; bounded,
  realistic program.
- **PARTIAL** — we can close a meaningful sub-case or supply a recognized missing
  ingredient, not the full problem.
- **EQUIPPED-OPEN** — the toolkit is uniquely adapted and has reduced the problem, but
  the residual is of the problem's own (extreme) hardness.
- **BLOCKED / DEFERRED** — assessed; structural obstruction identified; not a target.

---

## I. Analytic number theory

### 1. Riemann Hypothesis
**Status:** Open since 1859; the program's central target.
**Our levers:** the entire spine A1–A19: the reduction RH ⟺ one scalar (μ_λ ↓ 0, CCM
Cor 3.8) ⟺ arch-domination ⟺ u_B ≥ 0 ⟺ energy condition, with the archimedean half a
theorem (A2, A16), local Frobenius data in hand, the open content localized to the
single point τ = 1 (A19), and seven shortcut classes closed by exact no-gos (A14).
**Closing means:** proving the multiplicative-archimedean positivity over ℚ (front-end:
complete monotonicity / positive-energy on the prolate platform; endgames: unitary CFT
on the scaling site, or 𝔽₁ Hodge positivity).
**Verdict: EQUIPPED-OPEN.** The reduction is real and quantifiable (from "prove RH" to
"prove one decreasing scalar has limit 0," with every equivalent face named); no team is
better equipped; the residual is RH-hard by all the program's own no-go theorems.

### 2. Generalized RH at primorial conductors (GRH_N) — incl. height-bounded variants
**Status:** Open; the program's structural reduction chain (Apex Lemma_HJ ⟺
GRH-at-P_n) is assembled at [C] (GRH-Apex-Integration).
**Our levers:** A11 (cubic teeth, χ₃ anchor), A12 (BV schedule), A13, the induction
machinery T22.1/T22.3; height-bounded GRH at fixed primorial modulus
(HeightBoundedGRH-PrimorialN210) is *finitely checkable* with exact certificates (E2).
**Verdict: PARTIAL** (height-bounded, fixed-modulus statements are certifiable now;
full GRH_N is item-1-hard).

### 3. CCM Lemma 7.2 — prolate eigenfunction perturbation rate (Connes–Consani–Moscovici, arXiv 2511.22755)
**Status:** Stated by CCM as "the main remaining obstacle" of the live zeta-spectral-
triples route; the field's own formulation: rigorous convergence would establish RH.
**Our levers:** A13 — the λ^(−2) bulk rate is DERIVED (bandwidth c = 2πλ², first-order
harmonic-oscillator perturbation) and verified to <1% (CCM-Lemma72-ProlateRate-Draft1);
the boundary regime matches the classical γ^(−3/4) literature; plus the variational
relocation μ_λ ≤ ⟨k_λ, A_λ k_λ⟩/‖k_λ‖² identifying μ_λ as the Weil functional on the
prolate trial vector.
**Closing means:** a referee-grade proof of the eigenfunction estimate at the stated
rate (the lemma as posed — NOT the §7 convergence conjecture, which is RH).
**Verdict: CLOSED-PENDING-WRITEUP** — with the honest caveat published alongside: the
rate is the precision of the evaluation, not the RH content; closing 7.2 advances the
CCM program without closing RH.

### 4. Montgomery pair correlation / Rudnick–Sarnak n-level densities / Bogomolny–Keating off-diagonal
**Status:** Conjectural beyond the τ < 1 ramp (Montgomery 1973); the off-diagonal
(τ ≥ 1) prime regime is the recognized frontier; n-level arithmetic terms known
conditionally on HL k-tuples.
**Our levers:** A8 (exact all-order transfer τ_n = (−1)^n), A9 (per-prime keystone:
n-level arithmetic weight = conductor-block cumulant, 1/φ(p)^n, order 2 EXACT = the
twin-prime local factor), A19 (τ = 1 localization), B1 (the cumulant tower the identity
lives in).
**Closing means (bounded target):** a rigorous theorem deriving the magnitude-1 /
dual-sign transfer from the explicit formula at every order — i.e., "the
Rudnick–Sarnak n-level arithmetic factor IS the order-n cumulant of the conductor
block," term-by-term, all n, unconditionally. (Crossing τ = 1 — the closure — is item 1.)
**Verdict: CLOSABLE** (the term-by-term identity is algebraic, verified exactly at
n = 2, 3 per prime, with the mechanism identified; it is new structure for a mainstream
hierarchy).

### 5. Li's criterion — operator realizations and explicit zero-free regions
**Status:** Li 1997 / Bombieri–Lagarias 1999; positivity of all λ_n ⟺ RH; no known
generating operator with manifest per-zero positivity.
**Our levers:** A10 (apex generates the Li tower exactly, arch + von-Mangoldt split,
certified 2.3e-41; λ_n^arch closed form, positive for n ≥ 8); E2.
**Closing means (bounded target):** publishing the operator realization + the explicit
λ_n^arch-driven zero-free region (n* ~ (γ²/δ)·log → explicit region). Full Li
positivity = RH.
**Verdict: PARTIAL** (the realization theorem and a new explicit zero-free-region
mechanism are in hand; competitiveness with Vinogradov–Korobov regions must be checked
honestly before claiming strength).

### 6. de Bruijn–Newman constant: Λ ≤ 0
**Status:** Λ ≥ 0 proven (Rodgers–Tao 2018); Λ ≤ 0 ⟺ RH; Λ ≤ 0.2 (Polymath15).
**Our levers:** A14(ii) — a structural no-go: no backward-entropy/heat-flow monotone
can prove Λ ≤ 0 (the RH content is boundedness/energy-condition-shaped, not
monotone-shaped); the CCM μ_λ is the correct replacement monotone with open LIMIT.
**Closing means:** the no-go itself is publishable as a negative theorem redirecting
the field; Λ ≤ 0 itself is item 1.
**Verdict: PARTIAL** (negative-result publication; genuine field value).

### 7. Level of distribution on primorial / smooth moduli (Bombieri–Vinogradov beyond 1/2; primorial Elliott–Halberstam)
**Status:** BV gives θ = 1/2; beyond-1/2 known only on special factorizable moduli
(BFI, Zhang, Maynard, Pascadi 2511.08445 — live frontier ≈ 0.515–0.583 depending on
regime).
**Our levers:** A12 (the exact θ₀(p_n) = 1 − C*/n schedule; CRT-cap [P]; Pascadi
integration with certified dispersion bookkeeping; semi-primorial lever [P]/[C]); A18
(smooth primorial family for the interpolation); the assessments
(MatomakiRadziwill-EHTail, Pascadi2511) mapping exactly which technology moves which n.
**Closing means (bounded target):** unconditional θ > 1/2 through n ≈ 6–7 primorial
rows with explicit constants — a recognizable analytic-NT advance on the most
factorizable moduli family. The θ₀ → 1 tail is EH-strength: NOT claimed.
**Verdict: CLOSABLE (bounded regime); EQUIPPED-OPEN (tail).**

### 8. Hardy–Littlewood k-tuples / twin primes — structural reformulation
**Status:** Open; singular series conjectural at every order.
**Our levers:** A9 (order-2 exact identity: Fisher off-diagonal = twin-prime local
factor — a new *interpretation* of the singular series as information-geometric
curvature of the conductor block), A8, A12 (the binding obligation localized to the BV
level C* ≤ 2.80, NOT to HL itself — same single obligation as Goldbach mod-8 three-arc
structure, per the Washburn parallel).
**Verdict: PARTIAL** (reformulation + localization; the analytic obligation is item 7's
tail).

### 9. Patterson conjecture (cubic Gauss sums, explicit constant)
**Status:** X^(5/6) exponent known (Heath-Brown–Patterson); the constant requires GL(3)
metaplectic residue data; recent activity (Dunn et al.).
**Our levers assessed:** T27 cubic Gauss sums specialize exactly to Patterson's g(π),
but the program aggregates over FIXED cubic conductor; Patterson varies the conductor.
The distinctive lever (G³ ≠ I) acts on an orthogonal axis.
**Verdict: DEFERRED** (PattersonConjecture-Simplicial-Assessment: alignment real,
lever orthogonal; would require GL(3) metaplectic content the framework lacks).

### 10. Birch–Swinnerton-Dyer (CM, j = 0 sub-case)
**Status:** Open (Clay); CM cases most accessible classically.
**Our levers assessed:** cubic Kummer clock over ℚ(ζ₃).
**Verdict: BLOCKED** (BSD-Simplicial-Assessment: conductor mismatch; infinity-type
(1,0) Hecke characters outside the finite-order aggregation; positivity lives at s = ½,
BSD content at s = 1). Tractable sub-target identified instead: finite-order cubic
Hecke class-number formula at primorial cubic conductor.

### 11. Iwasawa invariants for CM curves
**Verdict: BLOCKED** (IwasawaCM-Simplicial-Assessment: the program is archimedean/ℂ-
side; Iwasawa is p-adic; no interpolation bridge exists; building one is a multi-year
Katz/Hida-scale program). Retained sub-target: ℂ-side primorial cubic Hecke L-value
moment identity (from T27 Thm F).

### 12. Cubic moments of Dirichlet L-functions M₃(T,q)
**Verdict: DEFERRED** (CubicMomentBounds-Simplicial-Assessment: M₃ is a value-spectrum
L¹-type statistic; the cubic bilateral is intrinsically L²/Parseval — G³ near-scalar,
no new analytic content; Cauchy–Schwarz already tight to 4.7% at small primorials).
Right cubic target instead: [A3′] at the cubic Kummer base (BV for Hecke L-functions
of ℚ(ζ₃) at primorial conductor).

### 13. Canonical interpolation of the primorial ("a Γ for primorials")
**Status:** Folklore gap (factorial has Γ via Bohr–Mollerup; primorial had no canonical
smooth family).
**Our levers:** A18 — existence + uniqueness proved, constant tower computed, smooth
Mertens bias identified as a Riemann-error integral.
**Verdict: CLOSED-PENDING-WRITEUP** (T33 is the paper; a clean standalone special-
functions/analytic-NT contribution).

### 14. Collatz conjecture
**Our levers:** the quanta object (q, n, r) — path-dependent residue arithmetic is its
native home; Collatz charge identity welded.
**Verdict: EQUIPPED-OPEN at best; honestly a LENS, not an instrument** (quanta.md's own
audit). Not a survey priority.

---

## II. Quantum information / information geometry

### 15. Quantum Chentsov problem — what selects THE quantum Fisher metric
**Status:** Chentsov uniqueness fails quantumly; Petz classified the monotone family
(1996); "which member is canonical, and by what operational principle" remains an
active foundational question.
**Our levers:** B8 (additivity/dual-flatness selects Kubo–Mori — with the fork located
concretely in the operator-ordering of the apex generator); B2 (SLD/Bures rigidity:
*conservative flow* selects Bures — so the two principles select DIFFERENT members,
which is itself the sharp statement); A14/A15 (the additive-vs-multiplicative split
behind it); the N0-route Chentsov caveat (classical towers: all monotone metrics agree
— the lever is the encoding functional, not the metric).
**Closing means:** a selection-principles theorem: each operational axiom (additivity,
dual flatness, conservative dynamics, monotonicity under coarse-graining of the
specific channel class) provably selects its member, with the fork exactly located.
**Verdict: CLOSABLE** (as a sharpening/organization theorem over Petz's
classification; risk: parts may be judged synthesis rather than new — the new content
is the located fork + the two-principles-two-metrics theorem).

### 16. Quantum-to-classical transition / preferred basis (decoherence program)
**Status:** Open conceptual program (Zurek et al.).
**Our levers:** B9 (classicality = commutative projection closure, quantified by typed
overflow); B7 (entanglement = cross-prime interaction information); the DBT26 bridge
(state-dependent single-prime vs state-independent cross-prime classicalization,
landed in Papers 26/31/32/44/48).
**Verdict: PARTIAL** (a quantitative finite-model frame with exact certificates; not a
resolution of the full program).

### 17. Kochen–Specker contextuality classicalization thresholds
**Status:** Active (DBT26, arXiv 2604.24735: depolarizing-channel classicalization).
**Our levers:** the two-tier (single-prime/cross-prime) classicalization dichotomy
gives structure DBT26 lacks; finite exact certificates available.
**Verdict: PARTIAL/CLOSABLE** (a joint refinement paper is a realistic bounded target).

---

## III. Machine learning theory

### 18. SSL identifiability beyond Gaussian/linear (the LeJEPA-class question)
**Status:** Live frontier: LeJEPA (Klindt/LeCun/Balestriero 2605.26379) proves Gaussian
uniqueness ⟹ linear identifiability — order 2 only; nonlinear-ICA identifiability
results require auxiliary variables; "what does matching MORE than second order buy"
is open and explicitly flagged (Neural LoFi 2605.13612 §3.3 "Beyond second order").
**Our levers:** C2 (apex identifiability: rank-r recovery at cumulant order r, exact +
approximate theorems, green empirical suite), C3 (Gaussian boundary theorem — the
exact stratum where linear probes suffice), C1 (the blind-spot mechanism explaining
WHY order 2 cannot see the rest), B5 (finite determinacy bounding the tower needed).
**Closing means:** the theorem package for the categorical/rank-r class with exact
finite certificates and the planning corollary.
**Verdict: ALREADY PUBLISHED** (corrected 2026-06-13). The result is Zenodo
10.5281/zenodo.20502084, "Beyond the Conductor Blind Spot: Eigenfunction
Identifiability and Planning in Non-Gaussian Worlds" (2026-06-01), plus the LeJEPA
relation in published CBS §7.11–7.12. NOTE: the "rank-r at order r / LeJEPA order-2
corner" slogan used in earlier drafts of this survey is a framing the published
manuscript DELIBERATELY DECLINED (internal log, locked 2026-05-31: do not frame as
"generalising LeJEPA"; do not trade on author names) and partly CONFLATES its two
load-bearing towers — (D) dynamical/eigenfunction recovery vs (S)
distributional/cumulant grading, which coincide only at the Gaussian. Do not
reintroduce "recovery order = Hankel rank." Genuine remaining ASAP opportunities
(both in the manuscript's own TODO): (i) anisotropy → signed-permutation
identifiability as a standalone short paper (disentanglement without rotation
ambiguity); (ii) the §7 interpretability claim made quantitative — matched
linear-vs-eigenfunction probe on middle-layer rogue dims, for which the audit-κ
retained per-layer residual streams + the P2 lens-vs-probe gap are now the substrate.

### 19. Why predictor heads / asymmetry in BYOL–SimSiam–JEPA work
**Status:** Open theory question since 2020 (collapse-avoidance explanations are
dynamical, not representational).
**Our levers:** C4 — single-encoder objectives are provably functionals of the
symmetric part only; the predictor is the minimal lift recovering the current; C5
(what is recovered = β₁-dimensional); C6 (orthogonal to the cumulant axis).
**Closing means:** the representational (not dynamical) theorem for the categorical/
Markov class + the GCP-trained E11 falsifier.
**Verdict: CLOSABLE** (math [P]; the trained two-encoder falsifier E11 ran on GCP
2026-06-02 and PASSED — empirically complete).

### 20. Faithfulness of interpretability artifacts (probes, logit lens, SAEs, circuit discovery)
**Status:** Recognized crisis-grade open problem; DCD (2605.09129) measures 87%
mixed-faithfulness empirically; no exact obstruction theory exists in the field.
**Our levers:** B4 (Pontryagin divisor rule — exact law of what quotient readouts can
see), C1 (CBS), C8 (base-N audit σ, CCSAE with certified packet purity and the
reconstruction-cost gap EXACTLY equal to the obstruction; layerwise spectroscopy with
pre-registered predictions; Llama-3.1-8B anchors measured).
**Closing means:** "faithfulness failures of quotient-mediated interpretability are
governed by an exact divisor law, certified by construction in CCSAE" — turning an
empirical crisis into a theorem + audit-instrument family for the cyclic/algebraic
task class.
**Verdict: CLOSABLE** (theory [P]; pre-registered experiments specified; the bounded
claim is for structured label algebras, not all interpretability).

### 21. Structural limits of second-order optimization (K-FAC / natural-gradient class)
**Status:** Empirical folklore ("second-order methods miss feature-learning effects");
no exact statement.
**Our levers:** C1 + B1 + B3 (the first coupled order is 3; order 4 Wick bifurcation).
**Verdict: PARTIAL/CLOSABLE** (the exact finite statement exists [P]; scope = the
categorical-head class; extending beyond is open).

### 22. Transformer architecture constants (why h = 8; attention sinks)
**Our levers:** C8-family: frame-cost minimization theorem reproducing Vaswani (8,64)
[P theorem + pre-registered test]; attention-sink Γ-law [C, protocol defined].
**Verdict: PARTIAL** (elegant variational account; empirical settlement pending;
high-risk/high-novelty for the Γ-law).

---

## IV. Nonequilibrium statistics / physics

### 23. Inferring irreversibility (entropy production) from partial/symmetric observations
**Status:** Active open area in stochastic thermodynamics (TUR-based estimators are
bounds, not identities; "which observables can certify the arrow" is open).
**Our levers:** C4 (Δ = Σσ − Σλ(S) ≥ 0, = 0 iff detailed balance — an exact computable
certificate), C5 (the arrow's dimension = β₁/b₁ — exact topological count of
certifiable current content), C6, C9 (current audit on empirical data), B10/A6 (the
same symmetric-blindness mechanism appearing as the archimedean arrow).
**Closing means:** the theorem pair (certificate + dimension) for finite Markov /
diffusion classes, with the falsifier suite — a definitive contribution to
detailed-balance testing.
**Verdict: CLOSABLE.**

### 24. Hilbert's 6th-flavored program: deriving field-theoretic structure from a finite substrate
**Status:** Open-ended foundational program.
**Our levers:** D1 (space=mass; time/energy/gravity one Noether structure; ℤ/6 closure
certificate; sin²θ_W = 3/8 tree-level; dimensional selection Q = 4), D2, B2, B6.
**Verdict: EQUIPPED-OPEN, long horizon** (interior theorems are [P]; the physics
identification is correspondence-grade [A/C] behind the dimensional firewall; the
falsifiable near-term items are the SM pure-number predictions).

---

## Summary table

| # | Problem | Verdict | Primary levers |
|---|---------|---------|----------------|
| 3 | CCM Lemma 7.2 rate | CLOSED-PENDING-WRITEUP | A13, E2 |
| 13 | Canonical primorial interpolation | CLOSED-PENDING-WRITEUP | A18 |
| 18 | SSL identifiability tower | CLOSED-PENDING-WRITEUP / CLOSABLE | C2, C3, C1 |
| 4 | n-level ⟷ cumulant transfer theorem | CLOSABLE | A8, A9 |
| 20 | Interpretability faithfulness | CLOSABLE | B4, C1, C8 |
| 23 | Irreversibility inference | CLOSABLE | C4, C5, C6 |
| 19 | Predictor-head theorem | CLOSABLE | C4, C5 |
| 7 | Primorial BV (bounded n) | CLOSABLE (bounded) | A12 |
| 15 | Quantum metric selection | CLOSABLE (synthesis-risk) | B8, B2 |
| 17 | KS classicalization refinement | PARTIAL/CLOSABLE | B9, DBT26 bridge |
| 5 | Li operator realization | PARTIAL | A10 |
| 6 | dBN no-go publication | PARTIAL | A14 |
| 8 | HL k-tuples reformulation | PARTIAL | A9, A8 |
| 2 | Height-bounded GRH_N | PARTIAL | A11, A12, E2 |
| 16 | Quantum-to-classical | PARTIAL | B9, B7 |
| 21 | Second-order optimizer limits | PARTIAL/CLOSABLE | C1, B3 |
| 22 | Transformer constants | PARTIAL | C8 |
| 1 | RH | EQUIPPED-OPEN | A1–A19 |
| 24 | Hilbert-6th program | EQUIPPED-OPEN | D1, D2 |
| 14 | Collatz | LENS only | quanta |
| 9 | Patterson constant | DEFERRED | (T27 orthogonal) |
| 12 | Cubic moments M₃ | DEFERRED | (L² vs L¹) |
| 10 | BSD (CM) | BLOCKED | (3 obstructions) |
| 11 | Iwasawa CM | BLOCKED | (ℂ vs p-adic) |
