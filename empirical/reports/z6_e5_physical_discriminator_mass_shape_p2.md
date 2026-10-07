# Z6 E5 Physical Discriminator

- Claim tested: E5 parameter-fixed physical discriminator for the Z6 canonical bridge
- Status: KILL

## Pre-Registration

- Model: a_candidate = a_Newton + lambda_E5 * (a_EL(eta_copula)-a_EL(eta_base))
- Cartesian lift: mass-metric minimum-norm inverse of D sigma
- participation lift: mass_shape
- shape participation power: 2.0
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

- lambda_E5: 1.020325686988e-02
- lambda source: ephemeris
- weak-field max relative correction: 5.425594e-16
- dyadic-boundary max relative correction: 4.747900e-12
- controlled relative signed projections: ['8.022284e-06', '7.781877e-06', '3.069938e-06', '7.056867e-06']
- controlled signs: [1, 1, 1, 1]
- controlled sign-definite: True
- controlled min abs signal: 3.069938e-06
- controlled max abs signal: 8.022284e-06
- ephemeris final position max: 1.657194e-03
- ephemeris final velocity max: 2.162294e-03
- ephemeris weak-field max sampled correction: 2.756874e-10
- near-equilateral Cartesian signed projections: ['8.008730e-06', '7.750203e-06', '3.064771e-06', '7.046235e-06']
- near-equilateral Cartesian signs: [1, 1, 1, 1]
- near-equilateral Cartesian sign-definite: True
- near-equilateral Cartesian min abs signal: 3.064771e-06
- near-equilateral Cartesian max abs signal: 8.008730e-06
- kills: ['ephemeris weak-field acceleration correction exceeds 1e-10 cap', 'finite-row rigidity prevents ephemeris recovery: final position residual exceeds tolerance', 'finite-row rigidity prevents ephemeris recovery: final velocity residual exceeds tolerance']

## Samples

### Weak Field

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 4.25, 5.200000000000002] | 8.363205e-17 | 1.698768e-18 |
| 1 | [1.0000000000000004, 8.65, 9.550000000000006] | 5.425594e-16 | -4.642938e-18 |
| 2 | [1.0, 14.199999999999992, 15.10000000000001] | 2.147852e-16 | -8.259944e-18 |

### Dyadic Boundary

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 99.99999999999996, 100.00000000000004] | 4.747900e-12 | 1.349882e-15 |
| 1 | [1.0000000000000013, 200.0000000000001, 200.0000000000001] | 1.220988e-12 | 1.773868e-15 |

### Controlled Near-Equilateral

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 1.0000000000000002, 1.0000000000000002] | 2.013886e-05 | 8.022284e-06 |
| 1 | [0.9999999999999999, 1.04, 0.9699999999999999] | 2.168834e-05 | 7.781877e-06 |
| 2 | [1.0, 0.9600000000000001, 1.03] | 5.296278e-06 | 3.069938e-06 |
| 3 | [1.02, 0.99, 1.0] | 1.679974e-05 | 7.056867e-06 |

### Ephemeris Propagation

| case | family | orbits | steps | final pos rel | final vel rel | max weak correction |
|---|---|---:|---:|---:|---:|---:|
| earth_moon_sun_quadrature | known_perturbed_three_body | 2 | 20 | 0.000000e+00 | 0.000000e+00 | 5.365089e-25 |
| jupiter_io_europa | known_perturbed_three_body | 2 | 20 | 1.689103e-09 | 1.032447e-09 | 2.756874e-10 |
| synthetic_lagrange_equilateral | synthetic_near_equilateral | 2 | 20 | 1.657194e-03 | 2.162294e-03 | 1.622477e-06 |

### Near-Equilateral Cartesian Sign Scan

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 1.0, 1.0] | 1.676615e-05 | 8.008730e-06 |
| 1 | [1.0, 1.04, 0.97] | 1.771973e-05 | 7.750203e-06 |
| 2 | [1.0, 0.96, 1.03] | 5.280075e-06 | 3.064771e-06 |
| 3 | [1.02, 0.99, 1.0] | 1.416949e-05 | 7.046235e-06 |

## Interpretation

A PASS means this finite bridge survives the fixed-parameter
reduced-shape and Cartesian ephemeris discriminator. A KILL means
the bridge remains a mathematical projection-closure prototype,
not a parameter-fixed physical candidate.
