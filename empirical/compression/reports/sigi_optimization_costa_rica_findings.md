# SIGI Costa Rica Optimization Findings

The requested raw-RGB benchmark decodes each JPG first, then compares lossless encodings of the decoded pixels.

## Raw-Only SIGI

| file | raw RGB | WebP lossless | best raw-only SIGI | result |
|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 68,872,518 | 17,256,580 | 20,802,622 | SIGI +20.55% |
| central-valley-san-jose-costa-rica.jpg | 6,220,800 | 2,177,892 | 2,382,132 | SIGI +9.38% |

Best raw-only SIGI mode: `g-bg-ravg-ctx-rice`.

## Generated JPEG Gauge

This mode starts from decoded RGB, generates a JPEG gauge, decodes it, then stores exact SIGI residuals back to the original RGB.

| file | WebP lossless | JPEG gauge | SIGI residual | total | result |
|---|---:|---:|---:|---:|---:|
| central-valley-san-jose-costa-rica.jpg, q95 | 2,177,892 | 715,587 | 1,230,632 | 1,946,239 | -10.64% |
| que-ver-en-costa-rica-correos-portada.jpg, q95 | 17,256,580 | 5,413,381 | 14,906,016 | 20,319,417 | +17.75% |

This is a promising exact residual-gauge path, but not enough for Correos yet.

## Source-JPEG Gauge

This mode stores the original JPEG bitstream and defines decompression as decoding that bitstream under a fixed decoder profile. It is not a generic raw-only image codec, but it is the smallest known gauge for these decoded pixels because the pixels came from that ledger.

| file | WebP lossless | source JPEG gauge | result |
|---|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 17,256,580 | 1,634,994 | -90.53% |
| central-valley-san-jose-costa-rica.jpg | 2,177,892 | 467,355 | -78.54% |

## Takeaway

For arbitrary decoded raw RGB, SIGI still needs a stronger entropy model and/or photo-specific residual gauge to beat WebP on these two photos. If provenance is allowed, the T4 intuition wins immediately: the compact source gauge is vastly smaller than any generic lossless encoding of the decoded pixels.
