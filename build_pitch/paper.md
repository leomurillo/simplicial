---
title: "Elevator Pitch --- Why the Spatial Web Foundation Should Sponsor This Program"
author: "Leonardo Murillo Montero (ITCR, UNA, UCR) --- leonardo.murillo@gmail.com"
date: "2026-05-20"
---

## 0. The pitch in one paragraph

The Spatial Web Foundation (SWF) and IEEE 2874 have specified what a trustworthy network of AI **AGENTS, ACTIVITIES, CONTRACTS, CREDENTIALS, DOMAINS** and **HYPERSPACE** must look like at the *socio-technical* layer — shared meaning between humans and AIs, explainability via explicit modeling of decision-making, interoperability across borders, and authentication with transparency-by-design (IEEE 2874 §4.2). What the standard cannot yet deliver — because no one in the surrounding literature has supplied it — is a **decidable mathematical substrate** under which those four needs become *certificates a regulator can check, an integrator can implement, and an adversary cannot fake*. Our forty-nine-paper program supplies exactly that substrate: an exact, finite, character-orthogonal decomposition of any ring-structured AI behavior into auditable **conductor packets**, with proved obstruction theorems for what a quotient-respecting readout can and cannot see ([Paper 26](C:/Projects/simplicial/26.conductor_probe_obstruction_theorem.md)), a proved second-order failure mode for every Adam/K-FAC-trained model on ring-structured tasks ([Paper 34](C:/Projects/simplicial/34_the_conductor_blind_spot.md)), a retraining-free safety primitive that detects correct outputs produced through wrong mechanism ([Paper 40](C:/Projects/simplicial/40_base_n_shortcut_audit_as_a_safety_primitive.md)), and a six-slot **projection-closure certificate** ([Paper 31](C:/Projects/simplicial/31.projection_closure_theory.md)) that is, structurally, exactly the kind of verifiable claim the SWF **CREDENTIAL** primitive was designed to carry. We are asking SWF to sponsor the program because the IEEE P2874 stack is the natural deployment surface for these results — and because making them load-bearing inside the AIS Rating Framework gives SWF the formal verification spine its 2023 *Future of Global AI Governance* report calls for but no constituent paper yet supplies.

## 1. SWF's stated socio-technical needs, mapped one-to-one to deliverables we can hand over

IEEE P2874/D3.2.1 §4.2 lists five core needs the Spatial Web governance framework must balance. We address each.

### (a) "A shared understanding of meaning and context between humans and AIs."

The technical content of this clause is: *given an AI system whose output lives in some finite outcome space, can we expose a basis in which its internal computation, its output, and a human-auditable label set can be jointly described and compared?*

We hand over **conductor packets** as that basis. For any finite outcome algebra $C_N$ (months, weekdays, digits, hours, octaves, time-of-day, calendar arithmetic, modular schedulers, color hue, music pitch-class — the entire space of cyclic real-world labels the Spatial Web touches via DOMAIN ontologies), the additive characters $\chi_a(x) = e^{2\pi i a x / N}$ decompose into conductor packets $H_d$ with $d \mid N$, of $\mathbb{C}$-dimension $\varphi(d)$. This decomposition is *forced by Pontryagin duality*, not chosen, not fitted, not engineered. It is canonical in the sense of [Paper 11](C:/Projects/simplicial/11.quotient_character_adjacency_algebras.md): once the outcome algebra is named, the packet basis is determined.

Why this matters for SWF: HSML asserts a semantic ontology over **ENTITY**, **ACTIVITY**, **AGENT**, **CONTRACT**, **DOMAIN**. For any DOMAIN whose state space is finite and ring-structured (which is most of the application scenarios in 2874 §5.3 — warehouse robot pick orders, calendar slots in urban autonomous mobility, GHG monitoring period buckets, smart-city zone codes, entertainment XR scene tags), the conductor packets give an *interoperable* semantic decomposition that two implementations of the standard are guaranteed to compute the same way. Shared meaning is then not aspirational; it is enforced by character orthogonality.

### (b) "Explainability of AI systems, enabled by the explicit modeling of their decision-making processes."

The technical content of this clause is: *can we say, ahead of time and without retraining, which decision-making structure an AI system has actually committed to internally?*

