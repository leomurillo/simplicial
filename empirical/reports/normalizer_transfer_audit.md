# B3 Normalizer Transfer Audit

This report asks when the B3 symmetry premium earns itself back.  A
source support is fixed, held-out tasks are normalizer transforms of it,
and policies are scored without seeing the target transform.

## Config

- `rows`: `['c7', 'c8', 'c12', 'f4-u2', 'f2-u4']`
- `source_tasks`: `64`
- `transfers_per_source`: `8`
- `max_source_size`: `2`
- `amplitude_min`: `0.15`
- `amplitude_max`: `0.45`
- `resource_weight`: `0.25`
- `seed`: `20260514`

## C_7

Winner by mean J: `full`.
Normalizer beats source-minimal rate: `0.000`.
Mean structural gain / premium / net gain: `0.000000` / `0.000000` / `0.000000`.

| policy | mean J | wins | support | structural | resource | Fisher | reciprocal | closure | balance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| full | 0.250000 | 512 | 6.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| oracle_minimal | 0.250000 | 0 | 6.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_conductor_packet | 0.250000 | 0 | 6.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_minimal | 0.250000 | 0 | 6.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_normalizer | 0.250000 | 0 | 6.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_raw | 2.220896 | 0 | 2.000 | 2.137563 | 0.333333 | 0.647654 | 0.646484 | 0.176758 | 0.666667 |

### Payoff Examples

- none

## C_8

Winner by mean J: `oracle_minimal`.
Normalizer beats source-minimal rate: `0.000`.
Mean structural gain / premium / net gain: `0.000000` / `0.000000` / `0.000000`.

| policy | mean J | wins | support | structural | resource | Fisher | reciprocal | closure | balance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| oracle_minimal | 0.172991 | 224 | 4.844 | 0.000000 | 0.691964 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_minimal | 0.172991 | 0 | 4.844 | 0.000000 | 0.691964 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_normalizer | 0.172991 | 0 | 4.844 | 0.000000 | 0.691964 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| full | 0.250000 | 288 | 7.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_conductor_packet | 0.848636 | 0 | 2.922 | 0.744283 | 0.417411 | 0.026649 | 0.000000 | 0.398438 | 0.319196 |
| source_raw | 1.332048 | 0 | 1.797 | 1.267874 | 0.256696 | 0.266479 | 0.246094 | 0.275391 | 0.479911 |

### Payoff Examples

- none

## C_12

Winner by mean J: `oracle_minimal`.
Normalizer beats source-minimal rate: `0.000`.
Mean structural gain / premium / net gain: `0.000000` / `0.000000` / `0.000000`.

| policy | mean J | wins | support | structural | resource | Fisher | reciprocal | closure | balance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| oracle_minimal | 0.121094 | 368 | 5.328 | 0.000000 | 0.484375 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_minimal | 0.121094 | 0 | 5.328 | 0.000000 | 0.484375 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_normalizer | 0.121094 | 0 | 5.328 | 0.000000 | 0.484375 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| full | 0.250000 | 144 | 11.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_conductor_packet | 0.835390 | 0 | 2.469 | 0.779282 | 0.224432 | 0.023742 | 0.000000 | 0.367188 | 0.388352 |
| source_raw | 1.075106 | 0 | 1.906 | 1.031782 | 0.173295 | 0.156746 | 0.136719 | 0.298828 | 0.439489 |

### Payoff Examples

- none

## F_4[u]/(u^2)

Winner by mean J: `oracle_minimal`.
Normalizer beats source-minimal rate: `0.812`.
Mean structural gain / premium / net gain: `1.498377` / `0.167708` / `1.330668`.

| policy | mean J | wins | support | structural | resource | Fisher | reciprocal | closure | balance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| oracle_minimal | 0.032292 | 512 | 1.938 | 0.000000 | 0.129167 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_normalizer | 0.200000 | 0 | 12.000 | 0.000000 | 0.800000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| full | 0.250000 | 0 | 15.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_conductor_packet | 0.359798 | 0 | 10.172 | 0.190267 | 0.678125 | 0.005892 | 0.000000 | 0.062500 | 0.121875 |
| source_minimal | 1.530668 | 0 | 1.938 | 1.498377 | 0.129167 | 0.749353 | 0.749023 | 0.000000 | 0.000000 |
| source_raw | 1.756131 | 0 | 1.469 | 1.731651 | 0.097917 | 0.779503 | 0.777344 | 0.018555 | 0.156250 |

### Payoff Examples

