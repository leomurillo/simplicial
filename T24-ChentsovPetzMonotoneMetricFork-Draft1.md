# T24 — The Monotone-Metric Apex: The Petz Fork and the Kubo–Mori Selection

**Leonardo Murillo Montero**

*First draft — May 28, 2026 — scoping paper for the quantum-sector metric selection*

<!--
PLANTATION — file-level notes.

This is T24: a scoping paper that names a fork the programme has so far
crossed without remark. T7 §4.5 / §7.2 / §7.3 open a "mixed-state /
density-matrix apex" forward door and label the next paper "The Bures
Apex." The word "Bures" is a *choice*, and this paper is about the choice.

The one structural fact:

  Classically there is ONE monotone metric (Chentsov: Fisher–Rao, unique up
  to scale). The whole "what is additive?" thesis of T0 leans on that
  uniqueness — a unique cumulant structure, a unique second-order form.

  Quantumly the uniqueness FAILS. Morozova–Chentsov–Petz: a whole family of
  monotone metrics, one per operator-monotone function f with f(1)=1 and
  f(t)=t f(1/t). Bures/SLD is the minimal member, RLD the maximal, Kubo–Mori
  (BKM) the one tied to log ρ and relative entropy.

  In M_ρ(β,c) = (1/N) tr(e^{βL_ρ} C_c*), L_ρ = log ρ − (1/N)tr(log ρ)I, the
  operators L_ρ and C_c do NOT commute when ρ is off-diagonal. The one-
  observable scalar is unambiguous (it is the BKM power tilt ρ^β). The
  AMBIGUITY is in the second-order / covariance structure — the would-be
  quantum metric — where you must choose how to interleave powers of ρ
  between two character observables. That interleaving choice IS the
  operator-monotone f. Chentsov-vs-Petz is the precise name of the fork.

  Kubo–Mori is flagged as the natural apex member: it is the one that keeps
  the log ρ cumulant structure intact, and (Grasselli–Streater) the UNIQUE
  monotone metric admitting a dually-flat (e/m) structure — i.e. the unique
  one for which "additive" survives. Any "Bures apex" privileges SLD silently.

This paper does not settle which member the programme should adopt; it states
the fork precisely, identifies it inside M_ρ, and argues the natural answer.
It is the quantum continuation of T0's founding question.

