# 59 — The Arithmetic of Work Extraction: Copy Thresholds, Process Orders, and the Size of the Prize

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*First draft — October 2, 2026*

<!--
INTERNAL LOG — NOT FOR PUBLICATION (pandoc drops HTML comments)
2026-10-02 v0.1.  Request (Leo): "proceed" with the copy-threshold standalone paper aimed at experiment, starting with the
missing "size of the prize" computation (Port Remark 6.9f).  Sections 2-3 condense PortPrinciple.md Section 6 (proofs
there in full); Sections 4-6 are new.
Prior-art check (2026-10-02): Sparaciari-Jennings-Oppenheim 2017 (open minimality question), Salvia-Giovannetti 2020,
Alicki-Fannes 2013, Skrzypczyk-Silva-Brunner 2015; nonlinear coherent heat machines (Opatrny et al. 2023, Kerr-based);
charge-preserving ergotropy (PRX Energy); ergotropy experiments in superconducting qubits, NMR, trapped ions.  No closed
form for the work of a k:m exchange, no minimal-order law, no copy-threshold experiment was found.
Certificates (empirical/copythresholds59/):
  p59_cert.py (oscillator prize): run 1 3/5 -- O2-O4 PASS blind; O1 FAILED on a checker truncation bound wrong for k != m
    (two cases agreed to 12 digits), O5 NO VERDICT (findroot left the physical range); retained.  Run 2 5/5 (O1, O5 not
    blind).
  p59b_qubit_prize.py (qubit copies): 4/4 -- R1, R2 reproduce an exploratory scan (not blind, disclosed); B1, B2 blind
    predictions (1/sqrt2 vs 3/4) pass.
Platform numbers (Section 6) are arithmetic on the certified closed form; [A] for the device assumptions.
-->

---

## Abstract

A passive state yields no work under any cycle. Many copies of it may, and the question of how many was left open (Sparaciari–Jennings–Oppenheim 2017). We answer it, and then ask how much work there is and how an experiment would see it.

**Thresholds.** For three levels, or two qubit reservoirs at different temperatures, the least number of copies is the denominator of the simplest fraction (Stern–Brocot) strictly inside a window. The window's ends are an energy ratio and an entropy ratio; for two reservoirs it is the Carnot window of gear ratios. Near equilibrium the threshold scales as $(T/\Delta T)^{1/r}$, where $r$ is the number of rationally independent level spacings, and as $(T/\Delta T)^{1/(d-1)}$ for almost every spectrum. Commensurate spectra are the worst case. For golden-ratio spacings the thresholds are Fibonacci numbers.

**Process orders.** For two harmonic modes one copy suffices, and the same arithmetic counts the order of the nonlinear process: an exchange of $k$ quanta of the hot mode for $m$ quanta of the cold one extracts work iff $1<k\omega_B/(m\omega_A)<T_B/T_A$.

**The size of the prize (new).** We give it in closed form. The most work any dynamics conserving the "gear charge" $kN_A+mN_B$ can extract is
$$W_{k,m}=\max\big\{0,\ (k\omega_B-m\omega_A)\,[\bar n_B(k\omega_B)-\bar n_A(m\omega_A)]\big\},$$
the energy of the composite exchange times the difference of the Bose occupations of the two composite quanta, each at its own temperature. Near equilibrium, $W_{k,m}=k_BT\,\delta^2\,\theta(1-\theta)\,C_E(m\hbar\omega_A/k_BT)$, where $\theta$ is the fraction's position in the window and $C_E$ the Einstein heat-capacity function. At the window's centre in the classical regime, a single $k{:}m$ exchange recovers the full reversible (Carnot) work between the two modes.

**Resonance penalties.** Commensurate spectra pay three times:
- in order: at 20% contrast a 1:2 pair needs order 11, a golden pair order 5;
- in prize: the minimal exchange of a resonant pair captures only about $4\delta$ of the reversible work, against $0.73$ on average for golden spacings;
- for qubit copies, in harvest: half the reversible work needs 94 copies at 10% contrast, against 11.

**Experiment.** We give platform estimates for superconducting circuits, trapped-ion modes and programmable qubit arrays. The cleanest test is a $k{:}m$ converter whose work output switches on at $T_B/T_A=k\omega_B/(m\omega_A)$. With processes up to order 5, golden-ratio modes yield work down to $7.9\%$ temperature contrast and 1:2 modes only above $33\%$. Certificates are exact or 40-digit, with failures retained.

