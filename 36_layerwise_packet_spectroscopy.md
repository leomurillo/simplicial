# Layerwise Packet Spectroscopy: A Conductor-Resolved Map of Cyclic Concept Sharpening in Transformer Language Models

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — protocol + anchor measurement, full sweep pre-registered)**

---

## Abstract

The Conductor Probe-Obstruction Theorem ([Paper 26](26.conductor_probe_obstruction_theorem.md)) reduces interpretability of ring-structured categorical readouts to an exact divisor law: a linear or logit-lens readout whose codomain is a $k$-resolution quotient of the cyclic label algebra $C_N$ retains exactly the conductor packets $H_d$ with $d \mid k$ and annihilates exactly those with $d \nmid k$. Applied to Llama-3.1-8B on the months task, Paper 26 reports one anchor pair: the *raw layer-28* hidden-state probe places fraction $0.355640$ of nontrivial cyclic energy in the full-period packet $H_{12}$, while the *native final-token* month logits place $0.657415$. The full-period packet is therefore *sharpened in the residual stream between layer 28 and the unembedding*. This paper turns that single observation into a measurement program: a packet-resolved spectrum $f_{d,\ell}$ giving, for every layer $\ell$ of a transformer and every conductor $d$ of a chosen cyclic task algebra $C_N$, the fraction of nontrivial cyclic energy carried by packet $H_d$ when the readout uses the hidden state at layer $\ell$.

We give: (i) the pre-registered divisor tables for the three immediate target tasks $C_{12}$ (months), $C_{7}$ (weekdays), $C_{10}$ (digits); (ii) the packet-projection protocol, made identical between a frozen-unembedding lens and a per-layer trained quotient probe so that the analytic forbidden-zeros of Paper 26 §T1–T2 are the same control object in both cases; (iii) seven pre-registered predictions about the shape of $f_{d,\ell}$, including a *monotonic full-period concentration* prediction, a *predecessor-leakage asymmetry* prediction (motivated by [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md) §weekday rows), and a *base-N shortcut survival* prediction (motivated by Paper 26 §nonlinear ablation); (iv) the Paper 26 anchor measurement restated and embedded as the layer-28 row of the months target; (v) the empirical reading rule, which keeps the theorem-side analytic zeros separate from the model-facing native-pre-bin fractions; and (vi) a script inventory.

The deliverable is a single figure per model–task: $f_{d,\ell}$ vs. $\ell$, with confidence bands from train/test resampling, accompanied by the analytic forbidden-fraction control row from Paper 26 §T1. No new theorem is required; every quantity reported here is a contraction of [Paper 11](11.quotient_character_adjacency_algebras.md) Proposition 1.2 and Paper 26 T1–T2 with a finite computational artifact. The empirical novelty is the layerwise resolution. The interpretive novelty is that the spectrum, read against the divisor table, names *which layer* lifts *which packet* — a structural question that previous linear-probe and tuned-lens literature has not been able to phrase.

**Keywords:** mechanistic interpretability, logit lens, tuned lens, conductor packets, additive characters, cyclic concepts, layerwise probing, Llama-3.1-8B, Mistral-7B, packet spectroscopy.

---

## 1. Introduction

### 1.1 What Paper 26 left underdetermined

Paper 26 closed the question of *which packets a quotient-respecting readout can see*: for the quotient $q_k : C_N \to C_k$, the readout retains exactly $\bigoplus_{d \mid k} H_d$ and annihilates the rest, sharply, with packet-pure unit signals giving exactly zero surviving energy on the forbidden side. The empirical bridge to a real transformer was a single pair of numbers: the raw layer-28 BF16 hidden-probe puts $f_{12,28} \approx 0.356$ into $H_{12}$, the native final-token logits put $f_{12,\mathrm{final}} \approx 0.657$. Paper 26 §Hidden-State Shortcut Audit comments on this gap: *"the full-period packet therefore concentrates between the layer-28 hidden representation and the final native month logits. This turns the gap into a layerwise prediction: a true tuned-lens sweep should show where the conductor sharpening occurs."* This paper is that sweep.

### 1.2 Why the sweep is more than an extrapolation

Three reasons.

First, the *direction* of conductor sharpening is not predicted by the algebraic obstruction. Paper 26 T1 forbids quotient lenses from *creating* full-period energy; it does not say anything about whether the full-period packet is built up gradually across layers, in one or two late layers, or already mostly present at the embedding and merely *un-mixed* by later layers. Each profile carries a different mechanistic interpretation. A monotonically rising $f_{12,\ell}$ is consistent with progressive cyclic encoding. A flat profile that jumps near the unembedding is consistent with a late-layer "decoding" step. A profile that overshoots $f_{12,\mathrm{final}}$ at an intermediate layer and then falls back is consistent with internal use of a *finer* cyclic structure than the one the head exposes. The native vs. raw-layer-28 gap from Paper 26 is silent on which.

Second, the sweep separates the *native* concentration from the *probe-induced* concentration. The Paper 26 native-logit binning experiment is the cleanest current artifact for the months task precisely because it starts from the model's own unembedding and does not train anything. The layerwise analogue exists in two flavours that must be reported side by side: (a) a *frozen-unembedding lens* that applies the model's own final linear+softmax to the residual stream at each layer (the "logit lens" of nostalgebraist; the affine $W_U h_\ell$ readout); and (b) a *per-layer trained quotient probe* with the same codomain restriction. The first is a direct readout of the residual stream in the model's own basis; the second is the strongest readout consistent with the codomain budget. The gap between (a) and (b) is itself informative: it bounds how much the residual stream's basis is already aligned with the unembedding's, layer by layer.

Third, every prediction in the spectrum is falsifiable on existing open-weights checkpoints with no training. The compute budget for the full sweep on Llama-3.1-8B (32 layers) and Mistral-7B-v0.3 (32 layers) across three tasks is dominated by one forward pass per example per model per task; the trained-probe arm adds a per-layer ridge regression. This is a paper that can be written in one week and falsified by anyone with a single GPU.

### 1.3 What this paper does *not* claim

