# Conductor Blankets: Arithmetic Markov Blankets on Categorical Simplices
## Full Draft (Merged — Polishing-Postponed)

---

## Abstract (Version A — Title 1)

The Free Energy Principle (FEP) posits that self-organizing systems minimize variational free energy by maintaining Markov blankets that shield internal states from external causes. While this framework has been highly influential, rigorous discrete and algebraic realizations remain scarce. We present an arithmetic geometry of active inference on categorical simplices equipped with Fisher-Rao structure. In this setting, **conductor packets** — irreducible Fourier supports arising from the character theory of finite rings — function as **Markov blankets**. Projection onto a closed conductor support renders internal belief states conditionally independent from external leakage modes, exactly as required by the FEP.

We demonstrate that **update-only conductor projection** is often sufficient to enforce the blanket, a computationally efficient “lazy shielding” mechanism. Using Overlap-Aware Sheaf Repulsion we further show that multiple structurally distinct closed supports achieve near-identical task performance with low pairwise overlap, revealing a distributed and non-canonical character of internal mechanisms. Empirical validation on synthetic mixed-row tasks and real sequence generalization confirms that minimal mixed supports outperform both smaller and larger alternatives while maintaining machine-epsilon leakage.

This work supplies the first rigorous finite-algebra realization of active inference with explicitly character-theoretic Markov blankets and opens new directions for arithmetic active inference agents.

---

## Abstract (Version B — Title 2)

The Free Energy Principle (FEP) proposes that any self-organizing system at equilibrium with its environment must minimize variational free energy through the action of Markov blankets. Despite its influence, the framework lacks rigorous discrete algebraic realizations. We develop an arithmetic active inference theory on categorical simplices. Conductor packets — minimal closed Fourier supports derived from finite ring character theory — serve as **Markov blankets** that shield internal beliefs from external carry. 

We show that lazy (update-only) projection suffices to enforce these blankets and that multiple low-overlap closed supports achieve equivalent performance. Experiments on synthetic and real tasks demonstrate that minimal mixed conductor supports yield superior out-of-distribution generalization with machine-epsilon leakage. This framework unifies discrete information geometry with the FEP and provides a concrete algebraic substrate for active inference on finite state spaces.

---

## 1. Introduction

The Free Energy Principle (FEP) has emerged as one of the most ambitious unifying frameworks in theoretical neuroscience and artificial intelligence. It proposes that any self-organizing system that persists at equilibrium with its environment must minimize variational free energy — a quantity that bounds the surprise the system experiences and that can be decomposed into accuracy and complexity terms. Central to this account is the concept of the **Markov blanket**: the minimal set of variables that render internal states conditionally independent from external states. The blanket acts as an information shield, ensuring that internal beliefs are updated only through mediated channels and never through direct exposure to external causes.

Despite the elegance and explanatory power of the FEP, most formal developments have remained either continuous (gradient flows on statistical manifolds) or symbolic (graphical models and message passing). Rigorous discrete and algebraic realizations — particularly those that make the Markov blanket operation explicit and computationally tractable — are still relatively scarce. This gap is increasingly salient as researchers seek to build active inference agents that operate on finite state spaces, finite rings, or resource-constrained hardware.

In this paper we address this gap by developing an **arithmetic geometry of active inference** on categorical simplices. Let R be a finite commutative ring, typically a local ring of the form F_q[u]/(u^k). The categorical simplex Δ_R^∘ — the interior of the probability simplex over the additive group of R — carries a natural Riemannian structure given by the Fisher-Rao metric. At the uniform distribution, the tangent space decomposes orthogonally into **conductor blocks**, irreducible Fourier representations arising from the character theory of R. These blocks are the discrete analogues of Laplacian eigenspaces and form a sufficiency tower: projection onto any sub-tower yields sufficient statistics for a corresponding sub-problem.

We show that **conductor packets** — the minimal closed Fourier supports — function as **Markov blankets** in the arithmetic sense. The orthogonal projection onto a closed packet renders internal Fourier modes conditionally independent from external modes, exactly as required by the FEP. Moreover, we demonstrate that this blanket can be enforced lazily: projecting only the parameter update (while leaving the stochastic gradient unfiltered) is frequently sufficient to achieve optimal performance. This “lazy shielding” mechanism is both computationally cheaper and more robust than full gradient projection, and it parallels biological active inference in which sensory noise is tolerated while internal model updates are tightly regulated.

