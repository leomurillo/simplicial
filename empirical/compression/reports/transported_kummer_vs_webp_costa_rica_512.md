# Transported Kummer Song + Apex-ANS vs WebP

Each image is decoded to RGB first. The transported model searches previous Kummer-compatible tiles, stores a compact reference/shift/gain/offset song, and entropy-codes the exact residual tail with Apex-ANS.

| file | dimensions | WebP | baseline Apex-ANS | transported Kummer | best state | ideal | vs WebP | transport tiles |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 231,732 | 250,198 | 250,198 | `ch-ctx-energy` | 245,546 | +18,466 (+7.97%) | 2 |
| central-valley-san-jose-costa-rica.jpg | 512x512 | 307,430 | 303,155 | 303,155 | `ch-ctx-grad` | 297,090 | -4,275 (-1.39%) | 1 |

## Totals

- WebP lossless bytes: `539,162`
- Baseline Apex-ANS bytes: `553,353`
- Transported Kummer Apex-ANS bytes: `553,353`
- Transported Kummer vs WebP: `+14,191` bytes (+2.63%)
- Transported Kummer vs baseline Apex-ANS: `+0` bytes (+0.00%)
- Transported ideal no-codebook bytes: `542,636`
- Transported ideal vs WebP: `+3,474` bytes (+0.64%)

## Notes

- This is an estimator, not a final bitstream.
- Kummer state is used for tile-level reference search, not as a per-symbol context.
- The entropy estimator now tries `channel+context`, `channel+context+gradient`, `channel+context+energy`, and their small transport/gradient-energy variants.
- A transport is accepted only when its local residual score plus metadata beats the local predictor score.
- `que-ver-en-costa-rica-correos-portada.jpg` transport saved local-score bytes: `3`, metadata bytes: `774`.
- `que-ver-en-costa-rica-correos-portada.jpg` transport model counts: `{'local-p4': 418, 'local-p6': 243, 'local-p8': 57, 'local-p5': 19, 'local-p7': 7, 'local-p20': 4, 'residual-s1-g0': 1, 'local-p9': 4, 'local-p2': 12, 'residual-s0-g0': 1, 'local-p14': 2}`.
- `central-valley-san-jose-costa-rica.jpg` transport saved local-score bytes: `2`, metadata bytes: `771`.
- `central-valley-san-jose-costa-rica.jpg` transport model counts: `{'local-p4': 481, 'local-p5': 28, 'local-p14': 14, 'local-p20': 50, 'local-p6': 96, 'local-p1': 2, 'local-p9': 39, 'local-p7': 27, 'local-p3': 29, 'local-p12': 1, 'residual-s0-g0': 1}`.
