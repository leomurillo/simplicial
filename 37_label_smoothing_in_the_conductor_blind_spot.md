# Label Smoothing Lives in the Conductor Blind Spot

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — substitution proposition + single decisive experiment)**

---

## Abstract

Label smoothing was introduced by Szegedy et al. (2016) and adopted by Vaswani et al. (2017, §5.4) as a regularizer of unspecified mechanism: $\varepsilon_{ls} = 0.1$ "hurts perplexity, improves BLEU." Nine years later the literature still has no agreed account of *why*. We give one. On a categorical readout over a finite ring algebra $R = C_N$, label smoothing fixes the cross-entropy equilibrium at $p_\varepsilon^\star = (1-\varepsilon)e_y + \varepsilon p_*$, exactly $(1-\varepsilon)$ units away from the maximum-entropy point $p_* = N^{-1}\mathbf{1}$ in the direction of the true class. The off-centroid displacement $h = p_\varepsilon^\star - p_*$ is the leading-order driver of the cross-packet Fisher couplings identified by the Conductor Blind Spot theorem ([Paper 34](34_the_conductor_blind_spot.md), Theorem 5.2): every quadratic preconditioner — Adam included — is structurally blind to these couplings, and the size of the missed signal scales linearly in $\|h\|$. Label smoothing therefore *shrinks the operational domain of the blind spot* by keeping the equilibrium near $p_*$, while conductor-aware update projection ([Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md), "update-projection 100%, gradient-projection 0%" Pareto rule) *closes the blind spot's content* by injecting the missing cross-packet structure into the applied update. The two are *partial substitutes*: they reduce the same per-step blind-spot error by different mechanisms.

We formalize this as a Substitution Proposition (§3) whose leading-order content is $E(\alpha, \varepsilon) \approx (1-\alpha)(1-\varepsilon) \cdot C$ where $\alpha$ is the projection strength of Paper 12's Pareto rule, $\varepsilon$ is the smoothing parameter, and $E$ is the $L^2$ error of the quadratic-preconditioned update relative to the cubic-aware optimum. The single decisive prediction is geometric: the iso-generalization-loss curve in $(\alpha, \varepsilon)$ space is monotonically decreasing, with optimal $\varepsilon^\star(\alpha) \to 0$ as $\alpha \to 1$. We pre-register one experiment — months ($C_{12}$) at three widths, sweep $\alpha \in \{0, 0.25, 0.5, 0.75, 1.0\}$ against $\varepsilon \in \{0, 0.03, 0.06, 0.1, 0.15, 0.2\}$, three seeds — and three failure conditions, each of which would change which mechanism this paper attributes label smoothing to. The Paper 12 anchor pairs are $(6.1250 \to 4.0514)$ at width 32 and $(9.0838 \to 5.7104)$ at width 64 (plain-Adam → Pareto-rule corner at $\alpha = 1, \varepsilon = 0$). Audit $\lambda$ (v2insert-07 §2.2) reproduced both anchor pairs to four-digit match; the V/M empirical-propagation prediction P11 (v2insert-06; §5.A below) settled at K-branch on all three widths with signal-to-noise > 47.

This is a single-result paper. If the iso-loss ridge falls, label smoothing has been a confounder for cubic structure since 2017 and the Vaswani-era hyperparameter inherits a mechanism it never declared. If the ridge does not fall, label smoothing has additional content the Conductor Blind Spot does not capture, and the paper's contribution is the negative result.

**Keywords:** label smoothing, conductor blind spot, Amari–Chentsov cubic, second-order preconditioning, cross-entropy regularization, transformer training, Adam, K-FAC, categorical heads.

---

## 1. Introduction

### 1.1 The 2017 anomaly

Vaswani et al. (2017, §5.4) report label smoothing of $\varepsilon_{ls} = 0.1$ and observe: "This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score." Two things in this sentence have remained unaccounted for in the nine years since:

(a) The *direction* of the trade. A regularizer that hurts the loss it is trained on and improves a downstream metric is doing something specific to the optimizer's update geometry, not the loss landscape itself.

(b) The *number*. $\varepsilon_{ls} = 0.1$ has migrated, essentially unchanged, into nearly every transformer-training recipe — including settings where the cyclic / ring-structured behavior subspaces in the output have completely different algebra. A regularizer with no mechanism does not earn a universal constant.

Subsequent attempts to explain label smoothing have produced calibration arguments (Müller et al. 2019: smoothing improves calibration but harms knowledge distillation), penultimate-layer-clustering arguments (Müller et al. 2020), and information-theoretic readings. None of them predict that the optimum $\varepsilon^\star$ should *depend on the optimizer's curvature model*. The Conductor Blind Spot theorem ([Paper 34](34_the_conductor_blind_spot.md)) does — sharply.

### 1.2 The two mechanisms

