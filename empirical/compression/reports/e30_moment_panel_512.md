# E30 Moment-Barrier Gate

E30 tests the P6 moment-barrier lesson in the image codec: use a causal Hankel sign from already-decoded residual magnitudes to choose whether the entropy model should lean smooth or rough, with no transmitted gate map.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `231,732` bytes
- E30 baseline: `234,465` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | hard-moment-context | 0/1 | 229,866 | -4,599 | -1,866 | True |
| 2 | baseline | 0/1 | 234,465 | +0 | +2,733 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `229,866` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 452044, '2': 334373}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

## central-valley-san-jose-costa-rica.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `307,430` bytes
- E30 baseline: `298,811` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | hard-moment-context | 0/1 | 298,588 | -223 | -8,842 | True |
| 2 | baseline | 0/1 | 298,811 | +0 | -8,619 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `298,588` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 350253, '2': 436164}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

## 133925289798805247.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `306,272` bytes
- E30 baseline: `286,705` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | baseline | 0/1 | 286,705 | +0 | -19,567 | True |
| 2 | hard-moment-context | 0/1 | 287,475 | +770 | -18,797 | True |

## Interpretation

The best E30 row is `baseline` at `286,705` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 365839, '2': 420578}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

## 133893333653186297.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `489,474` bytes
- E30 baseline: `481,109` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | baseline | 0/1 | 481,109 | +0 | -8,365 | True |
| 2 | hard-moment-context | 0/1 | 482,507 | +1,398 | -6,967 | True |

## Interpretation

The best E30 row is `baseline` at `481,109` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 220624, '2': 565793}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

## 133921439458600606.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `505,660` bytes
- E30 baseline: `486,804` bytes

| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---:|---|
| 1 | baseline | 0/1 | 486,804 | +0 | -18,856 | True |
| 2 | hard-moment-context | 0/1 | 487,827 | +1,023 | -17,833 | True |

## Interpretation

The best E30 row is `baseline` at `486,804` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 162228, '2': 624189}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.