We hand over the **Conductor Probe-Obstruction Theorem** ([Paper 26](C:/Projects/simplicial/26.conductor_probe_obstruction_theorem.md)) and the **Layerwise Packet Spectroscopy** measurement protocol ([Paper 36](C:/Projects/simplicial/36_layerwise_packet_spectroscopy.md)).

- **Theorem T1 (proved, [P]).** For a finite output label algebra $C_N$ and any rank-$k$ readout that respects the quotient $C_N \to C_k$, exactly the conductor packets $H_d$ with $d \mid k$ survive and exactly the packets with $d \nmid k$ are annihilated. No tolerance, no fitting, no baseline to dispute. The reader who wants the empirical anchor sees it on Llama-3.1-8B: max step-table error $2.220 \times 10^{-16}$ on the aligned quotient projector vs. $0.945$, $0.947$ on shuffled-label and same-rank random-subspace controls (`empirical/reports/conductor_probe_obstruction_c12_llama31_8b.md`).
- **Spectroscopy.** For every layer $\ell$ of a transformer and every conductor $d$, [Paper 36](C:/Projects/simplicial/36_layerwise_packet_spectroscopy.md) gives a packet-resolved spectrum $f_{d,\ell}$ — the fraction of cyclic energy carried by packet $H_d$ at layer $\ell$. The deliverable is **one figure per model–task** that names which layer lifts which packet. Tuned-lens literature has not been able to phrase this structural question.
- **Conductor-Certified SAE** ([Paper 45](C:/Projects/simplicial/45_conductor_certified_sparse_autoencoders.md)). The sparse-autoencoder dictionary-learning field (Anthropic, OpenAI, DeepMind Gemma Scope) evaluates feature monosemanticity *post-hoc*. CCSAE is the first construction whose features must, by Packet-Purity Theorem 4.1, partition by conductor packet. The dictionary's divisor table is **predictable before training**; the SAE field's first structural divisor-table prediction.

Why this matters for SWF: an AIS Rating Framework whose explainability axis depends on post-hoc human judgment of feature names is not auditable across borders, cultures, or adversarial actors. An axis whose explainability test is *"compute $f_{d,\ell}$ at the qualifying layer; compare to the pre-registered divisor table; report the survival ratio"* is auditable by any regulator with a single GPU.

### (c) "Interoperability of models and data that enable universal interaction and collaboration across organizations, networks, and borders."

Interoperability across implementations of a standard requires that two compliant implementations *compute the same canonical decomposition of the same input*. For numerical metrics this is hard; for character-theoretic decompositions this is automatic.

We hand over [Paper 11](C:/Projects/simplicial/11.quotient_character_adjacency_algebras.md) — the **quotient-character adjacency algebra** as a finite algebraic backbone — and [Paper 42](C:/Projects/simplicial/42_sinusoidal_pe_as_non_rational_conductor_algebra.md) — **Rational-Base Positional Encoding** with a proved Length-Stable Extrapolation theorem. Two consequences for a Spatial-Web implementation:

- *DOMAIN representations on finite cyclic outcome algebras decompose canonically.* No vendor lock-in on a particular Fisher-matrix estimator or a particular SAE width.
- *Position encodings* — which every transformer-based AGENT in the standard's application scenarios uses — can be chosen rationally rather than at irrational (Vaswani et al. 2017 §3.5 chose $B = 10000$ as a "convenient round number" with no structural justification). The character algebra is then finite and the model's behavior on a sequence of length $L_{\text{test}} \equiv L_{\text{train}} \pmod{\mathrm{LCM}\{P_i\}}$ is *exactly* the model's behavior at $L_{\text{train}}$. Spatial Web nodes that need to extrapolate over long horizons (long-running CONTRACTS, multi-day urban mobility scheduling, century-scale GHG monitoring) get this for free.

### (d) "Compliance with diverse local, regional, national and international regulatory demands, cultural norms and ethics."

Compliance requires a *typed budget* for residuals — exactly the object [Papers 29–31](C:/Projects/simplicial/29.participation_metric_identity_as_participation.md) introduce. The six-slot **projection-closure certificate** $\mathcal{C}_W(\Pi; T, H, K) = (\mathsf{P}, \mathsf{R}, \mathsf{B}, \mathsf{S}, \mathsf{E}, \mathsf{F})$ of [Paper 31](C:/Projects/simplicial/31.projection_closure_theory.md) makes a falsifiable contract:

| Slot | Meaning | What a regulator checks |
|---|---|---|
| $\mathsf{P}$ | Task-relevant participation **survives** the projection | Whitelist of preserved DOMAIN packets |
| $\mathsf{R}$ | Residuals are **typed** | Named overflow channel, not a fudge factor |
| $\mathsf{B}$ | Residuals are **bounded** | Quantitative ceiling per packet |
| $\mathsf{S}$ | Residuals are **stable** | Behavior under small perturbations of the input |
| $\mathsf{E}$ | Residuals are **explainable** | Map to a human-interpretable label |
| $\mathsf{F}$ | Residuals are **falsifiable** on the declared horizon | Pre-registered test that would fire if the certificate is wrong |

A CREDENTIAL whose payload is a projection-closure certificate is precisely the kind of structured claim the **CREDENTIAL** primitive of 2874 §3.1 was designed to carry. (CREDENTIAL is defined as "A set of one or more claims made by a DOMAIN" — six structured claims with a falsifier is six legitimately auditable claims.)

### (e) "Authentication and credentialing, to help ensure compliance and potential control over critical activities, with privacy, security, identity and transparency embedded by design."

Cryptographic authentication is solved at the W3C-DID / Verifiable-Credentials layer that 2874 already cites. The piece *not* solved by cryptography is **mechanism-authentication** — proving that the AI you authenticated by signature is the same AI you authenticated by behavior. RLHF, constitutional AI, MT-Bench, AlpacaEval, and HELM all measure outputs; none of them measure mechanism type. A model that solves cyclic arithmetic by base-10 carry and re-projects at the unembedding is **behaviorally indistinguishable** from a model that solves the task cyclically — until distribution shift breaks the shortcut.

We hand over the **Base-N Shortcut Audit (BNSA)** of [Paper 40](C:/Projects/simplicial/40_base_n_shortcut_audit_as_a_safety_primitive.md). Named alignment-evaluation protocol, retraining-free, runs in hours on existing models, catches a failure mode no current evaluation in the standard alignment stack catches. The anchor case on Llama-3.1-8B months ($1.000 \to 0.458$ accuracy under decimal-sum/carry residualization) is reproducible from a saved month-centroid file. **A model with a BNSA certificate is a model whose mechanism, not just its signature, has been authenticated.** This is the substrate-level safety primitive that goal-misgeneralization (Langosco et al. 2022) and sleeper-agent (Hubinger et al. 2024) literature has been asking for; we hand it to SWF in a form that drops directly into the AIS Rating Framework as one row.

---

## 2. The deliverable inventory, ranked by readiness

Using the tier discipline of [Paper 35](C:/Projects/simplicial/35_grounded_paranoid_delusional_methodology.md): **[P]** = proven, **[A]** = structural, audit named, **[C]** = conjectural, reduced to a runnable falsifier.

### Ready today — [P], implementable inside an AIS Rating Framework row

