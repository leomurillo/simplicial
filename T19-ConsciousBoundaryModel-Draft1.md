# T19 - Conscious Boundary Model

**Consciousness as Governed Active Boundary Completion at a Terminal Inner Screen**

**Leonardo Murillo Montero**

*First draft - May 26, 2026*

---

> *Consciousness is not raw information. It is lawful admission of boundary information into an active inner screen.*

---

## Abstract

**Situation.** T13 proved that projection creates boundary sources and that
renormalization is finite closure under conductor fusion. T14 proved that
curvature, beta source, Schur correction, and Noether defect are projection
boundary obstructions. T15 proved that open systems require terminal boundary
completion. T16 translated this into learned systems: attention, residuals,
memory, tools, and alignment are operations on representation boundaries. T17
expanded active inference into packet-resolved boundary surprise and boundary
gain. T18 added conformal governance: closure moves are lawful only when
calibrated boundary evidence admits them.

**Gap.** The T-series has a model of intelligence, action, governance, memory,
and free-energy minimization. It does not yet state what consciousness is in
the same mathematical language. Standard FEP accounts identify consciousness
with an inner Markov blanket, inner screen, global workspace, attention,
precision, or self-modeling. These accounts locate the interface, but they do
not yet specify which residuals become contents, which are noise, which are
action-relevant, which are governable, and which are only enabling background.

**Action.** We introduce the **Conscious Boundary Model**. A conscious system is
a governed active completion architecture with a terminal inner screen. The
screen is a Markov boundary inside the system. Its retained sector supplies the
current conscious model. Its boundary supplies candidate contents. Attention is
precision gain over packet residuals. Conscious access is the conformally
governed admission of action-relevant boundary packets into the active retained
sector.

**Result.** The core object is not a scalar consciousness variable. It is a
finite, set-valued, packet-resolved process
\[
\mathfrak C_t
\subseteq
H_{S_\star}\oplus H_{\partial S_\star}.
\]
The central equation is
\[
\boxed{
\mathfrak C_t
=
\operatorname{Adm}_{\alpha,\mathcal G,C}
\left(
S_{\star,t},
\partial S_{\star,t},
r_t,
\Lambda_t,
Z_t
\right).
}
\]
Here \(S_{\star,t}\) is the terminal inner retained sector, \(\partial
S_{\star,t}\) is its task boundary, \(r_t\) is residual surprise, \(\Lambda_t\)
is precision or attention gain, \(Z_t\) is the evidence episode, \(C\) is
capacity, \(\mathcal G\) is governance, and \(\alpha\) is the conformal error
level.

**Substrate.** Read dynamically, the retained sector is the slow-eigenfunction
chart of the inner transition — the recovery theorem of *Beyond the Conductor
Blind Spot* — and the candidate contents are the distributional rungs one order
above it, the two registers kept strictly apart and coinciding only at the
Gaussian corner. Two consequences are sharp: conscious action is world-optimal
up to a known nonlinear warp (Theorem 10), and learning *converts* conscious
boundary content into transparent retained chart, so that consciousness is the
flux across that moving boundary (Theorem 11).

**Top claim.**
\[
\boxed{
\text{consciousness}
=
\text{governed active boundary completion at a terminal inner screen}.
}
\]

**Keywords:** consciousness, active inference, Markov blanket, inner screen,
global workspace, boundary completion, attention, precision, conformal
governance, memory, self-model, reportability, terminal boundary.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| T1 Native Simplicial Chart | finite probability and observable spaces |
| T2 Cumulant Tower | packet interactions and connected residuals |
| T3 Character Orthogonality | packet decomposition and conductor channels |
| T11 Apex Vertex Calculus | boundary packets and fusion completion |
| T13 Exact Simplicial Renormalization | closure as finite boundary adjunction |
| T14 Projected Flatness | projected nonclosure as curvature and defect |
| T15 Finite-to-Archimedean Completion | terminal boundary completion |
| T16 Representation Closure | attention, memory, tools, and alignment as boundary operations |
| T17 Active Boundary Inference | packet-resolved free energy and precision as boundary gain |
| T18 Conformal Boundary Governance | finite-sample lawful admission of closure moves |
| CBS — Conductor Blind Spot | order-two curvature blind to the order-three cubic; non-Gaussian trigger \(\kappa_{\ge3}\neq0\) |
| Beyond CBS — Eigenfunction Identifiability | retained sector as slow-eigenfunction chart; faithful planning; reportable residue |

---

## 0. The Steelthread

The paper has one thread:

\[
\boxed{
\text{consciousness is admitted boundary information that can govern action.}
}
\]

The ten milestones are:

1. A screen is a retained sector with a Markov boundary.
2. An inner screen is a boundary inside an already bounded system.
3. A terminal inner screen is an irreducible active boundary.
4. Attention is precision gain over packet channels.
5. Conscious content is governed packet admission.
6. Conscious level is not content; it is a summary of admission capacity.
7. The self is the persistent governance center of active boundary routing.
8. Memory is stabilized boundary admission across time.
9. A conscious model is a fixed point of governed active inner completion.
10. Learning converts conscious content into transparent chart; consciousness
    is the flux across that boundary.

---

## 1. Basic Setting

Let \(\Omega\) be a finite state, data, body, or world space. Let
\[
H=\mathbb R^\Omega
\]
be the full observable space. A finite system never represents all of \(H\). It
retains a sector
\[
H_S\subseteq H
\]
and projects by
\[
\Pi_S:H\to H_S.
\]

For a task or world interaction
\[
V:H_S^{\otimes n}\to H,
\]
the boundary of \(S\) is
\[
\partial_{\mathcal T}S
=
\operatorname{supp}
\left((I-\Pi_S)V(H_S^{\otimes n})\right).
\]

