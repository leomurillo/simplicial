# Local Nonuniform Fisher-Conductor Orthogonality Loci

## Criterion

For a nonuniform categorical point `p`, set `m_p = 1/p`.  A fixed
conductor-packet splitting remains mutually Fisher-orthogonal exactly
when `hat(m_p)` is supported only on reciprocal modes `eta` whose
translation action preserves conductor labels on all nontrivial
character labels.

This report enumerates those allowed reciprocal modes for local rows
already supported by the quotient-character adjacency constructor.

## Atlas

| key | ring | packets | allowed reciprocal modes | normalizer orbits | reading |
|---|---|---|---|---:|---|
| f4-u2 | F_4[u]/(u^2) | u:3, u^2:12 | 0, u, wu, (w+1)u | 2 | structured locus: nonconstant reciprocal modes remain |
| f16 | F_16 | field:15 | 0, 1, a, 1+a, a^2, 1+a^2, a+a^2, 1+a+a^2, a^3, 1+a^3, a+a^3, 1+a+a^3, a^2+a^3, 1+a^2+a^3, a+a^2+a^3, 1+a+a^2+a^3 | 2 | single-packet: block orthogonality is vacuous |
| f2-u4 | F_2[u]/(u^4) | u:1, u^2:2, u^3:4, u^4:8 | 0, u^3 | 2 | structured locus: nonconstant reciprocal modes remain |
| f2-u5 | F_2[u]/(u^5) | u:1, u^2:2, u^3:4, u^4:8, u^5:16 | 0, u^4 | 2 | structured locus: nonconstant reciprocal modes remain |
| f4-u3 | F_4[u]/(u^3) | u:3, u^2:12, u^3:48 | 0, u^2, w*u^2, (1+w)*u^2 | 2 | structured locus: nonconstant reciprocal modes remain |
| f8-u2 | F_8[u]/(u^2) | u:7, u^2:56 | 0, u, b*u, (1+b)*u, b^2*u, (1+b^2)*u, (b+b^2)*u, (1+b+b^2)*u | 2 | structured locus: nonconstant reciprocal modes remain |

## Allowed-Mode Normalizer Orbits

### f4-u2

| representative | size | members |
|---|---:|---|
| (w+1)u | 3 | (w+1)u, u, wu |
| 0 | 1 | 0 |

### f16

| representative | size | members |
|---|---:|---|
| 0 | 1 | 0 |
| 1 | 15 | 1, 1+a, 1+a+a^2, 1+a+a^2+a^3, 1+a+a^3, 1+a^2, 1+a^2+a^3, 1+a^3, a, a+a^2, a+a^2+a^3, a+a^3, a^2, a^2+a^3, a^3 |

### f2-u4

| representative | size | members |
|---|---:|---|
| 0 | 1 | 0 |
| u^3 | 1 | u^3 |

### f2-u5

| representative | size | members |
|---|---:|---|
| 0 | 1 | 0 |
| u^4 | 1 | u^4 |

### f4-u3

| representative | size | members |
|---|---:|---|
| (1+w)*u^2 | 3 | (1+w)*u^2, u^2, w*u^2 |
| 0 | 1 | 0 |

### f8-u2

| representative | size | members |
|---|---:|---|
| (1+b)*u | 7 | (1+b)*u, (1+b+b^2)*u, (1+b^2)*u, (b+b^2)*u, b*u, b^2*u, u |
| 0 | 1 | 0 |


## First Bad Witnesses

Each witness shows a reciprocal mode `eta` translating one nontrivial
character label into a different conductor packet.

### f4-u2

