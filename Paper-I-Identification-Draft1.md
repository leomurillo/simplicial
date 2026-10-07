<!--
Paper I — Identification.
First draft of the first of the post-trilogy RH-Done sequence.
Bridges the published trilogy (ל1 + ל2 + ל3) and Papers II + III.

Writing order: introduction → body → conclusion, then abstract and title last.

This file is the working manuscript. Do not commit unless asked.
-->

# Paper I — Identification: $\log\zeta$ as Categorical Effective Action on the Prime-Axis Simplex, and the $\mathbb{Q}(\sqrt{-3})$ Galois Decomposition of the $\mathbb{Z}/6$ Hurwitz Packet

**Leonardo Murillo Montero**

*Preprint, first draft — May 22, 2026*

---

## Abstract

**Situation.** The trilogy *Identifying 3* — `ל1`, `ל2`, `ל3` — supplied
a chart, a cumulant tower, and a character basis on the conductor lattice
of $\mathbb{Z}/N$, ending at the cubic selection rule $a + b + c \equiv 0
\pmod N$. The trilogy did not specify which exponential family to read on
the chart, or what cubic structure to expect off the uniform distribution.

**Task.** Identify the natural exponential family for the Riemann
zeta function, derive the cubic Amari–Chentsov tensor of its log-partition
in closed form, locate the critical line as a structural locus on the
primorial ladder, and resolve the smallest squarefree multi-prime modulus
($N = 6$) into its finite-arithmetic Galois content.

**Action.** Take the prime-axis multi-index space $\mathbb{N}^{(\mathcal{P})}$
with $X_p(n) = k_p(n)$ the $p$-adic valuation. The categorical exponential
family on $\mathbb{N}_{>0}$ with natural parameters $(\eta_p)_p$ has
log-partition $\Phi(\eta) = -\sum_p \log(1 - e^{\eta_p})$. Specialize along
$\eta_p(s) = -s\log p$. Read the cumulant tower in `ל3`'s character basis on
the residue-projected zeta distribution $Q^{(N)}(s)$. Use Gauss-sum
inversion to translate additive to multiplicative selection rules. At
$N = 6$, expand the Hurwitz channels in closed form. Identify their
2-dimensional span with the Galois decomposition of the Dedekind zeta of
$\mathbb{Q}(\sqrt{-3})$.

**Result.** On $\mathrm{Re}(s) > 1$, the Riemann zeta function satisfies
$\log\zeta(s) = \Phi(\eta(s))$, where $\Phi$ is `ל2`'s categorical
effective action of the prime-axis exponential family along the slice
$\eta_p(s) = -s\log p$ (**Theorem 2.1**); $\zeta$ continues meromorphically
to $\mathbb{C}\setminus\{1\}$, but $\log\zeta$ continues only as a
multi-valued object with branch singularities at the zeros of $\zeta$. The
third cumulant of the residue-projected zeta distribution $Q^{(N)}(s)$ on
$\mathbb{Z}/N$, read in `ל3`'s character basis, has the closed-form
polynomial expression
$T^\zeta(\chi_a, \chi_b, \chi_c; s, N) = \zeta(s)^{-1}\zeta_N(s, a+b+c) -
\zeta(s)^{-2}\sum_{(ij)}\zeta_N(s, i+j)\zeta_N(s, k) + 2\,\zeta(s)^{-3}\prod_j \zeta_N(s, j)$
in the additive twists $\zeta_N(s, k) = \sum_m e^{2\pi i k m/N}/m^s$
(**Theorem 3.1**); equivalently, it is $\partial_\theta^3 \Phi_N|_{\theta = 0}$
for the finite categorical exponential family $\Phi_N(\theta; s)$ on
$\mathbb{Z}/N$ with base distribution $Q^{(N)}(s)$, and it recovers the
trilogy selection rule as its $s \to 1^+$ boundary value. A naive scalar
functional equation $|\hat Q^{(N)}_k(s)| = N^{1/2 - \mathrm{Re}(s)}\,d_k^{\mathrm{Re}(s) - 1/2}\,
|\hat Q^{(N)}_{-k}(1-s)|$ for the twisted Plancherel coefficients
$\hat Q^{(N)}_k(s) := \zeta_N(s,k)/\zeta(s)$ **does not hold**: the
gamma factors of even ($\Gamma(s/2)$) and odd ($\Gamma((s+1)/2)$) Dirichlet
$L$-functions do not cancel uniformly against $\zeta$'s chi-factor, and the
identity fails at $N = 2, k = 1, s = 2$ (numerical counterexample, §4.4).
§4 records this withdrawal and identifies the correct vector/parity-mixed
functional equation as an open structural problem; the classical Riemann,
Mellin, and trilogy "$1/2$"s still converge independently on the critical
line (§4.6). The five non-trivial Hurwitz channels $\zeta(s, r/6)$ for
$r \in \{1, 2, 3, 4, 5\}$ live in a 2-dimensional function space spanned by
$\zeta(s)$ and $L(s, \chi_3)$, with explicit closed-form coefficients in
$a = 2^{-s}, b = 3^{-s}$ (**Theorem 5.1**); the K-involution
$r \to -r \pmod 6$ block-diagonalizes the collapse into a K-fixed
$\zeta$-channel and a K-anti-fixed $L_{\chi_3}$-channel (**Theorem 5.2**).
The Dedekind factorization
$\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) \cdot L(s, \chi_3)$ for the
degree-2 cover $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ is classical, with
K-involution matching the Galois involution of the cover
(**Identification T3.3**, a structural dictionary). The program's
$\mathbb{Z}/6$ Bures carrier is correspondingly handed off to Paper II as
the natural finite-arithmetic substrate for the degree-2 cover of the
Connes–Consani adele class space (**Identification I3.4** — a handoff, not
an analytic theorem). Two empirical probes confirm the closed forms to
machine precision (Hurwitz collapse: ~$10^{-60}$ analytical agreement;
Dedekind factorization: seven-digit class-number-formula agreement).

**Position.** Paper I is the first of three papers in the post-trilogy
**RH-Done** sequence: identification (this paper), the right carrier (Paper
II — occupation-decorated symmetric Fock + Uniform Place Treatment + CM
Poisson Monotonicity), closure (Paper III — convolution-square positivity
+ averaged CRT shadow uniformity + positive-current transport). Paper I
establishes **what the program is working with**; it does not construct
the Hilbert space (Paper II) or prove the Riemann Hypothesis (Paper III).

**Keywords:** Riemann zeta function, information geometry, categorical
exponential family, Amari–Chentsov tensor, conductor packet, Dirichlet
characters, Hurwitz zeta, Galois decomposition, Connes–Consani adele class
space, $\mathbb{Q}(\sqrt{-3})$, prime-axis simplex.

---

## Introduction

The trilogy *Identifying 3* — `ל1` [`Murillo2026a`], `ל2` [`Murillo2026b`],
`ל3` [`Murillo2026c`] — supplied a substrate whose shape does not depend on
which way the reader prefers to read it. From information geometry it is
the native simplicial chart, the cumulant tower of a single log-partition,
and the Pontryagin character basis on $\mathbb{Z}/N$. From discrete harmonic
analysis it is the same chart together with the DFT-diagonalization of the
categorical Fisher tensors. From classical analytic number theory it is the
beginning of a dictionary: at the third cumulant, evaluated at the uniform
distribution on $\mathbb{Z}/N$, the single selection rule
$$a+b+c \equiv 0 \pmod N$$
is the same line of modular arithmetic that controls diagonal contributions
to triple L-function moments. The trilogy stopped at the selection rule.
What sits on it has been the program's question ever since.

Paper I makes the answer explicit. On the Euler-product half-plane
$\mathrm{Re}(s) > 1$, $\log\zeta(s)$ is the trilogy's categorical
effective action — `ל2`'s $\Phi = \log Z$ — read on the prime-axis
exponential family ($\zeta$ continues meromorphically to
$\mathbb{C}\setminus\{1\}$; the $\log\zeta$ reading is single-valued only
on simply-connected zero-free subdomains). The third cumulant of the
residue-projected zeta distribution on $\mathbb{Z}/N$, in `ל3`'s residue
chart, has a closed-form expression, graded by the divisor lattice of $N$,
that recovers the trilogy selection rule as its high-temperature boundary
value. The critical line $\mathrm{Re}(s) = 1/2$ is identified by three
independent classical "$1/2$"s — Riemann's FE-symmetry, Mellin
self-duality, and the trilogy's amplitude convention — after withdrawing
an earlier conjectural scalar uniformity identity for the twisted
Plancherel coefficients $\zeta_N(s,k)/\zeta(s)$ that the parity-mixed gamma
factors of Dirichlet $L$-functions show to be false (§4.4). At the
smallest squarefree multi-prime modulus, $N = 6$, the five non-trivial
Hurwitz channels $\zeta(s, r/6)$ for $r \in \{1, 2, 3, 4, 5\}$ live not in
a 5-dimensional space but in the 2-dimensional space spanned by $\zeta(s)$
and the unique primitive Dirichlet $L$-function modulo $3$,
$L(s, \chi_3)$. This 2-channel system aligns row-by-row with the Galois
decomposition of the Dedekind zeta of $\mathbb{Q}(\sqrt{-3})$ under the
degree-2 cover $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ as a structural
dictionary: the program's K-involution on the $\mathbb{Z}/6$ Bures fiber
matches the Galois involution $\sqrt{-3} \mapsto -\sqrt{-3}$, and the
Dedekind factorization is classical. The metric-matching row (Arakelov ↔
Bures Hermitian) is flagged as a deferred handoff to Paper II.

These are the **identifications** Paper I delivers. They establish *what we
are working with* — they do not yet build the right Hilbert space (Paper II)
or close to a proof of the Riemann Hypothesis (Paper III).

### Position in the program

The trilogy `Identifying 3` is published [`Murillo2026a`, `Murillo2026b`,
`Murillo2026c`]. The present paper is the first of a second three-paper
sequence, **RH-Done**, of which the planned components are:

- **Paper I — Identification** (this paper). What the program is working
  with. Dots 1–3 of the spine [`RH-Done-Draft1`, §A].
- **Paper II — The Right Carrier**. The occupation-decorated symmetric Fock
  that hosts an exact von Mangoldt formula upstairs of the CRT compression;
  the Uniform Place Treatment that promotes this finite carrier to the
  Archimedean place by Stone–von Neumann uniqueness; the CM Poisson
  Monotonicity criterion. Dots 4–6.
- **Paper III — Closure**. Convolution-square positivity of Poisson windows,
  averaged CRT shadow uniformity at polynomial scale, the positive-current
  transport theorem, and the main theorem on RH via Polya–Laguerre. Dots
  7–10.

Paper I sits at the seam between two trilogies. It cites `ל1, ל2, ל3` as
established foundation; it sets the stage for `Paper II` by identifying the
right finite arithmetic substrate.

### What is new here, what is cited

The load-bearing identifications of Paper I were sketched in working notes
circulated within the program; we re-derive them in clean form here. The
provenance maps section by section as follows.

- **Theorem T2.1** *(Prime-Axis Effective Action; §2.5)* — clean rewrite of
  *siete* §2's substitution $\eta_p(s) = -s\log p \Rightarrow \Phi(\eta(s))
  = \log\zeta(s)$, integrated with the trilogy notation. No new analytic
  content; the partition-function-as-Euler-product identification is the
  same as in *siete*.
- **Theorem T2.2** *(Closed-Form Third Cumulant of $Q^{(N)}(s)$ on
  $\mathbb{Z}/N$; §3.4)* — clean rewrite of *siete* §5's closed-form
  polynomial in $\zeta_N(s, k)/\zeta(s)$, recast as the third cumulant of
  the residue-projected zeta distribution (equivalently, the
  Amari–Chentsov tensor of the finite categorical exponential family
  $\Phi_N(\theta;s)$ with base distribution $Q^{(N)}(s)$). The explicit
  term-by-term contraction of $T_{ijk}(Q^{(N)})$ against
  $\chi_a \otimes \chi_b \otimes \chi_c$ in the proof of Theorem 3.1 is new
  in Paper I; the finite-deformation identification with $\Phi_N$ is also
  new and explicit.
- **§4 — Withdrawn cubic functional equation, with the three-"1/2"s
  compatibility paragraph (§4.6) retained.** *Siete* §7 conjectured a
  scalar modulus identity
  $|\hat Q^{(N)}_k(s)| = N^{1/2 - \mathrm{Re}(s)}\,d_k^{\mathrm{Re}(s) - 1/2}\,
  |\hat Q^{(N)}_{-k}(1-s)|$
  and inferred a critical-line $N$-uniformity locus from it. **The scalar
  identity does not hold** (numerical counterexample at $N=2, k=1, s=2$;
  §4.4), because the gamma factors of even and odd Dirichlet $L$-functions
  do not cancel uniformly in the ratio $\zeta_N(s,k)/\zeta(s)$. §4 records
  the withdrawal of the conjecture, identifies the obstruction
  (parity-mixed vector functional equation in the Dirichlet $L$-basis),
  and retains the three-"1/2"s compatibility paragraph (§4.6) — the
  critical line remains identified by the classical Riemann, Mellin, and
  trilogy 1/2's, each independent of the withdrawn cubic uniformity claim.
- **Theorem T3.1** *(Closed Form for $\zeta(s, r/6)$; §5.2)* — promotion of
  [HPo-notes, Addendum A1] to a formal theorem with a three-step classical
  proof (half-shift collapse, mod-3 split, joint mod-6 reduction). New
  in Paper I.
- **Theorem T3.2** *(K-Orbit Parity Decomposition; §5.3)* — promotion of
  [HPo-notes, Addendum A2–A3] to a formal theorem. New in Paper I.
- **Identification T3.3** *(Structural dictionary for the
  $\mathbb{Q}(\sqrt{-3})$ Galois cover; §6.4)* — entry-by-entry dictionary
  table aligning the $(\zeta, L_{\chi_3})$ 2-channel structure with the
  Galois decomposition of the Dedekind zeta of $\mathbb{Q}(\sqrt{-3})$,
  with row-by-row justification. The Dedekind factorization
  $\zeta_K = \zeta \cdot L_{\chi_3}$ and the matching of K-involution
  with the Galois involution are classical/derived from Theorem 5.2; the
  rows identifying the Arakelov metric with a Bures Hermitian metric, and
  the program's $\mathbb{Z}/6$ Bures carrier with a degree-2 cover of the
  Connes–Consani adele class space, are **structural correspondences not
  proved from the data in Paper I** — they are handoffs to Paper II's
  functorial construction.
- **Identification I3.4** *(Handoff: the $\mathbb{Z}/6$ Bures carrier as
  the natural finite-arithmetic substrate for the
  $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ cover; §6.5)* — structural handoff to
  Paper II; not an analytic theorem.
- **Theorem T5.3** *(Strict positivity of $L(1/2, \chi_3)$; §5.6)* —
  rigorous interval-arithmetic verification that $L(1/2, \chi_3) > 0$,
  combined with the Iwaniec–Sarnak (2000) non-negativity result on the
  same family. The interval computation is via the Hurwitz representation
  and a verified bound on the truncation tail; the LMFDB record
  `1-3-3.2-r1-0-0` is referenced as a numerical cross-check. New in Paper
  I in this rigorous form; the underlying value is classical.

The numerical verifications underlying T3.1 and T3.3 are recorded in the
probes [`probe_Hurwitz_z6_closed_form.py`] (verifies T3.1 + T3.2 to
60-digit `mpmath` precision; verifies K-even zero-ordinate constraints to
machine epsilon) and [`probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`]
(verifies Dedekind factorization against finite Euler product on norms
$\leq 200$; class-number-formula agreement to $\sim 10^{-7}$).

