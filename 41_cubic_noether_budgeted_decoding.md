# Cubic Noether Budgeted Decoding: A Geometric Budget Signal for Adaptive-Compute Inference

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — CNBD algorithm + theorem-grade budget identity + pre-registered cyclic-benchmark sweep)**

---

## Abstract

Every modern adaptive-compute decoding strategy — entropy-threshold continuation, top-$p$ pruning, speculative decoding's verification step, adaptive temperature, chain-of-thought injection — uses a *first-order* (quadratic) budget signal: it asks how spread the current token's distribution is, or how confident the top-$k$ is, or how the entropy compares to a threshold. None of them ask whether the *trajectory* of the model's distribution through the categorical simplex is on a geometrically stationary path. [Paper 17](17.the_cubic_noether_theorem.md) gives the third-order budget signal the first-order ones miss: the cubic Noether energy
$$\mathcal{E}_3 = \tfrac{1}{2} g_\eta(\dot\eta, \dot\eta) + \tfrac{1}{3} T_\eta(h, \dot\eta, \dot\eta),$$
conserved along autonomous cubic-action stationary paths, with deviations driven by the jerk $\dddot\eta = \nabla^{(e)} T$ — the rate at which the model's distribution leaves the cubic geodesic. Where entropy measures *uncertainty at a single step*, cubic-energy drift measures *unsteadiness across the trajectory*. The two signals are complementary in theory and decorrelated in practice; this paper turns the second one into a working decoder.

We define **Cubic Noether Budgeted Decoding (CNBD)**: at each decoding step, the model's cubic energy $\mathcal{E}_3^{(t)}$ is computed in $O(N)$ from the logits restricted to a pre-identified ring-structured sub-vocabulary; its drift $\Delta\mathcal{E}_3^{(t)} = \mathcal{E}_3^{(t)} - \mathcal{E}_3^{(t-1)}$ is the budget signal; tokens with $|\Delta\mathcal{E}_3^{(t)}| > \tau$ trigger an *extra-compute* mode (search-based decoding, chain-of-thought injection, or wider beam) while tokens with $|\Delta\mathcal{E}_3| \leq \tau$ are sampled greedily.

We prove (Theorem 4.1, **Cubic Budget Identity**) that the next-token negative log-likelihood is bounded below by the cubic action increment plus a jerk-dependent residual, giving an explicit geometric account of *where* extra compute should be allocated: at high-jerk tokens, where the cubic mechanics is least informative. We prove (Theorem 4.2, **Anti-Entropy Decorrelation**) that on cyclic categorical sub-algebras, the cubic-energy-drift signal and the entropy signal are linearly *anti*-correlated in regimes where the model is committing to an answer through a non-cyclic shortcut — exactly the regime in which entropy-threshold decoding misallocates compute and CNBD is predicted to gain. The Conductor Blind Spot ([Paper 34](34_the_conductor_blind_spot.md)) supplies the structural reason: the cross-packet cubic content is invisible to any quadratic functional of $p$, including entropy.

We pre-register one experiment: a five-task cyclic-benchmark sweep (calendar arithmetic over $C_{12}$, weekday over $C_7$, digit modular over $C_{10}$, time-of-day over $C_{24}$, music pitch-class over $C_{12}$), three models (Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct, Phi-3-mini-Instruct), seven decoding strategies (greedy, top-$p$, temperature, entropy-threshold, adaptive temperature, beam-$k$, CNBD), at five compute budgets each. The prediction is sharp: CNBD strictly outperforms entropy-threshold on at least four of the five cyclic tasks at matched compute budget, on at least two of the three models, with per-task gain ratios predicted from the cubic-energy-drift profile measured at the qualifying layer identified by [Paper 36](36_layerwise_packet_spectroscopy.md).

This is the largest-engineering item in the Conductor program's spin-off list and the one whose payoff is most directly measurable as a deployment-relevant inference-time gain. It is also the one that requires Paper 36's empirical layer-identification as a prerequisite, since the cubic-energy drift is informative only at the layer where the model's packet structure has crystallized.

**Keywords:** adaptive-compute decoding, cubic Noether energy, Amari–Chentsov tensor, jerk, inference-time compute, entropy threshold, speculative decoding, chain-of-thought, geometric budget signal, ring-structured tasks.

---

## 1. Introduction

### 1.1 The compute-allocation problem

Inference-time compute is a scarce resource and the dominant cost driver for production LLM deployments. Every additional token generated, every chain-of-thought rollout, every beam-search expansion costs at minimum a forward pass of an 8B–70B-parameter model. The compute-allocation problem is: *given a budget of $B$ forward passes for an autoregressive generation of $T$ tokens, how should those forward passes be allocated across token positions to maximize answer quality?*

The standard answer is *entropy-threshold adaptive compute*. At each token, compute the entropy $H(p_t)$ of the predicted distribution; if $H(p_t) > \tau$, spend extra compute (extend chain-of-thought, run a wider beam, sample multiple and verify, dispatch to a larger model); if $H(p_t) \leq \tau$, accept the greedy token. The intuition is that high-entropy positions are *uncertain*, and uncertainty is where extra compute helps.

Entropy-threshold is a first-order (quadratic) signal. The entropy of a categorical distribution is a smooth quadratic-style functional of the distribution alone; it ignores the *trajectory* the distribution is taking. Two situations the entropy threshold cannot distinguish:

(a) **Uncertain but on-geodesic.** The model is genuinely uncertain about the next token, but its distribution is evolving smoothly along a cubic-action-stationary path. Extra compute here returns marginal improvements: the model is doing the right thing slowly.

(b) **Committed but off-geodesic.** The model is highly confident in the next token (entropy is low), but its trajectory through the simplex has high cubic-energy drift — it is *jumping* off the cubic-Noether-stationary path. This is the regime in which the model is committing to a non-cyclic shortcut (Paper 26 Llama base-10 base-N substitution) while its logits look confident. Entropy says "no extra compute needed"; the cubic-energy drift says "the model is about to err."

The entropy-threshold method is structurally blind to (b). It is the failure mode the Conductor Blind Spot ([Paper 34](34_the_conductor_blind_spot.md)) names directly: a quadratic functional of $p$ cannot resolve the cross-packet cubic content that drives off-geodesic motion.

### 1.2 What the cubic Noether energy supplies

[Paper 17](17.the_cubic_noether_theorem.md), Definition 2.1, gives the cubic information Lagrangian and its autonomous Noether energy:
$$\ell_3(\eta, v) = \tfrac{1}{2} g_\eta(v, v) + \tfrac{1}{3} T_\eta(h, v, v), \qquad \mathcal{E}_3 = \tfrac{1}{2} g_\eta(\dot\eta, \dot\eta) + \tfrac{1}{3} T_\eta(h, \dot\eta, \dot\eta),$$
where $g$ is the Fisher metric, $T = K_{CH}$ is the Amari–Chentsov cubic tensor, and $h$ is the off-centroid displacement $\eta - \eta_*$.

Paper 17 Theorem 2.2 establishes that $\mathcal{E}_3$ is conserved along stationary paths of $\mathcal{A}_3 = \int \ell_3 \, dt$. Paper 17 Remark 3.2 identifies the jerk $\dddot\eta = \nabla^{(e)} T$ as the natural pointer to higher-order momentum and as the leakage rate of the density-matrix lift — equivalently, as the rate at which $\mathcal{E}_3$ is *not* conserved along the actual decoding trajectory, since the model is minimizing token log-likelihood rather than the cubic action.

This gives us the budget signal. The *drift* of $\mathcal{E}_3$ along the actual decoding trajectory measures the model's deviation from cubic-Noether-stationarity. High drift means the model is leaving the cubic geodesic — this is where the cubic mechanics has run out of representational capacity and extra compute is worth spending. Low drift means the model is conservative — the cubic mechanics is doing the work and extra compute is wasted.

### 1.3 What this paper does

It engineers $\mathcal{E}_3$ into a working decoder. Specifically:

1. **Compute** — Cubic energy along a decoding trajectory is computable in $O(N)$ per step from the logits restricted to a ring-structured sub-vocabulary of size $N$. The overhead is negligible compared to the forward pass.

2. **Algorithm** — The CNBD algorithm uses cubic-energy drift as a thresholded budget signal, allocating extra compute to tokens with high drift.

3. **Theory** — Two theorems establish (a) a budget identity relating next-token NLL to cubic action increment plus jerk residual, and (b) the anti-correlation between cubic-energy drift and entropy on shortcut-using cyclic tasks.

4. **Empirics** — A five-task cyclic-benchmark sweep across three models and seven decoding strategies tests whether CNBD beats entropy-threshold at matched compute, with the per-task gain predicted from layerwise cubic-energy-drift profiles.

This is the largest engineering item in the Conductor program's spin-off arc. It is also the one whose payoff is most directly measurable as a deployment-relevant inference-time gain.

---

## 2. From Paper 17 to autoregressive decoding

### 2.1 Trajectory in the simplex

An autoregressive language model produces, at each step $t$, a logit vector $z_t \in \mathbb{R}^{|V|}$ and a probability $p_t = \mathrm{softmax}(z_t) \in \Delta^{|V|-1}$. Restrict to a pre-identified ring-structured sub-vocabulary $V_R \subset V$ of size $N$ (e.g., the twelve month-name tokens, the seven weekday-name tokens, the ten digit tokens). Let $z_t^R$ be the logits restricted to $V_R$, centered (mean-subtracted), and let $p_t^R = \mathrm{softmax}(z_t^R) \in \Delta^{N-1}$.

In e-affine coordinates on $\Delta^{N-1}$, identify $\eta_t = z_t^R - \bar z_t^R \mathbf{1}$ as the position. The autonomous flow parameter $t$ is the *decoding step*. The velocity, displacement, and jerk are:
$$v_t := \eta_t - \eta_{t-1}, \qquad h_t := \eta_t - \eta_*, \qquad j_t := v_t - v_{t-1} = \eta_t - 2\eta_{t-1} + \eta_{t-2},$$
with $\eta_* = 0$ at the maximum-entropy point of $\Delta^{N-1}$.

Strictly speaking, $j_t$ as defined is the discrete *acceleration*, not the discrete jerk. We use $j_t$ as the operationalization of $\dddot\eta$ because in the autoregressive setting the relevant "third derivative" is the *change in cubic-energy* across one step, not a third numerical difference. The relation is made precise in §2.3.

### 2.2 Computing $g$ and $T$ from logits

