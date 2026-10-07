# E17 - Temporal PenDigits Admission

**When Static Recognition Fails, Temporal Persistence Helps**

**Leonardo Murillo Montero**

**Draft 1**

---

> *Admission should matter where local evidence has not yet earned the right to
> become a durable operation.*

---

## Status

E17 follows E16, the first external static-image anchor.

E16 used real UCI Optdigits images and produced a useful negative result:
original-image continuous evidence absorbed the persistence gate on simple
static recognition.

E17 asks the next question:

\[
\text{does the gate return when the external task is temporal?}
\]

The empirical companion is:

`empirical/e17_temporal_pendigits_admission_probe.py`

with reports:

- `empirical/reports/e17_temporal_pendigits_admission_probe.md`
- `empirical/reports/e17_temporal_pendigits_admission_probe.json`

The data source is the UCI Pen-Based Recognition of Handwritten Digits dataset:

`https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits`

UCI describes this dataset as 10992 instances with 16 integer features. The
features are eight resampled \((x,y)\) points along a handwritten digit
trajectory.

---

## Abstract

**Situation.** E16 showed that static recognition can be too local for the
admission-gate hypothesis. If the whole image is already present, local
continuous evidence can predict perturbation durability.

**Task.** E17 tests an external temporal proxy. A digit is only partially drawn.
The model first sees an early prefix of the pen trajectory. It can then observe
middle points for label-free persistence. Durable admission is evaluated using
late points.

**Action.** The experiment separates three windows:

1. **early field:** the first two trajectory points;
2. **persistence gate:** middle prefixes ending at points 4, 5, and 6;
3. **audit target:** late prefixes ending at points 7 and 8.

The continuous model receives only early evidence. The gate receives
middle-stroke persistence. The target asks whether the early prediction is
correct and remains correct under late audit.

**Result.**

\[
\boxed{
\text{TEMPORAL\_PERSISTENCE\_GOVERNS\_ADMISSION.}
}
\]

Early continuous evidence fits graded intensity, but it over-admits. The
temporal gate sharply reduces false admission:

| Quantity | Early continuous evidence | Temporal persistence gate |
|---|---:|---:|
| intensity RMSE | 0.016 | 0.017 |
| admission RMSE | 0.397 | 0.312 |
| non-admitted false admission | 0.265 | 0.055 |
| admission detection | 0.794 | 0.768 |
| bait false admission | 0.484 | 0.135 |

The hybrid model is strongest:

\[
\operatorname{RMSE}_{\text{hybrid admission}} = 0.212.
\]

Therefore E17 repairs the E16 correction:

\[
\boxed{
\text{governed admission is predicted under partial temporal evidence, not
under all recognition tasks.}
}
\]

---

## Why E17 Is Different From E16

E16 was static. The whole digit image was available at once.

E17 is sequential. The digit has only begun.

That difference matters. With a static image, local evidence already contains
most of the durable-recognition information. With a trajectory prefix, local
evidence is incomplete. The system can have a plausible early guess that should
not yet become a durable operation.

The B-series hypothesis should therefore be:

\[
\boxed{
\text{admission gates matter when evidence must persist beyond the local
sample.}
}
\]

not:

\[
\text{every recognition decision requires a separate gate.}
\]

---

## Experimental Design

The script downloads and caches:

- `pendigits.tra`
- `pendigits.tes`

from the UCI repository.

The UCI training file is split into:

- classifier-training examples;
- calibration examples.

The UCI test file is held out for reporting.

For each prefix length, the script trains a NumPy ridge classifier. No external
machine-learning package is required.

---

## Temporal Windows

Each example has eight \((x,y)\) points:

\[
(x_1,y_1),\ldots,(x_8,y_8).
\]

E17 uses:

| Window | Points used | Role |
|---|---:|---|
| early field | 1-2 | local continuous evidence |
| gate | 1-4, 1-5, 1-6 | label-free persistence of early prediction |
| audit | 1-7, 1-8 | durable target against true label |

The gate does not see the label. It asks whether the early predicted digit
continues to be predicted as more of the trajectory arrives.

The audit target does use the label, but only on later prefixes:

\[
\text{admit} = 
\left[
\begin{array}{c}
\text{early prediction is correct}\\
\text{and late audit prefixes preserve the true label}
\end{array}
\right].
\]

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | early top confidence only | over-admits confident starts |
| continuous early | early prediction, probability vector, margins, entropy, trajectory geometry | local evidence may over-admit |
| temporal gate | predicted digit plus conformal persistence bit | may lose intensity |
| governed temporal | early evidence plus gate bit | should split intensity and admission |
| hybrid full | early evidence plus raw persistence scores | strongest composite model |

