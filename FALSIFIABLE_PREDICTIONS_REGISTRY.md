# Falsifiable Prediction Registry

*On record 2026-06-25. Pre-registered, matched-pair (KILL **and** CONFIRM), tiered by how we would
test it. The discipline differentiator: almost no unifying framework pre-registers its own
falsifiers; this is the spine that separates the testable claims from the [A]/[C] interpretive
frame.* Each prediction names a mechanism, a symmetric falsifier, and a discriminating variable.

## How to read the tiers
- **Status [P]/[A]/[C]** — proof tier of the *mechanism* (certified / structural identification / correspondence).
- **Test** — how a verdict is reached: **NOW** (runnable on hardware we have), **COMP** (exact computation), **PHYS** (an experiment/observation we await).
- Every entry is **symmetric**: a fixed KILL and a fixed CONFIRM, set before the verdict.

---

## Tier A — Machine learning / interpretability (testable now; no firewall)

### A1 · The Compositionality Tax (faithfulness phase boundary)
- **Claim:** an order-$m$ probe is faithful to an order-$k$ behavior **iff** $m\ge k$; faithfulness is a sharp step, and $\tau$ (the saturation order) = compositional depth.
- **Mechanism [P synthetic / A operational]:** moment-matched pairs (the $k$-th finite difference) are invisible below order $k$; degree-$m$ polynomial kernel = order-$m$ readout.
- **KILL:** faithfulness rises *smoothly* with $m$ (a ramp), or $\tau\ne k$ on controlled-order behaviors, or an $m{=}2$ probe reads a verified order-$\ge3$ conjunction.
- **CONFIRM:** a single sharp jump at $m=k$, $\tau=k$, robust across layers.
- **Discriminator:** the *shape* of faithfulness-vs-$m$ (step vs ramp).
- **Status:** synthetic **certified** (`compositionality_tax.py`, 8/8). **LLM test RUN (Pythia-410m, 2026-06-25): the SHARP form is FALSIFIED.** On real activations the accuracy *ramps* with probe order instead of stepping — a linear probe already scores 0.77 (k=2) / 0.60 (k=3,4), and τ=1,2,3 for k=2,3,4 (not τ=k). Cause: real PCA coordinates are correlated/asymmetric, so a k-parity of them is *not* orthogonal to lower-order polynomials (the clean boundary needs independent features — it holds synthetically, smears on real reps). **What survives:** the *graded* form — τ rises monotonically with k; higher-order behaviors do need higher-order probes, but as a continuous "effective order," not a threshold. **Reformulate** the tax as a continuous effective-order and re-run (and test ICA/whitened features for a sharper boundary). The sharp claim cannot lead the paper.

### A2 · Arrow = $b_1$
- **Claim:** a single-encoder (self-adjoint) objective is blind to the antisymmetric current; a two-sided predictor recovers **exactly $b_1$** irreversible modes (graph $\beta_1$, Hodge-collapsed to $b_1$ on filled complexes).
- **Mechanism [P]:** $A=\tfrac12(T-T^*)$ in the kernel of the quadratic form; stationary current is divergence-free → cycle space.
- **KILL:** recovered arrow dimension $\ne b_1$; or single-encoder recovers the arrow.
- **CONFIRM:** recovered modes $=b_1$ across graph families; predictor-head necessity.
- **Status:** **certified + tested** (E12, E16; E11 trained 2-encoder on GCP). Strongest empirical leg.