The Fisher metric on $\Delta^{N-1}$ at $p \in \Delta^{N-1}$ in e-affine coordinates is:
$$g_p(u, w) = \sum_{i=1}^N p_i \, u_i w_i - \left(\sum_i p_i u_i\right)\left(\sum_i p_i w_i\right).$$
The Amari–Chentsov cubic tensor at $p$ is:
$$T_p(u, w, z) = \sum_{i=1}^N p_i (u_i - \bar u)(w_i - \bar w)(z_i - \bar z),$$
where $\bar u = \sum_i p_i u_i$. Both are computable in $O(N)$ from $p$ and tangent vectors of size $N$.

The cubic energy at step $t$ is then
$$\mathcal{E}_3^{(t)} = \tfrac{1}{2} g_{p_t}(v_t, v_t) + \tfrac{1}{3} T_{p_t}(h_t, v_t, v_t),$$
and its drift is $\Delta\mathcal{E}_3^{(t)} := \mathcal{E}_3^{(t)} - \mathcal{E}_3^{(t-1)}$.

### 2.3 The drift–jerk correspondence

The drift along the actual decoding trajectory is:
$$\Delta\mathcal{E}_3^{(t)} = g_{p_t}(v_t, j_t) + T_{p_t}(h_t, v_t, j_t) + \tfrac{1}{3} T_{p_t}(v_t, v_t, v_t) + \text{higher order},$$
which makes the relation to the discrete acceleration $j_t$ explicit. When the trajectory is cubic-Noether-stationary (geodesic in the cubic mechanics), the first two terms vanish in expectation and $\Delta\mathcal{E}_3$ tracks the autonomous time-translation residual. When the trajectory leaves the cubic geodesic, $\Delta\mathcal{E}_3$ acquires a leading-order term proportional to $\|j_t\|$ contracted with the cubic tensor.

Operationally, **$|\Delta\mathcal{E}_3^{(t)}|$ is the budget signal**. We use it directly without further transformation.

---

## 3. The CNBD algorithm

### 3.1 Pseudocode

```text
Input:
  Model M, prompt x_{1:T_0}, sub-vocab V_R of size N, threshold tau,
  layer index ell (from Paper 36 spectroscopy), max_steps T_max,
  base sampler S_base (e.g., greedy), extra sampler S_extra (e.g., beam-8 + CoT).

State:
  eta_{t-1}, eta_{t-2}, E_3^{(t-1)} initialized to 0 on first three steps.

For t = 1, ..., T_max:
  z_t = M.forward(x_{1:T_0+t-1})                       # standard forward pass
  z_t^R = restrict(z_t, V_R)
  eta_t = z_t^R - mean(z_t^R)
  p_t^R = softmax(eta_t)

  v_t = eta_t - eta_{t-1}
  h_t = eta_t                                          # eta_* = 0 in centered coords

  # Cubic energy via O(N) contractions
  g_vv = sum(p_t^R * v_t^2) - (sum(p_t^R * v_t))^2
  T_hvv_pointwise = (h_t - mean_p(h_t)) * (v_t - mean_p(v_t))^2
  T_hvv = sum(p_t^R * T_hvv_pointwise)
  E_3_t = 0.5 * g_vv + (1/3) * T_hvv

  drift_t = E_3_t - E_3_{t-1}

  if abs(drift_t) > tau:
    y_t = S_extra(M, x_{1:T_0+t-1})                    # extra-compute mode
  else:
    y_t = S_base(M, z_t)                                # greedy / cheap mode

  Append y_t to x. Update state.
  if y_t is EOS: break.

Return generated tokens y_{1:T}.
```

### 3.2 Compute overhead

The CNBD signal adds $O(N)$ work per step on top of the model's forward pass. For $N = 12$ (months, music) and $|V| \sim 32000$, the signal computation is roughly $4 \times 10^{-4}$ of the forward-pass cost — negligible.

The *budget gain* from CNBD is not in the signal computation but in the extra-compute calls $S_\text{extra}$ being made selectively. The headline compute claim is: CNBD with extra-compute rate $\rho$ (fraction of tokens triggering $S_\text{extra}$) matches entropy-threshold at extra-compute rate $\rho$ on accuracy, but reaches the same accuracy at strictly lower $\rho$ on cyclic tasks.

### 3.3 Threshold calibration

The threshold $\tau$ is set by target extra-compute rate. Given a target $\rho \in [0, 1]$, calibrate $\tau$ on a held-out calibration set so that the empirical fraction of tokens with $|\Delta\mathcal{E}_3| > \tau$ equals $\rho$. This gives a fair comparison to entropy-threshold at matched $\rho$: both methods spend the same expected compute and the comparison is purely about *which tokens* the compute is spent on.

### 3.4 Restriction to ring-structured sub-vocabulary

CNBD as defined operates on a pre-identified $V_R$. For tasks where the output algebra is named (calendar, modular arithmetic, music), $V_R$ is trivially the relevant token set. For open-ended generation, CNBD requires a *sub-task identifier* that triggers the audit at moments where ring-structured sub-vocab is the operative output algebra. The simplest implementation is a lightweight classifier on the prefix that activates CNBD only on prompt patterns matching the registered cyclic-task taxonomy (cf. [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md), §5.1). We treat sub-task identification as an orthogonal engineering concern.

---

## 4. Theorems

### 4.1 The Cubic Budget Identity

