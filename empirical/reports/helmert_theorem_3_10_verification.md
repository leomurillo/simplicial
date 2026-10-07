# Theorem 3.10 Numerical Verification

This script verifies the structural content of Theorem 3.10 of Paper 25
across the F_2[u]/(u^k) wild tower for k = 2, ..., 5.

For each (target packet u^s, amplitude alpha), we compare:

1. **Within-prefix Fisher Gram equality** (Lemma 3.10.C(i)):
   max |G_h^{R_k}[V_{<=s}] - G_h^{R_s}| should be 0 (machine precision).
2. **Cross-prefix Fisher Gram vanishing** (Lemma 3.10.C(ii)):
   max |G_h^{R_k}[V_{<=s}, V_{>s}]| should be 0 (machine precision).
3. **mu* invariance** (Theorem 3.10):
   |mu*_{R_k} - mu*_{R_s}| should be 0 (machine precision).

## Config

- `amplitudes`: `[0.1, 0.35, 0.5]`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`

## Verification table

| target packet | amp | reference row | reference mu* | max within-prefix diff | max cross-prefix entry | max mu* diff |
|---|---:|---|---:|---:|---:|---:|
| u^2 | 0.1 | F_2[u]/(u^2) | 0.000436543 | 2.220e-16 | 3.335e-17 | 6.939e-12 |
| u^2 | 0.35 | F_2[u]/(u^2) | 0.0232333 | 2.220e-16 | 9.507e-17 | 1.388e-11 |
| u^2 | 0.5 | F_2[u]/(u^2) | 0.0893615 | 4.441e-16 | 4.717e-17 | 5.551e-11 |
| u^3 | 0.1 | F_2[u]/(u^3) | 0.000327403 | 2.220e-16 | 3.609e-17 | 0.000e+00 |
| u^3 | 0.35 | F_2[u]/(u^3) | 0.0174249 | 2.220e-16 | 7.773e-17 | 5.551e-11 |
| u^3 | 0.5 | F_2[u]/(u^3) | 0.0670209 | 2.220e-16 | 1.942e-17 | 5.551e-11 |
| u^4 | 0.1 | F_2[u]/(u^4) | 0.000190984 | 2.220e-16 | 3.609e-17 | 1.388e-11 |
| u^4 | 0.35 | F_2[u]/(u^4) | 0.0101645 | 2.220e-16 | 9.160e-17 | 5.551e-11 |
| u^4 | 0.5 | F_2[u]/(u^4) | 0.0390955 | 4.163e-17 | 1.248e-17 | 5.551e-11 |

## Per-embedding details

### Target u^2 at amp=0.1

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | F_2[u]/(u^3) | 7 | 3 | 2.220e-16 | 3.335e-17 | 0.000436543 | 6.939e-12 |
| 4 | F_2[u]/(u^4) | 15 | 3 | 5.551e-17 | 0.000e+00 | 0.000436543 | 0.000e+00 |
| 5 | F_2[u]/(u^5) | 31 | 3 | 5.551e-17 | 2.221e-17 | 0.000436543 | 3.469e-12 |

### Target u^2 at amp=0.35

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | F_2[u]/(u^3) | 7 | 3 | 2.220e-16 | 4.723e-17 | 0.0232333 | 0.000e+00 |
| 4 | F_2[u]/(u^4) | 15 | 3 | 2.776e-17 | 0.000e+00 | 0.0232333 | 1.388e-11 |
| 5 | F_2[u]/(u^5) | 31 | 3 | 2.220e-16 | 9.507e-17 | 0.0232333 | 0.000e+00 |

### Target u^2 at amp=0.5

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | F_2[u]/(u^3) | 7 | 3 | 2.220e-16 | 1.947e-17 | 0.0893615 | 5.551e-11 |
| 4 | F_2[u]/(u^4) | 15 | 3 | 1.110e-16 | 0.000e+00 | 0.0893615 | 0.000e+00 |
| 5 | F_2[u]/(u^5) | 31 | 3 | 4.441e-16 | 4.717e-17 | 0.0893615 | 2.776e-11 |

### Target u^3 at amp=0.1

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 4 | F_2[u]/(u^4) | 15 | 7 | 2.220e-16 | 0.000e+00 | 0.000327403 | 0.000e+00 |
| 5 | F_2[u]/(u^5) | 31 | 7 | 2.776e-17 | 3.609e-17 | 0.000327403 | 0.000e+00 |

### Target u^3 at amp=0.35

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 4 | F_2[u]/(u^4) | 15 | 7 | 2.220e-16 | 0.000e+00 | 0.0174249 | 0.000e+00 |
| 5 | F_2[u]/(u^5) | 31 | 7 | 5.551e-17 | 7.773e-17 | 0.0174249 | 5.551e-11 |

### Target u^3 at amp=0.5

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 4 | F_2[u]/(u^4) | 15 | 7 | 2.220e-16 | 0.000e+00 | 0.0670209 | 5.551e-11 |
| 5 | F_2[u]/(u^5) | 31 | 7 | 5.551e-17 | 1.942e-17 | 0.0670209 | 5.551e-11 |

### Target u^4 at amp=0.1

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 5 | F_2[u]/(u^5) | 31 | 15 | 2.220e-16 | 3.609e-17 | 0.000190984 | 1.388e-11 |

### Target u^4 at amp=0.35

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 5 | F_2[u]/(u^5) | 31 | 15 | 2.220e-16 | 9.160e-17 | 0.0101645 | 5.551e-11 |

### Target u^4 at amp=0.5

| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |
|---:|---|---:|---:|---:|---:|---:|---:|
| 5 | F_2[u]/(u^5) | 31 | 15 | 4.163e-17 | 1.248e-17 | 0.0390955 | 5.551e-11 |

## Pass criterion

Theorem 3.10 is verified if all within-prefix diffs, cross-prefix
entries, and mu* differences are at floating-point noise levels
(< 1e-10).  See `helmert_theorem_3_10_verification.json` for full
precision.
