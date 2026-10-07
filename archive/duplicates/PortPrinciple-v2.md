<!--
================================================================================
INTERNAL LOG — NOT FOR PUBLICATION (Pandoc drops HTML comments)

  v1 (2026-09-29): spine. Backup: PortPrinciple-v1.md.
  v2 (2026-09-29): folds a critical-collaborative review. Dispositions:
    ACCEPTED, SHARPENED
      - Quantifier structure: v1's "three independent quantifiers" replaced by one
        base inequality (every input, wave form) + two lifts (every instant, every
        copy); every-instant => every-input, strictly (Prop 3.1).
      - Charges: accepted that they must enter; CORRECTED the form. They are not a
        fourth demand that "uniquely selects" the NATS. They restrict which cycles
        count, which ENLARGES the free family by one multiplier per charge (§7,
        Thms 7.1-7.2; cert R4.K4c).
      - Echo horizon: added the exact Wiener dichotomy (Thm 4.5).
      - Petz family: the watch/push reading is extended to the whole family as
        frequency filters with closed forms, including Wigner-Yanase-Dyson (Thm 6.5).
      - Active ports: boundary rule and pump theorem made explicit (Def 2.5, Prop 8.3).
      - Non-Abelian table: accepted, and derived via Schur (Thm 9.3).
      - Low-hanging fruit: three boundaries (§5); resource theories (§7);
        continuum fields (Thm 8.4); TUR, generalized into the coth law (Prop 6.7).
    REBUTTED, WITH REASON
      - "Causal parity fails for active media; restrict to passive." Wrong
        restriction. The theorem needs causal + finite energy (stability); gain is
        allowed (cert R2: a stable amplifier has zero defect). Upgraded to an exact
        defect formula for arbitrary kernels (Thm 5.4).
      - "Thm 6.2's proof skips degenerate spectra." v1 handled g = 0 explicitly. The
        question did lead us to a genuine v1 bug: H proportional to I (every state
        completely passive). Fixed; the proof is now a lattice argument (Thm 7.2
        with m = 0).
    Certificates: P1 21/22 (C4.a superseded, retained), P2 10/10, P3 17/17, P4 20/20.
================================================================================
-->

# The Port Principle: One Inequality Beneath Impedance, Fluctuation, Measurement, and Information

**Leonardo Murillo Montero**

---

## Abstract

Every measurement, model, and machine touches the world through a *port*: a boundary at which a system can be both pushed and watched. In wave variables, a port's power is incoming minus outgoing, and the Port Principle is a single inequality: *outgoing never exceeds incoming* — no port gives more than it takes. Demanded **for every input**, the inequality makes the port a contraction, and every contraction is the corner of a lossless ledger. Whether "lost" information ever returns is decided exactly by the ledger's spectral type (Wiener): pure point spectra echo, continuous spectra forget. Lifted to **every instant**, it forces causality. The resistive and reactive parts of a stable causal response then carry exactly equal energy, and for an arbitrary kernel the defect equals its overlap with its own time reverse — gain is allowed, and only instability or acausality registers. Lifted to **every number of copies**, it forces temperature and the zeroth law. A single dissipation spectrum then determines every variance and every quantum Fisher metric through frequency filters: $\coth x$ for watching, $1/x$ for pushing, $\tanh x$ for Bures, $x$ for Kubo–Mori, $2\tanh(x/2)$ for Wigner–Yanase, and a closed form for the whole Wigner–Yanase–Dyson family. Restricting which cycles count to those that conserve a set of charges adds one chemical potential per charge, giving generalized and non-Abelian Gibbs states. Two joins carry most of the practical weight. First, noise is temperature times the squared defect of the dilation, a statement independent of which dilation is used. It unifies Kirchhoff's radiation law, Johnson–Nyquist noise, and Caves's amplifier bound as $N=|1-\tau|(n+\tfrac12)$ for passive (rotation-dilated) and active (boost-dilated, pump-fed) ports. Second, a port's relation to a conserved Noether charge — can it supply it, can it read it — classifies protected memory, non-demolition measurement, control, and thermalization. For non-Abelian charges, Schur's lemma collapses the read-only cell onto the Casimirs: reading one component supplies its conjugates. An elementary *coth law* — symmetric fluctuation over antisymmetric response equals $\coth u$, where $u$ is half the log-ratio of forward to backward rates — shows that the quantum FDT inequality, the thermodynamic uncertainty relation, and the shot-to-Johnson noise crossover of a tunnel junction are one inequality, $u\coth u\ge1$. We give finite, exact proofs and a certificate suite, a definition of "port" usable from any discipline, a modeling calculus, about two dozen one-line answers, and an account of where the principle strains.

---

## 1. Watching and pushing

There are exactly two ways to learn about anything. You can **watch** it — record its fluctuations while leaving it alone — or you can **push** it — apply a small, known disturbance and record the response. A physicist watches Brownian motion and pushes with a force; an engineer watches the hiss of a resistor and pushes with a voltage; a statistician watches observational data and pushes with an intervention; a neuroscientist watches spontaneous activity and pushes with a stimulus.

The fluctuation–dissipation theorem (FDT) says that, at equilibrium, the two agree: watching determines pushing. This paper argues that the FDT is one face of a more primitive fact about the place where watching and pushing happen — the *port* — and that the same fact, read in a few precise ways, also yields causality, reversible completions of irreversible processes, temperature, chemical potentials, and the cost of noise, records, and precision. The primitive fact is Kelvin's inequality localized at a port:

> **Port Principle.** No port gives more than it takes.

### 1.1 One inequality, two lifts, one symmetry axis

In wave variables (Definition 2.2) the power into a port is $\|a\|^2-\|b\|^2$, incoming minus outgoing. The principle is $\|b\|\le\|a\|$. It can be demanded in the following ways:

| Demanded … | Mathematical form | Forces … | § |
|---|---|---|---|
| **for every input** (base) | $S$ is a contraction | a lossless ledger (dilation); Wiener's echo-or-forget dichotomy | 4 |
| **at every instant** (lift over time) | $\|P_tb\|\le\|P_ta\|$ for every truncation $P_t$ | causality; dispersion; parity defect = time-reflection overlap | 5 |
| **for every number of copies** (lift over tensor powers) | no work from $\rho^{\otimes n}$ for all $n$ | temperature; zeroth law; one spectrum, many filters (FDT, Petz family); the coth law | 6 |
| **only over cycles respecting a symmetry** (restriction of the admissible class) | passivity under charge-conserving unitaries | one chemical potential per conserved charge; GGE; non-Abelian thermal state | 7 |

The lifts strengthen the base (Proposition 3.1). The symmetry axis weakens the admissible class, and therefore *enlarges* the family of free states. Two joins connect the rows: the ledger's hidden ports carry the heat (**noise = temperature × squared dilation defect**, §8), and the ledger's symmetries decide what a port can change (**a port flips only what it can supply and dephases only what it can read**, §9).

### 1.2 What is new, and what is not

