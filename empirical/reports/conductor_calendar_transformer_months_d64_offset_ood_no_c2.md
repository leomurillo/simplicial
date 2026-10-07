# Calendar Transformer Conductor Filter (months)

## Verdict

This is a small real-sequence training-loop pilot for the Pareto rule
`gradient projection 0%, update projection 100%`.  The model is a
trainable character-level attention classifier over the checked-in
months prompts; only the output-head Adam update is projected
in the cyclic character basis.
The projected arm starts with the output head in the same support,
then leaves the stochastic gradient and all Adam moments unprojected.

- test accuracy delta vs Adam: `-0.009259`
- generalization-gap delta vs Adam: `+0.085385`
- final logit-leakage delta vs Adam: `-0.006833`
- JSON payload: `empirical\reports\conductor_calendar_transformer_months_d64_offset_ood_no_c2.json`

This run uses an offset-OOD split: training examples use only the
declared train offsets, while test examples use offsets never seen
during training.  Missing calendar offsets are generated from the
exact cyclic label rule before tokenization.

## Setup

- task: `months`
- labels: `January, February, March, April, May, June, July, August, September, October, November, December`
- cases: `144`
- checked-in/generated cases: `84` / `60`
- split mode: `offset_ood`
- train offsets: `1, 2, 3, 4, 5, 6`
- test offsets: `7, 8, 9, 10, 11, 12`
- train/test split: `72` / `72`
- seeds: `3` starting at `9101`
- epochs: `300`
- batch size: `16`
- model width / FF width: `64` / `128`
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
| Adam | 0.145485 | 8.694958 | 8.549474 | 0.976852 | 0.050926 | 0.925926 | 0.006833 | 0.128540 | 2.657e+04 | 178.459125 |
| update-only conductor Adam | 0.150207 | 8.785066 | 8.634859 | 0.976852 | 0.041667 | 0.935185 | 3.702e-32 | 2.298e-33 | 2.769e+04 | 1.026e-27 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.130273 | 8.579241 | 8.448968 | 0.972222 | 0.055556 | 0.005122 |
| 9101 | update-only conductor Adam | 0.166782 | 8.386984 | 8.220203 | 0.972222 | 0.069444 | 6.064e-32 |
| 9102 | Adam | 0.131372 | 9.049469 | 8.918098 | 0.986111 | 0.027778 | 0.009946 |
| 9102 | update-only conductor Adam | 0.128045 | 9.387153 | 9.259108 | 0.972222 | 0.027778 | 2.996e-32 |
| 9103 | Adam | 0.174809 | 8.456165 | 8.281356 | 0.972222 | 0.069444 | 0.005430 |
| 9103 | update-only conductor Adam | 0.155796 | 8.581062 | 8.425266 | 0.986111 | 0.027778 | 2.046e-32 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 12.042788 | 3.053768 | 0.193447 |
| 0 | update-only conductor Adam | 12.042788 | 1.174e-31 | 9.814e-33 |
| 1 | Adam | 11.240282 | 1.805965 | 0.134820 |
| 1 | update-only conductor Adam | 11.502940 | 1.210e-31 | 1.058e-32 |
| 75 | Adam | 3.891e+03 | 35.740621 | 0.009169 |
| 75 | update-only conductor Adam | 4.118e+03 | 5.791e-29 | 1.412e-32 |
| 150 | Adam | 1.246e+04 | 52.162749 | 0.004100 |
| 150 | update-only conductor Adam | 1.292e+04 | 3.654e-28 | 2.827e-32 |
| 300 | Adam | 2.658e+04 | 181.512893 | 0.006833 |
| 300 | update-only conductor Adam | 2.771e+04 | 1.026e-27 | 3.702e-32 |

## Per-Epoch Output Gradient Packet Norms

Values are seed means of the mean minibatch output-head gradient L2
norms before gradient clipping.  These gradients are not projected in
the conductor arm; only the resulting Adam update is filtered.

| epoch | method | cond 2 | cond 3 | cond 4 | cond 6 | cond 12 |
|---:|---|---:|---:|---:|---:|---:|
| 0 | Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 0 | update-only conductor Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 1 | Adam | 0.067357 | 0.113930 | 0.142165 | 0.118274 | 0.134496 |
| 1 | update-only conductor Adam | 0.065595 | 0.114131 | 0.142302 | 0.118367 | 0.134690 |
| 75 | Adam | 0.183997 | 0.304294 | 0.295851 | 0.242096 | 0.418315 |
| 75 | update-only conductor Adam | 0.198131 | 0.309758 | 0.299128 | 0.248217 | 0.432919 |
| 150 | Adam | 0.285091 | 0.465345 | 0.402324 | 0.330887 | 0.473820 |
| 150 | update-only conductor Adam | 0.293877 | 0.473143 | 0.409127 | 0.325096 | 0.466500 |
| 300 | Adam | 0.148590 | 0.197613 | 0.165086 | 0.125173 | 0.214854 |
| 300 | update-only conductor Adam | 0.152603 | 0.217425 | 0.170343 | 0.134809 | 0.232559 |

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
python empirical/conductor_calendar_transformer.py --task months --split-mode offset_ood --train-offsets 1-6 --test-offsets 7-12 --closed-conductors 3,4,6,12 --epochs 300 --batch-size 16 --d-model 64 --d-ff 128 --lr 0.0005
```
