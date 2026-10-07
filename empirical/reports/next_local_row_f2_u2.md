# Next Local Row Verification

- ring: F_2[u]/(u^2)
- labels: 4 total, 3 nontrivial
- packets: {'u': 1, 'u^2': 2}
- Gamma size: 2
- quotient-shift generators: 7
- quotient-shift support distribution: {1: 5, 2: 2}
- carry records: 4

## Carry Paths

- u^2->u->u^2: 4

## Ext_CH

- raw atoms: 4
- raw carry pairs: 4
- canonical pair orbits: 2
- pair-orbit missing total: 0
- raw coefficient distribution: {'-1': 4}
- full-block dimensions: C1 17, C2 61

### Canonical Pair-Orbit Representative Table

| orbit | size | atoms | path | representative | coeffs |
|---:|---:|---:|---|---|---|
| 1 | 2 | 2 | u^2->u->u^2 | `1 <- 1 (u^2->u->u^2)` | `{'-1': 2}` |
| 2 | 2 | 2 | u^2->u->u^2 | `1 <- 1+u (u^2->u->u^2)` | `{'-1': 2}` |

## Closed Cells

- H3: 6 cells / 1 orbits
- H4: 21 cells / 4 orbits

### H3 Orbit Table

| orbit | size | family | representative |
|---:|---:|---|---|
| 0 | 6 | 122 | `(1, 1+u, u)` |

### H4 Orbit Table

| orbit | size | family | representative |
|---:|---:|---|---|
| 0 | 2 | 2222 | `(1, 1, 1, 1)` |
| 1 | 6 | 2222 | `(1, 1, 1+u, 1+u)` |
| 2 | 12 | 1122 | `(1, 1, u, u)` |
| 3 | 1 | 1111 | `(u, u, u, u)` |

## Fisher Probe

- modes: u and 1
- supports: order0 2, left1 3, right1 2, mixed2 2

## Full-Block Coboundary Diagnostic

- coefficient field: Q
- C1 generators: 17
- C2 dimension: 61
- coboundary rank: 16
- residual quotient dimension: 45
- raw support: 4
- residual support: 4
- residual equals raw cochain: True
- raw is coboundary: False
- rational rank certified: True
- rational non-coboundary certified: True

## Support-Projection Coboundary Diagnostic

- mode: support
- C2 scope: raw_support
- coefficient field: Q
- C1 generators: 9
- C2 dimension: 4
- coboundary rank: 4
- residual quotient dimension: 0
- raw support: 4
- residual support: 0
- residual equals raw cochain: False
- raw is coboundary in projection: True
