# E14 - Governance Risk Falsifier

**Risk Suppression, Rule Persistence, and Represented-But-Blocked Competence**

**Leonardo Murillo Montero**

**Draft 1**

---

> *Risk explains inhibition. Rule persistence decides refusal.*

---

## Status

E14 is the empirical falsifier for the governance/refusal bucket.

B10 through E13 converged on the same correction: early buckets are usually not
primitive substrate variables. They are governed admissions over continuous
control fields.

E14 asks whether governance follows this pattern:

\[
\text{continuous risk/preference control} + \text{governed refusal admission}.
\]

The empirical companion is:

`empirical/e14_governance_risk_falsifier.py`

with reports:

- `empirical/reports/e14_governance_risk_falsifier.md`
- `empirical/reports/e14_governance_risk_falsifier.json`

---

## Abstract

**Situation.** B2 listed governance error as a prediction-error bucket whose
operation is inhibition or refusal. B7 showed that forbidden predictive
structure should be inhibited while lawful competence is preserved. B9 then
identified the stronger rival: refusal may be continuous risk/preference
suppression rather than a distinct governed route.

**Task.** E14 separates two jobs:

1. predicting graded behavioral inhibition;
2. admitting governed refusal, where a useful completion is represented but
   blocked because it is disallowed.

Synthetic episodes come from five worlds:

1. **allowed world:** high competence, low risk, permitted action;
2. **risk world:** high competence, high ordinary risk, suppress but do not
   refuse;
3. **bait world:** local rule pressure looks forbidden but does not persist;
4. **forbidden world:** high competence and persistent governance violation;
5. **no-signal world:** weak competence and no governed refusal.

**Action.** The continuous rival receives competence, action value, ordinary
risk, preference conflict, policy cost, and train-side rule pressure. The
governance gate receives held-out rule/sanction persistence calibrated on
non-forbidden worlds.

**Result.**

\[
\boxed{
\text{RISK\_FITS\_BUT\_GATE\_RECOVERS\_REFUSAL.}
}
\]

Continuous risk/preference variables beat the gate-only model on inhibition:
RMSE \(0.209\) versus \(0.283\). But they falsely refuse bait worlds \(0.990\)
of the time. The held-out governance gate detects \(1.000\) of true forbidden
worlds with \(0.000\) non-forbidden false refusal in the default run.

Therefore governance is not ordinary risk. Governance is represented competence
under persistent rule admission.

---

## The Falsifier

The early bucket phrase was:

\[
\text{forbidden structure} \longrightarrow \text{inhibit/refuse}.
\]

The stronger rival says:

\[
\text{refusal is continuous risk/preference suppression.}
\]

E14 lets that rival win where it should. Ordinary risk worlds suppress action
without being governed refusals. If continuous risk can explain both
inhibition and refusal while controlling bait, the governance bucket should be
demoted.

The adversarial pressure is local rule bait:

\[
\text{bait worlds and forbidden worlds both have high train-side rule pressure.}
\]

Only forbidden worlds preserve rule violation and sanction out of sample.

---

## Synthetic Worlds

| World | Generator | Correct response |
|---|---|---|
| allowed world | high competence, low risk, allowed | act |
| risk world | high competence, high ordinary risk | suppress action, do not refuse |
| bait world | high train rule pressure, low held-out rule pressure | resist false refusal |
| forbidden world | high competence, persistent held-out rule violation | refuse/inhibit |
| no-signal world | weak competence | ignore, no refusal |

The hard comparison is bait world versus forbidden world. Both look locally
disallowed. Only forbidden world stays disallowed.

---

## Models Compared

| Model | Information available | Expected failure mode |
|---|---|---|
| scalar | scalar surprise only | blind under matched surprise |
| continuous risk | competence, value, risk, preference conflict, policy cost, train rule pressure | over-refuses bait |
| governance gate | held-out rule/sanction persistence | loses graded inhibition |
| governed risk gate | risk variables plus governance gate | should split inhibition and refusal |
| hybrid risk governance | risk variables plus held-out governance features | strongest composite model |

The continuous rival is intentionally strong. It sees ordinary risk and
train-side rule pressure. The gate is intentionally narrow. It asks whether the
rule violation persists under held-out evidence.

---

## Main Result

Default configuration:

- seed: `20260603`
- route/null trials: `900` / `450`
- main forbidden mix: `0.4`
- risk/bait share: `0.35` / `0.35`
- conformal alpha: `0.05`
- conformal governance gate: `0.368`

| Model | Inhibition RMSE | Inhibition R2 | Refusal accuracy | Refusal detection | Non-forbidden false refusal | Bait false refusal |
|---|---|---|---|---|---|---|
| scalar | 0.319 | -0.002 | 0.739 | 0.000 | 0.000 | 0.000 |
| continuous risk | 0.209 | 0.570 | 0.847 | 0.969 | 0.196 | 0.990 |
| governance gate | 0.283 | 0.214 | 1.000 | 1.000 | 0.000 | 0.000 |
| governed risk gate | 0.098 | 0.905 | 1.000 | 1.000 | 0.000 | 0.000 |
| hybrid risk governance | 0.096 | 0.910 | 1.000 | 1.000 | 0.000 | 0.000 |

The split is:

\[
\begin{array}{rcl}
\text{risk/preference control} &:& \text{graded inhibition;}\\
\text{held-out governance persistence} &:& \text{refusal admission.}
\end{array}
\]

Continuous risk is not bad. It detects most forbidden worlds and predicts
ordinary inhibition better than the gate-only model. But it treats local bait
as refusal. The gate supplies exactly the missing distinction.

---

## Source Means

| Source | Competence | Action value | Risk | Preference conflict | Train rule | Held-out rule | Governance score | Target inhibition | Target refusal |
|---|---|---|---|---|---|---|---|---|---|
| forbidden world | 0.859 | 0.858 | 0.311 | 0.306 | 0.873 | 0.873 | 0.853 | 0.950 | 1.000 |
| risk world | 0.872 | 0.875 | 0.876 | 0.771 | 0.139 | 0.148 | 0.284 | 0.981 | 0.000 |
| bait world | 0.857 | 0.875 | 0.318 | 0.291 | 0.879 | 0.148 | 0.272 | 0.315 | 0.000 |
| allowed world | 0.861 | 0.879 | 0.135 | 0.118 | 0.112 | 0.109 | 0.246 | 0.069 | 0.000 |
| no-signal world | 0.098 | 0.102 | 0.133 | 0.120 | 0.104 | 0.101 | 0.093 | 0.748 | 0.000 |

The no-signal world has high behavioral inhibition because no action is
warranted; it is not a refusal. This is why E14 separates inhibition from
governed refusal.

---

## Phase Sweep

The phase sweep varies the proportion of forbidden worlds among route trials.

| Forbidden mix | Inhibition winner | Refusal winner | Continuous inhibition | Gate inhibition | Hybrid inhibition | Continuous FA | Gate FA | Gate detection | Continuous bait FA |
|---|---|---|---|---|---|---|---|---|---|
| 0.000 | continuous risk | scalar | 0.079 | 0.352 | 0.079 | 0.000 | 0.000 | nan | 0.000 |
| 0.200 | hybrid risk governance | hybrid risk governance | 0.191 | 0.316 | 0.089 | 0.002 | 0.000 | 1.000 | 0.010 |
| 0.400 | hybrid risk governance | hybrid risk governance | 0.212 | 0.286 | 0.093 | 0.195 | 0.000 | 1.000 | 0.993 |
| 0.700 | hybrid risk governance | hybrid risk governance | 0.175 | 0.213 | 0.100 | 0.113 | 0.000 | 1.000 | 1.000 |
| 1.000 | hybrid risk governance | hybrid risk governance | 0.062 | 0.066 | 0.062 | 0.000 | 0.003 | 1.000 | nan |

When there is no forbidden world, continuous risk wins. As forbidden worlds and
bait worlds appear, the governed models become necessary. This is the desired
falsifier shape: the gate is not crowned in every regime.

---

## Interpretation

E14 changes the governance bucket.

The older phrase was:

\[
\boxed{
\text{governance error routes to inhibition/refusal.}
}
\]

The updated phrase is:

\[
\boxed{
\text{refusal is risk control under persistent-governance admission.}
}
\]

Inhibition is not refusal. A system can inhibit action because the action is
risky, because the action is not useful, or because no signal warrants action.
Governed refusal is narrower: a useful completion is represented as competent
but is blocked because a rule, sanction, social constraint, or task constraint
persists.

The bucket is therefore not the risk signal. The bucket is the admission
decision:

\[
\text{is this competent completion disallowed?}
\]

---

## Biological Prediction

E14 predicts a dissociation:

1. ordinary risk and preference conflict should predict graded behavioral
   inhibition;
2. governed refusal should require represented competence plus persistent
   disallowance;
3. local bait should produce hesitation or uncertainty without durable refusal;
4. perturbing governance gates should alter refusal more than ordinary risk
   aversion.

The decisive measurement is not whether action is suppressed. It is whether the
brain represents the option as useful while blocking admission.

---

## Consequence for the B-Series

B10 through E14 now form a coherent pattern:

| Domain | Continuous variable | Governed admission |
|---|---|---|
| current | temporal flow | current admission |
| noise/structure | expected/unexpected uncertainty | structural closure |
| ambiguity/sampling | expected information gain | candidate-set persistence |
| capacity/tool use | resource-rational cost control | externalization admission |
| governance/refusal | risk/preference control | persistent-governance refusal |

The updated B-series claim is:

\[
\boxed{
\text{brains route continuous control fields through governed admissions.}
}
\]

This does not make the early bucket table useless. It demotes it from substrate
taxonomy to operational policy surface.

---

## What Would Falsify This Update

The governed-risk update would fail if:

1. continuous risk/preference variables predict inhibition and refusal;
2. held-out governance persistence adds no protection against bait;
3. risk worlds, bait worlds, and forbidden worlds cannot be separated
   behaviorally or neurally;
4. perturbing governance circuits leaves represented-but-blocked competence
   intact.

If that happens, governance should be demoted to a readable discretization of
risk/preference suppression.

---

## Next Experimental Target

The next best task is no longer just another bucket probe. The next best task
is a synthesis pass: collect B10/E11/E12/E13/E14 into a revised B-series core
claim, then choose which remaining bucket still looks primitive enough to
deserve a probe.

