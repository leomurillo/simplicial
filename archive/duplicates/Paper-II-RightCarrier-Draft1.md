<!--
Paper II — The Right Carrier.
First draft of the second of the post-trilogy RH-Done sequence.
Bridges Paper I (Identification) and Paper III (Closure).

Writing order: introduction → body → conclusion, then abstract and title last.

This file is the working manuscript. Do not commit unless asked.
-->

# Paper II — The Right Carrier:
# Occupation-Decorated Symmetric Fock, Uniform Place Treatment,
# and the Bures-Covariant Log-Derivative for $\zeta$

*First draft — 2026-05-22.*

---

## Abstract

**Situation.** Paper I [`MurilloPaperI2026`] of the post-trilogy
*RH-Done* sequence named the natural object on the trilogy's chart:
$\log\zeta$ is the categorical effective action $\Phi = \log Z$ of `ל2`
evaluated on the prime-axis exponential family, with closed-form cubic
A-C tensor on $\mathbb{Z}/N$, critical-line $N$-uniformity locus along
the primorial ladder, and 2-channel collapse $(\zeta, L_{\chi_3})$ at
$N = 6$ identified with the Galois decomposition of the Dedekind zeta
of $\mathbb{Q}(\sqrt{-3})$. Paper I supplied the finite-arithmetic
substrate; it did not yet build a Hilbert space.

**Task.** Build the right Hilbert carrier on that substrate. Identify
the finite-place occupation Fock supporting an exact upstairs von
Mangoldt formula; extend to the Archimedean place by adelic uniformity;
identify the operator-theoretic Hilbert–Polya / CM Poisson Monotonicity
target on this carrier.

**Action.** At each primorial row $n$, take the occupation-decorated
symmetric Fock
$\mathcal{F}_n = \mathrm{Sym}(\bigoplus_{p \leq p_n}\mathbb{C}\,e_p)$
with single-axis projector $\Pi_{\mathrm{sa}}$ and differentiation
operator $D_s = -\partial_s$. Compute the upstairs logarithmic
occupation series $L_{n, K}(s) = \sum_{k = 1}^K k^{-1}\,H_s^k$ with
$H_s = \sum_p p^{-s}\,e_p$. Verify that mixed-axis occupations alias to
single-axis labels under CRT compression and conclude that
$\Pi_{\mathrm{sa}}$ must act before $\pi_{\mathrm{CRT}}$. Axiomatize
**Uniform Place Treatment**: every place $v$ of $\mathbb{Q}$ carries a
local Fock $\mathcal{F}_v = \mathbb{C}[e_v]$ (UPT-structure), and the
Archimedean local Fock carries the Heisenberg algebra
$[\hat a, \hat a^\dagger] = 1$ (UPT-Heisenberg). Apply Stone–von
Neumann uniqueness and Tate–Weil normalization. Evaluate Tate local
zeta integrals at the Bargmann ground and first-excited states. Treat
the K-odd channel $L_{\chi_3}$ of Paper I as a gauge connection,
not a state, and form the covariant log-derivative of the scalar Bures
transfer.

