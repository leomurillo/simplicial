# E28 Face-Governed Transform Stack

This experiment tests the Pe-series reading of the compression stack: a local gauge command map is a face/boundary object, not inert metadata.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: 64x64 RGB
- WebP lossless baseline: `6,032` bytes
- transforms: `r-gr-bg, r-gr-bavg, g-rg-bavg, g-bg-ravg, ycocg, rgb`
- tropical face threshold: `16` bits
- selection time: `1.20` s

| rank | lambda bits | bytes | vs WebP | boundary edges | RLE bytes | face hit | mean regret | labels | roundtrip |
|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 5,903 | -129 | 0 | 2 | 1.000 | 0.00 | r-gr-bg:4 | True |

## Interpretation

E28 prices the exterior boundary explicitly. Per-tile scores are first converted to tropical regrets; the near-minimal gauges form a local face. The deployed command field is then selected by trading unary residual score against gauge-boundary crossings.

A pass is not only a byte win. A strong joint-on-disjoint result is also informative: if boundary governance produces smoother, auditable face maps but the exact byte stream still loses, then the face labels should drive priors or reference mining rather than be transmitted directly as a command map.

