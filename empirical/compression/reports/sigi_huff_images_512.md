# Native Lossless Image Benchmark

Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.

| file | pixels | raw RGB | PNG | WebP lossless | gzip RGB | SIGI | SIGI mode | SIGI decode | HCS1D residual | HCS2D |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 133925289798805247.jpg | 262,144 | 786,432 | 382,515 | 306,272 | 426,904 | 359,059 | ycocg-rice | 2.15 s | 786,459 | skipped |
| 133893333653186297.jpg | 262,144 | 786,432 | 574,479 | 489,474 | 632,555 | 513,525 | ycocg-rice | 1.96 s | 786,459 | skipped |
| 133921439458600606.jpg | 262,144 | 786,432 | 684,111 | 505,660 | 765,756 | 522,889 | ycocg-huff | 2.67 s | 786,459 | skipped |

## Totals

- Raw RGB bytes: `2,359,296`
- PNG bytes: `1,641,105`
- WebP lossless bytes: `1,301,406`
- gzip RGB bytes: `1,825,215`
- SIGI bytes: `1,395,473`
- SIGI vs gzip RGB: `-429,742` bytes (-23.54%)
- SIGI vs PNG: `-245,632` bytes (-14.97%)
- SIGI vs WebP lossless: `+94,067` bytes (+7.23%)
- HCS residual bytes: `2,359,377`
- HCS residual vs PNG: `+718,272` bytes (+43.77%)

## Notes

- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.
- `WebP lossless` is encoded through Pillow/libwebp when available.
- `SIGI` is the native predictive-gauge image codec: reversible color transform, local predictor choice, and Rice entropy coding.
- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.
- `HCS2D` was skipped here because the interval-song compressor is currently much slower than the predictive codec.
