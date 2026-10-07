# E31 Regret-Governed Moment Gate Findings

E31 answers the failure mode exposed by E30. The hard Hankel/moment gate is useful, but a hard split can fragment small contexts before there is enough evidence. E31 therefore treats the split as an expert, not as an always-on rule.

The codec keeps two synchronized entropy experts:

- baseline expert: native Apex context key
- moment expert: Hankel class prepended to the native key

Both experts are updated on every decoded symbol. The actual arithmetic stream follows the moment expert only when the past regret score exceeds a fixed causal threshold. The decoder computes the same score from previous decoded symbols, so no gate payload is transmitted.

Run configuration:

- mode: `regret-global`
- activation threshold: `512` bits
- warmup: `2048` symbols
- transform: `r-gr-bg`
- scheme: `ch-ctx-energy-unitary-split-blend71-apex128`

## 512 Panel

| image | WebP | E30 baseline | E30 hard | E31 governed | E31 vs baseline | E31 vs hard | E31 vs WebP |
|---|---:|---:|---:|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 231,732 | 234,465 | 229,866 | 229,933 | -4,532 | +67 | -1,799 |
| central-valley-san-jose-costa-rica.jpg | 307,430 | 298,811 | 298,588 | 298,655 | -156 | +67 | -8,775 |
| 133925289798805247.jpg | 306,272 | 286,705 | 287,475 | 286,708 | +3 | -767 | -19,564 |
| 133893333653186297.jpg | 489,474 | 481,109 | 482,507 | 481,112 | +3 | -1,395 | -8,362 |
| 133921439458600606.jpg | 505,660 | 486,804 | 487,827 | 486,807 | +3 | -1,020 | -18,853 |

All E31 roundtrips were true.

At 512, E31 keeps the two hard-gate wins while avoiding all three satellite-control regressions. Where hard is useful, E31 trails hard by `67` bytes: `64` bytes from the 512-bit activation threshold plus roughly `3` bytes of SM31 header/config overhead. Where hard is harmful, E31 trails baseline by only `3` bytes.

## 1024 Stress Panel

| image | WebP | E30 baseline | E30 hard | E31 governed | E31 vs baseline | E31 vs hard | E31 vs WebP |
|---|---:|---:|---:|---:|---:|---:|---:|
| que-ver-en-costa-rica-correos-portada.jpg | 975,520 | 961,567 | 947,176 | 947,243 | -14,324 | +67 | -28,277 |
| central-valley-san-jose-costa-rica.jpg | 1,142,164 | 1,087,964 | 1,085,582 | 1,085,649 | -2,315 | +67 | -56,515 |
| 133925289798805247.jpg | 1,324,414 | 1,217,366 | 1,216,896 | 1,216,963 | -403 | +67 | -107,451 |

All E31 roundtrips were true.

At 1024, E30 hard is beneficial for all three tested crops, and E31 follows it after the regret score crosses threshold. Again the cost is exactly the governance price: `67` bytes.

## Gate Diagnostics

| image | crop | hard expert advantage | chosen vs baseline | selected baseline | selected hard |
|---|---:|---:|---:|---:|---:|
| Correos | 512 | 36,790.6 bits | 36,276.9 bits | 40,138 | 746,294 |
| Central Valley | 512 | 1,783.0 bits | 1,268.3 bits | 604,942 | 181,490 |
| Satellite 133925 | 512 | -6,159.6 bits | 0.0 bits | 786,432 | 0 |
| Satellite 133893 | 512 | -11,180.2 bits | 0.0 bits | 786,432 | 0 |
| Satellite 133921 | 512 | -8,182.5 bits | 0.0 bits | 786,432 | 0 |
| Correos | 1024 | 115,122.6 bits | 114,610.3 bits | 117,416 | 3,028,312 |
| Central Valley | 1024 | 19,060.8 bits | 18,542.8 bits | 508,565 | 2,637,163 |
| Satellite 133925 | 1024 | 3,758.9 bits | 3,246.1 bits | 2,908,232 | 237,496 |

The governed model behaves like a causal expert selector. It does not need to know the image class. It only waits until the moment split has earned its activation cost.

## Conclusion

E31 is stronger than E30 as a codec principle.

E30 proved that the Hankel/moment barrier is a real compression signal. E31 proves that the signal can be governed causally: activate it when it is useful, suppress it when it is unresolved, and do so without transmitting an external gate map.

In Lamed-series language, this is boundary governance made computational. A boundary packet is not always admitted merely because it exists. It is admitted when its retained-sector contribution has paid for its projection cost.

## Next Target

E32 should make the governance local rather than only global. The natural next step is a multi-scale regret gate:

- global score for broad image-level activation
- channel score for color-sector differences
- context-family score for local texture/edge regimes
- maturity penalty so sparse local gates cannot fragment too early

The target is to beat `min(E30 baseline, E30 hard)` more often, not merely trail it by a fixed threshold.

