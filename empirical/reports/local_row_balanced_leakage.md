# Local Row Balanced-Leakage Census

## Status

- JSON artifact: `C:\Projects\simplicial\empirical\reports\local_row_balanced_leakage.json`
- active leaf rule: canonical carry orbits with source,middle inside the leaf
- leakage rule: active carry orbit whose target lands outside the leaf
- balanced leakage: active leakage fraction weighted by the full-block residual survival ratio

This is a support-level finite audit over saved Ext_CH rows. It does not replace a leaf-specific full-block coboundary computation.

## F_4[u]/(u^2)

- source: `C:\Projects\simplicial\empirical\reports\ext_ch_cocycle_f4_u2.json`
- packets: `u, u^2`
- raw atoms / pairs / pair orbits: `1569` / `369` / `20`
- full-block residual weight: `1.000000`
- support-projection residual weight: `n/a`
- best regular leaf: `u^2`
- best proper regular leaf: `u^2`

| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `u+u^2` | 1.000000 | 20 | 0 | 0.000000 | 0.000000 | 0.000000 | full, regular, closed |
| 2 | `u^2` | 0.367113 | 7 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 3 | `u` | 0.028681 | 4 | 2 | 0.800000 | 0.800000 | 0.500000 | regular |

## F_2[u]/(u^2)

- source: `C:\Projects\simplicial\empirical\reports\next_local_row_f2_u2.json`
- packets: `u, u^2`
- raw atoms / pairs / pair orbits: `4` / `4` / `2`
- full-block residual weight: `1.000000`
- support-projection residual weight: `0.000000`
- best regular leaf: `u+u^2`
- best proper regular leaf: `None`

| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `u+u^2` | 1.000000 | 2 | 0 | 0.000000 | 0.000000 | 0.000000 | full, regular, closed |

## F_2[u]/(u^3)

- source: `C:\Projects\simplicial\empirical\reports\next_local_row_f2_u3.json`
- packets: `u, u^2, u^3`
- raw atoms / pairs / pair orbits: `100` / `52` / `10`
- full-block residual weight: `1.000000`
- support-projection residual weight: `0.000000`
- best regular leaf: `u^2+u^3`
- best proper regular leaf: `u^2+u^3`

| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `u+u^2+u^3` | 1.000000 | 10 | 0 | 0.000000 | 0.000000 | 0.000000 | full, regular, closed |
| 2 | `u^2+u^3` | 0.320000 | 3 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 3 | `u+u^3` | 0.560000 | 4 | 1 | 0.142857 | 0.142857 | 0.250000 | regular |
| 4 | `u+u^2` | 0.120000 | 3 | 1 | 0.666667 | 0.666667 | 0.333333 | regular |

## F_2[u]/(u^4)

- source: `C:\Projects\simplicial\empirical\reports\next_local_row_f2_u4.json`
- packets: `u, u^2, u^3, u^4`
- raw atoms / pairs / pair orbits: `1540` / `404` / `33`
- full-block residual weight: `1.000000`
- support-projection residual weight: `0.000000`
- best regular leaf: `u^3+u^4`
- best proper regular leaf: `u^3+u^4`

| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `u+u^2+u^3+u^4` | 1.000000 | 33 | 0 | 0.000000 | 0.000000 | 0.000000 | full, regular, closed |
| 2 | `u^2+u^3+u^4` | 0.519481 | 15 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 3 | `u^3+u^4` | 0.166234 | 5 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 4 | `u+u^3+u^4` | 0.628571 | 18 | 3 | 0.024793 | 0.024793 | 0.166667 | regular |
| 5 | `u^2+u^4` | 0.290909 | 6 | 1 | 0.142857 | 0.142857 | 0.166667 | regular |
| 6 | `u+u^2+u^4` | 0.672727 | 19 | 3 | 0.162162 | 0.162162 | 0.157895 | regular |
| 7 | `u+u^4` | 0.363636 | 8 | 3 | 0.200000 | 0.200000 | 0.375000 | regular |
| 8 | `u+u^2+u^3` | 0.179221 | 14 | 4 | 0.637681 | 0.637681 | 0.285714 | regular |
| 9 | `u^2+u^3` | 0.062338 | 4 | 1 | 0.666667 | 0.666667 | 0.250000 | regular |
| 10 | `u+u^3` | 0.098701 | 5 | 2 | 0.684211 | 0.684211 | 0.400000 | regular |
| 11 | `u+u^2` | 0.018182 | 5 | 3 | 0.857143 | 0.857143 | 0.600000 | regular |

