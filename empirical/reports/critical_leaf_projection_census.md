# Critical Leaf Projection Census

## Status

- JSON artifact: `C:\Projects\simplicial\empirical\reports\critical_leaf_projection_census.json`
- leaf model: nonempty cyclic conductor-packet subsets in the DFT basis
- leakage score: mean `rho_frac = 0.5 ||K^CH_p(s)s||_p / ||s||_p` after projection
- closure defect: fraction of the projected step's K^CH response outside the selected conductor support
- balanced leakage: mean `rho_frac * sqrt(closure defect)`, the outside cubic budget proxy

This is an empirical conductor-leaf proxy. It is a finite audit artifact, not by itself a proof of the RH reduction.

## weekdays / llama31_8b

- centroid source: `C:\Projects\simplicial\weekdays\baseline\per_class_output_dists.safetensors`
- conductors: `7`
- best regular leaf by rho_frac: `full_nontrivial`
- best proper leaf by rho_frac: `None`
- best non-flat leaf by rho_frac: `full_nontrivial`
- best proper non-flat leaf by rho_frac: `None`
- best regular leaf by closure-weighted score: `full_nontrivial`
- best regular leaf by balanced leakage: `full_nontrivial`

| rank | leaf | retained Fisher frac | rho | rho_frac | KCH norm | closure leakage | balanced leakage | packet balance | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `full_nontrivial` | 1.000000 | 1.951842 | 1.780817 | 6.563653 | 0.000000 | 0.000000 | 0.000000 | full |

### Best Leaf Detail

| label | retained Fisher frac | rho_frac | closure leakage | balanced leakage |
|---|---:|---:|---:|---:|
| Monday | 1.000000 | 1.265973 | 0.000000 | 0.000000 |
| Tuesday | 1.000000 | 1.742771 | 0.000000 | 0.000000 |
| Wednesday | 1.000000 | 1.716303 | 0.000000 | 0.000000 |
| Thursday | 1.000000 | 1.822443 | 0.000000 | 0.000000 |
| Friday | 1.000000 | 2.004337 | 0.000000 | 0.000000 |
| Saturday | 1.000000 | 1.718762 | 0.000000 | 0.000000 |
| Sunday | 1.000000 | 2.195129 | 0.000000 | 0.000000 |

## months / llama31_8b

- centroid source: `C:\Projects\simplicial\months\baseline\per_class_output_dists.safetensors`
- conductors: `2, 3, 4, 6, 12`
- best regular leaf by rho_frac: `conductor_2`
- best proper leaf by rho_frac: `conductor_2`
- best non-flat leaf by rho_frac: `conductor_3`
- best proper non-flat leaf by rho_frac: `conductor_3`
- best regular leaf by closure-weighted score: `conductor_2`
- best regular leaf by balanced leakage: `conductor_2`

| rank | leaf | retained Fisher frac | rho | rho_frac | KCH norm | closure leakage | balanced leakage | packet balance | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `conductor_2` | 0.085581 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | flat |
| 2 | `conductor_3` | 0.168923 | 0.707107 | 0.424048 | 1.032970 | 0.000000 | 0.000000 | 0.000000 | regular |
| 3 | `conductor_6` | 0.192102 | 0.707107 | 0.449338 | 1.147852 | 1.000000 | 0.449338 | 0.000000 | regular |
| 4 | `conductor_4` | 0.172981 | 0.992351 | 0.603231 | 1.486984 | 1.000000 | 0.603231 | 0.000000 | regular |
| 5 | `conductor_2+conductor_3` | 0.254504 | 1.054593 | 0.776413 | 2.322442 | 0.801566 | 0.695255 | 0.164138 | regular |
| 6 | `conductor_2+conductor_4` | 0.258562 | 1.151183 | 0.854652 | 2.575051 | 0.000000 | 0.000000 | 0.169317 | regular |
| 7 | `conductor_3+conductor_4` | 0.341905 | 1.172116 | 1.000184 | 3.464275 | 0.911152 | 0.954697 | 0.006033 | regular |
| 8 | `conductor_4+conductor_6` | 0.365083 | 1.164276 | 1.024199 | 3.634636 | 1.000000 | 1.024199 | 0.025918 | regular |
| 9 | `conductor_2+conductor_6` | 0.277683 | 1.408179 | 1.079310 | 3.333310 | 1.000000 | 1.079310 | 0.191106 | regular |
| 10 | `conductor_2+conductor_3+conductor_4` | 0.427486 | 1.232449 | 1.175934 | 4.555343 | 0.629324 | 0.932715 | 0.133314 | regular |
| 11 | `conductor_3+conductor_6` | 0.361025 | 1.403983 | 1.229019 | 4.340890 | 0.497429 | 0.867292 | 0.031871 | regular |
| 12 | `conductor_12` | 0.380412 | 1.397096 | 1.253939 | 4.529492 | 1.000000 | 1.253939 | 0.000000 | regular |

### Best Leaf Detail

| label | retained Fisher frac | rho_frac | closure leakage | balanced leakage |
|---|---:|---:|---:|---:|
| January | 0.070932 | 0.000000 | 0.000000 | 0.000000 |
| February | 0.087670 | 0.000000 | 0.000000 | 0.000000 |
| March | 0.085717 | 0.000000 | 0.000000 | 0.000000 |
| April | 0.067000 | 0.000000 | 0.000000 | 0.000000 |
| May | 0.095840 | 0.000000 | 0.000000 | 0.000000 |
| June | 0.090803 | 0.000000 | 0.000000 | 0.000000 |
| July | 0.091371 | 0.000000 | 0.000000 | 0.000000 |
| August | 0.088452 | 0.000000 | 0.000000 | 0.000000 |
| September | 0.088058 | 0.000000 | 0.000000 | 0.000000 |
| October | 0.088028 | 0.000000 | 0.000000 | 0.000000 |
| November | 0.089100 | 0.000000 | 0.000000 | 0.000000 |
| December | 0.083998 | 0.000000 | 0.000000 | 0.000000 |

## weekdays / mistral_7b

- centroid source: `C:\Projects\simplicial\per_class_output_dists.safetensors`
- conductors: `7`
- best regular leaf by rho_frac: `full_nontrivial`
- best proper leaf by rho_frac: `None`
- best non-flat leaf by rho_frac: `full_nontrivial`
- best proper non-flat leaf by rho_frac: `None`
- best regular leaf by closure-weighted score: `full_nontrivial`
- best regular leaf by balanced leakage: `full_nontrivial`

| rank | leaf | retained Fisher frac | rho | rho_frac | KCH norm | closure leakage | balanced leakage | packet balance | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `full_nontrivial` | 1.000000 | 1.808926 | 1.600247 | 5.718552 | 0.000000 | 0.000000 | 0.000000 | full |

### Best Leaf Detail

| label | retained Fisher frac | rho_frac | closure leakage | balanced leakage |
|---|---:|---:|---:|---:|
| Monday | 1.000000 | 1.377203 | 0.000000 | 0.000000 |
| Tuesday | 1.000000 | 1.798680 | 0.000000 | 0.000000 |
| Wednesday | 1.000000 | 1.470533 | 0.000000 | 0.000000 |
| Thursday | 1.000000 | 2.106975 | 0.000000 | 0.000000 |
| Friday | 1.000000 | 1.789494 | 0.000000 | 0.000000 |
| Saturday | 1.000000 | 1.416267 | 0.000000 | 0.000000 |
| Sunday | 1.000000 | 1.242579 | 0.000000 | 0.000000 |
