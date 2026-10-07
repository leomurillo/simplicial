# Publication And Knowledge-Base Strategy

Created: 2026-05-14
Last updated: 2026-05-15

The private graph is a disconfirmation machine. The public papers should not
reveal the whole route by which the graph was found. They should present the
minimal theorem spine, the necessary evidence, and the right audience-specific
motivation.

## Core Strategic Principle

Lead with the narrowest claim that is still genuinely new.

Bad public spine:

> We found the missing engine of AI, active inference, and physics.

Current strongest public spine:

> For categorical behavior spaces with finite algebraic output structure, the
> Fisher geometry has finite quotient-character coordinates. At maximum
> entropy these are conductor packets; off maximum entropy, their coupling is
> governed by an operator-valued finite adjacency algebra.

## Publication Lanes

| Lane | Working title / unit | Audience | Lead claim | Evidence to include | Claims to exclude |
|---|---|---|---|---|---|
| L1 | Simplicial vector calculus | geometry, numerical methods, frame theory | `N=4` simplicial coordinates give a gauge-compatible coordinate presentation of classical 3D algebraic rotations. | Theorems T1-T3, validation scripts, review fixes. | "New vector calculus" beyond algebraic rotations; differential operators. |
| L2 | Simplicial coordinates and Fisher geometry | information geometry, compositional data, ML theory | Fisher-Rao at uniform is the simplicial metric up to scale; softmax initialization and natural gradient have a native simplicial form. | T4-T5, Wurgaft/Hellinger bridge as motivation. | Global Fisher isometry claims; beyond-uniform claims not proved. |
| L3 | Fisher-conductor bridge | information geometry, finite harmonic analysis | At `p_*`, conductor packets are Fisher tangent spectral blocks; off-centroid flat-ray couplings obey convolution Taylor rules. | T6-T7, Ramanujan/Hayes formulas, Problem 10.1. | Neural universality; FEP. |
| L4 | Quotient-character adjacency algebras | algebra, finite fields, arithmetic geometry | Scalar conductor traces are lossy; the correct finite object is an operator-valued quotient-character adjacency algebra with filtered local `Ext_CH` obstruction. | T8-T10, E8-E10, closure-deficit ledger. | Transformer claims except as optional outlook. |
| L5 | AI behavior skeletons | ML interpretability, optimization, information geometry | Smooth behavior manifolds can have a finite arithmetic Fisher skeleton on structured labels; probes and update-side filters can diagnose it. | C7/C12 reports, activation pullback, bigram control, optimizer pilots. | General neural loss-landscape theory; "simplectic optimizers" as completed product. |
| L6 | Simplectic mechanics | mathematical physics, information geometry | Categorical simplices admit Nambu-Fisher volume-form mechanics with finite conductor closure criteria. | T12-T13 and finite-jet closure statements. | Physical correctness as a settled claim; FEP proof. |
| L7 | Conductor blankets / FEP | FEP, active inference, complex systems | Orthogonal conductor projection is a candidate finite arithmetic model of blanket-like update closure. | Update-only projection pilots and exact conductor closure, with caveats. | Exact Markov blanket theorem unless conditional independence and MI variables are formalized. |
| L8 | Cubic/Bures completion | information geometry, quantum information, mathematical physics | The real `R=Z/6Z` simplex has a Cartan obstruction, and Bures density matrices supply the bounded nonabelian completion. | T14-T16, Paper 24, Constraint 3 trajectory audit; Q1 only as exploratory outlook. | Complete QFT, Standard Model, gravity, or "gauge action inside transformers." |
| L9 | Primorial Noether-Weil program | internal / arithmetic theory only for now | Primorial cumulants define a conditional route whose blockers are explicit. | R1/R2, Z30 certificate, Constraint 3 audit, critical-leaf tower candidate. | Any unconditional RH proof claim. |

## Audience Translations