## F_2[u]/(u^5)

- source: `C:\Projects\simplicial\empirical\reports\next_local_row_f2_u5.json`
- packets: `u, u^2, u^3, u^4, u^5`
- raw atoms / pairs / pair orbits: `19140` / `2516` / `81`
- full-block residual weight: `1.000000`
- support-projection residual weight: `0.000000`
- best regular leaf: `u^4+u^5`
- best proper regular leaf: `u^4+u^5`

| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `u+u^2+u^3+u^4+u^5` | 1.000000 | 81 | 0 | 0.000000 | 0.000000 | 0.000000 | full, regular, closed |
| 2 | `u^2+u^3+u^4+u^5` | 0.643678 | 46 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 3 | `u^3+u^4+u^5` | 0.334378 | 21 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 4 | `u^4+u^5` | 0.107001 | 7 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 5 | `u+u^3+u^4+u^5` | 0.687565 | 50 | 4 | 0.004255 | 0.004255 | 0.080000 | regular |
| 6 | `u^2+u^4+u^5` | 0.404598 | 25 | 4 | 0.024793 | 0.024793 | 0.160000 | regular |
| 7 | `u+u^2+u^4+u^5` | 0.742947 | 52 | 9 | 0.034318 | 0.034318 | 0.173077 | regular |
| 8 | `u+u^4+u^5` | 0.442215 | 28 | 7 | 0.039698 | 0.039698 | 0.250000 | regular |
| 9 | `u^3+u^5` | 0.187252 | 8 | 1 | 0.142857 | 0.142857 | 0.125000 | regular |
| 10 | `u^2+u^3+u^5` | 0.433020 | 26 | 3 | 0.162162 | 0.162162 | 0.115385 | regular |
| 11 | `u+u^2+u^3+u^5` | 0.713271 | 52 | 7 | 0.172282 | 0.172282 | 0.134615 | regular |
| 12 | `u+u^3+u^5` | 0.464368 | 28 | 5 | 0.173717 | 0.173717 | 0.178571 | regular |
| 13 | `u^2+u^5` | 0.234065 | 11 | 4 | 0.200000 | 0.200000 | 0.363636 | regular |
| 14 | `u+u^2+u^5` | 0.496343 | 29 | 11 | 0.211368 | 0.211368 | 0.379310 | regular |
| 15 | `u+u^5` | 0.259143 | 12 | 5 | 0.225806 | 0.225806 | 0.416667 | regular |
| 16 | `u+u^2+u^3+u^4` | 0.212539 | 43 | 10 | 0.621436 | 0.621436 | 0.232558 | regular |

## F_8[u]/(u^2)

- source: `C:\Projects\simplicial\empirical\reports\next_local_row_f8_u2.json`
- packets: `u, u^2`
- raw atoms / pairs / pair orbits: `158081` / `7105` / `49`
- full-block residual weight: `1.000000`
- support-projection residual weight: `0.000000`
- best regular leaf: `u^2`
- best proper regular leaf: `u^2`

| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `u+u^2` | 1.000000 | 49 | 0 | 0.000000 | 0.000000 | 0.000000 | full, regular, closed |
| 2 | `u^2` | 0.158703 | 20 | 0 | 0.000000 | 0.000000 | 0.000000 | regular, closed |
| 3 | `u` | 0.002790 | 6 | 3 | 0.888889 | 0.888889 | 0.500000 | thin |
