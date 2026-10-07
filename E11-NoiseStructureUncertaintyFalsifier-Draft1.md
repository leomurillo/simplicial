# E11 - Noise-Structure Uncertainty Falsifier

**Continuous Expected/Unexpected Uncertainty, Held-Out Boundary Evidence, and Structural Admission**

**Leonardo Murillo Montero**

**Draft 1**

---

> *Uncertainty explains gain. Held-out boundary evidence decides whether a
> residual becomes structure.*

---

## Status

E11 is the empirical falsifier for the next vulnerable B-series bucket family:
noise versus structure.

B10 corrected the current bucket. It showed that continuous temporal flow fits
directional magnitude, while a conformal gate controls false current admission.
E11 asks whether the same correction applies to stochastic residuals,
unexpected uncertainty, and structural closure.

The empirical companion is:

`empirical/e11_noise_structure_uncertainty_falsifier.py`

with reports:

- `empirical/reports/e11_noise_structure_uncertainty_falsifier.md`
- `empirical/reports/e11_noise_structure_uncertainty_falsifier.json`

---

## Abstract

**Situation.** B2 treated noise error and packet/chart structure as distinct
prediction-error buckets. B9 warned that ACh/NE-style expected and unexpected
uncertainty may explain much of this distinction continuously. B10 then showed
that a bucket may be an admission decision over a continuous variable rather
than the primitive neural variable itself.

**Task.** E11 tests whether noise-versus-structure survives a strong continuous
uncertainty rival. Synthetic episodes come from three worlds:

1. **noise world:** stochastic residual, no stable structure;
2. **uncertainty world:** unexpected volatility, no stable structure;
3. **structure world:** a stable hidden feature explains the residual.

All residuals are standardized so scalar surprise is approximately matched.
All worlds include train-only bait so train gain alone is untrustworthy.

**Action.** Models must solve two separate jobs:

1. predict graded precision/arousal response;
2. decide whether to admit structural closure.

The continuous rival receives expected uncertainty, unexpected uncertainty,
volatility, precision, and train-side gain. The bucket gate receives held-out
structural gain calibrated on nonstructure worlds.

**Result.**

\[
\boxed{
\text{UNCERTAINTY\_FITS\_BUT\_GATE\_RECOVERS\_STRUCTURE.}
}
\]

Continuous uncertainty wins graded precision prediction: RMSE \(0.065\) versus
\(0.165\) for the bucket gate. But the continuous rival detects only \(0.818\)
of real structures. The conformal held-out gate detects \(0.949\) of real
structures at \(0.050\) nonstructure false admission.

The pure bucket story weakens, but the governed-boundary story strengthens.

---

## The Falsifier

The early bucket table invited this reading:

\[
\text{noise error} \longrightarrow \text{suppress}
\]

and

\[
\text{structure error} \longrightarrow \text{close/rechart}.
\]

E11 tests a stronger rival:

\[
\text{noise and structure may be continuous expected/unexpected uncertainty plus gain control.}
\]

If a continuous uncertainty model predicts both graded response and structural
admission, the discrete noise-versus-structure bucket should be weakened. If
the bucket gate predicts both, the discrete route survives. If the two split
the task, the B-series must be refined.

They split the task.

---

## Synthetic Worlds

| World | Generator | Correct response |
|---|---|---|
| noise world | stochastic residual with expected uncertainty | suppress structural closure |
| uncertainty world | unexpected volatility without stable feature | raise precision response, do not close |
| structure world | stable hidden feature with held-out gain | admit boundary structure |

The hard case is the uncertainty world. It resembles structure through high
unexpected uncertainty, but has no stable held-out explanatory feature.

The anti-tautology pressure is train-only bait:

\[
\text{train gain is high in all worlds.}
\]

Therefore a model cannot call structure merely because a candidate feature
looks useful on the training sample.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | scalar surprise only | cannot route matched residuals |
| continuous uncertainty | expected/unexpected uncertainty, volatility, precision, train gain | may miss stable structure or confuse uncertainty with structure |
| bucket structure gate | conformal held-out structural admission | loses graded precision response |
| governed uncertainty gate | continuous uncertainty plus conformal structure gate | should split gain and closure |
| hybrid uncertainty-structure | continuous uncertainty plus held-out structural evidence | strongest composite rival |

The continuous rival is strong on purpose. It receives the neuromodulatory
style variables that an ACh/NE interpretation would naturally use.

The bucket model is also disciplined. It does not get semantic labels. It gets
only held-out gain over a conformal nonstructure threshold.

---

## Main Result

Default configuration:

- seed: `20260603`
- route/null trials: `900` / `450`
- main structure mix: `0.5`
- conformal alpha: `0.05`
- conformal structure gate: `0.044`

| Model | Precision RMSE | Structure accuracy | Structure detection | Nonstructure false admission |
|---|---|---|---|---|
| scalar | 0.195 | 0.663 | 0.000 | 0.000 |
| continuous uncertainty | 0.065 | 0.939 | 0.818 | 0.000 |
| bucket structure gate | 0.165 | 0.950 | 0.949 | 0.050 |
| governed uncertainty gate | 0.064 | 0.950 | 0.949 | 0.050 |
| hybrid uncertainty-structure | 0.064 | 0.950 | 0.949 | 0.050 |

