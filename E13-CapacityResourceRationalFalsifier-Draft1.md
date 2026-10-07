# E13 - Capacity Resource-Rational Falsifier

**Memory Load, Compression, Tool Persistence, and Governed Externalization**

**Leonardo Murillo Montero**

**Draft 1**

---

> *Resource rationality explains load. Held-out tool persistence decides when
> cognition should leave the head.*

---

## Status

E13 is the empirical falsifier for the capacity/compression/tool-use bucket.

B10, E11, and E12 produced the same correction in three different domains:

| Prior falsifier | Continuous variable | Governed admission |
|---|---|---|
| B10 current | temporal flow | current admission |
| E11 noise/structure | expected/unexpected uncertainty | structural closure |
| E12 ambiguity/sampling | expected information gain | candidate-set persistence |

E13 asks whether capacity follows the same pattern:

\[
\text{resource-rational cost control} + \text{externalization admission gate}.
\]

The empirical companion is:

`empirical/e13_capacity_resource_falsifier.py`

with reports:

- `empirical/reports/e13_capacity_resource_falsifier.md`
- `empirical/reports/e13_capacity_resource_falsifier.json`

---

## Abstract

**Situation.** B2 listed capacity error as a prediction-error bucket whose
operation is compression or externalization. B6 showed that exact high-cardinal
lookup cases should be routed to tools rather than absorbed as internal
compression. B9 identified the stronger rival: compression and tool use may
follow continuous memory/action cost minimization, not a discrete capacity
route.

**Task.** E13 separates two jobs:

1. predicting graded cognitive/resource effort;
2. admitting a persistent external tool or memory route.

Synthetic episodes come from four worlds:

1. **no-capacity world:** low load, no useful tool;
2. **compress world:** stable low-rank structure, internal compression is best;
3. **bait world:** train-side tool looks useful but fails out of sample;
4. **tool world:** stable external aid beats internal memory under capacity.

**Action.** The continuous rival receives memory load, capacity pressure,
compression value, train-side tool value, tool cost, and action cost. The
externalization gate receives held-out tool persistence calibrated on non-tool
worlds.

**Result.**

\[
\boxed{
\text{RESOURCE\_FITS\_BUT\_GATE\_RECOVERS\_EXTERNALIZATION.}
}
\]

Continuous resource variables win the graded effort problem: RMSE \(0.051\)
versus \(0.250\) for the gate-only model. But train-side utility alone falsely
externalizes bait worlds \(0.667\) of the time. The held-out tool gate detects
\(1.000\) of true tool worlds with \(0.000\) non-tool false admission in the
default run.

Therefore capacity is not a primitive bucket. Capacity is resource-rational
control under externalization admission.

---

## The Falsifier

The early bucket phrasing was:

\[
\text{capacity overload} \longrightarrow \text{compress or externalize}.
\]

The stronger rival says:

\[
\text{compression and tool use follow continuous cost minimization.}
\]

E13 lets that rival win wherever it should. If resource-rational variables
predict both effort and externalization while controlling false tool use, the
capacity bucket should be demoted to engineering language.

The adversarial pressure is train-side tool bait:

\[
\text{tool worlds and bait worlds both look tool-useful locally.}
\]

Only tool worlds preserve external utility out of sample.

---

## Synthetic Worlds

| World | Generator | Correct response |
|---|---|---|
| no-capacity world | low load, weak tool, weak compression | commit internally |
| compress world | low-rank structure, good internal compression | compress |
| bait world | high train tool value, poor held-out tool value | resist externalization |
| tool world | high held-out tool value under high load | externalize |

The hard comparison is bait world versus tool world. Both have high memory
load, high capacity pressure, and high train-side tool value. Only the tool
world has persistent held-out tool reliability.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | scalar surprise only | blind under matched surprise |
| continuous resource | load, capacity, compression value, train tool value, costs | externalizes train-side bait |
| external tool gate | held-out tool persistence | loses graded effort |
| governed resource gate | resource variables plus tool gate | should split effort and externalization |
| hybrid resource tool | resource variables plus held-out tool features | strongest composite model |

The continuous rival is intentionally strong. It receives the variables that a
resource-rational control model would naturally use.

The gate is intentionally narrow. It asks only whether the external aid remains
useful beyond the local sample.

---

## Main Result

Default configuration:

- seed: `20260603`
- route/null trials: `900` / `450`
- main tool mix: `0.5`
- compress share: `0.45`
- conformal alpha: `0.05`
- conformal tool gate: `0.226`

| Model | Effort RMSE | Effort R2 | Externalize accuracy | Tool detection | Non-tool false admission | Bait false admission |
|---|---|---|---|---|---|---|
| scalar | 0.324 | -0.000 | 0.671 | 0.000 | 0.000 | 0.000 |
| continuous resource | 0.051 | 0.975 | 0.856 | 0.923 | 0.177 | 0.667 |
| external tool gate | 0.250 | 0.405 | 1.000 | 1.000 | 0.000 | 0.000 |
| governed resource gate | 0.050 | 0.977 | 1.000 | 1.000 | 0.000 | 0.000 |
| hybrid resource tool | 0.049 | 0.977 | 1.000 | 1.000 | 0.000 | 0.000 |

