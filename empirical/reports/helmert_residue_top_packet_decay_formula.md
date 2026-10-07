# Helmert Residue Top Packet Decay Formula

This report verifies Theorem 3.12 of Paper 25: the closed-form
top-coupling branch of the top-packet first-order frame price for
F_q[u]/(u^k) with q = 2^r, r >= 2.  The branch formula is

    mu*^top_{F,k}(alpha) = 2 rho^2 |(F-1)rho - F(F-2)|
                          / (F^k * (1 + rho(F-1))^2 (1 - rho)^2),

with rho = 0.95 * alpha.  On this branch, the maximizing plane connects
packet u^{k-1} to the top packet u^k.  At higher amplitudes and k >= 3,
the full coordinate-plane envelope can instead be controlled by the
largest non-top/non-top plane.

## Config

- `amplitudes`: `[0.1, 0.35, 0.5]`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`
- `F_values`: `[2, 4, 8, 16, 32]`
- `k_values_per_F`: `{2: [2, 3, 4, 5, 6, 7, 8], 4: [2, 3, 4, 5, 6], 8: [2, 3, 4], 16: [2, 3], 32: [2]}`

## Verification table (predicted vs atlas)

Rows where the atlas has a measurement are marked with the relative error
between predicted and measured mu*; unsupported rows have only the
extrapolated prediction.

| F | k | amp | envelope mu* | top branch | non-top branch | winner | atlas mu* | rel err | F^k * mu* |
|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 2 | 2 | 0.1 | 0.0004365 | 0.0004365 | 0.0000000 | top-f2 | 0.0004365 | 2.63e-05 | 0.001746 |
| 2 | 2 | 0.35 | 0.0232331 | 0.0232331 | 0.0000000 | top-f2 | 0.0232333 | 7.35e-06 | 0.092933 |
| 2 | 2 | 0.5 | 0.0893610 | 0.0893610 | 0.0000000 | top-f2 | 0.0893615 | 5.03e-06 | 0.357444 |
| 2 | 3 | 0.1 | 0.0003274 | 0.0003274 | 0.0000104 | top-f2 | 0.0003274 | 1.22e-05 | 0.002619 |
| 2 | 3 | 0.35 | 0.0174249 | 0.0174249 | 0.0019313 | top-f2 | 0.0174249 | 3.34e-06 | 0.139399 |
| 2 | 3 | 0.5 | 0.0670208 | 0.0670208 | 0.0106116 | top-f2 | 0.0670209 | 2.22e-06 | 0.536166 |
| 2 | 4 | 0.1 | 0.0001910 | 0.0001910 | 0.0000078 | top-f2 | 0.0001910 | 8.17e-06 | 0.003056 |
| 2 | 4 | 0.35 | 0.0101645 | 0.0101645 | 0.0014484 | top-f2 | 0.0101645 | 2.20e-06 | 0.162632 |
| 2 | 4 | 0.5 | 0.0390955 | 0.0390955 | 0.0079587 | top-f2 | 0.0390955 | 1.42e-06 | 0.625527 |
| 2 | 5 | 0.1 | 0.0001023 | 0.0001023 | 0.0000045 | top-f2 | 0.0001023 | 6.67e-06 | 0.003274 |
| 2 | 5 | 0.35 | 0.0054453 | 0.0054453 | 0.0008449 | top-f2 | 0.0054453 | 1.73e-06 | 0.174249 |
| 2 | 5 | 0.5 | 0.0209440 | 0.0209440 | 0.0046426 | top-f2 | 0.0209440 | 1.10e-06 | 0.670208 |
| 2 | 6 | 0.1 | 0.0000529 | 0.0000529 | 0.0000024 | top-f2 | -- | -- | 0.003383 |
| 2 | 6 | 0.35 | 0.0028134 | 0.0028134 | 0.0004526 | top-f2 | -- | -- | 0.180057 |
| 2 | 6 | 0.5 | 0.0108211 | 0.0108211 | 0.0024871 | top-f2 | -- | -- | 0.692548 |
| 2 | 7 | 0.1 | 0.0000269 | 0.0000269 | 0.0000013 | top-f2 | -- | -- | 0.003438 |
| 2 | 7 | 0.35 | 0.0014294 | 0.0014294 | 0.0002339 | top-f2 | -- | -- | 0.182961 |
| 2 | 7 | 0.5 | 0.0054978 | 0.0054978 | 0.0012850 | top-f2 | -- | -- | 0.703718 |
| 2 | 8 | 0.1 | 0.0000135 | 0.0000135 | 0.0000006 | top-f2 | -- | -- | 0.003465 |
| 2 | 8 | 0.35 | 0.0007204 | 0.0007204 | 0.0001188 | top-f2 | -- | -- | 0.184413 |
| 2 | 8 | 0.5 | 0.0027707 | 0.0027707 | 0.0006529 | top-f2 | -- | -- | 0.709303 |
| 4 | 2 | 0.1 | 0.0064356 | 0.0064356 | 0.0000000 | top | 0.0064356 | 5.57e-07 | 0.102970 |
| 4 | 2 | 0.35 | 0.0544340 | 0.0544340 | 0.0000000 | top | 0.0544340 | 2.88e-07 | 0.870944 |
| 4 | 2 | 0.5 | 0.1144066 | 0.1144066 | 0.0000000 | top | 0.1144065 | 8.72e-08 | 1.830505 |
| 4 | 3 | 0.1 | 0.0016089 | 0.0016089 | 0.0000381 | top | 0.0016089 | 4.47e-07 | 0.102970 |
| 4 | 3 | 0.35 | 0.0136085 | 0.0136085 | 0.0043508 | top | 0.0136085 | 7.47e-08 | 0.870944 |
| 4 | 3 | 0.5 | 0.0286016 | 0.0286016 | 0.0198750 | top | 0.0286016 | 4.32e-07 | 1.830505 |
| 4 | 4 | 0.1 | 0.0004022 | 0.0004022 | 0.0000119 | top | -- | -- | 0.102970 |
| 4 | 4 | 0.35 | 0.0034021 | 0.0034021 | 0.0013596 | top | -- | -- | 0.870944 |
| 4 | 4 | 0.5 | 0.0071504 | 0.0071504 | 0.0062109 | top | -- | -- | 1.830505 |
| 4 | 5 | 0.1 | 0.0001006 | 0.0001006 | 0.0000031 | top | -- | -- | 0.102970 |
| 4 | 5 | 0.35 | 0.0008505 | 0.0008505 | 0.0003569 | top | -- | -- | 0.870944 |
| 4 | 5 | 0.5 | 0.0017876 | 0.0017876 | 0.0016304 | top | -- | -- | 1.830505 |
| 4 | 6 | 0.1 | 0.0000251 | 0.0000251 | 0.0000008 | top | -- | -- | 0.102970 |
| 4 | 6 | 0.35 | 0.0002126 | 0.0002126 | 0.0000903 | top | -- | -- | 0.870944 |
| 4 | 6 | 0.5 | 0.0004469 | 0.0004469 | 0.0004124 | top | -- | -- | 1.830505 |
| 8 | 2 | 0.1 | 0.0058797 | 0.0058797 | 0.0000000 | top | 0.0058797 | 1.19e-07 | 0.376300 |
| 8 | 2 | 0.35 | 0.0319852 | 0.0319852 | 0.0000000 | top | 0.0319852 | 5.84e-07 | 2.047055 |
| 8 | 2 | 0.5 | 0.0610957 | 0.0610957 | 0.0000000 | top | 0.0610957 | 1.42e-06 | 3.910128 |
| 8 | 3 | 0.1 | 0.0007350 | 0.0007350 | 0.0000421 | top | -- | -- | 0.376300 |
| 8 | 3 | 0.35 | 0.0039982 | 0.0039982 | 0.0029046 | top | -- | -- | 2.047055 |
| 8 | 3 | 0.5 | 0.0115757 | 0.0076370 | 0.0115757 | non-top | -- | -- | 5.926739 |
| 8 | 4 | 0.1 | 0.0000919 | 0.0000919 | 0.0000059 | top | -- | -- | 0.376300 |
| 8 | 4 | 0.35 | 0.0004998 | 0.0004998 | 0.0004085 | top | -- | -- | 2.047055 |
| 8 | 4 | 0.5 | 0.0016278 | 0.0009546 | 0.0016278 | non-top | -- | -- | 6.667581 |
| 16 | 2 | 0.1 | 0.0032583 | 0.0032583 | 0.0000000 | top | -- | -- | 0.834128 |
| 16 | 2 | 0.35 | 0.0118426 | 0.0118426 | 0.0000000 | top | -- | -- | 3.031717 |
| 16 | 2 | 0.5 | 0.0210098 | 0.0210098 | 0.0000000 | top | -- | -- | 5.378502 |
| 16 | 3 | 0.1 | 0.0002036 | 0.0002036 | 0.0000261 | top | -- | -- | 0.834128 |
| 16 | 3 | 0.35 | 0.0011822 | 0.0007402 | 0.0011822 | non-top | -- | -- | 4.842259 |
| 16 | 3 | 0.5 | 0.0043224 | 0.0013131 | 0.0043224 | non-top | -- | -- | 17.704519 |
| 32 | 2 | 0.1 | 0.0013235 | 0.0013235 | 0.0000000 | top | -- | -- | 1.355261 |
| 32 | 2 | 0.35 | 0.0035997 | 0.0035997 | 0.0000000 | top | -- | -- | 3.686044 |
| 32 | 2 | 0.5 | 0.0061119 | 0.0061119 | 0.0000000 | top | -- | -- | 6.258575 |

## Residue-degree profile at k=2, amp=0.35

This shows the non-monotone residue-degree peak at F=4 explicitly.
F^k mu* is monotone increasing in F (and bounded by 2/(1-rho)^2 as
F -> infinity), but mu* itself decays as F^{-k}, so the product peaks
at finite F.

| F | k | predicted mu* | F^k * mu* |
|---:|---:|---:|---:|
| 2 | 2 | 0.0232331 | 0.092933 |
| 4 | 2 | 0.0544340 | 0.870944 |
| 8 | 2 | 0.0319852 | 2.047055 |
| 16 | 2 | 0.0118426 | 3.031717 |
| 32 | 2 | 0.0035997 | 3.686044 |
| 64 | 2 | 0.0009928 | 4.066432 |
| 128 | 2 | 0.0002607 | 4.272012 |

## Reading

Theorem 3.12 supplies a closed form for the diagonal mu*^top in the F_q
wild tower (q = 2^r, r >= 2).  Two structural features distinguish it
from the F=2 case (Theorem 3.11):

1. On the low-amplitude/top-coupling branch, the maximizing plane connects
   u^{k-1} (highest non-top packet) to u^k (top packet), not u to u^k as
   in F=2.  This is because the F^{k-1}(F-2) term in the descent rate is
   zero for F=2 but nonzero for F>2.
2. On that branch, F^k mu*^top is *exactly* constant in k for F>2.  For
   F=2, only an asymptotic limit holds (with leading (2^{k-1}-1) factor).
3. Above the amplitude threshold, the envelope switches to a non-top
   branch connecting u to u^{k-1}.  The default paper amplitudes
   0.1, 0.35, and 0.5 remain on the top-coupling branch for the
   supported F>2 rows.

The residue-degree profile at fixed k peaks at finite F (here F=4 for
k=2 and amp=0.35), reconciling the apparent non-monotonicity that
Computation 3.9 flagged as the next open question.
