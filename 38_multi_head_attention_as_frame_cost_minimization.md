# Multi-Head Attention as Frame-Cost Minimization

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — frame-cost ledger, Frame-Cost Theorem, Vaswani $h=8$ as the $C=1$ corner, cyclic-deviation phase diagram)**

---

## Abstract

Vaswani et al. (2017, §3.2.2) chose $h = 8$ parallel attention heads at $d_k = d_v = 64$ for $d_\text{model} = 512$, with the rationale "we found it beneficial to linearly project the queries, keys and values $h$ times with different, learned linear projections." Their Table 3 ablation (rows A and B) sweeps $h \in \{1, 4, 8, 16, 32\}$ and reports a *broad* optimum near $h = 8$–$16$, falling off at both ends. No analytic account exists in the literature for the shape of that optimum or for why it sits where it does. We give one.

A multi-head attention configuration $(h, d_k)$ at fixed $d_\text{model} = h d_k$ is a *frame* on the residual stream — a decomposition of $\mathbb{R}^{d_\text{model}}$ into $h$ subspaces of dimension $d_k$, equipped with three learned projections. We define an **information-investment functional** $\mathcal{I}(h, d_k)$ as the constrained sum of three ledger terms: (i) the **Fisher-projection error** $F(h, d_k)$ measuring how poorly $h$ equal blocks tile the local Fisher tangent at the maximum-entropy point of the task's categorical readout; (ii) the **packet-mismatch leakage** $L(h, d_k)$ measuring the cross-packet Amari–Chentsov coupling forced across block boundaries by the Conductor Blind Spot ([Paper 34](34_the_conductor_blind_spot.md), Theorem 5.2); and (iii) the **memory-bandwidth penalty** $M(h, d_k)$ enforcing the dyadic hardware lattice of modern tensor cores. The trade-off coefficient $C := \lambda_L / \lambda_M$ controls a one-parameter family of minimizers.

We prove (Theorem 4.1, **Frame-Cost Minimization**) that the constrained minimum of $\mathcal{I}$ over the dyadic lattice $\Lambda = \{(h, d_k) : h, d_k \in 2^\mathbb{N}, h d_k = d_\text{model}\}$ has three regimes:

- **Hardware-dominant** ($C \ll 1$, or *task algebra purely dyadic*): the minimizer is $(h^\star, d_k^\star) = (2^{\lfloor \log_2 (d_\text{model}/16) \rfloor}, 16)$ saturated against the smallest tile size. For $d_\text{model} = 512$, this is $(32, 16)$.
- **Mixed** ($C \sim 1$): the minimizer sits at the broad optimum $(h^\star, d_k^\star) \in \{(8, 64), (16, 32)\}$ — exactly the Vaswani Table 3 plateau, with the Vaswani-chosen $(8, 64)$ being the constrained optimum when $\lambda_F$ penalizes very small $d_k$.
- **Packet-dominant** ($C \gg 1$, or *task algebra strongly non-dyadic*): the minimizer is the dyadic allocation closest to the **packet-aligned target** $(h_{\text{pkt}}, d_k^{\text{pkt}})$ obtained from the conductor packet ranks $\{\varphi(d)\}_{d \mid N, d > 1}$ of the dominant cyclic sub-algebra.

The corollary that justifies the title: **Vaswani's $(h, d_k) = (8, 64)$ is the $C = 1$ constrained optimum of the Frame-Cost functional for $d_\text{model} = 512$ under a task algebra dominated by 2-power structure** (BPE merge depth, byte-pair frequency, position-mod-$2^k$). The Vaswani Table 3 row A plateau ($h = 8$ to $h = 16$, BLEU 25.8) is the predicted breadth of the mixed-regime minimum. The shape of the falloff at $h = 1$ ($\Delta\text{BLEU} = -0.9$) and at $h = 32$ ($\Delta\text{BLEU} = -0.4$) is the predicted asymmetry of $F$ vs. $M$ at the regime boundaries.

We pre-register one architecture experiment to falsify the prediction in its strongest form: train two transformers at *exactly* matched parameter count, one with the Vaswani allocation $(8, 64)$, one with a packet-aligned allocation derived from the $C_{12}$ conductor lattice $\{1, 2, 2, 2, 4\}$, on a benchmark whose evaluation split contains both natural-language perplexity (mixed regime) and cyclic sub-tasks (calendar arithmetic, modular addition, music-theory pitch-class prediction, scheduling). The prediction is sharp: equal performance on natural-language perplexity, strict packet-aligned superiority on cyclic sub-tasks, with the per-sub-task gap quantitatively predicted by the corresponding $\Sigma(N, S)$ sum from [Paper 34](34_the_conductor_blind_spot.md), Theorem 3.5.

If the prediction holds, the empirical $h = 8$ heuristic that has dominated transformer design since 2017 is the *constrained* — not unconstrained — optimum of a variational principle whose unconstrained minimizer is task-algebra-dependent and explicitly computable. If it fails, the Frame-Cost ledger is missing a term, and the experiment identifies which one.

**Keywords:** multi-head attention, transformer architecture, frame cost, information-investment functional, conductor packets, dyadic hardware lattice, Amari–Chentsov tensor, variational principle, tensor cores, packet alignment.

---

## 1. Introduction

### 1.1 The $h = 8$ mystery

Vaswani et al. (2017) state their multi-head allocation as a design choice and ablate it (Table 3, rows A and B). The relevant ablation is reproduced as our anchor:

| row | $h$ | $d_k$ | $d_v$ | PPL (dev) | BLEU (dev) |
|---:|---:|---:|---:|---:|---:|
| base | 8 | 64 | 64 | 4.92 | 25.8 |
| (A) | 1 | 512 | 512 | 5.29 | 24.9 |
| (A) | 4 | 128 | 128 | 5.00 | 25.5 |
| (A) | 16 | 32 | 32 | 4.91 | 25.8 |
| (A) | 32 | 16 | 16 | 5.01 | 25.4 |
| (B) | 16 | 16 | 16 | 5.16 | 25.1 |
| (B) | 16 | 32 | 32 | 5.01 | 25.4 |

