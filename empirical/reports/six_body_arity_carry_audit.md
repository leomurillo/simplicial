# Six-Body Arity/Carry Audit

This is a controlled Paper 28 scaffold, not a claim about real gravitation.
Six bodies are the first room where 2 and 3 both tile the whole:
perfect matchings (`2+2+2`), bi-triangles (`3+3`), and `2x3` carry.

## Configuration

- trials: `10`
- steps: `850`
- dt: `0.0015`
- sample_stride: `25`
- masses: `[1.0, 1.12, 0.94, 1.07, 0.89, 1.16]`
- gravity: `0.18`
- softening: `0.3`
- mu_222: `0.015`
- nu_33: `0.02`
- kappa_23: `0.006`

## Force Recovery

### Pairwise Null

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0 | 0 | 0 | 0 | nan |
| pairwise_radial_basis | 90 | 0 | 0 | 0 | 0 | nan |
| triplet_basis | 20 | 0 | 0 | 0 | 0 | nan |
| tetra_basis | 15 | 0 | 0 | 0 | 0 | nan |
| lower_le4_basis | 125 | 0 | 0 | 0 | 0 | nan |
| matching222_one_coeff | 1 | 0 | 0 | 0 | 0 | 0 |
| bitriangle33_one_coeff | 1 | 0 | 0 | 0 | 0 | 0 |
| carry23_one_coeff | 1 | 0 | 0 | 0 | 0 | 0 |
| cover_222_33_23_basis | 3 | 0 | 0 | 0 | 0 | nan |
| lower_plus_cover_basis | 128 | 0 | 0 | 0 | 0 | nan |
| shuffled_carry23_feature | 1 | 0 | 0 | 0 | 0 | 0 |
| random_same_rank_feature | 1 | 0 | 0 | 0 | 0 | 0 |

### Matching 2+2+2 Planted

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0.0358891 | 0.035682 | 0 | 0 | nan |
| pairwise_radial_basis | 90 | 0.00186406 | 0.00268755 | 0.997302 | 0.994327 | nan |
| triplet_basis | 20 | 0.00177652 | 0.00167995 | 0.99755 | 0.997783 | nan |
| tetra_basis | 15 | 0.0287513 | 0.0286167 | 0.358218 | 0.356811 | nan |
| lower_le4_basis | 125 | 0.000436275 | 0.000974193 | 0.999852 | 0.999255 | nan |
| matching222_one_coeff | 1 | 1.758985e-17 | 1.757372e-17 | 1 | 1 | 0.015 |
| bitriangle33_one_coeff | 1 | 0.0113176 | 0.0105573 | 0.900555 | 0.91246 | 0.0191007 |
| carry23_one_coeff | 1 | 0.0192418 | 0.0179905 | 0.712549 | 0.745794 | 0.00296597 |
| cover_222_33_23_basis | 3 | 1.504190e-17 | 1.458426e-17 | 1 | 1 | nan |
| lower_plus_cover_basis | 128 | 6.792775e-16 | 6.167512e-16 | 1 | 1 | nan |
| shuffled_carry23_feature | 1 | 0.0308694 | 0.0302859 | 0.260173 | 0.279586 | 0.00179222 |
| random_same_rank_feature | 1 | 0.0358847 | 0.0357071 | 0.000246429 | -0.00140491 | 0.000567926 |

