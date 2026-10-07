# B10 - Current Falsifier Polymath

**Continuous Temporal Flow, Discrete Admission, and the Failure of a Pure Current Bucket**

**Leonardo Murillo Montero**

**Draft 1**

---

> *The current variable survives the falsifier. The pure current bucket does
> not. The better hypothesis is governed flow: a continuous temporal current
> with a lawful admission gate.*

---

## Status

This note records the first deliberately adversarial B-series result after B8.
It should be read as a correction to the early bucket story, not as a
confirmation exercise.

B8 found:

\[
\boxed{
\text{RIVAL\_MATCH\_BUCKET\_NOT\_UNIQUE.}
}
\]

B9 therefore required the B-series to test route variables against continuous
precision-active and solenoidal rivals. B10 instantiates that requirement for
the current bucket.

The empirical companion is:

`empirical/b10_current_falsifier_polymath_probe.py`

with reports:

- `empirical/reports/b10_current_falsifier_polymath_probe.md`
- `empirical/reports/b10_current_falsifier_polymath_probe.json`

---

## Abstract

**Situation.** B1 and B2 proposed that prediction errors are routed into
operation-specific buckets. B3 supported a current bucket by showing that scalar
surprise and symmetric transition evidence are blind to time reversal, while a
signed antisymmetric current recovers the arrow. B8 then showed that bucket
language may be an operational discretization of a continuous precision/cost
control problem.

**Task.** B10 asks whether the current bucket survives a strong continuous
solenoidal rival. The synthetic generator can produce three worlds:
null worlds with no directional action, continuous-flow worlds where behavior
varies smoothly with signed temporal current, and bucket worlds where a discrete
gate admits or refuses current as an actionable route.

**Action.** We compare scalar, symmetric, continuous-solenoidal,
conformal-bucket, governed-flow-gate, and ungated hybrid models. The continuous
rival receives signed current magnitude and observation precision. The bucket
model receives only a conformal current admission gate and sign. Null worlds
calibrate false current admission.

**Result.** The result is:

\[
\boxed{
\text{FLOW\_FITS\_BUT\_GATE\_GOVERNS\_FALSE\_ADMISSION.}
}
\]

Continuous solenoidal flow predicts directional vigor better than the bucket
gate, with RMSE \(0.378\) versus \(0.467\). But it produces many false actions
on null worlds, \(0.358\) versus \(0.036\) for the conformal gate. The pure
bucket story therefore fails, but the governance story strengthens: brains may
use continuous temporal current as the graded variable and a lawful gate to
decide when that current becomes actionable.

---

## The Falsifier

The early B-series phrasing invited a too-simple reading:

\[
\text{current error} \longrightarrow \text{current bucket} \longrightarrow \text{predict direction}.
\]

B10 tests a sharper rival:

\[
\text{temporal behavior may be continuous solenoidal flow, not a discrete bucket.}
\]

The falsifier is intentionally allowed to weaken the B-series. If the
continuous rival explains held-out behavior and the bucket adds no admission
control, then current should be removed from the bucket table as a distinct
route variable.

The current bucket survives only if it improves both:

1. held-out prediction of directional behavior;
2. false current control on detailed-balance or null worlds.

The empirical result splits those virtues.

---

## Synthetic Worlds

All worlds are ring-transition worlds with matched scalar surprise, matched
symmetric transition backbone, and matched stationary occupancy.

| World | Generator | Behavioral rule |
|---|---|---|
| null world | detailed-balance transition evidence | no directional action |
| continuous world | signed solenoidal current | graded directional vigor |
| bucket world | signed current plus hidden gate | action only after admission |

This makes the test more severe than B3. B3 asked whether signed current exists
after scalar and symmetric evidence fail. B10 asks whether the signed current
should be modeled as a discrete route bucket, a continuous flow variable, or a
governed flow with an admission gate.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | scalar surprise only | blind to direction and source |
| symmetric | scalar plus symmetric transition evidence | blind to current sign |
| continuous solenoidal | signed current, magnitude, precision | over-admits weak/null current |
| bucket current | conformal gate plus sign | loses graded vigor |
| governed flow-gate | gated continuous flow | safer admission, weaker smooth fit |
| hybrid flow-gate | continuous flow plus gate features | can fit but may over-admit |

The continuous rival is strong on purpose. It receives the variable that a
solenoidal/free-energy account would naturally want: signed temporal flow with
precision. The bucket model is not allowed to smuggle in continuous magnitude.
It gets only a calibrated admission event and a sign.

---

## Main Result

Default configuration:

- seed: `20260603`
- route/null trials: `900` / `450`
- main bucket mix: `0.5`
- conformal alpha: `0.05`
- conformal current gate: `0.200`

| Model | RMSE observed | R2 observed | Route accuracy | Null false action |
|---|---|---|---|---|
| scalar | 0.613 | 0.000 | 0.511 | 0.000 |
| symmetric | 0.613 | 0.000 | 0.511 | 0.000 |
| continuous solenoidal | 0.378 | 0.620 | 0.696 | 0.358 |
| bucket current | 0.467 | 0.419 | 0.693 | 0.036 |
| governed flow-gate | 0.467 | 0.419 | 0.693 | 0.036 |
| hybrid flow-gate | 0.377 | 0.621 | 0.699 | 0.349 |

