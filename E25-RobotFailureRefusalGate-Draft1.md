# E25 - Robot Failure Refusal Gate

**External Failure-Cost Data After Action-Outcome Absorption**

**Leonardo Murillo Montero**

**Draft 1**

---

> *A refusal gate should earn its name where continuing is costly.*

---

## Status

E25 follows E24.

E24 used external Pioneer-1 action-outcome traces and still found no clean gate
residual. E25 moves to a sharper failure-cost setting: UCI Robot Execution
Failures.

Each instance is a 15-step force/torque sequence after failure detection during
a robot execution task. The operational decision is:

\[
\{\text{continue},\text{refuse/recover}\}.
\]

The empirical companion is:

`empirical/e25_robot_failure_refusal_gate_probe.py`

with reports:

- `empirical/reports/e25_robot_failure_refusal_gate_probe.md`
- `empirical/reports/e25_robot_failure_refusal_gate_probe.json`

Dataset source:

- `https://archive.ics.uci.edu/dataset/138/robot+execution+failures`
- `https://kdd.ics.uci.edu/databases/robotfailure/robotfailure.html`

---

## Abstract

**Situation.** E22 showed that a trained no-gate MLP absorbs the synthetic
closed-loop gate. E23 and E24 extended the absorption result to external robot
command imitation and action-outcome traces. E25 asks whether a gate reappears
when failure/refusal cost is explicit.

**Task.** The dataset contains `463` robot execution instances across five
learning problems. E25 treats `normal` and `ok` as safe continuation labels and
all other labels as failure/refusal labels:

\[
\text{safe} = \{\text{normal},\text{ok}\},
\]

\[
\text{failure} =
\text{collisions, obstructions, moved, lost, and related variants.}
\]

From prefixes of the force/torque trace, the agent chooses:

\[
\text{continue}
\quad\text{or}\quad
\text{refuse/recover}.
\]

**Result.**

\[
\boxed{
\text{ROBOT\_FAILURE\_MLP\_ABSORBS\_GATE\_WITH\_SAFETY\_HINT.}
}
\]

The no-gate continuous MLP wins on the primary policy metrics:

| Quantity | Continuous MLP | Hybrid MLP |
|---|---:|---:|
| action accuracy | 0.948 | 0.946 |
| mean regret | 0.080 | 0.081 |
| select RMSE | 0.222 | 0.301 |

The hybrid has a small safety-shaped edge:

| Quantity | Continuous MLP | Hybrid MLP |
|---|---:|---:|
| unsafe continue | 0.0217 | 0.0196 |
| false refusal | 0.0304 | 0.0348 |

So the gate behaves like a conservative refusal hint. It reduces unsafe
continuation slightly, but increases false refusal and does not improve
accuracy or regret.

---

## Dataset Audit

E25 uses all five UCI Robot Execution Failures learning problems:

| File | Instances | Safe | Failure |
|---|---:|---:|---:|
| LP1 | 88 | 21 | 67 |
| LP2 | 47 | 20 | 27 |
| LP3 | 47 | 20 | 27 |
| LP4 | 117 | 24 | 93 |
| LP5 | 164 | 44 | 120 |

Total:

| Class | Instances |
|---|---:|
| safe continue | 129 |
| failure/refuse | 334 |

Each instance has `15` force/torque samples with six channels. E25 uses prefix
lengths:

\[
3,6,9,12,15.
\]

The split is by instance, not prefix, so prefixes from the same execution never
cross train, calibration, and test.

Test split:

| Class | Instances |
|---|---:|
| safe | 26 |
| failure | 66 |

Prefix counts:

| Split | Prefixes |
|---|---:|
| train | 1385 |
| calibration | 470 |
| test | 460 |

The target is learnable: the probe test accuracy is `0.898` against a majority
baseline of `0.717`.

---

## Gate Definition

The gate is label-free at decision time.

First, a lightweight probe classifier estimates:

\[
p(\text{safe}\mid\text{force/torque prefix}),
\quad
p(\text{failure}\mid\text{force/torque prefix}).
\]

For each candidate action, the gate uses:

1. candidate probability;
2. candidate margin;
3. recent candidate stability;
4. entropy;
5. temporal anomaly energy.

The conformal threshold is calibrated on non-selected calibration packets.

