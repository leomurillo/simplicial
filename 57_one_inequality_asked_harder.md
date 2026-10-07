# 57 — One Inequality, Asked Harder: A Synthesis of the Port Program, a Modeling Grammar, and a First Lecture

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*First draft — October 2, 2026*

<!--
INTERNAL LOG — NOT FOR PUBLICATION (pandoc drops HTML comments)
2026-10-02 v0.1.  Request (Leo): "Analyze the progress, think big and synth the principles and close the gaps.  We are on to
something so big that can be expressed so small.  Can we now model any system?  Can you distill the physics unification?
And how would you explain it to a junior physics student."  This paper is the synthesis (Sections 1-3), the modeling answer
(Section 4), the lecture (Section 5) and the gap ledger (Section 6).  The gaps closed in this round landed in the papers they
belong to: PortPrinciple.md v3.3 (Remark 7.3 corrected; Lemma 7.4a, Theorem 7.4, Proposition 7.5, Open Problem 7.6;
Proposition 11.2; echo labeling; Appendix A repair), Paper 55 draft 2 (Theorem 3.8 storage order; Theorem 6.6 + Lemma 6.7
closing O2; Section 7.1 correction), Paper 56 (Section 4.3: the matter half at 60 digits).
Certificates of this round: P9 7/7, P10 5/5 (run 3), p55b 9/9 (run 2), p56c 8/9 (K_eta failed, retained), p56d (IR
post-diagnosis, not blind: flat overshoot at R = 12 down 6.5% when R_max 26 -> 36, mass ratio 0.762 -> 0.772), p57 8/8 (run 2).

PEER PASS (feedback on the corpus, 2026-10-02; "process with open mind, have backbone").  Dispositions:
  1 "Definitive no-go theorem: weights cannot gravitate; combinatorial rewiring is mathematically proven the sole mechanism."
    REJECTED as stated.  Exact: lattice Weyl covariance at conformal coupling (56 Cor 2.2-2.3), vacuum stationarity
    (56 Prop 2.6).  Numerical: the 4-9% volume term on finite lattices (two runs formally inconclusive or gate-missed).
    Nothing excludes other mechanisms.  Kept as numerics + structural explanation (Section 3.4 here).
  2 "Division-of-labor theorem: causality and gravity live on disjoint tiers."  REFINED.  Not disjoint: the cone needs the bond
    star's directions (A = sum w delta delta^T); G = a_cell/(4 eta_b) depends on the weights through eta_b.  The true division:
    weights fix the constants (c, G); combinatorics carries the curvature.  Landed in 56 Sec. 5.1.
  3 "Passivity is the single universal axiom; thermodynamics, causality, quantum geometry and GR are exact shadows."  REFINED.
    Each law needs a named test with stated hypotheses (Port Sec. 3); GR is conditional.  The strongest true statement is
    Section 3.1 here.
  4 "Bekenstein completely demystified; neither quantum gravity nor horizons."  PARTLY ACCEPTED: the finite inequality is
    relative-entropy positivity against a KMS state (Casini; 54 Thm 4).  The step Delta K <= 2 pi R E stays [A] (energy
    density is not pointwise positive).
  5 "Locking IS the FDT for spacetime; Einstein = static FDT; unlocked = testable QG signatures."  KERNEL ACCEPTED as a reading:
    the causal metric is read by pushing, the entropic by watching; for weights both are functions of one operator (56 Thm 2.1),
    hence locked (Weyl covariance), hence no Jacobson term from weights.  REJECTED: "Einstein = static FDT" (the equilibrium
    condition is first order, the static FDT second order; they are two faces of one equilibrium); unlocked spacetime =
    Eling-Guedens-Jacobson nonequilibrium corrections (credited); "testable QG signatures" [C].
  6 "Gravity is the nonequilibrium relaxation current of graph topology."  REJECTED: static fields are equilibrium
    configurations; it also contradicts item 5.  A rewiring dynamics would be a relaxation (detailed balance) toward entanglement
    equilibrium, [C] (56 O3).
  7 "Spatial geometry and work are dual projections of network homology; Port Remark 3.4 is false; holographic principle."
    REJECTED, kernel accepted: Prop 6.9e mislabeled the echo exponent as a time-lift quantity (fixed in Port v3.3).  Remark 3.4
    (logical independence) stands.  The spacing module M of a ledger is not the cycle lattice H_1 of a network (5-ring:
    b_1 = 1, rank M = 2); 55 Sec. 7.1, whose fenced sentence invited the conflation, corrected.
-->

---

## Abstract

