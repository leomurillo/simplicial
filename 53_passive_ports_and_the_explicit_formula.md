# 53 — Passive Ports and the Explicit Formula

## The Riemann Hypothesis as the Port Constraint at the Archimedean Place

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — October 1, 2026*

<!--
Program record. Bridge paper between the Port Principle (PortPrinciple.md: passivity, wave variables, Halmos /
Sz.-Nagy–Foias dilation, defect Gram, boundary rule, lift calculus) and the RH line (P∞-A, P∞, N14: Herglotz /
de Branges / reflection positivity / archimedean relative entropy). A 2026-10-01 grep of the 364 manuscripts found
that the two lines use the same operator theory (dilation and model spaces) without a single cross-reference.
This paper does NOT prove RH. Every equivalence in Theorem 3.1 is classical or assembled from classical results;
the deposit is the identification, the Foster/ledger reading (Pick rank = ledger dimension), the forced-ledger
corollary for Hilbert–Pólya programs, the gain/boundary/lift readings, and matched-pair certificates.
Certificate: empirical/passive_ports/p53_bridge_cert.py (K1, K2' exact; K3 50-digit witnesses + control).
K2 failed as pre-registered (PD demanded where only PSD holds) and is retained; K2' is post-diagnosis.
Tiers [P]/[A]/[C].
2026-10-10: §4.6 added (finite-resolution port, Props 4.6–4.9, matched pair zeta / L(chi) / DH; certificate
empirical/passive_ports/p53_finite_port_probe.py, K4). Leo's framing: beta = 1/2 is balance (Prop 4.5); zero means
below resolution; the third law as the finite-resolution principle.
2026-10-11: §§4.7-4.12 (third-law curve, instrument, Castelnuovo-Severi over Q, arithmetic RR, arithmetic Frobenius,
optimal auxiliary + parity identity). Peer (Astro) corrections folded with credit [As26a, As26b]: N_K rational not
integral; spur fit uncontrolled remainder; m(x) != O(x^-alpha) for alpha > 1/2; integral majorants. Certificates K5-K10.
2026-10-11 (later): §4.13 uniform construction = Mobius on the hyperbola cells (Thm 4.18, Cor 4.19, K11 to 1e9).
The polytope bound sits between RH and RH + cell-wise sqrt cancellation of mu; RH alone gives x^(2/3+eps).
§4.14: averaged over x the polytope is an exact RH-equivalent (Thm 4.20; Lemma 4.21 = RH mean-square Mobius in
short intervals via Plancherel + 1/zeta on Re s > 1/2; Landau on int psi). K12.
-->

---

> *No port gives more than it takes. For the primes, that sentence is the Riemann Hypothesis.*

---

## Abstract

The Port Principle studies one constraint — *no port gives more than it takes* — and what it forces when lifted across time, copies and symmetry. In the frequency domain the constraint says that a port's input impedance is **positive-real**, its scattering function is a **Schur contraction**, and its **defect Gram** (Pick) matrices are positive; by dilation theory it says that the port is the corner of a **lossless ledger**. The program's Riemann-Hypothesis line reached the same objects from the other side: P∞-A reduced RH to the Herglotz property of $m_B=-\Xi'/\Xi$ and the positivity of the de Branges canonical system. The two lines never cite each other.

We show they describe one port. Define the **zeta port** by its impedance
$$Z_\xi(s)=\frac{\xi'}{\xi}\Big(\tfrac12+s\Big),\qquad \operatorname{Re}s>0 .$$
**Theorem 3.1** assembles, from classical results, the equivalence of RH with each of: $Z_\xi$ positive-real (Lagarias' positivity); its Cayley scattering function contractive; all its defect-Gram matrices positive; the **Foster form** $Z_\xi(s)=\sum_{\gamma>0}2s/(s^2+\gamma^2)$ with real $\gamma$ — an infinite series chain of lossless LC tanks with $C=\tfrac12$, $L_\gamma=2/\gamma^2$, one tank resonating at each zero ordinate; and the de Branges / Sz.-Nagy–Foias statement that a lossless ledger $\mathcal H(E_B)\cong K_{\Theta_B}$ exists. **Lemma 3.2** shows the de Branges reproducing kernel *is* the defect Gram of the scattering function.

The Port Principle then contributes readings with content. **The defect Gram's rank is the ledger's dimension** (Corollary 4.1): a finite Foster network with $n$ tanks has Pick matrices of rank exactly $2n$, while the zeta port's are positive definite at every finite set of distinct points. **The ledger is forced** (Corollary 4.2): minimal lossless realizations of the zeta port are unitarily equivalent, so Hilbert–Pólya constructions that realize this port can differ only outside their minimal part. **Off-line zeros are gain** (Proposition 4.3): each zero is a mode $e^{(\rho-1/2)t}$ of the normalized prime signal, undamped iff on the line. **The functional equation is losslessness** (Proposition 4.5): evenness of $\xi(\tfrac12+s)$ makes $Z_\xi$ odd, hence a pure reactance. The archimedean place, already passive (Connes–Consani; N14), is the port's passive element, the primes enter with the gain sign, and the Port Principle's *boundary rule* reads RH as passivity of the fully completed (adelic) port [A].

At finite resolution the port becomes a test (§4.6). Truncate the primon gas to the primes up to $X$ and build the balanced port from it. Balance is then free at every resolution. A finite free gas has no partition-function zeros, so its port loses no zero from the line, and it is passive above a finite height. The Davenport–Heilbronn port, an interference of two free gases, drains the line at every height: at $X=13$ and $t\le1000$ it has $29$ off-line zeros and exactly $58$ fewer on-line zeros than the free ports. RH sits at the one limit that is not a stage: the pole-compensated free energy must converge down to the balance line (Proposition 4.9).

Measured as a third-law curve (§4.7), resolution trades certification off the line for precision on it. The certified band shrinks like $c/\log X$, with $c\approx1.5$–$2$, while the zeros on the line sharpen. The passive count reads $\zeta$ correctly at every tested height up to $t=3220$, and it reads DH wrong by exactly two per off-line zero.

Theorem 4.10 explains why: the balance count minus the line count equals twice the off-line count plus the variation of Selberg's remainder $S_X-S$. A finite free port is therefore an off-line zero counter whose only error is arithmetic. It reads $250$ windows of $\zeta$ to $t=5100$ and the DH matched pair correctly at height-matched resolution. An exact certificate verifies the identities and a Foster matched pair (real zeros give positive tanks and a rank-$2n$ Gram; an off-line pair gives a right-half-plane pole and a negative Gram entry). A 50-digit witness on $\zeta$ checks positive-realness on a grid, positive-definite Pick matrices near the first six zeros, a dissipation-spectrum count of the zeros ($10.0023$ against $10$), and the Foster tanks at the actual zero ordinates ($1.1\times10^{-4}$ relative error with tail). A control with a planted off-line quartet is flagged.

Sections 4.9–4.12 carry Weil's proof over $\mathbb F_q$ across to $\mathbb Q$ step by step.
- *Castelnuovo–Severi.* The Castelnuovo–Severi Gram becomes the two-packet Weil Gram, whose diagonal is archimedean and unconditional (Theorem 4.14). Two prime clocks make the condition an exact equivalence (Theorem 4.15).
- *Riemann–Roch.* Riemann–Roch on $\overline{\operatorname{Spec}\mathbb Z}$ is the functional equation, and the Landau half of Bombieri–Stepanov is the one-sided ledger.
- *The Stepanov half.* It becomes a linear program with no primes in it. Factorial auxiliaries vanishing on the dyadic window are optimized subject to floor positivity.
  - The exact optimum is the Legendre sieve.
  - Economical auxiliaries are forced to be the Möbius function on the heavy scales (Theorem 4.16).
  - The a priori optimum, with Stirling's formula in place of every factorial, bounds $\psi(x)-\psi(x/2)$ by $x/2+(0.39$–$0.42)\sqrt x\log x$ for $10^3\le x\le10^7$.
  - A uniform bound of that shape would prove RH (Theorem 4.17).
  - The Möbius function itself is a uniform feasible point (Theorem 4.18). Its height is the prime window plus the Mertens variation over the hyperbola cells, measured to $x=10^9$.
  - Averaged over $x$, the polytope bound is equivalent to RH (Theorem 4.20). RH supplies the cell-by-cell parity balance in mean square (Lemma 4.21), and Landau's positivity returns RH.
- *The parity behind the square root has three exact forms:*
  - the spheres of Björner's squarefree complex, through the prime-2 cone;
  - the squares, which set the abscissa $\tfrac12$ of $\zeta(2s)/\zeta(s)$;
  - over $\mathbb F_q[T]$, a constant window Euler characteristic, explained by Stickelberger and Grothendieck–Lefschetz.

Finite witnesses are necessary-only. **RH is not proved here; it is placed** — as the program's base inequality, evaluated at the archimedean place.

---

## 1. Two lines, one inequality

The **Port Principle** (PortPrinciple.md) organizes impedance, fluctuation, measurement and information around one inequality. In wave variables (its Definition 2.2) the power absorbed by a port is $\|a\|^2-\|b\|^2$, and the port constraint is $\|b\|\le\|a\|$. Its base results are dilation theorems (Halmos, Egerváry, Sz.-Nagy–Foias): a passive port is the corner of a lossless ledger (Theorems 4.1–4.3), whose port-visible part is the defect Gram $I-SS^\dagger$, independent of which ledger is chosen (Proposition 4.4). Passivity at every instant forces causality (Theorem 5.1), and an *active* port is handled by a boundary rule: enlarge the boundary until the non-passive source is inside (Definition 2.5).

The **RH line** of the program (P∞, P∞-A, N13–N15) reduced the Riemann Hypothesis to a single positivity, seen through many equivalent faces:
$$\mathrm{RH}\iff m_B=-\Xi'/\Xi\ \text{Herglotz}\iff E_B=\Xi+i\Xi'\ \text{Hermite–Biehler}\iff H(t)\succeq0\iff\text{reflection positivity}$$
(P∞-A, §3). Its archimedean half is a theorem (Connes–Consani [CC]) and is a relative entropy (N14).

A Herglotz function is a passive impedance written in the upper half-plane. A Hermite–Biehler function generates a meromorphic inner function, which is a lossless scattering function. A de Branges space is a Sz.-Nagy–Foias model space. The two lines are therefore using **the same operator theory** — dilation and model spaces — under different names. Yet a search of the program's 364 manuscripts finds Sz.-Nagy–Foias only in the Port Principle, and de Branges, Lax–Phillips and Herglotz only in the RH line. This paper writes the missing bridge.

**What is classical.** Every equivalence in Theorem 3.1 is classical or assembled from classical results: Lagarias' positivity [La99], Cayley, Pick–Nevanlinna, Foster's reactance theorem [Fo24], the Hadamard product, the de Branges structure theory [dB68], and its identification with model spaces [MP05, SNF70]. **What is new here** is the identification across the program, the ledger-dimension reading of the defect Gram, the forced-ledger corollary, the readings in §4, and the matched-pair certificates of §5.

## 2. The zeta port

Let $\xi(w)=\tfrac12w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w)$, entire of order 1, real on $\mathbb R$, with $\xi(w)=\xi(1-w)$. Its zeros are the non-trivial zeros $\rho$ of $\zeta$.

**Definition 2.1 (the zeta port).** The *zeta port* is the one-port whose input impedance is
$$Z_\xi(s)=\frac{\xi'}{\xi}\Big(\tfrac12+s\Big)=\frac{1}{\tfrac12+s}+\frac{1}{s-\tfrac12}-\frac{\log\pi}{2}+\frac12\,\psi\Big(\frac{\tfrac12+s}{2}\Big)+\frac{\zeta'}{\zeta}\Big(\tfrac12+s\Big).$$
Here the *passive side* is the right half-plane $\operatorname{Re}s>0$, and the critical line is the imaginary axis $s=it$. Its *scattering function* is the Cayley transform $S_\xi=(Z_\xi-1)/(Z_\xi+1)$.

In the upper-half-plane coordinate $z=-is$ of the de Branges literature, put $\Xi(z)=\xi(\tfrac12+iz)$ (real-entire and even), and
$$E_B=\Xi+i\Xi',\quad A=\Xi,\quad B=-\Xi',\quad \Theta_B=E_B^\#/E_B,\quad m_B=B/A=-\Xi'/\Xi,$$
where $F^\#(z)=\overline{F(\bar z)}$. Using the evenness of $\Xi$, one checks
$$Z_\xi(s)=-i\,m_B(is),$$
so the right half-plane of $s$ is the upper half-plane of $z$.

**Proposition 2.2 (two forms of one constraint) [P].**
1. $\operatorname{Re}Z>0\iff|S|<1$ on $\operatorname{Re}s>0$, because $|Z-1|^2-|Z+1|^2=-4\operatorname{Re}Z$.
2. In the $z$-plane, $m=i(1-\Theta)/(1+\Theta)$ identically, and $\operatorname{Im}m>0\iff|\Theta|<1$ on $\operatorname{Im}z>0$.

These are the continuous-variable forms of the Port Principle's Proposition 2.3: net passivity is a positive symmetric part, which is equivalent to a contractive Cayley transform. *Certificate K1(a, d).*

## 3. The theorem: RH as the port constraint

**Theorem 3.1 (the zeta port is passive iff RH) [P, assembled].** The following are equivalent:
1. **(RH)** Every non-trivial zero of $\zeta$ has real part $\tfrac12$.
2. **(Positive-real impedance)** $Z_\xi$ is holomorphic on $\operatorname{Re}s>0$ with $\operatorname{Re}Z_\xi>0$ there [La99].
3. **(Contractive scattering)** $|S_\xi|<1$ on $\operatorname{Re}s>0$: outgoing never exceeds incoming.
4. **(Positive defect Gram)** For every finite set of points $s_1,\dots,s_n$ in $\operatorname{Re}s>0$, the Pick matrix
$$P_{jk}=\frac{Z_\xi(s_j)+\overline{Z_\xi(s_k)}}{s_j+\bar s_k}$$
is positive semidefinite (and then positive definite at distinct points).
5. **(Foster form: a lossless LC chain)** $Z_\xi(s)=\sum_{\gamma>0}\dfrac{2s}{s^2+\gamma^2}$, with every $\gamma$ real. Each term is a parallel tank with $C=\tfrac12$ and $L_\gamma=2/\gamma^2$, resonating at $\gamma$, and the tanks are in series.
6. **(Lossless ledger)** $E_B$ is Hermite–Biehler; equivalently $m_B$ is Herglotz, and $\Theta_B$ is a meromorphic inner function. The de Branges space $\mathcal H(E_B)$ then exists and is isometric to the model space $K_{\Theta_B}=H^2\ominus\Theta_BH^2$, the lossless (Sz.-Nagy–Foias / Lax–Phillips) realization of the scattering function $\Theta_B$.
7. **(Reflection positivity)** The explicit-formula system is reflection-positive; equivalently, the reconstructed scaling semigroup is positive-energy (P∞-A, Theorem 3).

*Proof.*

**(1)⇔(5).** By Hadamard, pairing the zeros $\rho=\tfrac12\pm i\gamma$ (with $\gamma$ complex in general),
$$\xi(\tfrac12+s)=\xi(\tfrac12)\prod_{\gamma}\big(1+s^2/\gamma^2\big).$$
The product converges absolutely because $\sum|\rho-\tfrac12|^{-2}<\infty$, and it is even because $\xi(\tfrac12+s)=\xi(\tfrac12-s)$. Logarithmic differentiation gives the series unconditionally. Its terms are positive LC tanks exactly when every $\gamma$ is real, which is RH.

**(5)⇒(2).** For real $\gamma$, $\frac{2s}{s^2+\gamma^2}=\frac1{s-i\gamma}+\frac1{s+i\gamma}$, and $\operatorname{Re}\frac1{s\mp i\gamma}=\frac{\operatorname{Re}s}{|s\mp i\gamma|^2}>0$. The series converges absolutely, so $\operatorname{Re}Z_\xi>0$.

**(2)⇒(1).** An off-line zero $\tfrac12+s_0$ can be taken with $\operatorname{Re}s_0>0$, because zeros come in pairs $\pm s_0$ by evenness. It is a pole of $Z_\xi$ with positive residue equal to its multiplicity. Near a pole, $Z_\xi$ takes values of every argument, so $\operatorname{Re}Z_\xi<0$ somewhere in $\operatorname{Re}s>0$.

**(2)⇔(3).** This is Proposition 2.2.

**(2)⇔(4).**
- (⇐) Diagonal entries give $\operatorname{Re}Z_\xi(s_j)/\operatorname{Re}s_j\ge0$, and holomorphy fails at any right-half-plane pole, where a nearby diagonal entry is negative.
- (⇒) This is the Riesz–Herglotz representation, under which the kernel is a positive superposition of the rank-one kernels $f_c(s_j)\overline{f_c(s_k)}$ with $f_c(s)=1/(s-c)$, $\operatorname{Re}c=0$ (Lemma 3.2 makes this explicit for the Foster form).
- Strict definiteness at distinct points follows because Cauchy matrices $[1/(s_j-c_k)]$ built from infinitely many distinct $c_k$ have full rank (Corollary 4.1).

**(2)⇔(6).** Use $Z_\xi(s)=-i\,m_B(is)$ and Proposition 2.2.2. Hermite–Biehler means $|E_B^\#|<|E_B|$ on the upper half-plane, i.e. $|\Theta_B|<1$; inner-ness on $\mathbb R$ holds because $|E_B^\#(x)|=|E_B(x)|$ for real $x$. The isometry $\mathcal H(E)\to K_\Theta$, $F\mapsto F/E$, is de Branges' structure theory in the form of [MP05]. $K_\Theta$ is the Sz.-Nagy–Foias model space of the compressed shift with characteristic function $\Theta$ [SNF70], equivalently the Lax–Phillips realization of the scattering function $\Theta$ [LP67].

**(6)⇔(7).** This is P∞-A, which assembles Neeb–Ólafsson reflection positivity with the de Branges / Herglotz representation. $\square$

**Lemma 3.2 (the de Branges kernel is the defect Gram) [P].** For any real-entire $A,B$ with $E=A-iB$, $\Theta=E^\#/E$, $m=B/A$, and $\bar w$ written $w^\ast$:
$$K_E(w,z):=\frac{E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}}{2\pi i\,(\bar w-z)}=E(z)\overline{E(w)}\;\frac{1-\Theta(z)\overline{\Theta(w)}}{2\pi i\,(\bar w-z)},$$
$$\frac{m(z)-\overline{m(w)}}{z-\bar w}=\frac{\pi\,K_E(w,z)}{A(z)\overline{A(w)}} .$$
So the de Branges reproducing kernel is, up to the outer factor $E(z)\overline{E(w)}$, the defect kernel $1-\Theta\Theta^\ast$ of the scattering function. That is the continuous form of the Port Principle's $\Delta_{\rm out}=I-SS^\dagger$ (Proposition 4.4). The Pick kernel of the impedance is congruent to it, by the diagonal scaling $1/A$.

*Proof.* Direct algebra: the numerator equals $2i\big(A(z)\overline{B(w)}-B(z)\overline{A(w)}\big)$. *Certificate K1(b, c)*, exact and symbolic. $\square$

## 4. What the Port Principle adds

### 4.1 The defect Gram's rank is the ledger's dimension

**Corollary 4.1 (rank = ledger dimension) [P].**
- A Foster network with $n$ tanks, $Z(s)=\sum_{k\le n}2s/(s^2+a_k^2)$ with $a_k>0$, has Pick matrices $P=FF^\ast$, where $F_{jc}=1/(s_j-c)$ and $c$ ranges over the $2n$ poles $\pm ia_k$. Every Pick matrix is therefore positive semidefinite, and its rank is exactly $2n$ once the sample has at least $2n$ distinct points. That rank is the McMillan degree, i.e. the dimension of the minimal lossless ledger.
- If RH holds, the zeta port has infinitely many tanks, and its Pick matrix at any $n$ distinct points is positive *definite*.

*Proof.* The factorization is Lemma 3.2 applied termwise. The rank claim is the non-vanishing of Cauchy determinants. $\square$

*Certificates.*
- K2′: $(z^2-1)(z^2-4)(z^2-9)$, three tanks $(C,L)=(\tfrac12,2),(\tfrac12,\tfrac12),(\tfrac12,\tfrac29)$. The exact identity $P=FF^\ast$ holds, with rank $6$.
- K3(b): the zeta port at twelve points near its first six zeros, minimum eigenvalue $1.0\times10^{-9}>0$.

The pre-registered K2 demanded positive *definiteness* for the finite network and failed. The failure is retained: it is what exposed the rank statement.

### 4.2 The ledger is forced

**Corollary 4.2 (minimal lossless realizations are unique) [P, cited].**
- If RH holds, the zeta port has a minimal conservative (lossless) realization. Any two minimal conservative realizations of its scattering function are unitarily equivalent, by Arov's theorem on minimal passive systems [Ar79] and the uniqueness of the Sz.-Nagy–Foias model [SNF70].
- In canonical-system form, the Hamiltonian $H(t)\succeq0$ is determined by $m_B$ up to reparametrization (de Branges' uniqueness theorem; [Re18]).
- In $\mathcal H(E_B)$, multiplication by $z$ has self-adjoint extensions with spectra equal to the zero sets of $A\sin\alpha-B\cos\alpha$ [dB68, Thm 22]. At $\alpha=\pi/2$ that spectrum is the set of zero ordinates of $\Xi$.

**Reading [A].** This is the Port Principle's Proposition 4.4 — *the defect Gram does not depend on the ledger* — at the scale of the program's Hilbert–Pólya question.
- Any Hilbert–Pólya construction that realizes this *port* (this scattering function, this coupling channel) has the same minimal part, $\mathcal H(E_B)$ with the de Branges operator. Two such constructions can differ only in non-minimal ("dark") components, or by realizing *different* port data.
- The de Branges route is circular as a proof strategy, as is classical: the ledger exists iff RH. Its value here is organizational. It tells competing constructions (the prolate/Sonin route of Connes–Consani–Moscovici, the screw-function realization of Suzuki, the program's apex operators) what they must agree on.

### 4.3 Off-line zeros are gain

**Proposition 4.3 (gain reading) [P cited; A reading].**
- RH $\iff \psi(x)-x=O(x^{1/2}\log^2x)$ [vK01].
- A zero with $\operatorname{Re}\rho>\tfrac12$ forces $\psi(x)-x=\Omega_\pm(x^{\operatorname{Re}\rho-\epsilon})$ for every $\epsilon>0$ [In32].

In logarithmic time $t=\log x$, the truncated explicit formula writes the normalized prime signal as
$$e^{-t/2}\big(\psi(e^t)-e^t\big)=-\sum_\rho\frac{e^{(\rho-\frac12)t}}{\rho}+O(e^{-t/2}).$$
Each zero is a mode whose growth rate $\operatorname{Re}\rho-\tfrac12$ is exactly the real part of the corresponding pole $s_0=\rho-\tfrac12$ of $Z_\xi$.
- **On the line,** every mode is undamped: the normalized signal is the free *echo* of a lossless port, almost periodic, as for a pure-point spectrum (Port Principle Theorem 4.5).
- **Off the line,** a mode grows: the port gives more than it takes.

RH is the statement that the prime signal, once normalized by the critical amplitude $\sqrt x$, has no gain.

### 4.4 The boundary rule: the archimedean place is the passive element

Split the impedance by places. For $\operatorname{Re}s>\tfrac12$, where the Dirichlet series converges,
$$Z_\xi=Z_\infty+Z_{\rm fin},\qquad Z_\infty(s)=\frac{1}{\tfrac12+s}+\frac{1}{s-\tfrac12}-\frac{\log\pi}2+\frac12\psi\Big(\frac{\tfrac12+s}2\Big),\qquad Z_{\rm fin}(s)=-\sum_{n}\Lambda(n)\,n^{-1/2-s}.$$
The archimedean place carries a theorem-level positivity (Connes–Consani's archimedean Weil positivity [CC]), which N14 identifies as a relative entropy, i.e. the Port Principle's bath passivity. The primes enter with the minus sign: they are the *gain* elements.

**Reading [A].** The Port Principle's boundary rule (Definition 2.5) says: when a port shows gain, enlarge its boundary until the non-passive source is inside, and apply the constraint to the enlarged port. The enlarged boundary that contains every place is the completed $\xi$ — the program's place-completion $\xi=\prod_vZ_v$ (P0). RH asserts that this fully completed, adelic port is passive. "Arch-domination" (the program's name for the residual) is the circuit statement that the passive element dominates the gain elements.

*Caveat.* The split converges only for $\operatorname{Re}s>\tfrac12$. The RH-relevant strip $0<\operatorname{Re}s\le\tfrac12$ is reached only through the completed object, which is why the reading stays [A].

### 4.5 The three lifts at the archimedean place

**Proposition 4.5 (the functional equation is losslessness) [P].** $\xi(\tfrac12+s)$ is even, so $Z_\xi(-s)=-Z_\xi(s)$, and $Z_\xi$ is real on the real axis. An odd positive-real function has $\operatorname{Re}Z=0$ on the imaginary axis away from its poles: it is a pure reactance (Foster [Fo24]). The functional equation is therefore exactly what makes the zeta port *lossless* rather than merely passive. It is the symmetry restriction of the lift calculus, read at this place.

**Time lift [P, cited].**
- Passivity forces causality (Port Principle Theorem 5.1; Youla–Castriota–Carlin). In this setting it is the Riesz–Herglotz representation of $Z_\xi$, a Kramers–Kronig pair on the critical line.
- Its representing measure is the port's dissipation spectrum, $\pi\sum_\gamma\delta_{\gamma}$. *The dissipation spectrum of the zeta port is the set of zero ordinates.*
- *Certificate K3(c):* $\tfrac1\pi\int_0^{51.5}\operatorname{Re}Z_\xi(0.01+it)\,dt=10.0023$, against the $10$ zeros with $0<\gamma<51.5$.

**Copy lift [P cited; A reading].**
- The Bost–Connes system [BC95] has Hamiltonian $H\varepsilon_n=(\log n)\varepsilon_n$ and partition function $\operatorname{Tr}e^{-\beta H}=\zeta(\beta)$, with its KMS phase transition at $\beta=1$. It is the copy lift's arithmetic instance.
- By unique factorization, the spectral gaps $\log(m/n)$ generate $\bigoplus_p\mathbb Z\log p$, free of infinite rank [P].
- In the language of the Port Principle's resonance-rank law and echo–yield duality (Theorem 6.9, Proposition 6.9e), the arithmetic ledger never echoes exactly and is maximally exploitable. Baker's theorem bounds the relevant linear forms below effectively.
- Any *quantitative* copy-threshold statement for truncated Bost–Connes ledgers is [C] and is left open. The zero geometry of truncated ledgers is §4.6.

### 4.6 The port at finite resolution: balance is free, the deficit is the test

The ledger of §4.5 is infinite. A finite port keeps only the prime modes up to a resolution $X$. Write the crystal $\mathbb N=\bigoplus_p\mathbb N$ multiplicatively, and keep the free energy of the primon gas up to $X$:
$$L_X(s;c)=\sum_{p^k\le X}\frac{c(p)^k}{k\,p^{ks}},\qquad A_X=e^{L_X}.$$
$A_X$ is entire and zero-free: *a finite free gas has no partition-function zeros*. With fugacity $c\equiv1$ it truncates $\zeta$; with $c=\chi$, a Dirichlet character, it truncates $L(s,\chi)$.

**Definition 4.6 (the finite port).** For an amplitude $A$ and the archimedean factor $G$ of a target functional equation, set
$$F(s)=A(s)+G(s)\,A^\#(1-s),\qquad A^\#(w)=\overline{A(\bar w)}.$$
- *$\zeta$-port:* $A=A_X(\cdot;1)$ and $G=\chi_\zeta(s)=\pi^{s-1/2}\Gamma(\tfrac{1-s}2)/\Gamma(\tfrac s2)$.
- *$L(\chi)$-port:* $\chi$ the character mod $5$ with $\chi(2)=i$; $A=A_X(\cdot;\chi)$ and $G=W(\chi)\chi_5(s)$, where $\chi_5(s)=(5/\pi)^{1/2-s}\Gamma(1-\tfrac s2)/\Gamma(\tfrac{1+s}2)$.
- *DH-port:* $A=c_1A_X(\cdot;\chi)+c_2A_X(\cdot;\bar\chi)$ with $c_{1,2}=(1\mp i\kappa)/2$ and $\kappa$ as in N7 §5.5 [DH36], and $G=\chi_5$. The functional equation of the Davenport–Heilbronn function is exactly the identity $W(\chi)=c_2/c_1$ (certified to $10^{-12}$).

Each port satisfies $F(s)=G(s)F^\#(1-s)$ with $|G|=1$ on the critical line. **Balance is built in:** every finite port is lossless (Proposition 4.5) at every resolution. On the line, write $G(\tfrac12+it)=e^{-2i\vartheta(t)}$ and $A=|A|e^{i\alpha}$. Then
$$F(\tfrac12+it)=2e^{-i\vartheta(t)}\,|A|\cos\big(\vartheta(t)+\alpha(t)\big).\tag{4.6}$$
- A zero on the line is a point where the archimedean phase $\vartheta$ plus the amplitude phase $\alpha$ crosses $\tfrac\pi2+\pi\mathbb Z$.
- A zero off the line is a point where the reflection $S=G\,A^\#(1-s)/A(s)$ equals $-1$. There $|S|=1$ although the gas sits at temperature $\sigma$ and its mirror at $1-\sigma$.

**Proposition 4.6 (balance floor) [P].** Suppose $A$ is zero-free on $\operatorname{Re}s\ge\tfrac12$ and has a single-valued logarithm there whose imaginary part is bounded by $B$. Then $F$ has at least $\big(\vartheta(T_2)-\vartheta(T_1)-2B\big)/\pi-1$ zeros on $\tfrac12+i(T_1,T_2]$.

For a finite free gas, $B=B_X=\sum_{p^k\le X}p^{-k/2}/k$. The finite free port therefore turns archimedean phase into zeros on the line one for one, up to a constant fixed by the resolution. No zero is lost from the line.

*Proof.* In (4.6), $\alpha$ is continuous with $|\alpha|\le B$, so $\vartheta+\alpha$ advances by at least $\vartheta(T_2)-\vartheta(T_1)-2B$. Apply the intermediate value theorem to the cosine. $\square$

**Proposition 4.7 (finite free ports are passive above a finite height) [P].** For the $\zeta$-port and $\tfrac12<\sigma\le1$,
$$\log|S(\sigma+it)|\le(\sigma-\tfrac12)\Big(C_X-\log\tfrac t{2\pi}+O(t^{-2})\Big),\qquad C_X=\frac{2\sinh(\tfrac12\log X)}{\tfrac12\log X}\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.$$
So above $T_X=2\pi e^{C_X+1}$ every zero of the $\zeta$-port in the critical strip lies on the line. The same holds for the $L(\chi)$-port, with $\chi_5$ in place of $\chi_\zeta$.

*Proof.*
- First, $\log|A_X(1-s)/A_X(s)|=\sum_{p^k\le X}k^{-1}\,2p^{-k/2}\sinh\big((\sigma-\tfrac12)k\log p\big)\cos(kt\log p)$.
- Next, $\sinh u\le u\sinh U/U$ for $0\le u\le U=\tfrac12\log X$.
- Stirling gives $\partial_\sigma\log|\chi_\zeta(\sigma+it)|=-\log(t/2\pi)+O(t^{-2})$ uniformly for $\tfrac12\le\sigma\le1$, and $\log|\chi_\zeta(\tfrac12+it)|=0$.
- The functional equation covers $0\le\sigma<\tfrac12$. $\square$

Gonek [Go12] proved a statement of this kind, RH up to finitely many zeros, for a related non-analytic family built from finite Euler products. Propositions 4.6–4.7 are the analytic, port-theoretic version, and the matched pair below is what they add. The height $T_X$ is crude: $C_{13}\approx12.9$, so $T_{13}\approx7\times10^6$. The certificate finds no off-line zero of the $\zeta$-port at $X=13$ at any height up to $10^3$.

**Proposition 4.8 (interference drains the line) [P mechanism; certified counts].**
- The DH amplitude $D_X=c_1A_X(\cdot;\chi)+c_2A_X(\cdot;\bar\chi)$ vanishes where $A_X(s;\bar\chi)/A_X(s;\chi)=-c_1/c_2$, a unimodular value.
- At $X=13$ it has $12$ zeros in $\tfrac12<\sigma<1$ below $t=300$.
- $D_X(\sigma+it)$ is almost periodic in $t$, so these zeros recur with positive density.
- In $\sigma\ge\tfrac12+\eta$, $|\chi_5|\to0$ as $t\to\infty$ while $D_X(1-s)$ stays bounded. By Rouché, each such zero carries a zero of the DH-port off the line.
- On the line, the argument principle lowers $\alpha$ by $2\pi$ for each zero of $D_X$ to the right of the line, so each such zero removes two zeros from the line.

**The certified matched pair (K4).** Resolution $X=13$, heights $1\le t\le1000$:

| port | zeros on the line | zeros in $\tfrac12<\sigma<1$ | zeros of the amplitude in $\tfrac12<\sigma<1$, $t\le300$ |
|---|---|---|---|
| $\zeta$ (free gas) | $649=N(1000)$ | $0$ | $0$ |
| $L(\chi)$ (free gas, complex fugacity) | $904$ | $0$ | $0$ |
| DH (interference of two free gases) | $846$ | $29$ | $12$ |

The DH deficit is $904-846=58=2\times29$: every off-line zero of the DH-port took exactly two zeros off the line. The free ports lost none.

**What raising the resolution does (K4(c), K4(d)).**
- The $\zeta$-port's count on the line stays at $N(300)=138$ for $X=5,13,50$; at $X=200$ it is $139$, the extra zero sitting at $t=1.26$.
- Its zeros on the line converge to those of $\zeta$. Below $t=100$ the mean error is $0.25,\ 0.12,\ 0.065,\ 0.026,\ 0.017$ at $X=2,5,13,50,200$, after which it holds near $0.015$, the floor of a sharp cutoff on the line. A single prime ($X=2$) already places all $29$ zeros below $t=100$ on the line.
- At high resolution the $\zeta$-port does gain zeros off the line: $73$ at $X=50$ and $297$ at $X=200$, below $t=300$. They are *added*, not taken from the line, and they sit at the edge $\sigma\to1$ (at $X=50$, $58$ of the $71$ located zeros have $0.9\le\sigma<1$).
- At that edge the mirror amplitude $A_X(1-s)$ is a truncated free gas evaluated at $\beta=1-\sigma\to0$, far past its Hagedorn point: an *overheated mirror*. These zeros are resolution artifacts of the mirror, not gain of the gas.
- DH's off-line zeros at $X=13$ sit in the bulk ($0.5<\sigma<0.9$) and come from its amplitude.

**Proposition 4.9 (where the limit lives) [P, classical, assembled].** Let $E_X(s)=E_1\big((s-1)\log X\big)$, the continuation of $\int_X^\infty u^{-s}\,du/\log u$, i.e. the tail of the Hagedorn pole. Then
$$\mathrm{RH}\iff \exp\big(L_X(s;1)+E_X(s)\big)\to\zeta(s)\ \text{ locally uniformly on }\{\sigma>\tfrac12,\ t>0\}.$$

*Proof.*
- (⇐) The approximants are zero-free, so Hurwitz's theorem applies.
- (⇒) For $\sigma>1$, $\log\zeta-L_X=\int_{X^+}^\infty u^{-s}(\log u)^{-1}d\psi(u)=E_X(s)+\int_{X^+}^\infty u^{-s}(\log u)^{-1}d(\psi(u)-u)$.
- Under RH, $\psi(u)-u=O(\sqrt u\log^2u)$. Integration by parts continues the last integral to $\sigma>\tfrac12$ as $O_s(X^{1/2-\sigma}\log^2X)$, locally uniformly.
- Both sides are analytic on the simply connected, zero-free region and agree for $\sigma>1$. $\square$

Without $E_X$ the limit diverges in $\tfrac12<\sigma<1$ even under RH, since $|E_X|\asymp X^{1-\sigma}/(|s-1|\log X)$. The Hagedorn pole has to be carried along. That is the pole term of the Weil form, the term N7 keeps coupled to the prime translations.

**Reading [A].**
- *Finite systems have no phase transitions.* A finite free gas has no partition-function zeros. Its balanced port still has zeros, and they sit on the balance line with exactly the archimedean count: finite-size precursors of the zeros of $\zeta$ (K4(d)).
- *Zeros are born only in the thermodynamic limit.* Each local factor carries none (N13, the multiplicative-holonomy probe). RH says they are born only on the balance line. Proposition 4.9 places that limit: the pole-compensated free energy must converge past the Hagedorn point down to the balance line, which means no phase transition in $\tfrac12<\operatorname{Re}\beta<1$.
- *DH-sighted at finite resolution.* The prolate approximants of Connes–Consani–Moscovici are real-rooted for DH as well (N7, Observation 5.8), so their passivity carries no arithmetic. The finite ports above separate the matched pair already at $X=13$: the free gases keep the line, and the interference drains it.
- *Third law.* Every finite resolution is certified (Propositions 4.6–4.7), and the limit is not a stage. A finite resolution suffices to see a given height. Pushing $X$ past what that height needs only overheats the mirror at the Hagedorn edge. The infinite-resolution object exists only as the limit of Proposition 4.9. This is the arithmetic form of the statement that an ideal measurement costs unbounded resources [GFH20].
- *The strip as the optimist segment.* In the two gauges of Paper 01e, the pair $(\sigma,1-\sigma)$ holds the temperatures of the gas and of its mirror.
  - Both entries are true numbers (non-negative) exactly on the critical strip, and the functional equation swaps them.
  - The standard form (subtract the minimum) and the zero-sum gauge (subtract the mean) both send the critical line to the origin, the balance point.
  - A zero's displacement is then a true number $2\delta$, and RH says it vanishes.
  - In "zero means below resolution", the N7 lower-bound notes say exactly this: their exponent $\Theta=\limsup\log|E(X)|/\log X$ equals $\sup(\operatorname{Re}\rho-\tfrac12)$, and a polylogarithmic discrepancy registers as $\Theta=0$.

### 4.7 The third-law curve [certified witnesses; readings A]

**The question.** At a given height, what resolution does a finite port need, and how well does it then measure?

**Protocol.**
- Height windows $W=[t_0,t_0+20]$ with $t_0$ from $20$ to $3200$; resolutions $X$ from $2$ to $8147$.
- The $\zeta$-port is run plain, and with the Hagedorn tail carried along ($A=\exp(L_X+E_X)$, Proposition 4.9).
- Off-line zeros in $\tfrac12<\sigma<1$ are counted by the argument principle, split at $\sigma=\tfrac34$.
- Zeros on the line are found from sign changes.
- *Error*: each true zero is matched to the nearest port zero, and the distance is measured in mean spacings $2\pi/\log(t/2\pi)$.

**1. The count on the line is exact.** In every window, the $\zeta$-port's count on the line equals $\zeta$'s at every resolution $X\ge11$. In the highest window ($t_0=3200$) low resolutions are off by one, and from $X=53$ the count is exact. A balance count built from a finite prime sum is, in effect, Selberg's short-sum approximation of $S(t)$ [Se46].

**2. Precision on the line improves with resolution.** At $X=8147$ the error is:

| $t_0$ | $20$ | $50$ | $100$ | $200$ | $400$ | $800$ | $1600$ | $3200$ |
|---|---|---|---|---|---|---|---|---|
| true zeros in $W$ | $5$ | $7$ | $9$ | $11$ | $13$ | $15$ | $18$ | $20$ |
| error, plain port | $0.0049$ | $0.0026$ | $0.0051$ | $0.0032$ | $0.0053$ | $0.0098$ | $0.0083$ | $0.0149$ |
| error, Hagedorn tail carried | $0.0004$ | $0.0017$ | $0.0027$ | $0.0029$ | $0.0056$ | $0.0096$ | $0.0084$ | $0.0148$ |
| first $X$ with an off-line zero (plain) | $41$ | $23$ | $23$ | $41$ | $17$ | $41$ | $31$ | $31$ |

Carrying the Hagedorn tail removes the low-height floor (from $0.0049$ to $0.0004$ at $t_0=20$) and changes nothing at large heights. That is what $|E_X|\asymp\sqrt X/(t\log X)$ predicts.

**3. Full passivity is not bought by resolution.** The first off-line zero of the strip appears at $X$ between $17$ and $53$ at every height from $20$ to $3220$. The curve is flat.

**4. The artifact front.** The port's off-line zeros appear at the edge $\sigma\to1$ and recede toward the line as $X$ grows. With $\sigma_{\min}$ the smallest real part among them:

| $\sigma_{\min}-\tfrac12$ | $X=53$ | $293$ | $1543$ | $8147$ |
|---|---|---|---|---|
| $t_0=30$ | $0.413$ | $0.342$ | $0.258$ | $0.238$ |
| $t_0=410$ | $0.401$ | $0.289$ | $0.239$ | $0.197$ |
| $t_0=3210$ | $0.496$ | $0.330$ | $0.206$ | $0.184$ |

- Across all $52$ cells where the port has an off-line zero, $(\sigma_{\min}-\tfrac12)\log X$ lies between $1.34$ and $2.14$: about $2.0$ at $t_0=30$ and about $1.6$ at $t_0=3210$. The artifact-free band around the line has width $\approx c/\log X$ with $c\approx1.5$–$2$, drifting slightly down with height.
- With the Hagedorn tail carried, the functional equation gives exactly $S_X=\exp\big(R_X(s)-R_X(1-s)\big)$, where $R_X$ is the error of the finite free energy. Under RH these zeros are fluctuations of the mirror tail $R_X(1-s)$. Under refinement they wander: a bulk zero at one resolution is gone at the next.

**5. The matched pair.**
- *DH windows without off-line zeros* ($[20,40]$, $[50,70]$) behave like $\zeta$.
- *Windows containing DH's off-line zeros:* the passive ports ($X\le5$) over-count the line by exactly two per off-line zero:

| window | DH's off-line zeros in it | passive count error ($X=3,5$) |
|---|---|---|
| $[80,100]$ | $0.8085+85.70i$ | $+2$ |
| $[110,130]$ | $0.6508+114.16i$ | $+2$ |
| $[160,180]$ | $0.5744+166.48i$, $0.7243+176.70i$ | $+4$ |

- *Once active (from $X\approx7$–$17$), the port's off-line zeros sit at DH's.* At $0.7243+176.70i$ the port zero is $1.7\times10^{-3}$ away at $X=8147$. At $0.8085+85.70i$ it stays within $0.09$ at every $X$ from $13$ to $8147$.
- DH's port is not expected to converge in the strip: DH has zeros with $\operatorname{Re}s>1$, so its tail is never small. What is measured is tracking.
- The zero nearest the line ($0.5744+166.48i$, $\delta=0.074$) is acquired at $X=17$. For $293\le X\le6173$ it falls inside the artifact-free band, and the port folds it back onto the line. The count on the line then shows it again as $+2$.

**Reading [A].**
- *The instrument.* The passive count is a finite measurement. Its mismatch with the true count is exactly twice the number of off-line zeros in the window, including those below the port's off-line resolution. It reads $\zeta$ correctly at every tested height and reads DH wrong by exactly its off-line pairs.
- *Features and artifacts.* An off-line zero of the target is a feature: it persists under refinement (DH). An artifact wanders and recedes ($\zeta$).
- *Complementarity.* Resolution trades certification off the line for precision on it.
  - The error on the line falls with $X$.
  - The artifact-free band shrinks like $\approx c/\log X$ with $c\approx1.5$–$2$.
  - Full passivity is lost at $X\approx20$–$50$ at every height.
  - The ideal measurement $X\to\infty$ would be perfect on the line and would certify nothing off it.
  - This is the third law in this setting: the limit is unreachable, and off the line, approaching it does not help. Off-line certainty has to come from the archimedean damping and the arithmetic, not from resolution.
- *The scale.* Matched to the height ($X=t^\theta$), the band width $c/\log X$ becomes $\asymp1/\log t$. That is the scale on which Selberg's and Levinson's methods work [Se46, Le74].

**Status.** The curve is a measurement protocol on finite windows, and it is consistent with RH at every tested height.
- What it isolates is the off-line certification band. Resolution alone narrows that band like $c/\log X$.
- Certification off the line is carried by the archimedean damping and the arithmetic. §4.9 states that target in Castelnuovo–Severi form.

Witnesses:
- `empirical/passive_ports/p53_third_law_curve.py` (log `p53_third_law_run.log`)
- `p53_artifact_front.py` (log `p53_artifact_front_run.log`)
- `p53_persistence_probe.py` (log `p53_persistence_run.log`)

### 4.8 The instrument

§4.7 found that the passive count reads $\zeta$ correctly and reads DH wrong by exactly two per off-line zero. This section proves the identity behind that and names its error term.

**Setting.**
- $f$ is $\zeta$, a Dirichlet $L$-function, or the Davenport–Heilbronn function, with completion $\Lambda=\gamma f$ satisfying $\Lambda(s)=\Lambda(1-s)$ and $\Lambda(\bar s)=\overline{\Lambda(s)}$.
- $\vartheta_f(t)=\arg\gamma(\tfrac12+it)$, taken continuous; for $\zeta$ this is the Riemann–Siegel theta function up to a constant.
- $S_f(t)=\pi^{-1}\arg f(\tfrac12+it)$, by continuous variation along the horizontal from $\sigma=+\infty$.
- $A$ is analytic and zero-free on $\operatorname{Re}s\ge\tfrac12$, tends to a nonzero constant as $\sigma\to\infty$, and has $S_A(t)=\pi^{-1}\arg A(\tfrac12+it)$ defined the same way.
- For a window $W=[T_1,T_2]$ whose endpoints are not ordinates of zeros of $f$:
  - the *balance count* is $N_{\rm bal}(A;W)=\Delta_W\vartheta_f/\pi+\Delta_W S_A$;
  - $N_{\rm line}(f;W)$ counts the zeros of $f$ on the line in $W$;
  - $N_{\rm off}(f;W)$ counts those with $\operatorname{Re}s>\tfrac12$;
  - both counts include multiplicity.

**Theorem 4.10 (the instrument identity) [P].**
$$N_{\rm bal}(A;W)-N_{\rm line}(f;W)=2\,N_{\rm off}(f;W)+\Delta_W\big(S_A-S_f\big).$$

*Proof.*
- Apply the argument principle to $\Lambda$ on the rectangle $[1-a,a]\times[T_1,T_2]$ with $a$ large.
- The two symmetries make the boundary variation twice its variation along the right half, from $\tfrac12+iT_1$ out to $a+iT_1$, up to $a+iT_2$, and back to $\tfrac12+iT_2$.
- Along that path, $\gamma$ is zero- and pole-free and contributes $\Delta_W\vartheta_f$. The factor $f$ contributes $\pi\Delta_WS_f$: the vertical edge contributes nothing as $a\to\infty$, which is how $S_f$ is defined.
- So the rectangle holds $\Delta_W\vartheta_f/\pi+\Delta_WS_f$ zeros. They are the zeros on the line plus both members $\rho$, $1-\bar\rho$ of every off-line pair, i.e. $N_{\rm line}+2N_{\rm off}$.
- Subtract this from $N_{\rm bal}$. $\square$

**Corollary 4.11 (the readout) [P].** Write $R_W=N_{\rm bal}(A;W)-N_{\rm line}(f;W)$ and $E_W=\Delta_W(S_A-S_f)$. If $|E_W|<1$, then $N_{\rm off}(f;W)$ is the nearest integer to $R_W/2$.

So a zero-free amplitude, one count of sign changes, and two phases form an off-line zero counter. Its only error is the variation, across the window, of the gap between the model phase and the true phase. The sign-change count of the port itself equals $N_{\rm bal}$ up to rounding whenever $\vartheta_f+\pi S_A$ is monotone on $W$ (Proposition 4.6), which is the version measured in §4.7.

**Proposition 4.12 (the error is Selberg's remainder) [P, cited].** For the finite free gas $A=A_X$,
$$S_A=S_X,\qquad S_X(t)=-\frac1\pi\sum_{p^k\le X}\frac{\sin(kt\log p)}{k\,p^{k/2}},$$
which is Selberg's short prime-sum approximation of $S(t)$ [Se46]. So $E_W=\Delta_W(S_X-S)$.
- Pointwise, $|E_W|\le2\max_W|S|+2B_X/\pi$, and $S(t)=O(\log t)$ unconditionally. The target is pointwise control below $1$.
- In mean, Selberg showed that $S-S_X$ has bounded moments on $[T,2T]$ when $X$ is a suitable small power of $T$. The instrument therefore misreads on a set of bounded relative density.
- A Gaussian model of the primes (variance $\tfrac1{2\pi^2}\sum_{X<p\le T}1/p$) predicts that a fixed $X$ degrades slowly with height, while $X=T^\theta$ keeps the misread rate bounded.

This is Turing's method [Tu53] with Selberg's prime sum in place of Turing's integral bound on $S$. It is rigorous wherever $|E_W|<1$ is certified; certifying that through $S$ at the endpoints recovers Backlund's count. What the instrument adds is structural: the port does the bookkeeping, and Selberg's remainder is the single quantity left to control.

**The certificate (K6).** `empirical/passive_ports/p53_instrument_cert.py`, log `p53_instrument_run.log`.
- $S$ is computed by tracking $\arg f$ from $\sigma=4$, with no zero counting: an Euler–Maclaurin $\zeta$ agreeing with mpmath to $10^{-11}$–$10^{-14}$, and mpmath Hurwitz sums for DH.
- Zeros on the line come from Riemann–Siegel sign changes on a $0.004$ grid.

| target, windows | identity residual $\max\lvert R_W-E_W-2N_{\rm off}\rvert$ | readout |
|---|---|---|
| $\zeta$, $250$ windows of width $20$ on $[100,5100]$, $4598$ zeros | $2\times10^{-11}$ | $N_{\rm off}=0$ everywhere |
| DH, $X=5$, windows $[20,40]$, $[50,70]$, $[80,100]$, $[110,130]$, $[160,180]$ | $<10^{-4}$, with $2N_{\rm off}=0,0,2,2,4$ | $0,0,1,1,2$, all correct |

Misreads over the $250$ $\zeta$ windows, by resolution rule:

| rule | $X=13$ | $X=1000$ | $X=t^{1/2}$ | $X=t$ |
|---|---|---|---|---|
| rms $E_W$ | $0.419$ | $0.314$ | $0.402$ | $0.284$ |
| max $\lvert E_W\rvert$ | $1.098$ | $1.047$ | $0.995$ | $0.991$ |
| misreads | $2$ | $1$ | $0$ | $0$ |

A height-matched resolution reads every window correctly, but with a margin of only $0.01$ at worst. DH's window $[160,180]$ reads correctly with $E_W=-0.989$, also at the margin. The instrument works, and its error is the size Selberg's remainder predicts. It has no slack to spare, which is the third law once more: a finite measurement has a finite error rate.

**Remark 4.13 (why $\tfrac12$: two 2's).** In response to the question why $\tfrac12$ is special.
- *The prime 2 is the arithmetic zoom gauge [P].*
  - $\mathbb N\setminus2\mathbb N=2(\mathbb N-\tfrac12)$: removing the prime $2$ returns one ray, the crystal zoomed by $2$ and shifted by $\tfrac12$.
  - For $p\ge3$ the sieve leaves $\varphi(p)=p-1$ rays.
  - In Dirichlet series, $(1-2^{-s})\zeta(s)=2^{-s}\zeta(s,\tfrac12)$.
  - $2$ is also the only prime whose pole-cancelling Euler factor leaves unimodular coefficients: $(1-2^{1-s})\zeta(s)=\eta(s)=\sum(-1)^{n-1}n^{-s}$. For $p\ge3$ the coefficients are $1$ and $1-p$.
  - On the crystal $\mathbb Z$, the Brillouin zone has exactly two points fixed by $k\mapsto-k$, namely $0$ and $\tfrac12$. The $k=\tfrac12$ mode is $(-1)^n$, of period $2$.
  - Jacobi's inversion fixes $\theta_3$, whose Mellin transform is $\xi$, and swaps the $\tfrac12$-twist $\theta_4$ with the $\tfrac12$-shift $\theta_2$ (verified to $10^{-32}$).
- *The critical line's $\tfrac12$ is a different $\tfrac12$ [P].*
  - It is the fixed line of the unitary point inversion $Jf(x)=x^{-1}f(1/x)$ on $L^2(\mathbb R_+,dx)$, which acts on Mellin transforms by $s\mapsto1-s$. The $\sqrt x$ in $\theta(1/x)=\sqrt x\,\theta(x)$ is this half-density.
  - The same $\tfrac12$ makes dilations unitary: $U_\lambda f(x)=\lambda^{1/2}f(\lambda x)$ sends $x^{-s}$ to $\lambda^{1/2-s}x^{-s}$, unimodular iff $\operatorname{Re}s=\tfrac12$.
  - The Noether charge of dilations is the self-adjoint $-i(x\partial_x+\tfrac12)$.
  - For a rank-$d$ lattice the line sits at $d/2$ (Epstein). So $\tfrac12$ is the dimension $1$ of the ray over the quadratic $2$ of the norm.
- *Reading [A].*
  - The prime $2$ is the gauge; the quadratic $2$ is the energy: the Port Principle's power $\|a\|^2-\|b\|^2$, and the Hodge-index square behind $|\alpha|=\sqrt q$ over $\mathbb F_q$.
  - They meet in the distortion-free zoom by $2$, $f\mapsto\sqrt2\,f(2x)$, which is lossless exactly on $\operatorname{Re}s=\tfrac12$. Its $\sqrt2$ is the program's Helmert first-prime normalizer.
  - The line itself comes from the quadratic $2$: it sits at $\tfrac12$ for every Dirichlet $L$-function and for curves over $\mathbb F_q$, where the prime $2$ plays no special role.
- *Rays and characters [P + A].*
  - Removing the primes of $n$ leaves $\varphi(n)$ rays, for instance $\{1,5\}$ mod $6$. By orthogonality their Fourier duals are the $\varphi(n)$ Dirichlet characters. Mod $6$ these are $\zeta$ and $L(s,\chi_3)$, the program's $\mathbb Z/6$ collapse.
  - Unitary compositions of rays (characters, multiplicative and unimodular) keep the balance: their finite ports are passive (§4.6). DH, with ray weights $0,1,\kappa,-\kappa,-1$ mod $5$, is a non-unitary composition and breaks it.
  - The complement closes the loop: $\big(\sum\mu(n)n^{-s}\big)\zeta(s)=1$, so the squarefree (fermionic, $\mu=(-1)^F$ [Sp90]) crystal times the full crystal is the unit.
  - RH $\iff\sum_{n\le x}\mu(n)=O(x^{1/2+\varepsilon})$: the crystal's fermion parity walks like a random walk. This is square-root cancellation, the quadratic $2$ again.

### 4.9 Castelnuovo–Severi over $\mathbb Q$: one clock, two clocks

**The $\mathbb F_q$ template [P, classical].** Let $C$ be a curve of genus $g$ over $\mathbb F_q$. On $C\times C$, take the fibre classes $H_1,H_2$, the diagonal $\Delta$ and the Frobenius graph $\Gamma_n$. Their intersection numbers are:
- $\Delta^2=2-2g$ and $\Gamma_n^2=q^n(2-2g)$;
- $\Delta\cdot\Gamma_n=N_n$, the number of points of $C$ over $\mathbb F_{q^n}$;
- $\Delta\cdot H_i=\Gamma_n\cdot H_1=H_1\cdot H_2=1$, $\Gamma_n\cdot H_2=q^n$, and $H_i^2=0$.

The Hodge index theorem gives the Gram matrix of $\{\Delta,\Gamma_n,H_1,H_2\}$ exactly one positive eigenvalue. Remove the hyperbolic plane $\langle H_1,H_2\rangle$ and normalize $\Gamma_n$ by $q^{-n/2}$. What is left is
$$\begin{pmatrix}-2g&e_n\\e_n&-2g\end{pmatrix},\qquad e_n=\frac{N_n-q^n-1}{q^{n/2}},$$
and negative semidefiniteness is the Castelnuovo–Severi inequality $|e_n|\le2g$. Holding for every $n$, it gives $|\alpha|=\sqrt q$ for every Frobenius eigenvalue.

*Certificate.* For $E:y^2=x^3+x+1$ over $\mathbb F_{101}$, exact rational inertia gives $(1,3)$ for $n=1,\dots,8$. A control with $N_1$ pushed beyond the Hasse bound gives $(2,2)$. Floating-point eigenvalues misreport the signature at $n=5,8$, where the entries reach $q^8\approx10^{16}$; exact arithmetic is required.

**The dictionary [P].** Take the packet $f(x)=e^x\mathbf 1_{[0,\log2]}$, its zooms $\tau_tf$, and the Weil Gram matrix $\begin{pmatrix}q_0&K(t)\\K(t)&q_0\end{pmatrix}$ of the N7 lower-bound notes. The Weil form is minus the intersection form on the primitive part.

| $\mathbb F_q$ | $\mathbb Q$ |
|---|---|
| diagonal $\Delta$ | packet $f$ |
| Frobenius graph $\Gamma_n$ (degree $q^n$) | zoom $\tau_{\log X}f$ (scale $X$) |
| hyperbolic plane $\langle H_1,H_2\rangle$ | pole terms at $s=0,1$ (the $A\sqrt X$ and $A/\sqrt X$ of $K$) |
| $2g$ | $q_0=Q(f)=0.29984744\ldots$ |
| $e_n$ | $K(\log X)=A\sqrt X-P(X)-D(X)$ |
| $\lvert e_n\rvert\le2g$ | $\lvert K(t)\rvert\le q_0$ |

The diagonal entry $q_0$ is purely archimedean, because the packet sits below the first prime. It is positive unconditionally: the support of $g=f*f^*$ is $[-\log2,\log2]$, inside the range of Yoshida and Connes–Consani.

**Theorem 4.14 (Castelnuovo–Severi over $\mathbb Q$) [P].**
$$\mathrm{RH}\iff|K(t)|\le q_0\ \text{for all }t\iff K(t)\ge-C(1+t)^m\ \text{for some }C,m.$$
One side suffices.

*Proof.*
- (⇒) Under RH, $K(t)=\sum_\rho b_\rho e^{i\gamma t}$ with $b_\rho\ge0$ and $\sum_\rho b_\rho=q_0$.
- (⇐) This is the Landau argument of the N7 Divergence Ledger, §2. $\square$

**The one-clock ladder: the prime $2$ as zoom gauge [P + certificate].**
- Zoom by $2^m$. The Weil Gram of $\{\tau_{m\log2}f\}_{m<N}$ is the Toeplitz matrix $T_N=[c_{j-k}]$, with $c_0=q_0$ and $c_m=K(m\log2)$. For a modulated packet $f_\omega=e^{i\omega x}f$ it is the Hermitian analogue.
- RH implies $T_N\succeq0$ for every $N$. Equivalently, every reflection coefficient of the Levinson–Szegő recursion has $|\kappa_k|\le1$: each rung is a passive 2-port.
- This is necessary. It is sufficient up to an exceptional coincidence, because one clock samples $K$ only on $\log2\cdot\mathbb Z$.

| ladder (rungs $m\le22$) | $\omega=0$ | $\omega=14.1347$ | $\omega=85.6993$ (DH's off-line height) |
|---|---|---|---|
| $\zeta$, from primes to $2^{23}$ | passive; $\max\lvert\kappa\rvert=0.58$ | passive; $0.78$ | passive; $0.76$ |
| DH, from its zeros ($106$ ordinates below $180$ plus four off-line quadruples) | passive; $0.72$ | — | **leaves the disk at rung $5$**; $\lambda_{\min}(T_{23})/c_0=-47$ |

- The $\zeta$ values from primes agree with a $250$-zero computation to $0.02$, the truncation error of the zero side.
- The untuned packet does not see DH's off-line zero within $22$ rungs: $G(\delta+iH)\approx10^{-3}$ suppresses it. The packet tuned to its height catches it at rung $5$.
- The prediction error $E_k$ of the $\zeta$ ladder decreases: $E_{22}/c_0=0.37$, $0.09$, $0.07$ for the three modulations. Under RH the spectral measure is pure point (the zeros mod $2\pi/\log2$), so Szegő's condition fails and $E_k\to0$. The ladder is passive at every rung and approaches zero prediction error without reaching it.

In the clock $w=2^{-(s-1/2)}$ the Euler factor at $2$ is rational, $(1-2^{-1/2}w)^{-1}$, with its pole at $|w|=\sqrt2$. Every other prime is an irrational rotation of this clock, since $\log p/\log2\notin\mathbb Q$ by unique factorization. Over $\mathbb F_q$ every local factor is rational in the one clock $T=q^{-s}$. That common clock is what makes a curve's zeta function a polynomial, so that one surface carries all Frobenius graphs and Hodge index applies to all of them at once.

**Theorem 4.15 (two clocks suffice) [P].** RH holds if and only if
$$c_{m,n}=K(m\log2+n\log3)$$
is a positive definite function on $\mathbb Z^2$.

*Proof.*
- (⇒) The restriction of a positive definite function to a subgroup is positive definite.
- (⇐) By unique factorization, $\log3/\log2$ is irrational, so $\mathbb Z\log2+\mathbb Z\log3$ is dense in $\mathbb R$.
- $K$ is continuous, and a limit of positive semidefinite matrices is positive semidefinite. So $K$ is positive definite on $\mathbb R$, and $|K|\le K(0)=q_0$.
- Theorem 4.14 then gives RH. $\square$

One clock gives a necessary condition and two incommensurable clocks give an equivalence. The minimal clock set is $\{2,3\}$, the primes whose removal first produces "compositions of rays" (Remark 4.13). The entries $c_{m,n}$ with $|m\log2+n\log3|<\log2$ use the Weil pairing at short separation, where the archimedean term with overlapping supports enters. Formula (8) of the lower-bound note does not cover them.

**Reading [A]: what closing requires.**
- Over $\mathbb F_q$ the inequality holds for every $n$ because one surface carries every Frobenius graph, and Riemann–Roch on that surface proves Hodge index for all of them at once.
- Over $\mathbb Q$ the analogue must carry every zoom at once. Theorem 4.15 reduces this to the two clocks $2$ and $3$.
- The closing statement in this form: *one arithmetic structure, built from the Euler product, that makes every finite section of the two-clock form positive semidefinite.* That is the analogue of Riemann–Roch on $C\times C$.
- Window-by-window certification has been pushed past the first primes: Zhu [Zh26] certifies Weil positivity unconditionally for supports in $[-0.8,0.8]$. His unconditional variational upper bounds are tiny at selected larger windows, and his decay $\lambda_{\min}(L)\le e^{-Le^L}$ is conditional on RH. Shrinking margins are not a logical obstruction: positivity of every finite section suffices. What window certification cannot supply is the universal quantifier.
- *The extension inequality and the realization (N7 two-clock note, 2026-10-11).*
  - Let $M$ be a finite section and $b$ the correlations of a new zoom with it. The enlarged section is positive semidefinite iff $b\in\operatorname{range}M$ and $q_0-b^*M^+b\ge0$, which permits zero margin.
  - The mixed two-clock section on the zooms $1,2,3,6,4,9,12,18,36$, computed from primes with the short-separation formula, has all nine Schur pivots positive. The smallest is $0.408\,q_0$, and the smallest eigenvalue is $0.0885\,q_0$.
  - Once every finite section is positive semidefinite, the Gram (Kolmogorov) construction gives one Hilbert space with commuting unitary zooms carrying them all. The completion needs no separate invention.

### 4.10 The arithmetic Riemann–Roch

Over $\mathbb F_q$, Riemann–Roch enters Weil's theorem by two routes:
- **Hodge index on $C\times C$** (Weil, Grothendieck). This is the two-clock surface of §4.9, whose open input is the extension inequality.
- **Bombieri–Stepanov on the curve alone** [Bo73]. It needs no surface:
  - Riemann–Roch on $C$ and the Frobenius build an auxiliary function vanishing to order $p^\mu$ at every rational point. Counting its zeros against its degree gives the one-sided bound $N_n\le q^n+(2g+1)q^{n/2}+1$.
  - The rationality of $Z(C,T)$ turns this one-sided bound into $|\alpha|=\sqrt q$.

Both halves of the second route can be placed over $\mathbb Q$.

**(a) Riemann–Roch on the curve $\overline{\operatorname{Spec}\mathbb Z}$ [P, classical; certificate K8].**
- Give the Arakelov degree $d\in\mathbb R$ the lattice $\mathbb Z$ with metric $|n|e^{-d}$, and set $h^0(d)=\log\sum_{n\in\mathbb Z}e^{-\pi n^2e^{-2d}}$ [vdGS00].
- Then $h^0(d)\ge0$, because the zero section is always present.
- Jacobi's inversion (Poisson summation) is exactly Riemann–Roch: $h^0(d)-h^0(-d)=d$.
- The completed zeta function is the Mellin transform of the section count: $\pi^{-s/2}\Gamma(\tfrac s2)\zeta(s)=\int_0^\infty\tfrac12(\theta(x)-1)x^{s/2}\,dx/x$, with $\theta(x)=e^{h^0(-\frac12\log x)}$.
- So the functional equation, the balance of Proposition 4.5, is Riemann–Roch for the arithmetic curve.
- *Certificate.* Direct theta sums give $h^0(d)-h^0(-d)-d$ below $3\times10^{-39}$ for $d\in[-3,4]$. Riemann's continuation, built from $x\ge1$ sections only, matches $\Lambda(s)$ to $10^{-44}$ at $\tfrac12+14.1347i$, $\tfrac12+10i$ and $0.3+7i$.

**(b) The Landau half [P].** The rationality step has an exact $\mathbb Q$-form: the one-sided Laplace argument of the N7 Divergence Ledger §2, with the pole terms $A\sqrt X+A/\sqrt X$ in place of $q^n+1$. Writing $P(X)$ for the smoothed prime sum and $A\sqrt X$ for its main term:
$$P(X)\le A\sqrt X+C(\log X)^m\ \text{ for all large }X\implies\mathrm{RH}.$$
This holds with the upper bound alone.

**(c) The Stepanov half: the arithmetic Stepanov lemma (the target).** The remaining statement is the one-sided bound in (b):
$$\boxed{\ \text{the smoothed prime count over }[X/2,2X]\text{ is at most its main term plus }O\big(\sqrt X(\log X)^m\big)\ }$$
This is an upper bound on primes at square-root precision.

**What an auxiliary object over $\mathbb Z$ has to supply (certificate K8(iv)).**
- *Multiplicity one already exists.* Chebyshev's integer $\binom{2X}{X}$ is divisible by every prime in $(X,2X]$; it "vanishes" there to order one. Its size bounds the count: $\vartheta(2X)-\vartheta(X)\le\log\binom{2X}{X}\sim2X\log2$.
- *Its excess is linear.* The overshoot is $(2\log2-1)X\approx0.386X$: $3.9\times10^5$ at $X=10^6$, against the needed scale $\sqrt X\log^2X=1.9\times10^5$.
- *Selberg's sieve is the quadratic version.* Its $\Lambda^2$ form is a positive quadratic form built from the Euler product, and it loses the parity factor $2$ on the main term (N7 barrier note §4).
- *Square-root precision needs multiplicity.* Stepanov's multiplicity $p^\mu\sim\sqrt q$ comes from the char-$p$ Frobenius, under which $p$-th powers have identically vanishing derivative, and it holds at every rational point at once. That is what turns an $O(\text{count})$ error into $O(\sqrt{\text{count}})$.
- *Characteristic $0$ has no such Frobenius.* Characteristic one does. On the min-plus semifield, the standard-form gauge of Paper 01e, $x\mapsto\lambda x$ is an automorphism for every $\lambda>0$, a continuous Frobenius. Connes–Consani's scaling site carries Riemann–Roch on each periodic orbit $C_p$ of length $\log p$ [CC16].

**The target, stated once.** The arithmetic Riemann–Roch has three parts:
1. Riemann–Roch on the curve, which is the functional equation (built).
2. The Landau half (built).
3. An auxiliary object over $\mathbb Z$ that vanishes at every prime in the window with multiplicity of order $\sqrt X$ and has degree $X+O(\sqrt X)$.

Item 3 is the arithmetic Frobenius. The two-clock surface of §4.9 is the Hodge-index form of the same requirement. Characteristic one, where the program's massaction gauge and the scaling site's continuous Frobenius live, is where that multiplicity can be sought.

### 4.11 The arithmetic Frobenius: what it must do, measured

**The literature (checked October 2026, arXiv and Zenodo).**
- *The Frobenius already exists in characteristic one.* On the arithmetic site [CC14], $x\mapsto x^\lambda$ is an automorphism of the max-plus semifield for every $\lambda>0$. Its periodic orbits are the primes, with length $\log p$, and its Lefschetz trace is the prime side of the explicit formula. Riemann–Roch holds on each orbit $C_p$ [CC16].
- *Recent work builds the absolute curve.* Connes–Consani's 2026 preprints construct the Jacobian of $\overline{\operatorname{Spec}\mathbb Z}$ [CC26a], an $\mathbb F_1$-curve over $\operatorname{Spec}\mathbb Z$ whose orbit at $p$ is a Tate curve with $q=p^{-1}$ under discrete Frobenius symmetries [CC26b], and an absolute Frobenius over $\mathbb F_{1^2}$ with Adams operations [CC26c].
- *No Stepanov multiplicity yet.* None of these states an intersection pairing, a Hodge index or a positivity theorem. No preprint found, on arXiv or Zenodo, gives a Stepanov-type multiplicity over $\mathbb Z$. The obstruction usually cited is that $\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z=\operatorname{Spec}\mathbb Z$ is one-dimensional [Mi15].
- *Two refinements from the peer audit [As26b].*
  - The 2026 Jacobian [CC26a] admits rank-one groups such as $\mathbb Z[1/p]$ beyond classical metrized lattices. Its ordinary Gaussian section sum diverges, since the elements $p^{-r}$ all have bounded norm, so the section count of §4.10(a) needs a regularization there. The simplest exhaustion $p^{-r}\mathbb Z$ leaves after subtraction only the linear degree term, without the sign the section count needs.
  - The signed base $\mathbb F_{1^2}$ of [CC26c] carries a canonical sign and an odd-integer Frobenius. "Characteristic one has no $-1$" describes the idempotent semifield only, not the newer signed geometry.

**The Möbius–Chebyshev object over $\mathbb Z$ [P, classical identity; corrected after [As26a]].** Write $T(y)=\log\lfloor y\rfloor!$ and $\nu_K(y)=\sum_{k\le K}\mu(k)\lfloor y/k\rfloor$, and set
$$N_K(x)=\prod_{k\le K}\Big(\frac{\lfloor x/k\rfloor!}{\lfloor x/2k\rfloor!}\Big)^{\mu(k)},\qquad \log N_K(x)=\sum_{k\le K}\mu(k)\big[T(x/k)-T(x/2k)\big].$$
- Its size is known from Stirling alone: the archimedean Riemann–Roch, with no primes needed.
- *It is rational, and in general not an integer.* For example $N_5(18)=\tfrac{2\cdot11\cdot13\cdot17}{3}=\tfrac{4862}{3}$ [As26a].
- *Valuations.* Legendre's formula gives $v_p(N_K)=\sum_{r\ge1}a_K(x/p^r)$ with $a_K(y)=\nu_K(y)-\nu_K(y/2)$. So $a_K(x/n)$ is a *contribution indexed by the prime power $n$*, not a valuation at $n$.
  - Since $\nu_K(y)=1$ for $1\le y<K+1$ (the Möbius identity), the contribution is exactly $1$ for $n\in(x/2,x]$ and $0$ for $n\in(x/(K+1),x/2]$.
  - Below $x/(K+1)$ contributions of both signs occur, so the spurious part contains poles as well as zeros.
- Hence, as an exact signed identity,
$$\log N_K(x)=\big[\psi(x)-\psi(x/2)\big]+\mathrm{spur}(K),\qquad \mathrm{spur}(K)=\sum_{n\le x/(K+1)}\Lambda(n)\,a_K(x/n).$$
- At full complexity $K=x$ the object is $N_x(x)=e^{\psi(x)-\psi(x/2)}=\operatorname{lcm}(1,\dots,x)/\operatorname{lcm}(1,\dots,\lfloor x/2\rfloor)$.
- *The spurious term, exactly* [As26a, eq. (7)]. With $m_K=\sum_{k\le K}\mu(k)/k$, $R_K(y)=\sum_{k\le K}\mu(k)\{y/k\}$ and $z=x/(K+1)$:
$$\mathrm{spur}(K)=\tfrac x2\,m_K\sum_{n\le z}\frac{\Lambda(n)}n-\sum_{n\le z}\Lambda(n)\big[R_K(x/n)-R_K(x/2n)\big].$$
  The first term is the fitted law $\tfrac12xm_K\log(x/K)$. Elementarily the second is only $O(K\psi(z))=O(x)$, so the fit is a measurement on the tested range, not an asymptotic.

**Certificate K9** (`p53_arithmetic_frobenius.py`, log `p53_arithmetic_frobenius_run.log`; the integrality and decomposition checks are the peer's `check_factorial_auxiliary.py`, all $2\le x\le80$, $1\le K\le x$).
- The identity at $K=x$ reproduces $\psi(x)-\psi(x/2)$ to $1\times10^{-10}$, $4\times10^{-9}$ and $7\times10^{-8}$ at $x=10^5$, $10^6$, $4\times10^6$, against values of order $5\times10^4$ to $2\times10^6$.
- $\mathrm{spur}(K)$ follows $\tfrac12xm_K\log(x/K)$ across $K=10^2$ to $10^5$ at $x=4\times10^6$. For example, $7.19\times10^4$ is measured against $7.3\times10^4$ predicted at $K=10^3$.
- *Finite-range envelopes* (numerical evidence, not an asymptotic rate): $\max\sqrt k\,|m_k|=0.451$ over $10^3\le k\le4\times10^6$, and $\max|M(y)|/\sqrt y=0.472$ over $10^3\le y\le4\times10^6$.

| auxiliary object | complexity $K$ | error | complexity for error $\sqrt x$ |
|---|---|---|---|
| Chebyshev, $\binom{2X}{X}$ | $2$ | $\approx0.39X$ | not reached |
| Möbius–Chebyshev $N_K$ (measured, $x\le4\times10^6$) | $K$ | $\approx x/\sqrt K$, up to logs | $K\approx x$: no compression |
| Stepanov over $\mathbb F_q$ | $\dim\approx\sqrt q$ | $\approx q/K$ | $K\approx\sqrt q$ |

**Stepanov efficiency needs other coefficients [P, As26a §6].** No bound $m(x)=O(x^{-\alpha}(\log x)^B)$ holds with $\alpha>\tfrac12$. Partial summation gives $1/\zeta(s)=(s-1)\int_1^\infty m(x)x^{-s}\,dx$, and such a bound would continue $1/\zeta$ holomorphically across the zeros on the critical line.
- So square-root balance of the parity pair is exactly what produces the rate $x/\sqrt K$ in the table, and no improvement of $m_K$ can reach the Stepanov rate.
- The parity pair: in the Optimist-plane coordinates of Paper 01e, $\sum\mu$ is the pair $(E(x),O(x))$ of squarefree counts with an even or odd number of prime factors, and its standard form is $|M(x)|$. RH holds iff $|M(x)|=O(x^{1/2+\varepsilon})$ (classical).
- An auxiliary at Stepanov efficiency therefore needs *different coefficients*. The peer's integral majorants [As26b] are the first instance, and §4.12 determines the optimal coefficients exactly.
- Over $\mathbb F_q$ the balance is automatic, because $1/Z(C,T)=(1-T)(1-qT)/P(T)$ is a ratio of polynomials: a finite Möbius. §4.12(e) identifies the mechanism behind that identity.

### 4.12 The optimal auxiliary and the parity identity

Throughout, $J(x)=\{\lfloor x/n\rfloor:2\le n\le x\}$, a set of about $2\sqrt x$ scales, symmetric under the hyperbola involution $n\leftrightarrow x/n$ with fixed point $\sqrt x$. For real coefficients $c_1,\dots,c_K$ put
$$G_c(j)=\sum_{k\le K}c_k\big(\lfloor j/k\rfloor-\lfloor j/2k\rfloor\big),\qquad H_x(c)=\sum_{k\le K}c_kF(\lfloor x/k\rfloor),\quad F(m)=\log m!-\log\lfloor m/2\rfloor!.$$

**(a) Integral majorants [P; As26b, refined].**
- *The peer's construction.* If $G_c(1)\ge1$ and $G_c(j)\ge0$ for $2\le j\le x/2$, then the factorial ratio $\prod_k(\lfloor x/k\rfloor!/\lfloor x/2k\rfloor!)^{Qc_k}$ is an integer divisible by $\big(\operatorname{lcm}(1..x)/\operatorname{lcm}(1..\lfloor x/2\rfloor)\big)^Q$. Its normalized height is $H_x(c)$.
  - The peer optimizes $c$ by linear programming and certifies integrality exactly.
  - At $K=\lceil\sqrt x\rceil$ the integral optima have height $573.19$, $2209.39$ and $5494.47$ at $x=10^3$, $4\cdot10^3$, $10^4$.
  - If $H_x(c)\le x/2+C\sqrt x\log^mx$ held uniformly, RH would follow (Landau, as in (b) of §4.10).
- *Refinement 1: the inequalities on $J(x)$ suffice.* Since $\lfloor y/k\rfloor=\lfloor\lfloor y\rfloor/k\rfloor$, Legendre's formula reads $G_c$ only at the points $\lfloor x/p^r\rfloor\in J(x)$. So about $2\sqrt x$ inequalities replace $x/2$.
- *Refinement 2: integrality is not needed for the prime bound.* By $\Lambda\ge0$ and $\log\lfloor y\rfloor!=\sum_n\Lambda(n)\lfloor y/n\rfloor$,
$$\psi(x)-\psi(x/2)=\sum_n\Lambda(n)\,[\lfloor x/n\rfloor=1]\le\sum_n\Lambda(n)\,G_c(\lfloor x/n\rfloor)=H_x(c)$$
  for every real $c$ satisfying the inequalities on $J(x)$.
- *Effect.* On $J(x)$ the optimal heights at the peer's three points drop to $572.50$, $2184.01$ and $5398.14$ (certificate K10a).

**(b) The exact optimum is the Legendre sieve [P for the duality; measured threshold].** Let $H^*(x,K)$ be the optimal value. By LP duality,
$$H^*(x,K)=\max\Big\{z_1:\ z\ge0\text{ on }J,\ \sum_{j\in J}z_j\big(\lfloor j/k\rfloor-\lfloor j/2k\rfloor\big)=F(\lfloor x/k\rfloor)\ (k\le K)\Big\}.$$
The dual variables are fake prime masses that reproduce the first $K$ factorial identities. The true masses $z_j=\sum_{\lfloor x/n\rfloor=j}\Lambda(n)$ are feasible, so $H^*\ge\psi(x)-\psi(x/2)$.

Measured (K10a, K10b):
- *There is a sharp exactness threshold* $K_{\rm LP}(x)$. For $K\ge K_{\rm LP}$, $H^*(x,K)=\psi(x)-\psi(x/2)$ to $10^{-10}$, with $K_{\rm LP}/\sqrt x=2.75$, $2.5$, $2.75$ at $x=10^3$, $10^4$, $10^5$ and $K_{\rm LP}\le4\sqrt x$ at $x=10^6$.
- *At the threshold the optimum is adapted to the primes.* $G^*$ vanishes on every class $\{n:\lfloor x/n\rfloor=j\}$ that contains a prime power, and it is positive on some classes that contain none ($8$ of $21$, $38$ of $99$, $113$ of $355$).
- *A prime-free exact identity needs far more complexity.* $G_c=[j=1]$ on all of $J$ is not solvable for any tested $K\le4\sqrt x$: the rank stays below $|J|$ and the least-squares residual stays between $0.73$ and $0.98$. It is solvable at $K=x/2$, by the full Möbius vector.
- *Below the threshold the excess is large.* At $K=\sqrt x$, $H^*-(\psi(x)-\psi(x/2))=383$, $2314$, $14842$ at $x=10^4$, $10^5$, $10^6$, roughly $x^{0.8}$.

*Reading.*
- The exact log-factorials $F(m)$, $m<\sqrt x$, contain $\log m$ and hence $\Lambda=\mu*\log$ below $\sqrt x$.
- The primes below $\sqrt x$ determine those in the window, by Eratosthenes–Legendre.
- So at $K\ge K_{\rm LP}$ the exact auxiliary *is* the window count. The uniform height bound for it is equivalent to the dyadic prime bound itself, with no slack in either direction.
- The factorial family is therefore complete: it is exact as soon as it can be. This is Chebyshev's method [DE80] carried to its end.

**Theorem 4.16 (forced parity) [P].** Let $0\le\theta<1$ and let $c\in\mathbb Z^K$ satisfy the inequalities on $J(x)$ with spillover $H_x(c)-(\psi(x)-\psi(x/2))\le x^\theta$. Then for all large $x$,
$$c_k=\mu(k)\qquad\text{for every }k\le\min\big(x^{(1-\theta)/2}/\sqrt2,\ x^{5/17-\varepsilon}\big).$$
*Proof.*
- The spillover is a sum of nonnegative terms, $\big(G_c(1)-1\big)\big(\psi(x)-\psi(x/2)\big)+\sum_{j\ge2}z_jG_c(j)$, with $z_j$ the true masses.
- For $j\le x^{5/17-\varepsilon}$ the class of $j$ is an interval of length $x/(j(j+1))\ge(x/j)^{7/12+\varepsilon}$. Huxley's prime number theorem in short intervals [Hu72] gives $z_j\ge x/(2j^2)$ there.
- $G_c$ is integer-valued. So $G_c(j)\ge1$ for some $2\le j<x^{(1-\theta)/2}/\sqrt2$ would make the spillover exceed $x^\theta$, and $G_c(1)\ge2$ would make it at least $\psi(x)-\psi(x/2)>x^\theta$.
- Hence $G_c(j)=[j=1]$ on that range. This system is triangular with unit diagonal, and the two-window Möbius identity $\sum_{k\le j}\mu(k)(\lfloor j/k\rfloor-\lfloor j/2k\rfloor)=[j=1]$ solves it. So $c=\mu$ there. ∎

At $\theta=\tfrac12$ the forced range is $[1,x^{1/4}/\sqrt2]$. The parity function is not an input of the construction: an economical auxiliary must reproduce the unit $G=[j=1]$ on every heavy scale, and the unique solution of that requirement is $\mu$. This is the complement unitary requirement of Remark 4.13, made exact.

Measured: the optima agree with $\mu$ up to $k=20$, $31$, $71$ at $x=10^4$, $10^5$, $10^6$ ($K=\sqrt x$), about $2x^{1/4}$.

**(c) The a priori polytope: Stepanov's lemma as a linear program [P for the inequality; measured values].** Replace each exact log-factorial by Stirling's main term with an explicit allowance:
$$S(y)=\tfrac y2\log y+\tfrac y2(\log2-1),\qquad |F(\lfloor y\rfloor)-S(y)|\le b(y)=\tfrac12\log y+1\quad(y\ge2).$$
The allowance follows from Stirling's formula with remainder; the computed deviation is $\le\tfrac12\log y+\tfrac12\log2+O(1/y)$, and it is checked on $2\le y\le10^7$. Then for every $c$ satisfying the inequalities on $J(x)$,
$$\psi(x)-\psi(x/2)\le H_x(c)\le E(c):=\tfrac x2\big[C(1)(\log x+\log2-1)+C'(1)\big]+\sum_k|c_k|\,b(x/k),\qquad C(s)=\sum_kc_kk^{-s}.$$
- *No prime, no exact factorial and no zero enters $E$.* The data are the floor matrix on $J(x)$ and Stirling's main term. The inequality itself uses only $\Lambda\ge0$ and $\log=1*\Lambda$, both from the Euler product.
- *Columns collapse.* On $J(x)$ all $k$ with the same $\lfloor x/k\rfloor$ give the same column, so all $k\le x/2$ reduce to about $2\sqrt x$ groups. The minimum $E^*(x)$ over unlimited complexity is a linear program of size $\approx2\sqrt x$ (K10d).
- *Dual reading.* $E^*(x)$ is the largest window mass of a nonnegative fake prime measure on $J$ whose log-factorials stay within $b$ of Stirling at every scale. Without the positivity, Möbius inversion could carry the slack to order $\sum_{k\le x}|\mu(k)|b(x/k)\asymp x$ [A]. With it, the slack is measured at $\sqrt x$ scale.

Certificate K10d:

| $x$ | $E^*(x)-x/2$ | $\div\sqrt x$ | $\div\sqrt x\log x$ | $\psi(x)-\psi(x/2)-x/2$ |
|---:|---:|---:|---:|---:|
| $10^3$ | $88.3$ | $2.79$ | $0.404$ | $-5.0$ |
| $10^4$ | $386.6$ | $3.87$ | $0.420$ | $15.4$ |
| $10^5$ | $1423.6$ | $4.50$ | $0.391$ | $65.6$ |
| $10^6$ | $5434.6$ | $5.43$ | $0.393$ | $-526.7$ |
| $3\cdot10^6$ | $10590.7$ | $6.12$ | $0.410$ | $-134.9$ |
| $10^7$ | $20741.8$ | $6.56$ | $0.407$ | $-2431.7$ |

The $x=10^7$ row is from the dual program (`p53_apriori_dual.py`, $|J|=6322$, $2.0\times10^7$ nonzeros). At every smaller $x$ the dual and the primal agree to all printed digits.

*Structure of the optimum: a mollified Möbius head and a positivity tail.*
- *Head.* $c=\mu$ on $[1,\approx3$–$4x^{1/4}]$, as Theorem 4.16 forces (K10c, $K=6$–$8\sqrt x$ at $x=10^4,10^5$). Then $c/\mu\approx0.6$ on average up to $\sqrt x$, $\approx0.15$ on $(\sqrt x,2\sqrt x)$, and $\approx0$ beyond. This is the shape of a Barban–Vehov weight with cut-offs near $x^{1/4}$ and $x^{1/2}$ [BV68, Gr78].
- *Tail.* A positivity repair sits on the column groups $k>\sqrt x$, i.e. on the log-factorials of numbers below $\sqrt x$. It carries a growing share of the $\ell^1$ mass: $0.48$, $0.56$, $0.69$ at $x=10^4$, $10^5$, $10^6$ (K10f).
- *The tail is essential.* The Barban–Vehov vector alone violates positivity: its floor sums are negative on $34$–$56\%$ of $J(x)$, down to $-26$ at $x=10^6$ (K10f).
- *Size.* The total is $\ell^1=(0.089$–$0.092)\sqrt x\log x$ for $10^4\le x\le3\cdot10^6$.

**Theorem 4.17 [P].** If $E^*(x)\le x/2+C\sqrt x(\log x)^m$ for all large $x$, then RH holds.

*Proof.* $\psi(x)-\psi(x/2)\le E^*(x)$; sum over dyadic windows, then apply the one-sided Landau argument of §4.10(b). ∎

*Conversely [P, under RH].* The full Möbius vector is feasible, with $H_x=\psi(x)-\psi(x/2)$. Its a priori penalty is a total variation of the Mertens function along the scale groups, $\sum_m|M(x/m)-M(x/(m+1))|\log m$. With only $M(y)=O(y^{1/2+\varepsilon})$ this gives $E^*(x)-x/2\ll x^{2/3+\varepsilon}$. Closing the gap from $\tfrac23$ to $\tfrac12$ is a short-interval parity statement, and the optimizer already achieves it numerically.

**(d) The matched pair.** The inequality $\psi(x)-\psi(x/2)\le E(c)$ uses exactly two facts: $\Lambda\ge0$, and that $\log\lfloor y\rfloor!$ is the $\Lambda$-weighted floor sum, i.e. $\log=1*\Lambda$. Both are the Euler product.
- Davenport–Heilbronn has neither: its $-L'/L$ coefficients change sign, and its partial sums are not log-factorials.
- So the polytope is one-sided, closed (an LP optimum, not a margin), and built on the Euler product. These are the three properties §4.9–4.10 asked of a closure.
- Formally, zeros are invisible to its data [A]: $\log\lfloor y\rfloor!=\sum_m\psi(y/m)$, and each zero's term $y^\rho\zeta(\rho)/\rho$ in that sum vanishes because $\zeta(\rho)=0$. That is why Stirling alone can serve as the data.

**(e) The parity identity, exact forms (certificate K10e).**
- *The prime-2 cone [P; homotopy type and Betti numbers: Bj11].* Let $\Delta_n$ be the simplicial complex of squarefree $k\le n$, with faces their prime sets.
  - Faces containing $2$ form the cone over $\Delta^{\rm odd}_{n/2}$, so $\Delta_n\simeq\Delta^{\rm odd}_n/\Delta^{\rm odd}_{n/2}$.
  - Every proper face of an odd squarefree $k\in(n/2,n]$ has the form $k/p\le n/3$. Hence
$$\Delta_n\simeq\bigvee_{k\ \text{odd squarefree},\ n/2<k\le n}S^{\omega(k)-1},\qquad M(n)=-\tilde\chi(\Delta_n)=\sum_{k\ \text{odd squarefree}\in(n/2,n]}\mu(k).$$
  - In the filtration $n\mapsto\Delta_n$, each class is born at $k$ and dies at $2k$: every persistence bar has log-length $\log2$. The prime $2$ is the zoom gauge, now topologically.
  - RH holds iff the spheres of one $2$-zoom (about $2n/\pi^2$ of them [Bj11]) cancel by dimension parity to within the square root of their number, up to $n^\varepsilon$.
  - Checked: reduced Betti numbers over $\mathrm{GF}(10^6+3)$ for $n\le60$, $72$, $90$; the window identity for $M$ for all $n\le10^6$.
- *Over $\mathbb F_q[T]$ the same cone at $T$ gives a constant.* The window sum $\sum_{\deg f=n,\ T\nmid f}\mu(f)=1-q$ for every $n\ge1$ (checked for $q=3$, $n\le7$; $q=5$, $n\le5$). This is $1/Z=1-qT$.
  - *Mechanism.* By Stickelberger's theorem ($q$ odd), $\mu(f)=(-1)^{\deg f}\operatorname{sgn}(\mathrm{Frob}\mid\text{roots of }f)$.
  - The window sum is therefore a sign-twisted point count of the configuration space of $n$ points on the line. The Grothendieck–Lefschetz formula evaluates it on the sign-isotypic cohomology of $\mathrm{Conf}_n(\mathbb C)$, which is zero for $n\ge2$ (cf. [CEF14]).
  - *This is the operation that makes the balance structural:* a Lefschetz trace on a small cohomology replaces the alternating count of the $\approx q^n$ spheres. Over $\mathbb Z$ the cone produces the $\approx2n/\pi^2$ spheres, and their compression is the construction this target names.
- *Squares, the second 2 [P, classical identities].* $\lambda*1=\mathbf 1_\square$, so
$$\sum_{d\le x}\lambda(d)\Big\lfloor\frac xd\Big\rfloor=\lfloor\sqrt x\rfloor\quad\text{exactly},\qquad v_p\Big(\prod_{d\le x}\lfloor x/d\rfloor!^{\lambda(d)}\Big)=\sum_{r\ge1}\big\lfloor\sqrt{x/p^r}\big\rfloor.$$
  - So the Liouville factorial is an *integer* with multiplicity $\lfloor\sqrt{x/p}\rfloor$ at $p$: a square-root multiplicity built from the parity function alone.
  - Its generating function is $\sum\lambda(n)n^{-s}=\zeta(2s)/\zeta(s)$. At the parity point the pole of $\zeta$ at $1$ cancels, and the pole of the squares at $s=\tfrac12$ is exposed.
  - **RH holds iff the squares set the abscissa**, i.e. $\zeta(2s)/\zeta(s)$ is holomorphic on $\operatorname{Re}s>\tfrac12$. Over a curve, $\sum\lambda(D)u^{\deg D}=Z(C,u^2)/Z(C,u)$ has radius $q^{-1/2}$ iff $|\alpha_i|\le\sqrt q$.
  - The critical $\tfrac12$ is the point where $2s=1$: the two 2's of Remark 4.13 in one line.

**The target, stated once.** The arithmetic Stepanov lemma is now a finite-dimensional statement with no primes in it:
- *Statement.* For every large $x$, find $c$ with $G_c\ge[j=1]$ on $J(x)$ and $E(c)\le x/2+C\sqrt x(\log x)^m$.
- *Equivalently,* a mollified Möbius head plus a positivity tail on the small log-factorials, such that:
  - the floor sums stay nonnegative on the $\approx2\sqrt x$ points of $J(x)$;
  - the two Stirling moments $C(1)$ and $C'(1)-1$ vanish to precision $x^{-1/2}$;
  - the total $\ell^1$ mass is $O(\sqrt x\log^mx)$.
- *Status.* The linear program supplies such a $c$ at every tested scale, at the level $\approx0.4\sqrt x\log x$. Theorem 4.17 turns a uniform construction into RH.
- *The Stepanov count.* Over $\mathbb F_q$, Stepanov proves the analogous existence by a dimension count. Here the count is favourable: the optimizer leaves about $40\%$ of the $J$-constraints slack. What remains is a uniform $\ell^1$ control of the solution.

### 4.13 The uniform construction

A feasible point of the polytope exists for every $x$ and has an explicit height. It is the Möbius function itself, read on the hyperbola.

**The hyperbola cells.** For $m\ge2$ let $I_m=(x/(m+1),x/m]$, the set of $k$ with $\lfloor x/k\rfloor=m$. On $J(x)$ every $k\in I_m$ gives the same column, since $\lfloor\lfloor x/n\rfloor/k\rfloor=\lfloor m/n\rfloor$.
- For $m\ge\sqrt x$ the cell is a single integer.
- For $m<\sqrt x$ it is an interval of length about $x/m^2$.
- The cell coefficient of the Möbius vector is
$$c_m=\sum_{k\in I_m}\mu(k)=M(x/m)-M(x/(m+1)).$$
- Its a priori cost uses Stirling's bracket at the cell's ends, $y_m^-=x/\max I_m$ and $y_m^+=x/\min I_m$, with width $w_m=(S+b)(y_m^-)-(S-b)(y_m^+)=O(\log x)$:
$$E(\mu)=\sum_m\big[c_m^+(S+b)(y_m^-)-c_m^-(S-b)(y_m^+)\big].$$

**Theorem 4.18 (the Möbius construction) [P].** For every $x\ge2$:
1. *Feasibility.* $G_\mu(j)=[j=1]$ for every $j\le x/2$, by the two-window Möbius identity. So the Möbius vector lies in the polytope with zero slack.
2. *Height.* $E(\mu)=\big(\psi(x)-\psi(x/2)\big)+\theta_x V_w(x)$ with $0\le\theta_x\le1$, where
$$V_w(x)=\sum_m|c_m|\,w_m .$$
3. *Sandwich.*
$$\psi(x)-\psi(x/2)\ \le\ E^*(x)\ \le\ E(\mu)\ \le\ \psi(x)-\psi(x/2)+V_w(x).$$

*Proof.*
- Part 1 is the identity $\sum_{k\le j}\mu(k)(\lfloor j/k\rfloor-\lfloor j/2k\rfloor)=[j=1]$.
- For part 2, the cell values satisfy $F(m)\in[(S-b)(y_m^+),(S+b)(y_m^-)]$. So each term of $E(\mu)$ exceeds $c_mF(m)$ by an amount in $[0,|c_m|w_m]$.
- And $\sum_mc_mF(m)=\sum_{k\le x/2}\mu(k)F(\lfloor x/k\rfloor)=\psi(x)-\psi(x/2)$, by Möbius inversion of $\log\lfloor y\rfloor!=\sum_n\Lambda(n)\lfloor y/n\rfloor$.
- Part 3 combines part 2 with the optimality of $E^*$ and the bound $H\ge\psi(x)-\psi(x/2)$. ∎

**Corollary 4.19.** Write $V(x)=\sum_m|M(x/m)-M(x/(m+1))|$ for the Mertens variation along the hyperbola.
- (i) *[Theorem 4.17]* If $E^*(x)\le x/2+C\sqrt x\log^mx$ for all large $x$, then RH holds.
- (ii) *[P]* If RH holds and $V(x)\ll\sqrt x\log^mx$, then $E^*(x)\le x/2+O(\sqrt x\log^{m+2}x)$.
- (iii) *[P]* Under RH alone, $E^*(x)-x/2\ll x^{2/3+\varepsilon}$. The cells with $m\le x^{1/3}$ are bounded by $M(y)\ll y^{1/2+\varepsilon}$, and the rest trivially by their length.

So the polytope bound is sandwiched between RH and RH plus a square-root law for $\mu$ on the hyperbola cells. Whether RH alone already gives $E^*(x)-x/2\ll x^{1/2+\varepsilon}$ is open. It would follow from any feasible construction whose $\ell^1$ penalty avoids the short cells.

**Certificate K11** (`p53_mobius_construction.py`: segmented Möbius sieve to $x/2$, segmented prime sieve on $(x/2,x]$; only $\approx2\sqrt x$ Mertens values enter):

| $x$ | $E(\mu)-x/2$ | $\div\sqrt x\log x$ | $\psi(x)-\psi(x/2)-x/2$ | $V_w$ | $\theta_x$ | $V\div\sqrt x\log x$ |
|---:|---:|---:|---:|---:|---:|---:|
| $10^3$ | $142.9$ | $0.654$ | $-5.0$ | $295.3$ | $0.501$ | $0.339$ |
| $10^4$ | $681.7$ | $0.740$ | $15.4$ | $1330.9$ | $0.501$ | $0.350$ |
| $10^5$ | $2445.7$ | $0.672$ | $65.6$ | $4795.4$ | $0.496$ | $0.286$ |
| $10^6$ | $9520.7$ | $0.689$ | $-526.7$ | $19570.5$ | $0.513$ | $0.285$ |
| $10^7$ | $39307.4$ | $0.771$ | $-2431.7$ | $80691.8$ | $0.517$ | $0.320$ |
| $10^8$ | $150941.7$ | $0.819$ | $-2964.5$ | $305131.2$ | $0.504$ | $0.317$ |
| $10^9$ | $561542.4$ | $0.857$ | $-5393.9$ | $1120636.7$ | $0.506$ | $0.305$ |

*Readings.*
- *Möbius is square-root balanced on every cell, as far as measured.* A random-sign model on the squarefree numbers gives $\mathbb E|c_m|\approx0.62\sqrt{x}/m$, hence $V(x)\approx0.31\sqrt x\log x+O(\sqrt x)$. The measured $V(x)/(\sqrt x\log x)$ stays at $0.29$–$0.35$ over six decades. In Paper 01e's terms, the parity pair is balanced cell by cell.
- *The bracket sits in the middle.* $\theta_x$ stays within $0.50\pm0.02$, so $E(\mu)$ is the window plus half the weighted variation.
- *Positivity slack buys a constant factor.* The optimum $E^*$ beats the exact Möbius vector by a factor of $0.53$–$0.62$ in $E-x/2$ at every common scale ($10^3\le x\le10^7$). Its $\ell^1$ is about $3.4$ times smaller ($0.09$ against $0.31$, in units of $\sqrt x\log x$). It achieves this by trading exactness ($G=[j=1]$) for positivity ($G\ge[j=1]$).

*Where the content sits.*
- Every feasible $c$ satisfies $E(c)\ge H_x(c)\ge\psi(x)-\psi(x/2)$, by the product formula. So a uniform height bound is a prime bound, and it can be proved only by an estimate that is itself RH-strength.
- For the Möbius construction that estimate has two parts:
  - the window, i.e. RH itself;
  - square-root cancellation of $\mu$ on the $\approx\sqrt x$ hyperbola cells $(x/(m+1),x/m]$.
- Over $\mathbb F_q[T]$ both are free: $1/Z=1-qT$ makes every cell sum vanish beyond degree one.
- The next targets are therefore:
  - (a) a construction under RH alone, which would make the polytope an exact RH-equivalent (done in §4.14, on average over $x$);
  - (b) a structural source for the cell-by-cell parity balance, the arithmetic counterpart of the Lefschetz compression of §4.12(e).

### 4.14 The construction under RH alone

Landau's argument does not need the polytope bound at every $x$. A bound on average over $x$ is enough, and on average RH alone controls the Möbius cells.

**Theorem 4.20 (the polytope is an exact RH-equivalent) [P].** The following are equivalent:
1. the Riemann Hypothesis;
2. for every $\varepsilon>0$,
$$\sum_{X<x\le2X}\Big(E^*(x)-\frac x2\Big)\ \ll_\varepsilon\ X^{3/2+\varepsilon}.$$

Item 2 may be taken one-sided (an upper bound). Its left side involves only the optimal values of the prime-free, zero-free linear programs of §4.12(c), and $\sum_{X<x\le2X}x/2=\tfrac34X^2+O(X)$.

*Proof of 2 ⇒ 1.* Write $W(x)=\psi(x)-\psi(\lfloor x/2\rfloor)$, so $W(x)\le E^*(x)$ (§4.12(a)).
- *Telescoping.* For integers $x$, $\psi(x)=\sum_{k\ge0}W(\lfloor x/2^k\rfloor)$ and $\tfrac12\sum_{k\ge0}\lfloor x/2^k\rfloor=x-\tfrac12s_2(x)$, where $s_2$ is the binary digit sum.
- *Summing over $x\in(X,2X]$.* Each $y=\lfloor x/2^k\rfloor$ in the interior of $(X/2^k,2X/2^k]$ occurs exactly $2^k$ times, and the boundary costs $O(X)$ per level $k$. Applying 2 at the scale $X/2^k$ gives
$$\sum_{X<x\le2X}(\psi(x)-x)\ \ll\ \sum_k2^k(X/2^k)^{3/2+\varepsilon}+X\log X\ \ll\ X^{3/2+\varepsilon}.$$
- *Integrated form.* Hence $\Psi(X)=\int_1^X(\psi(u)-u)\,du\le CX^{3/2+\varepsilon}$ for all $X$, because $\Psi(X)=\sum_{x<X}(\psi(x)-x-\tfrac12)+O(X)$.
- *Landau.* For $\operatorname{Re}s>2$,
$$\int_1^\infty\Psi(X)X^{-s-1}dX=\frac1s\Big(-\frac{\zeta'(s-1)}{(s-1)\zeta(s-1)}-\frac1{s-2}\Big).$$
  The pole at $s=2$ cancels, and the other poles sit at $s=\rho+1$. The transform of $CX^{3/2+\varepsilon}-\Psi(X)$ has a nonnegative integrand, so by Landau's theorem its abscissa is a real singularity.
- There is none on $(3/2+\varepsilon,\infty)$, because $\zeta$ has no zeros in $(0,1)$. So $\operatorname{Re}\rho\le\tfrac12+\varepsilon$ for every zero, for every $\varepsilon$. ∎

*Proof of 1 ⇒ 2.* By Theorem 4.18, $E^*(x)-x/2\le\big(W(x)-x/2\big)+V_w(x)$ and $V_w(x)\le(\log x+2)V(x)$.
- *The window.* By von Koch, $W(x)-x/2\ll\sqrt x\log^2x$.
- *The cells.* $V(x)\le\sqrt x+\sum_{m\le\sqrt{2X}+1}|\Delta_m(x)|$ with $\Delta_m(x)=M(x/m)-M(x/(m+1))$, a Möbius sum over an interval of relative length $1/m$ at height $x/(m+1)$.
- *Averaging one cell.* For each $m$, Cauchy–Schwarz over $x$ gives $\sum_x|\Delta_m(x)|\le X^{1/2}\big(\sum_x\Delta_m(x)^2\big)^{1/2}$.
  - Replacing the sum over integers by an integral costs $O(X^2/m^3+X)$.
  - Substituting $y=x/(m+1)$ turns the integral into $(m+1)\int_Y^{2Y}|M(y(1+\tfrac1m))-M(y)|^2dy$ with $Y=X/(m+1)$.
  - By Lemma 4.21 this is $\ll X^{2+\varepsilon}/m^2$, so $\sum_x|\Delta_m(x)|\ll X^{3/2+\varepsilon}/m$.
- *All cells.* Summing over $m\le\sqrt{2X}+1$ gives $\sum_{X<x\le2X}V(x)\ll X^{3/2+\varepsilon}\log X$. (The few top cells with $m\ge\sqrt{X/2}$ have length $O(1)$ and are bounded trivially.) ∎

**Lemma 4.21 (RH ⇒ square-root cancellation of $\mu$ in short intervals, in mean square) [P].** Assume RH. For $Y\ge2$ and $1\le T\le Y/2$,
$$\int_Y^{2Y}\big|M\big(y(1+\tfrac1T)\big)-M(y)\big|^2\,dy\ \ll_\varepsilon\ \frac{Y^{2+\varepsilon}}{T}.$$
*Proof.*
- *Setup.* Let $a_n=\mu(n)$ for $Y/2<n\le4Y$ and $0$ otherwise. Let $A(s)=\sum a_nn^{-s}$ and $S(y)=\sum_{y<n\le y(1+1/T)}a_n$. For $y\in[Y,2Y]$, $S(y)$ is the Möbius sum in question.
- *Plancherel.* The Mellin transform of $S$ is $A(s)(e^{\delta s}-1)/s$ with $e^\delta=1+1/T$. Plancherel on $\operatorname{Re}s=\sigma=\tfrac12+\varepsilon$ gives
$$\int_0^\infty|S(y)|^2y^{-2\sigma-1}dy=\frac1{2\pi}\int_{\mathbb R}|A(\sigma+it)|^2\Big|\frac{e^{\delta(\sigma+it)}-1}{\sigma+it}\Big|^2dt,$$
  and the kernel is $\ll\min(T^{-2},t^{-2})$.
- *Low frequencies, $|t|\le Y/2$.* On RH, Perron's formula shifted to $\operatorname{Re}(s+w)=\tfrac12+\varepsilon/2$, together with $1/\zeta(\tfrac12+\varepsilon/2+iv)\ll(|v|+2)^{\varepsilon/2}$ [Ti86, §14.2], gives
$$\sum_{n\le N}\mu(n)n^{-s}=\frac1{\zeta(s)}+O\big(N^{1/2-\sigma+2\varepsilon}\big)\qquad(|t|\le N).$$
  So $A=P_{4Y}-P_{Y/2}$ loses the $1/\zeta$ terms, and $|A(\sigma+it)|\ll Y^{\varepsilon}$ for $|t|\le Y/2$.
- *High frequencies, $|t|>Y/2$.* The mean value theorem for Dirichlet polynomials [MV74] gives $\int_U^{2U}|A|^2\ll U+Y$.
- *Assembly.* The right side is $\ll Y^{2\varepsilon}/T$. Restricting the left side to $[Y,2Y]$, where $y^{-2\sigma-1}\ge(2Y)^{-2-2\varepsilon}$, gives the claim. ∎

*What the averaging buys.*
- At each fixed $x$, RH controls a Möbius sum over a cell only up to $\min(|I_m|,(x/m)^{1/2+\varepsilon})$. That is where $x^{2/3}$ comes from in Corollary 4.19(iii).
- As $x$ varies, the cells sweep through all positions. Lemma 4.21, the mean value theorem for $1/\zeta$ on $\operatorname{Re}s>\tfrac12$, then gives square-root cancellation on average.
- Landau's theorem accepts the average because $\int\psi$ carries the same zeros as $\psi$.
- The pointwise statement, $E^*(x)-x/2\ll x^{1/2+\varepsilon}$ for every $x$, follows from RH together with pointwise square-root control of the hyperbola cells (Corollary 4.19(ii)). Under RH alone it remains open; Corollary 4.19(iii) gives $x^{2/3+\varepsilon}$.

**Certificate K12** (`p53_rh_construction.py`, log `p53_rh_construction_run.log`).
- *Lemma 4.21's square-root law.* $\frac1Y\sum_{Y<y\le2Y}|M(y(1+\frac1T))-M(y)|^2\div(Y/T)$ is $0.61$–$0.88$ at $Y=10^5$ and $0.85$–$1.02$ at $Y=10^6$, for $5\le T\le3000$. The random model gives $6/\pi^2=0.61$. At $T=2$ it is $0.09$–$0.13$: long intervals cancel better than random.
- *The averaged construction.* For $400$ random $x\in(X,2X]$, the mean of $(E(\mu)-x/2)/(\sqrt x\log x)$ is $0.664$, $0.703$, $0.754$, $0.785$ at $X=10^4,10^5,10^6,10^7$.
  - The pointwise spread is narrow: the extremes are $0.57$–$0.85$.
  - The mean cell variation $V/(\sqrt x\log x)$ is $0.304$–$0.314$, with maxima $0.35$–$0.39$.
  - The mean window term $(\psi(x)-\psi(x/2)-x/2)/(\sqrt x\log x)$ is below $0.005$ in absolute value.

*Reading.*
- The polytope of §4.12(c) is now an exact, prime-free and zero-free criterion: RH holds iff its optimal values average to $x/2$ up to $x^{1/2+\varepsilon}$.
- The construction behind the forward direction is the Möbius function on the hyperbola cells. Its feasibility is the complement unitary requirement $G=[j=1]$; its cost is the parity balance of $\mu$ cell by cell.
- RH supplies that balance on average, through the mean square of $1/\zeta$ on $\operatorname{Re}s>\tfrac12$. Conversely, the polytope bound returns RH through Landau's positivity.
- The criterion is one-sided and closed: an LP optimum, not a margin.

## 5. Certificates

`empirical/passive_ports/p53_bridge_cert.py` (K1–K3); `empirical/passive_ports/p53_finite_port_probe.py` with log `p53_finite_port_run.log` (K4, §4.6); `p53_cs_fq_exact.py` and `p53_dyadic_ladder.py` with their logs (K7, §4.9); `p53_arithmetic_rr.py` (K8, §4.10); `p53_arithmetic_frobenius.py` (K9, §4.11); `p53_chebyshev_lp.py`, `p53_lp_threshold.py`, `p53_apriori_lp.py`, `p53_apriori_scale.py`, `p53_apriori_full.py`, `p53_apriori_dual.py`, `p53_apriori_structure.py`, `p53_bv_auxiliary.py` and `p53_parity_identity.py` with their logs (K10, §4.12). `p53_mobius_construction.py` with its log (K11, §4.13). `p53_rh_construction.py` with its log (K12, §4.14). Falsifiers for K1–K3 were pre-registered before the first run. K4 is a double-precision witness, not an interval certificate: zeros on the line by sign changes on a $10^{-3}$ grid, off-line counts by the argument principle with adaptive phase steps below $0.4$, located zeros by Newton refinement.

| Check | Statement | Result |
|---|---|---|
| K1 [exact] | Cayley; Lemma 3.2's congruence and defect form; $Z=Q'/Q$ in the $s$-plane | PASS (symbolic) |
| K2 [exact] | Foster matched pair, **positive-definite** Pick for the finite network | **FAIL, retained**: only PSD holds (rank $=6$) |
| K2′ [exact, post-diagnosis] | GOOD: $P=FF^\ast$ exactly, rank $6=2\times$tanks. BAD (pair at $z_0=2+\tfrac i2$): right-half-plane poles $\tfrac12\pm2i$ and a negative diagonal entry $-17.18$ | PASS |
| K3(a) [50-digit] | $\operatorname{Re}Z_\xi>0$ on 804 grid points, $\sigma\in\{0.01,0.1,0.5,2\}$, $t\le100$ | PASS (min $4.6\times10^{-4}$) |
| K3(b) [50-digit] | 12×12 Pick matrix near the first six zeros is PD | PASS (min eig. $1.0\times10^{-9}$) |
| K3(c) [witness] | dissipation spectrum counts zeros | PASS ($10.0023$ vs $10$) |
| K3(d) [witness] | Foster tanks at the actual zero ordinates reproduce $Z_\xi(0.5+10i)$ | PASS: rel. err. $0.155$ (50 tanks), $0.054$ (300), $1.1\times10^{-4}$ (300 + density tail) |
| K3(e) [control] | planted off-line quartet $z_0=17+0.5i$ replacing $\gamma_1,\gamma_2$ is flagged | PASS: $\min\operatorname{Re}Z_{\rm bad}=-8.87$; augmented Pick min eig. $-10.86$ |
| K4(a) [numeric] | the DH functional equation is $W(\chi)=c_2/c_1$ | PASS: $\lvert W-c_2/c_1\rvert<10^{-12}$ |
| K4(b) [witness, matched pair] | finite ports at $X=13$, $t\le1000$: zeros on the line; off-line zeros by the argument principle | $\zeta$: $649$, $0$. $L(\chi)$: $904$, $0$. DH: $846$, $29$; deficit $58=2\times29$ |
| K4(c) [witness] | resolution sweep $X=5,13,50,200$, $t\le300$: line counts and where the extra zeros sit | $\zeta$ line count $138,138,138,139$; extra zeros at the $\sigma\to1$ edge |
| K4(d) [witness] | $\zeta$-port zeros on the line against $\gamma_n$, $10\le t\le100$ | count $29=29$ at every $X$ from $2$ to $5000$; mean error $0.25\to0.017$ by $X=200$, then a floor near $0.015$ (the uncarried Hagedorn tail, §4.7) |
| K5(a) [witness] | third-law curve, $\zeta$-port, 8 windows to $t=3220$, $X\le8147$ | count exact for $X\ge11$ ($X\ge53$ at $t_0=3200$); error at $X=8147$: $0.0004$–$0.015$ spacings; first off-line zero at $X=17$–$53$, flat in height |
| K5(b) [witness] | artifact front $\sigma_{\min}-\tfrac12$, 5 heights × 11 resolutions | $(\sigma_{\min}-\tfrac12)\log X\in[1.34,2.14]$; about $2.0$ at $t_0=30$, about $1.6$ at $t_0=3210$ |
| K9 [numeric] | Möbius–Chebyshev auxiliary $N_K(x)$, $x\le4\times10^6$ | identity exact (relative error $<10^{-13}$); $\mathrm{spur}(K)\approx\tfrac12xm_K\log(x/K)$ on the tested range; finite-range envelopes $\max\sqrt k\lvert m_k\rvert=0.451$, $\max\lvert M\rvert/\sqrt y=0.472$; $N_K$ rational, not integral in general ($N_5(18)=4862/3$, [As26a]) |
| K10(a,b) [LP, double precision] | optimal factorial auxiliary on $J(x)$; exactness threshold; prime adaptation; rank | peer's heights lowered ($572.50$, $2184.01$, $5398.14$); $H^*=\psi(x)-\psi(x/2)$ for $K\ge K_{\rm LP}\approx2.5$–$2.75\sqrt x$ ($x\le10^5$), $\le4\sqrt x$ ($x=10^6$); $G^*=0$ on every prime-power class; optimum $=\mu$ up to $\approx2x^{1/4}$ |
| K10(c,d) [LP] | a priori polytope $E^*(x)$ (Stirling $\pm b$, no primes, no factorials) | allowance $\lvert F-S\rvert\le b$ on $[2,10^7]$; $E^*(x)-x/2=(0.39$–$0.42)\sqrt x\log x$ for $10^3\le x\le10^7$ (table in §4.12; $10^7$ via the dual) |
| K10(f) [LP] | Barban–Vehov base vs the a priori optimum; $\ell^1$ split head/tail | base infeasible on $34$–$56\%$ of $J$; tail share of $\ell^1$: $0.48$, $0.56$, $0.69$ ($x=10^4,10^5,10^6$); primal = dual to all printed digits ($x\le10^6$) |
| K11 [exact sieve + double-precision Stirling] | Möbius construction on the hyperbola, $10^3\le x\le10^9$ | feasible for every $x$ (Thm 4.18); $E(\mu)-x/2=(0.65$–$0.86)\sqrt x\log x$; $\theta_x=0.50\pm0.02$; $V(x)=(0.29$–$0.35)\sqrt x\log x$ against a random-model $0.31$ |
| K12 [exact sieve] | Lemma 4.21 mean square; Möbius construction averaged over $x\in(X,2X]$, $X\le10^7$ | mean square $\div(Y/T)=0.61$–$1.02$ ($5\le T\le3000$); averaged $(E(\mu)-x/2)/(\sqrt x\log x)=0.66$–$0.79$, pointwise $0.57$–$0.85$ |
| K10(e) [exact] | parity identity: prime-2 cone, window Möbius, squares, $\mathbb F_q[T]$ window | Betti numbers match the odd squarefree window ($n\le60$, $72$, $90$); $M(n)$ window identity for all $n\le10^6$; $\sum\lambda(d)\lfloor x/d\rfloor=\lfloor\sqrt x\rfloor$; Liouville factorial valuations ($x=5000$); $\mathbb F_3$, $\mathbb F_5$ windows $=1-q$ |
| K8 [40-digit] | Riemann–Roch on $\overline{\operatorname{Spec}\mathbb Z}$ via direct theta sums; Mellin and continuation; Chebyshev multiplicity-one excess | RR residual $<3\times10^{-39}$; $\Lambda$ matched to $10^{-44}$ on and off the line; excess $0.386X$ against $\sqrt X\log^2X$ |
| K7(a) [exact] | Castelnuovo–Severi Gram on $E/\mathbb F_{101}$, $n\le8$ | inertia $(1,3)$ for every $n$; Hasse-violating control $(2,2)$ |
| K7(b) [numeric, matched pair] | dyadic ladder, $22$ rungs: $\zeta$ from primes to $2^{23}$, DH from its zeros | $\zeta$ passive at every rung for $\omega=0,14.13,85.70$; DH leaves the disk at rung $5$ for $\omega=85.70$ |
| K6 [numeric, independent phases] | Theorem 4.10 on $250$ $\zeta$ windows to $t=5100$ and $5$ DH windows; readout error by resolution rule | residual $2\times10^{-11}$ ($\zeta$), $<10^{-4}$ (DH); misreads $2,1,0,0$ of $250$ for $X=13,1000,t^{1/2},t$; DH readouts $0,0,1,1,2$ correct |
| K5(c) [witness, matched pair] | DH: passive count error; persistence | $+2,+2,+4$ in the windows holding $1,1,2$ off-line zeros, $0$ elsewhere; active port zero $1.7\times10^{-3}$ from $0.7243+176.70i$ at $X=8147$ |

Two further points belong to the record:
- The first run hit a removable singularity of the evaluation formula at $s=\tfrac12$, where the polar term cancels $\zeta$'s pole. It was fixed and logged.
- K3 is a finite witness and is necessary-only. A Pick test detects an off-line zero only when its sample points come near that zero, as K3(e) does by construction. The program's earlier experience is that sample-based Pick tests *under-detect* (P∞-A; the RH proof-path record). RH is a global statement.

## 6. What this paper does and does not do

**It does not prove RH.** The chain in Theorem 3.1 is a sequence of classical equivalences. None is weaker than RH, and the lossless ledger of Corollary 4.2 exists iff RH. Reformulation alone does not move the problem, and we do not claim it does.

**What it deposits:**
1. **One theorem joining the program's two pillars.** The Port Principle's base constraint, at the archimedean place, *is* the program's RH residual.
2. **The Foster/LC realization.** Under RH the zeta port is an infinite series chain of lossless tanks, one per zero pair. The defect Gram's rank counts the tanks (Corollary 4.1).
3. **The forced-ledger corollary.** It gives competing Hilbert–Pólya constructions a precise common target (Corollary 4.2).
4. **Three readings that locate the residual physically:** gain (Proposition 4.3), the boundary rule and arch-domination (§4.4), and the functional equation as losslessness (Proposition 4.5).
5. **Matched-pair certificates,** including a retained pre-registered failure.
6. **The port at finite resolution (§4.6).**
   - Balance is free at every resolution. A finite free gas loses no zero from the line (Proposition 4.6) and is passive above a finite height (Proposition 4.7).
   - Interference drains the line (Proposition 4.8), so the matched pair is separated already at $X=13$.
   - RH is placed at the one limit that is not a stage: the pole-compensated free energy converging down to the balance line (Proposition 4.9).
7. **The third-law curve (§4.7).**
   - The passive finite port is an instrument: its count mismatch is twice the number of off-line zeros.
   - Resolution trades off-line certification (band $\approx c/\log X$, $c\approx1.5$–$2$) for precision on the line.
   - The matched pair separates as predicted: features persist and artifacts wander.
8. **The instrument (§4.8).**
   - Theorem 4.10: the balance count minus the line count is twice the off-line count plus the variation of Selberg's remainder.
   - Corollary 4.11 reads off-line zeros exactly when that variation is below $1$. Certified on $250$ $\zeta$ windows and the DH matched pair.
   - Remark 4.13 separates the two 2's behind $\tfrac12$.
9. **Castelnuovo–Severi over $\mathbb Q$ (§4.9).**
   - Weil's $\mathbb F_q$ proof maps entry by entry onto the two-packet Weil Gram matrix. Its diagonal is archimedean and unconditional.
   - RH $\iff|K(t)|\le q_0$ (Theorem 4.14).
   - The prime $2$ is the zoom gauge of a passive Toeplitz ladder, and the primes $2,3$ give an exact two-clock equivalence (Theorem 4.15).
   - The open step is the arithmetic Riemann–Roch that carries every zoom at once.
10. **The arithmetic Riemann–Roch (§4.10).**
    - Riemann–Roch on $\overline{\operatorname{Spec}\mathbb Z}$ is the functional equation (built and certified), and the Landau half of Bombieri–Stepanov is the Ledger.
    - The remaining statement is the arithmetic Stepanov lemma: an upper bound on primes at square-root precision, i.e. an auxiliary object with multiplicity $\sim\sqrt X$ at every prime in the window. That is the arithmetic Frobenius, to be sought in characteristic one.
11. **The arithmetic Frobenius, measured (§4.11).**
    - The Möbius–Chebyshev object reaches the window count exactly at complexity $K=x$. It is rational, and not integral in general [As26a].
    - On the tested range its efficiency is the Möbius rate, error $x/\sqrt K$; Stepanov's is $x/K$.
    - No improvement of the Möbius mean can close that gap, since $m(x)\ne O(x^{-\alpha})$ for $\alpha>\tfrac12$ [As26a]. Other coefficients are needed.
12. **The optimal auxiliary and the parity identity (§4.12).**
    - The exact factorial optimum is the Legendre sieve: it equals $\psi(x)-\psi(x/2)$ from complexity $\approx2.75\sqrt x$ on.
    - Economical integral auxiliaries are forced to equal $\mu$ on $[1,x^{(1-\theta)/2}/\sqrt2]$ (Theorem 4.16).
    - The a priori polytope bounds $\psi(x)-\psi(x/2)$ with no prime, factorial or zero as input. It is measured at $x/2+0.4\sqrt x\log x$, and a uniform bound at that scale would prove RH (Theorem 4.17).
    - The uniform construction (§4.13). The Möbius function on the hyperbola cells is feasible for every $x$. Its height is the prime window plus half the weighted Mertens variation over the cells (Theorem 4.18), measured at $(0.65$–$0.86)\sqrt x\log x$ to $x=10^9$. The polytope bound lies between RH and RH plus square-root cancellation of $\mu$ on the cells (Corollary 4.19).
    - The construction under RH alone (§4.14). Averaged over $x$, the polytope is an exact RH-equivalent: RH holds iff $\sum_{X<x\le2X}(E^*(x)-x/2)\ll X^{3/2+\varepsilon}$ (Theorem 4.20). The forward direction is the Möbius construction plus Lemma 4.21, square-root cancellation of $\mu$ in short intervals in mean square on RH. The backward direction is Landau on $\int\psi$.
    - The parity identity in three exact forms: Björner's spheres through the prime-2 cone, persistence bars of log-length $\log2$, and squares setting the abscissa $\tfrac12$. Over $\mathbb F_q[T]$ the window Euler characteristic is the constant $q-1$, by Stickelberger and Grothendieck–Lefschetz.

## 7. One inequality at every place

The same inequality — passivity, equivalently positive-real response, positive energy, or positive relative entropy — is the base constraint in four places that the program has so far treated separately:

| Place | The inequality | Status / source |
|---|---|---|
| Thermodynamics and information | passivity ⟹ KMS/Gibbs, fluctuation–dissipation, Landauer; the Bekenstein bound as relative-entropy positivity (Casini) | Port Principle [P]; [Ca08] |
| Causality | passivity at every instant ⟹ causality, Kramers–Kronig | Port Principle Thm 5.1 [P] |
| Gravity | energy conditions (ANEC) from relative-entropy positivity; energy condition ⟹ causality | [FLPW16]; P∞ §4.1 [P]; reading [A] |
| Arithmetic | **RH ⟺ the zeta port is passive** | this paper, Thm 3.1 [P, assembled] |

The table is a statement of organization, not of derivation [A]. It says where to look: the obstruction at the archimedean place is the same *kind* of object as the energy conditions of gravity and the second law of thermodynamics — a positivity of a response function at a boundary — and the tools of each column (dilation, relative entropy, reflection positivity, network synthesis) apply to the others.

---

## References

- [Ar79] D. Z. Arov, Passive linear stationary dynamic systems, *Sibirsk. Mat. Zh.* 20 (1979) 211–228.
- [BC95] J.-B. Bost, A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, *Selecta Math.* 1 (1995) 411–457.
- [As26a] Astro (program peer), Factorial auxiliary: integrality, repair cost, and the exponent target, N7-Factorial-Auxiliary-Repair-2026-10-11.md, with `empirical/connes_route/check_factorial_auxiliary.py` (2026).
- [As26b] Astro (program peer), Integral factorial majorants and generalized arithmetic sections, N7-Integral-Majorants-and-Generalized-Sections-2026-10-11.md, with `empirical/connes_route/optimized_factorial_majorant.py` (2026).
- [Bj11] A. Björner, A cell complex in number theory, *Adv. Appl. Math.* 46 (2011) 71–85; arXiv:1101.5704.
- [BV68] M. B. Barban, P. P. Vehov, An extremal problem, *Trudy Moskov. Mat. Obšč.* 18 (1968) 83–90.
- [Bo73] E. Bombieri, Counting points on curves over finite fields (d'après S. A. Stepanov), *Séminaire Bourbaki* 430 (1973).
- [CEF14] T. Church, J. S. Ellenberg, B. Farb, Representation stability in cohomology and asymptotics for families of varieties over finite fields, *Contemp. Math.* 620 (2014) 1–54.
- [DE80] H. G. Diamond, P. Erdős, On sharp elementary prime number estimates, *L'Enseignement Math.* 26 (1980) 313–321.
- [Gr78] S. Graham, An asymptotic estimate related to Selberg's sieve, *J. Number Theory* 10 (1978) 83–94.
- [Hu72] M. N. Huxley, On the difference between consecutive primes, *Invent. Math.* 15 (1972) 164–170.
- [CC14] A. Connes, C. Consani, The arithmetic site, *C. R. Math. Acad. Sci. Paris* 352 (2014) 971–975; Geometry of the arithmetic site, *Adv. Math.* 291 (2016) 274–329.
- [CC26a] A. Connes, C. Consani, On the Jacobian of $\overline{\operatorname{Spec}\mathbb Z}$, arXiv:2602.15941 (2026).
- [CC26b] A. Connes, C. Consani, On the absolute geometry of $\operatorname{Spec}\mathbb Z$, arXiv:2606.06604 (2026).
- [CC26c] A. Connes, C. Consani, The absolute twistor line and the geometry of $\overline{\operatorname{Spec}\mathbb Z}$, arXiv:2609.00299 (2026).
- [Mi15] J. S. Milne, The Riemann hypothesis over finite fields: from Weil to the present day, arXiv:1509.00797 (2015).
- [CC16] A. Connes, C. Consani, The scaling site, *C. R. Math. Acad. Sci. Paris* 354 (2016) 1–6; Geometry of the scaling site, *Selecta Math.* 23 (2017) 1803–1850.
- [Ca08] H. Casini, Relative entropy and the Bekenstein bound, *Class. Quantum Grav.* 25 (2008) 205021.
- [CC] A. Connes, C. Consani, Weil positivity and trace formula, the archimedean place, arXiv:2006.13771.
- [dB68] L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
- [DH36] H. Davenport, H. Heilbronn, On the zeros of certain Dirichlet series I, II, *J. London Math. Soc.* 11 (1936) 181–185, 307–312.
- [FLPW16] T. Faulkner, R. G. Leigh, O. Parrikar, H. Wang, Modular Hamiltonians for deformed half-spaces and the averaged null energy condition, *JHEP* 09 (2016) 038.
- [Fo24] R. M. Foster, A reactance theorem, *Bell Syst. Tech. J.* 3 (1924) 259–267.
- [GFH20] Y. Guryanova, N. Friis, M. Huber, Ideal projective measurements have infinite resource costs, *Quantum* 4 (2020) 222.
- [Go12] S. M. Gonek, Finite Euler products and the Riemann hypothesis, *Trans. Amer. Math. Soc.* 364 (2012) 2157–2191.
- [In32] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge, 1932.
- [La99] J. C. Lagarias, On a positivity property of the Riemann ξ-function, *Acta Arith.* 89 (1999) 217–234.
- [LP67] P. D. Lax, R. S. Phillips, *Scattering Theory*, Academic Press, 1967.
- [Le74] N. Levinson, More than one third of zeros of Riemann's zeta-function are on $\sigma=1/2$, *Adv. Math.* 13 (1974) 383–436.
- [MV74] H. L. Montgomery, R. C. Vaughan, Hilbert's inequality, *J. London Math. Soc.* (2) 8 (1974) 73–82.
- [MP05] N. Makarov, A. Poltoratski, Meromorphic inner functions, Toeplitz kernels and the uncertainty principle, in *Perspectives in Analysis*, Springer, 2005.
- [Re18] C. Remling, *Spectral Theory of Canonical Systems*, de Gruyter, 2018.
- [Se46] A. Selberg, Contributions to the theory of the Riemann zeta-function, *Arch. Math. Naturvid.* 48 (1946) 89–155.
- [Sp90] D. Spector, Supersymmetry and the Möbius inversion function, *Comm. Math. Phys.* 127 (1990) 239–252.
- [SNF70] B. Sz.-Nagy, C. Foias, *Harmonic Analysis of Operators on Hilbert Space*, North-Holland, 1970.
- [Ti86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown, Oxford, 1986 (§14.2, §14.25).
- [Tu53] A. M. Turing, Some calculations of the Riemann zeta-function, *Proc. London Math. Soc.* (3) 3 (1953) 99–117.
- [Zh26] X. Zhu, Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law, arXiv:2608.24827 (2026).
- [vdGS00] G. van der Geer, R. Schoof, Effectivity of Arakelov divisors and the theta divisor of a number field, *Selecta Math.* 6 (2000) 377–398.
- [vK01] H. von Koch, Sur la distribution des nombres premiers, *Acta Math.* 24 (1901) 159–182.
- Program: PortPrinciple.md (Defs 2.2, 2.5; Prop 2.3; Thms 4.1–4.5, 5.1; Prop 4.4; Thm 6.9; Prop 6.9e); P∞-A (Pinf-A-deBranges-as-OS-Reconstruction-Draft1.md); P∞ (Pinf-WhatIsMultiplicative-Draft1.md §4.1); N14; P0.
