# E15 - Integrated Absorber Falsifier

**Can One Pooled Continuous Policy Absorb Governed Admission?**

**Leonardo Murillo Montero**

**Draft 1**

---

> *If the gates are fake, a strong pooled continuous model should make them
> unnecessary.*

---

## Status

E15 is the integrated absorber test for the B-series brain hypothesis.

B10 and E11-E14 repeatedly found the same shape:

\[
\text{continuous field fits intensity; governed gate controls admission.}
\]

The worry is that this shape may be an artifact of testing one bucket at a
time. E15 therefore pools the domains:

- current;
- structure;
- ambiguity;
- externalization;
- refusal.

The empirical companion is:

`empirical/e15_integrated_absorber_falsifier.py`

with reports:

- `empirical/reports/e15_integrated_absorber_falsifier.md`
- `empirical/reports/e15_integrated_absorber_falsifier.json`

---

## Abstract

**Situation.** The B-series has been correcting its own early bucket language.
The emerging claim is not that the brain contains primitive prediction-error
buckets. The stronger claim is that animal brains route continuous control
fields through governed admissions.

**Task.** E15 tests the strongest synthetic objection:

\[
\boxed{
\text{a sufficiently rich continuous policy absorbs all gates.}
}
\]

The continuous absorber receives all five domains, train-side continuous fields,
squares, and pairwise interactions. The gate bank receives only
domain-calibrated held-out persistence scores.

**Action.** Synthetic episodes contain admitted cases, bait cases, and ordinary
non-admitted cases. Admitted and bait cases share train-side continuous fields
inside each domain. Only held-out persistence separates durable admission from
local bait.

**Result.**

\[
\boxed{
\text{CONTINUOUS\_ABSORBER\_FITS\_INTENSITY\_BUT\_GATES\_CONTROL\_ADMISSION.}
}
\]

The continuous absorber predicts graded operation intensity well:

\[
\operatorname{RMSE}_{\text{intensity}} = 0.049.
\]

The gate-only model is worse on intensity:

\[
\operatorname{RMSE}_{\text{gate intensity}} = 0.140.
\]

But the continuous absorber falsely admits non-admitted cases \(0.708\) of the
time and bait cases \(0.925\) of the time. The gate bank detects admitted cases
at \(1.000\) while holding false admission to \(0.048\).

Therefore E15 strengthens the revised B-series claim:

\[
\boxed{
\text{the substrate is continuous, but operation entry is governed.}
}
\]

---

## The Falsifier

The older bucket story was:

\[
\text{prediction error} \rightarrow \text{bucket} \rightarrow \text{operation}.
\]

The corrected story after B10 and E11-E14 was:

\[
\text{continuous field} \rightarrow \text{persistence gate} \rightarrow
\text{operation}.
\]

E15 attacks the correction directly. It asks whether the gates are merely
shadows of a richer continuous policy. If so, one pooled absorber should solve
both jobs:

1. predict graded intensity;
2. admit only durable operations.

The absorber is intentionally not weak. It receives:

- a domain tag;
- local drive;
- train-side evidence;
- temporal flow;
- uncertainty;
- expected information gain;
- resource pressure;
- risk pressure;
- value and cost;
- train-side rule, tool, and candidate-set signals;
- compression, precision, and competence;
- squares and pairwise feature interactions.

It does not receive held-out persistence. That exclusion is the falsifier. If
train-side continuous fields are enough, the absorber should still control
false admission.

---

## Synthetic Domains

| Domain | Admitted case | Bait case | Ordinary non-admitted case | Gate evidence |
|---|---|---|---|---|
| current | current world | current bait world | idle world | persistent current |
| structure | structure world | uncertainty bait world | noise world | held-out structural persistence |
| ambiguity | ambiguity world | EIG bait world | no-sample world | held-out candidate persistence |
| externalize | tool world | tool bait world | compress world | held-out tool reliability |
| refusal | forbidden world | rule bait world | risk world | held-out rule persistence |

The bait cases are the important pressure. They look locally compelling but do
not persist. They should drive intensity without being admitted.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | matched scalar score only | blind baseline |
| continuous absorber | pooled train-side continuous fields, squares, interactions | may over-admit bait |
| gate bank | domain gate bit from held-out persistence | loses graded intensity |
| governed absorber | continuous absorber plus gate bit | should split intensity and admission |
| hybrid full | continuous fields plus raw gate score and gate bit | strongest composite model |

This comparison is deliberately asymmetric. The continuous absorber is strong
and broad. The gate bank is narrow. If the narrow gate still wins admission,
the result is not because the continuous rival was starved of ordinary control
signals.

---

## Main Result

Default configuration:

- seed: `20260603`
- trials per domain: `650`
- admitted/bait share: `0.60` / `0.30`
- conformal alpha: `0.05`
- ridge: `0.002`