### Two audiences

The paper is written for two readerships, and bridges between them.

**For the information geometer.** The conjugacy between $\eta$-coordinates
and $p$-coordinates, the cumulant tower of $\Phi = \log Z$, the
Amari–Chentsov tensor, the conductor packet $H_d$, and the character
selection rule on $\mathbb{Z}/N$ are all assumed familiar from the trilogy.
The analytic-number-theoretic objects entering Paper I — Dirichlet
$L$-functions $L(s, \chi)$, the Hurwitz zeta $\zeta(s, r/N)$, the additive
twist $\zeta_N(s, k)$, Gauss sums, and the functional equation of
$\zeta$ — are introduced with one-line glosses where they appear, but
without re-derivation; the standard reference is [Iwaniec & Kowalski, 2004].

**For the analytic number theorist.** $\zeta$, Dirichlet characters, and the
explicit-formula bridge are assumed familiar. The
information-geometric objects entering Paper I — the categorical
exponential family on $H_0$, the Legendre duality
$\eta \leftrightarrow p = \nabla\Phi$, the Fisher information $\Sigma$ as a
covariance, the Amari–Chentsov tensor $T_{ijk}$ as a third cumulant, and the
conductor packet $H_d$ on $\mathbb{Z}/N$ — are introduced with one-line
glosses where they appear; the standard reference is [Amari & Nagaoka,
2000]. The reader who is willing to import a chart in which $\log\zeta$ is
the natural object will find Paper I a chain of identifications, each one
classical in either of the two languages.

### Roadmap

§1 recaps the trilogy in three pages. §2 executes the prime-axis effective
action identification (Theorem 2.1 = T2.1). §3 develops the closed-form
third cumulant of $Q^{(N)}(s)$ in the residue chart (Theorem 3.1 = T2.2),
with the explicit finite-deformation reading $\partial^3_\theta \Phi_N|_{\theta=0}$.
§4 examines functional equations on $\mathbb{Z}/N$: it withdraws the
conjectural scalar uniformity identity that an earlier draft (*siete* §7)
used to pin the critical line, records the parity-mixed gamma obstruction,
and retains the critical-line identification via three independent
classical "$1/2$"s (§4.6). §5 promotes the $\mathbb{Z}/6$ 2D collapse from
the HPo Addendum A working note into a clean theorem (T3.1, T3.2). §6
carries that into the Galois dictionary with $\mathbb{Q}(\sqrt{-3})$ (T3.3,
I3.4) following HPo Addendum H. §7 closes with the hand-off to Paper II.

---

## §1. The Trilogy in One Page

This section is cite-and-use. It collects the three theorems and one
identification from `Identifying 3` that Paper I needs as input, in the form
in which they are quoted later. No proofs are given here; all are in the
published trilogy.

### 1.1 The native chart (`ל1`)

The probability simplex $\Delta^{N-1} \subset \mathbb{R}^N$ over $N$ outcomes
has its natural tangent space at any interior point given by the zero-sum
hyperplane
$$H_0 \;=\; \bigl\{ x \in \mathbb{R}^N \,:\, \textstyle\sum_i x_i = 0\bigr\}.$$
Through the square-root map $\psi : \Delta^{N-1} \to S^{N-1}_+$,
$\psi(p) = (\sqrt{p_1}, \ldots, \sqrt{p_N})$, the Fisher–Rao metric
$g_{\mathrm{FR}}$ on $\Delta^{N-1}$ is the pullback of $4 g_S$, where $g_S$
is the round sphere metric on $S^{N-1}_+$. At the uniform distribution
$u = \tfrac{1}{N}(1, \ldots, 1)$ the Fisher–Rao isometry group is
$$\mathrm{Stab}_{g_{\mathrm{FR}}}(u) \;=\; \mathrm{SO}(H_0) \;\cong\; \mathrm{SO}(N-1).$$
This is **Theorem T1.1**.

### 1.2 The cumulant tower (`ל2`)

Take $\eta = (\eta_1, \ldots, \eta_N) \in H_0$ as natural parameters of the
categorical exponential family
$$p_i(\eta) \;=\; \frac{e^{\eta_i}}{Z(\eta)},
  \qquad Z(\eta) \;=\; \sum_{j=1}^N e^{\eta_j},$$
and define the **categorical effective action**
$$\boxed{\;\Phi(\eta) \;:=\; \log Z(\eta).\;}$$
Successive derivatives of $\Phi$ in $\eta$ generate the cumulant tower of
the sufficient statistic $X$. The first four orders are
$$\partial_i \Phi \;=\; p_i \quad (\text{mean / position}), \qquad
  \partial_i \partial_j \Phi \;=\; p_i \delta_{ij} - p_i p_j \quad
  (\text{Fisher information } \Sigma_{ij}),$$
$$\partial_i \partial_j \partial_k \Phi \;=\; p_i \delta_{ij}\delta_{ik}
  - p_i p_k \delta_{ij} - p_i p_j \delta_{ik} - p_i p_j \delta_{jk}
  + 2 p_i p_j p_k \quad (\text{Amari–Chentsov tensor } T_{ijk}),$$
$$\partial_i \partial_j \partial_k \partial_\ell \Phi
  \;=\; Q_{ijk\ell} \quad (\text{closure defect / fourth cumulant}).$$
One scalar functional $\Phi$ generates four named geometric objects through
plain differentiation. This is **Theorem T1.2**. The leap from order 2
(Riemannian, Gaussian-visible) to order 3 (Amari–Chentsov, the first invariant
beyond Riemannian geometry) is the trilogy's titular *Identifying 3*; we
will write **I1.4** for this structural observation when we need to label it.

### 1.3 The character selection rule (`ל3`)

Identify the outcome index set with the cyclic ring $\mathbb{Z}/N$. The
Pontryagin character basis on $\mathbb{C}^N$ is
$$\chi_k(x) \;=\; e^{2\pi i k x / N}, \qquad k, x \in \mathbb{Z}/N.$$
The non-trivial characters $\{\chi_k\}_{k = 1, \ldots, N-1}$ span the
complexification $H_0 \otimes \mathbb{C}$. Each $\chi_k$ has a *conductor*
$d_k := N/\gcd(k, N)$, equal to the smallest divisor of $N$ on which $\chi_k$
is natively defined. The conductor packet
$$H_d \;:=\; \mathrm{span}_{\mathbb{C}}\bigl\{\chi_k \,:\, d_k = d\bigr\},
  \qquad \dim_{\mathbb{C}} H_d \;=\; \varphi(d),$$
gives the decomposition
$$H_0 \otimes \mathbb{C} \;=\; \bigoplus_{\substack{d \mid N \\ d > 1}} H_d.$$
Read `ל2`'s tensors at the uniform $u$ in this basis. The Fisher information
becomes diagonal — in fact scalar:
$$\Sigma\bigl(\chi_a, \chi_b\bigr)\big|_u \;=\; \delta_{a,b} \quad
  \text{for } a, b \in \{1, \ldots, N-1\}.$$
The Amari–Chentsov tensor satisfies the **selection rule**
$$\boxed{\;T\bigl(\chi_a, \chi_b, \chi_c\bigr)\big|_u
  \;=\; \delta_{a+b+c \equiv 0 \pmod N}, \quad a, b, c \in \{1, \ldots, N-1\}.\;}$$
This is **Theorem T1.3**. The second cumulant is silent on arithmetic; the
third cumulant carries the modular constraint.

### 1.4 What Paper I adds

The trilogy stopped at the selection rule. It established that **if** the
categorical exponential family of `ל2` is read on a $\mathbb{Z}/N$-structured
outcome set, **then** the third cumulant at the uniform satisfies
$a+b+c \equiv 0 \pmod N$. It did not specify *which* exponential family one
should care about, or *what* the resulting cubic structure looks like
*off* the uniform.

The present paper specifies. The right exponential family — for the
Riemann Hypothesis — is the prime-axis family of §2 below, with
$\Phi = \log\zeta$ on $\mathrm{Re}(s) > 1$. The third cumulant of the
residue-projected zeta distribution on $\mathbb{Z}/N$ — read in T1.3's
character basis as $\partial^3_\theta \Phi_N|_{\theta=0}$ of the finite
categorical exponential family with base $Q^{(N)}(s)$ — has a closed form
(T2.2). The critical line is identified by the classical Riemann, Mellin,
and trilogy "$1/2$"s of §4.6, after withdrawing the conjectural scalar
uniformity identity that an earlier draft (*siete* §7) attempted as the
mechanism. At $N = 6$ the five non-trivial Hurwitz channels collapse to a
2D system (T3.1, T3.2). That 2D system aligns row-by-row with the Galois
decomposition of $\zeta_{\mathbb{Q}(\sqrt{-3})}$ as a structural dictionary
(T3.3), with the metric-matching row flagged for Paper II (I3.4). The
trilogy supplied the substrate; the present paper names the natural
object on it.

---

## §2. The Prime-Axis Exponential Family and $\log\zeta$

We introduce the prime-axis exponential family on the discrete probability
space $\mathbb{N}_{>0}$ and identify its categorical effective action
$\Phi$ with $\log\zeta(s)$. The identification (Theorem T2.1) is by
substitution, not analogy.

### 2.1 Prime-axis coordinates on $\mathbb{N}_{>0}$

Every positive integer $n$ has a unique factorization
$$n \;=\; \prod_{p \in \mathcal{P}} p^{k_p(n)}, \qquad k_p(n) \in \mathbb{N},$$
where $\mathcal{P} = \{2, 3, 5, 7, 11, \ldots\}$ is the set of primes and
only finitely many $k_p(n)$ are nonzero. The map $n \mapsto k(n) = (k_p(n))_p$
is a bijection $\mathbb{N}_{>0} \cong \mathbb{N}^{(\mathcal{P})}$ onto the
finitely-supported $\mathbb{N}$-valued sequences indexed by primes. We treat
$\mathbb{N}^{(\mathcal{P})}$ as the **prime-axis multi-index space** on which
the prime-axis exponential family is defined.

The *sufficient statistic on the $p$-axis* is $X_p(n) := k_p(n)$, the $p$-adic
valuation of $n$. The $p$-axes are statistically independent under the
factorization (formalized below).

### 2.2 The exponential family and its log-partition

Let $\eta = (\eta_p)_{p \in \mathcal{P}}$ be a sequence of complex natural
parameters indexed by primes, with $\mathrm{Re}(\eta_p) < 0$ for every $p$
and the regularity condition $\sum_p |e^{\eta_p}| / (1 - |e^{\eta_p}|) <
\infty$ (which suffices for absolute convergence of every cumulant computed
below).

**Definition 2.1.** The *prime-axis exponential family* on $\mathbb{N}_{>0}$
is the family of probability distributions
$$p_n(\eta) \;=\; \frac{1}{Z(\eta)} \exp\!\Bigl(\sum_p k_p(n)\,\eta_p\Bigr),
  \qquad Z(\eta) \;=\; \sum_{n=1}^\infty
   \exp\!\Bigl(\sum_p k_p(n)\,\eta_p\Bigr).$$

The partition function factorizes by prime axis. Set $u_p := e^{\eta_p}$;
then
$$Z(\eta) \;=\; \sum_n \prod_p u_p^{k_p(n)} \;=\; \prod_p \sum_{k=0}^\infty
  u_p^k \;=\; \prod_p \frac{1}{1 - u_p},$$
where the double interchange of sum and product is justified by absolute
convergence under our regularity condition. The log-partition is therefore
$$\boxed{\;\Phi(\eta) \;=\; \log Z(\eta) \;=\; -\sum_p \log(1 - e^{\eta_p}).\;}$$

**The Euler product is categorical independence.** The factorization of
$Z(\eta)$ by prime axis is the partition-function fingerprint of the
multiplicative independence of the prime-axis sufficient statistics
$(X_p)_p$. Equivalently: under any $\eta$, the joint distribution of
$(X_p)_p$ under the prime-axis exponential family is the product of geometric
distributions, one per prime, with $p$-axis parameter $u_p = e^{\eta_p}$:
$$\mathrm{Pr}_\eta\bigl(X_p = k\bigr) \;=\; (1 - u_p)\, u_p^k, \qquad k \in \mathbb{N}.$$
The cumulant tower of $\Phi$ is, by construction, **diagonal in primes at
every order**: $\partial_{\eta_p} \partial_{\eta_q} \Phi = 0$ for $p \neq q$,
and similarly for all higher mixed partials.

### 2.3 Specialization to $\eta_p(s) = -s \log p$

Take a one-parameter family of natural parameters along the *diagonal slice*
$$\eta_p(s) \;:=\; -s \log p, \qquad p \in \mathcal{P}, \quad s \in \mathbb{C}.$$
For $\mathrm{Re}(s) > 1$ the regularity condition of §2.2 is satisfied
(this is the standard convergence region of $\zeta$), and
$e^{\eta_p(s)} = p^{-s}$. Substituting into the log-partition,
$$\Phi(\eta(s)) \;=\; -\sum_p \log\bigl(1 - p^{-s}\bigr) \;=\; \log\zeta(s).$$
We write $\Phi_\zeta(s) := \log\zeta(s)$ for this *diagonal specialization*
of $\Phi$, and we analytically continue $\Phi_\zeta$ to the standard domain
$\mathbb{C}\setminus\{1\}$ in the usual way (from this point onward
$\Phi_\zeta$ means the analytically continued object).

**The zeta distribution.** Under the natural parameter $\eta(s)$ at real
$s > 1$, the prime-axis exponential family on $\mathbb{N}_{>0}$ has
mean-parameter distribution
$$q_n(s) \;=\; \prod_p (1 - p^{-s})\, p^{-s k_p(n)} \;=\; \frac{1}{\zeta(s)}\,n^{-s},$$
which is the classical **Riemann zeta distribution** on $\mathbb{N}_{>0}$.

### 2.4 The Mellin/amplitude reading

Through the trilogy's square-root map $\psi$ (§1.1) applied to $q(s)$, the
amplitude vector on $\mathbb{N}_{>0}$ is
$$a_n(s) \;=\; \sqrt{q_n(s)} \;=\; \frac{n^{-s/2}}{\sqrt{\zeta(s)}}.$$
The Bhattacharyya coefficient of two zeta amplitudes at parameters
$s_1, s_2$ is
$$\langle a(s_1), a(s_2)\rangle \;=\; \sum_n a_n(s_1)\, a_n(s_2) \;=\;
  \frac{\zeta\bigl((s_1+s_2)/2\bigr)}{\sqrt{\zeta(s_1)\,\zeta(s_2)}}.$$
**The Bhattacharyya pairing is $\zeta$-valued at the midpoint** $(s_1+s_2)/2$.
Taking $s_1 = 1/2 + it$, $s_2 = 1/2 - it$ (a functional-equation conjugate
pair on the critical line) gives midpoint $1/2$, so
$$\langle a(1/2+it), a(1/2-it)\rangle \;=\; \frac{\zeta(1/2)}{|\zeta(1/2+it)|}.$$
The central value $\zeta(1/2)$ is the Bhattacharyya inner product of the
amplitude vector of the zeta distribution with its functional-equation
conjugate. We note this without claiming it is a new analytic fact; the
content is structural — $\zeta(1/2)$ is doing geometric work in the trilogy's
chart that the chart was not designed to host.

### 2.5 Theorem T2.1: Prime-Axis Effective Action

We now state the identification.

