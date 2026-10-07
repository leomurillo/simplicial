# Helmert Primorial/Squarefree Testbed

This report is the first Paper 25 frame-ledger testbed outside local
fields.  For squarefree cyclic rows `Z/nZ`, conductor packets form a
CRT divisor lattice.  A target conductor `d` uses the active prefix
spanned by all packets `e | d`; this replaces the wild quotient prefix
used in `F_q[u]/(u^k)`.

The table compares the conductor/CRT frame against Haar mixed frames
with the same conductor block sizes.  `structural` means the ledger
without packet-commutator or first-order packet price.  The break-even
columns record the packet price needed when a mixed frame beats that
unpriced structural ledger.

## Config

- `rows`: `[6, 10, 15, 30]`
- `samples`: `300`
- `seed`: `20260516`
- `amplitude_fraction`: `0.35`
- `min_target_omega`: `2`
- `weights`: `{'block': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1, 'packet_commutator': 1.0, 'first_order_packet': 0.0}`

## Summary

| row | target | active conductors | dim | active dim | conductor structural | random structural min | random structural median | better structural | break-even M max | break-even N max | better full |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Z/6Z | 6 | [2, 3, 6] | 5 | 5 | 0.4908565 | 0.2173471 | 0.3700725 | 300/300 | 0.4570348 | 0.07304119 | 0/300 |
| Z/10Z | 10 | [2, 5, 10] | 9 | 9 | 0.7246988 | 0.3760289 | 0.4986332 | 300/300 | 0.716222 | 0.07084902 | 0/300 |
| Z/15Z | 15 | [3, 5, 15] | 14 | 14 | 0.5902569 | 0.3765982 | 0.4786796 | 300/300 | 0.3723366 | 0.03269403 | 0/300 |
| Z/30Z | 6 | [2, 3, 6] | 29 | 5 | 2.128929 | 3.294069 | 4.14183 | 0/300 | 0 | 0 | 0/300 |
| Z/30Z | 10 | [2, 5, 10] | 29 | 9 | 1.942345 | 2.900719 | 3.602122 | 0/300 | 0 | 0 | 0/300 |
| Z/30Z | 15 | [3, 5, 15] | 29 | 14 | 0.9746979 | 1.834945 | 2.543592 | 0/300 | 0 | 0 | 0/300 |
| Z/30Z | 30 | [2, 3, 5, 6, 10, 15, 30] | 29 | 29 | 1.127446 | 0.8371502 | 0.9315863 | 300/300 | 0.2352106 | 0.01040922 | 0/300 |

## Detail

### Z/6Z target conductor `6`

- conductor order: `[2, 3, 6]`
- packet sizes: `{'2': 1, '3': 2, '6': 2}`
- active conductors: `[2, 3, 6]`
- probability range: `0.11125` to `0.222083`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.2908565 | 0.1700725 | 0.088594 | 0.2500821 |
| fisher_projection_error | 0 | 0 | 0 | 3.330669e-16 |
| reciprocal_projection_error | 0 | 0 | 0 | 3.330669e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |
| packet_commutator_impurity | 0 | 0.7464685 | 0.4429845 | 1.001067 |
| first_order_packet_cost | 0 | 4.168582 | 3.441266 | 4.750834 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 14 | 0.2173471 | 0.2735094 | 0.3025462 | 0.06281104 | 0.01734709 | 0 | 0 |
| 221 | 0.2358868 | 0.2549697 | 0.239587 | 0.05835948 | 0.03588685 | 0 | 0 |
| 130 | 0.2406163 | 0.2502402 | 0.3689054 | 0.0646631 | 0.04061632 | 0 | 8.881784e-16 |
| 9 | 0.2466026 | 0.2442539 | 0.2856266 | 0.07304119 | 0.04660261 | 0 | 0 |
| 81 | 0.2586675 | 0.232189 | 0.2666597 | 0.05057266 | 0.05866751 | 0 | 0 |

### Z/10Z target conductor `10`

- conductor order: `[2, 5, 10]`
- packet sizes: `{'2': 1, '5': 4, '10': 4}`
- active conductors: `[2, 5, 10]`
- probability range: `0.06675` to `0.13325`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.5246988 | 0.2986332 | 0.2094027 | 0.3872997 |
| fisher_projection_error | 0 | 0 | 0 | 3.330669e-16 |
| reciprocal_projection_error | 0 | 2.220446e-16 | 0 | 4.440892e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |
| packet_commutator_impurity | 0 | 0.6565139 | 0.4950814 | 0.807758 |
| first_order_packet_cost | 0 | 5.264827 | 4.704792 | 5.673777 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 122 | 0.3760289 | 0.3486699 | 0.6031824 | 0.06781577 | 0.1760289 | 0 | 2.220446e-16 |
| 247 | 0.3791675 | 0.3455313 | 0.4523509 | 0.06561168 | 0.1791675 | 0 | 0 |
| 80 | 0.3822969 | 0.342402 | 0.6072884 | 0.06153931 | 0.1822969 | 0 | 0 |
| 299 | 0.3911438 | 0.333555 | 0.4603845 | 0.06011848 | 0.1911438 | 0 | 1.110223e-16 |
| 44 | 0.394081 | 0.3306178 | 0.5068451 | 0.05978732 | 0.194081 | 0 | 0 |

