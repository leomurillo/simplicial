# Z6 Gaussian Base Metric Audit

- Claim tested: e-pure Gaussian/product base Fisher pullback equals lambda times G_shape
- Status: KILL
- max relative homothety residual: 7.227979e-01
- mean relative homothety residual: 4.843784e-01
- kills: ['Fisher pullback is not homothetic to G_shape within tolerance']

## Samples

| idx | best scale | relative residual |
|---:|---:|---:|
| 0 | 3.702435e+00 | 4.360601e-01 |
| 1 | 1.093897e+00 | 7.227979e-01 |
| 2 | 1.741017e+00 | 6.458447e-01 |
| 3 | 4.856890e+00 | 3.948449e-01 |
| 4 | 7.587764e+00 | 3.919880e-01 |
| 5 | 7.132243e+00 | 4.655727e-01 |
| 6 | 1.630001e+00 | 3.098958e-01 |
| 7 | 1.110707e+00 | 5.080229e-01 |

## Interpretation

A KILL means the discrete Z6 product/exponential base is not the
continuous Gaussian statistical family whose Fisher metric recovers a
Mahalanobis/Jacobi metric. The Cotton-York obstruction is therefore
not annihilated by this argument.