The off-centroid Fisher expansion of [Paper 34](34_the_conductor_blind_spot.md), Theorem 5.2, gives, for the cyclic label algebra $R = C_N$ and points $p = p_* + h$ near the maximum-entropy point:
$$g_{p_* + h}(\chi_k, \overline{\chi_\ell}) = -N^3 \, \hat h_{(\ell - k) \bmod N} + O(\|h\|^2).$$
The cross-packet Fisher matrix entry between characters $\chi_k$ and $\chi_\ell$ is, at leading order in $\|h\|$, *linear in the Fourier coefficient of the displacement $h$*. Every quadratic preconditioner (natural gradient, Gauss–Newton, K-FAC, Adam's empirical Fisher, NTK Gram) lives inside the Fisher form's representation class and inherits the entire structure of $h \mapsto g_{p_* + h}$. The Amari–Chentsov cubic, by contrast, has nonzero cross-packet content already *at* $p_*$ (Paper 34, Lemma 3.4 selection rule $k + \ell + m \equiv 0 \pmod N$), and that content is what the quadratic model class cannot represent at any $h$.

Two independent levers reduce the per-step damage from this blind spot:

**Mechanism A (suppress the domain):** Keep the optimizer's equilibrium near $p_*$ where the missing coupling is small in $\|h\|$. Label smoothing does this *exactly* — the equilibrium of the smoothed cross-entropy at fixed target class $y$ is $p_\varepsilon^\star = (1-\varepsilon)e_y + \varepsilon p_*$, with off-centroid displacement
$$h_\varepsilon = p_\varepsilon^\star - p_* = (1-\varepsilon)(e_y - p_*).$$
The displacement shrinks linearly in $(1-\varepsilon)$.

**Mechanism B (close the content):** Project the applied update into the closed conductor support to inject the cross-packet structure directly. [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md) does this with the "gradient-projection 0%, update-projection 100%" Pareto rule, parameterized continuously by a projection strength $\alpha \in [0,1]$:
$$\theta_{t+1} = \theta_t - \eta \cdot [(1-\alpha) g_t + \alpha \, P_S g_t],$$
where $g_t$ is the Adam-preconditioned descent direction and $P_S$ is the orthogonal projector onto the declared closed packet support $S \subseteq \{1, \dots, N-1\}$ in the character basis of the output layer.

Both reduce the same per-step error. They are partial substitutes. The substitution structure is the content of this paper.

### 1.3 Single decisive experiment

We pre-register one experiment: a two-axis sweep over $(\alpha, \varepsilon)$ on the months task ($C_{12}$) at three model widths, three seeds, with held-out test loss as the primary outcome. The prediction is geometric: the iso-loss curve in $(\alpha, \varepsilon)$ space is monotonically decreasing, with $\varepsilon^\star(\alpha) \to 0$ as $\alpha \to 1$. The Paper 12 anchor is the $(\alpha, \varepsilon) = (1, 0)$ corner; the Vaswani-canonical $(\alpha, \varepsilon) = (0, 0.1)$ is the off-diagonal corner against which the ridge structure is read.

If the prediction holds, label smoothing has been a confounder for cubic structure for nine years. If it does not, the paper reports a sharp falsification of the substitution proposition with a known mechanism budget for what label smoothing must additionally be doing.

---

## 2. Setup

### 2.1 Categorical readout and label smoothing

Fix $N \geq 2$ and let $R = C_N$. A model parameterized by $\theta$ outputs logits $z_\theta(x) \in \mathbb{R}^N$ and a categorical distribution $p_\theta(x) = \mathrm{softmax}(z_\theta(x))$. The *label-smoothed* cross-entropy loss at target $y \in R$ with smoothing parameter $\varepsilon \in [0, 1)$ is
$$\mathcal{L}_\varepsilon(\theta; x, y) = -\sum_{c \in R} q_\varepsilon(c \mid y) \log p_\theta(x)_c, \qquad q_\varepsilon(c \mid y) = (1-\varepsilon)\delta_{c, y} + \frac{\varepsilon}{N}.$$

The gradient with respect to logits is the standard $\nabla_z \mathcal{L}_\varepsilon = p_\theta - q_\varepsilon(\cdot \mid y)$. At a fixed input $x$ with target $y$, the loss-minimizing distribution is $p = q_\varepsilon(\cdot \mid y) = (1-\varepsilon) e_y + \varepsilon p_*$, which we denote $p_\varepsilon^\star(y)$.

The equilibrium off-centroid displacement is
$$h_\varepsilon(y) = p_\varepsilon^\star(y) - p_* = (1-\varepsilon)(e_y - p_*).$$
For $\varepsilon = 0$, $\|h_0\|_2 = \|e_y - p_*\|_2 = \sqrt{1 - 1/N}$. For $\varepsilon = 1$, $h_1 = 0$.

### 2.2 The Pareto rule of Paper 12

Let $S \subseteq \{1, \dots, N-1\}$ be a chosen closed packet support (in Paper 12 §months: $S = \{12\}$ or $S = \{6, 12\}$, both of which gave the best held-out generalization). Let $P_S$ be the orthogonal projection onto $\bigoplus_{d \in S} H_d$ in the character basis of the output-layer logits. The Paper 12 Pareto rule with strength $\alpha \in [0, 1]$ is
$$\theta_{t+1} = \theta_t - \eta_t \cdot U_\alpha(g_t), \qquad U_\alpha(g) := (1-\alpha) g + \alpha P_S^{(\text{logit})} g,$$
where $g_t$ is the optimizer's preconditioned descent direction (Adam, in Paper 12's experiments) and $P_S^{(\text{logit})}$ acts on the output-layer logit-row block of the parameter update, pulled back through the unembedding. At $\alpha = 1$ this is the "update-projection 100%" Pareto reported by Paper 12; at $\alpha = 0$ it reduces to Adam.