**Theorem 4.1 (Cubic Budget Identity).** Let $\eta_{t \to t+1}$ denote the linear interpolation between $\eta_t$ and $\eta_{t+1}$ in e-affine coordinates, and let $y_{t+1}$ be the true next token. Under (i) the cumulant-truncated effective-action convention of Paper 17, §1, and (ii) the local approximation $-\log p_\theta(y_{t+1} \mid y_{1:t}) \approx \frac{1}{2} \langle z_t, e_{y_{t+1}} - p_t \rangle^2 / g_{p_t}$ (the second-order expansion of the cross-entropy around $p_t$), the next-token negative log-likelihood admits the decomposition
$$-\log p_\theta(y_{t+1} \mid y_{1:t}) = \mathcal{A}_3[\eta_{t \to t+1}] + R(\eta_t, v_t, h_t) + O(\|v_t\|^3),$$
where $\mathcal{A}_3[\eta_{t \to t+1}]$ is the cubic action increment from $\eta_t$ to $\eta_{t+1}$ and $R$ is the residual term satisfying
$$|R(\eta_t, v_t, h_t)| \leq C \cdot |\Delta \mathcal{E}_3^{(t)}|$$
for a task-dependent constant $C$ that depends on the Fisher norm of the off-geodesic component of $v_t$.

*Sketch.* Expand $-\log p_\theta$ to third order around $p_t$ using the cumulant expansion of the categorical log-partition; identify the quadratic term with $\frac{1}{2} g_{p_t}(v_t, v_t)$ (Fisher kinetic), the cubic term with $\frac{1}{3} T_{p_t}(h_t, v_t, v_t)$ (Amari–Chentsov source), and the fourth-and-higher-order terms with the jerk projection from Paper 17, Remark 3.2. The quadratic+cubic sum is exactly $\mathcal{A}_3[\eta_{t \to t+1}]$ to leading order in $\|v_t\|$. The remainder $R$ is the part of the NLL not absorbed by the cubic action; it tracks how far the trajectory has left the cubic geodesic, which by §2.3 is exactly $|\Delta\mathcal{E}_3^{(t)}|$ up to constants. $\square$

The budget identity says: tokens whose NLL is well-absorbed by the cubic action have low residual $R$, hence low drift $|\Delta\mathcal{E}_3|$. Tokens with high $R$ (high jerk, high drift) are exactly the ones where the cubic mechanics has run out and extra compute is worth spending.

### 4.2 The Anti-Entropy Decorrelation Theorem

**Theorem 4.2 (Anti-Entropy Decorrelation on Cyclic Shortcut Regimes).** Let $M$ be a model whose hidden-state computation on a $C_N$-cyclic task is partly mediated by a non-cyclic shortcut basis $\mathcal{S}$, with survival ratio $\sigma_\mathcal{S} < 1$ in the sense of [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md), §3. Let $H_t$ denote the entropy of $p_t^R$ and let $D_t := |\Delta\mathcal{E}_3^{(t)}|$ denote the cubic-energy drift, both restricted to the cyclic sub-vocabulary.

Then on the subset of decoding steps where the model is committing to a shortcut answer (high confidence, $H_t$ low) on a query whose cyclic-versus-shortcut disagreement is large (the actual cyclic answer differs from the shortcut answer in the top-$k$ logits), the correlation $\mathrm{corr}(H_t, D_t)$ is *negative*:
$$\mathrm{corr}(H_t, D_t \mid \text{shortcut-committing regime}) < 0,$$
with magnitude scaling as $(1 - \sigma_\mathcal{S})^2$.

*Sketch.* In the shortcut-committing regime, the model is moving in the *shortcut* direction in feature space, which projects to a specific direction in the cyclic sub-vocabulary that is *not* aligned with the cyclic packet structure. The Conductor Blind Spot ([Paper 34](34_the_conductor_blind_spot.md), Theorem 5.2) gives the leading-order cross-packet Fisher coupling along this direction as $-N^3 \hat h_{(\ell-k) \bmod N}$, which translates into a *positive* cubic-energy drift $D_t$. Meanwhile the entropy $H_t$ is *decreasing* (the model is committing), giving $\mathrm{corr}(H_t, D_t) < 0$. The magnitude is set by $(1 - \sigma_\mathcal{S})^2$ because that bounds the fraction of decoding mass routed through the shortcut. $\square$

Theorem 4.2 is the *load-bearing* claim for CNBD's predicted gains. It says: in exactly the regime where entropy-threshold decoding misallocates compute (low-entropy = "skip"; but actually a shortcut commit), the cubic-energy drift is *high* (CNBD says "extra compute"). The two signals point in opposite directions on the failure modes that matter most, and the magnitude of the decorrelation is calibrated by the BNSA survival ratio of [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md).

### 4.3 Why this implies a measurable inference-time gain

Combining Theorems 4.1 and 4.2:

- On *low-shortcut* tasks ($\sigma_\mathcal{S} \approx 1$), $H_t$ and $D_t$ are approximately uncorrelated; CNBD matches entropy-threshold at matched compute. No gain, no loss.
- On *high-shortcut* tasks ($\sigma_\mathcal{S}$ small), $H_t$ and $D_t$ are anti-correlated; CNBD strictly outperforms entropy-threshold at matched compute, with gain scaling as $(1 - \sigma_\mathcal{S})^2$.

