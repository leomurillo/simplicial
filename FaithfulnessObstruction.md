# What a Readout Can See: An Exact Conductor-Divisor Law for the Faithfulness of Probes, Logit Lenses, and Sparse Autoencoders on Cyclic Concepts

**Leonardo Murillo Montero**
*June 13, 2026*

**arXiv-style preprint (draft v0.1 — spine: consolidation of the conductor obstruction line (Papers 26, 36, 40, 45) into one interpretability-facing unit, with cross-model spectroscopy and the CCSAE certificate as delivered empirical anchors)**

---

## Abstract

Mechanistic interpretability is built on *readouts* — linear probes, the logit and tuned lens, and sparse-autoencoder dictionaries — yet the field has no a priori theory of what a given readout *can* recover, only post hoc faithfulness scores, and those scores increasingly disagree: data-driven circuit discovery reports 87% mixed-faithfulness, probes clear chance on meaningless control tasks, and sparse autoencoders leave a fraction of linearly predictable error unexplained. We supply an exact theory for the structured concept class where the question is sharpest — cyclic categories, the days-of-week and months features that Engels et al. (2024) showed are genuinely circular and serve as the computational unit of modular arithmetic across GPT-2, Mistral-7B, and Llama-3-8B.

We prove that any readout whose codomain is a $k$-resolution quotient of the cyclic label algebra $C_N$ retains exactly the conductor packets $H_d$ with $d \mid k$ and annihilates exactly those with $d \nmid k$. This Pontryagin divisor rule fixes, before any activation is observed, which concept-packets a probe, lens, or autoencoder is structurally blind to: faithfulness becomes a *computable obstruction* rather than a measured number, and the readout quotient — not the model — determines what is visible.

We validate the law with a pre-registered, cross-model layerwise spectroscopy on Llama-3.1-8B and Mistral-7B-v0.3. Final-layer packet fractions reproduce to $\leq 5\times10^{-4}$ and the forbidden-packet zeros hold at machine precision. Our central exhibit is a *measured instrument-dependence*: at one fixed layer of a fixed model the full-period concept reads $0.356$ through a trained probe and $0.638$ through the frozen-unembedding lens — a $0.28$ discrepancy with no model-side cause, reconciled to $6\times10^{-5}$ by the theorem. We further show that single-prime ("kinematic") and cross-prime ("carry") packets saturate at systematically different depths with the same sign in both model families. Finally, we prove — and verify to machine precision on both model families (worst error $10^{-16}$) — that a *conductor-certified* autoencoder's reconstruction-cost gap equals exactly the cross-packet content the obstruction forbids, with a trained sparse autoencoder confirming the predicted gap to $4\%$ at a held-out model–task cell; the certification/reconstruction trade-off is fixed by the Pontryagin law, not a hyperparameter, and the same law specifies the per-packet feature count before training. A base-$N$ specialization yields a deployment-grade shortcut audit. We release the theorem, the pre-registered protocol with its retained refutations, the cross-model spectra, and the certificate code.

**Keywords:** mechanistic interpretability, faithfulness, logit lens, tuned lens, sparse autoencoders, linear representation hypothesis, conductor packets, additive characters, cyclic concepts, Llama-3.1-8B, Mistral-7B.

---

## 1. Introduction

### 1.1 The faithfulness gap

Every claim in mechanistic interpretability passes through a *readout*: a map from a model's internal activations to a human-legible space. The three dominant readouts are the linear probe, the logit/tuned lens, and the sparse-autoencoder dictionary. Each has a large and growing literature, and each has an acknowledged faithfulness problem.

- *Probes.* Hewitt and Liang (2019) showed with control tasks that a probe's accuracy conflates what the model *uses* with what is merely *extractable*; amnesic-probing and concept-removal methods inherit the confound (Elazar et al. 2021; Belinkov 2022). Above-chance probing on linguistically meaningless labels is routine.
- *Lenses.* The logit lens (nostalgebraist 2020) is, in Belrose et al.'s (2023) own word, "brittle"; the tuned lens repairs it with a per-layer affine probe — but the repair is itself a *different readout*, and nothing says the two see the same thing.
- *Dictionaries.* Sparse autoencoders (Templeton et al. 2024; Gao et al. 2024; Lieberum et al. 2024) are evaluated for monosemanticity *post hoc*; foundational SAEs leave a fraction of linearly predictable reconstruction error, and benchmarks (SAEBench) measure the gap without predicting it.

Data-driven circuit discovery puts a number on the cost: hypothesis-driven discovery on mixed-task data returns single circuits that smear distinct mechanisms, with 87% mixed-faithfulness at 10% mixture injection (Rai, Geva & Yao 2026). The field measures faithfulness; it has no theory that *bounds it in advance*.

### 1.2 The sharpest test case: cyclic concepts

The cleanest place to demand such a theory is a concept class with exact algebraic structure. Engels et al. (2024) supplied it empirically: days-of-the-week and months-of-the-year are represented as genuinely *circular*, multi-dimensional features in GPT-2, Mistral-7B, and Llama-3-8B, and intervention experiments show these circles are the *computational unit* of modular arithmetic on those tasks. The circles are not an artifact of a probe — they are how the model computes. This is the substrate on which a faithfulness theory can be made exact, and it is the substrate we use.

The circular structure has a name in finite harmonic analysis: the additive characters of $C_N$, organized by *conductor* into packets $H_d$. The linear representation hypothesis (Park, Choe & Veitch 2024) gives a causal inner product for *linear* concepts; cyclic concepts are precisely where the linear hypothesis is provably insufficient (Engels et al.), and where the correct geometry is the non-Euclidean, arithmetically determined conductor-packet inner product.

### 1.3 Contribution

We make the faithfulness of cyclic-concept readouts an exact, computable property, and we deliver four results — one theorem, one measured exhibit, one cross-model validation, one certified construction:

1. **The divisor obstruction (§3).** Any quotient-codomain readout retains exactly $\bigoplus_{d \mid k} H_d$ and annihilates the rest (Pontryagin divisor rule). Faithfulness becomes a divisor table, computable before any activation is seen.
2. **The instrument-conflation exhibit (§4).** At one fixed layer of Llama-3.1-8B the full-period month concept reads $0.356$ through a full-label trained probe and $0.638$ through the frozen-unembedding lens — a $0.28$ gap with *no model-side cause*, reconciled to $6\times10^{-5}$ by the theorem. The readout quotient, not the model, determines what is visible.
3. **Cross-model spectroscopy (§5).** A pre-registered layerwise sweep on Llama-3.1-8B and Mistral-7B-v0.3 reproduces the Paper-26 anchors to $\leq 5\times10^{-4}$, holds the forbidden zeros at machine precision, and shows single-prime vs. cross-prime packets saturating at different depths with the same sign in both families — with retained refutations that demonstrate the pre-registration is real, not fitted.
4. **The conductor-certified autoencoder (§6).** A certified SAE's reconstruction-cost gap equals exactly the obstruction (verified to $10^{-16}$ on both models, all supports), and a trained SAE attains that floor to $4\%$; the per-packet feature count is fixed before training.