### 2.3 The blind-spot residual

Define the *cubic-aware optimal* descent direction $g_t^\star$ at iterate $\theta_t$ as the direction that minimizes the cumulant-truncated loss to third order — equivalently, the natural gradient under the Fisher metric augmented by the Amari–Chentsov correction (Paper 17 §2 cubic kinetic + AC source). Then the *blind-spot residual* of the update $U_\alpha$ at smoothing $\varepsilon$ is
$$E(\alpha, \varepsilon; \theta) := \| g_t^\star - U_\alpha(g_t) \|_{g_\theta}^2.$$
$E$ measures, in the Fisher metric, how far the deployed quadratic-preconditioned update is from the cubic-aware optimum at the current iterate.

---

## 3. The Substitution Proposition

**Proposition 3.1 (Substitution at leading order).**  
Let $\theta_\varepsilon$ be an iterate at which the model has converged to the label-smoothed equilibrium for the current input batch, so $p_{\theta_\varepsilon}(x) = p_\varepsilon^\star(y)$. Assume the deployed second-order preconditioner is the exact Fisher at $p_\varepsilon^\star$ (the favorable case for Adam; the bound below is a lower bound on the realistic blind-spot residual). Then, with $h_\varepsilon = (1-\varepsilon)(e_y - p_*)$ and $S \subseteq \{1, \dots, N-1\}$ the closed packet support,
$$E(\alpha, \varepsilon; \theta_\varepsilon) = (1-\alpha)^2 (1-\varepsilon)^2 \cdot C(y, S) + O((1-\varepsilon)^3),$$
where
$$C(y, S) = \sum_{(k, \ell, m) \in \Sigma(N, S)} N^4 \left| T_{p_*}(\chi_k, \chi_\ell, \chi_m) \right|^2 \cdot |\hat{(e_y - p_*)}_{(\ell - k) \bmod N}|^2$$
and $\Sigma(N, S)$ ranges over the cross-packet triples $(k, \ell, m)$ that satisfy the AC selection rule $k + \ell + m \equiv 0 \pmod N$ and have at least one of $\mathrm{cond}(k), \mathrm{cond}(\ell), \mathrm{cond}(m)$ outside $S$.

*Sketch.* Expand $g_{p_*+h_\varepsilon}$ to first order in $h_\varepsilon$ using Paper 34, Theorem 5.2. The leading cross-packet entry between $\chi_k$ and $\chi_\ell$ is $-N^3 \hat{h_\varepsilon}_{(\ell - k) \bmod N}$, which is linear in $(1-\varepsilon)$ by §2.1. The cubic-aware optimum $g^\star$ contributes the Amari–Chentsov correction whose cross-packet matrix elements are $T_{p_*}(\chi_k, \chi_\ell, \chi_m)$ contracted with the current cubic carry direction; Paper 34, Lemma 3.4, gives these as $N^3$ on the selection-rule support. The blind-spot residual is the projection of this difference onto the kernel of $U_\alpha$, which is $(1-\alpha) \cdot (\mathrm{id} - P_S)$ applied to the cross-packet components. Squaring in the Fisher metric and isolating leading order gives the stated form. The $(1-\varepsilon)^3$ remainder is uniform on compact sets of $\theta$. $\square$

**Corollary 3.2 (Iso-loss geometry).**  
For fixed task / model / training horizon, define the generalization loss $\mathcal{G}(\alpha, \varepsilon) := \mathbb{E}_{(x,y) \sim \text{test}} [-\log p_\theta(x)_y]$ where $\theta$ is the parameter at the end of training with $(\alpha, \varepsilon)$. Under Proposition 3.1 plus the auxiliary hypothesis that $\mathcal{G}$ is monotone in $E$ (smaller blind-spot residual implies smaller generalization loss),
$$\frac{\partial \mathcal{G}}{\partial \alpha} < 0 \quad \text{and} \quad \frac{\partial \mathcal{G}}{\partial \varepsilon}\bigg|_{\alpha < 1} < 0,$$
in the neighborhood of $(\alpha, \varepsilon) = (0, 0)$, and the iso-loss curves in $(\alpha, \varepsilon)$ space are monotonically decreasing with slope determined by the substitution rate $\partial \varepsilon / \partial \alpha|_\mathcal{G} = -1 / (1 - \alpha^\star)$ at leading order.

