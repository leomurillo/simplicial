# Z6 Jacobi-Fisher Execution Audit

- Claim tested: Z6 linear sector-pure Jacobi-Fisher base map plus K_CH mixed spillover
- Status: KILL
- evaluated samples: 8
- max conformal relative residual: 6.388655e-01
- min mixed spillover ratio: 4.428970e-01
- kills: ['linear Z6 base map is not conformal to G_shape within tolerance']

## Basis Gram

- e_rho: 1.000000000000
- e_u: 1.000000000000
- e_w: 1.000000000000

## Samples

| idx | used | quality | conformal residual | mixed spillover ratio | omega^2 |
|---:|:---:|---:|---:|---:|---:|
| 0 | yes | 1.612409e-01 | 5.531123e-01 | 9.344007e-01 | 2.091932e-06 |
| 1 | yes | 1.782918e-01 | 4.205534e-01 | 9.788318e-01 | 6.002261e-06 |
| 2 | yes | 1.906779e-01 | 3.628761e-01 | 7.877505e-01 | 5.996234e-06 |
| 3 | yes | 1.876104e-01 | 2.119608e-01 | 4.428970e-01 | 1.254853e-05 |
| 4 | yes | 1.741636e-01 | 3.434923e-01 | 9.976708e-01 | 8.227625e-06 |
| 5 | yes | 1.448083e-01 | 6.388655e-01 | 8.651478e-01 | 4.428541e-06 |
| 6 | yes | 1.844333e-01 | 2.788407e-01 | 7.320781e-01 | 4.776047e-06 |
| 7 | yes | 1.913977e-01 | 2.566087e-01 | 5.023113e-01 | 5.863374e-06 |

## Interpretation

A KILL from the conformal residual means the naive linear sector-pure
base map does not solve the Jacobi-Fisher isometry equation. A nonzero
mixed spillover still matters: it shows the Z6 CRT tensor can generate
a ternary mixed component once a valid base map is found.