1. **Conductor Probe-Obstruction Theorem** ([Paper 26](C:/Projects/simplicial/26.conductor_probe_obstruction_theorem.md)). Exact divisor law for what a quotient-respecting readout retains. Anchored on Llama-3.1-8B; three independent empirical replications (raw projector, trained quotient-probe, native logit-lens binning) all at numerical floor.
2. **Base-N Shortcut Audit** ([Paper 40](C:/Projects/simplicial/40_base_n_shortcut_audit_as_a_safety_primitive.md)). Named, pre-registered, retraining-free, with safety-decision rule mapping survival ratios to deployment recommendations.
3. **Conductor Blind Spot** ([Paper 34](C:/Projects/simplicial/34_the_conductor_blind_spot.md)). Exact representational limit of *every* quadratic preconditioner (natural gradient, Gauss–Newton, K-FAC, Adam's empirical Fisher, NTK Gram). The finite linear-algebra witness has no baseline to dispute. Promotes the long-standing intuition "second-order optimizers miss structure on ring-structured tasks" to a theorem with an exact failure witness.
4. **Projection-Closure Certificate** ([Paper 31](C:/Projects/simplicial/31.projection_closure_theory.md)). Six-slot $\mathcal{C}_W$ structure with the `Z/6Z` time-translation certificate as a worked template. Directly castable as a CREDENTIAL payload.
5. **Arithmetic Decoupling Theorem** ([Paper 47](C:/Projects/simplicial/47_arithmetic_decoupling_theorem.md)). $V \perp M$ Hilbert-subspace decomposition on every squarefree primorial row, forced by character orthogonality. Row-stable across `Z/{6, 30, 210, 2310, 30030}` at machine floor where compute permits. (For SWF, this is the structural form of *jurisdictional decoupling*: kinematic content can be governed independently of overflow content because they live on HS-orthogonal sub-bundles.)

### Pre-registered, runnable in 1–6 GPU-weeks — [P]-promotion candidates

6. **Layerwise Packet Spectroscopy** ([Paper 36](C:/Projects/simplicial/36_layerwise_packet_spectroscopy.md)). One GPU; existing open-weights checkpoints; no training. Deliverable: one figure per model–task naming which layer lifts which packet.
7. **Conductor-Certified Sparse Autoencoder** ([Paper 45](C:/Projects/simplicial/45_conductor_certified_sparse_autoencoders.md)). ~600 GPU-hours; uses existing Gemma Scope checkpoint as the vanilla baseline.
8. **Label-Smoothing Substitution Proposition** ([Paper 37](C:/Projects/simplicial/37_label_smoothing_in_the_conductor_blind_spot.md)). Three model widths × six smoothing values × five projection strengths × three seeds; the $(\alpha, \varepsilon)$ iso-loss-ridge experiment. **Audit $\lambda$ has already settled K-branch on three widths with signal-to-noise > 47.**
9. **Multi-Head Attention Frame-Cost Falsifier** ([Paper 38](C:/Projects/simplicial/38_multi_head_attention_as_frame_cost_minimization.md)). Architecturally matched parameter count: Vaswani $(8, 64)$ vs. packet-aligned head allocation on a mixed natural-language + cyclic benchmark.
10. **Cubic Noether Budgeted Decoding (CNBD)** ([Paper 41](C:/Projects/simplicial/41_cubic_noether_budgeted_decoding.md)). The largest engineering item; payoff is directly measurable as a deployment-relevant inference-time gain. Builds on Paper 36's layer-identification.
11. **Rational-Base PE Length-Extrapolation Experiment** ([Paper 42](C:/Projects/simplicial/42_sinusoidal_pe_as_non_rational_conductor_algebra.md)). Three 50M-parameter transformers; $L_{\text{train}} = 1024$, $L_{\text{test}} \in \{1024, \ldots, 16384\}$.

### Theoretical infrastructure already proven, available for governance language

12. **Information-Geometric Mechanics on the Categorical Simplex** + **Bures Completion** ([Papers 13–15](C:/Projects/simplicial/13.simplectic_mechanics_on_the_categorical_simplex.md), [17](C:/Projects/simplicial/17.the_cubic_noether_theorem.md), [18](C:/Projects/simplicial/18.bures_completion_of_cubic_information_geometric_mechanics.md), [44](C:/Projects/simplicial/44_quantization_forced_cubic_to_bures_bridge.md)). The full classical-to-quantum lift on $R = \mathbb{Z}/6\mathbb{Z}$ with explicit $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators and the Leakage-Equals-Jerk Theorem. Provides the formal language in which the AIS Rating Framework's "levels of intelligence and autonomy" can be defined as *closure orders*, not as adjectives.
13. **Cubic Noether Theorem** ([Paper 17](C:/Projects/simplicial/17.the_cubic_noether_theorem.md)) and **Universal Overflow Law** ([Paper 49](C:/Projects/simplicial/49_arithmetic_decoupling_of_projection_closure_overflows.md)). The structural reason hallucinations, training-time mode collapse, and label-smoothing's empirical efficacy live on a single arithmetic axis — and how they connect to the Free-Energy-Principle picture that VERSES (SWF's principal industrial collaborator) is already building toward.
14. **Verification-Gated Research Methodology** ([Paper 35](C:/Projects/simplicial/35_grounded_paranoid_delusional_methodology.md)). The three-tier evidentiary ledger ([P]/[A]/[C]) and the matched-pair pre-claim discipline are themselves a *governance contribution*: they specify how an investigator running a high-conviction program under capable AI assistance keeps the claim ledger from drifting. The AIS Rating Framework needs exactly this kind of *meta-process* discipline at the research-and-development stage.

