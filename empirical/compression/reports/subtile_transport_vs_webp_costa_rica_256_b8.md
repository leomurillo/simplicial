# Sub-Tile Transported Residual Strings + Apex Posterior vs WebP

Each image is decoded to RGB first. The codec model keeps the `g-bg-ravg` gauge and local tile predictors, then refines the exact residual boundary into sub-tile blocks. Blocks may use direct residuals, a DC boundary correction, or a transported prior residual string.

| file | dimensions | block | WebP | sub-tile Apex | best state | ideal | vs WebP | DC blocks | copy blocks |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 256x256 | 8 | 63,034 | 70,996 | `ch-ctx` | 68,931 | +7,962 (+12.63%) | 38 | 24 |
| central-valley-san-jose-costa-rica.jpg | 256x256 | 8 | 80,852 | 79,681 | `ch-ctx-grad` | 76,764 | -1,171 (-1.45%) | 17 | 15 |

## Totals

- WebP lossless bytes: `143,886`
- Sub-tile Apex bytes: `150,677`
- Sub-tile Apex vs WebP: `+6,791` bytes (+4.72%)
- Ideal no-codebook bytes: `145,695`
- Ideal no-codebook vs WebP: `+1,809` bytes (+1.26%)

## Notes

- This is an estimator, not a final bitstream.
- Metadata includes local tile predictor bytes, one sparse command-flag bit per subblock, and command bytes for DC/copy subblocks.
- Contexts are decoder-visible: channel, local residual context, subblock mode, and spatial gradient class.
- `que-ver-en-costa-rica-correos-portada.jpg` blocks: `3072`, metadata bytes: `724`, local score saved: `102`.
- `que-ver-en-costa-rica-correos-portada.jpg` model counts: `{'pred-6': 68, 'pred-4': 93, 'pred-8': 16, 'pred-7': 3, 'pred-20': 3, 'direct': 3010, 'copy': 24, 'dc': 38, 'pred-5': 6, 'pred-2': 3}`.
- `central-valley-san-jose-costa-rica.jpg` blocks: `3072`, metadata bytes: `655`, local score saved: `44`.
- `central-valley-san-jose-costa-rica.jpg` model counts: `{'pred-4': 124, 'pred-9': 15, 'pred-20': 10, 'pred-7': 8, 'pred-3': 2, 'direct': 3040, 'pred-5': 5, 'pred-14': 2, 'pred-6': 26, 'dc': 17, 'copy': 15}`.