**Remark 3.3 (Asymmetric mechanism budgets).**  
$\alpha$ and $\varepsilon$ are not interchangeable beyond their leading-order contribution to $E$. $\varepsilon$ also affects (i) calibration of the output (Müller et al. 2019), (ii) the magnitude of confident-region gradients (preventing the gradient from vanishing at $p \approx e_y$), and (iii) the effective learning-rate scaling on the trivial character (scaling by $(1-\varepsilon)$). $\alpha$, by contrast, affects only the cross-packet structure of the applied update and leaves calibration, gradient magnitude, and trivial-character behavior unchanged. The substitution prediction is therefore *partial*: $\varepsilon^\star(\alpha) \to 0$ as $\alpha \to 1$ means $\varepsilon$'s mechanism-A content is fully absorbed by $\alpha$, but any *residual benefit* of $\varepsilon$ traceable to (i)–(iii) above is what the experiment will measure.

---

## 4. Pre-registered experimental design

### 4.1 Task and model

Months task ($N = 12$), Paper 12 setup: input is (source month $\in C_{12}$, offset $\in \{1, \dots, 11\}$), target is (source + offset) $\mod 12$. The model is a two-layer MLP with one hidden width $W$, ReLU activation, output dim 12, trained with cross-entropy. Three widths: $W \in \{16, 32, 64\}$. Paper 12 reports the width-32 baseline (Adam, no projection, no smoothing) at test loss $6.1250$ and the Pareto-rule corner ($\alpha = 1, \varepsilon = 0, S = \{12\}$) at test loss $4.0514$. The width-64 plain-Adam baseline is $9.0838$ and the corresponding Pareto-rule corner is $5.7104$ (audit $\lambda$ v2insert-07 §2.2, four-digit reproduction of Paper 12).

### 4.2 Sweep grid

$$\alpha \in \{0,\; 0.25,\; 0.5,\; 0.75,\; 1.0\}, \quad \varepsilon \in \{0,\; 0.03,\; 0.06,\; 0.1,\; 0.15,\; 0.2\}.$$

This is $5 \times 6 = 30$ configurations per width, three widths, three seeds: $270$ training runs. Each run is short (Paper 12 horizons are minutes on a single GPU). Total wall-clock under one day on a single H100.

### 4.3 Splits

Two test splits, both from Paper 12:

- **IID split:** held-out (source, offset) pairs drawn from the same distribution.
- **Offset-OOD split:** training on offsets $\{1, \dots, 9\}$, testing on offsets $\{10, 11\}$. Paper 12 reports that the support $S = \{6, 12\}$ outperforms $S = \{12\}$ on this split; we hold $S = \{12\}$ fixed for the primary experiment but report the $S = \{6, 12\}$ row at the corner $(\alpha, \varepsilon) = (1, 0)$ as a sanity check.

### 4.4 Primary outcomes

- $\mathcal{G}_{\text{IID}}(\alpha, \varepsilon, W, \text{seed})$: test cross-entropy on IID split. Averaged over seeds.
- $\mathcal{G}_{\text{OOD}}(\alpha, \varepsilon, W, \text{seed})$: test cross-entropy on offset-OOD split. Averaged over seeds.
- Logit packet-fraction profile at end of training: $f_d^{(\text{final})}$ for $d \in \{2, 3, 4, 6, 12\}$, restricted to the trained logits' non-trivial character energy.

### 4.5 Secondary outcomes

- Calibration: expected calibration error (ECE) on the IID split.
- Off-support leakage: $\|(I - P_S) z_\theta\|_2 / \|z_\theta\|_2$ over the test set. Paper 12 reports machine-precision leakage ($<10^{-30}$) at $\alpha = 1$; we report leakage as a function of $(\alpha, \varepsilon)$.
- Generalization gap: train cross-entropy minus test cross-entropy.

### 4.6 Iso-loss extraction

For each width $W$, fit a smooth (e.g., bivariate Loess) surface to $\mathcal{G}_{\text{IID}}(\alpha, \varepsilon)$ over the grid. Extract iso-loss contours at $\mathcal{G} \in \{4.5, 5.0, 6.0, 8.0\}$. Report the slope $d\varepsilon / d\alpha$ along each contour, both as a constant fit and as a per-segment estimate.

---

## 5. Pre-registered predictions

**P1 (Substitution ridge).** For each width $W$ and each iso-loss level $\mathcal{G}_0$ in the achievable range, the iso-loss contour in $(\alpha, \varepsilon)$ space is monotonically decreasing: $d\varepsilon / d\alpha < 0$ along the contour, with a strict inequality at every interior point.

**P2 (Optimal $\varepsilon$ vanishes at $\alpha = 1$).** $\arg\min_\varepsilon \mathcal{G}_{\text{IID}}(\alpha = 1, \varepsilon, W)$ is $0$ within seed noise, for all three widths. The width-32 row anchors to Paper 12 ($\mathcal{G} = 4.0514$).

**P3 (Vaswani-canonical replication at $\alpha = 0$).** $\arg\min_\varepsilon \mathcal{G}_{\text{IID}}(\alpha = 0, \varepsilon, W)$ is in $[0.05, 0.15]$ for all three widths, replicating the canonical $\varepsilon_{ls} \approx 0.1$ choice under the no-projection condition.

