# E16 - External Digits Persistence Anchor

**A First Real-Data Check on Field Versus Admission**

**Leonardo Murillo Montero**

**Draft 1**

---

> *The first external anchor should be allowed to say no.*

---

## Status

E16 is the first B/E-series experiment after E15's integrated synthetic
absorber test.

E15 showed that, inside the synthetic grammar, one pooled continuous absorber
still failed to replace governed admission. E16 asks whether that split survives
on a real perceptual proxy.

The empirical companion is:

`empirical/e16_external_digits_persistence_anchor.py`

with reports:

- `empirical/reports/e16_external_digits_persistence_anchor.md`
- `empirical/reports/e16_external_digits_persistence_anchor.json`

The data source is the UCI Optical Recognition of Handwritten Digits dataset:

`https://archive.ics.uci.edu/dataset/80/optical%2Brecognition%2Bof%2Bhandwritten%2Bdigits`

UCI describes this dataset as 8x8 integer features derived from normalized
handwritten digit bitmaps, with 64 features and 5620 instances.

---

## Abstract

**Situation.** B10 through E15 support a revised B-series hypothesis:

\[
\text{continuous field} \rightarrow \text{persistence/admission gate}
\rightarrow \text{operation}.
\]

But those results are still synthetic. E16 tests a real perceptual proxy using
handwritten digit recognition.

**Task.** Train a small OCR classifier from scratch on real UCI digit data. Use
original-image evidence as the continuous field. Use label-free perturbation
persistence as the gate. Evaluate durable recognition on a different audit
perturbation set using true labels.

**Action.** The experiment separates:

1. **graded recognition intensity:** the classifier's probability assigned to
   the true digit on the original image;
2. **durable admission:** whether the original prediction is correct and remains
   correct under held-out audit perturbations.

The continuous model receives only original-image evidence. The persistence
gate receives perturbation stability. The audit target uses a different
perturbation family.

**Result.**

\[
\boxed{
\text{EXTERNAL\_CONTINUOUS\_EVIDENCE\_ABSORBS\_PERSISTENCE.}
}
\]

On this simple perceptual proxy, original-image continuous evidence is at least
as good as the persistence gate for durable admission:

| Quantity | Continuous evidence | Persistence gate |
|---|---:|---:|
| intensity RMSE | 0.019 | 0.029 |
| admission RMSE | 0.298 | 0.325 |
| non-admitted false admission | 0.093 | 0.090 |
| admission detection | 0.765 | 0.690 |
| bait false admission | 0.065 | 0.081 |

The governed and hybrid models improve admission slightly, but the gate alone
does not supply the clean E15 advantage.

Therefore E16 is a useful negative anchor:

\[
\boxed{
\text{simple perceptual confidence can absorb persistence in this proxy.}
}
\]

---

## Why This Matters

E16 is not a biological experiment. It is a real-data protocol rehearsal.

That still matters because it prevents the B-series from becoming too smooth.
If the architecture were merely a universal pattern we can always impose, every
external proxy would produce the same gate-survival result. E16 does not.

The result says:

\[
\text{do not claim governed admission for every recognition problem.}
\]

For simple handwritten digits, original-image evidence already contains much of
the information needed for perturbation durability. The gate is not a distinct
winner.

---

## Experimental Design

The script downloads and caches:

- `optdigits.tra`
- `optdigits.tes`

from the UCI repository.

The training split is divided into:

- classifier-training examples;
- calibration examples.

The UCI test file is held out for reporting.

The OCR classifier is a NumPy ridge classifier over the 64 digit features. No
external machine-learning package is required.

---

## Variables

### Continuous Evidence

The continuous evidence model receives only original-image variables:

- predicted digit;
- top probability;
- probability margin;
- entropy;
- logit margin;
- image mass, contrast, edge energy;
- horizontal and vertical symmetry;
- center of mass and spread;
- centroid-distance features.

These are local perceptual evidence fields.

### Persistence Gate

The gate uses label-free perturbation persistence. It asks whether the predicted
digit remains stable under a gate perturbation set:

- vertical and horizontal shifts;
- fade;
- brighten.

The gate score is:

\[
\text{top confidence} \times \text{same-prediction fraction}
\times \text{mean perturbed confidence}.
\]

The conformal gate threshold is calibrated on non-admitted calibration examples.

### Durable Admission Target

The durable admission target is evaluated separately. An example is admitted if:

1. the original prediction is correct;
2. the true label survives at least half of the audit perturbations.

The audit perturbation set differs from the gate set:

- diagonal shifts;
- blur;
- thickening;
- center occlusion;
- border fading.

This is the main anti-tautology check. Gate evidence and admission target are
related but not identical.

