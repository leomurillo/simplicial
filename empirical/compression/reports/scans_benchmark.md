# SCANS v0 Benchmark

Baseline: Python `gzip.compress(..., compresslevel=9, mtime=0)`.
SCANS-deflate: per-file mined finite dictionary + raw deflate payload + CRC.
SCANS-zstd19: same SCANS container with Zstandard level 19 as an optimized entropy-backend proxy.

| file | input | gzip | gzip decode | SCANS-deflate | delta | deflate decode | SCANS-zstd19 | delta | zstd decode |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T7-ComplexAmplitudesQuantumSector-Draft1.md | 72,557 | 22,139 | 202 us | 22,135 | -4 (-0.02%) | 197 us | 20,866 | -1,273 (-5.75%) | 143 us |
| T15-FiniteToArchimedeanCompletion-Draft1.md | 35,096 | 10,428 | 91 us | 10,424 | -4 (-0.04%) | 91 us | 10,004 | -424 (-4.07%) | 79 us |
| T0-GaugeSelectionFourierMellinSimplex-Draft1.md | 93,429 | 29,641 | 287 us | 29,630 | -11 (-0.04%) | 257 us | 27,505 | -2,136 (-7.21%) | 148 us |
| T12-FiniteApexDeterminacy-Draft1.md | 26,261 | 8,543 | 68 us | 8,539 | -4 (-0.05%) | 59 us | 8,240 | -303 (-3.55%) | 50 us |
| T13-ExactSimplicialRenormalization-Draft1.md | 32,966 | 10,127 | 86 us | 10,123 | -4 (-0.04%) | 79 us | 9,759 | -368 (-3.63%) | 53 us |
| T14-ProjectedFlatnessCurvatureLinearization-Draft1.md | 25,529 | 8,295 | 68 us | 8,291 | -4 (-0.05%) | 56 us | 8,016 | -279 (-3.36%) | 41 us |
| three_gap_compression_safety_audit.py | 16,742 | 4,770 | 31 us | 4,766 | -4 (-0.08%) | 33 us | 4,621 | -149 (-3.12%) | 27 us |
| _tiny_canned_corpus.txt | 1,250 | 511 | 7 us | 506 | -5 (-0.98%) | 8 us | 521 | +10 (+1.96%) | 6 us |

## Totals

- Input bytes: `303,830`
- gzip bytes: `94,454`
- SCANS bytes: `94,414`
- SCANS delta: `-40` bytes (-0.04%)
- SCANS-zstd19 bytes: `89,532`
- SCANS-zstd19 delta: `-4,922` bytes (-5.21%)

## Notes

- This is an intentionally conservative first prototype. It does not yet include a custom rANS backend or blockwise packet closure.
- Method `0` is identity/raw deflate. Method `1` is the LZP predictive-residual transform.
- Method `2` is the optional Zstandard backend proxy. It requires the `zstandard` Python package for this benchmark; in production this maps to the optimized entropy backend.
- Decode time includes Python header parsing, optional dictionary inflation, entropy decode, inverse transform, and CRC verification.
- The current per-file dictionary is stored inside the stream, so these mid-sized files correctly fall back to no embedded dictionary.