The split is:

\[
\begin{array}{rcl}
\text{resource rationality} &:& \text{graded load and effort;}\\
\text{tool persistence} &:& \text{externalization admission.}
\end{array}
\]

The external tool gate is not a good effort model. It is a good admission
model. The resource-rational rival is not a good externalization model when it
sees only train-side utility. It over-trusts bait.

---

## Source Means

| Source | Memory load | Capacity | Train tool | Held-out tool | Held-out compression | Tool score | Target effort | Target external |
|---|---|---|---|---|---|---|---|---|
| tool world | 0.870 | 0.877 | 0.882 | 0.864 | 0.218 | 0.811 | 0.960 | 1.000 |
| compress world | 0.552 | 0.455 | 0.229 | 0.209 | 0.769 | 0.143 | 0.693 | 0.000 |
| bait world | 0.860 | 0.869 | 0.881 | 0.186 | 0.212 | 0.077 | 0.907 | 0.000 |
| no-capacity world | 0.185 | 0.127 | 0.064 | 0.059 | 0.091 | -0.005 | 0.225 | 0.000 |

The table shows why train-side cost control is insufficient. Tool world and
bait world are nearly indistinguishable by load and train tool value. They
differ in held-out tool persistence.

---

## Phase Sweep

The phase sweep varies the proportion of tool worlds among route trials.

| Tool mix | Effort winner | External winner | Continuous effort | Gate effort | Hybrid effort | Continuous FA | Gate FA | Gate detect | Continuous bait FA |
|---|---|---|---|---|---|---|---|---|---|
| 0.000 | hybrid resource tool | scalar | 0.051 | 0.291 | 0.051 | 0.000 | 0.000 | nan | 0.000 |
| 0.250 | hybrid resource tool | hybrid resource tool | 0.052 | 0.275 | 0.050 | 0.014 | 0.000 | 1.000 | 0.041 |
| 0.500 | hybrid resource tool | hybrid resource tool | 0.051 | 0.260 | 0.049 | 0.240 | 0.000 | 1.000 | 0.816 |
| 0.750 | hybrid resource tool | hybrid resource tool | 0.049 | 0.206 | 0.048 | 0.192 | 0.000 | 1.000 | 0.990 |
| 1.000 | hybrid resource tool | hybrid resource tool | 0.046 | 0.074 | 0.046 | 0.000 | 0.000 | 1.000 | nan |

Again, the pure bucket is not the story. The effort winner is always in the
resource-rational family. But when bait worlds exist, held-out tool persistence
is needed to prevent false externalization.

---

## Interpretation

E13 changes the capacity bucket.

The older phrase was:

\[
\boxed{
\text{capacity error routes to compression or tool use.}
}
\]

The updated phrase is:

\[
\boxed{
\text{capacity routing is resource-rational control under externalization admission.}
}
\]

This is a better brain hypothesis. Animals and humans do not externalize merely
because something is hard. They externalize when the outside resource is stable,
cheap enough, accessible enough, and superior to internal compression.

The bucket is not the load signal. The bucket is the admission decision:

\[
\text{should this control problem leave the internal workspace?}
\]

---

## Biological Prediction

E13 predicts a dissociation:

1. working-memory load, cognitive effort, and compression demand should track
   continuous resource-rational variables;
2. durable tool use should depend on stable external reliability, not only
   train-side success;
3. bait tools should trigger transient interest or trial use without durable
   externalization;
4. perturbing externalization gates should alter tool adoption more than
   internal compression effort.

The decisive measurement is not whether task load is high. It is whether high
load and stable external reliability come apart.

---

## Consequence for the B-Series

B10, E11, E12, and E13 now form a pattern:

| Domain | Continuous variable | Governed admission |
|---|---|---|
| current | temporal flow | current admission |
| noise/structure | expected/unexpected uncertainty | structural closure |
| ambiguity/sampling | expected information gain | candidate-set persistence |
| capacity/tool use | resource-rational cost control | externalization admission |

The B-series should now be stated as:

\[
\boxed{
\text{brains route continuous control fields through governed admissions.}
}
\]

That is sharper than the original bucket taxonomy. It preserves the operational
value of buckets while making the substrate more biologically plausible.

---

## What Would Falsify This Update

The governed-resource update would fail if:

1. continuous resource-rational variables predict effort and externalization;
2. held-out tool persistence adds no protection against bait tools;
3. stable tool worlds and train-side bait worlds cannot be separated
   behaviorally or neurally;
4. perturbing externalization control leaves tool adoption intact.

If that happens, capacity should be demoted to a readable discretization of
cost minimization.

---

## Next Experimental Target

The next best falsifier is **E14: Governance Versus Risk/Preference Control**.
The question should be whether refusal/inhibition is a distinct governed route,
or whether it is continuous risk/preference suppression. The experiment should
let risk control win if it can.

