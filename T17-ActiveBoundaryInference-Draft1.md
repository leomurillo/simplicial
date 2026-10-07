# T17 - Active Boundary Inference

**Free Energy Minimization as Governed Representation Completion**

**Leonardo Murillo Montero**

*First draft - May 26, 2026*

---

> *The mind should not update on surprise alone. It should update on the part of surprise that names a missing boundary.*

---

## Abstract

**Situation.** T13 proved that projection creates boundary sources and that renormalization is finite closure under conductor fusion. T14 proved that curvature, beta source, Schur correction, and Noether defect are the same projection-boundary obstruction. T15 proved that open systems require terminal boundary completion. T16 translated these results into learned representations: activations, residual streams, attention, memory, tools, and alignment are operations on retained sectors and their boundaries.

**Gap.** Active Inference and the Free Energy Principle offer a powerful variational language for perception, action, planning, and self-evidencing. In their standard form, however, free energy, surprise, accuracy, complexity, risk, ambiguity, and information gain are scalar totals. They tell us that a model is surprised or that a policy is valuable, but they do not by themselves identify which structural component of a representation should be changed. In deep learning this missing decomposition appears as shortcut learning, hallucination, over-updating on noise, under-updating on hidden structure, and brittle out-of-distribution behavior.

**Action.** We introduce **Active Boundary Inference**: a packet-resolved expansion of variational and expected free energy. The retained representation sector \(S\) supplies the current generative model. Its closure boundary \(\partial S\) supplies the missing structural packets. Scalar FEP quantities are recovered only after summing over retained, boundary, noise, and governance channels. The central refinement is
\[
\boxed{
\text{belief updating should follow boundary-structured surprise and packet-resolved accuracy gain, not raw surprise alone.}
}
\]

**Result.** We prove twelve structure theorems. First, the **Generative Model as Retained Sector Theorem**. Second, the **Free Energy Packet Decomposition Theorem**. Third, the **Surprise Decomposition Theorem**. Fourth, the **Accuracy Decomposition Theorem**. Fifth, the **Complexity / Closure Budget Theorem**. Sixth, the **Divergence as Projection Mismatch Theorem**. Seventh, the **Precision as Boundary Gain Theorem**. Eighth, the **Expected Free Energy as Active Boundary Functional Theorem**. Ninth, the **Perception-Action Completion Duality Theorem**. Tenth, the **Markov Blanket as Boundary Interface Theorem**. Eleventh, the **Matched-Surprise Separation Theorem**. Twelfth, the **Active Boundary Fixed-Point Theorem**.

**Empirical test.** Three controlled experiments instantiate the theory. E1, the Conductor/XOR Boundary Experiment, shows that boundary residuals identify the missing interaction packet \(z_0z_1\) in 300/300 main trials and 180/180 stress trials. E2, the Matched-Surprise Active-Inference Experiment, constructs noise and structural episodes with matched scalar surprise. Scalar surprise remains near chance for distinguishing them, while packet-resolved T accuracy gain reaches AUC 1.000 in the main run and 1.000 by 32 evidence labels in a 64-dimensional stress run with 2,016 candidate packets. E3, the Boundary-Cue T-Maze Experiment, shows that boundary decomposition changes active policy selection: scalar surprise remains at chance, while boundary accuracy gain reaches AUC 1.000 and the T17 boundary agent reaches oracle-level structural net reward.

**Harvest.** T17 does not reject Active Inference. It supplies a packet-resolved structural refinement of it. Variational free energy is the aggregate thermodynamic quantity. Active Boundary Inference decomposes that aggregate into operational terms: which packet caused surprise, which packet would improve accuracy, which update costs too much, which boundary should be routed externally, and which completion is governed.

**Keywords:** active inference, Free Energy Principle, expected free energy, surprise, complexity, accuracy, information gain, precision, representation closure, boundary surprise, shortcut learning, belief updating, active boundary inference, Markov blanket, governed completion.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| T1 Native Simplicial Chart | Probability coordinates and finite observed state spaces |
| T2 Cumulant Tower | Connected residuals and interaction order |
| T3 Character Orthogonality | Packet decomposition of observables |
| T11 Apex Vertex Calculus | Interaction boundaries and conductor fusion |
| T12 Finite Apex Determinacy | Finite spectral closure of observation towers |
| T13 Exact Simplicial Renormalization | Boundary integration and closure flow |
| T14 Projected Flatness | Curvature as projection-commutator boundary |
| T15 Finite-to-Archimedean Completion | External and terminal boundary completion |
| T16 Representation Closure | Learned systems as projection-completion architectures |
| E1 Conductor/XOR Boundary Experiment | Empirical test of boundary surprise in shortcut learning |
| E2 Matched-Surprise Active-Inference Experiment | Empirical test of structural belief update under matched scalar surprise |
| E3 Boundary-Cue T-Maze Experiment | Empirical test of boundary-resolved active policy selection |

---

## 1. Starting Point: Standard FEP/AIF Decompositions

Let \(y\) denote observations, \(x\) hidden states, \(Q(x)\) an approximate posterior or recognition density, and \(P(y,x)\) a generative model. Variational free energy is
\[
F[Q,y]
=
\mathbb E_Q[\ln Q(x)-\ln P(y,x)].
\]
Equivalently,
\[
F[Q,y]
=
D_{KL}[Q(x)\|P(x)]
-
\mathbb E_Q[\ln P(y|x)].
\]
The usual reading is
\[
\boxed{
F=\mathrm{Complexity}-\mathrm{Accuracy}.
}
\]
Another identity is
\[
F[Q,y]
=
D_{KL}[Q(x)\|P(x|y)]-\ln P(y),
\]
so free energy is an upper bound on surprise
\[
\mathcal S(y)=-\ln P(y).
\]