The Port Principle and its companion papers (54–56) build physics from one constraint: *no port gives more than it takes*. This paper distills what they establish, says exactly what is and is not unified, turns the result into a modeling grammar, and gives a first lecture for students.

**The constraint has three faces.** Outgoing waves never exceed incoming waves; the response function is positive-real; relative entropy to a passive reference state is nonnegative.

**The laws arise by asking it harder.** Each test below exposes one law:
- at every input, a lossless ledger (unitary dilation);
- at every instant, causality;
- on every number of copies, temperature and the fluctuation–dissipation theorem, which says that at equilibrium watching a system determines how it responds when pushed;
- under a symmetry, chemical potentials. For non-commuting charges and states without orientation, only central charges carry them;
- across every cut of a network, the area law;
- with two kinds of storage on a network, the light cone. It is present exactly when one storage is ultralocal and the other gradient;
- conditionally, at first order around equilibrium at every ball, Einstein's equation, with the network's bond count as the dynamical variable.

**A second axis orders the consequences.**
- The inequality itself gives the second law, the Bekenstein inequality and the area law.
- Its first-order equality face gives the first laws, Clausius's relation and entanglement equilibrium.
- Its second-order curvature gives the Fisher metrics, the fluctuation–dissipation theorem and stability.

**What follows exactly, and what conditionally.** Thermodynamics, information geometry, causality, and the existence of light cones and area laws follow exactly. Gravity follows conditionally. Its geometric half is certified numerically in $2+1$ and $3+1$ dimensions. Its matter half is certified here in $2+1$ at 60 digits: a disclination is a point mass whose value is independent of the ball radius to within $3$–$7\%$ (two box sizes), at $0.76$–$0.77$ of the continuum prediction. Nothing here computes a constant of nature, the dimension of space, or the matter content. The principle fixes the shape of laws, not their inputs.

**As a modeling grammar** it covers linear and nonlinear systems, classical and quantum ones, memoryless and memory-bearing ones, and passive and, by enlarging the boundary, active ones; we state its limits.

**Gaps closed in this round** (in the papers where they belong):
- a converse that the Port paper had credited to the literature for non-commuting charges, now corrected and proved for states without orientation;
- the nonlinear modeling calculus;
- the storage-order theorem;
- the least lattice with fourth-order isotropic dispersion (fourteen bonds);
- the multiprecision matter test of gravity on cones.

---

## 1. One inequality, three faces

A **port** is a boundary through which a system exchanges energy, or another conserved quantity, and at which that exchange can be both driven and observed (PortPrinciple.md, §2). The one constraint has three faces. They are equivalent where their settings overlap, and each is the natural form in one community.

- **Waves (engineering).** In incoming and outgoing wave variables, $b=Sa$ with $\|Sa\|\le\|a\|$: the absorbed power $\|a\|^2-\|b\|^2$ is nonnegative (PortPrinciple.md, Definition 2.2, Proposition 2.3).
- **Response (circuits and materials).** The impedance is positive-real, $\operatorname{Re}Z(s)\ge0$ for $\operatorname{Re}s>0$, the Cayley transform of a contraction.
- **States (thermodynamics and information).** $D(\rho\|\sigma)\ge0$, with equality iff $\rho=\sigma$, where $\sigma$ is the passive reference. For a Gibbs reference, $D(U\sigma U^\dagger\|\sigma)=\beta W\ge0$ is Kelvin's second law at a port (PortPrinciple.md, Corollary 6.13). The same gap is the Fenchel–Young gap of the one functional $\Phi=\log Z$ (Paper 54, Theorem 1).

Applied to processes, the third face becomes monotonicity: $D(\Phi(\rho)\|\Phi(\sigma))\le D(\rho\|\sigma)$ for every channel $\Phi$. Every channel is a contraction of distinguishability, because every channel is a unitary on a larger ledger followed by forgetting (Stinespring).

*Prior art.* The positivity and monotonicity of relative entropy are among the most powerful tools of modern quantum field theory and quantum information (Lindblad 1975; Uhlmann 1977; Casini 2008; Wall 2012; Ceyhan–Faulkner 2018; Witten 2018). The program's contribution is not the inequality. It is:
- the *port* as its carrier, a boundary of any kind, with or without an observer;
- the *lift calculus*, which says which operation on the constraint exposes which law (PortPrinciple.md, §3);
- the *network layer* (Papers 55–56): cones, cuts and bond-count gravity;
- finite exact proofs with certificates that keep their failures.

---

## 2. Seven tests, three orders

Two operations organize everything. A **test** strengthens the constraint by enlarging what it must survive. Restricting the admissible processes, instead, weakens the demand and enlarges the free family. An **order** expands the constraint around its equality point. The zeroth order is the inequality, the first is the vanishing of its first variation, and the second is its curvature.

