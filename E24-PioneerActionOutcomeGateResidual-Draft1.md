# E24 - Pioneer Action-Outcome Gate Residual

**External Robot Experiences After the MLP Absorber**

**Leonardo Murillo Montero**

**Draft 1**

---

> *The next external anchor has to carry action effects, not just command
> labels. E24 gets closer, and the gate still does not survive.*

---

## Status

E24 follows E23.

E23 used UCI Wall-Following robot data. That was external and sequential, but
it was still command imitation. E24 moves to the UCI KDD Pioneer-1 Mobile Robot
Data, where traces are organized as experiences:

\[
\text{robot action} \quad\rightarrow\quad \text{controlled interaction}
\quad\rightarrow\quad \text{qualitative outcome}.
\]

The empirical companion is:

`empirical/e24_pioneer_action_outcome_gate_residual_probe.py`

with reports:

- `empirical/reports/e24_pioneer_action_outcome_gate_residual_probe.md`
- `empirical/reports/e24_pioneer_action_outcome_gate_residual_probe.json`

Dataset source:

- `https://kdd.ics.uci.edu/databases/pioneer/pioneer.html`
- `https://kdd.ics.uci.edu/databases/pioneer/pioneer.data.html`

---

## Abstract

**Situation.** E22 showed that a trained no-gate MLP absorbs the synthetic
closed-loop gate. E23 found the same pattern on external command imitation,
with only a weak hybrid hint. E24 asks whether action-outcome experience traces
show a stronger residual.

**Task.** E24 uses the `move` and `turn` Pioneer-1 files. Each trial is a
sensorimotor experience. The model sees prefixes of the time series and predicts
the final qualitative outcome:

\[
\{\text{clear\_visible},\text{obstructed},\text{discover},
\text{vanish},\text{push}\}.
\]

The outcome labels are parsed from the dataset description strings. The outcome
markers are used only as targets, not predictor features.

**Result.**

\[
\boxed{
\text{PIONEER\_MLP\_ABSORBS\_GATE.}
}
\]

The target is learnable under a stratified trial split: probe test accuracy is
`0.664` against `0.300` majority accuracy. But the trained no-gate MLP beats the
hybrid on the main policy quantities:

| Quantity | Continuous MLP | Hybrid MLP |
|---|---:|---:|
| action accuracy | 0.672 | 0.662 |
| mean regret | 0.388 | 0.399 |
| unsafe wrong proxy | 0.103 | 0.099 |
| severe miss proxy | 0.049 | 0.041 |
| select RMSE | 0.379 | 0.342 |

The hybrid improves the safety proxies and select-RMSE, but it loses on action
accuracy and regret. Therefore this is not a gate-residual result.

---

## Dataset Audit

The UCI KDD description says the data are multivariate time series from
Pioneer-1 experiences in which the robot takes action and undergoes controlled
interactions with the environment.

E24 uses:

| File | Role |
|---|---|
| `move.data.gz` | moving forward or retreating experiences |
| `turn.data.gz` | turning experiences |

The gripper file is excluded in E24 because it has only `16` trials and a
different action semantics.

Trial counts:

| Outcome | Trials |
|---|---:|
| clear_visible | 36 |
| obstructed | 30 |
| discover | 22 |
| vanish | 16 |
| push | 40 |

The default split is stratified by file and outcome, and split by trial rather
than row. This prevents prefixes from the same experience crossing train,
calibration, and test.

Test split:

| Outcome | Test trials |
|---|---:|
| clear_visible | 7 |
| obstructed | 6 |
| discover | 4 |
| vanish | 3 |
| push | 8 |

Prefix counts:

| Split | Prefix examples |
|---|---:|
| train | 1490 |
| calibration | 517 |
| test | 467 |

Each prefix becomes five candidate outcome packets.

---

## Gate Definition

The gate is label-free at decision time.

First, a lightweight probe classifier predicts outcome probabilities from
prefix features. For each candidate outcome, the gate uses:

