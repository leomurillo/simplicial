# Apex-ANS vs WebP Lossless

Each image is decoded to RGB first. Apex-ANS is a no-codebook adaptive entropy estimate over SIGI residuals using native gauge/context state.

| file | dimensions | WebP lossless | Apex-ANS | mode | vs WebP | ideal no-codebook |
|---|---:|---:|---:|---|---:|---:|
| central-valley-san-jose-costa-rica.jpg | 512x512 | 307,430 | 307,000 | `g-bg-ravg/ch-ctx` | -430 (-0.14%) | 295,097 |
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 231,732 | 253,505 | `g-bg-ravg/ch-ctx` | +21,773 (+9.40%) | 243,069 |

## Totals

- WebP lossless bytes: `539,162`
- Apex-ANS bytes: `560,505`
- Apex-ANS vs WebP: `+21,343` bytes (+3.96%)
- Ideal no-codebook Apex entropy bytes: `538,166`
- Ideal no-codebook vs WebP: `-996` bytes (-0.18%)

## Notes

- This is a feasible entropy-model estimate, not a final rANS bitstream.
- New residual symbols are encoded as adaptive escapes plus varint literals, so the estimate does not rely on stored codebooks.
- The `ideal no-codebook` column removes adaptation/escape friction and measures the model ceiling.
- `central-valley-san-jose-costa-rica.jpg` best contexts: `23`, new symbols: `2174`.
- `que-ver-en-costa-rica-correos-portada.jpg` best contexts: `24`, new symbols: `1457`.