The continuous MLP receives task and prefix features but no gate score or gate
bit. The hybrid MLP receives the same features plus gate score, margin,
stability, conformal bit, and bit-score interaction.

---

## Utility

E25 makes refusal cost explicit.

If the trace is safe:

\[
U(\text{continue}) = 1,
\]

\[
U(\text{refuse}) = -c_{\text{false refusal}}.
\]

If the trace is failure:

\[
U(\text{refuse}) = 1 - c_{\text{refusal}},
\]

\[
U(\text{continue}) = -c_{\text{unsafe continue}}.
\]

Default costs:

| Cost | Value |
|---|---:|
| unsafe continue | 1.00 |
| false refusal | 0.25 |
| refusal cost | 0.08 |

This is still a proxy, because the dataset provides labels rather than measured
reward. But it is the first E-series external anchor where continuing into
failure is explicitly penalized.

---

## Main Result

Default configuration:

- prefix lengths: `[3, 6, 9, 12, 15]`;
- hidden layers: `[72, 36]`;
- conformal alpha: `0.05`;
- gate threshold: `0.001`;
- instance-level stratified split by problem and safe/failure.

Model scores:

| Model | Features | Value RMSE | Select RMSE | Action acc | Regret | Unsafe continue | False refusal |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar MLP | 4 | 0.492 | 0.280 | 0.909 | 0.155 | 0.061 | 0.030 |
| continuous MLP | 64 | 0.401 | 0.222 | 0.948 | 0.080 | 0.022 | 0.030 |
| hybrid MLP | 69 | 0.432 | 0.301 | 0.946 | 0.081 | 0.020 | 0.035 |

The hybrid is marginally safer on unsafe continuation, but the no-gate
continuous MLP is better overall.

---

## Interpretation

E25 is the best place so far for a refusal gate to appear, because continuing
into failure is costly.

The result still does not support a clean gate residual.

It says:

\[
\text{failure/refusal is learnable from force/torque prefixes,}
\]

and:

\[
\text{a trained no-gate MLP absorbs the gate on primary policy metrics.}
\]

But it also says:

\[
\text{the gate shifts the policy slightly toward safer refusal.}
\]

That is a useful hint. It suggests that if a genuine brain-like gate exists, it
may show up not as better average prediction, but as a risk-preference or
asymmetric-cost effect:

\[
\text{avoid catastrophic continuation even at the cost of more false refusals.}
\]

E25 therefore narrows the target again. We should not look for a gate that beats
an MLP on generic accuracy. We should look for a gate that optimizes under
asymmetric cost, rare catastrophe, or irreversible commitment.

---

## Consequence for the B-Series Brain Program

The current empirical sequence is:

| Experiment | Anchor | Result |
|---|---|---|
| E22 | synthetic trained MLP | gate absorbed |
| E23 | external command imitation | absorbed with weak hybrid hint |
| E24 | external action-outcome traces | gate absorbed |
| E25 | external failure/refusal cost | absorbed with safety hint |

This is now a coherent correction:

\[
\boxed{
\text{ordinary learned prediction absorbs most engineered gates.}
}
\]

The remaining live hypothesis is narrower:

\[
\boxed{
\text{gates matter under asymmetric failure cost and irreversible boundary}
}
\]

\[
\boxed{
\text{crossing, not ordinary prediction.}
}
\]

For animal brains, the best candidates are now:

1. pain/withdrawal override;
2. startle/freeze inhibition;
3. stop-signal action cancellation;
4. sleep/wake transition;
5. working-memory admission under capacity;
6. irreversible social or motor commitment.

---

## Anti-Tautology Notes

Strengths:

- external robot failure data;
- explicit safe/failure labels;
- explicit continue/refuse utility;
- instance-level split prevents prefix leakage;
- trained no-gate MLP baseline;
- same-architecture hybrid MLP;
- unsafe continuation and false refusal are reported separately.

Limits:

- refusal utility is constructed from labels, not measured reward;
- normal/ok versus failure is a coarse binarization;
- the dataset is small;
- failure is already highly learnable from force/torque prefixes;
- the gate is engineered from the same prefix evidence;
- no real intervention policy is evaluated.

The honest takeaway:

\[
\boxed{
\text{E25 is not a gate win, but it identifies the right next pressure point.}
}
\]

The next experiment should vary asymmetric costs and ask whether the hybrid
becomes useful only in the rare-catastrophe regime.

