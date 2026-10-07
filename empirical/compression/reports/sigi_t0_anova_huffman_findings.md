# SIGI T0 ANOVA/Huffman Findings

T0's useful instruction for compression was: choose the gauge where the block is most additive before coding the residue. I implemented that two ways in SIGI:

- `g-bg-ravg-anova-rice`: a per-tile additive song over the best current color gauge, choosing among constant, row, column, and row+column gauges before falling back to the existing context predictor.
- `*-ctx-huff`: a native context-Huffman entropy stage over the same residual structure, now available for `YCoCg`, `green16`, and `G, B-G, R-avg(G,B)`.

## Raw-RGB Costa Rica Results

Each JPG was decoded to exact RGB pixels first. WebP lossless and SIGI are measured on those decoded pixels, not on the original JPEG bytes.

### 512x512 Center Crops

| file | WebP lossless | best SIGI | best SIGI mode | result |
|---|---:|---:|---|---:|
| central-valley-san-jose-costa-rica.jpg | 307,430 | 321,726 | `g-bg-ravg-ctx-rice` | +14,296 (+4.65%) |
| que-ver-en-costa-rica-correos-portada.jpg | 231,732 | 266,380 | `g-bg-ravg-ctx-huff` | +34,648 (+14.95%) |

Totals: WebP `539,162`, SIGI `588,106`, SIGI is `+48,944` bytes (`+9.08%`).

ANOVA stats on these crops: `0 / 768` channel-tiles selected ANOVA on both images.

### Full Central Valley Image

| mode | bytes | result vs WebP |
|---|---:|---:|
| WebP lossless | 2,177,892 | baseline |
| previous `g-bg-ravg-ctx-rice` | 2,382,132 | +204,240 (+9.38%) |
| new `g-bg-ravg-ctx-huff` | 2,371,672 | +193,780 (+8.90%) |

The Huffman backend saved `10,460` bytes over Rice on the full central image, but still did not beat WebP.

## What We Learned

ANOVA is mathematically faithful to T0, but for these natural photos it is dominated by the existing `plane` predictor. For a separable tile, `left + up - up_left` already removes the row/column gauge with only a tiny tile header, while ANOVA must store row/column ledgers.

Context-Huffman is a real improvement on some image regions, especially the Correos crop, but the current residual stream still lacks WebP's stronger LZ/back-reference and richer entropy modeling.

A quick zlib proxy over SIGI residuals also lost badly on the 512 crops, so the next promising raw-only step is not “wrap the residuals in a generic compressor.” It is a better native image model: larger-scale copy/gauge references, rANS-style entropy with adaptive contexts, or a JPEG-block-aware residual gauge.

The provenance gauge remains the clear size win for JPEG-origin inputs: if the contract allows storing the original JPEG ledger plus a fixed decoder profile, both Costa Rica images beat WebP by a very large margin. That is a different contract from raw-only compression, but it is exactly the T-series lesson in its sharpest form.
