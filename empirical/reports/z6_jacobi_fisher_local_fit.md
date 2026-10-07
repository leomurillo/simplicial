# Z6 Jacobi-Fisher Local Power-Series Fit

- Claim tested: quadratic local sector-pure power series can solve Jacobi-Fisher conformal matching numerically
- Status: KILL
- naive max relative residual: 3.468315e-01
- fit max relative residual: 1.358818e-01
- fit mean relative residual: 7.273066e-02
- improvement factor: 2.552451e+00
- kills: ['local polynomial fit did not meet target residual']

## History

| iteration | loss | max residual | mean residual | step size |
|---:|---:|---:|---:|---:|
| 0 | 7.168924e-02 | 3.407122e-01 | 2.618527e-01 | 1.050000e-02 |
| 10 | 4.067440e-02 | 2.718390e-01 | 1.949236e-01 | 1.710339e-02 |
| 20 | 1.913298e-02 | 1.995735e-01 | 1.322550e-01 | 2.785963e-02 |
| 30 | 1.003179e-02 | 1.439051e-01 | 9.381086e-02 | 4.538039e-02 |
| 40 | 7.916756e-03 | 1.394169e-01 | 8.103885e-02 | 7.391988e-02 |
| 50 | 7.575853e-03 | 1.450079e-01 | 7.872152e-02 | 1.204077e-01 |
| 60 | 7.340824e-03 | 1.439269e-01 | 7.741909e-02 | 1.961315e-01 |
| 70 | 6.980272e-03 | 1.405867e-01 | 7.545385e-02 | 3.194775e-01 |
| 79 | 6.494695e-03 | 1.358818e-01 | 7.273066e-02 | 4.956144e-01 |

## Interpretation

PASS means the local power-series ansatz solved the sampled conformal
matching problem to the target tolerance. KILL means this ansatz is
still too rigid or the finite-row isometry equation is obstructed.
