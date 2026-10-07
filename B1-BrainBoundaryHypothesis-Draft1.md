# B1 - The Brain Boundary Hypothesis

**Reverse Engineering Animal Brains as Governed Active Boundary Systems**

**Leonardo Murillo Montero**

**Draft 1**

---

> *The brain should not be read as a predictor only. It should be read as a boundary-routing organ: a system that decides which prediction errors reweight belief, which reveal a missing structure, which require action, which are only noise, and which must not be admitted.*

---

## Abstract

**Situation.** The T-series developed a finite language of projection,
boundary, closure, active inference, conformal governance, and conscious
admission. T17 decomposed free energy into retained, boundary, noise,
capacity, and governance channels. T18 added finite-sample lawful admission:
a boundary completion should be acted on only when it passes a calibration
ledger. T19 proposed consciousness as governed active boundary completion at a
terminal inner screen. The later Conductor Blind Spot papers add two missing
operator-level axes: **curvature**, where a linear readout misses a nonlinear
slow-feature chart, and **current**, where a symmetric objective erases the
arrow of time.

**Gap.** A theory of animal and human brains needs all of these pieces at
once. Prediction-error theories explain why organisms update. Active inference
explains perception and action as free-energy minimization. Global-workspace
and screen theories locate conscious access. But none of these, by themselves,
give a packet-resolved management rule for prediction error: when should an
error change a belief, grow a representation, trigger an action, open a new
temporal-current channel, be compressed, be ignored, or be blocked?

**Action.** We introduce the **Brain Boundary Hypothesis**. An animal brain is
a nested governed active boundary system. Its retained sectors are slow charts
of organism-environment transitions; its unresolved residuals are candidate
boundary packets; its temporal flow is the antisymmetric current of those
transitions; its attention is precision gain over residual channels; its
learning is lawful boundary closure; its action is external boundary
completion through the body; and its conscious contents are the subset of
boundary packets admitted into terminal inner screens under capacity and
governance.

**Result.** This draft is a hypothesis paper, not a proof. It proposes a
reverse-engineering program for animal brains, including human brains. The
program predicts that prediction errors are not managed by a single scalar
surprise signal. They are sorted into nine operational buckets: retained
error, chart error, packet error, current error, ambiguity error, capacity
error, noise error, governance error, and ledger error. Each bucket implies a
different neural operation and a different experimental signature. The aim of
the B-series is to turn this into a working brain-reverse-engineering stack:
from neural recordings to retained charts, boundary packets, current channels,
admission ledgers, route maps, and conscious screens.

**Top claim.**
\[
\boxed{
\text{the animal brain is governed active boundary inference implemented in tissue.}
}
\]

**Keywords:** brain, animal cognition, human brain, active inference, prediction
error, boundary completion, slow-feature chart, probability current, attention,
precision, conformal governance, consciousness, Markov blanket, reverse
engineering.

---

## Cross-references from prior papers

| Source | Role in B1 |
|---|---|
| T13 Exact Simplicial Renormalization | Closure as finite boundary adjunction |
| T14 Projected Flatness | Curvature as projection-boundary obstruction |
| T15 Finite-to-Archimedean Completion | Open and terminal boundary completion |
| T16 Representation Closure | Attention, memory, tools, alignment as boundary operations |
| T17 Active Boundary Inference | Packet-resolved free energy and prediction-error buckets |
| T18 Conformal Boundary Governance | Calibration ledgers and lawful admission |
| T19 Conscious Boundary Model | Terminal inner screens and conscious packet admission |
| The Conductor Blind Spot | Order-two curvature misses order-three structure |
| Beyond the Conductor Blind Spot | Retained sectors are nonlinear slow-feature charts |
| The Irreversible Blind Spot | Symmetric objectives erase temporal current |
| Curvature and Current | One transition operator, two independent blind spots |

---

## 0. Steelthread

The working claim is:
\[
\boxed{
\text{animal brains manage prediction error by governed boundary routing.}
}
\]

The brain does not merely minimize a scalar error. It decides which kind of
error it is seeing. The same surprise magnitude can mean:

- the current model is right but needs reweighting;
- the retained chart is nonlinear and must be decoded through a warp;
- a missing interaction packet should be learned;
- the direction of time or causal flow has been missed;
- the evidence is ambiguous and should be sampled;
- the structure is real but too expensive to internalize;
- the signal is noise;
- the completion is disallowed;
- the calibration context itself has broken.