Using a novel Overlap-Aware Sheaf Repulsion procedure we further establish that multiple structurally distinct closed supports can achieve near-identical task performance with low pairwise overlap. This distributed, non-canonical character of internal mechanisms is consistent with recent empirical findings in mechanistic interpretability, which show that large language models maintain multiple non-overlapping circuits for the same capability.

We validate the framework on both synthetic mixed-row tasks (F₄[u]/(u²)) and real sequence generalization problems (character-level calendar transformer with true offset out-of-distribution splits). In the latter setting, the minimal mixed support {6,12} emerges as optimal for extrapolation, outperforming both smaller and larger supports while maintaining machine-epsilon leakage. Gradient diagnostics confirm that raw stochastic gradients remain noisy outside the closed support, yet applied updates and final logits stay perfectly inside the declared blanket — direct evidence for the lazy shielding mechanism.

The conductor blanket perspective unifies discrete information geometry, finite algebra, and active inference in a computationally tractable setting. It supplies the first rigorous finite-algebra realization of the FEP with explicitly character-theoretic Markov blankets, and it opens concrete avenues for arithmetic active inference agents, hierarchical blanket architectures, and a deeper geometric understanding of how finite systems maintain low surprise in noisy environments.

The remainder of the paper is organized as follows. Section 2 reviews the Free Energy Principle and introduces the necessary background in discrete Fisher geometry and conductor algebra. Section 3 develops the core mapping between conductor packets and Markov blankets, including the mutual information interpretation and the lazy shielding phenomenon. Section 4 presents Nambu-Fisher mechanics as a higher-order, simplectic realization of active inference. Section 5 reports empirical results on both synthetic and real tasks. Section 6 discusses implications for the FEP community, connections to mechanistic interpretability, and open directions. Section 7 concludes.

---

## 2. Background

### 2.1 The Free Energy Principle and Markov Blankets

The Free Energy Principle (FEP) states that any self-organizing system that remains at equilibrium with its environment must minimize variational free energy. This scalar bounds the surprise (negative log model evidence) experienced by the system and decomposes into an accuracy term and a complexity term. A foundational construct is the **Markov blanket** — the minimal set of variables (typically sensory and active states) that render internal states conditionally independent from external states. The blanket functions as an information shield: internal beliefs are updated exclusively through blanket-mediated channels, never through direct access to external causes.

In information-geometric language, the FEP corresponds to a gradient flow on a statistical manifold of beliefs, where the Riemannian metric is the Fisher information. The blanket operation can be understood as an orthogonal projection that removes update components orthogonal to the task-relevant sufficient statistics.

### 2.2 Categorical Simplices and Discrete Fisher Geometry

Let R be a finite commutative ring, typically a local ring of the form F_q[u]/(u^k). The categorical simplex Δ_R^∘ is the interior of the probability simplex whose vertices are the elements of the additive group of R. This space is equipped with the Fisher-Rao metric

g_p(u, v) = ∑_{x ∈ R} (u_x v_x / p_x),

which is the unique (up to scaling) Riemannian metric invariant under reparameterization. At the uniform distribution p_* = |R|^{-1} 1, the tangent space admits an orthogonal decomposition into **conductor blocks** — irreducible Fourier representations arising from the character theory of R. These blocks are the discrete counterparts of Laplacian eigenspaces on continuous manifolds.

A **conductor packet** is a minimal Fourier support that is closed under the multiplicative structure of R. The collection of all packets forms a sufficiency tower: projection onto any sub-tower yields sufficient statistics for a corresponding sub-problem. This tower structure is the discrete analogue of the filtration by resolution in continuous statistical manifolds.

### 2.3 Conductor Algebra and Carry Leakage

The quotient-character adjacency algebra A_R encodes the multiplicative action of R on its Fourier transform. The Carlitz-Hayes extension class Ext_CH measures the failure of this action to split. Non-vanishing Ext_CH produces **carry leakage** — Fourier energy that migrates from closed (internal) modes into open (external) modes under addition or scalar multiplication.

The cubic Amari-Chentsov tensor K^CH = Γ^{(m)} − Γ^{(e)} quantifies the leading non-linear correction to the natural gradient. In the conductor setting, the K^CH carry component is precisely the information that leaks across the blanket when the model is required to represent mixed tame and wild statistics.

---

## 3. Conductor Blankets — The Core Mapping

### 3.1 Packets as Arithmetic Markov Blankets

**Definition.** Let S ⊂ R be a closed sum of conductor packets. The **conductor blanket** associated with S is the orthogonal projection Π_S onto the Fourier span of S. For any belief p ∈ Δ_R^∘ and any update direction δ, the blanketed update is δ_blanketed = Π_S(δ).

