# The Port Principle: One Inequality Beneath Impedance, Fluctuation, Measurement, and Information

**Leonardo Murillo Montero**

---

## Abstract

Every measurement, model, and machine touches the world through a *port*: a boundary at which a system can be both pushed and watched. We state one inequality — *no port gives more than it takes* (passivity) — and show that three quantifiers of it generate structural laws usually taught in separate courses. Passivity **at every instant** forces causality, hence Kramers–Kronig dispersion and an exact equal-energy law between the resistive and reactive parts of any response. Passivity **for every input** forces a lossless ledger: every lossy port is a corner of a reversible system, and a finite ledger carries loss only up to a sharp horizon, after which the echo returns. Passivity **for every number of copies** forces temperature, the zeroth law, and the fluctuation–dissipation theorem, whose four spectral weights $\coth x,\;1/x,\;\tanh x,\;x$ are, respectively, the watched variance, the pushed susceptibility, and the Bures and Kubo–Mori information metrics. Two joins then carry most of the practical weight. First, *noise is temperature times the squared defect of the dilation*: Kirchhoff's radiation law, Johnson–Nyquist noise, and Caves's amplifier bound are one formula, $N=|1-\tau|(n+\tfrac12)$, for passive (rotation-dilated) and active (boost-dilated) ports alike. Second, the relation of a port to a conserved Noether charge — *can it supply the charge, can it read it* — classifies protected memory, non-demolition measurement, control, and thermalization in a single two-by-two table. We give finite, exact proofs, a certificate suite, a definition of "port" usable from any discipline, a modeling calculus in which interconnection, reduction, dilation, and noise assignment all preserve passivity, a list of questions the principle answers in one line, and an account of where it strains: gravity, the origin of the arrow of time, and single measurement outcomes.

---

## 1. Watching and pushing

There are exactly two ways to learn about anything. You can **watch** it — record its fluctuations while leaving it alone — or you can **push** it — apply a small, known disturbance and record the response. A physicist watches Brownian motion and pushes with a force; an engineer watches the hiss of a resistor and pushes with a voltage; an economist watches prices and pushes with an order; a statistician watches observational data and pushes with an intervention; a neuroscientist watches spontaneous activity and pushes with a stimulus.

The fluctuation–dissipation theorem (FDT) says that, at equilibrium, the two ways agree: what you learn by watching determines what you would learn by pushing. This paper argues that the FDT is one face of a more primitive fact, and that the same fact, read three ways, also yields causality, the existence of reversible completions of irreversible processes, and the existence of temperature. The primitive fact is a statement about the place where watching and pushing happen — the *port* — and it is the oldest inequality in thermodynamics, Kelvin's: **no cyclic process at a port can extract net work from its reference state.** In one line:

> **Port Principle.** No port gives more than it takes.

### 1.1 The three quantifiers

The inequality "absorbed energy $\ge 0$" can be demanded over three different ranges, and each range forces a different law.

| Passive for … | forces … | §  |
|---|---|---|
| **every instant** (absorbed energy up to *any* time $t$) | causality ⟹ dispersion relations, causal parity | 4 |
| **every input** (the scattering map is a contraction) | a lossless ledger: every lossy port is a corner of a reversible system; finite ledgers echo | 5 |
| **every number of copies** (no work from $\rho^{\otimes n}$ for any $n$) | temperature, zeroth law, KMS ⟹ FDT and its four weights | 6 |

Two *joins* connect the rows. The ledger's hidden ports are exactly where the heat lives: **noise is temperature times the squared defect of the dilation** (§7). And the ledger's symmetries decide what the port can change: **a port can only flip what it can supply a charge for, and can only dephase what it can read** (§8).

### 1.2 What is new, and what is not

