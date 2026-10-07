# SIGI vs WebP Lossless Raw-RGB Benchmark

Each JPG is decoded to RGB bytes first. WebP lossless and SIGI are measured on those exact decoded pixels.

| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |
|---|---:|---:|---:|---:|---|---:|
| central-valley-san-jose-costa-rica.jpg | 512x512 | 786,432 | 307,430 | 321,726 | g-bg-ravg-anova-rice | +14,296 (+4.65%) |
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 786,432 | 231,732 | 270,332 | g-bg-ravg-anova-rice | +38,600 (+16.66%) |

## Totals

- Raw RGB bytes: `1,572,864`
- WebP lossless bytes: `539,162`
- SIGI bytes: `592,058`
- SIGI vs WebP lossless: `+52,896` bytes (+9.81%)

## Notes

- SIGI sizes are exact context-Rice byte counts including SIGI header, mode byte, tile headers, and tile padding.
- This fast benchmark does not emit full SIGI files; it measures size for the current context-Rice modes.
- This run used only SIGI mode `g-bg-ravg-anova-rice`.
- This run used center crops with requested size `512`.
- `central-valley-san-jose-costa-rica.jpg` ANOVA tiles: `0` / `768`, saved `0` payload bytes.
- `que-ver-en-costa-rica-correos-portada.jpg` ANOVA tiles: `0` / `768`, saved `0` payload bytes.