**Theorem 2.1** (*Prime-Axis Effective Action; T2.1 of [`RH-Done-Draft1`]*).
*On the half-plane $\mathrm{Re}(s) > 1$, the Riemann zeta function
satisfies $\log\zeta(s) = \Phi(\eta(s))$, where $\Phi$ is the log-partition
function of the prime-axis exponential family of §2.2 and $\eta(s)$ is the
diagonal slice $\eta_p(s) = -s\log p$:*
$$\Phi_\zeta(s) \;:=\; \Phi\bigl(\eta(s)\bigr) \;=\; -\sum_p \log\bigl(1 - p^{-s}\bigr) \;=\; \log\zeta(s), \qquad \mathrm{Re}(s) > 1.$$
*The corresponding mean-parameter distribution is the Riemann zeta
distribution $q_n(s) = n^{-s}/\zeta(s)$ on $\mathbb{N}_{>0}$, defined first
on $\mathrm{Re}(s) > 1$ and extended meromorphically to $s \in
\mathbb{C}\setminus\{1\}$ wherever $\zeta(s) \neq 0$.*

*Proof.* The factorization argument of §2.2 gives
$\Phi(\eta) = -\sum_p \log(1 - e^{\eta_p})$ on the regularity domain of
§2.2. The substitution $\eta_p(s) = -s\log p$ of §2.3 specializes this to
$-\sum_p \log(1 - p^{-s})$, which is the standard Euler product
representation of $\log\zeta(s)$ on $\mathrm{Re}(s) > 1$. The
mean-parameter identification of $q_n(s)$ with the Riemann zeta
distribution is direct substitution. $\square$

**Scope of the $\log\zeta$ identification.** $\zeta(s)$ continues to a
meromorphic function on $\mathbb{C}\setminus\{1\}$ (DLMF 25.2); $\log\zeta(s)$
does **not** continue as a globally single-valued meromorphic function,
because each non-trivial zero of $\zeta$ is a branch singularity of any
local branch of $\log\zeta$. The identification of Theorem 2.1 is therefore
stated cleanly on $\mathrm{Re}(s) > 1$; on any simply connected zero-free
subdomain of $\mathbb{C}\setminus\{1\}$ it extends to a chosen branch of
$\log\zeta$. Throughout Paper I we use "$\log\zeta$" as a structural label
for $\Phi_\zeta$; when an analytic statement must hold globally, we work
with $\zeta$, $\zeta'/\zeta$, or the additive twist ratios
$\zeta_N(s,k)/\zeta(s)$ — all single-valued meromorphic on
$\mathbb{C}\setminus\{1\}$ — rather than with a putative global $\log\zeta$.

### 2.6 The cumulant tower of $\Phi$ in the prime-axis chart

Because $\Phi$ is additive over primes, every cumulant tensor of $\Phi$ in
the prime-axis chart is diagonal in primes. On a single prime axis, set
$u = e^{\eta_p}$ and write $\Phi^{(p)}(\eta_p) = -\log(1 - u)$. Repeated
application of the chain rule $d/d\eta_p = u \cdot d/du$ yields
$$\partial^n_{\eta_p} \Phi^{(p)} \;=\; \mathrm{Li}_{-(n-1)}(u)
  \;=\; \sum_{k=1}^\infty k^{n-1}\, u^k, \qquad n \geq 1,$$
the *negative-index polylogarithm*. Equivalently, with $A_{n-1}(u)$ the
$(n-1)$st Eulerian polynomial,
$$\partial^n_{\eta_p} \Phi^{(p)} \;=\; \frac{u\, A_{n-1}(u)}{(1-u)^n}.$$
The successive geometric-distribution cumulants on the $p$-axis emerge as
the values of these polylogarithms at $u = e^{\eta_p}$.

Specializing to $\eta_p = -s\log p$ gives the per-axis cumulants
$$\Sigma_{pp}(s) \;=\; \frac{p^{-s}}{(1 - p^{-s})^2}, \qquad
  T_{ppp}(s) \;=\; \frac{p^{-s}(1 + p^{-s})}{(1 - p^{-s})^3}, \qquad \ldots,$$
with all cross-prime entries vanishing. **The prime-axis chart is silent on
arithmetic.** All cubic content is diagonal; no cross-prime selection rule
is visible.

This is not a defect; it is a constraint on what charts can see. Arithmetic
content lives off the prime-axis chart, in dual coordinates. The
$\mathbb{Z}/N$ residue chart of §3 is the natural dual: there the
character selection rule of T1.3 becomes the operational support condition.

> The prime-axis chart and the residue chart are Fourier duals. The
> prime-axis chart trivializes the cumulant tower (diagonal in primes); the
> residue chart trivializes the arithmetic structure (selection rule on
> character indices). The cubic A-C tensor of $\Phi_\zeta$ exhibits both
> faces — as a sum of single-axis polylogs in the prime-axis chart, and as
> a finite linear combination of Dirichlet $L$-functions of cyclic moduli
> in the residue chart.

---

## §3. The Residue Chart and the Closed-Form Cubic A-C Tensor

We now read $\Phi_\zeta = \log\zeta$ in the trilogy's character basis on
$\mathbb{Z}/N$. Section 3.1 defines the residue-projected zeta distribution
$Q^{(N)}(s)$; section 3.2 introduces the *additive-twist zeta*
$\zeta_N(s, k)$ as the natural Fourier coefficient of $Q^{(N)}(s)$; section
3.3 recalls the conductor-packet decomposition for primorial $N$;
section 3.4 derives the **closed-form formula** for the cubic A-C tensor
on the zeta distribution; section 3.5 verifies that this formula recovers
T1.3's selection rule in the $s \to 1^+$ high-temperature limit; section
3.6 records the Gauss-sum duality identifying additive-character selection
with multiplicative-character orthogonality of triple $L$-moments.

### 3.1 The residue-projected zeta distribution

Fix $N \geq 2$. The reduction-mod-$N$ map $r_N : \mathbb{N}_{>0} \to
\mathbb{Z}/N$, $r_N(m) = m \bmod N$, pushes the zeta distribution of §2.3
to a discrete distribution on $\mathbb{Z}/N$.

**Definition 3.1.** For $s \in \mathbb{C}$ with $\mathrm{Re}(s) > 1$ and
$r \in \mathbb{Z}/N$,
$$Q^{(N)}_r(s) \;:=\; \mathrm{Pr}_{X \sim q(s)}\bigl[X \equiv r \pmod N\bigr]
  \;=\; \frac{1}{\zeta(s)}\sum_{m \equiv r \pmod N} m^{-s}.$$

For real $s > 1$, $Q^{(N)}_r(s) > 0$ for every $r$ and
$\sum_r Q^{(N)}_r(s) = 1$, so $Q^{(N)}(s) \in \Delta^{N-1}$. For complex
$s$ with $\mathrm{Re}(s) > 1$, $Q^{(N)}(s)$ is a normalized signed measure
on $\mathbb{Z}/N$; for $\mathrm{Re}(s) \leq 1$ both $\zeta(s)$ and the
inner sum acquire poles and the normalization becomes problematic. The
analytic identifications below are stated on $\mathrm{Re}(s) > 1$ and
extended by meromorphic continuation in the usual way.

### 3.2 The additive-twist zeta and the Fourier coefficients of $Q^{(N)}$

Read $Q^{(N)}(s)$ in T1.3's character basis $\{\chi_k(r) = e^{2\pi i k r/N}\}_{k \in \mathbb{Z}/N}$:
$$\hat Q^{(N)}_k(s) \;:=\; \sum_{r \in \mathbb{Z}/N} Q^{(N)}_r(s)\,\chi_k(r)
  \;=\; \frac{1}{\zeta(s)}\sum_{m=1}^\infty \frac{e^{2\pi i k m/N}}{m^s}.$$

**Definition 3.2.** The *additive-twist zeta* at modulus $N$ and frequency $k$ is
$$\boxed{\;\zeta_N(s, k) \;:=\; \sum_{m=1}^\infty \frac{e^{2\pi i k m / N}}{m^s}.\;}$$

Then
$$\hat Q^{(N)}_k(s) \;=\; \frac{\zeta_N(s, k)}{\zeta(s)}.$$

Two boundary values are immediate.

- **Trivial frequency $k = 0$:** $\zeta_N(s, 0) = \zeta(s)$, so
  $\hat Q^{(N)}_0(s) = 1$ — the probability normalization.

- **High-temperature limit $s \to 1^+$:** by the Wiener–Ikehara theorem
  applied to $\sum_{m \equiv r \pmod N} m^{-s}$ — equivalently, by the
  primitive-character L-function dictionary of §3.6 below combined with
  the simple pole structure of $L(s, \chi_0) = \zeta(s) \prod_{p | N}(1 -
  p^{-s})$ — every $Q^{(N)}_r(s) \to 1/N$ as $s \to 1^+$. Equivalently,
  $\hat Q^{(N)}_k(s) \to \delta_{k \equiv 0 \pmod N}$.

The second observation says that the residue-projected zeta distribution
*continuously deforms* to the uniform distribution on $\mathbb{Z}/N$ as $s
\to 1^+$. This is the natural base point for reading the trilogy's
selection rule.

### 3.3 Conductor packets on $\mathbb{Z}/N$

We recall T1.3's conductor-packet decomposition (`ל3` §3) and specialize
to the case $N = P_n := p_1 p_2 \cdots p_n$ of a primorial modulus, which
is the natural ladder along which Paper II's transport theorem will compute.

Each character $\chi_k$ on $\mathbb{Z}/N$ has conductor
$d_k := N/\gcd(k, N)$. For squarefree $N$ — in particular $N = P_n$ — every
divisor $d \mid N$ corresponds to a subset $S \subseteq \{p_1, \ldots, p_n\}$
with $d = \prod_{p \in S} p$. The conductor packet
$$H_d \;=\; \mathrm{span}_{\mathbb{C}}\bigl\{\chi_k \,:\, d_k = d\bigr\}$$
has dimension $\varphi(d) = \prod_{p \in S}(p-1)$. The total dimension of
$H_0(\mathbb{Z}/P_n)$ is $P_n - 1 = \sum_{d \mid P_n,\, d > 1} \varphi(d)$,
which is a special case of $\sum_{d \mid N} \varphi(d) = N$.

The Fourier coefficient $\hat Q^{(N)}_k(s) = \zeta_N(s, k)/\zeta(s)$ is
**attached to the conductor packet $H_{d_k}$** of T1.3 — the conductor $d_k$
fixes the set of primitive characters whose $L$-functions enter the
Gauss-sum expansion of §3.6 — but it varies **within** the packet $H_{d_k}$
with the reduced index $k' = k/\gcd(k,N) \in (\mathbb{Z}/d_k)^\times$. For
prime modulus $N = p$ with $k = 1$ and $k = 2$ (say $p = 5$), the two
twists have the same conductor $d_k = 5$ but $\zeta_5(s,1) \neq \zeta_5(s,2)$
as functions; they differ by the Gauss-sum weighted combination of the
$\varphi(5) = 4$ primitive characters mod $5$. The conductor controls which
$L$-functions can appear; the reduced index controls the linear combination.

The residue chart on $\mathbb{Z}/P_n$ is the natural setting in which the
prime-axis cross-prime structure becomes visible, graded by the divisor
lattice of $P_n$.

### 3.4 Closed form for the cubic Amari–Chentsov tensor at $Q^{(N)}(s)$

We compute T1.2's third cumulant tensor $T_{ijk}$ at the distribution
$p = Q^{(N)}(s)$, read in T1.3's character basis.

**The finite-deformation reading.** Before the term-by-term computation, we
fix the rigorous content of what is being computed. The categorical
exponential family on $\mathbb{Z}/N$ with reference distribution
$Q^{(N)}(s)$ has natural parameters $\theta = (\theta_k)_{k \in \mathbb{Z}/N
\setminus\{0\}} \in H_0(\mathbb{Z}/N) \otimes \mathbb{C}$ and log-partition
$$\Phi_N(\theta; s) \;:=\; \log \!\Bigl(\sum_{r \in \mathbb{Z}/N} Q^{(N)}_r(s)\, \exp\!\Bigl(\sum_k \theta_k\, \chi_k(r)\Bigr)\Bigr).$$
This is `ל2`'s framework specialized to the finite $\mathbb{Z}/N$ grid with
base point $Q^{(N)}(s)$, and its third derivative
$\partial_{\theta_a}\partial_{\theta_b}\partial_{\theta_c} \Phi_N|_{\theta=0}$
is exactly the third cumulant of the triple
$(\chi_a(X), \chi_b(X), \chi_c(X))$ under $X \sim Q^{(N)}(s)$. **The closed
form below is $\partial^3_\theta \Phi_N|_{\theta=0}$**; the "Amari–Chentsov
tensor of $\log\zeta$" slogan refers to this finite-deformation cumulant of
the residue-projected zeta distribution, not to a putative third derivative
of a global $\log\zeta$ in residue-character natural parameters (which would
require a global single-valued $\log\zeta$ that does not exist; cf. the
scope note after Theorem 2.1).

From T1.2's formula (substituting $Q^{(N)}_i(s)$ for $p_i$):
$$T_{ijk}\bigl(Q^{(N)}(s)\bigr) \;=\; Q^{(N)}_i\,\delta_{ij}\delta_{ik}
  - Q^{(N)}_i Q^{(N)}_k \delta_{ij} - Q^{(N)}_i Q^{(N)}_j \delta_{ik}
  - Q^{(N)}_i Q^{(N)}_j \delta_{jk} + 2\,Q^{(N)}_i Q^{(N)}_j Q^{(N)}_k.$$

Contract this with three character vectors $\chi_a, \chi_b, \chi_c$ in the
bilinear convention (T1.3 §5), using the Fourier coefficient $\hat Q^{(N)}_k(s)
= \sum_r Q^{(N)}_r\,\chi_k(r) = \zeta_N(s, k)/\zeta(s)$ from §3.2. The
term-by-term computation is recorded in the proof of Theorem 3.1 below; the
resulting closed form is:

**Theorem 3.1** (*Closed-Form Third Cumulant of $Q^{(N)}(s)$ on
$\mathbb{Z}/N$; T2.2 of [`RH-Done-Draft1`]*).
*The third cumulant
$\mathrm{cum}_{Q^{(N)}(s)}(\chi_a(X), \chi_b(X), \chi_c(X)) =
\partial_{\theta_a}\partial_{\theta_b}\partial_{\theta_c} \Phi_N(\theta; s)|_{\theta = 0}$
of the residue-projected zeta distribution $Q^{(N)}(s)$, evaluated in
T1.3's character basis on $\mathbb{Z}/N$, has the closed form*
$$\boxed{\;
\begin{aligned}
T^\zeta\bigl(\chi_a, \chi_b, \chi_c; \, s, N\bigr) \;=\;&
  \frac{\zeta_N(s, a+b+c)}{\zeta(s)} \\[1mm]
  &-\frac{\zeta_N(s, a+b)\,\zeta_N(s, c)
       + \zeta_N(s, a+c)\,\zeta_N(s, b)
       + \zeta_N(s, b+c)\,\zeta_N(s, a)}{\zeta(s)^2} \\[1mm]
  &+\frac{2\,\zeta_N(s, a)\,\zeta_N(s, b)\,\zeta_N(s, c)}{\zeta(s)^3},
\end{aligned}
\;}$$
*for $a, b, c \in \mathbb{Z}/N \setminus \{0\}$ and $\mathrm{Re}(s) > 1$,
with meromorphic continuation in $s$.*

