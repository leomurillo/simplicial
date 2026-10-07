# E29 Ramanujan Transfer Prior

E29 tests the P5 reading in codec form: the conductor boundary should govern the entropy prior without being transmitted as a dense command map.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `512x512` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- conductor modulus: `30`
- WebP lossless: `231,732` bytes
- E29 baseline: `234,467` bytes

| rank | model | mix | rung mode | bytes | vs E29 baseline | vs WebP | roundtrip |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | baseline | 0/1 | tile | 234,467 | +0 | +2,735 | True |
| 2 | soft-ramanujan | 1/4 | tile | 234,502 | +35 | +2,770 | True |
| 3 | soft-ramanujan | 1/2 | tile | 234,555 | +88 | +2,823 | True |
| 4 | shuffled-ramanujan | 1/4 | tile | 234,624 | +157 | +2,892 | True |
| 5 | shuffled-ramanujan | 1/2 | tile | 234,842 | +375 | +3,110 | True |
| 6 | hard-rung-context | 0/1 | tile | 235,321 | +854 | +3,589 | True |

## Interpretation

The best E29 row is `baseline` with mix `0/1` and rung mode `tile`, at `234,467` bytes.

The key comparison is against both the baseline and the shuffled control. A genuine Ramanujan-transfer effect should beat the baseline and also beat a prior with the same mass histogram assigned to the wrong conductor packets.

The realized branch is joint-on-disjoint, but not a byte win. The correct Ramanujan assignment is consistently better than the shuffled conductor assignment, so the packet names are not inert:

| mix | soft Ramanujan | shuffled control | Ramanujan advantage |
|---:|---:|---:|---:|
| 1/4 | 234,502 | 234,624 | 122 bytes |
| 1/2 | 234,555 | 234,842 | 287 bytes |

However, both soft Ramanujan rows still lose to the E29 baseline, and the hard conductor/rung context is much worse (`+854` bytes). The boundary coordinate is therefore detectable but not yet deployable as a direct per-symbol prior in this raster residual stream.

An extended sweep also wrote exact `.sr29` artifacts for `x` rung mode and mix `3/4`. They preserve the same shape: soft Ramanujan remains closer to baseline than the shuffled control, but the baseline remains best (`soft 3/4 tile = 234,620`, `shuffled 3/4 tile = 235,093`; `soft 1/4 x = 234,502`, `soft 1/2 x = 234,554`, `soft 3/4 x = 234,619`).

Conclusion: E29 does not close the byte gap. It does validate the more subtle P5 reading: Ramanujan packet identity carries signal relative to a wrong-packet control, but using it as a generic dynamic prior over residual magnitudes is too blunt. The next use should be selective: Ramanujan priors should trigger only where a residual block has measured conductor energy, or they should guide reference/string mining before entropy coding rather than touch every pixel event.

