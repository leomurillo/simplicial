# E28 Face-Governed Transform Stack

This experiment tests the Pe-series reading of the compression stack: a local gauge command map is a face/boundary object, not inert metadata.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: 512x512 RGB
- WebP lossless baseline: `231,732` bytes
- transforms: `r-gr-bg, r-gr-bavg, g-rg-bavg, g-bg-ravg, ycocg, rgb`
- tropical face threshold: `16` bits
- selection time: `197.42` s

| rank | lambda bits | bytes | vs WebP | boundary edges | RLE bytes | face hit | mean regret | labels | roundtrip |
|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 8 | 236,184 | +4,452 | 160 | 204 | 0.980 | 1.17 | g-bg-ravg:3, g-rg-bavg:57, r-gr-bavg:42, r-gr-bg:149, ycocg:5 | True |
| 2 | 16 | 235,825 | +4,093 | 137 | 178 | 0.949 | 2.17 | g-bg-ravg:3, g-rg-bavg:54, r-gr-bavg:44, r-gr-bg:151, ycocg:4 | True |
| 3 | 0 | 237,041 | +5,309 | 227 | 262 | 1.000 | 0.00 | g-bg-ravg:4, g-rg-bavg:53, r-gr-bavg:54, r-gr-bg:139, ycocg:6 | True |
| 4 | 32 | 234,883 | +3,151 | 79 | 116 | 0.852 | 7.38 | g-bg-ravg:1, g-rg-bavg:54, r-gr-bavg:34, r-gr-bg:167 | True |
| 5 | 64 | 234,597 | +2,865 | 51 | 90 | 0.797 | 12.69 | g-rg-bavg:44, r-gr-bavg:29, r-gr-bg:183 | True |

### Zero-Boundary and Label-Context Endpoints

The all-global `r-gr-bg` endpoint was encoded separately because it has zero command boundary. It produced `234,472` bytes, exactly matching the prior span-8 stack result and remaining the best exact stream in this family.

The command-label posterior branch was also tested. In this branch, the fine arithmetic posterior sees the selected gauge label while the parent posterior remains ungated as a backoff. This directly tests whether the missing ingredient was simply "tell the entropy model which face it is on."

| endpoint | label context | bytes | vs WebP | note |
|---|---:|---:|---:|---|
| lambda 32 | true | 235,088 | +3,356 | worse than ungated lambda 32 |
| lambda 64 | true | 234,675 | +2,943 | worse than ungated lambda 64 |
| global `r-gr-bg` | true | 234,473 | +2,741 | unchanged except one flag byte |

## Interpretation

E28 prices the exterior boundary explicitly. Per-tile scores are first converted to tropical regrets; the near-minimal gauges form a local face. The deployed command field is then selected by trading unary residual score against gauge-boundary crossings.

The realized branch is joint-on-disjoint. Boundary governance works as a diagnostic: increasing the boundary price monotonically smooths the command field, reduces RLE metadata, and reduces entropy from the raw per-tile map. But the exact byte stream still loses to the zero-boundary global face. Adding the selected face label to the fine posterior does not rescue the local command map.

So E28 says the local gauge faces are real, but the current way of transmitting them is not yet the right deployment. The next use should be indirect: let face labels drive static priors, reference mining, or parent-region selection, while transmitting only rare exceptions. In Pe-series language, the exterior face lattice should govern the model, not necessarily appear as a dense command surface in the bitstream.

