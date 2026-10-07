# Native Lossless Image Benchmark

Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.

| file | pixels | raw RGB | PNG | gzip RGB | SIGI | SIGI mode | SIGI decode | HCS1D residual | HCS2D |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 133925289798805247.jpg | 65,536 | 196,608 | 79,802 | 89,409 | 75,840 | ycocg-rice | 438.16 ms | 196,635 | skipped |
| 133893333653186297.jpg | 65,536 | 196,608 | 158,692 | 168,936 | 143,223 | ycocg-rice | 542.03 ms | 196,635 | skipped |
| 133921439458600606.jpg | 65,536 | 196,608 | 171,310 | 190,658 | 131,845 | ycocg-rice | 321.53 ms | 196,635 | skipped |

## Totals

- Raw RGB bytes: `589,824`
- PNG bytes: `409,804`
- gzip RGB bytes: `449,003`
- SIGI bytes: `350,908`
- SIGI vs gzip RGB: `-98,095` bytes (-21.85%)
- SIGI vs PNG: `-58,896` bytes (-14.37%)
- HCS residual bytes: `589,905`
- HCS residual vs PNG: `+180,101` bytes (+43.95%)

## Notes

- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.
- `SIGI` is the native predictive-gauge image codec: reversible color transform, local predictor choice, and Rice entropy coding.
- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.
- `HCS2D` was skipped here because the interval-song compressor is currently much slower than the predictive codec.