---

## 1. The question

A state is **passive** for a Hamiltonian if no unitary lowers its energy, and **completely passive** if every number of copies is passive. Pusz–Woronowicz (1978) and Lenard (1978) showed that the completely passive states are the thermal ones. Every passive but non-thermal state is therefore activated at some finite number of copies $n^*$. Alicki and Fannes (2013) showed that collective operations on many copies can extract more work per copy than local ones. Skrzypczyk, Silva and Brunner (2015) characterized complete passivity by equal virtual temperatures. Sparaciari, Jennings and Oppenheim (2017) showed that a passive state activated by a swap cycle on $m$ and $n$ pairs becomes active at $m+n$ copies, and asked whether fewer suffice. Salvia and Giovannetti (2020) gave the occupation-number criterion for $N$-passivity.

This paper:
- (i) gives $n^*$ exactly, with its asymptotics (§§2–3; the full proofs are in PortPrinciple.md, §6);
- (ii) shows that for oscillators the same arithmetic counts process orders (§4);
- (iii) computes the work that becomes available at threshold and beyond (§5);
- (iv) proposes how to see all of this in a laboratory (§6).

**Tiers.** [P] proven here or cited as stated; [A] structural reading or device assumption; numerics are labelled. *Copies* means independent systems acted on by one global unitary, with energy additive over copies.

---

## 2. The lattice form of passivity

**Lemma 2.1 (occupation lattice) [P].** Let $\rho$ be faithful and diagonal in an eigenbasis of $H$, with levels $E_i$ and $f_i=-\ln p_i$. Then $\rho^{\otimes n}$ is passive iff no integer vector $c$ satisfies
$$\textstyle\sum_ic_i=0,\qquad\sum_ic_i^+\le n,\qquad c\cdot E<0<c\cdot f .$$

*Proof.* A product basis vector is fixed by occupation numbers $\nu$ with $\sum\nu_i=n$; its energy is $\nu\cdot E$ and its probability $e^{-\nu\cdot f}$. A state diagonal in the energy basis is passive iff no lower-energy basis vector is less populated than a higher-energy one. With $c=\nu-\nu'$ this is the condition stated. Conversely, any such $c$ is realized by $\nu=c^++r$ and $\nu'=c^-+r$, with $r\ge0$ and $\sum_i r_i=n-\sum_ic^+_i$. $\square$

Passing to the difference vector $c$ turns the number of copies into a cost, $\sum_ic_i^+$, to be minimized over the integer points of an open cone.

---

## 3. Thresholds

**Theorem 3.1 (three levels) [P].** Let $E_0<E_1<E_2$, and let $\rho$ be faithful, passive and not thermal. Put $r_E=\frac{E_1-E_0}{E_2-E_0}$ and $r_f=\frac{f_1-f_0}{f_2-f_0}$. Then $n^*$ is the least denominator of a fraction strictly between $r_E$ and $r_f$: the denominator of the Stern–Brocot simplest fraction of that interval.

*Proof.* Write $c=(-a-b,a,b)$. The two inequalities force $a$ and $b$ to have opposite signs. In both cases they say that $k/m$ lies strictly between $r_E$ and $r_f$, and the cost $\sum c^+$ equals the denominator $m$. The simplest fraction of an interval has the least denominator (Stern 1858; Brocot 1861). $\square$

**Corollary 3.2 (two reservoirs: the Carnot window) [P].** Two qubit ports with gaps $\varepsilon_A,\varepsilon_B$ in thermal states at $\beta_A>\beta_B$ have
$$n^*=\min\Big\{\max(k,m):\ \frac{\varepsilon_A}{\varepsilon_B}<\frac km<\frac{\beta_A}{\beta_B}\frac{\varepsilon_A}{\varepsilon_B}\Big\}.$$
The minimizing exchange moves $k$ quanta out of the hot port and $m$ into the cold one, with efficiency $1-m\varepsilon_A/(k\varepsilon_B)$, which lies strictly between $0$ and the Carnot value exactly inside the window. (Proof: Lemma 2.1 on the four joint levels; PortPrinciple.md, Corollary 6.7.) This settles the minimality question of Sparaciari–Jennings–Oppenheim: no unitary on fewer copies extracts work, and that many copies suffice.

