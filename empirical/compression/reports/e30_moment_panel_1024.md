# E30 Moment-Barrier Gate

E30 tests the P6 moment-barrier lesson in the image codec: use a causal Hankel sign from already-decoded residual magnitudes to choose whether the entropy model should lean smooth or rough, with no transmitted gate map.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `975,520` bytes
- E30 baseline: `961,567` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | hard-moment-context | 0/1 | 947,176 | -14,391 | -28,344 | True |
| 2 | baseline | 0/1 | 961,567 | +0 | -13,953 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `947,176` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 1763305, '2': 1382408}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

## central-valley-san-jose-costa-rica.jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `1,142,164` bytes
- E30 baseline: `1,087,964` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | hard-moment-context | 0/1 | 1,085,582 | -2,382 | -56,582 | True |
| 2 | baseline | 0/1 | 1,087,964 | +0 | -54,200 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `1,085,582` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 1625612, '2': 1520101}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

## 133925289798805247.jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `1,324,414` bytes
- E30 baseline: `1,217,366` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | hard-moment-context | 0/1 | 1,216,896 | -470 | -107,518 | True |
| 2 | baseline | 0/1 | 1,217,366 | +0 | -107,048 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `1,216,896` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 1360280, '2': 1785433}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

