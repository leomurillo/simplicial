# SESSION PROMPT — Paper 55: The Network of Ports (where space, light cones, and area laws come from)

Open a fresh Claude Code session in `C:\Projects\simplicial` and paste everything below.

---

This is a CONSTRUCTION paper and the program's missing layer. Everything so far lives on ONE
finite system: a categorical simplex, its Fisher sphere, its cumulant tower. Physical space
cannot live there. Three negative results already say so:

- **Paper 32 §14.2** refuted a Lorentzian signature at the manifold level. A single
  simplex's Bures lift is Euclidean-4.
- **Paper 32.1 §7** found no geometric area law. The "boundary" there is the unit group of
  Z/N, a boundary in the divisor poset, not a spatial one.
- **Paper 32 §8 / G3** concedes that "experienced space" is a closure-valid block, "not yet
  a physical-space reconstruction".

**Thesis to build and test:** physical space is a NETWORK OF PORTS. Nodes are finite
simplices (finite distinguishability). Edges are passive ports. The network's combinatorial
geometry — its graph Laplacian, discrete exterior calculus, Hodge theory and Betti numbers —
is space. Treat the three negatives above as goals to break.

## Context from the 2026-10-01 session (read these memory files first)

Memory directory: `C:\Users\leomu\.claude\projects\C--Projects-simplicial\memory\`

- `project_toe_synthesis_one_inequality.md`: one inequality (passivity = positive-real
  response = positive energy) at every place, and "space = network of ports".
- `project_corpus_reorg_first_principles.md`: the 32/32.1 review and the layered
  architecture. This paper is Layer II/III's spatial half.
- `project_port_principle_paper.md` and `project_port_forest_pontryagin_summit.md`: the
  lift calculus and the spacing-lattice ↔ torus picture.
- `user_thesis_finite_grid_overflow.md`: Leo's framing compass (a finite grid plus a
  designated leakage channel). Use it to recognize shape. Do NOT inject it into the
  technical manuscript.

## READ IN FULL FIRST

1. `PortPrinciple.md`: Defs 2.1–2.5 (ports, wave variables, the active-port boundary
   rule), Theorems 4.1–4.5 (dilation, echo-or-forget), Theorem 5.1 (passivity ⟹
   causality), §8 (noise = temperature × defect Gram; FDT on every loss), §10 (the arrow),
   §11 (the modeling calculus: Kirchhoff/Bosma, compositional passive networks,
   Baez–Fong), Theorem 6.11 (Petz metrics = self-dual RL circuits).
2. `53_passive_ports_and_the_explicit_formula.md`: the zeta port as an infinite LC
   (Foster) chain; Pick/defect-Gram rank = ledger dimension. Reuse its conventions.
3. The simplicial frame, i.e. the discrete calculus on the tetrahedron:
   - `01b.simplicial_vector_calculus.md`: grad/div/curl; curl = K̃(grad); K̃ = ⋆_E d₀ on
     K₄ as DEC.
   - `01d.simplicial_keystone_integration.md`: the complete-graph Laplacian, the FEEC
     bicomplex, the orientation gauge.
   - `forward1_spectral_generalN.md`: the metric as complete-graph Laplacian.
   - `forward3_reversibility.md`: discrete Hodge decomposition; arrow of time = first
     Betti number.
   - `forward5_gauge_curvature.md`: gauge curvature of varying frames; abelian triviality.
4. `32_one_functional_four_forces_v0.2 (2).md` §8, §9, §14.2, and
   `32.1_the_bekenstein_sphere.md` §7, §10. These are what to break.
5. `46_hartle_hawking_signature.md`: the local (1,3) Casimir–Hessian sub-bundle. It is
   post-hoc after the refutation; read it critically.
6. `Pinf-WhatIsMultiplicative-Draft1.md` §2: the MULTIPLICATIVE second-order invariant
   (intersection form, Hodge index) is Lorentzian (1, ρ−1). It is an alternative source of
   signature; compare it with what the network gives.
7. Speculative ancestor, fenced and never cited as evidence: Leo's Occupation Thesis,
   `C:\Users\leomu\Downloads\occupation_thesis_arxiv_v4.pdf`. Relevant pieces:
   - a four-valent tetrahedral "Storm-Ball" network;
   - a phase-sector dispersion ω² = Ω²Σ(1 − cos k·δₙ) giving ω² ≈ c²k²(1 − ℓ²k²/36),
     η̃ = 1/72 on the tetrahedral first-neighbor shell;
   - node-scale "holographic screening" I ≤ Σ cap(b_ij);
   - "Cyclone" (looped/matter) versus "Unlooped" (radiation).

   The 2026-10-01 session mapped looped/unlooped onto echo-or-forget: pure point spectrum
   vs continuous.

## HYPOTHESES TO SETTLE (pre-register a K/L matched pair for each BEFORE computing)

- **H1 [target P] Composition.** A network of passive ports, connected by Kirchhoff
  constraints, is a passive multiport. Kirchhoff's current law is the network's Noether
  conservation. The network's admittance is a weighted graph Laplacian. Identify that
  Laplacian with the program's complete-graph Laplacian on K₄ (01d/forward1) for a single
  tetrahedron.
- **H2 [target P] Light cones from lossless ports.**
  - A network of LOSSLESS reactive ports (L and C: the Foster tanks of Paper 53) has a
    hyperbolic continuum limit: the telegrapher's wave equation, with finite speed
    c = 1/√(LC) and causal cones.
  - A network of LOSSY ports (R and C) has a parabolic (diffusive, Euclidean) limit.
  - Prediction: Lorentzian signature is a property of lossless networks, not of single
    nodes. Paper 32's Euclidean-4 verdict for one node's Bures lift is then the statement
    that a single node has no light cone.
  - Make this precise with exact discrete dispersion relations: LC ladder
    ω = (2/√(LC)) sin(k/2) versus RC diffusion.
  - Compare with the multiplicative (1, ρ−1) route. Are they the same signature or two
    different ones?
- **H3 [target P, imported + new instance] Area law from passivity + locality.**
  - Gibbs states of local Hamiltonians obey a thermal mutual-information area law:
    I(A:B) ≤ 2β‖h‖·|∂A| (Wolf–Verstraete–Hastings–Cirac, PRL 100 (2008) 070502). Copy
    lift ⟹ Gibbs; network locality ⟹ area law.
  - Prove the instance for networks of passive ports. Then compute it exactly for
    Gaussian (harmonic) networks, where covariance matrices give exact mutual information,
    on 1D/2D/3D lattices including the tetrahedral (diamond) lattice.
  - Fit I(A:B) against |∂A| and against |A| as BANDS, not pointwise exponents.
  - This is the area law 32.1 could not get from one simplex.
- **H4 [target P] Boundary-capacity bound.** The information that can cross a cut of the
  network per unit time is bounded by the sum of the cut ports' capacities. Each passive
  port at temperature T has a Shannon–Nyquist capacity set by its noise, and the noise is
  temperature × defect Gram (PortPrinciple §8). This is the rigorous form of the Occupation
  Thesis's "I ≤ Σ cap(b_ij)" and a Bekenstein-type bound on networks.
- **H5 [target P] Arrow = cycle space.** Non-equilibrium steady states of the network
  carry probability/charge currents on its cycle space. Their dimension is b₁ (forward3).
  Lossless loops echo; lossy or driven loops forget, and they carry the arrow.
  - Tie this to the looped/unlooped reading as [A].
  - Tie it to PortPrinciple Prop 6.9e (echo–yield) as [A]: the loop frequencies'
    arithmetic rank governs echo times.
- **H6 [A→P if possible] Which network?**
  - Is four-valent tetrahedral coordination singled out? Test rigidity (Maxwell counting:
    in 3D, generic rigidity needs average degree ≥ 6, so a four-valent network is NOT
    rigid as a bar framework). Report honestly what it does give: diamond-lattice
    isotropy at second order, and the η̃ = 1/72 dispersion. Verify that dispersion exactly.
  - Compare with the simplicial complex built from K₄ cells, whose DEC is 01b/01d.
  - Do not force a match.
- **H7 [C, fenced] Gauge.** Edge phases/orientations as a connection; holonomy around
  cycles as curvature. 01d/forward5 found abelian triviality for flat frames. State what
  survives on a network with cycles (holonomy ≠ 1 iff flux through cycles). Keep this
  short and fenced.

## THE PAPER: `55_the_network_of_ports.md`

**Working title:** "The Network of Ports: Space, Light Cones, and Area Laws from Passive
Composition."

**Suggested arc:**
1. Why one simplex cannot be space (the three negatives, cited).
2. Networks of ports: definitions and composition (H1).
3. Light cones from losslessness (H2).
4. Area law and the capacity bound (H3, H4).
5. The arrow on the cycle space (H5).
6. Which network (H6).
7. Fenced outlook: gauge (H7); the Occupation Thesis lineage; how this fills the
   "network" layer of the corpus architecture.
8. What is [P], what is [A], what failed.

**Credit prior art honestly:** Kirchhoff; Foster; Cauer; Brune; Darlington; Willems
(dissipativity); van der Schaft (port-Hamiltonian systems); Baez–Fong (compositional
passive networks); Lieb–Robinson (finite propagation speed on lattices); Wolf–Verstraete–
Hastings–Cirac (thermal area law); Eisert–Cramer–Plenio (area laws review); Hastings
(1D area law); Maxwell (rigidity counting); Desbrun–Hirani and Arnold–Falk–Winther
(DEC/FEEC). Port-Hamiltonian systems theory is the closest existing framework: say
precisely what is new relative to it.

## CERTIFICATE: `empirical/network55/p55_cert.py`

numpy/sympy/mpmath only. **Never run torch locally** (it crashed this laptop; torch runs on
GCP only). Write the K/L text into the docstring BEFORE the first run.

- **K1 [exact]** Random passive 2-ports composed into small networks stay passive (Pick or
  symmetric-part PSD). The Kirchhoff admittance equals a weighted graph Laplacian. The K₄
  Laplacian is 4I − J.
- **K2 [exact]** LC ladder versus RC ladder: exact discrete dispersion. LC has a finite
  maximal group velocity and a strict light cone. Check the support of the response at
  t: exact zero outside the cone for the discrete-time leapfrog scheme, or exponentially
  small Lieb–Robinson tails for continuous time; pre-register WHICH. RC has diffusive
  t^{1/2} spreading.
- **K3 [numerics, exact covariance]** Gaussian thermal states on harmonic networks (chain,
  square, cubic, diamond lattices): mutual information I(A:B) scales with |∂A| within a
  pre-registered band, and is not proportional to |A|. Include a long-range control (all-to-all
  coupling) that violates the area law. **No sampling noise:** use exact covariance
  formulas.
- **K4 [exact]** The cut-capacity bound holds on random networks; equality conditions
  identified.
- **K5 [exact]** Steady-state currents live in the cycle space; dim = b₁. A tree network has
  no steady current.
- **K6 [exact, sympy]** Tetrahedral first-shell dispersion: ω² = c²k²(1 − ℓ²k²/36 + O(k⁴)),
  isotropic at that order, η̃ = 1/72. Pre-register; this may FAIL if the isotropy claim is
  wrong. Retain the result either way.

**Pre-registration lessons from 2026-10-01 (follow them):**
- Asymptotic and scaling claims are tested as bounded-constant bands or fitted slopes over
  ranges, never as pointwise local-exponent ceilings at finite size.
- A finite network's Gram/Pick matrix is positive SEMIdefinite, with rank equal to its
  degree. Do not demand definiteness.
- Copy shared helpers verbatim from existing certificates; never retype them.
- Retain every failure in a RUN LOG. Label post-diagnosis checks NOT BLIND. Checker
  artifacts are fixed and logged, not counted as results.

## RULES

- Papers lead. No standalone `Note_*.md`. Results land in Paper 55. If a result changes
  Paper 32/32.1/46, add a one-line forward pointer in that paper's internal log; do not
  rewrite those papers in this session.
- Tiers [P]/[A]/[C] on every claim. GPD method (Paper 35): fenced speculation sets a
  heading only, matched-pair falsifiers come first, exact arithmetic settles.
- Difficulty is a scale. Quantify what each result reduces; never write "the wall".
- Manuscripts use LaTeX math. Chat replies use plain Unicode math.
- Work serially. Do not fan out parallel agents.
- Keep the Occupation Thesis, the finite-grid thesis, consciousness and RH OUT of the
  technical body. The Occupation Thesis may appear once, as fenced lineage in the outlook.

## DONE WHEN

1. `55_the_network_of_ports.md` is written, with H1–H6 settled at stated tiers and H7
   fenced.
2. `empirical/network55/p55_cert.py` runs, with every pre-registered failure retained and
   labelled.
3. README.md lists Paper 55 with a one-paragraph summary.
4. Memory: add a project memory for Paper 55 and update
   `project_toe_synthesis_one_inequality.md` with what the network layer settled,
   especially H2 (does losslessness give the light cone?) and H3 (the area law).
5. Final report to Leo in under 300 words, plain Unicode math: which of the three negatives
   were broken, which held, and the single best next move.