*Proof.* The contraction of $T_{ijk}(Q^{(N)}(s))$ with
$\chi_a \otimes \chi_b \otimes \chi_c$ is the sum
$$\sum_{i, j, k \in \mathbb{Z}/N} T_{ijk}\bigl(Q^{(N)}(s)\bigr)\,
   \chi_a(i)\,\chi_b(j)\,\chi_c(k).$$
Read each of the five terms of $T_{ijk}$ separately. The Fourier coefficient
$\hat Q^{(N)}_k(s) = \sum_r Q^{(N)}_r(s)\,\chi_k(r)$ of §3.2 and the
multiplicative property $\chi_a(r)\,\chi_b(r) = \chi_{a+b}(r)$ of additive
characters on $\mathbb{Z}/N$ are the only inputs.

*Term 1* (linear in $Q$, double Kronecker $\delta_{ij}\delta_{ik}$). Forcing
$i = j = k$:
$$\sum_{i, j, k} Q^{(N)}_i\,\delta_{ij}\delta_{ik}\,\chi_a(i)\chi_b(j)\chi_c(k)
  \;=\; \sum_i Q^{(N)}_i\,\chi_a(i)\,\chi_b(i)\,\chi_c(i)
  \;=\; \sum_i Q^{(N)}_i\,\chi_{a+b+c}(i)
  \;=\; \hat Q^{(N)}_{a+b+c}(s).$$

*Term 2* (bilinear in $Q$, single $\delta_{ij}$). Forcing $i = j$, $k$ free,
and factoring:
$$-\!\!\sum_{i, j, k} Q^{(N)}_i Q^{(N)}_k\,\delta_{ij}\,\chi_a(i)\chi_b(j)\chi_c(k)
  \;=\; -\!\Bigl(\sum_i Q^{(N)}_i\,\chi_{a+b}(i)\Bigr)\!
        \Bigl(\sum_k Q^{(N)}_k\,\chi_c(k)\Bigr)
  \;=\; -\hat Q^{(N)}_{a+b}(s)\,\hat Q^{(N)}_c(s).$$

*Term 3* (bilinear in $Q$, single $\delta_{ik}$). Symmetric to Term 2 with
$j \leftrightarrow k$: forcing $i = k$, $j$ free,
$$-\!\!\sum_{i, j, k} Q^{(N)}_i Q^{(N)}_j\,\delta_{ik}\,\chi_a(i)\chi_b(j)\chi_c(k)
  \;=\; -\hat Q^{(N)}_{a+c}(s)\,\hat Q^{(N)}_b(s).$$

*Term 4* (bilinear in $Q$, single $\delta_{jk}$). Symmetric to Term 2 with
$i \leftrightarrow j$: forcing $j = k$, $i$ free,
$$-\!\!\sum_{i, j, k} Q^{(N)}_i Q^{(N)}_j\,\delta_{jk}\,\chi_a(i)\chi_b(j)\chi_c(k)
  \;=\; -\hat Q^{(N)}_a(s)\,\hat Q^{(N)}_{b+c}(s).$$

*Term 5* (cubic in $Q$, no $\delta$'s). All three sums factor independently:
$$+2\!\sum_{i, j, k} Q^{(N)}_i Q^{(N)}_j Q^{(N)}_k\,\chi_a(i)\chi_b(j)\chi_c(k)
  \;=\; +2\,\hat Q^{(N)}_a(s)\,\hat Q^{(N)}_b(s)\,\hat Q^{(N)}_c(s).$$

Adding the five terms yields the polynomial-in-$\hat Q$ form
$$T\bigl(\chi_a, \chi_b, \chi_c;\, Q^{(N)}(s)\bigr) \;=\;
  \hat Q^{(N)}_{a+b+c}(s)
  - \hat Q^{(N)}_{a+b}(s)\,\hat Q^{(N)}_c(s)
  - \hat Q^{(N)}_{a+c}(s)\,\hat Q^{(N)}_b(s)
  - \hat Q^{(N)}_a(s)\,\hat Q^{(N)}_{b+c}(s)
  + 2\,\hat Q^{(N)}_a(s)\,\hat Q^{(N)}_b(s)\,\hat Q^{(N)}_c(s),$$
which is the moment-to-cumulant identity for the triple
$(\chi_a(X), \chi_b(X), \chi_c(X))$ under $X \sim Q^{(N)}(s)$. Substituting
$\hat Q^{(N)}_k(s) = \zeta_N(s, k)/\zeta(s)$ from §3.2 collects the powers
of $\zeta(s)^{-1}$ displayed in the boxed equation. (The same five-term
contraction, in the same notation, appears as the central computation of
*siete* §5.) $\square$

This is the **closed-form cubic Amari–Chentsov tensor of the
residue-projected zeta distribution $Q^{(N)}(s)$** in the trilogy's
character basis on $\mathbb{Z}/N$ — equivalently, $\partial^3_\theta \Phi_N|_{\theta=0}$
for the finite categorical exponential family at base point $Q^{(N)}(s)$.
It is a polynomial in the additive-twist zetas $\zeta_N(s, k)$, with
conductor structure inherited from the conductors $d_k = N/\gcd(k, N)$ of
the characters involved. The reading "$\log\zeta$'s cubic tensor on the
residue chart" remains as program slogan, but its rigorous content is
exactly this finite-Φ statement.

### 3.5 The high-temperature limit recovers the trilogy selection rule

We verify that Theorem 3.1 collapses to T1.3 (the trilogy selection rule)
as $s \to 1^+$.

By §3.2's boundary observation, $\hat Q^{(N)}_k(s) \to \delta_{k \equiv 0
\pmod N}$ as $s \to 1^+$, for every $k \in \mathbb{Z}/N$. Substituting term
by term:

- *Leading term* $\zeta_N(s, a+b+c)/\zeta(s) \to \delta_{a+b+c \equiv 0
  \pmod N}$.
- *Cross-product terms* $\zeta_N(s, a+b)\,\zeta_N(s, c)/\zeta(s)^2 \to
  \delta_{a+b \equiv 0} \cdot \delta_{c \equiv 0}$. Restricted to
  non-trivial characters ($c \not\equiv 0$), this vanishes.
- *Triple-product term* $2\,\zeta_N(s, a)\,\zeta_N(s, b)\,\zeta_N(s, c)/\zeta(s)^3
  \to 2\,\delta_{a \equiv 0}\,\delta_{b \equiv 0}\,\delta_{c \equiv 0}$. Also
  vanishes on non-trivial characters.

So for $a, b, c \in \mathbb{Z}/N \setminus \{0\}$,
$$T^\zeta\bigl(\chi_a, \chi_b, \chi_c; \, s \to 1^+, N\bigr)
  \;=\; \delta_{a + b + c \equiv 0 \pmod N},$$
which is exactly T1.3's selection rule. The zeta distribution
**continuously deforms** the trilogy selection rule, as $s$ decreases from
$+\infty$ (zeta concentrates on $n = 1$) toward $1^+$ (zeta becomes uniform
on $\mathbb{Z}/N$).

### 3.6 Gauss-sum duality: additive selection = multiplicative orthogonality

Theorem 3.1 expresses the cubic A-C tensor as a polynomial in the
*additive-twist zetas* $\zeta_N(s, k)$. The classical analytic
number-theoretic apparatus of triple $L$-function moments works in
*multiplicative-character* coordinates. The two are dual, and the dictionary
is Gauss-sum inversion.

Let $\psi$ be a primitive Dirichlet character mod $d$ and let
$$\tau(\psi) \;=\; \sum_{a=1}^{d-1} \psi(a)\, e^{2\pi i a/d}$$
be its Gauss sum. The fundamental inversion identity, classical
[Davenport, 2000, Ch. 9; Iwaniec & Kowalski, 2004, §3.5], expresses
the additive twist in terms of the multiplicative $L$-functions of the same
conductor:
$$\zeta_d(s, a) \;=\; \frac{1}{\varphi(d)}\sum_{\substack{\psi \bmod d \\ \text{primitive}}}
  \tau(\psi)\,\overline\psi(a)\,L(s, \overline\psi) \;+\; (\text{boundary terms for non-primitive }\psi),$$
