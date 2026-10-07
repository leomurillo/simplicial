# Z6 E5 Physical Discriminator

- Claim tested: E5 parameter-fixed physical discriminator for the Z6 canonical bridge
- Status: KILL

## Pre-Registration

- Model: a_candidate = a_Newton + lambda_E5 * (a_EL(eta_copula)-a_EL(eta_base))
- Cartesian lift: mass-metric minimum-norm inverse of D sigma
- participation lift: none
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

- lambda_E5: 7.484436188256e-11
- lambda source: ephemeris
- weak-field max relative correction: 7.538851e-13
- dyadic-boundary max relative correction: 3.208667e-13
- controlled relative signed projections: ['5.884618e-14', '5.765008e-14', '2.274289e-14', '5.186125e-14']
- controlled signs: [1, 1, 1, 1]
- controlled sign-definite: True
- controlled min abs signal: 2.274289e-14
- controlled max abs signal: 5.884618e-14
- ephemeris final position max: 1.364257e-09
- ephemeris final velocity max: 3.726244e-09
- ephemeris weak-field max sampled correction: 1.014886e-10
- near-equilateral Cartesian signed projections: ['5.874676e-14', '5.741542e-14', '2.270461e-14', '5.178312e-14']
- near-equilateral Cartesian signs: [1, 1, 1, 1]
- near-equilateral Cartesian sign-definite: True
- near-equilateral Cartesian min abs signal: 2.270461e-14
- near-equilateral Cartesian max abs signal: 5.874676e-14
- kills: ['controlled-regime signal is below floor', 'ephemeris weak-field acceleration correction exceeds 1e-10 cap', 'finite-row rigidity prevents ephemeris recovery: final position residual exceeds tolerance', 'finite-row rigidity prevents ephemeris recovery: final velocity residual exceeds tolerance', 'near-equilateral Cartesian E5 signal is below floor']

## Samples

### Weak Field

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 4.25, 5.200000000000002] | 2.104132e-14 | 4.273998e-16 |
| 1 | [1.0000000000000004, 8.65, 9.550000000000006] | 3.337457e-13 | -2.856021e-15 |
| 2 | [1.0, 14.199999999999992, 15.10000000000001] | 7.538851e-13 | -2.899199e-14 |

### Dyadic Boundary

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 99.99999999999996, 100.00000000000004] | 7.955445e-14 | 2.261823e-17 |
| 1 | [1.0000000000000013, 200.0000000000001, 200.0000000000001] | 3.208667e-13 | 4.661595e-16 |

### Controlled Near-Equilateral

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 1.0000000000000002, 1.0000000000000002] | 1.477254e-13 | 5.884618e-14 |
| 1 | [0.9999999999999999, 1.04, 0.9699999999999999] | 1.606726e-13 | 5.765008e-14 |
| 2 | [1.0, 0.9600000000000001, 1.03] | 3.923619e-14 | 2.274289e-14 |
| 3 | [1.02, 0.99, 1.0] | 1.234621e-13 | 5.186125e-14 |

### Ephemeris Propagation

| case | family | orbits | steps | final pos rel | final vel rel | max weak correction |
|---|---|---:|---:|---:|---:|---:|
| earth_moon_sun_quadrature | known_perturbed_three_body | 2 | 20 | 2.633572e-12 | 4.257130e-11 | 6.681992e-13 |
| jupiter_io_europa | known_perturbed_three_body | 2 | 20 | 1.364257e-09 | 3.726244e-09 | 1.014886e-10 |
| synthetic_lagrange_equilateral | synthetic_near_equilateral | 2 | 20 | 1.213161e-11 | 1.583888e-11 | 5.040345e-17 |

### Near-Equilateral Cartesian Sign Scan

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 1.0, 1.0] | 1.229854e-13 | 5.874676e-14 |
| 1 | [1.0, 1.04, 0.97] | 1.312722e-13 | 5.741542e-14 |
| 2 | [1.0, 0.96, 1.03] | 3.911616e-14 | 2.270461e-14 |
| 3 | [1.02, 0.99, 1.0] | 1.041322e-13 | 5.178312e-14 |

## Interpretation

A PASS means this finite bridge survives the fixed-parameter
reduced-shape and Cartesian ephemeris discriminator. A KILL means
the bridge remains a mathematical projection-closure prototype,
not a parameter-fixed physical candidate.
