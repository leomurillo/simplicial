# E30 Moment-Barrier Gate

E30 tests the P6 moment-barrier lesson in the image codec: use a causal Hankel sign from already-decoded residual magnitudes to choose whether the entropy model should lean smooth or rough, with no transmitted gate map.

## Neckertal_20150527-6384 (1).jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `1,210,060` bytes
- E30 baseline: `1,173,635` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | baseline | 0/1 | 1,173,635 | +0 | -36,425 | True |
| 2 | hard-moment-context | 0/1 | 1,173,956 | +321 | -36,104 | True |

## Interpretation

The best E30 row is `baseline` at `1,173,635` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 1042966, '2': 2102747}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

