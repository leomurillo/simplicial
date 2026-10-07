# SIGI JPEG-Gauge Test: Correos Full Image

The JPG was decoded to raw RGB first. The experimental SIGI mode stores a JPEG quality-95 gauge plus exact context-Rice residuals back to the decoded RGB pixels.

| item | bytes |
|---|---:|
| Raw RGB | 68,872,518 |
| WebP lossless | 17,256,580 |
| JPEG gauge | 5,413,381 |
| SIGI residual | 14,906,016 |
| SIGI JPEG-gauge total | 20,319,417 |

- SIGI JPEG-gauge vs WebP: +3,062,837 bytes (+17.75%)
- WebP encode: 149.97 s
- JPEG gauge encode: 0.44 s
- SIGI residual estimate: 1009.90 s