**Table 1. What each test exposes, by order.** Tiers: [P] proven (finite and exact, or a cited theorem); [A] structural or conditional; numerics are labelled.

| Test | 0th order: the inequality | 1st order: the equality face | 2nd order: the curvature face | Where |
|---|---|---|---|---|
| **every input** (base) | contraction ⇒ lossless ledger (unitary dilation); Wiener: point spectrum echoes, continuous spectrum forgets | losslessness ⟺ rotations between two conjugate storages (Foster's LC tanks) | defect Gram $\succeq0$, independent of the ledger; Pick matrices | Port Thms 4.1, 4.5, Prop 4.4; 55 Prop 3.7; 53 Lemma 3.2 [P] |
| **every instant** (time) | causality | Kramers–Kronig | parity defect $\|\operatorname{Re}\hat f\|^2-\|\operatorname{Im}\hat f\|^2=2\pi\langle f,\mathcal Rf\rangle$ | Port Thms 5.1, 5.4 [P] |
| **every number of copies** | the Gibbs state is the only completely passive state; zeroth law; at finite $n$, thresholds are simplest fractions, $n^*\asymp(T/\Delta T)^{1/r}$ | Gibbs variational principle; $\Phi=\log Z$ generates the free states; first law of entanglement $\delta S=\delta\langle K\rangle$ | static FDT: $\nabla^2\Phi$ = covariance = response = Fisher; Petz metrics = self-dual RL networks; coth law | Port Thms 6.3, 6.6, 6.9–6.11; 54 Thms 1–2 [P] |
| **restricted processes** (symmetry) | one chemical potential per conserved charge; non-commuting charges and no orientation: central charges only | Noether: Kirchhoff's current law is the Noether identity of the potential shift | charge susceptibility = charge covariance | Port Thms 7.2, 7.4; 55 Prop 2.3 [P] |
| **every cut** (composition) | $I(A{:}B)+D=\beta(\langle H_\partial\rangle_{\rho_A\otimes\rho_B}-\langle H_\partial\rangle_\rho)$ ⇒ cut law ⇒ area law on local networks; Bekenstein's inequality as passivity of a KMS state | capacity across a cut = min cut | Kron reduction preserves positive-realness | 55 Thms 2.2, 4.2, 4.4; 54 Thm 4 [P] |
| **two storages on a network** | passive stiffness ⇒ Lorentzian $(1,d)$ symbol; gain = a second timelike direction | $\omega^2=\hat A\hat B$; a cone iff one storage is ultralocal and the other gradient | isotropy order by order (fourteen bonds to fourth order) | 55 Thms 3.5, 3.8, 6.6 [P] |
| **geometry as a port** | no global passive state: gravity is where local ports fail to glue | entanglement equilibrium at every ball ⇒ Einstein's equation; dynamical variable = bond count; $G=a_{\rm cell}/(4\eta_b)$ | second variation = Fisher = canonical energy (stability) | 56 §§4–5 [A, conditional]; geometric half [numerics]; matter half at 60 digits (§6) |
| *away from equality* | the arrow: watching minus pushing; static defect linear in the current | quantum Harada–Sasa: first moment of the total violation $=\|\mathcal A_f\|^2_{\rm HS}$ | total violation $\ge0$ at every frequency | 54 Thms 3, 3Q, 3H, 4.7; Port Thm 10.1 [P] |

Two joins connect the rows. Base and copies give *noise = temperature × defect Gram*, for passive and active ports alike (PortPrinciple.md, Theorems 8.1–8.2). Base and symmetry give the *port–charge table*: a port flips only what it can supply and dephases only what it can read (Theorems 9.1, 9.3).

**Reading the table [A].** Down a column, the tests get harder and the laws get stronger. Across a row, the expansion goes deeper. In the copy row, the first-order face is the first law and the second-order face is the fluctuation–dissipation theorem. In the geometry row, the first-order face is Einstein's equation (Jacobson 1995, 2016) and the second-order face is the stability of the equilibrium (Lashkari–Van Raamsdonk 2016). So Jacobson's "equation of state" and the static FDT are the first- and second-order faces of one equilibrium. They are not the same statement.

---

## 3. The distillation

### 3.1 The statement

> **Physics, as far as these papers reach, is the theory of what passive ports cannot do.** One inequality — no port gives more than it takes — asked under stronger tests and expanded around its equality point yields:
> - unitarity (every input);
> - causality (every instant);
> - temperature and the fluctuation–dissipation theorem (every number of copies);
> - chemical potentials (processes restricted by a symmetry);
> - the area law (every cut);
> - the light cone (two kinds of storage on a network, one on the nodes and one on the links);
> - and, conditionally, Einstein's equation (balance at every cut, with the network's bond count as the dynamical variable).

