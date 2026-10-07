# Top 7: Open Problems the Toolkit Has the Highest Possibility of Solving

> **Addendum (same day):** this ranking was cross-checked against canonical
> open-problem lists with web verification — see `04_FamousListsCrossCheck.md`.
> Order unchanged; items 2, 4, 5 strengthened by named problems in the field's own
> agenda papers (Sharkey et al. 2501.16496; FDIG 2025 2509.06989); quantum
> monotone-metric selection upgraded among honorable mentions (it answers Ito's named
> FDIG 2025 problem); Smale #18 added as honorable mention via T16/T19.

Date: 2026-06-12. Ranked from `02_OpenProblemsSurvey.md` by composite score
**P(closure) × significance**, where P(closure) is the honest probability that the
program settles the *stated bounded target* (not a grander superset) within ~1–2
working years, and significance is external recognition value. Raw P(closure) is given
per entry so the two factors stay visible. Methodology assumed throughout: GPD
(fenced generation → pre-registered matched-pair falsifiers → exact-arithmetic
settlement), tier hygiene, signature-not-conditioning exact computation.

---

## 1. CCM Lemma 7.2 — the prolate eigenfunction rate (Connes–Consani–Moscovici, arXiv 2511.22755)

**P(closure): ~0.85.** Bounded target: a referee-grade proof of the eigenfunction
perturbation estimate max|h_{n,λ} − h_n| ≤ c·λ^(−2) that CCM name as "the main
remaining obstacle" of the zeta-spectral-triples route.

**Why us:** the content is already derived and verified
(`CCM-Lemma72-ProlateRate-Draft1.md`): rescaling exposes Slepian bandwidth c = 2πλ²,
the λ^(−2) is first-order harmonic-oscillator perturbation theory — classical
machinery, exactly checked (exponents −2.004/−2.007/−2.010, err·c constant < 1%), with
the boundary regime matched to the Morrison–Slepian γ^(−3/4) literature. We also hold
the variational relocation (μ_λ = the Weil functional on the prolate trial vector)
that tells the field what closing 7.2 does and does not buy.

**Remaining work:** uniformity in n; rigorous error bounds replacing the verified
numerics; the honest companion statement (the rate is evaluation precision, not the RH
content). **Risk:** low — the only real risk is that CCM close it themselves first;
even then the variational relocation stands as independent content.

---

## 2. SSL identifiability beyond second order — the disentanglement spin-off

**CORRECTION (2026-06-13):** the core result is ALREADY PUBLISHED — Zenodo
10.5281/zenodo.20502084, "Beyond the Conductor Blind Spot: Eigenfunction
Identifiability and Planning in Non-Gaussian Worlds" (2026-06-01), with the LeJEPA
relation in published CBS §7.11–7.12. The earlier "rank-r at order r / LeJEPA order-2
corner" headline was an optimistic mis-framing: the published manuscript deliberately
declines the "generalising-LeJEPA" framing and the slogan conflates its two towers
(D: eigenfunction recovery; S: cumulant grading). So this slot is NOT a fresh
identifiability paper. The live, bounded ASAP target is the spin-off the manuscript's
own TODO names:

**P(closure): ~0.75.** Bounded target: **anisotropy → signed-permutation
identifiability as a standalone short paper** — disentanglement without rotation
ambiguity, the practical lever §7 of "Beyond" flags but does not develop; plus the
companion quantitative interpretability datum (matched linear-vs-eigenfunction probe
on middle-layer rogue dims).

**Why us:** the theory is already proved and published; the spin-off is a focused
restatement + one targeted experiment, and the audit-κ run just delivered its
substrate (per-layer BF16 residual streams + the P2 lens-0.638-vs-probe-0.356 gap at
a single layer = a measured linear-vs-richer-readout separation). **Risk:** low —
small scope, theory done; the only question is whether the signed-permutation lever is
strong enough to stand alone or is better as a section in the interp paper (item 4).

---

## 3. The n-level ⟷ cumulant transfer theorem (Rudnick–Sarnak arithmetic factors from the explicit formula)

**P(closure): ~0.6.** Bounded target: an unconditional, term-by-term theorem that the
arithmetic factor of the n-level density at full resonance equals the order-n cumulant
of the conductor block (ℤ/p)^×, with magnitude exactly 1/φ(p)^n and sign (−1)^n given
by the explicit-formula minus / Amari dual involution — at every order n and every
prime, on squarefree support.