**P4 (Leading-order substitution rate).** The constant fit to $d\varepsilon / d\alpha$ along the $\mathcal{G} = 5.0$ contour is negative and approximately width-independent, with magnitude in $[0.05, 0.20]$ (corresponding to a substitution rate of one ε-step per several α-steps; the exact constant depends on $C(y, S)$ and is not a free parameter once $S$ is fixed).

**P5 (Calibration decouples).** ECE at $(\alpha = 1, \varepsilon = 0)$ is worse than ECE at $(\alpha = 0, \varepsilon = 0.1)$, while $\mathcal{G}_{\text{IID}}$ at $(\alpha = 1, \varepsilon = 0)$ is better. This is the Remark 3.3 prediction: mechanism A retains calibration content that mechanism B does not absorb.

**P6 (Off-support leakage is α-dominated).** Off-support leakage is determined primarily by $\alpha$, with $\varepsilon$ contributing at most a secondary scaling. At $\alpha = 1$, leakage is at machine-precision floor (Paper 12 anchor) for all $\varepsilon$.

**P7 (Generalization gap is decreasing in both).** Both $\alpha$ and $\varepsilon$ reduce the generalization gap monotonically in the neighborhood of $(0, 0)$, consistent with the mechanism that both reduce overfitting to non-cyclic structure.

### 5.A V/M empirical-propagation prediction P11 (appended from v2insert-06; settled K-branch by audit λ in v2insert-07)

Paper 47 (proposed) *Arithmetic Decoupling Theorem* (v2insert-02) decomposes the conductor lattice of `ℤ/12 = 2² · 3` into V (single-prime / prime-power packets `H_2 + H_3 + H_4`, dim 5) and M (cross-prime carry packets `H_6 + H_{12}`, dim 6). The structural observation (v2insert-06 §1): the Pareto-rule support `S = \{12\}` projects onto the maximal-conductor part of M; the α-mechanism of this paper is, in v2insert-02 vocabulary, *the direct M-injection lever*. This makes P11 a *training-side* test of whether Paper 47's V/M decoupling propagates through training to the trained network's output-logit packet signature.

Define the V/M packet ratio at end of training:
$$\rho_{V/M}(\alpha, \varepsilon, W) := \frac{f_2^{(\text{final})} + f_3^{(\text{final})} + f_4^{(\text{final})}}{f_6^{(\text{final})} + f_{12}^{(\text{final})}} = \frac{\sigma_V(\alpha, \varepsilon, W)}{\sigma_M(\alpha, \varepsilon, W)}.$$

**P11 (V/M packet signature along the iso-loss ridge).** Three-outcome pre-claim under v2insert-04 §3.1:

- **K-branch.** Along iso-loss contours $\mathcal{G}_{\text{IID}}(\alpha, \varepsilon, W) = \text{const}$, $\rho_{V/M}$ varies *monotonically* with $\alpha$; iso-loss is *not* iso-packet. Mechanism A produces M-dominant logit content as $\alpha \to 1$; mechanism B produces balanced V/M content.
- **L-branch.** $\rho_{V/M}$ is iso-loss-invariant within seed noise; the Substitution Proposition holds at the packet level (stronger than the leading-order loss-only substitution).
- **Joint-on-disjoint.** $\rho_{V/M}$ varies along the ridge but non-monotonically (saddle, sign reversal); higher-resolution diagnostic separating substitution from deeper non-linear interaction.

**P11 settled at K-branch on all three widths (audit λ, v2insert-07 §2.4):**

| width | seed-noise scale (median SD of $\rho_{V/M}$) | signal scale (range of $\rho_{V/M}$ mean over grid) | signal/noise | $\rho_{V/M}$ monotone in $\alpha$ at *every* fixed $\varepsilon$? |
|---:|---:|---:|---:|:---:|
| 16 | 0.018 | 0.873 | **47.7** | **yes** (all 6 slices strictly decreasing) |
| 32 | 0.006 | 0.739 | **118.9** | **yes** (all 6 slices strictly decreasing) |
| 64 | 0.006 | 0.700 | **107.2** | **yes** (all 6 slices strictly decreasing) |

At every fixed $\varepsilon \in \{0, 0.03, 0.06, 0.10, 0.15, 0.20\}$ and every width $W \in \{16, 32, 64\}$, $\rho_{V/M}(\alpha = 0, \varepsilon)$ ranges from 0.65 to 0.87 and falls strictly monotonically to $\rho_{V/M}(\alpha = 1, \varepsilon) = 0$ — the latter forced to zero by the structural identity $S = \{12\} \subset M$, which makes the $\alpha = 1$ boundary the V/M-zero boundary. Seed-noise scale ~0.01 against signal ~0.7 → signal-to-noise between 47 and 119 across widths.

**Structural reading (correspondence-language per v2insert-06 §7 (a)).** The K-branch result *does not* prove the small MLP "is doing" the program's arithmetic decoupling. What is recorded is a third empirical reading neither paper would have predicted alone: the trained MLP's output-logit packet signature varies with the training mechanism in the direction the V/M arithmetic predicts. Paper 37's Substitution Proposition (loss-direction prediction) and Paper 47's V/M decoupling (lift-tangent structural claim) are both load-bearing internally; P11 is a third measurement that the composition admits.