These are not synonyms. They are different control outcomes.

---

## 1. Basic Object

At a task scale, model an animal brain as a nested family of active boundary
systems. For one such system at time \(t\), write
\[
\mathcal B_t
=
\left(
R_t,\partial R_t,T_t=S_t+A_t,\Lambda_t,\mathcal L_t,C_\alpha,
\mathcal G_t,\mathcal R_t,K_t
\right).
\]

Here:

| Symbol | Meaning |
|---|---|
| \(R_t\) | retained sector, the variables currently carried by the system |
| \(\partial R_t\) | task-relative boundary, the candidate missing packets |
| \(T_t\) | transition operator over organism-environment or inner states |
| \(S_t=\tfrac12(T_t+T_t^\ast)\) | reversible/symmetric part of the transition |
| \(A_t=\tfrac12(T_t-T_t^\ast)\) | antisymmetric current, the arrow of time |
| \(\Lambda_t\) | precision or attention gain over channels |
| \(\mathcal L_t\) | calibration ledger for admissible updates/actions |
| \(C_\alpha\) | conformal boundary set at error level \(\alpha\) |
| \(\mathcal G_t\) | governance constraints: biological, task, safety, social |
| \(\mathcal R_t\) | route map to action, memory, report, body, tool, or world |
| \(K_t\) | capacity/compression budget |

This is not proposed as a literal anatomical tuple. It is the reverse
engineering target: if a brain system is performing governed active boundary
inference, then these objects should be recoverable, approximately, from
behavior, neural dynamics, perturbation, and task structure.

---

## 2. The Post-CBS Prediction-Error Buckets

The B1 claim begins with the error-management taxonomy. A prediction error
should first be diagnosed by boundary source and then gated by lawful
admission.

| Bucket | Diagnosis | Operation | Brain reading |
|---|---|---|---|
| Retained error | The right variables are already in \(R_t\); weights are wrong | reweight | ordinary belief update |
| Chart error | The variable is present but encoded through a nonlinear slow chart | rechart | nonlinear decoding, remapping, reinterpretation |
| Packet error | A missing packet \(\beta\in\partial R_t\) explains the residual | close | learning, insight, representation growth |
| Current error | The error concerns direction, sequence, causality, or flow | predict | current tracking through asymmetric dynamics |
| Ambiguity error | Multiple packets remain plausible | sample | attention, inspection, intervention, query |
| Capacity error | The packet is real but too costly to retain | compress | summary, habit, external memory, delegation |
| Noise error | No stable held-out boundary gain | suppress | ignore, habituate, damp precision |
| Governance error | The completion is evidenced but disallowed | inhibit | constraint, refusal, affective or social braking |
| Ledger error | The calibration regime itself has shifted | recalibrate | context change, new task cell, surprise about surprise |

T17 supplies the decomposition, T18 supplies the admission gate, and the CBS
papers split two structurally different errors that older T19 could only
gesture toward: **chart error** and **current error**.

---

## 3. Hypothesis 1: The Brain Retains Slow Charts

For a stream of organism-environment states \(z_t\), define a transition
operator
\[
(T\psi)(z)=\mathbb E[\psi(z_{t+1})\mid z_t=z].
\]

The curvature paper says that, under the alignment-and-whitening objective, the
retained representation is the slow-eigenfunction chart of this operator. In a
brain setting, this predicts:

\[
\boxed{
R_t \simeq \operatorname{span}\Phi_1,
}
\]

where \(\Phi_1\) contains the slowest nontrivial eigenfunctions relevant to the
organism's task scale.

Interpretation:

- perception should preserve slowly varying causes rather than raw sensory
  coordinates;
- linear decodability is not the criterion for representation;
- non-Gaussian latent causes should be recoverable through nonlinear charts;
- the apparent "hiddenness" of a variable may be a chart mismatch rather than
  absence.

**Brain prediction.** In neural data, nonlinear slow-feature probes should
recover task variables that linear decoders miss, especially in intermediate
integration regions rather than earliest sensory or final motor layers.

---

## 4. Hypothesis 2: The Brain Tracks Current, Not Only State

The irreversible blind spot says that a symmetric single-encoder objective
depends only on \(S=\tfrac12(T+T^\ast)\). It erases \(A=\tfrac12(T-T^\ast)\),
the probability current and arrow of time.

For brains this matters because animals live in irreversible worlds:

- motion has direction;
- action has consequence;
- hunger, fatigue, threat, and reward evolve;
- speech, song, grooming, play, pursuit, and social turn-taking are ordered;
- the same state means different things depending on whether it is being
  approached or left.

So the brain hypothesis is:
\[
\boxed{
\text{directed cognition requires an explicit current channel }A_t.
}
\]

This channel may be implemented by recurrence, predictive coding,
efference copy, phase dynamics, asymmetric synaptic routing, hippocampal
sequence replay, cerebellar forward modeling, basal ganglia action gating, or
other biological mechanisms. B1 does not identify one anatomy as the unique
substrate. It claims that any adequate reverse engineering must audit the
antisymmetric part of the transition.

**Brain prediction.** Analyses based only on static similarity, symmetric
covariance, or representational geometry will miss part of temporal cognition.
Predictor blocks, cross-lagged operators, left/right singular charts, and
time-reversal tests should reveal current-like signals.

---

## 5. Hypothesis 3: Attention Is Gain Over Buckets

T17 reads precision as boundary gain. B1 imports that reading:
\[
\|r_t\|_{\Lambda_t}^2
=
\sum_\gamma \lambda_{\gamma,t}\|\Pi_\gamma r_t\|^2
+\text{cross terms}.
\]

Attention is therefore not a flashlight and not a consciousness variable by
itself. It is a gain policy over prediction-error channels.

In B1:

- increasing retained-channel gain supports ordinary inference;
- increasing boundary-packet gain supports learning or insight;
- increasing current-channel gain supports temporal and causal tracking;
- increasing ambiguity gain supports sampling and orienting;
- decreasing gain suppresses noise or irrelevant variation.

**Brain prediction.** Attention should dissociate from raw surprise. Under
matched scalar surprise, attention should track held-out boundary gain and
current relevance better than error magnitude.

---

## 6. Hypothesis 4: Consciousness Is Terminal Admission, Not All Processing

T19 proposed:
\[
\mathfrak C_t
:=
\operatorname{Adm}_{\alpha,\mathcal G,K}
\left(
S_{\star,t},
\partial S_{\star,t},
r_t,
\Lambda_t,
Z_t
\right).
\]

B1 keeps this but upgrades the substrate:

\[
\boxed{
\mathfrak C_t
\text{ is governed admission into a terminal inner screen whose retained sector is a slow chart and whose temporal flow is current-bearing.}
}
\]

Conscious content is not every represented variable. It is the subset of
boundary or retained packets that:

1. have enough gain;
2. have enough evidence;
3. fit capacity;
4. have an action, report, memory, or control route;
5. pass governance;
6. enter a terminal inner screen.

Automatic skill then has a clean explanation. A packet that was once conscious
can become transparent after repeated lawful admission: it descends into the
retained chart. Consciousness tracks the moving boundary between not-yet-learned
and already-transparent.

**Brain prediction.** Practice should move neural content from high boundary
gain and conscious reportability toward lower-gain retained-chart dynamics,
while preserving behavioral control.

---

## 7. Hypothesis 5: Governance Is Biological, Social, and Statistical

T18 says that boundary completion should be lawful:
\[
h\in C_\alpha(Z),
\qquad
h\in\operatorname{Allow}_{\mathcal G}.
\]

For brains, governance is not only ethics. It includes every constraint that
limits admission:

- biological viability;
- pain, fatigue, hunger, threat, immune state;
- social norms and attachment structure;
- learned taboos and affordance boundaries;
- task rules;
- memory consistency;
- motor feasibility;
- organism-level risk.

T18 adds a special bucket: **ledger error**. Sometimes the animal does not only
experience a surprising object. It experiences a breakdown of the context in
which surprise was being judged.

Examples:

- a familiar place becomes dangerous;
- a trusted conspecific becomes unreliable;
- a body state changes under illness or intoxication;
- a cue that used to predict reward no longer does;
- a social rule has shifted.

In B1 language, these are not merely high surprise. They are calibration-cell
failures.

**Brain prediction.** Context-shift signals should look different from ordinary
object-level prediction errors. They should trigger ledger rebuilding: renewed
sampling, cautious action, exploration, social checking, or new rule formation.

---

## 8. Reverse-Engineering Protocol

The B-series aims to reverse engineer animal brains by reconstructing the
objects of \(\mathcal B_t\).

### Step 1. Declare the organism-task scale

Choose a behavior, environment, timescale, and state description. Do not begin
with "the whole brain." Begin with a boundary: prey capture, navigation,
grooming, song, threat response, tool use, social turn-taking, working memory,
dreaming, or report.