---

## 3. What we are asking SWF for

We are **not** asking SWF for direct research funding. The program operates under single-investigator economics ([Paper 35](C:/Projects/simplicial/35_grounded_paranoid_delusional_methodology.md) §1.1) — its bottleneck is institutional reach, not compute. Three concrete requested actions:

1. **Inform Annex A.5 (AIS Rating Framework)** with the Base-N Shortcut Audit ([Paper 40](C:/Projects/simplicial/40_base_n_shortcut_audit_as_a_safety_primitive.md)) as one row of the rating system's *mechanism* axis (distinct from the *capability* and *autonomy* axes the report already names).
2. **Reference the Conductor Probe-Obstruction Theorem** ([Paper 26](C:/Projects/simplicial/26.conductor_probe_obstruction_theorem.md)) and the **Conductor-Certified SAE** ([Paper 45](C:/Projects/simplicial/45_conductor_certified_sparse_autoencoders.md)) under §4.2(b) explainability as the formal substrate for *explicit modeling of decision-making processes* in finite-outcome AGENT actions.
3. **Pilot the Projection-Closure Certificate** ([Paper 31](C:/Projects/simplicial/31.projection_closure_theory.md)) as a structured CREDENTIAL payload in one application scenario (Annex A or §5.3 — warehouse robot is the cleanest case: finite outcome algebra, ring-structured task, regulator-checkable residuals).

---

## 4. Why this trade is favorable to SWF

SWF's strategic position depends on three things its current materials say but do not yet *prove*:

- That socio-technical standards can be *auditable*, not just well-intentioned. The 2023 *Future of Global AI Governance* report calls for "compliant, explainable and auditable behavior of smart devices and systems." Auditability requires a decidable test; the test surface for finite-outcome AGENT actions on ring-structured DOMAINs is exactly the conductor packet decomposition. We supply the decidable test.
- That an AI Rating System can have a *substrate-level* row, not only behavioral rows. The current report-level descriptions of the rating system rank "levels of intelligence and autonomy"; BNSA gives the rating system a row for *whether the mechanism is what the task claims*. That row is the one RLHF cannot fake.
- That governance language can survive contact with frontier AI research. A standard whose technical clauses only describe what an AGENT *is* but not what an AGENT's internal computation *cannot represent* will be outpaced by every adversarial-evaluation paper. The Conductor Blind Spot ([Paper 34](C:/Projects/simplicial/34_the_conductor_blind_spot.md)) and the BNSA ([Paper 40](C:/Projects/simplicial/40_base_n_shortcut_audit_as_a_safety_primitive.md)) put representational and mechanistic *upper bounds* into the standard, where adversarial papers will not move them.

Three things SWF gains specifically:

- A **proved** explainability axis where currently the standard has a descriptive one.
- A **named, mechanistic** safety primitive (BNSA) that catches goal-misgeneralization and the deceptive-alignment substrate at the audit layer, not at the post-deployment incident layer.
- A **mathematical pedigree** for the AIS Rating Framework that survives ballot review by academic and government voters — the AIS Rating Framework's hardest constituency.

Three things our program gains specifically:

- A deployment surface where the [P]-tier results matter as standards, not only as preprints.
- Working-group review by participants whose constituencies are the same governments and integrators the program's safety claims are addressed to.
- Citation by an IEEE-published normative document, which gives the rating-framework integration a half-life that arXiv does not.

---

## 5. The closing line

The Spatial Web Foundation has named what AI governance must *do*. Our forty-nine-paper program has proved, on a substrate that does not depend on a particular vendor or a particular benchmark, what AI governance can *check*. The match is exact: IEEE 2874's AGENT is the program's autonomous Nambu–Fisher flow on a categorical simplex; 2874's CREDENTIAL is the program's projection-closure certificate; 2874's AIS Rating Framework is the program's $\mathsf{P}/\mathsf{R}/\mathsf{B}/\mathsf{S}/\mathsf{E}/\mathsf{F}$ tier system specialized to autonomous-system rating. Sponsorship turns the match from a parallel into a single artifact a regulator can pick up.