| Model | Intensity RMSE | Intensity R2 | Admission RMSE | Admission accuracy | Detection | Non-admitted false admission | Bait false admission |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar | 0.162 | -0.000 | 0.473 | 0.611 | 1.000 | 1.000 | 1.000 |
| continuous absorber | 0.049 | 0.906 | 0.446 | 0.683 | 0.931 | 0.708 | 0.925 |
| gate bank | 0.140 | 0.246 | 0.132 | 0.982 | 1.000 | 0.048 | 0.062 |
| governed absorber | 0.047 | 0.916 | 0.136 | 0.982 | 1.000 | 0.048 | 0.062 |
| hybrid full | 0.047 | 0.916 | 0.043 | 1.000 | 1.000 | 0.000 | 0.000 |

The continuous absorber is the right model for intensity. The gate bank is the
right model for admission. The governed absorber has both properties.

---

## Domain-Level Result

| Domain | Continuous detection | Continuous FA | Continuous bait FA | Gate detection | Gate FA | Gate bait FA |
|---|---:|---:|---:|---:|---:|---:|
| current | 0.869 | 0.619 | 0.827 | 1.000 | 0.054 | 0.073 |
| structure | 0.940 | 0.733 | 0.925 | 1.000 | 0.032 | 0.040 |
| ambiguity | 0.954 | 0.775 | 0.971 | 1.000 | 0.069 | 0.086 |
| externalize | 0.932 | 0.708 | 0.917 | 1.000 | 0.049 | 0.063 |
| refusal | 0.963 | 0.697 | 0.983 | 1.000 | 0.033 | 0.046 |

The failure is not confined to one hand-picked bucket. It appears across all
five domains.

---

## Phase Sweep

The phase sweep varies the admitted share while preserving bait pressure when
possible.

| Admitted share | Bait share | Intensity winner | Admission winner | Continuous FA | Gate FA | Gate detection | Continuous bait FA |
|---:|---:|---|---|---:|---:|---:|---:|
| 0.000 | 0.300 | continuous absorber | gate bank | 0.000 | 0.000 | nan | 0.000 |
| 0.250 | 0.300 | hybrid full | hybrid full | 0.149 | 0.058 | 1.000 | 0.370 |
| 0.450 | 0.300 | hybrid full | hybrid full | 0.434 | 0.055 | 1.000 | 0.796 |
| 0.600 | 0.300 | governed absorber | hybrid full | 0.696 | 0.062 | 1.000 | 0.901 |
| 0.800 | 0.100 | governed absorber | hybrid full | 0.471 | 0.044 | 1.000 | 1.000 |
| 1.000 | 0.000 | continuous absorber | scalar | nan | nan | 1.000 | nan |

The gate is not crowned in every regime. When no admitted cases exist, there is
nothing to detect. When no non-admitted cases exist, false admission is
undefined. The gate matters in the mixed regime where durable admission and
bait coexist.

---

## Interpretation

E15 is the strongest internal result so far against primitive bucket language.
The continuous absorber is excellent at graded operation intensity. That means
the early bucket taxonomy is probably not the neural substrate.

But the same result is also the strongest internal result so far for governed
admission. The absorber confuses local drive with durable entry. It can say how
strongly the system should move, sample, inhibit, externalize, or close, but it
does not know whether that movement should become an admitted operation.

The revised architecture is therefore:

\[
\boxed{
\text{control field} \rightarrow \text{persistence test} \rightarrow
\text{admission} \rightarrow \text{operation}.
}
\]

The "bucket" is not gone. It has changed jobs. It is not the hidden substrate.
It is the visible operational admission surface.

---

## What This Implies for the Brain Hypothesis

For reverse-engineering animal brains, E15 says not to search first for a
neural population that literally encodes "the current bucket" or "the
ambiguity bucket." Search instead for:

1. a continuous control field that explains graded drive;
2. a persistence or cross-context test that rejects local bait;
3. an admission event that allows the field to enter learning, action,
   attention, externalization, refusal, or conscious report.

The likely biological picture is:

\[
\text{distributed field dynamics} + \text{gated recurrent admission}.
\]

That is compatible with T17/T18/T19:

- T17 supplies active boundary inference and route variables;
- T18 supplies conformal admission and lawful calibration;
- T19 supplies terminal governed access for conscious report.

The B/E series now supplies a reverse-engineering task: identify the continuous
field and the admission gate separately.

---

## Limits

E15 is still synthetic. It does not prove that brains use held-out persistence
gates. It proves something narrower:

\[
\text{within this grammar, continuous intensity and operation admission are
separable jobs.}
\]

The remaining risks are serious:

- held-out persistence is explicitly provided to the gate models;
- admitted and bait cases are deliberately matched on train-side fields;
- the phase sweep uses the same generator grammar across domains;
- no neural, behavioral, or external dataset has been used yet;
- the hybrid full model is unsurprisingly strongest because it receives the raw
  gate score.

These are not defects to hide. They are the next experimental obligations.

---

## Conclusion

E15 does not prove the brain hypothesis. It does something more useful at this
stage: it blocks the easiest internal absorber objection.

The corrected B-series thesis is now:

\[
\boxed{
\begin{array}{c}
\text{animal brains are continuous control systems}\\
\text{whose durable operations are governed by admission gates.}
\end{array}
}
\]

The next falsifier should leave the synthetic sandbox.

