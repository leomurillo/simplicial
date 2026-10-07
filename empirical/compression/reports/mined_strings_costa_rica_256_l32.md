# Mined Residual Strings + Apex Posterior vs WebP

The model keeps the `g-bg-ravg` gauge and local tile predictors, then mines row residual strings with compatible energy/unitary/context signatures. The deployed estimate is the smaller of direct residual strings and mined string commands.

| file | dimensions | len | WebP | direct strings | mined strings | deployed | best state | ideal | vs WebP | DC | copy |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 256x256 | 32 | 63,034 | 69,678 | 70,438 | 69,678 | `ch-ctx-energy` | 65,690 | +6,644 (+10.54%) | 0 | 0 |
| central-valley-san-jose-costa-rica.jpg | 256x256 | 32 | 80,852 | 79,213 | 79,981 | 79,213 | `ch-ctx-grad` | 74,879 | -1,639 (-2.03%) | 0 | 0 |

## Totals

- WebP lossless bytes: `143,886`
- Deployed native bytes: `148,891`
- Deployed native vs WebP: `+5,005` bytes (+3.48%)
- Ideal no-codebook bytes: `140,569`
- Ideal no-codebook vs WebP: `-3,317` bytes (-2.31%)

## Notes

- This is an estimator, not a final bitstream.
- Mined metadata includes predictor bytes, one sparse command-flag bit per string, and command bytes for DC/copy strings.
- Unitariy/energy packet contexts are charged as side metadata when used.
- `que-ver-en-costa-rica-correos-portada.jpg` mined strings: `6144`, copy: `5`, DC: `0`, local score saved: `16`.
- `que-ver-en-costa-rica-correos-portada.jpg` mined model counts: `{'pred-6': 68, 'pred-4': 93, 'pred-8': 16, 'pred-7': 3, 'pred-20': 3, 'direct': 6139, 'copy+': 5, 'pred-5': 6, 'pred-2': 3}`.
- `central-valley-san-jose-costa-rica.jpg` mined strings: `6144`, copy: `0`, DC: `1`, local score saved: `3`.
- `central-valley-san-jose-costa-rica.jpg` mined model counts: `{'pred-4': 124, 'pred-9': 15, 'pred-20': 10, 'pred-7': 8, 'pred-3': 2, 'direct': 6143, 'dc': 1, 'pred-5': 5, 'pred-14': 2, 'pred-6': 26}`.
