# B5 Active Sensing Versus Belief Revision Probe

- timestamp: `2026-06-03T20:22:14.501747+00:00`
- seed: `20260603`
- trials per kind: `300`
- calibration episodes: `900`
- evidence train/test: `72` / `72`
- noise scale: `0.35`
- sample/action cost: `0.06` / `0.18`
- alpha: `0.05`

## Claim Tested

B5-E1 asks whether an active boundary agent moves or samples before revising
belief when the current view is underdetermined. Active episodes are designed
so a naive belief update fits the training view, but only the action cue
generalizes.

## Conformal Null Thresholds

| score | threshold |
|---|---|
| alpha | 0.050 |
| scalar | 1.000 |
| retained_train | 0.055 |
| retained | 0.026 |
| sample_value | -0.037 |
| action_value | -0.153 |
| packet | 0.025 |
| family_margin | 0.029 |
| fixed_gain | 0.120 |
| fixed_sample_value | 0.100 |
| fixed_action_value | 0.100 |

## Agent Summary

| agent | routing accuracy | noise false admission | retained success | sample success | act success | packet success | act as belief revision |
|---|---|---|---|---|---|---|---|
| scalar | 0.205 | 0.043 | 0.067 | 0.000 | 0.000 | 0.000 | 0.027 |
| naive_belief_revision | 0.399 | 0.007 | 1.000 | 0.000 | 0.000 | 0.000 | 0.930 |
| packet_only_closure | 0.400 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| passive_bucket | 0.800 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| active_boundary | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| t18_conformal_active | 0.997 | 0.013 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |

## Accuracy by Episode Kind

| kind | true op | scalar | naive belief | packet only | passive bucket | active boundary | T18 conformal active |
|---|---|---|---|---|---|---|---|
| retained | reweight | 0.067 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| sample | sample | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| act | act | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 |
| packet | close | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| noise | suppress | 0.957 | 0.993 | 1.000 | 1.000 | 1.000 | 0.987 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_non_noise_vs_noise | 0.456 |
| retained_gain_retained_vs_noise | 1.000 |
| sample_value_sample_vs_noise | 1.000 |
| action_value_act_vs_noise | 1.000 |
| packet_gain_packet_vs_noise | 1.000 |
| train_belief_act_vs_noise | 0.998 |
| action_value_act_vs_retained | 1.000 |

## Mean Scores by Kind

| kind | scalar | train belief | heldout belief | sample value | action value | packet | premature revision risk |
|---|---|---|---|---|---|---|---|
| retained | 1.000 | 0.894 | 0.891 | -0.072 | -0.195 | -0.014 | 0.003 |
| sample | 1.000 | 0.013 | -0.014 | 0.834 | -0.195 | -0.016 | 0.027 |
| act | 1.000 | 0.231 | -0.234 | -0.075 | 0.697 | -0.017 | 0.465 |
| packet | 1.000 | 0.013 | -0.012 | -0.072 | -0.193 | 0.894 | 0.025 |
| noise | 1.000 | 0.014 | -0.014 | -0.076 | -0.194 | -0.017 | 0.028 |

## Pass Checks

| check | result |
|---|---|
| scalar_surprise_matched | pass |
| naive_belief_overupdates_action | pass |
| passive_bucket_misses_action | pass |
| active_boundary_recovers_action | pass |
| active_boundary_routes_core_cases | pass |
| conformal_recovers_action | pass |
| conformal_false_admission_controlled | pass |

Overall: **PASS**

## Interpretation

This is a pass if scalar surprise is matched, naive belief revision
over-updates active episodes, passive routing misses the action cases, and the
active routers choose action while keeping noise admission under conformal
control.

This would falsify the active-sensing bucket if belief revision generalized as
well as action on the active episodes, or if the passive bucket router solved
the action cases without an intervention channel.
