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
| 3 | soft-moment-prior | 1/4 | 234,608 | +143 | +2,876 | True |
| 4 | soft-moment-prior | 1/2 | 234,841 | +376 | +3,109 | True |
| 5 | inverted-moment-prior | 1/4 | 234,973 | +508 | +3,241 | True |
| 6 | inverted-moment-prior | 1/2 | 235,535 | +1,070 | +3,803 | True |

## Interpretation

The best E30 row is `hard-moment-context` at `229,866` bytes.
The baseline causal Hankel classes were `{'0': 15, '1': 452044, '2': 334373}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.

This is a pass. The causal moment-barrier context beats the E30 baseline by `4,599` bytes and beats WebP lossless by `1,866` bytes, with exact round-trip recovery. The decoded `.sm30` artifact was independently checked against the 512x512 RGB crop byte-for-byte.

The important shape is not "use a smoother prior." The soft moment prior loses, and the inverted prior loses more. The win comes from using the Hankel sign as a no-payload routing variable in the adaptive context. In P6 language: the moment barrier is not a scalar smoothness knob; it is a boundary that separates two residual regimes.

Artifacts:

- best stream: `que-ver-en-costa-rica-correos-portada_512_e30_hard_moment_context_m0-1.sm30`
- recovered image: `que-ver-en-costa-rica-correos-portada_512_e30_hard_moment_context_recovered.png`