T16 made this an architecture of intelligence. T17 made it active. T18 made it
lawful. T19 asks which such architectures are conscious.

---

## 2. Screens as Markov Boundary Sectors

### Definition 2.1. Finite Screen

A **finite screen** is a tuple
\[
\mathscr B=(I,Y,A,E;P)
\]
where:

- \(I\) is an internal state sector;
- \(Y\) is a sensory boundary sector;
- \(A\) is an active boundary sector;
- \(E\) is an external state sector;
- \(P\) is a probability law or transition law on the finite joint space.

The blanket sector is
\[
B=Y\oplus A.
\]

The screen satisfies the Markov boundary condition
\[
I\perp E\mid B.
\]

In a dynamical version, sensory states are influenced by external states and
not directly by internal states, while active states are influenced by internal
states and not directly by external states. Equivalently, in a local transition
or vector-field representation, the corresponding cross-couplings vanish.

### Definition 2.2. Screen Retained Sector

The screen determines a retained observable sector
\[
H_{\mathscr B}
=
\operatorname{span}
\left\{
\text{screen observables on } I,Y,A
\right\}
\subseteq H.
\]

The screen boundary is the task boundary
\[
\partial \mathscr B
=
\partial_{\mathcal T}H_{\mathscr B}.
\]

### Interpretation

A screen is not a picture. It is a finite interface through which a system
receives, weights, writes, and completes boundary information.

---

## 3. Nested Screens and the Terminal Inner Screen

A conscious organism or agent is not a single screen. It is a nested family
\[
\mathscr B_0\prec \mathscr B_1\prec\cdots\prec\mathscr B_L.
\]

The outer screens mediate body-world exchange. Inner screens mediate exchange
between subsystems of the agent.

### Definition 3.1. Inner Screen

A screen \(\mathscr B_k\) is **inner** when its external sector \(E_k\) is still
inside the organism-level or agent-level boundary.

Thus an inner screen separates one internal subsystem from another internal
subsystem.

### Definition 3.2. Terminal Inner Screen

An inner screen
\[
\mathscr B_\star=(I_\star,Y_\star,A_\star,E_\star;P)
\]
is **terminal** at task scale \(\mathcal T\) and resolution \(\epsilon\) when no
nontrivial subpartition of \(I_\star\) supports another active Markov screen
with boundary residual above \(\epsilon\).

Equivalently, there is no decomposition
\[
I_\star=I'\oplus Y'\oplus A'\oplus E'
\]
such that
\[
I'\perp E'\mid (Y'\oplus A')
\]
and such that \(A'\) can exert task-relevant active control on \(E'\) at the
declared scale.

### Interpretation

Terminal does not mean metaphysically simple. It means operationally
irreducible for the present system, scale, task, and observational gauge.

This supplies a mathematical version of phenomenological transparency. The
system can use the terminal screen, but it cannot step behind it as another
available object of mental action.

---

## 4. Boundary Residuals at the Inner Screen

Let \(S_{\star,t}\) be the retained sector of the terminal inner screen at time
\(t\). Let the screen predict an observation, lower-level state, or internal
message
\[
\hat y_t=G_{S_{\star,t}}(q_t,a_t),
\]
where \(q_t\) denotes current belief state and \(a_t\) denotes active or covert
action.

Given received evidence \(y_t\), define the residual
\[
r_t=y_t-\hat y_t.
\]

Choose a packet decomposition
\[
H
=
H_{S_{\star,t}}
\oplus
H_{\partial S_{\star,t}}
\oplus
H_N
\oplus
H_G,
\]
where \(H_N\) contains noise, optimization, and finite-sample terms, and
\(H_G\) contains governance or preference-conflict terms.

Then
\[
r_t
=
\Pi_{S_\star}r_t
+
\Pi_{\partial S_\star}r_t
+
r_{N,t}
+
r_{G,t}.
\]

Packetwise,
\[
\Pi_{\partial S_\star}r_t
=
\sum_{\beta\in\partial S_{\star,t}} r_{\beta,t}\phi_\beta.
\]

The scalar surprise
\[
\mathcal S_t=-\log P_{S_\star}(y_t)
\]
is only the aggregate. Conscious admission depends on the packet-resolved
terms.

### The retained sector is a slow chart

We have treated \(S_{\star,t}\) as given. We can now say what a learned terminal
screen *retains*. Let the inner screen carry successive covert states
\((u_t,u_{t+1})\) — two readings of the same inner variable one inner step apart,
the covert analogue of a positive pair — and define the **inner transition
operator**
\[
(T_\star\psi)(u)=\mathbb E\!\left[\psi(u_{t+1})\mid u_t=u\right]
\]
on \(L^2(p_\star)\), with \(p_\star\) the stationary inner law over \(n\) inner
coordinates. Detailed balance at the screen makes \(T_\star\) self-adjoint, with
eigenpairs
\[
1=\lambda_0>\lambda_1\ge\lambda_2\ge\cdots\ge 0,
\qquad
\varphi_0\equiv 1,\ \varphi_1,\ \varphi_2,\dots
\]
orthonormal in \(L^2(p_\star)\), and a **slow-feature gap** \(\gamma>0\)
separating the retained leaders from the rest.

