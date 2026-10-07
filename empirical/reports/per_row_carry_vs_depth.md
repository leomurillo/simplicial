# Per-row (†_p) verification: carry-vs-depth on the mixed atlas

Verifies the hypothesis (†_p) of Paper 12 Theorem 9.2.1 on the mixed local atlas: F_2[u]/(u^n) for n in {2,3,4,5} (residue degree 1, sweeping wild depth), F_4[u]/(u^2) and F_4[u]/(u^3) (residue degree 2), F_8[u]/(u^2) (residue degree 3), and F_16[u]/(u^2) (residue degree 4).

For each row R and each Fourier-pure test displacement h supported in one conductor packet, the verifier:

- builds h via inverse DFT of the packet-indicator;
- forms ĥ_n = DFT(h^n) for n = 1, ..., n_max (n_max controls the carry-series truncation);
- for each shallow PSL flag M' of depth d < d*, sums the operator-valued carry Σ_n ‖Carry_n^{tgt,src}‖_F^2 over consecutive-packet boundaries the shallow flag fails to cover;
- reports λ_crit(h, M') = total_carry_sq / (d* − d), and the per-row break-even λ_PSL_crit = min over (h, M').

(†_p) is the inequality `total_carry_sq > λ_PSL · (d* − d)` for every shallow (h, M').  It is satisfied for every λ_PSL < λ_PSL_crit(R).

## Summary

| Row | |R| | conductor_order | d_max | λ_PSL_crit | (†_p) holds |
|---|---:|---|---:|---:|---|
| F_2[u]/(u^2) | 4 | u ⊂ u^2 | 2 | 2.125 | yes |
| F_2[u]/(u^3) | 8 | u ⊂ u^2 ⊂ u^3 | 3 | 2.00781 | yes |
| F_2[u]/(u^4) | 16 | u ⊂ u^2 ⊂ u^3 ⊂ u^4 | 4 | 2.00049 | yes |
| F_2[u]/(u^5) | 32 | u ⊂ u^2 ⊂ u^3 ⊂ u^4 ⊂ u^5 | 5 | 2.00003 | yes |
| F_4[u]/(u^2) | 16 | u ⊂ u^2 | 2 | 55.4062 | yes |
| F_4[u]/(u^3) | 64 | u ⊂ u^2 ⊂ u^3 | 3 | 36.5903 | yes |
| F_8[u]/(u^2) | 64 | u ⊂ u^2 | 2 | 924.038 | yes |
| F_16[u]/(u^2) | 256 | u ⊂ u^2 | 2 | 10950 | yes |

## F_2[u]/(u^2)

- ring: `F_2[u]/(u^2)`, |R| = 4
- conductor_order: u ⊂ u^2, d_max = 2
- packet sizes: |X_u| = 1, |X_u^2| = 2
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2)
- **row λ_PSL_crit = 2.125**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 1

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 2

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2) | 4.25 | 2.125 |
| 1 | 1 | (u↔u^2) | 4.25 | 4.25 |

## F_2[u]/(u^3)

- ring: `F_2[u]/(u^3)`, |R| = 8
- conductor_order: u ⊂ u^2 ⊂ u^3, d_max = 3
- packet sizes: |X_u| = 1, |X_u^2| = 2, |X_u^3| = 4
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2), (u^2 ↔ u^3)
- **row λ_PSL_crit = 2.00781**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 1

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2), (u^2↔u^3) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 2

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2), (u^2↔u^3) | 4.01562 | 2.00781 |
| 1 | 1 | (u↔u^2), (u^2↔u^3) | 4.01562 | 4.01562 |

### Test displacement: Fourier-pure on packet `u^3` (d* = 3)

- ĥ total energy on nontrivial characters: 4

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 3 | (u↔u^2), (u^2↔u^3) | 18.0625 | 6.02083 |
| 1 | 2 | (u↔u^2), (u^2↔u^3) | 18.0625 | 9.03125 |
| 2 | 1 | (u^2↔u^3) | 17 | 17 |

## F_2[u]/(u^4)

- ring: `F_2[u]/(u^4)`, |R| = 16
- conductor_order: u ⊂ u^2 ⊂ u^3 ⊂ u^4, d_max = 4
- packet sizes: |X_u| = 1, |X_u^2| = 2, |X_u^3| = 4, |X_u^4| = 8
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2), (u^2 ↔ u^3), (u^3 ↔ u^4)
- **row λ_PSL_crit = 2.00049**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 1

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 2

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 4.00098 | 2.00049 |
| 1 | 1 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 4.00098 | 4.00098 |

### Test displacement: Fourier-pure on packet `u^3` (d* = 3)

- ĥ total energy on nontrivial characters: 4

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 3 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 16.3135 | 5.43783 |
| 1 | 2 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 16.3135 | 8.15674 |
| 2 | 1 | (u^2↔u^3), (u^3↔u^4) | 16.0625 | 16.0625 |

### Test displacement: Fourier-pure on packet `u^4` (d* = 4)

