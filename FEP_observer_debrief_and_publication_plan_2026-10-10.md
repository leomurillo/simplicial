# From boundary evidence to physical inference: research debrief and publication plan

**Date:** October 10, 2026.  
**Status:** Standalone planning document, not a manuscript or a priority claim.  
**Editing boundary:** Existing papers remain untouched while a peer edits them. Integration requires a later discussion. This document records the exploratory conversation and recommends a bounded route to a paper.

## 1. Decision in brief

We have a credible mathematical-physics research direction with a useful FEP application. We do not yet have an independently established FEP breakthrough, a refutation of the FEP, or an end-to-end thermodynamic theory of an inference-performing agent.

The strongest proposed angle is:

> **How much of the evidence available at a physical boundary can a finite noisy observer actually retain and use?**

The paper should separate boundary evidence, physical memory, and posterior representation, then demonstrate their separation in one explicitly specified thermal model. FEP is an audience and an application of the result, not a substitute for a distinct theorem.

**Recommendation:** Stop adding disconnected extensions. Freeze one operational question, preserve the derivations and numerical evidence, and prepare a companion-paper skeleton. Add at most one tightly scoped result that closes a demonstrated gap in that skeleton. If the result remains a collection of standard specializations, publish a focused technical note or propose a short application section after negotiating with the Paper 60 editor.

My repeated next-turn suggestions kept expanding the research tree. They produced useful material, but several turns introduced a new model rather than closing the preceding model. We should now favor consolidation and falsification over another attractive extension.

## 2. What is newsworthy, and for whom?

| Assessment | Present position |
|---|---|
| Useful to the FEP community | Yes: an operational way to distinguish access to evidence, storage of evidence, and quality of a declared posterior representation. |
| A new general FEP principle | No established claim. The relevant identities and much of the mathematical machinery are standard. |
| A counterexample to all FEP formulations | No. A passive coordinate failing a particular inference task does not refute an existence-based interpretation with a different model, task, or encoding. |
| A viable specialist theory paper | Plausible, conditional on a clear theorem beyond restating data processing and on reproducible results. |
| Broad scientific-communications potential | Not yet demonstrated. Needs a discriminating physical result, a clear advance over sensory-capacity/control literature, and preferably a realizable test. |
| Ready for submission | No. The exploratory observer calculations mostly remain in chat, and the scope and novelty audit need consolidation. |

The most defensible public-facing sentence is:

> A thermal boundary can supply evidence that a physical observer fails to preserve; within a specified model, powered dynamics improve the observer's usable record without increasing the evidence available in the complete boundary history.

This is a model-specific claim about an initial hidden preparation. It must not become “action cannot improve knowledge,” “all agents face a 25% ceiling,” or “the FEP is thermodynamically impossible.”

The potential scientific hook is an **operational completion** of an inference interpretation: specify the task, the accessible record, the physical internal state, its noise, and the decoder before assessing whether the system performs inference. The general demand for operational clarity is not itself novel; the paper must supply a quantitative result that makes it useful.

## 3. Recommended paper angle and title

**Working title:** *From Boundary Evidence to Physical Inference in Thermal Gaussian Networks*.

**Alternative if a constrained-observer theorem becomes the central result:** *Physical Memory Limits Inference from Thermal Boundary Records*.

Do not lead with “a new Free Energy Principle,” “beyond the FEP,” or a universal energy price of knowledge. Avoid making the quarter-transfer bound the title: its mathematical basis is classical and its scope is narrow.

**Central question:** Given a fixed hidden-preparation experiment, how do physical memory and a declared posterior encoding limit the inference achievable from a boundary record?

**Candidate contribution:** A single model and theorem relating the ideal boundary channel to a realizable internal memory, with explicit conditions for information sufficiency, an acquisition/retention limitation, and a controlled comparison of passive and powered dynamics.

The exact rotational work frontier can be a supporting benchmark or appendix. It should not silently replace the original acquisition problem: it begins with an input register already present.