---

## Main Result

Default configuration:

- seed: `20260603`
- train/calibration/test: `2867` / `956` / `1797`
- audit threshold: `0.50`
- conformal alpha: `0.05`
- durable rate on test: `0.267`
- original test accuracy: `0.918`

| Model | Intensity RMSE | Intensity R2 | Admission RMSE | Admission accuracy | Detection | Non-admitted FA | Bait FA |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar | 0.017 | 0.762 | 0.431 | 0.733 | 0.000 | 0.000 | 0.000 |
| continuous evidence | 0.019 | 0.699 | 0.298 | 0.869 | 0.765 | 0.093 | 0.065 |
| persistence gate | 0.029 | 0.257 | 0.325 | 0.851 | 0.690 | 0.090 | 0.081 |
| governed evidence | 0.020 | 0.666 | 0.295 | 0.880 | 0.790 | 0.087 | 0.076 |
| hybrid full | 0.021 | 0.613 | 0.286 | 0.883 | 0.794 | 0.084 | 0.068 |

The gate controls false admission by a tiny amount, but it loses detection and
does not beat continuous evidence on admission RMSE or bait false admission.
The hybrid model is best, but only modestly.

---

## Threshold Sweep

The audit threshold sweep is the most important diagnostic.

| Audit threshold | Durable rate | Admission winner | Continuous FA | Gate FA | Continuous detection | Gate detection |
|---:|---:|---|---:|---:|---:|---:|
| 0.500 | 0.267 | hybrid full | 0.093 | 0.090 | 0.765 | 0.690 |
| 0.580 | 0.134 | governed evidence | 0.031 | 0.054 | 0.671 | 0.608 |
| 0.720 | 0.028 | governed evidence | 0.002 | 0.000 | 0.080 | 0.000 |
| 0.860 | 0.004 | hybrid full | 0.001 | 0.000 | 0.000 | 0.000 |
| 1.000 | 0.004 | hybrid full | 0.001 | 0.000 | 0.000 | 0.000 |

When the audit is too strict, almost nothing is admitted. The gate then
controls false admission trivially but detects almost no durable examples. When
the audit is non-degenerate, original continuous evidence is competitive with
or better than persistence.

---

## Interpretation

E16 weakens the broad version of the B-series hypothesis.

The broad version would say:

\[
\text{continuous evidence alone cannot decide durable operation entry.}
\]

The external digit proxy says:

\[
\text{for simple static recognition, it often can.}
\]

That does not refute the brain hypothesis. It narrows it.

The better claim is:

\[
\boxed{
\text{governed admission should matter most when local evidence is not enough.}
}
\]

The likely regimes are:

- active sensing;
- delayed evidence;
- temporal continuity;
- tool-use decisions;
- rule-governed inhibition;
- conscious report under capacity;
- cases where confidence and persistence can be experimentally dissociated.

Simple handwritten digit recognition is too local. It does not force a separate
admission mechanism.

---

## Consequence for the B-Series

E16 should be treated as a corrective anchor.

After E15, the tempting sentence was:

\[
\text{continuous fields always need governed admission.}
\]

After E16, the safer sentence is:

\[
\boxed{
\text{governed admission is predicted when durable operation cannot be read
from local evidence alone.}
}
\]

That is a better biological hypothesis. It is less sweeping and more testable.

---

## Anti-Tautology Checks

- The dataset is external real handwritten digit data, not a synthetic B-series
  generator.
- The OCR classifier is trained from scratch using NumPy only.
- Continuous evidence uses the original image only.
- Gate evidence uses label-free perturbation persistence under one
  perturbation set.
- Durable admission is evaluated with true labels under a different audit
  perturbation set.
- Calibration thresholds are estimated on calibration examples and scored on
  the held-out UCI test file.
- The result is allowed to be negative.

---

## Limits

E16 is not a neural experiment.

It also has several computational limitations:

- the OCR model is deliberately simple;
- classifier probabilities are not psychophysical confidence reports;
- perturbations are hand-chosen image transforms;
- durable recognition is an engineered proxy for perceptual admission;
- the dataset is static, not active or temporal;
- no behavior, reaction time, neural recording, or perturbation intervention is
  measured.

These limits explain why E16 is an anchor, not an endpoint.

---

## Conclusion

E16 is the first real pushback against the synthetic sequence.

The result does not kill the program. It improves it:

\[
\boxed{
\begin{array}{c}
\text{local continuous evidence may be enough for simple static recognition;}\\
\text{governed admission should be tested where evidence must persist}\\
\text{across time, action, rule, or report.}
\end{array}
}
\]

The next experiment should therefore use an external task with temporal or
active structure, not another static image classifier.

