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
- generalization-gap delta vs Adam: `-2.175437`
- final logit-leakage delta vs Adam: `-0.643158`
- JSON payload: `C:\Projects\simplicial\empirical\reports\conductor_calendar_transformer_months.json`

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
- closed conductors: `12`

## Character Packets

| conductor | character indices | kept by filter |
|---:|---|---|
| 2 | `6` | no |
| 3 | `4, 8` | no |
| 4 | `3, 9` | no |
| 6 | `2, 10` | no |
| 12 | `1, 5, 7, 11` | yes |

## Final Metrics

| method | train loss | test loss | gen gap | train acc | test acc | acc gap | final logit leakage | output-update leakage | closed energy growth | leak energy growth |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Adam | 0.886851 | 6.125025 | 5.238174 | 0.708995 | 0.000000 | 0.708995 | 0.643158 | 0.660634 | 2.194e+03 | 4.110e+03 |
| update-only conductor Adam | 0.988646 | 4.051384 | 3.062737 | 0.708995 | 0.015873 | 0.693122 | 1.814e-31 | 1.380e-32 | 5.902e+03 | 1.060e-27 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.782505 | 6.822636 | 6.040132 | 0.777778 | 0.000000 | 0.748287 |
| 9101 | update-only conductor Adam | 0.965137 | 4.072962 | 3.107825 | 0.730159 | 0.000000 | 1.552e-31 |
| 9102 | Adam | 1.144067 | 5.430185 | 4.286118 | 0.539683 | 0.000000 | 0.661234 |
| 9102 | update-only conductor Adam | 1.097936 | 4.156299 | 3.058363 | 0.619048 | 0.000000 | 2.224e-31 |
| 9103 | Adam | 0.733982 | 6.122253 | 5.388272 | 0.809524 | 0.000000 | 0.519953 |
| 9103 | update-only conductor Adam | 0.902867 | 3.924890 | 3.022024 | 0.777778 | 0.047619 | 1.666e-31 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 2.064719 | 3.928676 | 0.665588 |
| 0 | update-only conductor Adam | 2.064719 | 1.039e-31 | 5.055e-32 |
| 1 | Adam | 1.787609 | 3.368060 | 0.663964 |
| 1 | update-only conductor Adam | 1.920099 | 1.208e-31 | 6.503e-32 |
| 75 | Adam | 383.603059 | 424.976864 | 0.527430 |
| 75 | update-only conductor Adam | 531.324665 | 4.519e-29 | 8.518e-32 |
| 150 | Adam | 950.754752 | 1.318e+03 | 0.582059 |
| 150 | update-only conductor Adam | 1.565e+03 | 2.115e-28 | 1.341e-31 |
| 300 | Adam | 2.196e+03 | 4.114e+03 | 0.643158 |
| 300 | update-only conductor Adam | 5.904e+03 | 1.060e-27 | 1.814e-31 |

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
python empirical/conductor_calendar_transformer.py --task months --closed-conductors primitive
```