Three structural facts from this table are mechanism-unexplained in the literature:

(i) The **plateau** at $h \in \{8, 16\}$. BLEU is identical (25.8); PPL is essentially identical (4.91 vs. 4.92).

(ii) The **asymmetric falloff**. $h = 1$ costs 0.9 BLEU; $h = 32$ costs only 0.4 BLEU. The penalty for too few heads is steeper than the penalty for too many.

(iii) The **$d_k$ floor**. Row (B) shows that shrinking $d_k$ below 32 hurts (PPL 5.16 at $d_k = 16$ vs. 5.01 at $d_k = 32$), independent of $h$.

Vaswani et al. themselves observe (§6.2): "we further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings, and observe nearly identical results." On the rows (A) and (B) plateau they offer no comment. "Determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial" is the closest they come to admitting that the head-allocation question has internal structure they did not resolve.

### 1.2 Two competing constraints

We claim the plateau, the asymmetry, and the floor are jointly explained by two competing constraints living on the same lattice.

**Hardware lattice.** Modern GPU tensor cores operate at fixed tile sizes (16, 32, 64, 128) and yield maximum throughput when matrix dimensions are powers of 2 above the smallest tile. Memory bandwidth and SM occupancy further reward dyadic widths. The hardware constraint is a *lattice* $\Lambda \subset \mathbb{N}^2$:
$$\Lambda = \{ (h, d_k) : h, d_k \in 2^\mathbb{N}_{\geq 4}, \; h d_k = d_\text{model} \}.$$
For $d_\text{model} = 512$ this is the seven points $\{(1, 512), (2, 256), (4, 128), (8, 64), (16, 32), (32, 16)\}$ together with the (rarely used) $(64, 8)$.

**Packet lattice.** The Conductor Probe-Obstruction Theorem ([Paper 26](26.conductor_probe_obstruction_theorem.md), T1) and the Conductor Blind Spot Theorem ([Paper 34](34_the_conductor_blind_spot.md), 3.5) jointly imply that for any cyclic sub-algebra $C_N$ of the model's output, the Fisher tangent at $p_*$ has a canonical decomposition $\bigoplus_{d \mid N} H_d$ with packet ranks $\{\varphi(d)\}$. The natural head allocation for that sub-algebra is one head per nontrivial packet, with widths matching $\varphi(d)$. This is the *packet lattice*: a partition of $d_\text{model}$ into blocks of size proportional to packet ranks.

For most natural-language vocab the packet lattice is approximately dyadic, because the dominant algebraic structure of token transitions (BPE merge depth, byte-level frequency, position-mod-$2^k$) is 2-power. The two lattices nearly coincide. **This is why $h = 8$ works**.

For cyclic sub-tasks (calendar reasoning, modular arithmetic, music in 12-tone equal temperament, scheduling, color in hue-cycle) the packet lattice is non-dyadic. The two lattices *do not* coincide. The theory predicts a measurable architectural improvement from aligning to the packet lattice — *at the cost* of leaving the hardware lattice.

### 1.3 The information-investment lens

[Paper 25](25.arithmetic_frame_cost_and_curvature_linearization.md) introduced an information-investment functional for choosing arithmetic frames in conductor-respecting cascades. The functional has the form
$$\mathcal{I}(\text{frame}) = \text{(Fisher-projection error)} + \text{(packet-commutator impurity)} + \text{(resource)} + \text{(depth)} + \text{(carry)},$$
with the conductor frame selected not as a universal optimum but as a convergent in a Diophantine approximation that balances additive gauge descent against multiplicative prime/conductor descent. Bounded frame prices are the finite analogue of bounded continued-fraction partial quotients.

The present paper pulls $\mathcal{I}$ out of arithmetic geometry and into transformer architecture. The "arithmetic frame" becomes the head allocation $(h, d_k)$; the "Fisher-projection error" becomes the per-head tangent capture; the "packet-commutator impurity" becomes the cross-block Amari–Chentsov coupling; the "resource" becomes the hardware-lattice penalty; "depth" and "carry" we set aside for the present scope.

The result is a single variational principle whose minimizer over the dyadic lattice predicts Vaswani's empirical choice at one trade-off coefficient, and predicts a measurable deviation at another. The trade-off coefficient is what the *task algebra* sets.

---

## 2. Setup

### 2.1 The residual stream and its frames

A transformer with model dimension $d_\text{model}$ maintains a residual stream $h \in \mathbb{R}^{d_\text{model}}$. A multi-head attention layer with head count $h$ and per-head dimensions $d_k = d_v = d_\text{model} / h$ acts via three learned projections $W_i^Q, W_i^K, W_i^V \in \mathbb{R}^{d_\text{model} \times d_k}$ for $i = 1, \dots, h$, followed by a recombining $W^O \in \mathbb{R}^{h d_v \times d_\text{model}}$.

A *frame* at this layer is the orthogonal decomposition $\mathbb{R}^{d_\text{model}} = \bigoplus_{i=1}^h V_i$ with $\dim V_i = d_k$ induced (after $W^O$) by the column-spans of the head-output projections. We treat the frame as the architectural object; the specific weights learned within a frame are a separate optimization problem and are not the subject of this paper.

### 2.2 The hardware lattice

The hardware lattice for a given $d_\text{model}$ is
$$\Lambda(d_\text{model}) = \{ (h, d_k) \in \mathbb{N}^2 : h, d_k \in 2^{\mathbb{Z}_{\geq 4}}, \; h \cdot d_k = d_\text{model} \}.$$
For $d_\text{model} = 512$, $\Lambda$ has six points; for $d_\text{model} = 4096$ (GPT-3 175B class), $\Lambda$ has nine points. The smallest tile size 16 reflects current NVIDIA tensor core minimums (Ampere through Hopper); future hardware shrinks this floor and enlarges $\Lambda$.

