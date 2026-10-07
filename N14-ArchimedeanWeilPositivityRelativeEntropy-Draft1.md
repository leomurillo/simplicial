# N14 — The Archimedean Weil Positivity is a Relative Entropy

## An Information-Geometric Reading of the Archimedean Term (Expository Note)

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — June 7, 2026*

<!--
Program record (not part of the paper). Fourteenth paper of the Numbers (N-) series. EXPOSITORY NOTE, not
a research contribution; does NOT prove RH. NOVELTY-AUDITED 2026-06-08: the content is KNOWN. The
convex-duality identity (conjugate of log-partition = relative entropy; Fenchel-Young = Bregman; >=0 =
Gibbs) is textbook info-geometry (Amari-Nagaoka; Nielsen 2024); the zeta-function instance is published
(Garbouge-Nielsen arXiv:2104.10548). FRAMING CORRECTED: Connes's p.21 remark (real, verbatim) is about
YOSHIDA's numerical proof, NOT a claim that no conceptual reason exists -- Connes-Consani DO provide one
(Sonin space) and Connes extends it to primes (arXiv:2602.04022 sec 7.2-7.4). So this note offers only an
alternative information-geometric LENS, not a missing reason. W_inf(f) >= 0 was proven by Connes-Consani
(arXiv:2006.13771) and numerically by Yoshida. Reading: W_inf as the non-negativity of a relative entropy /
Fenchel-Young gap of a log-convex local factor. Internal apparatus (sec 7) rests on: T0 Thm 2.7 (conjugate
potential = relative entropy, exact), N4/N5 (the apex archimedean operator = the Connes-Consani
archimedean operator), T15 (finite-to-archimedean completion). Honest scope: the prime contribution
enters with the opposite (Legendre) sign, so the full functional is a difference of convex potentials and
the conceptual reason does NOT extend to the primes -- that domination is the Riemann Hypothesis, left
open. Sec 7.3 converts the tempting Petz/data-processing "monotonicity proof" into a sharply-stated
OBLIGATION: a DPI proof would need a CPTP channel whose pushed-forward divergence reproduces the prime
log-partition WITH the Hardy-Littlewood per-prime 1/phi(p)^2 weights -- i.e. it hides the tau=1 singular-
series closure (N15 sec 7) inside "this map is CPTP," and an additive-monotonicity-only proof would
contradict the Remark 7.2 multiplicative dichotomy. Conditional entropy is the wrong (sign-indefinite)
invariant; the non-negative object is the monotonicity defect, available only after the obligation is met.
Sec 7.4 (added) DISCHARGES the construction explicitly with the apex unitary U_p [N1]: Phi_p = dephasing in
the character (Frobenius) frame, defect = classical entropy production S(Bp)-S(p) of the doubly-stochastic
B=|U_p|^2. Theorem 7.6 = a DICHOTOMY: (i) the even/metric half is delivered unconditionally (defect strictly
positive on every non-vacuum state, contraction I-B^T B PD on mean-zero, order-2 = Fisher form) [P];
(ii) no-go #1 phase blindness: B real => defect uses only |U_p|^2, blind to the odd/chiral L(.,chi_3) phase
(self-adjoint instrument blind to antisymmetric current = Irreversible Blind Spot) [P]; (iii) no-go #2
transfer reversibility: tau_n=(-1)^n is particle-hole X->1-X = a reflection = reversible => Petz-equality
defect == 0 [P]; (iv) the sole residue is the IRREVERSIBLE continuation across tau=1 = RH [C]. Does NOT prove
RH; localizes it to one irreversibility step. Pedagogical throughout; internal program vocabulary translated
into standard exponential-family and explicit-formula language. Tiering for the record: Thm 4.1 finite = [P];
Thm 4.2 archimedean completion = [P] modulo the cited completion theorem; Thm 7.6(i)-(iii) = [P]; Thm 7.6(iv)
/ sec 7.1-7.3 closure = [C], explicitly RH and open.
Certificates: Appendix A (finite worked instance) empirical/p_infinity/probe_archimedean_relative_entropy.py
-- GREEN (40 dps): (1) Phi* = logN - H = D(P||u) to <1e-30; (2) Fenchel-Young = Bregman = D(P_b2||P_b1) >= 0;
(3) Gibbs, unique zero at beta=0; (4) Omega_inf(0) = -5.3721834 < 0 (positivity is global, not kernel).
Sec 7.4 (Thm 7.6) empirical/p_infinity/probe_obligation73_pinching_channel.py -- GREEN (50 dps, p=3,5,7,11,13):
U_p unitary + B doubly-stochastic <1e-40; defect>=0 & order-2 Taylor match; I-B^T B PD on mean-zero w/ gap;
max|Im B|=0 (phase blindness); reflection-permutation defect ==0 (transfer reversibility).
Sec 7.5 (CORRECTED 2026-06-08 after paranoid audit). The missed chiral content is the STATE-DEPENDENT PHASE
C(rho)=Im(rho_chi), rho_chi=U diag(p) U*; vanishes at the self-dual vacuum (arrow=0 at equilibrium), phase-borne
(gauge-covariant Berry/Bargmann), invariant = character-triangle Im products. Its definite sign = c_2<0 =
L(1/2,chi_3)!=0 = RH content; Thm 7.6 LOCATES it but gives NO reduction of it. Certified
empirical/p_infinity/probe_obligation73_chirality_audit.py.
Rem 7.8 records a NEGATIVE result (overreach withdrawn): the earlier "Vector A/B" candidate J=B-B^T (B=|U_p|^2)
is NOT the chiral current -- it is PHASE-BLIND (rephasing chars leaves J fixed) and STATE-INDEPENDENT (nonzero at
vacuum where the true arrow=0). J has real structure (transpose-asymmetry of |U_p|^2: conveyor gap growing
0.055->0.164 and 0.081->0.230; >=97% odd under c->-c; cross-prime 45% at N=6) certified in
probe_obligation73_irreversibility_gap.py + probe_obligation73_primorial_tower.py, but its RH/L(.,chi_3)
interpretation is WITHDRAWN. Lesson = Thm 7.6(ii): the chiral half is unrecoverable from any modulus-squared
(symmetric) construction, J included. No reduction beyond the Thm 7.6 dichotomy.
Rem 7.9 (thread-(a) audit) empirical/p_infinity/probe_obligation73_genuine_chiral_audit.py -- GREEN (p=7,N=6):
the CORRECT object C(rho)=Im(rho_chi) passes every check J failed -- EXACTLY parity-odd (100% odd sector, not 97%),
vacuum-zero, individual Bargmann triangle phases gauge-INVARIANT. But the obstruction: real (T-symmetric) states
give Im(rho_chi) PURELY parity-odd => every parity-even/net readout = 0; a nonzero scalar needs a parity-ODD
ORIENTATION = chi_3 vs conj(chi_3) (chars 2<->4 at N=6, Im(rho_chi)_24=+0.00745 flips sign). The definite sign =
choosing sign of L(1/2,chi_3) = full RH. So the genuine object LOCATES RH exactly but gives NO reduction; dichotomy stands.
Companion exploratory probe: empirical/p_infinity/probe_logpartition_lever.py (the GPD lever test).
-->

