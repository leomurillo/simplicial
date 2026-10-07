# E31 Regret-Governed Moment Gate

E31 keeps the E30 hard Hankel/moment split but governs it by causal expert regret. The decoder computes the same regret state from prior decoded symbols, so no gate payload is transmitted.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `231,732` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 hard-moment-context | 229,866 | -4,599 | -1,866 | True |
| 2 | regret-global-t512-w2048 | 229,933 | -4,532 | -1,799 | True |
| 3 | E30 baseline | 234,465 | +0 | +2,733 | True |

### Gate Diagnostics

- best row: `E30 hard-moment-context` at `229,866` bytes
- best E31 row: `regret-global-t512-w2048` at `229,933` bytes
- selected counts: `{'baseline': 40138, 'hard': 746294}`
- final gate score summary: `{'keys': 1, 'min_bits': 36790.628137089145, 'max_bits': 36790.628137089145, 'sum_bits': 36790.628137089145}`
- hard expert advantage: `36790.6` bits
- chosen vs baseline: `36276.9` bits

## central-valley-san-jose-costa-rica.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `307,430` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 hard-moment-context | 298,588 | -223 | -8,842 | True |
| 2 | regret-global-t512-w2048 | 298,655 | -156 | -8,775 | True |
| 3 | E30 baseline | 298,811 | +0 | -8,619 | True |

### Gate Diagnostics

- best row: `E30 hard-moment-context` at `298,588` bytes
- best E31 row: `regret-global-t512-w2048` at `298,655` bytes
- selected counts: `{'baseline': 604942, 'hard': 181490}`
- final gate score summary: `{'keys': 1, 'min_bits': 1783.0038996583482, 'max_bits': 1783.0038996583482, 'sum_bits': 1783.0038996583482}`
- hard expert advantage: `1783.0` bits
- chosen vs baseline: `1268.3` bits

## 133925289798805247.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `306,272` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 baseline | 286,705 | +0 | -19,567 | True |
| 2 | regret-global-t512-w2048 | 286,708 | +3 | -19,564 | True |
| 3 | E30 hard-moment-context | 287,475 | +770 | -18,797 | True |

### Gate Diagnostics

- best row: `E30 baseline` at `286,705` bytes
- best E31 row: `regret-global-t512-w2048` at `286,708` bytes
- selected counts: `{'baseline': 786432}`
- final gate score summary: `{'keys': 1, 'min_bits': -6159.584362294722, 'max_bits': -6159.584362294722, 'sum_bits': -6159.584362294722}`
- hard expert advantage: `-6159.6` bits
- chosen vs baseline: `0.0` bits

## 133893333653186297.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `489,474` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 baseline | 481,109 | +0 | -8,365 | True |
| 2 | regret-global-t512-w2048 | 481,112 | +3 | -8,362 | True |
| 3 | E30 hard-moment-context | 482,507 | +1,398 | -6,967 | True |

### Gate Diagnostics

- best row: `E30 baseline` at `481,109` bytes
- best E31 row: `regret-global-t512-w2048` at `481,112` bytes
- selected counts: `{'baseline': 786432}`
- final gate score summary: `{'keys': 1, 'min_bits': -11180.160137115841, 'max_bits': -11180.160137115841, 'sum_bits': -11180.160137115841}`
- hard expert advantage: `-11180.2` bits
- chosen vs baseline: `0.0` bits

## 133921439458600606.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `505,660` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | E30 baseline | 486,804 | +0 | -18,856 | True |
| 2 | regret-global-t512-w2048 | 486,807 | +3 | -18,853 | True |
| 3 | E30 hard-moment-context | 487,827 | +1,023 | -17,833 | True |

### Gate Diagnostics

- best row: `E30 baseline` at `486,804` bytes
- best E31 row: `regret-global-t512-w2048` at `486,807` bytes
- selected counts: `{'baseline': 786432}`
- final gate score summary: `{'keys': 1, 'min_bits': -8182.471054043683, 'max_bits': -8182.471054043683, 'sum_bits': -8182.471054043683}`
- hard expert advantage: `-8182.5` bits
- chosen vs baseline: `0.0` bits

