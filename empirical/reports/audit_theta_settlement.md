# Audit θ — Settlement: Capacity_V Scaling on the Primorial Ladder `ℤ/{6, 30, 210, 2310, 30030}`

**Date:** 2026-05-20
**Audit script:** [`empirical/audit_theta_capacity_scaling_primorial_ladder.py`](../audit_theta_capacity_scaling_primorial_ladder.py)
**Deterministic transcript:** [`empirical/audit_theta_capacity_scaling_primorial_ladder_run_output.txt`](../audit_theta_capacity_scaling_primorial_ladder_run_output.txt)
**Tier:** **[P]** for all conductor-lattice / multiset-count / capacity-ratio values (integer arithmetic in every membership decision; closed-form orbit counting for total; O(|V|²) direct enumeration for pure-V); **[A]** for the structural-shape characterization (linear-in-log fit with documented residuals; the empirical decay law is *super-exponential in number-of-primes*, beyond what a linear fit captures).
**Wall time:** **0.260 seconds** across all five rows on CPU. No GPU. No HF.
**Anchors:** ℤ/6 and ℤ/30 v2insert-08 numbers reproduced to exact integer match.

---

## 1. Audit scope and pre-claim

Extends audit η of v2insert-08 (ℤ/6 + ℤ/30) to the next three squarefree primorials: **`ℤ/210 = 2·3·5·7`**, **`ℤ/2310 = 2·3·5·7·11`**, **`ℤ/30030 = 2·3·5·7·11·13`**. Settles the quantitative scaling shape of `Capacity_V` for Paper 48 (proposed, v2insert-03 C2 / v2insert-08).

Pre-claimed three-outcome branches (v2insert-04 §3.1 extension), v2insert-08 §6:
- **K-branch:** `Capacity_V` continues to decay monotonically; the 1/3 → 1/25 (8.3×) decay observed `ℤ/6 → ℤ/30` extends as a clean pattern.
- **L-branch:** decay stalls on some primorial row.
- **Joint-on-disjoint:** non-monotone behavior, or scaling exponent qualitatively different from log-linear-in-n.

---

## 2. The headline scaling table