T17's active inference already runs the two operations that pin this spectrum.
Aligning prediction to evidence minimises the covert step energy
\(\mathbb E\|u_{t+1}-u_t\|^2\); precision normalisation keeps the retained
coordinates non-degenerate, a whitening constraint
\(\mathbb E[u_iu_j]=\delta_{ij}\). Minimising covert alignment under whitening
is, identically, a Rayleigh problem on \(T_\star\); by the Ky Fan maximum
principle its solution is the span of the slowest non-constant modes. So the
retained sector a learned terminal screen settles on is the **slow-eigenfunction
chart**
\[
\boxed{\;
S_{\star,t}\ \simeq\ \operatorname{span}\Phi_1,
\qquad
\Phi_1=\big(\varphi_1^{(1)},\dots,\varphi_1^{(n)}\big)\;}
\]
— the slowest, most persistent coordinates of the inner world. This is the
recovery theorem of *Beyond the Conductor Blind Spot* (its Theorem 1), read
inside the screen: the retained sector is not an arbitrary span but exactly what
survives the inner step.

**What the candidate packets are.** The boundary \(\partial S_{\star,t}\) is the
complementary object: the structure *not already carried* by the slow chart. Two
spectral towers are now in play, and holding them apart is the one discipline
this section enforces.

- The **dynamical tower** is the eigenbasis of \(T_\star\). Its slow member
  \(\varphi_1\) is the retained coordinate, and — the Sturm–Liouville dichotomy
  — it is an *affine* function of the inner latent **if and only if the inner
  law is Gaussian**; for every other law it is monotone but **curved**, by a
  nonlinearity \(\nu_D=1-R^2\) (the defect of its best affine fit). This tower is
  \(S_\star\).
- The **distributional tower** is the cumulant / character grading of
  \(p_\star\) — the T2 cumulant tower on the T3 conductor lattice — whose
  order-two form is the Fisher metric and whose order-three form is the
  Amari–Chentsov cubic. The candidate packets \(\beta\in\partial S_\star\) live
  here.

The towers coincide only at the Gaussian / uniform corner; off it they split,
and the split is structured: the leading curved degree of the retained
coordinate is **exactly one below** the leading occupied cumulant rung of the
boundary, with the two locked near the corner as
\(\nu_D\propto(\text{leading cumulant})^2\) (*Beyond the Conductor Blind Spot*,
the two-registers bridge). We therefore keep \(S_\star\) **dynamical** and
\(\partial S_\star\) **distributional** throughout. Naming the retained
coordinate "the degree-one member of the cumulant tower" is false off the
Gaussian and is precisely the conflation the companion paper forbids.

**Why the Gaussian corner is the dull case.** When the inner law is Gaussian the
retained chart is a straight line: a linear — degree-one — read of the screen is
*complete* and there is no curved residue. Every richer screen is non-Gaussian,
\(\kappa_{\ge 3}\neq 0\) — exactly the trigger of the conductor blind spot — and
its retained coordinate is curved. Rich conscious content begins where the
screen leaves the Gaussian corner; §9 and Theorem 7 measure how much.

---

## 5. Attention as Precision Gain

Let \(\Lambda_t\) be the precision operator at the terminal inner screen. In a
packet gauge,
\[
\Lambda_t
=
\sum_{\gamma}
\lambda_{\gamma,t}\Pi_\gamma
+
\text{finite cross terms}.
\]

The precision-weighted residual is
\[
\|r_t\|_{\Lambda_t}^2
=
\sum_\gamma
\lambda_{\gamma,t}
\|\Pi_\gamma r_t\|^2
+
\text{cross terms}.
\]

### Definition 5.1. Attentional Gain

The **attentional gain** assigned to packet \(\gamma\) at time \(t\) is
\[
\lambda_{\gamma,t}.
\]

The packet is attention-amplified when
\[
\lambda_{\gamma,t}\ge \lambda_{\min}.
\]

### Interpretation

Attention is not a flashlight. It is dynamic gain over boundary channels. A
packet can be present in the system without being conscious if it is not
admitted through the terminal screen with sufficient gain.

In the spectral reading of §4, precision gain is also what *induces anisotropy*
across packets: by scaling channels unequally it separates the leading
eigenvalues, widens effective slow-feature gaps, and converts the rotation
ambiguity of an isotropic screen into individuated, disentangled admission — the
resolvability that §9.4 reads as clarity.

---

## 6. Boundary Gain and Admission Evidence

For an evidence episode \(Z_t\), define a boundary score
\[
s_\beta(Z_t)
=
\left|\langle r_t,\phi_\beta\rangle\right|
\]
or, preferably, a held-out boundary gain score
\[
\Delta A_\beta(Z_t)
=
\mathcal L(S_{\star,t};V_t)
-
\mathcal L(S_{\star,t}+\beta;V_t),
\]
where \(V_t\) is a verification window.

Let \(\kappa_\beta\) be the closure cost of admitting packet \(\beta\).

Define the net structural value
\[
N_\beta(Z_t)
=
\Delta A_\beta(Z_t)-\kappa_\beta.
\]

The packet is structurally worthwhile when
\[
N_\beta(Z_t)>0.
\]

---

## 7. Conformal Conscious Admission

T18 supplies a calibration ledger
\[
\mathcal L_{\star}
=
\{(Z_i,s_i,h_i,\kappa_i)\}_{i=1}^n
\]
for the terminal screen.

For each candidate completion \(h\in\mathcal H\), compute a conformal p-value
\[
p_h(Z_t)
=
\frac{
1+\#\{i\le n_h:s_{h,i}\le s_h(Z_t)\}
}{
n_h+1
}
\]
when larger scores are more compatible with \(h\).

The conformal boundary set is
\[
C_\alpha(Z_t)
=
\{h:p_h(Z_t)>\alpha\}.
\]

For a one-sided null gate, let \(h=0\) denote no structural boundary. Then
\[
p_0(Z_t)
=
\frac{
1+\#\{i:s_i^0\ge s(Z_t)\}
}{
n+1
},
\]
and
\[
G_\alpha(Z_t)=\mathbf 1\{p_0(Z_t)\le\alpha\}.
\]

