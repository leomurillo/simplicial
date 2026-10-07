# E12 - Ambiguity EIG Falsifier

**Expected Information Gain, Candidate-Set Persistence, and Governed Sampling**

**Leonardo Murillo Montero**

**Draft 1**

---

> *Expected information gain explains how hard to sample. Candidate-set
> persistence decides whether a multihypothesis state must stay open.*

---

## Status

E12 is the empirical falsifier for the ambiguity/sampling bucket.

B10 corrected the current bucket:

\[
\text{continuous temporal flow} + \text{admission gate}.
\]

E11 corrected the noise-versus-structure bucket:

\[
\text{continuous uncertainty} + \text{held-out boundary gate}.
\]

E12 asks whether ambiguity follows the same pattern:

\[
\text{continuous expected information gain} + \text{candidate-set admission gate}.
\]

The empirical companion is:

`empirical/e12_ambiguity_eig_falsifier.py`

with reports:

- `empirical/reports/e12_ambiguity_eig_falsifier.md`
- `empirical/reports/e12_ambiguity_eig_falsifier.json`

---

## Abstract

**Situation.** B2 listed ambiguity error as a prediction-error bucket whose
operation is sampling. B9 identified the main rival: sampling may follow
continuous expected information gain rather than a discrete ambiguity route.
After B10 and E11, the burden is sharper. The B-series should not claim a
primitive ambiguity bucket if EIG under cost explains the behavior.

**Task.** E12 separates two jobs:

1. predicting graded sampling effort;
2. admitting a persistent multihypothesis ambiguity state.

Synthetic episodes come from three worlds:

1. **no-sample world:** low EIG, one dominant candidate;
2. **EIG world:** high EIG and high sampling effort, but the candidate set
   collapses out of sample;
3. **ambiguity world:** high EIG and a persistent held-out candidate set.

**Action.** The continuous rival receives EIG, entropy, value, sampling cost,
precision, and train-side candidate multiplicity. The ambiguity gate receives
held-out candidate-set persistence calibrated on nonambiguity worlds.

**Result.**

\[
\boxed{
\text{EIG\_FITS\_BUT\_GATE\_RECOVERS\_AMBIGUITY.}
}
\]

Plain continuous EIG beats the bucket gate on graded effort: RMSE \(0.093\)
versus \(0.247\). The hybrid EIG-plus-heldout model is strongest overall on
effort, RMSE \(0.052\). But plain EIG detects only \(0.565\) of persistent
ambiguity and falsely admits ambiguity on \(0.178\) of nonambiguity worlds. The
held-out candidate-set gate detects \(1.000\) of ambiguity with \(0.000\)
nonambiguity false admission in the default run.

Therefore ambiguity is not the sampling drive. Ambiguity is the admission
condition for preserving multiple live hypotheses.

---

## The Falsifier

The early bucket table said:

\[
\text{ambiguity error} \longrightarrow \text{sample}.
\]

The strong rival says:

\[
\text{sampling follows continuous expected information gain under cost.}
\]

E12 lets the rival win wherever it should. If EIG predicts both sampling effort
and persistent ambiguity admission, the ambiguity bucket should be demoted to a
descriptive discretization.

The adversarial pressure is train-side multihypothesis bait:

\[
\text{EIG worlds and ambiguity worlds both look multivalued during training.}
\]

Only the ambiguity world preserves candidate-set multiplicity out of sample.

---

## Synthetic Worlds

| World | Generator | Correct response |
|---|---|---|
| no-sample world | low EIG, one candidate | commit |
| EIG world | high EIG, train-side candidate bait, held-out collapse | sample for value, but do not preserve ambiguity |
| ambiguity world | high EIG, persistent held-out candidate set | sample and preserve multihypothesis state |

This distinction matters. A high-EIG animal should inspect, query, or look
again, but it need not maintain a multihypothesis boundary set. Ambiguity is
not equivalent to sampling effort.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | scalar surprise only | blind under matched surprise |
| continuous EIG | EIG, entropy, value, cost, precision, train multiplicity | confuses high-EIG bait with persistent ambiguity |
| ambiguity set gate | held-out candidate-set persistence | loses graded effort |
| governed EIG gate | continuous EIG plus admission gate | should split effort and ambiguity |
| hybrid EIG ambiguity | continuous EIG plus held-out ambiguity variables | strongest composite model |

The continuous rival is intentionally strong. It sees the variables that an
efficient active sampler would use.

The ambiguity gate is intentionally narrow. It sees whether the candidate set
persists beyond the local sample.

---

## Main Result

Default configuration:

- seed: `20260603`
- route/null trials: `900` / `450`
- main ambiguity mix: `0.5`
- conformal alpha: `0.05`
- conformal ambiguity gate: `0.554`

| Model | Effort RMSE | Effort R2 | Ambiguity accuracy | Ambiguity detection | Nonambiguity false admission |
|---|---|---|---|---|---|
| scalar | 0.324 | -0.000 | 0.653 | 0.000 | 0.000 |
| continuous EIG | 0.093 | 0.917 | 0.733 | 0.565 | 0.178 |
| ambiguity set gate | 0.247 | 0.419 | 1.000 | 1.000 | 0.000 |
| governed EIG gate | 0.061 | 0.964 | 1.000 | 1.000 | 0.000 |
| hybrid EIG ambiguity | 0.052 | 0.974 | 1.000 | 1.000 | 0.000 |

