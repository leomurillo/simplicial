# Four-Body Tetrahedral Residual Audit

This is a controlled Paper 28 arity-resolution scaffold, not a claim about real gravitation.
The null is softened pairwise Newtonian mechanics. The tetrahedral planted alternative adds
`V4 = -beta*prod(m_i)*Delta_1234^2/prod(s_ij)^gamma`.

## Gate Verdict

- Status: `PASS_ARITY_RESOLUTION_GATE`
- kills: `[]`
- recovered beta: `0.08`
- lower edge-plus-face held-out R2 on tetra planting: `0.35115`
- tetra feature held-out R2 on tetra planting: `1`
- held-out C4 min tetra/face ratio: `20942.3`
- planar tetra force norm: `0`
- cluster force suppression ratio: `0.000303721`

## Configuration

- trials: `16`
- steps: `1400`
- dt: `0.0015`
- sample stride: `20`
- masses: `[1.0, 1.18, 0.9, 1.07]`
- softening: `0.18`
- gamma: `1.0`
- face alpha: `0.025`
- tetra beta: `0.08`

## Force Recovery

### Pairwise Null

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0 | 0 | 0 | 0 | nan |
| pairwise_only_radial_basis | 36 | 0 | 0 | 0 | 0 | nan |
| face_triplet_basis | 4 | 0 | 0 | 0 | 0 | nan |
| lower_pairwise_plus_face | 40 | 0 | 0 | 0 | 0 | nan |
| tetra_one_coefficient | 1 | 0 | 0 | 0 | 0 | 0 |
| lower_plus_tetra | 41 | 0 | 0 | 0 | 0 | nan |
| shuffled_tetra_feature | 1 | 0 | 0 | 0 | 0 | 0 |
| random_same_rank_feature | 1 | 0 | 0 | 0 | 0 | 0 |

### Face-Triplet Planted

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 1.00274 | 1.11346 | 0 | 0 | nan |
| pairwise_only_radial_basis | 36 | 0.305936 | 0.338492 | 0.906914 | 0.907584 | nan |
| face_triplet_basis | 4 | 4.655356e-16 | 5.628384e-16 | 1 | 1 | nan |
| lower_pairwise_plus_face | 40 | 8.501907e-15 | 8.490631e-15 | 1 | 1 | nan |
| tetra_one_coefficient | 1 | 0.983156 | 1.09223 | 0.03868 | 0.0377723 | -31.4861 |
| lower_plus_tetra | 41 | 7.549500e-15 | 7.474242e-15 | 1 | 1 | nan |
| shuffled_tetra_feature | 1 | 1.00169 | 1.11213 | 0.00210249 | 0.00239169 | 7.3408 |
| random_same_rank_feature | 1 | 1.00274 | 1.11345 | 2.566082e-07 | 2.300870e-05 | 0.000501477 |

### Tetrahedral Planted

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0.000484623 | 0.000494043 | 0 | 0 | nan |
| pairwise_only_radial_basis | 36 | 0.000375308 | 0.000435887 | 0.400255 | 0.221574 | nan |
| face_triplet_basis | 4 | 0.000467388 | 0.000477947 | 0.0698636 | 0.0640986 | nan |
| lower_pairwise_plus_face | 40 | 0.000354517 | 0.000397958 | 0.464861 | 0.35115 | nan |
| tetra_one_coefficient | 1 | 6.771777e-17 | 6.890280e-17 | 1 | 1 | 0.08 |
| lower_plus_tetra | 41 | 6.717225e-17 | 7.132779e-17 | 1 | 1 | nan |
| shuffled_tetra_feature | 1 | 0.000458621 | 0.000477972 | 0.104431 | 0.0640007 | 0.0258527 |
| random_same_rank_feature | 1 | 0.000484589 | 0.000494094 | 0.000139893 | -0.000203056 | 5.658867e-06 |

## Divergence Replay: Tetrahedral Planted Trajectory