For planning, Active Inference uses expected free energy. In the notation of the textbook equation,
\[
G(\pi)
=
-
\mathbb E_{Q(\tilde x,\tilde y|\pi)}
\left[
D_{KL}\left(
Q(\tilde x|\tilde y,\pi)\|Q(\tilde x|\pi)
\right)
\right]
-
\mathbb E_{Q(\tilde y|\pi)}
\left[
\ln P(\tilde y|C)
\right].
\]
The first term is information gain or epistemic value. The second is pragmatic value.

The same object can be rewritten as
\[
G(\pi)
=
\mathbb E_{Q(\tilde x|\pi)}
\left[
H[P(\tilde y|\tilde x)]
\right]
+
D_{KL}\left[
Q(\tilde y|\pi)\|P(\tilde y|C)
\right],
\]
or
\[
G(\pi)
\le
\mathbb E_{Q(\tilde x|\pi)}
\left[
H[P(\tilde y|\tilde x)]
\right]
+
D_{KL}\left[
Q(\tilde x|\pi)\|P(\tilde x|C)
\right].
\]
Thus expected free energy decomposes into expected ambiguity plus risk over outcomes or states. Finally,
\[
G(\pi)
=
-
\mathbb E_{Q(\tilde x,\tilde y|\pi)}
\left[
\ln P(\tilde y,\tilde x|C)
\right]
-
H[Q(\tilde x|\pi)].
\]
This is the expected energy minus entropy form.

These equations are correct, powerful, and too compressed for the present purpose. T17 asks for the packet resolution implicit in them.

---

## 2. The T17 Expansion

Let \(\Omega\) be a finite data, state, or world space. Let
\[
H=\mathbb R^\Omega
\]
be the full observable space. A learned or active model retains a sector
\[
H_S\subseteq H.
\]
It may be generated by features, hidden states, latent causes, predicates, probes, memory keys, or sufficient statistics.

Let
\[
\Pi_S:H\to H_S
\]
be the projection onto the retained sector. Let \(\partial_{\mathcal T}S\) denote the task-relative boundary: the packets produced by task interactions that are not represented in \(S\). A typical interaction has the form
\[
V_n:H_S^{\otimes n}\to H.
\]
The structural boundary is
\[
\partial_nS
=
\operatorname{supp}\left((1-\Pi_S)V_n(H_S^{\otimes n})\right).
\]

For a residual
\[
r_S=y-\hat y_S,
\]
the T17 decomposition is
\[
r_S
=
\Pi_S r_S
+
\Pi_{\partial S}r_S
+
r_{\mathrm{noise}}
+
r_{\mathrm{opt}}
+
r_{\mathrm{stat}}.
\]

The scalar FEP terms are then totals over channels:
\[
F_S
=
\sum_{\alpha\in S}(C_\alpha-A_\alpha)
+
\sum_{\beta\in\partial S}
\left(
C_\beta^{\mathrm{forced}}
-
A_\beta^{\mathrm{latent}}
\right)
+
N.
\]
Here:

| Symbol | Meaning |
|---|---|
| \(A_\alpha\) | accuracy carried by retained packet \(\alpha\in S\) |
| \(C_\alpha\) | complexity cost of reweighting retained packet \(\alpha\) |
| \(A_\beta^{\mathrm{latent}}\) | accuracy gain available if boundary packet \(\beta\) is admitted |
| \(C_\beta^{\mathrm{forced}}\) | cost of explaining boundary structure without representing it |
| \(N\) | noise, finite-sample, optimization, and gauge remainder |

The T17 slogan is
\[
\boxed{
\text{free energy is scalar only after summing packet-resolved accounting.}
}
\]

---

## 3. Dictionary: FEP Terms in Boundary Language

| FEP/AIF term | Standard role | T17 boundary reading |
|---|---|---|
| Generative model | Probabilistic model of hidden causes and observations | Retained sector plus transition/likelihood maps |
| Surprise | \(-\ln P(y)\) | Boundary exposure plus retained error plus noise |
| Bayesian surprise | Prior-posterior divergence | Amount and location of belief displacement |
| Variational free energy | Computable upper bound on surprise | Packet-summed explanation cost under current sector |
| Divergence | KL mismatch of distributions | Projection mismatch between retained sector and required belief state |
| Complexity | KL cost from prior to posterior | Reweighting plus closure plus compression plus external routing cost |
| Accuracy | Expected log likelihood | Packet-resolved fit and latent boundary accuracy gain |
| Expected free energy | Policy score for future inference/action | Expected governed boundary cost minus closure gain |
| Information gain | Expected posterior-prior divergence | Expected packet identification or closure gain |
| Pragmatic value | Expected preferred outcomes | Governed outcome completion |
| Ambiguity | Entropic observation mapping | Channel degeneracy that prevents packet assignment |
| Risk | Divergence from preferred outcomes/states | Governance mismatch at outcome or sector level |
| Expected energy | Expected negative log joint under preferences | Future potential cost under governed closure |
| Precision | Confidence/gain on prediction errors | Boundary gain: which residual channels are amplified or damped |
| Attention | Precision control and active sampling | Dynamic boundary routing |
| Action | Changing observations sampled | External boundary completion |
| Perception | Updating hidden-state beliefs | Internal closure and reweighting |
| Learning | Updating parameters | Slow-sector closure of repeated boundary residuals |
| Markov blanket | Statistical boundary separating system/environment | Interface across which boundary packets are sensed, routed, or completed |

