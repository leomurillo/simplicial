# SIGI Source-JPEG Gauge: Costa Rica Images

This is **not** the same contract as raw-only SIGI. It uses the fact that the benchmark raw RGB pixels were produced by decoding the attached JPEG files. A source-JPEG gauge stores the original JPEG bytes plus a tiny SIGI header and defines decompression as: decode that JPEG with the fixed decoder profile to recover the raw RGB pixels.

| file | dimensions | raw RGB | WebP lossless of raw RGB | source JPEG gauge | gauge vs WebP |
|---|---:|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 5946x3861 | 68,872,518 | 17,256,580 | 1,634,994 | -15,621,586 (-90.53%) |
| central-valley-san-jose-costa-rica.jpg | 1920x1080 | 6,220,800 | 2,177,892 | 467,355 | -1,710,537 (-78.54%) |

## Totals

- Raw RGB bytes: `75,093,318`
- WebP lossless bytes: `19,434,472`
- Source-JPEG gauge bytes: `2,102,349`
- Source-JPEG gauge vs WebP: `-17,332,123` bytes (`-89.18%`)

## Interpretation

This is a real T4-style gauge lesson, but it is not a universal raw image codec result. If the decoded pixels are known to be the image of a compact generative ledger, here the JPEG bitstream plus decoder, the smallest song is the ledger itself. For arbitrary raw RGB without provenance, SIGI must use its raw-only modes, which lost to WebP on these two photos.