## 4. Relationship to the existing project

The current [Paper 60](C:/Projects/simplicial/60_boundary_consistency_of_thermal_gaussian_networks.md), inspected on October 10, is titled *What a Boundary Can Know*. Its current text includes general friction/inertial models, a private-bath criterion, impedance/canonical-correlation identification, and physical compression, beyond the earlier version discussed in this chat. Those additions were inspected for scope, not independently re-audited here.

Consequently, a companion paper cannot claim “the boundary has an information ceiling” as its standalone contribution. That belongs to Paper 60. The proposed companion begins at the next question: what a physical observer does with the available evidence.

| Paper 60 | Proposed companion |
|---|---|
| Boundary reduction, response, induced noise, thermal reference | Realizable internal sensing and memory |
| Hidden preparation to complete boundary record | Complete record to current internal state and declared estimate |
| Visibility spectrum and admissible feedback invariance | Sufficiency, retention, and constrained implementation |
| Prospective thermal-circuit visibility test | A matched observer comparison, if it adds a distinct measurement |

Also present are an older [imported FEP draft](C:/Projects/simplicial/references/FEP_Paper_Full_Draft.md) and an [FEP-3 audit note](C:/Projects/simplicial/empirical/reports/audit_fep3_settlement.md). Their arithmetic/conductor and sector interpretations are a separate line. Do not import their novelty claims or proof-status labels into this Gaussian argument without a separate audit.

## 5. Claim ledger

“Derived” below means an argument was given in the conversation, not that an external referee has certified it. Numerical results are author computations, not experiments.

| Result | Evidence/status | Role in a paper |
|---|---|---|
| Conditional preparation KL equals a variational gap for the chosen Gibbs model; multiplying by temperature gives conditional physical free-energy excess | Exact standard identity under the stated identification | Bridge and notation, not main novelty |
| Full-record visibility and boundary-feedback invariance | Existing Paper 60 result; known SDPI/filtering/feedback ingredients | Cited foundation |
| Gaussian graph separator gives a static thermal Markov blanket | Standard precision-matrix characterization | Model definition |
| Exact posterior uncertainty can remain when approximation error vanishes | Standard Bayesian conditioning plus the visibility channel | Clarifies the scientific question |
| A passive three-coordinate network acquires then forgets initial-preparation information | Exact matrix-exponential formula; numerical witness | Minimal example |
| Reversible instantaneous transfer has visibility at most one quarter for initially independent normalized linear coordinates | Derived corollary of a classical spectral-spread estimate | Scoped supporting proposition; no new-inequality claim |
| Mobility switching improves deadline retention in the selected budgeted family | Exact covariance calculation; best-found numerical designs | Illustration of kinetic control, not a universal energetic advantage |
| Boundary-only nonconservative forces improve internal visibility while preserving the ideal hidden port experiment | Exact channel/covariance formulas; best-found numerical designs | Strongest current candidate comparison |
| Work/rate frontier for two rotating Gaussian registers | Analytic attainable optimum over deterministic rotation schedules and duration; numerical cross-checks | Restricted transfer theorem; priority audit incomplete |
| Optimal total allocation between acquisition and storage | Not derived | Optional next gap, only after a physically closed model is fixed |
| A full autonomous implementation of Bayesian/FEP inference | Not established by assigning a posterior map to a coordinate | Must not be claimed |

## 6. Corrections and scope boundaries to preserve

