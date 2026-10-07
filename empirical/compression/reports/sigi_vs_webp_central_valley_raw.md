# SIGI vs WebP Lossless Raw-RGB Benchmark

Each JPG is decoded to RGB bytes first. WebP lossless and SIGI are measured on those exact decoded pixels.

| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |
|---|---:|---:|---:|---:|---|---:|
| central-valley-san-jose-costa-rica.jpg | 1920x1080 | 6,220,800 | 2,177,892 | 2,382,719 | g-bg-ravg-ctx-rice | +204,827 (+9.40%) |

## Totals

- Raw RGB bytes: `6,220,800`
- WebP lossless bytes: `2,177,892`
- SIGI bytes: `2,382,719`
- SIGI vs WebP lossless: `+204,827` bytes (+9.40%)

## Notes

- SIGI sizes are exact context-Rice byte counts including SIGI header, mode byte, tile headers, and tile padding.
- This fast benchmark does not emit full SIGI files; it measures size for the current context-Rice modes.
