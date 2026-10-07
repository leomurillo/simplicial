# Rounding-Cell Image Benchmark

Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.

| file | pixels | raw RGB | PNG | PNG decode | HCS1D residual | HCS2D | HCS2D songs | HCS2D decode |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 133925289798805247.jpg | 65,536 | 196,608 | 79,802 | 1.51 ms | 196,635 | 196,542 | 86/3,072 | 21.38 ms |

## Totals

- Raw RGB bytes: `196,608`
- PNG bytes: `79,802`
- HCS residual bytes: `196,635`
- HCS residual vs PNG: `+116,833` bytes (+146.40%)
- HCS2D bytes: `196,542`
- HCS2D vs PNG: `+116,740` bytes (+146.29%)

## Notes

- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.
- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.
- `HCS2D` uses sparse 8x8 2D Haar songs per color plane, accepted only when the song floors back to the exact original pixels.
- This POC has no entropy coder and no coefficient-interval optimizer yet. It is expected to lose to PNG on photographs.
- The useful signal is the HCS2D song-block count; those blocks are exact cell hits with fewer than raw pixel values.