The split is clean:

\[
\begin{array}{rcl}
\text{EIG} &:& \text{graded sampling effort;}\\
\text{candidate-set persistence} &:& \text{ambiguity admission.}
\end{array}
\]

The ambiguity set gate is not a good effort model. It is a good admission
model. EIG is not a good ambiguity model. It is a good sampling-drive model.

---

## Source Means

| Source | Train EIG | Held-out EIG | Train entropy | Held-out entropy | Train set | Held-out set | Target effort | Target ambiguity |
|---|---|---|---|---|---|---|---|---|
| ambiguity world | 0.526 | 0.526 | 0.797 | 0.808 | 4.724 | 4.817 | 0.896 | 1.000 |
| EIG world | 0.596 | 0.468 | 0.797 | 0.223 | 4.661 | 1.430 | 0.757 | 0.000 |
| no-sample world | -0.150 | -0.150 | 0.164 | 0.138 | 1.339 | 1.299 | 0.183 | 0.000 |

The hard comparison is ambiguity world versus EIG world. They have similar
train entropy and train candidate-set size. EIG world even has higher train
EIG. The difference is that only ambiguity world preserves the candidate set
out of sample.

---

## Phase Sweep

The phase sweep varies the proportion of ambiguity worlds among non-null route
trials.

| Ambiguity mix | Effort winner | Ambiguity winner | Continuous effort | Bucket effort | Hybrid effort | Continuous FA | Bucket FA | Bucket detection |
|---|---|---|---|---|---|---|---|---|
| 0.000 | hybrid EIG ambiguity | scalar | 0.056 | 0.289 | 0.049 | 0.000 | 0.000 | nan |
| 0.250 | hybrid EIG ambiguity | hybrid EIG ambiguity | 0.084 | 0.271 | 0.051 | 0.001 | 0.000 | 0.994 |
| 0.500 | hybrid EIG ambiguity | hybrid EIG ambiguity | 0.092 | 0.253 | 0.051 | 0.208 | 0.000 | 1.000 |
| 0.750 | hybrid EIG ambiguity | hybrid EIG ambiguity | 0.084 | 0.202 | 0.054 | 0.306 | 0.000 | 1.000 |
| 1.000 | hybrid EIG ambiguity | hybrid EIG ambiguity | 0.064 | 0.112 | 0.054 | 0.000 | 0.060 | 1.000 |

The sweep says the same thing as the main table. EIG-family models own effort.
Candidate persistence owns ambiguity admission. The pure bucket is too coarse,
but the pure EIG rival confuses sampling drive with multihypothesis state.

---

## Interpretation

E12 changes the ambiguity bucket.

The older phrase was:

\[
\boxed{
\text{ambiguity error is a sampling bucket.}
}
\]

The updated phrase is:

\[
\boxed{
\text{sampling is continuous EIG under candidate-set admission.}
}
\]

This is a better brain hypothesis. It maps naturally onto animal behavior:
organisms sample more when information is valuable, but they preserve a live
set of alternatives only when the ambiguity persists across evidence.

The bucket is not the sampling drive. The bucket is the admission decision:

\[
\text{must more than one hypothesis remain alive?}
\]

---

## Biological Prediction

E12 predicts a dissociation:

1. eye movements, queries, orienting, or exploration effort should track
   continuous expected information gain and sampling cost;
2. sustained multihypothesis neural state should track candidate-set
   persistence, not merely high EIG;
3. train-side ambiguity that collapses with new evidence should produce
   transient sampling but not durable ambiguity maintenance;
4. perturbing candidate-set maintenance should impair ambiguity handling more
   than ordinary high-EIG sampling.

The decisive measurement is not whether the animal samples. It is whether
sampling effort and persistent ambiguity can be separated.

---

## Consequence for the B-Series

B10, E11, and E12 now share a pattern:

| Domain | Continuous variable | Governed admission |
|---|---|---|
| current | temporal flow | current admission |
| noise/structure | expected/unexpected uncertainty | held-out structural closure |
| ambiguity/sampling | expected information gain | candidate-set persistence |

The B-series should now speak less like a taxonomy of primitive buckets and
more like a theory of governed admissions over continuous control fields.

\[
\boxed{
\text{brains route continuous evidence by admitting it into operations.}
}
\]

---

## What Would Falsify This Update

The governed-sampling update would fail if:

1. continuous EIG predicts both effort and persistent ambiguity admission;
2. candidate-set persistence adds no held-out sensitivity;
3. high-EIG nonambiguous worlds and persistent ambiguity worlds cannot be
   behaviorally or neurally separated;
4. perturbing candidate-set maintenance leaves ambiguity behavior intact.

If that happens, ambiguity should be demoted to a readable discretization of
EIG under cost.

---

## Next Experimental Target

The next best falsifier is **E13: Capacity Versus Resource-Rational Control**.
The question should be whether compression/tool use is a distinct route, or
whether it is continuous resource-rational cost minimization with an external
memory/action gate. The experiment should let resource rationality win.

