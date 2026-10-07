# E19 - Selective PenDigits Glimpse

**Choosing Where to Sample**

**Leonardo Murillo Montero**

**Draft 1**

---

> *A brain hypothesis that wins every probe is probably measuring its own
> vocabulary. E19 is a negative anchor.*

---

## Status

E19 follows E18's active PenDigits sampling result.

E18 asked whether an agent should commit now or request the completed stroke.
E19 makes the active question more local:

\[
\text{if the agent may inspect only one future point, where should it look?}
\]

The empirical companion is:

`empirical/e19_selective_pendigits_glimpse_probe.py`

with reports:

- `empirical/reports/e19_selective_pendigits_glimpse_probe.md`
- `empirical/reports/e19_selective_pendigits_glimpse_probe.json`

The data source remains the UCI Pen-Based Recognition of Handwritten Digits
dataset:

`https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits`

---

## Abstract

**Situation.** E17 found that temporal persistence can govern admission when
the agent sees only an early pen-trajectory prefix. E18 found that active
commit/request control benefits from a hybrid of sampling value and temporal
admission.

**Task.** E19 tests a sharper selective-sampling task. From the first two
trajectory points, the agent must choose exactly one action:

\[
\{\text{commit}, p_3, p_4, p_5, p_6, p_7, p_8\}.
\]

Here \(p_k\) means: inspect the \(k\)-th trajectory point and then evaluate the
digit with that action packet. Each sample action pays a distance-sensitive
cost. The target action is the packet with maximal true-label support minus
cost.

**Result.**

\[
\boxed{
\text{SELECTIVE\_SAMPLING\_CONTINUOUS\_ACTION\_VALUE\_ABSORBS\_GATE.}
}
\]

This is a negative anchor for the broadest governance claim. On this task, the
continuous action-value model already captures almost all useful structure:

| Quantity | Continuous value | Gate | Hybrid |
|---|---:|---:|---:|
| value RMSE | 0.015 | 0.018 | 0.015 |
| action accuracy | 0.690 | 0.523 | 0.698 |
| mean regret | 0.002 | 0.003 | 0.002 |
| false commit | 0.219 | 0.477 | 0.202 |
| wrong sample | 0.045 | 0.000 | 0.049 |

The hybrid gives a small action-accuracy improvement over continuous value, but
it does not improve regret. The pure gate is too conservative and behaves close
to a commit-biased policy in the main-cost regime.

Therefore E19 supports the correction:

\[
\boxed{
\text{not every active sampling decision needs an admission gate.}
}
\]

---

## Experimental Design

Each PenDigits example contains eight \((x,y)\) trajectory points.

E19 uses:

| Component | Role |
|---|---|
| first two points | initial evidence field |
| commit | act on the early prefix |
| \(p_3,\ldots,p_8\) | inspect exactly one future point |
| sample cost | base cost plus distance penalty |
| utility | true-label packet support minus action cost |
| conformal gate | calibrated on non-optimal action packets |
| policy score | choose one action per held-out trajectory |

The conformal gate is label-free at decision time. It uses packet confidence,
margin, and entropy to admit or reject candidate action packets. Labels enter
only in the offline utility target used to score the experiment.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | action confidence plus action identity | crude commit/sample bias |
| continuous action value | packet probabilities, geometry, action identity, cost | may absorb gate |
| conformal action gate | action identity plus conformal admission bit | too conservative |
| governed action | continuous field plus gate bit | should help if admission matters |
| hybrid full | continuous field plus raw gate scores | strongest combined model |

E19 uses a lightweight local quadratic ridge basis without all-pairs
interactions. This keeps the action-packet probe reproducible on the full
train/calibration/test split.

---

## Main Result

Default configuration:

- seed: `20260603`
- train/calibration/test episodes: `5620` / `1874` / `3498`
- packets per test episode: `7`
- early points: `2`
- actions: `commit, p3, p4, p5, p6, p7, p8`
- base sampling cost: `0.010`
- distance cost: `0.003`
- conformal alpha: `0.05`

At the main cost, the optimal held-out actions were:

| Action | Optimal count |
|---|---:|
| commit | 1829 |
| p3 | 576 |
| p4 | 157 |
| p5 | 418 |
| p6 | 183 |
| p7 | 81 |
| p8 | 254 |

Model scores:

| Model | Value RMSE | Value R2 | Action acc | Regret | P90 regret | False commit | False sample | Wrong sample |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| scalar | 0.016 | 0.365 | 0.523 | 0.003 | 0.011 | 0.477 | 0.000 | 0.000 |
| continuous action value | 0.015 | 0.435 | 0.690 | 0.002 | 0.007 | 0.219 | 0.047 | 0.045 |
| conformal action gate | 0.018 | 0.209 | 0.523 | 0.003 | 0.011 | 0.477 | 0.000 | 0.000 |
| governed action | 0.015 | 0.435 | 0.698 | 0.002 | 0.007 | 0.202 | 0.051 | 0.049 |
| hybrid full | 0.015 | 0.434 | 0.698 | 0.002 | 0.007 | 0.202 | 0.051 | 0.049 |

The result is not a gate win. The gate reduces wrong samples by avoiding
sampling, but it pays for that conservatism with many false commits. The
continuous action-value model already tracks which future point is worth
sampling.

---

## Cost Sweep

| Base cost | Optimal regime | Continuous acc | Gate acc | Hybrid acc | Continuous regret | Gate regret | Hybrid regret |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0.000 | sample-rich | 0.625 | 0.321 | 0.629 | 0.003 | 0.006 | 0.003 |
| 0.010 | mixed commit/sample | 0.690 | 0.523 | 0.698 | 0.002 | 0.003 | 0.002 |
| 0.040 | commit-dominant | 0.999 | 0.999 | 0.999 | 0.000 | 0.000 | 0.000 |

The middle-cost regime is the real test. Cheap evidence makes sampling common;
expensive evidence makes commit nearly universal. In the middle regime,
continuous value and hybrid value tie on regret.

---

## Interpretation

E19 sharpens the brain hypothesis by denying an overgeneralization.

The earlier wording could tempt us toward:

\[
\text{prediction error management always needs a governance gate.}
\]

E19 says no. When the active action is just choosing one fixed future glimpse
from an already recorded trajectory, ordinary action-value prediction is enough.
The gate has no independent burden to carry.

The positive claim should therefore be narrower:

\[
\boxed{
\text{admission gates matter when action changes commitment, persistence,}
}
\]

\[
\boxed{
\text{or boundary ownership, not when action merely indexes evidence.}
}
\]

This distinction is valuable for the B-series brain program. Brains probably do
not gate every sensory look. They gate transitions where evidence becomes
commitment: belief update, motor issue, tool request, compression, refusal, or
other boundary-changing acts.

---

## Anti-Tautology Notes

E19 is externally anchored:

- it uses UCI pen-trajectory data, not synthetic STAR traces;
- the action set changes which future point is observed;
- the policy is scored by held-out regret, not just row-wise fit;
- the cost sweep includes cheap, mixed, and expensive sampling regimes.

But the probe is still limited:

- the action does not alter the world or the future trajectory;
- utility is derived from classifier true-label support;
- all candidate glimpses already exist offline;
- the gate score is a simple confidence/margin/entropy construction;
- the continuous model sees rich packet features, so absorption is a serious
  possibility by design.

For that reason, E19 should be treated as a negative anchor and design guide,
not as a rejection of E17 or E18.

---

## Consequence for the Brain Hypothesis

E19 gives the first clean empirical boundary around the B-series idea:

1. **Evidence indexing** can be managed by action-value fields.
2. **Commitment admission** needs persistence-sensitive governance.
3. **Active control** becomes hybrid when sampling and commitment are coupled.

The animal brain version should not say:

\[
\text{all prediction errors route through the same gate.}
\]

It should say:

\[
\text{prediction errors become governed when they cross a boundary of act,}
\]

\[
\text{belief, memory, compression, refusal, or costly external sampling.}
\]

E19 is the reminder that a good theory must know when its favorite mechanism is
unnecessary.

