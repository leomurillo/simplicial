# Audit lambda settlement record -- (alpha, eps) V/M packet signature on months

**Binning script version:** `audit_lambda_VM_binning_v0.1_2026_05_20`
**Pre-registered protocol:** Paper 37 §4 (5×6 grid); v2insert-06 §2 P11.
**Three-outcome rule (v2insert-04 §3.1):** K / L / joint-on-disjoint.

## V/M definitions on Z/12 (v2insert-05 §1; v2insert-06 §2)

- V analog = H_2 + H_3 + H_4 (single-prime / prime-power axes)
- M analog = H_6 + H_12 (cross-prime carry)
- rho_VM = sigma_V / sigma_M  (logit packet fractions, seed mean)

## Paper 12 anchor (Paper 37 §6 F2 falsifier)

| width | (alpha=1, eps=0) test loss mean (sd) | per-seed | in band [3.5, 4.5]? |
|---:|---|---|---:|
| 16 | 3.0993 (0.2583) | [2.902764333685, 3.391804896089, 3.003362677696] | no |
| 32 | 4.0514 (0.1172) | [4.072962055519, 4.156298652266, 3.924890378454] | yes |
| 64 | 5.7104 (0.4517) | [5.21053207858, 5.831304378042, 6.08941951674] | no |

Reference: Paper 12 §7.4.1 reports (alpha=1, eps=0, W=32) -> 4.0514 (mean over three seeds 9101/9102/9103).

## Plain-Adam corner (alpha=0, eps=0) reference

| width | (alpha=0, eps=0) test loss mean (sd) |
|---:|---|
| 16 | 4.1200 (0.0205) |
| 32 | 6.1250 (0.6962) |
| 64 | 9.0838 (0.5972) |

Reference: Paper 12 §7.4.1 reports (alpha=0, eps=0, W=32) -> 6.125 and W=64 -> 9.0838.

## Width 16

### G_IID(alpha, eps) (seed mean)

| alpha\eps | 0.00 | 0.03 | 0.06 | 0.10 | 0.15 | 0.20 |
|---:|---:|---:|---:|---:|---:|---:|
|0.00|4.120|4.048|3.993|3.906|3.783|3.659|
|0.25|3.507|3.475|3.440|3.391|3.320|3.240|
|0.50|3.400|3.371|3.341|3.301|3.249|3.191|
|0.75|3.289|3.249|3.210|3.160|3.105|3.058|
|1.00|3.099|3.058|3.024|2.993|2.935|2.876|

### rho_VM(alpha, eps) (seed mean)

| alpha\eps | 0.00 | 0.03 | 0.06 | 0.10 | 0.15 | 0.20 |
|---:|---:|---:|---:|---:|---:|---:|
|0.00|0.8730|0.8716|0.8708|0.8589|0.8331|0.8032|
|0.25|0.0869|0.0874|0.0881|0.0893|0.0916|0.0951|
|0.50|0.0532|0.0539|0.0548|0.0562|0.0584|0.0612|
|0.75|0.0209|0.0216|0.0222|0.0231|0.0248|0.0272|
|1.00|0.0000|0.0000|0.0000|0.0000|0.0000|0.0000|

- median seed SD of rho_VM across (alpha, eps) cells (where finite): `0.0183`

### Iso-loss band analysis

- G_IID range: [2.8760, 4.1200]

| band | G range | n configs | rho_VM mean | rho_VM range (min, max) | alpha range in band |
|---|---|---:|---:|---|---|
| low | [2.876, 3.287] | 14 | 0.0238 | (0.0000, 0.0951) | alpha=[0.25, 1.00] |
| mid | [3.287, 3.709] | 11 | 0.1350 | (0.0209, 0.8032) | alpha=[0.00, 0.75] |
| high | [3.709, 4.120] | 5 | 0.8615 | (0.8331, 0.8730) | alpha=[0.00, 0.00] |

### Monotonicity slices (does rho_VM track alpha at fixed eps?)