**Why us:** the identity is verified EXACTLY at orders 2 and 3 per prime
(probe_hl_apex_keystone; order 2 is the twin-prime local factor, numerator 1 = 1); the
closed-form transfer τ_n = (−1)^n is proven all orders (N5 Thm 6.2); the prime-power
test confirmed the conductor-block identification (φ on squarefree = HL product
exactly). What remains is algebraic derivation from the explicit formula
(Γ-factor weights + the n-fold resonance combinatorics), not new analytic estimates.
**Significance:** high — it welds the program's cumulant tower to the mainstream
n-level-density hierarchy and gives the singular series an information-geometric
meaning. **Risk:** moderate — the bookkeeping at general n is intricate; the
matched-pair falsifier (a wrong collaborator formula already caught and killed at
order 3) shows the discipline works here.

---

## 4. Faithfulness obstructions for interpretability artifacts (probes / logit lens / SAEs)

**P(closure): ~0.7.** Bounded target: the exact obstruction theory for
quotient-mediated interpretability on structured (cyclic/algebraic) label classes —
the Pontryagin divisor rule (Paper 26) as the governing law, CCSAE certificates where
the reconstruction-cost gap EQUALS the obstruction (no more, no less), the base-N
audit σ as a deployment-grade safety primitive — validated on the pre-registered
Llama/Mistral suites.