---

## 4. Theorem 1. Generative Model as Retained Sector Theorem

### Statement

Every finite active-inference generative model determines a retained observable sector
\[
H_S\subseteq \mathbb R^\Omega
\]
together with transition, likelihood, preference, and policy maps. Conversely, every retained sector with such maps defines a finite active-inference model up to gauge choice.

### Proof

Let the finite generative model contain hidden states \(x\), observations \(y\), policies \(\pi\), transition kernels \(P(x_{t+1}|x_t,\pi)\), likelihoods \(P(y_t|x_t)\), and preferences \(P(y_t|C)\) or \(P(x_t|C)\). Each state, observation, likelihood column, log-likelihood, posterior statistic, and preference log-potential is a function on the finite joint space \(\Omega\). Their span is a finite subspace
\[
H_S\subseteq \mathbb R^\Omega.
\]
The model's inference and planning operations act through functions in this span and through maps between their probability coordinates.

Conversely, given a retained sector \(H_S\), choose a coordinate basis of sufficient statistics and define probability kernels by exponentiating and normalizing finite potentials in that sector. Gauge freedom appears because multiple bases and normalizations define the same probability law. Thus finite generative models and retained sectors are two descriptions of the same projection architecture. \(\square\)

### Interpretation

An active-inference model is therefore a probability model together with a structural choice of which variables, factors, and interactions are represented inside the agent.

---

## 5. Theorem 2. Free Energy Packet Decomposition Theorem

### Statement

Let \(S\) be a retained sector and \(\partial S\) its task-relative closure boundary. Variational free energy decomposes as
\[
F_S
=
\sum_{\alpha\in S}(C_\alpha-A_\alpha)
+
\sum_{\beta\in\partial S}
\left(
C_\beta^{\mathrm{forced}}
-
A_\beta^{\mathrm{latent}}
\right)
+
N,
\]
where the first sum is retained-sector free energy, the second sum is boundary pressure, and \(N\) is noise/statistical/optimization remainder.

### Proof

Start with
\[
F[Q,y]
=
\mathbb E_Q[\ln Q(x)-\ln P(y,x)].
\]
Choose an orthogonal or biorthogonal packet decomposition of the finite observable space:
\[
H=H_S\oplus H_{\partial S}\oplus H_R.
\]
Project the sufficient-statistic error, log-likelihood contribution, and posterior displacement into these summands. Because expectation is linear, the free-energy functional splits into the sum of its packet contributions plus cross terms. In the orthogonal gauge the cross terms vanish. In a nonorthogonal frame they are absorbed into the finite Gram/Schur correction, already covered by T13 and T14. This yields retained contributions, boundary contributions, and residual remainder.

For \(\alpha\in S\), the terms are ordinary reweighting complexity and retained accuracy. For \(\beta\in\partial S\), the model cannot directly represent \(\beta\); the same data creates forced complexity and latent accuracy gain. Therefore the displayed decomposition follows. \(\square\)

### Interpretation

Scalar free energy is an aggregate quantity. T17 decomposes that aggregate by retained, boundary, and residual channels.

---

## 6. Theorem 3. Surprise Decomposition Theorem

### Statement

The scalar surprise
\[
\mathcal S(y)=-\ln P_S(y)
\]
admits a task-relative decomposition
\[
\mathcal S_S(y)
=
\mathcal S_{\mathrm{in}}(y)
+
\mathcal S_{\partial S}(y)
+
\mathcal S_{\mathrm{noise}}(y),
\]
where
\[
\mathcal S_{\partial S}(y)
\simeq
\sum_{\beta\in\partial S}
\|\Pi_\beta r_S\|^2
\]
to second order near the model's predictive mode.

### Proof

For a smooth finite likelihood, expand negative log likelihood around the retained-sector prediction. The first nonvanishing term is quadratic in the prediction residual:
\[
-\ln P_S(y)
=
\text{constant}
+
\frac12\langle r_S,\Lambda r_S\rangle
+
O(\|r_S\|^3),
\]
where \(\Lambda\) is a precision matrix. Decompose
\[
r_S=\Pi_Sr_S+\Pi_{\partial S}r_S+r_{\mathrm{noise}}.
\]
In the packet frame,
\[
\langle r_S,\Lambda r_S\rangle
\]
splits into retained, boundary, and noise contributions, with finite cross-corrections controlled by the frame Gram matrix. Thus scalar surprise is the sum of in-sector error, boundary-structured error, and noise. The boundary component is measured by the packet projections \(\Pi_\beta r_S\). \(\square\)

### Interpretation

Raw surprise says "this observation was improbable." Boundary surprise says "this packet is missing."

---

## 7. Theorem 4. Accuracy Decomposition Theorem

### Statement

Accuracy is packet-resolved. For a retained sector \(S\),
\[
\mathrm{Accuracy}_S
=
\sum_{\alpha\in S}A_\alpha
+
\sum_{\beta\in\partial S}A_\beta^{\mathrm{available}}
-
A_{\mathrm{shortcut}}
+
A_{\mathrm{noisefit}},
\]
where
\[
A_\beta^{\mathrm{available}}
=
\mathrm{Acc}(S+\beta)-\mathrm{Acc}(S)
\]
is the accuracy gain available by admitting boundary packet \(\beta\).