Cross-references to T-series are local-file links; the load-bearing external
citations are Chentsov, Morozova–Chentsov, Petz (already in T7's bibliography),
plus Petz 1996 (the classification), Petz–Sudár 1996 (the members), and
Grasselli–Streater 2001 (the BKM uniqueness).
-->

---

> *Chentsov gives one metric; Petz gives a corridor. The corridor is exactly the non-commutativity — and choosing a point in it is choosing what "additive" means.*

---

## Abstract

**Situation.** [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) opens with *what is additive?* and answers it on positive ledgers: a gauge $\beta$ selects a section of the projective cone, and the resulting cumulant tower is organized by a single canonical second-order form, the Fisher–Rao metric. That the answer is *single* is not an accident of the construction — it is **Chentsov's theorem**: on the classical simplex the Fisher–Rao metric is the *unique* (up to scale) Riemannian metric monotone under stochastic maps (Chentsov 1982). Every "the additive structure," "the cumulant," "the information metric" in [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)–[T6](T6-RMSSimplicialQuadraticGauge-Draft1.md) is licensed by that uniqueness.

**Gap.** [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §4.5 and §7.2–§7.3 push the apex into the quantum sector with a *density-matrix apex generator*
$$\mathcal M_\rho(\beta,c)=\tfrac1N\operatorname{tr}\!\big(e^{\beta L_\rho}C_c^{\ast}\big),\qquad L_\rho=\log\rho-\tfrac1N\operatorname{tr}(\log\rho)\,I,\qquad C_c=\sum_s\chi_c(s)\,|s\rangle\langle s|,$$
and names the planned forward paper *The Bures Apex*. The word **Bures** is a silent commitment. Quantumly, Chentsov's uniqueness **fails**: the **Morozova–Chentsov–Petz theorem** classifies the monotone metrics on density matrices as a *family*, one member per operator-monotone function $f:(0,\infty)\to(0,\infty)$ with $f(1)=1$ and $f(t)=tf(1/t)$ (Morozova–Chentsov 1989; Petz 1996). Bures/SLD is one member (the minimal one); Kubo–Mori and RLD are others. The classical "the metric" becomes a corridor, and the apex programme has been walking down it without choosing a side.

**Action.** We state the Chentsov (classical, unique) vs Morozova–Chentsov–Petz (quantum, family) dichotomy precisely, with the operator-monotone parameterization and the eigenbasis form of the metric. We then locate the choice *inside* $\mathcal M_\rho$: for off-diagonal $\rho$, $L_\rho=\log\rho-\text{const}$ and $C_c$ **do not commute** ($[\log\rho,C_c]\neq0$), so the second-order content of $\mathcal M_\rho$ — the covariance of character observables that would be the quantum Amari–Chentsov tensor / quantum Fisher metric — requires a choice of operator ordering, and the admissible orderings are *exactly* the operator-monotone functions $f$. The fork is not an artifact; it is the non-commutativity itself.

**Result.** Five claims of T24:

1. **The dichotomy (Theorem 1.2 / Theorem 2.1).** Classical: one monotone metric (Fisher–Rao, Chentsov). Quantum: the affine-rigid family $\{g^f\}_f$ over operator-monotone $f$ with $f(1)=1$, $f(t)=tf(1/t)$, with eigenbasis form $g^f_\rho(A,A)=\sum_{i,j}|A_{ij}|^2/\big(\lambda_j f(\lambda_i/\lambda_j)\big)$.

2. **The fork has zero width on the decoherent face (Proposition 3.1).** On diagonal $\rho$ every member restricts to the *same* classical Fisher–Rao metric, because $c^f(\lambda,\lambda)=1/\lambda$ for all $f$. The family separates *only* in off-diagonal directions — exactly the directions $[\log\rho,C_c]\neq0$ that $\mathcal M_\rho$ reaches and the classical $\mathcal M_x$ of [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) cannot. The quantum apex is the *width of the fork*.

3. **The one-observable generator is unambiguous and is the Kubo–Mori power tilt (Proposition 4.1).** $\mathcal M_\rho(\beta,c)=(\det\rho)^{-\beta/N}\cdot\tfrac1N\operatorname{tr}(\rho^{\beta}C_c^{\ast})$ — the geometric-mean–normalized escort family $\rho\mapsto\rho^{\beta}$, the quantum analog of [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §5's $G(z)^{-m}\widehat{z^m}_c$. The tilt *inside the log* is the Bogoliubov–Kubo–Mori (BKM) exponential family. The ambiguity is not here; it is in the **two**-observable covariance (Theorem 4.3), where it is $f$.

4. **The members, named (Theorem 3.2).** $f_{\mathrm{SLD}}(t)=\frac{1+t}2$ (arithmetic mean) $\to$ **Bures/SLD, the minimal monotone metric**, $4\times$ Bures $=$ QFI; $f_{\mathrm{KM}}(t)=\frac{t-1}{\log t}$ (logarithmic mean) $\to$ **Kubo–Mori**, the member that keeps [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s $\log\rho$ cumulant structure intact; $f_{\mathrm{RLD}}(t)=\frac{2t}{1+t}$ (harmonic mean) $\to$ **RLD, the maximal monotone metric**. The chain $f_{\mathrm{harm}}\le f_{\mathrm{KM}}\le f_{\mathrm{arith}}$ (HM $\le$ LM $\le$ AM) reverses to $g^{\mathrm{SLD}}\le g^{\mathrm{KM}}\le g^{\mathrm{RLD}}$.

5. **Kubo–Mori is the additive member (Theorem 5.1, citing Grasselli–Streater 2001).** It is the *unique* monotone metric admitting a dually-flat pair of $\pm1$-connections — the quantum exponential/mixture duality, additive (Pythagorean) relative entropy. It is therefore the precise quantum continuation of "what is additive?": the classical question had one answer because all roads agreed; the quantum question forks, and the road that keeps *additivity* is Kubo–Mori, **not** Bures.

**Harvest.** "What is additive?" ([T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)) has a unique classical answer because Chentsov makes the monotone metric unique. Its honest quantum continuation is **"which operator ordering — which monotone metric?"**, and Chentsov-vs-Petz is the exact name of that fork. A *Bures apex* answers "SLD" (estimation-optimal, minimal); a *Kubo–Mori apex* answers "BKM" (additive, dually flat, the one the $\log\rho$ generator already chose at first order). This paper does not legislate the choice; it makes the choice visible and argues that the apex programme's own commitments point at Kubo–Mori.

**Keywords:** monotone metric, Chentsov theorem, Morozova–Chentsov–Petz classification, operator-monotone function, Bures metric, symmetric logarithmic derivative, Kubo–Mori / Bogoliubov metric, right logarithmic derivative, quantum Fisher information, operator ordering, dually flat connection, density-matrix apex, what is additive.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) §1 (the thesis *what is additive?*; Gauge Selection Principle) | The classical pillar §1; the continuation question §6 |
| [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) §3 (additive apex generator $\mathcal M_x$; Amari–Chentsov tensor as the $n=3,c=0$ cumulant slice) | Classical second/third-order form forked in §4 |
| [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §4.5 (density-matrix apex generator $\mathcal M_\rho$, forward door) | The object whose ordering is the fork (§4) |
| [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §5 (closure diagonal $\mathcal M_z(m,c)=G(z)^{-m}\widehat{z^m}_c$) | Quantum analog $\mathcal M_\rho(\beta,c)=(\det\rho)^{-\beta/N}\operatorname{tr}(\rho^\beta C_c^\ast)/N$ (§4) |
| [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §7.2 (Bures metric; QFI $=4g_{\mathrm{Bures}}$) | The silent SLD commitment audited in §6 |
| [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §7.3 (Bures replicator; escort $\rho_\beta=e^{\beta L_\rho}/\operatorname{tr}(\cdot)$) | Re-read as BKM e-geodesic in §5 |
| [T2](T2-CumulantTowerEffectiveAction.md)/[T3](T3-CharacterOrthogonalityConductorLattice.md) (cumulant tower; character orthogonality) | Classical structure whose quantum lift forks (§4–§5) |

This paper introduces **no new apex object**. It scopes the *selection* problem for the object [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) already wrote, and is a prerequisite for any paper that writes "the" quantum apex metric.

---

## Notation

We carry the notation of [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) and add the metric-selection layer.

| Symbol | Meaning |
|---|---|
| $N$ | Dimension of the categorical Hilbert space $\mathbb C^N$, integer $\ge 2$. |
| $\mathcal D_N$ | Faithful (full-rank) density matrices on $\mathbb C^N$: $\rho=\rho^\ast>0$, $\operatorname{tr}\rho=1$. |
| $\mathcal D_N^{\mathrm{diag}}$ | Diagonal (in the character/computational basis) states $\cong\mathring\Delta^{N-1}$. |
| $T_\rho\mathcal D_N$ | Tangent space at $\rho$: Hermitian traceless matrices $A=A^\ast$, $\operatorname{tr}A=0$. |
| $\lambda_i,\,|i\rangle$ | Eigenvalues / eigenvectors of $\rho$. $A_{ij}=\langle i|A|j\rangle$. |
| $L_\rho,\,R_\rho$ | Left / right multiplication superoperators: $L_\rho(X)=\rho X$, $R_\rho(X)=X\rho$ (commuting, positive). |
| $\mathbf\Delta_\rho$ | Modular / relative-modular operator $L_\rho R_\rho^{-1}$ (so $\mathbf\Delta_\rho|i\rangle\langle j|=(\lambda_i/\lambda_j)|i\rangle\langle j|$). |
| $f$ | Operator-monotone function $(0,\infty)\to(0,\infty)$, normalized $f(1)=1$, symmetric $f(t)=tf(1/t)$. |
| $c^f(x,y)$ | Morozova–Chentsov function $c^f(x,y)=\dfrac1{y\,f(x/y)}$. |
| $g^f_\rho$ | Monotone (quantum Fisher) metric attached to $f$. |
| $\Omega^f_\rho$ | Petz superoperator $\Omega^f_\rho=R_\rho^{1/2}\,f(\mathbf\Delta_\rho)\,R_\rho^{1/2}$; the metric is $g^f_\rho(A,B)=\operatorname{tr}\!\big(A^\ast(\Omega^f_\rho)^{-1}B\big)$. |
| $C_c$ | Character observable $C_c=\sum_{s\in\mathbb Z/N}\chi_c(s)|s\rangle\langle s|$, $\chi_c(s)=e^{2\pi ics/N}$ (diagonal in the computational basis). |
| $L_\rho$ (overloaded) | When written as a single matrix, the **centered modular Hamiltonian** $\log\rho-\frac1N\operatorname{tr}(\log\rho)I$ (as in [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §4.5). The superoperator $L_\rho(\cdot)=\rho\,(\cdot)$ is always written with an argument. |
| $\mathcal M_\rho(\beta,c)$ | Density-matrix apex generator ([T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §4.5). |
| $\Lambda$ | Quantum score / logarithmic-derivative operator (its definition is the fork; §3). |
| SLD, RLD, KM/BKM | Symmetric / right logarithmic derivative; Kubo–Mori (Bogoliubov–Kubo–Mori). |

**Conflict note (two uses of $L_\rho$).** [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) writes $L_\rho$ for the *centered modular Hamiltonian matrix* $\log\rho-\frac1N\operatorname{tr}(\log\rho)I$; the monotone-metric literature writes $L_\rho$ for the *left-multiplication superoperator* $X\mapsto\rho X$. Both are standard and both are needed here. We keep [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s matrix $L_\rho$ (no argument) and write the superoperators with an explicit argument, $L_\rho(X)=\rho X$, $R_\rho(X)=X\rho$. The modular operator is $\mathbf\Delta_\rho=L_\rho R_\rho^{-1}$.

---

## 1. The classical pillar: Chentsov uniqueness {#sec:1}

### 1.1 The thesis and its hidden lemma {#sec:1-1}

[T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) begins: *a statistical theory begins by answering: what is additive?* The Gauge Selection Principle then chooses a section of the positive projective cone (the exponent $\beta$ / power-mean order $r$), and the cumulant tower of [T2](T2-CumulantTowerEffectiveAction.md) is read off the apex generator $\mathcal M_x(\beta,c)=\frac1N\sum_s e^{\beta y_s}\overline{\chi_c(s)}$ as moment/cumulant diagonals. The *second-order* content — the Fisher–Rao metric — and the *third-order* content — the Amari–Chentsov tensor ([T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) §3, the $n=3,c=0$ cumulant slice) — are taken to be **the** information geometry of the simplex.

The word *the* is licensed by a lemma so familiar it is rarely stated:

\hypertarget{stmt:1-1}{}
**Definition 1.1 (Monotone metric, classical).** A Riemannian metric $g$ on the family of (interior) probability vectors $\mathring\Delta^{N-1}$, defined for all $N$ and compatible across them, is **monotone** (Markov-invariant) if for every stochastic map $T:\mathring\Delta^{N-1}\to\mathring\Delta^{M-1}$ (column-stochastic, i.e. a coarse-graining / noisy channel),
$$g_{T p}\big(dT(v),dT(v)\big)\le g_p(v,v)\qquad\text{for all }p,\ v\in T_p\Delta.$$
Information is not created by processing.

\hypertarget{stmt:1-2}{}
**Theorem 1.2 (Chentsov 1982).** Up to a positive constant, the **only** monotone metric on $\mathring\Delta^{N-1}$ is the Fisher–Rao metric
$$g^{\mathrm{FR}}_p(v,v)=\sum_{i=1}^N\frac{v_i^2}{p_i}.$$

This is the pillar. *Because the monotone metric is unique*, the second-order form attached to the apex is canonical: there is nothing to choose. "What is additive?" admits a definite answer — the cumulant/exponential structure with its single attendant metric — and [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)–[T6](T6-RMSSimplicialQuadraticGauge-Draft1.md) inherit that definiteness everywhere they speak of *the* information geometry.

### 1.2 Why the gauge corridor does not threaten uniqueness {#sec:1-2}

[T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)'s $\beta$-corridor and Chentsov's uniqueness are not in tension. The corridor chooses *which additive coordinate* (which section of the cone, which power mean) carries the construction; Chentsov fixes *the metric* on the underlying simplex regardless. The corridor is a choice of chart/affine structure; the metric is chart-independent and unique. We will see that the quantum sector breaks exactly this second, deeper uniqueness — the one the corridor never touched — and that the break is genuinely new modeling content, not a re-labeling.

---

## 2. The quantum plurality: Morozova–Chentsov–Petz {#sec:2}

### 2.1 The classification {#sec:2-1}

Replace $\mathring\Delta^{N-1}$ by the manifold $\mathcal D_N$ of faithful density matrices, and replace stochastic maps by **completely positive trace-preserving (CPTP) maps** (quantum channels) — the quantum coarse-grainings. The monotonicity requirement reads identically: a metric $g$ on $\mathcal D_N$ (for all $N$, compatibly) is **monotone** if $g_{\Phi(\rho)}(d\Phi(A),d\Phi(A))\le g_\rho(A,A)$ for every channel $\Phi$ and every tangent $A$. One now asks Chentsov's question again — and the answer changes.

\hypertarget{stmt:2-1}{}
**Theorem 2.1 (Morozova–Chentsov 1989; Petz 1996).** The monotone metrics on $\mathcal D_N$ are in bijection with the **operator-monotone functions** $f:(0,\infty)\to(0,\infty)$ satisfying the normalization $f(1)=1$ and the symmetry $f(t)=t\,f(1/t)$. The metric attached to $f$ is, in the eigenbasis of $\rho$ ($\rho|i\rangle=\lambda_i|i\rangle$, $A=A^\ast$, $\operatorname{tr}A=0$),
$$\boxed{\;g^f_\rho(A,A)=\sum_{i,j=1}^N c^f(\lambda_i,\lambda_j)\,|A_{ij}|^2,\qquad c^f(x,y)=\frac{1}{y\,f(x/y)}.\;}$$
Equivalently $g^f_\rho(A,B)=\operatorname{tr}\!\big(A^\ast(\Omega^f_\rho)^{-1}B\big)$ with the Petz superoperator $\Omega^f_\rho=R_\rho^{1/2}f(\mathbf\Delta_\rho)R_\rho^{1/2}$, $\mathbf\Delta_\rho=L_\rho R_\rho^{-1}$. The function $c^f$ is the **Morozova–Chentsov function**.

Two structural facts make this a *theorem about non-commutativity*, not a mere relabeling.

- **Operator monotonicity is the content.** That $f$ is operator-monotone (not merely monotone) is exactly the condition equivalent, via Löwner's theorem, to the data-processing inequality holding for *all* channels including the genuinely quantum ones. Restricting to classical (diagonal) channels would impose nothing beyond ordinary monotonicity and would not pin a unique metric down — but it would not need to, because (Proposition 3.1) the diagonal sector is metric-degenerate across the whole family anyway.

- **The symmetry $f(t)=tf(1/t)$** is what makes $g^f$ a symmetric bilinear form ($c^f(x,y)=c^f(y,x)$); it is the self-duality that the SLD/KM/RLD members all satisfy and the reason they can be read as *metrics* rather than merely sesquilinear pairings.

### 2.2 The dichotomy, stated {#sec:2-2}

\hypertarget{stmt:2-2}{}
**Corollary 2.2 (Chentsov vs Morozova–Chentsov–Petz).**

| | classical ($\mathring\Delta^{N-1}$) | quantum ($\mathcal D_N$) |
|---|---|---|
| coarse-grainings | stochastic maps | CPTP channels |
| monotone metrics | **unique** (Fisher–Rao) | **family** $\{g^f\}$, one per op-monotone $f$, $f(1)=1$, $f(t)=tf(1/t)$ |
| selecting one | nothing to select | a genuine modeling choice |
| name | Chentsov 1982 | Morozova–Chentsov 1989, Petz 1996 |

The classical "the metric" is a quantum "a metric." The apex programme inherited the definite article from [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md); §4 shows where, in [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s $\mathcal M_\rho$, the article must become a choice.

---

## 3. The named members and the score-operator fork {#sec:3}

### 3.1 The fork is degenerate on the classical sector {#sec:3-1}

\hypertarget{stmt:3-1}{}
**Proposition 3.1 (Zero fork-width on the decoherent face).** For every operator-monotone $f$ with $f(1)=1$ and for every $\rho\in\mathcal D_N$, the diagonal directions agree:
$$c^f(\lambda,\lambda)=\frac1{\lambda\,f(1)}=\frac1\lambda,$$
so $g^f_\rho$ restricted to tangent vectors $A$ that are **diagonal in the eigenbasis of $\rho$** is $\sum_i |A_{ii}|^2/\lambda_i$ — the classical Fisher–Rao metric of [Theorem 1.2](#stmt:1-2) — independently of $f$. In particular, on $\mathcal D_N^{\mathrm{diag}}\cong\mathring\Delta^{N-1}$ (the **decoherent face**, the locus where $\rho$ and the character observables $C_c$ commute) *all* monotone metrics coincide and equal Fisher–Rao.

**Proof.** $c^f(\lambda,\lambda)=1/(\lambda f(\lambda/\lambda))=1/(\lambda f(1))=1/\lambda$. On $\mathcal D_N^{\mathrm{diag}}$ the eigenbasis is the computational basis, the tangent directions preserving diagonality have $A_{ij}=0$ for $i\ne j$, and only the $i=j$ terms survive. $\square$

This is the precise sense in which the quantum fork is invisible to [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md). The classical apex $\mathcal M_x$ lives entirely on the decoherent face, where every member of the family agrees with Fisher–Rao. The family separates **only** in the off-diagonal ($i\ne j$) directions — the genuinely non-commutative tangents, the ones reached the instant $\rho$ acquires coherence in the character basis, i.e. the instant $[\log\rho,C_c]\neq0$. The width of the quantum apex *is* the width of the Petz family, and that width opens exactly off the decoherent face.

### 3.2 Three members {#sec:3-2}

\hypertarget{stmt:3-2}{}
**Theorem 3.2 (The three canonical members; Petz–Sudár 1996).** The following operator-monotone functions are admissible (each satisfies $f(1)=1$, $f(t)=tf(1/t)$), and the listed extremal/duality properties hold.

| name | $f(t)$ | mean | $c^f(x,y)$ | score relation $A=\mathbb J^f_\rho(\Lambda)$ | role |
|---|---|---|---|---|---|
| **SLD / Bures** | $\dfrac{1+t}{2}$ | arithmetic | $\dfrac{2}{x+y}$ | $A=\tfrac12(\rho\Lambda+\Lambda\rho)$ (Jordan) | **minimal** monotone metric; $4g^{\mathrm{SLD}}=$ QFI |
| **Kubo–Mori (BKM)** | $\dfrac{t-1}{\log t}$ | logarithmic | $\dfrac{\log x-\log y}{x-y}$ | $A=\displaystyle\int_0^1\rho^{u}\Lambda\,\rho^{1-u}\,du$ (i.e. $\Lambda=D\!\log\rho[A]$) | **dually flat**; Hessian of relative entropy |
| **RLD** | $\dfrac{2t}{1+t}$ | harmonic | $\dfrac{x+y}{2xy}$ | $A=\rho\Lambda$ (right mult.) | **maximal** monotone metric |

\hypertarget{stmt:3-3}{}
**Proposition 3.3 (Extremality, with proof of the bounds).** Among all admissible $f$,
$$\frac{2t}{1+t}\;\le\;f(t)\;\le\;\frac{1+t}{2}\qquad(t>0),$$
i.e. the harmonic mean is the smallest and the arithmetic mean the largest admissible $f$. Since $c^f=1/(y f(x/y))$ is *order-reversing* in $f$, the induced metrics satisfy
$$g^{\mathrm{SLD}}_\rho\;\le\;g^{\mathrm{KM}}_\rho\;\le\;g^{\mathrm{RLD}}_\rho$$
on every tangent vector, with the Kubo–Mori member strictly interior (logarithmic mean: $\mathrm{HM}\le\mathrm{LM}\le\mathrm{AM}$, strict off $x=y$). Thus **Bures/SLD is the minimal and RLD the maximal** monotone metric, and Kubo–Mori sits strictly between.

**Proof of the bounds.** Any operator-monotone $f$ on $(0,\infty)$ with $f(1)=1$ is concave (Löwner) and, with the symmetry $f(t)=tf(1/t)$, satisfies the standard sandwich between harmonic and arithmetic means (Kubo–Ando theory of operator means: every symmetric normalized operator mean lies between the harmonic and arithmetic means). Concavity plus $f(1)=1$ gives $f(t)\le f'(1)(t-1)+1$; the symmetry forces $f'(1)=\tfrac12$, hence $f(t)\le\frac{1+t}2$. Applying the upper bound to the dual $\tilde f(t)=t/f(t)$ (itself admissible) gives the harmonic lower bound. The mean inequalities $\frac{2t}{1+t}\le\frac{t-1}{\log t}\le\frac{1+t}2$ are the classical HM–LM–AM chain. $\square$

### 3.3 The score-operator reading: one fork, three names {#sec:3-3}

The deepest way to see the family is through the **quantum score** (logarithmic derivative). Classically a tangent vector $\delta p$ to the simplex has a unique score $\ell=\delta p/p$ (the log-derivative), and the Fisher metric is $\mathbb E_p[\ell^2]$. Quantumly the relation between a tangent vector $A=\delta\rho$ and "its" score operator $\Lambda$ is **not unique**, because $\rho$ and $\Lambda$ need not commute. Each admissible $f$ is a choice of the superoperator $\mathbb J^f_\rho$ with $A=\mathbb J^f_\rho(\Lambda)$ and $g^f_\rho(A,A)=\operatorname{tr}(\rho\,\Lambda^2)$-type:

- **SLD**: solve $A=\frac12(\rho\Lambda+\Lambda\rho)$ — the symmetric (Jordan) ordering. This $\Lambda$ is the symmetric logarithmic derivative; its metric is the quantum Fisher information of estimation theory, the Bures metric ([T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §7.2, Braunstein–Caves 1994).
- **Kubo–Mori**: solve $A=\int_0^1\rho^u\Lambda\rho^{1-u}\,du$ — equivalently $\Lambda=D\log\rho[A]$, the Fréchet derivative of the matrix logarithm. Here the score *is* the perturbation of $\log\rho$. This is the ordering of the Bogoliubov inner product.
- **RLD**: solve $A=\rho\Lambda$ — pure right multiplication; $\Lambda=\rho^{-1}A$ (non-Hermitian), the right logarithmic derivative.

All three collapse to the single classical score when $[\rho,A]=0$. Off that locus they are three genuinely different ways to *order $\rho$ against the perturbation* — and that is the entirety of the choice. **The metric family is the operator-ordering family.**

---

## 4. The operator ordering in $\mathcal M_\rho(\beta,c)$ is the metric fork {#sec:4}

This is the load-bearing section: we locate the §3 fork *inside* [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s density-matrix apex generator.

### 4.1 First order: the generator already chose, and it chose Kubo–Mori {#sec:4-1}

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (The one-observable generator is the geometric-mean power tilt).** With $L_\rho=\log\rho-\frac1N\operatorname{tr}(\log\rho)I$ as in [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §4.5,
$$\mathcal M_\rho(\beta,c)=\frac1N\operatorname{tr}\!\big(e^{\beta L_\rho}C_c^{\ast}\big)=(\det\rho)^{-\beta/N}\cdot\frac1N\operatorname{tr}\!\big(\rho^{\beta}\,C_c^{\ast}\big).$$
The scalar is **unambiguous** — a single trace of a product of two definite operators — for every $\rho$, $\beta$, $c$, commuting or not.

**Proof.** $\operatorname{tr}(\log\rho)=\log\det\rho$, so $L_\rho=\log\rho-\frac1N(\log\det\rho)I$ and $e^{\beta L_\rho}=e^{-\frac\beta N\log\det\rho}\,e^{\beta\log\rho}=(\det\rho)^{-\beta/N}\rho^{\beta}$, using that $\frac1N(\log\det\rho)I$ is central. $\square$

Two observations.

1. **Quantum geometric mean.** $(\det\rho)^{1/N}$ is the *geometric mean of the spectrum* of $\rho$ — the exact density-matrix analog of [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §5's complex geometric mean $G(z)=(\prod_jz_j)^{1/N}$ in the closure-diagonal identity $\mathcal M_z(m,c)=G(z)^{-m}\widehat{z^m}_c$. The mixed-state apex is literally the geometric-mean–normalized character-Fourier coefficient of the **escort/power family** $\rho\mapsto\rho^\beta$.

2. **The power family is the e-geodesic / BKM exponential family.** The curve $\beta\mapsto\rho^\beta/\operatorname{tr}\rho^\beta$ (equivalently $\rho_\beta=e^{\log\rho+\beta H}/Z$ for the appropriate $H$) is the *quantum exponential family* — tilting **inside the log**. This is the Bogoliubov–Kubo–Mori e-geodesic (Amari–Nagaoka 2000 §7; Petz 2008 §3). [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §7.3's escort $\rho_\beta=e^{\beta L_\rho}/\operatorname{tr}(e^{\beta L_\rho})$, there called the *Bures replicator*, is in fact the **Kubo–Mori e-geodesic**, not the Bures/SLD geodesic. At first order the generator has *already* committed — to Kubo–Mori, by writing $\log\rho$ in the exponent.

So the one-observable object hides no fork. The fork lives at second order.

### 4.2 Second order: the covariance of character observables, where ordering bites {#sec:4-2}

The information-geometric content of the classical apex is not the value $\mathcal M_x(\beta,c)$ alone but its **derivatives**: the cumulant tower of [T2](T2-CumulantTowerEffectiveAction.md), and in particular the second cumulant — the Fisher metric — and the third — the Amari–Chentsov tensor ([T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) §3). To continue *that* structure quantumly we need the **covariance of two character observables** $C_c,C_{c'}$ in the state $\rho$. And a covariance of two non-commuting observables is exactly where operator ordering is unavoidable.

\hypertarget{stmt:4-2}{}
**Definition 4.2 (Apex covariance kernel).** For $A=C_c-\operatorname{tr}(\rho C_c)I$ and $B=C_{c'}-\operatorname{tr}(\rho C_{c'})I$ the $\rho$-centered character observables (Hermitian only after a real combination; we take real/imaginary parts or work with $C_c,C_c^\ast$ pairs), and any admissible $f$, the **apex covariance** is the monotone-metric pairing
$$\Gamma^f_\rho(c,c'):=g^f_\rho\big(A,B\big)=\operatorname{tr}\!\big(A^\ast(\Omega^f_\rho)^{-1}B\big),\qquad \Omega^f_\rho=R_\rho^{1/2}f(\mathbf\Delta_\rho)R_\rho^{1/2}.$$
Its eigenbasis form is $\Gamma^f_\rho(c,c')=\sum_{i,j}c^f(\lambda_i,\lambda_j)\,\overline{A_{ij}}\,B_{ij}$.

\hypertarget{stmt:4-3}{}
**Theorem 4.3 (The fork in $\mathcal M_\rho$).** Fix $\rho\in\mathcal D_N$ off the decoherent face, so $[\log\rho,C_c]\neq0$ for some $c$. Then:

1. The candidate "quantum apex metric / quantum Amari–Chentsov tensor" — the second-order covariance structure $\Gamma^f_\rho(c,c')$ that continues [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) §3's cumulant diagonal — depends on the operator-monotone function $f$, and the dependence is supported entirely on the off-diagonal block $\{(i,j):i\ne j\}$, i.e. on the directions where $\rho$ and $C_c$ fail to commute ([Proposition 3.1](#stmt:3-1)).
2. The admissible orderings of "powers of $\rho$ interleaved between $C_c^\ast$ and $C_{c'}$" — the symmetrized product $\frac12(\rho C+C\rho)$, the BKM integral $\int_0^1\rho^uC\rho^{1-u}du$, the right product $\rho C$, and their convex/operator-mean interpolations — are *exactly* the Morozova–Chentsov functions $c^f$. Choosing the ordering **is** choosing $f$ **is** choosing the monotone metric.
3. On the decoherent face the dependence vanishes: $\Gamma^f_\rho(c,c')$ is $f$-independent and reduces to the classical character covariance of [T3](T3-CharacterOrthogonalityConductorLattice.md) under $\rho=\operatorname{diag}(p)$ ([Proposition 3.1](#stmt:3-1)).

**Proof.** (1) and (3) are immediate from the eigenbasis form $\Gamma^f_\rho=\sum_{ij}c^f(\lambda_i,\lambda_j)\overline{A_{ij}}B_{ij}$ together with $c^f(\lambda,\lambda)=1/\lambda$ ([Proposition 3.1](#stmt:3-1)): the diagonal terms are $f$-free, the off-diagonal terms carry all $f$-dependence, and the off-diagonal block is nonempty iff $[\rho,C_c]\neq0$. For (2), the three named superoperators $\Omega^f_\rho$ act on the dyad $|i\rangle\langle j|$ by multiplication by, respectively, $\frac{\lambda_i+\lambda_j}2$ (SLD), $\frac{\lambda_i-\lambda_j}{\log\lambda_i-\log\lambda_j}$ (KM), $\frac{2\lambda_i\lambda_j}{\lambda_i+\lambda_j}$ (RLD); these are the matrix elements of the symmetrized, BKM, and right-multiplication interleavings respectively, and Kubo–Ando theory identifies the full set of such positive interleavings with operator means $\leftrightarrow$ operator-monotone $f$. $\square$

**Reading.** The literal scalar $\mathcal M_\rho(\beta,c)$ is unambiguous (Proposition 4.1), but it is only the *generating value*. The moment one differentiates to extract the second-order information geometry — the only reason [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) wrote a generating function at all — the non-commutativity $[\log\rho,C_c]\neq0$ forces an ordering, and the ordering is the metric. This is the exact quantum face of "what is additive?": the classical generating function had a unique attendant metric (Chentsov); the quantum one has a corridor (Petz), and the corridor opens precisely along the coherences.

---

## 5. Kubo–Mori is the additive member {#sec:5}

Three of the family's members are canonical for three different reasons; the apex programme's own commitments select **one**.

### 5.1 The additivity criterion {#sec:5-1}

\hypertarget{stmt:5-1}{}
**Theorem 5.1 (BKM uniqueness; Grasselli–Streater 2001).** Among all monotone metrics on $\mathcal D_N$, the **Kubo–Mori (Bogoliubov–Kubo–Mori) metric** $g^{\mathrm{KM}}$ is the *unique* one that admits a **dually flat** pair of torsion-free affine connections (the $e$- and $m$-connections) — equivalently, the unique monotone metric whose geodesically convex "exponential family" and "mixture family" are dual with respect to a canonical divergence, the quantum relative entropy $S(\rho\|\sigma)=\operatorname{tr}\rho(\log\rho-\log\sigma)$, which then obeys a Pythagorean (additive) decomposition.

This is the precise quantum analog of the property that, *classically*, singles out the Fisher–Rao metric together with the $\pm1$-Amari connections: dual flatness, exponential/mixture duality, additive relative entropy. Classically Chentsov makes the metric unique and dual flatness comes for free; quantumly the metric is *not* unique, and dual flatness is the discriminating property that picks out exactly one member — Kubo–Mori.

### 5.2 Why this is *the* answer for the apex {#sec:5-2}

Three independent threads of the programme converge on Kubo–Mori.

1. **The generator already chose it (Proposition 4.1).** $\mathcal M_\rho$ tilts inside the log, $\rho^\beta=e^{\beta\log\rho}$. The e-geodesic of that tilt is the BKM exponential family; its natural second-order form is $g^{\mathrm{KM}}$. To then measure that family with the *Bures/SLD* metric would be to read an exponential family with the wrong ruler — geometrically inconsistent with the curve the generator draws.

2. **Additivity is the founding question ([T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)).** *What is additive?* is answered classically by the cumulant/exponential structure with its unique dually-flat metric. The honest quantum continuation keeps *additivity* as the selection criterion, and [Theorem 5.1](#stmt:5-1) says additivity selects Kubo–Mori. The Pythagorean theorem for quantum relative entropy — the thing that lets the programme keep saying "the cumulant decomposes additively" — holds for $g^{\mathrm{KM}}$ and for no other monotone metric.

3. **The cumulant tower survives ([T2](T2-CumulantTowerEffectiveAction.md)).** The Bogoliubov inner product $\langle A,B\rangle_{\mathrm{KM}}=\int_0^1\operatorname{tr}(\rho^u A\rho^{1-u}B)\,du-\operatorname{tr}(\rho A)\operatorname{tr}(\rho B)$ is the second cumulant of the BKM exponential family; the higher Bogoliubov correlation functions are its higher cumulants. These are exactly the quantum lifts of [T2](T2-CumulantTowerEffectiveAction.md)'s tower and [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) §3's Amari–Chentsov tensor. Choosing $g^{\mathrm{KM}}$ keeps the entire $\log\rho$ cumulant calculus of [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §4.5 intact; choosing SLD breaks it (the SLD second moment is not a cumulant of the power family).

We therefore **flag Kubo–Mori as the natural apex member** and recommend it as the default for any continuation of [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s density-matrix forward door — while insisting (§6) that the choice be *named*, since it is a choice.

### 5.3 What the other members buy {#sec:5-3}

The recommendation is not a claim that the others are wrong — they are optimal for *different* questions.

- **Bures/SLD** is the metric of *quantum estimation*: $4g^{\mathrm{SLD}}=$ QFI is the quantum Cramér–Rao bound. If a future apex paper is about *estimating* a ledger from measurements (state tomography of $\rho$), SLD is the correct ruler, and a *Bures apex* is then well-motivated — but for the estimation question, not the additivity question.
- **RLD** is the maximal metric and governs certain asymptotic and channel-capacity bounds. It is the natural extremal companion to SLD and useful as an *upper* envelope on the apex covariance ([Proposition 3.3](#stmt:3-3)).

The three are the minimal, the additive, and the maximal corners of the corridor. The apex programme, being a programme *about additivity*, lives at the middle corner.

---

## 6. Audit: where [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) walks the corridor unmarked {#sec:6}

[T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) is careful and explicit that the mixed-state generalization is a forward door; what it does *not* flag is that the door has more than one room. We record the three spots, with the correction this paper supplies.

\hypertarget{stmt:6-1}{}
**Audit 6.1.**

| locus in [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) | what it says | what is silently chosen | T24 correction |
|---|---|---|---|
| §4.5 forward door | defines $\mathcal M_\rho$ via $L_\rho=\log\rho$; "connecting this to the Bures metric … is the natural next paper" | naming the metric *Bures* commits to SLD | the *generator* is BKM (Prop 4.1); Bures is a different ruler. Name the choice. |
| §7.2 Conj. 7.2 + "planned forward paper *The Bures Apex*" | density-matrix decoherence theorem under the Bures metric | SLD as *the* quantum Fisher metric | "the quantum Fisher metric" is not unique (Thm 2.1). State which $f$. Recommend KM. |
| §7.3 Conj. 7.3 "Bures replicator" $\rho_\beta=e^{\beta L_\rho}/\operatorname{tr}(\cdot)$ | calls the escort flow a *Bures*-Fisher gradient flow | the escort is the BKM e-geodesic, not the SLD geodesic | rename to **Kubo–Mori replicator**; the flow is dually-flat-natural for $g^{\mathrm{KM}}$ (§5). |

None of these is an error in [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s *stated theorems* — Theorem 4.5 and the pure-state results live on the decoherent face / pure-state stratum, where [Proposition 3.1](#stmt:3-1) makes the fork degenerate and *every* metric agrees. The issue is purely in the **forward-door framing**: the moment one leaves the decoherent face (the whole point of going mixed-state), "Bures" stops being a free label and becomes a substantive, and probably non-optimal, choice. T24's role is to make [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s §7 say *Kubo–Mori (with Bures and RLD as the estimation-optimal and maximal alternatives)* instead of *Bures* tout court.

---

## 7. The quantum continuation of "what is additive?" {#sec:7}

\hypertarget{stmt:7-1}{}
**Thesis 7.1.** [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)'s founding question

$$\text{\emph{What is additive?}}$$

has, on positive (classical) ledgers, a unique answer, because the monotone metric is unique (Chentsov, [Theorem 1.2](#stmt:1-2)). On density-matrix (quantum) ledgers the question does not dissolve — it **forks**, into

$$\boxed{\text{\emph{Which operator ordering? — equivalently, which monotone metric?}}}$$

and **Chentsov-vs-Petz is the exact statement of that fork** ([Corollary 2.2](#stmt:2-2)). The classical case is the degenerate fiber of the quantum one ([Proposition 3.1](#stmt:3-1)): on the decoherent face the corridor has zero width, all members agree, and [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)'s definite article is restored.

This is not a metaphor. It is the same move the programme has made before. [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) discovered that the *additive coordinate* (the power-mean gauge $\beta$/$r$) is a *choice* the classical literature had been making silently; the Gauge Selection Principle made it explicit. T24 discovers that, in the quantum sector, the *information metric* is a second choice — invisible classically because Chentsov collapses it, unavoidable quantumly because Petz expands it — and the Metric Selection Principle makes *that* explicit:

\hypertarget{stmt:7-2}{}
> **Metric Selection Principle (quantum continuation of the Gauge Selection Principle).** *A statistical theory on density-matrix ledgers must answer, beyond "what is additive?", the strictly quantum question "with respect to which monotone metric?". The answer selects an operator ordering — an operator-monotone function $f$ — and the choice determines which second-order calculus (which quantum Fisher information, which quantum cumulant tower) applies. The decoherent face is the locus where the choice is vacuous; off it, it is modeling content. The additivity criterion (dual flatness, additive relative entropy) selects the Kubo–Mori member uniquely.*

Two gauges, then, where the classical theory saw one: the **additive gauge** $\beta$ (real, [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)) and the **ordering gauge** $f$ (operator-monotone, T24). [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §1.4 already anticipated a multi-axis gauge structure (amplitude, phase, conductor, gauge); T24 names the axis that only appears once amplitudes become operators.

---

## 8. Forward doors {#sec:8}

**8.1 The Kubo–Mori apex, written out.** Construct the full second-order apex calculus on $\mathcal D_N$ with $f=f_{\mathrm{KM}}$: the Bogoliubov cumulant tower, the dually-flat $\pm1$-connections, and the quantum Amari–Chentsov tensor as the $\beta$-Hessian of $\mathcal M_\rho$. This is the "natural next paper" of [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §7.2, now correctly named. *Planned: The Kubo–Mori Apex and the Quantum Cumulant Tower.*

**8.2 The Bures apex, as the estimation companion.** Separately, the SLD/Bures calculus for the *estimation* question (QFI, quantum Cramér–Rao on the apex), explicitly scoped as the minimal-metric corner, not the default. *Planned: The Bures Apex — Quantum Estimation on the Categorical Simplex.*

**8.3 Fork-width as a coherence diagnostic.** [Proposition 3.1](#stmt:3-1) makes $g^{\mathrm{RLD}}_\rho-g^{\mathrm{SLD}}_\rho$ a non-negative form supported exactly on the coherences of $\rho$ in the character basis. Its trace against the character observables is a scalar "off-decoherent-face" diagnostic — a candidate quantum sibling of the CBS $\sigma_{\mathrm{PI}}$ packet-inverse-participation diagnostic. *Probe, not paper.*

**8.4 The $N\to\infty$ subtlety.** In infinite dimensions the monotone-metric family persists but the extremal/uniqueness statements need von Neumann–algebraic care (Lesniewski–Ruskai 1999; type-III modular theory). The BKM/relative-entropy member is the most robust under that passage and is the natural one to carry into [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md) §7.5's Hilbert-space limit.

---

## 9. Coda {#sec:9}

Classically, "the information metric" is a phrase with one referent — Chentsov saw to that, and [T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md)–[T6](T6-RMSSimplicialQuadraticGauge-Draft1.md) spent the definite article freely and correctly. The quantum sector spends it on credit. Morozova–Chentsov–Petz replaced *the* metric with a corridor of them, parameterized by operator-monotone functions, separated only along the coherences — exactly the directions [T7](T7-ComplexAmplitudesQuantumSector-Draft1.md)'s $\mathcal M_\rho$ was built to reach. The non-commutativity $[\log\rho,C_c]\neq0$ is not an obstacle the apex must route around; it *is* the apex's quantum content, and the operator ordering it forces is, precisely and not by analogy, the choice of monotone metric.

The programme's own gravity points to one corner of the corridor. The generator tilts inside the log, so it draws the Kubo–Mori e-geodesic; the founding question is about *additivity*, and additivity (dual flatness, Pythagorean relative entropy) singles out Kubo–Mori uniquely. A "Bures apex" is a coherent and useful object — for *estimation*. For the apex programme it is the wrong ruler held up to the right curve.

The one-sentence apex of T24:

$$\boxed{\begin{array}{c}\text{Classically "what is additive?" has one answer because the monotone metric is unique;}\\[2pt]\text{quantumly it forks into "which operator ordering / which monotone metric?",}\\[2pt]\text{and the additive road is Kubo–Mori, not Bures.}\end{array}}$$

[T0](T0-GaugeSelectionFourierMellinSimplex-Draft1.md) named the additive gauge; T24 names the ordering gauge that only the quantum sector can see.

> **One classical metric; a corridor of quantum ones. Choosing among them is choosing what "additive" means.**

---

## Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper. The identification of the operator-ordering ambiguity in $\mathcal M_\rho$ with the Morozova–Chentsov–Petz fork, the first-order reduction to the geometric-mean power tilt, and the Kubo–Mori selection argument emerged through critique-and-upgrade exchanges that I record transparently. The selection of which contributions to keep and the responsibility for the mathematical content are mine.

---

## References

### T-series (companion papers)

- Murillo Montero, L. (2026). *T0 — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo preprint, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985).
- Murillo Montero, L. (2026). *T2 — Identifying 3: The Cumulant Tower as Effective Action.* Zenodo preprint, DOI [10.5281/zenodo.20338126](https://doi.org/10.5281/zenodo.20338126).
- Murillo Montero, L. (2026). *T3 — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint, DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049).
- Murillo Montero, L. (2026). *T6 — The RMS-Simplicial Quadratic Gauge.* Zenodo preprint, DOI [10.5281/zenodo.20392428](https://doi.org/10.5281/zenodo.20392428).
- Murillo Montero, L. (2026). *T7 — Complex Amplitudes and the Quantum Sector of the Apex.* Zenodo preprint, DOI [10.5281/zenodo.20392442](https://doi.org/10.5281/zenodo.20392442).

### Monotone metrics and quantum information geometry (the fork)

- Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs, Vol. 53. Providence, RI: American Mathematical Society. ISBN 978-0-8218-4502-8. *(Classical uniqueness, [Theorem 1.2](#stmt:1-2).)*
- Morozova, E. A. and Chentsov, N. N. (1989). Markov invariant geometry on manifolds of states (Russian). *Itogi Nauki i Tekhniki, Sovremennye Problemy Matematiki. Noveishie Dostizheniya* 36, 69–102. English translation: *Journal of Soviet Mathematics* 56 (1991), 2648–2669. [DOI: 10.1007/BF01095975](https://doi.org/10.1007/BF01095975). *(First quantum classification, [Theorem 2.1](#stmt:2-1).)*
- Petz, D. (1996). Monotone metrics on matrix spaces. *Linear Algebra and its Applications* 244, 81–96. [DOI: 10.1016/0024-3795(94)00211-8](https://doi.org/10.1016/0024-3795(94)00211-8). *(The operator-monotone classification, [Theorem 2.1](#stmt:2-1).)*
- Petz, D. and Sudár, C. (1996). Geometries of quantum states. *Journal of Mathematical Physics* 37, 2662–2673. [DOI: 10.1063/1.531535](https://doi.org/10.1063/1.531535). *(SLD / Kubo–Mori / RLD members, [Theorem 3.2](#stmt:3-2).)*
- Petz, D. (2008). *Quantum Information Theory and Quantum Statistics.* Theoretical and Mathematical Physics. Berlin: Springer. ISBN 978-3-540-74634-8. [DOI: 10.1007/978-3-540-74636-2](https://doi.org/10.1007/978-3-540-74636-2).
- Grasselli, M. R. and Streater, R. F. (2001). On the uniqueness of the Chentsov metric in quantum information geometry. *Infinite Dimensional Analysis, Quantum Probability and Related Topics* 4, 173–182. [DOI: 10.1142/S0219025701000462](https://doi.org/10.1142/S0219025701000462). *(BKM dual-flatness uniqueness, [Theorem 5.1](#stmt:5-1).)*
- Lesniewski, A. and Ruskai, M. B. (1999). Monotone Riemannian metrics and relative entropy on noncommutative probability spaces. *Journal of Mathematical Physics* 40, 5702–5724. [DOI: 10.1063/1.533053](https://doi.org/10.1063/1.533053).
- Kubo, F. and Ando, T. (1980). Means of positive linear operators. *Mathematische Annalen* 246, 205–224. [DOI: 10.1007/BF01371042](https://doi.org/10.1007/BF01371042). *(Operator means HM ≤ … ≤ AM; [Proposition 3.3](#stmt:3-3).)*

### Quantum Fisher information and the Bures/SLD member

- Bures, D. (1969). An extension of Kakutani's theorem on infinite product measures to the tensor product of semifinite $W^*$-algebras. *Transactions of the American Mathematical Society* 135, 199–212. [DOI: 10.2307/1995012](https://doi.org/10.2307/1995012).
- Uhlmann, A. (1976). The "transition probability" in the state space of a $*$-algebra. *Reports on Mathematical Physics* 9, 273–279. [DOI: 10.1016/0034-4877(76)90060-4](https://doi.org/10.1016/0034-4877(76)90060-4).
- Braunstein, S. L. and Caves, C. M. (1994). Statistical distance and the geometry of quantum states. *Physical Review Letters* 72, 3439–3443. [DOI: 10.1103/PhysRevLett.72.3439](https://doi.org/10.1103/PhysRevLett.72.3439).

### Information geometry, general

- Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs, Vol. 191. Providence, RI: American Mathematical Society. ISBN 978-0-8218-0531-2. [AMS page](https://bookstore.ams.org/mmono-191).
- Ay, N., Jost, J., Lê, H. V., and Schwachhöfer, L. (2017). *Information Geometry.* Ergebnisse der Mathematik und ihrer Grenzgebiete 64. Cham: Springer. ISBN 978-3-319-56477-7. [DOI: 10.1007/978-3-319-56478-4](https://doi.org/10.1007/978-3-319-56478-4).
- Bengtsson, I. and Życzkowski, K. (2017). *Geometry of Quantum States: An Introduction to Quantum Entanglement.* 2nd ed. Cambridge: Cambridge University Press. ISBN 978-1-107-02625-4. [DOI: 10.1017/9781139207010](https://doi.org/10.1017/9781139207010).