That is the small expression. It is a statement about the *shape* of laws, and §3.3 lists the inputs it does not supply.

### 3.2 The second slogan: watching and pushing

There are two experimental ways to learn about a system: watch it, or push it. The FDT family says that at equilibrium the two agree:
- frequency by frequency (Callen–Welton, Kubo);
- in every quantum Fisher metric, each a filter on one dissipation spectrum (PortPrinciple.md, Theorem 6.10);
- statically, as one Hessian (Paper 54, Theorem 2).

Away from equilibrium the gap between them is the arrow of time. It is linear in the stationary current, and its total is nonnegative at every frequency (Paper 54, Theorems 3, 4.7).

Space has the same two readings. The *causal* metric is read by pushing: it is the support of the retarded response, set by the weights ($c=1/\sqrt{LC}$). The *entropic* metric is read by watching: it is the entanglement of vacuum fluctuations, counted in bonds. For the weights the two cannot be separated, because every entanglement entropy and the propagator are functions of one operator (Paper 56, Theorem 2.1). A weight deformation therefore moves both together. That is the lattice Weyl covariance which keeps weights from producing Jacobson's term at a fixed proper cutoff. A combinatorial defect does separate them, by changing the count of bonds at fixed cell size. Entanglement equilibrium is the condition that geometry absorbs the separation, and that condition is the Einstein equation in bond units [A].

### 3.3 What is unified, and how firmly

| Domain | Status | Where |
|---|---|---|
| second law, temperature, zeroth law, Landauer, Carnot, copy thresholds | exact [P] | Port §§6, 8 |
| fluctuation–dissipation (classical, quantum, every Petz metric), noise, Johnson–Nyquist, Caves | exact [P] | Port §§6, 8; 54 §§3–4 |
| information geometry (Fisher, Kubo–Mori, data processing), the cumulant tower | exact [P] | Port Thm 6.11; 54 §5 |
| causality, dispersion, Kramers–Kronig | exact [P] | Port §5 |
| reversible completion of irreversible processes; echo or forget | exact [P] | Port §4 |
| chemical potentials (commuting charges; non-commuting without orientation) | exact [P] | Port §7 |
| modeling: interconnection, reduction, noise assignment, stability, nonlinear and memory baths | exact [P] | Port §11 |
| area law (as a cut law), information capacity across cuts, the finite Bekenstein inequality | exact [P] | 55 §4; 54 Thm 4 |
| the light cone's existence and its placement law; Maxwell's vacuum as a network | exact [P] | 55 §3 |
| gravity: Einstein's equation by entanglement equilibrium, with combinatorial dynamics | conditional [A]; numerics | 56 |