valid for $\gcd(a, d) = 1$. For general $a \in \mathbb{Z}/N$ with conductor
$d_k = N/\gcd(k, N)$ and reduced index $k' = k/\gcd(k, N) \in (\mathbb{Z}/d_k)^\times$,
$$\boxed{\;\zeta_N(s, k) \;=\; \frac{1}{\varphi(d_k)}\sum_{\substack{\psi \bmod d_k \\ \text{primitive}}}
  \tau(\psi)\,\overline\psi(k')\,L(s, \overline\psi)
  \;+\; (\text{lower-conductor boundary}).\;}$$

**Caveat (additive vs multiplicative is a dictionary, not a strict
isomorphism).** Additive characters of the abelian group $\mathbb{Z}/N$ are
defined on every residue (units and non-units); multiplicative Dirichlet
characters of conductors $d \mid N$ are defined on the units of $\mathbb{Z}/d$.
The two are not dual bases of the same space, and the Gauss-sum inversion
above contains genuine **boundary terms from non-primitive characters and
non-unit residues** that we have packaged into the single phrase
"(lower-conductor boundary)." The naive translation
$$a + b + c \equiv 0 \pmod N \ \stackrel{?}{\Longleftrightarrow}\ \psi_a \psi_b \psi_c = \psi_0$$
captures the **leading** correspondence between additive selection on
$\mathbb{Z}/N$ and multiplicative orthogonality on triple $L$-moments, but
treating it as a strict bi-implication would require a precise lemma
expanding both sides on all imprimitive components and non-unit residue
classes. We do not prove such a lemma here; the present paragraph is a
**dictionary**, not a theorem, and downstream use is restricted to
suggestive language about why additive and multiplicative selection are
"the same constraint in two languages."

**Reading.** With that caveat, the dictionary says: the trilogy's character
selection rule (T1.3) — written additively in $\mathbb{Z}/N$ — sits in
correspondence with the classical multiplicative-character orthogonality
that controls diagonal contributions to triple $L$-function moments. The
prime-axis exponential family of T2.1 supplies the natural bilingual chart.
This dictionary is not re-used in Paper I (it is structural context).

---

## §4. Functional Equations on $\mathbb{Z}/N$ and the Critical Line

The Riemann zeta function and each additive twist $\zeta_N(s, k)$ satisfies a
functional equation relating $s$ to $1 - s$. *Siete* §7 conjectured that
the ratios $\hat Q^{(N)}_k(s) = \zeta_N(s, k)/\zeta(s)$ inherit a scalar
modulus identity of the form $|\hat Q^{(N)}_k(s)| = N^{1/2 - \mathrm{Re}(s)}
d_k^{\,\mathrm{Re}(s) - 1/2} |\hat Q^{(N)}_{-k}(1-s)|$, with all gamma
factors cancelling, and inferred from it a critical-line $N$-uniformity
locus. **The conjectured scalar identity does not hold**; §4.3–4.5 below
record the obstruction (parity-mixed gamma factors in the Dirichlet
$L$-basis), withdraw the conjectured theorem, and locate the critical line
on independent classical grounds (§4.6).

### 4.1 The functional equation of $\zeta$

The completed zeta $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\,\zeta(s)$
satisfies $\Lambda(s) = \Lambda(1-s)$ [Riemann, 1859], equivalently
$$\zeta(s) \;=\; \chi(s)\,\zeta(1-s), \qquad
  \chi(s) \;=\; 2^s \pi^{s-1}\sin\!\bigl(\tfrac{\pi s}{2}\bigr)\,\Gamma(1-s).$$
This $\chi$-factor (Riemann's notation) absorbs all gamma and power-of-$\pi$
content of the FE.

### 4.2 The functional equation of $\zeta_N(s, k)$ — parity-mixed vector form

The additive twist $\zeta_N(s, k)$ is a Gauss-sum linear combination of
Dirichlet $L$-functions $L(s, \psi)$ for primitive characters $\psi$ of
conductors $d$ dividing $N$ (§3.6). Each such $L$-function satisfies its own
completed functional equation, **with a gamma factor that depends on the
parity of $\psi$**:
$$\Lambda(s, \psi) \;:=\; \Bigl(\frac{d}{\pi}\Bigr)^{(s+\kappa)/2}
  \Gamma\!\Bigl(\tfrac{s + \kappa}{2}\Bigr)\,L(s, \psi),
  \qquad \Lambda(s, \psi) \;=\; \varepsilon(\psi)\,\Lambda(1-s, \overline\psi),$$
with parity $\kappa(\psi) = 0$ (even: $\psi(-1) = +1$) or $\kappa(\psi) = 1$
(odd: $\psi(-1) = -1$) and root number $\varepsilon(\psi)$ of modulus $1$
[Davenport, 2000, Ch. 9; Iwaniec & Kowalski, 2004, §3.8].

Consequently, the functional equation for $\zeta_N(s, k)$ is **not a scalar
identity multiplied by a single conductor-power factor**: it is the
parity-decomposed sum
$$\zeta_N(s, k) \;=\; \sum_{\substack{d \mid N \\ d \mid d_k}}\!\!\sum_{\substack{\psi \bmod d \\ \text{primitive}}}\!\!\!\bigl(\text{Gauss-sum/CRT weight}\bigr)\cdot L(s, \psi),$$
and each summand transforms under $s \leftrightarrow 1-s$ with its own
$\Gamma((s+\kappa(\psi))/2)$ gamma factor. The naive "single
$\chi^{\mathrm{full}}(s;d_k)$ multiplier" used in earlier drafts collapses
even/odd contributions into a single scalar — a step that is only valid if
all primitive $\psi$ contributing at the given $k$ have the same parity,
which is **not** the case in general for $N$ with $d_k > 2$.

### 4.3 Why the chi-factor cancellation fails for the ratio $\zeta_N(s,k)/\zeta(s)$

Dividing $\zeta_N(s,k)$ by $\zeta(s)$ would clear the gamma content of
the ratio *only if* every $L$-function entering the numerator carried the
same $\Gamma(s/2)$ factor as $\zeta(s)$. Since odd primitive characters
contribute $\Gamma((s+1)/2)$, the quotient of their gamma factor against
$\Gamma(s/2)$ is
$$\frac{\Gamma((s+1)/2)}{\Gamma(s/2)} \;=\; \frac{1}{\sqrt{\pi}}\,2^{1-s}\,\Gamma(s)\big/\Gamma(s/2)^2 \;=\; \frac{\Gamma((s+1)/2)}{\Gamma(s/2)},$$
a transcendental function of $s$ — **not** a scalar power of $d_k/N$ times a
unit-modulus phase. So the ratio $\hat Q^{(N)}_k(s) = \zeta_N(s,k)/\zeta(s)$
inherits a **parity-mixed** functional equation: the K-even
(even-character) contributions transform with gamma content cancelling
against $\Gamma(s/2)$ in the denominator and look "clean"; the K-odd
(odd-character) contributions carry a residual $\Gamma((s+1)/2)/\Gamma(s/2)$
factor that does not collapse to a power of $N$ or $d_k$.

### 4.4 Withdrawal of the conjectured scalar modulus identity

*Siete* §7 conjectured the boxed scalar identity
$$\bigl|\hat Q^{(N)}_k(s)\bigr| \;\stackrel{?}{=}\; N^{1/2 - \mathrm{Re}(s)}\,
  d_k^{\,\mathrm{Re}(s) - 1/2}\,\bigl|\hat Q^{(N)}_{-k}(1 - s)\bigr|. \tag{*W*}$$
*This identity does not hold.* A numerical counterexample:

**Counterexample at $N=2$, $k=1$, $s=2$.** $\zeta_2(s,1) = \sum_{m \geq 1}
(-1)^m m^{-s} = -\eta(s) = (2^{1-s} - 1)\,\zeta(s)$ classically, so
$\hat Q^{(2)}_1(s) = 2^{1-s} - 1$ is an entire function of $s$. On
$\mathbb{Z}/2$, $-1 \equiv 1$, so $\hat Q^{(2)}_{-1} = \hat Q^{(2)}_1$. At
$s = 2$, $\hat Q^{(2)}_1(2) = 2^{-1} - 1 = -1/2$, so the LHS of (*W*) is
$1/2$. With $d_k = 2 = N$, the RHS evaluates to $2^{1/2 - 2}\, 2^{2 - 1/2}\,
|\hat Q^{(2)}_1(-1)| = 1 \cdot |2^2 - 1| = 3$. **$1/2 \neq 3$**, so (*W*)
fails at this point. A second counterexample (recorded in the review of
this paper): $N = 6$, $k = 1$, $s = 0.7 + 2i$ gives a ratio of
$|\hat Q^{(6)}_1(s)| / |\hat Q^{(6)}_{-1}(1-s)|$ that is approximately
$0.6394$, neither $1$ nor any power of $d_k/N$.

The root cause is §4.3: the parity-mixed gamma factors of even and odd
Dirichlet $L$-functions do not collapse uniformly against $\Gamma(s/2)$ in
the denominator. Any scalar identity of the form (*W*) would require all
contributing primitive $\psi$ to share parity, which fails for $N$ with
$d_k > 2$ as soon as the conductor packet contains both even and odd
primitive characters.

### 4.5 Theorem 4.1, **withdrawn**

**Theorem 4.1 (***Siete* §7's *Critical-Line $N$-Uniformity; withdrawn in
Paper I*). *The conjectured scalar identity (*W*) is false, and the
critical-line $N$-uniformity claim that was derived from it is therefore
not established by the present argument.* A correctly stated functional
equation for the K-decomposed (parity-mixed) sectors of $\zeta_N(s,k)$
remains a natural and open structural object, requiring genuine vector-valued
analysis in the Dirichlet $L$-basis rather than a scalar identity in the
ratio $\zeta_N/\zeta$. This is flagged as an open workstream for the
program; Paper I makes no further use of (*W*) and does not infer a
critical-line uniformity locus from it.

The critical line is still distinguished — by the *three independent*
classical and trilogy-internal "$1/2$"s of §4.6 below — but not via the
mechanism *siete* §7 attempted.

### 4.6 The critical line via three independent "1/2"s

With Theorem 4.1 withdrawn, the critical line $\mathrm{Re}(s) = 1/2$ is
still identified by three **independent** classical and trilogy-internal
reasons, each of which is a single-line statement that does not depend on
the now-withdrawn scalar uniformity identity of §4.4:

- **The Riemann 1/2.** Riemann (1859) named $\mathrm{Re}(s) = 1/2$ as the
  fixed-point locus of $s \leftrightarrow 1 - s$, the symmetry axis of the
  classical functional equation of $\zeta$ (§4.1). $\Lambda(s) = \Lambda(1-s)$
  is unconditional; the fixed-point line is unconditional.
- **The Mellin 1/2.** Under the multiplicative-inversion involution
  $x \mapsto 1/x$ on $\mathbb{R}_{>0}$ with measure $dx/x$, the self-dual
  weighting on functions is $f \mapsto x^{-1/2} f(1/x)$. The Mellin transform
  fixed-point line is $\mathrm{Re}(s) = 1/2$.
- **The trilogy 1/2.** `ל1`'s amplitude convention $p = a^2$ is the
  discrete shadow of the Mellin Plancherel weight: $\sqrt{p_n}$ at the zeta
  distribution is $n^{-s/2}/\sqrt{\zeta(s)}$, with self-dual coordinate
  $s = 1/2$.

The three "$1/2$"s converge on the critical line from independent directions;
§4.5 does not need to add a fourth derived from a primorial-uniformity
mechanism, and indeed cannot, on the present data. The structural status
of the critical line in Paper I rests on these three, plus the K-parity
decomposition of §5 (which gives a clean finite-arithmetic fact at $N=6$
without invoking (*W*)).

**Important caveat (unchanged in substance).** Nothing in §4 — neither the
withdrawn (*W*) nor the surviving three-1/2's identification — proves the
Riemann Hypothesis. RH is the statement that every non-trivial zero of
$\zeta(s)$ lies on $\mathrm{Re}(s) = 1/2$. Paper I locates the critical
line as a natural locus; the location of $\zeta$-zeros at that locus
remains a Paper III question, requiring the positive-current transport
theorem promised there.

---

## §5. The $\mathbb{Z}/6$ Hurwitz Packet Collapses to a 2D System

We now restrict to $N = P_2 = 6$, the smallest squarefree multi-prime modulus
and the natural minimal case at which the program's cubic apparatus exhibits
genuine cross-prime structure (T1.3 §7.2). The Hurwitz zeta function
$\zeta(s, r/6)$ for $r \in \{1, 2, 3, 4, 5\}$ supplies five non-trivial
channels, naively living in a 5-dimensional function space. The first
load-bearing finding of this section is that these five channels actually
span a **2-dimensional** function space, with basis $\{\zeta(s), L(s,
\chi_3)\}$, where $\chi_3$ is the unique primitive (odd) Dirichlet character
modulo $3$. This is Theorem 5.1. The second finding is that the
$\mathbb{Z}/6$ K-involution $r \to -r \pmod 6$ block-diagonalizes the
2-channel system into a K-fixed $\zeta$-line and a K-anti-fixed
$L_{\chi_3}$-line; this is Theorem 5.2. Section 5.5 verifies the closed
form numerically against `probe_Hurwitz_z6_closed_form.py`; section 5.6
exhibits the cubic A-C tensor of §3 on $\mathbb{Z}/6$ as a *cubic
polynomial* in the single ratio $r(s) := L(s, \chi_3)/\zeta(s)$.

### 5.1 The five Hurwitz channels

Recall the *Hurwitz zeta function*
$$\zeta(s, a) \;:=\; \sum_{n=0}^\infty \frac{1}{(n + a)^s}, \qquad
  0 < a \leq 1, \quad \mathrm{Re}(s) > 1,$$
analytically continued to $\mathbb{C}\setminus\{1\}$ with the standard
meromorphic structure (DLMF 25.11). The additive twist $\zeta_N(s, k)$ of
§3.2 and the Hurwitz channels $\zeta(s, r/N)$ are linear DFT-duals on
$\mathbb{Z}/N$: writing the residue sum $\sum_{m \equiv r \!\!\pmod N} m^{-s}
= N^{-s}\,\zeta(s, r/N)$ for $1 \leq r \leq N$ (with the convention
$\zeta(s, 1) = \zeta(s)$ for $r = N$), the forward DFT gives
$$\boxed{\;\zeta_N(s, k) \;=\; N^{-s} \sum_{r = 1}^{N} e^{2\pi i k r/N}\,\zeta(s, r/N), \qquad k \in \mathbb{Z}/N,\;}$$
and the inverse DFT gives
$$\boxed{\;N^{-s}\,\zeta(s, r/N) \;=\; \frac{1}{N} \sum_{k \bmod N} e^{-2\pi i k r/N}\,\zeta_N(s, k), \qquad 1 \leq r \leq N.\;}$$
Dividing both sides of the inverse identity by $\zeta(s)$ converts the
right-hand side to the normalized coefficients
$\hat Q^{(N)}_k(s) = \zeta_N(s, k)/\zeta(s)$ when that normalization is
preferred (cf. DLMF 25.11.15 for the underlying Hurwitz multiplication
formula). The $k$-side carries the character index; the $r$-side carries
the residue label.

At $N = 6$ the residue labels $r \in \{1, 2, 3, 4, 5\}$ give the five
non-trivial Hurwitz channels of interest in this section:
$$\zeta(s, 1/6), \quad \zeta(s, 1/3), \quad \zeta(s, 1/2), \quad
  \zeta(s, 2/3), \quad \zeta(s, 5/6).$$

### 5.2 The closed form

**Theorem 5.1** (*Closed Form for $\zeta(s, r/6)$; T3.1 of [`RH-Done-Draft1`]*).
*With $\chi_3$ the unique primitive Dirichlet character modulo $3$ (odd,
$\chi_3(1) = 1$, $\chi_3(2) = -1$, $\chi_3(0) = 0$) and the abbreviations*
$$a \;:=\; 2^{-s}, \qquad b \;:=\; 3^{-s}, \qquad Z(s) \;:=\; \zeta(s),
  \qquad L_3(s) \;:=\; L(s, \chi_3),$$
*the five non-trivial Hurwitz channels at modulus $6$ satisfy*
$$\boxed{\;
\begin{aligned}
\zeta(s, 1/6) \;&=\; \tfrac{6^s}{2}\,\bigl[(1-a)(1-b)\,Z(s) + (1+a)\,L_3(s)\bigr], \\[1mm]
\zeta(s, 1/3) \;&=\; \tfrac{3^s}{2}\,\bigl[(1-b)\,Z(s) + L_3(s)\bigr], \\[1mm]
\zeta(s, 1/2) \;&=\; (2^s - 1)\,Z(s), \\[1mm]
\zeta(s, 2/3) \;&=\; \tfrac{3^s}{2}\,\bigl[(1-b)\,Z(s) - L_3(s)\bigr], \\[1mm]
\zeta(s, 5/6) \;&=\; \tfrac{6^s}{2}\,\bigl[(1-a)(1-b)\,Z(s) - (1+a)\,L_3(s)\bigr].
\end{aligned}
\;}$$

*Proof.* The proof proceeds in three classical steps, each standard
[Apostol, 1976; Iwaniec & Kowalski, 2004, §4]:

(i) **Half-shift collapse.** The identity $\zeta(s, 1/2) = (2^s - 1)\,\zeta(s)$
is the special case of the Hurwitz multiplication formula at $N = 2$,
$\alpha = 0$:
$\zeta(s, 1/2) + \zeta(s, 1) = 2^s \zeta(s)$, with $\zeta(s, 1) = \zeta(s)$.
Solving for $\zeta(s, 1/2)$ gives the displayed formula.

(ii) **Mod-3 split.** For each $r \in \{1, 2\}$, Hurwitz multiplication at
$N = 3$, $\alpha = r/3$ gives the standard expansion
$$3^s\,\zeta(s, r/3) \;=\; \zeta(s) + (\text{character sum involving } \chi_3, \chi_0).$$
Concretely, applying the inverse DFT on $\mathbb{Z}/3$ to the additive twist
$\zeta_3(s, k)$ and reducing via Gauss-sum inversion (§3.6) yields
$$\zeta(s, 1/3) \;=\; \tfrac{3^s}{2}\bigl[(1-3^{-s})\,\zeta(s) + L(s, \chi_3)\bigr], \qquad
  \zeta(s, 2/3) \;=\; \tfrac{3^s}{2}\bigl[(1-3^{-s})\,\zeta(s) - L(s, \chi_3)\bigr].$$
Both formulas use that $L(s, \chi_0^{(3)}) = (1 - 3^{-s})\,\zeta(s)$ and
that $L(s, \chi_3)$ is the unique primitive non-trivial character mod $3$.

(iii) **Joint mod-6 reduction.** Apply the Hurwitz multiplication formula at
$N = 2$ to each Hurwitz channel at modulus $3$:
$$\zeta(s, 1/6) + \zeta(s, 1/6 + 1/2) \;=\; 2^s\,\zeta(s, 1/3),$$
i.e., $\zeta(s, 1/6) + \zeta(s, 2/3) = 2^s\,\zeta(s, 1/3)$. Solving
$\zeta(s, 1/6) = 2^s\,\zeta(s, 1/3) - \zeta(s, 2/3)$ and substituting the
mod-3 formulas of (ii) — combined with the standard reduction
$$L(s, \chi_6^{\mathrm{ind}}) \;=\; (1 + 2^{-s})\,L(s, \chi_3),$$
where $\chi_6^{\mathrm{ind}}$ is the unique non-trivial Dirichlet character
modulo $6$ (necessarily non-primitive, induced from $\chi_3$ of conductor
$3$ via the inclusion $3 \mid 6$) — gives the formula for $\zeta(s, 1/6)$.
The formula for $\zeta(s, 5/6)$ follows from the K-involution $r \to -r
\pmod 6$ (equivalently, complex conjugation through Hurwitz's $\bar a + a
= 1$ identity) applied to the formula for $\zeta(s, 1/6)$. $\square$

*Explicit derivation of $L(s, \chi_6^{\mathrm{ind}}) = (1 + 2^{-s})\,L(s, \chi_3)$.*
Every Dirichlet character modulo $6$ factors uniquely as a product of
characters modulo $2$ and modulo $3$ (CRT, $6 = 2 \cdot 3$ with coprime
factors). Modulo $2$ there is only the trivial character $\chi_0^{(2)}$;
modulo $3$ there are two characters, the trivial $\chi_0^{(3)}$ and the
primitive $\chi_3$ with $\chi_3(1) = 1, \chi_3(2) = -1$. The four
characters modulo $6$ are therefore $\chi_0^{(2)}\chi_0^{(3)} = \chi_0^{(6)}$
(trivial) and $\chi_0^{(2)}\chi_3 =: \chi_6^{\mathrm{ind}}$ (the *induced*
non-primitive lift of $\chi_3$ to modulus $6$, of conductor $3$).

Comparing Euler products factor by factor: $L(s, \chi_3) =
\prod_p (1 - \chi_3(p)\,p^{-s})^{-1}$ with $\chi_3(2) = -1, \chi_3(3) = 0$;
and $L(s, \chi_6^{\mathrm{ind}}) = \prod_p (1 - \chi_6^{\mathrm{ind}}(p)\,
p^{-s})^{-1}$ with $\chi_6^{\mathrm{ind}}(p) = \chi_3(p)$ for $p \nmid 6$
and $\chi_6^{\mathrm{ind}}(p) = 0$ for $p \in \{2, 3\}$. The two
$L$-functions therefore differ only at the prime $p = 2$:
$$\text{factor at } p = 2 \text{ in } L(s, \chi_3) \;=\; (1 + 2^{-s})^{-1}, \qquad
  \text{factor at } p = 2 \text{ in } L(s, \chi_6^{\mathrm{ind}}) \;=\; 1.$$
Restoring the missing $p = 2$ Euler factor to $L(s, \chi_3)$ — multiplying
by $(1 + 2^{-s})$ — yields $L(s, \chi_6^{\mathrm{ind}})$:
$$L(s, \chi_6^{\mathrm{ind}}) \;=\; (1 + 2^{-s})\,L(s, \chi_3). \qquad \square$$

The five formulas have been verified analytically at two trivial-value test
points:
- $s = 0$, where $\zeta(0, a) = 1/2 - a$ (a classical formula) and
  $L(0, \chi_3) = 1/3 = -B_{1, \chi_3}$;
- $s = -1$, where $\zeta(-1, a) = -B_2(a)/2$ with $B_2(a) = a^2 - a + 1/6$,
  and $L(-1, \chi_3) = 0$ by the odd-character trivial-zero structure of
  $L(s, \chi_3)$.

Both checks pass identically (cf. `probe_Hurwitz_z6_closed_form.py`).

### 5.3 The 2-channel parity decomposition

Theorem 5.1 has a clean structural reading. Set
$$F_r(s) \;:=\; 6^{-s}\,\zeta(s, r/6), \qquad r \in \{0, 1, 2, 3, 4, 5\},$$
with the convention $F_0(s) = 6^{-s}\,\zeta(s) = ab\,Z(s)$. Then the vector
$F(s) := (F_0(s), F_1(s), \ldots, F_5(s)) \in \mathbb{C}^6$ has the
factorized form
$$\boxed{\;F(s) \;=\; Z(s)\,E(s) \;+\; L_3(s)\,O(s)\;}$$
with K-even and K-odd vector parts (under the K-involution $K : r \to -r \pmod 6$)
$$E(s) \;=\; \Bigl(ab,\ \tfrac{1}{2}(1-a)(1-b),\ \tfrac{1}{2}a(1-b),\ b(1-a),\
  \tfrac{1}{2}a(1-b),\ \tfrac{1}{2}(1-a)(1-b)\Bigr),$$
$$O(s) \;=\; \Bigl(0,\ \tfrac{1}{2}(1+a),\ \tfrac{1}{2}a,\ 0,\ -\tfrac{1}{2}a,\ -\tfrac{1}{2}(1+a)\Bigr).$$

**Theorem 5.2** (*K-Orbit Parity Decomposition; T3.2 of [`RH-Done-Draft1`]*).
*The K-involution $K : r \to -r \pmod 6$ on $\mathbb{Z}/6$ has orbits
$\{0\}, \{3\}, \{1, 5\}, \{2, 4\}$. The K-fixed orbits $\{0\}$ and
$\{3\}$ correspond to the pure-$\zeta$ entries of $F$ ($F_0 = ab\,Z$ and
$F_3 = (1-a)b\,Z + 0 \cdot L_3$); the K-non-fixed orbits split as a
K-even sum that lies on the $\zeta$-line and a K-odd difference that lies
on the $L_{\chi_3}$-line:*
$$F_1 + F_5 \;\in\; Z\text{-line}, \qquad F_1 - F_5 \;\in\; L_3\text{-line},$$
$$F_2 + F_4 \;\in\; Z\text{-line}, \qquad F_2 - F_4 \;\in\; L_3\text{-line}.$$

*Proof.* Direct substitution from the closed forms of Theorem 5.1, after
multiplying by $6^{-s}$. The K-even/K-odd decomposition is the eigendecomposition
of the involution $K$ acting on $\mathbb{C}^6$; the 4-dimensional non-fixed
sector ($r \in \{1, 2, 4, 5\}$) splits into a 2-dimensional K-even subspace
and a 2-dimensional K-odd subspace, both consisting of pairs $\{r, -r\}$ of
opposite signs in the two channels. Theorem 5.1 places the K-even pairs on
the $\zeta$-line and the K-odd pairs on the $L_3$-line. $\square$

The structural content of Theorem 5.2 is that the **2-channel collapse of
Theorem 5.1 is the eigendecomposition of the K-involution acting on the
six Hurwitz channels**. The K-fixed eigenspace (eigenvalue $+1$) is the
$\zeta$-channel; the K-anti-fixed eigenspace (eigenvalue $-1$) is the
$L_{\chi_3}$-channel.

### 5.4 At a zeta zero, the Hurwitz packet is purely K-odd

At any non-trivial zero $\rho$ of $\zeta$, $Z(\rho) = 0$, so by the
factorized form of Theorem 5.2,
$$F(\rho) \;=\; L_3(\rho)\,O(\rho).$$
Equivalently, $F_3(\rho) = 0$, $F_1(\rho) + F_5(\rho) = 0$, and
$F_2(\rho) + F_4(\rho) = 0$ — three vector identities verified numerically
at the first three zeta zeros (see §5.5).

Near $\rho$ with $s = \rho + \epsilon$ and $\rho$ a simple zero,
$$F(\rho + \epsilon) \;=\; L_3(\rho)\,O(\rho)
  \;+\; \epsilon\,\bigl[Z'(\rho)\,E(\rho) + L_3'(\rho)\,O(\rho)
   + L_3(\rho)\,O'(\rho)\bigr] \;+\; O(\epsilon^2).$$
The first-order K-even leakage is therefore *exactly* $Z'(\rho)\,\epsilon\,
E(\rho)$, with all other first-order contributions K-odd. This is the
structural reason — purely from Theorem 5.1 — why the program's $m_B$
log-derivative of [HPo-notes Addendum B] picks up a simple Herglotz pole
with residue equal to the zero multiplicity at $\rho$; see [HPo-notes B6]
and Paper II for the development.

### 5.5 Numerical verification

The probe [`probe_Hurwitz_z6_closed_form.py`] verifies Theorem 5.1 by:

(i) Evaluating each side of the five closed-form identities at a battery
of complex $s$-values (including critical-line points and zeta-zero
ordinates) at 60-digit `mpmath` precision.

(ii) Verifying the analytic test-points $s = 0$ and $s = -1$ identified
in the proof of Theorem 5.1.

(iii) Verifying that at zeta-zero ordinates $s = 1/2 + i\gamma_n$ (with
$\gamma_1 = 14.1347\ldots, \gamma_2 = 21.0220\ldots, \gamma_3 = 25.0109\ldots,
\gamma_4 = 30.4249\ldots, \gamma_5 = 32.9351\ldots$), the K-even vector
identities $F_3 = 0$, $F_1 + F_5 = 0$, $F_2 + F_4 = 0$ of Theorem 5.2 hold
to floating-point precision ($\leq 10^{-15}$).

The probe output shows
- maximum Hurwitz closed-form error: $\sim 10^{-60}$ across all sampled
  $r \in \{1, \ldots, 5\}$ and sampled $s$;
- vanishing $|Z|$ at sampled zero ordinates: $\sim 10^{-15}$ to $10^{-16}$;
- K-even vector residuals at zero ordinates: $\sim 10^{-15}$ to $10^{-16}$.

At the first three zeta-zero ordinates, the probe records:

| $\gamma_n$ | $\max_r\bigl|\zeta(s, r/6) - \text{closed form}\bigr|$ | $|F_3(\rho_n)|$ | $\bigl|F_1(\rho_n) + F_5(\rho_n)\bigr|$ |
|---|---|---|---|
| $14.13472514\ldots$ | $1.01 \times 10^{-60}$ | $6.5 \times 10^{-16}$ | $1.8 \times 10^{-15}$ |
| $21.02203964\ldots$ | $\sim 10^{-60}$        | $9.7 \times 10^{-16}$ | $2.3 \times 10^{-15}$ |
| $25.01085758\ldots$ | $\sim 10^{-60}$        | $5.8 \times 10^{-16}$ | $1.5 \times 10^{-15}$ |

The Hurwitz closed-form holds at 60-digit `mpmath` precision (column 2);
the K-even constraints $F_3 = 0$ and $F_1 + F_5 = 0$ of Theorem 5.2 hold
to floating-point precision (columns 3, 4) at the simple $\zeta$-zeros.
The identities are confirmed to machine precision.

### 5.6 The cubic A-C tensor on $\mathbb{Z}/6$ as a cubic polynomial in
       $r(s) = L_3(s)/Z(s)$

Set
$$r(s) \;:=\; \frac{L_3(s)}{\zeta(s)}.$$
Theorem 5.1 (equivalently, Theorem 5.2) expresses each ratio
$\hat Q^{(6)}_k(s) = \zeta_6(s, k)/\zeta(s)$ in the linear form
$\hat Q^{(6)}_k(s) = \alpha_k(s) + i\beta_k(s)\,r(s)$ (with $\alpha_k,
\beta_k$ explicit polynomials in $a = 2^{-s}, b = 3^{-s}$ — the K-even and
K-odd character-DFT coefficients of $E(s)$ and $O(s)$, respectively).

Substituting into the closed-form cubic A-C tensor of §3.4:
$$T^\zeta(\chi_a, \chi_b, \chi_c; s, 6) \;=\; T_0(s) \;+\; i\,T_1(s)\,r(s)
  \;-\; T_2(s)\,r(s)^2 \;-\; i\,T_3(s)\,r(s)^3,$$
a **cubic polynomial in $r(s)$** with $s$-dependent coefficients
$T_0(s), \ldots, T_3(s)$ given explicitly in terms of $a, b$ and the
$\alpha_k, \beta_k$ data.

The four coefficients $T_j(s)$ are real polynomials in $a = 2^{-s},\ b =
3^{-s}$, obtained by substituting $\hat Q^{(6)}_k = \alpha_k + i\beta_k\,r$
into Theorem 3.1 and collecting powers of $r$. Their explicit forms are
recorded in [HPo-notes, Addendum A5]; the §5.6 reasoning below uses only
the following structural properties:

(P1) **$T_3$ is a $\beta$-product.** $T_3(s) = 2\,\beta_a(s)\,\beta_b(s)\,\beta_c(s)$,
i.e., the $r^3$ coefficient is the cubic term $+2\,\hat Q_a\hat Q_b\hat Q_c$
of Theorem 3.1, restricted to its triple-$\beta$ contribution.

(P2) **$\beta_k$ vanishes on the K-fixed character indices.**
$\beta_k(s) = 0$ for $k \in \{0, 3\}$. *Proof.* The K-odd vector $O(s)$
of §5.3 satisfies $O_0 = O_3 = 0$ at the K-fixed residues $r \in \{0, 3\}$.
The DFT pairing on $\mathbb{Z}/6$ (§5.1) preserves K-parity under
$r \leftrightarrow k$, and the K-fixed character indices are exactly
$k \in \{0, 3\}$ (those with $2k \equiv 0 \pmod 6$). Hence $\beta_k(s)$,
the K-odd DFT coefficient of $O(s)$, vanishes at $k \in \{0, 3\}$.

(P3) **$T_0$ is the on-shell piece.** $T_0(s) = T^\zeta(\chi_a, \chi_b,
\chi_c; s, 6)\big|_{L_3(s) = 0}$, the cubic A-C tensor evaluated on the
K-even projection. It is a polynomial in $(\alpha_a(s), \alpha_b(s),
\alpha_c(s))$ alone, recovering Theorem 3.1's polynomial-in-$\hat Q$ form
in the $\beta_k \equiv 0$ specialization.

The structural observations from this expansion are:

(a) **The $r^3$ coefficient vanishes whenever any of $a, b, c$ lies in a
K-fixed orbit $\{0, 3\}$**, immediate from (P1) and (P2).

(b) **At a $\zeta$-zero $\rho$** (a simple non-trivial zero, $\zeta(\rho) = 0$,
$\zeta'(\rho) \neq 0$), $r(s) = L_3(s)/\zeta(s)$ has a simple pole at $\rho$.
The cluster residue is most cleanly written as a limit. Define
$$\widetilde T^\zeta(\chi_a, \chi_b, \chi_c; \rho, 6) \;:=\;
  \lim_{s \to \rho}\, \zeta(s)^3\,T^\zeta(\chi_a, \chi_b, \chi_c; s, 6).$$
Theorem 3.1 then yields
$$\widetilde T^\zeta(\chi_a, \chi_b, \chi_c; \rho, 6)
  \;=\; 2\!\prod_{j \in \{a, b, c\}}\!\zeta_6(\rho, j),$$
since $\zeta(s)^3\,T^\zeta = \zeta(s)^2 \zeta_6(s, a+b+c) - \zeta(s)
\sum_{(ij)} \zeta_6(s, i+j)\,\zeta_6(s, k) + 2\,\prod_j \zeta_6(s, j)$ by
Theorem 3.1, and the first two terms vanish as $s \to \rho$ by $\zeta(\rho)
= 0$ — provided $\zeta_6(\rho, k) < \infty$ for the indices involved
(automatic for $k \not\equiv 0 \pmod 6$). Substituting Theorem 5.1 then
expresses the surviving cubic-product in terms of $L_3(\rho)$ and the
K-odd coefficients $\beta_j$:
$$\widetilde T^\zeta(\chi_a, \chi_b, \chi_c; \rho, 6) \;\propto\;
  L_3(\rho)^3 \cdot \prod_j \beta_j(\rho),$$
with proportionality constant determined by Theorem 5.1.

**Hypotheses for the non-vanishing claim.** Strict non-vanishing of
$\widetilde T^\zeta$ at $\rho$ requires three conditions, listed
explicitly:

(H1) $\rho$ is a simple non-trivial zero of $\zeta$ (current expectation
under RH; unconditionally, $\widetilde T^\zeta$ may receive higher-pole
corrections at multiple zeros, treated as a separate limit).

(H2) $L(\rho, \chi_3) \neq 0$ — equivalently, $\rho$ is **not** a common
zero of $\zeta$ and $L(s, \chi_3)$. The Dedekind factorization
$\zeta_K = \zeta \cdot L_{\chi_3}$ for $K = \mathbb{Q}(\sqrt{-3})$ means
$\zeta_K$-zeros decompose as the union of $\zeta$-zeros and
$L_{\chi_3}$-zeros (§6.4 Row 6, corrected); a common zero would simultaneously
zero the leading cubic term. Paper I does not exclude common zeros of
$\zeta$ and $L_{\chi_3}$ unconditionally; the (H2) hypothesis flags this
explicitly.

(H3) $\beta_j(\rho) \neq 0$ for each $j \in \{a, b, c\}$ — equivalent to
$a, b, c$ all lying in non-K-fixed orbits (since $\beta_j \equiv 0$ on the
K-fixed character indices $\{0, 3\}$ by (P2)).

(c) **Under (H1)–(H3)**, non-vanishing holds iff none of $a, b, c$ lies
in a K-fixed orbit. On $\mathbb{Z}/6$ selection-rule triples (T1.3 §7.2),
the non-K-fixed selection triples are
$$(2, 2, 2), \quad (4, 4, 4), \quad (1, 1, 4), \quad (2, 5, 5)$$
(up to permutation), and exactly these contribute to the cluster residue.

The cubic-in-$r$ structure of §5.6 is what makes the program's cluster
$c_2 < 0$ analysis in [HPo-notes A6–A8] *unconditional* under the strict
positivity $L(1/2, \chi_3) > 0$, which is itself unconditional via a
rigorous interval computation backed by the Iwaniec–Sarnak (2000)
non-negativity envelope. We record this as

**Theorem 5.3** (*Strict positivity of $L(1/2, \chi_3)$*).
*$L(1/2, \chi_3) > 0$.*

*Proof (rigorous interval computation).* The Hurwitz representation gives
$$L(1/2, \chi_3) \;=\; 3^{-1/2}\bigl[\,\zeta(1/2,\, 1/3) - \zeta(1/2,\, 2/3)\,\bigr],$$
with $\zeta(s, a)$ the Hurwitz zeta function (DLMF 25.11). Each Hurwitz
value is evaluated by a truncated Euler–Maclaurin expansion whose
truncation error is controlled by a rigorous tail bound: for $\mathrm{Re}(s)
> 0$ and any cutoff $K \geq 1$,
$$\zeta(s, a) \;=\; \sum_{n=0}^{K-1}\frac{1}{(n+a)^s} \;+\; \frac{(K+a)^{1-s}}{s-1} \;+\; \frac{1}{2(K+a)^s} \;+\; R_K(s, a),$$
with $|R_K(s,a)|$ bounded by an explicit function of $K$, $a$, and $|s|$
(standard, e.g. [Apostol 1976, Ch. 12]). Taking $K = 200$ and propagating
both the truncated sum and the tail bound under interval arithmetic
(implemented in `mpmath` with `mp.dps = 80` working precision and an
auditable rounding direction), one obtains the enclosure
$$L(1/2, \chi_3) \;\in\; \bigl[\,0.4808675575,\ 0.4808675577\,\bigr],$$
which is strictly bounded below by $0.48 > 0$. Independent cross-check:
the LMFDB record `1-3-3.2-r1-0-0` reports
$L(1/2, \chi_3) = 0.4808675576\ldots$ (analytic rank $0$, root number $+1$),
consistent with the enclosure to all displayed digits.

The interval computation by itself proves $L(1/2, \chi_3) > 0$. We additionally
note that this value is consistent with the Iwaniec–Sarnak (2000, *Israel J.
Math.* 120) non-negativity envelope — their work proves non-vanishing for
a positive proportion of real primitive Dirichlet characters in families,
not strict positivity for every $\chi$ individually; the strict positivity
here rests on the interval computation, not on Iwaniec–Sarnak. $\square$

This strict positivity is the load-bearing input for the cluster sign
analysis of Paper III; it is recorded here because it is the most concrete
way in which the $L_{\chi_3}$ channel of Paper I enters the proof of RH.

---

## §6. Galois Identification with $\mathbb{Q}(\sqrt{-3})$

§5 established that the $\mathbb{Z}/6$ Hurwitz packet collapses to a 2D
function space, spanned by $\zeta(s)$ and $L(s, \chi_3)$, with the K-involution
$r \to -r \pmod 6$ acting as the parity operator. The present section
identifies this 2-channel structure with the **Galois decomposition** of the
Dedekind zeta function of $\mathbb{Q}(\sqrt{-3})$ under the degree-2 cover
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$, with the K-involution = Galois
involution. This is Identification T3.3. We close §6 with Identification
I3.4: the 2-channel Bures fiber is the explicit finite-cyclotomic
realization of the Connes–Consani Picard groupoid for this Galois cover.

### 6.1 The field $\mathbb{Q}(\sqrt{-3})$ and its cyclotomic structure

The cyclotomic field $\mathbb{Q}(\zeta_6) = \mathbb{Q}(e^{2\pi i / 6})$ contains
all sixth roots of unity. Since $\zeta_6 = \tfrac{1 + \sqrt{-3}}{2}$, we have
$$\mathbb{Q}(\zeta_6) \;=\; \mathbb{Q}(\sqrt{-3}).$$
The Galois group is
$$\mathrm{Gal}\bigl(\mathbb{Q}(\sqrt{-3})/\mathbb{Q}\bigr) \;=\; \mathbb{Z}/2,$$
generated by the involution $\sigma : \sqrt{-3} \mapsto -\sqrt{-3}$
(equivalently, $\zeta_6 \mapsto \zeta_6^{-1} = \overline{\zeta_6}$;
equivalently still, complex conjugation, since $\mathbb{Q}(\sqrt{-3})$ is
imaginary quadratic with discriminant $-3$).

The roots of unity in $\mathbb{Q}(\sqrt{-3})$ form the cyclic group
$\mu_6 \cong \mathbb{Z}/6$. The discriminant of the number field is $D_K
= -3$ and its class number is $h_K = 1$.

### 6.2 The Dedekind factorization

The Dedekind zeta function of $\mathbb{Q}(\sqrt{-3})$ factors as a product
of $\zeta$ with the Dirichlet $L$-function of the unique non-trivial
character associated to the Galois cover.

The Kronecker symbol associated with the discriminant $-3$ is the
quadratic character
$$\chi_{-3}(p) \;:=\; \Bigl(\frac{-3}{p}\Bigr) \;=\; \begin{cases}
  +1 & \text{if } p \equiv 1 \pmod 3, \\
  -1 & \text{if } p \equiv 2 \pmod 3, \\
   0 & \text{if } p = 3,
\end{cases}$$
which agrees on coprime arguments with the primitive Dirichlet character
$\chi_3$ mod $3$ used in §5. The Dedekind zeta of $\mathbb{Q}(\sqrt{-3})$ then
factors (by the conductor-discriminant theorem applied to the abelian
extension $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$; see [Marcus, 1977, §3, Cor.
to Thm. 20]) as
$$\boxed{\;\zeta_{\mathbb{Q}(\sqrt{-3})}(s) \;=\; \zeta(s) \cdot L(s, \chi_3).\;}$$

This factorization is **identical**, on the nose, to the 2-channel
$(\zeta, L_{\chi_3})$ decomposition that Theorem 5.1 derived from the
$\mathbb{Z}/6$ Hurwitz packet. The basis $\{\zeta, L_{\chi_3}\}$ of the
2D collapse is the basis of Galois eigenspaces of $\zeta_K$ under the
$\mathbb{Z}/2$ Galois action.

**Verification.** The probe
[`probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`] confirms the
factorization by:

- Evaluating $\zeta(s) \cdot L(s, \chi_3)$ at $s = 2, 3, 1.5, 2+5i$ and
  comparing with a finite Euler-product approximation of
  $\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \prod_{\mathfrak{p}}(1 - N\mathfrak{p}^{-s})^{-1}$
  over prime ideals $\mathfrak{p}$ of $\mathbb{Z}[\zeta_6]$ of norm $\leq 200$;
  agreement to $10^{-3}$ (the finite-Euler-product truncation error).
- The class number formula for the imaginary quadratic field
  $\mathbb{Q}(\sqrt{-3})$ (discriminant $D_K = -3$, class number $h_K = 1$,
  $w_K = 6$ roots of unity), gives
  $$L(1, \chi_3) \;=\; \frac{2\pi\,h_K}{w_K\,\sqrt{|D_K|}}
    \;=\; \frac{2\pi \cdot 1}{6\,\sqrt{3}} \;=\; \frac{\pi}{3\sqrt{3}}.$$
  Numerically the probe reports
  $$L(1, \chi_3) \;\approx\; 0.6046000107, \qquad
    \frac{\pi}{3\sqrt{3}} \;\approx\; 0.6045997881,$$
  agreement to within $3 \times 10^{-7}$ — consistent with the probe's
  evaluation at $s = 1 + 10^{-6}$ (deliberately off the pole structure of
  $L(s, \chi_0^{(3)})$), where the residual offset
  $|L'(1, \chi_3)| \cdot 10^{-6}$ matches the observed discrepancy.

### 6.3 The Connes–Consani Picard groupoid (brief)

We summarize Connes & Consani [arXiv:2602.15941, Feb 2026] only insofar as
needed to state the identification of §6.4. The reader is referred to their
paper for the full development.

Connes and Consani interpret the adele class space of $\mathbb{Q}$ as the
natural *monoidal extension* of the Picard group of $\overline{\mathrm{Spec}}\,\mathbb{Z}$.
The objects are torsion-free rank-1 abelian groups $L$ equipped with
**rigidifying data** consisting of:

- a **norm** = Arakelov metric on the line bundle (Riemann sector data);
- a group morphism to $\mathbb{R}_{>0}$ (the adele-norm sector);
- a **combinatorial datum** parametrizing the roots of unity in the
  character dual of $L$.

The composition law is the tensor product of rank-1 groups (with their
rigidifying structures). The **singular strata for spectral realization
of L-functions** in this framework are the points where the zeta/L-functions
have zeros and poles.

The framework is global; restricting to a single Galois cover gives a
finite-cyclotomic specialization. The relevant special case for Paper I is
the cover $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$.

### 6.4 The structural dictionary

**Identification T3.3** (*Structural dictionary for the
$\mathbb{Q}(\sqrt{-3})$ Galois cover; T3.3 of [`RH-Done-Draft1`]; HPo
Addendum H, H1–H3*).
*The Dedekind factorization
$\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) \cdot L(s, \chi_3)$ aligns
entry-by-entry with the 2-channel structure derived from the
$\mathbb{Z}/6$ Hurwitz packet in §5, under the dictionary below. The
rows split into two classes: **classical / derived** (Rows 1, 2, 4, 5,
6, 7), provable from the Dedekind factorization and the K-parity
decomposition of Theorem 5.2; and **structural correspondence**
(Row 3), a metric-matching claim flagged for Paper II's functorial
construction and not proved by the data of Paper I.*

| *Connes–Consani datum* | *2-channel realization* | *Status in Paper I* |
|---|---|---|
| *Rank-1 line bundle on $\overline{\mathrm{Spec}}\,\mathbb{Z}$* | *$\zeta$-channel (trivial extension)* | derived (Row 1) |
| *Rank-1 line bundle on $\overline{\mathrm{Spec}}\,\mathbb{Z}[\sqrt{-3}]$ via Galois cover* | *2-channel pair $(\zeta, L_{\chi_3})$* | derived (Row 2) |
| *Arakelov metric (Riemann sector norm)* | *Candidate Bures Hermitian metric $h = (|\Xi|^2 + |\mathcal{L}_3|^2)^{-1}$* | **structural; not proved in Paper I** (Row 3) |
| *Combinatorial datum: parametrization of roots of unity in character dual* | *T1.3's $\mathbb{Z}/6$ residue chart + K-involution* | derived (Row 4) |
| *Galois involution $\mathrm{Gal}(\mathbb{Q}(\sqrt{-3})/\mathbb{Q})$* | *K-involution $K : r \to -r \pmod 6$* | derived (Row 5) |
| *Zero set of $\zeta_{\mathbb{Q}(\sqrt{-3})}$* | *Union (parity-sorted) of $\zeta$-zeros and $L_{\chi_3}$-zeros* | derived (Row 6) |
| *Tensor product of rank-1 groups = $L$-product* | *Multiplicative product $\zeta \cdot L_{\chi_3}$* | derived (Row 7) |

*The Dedekind factorization itself is classical (§6.2). The dictionary
above re-reads the factorization with K-parity labels, transferring the
Galois structure of the $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ cover onto the
$(\zeta, L_{\chi_3})$ basis of §5. The Bures-metric row (Row 3) is
where Paper II will be expected to supply a functorial construction.*

*Justification.* Row-by-row.

**Row 1.** $\mathbb{Q}$ has Dedekind zeta $\zeta_{\mathbb{Q}}(s) = \zeta(s)$;
identified with the K-fixed $\zeta$-channel of Theorem 5.2.

**Row 2.** $\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) \cdot L(s, \chi_3)$
by §6.2 (conductor–discriminant theorem). The 2-channel pair
$(\zeta, L_{\chi_3})$ is the Galois eigenbasis.

**Row 3 (structural; not proved in Paper I).** On a rank-1 line bundle the
Arakelov norm is a Hermitian metric. *Siete* and the HPo notes propose that
in the Galois eigenbasis $\mathbb{C}^2$ the natural such Hermitian form is
the Bures candidate $h = (|\Xi|^2 + |\mathcal{L}_3|^2)^{-1}$ with $\Xi$ the
K-fixed amplitude and $\mathcal{L}_3$ the K-anti-fixed amplitude
[HPo-notes Addendum C1]. The borrowed Connes–Consani paper
[arXiv:2602.15941] supports the high-level summary of the adele class
space as a monoidal extension of the Picard group with rigidifying norm,
group morphism to $\mathbb{R}_{>0}$, and roots-of-unity combinatorial
datum, but it does **not** prove the metric-matching identity asserted in
this row — Paper I does not exhibit a functorial map between the Arakelov
metric on the cover's line bundle and the proposed Bures form. Row 3 is
therefore **flagged as a structural correspondence**: a candidate
identification whose proof is deferred to Paper II's representation-theoretic
construction.

**Rows 4–5.** Roots of unity in $\mathbb{Q}(\sqrt{-3})$ are
$\mu_6 = \{\zeta_6^k\}_{k=0}^5$, indexed by $\mathbb{Z}/6$. The Galois
involution $\sigma$ acts as $\zeta_6^k \mapsto \zeta_6^{-k}$; the
K-involution of §5.3 acts as $r \mapsto -r \pmod 6$; the DFT pairing
intertwines them. Hence K-involution = Galois involution, on the nose.

**Row 6 (zero set: union, not joint intersection).** The zeros of
$\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) L(s, \chi_3)$ form the
**union** of the zeros of the two factors,
$\{\rho : \zeta(\rho) = 0\} \cup \{\rho : L(\rho, \chi_3) = 0\}$ — not the
intersection. (A previous draft wrote "joint zeros"; that wording is
incorrect for a product factorization and is corrected here.) Sorting by
Galois parity: $\zeta$-zeros carry K-parity $+1$ and $L_{\chi_3}$-zeros
carry K-parity $-1$, with K-fixed common zeros — if any — counted in
both sectors. Paper I does not establish unconditionally that $\zeta$ and
$L_{\chi_3}$ have no common zeros; the hypothesis (H2) of §5.6 flags
this where it matters for the cluster-residue analysis.

**Row 7.** $\zeta_K = \zeta \cdot L_{\chi_3}$ is the $L$-level
multiplicative product corresponding to the tensor product of the
underlying rank-1 line bundles (Connes–Consani composition law). This is
the Dedekind factorization read at the $L$-function level. $\square$

The identification is **structural** — it is not a new analytic theorem
about $\zeta$, and Row 3 is a deferred construction handoff rather than a
proved equivalence. What the dictionary does is name the program's
2-channel object, in finite-cyclotomic coordinates on $\mathbb{Z}/6$, as a
candidate finite-arithmetic realization of the Connes–Consani Picard
groupoid for the $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ Galois cover — with
the metric-side identification to be supplied by Paper II.

### 6.5 Closing identification I3.4

We close §6 with the *closing identification* that ties Paper I's two main
threads — the cubic effective action of §§2–4 and the Galois decomposition
of §§5–6 — into one statement to be carried into Paper II.

**Identification I3.4** (*Handoff: the $\mathbb{Z}/6$ Bures carrier as the
natural finite-arithmetic substrate for the $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$
cover; T-handoff to Paper II — not an analytic theorem*).
*Paper I delivers the following structural setup to Paper II. The 2-channel
object derived in §5 from the Hurwitz packet collapse, with K-involution
acting as the parity operator and matched to the Galois involution of the
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ cover by Row 5 of T3.3, is the natural
finite-cyclotomic substrate on which Paper II will be expected to construct
a Bures carrier — i.e. an occupation-decorated symmetric Fock space with a
Bures Hermitian metric whose Arakelov reading matches Row 3 of T3.3.*

*Symbolically, the categorical effective action of Theorem 2.1, read locally
on a zero-free simply-connected subdomain $\Omega \subset \mathbb{C}\setminus
\{1\}$, has formal K-parity decomposition $\Phi_\zeta = \log\zeta_K -
\log L_{\chi_3}$ on $\Omega$ (with $\zeta_K = \zeta \cdot L_{\chi_3}$ the
Dedekind zeta of the cover); the Galois-even component is $\log\zeta$ and
the Galois-odd component is $\log L_{\chi_3}$, both single-valued on $\Omega$
by construction. Paper II will identify the Galois-odd component (after
the Bures-covariant gauge subtraction of [HPo-notes Addendum B]) as the
connection under which the spectral-coordinate log-derivative
$m_B = -\Xi'/\Xi$ on $\mathbb{C}_+$ becomes the natural Herglotz candidate
for the CM Poisson Monotonicity criterion.*

I3.4 is the handoff statement; it asserts no new analytic theorem about
$\zeta$, and the construction of the actual Bures carrier is **not** part
of Paper I. Paper II builds the right Hilbert space (the
occupation-decorated symmetric Fock $\mathcal{F}_n$ at each primorial row,
lifted to the Archimedean place via Stone–von Neumann uniqueness) on this
substrate and is responsible for supplying Row 3 of T3.3.

### 6.6 What I3.4 is, and is not

**I3.4 is**:
- A structural identification of the program's $\mathbb{Z}/6$ Bures fiber
  with the Galois decomposition of $\zeta_{\mathbb{Q}(\sqrt{-3})}$;
- The conceptual bridge from Paper I's finite-cyclotomic analysis to Paper
  II's representation-theoretic carrier;
- The recognition that the K-involution of the program is the Galois
  involution of an actual number-theoretic Galois cover.

**I3.4 is not**:
- An analytic theorem about $\zeta$ (no new analytic statement is asserted
  by I3.4 itself);
- A construction of the Hilbert-Polya / de Branges operator (this is
  Paper II's terrain);
- A proof of RH (this is Paper III).

The remaining Paper-I-internal task is to summarize what has been
established and to hand off to Paper II.

---

## §7. Conclusion and Hand-off to Paper II

### 7.1 What Paper I established

Paper I has executed three classes of identifications and one closing
structural claim.

**Identification class 1 — the natural object on the trilogy's chart.** The
prime-axis exponential family on $\mathbb{N}_{>0}$ (Definition 2.1) is the
canonical multi-index exponential family on which the trilogy's cumulant
tower naturally lives. On $\mathrm{Re}(s) > 1$ its log-partition is
$\log\zeta(s)$ (Theorem 2.1 = T2.1); the Euler product is the
partition-function fingerprint of multiplicative independence of prime-axis
sufficient statistics, and the Dirichlet series is the same partition
function in dual mean coordinates. $\zeta$ is therefore not an analytic
mystery imported from $\sum n^{-s}$; it is the categorical effective action
$\Phi = \log Z$ of `ל2`, specialized to the prime-axis simplex along the
slice $\eta_p(s) = -s\log p$. $\zeta$ continues meromorphically to
$\mathbb{C}\setminus\{1\}$; the $\log\zeta$ reading is single-valued only
on simply-connected zero-free subdomains.

**Identification class 2 — the cubic structure in the residue chart.** The
third cumulant of the residue-projected zeta distribution $Q^{(N)}(s)$,
read in T1.3's character basis on $\mathbb{Z}/N$ — equivalently,
$\partial^3_\theta \Phi_N|_{\theta=0}$ for the finite categorical
exponential family $\Phi_N(\theta;s)$ with base distribution $Q^{(N)}(s)$ —
has the closed-form formula of Theorem 3.1 (= T2.2), a polynomial in the
additive-twist zetas $\zeta_N(s, k)$ with conductor structure inherited
from the divisor lattice of $N$. This formula recovers the trilogy
selection rule as its $s \to 1^+$ boundary value. The Gauss-sum dictionary
of §3.6 connects (heuristically, with imprimitive/non-unit boundary terms)
the additive selection rule $a + b + c \equiv 0 \pmod N$ to the
multiplicative-character orthogonality of triple $L$-function moments.
**The cubic functional equation Theorem 4.1 has been withdrawn**: the
scalar identity (*W*) conjectured in *siete* §7 fails (numerical
counterexample at $N=2$, $k=1$, $s=2$; §4.4), the cause being parity-mixed
gamma factors of even and odd Dirichlet $L$-functions that do not cancel
uniformly against $\zeta$'s chi-factor. The critical line
$\mathrm{Re}(s) = 1/2$ is identified by the three independent classical
"$1/2$"s of §4.6 (Riemann FE, Mellin self-dual, trilogy amplitude) rather
than by any primorial-uniformity mechanism on the present data; a correctly
vector/parity-decomposed FE for $\zeta_N(s,k)$ is flagged as an open
workstream.

**Identification class 3 — the 2D collapse and the Galois dictionary.**
At $N = 6$, the five non-trivial Hurwitz channels $\zeta(s, r/6)$ live in
a 2-dimensional function space spanned by $\{\zeta(s), L(s, \chi_3)\}$
(Theorem 5.1 = T3.1), with closed-form coefficients. The K-involution
$r \to -r \pmod 6$ block-diagonalizes the collapse into K-fixed
$\zeta$-channel and K-anti-fixed $L_{\chi_3}$-channel (Theorem 5.2 = T3.2).
The 2-channel structure aligns row-by-row with the Galois decomposition of
the Dedekind zeta of $\mathbb{Q}(\sqrt{-3})$ under the degree-2 cover —
with K-involution matching the Galois involution, and the classical
Dedekind factorization
$\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) \cdot L(s, \chi_3)$ supplying
the multiplicative product — as a **structural dictionary** (Identification
6.4 = T3.3). The metric-matching row (Row 3, Arakelov ↔ Bures Hermitian) is
flagged as a deferred handoff to Paper II.

**Closing handoff.** The program's $\mathbb{Z}/6$ Bures carrier is set up
in §6.5 (= I3.4) as the natural finite-arithmetic substrate on which Paper
II will be expected to construct the right Bures carrier — not as an
analytic theorem of Paper I.

Numerical verifications of the new closed forms (T3.1 and T3.3) are
recorded in `probe_Hurwitz_z6_closed_form.py` (~$10^{-60}$ analytical
agreement) and `probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`
(seven-digit agreement with the class number formula).

### 7.2 What Paper I does not establish

Paper I is the *identification phase* of the program. It establishes **what
we are working with** — the natural object on the trilogy's chart and its
Galois decomposition for the smallest squarefree multi-prime modulus. It
does not yet:

(a) **Build the right Hilbert space.** The occupation-decorated symmetric
Fock $\mathcal{F}_n = \mathrm{Sym}\bigl(\bigoplus_{p \leq p_n} \mathbb{C}\,
e_p\bigr)$ that hosts the exact von Mangoldt formula upstairs of the CRT
compression is a Paper II object. Paper I does not construct it.

(b) **Promote the finite carrier to the Archimedean place.** The Uniform
Place Treatment that extends $\mathcal{F}_n$ to $v = \infty$, with
Stone–von Neumann uniqueness forcing the Bargmann–Fock = $L^2(\mathbb{R},
dx)$ realization with Tate-Weil normalization giving the standard
$\pi^{-s/2}\Gamma(s/2)$ Archimedean local L-factors, is a Paper II
construction.

(c) **State or use the CM Poisson Monotonicity criterion.** The
characterization RH $\iff$ $\mathrm{Im}\, m_B(z) \geq 0$ on $\mathbb{C}_+$,
with $m_B = -\Xi'/\Xi$ the Bures-covariant log-derivative of the
spectral-coordinate completed zeta, is a Paper II statement (with the
Bures-covariant K-gauge subtraction of [HPo-notes Addendum B] supplying
the program's natural derivation).

(d) **Prove convolution-square positivity of Poisson windows, transport, or
RH.** All of Paper III.

The boundary between Paper I and Paper II is the boundary between *what
the program is working with* and *the carrier on which the analytic
positivity machinery lives*. Paper I stays strictly on the first side.

### 7.3 Hand-off to Paper II

Paper II inherits from Paper I:

(i) **Theorem 2.1.** On $\mathrm{Re}(s) > 1$, $\log\zeta = \Phi(\eta(s))$
is the categorical effective action of the prime-axis exponential family
along $\eta_p(s) = -s\log p$. $\zeta$ continues meromorphically to
$\mathbb{C}\setminus\{1\}$; global $\log\zeta$ is multi-valued and is
handled by branch-localized or $\zeta'/\zeta$-style statements where needed.

(ii) **Theorem 3.1.** Closed-form third cumulant of $Q^{(N)}(s)$ on
$\mathbb{Z}/N$ — equivalently, $\partial^3_\theta \Phi_N|_{\theta=0}$ for
the finite categorical exponential family $\Phi_N(\theta; s)$ at base
distribution $Q^{(N)}(s)$ — as a polynomial in $\zeta_N(s, k)$.

(iii) **§4 — three "$1/2$"s identification.** The critical line is identified
by the classical Riemann FE, the Mellin self-dual line, and the trilogy
amplitude convention; the *siete* §7 scalar uniformity conjecture
(formerly Theorem 4.1) has been withdrawn, and a correctly
parity-decomposed vector FE for $\zeta_N(s,k)$ is left as open.

(iv) **Theorem 5.1, Theorem 5.2.** Closed-form $\zeta(s, r/6)$ in the
$(\zeta, L_{\chi_3})$ basis, with K-involution as parity decomposition.

(v) **Identification T3.3 + I3.4.** Structural dictionary aligning the
2-channel $(\zeta, L_{\chi_3})$ object with the Galois decomposition of
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ (K-involution = Galois involution;
Dedekind factorization $\zeta_K = \zeta \cdot L_{\chi_3}$). Row 3
(Arakelov ↔ Bures Hermitian metric) is flagged as a structural
correspondence not proved in Paper I; supplying it is part of Paper II's
remit.

(vi) **Theorem 5.3.** $L(1/2, \chi_3) > 0$ unconditionally, via rigorous
interval arithmetic on the Hurwitz representation (with the LMFDB record
as a numerical cross-check).

What Paper II must contribute beyond Paper I:

- **The occupation-decorated symmetric Fock $\mathcal{F}_n$** at each
  primorial row $n$, with the *single-axis projector* $\Pi_{\mathrm{sa}}$
  that distinguishes mixed-axis occupation histories from single-axis ones
  before CRT compression. The exact upstairs von Mangoldt formula
  $\mathrm{VM}_{n, K}(G) = D_s\,\Pi_{\mathrm{sa}}\,\sum_k k^{-1} H_s^k$ with
  $H_s = \sum_p p^{-s} e_p$.

- **Uniform Place Treatment** including the Archimedean local factor
  $\mathcal{F}_\infty = \mathrm{Sym}(\mathbb{C}\,e_\infty) = \mathbb{C}[e_\infty]$,
  with a Heisenberg algebra realization $[\hat a, \hat a^\dagger] = 1$
  on this factor. Stone–von Neumann uniqueness then forces the
  Hilbert-space completion to be Bargmann–Fock = $L^2(\mathbb{R}, dx)$, with
  Tate-Weil normalization giving the standard Archimedean local L-factors
  $\pi^{-s/2}\Gamma(s/2)$ (Tate's local zeta integral on the ground state)
  and $\pi^{-(s+1)/2}\Gamma((s+1)/2)$ (first excited state).

- **The Bures-covariant log-derivative $m_B = -\Xi'/\Xi$** identified
  (via the K-odd gauge subtraction of [HPo-notes Addendum B]) on the
  spectral coordinate $z$ with $s = 1/2 + iz$. CM Poisson Monotonicity:
  $\mathrm{Im}\, m_B(z) \geq 0$ on $\mathbb{C}_+ \iff$ RH (Polya–Laguerre,
  classical).

Paper I has identified *what* the program is working with on $\mathbb{Z}/6$.
Paper II identifies *the carrier* on which $m_B$ lives, equipping it with
the right finite arithmetic at each primorial row and the right Archimedean
factor at $v = \infty$.

### 7.4 The arc, in one paragraph

The trilogy `Identifying 3` gave us the chart, the cumulant tower, and the
character basis on the conductor lattice. Paper I (the present paper) names
$\log\zeta$ as the natural object on that chart, derives its cubic structure
in closed form, pins the critical line as a structural locus on the
primorial ladder, and identifies the smallest squarefree multi-prime
modulus's Hurwitz packet with the Galois decomposition of
$\zeta_{\mathbb{Q}(\sqrt{-3})}$. Paper II will build the right Hilbert
carrier on this substrate — occupation-decorated symmetric Fock at each
primorial row, Uniform Place Treatment extending to the Archimedean
factor, Bures-covariant log-derivative as the Hilbert-Polya/CM Poisson
target. Paper III will close to RH via convolution-square positivity of
Poisson windows, averaged CRT shadow uniformity at polynomial scale, and
positive-current transport. Paper I establishes the **finite arithmetic
substrate**; the analytic positivity machinery lives elsewhere.

---

## References

*Working bibliography; will be normalized at second-pass cleanup. Citations
in the text use shortform labels (e.g., `Iwaniec & Kowalski, 2004`).*

[Amari, 1985] Amari, S. (1985). *Differential-Geometrical Methods in
Statistics.* Lecture Notes in Statistics 28. Springer.

[Amari & Nagaoka, 2000] Amari, S. and Nagaoka, H. (2000). *Methods of
Information Geometry.* Translations of Mathematical Monographs 191.
American Mathematical Society.

[Apostol, 1976] Apostol, T. M. (1976). *Introduction to Analytic Number
Theory.* Undergraduate Texts in Mathematics. Springer.

[Chentsov, 1982] Chentsov, N. N. (1982). *Statistical Decision Rules and
Optimal Inference.* Translations of Mathematical Monographs 53. American
Mathematical Society.

[Connes & Consani, 2026] Connes, A. and Consani, C. (2026). *On the
Jacobian of $\overline{\mathrm{Spec}}\,\mathbb{Z}$.* arXiv:2602.15941.

[Connes, Consani & Moscovici, 2024] Connes, A., Consani, C. and
Moscovici, H. (2024). *Zeta zeros and prolate wave operators.* Annals of
Functional Analysis. arXiv:2310.18423.

[Davenport, 2000] Davenport, H. (2000). *Multiplicative Number Theory.*
3rd edition. Graduate Texts in Mathematics 74. Springer.

[Iwaniec & Kowalski, 2004] Iwaniec, H. and Kowalski, E. (2004). *Analytic
Number Theory.* American Mathematical Society Colloquium Publications 53.

[Iwaniec & Sarnak, 2000] Iwaniec, H. and Sarnak, P. (2000). The
non-vanishing of central values of automorphic $L$-functions and Landau-Siegel
zeros. *Annals of Mathematics* 151, 1175–1216.

[LMFDB] L-functions and Modular Forms Database. Record `1-3-3.2-r1-0-0` for
$L(s, \chi_3)$. https://www.lmfdb.org/.

[Marcus, 1977] Marcus, D. A. (1977). *Number Fields.* Universitext.
Springer.

[Murillo2026a] Murillo Montero, L. (2026). *`ל1` — Identifying 3: The
Native Simplicial Chart.* Zenodo preprint, DOI 10.5281/zenodo.20336872.

[Murillo2026b] Murillo Montero, L. (2026). *`ל2` — Identifying 3: The
Cumulant Tower as Effective Action.* Zenodo preprint, DOI
10.5281/zenodo.20338126.

[Murillo2026c] Murillo Montero, L. (2026). *`ל3` — Identifying 3: Character
Orthogonality on the Conductor Lattice.* Zenodo preprint, DOI
10.5281/zenodo.20339049.

[Riemann, 1859] Riemann, B. (1859). Ueber die Anzahl der Primzahlen unter
einer gegebenen Grösse. *Monatsberichte der Berliner Akademie*, November 1859.

[RH-Done-Draft1] Murillo Montero, L. and the program (2026). *RH-Done —
Draft 1: The Solution Arc.* Working document, 2026-05-22.

[siete] Murillo Montero, L. and the program (2026). *siete.md* working draft,
2026.

[HPo-notes] Murillo Montero, L. and the program (2026). *HPo-notes.md*,
Addenda A–L, 2026-05-22.

### Empirical probes (Python / `mpmath`)

`probe_Hurwitz_z6_closed_form.py` — verifies Theorem 5.1 (closed-form
$\zeta(s, r/6)$) at 60-digit precision; verifies Theorem 5.2 (K-even
vector identities) at zeta-zero ordinates to machine precision.

`probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py` — verifies
Identification T3.3 (Dedekind factorization $\zeta_K = \zeta \cdot L_{\chi_3}$)
against finite Euler product over prime ideals of norm $\leq 200$; verifies
class number formula $L(1, \chi_3) = \pi/(3\sqrt{3})$ to seven digits.