### Proof

Accuracy is
\[
\mathbb E_Q[\ln P(y|x)].
\]
Write the log likelihood in the packet basis of the finite coordinate algebra. Since the observation model is finite, the log likelihood is a finite function and can be decomposed into retained, boundary, and residual packets. The retained terms yield \(\sum_{\alpha\in S}A_\alpha\). If a boundary packet \(\beta\) is not represented, its contribution appears only as latent gain under the model extension \(S+\beta\). Define this gain by the difference in held-out log likelihood or expected log likelihood:
\[
A_\beta^{\mathrm{available}}
=
\mathrm{Acc}(S+\beta)-\mathrm{Acc}(S).
\]
Shortcut accuracy is the portion of apparent accuracy that depends on support restrictions rather than closure. Noise-fit is apparent accuracy gained by fitting random fluctuations. Subtracting or separately tracking these gives the displayed decomposition. \(\square\)

### Interpretation

Accuracy is not trustworthy until it is closure-resolved. Shortcut learning is high scalar accuracy in a nonclosed sector.

---

## 8. Theorem 5. Complexity / Closure Budget Theorem

### Statement

Complexity decomposes into
\[
\mathrm{Complexity}_S
=
C_{\mathrm{reweight}}
+
C_{\mathrm{closure}}
+
C_{\mathrm{compression}}
+
C_{\mathrm{external}}
+
C_{\mathrm{governance}}.
\]
Packetwise,
\[
C_{\mathrm{closure}}
=
\sum_{\beta\in\partial S}
\kappa_\beta\,\mathbf 1_{\beta\ \mathrm{admitted}}.
\]
Exact internal structural updating is possible only if available capacity exceeds the closure cost of the required packets.

### Proof

In standard FEP,
\[
\mathrm{Complexity}
=
D_{KL}[Q(x)\|P(x)].
\]
For a fixed model class, this measures reweighting from prior to posterior. But changing the representation class changes which coordinates are available. T16 proved that exact closure requires enough capacity to represent \(\operatorname{Cl}_{\mathcal T}(S)\). Therefore posterior change decomposes into: reweighting existing coordinates, adjoining missing coordinates, compressing or projecting them under finite capacity, routing unresolved components to tools/memory/environment, and enforcing governance constraints.

Since each finite boundary packet \(\beta\) has a representation cost \(\kappa_\beta\), the closure component is the sum of admitted packet costs. If the capacity budget is insufficient, the system must compress, ignore, hallucinate, or route externally. \(\square\)

### Interpretation

Changing weights and changing ontology are different kinds of complexity.

---

## 9. Theorem 6. Divergence as Projection Mismatch Theorem

### Statement

The divergence between approximate and required beliefs decomposes as
\[
D_S
=
\sum_{\alpha\in S}D_\alpha
+
\sum_{\beta\in\partial S}D_\beta
+
D_{\mathrm{gauge}}
+
D_{\mathrm{noise}},
\]
where
\[
D_\beta
\simeq
\left\|
\Pi_\beta(Q_{\mathrm{needed}}-Q_S)
\right\|^2
\]
in a local information metric.

### Proof

In a finite exponential family chart, the KL divergence has local quadratic approximation given by the Fisher metric:
\[
D_{KL}(Q_1\|Q_0)
=
\frac12\|\theta_1-\theta_0\|_F^2
+
O(\|\theta_1-\theta_0\|^3).
\]
Decompose the parameter displacement into retained, boundary, gauge, and noise directions:
\[
\theta_{\mathrm{needed}}-\theta_S
=
\Pi_S\Delta\theta+\Pi_{\partial S}\Delta\theta+\Pi_{\mathrm{gauge}}\Delta\theta+\Pi_N\Delta\theta.
\]
The quadratic form splits in a Fisher-orthogonal gauge, and in a general frame splits after Gram/Schur correction. The boundary component is exactly the projection of the required belief displacement onto missing packets. \(\square\)

### Interpretation

Divergence should not be read only as "how much I changed my mind." It should ask "where did my mind need a coordinate it did not have?"

---

## 10. Theorem 7. Precision as Boundary Gain Theorem

### Statement

Precision weighting is boundary gain control. If \(r_S\) decomposes into packet residuals, then precision acts as
\[
\|r_S\|_\Lambda^2
=
\sum_\gamma
\lambda_\gamma
\|\Pi_\gamma r_S\|^2
+
\text{cross terms}.
\]
Attention is the dynamic policy that chooses or modulates the gains \(\lambda_\gamma\) across retained, boundary, and noise channels.

### Proof

In predictive-coding and active-inference formulations, precision weights prediction errors by inverse variance or gain. Let \(\Lambda\) be the precision operator. Diagonalize or block-diagonalize \(\Lambda\) in a packet frame:
\[
\Lambda\sim \operatorname{diag}(\lambda_\gamma).
\]
Then the precision-weighted error is a weighted sum over packet residuals. Increasing \(\lambda_\beta\) amplifies boundary packet \(\beta\); decreasing it damps a channel as noise or irrelevant variation.

T16 proved that attention routes boundary interactions conditionally. Therefore attention implements dynamic precision assignment over packet channels. \(\square\)

### Interpretation

