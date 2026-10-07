# Reversible Transform-Stack POC

## What was implemented

`empirical/compression/transform_stack_poc.py` adds a separate experimental
stream format with magic `SGST`.

The stack is:

1. choose a local reversible color gauge command over coarse tile regions;
2. apply the selected triangular/integer channel lift per 32px tile;
3. build the existing predictor residual planes;
4. entropy-code the exact residual tail with the Apex arithmetic backend;
5. decode residuals, expand the command map, invert each local gauge, and
   verify the RGB CRC.

This is a native proof of concept for the T0/T4 transform grammar: the codec
does not assume one universal additive coordinate system. It stores a small
command map that says which reversible gauge is active over each region.

## Correos 512 benchmark

Input:

`C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg`

Crop:

center 512x512 RGB, raw size `786,432` bytes.

Scheme:

`ch-ctx-energy-unitary-split-blend71-apex128`

Candidate gauges:

`r-gr-bg`, `r-gr-bavg`, `g-rg-bavg`, `g-bg-ravg`, `ycocg`, `rgb`

| codec | bytes | vs WebP | recovery | note |
|---|---:|---:|---|---|
| WebP lossless | 231,732 | baseline | yes | Pillow/WebP method 6 |
| native SIGA best prior | 234,462 | +2,730 | yes | global `r-gr-bg` |
| SGST span 8 | 234,472 | +2,740 | yes | collapsed to global `r-gr-bg` |
| SGST span 4 | 234,570 | +2,838 | yes | real multi-gauge command map |
| SGST span 1, naive | 236,907 | +5,175 | yes | too much gauge flicker |

The best POC stream is:

`empirical/compression/reports/que-ver-en-costa-rica-correos-portada_512_stack_s8.sgst`

The recovered image is:

`empirical/compression/reports/que-ver-en-costa-rica-correos-portada_512_stack_s8_recovered.png`

The multi-gauge POC stream is:

`empirical/compression/reports/que-ver-en-costa-rica-correos-portada_512_stack_s4.sgst`

The recovered image is:

`empirical/compression/reports/que-ver-en-costa-rica-correos-portada_512_stack_s4_recovered.png`

## What the experiment says

The reversible transform stack works: `SGST` round-trips exactly and the CRC
guards the final RGB output.

The first naive local stack was too local. Switching gauges every 32px tile made
neighboring residual planes change semantics too often, and the entropy model
paid for that discontinuity.

Coarser commands are the right shape. Span 4 selected three gauges:

| gauge | tile count |
|---|---:|
| `r-gr-bg` | 192 |
| `g-rg-bavg` | 32 |
| `r-gr-bavg` | 32 |

Span 8 chose `r-gr-bg` everywhere, which explains why it lands almost exactly
on the previous best native global-gauge codec plus a small stack header.

## Next native improvement

The next useful step is not more transforms. It is a better command scorer:

1. price the mixed-gauge boundary entropy during selection, not after;
2. allow inherited commands plus sparse exceptions instead of a fixed grid;
3. add a transported-patch command over the transformed residual planes;
4. let the posterior context include the current gauge command so local gauges
   do not share cold-start statistics blindly.

That would make the stack behave like a real simplicial command language rather
than a coarse transform selector bolted in front of the existing stream.