Audit λ settlement record: [`empirical/reports/label_smoothing_substitution_VM_audit_lambda.md`](empirical/reports/label_smoothing_substitution_VM_audit_lambda.md). Per-width tables and heatmaps in [`empirical/reports/label_smoothing_substitution_months_width{16,32,64}.md`](empirical/reports). Wall time: ~22 minutes on CPU for 270 training runs.

---

## 6. Failure conditions

**F1 (Substitution falsified).** If P1 fails — that is, if the iso-loss contour in $(\alpha, \varepsilon)$ space is not monotonically decreasing anywhere in the achievable range — then label smoothing and conductor-aware update projection are *not* partial substitutes, and Proposition 3.1's bound is too loose to constrain training. The paper becomes a negative result: a specific structural prediction of the Conductor Blind Spot theorem fails to govern training trajectories at this scale, and the auxiliary hypothesis of Corollary 3.2 ($\mathcal{G}$ monotone in $E$) is the load-bearing assumption that breaks.

**F2 (Anchor failure).** If $\mathcal{G}_{\text{IID}}(\alpha = 1, \varepsilon = 0, W = 32) \notin [3.5, 4.5]$, the experimental setup does not reproduce Paper 12. The sweep is uninterpretable until reconciled.

**F3 (Inverted P2/P3).** If the optimal $\varepsilon$ at $\alpha = 1$ is strictly positive *and* the optimal $\varepsilon$ at $\alpha = 0$ is zero, the substitution direction is *opposite* to the predicted one. This would indicate that label smoothing and conductor-aware projection are complementary rather than substitutive — they target different blind spots — and Proposition 3.1's bound on $E$ is the wrong residual to track.

**F4 (Width-dependent ridge slope).** If P4 fails — the substitution rate $d\varepsilon / d\alpha$ varies strongly with $W$ — the leading-order analysis of Proposition 3.1 is too coarse, and a finite-sample / finite-width correction to $C(y, S)$ becomes the next theorem-level item. This is not a falsification of the substitution itself, but a quantitative falsification of its width-independence.

**F5 (No calibration decoupling).** If P5 fails — ECE at $(\alpha = 1, \varepsilon = 0)$ matches ECE at $(\alpha = 0, \varepsilon = 0.1)$ — then mechanism A's calibration content is also absorbed by mechanism B, and Remark 3.3 was wrong about the asymmetric budget. The paper would then report that conductor-aware projection is a *full* substitute, not a partial one, which would be the stronger version of the claim.

---

## 7. Anchor measurement (Paper 12 corner)

From [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md), months task, support $S = \{12\}$, reproduced to four-digit match by audit $\lambda$ (v2insert-07 §2.2):

| width | $\alpha$ | $\varepsilon$ | $\mathcal{G}_{\text{IID}}$ (test loss) | off-support leakage |
|---:|---:|---:|---:|---:|
| 32 | 0 (Adam, no smoothing) | 0 | $6.1250$ | not reported |
| 32 | 1 (update-projection, no smoothing) | 0 | $4.0514$ | $< 10^{-30}$ |
| 64 | 0 (Adam, no smoothing) | 0 | $9.0838$ | not reported |
| 64 | 1 (update-projection, no smoothing) | 0 | $5.7104$ | $< 10^{-30}$ |

These are the four corners of the proposed grid that are already known. The Vaswani-canonical configuration $(\alpha, \varepsilon) = (0, 0.1)$ is the additional corner of interest; the remaining configurations are the sweep.

Width-16 anchor at $(\alpha, \varepsilon) = (1, 0)$ is also reproduced by audit $\lambda$ ($3.0993$ mean over three seeds, not pre-registered in Paper 12).

---

## 8. Script inventory

```text
empirical/label_smoothing_substitution_sweep.py
  Top-level driver. Args: --width, --alphas, --epsilons, --seeds, --task months,
  --support {12 | 6,12}, --output-dir.
  For each (W, alpha, eps, seed) trains a months MLP and records:
    - train/test loss curves
    - final logit packet-fraction profile
    - ECE on test set
    - off-support leakage
    - generalization gap

empirical/label_smoothing_substitution_isoloss.py
  Post-hoc analysis: fits the bivariate surface to G_IID(alpha, eps) per width,
  extracts iso-loss contours, reports slopes and confidence bands.

empirical/reports/label_smoothing_substitution_months_width16.md
empirical/reports/label_smoothing_substitution_months_width32.md
empirical/reports/label_smoothing_substitution_months_width64.md
empirical/reports/label_smoothing_substitution_isoloss_summary.md
```

Run command schema:

```text
python empirical\label_smoothing_substitution_sweep.py ^
  --width 32 ^
  --alphas 0,0.25,0.5,0.75,1.0 ^
  --epsilons 0,0.03,0.06,0.1,0.15,0.2 ^
  --seeds 0,1,2 ^
  --task months ^
  --support 12 ^
  --output-dir empirical\reports
```

