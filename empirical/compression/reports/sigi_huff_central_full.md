# SIGI vs WebP Lossless Raw-RGB Benchmark

Each JPG is decoded to RGB bytes first. WebP lossless and SIGI are measured on those exact decoded pixels.

| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |
|---|---:|---:|---:|---:|---|---:|
| central-valley-san-jose-costa-rica.jpg | 1920x1080 | 6,220,800 | 2,177,892 | 2,371,672 | g-bg-ravg-ctx-huff | +193,780 (+8.90%) |

## Totals

- Raw RGB bytes: `6,220,800`
- WebP lossless bytes: `2,177,892`
- SIGI bytes: `2,371,672`
- SIGI vs WebP lossless: `+193,780` bytes (+8.90%)

## Notes

- SIGI sizes are exact byte counts including SIGI header, mode byte, tile headers, entropy metadata, and padding.
- This fast benchmark does not emit full SIGI files; it measures size for the current estimated modes.
- This run used only SIGI mode `g-bg-ravg-ctx-huff`.
