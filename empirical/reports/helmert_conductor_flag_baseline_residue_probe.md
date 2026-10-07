# Helmert Conductor-Flag Baseline

This audit compares conductor-respecting gauge blocks against Haar-random
orthogonal blocks with the same block sizes.  It reports both raw
off-centroid Fisher block coupling and a fuller subspace J ledger with
projection, closure, packet-respect, and resource terms.

The oracle eigenbasis is shown only as a sanity check.  It diagonalizes
the single tested Fisher matrix and is not a fixed arithmetic descent.

## Config

- `rows`: `['f4-u3', 'f8-u2']`
- `samples`: `300`
- `seed`: `20260515`
- `amplitude_fraction`: `0.35`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`
- `skip_lowest`: `True`

## Summary

| row | target packet | active dim | conductor J | random J median | random better J | full-J frame price max | raw frame price max | conductor coupling | random better raw |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F_4[u]/(u^3) | u^2 | 15 | 0.370323 | 3.4794 | 0/300 | 0 | 0 | 0.279846 | 0/300 |
| F_4[u]/(u^3) | u^3 | 63 | 0.567211 | 0.843245 | 0/300 | 0.505772 | 0.505772 | 0.367211 | 182/300 |
| F_8[u]/(u^2) | u^2 | 63 | 0.474524 | 0.670812 | 0/300 | 0.235752 | 0.235752 | 0.274524 | 3/300 |

## Detail

### F_4[u]/(u^3) target `u^2`

- probability range: `0.0104297` to `0.0312109`
- actual displacement amplitude: `0.083125`
- active prefix dimension: `15` at depth `2`
- conductor full J: `0.370322572808`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0`
- conductor block coupling: `0.279846382332`
- random mixed better fraction: `0`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0`
- packet-respecting random spread: `6.661e-16`
- oracle eigenbasis block coupling: `9.344e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 1.10451 | 1.21919 | 1.35235 | 1.35119 | 1.46743 | 1.57031 |
| random mixed full J | 2.88259 | 3.08377 | 3.4794 | 3.49741 | 4.00704 | 4.2919 |
| full-J frame price | 0 | 0 | 0 | 0 | 0 | 0 |
| random mixed total cost | 1.39214 | 1.503 | 1.63999 | 1.63704 | 1.75805 | 1.84251 |
| break-even mix weight | 0 | 0 | 0 | 0 | 0 | 0 |
| packet-respecting coupling | 0.279846 | 0.279846 | 0.279846 | 0.279846 | 0.279846 | 0.279846 |
| packet-commutator impurity | 0.246829 | 0.263636 | 0.285027 | 0.285846 | 0.30768 | 0.331478 |
| random mixed packet purity | 0.761905 | 0.761905 | 0.761905 | 0.761905 | 0.761905 | 0.761905 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.279846 | 1.35235 | 1.21919 | 1.46743 |
| mix_impurity | 0 | 0.285027 | 0.263636 | 0.30768 |
| fisher_projection_error | 0 | 0.77182 | 0.640688 | 0.882239 |
| reciprocal_projection_error | 0 | 0.765009 | 0.634799 | 0.872592 |
| closure_leakage | 0 | 0.193163 | 0 | 0.718966 |
| resource_cost | 0.238095 | 0.238095 | 0.238095 | 0.238095 |
| depth_cost | 0.666667 | 0.666667 | 0.666667 | 0.666667 |

### F_4[u]/(u^3) target `u^3`

- probability range: `0.0104297` to `0.0312109`
- actual displacement amplitude: `0.0207812`
- active prefix dimension: `63` at depth `3`
- conductor full J: `0.567211034131`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0.505772`
- conductor block coupling: `0.367211034131`
- random mixed better fraction: `0.606667`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0.505772`
- packet-respecting random spread: `3.886e-16`
- oracle eigenbasis block coupling: `2.615e-29`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.227775 | 0.282788 | 0.356916 | 0.354271 | 0.421686 | 0.451159 |
| random mixed full J | 0.701633 | 0.755837 | 0.843245 | 0.840318 | 0.908821 | 0.965214 |
| full-J frame price | 0 | 0 | 0.0369852 | 0.0862624 | 0.308756 | 0.505772 |
| random mixed total cost | 0.501633 | 0.555837 | 0.643245 | 0.640318 | 0.708821 | 0.765214 |
| break-even mix weight | 0 | 0 | 0.0369852 | 0.0862624 | 0.308756 | 0.505772 |
| packet-respecting coupling | 0.367211 | 0.367211 | 0.367211 | 0.367211 | 0.367211 | 0.367211 |
| packet-commutator impurity | 0.247822 | 0.262119 | 0.286724 | 0.286047 | 0.309185 | 0.326213 |
| random mixed packet purity | 0.761905 | 0.761905 | 0.761905 | 0.761905 | 0.761905 | 0.761905 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.367211 | 0.356916 | 0.282788 | 0.421686 |
| mix_impurity | 0 | 0.286724 | 0.262119 | 0.309185 |
| fisher_projection_error | 0 | 0 | 0 | 3.38618e-16 |
| reciprocal_projection_error | 0 | 2.22045e-16 | 0 | 4.44089e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |

### F_8[u]/(u^2) target `u^2`

- probability range: `0.0104297` to `0.0519922`
- actual displacement amplitude: `0.0415625`
- active prefix dimension: `63` at depth `2`
- conductor full J: `0.474524253721`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0.235752`
- conductor block coupling: `0.274524253721`
- random mixed better fraction: `0.01`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0.235752`
- packet-respecting random spread: `4.441e-16`
- oracle eigenbasis block coupling: `1.538e-29`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.25222 | 0.305038 | 0.395159 | 0.395898 | 0.481489 | 0.555812 |
| random mixed full J | 0.543302 | 0.58366 | 0.670812 | 0.671533 | 0.753378 | 0.830312 |
| full-J frame price | 0 | 0 | 0 | 0.00188677 | 0 | 0.235752 |
| random mixed total cost | 0.343302 | 0.38366 | 0.470812 | 0.471533 | 0.553378 | 0.630312 |
| break-even mix weight | 0 | 0 | 0 | 0.00188677 | 0 | 0.235752 |
| packet-respecting coupling | 0.274524 | 0.274524 | 0.274524 | 0.274524 | 0.274524 | 0.274524 |
| packet-commutator impurity | 0.0445899 | 0.0589306 | 0.0754857 | 0.0756354 | 0.0912295 | 0.110023 |
| random mixed packet purity | 0.888889 | 0.888889 | 0.888889 | 0.888889 | 0.888889 | 0.888889 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.274524 | 0.395159 | 0.305038 | 0.481489 |
| mix_impurity | 0 | 0.0754857 | 0.0589306 | 0.0912295 |
| fisher_projection_error | 0 | 0 | 0 | 3.33067e-16 |
| reciprocal_projection_error | 0 | 2.22045e-16 | 0 | 4.44089e-16 |
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