**Proposition 3.3 (resonant versus irrational spacings) [P].** Write $x=\varepsilon_A/\varepsilon_B$ and $\beta_A/\beta_B=1+\delta$.
- If $x=p/q$, then $n^*>1/(p\delta)$; for $x=\tfrac12$, $n^*$ is the least odd integer exceeding $1/\delta$.
- If the partial quotients of $x$ are bounded by $A$, then $n^*\le(A+1)^2/\sqrt{x\delta}$.
- For $x=1/\varphi$, $n^*$ is a Fibonacci number $F_n$, with $n$ the least even integer such that $\varphi^{2n-1}>\sqrt5/\delta+1/\varphi$.

(PortPrinciple.md, Proposition 6.8.)

**Theorem 3.4 (resonance-rank law) [P].** For $d$ levels near equilibrium, let $r$ be the rank of the module of level spacings. If that module is badly approximable, then $n^*\asymp\delta^{-1/r}$. For Lebesgue-almost every spectrum, $\ln n^*/\ln(1/\delta)\to1/(d-1)$. With $k$ qubit reservoirs whose gaps span a degree-$k$ number field, $n^*\asymp\delta^{-1/k}$. A conserved charge can raise the exponent. (PortPrinciple.md, Theorems 6.9, 6.9′, Corollaries 6.9a–d; proofs by norm forms, Dirichlet, Minkowski's second theorem, Jarník's covering bound and Borel–Cantelli.)

**Proposition 3.5 (echo–yield duality) [P + A].** The time for all phases of a ledger with these spacings to return within $\varepsilon$ scales as $\varepsilon^{-(r-1)}$. So the echo exponent $e=r-1$ and the yield exponent $y=1/r$ satisfy $y(e+1)=1$, through Khinchin's transference (PortPrinciple.md, Proposition 6.9e).

---

## 4. Process orders for oscillators

For harmonic modes the levels are unbounded, so one copy already contains every exchange. The arithmetic moves from copies to the order of the process.

**Proposition 4.1 (minimal order) [P].** Two harmonic modes with frequencies $\omega_A,\omega_B$, in thermal states at $T_A<T_B$, are never jointly passive. The levels $(n_A,n_B)$ and $(n_A+m,\,n_B-k)$ form an inverted pair — the higher-energy one more populated — exactly when
$$1<\frac{k\,\omega_B}{m\,\omega_A}<\frac{T_B}{T_A}.\tag{4.1}$$
The least order $k+m$ of a work-extracting exchange is the order of the simplest fraction in the window $(x,\,x(1+\delta))$, with $x=\omega_A/\omega_B$ and $1+\delta=T_B/T_A$. That fraction also minimizes $k$ and $m$ separately.

*Proof.* The energy difference is $k\omega_B-m\omega_A$. The population ratio is $e^{\beta_Bk\omega_B-\beta_Am\omega_A}$. Inversion requires both to be positive, which is (4.1). Minimality follows from the Stern–Brocot property. (PortPrinciple.md, Corollary 6.9c; certificate O2: 300 random windows.) $\square$

Condition (4.1) is a Carnot condition for a $k{:}m$ converter. The composite hot quantum $k\hbar\omega_B$ must exceed the composite cold quantum $m\hbar\omega_A$, by less than the temperature ratio. For $k=m=1$ it is the condition for a frequency converter to act as an engine. The arithmetic enters when the temperature contrast is small: then only high-order exchanges fit in the window, and which orders fit depends on how well $x$ is approximated by fractions.

---

## 5. The size of the prize

### 5.1 Oscillators: the gear-charge ergotropy

For coprime $(k,m)$, call $K=kN_A+mN_B$ the **gear charge**. The unitaries conserving $K$ are exactly those generated by $a^{\dagger m}b^k$, its adjoint, $N_A$ and $N_B$. Each eigenspace of $K$ is one *ladder* $\{(a+jm,\,b-jk)\}$, because solutions of $kn_A+mn_B=K$ differ by multiples of $(m,-k)$.

