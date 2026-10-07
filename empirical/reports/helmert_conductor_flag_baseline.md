# Helmert Conductor-Flag Baseline

This audit compares conductor-respecting gauge blocks against Haar-random
orthogonal blocks with the same block sizes.  It reports both raw
off-centroid Fisher block coupling and a fuller subspace J ledger with
projection, closure, packet-respect, and resource terms.

The oracle eigenbasis is shown only as a sanity check.  It diagonalizes
the single tested Fisher matrix and is not a fixed arithmetic descent.

## Config

- `rows`: `['f4-u2', 'f2-u4', 'f2-u5']`
- `samples`: `1000`
- `seed`: `20260515`
- `amplitude_fraction`: `0.35`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`
- `skip_lowest`: `True`

## Summary

| row | target packet | active dim | conductor J | random J median | random better J | full-J frame price max | raw frame price max | conductor coupling | random better raw |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F_4[u]/(u^2) | u^2 | 15 | 0.479846 | 0.636233 | 12/1000 | 1.81929 | 1.81929 | 0.279846 | 728/1000 |
| F_2[u]/(u^4) | u^2 | 3 | 0.209748 | 3.45183 | 0/1000 | 0 | 0 | 0.139748 | 0/1000 |
| F_2[u]/(u^4) | u^3 | 7 | 0.335152 | 2.44114 | 0/1000 | 0 | 0.0698086 | 0.213485 | 15/1000 |
| F_2[u]/(u^4) | u^4 | 15 | 0.451319 | 1.0955 | 0/1000 | 0.284626 | 0.284626 | 0.251319 | 1000/1000 |
| F_2[u]/(u^5) | u^2 | 3 | 0.189426 | 4.59111 | 0/1000 | 0 | 0 | 0.139748 | 0/1000 |
| F_2[u]/(u^5) | u^3 | 7 | 0.296066 | 3.43432 | 0/1000 | 0 | 0 | 0.213485 | 0/1000 |
| F_2[u]/(u^5) | u^4 | 15 | 0.379706 | 2.49862 | 0/1000 | 0 | 0 | 0.251319 | 0/1000 |
| F_2[u]/(u^5) | u^5 | 31 | 0.470477 | 1.19304 | 0/1000 | 0.189312 | 0.189312 | 0.270477 | 1000/1000 |

## Detail

### F_4[u]/(u^2) target `u^2`

- probability range: `0.0417187` to `0.124844`
- actual displacement amplitude: `0.083125`
- active prefix dimension: `15` at depth `2`
- conductor full J: `0.479846382332`
- random mixed better fraction by full J: `0.012`
- max full-J frame price among sampled random flags: `1.81929`
- conductor block coupling: `0.279846382332`
- random mixed better fraction: `0.728`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0.012`
- max break-even mix price among sampled random flags: `1.81929`
- packet-respecting random spread: `7.772e-16`
- oracle eigenbasis block coupling: `1.153e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.0868089 | 0.151888 | 0.2418 | 0.246542 | 0.358845 | 0.49021 |
| random mixed full J | 0.402993 | 0.521105 | 0.636233 | 0.64038 | 0.777106 | 0.952149 |
| full-J frame price | 0 | 0 | 0.193187 | 0.25417 | 0.729069 | 1.81929 |
| random mixed total cost | 0.202993 | 0.321105 | 0.436233 | 0.44038 | 0.577106 | 0.752149 |
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

### F_2[u]/(u^4) target `u^2`

- probability range: `0.0417187` to `0.0832813`
- actual displacement amplitude: `0.16625`
- active prefix dimension: `3` at depth `2`
- conductor full J: `0.209748232519`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0`
- conductor block coupling: `0.139748232519`
- random mixed better fraction: `0`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0`
- packet-respecting random spread: `3.608e-16`
- oracle eigenbasis block coupling: `2.750e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.380973 | 0.491629 | 0.610689 | 0.607695 | 0.714599 | 0.789572 |
| random mixed full J | 1.85659 | 2.66705 | 3.45183 | 3.43374 | 4.06431 | 4.29404 |
| full-J frame price | 0 | 0 | 0 | 0 | 0 | 0 |
| random mixed total cost | 1.06163 | 1.19434 | 1.34891 | 1.3416 | 1.47041 | 1.55166 |
| break-even mix weight | 0 | 0 | 0 | 0 | 0 | 0 |
| packet-respecting coupling | 0.139748 | 0.139748 | 0.139748 | 0.139748 | 0.139748 | 0.139748 |
| packet-commutator impurity | 0.504899 | 0.64157 | 0.736114 | 0.733909 | 0.810947 | 0.871944 |
| random mixed packet purity | 0.533333 | 0.533333 | 0.533333 | 0.537451 | 0.556358 | 0.588709 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.139748 | 0.610689 | 0.491629 | 0.714599 |
| mix_impurity | 0 | 0.736114 | 0.64157 | 0.810947 |
| fisher_projection_error | 0 | 0.82948 | 0.544298 | 0.976188 |
| reciprocal_projection_error | 0 | 0.826456 | 0.555422 | 0.975157 |
| closure_leakage | 0 | 0.504361 | 0 | 0.821187 |
| resource_cost | 0.2 | 0.2 | 0.2 | 0.2 |
| depth_cost | 0.5 | 0.5 | 0.5 | 0.5 |