- source `(w+1)u` -> target `wu`; minimal `(w+1)u`; normalizer `(w+1)u, u, wu`; J `2.016667` -> `0.050000`; gain/premium `2.000000`/`0.033333`
- source `(w+1)u` -> target `u`; minimal `(w+1)u`; normalizer `(w+1)u, u, wu`; J `2.016667` -> `0.050000`; gain/premium `2.000000`/`0.033333`
- source `(w+1)u` -> target `(w+1)u`; minimal `(w+1)u`; normalizer `(w+1)u, u, wu`; J `0.016667` -> `0.050000`; gain/premium `0.000000`/`0.033333`
- source `(w+1)u` -> target `u`; minimal `(w+1)u`; normalizer `(w+1)u, u, wu`; J `2.016667` -> `0.050000`; gain/premium `2.000000`/`0.033333`
- source `(w+1)u` -> target `(w+1)u`; minimal `(w+1)u`; normalizer `(w+1)u, u, wu`; J `0.016667` -> `0.050000`; gain/premium `0.000000`/`0.033333`
- source `(w+1)u` -> target `(w+1)u`; minimal `(w+1)u`; normalizer `(w+1)u, u, wu`; J `0.016667` -> `0.050000`; gain/premium `0.000000`/`0.033333`

## F_2[u]/(u^4)

Winner by mean J: `oracle_minimal`.
Normalizer beats source-minimal rate: `0.799`.
Mean structural gain / premium / net gain: `1.398391` / `0.168229` / `1.230162`.

| policy | mean J | wins | support | structural | resource | Fisher | reciprocal | closure | balance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| oracle_minimal | 0.034896 | 512 | 2.094 | 0.000000 | 0.139583 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_normalizer | 0.203125 | 0 | 12.188 | 0.000000 | 0.812500 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| full | 0.250000 | 0 | 15.000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| source_conductor_packet | 0.560166 | 0 | 7.703 | 0.431781 | 0.513542 | 0.006557 | 0.000000 | 0.070312 | 0.354911 |
| source_minimal | 1.433287 | 0 | 2.094 | 1.398391 | 0.139583 | 0.699172 | 0.699219 | 0.000000 | 0.000000 |
| source_raw | 1.694609 | 0 | 1.547 | 1.668828 | 0.103125 | 0.730677 | 0.725586 | 0.030273 | 0.182292 |

### Payoff Examples

- source `1+u^3, u^2+u^3` -> target `1+u^3, u^2+u^3`; minimal `1+u^2, 1+u^3, u^2+u^3`; normalizer `1, 1+u, 1+u+u^2, 1+u+u^2+u^3, 1+u+u^3, 1+u^2, 1+u^2+u^3, 1+u^3, u, u+u^2, u+u^2+u^3, u+u^3, u^2, u^2+u^3, u^3`; J `0.050000` -> `0.250000`; gain/premium `0.000000`/`0.200000`
- source `1+u^3, u^2+u^3` -> target `1+u^2, u^2+u^3`; minimal `1+u^2, 1+u^3, u^2+u^3`; normalizer `1, 1+u, 1+u+u^2, 1+u+u^2+u^3, 1+u+u^3, 1+u^2, 1+u^2+u^3, 1+u^3, u, u+u^2, u+u^2+u^3, u+u^3, u^2, u^2+u^3, u^3`; J `0.050000` -> `0.250000`; gain/premium `0.000000`/`0.200000`
- source `1+u^3, u^2+u^3` -> target `1+u+u^2, u^2`; minimal `1+u^2, 1+u^3, u^2+u^3`; normalizer `1, 1+u, 1+u+u^2, 1+u+u^2+u^3, 1+u+u^3, 1+u^2, 1+u^2+u^3, 1+u^3, u, u+u^2, u+u^2+u^3, u+u^3, u^2, u^2+u^3, u^3`; J `2.050000` -> `0.250000`; gain/premium `2.000000`/`0.200000`
- source `1+u^3, u^2+u^3` -> target `1+u^3, u^2+u^3`; minimal `1+u^2, 1+u^3, u^2+u^3`; normalizer `1, 1+u, 1+u+u^2, 1+u+u^2+u^3, 1+u+u^3, 1+u^2, 1+u^2+u^3, 1+u^3, u, u+u^2, u+u^2+u^3, u+u^3, u^2, u^2+u^3, u^3`; J `0.050000` -> `0.250000`; gain/premium `0.000000`/`0.200000`
- source `1+u^3, u^2+u^3` -> target `1+u+u^3, u^2`; minimal `1+u^2, 1+u^3, u^2+u^3`; normalizer `1, 1+u, 1+u+u^2, 1+u+u^2+u^3, 1+u+u^3, 1+u^2, 1+u^2+u^3, 1+u^3, u, u+u^2, u+u^2+u^3, u+u^3, u^2, u^2+u^3, u^3`; J `2.050000` -> `0.250000`; gain/premium `2.000000`/`0.200000`
- source `1+u^3, u^2+u^3` -> target `1+u+u^2, u^2`; minimal `1+u^2, 1+u^3, u^2+u^3`; normalizer `1, 1+u, 1+u+u^2, 1+u+u^2+u^3, 1+u+u^3, 1+u^2, 1+u^2+u^3, 1+u^3, u, u+u^2, u+u^2+u^3, u+u^3, u^2, u^2+u^3, u^3`; J `2.050000` -> `0.250000`; gain/premium `2.000000`/`0.200000`

## Reading

When the deployment task is fixed, B2 minimal descent is cheaper.  When
the deployment task is only known up to normalizer symmetry, B3 can
outperform B2 because it buys all equivalent supports at once.  The
break-even condition is structural transfer gain greater than the
resource-weighted symmetry premium.
