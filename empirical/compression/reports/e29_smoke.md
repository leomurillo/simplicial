# E29 Ramanujan Transfer Prior

E29 tests the P5 reading in codec form: the conductor boundary should govern the entropy prior without being transmitted as a dense command map.

## que-ver-en-costa-rica-correos-portada.jpg

- crop: `64x64` RGB
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`
- conductor modulus: `30`
- WebP lossless: `6,032` bytes
- E29 baseline: `5,899` bytes

| rank | model | mix | rung mode | bytes | vs E29 baseline | vs WebP | roundtrip |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | baseline | 0/1 | tile | 5,899 | +0 | -133 | True |
| 2 | soft-ramanujan | 1/2 | tile | 5,903 | +4 | -129 | True |
| 3 | shuffled-ramanujan | 1/2 | tile | 5,958 | +59 | -74 | True |
| 4 | hard-rung-context | 0/1 | tile | 5,983 | +84 | -49 | True |

## Interpretation

The best E29 row is `baseline` with mix `0/1` and rung mode `tile`, at `5,899` bytes.

The key comparison is against both the baseline and the shuffled control. A genuine Ramanujan-transfer effect should beat the baseline and also beat a prior with the same mass histogram assigned to the wrong conductor packets.

