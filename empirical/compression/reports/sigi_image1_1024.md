# Native Lossless Image Benchmark

Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.

| file | pixels | raw RGB | PNG | WebP lossless | gzip RGB | SIGI | SIGI mode | SIGI decode | HCS1D residual | HCS2D |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 133925289798805247.jpg | 1,048,576 | 3,145,728 | 1,642,726 | 1,324,414 | 1,885,843 | 1,489,395 | ycocg-rice | 4.34 s | 3,145,757 | skipped |

## Totals

- Raw RGB bytes: `3,145,728`
- PNG bytes: `1,642,726`
- WebP lossless bytes: `1,324,414`
- gzip RGB bytes: `1,885,843`
- SIGI bytes: `1,489,395`
- SIGI vs gzip RGB: `-396,448` bytes (-21.02%)
- SIGI vs PNG: `-153,331` bytes (-9.33%)
- SIGI vs WebP lossless: `+164,981` bytes (+12.46%)
- HCS residual bytes: `3,145,757`
- HCS residual vs PNG: `+1,503,031` bytes (+91.50%)

## Notes

- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.
- `WebP lossless` is encoded through Pillow/libwebp when available.
- `SIGI` is the native predictive-gauge image codec: reversible color transform, local predictor choice, and Rice entropy coding.
- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.
- `HCS2D` was skipped here because the interval-song compressor is currently much slower than the predictive codec.