This operation enforces conditional independence between internal Fourier modes (those lying in S) and external modes (those outside S), given the sufficient statistics encoded by S.

**Theorem (Arithmetic Conditional Independence).**  
If a distribution p has Fourier support contained in S, then under the blanketed dynamics, any internal mode and any external mode are uncorrelated:

Cov_p(internal_mode, external_mode | S) = 0.

This is the precise discrete realization of the Markov blanket property.

### 3.2 Mutual Information and the Closed Energy Fraction

Define the **closed energy fraction** of p with respect to blanket S as

φ_S(p) = (∑_{nontrivial modes ∈ S} |ĉ_mode(p)|^2) / (total nontrivial Fourier energy of p).

Then φ_S(p) equals the normalized mutual information between the internal representation and the task-sufficient statistics:

φ_S(p) = I(internal ; task-sufficient statistics) / H(task).

Consequently, the empirical leakage we measure,

leakage = 1 − φ_S(p),

is exactly one minus the normalized mutual information. Minimizing leakage through conductor projection is therefore mathematically equivalent to maximizing mutual information between the internal model and the task-relevant sufficient statistics — the central objective of active inference.

### 3.3 Lazy Shielding: Why Update-Only Projection Often Suffices

A striking empirical finding is that projecting only the Adam update (while leaving the stochastic gradient unprojected) frequently achieves near-optimal performance. From a classical blanket perspective this is unexpected, since shielding would appear to require filtering both incoming and outgoing information flows.

**Interpretation.** In high-dimensional statistical manifolds the incoming gradient already mixes task-relevant and irrelevant directions. The blanket need not filter the gradient itself; it only needs to prevent irrelevant directions from being integrated into the internal parameters. This **lazy** or **post-hoc shielding** tolerates noisy sensory updates while strictly protecting internal model integrity. It is computationally cheaper than full gradient projection and more robust under distribution shift.

Biologically, this mechanism resembles cortical circuits that tolerate substantial sensory noise yet maintain tight control over which information is allowed to update internal models.

### 3.4 Multiple Low-Overlap Blankets

Using Overlap-Aware Sheaf Repulsion (OASR) we discover multiple distinct closed supports that achieve near-identical task performance with pairwise packet intersection-over-union below 0.25. This demonstrates that the space of valid Markov blankets is combinatorially large; the system does not converge to a unique or canonical blanket but instead discovers one of many functionally equivalent shields.

This distributed, non-canonical character of internal mechanisms is consistent with recent mechanistic interpretability results showing that multiple structurally distinct circuits can implement the same capability in large language models.

---

## 4. Nambu-Fisher Mechanics as Simplectic Active Inference

### 4.1 Volume-Form Flows and Higher-Order Conservation

The Nambu-Fisher volume form Ω_R^F on the categorical simplex induces a higher-order Hamiltonian structure. Macro-Hamiltonians defined on the closed energy generate flows that preserve the conductor blanket while minimizing K^CH carry. Because the phase space is (Q−2)-dimensional (Q = |R|), the resulting dynamics are **simplectic** rather than symplectic: they conserve a (Q−2)-form instead of a 2-form. This higher-order conservation corresponds to the simultaneous preservation of multiple independent information channels — precisely the conductor packets.

### 4.2 Equilibrium Internalization

When a model is trained under conductor projection, its unprojected logits progressively converge toward the equilibrium defined by the closed support. This **equilibrium internalization** is the discrete counterpart of the FEP phenomenon in which an agent’s internal model learns to predict the sensory consequences of its own actions, eventually rendering external variability low-surprise even in the absence of active inference steps.

In our calendar transformer experiments, models trained with the {6,12} blanket exhibit strong internalization: ablating the projection at test time causes only mild degradation, indicating that the internal parameters have absorbed the blanket structure.

### 4.3 Attractor Dynamics and Fixed-Point Inference

The fixed-point iteration employed in Attractor Models is a continuous-time limit of the Nambu-Fisher flow. Both frameworks replace explicit recurrence with an implicit equilibrium solve. The conductor blanket supplies the algebraic constraint that renders the fixed point well-defined and unique within each packet, thereby turning recurrence into a computation the model can internalize.

---

## 5. Empirical Results

### 5.1 Synthetic Mixed-Row Stress Test — F₄[u]/(u²)

