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

An exact certificate verifies the identities and a Foster matched pair (real zeros give positive tanks and a rank-$2n$ Gram; an off-line pair gives a right-half-plane pole and a negative Gram entry). A 50-digit witness on $\zeta$ checks positive-realness on a grid, positive-definite Pick matrices near the first six zeros, a dissipation-spectrum count of the zeros ($10.0023$ against $10$), and the Foster tanks at the actual zero ordinates ($1.1\times10^{-4}$ relative error with tail). A control with a planted off-line quartet is flagged. Finite witnesses are necessary-only. **RH is not proved here; it is placed** — as the program's base inequality, evaluated at the archimedean place.

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
- Any *quantitative* copy-threshold statement for truncated Bost–Connes ledgers is [C] and is left open.

## 5. Certificates

`empirical/passive_ports/p53_bridge_cert.py`. Falsifiers were pre-registered before the first run.

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
- [Ca08] H. Casini, Relative entropy and the Bekenstein bound, *Class. Quantum Grav.* 25 (2008) 205021.
- [CC] A. Connes, C. Consani, Weil positivity and trace formula, the archimedean place, arXiv:2006.13771.
- [dB68] L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
- [FLPW16] T. Faulkner, R. G. Leigh, O. Parrikar, H. Wang, Modular Hamiltonians for deformed half-spaces and the averaged null energy condition, *JHEP* 09 (2016) 038.
- [Fo24] R. M. Foster, A reactance theorem, *Bell Syst. Tech. J.* 3 (1924) 259–267.
- [In32] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge, 1932.
- [La99] J. C. Lagarias, On a positivity property of the Riemann ξ-function, *Acta Arith.* 89 (1999) 217–234.
- [LP67] P. D. Lax, R. S. Phillips, *Scattering Theory*, Academic Press, 1967.
- [MP05] N. Makarov, A. Poltoratski, Meromorphic inner functions, Toeplitz kernels and the uncertainty principle, in *Perspectives in Analysis*, Springer, 2005.
- [Re18] C. Remling, *Spectral Theory of Canonical Systems*, de Gruyter, 2018.
- [SNF70] B. Sz.-Nagy, C. Foias, *Harmonic Analysis of Operators on Hilbert Space*, North-Holland, 1970.
- [vK01] H. von Koch, Sur la distribution des nombres premiers, *Acta Math.* 24 (1901) 159–182.
- Program: PortPrinciple.md (Defs 2.2, 2.5; Prop 2.3; Thms 4.1–4.5, 5.1; Prop 4.4; Thm 6.9; Prop 6.9e); P∞-A (Pinf-A-deBranges-as-OS-Reconstruction-Draft1.md); P∞ (Pinf-WhatIsMultiplicative-Draft1.md §4.1); N14; P0.