- ĥ total energy on nontrivial characters: 8

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 4 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 73.3125 | 18.3281 |
| 1 | 3 | (u↔u^2), (u^2↔u^3), (u^3↔u^4) | 73.3125 | 24.4375 |
| 2 | 2 | (u^2↔u^3), (u^3↔u^4) | 72.25 | 36.125 |
| 3 | 1 | (u^3↔u^4) | 68 | 68 |

## F_2[u]/(u^5)

- ring: `F_2[u]/(u^5)`, |R| = 32
- conductor_order: u ⊂ u^2 ⊂ u^3 ⊂ u^4 ⊂ u^5, d_max = 5
- packet sizes: |X_u| = 1, |X_u^2| = 2, |X_u^3| = 4, |X_u^4| = 8, |X_u^5| = 16
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2), (u^2 ↔ u^3), (u^3 ↔ u^4), (u^4 ↔ u^5)
- **row λ_PSL_crit = 2.00003**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 1

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 2

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 4.00006 | 2.00003 |
| 1 | 1 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 4.00006 | 4.00006 |

### Test displacement: Fourier-pure on packet `u^3` (d* = 3)

- ĥ total energy on nontrivial characters: 4

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 3 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 16.0664 | 5.35547 |
| 1 | 2 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 16.0664 | 8.03321 |
| 2 | 1 | (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 16.0039 | 16.0039 |

### Test displacement: Fourier-pure on packet `u^4` (d* = 4)

- ĥ total energy on nontrivial characters: 8

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 4 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 65.5049 | 16.3762 |
| 1 | 3 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 65.5049 | 21.835 |
| 2 | 2 | (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 65.2539 | 32.627 |
| 3 | 1 | (u^3↔u^4), (u^4↔u^5) | 64.25 | 64.25 |

### Test displacement: Fourier-pure on packet `u^5` (d* = 5)

- ĥ total energy on nontrivial characters: 16

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 5 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 294.312 | 58.8625 |
| 1 | 4 | (u↔u^2), (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 294.312 | 73.5781 |
| 2 | 3 | (u^2↔u^3), (u^3↔u^4), (u^4↔u^5) | 293.25 | 97.75 |
| 3 | 2 | (u^3↔u^4), (u^4↔u^5) | 289 | 144.5 |
| 4 | 1 | (u^4↔u^5) | 272 | 272 |

## F_4[u]/(u^2)

- ring: `F_4[u]/(u^2)`, |R| = 16
- conductor_order: u ⊂ u^2, d_max = 2
- packet sizes: |X_u| = 3, |X_u^2| = 12
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2)
- **row λ_PSL_crit = 55.4062**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 3

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 12

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2) | 110.812 | 55.4062 |
| 1 | 1 | (u↔u^2) | 110.812 | 110.812 |

## F_4[u]/(u^3)

- ring: `F_4[u]/(u^3)`, |R| = 64
- conductor_order: u ⊂ u^2 ⊂ u^3, d_max = 3
- packet sizes: |X_u| = 3, |X_u^2| = 12, |X_u^3| = 48
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2), (u^2 ↔ u^3)
- **row λ_PSL_crit = 36.5903**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 3

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2), (u^2↔u^3) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 12

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2), (u^2↔u^3) | 73.1805 | 36.5903 |
| 1 | 1 | (u↔u^2), (u^2↔u^3) | 73.1805 | 73.1805 |

### Test displacement: Fourier-pure on packet `u^3` (d* = 3)

- ĥ total energy on nontrivial characters: 48

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 3 | (u↔u^2), (u^2↔u^3) | 1831.38 | 610.459 |
| 1 | 2 | (u↔u^2), (u^2↔u^3) | 1831.38 | 915.688 |
| 2 | 1 | (u^2↔u^3) | 1773 | 1773 |

## F_8[u]/(u^2)

- ring: `F_8[u]/(u^2)`, |R| = 64
- conductor_order: u ⊂ u^2, d_max = 2
- packet sizes: |X_u| = 7, |X_u^2| = 56
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2)
- **row λ_PSL_crit = 924.038**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 7

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 56

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2) | 1848.08 | 924.038 |
| 1 | 1 | (u↔u^2) | 1848.08 | 1848.08 |

## F_16[u]/(u^2)

- ring: `F_16[u]/(u^2)`, |R| = 256
- conductor_order: u ⊂ u^2, d_max = 2
- packet sizes: |X_u| = 15, |X_u^2| = 240
- carry-series truncation n_max = 4
- adjacent PSL boundaries: (u ↔ u^2)
- **row λ_PSL_crit = 10950**
- (†_p) holds: **True**

### Test displacement: Fourier-pure on packet `u` (d* = 1)

- ĥ total energy on nontrivial characters: 15

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 1 | (u↔u^2) | 0 | 0 |

### Test displacement: Fourier-pure on packet `u^2` (d* = 2)

- ĥ total energy on nontrivial characters: 240

| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |
|---:|---:|---|---:|---:|
| 0 | 2 | (u↔u^2) | 21899.9 | 10950 |
| 1 | 1 | (u↔u^2) | 21899.9 | 21899.9 |