**Theorem 5.1 (the prize of a $k{:}m$ exchange) [P].** For thermal modes with $u=e^{-\beta_A\omega_A}$ and $v=e^{-\beta_B\omega_B}$, the most work extractable by unitaries conserving the gear charge is
$$W_{k,m}=\max\Big\{0,\ (k\omega_B-m\omega_A)\Big[\frac1{e^{\beta_Bk\omega_B}-1}-\frac1{e^{\beta_Am\omega_A}-1}\Big]\Big\}.$$
It is positive exactly in the window (4.1).

*Proof.* Consider a ladder whose top state $(a_0,b_0)$ has $a_0<m$. Along it, populations change by the factor $\rho=u^mv^{-k}$ per step and energies by $-\Delta$ per step, where $\Delta=k\omega_B-m\omega_A$. Take the case $\Delta>0$ and $\rho<1$, which is the window. The ladder is then fully inverted, and its passive rearrangement is its reversal. A ladder of length $J+1$ yields $p_0\Delta\sum_{j=0}^J\rho^j(J-2j)$.

Summing over $a_0\in[0,m)$ and $b_0=kJ+s$ with $s\in[0,k)$ gives $\Delta(1-u^m)(1-v^k)\sum_Jv^{kJ}\sum_{j\le J}\rho^j(J-2j)$. The double sum equals $w(1-\rho)/((1-w)^2(1-w\rho)^2)$ with $w=v^k$. Since $w\rho=u^m$, everything collapses to
$$\Delta\,\frac{v^k-u^m}{(1-v^k)(1-u^m)}=\Delta\big[\bar n_B(k\omega_B)-\bar n_A(m\omega_A)\big].$$
The opposite orientation is symmetric. Outside the window no ladder is inverted, so the work is zero. *Certificate O1:* brute-force ladder ergotropy against the closed form, 24 random parameter sets, at 40 digits, agreement to $10^{-25}$. $\square$

*Reading.* A $k{:}m$ exchange is an engine between two *composite oscillators*. One has quantum $k\hbar\omega_B$ and is Bose-occupied at $T_B$; the other has quantum $m\hbar\omega_A$ and is Bose-occupied at $T_A$. The work per cycle is the energy of the exchange times the occupation difference.

**Corollary 5.2 (near equilibrium) [P, leading order].** Let $\beta_A=\beta(1+\delta)$, $\beta_B=\beta$, and let the fraction sit at $k/m=x(1+\theta\delta)$ with $\theta\in(0,1)$. Then
$$W_{k,m}=k_BT\,\delta^2\,\theta(1-\theta)\,C_E\big(m\hbar\omega_A/k_BT\big)\,\big(1+O(\delta)\big),\qquad C_E(z)=\frac{z^2e^z}{(e^z-1)^2}.$$
*Certificate O3:* the relative error is $1.5\times10^{-2}$, $1.5\times10^{-3}$, $1.5\times10^{-4}$ at $\delta=10^{-2},10^{-3},10^{-4}$.

**Corollary 5.3 (one exchange can capture the Carnot work) [P, leading order].** The reversible work between two finite oscillators, at equal entropy and a common final temperature, is $W_{\rm rev}=\tfrac12k_BT\,\delta^2\,C_AC_B/(C_A+C_B)\,(1+O(\delta))$, which is $k_BT\delta^2/4$ in the classical regime. A single exchange with $\theta=\tfrac12$ and $m\hbar\omega_A\ll k_BT$ attains it. *Certificate O4:* ratio $0.9999999$ at $\delta=10^{-3}$.

In the quantum regime the composite quantum is penalized by $C_E(m\hbar\omega_A/k_BT)$. This decays like $z^2e^{-z}$, so high-order exchanges pay exponentially.

**Corollary 5.4 (the resonance penalty is paid in the prize) [P].** For $x=\tfrac12$, the minimal exchange $\tfrac{(m+1)/2}{m}$, with $m$ the least odd integer above $1/\delta$, has $4\theta(1-\theta)<8\delta$. In the classical regime it therefore captures less than $8\delta$ of the reversible work: $3.9\%$ at $\delta=10^{-2}$ and $0.40\%$ at $\delta=10^{-3}$. For $x=1/\varphi$, the minimal exchange captures on average $0.73$ of it (mean over 200 log-uniform $\delta$ in $[10^{-4},10^{-2}]$). *Certificate O5.*