### A3 · Order-$r$ identifiability
- **Claim:** a rank-$r$ world is identified by matching the cumulant tower to order $r$ — necessary and sufficient; order-2 methods (LeJEPA's isotropic corner) fail at rank $>2$.
- **Mechanism [P]:** Apex identifiability (cumulant-tower matching).
- **KILL:** an order-2 method recovers genuine rank-3 structure; or order-$r$ matching fails to identify a rank-$r$ world.
- **CONFIRM:** identifiability onset exactly at order $=$ rank.
- **Status:** **certified** (apex_recovery e1/e2/e3); real-data test open.

### A4 · Dark structure in representations
- **Claim:** learned representations carry "dark structure" — content that drives outputs (gravitates) but is invisible to order-2 probes; the dark:visible ratio $>1$.
- **Mechanism [A]:** the faithfulness obstruction (order-$\ge3$ output-relevant, order-2-blind). The cosmology dark-matter idea transplanted to its testable home.
- **KILL:** order-2 probes capture $\ge50\%$ of output-relevant (causal/ablation) structure.
- **CONFIRM:** majority of causal structure is order-$\ge3$ (dark), measured as dark:visible = (R²₄−R²₂)/R²₂ of predicting next-token surprisal across layers.
- **Status:** **LLM test RUN (Pythia-410m, 2026-06-25): INCONCLUSIVE / measurement-limited** — NOT a clean falsification. The degree-3/4 kernels give *negative* held-out R² (they overfit before capturing any order-≥3 signal), so dark<0 everywhere and the verdict printed FALSIFY, but the mechanism is overfitting, not order-2 sufficiency — exactly the pre-registered curse-of-dimensionality caveat, which *dominated*. Cannot distinguish "no dark structure" from "unmeasurable." **Reliable sub-result:** R²₁≈R²₂ (≈0.30 vs 0.29 at the late layer) — surprisal is largely *linearly* decodable, little order-2 gain; order≥3 unmeasured. **Fix:** abandon the kernel-R² estimator; use a **Gaussian-surrogate causal test** (gaussianize activations → preserve mean+cov, destroy order-≥3 → measure output KL), which sidesteps overfitting entirely.

### A5 · Mid-depth localization of the blind spot
- **Claim:** the order-2-vs-order-3 faithfulness gap peaks at mid-depth layers.
- **Mechanism [A]:** V/M propagation (Paper 36 / κ-audit).
- **KILL:** the gap is depth-flat or peaks at the edges.
- **CONFIRM:** a mid-depth peak across models (κ-audit found ~L28/HF row 29 on one model).
- **Status:** **partial** (κ-audit, one model); generalization test open.

---

## Tier B — Number theory (exact computational falsification)

### B1 · HL $n$-tuple connected weight = apex $n$-th cumulant — **CONFIRMED, all orders**
- **Claim:** the connected (cumulant) part of the Hardy–Littlewood $k$-tuple singular series $= 1/\varphi(p)^n=1/(p-1)^n$ per prime on squarefree support, beyond order 2 (twin primes).
- **Mechanism [A→P]:** partition-lattice cumulant of the per-prime moments $M_s=(1-s/p)/(1-1/p)^s$.
- **KILL:** $C_4(p)$ not $c_4/(p-1)^4$. **CONFIRM:** clean power-$n$ totient denominator.
- **RESULT (exact, certified `hl_cumulant_order4.py`, hand-checked $C_3$):** **CONFIRMED** — all-orders closed form
  $$C_n(p) = -\frac{(n-1)!}{(p-1)^n} = -\frac{(n-1)!}{\varphi(p)^n},\qquad c_2{=}-1,\ c_3{=}-2,\ c_4{=}-6,\ c_5{=}-24,\ c_6{=}-120 = -(n-1)!.$$
- **Honest provenance:** this is *not new* — it is **N5 Thm 6.2** (κ_n^HL = −(n−1)!/φ(p)ⁿ, proven 2026-06-07 via generating functions). The subagent's contribution is an **independent re-derivation by a different, more elementary route** (the partition-lattice cumulant of the HL singular series directly), which *agrees exactly*. So B1 is a **doubly-proven theorem**, not a freshly-cracked open question — the right way to log it. The factorial numerator is firewall-legal (dimensionless), exact. `HL_cumulant_order4_RESULT.md`.

### B2 · $D_3=-787680$ family-wide moment barrier
- **Claim:** in the smooth-primorial family, only $2^n$ survives the degree-3 moment barrier.
- **KILL:** another smooth-primorial family survives. **CONFIRM:** exhaustive check leaves only $2^n$.
- **Status:** **certified** (smooth-primorial paper).

### B3 · $\tau_n=(-1)^n$ transfer
- **Claim:** the all-orders transfer coefficient is $(-1)^n$ (channel split even/$\zeta$ vs odd/$L(s,\chi_3)$).
- **KILL:** a computed $\tau_n\ne(-1)^n$. **CONFIRM:** closed form holds all orders.
- **Status:** **certified** (N5 Thm 6.2).

---

## Tier C — Physics (one bold thread; high visibility, currently losing)

### C1 · Rigid $w=-1$ (cosmology)
- **Claim:** dark energy is a rigid cosmological constant, $(w_0,w_a)=(-1,0)$ exactly, **non-tunable** ($K=\tfrac14$ is $Q$-independent).
- **KILL:** DESI-final + Euclid + $\ge2$ SN samples give $w_a\ne0$ at $\ge5\sigma$, sample-consistently and stably.
- **CONFIRM:** the signal regresses below $2\sigma$ as systematics resolve.
- **Discriminator:** supernova-sample dependence (real → converges & strengthens; systematic → stays sample-dependent).
- **Status:** **on record**, currently ~3σ **against** us (DR1+DR2); decidable 2027–28. Full pre-reg: `PREREG_w_eq_minus1_DESI.md`. On a kill, the D-II geometry survives — only the dimensionful cash-out fails.

---

## What is explicitly NOT a prediction (firewall + honesty)
- Absolute scales: $\Lambda$ value, $G$, $\hbar$, $c$, particle masses, $H_0$ — out of scope by the §12 firewall (the firewall-crossing sandbox showed everything is fixed *modulo one undetermined scale* $M_0$).
- Density budget $\Omega_\Lambda/\Omega_m$ — a clock reading (time-dependent), not a constant; declined by design.
- Rejected numerical coincidences (no mechanism): $\beta_\infty\!\approx\!n_s$ (1.1%), $K\!\approx\!\Omega_{cdm}$ (5.5%), $3/8\!\approx\!\Omega_m$ (19%).
- The colloquial "meaning/consciousness" identifications — [C] correspondences, not predictions.

## Publication posture
Lead with **Tier A** (theorem + measuring stick + runnable falsifiers; the ML/AI-safety paper "The
Faithfulness Ceiling"). Carry **B** as exact-math results. Keep **C** as the single bold physical
thread. Fence the unifying frame (meaning/mass/intelligence/time) as a separate, clearly-tiered
"perspective" piece, published *after* the spine earns trust. This registry is itself a publishable
artifact — the pre-registered falsifier set is the credibility moat.