**Not unified, and not derived:**
- **the Hilbert-space structure.** Dilation theorems assume it. Reconstructing quantum theory needs further axioms (Chiribella–D'Ariano–Perinotti 2010).
- **the constants.** $c$ comes from the weights ($A/C$) and $G$ from the entanglement per bond and the cell area ($a_{\rm cell}/4\eta_b$). The program computes neither number. $\eta_b$ grows with the number of fields (the species problem).
- **the dimension of space.** It is the rank of the bond star, an input (Paper 55, §6).
- **the matter content**: gauge groups, masses, couplings.
- **the past hypothesis**: why reference states are passive.
- **single outcomes**: which branch a port is on.
- **global gravity**: there is no global passive state, because heat capacity is negative and energy is unbounded below. The principle locates gravity where local passive ports fail to glue, but does not remove the failure.

### 3.4 What we do not claim

- *That passivity alone implies the laws.* Each law needs a named test with stated hypotheses: linearity, additivity over copies, stationarity, finite dimension, locality, thermal hidden ports (PortPrinciple.md, §3).
- *That a theorem forbids weights from gravitating.* What is exact is lattice Weyl covariance at conformal coupling and the vanishing of the vacuum's first-order modular energy (Paper 56, Corollaries 2.2–2.3, Proposition 2.6). The small volume term, $4$–$9\%$ of Jacobson's target, is a numerical finding on finite lattices, two of whose runs were formally inconclusive.
- *That causality and gravity live on disjoint tiers.* The cone needs the directions of the bond star, and $G$ depends on the weights through $\eta_b$. The precise division of labour is that weights fix the constants and combinatorics carries the curvature.
- *That Bekenstein's bound is demystified outright.* The finite inequality is relative-entropy positivity against a KMS state (Casini 2008; Paper 54, Theorem 4). The step $\Delta K\le2\pi RE$ needs positive energy density, which fails pointwise in quantum field theory, so it stays [A].
- *That gravity is a nonequilibrium current.* Static fields are equilibrium configurations of the first-order balance. Departures from local equilibrium give corrections of the Eling–Guedens–Jacobson (2006) type.
- *That the ledger's arithmetic and a network's loops are one object.* The copy lift and the ledger's recurrence share the module of level spacings (PortPrinciple.md, Proposition 6.9e). The arrow and gauge holonomy live on the cycle lattice $H_1$ (Paper 55, §§5, 7.1). These are different lattices: a five-node ring has $b_1=1$ but spacing rank 2.

---

## 4. Can we now model any system?

**Yes in form, no in content.** Any physical system that has a passive reference somewhere inside its boundary can be written in the port grammar. That includes every driven system once its drivers are drawn inside the boundary (PortPrinciple.md, Definition 2.5). The grammar then fixes how the system may behave. It does not supply the system's numbers. It is a universal grammar, not a universal dictionary.

**Inputs (what the modeler must supply).**
1. *Storages* $H$: two conjugate kinds per lossless mode, each placed ultralocally or across links.
2. *Interconnection* $J$: Kirchhoff's laws, a Dirac structure.
3. *Losses* $R$, each with its temperature: one per bath port.
4. *Ports to the outside*, with every non-passive source drawn inside the boundary.
5. *Conserved charges*: the symmetry of the admissible processes.

**Outputs (what the grammar then determines).**
- dynamics;
- noise: $\theta R$ on every loss, plus the drift correction $\theta\nabla\!\cdot\!M^{\mathsf T}$ when the loss depends on the state (PortPrinciple.md, Proposition 11.2);
- stationary states: Gibbs, generalized Gibbs, or a steady current on the cycle space;
- causal structure: a cone exactly for the placement "one ultralocal, one gradient" (Paper 55, Theorem 3.8), with dispersion and Kramers–Kronig;
- stability: stored energy as a Lyapunov function, and passive feedback loops are stable;
- admissible reductions: compression and Kron reduction;
- information limits: capacity across a cut;
- thermodynamic prices: Landauer at resets, the Carnot window, copy thresholds;
- protection rules: supply and read.

**Coverage.**
- linear and nonlinear systems (Propositions 11.1–11.2);
- classical and quantum ones (Lindblad dynamics with quantum detailed balance in the metric that the push selects; Paper 54, §4.1);
- memoryless baths and baths with memory (Foster's oscillator realization of the bath port, which is the Ford–Kac–Mazur/Caldeira–Leggett model);
- fields (Levin's direct approach, Rytov's electrodynamics, Maxwell's vacuum as an LC network);
- chemistry (concentrations as storages, reactions as losses, chemostats as sources);
- active matter (a pump inside the boundary, priced by the gain branch of the noise formula);
- information processing (resets versus channels);
- spacetime, conditionally (Paper 56).

**Limits.**
- *It needs a passive reference.* For global self-gravitating systems there is none, and the grammar constrains only local pieces.
- *It does not supply the inputs:* $H$, $R$, the network, and the constants come from measurement or a deeper theory.
- *Far from equilibrium*, the linear filter tables give way to fluctuation theorems and the fluctuation–response inequality. The constraints still hold; the closed forms do not.
- *Strongly nonlinear quantum dynamics* beyond the Markov or Gaussian regime keeps the constraints (passivity, data processing) but not the closed-form calculus.
- *It says nothing about which outcome occurs.*

**Table 2. The grammar at work.**

| System | Storages (placement) | Losses | Ports and charges | What the grammar delivers |
|---|---|---|---|---|
| coaxial line | $C'$ on nodes, $L'$ on links | series $R'$, shunt $G'$ at $T$ | two ends | $v=1/\sqrt{L'C'}$, $Z=\sqrt{L'/C'}$, attenuation, Johnson noise, Kramers–Kronig, capacity |
| interferometer mirror | mass, elastic modes | internal friction (loss angle) at $T$ | the readout beam | thermal noise by pushing with the readout's own profile (Levin) |
| transmon qubit | capacitance, nonlinear Josephson inductance | dielectric and quasiparticle loss | charge (U(1)); drive | $T_1$ from the charged sector, $T_\phi$ from the neutral sector, protection by gapping and blinding |
| molecular motor | rotor and elastic linkers; chemical potential inside the boundary | viscous friction | ATP port | efficiency from the FDT violation (Harada–Sasa) |
| spin ensemble | Zeeman storage; non-commuting charges | relaxation baths | collective couplings | with no orientation, only central chemical potentials (Port Thm 7.4) |
| two-bath engine (qubits or ion modes) | level ladders | two baths | joint unitaries | copy threshold or process order from the Carnot window (Port §6) |
| electromagnetic vacuum | $\varepsilon_0$ ultralocal, $\mu_0$ curl–curl | radiation into the continuum | antennas | $c=1/\sqrt{\mu_0\varepsilon_0}$, $Z_0=376.73\ \Omega$, radiation resistance, blackbody noise by the FDT |
| chemical reaction network | concentrations | reactions | chemostats; conservation laws as charges | generalized Gibbs states, steady currents on cycles, the uncertainty relation for unicyclic cases |
| spacetime [A] | bond weights; bond counts | — | — | Einstein's equation by equilibrium; $G=a_{\rm cell}/4\eta_b$ |

---

## 5. A first lecture (for a junior physics student)

*Everything you will learn in physics happens at boundaries.* A battery's terminals, your eardrum, a cell membrane, a telescope's aperture, the surface of a star: each is a place where energy goes in or comes out, where you can push the system and watch what it does. Call such a place a **port**. This lecture is about one rule for ports, and how much physics comes out of asking it carefully.

**The rule.** *No port gives back more energy than it received.* A resistor, a spring, a pane of glass: none of them can hand you net energy over a cycle unless something inside is already charged up — a battery, a pump, a fuel. If you see a port giving more than it takes, redraw the boundary to include the hidden battery, and the rule holds again. That is just Kelvin's version of the second law, applied at a boundary.

**First consequence: a resistor hisses.** A resistor turns electrical energy into heat. Because it can absorb, it also emits: its electrons jiggle, and an ideal voltmeter across it sees noise. Nyquist showed in 1928 that the noise is $\sqrt{4k_BTR}$ per root hertz. For $1\ \mathrm{k\Omega}$ at room temperature that is about $4\ \mathrm{nV}/\sqrt{\mathrm{Hz}}$, and it limits every sensitive amplifier. The deep statement: *what you see when you watch the resistor (its noise) is fixed by what happens when you push it (its resistance).* That is the fluctuation–dissipation theorem, and it comes from asking the rule of many copies at once. If you could gang up enough copies of a non-thermal object to extract work, the rule would fail; the only states that survive every number of copies are thermal ones, with one temperature. That is *why temperature exists.*

**Second consequence: effects come after causes.** If the rule must hold at every instant, not just on average over a cycle, the response cannot start before the push. From that alone, Kramers and Kronig showed that how a material absorbs light fixes how it bends light. A prism separates colours *because* glass absorbs ultraviolet.

**Third consequence: waves need two kinds of storage.** A capacitor stores energy in its electric field; an inductor stores it in its magnetic field. Join one of each and the energy sloshes back and forth: an oscillation, a rotation between two storages. Now build a ladder: capacitors from each node to ground, inductors along the rungs. A pulse travels down it at speed $1/\sqrt{LC}$ per unit length. A real coaxial cable has about $250$ nH and $100$ pF per metre. So signals travel at $1/\sqrt{(2.5\times10^{-7})(10^{-10})}=2\times10^8$ m/s, two thirds of the speed of light, and the cable's impedance is $\sqrt{L/C}=50\ \Omega$. You will find "50 Ω" printed on every lab cable.

Empty space is such a ladder too. Its capacitance per metre is $\varepsilon_0$ and its inductance per metre is $\mu_0$. Its wave speed is $1/\sqrt{\mu_0\varepsilon_0}=299\,792\,458$ m/s, the speed of light, and its impedance is $\sqrt{\mu_0/\varepsilon_0}\approx377\ \Omega$. That is what Maxwell found in 1865: light is the ladder's wave. Now play with the ladder:
- Replace the inductors by resistors, so there is one storage plus loss. Pulses no longer travel; they *spread*, like heat in a rod. Diffusion has no speed limit.
- Let *both* storages couple neighbours. You get an equation whose waves get faster the shorter they are: Schrödinger's equation, which has no speed limit of its own.
- One storage on the nodes and one on the links is exactly the arrangement with a finite speed and a light cone.

Relativity's speed limit is a statement about where the two storages sit.

**Fourth consequence: conserved quantities get "prices".** If the processes you can perform must conserve electric charge, or particle number, then states with a definite chemical potential become just as "free" as thermal states. Every conserved charge adds one price, one chemical potential. One surprise is worth remembering. For rotations, which do not commute, a state with no preferred direction cannot carry a "price" for angular momentum. Only the total spin, the part that does not care about direction, can be watched without disturbing anything.

**Fifth consequence: information through a boundary is limited by the boundary.** Cut a network of ports in two. The information shared across the cut is bounded by the energy stored in the bonds you cut: the more bonds, the more information. In a network where every bond is short, the number of cut bonds is the *area* of the cut. Hence area laws, and hence the famous scaling of black-hole entropy with horizon area, rather than volume. The same reasoning, plus one physical step about where the energy sits, gives Bekenstein's inequality, $S\le2\pi RE/\hbar c$. It says that a thermal reference state cannot be beaten (Casini 2008).

**Sixth consequence (the frontier): gravity as balance.** Suppose the network can rewire itself, adding or removing bonds, so that every small region stays in balance: its entanglement does not change to first order when matter and geometry change together. Jacobson showed in 2016 that this balance condition is Einstein's equation. On a network, the papers find, what must change is the *number* of bonds, not their strength. Strengths set the constants: they make light fast and gravity weak. A missing wedge of bonds, a cone, behaves like a point mass. This last part is still being tested. The geometric half works numerically to $85$–$99.9\%$. The matter half agrees in form, giving a definite mass, but at about three quarters of its predicted value on the lattices tried.

**What the rule does not tell you.** It does not tell you the values of the constants, why space has three dimensions, which particles exist, why the universe started with low entropy, or why a measurement gives this outcome rather than that one. It tells you the *shape* every law must have. Those other questions remain open.

**Exercises.**
1. Compute the Johnson noise of $1\ \mathrm{k\Omega}$ at $300$ K. (*Answer:* $\sqrt{4\cdot1.380649\times10^{-23}\cdot300\cdot1000}=4.07\times10^{-9}$ V$/\sqrt{\rm Hz}$.)
2. A coaxial cable has $L'=250$ nH/m and $C'=100$ pF/m. Find its wave speed and impedance. (*Answer:* $2\times10^8$ m/s and $50\ \Omega$.)
3. Show that $1/\sqrt{\mu_0\varepsilon_0}$ is the speed of light and $\sqrt{\mu_0/\varepsilon_0}\approx376.73\ \Omega$.
4. What is the least heat released when one bit is erased into a bath at $300$ K? (*Answer:* $k_BT\ln2=2.87\times10^{-21}$ J $\approx0.018$ eV.)
5. Two qubits at temperatures $10\%$ apart have gap ratio $\tfrac12$ (one gap twice the other). How many copies are needed before any joint operation extracts work? And for gap ratio $1/\varphi$? (*Answer:* $11$ and $3$: the least denominators of fractions inside the "Carnot window" $(x,1.1x)$; PortPrinciple.md, Table 6.1.)

---

## 6. The gap ledger

### 6.1 Closed in this round

| Gap | Resolution | Where | Certificate |
|---|---|---|---|
| non-Abelian converse credited to the literature | The cited works prove a statement with reference frames and charge batteries. The strict statement is proved here for states without orientation (only central charges carry chemical potentials). Exact witnesses show that oriented non-thermal states are activated. The general strict converse is stated as Open Problem 7.6, with a reference-frame reduction. | Port Remark 7.3, Lemma 7.4a, Theorem 7.4, Proposition 7.5, Open Problem 7.6 | P9 7/7 (Part A blind) |
| modeling beyond linear | divergence drift; several temperatures; memory baths as Foster ports, with Kubo's second FDT | Port Prop 11.2 | P10 5/5 (run 3; two checker failures retained) |
| why two storages, and where | the cone iff one storage is ultralocal and one gradient; Schrödinger = both gradient; Maxwell's vacuum | 55 Thm 3.8 | p55b S1–S4 |
| fourth-order isotropy (55 O2) | at least seven bond pairs in 3D (six would be icosahedral); sc + bcc at $8{:}1$ attains it | 55 Thm 6.6, Lemma 6.7 | p55b I1–I5 (run 2 9/9; run-1 checker artifact retained) |
| matter half of the 2+1 point-mass law (56 O2) | At 60 digits the apex weight is $1.11$–$1.21\times$ Bisognano–Wichmann at $R_{\max}=26$ and $1.09$–$1.13\times$ at $R_{\max}=36$; the growth with $R$ is mostly infrared. $M=-\delta S/\beta(0)$ is independent of $R$ to $3.4\%$ and $6.6\%$ ($R=6$–$12$). Its value is $0.76$–$0.77\times\eta\delta c/2\pi$ in both boxes (pre-registered band $[0.8,1.25]$ missed and retained). | 56 §4.3 | p56c 8/9; p56d (box size, not blind) |
| debts | echo exponent mislabeled as a time-lift quantity (Port); backslash-mangled LaTeX in Port Appendix A; the cycle lattice conflated with the spacing module (55 §7.1) | Port v3.3; 55 draft 2 | p57 A2 |

### 6.2 Open, ranked by consequence

1. **Gravity, matter half and dynamics.** (a) The value $0.76$–$0.77$, stable when the box grows: do the lattice factors (modular-weight overshoot, digital geometry, entropy per bond) tend to 1 in the continuum, or is the mass renormalized? (b) The $3+1$ cosmic string at multiprecision; the same dihedral reduction applies to the prism. (c) Networks of hinges. (d) A passive rewiring dynamics that locks the weights to the combinatorics (56 O3).
2. **The strict non-Abelian converse for oriented states** (Port Open Problem 7.6). It needs a quantitative frame lemma for frames made of the state itself.
3. **Dimension.** No passivity criterion selects the rank of the bond star (55 O3).
4. **Constants.** None is computed. The relation $G=a_{\rm cell}/4\eta_b$ trades Newton's constant for the entanglement per bond and the cell area. Both depend on the field content.
5. **Copy thresholds** beyond three levels: exact values, and the distribution of $n^*\delta^{1/r}$ (Port Remark 6.9f).
6. **Experiments.** Copy thresholds on ion or superconducting platforms (Port falsifier 9). Shot-noise coth thermometry. FDT-violation calorimetry of motors. Kirchhoff violation per port in non-reciprocal emitters.

---

## 7. Certificate

`empirical/synthesis57/p57_synthesis_audit.py` (falsifiers in its docstring, written before the first run):
- **L1–L6** check every number in the lecture: Johnson noise, Landauer, the coaxial line, the vacuum's $c$ and $Z_0$, the Pendry–Bekenstein rate, the two copy thresholds, and the D3Q15 identity. The checks use exact rational arithmetic, or CODATA-exact constants.
- **A1** audits that every theorem label cited here exists, bold, in its manuscript.
- **A2** audits the touched manuscripts for control characters and checks that the word "headline" does not occur in the body of the Port paper.

*Runs.* Run 1 passed 7/8. L2 failed on a pre-registration transcription error: the eV value of Landauer's bound was written as $0.017918$ instead of $0.017919$, and missed its $5\times10^{-5}$ tolerance by $6\times10^{-6}$. The failure is retained. Run 2 passed 8/8, not blind for L2. The logs are in the same directory.

---

## References

- J. J. Bisognano, E. H. Wichmann, *J. Math. Phys.* 16 (1975) 985.
- H. Casini, Relative entropy and the Bekenstein bound, *Class. Quantum Grav.* 25 (2008) 205021.
- F. Ceyhan, T. Faulkner, Recovering the QNEC from the ANEC, *Commun. Math. Phys.* 377 (2020) 999 (arXiv:1812.04683).
- G. Chiribella, G. M. D'Ariano, P. Perinotti, Probabilistic theories with purification, *Phys. Rev. A* 81 (2010) 062348.
- C. Eling, R. Guedens, T. Jacobson, Nonequilibrium thermodynamics of spacetime, *Phys. Rev. Lett.* 96 (2006) 121301.
- T. Jacobson, Thermodynamics of spacetime: the Einstein equation of state, *Phys. Rev. Lett.* 75 (1995) 1260; Entanglement equilibrium and the Einstein equation, *Phys. Rev. Lett.* 116 (2016) 201101.
- N. Lashkari, M. Van Raamsdonk, Canonical energy is quantum Fisher information, *JHEP* 04 (2016) 153.
- G. Lindblad, Completely positive maps and entropy inequalities, *Commun. Math. Phys.* 40 (1975) 147.
- J. C. Maxwell, A dynamical theory of the electromagnetic field, *Phil. Trans. R. Soc.* 155 (1865) 459.
- H. Nyquist, Thermal agitation of electric charge in conductors, *Phys. Rev.* 32 (1928) 110.
- A. Uhlmann, Relative entropy and the Wigner–Yanase–Dyson–Lieb concavity, *Commun. Math. Phys.* 54 (1977) 21.
- A. C. Wall, A proof of the generalized second law for rapidly changing fields and arbitrary horizon slices, *Phys. Rev. D* 85 (2012) 104049.
- E. Witten, Notes on some entanglement properties of quantum field theory, *Rev. Mod. Phys.* 90 (2018) 045003.
- Program: PortPrinciple.md (v3.3); Paper 53; Paper 54 (draft 4); Paper 55 (draft 2); Paper 56; their certificates in `empirical/`.