---

## Main Result

Default configuration:

- seed: `20260603`
- train/calibration/test: `5620` / `1874` / `3498`
- early points: `2`
- gate points: `4, 5, 6`
- audit points: `7, 8`
- audit threshold: `1.00`
- conformal alpha: `0.05`
- early test accuracy: `0.457`
- durable rate on test: `0.418`

| Model | Intensity RMSE | Intensity R2 | Admission RMSE | Admission accuracy | Detection | Non-admitted FA | Bait FA |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar | 0.015 | 0.261 | 0.464 | 0.657 | 0.585 | 0.292 | 0.859 |
| continuous early | 0.016 | 0.192 | 0.397 | 0.760 | 0.794 | 0.265 | 0.484 |
| temporal gate | 0.017 | 0.123 | 0.312 | 0.871 | 0.768 | 0.055 | 0.135 |
| governed temporal | 0.017 | 0.104 | 0.292 | 0.885 | 0.858 | 0.096 | 0.119 |
| hybrid full | 0.017 | 0.058 | 0.212 | 0.937 | 0.957 | 0.077 | 0.112 |

The gate loses little on detection and greatly reduces false admission. The
governed and hybrid models are strongest because they combine early evidence
with temporal persistence.

---

## Prefix Sweep

The prefix sweep is the real lesson.

| Early points | Early accuracy | Durable rate | Continuous FA | Gate FA | Continuous detection | Gate detection | Continuous bait FA | Gate bait FA |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0.457 | 0.418 | 0.265 | 0.055 | 0.794 | 0.768 | 0.484 | 0.135 |
| 3 | 0.577 | 0.522 | 0.200 | 0.133 | 0.913 | 0.639 | 0.344 | 0.218 |
| 4 | 0.671 | 0.622 | 0.177 | 0.276 | 0.962 | 0.738 | 0.281 | 0.326 |
| 5 | 0.737 | 0.693 | 0.199 | 0.820 | 0.973 | 0.958 | 0.354 | 0.829 |

The gate matters when the early evidence is genuinely partial. Once enough of
the trajectory has arrived, early continuous evidence begins to absorb the
admission problem, and a standalone gate can become harmful.

This is exactly the correction E16 demanded.

---

## Interpretation

E17 does not restore the broad claim that all recognition requires governed
admission.

It supports the narrower, better claim:

\[
\boxed{
\text{governed admission appears when local evidence must survive temporal
continuation.}
}
\]

The brain-reverse-engineering implication is important. We should not expect
separate admission gates in every static perceptual classification. We should
look for them where the organism must decide whether an incomplete signal has
earned entry into a durable operation:

- continue a prediction;
- commit an action;
- preserve an ambiguity;
- seek information;
- externalize to a tool;
- inhibit/refuse;
- report consciously.

E17 says the right domain is not recognition in general. It is commitment under
partial evidence.

---

## Relation to T17/T18/T19

T17 says an active boundary system routes evidence into operations.

T18 says lawful admission must be calibrated, not merely asserted.

T19 says terminal access is a governed admission into reportable/conscious
availability.

E17 gives the external proxy version:

\[
\text{early field} \rightarrow \text{temporal persistence gate}
\rightarrow \text{durable admission}.
\]

This is close to the active-boundary story because the system sees only part of
the trajectory. Admission is not a classification label. It is a commitment to
let a local hypothesis survive additional evidence.

---

## Anti-Tautology Checks

- The dataset is external pen-trajectory digit data, not a synthetic B-series
  generator.
- Early evidence uses only the first trajectory points.
- The persistence gate is label-free and uses middle trajectory points.
- Durable admission is evaluated on later trajectory points and true labels.
- Calibration thresholds are estimated on calibration examples and scored on
  the held-out UCI test file.
- The prefix sweep tests whether the result depends on how much early evidence
  is available.

---

## Limits

E17 is still not brain data.

Its limitations are clear:

- the sequence is spatially resampled, not raw human sensorimotor time;
- the classifiers are simple ridge models;
- durable admission is engineered from labels and prefix classifiers;
- no reaction time, confidence report, neural signal, or intervention is
  measured;
- the positive gate result is specific to the early two-point regime.

These limits are good. They define the next empirical step.

---

## Conclusion

E16 and E17 together give the first externally anchored correction to the
B-series:

\[
\boxed{
\begin{array}{c}
\text{static local evidence can absorb persistence;}\\
\text{partial temporal evidence benefits from admission gating.}
\end{array}
}
\]

That is now the sharper brain hypothesis:

\[
\boxed{
\text{the brain needs governed admission where commitment outruns local
evidence.}
}
\]

