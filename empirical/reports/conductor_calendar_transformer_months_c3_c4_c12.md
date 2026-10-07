# Calendar Transformer Conductor Filter (months)

## Verdict

This is a small real-sequence training-loop pilot for the Pareto rule
`gradient projection 0%, update projection 100%`.  The model is a
trainable character-level attention classifier over the checked-in
months prompts; only the output-head Adam update is projected
in the cyclic character basis.
The projected arm starts with the output head in the same support,
then leaves the stochastic gradient and all Adam moments unprojected.

- test accuracy delta vs Adam: `+0.063492`
- generalization-gap delta vs Adam: `-1.202312`
- final logit-leakage delta vs Adam: `-0.285782`
- JSON payload: `empirical\reports\conductor_calendar_transformer_months_c3_c4_c12.json`

The checked-in calendar train/test files are identical enumerations, so
this run uses a deterministic holdout split before training.  This makes
the generalization gap a real held-out-case measurement rather than a
copy of the training score.

## Setup

- task: `months`
- labels: `January, February, March, April, May, June, July, August, September, October, November, December`
- cases: `84`
- train/test split: `63` / `21`
- seeds: `3` starting at `9101`
- epochs: `300`
- batch size: `16`
- model width / FF width: `32` / `64`
- learning rate: `0.0005`
- closed conductors: `3, 4, 12`

## Character Packets

| conductor | character indices | kept by filter |
|---:|---|---|
| 2 | `6` | no |
| 3 | `4, 8` | yes |
| 4 | `3, 9` | yes |
| 6 | `2, 10` | no |
| 12 | `1, 5, 7, 11` | yes |

## Final Metrics

| method | train loss | test loss | gen gap | train acc | test acc | acc gap | final logit leakage | output-update leakage | closed energy growth | leak energy growth |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Adam | 0.886851 | 6.125025 | 5.238174 | 0.708995 | 0.000000 | 0.708995 | 0.285782 | 0.275362 | 4.457e+03 | 1.847e+03 |
| update-only conductor Adam | 0.983013 | 5.018874 | 4.035862 | 0.666667 | 0.063492 | 0.603175 | 1.548e-31 | 4.697e-33 | 5.171e+03 | 8.103e-28 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.782505 | 6.822636 | 6.040132 | 0.777778 | 0.000000 | 0.358888 |
| 9101 | update-only conductor Adam | 0.996383 | 5.061635 | 4.065252 | 0.634921 | 0.047619 | 2.767e-31 |
| 9102 | Adam | 1.144067 | 5.430185 | 4.286118 | 0.539683 | 0.000000 | 0.262657 |
| 9102 | update-only conductor Adam | 1.089789 | 4.881882 | 3.792093 | 0.634921 | 0.047619 | 6.752e-32 |
| 9103 | Adam | 0.733982 | 6.122253 | 5.388272 | 0.809524 | 0.000000 | 0.235800 |
| 9103 | update-only conductor Adam | 0.862866 | 5.113106 | 4.250240 | 0.730159 | 0.095238 | 1.202e-31 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 4.299790 | 1.693605 | 0.277280 |
| 0 | update-only conductor Adam | 4.299790 | 7.014e-32 | 1.630e-32 |
| 1 | Adam | 3.733048 | 1.422621 | 0.278559 |
| 1 | update-only conductor Adam | 3.885843 | 8.208e-32 | 2.188e-32 |
| 75 | Adam | 585.881793 | 222.698129 | 0.275585 |
| 75 | update-only conductor Adam | 667.213821 | 2.128e-29 | 3.208e-32 |
| 150 | Adam | 1.670e+03 | 599.153108 | 0.262855 |
| 150 | update-only conductor Adam | 1.986e+03 | 1.385e-28 | 6.913e-32 |
| 300 | Adam | 4.462e+03 | 1.849e+03 | 0.285782 |
| 300 | update-only conductor Adam | 5.176e+03 | 8.104e-28 | 1.548e-31 |

## Reading

The filter is deliberately output-side: it does not modify the stochastic
gradient, and it does not constrain the attention or feed-forward weights.
Only the applied class-axis update is projected after Adam's moment
calculation.
For C12 the closed packet choice is a modeling assumption, not a theorem.
The useful object produced here is the harness plus a first held-out
measurement of how much accuracy/generalization is paid for a declared
class-character update filter.

## Reproduction

```powershell
python empirical/conductor_calendar_transformer.py --task months --closed-conductors 3,4,12
```