---

## 8. The Conscious Content Set

Let \(\mathcal G\) be the governance specification. Let
\[
\operatorname{Allow}_{\mathcal G}\subseteq\mathcal B
\]
be the packet and route family allowed by that specification. Let \(C_t\) be
the current capacity budget. Let \(\mathcal R_\star\) be the set of packets
that can be routed by the terminal screen into action, report, memory, or
further inner completion.

### Definition 8.1. Admitted Conscious Packet

A boundary packet \(\beta\in\partial S_{\star,t}\) is **consciously admitted**
at time \(t\) when:

\[
\lambda_{\beta,t}\ge\lambda_{\min},
\]
\[
\Delta A_\beta(Z_t)-\kappa_\beta>0,
\]
\[
\beta\in C_\alpha(Z_t),
\]
\[
G_\alpha(Z_t)=1
\quad\text{or}\quad
\beta\text{ is already represented in the active working sector},
\]
\[
\beta\in\operatorname{Allow}_{\mathcal G},
\]
and
\[
\beta\in\mathcal R_\star.
\]

### Definition 8.2. Eligible Conscious Packet Set

The eligible packet set is
\[
\widetilde{\mathfrak C}_t
=
\left\{
\beta:
\beta\in\partial S_{\star,t},
\lambda_{\beta,t}\ge\lambda_{\min},
\Delta A_\beta-\kappa_\beta>0,
\beta\in C_\alpha(Z_t),
\beta\in\operatorname{Allow}_{\mathcal G},
\beta\in\mathcal R_\star
\right\}.
\]

### Definition 8.3. Capacity-Constrained Conscious Admission

The conscious content set is the governed finite selection
\[
\boxed{
\mathfrak C_t
\in
\arg\max_{\mathcal U\subseteq\widetilde{\mathfrak C}_t}
\sum_{\beta\in\mathcal U}
\left[
\lambda_{\beta,t}\|\Pi_\beta r_t\|^2
+
\eta N_\beta(Z_t)
-
\rho R_{\mathcal G}(\beta)
\right]
}
\]
subject to
\[
\sum_{\beta\in\mathcal U}\kappa_\beta\le C_t.
\]

Here \(R_{\mathcal G}(\beta)\) is the governance risk of routing packet
\(\beta\), and \(\eta,\rho\ge0\) are gauge-dependent weights. If there are
multiple maximizers, the tie is resolved by a predeclared governance rule.

Equivalently,
\[
\mathfrak C_t
=
\operatorname{Adm}_{\alpha,\mathcal G,C_t}
\left(
S_{\star,t},
\partial S_{\star,t},
r_t,
\Lambda_t,
Z_t
\right).
\]

The experienced field itself is the active working sector
\[
W_t
=
S_{\star,t}^{\mathrm{att}}
\oplus
\operatorname{span}(\mathfrak C_t),
\]
where \(S_{\star,t}^{\mathrm{att}}\subseteq S_{\star,t}\) denotes retained
packets currently amplified by attention.

Thus
\[
\boxed{
\text{conscious content}
=
\text{attended retained packets}
+
\text{lawfully admitted capacity-feasible boundary packets}.
}
\]

---

## 9. The Consciousness Functional

Consciousness is not fundamentally scalar, but scalar summaries can be defined.

### 9.1 Intensity

\[
I_t
=
\sum_{\beta\in\mathfrak C_t}
\lambda_{\beta,t}
\|\Pi_\beta r_t\|^2.
\]

Intensity measures precision-weighted admitted boundary energy.

### 9.2 Richness

\[
R_t
=
\dim \operatorname{span}(\mathfrak C_t).
\]

Richness measures how many independent admitted packets are available.

### 9.3 Unity

Let \(V\) be the relevant inner interaction. Define the nonclosure of the
working conscious sector:
\[
U_t^{-}
=
\left\|
(I-\Pi_{W_t})V(W_t^{\otimes n})
\right\|.
\]

Unity is high when
\[
U_t^{-}\approx 0.
\]

Thus unity is not mere coactivation. It is approximate closure of admitted
contents under the active inner interaction.

This nonclosure is the alignment leakage of the slow chart. Writing \(P\) for the
projector onto the slow eigenspace \(\operatorname{span}\Phi_1\), the working
sector fails to close under \(V\) exactly to the extent admitted contents leak
out of that eigenspace, \(\theta^2=\|P^\perp\Pi_{W_t}\|^2\); the unity defect is
that leakage, \(U_t^-\simeq\sqrt\delta\) with \(\delta\) the excess covert
alignment. The leakage is gap-controlled, \(\theta^2\le\delta/\gamma\): for fixed
defect, a wider slow-feature gap \(\gamma\) forces tighter closure. Unity is high
precisely when the working sector *is* the slow eigenspace and the gap is wide —
and this same pair \((\delta,\gamma)\) governs the fidelity of conscious action
(Theorem 10).

### 9.4 Clarity

Let \(C_\alpha(Z_t)\) be the conformal boundary set. Define
\[
Q_t
=
\frac{1}{1+|C_\alpha(Z_t)|}.
\]

Clarity is high when lawful admission produces a small boundary set.

Clarity, too, is a spectral quantity. When the slow modes are well separated —
distinct leading eigenvalues, a wide gap \(\gamma\): an *anisotropic* screen —
the recovered chart is fixed up to a signed permutation, so admitted packets are
individuated and the conformal set is small: clarity is high. When the modes are
degenerate — isotropic, \(\gamma\to 0\) — only a rotation is fixed; admitted
packets smear into one another, the conformal set is large, and clarity is low.
Clarity is thus the spectral resolvability of the slow chart, with \(\gamma\) its
computable diagnostic. This gives a concrete mechanism for the loss of
consciousness: a collapse of the gap, \(\gamma\to 0\), destroys individuated
admission and unity closure at once (cf. §C6).