*Why.* For a commensurate ratio, the window's cold edge is the resonance itself. The first admissible fraction then sits at the hot edge, $\theta\approx1$, where the occupation difference vanishes. Larger orders reach the window's centre and restore the full prize. Resonant spectra must choose between the minimal order with almost no prize, or twice the order for the full prize.

### 5.2 Qubit copies: prize at threshold and harvest number

For qubit copies the exact $n$-copy ergotropy is computable from the $(n+1)^2$ occupation groups. Let $f(n)=W(n)/(n\,W_{\rm rev})$ be the per-copy work as a fraction of the reversible work of one copy. Let the **harvest number** $n_{1/2}$ be the least $n$ with $f\ge\tfrac12$. With $\varepsilon_B=1$, $\varepsilon_A=x$, $\beta_B=1$ and $\beta_A=1+\delta$:

| spectrum | $\delta$ | $n^*$ | $f(n^*)$ | $n_{1/2}$ |
|---|---|---|---|---|
| golden $1/\varphi$ | 0.2 | 3 | 0.199 | 5 |
| | 0.1 | 3 | 0.138 | 11 |
| | 0.05 | 8 | $1.6\times10^{-3}$ | 39 |
| $1/\sqrt3$ | 0.2 | 3 | 0.141 | 7 |
| | 0.1 | 5 | 0.051 | 14 |
| | 0.025 | 12 | $6.5\times10^{-5}$ | 70 |
| resonant $\tfrac12$ | 0.2 | 7 | $6.7\times10^{-3}$ | 29 |
| | 0.1 | 11 | $8.2\times10^{-5}$ | 94 |
| | 0.05 | 21 | $5.2\times10^{-9}$ | $>160$ |
| | 0.025 | 41 | $1.6\times10^{-17}$ | $>160$ |

- At threshold the prize is a modest fraction of the reversible work for badly approximable spectra.
- For resonant spectra it collapses roughly exponentially in $n^*$, because a qubit can hold one excitation and the inverted configurations become rare.
- The harvest number repeats the ordering.
- A blind prediction made before computing (certificate B1–B2) holds: at $\delta=0.05$, $x=1/\sqrt2$ has $n^*=7$, $f(n^*)$ thirteen times larger, and $n_{1/2}=39$, against $x=3/4$ with $n^*=9$ and $n_{1/2}=62$.

---

## 6. Platforms and protocols

**Table 6.1. The order staircase.** The least work-extracting exchange $k{:}m$, with its order $k+m$ in brackets, as the temperature contrast $\delta=T_B/T_A-1$ shrinks.

| $x=\omega_A/\omega_B$ | $\delta=0.5$ | 0.3 | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 |
|---|---|---|---|---|---|---|---|
| golden $1/\varphi$ | 2/3 [5] | 2/3 [5] | 2/3 [5] | 2/3 [5] | 5/8 [13] | 5/8 [13] | 13/21 [34] |
| $1/\sqrt2$ | 1/1 [2] | 3/4 [7] | 3/4 [7] | 3/4 [7] | 5/7 [12] | 5/7 [12] | 17/24 [41] |
| $1/\sqrt3$ | 2/3 [5] | 2/3 [5] | 2/3 [5] | 3/5 [8] | 3/5 [8] | 7/12 [19] | 11/19 [30] |
| $1/2$ (resonant) | 2/3 [5] | 3/5 [8] | 4/7 [11] | 6/11 [17] | 11/21 [32] | 26/51 [77] | 51/101 [152] |
| $2/3$ (resonant) | 3/4 [7] | 3/4 [7] | 3/4 [7] | 5/7 [12] | 9/13 [22] | 19/28 [47] | 35/52 [87] |

**The minimal contrast for a fixed process.** By (4.1), a $k{:}m$ exchange with $k/m>x$ works iff $\delta>(k/m)/x-1$. For the order-5 exchange $2{:}3$:

| spectrum | minimal contrast for $2{:}3$ |
|---|---|
| golden ratio | $\delta>2\varphi/3-1=0.079$ |
| $\sqrt3$ | $\delta>2\sqrt3/3-1=0.155$ |
| $1{:}2$ | $\delta>1/3$ |

**Table 6.2. Prize per cycle** (Theorem 5.1, at the least order; $\omega_B$ is the higher mode).