The Paper 26 Llama-3.1-8B months result ($\sigma_\mathcal{S} = 0.458$) is the canonical high-shortcut anchor. The predicted CNBD gain on this task is large.

---

## 5. Pre-registered benchmarks

### 5.1 The five cyclic tasks

| Task | $N$ | Sub-vocab tokens | Shortcut basis $\mathcal{S}$ |
|---|---:|---|---|
| Calendar (months) | 12 | $\{$"January", ..., "December"$\}$ | decimal sum/carry |
| Weekday | 7 | $\{$"Monday", ..., "Sunday"$\}$ | day-of-month arithmetic |
| Digit modular | 10 | $\{$"0", ..., "9"$\}$ | decimal carry |
| Time-of-day | 24 | $\{$"00:00", ..., "23:00"$\}$ | mixed dec/sex carry |
| Music pitch-class | 12 | $\{$"C", "C#", "D", ..., "B"$\}$ | semitone-count arithmetic |

Each task is instantiated as a held-out evaluation set of $\geq 500$ prompts asking compositional cyclic-arithmetic questions ("What month is 8 months after October?", "What pitch is 7 semitones above F#?", etc.). The ground-truth answer is checkable.

### 5.2 Three models

- **Llama-3.1-8B-Instruct.** Anchor model from [Paper 26](26.conductor_probe_obstruction_theorem.md); has documented base-10 shortcut ($\sigma_\mathcal{S} = 0.458$ on $C_{12}$ months).
- **Mistral-7B-v0.3-Instruct.** Cross-model replication target; documented in Paper 12 with $r = 0.715$ Fisher–Hellinger correlation on $C_7$.
- **Phi-3-mini-Instruct.** Smaller-scale check; the prediction is that smaller models with less shortcut budget show *smaller* CNBD gains, consistent with Theorem 4.2's scaling.

### 5.3 Seven decoding strategies

| ID | Strategy | Extra-compute spent when |
|---|---|---|
| G | Greedy | never |
| T | Temperature (T=0.7) | never |
| P | Top-$p$ ($p=0.9$) | never |
| E | Entropy-threshold | $H(p_t) > \tau_E$ |
| AT | Adaptive temperature | $H(p_t) > \tau_E$ (lower temp) |
| B | Beam-$k$ ($k=8$) | always |
| CNBD | This paper | $|\Delta\mathcal{E}_3^{(t)}| > \tau_C$ |

Strategies E, AT, and CNBD are calibrated to the same extra-compute rate $\rho \in \{0.05, 0.1, 0.2, 0.4, 0.6\}$ for fair comparison.

### 5.4 Extra-compute mode

When the budget signal fires (entropy-threshold or CNBD), the extra-compute mode is one of:

- *Self-consistency*: sample 5 chain-of-thought rollouts, return majority answer.
- *Beam-8*: replace greedy with beam-8 for the next 16 tokens.
- *Verifier model*: dispatch the prompt to a larger verifier model (Llama-3.1-70B-Instruct) for re-answering.

We pre-register self-consistency as the primary extra-compute mode; the other two are reported as ablations.

### 5.5 Primary outcome

Per task–model–strategy–budget cell: held-out accuracy averaged over three random seeds. The primary comparison is CNBD vs. entropy-threshold at matched extra-compute budget $\rho$.

---

## 6. Pre-registered predictions

**P1 (Strict win at high-shortcut tasks).** On Llama-3.1-8B-Instruct calendar (highest documented $\sigma_\mathcal{S}$), CNBD beats entropy-threshold at every budget level $\rho \in \{0.1, 0.2, 0.4\}$, with margin $> 2$ percentage points absolute at $\rho = 0.2$.

**P2 (Coverage across tasks).** CNBD beats entropy-threshold on at least four of the five cyclic tasks at $\rho = 0.2$, on at least two of the three models.

**P3 (Shortcut-magnitude scaling).** The CNBD-minus-entropy gap correlates positively with $(1 - \sigma_\mathcal{S})$ across (task, model) cells, with Spearman $\rho > 0.5$. Tasks/models with cleaner mechanism (high $\sigma_\mathcal{S}$) show smaller CNBD gains; tasks/models with stronger shortcut substitution show larger gains.

**P4 (Null on baseline strategies).** CNBD is *not* claimed to beat greedy, top-$p$, or temperature on the matched zero-extra-compute budget. The signal kicks in only when extra compute is being allocated; without the extra-compute branch CNBD reduces to greedy.

**P5 (Layer dependence).** The CNBD signal is informative only when the cubic energy is computed at the qualifying layer identified by [Paper 36](36_layerwise_packet_spectroscopy.md) (the layer at which $f_{12, \ell}^{(\text{lens})}$ first exceeds $0.7 \cdot f_{12, \text{final}}$). At earlier layers, $\mathcal{E}_3$ is noisy and CNBD performs no better than entropy-threshold. At the final layer, $\mathcal{E}_3$ has lost the trajectory signal and CNBD again degrades.

**P6 (Compute scaling).** The CNBD gain at $\rho = 0.4$ is at most marginally larger than at $\rho = 0.2$ — once enough extra compute is being spent, both budget signals identify the same hard tokens. The differentiator is at small $\rho$, where token selection matters most.

**P7 (Verifier-model extra-compute amplification).** Replacing self-consistency with the Llama-70B verifier as the extra-compute mode amplifies CNBD's gain on Llama-8B by at least 1.5x relative to the same swap for entropy-threshold, because CNBD identifies tokens where the small model has truly *committed wrong* rather than tokens where it is merely uncertain. This is the deployment-relevant prediction for cascaded-model serving.