The full sweep is three driver invocations (one per width) and one isoloss summary invocation. Total compute: under 24 hours on a single GPU.

---

## 9. Result templates

The manuscript v0.2 will populate the templates below from the sweep.

### 9.1 IID test loss heatmap

A $5 \times 6$ heatmap per width: rows $\alpha$, columns $\varepsilon$, cell value $\mathcal{G}_{\text{IID}}(\alpha, \varepsilon)$ averaged over seeds. Iso-loss contours overlaid. Paper 12 anchor at $(\alpha, \varepsilon) = (1, 0)$ marked.

### 9.2 Iso-loss slope table

| width | $\mathcal{G}_0$ | $d\varepsilon / d\alpha$ along $\mathcal{G}_0$ | 95% CI |
|---:|---:|---:|---:|
| 16 | 4.5 | pending | pending |
| 16 | 5.0 | pending | pending |
| 16 | 6.0 | pending | pending |
| 32 | 4.5 | pending | pending |
| ... | ... | ... | ... |

### 9.3 Optimal $\varepsilon$ vs. $\alpha$

A single figure: $\varepsilon^\star(\alpha) = \arg\min_\varepsilon \mathcal{G}_{\text{IID}}(\alpha, \varepsilon)$ vs. $\alpha$, three lines for three widths. Prediction: monotonically decreasing, with $\varepsilon^\star(1) = 0$ and $\varepsilon^\star(0) \in [0.05, 0.15]$.

### 9.4 Decoupling diagnostic

Two-row table at the four corner configurations $(\alpha, \varepsilon) \in \{0, 1\} \times \{0, 0.1\}$, per width:

| $(\alpha, \varepsilon)$ | $\mathcal{G}_{\text{IID}}$ | ECE | leakage | gen gap |
|---|---:|---:|---:|---:|
| $(0, 0)$ | pending | pending | pending | pending |
| $(0, 0.1)$ | pending | pending | pending | pending |
| $(1, 0)$ | pending | pending | pending | pending |
| $(1, 0.1)$ | pending | pending | pending | pending |

The $(1, 0.1)$ corner is the substitution test: if $\mathcal{G}_{\text{IID}}(1, 0.1) > \mathcal{G}_{\text{IID}}(1, 0)$, smoothing is *harmful* at full projection strength, which is the strongest form of the substitution prediction.

### 9.5 Cross-support replication

The full grid is run for $S = \{12\}$. The corner $(\alpha, \varepsilon) = (1, 0)$ is additionally reported for $S = \{6, 12\}$ on the offset-OOD split, confirming the Paper 12 cross-support finding under the no-smoothing condition.

---

## 10. Connections and scope

### 10.1 Connection to the program

- [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md): supplies the Pareto rule, the months experimental setup, and the corner anchor.
- [Paper 34](34_the_conductor_blind_spot.md): supplies the structural blind-spot theorem and the off-centroid Fisher expansion (Theorem 5.2) that makes Proposition 3.1 quantitative.
- [Paper 26](26.conductor_probe_obstruction_theorem.md): supplies the quotient-character / conductor-packet vocabulary and the empirical reading rule (analytic pullback zeros distinguished from model-facing measurements).
- [Paper 36](36_layerwise_packet_spectroscopy.md): the layerwise spectroscopy supplies the diagnostic against which a positive substitution result can be mechanistically interpreted ($\varepsilon$ vs. $\alpha$ should leave different per-layer packet-profile signatures, even when their $\mathcal{G}_{\text{IID}}$ values coincide along an iso-loss contour).

### 10.2 Connection to Neural LoFi (Dandi et al., arXiv 2605.13612v1)

Dandi et al.'s second-order spectral analysis predicts effective dimension growth under specific training conditions. The substitution prediction here is first-order — it concerns the *cross-packet content* of the applied update, which lives outside Dandi's quadratic spectral class by construction (Paper 34, Theorem 3.5). A natural cross-check is to track effective dimension and packet leakage in tandem across the $(\alpha, \varepsilon)$ grid; the prediction is that Dandi's effective dimension is approximately constant along iso-loss contours, while packet leakage tracks $\alpha$ monotonically. We do not run this cross-check in the primary experiment but flag it as the most natural empirical bridge.

### 10.2A Connection to Data-driven Circuit Discovery (Rai, Geva & Yao 2026, arXiv:2605.09129)

Rai, Geva & Yao 2026 report a *smooth* Jaccard similarity ridge across mixture ratios in their data-driven circuit-discovery study (their Fig 3c): circuits discovered at adjacent mixture proportions $\alpha_{\text{mix}}, \alpha_{\text{mix}} \pm 0.1$ share top-5% edge support at Jaccard $0.79$–$0.89$, with the similarity falling smoothly to $0.26$ at the extreme mixture endpoints. The structural reading via the Substitution Proposition: the mixture proportion $\alpha_{\text{mix}}$ acts on the off-centroid displacement $h$ of the centered logit by perturbing the empirical distribution's centroid, and label smoothing $\varepsilon$ acts on the same $h$ by shrinking it toward $p_*$; the smooth Jaccard ridge across $\alpha_{\text{mix}}$ is the iso-Jaccard contour of a bilinear substitution surface in $(\alpha_{\text{mix}}, \varepsilon)$.

