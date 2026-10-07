# Helmert Conductor-Flag Baseline

This audit compares conductor-respecting gauge blocks against Haar-random
orthogonal blocks with the same block sizes.  It reports both raw
off-centroid Fisher block coupling and a fuller subspace J ledger with
projection, closure, packet-respect, and resource terms.

The oracle eigenbasis is shown only as a sanity check.  It diagonalizes
the single tested Fisher matrix and is not a fixed arithmetic descent.

## Config

- `rows`: `['f4-u2']`
- `samples`: `1000`
- `seed`: `20260515`
- `amplitude_fraction`: `0.35`
- `ledger_weights`: `{'block': 1.0, 'mix': 2.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`
- `skip_lowest`: `True`

## Summary

| row | target packet | active dim | conductor J | random J median | random better J | full-J frame price max | raw frame price max | conductor coupling | random better raw |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F_4[u]/(u^2) | u^2 | 15 | 0.479846 | 0.833312 | 0/1000 | 1.81929 | 1.81929 | 0.279846 | 728/1000 |

## Detail

### F_4[u]/(u^2) target `u^2`

- probability range: `0.0417187` to `0.124844`
- actual displacement amplitude: `0.083125`
- active prefix dimension: `15` at depth `2`
- conductor full J: `0.479846382332`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `1.81929`
- conductor block coupling: `0.279846382332`
- random mixed better fraction: `0.728`
- mix impurity weight: `2`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `1.81929`
- packet-respecting random spread: `7.772e-16`
- oracle eigenbasis block coupling: `1.153e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.0868089 | 0.151888 | 0.2418 | 0.246542 | 0.358845 | 0.49021 |
| random mixed full J | 0.496798 | 0.653786 | 0.833312 | 0.834218 | 1.02689 | 1.25616 |
| full-J frame price | 0 | 0 | 0.193187 | 0.25417 | 0.729069 | 1.81929 |
| random mixed total cost | 0.296798 | 0.453786 | 0.633312 | 0.634218 | 0.826894 | 1.05616 |
| break-even mix weight | 0 | 0 | 0.193187 | 0.25417 | 0.729069 | 1.81929 |
| packet-respecting coupling | 0.279846 | 0.279846 | 0.279846 | 0.279846 | 0.279846 | 0.279846 |
| packet-commutator impurity | 0.0470345 | 0.117009 | 0.192603 | 0.193838 | 0.267118 | 0.357402 |
| random mixed packet purity | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.279846 | 0.2418 | 0.151888 | 0.358845 |
| mix_impurity | 0 | 0.192603 | 0.117009 | 0.267118 |
| fisher_projection_error | 0 | 0 | 0 | 4.44089e-16 |
| reciprocal_projection_error | 0 | 3.33067e-16 | 0 | 5.55112e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |

## Reading

A zero `random better raw` count is evidence that generic mixed Helmert
flags are worse even before pricing conductor respect.  A nonzero raw
count shows that Fisher block coupling alone is not the right structural
objective: a p-dependent or mixed flag can partially diagonalize one
local Fisher matrix.  The break-even mix price reports how much packet
respect must be worth before the conductor flag beats every sampled
mixed flag under this two-term score.  Here packet respect is measured
by projector-commutator impurity against the conductor packet
decomposition.  The full J columns add prefix-subspace projection,
reciprocal projection, additive closure leakage, resource, and depth
costs.  The decisive falsifier is therefore a sampled mixed flag with
lower full J than the conductor prefix at the same active dimension.