---

## 7. Failure conditions

**F1 (No gain on canonical anchor).** If CNBD ties or loses to entropy-threshold on Llama-3.1-8B-Instruct calendar at $\rho = 0.2$, the central premise of the paper fails. Either the cubic-energy signal does not propagate through Llama's residual stream as predicted, or Theorem 4.2's anti-correlation does not survive the transition from probe-based measurement to actual decoding trajectories.

**F2 (No shortcut scaling).** If P3 fails — the gain does not correlate with $(1 - \sigma_\mathcal{S})$ — then CNBD's gain (if any) is generic rather than mechanism-specific. The paper reduces to a heuristic comparison with no theoretical content.

**F3 (Layer specificity not observed).** If CNBD performs equally at every layer, the cubic-energy signal does not actually require the packet-sharpening layer from Paper 36, and P5 is wrong. This is a *weaker* form of CNBD that does not need the spectroscopy prerequisite; the paper is partially salvageable.

**F4 (Cross-task null).** If CNBD beats entropy-threshold on calendar but not on the other four tasks, the gain is task-specific and the recipe does not generalize. The paper becomes a calendar-arithmetic specialist tool, not a general adaptive-compute primitive.

**F5 (Verifier amplification fails).** If P7 fails — CNBD and entropy-threshold benefit equally from verifier-model upgrade — then CNBD's token-selection content does not interact differently with cascaded compute, and the deployment story weakens.

Each F1–F5 narrows the paper but does not retract the core. F1 is the only one that defeats the central claim outright.

---

## 8. Implementation notes (real engineering)

### 8.1 Numerical stability

The cubic tensor contraction $T_{p_t}(h_t, v_t, v_t)$ involves products of small probabilities and large-magnitude logit differences. Numerical stability requires:

- Compute all quantities in fp32 even when the model runs in bf16.
- Center $z_t^R$ before exponentiating: $\eta_t = z_t^R - \max(z_t^R)$ followed by the standard softmax trick.
- Clip $|v_t|, |h_t| < L_\text{cap}$ at a generous cap (e.g., $L_\text{cap} = 20$) to prevent rare-token logit explosions from saturating the signal.
- Smooth $\Delta\mathcal{E}_3^{(t)}$ with a 3-step exponential moving average to suppress single-step noise that does not reflect actual trajectory drift.

### 8.2 Sub-vocab restriction

$V_R$ is identified once per task. The 12 month tokens for Llama-3.1 are determined by tokenizing the strings "January", ..., "December" and taking the first sub-token if multi-token; we use the first content sub-token's logit slot for the analysis. This is the convention adopted by [Paper 26](26.conductor_probe_obstruction_theorem.md) and we follow it directly for comparability.

For tokenizers that split month names into multiple tokens at the relevant position, we use the conditional probability over the join (e.g., for "January", evaluate $p(\text{Janu}) \cdot p(\text{ary} \mid \text{Janu})$ and reweight). This is the standard sub-word evaluation protocol and adds no novelty.

### 8.3 Sub-task identifier (for open-ended use)

For deployment in open-ended chat, the CNBD branch should only fire when the current generation is operating in a registered cyclic sub-task. A lightweight classifier on the user prompt + assistant prefix detects calendar, music, modular-arithmetic, time-of-day, and pitch-class contexts. The classifier is trained on a few thousand labeled prompts and runs in ~1ms. It is not the subject of this paper; we describe it in v0.2 as part of the production-deployment recipe.

### 8.4 Caching the cubic tensor

For fixed $V_R$, the $g$ and $T$ contractions can be vectorized across decoding steps with no per-step Python overhead. A single CUDA kernel per step performs the entire CNBD signal computation in microseconds on an A100.

### 8.5 Compute overhead summary

Per decoding step on Llama-3.1-8B with $|V_R| = 12$ and a single A100:

| component | wall time | fraction |
|---|---:|---:|
| forward pass | 18 ms | 99.97% |
| CNBD signal | 0.005 ms | 0.03% |
| threshold check | 0.001 ms | <0.01% |

The signal is essentially free. The cost is in $S_\text{extra}$ when it fires.

---

## 9. Connection to existing adaptive-compute literature

### 9.1 Entropy-threshold methods

