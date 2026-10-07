# Sub-Tile Transported Residual Strings + Apex Posterior vs WebP

Each image is decoded to RGB first. The codec model keeps the `g-bg-ravg` gauge and local tile predictors, then refines the exact residual boundary into sub-tile blocks. Blocks may use direct residuals, a DC boundary correction, or a transported prior residual string.

| file | dimensions | block | WebP | direct block Apex | refined sub-tile | deployed | best state | ideal | vs WebP | DC blocks | copy blocks |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 256x256 | 16 | 63,034 | 69,678 | 69,834 | 69,678 | `ch-ctx-energy` | 66,555 | +6,644 (+10.54%) | 0 | 0 |
| central-valley-san-jose-costa-rica.jpg | 256x256 | 16 | 80,852 | 79,269 | 79,374 | 79,269 | `ch-ctx-grad` | 75,885 | -1,583 (-1.96%) | 0 | 0 |

## Totals

- WebP lossless bytes: `143,886`
- Deployed sub-tile/direct Apex bytes: `148,947`
- Deployed sub-tile/direct Apex vs WebP: `+5,061` bytes (+3.52%)
- Ideal no-codebook bytes: `142,440`
- Ideal no-codebook vs WebP: `-1,446` bytes (-1.00%)

## Notes

- This is an estimator, not a final bitstream.
- The deployed value is the smaller of direct block-refined posterior coding and command-refined sub-tile transport.
- Refined metadata includes local tile predictor bytes, one sparse command-flag bit per subblock, and command bytes for DC/copy subblocks.
- Energy-context schemes include 3 stored side bits per predictor tile; other contexts are decoder-visible: channel, local residual context, subblock mode, and spatial gradient class.
- `que-ver-en-costa-rica-correos-portada.jpg` deployed blocks: `768`, metadata bytes: `192`, energy metadata bytes if used: `72`.
- `que-ver-en-costa-rica-correos-portada.jpg` refined saved local-score bytes: `40`, refined model counts: `{'pred-6': 68, 'pred-4': 93, 'pred-8': 16, 'pred-7': 3, 'pred-20': 3, 'direct': 752, 'dc': 10, 'copy': 6, 'pred-5': 6, 'pred-2': 3}`.
- `central-valley-san-jose-costa-rica.jpg` deployed blocks: `768`, metadata bytes: `192`, energy metadata bytes if used: `72`.
- `central-valley-san-jose-costa-rica.jpg` refined saved local-score bytes: `3`, refined model counts: `{'pred-4': 124, 'pred-9': 15, 'pred-20': 10, 'pred-7': 8, 'pred-3': 2, 'direct': 765, 'dc': 3, 'pred-5': 5, 'pred-14': 2, 'pred-6': 26}`.
