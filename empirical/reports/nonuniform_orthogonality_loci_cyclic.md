# Cyclic Nonuniform Fisher-Conductor Orthogonality Loci

## Criterion

Let `m_p = 1/p`.  In additive-character coordinates,

```text
g_p(chi, psi) = hat(m_p)(psi chi^{-1}).
```

Therefore two conductor packets remain Fisher-orthogonal at a
nonuniform point exactly when `hat(m_p)` vanishes on every quotient
`psi chi^{-1}` connecting the two packets.  Equivalently, the allowed
reciprocal Fourier modes are those that preserve conductor labels on
all nontrivial character lines.

The actual probability locus is nonlinear: choose a positive reciprocal
density `m` supported only on allowed modes, then normalize
`p_x = (1/m_x) / sum_y (1/m_y)`.

## Cyclic Atlas

| group | conductors | allowed reciprocal modes | reading |
|---|---|---|---|
| C_2 | 2 | 0, 1 | prime/single-packet: block orthogonality is vacuous |
| C_3 | 3 | 0, 1, 2 | prime/single-packet: block orthogonality is vacuous |
| C_4 | 2, 4 | 0, 2 | structured locus: nonconstant reciprocal modes remain |
| C_5 | 5 | 0, 1, 2, 3, 4 | prime/single-packet: block orthogonality is vacuous |
| C_6 | 2, 3, 6 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_7 | 7 | 0, 1, 2, 3, 4, 5, 6 | prime/single-packet: block orthogonality is vacuous |
| C_8 | 2, 4, 8 | 0, 4 | structured locus: nonconstant reciprocal modes remain |
| C_9 | 3, 9 | 0, 3, 6 | structured locus: nonconstant reciprocal modes remain |
| C_10 | 2, 5, 10 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_11 | 11 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | prime/single-packet: block orthogonality is vacuous |
| C_12 | 2, 3, 4, 6, 12 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_13 | 13 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | prime/single-packet: block orthogonality is vacuous |
| C_14 | 2, 7, 14 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_15 | 3, 5, 15 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_16 | 2, 4, 8, 16 | 0, 8 | structured locus: nonconstant reciprocal modes remain |
| C_17 | 17 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | prime/single-packet: block orthogonality is vacuous |
| C_18 | 2, 3, 6, 9, 18 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_19 | 19 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 | prime/single-packet: block orthogonality is vacuous |
| C_20 | 2, 4, 5, 10, 20 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_21 | 3, 7, 21 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_22 | 2, 11, 22 | 0 | rigid: only constant reciprocal density preserves all blocks |
| C_23 | 23 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 | prime/single-packet: block orthogonality is vacuous |
| C_24 | 2, 3, 4, 6, 8, 12, 24 | 0 | rigid: only constant reciprocal density preserves all blocks |

## First Bad Witnesses

For each disallowed reciprocal mode `r`, the witness `k -> k+r` shows
a conductor-changing character translation.

### C_4

| mode r | witness |
|---:|---|
| 1 | 1 cond 4 -> 2 cond 2 |
| 3 | 2 cond 2 -> 1 cond 4 |

### C_6

| mode r | witness |
|---:|---|
| 1 | 1 cond 6 -> 2 cond 3 |
| 2 | 1 cond 6 -> 3 cond 2 |
| 3 | 1 cond 6 -> 4 cond 3 |
| 4 | 3 cond 2 -> 1 cond 6 |
| 5 | 2 cond 3 -> 1 cond 6 |

### C_8

| mode r | witness |
|---:|---|
| 1 | 1 cond 8 -> 2 cond 4 |
| 2 | 2 cond 4 -> 4 cond 2 |
| 3 | 1 cond 8 -> 4 cond 2 |
| 5 | 1 cond 8 -> 6 cond 4 |
| 6 | 4 cond 2 -> 2 cond 4 |
| 7 | 2 cond 4 -> 1 cond 8 |

### C_9

| mode r | witness |
|---:|---|
| 1 | 2 cond 9 -> 3 cond 3 |
| 2 | 1 cond 9 -> 3 cond 3 |
| 4 | 2 cond 9 -> 6 cond 3 |
| 5 | 1 cond 9 -> 6 cond 3 |
| 7 | 3 cond 3 -> 1 cond 9 |
| 8 | 3 cond 3 -> 2 cond 9 |

### C_10

| mode r | witness |
|---:|---|
| 1 | 1 cond 10 -> 2 cond 5 |
| 2 | 3 cond 10 -> 5 cond 2 |
| 3 | 1 cond 10 -> 4 cond 5 |
| 4 | 1 cond 10 -> 5 cond 2 |
| 5 | 1 cond 10 -> 6 cond 5 |
| 6 | 5 cond 2 -> 1 cond 10 |
| 7 | 1 cond 10 -> 8 cond 5 |
| 8 | 5 cond 2 -> 3 cond 10 |
| 9 | 2 cond 5 -> 1 cond 10 |

### C_12