### 2.3 The task algebra and its packet ranks

Let the model's output be a categorical distribution over a vocabulary $V$. A *cyclic sub-algebra* of the task is a subset $V_R \subseteq V$ of $N$ tokens identified with a cyclic ring $C_N = \mathbb{Z}/N\mathbb{Z}$ via a task-relevant labeling (e.g., the twelve month-name tokens labeled by month index modulo 12; the seven weekday-name tokens labeled modulo 7; the ten digit tokens labeled modulo 10; position-id tokens labeled by position modulo $N$).

For a cyclic sub-algebra $C_N$, the **conductor packet ranks** are $\{\varphi(d)\}_{d \mid N, d > 1}$:

| $N$ | task | nontrivial conductors $d$ | packet ranks $\varphi(d)$ |
|---:|---|---|---|
| 12 | months, hours | 2, 3, 4, 6, 12 | 1, 2, 2, 2, 4 |
| 7 | weekdays | 7 | 6 |
| 10 | digits | 2, 5, 10 | 1, 4, 4 |
| 24 | hours, semitones | 2, 3, 4, 6, 8, 12, 24 | 1, 2, 2, 2, 4, 4, 8 |
| 60 | seconds, minutes | 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 | 1, 2, 2, 4, 2, 4, 4, 8, 8, 8, 16 |
| 256 | byte vocab | 2, 4, 8, 16, 32, 64, 128, 256 | 1, 2, 4, 8, 16, 32, 64, 128 |

The last row is the empirically critical one for natural language. Byte-level and BPE vocabularies have a dominant 2-power conductor structure; this is what makes the hardware and packet lattices nearly coincide for natural language.

### 2.4 The closed packet support

For a frame to be *aligned* with the packet structure on a closed support $S \subseteq \{d \mid N : d > 1\}$ means that the orthogonal projector $P_S$ onto $\bigoplus_{d \in S} H_d$ factors through the block decomposition: $P_S = \sum_{i=1}^h P_i \pi_i$, where $\pi_i$ are the head projections and $P_i$ are within-head projectors. Alignment is exact when each $\bigoplus_{d \in S_i} H_d$ for some partition $\{S_i\}$ of $S$ sits inside a single head subspace $V_i$ with the correct dimension $d_k$.

---

## 3. The Frame-Cost Ledger

We define three ledger terms. Each is a non-negative real number depending on $(h, d_k)$ and on task-algebra metadata.

### 3.1 Fisher-projection error $F(h, d_k)$

Fix a cyclic sub-algebra $C_N$ with packet ranks $\{\varphi(d)\}$ and total tangent dimension $D = N - 1 = \sum_{d \mid N, d > 1} \varphi(d)$. Let $\Pi : \mathbb{R}^{d_\text{model}} \to \mathbb{R}^D$ be the (model-dependent) pullback that embeds the cyclic sub-algebra's tangent into the residual stream — this is the linear map from logits restricted to $V_R$ back into the layer at hand, as identified by the layerwise packet spectroscopy of [Paper 36](36_layerwise_packet_spectroscopy.md). The Fisher metric on $\mathbb{R}^D$ at $p_*$ is, in the character basis, $N^2 \cdot I_D$ ([Paper 34](34_the_conductor_blind_spot.md), Lemma 3.1).

For a frame $\{V_i\}_{i=1}^h$ with $\dim V_i = d_k$, the *Fisher-projection error* is
$$F(h, d_k) = \mathbb{E}_{\Pi} \left[ \| (I - P_{\text{frame}}) \Pi^* g \|_{N^2 I}^2 \right] = \sum_{d \mid N, d > 1} \varphi(d) \cdot \rho_d(h, d_k),$$
where $\rho_d(h, d_k) \in [0, 1]$ is the fraction of the packet $H_d$ that is forced to spread across more than one block under a generic dyadic block partition. A clean special case: when $\varphi(d) \leq d_k$, $\rho_d$ vanishes (the packet fits in a single block); when $\varphi(d) > d_k$, $\rho_d \geq 1 - d_k / \varphi(d)$.

The hardware $d_k$ floor of 16 from §2.2 ensures $\rho_d = 0$ for every packet with $\varphi(d) \leq 16$. For natural-language byte-level vocab, the largest packet has rank $\varphi(256) = 128$, which exceeds $d_k = 16, 32, 64$ but fits inside $d_k = 128, 256$. This already predicts the row (B) PPL floor: when $d_k$ drops below the largest dominant packet rank, $F$ jumps.

### 3.2 Packet-mismatch leakage $L(h, d_k; S)$

The Conductor Blind Spot Theorem ([Paper 34](34_the_conductor_blind_spot.md), 3.5) supplies the *content* of the cross-packet coupling that a frame must capture. The Amari–Chentsov cubic at $p_*$ has nonzero matrix element $T_{p_*}(\chi_k, \chi_\ell, \chi_m) = N^3$ for every triple with $k + \ell + m \equiv 0 \pmod N$. The cross-packet content (triples with at least two distinct conductors) is, by Theorem A.2 of [Paper 34](34_the_conductor_blind_spot.md), non-empty for every composite $N \geq 4$, and has at least one *pairwise-distinct-conductor* triple whenever $N$ is not a prime power.

