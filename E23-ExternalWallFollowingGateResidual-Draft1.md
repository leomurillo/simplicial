# E23 - External Wall-Following Gate Residual

**A Robot Navigation Anchor After the MLP Absorber**

**Leonardo Murillo Montero**

**Draft 1**

---

> *The first external anchor should not be asked to prove the theory. It should
> teach the theory what kind of evidence it deserves.*

---

## Status

E23 follows the E22 correction.

E22 showed that a trained no-gate MLP absorbs the synthetic closed-loop gate.
That raised the standard:

\[
\text{a gate-like residual must survive trained nonlinear prediction.}
\]

E23 moves from the synthetic simulator to an external sequential robot dataset:
the UCI Wall-Following Robot Navigation Data.

The empirical companion is:

`empirical/e23_external_wall_following_gate_residual_probe.py`

with reports:

- `empirical/reports/e23_external_wall_following_gate_residual_probe.md`
- `empirical/reports/e23_external_wall_following_gate_residual_probe.json`

Dataset source:

- `https://archive-beta.ics.uci.edu/dataset/194/wall+following+robot+navigation+data`
- `https://doi.org/10.24432/C57C8W`

---

## Abstract

**Situation.** E20 produced a synthetic hybrid-governance result. E21 weakened
it with stronger absorbers. E22 showed that a trained nonlinear no-gate model
absorbs the synthetic gate. E23 asks whether an external robot sequence shows a
gate-like residual.

**Task.** The dataset contains `5456` rows of robot wall-following behavior.
Each row has `24` ultrasound sensor readings and one command label:

\[
\{\text{Move-Forward},\text{Slight-Left-Turn},
\text{Slight-Right-Turn},\text{Sharp-Right-Turn}\}.
\]

E23 builds short chronological sensor-history windows and scores candidate
command packets. It compares:

1. a trained no-gate continuous MLP;
2. the same MLP plus label-free temporal gate features.

**Result.**

\[
\boxed{
\text{EXTERNAL\_MLP\_ABSORBS\_GATE\_WITH\_WEAK\_HYBRID\_EDGE.}
}
\]

The external task is learnable. A simple probe reaches `0.845` chronological
test accuracy against `0.390` majority accuracy.

The hybrid keeps a small edge:

| Quantity | Continuous MLP | Hybrid MLP |
|---|---:|---:|
| action accuracy | 0.861 | 0.869 |
| mean regret | 0.171 | 0.161 |
| unsafe wrong proxy | 0.091 | 0.086 |
| boundary error | 0.069 | 0.063 |
| select RMSE | 0.236 | 0.224 |

But the gain is below the configured survival margins. Therefore E23 is not a
positive gate-residual result. It is an external absorption result with a weak
hybrid hint.

---

## Dataset Audit

The data are external and sequential, but not a causal intervention log.

The command distribution is:

| Command | Count |
|---|---:|
| Move-Forward | 2205 |
| Slight-Left-Turn | 328 |
| Slight-Right-Turn | 826 |
| Sharp-Right-Turn | 2097 |

The command change rate is `0.072`, so the sequence is temporally persistent.
This makes it a plausible place to test whether a temporal gate helps, but also
means a strong predictor can exploit local continuity.

Chronological split:

| Split | Row bounds | Windows |
|---|---|---:|
| train | 0-3274 | 3270 |
| calibration | 3274-4365 | 1087 |
| test | 4365-5456 | 1087 |

The split is chronological, not random. This matters because random splitting
would overstate performance on a persistent control sequence.

---

## Gate Definition

The gate is label-free at decision time.

First, a lightweight probe classifier predicts command probabilities from the
sensor history. For each candidate command, the gate uses:

1. candidate probability;
2. candidate margin against other commands;
3. recent temporal stability of that candidate;
4. command entropy;
5. sensor-history smoothness.

The gate score is calibrated on non-selected calibration command packets.

The hybrid MLP receives the continuous features plus:

- gate score;
- stability;
- gate margin;
- conformal gate bit;
- gate-bit interaction with scalar score.

The no-gate continuous MLP receives no gate score or gate bit.

---

## Main Result

Default configuration:

- history window: `5`;
- stability history: `7`;
- hidden layers: `[80, 40]`;
- conformal alpha: `0.05`;
- gate threshold: approximately `0.000`;
- unsafe penalty: `0.35`;
- command-regret proxy, not causal intervention regret.

Model scores:

| Model | Features | Value RMSE | Select RMSE | Action acc | Regret | Unsafe wrong | Boundary error |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar MLP | 6 | 0.303 | 0.223 | 0.857 | 0.176 | 0.095 | 0.076 |
| continuous MLP | 256 | 0.313 | 0.236 | 0.861 | 0.171 | 0.091 | 0.069 |
| hybrid MLP | 261 | 0.309 | 0.224 | 0.869 | 0.161 | 0.086 | 0.063 |

The scalar result is already strong because the probe confidence is informative.
The continuous MLP improves slightly. The hybrid improves again, but not enough
to clear the stronger post-E22 standard.

---

## Interpretation

E23 is not a clean gate win.

It says:

\[
\text{external sequential robot data contain a weak gate-like hint,}
\]

but:

\[
\text{a trained no-gate MLP absorbs most of it.}
\]

That is the correct direction of pressure after E22. The theory is no longer
allowed to count any helpful gate feature as a separate management bucket.

For the brain hypothesis, E23 suggests:

\[
\boxed{
\text{ordinary sensorimotor command prediction may not require a distinct}
}
\]

\[
\boxed{
\text{admission gate once nonlinear prediction is available.}
}
\]

The remaining weak hybrid edge is interesting, but not yet decisive. It may be:

1. a real temporal-boundary residue;
2. a feature-engineering advantage;
3. a calibration artifact;
4. a consequence of command persistence;
5. an unsafe-proxy artifact.

E23 therefore strengthens the standard of evidence rather than the hypothesis
itself.

---

## Consequence for the B-Series Brain Program

After E23, the empirical ladder becomes:

1. synthetic toy separation;
2. synthetic strong-absorber falsifier;
3. trained no-gate nonlinear absorber;
4. external sequential imitation anchor;
5. external causal or reinforcement-learning anchor.

E23 occupies step 4, but only weakly. It is sequential and external, but it is
still command imitation. The action labels do not prove that selected commands
changed the future state in the logged sequence.

Therefore the corrected bucket rule is:

| Context | Current status |
|---|---|
| static evidence | continuous update remains enough |
| offline sampling | continuous action value often enough |
| synthetic closed-loop action | gate absorbed by trained MLP |
| external command imitation | gate mostly absorbed, weak hybrid hint |
| external causal control | still untested |

The next real target should involve action, outcome, and failure cost in the
same external record.

---

## Anti-Tautology Notes

Strengths:

- external UCI robot navigation data;
- chronological split;
- trained no-gate MLP baseline;
- same-architecture hybrid MLP;
- label-free temporal gate features;
- command-regret and unsafe-command proxy reported separately;
- majority and probe baselines audited.

Limits:

- not a causal intervention dataset;
- no direct collision or damage labels;
- unsafe-command is a proxy derived from command mismatch severity;
- the gate threshold is near zero because non-selected candidate scores are
  heavily concentrated near zero;
- command persistence may help both gate and no-gate models;
- the scalar probe is already strong, which reduces room for residual gains.

The honest takeaway:

\[
\boxed{
\text{E23 gives us an external anchor, not a gate residual.}
}
\]

The next external test must involve real action-outcome coupling.

