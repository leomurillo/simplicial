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
- generalization-gap delta vs Adam: `-3.679498`
- final logit-leakage delta vs Adam: `-0.592443`
- JSON payload: `empirical\reports\conductor_calendar_transformer_months_d64.json`

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
- model width / FF width: `64` / `128`
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
| Adam | 0.181103 | 9.083798 | 8.902695 | 0.968254 | 0.000000 | 0.968254 | 0.592443 | 0.588525 | 5.474e+03 | 8.075e+03 |
| update-only conductor Adam | 0.487221 | 5.710419 | 5.223197 | 0.878307 | 0.015873 | 0.862434 | 1.581e-31 | 1.597e-32 | 1.217e+04 | 1.945e-27 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.208864 | 8.414585 | 8.205721 | 0.968254 | 0.000000 | 0.670465 |
| 9101 | update-only conductor Adam | 0.569400 | 5.210532 | 4.641132 | 0.841270 | 0.000000 | 1.140e-31 |
| 9102 | Adam | 0.149764 | 9.274209 | 9.124445 | 0.984127 | 0.000000 | 0.623011 |
| 9102 | update-only conductor Adam | 0.499884 | 5.831304 | 5.331420 | 0.904762 | 0.047619 | 1.488e-31 |
| 9103 | Adam | 0.184681 | 9.562600 | 9.377919 | 0.952381 | 0.000000 | 0.483852 |
| 9103 | update-only conductor Adam | 0.392381 | 6.089420 | 5.697039 | 0.888889 | 0.000000 | 2.114e-31 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 3.370950 | 5.316157 | 0.621624 |
| 0 | update-only conductor Adam | 3.370950 | 2.071e-31 | 6.646e-32 |
| 1 | Adam | 3.708952 | 5.461332 | 0.629709 |
| 1 | update-only conductor Adam | 4.148719 | 2.600e-31 | 7.998e-32 |
| 75 | Adam | 707.823115 | 1.007e+03 | 0.583023 |
| 75 | update-only conductor Adam | 1.029e+03 | 7.390e-29 | 7.231e-32 |
| 150 | Adam | 2.562e+03 | 3.988e+03 | 0.605752 |
| 150 | update-only conductor Adam | 3.731e+03 | 3.699e-28 | 9.978e-32 |
| 300 | Adam | 5.477e+03 | 8.081e+03 | 0.592443 |
| 300 | update-only conductor Adam | 1.218e+04 | 1.946e-27 | 1.581e-31 |

## Per-Epoch Output Gradient Packet Norms

Values are seed means of the mean minibatch output-head gradient L2
norms before gradient clipping.  These gradients are not projected in
the conductor arm; only the resulting Adam update is filtered.

| epoch | method | cond 2 | cond 3 | cond 4 | cond 6 | cond 12 |
|---:|---|---:|---:|---:|---:|---:|
| 0 | Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 0 | update-only conductor Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 1 | Adam | 0.084222 | 0.088657 | 0.094451 | 0.136825 | 0.135462 |
| 1 | update-only conductor Adam | 0.083487 | 0.088788 | 0.093299 | 0.135427 | 0.135981 |
| 75 | Adam | 0.157830 | 0.253106 | 0.239957 | 0.222686 | 0.331002 |
| 75 | update-only conductor Adam | 0.133941 | 0.238589 | 0.277168 | 0.308310 | 0.305011 |
| 150 | Adam | 0.271913 | 0.412351 | 0.321792 | 0.363980 | 0.503784 |
| 150 | update-only conductor Adam | 0.284914 | 0.380143 | 0.410104 | 0.451051 | 0.445311 |
| 300 | Adam | 0.114423 | 0.187516 | 0.116706 | 0.140331 | 0.242734 |
| 300 | update-only conductor Adam | 0.185641 | 0.361928 | 0.368377 | 0.300420 | 0.330487 |

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
python empirical/conductor_calendar_transformer.py --task months --closed-conductors primitive --epochs 300 --batch-size 16 --d-model 64 --d-ff 128 --lr 0.0005
```
