# Transported Kummer Song + Apex-ANS vs WebP

Each image is decoded to RGB first. The transported model searches previous Kummer-compatible tiles, stores a compact reference/shift/gain/offset song, and entropy-codes the exact residual tail with Apex-ANS.

| file | dimensions | WebP | baseline Apex-ANS | transported Kummer | best state | ideal | vs WebP | transport tiles |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 256x256 | 63,034 | 69,606 | 69,604 | `ch-ctx-energy` | 66,633 | +6,570 (+10.42%) | 2 |
| central-valley-san-jose-costa-rica.jpg | 256x256 | 80,852 | 78,958 | 78,958 | `ch-ctx-grad` | 76,043 | -1,894 (-2.34%) | 0 |

## Totals

- WebP lossless bytes: `143,886`
- Baseline Apex-ANS bytes: `148,564`
- Transported Kummer Apex-ANS bytes: `148,562`
- Transported Kummer vs WebP: `+4,676` bytes (+3.25%)
- Transported Kummer vs baseline Apex-ANS: `-2` bytes (-0.00%)
- Transported ideal no-codebook bytes: `142,676`
- Transported ideal vs WebP: `-1,210` bytes (-0.84%)

## Notes

- This is an estimator, not a final bitstream.
- Kummer state is used for tile-level reference search, not as a per-symbol context.
- The entropy estimator now tries `channel+context`, `channel+context+gradient`, `channel+context+energy`, and their small transport/gradient-energy variants.
- A transport is accepted only when its local residual score plus metadata beats the local predictor score.
- `que-ver-en-costa-rica-correos-portada.jpg` transport saved local-score bytes: `4`, metadata bytes: `198`.
- `que-ver-en-costa-rica-correos-portada.jpg` transport model counts: `{'local-p6': 67, 'local-p4': 93, 'local-p8': 16, 'residual-s1-g1': 1, 'local-p20': 3, 'local-p7': 2, 'local-p5': 6, 'local-p2': 3, 'residual-s0-g0': 1}`.
- `central-valley-san-jose-costa-rica.jpg` transport saved local-score bytes: `0`, metadata bytes: `192`.
- `central-valley-san-jose-costa-rica.jpg` transport model counts: `{'local-p4': 124, 'local-p9': 15, 'local-p20': 10, 'local-p7': 8, 'local-p3': 2, 'local-p5': 5, 'local-p14': 2, 'local-p6': 26}`.
