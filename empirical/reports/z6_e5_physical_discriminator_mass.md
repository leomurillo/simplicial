# Z6 E5 Physical Discriminator

- Claim tested: E5 parameter-fixed physical discriminator for the Z6 canonical bridge
- Status: KILL

## Pre-Registration

- Model: a_candidate = a_Newton + lambda_E5 * (a_EL(eta_copula)-a_EL(eta_base))
- Cartesian lift: mass-metric minimum-norm inverse of D sigma
- participation lift: mass
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

- lambda_E5: 2.331680584938e-03
- lambda source: ephemeris
- weak-field max relative correction: 1.802116e-12
- dyadic-boundary max relative correction: 9.996192e-06
- controlled relative signed projections: ['1.833278e-06', '1.796015e-06', '7.085256e-07', '1.615671e-06']
- controlled signs: [1, 1, 1, 1]
- controlled sign-definite: True
- controlled min abs signal: 7.085256e-07
- controlled max abs signal: 1.833278e-06
- ephemeris final position max: 3.789840e-04
- ephemeris final velocity max: 4.947096e-04
- ephemeris weak-field max sampled correction: 1.014886e-10
- near-equilateral Cartesian signed projections: ['1.830180e-06', '1.788704e-06', '7.073333e-07', '1.613237e-06']
- near-equilateral Cartesian signs: [1, 1, 1, 1]
- near-equilateral Cartesian sign-definite: True
- near-equilateral Cartesian min abs signal: 7.073333e-07
- near-equilateral Cartesian max abs signal: 1.830180e-06
- kills: ['dyadic-boundary correction does not recover Newtonian shadow within tolerance', 'ephemeris weak-field acceleration correction exceeds 1e-10 cap', 'finite-row rigidity prevents ephemeris recovery: final position residual exceeds tolerance', 'finite-row rigidity prevents ephemeris recovery: final velocity residual exceeds tolerance']

## Samples

### Weak Field

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 4.25, 5.200000000000002] | 5.029798e-14 | 1.021673e-15 |
| 1 | [1.0000000000000004, 8.65, 9.550000000000006] | 7.977986e-13 | -6.827141e-15 |
| 2 | [1.0, 14.199999999999992, 15.10000000000001] | 1.802116e-12 | -6.930355e-14 |

### Dyadic Boundary

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 99.99999999999996, 100.00000000000004] | 2.478417e-06 | 7.046421e-10 |
| 1 | [1.0000000000000013, 200.0000000000001, 200.0000000000001] | 9.996192e-06 | 1.452261e-08 |

### Controlled Near-Equilateral

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0000000000000002, 1.0000000000000002, 1.0000000000000002] | 4.602197e-06 | 1.833278e-06 |
| 1 | [0.9999999999999999, 1.04, 0.9699999999999999] | 5.005551e-06 | 1.796015e-06 |
| 2 | [1.0, 0.9600000000000001, 1.03] | 1.222353e-06 | 7.085256e-07 |
| 3 | [1.02, 0.99, 1.0] | 3.846303e-06 | 1.615671e-06 |

### Ephemeris Propagation

| case | family | orbits | steps | final pos rel | final vel rel | max weak correction |
|---|---|---:|---:|---:|---:|---:|
| earth_moon_sun_quadrature | known_perturbed_three_body | 2 | 20 | 8.904854e-16 | 1.534873e-14 | 6.236406e-17 |
| jupiter_io_europa | known_perturbed_three_body | 2 | 20 | 1.364257e-09 | 3.726244e-09 | 1.014886e-10 |
| synthetic_lagrange_equilateral | synthetic_near_equilateral | 2 | 20 | 3.789840e-04 | 4.947096e-04 | 2.034493e-08 |

### Near-Equilateral Cartesian Sign Scan

| idx | sides | relative correction | signed projection |
|---:|---|---:|---:|
| 0 | [1.0, 1.0, 1.0] | 3.831455e-06 | 1.830180e-06 |
| 1 | [1.0, 1.04, 0.97] | 4.089617e-06 | 1.788704e-06 |
| 2 | [1.0, 0.96, 1.03] | 1.218614e-06 | 7.073333e-07 |
| 3 | [1.02, 0.99, 1.0] | 3.244106e-06 | 1.613237e-06 |

## Interpretation

A PASS means this finite bridge survives the fixed-parameter
reduced-shape and Cartesian ephemeris discriminator. A KILL means
the bridge remains a mathematical projection-closure prototype,
not a parameter-fixed physical candidate.
