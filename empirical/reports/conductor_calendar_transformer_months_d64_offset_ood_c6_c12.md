# Calendar Transformer Conductor Filter (months)

## Verdict

This is a small real-sequence training-loop pilot for the Pareto rule
`gradient projection 0%, update projection 100%`.  The model is a
trainable character-level attention classifier over the checked-in
months prompts; only the output-head Adam update is projected
in the cyclic character basis.
The projected arm starts with the output head in the same support,
then leaves the stochastic gradient and all Adam moments unprojected.

- test accuracy delta vs Adam: `+0.013889`
- generalization-gap delta vs Adam: `-0.203329`
- final logit-leakage delta vs Adam: `-0.092169`
- JSON payload: `empirical\reports\conductor_calendar_transformer_months_d64_offset_ood_c6_c12.json`

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
- closed conductors: `6, 12`

## Character Packets

| conductor | character indices | kept by filter |
|---:|---|---|
| 2 | `6` | no |
| 3 | `4, 8` | no |
| 4 | `3, 9` | no |
| 6 | `2, 10` | yes |
| 12 | `1, 5, 7, 11` | yes |

## Final Metrics

| method | train loss | test loss | gen gap | train acc | test acc | acc gap | final logit leakage | output-update leakage | closed energy growth | leak energy growth |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Adam | 0.145485 | 8.694958 | 8.549474 | 0.976852 | 0.050926 | 0.925926 | 0.092169 | 0.506961 | 2.430e+04 | 2.452e+03 |
| update-only conductor Adam | 0.223914 | 8.570058 | 8.346144 | 0.967593 | 0.064815 | 0.902778 | 1.369e-31 | 1.343e-32 | 2.942e+04 | 4.040e-27 |

## Per-Seed Results

| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |
|---:|---|---:|---:|---:|---:|---:|---:|
| 9101 | Adam | 0.130273 | 8.579241 | 8.448968 | 0.972222 | 0.055556 | 0.092177 |
| 9101 | update-only conductor Adam | 0.186411 | 8.751527 | 8.565116 | 0.972222 | 0.055556 | 1.355e-31 |
| 9102 | Adam | 0.131372 | 9.049469 | 8.918098 | 0.986111 | 0.027778 | 0.107623 |
| 9102 | update-only conductor Adam | 0.218015 | 8.340530 | 8.122516 | 0.972222 | 0.083333 | 1.132e-31 |
| 9103 | Adam | 0.174809 | 8.456165 | 8.281356 | 0.972222 | 0.069444 | 0.076709 |
| 9103 | update-only conductor Adam | 0.267315 | 8.618116 | 8.350801 | 0.958333 | 0.055556 | 1.619e-31 |

## Per-Epoch Energy Trace

Values below are seed means over the logits on all calendar cases.

| epoch | method | closed energy | leak energy | leakage |
|---:|---|---:|---:|---:|
| 0 | Adam | 7.474904 | 7.621652 | 0.492956 |
| 0 | update-only conductor Adam | 7.474904 | 3.762e-31 | 5.086e-32 |
| 1 | Adam | 7.104212 | 5.942035 | 0.452965 |
| 1 | update-only conductor Adam | 8.186598 | 4.754e-31 | 5.907e-32 |
| 75 | Adam | 3.386e+03 | 540.644278 | 0.138195 |
| 75 | update-only conductor Adam | 4.037e+03 | 2.593e-28 | 6.507e-32 |
| 150 | Adam | 1.169e+04 | 819.659041 | 0.065588 |
| 150 | update-only conductor Adam | 1.355e+04 | 1.117e-27 | 8.315e-32 |
| 300 | Adam | 2.431e+04 | 2.459e+03 | 0.092169 |
| 300 | update-only conductor Adam | 2.942e+04 | 4.040e-27 | 1.369e-31 |

## Per-Epoch Output Gradient Packet Norms

Values are seed means of the mean minibatch output-head gradient L2
norms before gradient clipping.  These gradients are not projected in
the conductor arm; only the resulting Adam update is filtered.

| epoch | method | cond 2 | cond 3 | cond 4 | cond 6 | cond 12 |
|---:|---|---:|---:|---:|---:|---:|
| 0 | Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 0 | update-only conductor Adam | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 1 | Adam | 0.067357 | 0.113930 | 0.142165 | 0.118274 | 0.134496 |
| 1 | update-only conductor Adam | 0.065670 | 0.113420 | 0.140045 | 0.118589 | 0.135409 |
| 75 | Adam | 0.183997 | 0.304294 | 0.295851 | 0.242096 | 0.418315 |
| 75 | update-only conductor Adam | 0.197959 | 0.347874 | 0.326796 | 0.258944 | 0.448692 |
| 150 | Adam | 0.285091 | 0.465345 | 0.402324 | 0.330887 | 0.473820 |
| 150 | update-only conductor Adam | 0.341148 | 0.512947 | 0.442507 | 0.309975 | 0.512407 |
| 300 | Adam | 0.148590 | 0.197613 | 0.165086 | 0.125173 | 0.214854 |
| 300 | update-only conductor Adam | 0.183552 | 0.257480 | 0.242972 | 0.168763 | 0.289066 |

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
python empirical/conductor_calendar_transformer.py --task months --split-mode offset_ood --train-offsets 1-6 --test-offsets 7-12 --closed-conductors 6,12 --epochs 300 --batch-size 16 --d-model 64 --d-ff 128 --lr 0.0005
```