It does not claim that the conductor-packet decomposition is a privileged basis for arbitrary natural-language behavior. The packet decomposition is the canonical orthogonal basis of the Fisher tangent at $p_*$ *for the cyclic label algebra being probed*. Whether the same packet structure is visible in other behavior subspaces is the subject of separate replication work, including the cross-task and cross-model audits proposed in §10.

It does not claim a causal account of full-period sharpening. The spectrum is a measurement. A causal account would require interventions (activation patching, head ablation, weight-space targeted edits), which are listed as follow-up in §10.

It does not claim that the spectrum eliminates the base-N shortcut warning of Paper 26 §Nonlinear Base-10 Shortcut Ablation. The shortcut survives at intermediate layers and is partly visible in the layer-28 hidden-state probe's $H_{12}$ fraction. The layerwise sweep makes this *more* legible, not less, by separating layers that survive decimal sum/carry residualization from those that do not.

---

## 2. Background and notation

### 2.1 The cyclic label algebra and its character basis

Fix $N \geq 2$ and let $R = C_N = \mathbb{Z}/N\mathbb{Z}$. The additive characters $\chi_a(x) = e^{2\pi i a x / N}$, $a \in \{0,1,\dots,N-1\}$, form an orthonormal basis of $L^2(R)$ under the normalized inner product $\langle f, g \rangle = N^{-1} \sum_x f(x) \overline{g(x)}$. The *conductor* of $\chi_a$ is $\mathrm{cond}(\chi_a) = N / \gcd(a, N)$, equivalently the order of $a$ in $R$. The *conductor packet* $H_d$ is the span of those characters with conductor exactly $d$; $H_d$ has $\mathbb{C}$-dimension $\varphi(d)$, and $L^2(R) = \bigoplus_{d \mid N} H_d$.

For $N = 12$ the nontrivial packets are $H_2, H_3, H_4, H_6, H_{12}$ with dimensions $1, 2, 2, 2, 4$. For $N = 7$ (prime) the only nontrivial packet is $H_7$ of dimension $6$. For $N = 10$ the nontrivial packets are $H_2, H_5, H_{10}$ of dimensions $1, 4, 4$.

### 2.2 The quotient projector and its packet diagonalization

For $k \mid N$ let $q_k : C_N \to C_k$ be the canonical quotient with kernel $K = \langle k \rangle = \{0, k, 2k, \dots, (N/k-1)k\}$. The orthogonal projection $P_{q_k} : L^2(R) \to V_{q_k}$ onto the subspace $V_{q_k}$ of functions factoring through $q_k$ is coset averaging by $K$. The Pontryagin obstruction (Paper 26 T1) is the statement that $P_{q_k}$ is diagonal in the character basis with eigenvalues
$$P_{q_k}|_{H_d} = \mathrm{id}_{H_d} \text{ if } d \mid k, \qquad P_{q_k}|_{H_d} = 0 \text{ if } d \nmid k.$$

This produces the pre-registered divisor tables for our three targets. For $N = 12$ (months):

| $k$ | $H_2$ | $H_3$ | $H_4$ | $H_6$ | $H_{12}$ |
|---:|---:|---:|---:|---:|---:|
| 2  | 1 | 0 | 0 | 0 | 0 |
| 3  | 0 | 1 | 0 | 0 | 0 |
| 4  | 1 | 0 | 1 | 0 | 0 |
| 6  | 1 | 1 | 0 | 1 | 0 |
| 12 | 1 | 1 | 1 | 1 | 1 |

For $N = 7$ (weekdays):

| $k$ | $H_7$ |
|---:|---:|
| 1 | 0 |
| 7 | 1 |

