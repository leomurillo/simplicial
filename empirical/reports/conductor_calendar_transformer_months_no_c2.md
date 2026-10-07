# Calendar Transformer Conductor Filter (months)

## Verdict

This is a small real-sequence training-loop pilot for the Pareto rule
`gradient projection 0%, update projection 100%`.  The model is a
trainable character-level attention classifier over the checked-in
months prompts; only the output-head Adam update is projected
in the cyclic character basis.
The projected arm starts with the output head in the same support,
then leaves the stochastic gradient and all Adam moments unprojected.

- test accuracy delta vs Adam: `+0.015873`
- generalization-gap delta vs Adam: `-0.388167`
- final logit-leakage delta vs Adam: `-0.058409`
- JSON payload: `empirical\reports\conductor_calendar_transformer_months_no_c2.json`

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
- closed conductors: `3, 4, 6, 12`

## Character Packets

| conductor | character indices | kept by filter |
|---:|---|---|
| 2 | `6` | no |
| 3 | `4, 8` | yes |
| 4 | `3, 9` | yes |
| 6 | `2, 10` | yes |
| 12 | `1, 5, 7, 11` | yes |

## Final Metrics

| method | train loss | test loss | gen gap | train acc | test acc | acc gap | final logit leakage | output-update leakage | closed energy growth | leak energy growth |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Adam | 0.886851 | 6.125025 | 5.238174 | 0.708995 | 0.000000 | 0.708995 | 0.058409 | 0.111633 | 5.910e+03 | 394.528218 |
| update-only conductor Adam | 0.910662 | 5.760669 | 4.850007 | 0.698413 | 0.015873 | 0.682540 | 2.998e-32 | 2.076e-33 | 6.155e+03 | 1.840e-28 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.782505 | 6.822636 | 6.040132 | 0.777778 | 0.000000 | 0.095056 |
| 9101 | update-only conductor Adam | 0.851758 | 6.045592 | 5.193834 | 0.746032 | 0.000000 | 2.624e-32 |
| 9102 | Adam | 1.144067 | 5.430185 | 4.286118 | 0.539683 | 0.000000 | 0.027871 |
| 9102 | update-only conductor Adam | 1.166919 | 5.092812 | 3.925893 | 0.555556 | 0.047619 | 2.796e-32 |
| 9103 | Adam | 0.733982 | 6.122253 | 5.388272 | 0.809524 | 0.000000 | 0.052298 |
| 9103 | update-only conductor Adam | 0.713310 | 6.143604 | 5.430294 | 0.793651 | 0.000000 | 3.573e-32 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 5.667749 | 0.325646 | 0.056896 |
| 0 | update-only conductor Adam | 5.667749 | 3.689e-32 | 6.617e-33 |
| 1 | Adam | 4.826070 | 0.329599 | 0.069871 |
| 1 | update-only conductor Adam | 4.948498 | 3.454e-32 | 7.396e-33 |
| 75 | Adam | 757.760537 | 50.819386 | 0.062035 |
| 75 | update-only conductor Adam | 787.818697 | 1.050e-29 | 1.344e-32 |
| 150 | Adam | 2.124e+03 | 144.917846 | 0.063181 |
| 150 | update-only conductor Adam | 2.280e+03 | 5.591e-29 | 2.461e-32 |
| 300 | Adam | 5.916e+03 | 394.853865 | 0.058409 |
| 300 | update-only conductor Adam | 6.160e+03 | 1.841e-28 | 2.998e-32 |

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
python empirical/conductor_calendar_transformer.py --task months --closed-conductors 3,4,6,12
```
