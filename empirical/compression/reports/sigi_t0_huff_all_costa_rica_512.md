# SIGI vs WebP Lossless Raw-RGB Benchmark

Each JPG is decoded to RGB bytes first. WebP lossless and SIGI are measured on those exact decoded pixels.

| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |
|---|---:|---:|---:|---:|---|---:|
| central-valley-san-jose-costa-rica.jpg | 512x512 | 786,432 | 307,430 | 321,726 | g-bg-ravg-ctx-rice | +14,296 (+4.65%) |
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 786,432 | 231,732 | 266,380 | g-bg-ravg-ctx-huff | +34,648 (+14.95%) |

## Totals

- Raw RGB bytes: `1,572,864`
- WebP lossless bytes: `539,162`
- SIGI bytes: `588,106`
- SIGI vs WebP lossless: `+48,944` bytes (+9.08%)

## Notes

- SIGI sizes are exact byte counts including SIGI header, mode byte, tile headers, entropy metadata, and padding.
- This fast benchmark does not emit full SIGI files; it measures size for the current estimated modes.
- This run used center crops with requested size `512`.
