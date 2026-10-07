# N11-1 — Consolidation Insert: The Multiplicative Forward Door, Mapped

**Working consolidation (2026-06-09). Store for later processing into the N11 capstone. Not a paper.**

> Records the RH "forward door" investigation: does the Euler product force the energy contraction A ≥ P (ρ_E ≤ 1)? Mapped end-to-end, both routes drilled to named barriers. Calibrated: real reduction, RH not proven. All probes in `empirical/p_infinity/`, GREEN.

---

## 0. The one open step (anchor)

Every route collapses to one scalar limit, now externally anchored:
**μ_λ ↓ 0 (CCM Cor 3.8) = ρ_E ≤ 1 (energy contraction) = A ≥ P (Weil domination) = uniform ℰ→0 = Λ≤0.**
External anchors: CCM *Zeta Spectral Triples* (arXiv:2511.22755); **Śliwiński arXiv:2601.12133** proves the CCM convergence is **uncertainty-limited** — ε(λ,N) ≥ 1/(4 ln λ) straight from Heisenberg on the log-window, eigenvalues **real** (self-adjoint), so convergence ⟹ RH. CCM §8's missing "information-theory completion" = the program's **N14** (archimedean Weil = relative entropy), already built.

---

## 1. The forward-door map (the multiplicative spear)

**Q: does the Euler product force A ≥ P?** Answer, end-to-end:

