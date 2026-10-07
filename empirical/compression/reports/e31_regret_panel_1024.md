# E31 Regret-Governed Moment Gate

E31 keeps the E30 hard Hankel/moment split but governs it by causal expert regret. The decoder computes the same regret state from prior decoded symbols, so no gate payload is transmitted.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `975,520` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 hard-moment-context | 947,176 | -14,391 | -28,344 | True |
| 2 | regret-global-t512-w2048 | 947,243 | -14,324 | -28,277 | True |
| 3 | E30 baseline | 961,567 | +0 | -13,953 | True |

### Gate Diagnostics

- best row: `E30 hard-moment-context` at `947,176` bytes
- best E31 row: `regret-global-t512-w2048` at `947,243` bytes
- selected counts: `{'baseline': 117416, 'hard': 3028312}`
- final gate score summary: `{'keys': 1, 'min_bits': 115122.57202144404, 'max_bits': 115122.57202144404, 'sum_bits': 115122.57202144404}`
- hard expert advantage: `115122.6` bits
- chosen vs baseline: `114610.3` bits

## central-valley-san-jose-costa-rica.jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `1,142,164` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 hard-moment-context | 1,085,582 | -2,382 | -56,582 | True |
| 2 | regret-global-t512-w2048 | 1,085,649 | -2,315 | -56,515 | True |
| 3 | E30 baseline | 1,087,964 | +0 | -54,200 | True |

### Gate Diagnostics

- best row: `E30 hard-moment-context` at `1,085,582` bytes
- best E31 row: `regret-global-t512-w2048` at `1,085,649` bytes
- selected counts: `{'baseline': 508565, 'hard': 2637163}`
- final gate score summary: `{'keys': 1, 'min_bits': 19060.830156263655, 'max_bits': 19060.830156263655, 'sum_bits': 19060.830156263655}`
- hard expert advantage: `19060.8` bits
- chosen vs baseline: `18542.8` bits

## 133925289798805247.jpg

- crop: `1024x1024` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `1,324,414` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 hard-moment-context | 1,216,896 | -470 | -107,518 | True |
| 2 | regret-global-t512-w2048 | 1,216,963 | -403 | -107,451 | True |
| 3 | E30 baseline | 1,217,366 | +0 | -107,048 | True |

### Gate Diagnostics

- best row: `E30 hard-moment-context` at `1,216,896` bytes
- best E31 row: `regret-global-t512-w2048` at `1,216,963` bytes
- selected counts: `{'baseline': 2908232, 'hard': 237496}`
- final gate score summary: `{'keys': 1, 'min_bits': 3758.9049664720465, 'max_bits': 3758.9049664720465, 'sum_bits': 3758.9049664720465}`
- hard expert advantage: `3758.9` bits
- chosen vs baseline: `3246.1` bits