| mode r | witness |
|---:|---|
| 1 | 1 cond 12 -> 2 cond 6 |
| 2 | 1 cond 12 -> 3 cond 4 |
| 3 | 1 cond 12 -> 4 cond 3 |
| 4 | 2 cond 6 -> 6 cond 2 |
| 5 | 1 cond 12 -> 6 cond 2 |
| 6 | 2 cond 6 -> 8 cond 3 |
| 7 | 1 cond 12 -> 8 cond 3 |
| 8 | 1 cond 12 -> 9 cond 4 |
| 9 | 1 cond 12 -> 10 cond 6 |
| 10 | 3 cond 4 -> 1 cond 12 |
| 11 | 2 cond 6 -> 1 cond 12 |

### C_14

| mode r | witness |
|---:|---|
| 1 | 1 cond 14 -> 2 cond 7 |
| 2 | 5 cond 14 -> 7 cond 2 |
| 3 | 1 cond 14 -> 4 cond 7 |
| 4 | 3 cond 14 -> 7 cond 2 |
| 5 | 1 cond 14 -> 6 cond 7 |
| 6 | 1 cond 14 -> 7 cond 2 |
| 7 | 1 cond 14 -> 8 cond 7 |
| 8 | 7 cond 2 -> 1 cond 14 |
| 9 | 1 cond 14 -> 10 cond 7 |
| 10 | 7 cond 2 -> 3 cond 14 |
| 11 | 1 cond 14 -> 12 cond 7 |
| 12 | 7 cond 2 -> 5 cond 14 |
| 13 | 2 cond 7 -> 1 cond 14 |

### C_15

| mode r | witness |
|---:|---|
| 1 | 2 cond 15 -> 3 cond 5 |
| 2 | 1 cond 15 -> 3 cond 5 |
| 3 | 2 cond 15 -> 5 cond 3 |
| 4 | 1 cond 15 -> 5 cond 3 |
| 5 | 1 cond 15 -> 6 cond 5 |
| 6 | 4 cond 15 -> 10 cond 3 |
| 7 | 2 cond 15 -> 9 cond 5 |
| 8 | 1 cond 15 -> 9 cond 5 |
| 9 | 1 cond 15 -> 10 cond 3 |
| 10 | 2 cond 15 -> 12 cond 5 |
| 11 | 1 cond 15 -> 12 cond 5 |
| 12 | 5 cond 3 -> 2 cond 15 |
| 13 | 3 cond 5 -> 1 cond 15 |
| 14 | 3 cond 5 -> 2 cond 15 |

### C_16

| mode r | witness |
|---:|---|
| 1 | 1 cond 16 -> 2 cond 8 |
| 2 | 2 cond 8 -> 4 cond 4 |
| 3 | 1 cond 16 -> 4 cond 4 |
| 4 | 4 cond 4 -> 8 cond 2 |
| 5 | 1 cond 16 -> 6 cond 8 |
| 6 | 2 cond 8 -> 8 cond 2 |
| 7 | 1 cond 16 -> 8 cond 2 |
| 9 | 1 cond 16 -> 10 cond 8 |
| 10 | 2 cond 8 -> 12 cond 4 |
| 11 | 1 cond 16 -> 12 cond 4 |
| 12 | 8 cond 2 -> 4 cond 4 |
| 13 | 1 cond 16 -> 14 cond 8 |
| 14 | 4 cond 4 -> 2 cond 8 |
| 15 | 2 cond 8 -> 1 cond 16 |

### C_18

| mode r | witness |
|---:|---|
| 1 | 1 cond 18 -> 2 cond 9 |
| 2 | 1 cond 18 -> 3 cond 6 |
| 3 | 1 cond 18 -> 4 cond 9 |
| 4 | 2 cond 9 -> 6 cond 3 |
| 5 | 1 cond 18 -> 6 cond 3 |
| 6 | 3 cond 6 -> 9 cond 2 |
| 7 | 1 cond 18 -> 8 cond 9 |
| 8 | 1 cond 18 -> 9 cond 2 |
| 9 | 1 cond 18 -> 10 cond 9 |
| 10 | 2 cond 9 -> 12 cond 3 |
| 11 | 1 cond 18 -> 12 cond 3 |
| 12 | 9 cond 2 -> 3 cond 6 |
| 13 | 1 cond 18 -> 14 cond 9 |
| 14 | 1 cond 18 -> 15 cond 6 |
| 15 | 1 cond 18 -> 16 cond 9 |
| 16 | 3 cond 6 -> 1 cond 18 |
| 17 | 2 cond 9 -> 1 cond 18 |

### C_20