### Z/15Z target conductor `15`

- conductor order: `[3, 5, 15]`
- packet sizes: `{'3': 2, '5': 4, '15': 8}`
- active conductors: `[3, 5, 15]`
- probability range: `0.0445` to `0.0904248`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.3902569 | 0.2786796 | 0.2175799 | 0.3427145 |
| fisher_projection_error | 0 | 0 | 0 | 4.440892e-16 |
| reciprocal_projection_error | 0 | 0 | 0 | 2.220446e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |
| packet_commutator_impurity | 0 | 0.6165102 | 0.5304304 | 0.7039859 |
| first_order_packet_cost | 0 | 6.64652 | 6.20096 | 6.998387 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 297 | 0.3765982 | 0.2136586 | 0.3613948 | 0.03269403 | 0.1765982 | 0 | 0 |
| 38 | 0.3844527 | 0.2058041 | 0.3430005 | 0.03060417 | 0.1844527 | 0 | 2.220446e-16 |
| 176 | 0.3981384 | 0.1921184 | 0.3142041 | 0.02905773 | 0.1981384 | 0 | 0 |
| 225 | 0.4034979 | 0.186759 | 0.2744048 | 0.02689623 | 0.2034979 | 0 | 2.220446e-16 |
| 189 | 0.4035969 | 0.1866599 | 0.3470774 | 0.02815735 | 0.2035969 | 0 | 4.440892e-16 |

### Z/30Z target conductor `6`

- conductor order: `[2, 3, 5, 6, 10, 15, 30]`
- packet sizes: `{'2': 1, '3': 2, '5': 4, '6': 2, '10': 4, '15': 8, '30': 8}`
- active conductors: `[2, 3, 6]`
- probability range: `0.02225` to `0.0444167`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 2.045021 | 1.60027 | 1.49734 | 1.684128 |
| fisher_projection_error | 0 | 0.8490289 | 0.6710064 | 0.9653592 |
| reciprocal_projection_error | 0 | 0.8392867 | 0.666823 | 0.9637123 |
| closure_leakage | 0 | 0.7872474 | 0.7091591 | 0.8470507 |
| resource_cost | 0.1724138 | 0.1724138 | 0.1724138 | 0.1724138 |
| depth_cost | 0.6666667 | 0.6666667 | 0.6666667 | 0.6666667 |
| packet_commutator_impurity | 0 | 1.235788 | 1.197094 | 1.267908 |
| first_order_packet_cost | 0 | 27.88497 | 27.28709 | 28.33291 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 65 | 3.294069 | -1.16514 | 0 | 0 | 1.527514 | 0.7746495 | 0.9079974 |
| 107 | 3.573847 | -1.444917 | 0 | 0 | 1.676653 | 0.8073046 | 1.005981 |
| 205 | 3.620279 | -1.49135 | 0 | 0 | 1.613621 | 0.7313791 | 1.191371 |
| 189 | 3.623161 | -1.494232 | 0 | 0 | 1.546685 | 0.7960009 | 1.196567 |
| 222 | 3.64045 | -1.511521 | 0 | 0 | 1.632043 | 0.8107976 | 1.113701 |

### Z/30Z target conductor `10`

- conductor order: `[2, 3, 5, 6, 10, 15, 30]`
- packet sizes: `{'2': 1, '3': 2, '5': 4, '6': 2, '10': 4, '15': 8, '30': 8}`
- active conductors: `[2, 5, 10]`
- probability range: `0.02225` to `0.0444167`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 1.844644 | 1.468164 | 1.383535 | 1.548433 |
| fisher_projection_error | 0 | 0.6977375 | 0.4895527 | 0.8579281 |
| reciprocal_projection_error | 0 | 0.7020371 | 0.4919645 | 0.8713856 |
| closure_leakage | 0 | 0.6518046 | 0.5982677 | 0.6928344 |
| resource_cost | 0.3103448 | 0.3103448 | 0.3103448 | 0.3103448 |
| depth_cost | 0.6666667 | 0.6666667 | 0.6666667 | 0.6666667 |
| packet_commutator_impurity | 0 | 1.235813 | 1.196431 | 1.27093 |
| first_order_packet_cost | 0 | 27.81307 | 27.32091 | 28.35111 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 37 | 2.900719 | -0.9583743 | 0 | 0 | 1.49212 | 0.6358944 | 0.6750034 |
| 104 | 2.939602 | -0.9972574 | 0 | 0 | 1.352776 | 0.6672568 | 0.8218688 |
| 173 | 3.015032 | -1.072688 | 0 | 0 | 1.424284 | 0.6191062 | 0.8739407 |
| 260 | 3.058899 | -1.116554 | 0 | 0 | 1.402452 | 0.5985743 | 0.9601718 |
| 291 | 3.060084 | -1.11774 | 0 | 0 | 1.443101 | 0.6672264 | 0.8520563 |

