# Coefficient Rank-Profile Probe

- CRT row: `C4 x C3`
- max order: `4`

The rank is the two-factor tensor rank of `Q_S C_n(h) Q_T`, computed as an exact rational matrix rank after vectorizing each local source/target block.

## pure_tensor

- first-order support by CRT pattern: `{'{1,2}': 6, '{1}': 3}`
- rank-counts by order: `{'1': {'1': 8, '0': 1}, '2': {'1': 9}, '3': {'1': 9}, '4': {'1': 9}}`

| order | source | target | rank | nonzero entries | local shape |
|---:|---|---|---:|---:|---|
| 1 | {1} | {1} | 1 | 6 | 9x1 |
| 1 | {1} | {2} | 1 | 6 | 3x2 |
| 1 | {1} | {1,2} | 1 | 12 | 9x2 |
| 1 | {2} | {1} | 1 | 6 | 3x2 |
| 1 | {2} | {1,2} | 1 | 12 | 3x4 |
| 1 | {1,2} | {1} | 1 | 12 | 9x2 |
| 1 | {1,2} | {2} | 1 | 12 | 3x4 |
| 1 | {1,2} | {1,2} | 1 | 24 | 9x4 |
| 2 | {1} | {1} | 1 | 9 | 9x1 |
| 2 | {1} | {2} | 1 | 6 | 3x2 |
| 2 | {1} | {1,2} | 1 | 18 | 9x2 |
| 2 | {2} | {1} | 1 | 6 | 3x2 |
| 2 | {2} | {2} | 1 | 4 | 1x4 |
| 2 | {2} | {1,2} | 1 | 12 | 3x4 |
| 2 | {1,2} | {1} | 1 | 18 | 9x2 |
| 2 | {1,2} | {2} | 1 | 12 | 3x4 |
| 2 | {1,2} | {1,2} | 1 | 36 | 9x4 |
| 3 | {1} | {1} | 1 | 9 | 9x1 |
| 3 | {1} | {2} | 1 | 6 | 3x2 |
| 3 | {1} | {1,2} | 1 | 18 | 9x2 |
| 3 | {2} | {1} | 1 | 6 | 3x2 |
| 3 | {2} | {2} | 1 | 4 | 1x4 |
| 3 | {2} | {1,2} | 1 | 12 | 3x4 |
| 3 | {1,2} | {1} | 1 | 18 | 9x2 |
| 3 | {1,2} | {2} | 1 | 12 | 3x4 |
| 3 | {1,2} | {1,2} | 1 | 36 | 9x4 |
| 4 | {1} | {1} | 1 | 9 | 9x1 |
| 4 | {1} | {2} | 1 | 6 | 3x2 |
| 4 | {1} | {1,2} | 1 | 18 | 9x2 |
| 4 | {2} | {1} | 1 | 6 | 3x2 |
| 4 | {2} | {2} | 1 | 4 | 1x4 |
| 4 | {2} | {1,2} | 1 | 12 | 3x4 |
| 4 | {1,2} | {1} | 1 | 18 | 9x2 |
| 4 | {1,2} | {2} | 1 | 12 | 3x4 |
| 4 | {1,2} | {1,2} | 1 | 36 | 9x4 |

## local_additive_sum

- first-order support by CRT pattern: `{'{1}': 2, '{2}': 2}`
- rank-counts by order: `{'1': {'1': 6, '0': 2, '2': 1}, '2': {'1': 4, '2': 4, '3': 1}, '3': {'1': 2, '2': 7}, '4': {'1': 2, '2': 6, '3': 1}}`

| order | source | target | rank | nonzero entries | local shape |
|---:|---|---|---:|---:|---|
| 1 | {1,2} | {1,2} | 2 | 14 | 9x4 |
| 2 | {1,2} | {1,2} | 3 | 24 | 9x4 |
| 3 | {1} | {2} | 2 | 6 | 3x2 |
| 3 | {1} | {1,2} | 2 | 18 | 9x2 |
| 3 | {2} | {1} | 2 | 6 | 3x2 |
| 3 | {2} | {1,2} | 2 | 10 | 3x4 |
| 3 | {1,2} | {1} | 2 | 18 | 9x2 |
| 3 | {1,2} | {2} | 2 | 10 | 3x4 |
| 3 | {1,2} | {1,2} | 2 | 26 | 9x4 |
| 4 | {1,2} | {1,2} | 3 | 28 | 9x4 |

## two_summand_mixed

- first-order support by CRT pattern: `{'{1,2}': 6}`
- rank-counts by order: `{'1': {'0': 2, '2': 7}, '2': {'1': 2, '2': 4, '3': 3}, '3': {'1': 2, '2': 4, '3': 3}, '4': {'1': 2, '2': 4, '3': 3}}`

| order | source | target | rank | nonzero entries | local shape |
|---:|---|---|---:|---:|---|
| 1 | {1} | {2} | 2 | 6 | 3x2 |
| 1 | {1} | {1,2} | 2 | 12 | 9x2 |
| 1 | {2} | {1} | 2 | 6 | 3x2 |
| 1 | {2} | {1,2} | 2 | 6 | 3x4 |
| 1 | {1,2} | {1} | 2 | 12 | 9x2 |
| 1 | {1,2} | {2} | 2 | 6 | 3x4 |
| 1 | {1,2} | {1,2} | 2 | 12 | 9x4 |
| 2 | {2} | {1,2} | 3 | 12 | 3x4 |
| 2 | {1,2} | {2} | 3 | 12 | 3x4 |
| 2 | {1,2} | {1,2} | 3 | 33 | 9x4 |
| 3 | {2} | {1,2} | 3 | 12 | 3x4 |
| 3 | {1,2} | {2} | 3 | 12 | 3x4 |
| 3 | {1,2} | {1,2} | 3 | 36 | 9x4 |
| 4 | {2} | {1,2} | 3 | 12 | 3x4 |
| 4 | {1,2} | {2} | 3 | 12 | 3x4 |
| 4 | {1,2} | {1,2} | 3 | 36 | 9x4 |

## Interpretation

- `pure_tensor` is the sanity check: every occupied block has tensor rank 1 through the tested orders.
- `local_additive_sum` has first-order support spread across the two CRT factors; higher orders show where additive cross-factor superposition creates rank greater than 1 inside a support block.
- `two_summand_mixed` is the impurity stress test: rank greater than 1 appears immediately in mixed support blocks and persists under convolution powers.

This is the paper-facing reason to keep `rho_n(h;S,T)`: scalar conductor support says which CRT corners are occupied, while the rank profile says whether the coefficient inside that corner factors over local components.
