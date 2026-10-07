# Calendar Transformer Conductor Filter (months)

## Verdict

This is a small real-sequence training-loop pilot for the Pareto rule
`gradient projection 0%, update projection 100%`.  The model is a
trainable character-level attention classifier over the checked-in
months prompts; only the output-head Adam update is projected
in the cyclic character basis.
The projected arm starts with the output head in the same support,
then leaves the stochastic gradient and all Adam moments unprojected.

- test accuracy delta vs Adam: `-0.027778`
- generalization-gap delta vs Adam: `+0.168510`
- final logit-leakage delta vs Adam: `-0.285408`
- JSON payload: `empirical\reports\conductor_calendar_transformer_months_d64_offset_ood.json`

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
| Adam | 0.145485 | 8.694958 | 8.549474 | 0.976852 | 0.050926 | 0.925926 | 0.285408 | 0.660256 | 1.913e+04 | 7.615e+03 |
| update-only conductor Adam | 0.472598 | 9.190582 | 8.717984 | 0.837963 | 0.023148 | 0.814815 | 1.600e-31 | 1.524e-32 | 3.302e+04 | 5.144e-27 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.130273 | 8.579241 | 8.448968 | 0.972222 | 0.055556 | 0.299993 |
| 9101 | update-only conductor Adam | 0.518136 | 8.572905 | 8.054769 | 0.875000 | 0.041667 | 2.363e-31 |
| 9102 | Adam | 0.131372 | 9.049469 | 8.918098 | 0.986111 | 0.027778 | 0.310993 |
| 9102 | update-only conductor Adam | 0.413771 | 9.832608 | 9.418837 | 0.819444 | 0.013889 | 1.059e-31 |
| 9103 | Adam | 0.174809 | 8.456165 | 8.281356 | 0.972222 | 0.069444 | 0.245239 |
| 9103 | update-only conductor Adam | 0.485887 | 9.166233 | 8.680346 | 0.819444 | 0.013889 | 1.376e-31 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 5.274553 | 9.822003 | 0.647769 |
| 0 | update-only conductor Adam | 5.274553 | 3.787e-31 | 7.195e-32 |
| 1 | Adam | 5.091186 | 7.955061 | 0.610133 |
| 1 | update-only conductor Adam | 6.295790 | 4.490e-31 | 7.240e-32 |
| 75 | Adam | 2.563e+03 | 1.363e+03 | 0.347365 |
| 75 | update-only conductor Adam | 3.715e+03 | 2.377e-28 | 6.442e-32 |
| 150 | Adam | 9.878e+03 | 2.633e+03 | 0.210850 |
| 150 | update-only conductor Adam | 1.499e+04 | 1.123e-27 | 7.749e-32 |
| 300 | Adam | 1.914e+04 | 7.625e+03 | 0.285408 |
| 300 | update-only conductor Adam | 3.302e+04 | 5.144e-27 | 1.600e-31 |

## Per-Epoch Output Gradient Packet Norms

Values are seed means of the mean minibatch output-head gradient L2
norms before gradient clipping.  These gradients are not projected in
the conductor arm; only the resulting Adam update is filtered.

| epoch | method | cond 2 | cond 3 | cond 4 | cond 6 | cond 12 |
|---:|---|---:|---:|---:|---:|---:|
| 0 | Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 0 | update-only conductor Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 1 | Adam | 0.067357 | 0.113930 | 0.142165 | 0.118274 | 0.134496 |
| 1 | update-only conductor Adam | 0.065686 | 0.113413 | 0.140073 | 0.117335 | 0.135935 |
| 75 | Adam | 0.183997 | 0.304294 | 0.295851 | 0.242096 | 0.418315 |
| 75 | update-only conductor Adam | 0.203777 | 0.346913 | 0.322767 | 0.283265 | 0.435596 |
| 150 | Adam | 0.285091 | 0.465345 | 0.402324 | 0.330887 | 0.473820 |
| 150 | update-only conductor Adam | 0.375114 | 0.561209 | 0.520580 | 0.392531 | 0.579728 |
| 300 | Adam | 0.148590 | 0.197613 | 0.165086 | 0.125173 | 0.214854 |
| 300 | update-only conductor Adam | 0.194207 | 0.362732 | 0.413203 | 0.322437 | 0.488522 |

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
python empirical/conductor_calendar_transformer.py --task months --split-mode offset_ood --train-offsets 1-6 --test-offsets 7-12 --closed-conductors primitive --epochs 300 --batch-size 16 --d-model 64 --d-ff 128 --lr 0.0005
```