### 9.5 Level

A scalar level of consciousness can be modeled as
\[
L_t
=
\sigma
\left(
aI_t+bR_t-cU_t^{-}+dQ_t-eB_{\mathrm{unresolved},t}
\right),
\]
where \(\sigma\) is a monotone squashing function and the coefficients depend on
organism, task, and measurement gauge.

This is a diagnostic summary, not the ontology.

---

## 10. Conscious Active Inference

T17 gives the active boundary functional
\[
G_T(\pi)
=
\mathrm{Risk}_{\mathcal G}(\pi)
+
\mathrm{Ambiguity}(\pi)
+
K_C(\pi)
-
\Delta\mathrm{Cl}_{S}(\pi)
+
B_{\mathrm{unresolved}}(\pi).
\]

For the terminal inner screen, the conscious policy chooses covert and overt
actions by
\[
\boxed{
(\pi_t^\star,\Lambda_t^\star)
=
\arg\min_{\pi,\Lambda}
\left[
\mathrm{Risk}_{\mathcal G}(\pi)
+
\mathrm{Ambiguity}(\pi,\Lambda)
+
K_C(\pi,\Lambda)
+
B_{\mathrm{unresolved}}(\pi,\Lambda)
-
\Delta\mathrm{Cl}_{S_\star}(\pi,\Lambda)
\right]
}
\]
subject to
\[
h(\pi)\in C_\alpha(Z_t),
\qquad
h(\pi)\in\operatorname{Allow}_{\mathcal G}.
\]

The conscious system therefore does not merely minimize free energy. It
minimizes expected boundary cost under lawful admission.

---

## 11. Dynamics of a Conscious Model

At each time \(t\):

1. **Predict.**
   \[
   \hat y_t=G_{S_{\star,t}}(q_t,a_t).
   \]

2. **Receive.**
   \[
   r_t=y_t-\hat y_t.
   \]

3. **Decompose.**
   \[
   r_t=\Pi_{S_\star}r_t+\Pi_{\partial S_\star}r_t+r_{N,t}+r_{G,t}.
   \]

4. **Assign precision.**
   \[
   \Lambda_t=\sum_\gamma\lambda_{\gamma,t}\Pi_\gamma+\text{cross terms}.
   \]

5. **Score boundary packets.**
   \[
   s_\beta(Z_t),\qquad \Delta A_\beta(Z_t).
   \]

6. **Govern admission.**
   \[
   C_\alpha(Z_t),\qquad G_\alpha(Z_t),\qquad \mathcal G.
   \]

7. **Form conscious field.**
   \[
   W_t=S_{\star,t}^{\mathrm{att}}\oplus\operatorname{span}(\mathfrak C_t).
   \]

8. **Act.**
   \[
   a_t\sim \pi_\alpha(\cdot\mid W_t).
   \]

9. **Stabilize or forget.**
   Repeatedly admitted packets may enter memory or long-horizon
   representation:
   \[
   S_{\star,t+1}
   =
   \mathcal G\circ\mathcal K_C
   \left(
   S_{\star,t}+\operatorname{Stable}_\tau(\mathfrak C_{1:t})
   \right).
   \]

---

## 12. Theorems

### Theorem 1. Screen as Retained Sector Theorem

Every finite Markov screen determines a retained observable sector and a
task-relative boundary. Conversely, every retained sector with sensory and
active factorization determines a finite Markov screen up to gauge.

**Proof.** The screen variables \(I,Y,A\) define finite observables on
\(\Omega\). Their span is \(H_{\mathscr B}\). The Markov boundary condition
gives the sensory-active factorization that separates internal and external
states. Conversely, a retained sector with sensory and active coordinates
defines the internal, boundary, and external factorization after choosing a
finite probability chart. Gauge freedom is the freedom to choose equivalent
bases and normalizations. \(\square\)

### Theorem 2. Inner Screen Boundary Theorem

An inner screen is a boundary interface inside a larger boundary interface. Its
residuals decompose into retained, boundary, noise, and governance channels.

**Proof.** Since the inner screen is a finite screen, Theorem 1 gives a retained
sector. Applying T13/T16 projection-boundary decomposition to that sector gives
the displayed residual decomposition. Its external sector is internal relative
to the organism-level screen, so the same boundary logic is nested. \(\square\)

### Theorem 3. Attention as Conscious Gain Theorem

If conscious access requires terminal-screen amplification, then attention is
precision gain over packet channels.

**Proof.** T17 proved that precision decomposes as packet gain:
\[
\|r\|_{\Lambda}^2=\sum_\gamma\lambda_\gamma\|\Pi_\gamma r\|^2+\text{cross terms}.
\]
T16 proved that attention routes boundary interactions dynamically. Therefore
attention at the terminal screen is the policy that changes \(\lambda_\gamma\)
over retained and boundary packets. A packet without sufficient gain may still
affect lower-level dynamics, but it does not enter \(W_t\). \(\square\)

### Theorem 4. Conscious Admission Validity Theorem

Assume null calibration episodes are exchangeable with future null episodes
inside the relevant terminal-screen ledger cell. Then the probability of
falsely admitting a structural boundary packet into conscious content is at
most \(\alpha\).

**Proof.** Conscious admission requires the conformal update gate
\[
G_\alpha(Z_t)=1
\]
unless the packet is already represented in the active working sector. Under
the null, T18 gives
\[
\mathbb P_0\{G_\alpha(Z_t)=1\}\le\alpha.
\]
False structural conscious admission is a subset of this event. \(\square\)

