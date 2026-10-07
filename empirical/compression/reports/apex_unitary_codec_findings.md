# Apex Unitary Codec Findings

This pass studies `N1-ApexUnitaries-Draft1.md` as compression guidance.

N1's codec reading is:

```text
Helmert/local contrast coordinates
  <-> apex unitary
  <-> character/conductor packet coordinates
```

For images, that suggests a small stored packet class: after local prediction,
ask where the residual tile's energy lives in conductor/Fourier packets. That
packet class can route the Apex posterior or later mine reference strings.

## What Was Implemented

`../benchmark_subtile_transport_vs_webp.py` now computes an N1-inspired
`unitary_packet_class` per predictor tile:

- class `0`: near-flat residual tile;
- class `1`: low conductor / low-frequency energy dominant;
- class `2`: mid conductor energy dominant;
- class `3`: high conductor / texture energy dominant.

When an entropy context uses this class, the estimate charges 2 stored side
bits per predictor tile. This keeps the test honest: the decoder cannot know
the residual tile's spectral packet before decoding unless the packet id is
stored.

## Costa Rica 512x512 Result

Best deployed run:

```powershell
python empirical\compression\benchmark_subtile_transport_vs_webp.py `
  --direct-only --crop-size 512 --block-size 32 `
  --json empirical\compression\reports\apex_unitary_context_costa_rica_512_b32.json `
  --report empirical\compression\reports\apex_unitary_context_costa_rica_512_b32.md `
  C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg `
  C:\Users\leomu\Downloads\central-valley-san-jose-costa-rica.jpg
```

| file | WebP | deployed native | best feasible state | ideal best state | ideal | result |
|---|---:|---:|---|---|---:|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 231,732 | 250,486 | `ch-ctx-energy` | `ch-ctx-grad-energy-unitary` | 243,827 | +18,754 (+8.09%) |
| `central-valley-san-jose-costa-rica.jpg` | 307,430 | 303,155 | `ch-ctx-grad` | `ch-ctx-grad-energy-unitary` | 296,140 | -4,275 (-1.39%) |

Totals:

- WebP lossless: `539,162` bytes
- deployed feasible native estimate: `553,641` bytes
- feasible vs WebP: `+14,479` bytes (`+2.69%`)
- ideal no-codebook with N1 unitary packet class: `539,967` bytes
- ideal vs WebP: `+805` bytes (`+0.15%`)

## Interpretation

N1 unitary packet side information is real signal. It improved the ideal
ceiling from the prior `543,211` bytes (`+0.75%` vs WebP) to `539,967` bytes
(`+0.15%` vs WebP), a gain of `3,244` ideal bytes.

But the feasible adaptive stream did not select the unitary contexts. The best
feasible states remain:

- Correos: `ch-ctx-energy`
- Central valley: `ch-ctx-grad`

The unitary contexts split the posterior too much early in the stream, so
new-symbol escape friction eats the theoretical gain.

## Blended Posterior Check

I also tested a parent-prior blend where fine unitary contexts borrow
probability mass from coarser contexts instead of cold-starting. On the 256
smoke crop it was still worse than the existing feasible states:

- Correos best blended: `70,096` bytes vs deployed `69,678`
- Central valley best blended: `79,649` bytes vs deployed `78,958`

So the current adaptive one-pass posterior should not use unitary packets as
live fine contexts.

## Next Use Of N1

The unitary packet class should move one level up:

1. **Static/two-pass model selection:** use unitary packets for a stored static
   model or table only when the whole-image codebook cost is repaid.
2. **Reference mining:** use unitary packet ids as a filter for row/path
   residual-string copies.
3. **Block family selection:** use unitary packet id to choose between direct
   residual, DC correction, row copy, path copy, or future conductor-string
   transport.

In short:

```text
N1 packet classes are excellent for compression decisions,
but too expensive as naive one-pass residual contexts.
```