| mode r | witness |
|---:|---|
| 1 | 1 cond 20 -> 2 cond 10 |
| 2 | 2 cond 10 -> 4 cond 5 |
| 3 | 1 cond 20 -> 4 cond 5 |
| 4 | 1 cond 20 -> 5 cond 4 |
| 5 | 1 cond 20 -> 6 cond 10 |
| 6 | 2 cond 10 -> 8 cond 5 |
| 7 | 1 cond 20 -> 8 cond 5 |
| 8 | 2 cond 10 -> 10 cond 2 |
| 9 | 1 cond 20 -> 10 cond 2 |
| 10 | 2 cond 10 -> 12 cond 5 |
| 11 | 1 cond 20 -> 12 cond 5 |
| 12 | 3 cond 20 -> 15 cond 4 |
| 13 | 1 cond 20 -> 14 cond 10 |
| 14 | 1 cond 20 -> 15 cond 4 |
| 15 | 1 cond 20 -> 16 cond 5 |
| 16 | 5 cond 4 -> 1 cond 20 |
| 17 | 1 cond 20 -> 18 cond 10 |
| 18 | 4 cond 5 -> 2 cond 10 |
| 19 | 2 cond 10 -> 1 cond 20 |

### C_21

| mode r | witness |
|---:|---|
| 1 | 2 cond 21 -> 3 cond 7 |
| 2 | 1 cond 21 -> 3 cond 7 |
| 3 | 4 cond 21 -> 7 cond 3 |
| 4 | 2 cond 21 -> 6 cond 7 |
| 5 | 1 cond 21 -> 6 cond 7 |
| 6 | 1 cond 21 -> 7 cond 3 |
| 7 | 2 cond 21 -> 9 cond 7 |
| 8 | 1 cond 21 -> 9 cond 7 |
| 9 | 5 cond 21 -> 14 cond 3 |
| 10 | 2 cond 21 -> 12 cond 7 |
| 11 | 1 cond 21 -> 12 cond 7 |
| 12 | 2 cond 21 -> 14 cond 3 |
| 13 | 1 cond 21 -> 14 cond 3 |
| 14 | 1 cond 21 -> 15 cond 7 |
| 15 | 7 cond 3 -> 1 cond 21 |
| 16 | 2 cond 21 -> 18 cond 7 |
| 17 | 1 cond 21 -> 18 cond 7 |
| 18 | 7 cond 3 -> 4 cond 21 |
| 19 | 3 cond 7 -> 1 cond 21 |
| 20 | 3 cond 7 -> 2 cond 21 |

### C_22

| mode r | witness |
|---:|---|
| 1 | 1 cond 22 -> 2 cond 11 |
| 2 | 9 cond 22 -> 11 cond 2 |
| 3 | 1 cond 22 -> 4 cond 11 |
| 4 | 7 cond 22 -> 11 cond 2 |
| 5 | 1 cond 22 -> 6 cond 11 |
| 6 | 5 cond 22 -> 11 cond 2 |
| 7 | 1 cond 22 -> 8 cond 11 |
| 8 | 3 cond 22 -> 11 cond 2 |
| 9 | 1 cond 22 -> 10 cond 11 |
| 10 | 1 cond 22 -> 11 cond 2 |
| 11 | 1 cond 22 -> 12 cond 11 |
| 12 | 11 cond 2 -> 1 cond 22 |
| 13 | 1 cond 22 -> 14 cond 11 |
| 14 | 11 cond 2 -> 3 cond 22 |
| 15 | 1 cond 22 -> 16 cond 11 |
| 16 | 11 cond 2 -> 5 cond 22 |
| 17 | 1 cond 22 -> 18 cond 11 |
| 18 | 11 cond 2 -> 7 cond 22 |
| 19 | 1 cond 22 -> 20 cond 11 |
| 20 | 11 cond 2 -> 9 cond 22 |
| 21 | 2 cond 11 -> 1 cond 22 |

### C_24

| mode r | witness |
|---:|---|
| 1 | 1 cond 24 -> 2 cond 12 |
| 2 | 1 cond 24 -> 3 cond 8 |
| 3 | 1 cond 24 -> 4 cond 6 |
| 4 | 2 cond 12 -> 6 cond 4 |
| 5 | 1 cond 24 -> 6 cond 4 |
| 6 | 2 cond 12 -> 8 cond 3 |
| 7 | 1 cond 24 -> 8 cond 3 |
| 8 | 1 cond 24 -> 9 cond 8 |
| 9 | 1 cond 24 -> 10 cond 12 |
| 10 | 2 cond 12 -> 12 cond 2 |
| 11 | 1 cond 24 -> 12 cond 2 |
| 12 | 4 cond 6 -> 16 cond 3 |
| 13 | 1 cond 24 -> 14 cond 12 |
| 14 | 1 cond 24 -> 15 cond 8 |
| 15 | 1 cond 24 -> 16 cond 3 |
| 16 | 2 cond 12 -> 18 cond 4 |
| 17 | 1 cond 24 -> 18 cond 4 |
| 18 | 2 cond 12 -> 20 cond 6 |
| 19 | 1 cond 24 -> 20 cond 6 |
| 20 | 1 cond 24 -> 21 cond 8 |
| 21 | 1 cond 24 -> 22 cond 12 |
| 22 | 3 cond 8 -> 1 cond 24 |
| 23 | 2 cond 12 -> 1 cond 24 |