---

> **Status and attribution (read first).** This is an *expository* note, not a research contribution, and it does not prove the Riemann Hypothesis. Its mathematical content is known. The identity "the Legendre conjugate of a convex log-partition function is a relative entropy; the Fenchel–Young gap is a Bregman divergence; its non-negativity is Gibbs' inequality" is standard exponential-family information geometry (Amari–Nagaoka 2000; Nielsen 2024). Its specialization to the Riemann zeta function — $\log\zeta$ as the convex cumulant generating function of the zeta distribution, with explicit Bregman/relative-entropy divergences — is already published (Garbouge–Nielsen 2021). And a *conceptual reason* for archimedean Weil positivity already exists in the literature we cite: Connes–Consani (2021) locate the positivity in the Sonin space (the compression of the scaling action), and Connes (2026, §7.2–7.4) extends that mechanism to incorporate the primes. The Connes remark we quote in §1.1 is real (arXiv:2602.04022, p. 21) but is aimed at *Yoshida's numerical proof*, not at the conceptual problem in general. What this note offers is therefore only an *alternative information-geometric lens* on a positivity that is already proven and already conceptually explained — useful for intuition, not new mathematics.

---

## Abstract

We give an information-geometric reading of the **archimedean** part of the Weil explicit-formula functional, $W_\infty(f)\ge 0$ (proven by Connes–Consani 2021, verified numerically by Yoshida): we exhibit $W_\infty$ as **the non-negativity of a relative entropy** — equivalently the **Fenchel–Young inequality** of a strictly convex log-partition function whose convexity is the logarithmic convexity of the archimedean factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$, so that the positivity is Gibbs' inequality $D(P\,\Vert\,u)\ge 0$. We read this against Connes' time–frequency presentation of $W_\infty$, identifying his Shannon-capacity term with the log-capacity and his projection-defect trace with the entropy. None of this is new mathematics: the convex-duality identity is textbook information geometry (Amari–Nagaoka; Nielsen), its zeta-function specialization is published (Garbouge–Nielsen), and a conceptual reason for the positivity already exists — the Sonin-space mechanism of Connes–Consani, extended to the primes by Connes (§7.2–7.4 of arXiv:2602.04022). The reading is an *alternative lens*, useful for intuition. We are careful about scope: the prime contribution enters the full Weil functional through the conjugate (Legendre) potential with the opposite sign, so the full functional is a **difference of convex potentials**, whose non-negativity — the domination of the prime potential by the archimedean one — is the Riemann Hypothesis, which we do not address.

**MSC 2020.** 11M26, 94A17, 62B10, 33B15, 46N55.

**Keywords.** Weil explicit formula, archimedean positivity, relative entropy, Kullback–Leibler divergence, log-partition function, Fenchel–Young inequality, Bregman divergence, exponential family, prolate spheroidal functions, Gamma factor, information geometry.

---

## 1. Introduction

### 1.1 A positivity in search of a reason

Weil's positivity criterion reformulates the Riemann Hypothesis as the non-negativity of an explicit Hermitian functional built from the explicit formula. Written for a test function $f$, the functional decomposes into three groups of terms,
$$
W(f)\;=\;\underbrace{W_\infty(f)}_{\text{archimedean}}\;+\;\underbrace{W_{\mathrm{pole}}(f)}_{\text{poles }s=0,1}\;-\;\underbrace{W_{\mathrm{prime}}(f)}_{\text{prime powers}},
$$
and the Riemann Hypothesis is the statement $W(f)\ge 0$ for all admissible $f$. The **archimedean** part $W_\infty$ is the contribution of the local factor at the real place, $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$. Unlike the full functional, *the archimedean part alone is unconditionally non-negative*: this was verified numerically by Yoshida and proven by Connes and Consani.

One might ask for a *conceptual* reason that a quantity attached to the Gamma factor should be positive. Connes makes a remark in this direction (arXiv:2602.04022, p. 21), but it is important to read it precisely: he is commenting on *Yoshida's proof* — a numerical analysis on a finite interval — when he writes that it "does not provide any conceptual reason for this positivity that would have a chance to continue to hold when primes are involved." He is not asserting that no conceptual reason exists. Indeed Connes and Consani provide one — they locate the positivity in the Sonin space, the compression of the scaling action — and Connes extends that mechanism to the primes (§7.2–7.4 of the same survey). So the conceptual question is *not open*; it has an operator-theoretic answer in the literature we build on.

What this note offers is a different, information-geometric lens on the same fact:

> **$W_\infty(f)$ admits a reading as a relative entropy; in that reading its non-negativity is Gibbs' inequality.**

Equivalently, $W_\infty(f)$ is the **Fenchel–Young gap** of a strictly convex log-partition function, that convexity being the logarithmic convexity of the Gamma factor. This is a re-description, not a new theorem: the convex-duality identity is standard (Amari–Nagaoka; Nielsen) and its zeta-function instance is already in print (Garbouge–Nielsen).

### 1.2 Why a relative entropy, and not merely a positive quadratic form

