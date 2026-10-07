# Apex Packet Song vs WebP Lossless

Each JPG is decoded to RGB first. Apex packet sizes are exact estimates for the experimental packet-song model plus exact context-Rice residual tail.

| file | dimensions | WebP lossless | SIGI context Rice | Apex packet | Apex vs WebP | packet tiles |
|---|---:|---:|---:|---:|---:|---:|
| central-valley-san-jose-costa-rica.jpg | 512x512 | 307,430 | 321,726 | 321,726 | +14,296 (+4.65%) | 0 |
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 231,732 | 270,332 | 270,332 | +38,600 (+16.66%) | 0 |

## Totals

- WebP lossless bytes: `539,162`
- SIGI context Rice bytes: `592,058`
- Apex packet bytes: `592,058`
- Apex packet vs WebP: `+52,896` bytes (+9.81%)
- Apex packet vs context Rice: `+0` bytes (+0.00%)

## Notes

- This is a POC estimator, not the final SIGI stream.
- Packet metadata includes quantized FFT coefficients and optional sparse indices.
- Residuals are still exact; the final decoded RGB would be lossless.
- `central-valley-san-jose-costa-rica.jpg` packet models: `{}`.
- `que-ver-en-costa-rica-correos-portada.jpg` packet models: `{}`.
