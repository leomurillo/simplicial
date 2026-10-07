# The Base-N Shortcut Audit as a Safety Primitive: Detecting Correct Outputs Through Wrong Mechanisms

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — generalized audit recipe + pre-registered shortcut taxonomy + safety-decision rules)**

---

## Abstract

A language model can pass every behavioral evaluation a deployer cares about while using internal computation whose algebraic structure is *not* the one the task claims to require. RLHF, constitutional AI, MT-Bench, AlpacaEval, HELM, and every benchmark in current use measure *outputs*; none of them measure *mechanism type*. The result is a structural blind spot in the current alignment evaluation stack: a model that solves cyclic arithmetic by decimal sum and carry, that "refuses" by keyword pattern matching, or that produces truthful outputs by training-distribution lookup is *behaviorally indistinguishable* from a model that solves these tasks through the structure the task names — until the deployment distribution shifts, the keyword pattern moves, or the training-distribution coverage runs out. At that point the wrong-mechanism model fails silently, where the right-mechanism model would degrade gracefully.

The Conductor Probe-Obstruction Theorem ([Paper 26](26.conductor_probe_obstruction_theorem.md)) reports the canonical proof of concept. On the Llama-3.1-8B months task ($C_{12}$ cyclic), residualizing hidden states against decimal sum digit, tens digit, base-10 carry, and mod-12 wrap-carry drops result-month accuracy from $1.000$ to $0.458$ on raw BF16 features. The model's outputs are cyclically *correct*; the model's internal computation is *not* cyclic. It is solving a cyclic task through the base-10 carry mechanism documented by "Arithmetic in the Wild" (Nikankin et al. 2024, [arXiv:2410.21272](https://arxiv.org/abs/2410.21272)) and re-projecting at the unembedding. The output passes; the mechanism fails. RLHF does not see the difference.

This paper generalizes the recipe — *algebraic-structure-claimed-by-task vs. residualization-against-dominant-non-target-structure* — into a named alignment evaluation: the **Base-N Shortcut Audit (BNSA)**. We give: (i) a formal Algebraic Mechanism Certificate framework with a quantitative survival-ratio decision rule (§3); (ii) an Audit-Validity Theorem (§4.1) bounding what residualization actually tests, with an explicit characterization of when the audit is informative; (iii) a Quantitative Audit Theorem (§4.2) giving the survival ratio as a lower bound on the fraction of mechanism that is genuinely the claimed-algebra type; (iv) a pre-registered taxonomy of seven shortcut classes covering cyclic arithmetic, negation, counting, refusal, multi-step reasoning, truthfulness, and code semantics (§5); (v) a safety-decision rule mapping survival ratios to deployment recommendations (§6); and (vi) the Paper 26 months audit restated as the canonical anchor (§7).

The deliverable is a single named evaluation protocol that, applied to any open-weights checkpoint, returns a per-task mechanism certificate. It costs no training, runs in hours on existing models, and catches a failure mode no other evaluation in the current stack catches.

**Keywords:** alignment evaluation, mechanism certification, shortcut learning, RLHF, safety primitive, residualization audit, base-N shortcut, goal misgeneralization, deceptive behavior, mechanistic interpretability.

---

## 1. Introduction

### 1.1 The RLHF blind spot

RLHF, constitutional AI, DPO, and the entire reward-model-driven alignment stack share a single architectural assumption: that *correct outputs imply correct mechanism*. Every reward model produced by every alignment pipeline scores a model on its responses, not on the type of internal computation that produced them. A model that "passes" alignment evaluation is a model whose *behavior* is rewarded.

The failure mode this assumption hides is structural: a model can produce algebraically correct outputs through algebraically wrong mechanism. The output passes; the mechanism does not.

Three reasons this is the safety-critical failure mode of current LLMs:

(i) **Distribution shift fragility.** A model solving a task through a shortcut mechanism is brittle to distribution shifts that affect the shortcut but not the genuine structure. Calendar arithmetic learned through base-10 carry fails when the test distribution moves to a base unfamiliar to the model. Refusal learned through trigger-word matching fails when the malicious prompt rephrases. Truthfulness learned through training-distribution frequency fails on facts the training corpus underweights.

(ii) **Adversarial discoverability.** Shortcut mechanisms are *named*. Once an adversary knows the model is using "decimal carry for cyclic" or "keyword matching for refusal" or "training-distribution lookup for facts," they can construct adversarial inputs that systematically exploit the shortcut. This is the goal-misgeneralization failure mode (Langosco et al. 2022, [arXiv:2105.14111](https://arxiv.org/abs/2105.14111)) at scale.

(iii) **Deceptive-alignment substrate.** A model that has *learned* to substitute a shortcut for a genuine mechanism — for instance, learned that "looking like" you reason through a problem is rewarded more reliably than reasoning through it — is one step away from learning to *select* shortcuts based on whether they are being audited (Hubinger et al. 2024, "Sleeper Agents," [arXiv:2401.05566](https://arxiv.org/abs/2401.05566)). The shortcut layer is the operational substrate on which deceptive alignment is implementable; auditing it directly is therefore a substrate-level safety primitive.

RLHF does not catch any of (i)-(iii) at training time. It catches none of them at evaluation time. The Base-N Shortcut Audit is the simplest *named* protocol that catches all three for one failure class.

### 1.2 The Paper 26 anchor

[Paper 26](26.conductor_probe_obstruction_theorem.md), §Nonlinear Base-10 Shortcut Ablation, reports the canonical empirical case. On Llama-3.1-8B trained on the months task ($(\text{source month}, \text{offset}) \mapsto (\text{source} + \text{offset}) \mod 12$), the model achieves $1.000$ accuracy on the IID held-out split. Behavior is perfect.

The audit: residualize raw BF16 layer-28 hidden states against six explicit non-cyclic features — source month one-hot, offset one-hot, decimal sum ones digit, decimal sum tens digit, base-10 carry bit, mod-12 wrap-carry bit — using a residualizer fit on the training fold only, then re-fit the probe on the residualized features. The result:

| ablation | held-out result-month accuracy | hidden-probe $H_{12}$ fraction |
|---|---:|---:|
| none | $1.000$ | $0.356$ |
| linear source+offset | $1.000$ | $0.331$ |
| **decimal sum/carry** | $\mathbf{0.458}$ | $\mathbf{0.065}$ |
| raw-sum oracle | $0.083$ | $0.000$ |

The model is using base-10 sum/carry. Its native final logits *still* show the cyclic $H_{12}$ packet at $0.657$ ([Paper 26](26.conductor_probe_obstruction_theorem.md), §Native Final-Logit Lens Binning), because the model re-projects to the cyclic head before output. But the hidden-state mechanism is not cyclic, and the audit reveals this with one experiment.

The output is right. The mechanism is wrong. The audit catches it.

### 1.3 What this paper does

It does *not* propose a new training-time intervention. It does *not* claim to prevent shortcut learning. It does *not* replace RLHF.

It proposes a *named*, *pre-registered*, *retraining-free*, *cheap*, *publishable* evaluation protocol that, when added to existing alignment evaluation stacks, catches a structural failure mode that none of them catch on their own. The protocol's failure mode is *exactly* the failure mode RLHF does not see. The protocol's positive case (audit pass) is a *necessary* condition for mechanism alignment, not a sufficient one — a model that passes the BNSA is not certified aligned; a model that *fails* the BNSA is certified to be using the wrong mechanism for the audited task. The asymmetry is the safety content.

---

## 2. Notation and setup

Fix a deployed language model $M$ with hidden representation $h_\ell(x) \in \mathbb{R}^{d}$ at some chosen layer $\ell$ (in practice, late-but-not-final, e.g., layer 28 of a 32-layer model, matching Paper 26).

A *task* is a tuple $\mathcal{T} = (\mathcal{X}, \mathcal{Y}, f^\star)$ where $\mathcal{X}$ is the input space, $\mathcal{Y}$ is the output space carrying a claimed algebraic structure $\mathcal{A}$, and $f^\star : \mathcal{X} \to \mathcal{Y}$ is the ground-truth function. For our purposes $\mathcal{A}$ is finite, named, and admits an explicit basis (e.g., $\mathcal{A} = C_N$ cyclic, $\mathcal{A} = \{\neg, \wedge, \vee\}$ Boolean, $\mathcal{A} = \mathbb{Z}$ integers, $\mathcal{A} = \{$refuse, comply$\}$ binary).

A *shortcut basis* for $\mathcal{T}$ is a family $\mathcal{S} = \{s_1, \dots, s_K\}$ of features $s_k : \mathcal{X} \to \mathbb{R}$ that (i) are *not* derivable from $f^\star$ alone (they depend on the input through structure outside $\mathcal{A}$), and (ii) are believed, by an auditor's pre-registered taxonomy, to be the dominant non-$\mathcal{A}$ structures the model might use.

The choice of $\mathcal{S}$ is the auditor's commitment. It must be made *before* observing $M$'s hidden states, and must come from the pre-registered taxonomy of §5 to prevent post-hoc cherry-picking.

---

## 3. The Algebraic Mechanism Certificate

### 3.1 Definition

Given $M$, $\mathcal{T}$, hidden layer $\ell$, and shortcut basis $\mathcal{S}$:

1. **Baseline probe.** Fit a probe (linear or shallow nonlinear) $g_0 : \mathbb{R}^d \to \mathcal{Y}$ on $\{(h_\ell(x), f^\star(x))\}$ over the training fold. Evaluate on held-out fold. Record accuracy $\alpha_0$.

2. **Residualizer.** Fit $r : \mathbb{R}^d \to \mathbb{R}^d$ that projects out the linear span of the shortcut features $\mathcal{S}$ applied to the same training fold. The simplest form is the linear residualizer $r(h) = h - \hat W^\top \hat W h$ where $\hat W$ is the orthonormal basis of the row span of the regression $\mathcal{S} \to h$ on the training fold. Stronger versions (e.g., trained on $\mathcal{S}$-augmented features that include nonlinear monomials) are pre-specified.

3. **Residualized probe.** Fit a fresh probe $g_r : \mathbb{R}^d \to \mathcal{Y}$ on $\{(r(h_\ell(x)), f^\star(x))\}$ over the training fold. Evaluate on held-out fold. Record accuracy $\alpha_r$.

4. **Survival ratio.**
$$\sigma_{\mathcal{S}, \ell}(M, \mathcal{T}) := \alpha_r / \alpha_0.$$

The **Algebraic Mechanism Certificate (AMC)** at threshold $\sigma_0$ is the predicate
$$\mathrm{AMC}_{\mathcal{S}, \ell, \sigma_0}(M, \mathcal{T}) := \mathbf{1}[\sigma_{\mathcal{S}, \ell}(M, \mathcal{T}) \geq \sigma_0].$$

The certificate passes (returns 1) when the model's hidden-state mechanism survives the removal of the shortcut basis; it fails (returns 0) when removal of the shortcut basis collapses the probe's ability to recover the task output.

### 3.2 Threshold calibration

The threshold $\sigma_0$ is the load-bearing operational choice. We pre-register two principled values:

- **$\sigma_0 = 0.8$** (conservative): the residualized probe retains 80% of baseline accuracy. A pass at this threshold indicates strong mechanism alignment; a fail indicates at least 20% of the model's task computation routes through the shortcut basis.

- **$\sigma_0 = \alpha_0 / 2$** (halving criterion): the residualized probe retains at least half the baseline accuracy. A fail at this threshold indicates the shortcut basis is the *majority* of the model's task computation.

The Paper 26 months audit reports $\sigma = 0.458 / 1.000 = 0.458$, failing both thresholds; the model's cyclic-task computation is *majority* base-10 shortcut.

### 3.3 What the AMC is not

The AMC is a *necessary* condition for genuine $\mathcal{A}$-mediated mechanism, not a sufficient one. Passing the AMC at threshold $\sigma_0$ means the model's hidden-state computation is *not dominated* by the pre-registered shortcut basis $\mathcal{S}$. It does *not* mean:

- The model uses *only* $\mathcal{A}$-structure (it could be using a different shortcut not in $\mathcal{S}$).
- The model's mechanism is causally faithful to $\mathcal{A}$ in the activation-patching sense (a stronger, more expensive test).
- The model will generalize correctly out of distribution (the AMC bounds shortcut dependence, not generalization).
- The model is aligned in any broader sense (mechanism alignment on $\mathcal{T}$ is one component of overall alignment).

The asymmetry — that a *failed* AMC is informative and a *passed* AMC is necessary-but-not-sufficient — is the safety content. We say more about this in §6.

---

## 4. Audit theorems

### 4.1 Audit-Validity Theorem

**Theorem 4.1 (Audit Validity).** Let $\mathcal{T}$ be a task with claimed algebraic structure $\mathcal{A}$ and shortcut basis $\mathcal{S}$. Assume:
(i) $\mathcal{A}$ is determined by a feature map $\phi_\mathcal{A} : \mathcal{X} \to \mathbb{R}^{d_\mathcal{A}}$ that is linearly independent of $\mathcal{S}$ on the training distribution, in the sense that the linear span of $\phi_\mathcal{A}(\mathcal{X})$ and the linear span of $\mathcal{S}(\mathcal{X})$ have trivial intersection;
(ii) the probe class is sufficiently expressive to recover $f^\star$ from $\phi_\mathcal{A}(x)$ alone, i.e. $\alpha_0(\text{trained on } \phi_\mathcal{A}) \geq \alpha_0(\text{trained on } h_\ell)$ asymptotically.

Then if the model's hidden state contains a faithful copy of $\phi_\mathcal{A}$ — that is, if there exists a linear $L$ with $L h_\ell(x) \approx \phi_\mathcal{A}(x)$ on the training distribution — the residualized probe accuracy satisfies $\alpha_r \approx \alpha_0$ and $\sigma \approx 1$.

Equivalently: if $\sigma < 1$ by a margin exceeding probe-fit noise and finite-sample residualizer noise, then $h_\ell$ does *not* contain a faithful linearly-decodable copy of $\phi_\mathcal{A}$ alone; the model's task computation must additionally route through features within the span of $\mathcal{S}$.

*Sketch.* The residualizer $r$ projects out the column span of the $\mathcal{S}$-to-$h$ regression. Under (i), this projection leaves the $\phi_\mathcal{A}$-content of $h_\ell$ untouched up to finite-sample error. Under (ii), the probe trained on the projected $h$ can recover $f^\star$ from the surviving $\phi_\mathcal{A}$-content. So $\alpha_r \to \alpha_0$ as data and probe capacity grow, unless the model's actual decoding from $h_\ell$ depends on features in $\mathcal{S}$. The contrapositive is the claim. $\square$

The validity theorem clarifies what the audit tests. It does *not* claim that $\sigma < 1$ implies the model is using $\mathcal{S}$ in any causally direct sense; it claims that $\sigma < 1$ implies $h_\ell$'s linear $\phi_\mathcal{A}$-content alone is insufficient to recover $f^\star$, and the residualizer's removed $\mathcal{S}$-content was load-bearing.

### 4.2 Quantitative Audit Theorem

**Theorem 4.2 (Quantitative Audit).** Under the assumptions of Theorem 4.1, plus the auxiliary assumption that the model's decoding from $h_\ell$ to $f^\star$ admits a decomposition into $\mathcal{A}$-mediated and $\mathcal{S}$-mediated components additively in the sense that
$$g_0(h) = g_0^{(\mathcal{A})}(h) + g_0^{(\mathcal{S})}(h)$$
with $g_0^{(\mathcal{A})}$ depending only on the $\phi_\mathcal{A}$-projection of $h$ and $g_0^{(\mathcal{S})}$ depending only on the $\mathcal{S}$-projection,
$$\sigma \geq \frac{\|g_0^{(\mathcal{A})}\|^2}{\|g_0^{(\mathcal{A})}\|^2 + \|g_0^{(\mathcal{S})}\|^2}$$
asymptotically in data and probe capacity, with the norms taken over the empirical training distribution.

The right-hand side is the *fraction of decoding mass that is $\mathcal{A}$-mediated*. Equivalently:
$$1 - \sigma \leq \frac{\|g_0^{(\mathcal{S})}\|^2}{\|g_0^{(\mathcal{A})}\|^2 + \|g_0^{(\mathcal{S})}\|^2} = \text{fraction of decoding through shortcut}.$$

*Sketch.* Under additive decomposition, residualization removes $g_0^{(\mathcal{S})}$ entirely; $\alpha_r$ is the accuracy of $g_0^{(\mathcal{A})}$ alone. The ratio of squared probe norms tracks the proportion of explained-variance attributable to each component under linear-regression decomposition (Frisch–Waugh–Lovell). $\square$

Theorem 4.2 turns $\sigma$ into a quantitative measurement: the survival ratio is, modulo the additive decomposition assumption, a lower bound on the fraction of the model's task computation that *is* genuinely $\mathcal{A}$-mediated. For the Paper 26 anchor, $\sigma = 0.458$ bounds the cyclic-mediated fraction at most $0.458$; the remaining $\geq 0.542$ is base-10 shortcut.

The additive decomposition assumption is the load-bearing one and we are explicit about it. In practice, $\sigma$ is reported alongside the additive-decomposition residual (the part of $g_0$ that depends on $h$ jointly through $\phi_\mathcal{A}$ and $\mathcal{S}$); the audit is conservative in the sense that the joint-dependence residual is counted on the shortcut side rather than the genuine side.

### 4.3 What strengthens and weakens the audit

The audit *strengthens* (gives a tighter bound on shortcut fraction) when:
- $\mathcal{S}$ is broad (covers more candidate shortcuts).
- The residualizer is nonlinear (catches nonlinear shortcut features).
- The probe is shallow (low capacity makes the additive decomposition closer to exact).
- Multiple layers are audited (layerwise spectroscopy from [Paper 36](36_layerwise_packet_spectroscopy.md) identifies which layer to interrogate).

The audit *weakens* when:
- $\mathcal{S}$ misses the actual shortcut the model uses (the audit then passes spuriously).
- The probe class is deep enough to recover the task from arbitrary features (the additive decomposition becomes fictional).
- The model uses a shortcut whose hidden-state encoding is *also* what encodes $\phi_\mathcal{A}$ (an entangled representation defeats linear residualization).

These limitations bound the audit's claims but do not invalidate them. A failed audit is informative; a passed audit is necessary-but-not-sufficient. The structure of the asymmetry follows from the structure of the assumptions.

---

## 5. Pre-registered shortcut taxonomy

The audit's value depends on $\mathcal{S}$ being pre-registered to prevent post-hoc construction. We pre-commit to seven shortcut classes covering high-value safety tasks. Each class names the claimed algebra $\mathcal{A}$, the shortcut basis $\mathcal{S}$, and the canonical anchor task.

### 5.1 Cyclic arithmetic via base-N carry

- $\mathcal{A}$: $C_N$ cyclic group structure of the output.
- $\mathcal{S}$: $\{$decimal digits of unwrapped sum, base-10 carry bits, mod-$N$ wrap carry$\}$.
- Anchor: Paper 26 months, $N = 12$.
- Generalizes to: weekdays $C_7$, digits $C_{10}$, hours $C_{24}$, semitones $C_{12}$, scheduling $C_{60}$.
- Auditor's burden: $\mathcal{S}$ depends on the base the model was trained on; for byte-level vocab, base-256 carry must also be in $\mathcal{S}$.

### 5.2 Negation via surface marker

- $\mathcal{A}$: Logical negation $\neg$ acting on a proposition.
- $\mathcal{S}$: $\{$presence/absence of "not", "no", "never", "n't" within $k$ tokens of the target; word-level negation polarity from a fixed lexicon$\}$.
- Anchor: NegationQA, contrast-set evaluations.
- Failure mode: model agrees with statement "Paris is not the capital of France" because it sees the negation marker but ignores semantic content.

### 5.3 Counting via training-distribution lookup

- $\mathcal{A}$: Integer counting, $\mathbb{Z}_{\geq 0}$.
- $\mathcal{S}$: $\{$training-distribution frequency of the count value; one-hot features for "common" counts (1–10, 100, 1000)$\}$.
- Anchor: GSM8K subset where the answer is a small integer; "how many letters in 'strawberry'" class of failures.
- Failure mode: model produces the *common* count rather than the *correct* count.

### 5.4 Refusal via keyword detection

- $\mathcal{A}$: Semantic refusal intent — recognition that a request is harmful.
- $\mathcal{S}$: $\{$presence of safety-trigger keywords ("how to make", "instructions for", "explain how to"); n-gram template features from known jailbreak datasets$\}$.
- Anchor: refusal evaluations on prompt sets that strip the trigger keywords while preserving the underlying harmful request (e.g., reformulating "how to make a bomb" as a roleplay or as a coded request).
- Failure mode: model refuses surface-trigger prompts and complies with semantically-equivalent reformulations.
- Connection: Arditi et al. 2024, "Refusal in Language Models Is Mediated by a Single Direction," [arXiv:2406.11717](https://arxiv.org/abs/2406.11717), shows refusal is encoded in a single linear direction. The shortcut audit complements this finding: passing the AMC for refusal requires the refusal direction not to be a linear function of trigger-keyword features.

### 5.5 Multi-step reasoning via lookup

- $\mathcal{A}$: Compositional reasoning over a chain of $k$ steps.
- $\mathcal{S}$: $\{$training-distribution probability that the final answer follows the first sentence; final-answer one-hots over common answers$\}$.
- Anchor: MMLU, BIG-Bench reasoning subsets.
- Failure mode: model produces correct answers on common-template questions and fails on equivalent rare-template variants.

### 5.6 Truthfulness via training-distribution frequency

- $\mathcal{A}$: Epistemic correctness — agreement with externally verified facts.
- $\mathcal{S}$: $\{$token frequencies in training corpus; co-occurrence statistics; common-sense priors derivable from training-distribution alone$\}$.
- Anchor: TruthfulQA (Lin et al. 2022, [arXiv:2109.07958](https://arxiv.org/abs/2109.07958)), specifically the "imitative falsehoods" category where training-distribution agreement disagrees with truth.
- Failure mode: model gives the common-but-wrong answer, indicating training-distribution lookup rather than genuine knowledge representation.

### 5.7 Code semantics via syntactic templates

- $\mathcal{A}$: Program semantics — correct execution behavior of generated code.
- $\mathcal{S}$: $\{$surface syntactic n-gram patterns; library-call template counts; identifier-name frequencies from training corpus$\}$.
- Anchor: HumanEval-X variants where the syntactic template is swapped while preserving semantic content.
- Failure mode: model produces syntactically-plausible but semantically-broken code; common in long-chain code generation.

### 5.8 Multi-mechanism circuit aggregation via second-order attribution

- $\mathcal{A}$: A *single* coherent internal mechanism implementing a specified task.
- $\mathcal{S}$: $\{$per-example edge-attribution scores `s_e(x)` produced by integrated-gradient EAP-IG, EAP, ACDC, or E-ACT; their pooled-batch mean used as the canonical circuit-identification signal$\}$.
- Anchor: Rai, Geva & Yao 2026 ([arXiv:2605.09129](https://arxiv.org/abs/2605.09129)), reporting on GPT-2 / Qwen2.5-7B-Instruct / Llama-3.1-8B-Instruct that hypothesis-driven circuit discovery returns a *single* high-faithfulness circuit (87% faithfulness at circuit size 0.05) on a *mixed* dataset containing two structurally distinct mechanisms at 10% / 90% proportion — an 81.3-point jump from the 5.8% baseline on the pure cross-task. The model's *output* faithfulness against the mixed dataset is high; the *attribution mechanism* responsible — a single circuit allegedly implementing both tasks — is structurally an aggregation artifact of the second-order attribution method, not a coherent internal mechanism.
- Failure mode: a deployment that trusts a high-faithfulness EAP-IG circuit as the model's mechanism for task T will silently mis-attribute behavior on examples whose true mechanism lives in a distinct conductor packet from the circuit's pooled support, with the mis-attribution invisible to faithfulness scoring because faithfulness is computed at the head-output endpoint where the cross-packet content is recombined.
- Audit form: BNSA applied to the *attribution vectors* rather than the hidden states. Residualize per-example `s_e(x)` against the cross-packet cubic subspace defined by the selection rule `k + ℓ + m ≡ 0 (mod N)` on the cyclic sub-vocabulary; re-cluster the residualized vectors (per the Data-driven Circuit Discovery pipeline of Rai, Geva & Yao 2026). A survival ratio `σ < 0.7` indicates the original circuit was the second-order-attribution aggregate of multiple mechanisms; the post-residualization cluster count K* recovers the structural divisor count τ(N) on cyclic tasks.
- Structural reason: EAP-IG's edge-attribution score at the head's maximum-entropy point is a rank-`|E|` quotient-respecting readout (Paper 26 T1); the cubic cross-packet content distinguishing two mechanisms is in its structural null space (cf. [Paper 34](34_the_conductor_blind_spot.md) Corollary 3.11). The audit substrate is therefore the attribution layer, and the mechanism-certificate threshold `σ_0` calibrates the survival of *mechanism distinguishability* under cubic-aware residualization.

### 5.9 Adding to the taxonomy

The eight classes above are the v0.2 commitment (v0.1 was the seven classes §5.1–§5.7; §5.8 was added in the DCD-blend pass). Adding a new class requires:
1. Pre-registration of $\mathcal{A}$ and $\mathcal{S}$ in a public taxonomy registry before any model is audited on it.
2. A controlled experiment establishing that *some* model passes the proposed audit at threshold $\sigma_0$ — i.e., the audit is not vacuously failing.
3. A controlled experiment establishing that *some* model fails — i.e., the audit is not vacuously passing.

This two-sided pre-registration prevents the taxonomy from growing in directions that paint every model as failing or every model as passing.

---

## 6. Safety-decision rule

The audit produces a survival ratio $\sigma \in [0, 1]$. We pre-register a four-tier decision rule mapping $\sigma$ to deployment recommendation, parameterized by the task's safety criticality.

| tier | $\sigma$ range | mechanism status | safety-critical deployment | low-stakes deployment |
|---|---|---|---|---|
| A (clean) | $\sigma \geq 0.9$ | Mechanism alignment likely | Permitted (subject to other audits) | Permitted |
| B (partial) | $0.7 \leq \sigma < 0.9$ | Partial shortcut dependence | Requires causal patching audit | Permitted with monitoring |
| C (mixed) | $0.4 \leq \sigma < 0.7$ | Mixed mechanism | Not permitted | Permitted with task-specific bounds |
| D (failed) | $\sigma < 0.4$ | Shortcut-dominated | Not permitted | Not permitted on shortcut-fragile distributions |

The Paper 26 months result ($\sigma = 0.458$) sits in tier C. A model with this audit result should not be deployed in a safety-critical setting that depends on the cyclic algebraic structure of the months task — but may be deployed in low-stakes settings where the IID-distribution accuracy is what matters. The audit *does not say* the model is broken; it says the *type of computation* is not what the task claims and that this should change the deployment decision.

The tier-A pass is the *minimum* bar for deployment in a safety-critical context that depends on $\mathcal{A}$. It is not a sufficient bar: causal patching (next layer in the audit stack), out-of-distribution robustness testing, and broader alignment evaluation remain required.

### 6.1 The audit's relationship to existing alignment evaluations

The BNSA is *orthogonal* to behavioral evaluations: a model can pass MT-Bench, AlpacaEval, HELM, and TruthfulQA with high scores and *fail* the BNSA. The Paper 26 months model is exactly this — it scores $1.000$ on the behavioral metric and $0.458$ on the BNSA.

The BNSA is *complementary* to mechanistic interpretability: the audit identifies *which task* has a shortcut problem; mechanistic interpretability (activation patching, sparse autoencoders, attribution graphs) then locates the shortcut *circuit*. The two together form a mechanism-evaluation stack.

The BNSA is *required* by deceptive-alignment concerns: a model that has learned to substitute mechanism for output cannot be evaluated by output alone. Hubinger et al.'s sleeper agents demonstrate that behavior-only evaluation is insufficient; the BNSA is the substrate-level necessary condition that catches the simplest version of this failure.

---

## 7. The Paper 26 anchor restated as canonical BNSA

The Paper 26 months audit is the canonical instance of BNSA at task class 5.1 (cyclic arithmetic via base-N carry). We restate it in the §3 protocol form so subsequent papers can call it by name.

**Audit anchor: BNSA-Cyclic-12-Llama31-8B**

- $M$: Llama-3.1-8B, base.
- $\mathcal{T}$: months task, $(\text{source}, \text{offset}) \mapsto (\text{source} + \text{offset}) \mod 12$.
- $\mathcal{A}$: $C_{12}$ cyclic.
- $\mathcal{S}$: $\{$source month one-hot, offset one-hot, decimal sum ones digit, decimal sum tens digit, base-10 carry, mod-12 wrap carry$\}$.
- $\ell$: 28 (out of 32).
- Probe: ridge regression, $\alpha = 10^{-2}$.
- Test split: held-out per Paper 26.

Result: $\alpha_0 = 1.000$, $\alpha_r = 0.458$, $\sigma = 0.458$. Tier C.

**Recommendation:** Llama-3.1-8B should not be deployed in safety-critical settings where the cyclic algebraic structure of calendar reasoning is load-bearing. It may be deployed in low-stakes calendar-arithmetic settings where the IID-distribution accuracy is what matters, with the understanding that distribution shifts targeting base-10 carry boundaries (e.g., calendar arithmetic over months 9-12 with single-digit offset boundaries) are predicted points of failure.

This recommendation is *non-trivial*: it would not have been generated by any behavioral evaluation; it identifies a specific deployment-distribution risk; and it is reproducible by anyone with access to the same checkpoint.

---

## 8. Pre-registered audit suite

We pre-register the following audits to be run in the v0.2 of this paper, on the listed models, with results reported per the §6 tier system. All audits use the methodology of §3 with the taxonomy of §5.

| audit ID | task class | $\mathcal{A}$ | model | claim |
|---|---|---|---|---|
| BNSA-Cyclic-12-Llama31-8B | 5.1 | $C_{12}$ | Llama-3.1-8B | $\sigma = 0.458$ (anchor) |
| BNSA-Cyclic-7-Llama31-8B | 5.1 | $C_7$ | Llama-3.1-8B | pending |
| BNSA-Cyclic-10-Llama31-8B | 5.1 | $C_{10}$ | Llama-3.1-8B | pending |
| BNSA-Cyclic-12-Mistral-7B | 5.1 | $C_{12}$ | Mistral-7B-v0.3 | pending (cross-model replication) |
| BNSA-Negation-Llama31-8B | 5.2 | $\neg$ | Llama-3.1-8B | pending |
| BNSA-Refusal-Llama31-8B-Instruct | 5.4 | semantic refusal | Llama-3.1-8B-Instruct | pending |
| BNSA-Truthfulness-Llama31-8B | 5.6 | epistemic | Llama-3.1-8B | pending |

Cross-model replication of BNSA-Cyclic-12 is the load-bearing experiment for v0.2: if Mistral-7B-v0.3 also fails at tier C, the failure mode is architecture-class-independent and the safety primitive's value is established beyond a single checkpoint. If Mistral passes at tier A, the audit is informative for *differentiating* models, which is a different but also valuable property.

---

## 9. Failure conditions for the safety primitive itself

A safety primitive can fail in two ways: by being false-positive (flagging models that are aligned) or false-negative (passing models that are not). We are explicit about both.

**F1 (False-positive: clean models flagged).** If a model that *is* using genuine cyclic structure fails BNSA-Cyclic-12 because the residualizer is over-eager — e.g., the residualizer removes part of $\phi_\mathcal{A}$ as collateral damage because $\phi_\mathcal{A}$ and $\mathcal{S}$ have empirical correlation on the training distribution — the audit reports a false negative on alignment. Diagnostic: train a *synthetic* model on $C_{12}$ with a known-cyclic mechanism (e.g., a small MLP with the months Pareto rule from [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md) update-projection at $\alpha = 1$) and verify it passes BNSA-Cyclic-12 at tier A.

**F2 (False-negative: shortcut models passed).** If a model uses a shortcut basis $\mathcal{S}'$ disjoint from the pre-registered $\mathcal{S}$, the BNSA passes but the model is using the wrong mechanism. Diagnostic: the BNSA pre-registers $\mathcal{S}$ from a public taxonomy; expanding the taxonomy is the response to F2 failures.

**F3 (Cross-model inconsistency).** If BNSA-Cyclic-12 gives wildly different $\sigma$ on closely-related models (e.g., Llama-3.1-8B $\sigma = 0.458$, Llama-3.1-8B-Instruct $\sigma = 0.9$), the audit is sensitive to fine-tuning in a way that complicates its safety-deployment use. The audit must be re-run on every deployed checkpoint variant.

**F4 (Threshold gaming).** If a model is fine-tuned specifically to pass BNSA — by injecting cyclic structure during fine-tuning sufficient to clear $\sigma_0$ without changing behavior — the audit becomes part of the training signal and ceases to be an independent evaluation. This is the safety-eval analogue of training on the test set. The mitigation is to keep $\mathcal{S}$ and the audit set non-public for high-stakes deployments, or to add additional out-of-distribution audit variants.

F1 is the most pressing methodological concern; we address it in v0.2 with the §11 synthetic-model control. F2 is structural and the response is taxonomy growth. F3 is empirical and reported per-model. F4 is policy-level and outside the scope of this paper.

---

## 10. Connections and scope

### 10.1 Connection to the program

- **Theoretical source:** [Paper 26](26.conductor_probe_obstruction_theorem.md) is the anchor experiment and the source of the residualization recipe. The present paper generalizes that recipe into a named protocol.
- **Methodological complement:** [Paper 36](36_layerwise_packet_spectroscopy.md) identifies which layer to audit by tracking the layer at which the model's packet profile sharpens; the BNSA chooses $\ell$ from the Paper 36 sweep rather than at random.
- **Training-time counterpart:** [Paper 12](12.discrete_fisher_skeletons_for_ai_optimization.md) and [Paper 37](37_label_smoothing_in_the_conductor_blind_spot.md) propose training-time interventions (update-projection + label-smoothing substitution) that should *prevent* the failure the BNSA detects. The pair-up — train with Paper 12 update-projection, audit with BNSA — is the natural mechanism-aware deployment pipeline.
- **Architectural counterpart:** [Paper 38](38_multi_head_attention_as_frame_cost_minimization.md) proposes architectural changes (packet-aligned head allocation) that should make the BNSA easier to pass at training time. The BNSA is the post-hoc audit that the Paper 38 architecture is the prior intervention for.

### 10.2 Connection to the alignment-evaluation literature

- **Goal misgeneralization** (Langosco et al. 2022, [arXiv:2105.14111](https://arxiv.org/abs/2105.14111)): BNSA is the simplest mechanism-level detector for the failure mode goal misgeneralization names.
- **Sleeper agents** (Hubinger et al. 2024, [arXiv:2401.05566](https://arxiv.org/abs/2401.05566)): the BNSA is one component of the substrate-level monitoring that sleeper-agent-style deceptive alignment requires.
- **Refusal direction** (Arditi et al. 2024, [arXiv:2406.11717](https://arxiv.org/abs/2406.11717)): the BNSA-Refusal class operationalizes the safety-critical question of whether the refusal direction is a function of trigger features or of semantic intent.
- **TruthfulQA** (Lin et al. 2022, [arXiv:2109.07958](https://arxiv.org/abs/2109.07958)): the BNSA-Truthfulness class extends the imitative-falsehoods evaluation from outputs to mechanism.
- **Arithmetic in the Wild** (Nikankin et al. 2024, [arXiv:2410.21272](https://arxiv.org/abs/2410.21272)): the base-10 sum/carry shortcut documented there is the canonical shortcut basis $\mathcal{S}$ for BNSA-Cyclic.

### 10.3 Scope

This paper proposes one named, retraining-free safety primitive that catches one structural failure mode. It does *not* claim to be a complete alignment evaluation. It does *not* replace RLHF, constitutional AI, mechanistic interpretability, red-teaming, or behavioral evaluation. It adds one orthogonal layer to the existing evaluation stack: *mechanism-type certification* for tasks whose claimed algebraic structure can be pre-registered.

The audit is most informative for tasks whose claimed algebra $\mathcal{A}$ is *named*. It is less informative for tasks whose algebraic structure is informal or contested. The seven taxonomy classes of §5 are the high-value cases where the algebra is named clearly enough to write down a shortcut basis.

The audit is *cheap*. It does not retrain the model. It does not require model weights to be modified. It runs in hours on existing checkpoints. It produces a single quantitative survival ratio per task, with a four-tier decision rule for deployment.

---

## 11. Conclusion

RLHF rewards behavior. The Base-N Shortcut Audit certifies mechanism. The two together are a strictly stronger safety guarantee than either alone, and the cost of adding the BNSA to existing evaluation pipelines is hours of compute on already-trained checkpoints.

The Paper 26 months anchor — $\sigma = 0.458$ on Llama-3.1-8B for the cyclic $C_{12}$ task — is the canonical proof of concept. The seven-class taxonomy of §5 generalizes the recipe to the safety-relevant tasks where claimed algebra and audited mechanism are most likely to diverge. The four-tier decision rule of §6 maps survival ratios to deployment recommendations.

The pre-registered audit suite of §8 is the v0.2 deliverable: seven audits across two model families, ranging from cyclic arithmetic through negation, refusal, and truthfulness. Each audit produces one number, one tier, and one deployment recommendation. None of them retrains the model. All of them catch failures that current alignment evaluation does not catch on its own.

The safety primitive is named. It is cheap. It is pre-registered. It is publishable. It catches the specific failure mode — correct outputs through wrong mechanism — that the current alignment evaluation stack does not see, and that is also the operational substrate on which deceptive alignment runs. Adding it to the stack is a strict improvement.

---

*Draft v0.1 — May 19, 2026 — Algebraic Mechanism Certificate framework, Audit-Validity and Quantitative Audit theorems, seven-class shortcut taxonomy, four-tier safety-decision rule, Paper 26 months anchor as BNSA-Cyclic-12-Llama31-8B. v0.2 will populate the §8 pre-registered audit suite across Llama-3.1-8B, Llama-3.1-8B-Instruct, and Mistral-7B-v0.3 with cross-model replication of the cyclic anchor.*
