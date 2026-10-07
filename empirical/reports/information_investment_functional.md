# B0 Information-Investment Functional Prototype

This report scores candidate finite discretizations on exact behavior
tables.  It is the first computable bridge from F0 to A0.

```text
fisher_projection_error + reciprocal_projection_error + closure_leakage + descent_balance_cost + resource_weight * resource_cost
```

Resource weight: `0.25`.
Reciprocal-density amplitude: `0.35`.

## C_7

Active reciprocal support: `1, 6`.
Winner: `allowed_reciprocal`.

| candidate | J | Fisher err | reciprocal err | closure | balance | resource | support |
|---|---:|---:|---:|---:|---:|---:|---:|
| allowed_reciprocal | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| conductor_packet | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| descent_closure | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| full | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 6 |
| low_index | 1.281948 | 0.031948 | 0.000000 | 0.500000 | 0.666667 | 0.333333 | 2 |
| top_fisher_energy | 1.281948 | 0.031948 | 0.000000 | 0.500000 | 0.666667 | 0.333333 | 2 |
| true_support | 1.281948 | 0.031948 | 0.000000 | 0.500000 | 0.666667 | 0.333333 | 2 |
| zero | 2.000000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0 |
| random_same_size | 2.750347 | 0.500347 | 0.500000 | 1.000000 | 0.666667 | 0.333333 | 2 |

## C_8

Active reciprocal support: `4`.
Winner: `allowed_reciprocal`.

| candidate | J | Fisher err | reciprocal err | closure | balance | resource | support |
|---|---:|---:|---:|---:|---:|---:|---:|
| allowed_reciprocal | 0.035714 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 1 |
| conductor_packet | 0.035714 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 1 |
| descent_closure | 0.035714 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 1 |
| top_fisher_energy | 0.035714 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 1 |
| true_support | 0.035714 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.142857 | 1 |
| full | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 7 |
| zero | 2.000000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0 |
| random_same_size | 2.702381 | 1.000000 | 1.000000 | 0.000000 | 0.666667 | 0.142857 | 1 |
| low_index | 2.892857 | 1.000000 | 1.000000 | 0.000000 | 0.857143 | 0.142857 | 1 |

## C_12

Active reciprocal support: `3, 9`.
Winner: `descent_closure`.

| candidate | J | Fisher err | reciprocal err | closure | balance | resource | support |
|---|---:|---:|---:|---:|---:|---:|---:|
| descent_closure | 0.068182 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.272727 | 3 |
| full | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 11 |
| conductor_packet | 0.936503 | 0.057715 | 0.000000 | 0.500000 | 0.333333 | 0.181818 | 2 |
| top_fisher_energy | 0.936503 | 0.057715 | 0.000000 | 0.500000 | 0.333333 | 0.181818 | 2 |
| true_support | 0.936503 | 0.057715 | 0.000000 | 0.500000 | 0.333333 | 0.181818 | 2 |
| allowed_reciprocal | 2.000000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0 |
| zero | 2.000000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0 |
| low_index | 2.863636 | 1.000000 | 1.000000 | 0.000000 | 0.818182 | 0.181818 | 2 |
| random_same_size | 2.892494 | 0.528857 | 0.500000 | 1.000000 | 0.818182 | 0.181818 | 2 |

## F_4[u]/(u^2)

Active reciprocal support: `(w+1)u, u, wu`.
Winner: `allowed_reciprocal`.

| candidate | J | Fisher err | reciprocal err | closure | balance | resource | support |
|---|---:|---:|---:|---:|---:|---:|---:|
| allowed_reciprocal | 0.050000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 3 |
| conductor_packet | 0.050000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 3 |
| descent_closure | 0.050000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 3 |
| top_fisher_energy | 0.050000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 3 |
| true_support | 0.050000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 3 |
| full | 0.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 15 |
| low_index | 1.383333 | 0.666667 | 0.666667 | 0.000000 | 0.000000 | 0.200000 | 3 |
| random_same_size | 1.954762 | 0.666667 | 0.666667 | 0.000000 | 0.571429 | 0.200000 | 3 |
| zero | 2.000000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0 |

## Reading

`true_support` tests raw approximation.  `descent_closure` tests the
nested zero-sum balance principle: if a support uses a conductor level,
it should pay for the lower balance-transfer levels needed for closure.
`allowed_reciprocal` is the exact Paper 10 full-block orthogonality
support.  `top_fisher_energy` is a PCA-style finite-table baseline.
`low_index` and `random_same_size` are adversarial baselines.
