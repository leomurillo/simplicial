# SIGI vs WebP Lossless: Costa Rica Images

Both JPG files were decoded to raw RGB bytes first. Sizes below compare lossless encodings of those exact decoded pixels.

| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |
|---|---:|---:|---:|---:|---|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 5946x3861 | 68,872,518 | 17,256,580 | 20,802,622 | g-bg-ravg-ctx-rice | +3,546,042 (+20.55%) |
| central-valley-san-jose-costa-rica.jpg | 1920x1080 | 6,220,800 | 2,177,892 | 2,382,719 | g-bg-ravg-ctx-rice | +204,827 (+9.40%) |

## Totals

- Raw RGB bytes: `75,093,318`
- WebP lossless bytes: `19,434,472`
- SIGI bytes: `23,185,341`
- SIGI vs WebP lossless: `+3,750,869` bytes (`+19.30%`)

## Notes

- SIGI sizes are exact context-Rice byte counts including SIGI header, mode byte, tile headers, and tile padding.
- The Correos image used only the current strongest SIGI mode, `g-bg-ravg-ctx-rice`, because the full decoded image is 68.9 MB and exhaustive pure-Python mode search is slow.
- The central-valley image was measured with all current context-Rice modes; `g-bg-ravg-ctx-rice` was best.
