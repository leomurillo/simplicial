# Rounding-Cell Image Benchmark

Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.

| file | pixels | raw RGB | PNG | PNG decode | HCS1D residual | HCS2D | HCS2D songs | HCS2D decode |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 133925289798805247.jpg | 262,144 | 786,432 | 382,515 | 4.81 ms | 786,459 | 788,033 | 280/12,288 | 141.74 ms |
| 133893333653186297.jpg | 262,144 | 786,432 | 574,479 | 7.45 ms | 786,459 | 790,913 | 224/12,288 | 176.73 ms |
| 133921439458600606.jpg | 262,144 | 786,432 | 684,111 | 6.17 ms | 786,459 | 798,733 | 0/12,288 | 134.81 ms |

## Totals

- Raw RGB bytes: `2,359,296`
- PNG bytes: `1,641,105`
- HCS residual bytes: `2,359,377`
- HCS residual vs PNG: `+718,272` bytes (+43.77%)
- HCS2D bytes: `2,377,679`
- HCS2D vs PNG: `+736,574` bytes (+44.88%)

## Notes

- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.
- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.
- `HCS2D` uses sparse 8x8 2D Haar songs per color plane, accepted only when the song floors back to the exact original pixels.
- This POC has no entropy coder and no coefficient-interval optimizer yet. It is expected to lose to PNG on photographs.
- The useful signal is the HCS2D song-block count; those blocks are exact cell hits with fewer than raw pixel values.