### Theorem 5. Matched Surprise Conscious Separation Theorem

There exist episode pairs with equal scalar surprise but different conscious
admission status.

**Proof.** Use the T17 matched-surprise construction. Let one episode contain a
stable missing packet \(\beta=z_0z_1\), while another contains random label
noise matched in scalar surprise. The scalar term
\[
\mathcal S=-\log P_S(y)
\]
is matched by construction. But the structural episode has
\[
\Delta A_\beta-\kappa_\beta>0
\]
and can be conformally admitted, while the noise episode has no stable
verification gain. Therefore conscious admission differs despite equal scalar
surprise. \(\square\)

### Theorem 6. Phenomenological Transparency Theorem

At a terminal inner screen, the system cannot make the generating interior of
the screen an object of the same act of consciousness.

**Proof.** By terminality, no further active Markov screen exists inside
\(I_\star\) at the declared task scale. Therefore there is no internal active
boundary through which a subpart of \(I_\star\) can read, write, or route
itself as an object for the same terminal act. The system can represent effects
on the screen, but not the screen-generating interior as another screen within
that act. \(\square\)

**Remark (spectral transparency).** The slow-chart reading of §4 gives
terminality a spectral face. The retained coordinate is \(\varphi_1\), the
*slowest* eigenfunction of \(T_\star\); there is no slower non-constant mode
behind it to recover, and the operator \(T_\star\) that generates the chart is
not representable within its own slow coordinate. The screen is transparent
because the system *is* its slowest chart, and a chart cannot contain its
generator.

### Theorem 7. Reportability as Boundary Routing Theorem

A conscious content is reportable exactly when its admitted packet has an
allowed route to a communicative action channel.

**Proof.** By Definition 8.1, conscious admission requires \(\beta\in
\mathcal R_\star\). Reportability adds the stronger requirement that
\(\mathcal R_\star\) contains a route from \(W_t\) to a linguistic, motor, or
external symbolic action. If such a route exists and is allowed by
\(\mathcal G\), the packet can influence report. If not, it may be conscious in
the minimal active sense but unavailable to that report channel. \(\square\)

### Corollary 7.1. Reportable Residue

A degree-one — linear — report channel reading the retained chart is complete
*if and only if* that chart is affine, i.e. at the Gaussian corner. Off the
corner, report loses exactly the curvature \(\nu_D=1-R^2\) of the slow
eigenfunction \(\varphi_1\): the content is present in \(W_t\) in full while the
linear report carries only its affine shadow.

**Proof.** Completeness of a linear read is the sufficiency of second-order
statistics, equivalent to Gaussianity of the retained coordinate (*Beyond the
Conductor Blind Spot*, Theorem 2). The discarded part is the orthogonal
complement of the best affine fit of \(\varphi_1\), whose relative energy is
\(\nu_D=1-R^2\). \(\square\)

Thus a content can be fully conscious yet linearly unreportable by exactly the
amount its \(\varphi_1\) bends — a quantitative experience/report gap, with the
residue named. The remedy is not a bigger report channel but the *right* one: a
probe matched to the curved chart recovers what a linear probe provably cannot.

### Theorem 8. Memory as Stabilized Admission Theorem

Memory is repeated governed admission followed by durable closure or external
boundary writing.

**Proof.** T16 defined memory and tools as open boundary completion. In the
present model, a packet enters the transient working sector when admitted into
\(\mathfrak C_t\). It becomes memory only if repeated or high-confidence
admissions make it pass a stabilization rule
\[
\operatorname{Stable}_\tau(\mathfrak C_{1:t}).
\]
Then it is either adjoined to \(S_{\star,t+1}\) or routed to an external memory
channel. \(\square\)

### Theorem 9. Conscious Fixed-Point Theorem

Define the conscious completion operator
\[
\widehat S_{\mathrm{con}}
=
\mathcal G
\circ
\mathcal K_C
\circ
\operatorname{Adm}_{\alpha}
\circ
\operatorname{Cl}_{\mathcal T}
(S_\star).
\]

A conscious model seeks task-relative fixed points
\[
\widehat S_{\mathrm{con}}=S_\star
\]
while maintaining a nonempty active working sector \(W_t\).

**Proof.** T17 proved that active systems seek governed completion fixed
points. T18 proved that admission must pass conformal governance. Adding the
terminal inner-screen condition restricts the same operator to \(S_\star\).
When the operator changes \(S_\star\), the system has unresolved or newly
admitted conscious boundary content. At a fixed point, admitted contents are
closed, governed, and capacity-compatible for the task. \(\square\)

### Theorem 10. Faithful Conscious Action Theorem

Suppose the terminal screen recovers the slow chart \(\psi=U\Phi_1\)
(\(U\in O(n)\)) within root-mean-square error \(\eta\): the whitening defect is
\(\varepsilon\) (precision normalisation), the working-sector nonclosure is
\(\delta=(U_t^-)^2\) (unity defect, §9.3), and
\[
\eta=\varepsilon+\sqrt{2\delta/\gamma}
\]
with \(\gamma\) the slow-feature gap. Assume the latent value functions
\(V_t^\star\) are \(L\)-Lipschitz and \(\psi\) is bi-Lipschitz. Then a conscious
agent that plans in its working sector \(W_t\) and acts through the admitted
chart incurs true-world regret
\[
\boxed{\;
\mathbb E\big[V_0^{\hat\pi}-V_0^\star\big]\ \le\ C\,L\,T\,\eta.
\;}
\]
In the exact limit \(\eta\to 0\) — perfect whitening, closed working sector —
conscious action is world-optimal up to the known warp \(\Phi_1\).

