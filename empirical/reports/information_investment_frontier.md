# B0 Information-Investment Frontier Audit

This report tests B0 beyond one hand-picked task.  For each finite row,
it samples train tasks, learns aggregate top-energy supports, then
scores policies on held-out tasks under the same information-investment
functional.

## Config

- `rows`: `['c7', 'c8', 'c12', 'f4-u2']`
- `train_tasks`: `48`
- `test_tasks`: `48`
- `amplitude_min`: `0.15`
- `amplitude_max`: `0.45`
- `resource_weight`: `0.25`
- `seed`: `20260514`

## C_7

Winner by mean J: `allowed_reciprocal`.
Learned energy ranking prefix: `5, 2, 1, 6, 3, 4`.

| policy | mean J | wins | support | Fisher | reciprocal | closure | balance | resource |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| allowed_reciprocal | 0.250000 | 48 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| conductor_packet | 0.250000 | 0 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| descent_closure | 0.250000 | 0 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| full | 0.250000 | 0 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| learned_top_descent_k | 0.250000 | 0 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| normalizer_saturation | 0.250000 | 0 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| random_descent_k | 0.250000 | 0 | 6.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| raw_support | 1.278751 | 0 | 2.000 | 0.028751 | 0.000000 | 0.500000 | 0.666667 | 0.333333 |
| learned_top_raw_k | 2.185969 | 0 | 2.000 | 0.623469 | 0.625000 | 0.187500 | 0.666667 | 0.333333 |
| random_raw_k | 2.450328 | 0 | 2.000 | 0.648245 | 0.645833 | 0.406250 | 0.666667 | 0.333333 |

### Example Held-Out Tasks

- active `1, 6` -> descent `1, 2, 3, 4, 5, 6`; winner `allowed_reciprocal`; learned-top-descent `1, 2, 3, 4, 5, 6`
- active `3, 4` -> descent `1, 2, 3, 4, 5, 6`; winner `allowed_reciprocal`; learned-top-descent `1, 2, 3, 4, 5, 6`
- active `2, 5` -> descent `1, 2, 3, 4, 5, 6`; winner `allowed_reciprocal`; learned-top-descent `1, 2, 3, 4, 5, 6`
- active `2, 5` -> descent `1, 2, 3, 4, 5, 6`; winner `allowed_reciprocal`; learned-top-descent `1, 2, 3, 4, 5, 6`
- active `1, 6` -> descent `1, 2, 3, 4, 5, 6`; winner `allowed_reciprocal`; learned-top-descent `1, 2, 3, 4, 5, 6`

## C_8

Winner by mean J: `descent_closure`.
Learned energy ranking prefix: `4, 2, 6, 3, 5, 7, 1`.

| policy | mean J | wins | support | Fisher | reciprocal | closure | balance | resource |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| descent_closure | 0.175595 | 38 | 4.917 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.702381 |
| learned_top_descent_k | 0.175595 | 0 | 4.917 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.702381 |
| normalizer_saturation | 0.175595 | 0 | 4.917 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.702381 |
| full | 0.250000 | 0 | 7.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| conductor_packet | 0.840500 | 0 | 2.958 | 0.019567 | 0.000000 | 0.395833 | 0.319444 | 0.422619 |
| random_descent_k | 0.961292 | 0 | 4.917 | 0.230142 | 0.229167 | 0.104167 | 0.222222 | 0.702381 |
| raw_support | 0.965771 | 0 | 1.792 | 0.019838 | 0.000000 | 0.395833 | 0.486111 | 0.255952 |
| allowed_reciprocal | 1.609451 | 10 | 1.000 | 0.782071 | 0.791667 | 0.000000 | 0.000000 | 0.142857 |
| learned_top_raw_k | 1.693085 | 0 | 1.792 | 0.677708 | 0.687500 | 0.000000 | 0.263889 | 0.255952 |
| random_raw_k | 2.510668 | 0 | 1.792 | 0.738843 | 0.739583 | 0.333333 | 0.634921 | 0.255952 |

### Example Held-Out Tasks

- active `1, 7` -> descent `1, 2, 3, 4, 5, 6, 7`; winner `descent_closure`; learned-top-descent `1, 2, 3, 4, 5, 6, 7`
- active `3, 5` -> descent `1, 2, 3, 4, 5, 6, 7`; winner `descent_closure`; learned-top-descent `1, 2, 3, 4, 5, 6, 7`
- active `1, 7` -> descent `1, 2, 3, 4, 5, 6, 7`; winner `descent_closure`; learned-top-descent `1, 2, 3, 4, 5, 6, 7`
- active `4` -> descent `4`; winner `allowed_reciprocal`; learned-top-descent `4`
- active `3, 5` -> descent `1, 2, 3, 4, 5, 6, 7`; winner `descent_closure`; learned-top-descent `1, 2, 3, 4, 5, 6, 7`

## C_12

Winner by mean J: `descent_closure`.
Learned energy ranking prefix: `2, 10, 6, 11, 1, 3, 9, 7`.