Precision is not merely confidence. It is a policy for deciding which residual channels are allowed to matter.

---

## 11. Theorem 8. Expected Free Energy as Active Boundary Functional

### Statement

Expected free energy admits the T17 expansion
\[
G_T(\pi)
=
\mathrm{Risk}_{\mathcal G}(\pi)
+
\mathrm{Ambiguity}(\pi)
+
K_C(\pi)
-
\Delta\mathrm{Cl}_S(\pi)
+
B_{\mathrm{unresolved}}(\pi),
\]
where \(\Delta\mathrm{Cl}_S(\pi)\) is expected closure gain and \(B_{\mathrm{unresolved}}\) is expected residual boundary cost.

### Proof

Start with the active-inference decomposition
\[
G(\pi)
=
-
\mathbb E
\left[
D_{KL}(Q(\tilde x|\tilde y,\pi)\|Q(\tilde x|\pi))
\right]
-
\mathbb E[\ln P(\tilde y|C)].
\]
The first term is information gain. Packet-decompose the future posterior displacement:
\[
D_{KL}(Q(\tilde x|\tilde y,\pi)\|Q(\tilde x|\pi))
=
\sum_\gamma D_\gamma(\pi).
\]
The part that identifies or resolves missing packets is \(\Delta\mathrm{Cl}_S(\pi)\). The part that merely changes retained weights remains ordinary reweighting information. The pragmatic term becomes governance risk because preferences define allowed outcome/state completions:
\[
\mathrm{Risk}_{\mathcal G}(\pi)
=
D_{KL}(Q(\tilde y|\pi)\|P_{\mathcal G}(\tilde y)).
\]
Expected ambiguity remains the entropy of the observation channel, but now interpreted as the difficulty of assigning residuals to packets:
\[
\mathrm{Ambiguity}(\pi)
=
\mathbb E_{Q(\tilde x|\pi)}
H[P(\tilde y|\tilde x)].
\]
Capacity and compression costs enter from Theorem 5. Unresolved future boundary costs enter when a policy predicts residual packets that remain outside the retained or external completion channels. Collecting terms yields the displayed functional. \(\square\)

### Interpretation

A good policy does not only seek reward or uncertainty reduction. It seeks the observations that resolve the right boundary at acceptable cost under governance.

---

## 12. Theorem 9. Perception-Action Completion Duality Theorem

### Statement

Perception and action are dual boundary-completion operations:
\[
\text{perception}: S\to S+\beta
\quad\text{or}\quad
\theta_S\to\theta_S+\Delta\theta_S,
\]
\[
\text{action}: \Omega\to\Omega'
\quad\text{so that}\quad
\partial S\ \text{is sampled, reduced, or externally completed}.
\]
The active-inference perception/action distinction is the T17 internal/external completion distinction.

### Proof

Perception updates beliefs so observations become explainable by the model. In T17 this is reweighting or adjoining representation packets. Action changes the observations sampled by the agent. In T17 this changes the boundary interface, either selecting observations that disambiguate missing packets or altering the world so retained-sector predictions are fulfilled. T15 and T16 already proved that tools, memory, retrieval, environment interaction, and user feedback are external boundary completion. Thus perception is internal closure, while action is external boundary routing and completion. \(\square\)

### Interpretation

Belief revision and environmental action are complementary ways of reducing the same boundary obstruction.

---

## 13. Theorem 10. Markov Blanket as Boundary Interface Theorem

### Statement

A Markov blanket is a statistical boundary interface through which retained sectors exchange packet evidence with their environment. In T17 language, it is the channel that separates internal closure from external completion.

### Proof

A Markov blanket separates internal states from external states by sensory and active states. Conditional independence means internal and external variables interact only through the blanket. In finite observable language, this says that the projection from external packet structure into internal retained variables factors through sensory channels, and the projection from internal policy to external change factors through active channels.

Therefore unresolved boundary packets outside the system can only be detected through sensory blanket projections and can only be modified through active blanket projections. The blanket is the interface of boundary detection and boundary completion. \(\square\)

### Interpretation

The Markov blanket is not merely a separator. It is the interface through which missing structure becomes surprise and through which action manages surprise.

---

## 14. Theorem 11. Matched-Surprise Separation Theorem

### Statement

There exist finite environments in which two episode classes have equal scalar surprise under a retained model,
\[
\mathbb E[\mathcal S_S(y)|E_{\mathrm{noise}}]
=
\mathbb E[\mathcal S_S(y)|E_{\mathrm{struct}}],
\]
but differ in boundary accuracy gain:
\[
\mathbb E[\Delta A_{\partial S}|E_{\mathrm{struct}}]
>
\mathbb E[\Delta A_{\partial S}|E_{\mathrm{noise}}].
\]
Therefore raw surprise cannot determine the correct belief update, while packet-resolved surprise and accuracy gain can.

### Proof

Take \(z_i\in\{-1,+1\}\) and retained sector \(S=\operatorname{span}\{z_0\}\). Define the structural class
\[
y=z_0z_1
\]
under a balanced distribution for \(z_1\). Define the noise class
\[
y=z_0
\]
with exactly half the labels flipped at random. Under the retained model \(S\), both classes produce the same expected error rate and thus can be matched in scalar surprise.

