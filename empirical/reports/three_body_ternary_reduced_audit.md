# Three-Body Ternary Reduced Static Audit

This report is a static structural precondition check. It does not integrate
the Theorem 7.2 dynamics and therefore does not evaluate E6.

## Pre-registered conditions

- E6: NOT EVALUATED HERE: future integrator drift of E3_red or L beyond floor
- E7: evaluated statically: dimensionless connected tensor ratio at numerical floor
- E8: implementation self-test: rank(Deta)>3 or unreduced Hessian rank>3 for invariant eta

## Summary

- E6 status: NOT_EVALUATED
- Static E7/E8 status: PASS
- evaluated samples: 8
- skipped samples: 0
- max rank(Deta): 3
- max epsilon-normalized unreduced Hessian rank: 3
- min raw connected tensor norm: 1.338140e-08
- min dimensionless connected tensor ratio: 1.000000e+00
- kills: []

## Samples

| seed | used | quality | rank(Deta) | Hessian rank | connected ratio | raw connected norm |
|---:|:---:|---:|---:|---:|---:|---:|
| 2800 | yes | 1.000303e-01 | 3 | 3 | 1.000000e+00 | 2.798776e-08 |
| 2801 | yes | 1.787169e-01 | 3 | 3 | 1.000000e+00 | 1.821531e-08 |
| 2802 | yes | 1.252328e-01 | 3 | 3 | 1.000000e+00 | 6.981691e-08 |
| 2803 | yes | 1.457667e-01 | 3 | 3 | 1.000000e+00 | 1.338140e-08 |
| 2804 | yes | 1.533973e-01 | 3 | 3 | 1.000000e+00 | 2.167845e-08 |
| 2805 | yes | 1.313293e-01 | 3 | 3 | 1.000000e+00 | 3.442544e-08 |
| 2806 | yes | 1.880347e-01 | 3 | 3 | 1.000000e+00 | 3.031490e-08 |
| 2807 | yes | 1.642099e-01 | 3 | 3 | 1.000000e+00 | 1.829007e-08 |
