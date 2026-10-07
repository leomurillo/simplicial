# Learned B4 Normalizer-Transfer Experiment

## Verdict

This is a direct learned update test of the B4 premium rule on
`F4[u]/(u^2)`.  Each held-out target is a normalizer transform of a
source support.  Policies train from samples using the same stochastic
Adam update loop, but their applied updates are projected into the
source-declared support.

- transfer cases: `32`
- mean measured transfer gain B3 over B2: `0.072084`
- mean resource-weighted premium: `0.212500`
- mean measured net gain: `-0.140416`
- implied break-even resource weight: `0.084805`
- B3 beats B2 by measured J rate: `0.000`

## Setup

- row: `F_4[u]/(u^2)`
- source tasks / transfers per source: `8` / `4`
- contexts: `32`
- training steps: `800`
- batch size: `96`
- signal scale: `2.0`
- learning rate: `0.08`
- resource weight: `0.25`
- gradient/update projection: `0.0` / `1.0`
- nontrivial transfers only: `True`

Measured J is `final_true_kl + resource_weight * resource_cost`.
The primary transfer gain is the measured KL improvement of source B3
over source B2 on the held-out target.

## Policy Summary

| policy | wins | support | resource | target coverage | target proj leak | KL | policy leak | K^CH leak | measured J |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| oracle target B2 | 32 | 2.250000 | 0.150000 | 1.000000 | 2.073e-33 | 0.005999 | 2.716e-33 | 2.619e-33 | 0.043499 |
| random B2 budget | 0 | 2.250000 | 0.150000 | 0.156250 | 0.853234 | 0.101492 | 0.005394 | 0.536443 | 0.138992 |
| source raw | 0 | 1.625000 | 0.108333 | 0.031250 | 0.966253 | 0.114285 | 0.001834 | 0.597320 | 0.141369 |
| source B2 | 0 | 2.250000 | 0.150000 | 0.046875 | 0.952786 | 0.114004 | 9.621e-34 | 1.959e-33 | 0.151504 |
| source conductor packet | 0 | 12.750000 | 0.850000 | 1.000000 | 5.706e-34 | 0.036212 | 0.010949 | 0.201242 | 0.248712 |
| full | 0 | 15.000000 | 1.000000 | 1.000000 | 0.000000 | 0.041921 | 0.000000 | 0.000000 | 0.291921 |
| random B3 budget | 0 | 15.000000 | 1.000000 | 1.000000 | 0.000000 | 0.041921 | 0.000000 | 0.000000 | 0.291921 |
| source B3 | 0 | 15.000000 | 1.000000 | 1.000000 | 0.000000 | 0.041921 | 0.000000 | 0.000000 | 0.291921 |

## Payoff Examples

- source `w+1+u` -> target `1+wu`; B2/B3 sizes `1`/`15`; gain/premium/net `0.028461`/`0.233333`/`-0.204872`; winner `oracle target B2`
- source `w+1+u` -> target `w+1`; B2/B3 sizes `1`/`15`; gain/premium/net `0.024280`/`0.233333`/`-0.209053`; winner `oracle target B2`
- source `w+1+u` -> target `w+(w+1)u`; B2/B3 sizes `1`/`15`; gain/premium/net `0.023985`/`0.233333`/`-0.209348`; winner `oracle target B2`
- source `w+1+u` -> target `1+wu`; B2/B3 sizes `1`/`15`; gain/premium/net `0.021320`/`0.233333`/`-0.212013`; winner `oracle target B2`
- source `w+wu, wu` -> target `(w+1)u, w+1+(w+1)u`; B2/B3 sizes `3`/`15`; gain/premium/net `0.104959`/`0.200000`/`-0.095041`; winner `oracle target B2`
- source `w+wu, wu` -> target `w+(w+1)u, wu`; B2/B3 sizes `3`/`15`; gain/premium/net `0.041269`/`0.200000`/`-0.158731`; winner `oracle target B2`

## Reading

This is stronger than the earlier support-only B4 audit because the numbers
come after stochastic training on target samples.  It is still scoped:
the model is a free context-logit table, so the result tests support-policy
investment under learned updates, not representation learning in a deep
network.

A positive result here means the next A0 test should introduce a shared
parameterization or real checkpoint dynamics.  A negative result would
say that the support-level premium/gain rule is not enough once learned
updates and finite samples enter.

## Reproduction

```powershell
python empirical/learned_normalizer_transfer_experiment.py
python empirical/learned_normalizer_transfer_experiment.py --check empirical/reports/learned_normalizer_transfer_f4_u2.json
```