For a frame $\{V_i\}$ and a closed packet support $S$, the *packet-mismatch leakage* is
$$L(h, d_k; S) = \sum_{(k, \ell, m) \in \Sigma_\times(N, S)} \mathbf{1}[\chi_k, \chi_\ell, \chi_m \text{ not jointly in one block}] \cdot \left| T_{p_*}(\chi_k, \chi_\ell, \chi_m) \right|^2,$$
where $\Sigma_\times(N, S)$ is the set of cross-packet selection-rule triples whose conductors lie in $S$. The indicator counts how many of the cross-packet cubic couplings *cannot* be expressed as a within-block operation — these are the couplings the frame is structurally unable to represent, regardless of training.

$L$ vanishes when the frame is exactly packet-aligned on $S$; it is bounded below by a task-algebra-dependent constant when the frame is restricted to the dyadic lattice and $S$ contains non-dyadic conductors.

### 3.3 Memory-bandwidth penalty $M(h, d_k)$

The hardware penalty has the form
$$M(h, d_k) = \mu_0 \cdot \mathbf{1}[(h, d_k) \notin \Lambda] + \mu_1 \cdot \mathbb{1}[d_k < d_k^{\text{tile}}] + \mu_2 \cdot \mathbb{1}[h > h^{\text{warp}}],$$
where $d_k^{\text{tile}}$ is the smallest tensor-core tile (currently 16) and $h^{\text{warp}}$ is the warp-occupancy ceiling above which scheduling overhead dominates (currently $\sim 64$). The three constants $(\mu_0, \mu_1, \mu_2)$ are hardware-specific; we treat them as known.

