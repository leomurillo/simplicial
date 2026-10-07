# Z6 E5 Physical Discriminator

- Claim tested: E5 parameter-fixed physical discriminator for the Z6 canonical bridge
- Status: KILL

## Pre-Registration

- Model: a_candidate = a_Newton + lambda_E5 * (a_EL(eta_copula)-a_EL(eta_base))
- Cartesian lift: mass-metric minimum-norm inverse of D sigma
- participation lift: mass_shape
- shape participation power: 1.0
- kappa: 0.8
- phi coefficients: [1.0, 0.0]
- lambda fixing: lambda_E5 fixed once by weak-field tolerance, then held fixed
- lambda source: ephemeris
- weak-field tolerance: 1.000000e-10
- dyadic-boundary tolerance: 1.000000e-08
- controlled signal floor: 1.000000e-12
- ephemeris metric: final RMS position/velocity deviation relative to initial RMS scale after N orbits
- ephemeris position tolerance: 1.000000e-10
- ephemeris velocity tolerance: 1.000000e-10
- ephemeris N orbits: 2
- ephemeris steps per orbit: 10

## Summary

- lambda_E5: 4.877574801746e-03
- lambda source: ephemeris
- weak-field max relative correction: 2.080512e-14
- dyadic-boundary max relative correction: 3.493599e-09
- controlled relative signed projections: ['3.834980e-06', '3.738498e-06', '1.474832e-06', '3.376622e-06']
- controlled signs: [1, 1, 1, 1]
- controlled sign-definite: True
- controlled min abs signal: 1.474832e-06
- controlled max abs signal: 3.834980e-06
- ephemeris final position max: 7.927810e-04
- ephemeris final velocity max: 1.034691e-03
- ephemeris weak-field max sampled correction: 2.534788e-10
- near-equilateral Cartesian signed projections: ['3.828501e-06', '3.723281e-06', '1.472350e-06', '3.371535e-06']
- near-equilateral Cartesian signs: [1, 1, 1, 1]
- near-equilateral Cartesian sign-definite: True
- near-equilateral Cartesian min abs signal: 1.472350e-06
- near-equilateral Cartesian max abs signal: 3.828501e-06
- kills: ['ephemeris weak-field acceleration correction exceeds 1e-10 cap', 'finite-row rigidity prevents ephemeris recovery: final position residual exceeds tolerance', 'finite-row rigidity prevents ephemeris recovery: final velocity residual exceeds tolerance']

## Samples

### Weak Field

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 4.25, 5.200000000000002] | 2.050981e-15 | 4.166036e-17 |
| 1 | [1.0000000000000004, 8.65, 9.550000000000006] | 2.080512e-14 | -1.780393e-16 |
| 2 | [1.0, 14.199999999999992, 15.10000000000001] | 1.967404e-14 | -7.565999e-16 |

### Dyadic Boundary

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 99.99999999999996, 100.00000000000004] | 3.430347e-09 | 9.752863e-13 |
| 1 | [1.0000000000000013, 200.0000000000001, 200.0000000000001] | 3.493599e-09 | 5.075548e-12 |

### Controlled Near-Equilateral

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 1.0000000000000002, 1.0000000000000002] | 9.627202e-06 | 3.834980e-06 |
| 1 | [0.9999999999999999, 1.04, 0.9699999999999999] | 1.041931e-05 | 3.738498e-06 |
| 2 | [1.0, 0.9600000000000001, 1.03] | 2.544391e-06 | 1.474832e-06 |
| 3 | [1.02, 0.99, 1.0] | 8.038462e-06 | 3.376622e-06 |

### Ephemeris Propagation

| case | family | orbits | steps | final pos rel | final vel rel | max weak correction |
|---|---|---:|---:|---:|---:|---:|
| earth_moon_sun_quadrature | known_perturbed_three_body | 2 | 20 | 0.000000e+00 | 0.000000e+00 | 5.784365e-21 |
| jupiter_io_europa | known_perturbed_three_body | 2 | 20 | 6.175108e-10 | 8.409495e-10 | 2.534788e-10 |
| synthetic_lagrange_equilateral | synthetic_near_equilateral | 2 | 20 | 7.927810e-04 | 1.034691e-03 | 1.801892e-07 |

### Near-Equilateral Cartesian Sign Scan

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 1.0, 1.0] | 8.014909e-06 | 3.828501e-06 |
| 1 | [1.0, 1.04, 0.97] | 8.512750e-06 | 3.723281e-06 |
| 2 | [1.0, 0.96, 1.03] | 2.536607e-06 | 1.472350e-06 |
| 3 | [1.02, 0.99, 1.0] | 6.779920e-06 | 3.371535e-06 |

## Interpretation

A PASS means this finite bridge survives the fixed-parameter
reduced-shape and Cartesian ephemeris discriminator. A KILL means
the bridge remains a mathematical projection-closure prototype,
not a parameter-fixed physical candidate.
