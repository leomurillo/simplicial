# Correos Gap Analysis

Target image:

```text
C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg
```

All numbers below use the 512x512 decoded-RGB center crop.

## Current Real Result

| codec | bytes | vs WebP | recovery |
|---|---:|---:|---|
| WebP lossless | 231,732 | baseline | yes |
| SIGA real, `r-gr-bavg`, `ch-ctx-apex128` | 244,235 | +12,503 (+5.40%) | exact |
| SIGA real, `r-gr-bavg`, `ch-ctx-energy-apex128` | 244,079 | +12,347 (+5.33%) | exact |
| SIGA real, `r-gr-bavg`, `ch-ctx-energy-unitary-apex128` | 247,873 | +16,141 (+6.97%) | exact |

Metadata is not the main cause:

| component | bytes |
|---|---:|
| header + predictor metadata | 789 |
| entropy stream | 243,446 |

The miss is therefore mostly the residual entropy model/backend.

## Estimator Versus Real Backend

The same `r-gr-bavg` residuals in the estimator:

| posterior state | estimate | ideal | new symbols | contexts |
|---|---:|---:|---:|---:|
| `ch-ctx-apex128` | 241,541 | 240,586 | 1,449 | 23 |
| `ch-ctx-grad-apex128` | 240,486 | 238,789 | 2,880 | 76 |
| `ch-ctx-energy-apex128` | 237,997 | 235,995 | 3,235 | 61 |
| `ch-ctx-energy-unitary-apex128` | 237,192 | 233,998 | 5,508 | 159 |
| `ch-ctx-grad-energy-unitary-apex128` | 237,546 | 232,706 | 8,930 | 387 |

Interpretation:

- The first real stream is `2,694` bytes above the matching `ch-ctx-apex128`
  estimate (`244,235` vs `241,541`).
- The best estimated state is `7,043` bytes below the current real stream
  (`237,192` vs `244,235`).
- The best ideal state is only `974` bytes above WebP (`232,706` vs `231,732`).

So Correos is not hopeless. The missing size is in context startup/prior
realization and packet metadata, not in the basic gauge/predictor ladder.

## Channel Cost Split

Winning gauge:

```text
R
G - R
B - floor((R + G) / 2)
```

Estimated residual entropy by channel, no side metadata:

| channel | `ch-ctx-apex128` | `ch-ctx-energy-apex128` | `ch-ctx-energy-unitary-apex128` | best ideal shown |
|---|---:|---:|---:|---:|
| `R` | 111,620 | 109,473 | 109,824 | 106,933 |
| `G-R` | 56,454 | 55,826 | 55,089 | 54,499 |
| `B-floor((R+G)/2)` | 72,685 | 71,629 | 71,018 | 70,013 |

The R/base channel dominates total entropy, but unitary packet routing mostly
helps the two color-residual channels. A single global context recipe is too
coarse.

## Gauge Switching Diagnostic

Whole-image reversible gauge costs under local context-Rice scoring:

| gauge | payload bytes |
|---|---:|
| `r-gr-bavg` | 262,683 |
| `g-rg-bavg` | 264,152 |
| `g-bg-ravg` | 270,318 |
| `ycocg` | 270,584 |
| `b-rb-gavg` | 271,520 |
| `green16` | 292,585 |
| `rgb` | 349,600 |

Per-32x32 whole-tile gauge switching:

| model | bytes |
|---|---:|
| best global gauge payload | 262,683 |
| best whole-tile gauge payload | 261,972 |
| plus 1 gauge byte per tile | 262,228 |
| net gain | 455 |

Whole-tile gauge switching is therefore too weak to close the gap.

But an optimistic per-channel/tile selector gives:

| model | bytes |
|---|---:|
| best global gauge payload | 262,683 |
| per-channel/tile optimistic payload | 247,410 |
| gain before metadata | 15,273 |

That is the large signal. It is not directly reversible as written, but it
points to a native improvement: local conductor/channel sector selection, not
coarse whole-tile color-gauge switching.

## Best Improvement Targets

1. **Exact Apex prior in the real arithmetic coder.**
   The real `ch-ctx` backend is `2,694` bytes above the matching estimate.
   Replace gamma escapes with exact arithmetic coding of the telescoping prior
   `q(n)=1/((n+1)(n+2))`.

2. **Parent-backed side contexts.**
   Energy/unitary contexts look strong in the estimator but cold-start badly in
   the real stream. Use parent posterior blending or fallback coding so fine
   contexts borrow mass from `ch-ctx` instead of restarting from scratch.

3. **Mixed per-channel contexts.**
   Use energy/unitary packet routing mostly for the two color-residual channels,
   while keeping a stabler model for the R/base channel.

4. **Bit-pack metadata.**
   Current predictor ids are one byte per tile. Fixed 5-bit packing saves about
   `288` bytes on 512x512. Entropy coding predictor ids could save more, but
   this is a secondary gain compared with the residual backend.

5. **Local channel-sector gauge.**
   Whole-tile gauge switching only shows about `455` bytes of value. The much
   stronger signal is per-channel/tile sector selection, with an optimistic
   `15,273` byte headroom before metadata. This needs a reversible formulation,
   likely a local retained-sector model plus exact residual certificate rather
   than arbitrary channel mixing.