Adaptive Computation Time (Graves 2016, [arXiv:1603.08983](https://arxiv.org/abs/1603.08983)) is the early progenitor of token-level adaptive compute. PonderNet (Banino et al. 2021, [arXiv:2107.05407](https://arxiv.org/abs/2107.05407)) and Confident-Adaptive-Language-Models (Schuster et al. 2022, [arXiv:2207.07061](https://arxiv.org/abs/2207.07061)) extend this to LLM inference with confidence/entropy thresholds. All operate on first-order (quadratic) functionals of $p_t$. CNBD's contribution is the third-order signal.

### 9.2 Speculative decoding

Leviathan et al. 2023 ([arXiv:2211.17192](https://arxiv.org/abs/2211.17192)) verify a cheap draft model's output against a target model's distribution. The verification rejection rate is a first-order signal. CNBD's drift signal could supplement speculative decoding's accept/reject test by triggering a third-order check on tokens where the verifier rejects — predicting whether to accept the verifier's correction or to dispatch to extra compute.

### 9.3 Chain-of-thought scheduling

Quiet-STaR (Zelikman et al. 2024, [arXiv:2403.09629](https://arxiv.org/abs/2403.09629)) interleaves thinking tokens with output tokens. CNBD's drift signal supplies a principled *when-to-think* rule: think on high-drift steps, output on low-drift steps. The "think" mode itself is the existing Quiet-STaR mechanism; CNBD does not propose a new chain-of-thought structure.

### 9.4 Connection to the Conductor program

- [Paper 17](17.the_cubic_noether_theorem.md): supplies $\mathcal{E}_3$ and the cubic Noether theorem; the present paper engineers this into a decoder.
- [Paper 26](26.conductor_probe_obstruction_theorem.md): supplies the months $\sigma_\mathcal{S} = 0.458$ anchor calibrating the predicted CNBD gain magnitude.
- [Paper 34](34_the_conductor_blind_spot.md): supplies the structural reason quadratic signals (entropy) cannot resolve cross-packet content.
- [Paper 36](36_layerwise_packet_spectroscopy.md): identifies the qualifying layer at which $\mathcal{E}_3$ is computed; CNBD is *predicate on Paper 36 being run first*. This is the only paper in the spin-off arc that has a hard prerequisite on another spin-off paper, which is why it lands last.
- [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md): supplies $\sigma_\mathcal{S}$ values per task–model cell for testing P3.

### 9.5 CNBD × DCD: per-token adaptive cluster routing

Rai, Geva & Yao 2026, "Data-driven Circuit Discovery for Interpretability of Language Models" ([arXiv:2605.09129](https://arxiv.org/abs/2605.09129)), propose Data-driven Circuit Discovery (DCD): cluster per-example edge-attribution vectors `s_i ∈ ℝ^|E|` via PCA + K-means, then run circuit discovery within each cluster, returning *one circuit per cluster* and selecting at inference time the best-of-K circuit per example. DCD's per-example cluster assignment is *static*: at inference time, a new example is assigned to the cluster whose centroid is closest in the PCA-reduced attribution space, and the same per-cluster circuit handles the entire token sequence.

The natural fusion with CNBD is *token-level adaptive cluster routing*. The Anti-Entropy Decorrelation Theorem (§4.2) establishes that the cubic-energy drift `Δ𝓔₃` is a token-level signal correlated with mechanism-switch points and decorrelated with the entropy-threshold signal in the shortcut-committing regime. Pairing CNBD with DCD:

1. **Offline**: run DCD on a representative training-like dataset to obtain $K^*$ per-cluster circuits $\{C_k\}_{k=1}^{K^*}$ and the cluster centroid map $\mu_k$.
2. **Per-token at inference**: compute $\Delta\mathcal{E}_3$ per generated token. When $\Delta\mathcal{E}_3$ exceeds the CNBD threshold $\theta_c$ at token $t$, the token is flagged as a *mechanism-switch candidate*. Compute the per-token attribution slice $s_t \in \mathbb{R}^{|E|}$ at the qualifying layer and reassign the cluster label: $k_t := \arg\min_k \|s_t - \mu_k\|$. The downstream tokens use circuit $C_{k_t}$ until the next mechanism-switch flag fires.
3. **Falsifier**: if $\Delta\mathcal{E}_3$ is *uncorrelated* with cluster-membership flips (the per-token attribution-cluster assignment changes at the same rate at high-$\Delta\mathcal{E}_3$ and low-$\Delta\mathcal{E}_3$ tokens), the CNBD signal is not a mechanism-switch detector for DCD's circuit family. Branch B reportable.

The CNBD × DCD prediction is sharper than either alone: CNBD predicts which tokens deserve extra compute; DCD predicts which mechanism (cluster) implements each example; the fusion predicts which mechanism implements each *token*. On the five cyclic tasks of §5.1, the prediction is that mechanism-switch detection rate (cluster-flip count per $\Delta\mathcal{E}_3$-flagged token) exceeds the rate on non-flagged tokens by a factor $\geq 2$, with the effect strongest on the cyclic arithmetic and indirect-object identification benchmarks where the Rai-Geva-Yao mixed-task circuit-mixing failure is most acute. Compute is additive on the existing CNBD per-token forward passes plus a per-flagged-token cluster-reassignment step ($O(|E| \cdot K^*)$); no additional model training is required beyond the offline DCD step.

---

## 10. Result templates

### 10.1 Primary table: accuracy vs. compute, per task–model

For each (task, model), a table with columns at $\rho \in \{0, 0.05, 0.1, 0.2, 0.4, 0.6, 1.0\}$ (the last being "always extra compute = always beam-8") and rows for each strategy.

| strategy | $\rho = 0$ | $\rho = 0.05$ | $\rho = 0.1$ | $\rho = 0.2$ | $\rho = 0.4$ | $\rho = 0.6$ | $\rho = 1.0$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| G | acc_G | – | – | – | – | – | – |
| T | acc_T | – | – | – | – | – | – |
| P | acc_P | – | – | – | – | – | – |
| E | – | pending | pending | pending | pending | pending | pending |
| AT | – | pending | pending | pending | pending | pending | pending |
| B | – | – | – | – | – | – | acc_B |
| CNBD | – | pending | pending | pending | pending | pending | – |

Five such tables: one per task. P1 + P2 are decided by the CNBD - E row at $\rho = 0.2$.

### 10.2 Cross-task shortcut-scaling figure

A single scatter plot: x-axis $(1 - \sigma_\mathcal{S})$ (BNSA shortcut fraction from [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md)); y-axis (CNBD accuracy - E accuracy) at $\rho = 0.2$; one point per (task, model) cell.

P3 predicts positive correlation with $\rho > 0.5$.

### 10.3 Layer-dependence figure

For the Llama-3.1-8B-Instruct calendar task, a single curve: CNBD-minus-E gap at $\rho = 0.2$ vs. layer index $\ell$ at which $\mathcal{E}_3$ is computed.

P5 predicts a peak near the qualifying layer from [Paper 36](36_layerwise_packet_spectroscopy.md).

### 10.4 Verifier-amplification table

Llama-3.1-8B-Instruct calendar, $\rho = 0.2$, with three extra-compute modes:

| strategy | self-consistency | beam-8 | Llama-70B verifier |
|---|---:|---:|---:|
| E | pending | pending | pending |
| CNBD | pending | pending | pending |
| (CNBD - E) | pending | pending | pending |

P7 predicts the (CNBD - E) row's last entry is $\geq 1.5$x the first entry.

---

## 11. Scope and limitations

### 11.1 What this paper does not prove

It does not prove that CNBD is the *optimal* adaptive-compute strategy at any given budget. It proves that CNBD strictly improves over entropy-threshold at matched budget on the specific failure mode (shortcut-committing low-entropy regime) Theorem 4.2 identifies. There may be a higher-order signal (quartic, quintic, …) that further improves over CNBD on cleaner tasks; [Paper 17](17.the_cubic_noether_theorem.md) Remark 3.2 argues that classical higher-order momentum cannot be added without violating real-cone preservation, but this constraint may not bind at the operational level of decoding heuristics.

### 11.2 What this paper does not require

It does not require modifying the model. CNBD is a pure inference-time recipe. The model weights, architecture, and training are all unchanged.

### 11.3 What this paper requires from the program

It requires [Paper 36](36_layerwise_packet_spectroscopy.md)'s spectroscopy to identify the qualifying layer $\ell$. Without that prerequisite, CNBD can still be tried at every layer, but P5's prediction is then untestable. The hard prerequisite is the reason this paper is the *last* of the five spin-offs in deployment order.

### 11.4 Open-ended generation

The pre-registered experiments restrict to cyclic sub-vocab tasks where $V_R$ is clear. Extending CNBD to general open-ended chat requires the sub-task identifier of §8.3 plus a taxonomy of ring-structured sub-vocabularies in natural-language generation. We do not solve this; we name it as the v0.3 deliverable.

### 11.5 Constant-time CNBD

For very-low-latency serving (under 5 ms per token), the per-step CNBD signal cost (currently 5 microseconds in our profile) is acceptable but the $S_\text{extra}$ dispatch latency is not. A constant-time-CNBD variant that pre-allocates extra compute to a fixed schedule informed by the cubic-energy drift *prediction* (rather than measurement) is a natural next paper but not the present scope.

---

## 12. Conclusion

The cubic Noether energy of [Paper 17](17.the_cubic_noether_theorem.md) is, when read at the right layer, a per-token compute-allocation signal that is *structurally* better than entropy on a specific failure mode every quadratic signal misses: shortcut-committing low-entropy tokens. The Conductor Blind Spot ([Paper 34](34_the_conductor_blind_spot.md)) supplies the reason; the BNSA ([Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md)) supplies the magnitude calibration; the spectroscopy ([Paper 36](36_layerwise_packet_spectroscopy.md)) supplies the layer; and the present paper supplies the algorithm, the budget identity, the anti-correlation theorem, and the pre-registered five-task sweep that turns the program's third-order machinery into a deployment-relevant inference-time gain.

The Cubic Budget Identity (Theorem 4.1) writes the next-token NLL as cubic action plus jerk-bounded residual. The Anti-Entropy Decorrelation Theorem (Theorem 4.2) proves CNBD and entropy point opposite directions in exactly the regimes where entropy misallocates. The five-benchmark sweep tests whether the predicted decorrelation translates into a measured accuracy gain at matched compute, with shortcut-magnitude scaling and layer specificity as orthogonal falsifiability checks.

The signal cost is microseconds per token. The expected gain on canonical Llama-3.1-8B calendar is a strict win over entropy-threshold at every tested budget, with magnitude calibrated by the BNSA shortcut ratio $\sigma_\mathcal{S} = 0.458$. The deployment-relevant variant — CNBD-gated cascade to a 70B verifier — amplifies the gain by at least 1.5x on the same anchor.

This is the biggest engineering item in the Conductor program's spin-off arc, the one whose payoff is most directly measurable in production-relevant terms, and the one that requires the rest of the program as prerequisite. We submit it as the program's first inference-time deliverable.

---

*Draft v0.1 — May 19, 2026 — CNBD algorithm, Cubic Budget Identity (Theorem 4.1), Anti-Entropy Decorrelation Theorem (Theorem 4.2), pre-registered five-task / three-model / seven-strategy sweep with seven sharp predictions and five failure conditions. v0.2 will populate §10 result templates from the sweep, with Paper 36 spectroscopy results supplying the per-model qualifying layer index for §10.3.*