A reader might expect the archimedean positivity to be the trivial positivity of a quadratic form with a positive kernel. It is not, and this is the heart of the matter. The archimedean density that appears in $W_\infty$,
$$
\Omega_\infty(r)\;=\;\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{ir}{2}\right)-\log\pi,\qquad \psi=\Gamma'/\Gamma,
$$
is **negative** near $r=0$ (one has $\Omega_\infty(0)=-5.37\ldots$). A naive quadratic form $\int |\hat f(r)|^2\,\Omega_\infty(r)\,dr$ is therefore *indefinite*; the positivity of $W_\infty$ is a subtler, global fact, exactly the kind of fact a relative entropy expresses. A relative entropy $D(P\,\Vert\,Q)=\sum_s P(s)\log\frac{P(s)}{Q(s)}$ is non-negative not because each summand is non-negative — they are not — but because of a global convexity (Gibbs' inequality). To say "$W_\infty$ is a relative entropy" is therefore a genuine structural claim that *explains* a non-obvious positivity, not a restatement of an obvious one.

### 1.3 Scope, stated at the outset

We give the information-geometric reading for the **archimedean** positivity only. The contribution of the primes enters the full functional with the opposite sign, through the Legendre-conjugate potential; the full Weil functional is a **difference of two convex potentials**, and the non-negativity of a difference of convex functions is never automatic. That non-negativity — the statement that the archimedean (convex) potential dominates the prime (conjugate) potential uniformly — is the Riemann Hypothesis, and we do not claim it. Section 7 makes this boundary precise. The boundary is the honest part: it shows how far the thermodynamic re-description reaches, and where genuine arithmetic begins.

### 1.4 Sources and standing on theorems

The argument assembles established results. From information geometry we use the identification of the Legendre conjugate of a log-partition function with a relative entropy; in the finite cyclic setting this is a theorem of the first paper of the companion series (cited below as [T0, Theorem 2.7]). The identification of the relevant operator with the Connes–Consani archimedean operator is a theorem of [N4]–[N5]; the passage from the finite models to the archimedean continuum is a theorem of [T15] (finite-to-archimedean completion). We use these as cited theorems; none of our conclusions rests on a conjecture of those papers. The classical inputs are the explicit formula (Weil), the time–frequency presentation of $W_\infty$ and its compression positivity (Connes–Consani), the prolate spheroidal calculus (Slepian–Pollak–Landau), the conjugate-duality of convex analysis (Fenchel, Rockafellar), the exponential-family/relative-entropy dictionary (Amari–Nagaoka), and the logarithmic convexity of $\Gamma$ (Bohr–Mollerup; Artin).

---

## 2. The archimedean Weil functional and Connes' question

We recall the objects, for a reader who has not met them in this form.

### 2.1 The explicit formula and its archimedean term

Write $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ for the completed zeta function, with nontrivial zeros $\rho=\tfrac12+i\gamma_\rho$. For an even Schwartz test function $g$ on $\mathbb R$ with Fourier transform $\hat g$, the Riemann–Weil explicit formula reads, schematically,
$$
\sum_\rho \hat g(\gamma_\rho)\;=\;\underbrace{\hat g\!\left(\tfrac{i}{2}\right)+\hat g\!\left(-\tfrac{i}{2}\right)}_{\text{poles}}\;+\;\underbrace{\frac{1}{2\pi}\int_{\mathbb R}\hat g(r)\,\Omega_\infty(r)\,dr}_{\text{archimedean }=:\,W_\infty}\;-\;\underbrace{\sum_{n\ge 2}\frac{\Lambda(n)}{\sqrt n}\,\big(g(\log n)+g(-\log n)\big)}_{\text{primes}},
$$
with $\Omega_\infty(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}{2})-\log\pi$ and $\Lambda$ the von Mangoldt function. The **Weil quadratic functional** is obtained by taking $g=f\star\tilde f$ (so $\hat g=|\hat f|^2$); the Riemann Hypothesis is equivalent to $W(f)\ge0$ for all admissible $f$. The **archimedean part** $W_\infty(f)$ is the term carrying $\Omega_\infty$, i.e. the contribution of the local factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ at the real place.

### 2.2 The known positivity, and the missing reason

That $W_\infty(f)\ge 0$ for all admissible $f$ is known: numerically (Yoshida) and by proof (Connes–Consani), the latter realizing $W_\infty$ as a trace over a Sonin/prolate subspace and obtaining positivity from a compression. Connes' remark — that this gives no *conceptual* reason — is the motivation for the present paper. We will not re-prove the inequality; we will identify what kind of quantity $W_\infty$ is, so that its sign becomes evident on conceptual grounds.

### 2.3 Connes' time–frequency presentation

A second presentation of $W_\infty$, due to Connes, will serve as our bridge. Working in $L^2(\mathbb R)_{\mathrm{ev}}$ with the multiplicative scaling action $\vartheta$, and writing $P_T$ for the projection limiting time to $[-T,T]$ and $\hat P_W$ for the projection limiting frequency to $[-W,W]$, Connes rewrites the archimedean functional as
$$
W_\infty(f)\;=\;\log(TW)\,f(1)\;+\;\operatorname{Tr}\!\Big(\vartheta(f)\,\big(1-P_T-\hat P_W\big)\Big).
\tag{2.1}
$$
The eigenvalues of the concentration operator $P_T\hat P_W P_T$ are the Slepian numbers $\chi_n\in(0,1)$; the operator $1-P_T-\hat P_W$ measures the information that the time–frequency uncertainty principle forbids one to localize. We will read (2.1) as a relative entropy in Section 5; first we recall the relevant information geometry.

---

## 3. Log-partition functions and relative entropy

This section is a self-contained primer; the one non-classical input is Theorem 3.4, cited from [T0].

### 3.1 Finite exponential families

Let $\Omega$ be a finite set, $|\Omega|=N$, with uniform reference measure $u(s)=1/N$. Fix a real function $y:\Omega\to\mathbb R$ with $\sum_s y(s)=0$ (a centered "energy"). The associated **exponential family** is
$$
P_\beta(s)\;=\;\frac{e^{\beta y(s)}}{Z(\beta)},\qquad Z(\beta)=\sum_{s}e^{\beta y(s)},\qquad \beta\in\mathbb R,
$$
with $P_0=u$. The **log-partition function** (cumulant generating function, relative to $u$) is
$$
\Phi(\beta)\;=\;\log\Big(\tfrac1N\textstyle\sum_s e^{\beta y(s)}\Big).
$$

### 3.2 Convexity is the Fisher metric

Differentiating, $\Phi'(\beta)=\mathbb E_{P_\beta}[y]=:\xi$ and $\Phi''(\beta)=\operatorname{Var}_{P_\beta}(y)\ge 0$. Thus **$\Phi$ is convex**, strictly so unless $y$ is constant; the second derivative is the Fisher information of the family along $y$. Convexity of the log-partition function is the single fact that will generate every positivity below.

### 3.3 The conjugate potential and Fenchel–Young

The **Legendre–Fenchel conjugate** is $\Phi^\ast(\xi)=\sup_\beta\big(\beta\xi-\Phi(\beta)\big)$. For convex $\Phi$ the **Fenchel–Young inequality** holds:
$$
\boxed{\;\Phi(\beta)+\Phi^\ast(\xi)\;\ge\;\beta\,\xi\;}\qquad\text{for all }\beta,\xi,\ \text{with equality iff }\xi=\Phi'(\beta).
\tag{3.1}
$$
The non-negative quantity $\Phi(\beta)+\Phi^\ast(\xi)-\beta\xi$ is the **Bregman divergence** generated by $\Phi$; it is the canonical "distance" of convex duality.

### 3.4 The conjugate potential is a relative entropy

The bridge to thermodynamics is the following identity, which is [T0, Theorem 2.7] in the finite cyclic setting and classical for general exponential families (Amari–Nagaoka).