Nearly every ingredient is owned, and credited where used: dispersion relations (Kramers, Kronig, Titchmarsh); passivity implies causality (Youla–Castriota–Carlin 1959; Zemanian 1965); unitary dilation (Halmos 1950; Egerváry 1954; Sz.-Nagy–Foias; Stinespring 1955; Naimark 1940; purification, Chiribella–D'Ariano–Perinotti 2010); Wiener's theorem and RAGE; complete passivity ⟺ KMS (Pusz–Woronowicz 1978; Lenard 1978); the FDT family (Einstein 1905; Nyquist 1928; Callen–Welton 1951; Kubo 1957); the Petz family from linear response (Shitara–Ueda 2016; Hauke et al. 2016) and skew-information bounds (Luo 2004); generalized and non-Abelian thermal states (Guryanova et al. 2016; Yunger Halpern et al. 2016; Lostaglio–Jennings–Rudolph 2017); dissipativity-based thermodynamics (Willems 1972; Haddad 2019; van der Schaft 2021); compositional passive networks (Baez–Fong 2018); noise waves (Twiss 1955; Bosma 1967); the amplifier bound (Haus–Mullen 1962; Caves 1982); noiseless subsystems (Zanardi–Rasetti 1997; Knill–Laflamme–Viola 2000); the thermodynamic uncertainty relation (Barato–Seifert 2015; Gingrich et al. 2016) and the fluctuation–response inequality (Dechant–Sasa 2020).

This paper adds:
- (i) **the organizing structure**: one base inequality, two lifts, one symmetry axis, with self-contained finite proofs (Proposition 3.1; Theorems 5.1, 7.2);
- (ii) **the parity defect**: $\|\operatorname{Re}\hat f\|^2-\|\operatorname{Im}\hat f\|^2=2\pi\langle f,\mathcal Rf\rangle$ for arbitrary kernels, which makes causal parity a diagnostic of instability and acausality — not of gain (Theorem 5.4);
- (iii) **Wiener's dichotomy read as the echo-or-forget law of dilations**, with its finite-ledger quantification (Theorem 4.5, Corollary 4.6);
- (iv) **one spectrum, many filters**: closed-form frequency filters for every named Petz metric and for the Wigner–Yanase–Dyson family, with a single ordering chain (Theorem 6.5);
- (v) **the coth law** unifying the quantum FDT inequality, the TUR, and tunnel-junction noise (Proposition 6.7);
- (vi) **the charge-restricted converse** of complete passivity for commuting charges, by a lattice argument that also repairs an edge case (Theorem 7.2);
- (vii) **the noise-defect formula** for passive and active ports, with the pump made explicit and dilation-independence proved (Theorem 8.1, Proposition 8.3);
- (viii) **the port–charge table** and its non-Abelian collapse (Theorems 9.2, 9.3);
- (ix) **the modeling calculus**, the one-line answers, and the falsifiers (§§11, 13, 16).

None of these is deep in isolation. The claim of the paper is the unification, and §15 makes it measurable.

### 1.3 Claim tiers

**[P]** proven here (finite, exact) or a cited theorem used as stated. **[A]** a standard physical argument or a structural identification not proven here. **[C]** a conjectural reading, fenced, with no evidentiary weight. Every [P] result proven here has an exact-arithmetic certificate (Appendix A).

---

## 2. What is a port

### 2.1 For any reader

A **port** is a boundary through which a system exchanges something with the rest of the world, and at which that exchange can be both driven and observed. A wall socket, an eardrum, a cell membrane, a telescope aperture, a strain gauge, an API endpoint, a black-hole horizon — each is a port. A port is *not* an observer: any subsystem boundary is a port, whether or not anyone is looking.

Every port carries an **effort** and a **flow** whose product is a power (the bond-graph observation of Paynter, 1961):

| Domain | Effort | Flow | Stores | Dissipates |
|---|---|---|---|---|
| Electrical | voltage | current | capacitor, inductor | resistor |
| Mechanical (translation) | force | velocity | spring, mass | damper |
| Mechanical (rotation) | torque | angular velocity | torsion spring, inertia | friction |
| Hydraulic | pressure | volume flow | tank, fluid inertia | constriction |
| Thermal | temperature | entropy flow | heat capacity | thermal resistance |
| Chemical | chemical potential | molar flow | concentration | reaction |
| Stochastic / information | affinity $\ln\frac{\pi_iT_{ij}}{\pi_jT_{ji}}$ | probability current $J_{ij}$ | — | entropy production |
| Any conserved charge $Q_k$ | its chemical potential $\mu_k$ | its current | — | — |

The information row is Schnakenberg's (1976): entropy production is flux times affinity. The last row is made exact in §7: each conserved charge adds one effort–flow pair.

### 2.2 Formal definitions

**Definition 2.1 (linear port, discrete time).** A real matrix $K$ maps inputs $u$ to outputs $y=Ku$ on the grid $\{0,\dots,n-1\}$, and $u_sy_s$ is the power at step $s$. The energy absorbed up to instant $t$ is $\mathcal E_t(u)=\sum_{s\le t}u_sy_s$.

**Definition 2.2 (wave variables, scattering port).** Put $a=\tfrac12(u+y)$ (incoming) and $b=\tfrac12(y-u)$ (outgoing). Then
$$u_sy_s=a_s^2-b_s^2 ,$$
so absorbed energy is incoming minus outgoing. A scattering port is $b=Sa$. It is **passive for every input** if $\|Sa\|\le\|a\|$ for all $a$ (a contraction), and **passive at every instant** if $\|P_tSa\|\le\|P_ta\|$ for every truncation $P_t$ to times $\le t$.

**Proposition 2.3 (the two forms agree) [P].** $\mathcal E_t(u)\ge0$ for all $u$ is equivalent to $\|P_tb\|\le\|P_ta\|$, and net passivity ($\operatorname{sym}K\succeq0$) is equivalent to $S=(K-I)(K+I)^{-1}$ being a contraction (Cayley).

*Proof.* The power identity gives the first statement. For the second, $\|(K-I)x\|^2\le\|(K+I)x\|^2\iff\langle x,Kx\rangle\ge0$. Put $y=(K+I)x$, noting that $K+I$ is invertible because its symmetric part is $\succeq I$. Certificate P4.R1. $\square$

**Definition 2.4 (quantum port).** A triple $(\mathcal H_S,\{S_k\},\rho)$: a system, its coupling operators ($H_{\rm int}=\sum_kS_k\otimes B_k$), and a reference state. The state $\rho$ is **passive** for $H$ if $\operatorname{tr}(U\rho U^\dagger H)\ge\operatorname{tr}(\rho H)$ for all unitaries $U$, and **completely passive** if $\rho^{\otimes n}$ is passive for $H_n=\sum_kH^{(k)}$ for every $n$.

**Definition 2.5 (active port; boundary rule).** A port is **active** if its boundary contains a sub-port whose reference state is not passive (positive ergotropy): a charged battery, a coherent pump, an inverted medium, a fuel reservoir. *Boundary rule:* when a port shows gain, enlarge its boundary until the non-passive source is inside it. The principle applies to the enlarged, passive-overall boundary, and the principle's formulas then price the draw on the source (§8). The principle never asserts that an active port is passive.

### 2.3 The watch–push pair

*Watching* measures the symmetrized correlation $C_{AB}(t)=\tfrac12\langle\{A(t),B\}\rangle$. *Pushing* measures the response $\chi_{AB}(t)=\tfrac i\hbar\theta(t)\langle[A(t),B]\rangle$ (Kubo). They are the symmetric and antisymmetric halves of one complex correlation $\langle A(t)B\rangle$. Watching *adds* the two directions of every elementary process, and pushing *subtracts* them (Proposition 6.7).

---

## 3. The principle and its derivation tree

**Port Principle.** *Every reference state of a port is passive* ($\|b\|\le\|a\|$ in wave variables).

**Proposition 3.1 (nesting) [P].** Passivity at every instant implies passivity for every input (take $t$ = final time). The converse fails: a net-passive anticausal kernel violates instantaneous passivity (Remark 5.2). The lift over time is strictly stronger than the base.

```
                     NO PORT GIVES MORE THAN IT TAKES   (‖b‖ ≤ ‖a‖)
                                      │
      ┌────────────────────── base: every input ─────────────────────────┐
      │ contraction ⇒ lossless ledger (Halmos, Egerváry, Sz.-Nagy,      │
      │ Stinespring, Naimark) ⇒ Wiener: point spectrum echoes,          │
      │ continuous spectrum forgets                                     │
      └───────────────┬───────────────────────────────┬────────────────┘
          lift: every instant                  lift: every copy
          causality ⇒ Kramers–Kronig           temperature, zeroth law
          parity defect = ⟨f, Rf⟩              one spectrum, many filters
          (gain allowed; instability shows)    (FDT; Petz; WYD)  ·  coth law
                          │                               │
          symmetry axis: only charge-conserving cycles count
          ⇒ one chemical potential per charge (GGE; non-Abelian thermal state)
                          │                               │
          JOIN 1: noise = T × (dilation defect)²  (Kirchhoff · Nyquist · Caves · kT ln 2)
          JOIN 2: port × Noether charge  (supply / read;  non-Abelian: Schur)
                          │
          away from equilibrium: arrow = watch–push gap (Harada–Sasa, FRI, TUR)
          modeling calculus: interconnect · reduce · dilate · assign noise
```

The teachable form is six **prohibitions**:

1. **No resistance without reactance** (causality + stability; §5). A prism works because glass absorbs ultraviolet.
2. **No loss without a ledger** (dilation; §4). A finite room echoes; only a continuous spectrum forgets.
3. **No dissipation without fluctuation** (FDT; §6). A resistor hisses in proportion to its resistance.
4. **No gain without noise, and no gain without a source** (§8). An amplifier hisses in proportion to its gain and draws on a non-passive pump.
5. **No record without heat** (Landauer; §8). A durable bit costs at least $k_BT\ln2$.
6. **No precision without dissipation** (TUR, via the coth law; §6). A steady current's relative variance times its entropy production is at least $2k_B$.

---

## 4. Every input: the lossless ledger

**Theorem 4.1 (Halmos dilation) [P].** For a contraction $T$ on a finite-dimensional space, with $D_T=(I-T^\dagger T)^{1/2}$ and $D_{T^\dagger}=(I-TT^\dagger)^{1/2}$,
$$U=\begin{pmatrix}T&D_{T^\dagger}\\D_T&-T^\dagger\end{pmatrix}$$
is unitary.

*Proof.* The intertwining $TD_T=D_{T^\dagger}T$ holds because $Tf(T^\dagger T)=f(TT^\dagger)T$ for polynomials $f$, hence for the square root. Expanding $U^\dagger U$ gives $I$. $\square$

**Theorem 4.2 (finite horizon; Egerváry 1954) [P].** For $N\ge1$, the operator $U_N$ on $\mathcal H^{N+1}$ is defined by first block row $(T,0,\dots,0,D_{T^\dagger})$, second block row $(D_T,0,\dots,0,-T^\dagger)$, and identity blocks shifting the remaining components down. It is unitary, and $P_{\mathcal H}U_N^kP_{\mathcal H}=T^k$ for $0\le k\le N$. In general the identity fails at $k=N+1$.

*Proof.* $U_N$ is the Halmos unitary on the first and last slots composed with a shift of the middle slots. A defect component created at step 1 travels down the chain and re-enters the first slot only after $N$ steps. Certificate P2.S2 gives an exact $15\times15$ rational instance with failure at $k=N+1$. $\square$

**Theorem 4.3 (all time, all channels, all measurements) [P, cited].** Every contraction has a unitary power dilation, and a completely non-unitary contraction requires an infinite bilateral shift (Sz.-Nagy 1953). Every quantum channel is a unitary on system⊗environment followed by a partial trace (Stinespring 1955). Every POVM is a projective measurement on a larger space (Naimark 1940). In general probabilistic theories, such reversible realizations exist iff the purification principle holds (Chiribella–D'Ariano–Perinotti 2010).

**Proposition 4.4 (the defect does not depend on the ledger) [P].** If $\begin{psmallmatrix}S&B\\C&D\end{psmallmatrix}$ is *any* unitary completion of $S$, then $BB^\dagger=I-SS^\dagger$ and $C^\dagger C=I-S^\dagger S$.

*Proof.* These are the top-left blocks of $UU^\dagger=I$ and $U^\dagger U=I$. Certificate P4.R10 exhibits two different exact ledgers with the same corner and identical defect Gram. $\square$

Every quantity in §8 is built from these Gram matrices, so the noise predictions do not depend on which ledger one imagines.

**Theorem 4.5 (echo or forget: Wiener's dichotomy) [P, cited; finite form certified].** Let $\psi$ be the port vector on the ledger, $H$ the ledger's generator, and $\mu_\psi$ the spectral measure of $\psi$. The return amplitude is $a(t)=\langle\psi,e^{-iHt}\psi\rangle=\int e^{-i\lambda t}d\mu_\psi(\lambda)$.

1. (Wiener) $\displaystyle\lim_{T\to\infty}\frac1T\int_0^T|a(t)|^2dt=\sum_\lambda\mu_\psi(\{\lambda\})^2$.
2. If $\mu_\psi$ is pure point, $a$ is almost periodic, and $|a(t)|$ returns within any $\varepsilon$ of 1 on a relatively dense set of times: the port echoes.
3. If $\mu_\psi$ is continuous, the time-averaged return is zero. If it is absolutely continuous, $a(t)\to0$ pointwise (Riemann–Lebesgue): the port forgets.

*Proof.* (1) is Wiener's theorem. (2) is Bohr almost-periodicity. (3) follows from (1) and the Riemann–Lebesgue lemma. The finite-ledger identity in (1) is checked exactly in certificate P4.R3. $\square$

**Corollary 4.6 (how finite ledgers approximate forgetting) [P + witness].** Every physical environment of finite extent has a pure point spectrum, so the forgetting in Theorem 4.5(3) is an idealization. Its finite-size corrections are quantified as follows. For a level coupled to $N$ equally spaced states (spacing $\delta$, bandwidth $W=N\delta$), the decay $e^{-\Gamma t}$ with $\Gamma=2\pi g^2/\delta$ is reproduced — as a sum of pure rotations — until
$$t_{\rm rec}=\frac{2\pi}{\delta}=\frac{2\pi N}{W},$$
and the time-averaged echo is $\sum_k w_k^2\approx\delta/(\pi\Gamma)\to0$ as $\delta\to0$. In certificate P1.C4 ($N=801$), the revival probability at $t_{\rm rec}=251$ is $0.55$, against $2.5\times10^{-34}$ had the loss been permanent. In certificate P4.R3 the average echo is $\sum w_k^2=0.0252$, against a predicted $0.0259$. *A record is durable only as long as the receiving channel's recurrence time.* Bell's "for all practical purposes" is thus given a number, and the continuum limit of Theorem 4.5 is what turns the number into "forever".

**Remark 4.7 (every motion is rotation, on the ledger).** Unitary evolution is a superposition of pure rotations $e^{-i\lambda t}$. A damped spiral at the port is the shadow of rotations on the ledger: decay is the dephasing of a continuum of rotations. Nonlinear conservative dynamics also decomposes into rotations on observables (Koopman). The caveat is non-normal dynamics, where the rotation basis is ill-conditioned and transient growth occurs that the eigenvalues do not show.

---

## 5. Every instant: causality and dispersion

**Theorem 5.1 (instantaneous passivity forces causality) [P].** If a linear port $K$ is passive at every instant, then $K_{ij}=0$ for $j>i$. Conversely, a causal $K$ is passive at every instant iff the symmetric part of every leading block $K_{[0..t]}$ is positive semidefinite.

*Proof.* Suppose $K_{ij}\neq0$ with $j>i$. Take $u=e_i+\lambda e_j$ and truncate at $t=i$: then $\mathcal E_i(u)=K_{ii}+\lambda K_{ij}$, which equals $-1$ for $\lambda=-(K_{ii}+1)/K_{ij}$. For the converse, causality gives $\mathcal E_t(u)=u_{[0..t]}^{\mathsf T}K_{[0..t]}u_{[0..t]}$. Certificate P2.S1. $\square$

**Remark 5.2 (net passivity permits precognition) [P].** $K=\begin{psmallmatrix}2&1&0\\1&2&1\\0&1&2\end{psmallmatrix}$ is net passive, but $u=(1,-3,0)$ gives $\mathcal E_0=-1$: this port borrows energy from the future. The arrow of time enters the theory exactly at the lift from "every input" to "every instant". The continuum statement (a linear, time-invariant operator passive at every instant is causal, with a positive-real transfer function) is due to Youla–Castriota–Carlin (1959) and Zemanian (1965); see Srivastava (2021).

**Theorem 5.3 (dispersion) [P, cited].** A causal response with finite energy has a Fourier transform analytic in the upper half-plane, whose real and imaginary parts are Hilbert-transform pairs (Kramers–Kronig; Titchmarsh 1937).

**Theorem 5.4 (parity defect) [P].** For *any* real kernel $K$ on a finite grid, with $S=\tfrac12(K+K^{\mathsf T})$ and $A=\tfrac12(K-K^{\mathsf T})$,
$$\|S\|_F^2-\|A\|_F^2=\operatorname{tr}(K^2)=\langle K,K^{\mathsf T}\rangle_F .$$
For *any* real $f\in L^2(\mathbb R)$, with $(\mathcal Rf)(t)=f(-t)$,
$$\int(\operatorname{Re}\hat f)^2d\omega-\int(\operatorname{Im}\hat f)^2d\omega=2\pi\int f(t)f(-t)\,dt=2\pi\langle f,\mathcal Rf\rangle .$$
The defect is the overlap of the response with its own time reversal.

*Proof.* $\|S\|^2-\|A\|^2=\tfrac14(\|K+K^{\mathsf T}\|^2-\|K-K^{\mathsf T}\|^2)=\langle K,K^{\mathsf T}\rangle$. In the continuum, $\operatorname{Re}\hat f$ and $i\operatorname{Im}\hat f$ are the transforms of $f_e=\tfrac12(f+\mathcal Rf)$ and $f_o=\tfrac12(f-\mathcal Rf)$, and $\|f_e\|^2-\|f_o\|^2=\langle f,\mathcal Rf\rangle$. Plancherel finishes. $\square$

**Corollary 5.5 (causal parity) [P].** If the response is causal and has finite energy, the overlap $\langle f,\mathcal Rf\rangle$ vanishes except for the instantaneous part. On the grid, $\|S\|^2-\|A\|^2=\sum_iK_{ii}^2$. In the continuum, $\int(\operatorname{Re}\hat f)^2=\int(\operatorname{Im}\hat f)^2=\pi\int_0^\infty f^2$: *in a stable causal response, the reactive and resistive parts carry exactly equal energy.* The hypothesis is stability, not passivity: a stable amplifier $\chi=G/(\gamma-i\omega)$ with $G=3$ has zero defect (certificate P4.R2).

*What the defect detects.* For measured spectra, after the instantaneous part is subtracted, a nonzero defect certifies that the real-axis response is not the transform of a single-sided finite-energy kernel. That happens under **instability** — a pole in the upper half-plane, where the real-axis function becomes the transform of a two-sided kernel — or under genuine acausality, or under a violation of the stationarity assumption such as drift. The defect is then the cross-overlap between causal and anticausal parts. For a decaying mode plus an unstable one, $\chi=\frac1{\gamma_1-i\omega}-\frac1{\gamma_2+i\omega}$, the defect is $-4\pi/(\gamma_1+\gamma_2)$ exactly (certificate P4.R2). The defect detects the same crossing that Liu (2026) tracks as a Blaschke-winding jump when the spectral abscissa of the reduced dynamics changes sign. The test is a global companion to the Kramers–Kronig compliance tests of impedance spectroscopy, and it needs adequate bandwidth coverage [A].

### Three boundaries, not one

Beyond passivity, three distinct boundaries are often conflated:
1. **The passivity (gain) boundary.** Net gain appears ($\operatorname{Re}Z<0$ or $\|S(\omega)\|>1$ at some $\omega$). The noise-defect formula switches branch there (Theorem 8.2), and its only noiseless point, $\tau=1$, lies exactly on this boundary.
2. **The stability boundary.** A pole crosses into the upper half-plane — for example, a lasing threshold. The parity defect switches on there.
3. **Exceptional points.** Eigenvectors coalesce. This is a spectral degeneracy that can occur on either side of the other two boundaries. In PT-symmetric gain–loss dimers the PT-breaking exceptional point coincides with boundary 2, which is why the three are often identified.

Time reversal exchanges poles and zeros of the scattering matrix: a laser at threshold (a pole on the real axis) time-reverses into a coherent perfect absorber (a zero on the real axis) (Chong–Ge–Cao–Stone 2010) [A].

*Examples.* Glass's ultraviolet absorption $n''$ forces the visible dispersion of $n'$, which is why a prism separates colors. In the Wigner–Weisskopf model the decay rate (resistance) arrives with its dispersion partner, the Lamb shift, measured at $0.0306$ against a Kramers–Kronig prediction of $0.0303$. The reactance's derivative renormalizes the decay itself, and the fit becomes $Z^2e^{-Z\Gamma t}$ with $Z=1/(1-\operatorname{Re}\Sigma')$: $2.8\times10^{-3}$ error with $Z$ against $4.3\%$ without (certificate P1.C4, whose first-run failure is retained).

---

## 6. Every copy: temperature

**Lemma 6.1 (passivity) [P].** A state $\rho$ is passive iff $[\rho,H]=0$ and its eigenvalues are anti-ordered with energy. Its ergotropy is $\operatorname{tr}(\rho H)-\sum_ip_i^\downarrow E_i^\uparrow$.

*Proof.* Apply the rearrangement inequality to the doubly stochastic matrix $|U_{ij}|^2$. $\square$

**Theorem 6.2 (complete passivity is temperature) [P].** Let $H$ have at least two distinct eigenvalues. A faithful state is completely passive iff $\rho=e^{-\beta H}/Z$ with $\beta\ge0$. If $H\propto I$, every state is completely passive.

*Proof.* This is the case of Theorem 7.2 with no charges. The lattice argument given there handles degenerate levels automatically. The hypothesis "at least two distinct eigenvalues" is exactly $E\notin\operatorname{span}\{\mathbf1\}$. When it fails, no unitary can change the energy (certificate P4.R4.K4a). $\square$

**Remark 6.3 (degenerate manifolds).** Passivity of a single copy allows any population profile within a degenerate eigenspace. Complete passivity forces uniformity there, because copies let a lower-energy configuration be assembled from the "wrong" degenerate state. Certificate P4.R4.K4b: $E=(0,0,1)$ with $p=(\tfrac12,\tfrac13,\tfrac16)$ is passive but first turns active at $n^*=3$ copies, as pre-registered. The lattice proof of Theorem 7.2 covers degenerate levels without a separate step, and the same argument identifies the one genuine exception, $H\propto I$, stated in Theorem 6.2.

**Corollary 6.4 (zeroth law) [P].** Two ports that are jointly completely passive for $H_A+H_B$ share one $\beta$. Two Gibbs ports at different temperatures are each completely passive but jointly active: a heat engine exists. Certificate P2.S3 checks, exactly:
- a passive non-Gibbs state first becomes active at $n^*=3$ (ergotropy $39/1000$);
- two Gibbs ports at unequal temperatures first become jointly active at $n^*=3$ (ergotropy $4/243$);
- at equal temperature they stay passive through $n=5$.

An independent inversion search reproduces both $n^*=3$ witnesses. The copy number $n^*$ is an integer diagnostic of how far a state is from thermal. Fixed-$k$ passivity is studied by Alicki–Fannes (2013).

**Theorem 6.5 (one spectrum, many filters) [P].** Let $\rho=e^{-\beta H}/Z$ and let $A$ be an observable. Define the dissipation spectrum $\chi''(\omega)=\pi\sum_{ij}(p_i-p_j)|A_{ij}|^2\delta(\omega-\omega_{ij})$ with $\omega_{ij}=E_j-E_i$ ($\hbar=1$), write $x=\beta\omega/2$, and let $\sigma_{\rm el}$ be the elastic (degenerate-pair) part. Then:

*(a) Variances* — in units of $\frac1\pi\int_0^\infty(\cdot)\,\chi''\,d\omega$, plus $\sigma_{\rm el}$ for the first two:

| Quantity | Experiment | Filter |
|---|---|---|
| symmetrized variance $\operatorname{Var}(A)$ | watch | $\coth x$ |
| isothermal susceptibility $\times T$ | push | $1/x$ |
| quantum variance $\operatorname{Var}-T\chi$ (Frérot–Roscilde 2016) | watch − push | $\coth x-1/x$ |
| Wigner–Yanase skew information $-\tfrac12\operatorname{tr}[\sqrt\rho,A]^2$ | — | $\tanh(x/2)$ |

*(b) Every Petz monotone metric is a filter.* For an operator-monotone $f$ with $f(1)=1$ and $f(t)=tf(1/t)$, the monotone metric of the rotation family $e^{-iA\theta}\rho e^{iA\theta}$ is
$$F_f=\sum_{ij}\frac{(p_i-p_j)^2}{p_jf(p_i/p_j)}|A_{ij}|^2=\frac2\pi\int_0^\infty w_f(x)\,\chi''(\omega)\,d\omega,\qquad w_f(x)=\frac{e^{2x}-1}{f(e^{2x})}.$$

| Metric | $f(t)$ | $w_f(x)$ |
|---|---|---|
| SLD / Bures (minimal) | $\frac{1+t}2$ | $2\tanh x$ |
| Wigner–Yanase | $\big(\frac{1+\sqrt t}2\big)^2$ | $4\tanh\frac x2$ |
| Wigner–Yanase–Dyson ($0<\alpha<1$) | $\frac{\alpha(1-\alpha)(t-1)^2}{(t^\alpha-1)(t^{1-\alpha}-1)}$ | $\dfrac{2\sinh(\alpha x)\sinh((1-\alpha)x)}{\alpha(1-\alpha)\sinh x}$ |
| Kubo–Mori / BKM ($\alpha\to0$ of WYD) | $\frac{t-1}{\ln t}$ | $2x$ |
| RLD (maximal) | $\frac{2t}{1+t}$ | $\sinh 2x$ |

The Kubo–Mori entry equals $\beta\langle[A,[H,A]]\rangle$ (the f-sum rule).

*(c) Ordering.* Pointwise in $x>0$,
$$\coth x-\tfrac1x\ \le\ \tanh\tfrac x2\ \le\ \tanh x\ \le\ 2\tanh\tfrac x2\ \le\ x\ \le\ \tfrac12\sinh2x ,$$
so $\operatorname{Var}_Q\le I_{WY}\le\tfrac14F_{\rm SLD}\le\tfrac14F_{WY}\le\tfrac14F_{KM}\le\tfrac14F_{RLD}$. As $x\to0$ every filter collapses to its classical form ($1/x$ for variances, $2x$ for metrics).

*Proof.* Each entry is a sum over Bohr pairs, with $p_i/p_j=e^{2x}$, $\frac{p_i+p_j}{p_i-p_j}=\coth x$, and $\frac{(\sqrt{p_i}-\sqrt{p_j})^2}{p_i-p_j}=\tanh\frac x2$. For (b), $\frac{(p_i-p_j)^2}{p_jf(p_i/p_j)}=(p_i-p_j)\frac{e^{2x}-1}{f(e^{2x})}$. The closed forms follow by rewriting in exponentials; the Wigner–Yanase–Dyson form uses $e^{2\alpha x}-1=2e^{\alpha x}\sinh\alpha x$. For (c): $\coth x-\frac1x\le\tanh\frac x2$ reduces, with $u=x/2$, to $u\le\sinh u\cosh u$; $\tanh x=\frac{2t}{1+t^2}\le2t$ with $t=\tanh\frac x2$; $\tanh y\le y$; $\sinh y\ge y$. The middle inequalities $I_{WY}\le\frac14F_{\rm SLD}\le2I_{WY}$ recover Luo (2004). Certificates: P1.C2 (the four original lines, three independent routes, $10^{-10}$); P4.R5 (exact closed forms; skew information and the Wigner–Yanase and RLD metrics from the matrix formulas, $10^{-8}$ or better). $\square$

*Reading.* There is one dissipation spectrum, and every experiment and every information metric is a frequency filter applied to it. "Bures = watching, Kubo–Mori = pushing" is a statement about the *two canonical experiments*, not a dichotomy of the family: the SLD metric is dual to the symmetrized (watched) covariance, and the Kubo–Mori metric is dual to the canonical (pushed) covariance. Every other Petz metric is a different filter on the same measured $\chi''$ (Shitara–Ueda 2016). The Wigner–Yanase–Dyson family interpolates continuously from Kubo–Mori ($\alpha\to0$) to Wigner–Yanase ($\alpha=\tfrac12$).

**Corollary 6.6 (the second law as a relative entropy) [P].** For every unitary $U$,
$$D(U\rho U^\dagger\|\rho)=\beta W,\qquad W=\operatorname{tr}(U\rho U^\dagger H)-\operatorname{tr}(\rho H)\ge0 .$$
*Proof.* $\ln\rho=-\beta H-\ln Z$, and entropy is unitarily invariant. Certificate P1.C2.h. $\square$

**Proposition 6.7 (the coth law) [P].** Let two opposite elementary processes run at rates $r_\pm$ with detailed-balance ratio $r_+/r_-=e^{2u}$. Then
$$\frac{\text{symmetric fluctuation}}{\text{antisymmetric response}}=\frac{r_++r_-}{r_+-r_-}=\coth u\ \ge\ \frac1u .$$
Three instances:
1. **Quantum FDT.** Emission/absorption at Bohr frequency $\omega$ has $u=\beta\hbar\omega/2$, and $\operatorname{Var}/(T\chi)=u\coth u$ per mode.
2. **Tunnel junction.** Forward/backward tunneling has $\Gamma_+/\Gamma_-=e^{eV/k_BT}$, so $S_I/(2eI)=\coth\frac{eV}{2k_BT}$. This interpolates from Johnson noise ($4k_BTG$, $u\to0$) to Schottky shot noise ($2eI$, $u\to\infty$), and the crossover is used as a primary thermometer (Spietz et al. 2003).
3. **Biased ring (unicyclic Markov process with affinity $A$).** With $u=A/2$, $\sigma\operatorname{Var}(J)/J^2=2u\coth u$. The bound $2u\coth u\ge2$ is the thermodynamic uncertainty relation, saturated in the linear limit.

*The quantum FDT inequality $\operatorname{Var}\ge T\chi$ and the TUR are the same inequality, $u\coth u\ge1$, applied to different forward/backward pairs.* In each case $e^{2u}$ is supplied by local detailed balance — the KMS condition of the bath that drives each elementary transition — so the coth law descends from the copy lift. The classical FDT is its $u\to0$ limit. For general Markov networks the TUR holds as an inequality (Barato–Seifert 2015; Gingrich et al. 2016), and the coth form is its unicyclic equality structure. Certificate P4.R8.

---

## 7. The symmetry axis: which cycles count

The first three rows of §1.1 say *where and how often* the inequality is demanded. A symmetry changes something different: *which cycles are admissible*. If the cycles must conserve charges $Q_1,\dots,Q_m$ (with $[H,Q_k]=0$), fewer cycles are tested. Passivity is therefore easier to satisfy, and the family of free states is larger.

**Theorem 7.1 (generalized and non-Abelian thermal states are completely passive) [P].** Let $[H,Q_k]=0$ for all $k$, where the $Q_k$ need **not** commute with one another, and let $\rho=e^{-\beta(H-\sum_k\mu_kQ_k)}/Z$ with $\beta\ge0$. For every $n$ and every unitary $U$ on $n$ copies that commutes with every total charge $Q_k^{(n)}$,
$$\operatorname{tr}(U\rho^{\otimes n}U^\dagger H_n)\ \ge\ \operatorname{tr}(\rho^{\otimes n}H_n).$$

*Proof.* $\rho^{\otimes n}=e^{-\beta\tilde H_n}/Z^n$ with $\tilde H_n=H_n-\sum_k\mu_kQ_k^{(n)}$, because operators on different copies commute. So $\rho^{\otimes n}$ is Gibbs for $\tilde H_n$ and passive for it under all unitaries (Lemma 6.1). Since $U$ commutes with each $Q_k^{(n)}$, $\operatorname{tr}(U\rho^{\otimes n}U^\dagger Q_k^{(n)})=\operatorname{tr}(\rho^{\otimes n}Q_k^{(n)})$, and the $\tilde H_n$ inequality becomes the $H_n$ inequality. $\square$

**Theorem 7.2 (converse for commuting charges; with Theorem 6.2 as the case $m=0$) [P].** Let $H,Q_1,\dots,Q_m$ commute, with joint eigenbasis $|i\rangle$ carrying energies $E_i$ and integer charge vectors $q_i$. Let $\rho$ be faithful and diagonal in this basis. If $E\notin\operatorname{span}\{\mathbf1,q^{(1)},\dots,q^{(m)}\}$ (energy is not a function of the charges), then $\rho$ is completely passive under charge-conserving cycles iff
$$p_i\propto e^{-\beta E_i-\lambda\cdot q_i}\quad\text{for some }\beta\ge0,\ \lambda\in\mathbb R^m ,$$
that is, $\rho$ is a generalized Gibbs state with $\beta\mu_k=-\lambda_k$. If $E$ is a function of the charges, every such $\rho$ is passive under charge-conserving cycles.

*Proof.* (⇐) is Theorem 7.1. (⇒) Let $f_i=-\ln p_i$. Charge-conserving unitaries on $n$ copies are block-diagonal over total-charge sectors, so Lemma 6.1 applied inside each sector gives the following: for multisets $\alpha,\alpha'$ of the same size and the same total charge, $\sum_\alpha E<\sum_{\alpha'}E\Rightarrow\sum_\alpha f\le\sum_{\alpha'}f$. Let $L=\{c\in\mathbb Z^d:\sum c_i=0,\ \sum c_iq_i=0\}$. Every $c\in L$ is $\alpha-\alpha'$ for such multisets (its positive and negative parts). So the functionals $\phi_E(c)=\sum c_iE_i$ and $\phi_f(c)=\sum c_if_i$ satisfy $\phi_E(c)<0\Rightarrow\phi_f(c)\le0$ on $L_{\mathbb Q}$, by scaling.
- *Kernels.* Because $E\notin\operatorname{span}\{\mathbf1,q\}=L_{\mathbb R}^\perp$, and $L_{\mathbb Q}$ is dense in $L_{\mathbb R}$, there is $d\in L_{\mathbb Q}$ with $\phi_E(d)<0$. For $c\in L_{\mathbb Q}$ with $\phi_E(c)=0$, the vectors $\pm Nc+d$ have $\phi_E<0$, so $\pm N\phi_f(c)+\phi_f(d)\le0$ for all $N$. Hence $\phi_f(c)=0$.
- *Proportionality.* On the $\mathbb Q$-linear image $\phi_E(L_{\mathbb Q})\subset\mathbb R$, $\phi_f$ therefore factors through a monotone additive map, which is multiplication by some $\beta\ge0$ (a monotone additive function on a subgroup of $\mathbb R$ is linear). So $\phi_f=\beta\phi_E$ on $L_{\mathbb Q}$, and hence on $L_{\mathbb R}$ by density.
- *Conclusion.* $f-\beta E\in L_{\mathbb R}^\perp=\operatorname{span}\{\mathbf1,q^{(k)}\}$.

If instead $E\in\operatorname{span}\{\mathbf1,q\}$, a charge-conserving unitary cannot change the energy at all. With $m=0$ the argument is Theorem 6.2, degenerate levels included. $\square$

Certificate P4.R4:
- **K4c.** A GGE with $\mu\neq0$ is active under unrestricted cycles at $n=1$, but passive under charge-conserving cycles through $n=3$.
- **K4d.** A non-GGE state that is passive at $n=1$ turns active under charge-conserving cycles at $n^*=5$.
- **K4e.** When $E\in\operatorname{span}\{\mathbf1,q\}$, a non-GGE state stays passive.

**Remark 7.3 (why this is an axis, not a fourth demand).** The symmetry does not *strengthen* the demand in order to "select" a state. It *restricts* the admissible processes, and each conserved charge adds one Lagrange multiplier (one effort, $\mu_k$) to the free family — which is exactly the last row of the effort–flow table (§2.1). Demanding passivity over *all* cycles would instead exclude every GGE with $\mu\neq0$ (K4c). For non-commuting charges, Theorem 7.1 gives the forward direction exactly. The converse — that complete passivity under symmetric cycles singles out the non-Abelian thermal state — is established in resource-theoretic and microcanonical form by Guryanova et al. (2016), Yunger Halpern et al. (2016), and Lostaglio–Jennings–Rudolph (2017) [A]. A finite lattice proof in the non-Abelian case is not given here.

### The bridge to thermodynamic resource theories

A *thermal operation* (Janzing et al. 2000; Horodecki–Oppenheim 2013) is $\mathcal E(\rho)=\operatorname{tr}_B[U(\rho\otimes\gamma_B)U^\dagger]$ with $[U,H_S+H_B]=0$ and $\gamma_B$ Gibbs. In port language, it is **an interconnection with a completely passive port through a lossless, energy-conserving ledger**. Theorem 6.2 explains why the Gibbs state is the unique free state: it is the only completely passive one. The family of second laws — monotonicity of all Rényi divergences to $\gamma$ (Brandão et al. 2015) — contains Corollary 6.6 as its unitary, $\alpha=1$ instance. With conserved charges, the free states become those of Theorems 7.1–7.2 and the free operations become (non-Abelian) thermal operations.

---

## 8. First join: noise is the defect of the dilation

**Theorem 8.1 (classical noise defect; Kirchhoff) [P].** Let $S$ be a passive scattering matrix whose hidden ports (in any unitary completion) are thermal at $\theta=k_BT$ (available power per unit bandwidth). If the incident covariance is $\Sigma_a$, the outgoing covariance is
$$\Sigma_b=S\Sigma_aS^\dagger+\theta\,(I-SS^\dagger),$$
independently of the completion chosen. It follows that:
- (i) a port at uniform temperature leaves thermal radiation unchanged;
- (ii) emissivity $e_i=(I-SS^\dagger)_{ii}$ equals absorptivity $a_i=(I-S^\dagger S)_{ii}$ whenever $S=S^{\mathsf T}$ (reciprocity);
- (iii) for non-reciprocal $S$, per-port equality can fail while $\sum_ie_i=\sum_ia_i$ still holds.

*Proof.* $b=Sa+Bc$ with hidden inputs $c$ of covariance $\theta I$, and $BB^\dagger=I-SS^\dagger$ by Proposition 4.4. Then (i) is $S\theta S^\dagger+\theta(I-SS^\dagger)=\theta I$, (ii) is equality of row and column norms, and (iii) is $\operatorname{tr}SS^\dagger=\operatorname{tr}S^\dagger S$. Certificates P3.N1 and P4.R10. $\square$

This is Bosma's (1967) and Twiss's (1955) theorem, and Kirchhoff's law (1860) in matrix form. Part (iii) is the observed per-port violation of Kirchhoff's law in magneto-optical emitters (Zhu–Fan 2014; Shayegan et al. 2023), with the second law untouched. The cause is the antisymmetric (Onsager–Casimir, gyrator) part of the response.

**Theorem 8.2 (quantum noise defect: passive and active ports) [P].** For a phase-insensitive bosonic channel $V_{\rm out}=\tau V_{\rm in}+N$ on quadrature variances:

1. It is completely positive iff $N\ge|1-\tau|/2$ (Holevo–Werner 2001).
2. For $\tau\le1$ it is dilated by a beam splitter, and for $\tau\ge1$ by a two-mode squeezer. With the hidden mode at occupation $n$, both give
$$N=|1-\tau|\big(n+\tfrac12\big),\qquad n+\tfrac12=\tfrac12\coth\frac{\hbar\omega}{2k_BT}.$$
3. At $n=0$ the bound in (1) is saturated. For $\tau>1$ this is Caves's theorem; for $\tau<1$ it is the vacuum noise of loss. The classical limit $N\to|1-\tau|k_BT/\hbar\omega$ recovers Theorem 8.1 per mode.

*Proof.* Symbolic (certificate P3.N2). The Heisenberg maps $b=\sqrt\tau a+\sqrt{1-\tau}\,c$ and $b=\sqrt\tau a+\sqrt{\tau-1}\,c^\dagger$ preserve $[b,b^\dagger]=1$ only with the hidden term present. $\square$

**Proposition 8.3 (rotation, boost, and where the gain comes from) [P].** Let $N_a,N_c$ be number operators.
- (a) The beam-splitter generator $a^\dagger c+ac^\dagger$ conserves $N_a+N_c$. Its invariant form is $|a|^2+|c|^2$ (compact, $SU(2)$: a rotation).
- (b) The squeezer generator $a^\dagger c^\dagger+ac$ conserves $N_a-N_c$. Its invariant form is $|a|^2-|c|^2$ (hyperbolic, $SU(1,1)$: a boost). It does **not** conserve the energy $\omega_aN_a+\omega_cN_c$, so it cannot act on its own.
- (c) With a pump mode $b$, the term $a^\dagger c^\dagger b+ac\,b^\dagger$ conserves $\omega_aN_a+\omega_cN_c+\omega_pN_b$ iff $\omega_p=\omega_a+\omega_c$.

The energy for gain is therefore drawn from the pump port, whose reference state (a coherent pump, or an inverted medium at negative temperature) is non-passive. Certificate P4.R7 checks all three exactly in truncated Fock space. $\square$

*Reading.* Passive ports dilate by rotations; active ports dilate by boosts fed by a non-passive source (Definition 2.5). In both cases the noise is the size of the non-unitarity, $|1-\tau|$, times the occupation of the hidden port. The $\coth$ is the same one that weights the watched variance (Theorem 6.5). Only $\tau=1$ — a lossless, gainless port on the passivity boundary (§5, "Three boundaries") — can be noiseless. Prohibition 4 has two halves: no gain without noise (the defect), and no gain without a source (the pump).

**Theorem 8.4 (noise is local; Levin's direct approach, finite and continuum) [P].** Let $\mathcal D(\omega)=\mathcal K-\omega^2\mathcal M+i\omega\mathcal C$ be a symmetric operator on a Hilbert space (a finite network or a field theory), with $\mathcal M,\mathcal K\succ0$ and $\mathcal C\succeq0$, and let each lossy element carry thermal force noise of one-sided spectral density $4k_BT\mathcal C$. For any readout $y=\langle p,x\rangle$, with $\mathcal G=\mathcal D^{-1}$ and $\chi_{pp}=\langle p,\mathcal Gp\rangle$,
$$S_y(\omega)=4k_BT\langle p,\mathcal G\mathcal C\bar{\mathcal G}p\rangle=\frac{4k_BT}{\omega}\big|\operatorname{Im}\chi_{pp}\big|=\frac{8k_BT\,W_{\rm diss}(\omega)}{\omega^2F_0^2},$$
where $W_{\rm diss}$ is the power dissipated when the system is pushed with force $F_0\cos\omega t$ distributed with the readout's own profile $p$.

*Proof.* $\mathcal G-\bar{\mathcal G}=-2i\omega\,\mathcal G\mathcal C\bar{\mathcal G}$ follows from $\mathcal G^{-1}-\bar{\mathcal G}^{-1}=2i\omega\mathcal C$ and the symmetry of $\mathcal G$. The proof uses only operator algebra, so it holds verbatim in infinite dimensions. Certificate P3.N6 checks the finite case exactly. $\square$

*Reading.* Noise modeling is **local and compositional**. Assign FDT noise to every loss and the correct noise appears at every port. To predict what a readout will watch, push with the readout's shape. This is how gravitational-wave mirror thermal noise is computed (Saulson 1990; Levin 1998). In continuum form (with the quantum replacement $k_BT\to\Theta=\frac{\hbar\omega}2\coth\frac{\hbar\omega}{2k_BT}$), the same statement is:
- Landau–Lifshitz fluctuating hydrodynamics (stress noise fixed by viscosity);
- Rytov's fluctuational electrodynamics (current noise fixed by $\operatorname{Im}\varepsilon$), and therefore the Lifshitz theory of Casimir and van der Waals forces, and super-Planckian near-field heat transfer (Polder–van Hove 1971) [A].

**Proposition 8.5 (the price of a bit) [P].** Through a port with thermal noise $N_0=k_BT$, Shannon's capacity $C(W)=W\log_2(1+\frac P{N_0W})$ gives $E_b\ge\lim_{W\to\infty}P/C=k_BT\ln2$ (exact limit, certificate P2.S4). Erasure into a thermal bath costs $Q\ge k_BT\ln2$ (Landauer 1961), via bath passivity: $\beta Q=\Delta S_{\rm sys}+I'(S{:}B)+D(\rho_B'\|\gamma_B)$ (Esposito–Lindenberg–Van den Broeck 2010; Reeb–Wolf 2014). It is the same $k_BT$ in Nyquist's noise, Shannon's floor, Landauer's erasure, and Theorem 8.1's defect, because the heat always crosses the same hidden ports.

---

## 9. Second join: ports and Noether charges

**Setup.** $[H_S,Q]=0$. The port couples through $H_{\rm int}=\sum_kg_kS_k\otimes B_k$, and the total charge is conserved. The port **supplies** a charge $Q$ if some coupling fails to commute with $Q$. It **reads** $Q$ if a coupling commuting with $Q$ acts on the $Q$-sectors as a non-constant function $f(Q)$.

**Theorem 9.1 (Abelian selection rule) [P for (a),(c),(d); A for (b)].**
- **(a) No supply, no flip — exactly.** If every coupling commutes with $Q$, then $Q$ is conserved by the full system–environment unitary, to all orders, for all environment states.
- **(b) Supply needs a donor.** To leading order, transitions $q\to q+\Delta Q$ occur at rate $\sum_{k:q_k=\Delta Q}|g_k|^2S_{B_k}(\omega)$, where $S_{B_k}$ is the environment's fluctuation spectrum in its $-\Delta Q$ sector. By KMS, $S_B=2\hbar(n+1)\chi_B''$, and detailed balance gives the generalized Gibbs ratio (Theorem 7.2). If the environment's charge carriers are gapped by $\Delta$, flips between degenerate sectors consume thermally pre-existing carriers and are suppressed by $e^{-\beta\Delta}$ (quasiparticle poisoning).
- **(c) Reading dephases in proportion to distinguishability.** A neutral coupling $f(Q)$ destroys the $(q,q')$ coherence at rate $\frac\gamma2|f(q)-f(q')|^2$ and leaves populations unchanged.
- **(d) What the port cannot touch, it cannot corrupt.** Information in the commutant of the port's coupling algebra is invariant (Zanardi–Rasetti 1997; Knill–Laflamme–Viola 2000).

*Proof.* (a) $[Q\otimes I,H_{\rm tot}]=0$. (c) and (d) are Lindblad identities. (b) combines the Davies rates with KMS, and its exact skeleton is certified. Certificate P3.N3, including $\Gamma_2=\Gamma_1/2+\Gamma_\phi$. $\square$

**Theorem 9.2 (the port–charge table, Abelian) [P structure, A examples].**

| | **does not read $Q$** | **reads $Q$** |
|---|---|---|
| **does not supply** | **protected memory** (decoherence-free subspaces, noiseless subsystems, topological qubits) | **non-demolition measurement** — watched forever without change (Braginsky–Vorontsov–Thorne 1980); dephasing = being measured; pointer basis = what the port reads |
| **supplies** | **control** — a coherent drive changes the charge without learning it | **thermalization** — $T_1$ from supply, $T_\phi$ from reading; relaxation to the GGE |

**Theorem 9.3 (non-Abelian collapse; Schur) [P].** Let the charges generate a compact Lie algebra $\mathfrak g$ acting on $\mathcal H_S=\bigoplus_\lambda V_\lambda\otimes M_\lambda$ (irreducible representations $V_\lambda$ with multiplicity spaces $M_\lambda$).
- **(a)** A coupling that commutes with *every* charge has the form $\bigoplus_\lambda I_{V_\lambda}\otimes X_\lambda$. It supplies nothing and reads only the center (the Casimirs, i.e. the label $\lambda$).
- **(b)** A coupling that commutes with one component $Q_a$ but is not of the form $I_{V_\lambda}\otimes X_\lambda$ on some block — for example, a non-constant $f(Q_a)$ on an irreducible sector — fails to commute with some $Q_b$. **Reading one non-central component supplies its conjugates.**
- **(c)** A port whose couplings lie in the algebra generated by the charges (collective noise) acts as $\bigoplus_\lambda\pi_\lambda(\cdot)\otimes I_{M_\lambda}$. **The multiplicity spaces are protected memory.**

*Proof.* By Schur's lemma, the commutant of an irreducible $\mathfrak g$-action on $V_\lambda\otimes M_\lambda$ is $I\otimes\operatorname{End}(M_\lambda)$, and inequivalent blocks cannot mix. That gives (a), and (b) is its contrapositive. For (c), the collective generators act trivially on each $M_\lambda$.

Certificate P4.R6 checks the following exactly:
- **(i)** Spin-½ with a jump $S_z$: $\mathcal L^*(S_z)=0$ but $\mathcal L^*(S_x)=-\frac\gamma2S_x$.
- **(ii)** Spin-1: $[f(S_z),S_x]=0$ iff $f$ is constant.
- **(iii)** Two spins with a Casimir jump $J^2$: no component is changed, and the singlet–triplet coherence decays at $2\gamma$.
- **(iv)** Three spins under collective $S_z,S_\pm$ noise: $\mathcal L^*(P_\sigma)=0$ for all six permutations, so the multiplicity-space qubit is protected.

$\square$

*Reading.* For an Abelian charge the four cells of the table are independent. For a non-Abelian algebra, the cell "reads without supplying" shrinks to the **center**: only the Casimirs (for spin, the total $J^2$) can be watched without disturbing any component. Reading $S_z$ is non-demolition *for $S_z$*, but it supplies $S_x$ and $S_y$. The protected cell becomes the **multiplicity spaces** — the logic behind collective-noise decoherence-free subsystems. The popular statement that "symmetry-protected sectors cannot flip unless the environment can supply the Noether charge" is the Abelian top row read left to right. Its completion is: **symmetry protects the bit, not the phase**, and, for non-Abelian charges, **it protects only what lives in multiplicity**.

*Engineering design rule [A].* $T_1$ is set by the charged sector of the environment's dissipation spectrum at the qubit frequency. $T_\phi$ is set by the neutral sector's low-frequency spectrum times $|f(q)-f(q')|^2$. Protection is bought by gapping the first and blinding the second. For non-Abelian encodings, store in multiplicity and read only Casimirs.

---

## 10. Away from equilibrium: the arrow is the gap between watching and pushing

**Theorem 10.1 (Harada–Sasa 2005) [P, cited; certified instance].** For Langevin dynamics, the heat dissipation rate equals $\gamma\{\langle v\rangle^2+\int\frac{d\omega}{2\pi}[\tilde C_v-2T\tilde R'_v]\}$, the frequency-resolved violation of the FDT.

*Certified instance (P1.C3).* An overdamped particle with a circulating force $kJx$ has an **exactly Gibbs** stationary density $\Sigma=(T/k)I$, so every snapshot reports equilibrium. Yet the FDT-violation integral equals the hidden heat $2kT\omega^2$ exactly, and it vanishes pointwise when $\omega=0$.

**Proposition 10.2 (when is a snapshot enough?) [P].** A finite Markov process $T$ and its time reverse $\tilde T=D_\pi^{-1}T^{\mathsf T}D_\pi$ share their stationary distribution. Pair statistics (a log) distinguish them iff detailed balance fails, and the entropy production rate is the Kullback–Leibler divergence between forward and reversed pair statistics (Schnakenberg 1976). *A snapshot suffices exactly when there is no current* (cf. the snapshot blindness to the antisymmetric part in *Curvature and Current*, Murillo 2026).

**Proposition 10.3 (watching bounds pushing, anywhere) [P, cited].** Around an arbitrary nonequilibrium steady state, the response of any observable to a perturbation satisfies $|\delta\langle A\rangle|^2\le2\operatorname{Var}(A)\,D_{KL}(P_\varepsilon\|P_0)$ (Dechant–Sasa 2020). At equilibrium the FDT fixes the response exactly in terms of fluctuations; the fluctuation–response inequality bounds it around any steady state, and the TUR follows from it for a "virtual" perturbation along the mean velocity. Together with the coth law (Proposition 6.7), this gives the nonequilibrium version of the watch–push relation: *watching bounds pushing, and the price is relative entropy*.

**Generalizations [P, cited].** Dissipation equals $k_BT$ times the relative entropy between forward and time-reversed path ensembles (Kawai–Parrondo–Van den Broeck 2007). The Jarzynski and Crooks fluctuation theorems are the nonlinear completion. Harada–Sasa has been used to measure the near-perfect efficiency of F$_1$-ATPase (Toyabe et al. 2010).

*Reading.* The arrow of time is measurable as the gap between watching and pushing. When do observational data predict interventions? Exactly at equilibrium, and the gap is the dissipation (cf. Baldovin–Cecconi–Vulpiani 2020).

---

## 11. The modeling calculus

**Proposition 11.1 (closure) [P].**
1. *Interconnection.* Power-conserving interconnection of passive ports is passive. For port-Hamiltonian systems $\dot x=(J-R)Qx+Bu,\ y=B^{\mathsf T}Qx$ (with $\dot H=-x^{\mathsf T}QRQx+y^{\mathsf T}u$), the feedback $u_1=-y_2,\ u_2=y_1$ yields $J_c$ skew and $R_c\succeq0$.
2. *Reduction.* A compression of a contraction is a contraction. Effort-constraint projection $W=QV(V^{\mathsf T}QV)^{-1}$ preserves $J_r$ skew, $R_r\succeq0$, and $Q_r\succ0$, so the reduced model is positive-real (Polyuga–van der Schaft 2012; cf. PRIMA, Odabasioglu–Celik–Pileggi 1998).
3. *Dilation.* Every passive model can be simulated as a reversible system coupled to a bath (§4), and the noise it predicts does not depend on the ledger chosen (Proposition 4.4).
4. *Noise assignment.* Local FDT at each loss implies the FDT at every port, in finite networks and in continuous fields (Theorem 8.4).
5. *Stability.* The stored energy is a Lyapunov function, and a feedback loop of passive systems is stable (Zames 1966).

Certificates: P3.N5 (items 1–2, including $\operatorname{Re}G(i\omega)\ge0$ for the full and reduced models) and P3.N6 (item 4).

**The workflow this licenses.** Specify two things: the reversible skeleton ($J$ and the storage $Q$) and the losses ($R$ with their temperatures). Noise, stationary states, and dispersion are then *determined*. Physical admissibility of fits (positive-realness, parity defect), validity of reduced models, and stability of assemblies are *checkable* by one inequality. Dynamics, noise, stability, and thermodynamic consistency — four modeling tasks — become one. Circuit simulators (resistor noise $4k_BTR$), signal-integrity tools (passivity enforcement of fitted macromodels), and gravitational-wave detectors (thermal noise from loss angles) each practice a fragment of this. The principle says the fragments are one method, valid in every row of the effort–flow table, including continuous fields (Theorem 8.4) and chemical reaction networks (the chemical Langevin equation). Stochastic gradient descent obeys an analogous set of fluctuation–dissipation relations (Yaida 2019) — a structural analogy only.

---

## 12. Measurement through a port

**What the principle resolves [P/A].**
- *The cut.* Von Neumann's movable cut is the statement that partial traces compose.
- *Generalized measurements.* Every POVM is a projective measurement on the ledger (Naimark).
- *The pointer basis.* It is the eigenbasis of what the port *reads*. For non-Abelian charges, only the Casimirs can be read without disturbing any component; a single component can be read non-demolitionally for itself, but doing so supplies its conjugates (Theorem 9.3).
- *Durability.* A record lasts as long as the recurrence time of the channel that received it, and forever only in the continuous-spectrum limit (Theorem 4.5, Corollary 4.6).
- *Cost.* At least $k_BT\ln2$ per durable bit (Proposition 8.5).
- *Timestamps.* A position reading is a joint event of pointer and clock, and time can be defined as correlation with a clock subsystem (Page–Wootters 1983).

**What it does not resolve [C, fenced].** Why *this* outcome occurs. The principle localizes the residue to one indexical question — *which branch of the ledger is this port on?* — and supplies the measure (Born, Gleason 1957) but not the pointer.

---

## 13. What the principle answers in one line

1. *Why does every absorbing material disperse light?* Stable causality gives resistance and reactance equal energy (§5).
2. *How much does a resistor hiss?* $4k_BTR$ per hertz: temperature times the squared defect (§8).
3. *Why must every amplifier add noise, and where does its energy come from?* Gain is a boost dilation: added noise $(G-1)(n+\tfrac12)$, energy from a pump with $\omega_p=\omega_s+\omega_i$ (§8).
4. *Least energy per bit?* $k_BT\ln2$, by Shannon + Nyquist or by Landauer — the same hidden ports (§8).
5. *A sensor's thermal noise floor?* Push with the readout's own profile and compute the loss (§8).
6. *Why do neutral bodies attract (Casimir / van der Waals)?* Each body's field fluctuations are fixed by its absorption, via the FDT on the field port (§8).
7. *How can shot noise measure temperature without calibration?* $S/2eI=\coth(eV/2k_BT)$ — the coth law (§6).
8. *What does precision cost?* $\sigma\operatorname{Var}(J)/J^2\ge2k_B$ — the same $u\coth u\ge1$ as the quantum FDT (§6).
9. *Why does temperature exist, and why is it shared?* Complete passivity forces Gibbs at one $\beta$ (§6).
10. *Why do chemical potentials exist?* Each conserved charge that the admissible cycles must respect adds one multiplier (§7).
11. *When does a symmetry protect a qubit, and against what?* Against flips if the environment cannot supply the charge; against dephasing only if no port can read it; for non-Abelian charges, only information stored in multiplicity (§9).
12. *Can I read $S_z$ without disturbing $S_x$?* Not on an irreducible sector. Only the total spin is readable without back-action on any component (§9).
13. *What can be monitored forever without disturbance?* Conserved charges; for the whole of a non-Abelian algebra, only its Casimirs (§9).
14. *Why is loss irreversible if physics is reversible?* The receiving ledger has (effectively) continuous spectrum. Point spectra echo (§4).
15. *How long does a record last?* About $2\pi N/W$ for the receiving channel. The average echo is about $\delta/\pi\Gamma$ (§4).
16. *When is a snapshot enough?* Iff there is no current (§10).
17. *When do observational data predict interventions?* At equilibrium; the gap is the dissipation (§10).
18. *Is my fitted model physical?* Check passivity and the parity defect (§§5, 11).
19. *Does a Kramers–Kronig-type test fail for a gain medium?* Only if it is unstable, not merely because it amplifies (§5).
20. *Can I simplify my model without breaking its physics?* Yes, by compression (§11).
21. *Can I measure entanglement by pushing?* Yes: every quantum Fisher metric is a filter on the measured dissipation (§6).
22. *What does the choice of quantum Fisher metric mean?* A choice of frequency filter on one spectrum (§6).
23. *Can emissivity differ from absorptivity?* Per port, if the emitter is non-reciprocal; never in total (§8).
24. *How efficient is a molecular motor?* Measure its FDT violation (§10).

---

## 14. Where the principle strains

**Gravity [P for the obstruction, A for the local statement].** Self-gravitating systems have negative heat capacity, and the Newtonian Hamiltonian is unbounded below, so no global passive state exists and the copy lift fails globally. Locally, the principle survives: the vacuum on a Rindler wedge is KMS for boosts (Bisognano–Wichmann 1975), and Jacobson (1995) derives Einstein's equations from $\delta Q=T\,dS$ on every local horizon. Gravity is where local passive ports fail to glue into a global passive state. Whether gravity's port is reactive (able to entangle; Bose et al. 2017; Marletto–Vedral 2017) or purely resistive (decohering; Oppenheim 2023, whose decoherence–diffusion trade-off is itself an FDT-type lock) is open. We note, without leaning on it, the stochastic-spacetime proposal for galactic dynamics (Oppenheim–Russo 2024) and its critique (Hertzberg–Loeb 2024).

**Non-Abelian converse [A].** Theorem 7.1 is exact. The converse selection of the non-Abelian thermal state is imported from the resource-theory literature rather than proven by a finite lattice argument here.

**Singular continuous spectra.** Theorem 4.5 guarantees forgetting on average, not pointwise. Sparse recurrences are possible.

**The origin of the arrow [fenced].** Passivity at every instant *selects* a direction of time. It does not explain why reference states are passive, that is, the low-entropy past. Misra–Prigogine–Courbage (1979) give the converse of dilation, and we take no side.

**The ledger's ontology [fenced].** Dilation theorems assert that a lossless completion *exists*, not that it is physically real. Proposition 4.4 makes every prediction independent of which completion is imagined.

**Active matter [A].** Apparent activity is passivity with a non-passive sub-port inside the boundary (Definition 2.5). Lasers, motors, and cells are priced by the active branch of Theorem 8.2 and by the pump rule of Proposition 8.3.

**Beyond linear response.** The spectral calculus of §§5–8 is linear. The fluctuation theorems and the fluctuation–response inequality (§10) extend the principle, but not the filter tables.

---

## 15. Objections and replies

- *"Textbook linear response."* The ingredients are, and they are credited (§1.2). The claim is the organization, which Kitcher's (1981) criterion lets us measure by counting argument patterns. From the single pattern *(passivity) × (lift or axis) → (filter on the port's spectral measure)* we derive about twenty results:
  - Kramers–Kronig; causal parity and the parity defect;
  - Halmos/Egerváry/Stinespring/Naimark; Wiener's echo-or-forget law;
  - Pusz–Woronowicz/Lenard; the zeroth law; the GGE and the non-Abelian thermal state;
  - the classical and quantum FDT; the Petz and WYD filters; $D=\beta W$; the coth law (quantum FDT inequality, TUR, tunnel-junction noise);
  - Kirchhoff/Bosma; Caves and the pump rule; Levin/Rytov/Lifshitz; Shannon–Nyquist–Landauer;
  - the Abelian and non-Abelian port–charge tables; Harada–Sasa; snapshot sufficiency.
- *"Dissipativity theory already did this"* (Willems, Haddad, van der Schaft). That work is classical and deterministic. The copy lift, the quantum dilations, the filter tables, the symmetry axis, and the charge tables are what the port view adds.
- *"Causality plus purification already reconstructs quantum theory"* (Chiribella et al.). The base inequality and the time lift are their axioms, which we read as corroboration. We add temperature, symmetry, and the spectral calculus.
- *"The quantifiers are redundant, or incomplete."* The time lift strictly strengthens the base (Proposition 3.1), and the copy lift is independent of both. Charges enter as a restriction of admissible cycles that enlarges the free family (§7). They do not enter as a further demand that selects a state.
- *"Causal parity fails for gain media."* It fails for *unstable* media. Gain is allowed (Corollary 5.5), and the exact defect for any kernel is its time-reflection overlap (Theorem 5.4).
- *"Active ports equivocate on the boundary."* The boundary rule (Definition 2.5) and the pump theorem (Proposition 8.3) make the source explicit. The principle never claims an active port is passive.
- *"'Port' is anthropocentric"* (Bell). A port is a subsystem plus its couplings; no observer is involved. "For all practical purposes" is made quantitative in Corollary 4.6, and made exact in the continuum by Theorem 4.5.
- *"A principle that explains everything forbids nothing"* (Popper). It forbids six things (§3), and §16 lists refuting observations.

---

## 16. Falsifiers

Each entry is a matched pair: an outcome that corroborates (K) and one that refutes (L).

1. **The root.** L: cyclic work extracted from a completely passive reference state. K: no such device exists.
2. **Collapse models.** A fundamental, non-dilatable loss must carry matched dissipation at finite temperature (dissipative CSL; Smirne–Bassi 2015). L: collapse heating that never saturates. K: collapse noise that thermalizes.
3. **Amplifiers.** L: a phase-insensitive amplifier beating $N=(G-1)/2$, or gain without an identifiable non-passive source. K: none has been built.
4. **Abelian protection.** L: flips between charge sectors in an environment that provably cannot supply the charge (Theorem 9.1a is exact). K: protected-qubit lifetimes scaling as $e^{\beta\Delta}$ with the carrier gap.
5. **Non-Abelian back-action.** L: reading a non-central charge component on an irreducible sector with no back-action on its conjugates (Theorem 9.3b is exact). K: none observed.
6. **Gravity.** L: gravitational decoherence without the diffusion the trade-off requires. K: observed gravitational entanglement, or a trade-off-respecting stochastic signature.
7. **Parity.** L: a *stable*, stationary, causal response over adequate bandwidth with a nonzero defect. K: stable amplifiers with zero defect; unstable systems with the predicted cross-overlap defect.
8. **The coth law.** L: a tunnel junction in the pure-tunneling regime whose $S/2eI$ deviates from $\coth(eV/2k_BT)$ beyond instrumental error. K: Spietz et al. (2003) primary thermometry.

The principle's empirical strength is inherited from the second law, unitarity, and KMS. Its own new risky content is modest, and we say so.

---

## 17. What is beautiful here, and what it is for

**Economy.** One inequality, one base, two lifts, one symmetry axis, two joins, and six prohibitions.

**Symmetry.** The same pairs keep recurring:
- watching and pushing; $\coth$ and $1/x$; $\tanh$ and $x$; sum and difference of opposite rates;
- symmetric and antisymmetric; emission and absorption;
- rotation (passive) and boost (active); $N_a+N_c$ and $N_a-N_c$;
- supplying and reading a charge; center and multiplicity;
- point and continuous spectrum; echo and forgetting.

**Compression.** A single elementary identity, $\frac{r_++r_-}{r_+-r_-}=\coth u$, carries the quantum FDT, the thermodynamic uncertainty relation, and a primary thermometer.

**Honesty about the unknown.** The principle marks where it strains: global gravity, the non-Abelian converse, the past hypothesis, and single outcomes.

**For teaching.** One resistor gives Johnson–Nyquist, Kramers–Kronig, Shannon, and Landauer. One tunnel junction gives the coth law. The effort–flow table lets every discipline enter from its own door.

**For research.** The principle ties together the Petz and WYD families, noiseless subsystems and their non-Abelian form, non-demolition measurement, resource theories, the TUR, and fluctuation theorems, and it yields design rules for protected qubits.

**For engineering.** Four modeling tasks become one, with universal checks (passivity, parity defect) and universal recipes (put $k_BT$ on every loss; push with the readout's shape; trace every gain to its source).

---

## Appendix A. Certificate suite

All certificates are in `empirical/port_principle/`. Every vanishing or membership decision uses exact rational or symbolic arithmetic. Floating point appears only in labelled numerical witnesses, with stated tolerances. Falsifiers were written into each file before its first run, and failures are retained.

| File | Content | Result |
|---|---|---|
| `p1_four_locks.py` | C1 causal parity; C2 four weights and $D=\beta W$; C3 Gibbs density with hidden current (Harada–Sasa); C4 decay from rotations, Lamb shift, $Z$-renormalization, echo | 21/22. C4.a failed (4.3%) because the reactance's derivative renormalizes the decay; superseded by C4.a′ (0.28%). The failure is retained. |
| `p2_three_quantifiers.py` | S1 every-instant ⟹ causality, and precognition; S2 exact Egerváry ledger, horizon sharp; S3 $n^*=3$ thresholds, zeroth law; S4 $E_b/N_0\to\ln2$ | 10/10. Independent inversion search agrees. |
| `p3_protection_noise_modeling.py` | N1 noise defect and Kirchhoff; N2 unified $|1-\tau|(n+\tfrac12)$; N3 Abelian port–charge table; N5 port-Hamiltonian closure; N6 Levin locality | 17/17. N2.K2c first failed on a symbolic-simplifier artifact ($\coth$); fixed and logged. |
| `p4_review_v2.py` | R1 wave form and Cayley; R2 parity defect (gain allowed; instability detected); R3 Wiener; R4 $H\propto I$ edge case, degenerate $n^*=3$, GGE enlargement, non-GGE $n^*=5$, trivial case; R5 Petz/WYD filters and ordering; R6 non-Abelian (Schur, Casimir, multiplicity); R7 pump rule; R8 coth law; R10 dilation independence | 20/20. R10 first failed on a checker bug (`nsimplify` corrupting exact rationals); fixed and logged. |

## Appendix B. Glossary across disciplines

| Here | Physics | Engineering | Information / data | Statistics / causality |
|---|---|---|---|---|
| port | open-system boundary, coupling | terminal pair, bond | interface, endpoint | unit exposed to intervention |
| watch | correlation, fluctuation spectrum | noise measurement | logs, traces | observational data |
| push | response function, susceptibility | transfer function, impedance | probe, query | intervention, do-operator |
| passivity | second law (Kelvin), complete passivity | positive-real, dissipativity | data-processing inequality | — |
| ledger (dilation) | purification, environment | lossless embedding + loads | event log (event sourcing) | full generative process |
| defect | loss channel | noise-wave source | lossy compression | unmeasured confounding |
| echo horizon | Poincaré recurrence; point spectrum | reverberation time | log retention window | — |
| charge | Noether charge | conserved quantity | invariant, checksum | — |
| active port | non-passive reference (pump, inversion) | powered amplifier | — | — |

## References (content-level; to be formatted)

Alicki & Fannes 2013 (PRE 87, 042123); Baez & Fong 2018 (TAC 33, 1158); Baldovin, Cecconi & Vulpiani 2020 (PRR 2, 043436); Barato & Seifert 2015 (PRL 114, 158101); Bisognano & Wichmann 1975; Bose et al. 2017 (PRL 119, 240401); Bosma 1967; Braginsky, Vorontsov & Thorne 1980 (Science 209, 547); Brandão, Horodecki, Ng, Oppenheim & Wehner 2015 (PNAS 112, 3275); Callen & Welton 1951; Caves 1982 (PRD 26, 1817); Chiribella, D'Ariano & Perinotti 2010 (PRA 81, 062348); Chong, Ge, Cao & Stone 2010 (PRL 105, 053901); Crooks 1999; Dechant & Sasa 2020 (PNAS 117, 6430); Egerváry 1954; Einstein 1905; Esposito, Lindenberg & Van den Broeck 2010 (NJP 12, 013013); Frérot & Roscilde 2016 (PRB 94, 075121); Gingrich, Horowitz, Perunov & England 2016 (PRL 116, 120601); Gleason 1957; Guryanova, Popescu, Short, Silva & Skrzypczyk 2016 (Nat. Commun. 7, 12049); Haddad 2019 (Princeton); Halmos 1950; Harada & Sasa 2005 (PRL 95, 130602); Hauke, Heyl, Tagliacozzo & Zoller 2016 (Nat. Phys. 12, 778); Haus & Mullen 1962; Hertzberg & Loeb 2024 (arXiv:2404.13037); Holevo & Werner 2001 (PRA 63, 032312); Horodecki & Oppenheim 2013 (Nat. Commun. 4, 2059); Jacobson 1995 (PRL 75, 1260); Janzing, Wocjan, Zeier, Geiss & Beth 2000; Jarzynski 1997; Kawai, Parrondo & Van den Broeck 2007 (PRL 98, 080602); Kitcher 1981; Knill, Laflamme & Viola 2000 (PRL 84, 2525); Kubo 1957; Landau & Lifshitz 1957 (fluctuating hydrodynamics); Landauer 1961; Lenard 1978; Levin 1998 (PRD 57, 659); Lifshitz 1956; Liu 2026 (arXiv:2605.00117); Lostaglio, Jennings & Rudolph 2017 (NJP 19, 043008); Luo 2004 (Proc. AMS 132, 885); Marletto & Vedral 2017 (PRL 119, 240402); Misra, Prigogine & Courbage 1979; Naimark 1940; Nyquist 1928; Odabasioglu, Celik & Pileggi 1998; Oppenheim 2023 (PRX 13, 041040); Oppenheim & Russo 2024 (arXiv:2402.19459); Page & Wootters 1983; Paynter 1961; Petz 1996; Polder & Van Hove 1971 (PRB 4, 3303); Polyuga & van der Schaft 2012; Pusz & Woronowicz 1978 (CMP 58, 273); Reeb & Wolf 2014 (NJP 16, 103011); Rytov 1953; Saulson 1990; Schnakenberg 1976; Shayegan et al. 2023 (Nat. Photon.); Shitara & Ueda 2016 (PRA 94, 062316); Smirne & Bassi 2015; Spietz, Lehnert, Siddiqi & Schoelkopf 2003 (Science 300, 1929); Srivastava 2021 (arXiv:2008.05546); Stinespring 1955; Sz.-Nagy 1953; Titchmarsh 1937; Toyabe et al. 2010 (PRL 104, 198103); Twiss 1955; van der Schaft 2021 (arXiv:2010.04213); Wiener 1933; Wigner & Yanase 1963; Willems 1972; Yaida 2019 (ICLR); Yunger Halpern, Faist, Oppenheim & Winter 2016 (Nat. Commun. 7, 12051); Zames 1966; Zanardi & Rasetti 1997; Zemanian 1965; Zhu & Fan 2014 (PRB 90, 220301).
