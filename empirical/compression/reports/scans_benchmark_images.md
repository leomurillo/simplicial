# SCANS v0 Benchmark

Baseline: Python `gzip.compress(..., compresslevel=9, mtime=0)`.
SCANS-deflate: per-file mined finite dictionary + raw deflate payload + CRC.
SCANS-zstd19: same SCANS container with Zstandard level 19 as an optimized entropy-backend proxy.

| file | input | gzip | gzip decode | SCANS-deflate | delta | deflate decode | SCANS-zstd19 | delta | zstd decode |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 133925289798805247.jpg | 2,139,258 | 2,137,690 | 4.19 ms | 2,136,554 | -1,136 (-0.05%) | 4.50 ms | 2,137,638 | -52 (-0.00%) | 2.15 ms |
| 133893333653186297.jpg | 2,443,514 | 2,435,009 | 3.27 ms | 2,434,253 | -756 (-0.03%) | 3.37 ms | 2,430,676 | -4,333 (-0.18%) | 2.63 ms |
| 133921439458600606.jpg | 2,391,046 | 2,388,151 | 3.32 ms | 2,387,353 | -798 (-0.03%) | 3.39 ms | 2,385,521 | -2,630 (-0.11%) | 2.47 ms |

## Totals

- Input bytes: `6,973,818`
- gzip bytes: `6,960,850`
- SCANS bytes: `6,958,160`
- SCANS delta: `-2,690` bytes (-0.04%)
- SCANS-zstd19 bytes: `6,953,835`
- SCANS-zstd19 delta: `-7,015` bytes (-0.10%)

## Notes

- This is an intentionally conservative first prototype. It does not yet include a custom rANS backend or blockwise packet closure.
- Method `0` is identity/raw deflate. Method `1` is the LZP predictive-residual transform.
- Method `2` is the optional Zstandard backend proxy. It requires the `zstandard` Python package for this benchmark; in production this maps to the optimized entropy backend.
- Decode time includes Python header parsing, optional dictionary inflation, entropy decode, inverse transform, and CRC verification.
- The current per-file dictionary is stored inside the stream, so these mid-sized files correctly fall back to no embedded dictionary.