| eta | witness |
|---|---|
| 1 | u (u) -> 1+u (u^2) |
| 1+(w+1)u | u (u) -> 1+wu (u^2) |
| 1+u | u (u) -> 1 (u^2) |
| 1+wu | u (u) -> 1+(w+1)u (u^2) |
| w | u (u) -> w+u (u^2) |
| w+(w+1)u | u (u) -> w+wu (u^2) |
| w+1 | u (u) -> w+1+u (u^2) |
| w+1+(w+1)u | u (u) -> w+1+wu (u^2) |
| w+1+u | u (u) -> w+1 (u^2) |
| w+1+wu | u (u) -> w+1+(w+1)u (u^2) |
| w+u | u (u) -> w (u^2) |
| w+wu | u (u) -> w+(w+1)u (u^2) |

### f2-u4

| eta | witness |
|---|---|
| 1 | u (u^3) -> 1+u (u^4) |
| 1+u | 1 (u^4) -> u (u^3) |
| 1+u+u^2 | 1 (u^4) -> u+u^2 (u^3) |
| 1+u+u^2+u^3 | 1 (u^4) -> u+u^2+u^3 (u^3) |
| 1+u+u^3 | 1 (u^4) -> u+u^3 (u^3) |
| 1+u^2 | 1 (u^4) -> u^2 (u^2) |
| 1+u^2+u^3 | 1 (u^4) -> u^2+u^3 (u^2) |
| 1+u^3 | 1 (u^4) -> u^3 (u) |
| u | u^2 (u^2) -> u+u^2 (u^3) |
| u+u^2 | u (u^3) -> u^2 (u^2) |
| u+u^2+u^3 | u (u^3) -> u^2+u^3 (u^2) |
| u+u^3 | u (u^3) -> u^3 (u) |
| u^2 | u^3 (u) -> u^2+u^3 (u^2) |
| u^2+u^3 | u^2 (u^2) -> u^3 (u) |

### f2-u5

| eta | witness |
|---|---|
| 1 | u^4 (u) -> 1+u^4 (u^5) |
| 1+u | u^4 (u) -> 1+u+u^4 (u^5) |
| 1+u+u^2 | u^4 (u) -> 1+u+u^2+u^4 (u^5) |
| 1+u+u^2+u^3 | u^4 (u) -> 1+u+u^2+u^3+u^4 (u^5) |
| 1+u+u^2+u^3+u^4 | u^4 (u) -> 1+u+u^2+u^3 (u^5) |
| 1+u+u^2+u^4 | u^4 (u) -> 1+u+u^2 (u^5) |
| 1+u+u^3 | u^4 (u) -> 1+u+u^3+u^4 (u^5) |
| 1+u+u^3+u^4 | u^4 (u) -> 1+u+u^3 (u^5) |
| 1+u+u^4 | u^4 (u) -> 1+u (u^5) |
| 1+u^2 | u^4 (u) -> 1+u^2+u^4 (u^5) |
| 1+u^2+u^3 | u^4 (u) -> 1+u^2+u^3+u^4 (u^5) |
| 1+u^2+u^3+u^4 | u^4 (u) -> 1+u^2+u^3 (u^5) |
| 1+u^2+u^4 | u^4 (u) -> 1+u^2 (u^5) |
| 1+u^3 | u^4 (u) -> 1+u^3+u^4 (u^5) |
| 1+u^3+u^4 | u^4 (u) -> 1+u^3 (u^5) |
| 1+u^4 | u^4 (u) -> 1 (u^5) |
| u | u^4 (u) -> u+u^4 (u^4) |
| u+u^2 | u^4 (u) -> u+u^2+u^4 (u^4) |
| u+u^2+u^3 | u^4 (u) -> u+u^2+u^3+u^4 (u^4) |
| u+u^2+u^3+u^4 | u^4 (u) -> u+u^2+u^3 (u^4) |
| u+u^2+u^4 | u^4 (u) -> u+u^2 (u^4) |
| u+u^3 | u^4 (u) -> u+u^3+u^4 (u^4) |
| u+u^3+u^4 | u^4 (u) -> u+u^3 (u^4) |
| u+u^4 | u^4 (u) -> u (u^4) |
| u^2 | u^4 (u) -> u^2+u^4 (u^3) |
| u^2+u^3 | u^4 (u) -> u^2+u^3+u^4 (u^3) |
| u^2+u^3+u^4 | u^4 (u) -> u^2+u^3 (u^3) |
| u^2+u^4 | u^4 (u) -> u^2 (u^3) |
| u^3 | u^4 (u) -> u^3+u^4 (u^2) |
| u^3+u^4 | u^4 (u) -> u^3 (u^2) |