1. candidate probability;
2. candidate margin;
3. recent candidate stability within the same trial;
4. prefix entropy;
5. effect-energy smoothness.

The conformal threshold is calibrated on non-selected calibration packets.

The continuous MLP receives prefix sensor/action features and candidate outcome
identity. The hybrid MLP receives the same features plus gate score, stability,
margin, conformal bit, and bit-score interaction.

---

## Main Result

Default configuration:

- min prefix: `8`;
- prefix stride: `3`;
- stability history: `5`;
- split strategy: `stratified`;
- hidden layers: `[80, 40]`;
- conformal alpha: `0.05`;
- gate threshold: `0.002`.

Model scores:

| Model | Features | Value RMSE | Select RMSE | Action acc | Regret | Unsafe wrong | Severe miss |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar MLP | 7 | 0.421 | 0.352 | 0.668 | 0.392 | 0.103 | 0.041 |
| continuous MLP | 276 | 0.420 | 0.379 | 0.672 | 0.388 | 0.103 | 0.049 |
| hybrid MLP | 281 | 0.424 | 0.342 | 0.662 | 0.399 | 0.099 | 0.041 |

The hybrid is more conservative on safety proxies, but it does not improve the
primary selection result. The no-gate MLP absorbs the gate under the configured
standard.

---

## Interpretation

E24 is a stronger external anchor than E23, but it still does not produce a
gate residual.

The result says:

\[
\text{external action-outcome traces are learnable,}
\]

but:

\[
\text{the label-free gate does not beat a trained nonlinear no-gate model.}
\]

This continues the E22-E23 correction. A gate feature can help a diagnostic
metric without becoming a separate boundary mechanism.

For the brain hypothesis, E24 says:

\[
\boxed{
\text{even external action-outcome prediction may be absorbed by learned}
}
\]

\[
\boxed{
\text{state-action dynamics.}
}
\]

So the B-series should keep narrowing the claim. The likely place for a genuine
gate is not ordinary qualitative outcome prediction. It is where an organism
faces an irreversible, costly, capacity-limited, or inhibitory transition.

---

## Consequence for the Empirical Ladder

The current ladder now looks like this:

| Experiment | Anchor | Result |
|---|---|---|
| E20 | synthetic closed-loop action | hybrid initially wins |
| E21 | stronger absorbers | E20 capacity confound |
| E22 | trained no-gate MLP | synthetic gate absorbed |
| E23 | external command imitation | absorbed with weak hybrid hint |
| E24 | external action-outcome traces | gate absorbed |

This is a useful negative sequence. It prevents the brain program from
mistaking engineered gate features for irreducible mechanisms.

The next target should not be another ordinary prediction dataset. It should
contain at least one of:

1. explicit failure cost;
2. irreversible commitment;
3. collision or damage labels;
4. delayed outcome after action;
5. capacity-limited memory admission;
6. explicit inhibit/act choices.

That is where a boundary gate has a fair chance to be more than a coordinate
inside prediction.

---

## Anti-Tautology Notes

Strengths:

- external UCI KDD Pioneer-1 robot experience data;
- action-outcome traces rather than command imitation only;
- trial-level splitting prevents prefix leakage;
- stratification keeps rare outcomes represented;
- trained no-gate MLP baseline;
- same-architecture hybrid MLP;
- outcome markers are excluded from predictor features;
- safety proxies are reported separately from action accuracy and regret.

Limits:

- the labels are qualitative descriptions, not measured reward;
- the split is stratified, not chronological;
- the target taxonomy is parsed from description strings;
- gripper experiences are excluded;
- the gate threshold is small;
- the scalar/probe path is already fairly strong;
- no explicit policy exploration is learned.

The honest takeaway:

\[
\boxed{
\text{E24 is a better external anchor, and still a negative gate result.}
}
\]

The next positive test must involve real cost, inhibition, or irreversible
boundary crossing.

