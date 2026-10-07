# E20 - Closed-Loop Motor Sensing

**When Action Changes the Future State**

**Leonardo Murillo Montero**

**Draft 1**

---

> *A look is not yet an intervention. E20 makes the action change what can be
> seen next.*

---

## Status

E20 follows the E19 negative anchor.

E19 tested selective sampling on PenDigits, but every possible future glimpse
already existed in the offline trajectory. The action selected evidence. It did
not alter the future.

E20 changes that:

\[
\text{same early state} + \text{different action}
\quad\Rightarrow\quad
\text{different future state.}
\]

The empirical companion is:

`empirical/e20_closed_loop_motor_sensing_probe.py`

with reports:

- `empirical/reports/e20_closed_loop_motor_sensing_probe.md`
- `empirical/reports/e20_closed_loop_motor_sensing_probe.json`

---

## Abstract

**Situation.** E19 showed that a continuous action-value field can absorb the
admission gate when the action merely chooses an offline glimpse. This was a
useful failure: it said the brain hypothesis must not claim that every active
sampling decision needs governance.

**Task.** E20 asks whether governance reappears when action is a true
intervention. A synthetic four-class motor-sensing field generates ambiguous
early evidence. The agent can:

\[
\{\text{commit}, \text{hold}, \text{aim}_0,\text{aim}_1,\text{aim}_2,\text{aim}_3\}.
\]

The `aim_k` actions push the future state toward basin \(k\). If the action is
wrong, it can deform or rupture the post-action evidence. Thus action changes
the future state before utility is scored.

**Result.**

\[
\boxed{
\text{CLOSED\_LOOP\_HYBRID\_GOVERNANCE\_NEEDED.}
}
\]

At the main intervention cost, the hybrid policy beats continuous value and the
pure gate:

| Quantity | Continuous value | Gate | Hybrid |
|---|---:|---:|---:|
| value RMSE | 0.310 | 0.418 | 0.302 |
| action accuracy | 0.644 | 0.368 | 0.720 |
| mean regret | 0.242 | 0.591 | 0.164 |
| unnecessary unsafe action | 0.243 | 0.577 | 0.172 |
| missed control | 0.033 | 0.058 | 0.060 |

The gate alone is not a policy. It is too conservative in some regimes and too
coarse in others. But the hybrid model uses boundary-persistence information to
reduce regret and unsafe control choices.

Therefore E20 supports:

\[
\boxed{
\text{when action changes the future state, value needs governance.}
}
\]

---

## Experimental Design

E20 is synthetic by design. The aim is not external anchoring. The aim is to
isolate the closed-loop feature missing from E19.

Each episode has:

| Component | Meaning |
|---|---|
| latent class | correct sensorimotor basin |
| early state | ambiguous evidence mixture |
| commit | act on early evidence without transition |
| hold | passive drift toward the true basin |
| aim actions | active push toward one basin |
| rupture | wrong control can deform the future state |
| utility | true-label post-action support minus cost and unsafe penalties |
| gate | label-free boundary persistence under the action |

The same early state is evaluated under all candidate actions. The future state
is generated separately for each action:

\[
s_1 = F(s_0, a, y, \epsilon).
\]

This is the crucial difference from E19. The action enters the transition
function.

---

## Gate Definition

The gate is not allowed to see the true label at decision time. It sees:

1. whether the post-action prediction preserves the early boundary;
2. whether the action is aligned with that early boundary;
3. post-action confidence, margin, entropy, and smoothness.

Its score is then conformally calibrated on held-out non-optimal action packets.

This makes the gate an admission rule over intervention packets:

\[
\text{admit}(s_0,a,s_1)
\]

rather than a classifier for the latent class.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | post-action confidence, cost, action identity | crude confidence policy |
| continuous transition value | rich pre/post state, probabilities, action, cost | may absorb gate |
| conformal transition gate | action identity plus admission bit | too coarse alone |
| governed transition | continuous field plus gate bit | should reduce unsafe interventions |
| hybrid full | continuous field plus raw gate scores | strongest closed-loop controller |

The continuous model receives rich post-action evidence. The hybrid win is
therefore not automatic. However, E20 still uses a lightweight quadratic ridge
basis without all-pairs interactions. A stronger absorber is the next falsifier.

---

## Main Result

Default configuration:

- seed: `20260603`
- train/calibration/test episodes: `7000` / `2400` / `3600`
- packets per test episode: `6`
- action set: `commit, hold, aim_0, aim_1, aim_2, aim_3`
- aim cost: `0.040`
- hold cost: `0.018`
- conformal alpha: `0.05`
- gate threshold: `0.800`

At the main cost, the optimal held-out actions were:

| Action | Optimal count |
|---|---:|
| commit | 836 |
| hold | 385 |
| aim_0 | 588 |
| aim_1 | 641 |
| aim_2 | 537 |
| aim_3 | 613 |

Model scores:

| Model | Value RMSE | Value R2 | Action acc | Regret | P90 regret | Unsafe choice | Unnecessary unsafe |
|---|---:|---:|---:|---:|---:|---:|---:|
| scalar | 0.366 | 0.424 | 0.564 | 0.343 | 1.088 | 0.339 | 0.337 |
| continuous transition value | 0.310 | 0.585 | 0.644 | 0.242 | 1.018 | 0.246 | 0.243 |
| conformal transition gate | 0.418 | 0.247 | 0.368 | 0.591 | 1.125 | 0.579 | 0.577 |
| governed transition | 0.310 | 0.586 | 0.709 | 0.177 | 0.959 | 0.185 | 0.183 |
| hybrid full | 0.302 | 0.608 | 0.720 | 0.164 | 0.948 | 0.174 | 0.172 |

The hybrid improves action accuracy by `0.076` over continuous value and reduces
mean regret by about `32%`. It also reduces unnecessary unsafe action choices
from `0.243` to `0.172`.

---

## Cost Sweep

| Aim cost | Regime | Continuous acc | Gate acc | Hybrid acc | Continuous regret | Gate regret | Hybrid regret |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0.000 | cheap control | 0.729 | 0.277 | 0.706 | 0.159 | 0.607 | 0.186 |
| 0.040 | mixed control | 0.644 | 0.368 | 0.720 | 0.242 | 0.591 | 0.164 |
| 0.100 | costly control | 0.638 | 0.402 | 0.720 | 0.267 | 0.233 | 0.191 |

The result is regime-sensitive.

When control is free, continuous value wins. The system should often act, and
the gate can over-constrain useful intervention.

In the mixed and costly regimes, the hybrid wins. These are the regimes where
action has to negotiate value and boundary safety at the same time.

---

## Why This Matters After E19

E19 said:

\[
\text{if action only indexes future evidence, value can be enough.}
\]

E20 says:

\[
\text{if action changes future evidence, value and admission separate.}
\]

That is exactly the boundary the B-series needed.

The brain hypothesis should not say:

\[
\text{every look is governed.}
\]

It should say:

\[
\text{intervention packets need admission when they can deform future state.}
\]

This is closer to animal control. A movement is not just a query. It changes
the body-world channel that will generate the next evidence.

---

## Anti-Tautology Notes

E20 is positive, but it is not a final proof.

Strengths:

- the action enters the transition function;
- every episode compares multiple interventions from the same early state;
- wrong control can produce post-action rupture;
- policy is scored by held-out action regret;
- the continuous model sees rich pre/post evidence, not only scalar surprise;
- the cost sweep includes cheap, mixed, and costly control.

Limits:

- the task is synthetic;
- the gate construction explicitly encodes boundary persistence;
- the continuous model uses a lightweight quadratic basis without all-pairs
  interactions;
- utility is designed from true-label support and unsafe penalties;
- no learned world model is required, since the simulator enumerates actions.

Therefore E20 should be read as a design theorem in empirical form:

\[
\boxed{
\text{closed-loop intervention is the right place to test governance.}
}
\]

It is not yet an external biological anchor.

---

## Consequence for the Brain Hypothesis

E19 and E20 together suggest a cleaner bucket rule for prediction-error
management:

| Error context | Likely management bucket |
|---|---|
| better passive evidence is available | value-guided sampling |
| evidence is static and local | continuous update |
| evidence must become commitment | admission gate |
| action changes future evidence | hybrid value-governance |
| action can damage the channel | safety/refusal or recovery |

For animal brains, this points toward a reverse-engineering program:

\[
\text{do not look for one prediction-error handler.}
\]

Look for boundary transitions where an error is allowed to become:

1. updated belief;
2. directed attention;
3. motor issue;
4. active sampling;
5. memory compression;
6. refusal or inhibition.

E20 says the hybrid regime begins when the organism is not merely receiving the
world, but helping construct the next world-state it will have to interpret.