**Result.** The occupation-decorated symmetric Fock $\mathcal{F}_n$
implements the exact identity
$D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s) = \sum_{p \leq p_n}\sum_{r = 1}^K
(\log p)\,p^{-rs}\,e_{r e_p}$ as a closed algebraic identity in
$\mathcal{F}_n$ — the upstairs Mangoldt distribution before CRT
compression (**Theorem 2.5 = T4.1**); the single-axis projector
$\Pi_{\mathrm{sa}}$ is structurally ill-defined after CRT, since
mixed-axis occupations such as $2 e_2 + 3 e_3$ at row $n = 3$ alias to
the same compressed label as the single-axis $5 e_5$
(**Identification 3.3 = I4.2**). Under UPT-structure and
UPT-Heisenberg (**Axioms A5.1, A5.2**), Stone–von Neumann uniqueness
forces the Hilbert completion of the Archimedean local Fock to be
Bargmann–Fock $\cong L^2(\mathbb{R}, dx)$ with
$\langle z^m, z^n\rangle = m!\,\delta_{m, n}$ (**Theorem 5.1 = T5.3**),
derived not assumed; Tate local zeta integrals at the Bargmann ground
state $\psi_0 \propto e^{-\pi x^2}$ and first-excited state
$\psi_1 \propto x e^{-\pi x^2}$ produce, by direct Gaussian integration,
the **standard Archimedean local $L$-factors** $Z_+(s) = \pi^{-s/2}\Gamma(s/2)$
and $Z_-(s) = \pi^{-(s + 1)/2}\Gamma((s + 1)/2)$ — derived, not imposed
(**Theorem 6.1 = T5.4**); the Hardy–Titchmarsh intertwining selects the
canonical Archimedean height measure
$dm \propto |\Gamma_\mathbb{R}(\tfrac12 + is)|^2\,ds$ and identifies the
Bargmann rotation with the Riemann–Siegel gamma multiplier plus branch
reflection (**Theorem 7.1 = T5.5**). The K-odd channel $\mathcal{L}_3$
acts as a gauge connection on the 2-channel Bures fiber of Paper I; the
covariant log-derivative $\nabla_B \log M = d\log M - d\log\mathcal{L}_3$
of the scalar transfer $M = \mathcal{L}_3/\Xi$ equals $-d\log\Xi$
identically, identifying
$$m_B(z) \;:=\; -\frac{\Xi'(z)}{\Xi(z)},\qquad \Xi(z) = \xi(\tfrac12 + iz)$$
as the Bures-covariant logarithmic derivative on the spectral coordinate
(**Definition 8.3 = D6.1, Theorem 8.4 = T6.2**). By the classical
Pólya–Laguerre characterization of the Laguerre–Pólya class, $m_B$ is
Herglotz on $\mathbb{C}_+$ if and only if all zeros of $\Xi$ are real,
i.e., the Riemann Hypothesis holds (**Theorem 9.1 = T6.3**). Three
empirical probes confirm the identifications:
$\langle z^n, z^n\rangle_B = n!$ and the Tate integrals
$Z_\pm(s)$ to machine precision; the Bures covariant identity
$d\log(\mathcal{L}_3/\Xi) - d\log\mathcal{L}_3 = -d\log\Xi$ to
$\leq 10^{-13}$; simple Herglotz pole with residue $1$ at the first
zeta-zero ordinate.

**Position.** Paper II is the carrier-construction phase of the program.
It builds the right Hilbert carrier on which Paper III's positivity
machinery will live; it does not yet prove convolution-square positivity,
averaged CRT shadow uniformity, the positive-current transport theorem,
or the main theorem on RH — these are Paper III. Paper II terminates
with a clean statement of the CM Poisson Monotonicity criterion as the
target on the carrier it has built. Paper I named what the program is
working with; Paper II builds the carrier; Paper III closes to RH.

**Keywords:** Riemann zeta function, occupation-decorated symmetric Fock,
single-axis projector, von Mangoldt formula, Uniform Place Treatment,
Stone–von Neumann uniqueness, Bargmann–Fock space, Tate local zeta
integrals, Archimedean local $L$-factor, Hardy–Titchmarsh transform,
metaplectic representation, Hilbert–Polya, Pólya–Laguerre class,
Herglotz function, Bures-covariant log-derivative, K-odd gauge,
CM Poisson Monotonicity.

---

## Introduction

Paper I [`MurilloPaperI2026`] named the natural object on the trilogy's
chart: $\log\zeta(s)$ is the categorical effective action $\Phi = \log Z$
of `ל2` evaluated on the prime-axis exponential family along the slice
$\eta_p(s) = -s\log p$. It derived the cubic Amari–Chentsov tensor of
$\log\zeta$ in closed form on $\mathbb{Z}/N$, pinned the critical line as
the unique $N$-uniformity locus along the primorial ladder, and identified
the $\mathbb{Z}/6$ Hurwitz packet's 2-dimensional collapse with the
Galois decomposition of the Dedekind zeta of $\mathbb{Q}(\sqrt{-3})$.
What Paper I delivered is the **finite arithmetic substrate** — the
object the program is working with, in finite-cyclotomic coordinates.

Paper I did not yet build a Hilbert space. It did not lift the cubic
substrate to a representation-theoretic carrier on which an explicit-formula
positivity argument could live. The trilogy gave us a chart; Paper I
named the natural function on it; the present paper builds **the right
Hilbert carrier**.

The carrier has three layers.

**Layer 1 — The finite occupation-decorated symmetric Fock.** At each
primorial row $n$, the finite carrier is the symmetric algebra
$$
\mathcal{F}_n \;=\; \mathrm{Sym}\Bigl(\bigoplus_{p \leq p_n}\mathbb{C}\,e_p\Bigr)
$$
of the prime-axis vector space, **with the single-axis projector
$\Pi_{\mathrm{sa}}$ acting *before* CRT compression**. The exact upstairs
von Mangoldt formula
$$
\mathrm{VM}_{n, K}\;=\;D_s\,\Pi_{\mathrm{sa}}\,\sum_{k=1}^K\,\frac{1}{k}\,H_s^k,
\qquad H_s\;=\;\sum_{p \leq p_n} p^{-s}\,e_p,\qquad D_s\;=\;-\partial_s,
$$
is realized in $\mathcal{F}_n$ exactly, with no analytic estimate
involved. The single-axis projector is *not* well-defined after CRT
compression — mixed occupations alias to single-axis labels modulo the
local prime orders — and the program's finite-place lock closes exactly
in $\mathcal{F}_n$ and only there.

**Layer 2 — The Archimedean factor selected by Uniform Place Treatment.**
The same local Fock structure extends to the Archimedean place $v = \infty$
as a single Archimedean local factor $\mathcal{F}_\infty
= \mathrm{Sym}(\mathbb{C}\,e_\infty) = \mathbb{C}[e_\infty]$. This is the
**Uniform Place Treatment** (UPT): every place $v$ of $\mathbb{Q}$ — finite
or Archimedean — carries a local Fock on equal structural footing. UPT
splits into two named axioms, *UPT-structure* (the extension itself) and
*UPT-Heisenberg* (the algebra realization $[\hat a, \hat a^\dagger] = 1$
at $v = \infty$). Under these, **Stone–von Neumann uniqueness forces the
Hilbert completion of $\mathcal{F}_\infty$ to be Bargmann–Fock
$\cong L^2(\mathbb{R}, dx)$** with $\langle z^m, z^n\rangle = m!\,\delta_{m,n}$.
The standard Archimedean local $L$-factors $\pi^{-s/2}\Gamma(s/2)$ and
$\pi^{-(s+1)/2}\Gamma((s+1)/2)$ emerge as **Tate local zeta integrals of
the Bargmann ground and first-excited states** — not imposed, derived.

**Layer 3 — The Bures-covariant log-derivative $m_B$.** On the spectral
coordinate $z$ with $s = 1/2 + iz$, the program's natural Hilbert–Polya
target is the Bures-covariant logarithmic derivative
$$
m_B(z)\;:=\;-\frac{\Xi'(z)}{\Xi(z)},\qquad \Xi(z) := \xi\!\bigl(\tfrac12 + iz\bigr),
$$
of the completed Riemann xi. The identification is structural: in the
2-channel ($\zeta, L_{\chi_3}$) Bures fiber of Paper I, the K-odd channel
$L_{\chi_3}$ acts as a **connection** (gauge), not as a state; the
covariant log-derivative of the scalar transfer $M = \mathcal{L}_3/\Xi$,
after subtraction of the K-odd connection, is trivially $-\Xi'/\Xi$. The
**CM Poisson Monotonicity criterion** — $\mathrm{Im}\,m_B(z) \geq 0$ on
$\mathbb{C}_+$ if and only if RH — is a classical Pólya–Laguerre statement
[`Polya1927`, `LevinLP1980`] now equipped with the program's natural
target.

### What this paper is, and is not

Paper II is the **carrier-construction phase** of the program. It
establishes the Hilbert space on which Paper III's analytic positivity
machinery will live. **It does not yet prove RH**, nor does it prove the
convolution-square positivity, the averaged CRT shadow uniformity, the
double-cutoff dominated convergence, or the positive-current transport
theorem — those are the work of Paper III. Paper II terminates with a
clean statement of the CM Poisson Monotonicity criterion as the natural
target on the carrier it has built, and hands off.

### Two audiences

The paper is written for two readerships and bridges between them.

**For the representation theorist.** The Heisenberg algebra
$[\hat a, \hat a^\dagger] = 1$, Stone–von Neumann uniqueness of its
irreducible unitary representations, the Bargmann–Fock realization
$\mathcal{F}^{\mathrm{Bargmann}} \cong L^2(\mathbb{R}, dx)$ via the
Bargmann transform, the metaplectic group $\mathrm{Mp}_2(\mathbb{R})$ as
the unitary double cover of $\mathrm{SL}_2(\mathbb{R})$ acting on the Weyl
representation, and the standard Tate local zeta integrals are all
assumed familiar from [`Folland1989`, `ReedSimonII`, `Tate1967`]. The
program-side objects — the $\mathbb{Z}/6$ Bures fiber, the K-involution,
the Galois identification with $\mathbb{Q}(\sqrt{-3})$, the
occupation-decorated symmetric algebra — are introduced with one-line
glosses where they appear, but the load-bearing prerequisites are
collected in Paper I.

**For the arithmetic geometer / Connes-school reader.** The adele class
space of $\mathbb{Q}$, the Connes–Consani Picard groupoid framework
[`ConnesConsani2026`], the Connes–Consani–Moscovici prolate operator
[`CCM2024`], and Tate's adelic framework [`Tate1967`] are all assumed
familiar. The program-side objects new to Paper II — the occupation lift,
the single-axis projector, the K-odd-as-gauge subtraction, the Bures
log-derivative target — are introduced with derivation in the body. The
reader who is willing to import the carrier we build will find a clean
match with the Tate-Connes-Consani framework on the analytic side.

### Position in the program

The trilogy `Identifying 3` [`Murillo2026a`, `Murillo2026b`,
`Murillo2026c`] is published. The post-trilogy **RH-Done** sequence is:

- **Paper I — Identification.** What the program is working with. Dots
  1–3 of the spine [`RH-Done-Draft1`, §A].
- **Paper II — The Right Carrier** (this paper). The occupation-decorated
  symmetric Fock; Uniform Place Treatment; the Bures-covariant
  log-derivative as the Hilbert–Polya / CM Poisson target. Dots 4–6.
- **Paper III — Closure.** Convolution-square positivity of Poisson
  windows, averaged CRT shadow uniformity at polynomial scale, the
  positive-current transport theorem, and the main theorem on RH via
  Pólya–Laguerre. Dots 7–10.

Paper II sits between identification and closure. It cites Paper I freely
for the substrate; it sets the stage for Paper III by building the
carrier and naming the target.

### What is new here, what is cited

The three layers of Paper II have distinct provenance.

**Layer 1.** The exact upstairs von Mangoldt formula
(Theorem T4.1) and the necessity of placing $\Pi_{\mathrm{sa}}$ before
CRT compression (Identification I4.2) are extracted from the working
notes `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md` and
`Note_LastLockOccupationDecoratedRecovery_H9qT6.md`, and made explicit
here for the first time. The convolution-occupation derivation is
classical in spirit (it is the logarithmic Euler-product identity read in
the symmetric algebra), but the **structural recognition that
$\Pi_{\mathrm{sa}}$ must precede compression** is the program's
contribution.

**Layer 2.** The UPT-axiomatization (Axioms A5.1, A5.2) is the program's
naming of an implicit commitment already present in any adelic treatment
of $\zeta$: every place $v$ of $\mathbb{Q}$ carries a local factor. The
**derivation of Bargmann–Fock from UPT + Stone–von Neumann** (Theorem
T5.3) is structurally classical [`Folland1989`, Ch. 1] — what is new is
the recognition that the program's finite-place occupation lift, when
extended to $v = \infty$ by UPT, *automatically* produces the
Archimedean carrier. Tate's local zeta integrals on the Bargmann ground
and first-excited states (Theorem T5.4) are textbook
[`Tate1967`, `Bump1997`]; the **program's contribution is observing that
they emerge here without being imposed** — they are inner products
between UPT-forced eigenstates and the Tate multiplicative character
$|x|^{s-1}$. The Hardy–Titchmarsh intertwining (Theorem T5.5) is
classical Mellin-transform theory; it is recorded here for completeness
because it pins down the canonical Archimedean height measure $dm
\propto |\Gamma_\mathbb{R}(\tfrac12 + is)|^2\,ds$ that arises naturally
on the spectral side.

**Layer 3.** The Bures-covariant log-derivative
$m_B = -\Xi'/\Xi$ (Definition D6.1) and the K-odd gauge identification
(Theorem T6.2) are new in Paper II; they are extracted from
[`HPo-notes`] Addendum B (`Note_BuresLogDerivative_ClaudeEinstein.md`).
The equivalence
$\mathrm{Im}\,m_B \geq 0 \;\Leftrightarrow\;$ RH (Theorem T6.3) is the
classical Pólya–Laguerre criterion [`Polya1927`, `LevinLP1980`,
`Boas1954`]; the **program's contribution is supplying the natural
$m_B$ target via the K-odd gauge subtraction**, which links Paper I's
finite-cyclotomic Galois decomposition to the analytic Hilbert–Polya
target.

The numerical verifications underlying the new identifications are
recorded in the probes
[`probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py`],
[`probe_BuresLogDerivative_ClaudeEinstein.py`], and
[`probe_BuresPickGram_R6mT4.py`], all of which confirm the analytical
identities to floating-point precision.

### Roadmap

§1 collects what Paper II inherits from Paper I (cite-and-use, no
re-derivation). §§2–3 build the finite carrier and prove the upstairs
formula with the CRT-after-not-before identification. §4 states and
justifies the UPT axioms. §5 derives Bargmann–Fock from
UPT + Stone–von Neumann. §6 computes the Tate local zeta integrals on
the ground and first-excited states and recovers the standard
Archimedean local $L$-factors. §7 records the Hardy–Titchmarsh
intertwining. §8 defines the Bures-covariant log-derivative and proves
the K-odd gauge identification. §9 states the CM Poisson Monotonicity
criterion. §10 closes with a hand-off to Paper III.

A reader interested only in the carrier construction can read §§2–7. A
reader interested only in the analytic target can read §§8–9 (with §1
as backref to Paper I). The full chain runs §§2–9 in order.

---

## §1. Inheritance from Paper I

This section is cite-and-use. It collects the results from
Paper I [`MurilloPaperI2026`] that Paper II requires as input, in the
form in which they are quoted later. No proofs are given here; all are
in Paper I.

### 1.1 What Paper I delivered

Paper I established the following.

**Theorem 2.1 of Paper I** ($\log\zeta$ as effective action).
The Riemann zeta function is the categorical effective action of `ל2`'s
log-partition $\Phi(\eta) = -\sum_p \log(1 - e^{\eta_p})$ on the
prime-axis exponential family along the diagonal slice
$\eta_p(s) = -s\log p$:
$$
\Phi(\eta(s)) \;=\; -\sum_p \log(1 - p^{-s}) \;=\; \log\zeta(s).
$$
The corresponding mean-parameter distribution is the Riemann zeta
distribution $q_n(s) = n^{-s}/\zeta(s)$ on $\mathbb{N}_{>0}$.

**Theorem 4.1 of Paper I** (Critical-line $N$-uniformity). Along the
primorial ladder $\{P_n\}_{n \geq 1}$, the twisted Plancherel
coefficients $\hat Q^{(P_n)}_k(s) = \zeta_{P_n}(s, k)/\zeta(s)$ of the
residue-projected zeta distribution satisfy
$|\hat Q^{(P_n)}_k(s)| = |\hat Q^{(P_n)}_{-k}(1-s)|$ for every $k$ and
every $n$ if and only if $\mathrm{Re}(s) = 1/2$.

**Theorem 5.1 of Paper I** ($\mathbb{Z}/6$ 2D collapse). The five
non-trivial Hurwitz channels $\zeta(s, r/6)$ for $r \in \{1, 2, 3, 4, 5\}$
live in the 2-dimensional function space spanned by $\zeta(s)$ and
$L(s, \chi_3)$, with explicit closed-form coefficients in
$a = 2^{-s}, b = 3^{-s}$.

**Theorem 5.2 of Paper I** (K-orbit parity). The K-involution
$K : r \to -r \pmod 6$ on $\mathbb{Z}/6$ block-diagonalizes the
2-channel system into a K-fixed $\zeta$-line and a K-anti-fixed
$L_{\chi_3}$-line.

**Theorem 5.3 of Paper I** ($L(1/2, \chi_3) > 0$ unconditionally).
By Iwaniec–Sarnak [`IwaniecSarnak2000`] for real primitive Dirichlet
characters and the LMFDB record `1-3-3.2-r1-0-0`, with
$L(1/2, \chi_3) = 0.4808675576\ldots$ to arbitrary precision.

**Identification T3.3 of Paper I** (Galois identification). The
2-channel structure $(\zeta, L_{\chi_3})$ is the Galois decomposition
of the Connes–Consani Picard groupoid for the degree-2 cover
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$, with
$\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) L(s, \chi_3)$ and
K-involution = Galois involution.

**Identification I3.4 of Paper I** ($\mathbb{Z}/6$ Bures carrier as
degree-2 cover). The program's $\mathbb{Z}/6$ Bures carrier is
structurally the degree-2 cover by $\mathbb{Q}(\sqrt{-3})$ of the
Connes–Consani adele class space of $\mathbb{Q}$.

### 1.2 The structural input Paper II needs

Paper II uses Paper I's inheritance in two structurally distinct places.

(a) **The Archimedean factor $\pi^{-s/2}\Gamma(s/2)$.** Paper I's
Theorem 2.1 identifies $\log\zeta$ as a finite-place categorical
effective action read on the prime-axis simplex; the Archimedean factor
of the completed $\xi(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$
is not derived in Paper I. Paper II §6 supplies it from UPT + Tate's
local zeta integral on the Bargmann ground state.

(b) **The K-odd $L_{\chi_3}$ channel as a gauge.** Paper I's
Theorems 5.1, 5.2, and Identification T3.3 supply the 2-channel
$(\zeta, L_{\chi_3})$ structure, with the K-involution acting as the
Galois involution of the cover. Paper II §8 treats the K-odd channel
$L_{\chi_3}$ as a *connection* (gauge), not as a state, and uses
its log-derivative as the subtraction needed to isolate the
$\Xi$-divisor in the Bures-covariant log-derivative $m_B$.

These two uses of Paper I material are independent. (a) feeds the
Archimedean construction of §§4–7; (b) feeds the Bures log-derivative
identification of §§8–9.

### 1.3 What is not used

Several Paper I results are recorded but not invoked in Paper II.

- The closed-form cubic A-C tensor of Paper I §3 (Theorem 3.1) is used
  only in the cluster sign analysis of Paper III; Paper II does not use
  it.
- The critical-line $N$-uniformity locus of Paper I Theorem 4.1 is
  structural context but is not invoked operationally in Paper II.
- The Iwaniec–Sarnak non-vanishing $L(1/2, \chi_3) > 0$ of Paper I
  Theorem 5.3 is the load-bearing input for the cluster sign theorem
  of Paper III, but Paper II's analytic content does not require it.

These results are loaded for use in Paper III; Paper II carries them
through structurally but does not depend on them.

---

## §2. The Occupation-Decorated Symmetric Fock $\mathcal{F}_n$

We construct the finite carrier at each primorial row: the symmetric
algebra on the prime-axis vector space, equipped with a single-axis
projector and a differentiation operator that together implement the
exact upstairs von Mangoldt formula. This is Dot 4 of
[`RH-Done-Draft1` §A], with Theorem T4.1 of [`RH-Done-Draft1` §B].

### 2.1 The carrier

Fix a primorial row $n \geq 1$ and let
$$
\mathcal{P}_n \;=\; \{p_1, p_2, \ldots, p_n\} \;=\; \{2, 3, 5, \ldots, p_n\}
$$
be the first $n$ primes, with $P_n = \prod_{p \in \mathcal{P}_n} p$ the
primorial.

**Definition 2.1** (Prime-axis vector space).
The *prime-axis vector space at row $n$* is
$$
V_n \;:=\; \bigoplus_{p \in \mathcal{P}_n}\mathbb{C}\,e_p,
$$
the complex vector space with basis $\{e_p\}_{p \in \mathcal{P}_n}$
indexed by the primes at the row. We write
$$
H_s \;:=\; \sum_{p \in \mathcal{P}_n} p^{-s}\,e_p \;\in\; V_n \subset \mathcal{F}_n
$$
for the *prime-axis $s$-vector*, a one-parameter family of elements of
$V_n$.

**Definition 2.2** (Occupation-decorated symmetric algebra).
The *occupation-decorated symmetric Fock at row $n$* is the symmetric
algebra
$$
\boxed{\;
\mathcal{F}_n \;:=\; \mathrm{Sym}(V_n)
\;\cong\; \mathbb{C}[e_{p_1}, e_{p_2}, \ldots, e_{p_n}]
\;\cong\; \mathbb{C}\bigl[\mathbb{N}^{\mathcal{P}_n}\bigr],
\;}
$$
i.e. the polynomial algebra in the prime-axis generators, equipped with
its grading by *occupation multi-index*
$\alpha = (\alpha_p)_{p \in \mathcal{P}_n} \in \mathbb{N}^{\mathcal{P}_n}$.
The monomial basis is
$$
e_\alpha \;:=\; \prod_{p \in \mathcal{P}_n} e_p^{\alpha_p},
\qquad
\text{with product}\qquad e_\alpha \cdot e_\beta \;=\; e_{\alpha + \beta}.
$$

We adopt the convention $e_p^r = e_{r\,e_p}$ with coefficient $1$ on the
single-axis monomial (i.e., no multinomial factor on the diagonal axis).

**Log-height dictionary.** Each multi-index $\alpha$ has a *log-height*
$$
|\alpha|_{\log} \;:=\; \sum_{p \in \mathcal{P}_n}\alpha_p\,\log p,
$$
and we identify single-axis occupations $\alpha = r\,e_p$ with prime
powers via
$$
\boxed{\;e_{r\,e_p}\;\longleftrightarrow\;p^r,\qquad |r\,e_p|_{\log}\;=\;r\log p.\;}
$$
For a log-side detector $G : \mathbb{R} \to \mathbb{C}$, we apply
the *height evaluation map* $e_\alpha \mapsto G(|\alpha|_{\log})$.

The carrier $\mathcal{F}_n$ is finitely generated (as a polynomial
algebra in $n$ variables) but infinite-dimensional as a complex vector
space, with $r$-th graded piece
$$
\mathrm{Sym}^r(V_n) \;=\; \mathrm{span}_{\mathbb{C}}\bigl\{e_\alpha : |\alpha| = r\bigr\},
\qquad
\dim_{\mathbb{C}} \mathrm{Sym}^r(V_n) \;=\; \binom{r + n - 1}{n - 1}.
$$

### 2.2 The single-axis projector

**Definition 2.3** (Single-axis projector $\Pi_{\mathrm{sa}}$).
The *single-axis projector* on $\mathcal{F}_n$ is the linear map
defined on basis vectors by
$$
\Pi_{\mathrm{sa}}\,e_\alpha \;=\;
\begin{cases}
e_\alpha & \text{if } \alpha = r\,e_p \text{ for some } p \in \mathcal{P}_n,\ r \geq 1,\\
0 & \text{otherwise}.
\end{cases}
$$
That is, $\Pi_{\mathrm{sa}}$ keeps **single-axis occupations**
(monomials supported on exactly one prime axis with strictly positive
occupation), and kills mixed-axis occupations and the constant
$e_{\mathbf{0}} = 1$.

The image $\Pi_{\mathrm{sa}}\,\mathcal{F}_n$ is the
**single-axis subalgebra**
$$
\mathcal{F}_n^{\mathrm{sa}} \;=\; \bigoplus_{p \in \mathcal{P}_n}\bigoplus_{r \geq 1}\mathbb{C}\,e_{r\,e_p},
$$
naturally indexed by the prime-power set
$\{p^r : p \in \mathcal{P}_n, r \geq 1\}$ under the log-height
dictionary.

**Remark.** $\Pi_{\mathrm{sa}}$ is the upstairs *algebraic* form of the
von Mangoldt support condition: $\Lambda(n) = \log p$ if $n = p^r$ for
some prime $p$ and integer $r \geq 1$, else $\Lambda(n) = 0$. The
support of $\Lambda$ on $\mathbb{N}_{>0}$ corresponds, under the
log-height dictionary, exactly to the image of $\Pi_{\mathrm{sa}}$ in
$\mathcal{F}_n$.

### 2.3 The differentiation operator $D_s$

**Definition 2.4** (Differentiation operator).
The *differentiation operator on $\mathcal{F}_n$* is the linear map
$$
D_s \;:=\; -\partial_s
$$
acting on coefficients of $e_\alpha$ that depend on a complex parameter
$s$. It is a derivation: on a coefficient $c(s)\,e_\alpha$,
$D_s(c\,e_\alpha) = (-c'(s))\,e_\alpha$.

For the family of one-parameter coefficients we use most often,
$c(s) = (1/r)\,p^{-rs}$ on the single-axis monomial $e_{r\,e_p}$:
$$
D_s\!\Bigl(\frac{1}{r}\,p^{-rs}\Bigr)
\;=\;\frac{1}{r}\cdot r\log p \cdot p^{-rs}
\;=\;(\log p)\,p^{-rs}.
$$
**The cancellation $1/r \cdot r = 1$ is the algebraic origin of the
von Mangoldt weight $\log p$**: it converts the logarithmic
cumulant coefficient $1/r$ from the Euler logarithm into the bare
$\log p$ of $\Lambda(p^r)$.

### 2.4 The logarithmic occupation series

For complex $s$ with $\mathrm{Re}(s) > 1$ and finite occupation cutoff
$K \in \mathbb{N}$, the *logarithmic occupation series* in $\mathcal{F}_n$
is
$$
L_{n, K}(s) \;:=\; \sum_{k = 1}^{K}\frac{1}{k}\,H_s^k \;\in\;\mathcal{F}_n,
$$
the truncated formal-power-series expansion of $-\log(1 - H_s)$ in the
free generator $H_s = \sum_p p^{-s}\,e_p$. For $K \to \infty$ this
converges in the $(\mathcal{F}_n)$-adic topology to
$-\log(1 - H_s)$ wherever the geometric series for $1/(1 - H_s)$
converges, i.e., for any $s$ such that
$\sum_p |p^{-s}| < \infty$, which holds when $\mathrm{Re}(s) > 1$.

The $k$-th symmetric power
$$
H_s^k \;=\; \sum_{\alpha\,:\,|\alpha| = k}\,\frac{k!}{\prod_p \alpha_p!}\,\Bigl(\prod_p p^{-s\alpha_p}\Bigr)\,e_\alpha
$$
is the multinomial expansion of the $k$-fold product of $H_s$ in the
commutative symmetric algebra. Applying the single-axis projector kills
every multi-axis monomial in this expansion, so the only surviving
$\alpha$ are the single-axis multi-indices $\alpha = k\,e_p$ for some
$p$. The multinomial coefficient
$k!/\prod_p\alpha_p!$ at $\alpha = k\,e_p$ is just $k!/k! = 1$. Hence
$$
\boxed{\;\Pi_{\mathrm{sa}}\,H_s^k \;=\; \sum_{p \in \mathcal{P}_n} p^{-ks}\,e_{k\,e_p}.\;}
$$

This is the key algebraic identity of §2. The mixed-occupation
multinomial coefficients are *killed at the source* by the single-axis
projector; only the single-axis "diagonal" survives, with coefficient
$p^{-ks}$ and trivial multinomial factor.

### 2.5 Theorem T4.1: the exact upstairs von Mangoldt formula

**Theorem 2.5** (*Exact Upstairs Von Mangoldt Recovery; T4.1 of
[`RH-Done-Draft1`]*).
*For every primorial row $n \geq 1$ and every finite occupation cutoff
$K \in \mathbb{N}$, the occupation-decorated symmetric Fock $\mathcal{F}_n$
implements the exact identity*
$$
\boxed{\;
D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s)
\;=\;
\sum_{p \in \mathcal{P}_n}\sum_{r = 1}^{K}(\log p)\,p^{-rs}\,e_{r\,e_p}
\;}
$$
*as an identity in $\mathcal{F}_n$, valid for every
$s \in \mathbb{C}$ with $\mathrm{Re}(s) > 1$ (the radius of convergence
in $s$ of $H_s^k$ for $k \geq 1$). Under the log-height dictionary
$e_{r\,e_p} \leftrightarrow p^r$, the right-hand side equals
$\sum_{p \leq p_n}\sum_{r = 1}^{K}\Lambda(p^r)\,(p^r)^{-s}\,e_{r\,e_p}$,
the upstairs (occupation-decorated) finite-cutoff Mangoldt
distribution.*

*Proof.* From §2.4,
$\Pi_{\mathrm{sa}}\,H_s^k = \sum_p p^{-ks}\,e_{k\,e_p}$. Linearity of
$\Pi_{\mathrm{sa}}$ in $\mathcal{F}_n$ gives
$$
\Pi_{\mathrm{sa}}\,L_{n, K}(s)
\;=\;
\sum_{k = 1}^{K}\frac{1}{k}\,\Pi_{\mathrm{sa}}\,H_s^k
\;=\;
\sum_{k = 1}^{K}\sum_{p \in \mathcal{P}_n}\frac{1}{k}\,p^{-ks}\,e_{k\,e_p}.
$$
Apply $D_s = -\partial_s$ termwise (justified by polynomial dependence
in $s$ of each term and finite occupation cutoff). On the term
$(1/k)\,p^{-ks}\,e_{k\,e_p}$, by §2.3,
$$
D_s\!\Bigl(\frac{1}{k}\,p^{-ks}\Bigr)\,e_{k\,e_p}
\;=\;
\frac{1}{k}\cdot k\log p\cdot p^{-ks}\,e_{k\,e_p}
\;=\;
(\log p)\,p^{-ks}\,e_{k\,e_p}.
$$
Re-indexing $k \to r$, summing over $r = 1, \ldots, K$ and
$p \in \mathcal{P}_n$ gives the displayed identity. The dictionary
identification of the right-hand side with $\Lambda(p^r)(p^r)^{-s}$ is
the definition of $\Lambda$ on prime powers. $\square$

**Test-function form.** Apply the height evaluation map
$e_\alpha \mapsto G(|\alpha|_{\log})$ to Theorem 2.5 on a log-side
detector $G : \mathbb{R} \to \mathbb{C}$. The right-hand side becomes
$$
\boxed{\;
\mathrm{VM}_{n, K}(G)
\;:=\;
\sum_{p \leq p_n}\sum_{r = 1}^{K}(\log p)\,G(r\log p),
\;}
$$
which is the explicit-formula finite-place test-function distribution.
The reflected test-function distribution is obtained by applying the
same extractor to the reflected detector $G^\#(u) = G(-u)$.

### 2.6 What Theorem 2.5 does and does not say

Theorem 2.5 is **exact**: no analytic estimate is involved. It is a
purely algebraic identity in $\mathcal{F}_n$, valid termwise on the
truncated logarithmic occupation series. The convergence of
$L_{n, K}(s)$ for $K \to \infty$ at $\mathrm{Re}(s) > 1$ is the
classical convergence region of the Dirichlet series of $\zeta$; in
$\mathcal{F}_n$ this is the convergence of the geometric series
$1/(1 - H_s) = \sum_k H_s^k$ when $\sum_p |p^{-s}| < \infty$.

Theorem 2.5 *does not* extend to $\mathrm{Re}(s) \leq 1$ at the level of
the formal series; the analytic continuation of the right-hand side
(the von Mangoldt distribution on prime powers) to the rest of
$\mathbb{C}$ goes through the explicit formula and is the Paper III
content. Paper II's contribution at finite primorial row is the
algebraic identity in $\mathcal{F}_n$.

Theorem 2.5 also *does not* yet supply the Archimedean side. The
completed $\xi'/\xi$ has additional gamma-and-pi factors and an
Archimedean term $-\tfrac12\log\pi - \tfrac12 (\Gamma'/\Gamma)(s/2)$,
which lives in the Archimedean local factor we construct in §§4–6.
Paper II's hand-off to the Archimedean factor is via the
Uniform Place Treatment of §4.

---

## §3. Why CRT After, Not Before

The single-axis projector $\Pi_{\mathrm{sa}}$ of §2.2 is well-defined on
the upstairs occupation algebra $\mathcal{F}_n$, but **ill-defined after
CRT compression**. This is the program's key structural recognition at
the finite-place level: the von Mangoldt support condition can only be
applied *before* the residue-axis compression of the explicit-formula
machinery. This is Identification I4.2 of [`RH-Done-Draft1` §B].

### 3.1 The CRT compression map

At primorial row $n$, the *finite-character group* is
$$
\widehat{R}_n \;\cong\; \prod_{p \in \mathcal{P}_n}\mathbb{Z}/p\mathbb{Z}
\;\cong\;\widehat{(\mathbb{Z}/P_n)},
$$
the Pontryagin dual of $\mathbb{Z}/P_n$. For each prime $p \in \mathcal{P}_n$
choose a local prime-axis character $\chi_p : \mathbb{Z}/p \to \mathbb{C}^\times$
(any non-trivial generator suffices).

**Definition 3.1** (CRT compression).
The *CRT compression map* is the algebra homomorphism
$$
\pi_{\mathrm{CRT}} : \mathcal{F}_n \;\to\; \mathbb{C}[\widehat{R}_n],
\qquad
\pi_{\mathrm{CRT}}(e_\alpha) \;=\; \prod_{p \in \mathcal{P}_n}\chi_p^{\,\alpha_p},
$$
extending multiplicatively from the prime-axis generators
$e_p \mapsto \chi_p$.

Because each $\chi_p$ has finite order $p$, the compression is
**occupation-periodic on each axis**:
$$
\pi_{\mathrm{CRT}}(e_{(r + p)\,e_p}) \;=\; \chi_p^{r + p} \;=\; \chi_p^r \;=\; \pi_{\mathrm{CRT}}(e_{r\,e_p}).
$$
Unbounded prime-power occupation depth $r \in \mathbb{N}$ is aliased to
$r \bmod p$ under $\pi_{\mathrm{CRT}}$.

### 3.2 The mixed-occupation aliasing

The genuinely structural obstruction is *not* the occupation-periodicity
on a single axis, but the **aliasing of mixed-axis occupations to
single-axis labels**. This is the content of [`RH-Done-Draft1` §B I4.2]
and [`Note_LastLockOccupationDecoratedRecovery_H9qT6` §3].

**Example (mixed/single-axis collision at row $n = 3$).** At
$\mathcal{P}_3 = \{2, 3, 5\}$, with $\chi_p$ the standard generator of
$\widehat{\mathbb{Z}/p}$:
$$
\pi_{\mathrm{CRT}}(e_{5\,e_5})\;=\;\chi_5^{\,5}\;=\;\chi_5^{\,0}\;=\;1,
$$
$$
\pi_{\mathrm{CRT}}(e_{2\,e_2 + 3\,e_3})\;=\;\chi_2^{\,2}\,\chi_3^{\,3}\;=\;\chi_2^{\,0}\,\chi_3^{\,0}\;=\;1.
$$
The single-axis occupation $5\,e_5$ (representing the prime power
$5^5 = 3125$, with $\Lambda(3125) = \log 5$ under Theorem 2.5) and the
mixed-axis occupation $2\,e_2 + 3\,e_3$ (representing the composite
$2^2 \cdot 3^3 = 108$, with $\Lambda(108) = 0$ since $108$ has two
distinct prime factors) **share the same compressed CRT label**, both
equal to the trivial character.

Equivalently, under the multi-index congruence,
$$
(0, 0, 5) \;\equiv\; (2, 3, 0) \;\equiv\; (0, 0, 0) \pmod{(2, 3, 5)}.
$$

**Consequence.** The single-axis projector $\Pi_{\mathrm{sa}}$ cannot
be defined on $\mathbb{C}[\widehat{R}_n]$ in a way consistent with its
definition on $\mathcal{F}_n$. There is no canonical map
$\mathbb{C}[\widehat{R}_n] \to \mathcal{F}_n^{\mathrm{sa}}$ that picks
out "the single-axis preimage" of a compressed character, because the
preimage is not single-valued: it contains both single-axis and mixed
preimages.

### 3.3 Identification I4.2: the structural correspondence

**Identification 3.3** (*$\Pi_{\mathrm{sa}}$-before-CRT necessity; I4.2 of
[`RH-Done-Draft1`]*).
*The single-axis projector $\Pi_{\mathrm{sa}} : \mathcal{F}_n \to
\mathcal{F}_n^{\mathrm{sa}}$ is well-defined on the upstairs occupation
algebra and **ill-defined after CRT compression**. The correct order of
operations for finite-place von Mangoldt recovery is*
$$
\mathcal{F}_n \;\xrightarrow{\Pi_{\mathrm{sa}}}\; \mathcal{F}_n^{\mathrm{sa}}
\;\xrightarrow{D_s}\; \text{Mangoldt-weighted single-axis distribution}
\;\xrightarrow{\pi_{\mathrm{CRT}}}\; \text{compressed CRT shadow}.
$$
*The wrong order*
$$
\mathcal{F}_n \;\xrightarrow{\pi_{\mathrm{CRT}}}\; \mathbb{C}[\widehat{R}_n]
\;\xrightarrow{?}\; \mathcal{F}_n^{\mathrm{sa}}
$$
*has no canonical second arrow.*

*Justification.* §3.2's mixed/single-axis collision example exhibits a
mixed occupation $\alpha = 2\,e_2 + 3\,e_3$ and a single-axis occupation
$\beta = 5\,e_5$ with $\pi_{\mathrm{CRT}}(e_\alpha) = \pi_{\mathrm{CRT}}(e_\beta)$.
Any putative projector $\widetilde{\Pi}_{\mathrm{sa}}$ on
$\mathbb{C}[\widehat{R}_n]$ satisfying
$\widetilde{\Pi}_{\mathrm{sa}} \circ \pi_{\mathrm{CRT}} =
\pi_{\mathrm{CRT}} \circ \Pi_{\mathrm{sa}}$ would need to send the
common image $\pi_{\mathrm{CRT}}(e_\alpha) = \pi_{\mathrm{CRT}}(e_\beta) = 1$
to both
$\pi_{\mathrm{CRT}}(\Pi_{\mathrm{sa}}\,e_\alpha) = \pi_{\mathrm{CRT}}(0) = 0$
(since $\alpha$ is mixed) and
$\pi_{\mathrm{CRT}}(\Pi_{\mathrm{sa}}\,e_\beta) = \pi_{\mathrm{CRT}}(e_\beta) = 1$
(since $\beta$ is single-axis). These are incompatible, so no such
$\widetilde{\Pi}_{\mathrm{sa}}$ exists. The first order of operations is
therefore forced. $\square$

### 3.4 Why the upstairs lift is not new data

A natural question: does the occupation-decorated Fock add *new
arithmetic information* beyond the compressed CRT algebra
$\mathbb{C}[\widehat{R}_n]$? The answer is no — it remembers
information that the compressed algebra forgets. Specifically:

**Observation 3.4.** For every convolution-coefficient vector
$\widehat{h}^{*k}$ defined on the finite character group
$\widehat{R}_n$ and every $k \geq 1$, there exists an
occupation-resolved preimage
$$
\widetilde{\widehat{h}^{*k}} \;=\; \sum_{\alpha\,:\,|\alpha| = k}\frac{k!}{\prod_p\alpha_p!}\,\prod_p h_p^{\,\alpha_p}\,e_\alpha
\;\in\;\mathrm{Sym}^k(V_n)
$$
satisfying
$\pi_{\mathrm{CRT}}\,\widetilde{\widehat{h}^{*k}} = \widehat{h}^{*k}$.

That is, **the occupation lift is the pre-compression form of the
compressed Hayes–Mobius current**; no external arithmetic input is
added. The extra information stored in $\mathcal{F}_n$ is exactly the
**occupation history** — the multi-index $\alpha$ that the compressed
character $\chi^\alpha = \prod_p \chi_p^{\alpha_p}$ forgets.

For most finite-place applications (conductor support analysis, finite
Fisher geometry), the compressed object suffices. **For von Mangoldt
recovery specifically**, the occupation history is not optional: it is
the only place where the distinction between single-axis $p^r$ and
mixed-axis composites $p_1^{a_1}p_2^{a_2}\cdots$ survives.

### 3.5 Summary of §§2–3

The finite carrier at primorial row $n$ is the occupation-decorated
symmetric Fock $\mathcal{F}_n$. It supports the exact upstairs von
Mangoldt formula
$\mathrm{VM}_{n, K} = D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s)$
(Theorem 2.5 = T4.1). The single-axis projector $\Pi_{\mathrm{sa}}$ is
well-defined on $\mathcal{F}_n$ and not on the CRT-compressed shadow
$\mathbb{C}[\widehat{R}_n]$, so CRT compression must come *after*
$\Pi_{\mathrm{sa}}$ (Identification 3.3 = I4.2). The upstairs lift
$\mathcal{F}_n$ is the pre-compression form of the program's existing
Hayes–Mobius currents; it adds no external arithmetic data, only the
occupation history that compression discards.

This closes the finite-place layer of the carrier. The next three
sections extend it to the Archimedean place.

---

## §4. Uniform Place Treatment

The finite-place carrier $\mathcal{F}_n = \mathrm{Sym}(V_n) =
\bigotimes_{p \in \mathcal{P}_n}\mathrm{Sym}(\mathbb{C}\,e_p)$ has a
natural global extension that places every prime *and the Archimedean
place* on equal structural footing. This is the **Uniform Place
Treatment** (UPT). It splits into two axioms — *UPT-structure* (the
extension itself) and *UPT-Heisenberg* (the algebra realization at
$v = \infty$) — and these together with Stone–von Neumann uniqueness
will force, in §5, the Bargmann–Fock realization of the Archimedean
local Fock. This is Dot 5 of [`RH-Done-Draft1` §A].

### 4.1 The places of $\mathbb{Q}$

The set of places of $\mathbb{Q}$ is
$$
\Pi(\mathbb{Q}) \;=\; \{2, 3, 5, 7, 11, \ldots\} \;\cup\; \{\infty\}
\;=\;\mathcal{P}\;\cup\;\{\infty\},
$$
i.e., the rational primes (finite places) together with the unique
Archimedean place $\infty$ (the completion $\mathbb{Q}_\infty = \mathbb{R}$).
The standard adelic norm-product formula
$\prod_v |x|_v = 1$ for $x \in \mathbb{Q}^\times$ binds the finite-place
norms and the Archimedean absolute value into a single global structure
[`Cassels1986`, Ch. II].

The program's finite carrier $\mathcal{F}_n$ at row $n$ is defined on
the first $n$ finite places; for $n \to \infty$ it covers all finite
places of $\mathbb{Q}$. The Archimedean place is left unaddressed by
$\mathcal{F}_n$ — it is the missing local factor that any adelic
treatment of $\zeta$ must supply.

### 4.2 Axiom A5.1: UPT-structure

**Axiom A5.1** (*UPT-structure; A5.1 of [`RH-Done-Draft1`]*).
*The global occupation Fock of the program includes a local factor at
every place $v$ of $\mathbb{Q}$:*
$$
\mathcal{F}_v \;:=\; \mathrm{Sym}(\mathbb{C}\,e_v)\;\cong\;\mathbb{C}[e_v],\qquad v \in \Pi(\mathbb{Q}).
$$
*The Archimedean place $v = \infty$ is treated on equal structural
footing with the finite primes. The global occupation Fock is the
restricted tensor product*
$$
\mathcal{F}_\Pi \;=\; \bigotimes'_{v \in \Pi(\mathbb{Q})} \mathcal{F}_v,
$$
*with respect to the vacuum vectors $1 \in \mathcal{F}_v$.*

**Justification.** The axiom is the **make-explicit** of an implicit
adelic commitment present in any treatment of $\zeta$ that goes through
the Euler product
$\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ and its completed form
$\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ with the Archimedean local
factor $L_\infty(s) = \pi^{-s/2}\Gamma(s/2)$. The completed $\Lambda$
treats every place as a local factor; the program's finite-place lift
$\mathcal{F}_p = \mathrm{Sym}(\mathbb{C}\,e_p)$ is the symmetric-algebra
form of that local factor at the finite primes. UPT-structure asserts
that the same symmetric-algebra form applies at $v = \infty$. It is the
adelic-uniformity statement at the level of local Fock factors.

This axiom is structural, not analytic. It does not assert a Hilbert
norm; it asserts the existence of a polynomial local algebra
$\mathbb{C}[e_\infty]$ at $v = \infty$.

### 4.3 Axiom A5.2: UPT-Heisenberg

**Axiom A5.2** (*UPT-Heisenberg; A5.2 of [`RH-Done-Draft1`]*).
*The Archimedean local Fock $\mathcal{F}_\infty = \mathbb{C}[e_\infty]$
carries an irreducible unitary representation of the Heisenberg algebra*
$$
[\hat a, \hat a^\dagger]\;=\;\mathbf{1},
$$
*with $\hat a^\dagger = e_\infty$ (= multiplication by $e_\infty$, the
occupation-raising operator on the polynomial algebra) and
$\hat a = (\hat a^\dagger)^*$ in the unique Hilbert completion compatible
with the algebra and the K-real conjugation structure on $\mathcal{F}_v$.*

**Justification.** UPT-Heisenberg is the *operator-algebra realization*
of the Archimedean local factor. It is implicit in three commitments
the program already endorses:

(i) **Tate's adelic framework.** [`Tate1967`] treats the Archimedean
local zeta integral as the action of the multiplicative group
$\mathbb{R}^\times$ on $L^2(\mathbb{R}, dx)$ by the regular
representation, with Heisenberg–Weyl as the natural symplectic extension.
The Heisenberg algebra is the infinitesimal form of the Weyl
representation.

(ii) **The Connes–Consani–Moscovici prolate operator** [`CCM2024`]. The
operator
$\mathbf{W}_\lambda = -\mathbb{S}^2 + 2\pi\lambda^2(4\hat N + 1) - 1/4$
acts on $L^2(\mathbb{R})^{\mathrm{ev}}$ and uses both the scaling
operator $\mathbb{S}$ (= the dilation generator) and the number operator
$\hat N$. These are precisely the generators of a Heisenberg-style
algebra on the Archimedean local space.

(iii) **The program's finite-place occupation lift.** Each
finite-place local Fock $\mathcal{F}_p$ has a built-in Heisenberg-style
structure: the raising operator $e_p$ (multiplication) and the lowering
operator $\partial_{e_p}$ (formal differentiation, normalized to give
$[\partial_{e_p}, e_p] = 1$). UPT-Heisenberg asserts that this structure
*persists* at $v = \infty$.

The axiom is the **explicit form of an implicit commitment**: any
program that uses Tate's local zeta integrals at $v = \infty$, or
CCM's prolate operator, or extends the program's finite-place occupation
lift to all of $\Pi(\mathbb{Q})$, is already endorsing the
Heisenberg-algebra realization. UPT-Heisenberg names it.

### 4.4 What A5.1 and A5.2 do and do not do

The two axioms together specify the Archimedean local algebra
$\mathcal{F}_\infty = \mathbb{C}[e_\infty]$ and the Heisenberg structure
on it. They do not yet supply:

- the inner product / Hilbert norm (this is forced by Stone–von Neumann
  in §5);
- the metaplectic / Weyl realization (forced by §5 + the symplectic
  cocycle, see §5.4);
- the Tate local zeta integrals / Archimedean $L$-factors (Tate's
  theorem applied to the Bargmann ground state, §6);
- the gamma-multiplier intertwining of Fourier with branch reflection
  on the spectral side (Hardy–Titchmarsh classical, §7).

What A5.1 and A5.2 *do* supply is the structural input that Stone–von
Neumann uniqueness can act on. From that point onward the construction
is forced.

**Calibration of axiomatic content.** A5.1 and A5.2 are *named axioms*,
not theorems. The program does not pretend they are derived from
deeper finite-place input. They are the program's commitment to global
adelic uniformity at the level of the operator-algebra structure of
local Fock factors. The next three sections show that **given this
commitment**, the standard Archimedean local structure (Bargmann–Fock,
$\pi^{-s/2}\Gamma(s/2)$, the metaplectic Fourier, the Hardy–Titchmarsh
measure) is forced *without further choice*.

---

## §5. Bargmann–Fock from Stone–von Neumann

The Archimedean local algebra $\mathcal{F}_\infty = \mathbb{C}[e_\infty]$
of A5.1 with the Heisenberg structure of A5.2 has a unique unitary
Hilbert completion: the **Bargmann–Fock space**. This is Theorem T5.3 of
[`RH-Done-Draft1` §B]. The derivation is by Stone–von Neumann uniqueness
applied to the Heisenberg-algebra realization, exactly as in
[`Folland1989`, Ch. 1].

### 5.1 The Heisenberg algebra and its representations

Recall the *Heisenberg Lie algebra*
$$
\mathfrak{h} \;=\; \mathrm{span}_\mathbb{R}\{\hat a, \hat a^\dagger, \mathbf{1}\}
\quad\text{with bracket}\quad
[\hat a, \hat a^\dagger]\;=\;\mathbf{1},\qquad [\hat a, \mathbf{1}]\;=\;[\hat a^\dagger, \mathbf{1}]\;=\;0.
$$
A *unitary representation* of $\mathfrak{h}$ on a complex Hilbert
space $\mathcal{H}$ is a pair $(\hat a, \hat a^\dagger)$ of densely
defined adjoint operators on $\mathcal{H}$ with $\hat a^\dagger$ the
adjoint of $\hat a$, the central element acting as $\mathbf{1}_\mathcal{H}$,
satisfying $[\hat a, \hat a^\dagger] = 1$ on a common dense invariant
subspace.

**Stone–von Neumann uniqueness** [`StoneVN`, see also `Folland1989`
Thm. 1.50]: *every irreducible unitary representation of the
Heisenberg group on a separable Hilbert space with central character
$z = 1$ is unitarily equivalent to the Schrödinger representation on
$L^2(\mathbb{R}, dx)$, equivalently to the Bargmann–Fock representation
on the holomorphic completion of $\mathbb{C}[z]$.*

This is the load-bearing classical input. UPT-Heisenberg supplies the
hypothesis; Stone–von Neumann supplies the uniqueness.

### 5.2 Theorem T5.3: Bargmann–Fock as the unique completion

**Theorem 5.1** (*Bargmann–Fock from UPT + Stone–von Neumann; T5.3 of
[`RH-Done-Draft1`]*).
*Under A5.1 and A5.2, the Hilbert-space completion of the Archimedean
local algebra $\mathcal{F}_\infty = \mathbb{C}[e_\infty]$ is uniquely the
**Bargmann–Fock space***
$$
\mathcal{F}_\infty^{\mathrm{Bargmann}} \;=\; \overline{\mathbb{C}[z]}^{\,\|\cdot\|_B},
\qquad
\langle z^m, z^n\rangle_B \;=\; m!\,\delta_{m, n},
$$
*equivalently, via the Bargmann transform [`Bargmann1961`,
`Folland1989` §1.6],*
$$
B : \mathcal{F}_\infty^{\mathrm{Bargmann}} \xrightarrow{\sim} L^2(\mathbb{R}, dx),
$$
*with $z^n/\sqrt{n!}$ mapping to the normalized Hermite functions
$h_n(x) = \pi^{-1/4}(2^n n!)^{-1/2}\,H_n(x)\,e^{-x^2/2}$.*

*Proof.* Identify $\hat a^\dagger$ with multiplication by $z$
(the generator $e_\infty$ in the polynomial algebra) and seek
$\hat a$ as the adjoint determined by $[\hat a, \hat a^\dagger] = 1$ and
unitarity.

Setting $w_n := \langle z^n, z^n\rangle_B$ on the Hilbert completion and
using $\hat a = (\hat a^\dagger)^*$:
$$
\langle z^{m + 1}, z^n\rangle_B \;=\; \langle \hat a^\dagger z^m, z^n\rangle_B
\;=\;\langle z^m, \hat a z^n\rangle_B.
$$
By Stone–von Neumann uniqueness up to scaling, the unique annihilation
operator satisfying $[\hat a, z] = 1$ on $\mathbb{C}[z]$ is
$\hat a = \partial_z$. (Any operator $\hat a'$ satisfying
$[\hat a', z] = c\,\mathbf{1}$ for a constant $c$ must be of the form
$\hat a' = c\partial_z + \text{lower-order}$, and unitarity plus
positive-energy spectrum forces $c = 1$ and no lower-order term.)
Substituting $\hat a = \partial_z$ on the right-hand side:
$$
w_{m + 1}\,\delta_{m + 1, n} \;=\; n\,w_n\,\delta_{m, n - 1},
$$
i.e., $w_{n + 1} = (n + 1)\,w_n$ for $n \geq 0$. With normalization
$w_0 = \langle 1, 1\rangle_B = 1$, this yields the unique solution
$$
w_n \;=\; n!.
$$
Orthogonality $\langle z^m, z^n\rangle_B = 0$ for $m \neq n$ follows
from the self-adjointness of the number operator
$\hat N = \hat a^\dagger \hat a = z\partial_z$ on the polynomial dense
subspace: $\hat N z^n = n z^n$ has distinct eigenvalues, and self-adjoint
operators with distinct eigenvalues have orthogonal eigenvectors. The
unique Hilbert completion is therefore $\overline{\mathbb{C}[z]}$ with the
norm $\langle z^m, z^n\rangle_B = m!\,\delta_{m, n}$.

The Bargmann transform $B : \mathcal{F}_\infty^{\mathrm{Bargmann}} \to
L^2(\mathbb{R}, dx)$ is the unique unitary isomorphism implementing the
Stone–von Neumann equivalence between the Bargmann–Fock and Schrödinger
realizations (its explicit kernel is classical, see [`Folland1989`
§1.6]). It maps $z^n/\sqrt{n!} \mapsto h_n(x)$, the normalized Hermite
functions. $\square$

**Numerical verification.** The probe
[`probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py`] confirms
$\langle z^n, z^n\rangle_B = n!$ for $n = 0, 1, 2, 3, 4, 5$ by direct
Gaussian-integral computation. The norm is derived, not assumed.

### 5.3 Tate–Weil normalization

The Bargmann–Fock construction of §5.2 is up to an overall positive
real scaling on $\hat a^\dagger$ (the choice of $\hbar$). To pin down
the **Tate–Weil normalization** that matches the standard adelic
Fourier transform [`Weil1964`], we fix
$$
\hbar \;=\;\frac{1}{2\pi},\qquad [\hat x, \hat p]\;=\;\frac{i}{2\pi},
$$
with $\hat x$ multiplication by $x$ and $\hat p = -i\hbar\,\partial_x$.
The annihilation and creation operators are then
$$
\boxed{\;
\hat a \;=\; \sqrt{\pi}\,\hat x + \frac{i}{\sqrt{4\pi}}\,\hat p,
\qquad
\hat a^\dagger \;=\;\sqrt{\pi}\,\hat x - \frac{i}{\sqrt{4\pi}}\,\hat p,
\;}
$$
giving $[\hat a, \hat a^\dagger] = 1$. The ground state $\psi_0$, defined
by $\hat a\psi_0 = 0$, satisfies
$$
\Bigl(\sqrt{\pi}\,x + \frac{1}{\sqrt{4\pi}}\,\partial_x\Bigr)\psi_0(x) \;=\; 0
\;\implies\; \partial_x\psi_0 \;=\; -2\pi x\,\psi_0
\;\implies\; \psi_0(x) \;=\; e^{-\pi x^2}
$$
(up to overall normalization; with $L^2$-normalization
$\psi_0(x) = 2^{1/4}\,e^{-\pi x^2}$). The first excited state is
$$
\psi_1(x) \;=\; \hat a^\dagger\,\psi_0(x) \;\propto\; x\,e^{-\pi x^2}.
$$

The Tate–Weil normalization is fixed by the requirement that the
Fourier transform on $L^2(\mathbb{R}, dx)$ has kernel $e^{-2\pi i x\xi}$
(the standard adelic / Tate-style normalization), matching the global
Fourier transform on the ring of adeles $\mathbb{A}_\mathbb{Q}$.

### 5.4 The Weyl cocycle and the metaplectic group

The Weyl group elements $W(u, v) := \exp(2\pi i(u\hat p - v\hat x))$
satisfy the symplectic cocycle
$$
W(u, v)\,W(u', v')\;=\;e^{i\pi(uv' - vu')}\,W(u + u', v + v')
\qquad((u, v), (u', v') \in \mathbb{R}^2).
$$
This is the **Tate–Weil metaplectic cocycle**, the standard cocycle of
the symplectic-projective representation on $L^2(\mathbb{R})$ in the
$\hbar = 1/(2\pi)$ normalization [`Weil1964`, `LV1980`, `Folland1989`
§4.1].

The rotation $\hat R : z \mapsto -iz$ on
$\mathcal{F}_\infty^{\mathrm{Bargmann}}$ corresponds, under the Bargmann
transform, to the standard Fourier transform $\hat{\mathcal{F}}$ on
$L^2(\mathbb{R}, dx)$:
$$
B\,\hat R\,B^{-1} \;=\; \hat{\mathcal{F}},\qquad \hat{\mathcal{F}}f(\xi) \;=\;\int_\mathbb{R} f(x)\,e^{-2\pi i x\xi}\,dx.
$$
This is the **metaplectic Fourier transform**: the lift of the rotation
$\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} \in \mathrm{SL}_2(\mathbb{R})$
to $\mathrm{Mp}_2(\mathbb{R})$, acting on the Heisenberg–Weyl
representation. Stone–von Neumann uniqueness identifies this as the
unique unitary extension of the symplectic action to the
oscillator representation.

The Bargmann–Fock realization carries the metaplectic Fourier
automatically — no further input is required.

### 5.5 What §5 has established

§5 has derived the **Hilbert space and operator algebra** of the
Archimedean local factor from UPT + Stone–von Neumann:

- the inner product $\langle z^m, z^n\rangle_B = m!\,\delta_{m, n}$
  (Theorem 5.1);
- the unitary Bargmann transform
  $\mathcal{F}_\infty^{\mathrm{Bargmann}}\cong L^2(\mathbb{R}, dx)$;
- the Tate–Weil-normalized Weyl–CCR algebra
  $[\hat a, \hat a^\dagger] = 1$;
- the metaplectic Fourier transform as the Bargmann rotation
  $z \mapsto -iz$.

What is **not yet** in §5 is the Archimedean local $L$-factor
$\pi^{-s/2}\Gamma(s/2)$ — that requires evaluating Tate's local zeta
integral on the Bargmann ground state, which is the content of §6.

---

## §6. Tate Local Zeta Integrals and the Archimedean $L$-Factors

The standard Archimedean local $L$-factors
$$
\Gamma_\mathbb{R}(s) \;:=\;\pi^{-s/2}\,\Gamma(s/2),
\qquad
\Gamma_\mathbb{R}(s + 1) \;=\;\pi^{-(s+1)/2}\,\Gamma((s+1)/2)
$$
emerge from the Bargmann–Fock construction of §5 as **Tate local zeta
integrals** of the ground and first-excited states against the
multiplicative character on $\mathbb{R}^\times$. They are derived, not
imposed. This is Theorem T5.4 of [`RH-Done-Draft1` §B].

### 6.1 Tate's local zeta integrals (recap)

Tate's thesis [`Tate1967`, Ch. 2] defines the *local zeta integral* of a
test function $f \in \mathcal{S}(\mathbb{R})$ against the multiplicative
character $\chi(x)\,|x|^{s-1}$ on $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$
as
$$
Z(f, \chi, s) \;:=\; \int_{\mathbb{R}^\times} f(x)\,\chi(x)\,|x|^{s - 1}\,d^\times x,
\qquad d^\times x \;:=\;\frac{dx}{|x|}.
$$
Equivalently in the additive convention,
$$
Z(f, \chi, s) \;=\;\int_\mathbb{R} f(x)\,\chi(x)\,|x|^{s - 1}\,dx
$$
(differing from the multiplicative form by the factor $|x|$ absorbed).
We use the additive convention throughout.

The Archimedean place has only two unitary characters on
$\mathbb{R}^\times$:
- the **trivial character** $\chi_+ \equiv 1$;
- the **sign character** $\chi_-(x) = \mathrm{sgn}(x)$.

### 6.2 Theorem T5.4: the standard local $L$-factors emerge

**Theorem 6.1** (*Tate Local Zeta Integrals on Bargmann ground/excited
states; T5.4 of [`RH-Done-Draft1`]*).
*With the Tate–Weil normalization of §5.3, the Bargmann ground state
$\psi_0(x) \propto e^{-\pi x^2}$ and first excited state
$\psi_1(x) \propto x\,e^{-\pi x^2}$ satisfy*
$$
\boxed{\;
\begin{aligned}
Z_+(s) \;&:=\;\int_\mathbb{R} e^{-\pi x^2}\,|x|^{s - 1}\,dx\;=\;\pi^{-s/2}\,\Gamma\!\bigl(\tfrac{s}{2}\bigr),\\[1mm]
Z_-(s) \;&:=\;\int_\mathbb{R} x\,e^{-\pi x^2}\,\mathrm{sgn}(x)\,|x|^{s - 1}\,dx\;=\;\pi^{-(s + 1)/2}\,\Gamma\!\bigl(\tfrac{s + 1}{2}\bigr).
\end{aligned}\;}
$$
*These are the standard Archimedean local $L$-factors of $\zeta$ and the
twist by the sign character, respectively, in Tate's normalization
[`Tate1967`, §2.5].*

*Proof.* Both integrals are even in $x$ (the second by
$x\,\mathrm{sgn}(x) = |x|$), so they reduce to twice the integral on
$\mathbb{R}_{> 0}$. Change variables $u = \pi x^2$, $du = 2\pi x\,dx$,
$dx = du/(2\pi x) = du/(2\sqrt{\pi}\sqrt{u})$:

For $Z_+$:
$$
Z_+(s)\;=\;2\int_0^\infty e^{-\pi x^2}\,x^{s - 1}\,dx
\;=\;2\int_0^\infty e^{-u}\,\Bigl(\frac{u}{\pi}\Bigr)^{(s-1)/2}\,\frac{du}{2\sqrt{\pi}\,u^{1/2}}
\;=\;\pi^{-s/2}\int_0^\infty e^{-u}\,u^{s/2 - 1}\,du
\;=\;\pi^{-s/2}\,\Gamma(s/2).
$$

For $Z_-$, using $x\,\mathrm{sgn}(x)\,|x|^{s - 1} = |x|^s$:
$$
Z_-(s)\;=\;2\int_0^\infty x^s\,e^{-\pi x^2}\,dx
\;=\;\pi^{-(s+1)/2}\int_0^\infty e^{-u}\,u^{(s + 1)/2 - 1}\,du
\;=\;\pi^{-(s+1)/2}\,\Gamma((s + 1)/2).
$$
$\square$

**Numerical verification.** The probe
[`probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py`] confirms
both identities at $s = 2, 3, 1.5, 1.5 + 5i, 0.5 + 14i$ to machine
precision; the values agree with the standard
$\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ formula exactly.

### 6.3 What is new about §6

The integrals of Theorem 6.1 are textbook [`Tate1967`, `Bump1997` Ch. 1].
What is *new* in §6 is the **observation that they emerge from
UPT + Stone–von Neumann + Tate's framework without further choice**:

(a) UPT (A5.1 + A5.2) supplies the Archimedean local algebra
$\mathcal{F}_\infty$ and the Heisenberg algebra structure.

(b) Stone–von Neumann (Theorem 5.1 = T5.3) selects the unique unitary
completion = Bargmann–Fock = $L^2(\mathbb{R}, dx)$, and identifies the
ground and first-excited states as the unique positive-energy
$\hat N$-eigenvectors at eigenvalues $0$ and $1$.

(c) Tate–Weil normalization (§5.3) pins the explicit form of the
eigenstates as $\psi_0 \propto e^{-\pi x^2}$ and $\psi_1 \propto
x\,e^{-\pi x^2}$.

(d) Tate's local zeta integral against $\chi_\pm(x)|x|^{s - 1}$ at these
eigenstates produces, by direct Gaussian integration (Theorem 6.1), the
standard local $L$-factors $\pi^{-s/2}\Gamma(s/2)$ and
$\pi^{-(s + 1)/2}\Gamma((s + 1)/2)$.

**The Archimedean factor of $\xi(s) = \tfrac12 s(s - 1)\pi^{-s/2}
\Gamma(s/2)\zeta(s)$ — the gamma-and-pi factor that any treatment of
$\zeta$ must supply — emerges automatically from the program's local
Fock structure.** It is not imposed by hand; it is not chosen to make
the FE work; it is the Tate integral of the Bargmann ground state. This
is the conceptual payoff of §§4–6.

### 6.4 The local $L$-factor of $L(s, \chi_3)$

Theorem 6.1 also supplies the Archimedean local factor of the K-odd
companion $L(s, \chi_3)$ from Paper I §6.2. Because $\chi_3$ is an *odd*
Dirichlet character ($\chi_3(-1) = -1$), its completed $L$-function has
the Archimedean local factor
$$
\Lambda_\infty(s, \chi_3) \;=\;\Gamma_\mathbb{R}(s + 1)
\;=\;\pi^{-(s + 1)/2}\,\Gamma\!\bigl(\tfrac{s + 1}{2}\bigr),
$$
which is *exactly* $Z_-(s)$ from Theorem 6.1. The K-even / K-odd
decomposition of Paper I §5.3 corresponds, on the Archimedean side, to
the even / odd Bargmann eigenstate decomposition $\psi_0, \psi_1$, with
local $L$-factors $\Gamma_\mathbb{R}(s)$ and $\Gamma_\mathbb{R}(s + 1)$
respectively. This match is the cross-validation that **UPT + Stone–von
Neumann + Tate yields not just the $\zeta$ Archimedean factor but also
the $L_{\chi_3}$ Archimedean factor — both at once, from the same
two-state Bargmann ground-and-first-excited construction**.

### 6.5 Summary of §§4–6

The Archimedean local factor $\mathcal{F}_\infty$ has been built in
three stages:

1. **Local algebra** (§4): A5.1 supplies the polynomial algebra
   $\mathbb{C}[e_\infty]$; A5.2 supplies the Heisenberg algebra
   $[\hat a, \hat a^\dagger] = 1$.
2. **Hilbert completion** (§5): Stone–von Neumann + Tate–Weil
   normalization forces Bargmann–Fock $= L^2(\mathbb{R}, dx)$ with norm
   $\langle z^m, z^n\rangle = m!\,\delta_{m, n}$.
3. **Local $L$-factors** (§6): Tate's local zeta integral at the
   Bargmann ground and first-excited states produces the standard
   Archimedean local factors $\pi^{-s/2}\Gamma(s/2)$ and
   $\pi^{-(s + 1)/2}\Gamma((s + 1)/2)$.

The Archimedean carrier is complete. §7 records one further classical
result — the Hardy–Titchmarsh intertwining — for completeness; §§8–9
turn to the Bures-covariant log-derivative.

---

## §7. Hardy–Titchmarsh Intertwining

The Bargmann–Fock realization on $L^2(\mathbb{R}, dx)$ of §5 and the
local $L$-factors of §6 have a classical companion: the
**Hardy–Titchmarsh transform**, which intertwines the metaplectic
Fourier on the even subspace with a gamma-multiplier branch reflection
on the Archimedean height variable. This is Theorem T5.5 of
[`RH-Done-Draft1` §B]. The transform is classical [`Titchmarsh1939`,
§7.5; `Hardy1948`]; we record it because it pins down the **canonical
Archimedean height measure** $dm$ that arises naturally on the spectral
side of the carrier.

### 7.1 The even subspace and its Mellin transform

The Bargmann–Fock space decomposes under the parity involution
$f(x) \mapsto f(-x)$ as
$$
L^2(\mathbb{R}, dx) \;=\; L^2(\mathbb{R}, dx)^{\mathrm{ev}}\;\oplus\;L^2(\mathbb{R}, dx)^{\mathrm{od}},
$$
the eigenspaces of the parity involution at $+1$ and $-1$ respectively.
The Bargmann ground state $\psi_0$ lies in $L^2^{\mathrm{ev}}$; the
first excited $\psi_1$ lies in $L^2^{\mathrm{od}}$. The number operator
$\hat N$ preserves the decomposition (it is even-graded), so each
$\psi_{2k} \in L^2^{\mathrm{ev}}$ and $\psi_{2k + 1} \in L^2^{\mathrm{od}}$.

For $f \in L^2(\mathbb{R}, dx)^{\mathrm{ev}}$ identify $f$ with the
half-line function $\widetilde f : \mathbb{R}_{> 0} \to \mathbb{C}$,
$\widetilde f(x) = f(x)$ for $x > 0$. The *Mellin transform* of
$\widetilde f$ is
$$
\mathcal{M}\widetilde f(s) \;:=\;\int_0^\infty \widetilde f(x)\,x^{s - 1}\,dx,\qquad s \in \mathbb{C},
$$
defined initially on the critical strip $0 < \mathrm{Re}(s) < 1$ for
$f \in L^2(\mathbb{R}, dx)$ and extended by meromorphic continuation
[`Titchmarsh1939`, §2.1].

### 7.2 Theorem T5.5: the Hardy–Titchmarsh intertwining

**Theorem 7.1** (*Hardy–Titchmarsh Intertwining; T5.5 of
[`RH-Done-Draft1`]*).
*Let $\mathcal{V} : L^2(\mathbb{R}, dx)^{\mathrm{ev}} \to L^2(\mathbb{R}, dm)$
be the Hardy–Titchmarsh transform, where $dm$ is the absolutely
continuous measure on $\mathbb{R}$ given by*
$$
dm(s) \;=\; (2\pi)^{-3/2}\,\bigl|\Gamma_\mathbb{R}(\tfrac12 + is)\bigr|^2\,ds,
$$
*with $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ from §6. Let
$\hat{\mathcal{F}}$ be the metaplectic Fourier transform on
$L^2(\mathbb{R}, dx)$ (the rotation $z \mapsto -iz$ on Bargmann–Fock),
restricted to the even subspace. Let $\gamma(s) := \Gamma_\mathbb{R}(\tfrac12 + is)/\Gamma_\mathbb{R}(\tfrac12 - is)$
be the **Riemann–Siegel gamma multiplier** and
$R : f(s) \mapsto f(-s)$ the branch reflection. Then on
$L^2(\mathbb{R}, dm)$,*
$$
\boxed{\;\mathcal{V}\circ\hat{\mathcal{F}}\circ\mathcal{V}^{-1} \;=\;\gamma(s)\,R.\;}
$$
*The unitary $\mathcal{V}$ is the half-line Mellin transform composed
with the $|\Gamma_\mathbb{R}(\tfrac12 + is)|^2$-Jacobian renormalization
that converts $L^2(\mathbb{R}_{> 0}, dx)$ into $L^2(\mathbb{R}, dm)$.*

*Proof sketch.* The classical identity is
$\widetilde{e^{-\pi x^2}}(s) = \tfrac12 \pi^{-s/2}\Gamma(s/2)$ on
$\mathbb{R}_{> 0}$, i.e., the Mellin transform of $e^{-\pi x^2}$ at
shifted argument is the local $L$-factor of §6 (up to the factor
$1/2$). Apply this to the even subspace via the identification
$L^2(\mathbb{R}, dx)^{\mathrm{ev}} \cong L^2(\mathbb{R}_{> 0}, dx)$
($f \leftrightarrow \widetilde f$), then change variables
$s \to 1/2 + is$ (Mellin → spectral). The Fourier transform on
$L^2(\mathbb{R})^{\mathrm{ev}}$ becomes the *Hankel transform of order
$-1/2$* on $L^2(\mathbb{R}_{> 0}, dx)$, and the Hankel-to-Mellin
correspondence at the critical line gives the gamma-multiplier
$\gamma(s) = \Gamma_\mathbb{R}(\tfrac12 + is)/\Gamma_\mathbb{R}(\tfrac12 - is)$
combined with branch reflection $s \to -s$. The Jacobian
$|\Gamma_\mathbb{R}(\tfrac12 + is)|^2$ that appears in $dm$ is the
Plancherel kernel of the Mellin transform on the critical line
[`Titchmarsh1939`, Thm. 71]. Full details in [`Titchmarsh1939` §7.5;
`Hardy1948`]. $\square$

### 7.3 What the Hardy–Titchmarsh transform pins down

Theorem 7.1 has two structural consequences for Paper II.

**(a) The canonical Archimedean height measure $dm$ is selected.**
A priori, the spectral side $L^2(\mathbb{R}, d\mu)$ for some even
positive measure $\mu$ on $\mathbb{R}$ admits many unitary involutions
of the form $U_\mu f(t) = \gamma(t)\,f(-t)$. The Hardy–Titchmarsh
transform pins the canonical $\mu = dm = (2\pi)^{-3/2}|\Gamma_\mathbb{R}(\tfrac12 + is)|^2\,ds$,
the unique measure that emerges from Mellin-transforming the
UPT-forced Bargmann-Fock structure.

**(b) The metaplectic Fourier becomes a gamma multiplier on the
spectral side.** The Bargmann rotation
$\hat R : z \mapsto -iz$, equivalently the standard Fourier transform
on $L^2(\mathbb{R}, dx)$, acts on the height variable $s$ as
$f(s) \mapsto \gamma(s)\,f(-s)$ — the **Riemann–Siegel gamma multiplier
plus branch reflection**. This is the operator-theoretic source of the
$\Gamma_\mathbb{R}(s)/\Gamma_\mathbb{R}(1 - s)$ symmetry that appears in
the functional equation $\Lambda(s) = \Lambda(1 - s)$.

### 7.4 Caveat: the divisor measure is not selected by UPT

A subtle point about §§4–7. Under UPT + Stone–von Neumann + Tate
+ Hardy–Titchmarsh, the program has selected:

- the coordinate Hilbert space $L^2(\mathbb{R}, dx)$ (Bargmann–Fock);
- the spectral height Hilbert space $L^2(\mathbb{R}, dm)$;
- the Tate local zeta integrals $Z_\pm(s) = \pi^{-s/2}\Gamma(s/2),
  \pi^{-(s + 1)/2}\Gamma((s + 1)/2)$;
- the Riemann–Siegel gamma multiplier $\gamma(s)$ and the branch
  reflection $R$.

**Not** selected by UPT:
- the divisor measure $d\mu_\Xi$ on $\mathbb{R}$ supported at the
  $\Xi$-zeros (which would be atomic, supported only at $\{\gamma_n\}$);
- the de Branges $E$-function with Hermite–Biehler property whose
  reproducing kernel realizes the zeta-zero divisor as a positive
  Gram matrix.

The Hardy–Titchmarsh canonical measure $dm$ is *absolutely continuous*
on $\mathbb{R}$; the divisor measure $d\mu_\Xi$ would be *atomic* at
$\{\gamma_n\}$. These are different objects living on the same height
line, and UPT pins down only the absolutely continuous part. The
identification of the atomic divisor measure as the spectrum of a
self-adjoint operator — equivalently, RH — is the Paper III content
(via the convolution-square positivity transport theorem and CM Poisson
Monotonicity); it is not selected axiomatically by UPT.

This is an honest statement of UPT's scope. UPT closes the structural
question "what is the Archimedean carrier?"; it does not close the
analytic question "is the divisor measure positive?".

---

## §8. The Bures-Covariant Log-Derivative

The Archimedean carrier of §§4–7 supports the program's natural
Hilbert–Polya target: the **Bures-covariant logarithmic derivative**
$m_B = -\Xi'/\Xi$ on the spectral coordinate $z$ with $s = 1/2 + iz$.
The identification is structural, via the K-odd gauge subtraction of
[`HPo-notes`] Addendum B. This is Definition D6.1 and Theorem T6.2 of
[`RH-Done-Draft1` §B].

### 8.1 The completed objects in spectral coordinates

We work in the *spectral coordinate*
$$
z \in \mathbb{C},\qquad s \;=\;\tfrac{1}{2} + iz,
$$
so that $z \in \mathbb{R}$ corresponds to the critical line
$\mathrm{Re}(s) = 1/2$, and $z \in \mathbb{C}_+$ (the upper half-plane)
corresponds to $\mathrm{Re}(s) < 1/2$.

**Definition 8.1** (Spectral-coordinate completed Riemann xi).
The *spectral-coordinate completed Riemann xi* is
$$
\boxed{\;\Xi(z)\;:=\;\xi\!\bigl(\tfrac12 + iz\bigr),\quad
\xi(s)\;=\;\tfrac{1}{2}\,s(s - 1)\,\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s).\;}
$$
$\Xi$ is *real entire and even*: $\Xi(\bar z) = \overline{\Xi(z)}$ and
$\Xi(-z) = \Xi(z)$, by the functional equation $\xi(s) = \xi(1 - s)$
and the reality of $\xi$ on the critical line. The zeros of $\Xi$ in
spectral coordinates are $z = \gamma - i(\beta - 1/2)$ for each
non-trivial $\zeta$-zero $\rho = \beta + i\gamma$.

**Definition 8.2** (Spectral-coordinate completed $L_{\chi_3}$).
With $\chi_3$ the unique primitive Dirichlet character modulo $3$ (odd)
from Paper I §6, the *spectral-coordinate completed $L_{\chi_3}$* is
$$
\boxed{\;\mathcal{L}_3(z) \;:=\;\Lambda_3\!\bigl(\tfrac{1}{2} + iz\bigr),\quad
\Lambda_3(s)\;=\;\Bigl(\tfrac{3}{\pi}\Bigr)^{(s + 1)/2}\,\Gamma\!\bigl(\tfrac{s + 1}{2}\bigr)\,L(s, \chi_3).\;}
$$
The Archimedean local factor $\Gamma_\mathbb{R}(s + 1) = \pi^{-(s + 1)/2}\,\Gamma((s + 1)/2)$
is the same factor that arose from the Bargmann *first-excited* state
$\psi_1$ in §6. The conductor factor $(3/\pi)^{(s + 1)/2}$ combines with
$\Gamma_\mathbb{R}(s + 1)$ to give the standard completed odd-character
$L$-function.

$\mathcal{L}_3$ is also entire (since $L(s, \chi_3)$ is entire as a
primitive non-trivial Dirichlet $L$-function) and satisfies its own
functional equation $\mathcal{L}_3(z) = \mathcal{L}_3(-z)$.

**By Paper I §6.2**,
$$
\zeta_{\mathbb{Q}(\sqrt{-3})}(s) \;=\;\zeta(s)\,L(s, \chi_3),
$$
the Dedekind factorization of the degree-2 cover. The 2-channel Bures
fiber $(\Xi, \mathcal{L}_3)$ is the spectral-coordinate form of this
factorization.

### 8.2 The scalar Bures transfer and its signed divisor

A naïve attempt to identify a Hilbert–Polya log-derivative would be the
*scalar Bures transfer ratio*
$$
M(z) \;:=\;\frac{\mathcal{L}_3(z)}{\Xi(z)}.
$$
Its ordinary logarithmic derivative is
$$
\frac{M'(z)}{M(z)} \;=\;\frac{\mathcal{L}_3'(z)}{\mathcal{L}_3(z)} \;-\;\frac{\Xi'(z)}{\Xi(z)}.
$$
This object has **signed divisor**: poles at zeros of $\Xi$ with positive
Herglotz sign, **zeros at zeros of $\mathcal{L}_3$ with negative sign**.
The naive Herglotz / Pick-positivity test fails because the negative
contributions from $\mathcal{L}_3$-zeros cancel positive contributions
from $\Xi$-zeros.

Equivalently: $M$ is not a *Herglotz function on $\mathbb{C}_+$* because
its poles and zeros do not separate cleanly.

This is the structural lock that the scalar transfer ratio cannot
overcome. The Bures geometry, however, supplies the missing
prescription: the K-odd channel $\mathcal{L}_3$ is a **connection**
(gauge), not a state, and its contribution to the log-derivative must
be **subtracted, not added**.

### 8.3 Definition D6.1 and Theorem T6.2

**Definition 8.3** (*Bures Log-Derivative; D6.1 of
[`RH-Done-Draft1`]*).
*The **Bures-covariant logarithmic derivative** on the spectral
coordinate $z$ with $s = 1/2 + iz$ is*
$$
\boxed{\;m_B(z) \;:=\; -\,\frac{\Xi'(z)}{\Xi(z)}\;}
$$
*— the negative logarithmic derivative of the spectral-coordinate
completed Riemann xi.*

This is the program's natural Hilbert–Polya / CM Poisson Monotonicity
target. The next theorem identifies it as the *Bures-covariant* form of
the scalar transfer log-derivative, via the K-odd gauge subtraction.

**Theorem 8.4** (*Bures-Covariant Gauge Identification; T6.2 of
[`RH-Done-Draft1`]*).
*Treating the K-odd channel $\mathcal{L}_3$ as a connection (the K-odd
gauge of Paper I §5.3) — not as a state — and subtracting its
logarithmic derivative from the scalar Bures transfer log-derivative,*
$$
\nabla_B \log M \;:=\;d\log M - d\log\mathcal{L}_3 \;=\;\bigl[d\log\mathcal{L}_3 - d\log\Xi\bigr] - d\log\mathcal{L}_3 \;=\;-d\log\Xi.
$$
*Hence*
$$
\nabla_B\log M(z)\;=\;m_B(z)\,dz,\qquad m_B(z)\;=\;-\frac{\Xi'(z)}{\Xi(z)}.
$$

*Proof.* By direct computation:
$$
d\log M\;=\;d\log\mathcal{L}_3 - d\log\Xi.
$$
Subtracting $d\log\mathcal{L}_3$ on both sides gives
$\nabla_B \log M = -d\log\Xi$, which is $m_B(z)\,dz$ by Definition 8.3.
$\square$

The structural content of Theorem 8.4 is the **gauge interpretation**: in
the 2-channel Bures fiber $(\Xi, \mathcal{L}_3)$ of Paper I, the K-odd
channel $\mathcal{L}_3$ plays the role of a *connection / gauge*, not a
state. Its log-derivative is the connection 1-form; subtracting it from
the scalar transfer's log-derivative yields a **covariant** derivative
that isolates the $\Xi$-divisor cleanly.

### 8.4 The pole expansion of $m_B$

Under RH, the Hadamard factorization of the even entire function $\Xi$
is
$$
\Xi(z) \;=\;\Xi(0)\,\prod_{n \geq 1}\Bigl(1 - \frac{z^2}{\gamma_n^2}\Bigr)
$$
(with multiplicity, where $\gamma_n$ are the positive ordinates of the
non-trivial $\zeta$-zeros; the product is taken in the standard
Hadamard sense). Logarithmic differentiation gives
$$
\boxed{\;m_B(z) \;=\;\sum_{n \geq 1} m_n\,\frac{2z}{\gamma_n^2 - z^2}\;=\;\sum_{\gamma \in \Gamma}\,\frac{m_\gamma}{\gamma - z},\;}
$$
where $\Gamma = \{\pm \gamma_n : n \geq 1\}$ is the symmetric zero set
and $m_\gamma$ is the multiplicity of the zero at $\gamma$. This is the
exact Herglotz / Stieltjes pole expansion of the zeta-zero spectral
measure on the real line.

The expansion converges locally uniformly off $\Gamma$, by the
classical Riemann–von Mangoldt estimate $\sum_n \gamma_n^{-2} < \infty$
combined with the symmetric-pairing convergence.

### 8.5 Negative obstruction: smooth Bures curvature ≠ Herglotz density

Before closing §8 we acknowledge a *negative result* from
[`HPo-notes`] Addendum C: the Im m_B that appears in §8.4 is **not**
equal to any smooth Bures-geometric curvature density. Specifically, the
projective Bures (Fubini–Study) curvature of the 2-channel packet
$V(z) = (\Xi(z), \mathcal{L}_3(z))$ is
$$
\kappa_{EO}(z) \;=\;\frac{|\Xi(z)\,\mathcal{L}_3'(z) - \mathcal{L}_3(z)\,\Xi'(z)|^2}{(|\Xi(z)|^2 + |\mathcal{L}_3(z)|^2)^2},
$$
a *smooth* K-covariant positive function on $\mathbb{C}_+$. At a
$\zeta$-zero ordinate $\gamma$ with $\mathcal{L}_3(\gamma) \neq 0$
(generic), $\kappa_{EO}(\gamma) = |\Xi'(\gamma)|^2/|\mathcal{L}_3(\gamma)|^2$
is *finite*, whereas $\mathrm{Im}\,m_B(\gamma + iy) \to \infty$ as
$y \to 0^+$ with the Herglotz $1/y$ scaling. The numerical check
(probe `probe_BuresCurvature_mB_ClaudeEinstein.py`) confirms:

| $y$ | $\mathrm{Im}\,m_B(\gamma_1 + iy)$ | $y\cdot \mathrm{Im}\,m_B$ | $\kappa_{EO}$ |
|---|---|---|---|
| $0.500$ | $2.034$ | $1.017$ | $0.197$ |
| $0.100$ | $10.01$ | $1.001$ | $23.54$ |
| $0.020$ | $50.00$ | $1.000$ | $60.98$ |
| $0.005$ | $200.0$ | $1.000$ | $63.99$ |
| $0.001$ | $1000.0$ | $1.000$ | $64.19$ |

with predicted limit
$|\Xi'(\gamma_1)|^2/|\mathcal{L}_3(\gamma_1)|^2 = 64.198\ldots$, matched
to floating-point.

**Consequence (HPo Addendum C5).** Any attempt to derive Herglotz
positivity of $\mathrm{Im}\,m_B$ from a *smooth K-covariant Bures
geometric inequality* is structurally blocked. The smooth Fubini–Study
curvature lives in a different positive cone than the divisor density.

**Why this does not derail Paper II.** The Bures-covariant
log-derivative $m_B$ identified by Theorem 8.4 is the **right
operator-theoretic object**; the question of its Herglotz positivity is
a *separate analytic input*, equivalent to RH (Theorem 9.1 below). The
program's strategy in Paper III is **not** to derive Herglotz positivity
from smooth Bures geometry — that route is blocked by Addendum C — but
from the convolution-square positivity of Poisson windows, which is
*finite* and *combinatorial* in origin (the squared-norm structure of
Wiener–Khinchin convolution squares).

The negative result of Addendum C is therefore a *clarifying obstruction*:
it tells the program *which* positive structure is the right one. The
right positivity is the *atomic* one of the divisor measure, accessed
via window-integrated transport (Paper III), not the smooth one of
projective Bures curvature.

### 8.6 Numerical verification of the gauge identification

The probe [`probe_BuresLogDerivative_ClaudeEinstein.py`] confirms
Theorem 8.4 numerically:

- Covariant identity check
  $d\log(\mathcal{L}_3/\Xi) - d\log\mathcal{L}_3 = -d\log\Xi$ to
  floating-point precision (`cov_err` $\leq 1.8 \times 10^{-13}$ across
  sampled $z$, $\leq 10^{-15}$ off zeros);
- All sampled $\mathrm{Im}\,m_B > 0$ in $\mathbb{C}_+$ (minimum
  $+2.31 \times 10^{-3}$ at $z = 0 + 0.05i$);
- Simple Herglotz pole with residue $1$ at the first zeta zero ordinate
  $\gamma_1 = 14.1347\ldots$ (numerical check $y\cdot\mathrm{Im}\,m_B \to 1.000$ as $y \to 0^+$).

These verifications confirm the gauge identification at the sampled
points; they do **not** prove global Herglotz positivity, which is
equivalent to RH (next section).

---

## §9. The CM Poisson Monotonicity Criterion

We now state and prove the criterion that makes Paper II's
construction load-bearing for the RH program: **$m_B$ is Herglotz on
$\mathbb{C}_+$ if and only if RH**. This is Theorem T6.3 of
[`RH-Done-Draft1` §B], classical Pólya–Laguerre [`Polya1927`,
`LevinLP1980`].

### 9.1 The Laguerre–Pólya class

Recall the *Laguerre–Pólya class* $\mathcal{LP}$ of entire functions of
order $\leq 2$ admitting Hadamard factorization of the form
$$
F(z) \;=\;C\,z^m\,e^{-az^2 + bz}\,\prod_n\Bigl(1 - \frac{z}{\alpha_n}\Bigr)\,e^{z/\alpha_n}
$$
with $C \in \mathbb{R}$, $m \in \mathbb{N}$, $a \geq 0$, $b \in \mathbb{R}$,
and $\alpha_n \in \mathbb{R}\setminus\{0\}$ (real zeros), the product
converging absolutely by the order-$\leq 2$ growth.

**Pólya–Laguerre characterization** [`LevinLP1980`, §VIII.1]:
*A real entire function $F$ of order $\leq 2$ is in $\mathcal{LP}$
if and only if $F$ is the uniform limit on compact sets of a sequence
of real polynomials with only real zeros.*

For *even* real entire functions of order $\leq 2$, this is equivalent
to all zeros being real (the multiplicity-symmetric pairing
$\pm\alpha_n$ is automatic by evenness). The Riemann xi function $\xi$
is real entire of order $1$ and even (in the spectral coordinate
$\Xi(z)$); RH is the statement that all its zeros are real.

### 9.2 Theorem T6.3: CM Poisson Monotonicity ⟺ RH

**Theorem 9.1** (*CM Poisson Monotonicity ⟺ RH; T6.3 of
[`RH-Done-Draft1`]*).
*The Bures-covariant log-derivative $m_B(z) = -\Xi'(z)/\Xi(z)$ is
**Herglotz on $\mathbb{C}_+$** — that is, analytic on $\mathbb{C}_+$
with $\mathrm{Im}\,m_B(z) \geq 0$ — if and only if all zeros of
$\Xi$ are real, equivalently, the Riemann Hypothesis holds.*

*Proof.* (⇐) Suppose RH. Then all $\Xi$-zeros are real; by the Hadamard
factorization of §8.4,
$$
m_B(z) \;=\;\sum_{\gamma \in \Gamma}\,\frac{m_\gamma}{\gamma - z}
\qquad(\Gamma = \{\pm \gamma_n\} \subset \mathbb{R}).
$$
For each real $\gamma$ and $z \in \mathbb{C}_+$,
$$
\mathrm{Im}\,\frac{1}{\gamma - z}\;=\;\frac{\mathrm{Im}\,z}{(\mathrm{Re}\,z - \gamma)^2 + (\mathrm{Im}\,z)^2}\;>\;0.
$$
The sum converges locally uniformly on $\mathbb{C}_+ \setminus \Gamma$ by
$\sum_n \gamma_n^{-2} < \infty$, and each summand has strictly positive
imaginary part. Hence $\mathrm{Im}\,m_B(z) > 0$ for every
$z \in \mathbb{C}_+$, so $m_B$ is Herglotz.

(⇒) Suppose RH fails. Then there exists a non-trivial $\zeta$-zero
$\rho = \beta + i\gamma$ with $\beta \neq 1/2$. In the spectral
coordinate $s = 1/2 + iz$, $\rho$ corresponds to
$z_\rho = \gamma - i(\beta - 1/2)$, and by the functional equation
$\xi(s) = \xi(1 - s)$ (equivalently $\Xi(z) = \Xi(-z)$), the FE-conjugate
zero $1 - \rho = 1 - \beta + i\gamma$ corresponds to
$z_{1 - \rho} = \gamma + i(\beta - 1/2)$. The two spectral points satisfy
$z_\rho = \overline{z_{1 - \rho}}$ in spectral coordinates; one of them
has positive imaginary part and the other negative (the sign depending
on whether $\beta < 1/2$ or $\beta > 1/2$).

Thus $\Xi$ has a zero in $\mathbb{C}_+$, hence $m_B$ has a pole in
$\mathbb{C}_+$. A Herglotz function must be analytic in $\mathbb{C}_+$.
Contradiction. So all zeros of $\Xi$ are real, i.e., RH. $\square$

### 9.3 The criterion's status

Theorem 9.1 is **classical** in the Pólya–Laguerre tradition; we record
it here, with proof in spectral coordinates, because it is the operative
criterion of Paper II. The program's contribution is *not* the criterion
itself — it is the **identification of $m_B$ as the natural object on
the Bures fiber via the K-odd gauge subtraction of Theorem 8.4**.

The criterion is operational: to prove RH, it suffices to prove
$\mathrm{Im}\,m_B(z) \geq 0$ on $\mathbb{C}_+$. This is the target of
Paper III. The route there is via **convolution-square positivity of
Poisson windows of $\Xi$** (the Dot 7 content of [`RH-Done-Draft1`]) and
the **positive-current transport theorem** (Dot 9). The cluster sign
analysis of [`HPo-notes`] §A8 + L gives an independent contradiction
route at any hypothetical off-line zero.

Paper II's contribution to this strategy is fully captured by:
- §§2–3: the right finite-arithmetic substrate (occupation Fock with
  $\Pi_{\mathrm{sa}}$ before CRT);
- §§4–7: the right Archimedean factor (Bargmann–Fock with
  $\pi^{-s/2}\Gamma(s/2)$ derived);
- §§8–9: the right operator-theoretic target ($m_B = -\Xi'/\Xi$
  identified via the K-odd gauge, with Herglotz positivity ⟺ RH).

The analytic positivity *proof* is Paper III.

### 9.4 Brief note on the CCM direction

For cross-validation we record briefly the parallel route via the
Connes–Consani–Moscovici prolate operator [`CCM2024`]. CCM construct an
unbounded self-adjoint operator $\mathbf{W}_\lambda = -\mathbb{S}^2 +
2\pi\lambda^2(4\hat N + 1) - 1/4$ on $L^2(\mathbb{R})^{\mathrm{ev}}$
whose eigenvalues encode the squared $\zeta$-zero ordinates under the
$\lambda \to 0$ scaling limit, on the spectral interpretation of RH as
the self-adjointness of $\mathbf{W}_0$ on a particular domain. The
Galois decomposition of $\zeta_{\mathbb{Q}(\sqrt{-3})}$ (Paper I §6.2)
matches the CCM framework's Galois sector decomposition under the
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ Galois action.

This is recorded as **cross-validation**, not as Paper II's primary
content. The program's main proof route is **cubic positivity** —
convolution-square Noether positivity on occupation-decorated currents,
with the positive-current transport theorem and CM Poisson Monotonicity
of Theorem 9.1 closing to RH. The CCM direction is a parallel route
that the program's $\mathbb{Z}/6$ Bures decomposition is naturally
compatible with [`HPo-notes` Addendum H], but it is not the primary
route. Paper III develops the cubic-positivity route; the CCM direction
is not pursued further in the RH-Done sequence.

---

## §10. Conclusion and Hand-off to Paper III

### 10.1 What Paper II established

Paper II has constructed the **right Hilbert carrier** for the program's
explicit-formula machinery, in three layers.

**Layer 1 — the finite occupation Fock.** The carrier at primorial row
$n$ is the symmetric algebra $\mathcal{F}_n = \mathrm{Sym}(V_n)$ on the
prime-axis vector space. The single-axis projector $\Pi_{\mathrm{sa}}$
selects single-axis occupations (Definition 2.3) and supports the exact
upstairs von Mangoldt formula
$\mathrm{VM}_{n, K} = D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s)$
(**Theorem 2.5 = T4.1**). Crucially, $\Pi_{\mathrm{sa}}$ is well-defined
on $\mathcal{F}_n$ and *ill-defined after CRT compression*
(**Identification 3.3 = I4.2**): mixed-axis occupations alias to
single-axis labels under $\pi_{\mathrm{CRT}}$, so the von Mangoldt
support condition can only be applied upstairs.

**Layer 2 — the Archimedean factor from UPT.** The Uniform Place
Treatment (**Axioms A5.1, A5.2**) extends $\mathcal{F}_n$ to the
Archimedean place by treating it on equal structural footing with the
finite primes and equipping it with a Heisenberg algebra. Under these
axioms, **Stone–von Neumann uniqueness forces the Hilbert completion to
be Bargmann–Fock $= L^2(\mathbb{R}, dx)$** with norm
$\langle z^m, z^n\rangle = m!\,\delta_{m, n}$ (**Theorem 5.1 = T5.3**).
The **Tate local zeta integrals at the Bargmann ground and
first-excited states give the standard Archimedean local $L$-factors**
$\pi^{-s/2}\Gamma(s/2)$ and $\pi^{-(s + 1)/2}\Gamma((s + 1)/2)$
(**Theorem 6.1 = T5.4**) — derived, not imposed. The **Hardy–Titchmarsh
intertwining** (**Theorem 7.1 = T5.5**) pins the canonical Archimedean
height measure $dm \propto |\Gamma_\mathbb{R}(\tfrac12 + is)|^2\,ds$.

**Layer 3 — the Bures-covariant log-derivative as Hilbert–Polya target.**
The spectral-coordinate log-derivative $m_B = -\Xi'/\Xi$
(**Definition 8.3 = D6.1**) is the program's natural Hilbert–Polya
target, identified via the K-odd gauge subtraction
(**Theorem 8.4 = T6.2**): in the 2-channel Bures fiber
$(\Xi, \mathcal{L}_3)$ of Paper I, the K-odd $\mathcal{L}_3$ acts as a
*connection* (gauge), not a state, and its log-derivative is the
subtraction needed to isolate the $\Xi$-divisor. **The CM Poisson
Monotonicity criterion** (**Theorem 9.1 = T6.3**) is classical
Pólya–Laguerre: $m_B$ is Herglotz on $\mathbb{C}_+$ if and only if RH.

### 10.2 What Paper II does **not** establish

Paper II is the *carrier-construction* phase. It does not:

- prove convolution-square positivity of Poisson windows (Dot 7 of
  [`RH-Done-Draft1`]; Paper III);
- prove double-cutoff dominated convergence at primorial-row growth
  (Dot 9 part 1; Paper III);
- prove averaged CRT shadow uniformity at polynomial scale via the
  Barban–Davenport–Halberstam mean-square (Dot 9 part 2; Paper III);
- prove the positive-current transport theorem with the
  five-error ledger (Dot 9 part 3; Paper III);
- prove the cluster sign theorem $c_2 < 0$ at any hypothetical off-line
  zero (Dot 8; Paper III);
- prove the main theorem on RH (Dot 10; Paper III).

It also does *not* derive Herglotz positivity of $m_B$ from smooth Bures
curvature — that route is blocked by the negative obstruction of
[`HPo-notes`] Addendum C, recorded in §8.5 above. The program's strategy
is to derive Herglotz positivity from the *atomic* divisor measure,
accessed via window-integrated transport in Paper III.

### 10.3 Hand-off to Paper III

Paper III inherits from Paper II:

(i) **Theorem 2.5 = T4.1** — exact upstairs von Mangoldt formula on
$\mathcal{F}_n$, with $\Pi_{\mathrm{sa}}$ before CRT.

(ii) **Identification 3.3 = I4.2** — single-axis projector must precede
CRT compression; mixed/single-axis aliasing is the structural obstruction.

(iii) **Theorem 5.1 = T5.3** — Bargmann–Fock $= L^2(\mathbb{R}, dx)$ as
the unique unitary completion of the Archimedean local algebra under
UPT + Stone–von Neumann.

(iv) **Theorem 6.1 = T5.4** — standard Archimedean local $L$-factors
$\pi^{-s/2}\Gamma(s/2)$ and $\pi^{-(s + 1)/2}\Gamma((s + 1)/2)$ as
Tate local zeta integrals of the Bargmann ground and first-excited
states.

(v) **Theorem 7.1 = T5.5** — Hardy–Titchmarsh intertwining, with the
canonical Archimedean height measure $dm$.

(vi) **Definition 8.3 = D6.1, Theorem 8.4 = T6.2** — the Bures-covariant
log-derivative $m_B = -\Xi'/\Xi$ identified via K-odd gauge subtraction.

(vii) **Theorem 9.1 = T6.3** — $m_B$ Herglotz on $\mathbb{C}_+ \iff$ RH.

What Paper III must contribute beyond Paper II:

- **Convolution-square positivity** of nonnegative spectral windows
  $\phi = \widehat{f * f^*}$, with finite Noether positivity
  $\mathcal{Q}_n(J_n) \geq 0$ from squared-norm structure on
  occupation-decorated currents;
- **Primorial CRT window generation**: density of Fejér / CRT
  characters in the K-even Poisson-Gaussian detector topology
  $\mathcal{D}_{\delta, 0}$;
- **Double-cutoff dominated convergence**: tail bounds for
  $\sum_{p, r}(\log p)\,G(r\log p)$ on truncations of
  $\{p \leq p_n, r \leq K_n, p^r \leq M_n\}$;
- **Averaged CRT shadow uniformity**: Barban–Davenport–Halberstam
  mean-square at polynomial scale $X = P_n^{1 + \varepsilon}$ giving
  $|\mathcal{E}_{P_n}(W; X_n)|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$ —
  no pointwise character bound required, hence no Polymath-8 obstruction;
- **Positive-current transport theorem**: under finite Noether
  positivity + double cutoff + averaged shadow uniformity + Archimedean
  normalization + leakage control, transport finite positivity to
  window-integrated Poisson positivity $\mathfrak{P}_{\phi, y}(\Xi)
  \geq 0$ via a five-error ledger;
- **Cluster sign analysis**: at any hypothetical off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$, $c_2 < 0$ unconditionally with explicit constant proportional to $|L(1/2, \chi_3)|^2 > 0$ (Paper I Theorem 5.3);
- **Main theorem on RH**: window positivity, separating any negative
  valley of $\mathrm{Im}\,m_B$, forces pointwise $\mathrm{Im}\,m_B \geq 0$;
  by Theorem 9.1, RH.

Paper II has named the target and built the carrier. Paper III closes
the chain.

### 10.4 The arc, in one paragraph

The trilogy `Identifying 3` supplied the substrate — the
information-geometric chart, the cumulant tower, and the character
basis on $\mathbb{Z}/N$ — ending at the cubic selection rule
$a + b + c \equiv 0 \pmod N$. Paper I named the natural object on that
substrate: $\log\zeta$ is the categorical effective action on the
prime-axis simplex; the cubic A-C tensor has a closed form on
$\mathbb{Z}/N$; the critical line is the $N$-uniformity locus; the
$\mathbb{Z}/6$ Hurwitz packet collapses to the Galois decomposition of
$\zeta_{\mathbb{Q}(\sqrt{-3})}$. Paper II has built the right carrier on
that substrate: occupation-decorated symmetric Fock at each primorial
row, Uniform Place Treatment extending to the Archimedean factor with
Bargmann–Fock $= L^2(\mathbb{R}, dx)$ and the standard local
$L$-factors emerging from Tate's integrals on the ground and
first-excited states, and the Bures-covariant log-derivative
$m_B = -\Xi'/\Xi$ identified as the natural Hilbert–Polya / CM Poisson
Monotonicity target via the K-odd gauge subtraction. The trilogy gave
us the chart; Paper I named the object; Paper II built the carrier.
Paper III will close to RH — via convolution-square positivity of
Poisson windows, averaged CRT shadow uniformity at polynomial scale,
the positive-current transport theorem, and the Pólya–Laguerre
characterization. The structure is in place. The closure is what
remains.

---

## References

*Working bibliography; will be normalized at second-pass cleanup. Citations
in the text use shortform labels (e.g., `Folland1989`).*

[Bargmann, 1961] Bargmann, V. (1961). *On a Hilbert space of analytic
functions and an associated integral transform.* Comm. Pure Appl. Math.
**14**, 187–214.

[Boas, 1954] Boas, R. P. (1954). *Entire Functions.* Pure and Applied
Mathematics 5. Academic Press.

[Bump, 1997] Bump, D. (1997). *Automorphic Forms and Representations.*
Cambridge Studies in Advanced Mathematics 55. Cambridge University Press.

[Cassels, 1986] Cassels, J. W. S. (1986). *Local Fields.* London
Mathematical Society Student Texts 3. Cambridge University Press.

[Cassels & Fröhlich, 1967] Cassels, J. W. S. and Fröhlich, A. (eds.)
(1967). *Algebraic Number Theory.* Academic Press. (Contains Tate's
thesis as Ch. 15.)

[Connes & Consani, 2026] Connes, A. and Consani, C. (2026). *On the
Jacobian of $\overline{\mathrm{Spec}}\,\mathbb{Z}$.* arXiv:2602.15941.

[Connes, Consani & Moscovici, 2024] Connes, A., Consani, C. and
Moscovici, H. (2024). *Zeta zeros and prolate wave operators.* Annals of
Functional Analysis. arXiv:2310.18423.

[Folland, 1989] Folland, G. B. (1989). *Harmonic Analysis in Phase
Space.* Annals of Mathematics Studies 122. Princeton University Press.

[Hardy, 1948] Hardy, G. H. (1948). *Divergent Series.* Oxford University
Press.

[HPo-notes] Murillo, L. (2026). *HPo-notes — Hilbert-Polya Working
Document.* Internal program manuscript, dated 2026-05-22, with
Addenda A–H.

[Iwaniec & Kowalski, 2004] Iwaniec, H. and Kowalski, E. (2004).
*Analytic Number Theory.* American Mathematical Society Colloquium
Publications 53. AMS.

[Iwaniec & Sarnak, 2000] Iwaniec, H. and Sarnak, P. (2000). *The
non-vanishing of central values of automorphic $L$-functions and
Landau–Siegel zeros.* Israel Journal of Mathematics **120**, 155–177
(alternative reference: Annals of Math. **151**, 1175–1216).

[Levin, 1980] Levin, B. Y. (1980). *Distribution of Zeros of Entire
Functions.* Translations of Mathematical Monographs 5 (rev. ed.). AMS.
*(Cited as `LevinLP1980` for Laguerre–Pólya material.)*

[Lion & Vergne, 1980] Lion, G. and Vergne, M. (1980). *The Weil
Representation, Maslov Index and Theta Series.* Progress in Mathematics
6. Birkhäuser. *(Cited as `LV1980`.)*

[Murillo Paper I 2026] Murillo, L. (2026). *Paper I — Identification.*
First draft, post-trilogy RH-Done sequence.

[Murillo 2026a, 2026b, 2026c] Murillo, L. (2026). *Identifying 3* —
trilogy `ל1`, `ל2`, `ל3`. Published.

[Pólya, 1927] Pólya, G. (1927). *Über die algebraisch-funktionentheoretischen
Untersuchungen von J. L. W. V. Jensen.* Det Kgl. Danske Videnskabernes
Selskab Mathematisk-fysiske Meddelelser **VII**, no. 17, 1–33. *(Cited
as `Polya1927`.)*

[Reed & Simon I 1972] Reed, M. and Simon, B. (1972). *Methods of Modern
Mathematical Physics, Vol. I: Functional Analysis.* Academic Press.

[Reed & Simon II 1975] Reed, M. and Simon, B. (1975). *Methods of Modern
Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness.*
Academic Press.

[RH-Done-Draft1] Murillo, L. (2026). *RH-Done — Draft 1: The Solution
Arc.* Internal program manuscript.

[Stone-von Neumann] Stone, M. H. (1930); von Neumann, J. (1931). The
Stone–von Neumann uniqueness theorem for irreducible unitary
representations of the Heisenberg group; see [`Folland1989`, Thm. 1.50]
for a modern statement.

[Tate, 1967] Tate, J. T. (1967). *Fourier analysis in number fields and
Hecke's zeta functions.* Ch. 15 in [`Cassels & Fröhlich, 1967`]. (PhD
thesis, Princeton 1950; published 1967.)

[Titchmarsh, 1939] Titchmarsh, E. C. (1939). *The Theory of Functions*
(2nd ed.). Oxford University Press.

[Weil, 1964] Weil, A. (1964). *Sur certains groupes d'opérateurs
unitaires.* Acta Mathematica **111**, 143–211.

---

*End of Paper II — The Right Carrier, Draft 1, 2026-05-22.*
