# N15 — The Two Potentials of the Weil Form

## From the Euler Product to the $\tau=1$ Closure

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — June 8, 2026*

<!--
Program record (not part of the paper). Fifteenth paper of the Numbers (N-) series. It does NOT prove the
Riemann Hypothesis and does not claim to. It is a consolidation paper: it assembles the archimedean and
prime contributions of the Weil explicit-formula functional into two explicit convex potentials in one
common currency (relative entropy / log-partition), and follows the difference of those potentials through
a chain of exact computations down to the single residual it cannot cross. The chain: (1) both potentials
as convex/relative-entropy objects [N14 + the zeta-distribution log-partition]; (2) the functional-equation
reflection realizes the difference as the Laguerre-Polya log-concavity hierarchy; (3) order 2 (Fisher) is
separable in the two potentials, order 4 first couples them, and -- a refuted hypothesis -- higher orders
do NOT sharpen single-zero detection; (4) the de Bruijn-Newman flow shows the local order-2 margin is a
positive-measure moment, blind to the constant Lambda; (5) the residue is therefore global -- the Montgomery
pair-correlation / GUE form factor, whose ramp (tau<1) is proven (Lambda>=0, Rodgers-Tao) and whose plateau
(tau>1) is the Hardy-Littlewood prime off-diagonal, equivalent to RH. Honest tiering: every step is an exact
certificate except the final tau=1 closure, which is RH. Certificates (mpmath/sympy, no torch), all GREEN,
under empirical/p_infinity/: probe_archimedean_relative_entropy.py, probe_prime_side_bregman_logzeta.py,
probe_dc_reflection_laguerre.py, probe_order4_laguerre_interaction.py, probe_debruijn_newman_two_potential.py,
probe_montgomery_formfactor_two_potential.py, probe_toland_dual_signpreserving.py (sec 3.1, A.7: the
Toland-Singer dual is an exact SIGN-PRESERVING identity -- a new equivalent face, not a closure; m is
transform-invariant, the Omega_inf(0)<0 local negativity is sign(m)-irrelevant), and probe_tau1_crossing_vs_phase_transition.py
(Remark 7.2, A.8: the tau=1 corner is a Legendre phase transition, NOT a conformal-bootstrap/resurgent Stokes
line -- K has no tau->1/tau modular symmetry, iota=F^2 acts as channel-preserving evenness not a channel-
exchanging Stokes automorphism, the (-1)^n per-prime series is Borel-SUMMABLE with pole at z=-phi(p)<0; the
semiclassical Berry / Bogomolny-Keating plateau is HL-conditional, so crossing symmetry does NOT bypass the
off-diagonal summation), and probe_toland_barrier_margin.py (sec 3.2, A.9: the Singer barrier half of 3.1 --
the dual margin mu(nu)=lambda_min(M_A+M_pole-M_P,G) collapses 1.5e-3->1e-11 across support threshold nu*~1.2
= dual-cone image of tau=1; gate: matrix form = sum over 400 zeros to 1e-10; kappa>1 drives mu<0. Marginal
branch, no held floor). Internal references used
as THEOREMS only: T0 (Thm 2.7), N4, N5, N9, T15, N14. RH stays [C] throughout, never promoted.
-->

---

> **Status (read first).** This is an *expository* note, not a research contribution, and it does not reduce or prove the Riemann Hypothesis. Every link in its chain is an established equivalence or theorem (Weil 1952; Pólya / Csordas–Varga; de Bruijn–Newman / Rodgers–Tao 2020; Montgomery 1973; Goldston–Montgomery 1987; Bombieri–Vinogradov; Bettin–Chandee / Fouvry–Radziwiłł), and **no bound is improved** — the chain arrives at the known frontier $\theta\approx0.515$ without advancing it. Assembling Riemann-Hypothesis equivalences into one picture is itself a documented activity (Broughan, *Equivalents of the Riemann Hypothesis*, 2 vols., CUP 2017). The note's only offering is a unifying information-geometric *lens* on these known facts. The cumulant reformulation of the Laguerre hierarchy is also prior art (Nuttall 2013).
>
> *Two convex potentials, one subtracted from the other, agreeing at every order until the boundary $\tau=1$, where local analysis ends and arithmetic begins.*

---

## Abstract

The Riemann–Weil explicit-formula functional is a sum of an archimedean term and a prime term. We show that **both** terms are explicit convex potentials in a single information-geometric currency: the archimedean term is a relative entropy [N14], and the prime term is the log-partition function $\log\zeta(s)$ of the *zeta distribution* $P_s(n)=n^{-s}/\zeta(s)$, whose convexity is Cauchy–Schwarz and whose additivity over primes is exactly the Euler product. The Weil functional is therefore a **difference of convex potentials**, trivially signed on $\Re s>1$ (the Euler product has no zeros there) and equal to the Riemann Hypothesis precisely as the statement that the archimedean potential dominates the prime potential under continuation to the critical line. We then follow this difference, through a sequence of exact computations, to the single obstruction it cannot pass. The functional equation's reflection $s\leftrightarrow 1-s$ realizes the difference as the Laguerre–Pólya log-concavity hierarchy of $\Xi(t)=\xi(\tfrac12+it)$; the second-order rung (the first Laguerre inequality, $\log|\Xi|$ concave) is separable in the two potentials, and — correcting a natural expectation — the higher Laguerre rungs are *less* sensitive to off-line zeros, not more. The de Bruijn–Newman heat flow, in Cole–Hopf (Burgers) form, shows that the local second-order margin is a moment of a positive measure, monotone in the flow parameter and **blind to the de Bruijn–Newman constant $\Lambda$**. The residue is thus genuinely global: the Montgomery pair-correlation / GUE form factor $K(\tau)=\min(|\tau|,1)$, whose ramp ($\tau<1$) is proven (equivalently $\Lambda\ge0$, Rodgers–Tao) and whose plateau ($\tau>1$) is the Hardy–Littlewood prime off-diagonal — whose per-prime weight $1/\varphi(p)^2$ is the program's exact order-two conductor cumulant, and whose closure across $\tau=1$ is the Riemann Hypothesis. We do not prove that closure. The chain is an **expository synthesis**: every individual link — Weil positivity, the Laguerre–Pólya hierarchy, the de Bruijn–Newman flow, Montgomery pair correlation, Goldston–Montgomery, the level of distribution — is an established equivalence or theorem, and no bound is improved (the chain arrives *at* the known frontier $\theta\approx0.515$, it does not advance it). The aim is a single information-geometric lens that displays these known facts as one picture, not a new reduction of the Riemann Hypothesis.

