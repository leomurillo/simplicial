# SCANS v0 Benchmark

Baseline: Python `gzip.compress(..., compresslevel=9, mtime=0)`.
SCANS-deflate: per-file mined finite dictionary + raw deflate payload + CRC.

| file | input | gzip | SCANS-deflate | delta | gzip decode | deflate decode | method | dict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 133925289798805247.jpg | 2,139,258 | 2,137,690 | 2,136,554 | -1,136 (-0.05%) | 4.12 ms | 4.60 ms | 0 | 0 |
| 133893333653186297.jpg | 2,443,514 | 2,435,009 | 2,434,253 | -756 (-0.03%) | 3.46 ms | 3.48 ms | 0 | 0 |
| 133921439458600606.jpg | 2,391,046 | 2,388,151 | 2,387,353 | -798 (-0.03%) | 3.25 ms | 3.32 ms | 0 | 0 |

## Totals

- Input bytes: `6,973,818`
- gzip bytes: `6,960,850`
- SCANS bytes: `6,958,160`
- SCANS delta: `-2,690` bytes (-0.04%)

## Notes

- This is an intentionally conservative first prototype. It does not yet include a custom rANS backend or blockwise packet closure.
- Method `0` is identity/raw deflate. Method `1` is the LZP predictive-residual transform.
- Method `2` is the optional Zstandard backend proxy. It requires the `zstandard` Python package for this benchmark; in production this maps to the optimized entropy backend.
- Decode time includes Python header parsing, optional dictionary inflation, entropy decode, inverse transform, and CRC verification.
- The current per-file dictionary is stored inside the stream, so these mid-sized files correctly fall back to no embedded dictionary.