| policy | mean J | wins | support | Fisher | reciprocal | closure | balance | resource |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| descent_closure | 0.132102 | 37 | 5.812 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.528409 |
| normalizer_saturation | 0.132102 | 0 | 5.812 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.528409 |
| full | 0.250000 | 0 | 11.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| conductor_packet | 0.884614 | 11 | 2.583 | 0.021419 | 0.000000 | 0.385417 | 0.419066 | 0.234848 |
| raw_support | 0.930069 | 0 | 1.917 | 0.021420 | 0.000000 | 0.385417 | 0.479672 | 0.174242 |
| learned_top_descent_k | 1.483906 | 0 | 5.812 | 0.437221 | 0.437500 | 0.114583 | 0.362500 | 0.528409 |
| random_descent_k | 1.713673 | 0 | 5.812 | 0.468408 | 0.468750 | 0.213542 | 0.430871 | 0.528409 |
| allowed_reciprocal | 2.000000 | 0 | 0.000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 |
| learned_top_raw_k | 2.317386 | 0 | 1.917 | 0.771742 | 0.770833 | 0.114583 | 0.616667 | 0.174242 |
| random_raw_k | 2.680992 | 0 | 1.917 | 0.823416 | 0.822917 | 0.281250 | 0.709848 | 0.174242 |

### Example Held-Out Tasks

- active `10, 2` -> descent `10, 2, 4, 6, 8`; winner `descent_closure`; learned-top-descent `1, 10, 11, 2, 6`
- active `4, 8` -> descent `4, 8`; winner `conductor_packet`; learned-top-descent `10, 2`
- active `3, 9` -> descent `3, 6, 9`; winner `descent_closure`; learned-top-descent `10, 2, 6`
- active `1, 11` -> descent `1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9`; winner `descent_closure`; learned-top-descent `1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9`
- active `1, 11` -> descent `1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9`; winner `descent_closure`; learned-top-descent `1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9`

## F_4[u]/(u^2)

Winner by mean J: `descent_closure`.
Learned energy ranking prefix: `u, (w+1)u, wu, 1+u, 1+wu, w+1+u, w+1+(w+1)u, w+1`.

| policy | mean J | wins | support | Fisher | reciprocal | closure | balance | resource |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| descent_closure | 0.093056 | 25 | 5.583 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.372222 |
| normalizer_saturation | 0.154167 | 0 | 9.250 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.616667 |
| full | 0.250000 | 0 | 15.000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 |
| conductor_packet | 0.325780 | 0 | 7.688 | 0.007261 | 0.000000 | 0.086227 | 0.104167 | 0.512500 |
| raw_support | 0.432148 | 0 | 4.396 | 0.015581 | 0.000000 | 0.192708 | 0.150595 | 0.293056 |
| learned_top_descent_k | 0.766437 | 0 | 5.583 | 0.301159 | 0.305556 | 0.000000 | 0.066667 | 0.372222 |
| learned_top_raw_k | 0.936669 | 0 | 4.396 | 0.376252 | 0.380208 | 0.027778 | 0.079167 | 0.293056 |
| allowed_reciprocal | 1.084405 | 23 | 3.000 | 0.513572 | 0.520833 | 0.000000 | 0.000000 | 0.200000 |
| random_descent_k | 1.648635 | 0 | 5.583 | 0.573734 | 0.572917 | 0.020833 | 0.388095 | 0.372222 |
| random_raw_k | 1.937967 | 0 | 4.396 | 0.691928 | 0.692708 | 0.067567 | 0.412500 | 0.293056 |

### Example Held-Out Tasks

- active `(w+1)u, u, wu` -> descent `(w+1)u, u, wu`; winner `allowed_reciprocal`; learned-top-descent `(w+1)u, u, wu`
- active `1, 1+(w+1)u, 1+u, 1+wu, w, w+(w+1)u, w+1, w+1+(w+1)u, w+1+u, w+1+wu, w+u, w+wu` -> descent `(w+1)u, 1, 1+(w+1)u, 1+u, 1+wu, u, w, w+(w+1)u, w+1, w+1+(w+1)u, w+1+u, w+1+wu, w+u, w+wu, wu`; winner `descent_closure`; learned-top-descent `(w+1)u, 1, 1+(w+1)u, 1+u, 1+wu, u, w, w+(w+1)u, w+1, w+1+(w+1)u, w+1+u, w+1+wu, w+u, w+wu, wu`
- active `(w+1)u, u, wu` -> descent `(w+1)u, u, wu`; winner `allowed_reciprocal`; learned-top-descent `(w+1)u, u, wu`
- active `1+u, w, w+u` -> descent `1, 1+u, u, w, w+1, w+1+u, w+u`; winner `descent_closure`; learned-top-descent `(w+1)u, 1+u, 1+wu, u, w+1+(w+1)u, w+1+u, wu`
- active `(w+1)u, u, wu` -> descent `(w+1)u, u, wu`; winner `allowed_reciprocal`; learned-top-descent `(w+1)u, u, wu`

## Reading

`learned_top_descent_k` is the key baseline: it receives the same support
budget as `descent_closure`, but chooses modes from aggregate train-task
Fisher energy.  When descent closure wins, B0 is detecting a structural
balance-transfer mode that energy ranking alone can miss.
`normalizer_saturation` is the symmetry-complete policy: it may be worth
buying when equivariance matters, but B3 tracks that extra cost
separately from minimal subgroup descent.