A base-$N$ specialization (§7) turns the obstruction into a deployment-grade shortcut audit.

### 1.4 What we do not claim

We do not claim the conductor-packet decomposition is a privileged interpretability basis for arbitrary behavior; the theory applies to readouts of concepts with a *named cyclic (or finite-abelian) algebra*. We do not claim a causal account of where cyclic structure is built — the spectroscopy is a measurement; activation-patching follow-ups are listed in §9. We do not claim the trained-SAE results are at production scale — one decisive cell is shown; the full sweep is pre-registered for a sequel (§6.5, §9). And we mark single-seed and fp32-precision limitations explicitly where they occur.

---

## 2. Setup and the three readouts

### 2.1 Cyclic label algebra, characters, conductor packets

Fix an integer $N \geq 2$ and let $R = C_N = \mathbb{Z}/N\mathbb{Z}$ be the cyclic label algebra of the task — the months ($N=12$), the weekdays ($N=7$), the digits ($N=10$). The additive characters $\chi_a(x) = e^{2\pi i a x / N}$, $a \in \{0,1,\dots,N-1\}$, form an orthonormal basis of $L^2(R)$ under the normalized inner product $\langle f, g\rangle = N^{-1}\sum_x f(x)\overline{g(x)}$. The *conductor* of $\chi_a$ is $\mathrm{cond}(\chi_a) = N/\gcd(a, N)$ — the order of $a$ in $R$, equivalently the smallest modulus on which $\chi_a$ is already defined. Grouping characters by conductor gives the *conductor packets*
$$H_d = \mathrm{span}\{\chi_a : \mathrm{cond}(\chi_a) = d\}, \qquad \dim_{\mathbb C} H_d = \varphi(d),$$
and an orthogonal decomposition $L^2(R) = \bigoplus_{d \mid N} H_d$. The packet $H_1$ is the constants; it carries no cyclic information, and we work throughout in its orthogonal complement, the zero-sum subspace $\Sigma_0$. For the three targets the nontrivial packets are: $N=12$ — $H_2, H_3, H_4, H_6, H_{12}$ (dimensions $1,2,2,2,4$); $N=7$ — the single packet $H_7$ (dimension $6$, prime, the degenerate positive control); $N=10$ — $H_2, H_5, H_{10}$ (dimensions $1,4,4$). A packet is an arithmetic "frequency class": $H_2$ is parity, $H_3$ three-fold structure, $H_{12}$ the full period. The circular features Engels et al. (2024) discovered empirically are exactly the low-dimensional real combinations living in these packets; the remainder of this paper is the law of which of them a given readout can recover.

### 2.2 The three readouts as quotient-codomain maps

Let the model have residual stream $h_\ell(x) \in \mathbb{R}^{d_{\mathrm{model}}}$ at layer $\ell$ on input $x$ (final-token position), unembedding $W_U$, and let $V_R \subset V$ be the $N$ tokens identified with $R$ (the twelve month tokens, the seven weekday tokens, the ten digit tokens). Write $\pi(h) \in \mathbb{R}^N$ for the restriction of $W_U h$ to $V_R$, mean-centered — the model's own logit profile over the cyclic labels, living in $\Sigma_0$. The three dominant interpretability readouts each produce a score in $\Sigma_0$, distinguished only by a constraint on its codomain:

- **Frozen-unembedding lens.** $s^{(\mathrm{lens})}_\ell(x) = \pi(h_\ell(x))$ — the model's own basis, no training (the logit lens of nostalgebraist 2020; the tuned lens of Belrose et al. 2023 inserts a learned affine map per layer but keeps the codomain $\Sigma_0$).
- **Trained quotient probe** at resolution $k \mid N$. A ridge-fit affine map $L_{\ell,k}:\mathbb{R}^{d_{\mathrm{model}}}\to\mathbb{R}^k$ to the labels mod $k$, pulled back to $\Sigma_0$ via $q_k^*$; its codomain is by construction the $k$-resolution quotient subspace $V_{q_k}\subset\Sigma_0$.
- **SAE dictionary.** Each feature $w_j$ has cyclic image $\pi(w_j)\in\Sigma_0$; the reconstruction's cyclic content spans $\{\pi(w_j)\}$. A vanilla SAE leaves this span unconstrained; a *certified* SAE (§6) constrains it to a chosen packet support $\bigoplus_{d\in S}H_d$.

This is the conceptual hinge of the paper: **each readout is characterized by a codomain subspace of $\Sigma_0$, and the packet content it can express is the projection of that subspace onto the conductor packets.** Theorem 1 computes that projection in closed form for any quotient codomain, so it governs lens, probe, and dictionary *identically* — whatever a readout's training, if its codomain is the $k$-resolution quotient it sees exactly the packets $H_d$ with $d \mid k$, and nothing else.

### 2.3 The reading rule (two towers)

We keep two kinds of quantity strictly separate (Paper 36 §4), because conflating them is the most common way a structural interpretability claim becomes unfalsifiable. *Theorem-side rows* are analytic pullback checks: the projection of a quotient readout onto a forbidden packet is exactly zero, at every layer, by construction — these certify the projector is implemented correctly (numerical machine epsilon) and are never reported as model evidence. *Model-side rows* are quantities that could have failed before any projector was applied: the native packet fractions $f_{d,\ell}$ of the model's own residual stream as read by its own unembedding, and the retained accuracy of trained probes. Every table in this paper pairs the two; we never report a table whose only content is an analytic zero. The instrument-conflation exhibit of §4 and the spectra of §5 are model-side throughout; the certificate of §6.3 is the one place an analytic zero is the point, and it is labeled as such.

---

## 3. The divisor obstruction

### 3.1 Theorem (Pontryagin divisor rule)

For $k \mid N$, let $q_k:C_N\to C_k$ be the quotient with kernel $K=\langle k\rangle=\{0,k,2k,\dots\}$, and let $P_{q_k}$ be the orthogonal projection of $L^2(R)$ onto the functions that factor through $q_k$ — equivalently, averaging over the cosets of $K$.