| eps | (rho at alpha=0) | (rho at alpha=1) | sign of d(rho)/d(alpha) cumulative | strictly monotone in alpha? |
|---:|---:|---:|---:|:---:|
| 0.00 | 0.8730 | 0.0000 | decreasing | yes-dec |
| 0.03 | 0.8716 | 0.0000 | decreasing | yes-dec |
| 0.06 | 0.8708 | 0.0000 | decreasing | yes-dec |
| 0.10 | 0.8589 | 0.0000 | decreasing | yes-dec |
| 0.15 | 0.8331 | 0.0000 | decreasing | yes-dec |
| 0.20 | 0.8032 | 0.0000 | decreasing | yes-dec |

## Width 32

### G_IID(alpha, eps) (seed mean)

| alpha\eps | 0.00 | 0.03 | 0.06 | 0.10 | 0.15 | 0.20 |
|---:|---:|---:|---:|---:|---:|---:|
|0.00|6.125|5.907|5.672|5.390|5.049|4.743|
|0.25|4.243|4.152|4.051|3.921|3.744|3.614|
|0.50|4.180|4.076|3.975|3.853|3.685|3.541|
|0.75|4.133|4.024|3.917|3.765|3.591|3.445|
|1.00|4.051|3.951|3.850|3.698|3.539|3.360|

### rho_VM(alpha, eps) (seed mean)

| alpha\eps | 0.00 | 0.03 | 0.06 | 0.10 | 0.15 | 0.20 |
|---:|---:|---:|---:|---:|---:|---:|
|0.00|0.7301|0.7342|0.7391|0.7287|0.6910|0.6390|
|0.25|0.0520|0.0547|0.0586|0.0636|0.0699|0.0813|
|0.50|0.0342|0.0364|0.0388|0.0419|0.0463|0.0505|
|0.75|0.0147|0.0162|0.0178|0.0199|0.0222|0.0251|
|1.00|0.0000|0.0000|0.0000|0.0000|0.0000|0.0000|

- median seed SD of rho_VM across (alpha, eps) cells (where finite): `0.0062`

### Iso-loss band analysis

- G_IID range: [3.3600, 6.1250]

| band | G range | n configs | rho_VM mean | rho_VM range (min, max) | alpha range in band |
|---|---|---:|---:|---|---|
| low | [3.360, 4.272] | 24 | 0.0310 | (0.0000, 0.0813) | alpha=[0.25, 1.00] |
| mid | [4.272, 5.213] | 2 | 0.6650 | (0.6390, 0.6910) | alpha=[0.00, 0.00] |
| high | [5.213, 6.125] | 4 | 0.7330 | (0.7287, 0.7391) | alpha=[0.00, 0.00] |

### Monotonicity slices (does rho_VM track alpha at fixed eps?)

| eps | (rho at alpha=0) | (rho at alpha=1) | sign of d(rho)/d(alpha) cumulative | strictly monotone in alpha? |
|---:|---:|---:|---:|:---:|
| 0.00 | 0.7301 | 0.0000 | decreasing | yes-dec |
| 0.03 | 0.7342 | 0.0000 | decreasing | yes-dec |
| 0.06 | 0.7391 | 0.0000 | decreasing | yes-dec |
| 0.10 | 0.7287 | 0.0000 | decreasing | yes-dec |
| 0.15 | 0.6910 | 0.0000 | decreasing | yes-dec |
| 0.20 | 0.6390 | 0.0000 | decreasing | yes-dec |

## Width 64

### G_IID(alpha, eps) (seed mean)

| alpha\eps | 0.00 | 0.03 | 0.06 | 0.10 | 0.15 | 0.20 |
|---:|---:|---:|---:|---:|---:|---:|
|0.00|9.084|8.341|7.618|6.561|5.584|5.176|
|0.25|7.070|6.647|6.250|5.792|5.250|4.796|
|0.50|6.624|6.230|5.827|5.503|5.016|4.798|
|0.75|6.299|6.007|5.623|5.196|4.769|4.456|
|1.00|5.710|5.470|5.237|4.916|4.543|4.268|

