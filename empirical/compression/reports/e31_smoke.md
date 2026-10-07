# E31 Regret-Governed Moment Gate

E31 keeps the E30 hard Hankel/moment split but governs it by causal expert regret. The decoder computes the same regret state from prior decoded symbols, so no gate payload is transmitted.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `128x128` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- WebP lossless: `18,442` bytes

| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |
|---:|---|---:|---:|---:|---|
| 1 | regret-global-t64-w128 | 18,308 |  | -134 | True |
| 2 | regret-global-t512-w128 | 18,363 |  | -79 | True |

### Gate Diagnostics

- best row: `regret-global-t64-w128` at `18,308` bytes
- best E31 row: `regret-global-t64-w128` at `18,308` bytes
- selected counts: `{'baseline': 14586, 'hard': 34566}`
- final gate score summary: `{'keys': 1, 'min_bits': 1075.6182610524418, 'max_bits': 1075.6182610524418, 'sum_bits': 1075.6182610524418}`
- hard expert advantage: `1075.6` bits
- chosen vs baseline: `1001.5` bits

