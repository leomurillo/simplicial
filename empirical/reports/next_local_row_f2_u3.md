# Next Local Row Verification

- ring: F_2[u]/(u^3)
- labels: 8 total, 7 nontrivial
- packets: {'u': 1, 'u^2': 2, 'u^3': 4}
- Gamma size: 8
- quotient-shift generators: 27
- quotient-shift support distribution: {1: 13, 2: 10, 4: 4}
- carry records: 52

## Carry Paths

- u^2->u->u^2: 4
- u^2->u->u^3: 8
- u^3->u->u^2: 8
- u^3->u->u^3: 16
- u^3->u^2->u^3: 16

## Ext_CH

- raw atoms: 100
- raw carry pairs: 52
- canonical pair orbits: 10
- pair-orbit missing total: 0
- raw coefficient distribution: {'-1': 100}
- full-block dimensions: C1 177, C2 1709

### Canonical Pair-Orbit Representative Table

| orbit | size | atoms | path | representative | coeffs |
|---:|---:|---:|---|---|---|
| 1 | 2 | 2 | u^2->u->u^2 | `u <- u (u^2->u->u^2)` | `{'-1': 2}` |
| 2 | 2 | 2 | u^2->u->u^2 | `u <- u+u^2 (u^2->u->u^2)` | `{'-1': 2}` |
| 3 | 8 | 8 | u^2->u->u^3 | `1 <- u (u^2->u->u^3)` | `{'-1': 8}` |
| 4 | 8 | 8 | u^3->u->u^2 | `u <- 1 (u^3->u->u^2)` | `{'-1': 8}` |
| 5 | 4 | 12 | u^3->u->u^3 | `1 <- 1 (u^3->u->u^3)` | `{'-1': 12}` |
| 6 | 8 | 24 | u^3->u->u^3 | `1 <- 1+u (u^3->u->u^3)` | `{'-1': 24}` |
| 7 | 4 | 12 | u^3->u->u^3 | `1 <- 1+u^2 (u^3->u->u^3)` | `{'-1': 12}` |
| 8 | 4 | 8 | u^3->u^2->u^3 | `1 <- 1 (u^3->u^2->u^3)` | `{'-1': 8}` |
| 9 | 8 | 16 | u^3->u^2->u^3 | `1 <- 1+u (u^3->u^2->u^3)` | `{'-1': 16}` |
| 10 | 4 | 8 | u^3->u^2->u^3 | `1 <- 1+u^2 (u^3->u^2->u^3)` | `{'-1': 8}` |

## Closed Cells

- H3: 42 cells / 3 orbits
- H4: 301 cells / 12 orbits

### H3 Orbit Table

| orbit | size | family | representative |
|---:|---:|---|---|
| 0 | 24 | 233 | `(1, 1+u, u)` |
| 1 | 12 | 133 | `(1, 1+u^2, u^2)` |
| 2 | 6 | 122 | `(u, u+u^2, u^2)` |

### H4 Orbit Table

| orbit | size | family | representative |
|---:|---:|---|---|
| 0 | 4 | 3333 | `(1, 1, 1, 1)` |
| 1 | 24 | 3333 | `(1, 1, 1+u, 1+u)` |
| 2 | 12 | 3333 | `(1, 1, 1+u^2, 1+u^2)` |
| 3 | 48 | 2233 | `(1, 1, u, u)` |
| 4 | 24 | 1133 | `(1, 1, u^2, u^2)` |
| 5 | 24 | 3333 | `(1, 1+u, 1+u+u^2, 1+u^2)` |
| 6 | 96 | 1233 | `(1, 1+u, u+u^2, u^2)` |
| 7 | 48 | 2233 | `(1, 1+u^2, u, u+u^2)` |
| 8 | 2 | 2222 | `(u, u, u, u)` |
| 9 | 6 | 2222 | `(u, u, u+u^2, u+u^2)` |
| 10 | 12 | 1122 | `(u, u, u^2, u^2)` |
| 11 | 1 | 1111 | `(u^2, u^2, u^2, u^2)` |

## Fisher Probe

- modes: u^2 and u
- supports: order0 6, left1 7, right1 6, mixed2 6

## Full-Block Coboundary Diagnostic

- coefficient field: Q
- C1 generators: 177
- C2 dimension: 1709
- coboundary rank: 176
- residual quotient dimension: 1533
- raw support: 100
- residual support: 100
- residual equals raw cochain: True
- raw is coboundary: False
- rational rank certified: True
- rational non-coboundary certified: True

## Support-Projection Coboundary Diagnostic

- mode: support
- C2 scope: raw_support
- coefficient field: Q
- C1 generators: 49
- C2 dimension: 100
- coboundary rank: 36
- residual quotient dimension: 64
- raw support: 100
- residual support: 0
- residual equals raw cochain: False
- raw is coboundary in projection: True
