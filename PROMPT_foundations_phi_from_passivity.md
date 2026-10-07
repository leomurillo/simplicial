# SESSION PROMPT — Paper 54: The One Functional, Derived (Φ = log Z from passivity)

Open a fresh Claude Code session in `C:\Projects\simplicial` and paste everything below.

---

This is a FOUNDATIONS paper: short (target 15–25k characters), fully [P] at its core, and the
first layer of the corpus reorganization. Its job is to put the program's "one functional"
on a derived footing. Paper 32 *posits* Φ = log Z as "the categorical effective action". The
Port Principle *derives* it. Write that derivation as its own manuscript, certify it with
exact arithmetic, and then (Phase 2) propagate the consequences into Papers 32 and 32.1.

## Why this paper, and why now (context from the 2026-10-01 session)

- A full review of Papers 32 and 32.1 found the arithmetic core solid. The physics layer,
  however, carries identifications labelled [P]. Read `memory/project_corpus_reorg_first_principles.md`
  (the fix list) and `memory/project_toe_synthesis_one_inequality.md` (the synthesis) BEFORE
  starting. The memory directory is
  `C:\Users\leomu\.claude\projects\C--Projects-simplicial\memory\`.
- **Key reorganization insight:** the Port Principle sits BELOW Paper 32.
  - Complete passivity under the copy lift forces Gibbs/KMS states (PortPrinciple.md
    Theorem 6.3, Pusz–Woronowicz/Lenard).
  - The family of Gibbs states over all Hamiltonians is the categorical exponential family.
    Its generating function is Φ(θ) = log Z(θ).
  - Paper 32 Theorem 3.1 ("space = inertia": the Fisher metric is both the ruler and the
    inertia) is true in Paper 32 only because the Lagrangian is DEFINED with ½g(v,v). Its real
    content is the static fluctuation–dissipation theorem. ∇²Φ is the covariance of the
    sufficient statistics ("watching") and also the response of the mean to the natural
    parameter ("pushing"); this is the Koszul–Souriau "heat capacity = Fisher" identity.
  - That identity holds at equilibrium and FAILS away from it. The Port Principle (§10) says
    the gap between watching and pushing is the arrow. This gives Paper 32's identity a
    falsifiable non-equilibrium extension it currently lacks.
- **The Bekenstein bound belongs here too.** Casini (Class. Quantum Grav. 25 (2008) 205021)
  derives it from positivity of relative entropy relative to the vacuum's modular
  Hamiltonian. The 2π is the Bisognano–Wichmann KMS temperature. That is the Port
  Principle's bath passivity (PortPrinciple.md §10: βQ = ΔS + I + D ≥ ΔS). Paper 32.1 §5–6
  currently derive the bound from trivial facts (S_max = log Q, Fisher–Rao diameter π) plus
  a circular step (Remark 4.3 defines an energy so that it saturates the bound). This paper
  supplies the correct foundation.

## READ IN FULL FIRST

1. `PortPrinciple.md`: §2 (Defs 2.2–2.5, Prop 2.3), §3 (lift calculus), §6 up to and
   including Theorem 6.3 and the fluctuation–dissipation material, §10 (the arrow; bath
   passivity).
2. `32_one_functional_four_forces_v0.2 (2).md`: §1–§4 (Claim 2.1, Theorem 3.1,
   Remark 3.2 Koszul–Souriau, Theorem 4.1, Remark 4.2), §8, §9.1, §12. Paper 32 v0.3
   lives at this filename; its WIP twin is archived.
3. `32.1_the_bekenstein_sphere.md`: §2–§6 and §10 (what must be rebuilt).
4. `T2-CumulantTowerEffectiveAction.md` and `01c.simplicial_information_geometry.md`.
   These overlap each other and Paper 32 §2. The new paper must SUPERSEDE their shared
   "Φ as effective action" claim by deriving it, not add a fourth version.
5. `D2_discrete_einstein.md` and `order4_synthesis.md`. Skim only, for the cumulant-tower
   vocabulary; do not import their [A]/[C] readings into the [P] core.
6. `53_passive_ports_and_the_explicit_formula.md`, the companion bridge paper. Match its
   style and tier discipline.

## THE PAPER: `54_one_functional_from_passivity.md`

**Working title:** "The One Functional, Derived: Gibbs, the Cumulant Tower, and Space = Inertia
as Fluctuation–Dissipation."

Required results, with target tiers:

1. **[P] From the port constraint to Φ.** Complete passivity (all copies) ⟺ Gibbs (cite
   PortPrinciple Thm 6.3). On a Q-outcome system, the set of Gibbs states over all
   Hamiltonians H (θ = −βH up to the gauge 𝟙) is the open categorical simplex as an
   exponential family. The free-energy generating function is Φ(θ) = log Z(θ). Its Legendre
   dual is negative entropy. Nothing is posited: "the one functional" is the
   generating function of the free states of the copy lift.
2. **[P] Static fluctuation–dissipation = the second cumulant.** ∇²Φ(θ) equals the
   covariance of the sufficient statistics, which equals ∂⟨T⟩/∂θ, the linear response,
   which equals the Fisher metric. State it as one theorem with three readings: watching
   (covariance), pushing (response), distinguishing (Fisher). This is Paper 32 Theorem 3.1
   with its content made explicit. Credit Koszul–Souriau, Barbaresco, and the classical FDT
   (Callen–Welton, Kubo).
3. **[P] Where it fails, and why that is the arrow.**
   - For a non-equilibrium steady state (a Markov chain without detailed balance), the
     static response of a stationary observable to a potential perturbation differs from
     the covariance.
   - Prove for finite chains that the defect is controlled by the antisymmetric part of
     the generator (the probability current). Tie it to PortPrinciple §10 and to
     `forward3_reversibility.md` (arrow dimension = first Betti number b₁).
   - Pre-register a FALSIFIER before deriving it: e.g. "the response–covariance gap
     vanishes iff detailed balance".
4. **[P, credited] The tower's first rungs, with honest provenance.**
   - Third cumulant = the Amari–Chentsov cubic.
   - The Levi-Civita curvature of a Hessian metric is a quadratic contraction of the cubic:
     R = AN(T). This is classical Hessian geometry (Shima, *The Geometry of Hessian
     Structures*, 2007; Amari–Nagaoka). Paper 32 Remark 16.2b presents it as found; credit
     it.
   - The Hellinger sphere (K = ¼, radius 2, Fisher–Rao diameter π) and the capacity
     log Q are classical (Čencov; Amari–Nagaoka). State them as known.
5. **[P cited → reading A] Bekenstein from passivity.**
   - Finite form: for Gibbs σ = e^{−βH}/Z and any ρ, S(ρ) − S(σ) ≤ β(⟨H⟩_ρ − ⟨H⟩_σ), i.e.
     D(ρ‖σ) ≥ 0. This is exact and elementary.
   - Continuum form: Casini's theorem, with the modular Hamiltonian of a Rindler wedge
     equal to 2π × the boost generator (Bisognano–Wichmann). Cite; do not re-derive QFT.
   - Conclusion: the Bekenstein inequality is the Port Principle's passivity of a KMS
     state. 32.1's "2π coefficient [C]" is the KMS inverse temperature.
6. **[A] What this does to the dictionary.** Space = inertia holds as an equilibrium
   identity. "Gravity = closure defect" stays [C]. The firewall is a principle (true by
   construction), not a theorem. The dimensional-selection and signature claims of
   Paper 32 are out of scope here; list them as Phase-2 relabels.

Keep it SHORT. This is a foundations note, not a survey. No RH, no consciousness, no
cosmology in the body.

## CERTIFICATE: `empirical/foundations54/p54_cert.py`

Use exact sympy/Fraction arithmetic; numpy is fine. **Never run torch locally** (it crashed
this laptop). Write the K/L falsifiers into the docstring BEFORE the first run.

- **K1 [exact]** Complete passivity forces Gibbs. Re-verify on small systems by
  brute-force ergotropy of ρ^{⊗n}. You may import the logic of `empirical/port_principle/p4_review_v2.py`
  or `p5_copy_threshold_and_circuits.py`; copy helpers VERBATIM, never retype them.
- **K2 [exact, symbolic]** For Q = 3 and Q = 4:
  - Hess log Z = Cov(T) = ∂⟨T⟩/∂θ = Fisher metric, identically in θ.
  - The third derivative equals the third cumulant equals the Amari–Chentsov tensor.
- **K3 [exact]** The non-equilibrium matched pair:
  - A 3-state chain WITH detailed balance has response = covariance exactly.
  - A 3-state cycle WITHOUT it has a nonzero gap, and the gap is predicted by the
    current. Pre-register the predicted form.
- **K4 [exact]** The Hessian-geometry curvature identity R = AN(T) on Q = 3, 4, 5, at and
  off the centroid. Reuse `empirical/phiF_curvature_reverify.py` if present; cite it.
- **K5 [exact]** Finite Bekenstein/passivity: D(ρ‖σ) ≥ 0 ⟺ S(ρ) − S(σ) ≤ β(⟨H⟩_ρ − ⟨H⟩_σ),
  on random rational spectra. Include equality iff ρ = σ.

**Pre-registration lessons from 2026-10-01 (follow them):**
- State asymptotic or scaling claims as bounded-constant or slope tests, never as
  pointwise local-exponent ceilings at finite size.
- Positive DEFINITE vs SEMIdefinite matters: a finite network's Gram has rank equal to its
  degree.
- Retain every pre-registered failure in a RUN LOG. A post-diagnosis check must be
  labelled NOT BLIND.
- A checker artifact (removable singularity, retyped-helper bug) is fixed and logged, not
  counted as a result.

## PHASE 2 (only after Phase 1 certs are GREEN): process the impact in full

Leo expects foundations shifts to be propagated into the manuscripts, not left as notes.

- **Paper 32** (`32_one_functional_four_forces_v0.2 (2).md`):
  - Make Claim 2.1 and Theorem 3.1 cite Paper 54 as the derivation.
  - Relabel Theorem 4.1(3) "gravity = closure defect" to [P] for the localization
    and [C] for the gravity reading.
  - Rename Theorem 9.1 "forced (3,1)". The −H dt is the contact sign of extended
    phase space, present in any dimension.
  - Dimensional selection §8: route 1 is "angular momentum is a vector ⟺ n = 3", which
    Def 8.1 encodes. Route 2 is specific to Z/6 (Z/30 gives 1+2+4 = 7) and lives on a
    different row. Remove "two independent routes agree".
  - §10.2 table: the "Lorentzian [P] local-tangent" row is post-hoc after the §14.2
    refutation, so label it post-diagnosis.
  - §10.3: sin²θ_W = 3/8 is textbook SU(5) given the 2+3 split; Y ∝ (½, −⅓) is forced by
    tracelessness on any p₁+p₂ split. Retier to [A] with the provenance stated.
  - §12: "Firewall Theorem" becomes "Firewall Principle (by construction)".
  - Credit R = AN(T) to Shima.
- **Paper 32.1:**
  - Rebuild §5–§6 on Paper 54's passivity/Casini result.
  - Remark 4.3 is circular; remove it or demote it.
  - Call the §7 "holographic boundary" an *arithmetic (unit-group) boundary*, not a
    spatial one.
  - Keep §11 (Landau constant) and §13 (ladder laws) unchanged; they are the genuine [P]
    content.
- **T2 and 01c:** add a one-line forward pointer saying "Φ as effective action" is derived
  in Paper 54. Do not delete content.
- **README.md:** add Paper 54 under the numbered list, with a one-paragraph summary, as
  was done for 53.
- Keep an edit ledger: every change made to 32/32.1, as file:section → old → new. Put it in
  the internal HTML-comment log of each paper, not in a new Note file. Standalone notes are
  tech debt.

## RULES

- Papers lead. No standalone `Note_*.md`; results land in numbered manuscripts.
- Tiers [P]/[A]/[C] on every claim; GPD method (Paper 35); exact arithmetic decides.
- Manuscripts use LaTeX math. Chat replies use plain Unicode math (no `$...$`).
- Work serially. Do not fan out parallel agents.
- Credit prior art honestly: Koszul, Souriau, Barbaresco, Shima, Amari–Nagaoka, Čencov,
  Pusz–Woronowicz, Lenard, Casini, Bisognano–Wichmann, Callen–Welton, Kubo.
- Do not touch `PortPrinciple.md` beyond adding a one-line pointer if needed. Its internal
  log documents a deliberate exclusion of RH and consciousness.

## DONE WHEN

1. `54_one_functional_from_passivity.md` is written, with abstract, results 1–6, and
   references.
2. `empirical/foundations54/p54_cert.py` runs green, with every pre-registered failure
   retained and labelled.
3. Phase 2 edits to 32, 32.1, T2, 01c and README are made and ledgered.
4. Memory is updated: add a project memory for Paper 54 and update
   `project_corpus_reorg_first_principles.md` (mark the fix list items done).
5. Final report to Leo in under 300 words, plain Unicode math: what is [P], what was
   relabelled, which checks failed and why, and the single best next move.