| Audience | Say this | Avoid this |
|---|---|---|
| Information geometers | "This is a finite Fourier/conductor coordinate system for Fisher tangent and off-centroid Taylor coupling." | "The simplex is literally a phase space for all learning." |
| Algebraists | "The filtered quotient-character adjacency algebra retains data erased by the conductor associated graded." | "Neural nets prove the algebra." |
| ML researchers | "Structured categorical outputs expose finite behavior-side channels that natural-gradient/Fisher tools can audit." | "All SGD discovers quotient characters." |
| FEP readers | "Projection onto closed conductor support is a finite algebraic analogue of update closure, and may model blanket-like shielding." | "This proves Friston's Markov blankets." |
| Physics readers | "Nambu-Fisher mechanics is a volume-form formalism on the categorical simplex." | "Symplectic mechanics is obsolete." |
| Quantum information readers | "The Bures lift is the density-matrix completion of the real-simplex Cartan obstruction." | "This derives a full quantum field theory." |
| Number theorists | "The primorial branch is a conditional verification ledger with named finite-place and Archimedean gaps." | "This proves RH." |

## Risk Register

| Risk | Trigger phrase | Safe replacement |
|---|---|---|
| Scope creep | "new vector calculus" | "algebraic rotation layer in simplicial coordinates" |
| Globalization | "Fisher symmetry of the simplex" | "tangent Fisher isometry at the uniform distribution" |
| Neural universality | "SGD is quotient-character flow" | "under structured labels and approximate equivariance, the behavior-side forcing admits quotient-character coordinates" |
| Ext confusion | "`K_CH` detects `Ext_CH`" | "`K_CH` is transparent to binary `Ext_CH`; Ext-sensitive probes require filtered adjacency or higher pullback defects" |
| FEP overclaim | "conductor packets are literal Markov blankets" | "conductor packets are candidate arithmetic blanket supports; conditional independence remains to be formalized" |
| Support/full closure confusion | "support closes" | "support closes; full filtered closure is separately tested" |
| Data provenance | "Wurgaft data proves..." | "local Llama/Mistral safetensor centroid reports show..." |
| Quantum overclaim | "transformer residual streams have SU(2) x SU(3) gauge symmetry" | "residual-stream audits show an exploratory Cartan/nonabelian survival split before measurement" |
| RH overclaim | "Primorial Noether-Weil proves RH" | "RH follows only if the finite-place recovery gaps, structural Constraint 3, and Archimedean Noether Limit are proved" |
| Three-body overclaim | "the three-body problem is solved / not chaotic" | "the Bures lift supplies a bounded information-geometric analogy; `paper16_draft (1).pdf` is quarantined" |

## Private KB Schema

These fields are enough for a lightweight table, SQLite DB, YAML directory, or
graph database.

### `claim`

- `id`
- `rank`: fundamental, theorem, corollary, conjecture, problem, observation
- `statement`
- `scope_hypotheses`
- `status`: proof, exact-computation, empirical, both, gap, risk
- `confidence`: 0-5
- `publication_ready`: yes/no/conditional
- `source_paths`
- `disconfirmation_question`

### `evidence`

- `id`
- `type`: theorem, exact-enum, seeded-computation, empirical, corpus-control, design-note, review
- `artifact_path`
- `date`
- `repro_command`
- `supports_claims`
- `pressures_claims`
- `limitations`

### `dependency`

- `from_claim`
- `to_claim`
- `relation`: depends_on, supports, refutes, narrows, generalizes, specializes, controls_for, does_not_transfer
- `notes`

### `risk`

- `id`
- `risk_type`: overclaim, transfer, confound, normalization, classicality, provenance, evidence-level
- `trigger_phrase`
- `safe_replacement`
- `blocking_level`: low, medium, high, critical
- `target_claims`

### `publication_unit`

- `id`
- `audience`
- `venue_candidates`
- `novelty_line`
- `required_prior_art`
- `include_claims`
- `exclude_claims`
- `must_run_before_submission`

## Next Concrete Moves

1. Promote `claim_graph.md` into a machine-readable `claims.yaml` only after one human review pass.
2. Add a provenance table for all safetensor-derived reports.
3. Extract Paper 11 exact computations into theorem/proof obligations: what is proven by finite enumeration, what is conjectured by pattern, what is merely support-level.
4. Run the months C12 probe on a second model family.
5. Add a checkpoint conductor audit for a small training run.
6. Formalize or downgrade the FEP mutual-information and conditional-independence claims before any FEP-facing submission.
7. Replicate the quantum-lift residual audit with random-label and shuffled-residual controls before using it outside an outlook section.
8. Keep the primorial/RH material internal until the Archimedean Noether Limit has a proof sketch strong enough for hostile review.