### F_2[u]/(u^4) target `u^3`

- probability range: `0.0417187` to `0.0832813`
- actual displacement amplitude: `0.083125`
- active prefix dimension: `7` at depth `3`
- conductor full J: `0.335151525579`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0`
- conductor block coupling: `0.213484858912`
- random mixed better fraction: `0.015`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0.0698086`
- packet-respecting random spread: `4.718e-16`
- oracle eigenbasis block coupling: `2.007e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.168912 | 0.237285 | 0.314342 | 0.311531 | 0.377519 | 0.413248 |
| random mixed full J | 1.43683 | 1.79272 | 2.44114 | 2.48407 | 3.29869 | 3.80492 |
| full-J frame price | 0 | 0 | 0 | 0 | 0 | 0 |
| random mixed total cost | 0.768795 | 0.921585 | 1.0448 | 1.043 | 1.15278 | 1.24872 |
| break-even mix weight | 0 | 0 | 0 | 0.00028762 | 0 | 0.0698086 |
| packet-respecting coupling | 0.213485 | 0.213485 | 0.213485 | 0.213485 | 0.213485 | 0.213485 |
| packet-commutator impurity | 0.558898 | 0.633813 | 0.735016 | 0.731466 | 0.811421 | 0.877971 |
| random mixed packet purity | 0.533333 | 0.533333 | 0.533333 | 0.538153 | 0.559113 | 0.631157 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.213485 | 0.314342 | 0.237285 | 0.377519 |
| mix_impurity | 0 | 0.735016 | 0.633813 | 0.811421 |
| fisher_projection_error | 0 | 0.530217 | 0.251647 | 0.809956 |
| reciprocal_projection_error | 0 | 0.539185 | 0.237028 | 0.807094 |
| closure_leakage | 0 | 0.11056 | 0 | 0.813678 |
| resource_cost | 0.466667 | 0.466667 | 0.466667 | 0.466667 |
| depth_cost | 0.75 | 0.75 | 0.75 | 0.75 |

### F_2[u]/(u^4) target `u^4`

- probability range: `0.0417187` to `0.0832813`
- actual displacement amplitude: `0.0415625`
- active prefix dimension: `15` at depth `4`
- conductor full J: `0.451318799642`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0.284626`
- conductor block coupling: `0.251318799642`
- random mixed better fraction: `1`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0.284626`
- packet-respecting random spread: `4.996e-16`
- oracle eigenbasis block coupling: `1.532e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.0520924 | 0.104091 | 0.161598 | 0.157705 | 0.197759 | 0.233776 |
| random mixed full J | 0.898082 | 0.990461 | 1.0955 | 1.09114 | 1.18088 | 1.25116 |
| full-J frame price | 0.0255953 | 0.0734721 | 0.121708 | 0.12813 | 0.201223 | 0.284626 |
| random mixed total cost | 0.698082 | 0.790461 | 0.895498 | 0.891144 | 0.980879 | 1.05116 |
| break-even mix weight | 0.0255953 | 0.0734721 | 0.121708 | 0.12813 | 0.201223 | 0.284626 |
| packet-respecting coupling | 0.251319 | 0.251319 | 0.251319 | 0.251319 | 0.251319 | 0.251319 |
| packet-commutator impurity | 0.563383 | 0.643379 | 0.738288 | 0.733439 | 0.811725 | 0.88337 |
| random mixed packet purity | 0.533333 | 0.533333 | 0.533333 | 0.537644 | 0.558054 | 0.607185 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.251319 | 0.161598 | 0.104091 | 0.197759 |
| mix_impurity | 0 | 0.738288 | 0.643379 | 0.811725 |
| fisher_projection_error | 0 | 0 | 0 | 3.33067e-16 |
| reciprocal_projection_error | 0 | 0 | 0 | 3.33067e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |

### F_2[u]/(u^5) target `u^2`

- probability range: `0.0208594` to `0.0416406`
- actual displacement amplitude: `0.16625`
- active prefix dimension: `3` at depth `2`
- conductor full J: `0.189425651874`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0`
- conductor block coupling: `0.139748232519`
- random mixed better fraction: `0`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0`
- packet-respecting random spread: `3.053e-16`
- oracle eigenbasis block coupling: `1.233e-29`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 1.16834 | 1.27252 | 1.38469 | 1.38544 | 1.49732 | 1.62275 |
| random mixed full J | 3.54792 | 3.89369 | 4.59111 | 4.51413 | 5.01005 | 5.20848 |
| full-J frame price | 0 | 0 | 0 | 0 | 0 | 0 |
| random mixed total cost | 1.97565 | 2.07421 | 2.19345 | 2.19343 | 2.31652 | 2.44056 |
| break-even mix weight | 0 | 0 | 0 | 0 | 0 | 0 |
| packet-respecting coupling | 0.139748 | 0.139748 | 0.139748 | 0.139748 | 0.139748 | 0.139748 |
| packet-commutator impurity | 0.722698 | 0.769392 | 0.808314 | 0.807994 | 0.847796 | 0.879625 |
| random mixed packet purity | 0.516129 | 0.516129 | 0.516129 | 0.51665 | 0.519883 | 0.529189 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.139748 | 1.38469 | 1.27252 | 1.49732 |
| mix_impurity | 0 | 0.808314 | 0.769392 | 0.847796 |
| fisher_projection_error | 0 | 0.917492 | 0.764575 | 0.988728 |
| reciprocal_projection_error | 0 | 0.920253 | 0.763299 | 0.988677 |
| closure_leakage | 0 | 0.602741 | 0 | 0.831786 |
| resource_cost | 0.0967742 | 0.0967742 | 0.0967742 | 0.0967742 |
| depth_cost | 0.4 | 0.4 | 0.4 | 0.4 |

### F_2[u]/(u^5) target `u^3`