### rho_VM(alpha, eps) (seed mean)

| alpha\eps | 0.00 | 0.03 | 0.06 | 0.10 | 0.15 | 0.20 |
|---:|---:|---:|---:|---:|---:|---:|
|0.00|0.6470|0.6529|0.6619|0.6503|0.6859|0.7000|
|0.25|0.0585|0.0783|0.1014|0.1362|0.1650|0.1970|
|0.50|0.0263|0.0308|0.0377|0.0511|0.0719|0.0996|
|0.75|0.0116|0.0131|0.0155|0.0180|0.0227|0.0296|
|1.00|0.0000|0.0000|0.0000|0.0000|0.0000|0.0000|

- median seed SD of rho_VM across (alpha, eps) cells (where finite): `0.0065`

### Iso-loss band analysis

- G_IID range: [4.2678, 9.0838]

| band | G range | n configs | rho_VM mean | rho_VM range (min, max) | alpha range in band |
|---|---|---:|---:|---|---|
| low | [4.268, 5.857] | 19 | 0.1174 | (0.0000, 0.7000) | alpha=[0.00, 1.00] |
| mid | [5.857, 7.495] | 8 | 0.1213 | (0.0116, 0.6503) | alpha=[0.00, 0.75] |
| high | [7.495, 9.084] | 3 | 0.6539 | (0.6470, 0.6619) | alpha=[0.00, 0.00] |

### Monotonicity slices (does rho_VM track alpha at fixed eps?)

| eps | (rho at alpha=0) | (rho at alpha=1) | sign of d(rho)/d(alpha) cumulative | strictly monotone in alpha? |
|---:|---:|---:|---:|:---:|
| 0.00 | 0.6470 | 0.0000 | decreasing | yes-dec |
| 0.03 | 0.6529 | 0.0000 | decreasing | yes-dec |
| 0.06 | 0.6619 | 0.0000 | decreasing | yes-dec |
| 0.10 | 0.6503 | 0.0000 | decreasing | yes-dec |
| 0.15 | 0.6859 | 0.0000 | decreasing | yes-dec |
| 0.20 | 0.7000 | 0.0000 | decreasing | yes-dec |

## P11 branch classification (heuristic)

**Method (Paper 37 §9.7 V/M-tracks-ridge diagnostic, simplified):**
Per width, compute the seed-noise scale = median per-cell SD of rho_VM.
Compute the signal scale = max(rho_VM mean) - min(rho_VM mean) over the grid.
Classify:
  * If signal/noise > 2 AND rho_VM is monotone in alpha at each fixed eps -> K-branch.
  * If signal/noise < 1 -> L-branch (iso-packet within seed noise).
  * Otherwise -> joint-on-disjoint or ambiguous (record range).

| width | seed-noise scale (SD of rho) | signal scale (range of rho) | signal/noise | monotone? | provisional branch |
|---:|---:|---:|---:|:---:|---|
| 16 | 0.0183 | 0.8730 | 47.73 | yes | K |
| 32 | 0.0062 | 0.7391 | 118.88 | yes | K |
| 64 | 0.0065 | 0.7000 | 107.22 | yes | K |

## Settlement (P11)

**P11 realized branch:** K-branch realized (rho_VM monotone in alpha at every eps slice, signal exceeds seed noise by >2x).

Notes:
- This classification is heuristic; the per-width tables above carry the raw data.
- At alpha=1 with S={12}, the projector forces all nontrivial logit energy into H_12 ⊂ M, so sigma_V = 0 and rho_VM = 0 by construction. This is not a deflated signal -- it is the alpha=1 boundary of the V/M ratio.
- A monotone decrease of rho_VM with alpha along any fixed-eps row is the K-branch prediction direction (alpha-mechanism injects M-content; the V share shrinks).
