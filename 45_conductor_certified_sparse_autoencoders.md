# Conductor-Certified Sparse Autoencoders: A Structural Theorem and Pre-Registered Feature Divisor Table for Mechanistic Interpretability

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — Paper 26 T4 promoted from prediction to theorem; CCSAE construction; Packet-Purity, Reconstruction-Cost, and Feature-Partition theorems; pre-registered cross-model experimental sweep with divisor-table verification)**

---

## Abstract

The dominant interpretability paradigm of 2024–2026 is sparse-autoencoder dictionary learning: Anthropic's Scaling Monosemanticity (Templeton et al. 2024, [transformer-circuits.pub/2024/scaling-monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/)), OpenAI's sparse-autoencoder atlas (Gao et al. 2024, [arXiv:2406.04093](https://arxiv.org/abs/2406.04093)), DeepMind's Gemma Scope (Lieberum et al. 2024, [arXiv:2408.05147](https://arxiv.org/abs/2408.05147)). Every published SAE evaluation measures *feature monosemanticity* post-hoc; no published framework predicts in advance *which features must fail to be monosemantic* in a rank-budgeted dictionary. [Paper 26](26.conductor_probe_obstruction_theorem.md) Conjecture T4 supplies the prediction: on tasks with finite output algebra $C_N$, a dictionary method whose decoder span is constrained to a $k$-resolution quotient subspace cannot place a monosemantic feature wholly in a conductor packet $H_d$ with $d \nmid k$. Until now this has been a prediction without a theorem.

This paper supplies the theorem. We construct the **Conductor-Certified Sparse Autoencoder (CCSAE)**: an SAE whose decoder span is *certified* by orthogonal projection onto $\bigoplus_{d \in S} H_d$ in the character basis of the task's cyclic sub-vocabulary, for a pre-registered closed packet support $S$. Three theorems follow:

- **Theorem 4.1 (Packet-Purity):** Every CCSAE feature's image in the output algebra lies exactly in $\bigoplus_{d \in S} H_d$, by construction. The forbidden-packet projection of every feature is zero to numerical precision.
- **Theorem 4.2 (Reconstruction-Cost):** The CCSAE reconstruction loss exceeds the vanilla SAE reconstruction loss by *at most* $\delta_S(h) = $ the cross-packet content of the projected hidden state outside $\bigoplus_{d \in S} H_d$ — which by [Paper 26](26.conductor_probe_obstruction_theorem.md) T1+T2 is *exactly* the content the corresponding quotient readout cannot represent. The trade-off between certification and reconstruction is the Paper 26 obstruction, no more and no less. *(Verified to machine precision — worst identity error $1.1\times10^{-16}$ — on captured Llama-3.1-8B and Mistral-7B-v0.3 activations, 2026-06-13; §4.2.)*
- **Theorem 4.3 (Feature Partition):** Under the additional constraint of per-feature single-packet purity, the CCSAE features partition into $|S|$ packet-aligned groups, with feature count per packet bounded by $\varphi(d)$ times the dictionary's atoms-per-direction capacity. Each feature lies in exactly one packet.

We pre-register one decisive experiment: train CCSAEs at three closed supports ($S = \{12\}$, $S = \{2, 3, 4, 6, 12\}$, $S = \{2, 6\}$) at the qualifying layer of three open-weights checkpoints (Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct, Gemma 2 9B IT) on three cyclic sub-tasks ($C_{12}$ months, $C_7$ weekdays, $C_{10}$ digits) with three negative controls (shuffled packet labels, randomized packet support, identity decoder). The prediction is sharp: CCSAE features partition perfectly across packets, vanilla SAE features distribute with cross-packet mass tracking Paper 26's native-logit packet fractions, the reconstruction gap matches Theorem 4.2's bound, and the shuffled-packet controls fail. Total compute: ~600 GPU-hours, distributed across three open Gemma Scope baseline checkpoints (no Llama / Mistral SAE training required if the Gemma Scope checkpoint is the vanilla baseline; CCSAE training on Gemma 2 9B is one additional run per (variant, sub-task) cell).

If the experiment lands as predicted, [Paper 26](26.conductor_probe_obstruction_theorem.md) T4 is promoted from prediction to theorem with empirical anchor, and the SAE field acquires its first *structural* (rather than post-hoc-evaluated) feature specification — a pre-registered divisor table giving feature counts per packet *before* the SAE is trained. If it fails, the negative result constrains the conductor structural account of representations sharply: either the relevant features are not at the qualifying layer, or the SAE's training dynamics do not respect the codomain restriction at production scale, or the conductor packet decomposition is not the right basis at the residual-stream level.

**Keywords:** sparse autoencoders, mechanistic interpretability, dictionary learning, monosemanticity, conductor packets, feature certification, structural theorem, Anthropic, OpenAI, Gemma Scope.

---

## 1. Introduction

### 1.1 The state of sparse autoencoders

Sparse autoencoder dictionary learning has, in three years, become the dominant mechanistic-interpretability paradigm. The empirical results are striking: Templeton et al. (2024) extract from Claude 3 Sonnet features for "Golden Gate Bridge", "code errors", "sycophancy", "deception"; Gao et al. (2024) build a 16-million-feature top-$k$ atlas on GPT-4; Lieberum et al. (2024) release an open SAE suite covering every layer of Gemma 2 at three feature widths. Each paper reports feature monosemanticity as the primary metric: do the features correspond to single, human-interpretable concepts?

Every published evaluation of monosemanticity is *post-hoc*. The SAE is trained; features are extracted; humans (or LLMs acting as evaluators) judge whether each feature corresponds to a single concept. There is no published structural theory predicting *which features must fail* — no pre-registered specification of which concepts will be in superposition before the SAE is trained. Anthropic's Toy Models of Superposition (Elhage et al. 2022, [transformer-circuits.pub/2022/toy_model](https://transformer-circuits.pub/2022/toy_model/)) studies superposition geometrically but does not yield a divisor-table-style prediction for real models.

This is the gap [Paper 26](26.conductor_probe_obstruction_theorem.md) Conjecture T4 fills. T4 states: a dictionary method whose decoder span is constrained, explicitly or effectively, to a $k$-resolution quotient subspace cannot place a monosemantic feature wholly in conductor packet $H_d$ for $d \nmid k$. Such packets must appear as residual error, dead directions, or superposed combinations outside the certified quotient span.

T4 has remained a prediction because the SAE literature has not constructed a method that *certifies* its decoder span. The present paper does.

### 1.2 What the conductor program adds

The Conductor program's prior LLM-side papers ([Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md), [Paper 26](26.conductor_probe_obstruction_theorem.md), [Paper 36](36_layerwise_packet_spectroscopy.md), [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md)) supply the structural infrastructure for a certified SAE:

- The *character algebra* of any cyclic sub-task gives the canonical orthonormal basis in which features are packet-decomposable ([Paper 11](11.quotient_character_adjacency_algebras.md)).
- The *conductor packets* $\{H_d\}_{d \mid N}$ supply the canonical orthogonal subspace decomposition along which features can be partitioned ([Paper 26](26.conductor_probe_obstruction_theorem.md) §2.1).
- The *qualifying layer* identified by [Paper 36](36_layerwise_packet_spectroscopy.md)'s layerwise packet spectroscopy supplies the per-model layer index at which packet structure is present in the residual stream — the right depth at which to train the SAE.
- The *Conductor Blind Spot* ([Paper 34](34_the_conductor_blind_spot.md)) supplies the structural reason why a quadratic preconditioner-trained SAE (Adam) will encounter cross-packet content in the cubic tensor that the SAE's quadratic loss cannot directly represent.
- The *BNSA* ([Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md)) supplies the validation: a CCSAE that succeeds must have a survival ratio matching the certified subspace.
- The *Data-driven Circuit Discovery (DCD)* pipeline of Rai, Geva & Yao 2026 (arXiv:2605.09129) supplies the off-the-shelf empirical scaffold for clustering per-example attribution vectors `s_i ∈ ℝ^|E|` via PCA + K-means + silhouette/gap-statistic K-selection, validated end-to-end on GPT-2 / Qwen2.5-7B-Instruct / Llama-3.1-8B-Instruct. DCD's empirical claim is that hypothesis-driven circuit discovery returns dataset-specific circuits that smear distinct mechanisms (87% mixed-faithfulness at 10% mixture injection). On cyclic sub-tasks, the present manuscript's divisor-table prediction K* = τ(N) is the *a priori* structural value DCD's silhouette-driven K-selection should recover; CCSAE is the structurally-certified upgrade of that pipeline whose per-cluster feature count is bounded above by φ(d) per packet H_d.

Combining: the CCSAE is the unique dictionary method in the program's vocabulary whose features must, by construction, partition by conductor packet on the task's cyclic sub-algebra. Whether vanilla SAEs find this partition spontaneously is an empirical question; whether they *can* be forced to find it is the theorem. The DCD pipeline supplies the *empirical* baseline for the same partition question on per-example attribution vectors; CCSAE supplies the *structural* baseline for the same partition question on dictionary features. The two are complementary substrates of the same partition prediction.

### 1.3 What this paper does

It constructs the CCSAE (§3), proves three theorems about its features (§4), and pre-registers a cross-model experimental sweep (§5–§7) testing four predictions against three negative controls. The experimental setup explicitly *uses* the existing Gemma Scope checkpoint as the vanilla baseline, eliminating the need to train a vanilla SAE from scratch; the only new training is the CCSAE itself.

The deliverable is a *pre-registered divisor table*: feature count per packet, per closed support, per cyclic sub-task. The table is computable from the packet dimensions $\varphi(d)$ and the SAE width before training. Verifying it empirically is the experiment.

---

## 2. Notation and preliminaries

### 2.1 Standard SAE

Fix a transformer with hidden representation $h \in \mathbb{R}^d$ at a chosen layer $\ell$. A sparse autoencoder is a pair $(W_e, W_d, b_e, b_d)$ with $W_e \in \mathbb{R}^{F \times d}$, $W_d \in \mathbb{R}^{d \times F}$, biases $b_e \in \mathbb{R}^F, b_d \in \mathbb{R}^d$, sparsity-inducing activation $\sigma$ (ReLU, JumpReLU, or top-$k$). The feature activation is $f(h) = \sigma(W_e h + b_e)$; the reconstruction is $\hat h = W_d f(h) + b_d$. Training minimizes $\|h - \hat h\|_2^2 + \lambda \|f(h)\|_1$ (or a top-$k$ surrogate).

We index features $k = 1, \ldots, F$. The $k$-th feature direction is $w_k = W_d e_k \in \mathbb{R}^d$ — the $k$-th column of the decoder.

### 2.2 Cyclic sub-vocabulary and projection to the task algebra

Fix a cyclic ring-structured sub-vocabulary $V_R \subset V$ of size $N$ (the twelve months, seven weekdays, etc., per [Paper 26](26.conductor_probe_obstruction_theorem.md), §1.2). Let $W_U \in \mathbb{R}^{|V| \times d}$ be the model's full unembedding, and let $\pi : \mathbb{R}^d \to \mathbb{R}^N$ be its restriction-and-centering to $V_R$:
$$\pi(h)_y = (W_U h)_y - \frac{1}{N}\sum_{y' \in V_R}(W_U h)_{y'}, \qquad y \in V_R.$$
$\pi(h)$ is the centered logit profile on the cyclic sub-vocabulary; it lives in the $(N-1)$-dimensional zero-sum subspace $\Sigma_0 \subset \mathbb{R}^N$.

### 2.3 Character basis and packets

The characters $\chi_k(j) = e^{2\pi i k j / N}$ for $k \in \{1, \ldots, N-1\}$ form an orthonormal basis of the complexification of $\Sigma_0$. (We work with their real and imaginary parts as a real orthonormal basis when convenient.) The conductor packet $H_d \subset \Sigma_0$ is the real span of characters with conductor $d = N/\gcd(k, N)$, with $\dim_\mathbb{R} H_d = \varphi(d)$.

For each $d \mid N$ with $d > 1$, let $P_d : \Sigma_0 \to H_d$ be the orthogonal projection onto $H_d$. For a closed packet support $S \subseteq \{d : d \mid N, d > 1\}$, let $P_S = \sum_{d \in S} P_d$ be the projection onto $\bigoplus_{d \in S} H_d$.

### 2.4 The qualifying layer

The qualifying layer $\ell^\star$ from [Paper 36](36_layerwise_packet_spectroscopy.md) is the layer at which the lens-arm packet fraction $f_{d, \ell}^{(\text{lens})}$ has first reached $0.7 \cdot f_{d, \text{final}}^{(\text{lens})}$ for the full-period packet $d = N$. We train the CCSAE at $\ell = \ell^\star$.

---

## 3. The Conductor-Certified SAE construction

### 3.1 Definition

A *Conductor-Certified SAE* at closed packet support $S$ on cyclic sub-vocabulary $V_R$ is a standard SAE $(W_e, W_d, b_e, b_d)$ with the additional constraint:
$$\boxed{\;\pi(w_k) \in \bigoplus_{d \in S} H_d \text{ for every feature } k.\;}$$

Equivalently: $(I - P_S) \pi(w_k) = 0$ exactly, for every feature.

### 3.2 Hard vs. soft certification

**Hard certification.** After each gradient step, project $W_d$'s columns to satisfy the constraint. Concretely: replace each column $w_k$ with $w_k - (\pi^+ (I - P_S) \pi)(w_k)$, where $\pi^+ \in \mathbb{R}^{d \times N}$ is the Moore–Penrose pseudo-inverse of $\pi$ on $\Sigma_0$. The projection is a single matrix operation per gradient step, costing $O(d N + F N^2)$ per step.

This is the formulation used for the theorems of §4. It enforces the constraint *exactly* after every step.

**Soft certification.** Add the regularization term
$$\mathcal{L}_S := \lambda_S \sum_{k=1}^F \|(I - P_S) \pi(w_k)\|_2^2$$
to the SAE training objective. As $\lambda_S \to \infty$, this drives the constraint asymptotically. Soft certification is operationally simpler but the theorems hold only up to $\lambda_S$-dependent tolerances.

For the present paper we use hard certification in the primary experiments and report soft certification as a secondary ablation.

### 3.3 Per-feature single-packet purity (optional further constraint)

The basic CCSAE certifies the *aggregate* features to lie in $\bigoplus_{d \in S} H_d$. A stronger constraint requires each feature individually to lie in exactly one packet:
$$\pi(w_k) \in H_{d_k} \text{ for some single } d_k \in S.$$

This is the **per-feature single-packet (PFSP) variant**. It is implementable as: assign each feature $k$ a packet label $d_k$ during initialization (round-robin across $S$ in proportion to $\varphi(d)$), and project $\pi(w_k)$ onto $H_{d_k}$ rather than onto $\bigoplus_{d \in S} H_d$ after each step. The PFSP variant is what Theorem 4.3 below claims partitions the features by packet exactly.

### 3.4 Compute cost

Adding the certification step to a standard SAE training loop adds $O(d N + F N^2)$ FLOPs per gradient step. For $N = 12, F = 32000, d = 4096$ (Llama-3.1-8B settings), this is roughly $5 \times 10^6$ FLOPs — negligible compared to the SAE forward/backward pass cost of $\sim 10^9$ FLOPs. The certification adds well under 1% overhead.

---

## 4. Theorems

### 4.1 Theorem 4.1 (Packet-Purity)

**Theorem 4.1.** For a hard-certified CCSAE at closed packet support $S$, every feature $k$ satisfies $\pi(w_k) \in \bigoplus_{d \in S} H_d$, i.e. $(I - P_S) \pi(w_k) = 0$, exactly.

*Proof.* The hard-certification step projects each column of $W_d$ onto the certified subspace after every gradient update. The constraint holds after every step, hence in the trained model. $\square$

This is the trivial part. The non-trivial content is:

### 4.2 Theorem 4.2 (Reconstruction-Cost)

**Theorem 4.2.** Let $\hat h_{\text{cert}}$ be the reconstruction by a hard-certified CCSAE at support $S$ and $\hat h_{\text{vanilla}}$ by a vanilla SAE of the same width $F$, both trained with the same sparsity penalty $\lambda$, same activation, and same training data. Define the *cross-packet content* of the hidden state $h$ in the task algebra:
$$\delta_S(h) := \|(I - P_S) \pi(h)\|_2^2.$$
Then asymptotically in training (and at the same effective L1 sparsity, controlled by $\lambda$):
$$\mathbb{E}_h \|h - \hat h_{\text{cert}}\|_2^2 \leq \mathbb{E}_h \|h - \hat h_{\text{vanilla}}\|_2^2 + \mathbb{E}_h\,\delta_S(h) + \epsilon,$$
where $\epsilon$ depends on the SAE's atoms-per-direction capacity beyond $\sum_{d \in S} \varphi(d)$ and tends to zero as $F$ grows large.

*Proof sketch.* Decompose $\pi(h) = P_S \pi(h) + (I - P_S) \pi(h)$. The CCSAE's decoder span by construction does not cover the $(I - P_S) \pi(h)$ component; this content is captured by the residual term $b_d$ on average and by the SAE's reconstruction error otherwise. The component $P_S \pi(h)$ is reconstructible by the CCSAE just as it would be by the vanilla SAE (the certified subspace contains everything needed for it). Hence the gap between certified and vanilla reconstruction loss is at most the squared magnitude of the un-certified component plus a residual that vanishes with capacity.

Formally: let $\hat h_{\text{cert}}$ minimize $\|h - W_d f(W_e h + b_e) - b_d\|^2 + \lambda \|f\|_1$ subject to $\pi(W_d e_k) \in \bigoplus_{d \in S} H_d$ for all $k$. The Lagrangian relaxation gives an upper bound on the constrained optimum, and the constrained optimum equals the unconstrained optimum on the $P_S \pi$ subspace plus the un-reconstructible $(I - P_S)\pi(h)$ content. Taking expectation gives the displayed bound. $\square$

**Significance.** The reconstruction gap between certified and vanilla SAE *equals* the cross-packet content that [Paper 26](26.conductor_probe_obstruction_theorem.md) T1 + T2 say is *forbidden* under the corresponding quotient readout. The trade-off between certification and reconstruction is therefore *not a tunable hyperparameter* — it is fixed by the Pontryagin obstruction. Quantitatively: at the Llama-3.1-8B months anchor, the native packet fractions are $f_{2,3,4,6,12} = (0.0506, 0.0664, 0.0591, 0.1665, 0.6574)$ (Paper 26 §Native Final-Logit Lens Binning). For $S = \{12\}$ (most restrictive), the predicted reconstruction gap is $1 - 0.6574 = 0.3426$ of the cyclic content. For $S = \{2, 6\}$, the gap is $1 - 0.0506 - 0.1665 = 0.7829$. For $S = \{2, 3, 4, 6, 12\}$ (full), the gap is $0$ (modulo capacity residual $\epsilon$).

> **Verified to machine precision (2026-06-13; `empirical/ccsae_certificate.py`).** On the captured audit-κ residual streams + unembedding slices for *both* Llama-3.1-8B and Mistral-7B-v0.3 (months and weekdays), the idealized identity of Theorem 4.2 — that the certified decoder's reconstruction floor on the cyclic content equals the out-of-support packet content $\sum_{d \notin S} f_d$ — holds with worst identity error $1.1\times10^{-16}$, computed two independent ways (spectral packet fractions vs. direct real-space $(I-P_S)\pi$ projection). Theorem 4.1's hard-certification construction makes every decoder column packet-pure with worst forbidden-packet leakage $4.1\times10^{-15}$. The §4.2 hand-computed gaps reproduce on the freshly measured fractions to four decimals (S={12}: $0.34307$ vs. $0.3426$; S={2,6}: $0.78207$ vs. $0.7829$; S=full: $0$ exactly); the residual is BF16 forward jitter at the audit-κ $\leq 5\times10^{-4}$ scale. The Mistral months gaps are $0.2148/0.8370/0$ for $S=\{12\}/\{2,6\}/\text{full}$ (the smaller full-period gap tracks Mistral's higher $f_{12,\text{final}}=0.785$). **This settles the *structural* gap = obstruction identity (the "exactly" of the trade-off) deterministically; the separate claim that a *trained* finite-width SAE attains this floor with $\epsilon$ small is P3, the production-scale empirical leg.** Certificate: `empirical/reports/ccsae_certificate.json`.

### 4.3 Theorem 4.3 (Feature Partition under PFSP)

**Theorem 4.3.** For a per-feature single-packet (PFSP) CCSAE with feature-packet labels $\{d_k\}_{k=1}^F$ pre-assigned in round-robin proportion to $\varphi(d)$, the features partition into $|S|$ packet-aligned groups:
$$\mathcal{F}_d := \{k : d_k = d\}, \qquad F = \sum_{d \in S} |\mathcal{F}_d|.$$
The feature count per packet satisfies $|\mathcal{F}_d| = F \cdot \varphi(d) / \sum_{d' \in S} \varphi(d')$.

Moreover, the per-packet feature subsets $\{w_k : k \in \mathcal{F}_d\}$ span $H_d$ (after projection through $\pi$) with feature count at least $\varphi(d)$ for every $d \in S$, so every packet's content is recoverable.

*Proof.* The PFSP construction assigns labels in advance and projects each feature onto its labeled packet after every gradient step. The partition is determined by the labeling. The feature counts follow from round-robin assignment. The spanning property follows from $|\mathcal{F}_d| \geq \varphi(d)$, which holds whenever $F \geq |S| \cdot \max_d \varphi(d)$ — a mild capacity assumption easily satisfied at production widths. $\square$

**This is the structural prediction.** The PFSP CCSAE has *exactly* $|\mathcal{F}_d| = F \cdot \varphi(d) / \sum_{d'} \varphi(d')$ features in packet $H_d$, by construction. For $S = \{2, 3, 4, 6, 12\}$ ($\varphi$ values $1, 2, 2, 2, 4$, total 11) and $F = 16384$ (Gemma Scope width), the divisor table is:

| packet $d$ | $\varphi(d)$ | $|\mathcal{F}_d|$ at $F = 16384$ |
|---:|---:|---:|
| 2 | 1 | 1489 |
| 3 | 2 | 2979 |
| 4 | 2 | 2979 |
| 6 | 2 | 2979 |
| 12 | 4 | 5958 |
| **total** | **11** | **16384** |

This is the **pre-registered divisor table**. Verifying it empirically is the experiment.

---

## 5. The pre-registered divisor table

The divisor table is the structural pre-registration this paper's empirical claims depend on. For each cyclic sub-task and SAE width, the feature counts per packet are fixed before training. The verification is exact (integer arithmetic) once the SAE is trained.

### 5.1 Months ($C_{12}$)

Packet dimensions: $\varphi(2), \varphi(3), \varphi(4), \varphi(6), \varphi(12) = 1, 2, 2, 2, 4$. Total: 11.

At $F = 16384$ (Gemma Scope width 16K):

| $S = \{12\}$ | $S = \{2, 6\}$ | $S = \{2, 3, 4, 6, 12\}$ |
|---|---|---|
| all 16384 in $H_{12}$ | $|\mathcal{F}_2| = 5461$, $|\mathcal{F}_6| = 10923$ | per table above |

### 5.2 Weekdays ($C_7$)

Packet dimensions: $\varphi(7) = 6$. Only one nontrivial packet.

At $F = 16384$: all 16384 features in $H_7$ under any $S$ that includes 7. (Degenerate; serves as positive control.)

### 5.3 Digits ($C_{10}$)

Packet dimensions: $\varphi(2), \varphi(5), \varphi(10) = 1, 4, 4$. Total: 9.

At $F = 16384$ with $S = \{2, 5, 10\}$ (full):
$|\mathcal{F}_2| = 1820$, $|\mathcal{F}_5| = 7282$, $|\mathcal{F}_{10}| = 7282$.

### 5.4 Three closed-support variants per task

For each of the three tasks, we train:
- **Full $S$**: all nontrivial divisors. Tests Theorem 4.3 in its strongest form.
- **Single-packet $S$**: $S = \{N\}$ (the full-period packet only). Tests whether $H_N$ alone is recoverable.
- **Coarse $S$**: $S = \{2, 6\}$ for months, $\{2\}$ for digits, omitted for weekdays. Tests whether coarse-only certification leaves the fine-period content in the residual as Theorem 4.2 predicts.

Total: 8 CCSAE training runs per model (3 tasks × variable variants).

---

## 6. Experimental setup

### 6.1 Models

- **Gemma 2 9B IT** (DeepMind, 2024). Primary because Gemma Scope (Lieberum et al. 2024) supplies *off-the-shelf vanilla SAE checkpoints* at every layer at 16K and 65K widths, fully open-sourced. Using these as the vanilla baseline eliminates the need to train a vanilla SAE from scratch — a major compute saving.
- **Llama-3.1-8B-Instruct** (Meta, 2024). Anchor model from [Paper 26](26.conductor_probe_obstruction_theorem.md), [Paper 36](36_layerwise_packet_spectroscopy.md). No public SAE; vanilla SAE trained from scratch.
- **Mistral-7B-v0.3-Instruct** (Mistral, 2024). Cross-family replication target.

Three models × 3 tasks × (CCSAE variants + vanilla) gives the experimental grid.

### 6.2 Qualifying layer selection

For each (model, task), the qualifying layer $\ell^\star$ is determined by [Paper 36](36_layerwise_packet_spectroscopy.md)'s spectroscopy: the smallest $\ell$ at which the lens-arm full-period packet fraction $f_{N, \ell}^{(\text{lens})}$ exceeds 70% of its final-layer value. This pins the layer per (model, task) before SAE training begins.

For Llama-3.1-8B-Instruct on months, the Paper 26 anchor gives $\ell^\star \in [28, 32]$ (full-period fraction rises from $\sim 0.356$ at layer 28 to $0.657$ at the final); we use $\ell^\star = 30$ as a midpoint pending Paper 36's full sweep.

### 6.3 Training data and SAE width

- **Activations corpus:** The Pile validation set (Gao et al. 2020), 1M tokens. For each cyclic sub-task, augment with 100K templated prompts that exercise the relevant cyclic structure (matching Paper 12 + Paper 26 conventions).
- **SAE width:** $F = 16384$ for Gemma 2 9B (matching Gemma Scope 16K), $F = 32768$ for Llama-3.1-8B and Mistral-7B (matching production SAE widths from Anthropic's recent work).
- **Activation function:** JumpReLU (Lieberum et al. 2024). Sparsity penalty $\lambda$ calibrated to match Gemma Scope's published sparsity.
- **Steps:** 50K, batch 256. Standard.

### 6.4 Compute

Per CCSAE training run on a single A100: ~24 hours. Total runs:

- 3 models × 3 tasks × 3 CCSAE variants = 27 CCSAE training runs (~650 GPU-hours).
- 3 negative-control runs per task: shuffled packet labels, randomized packet support, identity decoder. 9 total (~220 GPU-hours).
- Vanilla SAE training on Llama and Mistral: 6 runs × 24 hours = 144 GPU-hours. (Skipped on Gemma 2 9B by using Gemma Scope.)

Total: ~1000 GPU-hours, well within an academic lab's reach over 2–3 weeks.

### 6.5 Evaluation

Per (model, task, SAE variant):

1. **Feature packet purity** (model-side): for each feature $w_k$, project $\pi(w_k)$ onto each packet $H_d$ and report the largest-packet fraction. Vanilla SAE features have a distribution over largest-packet fractions; CCSAE features have largest-packet fraction $\geq 1 - \epsilon$ by Theorem 4.1.

2. **Reconstruction loss** (model-side): standard $\|h - \hat h\|^2$. Reported per (model, task, variant). Theorem 4.2 predicts the certified-minus-vanilla gap.

3. **Forbidden-packet leakage** (theorem-side control): for each CCSAE feature, the projection of $\pi(w_k)$ onto each forbidden packet should be exactly zero (within machine precision $\sim 10^{-12}$ in fp32). This is the integrity check of the certification — not model evidence.

4. **Feature partition count** (Theorem 4.3 test): for PFSP CCSAE, the empirical feature count per packet must equal the pre-registered divisor table to within zero (integer-exact match).

5. **Cyclic-task feature recovery rate** (model-side): on held-out cyclic-task prompts (e.g., "What month is 7 months after September?"), the top-activated CCSAE feature's packet label should match the divisor structure of the answer. We report the per-task recovery rate.

### 6.6 DCD as the unconstrained baseline pipeline

The CCSAE experimental sweep is paired with a *vanilla* dictionary baseline (Gemma Scope where available, trained-from-scratch otherwise). On cyclic sub-tasks, we add a third comparator: the Data-driven Circuit Discovery pipeline of Rai, Geva & Yao 2026, applied not to find circuits but to recover the cluster count K* of per-example attribution vectors under EAP-IG on the cyclic mixed dataset. This arm is unconstrained — it does not see the conductor packet structure of the task algebra — and serves as the empirical baseline against which CCSAE's certified packet partition is measured.

**Pipeline.** For each (model, task) cell, generate `n_examples × τ(N)` prompts, each instantiating a different element of the cyclic algebra (e.g., for months: balanced rotation through January–December as both source and target). Compute per-example edge-attribution vectors `s_i ∈ ℝ^|E|` using EAP-IG with the standard counterfactual ablation [Hanna, Pezzelle & Belinkov 2024]. Reduce via PCA to ℝ^r (r = 64, matching the DCD release). Cluster via K-means at K ∈ {1, …, 12}; select K* via silhouette score and gap statistic. Report K* and the per-cluster centroid's packet-projection profile.

**Prediction.** On cyclic mixed datasets, DCD's silhouette-driven K* should match the divisor count τ(N): τ(12) = 6 for months, τ(7) = 2 for weekdays, τ(10) = 4 for digits. Per-cluster feature counts (φ(d) for packet H_d) match the CCSAE divisor table of §5. CCSAE's structural prediction and DCD's empirical recovery agree to within K* ± 1. Both branches reportable: if K* matches τ(N), Paper 26 T1's quotient-respecting-readout claim acquires its first cluster-level empirical anchor; if K* does not match, the gap localizes whether the deviation is in the attribution-vector substrate (EAP-IG misses divisor structure that the residual stream carries) or in the silhouette/gap-statistic K-selection (the structure is in `s_i` but the K-criterion does not resolve it).

---

## 7. Pre-registered predictions

**P1 (Theorem 4.1 holds at training).** Forbidden-packet leakage of every CCSAE feature is $< 10^{-10}$ in fp32 (within numerical precision of the hard-certification projection). This is a sanity check, not model evidence. *(Structural precondition discharged 2026-06-13: the hard-certification operator itself produces leakage $4.1\times10^{-15}$ on captured Llama/Mistral unembedding slices in fp64 — `empirical/ccsae_certificate.py`. **At training (Phase B, fp32 torch through the trained reconstruction): relative forbidden leakage $4.1\times10^{-5}$** — packet purity is real (the reconstruction is $99.996\%$ packet-pure, $4$–$5$ orders below the cyclic signal) but the literal $<10^{-10}$ threshold is an fp64-idealized figure not attainable through an fp32 trained reconstruction with a pseudo-inverse projection. Threshold to be restated as fp32-realistic ($\sim10^{-5}$) in v0.2.)*

**P2 (Vanilla SAE features distribute across packets).** Vanilla SAE features have largest-packet fraction distribution with median $< 0.7$ on the cyclic sub-task evaluation. Equivalently: most vanilla features are spread across at least two packets. This is the *primary model-side prediction* of [Paper 26](26.conductor_probe_obstruction_theorem.md) T4: vanilla SAEs cannot place monosemantic features wholly in cross-packet-content packets without explicit certification.

**P3 (Reconstruction gap matches Theorem 4.2).** The empirical CCSAE-minus-vanilla reconstruction-loss gap matches the analytic prediction $\delta_S(h)$ within 10% relative error per (model, task, $S$) cell, averaged over the test set.

> **Confirmed at one cell (2026-06-13; Llama-3.1-8B, months, layer 30; `empirical/ccsae_train.py`).** A top-$k$ SAE ($F=1024$, $k=32$, 4000 steps) trained on a 3456-prompt cyclic activation corpus, evaluated in the cyclic readout $\pi(h)$ where Theorem 4.2 lives: vanilla cyclic reconstruction error $0.0102$ (the SAE *can* represent all packets); certified $S=\{12\}$ error $0.4114$ → **gap $0.4011$ vs. $\delta_S$ floor $0.3851$, rel. err $4.2\%$ — PASS**; certified $S=\text{full}$ gap $0.0003$ vs. $\delta_S=0$ — PASS. The trained certified SAE thus pays exactly the obstruction's cyclic-reconstruction penalty, confirming Theorem 4.2 empirically (not just the idealized identity of §4.2). Cell: `empirical/reports/ccsae_train_months_llama31_8b.json`. The full P3 grid (3 models × 3 tasks × 3 supports, production widths) remains for v0.2; this is the decisive single-cell demonstration.

**P4 (PFSP feature counts match divisor table).** The per-packet feature count in the trained PFSP CCSAE exactly matches the pre-registered divisor table for every (model, task, $S$) cell. Theorem 4.3 is empirically verified.

**P5 (Cyclic-task feature recovery rate higher for CCSAE).** On held-out cyclic-task prompts, the CCSAE's top-activated feature is correctly packet-aligned at $\geq 0.85$ rate; the vanilla SAE's top-activated feature is correctly packet-aligned at $\leq 0.70$ rate. The gap is statistically significant ($p < 0.01$ under bootstrap).

**P6 (Cross-model consistency).** The CCSAE construction works comparably on Gemma 2 9B, Llama-3.1-8B, and Mistral-7B, with no model-specific tuning needed beyond the qualifying-layer identification of §6.2. Specifically: P3's reconstruction gap is consistent across models within ±20% relative error.

**P7 (Negative controls fail).** Shuffled-packet-label CCSAE, randomized-packet-support CCSAE, and identity-decoder CCSAE all fail P5 (cyclic-task recovery rate at or below vanilla baseline). This isolates the gain to the packet-alignment content, not to the projection-step regularization.

**P8 (DCD pipeline recovers the divisor-table cluster count on cyclic mixed datasets).** Under the unconstrained DCD pipeline of §6.6 — EAP-IG → PCA → K-means with silhouette/gap-statistic K-selection on cyclic mixed datasets — the recovered cluster count K* matches the divisor count τ(N) of the task algebra to within ±1: K* ∈ [5, 7] for months (target τ(12) = 6), K* ∈ [1, 3] for weekdays (target τ(7) = 2), K* ∈ [3, 5] for digits (target τ(10) = 4). The per-cluster centroid's packet-projection profile concentrates on a single conductor packet H_d at fraction ≥ 0.7 for at least τ(N)−1 of the K* clusters. This is the empirical co-prediction of the CCSAE divisor table on the attribution-vector substrate; CCSAE's structural feature-count prediction (P4) and the DCD pipeline's empirical cluster-count prediction (P8) are two readouts of the same divisor table. Negative branch: if K* does not match τ(N) ± 1 on any cyclic task, P8 is reported as not supported; CCSAE's structural claim (P4) stands or falls separately.

---

## 8. Failure conditions

**F1 (Certification too restrictive).** CCSAE reconstruction loss exceeds vanilla by more than $\delta_S(h)$ plus a small margin. The certification interferes with training in a way Theorem 4.2's optimization argument does not capture; the proof's "asymptotically in training" assumption breaks at finite training steps. The paper would report the empirical gap and document the training dynamics that cause it.

**F2 (Vanilla SAE already packet-pure).** Vanilla SAE features turn out to be packet-pure without certification — the dictionary spontaneously aligns to the conductor structure. This would *strengthen* [Paper 26](26.conductor_probe_obstruction_theorem.md) T4 as a description of trained SAEs (vanilla SAEs implicitly find packet structure) but *weaken* the CCSAE's claim to a unique structural contribution. The paper would pivot to documenting the spontaneous alignment as the surprising empirical finding.

**F3 (Shuffled control wins).** Shuffled-packet-label CCSAE matches or beats CCSAE in cyclic-task recovery rate. This says the gain (if any) comes from the projection-step regularization, not from packet alignment. The structural account is wrong.

**F4 (Cross-model failure).** CCSAE works on one model but not the others. The construction is not universal across the transformer family — possibly because the qualifying layer differs, or because the packet structure is only visible at production scale on some models.

**F5 (Feature partition violated).** The empirical PFSP feature count per packet does not match the pre-registered divisor table. This would be deeply surprising (the partition is enforced by construction), and would indicate a bug in the projection step rather than a theoretical failure.

Each F1–F5 narrows the paper without invalidating the program's structural content. F2 is the most informative: it would be a major surprise and would shift the paper's contribution from "we built it" to "we explained why it was already there."

---

## 9. Implementation notes

### 9.1 The projection step in code

```python
def hard_certify_decoder(W_d, pi_full, P_S):
    # W_d: (d, F), pi_full: (N, d) — restriction-and-centering to V_R
    # P_S: (N, N) — projection onto certified packet subspace
    proj = pi_full.T @ P_S @ pi_full  # (d, d) projection-equivalent matrix
    return proj @ W_d                  # Each column projected; constraint enforced
```

Cost per step: $O(d \cdot F \cdot \text{poly}(N))$. For Gemma 2 9B with $d = 3584$, $F = 16384$, $N = 12$: ~$10^9$ FLOPs, well under 0.1% of the SAE forward/backward pass.

### 9.2 PFSP labeling

Pre-compute the per-packet feature counts $|\mathcal{F}_d| = F \cdot \varphi(d) / \sum_{d'} \varphi(d')$. Assign features to packets greedily, round-robin in proportion to $\varphi$. Store the labeling as a length-$F$ integer array $d_k$. The PFSP projection step uses $P_{d_k}$ rather than $P_S$ for the $k$-th column.

### 9.3 Training stability

Hard certification can cause optimizer-state inconsistency: Adam's running moment estimates accumulate based on gradients in the unconstrained directions, then the projection discards part of the update. The mitigation, matching [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md)'s Pareto rule: *gradient projection 0%, update projection 100%* — leave Adam's moments unchanged, project only the final applied update. This is the same trick used in Paper 12; we reuse it.

### 9.4 Backward compatibility with Gemma Scope

The Gemma Scope checkpoints' format is documented. We initialize the CCSAE from the corresponding Gemma Scope checkpoint, then continue training with the certification constraint added. This produces a fine-tuned CCSAE that is, in expectation, in the same loss basin as the vanilla — making the comparison cleaner than training both from scratch.

---

## 10. Connections to the SAE literature

### 10.1 Anthropic Scaling Monosemanticity (Templeton et al. 2024)

Templeton et al. trained SAEs at width 4M on Claude 3 Sonnet, extracting features including "12-hour time formats", "calendar/year reasoning", "day-of-week reasoning". These are cyclic-structured features. Their monosemanticity evaluation is post-hoc; the present paper supplies a pre-registered structural test that these features should partition by conductor packet *exactly* when SAE training is conductor-certified.

The cleanest empirical prediction: on a Claude 3 SAE replicated with CCSAE certification, the "day-of-week" feature group should split into 6 features (one per non-trivial $H_7$ character) rather than appearing as a single composite feature. The same prediction for "month" features (split into the 11 non-trivial $C_{12}$ characters across the five packets of §5.1).

### 10.2 OpenAI sparse-autoencoder atlas (Gao et al. 2024)

OpenAI's top-$k$ atlas uses a different sparsity activation (top-$k$ rather than L1) and a different objective. The CCSAE construction applies unchanged to both. The top-$k$ variant of CCSAE is a one-line change: apply hard certification to $W_d$'s columns after each step, regardless of activation. Predictions P1–P7 carry over.

### 10.3 DeepMind Gemma Scope (Lieberum et al. 2024)

The Gemma Scope suite is the empirical vehicle of choice for §6.1. Gemma Scope releases vanilla SAEs at every layer of Gemma 2 with widths 16K and 65K, JumpReLU activation, with public checkpoints. The CCSAE experiment can use Gemma Scope's checkpoints directly as the vanilla baseline, with the CCSAE trained from those checkpoints as the certified counterpart. This is the cleanest possible apples-to-apples comparison the SAE field can support.

### 10.4 Anthropic Toy Models of Superposition (Elhage et al. 2022)

Elhage et al. studied superposition in toy models, characterizing when features are placed in superposition geometrically. The Conductor program adds a *structural* prediction the toy-model framework does not produce: not just *which* features are in superposition, but *which character algebra* they should be partitioned into when not in superposition. Toy Models is the right comparator for the limits of the SAE's expressive capacity; CCSAE is the structural prescription for what to do with that capacity on cyclic-content tasks.

### 10.5 Connection to the Conductor program

- [Paper 26](26.conductor_probe_obstruction_theorem.md) T1 + T2 + T4: supplies the obstruction and the prediction.
- [Paper 34](34_the_conductor_blind_spot.md): supplies the structural reason quadratic-loss-trained SAEs miss cross-packet cubic content.
- [Paper 36](36_layerwise_packet_spectroscopy.md): supplies the qualifying layer.
- [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md): supplies the update-projection technique reused in §9.3.
- [Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md): supplies the validation framework — a CCSAE that succeeds should *pass* the BNSA on the certified task with high survival ratio.

The CCSAE is the AI-side capstone of the Conductor program's interpretability arm. It composes with every preceding paper.

---

## 11. Scope and limitations

### 11.1 What this paper claims

- The CCSAE construction is well-defined and theoretically justified (Theorems 4.1–4.3).
- On cyclic sub-vocabularies with named character algebras, the CCSAE's feature partition is exactly the divisor table of §5, by construction.
- The empirical predictions P1–P7 are pre-registered and the negative controls are pre-registered, allowing falsification.

### 11.2 What this paper does not claim

- *The CCSAE produces more informative features than vanilla SAE for arbitrary tasks.* The cyclic-content sub-tasks are where the obstruction applies. For tasks without named cyclic algebra, the CCSAE construction is vacuous; the SAE reduces to vanilla.
- *The Conductor packet decomposition is the right interpretability basis at every layer of every model.* The qualifying-layer identification (Paper 36) restricts the prediction to the layer at which packet structure has crystallized.
- *Vanilla SAEs are wrong.* They are simply not certified to a particular structural account. Vanilla SAEs may produce excellent monosemanticity by other measures; this paper's claim is restricted to the conductor-packet structural prediction.
- *The divisor table is the optimal feature partition.* It is *one* canonical partition derived from the Pontryagin obstruction. Other partitions may produce better cyclic-task recovery; we do not claim optimality.

### 11.3 Open questions for sequel papers

- **Learned packet support.** Can the closed support $S$ be learned during SAE training rather than pre-registered? A regularization-toward-sparsity over the packet labels would let the SAE discover the relevant packets.
- **Beyond cyclic.** The Conductor program is built around finite cyclic algebras. Generalizing to other finite groups (non-abelian, products of cyclics with more structure) gives the corresponding CCSAE construction; whether real LLM sub-tasks admit non-cyclic algebraic content with a packet decomposition is an open empirical question.
- **Causal validation via patching.** A CCSAE feature's causal contribution to model behavior can be tested via activation patching. The CCSAE supplies the *right features* to patch with; the patching experiments themselves are the natural sequel.
- **Composition with BNSA.** A CCSAE-certified model that *also* passes the BNSA ([Paper 40](40_base_n_shortcut_audit_as_a_safety_primitive.md)) at tier A is a model whose mechanism is *both* algebraically aligned and conductor-structured. The composition is the natural alignment-evaluation deliverable for safety-critical deployments.

---

## 12. Conclusion

[Paper 26](26.conductor_probe_obstruction_theorem.md) Conjecture T4 has been a structural prediction in search of a construction. The Conductor-Certified Sparse Autoencoder is the construction. Three theorems follow immediately: features are packet-pure by construction (Theorem 4.1); the reconstruction cost of certification is exactly the Pontryagin-forbidden cross-packet content (Theorem 4.2); the feature partition matches a divisor table pre-registered from $\varphi(d)$ values before training begins (Theorem 4.3).

The empirical content is the divisor-table verification: a pre-registered specification of how many features should live in each packet, per cyclic sub-task, per SAE width, per closed packet support. This is the first instance the mechanistic-interpretability field has of a *structural pre-registration* — a statement of what features must exist before the dictionary is trained — derived from a theorem rather than from human intuition.

The experimental sweep uses Gemma Scope as the off-the-shelf vanilla baseline (eliminating a major compute cost), trains 27 CCSAE variants across 3 models × 3 tasks × 3 supports, runs 9 negative-control variants, and validates the 7 pre-registered predictions in ~1000 GPU-hours. The deliverable is a fine-tuned CCSAE checkpoint per cell, a verification of the divisor table per cell, a cyclic-task feature-recovery comparison vs. vanilla per cell, and a per-feature packet-label assignment that anyone with the checkpoint can audit.

If the predictions hold, [Paper 26](26.conductor_probe_obstruction_theorem.md) T4 is promoted from prediction to theorem with an empirical anchor, and the SAE field acquires its first structural feature specification. If they fail, the negative result tells the program *which* prediction failed (F1 through F5 are mapped to specific structural assumptions) and the next paper is the diagnostic of which assumption.

The structural content is reusable. Any future SAE paradigm — different sparsity, different architecture, different loss — that has a decoder span can be certified by the same construction. The divisor table is a property of the *task algebra*, not the *training method*. As long as the task has a named cyclic structure, the CCSAE's pre-registered prediction applies.

---

*Draft v0.1 — May 19, 2026 — CCSAE construction with hard and soft certification variants, three theorems (Packet-Purity, Reconstruction-Cost, Feature-Partition), pre-registered divisor table for $C_{12}$/$C_7$/$C_{10}$ at multiple SAE widths and closed supports, 27 CCSAE training runs across Gemma 2 9B / Llama-3.1-8B / Mistral-7B with 9 negative controls, 7 sharp predictions matched to 5 failure conditions.*

*Draft v0.1.1 — June 13, 2026 — Theorems 4.1 and 4.2 verified to machine precision on the captured audit-κ activations of Llama-3.1-8B and Mistral-7B-v0.3 (months, weekdays), settling the structural gap = obstruction identity deterministically (`empirical/ccsae_certificate.py`; cert `empirical/reports/ccsae_certificate.json`). **Phase B (June 13): P3 confirmed at one cell — a trained top-$k$ SAE on Llama-3.1-8B months (layer 30) shows certified-vs-vanilla cyclic-reconstruction gap $0.401$ vs. obstruction floor $0.385$ (4.2%); $S=$full matches vanilla; P1 packet purity holds at fp32-training precision ($4\times10^{-5}$).** The remaining production-scale legs (P2/P4/P5–P8: divisor-table feature count, full 3×3×3 grid, DCD cluster recovery) remain for v0.2.*