### f4-u3

| eta | witness |
|---|---|
| (1+w)*u | u^2 (u) -> (1+w)*u+u^2 (u^2) |
| (1+w)*u+(1+w)*u^2 | u^2 (u) -> (1+w)*u+w*u^2 (u^2) |
| (1+w)*u+u^2 | u^2 (u) -> (1+w)*u (u^2) |
| (1+w)*u+w*u^2 | u^2 (u) -> (1+w)*u+(1+w)*u^2 (u^2) |
| 1 | u^2 (u) -> 1+u^2 (u^3) |
| 1+(1+w)*u | u^2 (u) -> 1+(1+w)*u+u^2 (u^3) |
| 1+(1+w)*u+(1+w)*u^2 | u^2 (u) -> 1+(1+w)*u+w*u^2 (u^3) |
| 1+(1+w)*u+u^2 | u^2 (u) -> 1+(1+w)*u (u^3) |
| 1+(1+w)*u+w*u^2 | u^2 (u) -> 1+(1+w)*u+(1+w)*u^2 (u^3) |
| 1+(1+w)*u^2 | u^2 (u) -> 1+w*u^2 (u^3) |
| 1+u | u^2 (u) -> 1+u+u^2 (u^3) |
| 1+u+(1+w)*u^2 | u^2 (u) -> 1+u+w*u^2 (u^3) |
| 1+u+u^2 | u^2 (u) -> 1+u (u^3) |
| 1+u+w*u^2 | u^2 (u) -> 1+u+(1+w)*u^2 (u^3) |
| 1+u^2 | u^2 (u) -> 1 (u^3) |
| 1+w | u^2 (u) -> 1+w+u^2 (u^3) |
| 1+w*u | u^2 (u) -> 1+w*u+u^2 (u^3) |
| 1+w*u+(1+w)*u^2 | u^2 (u) -> 1+w*u+w*u^2 (u^3) |
| 1+w*u+u^2 | u^2 (u) -> 1+w*u (u^3) |
| 1+w*u+w*u^2 | u^2 (u) -> 1+w*u+(1+w)*u^2 (u^3) |
| 1+w*u^2 | u^2 (u) -> 1+(1+w)*u^2 (u^3) |
| 1+w+(1+w)*u | u^2 (u) -> 1+w+(1+w)*u+u^2 (u^3) |
| 1+w+(1+w)*u+(1+w)*u^2 | u^2 (u) -> 1+w+(1+w)*u+w*u^2 (u^3) |
| 1+w+(1+w)*u+u^2 | u^2 (u) -> 1+w+(1+w)*u (u^3) |
| 1+w+(1+w)*u+w*u^2 | u^2 (u) -> 1+w+(1+w)*u+(1+w)*u^2 (u^3) |
| 1+w+(1+w)*u^2 | u^2 (u) -> 1+w+w*u^2 (u^3) |
| 1+w+u | u^2 (u) -> 1+w+u+u^2 (u^3) |
| 1+w+u+(1+w)*u^2 | u^2 (u) -> 1+w+u+w*u^2 (u^3) |
| 1+w+u+u^2 | u^2 (u) -> 1+w+u (u^3) |
| 1+w+u+w*u^2 | u^2 (u) -> 1+w+u+(1+w)*u^2 (u^3) |
| 1+w+u^2 | u^2 (u) -> 1+w (u^3) |
| 1+w+w*u | u^2 (u) -> 1+w+w*u+u^2 (u^3) |
| 1+w+w*u+(1+w)*u^2 | u^2 (u) -> 1+w+w*u+w*u^2 (u^3) |
| 1+w+w*u+u^2 | u^2 (u) -> 1+w+w*u (u^3) |
| 1+w+w*u+w*u^2 | u^2 (u) -> 1+w+w*u+(1+w)*u^2 (u^3) |
| 1+w+w*u^2 | u^2 (u) -> 1+w+(1+w)*u^2 (u^3) |
| u | u^2 (u) -> u+u^2 (u^2) |
| u+(1+w)*u^2 | u^2 (u) -> u+w*u^2 (u^2) |
| u+u^2 | u^2 (u) -> u (u^2) |
| u+w*u^2 | u^2 (u) -> u+(1+w)*u^2 (u^2) |
| w | u^2 (u) -> w+u^2 (u^3) |
| w*u | u^2 (u) -> w*u+u^2 (u^2) |
| w*u+(1+w)*u^2 | u^2 (u) -> w*u+w*u^2 (u^2) |
| w*u+u^2 | u^2 (u) -> w*u (u^2) |
| w*u+w*u^2 | u^2 (u) -> w*u+(1+w)*u^2 (u^2) |
| w+(1+w)*u | u^2 (u) -> w+(1+w)*u+u^2 (u^3) |
| w+(1+w)*u+(1+w)*u^2 | u^2 (u) -> w+(1+w)*u+w*u^2 (u^3) |
| w+(1+w)*u+u^2 | u^2 (u) -> w+(1+w)*u (u^3) |
| w+(1+w)*u+w*u^2 | u^2 (u) -> w+(1+w)*u+(1+w)*u^2 (u^3) |
| w+(1+w)*u^2 | u^2 (u) -> w+w*u^2 (u^3) |
| w+u | u^2 (u) -> w+u+u^2 (u^3) |
| w+u+(1+w)*u^2 | u^2 (u) -> w+u+w*u^2 (u^3) |
| w+u+u^2 | u^2 (u) -> w+u (u^3) |
| w+u+w*u^2 | u^2 (u) -> w+u+(1+w)*u^2 (u^3) |
| w+u^2 | u^2 (u) -> w (u^3) |
| w+w*u | u^2 (u) -> w+w*u+u^2 (u^3) |
| w+w*u+(1+w)*u^2 | u^2 (u) -> w+w*u+w*u^2 (u^3) |
| w+w*u+u^2 | u^2 (u) -> w+w*u (u^3) |
| w+w*u+w*u^2 | u^2 (u) -> w+w*u+(1+w)*u^2 (u^3) |
| w+w*u^2 | u^2 (u) -> w+(1+w)*u^2 (u^3) |