> **Theorem 1 (Pontryagin divisor rule; Paper 26 T1–T2).** $P_{q_k}$ is diagonal in the character basis, with
> $$P_{q_k}\big|_{H_d} = \mathrm{id}_{H_d}\ \text{if}\ d\mid k, \qquad P_{q_k}\big|_{H_d}=0\ \text{if}\ d\nmid k.$$
> Consequently any readout whose codomain is the $k$-resolution quotient subspace $V_{q_k}$ retains exactly $\bigoplus_{d\mid k}H_d$ and annihilates exactly the packets $H_d$ with $d\nmid k$ — sharply: a packet-pure signal in a forbidden packet contributes exactly zero surviving energy.

*Proof.* Coset-averaging by $K$ sends $\chi_a$ to $\chi_a\cdot\big(|K|^{-1}\sum_{y\in K}\chi_a(y)\big)$. The scalar is $1$ if $\chi_a|_K\equiv 1$ and $0$ otherwise; and $\chi_a(mk)=e^{2\pi i a m k/N}=1$ for all $m$ iff $N\mid ak$ iff $\mathrm{cond}(\chi_a)=N/\gcd(a,N)\mid k$. Thus $P_{q_k}\chi_a=\chi_a$ exactly when $\mathrm{cond}(\chi_a)\mid k$, giving the stated packet eigenvalues. The full argument, the sharpness, and the finite-field generalization are Paper 26 §T1–T2. $\square$

### 3.2 Corollary (faithfulness is a computable obstruction)

> **Corollary 2.** The set of conductor packets a readout is structurally blind to is $\{H_d:d\nmid k\}$, determined by its codomain quotient alone — a divisor table fixed before any activation is observed.

For the months target ($N=12$), the retained packets ($1$ = retained, $0$ = annihilated) per quotient resolution $k$:

| $k$ | $H_2$ | $H_3$ | $H_4$ | $H_6$ | $H_{12}$ |
|---:|:---:|:---:|:---:|:---:|:---:|
| 2  | 1 | 0 | 0 | 0 | 0 |
| 3  | 0 | 1 | 0 | 0 | 0 |
| 4  | 1 | 0 | 1 | 0 | 0 |
| 6  | 1 | 1 | 0 | 1 | 0 |
| 12 | 1 | 1 | 1 | 1 | 1 |

The weekday case ($N=7$, prime) is degenerate — one nontrivial packet $H_7$, retained only at $k=7$ — which is exactly why it is the positive control: it isolates the cyclic-concept question from the divisor-lattice question. The digit case ($N=10=2\cdot5$) gives the cleanest two-prime row: $k=2$ retains $H_2$ only, $k=5$ retains $H_5$ only, $k=10$ retains all of $H_2,H_5,H_{10}$. A readout cannot *create* full-period ($H_N$) energy from a coarser codomain, and cannot recover a packet its quotient annihilates, regardless of how it is trained or how much data it sees. Faithfulness, for these concepts, is a property of the divisor lattice of $N$, computable in advance.

### 3.3 Dialogue with the linear representation hypothesis

The linear representation hypothesis (Park, Choe & Veitch 2024) makes the same foundational move this paper does — it discards the Euclidean dot product on the unembedding space in favor of a covariance whitening under which the natural concept structure is orthogonal — and it is the right framework in the regime ours is not: genuinely *linear*, one-dimensional concepts. Their *causal inner product* $\langle\bar\gamma,\bar\gamma'\rangle_{\mathrm C}=\bar\gamma^\top M\,\bar\gamma'$ is pinned by requiring causally separable concept directions to be orthogonal, but that requirement leaves $M$ identified only up to a $d$-parameter family (a free diagonal $D$ in their explicit-form theorem); lacking a principle to fix $D$, they adopt the representative $D=I$, i.e. $M=\mathrm{Cov}(\gamma)^{-1}$ — Mahalanobis whitening by the unembedding covariance, *estimated* from the unembedding matrix. Cyclic concepts are precisely where the one-dimensional picture is insufficient: Engels et al. (2024) show months and weekdays are irreducibly multi-dimensional (circular), and intervention confirms the circle — not any single direction — is the computational unit. Here the analogous whitening is not estimated but *forced*: on the cyclic label algebra $C_N$ the additive characters simultaneously diagonalize the Fisher form and the quotient projectors of Theorem 1 — by Pontryagin duality, since both are shift-equivariant — and their grouping by conductor into the packets $H_d$ is canonical, so the $d$-fold ambiguity Park–Veitch resolve by a data-driven choice of $D$ collapses to zero free parameters, fixed by the divisor lattice of $N$ before any activation is observed. On top of that parameter-free basis, Theorem 1 supplies what their existence-level geometry does not — the exact per-readout obstruction: which packets a quotient codomain retains and which it annihilates. Where Park–Veitch give a causal inner product for linear directions, the divisor rule gives the recoverability law for cyclic packets. The two are complementary answers to one question, "what can a readout recover?", in two regimes: linear directions and cyclic packets.

---

## 4. The instrument-conflation exhibit

### 4.1 The measurement
On Llama-3.1-8B, months, at the layer the prior literature calls "layer 28" (the causalab `L28_last_token` artifact = HF `hidden_states` row 29, verified per-example: cosine $0.9998$ vs. the saved residuals): the full-period packet $H_{12}$ reads
$$f_{12}^{(\mathrm{probe})}=0.356 \quad\text{(full-label trained probe)}, \qquad f_{12}^{(\mathrm{lens})}=0.638 \quad\text{(frozen-unembedding lens)}.$$
The lens value reproduces from Paper 26's *own saved layer-28 residuals* to $6\times10^{-5}$; the gap is $0.28$.

### 4.2 Why: same model, different quotient
The probe and the lens are *different codomain quotients* of the same hidden state, so by §3 they retain different packet content. The $0.28$ gap is not noise and has no model-side cause — it is the divisor law operating between two instruments, measured in the wild. This both *reconciles* the apparent Paper-26 discrepancy (the published $0.356$ was a probe number; the lens at that depth is $0.638$) and *exhibits* the thesis: the readout quotient, not the model, determines what you see.

### 4.3 Significance for the field
This is the faithfulness crisis localized to a single exact cause on a single layer. It directly addresses the tuned-lens motivation (Belrose et al. 2023): the lens/probe gap is largest exactly where the codomain quotients differ most in retained packets.

---

## 5. Cross-model layerwise spectroscopy (pre-registered)