This is the key asymmetry:

\[
\begin{array}{rcl}
\text{continuous flow} &:& \text{better magnitude prediction, worse false admission;}\\
\text{bucket gate} &:& \text{worse magnitude prediction, better false admission.}
\end{array}
\]

The pure current bucket does not win the behavioral prediction problem. The
pure continuous rival does not win the governance problem.

---

## Phase Sweep

The phase sweep varies how often the non-null world is generated by a discrete
bucket gate rather than smooth flow.

| Bucket mix | Winner by RMSE | Continuous RMSE | Bucket RMSE | Governed RMSE | Hybrid RMSE | Bucket null FA |
|---|---|---|---|---|---|---|
| 0.000 | continuous solenoidal | 0.351 | 0.462 | 0.465 | 0.351 | 0.034 |
| 0.250 | hybrid flow-gate | 0.368 | 0.454 | 0.456 | 0.367 | 0.040 |
| 0.500 | continuous solenoidal | 0.365 | 0.468 | 0.467 | 0.365 | 0.026 |
| 0.750 | hybrid flow-gate | 0.373 | 0.420 | 0.418 | 0.367 | 0.046 |
| 1.000 | hybrid flow-gate | 0.354 | 0.381 | 0.366 | 0.346 | 0.060 |

The bucket model never wins the RMSE sweep. This matters. If a model cannot win
even when the generator is entirely bucket-world, the model is too coarse to be
the whole story. The hidden gate is not enough; graded current magnitude still
matters.

But the null false-admission column points the other way. The continuous and
ungated hybrid models fit vigor while hallucinating current on null worlds.
The conformal gate is doing real work.

---

## Interpretation

B10 changes the B-series claim.

The earlier claim was:

\[
\boxed{
\text{current error is one prediction-error bucket.}
}
\]

The updated claim is:

\[
\boxed{
\text{current is a continuous temporal-flow variable under governed admission.}
}
\]

In words: the current bucket is probably not the neural variable. The neural
variable is closer to signed temporal flow, sequence drift, or solenoidal
transition structure. The bucket is the governance decision that says when that
flow should be trusted as actionable rather than treated as null fluctuation.

This is a better brain hypothesis. It lets hippocampal sequence dynamics,
cortico-striatal transition coding, and active-inference flow models keep their
continuous geometry, while preserving the B-series insistence that organisms
must decide when a signal is admitted.

---

## Consequence for the Bucket Table

B10 suggests a general correction:

Prediction-error buckets should not all be treated as primitive neural
variables. Some buckets may be **routes over continuous variables**.

| Earlier bucket phrasing | B10 correction |
|---|---|
| current error | continuous temporal flow plus admission gate |
| chart error | possible continuous geometry plus rechart threshold |
| ambiguity error | continuous posterior set size plus sampling gate |
| ledger error | continuous miscalibration plus reset gate |
| governance error | represented affordance plus inhibition gate |

This preserves the operational value of the bucket table while making it less
metaphysically brittle. The bucket is often the animal's management decision,
not necessarily the substrate variable itself.

---

## Biological Prediction

B10 predicts a dissociation in neural data:

1. graded temporal-current variables should track direction, sequence vigor,
   and transition flow continuously;
2. a slower or more global admission signal should decide when that flow affects
   action, attention, replay, or conscious report;
3. null or detailed-balance regimes should still contain noisy local current
   estimates, but the admission gate should suppress their behavioral uptake.

In a brain, this suggests looking for:

- hippocampal and entorhinal sequence-flow variables;
- cortico-striatal current-to-policy coupling;
- prefrontal, basal-ganglia, or neuromodulatory admission control;
- a dissociation between decoded current magnitude and actual behavioral use.

The decisive experiment is not simply decoding current. It is showing that
decoded current and admitted current come apart.

---

## What Would Falsify This Updated Claim

The governed-flow update would fail if:

1. continuous current magnitude alone predicts both behavior and null refusal;
2. no independent gate or admission variable improves false-current control;
3. perturbing candidate gate circuits changes neither current admission nor
   false-current behavior;
4. route decisions are fully mediated by ordinary precision, value, and policy
   cost variables.

If that happens, B10 collapses into the continuous precision-active rival. The
bucket table remains useful engineering language, but not a distinct brain
architecture.

---

## Current B-Series Update

B1 remains intact at the highest level:

\[
\text{brains manage prediction error under boundary, action, capacity, and governance.}
\]

B2 needs refinement:

\[
\text{some buckets are primitive routes; others are admission decisions over continuous variables.}
\]

B3 remains valuable:

\[
\text{scalar and symmetric evidence miss the temporal arrow.}
\]

B8 and B10 now jointly impose the discipline:

\[
\text{do not infer a discrete bucket when a strong continuous rival can do the work.}
\]

The new B-series slogan should be:

\[
\boxed{
\text{animal brains route continuous evidence through governed admissions.}
}
\]

---

## Next Experimental Target

The next best falsifier is to run the same correction on the **noise versus
structure** bucket. The danger is that "noise", "unexpected uncertainty",
"chart change", and "packet closure" may also be continuous neuromodulatory
precision variables plus admission gates, not discrete buckets. A good B11
should let an ACh/NE-style continuous uncertainty rival beat the bucket table
if it can.