| platform | $x$ | $\delta$ | least exchange | prize per cycle |
|---|---|---|---|---|
| superconducting, $\omega_B/2\pi=6$ GHz, $T_B=150$ mK | golden | 0.2 | 2:3 [5] | $1.1\times10^{-3}\,\hbar\omega_B$ |
| | 1/2 | 0.2 | 4:7 [11] | $7.4\times10^{-5}\,\hbar\omega_B$ |
| superconducting, $T_B=300$ mK | golden | 0.2 | 2:3 [5] | $5.5\times10^{-3}\,\hbar\omega_B$ |
| | 1/2 | 0.2 | 4:7 [11] | $2.0\times10^{-3}\,\hbar\omega_B$ |
| trapped-ion radial modes, $\omega_B/2\pi=3$ MHz, $T_B=1$ mK | golden | 0.2 | 2:3 [5] | $0.051\,\hbar\omega_B$ |
| | 1/2 | 0.2 | 4:7 [11] | $0.040\,\hbar\omega_B$ |

**Protocol P1: a $k{:}m$ converter in superconducting circuits [A].**
- *Setup.* Two microwave modes whose frequency ratio is set by flux tuning. Engineered noise injection holds them at effective temperatures $T_A<T_B$. A parametrically pumped Josephson element supplies the coupling $a^{\dagger m}b^k$, with the pump at $|k\omega_B-m\omega_A|$. Three-photon conversion has been observed (Chang et al. 2020), so orders up to about 5 are plausible.
- *Observable.* The sign of the energy delivered to the pump, the work, as $T_B/T_A$ is swept.
- *Prediction.* The sign switches on at $T_B/T_A=k\omega_B/(m\omega_A)$. With the $2{:}3$ exchange, a golden pair delivers work above $7.9\%$ contrast, a $1{:}2$ pair only above $33\%$.
- *Prize.* About $10^{-3}$ quanta per cycle at 150 mK. Measuring the sign is far easier than measuring the amount.

**Protocol P2: trapped-ion radial modes [A].**
- *Setup.* In a two-ion crystal the radial centre-of-mass and rocking frequencies have ratio $\sqrt{1-(\omega_z/\omega_r)^2}$. Changing the axial confinement $\omega_z$ by about $10\%$ moves $x$ from the golden ratio ($\omega_z=0.786\,\omega_r$) to $\tfrac12$ ($\omega_z=0.866\,\omega_r$).
- *Couplings.* Sidebands driven by lasers supply $a^{\dagger m}b^k$, suppressed by roughly the Lamb–Dicke factor $\eta^{k+m}$. The Coulomb anharmonicity supplies native couplings of order 3 (Marquet–Schmidt-Kaler–James 2003).
- *Regime.* Near the Doppler limit, the modes are in the classical regime, and the prize is about $0.05$ quanta per cycle at 20% contrast. The observable is the phonon-number change of the two modes.

**Protocol P3: copy thresholds on a programmable qubit array [A].**
- *Setup.* Prepare $n$ pairs of qubits in diagonal thermal-like states at two temperatures. Apply the optimal permutation unitary on all $2n$ qubits. Measure the energy before and after.
- *Prediction.* Nothing for $n<n^*$ and a positive prize at $n^*$. For golden spacings at 10–20% contrast that is 6 qubits ($n^*=3$); for a $1{:}2$ ratio at 20% it is 14 qubits ($n^*=7$).
- *What it tests.* This demonstrates the hierarchy of collective activation on real hardware. Its content is the combinatorics together with the device's fidelity; the oscillator protocols test the physics.

**What an experiment can refute [A].** The thresholds and the prize are theorems, given additive energies, thermal input states and unitary (closed-system) processes. A measured violation would therefore indicate a broken hypothesis. Candidates: interaction energies between modes, non-thermal preparation, other channels for energy, or a pump that is not a pure work reservoir. Within those hypotheses, P1 is a sharp test. Work below $T_B/T_A=k\omega_B/(m\omega_A)$, or none above it once losses are accounted for, would be a genuine anomaly.

---

## 7. What is new

