# B7 Refusal/Inhibition Versus Competence Probe

- timestamp: `2026-06-03T20:42:01.034478+00:00`
- seed: `20260603`
- trials per kind: `300`
- calibration episodes: `900`
- evidence train/test: `72` / `72`
- noise scale: `0.35`
- sanction/inhibition cost: `1.05` / `0.1`
- alpha: `0.05`

## Claim Tested

B7-E1 asks whether governance is distinct from incompetence. Forbidden episodes
are genuinely predictive: a competence maximizer can explain them. The governed
boundary should inhibit/refuse them while still closing lawful packets.

## Conformal Null Thresholds

| score | threshold |
|---|---|
| alpha | 0.050 |
| scalar | 1.000 |
| retained | 0.024 |
| safe_packet | 0.021 |
| forbidden | 0.024 |
| route | 0.038 |
| family_gate | 2.129 |
| fixed_gain | 0.120 |

## Agent Summary

| agent | routing accuracy | noise false admission | retained success | safe packet success | forbidden inhibit success | forbidden as closure | safe false inhibition |
|---|---|---|---|---|---|---|---|
| scalar | 0.256 | 0.027 | 0.050 | 0.000 | 0.000 | 0.000 | 0.000 |
| competence_maximizer | 0.750 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| refusal_only | 0.500 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| governed_boundary | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 |
| t18_conformal_governed | 0.978 | 0.037 | 0.947 | 1.000 | 1.000 | 0.000 | 0.000 |

## Accuracy by Episode Kind

| kind | true op | scalar | competence maximizer | refusal only | governed boundary | T18 conformal governed |
|---|---|---|---|---|---|---|
| retained | reweight | 0.050 | 1.000 | 0.000 | 1.000 | 0.947 |
| safe_packet | close | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 |
| forbidden | inhibit | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| noise | suppress | 0.973 | 1.000 | 1.000 | 1.000 | 0.963 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_non_noise_vs_noise | 0.509 |
| retained_gain_retained_vs_noise | 1.000 |
| safe_packet_gain_safe_vs_noise | 1.000 |
| forbidden_gain_forbidden_vs_noise | 1.000 |
| forbidden_gain_forbidden_vs_safe | 1.000 |
| best_competence_forbidden_or_safe_vs_noise | 1.000 |

## Mean Scores by Kind

| kind | scalar | retained | safe packet | forbidden | best competence | forbidden close value | inhibition value |
|---|---|---|---|---|---|---|---|
| retained | 1.000 | 0.894 | -0.016 | -0.013 | 0.009 | -1.063 | -0.113 |
| safe_packet | 1.000 | -0.010 | 0.893 | -0.015 | 0.893 | -1.065 | -0.115 |
| forbidden | 1.000 | -0.013 | -0.014 | 0.893 | 0.893 | -0.157 | 0.793 |
| noise | 1.000 | -0.016 | -0.015 | -0.014 | 0.009 | -1.064 | -0.114 |

## Pass Checks

| check | result |
|---|---|
| scalar_surprise_matched | pass |
| competence_closes_forbidden | pass |
| refusal_only_fails_safe_packet | pass |
| governed_boundary_inhibits_forbidden | pass |
| governed_boundary_preserves_competence | pass |
| conformal_inhibits_forbidden | pass |
| conformal_false_admission_controlled | pass |

Overall: **PASS**

## Interpretation

This is a pass if scalar surprise stays matched, unconstrained competence closes
forbidden predictive structure, refusal-only behavior fails lawful competence,
and governed routers inhibit forbidden structure while preserving retained and
lawful packet performance.

This would falsify the governance bucket if forbidden structure were merely
noise, if refusal were just incompetence, or if the governed router could not
separate lawful closure from forbidden closure under matched predictive gain.
