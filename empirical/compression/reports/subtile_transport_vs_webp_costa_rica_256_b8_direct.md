# Sub-Tile Transported Residual Strings + Apex Posterior vs WebP

Each image is decoded to RGB first. The codec model keeps the `g-bg-ravg` gauge and local tile predictors, then refines the exact residual boundary into sub-tile blocks. Blocks may use direct residuals, a DC boundary correction, or a transported prior residual string.

| file | dimensions | block | WebP | direct block Apex | refined sub-tile | deployed | best state | ideal | vs WebP | DC blocks | copy blocks |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 256x256 | 8 | 63,034 | 69,678 | 69,678 | 69,678 | `ch-ctx-energy` | 66,367 | +6,644 (+10.54%) | 0 | 0 |
| central-valley-san-jose-costa-rica.jpg | 256x256 | 8 | 80,852 | 79,288 | 79,288 | 79,288 | `ch-ctx-grad` | 75,715 | -1,564 (-1.93%) | 0 | 0 |

## Totals

- WebP lossless bytes: `143,886`
- Deployed sub-tile/direct Apex bytes: `148,966`
- Deployed sub-tile/direct Apex vs WebP: `+5,080` bytes (+3.53%)
- Ideal no-codebook bytes: `142,082`
- Ideal no-codebook vs WebP: `-1,804` bytes (-1.25%)

## Notes

- This is an estimator, not a final bitstream.
- The deployed value is the smaller of direct block-refined posterior coding and command-refined sub-tile transport.
- When `direct_only` is true in JSON, the refined column is intentionally equal to the direct column to skip the currently unprofitable command-search pass.
- Refined metadata includes local tile predictor bytes, one sparse command-flag bit per subblock, and command bytes for DC/copy subblocks.
- Energy-context schemes include 3 stored side bits per predictor tile; other contexts are decoder-visible: channel, local residual context, subblock mode, and spatial gradient class.
- `que-ver-en-costa-rica-correos-portada.jpg` deployed blocks: `3072`, metadata bytes: `192`, energy metadata bytes if used: `72`.
- `que-ver-en-costa-rica-correos-portada.jpg` refined saved local-score bytes: `0`, refined model counts: `{'pred-6': 68, 'pred-4': 93, 'pred-8': 16, 'pred-7': 3, 'pred-20': 3, 'direct': 3072, 'pred-5': 6, 'pred-2': 3}`.
- `central-valley-san-jose-costa-rica.jpg` deployed blocks: `3072`, metadata bytes: `192`, energy metadata bytes if used: `72`.
- `central-valley-san-jose-costa-rica.jpg` refined saved local-score bytes: `0`, refined model counts: `{'pred-4': 124, 'pred-9': 15, 'pred-20': 10, 'pred-7': 8, 'pred-3': 2, 'direct': 3072, 'pred-5': 5, 'pred-14': 2, 'pred-6': 26}`.