### Step 2. Identify the active Markov blanket

Separate sensory channels, active channels, internal states, and external
states. In animals this means including body loops: eyes, whiskers, vestibular
flow, proprioception, gut state, motor efference, vocal tract, limbs, and social
signals.

### Step 3. Estimate the transition operator

From neural and behavioral trajectories, estimate a task-relative transition
operator \(T_t\). Then split:
\[
T_t=S_t+A_t.
\]

The symmetric part gives reversible slow structure. The antisymmetric part
gives current, sequence, and temporal direction.

### Step 4. Recover the retained slow chart

Compute or approximate the leading slow features of \(S_t\) or the relevant
singular charts of \(T_t\). Test whether linear decoding is complete or whether
a nonlinear chart is required.

### Step 5. Search for boundary packets

Project residuals onto candidate packet dictionaries:

- interaction terms;
- phase and cycle packets;
- body-world couplings;
- social role packets;
- temporal-current packets;
- hidden task rules;
- cross-modal bindings.

Use held-out gain, not raw surprise, as the primary score.

### Step 6. Build calibration ledgers

For each packet/channel/task cell, build T18-style ledgers. Ask:

- is this score exchangeable in this cell?
- does the conformal update gate open?
- is the boundary set singleton, multivalued, null, or incompatible?
- has the ledger itself broken?

### Step 7. Map routes

For admitted packets, identify the route:

- belief reweighting;
- learning/closure;
- attention/sampling;
- action;
- memory stabilization;
- compression;
- suppression;
- governance/inhibition;
- report or communication.

### Step 8. Perturb and falsify

A reverse-engineered bucket should predict what happens under perturbation:
lesion, stimulation, task shift, sensory conflict, reversal, practice, sleep,
pharmacology, or social manipulation.

---

## 9. First Falsifiers

B1 should fail if these signatures do not appear.

1. **Matched-surprise failure.** If scalar surprise always predicts belief
   update, attention, learning, and conscious report as well as boundary gain,
   then T17-style decomposition adds little.

2. **No chart gap.** If nonlinear slow-feature probes never recover behaviorally
   relevant variables missed by linear probes, then the curvature axis is not
   doing brain work.

3. **No current gap.** If time reversal, cross-lagged predictors, or left/right
   singular charts reveal no missing directed structure beyond symmetric
   geometry, then the current axis is not doing brain work.

4. **No ledger behavior.** If context shifts do not produce separate
   recalibration dynamics from ordinary object-level errors, then T18 is not
   brain-relevant.

5. **No automaticity flux.** If learned skills do not move from conscious
   boundary admission into transparent retained dynamics, then the T19 flux
   claim is wrong.

6. **No bucket-specific perturbation.** If perturbing the same scalar error
   magnitude produces no dissociation among reweighting, learning, action,
   suppression, inhibition, and recalibration, then the bucket taxonomy is too
   fine.

---

## 10. Anatomical Working Map

This section is deliberately provisional. B1 does not identify exact brain
regions with exact mathematical objects. It proposes search targets.

| Mathematical role | Possible biological search target |
|---|---|
| sensory boundary | sensory epithelia, thalamic relays, early sensory cortex |
| retained slow chart | cortical and subcortical population manifolds |
| boundary packet residuals | prediction-error channels and mismatch responses |
| precision gain | thalamocortical gain, neuromodulation, attention control |
| current channel | recurrence, hippocampal sequences, cerebellar prediction, motor efference |
| calibration ledger | context memory, hippocampal-prefrontal state cells, task sets |
| governance | basal ganglia gating, prefrontal constraints, affective and social control |
| capacity/compression | working memory limits, habit formation, chunking |
| conscious terminal screen | nested thalamocortical or frontoparietal inner interfaces |
| external completion | body action, social communication, environmental scaffolds |

This table is a hypothesis map, not an anatomical doctrine.

---

## 11. Animal Gradient

The B-series should not start with humans only. Animal brains let us separate
the architecture.

Minimal mobile animals need:

- a sensory boundary;
- an active boundary;
- retained slow variables;
- current tracking;
- action routing.

Animals with richer learning need:

- packet closure;
- memory stabilization;
- capacity management;
- context ledgers.

Social animals need:

- governance;
- shared ledgers;
- role packets;
- turn-taking current;
- communicative boundary routes.

