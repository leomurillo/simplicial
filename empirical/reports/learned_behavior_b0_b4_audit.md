# Learned Behavior B0/B4 Audit

## Verdict

This report keeps exact-support theorems separate from learned evidence.
Raw learned behavior tables are scored with B0-style projection, closure,
balance, and resource terms.  Calendar and optimizer reports are treated
as update-side summaries, so their declared filters are checked for B2
closure without being upgraded into exact-support evidence.

- behavior tables with full B2 closure: `2` / `2`
- cyclic learned behavior has zero B3 symmetry premium because B2 and B3 coincide;
- C12 update filters often suppress declared leakage while underbuying B2 closure;
- the F4[u]/(u^2) optimizer support is genuinely B2 closed, but B3 would buy the full local row for transfer.

## Learned Behavior Tables

| task | row | reciprocal active | B2 size | B3 size | filtered size | winner | premium | net transfer | pullback CV |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| weekdays | C_7 | 6 | 6 | 6 | 6 | b2_minimal_descent | 0.000000 | 0.000000 | 0.154000 |
| months | C_12 | 11 | 11 | 11 | 11 | b2_minimal_descent | 0.000000 | 0.000000 | 0.233100 |

The active support above is inferred from reciprocal-density Fourier energy
with threshold `0.01`.  Probability
support is also stored in the JSON, but B2 is computed from reciprocal
support to match the B0 theorem.

## Behavior Policy Scores

### weekdays (C_7)

| policy | J | Fisher | reciprocal | closure | balance | resource | support |
|---|---:|---:|---:|---:|---:|---:|---:|
| b2_minimal_descent | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| b3_normalizer_saturation | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| full | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| full_filtered_closure | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| probability_active_support | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| reciprocal_active_support | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |

### months (C_12)

| policy | J | Fisher | reciprocal | closure | balance | resource | support |
|---|---:|---:|---:|---:|---:|---:|---:|
| b2_minimal_descent | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |
| b3_normalizer_saturation | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |
| full | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |
| full_filtered_closure | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |
| probability_active_support | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |
| reciprocal_active_support | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |

## Calendar Update Filters

| report | split | conductors | declared | B2 | missing B2 | acc delta | gap delta | leakage delta | proxy J |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| months.json | random | 12 | 4 | 11 | 7 | 0.015873 | -2.175437 | -0.643158 | 0.727273 |
| months_no_c2.json | random | 3,4,6,12 | 10 | 11 | 1 | 0.015873 | -0.388167 | -0.058409 | 0.318182 |
| months_c3_c4_c12.json | random | 3,4,12 | 8 | 11 | 3 | 0.063492 | -1.202312 | -0.285782 | 0.454545 |
| months_d64_offset_ood.json | offset_ood | 12 | 4 | 11 | 7 | -0.027778 | 0.168510 | -0.285408 | 0.727273 |
| months_d64_offset_ood_no_c2.json | offset_ood | 3,4,6,12 | 10 | 11 | 1 | -0.009259 | 0.085385 | -0.006833 | 0.318182 |
| months_d64_offset_ood_c6_c12.json | offset_ood | 6,12 | 6 | 11 | 5 | 0.013889 | -0.203329 | -0.092169 | 0.590909 |
| months_d64_offset_ood_full.json | offset_ood | 2,3,4,6,12 | 11 | 11 | 0 | 0.000000 | 0.000000 | 0.000000 | 0.250000 |

`missing B2` is the count of subgroup-descent modes absent from the declared
calendar filter.  A zero declared leakage number is therefore a filter
invariant, not proof that the filter is B2 minimal.

## Optimizer Update Audit

- declared support: `7` modes
- B2 minimal descent: `7` modes
- B3 normalizer saturation: `15` modes
- symmetry premium at resource weight `0.25`: `0.133333`
- conductor-closed KL vs Adam: `0.023031` vs `0.036156`
- conductor-closed probability leakage: `0.000000`
- support-transfer estimate gain/premium/net: `0.761905` / `0.133333` / `0.628571`

The projection Pareto report selects update-only full projection as the
best KL setting in the saved sweep:

- gradient/update projection: `0%` / `100%`
- KL: `0.014998`
- probability leakage: `0.000000`

## Reading

B5 should be treated as an empirical audit/protocol, not a theorem.
For learned behavior tables, the current weekday/month rows do not show a
compression win: the inferred reciprocal support already forces full B2
cyclic closure at the default threshold.  For update experiments, the
evidence is real but narrower: conductor filters can reduce leakage, and
the F4[u]/(u^2) optimizer shows a B2-closed update policy with strong
fixed-task performance.  The support-level B4 transfer estimate in this
report should be read alongside the direct learned normalizer-transfer
experiment in `learned_normalizer_transfer_f4_u2.md`.

## Reproduction

```powershell
python empirical/learned_behavior_b0_b4_audit.py
python empirical/learned_behavior_b0_b4_audit.py --check empirical/reports/learned_behavior_b0_b4_audit.json
```