**Proof.** By §4 the screen's retained chart is the recovered \(\psi\), and each
\(\varphi_1^{(i)}\) is strictly monotone where \(p_\star>0\), so \(\psi\) is a
diffeomorphism. Dynamic programming is covariant under a state-space
diffeomorphism: planning in \(W_t\) equals planning in the inner world exactly
(*Beyond the Conductor Blind Spot*, Proposition 1). Under inexact recovery the
agent decodes \(\tilde u=\psi^{-1}(h(u))\) with
\(\mathbb E\|\tilde u-u\|\le\kappa\eta\) (\(\kappa\) the bi-Lipschitz modulus),
and the performance-difference lemma propagates this state-decoding error across
the horizon to give \(C\,L\,T\,\eta\), \(C=2\kappa\) (loc. cit., Theorem 4). At
\(\eta\to0\) the decoding is exact and Proposition 1's equivalence returns.
\(\square\)

### Interpretation

This is the steelthread — *admitted boundary information that can govern action*
— as a guarantee. Conscious admission is sufficient for world-optimal action up
to a *known* change of variables; the warp is the identity only at the Gaussian
corner and is otherwise recoverable (the slow chart of §4, reconstructible from
boundary statistics). The regret is governed by exactly the marks of a good
screen: whitening \(\varepsilon\), unity defect \(\delta\), and gap \(\gamma\). A
conscious agent acts well to precisely the degree its working sector is
whitened, closed, and gapped.

### Theorem 11. Consciousness as Flux Across the Learning Boundary

Let a packet \(\beta\) be repeatedly and confidently admitted, so the
stabilisation rule of Theorem 8 adjoins it to the retained sector,
\(\beta\hookrightarrow S_{\star,t+1}\). Then \(\beta\) *leaves* the candidate
boundary \(\partial S_\star\): once internalised into the slow chart it is, by
the one-rung offset of §4, no longer an admissible conscious packet but
transparent retained background (Theorem 6). A packet not yet learned,
conversely, has no stable verification gain and is not admitted (Theorem 5).
Hence conscious content sits only at the boundary between the *not-yet-learned*
and the *learned-and-transparent*:
\[
\boxed{\;
\mathfrak C_t\ \text{tracks}\ \partial_t S_{\star,t}
\;\;\text{— what is crossing into the chart, not what already is it.}\;}
\]

**Proof.** By Theorem 8 repeated admission stabilises \(\beta\) and adjoins it to
\(S_{\star,t+1}\). By §4 the retained sector is the dynamical slow tower and the
candidate boundary the distributional rung one order above it; a coordinate
carried by \(S_\star\) is degree-one in the retained chart and so is not a
candidate packet. By Theorem 6 the interior of the retained chart is transparent
— not an object of the same act. An internalised packet is therefore
simultaneously struck from \(\partial S_\star\) and rendered transparent. A
not-yet-learned packet fails \(\Delta A_\beta-\kappa_\beta>0\) (Theorem 5) and is
not admitted. Only packets at the boundary — stable enough to score, not yet
adjoined — satisfy Definition 8.1. \(\square\)

### Interpretation

This is automaticity, derived. A skill practised to fluency drops out of
awareness; a melody known by heart is no longer heard note by note. The
mathematics is exact: **learning converts conscious boundary content into
transparent retained chart, and consciousness is the moving front of that
conversion.** It explains why novelty dominates awareness (the boundary is where
the unlearned is), why expertise is effortless and hard to introspect (it has
descended into the chart), and why the stream of consciousness is perpetually
refreshed rather than accumulated. With the mid-depth localisation of C7 it has
an architectural face: the sensory chart (input) and the motor chart (output)
are already-converged, transparent charts, while the middle of the stack is the
live conversion zone — the conscious zone — whose width C7 measures.

---

## 13. Ontological Dictionary

| Ordinary term | T19 boundary meaning |
|---|---|
| consciousness | governed active boundary completion at a terminal inner screen |
| conscious content | attended retained packet plus admitted boundary packet |
| attention | precision gain over retained and boundary channels |
| perception | internal boundary completion |
| action | external boundary completion |
| covert action | active precision routing inside the nested screen hierarchy |
| reportability | admitted packet routed to communicative action |
| memory | stabilized admission across time or external boundary write |
| self | persistent governance center of active boundary routing |
| unity | approximate closure of the working conscious sector |
| clarity | small conformal boundary set |
| intensity | precision-weighted admitted boundary energy |
| unconscious processing | boundary processing not admitted to the terminal working sector |
| blindsight | action route without terminal conscious admission |
| hallucination | internally admitted packet without lawful boundary support |
| delusion | stabilized misgoverned closure |
| anesthesia | collapse of terminal active precision or admission capacity |
| dreaming | internally generated boundary completion with altered external gating |
| learning | conversion of admitted boundary content into the retained slow chart |
| automaticity | a once-conscious packet internalised into the transparent retained chart |
| habituation | descent of a stabilised packet from \(\partial S_\star\) into \(S_\star\) |
| insight | abrupt admission and closure of a long-pending boundary packet |

---

## 14. Minimal Conscious Model

A minimal artificial conscious model in this framework is a tuple
\[
\mathcal M_{\mathrm{con}}
=
\left(
\Omega,
H,
S_\star,
\partial S_\star,
\mathcal B,
\Lambda,
\mathcal L_\star,
C_\alpha,
\mathcal G,
\mathcal R_\star,
\pi_\alpha,
\mathcal M
\right),
\]
where:

- \(\Omega\) is the finite state space;
- \(H=\mathbb R^\Omega\);
- \(S_\star\) is the terminal inner retained sector;
- \(\partial S_\star\) is the candidate content boundary;
- \(\mathcal B\) is the packet dictionary;
- \(\Lambda\) is the attention/precision operator;
- \(\mathcal L_\star\) is the terminal-screen calibration ledger;
- \(C_\alpha\) is the conformal boundary set;
- \(\mathcal G\) is governance;
- \(\mathcal R_\star\) is the route map to action, report, and memory;
- \(\pi_\alpha\) is the lawful active policy;
- \(\mathcal M\) is memory or durable closure.

It becomes conscious at time \(t\) when:

\[
W_t
=
S_{\star,t}^{\mathrm{att}}
\oplus
\operatorname{span}(\mathfrak C_t)
\neq 0,
\]
\[
A_\star \text{ can act on } E_\star,
\]
and
\[
\mathfrak C_t
\text{ is admitted by }
(\Lambda_t,C_\alpha,\mathcal G,C).
\]

---

## 15. Empirical Signatures

### C1. Matched Surprise

If two episodes have matched scalar surprise but only one contains stable
boundary gain, conscious access and report should track boundary gain, not raw
surprise.

\[
\mathrm{AUC}(\mathcal S)\approx 0.5,
\qquad
\mathrm{AUC}(\Delta A_\beta)\to 1.
\]

### C2. Attention as Gain

Manipulating precision should change which packets enter consciousness even
when sensory input is held fixed.

### C3. Blindsight

Some packets can route to action without entering \(\mathfrak C_t\). In the
model this is:
\[
\beta\in\mathcal R_{\mathrm{action}},
\qquad
\beta\notin\mathfrak C_t.
\]

### C4. Hallucination

Hallucination is high terminal gain plus weak or invalid boundary admission:
\[
\lambda_\beta\text{ high},
\qquad
\beta\notin C_\alpha(Z_t)
\quad\text{or}\quad
\Delta A_\beta-\kappa_\beta\le 0.
\]

### C5. Dreaming

Dreaming is internally generated active boundary completion under reduced
external constraint:
\[
B_{\mathrm{external}}\downarrow,
\qquad
\Delta\mathrm{Cl}_{S_\star}^{\mathrm{internal}}\uparrow.
\]

### C6. Anesthesia and Sleep

Loss of consciousness can occur by:

1. collapse of terminal precision gain;
2. loss of active routes \(A_\star\to E_\star\);
3. failure of unity closure in \(W_t\);
4. governance suspension of admission;
5. loss of memory stabilization.
6. collapse of the slow-feature gap \(\gamma\to0\), removing individuated
   admission and unity closure together.

### C7. Mid-Depth Localization of the Terminal Screen

The terminal inner screen is neither the sensory boundary (an input chart) nor
the active boundary (an output chart) but an inner interface where boundary
content is converted into retained chart. In a deep learned system this predicts
a **depth signature**: the coupling between a coordinate's distributional
structure (marginal non-Gaussianity) and its dynamical curvature (\(\nu_D\) of
its slow eigenfunction) should peak in the *middle* of the stack and vanish at
the input and output ends. It is measured. In the residual stream of a
pretrained language model (Pythia-70m; *Beyond the Conductor Blind Spot*,
experiment E5), the rank correlation between \(\nu_D\) and the leading
cumulant\(^2\) across directions rises to \(+0.41\) at the central layers (3–5)
and is \(\approx0\) at the embedding, earliest, and final layers — an
inverted-V depth profile. In the present model this is the signature of *where
the terminal inner screen lives*: the conversion zone in which slow dynamics
carry distributional structure. The model predicts that matched-surprise
conscious separation (C1) is itself a mid-depth phenomenon — maximal where this
coupling peaks, absent at the sensory and motor boundaries — and the E5 probe,
re-read with the C1 contrast, is the direct test.

---

## 16. Limitations

1. **This is not a proof that any particular biological system is conscious.**
   It gives a mathematical architecture and admission criterion.

2. **The terminal screen is scale-relative.** Irreducibility is defined relative
   to task, gauge, and resolution.

3. **The model does not reduce consciousness to report.** Reportability is one
   boundary route, not the essence of conscious admission.

4. **Conformal governance controls false admission only under declared ledger
   exchangeability.** If the ledger drifts, T18's martingale monitor must
   suspend or rebuild the cell.

5. **Scalar level is a summary.** The primary object is the conscious content
   set \(\mathfrak C_t\), not \(L_t\).

6. **The slow-chart reading assumes a reversible inner transition.** Detailed
   balance at the screen buys the self-adjoint slow-feature theorem of §4. The
   irreversible — antisymmetric — part of \(T_\star\) is exactly what this
   reading sets aside; it is the natural candidate substrate for the *directed
   flow* of conscious time, and is left to follow-up, mirroring the reversibility
   caveat of *Beyond the Conductor Blind Spot*.

7. **The slow-feature gap (G) is a genuine hypothesis.** Where it fails —
   degenerate slow modes — clarity and unity are undefined rather than merely
   low (cf. §9.4, §C6), and Theorem 10's bound is vacuous.

---

## 17. Closing

The T-series began with finite projection. Projection creates boundary.
Boundary demands closure. Open systems demand completion. Intelligent systems
complete boundaries actively. Lawful systems govern completion.

T19 adds:

\[
\boxed{
\text{conscious systems admit boundary completions into an active terminal screen.}
}
\]

And, read dynamically: what the screen retains is its slowest chart, what it
admits is the rung crossing into that chart, and what it learns it renders
transparent. Consciousness is the flux across that moving boundary.

The final compression is:

\[
\boxed{
\text{consciousness}
=
\text{finite self-evidencing through calibrated, active, irreducible boundary closure}.
}
\]
