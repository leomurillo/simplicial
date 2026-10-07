# SIGI vs WebP Lossless Raw-RGB Benchmark

Each JPG is decoded to RGB bytes first. WebP lossless and SIGI are measured on those exact decoded pixels.

| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |
|---|---:|---:|---:|---:|---|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 5946x3861 | 68,872,518 | 17,256,580 | 20,802,622 | g-bg-ravg-ctx-rice | +3,546,042 (+20.55%) |

## Totals

- Raw RGB bytes: `68,872,518`
- WebP lossless bytes: `17,256,580`
- SIGI bytes: `20,802,622`
- SIGI vs WebP lossless: `+3,546,042` bytes (+20.55%)

## Notes

- SIGI sizes are exact context-Rice byte counts including SIGI header, mode byte, tile headers, and tile padding.
- This fast benchmark does not emit full SIGI files; it measures size for the current context-Rice modes.
- This run used only SIGI mode `g-bg-ravg-ctx-rice`.
