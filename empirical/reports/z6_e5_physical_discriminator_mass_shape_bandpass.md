# Z6 E5 Physical Discriminator

- Claim tested: E5 parameter-fixed physical discriminator for the Z6 canonical bridge
- Status: KILL

## Pre-Registration

- Model: a_candidate = a_Newton + lambda_E5 * (a_EL(eta_copula)-a_EL(eta_base))
- Cartesian lift: mass-metric minimum-norm inverse of D sigma
- participation lift: mass_shape
- shape participation power: 1.0
- dynamic suppression: shape_bandpass
- dynamic shape-rate center: 4.716991e-02
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

- lambda_E5: 2.121482226628e+04
- lambda source: ephemeris
- weak-field max relative correction: 9.760308e-12
- dyadic-boundary max relative correction: 1.434093e-06
- controlled relative signed projections: ['1.668010e+01', '1.626045e+01', '6.414725e+00', '1.468649e+01']
- controlled signs: [1, 1, 1, 1]
- controlled sign-definite: True
- controlled min abs signal: 6.414725e+00
- controlled max abs signal: 1.668010e+01
- ephemeris final position max: 1.169556e+07
- ephemeris final velocity max: 2.000266e+06
- ephemeris weak-field max sampled correction: 1.000000e-10
- near-equilateral Cartesian signed projections: ['1.665192e+01', '1.619427e+01', '6.403929e+00', '1.466436e+01']
- near-equilateral Cartesian signs: [1, 1, 1, 1]
- near-equilateral Cartesian sign-definite: True
- near-equilateral Cartesian min abs signal: 6.403929e+00
- near-equilateral Cartesian max abs signal: 1.665192e+01
- kills: ['dyadic-boundary correction does not recover Newtonian shadow within tolerance', 'finite-row rigidity prevents ephemeris recovery: final position residual exceeds tolerance', 'finite-row rigidity prevents ephemeris recovery: final velocity residual exceeds tolerance']

## Samples

### Weak Field

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 4.25, 5.200000000000002] | 9.621768e-13 | 1.954413e-14 |
| 1 | [1.0000000000000004, 8.65, 9.550000000000006] | 9.760308e-12 | -8.352359e-14 |
| 2 | [1.0, 14.199999999999992, 15.10000000000001] | 9.229683e-12 | -3.549438e-13 |

### Dyadic Boundary

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 99.99999999999996, 100.00000000000004] | 1.408128e-06 | 4.003468e-10 |
| 1 | [1.0000000000000013, 200.0000000000001, 200.0000000000001] | 1.434093e-06 | 2.083470e-09 |

### Controlled Near-Equilateral

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 1.0000000000000002, 1.0000000000000002] | 4.187314e+01 | 1.668010e+01 |
| 1 | [0.9999999999999999, 1.04, 0.9699999999999999] | 4.531840e+01 | 1.626045e+01 |
| 2 | [1.0, 0.9600000000000001, 1.03] | 1.106673e+01 | 6.414725e+00 |
| 3 | [1.02, 0.99, 1.0] | 3.496298e+01 | 1.468649e+01 |

### Ephemeris Propagation

| case | family | orbits | steps | final pos rel | final vel rel | max weak correction |
|---|---|---:|---:|---:|---:|---:|
| earth_moon_sun_quadrature | known_perturbed_three_body | 2 | 20 | 1.324531e-15 | 2.250267e-14 | 6.259522e-15 |
| jupiter_io_europa | known_perturbed_three_body | 2 | 20 | 1.772830e-10 | 1.596002e-09 | 1.000000e-10 |
| synthetic_lagrange_equilateral | synthetic_near_equilateral | 2 | 20 | 1.169556e+07 | 2.000266e+06 | 2.342441e+15 |

### Near-Equilateral Cartesian Sign Scan

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 1.0, 1.0] | 3.486053e+01 | 1.665192e+01 |
| 1 | [1.0, 1.04, 0.97] | 3.702588e+01 | 1.619427e+01 |
| 2 | [1.0, 0.96, 1.03] | 1.103287e+01 | 6.403929e+00 |
| 3 | [1.02, 0.99, 1.0] | 2.948900e+01 | 1.466436e+01 |

## Interpretation

A PASS means this finite bridge survives the fixed-parameter
reduced-shape and Cartesian ephemeris discriminator. A KILL means
the bridge remains a mathematical projection-closure prototype,
not a parameter-fixed physical candidate.