**Why us:** the field has an acknowledged crisis (DCD's 87% mixed-faithfulness) and
zero exact theory; our theorems are at [P] with measured anchors already in hand
(layer-28 vs logits packet fractions; σ = 0.458 base-10 shortcut finding). The
methodology (pre-registered falsifiers, exact certificates) is itself the
differentiator in an empirics-driven field. **Remaining work:** run the pre-registered
suites (local exact gate + GCP for anything torch); write the consolidated
obstruction-theory paper. **Risk:** moderate — empirical components could come back
messy; the theorems stand regardless, but the claim must then be narrowed.

**Update 2026-06-12 (audit κ executed; Paper 36 §3/§3.A settled):** the GPU half of the
pre-registered suite ran on Llama-3.1-8B + Mistral-7B-v0.3 (months, weekdays; ≈$0.40).
The empirical core for the consolidated paper is now in hand, three pieces:
(i) the **instrument-conflation exhibit** — at the same layer of the same model the
full-label trained probe reads f₁₂ = 0.356 while the frozen-unembedding lens reads
0.638 (reconciled to 6e-5 against Paper 26's own saved residuals): the readout
quotient determining what you see, measured in the wild; (ii) **cross-model V/M
propagation** (P9: K-branch on BOTH models, significant — 2000-resample bootstrap
gives min(σ_V)−max(σ_M) > 0 in 100% of resamples on each; the earlier "Llama
joint-on-disjoint / H₂ defector" was a point-estimate artifact, refuted by the bands —
real finding is a 3-level V ladder on Llama M<H₂<{H₃,H₄}); (iii) the **replicated crystallization-jump profile**
(single mid-late jump + overshoot + decline on both models, refuting the
monotone-late prior, P1). Failures retained: P3's ℓ* statistic and P4's fraction
metric are apparatus defects to fix in any v2 pre-registration; digits arm has no
pre-registered prompt set. Anchors and ledger:
`empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md`. NOTE for the
CCSAE leg: the retained residual captures are last-token only — sufficient for
P6/P7 offline settlement, but if CCSAE training wants full-sequence activations a
fresh (similarly cheap) capture run is needed.

---

## 5. The Irreversible-Blind-Spot package: detailed-balance certification + the predictor-head theorem

**P(closure): ~0.65.** Bounded target: (i) the certificate theorem Δ = Σσ − Σλ(S) ≥ 0
with equality iff detailed balance, plus the arrow-dimension theorem
(dim of certifiable current = cycle rank β₁ / Betti b₁) for finite Markov and
diffusion classes — a definitive contribution to irreversibility inference in
stochastic thermodynamics; (ii) the representational theorem that single-encoder SSL
objectives are functionals of the symmetric part only, with the predictor head as the
minimal lift (answering WHY BYOL/SimSiam asymmetry works, structurally rather than
dynamically).

**Why us:** all theorems [P] with green exact certificates (E9–E16); curvature–current
orthogonality proven (the audit is two independent axes, complete); the trained
two-encoder falsifier E11 ran on GCP 2026-06-02 and PASSED (correction to the first
draft of this file, which listed it as pending) — the package is fully validated and
`CurvatureAndCurrent.md` is already assembled as the unified submission.
**Risk:** moderate —
stochastic-thermodynamics literature on entropy-production estimation is large; the
novelty claim must be positioned precisely (exact certificate + topological dimension
count vs existing TUR-type bounds).

---

## 6. Level of distribution beyond 1/2 on primorial moduli — the bounded-n regime

**P(closure): ~0.45.** Bounded target: unconditional θ > 1/2 with explicit constants
through primorial rows n ≈ 6–7, by integrating Pascadi's bilinear Kloosterman
(c^(−1/12)) with the program's CRT-cap [P] and certified dispersion bookkeeping —
making the exact schedule θ₀(p_n) = 1 − C*/n rigorous in its first rows.

**Why us:** primorial moduli are the maximally factorizable family — exactly where
Pascadi-type savings bite hardest — and the program owns the only primorial-indexed
schedule and the certified semi-primorial lever. This is mainstream analytic NT where
a bounded, recognizable advance is available without touching the EH-strength tail
(θ₀ → 1), which we explicitly do NOT claim. **Risk:** moderate-high — dispersion
efficiency κ ≥ 2/5 must be earned, not assumed; the Paper-43 v0.1 θ₀(5) mis-derivation
(caught, flagged) shows the failure mode; specialist-grade large-sieve work. The right
play may be collaboration (Pascadi/Maynard orbit).

---

## 7. The Riemann Hypothesis (and GRH at primorial conductors)

**P(closure): low — and ranked here on significance × unique equipment, stated
plainly.** The reduction achieved is real and quantified: RH ⟺ one decreasing scalar
having limit 0 (CCM μ_λ ↓ 0) ⟺ arch-domination ⟺ u_B ≥ 0 ⟺ the arithmetic
dominant-energy condition, with the archimedean half a THEOREM (and now a relative-
entropy identity, N14), the local Frobenius data assembled, the open content localized
to the single point τ = 1, the correct register identified (additive/Li/Kubo–Mori;
boundedness-shaped, not monotone-shaped), and seven shortcut classes closed by exact
no-go theorems so effort cannot be wasted re-chasing them.

**Why it stays on the list:** every one of items 1, 3, 6 feeds it directly (1 = the
live route's stated obstacle; 3 = the term-by-term half of the τ = 1 closure; 6 = the
unconditional partial-credit frontier), and the program's comparative advantage over
the rest of the field — the named equivalences, the exact-signature methodology, the
matched-pair DH filter — is largest precisely here. The honest statement per the
program's own discipline: structural reduction real; proof not yet; the difficulty is
a scale and we keep lowering it. **Settlement path:** front-end = complete
monotonicity / positive-energy on the prolate platform; endgame = unitary CFT on the
scaling site (preferred) or 𝔽₁ Hodge positivity.

---

## Honorable mentions (high P, smaller scope — do these opportunistically)

- **Canonical primorial interpolation (T33).** P ≈ 0.9 — already closed; a clean
  standalone special-functions paper. Highest raw closability in the portfolio; ranked
  below only on scope.
- **Quantum monotone-metric selection (T24 + Paper 18 rigidity).** P ≈ 0.5 — the
  two-principles-two-metrics theorem (additivity → Kubo–Mori; conservative flow →
  Bures) with the fork located in the apex generator. Watch the synthesis-vs-new line.
- **de Bruijn–Newman flow no-go.** Publishable negative theorem (no backward-entropy
  monotone; RH is boundedness-shaped) redirecting a route the field still works.
- **Li-criterion operator realization + λ_n^arch zero-free regions.** Publish the
  realization; check competitiveness against Vinogradov–Korobov before any strength
  claim.
- **KS-classicalization refinement with DBT26.** Bounded joint-refinement target.

## Do not chase (assessed, structural obstructions on file)

- **BSD (CM)** — conductor mismatch, infinity-type, wrong-s positivity
  (`BSD-Simplicial-Assessment-Draft1.md`).
- **Iwasawa CM** — ℂ-side vs p-adic, no bridge (`IwasawaCM-Simplicial-Assessment-Draft1.md`).
- **Patterson constant** — lever orthogonal to the varying-conductor sum; GL(3)
  metaplectic content missing (`PattersonConjecture-Simplicial-Assessment-Draft1.md`).
- **Cubic moments M₃(T,q)** — L¹-type value statistic vs intrinsically L² bilateral
  (`CubicMomentBounds-Simplicial-Assessment-Draft1.md`).
- **Collatz as an instrument target** — the quanta object is a lens, by its own audit.

## Portfolio note

Items 1–6 are mutually independent and individually bounded; items 1, 3, 6 compound
toward item 7. The two ML items (2, 4, 5 partially) monetize the SAME mathematics
(conductor packets, cumulant tower, symmetric-vs-antisymmetric split) in a field with
faster referee cycles — they are the program's external-validation flank, not a
detour: every theorem there is an instance of the same blind-spot/closure family that
the RH spine runs on (order-2 blindness = Bures zero-blindness = symmetric instrument
blind to the archimedean arrow).