(The weekday case is degenerate from the obstruction's standpoint — there is only one nontrivial packet and only one nontrivial quotient — which is precisely why it functions as a *positive control*: it isolates the cyclic-concept question from the divisor-lattice question.)

For $N = 10$ (digits):

| $k$ | $H_2$ | $H_5$ | $H_{10}$ |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 5 | 0 | 1 | 0 |
| 10 | 1 | 1 | 1 |

### 2.3 The packet fraction at a layer

Let the model have residual stream dimension $d_\mathrm{model}$ and unembedding $W_U \in \mathbb{R}^{|V| \times d_\mathrm{model}}$ over the full vocabulary $V$. Let $V_R \subset V$ be the $N$ tokens identified with elements of $R$ (the twelve month-name tokens, the seven weekday-name tokens, the ten digit tokens). Let $h_\ell(x) \in \mathbb{R}^{d_\mathrm{model}}$ be the residual stream at layer $\ell$ for input prompt $x$, evaluated at the final token position.

For each layer $\ell$ we compute two readouts. The *frozen-unembedding lens score* is
$$s_\ell^{(\mathrm{lens})}(x) = (W_U h_\ell(x))_{V_R} \in \mathbb{R}^N$$
restricted to the cyclic sub-vocabulary, centered (mean-subtracted), and Fourier-transformed over $R$:
$$\hat s_\ell^{(\mathrm{lens})}(x, a) = N^{-1} \sum_{y \in R} s_\ell^{(\mathrm{lens})}(x)_y \chi_{-a}(y).$$
The *trained quotient probe score* with target $k$ is
$$s_{\ell,k}^{(\mathrm{probe})}(x) = q_k^* L_{\ell,k}(h_\ell(x)),$$
where $L_{\ell,k} : \mathbb{R}^{d_\mathrm{model}} \to \mathbb{R}^k$ is a ridge-fit affine probe ($\alpha = 10^{-2}$, matching Paper 26's quotient probe) and $q_k^*$ is the pullback to $\mathbb{R}^N$ via $s_{\ell,k}^{(\mathrm{probe})}(x)_y = L_{\ell,k}(h_\ell(x))_{y \bmod k}$.

The *packet fraction* at layer $\ell$, conductor $d$, readout type $\tau \in \{\mathrm{lens}, \mathrm{probe}_k\}$ is
$$f_{d, \ell}^{(\tau)} = \frac{\sum_{a : \mathrm{cond}(a) = d} \mathbb{E}_x |\hat s_\ell^{(\tau)}(x, a)|^2}{\sum_{a \neq 0} \mathbb{E}_x |\hat s_\ell^{(\tau)}(x, a)|^2}.$$
This is the held-out expectation of the conductor-resolved energy fraction, normalized to exclude the trivial character (since the trivial character is a per-example constant and carries no cyclic information).

### 2.4 What the divisor table predicts about $f_{d,\ell}^{(\mathrm{probe}_k)}$

For every $d \nmid k$ the obstruction predicts $f_{d, \ell}^{(\mathrm{probe}_k)} = 0$ exactly, *at every layer*, by Paper 26 §T2. These zeros are *analytic* — they are pullback artifacts, not model evidence. They appear in the manuscript only as control rows. The model-facing measurements are the *native* lens fractions $f_{d, \ell}^{(\mathrm{lens})}$ and the *retained accuracies* of the trained quotient probes; both could have come out flat across $d$, and they will not.

---

## 3. Pre-registered predictions

We commit to the following before the sweep. Negative results are as informative as positive ones; we will report them.

**P1 (full-period concentration is late and monotonic in expectation).**  
For $N = 12$ on months, $f_{12, \ell}^{(\mathrm{lens})}$ is non-decreasing in $\ell$ across the second half of the network in expectation over inputs, and the largest single-layer increment occurs in the last six layers. We commit to the qualifier *in expectation*: per-input curves may be non-monotone, but the average curve should be.

> **Settled (audit κ, 2026-06-12): REFUTED on both models.** The expectation curve is non-monotone in the second half (11 violations on Llama-3.1-8B, 9 on Mistral-7B-v0.3), and the largest single-layer increment is a mid-late crystallization jump *outside* the last six layers (Llama rows 21→22, $+0.454$; Mistral rows 17→18, $+0.388$; row = HF `hidden_states` index, 0 = embeddings, 32 = post-final-norm). Both models then *overshoot* the final value (Llama peak $0.776$ at row 24 vs. final $0.657$; Mistral peak $0.823$ at row 18 vs. final $0.785$) and decline into the readout — the third profile of §1.2 ("internal use of a finer cyclic structure than the head exposes"), replicated cross-model.

**P2 (anchor row).**  
$f_{12, 28}^{(\mathrm{lens})}_{\mathrm{Llama}} \in [0.30, 0.40]$ and $f_{12, \mathrm{final}}^{(\mathrm{lens})}_{\mathrm{Llama}} \in [0.62, 0.69]$, consistent with the Paper 26 anchor pair (raw layer-28 BF16: $0.355640$; native final logits: $0.657415$). Any sweep that does not reproduce the anchor pair within these bands has a methodological discrepancy with Paper 26 that must be reconciled before the rest of the table is interpreted.

> **Settled (audit κ, 2026-06-12): final-layer half CONFIRMED; layer-28 half REFUTED and RECONCILED.** The sweep's final row reproduces all five Paper 26 final-layer fractions to $\leq 5 \times 10^{-4}$ ($f_{12} = 0.656935 \in [0.62, 0.69]$). The layer-28 half fails its band — and the F1 reconciliation pinned why, with two exact cross-checks: (i) the causalab artifact "L28" is sweep row 29 (cosine $0.9998$ per-example against the saved `raw_features.safetensors`); (ii) scoring *Paper 26's own saved layer-28 residuals* with the model's $W_U$ slice gives $f_{12}^{(\mathrm{lens})} = 0.638165$, and the fresh sweep's row 29 gives $0.638223$ (agreement $\sim 6 \times 10^{-5}$) — both far above $0.40$. The $0.355640$ inside the band is the **full-label trained-probe** quantity (§5), not the lens quantity: P2 pre-registered a probe number as a lens band. The apparatus is fully consistent with Paper 26; the band itself conflated the two instruments of §1.2. The $\sim 0.28$ lens-vs-probe difference at this depth is a single-layer datum in P7's direction. Settlement record: [audit κ](empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md) §2.

**P3 (coarse packets emerge earlier).**  
For $N = 12$ on months, the layer index $\ell_d^*$ at which $f_{d,\ell}^{(\mathrm{lens})}$ first exceeds its final value times $0.7$ is non-decreasing in $d$ when $d$ runs over $\{2, 3, 4, 6, 12\}$. That is, parity ($H_2$) and three-fold ($H_3$) structure crystallize earlier than the full period ($H_{12}$). Falsification: if $H_{12}$ saturates at or before $H_2$ in either model, this prediction fails and the spectrum must be re-narrated.

> **Settled (audit κ, 2026-06-12): REFUTED as defined, both models (F3 fires).** Llama $\ell^*_d = (H_2{:}\,7,\ H_3{:}\,0,\ H_4{:}\,0,\ H_6{:}\,0,\ H_{12}{:}\,2)$; Mistral $(1, 0, 0, 0, 0)$ — not non-decreasing; $H_{12}$ saturates at or before $H_2$ on both. Apparatus caveat, recorded not retrofitted: $\ell^*$ as pre-registered has no guard against the noisy embedding-adjacent rows, where lens readouts are near-arbitrary and several packets cross the $0.7 \times$ threshold spuriously (e.g. Llama row 0 has $f_4 = 0.43$). The statistic, not only the divisor narrative, needs re-design before a v2 pre-registration.

**P4 (weekday positive control).**  
For $N = 7$ on weekdays, $f_{7, \ell}^{(\mathrm{lens})}$ rises from near zero in the first quarter of the network to near unity in the last quarter, monotonically in expectation. Because $C_7$ has a single nontrivial packet, $H_7$, this is the *cleanest* possible signal of cyclic-concept acquisition and serves as the positive control: a model that does not produce a $H_7$ ramp on weekdays is not solving the task cyclically at any layer.

> **Settled (audit κ, 2026-06-12): AMBIGUOUS — vacuous at the pre-registered metric.** $f_{7,\ell} = 1.000000$ identically at all 33 rows on both models, *by construction*: on the prime modulus every nontrivial character has conductor 7, so the nontrivial-energy *fraction* normalizes to 1 regardless of the data. The predicted ramp lives in the absolute nontrivial cyclic energy, which $f_{d,\ell}$ cannot express. P4 as written cannot be confirmed or refuted by the fraction; a v2 must pre-register an energy (not fraction) observable. The final-layer consistency check holds.

**P5 (digits divisor split).**  
For $N = 10$ on digits, $f_{2,\ell}^{(\mathrm{lens})}$ and $f_{5,\ell}^{(\mathrm{lens})}$ separate non-trivially across layers: parity ($H_2$, the even/odd structure that base-10 digit prediction is well-known to handle via dedicated heads) saturates earlier than the order-5 packet ($H_5$). This will provide the strongest cross-task replication of P3 because the divisor structure of $10 = 2 \cdot 5$ is the cleanest two-prime conductor row available.

> **Settled (audit κ, 2026-06-12): DEFERRED.** No digits baseline prompt set exists in the tree (the Paper 26 apparatus never produced `digits/baseline/`); generating a fresh prompt set on the fly would not be the pre-registered input. Deferred with P8.

**P6 (predecessor-leakage asymmetry).**  
For both $N = 12$ and $N = 7$, the centered class-conditional packet profile (Paper 12 §weekday and §month rows) will display the predecessor-leakage asymmetry reported in Paper 12 *more strongly* at intermediate layers than at the final logits. This is a layerwise refinement of the weekday/month asymmetry already documented at a single layer in Paper 12, and it is consistent with the base-N shortcut localization of Paper 26 §Nonlinear Base-10 Shortcut Ablation: nonlinear sum/carry features survive at intermediate layers and bias adjacent-class transitions.

> **Settled (audit κ, 2026-06-12): DEFERRED — instrument not in the driver set.** The lens arm outputs only $\mathbb{E}_x$-averaged packet fractions; class-conditional profiles need an analysis script that does not exist. The captured per-layer residual streams (`empirical/data/residual_streams_*.safetensors`, BF16 $[n, 33, 4096]$, both models × both tasks) contain everything needed to settle P6 offline without re-running the models.

**P7 (lens vs. trained-probe gap is layer-dependent).**  
The frozen-unembedding lens $f_{d, \ell}^{(\mathrm{lens})}$ and the trained quotient probe $f_{d, \ell}^{(\mathrm{probe}_{12})}$ agree to within $0.10$ at the final layer but diverge by more than $0.10$ in the middle third of the network. This is the layerwise measurement of how much each layer's residual stream is already in the unembedding's basis, and it directly addresses the tuned-lens motivation (Belrose et al. 2023): tuned lenses help most where this gap is largest.

> **Settled (audit κ, 2026-06-12): DEFERRED — probe-arm driver not finalized.** `quotient_probe_packet_score_layerwise.py` (§8) was never written; only Paper 26's single-layer version exists. One single-layer datum in P7's direction fell out of the P2 reconciliation: at causalab-L28 (row 29 of 32+1), lens $f_{12} = 0.638$ vs. full-label probe $0.356$ — a gap of $\sim 0.28$ at a *late* layer, larger than P7's mid-network threshold. The captured residual streams make the probe arm runnable offline.

### 3.A V/M empirical-propagation predictions (audit κ; appended from v2insert-05; pre-registered under v2insert-04 §3.1 three-outcome rule)

Paper 47 (proposed) *The Arithmetic Decoupling Theorem* (v2insert-02) predicts that the single-prime-power packets (V) and the cross-prime carry packets (M) of a cyclic conductor lattice are Hilbert-subspace orthogonal in `ℂ^N` by Pontryagin character orthogonality. On Paper 36's three task algebras the V/M analog is:

| Task | Algebra | V analog (single-prime / prime-power packets) | M analog (cross-prime carry packets) | Dim V | Dim M |
|---|---|---|---|---:|---:|
| weekdays | `ℤ/7` (prime) | `H_7` | none | 6 | 0 |
| digits | `ℤ/10 = 2·5` | `H_2 + H_5` | `H_{10}` | 5 | 4 |
| months | `ℤ/12 = 2²·3` | `H_2 + H_3 + H_4` | `H_6 + H_{12}` | 5 | 6 |

Define the depth-normalized saturation index of a packet as
$$\sigma_d := \mathrm{mean}_{\ell} \big[\, f_{d,\ell}^{(\mathrm{lens})} \cdot \ell / L_{\mathrm{model}} \,\big] \big/ f_{d, \mathrm{final}}^{(\mathrm{lens})}.$$

**P8 (V/M-saturation asymmetry on digits, ℤ/10) — primary test.** Three-outcome pre-claim:
- **K-branch (V/M decoupling propagated):** σ_2 and σ_5 (V packets) differ from σ_{10} (M packet) by more than seed noise on at least one model.
- **L-branch:** σ_2, σ_5, σ_{10} statistically indistinguishable; V/M decoupling is lift-tangent only, not propagated through training.
- **Joint-on-disjoint:** σ_2, σ_5 differ from σ_{10} but the direction of separation is opposite the prediction (e.g., M saturates earlier than V) — propagation exists but with a model-specific sign.

> **Settled (audit κ, 2026-06-12): DEFERRED** — no digits baseline prompt set exists (see P5). P8's role as primary test passes to P9, which was measurable on both models.

**P9 (V/M-saturation asymmetry on months, ℤ/12) — non-squarefree stress test.** Three-outcome pre-claim:
- **K-branch:** σ_2, σ_3, σ_4 cluster together and separate from σ_6, σ_{12} as a measurable structural feature per model.
- **L-branch:** no clustering; V/M decoupling fails on non-squarefree rings.
- **Joint-on-disjoint:** V-cluster and M-cluster both exist but the prime-power packet `H_4` clusters with M rather than V, revealing a V / W / M trichotomy on non-squarefree rows (a method-improvement event under v2insert-04 §3.1).

> **Settled: K-branch on BOTH models; propagation REAL and significant (audit κ 2026-06-12 point estimates + bootstrap 2026-06-13; L-branch excluded both models, F7 does not fire).** Measured σ (rows 0–32, $L = 32$, inclusive V/M per audit χ_12):
>
> | | σ_2 (V) | σ_3 (V) | σ_4 (V) | σ_6 (M) | σ_12 (M) |
> |---|---:|---:|---:|---:|---:|
> | Llama-3.1-8B | 0.5642 | 0.9397 | 0.9215 | 0.4056 | 0.4369 |
> | Mistral-7B-v0.3 | 1.8856 | 1.2749 | 1.6706 | 0.4522 | 0.4070 |
>
> On both models every V-σ exceeds every M-σ (full order separation, same direction: V carries relatively more depth-weighted mass, M concentrates late), the M pair is tight, and the ordering σ_6 > σ_12 replicates. On Mistral the V/M gap (0.82) exceeds the V-internal spread (0.61): K-branch. On Llama the point estimates *suggested* the V triple does not cluster — σ_2 = 0.564 sits closer to the M pair than to {σ_3, σ_4} ≈ 0.93 — which was read (point-estimate only) as a joint-on-disjoint with H_2 the defector.
>
> **Bootstrap update (2026-06-13; `empirical/vm_bootstrap_significance.py`, 2000 prompt resamples — settles the significance leg).** The separation is significant on BOTH models: gap = min(σ_V) − max(σ_M) > 0 in 100% of resamples (Llama 0.13, CI [0.04, 0.23]; Mistral 0.82, CI [0.65, 1.05]). **Both models settle at K-branch**; F7 does not fire. The H_2-defector reading is *refuted*: σ_2 exceeds the entire M cluster in 100% of resamples (CI [0.49, 0.67] vs σ_12 CI [0.42, 0.45], zero overlap) — H_2 is firmly in V, not defecting. What is real is an internal V **three-level ladder on Llama** with non-overlapping bands: M (≈0.42) < H_2 (≈0.57) < {H_3, H_4} (≈0.93) — parity saturating at intermediate depth between the carry packets and the higher single-prime packets. Mistral's V triple is uniformly high (effect ~6× Llama's).
>
> **Checkpoint pass (2026-06-13; base→instruct weight axis, both families, same raw prompts).** K-branch holds on 3 of 4 checkpoints: gap min(σ_V)−max(σ_M) = +0.13 (Llama base, P=1.000), +0.82 (Mistral base, P=1.000), +0.64 (Mistral-Instruct, P=1.000), but **−0.13 on Llama-3.1-8B-Instruct (P(gap>0)=0.002 — significantly negative, K-branch BROKEN)**. The break is parity-localized: Llama instruct-tuning collapses σ_2 (0.56→0.40, below the carry packets) and lifts σ_6 (0.41→0.54), inverting their order; H_3,H_4 stay above M. Mistral instruct-tuning preserves the structure. So V/M propagation is robust across pretrained models and survives Mistral instruct-tuning, but Llama-3.1's instruct-tuning specifically reorganizes the parity packet. Caveat: instruct models run on raw (non-chat) prompts for comparability — but Mistral-Instruct (same condition) preserves K-branch, so the Llama-Instruct break is not a generic raw-prompt artifact. Artifacts: `empirical/reports/vm_bootstrap_significance.json`, figure `empirical/reports/figures/vm_checkpoint_gap.{pdf,png}`.

**P10 (negative control on weekdays, ℤ/7).** No V/M split exists, so the load-bearing pre-claim is:
- **K-branch:** no spurious V/M signal; only P4's `H_7` ramp is present.
- **L-branch:** a spurious V/M signal appears, indicating the V/M signature elsewhere is a measurement artifact (P8/P9 would then be uninterpretable).
- **Joint-on-disjoint:** spectrum shows structural separation on a different axis (model-specific apparatus signature).

P10 is *the load-bearing negative control* for P8 and P9.

> **Settled (audit κ, 2026-06-12): K-branch, both models.** $f_{7,\ell} = 1.000000$ at all 33 rows on Llama and Mistral: no off-divisor or spurious V/M-like structure appears at any layer (none *can* at the fraction level on a prime modulus — the control is partly structural, as the settlement record already anticipated — and none did). F6 does not fire; P9 remains interpretable.

**Status (audit κ run 2026-06-12; supersedes the v2insert-07 §3 deferral).** Audit κ was executed on GCP (transient `g2-standard-8` + L4, BF16, transformers 4.57.6) on Llama-3.1-8B and Mistral-7B-v0.3 across (months, weekdays); the digits arm stays deferred (no pre-registered digits prompt set exists). Outcomes: P1 refuted (both models), P2 final-half confirmed / layer-28 half refuted-and-reconciled (instrument conflation), P3 refuted as defined, P4 vacuous at the fraction metric, P5/P6/P7/P8 deferred (see each), P9 Mistral K-branch + Llama joint-on-disjoint (propagation real; F7 excluded), P10 K-branch. Settlement record and environment: [`empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md`](empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md); spectra: `empirical/reports/layerwise_packet_spectroscopy_<task>_<model>.{md,json}`; per-layer BF16 residual streams retained under `empirical/data/` for the deferred arms.

**Structural prerequisite settled (audit χ_12, 2026-05-20, [`empirical/reports/audits_xi_chi_settlement.md`](empirical/reports/audits_xi_chi_settlement.md)):** the V/M Bures-Hessian sub-bundle decomposition on `D(ℂ¹²)` was audited under three candidate partitions:
- *Strict V/M* (V = `H_2 + H_3`, dim 3): K-branch at machine floor.
- *Inclusive V/M* (V = `H_2 + H_3 + H_4`, dim 5; prime-power `H_4` folded into V): K-branch at machine floor.
- *Trichotomy V/W/M*: **joint-on-disjoint at tangent tier** — W ⊥ M overlap 0.447, NOT machine floor.

Conclusion for audit κ: **use the inclusive V/M convention on `ℤ/12`** (months task). The prime-power H_4 belongs to V (kinematic sector) at the Bures-Hessian tangent tier. The trichotomy V/W/M is NOT a clean tangent-level structural choice (P9 joint-on-disjoint realized at the tangent level by audit χ_12). When audit κ runs, σ_V should bin `{H_2 + H_3 + H_4} = {6, 4, 8, 3, 9}` and σ_M should bin `{H_6 + H_{12}} = {2, 10, 1, 5, 7, 11}`.

---

## 4. Empirical reading rule

We restate Paper 26's reading rule in spectroscopic form because it is the load-bearing methodological commitment of the program.

**Theorem-side rows (analytic pullback checks):**

- Forbidden-packet zeros for trained quotient probes at any layer: $f_{d, \ell}^{(\mathrm{probe}_k)} = 0$ for every $d \nmid k$. These are not model evidence; they certify that the projector was implemented correctly.
- Native-then-binned packet fractions for the lens: $f_{d, \ell}^{(\mathrm{lens, binned to } k)}$ for $d \nmid k$ should match floor (numerical machine epsilon at fp32, $\sim 10^{-33}$ at fp64 accumulation). Same status.

**Model-side rows (could have failed before any projector was applied):**

- $f_{d, \ell}^{(\mathrm{lens})}$ across all $d \mid N$ before any binning. These are the native packet fractions of the model's own residual stream as read by its own unembedding.
- Retained held-out accuracy of trained quotient probes: $\mathrm{acc}_{\ell, k}^{\mathrm{(probe)}}$. How much of the task survives when the readout is packet-blind by construction.
- The layerwise shape of all of the above: monotonicity, saturation index, lens/probe gap.

Forbidden zeros enter the manuscript exclusively as control rows in tables that *also* contain model-facing numbers. We will not report a table whose only contents are analytic zeros.

---

## 5. Anchor measurement (Paper 26, restated and embedded)

The Paper 26 anchor pair is the layer-28 row of the months target on Llama-3.1-8B. We restate it here in the spectroscopic table format used throughout this paper, exactly as it will appear after the full sweep, with the remaining rows marked `pending`.

Llama-3.1-8B, months ($N = 12$), packet fractions $f_{d, \ell}^{(\mathrm{lens})}$ (measured, audit κ 2026-06-12; key rows — full 33-row tables in `empirical/reports/layerwise_packet_spectroscopy_months_llama31_8b.md`):

| row (HF `hidden_states` index) | $f_{2,\ell}$ | $f_{3,\ell}$ | $f_{4,\ell}$ | $f_{6,\ell}$ | $f_{12,\ell}$ |
|---:|---:|---:|---:|---:|---:|
| 0 (embed) | 0.0017 | 0.0583 | 0.4305 | 0.1529 | 0.3565 |
| 16 (mid) | 0.0123 | 0.2481 | 0.0408 | 0.0698 | 0.6289 |
| 21 (pre-jump trough) | 0.1549 | 0.2358 | 0.1253 | 0.2505 | 0.2336 |
| 22 (post-jump) | 0.0616 | 0.0730 | 0.0500 | 0.1279 | 0.6875 |
| 24 (overshoot peak) | 0.0361 | 0.0632 | 0.0387 | 0.0857 | 0.7762 |
| 29 (= causalab "L28", raw BF16) | 0.0810 | 0.0706 | 0.0547 | 0.1555 | 0.6382 |
| 32 (final, post-norm) | 0.0511 | 0.0660 | 0.0591 | 0.1669 | 0.6569 |

The final row reproduces the Paper 26 native-logit anchors ($0.050608$, $0.066390$, $0.059082$, $0.166506$, $0.657415$) to $\leq 5 \times 10^{-4}$. The row-29 $f_{12} = 0.6382$ agrees to $\sim 6 \times 10^{-5}$ with the lens score recomputed from *Paper 26's saved layer-28 residuals* ($0.638165$); the Paper 26 number $\approx 0.356$ at this depth is the full-label **trained-probe** quantity, a distinct instrument (see P2 settlement above).

The weekday final row (and every other weekday row) is $f_{7,\ell} = 1.0$, on both models — see P4/P10. The digit rows remain pending (no pre-registered digits prompt set).

---

## 6. Why this is the right next paper after Paper 26

Paper 26 §What Is Missing lists six gaps. The current paper closes one of them — item 3, *true tuned-lens instantiation* — and provides the substrate for closing two more (item 2, *second model family*; item 4, *causal base-10 ablation*, becomes layer-targetable once the spectrum is known).

The spectrum also feeds three of the spin-off paper candidates identified in the cross-paper comparison with [Vaswani et al. 2017](https://arxiv.org/abs/1706.03762):

- *Multi-head attention as packet allocation* ([Paper 25](25.arithmetic_frame_cost_and_curvature_linearization.md) frame-cost extension): per-head packet alignment can only be measured after the per-layer spectrum is known, because head allocations live inside layers.
- *Sinusoidal PE as non-rational conductor algebra* (Paper 26 T1 applied to positional encoding): the position-mod-period analogue of the present sweep, done on the position-id sub-vocabulary instead of the months sub-vocabulary, is the cleanest length-extrapolation experiment licensed by the corpus.
- *Label smoothing in the conductor blind spot* ([Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md) + [Paper 34](34_the_conductor_blind_spot.md)): the layerwise spectrum is the diagnostic against which the label-smoothing-vs-cubic-update ablation should be evaluated; without it, the ablation cannot distinguish "smoothing helps because it activates the cubic" from "smoothing helps for unrelated reasons."

Layerwise packet spectroscopy is therefore not just the natural completion of Paper 26 — it is the empirical prerequisite for at least three follow-up papers that the program already wants to write.

---

## 7. Failure conditions and what each falsifies

We make the failure conditions explicit so the paper does not become unfalsifiable through narrative drift.

- **F1.** Anchor failure (P2): if either Paper 26 anchor number is outside its band, the sweep is not consistent with Paper 26 and must be reconciled before any spectrum is reported.
- **F2.** No full-period ramp on weekdays (P4): if $f_{7,\ell}^{(\mathrm{lens})}$ is flat or non-monotone, the cyclic-concept story for Llama/Mistral on weekdays is false at the spectroscopic level, regardless of behavior accuracy.
- **F3.** Inverted divisor ordering (P3): if $H_{12}$ saturates before $H_2$ on months, the divisor-lattice interpretation must be replaced.
- **F4.** Probe/lens gap collapse (P7): if the trained-probe and frozen-lens spectra are identical at all layers, the "tuned-lens helps most in the middle" hypothesis is falsified on these tasks and the corpus claim that tuned-lens improvements correlate with residual-stream basis drift is weakened.
- **F5.** Cross-model non-replication: if Mistral-7B-v0.3 produces a qualitatively different spectrum from Llama-3.1-8B on the same task (different monotonicity, different saturation order), the spectrum is model-specific rather than task-specific, and Paper 26's cross-model replication ambition is downgraded.
- **F6 (V/M empirical-propagation falsifier, audit κ).** If the weekday control P10 fires its L-branch (a spurious V/M signal appears on `ℤ/7` where no V/M split exists), P8 and P9 become uninterpretable; audit κ is inconclusive and the V/M empirical-propagation question is deferred until the apparatus signature is reconciled.
- **F7 (V/M decoupling lift-tangent only).** If σ_V and σ_M are statistically indistinguishable on *both* digits and months across *both* models (L-branch of P8 and P9), Paper 47 (proposed) V/M arithmetic decoupling is *lift-tangent only* — not propagated through transformer training to the trained network's residual stream. The Paper 47 row-generalization (audit α/η/θ, settled at K-branch on the conductor lattice) is unaffected; only the empirical-propagation claim falls.
- **F8 (cross-task sign reversal).** If the σ_V − σ_M separation on digits points opposite to the separation on months (e.g., V saturates earlier than M on digits but later on months), the V/M empirical signature is not row-stable across `ℤ/10` and `ℤ/12`; Paper 47's row-generalization is empirically weakened (separate from the arithmetic-substrate row-generalization settled by audits α/η/θ).

Each of F1–F8 produces a *narrower* paper; none produce a discardable paper.

**Failure-condition ledger (audit κ, 2026-06-12).** F1 fired (layer-28 band) and was reconciled per its own instruction before interpretation — instrument conflation, not methodological inconsistency (P2 settlement). F3 fired by the letter of the $\ell^*$ statistic, with the early-noise apparatus caveat recorded (P3 settlement). F2 did not fire at the only level the fraction metric can express (P4 settlement). F4 not evaluable (probe arm deferred). F5 did not fire: the two models agree qualitatively (jump + overshoot + decline; same V/M direction; σ_6 > σ_12 on both). F6 did not fire (P10 K-branch). F7 did not fire: V/M separation present on both models — the Paper 47 (proposed) empirical-propagation claim survives. F8 not testable across tasks (digits deferred); no sign reversal between models on months.

---

## 8. Script inventory

The full sweep requires the following artifacts, all to live under `empirical/`. Names follow Paper 26 convention.

```text
empirical/layerwise_packet_spectroscopy.py
  Top-level driver. Args: --model-tag, --task, --layers, --output-dir.
  Loads checkpoint, runs forward passes over the task dataset, saves
  per-layer last-token residual streams to a safetensors file.

empirical/native_logit_lens_packet_score_layerwise.py
  Lens arm. Reads residual streams, applies the model's own W_U, restricts
  to V_R, centers, Fouriers, computes f_{d,ell}^(lens) for every layer.
  Output: empirical/reports/layerwise_packet_spectroscopy_<task>_<model>.md
  and .json. Also produces the after-binning forbidden-fraction control
  rows for each quotient k.

empirical/quotient_probe_packet_score_layerwise.py
  Trained-probe arm. Per layer, fits ridge regression to month/weekday/
  digit mod k for each k | N. Lifts via q_k^*. Computes f_{d,ell}^(probe_k).
  Same output schema.

empirical/months_hidden_state_shortcut_audit_layerwise.py
  (Optional, follow-up.) Per-layer residualization against decimal sum,
  carry features, source month, offset. Per-layer ablated f_{d,ell}.
  Extends Paper 26 single-layer audit to a layerwise causal proxy.

empirical/reports/layerwise_packet_spectroscopy_months_llama31_8b.md
empirical/reports/layerwise_packet_spectroscopy_months_llama31_8b.json
empirical/reports/layerwise_packet_spectroscopy_months_mistral7b_v0_3.md
empirical/reports/layerwise_packet_spectroscopy_months_mistral7b_v0_3.json
empirical/reports/layerwise_packet_spectroscopy_weekdays_llama31_8b.md
empirical/reports/layerwise_packet_spectroscopy_weekdays_llama31_8b.json
empirical/reports/layerwise_packet_spectroscopy_weekdays_mistral7b_v0_3.md
empirical/reports/layerwise_packet_spectroscopy_weekdays_mistral7b_v0_3.json
empirical/reports/layerwise_packet_spectroscopy_digits_llama31_8b.md
empirical/reports/layerwise_packet_spectroscopy_digits_llama31_8b.json
empirical/reports/layerwise_packet_spectroscopy_digits_mistral7b_v0_3.md
empirical/reports/layerwise_packet_spectroscopy_digits_mistral7b_v0_3.json
```

Run command schema (matches Paper 26 style):

```text
python empirical\layerwise_packet_spectroscopy.py ^
  --model-tag llama31_8b ^
  --task months ^
  --layers all ^
  --output-dir empirical\reports
```

The full grid is six driver invocations followed by twelve scoring invocations. Total wall-clock on a single H100 is dominated by the forward passes (under 30 minutes per model across all three tasks at the dataset sizes used in Paper 26).

---

## 9. Result templates

The manuscript v0.2 will populate the templates below. They are reproduced here so reviewers can verify in advance that no result table will be added that does not have a pre-registered shape.

### 9.1 Spectrum table, months on Llama-3.1-8B

Rows: layer $\ell \in \{0, 1, \dots, 32\}$ (embedding through final). Columns: $f_{2,\ell}, f_{3,\ell}, f_{4,\ell}, f_{6,\ell}, f_{12,\ell}$ for the lens arm; same for each $\mathrm{probe}_k$, $k \in \{2,3,4,6,12\}$, restricted to its allowed packets.

### 9.2 Probe-retained accuracy table

Same rows. Columns: $\mathrm{acc}_{\ell, k}^{(\mathrm{probe})}$ for $k \in \{2, 3, 4, 6, 12\}$.

### 9.3 Lens vs. probe gap

Same rows. Single column: $\sum_d | f_{d, \ell}^{(\mathrm{lens})} - f_{d, \ell}^{(\mathrm{probe}_N)} |$, the $\ell^1$ packet-profile distance between the two arms.

### 9.4 Cross-model overlay

A single figure: $f_{12, \ell}^{(\mathrm{lens})}$ vs. $\ell / L_{\mathrm{model}}$ (depth normalized), Llama vs. Mistral, with the Paper 26 anchor pair marked.

### 9.5 Weekday and digit positive-control rows

For weekdays: $f_{7, \ell}$ across all layers. For digits: $f_{2, \ell}, f_{5, \ell}, f_{10, \ell}$.

---

## 10. Scope and what comes next

This paper is a measurement. It does not propose a new theorem (the theorems are in Papers 11, 17, 26) and does not propose a new training recipe (those are in Papers 12 and 34).

The natural follow-ups, in priority order:

1. **Causal layer-targeted ablations.** Once the spectrum identifies the layer (or short layer range) where $H_{12}$ is sharpened, activation patching at that layer with packet-projected hidden states becomes a clean intervention. This addresses Paper 26 §What Is Missing item 4.

2. **Per-head packet attribution.** The spectrum is at the residual-stream level. The next resolution is per-head: at each attention layer, compute the packet profile of each head's output before the projection $W^O$. This is the input to the *multi-head attention as packet allocation* paper sketched in the Vaswani comparison.

3. **Positional packet spectroscopy.** Apply the same method to the position-id sub-vocabulary across context windows. This is the empirical core of the *sinusoidal PE as non-rational conductor algebra* paper.

4. **Cross-family replication beyond Mistral.** Phi, Gemma, Qwen — each a different vocab, tokenizer, and training corpus. The spectrum should be reported for each, with the divisor table held fixed.

5. **Tuned-lens conductor diagnostic.** Train an actual Belrose-style tuned lens at each layer, then packet-score its output. The prediction is that tuned-lens improvements over the frozen-lens are concentrated in layers where the lens/probe gap (P7) is largest.

6. **Connection to Neural LoFi (Dandi et al., arXiv 2605.13612v1).** The Neural LoFi second-order spectral analysis and the present first-order packet spectroscopy live in adjacent diagrams; a unified reading would treat the packet profile as the *spectral structure of the local Fisher* at each layer, with the Neural LoFi outlier eigenvalues as the across-packet coupling that the present method does not directly resolve. This is the natural site for an explicit comparison.

6a. **Connection to Data-driven Circuit Discovery (Rai, Geva & Yao 2026, arXiv:2605.09129).** DCD constructs per-example edge-attribution vectors `s_i ∈ ℝ^|E|` from EAP-IG and clusters them via PCA + K-means to recover *multiple* circuits per dataset, observing that hypothesis-driven circuit discovery on mixed-task datasets returns single circuits that smear distinct mechanisms (87% mixed-faithfulness at 10% mixture injection). The present spectrum gives the layerwise residual-stream substrate; DCD gives the per-example attribution substrate. The two substrates are connected by Paper 26 T1 + Paper 34 Corollary 3.11: the EAP-IG score is itself a quotient-respecting rank-`|E|` readout, so its cross-packet content at the head's maximum-entropy point is in the same null space the present packet spectroscopy resolves at the residual-stream level. The joint prediction: applying DCD-style clustering to attribution vectors derived at the *qualifying layer* `ℓ*` of §6.2 (where `f_{N,ℓ}` first reaches 0.7 of its final-layer value) should recover the divisor-count cluster count `τ(N)` on cyclic mixed datasets, with the per-cluster centroid's packet-projection profile matching the divisor table of §2.2. This is the empirical co-prediction of Paper 26 T1 on the attribution-vector substrate.

7. **V/M empirical-propagation bridge (audit κ of v2insert-05; RUN 2026-06-12).** Extend the sweep's post-hoc analysis to bin packet-fractions into V (single-prime / prime-power) and M (cross-prime carry) groupings per task, and compute the depth-normalized saturation index σ_d. Tests whether Paper 47 (proposed) V/M arithmetic decoupling propagates through transformer training to leave a measurable signal on residual-stream packet content. Compute is additive on the same forward passes; no new theory or training required. The pre-registered predictions P8 (digits), P9 (months), and P10 (weekdays control) are stated in §3.A above under the three-outcome matched-pair rule (v2insert-04 §3.1 extension). **Status: executed on months + weekdays, both models** — P9 settles propagation as real (Mistral K-branch, Llama joint-on-disjoint with H_2 the defector), P10 K-branch, P8 deferred with the digits arm. Results: `empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md`.

---

## 11. Conclusion

Paper 26 proved which packets a quotient-respecting linear or logit-lens readout can see, and applied the theorem to one anchor measurement on Llama-3.1-8B months. This paper proposes the protocol that turns that anchor into a *spectrum*: a packet-resolved, layer-resolved map of where in the residual stream each conductor packet of a chosen cyclic task algebra concentrates. The protocol is preregistered, the divisor tables are tabulated, the failure conditions are explicit, the scripts are named, and the result templates are fixed. Every reportable number is either an analytic pullback check (which we will keep separate, per the empirical reading rule) or a model-facing quantity that could have failed before any projector was applied.

The minimal deliverable is one figure per model–task: $f_{d, \ell}$ vs. $\ell$. The maximal deliverable is the same figure plus the probe-retained accuracy table, the lens/probe gap curve, the cross-model overlay, and the weekday/digit positive controls. Both are reachable on existing open-weights checkpoints with no training and no new theorem.

The spectrum is the empirical prerequisite for the multi-head, positional-encoding, and label-smoothing follow-up papers that the program already wants to write. It is also, on its own, the cleanest available picture of *how a transformer assembles a cyclic concept*, layer by layer, packet by packet.

---

*Draft v0.1 — May 19, 2026 — protocol, pre-registered predictions, and Paper 26 anchor measurement.*

*Draft v0.2 — June 12, 2026 — audit κ executed (GCP, L4, BF16): months + weekdays spectra measured on Llama-3.1-8B and Mistral-7B-v0.3; P1–P4, P9, P10 settled (each annotated in §3/§3.A); §5 anchor table populated and the layer-28 anchor reconciled (lens/probe instrument conflation); failure-condition ledger added to §7. Digits arm (P5/P8), class-conditional arm (P6), and trained-probe arm (P7) remain deferred — the captured per-layer residual streams under `empirical/data/` suffice to settle P6 and P7 offline.*
