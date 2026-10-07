# SCANS v0 Benchmark

Baseline: Python `gzip.compress(..., compresslevel=9, mtime=0)`.
SCANS-deflate: per-file mined finite dictionary + raw deflate payload + CRC.

| file | input | gzip | SCANS-deflate | delta | gzip decode | deflate decode | method | dict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| T7-ComplexAmplitudesQuantumSector-Draft1.md | 72,557 | 22,139 | 22,135 | -4 (-0.02%) | 192 us | 188 us | 0 | 0 |
| T15-FiniteToArchimedeanCompletion-Draft1.md | 35,096 | 10,428 | 10,424 | -4 (-0.04%) | 82 us | 79 us | 0 | 0 |
| T0-GaugeSelectionFourierMellinSimplex-Draft1.md | 93,429 | 29,641 | 29,630 | -11 (-0.04%) | 258 us | 257 us | 0 | 0 |
| T12-FiniteApexDeterminacy-Draft1.md | 26,261 | 8,543 | 8,539 | -4 (-0.05%) | 72 us | 58 us | 0 | 0 |
| T13-ExactSimplicialRenormalization-Draft1.md | 32,966 | 10,127 | 10,123 | -4 (-0.04%) | 77 us | 73 us | 0 | 0 |
| T14-ProjectedFlatnessCurvatureLinearization-Draft1.md | 25,529 | 8,295 | 8,291 | -4 (-0.05%) | 63 us | 58 us | 0 | 0 |
| three_gap_compression_safety_audit.py | 16,742 | 4,770 | 4,766 | -4 (-0.08%) | 34 us | 33 us | 0 | 0 |
| _tiny_canned_corpus.txt | 1,250 | 511 | 506 | -5 (-0.98%) | 7 us | 7 us | 0 | 0 |

## Totals

- Input bytes: `303,830`
- gzip bytes: `94,454`
- SCANS bytes: `94,414`
- SCANS delta: `-40` bytes (-0.04%)

## Notes

- This is an intentionally conservative first prototype. It does not yet include a custom rANS backend or blockwise packet closure.
- Method `0` is identity/raw deflate. Method `1` is the LZP predictive-residual transform.
- Method `2` is the optional Zstandard backend proxy. It requires the `zstandard` Python package for this benchmark; in production this maps to the optimized entropy backend.
- Decode time includes Python header parsing, optional dictionary inflation, entropy decode, inverse transform, and CRC verification.
- The current per-file dictionary is stored inside the stream, so these mid-sized files correctly fall back to no embedded dictionary.