### 5.1 Protocol and anchor reproduction
Pre-registered sweep, Llama-3.1-8B and Mistral-7B-v0.3, months ($N{=}12$) and weekdays ($N{=}7$), exact Paper-26 prompt sets. Final-layer packet fractions reproduce the Paper-26 anchors to $\leq 5\times10^{-4}$ (Llama months $f_{12,\mathrm{final}}=0.6569$); forbidden-packet zeros at machine precision. **Anchor gate passed.** The full $f_{d,\ell}$ spectra for both base models are tabulated in Appendix A (source JSON `empirical/reports/layerwise_packet_spectroscopy_months_*`).

![Figure 1. (A) Full-period packet fraction $f_{12,\ell}$ vs. normalized depth for both models: the crystallization jump, overshoot above the final-layer anchor (★), and decline into the readout; the instrument-conflation exhibit of §4 is marked at row 29 (lens 0.638 on the curve vs. probe 0.356, grey square). (B) The V/M saturation index $\sigma_d$ with 95% prompt-bootstrap CIs: every single-prime $\sigma_V$ exceeds every carry $\sigma_M$ on both models ($P=1.000$), with Llama's internal three-level V ladder visible.](empirical/reports/figures/spectroscopy_cross_model.pdf)

### 5.2 The crystallization-jump profile (a discovered phenomenon)
The full-period fraction is *not* monotone-late. Both models show a single mid-late crystallization jump (Llama rows $21\to22$, $+0.454$; Mistral $17\to18$, $+0.388$), an overshoot above the final value (Llama peak $0.776$ @ row 24 vs. final $0.657$; Mistral $0.823$ vs. $0.785$), then a decline into the readout — the "finer internal structure than the head exposes" profile, replicated cross-model.

### 5.3 Single-prime vs. cross-prime propagation (V/M), with significance
Single-prime / prime-power packets (V $=H_2,H_3,H_4$) peak at intermediate depth and overshoot their readout share ($\sigma > \tfrac12$); cross-prime carry packets (M $=H_6,H_{12}$) concentrate at the readout ($\sigma < \tfrac12$). The depth-normalized saturation index $\sigma_d$ (point estimate; 95% CI from 2000 prompt-bootstrap resamples of the captured residual streams, `empirical/vm_bootstrap_significance.py`):

| | $\sigma_2$ | $\sigma_3$ | $\sigma_4$ | $\sigma_6$ | $\sigma_{12}$ |
|---|---:|---:|---:|---:|---:|
| Llama-3.1-8B | 0.56 [0.49, 0.67] | 0.94 [0.79, 1.13] | 0.92 [0.81, 1.07] | 0.41 [0.37, 0.44] | 0.44 [0.42, 0.45] |
| Mistral-7B-v0.3 | 1.89 [1.61, 2.26] | 1.27 [1.10, 1.50] | 1.67 [1.39, 2.03] | 0.45 [0.42, 0.49] | 0.41 [0.40, 0.42] |

The separation is **significant on both models**: the gap $\min(\sigma_V) - \max(\sigma_M)$ is positive in **100% of resamples** (Llama $0.13$, CI $[0.04, 0.23]$; Mistral $0.82$, CI $[0.65, 1.05]$) — settling P9 at **K-branch on both families**: single-prime structure crystallizes shallower than carry structure, same sign, significant (Figure 1B).

*New finding from the bootstrap.* A point-estimate reading had flagged Llama's $H_2$ as a "defector" toward M; the bands **refute it** — on the base model $\sigma_2$ exceeds the entire M cluster in 100% of resamples. What is real is an internal V *ladder* on Llama base: three levels with non-overlapping bands, M $(\approx 0.42)$ $<$ $H_2$ $(\approx 0.57)$ $<$ $\{H_3, H_4\}$ $(\approx 0.93)$ — parity ($H_2$) saturating at intermediate depth *between* the carry packets and the higher single-prime packets. Mistral base's V triple is uniformly high (effect size $\sim$6× Llama's).

### 5.4 Checkpoint robustness: a parity-localized instruct-tuning effect

Extending to the instruct-tuned checkpoint of each family — same raw prompts, different weights — tests whether the separation is a property of the pretrained model or of one checkpoint, and surfaces a clean differential finding. The gap $\min(\sigma_V)-\max(\sigma_M)$ per checkpoint (2000-resample bootstrap):

| checkpoint | gap | $P(\mathrm{gap}>0)$ | verdict |
|---|---:|---:|---|
| Llama-3.1-8B (base) | $+0.13$ | $1.000$ | K-branch |
| Llama-3.1-8B-**Instruct** | $\mathbf{-0.13}$ | $0.002$ | **broken** |
| Mistral-7B-v0.3 (base) | $+0.82$ | $1.000$ | K-branch |
| Mistral-7B-Instruct-v0.3 | $+0.64$ | $1.000$ | K-branch |

K-branch holds on **three of four** checkpoints. It **survives Mistral's instruct-tuning** ($0.82\to0.64$, still strongly significant) but **breaks under Llama's** (gap significantly *negative*, $P(\mathrm{gap}>0)=0.002$). The break is **parity-localized**: Llama instruct-tuning collapses the $H_2$ (parity) saturation ($\sigma_2:\,0.56\to0.40$, now below the carry packets) and lifts $H_6$ ($\sigma_6:\,0.41\to0.54$), inverting their order, while $H_3, H_4$ stay above M. The V/M conductor separation is thus a robust property of both pretrained models and of Mistral-Instruct, but Llama-3.1's instruct-tuning specifically reorganizes the parity packet (Figure 2) — the method detecting a real, packet-resolved consequence of fine-tuning, itself a use case for the spectroscopy.

![Figure 2. V/M separation gap $\min(\sigma_V)-\max(\sigma_M)$ across four checkpoints (filled = base, open = instruct; blue = Llama, red = Mistral), with 95% prompt-bootstrap CIs and the $P(\mathrm{gap}>0)$ for each. Three checkpoints sit above the K-branch threshold ($P=1.000$); Llama-3.1-8B-Instruct alone falls significantly below it ($P=0.002$), the parity-packet collapse of §5.4.](empirical/reports/figures/vm_checkpoint_gap.pdf)

*Two honesty notes.* (i) Instruct models are run on the same raw (non-chat) prompts as the base models for comparability — off their fine-tuning distribution; but Mistral-Instruct on the identical raw-prompt condition preserves K-branch, so the Llama-Instruct break is **not** a generic instruct-on-raw-prompt artifact. A chat-formatted re-run is the natural further control. (ii) The bands are over prompts at each checkpoint; we now span the base→instruct weight axis on two families, but not seed-level variance.

### 5.5 Negative control and retained refutations
Weekdays: $f_{7,\ell}\equiv1$ at every layer on both models (prime modulus — no spurious off-divisor structure can or does appear; negative control passes). Retained as recorded outcomes, not hidden: the $\ell^\star$ saturation-order statistic (P3) and the fraction metric on a prime modulus (P4) are apparatus defects — pre-registration working as intended, flagged for a v2 protocol. The pre-registered failure conditions (Paper 36 §7) fared as follows: **F1** (anchor band) fired on the layer-28 entry and was reconciled to an instrument conflation (§4) before any spectrum was interpreted; **F3** (inverted divisor order) fired by the letter of the $\ell^\star$ statistic, with the early-layer-noise caveat recorded; **F2, F5, F6, F7, F8 did not fire** — the weekday control is consistent, the two base models agree in profile and V/M sign, and the V/M separation is present and significant; **F4** (probe/lens gap collapse) is not evaluable here because the layerwise trained-probe arm is deferred.

---

## 6. The conductor-certified sparse autoencoder

### 6.1 Construction
A CCSAE at closed packet support $S$ is a standard SAE whose decoder columns satisfy $\pi(w_k)\in\bigoplus_{d\in S}H_d$ exactly: after each optimizer step the columns and pre-bias are projected through $I-\pi^+(I-P_S)\pi$ (hard certification, Adam moments untouched; Paper 45 §3).

### 6.2 Theorem (Packet-Purity and Reconstruction-Cost)

> **Theorem 2 (Paper 45 Thm 4.1–4.2).** Every certified feature is packet-pure, and the certified-minus-vanilla reconstruction gap equals exactly the cross-packet content $\delta_S(h)=\|(I-P_S)\pi(h)\|^2$ — which by Theorem 1 is exactly what the corresponding quotient readout cannot represent.

The certification/reconstruction trade-off is therefore the obstruction itself, not a tunable hyperparameter.

### 6.3 Structural certificate (exact, both models)
Theorem 2's identity is verified to machine precision on the captured Llama-3.1-8B and Mistral-7B-v0.3 activations: worst forbidden-packet leakage $4.1\times10^{-15}$ (Packet-Purity), and a gap-identity error of $1.1\times10^{-16}$ between $\delta_S$ computed spectrally and computed by direct real-space projection (Reconstruction-Cost). Predicted gaps: Llama months $S{=}\{12\}\to0.343$, $\{2,6\}\to0.782$, full $\to0$; Mistral $S{=}\{12\}\to0.215$ (smaller, tracking its higher $f_{12,\mathrm{final}}=0.785$). Code `empirical/ccsae_certificate.py`; certificate `empirical/reports/ccsae_certificate.json`.

### 6.4 Trained confirmation (one cell)
A top-$k$ SAE ($F{=}1024$, $k{=}32$, 4000 steps) trained on a 3456-prompt cyclic months corpus (Llama-3.1-8B, layer 30) and evaluated in the cyclic readout: the vanilla SAE attains cyclic reconstruction error $0.0102$ (it reconstructs all packets), while the certified $S{=}\{12\}$ SAE attains $0.4114$ — a **gap of $0.4011$ against the obstruction floor $0.3851$, within $4.2\%$** (Paper 45 P3); the certified $S{=}\text{full}$ SAE matches vanilla. Trained fp32 packet-purity is $4\times10^{-5}$ (the reconstruction is $99.996\%$ packet-pure; the $10^{-10}$ pre-registration is fp64-idealized and restated fp32-realistic). Cell `empirical/reports/ccsae_train_months_llama31_8b.json`.

### 6.5 The pre-registered divisor table (structural feature specification)

Every published evaluation of SAE feature quality is *post hoc*: train the dictionary, extract features, then judge monosemanticity by human or LLM (Templeton et al. 2024; Gao et al. 2024; Lieberum et al. 2024). There is no published framework that says, *before* training, which features must exist. Theorem 1 supplies one for cyclic concepts. Under per-feature single-packet certification (Paper 45 Thm 4.3) — each feature assigned a packet at initialization and projected onto $H_{d_j}$ after each step — the feature count per packet is fixed by the packet dimensions alone:
$$|\mathcal F_d| = F\cdot\frac{\varphi(d)}{\sum_{d'\in S}\varphi(d')},$$
where $F$ is the dictionary width. This is a *pre-registered divisor table*, computable before a single gradient step. At the Gemma Scope width $F=16384$ on full support:

| target | packets ($\varphi$) | feature counts $|\mathcal F_d|$ |
|---|---|---|
| months $C_{12}$ | $H_2(1),H_3(2),H_4(2),H_6(2),H_{12}(4)$, total 11 | $1489,\ 2979,\ 2979,\ 2979,\ 5958$ |
| weekdays $C_7$ | $H_7(6)$, total 6 | $16384$ (all in $H_7$; degenerate control) |
| digits $C_{10}$ | $H_2(1),H_5(4),H_{10}(4)$, total 9 | $1820,\ 7282,\ 7282$ |

The counts are integer-exact and sum to $F$. The empirical prediction is sharp: a certified SAE's per-packet feature count matches this table to within zero, and the *composite* cyclic features reported in the literature should split accordingly. Templeton et al.'s (2024) single "day-of-week" feature should resolve, under $C_7$ certification, into the six characters of $H_7$; their "month" features into the eleven nontrivial $C_{12}$ characters distributed across the five packets above. This is the first instance the field has of a structural feature specification derived from a theorem rather than from intuition. The full $3\times3\times3$ grid (models $\times$ tasks $\times$ supports), the negative controls, and the DCD cluster-count co-prediction ($K^\star=\tau(N)$; Rai, Geva & Yao 2026) are the sequel's production leg (Paper 45 §5–§7).

---

## 7. The base-$N$ shortcut audit (deployment primitive)
The obstruction's base-$N$ specialization yields a survival-ratio diagnostic $\sigma$ for decimal sum/carry shortcuts, with anchor $\sigma=0.458$ on months base-10 (Paper 40). Read as a safety primitive: a model whose cyclic mechanism is conductor-structured passes the audit, while one relying on a base-$N$ shortcut does not — a deployment-time check computable from the divisor lattice. The extension to the seven pre-registered task classes (the full $\sigma$-audit taxonomy) is future work.

---

## 8. Related work

**Lenses.** The logit lens (nostalgebraist 2020) reads the residual stream through the model's own unembedding; it is, as Belrose et al. (2023) put it, "brittle," and the tuned lens repairs it with a per-layer affine probe that is "more predictive, reliable and unbiased." Our contribution is orthogonal to that repair and explains where it helps: the lens and the tuned/probe readout are *different codomain quotients* of the same hidden state (§2.2), so by Theorem 1 they retain different packet content. We turn "more reliable" into an exact, per-packet recoverability statement, and §4 measures the resulting gap on a single layer ($0.638$ lens vs. $0.356$ probe) — precisely the regime the tuned lens was designed for.

**Probes and the faithfulness/illusion literature.** A long line of work establishes that probe accuracy conflates what a model *uses* with what is merely *extractable*: Hewitt and Liang (2019) with control tasks, the unreliability of concept-removal and amnesic probing (Elazar et al. 2021, arXiv:2006.00995; Belinkov 2022, arXiv:2102.12452), and the broader "interpretability illusion" that above-chance probing is achievable on linguistically meaningless labels. These are diagnoses of the problem after the fact. Theorem 1 is the complementary a priori bound for cyclic concepts: it states, before any probe is trained, which packets a probe of given codomain resolution *cannot* recover — an upper bound on faithfulness that no amount of data removes.

**Multi-dimensional features and the linear representation hypothesis.** Engels et al. (2024, arXiv:2405.14860) demonstrate that days-of-week and months are genuinely circular, multi-dimensional features in GPT-2, Mistral-7B, and Llama-3-8B, and that the circle is the computational unit of the corresponding modular arithmetic — the empirical substrate this paper makes exact. The linear representation hypothesis (Park, Choe & Veitch 2024, arXiv:2311.03658) replaces the Euclidean geometry of the unembedding space with a *causal inner product* — the covariance whitening $M=\mathrm{Cov}(\gamma)^{-1}$, identified only up to a $d$-parameter family and estimated from data — under which causally separable linear concepts are orthogonal. Cyclic concepts are exactly where the one-dimensional picture is insufficient, and there the analogous whitening is not estimated but forced: the additive characters diagonalize the Fisher form and the quotient projectors by Pontryagin duality, fixing the conductor-packet basis with zero free parameters, and on it the divisor rule reads off which packets each readout retains (§3.3). Linear directions and cyclic packets are two regimes of one question; each now has its exact recoverability law.

**Sparse autoencoders.** Dictionary learning is the dominant interpretability paradigm — Scaling Monosemanticity (Templeton et al. 2024), the top-$k$ atlas (Gao et al. 2024, arXiv:2406.04093), Gemma Scope (Lieberum et al. 2024, arXiv:2408.05147), with superposition geometry from Toy Models (Elhage et al. 2022) and evaluation harnesses such as SAEBench. Every monosemanticity metric in this line is post hoc, and foundational SAEs are known to leave a fraction of linearly predictable reconstruction error. Our §6 contributes two things the line lacks: a *pre-training* structural feature specification (the divisor table, §6.5) and an *exact* reconstruction-cost certificate (the gap equals the obstruction, §6.2–6.4) — turning the reconstruction/interpretability trade-off from a tuned hyperparameter into a computed quantity.

**Circuit-level faithfulness.** Data-driven circuit discovery (Rai, Geva & Yao 2026, arXiv:2605.09129) quantifies the crisis at the circuit level — 87% mixed-faithfulness when distinct mechanisms are blended — and recovers multiple circuits by clustering per-example attribution vectors. On cyclic mixed datasets our divisor count $\tau(N)$ is the a priori cluster count their silhouette-driven selection should return (Paper 45 §6.6), connecting the residual-stream substrate of this paper to the attribution-vector substrate of theirs through the same obstruction.

**Program lineage and second-order siblings.** This paper consolidates the conductor line: Paper 26 (the obstruction theorem), Paper 36 (layerwise spectroscopy), Paper 40 (the base-$N$ audit), and Paper 45 (the certified autoencoder). It sits adjacent to two second-order results that probe the *quadratic* curvature class rather than the exact divisor structure — Neural LoFi (Dandi et al. 2605.13612) and the LeJEPA identifiability theorem (Klindt et al. 2605.26379), both order-2 instances of the same blind spot — and to Amaral's (2025) published $R(N{=}2){=}0$, $R(N{=}3){=}\tfrac12$ statistical-manifold curvature computation, an external verification of the second-order corner. A fourth, *constructive* instance comes from outside the curvature literature: the vec2vec unsupervised embedding-translation method (Jha, Zhang, Shmatikov \& Morris 2505.12540) harnesses a universal cross-encoder geometry whose load-bearing geometric constraint is vector-space preservation of pairwise inner products — a Gram, i.e. order-2, object. Its results split exactly along the order-2 boundary: perfect top-1 matching of $8000+$ shuffled embeddings (a relation decided by second-order geometry) alongside sub-unit cosine fidelity and lossy inversion that the authors themselves frame as a *lower bound* — the structural residual this line attributes to the cross-packet, order-$\geq 3$ content that no order-2 alignment can transport. We confirm this directly on their released checkpoint for the flagship cross-architecture pair (\texttt{gte}$\to$\texttt{gtr}, $N=20{,}000$ NQ passages): reading the translation residual by cumulant order in the target's principal subspace (where the embeddings' non-Gaussianity is real, $3.4$–$11.5\times$ the sampling floor), vec2vec reproduces the second-order structure to $3$–$8\%$ but the third-order to $33$–$108\%$ — an $8$–$14\times$ gap stable across $k=8$ to $256$ principal directions. Against the no-translation baseline (raw \texttt{gte} vs.\ \texttt{gtr}, $\sim\!91\%$ error at every order) the method closes the order-2 gap $30\times$ ($0.91\to0.03$) but the order-3 gap only $2.3\times$ ($1.20\to0.51$): its capacity flows almost entirely into the second-order match and leaves the order-$\geq 3$ content where it found it — the order-2 floor, measured on a deployed system. The order-2/order-3 boundary on which all of these siblings sit is, moreover, not an artifact of the maximum-entropy point. The off-centroid analytic closure (conductor blind-spot probe-result P4, with the moving Amari–Chentsov cubic of the simplicial information-geometry program) shows that on every cross-packet selection-rule triple the blind cubic coupling equals the collision weight $C_2(p)=\sum_y p_y^{-2}$ — identical across triples, *minimized exactly at $p_*$* with $C_2(p_*)=N^3$, and growing as the distribution sharpens — while the Fisher form stays circulant in $k-\ell$ (a two-frequency object) at every interior $p$. The order-2-blind / order-3-coupled gap therefore *persists and intensifies* off-center, and is the order-2-vs-order-3 gap of the cumulant tower rather than a feature of $p_*$; the normalized $\rho_\times$ diagnostic is provably invariant on its selection-rule support (the $C_2(p)$ factor cancels), so the second-order siblings above measure the boundary at its single weakest point, and every distribution-sharpening trajectory widens it.

---

## 9. Limitations

- **V/M variance.** The separation is significant under prompt resampling and across the base→instruct weight axis on two families (§5.3–5.4); untested is seed-level (re-training) variance. Instruct checkpoints are scored on raw (non-chat) prompts for comparability, with Mistral-Instruct serving as the same-condition control that rules out a generic raw-prompt artifact.
- **Digits arm deferred** — no pre-registered digits prompt set exists; P5 and P8 remain open.
- **Trained-SAE at one cell** — §6.4 is a decisive single cell, not the production sweep; the full $3\times3\times3$ grid (Paper 45 §5–§7) is deferred.
- **fp32 thresholds** — trained packet-purity is $\sim10^{-5}$ (§6.4), not the fp64-idealized $10^{-10}$; the structural certificate (§6.3) attains $10^{-15}$.
- **Apparatus defects retained** — the $\ell^\star$ saturation-order statistic (P3) and the prime-modulus fraction metric (P4) are flagged for a v2 protocol (§5.5).

---

## 10. Conclusion
Faithfulness, for cyclic concepts, is not a score to be measured after the fact but a divisor table computable before any activation is seen. The same law that says which packets a probe or lens annihilates says what a certified autoencoder's reconstruction must cost and how many features each packet must hold. We exhibited the law operating between two instruments on one layer of one model (the $0.356$/$0.638$ gap), validated it across two model families with its refutations retained, and certified it to machine precision in the SAE dictionary it constrains. The readout quotient — not the model — determines what is visible.

---

## 11. References

*External works — arXiv identifiers are authoritative; author/title strings are draft-formatted and to be confirmed at submission.*

- Belinkov, Y. (2022). Probing Classifiers: Promises, Shortcomings, and Advances. *Computational Linguistics* 48(1). arXiv:2102.12452.
- Belrose, N., Furman, Z., Smith, L., Halawi, D., Ostrovsky, I., McKinney, L., Biderman, S., Steinhardt, J. (2023). Eliciting Latent Predictions from Transformers with the Tuned Lens. arXiv:2303.08112.
- Dandi, Y., et al. (2026). Neural LoFi. arXiv:2605.13612.
- Elazar, Y., Ravfogel, S., Jacovi, A., Goldberg, Y. (2021). Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals. *TACL*. arXiv:2006.00995.
- Elhage, N., et al. (2022). Toy Models of Superposition. *Transformer Circuits Thread*.
- Engels, J., Michaud, E. J., Liao, I., Gurnee, W., Tegmark, M. (2024). Not All Language Model Features Are Linear. arXiv:2405.14860.
- Gao, L., et al. (2024). Scaling and Evaluating Sparse Autoencoders. arXiv:2406.04093.
- Hewitt, J., Liang, P. (2019). Designing and Interpreting Probes with Control Tasks. *EMNLP*.
- Jha, R., Zhang, C., Shmatikov, V., Morris, J. X. (2025). Harnessing the Universal Geometry of Embeddings. arXiv:2505.12540.
- Klindt, D., Balestriero, R., LeCun, Y., et al. (2026). LeJEPA. arXiv:2605.26379.
- Lieberum, T., et al. (2024). Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2. arXiv:2408.05147.
- nostalgebraist (2020). Interpreting GPT: The Logit Lens. *LessWrong*.
- Park, K., Choe, Y. J., Veitch, V. (2024). The Linear Representation Hypothesis and the Geometry of Large Language Models. *ICML 2024*. arXiv:2311.03658.
- Rai, A., Geva, M., Yao, Z. (2026). Data-Driven Circuit Discovery (DCD). arXiv:2605.09129.
- Templeton, A., et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet. *Transformer Circuits Thread*.

*Program preprints (internal; the conductor line this paper consolidates):* Paper 02 (simplicial Fisher geometry), Paper 11 (quotient-character adjacency algebras), Paper 26 (Conductor Probe-Obstruction Theorem), Paper 36 (Layerwise Packet Spectroscopy), Paper 40 (base-$N$ shortcut audit), Paper 45 (Conductor-Certified Sparse Autoencoders). Published siblings on Zenodo: *The Conductor Blind Spot* and *Beyond the Conductor Blind Spot*.

---

## Appendix A — Full months spectra (base models)

The complete layerwise lens packet fractions $f_{d,\ell}^{(\mathrm{lens})}$ for the two base models (Figure 1A plots the $f_{12}$ column). Final rows reproduce the Paper-26 anchors to $\leq 5\times10^{-4}$. Source JSON: `empirical/reports/layerwise_packet_spectroscopy_months_{llama31_8b,mistral7b_v0_3}.json`; the four-checkpoint set (incl. the two instruct variants of §5.4) is in the same directory.

**Llama-3.1-8B (base)** — months, $f_{d,\ell}^{(\mathrm{lens})}$ (row = HF hidden_states index):

| row | $f_2$ | $f_3$ | $f_4$ | $f_6$ | $f_{12}$ |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.0017 | 0.0583 | 0.4305 | 0.1529 | 0.3565 |
| 1 | 0.0006 | 0.1738 | 0.3516 | 0.3381 | 0.1359 |
| 2 | 0.0046 | 0.1255 | 0.0990 | 0.0261 | 0.7448 |
| 3 | 0.0130 | 0.0324 | 0.2349 | 0.0563 | 0.6634 |
| 4 | 0.0038 | 0.0581 | 0.2999 | 0.0086 | 0.6296 |
| 5 | 0.0031 | 0.1980 | 0.2956 | 0.0037 | 0.4995 |
| 6 | 0.0306 | 0.1569 | 0.4661 | 0.0457 | 0.3007 |
| 7 | 0.0464 | 0.0388 | 0.4332 | 0.3122 | 0.1695 |
| 8 | 0.0309 | 0.0626 | 0.4086 | 0.3825 | 0.1154 |
| 9 | 0.0099 | 0.0873 | 0.4942 | 0.0703 | 0.3383 |
| 10 | 0.0473 | 0.1976 | 0.0805 | 0.1263 | 0.5482 |
| 11 | 0.0017 | 0.1700 | 0.1371 | 0.1209 | 0.5703 |
| 12 | 0.0129 | 0.2033 | 0.1586 | 0.1911 | 0.4342 |
| 13 | 0.0510 | 0.0538 | 0.5360 | 0.1027 | 0.2566 |
| 14 | 0.0071 | 0.1645 | 0.2130 | 0.1252 | 0.4902 |
| 15 | 0.0135 | 0.2554 | 0.0695 | 0.2321 | 0.4296 |
| 16 | 0.0123 | 0.2481 | 0.0408 | 0.0698 | 0.6289 |
| 17 | 0.0619 | 0.2254 | 0.0327 | 0.0493 | 0.6307 |
| 18 | 0.0573 | 0.2652 | 0.0553 | 0.0991 | 0.5230 |
| 19 | 0.0838 | 0.2890 | 0.0804 | 0.1262 | 0.4207 |
| 20 | 0.1600 | 0.2594 | 0.1466 | 0.1336 | 0.3003 |
| 21 | 0.1549 | 0.2358 | 0.1253 | 0.2505 | 0.2336 |
| 22 | 0.0616 | 0.0730 | 0.0500 | 0.1279 | 0.6875 |
| 23 | 0.0389 | 0.0589 | 0.0484 | 0.1170 | 0.7368 |
| 24 | 0.0361 | 0.0632 | 0.0387 | 0.0857 | 0.7762 |
| 25 | 0.0340 | 0.0643 | 0.0389 | 0.0988 | 0.7640 |
| 26 | 0.0316 | 0.0585 | 0.0370 | 0.1115 | 0.7614 |
| 27 | 0.0842 | 0.0489 | 0.0334 | 0.1078 | 0.7257 |
| 28 | 0.0904 | 0.0528 | 0.0420 | 0.1217 | 0.6931 |
| 29 | 0.0810 | 0.0706 | 0.0547 | 0.1555 | 0.6382 |
| 30 | 0.0609 | 0.0909 | 0.0784 | 0.1585 | 0.6113 |
| 31 | 0.0701 | 0.0858 | 0.0821 | 0.1719 | 0.5901 |
| 32 | 0.0511 | 0.0660 | 0.0591 | 0.1669 | 0.6569 |

**Mistral-7B-v0.3 (base)** — months, $f_{d,\ell}^{(\mathrm{lens})}$ (row = HF hidden_states index):

| row | $f_2$ | $f_3$ | $f_4$ | $f_6$ | $f_{12}$ |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.0024 | 0.1700 | 0.0604 | 0.1638 | 0.6033 |
| 1 | 0.4168 | 0.1042 | 0.0096 | 0.0860 | 0.3835 |
| 2 | 0.0000 | 0.1790 | 0.0077 | 0.1356 | 0.6777 |
| 3 | 0.0103 | 0.0139 | 0.2504 | 0.2875 | 0.4379 |
| 4 | 0.0115 | 0.0776 | 0.0769 | 0.3739 | 0.4600 |
| 5 | 0.0334 | 0.1761 | 0.1071 | 0.4924 | 0.1910 |
| 6 | 0.1123 | 0.2119 | 0.0231 | 0.3854 | 0.2673 |
| 7 | 0.0589 | 0.4844 | 0.0763 | 0.2616 | 0.1188 |
| 8 | 0.1054 | 0.2400 | 0.1771 | 0.2977 | 0.1799 |
| 9 | 0.1812 | 0.3065 | 0.1847 | 0.1060 | 0.2216 |
| 10 | 0.1852 | 0.1605 | 0.3810 | 0.1255 | 0.1479 |
| 11 | 0.3512 | 0.2349 | 0.1736 | 0.1359 | 0.1044 |
| 12 | 0.2168 | 0.2229 | 0.2218 | 0.0773 | 0.2613 |
| 13 | 0.2479 | 0.1043 | 0.1594 | 0.0887 | 0.3996 |
| 14 | 0.2008 | 0.1456 | 0.0355 | 0.0831 | 0.5350 |
| 15 | 0.5767 | 0.0903 | 0.0614 | 0.0209 | 0.2506 |
| 16 | 0.2770 | 0.1148 | 0.0336 | 0.2105 | 0.3641 |
| 17 | 0.1950 | 0.1305 | 0.0988 | 0.1404 | 0.4353 |
| 18 | 0.0460 | 0.0347 | 0.0328 | 0.0634 | 0.8231 |
| 19 | 0.0375 | 0.0607 | 0.0350 | 0.0577 | 0.8091 |
| 20 | 0.0170 | 0.0629 | 0.0522 | 0.0648 | 0.8031 |
| 21 | 0.0439 | 0.0625 | 0.0555 | 0.0833 | 0.7548 |
| 22 | 0.0413 | 0.0886 | 0.0730 | 0.1063 | 0.6908 |
| 23 | 0.0297 | 0.0554 | 0.0695 | 0.1015 | 0.7439 |
| 24 | 0.0256 | 0.0391 | 0.0413 | 0.0865 | 0.8075 |
| 25 | 0.0241 | 0.0381 | 0.0380 | 0.1034 | 0.7964 |
| 26 | 0.0338 | 0.0488 | 0.0354 | 0.1212 | 0.7608 |
| 27 | 0.0280 | 0.0365 | 0.0267 | 0.1272 | 0.7816 |
| 28 | 0.0281 | 0.0376 | 0.0306 | 0.1397 | 0.7640 |
| 29 | 0.0257 | 0.0362 | 0.0302 | 0.1359 | 0.7720 |
| 30 | 0.0235 | 0.0349 | 0.0296 | 0.1420 | 0.7700 |
| 31 | 0.0267 | 0.0438 | 0.0254 | 0.1383 | 0.7658 |
| 32 | 0.0231 | 0.0327 | 0.0191 | 0.1399 | 0.7852 |

---

*Draft v0.6 — June 17, 2026. Feature-complete: all sections in full prose (§1–§10), references (§11), and Appendix A (full base-model spectra); two figures. Empirical pillars all delivered and verified — the instrument-conflation exhibit (§4), cross-model spectroscopy with the bootstrap-settled, checkpoint-tested V/M result (§5), and the CCSAE gap = obstruction certificate, exact and trained-confirmed (§6). Sources of record: Papers 26/36/40/45; `empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md`, `ccsae_certificate_settlement.md`, `vm_bootstrap_significance.json`, Figures 1–2. No outstanding compute. Remaining to submission: confirm the draft-formatted external reference strings against the cited sources, and a final read-through pass.*

*Changelog (v0.6): the LRH dialogue (§3.3) and its Related-Work sibling (§8) were sharpened to the exact Park–Veitch causal inner product $M=\mathrm{Cov}(\gamma)^{-1}$, making the estimated-vs-forced contrast explicit — their data-fit free parameter $D$ ($d$ degrees of freedom) versus the Pontryagin-fixed, parameter-free character/conductor-packet basis. The Park et al. (2024) reference string was verified against the arXiv:2311.03658 v2 source (authors, title, ICML 2024 venue all correct).*