This is the split:

\[
\begin{array}{rcl}
\text{continuous uncertainty} &:& \text{better gain prediction, conservative structure;}\\
\text{held-out gate} &:& \text{better structure recovery, calibrated false admission.}
\end{array}
\]

The continuous rival is not stupid. It remains conservative and avoids false
structure. But that conservatism costs sensitivity: it misses roughly \(18\%\)
of stable structures. The conformal gate accepts a \(5\%\) false-admission rate
and recovers roughly \(95\%\) of structures.

---

## Source Means

| Source | Scalar | Expected U | Unexpected U | Train gain | Held-out gain | Target precision | Target structure |
|---|---|---|---|---|---|---|---|
| structure world | 1.000 | 0.493 | 0.788 | 0.999 | 0.218 | 0.795 | 1.000 |
| uncertainty world | 1.000 | 0.505 | 0.770 | 0.999 | 0.018 | 0.723 | 0.000 |
| noise world | 1.000 | 0.754 | 0.127 | 0.999 | 0.018 | 0.378 | 0.000 |

The table shows why scalar and train gain are bad controls here. Scalar is
matched. Train gain is high everywhere. The difference between uncertainty and
structure lives in held-out boundary gain.

---

## Phase Sweep

The phase sweep varies the proportion of structure worlds among non-noise
route trials.

| Structure mix | Precision winner | Continuous precision | Bucket precision | Bucket false admission | Bucket detection |
|---|---|---|---|---|---|
| 0.000 | continuous uncertainty | 0.059 | 0.178 | 0.000 | nan |
| 0.250 | continuous uncertainty | 0.064 | 0.174 | 0.009 | 0.913 |
| 0.500 | governed uncertainty gate | 0.066 | 0.170 | 0.059 | 0.963 |
| 0.750 | governed uncertainty gate | 0.064 | 0.151 | 0.046 | 0.934 |
| 1.000 | governed uncertainty gate | 0.065 | 0.110 | 0.049 | 0.957 |

When there is no structure, continuous uncertainty wins cleanly. As structure
becomes more frequent, the governed models become more useful. That is the
right qualitative behavior: the experiment is not secretly wired to crown a
bucket in every world.

---

## Interpretation

E11 changes the noise-versus-structure bucket in the same direction that B10
changed the current bucket.

The older phrase was:

\[
\boxed{
\text{noise error and structure error are distinct buckets.}
}
\]

The updated phrase is:

\[
\boxed{
\text{noise/structure routing is continuous uncertainty under held-out admission.}
}
\]

In words: expected and unexpected uncertainty are probably closer to the
neuromodulatory substrate. They explain graded gain, arousal, and precision
response. But they do not by themselves decide when the organism should grow a
new representational packet. That decision needs held-out boundary evidence.

The bucket is therefore not the raw neural variable. The bucket is the
admission decision:

\[
\text{does this residual generalize as structure?}
\]

---

## Biological Prediction

E11 predicts a dissociation:

1. ACh/NE-like signals should track expected and unexpected uncertainty and
   predict graded precision response.
2. Structural admission should require evidence that an explanatory feature
   generalizes beyond the local sample.
3. Neural or behavioral signatures of closure should appear when held-out
   structure is stable, not merely when uncertainty is high.
4. Uncertainty-world episodes should raise gain without creating durable new
   representational packets.

In animal experiments, this suggests separating:

- neuromodulatory uncertainty response;
- stable feature emergence;
- train-only cue exploitation;
- held-out generalization;
- false packet admission.

The decisive measurement is not whether uncertainty rises. It is whether
uncertainty alone explains structural closure.

---

## Consequence for the B-Series

B10 and E11 now agree:

\[
\boxed{
\text{many buckets are governed admissions over continuous variables.}
}
\]

For current:

\[
\text{continuous flow} + \text{admission gate}.
\]

For noise versus structure:

\[
\text{continuous uncertainty} + \text{held-out boundary gate}.
\]

This is a more realistic brain hypothesis. Brains likely do not carry a tidy
lookup table of discrete buckets. They carry continuous fields of uncertainty,
flow, value, cost, and precision, then admit some of those fields into discrete
operations when the boundary evidence is good enough.

---

## What Would Falsify This Update

The governed-uncertainty update would fail if:

1. continuous uncertainty alone predicts graded gain and structural admission;
2. held-out boundary evidence adds no sensitivity at controlled false
   admission;
3. perturbing candidate structural admission circuits changes neither closure
   nor false packet learning;
4. uncertainty and structure cannot be separated under train-only bait.

If that happens, the B-series should demote the noise-versus-structure bucket
to a descriptive engineering discretization.

---

## Next Experimental Target

The next best falsifier is **E12: Ambiguity Versus Expected Information Gain**.
The question should be whether ambiguity/sampling is a distinct route, or
whether it is just continuous expected information gain plus a sampling-cost
gate. The experiment should let EIG win.

