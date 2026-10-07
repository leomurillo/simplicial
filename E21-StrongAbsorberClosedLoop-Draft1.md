# E21 - Strong Absorber Closed Loop

**Does the E20 Gate Survive a Better Value Model?**

**Leonardo Murillo Montero**

**Draft 1**

---

> *A governance result is not serious until the continuous absorber has had a
> fair chance to eat it.*

---

## Status

E21 is the immediate falsifier for E20.

E20 found that a hybrid value-governance policy beat a lightweight continuous
value model on a closed-loop motor-sensing task. But the E20 continuous model
used only a lightweight quadratic basis. That left a serious concern:

\[
\text{did governance win, or did capacity lose?}
\]

The empirical companion is:

`empirical/e21_strong_absorber_closed_loop_probe.py`

with reports:

- `empirical/reports/e21_strong_absorber_closed_loop_probe.md`
- `empirical/reports/e21_strong_absorber_closed_loop_probe.json`

---

## Abstract

**Situation.** E20 made action part of the transition function:

\[
s_1 = F(s_0,a,y,\epsilon).
\]

The hybrid policy won over a lightweight continuous value model. E21 asks
whether that win survives stronger no-gate absorbers.

**Task.** The simulator, action set, and utility structure are inherited from
E20. The model class changes. E21 compares:

1. lightweight continuous value;
2. full pairwise quadratic continuous value;
3. random-feature MLP-style continuous value;
4. lightweight hybrid value-governance;
5. random-feature hybrid value-governance.

**Result.**

\[
\boxed{
\text{E20\_CAPACITY\_CONFOUND\_WITH\_HYBRID\_EDGE.}
}
\]

The strong continuous absorber erases most of the E20 hybrid-lite advantage:

| Quantity | Continuous lite | Continuous pairwise | Hybrid lite | Hybrid random |
|---|---:|---:|---:|---:|
| action accuracy | 0.636 | 0.763 | 0.723 | 0.784 |
| mean regret | 0.257 | 0.148 | 0.167 | 0.146 |
| unnecessary unsafe | 0.260 | 0.155 | 0.175 | 0.152 |
| value RMSE | 0.308 | 0.264 | 0.299 | 0.266 |

The best no-gate continuous model is `continuous_pairwise`. The best hybrid is
`hybrid_random_absorber`.

The hybrid keeps a small action-accuracy edge:

\[
0.784 - 0.763 = 0.021,
\]

but the regret gap is tiny:

\[
0.148 - 0.146 = 0.002.
\]

Therefore E21 does **not** support the strong reading of E20. It supports a
weaker and more honest reading:

\[
\boxed{
\text{closed-loop governance is capacity-sensitive, with at most a weak}
}
\]

\[
\boxed{
\text{hybrid edge under this absorber test.}
}
\]

---

## Experimental Design

E21 uses the E20 synthetic closed-loop motor-sensing field.

The agent sees an ambiguous early state and evaluates six candidate actions:

\[
\{\text{commit},\text{hold},\text{aim}_0,\text{aim}_1,\text{aim}_2,\text{aim}_3\}.
\]

Each action produces its own post-action state. Wrong controls can deform or
rupture the future evidence. Utility rewards true-label post-action support and
penalizes action cost, rupture, and unsafe transitions.

E21 changes only model capacity.

---

## Models Compared

| Model | Gate? | Basis | Expanded features | Purpose |
|---|---|---|---:|---|
| scalar lite | no | confidence/cost/action | 17 | crude baseline |
| gate lite | yes | conformal bit/action | 27 | pure admission baseline |
| continuous lite | no | local quadratic | 87 | E20 continuous baseline |
| continuous pairwise | no | full pairwise quadratic | 990 | strong absorber |
| continuous random absorber | no | random nonlinear features | 471 | MLP-style absorber |
| hybrid lite | yes | local quadratic plus gate | 109 | E20 hybrid baseline |
| hybrid random absorber | yes | random nonlinear plus gate | 493 | capacity-matched hybrid |

The critical comparison is:

\[
\text{best strong continuous}
\quad\text{vs.}\quad
\text{best hybrid}.
\]

A governance win is not counted merely because hybrid beats `continuous_lite`.
It must beat the best no-gate absorber.

---

## Main Result

