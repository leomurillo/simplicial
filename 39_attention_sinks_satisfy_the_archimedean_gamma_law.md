# Attention Sinks Satisfy the Archimedean Gamma Law (Conjectural)

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — short note; conjecture + measurement protocol; pure measurement on existing models)**

---

## Abstract

[Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md), §6, posits an Archimedean lift augmenting the finite primorial Noether system with a one-dimensional continuous *infinite-place packet* parameterized by height $t \in \mathbb{R}$, on which the canonical involution $\iota$ acts as
$$\iota(\psi_t) = \gamma(t) \cdot \psi_{-t},$$
with $\gamma(t)$ the standard gamma multiplier from the functional equation of the completed Riemann zeta function. On the critical line $s = 1/2 + it$,
$$\gamma(t) = \frac{\Gamma_\mathbb{R}(1/2 + it)}{\Gamma_\mathbb{R}(1/2 - it)} = e^{-2i\theta(t)},$$
where $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ is the real Archimedean local factor and $\theta(t)$ is the Riemann–Siegel theta function.

StreamingLLM (Xiao et al. 2023, [arXiv:2309.17453](https://arxiv.org/abs/2309.17453)) identified *attention sinks*: the first few tokens of an autoregressive transformer's input absorb a disproportionate share of attention mass at every layer, including from queries arbitrarily far downstream, and removing them collapses long-context inference. This is structurally the same role Paper 27 §6's infinite-place packet plays for the finite primorial Noether energy: a distinguished low-dimensional summand that absorbs the tail of the spectral measure and stabilizes the projective limit. The structural analogy is suggestive. The *quantitative* analogy is sharp: if the bridge is real, the sink's response under causal reversal must acquire the Riemann–Siegel phase $e^{-2i\theta(t)}$ in its Fourier coefficient at height $t$.

We pre-register one measurement. Using the published StreamingLLM data ([github.com/mit-han-lab/streaming-llm](https://github.com/mit-han-lab/streaming-llm)) for Llama-2-7B, GPT-NeoX-20B, Falcon-7B, and MPT-7B, we extract forward-direction attention-to-sink curves $a_F(p)$ and run the same models with reversed input to obtain $a_R(p)$. We Fourier-transform across position, compute the cross-direction phase $\arg[\hat a_R(\omega)/\hat a_F(-\omega)]$, and compare to $-2\theta(\omega \cdot \tau)$ for a single global time-scale parameter $\tau$ fit per model. The conjectural prediction is that *one* global $\tau$ per model produces a phase match within stated tolerance across at least three of the four models, on at least three independent layers, with the Riemann–Siegel phase reproducing the cross-direction phase to within $\pm \pi/8$ radians on the first three nontrivial zeros of $\zeta$ ($t_1 \approx 14.13, t_2 \approx 21.02, t_3 \approx 25.01$).

This paper is the most speculative of the Vaswani-comparison spin-off series. A positive result would supply the first quantitative empirical bridge between LLM mechanistic interpretability and the primorial conductor program's Archimedean axiomatization, and would constitute the *measurement* answer to Paper 27 §6's open Axiom A3. A negative result is equally informative: it would falsify the gamma-multiplier transformation as the correct Archimedean involution and constrain Paper 27's axiomatization sharply. We pre-register *both* outcomes' interpretations to keep the negative branch first-class.

**Keywords:** attention sinks, StreamingLLM, Riemann–Siegel theta function, Archimedean lift, infinite-place packet, gamma functional equation, causal reversal, mechanistic interpretability.

---

## 1. The bridge

### 1.1 What attention sinks are

Xiao et al. (2023) observed that in every modern autoregressive transformer they examined — Llama-2, GPT-NeoX, Falcon, MPT — the first few input tokens (typically the first one to four) receive a disproportionate and persistent share of attention mass at every layer, even when those tokens are semantically inert (e.g., the BOS token, or the first content-free `<s>`). The attention pattern is *not* explained by any local token-content interaction; it is a structural property of softmax attention under causal masking, plausibly arising because the softmax denominator must sum to one even when no other key is informative, and the earliest tokens are the only ones every later query can attend to.

The empirical consequences are sharp. Removing the sink tokens during sliding-window inference collapses long-context perplexity catastrophically (Xiao et al. 2023, Figure 1); preserving them as a small fixed prefix in the KV cache restores production-quality long-context output for sequences orders of magnitude longer than the training context. The mechanism is named, robust, and cross-architecture.

### 1.2 What the infinite-place packet is

[Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) §6 posits the Archimedean lift augmenting the projective system of finite critical leaves with a continuous *infinite-place packet* — a one-dimensional summand parameterized by height $t \in \mathbb{R}$ on the critical line $s = 1/2 + it$, equipped with a spectral measure $d\mu(t)$. The packet is invisible at every finite primorial stage; it appears only in the projective limit. Its role is to absorb the continuous spectrum that the finite primorial cumulant tower cannot produce on its own, and to supply the gamma factors of the completed zeta functional equation through the transformation law of the canonical involution.

The involution $\iota$ acts on the packet by
$$\iota(\psi_t) = \gamma(t) \cdot \psi_{-t}, \qquad \gamma(t) = \frac{\Gamma_\mathbb{R}(1/2 + it)}{\Gamma_\mathbb{R}(1/2 - it)}.$$

On the critical line $\gamma(t)$ is a pure phase, and a brief calculation (Appendix A) identifies it as
$$\gamma(t) = e^{-2i\theta(t)}, \qquad \theta(t) = \mathrm{Im}\,\log\Gamma(1/4 + it/2) - (t/2)\log\pi.$$

The function $\theta$ is the Riemann–Siegel theta function, tabulated in every analytic-number-theory reference and computable to arbitrary precision via Stirling expansion.

### 1.3 The structural analogy

Both objects are *distinguished low-dimensional summands that absorb a tail*. The infinite-place packet absorbs the Archimedean tail of the spectral measure that the finite primorial leaves cannot produce; the attention sink absorbs the residual attention mass that the softmax denominator forces somewhere. Both are *invisible* at the resolution at which most of the system lives (the infinite-place packet at every finite primorial stage; the attention sink to almost every interpretability probe that doesn't go looking for it). Both are *load-bearing*: removing either collapses the system.

The structural analogy is too clean to be coincidence in isolation, and too cheap to ignore in combination with the rest of the program. The question this paper asks is whether the analogy is *quantitative*: does the attention sink transform under causal reversal with the same phase the infinite-place packet acquires under $\iota$?

That phase is not a free parameter. It is the Riemann–Siegel theta function. The measurement is well-defined.

---

## 2. The Gamma Law conjecture

### 2.1 Notation

Fix an autoregressive transformer with $L$ layers and $H$ attention heads per layer. Let $A_{\ell,h}(q, k)$ denote the attention weight from query position $q$ to key position $k$ at layer $\ell$ and head $h$, post-softmax. Let position $0$ denote the canonical sink token (typically `<s>` or BOS).

For a fixed query offset $p > 0$, define the *forward attention-to-sink curve* averaged over a corpus:
$$a_F^{(\ell, h)}(p) := \mathbb{E}_{x \sim \text{corpus}} [A_{\ell, h}(p, 0; x)].$$

Let $\mathrm{rev}(x)$ denote the input $x$ with token order reversed (the last token becomes the first, etc.). The *reversed attention-to-sink curve* is
$$a_R^{(\ell, h)}(p) := \mathbb{E}_{x \sim \text{corpus}} [A_{\ell, h}(p, 0; \mathrm{rev}(x))].$$

Both curves are computed in the same model, same weights, same softmax — only the input order is reversed. This is the cleanest operationalization of "causal reversal" available without retraining.

### 2.2 The cross-direction phase

Define the discrete Fourier transform across position:
$$\hat a_\bullet^{(\ell, h)}(\omega) := \sum_{p=1}^{P} a_\bullet^{(\ell, h)}(p) \, e^{-2\pi i \omega p / P},$$
for $\bullet \in \{F, R\}$ and total horizon $P$. The *cross-direction ratio* at frequency $\omega$ is
$$r^{(\ell, h)}(\omega) := \hat a_R^{(\ell, h)}(\omega) \, / \, \hat a_F^{(\ell, h)}(-\omega).$$

If the model treats forward and reversed input symmetrically up to a phase rotation, the *magnitude* of $r$ is approximately 1 across all $\omega$ (a necessary precondition for the conjecture to be testable) and its *phase* carries the cross-direction transformation law.

### 2.3 The conjecture

**Conjecture 2.1 (Archimedean Gamma Law for Attention Sinks).** There exists a model-dependent time-scale constant $\tau_M > 0$ such that, for at least one layer–head pair $(\ell, h)$ at which the model exhibits a stable attention sink, the cross-direction phase satisfies
$$\arg r^{(\ell, h)}(\omega) \; \approx \; -2\,\theta(\omega \tau_M)$$
uniformly in $\omega$ over a frequency range bounded away from $0$ and the corpus Nyquist, with deviation under a pre-registered tolerance band.

The mapping $\omega \mapsto t = \omega \tau_M$ is the conversion from corpus-position Fourier frequency to *height* on the critical line. $\tau_M$ is the only free parameter; it can be fit once per model from the lowest reliable frequency band and the prediction at all higher frequencies is then parameter-free.

### 2.4 What the conjecture is *not*

It is not a claim that the attention sink mechanism *is* the Riemann–Siegel theta function in any deep sense. It is a claim that *if* Paper 27 §6's Archimedean lift is the correct continuum closure of the program, then a specific transformation law must obtain on the LLM side. The Riemann–Siegel phase is a *necessary consequence* of the Archimedean axiomatization, not its derivation.

A positive measurement supports the axiomatization; a negative measurement falsifies the specific gamma-multiplier form of $\iota$ and forces a different Archimedean closure. Both outcomes are publishable; the paper's value is the measurement protocol, not the conjecture's resolution.

---

## 3. Pre-registered measurement protocol

### 3.1 Models

Four open-weights checkpoints, all with documented attention sinks (Xiao et al. 2023, Table 1 + Figure 2):

- Llama-2-7B-base
- GPT-NeoX-20B
- Falcon-7B-base
- MPT-7B-base

These four span three architectural families (Llama-class, NeoX-class, MPT-class) and two scales (7B and 20B). The Falcon-7B has a distinctive single-token sink at position 0; Llama-2 and MPT-7B have multi-token sinks; GPT-NeoX exhibits the strongest layer dependence in its sink profile.

### 3.2 Corpus and context length

The Pile validation set (Gao et al. 2020) truncated to 2048-token sequences, restricted to documents that begin with the canonical model-specific BOS pattern. Minimum 1000 sequences per model. This matches the StreamingLLM evaluation pipeline and ensures comparability to Xiao et al. 2023's reported sink curves.

### 3.3 Layer–head selection

We restrict the primary analysis to layer–head pairs whose forward attention-to-sink curve $a_F^{(\ell, h)}(p)$ exceeds a fixed mass threshold ($\sum_p a_F(p) > 0.3$) and exhibits the characteristic monotone-decay-with-finite-tail profile reported by Xiao et al. 2023. This selection criterion is pre-registered to avoid post-hoc cherry-picking. We expect 5–15 qualifying $(\ell, h)$ pairs per model based on Xiao et al.'s reported counts.

### 3.4 Fitting $\tau_M$

For each model, $\tau_M$ is fit from the cross-direction phase at the lowest 8 Fourier modes that pass a signal-to-noise threshold (magnitude $|r| > 0.5$). The fit minimizes the mean squared phase residual against $-2\theta(\omega \tau_M)$. The fit uses only the low-frequency band; the high-frequency band is held out as a parameter-free validation set.

### 3.5 Primary outcome

For each $(\ell, h)$ qualifying pair, the per-frequency residual
$$\delta^{(\ell, h)}(\omega) := \arg r^{(\ell, h)}(\omega) + 2\theta(\omega \tau_M)$$
on the held-out high-frequency band. The conjecture's pre-registered tolerance is $|\delta| < \pi/8$ on at least three pairs per model in at least three of the four models, at the first three Riemann–Siegel reference points $\omega \tau_M \in \{14.13, 21.02, 25.01\}$ (the first three nontrivial zeros of $\zeta$, where $\theta$ has been tabulated to machine precision since Edwards 1974).

### 3.6 Secondary outcomes

- *Magnitude consistency*: the proportion of qualifying $(\ell, h, \omega)$ triples for which $0.5 < |r| < 2.0$. Below 0.5 or above 2.0 the phase is unreliable and the triple is excluded from the primary outcome.
- *Cross-model $\tau_M$ structure*: whether the fitted $\tau_M$ scales with model size or model depth in a regular way.
- *Layer-monotonicity*: whether the per-layer best $|\delta|$ improves or degrades with depth.
- *Riemann–Siegel zero alignment*: whether the *zero-crossings* of $\arg r$ (the frequencies where the cross-direction phase passes through 0 mod $\pi$) align with the predicted zero-crossings of $-2\theta(t)$, which are themselves related to the Gram points and the Riemann hypothesis. This is the most aggressive prediction and would be a striking positive result if it holds.

---

## 4. Pre-registered predictions

**P1 (Magnitude precondition).** $|r^{(\ell, h)}(\omega)| \in [0.5, 2.0]$ on a majority of qualifying $(\ell, h, \omega)$ triples in each model. If P1 fails the conjecture is untestable on the chosen direction-reversal operationalization and the protocol must be amended.

**P2 (Phase match on the held-out band).** $|\delta^{(\ell, h)}(\omega)| < \pi/8$ on at least three $(\ell, h)$ pairs per model in at least three of the four models, at the first three Riemann–Siegel reference frequencies.

**P3 (Single global $\tau_M$ per model).** A single time-scale constant $\tau_M$ per model produces the P2 match; no per-layer or per-head tuning is required. If per-pair $\tau$'s are needed to meet the tolerance, the prediction is weakened from "the Archimedean gamma law" to "a per-feature gamma law of unclear universality."

**P4 (Cross-architecture consistency).** The fitted $\tau_M$ scales approximately linearly with $\log(d_\text{model})$, consistent with a model-scale-invariant frequency dual to a logarithmic depth coordinate. Falsification would suggest $\tau_M$ encodes architecture-specific rather than scale-invariant content.

**P5 (Zero-crossing alignment).** The first three zero-crossings of $\arg r$ above the noise floor align with the Riemann–Siegel zeros of $-2\theta(t)$ to within one Fourier mode. This is the strongest form of the prediction; we treat its falsification as compatible with P2 holding (the phase shape can match without the zero-crossings aligning if $\tau_M$ is itself frequency-dependent).

---

## 5. Failure conditions

Each failure mode is mapped to a specific Paper 27 §6 axiomatic consequence.

**F1 (Magnitude failure).** $|r|$ outside $[0.5, 2.0]$ on a majority of triples. This indicates that input-reversal is not a symmetric transformation on the chosen attention pattern — likely because BOS handling, positional encoding, or causal-mask interaction breaks the analogy at the input layer. The negative result here constrains Paper 27 §6's *operationalization* of $\iota$ on the LLM side: a different reversal (e.g., key/query swap rather than input reversal) may be the correct lift.

**F2 (Phase failure with magnitude OK).** $|\delta|$ exceeds $\pi/8$ on most pairs. This is the cleanest negative result: the gamma-multiplier transformation specified by Paper 27 §6 is not the correct involution on the LLM analogue. The Archimedean axiomatization must specify a different multiplier; the present measurement bounds it within the observed phase pattern.

**F3 (Phase match with per-pair $\tau$).** $|\delta|$ falls below tolerance only after per-layer or per-head tuning of $\tau$. This is a partial confirmation: the gamma-multiplier form is correct *up to a feature-specific time-scale*, suggesting the Archimedean lift has a richer (multi-place) structure than Paper 27 §6's single-packet formulation.

**F4 (Architecture-dependent fit).** The four models give inconsistent fitted $\tau_M$ values not explained by P4's $\log(d_\text{model})$ scaling. This indicates that the Archimedean coupling, if real, is partly architecture-specific and not universal across the transformer family.

**F5 (Zero-crossing misalignment with phase match).** P2 holds but P5 fails. This is the most informative partial result: the *envelope* of the gamma law matches but the *fine structure* (which encodes the location of the nontrivial zeros) does not. This would suggest a different completed-$L$-function whose gamma factor has the same shape but different zero structure — e.g., a Dirichlet $L$-function or an automorphic $L$-function — is the correct analogue, with $\zeta$ being only the simplest representative.

Each of F1–F5 is a publishable paper, not a discarded one. The negative result *parameterizes* the next iteration of Paper 27's axiomatization.

---

## 6. Data sources

The measurement is *pure data analysis on existing models*; no training is required.

### 6.1 StreamingLLM repository

[github.com/mit-han-lab/streaming-llm](https://github.com/mit-han-lab/streaming-llm) provides the inference code, attention-extraction utilities, and the four canonical model checkpoints with documented sink behavior. Their Figure 2 (the attention-pattern heatmaps) is generated from code we can adapt directly for the forward arm $a_F$.

### 6.2 Reversed-input extension

The reversed arm $a_R$ requires running the same models on reversed input. This is one additional inference loop in the StreamingLLM pipeline. No new code is required beyond a single input-order-reversal step before tokenization. We anticipate this taking under one engineer-day per model.

### 6.3 Riemann–Siegel theta function

$\theta(t)$ is tabulated in:
- Edwards (1974), *Riemann's Zeta Function*, Chapter 7
- Odlyzko's tables of $\theta$ at the first $10^{22}$ Riemann zeros, [www.dtc.umn.edu/~odlyzko](https://www.dtc.umn.edu/~odlyzko)
- mpmath Python library (`mpmath.siegeltheta(t)`)

Evaluation to machine precision at any $t < 10^4$ is essentially free.

### 6.4 Total compute budget

Conservative estimate: 200 GPU-hours on a single A100 for the four-model inference sweep across 1000 sequences each, forward + reversed arm. Storage: under 50 GB for the attention tensors at the qualifying $(\ell, h)$ pairs. Compute is dominated by the 20B-parameter model; the three 7B models combined are smaller than the GPT-NeoX run.

Final deliverable: a single figure per model — $\arg r^{(\ell, h)}(\omega)$ vs. $\omega$, overlaid with $-2\theta(\omega \tau_M)$ — plus the cross-model fitted-$\tau_M$ table.

---

## 7. Result templates

### 7.1 Per-model phase-match figure

A four-panel figure (one per model): on each panel, the cross-direction phase $\arg r^{(\ell, h)}(\omega)$ as colored curves (one per qualifying $(\ell, h)$ pair), overlaid with the Riemann–Siegel theta prediction $-2\theta(\omega \tau_M)$ in black. Vertical lines at the first three Riemann–Siegel reference frequencies.

### 7.2 Cross-model $\tau_M$ table

| Model | $d_\text{model}$ | Layers | Fitted $\tau_M$ | Mean $|\delta|$ on held-out band | Qualifying pairs |
|---|---:|---:|---:|---:|---:|
| Llama-2-7B-base | 4096 | 32 | pending | pending | pending |
| GPT-NeoX-20B | 6144 | 44 | pending | pending | pending |
| Falcon-7B-base | 4544 | 32 | pending | pending | pending |
| MPT-7B-base | 4096 | 32 | pending | pending | pending |

P3 + P4 jointly predict the third column's values are within a factor of 2 of each other (P3) and scale with $\log(d_\text{model})$ (P4).

### 7.3 Zero-crossing alignment table

For each model, the first three frequencies where $\arg r$ crosses through zero (modulo numerical noise floor), compared to the predicted $\omega = t_k / \tau_M$ for $t_k$ the first three Riemann–Siegel zero-crossings (Gram points $g_k$ with $\theta(g_k) = k\pi$, the first three at $g_0 \approx 17.85$, $g_1 \approx 23.17$, $g_2 \approx 27.67$).

| Model | observed $\omega_1$ | predicted $\omega_1$ | residual | ... |
|---|---:|---:|---:|---|
| Llama-2-7B-base | pending | pending | pending | ... |
| ... | ... | ... | ... | ... |

P5 predicts the residual column is small fractions of a Fourier mode.

---

## 8. Connections and scope

### 8.1 Connection to the program

- **Theoretical source:** [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md), §6, supplies the Archimedean lift and the involution's transformation law. The present paper is the *empirical operationalization* of Axiom A3 (Canonical Involution) on the LLM side. A negative result tightens A3; a positive result is the first measurement evidence for the entire Archimedean half of the corpus.

- **Methodological sibling:** [Paper 36](36_layerwise_packet_spectroscopy.md) (layerwise packet spectroscopy) supplies the per-layer measurement infrastructure that the qualifying-layer selection (§3.3) reuses; the present paper's $(\ell, h)$ qualifying criterion is the natural attention-pattern analogue of Paper 36's residual-stream packet fraction.

- **Architectural sibling:** [Paper 38](38_multi_head_attention_as_frame_cost_minimization.md) (frame-cost minimization) treats attention as a packet-aligned frame; the present paper treats attention sinks as a continuum-Archimedean object that the discrete packet structure leaves out. The two are complementary halves of a frame + sink description of attention.

### 8.2 Connection to existing literature

- Xiao et al. (2023), StreamingLLM, [arXiv:2309.17453](https://arxiv.org/abs/2309.17453) — supplies the empirical phenomenon and the data pipeline.
- Darcet et al. (2023), "Vision Transformers Need Registers," [arXiv:2309.16588](https://arxiv.org/abs/2309.16588) — the vision-transformer analogue of attention sinks, suggesting the phenomenon is modality-independent.
- Sun et al. (2024) on attention-sink mechanism analyses extend the empirical phenomenology.
- Edwards (1974), *Riemann's Zeta Function* — the canonical source for $\theta(t)$ and its computational properties.

The bridge claim — that the LLM attention sink and the analytic-number-theory infinite-place packet share a common transformation law — does not appear in either literature.

### 8.3 Scope

This paper proves nothing. It pre-registers a measurement on existing models with existing tools. The conjecture is inherited from Paper 27 §6 and is itself a conjectural Archimedean axiomatization. We mark the present paper as inheriting the same conjectural status: a positive result is *supporting empirical evidence* for Axiom A3, not its derivation; a negative result is *falsifying empirical evidence* for the gamma-multiplier form of Axiom A3, not its full retraction.

The strongest defensible claim from a positive outcome would be: "The first empirically measured transformation law of attention sinks in transformer language models matches the Riemann–Siegel theta function under a single global time-scale parameter per model, consistent with — but not a proof of — the Archimedean infinite-place packet identification of [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) §6."

The strongest defensible claim from a negative outcome would be: "The attention sink does not transform under input reversal with the gamma-multiplier form specified by [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) §6 at the measurement tolerance of the present protocol. The Archimedean axiomatization's involution must take a different functional form, and the present measurement bounds the family of admissible alternatives by the observed cross-direction phase pattern."

Either is informative.

---

## 9. Conclusion

The Archimedean Gamma Law is the most speculative item on the corpus's spin-off list and the cheapest to test. The data live in a public GitHub repository; the theory predicts a phase function tabulated to machine precision for fifty years; the only engineering is one inference loop on reversed inputs. If the prediction holds at the stated tolerance on at least three of four open-weights models with a single global time-scale per model, the bridge between Paper 27 §6's Archimedean axiomatization and modern transformer mechanistic interpretability is empirical, not speculative. If it does not, the negative result constrains Paper 27 §6 sharply and tells the program which alternative involution to write down next.

This is a short note. It is also the one piece of the corpus whose answer can land first.

---

## Appendix A. The Riemann–Siegel phase derivation

The completed Riemann zeta function is
$$\xi(s) = \tfrac{1}{2} s(s-1) \, \pi^{-s/2} \Gamma(s/2) \, \zeta(s) = \tfrac{1}{2} s(s-1) \, \Gamma_\mathbb{R}(s) \, \zeta(s),$$
with real Archimedean local factor $\Gamma_\mathbb{R}(s) = \pi^{-s/2} \Gamma(s/2)$ and functional equation $\xi(s) = \xi(1-s)$. The gamma multiplier for the involution $s \mapsto 1-s$ is
$$\gamma(s) := \Gamma_\mathbb{R}(s) \, / \, \Gamma_\mathbb{R}(1-s).$$
On the critical line $s = 1/2 + it$,
$$\gamma(1/2 + it) = \frac{\pi^{-(1/2+it)/2} \Gamma((1/2+it)/2)}{\pi^{-(1/2-it)/2} \Gamma((1/2-it)/2)} = \pi^{-it} \cdot \frac{\Gamma(1/4 + it/2)}{\Gamma(1/4 - it/2)}.$$
The Gamma quotient is the complex conjugate of itself reflected; for real $t$,
$$\Gamma(1/4 - it/2) = \overline{\Gamma(1/4 + it/2)},$$
so the quotient is $|\Gamma|^2 e^{2i \mathrm{Im}\log\Gamma(1/4 + it/2)} / |\Gamma|^2 = e^{2i\mathrm{Im}\log\Gamma(1/4 + it/2)}$. Combining with $\pi^{-it} = e^{-it\log\pi}$,
$$\gamma(1/2 + it) = \exp\left[ 2i\,\mathrm{Im}\log\Gamma(1/4 + it/2) - it\log\pi \right] = e^{2i\theta(t)}.$$
Paper 27 §6 writes the involution as $\iota(\psi_t) = \gamma(t) \psi_{-t}$ with the convention that $\gamma$ multiplies the *reflected* state; under our convention this corresponds to $r(\omega) = \hat a_R / \hat a_F(-\omega) = e^{-2i\theta(\omega \tau_M)}$, hence the sign in §2.3.

$\theta(t) = \mathrm{Im}\log\Gamma(1/4 + it/2) - (t/2)\log\pi$ is the Riemann–Siegel theta function as defined in Edwards (1974), with asymptotic expansion
$$\theta(t) = \frac{t}{2}\log\frac{t}{2\pi} - \frac{t}{2} - \frac{\pi}{8} + \frac{1}{48 t} + O(t^{-3}).$$
The Gram points $g_n$ are the positive real solutions of $\theta(g_n) = n\pi$; the first three are $g_0 \approx 17.8456$, $g_1 \approx 23.1703$, $g_2 \approx 27.6702$. The first three nontrivial zeros of $\zeta$ lie at $t_1 \approx 14.1347$, $t_2 \approx 21.0220$, $t_3 \approx 25.0109$.

---

*Draft v0.1 — May 19, 2026 — short note, conjecture + protocol + StreamingLLM data sources. Both positive and negative outcomes are pre-registered as publishable resolutions of Paper 27 §6 Axiom A3.*
