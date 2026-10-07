# Sub-Tile Transported Residual Strings + Apex Posterior vs WebP

Each image is decoded to RGB first. The codec model keeps the `g-bg-ravg` gauge and local tile predictors, then refines the exact residual boundary into sub-tile blocks. Blocks may use direct residuals, a DC boundary correction, or a transported prior residual string.

| file | dimensions | block | WebP | direct block Apex | refined sub-tile | deployed | best state | ideal | vs WebP | DC blocks | copy blocks |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 16 | 231,732 | 250,486 | 250,486 | 250,486 | `ch-ctx-energy` | 245,677 | +18,754 (+8.09%) | 0 | 0 |
| central-valley-san-jose-costa-rica.jpg | 512x512 | 16 | 307,430 | 303,625 | 303,625 | 303,625 | `ch-ctx-grad` | 297,043 | -3,805 (-1.24%) | 0 | 0 |

## Totals

- WebP lossless bytes: `539,162`
- Deployed sub-tile/direct Apex bytes: `554,111`
- Deployed sub-tile/direct Apex vs WebP: `+14,949` bytes (+2.77%)
- Ideal no-codebook bytes: `542,720`
- Ideal no-codebook vs WebP: `+3,558` bytes (+0.66%)

## Notes

- This is an estimator, not a final bitstream.
- The deployed value is the smaller of direct block-refined posterior coding and command-refined sub-tile transport.
- When `direct_only` is true in JSON, the refined column is intentionally equal to the direct column to skip the currently unprofitable command-search pass.
- Refined metadata includes local tile predictor bytes, one sparse command-flag bit per subblock, and command bytes for DC/copy subblocks.
- Energy-context schemes include 3 stored side bits per predictor tile; other contexts are decoder-visible: channel, local residual context, subblock mode, and spatial gradient class.
- `que-ver-en-costa-rica-correos-portada.jpg` deployed blocks: `3072`, metadata bytes: `768`, energy metadata bytes if used: `288`.
- `que-ver-en-costa-rica-correos-portada.jpg` refined saved local-score bytes: `0`, refined model counts: `{'pred-4': 418, 'pred-6': 244, 'pred-8': 57, 'pred-5': 19, 'pred-7': 8, 'pred-20': 4, 'pred-9': 4, 'direct': 3072, 'pred-2': 12, 'pred-14': 2}`.
- `central-valley-san-jose-costa-rica.jpg` deployed blocks: `3072`, metadata bytes: `768`, energy metadata bytes if used: `288`.
- `central-valley-san-jose-costa-rica.jpg` refined saved local-score bytes: `0`, refined model counts: `{'pred-4': 482, 'pred-5': 28, 'pred-14': 14, 'pred-20': 50, 'pred-6': 96, 'pred-1': 2, 'pred-9': 39, 'pred-7': 27, 'pred-3': 29, 'pred-12': 1, 'direct': 3072}`.