1. **The task changed during exploration.** The first example fixed the initial boundary and memory; later examples used a stationary thermal ensemble and targeted a conditional hidden residual. Keep those preparations separate. Comparing raw numbers across them is invalid without matching the experiment.
2. **A calibrated posterior map is not a proof of inference dynamics.** Every joint distribution defines a conditional law. Calling that law a belief does not demonstrate a physical implementation, a gradient flow, or task success. Predeclare the encoding, available inputs, and loss.
3. **Static blankets need verification in every comparison.** The passive reference has a Gaussian blanket. Adding nonconservative forces generally changes transient and stationary covariances; preservation of the same blanket has not been proved for the optimized active three-coordinate designs. The separate two-register rotation keeps its marginal density fixed but is not the same three-part blanket experiment.
4. **Modern FEP includes dynamics and probability currents.** Equal one-time densities with different information transfer show that a density alone is insufficient. They do not by themselves contradict a path-based FEP formulation.
5. **Initial preparation is not ongoing environmental tracking.** Results about remembering the initial hidden residual need not apply to learning a continuously refreshed signal, unknown parameters, or policy-dependent sensing geometry.
6. **Known additive boundary feedback is a restricted intervention class.** It does not cover every epistemic action. An instantaneous internal memory can improve even when the complete-record experiment is invariant.
7. **The quarter bound is not a universal memory ceiling.** It assumes stationary reversible overdamped Gaussian dynamics, initially independent linear signal/readout coordinates, and an instantaneous readout. It does not cover histories, inertia, time-switched dynamics, or nonreversible circulation.
8. **Mobility control has an unmodeled controller.** Changing mobility has no direct Hamiltonian work term in the adopted coarse-grained SDE. That does not establish zero cost for a physical switch or clock. Switched protocols are not autonomous constant-parameter devices.
9. **Work budgets were reference-averaged.** They are not worst-case budgets over arbitrary non-Gaussian preparations. The arbitrary-preparation KL contraction and the reference-ensemble work formula have different quantifiers.
10. **KL slack is not automatically heat.** Identify heat or entropy production only when the Hamiltonian, forces, baths, and preparation protocol justify it.
11. **Variational and predictive KL directions differ.** FEP uses a reverse posterior KL in its usual variational identity; expected excess logarithmic prediction loss uses a forward posterior KL. Do not interchange them.
12. **Optimization is not experimental validation.** Repeated global-search heuristics plus local polishing do not certify a global optimum. A later independently checked ODE confirms the value of a candidate, not its optimality.
13. **There is a model transition at the rotational frontier.** Its input register is already available. Its attainable frontier does not certify the original network's acquisition frontier or its full lifecycle cost.

## 7. The mathematical spine to freeze before further expansion

Use one hidden target U, one accessible complete record R, one physical memory M, and one predeclared decoder. Establish U -> R -> M, including any initial memory state and private randomization needed for that statement.

For a scalar Gaussian reference, normalize Var(U)=1. Let pi_R and pi_M denote the variance reductions from the complete record and physical memory. Then an estimator uhat(M) obeys the orthogonal-projection identity

    E[(U - uhat(M))^2]
      = (1 - pi_R)
        + (pi_R - pi_M)
        + E[(E[U|M] - uhat(M))^2].

The terms are respectively the ideal-record uncertainty, the loss from compressing the record into physical memory, and decoder excess error. This identity is standard; its role is to prevent three distinct limitations from being conflated.

For a declared conditional density q(U|M), under the needed integrability assumptions,

    E[-log q(U|M)] - H(U|R)
      = I(U;R|M)
        + E_M D(p(U|M) || q(U|M)).

This is a predictive-log-loss identity, not the usual reverse-KL variational-free-energy decomposition. If the paper uses both objectives, name and evaluate both.

The necessary nontrivial addition is a physical characterization or bound on pi_M under explicit acquisition, retention, and actuation constraints. The identities alone are not enough for a distinct paper.

**Preferred closure:** One fixed-port observer theorem, plus an attainable example, that quantifies the gap between complete-record inference and a finite noisy memory at a specified deadline. Connect the theorem to a declared posterior representation without a post hoc change of target or generative model.

**Fallback:** A focused technical note on the exact rotational work/rate frontier, with physical information-transfer interpretation and careful provenance. Do not market this fallback as an end-to-end FEP result.

## 8. Proposed manuscript structure