However, in the structural class the residual correlates with the packet
\[
\beta_\star=z_0z_1.
\]
Adjoining \(\beta_\star\) makes the rule linearly representable and increases held-out accuracy. In the noise class, no fixed packet explains the random flips across a verification window, so expected packet-resolved accuracy gain is small or zero after closure cost. Thus scalar surprise is equal while structural update value differs. \(\square\)

### Interpretation

This theorem is the formal core of Experiment E2. Surprise can be matched; update-worthiness can still differ.

---

## 15. Theorem 12. Active Boundary Fixed-Point Theorem

### Statement

Define the governed active completion operator
\[
\widehat S_{\mathcal G,C}
=
\mathcal G\circ
\mathcal E\circ
\mathcal K_C\circ
\operatorname{Cl}_{\mathcal T}.
\]
Here \(\operatorname{Cl}_{\mathcal T}\) closes under task interactions, \(\mathcal K_C\) compresses under capacity, \(\mathcal E\) routes unresolved boundaries externally, and \(\mathcal G\) enforces governance. An active intelligent system seeks task-relative fixed points
\[
\widehat S_{\mathcal G,C}=S.
\]
At such a fixed point, expected free energy is minimized subject to closure, capacity, external completion, and governance constraints.

### Proof

T13 proved closure is a finite renormalization operator. T15 proved completion adds refinement and external/archimedean boundary terms. T16 proved learned intelligence is governed open completion under capacity. Composing these operations gives \(\widehat S_{\mathcal G,C}\).

If \(S\) is not a fixed point, then some task interaction, capacity compression, external routing, or governance constraint changes it. This nonzero change appears as expected boundary cost or risk in \(G_T\). If \(S\) is a fixed point, no further forced boundary update is required relative to the task/environment class. Therefore minimizing the active boundary functional is equivalent to approaching fixed points of governed active completion. \(\square\)

### Interpretation

Cognition is not only prediction. It is fixed-point seeking under open boundary constraints.

---

## 16. Empirical Study 1: Conductor/XOR Boundary Surprise

### Setup

Coordinates:
\[
z_i\in\{-1,+1\}.
\]
The true label is
\[
y=\mathbf 1[z_0z_1=+1].
\]
Training data is biased so \(z_1=+1\) with probability \(0.96\). Thus the shortcut
\[
y\approx \mathbf 1[z_0=+1]
\]
works in-distribution but fails under a boundary-exposing distribution shift.

The retained sector is first-order:
\[
S_1=\operatorname{span}\{z_0,\ldots,z_{d-1}\}.
\]
The boundary candidates are pair packets:
\[
\partial_2S_1=\{z_iz_j:0\le i<j<d\}.
\]

The T-boundary score is
\[
B(\phi_{ij})
=
\frac{|\langle r,\phi_{ij}\rangle|}
{\sqrt{\langle \phi_{ij}^2\rangle}},
\qquad
\phi_{ij}=z_iz_j.
\]

### Main result

In the \(d=8\) main run:

```text
candidate pair packets = 28
initial labels = 128
seeds = 50
budgets = 0, 4, 8, 16, 32, 64 boundary-exposing labels
```

The T-boundary method selected the true hidden packet \(z_0z_1\) in:

```text
300 / 300 trials.
```

With 4 boundary-exposing labels:

```text
OOD accuracy = 1.000
forced-shift accuracy = 1.000
```

The shortcut baseline remained near:

```text
OOD accuracy = 0.580
forced-shift accuracy = 0.162
```

### Stress result

In the \(d=32\) stress run:

```text
candidate pair packets = 496
seeds = 30
```

The T-boundary method selected the true packet in:

```text
180 / 180 trials.
```

It reached:

```text
OOD accuracy = 0.997 with 8 labels
OOD accuracy = 1.000 with 16 labels
```

### Interpretation

E1 shows that boundary surprise identifies the missing belief update:
\[
\{z_i\}\longrightarrow \{z_i,z_0z_1\}.
\]
This is not merely better prediction. It is representation repair.

---

## 17. Empirical Study 2: Matched-Surprise Active Inference

### Setup

The retained sector is
\[
S=\operatorname{span}\{z_0\}.
\]
Two episode classes are constructed.

Structural:
\[
y=z_0z_1.
\]

Noise:
\[
y=z_0
\]
with exactly half the labels flipped randomly.

Both produce matched scalar surprise under the retained model. Only the structural episode contains a stable missing packet.

The T-agent computes the boundary packet score, selects \(\hat\beta\), then measures packet-resolved accuracy gain:
\[
\Delta A_{\hat\beta}
=
\mathcal L(S)-\mathcal L(S+\hat\beta).
\]
It updates structurally only if
\[
\Delta A_{\hat\beta}>C_{\mathrm{closure}}.
\]

### Main result

In the \(d=16\) main run:

```text
candidate pair packets = 120
initial labels = 512
seeds = 200
episodes = 2,000
```

Mean scalar surprise was matched:

| evidence labels | structural surprise | noise surprise |
|---:|---:|---:|
| 8 | 1.637 | 1.650 |
| 16 | 1.638 | 1.637 |
| 32 | 1.647 | 1.647 |
| 64 | 1.660 | 1.643 |
| 128 | 1.646 | 1.649 |

Scalar surprise could not separate structure from noise:

| evidence labels | scalar surprise AUC | T accuracy-gain AUC |
|---:|---:|---:|
| 8 | 0.472 | 1.000 |
| 16 | 0.508 | 1.000 |
| 32 | 0.514 | 1.000 |
| 64 | 0.537 | 1.000 |
| 128 | 0.495 | 1.000 |

