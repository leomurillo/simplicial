# Mined Residual Strings + Apex Posterior vs WebP

The model chooses among reversible native color gauges, keeps local tile predictors, then optionally mines row residual strings with compatible energy/unitary/context signatures. Coding uses either literal-start adaptive contexts or a deterministic Apex integer prior followed by posterior updates, so the decoder gets a shared native seed with no histogram side table. The deployed estimate is the smaller of direct residual strings and mined string commands.

| file | dimensions | gauge | len | WebP | direct strings | mined strings | deployed | best state | ideal | vs WebP | DC | copy |
|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | `r-gr-bavg` | 32 | 231,732 | 237,192 | 237,192 | 237,192 | `ch-ctx-energy-unitary-apex128` | 232,706 | +5,460 (+2.36%) | 0 | 0 |
| central-valley-san-jose-costa-rica.jpg | 512x512 | `g-rg-bavg` | 32 | 307,430 | 294,424 | 294,424 | 294,424 | `ch-ctx-grad-apex128` | 287,532 | -13,006 (-4.23%) | 0 | 0 |

## Totals

- WebP lossless bytes: `539,162`
- Deployed native bytes: `531,616`
- Deployed native vs WebP: `-7,546` bytes (-1.40%)
- Ideal no-codebook bytes: `520,238`
- Ideal no-codebook vs WebP: `-18,924` bytes (-3.51%)

## Notes

- This is an estimator, not a final bitstream.
- Gauge selection is charged as part of the existing mode byte in the SIGI-style header.
- Mined metadata includes predictor bytes, one sparse command-flag bit per string, and command bytes for DC/copy strings.
- Unitary/energy packet contexts are charged as side metadata when used.
- Apex-seeded schemes use `q(n)=1/((n+1)(n+2))` over zigzag residuals, mixed into each context before adaptive updates.
- `que-ver-en-costa-rica-correos-portada.jpg` mined strings: `24576`, copy: `0`, DC: `0`, local score saved: `0`.
- `que-ver-en-costa-rica-correos-portada.jpg` mined model counts: `{'pred-4': 396, 'pred-6': 226, 'pred-8': 68, 'pred-5': 33, 'pred-7': 13, 'pred-20': 3, 'pred-9': 8, 'direct': 24576, 'pred-2': 15, 'pred-14': 6}`.
- `central-valley-san-jose-costa-rica.jpg` mined strings: `24576`, copy: `0`, DC: `0`, local score saved: `0`.
- `central-valley-san-jose-costa-rica.jpg` mined model counts: `{'pred-4': 486, 'pred-5': 34, 'pred-14': 18, 'pred-20': 50, 'pred-6': 79, 'pred-1': 2, 'pred-9': 39, 'pred-7': 30, 'pred-3': 29, 'pred-12': 1, 'direct': 24576}`.