Humans add a large terminal-screen and symbolic/external completion stack:
language, tools, writing, institutions, explicit report, deliberate refusal,
and long-range self-modeling. On this view, the human brain is not a wholly
different kind of system. It is an extreme case of governed active boundary
inference with unusually powerful external completion routes.

---

## 12. Empirical Program

### B1-E1. Matched Surprise in Animals

Construct two conditions with matched scalar prediction error:

- noise perturbation;
- hidden structural packet.

Prediction: attention, learning, and policy change should track boundary gain,
not scalar surprise.

### B1-E2. Time-Reversal Task

Train or observe animals in tasks where forward and reversed sequences have
matched symmetric similarity but different causal direction.

Prediction: predictor/current measures should separate the conditions better
than symmetric representational similarity.

### B1-E3. Nonlinear Chart Probe

Record neural population states in a task with known nonlinear latent variables.

Prediction: slow-feature or diffusion-map coordinates should recover latent
state and planning variables missed by linear probes.

### B1-E4. Ledger Break Task

Change a task regime after calibration: cue validity, social rule, reward
mapping, or body-state contingency.

Prediction: the brain should show context-rebuilding dynamics distinct from
ordinary error correction.

### B1-E5. Automaticity Flux

Track a skill from novice to expert.

Prediction: early learning shows conscious/boundary gain and explicit report;
late performance shifts toward retained-chart control with reduced reportable
packet structure.

### B1-E6. Conscious Admission Under Matched Surprise

In humans, create matched-surprise events where only one has stable boundary
gain.

Prediction: report, memory, and conscious access should follow lawful boundary
gain rather than raw surprise.

---

## 13. B-Series Roadmap

| Paper | Working role |
|---|---|
| B1 | Brain Boundary Hypothesis: full program statement |
| B2 | Prediction-Error Buckets in Neural Systems |
| B3 | Current, Sequence, and the Arrow of Animal Time |
| B4 | Nonlinear Slow Charts in Perception and Navigation |
| B5 | Attention as Boundary Gain |
| B6 | Conformal Ledgers, Context Shift, and Recalibration |
| B7 | Conscious Screens and Automaticity Flux |
| B8 | Social Brains as Shared Boundary Governance |
| B9 | Human Symbolic Completion: Language, Tools, Institutions |

The numbering is provisional. The important move is that the B-series is not
another metaphor for the brain. It is an engineering program: identify the
boundary objects, estimate the operators, split curvature from current, build
ledgers, and test the routing.

---

## 14. Limitations

1. **This is not a proof about biological brains.** It is a reverse-engineering
   hypothesis using mathematical objects already developed elsewhere in the
   program.

2. **The mapping to anatomy is open.** B1 predicts roles, not one-to-one region
   labels.

3. **Conformal validity needs calibration cells.** Biological brains may
   approximate ledgers through context memory, but this is an empirical claim.

4. **Packet dictionaries are hard.** The hardest practical step is discovering
   the right candidate boundary packets in natural behavior.

5. **Current is not optional.** Any brain theory that treats cognition as static
   representation geometry risks erasing temporal direction.

6. **Consciousness is not the whole brain.** T19-style terminal screens are one
   special layer of the architecture, not all cognition.

7. **Human interpretation requires care.** The program should begin with
   controlled animal and artificial-agent tests before claiming broad human
   conclusions.

---

## 15. Closing

The T-series gave a finite calculus of boundary and closure. T17 made boundary
active. T18 made it lawful. T19 made conscious admission a terminal-screen
event. The Conductor Blind Spot papers then sharpened the substrate: retained
representations are nonlinear slow charts, and temporal cognition requires
current.

B1 says that this is enough to begin a brain program.

\[
\boxed{
\text{To reverse engineer an animal brain, recover how it routes prediction error.}
}
\]

The animal brain is not merely surprised. It sorts surprise. It reweights what
is already known, grows what is missing, samples what is ambiguous, predicts
what flows, compresses what is too costly, suppresses what is noise, blocks what
is disallowed, and rebuilds its ledgers when the world changes.

That routing is the object.

---

## Local References

1. `T17-ActiveBoundaryInference-Draft1.md`.
2. `T18-ConformalBoundaryGovernance-Draft1.md`.
3. `T19-ConsciousBoundaryModel-Draft1.md`.
4. `ConductorBlindSpot.md`.
5. `BeyondTheConductorBlindSpot.md`.
6. `IrreversibleBlindSpot.md`.
7. `CurvatureAndCurrent.md`.
