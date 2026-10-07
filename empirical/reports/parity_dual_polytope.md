# Parity-Dual Polytope Census

**Script:** `empirical/census_parity_dual_polytope.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** all checks passed

For `N=2m`, the convex hull of the parity-dual compound has the exact decomposition

```text
conv(X_N) ~= (Delta_{m-1} direct-sum Delta_{m-1}) x I.
```

The base `Delta_{m-1} direct-sum Delta_{m-1}` is polar to `Delta_{m-1} x Delta_{m-1}`.  The f-vectors below are computed from this decomposition, not from numerical convex-hull software.

| N | m | dim conv(X_N) | base f-vector | conv(X_N) f-vector | vertices | facets |
|---:|---:|---:|---|---|---:|---:|
| 4 | 2 | 3 | `(4, 4)` | `(8, 12, 6)` | 8 | 6 |
| 6 | 3 | 5 | `(6, 15, 18, 9)` | `(12, 36, 51, 36, 11)` | 12 | 11 |
| 8 | 4 | 7 | `(8, 28, 56, 68, 48, 16)` | `(16, 64, 140, 192, 164, 80, 18)` | 16 | 18 |
| 10 | 5 | 9 | `(10, 45, 120, 210, 250, 200, 100, 25)` | `(20, 100, 285, 540, 710, 650, 400, 150, 27)` | 20 | 27 |
| 12 | 6 | 11 | `(12, 66, 220, 495, 792, 922, 780, 465, 180, 36)` | `(24, 144, 506, 1210, 2079, 2636, 2482, 1710, 825, 252, 38)` | 24 | 38 |

## Consequences

1. `N=4` gives a cube: the prism over the free sum of two segments, i.e. over a square.
2. `N=6` gives a 5-polytope with f-vector `(12, 36, 51, 36, 11)`: a prism over the free sum of two triangles.
3. In general the polytope is vertex-transitive under the full Gram/orthogonal stabilizer, but it is not centrally symmetric for `N>=6`.
4. The polar polytope is the bipyramid over `Delta_{m-1} x Delta_{m-1}`.
