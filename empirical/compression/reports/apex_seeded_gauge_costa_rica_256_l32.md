# Mined Residual Strings + Apex Posterior vs WebP

The model chooses among reversible native color gauges, keeps local tile predictors, then optionally mines row residual strings with compatible energy/unitary/context signatures. Coding uses either literal-start adaptive contexts or a deterministic Apex integer prior followed by posterior updates, so the decoder gets a shared native seed with no histogram side table. The deployed estimate is the smaller of direct residual strings and mined string commands.

| file | dimensions | gauge | len | WebP | direct strings | mined strings | deployed | best state | ideal | vs WebP | DC | copy |
|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 256x256 | `r-gr-bavg` | 32 | 63,034 | 65,936 | 65,936 | 65,936 | `ch-ctx-energy-apex128` | 63,299 | +2,902 (+4.60%) | 0 | 0 |
| central-valley-san-jose-costa-rica.jpg | 256x256 | `g-rg-bavg` | 32 | 80,852 | 77,407 | 77,407 | 77,407 | `ch-ctx-grad-apex128` | 74,144 | -3,445 (-4.26%) | 0 | 0 |

## Totals

- WebP lossless bytes: `143,886`
- Deployed native bytes: `143,343`
- Deployed native vs WebP: `-543` bytes (-0.38%)
- Ideal no-codebook bytes: `137,443`
- Ideal no-codebook vs WebP: `-6,443` bytes (-4.48%)

## Notes

- This is an estimator, not a final bitstream.
- Gauge selection is charged as part of the existing mode byte in the SIGI-style header.
- Mined metadata includes predictor bytes, one sparse command-flag bit per string, and command bytes for DC/copy strings.
- Unitary/energy packet contexts are charged as side metadata when used.
- Apex-seeded schemes use `q(n)=1/((n+1)(n+2))` over zigzag residuals, mixed into each context before adaptive updates.
- `que-ver-en-costa-rica-correos-portada.jpg` mined strings: `6144`, copy: `0`, DC: `0`, local score saved: `0`.
- `que-ver-en-costa-rica-correos-portada.jpg` mined model counts: `{'pred-6': 55, 'pred-4': 102, 'pred-8': 17, 'pred-7': 3, 'pred-9': 1, 'pred-20': 2, 'direct': 6144, 'pred-5': 12}`.
- `central-valley-san-jose-costa-rica.jpg` mined strings: `6144`, copy: `0`, DC: `0`, local score saved: `0`.
- `central-valley-san-jose-costa-rica.jpg` mined model counts: `{'pred-4': 116, 'pred-9': 15, 'pred-20': 10, 'pred-7': 12, 'pred-3': 2, 'direct': 6144, 'pred-6': 28, 'pred-14': 5, 'pred-5': 4}`.