**Joint experiment (pre-registered).** Re-run the Rai-Geva-Yao 2026 EAP-IG mixture sweep (their Fig 3a/b/c protocol: mixture proportion $\alpha_{\text{mix}} \in \{0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0\}$ on the entity-binding × arithmetic mixed dataset) at each of four label-smoothing fine-tune values $\varepsilon \in \{0.0, 0.05, 0.1, 0.2\}$. The Substitution Proposition predicts that the recovered circuit's Jaccard similarity to the $(\alpha_{\text{mix}} = 0, \varepsilon = 0)$ reference circuit is a function of the single combined parameter $\eta = (1 - \alpha_{\text{mix}})(1 - \varepsilon)$, not of $\alpha_{\text{mix}}$ and $\varepsilon$ separately, up to leading order in $h$. Concretely: the seven-by-four grid of Jaccard values, plotted against $\eta$, should collapse onto a single curve to within bootstrap noise. If the collapse holds, the Rai-Geva-Yao smooth-ridge finding is a direct measurement of the substitution surface at production-LLM scale; if it fails, the substitution is either narrower than the present claim or interacts nontrivially with the choice of attribution method. Both branches reportable. Compute is additive on the released Rai-Geva-Yao attribution artifacts: tens of GPU-hours per (model, $\varepsilon$) cell for the label-smoothing fine-tune, plus the existing EAP-IG pipeline run unchanged.

### 10.3 What this paper does not claim

- It does not claim that conductor-aware update projection is the *only* mechanism through which label smoothing acts. Calibration (Müller et al. 2019), penultimate-layer clustering (Müller et al. 2020), and gradient-magnitude regularization in the confident regime are real and independently documented; Remark 3.3 enumerates them.
- It does not claim that the substitution holds beyond the cyclic ring-structured head case. Vaswani et al.'s vocab is not $C_N$; the present analysis applies wholesale only to the ring-structured slice of the output algebra. Whether transformer vocabularies have enough latent cyclic structure for the substitution to be visible at production scale is an open question on the experimental schedule of [Paper 36](36_layerwise_packet_spectroscopy.md).
- It does not claim that $\varepsilon_{ls} = 0.1$ was a free hyperparameter choice. The historical evidence (Szegedy et al. 2016 → Vaswani et al. 2017) suggests it was selected empirically against a fixed Adam-class optimizer. The present proposition predicts that an empirical search at full conductor-aware projection strength would have selected $\varepsilon_{ls} \approx 0$ instead — which is a counterfactual statement about Vaswani et al., not a normative one about subsequent practice.

### 10.4 Scope of the substitution claim

The substitution is partial, leading-order, at the equilibrium of the smoothed cross-entropy. It does *not* claim that $\alpha$ and $\varepsilon$ are equivalent at every iterate of training, only that they trade off in the same direction at the iso-loss frontier. The auxiliary monotonicity hypothesis of Corollary 3.2 is what couples the per-step blind-spot residual $E$ to end-of-training generalization $\mathcal{G}$, and that hypothesis is empirical, not theoretical, for the present scope.

---

## 11. Conclusion

Label smoothing has been a universal transformer-training constant since 2017 with no agreed account of its mechanism. The Conductor Blind Spot theorem makes a specific prediction: label smoothing acts at leading order by shrinking the off-centroid displacement $\|h_\varepsilon\| = (1-\varepsilon) \|e_y - p_*\|$ that drives the cross-packet Fisher coupling, and conductor-aware update projection at strength $\alpha$ closes the same coupling by direct injection. The two mechanisms are partial substitutes at leading order, and the substitution rate is calculable from the Amari–Chentsov selection rule.

We pre-register one experiment to test this: a two-axis sweep on months at three widths. The Paper 12 anchor occupies the $(\alpha = 1, \varepsilon = 0)$ corner; the Vaswani-canonical configuration occupies $(\alpha = 0, \varepsilon = 0.1)$; the substitution prediction is that the iso-loss contour connecting them is monotonically decreasing, with $\varepsilon^\star(\alpha = 1) = 0$.

If the prediction holds, label smoothing has been a confounder for cubic structure for nine years, and the natural constant for $\varepsilon_{ls}$ depends on the optimizer's curvature model in a way that the literature has never declared. If the prediction fails, the substitution proposition is wrong at this scale, and the paper reports the specific component of $\varepsilon$'s mechanism that remains unaccounted for. Both outcomes resolve a confounder.

The deliverable is a single decisive heatmap per width plus the iso-loss slope table. Compute is one day on one GPU. The experiment is now write-up-ready.

---

*Draft v0.1 — May 19, 2026 — Substitution Proposition, pre-registered sweep, Paper 12 anchor at the $(1, 0)$ corner. v0.2 will populate §9 result templates from the months sweep at widths $\{16, 32, 64\}$.*
