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

- `amplitudes`: `[0.65, 0.75, 0.9]`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`
- `F_values`: `[2, 4, 8, 16, 32]`
- `k_values_per_F`: `{2: [2, 3, 4, 5, 6, 7, 8], 4: [2, 3, 4, 5, 6], 8: [2, 3, 4], 16: [2, 3], 32: [2]}`

## Verification table (predicted vs atlas)

Rows where the atlas has a measurement are marked with the relative error
between predicted and measured mu*; unsupported rows have only the
extrapolated prediction.

| F | k | amp | envelope mu* | top branch | non-top branch | winner | atlas mu* | rel err | F^k * mu* |
|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 2 | 2 | 0.65 | 0.3075597 | 0.3075597 | 0.0000000 | top-f2 | 0.3075609 | 3.74e-06 | 1.230239 |
| 2 | 2 | 0.75 | 0.7460840 | 0.7460840 | 0.0000000 | top-f2 | 0.7460864 | 3.15e-06 | 2.984336 |
| 2 | 2 | 0.9 | 4.3196098 | 4.3196098 | 0.0000000 | top-f2 | 4.3196206 | 2.50e-06 | 17.278439 |
| 2 | 3 | 0.65 | 0.2306698 | 0.2306698 | 0.0474795 | top-f2 | 0.2306701 | 1.58e-06 | 1.845358 |
| 2 | 3 | 0.75 | 0.5595630 | 0.5595630 | 0.1328962 | top-f2 | 0.5595637 | 1.28e-06 | 4.476504 |
| 2 | 3 | 0.9 | 3.2397073 | 3.2397073 | 0.9233166 | top-f2 | 3.2397104 | 9.37e-07 | 25.917659 |
| 2 | 4 | 0.65 | 0.1345574 | 0.1345574 | 0.0356096 | top-f2 | 0.1345575 | 9.63e-07 | 2.152918 |
| 2 | 4 | 0.75 | 0.3264118 | 0.3264118 | 0.0996722 | top-f2 | 0.3264120 | 7.47e-07 | 5.222588 |
| 2 | 4 | 0.9 | 1.8898293 | 1.8898293 | 0.6924874 | top-f2 | 1.8898302 | 4.92e-07 | 30.237268 |
| 2 | 5 | 0.65 | 0.0720843 | 0.0720843 | 0.0207723 | top-f2 | 0.0720844 | 7.16e-07 | 2.306698 |
| 2 | 5 | 0.75 | 0.1748634 | 0.1748634 | 0.0581421 | top-f2 | 0.1748635 | 5.33e-07 | 5.595630 |
| 2 | 5 | 0.9 | 1.0124085 | 1.0124085 | 0.4039510 | top-f2 | 1.0124089 | 3.16e-07 | 32.397073 |
| 2 | 6 | 0.65 | 0.0372436 | 0.0372436 | 0.0111280 | top-f2 | -- | -- | 2.383588 |
| 2 | 6 | 0.75 | 0.0903461 | 0.0903461 | 0.0311476 | top-f2 | -- | -- | 5.782151 |
| 2 | 6 | 0.9 | 0.5230777 | 0.5230777 | 0.2164023 | top-f2 | -- | -- | 33.476976 |
| 2 | 7 | 0.65 | 0.0189221 | 0.0189221 | 0.0057495 | top-f2 | -- | -- | 2.422033 |
| 2 | 7 | 0.75 | 0.0459017 | 0.0459017 | 0.0160929 | top-f2 | -- | -- | 5.875412 |
| 2 | 7 | 0.9 | 0.2657572 | 0.2657572 | 0.1118079 | top-f2 | -- | -- | 34.016927 |
| 2 | 8 | 0.65 | 0.0095362 | 0.0095362 | 0.0029211 | top-f2 | -- | -- | 2.441255 |
| 2 | 8 | 0.75 | 0.0231330 | 0.0231330 | 0.0081762 | top-f2 | -- | -- | 5.922042 |
| 2 | 8 | 0.9 | 0.1339332 | 0.1339332 | 0.0568056 | top-f2 | -- | -- | 34.286903 |
| 4 | 2 | 0.65 | 0.2461321 | 0.2461321 | 0.0000000 | top | 0.2461320 | 6.63e-07 | 3.938114 |
| 4 | 2 | 0.75 | 0.4572139 | 0.4572139 | 0.0000000 | top | 0.4572134 | 1.18e-06 | 7.315423 |
| 4 | 2 | 0.9 | 1.8586034 | 1.8586034 | 0.0000000 | top | 1.8585993 | 2.20e-06 | 29.737654 |
| 4 | 3 | 0.65 | 0.0772874 | 0.0615330 | 0.0772874 | non-top | 0.0772874 | 2.23e-07 | 4.946394 |
| 4 | 3 | 0.75 | 0.2004340 | 0.1143035 | 0.2004340 | non-top | 0.2004340 | 2.22e-07 | 12.827775 |
| 4 | 3 | 0.9 | 1.2655649 | 0.4646508 | 1.2655649 | non-top | 1.2655652 | 2.24e-07 | 80.996156 |
| 4 | 4 | 0.65 | 0.0241523 | 0.0153833 | 0.0241523 | non-top | -- | -- | 6.182992 |
| 4 | 4 | 0.75 | 0.0626356 | 0.0285759 | 0.0626356 | non-top | -- | -- | 16.034719 |
| 4 | 4 | 0.9 | 0.3954890 | 0.1161627 | 0.3954890 | non-top | -- | -- | 101.245195 |
| 4 | 5 | 0.65 | 0.0063400 | 0.0038458 | 0.0063400 | non-top | -- | -- | 6.492142 |
| 4 | 5 | 0.75 | 0.0164419 | 0.0071440 | 0.0164419 | non-top | -- | -- | 16.836455 |
| 4 | 5 | 0.9 | 0.1038159 | 0.0290407 | 0.1038159 | non-top | -- | -- | 106.307455 |
| 4 | 6 | 0.65 | 0.0016039 | 0.0009615 | 0.0016039 | non-top | -- | -- | 6.569429 |
| 4 | 6 | 0.75 | 0.0041594 | 0.0017860 | 0.0041594 | non-top | -- | -- | 17.036889 |
| 4 | 6 | 0.9 | 0.0262629 | 0.0072602 | 0.0262629 | non-top | -- | -- | 107.573020 |
| 8 | 2 | 0.65 | 0.1255705 | 0.1255705 | 0.0000000 | top | 0.1255701 | 2.59e-06 | 8.036510 |
| 8 | 2 | 0.75 | 0.2302755 | 0.2302755 | 0.0000000 | top | 0.2302747 | 3.56e-06 | 14.737631 |
| 8 | 2 | 0.9 | 0.9356594 | 0.9356594 | 0.0000000 | top | 0.9356544 | 5.34e-06 | 59.882203 |
| 8 | 3 | 0.65 | 0.0411259 | 0.0156963 | 0.0411259 | non-top | -- | -- | 21.056481 |
| 8 | 3 | 0.75 | 0.1019612 | 0.0287844 | 0.1019612 | non-top | -- | -- | 52.204134 |
| 8 | 3 | 0.9 | 0.6107421 | 0.1169574 | 0.6107421 | non-top | -- | -- | 312.699943 |
| 8 | 4 | 0.65 | 0.0057833 | 0.0019620 | 0.0057833 | non-top | -- | -- | 23.688541 |
| 8 | 4 | 0.75 | 0.0143383 | 0.0035981 | 0.0143383 | non-top | -- | -- | 58.729650 |
| 8 | 4 | 0.9 | 0.0858856 | 0.0146197 | 0.0858856 | non-top | -- | -- | 351.787436 |
| 16 | 2 | 0.65 | 0.0415148 | 0.0415148 | 0.0000000 | top | -- | -- | 10.627781 |
| 16 | 2 | 0.75 | 0.0749302 | 0.0749302 | 0.0000000 | top | -- | -- | 19.182142 |
| 16 | 2 | 0.9 | 0.3001224 | 0.3001224 | 0.0000000 | top | -- | -- | 76.831346 |
| 16 | 3 | 0.65 | 0.0145779 | 0.0025947 | 0.0145779 | non-top | -- | -- | 59.710908 |
| 16 | 3 | 0.75 | 0.0352643 | 0.0046831 | 0.0352643 | non-top | -- | -- | 144.442693 |
| 16 | 3 | 0.9 | 0.2054534 | 0.0187577 | 0.2054534 | non-top | -- | -- | 841.537016 |
| 32 | 2 | 0.65 | 0.0118042 | 0.0118042 | 0.0000000 | top | -- | -- | 12.087546 |
| 32 | 2 | 0.75 | 0.0211073 | 0.0211073 | 0.0000000 | top | -- | -- | 21.613870 |
| 32 | 2 | 0.9 | 0.0837944 | 0.0837944 | 0.0000000 | top | -- | -- | 85.805459 |

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
