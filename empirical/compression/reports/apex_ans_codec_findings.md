# Apex-ANS Codec Findings

This is the first native analog of `rANS/adaptive-context` in the simplicial compression program.

The front-end remains SIGI's reversible gauge and local predictor:

```text
RGB -> gauge channels -> per-tile predictor -> exact residual symbols
```

The backend is replaced by an adaptive apex-state entropy estimate:

```text
context = channel x residual-gradient-context
symbol  = zigzag(residual)
model   = deterministic counts updated after every decoded symbol
```

For a seen symbol, the coder pays `-log2(count/(total+1))`. For a new symbol, it pays an escape plus a varint literal. This is implementable as a real range/rANS stream and requires no stored per-image codebook.

## Costa Rica 512x512 Raw-RGB Crops

Each JPG is decoded to RGB first. WebP lossless and Apex-ANS are both measured on those exact decoded pixels.

| file | WebP lossless | Apex-ANS | best native state | result |
|---|---:|---:|---|---:|
| central-valley-san-jose-costa-rica.jpg | 307,430 | 307,000 | `g-bg-ravg/ch-ctx` | -430 (-0.14%) |
| que-ver-en-costa-rica-correos-portada.jpg | 231,732 | 253,505 | `g-bg-ravg/ch-ctx` | +21,773 (+9.40%) |

Totals:

- WebP lossless: `539,162`
- Apex-ANS feasible estimate: `560,505`
- Apex-ANS vs WebP: `+21,343` bytes (`+3.96%`)

The ideal no-codebook ceiling for the same native context family is:

- ideal Apex entropy: `538,166`
- ideal vs WebP: `-996` bytes (`-0.18%`)

## Interpretation

This is the first clean evidence that the native program can reach WebP territory without borrowing WebP's bitstream. The adaptive model already beats WebP on the central crop. The total model ceiling beats WebP, but the feasible escape/adaptation friction leaves a 3.96% gap.

The hard case is the Correos image. Its ideal entropy is still `243,069` bytes, which is `+11,337` bytes over WebP, so entropy modeling alone is not enough there.

## Next Program Move

The next native codec needs two layers:

1. **Apex-ANS backend**
   - implement the adaptive count model as an actual range/rANS coder;
   - preserve the winning `g-bg-ravg/ch-ctx` low-friction context;
   - add carefully pooled higher contexts only when their escape cost is amortized.

2. **Transported song / copy gauge front-end**
   - WebP's remaining advantage on Correos is likely LZ/reference structure;
   - native analog: store a reference tile plus a small transport/correction, then entropy-code the exact residual;
   - candidate transports: shift, same-row copy, small affine luminance correction, conductor-packet correction.

So the elevated version of WebP is:

```text
transported gauge song + exact residual + adaptive apex-state entropy
```

not `DCT coefficients` or `LZ` as external primitives.

## 2026-05-28 Update

The transported-song follow-up is now implemented in
`benchmark_transported_kummer_vs_webp.py`; see
`transported_kummer_codec_findings.md`.

The strongest Costa Rica 512x512 estimate improved the two-image gap from
`+21,343` bytes (`+3.96%`) to `+14,191` bytes (`+2.63%`) by adding a compact
residual-energy context. Whole-tile Kummer transport itself was effectively
neutral: it accepted only three transported residual tiles and tied the
non-transported baseline.

## T10 Correction: Use The Whole Native Ladder

T10 makes the word "native" much larger than a residual entropy backend. The codec should use the full Kummer gauge corridor:

```text
m in {-4,-3,-2,-1,0,1,2,3,4} plus tropical limits
```

Each rung is a possible additive substance for a tile: raw, log/geometric, RMS/Born, cubic, quartic, harmonic, inverse-square, inverse-cubic, and max/min support.

A quick direct test added a Kummer-corridor tile class as an Apex-ANS context. It did not help the feasible estimate:

| file | best Apex-ANS | + direct Kummer class |
|---|---:|---:|
| central-valley-san-jose-costa-rica.jpg | 307,000 | 307,519 |
| que-ver-en-costa-rica-correos-portada.jpg | 253,505 | 254,864 |

The lesson is architectural: Kummer state should not be spent as a high-cardinality per-symbol context. It should select tile gauges, transported-song candidates, and pooled entropy priors.

See `native_simplicial_codec_program.md` for the all-native stack.