| Row | `n` (# primes) | `dim_V` | `dim_M` | `T_total` | pure_V | **`Capacity_V`** | `log₁₀(Capacity_V)` | Decay vs previous |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `ℤ/6 = 2·3` | 2 | 3 | 2 | 6 | 2 | **0.33333333** | -0.4771 | — |
| `ℤ/30 = 2·3·5` | 3 | 7 | 22 | 150 | 6 | **0.04000000** | -1.3979 | **8.333×** |
| `ℤ/210 = 2·3·5·7` | 4 | 13 | 196 | 7350 | 14 | **0.00190476** | -2.7202 | **21.000×** |
| `ℤ/2310 = 2·3·5·7·11` | 5 | 23 | 2286 | 889 350 | 34 | **0.00003823** | -4.4176 | **49.824×** |
| `ℤ/30030 = 2·3·5·7·11·13` | 6 | 35 | 29 994 | 150 300 150 | 62 | **0.00000041** | -6.3846 | **92.677×** |

**The decay factor itself grows roughly linearly with `n`.** This is the headline finding: the per-step decay accelerates, not decelerates. Capacity_V's vanishing is **super-exponential in number-of-primes**.

---

## 3. The realized branch — K, with sub-finding

### 3.1 Monotonicity: K-branch confirmed

`Capacity_V(ℤ/6) > Capacity_V(ℤ/30) > Capacity_V(ℤ/210) > Capacity_V(ℤ/2310) > Capacity_V(ℤ/30030)` ✓

All four pairwise inequalities strict. v2insert-08's monotone-decay prediction (the K-branch of audit η extended to audit θ) is confirmed across four primorial steps.

### 3.2 The scaling-law structure

Linear fit in log space, `log₁₀(Capacity_V) = a·n + b`:

| Parameter | Value |
|---|---:|
| Slope `a` | **-1.4835** |
| Intercept `b` | +2.8543 |
| Equivalent: per-prime decay factor `10^|a|` | **30.44×** (geometric mean over the 4 steps) |
| Max absolute residual `\|observed − fit\|` (log₁₀ units) | **0.3646** |

The residuals are **not** small. A clean log-linear fit (exponential decay in `n`) would have residuals near machine precision. The observed `≈ 0.36 log₁₀` residual indicates **super-exponential decay in `n`** — the decay accelerates as `n` grows, exactly matching the v2insert-03 §1.2 prediction that `Capacity_V` decays "faster than any holographic power law."

This is a **sub-finding worth recording explicitly**: the empirical scaling is not a pure exponential. The pre-claim's K-branch is "monotonic decay" without committing to functional form; the structural-shape characterization (audit ι, Bousso-bound comparison) becomes load-bearing for adjudicating Paper 48 C4 ("the shape matches Bekenstein–Hawking holographic structure").

### 3.3 Why super-exponential is structurally expected

Heuristic (not part of the [P] tier, but useful for orientation):

- `dim_V(P_n) = Σ_{p∈primes(P_n)} φ(p) = Σ(p-1) ~ Σp ~ n²·ln(n)/2` (Prime Number Theorem)
- `P_n ~ exp(n·ln(n))` (Mertens-style primorial growth)
- `Capacity_V ~ |pure-V triples| / |total triples| ~ |V|²·O(1) / |dynamical|² ~ |V|²/P_n²`
- `~ polynomial(n)·ln^a(n) / exp(2n·ln(n))`

So `log₁₀(Capacity_V) ~ -2n·ln(n)/ln(10) ≈ -0.868·n·ln(n)` to leading order. That's *super-linear in `n`* — exactly the residual pattern observed.

At the five data points the linear-in-`n` fit catches the dominant behavior with `O(0.3-0.4)` log₁₀ residuals; a better fit would be `log₁₀(Capacity_V) ~ -n·ln(n)·(const) + lower-order corrections`. Audit ι (Bousso-bound shape comparison) is the appropriate venue for adjudicating which specific holographic-saturation shape matches the residual structure.

---

## 4. Anchor verification (v2insert-08)

| Row | Quantity | v2insert-08 | This audit | Status |
|---|---|---:|---:|:---:|
| ℤ/6 | `dim_V` | 3 | 3 | ✓ |
| ℤ/6 | `dim_M` | 2 | 2 | ✓ |
| ℤ/6 | `T_total` | 6 | 6 | ✓ |
| ℤ/6 | `pure_V` | 2 | 2 | ✓ |
| ℤ/6 | `Capacity_V` | 0.3333… | 0.3333… | ✓ |
| ℤ/30 | `dim_V` | 7 | 7 | ✓ |
| ℤ/30 | `dim_M` | 22 | 22 | ✓ |
| ℤ/30 | `T_total` | 150 | 150 | ✓ |
| ℤ/30 | `pure_V` | 6 | 6 | ✓ |
| ℤ/30 | `Capacity_V` | 0.04 | 0.04 | ✓ |

All v2insert-08 numbers reproduced to exact integer match. Anchor verified.

---

## 5. Pontryagin orthogonality (Paper 47 C3 row-generalization extended)

| Row | `‖V_proj · M_proj‖_F` | Method | Algebraic value |
|---|---:|---|---:|
| ℤ/6 | 1.14e-15 | Numerical (6×6 projectors) | 0 |
| ℤ/30 | 1.22e-14 | Numerical (30×30 projectors) | 0 |
| ℤ/210 | 1.44e-13 | Numerical (210×210 projectors) | 0 |
| ℤ/2310 | — | Skipped (memory; 2310×2310 complex too large for the audit's per-row budget) | 0 (algebraic, by Pontryagin character orthogonality) |
| ℤ/30030 | — | Skipped (memory) | 0 (algebraic) |

For all five primorial rows: V and M character index sets are **disjoint by construction** (different conductors live in disjoint character classes). Pontryagin character orthogonality `⟨χ_k | χ_ℓ⟩ = δ_{k,ℓ}` on `(ℤ/N)*` forces `V ⊥ M` as Hilbert subspaces **algebraically**, on every row. The numerical floor values (`~10^{-15}` to `~10^{-13}`) are machine-precision artifacts of the floating-point matrix multiplication.

**Paper 47 C3 row-generalization is now confirmed on five primorial rows** — the Arithmetic Decoupling Theorem extends to every primorial row up to ℤ/30030 at the conductor-lattice level.

---

## 6. Per-row class breakdowns (where computed)

The full O(N²) class enumeration was performed for `N ≤ 210`:

### `ℤ/6` (anchor; Paper 32 Cor 6.1d.1)
| Class | Count | % |
|---|---:|---:|
| VVV | 2 | 33.33% |
| MVV | 2 | 33.33% |
| MMV | 2 | 33.33% |
| MMM | 0 | 0.00% |

### `ℤ/30` (v2insert-08)
| Class | Count | % |
|---|---:|---:|
| VVV | 6 | 4.00% |
| MVV | 14 | 9.33% |
| MMV | 66 | 44.00% |
| MMM | 64 | 42.67% |

### `ℤ/210` (this audit, new)
| Class | Count | % |
|---|---:|---:|
| VVV | 14 | 0.19% |
| MVV | 56 | 0.76% |
| MMV | 1224 | 16.65% |
| MMM | 6056 | 82.39% |

The MMM share grows monotonically (0% → 42.67% → 82.39% → ?), consistent with the structural intuition that the "kinematic" V sector becomes asymptotically negligible compared to the "gravity-adjacent" M sector as the primorial grows. For `ℤ/{2310, 30030}` the breakdown is skipped for compute but the MMM share trend is expected to approach 1 (since `dim_M/dim_dynamical → 1` as `n → ∞`).

The 14 pure-V multisets on `ℤ/210` (explicitly enumerated in the transcript) are all *pure-single-conductor* triples — every pure-V multiset has all three legs in the same single-prime packet `H_p`. This is the **same structural fact** as on `ℤ/6` and `ℤ/30`: cross-`H_p`/`H_q` triples (where `p ≠ q` are distinct single primes) cannot close without routing through M. The arithmetic root (Paper 32 Cor 6.3 L1 + L2 generalized) holds on every primorial row.

---

## 7. Implications for Paper 48 (Conductor Capacity Bound)

### 7.1 C2 — extended to five primorial rows

Paper 48 C2 was settled at K-branch on `ℤ/30` in v2insert-08. Audit θ confirms K-branch on the full primorial ladder up to `ℤ/30030` — five data points, monotone decay strict, super-exponential in `n`.

### 7.2 C4 — the structural-shape correspondence

v2insert-03 §1.2 / §1.3 conjectured that `Capacity_V` decays with **the shape of Bekenstein–Hawking holographic saturation** (boundary becomes asymptotically negligible relative to bulk) but NOT with the literal `S = A/4` exponent. Audit θ confirms this:

- **Shape (qualitative):** K-branch confirmed — `Capacity_V → 0` with monotone decay.
- **Exponent (quantitative):** super-exponential in `n`, *steeper* than any power-law in `N = P_n`. So the program's holographic-shape correspondence is **direction-confirmed and exponent-distinct** from literal `S ~ R²`. The shape matches; the literal formula does not.

Paper 48 C4's pre-claim now has a more precise quantitative description:
- *K-direction-confirmed:* the shape of decay is monotonic and accelerating (decay factor per added prime grows: 8.3× → 21× → 50× → 93×).
- *Joint-on-disjoint at the exponent:* the decay is NOT a clean power law; the per-prime decay factor itself grows roughly linearly. Audit ι (Bousso-bound shape comparison) is the natural next move to characterize the structural shape more precisely.

### 7.3 The per-prime decay factor growth pattern

| Step | Added prime | Decay factor |
|---|---:|---:|
| 6 → 30 | +5 | 8.333× |
| 30 → 210 | +7 | 21.000× |
| 210 → 2310 | +11 | 49.824× |
| 2310 → 30030 | +13 | 92.677× |

Roughly, decay-factor ≈ (added prime) × (something growing). If the decay scales as `~ p_{n+1}²` per step (heuristic from `Capacity_V ~ |V|²/P_n²` and `P_{n+1} = P_n · p_{n+1}`), then decay factor `≈ p_{n+1}²` after correcting for `|V|` growth. Check: `5² = 25` vs observed 8.3; `7² = 49` vs 21; `11² = 121` vs 50; `13² = 169` vs 93. The observed decay is slower than `p²` (consistent with `|V|` also growing). The asymptotic behavior is something like `~ p_{n+1}²·g(n)` for a slowly-varying `g`. Pinning down the exact asymptotic is open.

---

## 8. Discipline check (Paper 35 §3 honored throughout)

- **Anchored objects (§3.3).** v2insert-08's `ℤ/6` and `ℤ/30` numbers reproduced to exact integer match (verified inline). Closed-form orbit-count formula derived from Burnside-type counting on ordered triples; verified against the O(N²) full enumeration for `N ≤ 210` (no discrepancy).

- **Deterministic, exact, reproducible (§3.4).** Pure integer arithmetic in all multiset counts; closed-form total via orbit counting; integer GCD for conductor; floating-point only in Pontryagin overlap reporting (`~10^{-15}` to `~10^{-13}`, machine floor; algebraic value 0 exactly). No seeds, no tolerances except the machine-floor floor itself. Total wall time 0.26 seconds — deterministic on every re-run.

- **Three-outcome matched-pair (v2insert-04 §3.1).** Pre-claimed K (monotone decay) / L (stall) / joint-on-disjoint (non-monotone or different exponent). Realized: **K (monotonicity) with joint-on-disjoint flavor at the exponent level** — monotonic across all five rows, but the per-step decay factor grows rather than stabilizing, indicating the *exponent* is super-exponential in `n` rather than constant. This is reported honestly; not silently absorbed into "K-confirms" only.

- **No upward tier-crossing (§3.5).** Capacity values reported at [P] (deterministic integer arithmetic); the linear-fit residuals reported at [A] (the fit is a *characterization*, not a law); the super-exponential characterization reported at [A] (consistent with PNT-style heuristics, not proved in this audit).

- **Failures-first-class (§3.6).** Full O(N²) class breakdown was *skipped* for `N > 210` to avoid memory blowup; this scope boundary is stated explicitly, not hidden. Pontryagin numerical check similarly skipped for `N > 210`; the algebraic alternative is stated. Audit ι (Bousso-bound shape comparison) is named explicitly as the natural sequel, not glossed.

- **Dimensional firewall (Paper 32 §11.2).** No physical units. No Planck scale. No horizon area. No Bekenstein–Hawking entropy values. Only dimensionless ratios (`Capacity_V`), integer counts (multiset enumerations), and log-space ratios (decay factors). The holographic-shape correspondence remains *correspondence language* per §11.1 emergent-gravity positioning; this audit does not promote it.

---

## 9. Carry forward

| Audit | Status | Next step |
|---|---|---|
| **θ (this audit)** | **SETTLED — K (direction), joint-on-disjoint at exponent** | — |
| ι (Bousso-bound shape comparison) | PENDING — pure mathematics | Compare super-exponential `Capacity_V` decay against Bekenstein bound (`S ≤ 2πRE`), 't Hooft–Susskind holographic (`S ≤ A/4`), Bousso bound (`S ≤ A/4G` on null geodesic congruences). Identify which shape the program's decay most closely matches. |
| δ (Paper 47 all-orders Pontryagin proof) | PENDING — pure mathematics | Independent of θ but synergistic. Would promote Paper 47 C1 to [P] at all orders. |
| ε (Paper 47 QG structural dictionary) | PENDING | Independent |
| Paper 46 C5 geometric realization on `D(ℂ^N)` for `N > 6` | PENDING | CPU-tractable Bures-Hessian sub-bundle audit on `D(ℂ^30)`; queued from v2insert-08 |
| κ-`ℤ/30` (Paper 47 + Paper 46 empirical) | DEFERRED | Requires GPU + HF + `ℤ/30` cyclic-task corpus |
| Higher primorial rows beyond `ℤ/30030` | PENDING | Easy extension; `ℤ/510510 = 2·3·5·7·11·13·17` is the next; same script, ~0.05 s additional |

**Recommended next-best move:** **audit ι** — Bousso-bound shape comparison. Pure mathematics, no compute needed. Compares the empirical super-exponential decay of `Capacity_V` against the canonical holographic-bound shapes (Bekenstein, 't Hooft–Susskind, Bousso). Identifies which peer-reviewed holographic structure (if any) matches the program's decay shape. Settles Paper 48 C4 at a structural-correspondence level.

---

*Settlement record archived. Audit θ on the primorial ladder `ℤ/{6, 30, 210, 2310, 30030}` settled with K-branch (monotone decay) and joint-on-disjoint flavor at the exponent level (super-exponential in number-of-primes, beyond log-linear). Five data points; full enumeration on the first three rows; closed-form + O(|V|²) on the last two; all v2insert-08 anchors reproduced exactly. Paper 35 §3 discipline honored throughout; no tier-crossing, no silent absorption. Reproducibility artifact and deterministic transcript archived under `empirical/`. Total wall time 0.260 seconds.*
