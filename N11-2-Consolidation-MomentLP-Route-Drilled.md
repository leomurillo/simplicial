# N11-2 — Consolidation Insert: The Moment / Laguerre–Pólya Route, Drilled to Its Floor

**Working consolidation (2026-06-10). Store for later processing into the N11 capstone. Not a paper.**

> Continues N11-1 §4 (the moment/L-P route opened by T15's D₃<0). Drills it end-to-end: the diagonal "transfer the rigid reference's hyperbolicity to Ξ" spear is **dead by theorem** (moment ⊥ multiplier), the within-family variant is **closed by measurement**, and the survivor is a **measurement frame** that welds the Jensen-margin tower to the one proven theorem on the axis (Rodgers–Tao Λ≥0). One genuinely new observable falls out: the smear width w(χ), parity-selective. Calibrated: three spears down with proofs/measurements, RH **not** proven, no independent inequality imported. Scripts in `empirical/p_infinity/` (`ms_test.py`, `test3.py`, `effective_lambda.py`, `analyze_efflambda.py`); external `zeta_multiplier_kill.py`, `family_turan_smear.py`.

---

## 0. Where this sits (anchor)

N11-1 §4 elevated T15's cubic obstruction (primorial **not** a moment sequence, Hankel **D₃ = −787680 < 0**) to the completed object's Jensen / Turán / Laguerre–Pólya characterization: **all Jensen polynomials of Ξ hyperbolic ⟺ RH** (Griffin–Ono–Rolen–Zagier). The natural spear: pick a concrete L-P reference whose hyperbolicity is manifest — the **picket/sine** `S(t)=sin(πt)/(πt)=∏(1−t²/k²)`, ẽ_m = π^{2m}/(2m+1)! — and try to **transfer** its rigidity to Ξ_χ via the diagonal ratio λ_m = a_m/ẽ_m. If λ is a **multiplier sequence** (Pólya–Schur), the transfer is a theorem and RH-for-the-family follows. This note drills that spear.

Setup, fixed throughout: completed self-dual L-functions Ξ_χ(t) = Σ_m (−1)^m a_m t^{2m}, a_m = e_m({1/γ_ρ²}) (elementary symmetric of inverse-square zeros, >0 under RH). Reference ẽ_m = e_m({1/k²}) ∝ 1/(2m+1)!. All margins/ratios scale-invariant (rescaling zeros multiplies the diagonal by a geometric factor, harmless).

---

## 1. The multiplier-sequence kill — moment ⊥ multiplier (dead by theorem)

**Theorem (the diagonal is provably not a multiplier sequence).** Write λ_m = b_m/ẽ_m for Ξ = ζ-completed ξ. Insert Pólya's kernel ξ(½+it) = 2∫₀^∞ Φ(u)cos(ut)du and integrate by parts once (Φ>0, Φ′<0 for u>0.0024, boundary terms vanish):

  λ_m = ∫₀^∞ (u/π)^{2m} dτ(u),  dτ = −2uΦ′(u)du ≥ 0.

So **λ is a Stieltjes moment sequence** (variable v=(u/π)²) ⟹ strictly **log-convex** by Cauchy–Schwarz (τ has a density, not an atom): λ_{m−1}λ_{m+1} > λ_m². But Pólya–Schur applied to the real-rooted x^{m−1}(1+x)² forces any multiplier sequence to satisfy the **Turán** inequality λ_m² ≥ λ_{m−1}λ_{m+1}. **Log-convex ∩ log-concave = geometric = a rescaled sine.** False. So λ is not a multiplier sequence, and the failure is **total** (every Turán index, strictly), not marginal. The route dies at **degree two, by structure**. [external `zeta_multiplier_kill.py`: T_m=λ_m²/(λ_{m−1}λ_{m+1}) climbs 0.645→0.973, all <1; d=2 Pólya–Schur polynomial already has complex roots.]

**Calibration of the kill:** essentially classical (Pólya 1926 sinc + Pólya–Schur; folklore-adjacent in the Csordas–Norfolk–Varga / Laguerre–Pólya school). Treat as **decisively settling our question**, not a novelty claim.

**Numerical confirmation across the family (`ms_test.py`, dps=140, 607 chars |D|≤1000):** R_n = τ_n(a)/τ_n(sine), τ_n(a)=a_{n+1}²/(a_n a_{n+2}). **607/607 characters violate** (some R_n<1 at every character); global min R_n = **0.672** (D=−3, n=0); R_n → 1 from **below** (R₁₀≈.986, R₂₀≈.991, R₃₈≈.995) — the ζ-anchor's 0.645→0.973 signature.

**Family refinement (vs ζ):** for Dirichlet L the kernel positivity is **not** termwise-automatic, so the *low-order* Turán often **passes** (R₀>1, e.g. D=−955 gives R₀=4.21) — these are **kernel-positivity events** (§4). The failure nonetheless **locks in at high order** for every character ⟹ MS dead for all. The strict "every m" of the ζ theorem becomes "guaranteed at high m" for the family.

---

## 2. Test 3 — the within-family diagonal (closed by measurement)

The moment-kill does **not** apply to a ratio of two Ξ's (no kernel identity forces log-convexity). So the last diagonal: μ_m = a_m(χ_{−|D|})/a_m(χ_{+|D|}) at **matched conductor** (both ±4m fundamental ⟺ |D|=8j), Turán-tested. A clean pass would give a conditional transfer **even-channel hyperbolic ⟹ odd-channel hyperbolic** — reducing the critical chiral channel to the ζ-like one.

**Result (`test3.py`, 51 matched pairs |D|≤1000): mixed-negative.** 32/51 pass μ-Turán at all shifts (but **marginally**, min≈1.0003 at the highest shift); **19/51 fail at low order** (minT 0.53–0.99 at m=1–3, the best-conditioned ratios ⟹ real, not noise). So the clean universal even→odd transfer **does not hold; the diagonal program is closed.** The failures concentrate at low order = the archimedean Γ-factor difference (reconfirms the chiral gap is archimedean; not leverage). High-order μ is universally Turán-positive (→1.0003), only the low-order/archimedean part obstructs.

---

## 3. The survivor — effective de Bruijn–Newman calibration (couples to a theorem)

The one move that touches a **proven theorem** rather than another equivalent positivity. The dBN heat flow Φ→e^{tu²}Φ acts on the Taylor coefficients by an **exact shift** (from ∂_t b_m = (2m+1)(2m+2) b_{m+1}):

  b_m(t) = Σ_{k≥0} (t^k/k!) · (2m+2k)!/(2m)! · a_{m+k}(0).

Define **t*_d(χ)** = the t<0 where the degree-d Jensen margin dies (two real Jensen roots collide → complex). RH ⟺ Λ=0 (Rodgers–Tao **Λ ≥ 0**), so t*_d is a **finite-degree image of Λ**, and |t*_d| → 0 as d→∞. [`effective_lambda.py`, dps=180, MFLOW=44; death = loss of root-reality, *not* coefficient sign — gotcha: guarding b₁≤0 gave a spurious d-independent t* at D=−163.]

**Finding 1 — the coupling works.** |t*_d| **decreases monotonically toward 0** with degree (odd 2.07→0.60, even 2.02→0.57 over d=6→24) = exactly what Λ=0 requires. The margin tower is now a **measured distance to the proven boundary**. ✓

**Finding 2 — distance is conductor-governed, parity-blind (honest negative).** r(log conductor, |t*₂₄|) = **−0.961**, r(γ₁, |t*₂₄|) = **+0.903**. At matched conductor the channels are **equidistant** (odd/even |t*| ratio ≈0.99 for q>40; only q<40 shows odd ~11% farther). The chiral *margin* gap (H0/H3, ~15–22%) does **not** manifest as a chiral *dBN-distance* gap — distance is a known zero-density effect. The speculative "t* carries provable structure" did **not** materialize: t* is a known quantity, no new arithmetic handle.

(Honest caveat: low-d / large-|t*| points carry heat-flow truncation error from finite MFLOW; the *trend* and the *correlations* are robust, a precise Λ-extrapolation is not claimed.)

---

## 4. The one new observable — the smear width w(χ)

w(χ) = λ₀λ₂/λ₁² − 1 = Var(v)/E(v)² of the positive scaling measure τ_χ (the "smear" connecting the rigid picket to Ξ_χ: Ξ_χ(t) = ∫ sinc(ut) dτ(u)). w>0 ⟺ λ log-convex (moment-like, the kernel positive-decreasing). w<0 = a **kernel-positivity event** (Φ_χ not positive-decreasing, λ not a moment sequence) ⟺ R₀>1 (ties §1 and §3).

**Parity signature (`analyze_efflambda.py`, 91 chars |D|≤150 both parities):**

| channel | mean w | w<0 (kernel-positivity events) |
|---|---|---|
| **odd (chiral)** | **−0.053** | **25/47 = 53%** |
| **even (real)** | **+0.130** | **11/45 = 24%** |

The chiral channel breaks moment-positivity at **2.2× the rate**, with opposite-sign means. So the chiral asymmetry is distinguished **not by distance-to-boundary (§3, parity-blind) but by archimedean kernel structure** — the Pólya kernel's monotonicity. (Secondary: r(w,|t*₂₄|)=+0.42, r(w,γ₁)=+0.71.) This is the session's one genuinely new, clean empirical object, and it localizes "chiral = archimedean" to a specific analytic statement about Φ_χ.

---

## 5. The sharpened dichotomy (what the failure means)

The identity that kills the route also names the transfer: T_λ = ∫ S_v dτ̃(v) — the L-function is a **positive smear of rescaled rigid pickets**, RH = that smear sitting **exactly at the hyperbolicity boundary**. That is the de Bruijn–Newman frame; the H0 floor (margins at 0.99–1.0 of sine, step-ratio→1.005, **zero slack**) is its finite-degree image; Λ=0 (Rodgers–Tao Λ≥0) is "RH is barely true if true."

Welded to T15 the dichotomy is **sharp and complementary:**

- **Finite-prime side** (T15 Prop 12.2): primorial is **not a moment sequence**, D₃<0 — fails **Hankel/moment** positivity at cubic order.
- **Archimedean-completed side** (§1): the ratio-to-rigid **is** a moment sequence (dτ≥0) — but therefore fails **multiplier** positivity (moment ⊥ multiplier).

So "the archimedean is the repair" (N11-1 §4) sharpens to: **the repair is a positive scaling-smear; the smear forfeits diagonal rigidity-transfer as the price of positivity; RH is the smear's exact criticality.** A positive average of scaling operators is an element of the **positive cone of the scaling-group algebra** — the CCM/apex native object. The moment/L-P spear, drilled to its floor, **routes into the scaling frame** (N11-1 §2 allocation verdict, now *derived* rather than chosen).

---

## 6. Calibration

Real map-narrowing: **three spears eliminated** — polynomial-edge (N11-1 §1, dead by structure), diagonal/multiplier (§1, dead by theorem), within-family diagonal (§2, closed by measurement) — the survivor identified as a **measurement frame** (§3) that couples the margin tower to the one proven theorem on the axis, plus **one new observable** (§4, w(χ): chiral kernel-positivity-breaking).

RH **not proven**, and **no independent inequality imported.** Applying the discipline — *where does new information enter?* — the answer for §3 is "Rodgers–Tao, as a backstop we measure against," not "an inequality that dominates the Weil form." Observables tell you where the difficulty sits; they do not supply the inequality that overcomes it. The open quantity is unchanged: uniform low-zero control / Λ=0 / level-of-distribution → 1, the same wall as N11-1 §0, now triangulated also from the moment/L-P side and shown to **converge with** the scaling/CCM spear rather than run parallel to it.

Forward: nothing further on the diagonal axis (exhausted). Next compute waits for a candidate **independent input** to test, not another reformulation to measure.