**Theorem 3.4 (conjugate potential $=$ relative entropy).** *With the notation above, for $\xi=\Phi'(\beta)$,*
$$
\Phi^\ast(\xi)\;=\;\log N-H(P_\beta)\;=\;D\big(P_\beta\,\Vert\,u\big),
$$
*where $H$ is Shannon entropy and $D(\cdot\Vert\cdot)$ is relative (Kullback–Leibler) entropy. Moreover the Bregman divergence of $\Phi$ equals the relative entropy of escorts, $\Phi(\beta_1)+\Phi^\ast(\xi_2)-\beta_1\xi_2=D(P_{\beta_1}\Vert P_{\beta_2})$.*

In particular $\Phi^\ast(\xi)\ge 0$ with equality iff $\xi=0$ (i.e. $P_\beta=u$): this is **Gibbs' inequality**, and it is the unconditional positivity we will transport to the archimedean place. The point of Theorem 3.4 is interpretive: the abstract conjugate potential of any log-partition function *is* an information distance from the maximum-entropy state.

---

## 4. Main theorem: the archimedean Weil functional is a relative entropy

We now identify $W_\infty$ with a conjugate potential, hence with a relative entropy.

### 4.1 The finite identity

The companion papers attach to each modulus $N$ a finite exponential family of the kind in Section 3, built on the cyclic group $\mathbb Z/N$, and a finite analogue of the archimedean functional. Two theorems connect them to the objects above:

- [N4]–[N5]: the operator generating the finite archimedean functional is exactly the Connes–Consani archimedean operator (its multiplier is the archimedean density $\Omega_\infty$); equivalently, the finite archimedean functional is the conjugate potential $\Phi^\ast$ of the finite log-partition function of Section 3.
- [T0, Theorem 2.7]: that conjugate potential equals $D(P_\beta\Vert u)$.

Combining these two cited theorems gives the finite identity.

**Theorem 4.1 (finite archimedean functional $=$ relative entropy).** *For each $N$, the finite archimedean Weil functional equals the conjugate potential of the associated finite exponential family, and hence a relative entropy:*
$$
W_\infty^{(N)}(f)\;=\;\Phi^\ast(\xi_f)\;=\;D\big(P_{\xi_f}\,\Vert\,u\big)\;\ge\;0,
$$
*with equality iff $f$ is at the maximum-entropy (uniform) configuration.* The operator identification is the certified content of [N4]–[N5]; the relative-entropy reading of the resulting functional is the contribution of the present paper. At the finite level the identity is exact.

### 4.2 The archimedean limit

The passage from the finite models to the continuum is the content of the finite-to-archimedean completion theorem.

- [T15]: along a cofinal tower of moduli, the finite exponential families and their conjugate potentials converge, in the appropriate sense, to a continuum object whose terminal boundary correction is the archimedean factor; the limit of the finite archimedean functionals is the archimedean Weil functional $W_\infty$.

**Theorem 4.2 (archimedean Weil functional $=$ relative entropy).** *Under the completion of [T15], the archimedean Weil functional is the archimedean limit of the conjugate potentials of Theorem 4.1:*
$$
\boxed{\;W_\infty(f)\;=\;\lim_{N}\,D\big(P^{(N)}_{\xi_f}\,\Vert\,u^{(N)}\big)\;=\;\Phi^\ast_\infty(\xi_f)\;\ge\;0.\;}
$$
*Consequently $W_\infty(f)\ge 0$, with equality precisely at the self-dual (maximum-entropy) configuration; equivalently $W_\infty(f)$ is the Fenchel–Young gap $\Phi_\infty(\beta)+\Phi^\ast_\infty(\xi)-\beta\xi$ of the archimedean log-partition function $\Phi_\infty$.*

**Remark 4.3 (what is proven, and what the limit rests on).** Theorem 4.1 is an exact identity. In Theorem 4.2 the *positivity* is robust: each finite term is a relative entropy, hence $\ge 0$ uniformly in $N$, so the limit is $\ge 0$ independently of any delicacy in the mode of convergence. The *identity* in the limit is the completion theorem of [T15]; we use it as cited. The conceptual conclusion — $W_\infty$ is (the archimedean realization of) a relative entropy — therefore holds at the level of an exact finite identity together with a uniform non-negativity that survives the limit.

### 4.3 The statement in words

The archimedean Weil functional measures how far the time–frequency profile of the test function sits from the maximum-entropy profile, in the sense of information distance. It is non-negative for the same reason any information distance is non-negative — the convexity of a log-partition function — and it vanishes only at the unique self-dual configuration. This is the conceptual reason Connes asked for.

---

## 5. The dictionary to Connes' time–frequency form

Theorem 4.2 becomes transparent — and verifiably Connes' own object — when read against the presentation (2.1).

A time- and band-limited signal is, by the Slepian–Pollak–Landau theory, governed by the concentration operator $P_T\hat P_W P_T$ with eigenvalues $\chi_n\in(0,1)$, of which approximately $TW$ (the Shannon number) are near $1$. Normalizing $\{\chi_n\}$ to a probability vector over the effective modes yields a distribution $P_f$ — the **concentration distribution** of $f$ — whose Shannon entropy $H(P_f)$ quantifies how the signal's energy is spread across the available time–frequency cells. Reading (2.1) term by term:

- $\log(TW)$ is the logarithm of the **Shannon capacity** (the number of available cells), i.e. the maximal entropy $\log N$ of a uniform profile over the cells;
- $\operatorname{Tr}\!\big(\vartheta(f)(1-P_T-\hat P_W)\big)$ is the **information defect** — the entropy the uncertainty principle removes — i.e. $-H(P_f)$ to leading order.

Hence Connes' presentation is, term for term,
$$
W_\infty(f)\;=\;\log(TW)\,f(1)+\operatorname{Tr}\!\big(\vartheta(f)(1-P_T-\hat P_W)\big)\;=\;\log(\text{capacity})-H(P_f)\;=\;D(P_f\,\Vert\,u),
$$
matching Theorem 4.2. Connes' Shannon-capacity term is the log-capacity $\log N$; his projection-defect trace is the entropy term; their difference is the relative entropy. The compression that yields positivity in the Connes–Consani proof is exactly the restriction to the maximum-entropy (concentrated) family, and the positivity it produces is Gibbs' inequality. This is the answer to the conceptual question in Connes' own language.

---

## 6. The convexity source: logarithmic convexity of the Gamma factor

It remains to say *why the relevant log-partition function is convex*, i.e. where the Fisher metric positivity ultimately comes from at the archimedean place. It comes from the archimedean local factor itself.

The factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ is **logarithmically convex** on $(0,\infty)$: this is the Bohr–Mollerup characterization of $\Gamma$ (equivalently, $(\log\Gamma)''=\psi'>0$). Logarithmic convexity is precisely the statement that $\log\Gamma_{\mathbb R}$ is a convex log-partition-type function; its second derivative $\psi'$ is the archimedean Fisher metric, and the density $\Omega_\infty=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}{2})-\log\pi$ that appears in $W_\infty$ is built from the first logarithmic derivative $\psi$. Thus the convexity that Section 3 required, and that Theorem 4.2 transports into the positivity of $W_\infty$, is the same convexity that makes $\Gamma$ a moment-generating (totally monotone) object. In one line:

> *The Gamma factor is log-convex; a log-convex local factor is a log-partition function; its conjugate is a relative entropy; relative entropy is non-negative; that non-negativity is the archimedean Weil positivity.*

---

## 7. Scope: the primes, and where the conceptual reason ends

We delimit the result precisely, because the boundary is informative.

In the full Weil functional the primes appear with the **opposite sign** to the archimedean term. In the language of Section 3, the archimedean term is the convex potential $\Phi$ (equivalently its conjugate $\Phi^\ast$, a relative entropy), while the prime term is read in the *dual* (mean) chart and enters as the **Legendre conjugate with a minus sign**. The full functional is therefore of the form
$$
W(f)\;=\;\underbrace{\Phi^\ast_\infty(\xi_f)}_{\text{archimedean (convex)}}\;-\;\underbrace{\Psi(\xi_f)}_{\text{prime (convex)}},
$$
a **difference of convex functions**. A relative entropy is a single convex potential and is unconditionally non-negative; a difference of convex potentials is in general indefinite, and its non-negativity is not a consequence of convexity. The non-negativity of $W$ — equivalently, the statement that the archimedean convex potential dominates the prime one uniformly over all admissible $f$ — is the Riemann Hypothesis. The thermodynamic argument of this paper gives the archimedean term for free and says nothing, by itself, about the domination; that is exactly the content Connes anticipated would require new ideas "when primes are involved." We make no claim toward it here.

Two structural remarks sharpen the boundary, without crossing it.

**Remark 7.1 (necessity of the conjugate sign).** That the primes must be read in the dual chart, with the opposite sign, is forced by the explicit formula (the prime side is the term subtracted in the explicit formula). It is the reason the full functional is a difference of convex potentials rather than a single divergence. The conceptual reason for positivity is thus genuinely confined to the archimedean place; this is not a limitation of the method but a feature of the arithmetic.

**Remark 7.2 (the multiplicative obstruction).** A purely additive (second-moment) positivity over $\mathbb Q$ is, by a structural dichotomy established in the companion series [P-series; N9], either unconditional and content-free or contentful and indefinite; the contentful, RH-bearing positivity is multiplicative (an intersection-theoretic positivity), available unconditionally only over function fields. The relative-entropy reason of this paper is exactly the unconditional, content-free archimedean half of that dichotomy; the RH content lives on the other, multiplicative side, beyond the reach of a single convex potential. We record this only to locate the present result honestly within the larger landscape.

### 7.3 A monotonicity route, and the obligation it incurs

Because both terms live in one relative-entropy currency, the data-processing inequality is tempting. Relative entropy is monotone under any completely positive trace-preserving (CPTP) map — Petz's monotonicity theorem [Pe], the quantum data-processing inequality [Li], [Uh] — so $D(\rho\Vert\sigma)\ge D(\Phi\rho\Vert\Phi\sigma)$ for every channel $\Phi$. The restriction from the continuous archimedean scaling flow on $\mathbb R_+^\times$ to the discrete prime lattice is a coarse-graining; were it realized as a single CPTP map $\Phi$, and were the two Weil potentials the relative entropies of one pair of states before and after $\Phi$, the gap $D_{\mathrm{arch}}-\Phi_{\mathrm{prime}}$ would be the non-negative monotonicity defect $D(\rho\Vert\sigma)-D(\Phi\rho\Vert\Phi\sigma)\ge0$, and the archimedean domination — hence the Riemann Hypothesis — would follow unconditionally. The intuition points the right way ("fine $\ge$ coarse"). But as a proof it is incomplete in an informative way; we state the gap precisely rather than cross it.

**Obligation 7.3 (what a monotonicity proof must supply).** *To conclude $W\ge0$ from data processing one must exhibit*
1. *a CPTP map $\Phi$ realizing the restriction $\mathbb R_+^\times\twoheadrightarrow\{\text{prime lattice}\}$, with states $\rho_f,\sigma$ such that $D_{\mathrm{arch}}(f)=D(\rho_f\Vert\sigma)$; and*
2. *the identification $\Phi_{\mathrm{prime}}(f)=D(\Phi\rho_f\Vert\Phi\sigma)$ with the correct normalization — the pushed-forward divergence must reproduce the prime log-partition / zeta-distribution divergence, including its per-prime weights.*

*Step (2) is the entire content.* The pushed-forward divergence reproduces the prime side only if $\Phi$ already encodes the off-diagonal prime correlations — the Hardy–Littlewood singular series with per-prime weight $1/\varphi(p)^2$ [N5, Theorem 6.2]. That is precisely the $\tau=1$ closure of the companion paper [N15, §7], not a structure an abstract channel supplies for free. The monotonicity route does not eliminate the arithmetic; it hides it inside the assertion "this map is CPTP with these states."

The obligation is not, however, vacuous: the program *does* possess a canonical candidate channel — the apex unitary $U_N$ of [N1]. Building $\Phi$ from it and reading off the defect (§7.4) resolves Obligation 7.3 into a sharp **dichotomy** (Theorem 7.6): the channel delivers the even/metric half unconditionally, is provably blind to the odd/chiral half, and the transfer of step (2) carries no slack at all — so the entire residue is a single *irreversible* step that is the Riemann Hypothesis.

Two cautions delimit the route.

**Remark 7.4 (conditional entropy is the wrong invariant).** The non-negative object furnished by data processing is the monotonicity *defect* $D(\rho\Vert\sigma)-D(\Phi\rho\Vert\Phi\sigma)$, not a conditional entropy. Quantum conditional entropy is sign-indefinite (negative on entangled states); identifying the Weil gap with a conditional entropy would *not* yield non-negativity and would be consistent with $W<0$. Only the defect is unconditionally non-negative — and only once Obligation 7.3(1)–(2) are met.

**Remark 7.5 (the additive dichotomy, again).** Petz monotonicity is a statement in the monotone-metric (Morozova–Chentsov) geometry — the *additive* side of the dichotomy of Remark 7.2. A data-processing argument that closed the gap by additive monotonicity alone would contradict that dichotomy, by which an additive/relative-entropy second-moment positivity over $\mathbb Q$ is either content-free or indefinite, the RH-bearing positivity being multiplicative [N9; P-series]. The resolution is exactly Obligation 7.3(2): the arithmetic content cannot reside in the abstract channel; it is the multiplicative singular-series input that the additive inequality does not see. The monotonicity route is therefore a faithful *reformulation* of the prime-domination problem, with the entire difficulty isolated in the channel-construction step — and that step is the Riemann Hypothesis.