1. **Question and operational definitions.** State the hidden target, observation history, internal state, decoder, loss, and resource constraints. Explain the FEP relevance in one paragraph.
2. **Physical model and boundary experiment.** Cite the necessary Paper 60 result; do not rederive its entire program. State exactly when the blanket property holds.
3. **From accessible evidence to usable inference.** Give the error decomposition and the new physical-memory result. Separate standard identities from the contribution.
4. **One matched comparison.** Same target, preparation, baths, hidden channel, and deadline; compare passive, kinetically switched, and powered observers only under explicitly listed resources.
5. **Thermodynamic accounting and restricted attainable benchmark.** Count mechanical work, remaining free energy, and dissipation; state excluded controller/initialization costs. Put the rotation frontier here only if it supports the central question.
6. **Implications and limitations.** Explain what is added to an FEP interpretation; distinguish a boundary, a record, a sufficient internal statistic, and a physically implemented inference mechanism.

Appendices: standard Gaussian calculations; reversible-transfer corollary; numerical methods; expanded work-frontier derivation if it would interrupt the main narrative.

**Three figures are enough initially:**

- A physical network and its statistical chain U -> R -> M -> declared estimate, labeling what each arrow assumes.
- Visibility versus time for matched observers, with the same complete-record ceiling.
- A work/rate/retention tradeoff with analytic boundaries clearly separated from numerical candidate points.

Do not create a sprawling survey of FEP, consciousness, arithmetic blankets, quantum recovery, and thermal circuits in this manuscript. Those connections can be discussed later if the central result earns them.

## 9. Bounded execution plan and decision gates

| Stage | Concrete deliverable | Pass condition / stop rule |
|---|---|---|
| A. Preserve the evidence | A standalone derivation note and saved reproducibility scripts for the chat calculations, with initializations, units, seeds, candidate parameters, and work definitions | Values reproduce; no numerical optimum is relabeled as a theorem. Do this before extending the model. |
| B. Freeze the claim | A one-page theorem statement, assumptions, comparison class, and nearest-prior-work table | A reviewer can identify the contribution without the phrase “new FEP.” If not, choose the technical-note fallback. |
| C. Close one physical gap | A single acquisition-to-memory model with explicit port, initialization, decoder, deadline, and resources | No ideal writer hidden in an end-to-end claim; blanket conditions checked when invoked. Limit exploration to two planned attempts, then draft the weaker valid result if necessary. |
| D. Draft the minimum paper | Introduction, model, theorem/proof, one comparison, limitations; placeholders only for genuinely missing figures | The central claim is readable and supported. Stop adding examples that do not change it. |
| E. Seek adversarial comparison | Review from control/information theory and FEP/statistical physics perspectives, arranged only when authorized | Resolve novelty and scope objections before venue selection or a broad headline. |

Stage A is the recommended next work. It is evidence preservation, not another speculative research branch. Drafting a new manuscript or editing Paper 60 remains a later decision; this plan itself does not authorize those changes.

### When the proposed acquisition/storage allocation calculation is worth doing

Proceed only if it closes Stage C. Define W_acq, W_transfer, W_hold, and W_reset, plus the finite-time and hardware constraints. Do not optimize an expression such as pi_acq(W_acq) Phi(W_transfer/T,R) until the same physical model justifies both factors, their independence, and the allocation constraint.

The most valuable possible outcome is a demonstrable change of optimal architecture or budget allocation with retention deadline. A generic statement that resources trade off is insufficient.

### Publication decision

- **Companion theory paper:** choose this if the physical-memory result is distinct from Paper 60 and from sensory-capacity/nonreciprocal-sensing results.
- **Short technical note:** choose this if the strongest self-contained result is the restricted attainable work frontier.
- **Application in Paper 60:** propose this only after peer coordination if no independent theorem survives the audit.
- **Broad-interest submission:** consider only after a strong distinguishing theorem or credible physical validation exists. Do not infer likely acceptance from topical relevance to FEP.