### Z/30Z target conductor `15`

- conductor order: `[2, 3, 5, 6, 10, 15, 30]`
- packet sizes: `{'2': 1, '3': 2, '5': 4, '6': 2, '10': 4, '15': 8, '30': 8}`
- active conductors: `[3, 5, 15]`
- probability range: `0.02225` to `0.0452124`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.8597554 | 0.8587688 | 0.8013641 | 0.9077003 |
| fisher_projection_error | 0 | 0.543866 | 0.3191297 | 0.7427821 |
| reciprocal_projection_error | 0 | 0.541097 | 0.335865 | 0.7491497 |
| closure_leakage | 0 | 0.4873999 | 0.4555461 | 0.5165194 |
| resource_cost | 0.4827586 | 0.4827586 | 0.4827586 | 0.4827586 |
| depth_cost | 0.6666667 | 0.6666667 | 0.6666667 | 0.6666667 |
| packet_commutator_impurity | 0 | 1.239581 | 1.207283 | 1.269093 |
| first_order_packet_cost | 0 | 27.89349 | 27.28594 | 28.36264 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 242 | 1.834945 | -0.8602472 | 0 | 0 | 0.8405392 | 0.5068549 | 0.3726085 |
| 17 | 1.904637 | -0.9299394 | 0 | 0 | 0.8703231 | 0.46605 | 0.4533217 |
| 211 | 1.913962 | -0.9392643 | 0 | 0 | 0.8735453 | 0.4584763 | 0.4669981 |
| 190 | 1.915898 | -0.9412004 | 0 | 0 | 0.7936716 | 0.474396 | 0.5328882 |
| 106 | 1.922048 | -0.9473498 | 0 | 0 | 0.8586861 | 0.5001324 | 0.4482867 |

### Z/30Z target conductor `30`

- conductor order: `[2, 3, 5, 6, 10, 15, 30]`
- packet sizes: `{'2': 1, '3': 2, '5': 4, '6': 2, '10': 4, '15': 8, '30': 8}`
- active conductors: `[2, 3, 5, 6, 10, 15, 30]`
- probability range: `0.02225` to `0.0444167`

| term | conductor | random median | random p05 | random p95 |
|---|---:|---:|---:|---:|
| block_coupling | 0.9274456 | 0.7315863 | 0.6860671 | 0.7739016 |
| fisher_projection_error | 0 | 0 | 0 | 2.220446e-16 |
| reciprocal_projection_error | 0 | 0 | 0 | 3.330669e-16 |
| closure_leakage | 0 | 0 | 0 | 0 |
| resource_cost | 1 | 1 | 1 | 1 |
| depth_cost | 1 | 1 | 1 | 1 |
| packet_commutator_impurity | 0 | 1.240199 | 1.200788 | 1.271796 |
| first_order_packet_cost | 0 | 27.91325 | 27.42321 | 28.39354 |

| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | 0.8371502 | 0.2902954 | 0.2333847 | 0.01040922 | 0.6371502 | 0 | 4.440892e-16 |
| 101 | 0.8422326 | 0.285213 | 0.2352106 | 0.01025703 | 0.6422326 | 0 | 2.220446e-16 |
| 124 | 0.8505912 | 0.2768544 | 0.2226382 | 0.009829436 | 0.6505912 | 0 | 0 |
| 32 | 0.8634463 | 0.2639993 | 0.2205836 | 0.009481461 | 0.6634463 | 0 | 0 |
| 104 | 0.8679269 | 0.2595188 | 0.206181 | 0.009423103 | 0.6679269 | 0 | 1.110223e-16 |

## Reading

For local wild rows, Theorems 3.10 and 3.14 use a quotient map that
preserves packet prefixes.  Squarefree rows do not have that single
tower map.  This testbed replaces it with the CRT divisor prefix
`e | d`.  If mixed frames beat the conductor frame structurally, the
break-even columns quantify how much packet budget is needed to keep
prime/conductor compatibility.

In the default run, full-conductor rows behave like top-prefix rows:
`Z/6Z`, `Z/10Z`, `Z/15Z`, and the full `Z/30Z` target all have
mixed structural wins in every sample, but none survive the unit
packet-commutator price.  The proper CRT faces inside `Z/30Z`,
targets `6`, `10`, and `15`, show no mixed structural wins in 300
samples.  This suggests a candidate squarefree replacement for local
packet-locality: proper primorial faces may have structural
CRT-face stability, while full-conductor rows retain the top-prefix
need for priced carry.

The next theorem-facing question is whether these budgets and face
stability signals have stable scaling along primorial rows.
