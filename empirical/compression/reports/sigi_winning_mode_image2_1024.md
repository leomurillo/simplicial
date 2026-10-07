# SIGI Winning Mode 1024 Benchmark

Decoded RGB center crop from `133893333653186297.jpg`.

| codec | bytes |
|---|---:|
| Raw RGB | 3,145,728 |
| gzip RGB | 2,607,759 |
| PNG | 2,286,473 |
| WebP lossless | 1,872,748 |
| SIGI `g-bg-ravg-ctx-rice` | 1,835,857 |

- SIGI vs WebP lossless: -36,891 bytes (-1.97%)
- SIGI vs PNG: -450,616 bytes (-19.71%)
- SIGI vs gzip RGB: -771,902 bytes (-29.60%)
- Roundtrip: `True`
- SIGI encode: 187.21 s; SIGI decode: 7.15 s