**MSC 2020.** 11M26, 11M06, 60G55, 94A17, 33B15.

**Keywords.** Weil explicit formula, relative entropy, log-partition function, Euler product, difference of convex functions, Laguerre–Pólya class, de Bruijn–Newman constant, Cole–Hopf, Montgomery pair correlation, GUE form factor, Hardy–Littlewood singular series.

---

## 1. Introduction

### 1.1 Two terms, one currency

Weil's positivity criterion writes the Riemann Hypothesis as the non-negativity of an explicit Hermitian functional. For an even test function the functional decomposes as
$$
W(f)\;=\;\underbrace{W_\infty(f)}_{\text{archimedean}}\;+\;\underbrace{W_{\mathrm{pole}}(f)}_{\text{poles}}\;-\;\underbrace{W_{\mathrm{prime}}(f)}_{\text{primes}} .
$$
The archimedean term comes from the local factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ at the real place; the prime term is the sum over prime powers weighted by the von Mangoldt function. These two terms are usually treated as objects of different kinds — one transcendental and analytic, one arithmetic and discrete. The thesis of this paper is that they are **the same kind of object**: each is an explicit *convex potential*, and the Weil functional is their difference.

This is not a formal analogy. The companion paper [N14] proves that the archimedean term is exactly a relative entropy. Here we show (Section 2) that the prime term is the log-partition function of a probability distribution on the integers, convex for an elementary reason, additive over primes for exactly the reason the Euler product holds. Once both terms live in one currency, the Riemann Hypothesis becomes a clean inequality between two convex functions — a *difference-of-convex* statement (Section 3) — and one can ask the sharp question: how far can one follow that difference before genuinely new input is required, and what is the input?

### 1.2 The picture: known equivalences in one lens

We follow the difference through five computations, each verifying a *known* equivalence, and arrive at the known residual. The route is:

1. **Both potentials (Section 2).** Archimedean $=$ relative entropy [N14]; prime $=\log\zeta$, the convex, Euler-separable log-partition of the zeta distribution.
2. **Difference of convex (Section 3).** $W$ is convex minus convex; trivially signed on $\Re s>1$; RH $=$ domination under continuation.
3. **Reflection and concavity (Section 4).** The functional equation's reflection turns the difference into the Laguerre–Pólya log-concavity hierarchy of $\Xi$. The second-order rung is separable in the two potentials.
4. **Order four — two cautions (Section 5).** The apparent fourth-order "coupling" of the two potentials is an algebraic artifact (squaring an additive cumulant), with no arithmetic content; and, contrary to a natural expectation, higher Laguerre rungs are less sensitive to isolated off-line zeros, not more. The lever is order two, not beyond.
5. **The local ceiling (Section 6).** In de Bruijn–Newman / Cole–Hopf form, the local second-order margin is a moment of a positive measure — monotone in the flow and blind to the constant $\Lambda$.

The residue (Section 7) is therefore global: the Montgomery pair-correlation form factor at the boundary $\tau=1$. Its ramp is proven; its plateau is the Hardy–Littlewood prime off-diagonal, equal to RH. Section 8 lays out the picture; Section 9 states honestly what is and is not achieved.

Every step is backed by a deterministic exact-arithmetic certificate (Appendix A). The one thing we do not do is cross $\tau=1$; that is the Riemann Hypothesis.

### 1.3 Standing on theorems

We use established results only. From the companion series: the relative-entropy identity for the archimedean term [N14, building on T0 Theorem 2.7]; the apex–archimedean operator identification [N4], [N5]; the finite-to-archimedean completion [T15]; the cross-prime fusion / Davenport–Heilbronn analysis [N9]. The classical inputs are the explicit formula (Weil), the zeta distribution (Golomb), the Laguerre–Pólya theory (Pólya; Csordas–Varga), the de Bruijn–Newman constant (de Bruijn; Newman; Rodgers–Tao $\Lambda\ge0$; Polymath15 $\Lambda\le0.2$), Montgomery's pair correlation, and the Hardy–Littlewood singular series with the Goldston–Montgomery equivalence. None of our conclusions rests on a conjecture of the cited papers; the Riemann Hypothesis itself is the only conjectural statement and it appears only as the named residual.

---

## 2. The two potentials

### 2.1 The archimedean potential is a relative entropy

We recall the result of [N14]. The archimedean Weil functional $W_\infty$ is, exactly, the relative entropy of the time–frequency concentration of the test function from its maximum-entropy reference,
$$
W_\infty(f)\;=\;D\!\left(P_f\,\Vert\,u\right)\;\ge\;0,
$$
with equality at the self-dual configuration. Its non-negativity is Gibbs' inequality, and its convexity descends from the logarithmic convexity of $\Gamma_{\mathbb R}$. The positivity is non-trivial: the archimedean density $\Omega_\infty(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}{2})-\log\pi$ is negative near $r=0$ (with $\Omega_\infty(0)=-5.3721834\ldots$), so the positivity is a global, entropic fact, not the positivity of a kernel (certified: Appendix A.1).

### 2.2 The prime potential is a log-partition function

We now exhibit the prime term as a convex potential of the same kind. Put the Gibbs measure on the positive integers,
$$
P_s(n)\;=\;\frac{n^{-s}}{\zeta(s)},\qquad s>1,
$$
the **zeta distribution** (Golomb). Then $\zeta$ is its partition function and
$$
\Phi(s)\;:=\;\log\zeta(s)
$$
is the log-partition function (cumulant generating function) of the statistic $\log n$. Two elementary facts make $\Phi$ a genuine convex potential.

