# E22 - Trained MLP Closed Loop

**When Nonlinear Value Learns the Gate**

**Leonardo Murillo Montero**

**Draft 1**

---

> *If a gate disappears inside a learned predictor, it was not yet a boundary
> mechanism. It was a coordinate we had named.*

---

## Status

E22 is the direct successor to E21.

E21 showed that a strong pairwise continuous absorber nearly erased the E20
hybrid governance advantage. E22 asks the sharper question:

\[
\text{does a genuinely trained nonlinear state-action model absorb the gate?}
\]

The empirical companion is:

`empirical/e22_trained_mlp_closed_loop_probe.py`

with reports:

- `empirical/reports/e22_trained_mlp_closed_loop_probe.md`
- `empirical/reports/e22_trained_mlp_closed_loop_probe.json`

---

## Abstract

**Situation.** E20 made action part of the transition function and found a
hybrid value-governance advantage. E21 weakened that result: pairwise
continuous value nearly matched the best hybrid. E22 replaces the random-feature
absorber with a trained NumPy MLP.

**Task.** The simulator is unchanged from E20/E21. The agent evaluates six
candidate actions from the same early state:

\[
\{\text{commit},\text{hold},\text{aim}_0,\text{aim}_1,\text{aim}_2,\text{aim}_3\}.
\]

Each action changes the post-action state before utility is scored. The
decisive comparison is:

\[
\text{continuous MLP without gate features}
\quad\text{vs.}\quad
\text{hybrid MLP with gate features}.
\]

**Result.**

\[
\boxed{
\text{TRAINED\_MLP\_ABSORBS\_GATE.}
}
\]

The no-gate continuous MLP matches the gate-aware hybrid:

| Quantity | Pairwise ridge | Continuous MLP | Hybrid MLP |
|---|---:|---:|---:|
| action accuracy | 0.738 | 0.805 | 0.806 |
| mean regret | 0.154 | 0.128 | 0.128 |
| unnecessary unsafe | 0.161 | 0.131 | 0.131 |
| value RMSE | 0.268 | 0.256 | 0.255 |
| select RMSE | 0.272 | 0.244 | 0.242 |

The hybrid has a tiny accuracy and value-fit edge, but no policy advantage. On
regret and unnecessary unsafe action, it is tied with the no-gate MLP.

Therefore E22 supports the correction:

\[
\boxed{
\text{the E20 gate residual is not irreducible in this simulator.}
}
\]

---

## Experimental Design

E22 inherits the E20 closed-loop motor-sensing simulator.

Each episode has:

| Component | Meaning |
|---|---|
| early state | ambiguous sensorimotor evidence |
| action | commit, hold, or aim at one basin |
| transition | action changes the post-action state |
| rupture | wrong control can deform future evidence |
| utility | true-label support minus cost and unsafe penalties |
| policy score | choose one action per held-out episode |

The simulator is the same. The model class changes.

---

## Models Compared

| Model | Gate features? | Basis |
|---|---|---|
| continuous pairwise ridge | no | full pairwise quadratic |
| continuous MLP | no | trained `[64, 32]` ReLU MLP |
| hybrid MLP | yes | same MLP plus gate features |

Both MLPs are trained with minibatch Adam and validation early stopping. The
calibration set also supplies the conformal gate threshold.

The split is smaller than E21 because the MLPs are actually trained:

- train/calibration/test episodes: `2400` / `900` / `1600`;
- packets per episode: `6`;
- train/calibration/test packets: `14400` / `5400` / `9600`.

---

## Main Result

Default configuration:

- seed: `20260603`
- aim cost: `0.040`
- hold cost: `0.018`
- hidden layers: `[64, 32]`
- epochs/patience: `55` / `8`
- conformal alpha: `0.05`
- gate threshold: `0.811`

At the main cost, the optimal held-out actions were:

| Action | Optimal count |
|---|---:|
| commit | 388 |
| hold | 182 |
| aim_0 | 242 |
| aim_1 | 259 |
| aim_2 | 263 |
| aim_3 | 266 |

Model scores:

| Model | Value RMSE | Value R2 | Select RMSE | Action acc | Regret | P90 regret | Unnecessary unsafe |
|---|---:|---:|---:|---:|---:|---:|---:|
| continuous pairwise ridge | 0.268 | 0.692 | 0.272 | 0.738 | 0.154 | 0.954 | 0.161 |
| continuous MLP | 0.256 | 0.719 | 0.244 | 0.805 | 0.128 | 0.946 | 0.131 |
| hybrid MLP | 0.255 | 0.721 | 0.242 | 0.806 | 0.128 | 0.949 | 0.131 |

The trained no-gate MLP beats the pairwise absorber and ties the hybrid on the
policy quantities that matter most.

---

## Interpretation

E22 is the strongest correction so far.

E20 suggested:

\[
\text{closed-loop action needs hybrid governance.}
\]

E21 corrected that to:

\[
\text{closed-loop governance is capacity-sensitive.}
\]

E22 corrects it further:

\[
\boxed{
\text{in this simulator, nonlinear state-action prediction absorbs the gate.}
}
\]

This does not mean brains have no gates. It means our current synthetic gate is
not evidence for an irreducible brain mechanism. A trained continuous predictor
can learn the boundary-persistence relation from the raw state-action packet.

The biological lesson is sharper:

\[
\text{a gate is real only if it survives a strong learned absorber}
\]

or if it can be identified as a separate bottleneck, cost, latency, inhibition,
or anatomical routing constraint.

---

## Consequence for the Brain Hypothesis

After E22, the B-series should not treat every successful gate feature as a
separate prediction-error management bucket.

The corrected hierarchy is:

1. scalar surprise baseline;
2. lightweight continuous value;
3. strong pairwise/nonlinear absorption;
4. trained state-action predictor;
5. only then: residual gate, refusal, compression, or admission mechanism.

For the animal brain, this implies:

\[
\boxed{
\text{look for gates where learned prediction cannot cheaply absorb the}
}
\]

\[
\boxed{
\text{constraint.}
}
\]

Good candidates are not ordinary value decisions. They are bottlenecked
transitions:

- action inhibition;
- pain/avoidance override;
- sleep/wake admission;
- working-memory admission;
- irreversible commitment;
- social refusal;
- tool-use delegation;
- compression into durable memory.

Those are places where the brain may need a distinct boundary controller, not
just a richer value function.

---

## Anti-Tautology Notes

Strengths:

- the task is unchanged from E20/E21;
- the no-gate continuous MLP has no explicit gate inputs;
- the hybrid MLP has the same architecture plus gate features;
- both are trained by minibatch Adam with validation early stopping;
- the pairwise E21 absorber is retained as a reference;
- the policy is scored by held-out action regret.

Limits:

- the task is still synthetic;
- the MLP is small and feed-forward, not recurrent;
- the split is smaller than E21 for runtime;
- the calibration set doubles as MLP validation and gate calibration;
- the simulator enumerates all actions rather than learning exploration;
- there is no external animal or neural dataset.

The honest takeaway:

\[
\boxed{
\text{E22 weakens the synthetic gate claim and strengthens the program.}
}
\]

It gives us the next empirical standard: find a gate-like residual that survives
trained nonlinear prediction, preferably in an external sequential-control
dataset or a simulator with unenumerated exploration.