## 10. Numerical and analytic record from the conversation

These numbers are preserved for recovery, not promoted to a release-quality certificate. Scripts were executed inline during the chat; this document is not their replacement.

### Passive autonomous baseline

    K = [[3,4,0],[4,7,1],[0,1,1]],  Sigma_0 = T K^{-1}
    u = sqrt(3/T) (e_0 + 4 b_0/3)
    pi_i(t) = [exp(-Kt)_{ie}]^2 / [3 (K^{-1})_{ii}]

Peak: t approximately 1.95670415, pi_i approximately 0.00778725293. The complete-record ceiling is 0.25. The covariance ODE agreed with the stationary covariance to about 5e-11 in a recorded check.

### Numerical constrained designs

Budget: a+d=8, K >= 0.1 I, fixed hidden c=3 and coupling 4; memory mobility in [0.01,1]. Peak searches used the stated acquisition windows; retention readout is at t=10. Gating means a prescheduled mobility switch, not a constant autonomous mechanism.

| Comparison | Visibility |
|---|---:|
| Best-found fixed passive peak | 0.00925008774 |
| Best-found constant passive at t=10 | 0.00197790652 |
| Passive with mobility switching at t=10 | 0.00861339958 |
| Active acquisition peak, W/T <= 1 | 0.01842812626 |
| Active acquisition peak, W/T <= 10 | 0.04822544982 |
| Active acquisition plus gating, W/T <= 1, read t=10 | 0.01656870865 |
| Active acquisition plus gating, W/T <= 10, read t=10 | 0.04090894782 |

Active force: -Nq with N_bi=omega, N_ib=-omega, other entries zero; |omega|<=4; acquisition duration <=3. Initial covariance T K^{-1}; covariance subsequently evolves and is not assumed to remain thermal. Active work is the reference-ensemble mean integral of tr[N^T(K+N) Sigma_t].

Candidate tuples (d,h,omega,acquisition_duration), with a=8-d:

    peak, W/T=1:  (1.4206816623, 0.6912585214, -0.8580760009, 1.1281969373)
    peak, W/T=10: (0.8742097892, 0.2257380616, -3.9445793054, 0.5793468395)
    gate, W/T=1:  (1.3691618907, 0.7569035493, -0.8296361053, 1.1765367761)
    gate, W/T=10: (0.8431250914, 0.3282385339, -3.8111247091, 0.6087800734)

After acquisition, the gated cases remove N and use memory mobility 0.01 until t=10. Independent covariance/mean/work ODE integration reproduced the candidate values. Work has not been bounded uniformly over all input preparations.

### Exact restricted transfer frontier

For normalized registers initially N(0,I), dynamics dX=-(alpha I+omega(t)J)X dt+sqrt(2alpha)dW, J=[[0,-1],[1,0]], and deterministic controls:

    pi_transfer = exp(-2 alpha t_f) sin^2(theta)
    theta = integral omega(t) dt
    W/T = (2/alpha) integral omega(t)^2 dt

For E=W_max/T>0 and R=omega_max/alpha>0,

    Phi(E,R) = max_{0<=theta<=pi/2}
      sin^2(theta) exp[-2 max(2 theta^2/E, theta/R)].

Constant-rate rotation attains the bound. The proof combines Cauchy-Schwarz, the drive-rate cap, and the exact propagator. It allows free choice of predetermined duration; a fixed deadline, feedback stopping, additional controls, or a different covariance changes the problem.

When the rate cap is inactive, E=4 theta tan(theta), and Phi=exp[-theta cot(theta)] sin^2(theta). At R=4, Phi(1,4)=0.08484435006, Phi(5,4)=0.32169223042, Phi(10,4)=0.48204135231, and the large-budget ceiling is 0.48503537447. Crossing 0.25 requires E>3.538842106 in this family. These are transfer fractions, not the original network's end-to-end visibility.