### f8-u2

| eta | witness |
|---|---|
| 1 | u (u) -> 1+u (u^2) |
| 1+(1+b)*u | u (u) -> 1+b*u (u^2) |
| 1+(1+b+b^2)*u | u (u) -> 1+(b+b^2)*u (u^2) |
| 1+(1+b^2)*u | u (u) -> 1+b^2*u (u^2) |
| 1+(b+b^2)*u | u (u) -> 1+(1+b+b^2)*u (u^2) |
| 1+b | u (u) -> 1+b+u (u^2) |
| 1+b*u | u (u) -> 1+(1+b)*u (u^2) |
| 1+b+(1+b)*u | u (u) -> 1+b+b*u (u^2) |
| 1+b+(1+b+b^2)*u | u (u) -> 1+b+(b+b^2)*u (u^2) |
| 1+b+(1+b^2)*u | u (u) -> 1+b+b^2*u (u^2) |
| 1+b+(b+b^2)*u | u (u) -> 1+b+(1+b+b^2)*u (u^2) |
| 1+b+b*u | u (u) -> 1+b+(1+b)*u (u^2) |
| 1+b+b^2 | u (u) -> 1+b+b^2+u (u^2) |
| 1+b+b^2*u | u (u) -> 1+b+(1+b^2)*u (u^2) |
| 1+b+b^2+(1+b)*u | u (u) -> 1+b+b^2+b*u (u^2) |
| 1+b+b^2+(1+b+b^2)*u | u (u) -> 1+b+b^2+(b+b^2)*u (u^2) |
| 1+b+b^2+(1+b^2)*u | u (u) -> 1+b+b^2+b^2*u (u^2) |
| 1+b+b^2+(b+b^2)*u | u (u) -> 1+b+b^2+(1+b+b^2)*u (u^2) |
| 1+b+b^2+b*u | u (u) -> 1+b+b^2+(1+b)*u (u^2) |
| 1+b+b^2+b^2*u | u (u) -> 1+b+b^2+(1+b^2)*u (u^2) |
| 1+b+b^2+u | u (u) -> 1+b+b^2 (u^2) |
| 1+b+u | u (u) -> 1+b (u^2) |
| 1+b^2 | u (u) -> 1+b^2+u (u^2) |
| 1+b^2*u | u (u) -> 1+(1+b^2)*u (u^2) |
| 1+b^2+(1+b)*u | u (u) -> 1+b^2+b*u (u^2) |
| 1+b^2+(1+b+b^2)*u | u (u) -> 1+b^2+(b+b^2)*u (u^2) |
| 1+b^2+(1+b^2)*u | u (u) -> 1+b^2+b^2*u (u^2) |
| 1+b^2+(b+b^2)*u | u (u) -> 1+b^2+(1+b+b^2)*u (u^2) |
| 1+b^2+b*u | u (u) -> 1+b^2+(1+b)*u (u^2) |
| 1+b^2+b^2*u | u (u) -> 1+b^2+(1+b^2)*u (u^2) |
| 1+b^2+u | u (u) -> 1+b^2 (u^2) |
| 1+u | u (u) -> 1 (u^2) |
| b | u (u) -> b+u (u^2) |
| b+(1+b)*u | u (u) -> b+b*u (u^2) |
| b+(1+b+b^2)*u | u (u) -> b+(b+b^2)*u (u^2) |
| b+(1+b^2)*u | u (u) -> b+b^2*u (u^2) |
| b+(b+b^2)*u | u (u) -> b+(1+b+b^2)*u (u^2) |
| b+b*u | u (u) -> b+(1+b)*u (u^2) |
| b+b^2 | u (u) -> b+b^2+u (u^2) |
| b+b^2*u | u (u) -> b+(1+b^2)*u (u^2) |
| b+b^2+(1+b)*u | u (u) -> b+b^2+b*u (u^2) |
| b+b^2+(1+b+b^2)*u | u (u) -> b+b^2+(b+b^2)*u (u^2) |
| b+b^2+(1+b^2)*u | u (u) -> b+b^2+b^2*u (u^2) |
| b+b^2+(b+b^2)*u | u (u) -> b+b^2+(1+b+b^2)*u (u^2) |
| b+b^2+b*u | u (u) -> b+b^2+(1+b)*u (u^2) |
| b+b^2+b^2*u | u (u) -> b+b^2+(1+b^2)*u (u^2) |
| b+b^2+u | u (u) -> b+b^2 (u^2) |
| b+u | u (u) -> b (u^2) |
| b^2 | u (u) -> b^2+u (u^2) |
| b^2+(1+b)*u | u (u) -> b^2+b*u (u^2) |
| b^2+(1+b+b^2)*u | u (u) -> b^2+(b+b^2)*u (u^2) |
| b^2+(1+b^2)*u | u (u) -> b^2+b^2*u (u^2) |
| b^2+(b+b^2)*u | u (u) -> b^2+(1+b+b^2)*u (u^2) |
| b^2+b*u | u (u) -> b^2+(1+b)*u (u^2) |
| b^2+b^2*u | u (u) -> b^2+(1+b^2)*u (u^2) |
| b^2+u | u (u) -> b^2 (u^2) |