### 7.4 The apex channel: discharging the construction explicitly

We now stop treating $\Phi$ as abstract and build it from the one canonical unitary the program supplies, the **apex unitary** $U_p\in U(p-1)$ of [N1]. This makes Obligation 7.3 fully concrete and exposes exactly which half of it is free and which half is the Riemann Hypothesis.

Fix a prime $p$ and work on the mean-zero hyperplane $H_p\subset\mathbb C^p$, of dimension $p-1$. It carries two orthonormal frames intertwined by $U_p$ [N1, Def. 2.1]: the real **Helmert** (contrast) frame $\{e_k\}$, in which the finite *archimedean* exponential family of Theorem 4.1 is diagonal — it is the time/prolate side of $W_\infty$ — and the **character** (Frobenius) frame $\{\tilde\chi_c\}$ of the additive characters of $\mathbb Z/p$, which carries the *multiplicative/prime* block $(\mathbb Z/p)^\times$ and its Galois monodromy $c\mapsto pc$ [N1 §4; N5]. The restriction "$\mathbb R_+^\times\twoheadrightarrow\{\text{prime lattice}\}$" of Obligation 7.3(1) is, at finite level, the coarse-graining of the archimedean state onto the prime observable, i.e. **dephasing in the character frame**:
$$
\Phi_p(\rho)\;:=\;\sum_{c=1}^{p-1}\Pi_c\,\rho\,\Pi_c,\qquad \Pi_c=\tilde\chi_c\tilde\chi_c^\ast,
$$
the pinching by the character projectors. $\Phi_p$ is completely positive, trace-preserving, unital, and fixes the vacuum $\sigma=I/(p-1)$. For the archimedean state $\rho$ — diagonal in the Helmert frame with populations $p=(p_k)$ — the pushed-forward state $\Phi_p\rho$ is diagonal in the character frame with populations $q=Bp$, where
$$
B_{ck}:=\big|(U_p)_{kc}\big|^2
$$
is the **doubly-stochastic Helmert$\to$character transition matrix** (double-stochasticity is the unitarity of $U_p$). Because $\sigma$ is fixed and $\Phi_p$ is a pinching, the monotonicity defect of Obligation 7.3 collapses to a transparent **classical entropy production**:
$$
\boxed{\;\Delta_p(\rho)\;=\;D(\rho\,\Vert\,\sigma)-D(\Phi_p\rho\,\Vert\,\sigma)\;=\;S(Bp)-S(p)\;=\;D(\rho\,\Vert\,\Phi_p\rho)\;\ge\;0,\;}
\tag{7.1}
$$
the non-negativity being Schur concavity ($Bp\prec p$, Hardy–Littlewood–Pólya majorization), the special case of Petz monotonicity for a pinching. This is the defect of Obligation 7.3, now an explicit, computable object built from $U_p$.

**Theorem 7.6 (the apex channel resolves Obligation 7.3 as a dichotomy).** *Let $\Phi_p$ and $B=|U_p|^2$ be as above. Then:*

*(i) (the even/metric half is delivered, unconditionally).* *$\Delta_p(\rho)\ge0$ for every state, and it is **strictly** positive for every non-vacuum archimedean $\rho$: the contraction $I-B^{\mathsf T}B$ is positive-definite on the mean-zero subspace, its only kernel direction being the vacuum, with a strictly positive spectral gap. To second order in the natural parameter,*
$$
\Delta_p(\rho_\beta)\;=\;\frac{\beta^2}{2}\,\frac{1}{p-1}\,\tilde y^{\mathsf T}\big(I-B^{\mathsf T}B\big)\,\tilde y\;+\;O(\beta^3),
$$
*a positive quadratic form in the centered energy $\tilde y$ — the **even (Fisher/metric) channel** of the parity split [N5, Rem. 6.4]. The $U_p$-channel hands this half over for free.*