| Result | Status |
|---|---|
| occupation criterion for $N$-passivity | known (Pusz–Woronowicz, Lenard; Salvia–Giovannetti 2020) |
| swap-cycle activation at $m+n$ copies; the Carnot window of swap cycles | known (Sparaciari–Jennings–Oppenheim 2017) |
| **exact $n^*$** (Stern–Brocot) and its two-reservoir form | new (Theorem 3.1, Corollary 3.2; PortPrinciple.md) |
| resonance-rank law, almost-every exponent, echo–yield duality | new (PortPrinciple.md) |
| minimal process order for oscillators; the $k{:}m$ Carnot condition (4.1) | the condition is elementary; the minimal-order law is new |
| **closed-form gear-charge ergotropy** and its near-equilibrium form | new (Theorem 5.1, Corollaries 5.2–5.4) |
| one exchange at the window's centre captures the reversible work | new (Corollary 5.3) |
| resonance penalties in prize and harvest; qubit prize table | new (§5) |
| platform estimates and protocols | new [A] |

---

## 8. Certificates

`empirical/copythresholds59/`:

| File | Checks | Result |
|---|---|---|
| `p59_cert.py` | O1 closed form against brute force; O2 minimal order = simplest fraction; O3 near-equilibrium formula; O4 Carnot capture; O5 resonance penalty | run 1: 3/5. O2–O4 passed blind. O1 failed on a checker truncation bound that was wrong for $k\ne m$ (the two cases agreed to 12 digits); O5 gave no verdict (the root-finder left the physical range). Both retained. Run 2: 5/5, not blind for O1 and O5 |
| `p59b_qubit_prize.py` | R1 reproduction of the exploratory table (not blind, disclosed); R2 $W=0$ below $n^*$, $n^*$ = Stern–Brocot; B1–B2 blind prediction $1/\sqrt2$ versus $3/4$ | 4/4 |

The threshold theorems of §3 are certified in PortPrinciple.md (certificates P2, P5–P8).

---

## References

- R. Alicki, M. Fannes, Entanglement boost for extractable work from ensembles of quantum batteries, *Phys. Rev. E* 87 (2013) 042123.
- A. Brocot, Calcul des rouages par approximation, *Revue Chronométrique* 3 (1861) 186.
- J. W. S. Cassels, *An Introduction to Diophantine Approximation*, Cambridge, 1957.
- C. W. S. Chang et al., Observation of three-photon spontaneous parametric down-conversion in a superconducting parametric cavity, *Phys. Rev. X* 10 (2020) 011011.
- D. F. V. James, Quantum dynamics of cold trapped ions with application to quantum computation, *Appl. Phys. B* 66 (1998) 181.
- A. Lenard, Thermodynamical proof of the Gibbs formula for elementary quantum systems, *J. Stat. Phys.* 19 (1978) 575.
- N. Linden, S. Popescu, P. Skrzypczyk, How small can thermal machines be?, *Phys. Rev. Lett.* 105 (2010) 130401.
- J. M. Manley, H. E. Rowe, Some general properties of nonlinear elements, *Proc. IRE* 44 (1956) 904.
- C. Marquet, F. Schmidt-Kaler, D. F. V. James, Phonon–phonon interactions due to non-linear effects in a linear ion trap, *Appl. Phys. B* 76 (2003) 199.
- T. Opatrný et al., Nonlinear coherent heat machines, *Sci. Adv.* 9 (2023) eadf1070.
- W. Pusz, S. L. Woronowicz, Passive states and KMS states for general quantum systems, *Commun. Math. Phys.* 58 (1978) 273.
- J. Roßnagel et al., A single-atom heat engine, *Science* 352 (2016) 325.
- R. Salvia, V. Giovannetti, Energy upper bound for structurally stable N-passive states, *Quantum* 4 (2020) 274.
- P. Skrzypczyk, R. Silva, N. Brunner, Passivity, complete passivity, and virtual temperatures, *Phys. Rev. E* 91 (2015) 052133.
- C. Sparaciari, D. Jennings, J. Oppenheim, Energetic instability of passive states in thermodynamics, *Nat. Commun.* 8 (2017) 1895.
- M. A. Stern, Über eine zahlentheoretische Funktion, *J. reine angew. Math.* 55 (1858) 193.
- Program: PortPrinciple.md (Lemma 6.2, Theorems 6.6, 6.9, 6.9′, Corollaries 6.7, 6.9a–d, Propositions 6.8, 6.8a, 6.9e).