| replay model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |
|---|---:|---:|---:|---:|
| pairwise_null | 0.000784644 | 0.000784644 | 0.00108093 | 0.00149357 |
| pairwise_only_radial_basis | 0.000234735 | 0.000234735 | 0.000479434 | 0.000479434 |
| lower_pairwise_plus_face | 0.00018039 | 0.00018039 | 0.000374886 | 0.000374886 |
| recovered_tetra | 0 | 0 | 0 | 0 |

## C4 Minimal-Nonface Detector

The detector uses the three opposite-edge mixed derivatives and the four
vertex-star mixed derivatives of the scalar potential in squared-edge
coordinates.

- first replay tetra C4 max abs: `0.000987372`
- first replay face C4 max abs: `5.551115e-08`
- tetra opposite-edge derivatives: `['0.000987372', '0.000140681', '0.000820456']`
- tetra vertex-star derivatives: `['0.000430593', '0.000583043', '0.000549571', '0.000606261']`

### Held-Out Asymmetric C4 Samples

- held-out trial ids: `[10, 11, 12, 13, 14, 15]`
- sample count: `18`
- min tetra volume: `0.0249346`
- min edge-length CV: `0.118313`
- min tetra C4 max abs: `0.00115367`
- max face C4 max abs: `4.440892e-07`
- min tetra/face C4 ratio: `20942.3`
- max opposite-edge C4 abs: `0.0292456`
- max vertex-star C4 abs: `0.11246`

| trial | t | volume | edge CV | tetra C4 | face C4 | ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 20 | 0.366695 | 0.162556 | 0.0012914 | 2.775558e-08 | 46527.5 |
| 10 | 700 | 0.0331162 | 0.366951 | 0.11246 | 2.220446e-07 | 5.064755e+05 |
| 10 | 1380 | 0.0270157 | 0.314256 | 0.0279903 | 1.110223e-07 | 2.521144e+05 |
| 11 | 20 | 0.365531 | 0.161457 | 0.00138338 | 5.551115e-08 | 24920.8 |
| 11 | 700 | 0.0448869 | 0.334188 | 0.0713746 | 4.440892e-07 | 1.607213e+05 |
| 11 | 1380 | 0.0249346 | 0.334963 | 0.0794211 | 2.220446e-07 | 3.576808e+05 |
| 12 | 20 | 0.378775 | 0.129175 | 0.00115367 | 2.775558e-08 | 41565.4 |
| 12 | 700 | 0.0631643 | 0.252372 | 0.0244451 | 2.220446e-07 | 1.100911e+05 |
| 12 | 1380 | 0.0403733 | 0.224326 | 0.0506987 | 2.220446e-07 | 2.283266e+05 |
| 13 | 20 | 0.35756 | 0.147419 | 0.00130019 | 2.775558e-08 | 46844.2 |
| 13 | 700 | 0.0489335 | 0.240706 | 0.0386575 | 3.330669e-07 | 1.160653e+05 |
| 13 | 1380 | 0.049523 | 0.216157 | 0.0396075 | 2.220446e-07 | 1.783761e+05 |

## Degeneration Controls

| control | value |
|---|---:|
| planar volume | 0 |
| planar tetra force norm | 0 |
| planar tetra potential abs | 0 |
| cluster radius | 10000 |
| cluster force suppression ratio | 0.000303721 |
| cluster potential suppression ratio | 0.000246723 |

## Invariants

| trajectory | max |P| | max angular drift | max relative energy drift |
|---|---:|---:|---:|
| truth | 8.907291e-15 | 2.353994e-15 | 5.742580e-05 |
| pairwise_null | 6.381187e-15 | 5.736816e-15 | 5.762141e-05 |
| recovered_tetra | 8.907291e-15 | 2.353994e-15 | 5.742580e-05 |
| pairwise_only_radial_basis | 1.604051e-14 | 2.610943e-15 | nan |
| lower_pairwise_plus_face | 5.264787e-15 | 3.231231e-15 | nan |

## Reading

The audit asks for type separation. Under the null, residual coefficients should vanish.
Under face-triplet planting, lower-arity face features should explain the residual.
Under tetrahedral planting, a one-coefficient tetrahedral feature should recover beta,
while lower-arity shadows should be reported as controls rather than arity certificates.