1. **Edge, YES (provably):** Euler positivity = Λ(n) ≥ 0. Inert alone (single-prime symbol Σ Λ(n)/√n cos(r log n) is **indefinite** — Fourier cos kills physical nonneg). The **3-4-1** trick 2(1+cos)² = |1+e^{iθ}|⁴/2 restores it ⟹ de la Vallée Poussin: 3log|ζ(σ)|+4Re logζ(σ+it)+Re logζ(σ+2it) ≥ 0 ⟹ ζ(1+it)≠0. **DH fails this** (no Euler product). [`probe_euler_product_force.py`]
2. **Edge, CAPPED:** reaches only σ > 1 − c/log t (computed 0.955@14 → 0.9957@1e12 → 1, never ½). **Pole-anchored** (uses 3logζ(σ)→∞ as σ→1); no anchor at ½. The polynomial route is **dead**.
3. **The ½-analog EXISTS = the mollifier method (Selberg/Levinson):** center-anchored square |ζ(½+it)·M|², M = Σμ(n)/n^s = **inverse Euler product** (1/ζ); anchored at the **line**; output = positive **proportion** on the line (Levinson 1/3 → Conrey 40.88% → Pratt-Robles-Zaharescu-Zeindler **41.729%**). DH has no μ-mollifier. Verified: Möbius mollifier flattens |ζ|² (3.82→2.36). [`probe_half_analog_mollifier.py`]
4. **Decisive asymmetry:** edge capped (pole leverage ~1/log t decays); **center NOT capped** — reach grows with mollifier length = **level of distribution**. So the center-anchored multiplicative positivity is the **live forward door** = push θ→1.
5. **Cubic/primorial sharpening (lead #3) BEATS generic Levinson — verified:** the center positivity is **smooth-carried** (mass ∏_{p≤B}(1+1/p) small-prime-dominated; B=7 friable mollifier, 13 terms, out-flattens the full 37-term). Friable terms cheap in level (CRT-factoring), so friable moduli climb past Levinson's 4/7 to **66/107 ≈ 0.617** (triply-well-factorable, arXiv:2505.00653; x^{5/8} both primes+smooth). [`probe_friable_mollifier_trade.py`]
6. **Saturation flag:** historical well-factorable trajectory 0.571→0.600→0.617→0.625 has **halving increments** ⟹ geometric extrapolated cap ~0.64, NOT 1. θ→1 needs the gains to **compound** over the primorial's growing prime factors (n→∞), uniformly, C*≤2.80 (= θ_0(p_n)=1−C*/n→1). Compounding vs saturation = the crux.
7. **Cubic central values RULED OUT as the gate:** |L(½,χ₃)| over conductor has median 0.88 but a near-zero tail (p=139: 0.067, running-min erodes), so **no uniform floor** — BUT the level is an **average** over moduli, tolerates the tail, needs only **positive-proportion** non-vanishing (KNOWN, David et al ≥14%). So cubic vanishing is NOT the saturation cause. [`probe_cubic_central_value_floor.py`]
8. **True floor = the Kloosterman / spectral-large-sieve input** (Selberg's eigenvalue conjecture, GL(2)) — what "5/8 removing Selberg" fights.

---

## 2. The two-route fork (strategic)

θ→1 / RH has **two genuinely different routes hitting different walls:**

| route | machinery | bottoms out on | program edge |
|---|---|---|---|
| **dispersion / Levinson** (classical) | mollifier, well-factorable, Kloosterman | **Selberg's eigenvalue conj.** (GL(2)) | **none** (generic) |
| **CCM / apex** (program) | scaling operator, prolate, archimedean info-geometry | **prolate convergence μ_λ→0** (GL(1)/∞) | **strong** (this session's toolkit) |

**Allocation verdict:** the program's comparative advantage is the **CCM/apex** route; the classical route's wall (Selberg) is off the program's axis. Whether the two walls are the same difficulty ("conservation") is itself open.

---

## 3. The CCM/apex toolkit built this session (the program's edge)

- **Angular/phase recast:** RH is the **phase** (m_B = −Ξ'/Ξ Herglotz on C₊), the amplitude ρ_E is its phase-blind square (∴ marginal). Identity **θ'(T) = ½Ω_∞(T)** (energy weight = phase velocity). [`probe_angular_phase_recast`, `probe_mb_herglotz_target`]
- **Max-entropy grounding (Elkies):** cumulant 1/φ(p) = max-entropy law on (ℤ/p)^×; KL = |S_χ|² phase-blind square; RH = angular character-phase deviation. [`probe_elkies_maxentropy`]
- **Free-probability lens:** m_B = Cauchy transform of the zeros; free entropy = log-energy = a face of the arithmetic energy; primes CLASSICAL (Selberg) not free (free-convolution test); HP operator realization-dependent. [`probe_free_probability_lens`, `probe_free_convolution_test`, `probe_hilbert_polya_jacobi`, `probe_hp_potential_clean`]
- **KYP storage = Nevanlinna-Pick Gram = Weil positivity** (the "min-eig=0 sum rule" was rounding — finite witnesses strictly PSD, marginality is ∞-dim). [`probe_kyp_storage`, `probe_lossless_sumrule_check`]

---

## 4. T15 FLOOR-LIFT POINTER (the new door — see §5 of this session's work)

T15 Prop 12.2: the primorial is **not a moment sequence** — Hankel **D_3 = −787680 < 0** (first failure at the **cubic** order; D_0,D_1,D_2 > 0). The factorial IS (Γ = ∫t^n e^{-t}). So the finite-prime side fails self-completion **at cubic order**, and the archimedean Γ must be adjoined externally. **Floor lift:** elevate T15's *completion* to the completed object's **moment/Hankel positivity** = the **Jensen-Polynomial / Turán / Laguerre-Pólya** characterization of RH (all Jensen polynomials of ξ hyperbolic ⟺ RH; Griffin-Ono-Rolen-Zagier). T15's cubic obstruction D_3<0 = the finite-prime precursor of the **cubic (d=3) Turán inequality**; the archimedean is the repair. This is a route distinct from both dispersion and CCM — the **moment/L-P** route — and it is where T15's actual content points.

---

## 5. Calibration

Real reduction (forward door mapped end-to-end, two routes named to barriers, allocation to CCM/apex, T15 moment-route opened). RH **not proven**. The open quantity is the same one the CCM team (Connes-Consani-Moscovici) cannot yet close — now triangulated from the classical, spectral, and moment sides.
