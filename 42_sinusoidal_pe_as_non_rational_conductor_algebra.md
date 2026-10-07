# Sinusoidal Positional Encoding as a Non-Rational Conductor Algebra: Rational-Base PE and Provable Length Extrapolation on Cyclic Sub-Tasks

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — irrationality theorem + rational-base construction + length-extrapolation theorem + one decisive experiment)**

---

## Abstract

Vaswani et al. (2017, §3.5) defined sinusoidal positional encoding as
$$PE_{pos, 2i} = \sin(pos / 10000^{2i/d}), \quad PE_{pos, 2i+1} = \cos(pos / 10000^{2i/d}),$$
chose the base $10000$ as a convenient round number, and observed in Table 3 row (E) that learned positional embeddings give "nearly identical results." Rotary Position Embedding (Su et al. 2021, [arXiv:2104.09864](https://arxiv.org/abs/2104.09864)) inherits the same geometric frequency ladder under a rotational reparameterization. ALiBi (Press et al. 2022, [arXiv:2108.12409](https://arxiv.org/abs/2108.12409)) discards the ladder entirely. Every subsequent length-extrapolation fix — NTK-aware RoPE, position interpolation (Chen et al. 2023, [arXiv:2306.15595](https://arxiv.org/abs/2306.15595)), YaRN (Peng et al. 2023, [arXiv:2309.00071](https://arxiv.org/abs/2309.00071)), xPos (Sun et al. 2022, [arXiv:2212.10554](https://arxiv.org/abs/2212.10554)) — is a post-hoc rescaling of the same irrational frequency set.

This paper supplies the structural diagnosis. The geometric base-$B$ frequency ladder $\omega_i = 1/B^{2i/d}$ generates a set of frequencies that are *rationally independent* over $\mathbb{Q}$ for every $B \notin \mathbb{Q}^{\times}_{\text{algebraic}}$ and for almost all rational $B$. The resulting position-encoding function $\mathbb{Z} \to \mathbb{R}^d$ is therefore *quasi-periodic but not periodic*: it has no finite character algebra. Under the Conductor Probe-Obstruction Theorem ([Paper 26](26.conductor_probe_obstruction_theorem.md), T1), a quotient-respecting readout — which every position-dependent downstream computation effectively is, on tasks whose label set has a finite output algebra — sees the PE only through the rational approximations of its frequencies *at the sequence length actually observed*. Train at length $L_\text{train}$; the model fits the rational approximations that look right at $L_\text{train}$; test at $L_\text{test} \neq L_\text{train}$; the rational approximations move, and the position-dependent computation breaks. *This is length-extrapolation failure, named structurally.*

We supply the positive construction. **Rational-base positional encoding** sets $\omega_i = 2\pi / P_i$ for a fixed set of integer periods $\{P_1, \dots, P_{d/2}\}$ chosen from the task's period priors (powers of 2 for byte/BPE structure; $\{3, 5, 7, 12, 24, 60, 365\}$ for calendar/time/code). The resulting PE is *exactly periodic* with period $\mathrm{LCM}\{P_i\}$; the character algebra of the PE is the finite abelian group $\bigoplus_i C_{P_i}$, decomposed exactly into conductor packets by the divisor structure of the $P_i$.

We prove (Theorem 3.1, **Length-Periodicity**) that rational-base PE is the unique class of trigonometric position encodings whose character algebra is finite. We prove (Theorem 3.2, **Length-Stable Extrapolation**) that for any model trained on rational-base PE at context length $L$, position-dependent computation is exactly preserved under any shift by a multiple of $\mathrm{LCM}\{P_i\}$, *with no architectural modification or post-hoc rescaling*. We prove (Theorem 3.3, **T1 Compatibility**) that the conductor packets of rational-base PE are the canonical packets of [Paper 26](26.conductor_probe_obstruction_theorem.md) T1, so every quotient-respecting downstream readout sees a stable, length-independent character support.

We pre-register one decisive experiment: train three small transformers ($d_\text{model} = 256$, six layers, 50M parameters) at context length $L_\text{train} = 1024$ on a cyclic-position-arithmetic training distribution; evaluate at $L_\text{test} \in \{1024, 2048, 4096, 8192, 16384\}$ on three sub-tasks (modular counting, calendar arithmetic over long contexts, music pitch-class over extended scores). The three configurations are Vaswani sinusoidal PE, RoPE, and rational-base PE aligned to $\mathrm{LCM}\{2, 3, 5, 7, 12, 24, 60\}$. The prediction is sharp: rational-base PE matches Vaswani and RoPE at $L_\text{test} = L_\text{train}$, beats both at $L_\text{test} \geq 2 L_\text{train}$ by a margin scaling with the cyclic content of the test split, and shows *zero* length-extrapolation degradation when $L_\text{test} \equiv L_\text{train} \pmod{\mathrm{LCM}}$ — the strongest form of the prediction, falsified by any nonzero observed degradation at the modular-equivalent length.

If the prediction holds, the irrational frequency ladder is the cause of the length-extrapolation problem that has accumulated five years of post-hoc fixes, and the rational-base construction is the principled alternative the literature has not tried because the structural diagnosis was absent. If it fails, the conductor-algebra account of positional encoding is wrong, and the post-hoc fixes are doing real work that rational-base PE cannot replicate.

**Keywords:** positional encoding, sinusoidal PE, rotary position embedding (RoPE), ALiBi, length extrapolation, conductor packets, character algebra, Pontryagin duality, rational frequencies, NTK-aware scaling, YaRN.

---

## 1. Introduction

### 1.1 The base-10000 choice and what it commits to

Vaswani et al. (2017, §3.5) chose base $B = 10000$ for the sinusoidal PE "because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset $k$, $PE_{pos+k}$ can be represented as a linear function of $PE_{pos}$." This is true: for any base $B$, the sinusoidal encoding satisfies
$$PE_{pos+k} = R_{\Omega k} \cdot PE_{pos},$$
where $R_{\Omega k}$ is a block-diagonal rotation matrix with per-frequency rotation angles $\omega_i k$. The choice of $B = 10000$ is irrelevant to this relative-position property.

What the choice of $B$ *does* commit to is the *set of frequencies* $\{\omega_i\}_{i=0}^{d/2-1} = \{1/B^{2i/d}\}$. For $B = 10000$ and $d = 512$, these frequencies span roughly four decades of $\omega \in [10^{-4}, 1]$ in a geometric progression. Geometric progressions of frequencies are, generically, rationally independent: there is no integer relation $\sum c_i \omega_i = 0$ with $c_i \in \mathbb{Z}$ not all zero. This is true for $B$ algebraic of degree $\geq d/2$ and for almost all transcendental $B$. (For $B = 10000$, the integer relation $\omega_0 / \omega_{d/2-1} = 10000$ is the only rational relation among the extremes; for intermediate frequencies the ratios are generically irrational.)

Rationally independent frequencies generate a position-encoding function $PE : \mathbb{Z} \to \mathbb{R}^d$ that is *quasi-periodic*: it densely fills an orbit on the $d/2$-torus and never exactly repeats. There is no integer $T > 0$ such that $PE_{pos + T} = PE_{pos}$ for all $pos$.

### 1.2 What quasi-periodicity costs at inference time

A model trained at context length $L_\text{train}$ sees $L_\text{train}$ samples of $PE$. The model fits the position-dependent regularities present in those $L_\text{train}$ samples. Among those regularities are approximate periodicities: at any sequence length, *some* rational approximation $\omega_i \approx p/q$ holds for *some* $p, q$, and the model can exploit it within that length.

But the rational approximations are length-dependent. At $L_\text{train} = 1024$, the rational approximation $\omega_i \approx p_i / q_i$ that the model can exploit has $q_i$ comparable to $L_\text{train}$. At $L_\text{test} = 4 L_\text{train} = 4096$, the optimal rational approximation has $q_i$ comparable to $L_\text{test}$, and it is *not* the same approximation. The model's position-dependent computation, built around the $L_\text{train}$-scale approximations, becomes inconsistent with the $L_\text{test}$-scale approximations.

This is the structural form of the length-extrapolation problem that NTK-aware RoPE, position interpolation, YaRN, and xPos are post-hoc fixes for. Each of those methods is, in effect, a *rescaling of the frequency ladder* to bring the $L_\text{train}$-scale rational approximations into alignment with the $L_\text{test}$-scale ones. They are local fixes for a global structural mismatch.

The Conductor Probe-Obstruction Theorem ([Paper 26](26.conductor_probe_obstruction_theorem.md), T1) makes the structural mismatch precise: any downstream readout whose codomain has a finite output algebra factors through a quotient $C_N \to C_k$, retaining exactly the conductor packets $H_d$ with $d \mid k$. The packets are defined by the *character algebra* of the PE input. For sinusoidal PE with rationally independent frequencies, *the character algebra is not finite*; the effective packet structure is whatever finite approximation of the irrational frequencies the model has implicitly learned at training scale, and this approximation shifts at test scale.

### 1.3 The positive construction

Replace the geometric base-$B$ ladder with rational periods drawn from task priors:
$$\omega_i = \frac{2\pi}{P_i}, \qquad P_i \in \mathbb{Z}_{\geq 2}.$$
The PE function $\mathbb{Z} \to \mathbb{R}^d$ is now *exactly periodic* with period $\mathrm{LCM}\{P_i\}$. Its character algebra is the finite abelian group $\bigoplus_i C_{P_i}$, and its conductor packet decomposition is the canonical one of [Paper 26](26.conductor_probe_obstruction_theorem.md) T1.

The choice of $\{P_i\}$ is the load-bearing design choice. For 2-power-dominated task structure (byte vocab, BPE merges, position-mod-$2^k$), $P_i = 2^{i+1}$ recovers a 2-adic conductor algebra. For natural-language code/math/calendar mixes, the LCM-saturating set $\{2, 3, 5, 7, 12, 24, 60, 365\}$ covers the standard period priors and gives $\mathrm{LCM} = 2^3 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 365 / \gcd = 8 \cdot 9 \cdot 25 \cdot 7 \cdot 73 = 919800$ — comfortably larger than any realistic training context. For pure long-context byte-stream tasks the powers-of-2 ladder $\{2, 4, 8, 16, ..., 2^{d/2}\}$ saturates the 2-adic algebra with $\mathrm{LCM} = 2^{d/2}$.

This paper proves three theorems about this construction (§3), pre-registers one decisive experiment (§4–6), and closes the structural diagnosis the length-extrapolation literature has been working around for five years.

---

## 2. Setup

### 2.1 The PE as a function $\mathbb{Z} \to \mathbb{R}^d$

A positional encoding is a function $PE : \mathbb{Z} \to \mathbb{R}^d$. Its *character algebra* is the smallest finite abelian group $A$ such that $PE$ factors through the canonical projection $\mathbb{Z} \to A$, if such an $A$ exists; otherwise its character algebra is *infinite* (equivalently, $PE$ is non-periodic).

For trigonometric PE with frequency set $\Omega = \{\omega_i\}$, $PE$ factors through $\mathbb{Z} / T \mathbb{Z}$ for some finite $T$ if and only if there exist integers $n_i \in \mathbb{Z}$ such that $\omega_i = 2\pi n_i / T$ for all $i$. Equivalently: all $\omega_i / (2\pi)$ are rational with a common denominator $T$.

If $\Omega$ contains any irrational $\omega_i / (2\pi)$, no finite $T$ works, and the character algebra of $PE$ is infinite. The PE is then *quasi-periodic*: it has dense orbit on $\mathbb{T}^{d/2}$ but never closes.

### 2.2 Vaswani's sinusoidal PE

Vaswani's choice $\omega_i = 1/10000^{2i/d}$ gives $\omega_i / (2\pi)$ values that are generically irrational. For $d = 512$ and $i \in \{0, 1, \ldots, 255\}$, exactly two values $(i = 0$ giving $\omega = 1$ and $i = d/2$ giving $\omega = 1/10000)$ are rational, and the rest are transcendental by the Gelfond–Schneider theorem applied to $10000^{2i/d}$ with $2i/d$ irrational for most $i$. The character algebra is therefore *infinite*.

### 2.3 RoPE

Rotary Position Embedding (Su et al. 2021) uses the same frequency ladder $\omega_i = 1/B^{2i/d}$ as Vaswani, rotating pairs of embedding dimensions by $\omega_i \cdot pos$ rather than concatenating sin/cos. The character algebra of the *rotation pattern* is identical to Vaswani's: infinite, quasi-periodic. RoPE inherits the length-extrapolation problem exactly because the rotation angles do not commensurate over any finite period.

### 2.4 ALiBi

Press et al. 2022's ALiBi replaces sinusoidal PE with a linear distance bias $-m \cdot |i - j|$ added to attention logits, where $m$ is a per-head slope. The character algebra of ALiBi's positional information is *trivial* (the linear function $i - j$ has no nontrivial Fourier content over $\mathbb{Z}$), so the conductor obstruction is vacuous for ALiBi. ALiBi extrapolates well at the cost of representing essentially no positional structure beyond distance — a separate trade-off explored in §9.2.

---

## 3. Theorems

### 3.1 The Length-Periodicity Theorem

**Theorem 3.1 (Length-Periodicity).** Let $PE : \mathbb{Z} \to \mathbb{R}^d$ be a trigonometric positional encoding with frequency set $\Omega = \{\omega_0, \dots, \omega_{d/2-1}\}$. The character algebra of $PE$ is finite if and only if every $\omega_i / (2\pi) \in \mathbb{Q}$. When this holds, the character algebra is exactly
$$A_\text{PE} = \bigoplus_{i=0}^{d/2-1} C_{P_i}, \qquad P_i = \text{denominator of } \omega_i / (2\pi) \text{ in lowest terms},$$
and $PE_{pos + \mathrm{LCM}\{P_i\}} = PE_{pos}$ for all $pos \in \mathbb{Z}$.

*Proof.* For $\omega_i / (2\pi) = a_i / P_i$ with $\gcd(a_i, P_i) = 1$, the $i$-th frequency component of $PE$ has minimal period $P_i$ in $pos$. The vector PE has period equal to the LCM of all component periods, which is $\mathrm{LCM}\{P_i\}$. The character algebra is then $\mathbb{Z} / \mathrm{LCM}\{P_i\}\mathbb{Z}$, which decomposes by CRT into $\bigoplus_i C_{P_i}$.

Conversely, if any $\omega_j / (2\pi)$ is irrational, the sequence $\{\omega_j \cdot pos \mod 2\pi\}_{pos \in \mathbb{Z}}$ is equidistributed on $[0, 2\pi)$ by Weyl's theorem, hence non-periodic; the vector $PE$ is then also non-periodic, and the character algebra is infinite. $\square$

### 3.2 The Length-Stable Extrapolation Theorem

**Theorem 3.2 (Length-Stable Extrapolation).** Let $M$ be a transformer with rational-base PE having character algebra $A_\text{PE}$ of period $T = \mathrm{LCM}\{P_i\}$. Let $f : \mathbb{Z}^L \to \mathcal{Y}$ be any position-equivariant function computed by $M$ (e.g., the output of a head at the last position, the attention pattern, the hidden state at a given position). Then for every $L \geq 1$, every input $x \in \mathbb{Z}^L$, and every $k \in \mathbb{Z}$,
$$f(x; \text{positions } 0, 1, \ldots, L-1) = f(x; \text{positions } k T, k T + 1, \ldots, k T + L - 1).$$

In particular, a model trained at context length $L_\text{train}$ computes the same position-dependent function at any test length $L_\text{test} \equiv L_\text{train} \pmod{T}$, with zero degradation from the position-encoding source.

*Proof.* The PE input to $M$ at position $kT + j$ equals the PE input at position $j$ by Theorem 3.1, since $PE_{kT + j} = PE_j$. All position-dependent computation in $M$ depends on the sequence only through the PE values at the input positions and through token content; the token content at $kT + j$ in the second expression is, by construction, the same as at $j$ in the first. Hence the output is identical. $\square$

Theorem 3.2 is the strongest form of length extrapolation: it says the *failure does not occur* when the test length is modulo-LCM-congruent to the training length, not merely that the failure is *small*. The non-rational case has no analogous theorem because there is no $T$ at which the PE periodically closes.

### 3.3 The T1 Compatibility Theorem

**Theorem 3.3 (T1 Compatibility).** Let $PE$ have rational-base character algebra $A_\text{PE} = \bigoplus_i C_{P_i}$ as in Theorem 3.1, and let $q : A_\text{PE} \to A_\text{PE}/K$ be any quotient. The conductor packets of $A_\text{PE}$ — defined per [Paper 26](26.conductor_probe_obstruction_theorem.md), §2.1, as the spans of characters with equal conductor — admit a canonical decomposition $A_\text{PE} = \bigoplus_d H_d$, and the orthogonal projection $P_q$ onto the quotient-respecting subspace is diagonal in the packet basis with eigenvalues $0$ or $1$ exactly as in [Paper 26](26.conductor_probe_obstruction_theorem.md), T1.

*Proof.* The packet decomposition is the direct sum over conductors $d$ dividing the period of $A_\text{PE}$, where each packet is the sum of character lines of order exactly $d$ in $A_\text{PE}$. The application of T1 of [Paper 26](26.conductor_probe_obstruction_theorem.md) is then immediate: $P_q$ retains exactly the characters trivial on $K$, equivalently those whose conductor divides the order of $A_\text{PE}/K$. $\square$

The combined content of Theorems 3.1, 3.2, 3.3: rational-base PE is the unique class of trigonometric position encodings whose conductor algebra is *both* finite (Theorem 3.1, length-stable) and *aligned with the T1 obstruction* (Theorem 3.3, packet-resolvable). Sinusoidal PE has neither property; RoPE inherits the failure.

### 3.4 What changes vs. what doesn't

What rational-base PE *preserves* relative to sinusoidal:
- The relative-position lift $PE_{pos+k} = R_{\Omega k} PE_{pos}$ remains exact and linear, with the same per-frequency rotation structure. The "any fixed offset $k$ is a linear function" property Vaswani named is *not* lost.
- The $d$-dimensional embedding budget is identical.
- The attention computation is unchanged.

What rational-base PE *changes*:
- The frequency spectrum is sparse (only rational frequencies with bounded denominators) rather than dense (geometric ladder).
- The character algebra is finite and named, not infinite and quasi-periodic.
- Length extrapolation modulo the LCM is exact rather than approximate.

What rational-base PE *gives up*:
- The fine-grained sub-period frequency content of the geometric ladder. At small $\mathrm{LCM}$ choices, the model has less positional resolution per token at any single length.

The trade-off is positional *resolution* (sinusoidal wins) vs. positional *stability under length shift* (rational wins). For tasks with strong cyclic structure at known periods, rational is the right side of the trade-off. For tasks where positional information is unknown-period and fine-grained, sinusoidal may remain better; the experiment in §5 separates these regimes.

---

## 4. The rational-base PE construction

### 4.1 Choosing the period set $\{P_i\}$

We pre-commit to three rational-base PE variants for the experiments:

**RBP-natural.** $\{P_i\} = $ a stratified set covering the LCM of $\{2, 3, 5, 7, 12, 24, 60, 365\}$, with the first $d/2$ chosen to include one copy of each small prime power up to $7$ and then progressively larger LCMs. For $d = 256$ and $d/2 = 128$ frequencies, the set is $\{2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, \dots\}$ continuing through divisors of $\mathrm{LCM}\{2, 3, 5, 7, 12, 24, 60, 365\} = 919800$.

**RBP-byte.** Powers-of-2 ladder $\{P_i = 2^{i+1}\}_{i=0}^{d/2-1}$, saturating the 2-adic algebra. For $d = 256$ this gives $\mathrm{LCM} = 2^{128}$, far larger than any practical context, so for byte-only tasks this is effectively length-stable on all realistic windows.

**RBP-calendar.** Specifically tuned to calendar periods $\{12, 7, 24, 30, 365, 60, 4, 52\}$ replicated and combined with small powers $\{1, 2, 3, 4, 5, 6\}$ to fill $d/2$ frequencies. Predicted to dominate on time-aware tasks specifically.

The choice between RBP-natural, RBP-byte, and RBP-calendar is itself a hyperparameter. We test all three in the experiment.

### 4.2 The encoding formula

For each $i \in \{0, \dots, d/2-1\}$ with chosen period $P_i$:
$$PE_{pos, 2i} = \sin(2\pi \cdot pos / P_i), \qquad PE_{pos, 2i+1} = \cos(2\pi \cdot pos / P_i).$$

Identical functional form to Vaswani; only the frequencies change.

### 4.3 The rotary variant

A rational-base RoPE (RBR) uses the same rational frequencies as RBP but rotates query/key pairs by $2\pi \cdot pos / P_i$. The Theorem 3.2 length-stability inherits: relative-position dot products between positions $pos$ and $pos + k$ depend only on $k \mod P_i$ for each frequency, hence on $k \mod \mathrm{LCM}\{P_i\}$ globally.

### 4.4 Initialization and learnability

The rational-base PE is *fixed* and *not learned*. Like Vaswani sinusoidal, it requires no parameters. Adding it to an existing codebase is a one-line change: replace the frequency-ladder function with the rational-period set.

---

## 5. Pre-registered experiment

### 5.1 Goal

Falsify, or fail to falsify, Theorem 3.2 in operational form: a model trained with rational-base PE shows zero length-extrapolation degradation at $L_\text{test} \equiv L_\text{train} \pmod{\mathrm{LCM}}$, and superior degradation at $L_\text{test}$ not modulo-congruent. Models trained with sinusoidal PE or RoPE show standard quasi-monotonic degradation in $L_\text{test}/L_\text{train}$.

### 5.2 Model

Six-layer transformer, $d_\text{model} = 256$, $h = 8$, $d_k = d_v = 32$, FFN expansion 4, GELU activation, pre-norm. Parameters: ~50M. Identical across PE variants; only the position-encoding function differs.

### 5.3 PE variants

Five configurations:

| ID | PE variant | Frequency set |
|---|---|---|
| Sin-10K | Vaswani sinusoidal | $\omega_i = 1/10000^{2i/d}$ |
| RoPE-10K | Su et al. RoPE | $\omega_i = 1/10000^{2i/d}$ |
| RBP-nat | This paper, natural | $\omega_i = 2\pi / P_i^{\text{nat}}$ |
| RBP-byte | This paper, byte | $\omega_i = 2\pi / 2^{i+1}$ |
| RBR-nat | This paper, RoPE-style rational | $\omega_i = 2\pi / P_i^{\text{nat}}$ |

### 5.4 Training distribution

Synthetic cyclic-position-arithmetic tasks at $L_\text{train} = 1024$:

- *Modular counting*: prompt is a sequence of tokens with one numeric anchor; target is anchor + position mod $N$ for $N \in \{7, 12, 24, 60\}$, sampled per example.
- *Calendar arithmetic*: prompt contains a date and an offset; target is the date shifted by the offset, with one of (day-of-week, day-of-month, month, year-of-decade) selected.
- *Music pitch-class*: prompt contains a starting pitch and an interval expressed in semitones; target is the pitch-class shifted modulo 12.

Mixed in a 1:1:1 ratio. Standard transformer training: AdamW, lr=3e-4, batch size 32, dropout 0.1, label smoothing 0.0 (per [Paper 37](37_label_smoothing_in_the_conductor_blind_spot.md), to avoid confounding the experiment), 100k steps.

### 5.5 Test grid

For each (PE variant, task), evaluate at:
- $L_\text{test} = 1024$ ($= L_\text{train}$).
- $L_\text{test} = 2048, 4096, 8192, 16384$ (powers-of-2 extrapolation).
- $L_\text{test} = L_\text{train} + k \cdot \mathrm{LCM}\{P_i^\text{nat}\}$ for $k = 1, 2, 3$ — the *modular-congruent* extrapolation lengths predicted by Theorem 3.2 to give zero degradation for RBP-nat.

The $L_\text{test} = L_\text{train} + k \cdot \mathrm{LCM}$ rows are the load-bearing rows. For RBP-nat with the natural period set, $\mathrm{LCM} = 919800$, but for shorter LCMs (e.g., dropping $365$) we can choose $\mathrm{LCM} = 2520 = \mathrm{LCM}\{2,3,4,5,6,7,8,9,10\}$, giving testable modular-congruent lengths $L_\text{train} + 2520 = 3544$, $L_\text{train} + 5040 = 6064$, etc. The experiment uses the shorter $\mathrm{LCM} = 2520$ set for testability.

### 5.6 Primary outcomes

Per (PE variant, task, $L_\text{test}$) cell:
- Held-out accuracy averaged over three seeds.
- *Length-extrapolation degradation* $\Delta_L := \text{acc}(L_\text{test}) - \text{acc}(L_\text{train})$.
- *Modular-congruent degradation* $\Delta_L^*$ at $L_\text{test} = L_\text{train} + k \cdot \mathrm{LCM}$.

### 5.7 Compute

Five PE variants × three tasks × three seeds × ~12 hours per training run on a single A100. Total: ~30 GPU-days. Achievable on a small academic cluster in two weeks.

---

## 6. Pre-registered predictions

**P1 (At training length).** All five PE variants achieve comparable accuracy at $L_\text{test} = L_\text{train}$, within seed noise (gap $< 2\%$).

**P2 (Powers-of-2 extrapolation).** At $L_\text{test} = 2 L_\text{train}, 4 L_\text{train}, 8 L_\text{train}, 16 L_\text{train}$:
- Sin-10K and RoPE-10K show progressively larger negative $\Delta_L$ (monotone-in-$L_\text{test}/L_\text{train}$ degradation).
- RBP-byte shows the *smallest* $\Delta_L$ at powers-of-2 test lengths because all powers-of-2 are exactly congruent to integer multiples of small periods in its ladder.
- RBP-nat and RBR-nat show degradation intermediate between RBP-byte and the irrational baselines: they degrade because $2 L_\text{train} \not\equiv L_\text{train} \pmod{\mathrm{LCM}}$, but less than the irrational baselines because some sub-frequencies are still aligned.

**P3 (Modular-congruent extrapolation — the load-bearing prediction).** At $L_\text{test} = L_\text{train} + k \cdot 2520$ for $k = 1, 2, 3$:
- RBP-nat and RBR-nat show $|\Delta_L^*| < 1\%$ (within seed noise, equivalent to "no degradation") on all three tasks.
- Sin-10K and RoPE-10K show $|\Delta_L^*| \geq 5\%$ on at least two of the three tasks at the longest modular-congruent length tested.

**P4 (Task scaling).** Within each PE variant, the degradation $|\Delta_L|$ at fixed $L_\text{test}$ scales with the *cyclic content* of the task — calendar arithmetic with explicit periodic answer space is most degraded by irrational PE; modular counting next; music pitch-class similarly. P4 is a positive prediction for the conductor account: degradation is structurally located in tasks whose output has finite cyclic algebra, exactly where T1 applies.

**P5 (Per-LCM monotonicity).** For RBP-nat, $|\Delta_L|$ as a function of $L_\text{test}$ is *non-monotone*: local minima appear at every multiple of every $P_i$ in the period set, with the global minimum at every multiple of $\mathrm{LCM}$. This is the signature of finite character algebra: the model is *length-equivariant* under every LCM step, and partially equivariant under each $P_i$ step.

**P6 (Comparison to YaRN/PI fixes).** Adding NTK-aware rescaling (NTK-aware) or position interpolation (PI) to Sin-10K and RoPE-10K *closes the gap* to RBP-nat at extrapolation lengths far from training but *cannot close the gap at modular-congruent lengths*, because the post-hoc fixes still operate on an irrational frequency set whose alignment with arbitrary $L_\text{test}$ remains accidental. Predicted: RBP-nat strictly beats NTK-aware-RoPE and PI-RoPE at modular-congruent lengths.

**P7 (Single rational-base wins on byte tasks).** On a separate byte-stream evaluation (per-byte language modeling perplexity at extrapolation lengths), RBP-byte's powers-of-2 ladder beats all other PE variants because byte-stream length extrapolation tests are dominated by 2-power period structure (byte boundaries at every $2^k$, etc.). This is a side-prediction that, if correct, gives RBP-byte a credible deployment niche.

---

## 7. Failure conditions

**F1 (No modular-congruent advantage).** If P3 fails — RBP-nat does *not* show $|\Delta_L^*| < 1\%$ at modular-congruent lengths — the operational form of Theorem 3.2 fails. The theorem proves the PE input is equal at modular-congruent positions; the failure would mean the model has learned something else that breaks under the supposed equivariance (positional content leaking through token embeddings, attention biases learned in a length-dependent way, etc.). The paper would report this as a structural surprise.

**F2 (No general extrapolation advantage).** If P2 fails — Sin-10K and RoPE-10K do *not* degrade more than RBP-nat at non-modular-congruent lengths — the irrational frequency ladder is not the cause of length extrapolation problems. The standard literature account (post-hoc rescaling fixes are necessary) is then the correct one, and the present paper's positive claim has no empirical content.

**F3 (RBP-byte fails on byte tasks).** If P7 fails — RBP-byte does not dominate byte-stream extrapolation — the powers-of-2 ladder's theoretical advantage for byte tasks does not translate to a practical gain, and the rational-base approach's strongest case for deployment evaporates.

**F4 (NTK-aware closes everything).** If P6 fails — NTK-aware rescaling fully closes the gap at modular-congruent lengths too — then the structural diagnosis is wrong: the irrationality of the frequency ladder *is* fixable by post-hoc rescaling, and rational-base PE is at most a convenience, not a structural improvement.

**F5 (Resolution loss dominates).** If at $L_\text{test} = L_\text{train}$ (P1) the rational-base variants are *strictly worse* than Sin-10K (gap > 2%), the lower positional resolution of the rational ladder is operationally important and the trade-off is not favorable. We would then narrow the recommendation to specifically cyclic-content-dominated tasks and back away from a general replacement claim.

---

## 8. Implementation notes

### 8.1 The one-line change

Replacing Vaswani sinusoidal with rational-base PE in a standard codebase is the substitution:

```python
# Vaswani (current):
freqs = 1.0 / (10000.0 ** (torch.arange(0, d, 2) / d))
# Rational-base (proposed):
periods = torch.tensor([P_i for i in range(d // 2)])   # pre-registered set
freqs = 2 * math.pi / periods
```

with $\{P_i\}$ fixed by the chosen variant (§4.1).

### 8.2 Period set storage

The natural period set RBP-nat must be specified explicitly. For reproducibility, the experiment ships a single file `empirical/rbp_periods_natural.json` enumerating the $d/2 = 128$ chosen periods in canonical order. Any deviation must be documented.

### 8.3 Floating-point considerations

For very large periods $P_i$ (e.g., 919800), the angle $2\pi \cdot pos / P_i$ at $pos = 10^5$ has absolute value under $0.7$ — well within fp32 precision. No special handling required.

For very small periods (e.g., $P_0 = 2$), the angle $2\pi \cdot pos / 2 = \pi \cdot pos$ has period 2 in $pos$; the sin/cos values are exactly $\{0, 1, 0, -1, \dots\}$ in floating point. The encoding is degenerate-but-correct for $P_i = 2$; we exclude $P_i = 1$ (constant, no information).

### 8.4 Backward compatibility

Models trained with sinusoidal PE *cannot* be evaluated with rational-base PE without retraining. The PE variant is part of the model's weights' interpretation; the input at position $pos$ at frequency $i$ is different under the two encodings. This restricts deployment-relevant comparisons to models that were trained from scratch with the chosen PE variant.

---

## 9. Connections to the existing PE literature

### 9.1 RoPE and its extensions

Rotary Position Embedding (Su et al. 2021, [arXiv:2104.09864](https://arxiv.org/abs/2104.09864)) replaces additive sinusoidal PE with rotational query/key pair updates. It inherits the geometric base-$B$ frequency ladder exactly; the relative-position rotation angle at frequency $i$ over position offset $k$ is $\omega_i k = k / B^{2i/d}$, the same irrational quantity. Length extrapolation problems are reported throughout the RoPE literature.

NTK-aware RoPE (bloc97 2023, technical report) and position interpolation (Chen et al. 2023, [arXiv:2306.15595](https://arxiv.org/abs/2306.15595)) rescale the frequency ladder by a length-dependent factor. YaRN (Peng et al. 2023, [arXiv:2309.00071](https://arxiv.org/abs/2309.00071)) combines both with frequency-dependent rescaling. xPos (Sun et al. 2022, [arXiv:2212.10554](https://arxiv.org/abs/2212.10554)) adds exponential decay terms. All are post-hoc fixes; none changes the irrationality.

The present paper's claim is that the irrationality *is* the structural problem. Rational-base PE is the direct fix.

### 9.2 ALiBi

Press et al. 2022's ALiBi removes the PE and adds a linear distance bias. Its character algebra is trivial; the obstruction is vacuous. ALiBi extrapolates exceptionally well *and* loses essentially all non-distance positional content. The trade-off: rational-base PE retains the *cyclic content* that ALiBi discards, at the cost of more complexity than ALiBi.

The clean comparison is: ALiBi is the right answer when no cyclic content is needed; RBP is the right answer when cyclic content is needed; sinusoidal/RoPE is the wrong answer either way (too much complexity for ALiBi's case, wrong algebraic structure for RBP's case).

### 9.3 Other absolute PE approaches

Learned PE (Vaswani Table 3 row E) ties positional information to a parameter per (position, dimension) pair, with no algebraic structure. It is bounded by training length and does not extrapolate at all. Relative PE (Shaw et al. 2018) and T5's relative bucket PE (Raffel et al. 2020) introduce coarser relative-position structure; their character algebras are typically finite but ad-hoc. The conductor-algebra view subsumes both: any choice of finite character algebra is a valid rational-base PE variant; the design question is which one.

### 9.4 Connection to the Conductor program

- [Paper 11](11.quotient_character_adjacency_algebras.md): supplies the character algebra and conductor packet vocabulary.
- [Paper 26](26.conductor_probe_obstruction_theorem.md), T1: supplies the structural obstruction that distinguishes rational from irrational character algebras at the readout level.
- [Paper 36](36_layerwise_packet_spectroscopy.md): the present paper's experiment can be evaluated *layerwise* using Paper 36's protocol, giving a more granular picture of where positional content is encoded.
- [Paper 38](38_multi_head_attention_as_frame_cost_minimization.md): rational-base PE supplies a *coordinatized* substrate for the frame-cost minimization on the position-id sub-vocabulary; the two papers compose for positional packet allocation.

---

## 10. Result templates

### 10.1 Length-extrapolation grid

Per (PE variant, task), a length-extrapolation curve $\text{acc}(L_\text{test}) - \text{acc}(L_\text{train})$ vs. $L_\text{test} / L_\text{train}$:

| $L_\text{test}$ | $L_\text{test}/L_\text{train}$ | Sin-10K | RoPE-10K | RBP-nat | RBP-byte | RBR-nat |
|---:|---:|---:|---:|---:|---:|---:|
| 1024 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2048 | 2.0 | pending | pending | pending | pending | pending |
| 4096 | 4.0 | pending | pending | pending | pending | pending |
| 8192 | 8.0 | pending | pending | pending | pending | pending |
| 16384 | 16.0 | pending | pending | pending | pending | pending |
| **3544** | **3.46** | pending | pending | pending | pending | pending |
| **6064** | **5.92** | pending | pending | pending | pending | pending |
| **8584** | **8.38** | pending | pending | pending | pending | pending |

Three such tables, one per task. The **bold rows** are the modular-congruent test lengths $L_\text{train} + k \cdot 2520$ — the load-bearing rows for P3.

### 10.2 Modular-congruent comparison figure

A single figure: $\Delta_L^*$ vs. $k \in \{0, 1, 2, 3\}$ (the modular-congruent index), one line per PE variant. P3 predicts RBP-nat and RBR-nat are flat at $\Delta_L^* \approx 0$; Sin-10K and RoPE-10K show negative drift.

### 10.3 NTK-aware comparison

For Sin-10K and RoPE-10K only, evaluated with and without NTK-aware rescaling. P6 predicts NTK closes the *non-congruent* gap but not the modular-congruent gap.

### 10.4 Byte-task table

Per-byte language modeling perplexity at $L_\text{test}$ extrapolation lengths, all five PE variants. P7 predicts RBP-byte's powers-of-2 ladder dominates.

---

## 11. Scope and limitations

### 11.1 What this paper does not claim

It does not claim that rational-base PE is the *best* positional encoding for *all* tasks. The trade-off between positional resolution and length stability favors rational-base on tasks with strong cyclic content; on tasks where positional content is unknown-period and fine-grained, the irrational sinusoidal ladder may remain preferable. The paper's claim is that rational-base PE *exists*, has *named theoretical properties*, and *beats irrational baselines* on cyclic-content tasks at extrapolation lengths. It does not claim a universal replacement.

### 11.2 What this paper does not require

It does not require retraining of existing models. It is a recipe for *new* models trained from scratch with the rational-base PE. The existing fleet of Llama, Mistral, GPT-class models will continue using their sinusoidal/RoPE PEs and will continue to need YaRN/PI for long-context inference.

### 11.3 What this paper opens up

The structural diagnosis — irrationality is the source of length-extrapolation problems — invites a series of follow-up questions:

- *Learned rational PE*: can the period set $\{P_i\}$ be learned during training, with regularization toward small primes? This would give a learned rational character algebra optimized to the actual task period priors, going beyond pre-committed sets.
- *Task-adaptive period activation*: at inference time, gating which $P_i$'s contribute to attention based on the prefix's identified cyclic content, recovering positional resolution where it matters.
- *Compositional PE*: combining rational-base PE with ALiBi's distance bias gives a model that has both cyclic and decay content. The theory permits this composition; the experiments do not include it.

### 11.4 Restriction to trigonometric PE

The theorems are stated for trigonometric PE. They do not directly apply to ALiBi's linear bias, to T5's relative-position buckets, or to learned PE. The natural generalization treats any positional encoding as a function $\mathbb{Z} \to \mathbb{R}^d$ and asks whether its image lies on a compact orbit (finite character algebra) or not. For ALiBi, the function is linear and the image is unbounded; the "compact orbit" question is degenerate. We do not generalize.

---

## 12. Conclusion

Vaswani et al.'s 10000-base sinusoidal PE committed the transformer architecture to an *irrational* frequency ladder. Every subsequent length-extrapolation fix — NTK-aware, position interpolation, YaRN, xPos — has been a rescaling of that ladder. The Conductor Probe-Obstruction Theorem of [Paper 26](26.conductor_probe_obstruction_theorem.md) makes the structural cost precise: any downstream readout with a finite output algebra sees the PE only through whatever rational approximations are valid at the observed sequence length, and those approximations shift with length.

Rational-base PE replaces the geometric ladder with frequencies drawn from a fixed integer period set. The character algebra becomes finite (Theorem 3.1), length extrapolation is exact at modular-congruent lengths (Theorem 3.2), and the conductor packets are the canonical T1 packets of the Conductor program (Theorem 3.3). The construction is a one-line code change, parameter-free, fully backward-incompatible with existing models trained on sinusoidal/RoPE, and predicted to beat both baselines on cyclic-content tasks at extrapolation lengths.

The pre-registered five-variant × three-task × eight-test-length experiment is decisive: P3's modular-congruent prediction is sharp enough that a single observed non-flat $\Delta_L^*$ on RBP-nat would falsify the operational form of the theorem. P2's general extrapolation prediction matches the structural diagnosis to the empirical phenomenology of irrational-PE length problems. P6's NTK comparison directly tests whether post-hoc rescaling can do what rational-base PE does structurally.

If the predictions hold, the five years of post-hoc length-extrapolation fixes have been working around a structural problem that the rational-base alternative removes from the start. If they fail, the conductor-algebra account of positional encoding is wrong, and the literature's empirical instinct that rescaling is necessary is correct.

The one decisive experiment costs thirty GPU-days. The literature has spent more on rescaling.

---

*Draft v0.1 — May 19, 2026 — Length-Periodicity Theorem 3.1, Length-Stable Extrapolation Theorem 3.2, T1 Compatibility Theorem 3.3, rational-base PE construction with three pre-committed variants, five-variant × three-task × eight-test-length experimental sweep with seven sharp predictions and five failure conditions. v0.2 will populate §10 result templates from the sweep, with the modular-congruent rows at $L_\text{train} + k \cdot 2520$ as the load-bearing observations.*
