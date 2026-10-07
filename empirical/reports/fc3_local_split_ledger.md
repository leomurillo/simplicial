# FC3 Local Split-Cost Ledger

This report extends FC3 from the first `F4[u]/(u^2)` bounded Noether
ledger to the current exact FC2 row-classifier ledger.  It is a
projection-cost certificate, not a claim that every row has the full
FC1 Noether atlas.

## Aggregate

| field | value |
|---|---:|
| rows | 5 |
| full filtered residual | 180555 |
| support projection residual | 0 |
| support underpricing gap | 180555 |
| H4-visible atoms | 6648 |
| H3-contraction visible atoms | 173404 |
| remaining hidden atoms | 503 |

## Row Ledger

| row | full | support | H4 | H3 | remaining | underprice | K_CH status | PSL lambda | normalizer margin |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| f4-u2 (F_4[u]/(u^2)) | 1569 | 0 | 72 | 1470 | 27 | 1569 | exact | 55.406250 | 1.330668 |
| f2-u5 (F_2[u]/(u^5)) | 19140 | 0 | 5424 | 13618 | 98 | 19140 | exact | 2.000031 | n/a |
| f8-u2 (F_8[u]/(u^2)) | 158081 | 0 | 784 | 157178 | 119 | 158081 | exact | 924.037598 | n/a |
| f16-field (F_16) | 225 | 0 | 0 | 0 | 225 | 225 | empty | n/a | n/a |
| f2-u4-control (F_2[u]/(u^4)) | 1540 | 0 | 368 | 1138 | 34 | 1540 | exact | 2.000488 | 1.230162 |

## Visibility Fractions

| row | support | H4 | H3 | remaining | underprice |
|---|---:|---:|---:|---:|---:|
| f4-u2 | 0.000000 | 0.045889 | 0.936902 | 0.017208 | 1.000000 |
| f2-u5 | 0.000000 | 0.283386 | 0.711494 | 0.005120 | 1.000000 |
| f8-u2 | 0.000000 | 0.004959 | 0.994288 | 0.000753 | 1.000000 |
| f16-field | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 |
| f2-u4-control | 0.000000 | 0.238961 | 0.738961 | 0.022078 | 1.000000 |

## Checks

| check | observed | expected | pass |
|---|---|---|---|
| all_row_checks_pass | `{"f16-field": true, "f2-u4-control": true, "f2-u5": true, "f4-u2": true, "f8-u2": true}` | `"all true"` | True |
| all_support_projection_residuals_zero | `{"f16-field": 0, "f2-u4-control": 0, "f2-u5": 0, "f4-u2": 0, "f8-u2": 0}` | `0` | True |
| aggregate_visibility_partition | `180555` | `180555` | True |

## Reading

Across the current exact FC2 rows, support-only pricing reports `0`
residual while full filtered carry reports `180555`
atoms.  This proves the FC3 local pricing rule at projection-ledger
scope: full filtered carry must remain a separate cost channel, and
H4/H3/remaining fields are visibility partitions rather than closure
certificates.