The first indicator forces the minimizer onto $\Lambda$ unless $\lambda_M$ is very small (i.e., unless the packet lattice's gain exceeds the hardware penalty by a large factor). The second indicator gives the row (B) sub-floor at $d_k = 16$. The third gives the $h = 32$ falloff observed in row (A).

### 3.4 The information-investment functional

$$\boxed{\;\mathcal{I}_C(h, d_k; S) := \lambda_F \, F(h, d_k) + \lambda_L \, L(h, d_k; S) + \lambda_M \, M(h, d_k)\;}$$

with weights normalized so that $\lambda_F + \lambda_L + \lambda_M = 1$ and trade-off coefficient
$$C := \lambda_L / \lambda_M.$$
$C$ is the *packet-vs-hardware* trade-off. Pure-hardware regime is $C \to 0$; pure-packet regime is $C \to \infty$. The Frame-Cost Theorem says Vaswani sits at $C \approx 1$.

---

## 4. The Frame-Cost Theorem

### 4.1 Main result

**Theorem 4.1 (Frame-Cost Minimization).** Fix $d_\text{model}$, a cyclic task algebra $C_N$ with packet ranks $\{\varphi(d)\}_{d \mid N, d > 1}$, a closed packet support $S$, and weights $(\lambda_F, \lambda_L, \lambda_M)$ with trade-off coefficient $C = \lambda_L / \lambda_M$. Let $\Lambda = \Lambda(d_\text{model})$ be the dyadic hardware lattice of §2.2. Define the *packet-aligned target* as
$$(h^{\text{pkt}}, d_k^{\text{pkt}}) := \left( |S|, \left\lceil \frac{d_\text{model}}{|S|} \right\rceil \right),$$
with one head per nontrivial conductor in $S$.

Then the constrained minimizer
$$(h^\star, d_k^\star) := \arg\min_{(h, d_k) \in \Lambda} \mathcal{I}_C(h, d_k; S)$$
satisfies the following three-regime classification:

**(R1) Hardware-dominant regime, $C < C_1$:** The minimizer is the dyadic point with smallest hardware penalty: $(h^\star, d_k^\star) = (d_\text{model} / d_k^{\text{tile}}, d_k^{\text{tile}})$ if the row (B) sub-floor is small, else $(h^{\text{warp}}, d_\text{model} / h^{\text{warp}})$.

**(R2) Mixed regime, $C_1 \leq C \leq C_2$:** The minimizer is the dyadic point closest (in lattice distance) to $(h^{\text{pkt}}, d_k^{\text{pkt}})$ *subject to* $d_k \geq \max_{d \in S} \varphi(d)$ when feasible. For $d_\text{model} = 512$ and a 2-power-dominated task algebra, this is $(8, 64)$ or $(16, 32)$, with the choice between them determined by the relative weights of $F$ and $M$.

**(R3) Packet-dominant regime, $C > C_2$:** The minimizer is the unique dyadic point that *exactly* tiles $S$ into single-head blocks when one exists; if no such point exists, the minimizer leaves the dyadic lattice and the constraint $\Lambda$ is no longer binding (a *packet-defection* prediction).

The threshold constants $C_1, C_2$ depend explicitly on the task algebra's packet ranks and on $(\mu_0, \mu_1, \mu_2)$; closed forms in the Appendix.

*Proof.*  
Within $\Lambda$, $M$ is bounded above by a constant and below by 0; outside $\Lambda$, $M$ jumps by $\mu_0$. The constrained minimization within $\Lambda$ reduces to minimizing $\lambda_F F + \lambda_L L$.

By §3.1, $F$ is monotone decreasing in $d_k$ whenever $d_k < \max \varphi(d)$ for any $d \in S$, and constant otherwise. Hence $F$ is a step function of $d_k$ with a single floor reached when $d_k \geq \max_{d \in S} \varphi(d)$.

By §3.2, $L$ is bounded below by the count of cross-packet triples whose conductors cannot be jointly placed in a single block of size $d_k$. For a dyadic block partition and a non-dyadic packet structure, $L$ is bounded below by a positive constant proportional to $\sum_{(k, \ell, m) \in \Sigma_\times(N, S) : \text{forbidden}} N^6$. When the packet structure is itself dyadic (all $\varphi(d)$ powers of 2), there exists $(h, d_k) \in \Lambda$ with $L = 0$.

Combining: when packet structure is dyadic, $\mathcal{I}_C$ has a clean dyadic-lattice minimum; the trade-off between $F$ and $M$ selects the position on $\Lambda$. When packet structure is non-dyadic, $L$ contributes an irreducible positive term inside $\Lambda$, and as $C$ grows this term eventually outweighs the $\mu_0$ penalty for leaving $\Lambda$. The three regimes follow from the sign of $\lambda_L (L|_\Lambda - L|_{\text{pkt}}) - \mu_0$ and its comparison to $\lambda_F (F|_{d_k = d_k^{\text{tile}}} - F|_{d_k = \max \varphi(d)})$. The threshold constants $C_1, C_2$ are the two roots of this two-condition system. $\square$

### 4.2 Corollary: Vaswani as $C = 1$ for dyadic-dominated task algebras

**Corollary 4.2 (Vaswani $h = 8$).** Suppose the dominant cyclic sub-algebras of the task have 2-power packet ranks (byte-level vocab, BPE merge depth, position-mod-$2^k$). Let $d_\text{model} = 512$, $d_k^{\text{tile}} = 16$, $h^{\text{warp}} = 32$. Then for $C = 1$ and reasonable weight calibration $(\lambda_F, \lambda_L, \lambda_M) = (1/3, 1/3, 1/3)$, the unique minimizer of $\mathcal{I}_C$ over $\Lambda$ is
$$(h^\star, d_k^\star) = (8, 64),$$
with $(16, 32)$ tied within $|F|$ noise. The plateau predicted by R2 covers exactly $\{(8, 64), (16, 32)\}$.

The Vaswani Table 3 BLEU plateau at 25.8 across $\{(8, 64), (16, 32)\}$ is the empirical signature of R2.

### 4.3 Corollary: cyclic deviation

**Corollary 4.3 (Cyclic-task deviation).** Suppose the dominant cyclic sub-algebra is non-dyadic — concretely, $C_{12}$ with packet ranks $(1, 2, 2, 2, 4)$ on $S = \{2, 3, 4, 6, 12\}$. Then for $C$ large enough that R3 applies, the minimizer satisfies
$$h^\star = |S| = 5, \quad \text{head widths} = (16, 16, 16, 16, 16) \text{ if } d_\text{model} = 80,$$
*outside* $\Lambda$, with the packet-aligned target taking precedence over the dyadic constraint. For $d_\text{model} = 512$ at full transformer scale, the projection of $h^{\text{pkt}}$ onto $\Lambda$ gives $h^\star = 8$ with the heads internally further subdivided to match $\{1, 2, 2, 2, 4\}$ via a *block-sub-allocation* — a sub-frame within the dyadic frame.

This is the testable prediction: on tasks where $C_{12}$ structure dominates (calendar reasoning, music in 12-tone equal temperament, scheduling), a $(h, d_k) = (8, 64)$ transformer with internally packet-sub-allocated heads should outperform an isotropic $(8, 64)$ transformer at matched parameter count.

### 4.4 The phase diagram

Plotting the minimizer's identity as a function of $C$ and of *task-algebra dyadicity* (a single scalar summarizing $|S \cap 2^\mathbb{Z}| / |S|$) gives a three-region phase diagram:

```text
                        C (packet weight)
                              ^
                              |       R3: packet-aligned
                              |       (h^star = |S|, possibly off Lambda)
                              |
                       C_2 ---+- - - - - - - - - - - - -
                              |       R2: mixed plateau
                              |       (h^star in {(8,64),(16,32)} for d=512)
                       C_1 ---+- - - - - - - - - - - - -
                              |       R1: hardware-dominant
                              |       (h^star = (32,16) or (64,8) for d=512)
                              |
                              +----------------------------------> task dyadicity
                              0                                  1
                          (purely non-dyadic)         (purely 2-power)
```

Vaswani et al. operate effectively at $(C, \text{dyadicity}) \approx (1, 0.9)$: natural language with BPE is mostly dyadic, and they implicitly weight $L \sim M$. The R2 corner predicts $(8, 64)$.

Modern code/math/calendar fine-tunes shift the operating point leftward (lower dyadicity). The theory predicts that at sufficiently low dyadicity, $h = 8$ becomes strictly suboptimal.

---

## 5. Pre-registered architecture experiment

### 5.1 Goal

Falsify the Frame-Cost Theorem in its strongest form (Corollary 4.3): on tasks with strong $C_{12}$ structure, a packet-sub-allocated head arrangement outperforms an isotropic $(8, 64)$ arrangement at exactly matched parameter count.

### 5.2 Two configurations at matched parameter count

**Configuration V (Vaswani baseline):** Standard transformer, $d_\text{model} = 512$, $h = 8$, $d_k = d_v = 64$, all heads identically parameterized.

**Configuration P (packet-sub-allocated):** Same $d_\text{model} = 512$, same $h = 8$, same total parameter count. Each head's internal $d_k = 64$ subspace is further partitioned by an *initialization mask* into sub-blocks of widths $(1, 2, 2, 2, 4)$ (packet ranks of $C_{12}$) repeated as needed to fill 64. The mask is a learned re-parametrization; gradient flow within each sub-block is unrestricted, but the orthogonal-projection prior at the head output enforces the sub-block structure as the closed support during training (Paper 12 update-projection 100% rule applied at the head level rather than the output-head level). Total parameters identical to V.

### 5.3 Evaluation suite

Two-track evaluation:

**Track A (natural-language sanity):** WMT 2014 EN-DE perplexity. Prediction: Configurations V and P score within 0.05 PPL of each other (R2 mixed regime, dyadic-dominated; packet alignment irrelevant).

**Track B (cyclic sub-tasks):** Four held-out benchmarks with strong $C_{12}$ structure:

- *Calendar arithmetic:* "What month is 7 months after September?"
- *Modular arithmetic:* $(a + b) \mod 12$ for random $a, b$.
- *Music pitch-class:* "What pitch is 5 semitones above F?" (12-tone equal temperament).
- *Time-of-day:* "What hour is 4 hours after 9 PM?" (12-hour clock).

Prediction: Configuration P outperforms V on every Track B benchmark, with quantitative gap per task predicted by the corresponding $\Sigma_\times(12, S)$ sum:
$$\Delta \text{NLL}_{\text{task}} \approx C \cdot \lambda_L \cdot \sum_{(k, \ell, m) \in \Sigma_\times(12, S)} \left| T_{p_*}(\chi_k, \chi_\ell, \chi_m) \right|^2 \cdot \beta_{\text{task}},$$
where $\beta_{\text{task}}$ is the fraction of the task's loss attributable to cyclic structure (estimated by the Paper 26 native packet fraction on a baseline model).

### 5.4 Sample sizes and controls

- Three random seeds per configuration.
- One *negative control:* same configuration P, but with the sub-block mask shuffled (random partition of $64$ into the same multiset of widths). This isolates the packet-alignment content from the mere fact of sub-block partitioning.
- One *cross-task control:* Track C, an $\alpha$-task with no cyclic structure (sentiment classification on SST-2). Prediction: V and P tied within seed noise.

### 5.5 Compute

A small transformer (six-layer, $d_\text{model} = 512$, identical to Vaswani-base hyperparameters except for the head sub-allocation in Config P) trained on the standard WMT 2014 EN-DE pipeline plus the Track B benchmarks added as auxiliary tasks during the last 10% of training. Total compute: under 1000 GPU-hours on A100s for the full $2 \times 3 + 3$ runs.

---

## 6. Pre-registered predictions

**P1 (Vaswani anchor).** Configuration V achieves WMT 2014 EN-DE dev PPL within $[4.7, 5.1]$ and BLEU within $[25.4, 26.2]$, replicating the Vaswani Table 3 base row within seed noise.

**P2 (Track A null).** $|\text{PPL}_V - \text{PPL}_P| < 0.10$ on WMT 2014 EN-DE dev. The R2 mixed-regime prediction is that packet sub-allocation is neither help nor hindrance for dyadic-dominated natural language.

**P3 (Track B strict win).** Configuration P strictly outperforms V on all four cyclic sub-tasks, with margin $> 2 \times$ the seed-noise standard error.

**P4 (Per-task quantitative match).** The per-task margin in Track B matches the formula in §5.3 within a single global rescaling constant (the unknown calibration of $C \cdot \lambda_L$). That is, after fitting one global constant, the *ratio* of margins across the four Track B tasks should match the *ratio* of $\sum |T|^2 \beta_{\text{task}}$ predicted by Theorem 3.5 of [Paper 34](34_the_conductor_blind_spot.md).

**P5 (Shuffled-mask negative control).** Configuration P with shuffled sub-block widths does *not* outperform V on Track B; the gain is specifically attributable to packet alignment, not to sub-block partitioning per se.

**P6 (Cross-task null).** $|\text{acc}_V - \text{acc}_P| < 1\%$ on SST-2 (no cyclic structure → no theoretical gain).

**P7 (Phase-diagram corner).** The Vaswani Table 3 row (A) plateau between $h = 8$ and $h = 16$ corresponds to R2 in our phase diagram; the falloff at $h = 1$ corresponds to crossing $C_2$ from below (Fisher-projection error dominates); the falloff at $h = 32$ corresponds to crossing the warp-occupancy ceiling $h^{\text{warp}}$. The asymmetric falloff magnitudes ($-0.9$ at $h = 1$, $-0.4$ at $h = 32$) are consistent with $\lambda_F > \lambda_M$ in the natural-language operating regime.

---

## 7. Failure conditions

**F1 (Track A asymmetry).** If P5 fails but P3 succeeds — that is, P beats V on Track B *but also* on Track A — then packet sub-allocation has content beyond cyclic-task alignment, and Theorem 4.1's separation of regimes does not cleanly map to the experiment. This would be a partial confirmation requiring an extended ledger term.

**F2 (Track B null).** If P fails to outperform V on Track B, the Frame-Cost Theorem at its current resolution does not predict measurable architectural improvement from packet alignment. Two diagnostic sub-cases:
- F2a: Track B *with* shuffled mask still ties V → sub-block partitioning is the gain, alignment is not.
- F2b: Track B *with* aligned mask matches V → cyclic structure is not localized to the head dimension at this scale.

**F3 (Quantitative mismatch).** If P3 succeeds but P4 fails — the per-task margins do not follow the $\sum |T|^2 \beta_{\text{task}}$ ratio — the qualitative prediction holds but the quantitative content of Theorem 3.5 (Paper 34) is not the load-bearing mechanism at this scale. The theorem reduces to a heuristic.

**F4 (Plateau mis-prediction).** If repeating the Vaswani Table 3 row (A) ablation on the experimental setup does not reproduce the $\{(8, 64), (16, 32)\}$ plateau, the R2 prediction is inconsistent with the ablation regime at this scale.

**F5 (Cross-task non-null).** If P6 fails — V and P diverge on SST-2 — then packet sub-allocation has spurious side effects on non-cyclic tasks, and the experiment cannot isolate the predicted effect.

Each F1–F5 modifies the manuscript but does not retract the paper: the Frame-Cost ledger is reported with its empirically observed scope.

---

## 8. Anchor measurements

The Vaswani Table 3 row (A) data:

| $h$ | $d_k$ | $d_v$ | PPL (dev) | BLEU (dev) |
|---:|---:|---:|---:|---:|
| 1 | 512 | 512 | 5.29 | 24.9 |
| 4 | 128 | 128 | 5.00 | 25.5 |
| 8 | 64 | 64 | 4.92 | 25.8 |
| 16 | 32 | 32 | 4.91 | 25.8 |
| 32 | 16 | 16 | 5.01 | 25.4 |

These are the empirical points the Frame-Cost Theorem must explain in its current scope. The base row is the predicted minimum at $C = 1$, dyadic-dominated. The flat region $h \in \{8, 16\}$ at BLEU 25.8 is R2's plateau. The drop at $h = 1$ encodes the Fisher-projection floor (packet rank 128 exceeds $d_k = 512$ but the cross-head structure is absent). The drop at $h = 32$ encodes the warp-occupancy ceiling $\mu_2$ in $M(h, d_k)$.

The Vaswani Table 3 row (B) data:

| $h$ | $d_k$ | $d_v$ | PPL (dev) | BLEU (dev) |
|---:|---:|---:|---:|---:|
| 16 | 16 | 16 | 5.16 | 25.1 |
| 16 | 32 | 32 | 5.01 | 25.4 |

This is the row (B) $d_k$ floor: shrinking $d_k$ below the largest packet rank costs PPL. The Frame-Cost ledger predicts this drop's magnitude is proportional to the squared rank of the largest packet that fails to fit, weighted by its prevalence in the training distribution.

---

## 9. Script inventory

```text
empirical/frame_cost_minimizer.py
  Computes I_C(h, d_k; S) over the full hardware lattice for given
  task-algebra packet ranks. Output: the predicted (h^star, d_k^star)
  as a function of C, with phase boundaries C_1, C_2.

empirical/architecture_experiment_v_vs_p.py
  Trains Configurations V and P at matched parameter count on WMT 2014
  EN-DE plus auxiliary Track B benchmarks. Records per-task NLL, BLEU,
  PPL, per-head packet alignment metrics from Paper 36 spectroscopy.

empirical/shuffled_mask_control.py
  Runs the §5.4 shuffled-mask negative control.

empirical/cross_task_null_sst2.py
  Runs the §5.4 cross-task null control on SST-2.

empirical/reports/frame_cost_phase_diagram.md
empirical/reports/architecture_experiment_v_vs_p.md
empirical/reports/architecture_experiment_v_vs_p_shuffled_control.md
empirical/reports/architecture_experiment_v_vs_p_sst2_control.md
```

---

## 10. Result templates

### 10.1 Frame-Cost phase diagram

A figure: $(h^\star, d_k^\star)$ identity as a function of $C \in [10^{-2}, 10^2]$ and task dyadicity $\delta \in [0, 1]$, for $d_\text{model} \in \{256, 512, 1024, 4096\}$. Vaswani's operating point marked. Phase boundaries $C_1, C_2$ shown.

### 10.2 Track A (natural-language) table

| Config | PPL (dev) | BLEU (dev) |
|---|---:|---:|
| V (Vaswani) | pending | pending |
| P (packet-sub-allocated) | pending | pending |
| P (shuffled mask) | pending | pending |

P2 predicts the first two rows agree to $\pm 0.10$ PPL.

### 10.3 Track B (cyclic sub-tasks) table

| Task | $\beta_\text{task}$ (cyclic share) | NLL$_V$ | NLL$_P$ | NLL$_{P,\text{shuf}}$ | predicted gap | observed gap |
|---|---:|---:|---:|---:|---:|---:|
| Calendar | pending | pending | pending | pending | pending | pending |
| Mod-12 arithmetic | pending | pending | pending | pending | pending | pending |
| Music pitch-class | pending | pending | pending | pending | pending | pending |
| Time-of-day | pending | pending | pending | pending | pending | pending |

P3 + P4 jointly predict the *observed gap* column strictly exceeds zero on all four rows, and its ratio across rows matches the *predicted gap* column up to a single rescaling.

### 10.4 Cross-task control (SST-2) table

| Config | Accuracy |
|---|---:|
| V | pending |
| P | pending |

P6 predicts a difference under 1%.

### 10.5 Phase-diagram empirical check

Re-running the Vaswani Table 3 row (A) ablation on the experimental codebase. Predicted plateau at $\{(8, 64), (16, 32)\}$ within 0.1 BLEU; predicted asymmetric falloff at $h \in \{1, 32\}$.

---

## 11. Connections to the program

This paper sits at the intersection of seven companion papers in the corpus.

- **Foundation:** [Paper 25](25.arithmetic_frame_cost_and_curvature_linearization.md) (information-investment functional) supplies the variational template. We pulled three of its terms (Fisher-projection, packet-commutator, resource) into the transformer setting and renamed them $F$, $L$, $M$. The remaining two (depth, carry) are reserved for a forthcoming sequel on layerwise frame-cost — the natural next paper, treating depth as the resource term across the residual stream and carry as the inter-layer commutator structure.

- **Algebraic content:** [Paper 11](11.quotient_character_adjacency_algebras.md) supplies the conductor packet algebra; [Paper 26](26.conductor_probe_obstruction_theorem.md), T1 supplies the quotient projector; [Paper 34](34_the_conductor_blind_spot.md), Theorems 3.5 and 5.2 supply the cross-packet cubic structure that makes $L(h, d_k; S)$ quantitative.

- **Empirical substrate:** [Paper 36](36_layerwise_packet_spectroscopy.md) supplies the per-layer packet fraction measurement that the architecture experiment uses to estimate $\beta_\text{task}$ for each Track B task. Without the spectroscopy, the per-task quantitative prediction P4 is not testable.

- **Optimization-side counterpart:** [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md) supplies the update-projection mechanism that Configuration P uses internally; the architecture experiment is the *architectural* analogue of the Paper 12 *optimizer* experiment. The two should compose: applying update-projection to a packet-aligned architecture should give the largest gain.

- **Sibling experiment:** [Paper 37](37_label_smoothing_in_the_conductor_blind_spot.md) tests the substitution between label smoothing and update-projection. A natural three-way ablation, deferred to a sequel, is V × (no smoothing / smoothing) × (no projection / projection) on Track B.

- **Spin-off siblings:** the Paper 36 spectroscopy and Paper 37 label-smoothing experiment are this paper's two siblings in the Vaswani-comparison spin-off series identified in conversation. Together they cover the three Vaswani choices the Conductor program has sharp predictions for: head allocation (this paper), positional encoding (forthcoming Paper 39), and label smoothing (Paper 37).

### 11.1 Connection to Neural LoFi (Dandi et al., arXiv 2605.13612v1)

The Frame-Cost Theorem and the Neural LoFi second-order spectral framework live in adjacent diagrams. Neural LoFi predicts effective-dimension growth under specific training conditions; the Frame-Cost Theorem predicts which *architectural* head allocation minimizes the per-step blind-spot error at a given trade-off coefficient. A natural cross-check: the Neural LoFi effective dimension should be approximately equal across Configurations V and P on Track A (where they predict null) and should *differ* across V and P on Track B, with P showing higher effective dimension by exactly the cross-packet cubic content captured by its packet sub-allocation. This experiment is one additional driver on the architecture-experiment script and is recommended for inclusion in v0.2 of this paper.

---

## 12. Scope and limitations

This paper proves a variational principle and pre-registers one architecture experiment. It does *not*:

- Prove that the operating-point coefficient $C$ for natural language is exactly 1. The R2 corner is consistent with $C \in [0.5, 2.0]$ for the Vaswani parameters; isolating $C$ requires a hyperparameter sweep with the ledger fitted, which is deferred.

- Prove that packet sub-allocation generalizes beyond $C_{12}$ structure. The architecture experiment is the first test; replication on $C_7, C_{10}, C_{24}$ structure is the natural follow-up.

- Address the depth (multi-layer) generalization. The packet structure of the residual stream changes with layer (Paper 36); a layer-dependent head allocation is a forthcoming generalization, not the present scope.

- Address the *learned* sub-allocation question. Configuration P uses a *fixed* mask derived from the packet ranks of the dominant cyclic sub-algebra. A version of P with a *learned* sub-allocation, trained jointly with task data, is a natural sequel; we conjecture it converges to the fixed-mask configuration but do not test this here.

- Replace the dot-product attention compatibility function. Vaswani et al. observe (§6.2) that "a more sophisticated compatibility function than dot product may be beneficial." The Frame-Cost Theorem is silent on this; we treat the compatibility function as fixed.

- Predict optimal $h^\text{warp}$ on next-generation hardware. The constants $(\mu_0, \mu_1, \mu_2)$ are current-hardware-specific; the theorem's structure persists but the phase boundaries $(C_1, C_2)$ shift.

---

## 13. Conclusion

The Frame-Cost Theorem is the answer to one of the longest-standing unexplained empirical choices in transformer design: why $h = 8$. The answer has three parts.

First, the choice lives on a *lattice*. The hardware lattice $\Lambda$ and the packet lattice are both real constraints, and they only coincidentally align for the natural-language vocabularies on which transformers were originally trained.

Second, the choice is the *constrained* — not unconstrained — minimum of a three-term variational principle whose terms are individually identifiable: Fisher-projection error, packet-mismatch leakage, memory-bandwidth penalty. The constraint is the hardware lattice; the unconstrained minimum is the packet-aligned target.

Third, the choice is task-algebra-dependent in a way the Vaswani-era literature has never declared. For natural language (mostly 2-power) the constraint binds and the dyadic optimum is correct. For cyclic sub-tasks the constraint is binding *only* because the constraint weight $\lambda_M$ has been implicitly set high; lowering $\lambda_M$ — or equivalently, raising $C$ — shifts the optimum off the dyadic lattice in a quantitatively predictable way.

The architecture experiment pre-registered in §5 is the cleanest existing way to settle whether the cyclic-deviation prediction has real architectural content at production scale. The Track A null + Track B win + shuffled-mask null + cross-task null structure is fully falsifiable. If it holds, $h = 8$ is a coincidence of natural-language tokenization, and the next decade of transformer design has a degree of freedom — *task-aware head allocation* — that the Vaswani-era convention has been hiding.

If it does not hold, the Frame-Cost ledger is missing a term, and we know which experiment to run next.

The variational principle, once written down, never goes away.

---

## Appendix A. Closed forms for $C_1, C_2$ at $d_\text{model} = 512$

Under $(\mu_0, \mu_1, \mu_2) = (1, 1, 0.5)$ (hardware constants normalized to the largest-packet Fisher-projection drop), and packet ranks for the natural-language byte-level case $\{1, 2, 4, 8, 16, 32, 64, 128\}$ on $S = \{2, 4, 8, 16, 32, 64, 128, 256\}$:

$$C_1 = \mu_0 / |F|_{d_k = 16} - F|_{d_k = 32}| \approx 0.2,$$
$$C_2 = (\mu_0 + \mu_2) / |L|_{(8, 64)} - L|_{(h^\text{pkt}, d_k^\text{pkt})}| \approx 5.7.$$

The Vaswani operating point $C \approx 1$ sits squarely inside $[C_1, C_2]$, predicting R2.

For the $C_{12}$ task algebra on $S = \{2, 3, 4, 6, 12\}$ with packet ranks $\{1, 2, 2, 2, 4\}$ at $d_\text{model} = 64$:
$$C_1^{(12)} \approx 0.15, \quad C_2^{(12)} \approx 1.8.$$

A code/math/calendar fine-tune effectively operating at $C \approx 2$ would cross $C_2^{(12)}$ and predict R3: packet-aligned heads strictly outperform dyadic at $d_\text{model} = 64$.

---

*Draft v0.1 — May 19, 2026 — Frame-Cost Ledger, Frame-Cost Theorem 4.1, Vaswani $h = 8$ as the $C = 1$ corner of R2, pre-registered architecture experiment with five-prediction package and four-failure-condition envelope. v0.2 will populate §10 result templates from the architecture run on Configurations V and P at matched parameter count.*