The scalar-surprise agent updated on both classes:

| evidence labels | scalar TPR | scalar FPR | T-boundary TPR | T-boundary FPR |
|---:|---:|---:|---:|---:|
| 8 | 1.000 | 1.000 | 1.000 | 0.000 |
| 16 | 1.000 | 1.000 | 1.000 | 0.000 |
| 32 | 1.000 | 1.000 | 1.000 | 0.000 |
| 64 | 1.000 | 1.000 | 1.000 | 0.000 |
| 128 | 1.000 | 1.000 | 1.000 | 0.035 |

### Stress result

In the \(d=64\) stress run:

```text
candidate pair packets = 2,016
episodes = 480
```

| evidence labels | scalar surprise AUC | T accuracy-gain AUC | T-boundary TPR | T-boundary FPR |
|---:|---:|---:|---:|---:|
| 8 | 0.569 | 0.844 | 0.700 | 0.000 |
| 16 | 0.461 | 0.997 | 0.983 | 0.000 |
| 32 | 0.538 | 1.000 | 1.000 | 0.000 |
| 64 | 0.493 | 1.000 | 1.000 | 0.000 |

### Interpretation

E2 provides the following empirical distinction:
\[
\text{noise surprise}\neq \text{boundary surprise}.
\]
Scalar FEP surprise says both episode types are surprising. T17 says only one deserves a structural belief update.

---

## 18. Empirical Study 3: Boundary-Cue T-Maze

### Setup

E1 and E2 test diagnosis. E3 tests active policy selection.

The environment is a two-arm cue task. A hidden context
\[
c\in\{-1,+1\}
\]
determines the rewarded arm. The agent may inspect a cue
\[
q\in\{-1,+1\}
\]
at cost
\[
\lambda_{\mathrm{cue}}=0.05.
\]
It also observes visible gate features
\[
g=(g_0,\ldots,g_{m-1}),\qquad g_j\in\{-1,+1\}.
\]
The retained model assumes
\[
q=c.
\]
The candidate boundary packets are transformed cue rules
\[
\beta_j=qg_j.
\]

Two conditions are presented.

Structural:
\[
q=cg_0.
\]

Noise:
\[
q=c
\]
with exactly half the cue labels randomly flipped.

The two conditions have matched scalar surprise under the retained model, but only the structural condition has a stable boundary packet.

### Agents

The standard active-inference-style agent evaluates cue inspection by an expected-free-energy score:
\[
-G(\mathrm{inspect})
=
\mathrm{PragmaticValue}
+
\mathrm{EpistemicValue}
-
\lambda_{\mathrm{cue}}.
\]
With cue reliability \(r\),
\[
\mathrm{PragmaticValue}=r,
\qquad
\mathrm{EpistemicValue}=\log 2-H(r,1-r).
\]
The entropy term was computed with the `pymdp` stable entropy primitive.

The scalar-precision agent treats high scalar surprise as cue unreliability and downweights the cue in both conditions.

The T17 boundary agent scores
\[
B_j=|\langle c q,g_j\rangle|,
\]
selects the leading candidate, and admits it only when held-out boundary accuracy gain exceeds closure cost:
\[
\Delta A_{\hat\beta}
=
\mathcal L(S)-\mathcal L(S+\hat\beta)
>
C_{\mathrm{closure}}.
\]
Here
\[
C_{\mathrm{closure}}=0.75.
\]

### Main result

The main run used:

```text
candidate gate features = 16
seeds = 200
budgets = 8, 16, 32, 64, 128 evidence trials
eval trials per episode = 512
episodes = 2,000
cue reliability = 0.92
cue cost = 0.05
closure cost = 0.75
```

Boundary discrimination:

| evidence trials | scalar surprise AUC | boundary score AUC | boundary gain AUC | true gate rate | T17 TPR | T17 FPR |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.500 | 0.928 | 1.000 | 1.000 | 1.000 | 0.025 |
| 16 | 0.500 | 1.000 | 1.000 | 1.000 | 1.000 | 0.005 |
| 32 | 0.498 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| 64 | 0.505 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| 128 | 0.518 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |

Matched scalar surprise:

| evidence trials | structural surprise | noise surprise | structural gain | noise gain |
|---:|---:|---:|---:|---:|
| 8 | 1.305 | 1.305 | 1.221 | 0.018 |
| 16 | 1.305 | 1.305 | 1.221 | -0.018 |
| 32 | 1.305 | 1.305 | 1.221 | -0.027 |
| 64 | 1.305 | 1.305 | 1.221 | -0.006 |
| 128 | 1.305 | 1.305 | 1.221 | -0.001 |

Policy net reward in the structural condition:

| evidence trials | standard AIF | scalar precision | T17 boundary | oracle |
|---:|---:|---:|---:|---:|
| 8 | 0.450 | 0.500 | 0.950 | 0.950 |
| 16 | 0.450 | 0.500 | 0.950 | 0.950 |
| 32 | 0.450 | 0.500 | 0.950 | 0.950 |
| 64 | 0.450 | 0.500 | 0.950 | 0.950 |
| 128 | 0.450 | 0.500 | 0.950 | 0.950 |

Policy net reward in the noise condition:

| evidence trials | standard AIF | scalar precision | T17 boundary | oracle |
|---:|---:|---:|---:|---:|
| 8 | 0.450 | 0.500 | 0.498 | 0.500 |
| 16 | 0.450 | 0.500 | 0.500 | 0.500 |
| 32 | 0.450 | 0.500 | 0.500 | 0.500 |
| 64 | 0.450 | 0.500 | 0.500 | 0.500 |
| 128 | 0.450 | 0.500 | 0.500 | 0.500 |

### Stress result

The stress run used:

```text
candidate gate features = 128
episodes = 1,000
```

| evidence trials | scalar surprise AUC | boundary score AUC | boundary gain AUC | true gate rate | T17 TPR | T17 FPR |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.500 | 0.670 | 1.000 | 1.000 | 1.000 | 0.020 |
| 16 | 0.500 | 1.000 | 1.000 | 1.000 | 1.000 | 0.010 |
| 32 | 0.515 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| 64 | 0.515 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| 128 | 0.510 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |

The larger candidate set weakens the raw boundary score at 8 evidence trials, but held-out boundary gain remains decisive.

### Interpretation

E3 establishes the policy-level form of the T17 claim:
\[
\boxed{
\text{boundary-resolved surprise changes epistemic action selection.}
}
\]
Standard active-inference-style policy selection overuses the cue because its retained model says the cue is reliable. Scalar precision control underuses the cue because it treats matched surprise as unreliability. The T17 boundary agent uses the cue exactly when the residual identifies a stable rule packet.

---

## 19. The New Active-Inference Equation

The standard prospective equation is
\[
\pi^\star
=
\arg\min_\pi G(\pi).
\]

The T17 active-boundary equation is
\[
\boxed{
\pi^\star
=
\arg\min_\pi
\left[
\mathrm{Risk}_{\mathcal G}(\pi)
+
\mathrm{Ambiguity}(\pi)
+
K_C(\pi)
+
B_{\mathrm{unresolved}}(\pi)
-
\Delta\mathrm{Cl}_S(\pi)
\right].
}
\]

Where:

| Term | Meaning |
|---|---|
| \(\mathrm{Risk}_{\mathcal G}\) | divergence from governed/preferred outcomes or states |
| \(\mathrm{Ambiguity}\) | observation-channel uncertainty that prevents packet assignment |
| \(K_C\) | capacity and compression cost |
| \(B_{\mathrm{unresolved}}\) | expected future boundary leakage |
| \(\Delta\mathrm{Cl}_S\) | expected closure gain, information that identifies useful missing packets |

This reduces to the ordinary expected-free-energy story after summing packet terms and suppressing explicit boundary structure. But the expanded form tells us which surprise should change beliefs.

---

## 20. Practical Consequences

### 20.1 For active inference

The framework suggests a diagnostic addition to active-inference agents:

1. compute ordinary free energy or expected free energy;
2. decompose residuals by packet/channel;
3. estimate packet-resolved accuracy gain;
4. decide whether to reweight, close, compress, route externally, or ignore.

### 20.2 For deep learning

Shortcut learning becomes:
\[
\text{high scalar accuracy in a nonclosed sector}.
\]
The fix is not only more data. It is boundary-aware evidence collection and closure.

### 20.3 For AI agents

Tools and memory become external completion channels. A model should call a tool when:
\[
B_{\mathrm{unresolved}}
>
C_{\mathrm{external}}
\]
and internal closure is too costly or impossible.

### 20.4 For alignment

Preferences \(C\) are not mere rewards. They are governance constraints on completion:
\[
P(\tilde y|C)\quad\leadsto\quad P_{\mathcal G}(\tilde y).
\]
Alignment is the rule that unresolved boundaries may be completed only through governed channels.

---

## 21. Limitations and Next Experiments

The current empirical tests use synthetic packet dictionaries. They prove that the T17 decomposition has empirical content, not that it solves representation discovery in full generality.

Next tests should include:

1. active query selection, where the agent chooses which boundary-exposing intervention to perform;
2. hierarchical packets, where a missing factor is not pairwise;
3. noisy structural packets, where boundary and stochastic noise coexist;
4. image or language shortcuts, where packets correspond to learned probes or SAE features;
5. tool-use environments, where external completion competes with internal closure;
6. a fully native discrete active-inference implementation where \(G_T(\pi)\) is compared directly with standard \(G(\pi)\) across multi-step policies.

The important criterion is not only accuracy. It is whether the system updates on structurally relevant surprise.

---

## 22. Conclusion

Active Inference says that perception, action, learning, attention, and planning minimize free energy. T17 agrees, but expands the ledger:
\[
\text{Free energy}
=
\text{retained-sector cost}
+
\text{boundary cost}
+
\text{noise}
+
\text{governance}.
\]

The decisive move is packet resolution:
\[
\boxed{
\text{surprise should be decomposed before it is trusted.}
}
\]

Raw surprise can be caused by noise. It can be caused by a missing interaction. It can be caused by a bad precision assignment. It can be caused by a governance conflict. A scalar total does not tell the agent which operation is appropriate.

Active Boundary Inference says:
\[
\boxed{
\text{intelligence is free-energy minimization by governed boundary completion.}
}
\]

The controlled experiments provide initial empirical support for that claim. E1 shows that boundary surprise names a missing representation packet. E2 shows that two episodes can be equally surprising while only one deserves structural belief updating. E3 shows that boundary-resolved surprise changes active policy selection and can recover oracle-level cue-use behavior under matched scalar surprise.

This is where T17 lands:
\[
\boxed{
\text{structurally relevant surprise is the surprise that points to closure.}
}