- probability range: `0.0208594` to `0.0416406`
- actual displacement amplitude: `0.083125`
- active prefix dimension: `7` at depth `3`
- conductor full J: `0.296065504073`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0`
- conductor block coupling: `0.213484858912`
- random mixed better fraction: `0`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0`
- packet-respecting random spread: `5.551e-16`
- oracle eigenbasis block coupling: `6.514e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.565403 | 0.636593 | 0.710613 | 0.709421 | 0.781479 | 0.833907 |
| random mixed full J | 2.39172 | 2.87265 | 3.43432 | 3.47208 | 4.11425 | 4.38571 |
| full-J frame price | 0 | 0 | 0 | 0 | 0 | 0 |
| random mixed total cost | 1.36943 | 1.43512 | 1.51771 | 1.51716 | 1.5947 | 1.67408 |
| break-even mix weight | 0 | 0 | 0 | 0 | 0 | 0 |
| packet-respecting coupling | 0.213485 | 0.213485 | 0.213485 | 0.213485 | 0.213485 | 0.213485 |
| packet-commutator impurity | 0.734874 | 0.769346 | 0.806998 | 0.80774 | 0.845448 | 0.884026 |
| random mixed packet purity | 0.516129 | 0.516129 | 0.516129 | 0.516726 | 0.520313 | 0.535233 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.213485 | 0.710613 | 0.636593 | 0.781479 |
| mix_impurity | 0 | 0.806998 | 0.769346 | 0.845448 |
| fisher_projection_error | 0 | 0.784642 | 0.568568 | 0.924737 |
| reciprocal_projection_error | 0 | 0.781637 | 0.586687 | 0.922022 |
| closure_leakage | 0 | 0.284524 | 0 | 0.852505 |
| resource_cost | 0.225806 | 0.225806 | 0.225806 | 0.225806 |
| depth_cost | 0.6 | 0.6 | 0.6 | 0.6 |

### F_2[u]/(u^5) target `u^4`

- probability range: `0.0208594` to `0.0416406`
- actual displacement amplitude: `0.0415625`
- active prefix dimension: `15` at depth `4`
- conductor full J: `0.379705896416`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0`
- conductor block coupling: `0.251318799642`
- random mixed better fraction: `0`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0`
- packet-respecting random spread: `4.996e-16`
- oracle eigenbasis block coupling: `5.684e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.25858 | 0.306475 | 0.361217 | 0.359709 | 0.408648 | 0.444206 |
| random mixed full J | 1.68416 | 2.0099 | 2.49862 | 2.53527 | 3.18238 | 3.69092 |
| full-J frame price | 0 | 0 | 0 | 0 | 0 | 0 |
| random mixed total cost | 1.00508 | 1.10254 | 1.16833 | 1.16667 | 1.22833 | 1.29549 |
| break-even mix weight | 0 | 0 | 0 | 0 | 0 | 0 |
| packet-respecting coupling | 0.251319 | 0.251319 | 0.251319 | 0.251319 | 0.251319 | 0.251319 |
| packet-commutator impurity | 0.722564 | 0.764324 | 0.808564 | 0.806961 | 0.846816 | 0.86641 |
| random mixed packet purity | 0.516129 | 0.516129 | 0.516129 | 0.516734 | 0.520669 | 0.530147 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.251319 | 0.361217 | 0.306475 | 0.408648 |
| mix_impurity | 0 | 0.808564 | 0.764324 | 0.846816 |
| fisher_projection_error | 0 | 0.52527 | 0.322693 | 0.729955 |
| reciprocal_projection_error | 0 | 0.517564 | 0.325879 | 0.715376 |
| closure_leakage | 0 | 0.055021 | 0 | 0.710651 |
| resource_cost | 0.483871 | 0.483871 | 0.483871 | 0.483871 |
| depth_cost | 0.8 | 0.8 | 0.8 | 0.8 |

### F_2[u]/(u^5) target `u^5`

- probability range: `0.0208594` to `0.0416406`
- actual displacement amplitude: `0.0207812`
- active prefix dimension: `31` at depth `5`
- conductor full J: `0.47047717689`
- random mixed better fraction by full J: `0`
- max full-J frame price among sampled random flags: `0.189312`
- conductor block coupling: `0.27047717689`
- random mixed better fraction: `1`
- mix impurity weight: `1`
- random mixed better fraction after mix price: `0`
- max break-even mix price among sampled random flags: `0.189312`
- packet-respecting random spread: `4.996e-16`
- oracle eigenbasis block coupling: `8.779e-30`

| distribution | min | p05 | median | mean | p95 | max |
|---|---:|---:|---:|---:|---:|---:|
| random mixed coupling | 0.109101 | 0.14699 | 0.183137 | 0.181679 | 0.210926 | 0.230415 |
| random mixed full J | 1.09597 | 1.14167 | 1.19304 | 1.19163 | 1.24201 | 1.27814 |
| full-J frame price | 0.051618 | 0.0730369 | 0.107724 | 0.109702 | 0.152301 | 0.189312 |
| random mixed total cost | 0.895971 | 0.941667 | 0.993036 | 0.991627 | 1.04201 | 1.07814 |
| break-even mix weight | 0.051618 | 0.0730369 | 0.107724 | 0.109702 | 0.152301 | 0.189312 |
| packet-respecting coupling | 0.270477 | 0.270477 | 0.270477 | 0.270477 | 0.270477 | 0.270477 |
| packet-commutator impurity | 0.722272 | 0.768579 | 0.810749 | 0.809947 | 0.851071 | 0.883597 |
| random mixed packet purity | 0.516129 | 0.516129 | 0.516129 | 0.516746 | 0.52135 | 0.529723 |

| J term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.270477 | 0.183137 | 0.14699 | 0.210926 |
| mix_impurity | 0 | 0.810749 | 0.768579 | 0.851071 |
| fisher_projection_error | 0 | 0 | 0 | 3.33067e-16 |
| reciprocal_projection_error | 0 | 0 | 0 | 2.22045e-16 |
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