Default configuration:

- seed: `20260603`
- train/calibration/test episodes: `5200` / `1800` / `3000`
- aim cost: `0.040`
- hold cost: `0.018`
- random hidden features: `384`
- conformal alpha: `0.05`
- gate threshold: `0.803`

At the main cost, the optimal held-out actions were:

| Action | Optimal count |
|---|---:|
| commit | 709 |
| hold | 322 |
| aim_0 | 499 |
| aim_1 | 518 |
| aim_2 | 457 |
| aim_3 | 495 |

Model scores:

| Model | Value RMSE | Value R2 | Action acc | Regret | P90 regret | Unsafe choice | Unnecessary unsafe |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar lite | 0.362 | 0.436 | 0.542 | 0.362 | 1.096 | 0.360 | 0.358 |
| gate lite | 0.417 | 0.252 | 0.374 | 0.577 | 1.124 | 0.569 | 0.568 |
| continuous lite | 0.308 | 0.593 | 0.636 | 0.257 | 1.022 | 0.261 | 0.260 |
| continuous pairwise | 0.264 | 0.700 | 0.763 | 0.148 | 0.947 | 0.156 | 0.155 |
| continuous random absorber | 0.273 | 0.680 | 0.728 | 0.166 | 0.973 | 0.173 | 0.172 |
| hybrid lite | 0.299 | 0.615 | 0.723 | 0.167 | 0.952 | 0.176 | 0.175 |
| hybrid random absorber | 0.266 | 0.695 | 0.784 | 0.146 | 0.961 | 0.153 | 0.152 |

The decisive correction is this:

\[
\text{continuous pairwise} \approx \text{hybrid random}
\]

on regret and unsafe action.

Hybrid random has the best action accuracy, but the advantage is not large
enough to restore E20's strong conclusion.

---

## Interpretation

E21 is not a collapse of the B-series brain hypothesis. It is a correction of
an overconfident empirical step.

E20's result should no longer be stated as:

\[
\text{closed-loop intervention requires governance.}
\]

It should be stated as:

\[
\text{closed-loop intervention exposes a governance-like feature, but}
\]

\[
\text{strong continuous absorbers can capture much of it.}
\]

This matters. A biological brain does not choose between "continuous value" and
"gate" as toy model columns. It has recurrent nonlinear absorbers everywhere.
So if a gate-like effect disappears under nonlinear value learning, the theory
must not count it as evidence for a distinct governance layer.

E21 tells us the next standard:

\[
\boxed{
\text{a brain-relevant gate must beat a strong learned absorber,}
}
\]

or else it should be reinterpreted as a coordinate choice inside value learning.

---

## Consequence for the Bucket Rule

After E21, the prediction-error management buckets should be more cautious.

| Context | Earlier reading | E21 correction |
|---|---|---|
| passive evidence | value-guided sampling | unchanged |
| static local evidence | continuous update | unchanged |
| commitment | admission gate | still plausible |
| closed-loop action | hybrid governance | capacity-sensitive |
| unsafe intervention | safety/refusal | must beat nonlinear absorber |

The corrected rule:

\[
\text{do not infer a separate management bucket from a weak baseline.}
\]

Instead:

1. test scalar surprise;
2. test lightweight continuous value;
3. test strong nonlinear continuous absorption;
4. only then test whether a gate adds irreducible policy value.

That gives the B-series a better empirical discipline.

---

## Anti-Tautology Notes

Strengths:

- the simulator and task are identical to E20;
- strong no-gate absorbers are explicitly included;
- the pairwise absorber has `990` expanded features;
- the random absorber supplies MLP-style nonlinear features;
- the hybrid random absorber has comparable capacity;
- the finding is scored against the best strong continuous baseline.

Limits:

- the task remains synthetic;
- the random absorber is not a fully trained neural network;
- the pairwise absorber may still miss higher-order temporal structure;
- the hybrid feature set still explicitly contains the gate construction;
- the split size is smaller than E20 to make the strong absorber run practical;
- no external animal or neural dataset is involved.

The honest takeaway:

\[
\boxed{
\text{E21 weakens E20 and improves the program.}
}
\]

It tells us that the next meaningful positive result must survive a stronger
absorber on either an external sequential-control dataset or a more realistic
closed-loop simulator.

