# E18 - Active PenDigits Sampling

**Commit Now or Request More Evidence?**

**Leonardo Murillo Montero**

**Draft 1**

---

> *Active minds do not only classify. They decide when the evidence is worth
> extending.*

---

## Status

E18 follows E17's temporal PenDigits admission result.

E17 showed that temporal persistence controls false admission when only the
first two pen-trajectory points are available. E18 asks the active version:

\[
\text{should the system commit now, or request more of the stroke?}
\]

The empirical companion is:

`empirical/e18_active_pendigits_sampling_probe.py`

with reports:

- `empirical/reports/e18_active_pendigits_sampling_probe.md`
- `empirical/reports/e18_active_pendigits_sampling_probe.json`

The data source remains the UCI Pen-Based Recognition of Handwritten Digits
dataset:

`https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits`

---

## Abstract

**Situation.** E16 and E17 sharpened the brain hypothesis:

\[
\text{static local evidence can absorb persistence,}
\]

but

\[
\text{partial temporal evidence benefits from admission gating.}
\]

E18 tests the next operation: active information seeking.

**Task.** At the first two trajectory points, an agent has an early digit
prediction. It can commit immediately or pay an observation cost to request the
completed trajectory. The target is cost-sensitive: request more only when the
completed trajectory improves true-label support enough to pay for the extra
observation.

**Action.** The experiment separates:

1. **sampling value:** how much requesting more evidence is worth;
2. **commit admission:** whether the early prediction is safe to admit as a
   commitment.

**Result.**

\[
\boxed{
\text{ACTIVE\_HYBRID\_SAMPLING\_GATE\_NEEDED.}
}
\]

Neither early evidence nor the pure temporal gate wins alone. The hybrid model
is best:

| Quantity | Early evidence | Temporal gate | Hybrid |
|---|---:|---:|---:|
| sampling RMSE | 0.077 | 0.082 | 0.046 |
| commit RMSE | 0.409 | 0.438 | 0.293 |
| false commit | 0.074 | 0.045 | 0.052 |
| commit detection | 0.376 | 0.180 | 0.731 |
| request detection | 0.926 | 0.955 | 0.948 |
| bait false commit | 0.078 | 0.054 | 0.058 |

The pure gate is very conservative: it controls false commits but misses too
many safe commits. The early continuous model detects more commits but
over-commits. The hybrid policy keeps request detection high while recovering
safe commits.

Therefore E18 supports:

\[
\boxed{
\text{active sampling requires a governed hybrid of value and persistence.}
}
\]

---

## Why E18 Is Not Just E17 Again

E17 asked:

\[
\text{is this early prediction durable?}
\]

E18 asks:

\[
\text{is it worth paying for more evidence before committing?}
\]

That is a different operation. It introduces cost.

The first implementation used a binary correct/incorrect utility. That made the
commit/request target almost insensitive to observation cost. The corrected E18
uses true-label support:

\[
\begin{array}{rcl}
U_{\text{commit}} &=& p_{\text{early}}(y),\\
U_{\text{request}} &=& p_{\text{full}}(y) - c.
\end{array}
\]

The agent should request more when:

\[
U_{\text{request}} > U_{\text{commit}}.
\]

This makes the cost sweep meaningful.

---

## Experimental Design

Each PenDigits example has eight \((x,y)\) trajectory points.

E18 uses:

| Window | Points used | Role |
|---|---:|---|
| early field | 1-2 | local evidence and sampling value |
| temporal gate | 1-4, 1-5, 1-6 | label-free persistence |
| full utility | 1-8 | utility after requesting more |

The gate does not use labels. It asks whether the early predicted digit remains
stable as middle trajectory points arrive.

The active target uses the true label only to evaluate utility.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | early top confidence only | near always request or crude commit |
| continuous sampling | early prediction, probabilities, margins, entropy, prefix geometry | detects value but over-commits |
| temporal commit gate | predicted digit plus conformal persistence bit | controls false commits but too conservative |
| governed sampling | early evidence plus gate bit | should balance value and admission |
| hybrid full | early evidence plus raw persistence scores | strongest active policy |

---

## Main Result

Default configuration:

- seed: `20260603`
- train/calibration/test: `5620` / `1874` / `3498`
- early points: `2`
- gate points: `4, 5, 6`
- full points: `8`
- observation cost: `0.025`
- conformal alpha: `0.05`
- early test accuracy: `0.457`
- full test accuracy: `0.820`
- commit rate: `0.324`
- request rate: `0.676`

| Model | Sampling RMSE | Sampling R2 | Commit RMSE | Commit accuracy | Commit detection | False commit | Request detection | Bait false commit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| scalar | 0.085 | 0.033 | 0.455 | 0.688 | 0.047 | 0.005 | 0.995 | 0.017 |
| continuous sampling | 0.077 | 0.212 | 0.409 | 0.748 | 0.376 | 0.074 | 0.926 | 0.078 |
| temporal commit gate | 0.082 | 0.097 | 0.438 | 0.704 | 0.180 | 0.045 | 0.955 | 0.054 |
| governed sampling | 0.077 | 0.214 | 0.408 | 0.747 | 0.378 | 0.076 | 0.924 | 0.085 |
| hybrid full | 0.046 | 0.719 | 0.293 | 0.878 | 0.731 | 0.052 | 0.948 | 0.058 |

The active result is not a pure-gate win. The pure gate is safer but too
reluctant. The hybrid policy is the first model that looks like a plausible
active controller.

---

## Cost Sweep

| Observation cost | Commit rate | Request rate | Commit winner | Continuous false commit | Gate false commit | Continuous commit detection | Gate commit detection |
|---:|---:|---:|---|---:|---:|---:|---:|
| 0.000 | 0.043 | 0.957 | hybrid full | 0.002 | 0.000 | 0.033 | 0.000 |
| 0.010 | 0.143 | 0.857 | hybrid full | 0.013 | 0.000 | 0.062 | 0.000 |
| 0.025 | 0.324 | 0.676 | hybrid full | 0.074 | 0.045 | 0.376 | 0.180 |
| 0.050 | 0.727 | 0.273 | hybrid full | 0.482 | 0.711 | 0.840 | 0.903 |
| 0.100 | 1.000 | 0.000 | scalar | 1.000 | 1.000 | 1.000 | 1.000 |

The cost sweep shows three regimes:

1. **cheap evidence:** request almost always;
2. **intermediate cost:** active control is nontrivial and hybrid wins;
3. **expensive evidence:** commit almost always.

The interesting regime is the middle one.

---

## Interpretation

E18 is the first active external anchor.

It supports neither:

\[
\text{sampling is just early continuous uncertainty}
\]

nor:

\[
\text{sampling is just a persistence gate.}
\]

The better reading is:

\[
\boxed{
\text{active information seeking is value control under admission governance.}
}
\]

The continuous field estimates whether more evidence may be worth the cost.
The persistence gate prevents bad early commitments. The hybrid policy joins
them.

This fits T17 better than a bucket story. T17 does not need a primitive
"sampling bucket." It needs an active boundary policy that can route uncertainty
into more evidence, while controlling when a partial hypothesis is allowed to
become a commitment.

---

## Anti-Tautology Checks

- The dataset is external pen-trajectory digit data.
- Early evidence uses only the first trajectory points.
- Requesting more has an explicit cost, so the target is not always-sample.
- The gate is label-free and uses middle trajectory persistence.
- The commit target is evaluated from early utility versus full-trajectory
  utility.
- Calibration thresholds are estimated on calibration examples and scored on
  the held-out UCI test file.
- The cost sweep tests whether the active result depends on sampling cost.

---

## Limits

E18 is still a proxy.

Its limitations:

- the active decision is simulated from an already recorded trajectory;
- requesting more does not change the world, only reveals more of the existing
  sample;
- utility is engineered from classifier support for the true label;
- no human reaction time, confidence, neural activity, or intervention is
  measured;
- the hybrid model receives raw persistence scores, so its win is expected but
  still informative.

The next step should use an external task where the next observation is chosen,
not merely revealed.

---

## Conclusion

E16, E17, and E18 now form a useful external ladder:

\[
\begin{array}{rcl}
\text{E16} &:& \text{static local evidence can absorb persistence;}\\
\text{E17} &:& \text{partial temporal recognition needs persistence;}\\
\text{E18} &:& \text{active sampling needs value plus persistence.}
\end{array}
\]

The sharper brain hypothesis is:

\[
\boxed{
\text{animal brains govern commitment by combining value of information with
persistent evidence.}
}
\]

