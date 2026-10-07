# T0-Inspired Compression Notes

T0's core sentence is the compression question:

> A statistical theory begins by answering: what is additive?

For SIGI, this becomes:

> A compressor begins by answering: in which gauge is this block simple?

## 1. Gauge Choice Is the Model

Current SIGI tries a few fixed gauges:

- `YCoCg`
- `G, R - G/2, B - G`
- `G, B - G, R - floor((G+B)/2)`

T0 says this should be a corridor, not a menu. For each tile, choose an additive substance:

- arithmetic: raw pixel/channel differences are additive
- geometric/log: ratios and illumination are additive
- quadratic/RMS: energy or contrast is additive
- harmonic/inverse: dark detail and reciprocal intensity are additive
- tropical/max-min: edges, plateaus, and clipped regions are additive by support

Practical codec move: per tile, evaluate several gauge families and store a small gauge id. The winner is the one minimizing estimated coded residual size.

## 2. Centered Log-Ledger as Tile Signature

T0's universal coordinate is the centered log-ledger

```text
y_i = log(x_i + epsilon) - mean(log(x + epsilon))
```

For an image tile, this removes the illumination scale. The apex generator

```text
K_y(beta) = log mean(exp(beta y_i))
```

becomes a cheap feature vector:

- `K(+1), K(-1)` distinguish bright-dominant vs dark-dominant tiles
- even/odd split detects symmetric texture vs skewed highlights/shadows
- large-beta limits detect clipped or edge-dominated support
- low cumulants detect smooth/gentle regions

Practical codec move: use `K_y(beta)` samples to choose predictor family, color gauge, and entropy context.

## 3. Fourier-Mellin Blocks

T0 upgrades the scalar apex to

```text
M_x(beta, c) = mean_s exp(beta y_s) conjugate(chi_c(s))
```

For image tiles, labels are spatial positions. Use a 2D finite character basis on `Z/w x Z/h`.

Practical codec move: compute low-order Fourier-Mellin packet energies for each tile:

- DC/low frequency: smooth field, use plane or gradient predictor
- row/column packet: separable horizontal/vertical structure
- mixed packet: texture/corner/detail
- high conductor packet: noise or JPEG artifact field

Then encode low packets as the song and entropy-code only the high-conductor residual.

## 4. ANOVA/CRT Decomposition

T0's separability theorem says mixed terms are the non-factorizing content. For an image tile:

```text
tile(x,y) = mean + row_effect(x) + col_effect(y) + mixed_residual(x,y)
```

This is exactly a compression structure:

- encode row and column effects cheaply
- encode mixed residual only when needed
- skip this mode when mixed residual entropy is high

This may help sky, building facades, horizons, roads, water, and city grids.

## 5. New SIGI Modes To Try

Priority order:

1. `anova-ctx-rice`
   - For each transformed channel tile, subtract mean + row effect + column effect.
   - Store quantized row/column ledgers plus exact residuals.

2. `fourier-lowpack-ctx-rice`
   - Keep a small set of low Fourier coefficients.
   - Reconstruct a smooth song, then code exact integer residuals.

3. `beta-gauge-search`
   - For positive shifted ledgers, test beta gauges such as `-2, -1, 0, 1, 2, 3`.
   - Choose the gauge minimizing residual entropy.

4. `apex-classified-entropy`
   - Use `K_y(beta)` features to select context tables.
   - Move from Rice to rANS/arithmetic once the context split is stable.

## 6. Best Next Experiment

The next smallest useful POC is ANOVA tile residual coding:

```text
for each tile/channel:
    choose color gauge
    compute mean, row means, column means
    predict = mean + row_effect + col_effect
    residual = original - round(predict)
    compare estimated residual bits against current predictor mode
```

This is faithful to T0: it asks what decomposes additively before asking how to entropy-code the leftovers.