**Proposition 2.1 (convexity).** *$\Phi=\log\zeta$ is convex on $(1,\infty)$, with*
$$
\Phi''(s)\;=\;\frac{\zeta''(s)}{\zeta(s)}-\left(\frac{\zeta'(s)}{\zeta(s)}\right)^2\;=\;\operatorname{Var}_{P_s}(\log n)\;\ge\;0 .
$$
*Proof.* $\zeta''\zeta-(\zeta')^2=\big(\sum(\log n)^2 n^{-s}\big)\big(\sum n^{-s}\big)-\big(\sum(\log n)n^{-s}\big)^2\ge0$ by Cauchy–Schwarz; this is the variance of $\log n$ under $P_s$, the Fisher information of the family. $\square$

Moreover $\Phi'(s)=\zeta'/\zeta(s)=-\sum_{n}\Lambda(n)\,n^{-s}$, so **the prime term of the Weil functional is generated by the first derivative of $\Phi$**: the von Mangoldt content is $-\Phi'$.

### 2.3 The Euler product is separability

The decisive structural fact is that this convex potential is *additive over primes*, and that additivity is the Euler product. Factoring $n$ by its prime exponents $n=\prod_p p^{k_p}$, the energy $\log n=\sum_p k_p\log p$ is separable, so under $P_s$ the exponents $\{k_p\}$ are **independent geometric variables**, and
$$
\Phi(s)=\log\zeta(s)=\sum_p\big[-\log(1-p^{-s})\big],\qquad
\Phi''(s)=\sum_p(\log p)^2\frac{p^{-s}}{(1-p^{-s})^2},
$$
with no cross-prime covariance. In the language of [T0, Theorem 4.7] (analysis-of-variance separability) and [N9] (cross-prime fusion closure), this independence is precisely the Euler product, and it is the invariant that distinguishes $\zeta$ from a Dirichlet series with a functional equation but off-line zeros (the Davenport–Heilbronn function fails it, with cross-prime defect $\approx1.081$; certified in [N9] and re-certified here, Appendix A.2). Finally, the conjugate potential is a relative entropy between zeta distributions,
$$
D\!\left(P_{s_1}\Vert P_{s_2}\right)=\Phi(s_2)-\Phi(s_1)-\Phi'(s_1)(s_2-s_1)\;\ge\;0 ,
$$
the exact prime-side analogue of the archimedean relative entropy of Section 2.1 (certified: Appendix A.2).

---

## 3. The Weil functional as a difference of convex potentials

We can now state the structure that organizes the rest of the paper.

**Theorem 3.1 (difference of convex potentials).** *Both terms of the Weil functional are convex potentials in the relative-entropy currency: the archimedean term is $D_{\mathrm{arch}}$ (Section 2.1) and the prime term is the convex log-partition $\Phi=\log\zeta$ (Section 2.2). Schematically,*
$$
W\;=\;D_{\mathrm{arch}}\;-\;\Phi_{\mathrm{prime}},
$$
*a difference of convex functions. On $\Re s>1$ the Euler product is non-vanishing, so the difference is trivially signed there (no zeros, no difficulty). The Riemann Hypothesis is the statement that the archimedean potential dominates the prime potential under analytic continuation to the critical line $\Re s=\tfrac12$.*

This is the crux that the rest of the paper exploits. A single convex potential is unconditionally signed (Gibbs). A *difference* of convex potentials is not, and its sign is exactly the open content. The Euler product (Section 2.3) certifies the prime potential as a genuine, separable, convex object — which is what makes "difference of convex" precise rather than metaphorical. The remaining sections ask how far the difference can be followed toward the critical line.

### 3.1 The Toland–Singer dual: an equivalent face

A difference of convex potentials carries a canonical dual. By **Toland–Singer duality** [To] (which requires only the *subtracted* potential to be convex, lower-semicontinuous and proper),
$$
m\;:=\;\inf_f\big(D_{\mathrm{arch}}(f)-\Phi_{\mathrm{prime}}(f)\big)\;=\;\inf_\xi\big(\Phi_{\mathrm{prime}}^\ast(\xi)-D_{\mathrm{arch}}^\ast(\xi)\big).
$$
The conjugates exchange the two registers of Section 2: $\Phi_{\mathrm{prime}}^\ast$ is the **prime relative entropy** — the Bregman divergence of $\log\zeta$ between zeta distributions (Section 2.3) — and $D_{\mathrm{arch}}^\ast$ is the **archimedean log-partition**, the conjugate of the archimedean relative entropy (Section 2.1). The transform thus *swaps which place carries the entropy and which carries the log-partition*: the primal "archimedean entropy minus prime log-partition" becomes the dual "prime entropy minus archimedean log-partition." This symmetric swap is a genuinely distinct presentation of the same content, and we record it as such — with two cautions that fix its status (certified, Appendix A.7).

**Proposition 3.2 (sign invariance).** *The optimal value $m=\inf_f(D_{\mathrm{arch}}-\Phi_{\mathrm{prime}})$ is invariant under the Toland transform: the primal and dual infima are equal. Hence the Riemann Hypothesis ($m\ge0$) holds for the dual if and only if it holds for the primal; the transform cannot manufacture positivity. If RH is false ($m<0$), the dual infimum is equally negative.*

**Remark 3.3 (the local negativity is not the obstruction).** One might hope the dual "integrates out" the pointwise negativity of the archimedean density near $r=0$ ($\Omega_\infty(0)=-5.37\ldots$). It does not — because that negativity was never the obstruction. As established in [N14, §1.2], the positivity of $W_\infty$ is a *global, entropic* fact, not the positivity of a kernel; the sign of $m$ is a global property of the difference, carried across the transform verbatim. The Toland dual *relocates* the difficulty — to the uniform domination of the archimedean log-partition by the prime entropy on the dual side — but does not reduce it. The single hand-off is still at $\tau=1$ (Section 7).

The certificate (A.7) verifies the Toland identity to machine zero on closed-form quadratic potentials across $m>0$, $m=0$, $m<0$, and to $\sim 10^{-42}$ on the two finite $\mathbb Z/6$ ledgers of [N14] (archimedean $\log k$; prime-counting), exhibiting the entropy $\leftrightarrow$ log-partition swap explicitly. The dual is a new face of the residual; it is not a crossing of it.

### 3.2 The Singer barrier: the dual margin collapses at the support threshold

Proposition 3.2 closes the hope of *transporting* $m$. Its constructive counterpart is the dual **barrier**, and it is worth recording because it is the right register for a difference-of-convex infimum. Such an infimum is not located by a descending flow — the de Bruijn–Newman / Cole–Hopf flow of Section 6 is exactly such a flow, and Proposition 6.1 shows it is blind to $\Lambda$. It is located by a barrier: a tractable convex minorant $\psi\le W$ whose own infimum certifies a floor, $\inf\psi>0$. In the dual register of §3.1 the barrier is the pointwise inequality
$$
\text{RH}\quad\Longleftrightarrow\quad \Phi_{\mathrm{prime}}^\ast(\xi)\;\ge\;D_{\mathrm{arch}}^\ast(\xi)\quad(\forall\,\xi),
$$
the prime relative entropy dominating the (explicit, transition-free) archimedean log-partition; a barrier is any tractable convex minorant of $\Phi_{\mathrm{prime}}^\ast$ that clears $D_{\mathrm{arch}}^\ast$ by a margin.

The primal realization of that margin is concrete. For test functions of frequency support $[-\nu,\nu]$ the tightest convex (quadratic) certificate is the smallest generalized eigenvalue of the explicit-formula quadratic form,
$$
\mu(\nu)\;:=\;\min_{\operatorname{supp}\widehat\varphi\subset[-\nu,\nu]}\frac{W(\varphi)}{\lVert\varphi\rVert^2}\;=\;\lambda_{\min}\!\big(M_A+M_{\mathrm{pole}}-M_P,\;G\big),
$$
with $M_A$ the archimedean Gram (the density $\Omega_\infty$ of §2.1), $M_P$ the prime Gram (the von Mangoldt kernel of §2.2), $M_{\mathrm{pole}}$ the rank-two pole term, and $G$ the $L^2$ Gram. Since $W(\varphi)=\sum_\rho|\widehat\varphi(\gamma_\rho)|^2$, the form is non-negative under RH, and $\mu(\nu)\ge0$ is the support-$\nu$ shadow of the Riemann Hypothesis. The barrier proposal is exactly the question whether $\mu(\nu)$ stays bounded away from $0$.

It does not. On a frequency-reaching Gaussian-bump cone (certified A.9; the assembled form agrees with the direct sum over the first $400$ zeros to $\sim10^{-10}$, so it is genuinely $\sum_\rho|\widehat\varphi(\gamma_\rho)|^2$), the margin carries a small positive floor only while the support is too short to reach the primes, and that floor **collapses by eight orders of magnitude** as the support crosses a threshold $\nu_\star\approx1.2$:

| $\nu$ | $0.5$ | $0.9$ | $1.2$ | $1.5$ | $2.0$ | $3.0$ | $3.6$ |
|---|---|---|---|---|---|---|---|
| $\mu(\nu)$ | $1.5\!\times\!10^{-3}$ | $2.2\!\times\!10^{-3}$ | $5.8\!\times\!10^{-6}$ | $1.7\!\times\!10^{-6}$ | $6.9\!\times\!10^{-8}$ | $1.2\!\times\!10^{-11}$ | $\sim 0$ |

The threshold $\nu_\star$ is the support at which the autocorrelation $\varphi\star\widetilde\varphi$ first reaches the low prime powers $\log 2,\log 3$ — the support at which $M_P$ turns on. Below $\nu_\star$ the form is unconditionally positive because the test cone cannot sample the primes (the band-limited / Bombieri regime); above it the dual margin sits on the knife-edge. A control scaling $M_P\mapsto\kappa M_P$ confirms $\mu$ is a genuine archimedean-versus-prime domination margin: at $\kappa=1$ it is the knife-edge value, and prime over-weight $\kappa>1$ drives it sharply negative ($M_P$ is indefinite — the autocorrelation at non-zero lag is sign-indefinite — so $\mu(\kappa)$ is not monotone; the load-bearing fact is the sign break at $\kappa>1$).

This is the constructive companion to Proposition 3.2: the bare transform cannot move the sign of $m$, and the Singer relaxation cannot stand a floor under it. A valid convex minorant obeys $\inf\psi\le m$, and once the support is rich enough to feel the primes the truth $m$ is itself the knife-edge — so no honest barrier is bounded away from zero past $\nu_\star$. The collapse threshold is the dual-test-cone image of the corner $\tau=1$ of Section 7: the support at which the archimedean diagonal $M_A$ ceases to dominate alone and the prime off-diagonal $M_P$ must be summed. A held floor past $\nu_\star$ would require precisely the uniform individual repulsion bound of Section 7 — the level-of-distribution input — which is the open content itself, not a relaxation of it.

---

## 4. The reflection and the Laguerre hierarchy

### 4.1 Reflection turns the difference into log-concavity

The completed zeta function satisfies $\xi(s)=\xi(1-s)$. In the critical-line variable $\Xi(t):=\xi(\tfrac12+it)$, the reflection $s\leftrightarrow1-s$ is $t\leftrightarrow-t$: $\Xi$ is real and even, and the critical line is the fixed set of the reflection. The Riemann Hypothesis is the statement that $\Xi$ has only real zeros, i.e. $\Xi$ lies in the Laguerre–Pólya class.

The second-order shadow of that class is the first **Laguerre inequality**
$$
L_1[\Xi](t)\;=\;\Xi'(t)^2-\Xi(t)\Xi''(t)\;=\;-\,\Xi(t)^2\,(\log|\Xi|)''(t)\;\ge\;0\qquad(\forall\,t\in\mathbb R),
$$
equivalently *$\log|\Xi|$ is concave*. This is the reflection-symmetric, difference-of-convex condition: the archimedean concavity must dominate the prime convexity to keep $\log|\Xi|$ concave. It is verified across the first zeros (Appendix A.3) and is non-vacuous: a single off-line zero pair forces $L_1<0$ in a neighborhood (the toy $\Xi=t^2+b^2$ gives $L_1=2(t^2-b^2)<0$ for $|t|<b$).

### 4.2 The two potentials inside the condition

The condition factors exactly through the two potentials. Writing $\Xi=A\cdot\zeta_{\mathrm{line}}$ with $A$ the archimedean factor and $\zeta_{\mathrm{line}}(t)=\zeta(\tfrac12+it)$,
$$
L_1[\Xi]\;=\;L_1[A]\,\zeta_{\mathrm{line}}^2+A^2\,L_1[\zeta_{\mathrm{line}}],
\qquad\text{equivalently}\qquad
(\log|\Xi|)''=(\log|A|)''+(\log|\zeta_{\mathrm{line}}|)'' .
$$
The second form is the cleanest statement of domination at second order: the archimedean concavity $(\log|A|)''$ versus the prime curvature $(\log|\zeta_{\mathrm{line}}|)''$. Pointwise it is a genuine inequality (e.g. at $t=5$, archimedean $-0.0673$ against prime $+0.0144$, net $-0.0529$; certified A.3), and it is the order-two form of the N14/N5 archimedean domination.

### 4.3 The cumulant form

It is convenient to write the rungs in cumulant variables. With $m_k=\Xi^{(k)}/\Xi$ and the cumulants $c_k=(\log\Xi)^{(k)}$ (so $c_2=m_2-m_1^2$, $c_4=m_4-4m_1m_3-3m_2^2+12m_1^2m_2-6m_1^4$),
$$
\frac{L_1[\Xi]}{\Xi^2}=-c_2\ge0,\qquad \frac{L_2[\Xi]}{\Xi^2}=2c_4+12c_2^2\ge0 .
$$
The Riemann Hypothesis is thus, in this register, the full hierarchy of cumulant inequalities on the critical line, of which $-c_2\ge0$ (log-concavity, $\equiv$ the Fisher rung) is the second-order member.

---

## 5. Order four: two cautions (an algebraic artifact and a refuted hypothesis)

The cumulants are additive over the product $\Xi=A\zeta_{\mathrm{line}}$ at **every** order — $c_k(\Xi)=c_k(A)+c_k(\zeta_{\mathrm{line}})$ for all $k$, because $\log\Xi$ is literally a sum (certified to $10^{-41}$, A.4). This section records two cautions against over-reading that fact at fourth order.

**Proposition 5.1 (the order-four "coupling" is an algebraic artifact, not a structural feature).** *The second-order rung is the additive $L_1/\Xi^2=-(c_2^A+c_2^\zeta)$. The fourth-order rung $L_2/\Xi^2=2c_4+12c_2^2$ is **quadratic** in $c_2$; substituting the additive $c_2=c_2^A+c_2^\zeta$ and expanding the square gives*
$$
\frac{L_2}{\Xi^2}=\big[2c_4^A+12(c_2^A)^2\big]+\big[2c_4^\zeta+12(c_2^\zeta)^2\big]+24\,c_2^A c_2^\zeta .
$$
*The cross-term $24\,c_2^A c_2^\zeta$ is exactly the $2ab$ of $(a+b)^2=a^2+b^2+2ab$. It is a consequence of squaring an additive quantity, **not** a coupling of the two potentials, and it carries no arithmetic content — the cumulants remain additive at every order. We state this explicitly to retract a tempting misreading: there is no genuine "order-four interaction" of the archimedean and prime potentials.*

The second caution concerns sensitivity, and is a genuine (negative) finding.

**Proposition 5.2 (higher rungs are not sharper).** *The fourth-order rung is less sensitive to isolated off-line zeros than the second. For a simple off-line pair $\Xi=t^2+b^2$,*
$$
L_1=2(t^2-b^2)<0\ \ (|t|<b)\quad\text{(order two detects)},\qquad L_2=24>0\ \ \text{everywhere}\quad\text{(order four is blind)} .
$$
*A finite model with a planted off-line quartet confirms it across depths* (A.4): *$L_1<0$ for every depth, $L_2<0$ only for the deepest.*

The consequence is a correction to the natural expectation: the lever is **order two**, the log-concavity rung, which already detects off-line zeros locally; the higher rungs are additional necessary conditions but not more discriminating. The residue is therefore not "beyond second order." It is the *uniform* second-order condition — the archimedean concavity dominating the prime curvature at every height — which returns us to the difference-of-convex domination of Theorem 3.1, now identified as an order-two phenomenon.

---

## 6. The de Bruijn–Newman flow and the local ceiling

To probe the *uniform* second-order condition we use the canonical deformation that measures distance from log-concavity: the de Bruijn–Newman flow. With the kernel $\Phi$ of Pólya–de Bruijn ($\Phi>0$, validated $\int_0^\infty\Phi=\xi(\tfrac12)/8$, A.5),
$$
H_\lambda(x)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(xu)\,du,\qquad H_0=\tfrac18\Xi(x/2),
$$
the zeros of $H_\lambda$ are all real iff $\lambda\ge\Lambda$ (the de Bruijn–Newman constant); RH $\iff\Lambda\le0$. The flow is the backward heat equation $\partial_\lambda\Xi=-\Xi''$, and the Cole–Hopf substitution $u=(\log\Xi)'$ turns it into **Burgers**:
$$
\partial_\lambda u=-u_{tt}-2u\,u_t .
$$
The two potentials $u=u^A+u^\zeta$ are additive in the linear part $-u_{tt}$; the quadratic term $-2uu_t$ mixes them, as any nonlinear term in a sum does. (This is genuine nonlinearity of the PDE, and should not be conflated with the algebraic cross-term of Section 5, which is not a coupling at all.)

The key computation concerns the second-order margin at the centre. By evenness,
$$
-c_2(0)\;=\;-(\log H_\lambda)''(0)\;=\;\frac{\int_0^\infty u^2 e^{\lambda u^2}\Phi(u)\,du}{\int_0^\infty e^{\lambda u^2}\Phi(u)\,du}\;=\;\langle u^2\rangle_\lambda\;>\;0,
$$
a **second moment of a positive measure**, with $\partial_\lambda\langle u^2\rangle=\operatorname{Var}_\lambda(u^2)>0$ (computed A.5). Two consequences follow, and they are the ceiling of the local programme.

**Proposition 6.1 (the margin is blind to $\Lambda$).** *The central second-order margin $-c_2(0)=\langle u^2\rangle_\lambda$ is strictly positive for every $\lambda$, including $\lambda<0$, and increases monotonically with $\lambda$. It is identical in character at $\lambda=0$ and across the admissible window $\lambda\in(0,0.2]$, and so carries no information distinguishing $\Lambda=0$ from $\Lambda>0$.*

The two-potential split is, by contrast, quantitative about the *mechanism* — but only in a narrow window. Near the centre the split is contaminated by a spurious cancellation: $A$ and $\zeta_{\mathrm{line}}$ each carry the pair of singularities at $t=\pm i/2$ (the pole of $\zeta$ at $s=1$ and the trivial structure) that *cancels* in $\Xi$, giving large opposite contributions ($-c_2^A\approx-3.70$, $-c_2^\zeta\approx+3.75$) summing to the thin true margin ($+0.046$). The clean "archimedean concavity beats prime convexity" holds only in a window around $t\approx5$; above $t\approx8$ the zeros themselves supply the concavity and the archimedean term is negligible (A.5).

**Corollary 6.2 (the local ceiling).** *The local, finite-order programme — relative-entropy potentials, log-concavity, the cumulant hierarchy, the de Bruijn–Newman margin — reduces the Riemann Hypothesis to the uniform second-order domination of the archimedean potential over the prime potential, and shows that this margin is a positive-measure moment with no $\Lambda$ content. The constant $\Lambda$ is not a local quantity: $\Lambda\ge0$ (Rodgers–Tao) is a statement about the global spacing of the zeros. The residue is therefore global, and no further local order will reach it.*

---

## 7. The global residue: the form factor at $\tau=1$

The global second-order statistic of the zeros is the Montgomery pair correlation, equivalently the GUE form factor
$$
K(\tau)\;=\;\min(|\tau|,1)\;:\qquad \text{ramp } |\tau|\ (|\tau|<1),\quad \text{plateau } 1\ (|\tau|>1),\quad \text{corner at } \tau=1 .
$$
Its real-space dual is the pair correlation $R_2(r)=1-\big(\tfrac{\sin\pi r}{\pi r}\big)^2$; the corner at $\tau=1$ is the $\operatorname{sinc}^2$. The empirical pair correlation of the first $300$ zeta zeros, after unfolding, exhibits the GUE level-repulsion hole near $r=0$ — the second-order statistic in data (A.6; the statistics are limited, the hole is the robust feature).

The form factor is the **global parent** of the de Bruijn–Newman margin of Section 6: both are the order-two (pair $=$ Fisher $=$ $c_2$) statistic, one local, one global. And it splits along the two potentials:

| region | mechanism | de Bruijn–Newman | status |
|---|---|---|---|
| ramp $\tau<1$ | prime number theorem / archimedean diagonal density | $\Lambda\ge0$ (Rodgers–Tao) | **proven** |
| corner $\tau=1$ | diagonal saturates; off-diagonal must take over | — | boundary |
| plateau $\tau>1$ | Hardy–Littlewood prime off-diagonal | $\Lambda\le0=$ RH | **open** |

The ramp is Montgomery's theorem; equivalently it is the lower bound $\Lambda\ge0$ of Rodgers–Tao — the rigidity side, which the local programme already "has." The plateau is the conjectural side: it is built from the off-diagonal prime correlations, the Hardy–Littlewood singular series. Its per-prime weight is exactly the program's order-two conductor cumulant,
$$
\prod_{p\ge3}\Big(1-\frac{1}{(p-1)^2}\Big)=\prod_{p\ge3}\Big(1-\frac{1}{\varphi(p)^2}\Big)=C_2=0.6601618\ldots\quad(\text{twin-prime constant, A.6}),
$$
the per-prime $1/\varphi(p)^2$ being the Fisher / order-two cumulant of [N5, Theorem 6.2] (Fisher $=$ twin-prime). The program owns these off-diagonal correlations to all orders [N5, Theorem 6.2, the transfer $(-1)^n$]. What is open is their **closure across $\tau=1$** into the flat plateau $K\equiv1$.

**Statement 7.1 (the residual, RH-equivalent).** *The off-diagonal prime correlations — the order-two conductor cumulants $1/\varphi(p)^2$ summed via the Hardy–Littlewood singular series — close across $\tau=1$ to the plateau $K(\tau)=1$. This closure is the Montgomery pair-correlation conjecture (in the relevant range), equivalent to $\Lambda\le0$, equivalent to the archimedean self-adjointness of [N9], equivalent to the Riemann Hypothesis.*

**Remark 7.2 (the semiclassical picture, and why crossing symmetry does not bypass $\tau=1$).** The ramp–plateau morphology with its corner at $\tau=1$ is precisely the semiclassical form factor of Berry [Be] and Bogomolny–Keating [BK], who recovered the GUE plateau ($\tau>1$) from the diagonal/off-diagonal pairing of prime "periodic orbits," the off-diagonal sum being the Hardy–Littlewood singular series. This is the correct physical reading of the present section, and it makes the residue concrete. It is tempting to go further and treat $\tau=1$ as a *Stokes line* crossed "for free" by a conformal-bootstrap / Cardy argument — the flat plateau forced by the vacuum block of a dual channel, with the reflection $\iota=F^2$ ($s\leftrightarrow1-s$) cast as the exact Stokes automorphism and the transfer $(-1)^n$ [N5] as a Borel trans-series parity. Three exact structural facts (certified A.8) show this is a *picture, not a theorem*. **(i)** Cardy/crossing is a theorem in $2$d CFT because the torus partition function is *modular invariant* ($S:\tau\mapsto-1/\tau$ exchanges two channels); the form factor $K(\tau)=\min(|\tau|,1)$ has **no** $\tau\mapsto1/\tau$ symmetry, hence no second channel related by a group action and no vacuum-block mechanism. **(ii)** The reflection $\iota=F^2$ acts on the zeros as $\gamma\mapsto-\gamma$, i.e. on the form factor as $\tau\mapsto-\tau$ (*evenness*), leaving the diagonal and off-diagonal sectors each invariant: it is channel-**preserving**, whereas a Stokes automorphism must **exchange** the perturbative and non-perturbative sectors. **(iii)** The transfer $(-1)^n$ makes the per-prime cumulant series $\sum_{n\ge2}(-1)^n z^n/\varphi(p)^n$ Borel-**summable** — its only singularity sits at $z=-\varphi(p)$, on the *negative* axis, off the positive Borel ray ($p=2$ marginal at radius $1$) — the opposite of a Borel-non-summable trans-series; and the $\tau=1$ corner is a *continuous, slope-discontinuous* kink, the signature of a Legendre/convex **phase transition** (the adelic-Legendre, dually-flat reading the program already carries), not of a Stokes jump. The one place the plateau is genuinely *computed* — Bogomolny–Keating — is conditional on Hardy–Littlewood with uniformity: it **uses** the open arithmetic (the uniform level-of-distribution $\theta_0\approx0.515$ of the sequel push), it does not cross it. The semiclassical picture thus sharpens the attribution of this section without lowering the residual.

By the Goldston–Montgomery equivalence, the plateau is in turn equivalent to a second-moment asymptotic for primes in short intervals,
$$
\int_1^X\big(\psi(x+h)-\psi(x)-h\big)^2\,dx\;\sim\;hX\log(X/h)
$$
over the appropriate range of $h$ — the prime-variance form of the $\tau=1$ closure, and the natural target for a direct arithmetic attack (taken up in the sequel computation).

---

## 8. The map

Assembling the chain — a sequence of *known* relationships, most of them established equivalences (with one caveat noted below) — the picture is:

$$
\begin{aligned}
&\text{Euler product (Section 2.3)} &&\Longrightarrow\quad \text{prime potential }\Phi=\log\zeta\text{ convex, separable}\\
&\text{both terms (Sections 2–3)} &&\Longrightarrow\quad W=D_{\mathrm{arch}}-\Phi_{\mathrm{prime}}\ \text{(difference of convex)}\\
&\text{reflection (Section 4)} &&\Longrightarrow\quad \text{log-concavity of }\Xi\ \text{(Laguerre, order 2)}\\
&\text{order four (Section 5)} &&\Longrightarrow\quad \text{order 2 is the lever (higher rungs not sharper)}\\
&\text{de Bruijn–Newman (Section 6)} &&\Longrightarrow\quad \text{local margin a positive-measure moment, blind to }\Lambda\\
&\text{form factor (Section 7)} &&\Longrightarrow\quad \boxed{\ \tau=1\ \text{singular-series closure}\ =\ \text{RH}\ }
\end{aligned}
$$

The two potentials are additive as cumulants at every order, separable at second order in the Laguerre conditions, until the boundary $\tau=1$, where the local analysis is exhausted and the global arithmetic of prime correlations takes over. The difference of convex potentials is trivially signed where the Euler product converges and is the Riemann Hypothesis where it does not.

**One honest caveat about the arrows.** Not every "$\Longrightarrow$" above is a logical equivalence. Two are: $\Lambda\le0\iff$ RH (de Bruijn–Newman) and, under RH, the Goldston–Montgomery plateau $\iff$ short-interval variance. But pair correlation is *logically independent* of RH (Gallagher–Mueller), and the level of distribution for primes in arithmetic progressions is a *distinct* prong; pushing $\theta$ past $1/2$ is not known to imply RH, nor RH to imply it. So the passage from the pair-correlation plateau to the level-of-distribution frontier is a thematic bridge, not a deductive implication. The "map" is a unifying narrative, not a chain of equivalences collapsing RH onto an exponent.

---

## 9. Honest status

This paper proves no new positivity and does not prove the Riemann Hypothesis. What it establishes is a *map*, each edge of which is an exact, deterministic certificate (Appendix A): the prime term of the Weil functional is a convex log-partition (Section 2, A.2); the Weil functional is a difference of convex potentials (Section 3); the reflection realizes it as log-concavity (Section 4, A.3); order two is the lever and higher orders are not sharper (Section 5, A.4); the local margin is a positive-measure moment blind to $\Lambda$ (Section 6, A.5); the residue is the global form-factor plateau, the $\tau=1$ singular-series closure (Section 7, A.6).

The value, such as it is, is in the delimitation, and it is expository: the Riemann Hypothesis is displayed as neither an archimedean-positivity problem (that half is a relative entropy, unconditionally non-negative) nor a higher-order phenomenon (order two is the lever) nor a local one (the de Bruijn–Newman margin is $\Lambda$-blind), but a global, second-order, arithmetic statement about prime correlations.

**What is and is not new.** Nothing here is new mathematics. Each ingredient is established: the convex-duality reading of the archimedean term is textbook information geometry (Amari–Nagaoka; Nielsen), its zeta-function instance is published (Garbouge–Nielsen); the zeta distribution and Euler-product-as-independence are classical (Golomb; Lin–Hu); the Laguerre/cumulant hierarchy $\iff$ RH is Csordas–Varga, and the cumulant reformulation specifically is Nuttall (2013); the de Bruijn–Newman/Cole–Hopf/Burgers picture and the global nature of $\Lambda$ are standard (Poláčik–Šverák; Rodgers–Tao); the pair correlation, the short-interval-variance equivalence, and the trilinear-Kloosterman frontier are Montgomery, Goldston–Montgomery, and Bettin–Chandee/Fouvry–Radziwiłł. No bound is improved and no new theorem is proved. Collecting Riemann-Hypothesis equivalences into one account is itself a documented genre (Broughan, *Equivalents of the Riemann Hypothesis*, CUP 2017). This note's only contribution is a unifying information-geometric lens; it should be read as exposition, not as research, and it does not constitute progress toward the Riemann Hypothesis.

---

## Appendix A. Certificates

All certificates are deterministic, run under `empirical/p_infinity/` with `mpmath`/`sympy` (no floating-point-conditioning verdicts, no external data), and report GREEN.

- **A.1** `probe_archimedean_relative_entropy.py` — the archimedean term as a relative entropy: $\Phi^\ast=\log N-H=D(P_\beta\Vert u)$ to $<10^{-30}$; Fenchel–Young $=$ Bregman $=$ relative entropy; Gibbs; $\Omega_\infty(0)=-5.3721834$.
- **A.2** `probe_prime_side_bregman_logzeta.py` — the prime term as the convex log-partition $\log\zeta$: convexity $=$ Fisher; $\Phi'=-\sum\Lambda(n)n^{-s}$; Euler $=$ separability; Bregman $=$ relative entropy; Davenport–Heilbronn defect $\approx1.081$ (fusion-sighted).
- **A.3** `probe_dc_reflection_laguerre.py` — reflection $\Xi(t)=\Xi(-t)$; $L_1[\Xi]\ge0$ ($\log|\Xi|$ concave); exact factorization $L_1[\Xi]=L_1[A]\zeta^2+A^2L_1[\zeta]$; $L_1$ detects off-axis pairs.
- **A.4** `probe_order4_laguerre_interaction.py` — cumulant forms $L_1/\Xi^2=-c_2$, $L_2/\Xi^2=2c_4+12c_2^2$; cumulant additivity to $10^{-41}$; the order-four interaction $24c_2^Ac_2^\zeta$; the refutation $L_2[t^2+b^2]=24$.
- **A.5** `probe_debruijn_newman_two_potential.py` — kernel validation $\int\Phi=\xi(\tfrac12)/8$; Cole–Hopf/Burgers; central margin $=\langle u^2\rangle_\lambda$, monotone, blind to $\Lambda$; the two-potential split and its narrow clean window.
- **A.6** `probe_montgomery_formfactor_two_potential.py` — form factor $\min(|\tau|,1)$; empirical pair correlation of $300$ zeros (GUE hole); singular series $C_2=0.6601618\ldots$ with per-prime $1/\varphi(p)^2$.
- **A.7** `probe_toland_dual_signpreserving.py` — the Toland–Singer dual (Section 3.1): the identity $\inf_f(D_{\mathrm{arch}}-\Phi_{\mathrm{prime}})=\inf_\xi(\Phi_{\mathrm{prime}}^\ast-D_{\mathrm{arch}}^\ast)$ to machine zero on closed-form quadratics across $m>0,\,m=0,\,m<0$, and to $\sim10^{-42}$ on the two $\mathbb Z/6$ ledgers, with the explicit entropy $\leftrightarrow$ log-partition conjugate swap; sign invariance of $m$ (Prop. 3.2) confirmed.
- **A.8** `probe_tau1_crossing_vs_phase_transition.py` — the $\tau=1$ corner is a Legendre phase transition, not a resurgent Stokes line (Remark 7.2): (i) $K$ has no $\tau\mapsto1/\tau$ modular symmetry; (ii) $\iota=F^2$ acts as channel-preserving evenness on $200$ real zeros (diagonal/off-diagonal sectors invariant); (iii) the $(-1)^n$ per-prime series is Borel-summable (pole at $z=-\varphi(p)<0$), the corner a continuous slope-kink. The semiclassical (Berry / Bogomolny–Keating) plateau is HL-conditional.
- **A.9** `probe_toland_barrier_margin.py` — the Singer barrier (Section 3.2): the dual margin $\mu(\nu)=\lambda_{\min}(M_A+M_{\mathrm{pole}}-M_P,G)$, the tightest convex certificate over support-$\nu$ test functions. Self-validating gate: the assembled matrix form equals the direct sum $\sum_\rho|\widehat\varphi(\gamma_\rho)|^2$ over the first $400$ zeros to $\sim10^{-10}$. Result: $\mu(\nu)$ collapses $1.5\times10^{-3}\to\sim10^{-11}$ across the support threshold $\nu_\star\approx1.2$ (the dual-cone image of $\tau=1$); control $M_P\mapsto\kappa M_P$ shows $\kappa>1$ drives $\mu<0$ ($M_P$ indefinite, $\mu(\kappa)$ non-monotone). Marginal branch confirmed; no held floor.

---

## References

**Internal (used as cited theorems).**

[T0] Murillo Montero, L. (2026). *Gauge Selection and the Fourier–Mellin Simplex.* (Theorem 2.7: conjugate potential $=$ relative entropy; Theorem 4.7: ANOVA separability.)

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.*

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.* (Theorem 6.2: the explicit-formula transfer $(-1)^n$; the per-prime order-two cumulant $1/\varphi(p)^2$.)

[N9] Murillo Montero, L. (2026). *The Cross-Prime Fusion Criterion.* (Cross-prime fusion $=$ Euler product; the Davenport–Heilbronn no-go; the archimedean residue.)

[T15] Murillo Montero, L. (2026). *Finite-to-Archimedean Completion.*

[N14] Murillo Montero, L. (2026). *The Archimedean Weil Positivity is a Relative Entropy.*

**Classical and external.**

[Go] Golomb, S. W. (1992). *A class of probability distributions on the integers.* J. Number Theory 2, 189–192.

[Po] Pólya, G. (1927). *Über die algebraisch-funktionentheoretischen Untersuchungen von J. L. W. V. Jensen.*

[CV] Csordas, G., Varga, R. S. (1990). *Necessary and sufficient conditions and the Riemann Hypothesis.* Adv. Appl. Math. 11, 328–357.

[dB] de Bruijn, N. G. (1950). *The roots of trigonometric integrals.* Duke Math. J. 17, 197–226.

[Ne] Newman, C. M. (1976). *Fourier transforms with only real zeros.* Proc. Amer. Math. Soc. 61, 245–251.

[RT] Rodgers, B., Tao, T. (2020). *The de Bruijn–Newman constant is non-negative.* Forum Math. Pi 8, e6.

[P15] Polymath, D. H. J. (2019). *Effective approximation of heat flow evolution of the Riemann $\xi$ function, and a new upper bound for the de Bruijn–Newman constant.* Res. Math. Sci. 6, 31.

[Mo] Montgomery, H. L. (1973). *The pair correlation of zeros of the zeta function.* Proc. Sympos. Pure Math. 24, 181–193.

[Be] Berry, M. V. (1988). *Semiclassical formula for the number variance of the Riemann zeros.* Nonlinearity 1, 399–407.

[BK] Bogomolny, E. B., Keating, J. P. (1996). *Random matrix theory and the Riemann zeros II: $n$-point correlations.* Nonlinearity 9, 911–935.

[GM] Goldston, D. A., Montgomery, H. L. (1987). *Pair correlation of zeros and primes in short intervals.* In *Analytic Number Theory and Diophantine Problems*, Birkhäuser, 183–203.

[HL] Hardy, G. H., Littlewood, J. E. (1923). *Some problems of 'Partitio numerorum' III.* Acta Math. 44, 1–70.

[We] Weil, A. (1952). *Sur les "formules explicites" de la théorie des nombres premiers.* Comm. Sém. Math. Univ. Lund.

[To] Toland, J. F. (1979). *A duality principle for non-convex optimisation and the calculus of variations.* Arch. Rational Mech. Anal. 71, 41–61. (Toland–Singer duality for differences of convex functions.)

**Prior art establishing that the content of this expository note is known.**

[LH] Lin, G. D., Hu, C.-Y. (2001). *The Riemann zeta distribution.* Bernoulli 7(5), 817–828. (Independent-geometric prime-exponent representation of the zeta distribution — Section 2.3.)

[AN] Amari, S., Nagaoka, H. (2000). *Methods of Information Geometry.* AMS/Oxford; F. Nielsen (2024), *Divergences Induced by the Cumulant and Partition Functions of Exponential Families*, Entropy 26(3):193. (Conjugate of log-partition $=$ relative entropy; Fenchel–Young $=$ Bregman — Sections 2–3.)

[GN] Garbouge, S., Nielsen, F. (2021). *A note on some information-theoretic divergences between zeta distributions.* arXiv:2104.10548. ($\log\zeta$ as the convex cumulant function of the zeta distribution, with explicit Bregman/relative-entropy divergences — the published instance of Sections 2–3.)

[Nu] Nuttall, J. (2013). *Wronskians, Cumulants, and the Riemann Hypothesis.* Constr. Approx. 38, 469–484. (The cumulant reformulation of the Laguerre/Wronskian hierarchy for $\Xi$ — prior art for Section 4.3.)

[PS] Poláčik, P., Šverák, V. (2008). *Zeros of complex caloric functions and singularities of complex viscous Burgers equation.* J. Reine Angew. Math. (Crelle). (Cole–Hopf mapping of caloric-function zeros to Burgers — prior art for Section 6.)

[Br] Broughan, K. (2017). *Equivalents of the Riemann Hypothesis*, 2 vols. Cambridge University Press. (The documented genre of collecting RH equivalences into one account.)

[KLM] Kandhil, S., Languasco, A., Moree, P. (2026). *Pair correlation of zeros of Dirichlet L-functions...*; accepted Math. Ann. (arXiv:2411.19762). (The pair-correlation $\to$ level-of-distribution conditional implication — the only candidate-new joint of Section 7, already published.)
