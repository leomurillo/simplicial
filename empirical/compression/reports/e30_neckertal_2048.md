# E30 Moment-Barrier Gate

E30 tests the P6 moment-barrier lesson in the image codec: use a causal Hankel sign from already-decoded residual magnitudes to choose whether the entropy model should lean smooth or rough, with no transmitted gate map.

## Neckertal_20150527-6384 (1).jpg

- crop: `2048x2048` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `4,841,382` bytes
- E30 baseline: `4,572,054` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | hard-moment-context | 0/1 | 4,569,640 | -2,414 | -271,742 | True |
| 2 | baseline | 0/1 | 4,572,054 | +0 | -269,328 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `4,569,640` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 4511549, '2': 8071348}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

