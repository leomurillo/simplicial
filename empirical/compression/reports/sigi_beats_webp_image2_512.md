# Native Lossless Image Benchmark

Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.

| file | pixels | raw RGB | PNG | WebP lossless | gzip RGB | SIGI | SIGI mode | SIGI decode | HCS1D residual | HCS2D |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 133893333653186297.jpg | 262,144 | 786,432 | 574,479 | 489,474 | 632,555 | 484,907 | g-bg-ravg-ctx-rice | 1.75 s | 786,459 | skipped |

## Totals

- Raw RGB bytes: `786,432`
- PNG bytes: `574,479`
- WebP lossless bytes: `489,474`
- gzip RGB bytes: `632,555`
- SIGI bytes: `484,907`
- SIGI vs gzip RGB: `-147,648` bytes (-23.34%)
- SIGI vs PNG: `-89,572` bytes (-15.59%)
- SIGI vs WebP lossless: `-4,567` bytes (-0.93%)
- HCS residual bytes: `786,459`
- HCS residual vs PNG: `+211,980` bytes (+36.90%)

## Notes

- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.
- `WebP lossless` is encoded through Pillow/libwebp when available.
- `SIGI` is the native predictive-gauge image codec: reversible color transform, local predictor choice, and Rice entropy coding.
- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.
- `HCS2D` was skipped here because the interval-song compressor is currently much slower than the predictive codec.