*(ii) (the odd/chiral half is invisible — no-go #1).* *$B=|U_p|^2$ is real: $\Delta_p$ depends on $U_p$ only through $|U_p|^2$ and discards the phases $\arg U_p$. Equivalently $\Delta_p$ is invariant under character-frame conjugation $C:\tilde\chi_c\mapsto\tilde\chi_{-c}$ — the parity that separates the even carrier $\zeta$ from the odd chiral $L(\cdot,\chi_3)$ [N5, Rem. 6.4]. Hence the odd/chiral channel, where the RH-bearing sign $c_2<0$ lives, contributes nothing to $\Delta_p$ at first order. A self-adjoint (symmetric) instrument is blind to the antisymmetric current — the same blindness as the Irreversible Blind Spot.*

*(iii) (the transfer carries no slack — no-go #2).* *The explicit-formula transfer $\tau_n=(-1)^n$ of [N5, Theorem 6.2] that carries the apex (archimedean-source) cumulants to the Hardy–Littlewood prime weights is the particle–hole involution $X\mapsto 1-X$, $\kappa_n(\mathbf 1-X)=(-1)^n\kappa_n(X)$ — a reflection, hence a reversible relabeling. By Petz's equality theorem a reversible (sufficient) channel has monotonicity defect identically $0$. So the slack of Obligation 7.3 cannot arise from the transfer relating the two potentials.*

*(iv) (what remains is exactly RH — [C]).* *By (ii)–(iii) the only possible source of strictly positive slack $W>0$ is the **irreversible** continuation of the per-block defects $(7.1)$ summed across the form-factor boundary $\tau=1$ — the ramp$\to$plateau hand-off of [N15, §7], i.e. the Hardy–Littlewood singular-series closure. No finite conductor-block channel implements this continuation. That continuation is the Riemann Hypothesis.*

*Parts (i)–(iii) are exact and unconditional; part (iv) is [C]. The construction, the strict positivity and spectral gap, the order-2 form, the reality of $B$, and the vanishing of the reflection defect are certified to $40$–$50$ digits in $\texttt{empirical/p\_infinity/probe\_obligation73\_pinching\_channel.py}$ at $p=3,5,7,11,13$.*

The theorem is the honest discharge of Obligation 7.3. It does *not* prove RH; it converts the open obligation into a structural fact. The data-processing route is genuine and its defect is now an explicit, strictly positive, $U_p$-built quantity — but it is a *symmetric* (even/metric) defect by construction, and the two no-gos (ii)–(iii) show why the arithmetic content cannot leak into it: the chiral half is a phase the modulus-squared channel never sees, and the apex$\leftrightarrow$prime transfer is reversible. The whole of the Riemann Hypothesis is thereby localized to a single *irreversibility* across $\tau=1$ — precisely where Remark 7.5 said the difficulty must sit, now pinned to one identifiable step rather than hidden in "this map is CPTP." This also fixes the precise sense of Remark 7.4: the non-negative object is the defect $(7.1)$, it exists and is strictly positive, but it is the even-channel defect, and conditional-entropy/odd-channel sign data does not enter it.

### 7.5 What the missed chiral content is — and what it is not

Theorem 7.6(ii) says the symmetric defect is blind to the odd/chiral sector. It is worth naming the missed object correctly, because a natural candidate fails an honest audit and the failure is instructive.

**The correct object.** For the archimedean state $\rho$ (diagonal in the Helmert frame with real populations $p$), the character-frame density matrix is $\rho_\chi=U_p\operatorname{diag}(p)\,U_p^\ast$, a Hermitian matrix. The metric defect $(7.1)$ depends only on its *diagonal* $q_c=(\rho_\chi)_{cc}=\sum_k|U_{kc}|^2p_k$ — that is why it is built from $|U_p|^2$ alone (Theorem 7.6(ii)). The missed content is the **off-diagonal phase**, concretely the antisymmetric part
$$
C(\rho)\;:=\;\operatorname{Im}\rho_\chi,\qquad C(\rho)_{cc'}=\sum_k p_k\,\operatorname{Im}\!\big(U_{kc}\,\overline{U_{kc'}}\big),
$$
the genuine chiral current of the state in the multiplicative frame. Two properties make it the right object (certified, $\texttt{empirical/p\_infinity/probe\_obligation73\_chirality\_audit.py}$): it **vanishes at the self-dual vacuum** $\rho=\sigma$ (then $\rho_\chi=\sigma$ is real; an arrow must vanish at equilibrium), and it is **genuinely phase-borne** — rephasing the characters moves $C(\rho)$ while leaving the metric defect untouched. The chiral content the defect misses is therefore a *state-dependent, gauge-covariant phase* (a Berry/Bargmann quantity), whose gauge-invariant content is carried by the character-triangle products $\operatorname{Im}\big[(\rho_\chi)_{cc'}(\rho_\chi)_{c'c''}(\rho_\chi)_{c''c}\big]$. Its definite sign — for the relevant prolate test states, summed across the primorial tower — is exactly the program's $c_2<0$, i.e. $L(\tfrac12,\chi_3)\ne0$; this is the Riemann-Hypothesis content, and Theorem 7.6 locates it but supplies no reduction of it. The honest statement is the dichotomy of Theorem 7.6 itself: the DPI defect delivers the even/metric half unconditionally and is structurally blind (phase-blind, by (ii); reversible-transfer, by (iii)) to this chiral phase. No more, no less.

**Remark 7.8 (a phase-blind proxy that does *not* work — recorded so it is not repeated).** It is tempting to read the chiral content off the *modulus* asymmetry of the transition, via the antisymmetric matrix $J:=B-B^{\mathsf T}$ ($B=|U_p|^2$). This object has genuine and certifiable structure — $J=0$ at $p=3$ and $J\neq0$ for $p\ge5$; $B$ has real spectrum (conveyor-type non-normality) with a departure-from-normality gap $G_p=\sum_i\sigma_i(B)-\sum_i|\lambda_i(B)|$ that grows ($G_p\approx0.055,0.096,0.147,0.164$ at $p=5,7,11,13$, and $0.081,0.226,0.230$ along $N=6,30,210$); $J$ is $\ge97\%$ odd under the character reflection $c\mapsto-c$ and is irreducibly cross-prime ($45\%$ of $\|J\|^2$ at $N=6$ couples different CRT sectors). **But $J$ is not the chiral current.** Being a function of $|U_p|^2$, it is *phase-blind* (rephasing characters leaves it invariant) and *state-independent* (it is nonzero at the vacuum, where the true arrow vanishes) — the two properties the audit checks and the genuine $C(\rho)$ has oppositely. Identifying $J$'s flux-sign with $c_2<0/L(\tfrac12,\chi_3)$ — as an earlier draft of this section did — is therefore an overreach: $J$ measures a real transpose-asymmetry of $|U_p|^2$, not the chiral phase. The structural facts are certified in $\texttt{probe\_obligation73\_irreversibility\_gap.py}$ and $\texttt{probe\_obligation73\_primorial\_tower.py}$; their RH interpretation is withdrawn. The lesson is exactly Theorem 7.6(ii): the chiral half cannot be recovered from any modulus-squared (symmetric) construction, $J$ included.

