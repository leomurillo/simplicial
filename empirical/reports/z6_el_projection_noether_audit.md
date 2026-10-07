# Z6 EL Projection Noether Audit

- Claim tested: EL-defined Z6 copula projection conserves autonomous Jacobi energy numerically
- Status: PASS
- initial energy: 1.641762068085e-02
- max relative energy drift: 3.613729e-10
- max ternary acceleration norm: 2.679040e-02
- kills: []

## Samples

| step | energy | relative drift | ternary acceleration norm |
|---:|---:|---:|---:|
| 0 | 1.641762068085e-02 | 0.000000e+00 | 2.607304e-02 |
| 12 | 1.641762050763e-02 | 1.732141e-10 | 2.642702e-02 |
| 24 | 1.641762039749e-02 | 2.833543e-10 | 2.679040e-02 |

## Interpretation

This audit tests the projection definition that makes the physical flow
Euler-Lagrange by construction. It does not validate the older algebraic
K_CH force shortcut; that shortcut remains a residual diagnostic.