Nearly every ingredient is owned, and the paper credits it where it is used: dispersion relations (Kramers, Kronig, Titchmarsh); passivity implies causality (Youla–Castriota–Carlin 1959; Zemanian 1965); unitary dilation (Halmos 1950; Egerváry 1954; Sz.-Nagy–Foias; Stinespring 1955; Naimark 1940; the purification postulate of Chiribella–D'Ariano–Perinotti 2010); complete passivity ⟺ KMS (Pusz–Woronowicz 1978; Lenard 1978); the FDT family (Einstein 1905; Nyquist 1928; Callen–Welton 1951; Kubo 1957); the Petz family of quantum Fisher metrics from linear response (Shitara–Ueda 2016; Hauke et al. 2016); dissipativity-based thermodynamics (Willems 1972; Haddad 2019; van der Schaft 2021); compositional passive networks (Baez–Fong 2018); noise-wave theory (Twiss 1955; Bosma 1967); the amplifier bound (Haus–Mullen 1962; Caves 1982); noiseless subsystems (Zanardi–Rasetti 1997; Knill–Laflamme–Viola 2000).

What this paper adds is: (i) the **organizing theorem** — the three quantifiers of one inequality, with self-contained finite proofs in one place (Theorems 4.1, 5.2, 6.2); (ii) **causal parity** made explicit as an exact equal-energy law with an instantaneous-part excess, usable as a one-number dispersion test (Theorem 4.4); (iii) the **finite-horizon reading of dilation** as a quantitative "for all practical purposes" (Corollary 5.4); (iv) the **four-weight table** read as watching versus pushing (Theorem 6.4); (v) the **noise–defect formula** stated for passive and active ports at once, with the rotation/boost dichotomy (Theorem 7.2); (vi) the **port–charge table** (Theorem 8.2); (vii) the **modeling calculus** and the list of one-line answers (§§10, 12). None of these is deep in isolation. The claim of the paper is the unification, and we try to make that claim measurable (§14).

### 1.3 Claim tiers

**[P]** proven here (finite, exact) or a cited theorem used as stated. **[A]** a standard physical argument or an identification that is structural rather than proven here. **[C]** a conjectural reading, fenced, with no evidentiary weight. Every [P] result is backed by an exact-arithmetic certificate (Appendix A).

---

## 2. What is a port

### 2.1 For any reader

A **port** is a boundary through which a system exchanges something with the rest of the world and at which that exchange can be both driven and observed. A wall socket, an eardrum, a cell membrane, a telescope aperture, a strain gauge, an API endpoint, a black-hole horizon — each is a port. A port is *not* an observer: any subsystem boundary is a port, whether or not anyone is looking.

Every port carries a pair of conjugate variables, an **effort** and a **flow**, whose product is a power. This is the bond-graph observation of Paynter (1961), which engineers have long used to model mixed-domain systems with one formalism:

| Domain | Effort $e$ | Flow $f$ | Stores | Dissipates |
|---|---|---|---|---|
| Electrical | voltage | current | capacitor, inductor | resistor |
| Mechanical (translation) | force | velocity | spring, mass | damper |
| Mechanical (rotation) | torque | angular velocity | torsion spring, inertia | friction |
| Hydraulic | pressure | volume flow | tank, fluid inertia | constriction |
| Thermal | temperature | entropy flow | heat capacity | thermal resistance |
| Chemical | chemical potential | molar flow | concentration | reaction |
| Stochastic / information | affinity $\ln\frac{\pi_i T_{ij}}{\pi_j T_{ji}}$ | probability current $J_{ij}$ | — | entropy production |
| Any conserved charge $Q_k$ | its chemical potential $\mu_k$ | its current | — | — |

The information row is Schnakenberg's (1976): the entropy production of a Markov process is $\sum J_{ij}A_{ij}$, flux times affinity. The last row anticipates §8: every conserved Noether charge adds its own effort–flow pair.

### 2.2 Formal definitions

**Definition 2.1 (linear port, discrete time).** A linear port on the time grid $\{0,\dots,n-1\}$ is a real matrix $K$ mapping input sequences $u$ to output sequences $y=Ku$, with $u_s y_s$ the power delivered at step $s$. The energy absorbed up to instant $t$ is $\mathcal E_t(u)=\sum_{s\le t}u_s y_s$. The port is *passive at every instant* if $\mathcal E_t(u)\ge0$ for all $u$ and all $t$, and *net passive* if $\mathcal E_{n-1}(u)\ge0$ for all $u$.

**Definition 2.2 (scattering port).** A scattering port maps incoming wave amplitudes $a$ to outgoing ones $b=Sa$. It is *passive* if $\|Sa\|\le\|a\|$ for all $a$, that is, if $S$ is a contraction.

**Definition 2.3 (quantum port).** A quantum port is a triple $(\mathcal H_S, \{S_k\}, \rho)$: a system Hilbert space, the system operators through which it couples to its environment ($H_{\rm int}=\sum_k S_k\otimes B_k$), and a reference state. A state $\rho$ is *passive* for Hamiltonian $H$ if $\operatorname{tr}(U\rho U^\dagger H)\ge\operatorname{tr}(\rho H)$ for every unitary $U$ (no cyclic process extracts work), and *completely passive* if $\rho^{\otimes n}$ is passive for $H_n=\sum_{k=1}^n H^{(k)}$ for every $n$.

### 2.3 The watch–push pair

At every port there are two canonical experiments. *Watching* measures the symmetrized correlation $C_{AB}(t)=\tfrac12\langle\{A(t),B\}\rangle$. *Pushing* measures the response $\chi_{AB}(t)=\tfrac{i}{\hbar}\theta(t)\langle[A(t),B]\rangle$ (Kubo). The anticommutator is the symmetric half of the complex correlation $\langle A(t)B\rangle$ and the commutator is the antisymmetric half. The rest of the paper is about what locks the two halves together.

---

## 3. The principle and its derivation tree

**Port Principle.** *Every reference state of a port is passive.*

The three quantifiers give three roots, and everything else is a corollary:

```
                         NO PORT GIVES MORE THAN IT TAKES
          ┌───────────────────────┼───────────────────────────┐
   every instant            every input                  every copy
   (Thm 4.1)                (Thm 5.1-5.3)                (Thm 6.2)
      │                         │                            │
   causality              lossless ledger               temperature
      │                  (dilation, Naimark,          (zeroth law, KMS)
   Kramers–Kronig          Stinespring)                      │
   causal parity (4.4)          │                          FDT: four weights
   "no resistance        finite ledger ⇒ echo (5.4)     coth, 1/x, tanh, x (6.4)
    without reactance"   "no loss without a ledger"     "no dissipation without
      │                         │                          fluctuation"
      └──────────── JOIN 1: noise = T × (dilation defect)² (§7) ─────┘
                    Kirchhoff · Johnson–Nyquist · Caves · kT ln 2
                    "no gain without noise" · "no record without heat"
                                │
                    JOIN 2: port × Noether charge (§8)
                    supply / read table: memory · QND · control · thermalization
                                │
          away from equilibrium (§9): arrow = gap between watching and pushing
          modeling calculus (§10): interconnect · reduce · dilate · assign noise
```

The five **prohibitions** that fall out are the teachable form of the principle:

1. **No resistance without reactance** (causality; §4). A prism works because glass absorbs ultraviolet.
2. **No loss without a ledger** (dilation; §5). A finite room echoes; only an unbounded environment forgets.
3. **No dissipation without fluctuation** (FDT; §6). A resistor hisses in proportion to its resistance.
4. **No gain without noise** (Caves; §7). An amplifier hisses in proportion to its gain.
5. **No record without heat** (Landauer; §7). Every durable bit costs at least $k_BT\ln 2$ at the port where it is written.

---

## 4. Every instant: causality and dispersion

**Theorem 4.1 (instantaneous passivity forces causality) [P].** A linear port $K$ (Definition 2.1) that is passive at every instant is causal: $K_{ij}=0$ whenever $j>i$. Conversely, a causal $K$ is passive at every instant if and only if the symmetric part of every leading principal block $K_{[0..t]}$ is positive semidefinite.

*Proof.* Suppose $K_{ij}\neq0$ with $j>i$. Take $u=e_i+\lambda e_j$ and truncate at $t=i$. Only $s=i$ contributes, and $(Ku)_i=K_{ii}+\lambda K_{ij}$, so $\mathcal E_i(u)=K_{ii}+\lambda K_{ij}$. Choosing $\lambda=-(K_{ii}+1)/K_{ij}$ gives $\mathcal E_i(u)=-1<0$. For the converse, if $K$ is lower triangular then $y_s$ depends only on $u_{\le s}$, so $\mathcal E_t(u)=u_{[0..t]}^{\mathsf T}K_{[0..t]}u_{[0..t]}$, whose sign is set by the symmetric part of the block. $\square$

**Remark 4.2 (net passivity permits precognition) [P].** The "every instant" clause carries the causal content. The symmetric positive-definite $K=\begin{psmallmatrix}2&1&0\\1&2&1\\0&1&2\end{psmallmatrix}$ is net passive, but it is anticausal ($y_0$ depends on $u_1$), and $u=(1,-3,0)$ gives $\mathcal E_0=-1$. A system that is passive only on the total can borrow energy from the future and repay it later. Demanding passivity at every instant forbids the loan, and the arrow of time enters the theory exactly here. The continuum statement — a linear, time-invariant operator that is passive at every instant is causal and has a positive-real (Herglotz) transfer function — is due to Youla, Castriota, and Carlin (1959) and Zemanian (1965); see Srivastava (2021) for a modern review.

**Theorem 4.3 (dispersion) [P, cited].** A causal response $\chi(t)$ with finite energy has a Fourier transform analytic in the upper half-plane, and its real and imaginary parts are Hilbert-transform pairs (Kramers–Kronig; Titchmarsh 1937).

**Theorem 4.4 (causal parity) [P].** *(Finite grid.)* Let $K$ be lower triangular with diagonal $D$, and let $S=\tfrac12(K+K^{\mathsf T})$ and $A=\tfrac12(K-K^{\mathsf T})$. Then
$$\|S\|_F^2-\|A\|_F^2=\|D\|_F^2 ,$$
and in particular $\|S\|_F=\|A\|_F$ when $K$ is strictly causal. *(Continuum.)* For a real causal $f\in L^2$, $\;\int(\operatorname{Re}\hat f)^2d\omega=\int(\operatorname{Im}\hat f)^2d\omega=\pi\int_0^\infty f^2dt$.

*Proof.* For $i>j$, $S_{ij}=S_{ji}=A_{ij}=-A_{ji}=K_{ij}/2$, so the pair $\{ij,ji\}$ contributes $K_{ij}^2/2$ to each norm. The diagonal contributes $K_{ii}^2$ to $\|S\|^2$ and nothing to $\|A\|^2$. In the continuum, a causal $f$ has even part $f(|t|)/2$ and odd part $\operatorname{sgn}(t)f(|t|)/2$, which have equal norms. Their transforms are $\operatorname{Re}\hat f$ and $i\operatorname{Im}\hat f$, and Plancherel finishes. $\square$

*Reading.* In a causal response, the in-phase (reactive) and quadrature (resistive) parts carry **exactly equal energy**. The only escape is an instantaneous response (the diagonal) — the ideal resistor — which requires infinite bandwidth and does not exist. This is Prohibition 1 made quantitative. It also gives a **one-number dispersion test** for measured spectra: after subtracting the instantaneous part, the ratio $\|\operatorname{Re}\chi\|_2/\|\operatorname{Im}\chi\|_2$ must equal 1. It is a global companion to the Kramers–Kronig compliance tests used in impedance spectroscopy, and like them it requires adequate bandwidth coverage [A].

*Example (optics).* The refractive index $n(\omega)=n'+in''$ of glass is causal. Its strong ultraviolet absorption $n''$ forces, through dispersion, the frequency dependence of $n'$ in the visible. That is why a prism separates colors.

*Example (the reactance comes back).* In a decaying mode coupled to a band (the Wigner–Weisskopf model of §5), the decay rate $\Gamma$ (resistance) arrives with its dispersion partner, the Lamb shift (reactance). The derivative of the reactance then feeds back and renormalizes the decay itself (the residue $Z=1/(1-\operatorname{Re}\Sigma')$). Certificate P1.C4 measures the shift at 0.0306 against the Kramers–Kronig prediction 0.0303, and the decay curve matches $Z^2e^{-Z\Gamma t}$ to $2.8\times10^{-3}$, where ignoring $Z$ leaves a $4.3\%$ discrepancy. Ignoring reactance produces a measurable error even in a problem posed entirely in terms of loss.

---

## 5. Every input: the lossless ledger

**Theorem 5.1 (Halmos dilation) [P].** Let $T$ be a contraction on a finite-dimensional space, and let $D_T=(I-T^\dagger T)^{1/2}$ and $D_{T^\dagger}=(I-TT^\dagger)^{1/2}$. Then
$$U=\begin{pmatrix}T & D_{T^\dagger}\\ D_T & -T^\dagger\end{pmatrix}$$
is unitary.

*Proof.* Use the intertwining $TD_T=D_{T^\dagger}T$ (which holds because $Tf(T^\dagger T)=f(TT^\dagger)T$ for polynomials $f$, hence for the square root). Then $U^\dagger U=\begin{psmallmatrix}T^\dagger T+D_T^2 & T^\dagger D_{T^\dagger}-D_TT^\dagger\\ D_{T^\dagger}T-TD_T & D_{T^\dagger}^2+TT^\dagger\end{psmallmatrix}=I$. $\square$

Every lossy port is therefore the corner of a lossless one. The *defect operators* $D_T$ and $D_{T^\dagger}$ are the hidden ports through which the lost energy leaves and noise enters. §7 shows they carry the heat.

**Theorem 5.2 (finite horizon; Egerváry 1954) [P].** For a contraction $T$ on $\mathcal H$ and $N\ge1$, define $U_N$ on $\mathcal H^{N+1}$ by first block row $(T,0,\dots,0,D_{T^\dagger})$, second block row $(D_T,0,\dots,0,-T^\dagger)$, and identity blocks shifting the remaining components down one slot. Then $U_N$ is unitary and $P_{\mathcal H}U_N^kP_{\mathcal H}=T^k$ for $0\le k\le N$. In general the identity fails at $k=N+1$.

*Proof sketch.* Unitarity is Theorem 5.1 applied to the corner blocks, plus a permutation. Under iteration, the defect component created at step 1 is carried down the chain of identity blocks and re-enters the first slot only after $N$ steps, so the first $N$ compressed powers see pure $T$. Certificate P2.S2 verifies all of this exactly with a $15\times15$ rational orthogonal ledger and shows the failure at $k=N+1$. $\square$

**Theorem 5.3 (all time, all channels, all measurements) [P, cited].** Every contraction has a unitary power dilation on an infinite-dimensional space (Sz.-Nagy 1953), and a completely non-unitary contraction requires a bilateral shift, which is infinite. Every quantum channel is a unitary on system⊗environment followed by a partial trace (Stinespring 1955). Every generalized measurement (POVM) is a projective measurement on a larger space (Naimark 1940). In general probabilistic theories, the existence of such reversible realizations is equivalent to the purification principle (Chiribella–D'Ariano–Perinotti 2010).

**Corollary 5.4 (finite ledgers echo: a quantitative FAPP) [P].** A finite-dimensional ledger evolves almost periodically, $U(t)=\sum_k e^{-i\lambda_kt}P_k$, so for every $\varepsilon$ there are arbitrarily late times with $\|U(t)-I\|<\varepsilon$. No finite ledger realizes permanent loss. For a level coupled to $N$ equally spaced states of spacing $\delta$ (bandwidth $W=N\delta$), the decay $e^{-\Gamma t}$ with $\Gamma=2\pi g^2/\delta$ is reproduced — as a sum of pure rotations — up to the recurrence time
$$t_{\rm rec}=\frac{2\pi}{\delta}=\frac{2\pi N}{W},$$
at which the "lost" amplitude returns. Certificate P1.C4 ($N=801$, $\delta=0.025$) gives a revival probability of $0.55$ at $t_{\rm rec}=251$, compared with $e^{-\Gamma t_{\rm rec}}\approx2.5\times10^{-34}$ had the loss been permanent. *A record is durable only as long as the recurrence time of the channel into which its loss was exported.* Bell's complaint that decoherence explains records only "for all practical purposes" is thereby turned into a number: FAPP means "for all times short compared with $2\pi N/W$ of the receiving channel."

**Remark 5.5 (every motion is rotation, on the ledger).** By the spectral theorem, reversible (unitary) evolution is a superposition of pure rotations $e^{-i\lambda t}$. Damped motion is a spiral $e^{(-\gamma+i\omega)t}$ at the port, and by Theorems 5.1–5.3 it is the shadow of rotations on the ledger: decay is the dephasing of a continuum of rotations. Nonlinear conservative dynamics also decomposes into rotations on observables (Koopman). The caveat is non-normal dynamics ($[S,A]\neq0$ for the symmetric and antisymmetric parts of the generator), where the rotation basis is ill-conditioned and transient growth occurs that the eigenvalues do not show.

---

## 6. Every copy: temperature

**Lemma 6.1 (passivity) [P].** Let $H=\sum_iE_i|i\rangle\langle i|$. A state $\rho$ is passive if and only if $[\rho,H]=0$ and its eigenvalues are anti-ordered with energy ($E_i<E_j\Rightarrow p_i\ge p_j$). The *ergotropy* (maximal cyclically extractable work) is $\operatorname{tr}(\rho H)-\sum_ip_i^{\downarrow}E_i^{\uparrow}$.

*Proof.* The minimum of $\operatorname{tr}(\sigma H)$ over the unitary orbit of $\rho$ is attained when the largest eigenvalues sit on the lowest energies (the rearrangement inequality applied to the doubly stochastic matrix $|U_{ij}|^2$). $\square$

**Theorem 6.2 (complete passivity is temperature) [P].** A faithful state $\rho$ is completely passive if and only if $\rho=e^{-\beta H}/Z$ for some $\beta\ge0$.

*Proof.* (⇐) $\rho^{\otimes n}=e^{-\beta H_n}/Z^n$ is a non-increasing function of $H_n$. (⇒) Let $f_i=-\ln p_i$. Because $\rho^{\otimes n}$ is diagonal in the product eigenbasis, passivity of $\rho^{\otimes n}$ says: for multisets $\alpha,\alpha'$ of $n$ levels, $\sum_\alpha E<\sum_{\alpha'}E\Rightarrow\sum_\alpha f\le\sum_{\alpha'}f$. Take levels with gaps $g=E_j-E_i>0$ and $h=E_l-E_k>0$, and integers $a,b\ge1$ with $ag<bh$. The multisets $\alpha=\{j^a,k^b\}$ and $\alpha'=\{i^a,l^b\}$ give $a(f_j-f_i)\le b(f_l-f_k)$. Letting $a/b\uparrow h/g$ yields $(f_j-f_i)/g\le(f_l-f_k)/h$, and exchanging the roles gives equality. So the slope $(f_j-f_i)/(E_j-E_i)=\beta$ is the same for every pair. For a degenerate pair ($g=0$), $\alpha=\{j^a,k\}$ and $\alpha'=\{i^a,l\}$ give $a(f_j-f_i)\le f_l-f_k$ for every $a$, so $f_j\le f_i$, and by symmetry $f_j=f_i$. Hence $f=\beta E+c$, and $\beta\ge0$ by Lemma 6.1. $\square$

This is the finite-dimensional content of Pusz–Woronowicz (1978) and Lenard (1978). Passivity for a fixed number $k$ of copies ("$k$-passivity") is studied by Alicki and Fannes (2013).

**Corollary 6.3 (zeroth law) [P].** If two ports are jointly completely passive (for $H_A+H_B$), they are Gibbs at a common $\beta$. Two Gibbs ports at different temperatures are each completely passive but jointly active: a heat engine exists. Certificate P2.S3 exhibits both thresholds exactly. A passive, non-Gibbs state $p=(\tfrac12,\tfrac25,\tfrac1{10})$ on $E=(0,1,2)$ first becomes active at $n^*=3$ copies (ergotropy $39/1000$, witnessed by $(0,0,2)$ versus $(1,1,1)$). Two Gibbs ports at unequal temperatures first become jointly active at $n^*=3$ (ergotropy $4/243$). At equal temperature they remain passive through $n=5$. The copy number $n^*$ is a finite, integer diagnostic of how far a state is from thermal.

**Theorem 6.4 (the four weights of the FDT) [P].** Let $\rho=e^{-\beta H}/Z$ and let $A$ be an observable. Define the dissipation spectrum $\chi''(\omega)=\pi\sum_{ij}(p_i-p_j)|A_{ij}|^2\delta(\omega-\omega_{ij})$ with $\omega_{ij}=E_j-E_i$ ($\hbar=1$), write $x=\beta\omega/2$, and let $\sigma_{\rm el}=\sum_{E_i=E_j}p_i|\delta A_{ij}|^2$ be the elastic part. Then:

| Quantity | Experiment | Spectral formula | Weight |
|---|---|---|---|
| symmetrized variance $\operatorname{Var}(A)$ | watch | $\sigma_{\rm el}+\frac1\pi\int_0^\infty\coth x\;\chi''\,d\omega$ | $\coth x$ |
| isothermal susceptibility $\times T$ | push | $\sigma_{\rm el}+\frac1\pi\int_0^\infty\frac1x\;\chi''\,d\omega$ | $1/x$ |
| SLD (Bures) Fisher information of $e^{-iA\theta}$ | watch (estimation) | $\frac4\pi\int_0^\infty\tanh x\;\chi''\,d\omega$ | $\tanh x$ |
| Kubo–Mori (BKM) Fisher information of $e^{-iA\theta}$ | push (thermodynamic) | $\frac4\pi\int_0^\infty x\;\chi''\,d\omega=\beta\langle[A,[H,A]]\rangle$ | $x$ |

Moreover $D(U\rho U^\dagger\|\rho)=\beta\,W$ for every unitary $U$, where $W=\operatorname{tr}(U\rho U^\dagger H)-\operatorname{tr}(\rho H)\ge0$.

*Proof.* Every entry is a sum over Bohr pairs. With $p_i/p_j=e^{\beta\omega_{ij}}$ one has $\frac{p_i+p_j}{p_i-p_j}=\coth x_{ij}$ and $\frac{p_i-p_j}{p_i+p_j}=\tanh x_{ij}$. The Kubo canonical correlation carries $\frac{p_i-p_j}{\beta\omega_{ij}}$, the SLD metric carries $\frac{2}{p_i+p_j}(p_i-p_j)^2$, and the Kubo–Mori metric carries $(p_i-p_j)(\ln p_i-\ln p_j)=\beta\omega_{ij}(p_i-p_j)$. Summing $(E_j-E_i)(p_i-p_j)|A_{ij}|^2$ gives the double commutator (the f-sum rule). For the last identity, $\ln\rho=-\beta H-\ln Z$ and $S(U\rho U^\dagger)=S(\rho)$. Certificate P1.C2 confirms every line independently — the Sylvester equation for the SLD, the Kubo–Mori integral formula, and finite-difference pushing — to $10^{-10}$ or better. $\square$

*Reading.* One dissipation spectrum and four weights. Watching carries the $\coth/\tanh$ pair (the symmetric, anticommutator side) and pushing carries the $1/x,\,x$ pair (the canonical, commutator side). Since $\coth x\ge1/x$ and $\tanh x\le x$, one always has $\operatorname{Var}\ge T\chi$ and $F_{\rm Bures}\le F_{\rm KM}$, and all four weights coincide as $x\to0$ (classical physics, or commuting observables). Among the Petz monotone metrics, the Bures metric is the metric of watching and the Kubo–Mori metric is the metric of pushing, and the quantum FDT is the gap between them. The whole Petz family is recovered from linear response in Shitara–Ueda (2016), and the SLD entry is the Hauke et al. (2016) protocol for measuring entanglement by neutron scattering. The identity $D=\beta W$ is the second law in its sharpest form: rotating a thermal state always costs work, and the cost is temperature times relative entropy.

---

## 7. First join: noise is the defect of the dilation

**Theorem 7.1 (classical noise defect; Kirchhoff) [P].** Let $S$ be a passive scattering matrix whose hidden ports (the defect channels of Theorem 5.1) are thermal loads at temperature $\theta=k_BT$ (available noise power per unit bandwidth). If the incident waves have covariance $\Sigma_a$, the outgoing waves have covariance
$$\Sigma_b=S\Sigma_aS^\dagger+\theta\,(I-SS^\dagger).$$
In particular: (i) a port at uniform temperature leaves thermal radiation unchanged ($\Sigma_a=\theta I\Rightarrow\Sigma_b=\theta I$); (ii) the emissivity of port $i$, $e_i=(I-SS^\dagger)_{ii}$, equals its absorptivity $a_i=(I-S^\dagger S)_{ii}$ whenever $S$ is reciprocal ($S=S^{\mathsf T}$); (iii) for non-reciprocal $S$ the per-port equality can fail while $\sum_ie_i=\sum_ia_i$ still holds.

*Proof.* Read the output off the first block row of the Halmos ledger, $b=Sa+D_{S^\dagger}c$, with independent hidden inputs $c$ of covariance $\theta I$, and use $D_{S^\dagger}^2=I-SS^\dagger$. Part (i) is $S\theta S^\dagger+\theta(I-SS^\dagger)=\theta I$. Part (ii) follows because reciprocity makes row norms equal column norms, and (iii) is the trace identity $\operatorname{tr}SS^\dagger=\operatorname{tr}S^\dagger S$. Certificate P3.N1 verifies all three exactly, including a non-reciprocal instance with $e\neq a$ port by port and equal totals. $\square$

*Reading.* The noise a port emits is its temperature times its **squared defect** — the amount by which it fails to be lossless. This is Bosma's (1967) noise-wave theorem and Twiss's (1955) theorem, and it is Kirchhoff's law of thermal radiation (1860) in matrix form. Part (iii) is the recently observed breakdown of Kirchhoff's law in non-reciprocal (magneto-optical) emitters (Zhu–Fan 2014; Shayegan et al. 2023). The breakdown is per port only, and the second law is untouched, exactly as the matrix law requires. The culprit is the antisymmetric (Onsager–Casimir, gyrator) part of the response.

**Theorem 7.2 (quantum noise defect: passive and active ports in one formula) [P].** For a phase-insensitive single-mode bosonic channel acting on quadrature variances as $V_{\rm out}=\tau V_{\rm in}+N$:

1. The channel is completely positive iff $N\ge\frac{|1-\tau|}{2}$ (the CP matrix has eigenvalues $N\pm\frac{1-\tau}{2}$; Holevo–Werner 2001).
2. For $\tau\le1$ the channel is dilated by a beam splitter — a **rotation** of the pair (signal, hidden mode). For $\tau\ge1$ it is dilated by a two-mode squeezer — a **boost** of the pair (signal, idler). With the hidden mode at thermal occupation $n$, both dilations give
$$N=|1-\tau|\left(n+\tfrac12\right),\qquad n+\tfrac12=\tfrac12\coth\frac{\hbar\omega}{2k_BT}.$$
3. At $n=0$ the bound in (1) is saturated. For $\tau>1$ this is Caves's theorem (no gain without noise); for $\tau<1$ it is the vacuum noise of loss. As $\hbar\omega\ll k_BT$, $N\to|1-\tau|\,k_BT/\hbar\omega$, which is Theorem 7.1 per mode.

*Proof.* (1) is the Holevo–Werner CP condition, checked symbolically. (2) follows from the Heisenberg maps $b=\sqrt\tau a+\sqrt{1-\tau}\,c$ and $b=\sqrt\tau a+\sqrt{\tau-1}\,c^\dagger$, whose commutator bookkeeping $[b,b^\dagger]=1$ forces the hidden term, together with $V_c=n+\frac12$. (3) is substitution and a limit. Certificate P3.N2. $\square$

*Reading.* Passive ports dilate into **compact** symmetries (rotations, $SU(2)$) and active ports into **hyperbolic** ones (boosts, $SU(1,1)$). In both cases the added noise is the size of the non-unitarity, $|1-\tau|$, times the occupation of the hidden port. The factor $\coth$ is the same $\coth x$ that weights the watched variance in Theorem 6.4, so Prohibitions 3 and 4 are one prohibition read on either side of $\tau=1$. Only a lossless, gainless port ($\tau=1$) can be noiseless.

**Theorem 7.3 (noise is local; Levin's direct approach) [P].** Consider a linear mechanical (or electrical) network $M\ddot x+C\dot x+Kx=f+\xi$ with symmetric $M,K\succ0$ and $C\succeq0$, where each lossy element carries its own thermal force noise with one-sided spectrum $4k_BTC$ (the FDT applied locally). For any readout $y=p^{\mathsf T}x$, the readout noise spectrum is
$$S_y(\omega)=4k_BT\,p^{\mathsf T}GC\bar Gp=\frac{4k_BT}{\omega}\big|\operatorname{Im}\chi_{pp}(\omega)\big|=\frac{8k_BT\,W_{\rm diss}(\omega)}{\omega^2F_0^2},$$
where $G=(K-\omega^2M+i\omega C)^{-1}$, $\chi_{pp}=p^{\mathsf T}Gp$, and $W_{\rm diss}$ is the mean power dissipated when the system is pushed with force $F_0\cos\omega t$ distributed with the readout's own profile $p$.

*Proof.* $G^{-1}-\bar G^{-1}=2i\omega C$ gives $G-\bar G=-2i\omega\,GC\bar G$ (using $G=G^{\mathsf T}$), so $-\operatorname{Im}\chi_{pp}=\omega\,p^{\mathsf T}GC\bar Gp$. The dissipated power under the push is $\tfrac12\omega^2F_0^2\,p^{\mathsf T}\bar GCGp$. Certificate P3.N6 checks this exactly at three frequencies. $\square$

*Reading.* Noise modeling is **local and compositional**. Assign FDT noise to each loss and the correct noise appears at every port, for every readout. Conversely, to predict what a readout will *watch*, *push* with the readout's own shape and compute the loss. This is how LIGO's mirror thermal noise is computed (Saulson 1990; Levin 1998), and the principle says the same recipe applies in every row of the effort–flow table.

**Proposition 7.4 (the price of a bit) [P].** Transmitting information through a port whose noise is thermal, $N_0=k_BT$ (Johnson–Nyquist available power per hertz), costs at least
$$E_b\ \ge\ \lim_{W\to\infty}\frac{P}{C(W)}=N_0\ln2=k_BT\ln2$$
per bit, where $C(W)=W\log_2\!\big(1+\tfrac{P}{N_0W}\big)$ is Shannon's capacity (exact limit: certificate P2.S4). Erasing a bit into a thermal bath costs at least the same, $Q\ge k_BT\ln2$ (Landauer 1961). The proof in its sharpest form is bath passivity: $\beta Q=\Delta S_{\rm sys}+I'(S{:}B)+D(\rho_B'\|\gamma_B)\ge\Delta S_{\rm sys}$ (Esposito–Lindenberg–Van den Broeck 2010; Reeb–Wolf 2014). This is Prohibition 5: *no record without heat*. It is the same $k_BT$ in four places — Nyquist's noise, Shannon's floor, Landauer's erasure, and Theorem 7.1's defect — because in each case the heat enters or leaves through the same hidden ports.

---

## 8. Second join: ports and Noether charges

Symmetries give conserved charges, and conserved charges split the state space into sectors. We ask what a port can do to those sectors.

**Setup.** Let $Q$ be a conserved charge of the system ($[H_S,Q]=0$) with integer or discrete spectrum, and let the port couple through $H_{\rm int}=\sum_kg_k\,S_k\otimes B_k$, where each coupling operator carries a definite charge, $[Q,S_k]=q_kS_k$, and the total charge $Q+Q_E$ is conserved. The port **supplies** $\Delta Q$ if some $S_k$ has $q_k=\Delta Q\neq0$. The port **reads** $Q$ if its neutral couplings ($q_k=0$) act as a non-constant function $S_k=f_k(Q)\otimes(\cdot)$ on the sectors.

**Theorem 8.1 (port selection rule) [P for (a),(c),(d); A for (b)].**

(a) *No supply, no flip — exactly.* If the port supplies no charge ($q_k=0$ for all $k$), then $Q$ is conserved by the full system–environment unitary. Sector populations are invariant for all times, all coupling strengths, and all environment states — not merely to leading order.

(b) *Supply requires the environment to hand over the charge.* To leading order, transitions from $q$ to $q+\Delta Q$ occur at rate $\Gamma_{\Delta Q}=\sum_{k:\,q_k=\Delta Q}|g_k|^2S_{B_k}(\omega)$, where $S_{B_k}$ is the environment's fluctuation spectrum in its $-\Delta Q$ charge sector. By KMS and the FDT, $S_B(\omega)=2\hbar\,[n(\omega)+1]\,\chi''_B(\omega)$, and detailed balance fixes the stationary ratio $p_{q+\Delta Q}/p_q=e^{-\beta(E_{q+\Delta Q}-E_q-\mu\Delta Q)}$ (a generalized Gibbs state; each charge carries its own effort $\mu$). If the environment's charge carriers are gapped by $\Delta$, a flip between degenerate sectors must consume a thermally pre-existing carrier, and the rate is suppressed by $e^{-\beta\Delta}$ — the quasiparticle-poisoning law of topological qubits.

(c) *Reading dephases, in proportion to distinguishability.* A neutral coupling that acts on sectors as $f(Q)$ leaves populations invariant and destroys the coherence between sectors $q$ and $q'$ at rate $\tfrac{\gamma}{2}\,|f(q)-f(q')|^2$. It dephases exactly the pairs of sectors it can tell apart, and no others.

(d) *What the port cannot touch, it cannot corrupt.* Information encoded in the commutant of the algebra generated by the port's couplings (a noiseless subsystem) is invariant (Zanardi–Rasetti 1997; Knill–Laflamme–Viola 2000).

*Proof.* (a) $[Q\otimes I,H_S+H_{\rm int}+H_E]=0$ when every $S_k$ commutes with $Q$. (c) and (d): the Lindblad generator with jump $f(Q)$ multiplies the $(q,q')$ coherence by $-\tfrac\gamma2|f(q)-f(q')|^2$ and annihilates population changes, and jumps acting only on a gauge factor leave the logical reduced state invariant. (b) is the Davies/golden-rule rate with KMS detailed balance; its exact finite skeleton — rates in ratio $e^{-\beta\Delta}$ and a stationary ratio equal to $e^{-\beta\Delta}$ — is certified. Certificate P3.N3 checks (a)–(d) exactly on a logical qubit carrying charge $Q\in\{0,1\}$ with a gauge qubit alongside, including $\Gamma_2=\Gamma_1/2+\Gamma_\phi$, with $T_1$ set by supply and $T_\phi$ set by reading. $\square$

**Theorem 8.2 (the port–charge table) [P structure, A examples].** The relation of a port to a conserved charge has four cases:

| | **does not read $Q$** | **reads $Q$** |
|---|---|---|
| **does not supply $\Delta Q$** | **protected memory** — noiseless subsystems, decoherence-free subspaces, topological qubits | **non-demolition measurement** — $Q$ can be watched forever without being changed (Braginsky–Vorontsov–Thorne 1980); dephasing = being measured; the pointer basis is what the port reads (einselection) |
| **supplies $\Delta Q$** | **control** — a coherent drive changes the charge without learning it | **thermalization** — both $T_1$ (supply) and $T_2$ (read); relaxation to the generalized Gibbs state |

*Reading.* One fact — how a port stands toward a Noether charge — organizes four things usually studied by different communities: memory, measurement, control, and heat. The popular statement that "symmetry-protected sectors cannot flip unless the environment can supply the Noether charge" is exactly the top row, left to right. The table adds the other half: **symmetry protects the bit, not the phase.** Any port that can *read* the charge dephases the sectors it distinguishes. Topological protection is the corner where the port can do neither, which requires (i) gapped charge carriers (Theorem 8.1b: lifetime $\propto e^{\beta\Delta}$) and (ii) local indistinguishability, meaning that no local coupling acts as a non-constant $f(Q)$ on the code space (Theorem 8.1c).

*Engineering design rule [A].* For a qubit encoded in charge sectors: $T_1$ is set by the **charged** sector of the environment's dissipation spectrum at the qubit frequency; $T_\phi$ is set by the **neutral** sector's low-frequency spectrum times $|f(q)-f(q')|^2$. Protection is bought by gapping the first and blinding the second. The same accounting applies to spin qubits (spin as the charge), superconducting charge qubits (Cooper-pair number), and Majorana qubits (fermion parity).

*Generalization [A].* Complete passivity relative to processes that conserve charges $Q_1,\dots,Q_m$ selects the generalized Gibbs state $e^{-\beta(H-\sum_k\mu_kQ_k)}$. Each conserved charge adds an effort–flow row, with effort $\mu_k$ and flow the charge current. For non-commuting charges this yields the non-Abelian thermal state (Guryanova et al. 2016; Yunger Halpern et al. 2016).

---

## 9. Away from equilibrium: the arrow is the gap between watching and pushing

At equilibrium, watching determines pushing. Away from equilibrium they separate, and the size of the separation is the heat.

**Theorem 9.1 (Harada–Sasa 2005) [P, cited; certified instance].** For Langevin dynamics with friction $\gamma$ and bath temperature $T$, the mean heat dissipation rate equals $\gamma\big\{\langle v\rangle^2+\int\frac{d\omega}{2\pi}\big[\tilde C_v(\omega)-2T\tilde R'_v(\omega)\big]\big\}$: the frequency-resolved violation of the FDT.

*Certified instance (P1.C3).* An overdamped particle in the harmonic potential $\tfrac k2|x|^2$ with a circulating force $kJx$ ($J$ skew) has a stationary density that is **exactly Gibbs**, $\Sigma=(T/k)I$. Any snapshot — any instrument that sees only the stationary distribution — reports equilibrium. Yet the FDT-violation integral equals the hidden heat $2kT\omega^2$ exactly ($1.5876=1.5876$), and it vanishes pointwise when $\omega=0$.

**Proposition 9.2 (when is a snapshot enough?) [P].** For a finite Markov process with transition matrix $T$ and stationary distribution $\pi$, the time-reversed process $\tilde T=D_\pi^{-1}T^{\mathsf T}D_\pi$ has the same stationary distribution. The two processes are distinguishable from pair statistics (a log) if and only if $T\neq\tilde T$ (detailed balance fails), and the entropy production rate is the Kullback–Leibler divergence between forward and reversed pair statistics (Schnakenberg 1976). *A snapshot is a sufficient summary exactly when there is no current; a log is necessary exactly when there is one.* (Any snapshot-based objective is blind to the antisymmetric part of $T$; see *Curvature and Current*, Murillo 2026.)

**Generalizations [P, cited].** Dissipation equals $k_BT$ times the relative entropy between forward and time-reversed path ensembles (Kawai–Parrondo–Van den Broeck 2007). The Jarzynski (1997) and Crooks (1999) fluctuation theorems are the nonlinear completion, and the linear FDT is their second-order expansion. Harada–Sasa has been used to measure the near-perfect efficiency of the F$_1$-ATPase motor (Toyabe et al. 2010).

*Reading.* The arrow of time is measurable as the gap between watching and pushing. For data science this is the physical answer to "when do observational data predict interventions?": exactly at equilibrium, and the gap is the dissipation (cf. Baldovin–Cecconi–Vulpiani 2020).

---

## 10. The modeling calculus

The principle is also a set of closure rules, and closure rules make modeling easier.

**Proposition 10.1 (closure) [P].**

1. *Interconnection.* A power-conserving interconnection of passive ports is passive. For port-Hamiltonian systems $\dot x=(J-R)Qx+Bu,\ y=B^{\mathsf T}Qx$ (energy balance $\dot H=-x^{\mathsf T}QRQx+y^{\mathsf T}u$), the feedback $u_1=-y_2,\ u_2=y_1$ yields $J_c$ skew and $R_c\succeq0$.
2. *Reduction.* A compression of a contraction is a contraction. For port-Hamiltonian systems, effort-constraint projection with $W=QV(V^{\mathsf T}QV)^{-1}$ preserves $J_r$ skew, $R_r\succeq0$, and $Q_r\succ0$, so the reduced model is passive (positive-real) (Polyuga–van der Schaft 2012; cf. PRIMA, Odabasioglu–Celik–Pileggi 1998).
3. *Dilation.* Every passive model can be simulated as a reversible system coupled to a bath (Theorems 5.1–5.3; Caldeira–Leggett).
4. *Noise assignment.* Local FDT at each loss implies the FDT at every port (Theorem 7.3).
5. *Stability.* The stored energy is a Lyapunov function, and a feedback loop of passive systems is stable (the passivity theorem; Zames 1966).

Certificate P3.N5 checks 1–2 exactly, including $\operatorname{Re}G(i\omega)\ge0$ for full and reduced models. Certificate P3.N6 checks 4.

**The workflow this licenses.** Specify two things: the reversible skeleton (the interconnection $J$ and the storage $Q$) and the losses (the dissipation $R$ with its temperatures). Everything else is then either *determined* — noise (Theorem 7.3), stationary states (Theorem 6.2), dispersion (Theorem 4.3) — or *checkable* by one inequality: whether a fitted black-box model is physical (positive-realness, causal parity), whether a reduced model is still physical (compression), whether an assembly is stable (interconnection). Four modeling tasks that are usually separate — dynamics, noise, stability, and thermodynamic consistency — become one. Industry already does fragments of this: circuit simulators attach $4k_BTR$ to each resistor, signal-integrity tools enforce passivity on fitted macromodels, and gravitational-wave detectors compute thermal noise from loss angles. The principle says the fragments are one method, valid in every row of the effort–flow table, including fluctuating hydrodynamics (Landau–Lifshitz), chemical reaction networks (the chemical Langevin equation), and, as a structural analogy, stochastic gradient descent (Yaida 2019).

---

## 11. Measurement through a port

**What the principle resolves [P/A].**

- *The cut.* Von Neumann's movable Heisenberg cut is the statement that partial traces compose, $\operatorname{tr}_{AB}=\operatorname{tr}_A\operatorname{tr}_B$. A port is a cut, defined without reference to observers.
- *Generalized measurements.* By Naimark, every POVM is a projective measurement on the ledger.
- *The pointer basis.* Pointer states are the eigenbasis of what the port *reads* (Theorem 8.2, read column).
- *Durability.* Records last as long as the recurrence time of the channel that received the loss (Corollary 5.4).
- *Cost.* Writing a durable record costs at least $k_BT\ln2$ per bit (Proposition 7.4).
- *Timestamps.* A reading of position is always a joint event of pointer and clock, and time itself can be defined relationally as correlation with a clock subsystem (Page–Wootters 1983).

**What it does not resolve [C, fenced].** Why *this* outcome occurs. The principle localizes the residue to a single indexical question — *which branch of the ledger is this port on?* — and gives the measure (Born; Gleason 1957) but not the pointer. We claim nothing further.

---

## 12. What the principle answers in one line

The pragmatic test of a principle is how many questions it turns into one-liners. Each answer below cites the section that makes it exact.

1. *Why does every absorbing material disperse light?* Causality forces resistance to come with reactance of equal energy (§4).
2. *How much does a resistor hiss?* $4k_BTR$ per hertz: the squared defect times the temperature (§7).
3. *Why must every amplifier add noise, and how much?* Gain is a boost dilation, and its idler contributes $(G-1)(n+\tfrac12)\ge(G-1)/2$ (§7).
4. *What is the least energy per bit?* $k_BT\ln2$, from Shannon and Nyquist or from Landauer — the same hidden ports (§7).
5. *How do I predict a sensor's thermal noise floor?* Push with the readout's own profile and compute the loss (§7, Levin).
6. *Why does temperature exist, and why is it shared?* Complete passivity forces Gibbs at one $\beta$ (§6).
7. *When does a symmetry protect a qubit, and against what?* Against flips when the environment cannot supply the charge; against dephasing only when no port can read it (§8).
8. *What can be monitored forever without disturbance?* Conserved charges (non-demolition measurement) (§8).
9. *Why is loss irreversible if physics is reversible?* Because the ledger that receives it is effectively infinite; finite ledgers echo (§5).
10. *How long does a record last?* About $2\pi N/W$ for the receiving channel (§5).
11. *When is a snapshot enough, and when do I need the log?* A snapshot suffices iff there is no current (§9).
12. *When do observational data predict interventions?* At equilibrium; the gap is the dissipation (§9).
13. *Is my fitted model physical?* Check passivity and causal parity (§§4, 10).
14. *Can I simplify my model without breaking its physics?* Yes, by compression; not by unconstrained fitting (§10).
15. *Can I measure entanglement by pushing?* Yes: the Bures Fisher information is a $\tanh$-weighted integral of the measured dissipation (§6).
16. *What does the choice of quantum Fisher metric mean physically?* Bures is watching; Kubo–Mori is pushing (§6).
17. *Can an emitter's emissivity differ from its absorptivity?* Per port, if it is non-reciprocal; never in total (§7).
18. *How efficient is a molecular motor?* Measure its FDT violation (§9).

---

## 13. Where the principle strains

**Gravity [P for the obstruction, A for the local statement].** Self-gravitating systems have negative heat capacity, and the Newtonian Hamiltonian is unbounded below, so no global passive state exists and the third quantifier fails globally. Locally the principle survives: the vacuum restricted to a Rindler wedge is KMS with respect to boosts (Bisognano–Wichmann 1975), which gives the Unruh temperature, and Jacobson (1995) derives the Einstein equations from $\delta Q=T\,dS$ applied to every local horizon. The honest statement is that gravity is where local passive ports fail to glue into a global passive state. We make no further claim. Whether gravity's port is reactive (able to entangle; the Bose et al. 2017 and Marletto–Vedral 2017 proposals) or purely resistive (only decohering; Oppenheim 2023, with its decoherence–diffusion trade-off, itself an FDT-type lock) is an open experimental question. We note, without leaning on it, the proposal that stochastic spacetime affects galactic dynamics (Oppenheim–Russo 2024) and its critique (Hertzberg–Loeb 2024).

**The origin of the arrow [fenced].** Passivity at every instant *selects* a direction of time, but the principle does not explain why reference states are passive, that is, why the universe began in low entropy (the past hypothesis). Misra–Prigogine–Courbage (1979) supply the converse of dilation (from unitary K-flows to Markov semigroups), and we take no side between that view and the dilation view.

**The ledger's ontology [fenced].** Theorems 5.1–5.3 assert that a lossless completion *exists*, not that it is physically real. That is a representation theorem, not metaphysics (Jaynes would insist on this, and we agree).

**Active matter [A].** Systems that appear non-passive — molecular motors, living cells, lasers — are passive relative to a larger port that includes their fuel. The principle predicts that every apparent activity has a hidden fuel port. A laser is a boost-dilated port (Theorem 7.2) whose noise obeys the active branch of the same formula.

**Beyond linear response.** The spectral calculus of §§4–7 is linear. The nonlinear extension is the fluctuation theorems (§9), which retain the principle but not the four-weight table.

---

## 14. Objections and replies

- *"This is textbook linear response."* The ingredients are textbook, and they are credited (§1.2). What is claimed is the organization: one inequality, three quantifiers, two joins. The claim is testable by Kitcher's (1981) criterion of explanatory unification, which counts argument patterns. The results derived here from the single pattern *(passivity) × (quantifier) → (transform of the port's spectral measure)* are: Kramers–Kronig, causal parity, Halmos/Egerváry/Stinespring/Naimark, the recurrence bound, Pusz–Woronowicz/Lenard, the zeroth law, the classical and quantum FDT, the Petz fork, $D=\beta W$, Kirchhoff/Bosma, Caves, Levin, Shannon–Nyquist–Landauer, the port–charge table, Harada–Sasa, and snapshot sufficiency. That is about seventeen patterns reduced to one.
- *"Dissipativity theory already derived thermodynamics"* (Willems, Haddad, van der Schaft). That work is classical and deterministic. The third quantifier (copies → temperature), the quantum dilations, the four weights, and the charge table are what the port view adds.
- *"Causality plus purification already reconstructs quantum theory and Landauer"* (Chiribella et al.). Two of our three quantifiers are their axioms, which we read as corroboration. We add temperature and the spectral calculus.
- *"'Port' is anthropocentric"* (Bell). A port is a subsystem plus its couplings; no observer is involved. "For all practical purposes" is made quantitative in Corollary 5.4.
- *"A principle that explains everything forbids nothing"* (Popper). It forbids five things (§3), and §15 lists the observations that would refute it.

---

## 15. Falsifiers

Each entry is a matched pair: an outcome that corroborates (K) and one that refutes (L).

1. **The root.** L: cyclic work extracted from a completely passive (thermal) reference state. That would refute everything. K: no such device exists.
2. **Collapse models.** If wavefunction collapse is a fundamental, non-dilatable loss, the principle requires its noise to carry matched dissipation at a finite temperature (as in dissipative CSL, Smirne–Bassi 2015). L: collapse-induced heating that never saturates. K: any detected collapse noise thermalizes.
3. **Amplifiers.** L: a phase-insensitive amplifier beating $N=(G-1)/2$. K: none has been built (Caves).
4. **Protection.** L: flips between symmetry sectors in an environment that provably cannot supply the charge (Theorem 8.1a is exact). K: observed lifetimes of protected qubits scale as $e^{\beta\Delta}$ with the carrier gap.
5. **Gravity.** L: gravitational decoherence without the diffusion that the decoherence–diffusion trade-off requires. K: either observed gravitational entanglement (a reactive port) or a trade-off-respecting stochastic signature.
6. **Causal parity.** L: a stationary spectrum that passes Kramers–Kronig compliance but has $\|\operatorname{Re}\chi-\chi_\infty\|_2\neq\|\operatorname{Im}\chi\|_2$ over adequate bandwidth. That would indicate an error in the theorem or in its preconditions.

The principle's empirical strength is inherited from the second law and from unitarity. Its own new risky content is modest, and we say so.

---

## 16. What is beautiful here, and what it is for

**Economy.** One inequality, three quantifiers, two joins, five prohibitions.

**Symmetry.** The same pairs keep reappearing: watching and pushing, $\coth$ and $1/x$, $\tanh$ and $x$, anticommutator and commutator, symmetric and antisymmetric, emission and absorption, rotation-dilated (passive) and boost-dilated (active) ports, supplying and reading a charge.

**Honesty about the unknown.** The principle states exactly where it strains: global gravity, the past hypothesis, single outcomes.

**For teaching.** One resistor gives Johnson–Nyquist, Kramers–Kronig, Shannon, and Landauer in a single lecture, and the effort–flow table lets every discipline enter from its own door.

**For research.** The principle ties together the Petz fork, noiseless subsystems, non-demolition measurement, and fluctuation theorems, and it gives a design rule for protected qubits.

**For engineering.** Four modeling tasks become one, with universal checks (passivity, causal parity) and universal recipes (put $k_BT$ on every loss; push with the readout's shape).

---

## Appendix A. Certificate suite

All certificates are in `empirical/port_principle/`. Decisions use exact rational or symbolic arithmetic wherever a vanishing or membership decision is made; floating point appears only in numerical witnesses (P1.C2–C4), whose tolerances are stated. Falsifiers were written into each file before its first run.

| File | Content | Result |
|---|---|---|
| `p1_four_locks.py` | C1 causal parity (exact rationals, continuum oscillator); C2 four weights, $D=\beta W$; C3 Gibbs density with hidden current, Harada–Sasa $=2kT\omega^2$; C4 decay from rotations, Lamb shift = KK partner, $Z$-renormalization, echo at $2\pi/\delta$ | 21/22. C4.a failed (4.3%) because the reactance's derivative renormalizes the decay; superseded by C4.a′ (0.28%). The failure is retained. |
| `p2_three_quantifiers.py` | S1 every-instant passivity ⟹ causality, net-passive precognition; S2 exact $15\times15$ Egerváry ledger, horizon sharp at $N+1$; S3 $n^*=3$ for the non-Gibbs state and for the two-temperature joint, equal-temperature joint passive; S4 $E_b/N_0\to\ln2$ | 10/10. An independent pairwise-inversion search reproduces both $n^*=3$ witnesses. |
| `p3_protection_noise_modeling.py` | N1 noise $=\theta(I-SS^\dagger)$, equilibrium invisibility, Kirchhoff per port iff reciprocal; N2 CP $\Leftrightarrow N\ge|1-\tau|/2$, unified $|1-\tau|(n+\tfrac12)$; N3 port–charge table; N5 port-Hamiltonian closure; N6 Levin locality | 17/17. N2.K2c first failed because the symbolic simplifier does not close $\coth$ identities (a checker artifact; true on rewrite and at a spot value); fixed, with the failure logged in the file. |

## Appendix B. Glossary across disciplines

| Here | Physics | Engineering | Information / data | Statistics / causality |
|---|---|---|---|---|
| port | open-system boundary, coupling | terminal pair, bond | interface, endpoint | unit exposed to intervention |
| watch | correlation, fluctuation spectrum | noise measurement | logs, traces | observational data |
| push | response function, susceptibility | transfer function, impedance | probe, query | intervention, do-operator |
| passivity | second law (Kelvin), complete passivity | positive-real, dissipativity | data-processing inequality | — |
| ledger (dilation) | purification, environment | lossless embedding + loads | event log (event sourcing) | full generative process |
| defect | loss channel | noise-wave source | lossy compression | unmeasured confounding |
| echo horizon | Poincaré recurrence | reverberation time | log retention window | — |
| charge | Noether charge | conserved quantity | invariant, checksum | — |

## References (content-level; to be formatted)

Alicki & Fannes 2013 (PRE 87, 042123); Baez & Fong 2018 (TAC 33, 1158); Baldovin, Cecconi & Vulpiani 2020 (PRR 2, 043436); Bisognano & Wichmann 1975; Bose et al. 2017 (PRL 119, 240401); Bosma 1967; Braginsky, Vorontsov & Thorne 1980 (Science 209, 547); Callen & Welton 1951; Caves 1982 (PRD 26, 1817); Chiribella, D'Ariano & Perinotti 2010 (PRA 81, 062348); Crooks 1999; Egerváry 1954; Einstein 1905; Esposito, Lindenberg & Van den Broeck 2010 (NJP 12, 013013); Gleason 1957; Guryanova et al. 2016 (Nat. Commun. 7, 12049); Haddad 2019 (Princeton); Halmos 1950; Harada & Sasa 2005 (PRL 95, 130602); Hauke et al. 2016 (Nat. Phys. 12, 778); Haus & Mullen 1962; Hertzberg & Loeb 2024 (arXiv:2404.13037); Holevo & Werner 2001 (PRA 63, 032312); Jacobson 1995 (PRL 75, 1260); Jarzynski 1997; Kawai, Parrondo & Van den Broeck 2007 (PRL 98, 080602); Kitcher 1981; Knill, Laflamme & Viola 2000 (PRL 84, 2525); Kubo 1957; Landauer 1961; Lenard 1978; Levin 1998 (PRD 57, 659); Marletto & Vedral 2017 (PRL 119, 240402); Misra, Prigogine & Courbage 1979; Naimark 1940; Nyquist 1928; Odabasioglu, Celik & Pileggi 1998; Oppenheim 2023 (PRX 13, 041040); Oppenheim & Russo 2024 (arXiv:2402.19459); Page & Wootters 1983; Paynter 1961; Polyuga & van der Schaft 2012; Pusz & Woronowicz 1978 (CMP 58, 273); Reeb & Wolf 2014 (NJP 16, 103011); Saulson 1990; Schnakenberg 1976; Shayegan et al. 2023 (Nat. Photon.); Shitara & Ueda 2016 (PRA 94, 062316); Smirne & Bassi 2015; Srivastava 2021 (arXiv:2008.05546); Stinespring 1955; Sz.-Nagy 1953; Titchmarsh 1937; Toyabe et al. 2010 (PRL 104, 198103); Twiss 1955; van der Schaft 2021 (arXiv:2010.04213); Willems 1972; Yaida 2019 (ICLR); Yunger Halpern et al. 2016 (Nat. Commun. 7, 12051); Zames 1966; Zanardi & Rasetti 1997; Zemanian 1965; Zhu & Fan 2014 (PRB 90, 220301).