**Remark 7.9 (the genuine object is correct but offers no reduction — audited).** The correct chiral object $C(\rho)=\operatorname{Im}\rho_\chi$ passes every check $J$ failed and is audited in $\texttt{empirical/p\_infinity/probe\_obligation73\_genuine\_chiral\_audit.py}$ (GREEN, $p=7$, $N=6$): it is **exactly** parity-odd ($R\,C\,R=-C$ to machine $\varepsilon$, i.e. $100\%$ in the odd/$\chi_3$ sector, not $J$'s $97\%$), it **vanishes at the vacuum**, and its gauge-invariant content (the individual Bargmann triangle phases $\operatorname{Im}[(\rho_\chi)_{ab}(\rho_\chi)_{bc}(\rho_\chi)_{ca}]$) is invariant under character rephasing while the entrywise $\operatorname{Im}\rho_\chi$ is only covariant. But the audit also exhibits the obstruction to any shortcut: for a **real** (time-reversal-symmetric) archimedean state the chiral current is *purely* parity-odd, so every parity-even (symmetric, net) readout is exactly zero — a nonzero scalar appears only against a parity-**odd** weight, i.e. an *orientation*. At $N=6$ that orientation is the choice $\chi_3$ versus $\overline{\chi_3}$ (characters $2\leftrightarrow4$), and the scalar $\operatorname{Im}(\rho_\chi)_{2,4}=+0.00745$ flips sign under it. Selecting the orientation that makes the chiral signal definite is exactly selecting the sign of $L(\tfrac12,\chi_3)$. The genuine object therefore localizes the Riemann-Hypothesis content precisely — it *is* the $\chi_3$ chiral phase — but supplies no reduction of it: the sign is the arithmetic input, not an output of the geometry. This confirms the honest reading of Theorem 7.6: the dichotomy is the result; the chiral sign is RH, undiminished.

---

## 8. Conclusion

The archimedean Weil positivity is not an accident of the Gamma factor; it is a law of information geometry. $W_\infty(f)$ is the relative entropy of the time–frequency profile of $f$ from the maximum-entropy profile, equivalently the Fenchel–Young gap of a strictly convex log-partition function whose convexity is the logarithmic convexity of the archimedean local factor. Its non-negativity is Gibbs' inequality, with equality exactly at the self-dual configuration. This is the conceptual reason Connes identified as missing — a thermodynamic one: information distance cannot be negative. It is, by construction and by the arithmetic, confined to the archimedean place; extending a positivity principle across the prime contribution, which enters as a Legendre conjugate with the opposite sign, is the Riemann Hypothesis and remains open.

---

## Appendix A. A finite worked instance

For concreteness we record the exact finite identities behind Theorems 3.4 and 4.1, with an accompanying high-precision computational certificate (40 significant digits). Take a small modulus $N$ and a centered energy $y$ on $\mathbb Z/N$; form $\Phi(\beta)=\log\frac1N\sum_s e^{\beta y(s)}$, the escort $P_\beta$, and the conjugate potential $\Phi^\ast(\xi)$ at $\xi=\Phi'(\beta)$. The certificate confirms, for several ledgers ($\mathbb Z/6$ arithmetic, $\mathbb Z/6$ prime-counting, $\mathbb Z/4$ quadratic) and several inverse temperatures:

1. **Conjugate potential $=$ relative entropy.** $\Phi^\ast(\xi)=\log N-H(P_\beta)=D(P_\beta\Vert u)$, the three quantities agreeing to $<10^{-30}$.
2. **Fenchel–Young $=$ Bregman $=$ relative entropy of escorts.** $\Phi(\beta_1)+\Phi^\ast(\xi_2)-\beta_1\xi_2=D(P_{\beta_2}\Vert P_{\beta_1})\ge 0$, to the same precision.
3. **Gibbs.** $D(P_\beta\Vert u)\ge 0$, vanishing exactly at $\beta=0$ (the uniform vacuum).
4. **Non-triviality.** The archimedean density $\Omega_\infty(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}{2})-\log\pi$ is negative near the origin, with $\Omega_\infty(0)=-5.3721834\ldots<0$; hence the naive quadratic form $\int|\hat f(r)|^2\,\Omega_\infty(r)\,dr$ is indefinite, and the positivity of $W_\infty$ is the global non-negativity of a relative entropy rather than positivity of a kernel.

These confirm at the finite level that the object identified in Theorem 4.1 is a relative entropy, and that its positivity is the non-trivial global fact captured by Gibbs' inequality, not an artifact of a positive kernel.

---

## References

**Internal (used as cited theorems).**

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$.* (Definition 2.1: the apex unitary $U_N$ intertwining the Helmert and character frames; the radical–cyclotomic split; the Galois/Frobenius column action $c\mapsto ac$ used in §7.4.)

[T0] Murillo Montero, L. (2026). *Gauge Selection and the Fourier–Mellin Simplex.* (Theorem 2.7: the conjugate potential of the log-partition function equals the relative entropy $D(P_\beta\Vert u)$; Bregman $=$ relative entropy.)

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* (Identification of the relevant operator with the Connes–Consani archimedean operator; multiplier $\Omega_\infty$.)

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.* (Assembly of the archimedean functional from the local data.)

[T15] Murillo Montero, L. (2026). *Finite-to-Archimedean Completion.* (Completion of the finite families to the archimedean continuum; the archimedean factor as terminal boundary correction.)

[N9] Murillo Montero, L. (2026). *The Cross-Prime Fusion Criterion.* (The additive/multiplicative dichotomy referenced in Remark 7.2.)

[N15] Murillo Montero, L. (2026). *The Two Potentials of the Weil Form.* (The prime potential as $\log\zeta$; the $\tau=1$ singular-series closure of §7.3.)

**Classical and external.**

[We] Weil, A. (1952). *Sur les "formules explicites" de la théorie des nombres premiers.* Comm. Sém. Math. Univ. Lund.

[Co] Connes, A. (2026). *The Riemann Hypothesis: Past, Present and a Letter Through Time.* arXiv:2602.04022. (The time–frequency presentation (2.1); the remark on p. 21 concerns *Yoshida's numerical proof*; §7.2–7.4 supply the Sonin-space conceptual reason and extend it to the primes.)

[CC] Connes, A., Consani, C. (2021). *Weil positivity and the trace formula: the archimedean place.* Selecta Math. 27, art. 77 (arXiv:2006.13771). (Proof of archimedean positivity **and** its conceptual reason via compression of the scaling action onto Sonin's space — the operator-theoretic answer this note re-describes information-geometrically.)

[Yo] Yoshida, H. *On Hermitian forms attached to the zeta function.* (Numerical positivity of the archimedean form.)

[SPL] Slepian, D., Pollak, H., Landau, H. (1961). *Prolate spheroidal wave functions, Fourier analysis and uncertainty, I–II.* Bell System Tech. J.

[AN] Amari, S., Nagaoka, H. (2000). *Methods of Information Geometry.* AMS/Oxford. (Conjugate of the log-partition $=$ relative entropy; Fenchel–Young gap $=$ Bregman divergence — the standard identity this note specializes.)

[Ni24] Nielsen, F. (2024). *Divergences Induced by the Cumulant and Partition Functions of Exponential Families.* Entropy 26(3):193. (The convex-duality/Bregman/KL identity in the form used here.)

[GN] Garbouge, S., Nielsen, F. (2021). *A note on some information-theoretic divergences between zeta distributions.* arXiv:2104.10548 (and MDPI follow-up, 2024). (**Prior art for the central content:** $\log\zeta$ as the strictly convex cumulant function of the zeta distribution, with explicit Bregman/relative-entropy divergences — the zeta-function instance of this note's reading, already in print.)

[Ro] Rockafellar, R. T. (1970). *Convex Analysis.* Princeton.

[Ar] Artin, E. (1964). *The Gamma Function.* (Bohr–Mollerup: logarithmic convexity of $\Gamma$.)

[Bo] Bombieri, E. (2000). *Remarks on Weil's quadratic functional in the theory of prime numbers.* Atti Accad. Naz. Lincei 11, 183–233. (The Weil functional as a Hermitian form.)

[Pe] Petz, D. (1986). *Quasi-entropies for finite quantum systems.* Rep. Math. Phys. 23, 57–65. (Monotonicity of relative entropy / quasi-entropies under CPTP maps.)

[Li] Lindblad, G. (1975). *Completely positive maps and entropy inequalities.* Comm. Math. Phys. 40, 147–151. (The quantum data-processing inequality.)

[Uh] Uhlmann, A. (1977). *Relative entropy and the Wigner–Yanase–Dyson–Lieb concavity in an interpolation theory.* Comm. Math. Phys. 54, 21–32.
