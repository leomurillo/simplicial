<!--
================================================================================
INTERNAL LOG — NOT FOR PUBLICATION (Pandoc drops HTML comments)

  v1 (2026-09-29): spine. Backup: archive/duplicates/PortPrinciple-v1.md.
  v2 (2026-09-29): folded a critical-collaborative review (quantifier structure;
      symmetry as a restriction that enlarges the free family; Wiener; Petz/WYD
      filters; active-port boundary rule; non-Abelian Schur table; parity defect
      for arbitrary kernels; H ∝ I edge case). Backup: archive/duplicates/PortPrinciple-v2.md.
  v3 (2026-09-29): folds a peer review + two results from a divergence pass.
    ACCEPTED (peer review)
      - Lift calculus made the formal spine: Def 3.1-3.2, Prop 3.3, Table 3.1. Title,
        abstract, and §1 reframed: every law here is forced by the constraint
        TOGETHER WITH a named lift or restriction, never by passivity alone.
      - "Two ways to learn anything" -> two fundamental EXPERIMENTAL modes (§1).
      - Snapshot/causality overreach narrowed to the exact Markov statement
        (Prop 10.2; §10 reading; one-liners 18-19).
      - Landauer: erasure vs communication separated (Prop 8.5; prohibition 5;
        §12; one-liner 4; Bennett added).
      - "Every finite environment has pure point spectrum" softened (Cor 4.6).
      - Effort-flow table split into exact realizations vs structural
        translations (§2.1; §11; §14; Appendix B).
      - Coth law: exact identity vs the settings where it is the operative kernel;
        general TUR not implied (Prop 6.14).
      - Noise wording: "set by the dilation defect"; defect Gram defined (Prop 4.4).
      - Symmetry-restriction thesis elevated (§1.1, §7 intro).
      - Architecture section placed after the abstract (old §17 condensed there).
      - Five-way status table: assumed / derived / imported / analogous / new (§1.3).
    FOLDED FROM THE DIVERGENCE PASS
      - Arithmetic of the graded copy lift: Lemma 6.2, Thm 6.6, Cor 6.7, Prop 6.8,
        Open Problem 6.9 (cert P5: H2.K2a-c, K2d-f).
      - Circuit reading of the Petz classification: Thm 6.11, Rem 6.12
        (cert P5: H3.K3a-b, K3c', K3d; K3c pre-registered failure retained).
    HELD: no peer point rejected. One refinement: the matrix noise law is kept as
      "temperature × defect Gram" with the Gram defined, because it is exact.
    Certificates: P1 21/22 (C4.a retained), P2 10/10, P3 17/17, P4 20/20,
      P5 11/12 (K3c retained; superseded by K3c'; its 2x2 witness had a +1e-9 I
      regularization making B - A marginally non-PSD -> exact K3e added, passes).
      The P5 file was split verbatim
      from p5_headline_candidates.py; the part not used here is in
      aux_probe_tilt_translation.py (3/4; K1c retained, superseded by K1d).
    2026-10-01 (v3.1)
      - Prior art landed: Sparaciari-Jennings-Oppenheim 2017 (k-activable, m+n upper
        bound, Carnot-window swap cycle), Salvia-Giovannetti 2020 (N-passivity criterion
        = Lemma 6.2 occupation form; Prop 1 fraction bracket; commensurate case),
        Linden-Popescu-Skrzypczyk 2010. Remark 6.6a positions Thm 6.6 as the exact
        answer to SJO's open minimality question.
      - Open Problem 6.9 -> Theorem 6.9 (resonance-rank law n* ~ (T/dT)^(1/r)),
        Cor 6.9a (k reservoirs: n* = min ||m||_inf; delta^(-1/k)), Cor 6.9b (triple
        reduction fails: exact d=4 example + Roth asymptotics), Rem 6.9c (open:
        closed form d>=4, intermediate ranks, a.e. spectra).
        Cert P6 6/6 (p6_copy_threshold_d4.py; K/L pre-registered before first run).
    2026-10-01 (v3.2)
      - Thm 6.9 generalized to every rank (badly approximable M; K-visible upper bound needs NO
        Diophantine condition; K-blind via quotient + Minkowski-Jarnik); Thm 6.9' almost every
        spectrum (exponent 1/(d-1), Borel-Cantelli); Rem 6.9'' oscillation for very well
        approximable ratios; Prop 6.8a near resonance (detuning caps the penalty / two-copy
        collapse); Cor 6.9c harmonic modes = process order k+m; Cor 6.9d a conserved charge
        raises the exponent; Prop 6.9e echo-yield duality y(e+1)=1 (Khinchin transference);
        platform estimates [A] (Table 6.1: harmonic / ion modes sqrt3 / golden; transmon; NV).
      - Certs: P7 4/6 (H7a, H7b pre-registered ceilings on finite-delta local exponents failed
        narrowly -- RETAINED; post-diagnosis P7b 3/3, P7c 2/2 test the theorem-level claims);
        P8 3/3. Lesson: pre-register asymptotics as bounded constants or slopes, not pointwise
        local exponents.
    2026-10-02 (v3.3) -- gap closures + a second peer pass ("process with open mind, have backbone")
      - DEBT FOUND AND FIXED: Remark 7.3 credited the non-Abelian converse to Guryanova et al. 2016, Yunger
        Halpern et al. 2016, Lostaglio-Jennings-Rudolph 2017.  Literature check (2026-10-02): those works prove the
        battery/reference-frame statement (work valued by H - mu.Q; Pusz-Woronowicz applied to H - mu.Q), and LJR
        show max-ent and charge-wise passivity disconnect.  The STRICT statement (energy the only work, cycles that
        commute with every total charge, copies only) is not proven there.  Remark 7.3 rewritten; Section 1.3 table
        and Section 14 corrected.
      - NEW Section 7 results: Lemma 7.4a (multiplicity form of strict passivity); Theorem 7.4 (invariant states:
        completely passive under strict symmetry iff Gibbs up to central chemical potentials -- non-central charges
        carry no chemical potential without orientation); Proposition 7.5 (strict activation of non-thermal,
        non-invariant states: exact rational witnesses); Open Problem 7.6 (general strict converse; reduction to the
        stabilizer by reference frames built from copies, [A]).  Cert P9 7/7 (Part A blind; Part B not blind,
        exploration in the scratchpad preceded it).
      - NEW Proposition 11.2 (nonlinear calculus: divergence drift; two temperatures; memory baths = Foster ports,
        second FDT).  Cert P10: run 1 N5 no verdict (sympy MemoryError), run 2 N5(a) checker bug (int division ->
        floats), run 3 5/5 (N5 not blind).  Both failures retained in its run log.
      - Prop 6.9e / abstract / Section 17 wording: the echo exponent belongs to the LEDGER (the base, read in time),
        not to the time lift (causality).  Remark 3.4 sharpened: the two lifts constrain different components and are
        logically independent; their quantitative readouts on one ledger share the spacing module.
      - Appendix A: two rows carried backslash-mangled LaTeX ("\t" -> tab, "\a" -> bell) from an earlier shell
        write; repaired.  New rows P9, P10.
      PEER PASS 2 dispositions (feedback on the program as a whole; items touching this paper):
        * "passivity is the single universal axiom; the laws are exact shadows" -- REFINED, not adopted: Section 3 says
          nothing is forced by passivity alone; each law needs a named lift with stated hypotheses.  The strongest
          true statement (one constraint, named operations, exact where proven) is made in Paper 57.
        * "Remark 3.4 is false within the framework (time and copy lifts read the same homology)" -- REJECTED with a
          kernel accepted: Remark 3.4 is about logical independence and stands; Prop 6.9e had mislabeled the echo
          exponent as a time-lift quantity (fixed).  The spacing module M of the ledger is not the cycle lattice H_1 of
          a network (5-ring: b_1 = 1, rank M = 2); Paper 55 Section 7.1 corrected accordingly.
        * "Bekenstein completely demystified" -- the finite inequality is Paper 54 Thm 4 (Casini's insight); the step
          Delta K <= 2 pi R E stays [A] because energy density is not pointwise positive.

    2026-10-01 pointer (internal only): Paper 54 (54_one_functional_from_passivity.md) builds the program's Phi = log Z
      on Thm 6.3 and gives a static, finite form of §10 (watch-push defect linear in the stationary current); no edit here.

  INTERNAL NOTE — candidate line for a SEPARATE paper (not part of this manuscript)
    "Probes measure tilts; interventions measure translations."
    - For activations x ~ p and a readout f: a linear probe measures
      Sigma^-1 Cov(x, f), the response to an exponential TILT of p (static FDT);
      activation patching/steering measures E[grad f], the response to a
      TRANSLATION. Exact identity: patch - probe = -E[f (s - s_G)], with
      s = grad log p and s_G the score of the Gaussian fit.
    - 1-D: gap(x^2) = -kappa3/kappa2; gap(x^k) = -kappa_{k+1}/kappa2 + terms in
      lower cumulants of order >= 3; probe = patch for every polynomial readout
      <=> Gaussian (Stein characterization). The gap is a PRODUCT: readout
      curvature × representation non-Gaussianity (zero for linear readouts under
      any distribution).
    - Evidence (aux_probe_tilt_translation.py): K1a, K1b exact; K1c pre-registered
      FAIL (near-linear MLP readout gave a 2.5% gap, below the 10% threshold;
      retained); K1d post-diagnosis: curved readout, identity within 2%, gaps
      52% / 166% / 281% with separation, probe ANTI-aligned with the causal
      effect at separation 3 (cos = -0.21).
    - Why it matters: an exact mechanism for "decodability is not causality"
      (arXiv 2609.18080 reports Spearman 0.10 between probe alignment and gradient
      sensitivity, empirically, with no mechanism). Welds to the Conductor Blind
      Spot / Faithfulness line: the probe is an order-2 instrument and the gap is
      the order >= 3 cumulant tower.
    - Prior art: the identity is classical (Stein; Brillinger's average
      derivative). Its use for the probe/intervention gap was not found
      (search 2026-09-29).
    - Next: Pythia test on GCP (torch never local): estimate directional cumulants
      along probe directions; compare probe and patching directions per feature;
      predict the gap from cumulants × readout curvature. Risks: score estimation
      in high dimension; realistic magnitudes unknown.
================================================================================
-->

# The Port Principle: One Passivity Constraint Lifted across Time, Copies, and Symmetry

**Leonardo Murillo Montero**

---

## Abstract

Every measurement, model, and machine interacts with the world through a *port*: a boundary at which a system can be both pushed and watched. We study one familiar constraint — *no port gives more than it takes*; in wave variables, outgoing never exceeds incoming — and ask what it forces when it is *lifted*. Demanded for every input, the constraint makes a port the corner of a lossless ledger, whose spectral type decides whether lost information echoes or is forgotten. Lifted to every instant, it forces causality. The resistive and reactive parts of a stable causal response then carry equal energy, and for any kernel the defect is its overlap with its own time reverse. Lifted to every number of copies, it forces the Gibbs state and the fluctuation–dissipation theorem. One dissipation spectrum then fixes every variance and every monotone quantum Fisher metric through frequency filters. The admissible filters are exactly those realized by self-dual resistor–inductor networks, and Petz's symmetry condition becomes detailed balance. The graded copy lift has an arithmetic of its own: the number of copies at which a passive, non-thermal state first yields work is the denominator of a simplest fraction. Near equilibrium, that number scales as $T/\Delta T$ for commensurate level spacings but as $(T/\Delta T)^{1/2}$, through Fibonacci numbers, for golden-ratio spacings. More generally it scales as $(T/\Delta T)^{1/r}$, with $r$ the number of rationally independent spacings, and for almost every spectrum as $(T/\Delta T)^{1/(d-1)}$. The same rank sets how long the ledger takes to echo, so the copy lift and the ledger's recurrence read one arithmetic object. Restricting the admissible processes by a symmetry enlarges the free family by one chemical potential per charge. For non-commuting charges and strictly symmetric cycles, a state with no orientation is free only if it is thermal: without an orientation, only central charges carry chemical potentials. Two joins follow. First, noise is set by the defect of the dilation, for passive and active ports alike. Second, a port's relation to a conserved charge — can it supply it, can it read it — classifies protected memory, non-demolition measurement, control, and thermalization. Most ingredients are known. We separate what is assumed, derived, imported, merely analogous, and new, and we give finite exact proofs with certificates.

---

## Architecture of the Port Principle

**The constraint.** A port is a boundary through which a system exchanges energy (or another conserved quantity) with the rest of the world and at which that exchange can be both driven and observed. In wave variables its absorbed power is $\|a\|^2-\|b\|^2$, incoming minus outgoing. The *port constraint* is
$$\|b\|\le\|a\| \qquad\text{(no port gives more than it takes).}$$

**The lift calculus.** By itself the constraint says little. The paper's organizing claim is that the constraint, subjected to a few natural operations, exposes a sequence of laws one at a time:

$$
\boxed{\text{constraint}\ \xrightarrow{\ \text{every input}\ }\ \text{lossless ledger}}\qquad
\boxed{\text{constraint}\ \xrightarrow{\ \text{time lift}\ }\ \text{causality}}
$$
$$
\boxed{\text{constraint}\ \xrightarrow{\ \text{copy lift}\ }\ \text{Gibbs / KMS}}\qquad
\boxed{\text{constraint}\ \xrightarrow{\ \text{symmetry restriction}\ }\ \text{generalized Gibbs / resource theory}}
$$

The lifts *strengthen* the constraint by enlarging the family of tests. The restriction *weakens* it by shrinking the family of admissible processes, and therefore enlarges the family of free states (Proposition 3.3). The copy lift is *graded* by the number of copies, and its grades carry an arithmetic (§6). **Nothing in this paper is forced by passivity alone: each law is forced by the constraint together with a named lift or restriction**, and Table 3.1 says which.

**Two joins.** The base and the copy lift meet in the hidden ports of the ledger: *noise is set by the dilation defect* (§8). The base and the symmetry restriction meet in the ledger's conserved charges: *a port flips only what it can supply and dephases only what it can read* (§9).

**What is claimed.** §1.3 sorts every ingredient into five kinds: assumed, derived here, imported, structural analogy only, and new. The contribution is the lift calculus, a set of finite exact proofs with certificates, and the results it exposes. Among those results are the parity defect, the arithmetic of copy thresholds, the circuit reading of the Petz classification, the coth law, and the port–charge table.

**What it is for.**
- *For teaching:* one resistor gives Johnson–Nyquist, Kramers–Kronig, Shannon, and Landauer; one tunnel junction gives the coth law.
- *For research:* it gives a single map tying together the filters of quantum Fisher information, noiseless subsystems, non-demolition measurement, thermodynamic resource theories, the thermodynamic uncertainty relation, and fluctuation theorems.
- *For engineering:* four modeling tasks (dynamics, noise, stability, thermodynamic consistency) become one, with universal checks (passivity, parity defect) and recipes (put $k_BT$ on every loss; push with the readout's own shape; trace every gain to its source).

**How to read.** Physicists: §§3–10. Engineers: §§2, 8, 11. Information theorists: §6 (filters and circuits) and §7. Readers from statistics and computing: §2.1 (the structural rows), §10 (the Markov statement), and Appendix B.

---

## 1. Watching and pushing

There are two fundamental experimental ways to interrogate a system. You can **watch** it — record its fluctuations while leaving it alone — or you can **push** it — apply a small, known disturbance and record the response. A physicist watches Brownian motion and pushes with a force. An engineer watches the hiss of a resistor and pushes with a voltage. A neuroscientist watches spontaneous activity and pushes with a stimulus. Theory, deduction, simulation, and prior knowledge are other routes to knowledge; this paper concerns the two experimental ones.

The fluctuation–dissipation theorem (FDT) says that, at equilibrium, the two experiments agree: watching determines pushing. This paper argues that the FDT is one face of a more primitive constraint on the place where watching and pushing happen — the *port*. The same constraint, *lifted* in a few precise ways, also exposes causality, reversible completions of irreversible processes, temperature, chemical potentials, and the costs of noise, erasure, and precision. The constraint is Kelvin's inequality localized at a port:

> **Port Principle.** No port gives more than it takes.

### 1.1 The lift calculus in one table

In wave variables (Definition 2.2) the power into a port is $\|a\|^2-\|b\|^2$, and the constraint is $\|b\|\le\|a\|$. Four operations act on it:

| Operation | Mathematical form | Exposes | § |
|---|---|---|---|
| **base** — every input | $S$ is a contraction | a lossless ledger (dilation); Wiener's echo-or-forget dichotomy | 4 |
| **time lift** — every instant | $\|P_tb\|\le\|P_ta\|$ for every truncation $P_t$ | causality; dispersion; parity defect = time-reflection overlap | 5 |
| **copy lift** — every number of copies (graded by $n$) | no work from $\rho^{\otimes n}$ | at $n=\infty$: Gibbs, zeroth law, one spectrum with many filters (FDT, Petz family as circuits), the coth law; at finite $n$: copy thresholds as simplest fractions | 6 |
| **symmetry restriction** — only cycles respecting a symmetry | passivity under charge-conserving unitaries | one chemical potential per conserved charge; generalized and non-Abelian Gibbs states | 7 |

The lifts strengthen the constraint (Proposition 3.3). The restriction weakens the class of admissible processes and therefore *enlarges* the family of free states. This reverses the common intuition that conserved quantities add constraints. Two joins connect the rows. The ledger's hidden ports carry the heat: **noise is set by the dilation defect** (§8). The ledger's symmetries decide what a port can change: **a port flips only what it can supply and dephases only what it can read** (§9).

### 1.2 What is new, and what is not

Nearly every ingredient is owned, and credited where used: dispersion relations (Kramers, Kronig, Titchmarsh); passivity implies causality (Youla–Castriota–Carlin 1959; Zemanian 1965); unitary dilation (Halmos 1950; Egerváry 1954; Sz.-Nagy–Foias; Stinespring 1955; Naimark 1940; purification, Chiribella–D'Ariano–Perinotti 2010); Wiener's theorem and RAGE; complete passivity ⟺ KMS (Pusz–Woronowicz 1978; Lenard 1978) and virtual temperatures (Skrzypczyk–Silva–Brunner 2015); the FDT family (Einstein 1905; Nyquist 1928; Callen–Welton 1951; Kubo 1957); monotone metrics (Petz 1996), operator monotone functions (Löwner 1934), and operator means (Kubo–Ando 1980); the Petz family from linear response (Shitara–Ueda 2016; Hauke et al. 2016) and skew-information bounds (Luo 2004); generalized and non-Abelian thermal states (Guryanova et al. 2016; Yunger Halpern et al. 2016; Lostaglio–Jennings–Rudolph 2017); dissipativity-based thermodynamics (Willems 1972; Haddad 2019; van der Schaft 2021); compositional passive networks (Baez–Fong 2018); noise waves (Twiss 1955; Bosma 1967); the amplifier bound (Haus–Mullen 1962; Caves 1982); noiseless subsystems (Zanardi–Rasetti 1997; Knill–Laflamme–Viola 2000); the thermodynamic uncertainty relation (Barato–Seifert 2015; Gingrich et al. 2016) and the fluctuation–response inequality (Dechant–Sasa 2020).

This paper adds:
- (i) **the lift calculus**: a base constraint, a time lift, a graded copy lift, and a symmetry restriction, with their order relations and self-contained finite proofs (Proposition 3.3; Lemma 6.2; Theorems 5.1, 6.3, 7.2);
- (ii) **the parity defect**: $\|\operatorname{Re}\hat f\|^2-\|\operatorname{Im}\hat f\|^2=2\pi\langle f,\mathcal Rf\rangle$ for arbitrary kernels, which makes causal parity a diagnostic of instability and acausality — not of gain (Theorem 5.4);
- (iii) **Wiener's dichotomy read as the echo-or-forget law of dilations**, with its finite-ledger quantification (Theorem 4.5, Corollary 4.6);
- (iv) **the arithmetic of the graded copy lift**:
  - copy thresholds are simplest fractions between an energy ratio and an entropy ratio (Theorem 6.6);
  - the gear ratios of the smallest two-temperature engine fill exactly the Carnot window (Corollary 6.7);
  - near equilibrium, resonant and badly approximable level spacings separate, with Fibonacci thresholds for golden spacings (Proposition 6.8);
  - beyond three levels, a resonance-rank law: the threshold scales as $(T/\Delta T)^{1/r}$, with $r$ the number of rationally independent spacings, for every badly approximable spectrum and every rank;
  - for almost every spectrum the exponent is $1/(d-1)$, so resonance is a null-set penalty;
  - a detuning caps the resonance penalty;
  - for harmonic modes the same numbers count the order of the nonlinear process;
  - a conserved charge can raise the exponent;
  - $k$ reservoirs need only $(T/\Delta T)^{1/k}$ copies, and the three-level restrictions do not determine the four-level threshold (Theorems 6.9, 6.9′; Proposition 6.8a; Corollaries 6.9a–d);
- (iv′) **echo–yield duality**: the echo exponent of the ledger (the base, read in time) and the yield exponent of the copy lift are tied by $y(e+1)=1$, through Khinchin's transference (Proposition 6.9e);
- (v) **one spectrum, many filters**: closed-form frequency filters for every named Petz metric and for the Wigner–Yanase–Dyson family, with a single ordering chain (Theorem 6.10);
- (vi) **a circuit reading of the Petz classification**: the admissible filters are exactly those realized by self-dual resistor–inductor networks, and Petz's symmetry condition is detailed balance (Theorem 6.11);
- (vii) **the coth law**, together with a precise account of what it does and does not unify (Proposition 6.14);
- (viii) **the charge-restricted converse** of complete passivity for commuting charges, by a lattice argument that also repairs an edge case (Theorem 7.2); and, for strictly symmetric cycles with non-commuting charges, the converse for states without orientation, together with exact witnesses that non-thermal oriented states are activated (Theorem 7.4, Proposition 7.5);
- (ix) **the noise-defect formula** for passive and active ports, with the pump made explicit and dilation-independence proved (Theorem 8.1, Proposition 8.3);
- (x) **the port–charge table** and its non-Abelian collapse (Theorems 9.2, 9.3);
- (xi) **the modeling calculus**, linear and nonlinear (Propositions 11.1–11.2), the one-line answers, and the falsifiers (§§11, 13, 16).

None of these is deep in isolation. The claim is the lift calculus and what it exposes, and §15 makes the unification measurable.

### 1.3 What is assumed, derived, imported, analogous, and new

| Kind | Items |
|---|---|
| **Assumed** | the port constraint (reference states are passive); linearity, for the spectral calculus of §§4–8; additivity of energy over copies, for the copy lift; stationarity, for the dispersion and parity tests; finite dimension, for every exact proof; thermal hidden ports, for the noise formulas |
| **Derived here** (finite, exact, certified) | Propositions 2.3, 3.3, 4.4; Theorems 4.1–4.2; Theorem 5.1, Theorem 5.4, Corollary 5.5; Lemma 6.2, Theorem 6.3, Theorem 6.6, Corollary 6.7, Propositions 6.8 and 6.8a, Theorems 6.9 and 6.9′, Corollaries 6.9a–d, Theorem 6.10, Theorem 6.11(c), Corollary 6.13, Proposition 6.14; Theorems 7.1–7.2, Lemma 7.4a, Theorem 7.4, Proposition 7.5; Theorems 8.1, 8.2(2–3), 8.4, Proposition 8.3; Theorem 9.1(a, c, d), Theorem 9.3; Proposition 10.2; Propositions 11.1–11.2 |
| **Imported** (cited theorems used as stated) | Dirichlet, Minkowski's second theorem, Jarník's covering bound, Roth's theorem, Khinchin's transference (§6, number theory); Sz.-Nagy, Stinespring, Naimark, purification; Wiener and Riemann–Lebesgue; Titchmarsh; the continuum passivity–causality theorem (Youla–Castriota–Carlin; Zemanian); Pusz–Woronowicz and Lenard for general systems; Petz's classification; Löwner and Kubo–Ando; Holevo–Werner (Theorem 8.2(1)); Harada–Sasa; the fluctuation–response inequality; the general TUR; Kawai–Parrondo–Van den Broeck; Jacobson; the uniqueness of the non-Abelian thermal state with reference frames and charge batteries (Yunger Halpern et al.; Guryanova et al.; a different statement from §7's, see Remark 7.3); the divergence drift and the elimination of oscillator baths (Lau–Lubensky; Ford–Kac–Mazur; Zwanzig; Caldeira–Leggett) |
| **Structural analogy only** | the statistics, information-systems, and software rows of §2.1; the data and causal-inference columns of Appendix B; stochastic gradient descent (§11); design readings marked [A] |
| **New** | the lift calculus as an organizing structure; the parity defect for arbitrary kernels; the finite-ledger reading of Wiener's dichotomy; the copy-threshold arithmetic (Theorem 6.6 to Proposition 6.8a), the resonance-rank law and its almost-every form (Theorems 6.9, 6.9′, Corollaries 6.9a–d), and the echo–yield duality (Proposition 6.9e); the circuit reading of the Petz classification (Theorem 6.11(c) and its consequence for admissible filters); the organization of the coth law; the charge-restricted converse by lattice argument; under strict non-Abelian symmetry, the converse for states without orientation and the activation witnesses (Theorem 7.4, Proposition 7.5); the unified passive/active noise-defect statement; the port–charge table and its non-Abelian collapse |

### 1.4 Claim tiers

**[P]** proven here (finite, exact) or a cited theorem used as stated. **[A]** a standard physical argument, or a structural identification not proven here. **[C]** a conjectural reading, fenced, with no evidentiary weight. Every [P] result proven here has an exact-arithmetic certificate (Appendix A).

---

## 2. What is a port

### 2.1 For any reader

A **port** is a boundary through which a system exchanges something with the rest of the world, and at which that exchange can be both driven and observed. A wall socket, an eardrum, a cell membrane, a telescope aperture, a strain gauge, and a black-hole horizon are all ports. A port is *not* an observer: any subsystem boundary is a port, whether or not anyone is looking.

*Exact realizations.* In these domains every port carries an **effort** and a **flow** whose product is a power, and the Port Principle is a physical law. This is the bond-graph observation of Paynter (1961), extended here to stochastic and quantum ports:

| Domain | Effort | Flow | Stores | Dissipates |
|---|---|---|---|---|
| Electrical | voltage | current | capacitor, inductor | resistor |
| Mechanical (translation) | force | velocity | spring, mass | damper |
| Mechanical (rotation) | torque | angular velocity | torsion spring, inertia | friction |
| Hydraulic | pressure | volume flow | tank, fluid inertia | constriction |
| Thermal | temperature | entropy flow | heat capacity | thermal resistance |
| Chemical | chemical potential | molar flow | concentration | reaction |
| Stochastic thermodynamics | affinity $\ln\frac{\pi_iT_{ij}}{\pi_jT_{ji}}$ | probability current $J_{ij}$ | — | entropy production ($\times k_BT$: a power) |
| Any conserved charge $Q_k$ | its chemical potential $\mu_k$ | its current | — | — |
| Scattering (classical or quantum) | incoming amplitude $a$ | outgoing amplitude $b$ | — | absorbed power $\|a\|^2-\|b\|^2$ |

The stochastic row is Schnakenberg's (1976): entropy production is flux times affinity. The charge row is made exact in §7, where each conserved charge adds one effort–flow pair.

*Structural translations.* In other disciplines the same architecture — a boundary, a watch/push pair, a constraint, and its lifts — can be written down, but "effort × flow" is not a power and the constraint is not the second law:

| Discipline | "Push" | "Watch" | Status of the constraint |
|---|---|---|---|
| Statistics and causal inference | intervention | observational association | no energetic meaning |
| Information processing | channel input | channel output | monotonicity under processing — exact as mathematics for quantum Fisher metrics (Theorem 6.11), but not an energy balance |
| Software and data systems | request, query | response, log | analogy only |

Results proven in this paper apply to the exact realizations. The translations carry only the architecture.

### 2.2 Formal definitions

**Definition 2.1 (linear port, discrete time).** A real matrix $K$ maps inputs $u$ to outputs $y=Ku$ on the grid $\{0,\dots,n-1\}$, and $u_sy_s$ is the power at step $s$. The energy absorbed up to instant $t$ is $\mathcal E_t(u)=\sum_{s\le t}u_sy_s$.

**Definition 2.2 (wave variables, scattering port).** Put $a=\tfrac12(u+y)$ (incoming) and $b=\tfrac12(y-u)$ (outgoing). Then
$$u_sy_s=a_s^2-b_s^2 ,$$
so absorbed energy is incoming minus outgoing. A scattering port is $b=Sa$. It is **passive for every input** if $\|Sa\|\le\|a\|$ for all $a$ (a contraction), and **passive at every instant** if $\|P_tSa\|\le\|P_ta\|$ for every truncation $P_t$ to times $\le t$.

**Proposition 2.3 (the two forms agree) [P].** $\mathcal E_t(u)\ge0$ for all $u$ is equivalent to $\|P_tb\|\le\|P_ta\|$. Net passivity ($\operatorname{sym}K\succeq0$) is equivalent to $S=(K-I)(K+I)^{-1}$ being a contraction (Cayley).

*Proof.* The power identity gives the first statement. For the second, $\|(K-I)x\|^2\le\|(K+I)x\|^2\iff\langle x,Kx\rangle\ge0$. Put $y=(K+I)x$, noting that $K+I$ is invertible because its symmetric part is $\succeq I$. Certificate P4.R1. $\square$

**Definition 2.4 (quantum port).** A triple $(\mathcal H_S,\{S_k\},\rho)$: a system, its coupling operators ($H_{\rm int}=\sum_kS_k\otimes B_k$), and a reference state. The state $\rho$ is **passive** for $H$ if $\operatorname{tr}(U\rho U^\dagger H)\ge\operatorname{tr}(\rho H)$ for all unitaries $U$, and **completely passive** if $\rho^{\otimes n}$ is passive for $H_n=\sum_kH^{(k)}$ for every $n$.

**Definition 2.5 (active port; boundary rule).** A port is **active** if its boundary contains a sub-port whose reference state is not passive (it has positive ergotropy): a charged battery, a coherent pump, an inverted medium, a fuel reservoir. *Boundary rule:* when a port shows gain, enlarge its boundary until the non-passive source is inside it. The constraint then applies to the enlarged boundary, and the formulas of §8 price the draw on the source. The principle never asserts that an active port is passive.

### 2.3 The watch–push pair

*Watching* measures the symmetrized correlation $C_{AB}(t)=\tfrac12\langle\{A(t),B\}\rangle$. *Pushing* measures the response $\chi_{AB}(t)=\tfrac i\hbar\theta(t)\langle[A(t),B]\rangle$ (Kubo). They are the symmetric and antisymmetric halves of one complex correlation $\langle A(t)B\rangle$. Watching *adds* the two directions of every elementary process, and pushing *subtracts* them (Proposition 6.14).

---

## 3. The lift calculus

The paper's organizing claim is not that passivity alone implies the laws discussed below. It is that one passivity constraint, subjected to a few natural operations, exposes them one at a time. This section makes the operations precise.

**Definition 3.1 (port constraint).** A *port constraint* is a triple $(\mathcal X,\mathcal C,W)$ with three parts:
- $\mathcal X$ is a set of *reference objects*: a response kernel $K$, a reference state $\rho$, or the pair;
- $\mathcal C$ is a class of *admissible processes*: inputs, or cyclic unitaries;
- $W(\pi,x)$ is the energy the port delivers under process $\pi$ when its reference object is $x$.

The *admissible* reference objects are $\operatorname{Adm}(\mathcal C)=\{x\in\mathcal X:\ W(\pi,x)\le0\ \text{for all }\pi\in\mathcal C\}$. The *base* constraint takes $\mathcal C$ to be all inputs, with $W=\|Sa\|^2-\|a\|^2$, or all cyclic unitaries, with $W=\operatorname{tr}(\rho H)-\operatorname{tr}(U\rho U^\dagger H)$.

**Definition 3.2 (the operations).**
1. *Time lift.* Each admissible input is also tested on every truncation $P_t$: $\operatorname{Adm}_{\rm time}=\{x:\ W(P_t\pi,x)\le0\ \forall\pi,t\}$.
2. *Copy lift of grade $n$.* The reference state is replaced by $\rho^{\otimes n}$ with the additive Hamiltonian $H_n$, and the processes by all cyclic unitaries on $n$ copies. Call the result $\operatorname{Adm}_n$, and the full copy lift $\operatorname{Adm}_\infty=\bigcap_n\operatorname{Adm}_n$.
3. *Symmetry restriction.* The admissible processes are restricted to those commuting with the conserved charges of a symmetry: $\mathcal C\mapsto\mathcal C^G$.

Lifts enlarge the family of tests; the restriction shrinks it.

**Proposition 3.3 (order) [P].**
- **(a)** $\operatorname{Adm}_{\rm time}\subseteq\operatorname{Adm}_{\rm base}$, strictly.
- **(b)** $\operatorname{Adm}_{n+1}\subseteq\operatorname{Adm}_n$ for every $n$. If $H$ has at least two distinct eigenvalues, the faithful states in $\operatorname{Adm}_\infty$ are exactly the Gibbs states.
- **(c)** $\operatorname{Adm}(\mathcal C^G)\supseteq\operatorname{Adm}(\mathcal C)$, strictly. The full copy lift of the restricted class is the generalized Gibbs family, exactly for commuting charges.

*Proof.* (a) Take $t$ equal to the final time. Remark 5.2 shows the inclusion is strict. (b) If $U$ extracts work from $n$ copies, $U\otimes I$ extracts the same work from $n+1$, because $H_{n+1}=H_n\otimes I+I\otimes H$. The identification of $\operatorname{Adm}_\infty$ is Theorem 6.3. (c) Fewer processes are tested. Strictness and the identification are Theorems 7.1–7.2 and certificate P4.R4.K4c. $\square$

**Remark 3.4 (the time and copy lifts act on different components).** The time lift constrains a port's *response* (its kernel). The copy lift constrains its *reference state*. They are logically independent: a causal response can be evaluated in a non-Gibbs state, and an acausal model response can be paired with a Gibbs state. Linear-response theory is their conjunction — causal response functions (time lift) computed in KMS states (copy lift). Independence of the constraints does not mean their quantitative readouts are unrelated. On one ledger, the time at which all phases return (a base property, read in time; Corollary 4.6) and the number of copies at which work first appears (the graded copy lift) are governed by the same module of level spacings (Proposition 6.9e). That is a shared parameterization of two thresholds, not a logical dependence between the lifts.

**Table 3.1 (what each operation exposes).**

| Operation | Structure exposed | Proven in |
|---|---|---|
| base | lossless ledger; defect Gram independent of the ledger; echo or forget | Theorems 4.1–4.5, Proposition 4.4 |
| time lift | causality; dispersion; parity defect | Theorems 5.1–5.4, Corollary 5.5 |
| copy lift, $n=\infty$ | Gibbs state; zeroth law; filters and their circuit reading; $D=\beta W$; the coth law | Theorem 6.3, Corollary 6.5, Theorems 6.10–6.11, Corollary 6.13, Proposition 6.14 |
| copy lift, finite $n$ | copy thresholds; the Carnot window; resonance versus irrationality; the resonance-rank law | Lemma 6.2, Theorem 6.6, Corollary 6.7, Proposition 6.8, Theorem 6.9 |
| symmetry restriction | one chemical potential per charge; generalized and non-Abelian Gibbs states; under strict non-Abelian symmetry, only central charges for states without orientation | Theorems 7.1–7.2, 7.4; Proposition 7.5 |
| join: base × copy | noise set by the dilation defect | Theorems 8.1–8.4, Proposition 8.3 |
| join: base × symmetry | the port–charge table and its non-Abelian collapse | Theorems 9.1–9.3 |
| failure of the copy lift's conclusions | the arrow as the watch–push gap | Theorem 10.1, Propositions 10.2–10.3 |

```
             PORT CONSTRAINT:  no port gives more than it takes   (‖b‖ ≤ ‖a‖)
                                          │
   base (every input): contraction ⇒ lossless ledger (Halmos, Egerváry, Sz.-Nagy,
                       Stinespring, Naimark) ⇒ Wiener: point spectrum echoes,
                       continuous spectrum forgets
                                          │
        ┌─────────────────────────────────┼──────────────────────────────────┐
   time lift                        copy lift (n = 1, 2, …, ∞)         symmetry restriction
   causality ⇒ Kramers–Kronig       n = ∞: Gibbs, zeroth law;          fewer cycles tested ⇒
   parity defect = ⟨f, Rf⟩          one spectrum, many filters;        free family enlarged:
   (gain allowed;                   filters = self-dual RL networks;   one μ per charge
    instability shows)              coth law.  finite n: thresholds    (GGE; non-Abelian
                                    = simplest fractions               thermal state)
        └─────────────────────────────────┼──────────────────────────────────┘
   JOIN 1 (base × copy):     noise = temperature × defect Gram   (Kirchhoff · Nyquist · Caves)
   JOIN 2 (base × symmetry): port × Noether charge   (supply / read;  non-Abelian: Schur)
                                          │
   away from equilibrium: arrow = watch–push gap (Harada–Sasa, fluctuation–response, TUR)
   modeling calculus: interconnect · reduce · dilate · assign noise
```

The teachable form is six **prohibitions**, each attributed to the operation that forces it:

1. **No resistance without reactance** (base + time lift, for stable responses; §5). A prism works because glass absorbs ultraviolet.
2. **No loss without a ledger** (base; §4). A finite room echoes; forgetting requires a continuous spectrum.
3. **No dissipation without fluctuation** (copy lift; §6). A resistor hisses in proportion to its resistance.
4. **No gain without noise, and no gain without a source** (join of base and copy lift; §8). An amplifier hisses in proportion to its gain and draws on a non-passive pump.
5. **No erasure without heat** (copy lift applied to the bath, i.e. bath passivity; §8). Resetting a bit into a thermal bath releases at least $k_BT\ln2$ (Landauer).
6. **No precision without dissipation** (copy lift applied locally, i.e. local detailed balance, for steady currents of Markov processes; §§6, 10). A steady current's relative variance times its entropy production is at least $2k_B$ (the TUR).

---

## 4. The base: every input and the lossless ledger

**Theorem 4.1 (Halmos dilation) [P].** Let $T$ be a contraction on a finite-dimensional space, with $D_T=(I-T^\dagger T)^{1/2}$ and $D_{T^\dagger}=(I-TT^\dagger)^{1/2}$. Then
$$U=\begin{pmatrix}T&D_{T^\dagger}\\D_T&-T^\dagger\end{pmatrix}$$
is unitary.

*Proof.* The intertwining $TD_T=D_{T^\dagger}T$ holds because $Tf(T^\dagger T)=f(TT^\dagger)T$ for polynomials $f$, hence for the square root. Expanding $U^\dagger U$ gives $I$. $\square$

**Theorem 4.2 (finite horizon; Egerváry 1954) [P].** For $N\ge1$, define $U_N$ on $\mathcal H^{N+1}$ by first block row $(T,0,\dots,0,D_{T^\dagger})$, second block row $(D_T,0,\dots,0,-T^\dagger)$, and identity blocks shifting the remaining components down. Then $U_N$ is unitary and $P_{\mathcal H}U_N^kP_{\mathcal H}=T^k$ for $0\le k\le N$. In general the identity fails at $k=N+1$.

*Proof.* $U_N$ is the Halmos unitary on the first and last slots, composed with a shift of the middle slots. A defect component created at step 1 travels down the chain and re-enters the first slot only after $N$ steps. Certificate P2.S2 gives an exact $15\times15$ rational instance with failure at $k=N+1$. $\square$

**Theorem 4.3 (all time, all channels, all measurements) [P, cited].**
- Every contraction has a unitary power dilation, and a completely non-unitary contraction requires an infinite bilateral shift (Sz.-Nagy 1953).
- Every quantum channel is a unitary on system⊗environment followed by a partial trace (Stinespring 1955).
- Every POVM is a projective measurement on a larger space (Naimark 1940).
- In general probabilistic theories, such reversible realizations exist iff the purification principle holds (Chiribella–D'Ariano–Perinotti 2010).

**Proposition 4.4 (the defect Gram does not depend on the ledger) [P].** Define the *defect Gram matrices* of a contraction $S$ as $\Delta_{\rm out}(S)=I-SS^\dagger$ and $\Delta_{\rm in}(S)=I-S^\dagger S$; these are the squares of the Halmos defect operators. If $\begin{psmallmatrix}S&B\\C&D\end{psmallmatrix}$ is *any* unitary completion of $S$, then $BB^\dagger=\Delta_{\rm out}(S)$ and $C^\dagger C=\Delta_{\rm in}(S)$.

*Proof.* These are the top-left blocks of $UU^\dagger=I$ and $U^\dagger U=I$. Certificate P4.R10 exhibits two different exact ledgers with the same corner and identical defect Gram. $\square$

Every noise formula in §8 is built from these Gram matrices, so the noise predictions do not depend on which ledger one imagines.

**Theorem 4.5 (echo or forget: Wiener's dichotomy) [P, cited; finite form certified].** Let $\psi$ be the port vector on the ledger, $H$ the ledger's generator, and $\mu_\psi$ the spectral measure of $\psi$. The return amplitude is $a(t)=\langle\psi,e^{-iHt}\psi\rangle=\int e^{-i\lambda t}d\mu_\psi(\lambda)$.

1. (Wiener) $\displaystyle\lim_{T\to\infty}\frac1T\int_0^T|a(t)|^2dt=\sum_\lambda\mu_\psi(\{\lambda\})^2$.
2. If $\mu_\psi$ is pure point, $a$ is almost periodic, and $|a(t)|$ returns within any $\varepsilon$ of 1 on a relatively dense set of times: the port echoes.
3. If $\mu_\psi$ is continuous, the time-averaged return is zero. If it is absolutely continuous, $a(t)\to0$ pointwise (Riemann–Lebesgue): the port forgets.

*Proof.* (1) is Wiener's theorem, (2) is Bohr almost-periodicity, and (3) follows from (1) and the Riemann–Lebesgue lemma. Certificate P4.R3 checks the finite-ledger identity in (1) exactly. $\square$

**Corollary 4.6 (how finite ledgers approach forgetting) [P + witness].** Finite-dimensional or effectively confined ledgers have pure point spectra, and therefore recur (Theorem 4.5(2)). Forgetting in the sense of Theorem 4.5(3) requires a continuous spectrum, which arises in the continuum (infinite-volume) limit. The approach to that limit can be quantified.

Take a level coupled to $N$ equally spaced states, with spacing $\delta$ and bandwidth $W=N\delta$. The decay $e^{-\Gamma t}$ with $\Gamma=2\pi g^2/\delta$ is reproduced — as a sum of pure rotations — until
$$t_{\rm rec}=\frac{2\pi}{\delta}=\frac{2\pi N}{W}.$$
The time-averaged echo is $\sum_kw_k^2\approx\delta/(\pi\Gamma)$, which tends to 0 as $\delta\to0$. The certificates give:
- **P1.C4** ($N=801$): the revival probability at $t_{\rm rec}=251$ is $0.55$, against $2.5\times10^{-34}$ had the loss been permanent;
- **P4.R3**: the average echo is $\sum w_k^2=0.0252$, against a predicted $0.0259$.

*A record is durable only as long as the receiving channel's recurrence time.* This gives Bell's "for all practical purposes" a number, and the continuum limit of Theorem 4.5 turns the number into "forever".

**Remark 4.7 (every motion is rotation, on the ledger).** Unitary evolution is a superposition of pure rotations $e^{-i\lambda t}$. A damped spiral at the port is the shadow of rotations on the ledger: decay is the dephasing of a continuum of rotations. Nonlinear conservative dynamics also decomposes into rotations on observables (Koopman). The caveat is non-normal dynamics, where the rotation basis is ill-conditioned and transient growth occurs that the eigenvalues do not show.

---

## 5. The time lift: causality and dispersion

**Theorem 5.1 (instantaneous passivity forces causality) [P].** If a linear port $K$ is passive at every instant, then $K_{ij}=0$ for $j>i$. Conversely, a causal $K$ is passive at every instant iff the symmetric part of every leading block $K_{[0..t]}$ is positive semidefinite.

*Proof.* Suppose $K_{ij}\neq0$ with $j>i$. Take $u=e_i+\lambda e_j$ and truncate at $t=i$. Then $\mathcal E_i(u)=K_{ii}+\lambda K_{ij}$, which equals $-1$ for $\lambda=-(K_{ii}+1)/K_{ij}$. For the converse, causality gives $\mathcal E_t(u)=u_{[0..t]}^{\mathsf T}K_{[0..t]}u_{[0..t]}$. Certificate P2.S1. $\square$

**Remark 5.2 (net passivity permits precognition) [P].** The kernel $K=\begin{psmallmatrix}2&1&0\\1&2&1\\0&1&2\end{psmallmatrix}$ is net passive, but the input $u=(1,-3,0)$ gives $\mathcal E_0=-1$: this port borrows energy from the future. The arrow of time enters the theory exactly at the time lift. The continuum statement — a linear, time-invariant operator that is passive at every instant is causal, with a positive-real transfer function — is due to Youla–Castriota–Carlin (1959) and Zemanian (1965); see Srivastava (2021) for a review.

**Theorem 5.3 (dispersion) [P, cited].** A causal response with finite energy has a Fourier transform analytic in the upper half-plane, whose real and imaginary parts are Hilbert-transform pairs (Kramers–Kronig; Titchmarsh 1937).

**Theorem 5.4 (parity defect) [P].** For *any* real kernel $K$ on a finite grid, with $S=\tfrac12(K+K^{\mathsf T})$ and $A=\tfrac12(K-K^{\mathsf T})$,
$$\|S\|_F^2-\|A\|_F^2=\operatorname{tr}(K^2)=\langle K,K^{\mathsf T}\rangle_F .$$
For *any* real $f\in L^2(\mathbb R)$, with $(\mathcal Rf)(t)=f(-t)$,
$$\int(\operatorname{Re}\hat f)^2d\omega-\int(\operatorname{Im}\hat f)^2d\omega=2\pi\int f(t)f(-t)\,dt=2\pi\langle f,\mathcal Rf\rangle .$$
The defect is the overlap of the response with its own time reversal.

*Proof.* $\|S\|^2-\|A\|^2=\tfrac14(\|K+K^{\mathsf T}\|^2-\|K-K^{\mathsf T}\|^2)=\langle K,K^{\mathsf T}\rangle$. In the continuum, $\operatorname{Re}\hat f$ and $i\operatorname{Im}\hat f$ are the transforms of $f_e=\tfrac12(f+\mathcal Rf)$ and $f_o=\tfrac12(f-\mathcal Rf)$, and $\|f_e\|^2-\|f_o\|^2=\langle f,\mathcal Rf\rangle$. Plancherel finishes. $\square$

**Corollary 5.5 (causal parity) [P].** If the response is causal and has finite energy, the overlap $\langle f,\mathcal Rf\rangle$ vanishes except for the instantaneous part:
- on the grid, $\|S\|^2-\|A\|^2=\sum_iK_{ii}^2$;
- in the continuum, $\int(\operatorname{Re}\hat f)^2=\int(\operatorname{Im}\hat f)^2=\pi\int_0^\infty f^2$.

*In a stable causal response, the reactive and resistive parts carry exactly equal energy.* The hypothesis is stability, not passivity: a stable amplifier $\chi=G/(\gamma-i\omega)$ with $G=3$ has zero defect (certificate P4.R2).

*What the defect detects.* Subtract the instantaneous part from a measured spectrum. A nonzero defect then certifies that the real-axis response is not the transform of a single-sided finite-energy kernel. That happens in three situations:
- **instability**: a pole in the upper half-plane makes the real-axis function the transform of a two-sided kernel;
- genuine acausality;
- a violation of the stationarity assumption, such as drift.

The defect is then the cross-overlap between the causal and anticausal parts. For a decaying mode plus an unstable one, $\chi=\frac1{\gamma_1-i\omega}-\frac1{\gamma_2+i\omega}$, the defect is exactly $-4\pi/(\gamma_1+\gamma_2)$ (certificate P4.R2). It detects the same crossing that Liu (2026) tracks as a Blaschke-winding jump when the spectral abscissa of the reduced dynamics changes sign. The test is a global companion to the Kramers–Kronig compliance tests of impedance spectroscopy, and it needs adequate bandwidth coverage [A].

### Three boundaries, not one

Beyond passivity, three distinct boundaries are often conflated:
1. **The passivity (gain) boundary.** Net gain appears ($\operatorname{Re}Z<0$, or $\|S(\omega)\|>1$ at some $\omega$). The noise-defect formula switches branch here (Theorem 8.2), and its only noiseless point, $\tau=1$, lies exactly on this boundary.
2. **The stability boundary.** A pole crosses into the upper half-plane, for example at a lasing threshold. The parity defect switches on here.
3. **Exceptional points.** Eigenvectors coalesce. This is a spectral degeneracy that can occur on either side of the other two boundaries. In PT-symmetric gain–loss dimers the PT-breaking exceptional point coincides with boundary 2, which is why the three are often identified.

Time reversal exchanges the poles and zeros of the scattering matrix: a laser at threshold (a pole on the real axis) time-reverses into a coherent perfect absorber (a zero on the real axis) (Chong–Ge–Cao–Stone 2010) [A].

*Examples.*
- Glass's ultraviolet absorption $n''$ forces the visible dispersion of $n'$, which is why a prism separates colors.
- In the Wigner–Weisskopf model, the decay rate (resistance) arrives with its dispersion partner, the Lamb shift: $0.0306$ measured, against a Kramers–Kronig prediction of $0.0303$. The reactance's derivative renormalizes the decay itself, so the fit becomes $Z^2e^{-Z\Gamma t}$ with $Z=1/(1-\operatorname{Re}\Sigma')$. The error is $2.8\times10^{-3}$ with $Z$, against $4.3\%$ without it (certificate P1.C4, whose first-run failure is retained).

---

## 6. The copy lift: temperature, thresholds, and filters

**Lemma 6.1 (passivity) [P].** A state $\rho$ is passive iff $[\rho,H]=0$ and its eigenvalues are anti-ordered with energy. Its ergotropy is $\operatorname{tr}(\rho H)-\sum_ip_i^\downarrow E_i^\uparrow$.

*Proof.* Apply the rearrangement inequality to the doubly stochastic matrix $|U_{ij}|^2$. $\square$

**Lemma 6.2 (lattice form of the graded copy lift) [P].** Let $\rho$ be faithful and diagonal in an eigenbasis of $H$, with levels $i=1,\dots,d$, energies $E_i$, and $f_i=-\ln p_i$. Then $\rho^{\otimes n}$ is passive for $H_n$ iff no integer vector $c\in\mathbb Z^d$ satisfies all three conditions
$$\textstyle\sum_ic_i=0,\qquad \sum_ic_i^+\le n,\qquad c\cdot E<0<c\cdot f .$$
If the admissible cycles must conserve charges with integer charge vectors $q_i$, add the condition $\sum_ic_iq_i=0$.

*Proof.* $\rho^{\otimes n}$ is diagonal in the product eigenbasis. A product basis vector is specified by occupation numbers $\nu\in\mathbb N^d$ with $\sum_i\nu_i=n$. It has energy $\nu\cdot E$, because energy is additive over copies, and probability $e^{-\nu\cdot f}$.

By Lemma 6.1, $\rho^{\otimes n}$ is passive iff no two basis vectors $\nu,\nu'$ have $\nu\cdot E<\nu'\cdot E$ and $e^{-\nu\cdot f}<e^{-\nu'\cdot f}$. With $c=\nu-\nu'$ these conditions read $c\cdot E<0<c\cdot f$, and $c$ satisfies $\sum c_i=0$ and $\sum c_i^+\le n$. Conversely, for any such $c$, put $\nu=c^++r$ and $\nu'=c^-+r$, with $r\in\mathbb N^d$ and $\sum r_i=n-\sum c_i^+$.

A charge-conserving unitary acts within sectors of fixed total charge. So only pairs with $\nu\cdot q=\nu'\cdot q$ count, that is, pairs with $c\cdot q=0$. $\square$

The occupation-number criterion in this proof is standard. It goes back to Pusz–Woronowicz and Lenard, and is stated explicitly as the $N$-passivity condition by Salvia–Giovannetti (2020, eq. 13). What Lemma 6.2 adds is the bookkeeping: passing to the difference vector $c$ makes the copy count a cost, $\sum_ic_i^+$, which is what the threshold results below minimize.

**Theorem 6.3 (the full copy lift forces temperature) [P].** Let $H$ have at least two distinct eigenvalues. A faithful state is completely passive iff $\rho=e^{-\beta H}/Z$ with $\beta\ge0$. If $H\propto I$, every state is completely passive.

*Proof.* (⇐) $\rho^{\otimes n}=e^{-\beta H_n}/Z^n$ is a non-increasing function of $H_n$, hence passive (Lemma 6.1).

(⇒) A completely passive $\rho$ is passive, so it commutes with $H$ and is diagonal in a joint eigenbasis. Write $f_i=-\ln p_i$. By Lemma 6.2, complete passivity says: for every $c$ in the lattice $L=\{c\in\mathbb Z^d:\sum c_i=0\}$, $c\cdot E<0$ implies $c\cdot f\le0$. Scaling extends this to the rational span $L_{\mathbb Q}$.
- *Kernels.* $L_{\mathbb Q}$ spans $L_{\mathbb R}=\operatorname{span}\{\mathbf1\}^\perp$. Since $E\notin\operatorname{span}\{\mathbf1\}$, the functional $\phi_E(c)=c\cdot E$ is not identically zero on $L_{\mathbb Q}$, so some $d\in L_{\mathbb Q}$ has $\phi_E(d)<0$. Now take $c\in L_{\mathbb Q}$ with $\phi_E(c)=0$. The vectors $\pm Nc+d$ have $\phi_E<0$, so $\pm N\phi_f(c)+\phi_f(d)\le0$ for all $N$. Hence $\phi_f(c)=0$.
- *Proportionality.* So $\phi_f$ factors through $\phi_E$ on $L_{\mathbb Q}$, as a map on the subgroup $\phi_E(L_{\mathbb Q})\subset\mathbb R$. That map is additive and non-decreasing: if $\phi_E(c)<\phi_E(c')$, then $\phi_E(c-c')<0$, so $\phi_f(c)\le\phi_f(c')$. A non-decreasing additive map on a subgroup of $\mathbb R$ is multiplication by a constant $\beta\ge0$. So $\phi_f=\beta\phi_E$ on $L_{\mathbb Q}$, and on $L_{\mathbb R}$ by density.
- *Conclusion.* $f-\beta E\perp L_{\mathbb R}$, so $f-\beta E\in\operatorname{span}\{\mathbf1\}$, i.e. $\rho=e^{-\beta H}/Z$.

If $E\in\operatorname{span}\{\mathbf1\}$ ($H\propto I$), no unitary changes the energy, so every state is completely passive (certificate P4.R4.K4a). $\square$

This is the finite-dimensional content of Pusz–Woronowicz (1978) and Lenard (1978). In the language of Skrzypczyk–Silva–Brunner (2015), it says that complete passivity equalizes all virtual temperatures.

**Remark 6.4 (degenerate manifolds).** Passivity of a single copy allows any population profile within a degenerate eigenspace. Complete passivity forces uniformity there, because copies let a lower-energy configuration be assembled from the "wrong" degenerate state. Certificate P4.R4.K4b: $E=(0,0,1)$ with $p=(\tfrac12,\tfrac13,\tfrac16)$ is passive but first turns active at $n^*=3$ copies, as pre-registered. The lattice argument needs no separate step for degenerate levels, and it isolates the one genuine exception, $H\propto I$.

**Corollary 6.5 (zeroth law) [P].** Two ports that are jointly completely passive for $H_A+H_B$ share one $\beta$. Two Gibbs ports at different temperatures are each completely passive, but jointly they are not: a heat engine exists. Certificate P2.S3: at equal temperature, two Gibbs ports stay jointly passive through $n=5$ copies; at unequal temperature they first become jointly active at $n^*=3$ (the value predicted by Corollary 6.7 below). An independent pairwise-inversion search reproduces the witness.

### The graded copy lift: when copies become exploitable

Proposition 3.3(b) says the copy lift comes in grades. For a passive state that is not Gibbs, some finite grade $n^*$ is the first to fail. The following results show that $n^*$ is arithmetic: it is governed by the rational approximation of one ratio by another. This refines, at finite $n$, the characterization of complete passivity by equal virtual temperatures (Skrzypczyk–Silva–Brunner 2015). It also sharpens the $N$-passivity hierarchy (Salvia–Giovannetti 2020) and the "$k$-activable" hierarchy of Sparaciari–Jennings–Oppenheim (2017), who showed that a passive state activated by an $(m,n)$ swap cycle becomes active at $m+n$ copies and left open whether fewer copies suffice. Theorem 6.6 gives the exact least number (Remark 6.6a). As in all of this section, "copies" means cyclic unitaries acting jointly on $n$ independent systems — an idealization of collective work extraction (Alicki–Fannes 2013) — with energy additive over copies.

**Theorem 6.6 (copy threshold for three levels) [P].** Let $E_0<E_1<E_2$, and let $\rho$ be faithful, diagonal, passive, and not Gibbs, with $f_i=-\ln p_i$. Put
$$r_E=\frac{E_1-E_0}{E_2-E_0},\qquad r_f=\frac{f_1-f_0}{f_2-f_0}.$$
Then $r_E,r_f\in[0,1]$ and $r_E\neq r_f$. The least $n$ for which $\rho^{\otimes n}$ is not passive is
$$n^*=\min\{m\ge1:\ \text{some fraction }k/m\text{ lies strictly between }r_E\text{ and }r_f\},$$
the denominator of the Stern–Brocot simplest fraction of that interval.

*Proof.* Shift $E$ and $f$ so that $E_0=f_0=0$. Passivity gives $0\le f_1\le f_2$. Moreover $f_2>0$, since otherwise $\rho$ is maximally mixed (Gibbs at $\beta=0$), and $r_E\neq r_f$, since otherwise $f$ is proportional to $E$. By Lemma 6.2 we need the least $\sum c^+$ over vectors $c=(-a-b,\,a,\,b)$ with
$$c\cdot E=aE_1+bE_2<0<af_1+bf_2=c\cdot f .$$
If $a,b\ge0$ then $c\cdot E\ge0$, and if $a,b\le0$ then $c\cdot f\le0$; so $a$ and $b$ have opposite signs.
- If $a=-m<0<b=k$, the conditions read $r_f<k/m<r_E$. Since $k/m<r_E<1$, we have $c_0=m-k>0$ and $\sum c^+=c_0+k=m$.
- If $a=m>0>b=-k$, they read $r_E<k/m<r_f\le1$. Then $c_0=k-m<0$ and $\sum c^+=m$.

In both cases the cost is the denominator $m$ of a fraction strictly between $r_E$ and $r_f$, and every such fraction occurs. The simplest fraction of an open interval has the least denominator of all fractions in it (Stern 1858; Brocot 1861; certificate P5.K2d). $\square$

*Example.* $E=(0,1,2)$ and $p=(\tfrac12,\tfrac25,\tfrac1{10})$ give $r_E=\tfrac12$ and $r_f=\ln\tfrac54/\ln5\approx0.139$. The simplest fraction in $(0.139,0.5)$ is $\tfrac13$, so $n^*=3$, with ergotropy $39/1000$ at $n=3$ (certificate P2.S3). Theorem 6.6 is confirmed against brute-force exact ergotropy on 40 instances (P5.H2.K2a). The sign of $r_f-r_E$ is the sign of the difference between the two virtual temperatures $\frac{f_1-f_0}{E_1-E_0}$ and $\frac{f_2-f_1}{E_2-E_1}$. The width of the interval is what sets the threshold.

**Remark 6.6a (relation to Sparaciari–Jennings–Oppenheim 2017).** Their cycle performs $m$ swaps on the hot virtual pair $(0,1)$ and $n$ on the cold pair $(1,2)$. It extracts work when $m\,\Delta E_{10}>n\,\Delta E_{21}$ and $(p_1/p_2)^n>(p_0/p_1)^m$. In the variables of Theorem 6.6 these two conditions read $r_f<\frac{n}{m+n}<r_E$: a fraction with denominator $m+n$ lies in the interval. Their copy count $m+n$ is therefore exactly the cost of one admissible fraction, and their sub-Carnot efficiency $1-\frac{n\Delta E_{21}}{m\Delta E_{10}}$ is the gear-ratio reading of that fraction. Salvia–Giovannetti (2020, Prop. 1) give the same picture from the passive side. If $\rho$ is $N$-passive and a fraction $m/N$ brackets $r_E$, then the populations obey the matching interpolation inequality. Their Prop. 12 and Cor. 6 treat exactly commensurate gaps, which is the resonant case of Proposition 6.8(a), in the structurally stable (equal-population) setting. Neither paper identifies the least $n$. What Theorem 6.6 adds is the exact threshold. By Lemma 6.2, the cost of every violating exchange is the denominator of a fraction in the interval, so no unitary on fewer copies than the Stern–Brocot denominator extracts work, and that many copies suffice. This settles the question Sparaciari et al. leave open in their §IV.B.

**Corollary 6.7 (the smallest two-temperature engine; the Carnot window) [P].** Consider two qubit ports $A,B$ with gaps $\varepsilon_A,\varepsilon_B>0$ in Gibbs states at $\beta_A>\beta_B$ (so $A$ is colder). The least $n$ for which $(\rho_A\otimes\rho_B)^{\otimes n}$ is not passive for $H_A+H_B$ is
$$n^*=\min\Big\{\max(k,m):\ \frac{\varepsilon_A}{\varepsilon_B}<\frac km<\frac{\beta_A}{\beta_B}\,\frac{\varepsilon_A}{\varepsilon_B}\Big\},$$
the height $\max(k,m)$ of the simplest fraction in that interval. The violating exchange moves $k$ quanta out of the hot port and $m$ quanta into the cold one. Its efficiency $\eta=1-\frac{m\varepsilon_A}{k\varepsilon_B}$ satisfies $0<\eta<\eta_C=1-\beta_B/\beta_A$ exactly when $k/m$ lies in the interval. The interval is the *Carnot window* of gear ratios. ("Smallest" here counts copies of fixed ports. It is distinct from the question of the smallest machine Hilbert space, answered by the two-qubit and single-qutrit engines of Linden–Popescu–Skrzypczyk 2010. The swap-cycle form of this window, with efficiency $1-\frac{n\Delta E_{21}}{m\Delta E_{10}}$, appears in Sparaciari–Jennings–Oppenheim 2017. The exact threshold is new here.)

*Proof.* Apply Lemma 6.2 to the four joint levels $ij\in\{00,10,01,11\}$, whose energies are $i\varepsilon_A+j\varepsilon_B$ and whose values of $f$ are $i\beta_A\varepsilon_A+j\beta_B\varepsilon_B$ up to a constant. For a relation vector $c$, let $m'=c_{10}+c_{11}$ and $k'=c_{01}+c_{11}$ be the net numbers of $A$- and $B$-excitations. Then
$$c\cdot E=\varepsilon_Am'+\varepsilon_Bk',\qquad c\cdot f=\beta_A\varepsilon_Am'+\beta_B\varepsilon_Bk'.$$
- *Which signs work.* A violation needs $m'=m>0>k'=-k$ with $k/m$ in the stated interval. The opposite signs would require $k'/|m'|$ to lie both below $\varepsilon_A/\varepsilon_B$ and above $(\beta_A/\beta_B)\varepsilon_A/\varepsilon_B$, which is impossible because $\beta_A>\beta_B$.
- *The cost.* $\sum c^+\ge\max(|m'|,|k'|)$, because $m'\le c_{10}^++c_{11}^+\le\sum c^+$ and $-k'\le c_{01}^-+c_{11}^-\le\sum c^-=\sum c^+$. Equality is attained by $c_{10}=m$, $c_{01}=-k$, $c_{00}=k-m$, $c_{11}=0$.
- *Minimization.* The simplest fraction has the least numerator and the least denominator of all fractions in the interval (certificate P5.K2d), so it minimizes $\max(k,m)$.
- *Efficiency.* The statement about $\eta$ is algebra (certificate P5.K2e).

Corollary 6.7 is confirmed against brute force on 29 instances (P5.H2.K2b). The instance with $\varepsilon_A:\varepsilon_B=1:2$ and $\beta_A/\beta_B=2$ gives the fraction $\tfrac23$, so $n^*=3$ with ergotropy $4/243$ (P2.S3). $\square$

**Proposition 6.8 (near equilibrium: resonance and irrationality) [P].** Let $x=\varepsilon_A/\varepsilon_B<1$ and $\beta_A/\beta_B=1+\delta$. The window is then $(x,\,x(1+\delta))$, and $n^*$ is the least denominator of a fraction in it.
- **(a) Resonant spacings.** If $x=p/q$ in lowest terms, then $n^*>1/(p\delta)$. For $x=\tfrac12$, $n^*$ is the least odd integer exceeding $1/\delta$.
- **(b) Badly approximable spacings.** If the continued fraction of $x$ has partial quotients at most $A$, then $n^*\le(A+1)^2/\sqrt{x\delta}$.
- **(c) The golden ratio.** If $x=1/\varphi$, then $n^*=F_n$, the $n$-th Fibonacci number, where $n$ is the least even integer with $\varphi^{2n-1}>\sqrt5/\delta+1/\varphi$. In particular $n^*$ grows like $\delta^{-1/2}$.

*Proof.* (a) Any fraction $k/m\neq p/q$ satisfies $|k/m-p/q|\ge1/(qm)$. A fraction in the window has $0<k/m-x<x\delta$, so $1/(qm)<p\delta/q$, i.e. $m>1/(p\delta)$. For $x=\tfrac12$, the fraction above $\tfrac12$ closest to it with odd denominator $m$ is $\frac{m+1}{2m}$, at distance $\frac1{2m}$, which lies in the window iff $m>1/\delta$. With even denominator the closest is $\frac{m/2+1}{m}$, at distance $\frac1m$, which requires $m>2/\delta$.

(b) The convergents $p_j/q_j$ of $x$ alternate sides of $x$, satisfy $|x-p_j/q_j|<1/q_j^2$, and grow with $q_{j+1}\le(A+1)q_j$. Let $p_j/q_j$ be the first convergent above $x$ with $q_j^2>1/(x\delta)$. It lies in the window. The previous convergent above $x$ has $q_{j-2}\le(x\delta)^{-1/2}$, so $n^*\le q_j\le(A+1)^2q_{j-2}\le(A+1)^2/\sqrt{x\delta}$.

(c) The convergents of $1/\varphi$ are $F_{n-1}/F_n$. They lie above $1/\varphi$ for even $n$, with
$$\frac{F_{n-1}}{F_n}-\frac1\varphi=\frac{\varphi^{-n}}{F_n},$$
which follows from $F_n-\varphi F_{n-1}=(-1/\varphi)^{n-1}$. Since every partial quotient is 1, the Stern–Brocot path to $1/\varphi$ passes only through convergents. So the simplest fraction of $(1/\varphi,(1+\delta)/\varphi)$ is the first convergent above $1/\varphi$ inside it: the least even $n$ with $\varphi^{-n}/F_n<\delta/\varphi$, i.e. $\varphi^{n-1}F_n>1/\delta$. By Binet's formula this is $\varphi^{2n-1}-\varphi^{-1}>\sqrt5/\delta$.

Certificates P5.H2.K2c and P5.K2f check all three parts exactly for $\delta=10^{-2},\dots,10^{-14}$. For example, at $\delta=10^{-10}$, $n^*=121393=F_{26}$ for the golden ratio, against $10^{10}+1$ for $x=\tfrac12$. $\square$

**Proposition 6.8a (a detuning caps the resonance penalty) [P].** Work in the setting of Corollary 6.7, with window $(x,x+w)$ and $w=x\delta$. Let $x=p/q+s\eta$, where $p/q<1$ is in lowest terms, $\eta>0$ and $s=\pm1$.
- *Away from the resonance* ($s=+1$). Always $n^*>1/(q(\eta+w))$. If moreover $w\ge q^2\eta(\eta+w)$, then $n^*\le1/(q(\eta+w))+q$. The detuning acts as extra temperature contrast.
- *Toward the resonance* ($s=-1$). If $w>\eta$, the exchange $p{:}q$ is admissible and $n^*\le q$. If $q^2\eta^2\le w\le\eta$, then $1/(q\eta)<n^*\le1/(q\eta)+q$: a plateau, followed by a collapse to $q$ copies once the contrast exceeds the detuning.

*Proof.* Every fraction $k/m\neq p/q$ satisfies $|k/m-p/q|\ge1/(qm)$, with equality exactly when $|kq-pm|=1$. For a fixed sign of $kq-pm$, these $m$ form one residue class mod $q$.
- *Away.* A fraction in the window lies above $p/q$ by less than $\eta+w$, so $m>1/(q(\eta+w))$. The fractions with $kq-pm=1$ lie at distance $1/(qm)$ from $p/q$. They lie in the window iff $m\in(1/(q(\eta+w)),1/(q\eta))$, an interval of length $w/(q\eta(\eta+w))\ge q$, so it contains one with $m\le1/(q(\eta+w))+q$.
- *Toward.* If $w>\eta$, then $p/q$ lies in the window. Otherwise every fraction in the window lies below $p/q$ by less than $\eta$, so $m>1/(q\eta)$. Those with $pm-kq=1$ fill $m\in(1/(q\eta),1/(q(\eta-w)))$, an interval of length at least $w/(q\eta^2)\ge q$. $\square$

At $\eta=0$ the away bound reads $n^*=1/(qw)+O(q)$, which is Proposition 6.8(a). Certificate P7.H7c checks every inequality exactly for $p/q=\tfrac12$, at two detunings and 36 contrasts on each side.

*Reading.* Near equilibrium, commensurate level spacings need of order $T/\Delta T$ copies before any work-extracting exchange exists. Badly approximable spacings need only of order $(T/\Delta T)^{1/2}$, and for golden-ratio spacings the thresholds are Fibonacci numbers. The mechanism is elementary. A work-extracting exchange of $k$ quanta for $m$ must be slightly off resonance, in the right direction, by less than the Carnot window. Exactly commensurate spacings offer small combinations only at exact resonance, which extracts no work, so they need large ones.

### Beyond three levels: the resonance-rank law

For $d$ levels, or several ports, Lemma 6.2 makes $n^*$ the minimum of $\sum c^+$ over the integer points of the open cone $\{c:\sum c_i=0,\ c\cdot E<0<c\cdot f\}$, with $c\cdot q=0$ added under a symmetry restriction. For $d=3$ this is the one-dimensional Stern–Brocot problem of Theorem 6.6. For $d\ge4$ the cone is a dihedral wedge in a lattice of rank $d-1\ge3$. The Stern–Brocot structure does not survive: minimizing exchanges generically use all $d$ levels (Corollary 6.9b). What survives is the scaling.

Shift so that $E_0=f_0=0$, and write $c=(-\sum_ia_i,\,a)$ with $a\in\mathbb Z^{d-1}$ and $E'=(E_1,\dots,E_{d-1})$. Then $\sum c^+=\tfrac12\big(|\sum_ia_i|+\|a\|_1\big)$, which lies between $\|a\|_\infty$ and $\|a\|_1$. Near equilibrium put $f=\beta(E+\delta u)$ with $u_0=0$ and $u'=(u_1,\dots,u_{d-1})\notin\mathbb RE'$. For small $\delta>0$ the state is passive and not Gibbs. Let $M=\mathbb ZE_1+\dots+\mathbb ZE_{d-1}$ be the module of level spacings, and let $r$ be its rank: the number of rationally independent spacings. Let $K=\{a\in\mathbb Z^{d-1}:a\cdot E'=0\}$, the lattice of exactly resonant exchanges; it has rank $d-1-r$.

Call $M$ *badly approximable* if there is a $\kappa>0$ with
$$|a\cdot E'|\ge\kappa\,\|a\|_\infty^{-(r-1)}\qquad\text{whenever }a\in\mathbb Z^{d-1}\text{ and }a\cdot E'\ne0.$$
Three cases qualify:
- every commensurate spectrum ($r=1$, $M=g\mathbb Z$, $\kappa=g$);
- every spectrum whose spacings are integer combinations of $1,\theta,\dots,\theta^{r-1}$ for an algebraic integer $\theta$ of degree $r$. For $\alpha=a\cdot E'\ne0$, $|N(\alpha)|\ge1$ while each other conjugate is $O(\|a\|_\infty)$, so $|\alpha|\ge\kappa\|a\|_\infty^{-(r-1)}$ with $\kappa$ explicit;
- in particular, every quadratic irrational gap ratio.

**Theorem 6.9 (resonance-rank law) [P].** If $M$ is badly approximable, then for every $u'\notin\mathbb RE'$ there are constants $0<c\le C$, independent of $\delta$, with
$$c\,\delta^{-1/r}\ \le\ n^*\ \le\ C\,\delta^{-1/r}.$$
In more detail:
- **(a) Lower bound.** $n^*>(\kappa/\delta\|u'\|_1)^{1/r}$.
- **(b) Entropy that sees the resonances.** If $k\cdot u'\ne0$ for some $k\in K$, then $n^*\le C\delta^{-1/r}$ for *every* spectrum of rank $r$, badly approximable or not. When $r=1$ this always applies, because $u'\notin\mathbb RE'$.
- **(c) Entropy blind to them.** If $u'\perp K$, which is automatic when $r=d-1$, and $M$ is badly approximable, then $n^*\le C\delta^{-1/r}$.

*Proof.* Fix a basis $\omega_1,\dots,\omega_r$ of $M$ and write $a\cdot E'=L(a)\cdot\omega$, where $L:\mathbb Z^{d-1}\to\mathbb Z^r$ is onto. Choose a section $s$ of $L$ with $\|s(b)\|_1\le C_s\|b\|_\infty$. Then $\mathbb Z^{d-1}=K\oplus s(\mathbb Z^r)$, and $\|a\|_\infty\le\sum c^+\le\|a\|_1$ throughout.

(a) Let $a$ be violating, so $a\cdot E'<0<a\cdot E'+\delta\,a\cdot u'$, and put $H=\|a\|_\infty$. Then $\kappa H^{-(r-1)}\le|a\cdot E'|<\delta\,a\cdot u'\le\delta\|u'\|_1H$, so $H^r>\kappa/(\delta\|u'\|_1)$, and $\sum c^+\ge H$.

(b) By Dirichlet's theorem, for every $H\ge1$ there is a $b\in\mathbb Z^r$ with $\|b\|_\infty\le H$ and $0<|b\cdot\omega|\le C_\omega H^{-(r-1)}$. The value is nonzero because the $\omega_j$ are rationally independent. Replace $b$ by $-b$ if needed, so that $b\cdot\omega<0$. Pick $k_0\in K$ with $k_0\cdot u'>0$, and put $a=s(b)+tk_0$, with $t$ the least integer for which $\delta\,a\cdot u'>|b\cdot\omega|$. Then $a\cdot E'=b\cdot\omega<0<a\cdot E'+\delta\,a\cdot u'$, and $t=O(H^{-(r-1)}/\delta+H)$, so $\|a\|_1=O(H+H^{-(r-1)}/\delta)$. Take $H=\delta^{-1/r}$.

(c) Since $u'\perp K$, there is a $\tilde u\in\mathbb R^r$ with $a\cdot u'=L(a)\cdot\tilde u$, and $\tilde u\notin\mathbb R\omega$, since otherwise $u'\in\mathbb RE'$. Moreover $|b\cdot\omega|=|s(b)\cdot E'|\ge\kappa C_s^{-(r-1)}\|b\|_\infty^{-(r-1)}$. So it suffices to solve the full-rank problem on $\mathbb Z^r$ for the pair $(\omega,\tilde u)$, at cost at most $C_s\|b\|_\infty$.

Put $m=r$ and normalize $\omega_1=1$. The map $b\mapsto x=(b_2,\dots,b_m,\,b\cdot\omega)$ is unimodular, so its image $\Gamma$ is a lattice of determinant 1. Write $x'$ for its first $m-1$ coordinates. Since $b_1=x_m-\sum_{k\ge2}b_k\omega_k$, we have $\|b\|_\infty\le C_1\max(\|x'\|_\infty,|x_m|)$ with $C_1=\sum_k|\omega_k|$.

For $H\ge1$ let $\Gamma_H=D_H\Gamma$ with $D_H=\mathrm{diag}(H^{-1},\dots,H^{-1},H^{m-1})$; it is again unimodular. Its first minimum, for the cube $[-1,1]^m$, is at least $\lambda_0=\min\{1,(\kappa'/C_1^{m-1})^{1/m}\}$, where $\kappa'=\kappa C_s^{-(r-1)}$. Indeed, suppose $0\ne y=D_Hx$ had $\|y\|_\infty=\lambda<\lambda_0$. Then $|x_m|<1$. So $x'\ne0$, because otherwise $x_m=b_1$ would be a nonzero integer, and hence $\|x'\|_\infty\ge1>|x_m|$. Then $\kappa'\le|x_m|\,C_1^{m-1}\|x'\|_\infty^{m-1}\le C_1^{m-1}\lambda^m$, a contradiction.

By Minkowski's second theorem (Minkowski 1910; Gruber–Lekkerkerker 1987), $\lambda_1\cdots\lambda_m\le1$, so $\lambda_m\le\lambda_0^{-(m-1)}$. By Jarník's inequality (Jarník 1941), the covering radius is at most $\mu_0=\tfrac m2\lambda_0^{-(m-1)}$. Undoing $D_H$: for every target $(T',T_m)$ there is $b\in\mathbb Z^m$ with $\|x'-T'\|_\infty\le\mu_0H$ and $|b\cdot\omega-T_m|\le\mu_0H^{-(m-1)}$.

Now write $b\cdot\tilde u=\tilde u_1(b\cdot\omega)+w\cdot x'$ with $w_k=\tilde u_k-\omega_k\tilde u_1$ for $k=2,\dots,m$; here $w\ne0$. Take $T'=c_0H\,w/\|w\|_2$ with $c_0=2\mu_0\|w\|_1/\|w\|_2$, and $T_m=-2\mu_0H^{-(m-1)}$. Then
$$-3\mu_0H^{-(m-1)}\le b\cdot\omega\le-\mu_0H^{-(m-1)}<0,\qquad w\cdot x'\ge\mu_0\|w\|_1H,$$
so $b\cdot\tilde u\ge\tfrac12\mu_0\|w\|_1H$ once $H$ is large. The exchange $a=s(b)$ violates as soon as $\tfrac12\delta\mu_0\|w\|_1H>3\mu_0H^{-(m-1)}$, that is, $H^m>6/(\delta\|w\|_1)$. Its cost is $O(H)$. $\square$

**Theorem 6.9′ (almost every spectrum) [P].** For Lebesgue-almost every $E'\in\mathbb R^{d-1}$ and every $u'\notin\mathbb RE'$,
$$\lim_{\delta\to0}\frac{\ln n^*}{\ln(1/\delta)}=\frac1{d-1}.$$
For a qutrit, or a two-port engine, the exponent is $\tfrac12$ for almost every gap ratio. The commensurate ratios, with exponent 1, form a null set: *generic spectra are quadratically cheaper than resonant ones.*

*Proof.* Normalize $E'_1=1$ and fix $\epsilon>0$. Take $a'=(a_2,\dots,a_{d-1})\ne0$ with $\|a'\|_\infty=H$. The set of $(E'_2,\dots,E'_{d-1})$ in a unit cube for which $a'\cdot(E'_2,\dots,E'_{d-1})$ lies within $H^{-(d-2)-\epsilon}$ of an integer has measure $2H^{-(d-2)-\epsilon}$, and there are at most $CH^{d-3}$ such $a'$. The sum over $H$ converges. By Borel–Cantelli, almost every spectrum therefore has full rank and satisfies $|a\cdot E'|\ge c_\epsilon\|a\|_\infty^{-(d-2)-\epsilon}$ for all $a\ne0$; note that $\|a\|_\infty\le C\|a'\|_\infty$ whenever $|a\cdot E'|<1$.

This is the hypothesis of Theorem 6.9 with $\kappa$ replaced by $c_\epsilon\|a\|_\infty^{-\epsilon}$. Part (a) then gives $n^*\ge c\,\delta^{-1/(d-1+\epsilon)}$. The proof of (c) goes through with $\lambda_0\ge cH^{-\epsilon/(d-1)}$ and $\mu_0\le CH^{\epsilon}$, and gives $n^*\le C\delta^{-(1+\epsilon)/(d-1)}$. $\square$

Certificates P6.K6c and P7.H7a check the law with exact integer surrogates. Every answer is unchanged between the $2^{-40}$ and $2^{-43}$ grids, and every witness is re-verified at 50 digits on the true spectrum. Here $\theta^3=\theta+1$ (the plastic number) and $\psi^4=\psi+1$.

| levels | $E'$ | $r$ | entropy sees $K$? | fitted exponent | predicted |
|---|---|---|---|---|---|
| 4 | $1,2,3$ | 1 | yes | 0.996 | 1 |
| 4 | $1,\varphi,2$ | 2 | yes | 0.498 | 1/2 |
| 4 | $1,\varphi,2$ | 2 | no | 0.515 | 1/2 |
| 5 | $1,\varphi,2,1+\varphi$ | 2 | yes | 0.477 | 1/2 |
| 4 | $1,\theta,\theta^2$ | 3 | full rank | 0.351 | 1/3 |
| 5 | $1,\theta,\theta^2,1+\theta$ | 3 | yes | 0.353 | 1/3 |
| 5 | $1,\theta,\theta^2,1+\theta$ | 3 | no | 0.343 | 1/3 |
| 5 | $1,\psi,\psi^2,\psi^3$ | 4 | full rank | 0.244 | 1/4 |

Every computed $n^*$ lies above bound (a). With blind entropy and golden spacings, the thresholds are exactly Fibonacci numbers: $13,34,89,233,610,1597$.

One pre-registered check failed, and it is retained. For the very well approximable spectrum of Remark 6.9″, with entropy that sees $K$, a local exponent reached $0.604$ against a ceiling of $0.60$. A ceiling on local exponents at finite $\delta$ cannot absorb the constant in (b). The post-diagnosis certificate P7b (not blind) tests the actual claim:
- the constructive exchange of (b) violates passivity at every $\delta$ down to $10^{-30}$;
- its cost times $\delta^{1/2}$ stays at or below $14.3$, inside the proof's constant of $47$;
- at $\delta=10^{-7}$ the construction is optimal ($n^*=10723$).

For Theorem 6.9′, certificate P7.H7b samples 300 random gap ratios. At $\delta=10^{-12}$, 98.7% of local exponents lie in $[0.4,0.6]$, against 88.3% at $10^{-6}$, and the median is $0.525$. The pre-registered golden control failed narrowly, for the same reason: its exponent was $0.5801$ at $\delta=10^{-3}$, where $n^*=F_{10}=55$. P7c (not blind) confirms that $n^*\delta^{1/2}\in[0.86,2.22]$ for every $\delta$ from $10^{-3}$ to $10^{-70}$, and that local exponents lie within $0.0083$ of $\tfrac12$ below $10^{-40}$.

**Remark 6.9″ (very well approximable spectra oscillate) [P sketch].** Suppose the convergent denominators of a gap ratio satisfy $q_{k+1}\approx q_k^{K}$. Then the local exponent swings between about $1/(K+1)$ and $K/(K+1)$.
- It dips just above $\delta\approx1/(q_kq_{k+1})$ when $p_k/q_k$ lies on the window's side.
- On the other side it rises, because the nearest admissible fractions are intermediate fractions of denominator about $1/(q_kx\delta)$.

For partial quotients $a_{k+1}=q_k^2$ ($K=3$), certificate P7.H7b(iii) finds exponents spanning $[0.26,0.76]$ for $\delta$ from $10^{-3}$ to $10^{-70}$. Such spectra form a null set, but they show that Theorem 6.9′ cannot be upgraded to every spectrum. The lower bound genuinely needs a Diophantine condition. The upper bound, when the entropy sees $K$, does not: P7b finds $n^*\le5.7\times10^{9}\ll\delta^{-1/2}$ at $\delta=10^{-30}$.

**Corollary 6.9a (several reservoirs) [P].** Consider $k$ qubit ports in Gibbs states, with gaps $\varepsilon_j>0$ and inverse temperatures $\beta_j$, not all equal. The least $n$ for which the $n$ copies of the joint state are not passive for $\sum_jH_j$ is
$$n^*=\min\Big\{\|m\|_\infty:\ m\in\mathbb Z^k,\ \ m\cdot\varepsilon<0<\sum_j\beta_j\varepsilon_jm_j\Big\}.$$
Near equilibrium, $\beta_j=\beta(1+\delta v_j)$ with $v$ not constant. Commensurate gaps give $n^*\asymp1/\delta$. Gaps $(1,\theta,\dots,\theta^{k-1})$, with $\theta$ an algebraic integer of degree $k$, give $n^*\asymp\delta^{-1/k}$. For $k=2$ and golden gaps this is Proposition 6.8(c). For three reservoirs with plastic-number gaps the threshold scales as $(T/\Delta T)^{1/3}$.

*Proof.* Apply Lemma 6.2 to the $2^k$ joint levels. A relation vector $c$ moves $m_j=\sum_{\ell:\,\ell_j=1}c_\ell$ net quanta into port $j$, and it has $c\cdot E=m\cdot\varepsilon$ and $c\cdot f=\sum_j\beta_j\varepsilon_jm_j$. As in Corollary 6.7, $\sum c^+\ge|m_j|$ for every $j$. Equality is attained with $n=\|m\|_\infty$ copies, each of which changes every port by at most one quantum. The scaling follows from Theorem 6.9(a)–(c), applied to the lattice $\mathbb Z^k$ with $E'=\varepsilon$ and $u'=(v_j\varepsilon_j)$. The proofs of (a)–(c) use only that the cost lies between $\|a\|_\infty$ and $\|a\|_1$, which $\|m\|_\infty$ does, and $u'\notin\mathbb R\varepsilon$ because $v$ is not constant. $\square$

Certificate P6.K6e confirms the formula against brute-force exact ergotropy on 24 instances ($n\le4$). Near equilibrium, the fitted exponents are $0.328$ for plastic gaps against $0.975$ for gaps $(1,2,3)$. *More reservoirs make smaller engines.*

**Corollary 6.9b (triple reduction fails) [P].** The four-level threshold is not the least of the thresholds of its three-level restrictions.
- *(i) Exactly.* Take $E=(0,2,3,4)$ and $p\propto(1,\tfrac12,\tfrac14,\tfrac1{16})$. Then $n^*=2$, through the exchange $c=(1,-1,-1,1)$: one quantum pair moves from the middle two levels to the outer two. Each of the four three-level restrictions is still passive at $n=2$; their thresholds are $5,3,3,5$.
- *(ii) Asymptotically.* Take $E=(0,1,\theta,\theta^2)$ with $\theta$ the plastic number. Every triple has a cubic irrational gap ratio and an entropy ratio within $O(\delta)$ of it. By Roth's theorem (Roth 1955), its threshold is therefore at least $c_\epsilon\,\delta^{-1/(2+\epsilon)}$, while $n^*\le C\delta^{-1/3}$ by Theorem 6.9(c). So the ratio of $n^*$ to the best triple threshold tends to $0$.

*Proof.* (i) $c\cdot E=-1<0<\ln2=c\cdot f$. The four triples have the interval pairs $(\tfrac12,\tfrac23)$, $(\tfrac14,\tfrac12)$, $(\tfrac12,\tfrac34)$ and $(\tfrac13,\tfrac12)$, whose simplest fractions $\tfrac35,\tfrac13,\tfrac23,\tfrac25$ have denominators $5,3,3,5$ (Theorem 6.6). (ii) A fraction $k/m$ in a window of width $C\delta$ at an algebraic irrational $x$ satisfies $c_\epsilon m^{-2-\epsilon}\le|x-k/m|<C\delta$. $\square$

Certificate P6.K6b confirms (i) by brute-force ergotropy. On 396 small random instances, triple reduction fails on 33. At $\delta=10^{-8}$ in (ii), $n^*=595$ while the best triple needs $6458$ copies.

**Corollary 6.9c (two harmonic modes: the order of the engine) [P].** Two harmonic oscillators in Gibbs states at different temperatures are never jointly passive, even for a single copy. The least total order $|\Delta n_A|+|\Delta n_B|$ of a work-extracting exchange of levels is $k+m$, for the simplest fraction $k/m$ in the Carnot window of Corollary 6.7. The least $\max(|\Delta n_A|,|\Delta n_B|)$ is $\max(k,m)$.

*Proof.* Apply Lemma 6.1 to one copy. The levels $(n_A,n_B)$ and $(n_A+m,\,n_B-k)$ form an inverted pair exactly when $k/m$ lies in the window; this is the computation of Corollary 6.7. The ladders contain such pairs for every $k$ and $m$. The simplest fraction minimizes $k$ and $m$ simultaneously (P5.K2d). $\square$

*Reading [A].* For qubit ports, the arithmetic counts copies. For oscillator ports it counts the order of the nonlinear process, $a^{\dagger m}b^{k}$ driven at the mismatch $|m\varepsilon_A-k\varepsilon_B|$. Each extra quantum costs a factor of the nonlinearity — for trapped-ion modes, roughly the Lamb–Dicke parameter. So the resonance penalty becomes an *exponential* penalty in the rate. Certificate P7.H7d confirms the corollary by brute force on 32 pairs of ten-level ladders.

**Corollary 6.9d (a conserved charge can raise the exponent) [P].** Under the symmetry restriction of §7, with integer charges $q$, Lemma 6.2 confines $a$ to the charge-neutral sublattice $\Lambda_q=\{a:a\cdot q'=0\}$. The free states become the generalized Gibbs states (Theorem 7.2). Theorem 6.9 then applies on $\Lambda_q$ with three changes:
- $M$ is replaced by the module $M_q=\{a\cdot E':a\in\Lambda_q\}$ of charge-neutral spacings;
- $r$ is replaced by $r_q=\mathrm{rank}\,M_q\le r$;
- $\delta$ measures the distance from the generalized Gibbs family.

The threshold can only grow, $n^*_q\ge n^*$, and when $M$ and $M_q$ are badly approximable the exponent rises from $1/r$ to $1/r_q$.

*Proof.* $\Lambda_q\cong\mathbb Z^{d-2}$, and the cost restricted to it is still squeezed between $\|a\|_\infty$ and $\|a\|_1$. A state is generalized Gibbs exactly when $f$ restricted to $\Lambda_q$ is proportional to $E$ restricted to $\Lambda_q$, because $q$ vanishes there. Shrinking the admissible set can only raise the minimum. $\square$

*Example.* Take five levels with $E'=(1,\theta,\theta^2,1+\theta)$ (plastic $\theta$, $r=3$) and charge $q'=(1,1,1,2)$. Then $M_q$ is spanned by $\theta-1$ and $\theta^2-1$, so $r_q=2$. Certificate P8 measures exponent $0.550$ with the charge, against $0.353$ without it. The ratio $n^*_q/n^*$ grows from $1.75$ to $7.1$ between $\delta=10^{-2}$ and $10^{-6}$. *A conservation law removes resonance directions, and the engine grows.*

**Proposition 6.9e (echo–yield duality) [P + A].** Let $\omega_1,\dots,\omega_r$ be a basis of $M$ and $\alpha_j=\omega_j/\omega_1$. Let $q_{\rm rec}(\varepsilon)$ be the least $q\ge1$ with $\max_j\|q\alpha_j\|<\varepsilon$; at the times $2\pi q/\omega_1$, every level spacing returns to within $2\pi\varepsilon$ of its initial phase.
- If $M$ is badly approximable, then $q_{\rm rec}(\varepsilon)\asymp\varepsilon^{-(r-1)}$ and $n^*(\delta)\asymp\delta^{-1/r}$.
- For almost every spectrum, both hold with exponents correct up to $\pm o(1)$.

The *echo exponent* $e=r-1$ of the ledger (the base, read in time) and the *yield exponent* $y=1/r$ of the copy lift therefore satisfy
$$y\,(e+1)=1.$$

*Proof.*
- The upper bound on $q_{\rm rec}$ is Dirichlet's simultaneous approximation theorem.
- For the lower bound: a badly approximable linear form $(1,\alpha_2,\dots,\alpha_r)$ is also badly approximable for simultaneous approximation, by Khinchin's transference principle (Cassels 1957, Ch. V) [A].
- The almost-every statement follows from Borel–Cantelli, as in Theorem 6.9′.
- The yield half is Theorems 6.9 and 6.9′. $\square$

*Reading [A].* The ledger's recurrence and the copy lift read one object: the spacing module $M$ and its dual torus $\mathrm{Hom}(M,\mathbb R/2\pi\mathbb Z)$.
- Time evolution is the line $t\mapsto(t\omega_j)_j$ on the torus.
- A copy exchange is an element $b\in M$, whose phase at time $t$ is $t\,(b\cdot\omega)$.
- Recurrence asks when the line returns near the origin (simultaneous approximation, Corollary 4.6). This is the base ledger watched in time; the time lift proper (causality, §5) plays no role in it.
- The copy lift asks which lattice element is nearly invariant along the line (a small linear form).
- The symmetry restriction passes to a sublattice and a quotient torus (Corollary 6.9d).

Transference is the quantitative form of this Pontryagin duality. The equally spaced ledger of Corollary 4.6, which revives exactly at $2\pi/\delta_{\rm spacing}$, is the case $r=1$: perfect echo and maximal threshold. *What echoes, hoards; what forgets, yields.*

Certificate P7.H7f measures echo exponents $0.999$ (golden, $r=2$) and $1.82$ (plastic, $r=3$), and gives $y(e+1)=0.996,\ 0.996,\ 0.990$ for $r=1,2,3$.

**Platform estimates [A].** Table 6.1 is for two ports with window $(x,\,x(1+\Delta T/T))$. It lists the copy threshold for qubit ports and, in brackets, the process order $k+m$ for harmonic modes (certificate P7.H7e).

| $\Delta T/T$ | $x=\tfrac12$ (harmonic) | $x=1/\sqrt3$ (two-ion axial modes) | $x=1/\varphi$ (golden) |
|---|---|---|---|
| $10^{-1}$ | 11 [17] | 5 [8] | 3 [5] |
| $10^{-2}$ | 101 [152] | 19 [30] | 21 [34] |
| $10^{-3}$ | 1001 [1502] | 45 [71] | 55 [89] |
| $10^{-4}$ | 10001 [15002] | 168 [265] | 144 [233] |
| $10^{-6}$ | $10^{6}+1$ | 2340 [3691] | 987 [1597] |
| $10^{-10}$ | $10^{10}+1$ | 191861 | 121393 |

- *Equally spaced ladders* are the worst case, with $n^*\approx T/\Delta T$ (Theorem 6.9 with $r=1$). Examples are oscillators and a spin in a linear Zeeman field.
- *Trapped-ion axial modes* have frequency ratio $\sqrt3$ for two ions, and $\sqrt3$ and $\sqrt{29/5}$ for three (James 1998). These are quadratic irrationals, hence badly approximable, so ion-mode engines sit on the $(T/\Delta T)^{1/2}$ branch by construction.

  As oscillators, the modes need a process of order $k+m$, and each order costs roughly a Lamb–Dicke factor $\eta_{\rm LD}\sim0.1$ in coupling. At $\Delta T/T=10^{-1}$, a golden pair needs a fifth-order process and an ion pair an eighth-order one, against seventeenth order for a harmonic $2{:}1$ pair: about twelve orders of magnitude in coupling.
- *A transmon qutrit* with anharmonicity $|\alpha|/\omega\approx0.05$ has gap ratio $\omega_{01}/(\omega_{01}+\omega_{12})$ about $\eta\approx0.0128$ above $\tfrac12$. If its two transitions see temperatures differing by $\Delta T$, its window has width $w\approx\tfrac14\Delta T/T$. Proposition 6.8a then gives two regimes:
  - if the upper transition is the colder one by more than about $|\alpha|/\omega$, the $1{:}2$ exchange is admissible and *two copies* suffice;
  - with the opposite sign, the threshold plateaus below $1/(2\eta)+2\approx41$ instead of growing like $T/\Delta T$.

  P7.H7e checks both regimes in the two-port normalization.
- *A nitrogen-vacancy spin* ($D=2.87$ GHz, $\gamma=28$ GHz/T, field along the axis) has levels $0$ and $D\mp\gamma B$. Its gap ratio $(D-\gamma B)/(D+\gamma B)$ is therefore set by the field. The resonant ratio $\tfrac12$ sits at $B\approx34.2$ mT and the golden ratio at $B\approx24.2$ mT. A 10 mT change moves the spin from the $T/\Delta T$ branch to the $(T/\Delta T)^{1/2}$ branch.

These are structural estimates. They locate the first extractable exchange, not its yield, and they assume additive energies and collective unitaries.

**Remark 6.9f (what remains open).**
- *A closed form for $d\ge4$.* The minimizer is the least-cost lattice point of a dihedral wedge, and it generically has full support. A Stern–Brocot analogue would be a multidimensional continued fraction (Klein polyhedra) adapted to the cost $\sum c^+$; we do not have one.
- *Blind entropy at intermediate rank without a Diophantine condition.* When $u'\perp K$ and $M$ is not badly approximable, only the almost-every statement is available.
- *Fluctuations.* For almost every spectrum, $n^*\delta^{1/r}$ fluctuates without converging. Its limiting distribution — a Gauss–Kuzmin law for copy thresholds — is open [C].
- *The size of the prize.* $n^*$ says when work first becomes extractable, not how much. The ergotropy at threshold is small near equilibrium, and its scaling is open.
- *The idealization.* Copies stand for global unitaries on independent systems, with additive energy. For oscillator ports, Corollary 6.9c replaces copies by the order of the nonlinear process, which is the more physical count.

*Reading [A].* Rationally independent spacings act like extra reservoirs. Each one adds a direction in which an exchange can sit slightly off resonance, and the exponent is one over the number of such directions. Commensurate spectra, such as harmonic ladders, are the worst case. A conserved charge removes directions, and a detuning adds contrast. Copy thresholds therefore probe the arithmetic rank of a spectrum, the same rank that sets how long its ledger takes to echo.

### One spectrum, many filters

**Theorem 6.10 (one spectrum, many filters) [P].** Let $\rho=e^{-\beta H}/Z$ and let $A$ be an observable. Define the dissipation spectrum $\chi''(\omega)=\pi\sum_{ij}(p_i-p_j)|A_{ij}|^2\delta(\omega-\omega_{ij})$ with $\omega_{ij}=E_j-E_i$ ($\hbar=1$), write $x=\beta\omega/2$, and let $\sigma_{\rm el}$ be the elastic (degenerate-pair) part. Then:

*(a) Variances.* In units of $\frac1\pi\int_0^\infty(\cdot)\,\chi''\,d\omega$, with $\sigma_{\rm el}$ added to the first two:

| Quantity | Experiment | Filter |
|---|---|---|
| symmetrized variance $\operatorname{Var}(A)$ | watch | $\coth x$ |
| isothermal susceptibility $\times T$ | push | $1/x$ |
| quantum variance $\operatorname{Var}-T\chi$ (Frérot–Roscilde 2016) | watch − push | $\coth x-1/x$ |
| Wigner–Yanase skew information $-\tfrac12\operatorname{tr}[\sqrt\rho,A]^2$ | — | $\tanh(x/2)$ |

*(b) Every Petz monotone metric is a filter.* Let $f$ be operator monotone with $f(1)=1$ and $f(t)=tf(1/t)$. The monotone metric of the rotation family $e^{-iA\theta}\rho e^{iA\theta}$ is
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
so $\operatorname{Var}_Q\le I_{WY}\le\tfrac14F_{\rm SLD}\le\tfrac14F_{WY}\le\tfrac14F_{KM}\le\tfrac14F_{RLD}$. As $x\to0$ every filter collapses to its classical form: $1/x$ for variances, $2x$ for metrics.

*Proof.* Each entry is a sum over Bohr pairs, using $p_i/p_j=e^{2x}$, $\frac{p_i+p_j}{p_i-p_j}=\coth x$, and $\frac{(\sqrt{p_i}-\sqrt{p_j})^2}{p_i-p_j}=\tanh\frac x2$. For (b), $\frac{(p_i-p_j)^2}{p_jf(p_i/p_j)}=(p_i-p_j)\frac{e^{2x}-1}{f(e^{2x})}$. The closed forms follow by rewriting in exponentials; the Wigner–Yanase–Dyson form uses $e^{2\alpha x}-1=2e^{\alpha x}\sinh\alpha x$.

For (c), in order:
- $\coth x-\frac1x\le\tanh\frac x2$ reduces, with $u=x/2$, to $u\le\sinh u\cosh u$;
- $\tanh\frac x2\le\tanh x$ because $\tanh$ is increasing;
- $\tanh x=\frac{2t}{1+t^2}\le2t$ with $t=\tanh\frac x2$;
- $2\tanh\frac x2\le x$ from $\tanh y\le y$;
- $x\le\frac12\sinh2x$ from $\sinh y\ge y$.

The middle inequalities $I_{WY}\le\frac14F_{\rm SLD}\le2I_{WY}$ recover Luo (2004).

Certificates: P1.C2 (the four original lines, by three independent routes, to $10^{-10}$); P4.R5 (exact closed forms; skew information and the Wigner–Yanase and RLD metrics from their matrix formulas, to $10^{-8}$ or better). $\square$

*Reading.* There is one dissipation spectrum, and every experiment and every information metric is a frequency filter applied to it. "Bures = watching, Kubo–Mori = pushing" is a statement about the *two canonical experiments*, not a dichotomy of the family. The SLD metric is dual to the symmetrized (watched) covariance, and the Kubo–Mori metric is dual to the canonical (pushed) covariance. Every other Petz metric is a different filter on the same measured $\chi''$ (Shitara–Ueda 2016). The Wigner–Yanase–Dyson family interpolates continuously from Kubo–Mori ($\alpha\to0$) to Wigner–Yanase ($\alpha=\tfrac12$).

### A circuit reading of the Petz classification

Which filters $w$ in Theorem 6.10 define legitimate quantum Fisher metrics — that is, metrics that can only decrease under every quantum channel? Petz's classification answers in terms of operator monotone functions. The following reading turns that answer into circuit theory.

**Theorem 6.11 (monotone metrics are self-dual resistor–inductor networks) [P for (c); imported for (a), (b)].** Let $f:(0,\infty)\to(0,\infty)$ with $f(1)=1$, and let $w_f(x)=(e^{2x}-1)/f(e^{2x})$.
- **(a)** (Petz 1996) The metric $g_f$ is monotone under every CPTP map in every dimension iff $f$ is operator monotone and $f(t)=tf(1/t)$.
- **(b)** (Löwner 1934; Kubo–Ando 1980) $f$ is operator monotone iff
$$f(t)=\int_{[0,\infty]}\frac{(1+\lambda)\,t}{\lambda+t}\,dm(\lambda)$$
for a positive measure $m$ on $[0,\infty]$, with the atoms at $\lambda=0$ and $\lambda=\infty$ read as the constant $1$ and the function $t$. Then $f(1)=1$ iff $m$ is a probability measure. *Circuit identification (here):* each integrand is the impedance, at the positive real frequency $s=t$, of a resistor $1+\lambda$ in parallel with an inductor $(1+\lambda)/\lambda$, and the atoms at $0$ and $\infty$ are a unit resistor and a unit inductor. So $f$ is the driving-point impedance of a (possibly continuous) series connection of parallel resistor–inductor cells. This is a passive RL network in canonical form (Foster 1924; Cauer 1926), with unit impedance at unit frequency.
- **(c)** The following are equivalent:
  1. $f(t)=tf(1/t)$;
  2. $w_f$ is odd, i.e. invariant up to sign under emission ↔ absorption;
  3. $m$ is invariant under $\lambda\mapsto1/\lambda$;
  4. the network is invariant under the exchange $Z(s)\mapsto sZ(1/s)$, which replaces every resistor by an inductor of equal value, every inductor by a resistor of equal value, and the cell $\lambda$ by the cell $1/\lambda$.

*Consequently, a frequency filter $w$ on the dissipation spectrum defines a monotone quantum Fisher metric iff $w$ is odd and $t\mapsto(t-1)/w(\tfrac12\ln t)$ is the impedance of a passive resistor–inductor network.*
- The arithmetic mean (Bures/SLD) is the series connection of $R=\tfrac12$ and $L=\tfrac12$.
- The harmonic mean (RLD) is a single parallel cell with $R=L=2$.
- Kubo and Ando's bounds on symmetric operator means place every other admissible network between these two, in accordance with $g_{\rm SLD}\le g_f\le g_{\rm RLD}$.

*Proof.* (a) and (b) are the cited theorems, and the representing measure in (b) is unique. The circuit identification is the computation
$$\frac{R\cdot Ls}{R+Ls}=\frac{(1+\lambda)s}{\lambda+s}\quad\text{for }R=1+\lambda,\ L=(1+\lambda)/\lambda,$$
together with the fact that every cell equals $1$ at $s=1$.

For (c), note that $w_f(-x)=(e^{-2x}-1)/f(e^{-2x})$. This equals $-w_f(x)$ iff $f(e^{-2x})=e^{-2x}f(e^{2x})$, i.e. $f(1/t)=f(t)/t$. The exchange sends a resistor $a$ to an inductor $as$, an inductor $bs$ to a resistor $b$, and the cell $\frac{(1+\lambda)s}{\lambda+s}$ to $\frac{(1+\lambda)s}{1+\lambda s}=\frac{(1+\lambda^{-1})s}{\lambda^{-1}+s}$, which is the cell with parameter $1/\lambda$. By uniqueness of $m$, $sf(1/s)=f(s)$ iff $m$ equals its image under $\lambda\mapsto1/\lambda$.

Named realizations:
- SLD: $m=\tfrac12\delta_0+\tfrac12\delta_\infty$;
- RLD: $m=\delta_1$;
- $\sqrt t$: $dm=\lambda^{-1/2}d\lambda/(\pi(1+\lambda))$, a probability measure invariant under $\lambda\mapsto1/\lambda$;
- Wigner–Yanase: $\tfrac14\delta_0+\tfrac14\delta_\infty$ plus half the $\sqrt t$ measure;
- Kubo–Mori: $\frac{t-1}{\ln t}=\int_0^1t^s\,ds$, a continuum of such power elements.

Certificates P5.H3.K3a, K3b, and K3d (exact). $\square$

**Remark 6.12 (a symmetric filter that is not a network) [witness].** The quadratic mean $f(t)=\sqrt{(1+t^2)/2}$ satisfies $f(1)=1$ and $f(t)=tf(1/t)$, so its filter is odd. But it is not a resistor–inductor impedance: its analytic continuation has branch points at $t=\pm i$, off the negative real axis, like a resonant element. It is not operator monotone either. With $A=\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}$ and $B=\begin{psmallmatrix}2&1\\1&1\end{psmallmatrix}$, one has $B-A=\operatorname{diag}(1,0)\succeq0$, yet $\det\big(f(B)-f(A)\big)<0$ (certificate P5.K3e, exact). Equivalently, $\sqrt{(1+t^2)/2}\ge(1+t)/2$, so its "metric" lies below the Bures metric, which is the smallest monotone metric (Petz 1996).

Accordingly, it violates data processing. The violation appears under *pinching* — complete dephasing in a basis, which is the port reading that basis — and under partial trace. There the quadratic-mean metric grows by up to $11.5\%$, while every Petz member contracts (certificate P5.H3.K3c′). The pre-registered search over random channels, K3c, found no violation; it is retained as a failure of the search design, not of the claim. In the language of §9, a metric that is not a passive network would let *reading* appear to create information.

**Corollary 6.13 (the second law as a relative entropy) [P].** For every unitary $U$,
$$D(U\rho U^\dagger\|\rho)=\beta W,\qquad W=\operatorname{tr}(U\rho U^\dagger H)-\operatorname{tr}(\rho H)\ge0 .$$
*Proof.* $\ln\rho=-\beta H-\ln Z$, and entropy is unitarily invariant. Certificate P1.C2.h. $\square$

**Proposition 6.14 (the coth law) [P].** *Exact identity.* If two opposite elementary processes occur at rates $r_\pm$ with $r_+/r_-=e^{2u}$, then
$$\frac{\text{symmetric fluctuation}}{\text{antisymmetric response}}=\frac{r_++r_-}{r_+-r_-}=\coth u\ \ge\ \frac1u .$$
*Three settings in which this identity is the operative kernel:*
1. **Quantum FDT**, exactly. Per Bohr mode, $\operatorname{Var}/(T\chi)=u\coth u$ with $u=\beta\hbar\omega/2$ (Theorem 6.10).
2. **Tunnel junction**, exactly in the regime of energy-independent, Poissonian tunneling. There $\Gamma_+/\Gamma_-=e^{eV/k_BT}$, so $S_I/(2eI)=\coth\frac{eV}{2k_BT}$. This interpolates from Johnson noise ($4k_BTG$, as $u\to0$) to Schottky shot noise ($2eI$, as $u\to\infty$), and the crossover is used as a primary thermometer (Spietz et al. 2003).
3. **Unicyclic Markov process** (a biased ring with affinity $A$), exactly. With $u=A/2$, $\sigma\operatorname{Var}(J)/J^2=2u\coth u$. The thermodynamic uncertainty relation's bound, $2$, is attained in the linear limit.

*What is and is not unified.* In these three settings, the quantum FDT inequality $\operatorname{Var}\ge T\chi$ and the unicyclic TUR both reduce to $u\coth u\ge1$. The general TUR, for arbitrary Markov networks (Barato–Seifert 2015; Gingrich et al. 2016), is a bound proven by other means and is not implied by this identity; the coth form is its unicyclic instance. In each setting, the ratio $e^{2u}$ is supplied by local detailed balance — the KMS condition of the bath that drives each elementary transition — which is why the identity belongs to the copy lift. Certificate P4.R8.

---

## 7. The symmetry restriction: which cycles count

The lifts of §§5–6 enlarge the family of tests. A symmetry acts the other way: it restricts which cycles are admissible. If cycles must conserve charges $Q_1,\dots,Q_m$ (with $[H,Q_k]=0$), fewer cycles are tested, passivity is easier to satisfy, and the family of free states is larger. This reverses a common intuition — that conserved quantities add constraints and so strengthen a principle. Here they weaken the demand, and the result is a larger free family, with one chemical potential per charge.

**Theorem 7.1 (generalized and non-Abelian thermal states are completely passive) [P].** Let $[H,Q_k]=0$ for all $k$, where the $Q_k$ need **not** commute with one another, and let $\rho=e^{-\beta(H-\sum_k\mu_kQ_k)}/Z$ with $\beta\ge0$. Then for every $n$ and every unitary $U$ on $n$ copies that commutes with every total charge $Q_k^{(n)}$,
$$\operatorname{tr}(U\rho^{\otimes n}U^\dagger H_n)\ \ge\ \operatorname{tr}(\rho^{\otimes n}H_n).$$

*Proof.* Because operators on different copies commute, $\rho^{\otimes n}=e^{-\beta\tilde H_n}/Z^n$ with $\tilde H_n=H_n-\sum_k\mu_kQ_k^{(n)}$. So $\rho^{\otimes n}$ is Gibbs for $\tilde H_n$, and passive for it under all unitaries (Lemma 6.1). Since $U$ commutes with each $Q_k^{(n)}$, $\operatorname{tr}(U\rho^{\otimes n}U^\dagger Q_k^{(n)})=\operatorname{tr}(\rho^{\otimes n}Q_k^{(n)})$, and the $\tilde H_n$ inequality becomes the $H_n$ inequality. $\square$

**Theorem 7.2 (converse for commuting charges) [P].** Let $H,Q_1,\dots,Q_m$ commute, with a joint eigenbasis $|i\rangle$ carrying energies $E_i$ and integer charge vectors $q_i$. Let $\rho$ be faithful and diagonal in this basis. Suppose $E\notin\operatorname{span}\{\mathbf1,q^{(1)},\dots,q^{(m)}\}$, i.e. energy is not a function of the charges. Then $\rho$ is completely passive under charge-conserving cycles iff
$$p_i\propto e^{-\beta E_i-\lambda\cdot q_i}\quad\text{for some }\beta\ge0,\ \lambda\in\mathbb R^m ,$$
that is, iff $\rho$ is a generalized Gibbs state with $\beta\mu_k=-\lambda_k$. If $E$ is a function of the charges, every such $\rho$ is passive under charge-conserving cycles.

*Proof.* (⇐) is Theorem 7.1.

(⇒) Charge-conserving unitaries on $n$ copies are block-diagonal over total-charge sectors, so Lemma 6.2 applies with the added condition $\sum c_iq_i=0$. The argument of Theorem 6.3 then runs verbatim on the lattice
$$L_q=\{c\in\mathbb Z^d:\ \textstyle\sum c_i=0,\ \sum c_iq_i=0\},$$
whose real span is $\operatorname{span}\{\mathbf1,q^{(1)},\dots,q^{(m)}\}^\perp$. The hypothesis $E\notin\operatorname{span}\{\mathbf1,q\}$ supplies a vector $d$ with $\phi_E(d)<0$, and the conclusion becomes $f-\beta E\in\operatorname{span}\{\mathbf1,q^{(k)}\}$.

If $E\in\operatorname{span}\{\mathbf1,q\}$, a charge-conserving unitary cannot change the energy at all. $\square$

Certificate P4.R4:
- **K4c.** A GGE with $\mu\neq0$ is active under unrestricted cycles at $n=1$, but passive under charge-conserving cycles through $n=3$.
- **K4d.** A non-GGE state that is passive at $n=1$ turns active under charge-conserving cycles at $n^*=5$.
- **K4e.** When $E\in\operatorname{span}\{\mathbf1,q\}$, a non-GGE state stays passive.

**Remark 7.3 (a restriction, not a further demand).** The symmetry does not strengthen the demand in order to "select" a state. It restricts the admissible processes, and each conserved charge adds one Lagrange multiplier — one effort, $\mu_k$ — to the free family, exactly as in the charge row of the effort–flow table (§2.1). Demanding passivity over *all* cycles would instead exclude every GGE with $\mu\neq0$ (K4c).

For non-commuting charges, Theorem 7.1 gives the forward direction exactly. The literature's converse concerns a different setting. With a reference frame and batteries for the charges, and with work valued by $H-\sum_k\mu_kQ_k$, the non-Abelian thermal state is the unique completely passive state (Yunger Halpern et al. 2016; Guryanova et al. 2016). That statement is Pusz–Woronowicz applied to the operator $H-\mu\cdot Q$ under all unitaries. Lostaglio–Jennings–Rudolph (2017) show, moreover, that the maximum-entropy state is passive for that combination but not for each charge separately. The statement of this section is stricter: energy is the only work, the cycles commute with every total charge, and no frame or battery is supplied beyond the copies themselves. For that statement we prove the converse for states without orientation (Theorem 7.4), give exact witnesses that oriented non-thermal states are activated (Proposition 7.5), and state what remains (Open Problem 7.6).

### Strictly symmetric cycles with non-commuting charges

Let a compact connected Lie group $G$, generated by the charges, act on $\mathcal H_S=\bigoplus_\lambda V_\lambda\otimes M_\lambda$, with irreducible $V_\lambda$ of dimension $d_\lambda$ and multiplicity spaces $M_\lambda$. Since $[H,Q_k]=0$, $H=\bigoplus_\lambda I_{V_\lambda}\otimes H_\lambda$. A unitary on $n$ copies is *strictly symmetric* if it commutes with every total charge $Q_k^{(n)}$, equivalently with the collective action $U_g^{\otimes n}$. Decompose $\mathcal H_S^{\otimes n}=\bigoplus_\Lambda V_\Lambda\otimes M_\Lambda^{(n)}$ under that action, so that $H_n=\bigoplus_\Lambda I\otimes H_{n,\Lambda}$.

**Lemma 7.4a (multiplicity form of strict passivity) [P].** $\rho^{\otimes n}$ is passive under strictly symmetric cycles iff, for every $\Lambda$, the multiplicity marginal
$$\sigma^{(n)}_\Lambda=\operatorname{tr}_{V_\Lambda}\big(P_\Lambda\,\rho^{\otimes n}P_\Lambda\big)$$
is passive for $H_{n,\Lambda}$ under all unitaries of $M^{(n)}_\Lambda$.

*Proof.* By Schur's lemma the strictly symmetric unitaries are exactly the unitaries of the commutant $\bigoplus_\Lambda I_{V_\Lambda}\otimes\operatorname{End}(M^{(n)}_\Lambda)$. For $U=\bigoplus_\Lambda I\otimes U_\Lambda$, $\operatorname{tr}(U\rho^{\otimes n}U^\dagger H_n)=\sum_\Lambda\operatorname{tr}(U_\Lambda\sigma_\Lambda U_\Lambda^\dagger H_{n,\Lambda})$, and the $U_\Lambda$ are independent. $\square$

The multiplicity spaces are where non-Abelian thermodynamics happens: a strictly symmetric cycle cannot see absolute orientation, only the relative structure that $\rho^{\otimes n}$ writes into $M^{(n)}_\Lambda$.

**Theorem 7.4 (states without orientation) [P for $G=SU(2)$ and for tori; for general $G$ under hypothesis (F)].** Let $\rho$ be faithful and $G$-invariant, so that $\rho=\bigoplus_\lambda(I_{V_\lambda}/d_\lambda)\otimes\rho_\lambda$. Let $Q_c$ denote the central charges (generators of the identity component of the center of $G$, acting as scalars $z(\lambda)$ on each $V_\lambda\otimes M_\lambda$), and suppose $H$ is not a function of them. Then $\rho$ is completely passive under strictly symmetric cycles iff
$$\rho=e^{-\beta H-\kappa\cdot Q_c}/Z\qquad\text{for some }\beta\ge0\text{ and }\kappa,$$
that is, a Gibbs state with one chemical potential $\mu_c=-\kappa/\beta$ per central charge. For semisimple $G$ (for example $SU(2)$) these are exactly the Gibbs states $e^{-\beta H}/Z$. *Without an orientation, only central charges carry chemical potentials.*

*Hypothesis (F) (fusion with padding).* Two multisets of irreducibles occurring in $\mathcal H_S$ whose tensor products have the same central character can be padded by a common multiset of irreducibles occurring in $\mathcal H_S$ so that the padded products share an irreducible constituent. (F) holds for tori, where irreducibles are characters and the central character is the charge itself. It holds for $SU(2)$: the total spins of $V_{j_1}\otimes\cdots\otimes V_{j_m}$ are all $J\equiv\sum_ij_i\pmod1$ between $J_{\min}$ and $\sum_ij_i$, and padding with enough copies of any nonzero spin present in $\mathcal H_S$ lowers $J_{\min}$ to $0$ or $\tfrac12$, so the parity of $2J$ is the only obstruction.

*Proof.*
- *Spectrum of the marginals.* By invariance, on each configuration of irreducibles $(\lambda_1,\dots,\lambda_n)$ the block $P_\Lambda\rho^{\otimes n}P_\Lambda$ is $\big(\prod_i d_{\lambda_i}^{-1}\big)I_{V_\Lambda}\otimes I_{N^\Lambda}\otimes\bigotimes_i\rho_{\lambda_i}$, where $N^\Lambda$ is the multiplicity of $V_\Lambda$ in $\bigotimes_iV_{\lambda_i}$. Passivity at $n=1$ forces $[\rho_\lambda,H_\lambda]=0$; diagonalize jointly, with levels $\ell=(\lambda,a)$, energies $E_\ell$, and $f_\ell=-\ln(p_\ell/d_\lambda)$. Then $\sigma_\Lambda$ has eigenvalue $d_\Lambda\prod_i p_{\ell_i}/d_{\lambda_i}$ at energy $\sum_iE_{\ell_i}$, with multiplicity $N^\Lambda$.
- *Lattice form.* By Lemma 7.4a, $\rho^{\otimes n}$ is strictly passive iff no two configurations of $n$ copies whose irreducible multisets share a constituent $\Lambda$ are inverted. As in Lemma 6.2, with $c=\nu-\nu'$ and a common padding $r$: complete passivity holds iff no *admissible* $c$ has $c\cdot E<0<c\cdot f$, where admissible means that $c^++r$ and $c^-+r$ share a constituent for some $r$.
- *Admissibility is conservation of the central character.* Sharing a constituent forces equal central characters, since the center acts on an irreducible by one character. Conversely, (F) gives the padding. Write the character group of the center as $\mathbb Z^m\oplus F$, with $F$ finite. The admissible lattice $L_F=\{c:\sum c=0,\ \sum_\ell c_\ell z(\lambda_\ell)=0\}$ has the same real span as $\{c:\sum c=0,\ \sum_\ell c_\ell z_{\rm free}(\lambda_\ell)=0\}$, because the condition in $F$ has finite index.
- *Conclusion.* The argument of Theorem 6.3, run on $L_F$, gives $f-\beta E\in\operatorname{span}\{\mathbf 1,z_{\rm free}\}$, that is, $p_\ell/d_\lambda\propto e^{-\beta E_\ell-\kappa\cdot z_{\rm free}(\lambda)}$ for each level $\ell=(\lambda,a)$, which is $\rho=e^{-\beta H-\kappa\cdot Q_c}/Z$. Conversely, such a state is $e^{-\tilde H}/Z$ for $\tilde H=\beta H+\kappa\cdot Q_c$ (Gibbs at unit temperature), passive for $\tilde H$ under all unitaries, and strictly symmetric cycles conserve $Q_c$, as in Theorem 7.1. $\square$

Certificate P9 (Part A, blind) compares two independent computations on 16 random invariant instances for $n\le4$. The first builds $\rho^{\otimes n}$, $H_n$ and the collective spin, and restricts to every highest-weight space. The second is the configuration lattice above, with exact fusion. All 64 verdicts agree. Gibbs controls stay passive, and every instance with a "sector chemical potential" (a weight $e^{-\kappa}$ on the spin-$\tfrac12$ sector) is activated, at $n^*$ between 2 and 8.

*Reading.* Theorem 7.2 says that the charges which survive the copy lift are the ones whose values cannot be traded between copies. Theorem 7.4 says the same in the non-Abelian case: copies can always trade non-central charge in the relative degrees of freedom, so only central charges survive. A chemical potential for a non-central charge, such as a magnetization direction, requires an orientation — a state that breaks the symmetry. In infinite systems, chemical potentials appear in the same way, from extending KMS states of the gauge-invariant algebra to the field algebra (Araki–Haag–Kastler–Takesaki 1977).

**Proposition 7.5 (strict symmetry still activates oriented non-thermal states) [P, exact witnesses].** Take $G=SU(2)$.
- **(a) Correlated spin and temperature.** On $V_{1/2}\otimes\mathbb C^2$ (spin-$\tfrac12$ times an energy qubit), let $\rho=\tfrac12|{\uparrow}\rangle\langle{\uparrow}|\otimes\gamma_1+\tfrac12|{\downarrow}\rangle\langle{\downarrow}|\otimes\gamma_2$, with $\gamma_1=(\tfrac{20}{21},\tfrac1{21})$ and $\gamma_2=(\tfrac{11}{20},\tfrac9{20})$. It is not a non-Abelian thermal state, since those are products $r\otimes\gamma_\beta$. It is passive at $n=1$. At $n=4$, in the total-spin-1 sector, two Yamanouchi basis vectors whose energies differ by one quantum carry multiplicity-marginal weights $\tfrac{305761}{131712000}$ (lower energy) and $\tfrac{7070477}{1580544000}$ (higher energy), ratio $1.927$. Swapping them is a strictly symmetric cycle that extracts work.
- **(b) A spin that is not a group element.** For spin 1, $r=\operatorname{diag}(\tfrac12,\tfrac1{10},\tfrac25)$ is not of the form $c\,e^{aS_z}$, because its middle entry is not the geometric mean of the outer ones. Paired with an energy qubit at $e^{-\beta\varepsilon}=\tfrac12$, it has a strict activation witness at $n=5$ (weights $\tfrac{116}{151875}<\tfrac{1681}{1366875}$, ratio $1.61$). Numerically, the spread $\lambda_{\max}/\lambda_{\min}$ of the multiplicity marginals of $r^{\otimes n}$ roughly doubles with each copy ($1,\,1.35,\,2.18,\,4.50,\,9.38$ for $n=2,\dots,6$). That suggests every temperature is eventually beaten [numerics; not proven].
- **(c) Non-Abelian thermal states are flat.** If $r=c\,\pi(g_+)$ for a positive element $g_+$ of the complexified group, then $r^{\otimes n}=c^n\bigoplus_\Lambda\pi_\Lambda(g_+)\otimes I_{M_\Lambda}$, so every multiplicity marginal is proportional to the identity. This is consistent with Theorem 7.1.

*Proof.* (c) is the displayed identity. (a) and (b) follow from the swap argument: for orthonormal vectors $u,w$ at energies $E<E'$ in one multiplicity space, the swap changes the energy by $(E'-E)(\langle u|\sigma|u\rangle-\langle w|\sigma|w\rangle)$. The weights are exact rationals, because squared Clebsch–Gordan coefficients are rational. Certificate P9, Part B, which is not blind because exploratory runs preceded it. Those runs also found activation at $n=4$–$5$ for correlation strengths $p=\tfrac12,0.7,0.9$. $\square$

**Open Problem 7.6 (the strict non-Abelian converse).** Is every faithful state that is completely passive under strictly symmetric cycles a non-Abelian thermal state $e^{-\beta(H-\mu\cdot Q)}/Z$ with $\mu\in\mathfrak g$?

*A reduction [A].* Copies of $\rho$ form a quantum reference frame for $G$, defined up to the stabilizer $K=\{g:U_g\rho U_g^\dagger=\rho\}$ (Bartlett–Rudolph–Spekkens 2007). Relativizing a $K$-symmetric cycle on $k$ copies to a frame of $m$ further copies yields a strictly $G$-symmetric cycle on $m+k$ copies. If its extracted work converges to that of the $K$-symmetric cycle as $m\to\infty$, then $G$-complete passivity implies $K$-complete passivity of the $K$-invariant state $\rho$. Theorem 7.4, applied to $K$, then gives $\rho=e^{-\beta(H-\mu\cdot Q)}/Z$ with $\mu$ central in $\operatorname{Lie}K$: a non-Abelian thermal state. The missing step is that frame lemma with error control, for frames made of the state itself. Both activations in Proposition 7.5 use exactly such relative-orientation information.

### The bridge to thermodynamic resource theories

A *thermal operation* (Janzing et al. 2000; Horodecki–Oppenheim 2013) is $\mathcal E(\rho)=\operatorname{tr}_B[U(\rho\otimes\gamma_B)U^\dagger]$, with $[U,H_S+H_B]=0$ and $\gamma_B$ Gibbs. In port language it is **an interconnection with a completely passive port through a lossless, energy-conserving ledger**.
- Theorem 6.3 explains why the Gibbs state is the unique free state: it is the only completely passive one.
- The family of second laws — monotonicity of all Rényi divergences to $\gamma$ (Brandão et al. 2015) — contains Corollary 6.13 as its unitary, $\alpha=1$ instance.
- With conserved charges, the free states become those of Theorems 7.1–7.2, and the free operations become (non-Abelian) thermal operations.

---

## 8. First join (base × copy lift): noise is set by the dilation defect

**Theorem 8.1 (classical noise defect; Kirchhoff) [P].** Let $S$ be a passive scattering matrix whose hidden ports, in any unitary completion, are thermal at $\theta=k_BT$ (available power per unit bandwidth). If the incident covariance is $\Sigma_a$, the outgoing covariance is
$$\Sigma_b=S\Sigma_aS^\dagger+\theta\,\Delta_{\rm out}(S),\qquad \Delta_{\rm out}(S)=I-SS^\dagger,$$
whichever completion is chosen: *noise is temperature times the defect Gram*. It follows that:
- **(i)** a port at uniform temperature leaves thermal radiation unchanged;
- **(ii)** the emissivity $e_i=(\Delta_{\rm out})_{ii}$ equals the absorptivity $a_i=(\Delta_{\rm in})_{ii}$ whenever $S=S^{\mathsf T}$ (reciprocity);
- **(iii)** for non-reciprocal $S$, the per-port equality can fail while $\sum_ie_i=\sum_ia_i$ still holds.

*Proof.* $b=Sa+Bc$, with hidden inputs $c$ of covariance $\theta I$ and $BB^\dagger=\Delta_{\rm out}(S)$ by Proposition 4.4. Then (i) is $S\theta S^\dagger+\theta(I-SS^\dagger)=\theta I$, (ii) is the equality of row and column norms, and (iii) is $\operatorname{tr}SS^\dagger=\operatorname{tr}S^\dagger S$. Certificates P3.N1 and P4.R10. $\square$

This is Bosma's (1967) and Twiss's (1955) theorem, and Kirchhoff's law (1860) in matrix form. Part (iii) is the observed per-port violation of Kirchhoff's law in magneto-optical emitters (Zhu–Fan 2014; Shayegan et al. 2023), with the second law untouched. The cause is the antisymmetric (Onsager–Casimir, gyrator) part of the response.

**Theorem 8.2 (quantum noise defect: passive and active ports) [P].** Consider a phase-insensitive bosonic channel acting on quadrature variances as $V_{\rm out}=\tau V_{\rm in}+N$.
1. It is completely positive iff $N\ge|1-\tau|/2$ (Holevo–Werner 2001).
2. For $\tau\le1$ it is dilated by a beam splitter, and for $\tau\ge1$ by a two-mode squeezer. With the hidden mode at occupation $n$, both give
$$N=|1-\tau|\big(n+\tfrac12\big),\qquad n+\tfrac12=\tfrac12\coth\frac{\hbar\omega}{2k_BT}.$$
3. At $n=0$ the bound in (1) is saturated. For $\tau>1$ this is Caves's theorem; for $\tau<1$ it is the vacuum noise of loss. The classical limit $N\to|1-\tau|\,k_BT/\hbar\omega$ recovers Theorem 8.1 per mode.

*Proof.* Symbolic (certificate P3.N2). The Heisenberg maps $b=\sqrt\tau a+\sqrt{1-\tau}\,c$ and $b=\sqrt\tau a+\sqrt{\tau-1}\,c^\dagger$ preserve $[b,b^\dagger]=1$ only with the hidden term present. $\square$

**Proposition 8.3 (rotation, boost, and where the gain comes from) [P].** Let $N_a,N_c$ be number operators.
- **(a)** The beam-splitter generator $a^\dagger c+ac^\dagger$ conserves $N_a+N_c$. Its invariant form is $|a|^2+|c|^2$: it is compact ($SU(2)$), a rotation.
- **(b)** The squeezer generator $a^\dagger c^\dagger+ac$ conserves $N_a-N_c$. Its invariant form is $|a|^2-|c|^2$: it is hyperbolic ($SU(1,1)$), a boost. It does **not** conserve the energy $\omega_aN_a+\omega_cN_c$, so it cannot act on its own.
- **(c)** With a pump mode $b$, the term $a^\dagger c^\dagger b+ac\,b^\dagger$ conserves $\omega_aN_a+\omega_cN_c+\omega_pN_b$ iff $\omega_p=\omega_a+\omega_c$.

So the energy for gain is drawn from the pump port, whose reference state — a coherent pump, or an inverted medium at negative temperature — is non-passive. Certificate P4.R7 checks all three parts exactly in truncated Fock space. $\square$

*Reading.* Passive ports dilate by rotations; active ports dilate by boosts fed by a non-passive source (Definition 2.5). In both cases, the added noise is the magnitude of the scalar defect times the occupation $n+\tfrac12$ of the hidden port. The defect is $1-\tau$ for loss, and $\tau-1$ for gain, where the completing squeezer preserves the indefinite form $|a|^2-|c|^2$. The factor $\coth$ is the one that weights the watched variance (Theorem 6.10). Only $\tau=1$ — a lossless, gainless port on the passivity boundary (§5, "Three boundaries") — can be noiseless. Prohibition 4 has two halves: no gain without noise (the defect), and no gain without a source (the pump).

**Theorem 8.4 (noise is local; Levin's direct approach, finite and continuum) [P].** Let $\mathcal D(\omega)=\mathcal K-\omega^2\mathcal M+i\omega\mathcal C$ be a symmetric operator on a Hilbert space — a finite network or a field theory — with $\mathcal M,\mathcal K\succ0$ and $\mathcal C\succeq0$. Let each lossy element carry thermal force noise of one-sided spectral density $4k_BT\mathcal C$. For any readout $y=\langle p,x\rangle$, with $\mathcal G=\mathcal D^{-1}$ and $\chi_{pp}=\langle p,\mathcal Gp\rangle$,
$$S_y(\omega)=4k_BT\langle p,\mathcal G\mathcal C\bar{\mathcal G}p\rangle=\frac{4k_BT}{\omega}\big|\operatorname{Im}\chi_{pp}\big|=\frac{8k_BT\,W_{\rm diss}(\omega)}{\omega^2F_0^2},$$
where $W_{\rm diss}$ is the power dissipated when the system is pushed with force $F_0\cos\omega t$ distributed with the readout's own profile $p$.

*Proof.* $\mathcal G-\bar{\mathcal G}=-2i\omega\,\mathcal G\mathcal C\bar{\mathcal G}$ follows from $\mathcal G^{-1}-\bar{\mathcal G}^{-1}=2i\omega\mathcal C$ and the symmetry of $\mathcal G$. The proof uses only operator algebra, so it holds verbatim in infinite dimensions. Certificate P3.N6 checks the finite case exactly. $\square$

*Reading.* Noise modeling is **local and compositional**. Assign FDT noise to every loss, and the correct noise appears at every port. To predict what a readout will watch, push with the readout's own shape. This is how gravitational-wave mirror thermal noise is computed (Saulson 1990; Levin 1998). In continuum form, with the quantum replacement $k_BT\to\Theta=\frac{\hbar\omega}2\coth\frac{\hbar\omega}{2k_BT}$, the same statement gives [A]:
- Landau–Lifshitz fluctuating hydrodynamics, where stress noise is fixed by viscosity;
- Rytov's fluctuational electrodynamics, where current noise is fixed by $\operatorname{Im}\varepsilon$ — and therefore the Lifshitz theory of Casimir and van der Waals forces, and super-Planckian near-field heat transfer (Polder–van Hove 1971).

**Proposition 8.5 (the price of erasure and the price of communication) [P].** These are two different statements with the same number.
- **(a) Erasure** (Landauer 1961). Resetting one bit of a memory into a thermal bath releases heat $Q\ge k_BT\ln2$. The sharp form is bath passivity, $\beta Q=\Delta S_{\rm sys}+I'(S{:}B)+D(\rho_B'\|\gamma_B)\ge\Delta S_{\rm sys}$ (Esposito–Lindenberg–Van den Broeck 2010; Reeb–Wolf 2014). Writing a record into an already-reset memory can be done reversibly in principle; the unavoidable cost is in the reset (Bennett 1982).
- **(b) Communication** (Shannon–Nyquist). Consider a linear channel whose only noise is thermal, with $N_0=k_BT$ (the Johnson–Nyquist available power per hertz). Shannon's capacity $C(W)=W\log_2(1+\frac P{N_0W})$ gives a signal energy per bit $E_b\ge\lim_{W\to\infty}P/C=k_BT\ln2$ (exact limit: certificate P2.S4). Channels with other noise, and quantum channels with $\hbar\omega\gtrsim k_BT$, obey different limits.

The numbers coincide because in both cases the relevant heat crosses thermal hidden ports. The statements are not the same statement.

---

## 9. Second join (base × symmetry restriction): ports and Noether charges

**Setup.** $[H_S,Q]=0$. The port couples through $H_{\rm int}=\sum_kg_kS_k\otimes B_k$, and the total charge is conserved. The port **supplies** a charge $Q$ if some coupling fails to commute with $Q$. It **reads** $Q$ if a coupling that commutes with $Q$ acts on the $Q$-sectors as a non-constant function $f(Q)$.

**Theorem 9.1 (Abelian selection rule) [P for (a), (c), (d); A for (b)].**
- **(a) No supply, no flip — exactly.** If every coupling commutes with $Q$, then $Q$ is conserved by the full system–environment unitary, to all orders and for all environment states.
- **(b) Supply needs a donor.** To leading order, transitions $q\to q+\Delta Q$ occur at rate $\sum_{k:\,q_k=\Delta Q}|g_k|^2S_{B_k}(\omega)$, where $S_{B_k}$ is the environment's fluctuation spectrum in its $-\Delta Q$ sector. By KMS, $S_B=2\hbar(n+1)\chi_B''$, and detailed balance gives the generalized Gibbs ratio (Theorem 7.2). If the environment's charge carriers are gapped by $\Delta$, flips between degenerate sectors must consume thermally pre-existing carriers, and they are suppressed by $e^{-\beta\Delta}$ (quasiparticle poisoning).
- **(c) Reading dephases in proportion to distinguishability.** A neutral coupling $f(Q)$ destroys the $(q,q')$ coherence at rate $\frac\gamma2|f(q)-f(q')|^2$ and leaves populations unchanged.
- **(d) What the port cannot touch, it cannot corrupt.** Information in the commutant of the port's coupling algebra is invariant (Zanardi–Rasetti 1997; Knill–Laflamme–Viola 2000).

*Proof.* (a) $[Q\otimes I,H_{\rm tot}]=0$. (c) and (d) are Lindblad identities. (b) combines the Davies rates with KMS, and its exact skeleton is certified. Certificate P3.N3, including $\Gamma_2=\Gamma_1/2+\Gamma_\phi$. $\square$

**Theorem 9.2 (the port–charge table, Abelian) [P structure, A examples].**

| | **does not read $Q$** | **reads $Q$** |
|---|---|---|
| **does not supply** | **protected memory**: decoherence-free subspaces, noiseless subsystems, topological qubits | **non-demolition measurement**: $Q$ can be watched forever without change (Braginsky–Vorontsov–Thorne 1980); dephasing is being measured; the pointer basis is what the port reads |
| **supplies** | **control**: a coherent drive changes the charge without learning it | **thermalization**: $T_1$ from supply, $T_\phi$ from reading; relaxation to the GGE |

**Theorem 9.3 (non-Abelian collapse; Schur) [P].** Let the charges generate a compact Lie algebra $\mathfrak g$ acting on $\mathcal H_S=\bigoplus_\lambda V_\lambda\otimes M_\lambda$, with irreducible representations $V_\lambda$ and multiplicity spaces $M_\lambda$.
- **(a)** A coupling that commutes with *every* charge has the form $\bigoplus_\lambda I_{V_\lambda}\otimes X_\lambda$. It supplies nothing, and it reads only the center: the Casimirs, i.e. the label $\lambda$.
- **(b)** A coupling that commutes with one component $Q_a$, but is not of the form $I_{V_\lambda}\otimes X_\lambda$ on some block — for example a non-constant $f(Q_a)$ on an irreducible sector — fails to commute with some $Q_b$. **Reading one non-central component supplies its conjugates.**
- **(c)** A port whose couplings lie in the algebra generated by the charges (collective noise) acts as $\bigoplus_\lambda\pi_\lambda(\cdot)\otimes I_{M_\lambda}$. **The multiplicity spaces are protected memory.**

*Proof.* By Schur's lemma, the commutant of an irreducible $\mathfrak g$-action on $V_\lambda\otimes M_\lambda$ is $I\otimes\operatorname{End}(M_\lambda)$, and inequivalent blocks cannot mix. That gives (a), and (b) is its contrapositive. For (c), the collective generators act trivially on each $M_\lambda$.

Certificate P4.R6 checks the following exactly:
- **(i)** Spin-½ with a jump $S_z$: $\mathcal L^*(S_z)=0$ but $\mathcal L^*(S_x)=-\frac\gamma2S_x$.
- **(ii)** Spin-1: $[f(S_z),S_x]=0$ iff $f$ is constant.
- **(iii)** Two spins with a Casimir jump $J^2$: no component is changed, and the singlet–triplet coherence decays at $2\gamma$.
- **(iv)** Three spins under collective $S_z,S_\pm$ noise: $\mathcal L^*(P_\sigma)=0$ for all six permutations, so the multiplicity-space qubit is protected.

$\square$

*Reading.* For an Abelian charge the four cells of the table are independent. For a non-Abelian algebra, the cell "reads without supplying" shrinks to the **center**: only the Casimirs (for spin, the total $J^2$) can be watched without disturbing any component. Reading $S_z$ is non-demolition *for $S_z$*, but it supplies $S_x$ and $S_y$. The protected cell becomes the **multiplicity spaces**, which is the logic behind collective-noise decoherence-free subsystems.

A popular statement holds that symmetry-protected sectors cannot flip unless the environment can supply the Noether charge. That statement is the Abelian top row, read left to right. Its completion is that **symmetry protects the bit, not the phase**, and that, for non-Abelian charges, **it protects only what lives in multiplicity**.

*Engineering design rule [A].*
- $T_1$ is set by the charged sector of the environment's dissipation spectrum at the qubit frequency.
- $T_\phi$ is set by the neutral sector's low-frequency spectrum times $|f(q)-f(q')|^2$.
- Protection is bought by gapping the first and blinding the second. For non-Abelian encodings, store in multiplicity and read only Casimirs.

---

## 10. Away from equilibrium: the arrow is the gap between watching and pushing

**Theorem 10.1 (Harada–Sasa 2005) [P, cited; certified instance].** For Langevin dynamics, the heat dissipation rate equals $\gamma\{\langle v\rangle^2+\int\frac{d\omega}{2\pi}[\tilde C_v-2T\tilde R'_v]\}$: the frequency-resolved violation of the FDT.

*Certified instance (P1.C3).* An overdamped particle with a circulating force $kJx$ has an **exactly Gibbs** stationary density $\Sigma=(T/k)I$, so every snapshot reports equilibrium. Yet the FDT-violation integral equals the hidden heat $2kT\omega^2$ exactly, and it vanishes pointwise when $\omega=0$.

**Proposition 10.2 (what a snapshot cannot see) [P].** Let $T$ be a finite, irreducible Markov transition matrix with stationary distribution $\pi$, and let $\tilde T=D_\pi^{-1}T^{\mathsf T}D_\pi$ be its time reverse.
- $T$ and $\tilde T$ have the same stationary distribution, so no function of a single stationary snapshot distinguishes them.
- The pair statistics $\pi_iT_{ij}$ distinguish them iff detailed balance fails.
- The entropy production rate equals the Kullback–Leibler divergence between the forward and reversed pair statistics (Schnakenberg 1976).

In this setting, a one-time stationary marginal cannot reveal the antisymmetric probability current, and detailed balance is exactly the condition that removes it. For representation learning, the same blindness of snapshot-based objectives to the antisymmetric part is proven in *Curvature and Current* (Murillo 2026).

**Proposition 10.3 (watching bounds pushing, away from equilibrium) [P, cited].** Around an arbitrary nonequilibrium steady state, the response of any observable to a perturbation satisfies $|\delta\langle A\rangle|^2\le2\operatorname{Var}(A)\,D_{KL}(P_\varepsilon\|P_0)$ (Dechant–Sasa 2020). At equilibrium the FDT fixes the response exactly in terms of fluctuations. Around any steady state, the fluctuation–response inequality bounds it, and the TUR follows from it for a "virtual" perturbation along the mean velocity.

**Generalizations [P, cited].**
- Dissipation equals $k_BT$ times the relative entropy between the forward and time-reversed path ensembles (Kawai–Parrondo–Van den Broeck 2007).
- The Jarzynski and Crooks fluctuation theorems are the nonlinear completion.
- Harada–Sasa has been used to measure the near-perfect efficiency of F$_1$-ATPase (Toyabe et al. 2010).

*Reading.* The arrow of time is measurable as the gap between watching and pushing (Theorem 10.1). This is a statement about linear response and Markov dynamics; it is not a general criterion for causal identification. Observational data can identify interventional quantities away from equilibrium under additional causal assumptions. Equilibrium linear response — the FDT — is one sufficient condition, not a necessary one (cf. Baldovin–Cecconi–Vulpiani 2020 on causation and response).

---

## 11. The modeling calculus

**Proposition 11.1 (closure) [P].**
1. *Interconnection.* A power-conserving interconnection of passive ports is passive. For port-Hamiltonian systems $\dot x=(J-R)Qx+Bu$, $y=B^{\mathsf T}Qx$, with $\dot H=-x^{\mathsf T}QRQx+y^{\mathsf T}u$, the feedback $u_1=-y_2$, $u_2=y_1$ yields $J_c$ skew and $R_c\succeq0$.
2. *Reduction.* A compression of a contraction is a contraction. Effort-constraint projection with $W=QV(V^{\mathsf T}QV)^{-1}$ preserves $J_r$ skew, $R_r\succeq0$, and $Q_r\succ0$, so the reduced model is positive-real (Polyuga–van der Schaft 2012; cf. PRIMA, Odabasioglu–Celik–Pileggi 1998).
3. *Dilation.* Every passive model can be simulated as a reversible system coupled to a bath (§4), and the noise it predicts does not depend on the ledger chosen (Proposition 4.4).
4. *Noise assignment.* Local FDT at each loss implies the FDT at every port, in finite networks and in continuous fields (Theorem 8.4).
5. *Stability.* The stored energy is a Lyapunov function, and a feedback loop of passive systems is stable (Zames 1966).

Certificates: P3.N5 (items 1–2, including $\operatorname{Re}G(i\omega)\ge0$ for the full and reduced models) and P3.N6 (item 4).

**Proposition 11.2 (beyond linear ports) [P; classical, credited].** Let $x\in\mathbb R^m$ carry a storage function $H(x)$, an interconnection $J(x)=-J(x)^{\mathsf T}$ and a dissipation $R(x)=R(x)^{\mathsf T}\succeq0$, all smooth, with $e^{-H/\theta}$ integrable and $\theta=k_BT$. Put $M=R-J$ and $(\nabla\!\cdot\!M^{\mathsf T})_i=\sum_j\partial_jM_{ij}$.
- **(a) Nonlinear noise assignment.** The Itô equation
$$dx=\big[-M(x)\nabla H+\theta\,\nabla\!\cdot\!M^{\mathsf T}\big]dt+\sqrt{2\theta}\,\sigma(x)\,dW,\qquad\sigma\sigma^{\mathsf T}=R,$$
has the Gibbs density $e^{-H/\theta}$ as a stationary solution for every $H$, $J(x)$ and $R(x)$. Its stationary current is $(J\nabla H-\theta\nabla\!\cdot\!J^{\mathsf T})e^{-H/\theta}$, which is divergence-free: the reversible circulation.
- **(b) The divergence term is not optional.** Without $\theta\nabla\!\cdot\!M^{\mathsf T}$ (the "spurious drift"), Gibbs stationarity fails in general as soon as $R$ or $J$ depends on $x$. It holds when both are constant, which is the linear calculus of Proposition 11.1.
- **(c) Several temperatures.** If the losses sit at different temperatures, no Gibbs density is stationary for any $\theta$. The steady state carries a current, which is the arrow of §10.
- **(d) Memory.** A bath with memory is a passive port with impedance $\hat\gamma(s)$. Realizing it by Foster's theorem as oscillators $(\omega_k,c_k)$ and eliminating them gives the generalized Langevin equation, with kernel $\gamma(t)=\sum_kc_k^2\omega_k^{-2}\cos\omega_kt$ (a Foster reactance in the Laplace variable) and thermal noise obeying $\langle\xi(t)\xi(s)\rangle=\theta\,\gamma(t-s)$ (Kubo's second FDT). This is the base lift (a lossless realization of the bath port) together with the copy lift (thermal hidden ports): the Ford–Kac–Mazur/Caldeira–Leggett model is the Foster synthesis of the bath.
- **(e) Quantum.** For Lindblad dynamics, the counterpart of (a) is quantum detailed balance in a chosen monotone metric. The Gibbs state is stationary for Davies generators, and which metric's FDT holds depends on how the system is pushed (Paper 54, §4.1).

*Proof.* (a) The Fokker–Planck current of $p=e^{-H/\theta}$ is $j=bp-\theta\nabla\!\cdot(Rp)$. The $R$-terms cancel against $-R\nabla H\,p$, leaving $j=(J\nabla H-\theta\nabla\!\cdot\!J^{\mathsf T})p$. Its divergence vanishes by antisymmetry of $J$. (b), (c) Explicit polynomial instances. (d) Integrate the oscillator equations and integrate the memory term by parts. Then average over the bath's conditional Gibbs state, with $\langle\Delta q_k^2\rangle=\theta/\omega_k^2$ and $\langle p_k^2\rangle=\theta$. Certificate P10 checks (a)–(c) on symbolic 2D and 3D instances and (d) on two-oscillator baths. Its first two runs failed on checker artifacts (a symbolic integrator out of memory; integer division producing floats), and both failures are retained. Credits: thermodynamically consistent multiplicative noise (Gardiner; Lau–Lubensky 2007; the GENERIC framework, Öttinger 2005), oscillator baths (Ford–Kac–Mazur 1965; Zwanzig 1973; Caldeira–Leggett 1983). $\square$

So the calculus is not confined to linear systems. Nonlinear storage, state-dependent friction, several baths, and baths with memory are covered, provided that each loss carries its fluctuation and every state-dependent loss carries its drift correction.

**The workflow this licenses.** Specify two things: the reversible skeleton ($J$ and the storage $Q$), and the losses ($R$, with their temperatures). Then:
- noise, stationary states, and dispersion are *determined*;
- physical admissibility of fits (positive-realness, parity defect), validity of reduced models, and stability of assemblies are *checkable* by one inequality.

Dynamics, noise, stability, and thermodynamic consistency — four modeling tasks — become one. Circuit simulators (resistor noise $4k_BTR$), signal-integrity tools (passivity enforcement of fitted macromodels), and gravitational-wave detectors (thermal noise from loss angles) each practice a fragment of this. The fragments are one method, valid in every exact-realization row of the effort–flow table (§2.1). That includes continuous fields (Theorem 8.4), nonlinear and multi-bath systems and baths with memory (Proposition 11.2), and chemical reaction networks (the chemical Langevin equation). In the structural-translation rows, only the architecture carries over, not the energetics. Stochastic gradient descent, which obeys an analogous set of fluctuation–dissipation relations (Yaida 2019), is an example of such a translation.

---

## 12. Measurement through a port

**What the principle resolves [P/A].**
- *The cut.* Von Neumann's movable cut is the statement that partial traces compose.
- *Generalized measurements.* Every POVM is a projective measurement on the ledger (Naimark).
- *The pointer basis.* It is the eigenbasis of what the port *reads*. For non-Abelian charges, only the Casimirs can be read without disturbing any component. A single component can be read non-demolitionally for itself, but doing so supplies its conjugates (Theorem 9.3).
- *Durability.* A record lasts as long as the recurrence time of the channel that received it, and forever only in the continuous-spectrum limit (Theorem 4.5, Corollary 4.6).
- *Cost.* Resetting the recording memory releases at least $k_BT\ln2$ per bit into the bath (Proposition 8.5(a)). Recording itself can be reversible in principle.
- *Timestamps.* A position reading is a joint event of pointer and clock, and time can be defined as correlation with a clock subsystem (Page–Wootters 1983).

**What it does not resolve [C, fenced].** Why *this* outcome occurs. The principle localizes the residue to one indexical question — *which branch of the ledger is this port on?* — and supplies the measure (Born; Gleason 1957) but not the pointer.

---

## 13. What the principle answers in one line

1. *Why does every absorbing material disperse light?* Stable causality gives resistance and reactance equal energy (§5).
2. *How much does a resistor hiss?* $4k_BTR$ per hertz: temperature times the defect Gram (§8).
3. *Why must every amplifier add noise, and where does its energy come from?* Gain is a boost dilation, with added noise $(G-1)(n+\tfrac12)$; the energy comes from a pump with $\omega_p=\omega_s+\omega_i$ (§8).
4. *What is the minimum heat for erasing one bit into a thermal bath?* $k_BT\ln2$ (Landauer). The minimum signal energy per bit through a channel whose only noise is thermal is also $k_BT\ln2$ (Shannon–Nyquist) — a different statement with the same number (§8).
5. *What is a sensor's thermal noise floor?* Push with the readout's own profile and compute the loss (§8).
6. *Why do neutral bodies attract (Casimir / van der Waals)?* Each body's field fluctuations are fixed by its absorption, via the FDT on the field port (§8).
7. *How can shot noise measure temperature without calibration?* $S/2eI=\coth(eV/2k_BT)$ — the coth law (§6).
8. *What does precision cost?* For steady currents of Markov processes, $\sigma\operatorname{Var}(J)/J^2\ge2k_B$. In unicyclic processes this is $u\coth u\ge1$, the same kernel as the quantum FDT inequality (§6).
9. *Why does temperature exist, and why is it shared?* The full copy lift forces the Gibbs state at one $\beta$ (§6).
10. *How many copies of a passive, non-thermal state are needed before work can be extracted?* For three levels, the least denominator of a fraction between its energy ratio and its entropy ratio (§6).
11. *How small can a two-temperature engine be?* The height of the simplest gear ratio in the Carnot window. Near equilibrium this is of order $T/\Delta T$ for commensurate level spacings, and of order $(T/\Delta T)^{1/2}$ — a Fibonacci number — for golden-ratio spacings. With $k$ reservoirs whose gaps span a degree-$k$ number field, it is of order $(T/\Delta T)^{1/k}$. For two harmonic modes, one copy suffices, and the same numbers count the order of the nonlinear process (§6).
12. *Why do chemical potentials exist?* Each conserved charge that admissible cycles must respect adds one multiplier; restricting the processes enlarges the free family (§7).
13. *When does a symmetry protect a qubit, and against what?* Against flips if the environment cannot supply the charge; against dephasing only if no port can read it; and, for non-Abelian charges, only for information stored in multiplicity (§9).
14. *Can I read $S_z$ without disturbing $S_x$?* Not on an irreducible sector. Only the total spin can be read without back-action on any component (§9).
15. *What can be monitored forever without disturbance?* Conserved charges — and, for the whole of a non-Abelian algebra, only its Casimirs (§9).
16. *Why is loss irreversible if physics is reversible?* The receiving ledger has an effectively continuous spectrum; finite or confined ledgers recur (§4).
17. *How long does a record last?* About $2\pi N/W$ for the receiving channel, with an average echo of about $\delta/\pi\Gamma$ (§4).
18. *What can a stationary snapshot not see?* In a Markov chain, the antisymmetric probability current. Pair statistics see it iff detailed balance fails (§10).
19. *When does watching determine pushing?* In equilibrium linear response (the FDT). Away from equilibrium, watching bounds pushing, with a relative-entropy price (§10).
20. *Is my fitted model physical?* Check passivity and the parity defect (§§5, 11).
21. *Does a Kramers–Kronig-type test fail for a gain medium?* Only if the medium is unstable, not merely because it amplifies (§5).
22. *Can I simplify my model without breaking its physics?* Yes, by compression (§11).
23. *Can I measure entanglement by pushing?* Yes: every quantum Fisher metric is a filter on the measured dissipation (§6).
24. *Which quantum Fisher metrics respect data processing?* Exactly those whose filter is realized by a self-dual resistor–inductor network (§6).
25. *What does the choice of quantum Fisher metric mean?* A choice of frequency filter — equivalently, of network — on one dissipation spectrum (§6).
26. *Can emissivity differ from absorptivity?* Per port, if the emitter is non-reciprocal; never in total (§8).
27. *How efficient is a molecular motor?* Measure its FDT violation (§10).
28. *My model is nonlinear, with friction that depends on the state. Does "put $k_BT$ on every loss" survive?* Yes, with one correction: add the drift $\theta\nabla\!\cdot\!M^{\mathsf T}$, and the Gibbs state is stationary for every storage function (§11).
29. *Can a state with no preferred direction carry a chemical potential for angular momentum?* Not under strictly rotation-symmetric operations. Without an orientation, only central charges carry chemical potentials (§7).

---

## 14. Where the principle strains

**Gravity [P for the obstruction, A for the local statement].** Self-gravitating systems have negative heat capacity, and the Newtonian Hamiltonian is unbounded below. So no global passive state exists, and the copy lift fails globally; its additivity hypothesis also fails for long-range interactions. Locally, the principle survives. The vacuum on a Rindler wedge is KMS for boosts (Bisognano–Wichmann 1975), and Jacobson (1995) derives Einstein's equations from $\delta Q=T\,dS$ on every local horizon. Gravity is where local passive ports fail to glue into a global passive state.

Whether gravity's port is reactive (able to entangle; Bose et al. 2017; Marletto–Vedral 2017) or purely resistive (decohering; Oppenheim 2023) is open. Oppenheim's decoherence–diffusion trade-off is itself an FDT-type lock. We note, without leaning on it, the stochastic-spacetime proposal for galactic dynamics (Oppenheim–Russo 2024) and its critique (Hertzberg–Loeb 2024).

**Structural rows.** In the structural-translation rows of §2.1, "power" has no energetic meaning, and only the architecture — watch and push, constraint, lifts — carries over. Where a translation is exact mathematics, as for the data-processing monotonicity of quantum Fisher metrics (Theorem 6.11), it is stated as such; elsewhere it is analogy.

**Non-Abelian converse.** Theorem 7.1 is exact, and so is the converse for states without orientation (Theorem 7.4, for $SU(2)$, for tori, and for any $G$ satisfying the fusion hypothesis (F)). For oriented states the strict converse is open (Open Problem 7.6). Proposition 7.5 shows by exact witnesses that the natural candidate counterexamples are activated. The literature's uniqueness theorem uses reference frames and charge batteries and is a different statement (Remark 7.3).

**Copy thresholds beyond three levels.** Theorems 6.9 and 6.9′ settle their scaling for badly approximable and for almost every spectrum, but not their exact values. No Stern–Brocot analogue is known for $d\ge4$, and the fluctuations of $n^*\delta^{1/r}$ and the amount of work at threshold are open (Remark 6.9f). The thresholds of §6 also presuppose energy additivity and global unitaries on the copies.

**Singular continuous spectra.** Theorem 4.5 guarantees forgetting on average, not pointwise; sparse recurrences are possible.

**The origin of the arrow [fenced].** The time lift *selects* a direction of time. It does not explain why reference states are passive, that is, why the past had low entropy. Misra–Prigogine–Courbage (1979) give the converse of dilation, and we take no side.

**The ledger's ontology [fenced].** Dilation theorems assert that a lossless completion *exists*, not that it is physically real. Proposition 4.4 makes every prediction independent of which completion is imagined.

**Active matter [A].** Apparent activity is passivity with a non-passive sub-port inside the boundary (Definition 2.5). Lasers, motors, and cells are priced by the active branch of Theorem 8.2 and by the pump rule of Proposition 8.3.

**Beyond linear response.** The spectral calculus of §§5–8 is linear. The fluctuation theorems and the fluctuation–response inequality (§10) extend the principle, but not the filter tables.

---

## 15. Objections and replies

- *"Is the Port Principle one principle, or a common metaphor for several?"* It is one constraint with several explicit operations. What is forced is always "the constraint together with a named lift or restriction" (Table 3.1), and the lifts are not free:
  - the time lift is a genuine strengthening (Proposition 3.3(a));
  - the full copy lift is the content of Pusz–Woronowicz and Lenard;
  - the symmetry restriction changes the free family.

  The contribution is the lift calculus and what it exposes. It is not a claim that passivity alone yields the laws.
- *"Textbook linear response."* The ingredients are textbook, and they are credited (§1.2). The claim is the organization, which Kitcher's (1981) criterion lets us measure by counting argument patterns. The single pattern *(constraint) × (lift or restriction) → (filter on the port's spectral measure)* derives about twenty results:
  - Kramers–Kronig; causal parity and the parity defect;
  - Halmos/Egerváry/Stinespring/Naimark; Wiener's echo-or-forget law;
  - Pusz–Woronowicz/Lenard; the zeroth law; copy thresholds; the GGE and the non-Abelian thermal state;
  - the classical and quantum FDT; the Petz and WYD filters and their circuit reading; $D=\beta W$; the coth law;
  - Kirchhoff/Bosma; Caves and the pump rule; Levin/Rytov/Lifshitz; Landauer and Shannon–Nyquist;
  - the Abelian and non-Abelian port–charge tables; Harada–Sasa; the snapshot statement.
- *"Dissipativity theory already did this"* (Willems, Haddad, van der Schaft). That work is classical and deterministic. The copy lift and its arithmetic, the quantum dilations, the filter tables and their circuit reading, the symmetry restriction, and the charge tables are what the port view adds.
- *"Causality plus purification already reconstructs quantum theory"* (Chiribella et al.). The base and the time lift are among their axioms, which we read as corroboration. We add temperature, symmetry, and the spectral calculus.
- *"Does 'power' mean the same thing in every row of the effort–flow table?"* No. §2.1 separates exact realizations from structural translations, and the results of this paper apply to the former.
- *"There are other ways to learn than watching and pushing."* Yes: deduction, simulation, priors. Watching and pushing are the two fundamental *experimental* modes, and that is the only use the paper makes of them.
- *"Causal parity fails for gain media."* It fails for *unstable* media. Gain is allowed (Corollary 5.5), and the exact defect of any kernel is its time-reflection overlap (Theorem 5.4).
- *"Active ports equivocate on the boundary."* The boundary rule (Definition 2.5) and the pump theorem (Proposition 8.3) make the source explicit. The principle never claims an active port is passive.
- *"'Port' is anthropocentric"* (Bell). A port is a subsystem plus its couplings; no observer is involved. "For all practical purposes" is made quantitative in Corollary 4.6, and exact in the continuum by Theorem 4.5.
- *"A principle that explains everything forbids nothing"* (Popper). It forbids six things (§3), and §16 lists refuting observations.

---

## 16. Falsifiers

Each entry pairs an outcome that corroborates (K) with one that refutes (L).

1. **The root.** L: cyclic work extracted from a completely passive reference state. K: no such device exists.
2. **Collapse models.** A fundamental, non-dilatable loss must carry matched dissipation at finite temperature (dissipative CSL; Smirne–Bassi 2015). L: collapse heating that never saturates. K: collapse noise that thermalizes.
3. **Amplifiers.** L: a phase-insensitive amplifier beating $N=(G-1)/2$, or gain without an identifiable non-passive source. K: none has been built.
4. **Abelian protection.** L: flips between charge sectors in an environment that provably cannot supply the charge (Theorem 9.1(a) is exact). K: protected-qubit lifetimes scaling as $e^{\beta\Delta}$ with the carrier gap.
5. **Non-Abelian back-action.** L: reading a non-central charge component on an irreducible sector with no back-action on its conjugates (Theorem 9.3(b) is exact). K: none observed.
6. **Gravity.** L: gravitational decoherence without the diffusion that the trade-off requires. K: observed gravitational entanglement, or a stochastic signature that respects the trade-off.
7. **Parity.** L: a *stable*, stationary, causal response, measured over adequate bandwidth, with a nonzero defect. K: stable amplifiers with zero defect, and unstable systems with the predicted cross-overlap defect.
8. **The coth law.** L: a tunnel junction in the pure-tunneling regime whose $S/2eI$ deviates from $\coth(eV/2k_BT)$ beyond instrumental error. K: the primary thermometry of Spietz et al. (2003).
9. **Copy thresholds (a test of the lift's hypotheses).** Use a platform with additive, well-controlled energies, such as trapped ions or superconducting qubits. A work-extraction protocol restricted to $n$ copies of a prepared passive non-Gibbs state — or of two Gibbs ports at unequal temperatures — should extract nothing for $n<n^*$ and something for $n\ge n^*$. The threshold is a theorem, so L — extraction below $n^*$ — would indicate non-additive energies or imperfect preparation, i.e. a failure of the hypotheses. K: agreement.

The principle's empirical strength is inherited from the second law, unitarity, and KMS. Its own new risky content is modest, and we say so.

---

## 17. Conclusion

We have organized a family of laws around one constraint and a few operations on it. The claim is not that passivity alone yields the laws of impedance, fluctuation, measurement, and information. It is that each of these laws is exposed by the constraint under a named lift or restriction. The lift calculus is itself a useful object:
- it produces exact finite proofs;
- it tells a reader which assumption carries which conclusion;
- it has consequences of its own, among them the arithmetic of the copy lift and the circuit reading of the Petz classification.

The same pairs recur throughout: watching and pushing; sum and difference of opposite rates; rotation and boost; supplying and reading; center and multiplicity; echo and forgetting. The last pair turned out to have a partner in the copy lift. The module of level spacings and its dual torus carry both questions: the ledger, watched in time, asks when all phases return; the copy lift asks which integer exchange nearly conserves energy; and transference ties the answers by $y(e+1)=1$ (Proposition 6.9e). What echoes, hoards; what forgets, yields. The principle also marks where it strains: global gravity, the strict non-Abelian converse for oriented states, exact thresholds beyond three levels, the past hypothesis, and single outcomes.

---

## Appendix A. Certificate suite

All certificates are in `empirical/port_principle/`. Every vanishing or membership decision uses exact rational or symbolic arithmetic. Floating point appears only in labelled numerical witnesses, with stated tolerances. Falsifiers were written into each file before its first run, and failures are retained.

| File | Content | Result |
|---|---|---|
| `p1_four_locks.py` | C1 causal parity; C2 four weights and $D=\beta W$; C3 Gibbs density with hidden current (Harada–Sasa); C4 decay from rotations, Lamb shift, $Z$-renormalization, echo | 21/22. C4.a failed (4.3%) because the reactance's derivative renormalizes the decay; it is superseded by C4.a′ (0.28%) and retained. |
| `p2_three_quantifiers.py` | S1 every-instant passivity ⟹ causality, and precognition; S2 exact Egerváry ledger with sharp horizon; S3 $n^*=3$ thresholds and the zeroth law; S4 $E_b/N_0\to\ln2$ | 10/10. An independent inversion search agrees. |
| `p3_protection_noise_modeling.py` | N1 noise defect and Kirchhoff; N2 unified $|1-\tau|(n+\tfrac12)$; N3 Abelian port–charge table; N5 port-Hamiltonian closure; N6 Levin locality | 17/17. N2.K2c first failed on a symbolic-simplifier artifact ($\coth$); fixed and logged. |
| `p4_review_v2.py` | R1 wave form and Cayley; R2 parity defect (gain allowed, instability detected); R3 Wiener; R4 $H\propto I$ edge case, degenerate $n^*=3$, GGE enlargement, non-GGE $n^*=5$, trivial case; R5 Petz/WYD filters and ordering; R6 non-Abelian (Schur, Casimir, multiplicity); R7 pump rule; R8 coth law; R10 dilation independence | 20/20. R10 first failed on a checker bug (`nsimplify` corrupting exact rationals); fixed and logged. |
| `p5_copy_threshold_and_circuits.py` | H2.K2a–c copy thresholds (brute force), smallest engine, resonance vs golden scaling; K2d simplest fraction minimizes numerator and denominator; K2e Carnot window; K2f Fibonacci formula and resonant/badly approximable bounds; H3.K3a–b and K3d circuit reading; K3c/K3c′/K3e quadratic-mean counterexample | 11/12. K3c (pre-registered random-channel search) found no violation and is retained; K3c′ (post-diagnosis: pinching and partial trace) finds it. K3c's operator-monotonicity witness carried a regularization that made $B-A$ marginally non-PSD; K3e replaces it with an exact witness. K3b first failed on a symbolic `Piecewise` artifact; fixed and logged. |
| `p6_copy_threshold_d4.py` | H6.K6a lattice minimum vs brute-force ergotropy for $d=4$; K6a′ exact integer scan vs enumeration; K6b triple reduction fails (Corollary 6.9b); K6c resonance-rank exponents with surrogate stability and 50-digit witnesses; K6d norm-form bounds and Theorem 6.9(a); K6e the $k$-reservoir formula and its exponents (Corollary 6.9a) | 6/6. All falsifiers were pre-registered before the first run. |
| `p7_rank_law_metric_physics.py` | H7a intermediate ranks (K-visible and K-blind, $d=4,5$, $r=2,3,4$) and the very-well-approximable control; H7b almost every gap ratio, golden control, oscillation; H7c near resonance (Proposition 6.8a); H7d harmonic modes (Corollary 6.9c); H7e platform table; H7f echo–yield exponents (Proposition 6.9e) | 4/6. H7a and H7b failed narrowly and are retained: the pre-registered ceilings were on local exponents at finite $\delta$ (0.604 > 0.60; golden 0.5801 > 0.58), which cannot absorb the theorems' constants. A transcription bug in this file's copy of the Stern–Brocot routine hung the first runs; fixed and logged. |
| `p7b_post_diagnosis_A6.py` | post-diagnosis (not blind): the constructive exchange of Theorem 6.9(b) violates at every $\delta$ to $10^{-30}$ with cost$\cdot\delta^{1/2}\le14.3$ (proof constant 47); scan never beats it | 3/3 |
| `p7c_post_diagnosis_golden.py` | post-diagnosis (not blind): golden $n^*\delta^{1/2}\in[0.86,2.22]$ for $\delta$ to $10^{-70}$; local exponent within 0.0083 of $\tfrac12$ below $10^{-40}$ | 2/2 |
| `p8_charge_raises_exponent.py` | a conserved charge raises the exponent from $\approx\tfrac13$ to $\approx\tfrac12$ (Corollary 6.9d); restriction only raises thresholds | 3/3 |
| `p9_nonabelian_strict.py` | Part A (blind): brute-force strict passivity (highest-weight restriction) against the configuration lattice with exact fusion, on 16 invariant instances for $n\le4$; Gibbs controls; sector chemical potentials activated (Theorem 7.4). Part B (not blind): exact rational activation witnesses for the correlated spin–temperature state ($n=4$) and the non-group spin-1 state ($n=5$); exact flatness of the multiplicity marginals of non-Abelian thermal states (Proposition 7.5) | 7/7. Exploratory runs (scratchpad) preceded Part B and are disclosed. |
| `p10_nonlinear_modeling.py` | N1 Gibbs stationarity with the divergence drift (symbolic 2D, 3D); N2 failure without it; N3 the stationary current; N4 no Gibbs state at two temperatures; N5 Foster bath: kernel, second FDT, positive-real transform (Proposition 11.2) | 5/5 on run 3. Run 1: N5 no verdict (symbolic integrator out of memory); run 2: N5(a) failed on a checker bug (integer division produced floats). Both retained; run 3 is not blind for N5. |

## Appendix B. Glossary across disciplines

The last two columns are structural translations (§2.1), not exact realizations.

| Here | Physics | Engineering | Information / data | Statistics / causality |
|---|---|---|---|---|
| port | open-system boundary, coupling | terminal pair, bond | interface, endpoint | unit exposed to intervention |
| watch | correlation, fluctuation spectrum | noise measurement | logs, traces | observational data |
| push | response function, susceptibility | transfer function, impedance | probe, query | intervention, do-operator |
| constraint | second law (Kelvin), complete passivity | positive-real, dissipativity | data-processing inequality | — |
| ledger (dilation) | purification, environment | lossless embedding + loads | event log (event sourcing) | full generative process |
| defect | loss channel | noise-wave source | lossy compression | unmeasured confounding |
| echo horizon | Poincaré recurrence; point spectrum | reverberation time | log retention window | — |
| charge | Noether charge | conserved quantity | invariant, checksum | — |
| active port | non-passive reference (pump, inversion) | powered amplifier | — | — |

## References (content-level; to be formatted)

Alicki & Fannes 2013 (PRE 87, 042123); Anderson & Duffin 1969 (J. Math. Anal. Appl. 26, 576); Araki, Haag, Kastler & Takesaki 1977 (CMP 53, 97: extension of KMS states and chemical potential); Bartlett, Rudolph & Spekkens 2007 (RMP 79, 555: reference frames, superselection rules, and quantum information); Caldeira & Leggett 1983 (Ann. Phys. 149, 374); Ford, Kac & Mazur 1965 (J. Math. Phys. 6, 504); Gardiner (Handbook of Stochastic Methods, Springer); Lau & Lubensky 2007 (PRE 76, 011123: state-dependent diffusion and thermodynamic consistency); Öttinger 2005 (Beyond Equilibrium Thermodynamics, Wiley); Zwanzig 1973 (J. Stat. Phys. 9, 215); Baez & Fong 2018 (TAC 33, 1158); Baldovin, Cecconi & Vulpiani 2020 (PRR 2, 043436); Barato & Seifert 2015 (PRL 114, 158101); Bennett 1982 (Int. J. Theor. Phys. 21, 905); Bisognano & Wichmann 1975; Bose et al. 2017 (PRL 119, 240401); Bosma 1967; Braginsky, Vorontsov & Thorne 1980 (Science 209, 547); Brandão, Horodecki, Ng, Oppenheim & Wehner 2015 (PNAS 112, 3275); Brocot 1861; Callen & Welton 1951; Cassels 1957 (An Introduction to Diophantine Approximation, Cambridge); Cauer 1926; Caves 1982 (PRD 26, 1817); Chiribella, D'Ariano & Perinotti 2010 (PRA 81, 062348); Chong, Ge, Cao & Stone 2010 (PRL 105, 053901); Crooks 1999; Dechant & Sasa 2020 (PNAS 117, 6430); Egerváry 1954; Einstein 1905; Esposito, Lindenberg & Van den Broeck 2010 (NJP 12, 013013); Foster 1924 (Bell Syst. Tech. J. 3, 259); Frérot & Roscilde 2016 (PRB 94, 075121); Gingrich, Horowitz, Perunov & England 2016 (PRL 116, 120601); Gleason 1957; Gruber & Lekkerkerker 1987 (Geometry of Numbers, North-Holland); Guryanova, Popescu, Short, Silva & Skrzypczyk 2016 (Nat. Commun. 7, 12049); Haddad 2019 (Princeton); Halmos 1950; Harada & Sasa 2005 (PRL 95, 130602); Hardy & Wright (An Introduction to the Theory of Numbers); Hauke, Heyl, Tagliacozzo & Zoller 2016 (Nat. Phys. 12, 778); Haus & Mullen 1962; Hertzberg & Loeb 2024 (arXiv:2404.13037); Holevo & Werner 2001 (PRA 63, 032312); Horodecki & Oppenheim 2013 (Nat. Commun. 4, 2059); Jacobson 1995 (PRL 75, 1260); Janzing, Wocjan, Zeier, Geiss & Beth 2000; James 1998 (Appl. Phys. B 66, 181); Jarník 1941 (Věstník Král. České Spol. Nauk; covering radius ≤ ½Σλᵢ); Jarzynski 1997; Kawai, Parrondo & Van den Broeck 2007 (PRL 98, 080602); Kitcher 1981; Knill, Laflamme & Viola 2000 (PRL 84, 2525); Kubo 1957; Kubo & Ando 1980 (Math. Ann. 246, 205); Landau & Lifshitz 1957 (fluctuating hydrodynamics); Landauer 1961; Lenard 1978; Levin 1998 (PRD 57, 659); Lifshitz 1956; Linden, Popescu & Skrzypczyk 2010 (PRL 105, 130401: smallest refrigerators; and arXiv:1010.6029: smallest heat engines); Liu 2026 (arXiv:2605.00117); Lostaglio, Jennings & Rudolph 2017 (NJP 19, 043008); Löwner 1934 (Math. Z. 38, 177); Luo 2004 (Proc. AMS 132, 885); Marletto & Vedral 2017 (PRL 119, 240402); Minkowski 1910 (Geometrie der Zahlen, Teubner); Misra, Prigogine & Courbage 1979; Naimark 1940; Nyquist 1928; Odabasioglu, Celik & Pileggi 1998; Oppenheim 2023 (PRX 13, 041040); Oppenheim & Russo 2024 (arXiv:2402.19459); Page & Wootters 1983; Paynter 1961; Petz 1996 (Linear Algebra Appl. 244, 81); Polder & Van Hove 1971 (PRB 4, 3303); Polyuga & van der Schaft 2012; Pusz & Woronowicz 1978 (CMP 58, 273); Reeb & Wolf 2014 (NJP 16, 103011); Roth 1955 (Mathematika 2, 1); Rytov 1953; Salvia & Giovannetti 2020 (Quantum 4, 274; arXiv:1912.02099); Saulson 1990; Schnakenberg 1976; Shayegan et al. 2023 (Nat. Photon.); Shitara & Ueda 2016 (PRA 94, 062316); Skrzypczyk, Silva & Brunner 2015 (PRE 91, 052133); Smirne & Bassi 2015; Sparaciari, Jennings & Oppenheim 2017 (Nat. Commun. 8, 1895; arXiv:1701.01703); Spietz, Lehnert, Siddiqi & Schoelkopf 2003 (Science 300, 1929); Srivastava 2021 (arXiv:2008.05546); Stern 1858 (J. reine angew. Math. 55, 193); Stinespring 1955; Sz.-Nagy 1953; Titchmarsh 1937; Toyabe et al. 2010 (PRL 104, 198103); Twiss 1955; van der Schaft 2021 (arXiv:2010.04213); Wiener 1933; Wigner & Yanase 1963; Willems 1972; Yaida 2019 (ICLR); Yunger Halpern, Faist, Oppenheim & Winter 2016 (Nat. Commun. 7, 12051); Zames 1966; Zanardi & Rasetti 1997; Zemanian 1965; Zhu & Fan 2014 (PRB 90, 220301).