### Bi-Triangle 3+3 Planted

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0.0323416 | 0.031184 | 0 | 0 | nan |
| pairwise_radial_basis | 90 | 0.00351826 | 0.00585772 | 0.988166 | 0.964715 | nan |
| triplet_basis | 20 | 0.00968101 | 0.00883559 | 0.910398 | 0.91972 | nan |
| tetra_basis | 15 | 0.0270392 | 0.0259653 | 0.301023 | 0.306694 | nan |
| lower_le4_basis | 125 | 0.0009802 | 0.00228095 | 0.999081 | 0.99465 | nan |
| matching222_one_coeff | 1 | 0.00988469 | 0.0088803 | 0.906588 | 0.918905 | 0.0134211 |
| bitriangle33_one_coeff | 1 | 1.631605e-17 | 1.644508e-17 | 1 | 1 | 0.02 |
| carry23_one_coeff | 1 | 0.00814215 | 0.00729989 | 0.93662 | 0.945201 | 0.00359518 |
| cover_222_33_23_basis | 3 | 3.848528e-17 | 3.571899e-17 | 1 | 1 | nan |
| lower_plus_cover_basis | 128 | 4.812926e-17 | 5.347389e-17 | 1 | 1 | nan |
| shuffled_carry23_feature | 1 | 0.0290815 | 0.0277096 | 0.191443 | 0.21042 | 0.0016254 |
| random_same_rank_feature | 1 | 0.0323398 | 0.031196 | 0.000115105 | -0.00076842 | 0.000349778 |

### 2x3 Carry Planted

| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0.0513766 | 0.0458669 | 0 | 0 | nan |
| pairwise_radial_basis | 90 | 0.00804271 | 0.0151687 | 0.975494 | 0.89063 | nan |
| triplet_basis | 20 | 0.0264987 | 0.0221306 | 0.733978 | 0.767198 | nan |
| tetra_basis | 15 | 0.0454076 | 0.0401726 | 0.218866 | 0.232887 | nan |
| lower_le4_basis | 125 | 0.00291878 | 0.00612844 | 0.996772 | 0.982147 | nan |
| matching222_one_coeff | 1 | 0.0272682 | 0.0223953 | 0.718303 | 0.761595 | 0.0191156 |
| bitriangle33_one_coeff | 1 | 0.0130792 | 0.0107236 | 0.935192 | 0.945339 | 0.0311403 |
| carry23_one_coeff | 1 | 3.933709e-17 | 3.494810e-17 | 1 | 1 | 0.006 |
| cover_222_33_23_basis | 3 | 2.294164e-17 | 2.323640e-17 | 1 | 1 | nan |
| lower_plus_cover_basis | 128 | 4.573301e-17 | 4.651810e-17 | 1 | 1 | nan |
| shuffled_carry23_feature | 1 | 0.048446 | 0.042652 | 0.11083 | 0.135274 | 0.00199747 |
| random_same_rank_feature | 1 | 0.051376 | 0.0458732 | 2.492989e-05 | -0.000271878 | 0.000258588 |

## Divergence Replay: 2x3 Carry Planted Trajectory

| replay model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |
|---|---:|---:|---:|---:|
| pairwise_null | 0.0107376 | 0.0107376 | 0.0380347 | 0.0380347 |
| lower_le4_basis | 0.00129539 | 0.00129539 | 0.00206922 | 0.00206922 |
| cover_222_33_23_basis | 0 | 0 | 2.628295e-17 | 2.628295e-17 |
| recovered_carry23 | 2.616821e-17 | 2.616821e-17 | 5.965280e-17 | 5.965280e-17 |

## Invariants

| trajectory | max |P| | max angular drift | max relative energy drift |
|---|---:|---:|---:|
| truth | 1.433990e-15 | 6.828379e-16 | 1.050009e-06 |
| pairwise_null | 2.649749e-15 | 7.079372e-16 | 2.412429e-07 |
| recovered_carry23 | 1.420509e-15 | 6.828379e-16 | 1.050009e-06 |
| lower_le4_basis | 1.123907e-13 | 8.919191e-14 | nan |
| cover_222_33_23_basis | 1.537685e-15 | 6.826969e-16 | nan |

## Reading

The audit asks whether lower arities explain planted 6-body prime-cover channels.
Under the pairwise null, all residual models should remain at zero.
Under 2x3 carry planting, the carry feature should beat lower <=4 shadows and
recover the planted coefficient on held-out trajectories.