If a physically justified input register has visibility pi_in and the fresh output register/private noises are independent, the Gaussian cascade gives pi_out <= pi_in Phi(E,R). The transfer theorem does not provide pi_in or its acquisition cost. Its work formula uses the standard Gaussian reference; arbitrary-preparation SDPI does not automatically extend that work budget to every prior.

## 11. Nearest literature and how it changes the claim

This is a focused positioning audit, not proof of historical priority or an exhaustive review. Some sources were inspected through primary abstracts and indexed text rather than a complete technical rederivation.

| Source | Relevance and constraint on our positioning |
|---|---|
| Friston et al., [The free energy principle made simpler but not too simple](https://arxiv.org/abs/2201.06387) | Modern FEP includes partitions, dynamical paths, and Bayesian interpretations. Do not reduce it to static Gibbs minimization. |
| Aguilera et al., [How particular is the physics of the free energy principle?](https://arxiv.org/abs/2105.11203) | Linear stochastic counterexamples and inferential-interpretation concerns already exist. “A blanket alone is insufficient” is not an untouched discovery. |
| Heins and Da Costa, [Sparse coupling and Markov blankets](https://arxiv.org/abs/2205.10190) | Conditions connecting Gaussian dynamics and blankets need explicit verification; include the response side of the debate. |
| Hartich, Barato and Seifert, [Sensory capacity](https://arxiv.org/abs/1509.02111) | Current-state versus history information, physical memory, and efficiency tradeoffs are direct antecedents. Our target and contraction measure must be distinguished. |
| Harris et al., [Minimum requirements for feedback enhanced force sensing](https://arxiv.org/abs/1303.1589) | Complete-record feedback equivalence is established. Our physical-memory use is an application, not the discovery of feedback neutrality. |
| Dechant and Lutz, [Fundamental limits on nonequilibrium sensing](https://arxiv.org/abs/2407.17831), [published version](https://doi.org/10.1038/s41467-025-65058-7) | Nonreciprocal sensing improvements under dissipation constraints already exist. Initial-preparation KL, fixed hidden channels, finite deadlines, and the resource restrictions are the possible distinctions. |
| Bhatia and Sharma, [Positive linear maps and spreads of matrices-II](https://doi.org/10.1016/j.laa.2014.10.030) | Classical spectral-spread machinery underlies the quarter-transfer corollary. |
| Landi, Tome and de Oliveira, [Entropy production in linear Langevin systems](https://arxiv.org/abs/1507.00232) | Standard Gaussian thermodynamic work and entropy-production framework. |
| Sagawa and Ueda, [Minimal energy cost for thermodynamic information processing](https://arxiv.org/abs/0809.4098) | Measurement, memory, and erasure need protocol-specific accounting. Avoid universal prices inferred from one actuator. |
| Polyanskiy and Wu, [Strong data-processing inequalities](https://arxiv.org/abs/1508.06025) | Contraction machinery is standard; physical identification and attainable constrained realization must carry the contribution. |

The existing [Paper 60 novelty audit](C:/Projects/simplicial/60_visibility_literature_audit.md) additionally covers spatial Gramians, stochastic observability, and thermal-circuit precedents. Reuse its caution rather than reopening those claims as new discoveries.

## 12. Recommended next session

**Do not begin with another generalization.** Begin by turning the current observer results into a reproducible, reviewer-readable standalone note and a one-page claim contract. Preserve existing papers.

Suggested next-turn request:

> Consolidate the Gaussian observer exploration into a standalone derivation note and reproducibility package. Reproduce the passive, gated, active, and rotation-frontier results; label each assumption, prior, work definition, and numerical limitation. End with one proposed main theorem, its nearest prior result, and the single missing result needed for a distinct companion paper. Do not edit existing papers or add a new model unless needed to correct an identified error.

After that deliverable, decide between the companion paper, the restricted technical note, and a negotiated application in Paper 60. The aim is a clear scientific claim with durable evidence, not an indefinitely expanding sequence of promising next turns.
