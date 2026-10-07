# Transported Kummer Codec Findings

This pass implemented the native reference/copy experiment:

```text
Kummer tile class -> transported prior song -> exact residual tail -> Apex-ANS estimate
```

The compressor decodes each image to RGB, applies the reversible `g-bg-ravg`
gauge, predicts each channel tile locally, and then tries previous
Kummer-compatible tiles as references. Two transported forms are tested:

- raw tile transport: shifted, affine-corrected prior tile;
- residual transport: shifted, affine-corrected prior residual song over the
  current local predictor.

The entropy backend now also tries a low-cardinality residual-energy state.
That was the real gain in this pass.

## Costa Rica 512x512 Result

| file | WebP | best native estimate | best state | ideal | result |
|---|---:|---:|---|---:|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 231,732 | 250,198 | `ch-ctx-energy` | 245,546 | +18,466 (+7.97%) |
| `central-valley-san-jose-costa-rica.jpg` | 307,430 | 303,155 | `ch-ctx-grad` | 297,090 | -4,275 (-1.39%) |

Totals:

- WebP lossless: `539,162` bytes
- Transported Kummer + Apex-ANS estimate: `553,353` bytes
- Result vs WebP: `+14,191` bytes (`+2.63%`)
- Ideal no-codebook ceiling: `542,636` bytes
- Ideal vs WebP: `+3,474` bytes (`+0.64%`)

## What Improved

The new residual-energy context reduced the hard Correos estimate from the
previous `253,368` bytes to `250,198` bytes. The valley image still prefers
the gradient context at `303,155` bytes.

This says the Apex posterior should keep a small menu of pooled context states
and choose the cheapest stream. The useful state is not a big symbolic Kummer
class per residual. It is a compact local gauge of residual volatility.

## What Failed

Whole-tile Kummer transport is currently too coarse. On the 512 crops it
accepted only three transported tiles total:

- Correos: 2 transported residual tiles, saving only 3 local-score bytes.
- Central valley: 1 transported residual tile, saving only 2 local-score bytes.

After full entropy estimation, transported Kummer tied the non-transported
baseline exactly. The local predictors already remove most tile-level structure,
and a whole 32x32 tile reference is too expensive unless the match is excellent.

## Interpretation

The native stack is still viable, but this experiment changes where to spend
effort:

```text
keep:    reversible gauge + local predictor + compact adaptive Apex state
discard: whole-tile transported songs as the primary copy mechanism
next:    sub-tile conductor strings and real rANS/Apex-ANS implementation
```

The WebP gap on these two images is now mostly copy/string structure and
adaptive-coding friction, not color gauge or first-order prediction.

## Next Development Target

Build a sub-tile transported residual codec:

1. Keep the current `g-bg-ravg` gauge and per-tile local predictor.
2. Break residual planes into smaller conductor strings: rows, 4x4 patches, or
   short Hilbert/Z-order paths.
3. Search prior nearby residual strings with the Kummer/energy class as a
   candidate filter.
4. Store compact string references only when they beat direct residual coding.
5. Implement the winning `ch-ctx-energy` / `ch-ctx-grad` adaptive model as a
   real range/rANS stream.

That is the native analog of WebP's LZ transform, but expressed as transported
residual songs rather than byte copies.