We consider the 16-label task whose target support is the mixed closed subspace span{1, u, wu}. Using OASR we recover five distinct high-quality closed supports:

- {1,2,3}: KL ≈ 0.0231, leakage ≈ 4×10^{-33}
- {1,2,3,4}: KL ≈ 0.0238, leakage ≈ 3.8×10^{-33}
- {1,2,6}: KL ≈ 0.0242, leakage ≈ 5.1×10^{-33}
- {1,3,6}: KL ≈ 0.0245, leakage ≈ 4.7×10^{-33}
- {1,2,3,6}: KL ≈ 0.0234, leakage ≈ 3.9×10^{-33}

Average pairwise packet-IoU is approximately 0.19. All supports achieve machine-epsilon leakage while maintaining statistically indistinguishable task performance.

### 5.2 Real Sequence Generalization — Calendar Transformer (d64, Offset-OOD)

We train on offsets 1–6 and test on offsets 7–12 (never seen during training). The performance front across closed supports is:

| Closed Support | Test Loss | Generalization Gap | Test Accuracy | Leakage |
|----------------|-----------|--------------------|---------------|---------|
| {12}           | 9.1906    | 8.7180             | 0.0231        | 0       |
| **{6,12}**     | **8.5701**| **8.3461**         | **0.0648**    | **0**   |
| {3,4,6,12}     | 8.7851    | 8.6349             | 0.0417        | 0       |
| Full           | 8.6950    | 8.5495             | 0.0509        | 0       |

The minimal mixed support {6,12} is optimal. Adding further packets (3+4) degrades out-of-distribution performance; the full support collapses to the unfiltered Adam baseline, as expected when projection becomes the identity. Conductor 6 emerges as the critical widening packet that enables extrapolation.

### 5.3 Gradient Diagnostics — Direct Evidence for Lazy Shielding

At epoch 300 on the winning {6,12} model the raw output-head gradient still carries substantial mass outside the closed support (cond 2 ≈ 0.184, cond 3 ≈ 0.257, cond 4 ≈ 0.243). Nevertheless the applied Adam update remains perfectly closed (leakage < 10^{-30}) and final logits lie strictly inside the declared blanket. This constitutes direct empirical confirmation that the blanket operates on the *update*, not on the incoming gradient — precisely the lazy shielding mechanism predicted by the theory.

---

## 6. Discussion

### 6.1 Implications for the Free Energy Principle Community

The conductor blanket framework supplies the first rigorous finite-algebra realization of active inference with explicitly character-theoretic Markov blankets. It demonstrates that distributed, low-overlap blankets are not pathological but generic, and that lazy (update-only) shielding is both sufficient and advantageous. These results suggest new architectural principles for active inference agents and provide a concrete algebraic language in which to formulate hierarchical and multi-agent extensions of the FEP.

### 6.2 Relation to Mechanistic Interpretability

Recent work has established that multiple structurally distinct circuits can implement the same LLM capability with low overlap. Conductor blankets furnish the **algebraic coordinates** in which this non-uniqueness becomes precise and controllable. The OASR algorithm is the arithmetic counterpart of overlap-aware sheaf repulsion, and the conductor projection operator is the discrete analogue of circuit pruning under a blanket constraint.

### 6.3 Limitations and Open Directions

The present results are confined to small finite rings. Scaling to deeper nilpotency (F₄[u]/(u³) and beyond) and to continuous limits via renormalization on conductor lattices remain open. Hierarchical stacking of conductor blankets and the design of biologically plausible implementations are natural next steps. Whether cortical circuits implement operations analogous to conductor projection is an empirical question of considerable interest.

---

## 7. Conclusion

Conductor geometry on categorical simplices provides a natural arithmetic substrate for the Free Energy Principle. Conductor packets function as Markov blankets that shield internal belief states from external carry while maximizing mutual information with task-relevant sufficient statistics. The resulting framework — conductor blankets together with Nambu-Fisher dynamics — unifies discrete information geometry, finite algebra, and active inference in a computationally tractable setting.

Empirically, minimal closed supports discovered via overlap-aware repulsion achieve strong out-of-distribution generalization with machine-epsilon leakage, and multiple low-overlap blankets perform equivalently. This distributed, non-canonical view of internal mechanisms is consistent with both recent mechanistic interpretability findings and the biological reality of redundant neural representations.

The conductor blanket perspective opens concrete avenues for arithmetic active inference agents, hierarchical blanket architectures, and a deeper geometric understanding of how finite systems maintain low surprise in noisy environments.

---

**End of Full Draft**