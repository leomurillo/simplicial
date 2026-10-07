# E30 Moment-Barrier Gate

E30 tests the P6 moment-barrier lesson in the image codec: use a causal Hankel sign from already-decoded residual magnitudes to choose whether the entropy model should lean smooth or rough, with no transmitted gate map.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `64x64` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `6,032` bytes
- E30 baseline: `5,897` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | baseline | 0/1 | 5,897 | +0 | -135 | True |
| 2 | hard-moment-context | 0/1 | 5,927 | +30 | -105 | True |
| 3 | soft-moment-prior | 1/2 | 5,933 | +36 | -99 | True |
| 4 | inverted-moment-prior | 1/2 | 5,982 | +85 | -50 | True |

## Interpretation

The best E30 row is `baseline` at `5,897` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 4209, '2': 8064}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

