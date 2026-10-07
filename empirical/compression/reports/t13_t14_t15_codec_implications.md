# T13-T15 Codec Implications

This note studies T13, T14, and T15 as compression engineering guidance.

The central lesson is that a native codec should not treat residuals as an
embarrassing leftover. In the T13-T15 language, residuals are boundary
certificates: the exact finite data needed when a retained model/projection is
not closed.

## T13: Compression As Exact Boundary Accounting

T13's key compression reading:

```text
retained packet model + boundary source = exact finite theory
```

For a codec:

- The predictor/gauge/context model is the retained sector `S`.
- The residual stream is the conductor-fusion boundary `partial S`.
- Losslessness means the boundary is not discarded; it is encoded exactly.
- Better compression means choosing `S` so the encoded boundary is small.
- A model is "renormalizable" for the data when its effective boundary closes
  in a small finite coordinate algebra.

This explains why a compact residual-energy context helped the hard Correos
image: it did not create a huge new symbolic split. It adjoined one useful
boundary coordinate to the retained entropy sector.

T13 also warns against oversplitting contexts. A high-cardinality Kummer class
as a per-symbol context made the adaptive posterior pay too many new-symbol
escapes. That is a nonclosed projection made worse, not better.

## T14: Curvature Is Projection Failure

T14's key compression reading:

```text
lift -> linear/simple model
project -> residual curvature
```

The useful codec rule is:

```text
residual energy = observed curvature of the chosen projection
```

For images, the `g-bg-ravg` gauge plus local predictor is the lifted flat
attempt. When the local projection commutes with the image structure, residuals
are small. When it does not, the residual has curvature/texture. That curvature
should route the entropy state.

This gives a native justification for:

- gradient contexts: boundary caused by spatial nonflatness;
- residual-energy contexts: boundary magnitude after projection;
- sub-tile strings: curvature is local, not whole-tile;
- Schur-like corrections: small pooled context additions are often better than
  huge new context partitions.

The whole-tile Kummer transport result fits T14 exactly. A 32x32 transported
tile is too coarse a projection. The boundary curvature lives in smaller
strings/patches, so the transport rarely commutes with the actual data.

## T15: Compression As A Refinement-Compatible Tower

T15's key compression reading:

```text
finite closure + refinement compatibility + terminal bit boundary
= completed codec
```

A codec should therefore be designed as a refinement tower, not a bag of
isolated transforms:

```text
image
  -> 32x32 tile packets
  -> 16x16 / 8x8 / 4x4 refinement packets
  -> row/path conductor strings
  -> exact residual boundary
  -> arithmetic bitstream completion
```

Refinement compatibility means old packet decisions must remain meaningful when
the compressor descends to smaller packets. New packets should be explicitly
marked as refinement boundaries, not silently mixed into unrelated contexts.

This points directly at the next experiment:

```text
sub-tile transported residual strings + Apex posterior coding
```

Whole-tile transport was too blunt. T15 says the next packets should be the
genuinely new refinement modes: rows, 4x4 patches, Hilbert/Z-order paths, or
conductor packet strings.

## Is Apex-ANS Native?

Yes, if framed correctly.

The native object is not "rANS" as an external compression brand. The native
object is:

```text
finite categorical posterior over residual cells
```

Each context owns a simplex of residual-symbol probabilities:

```text
p_s = (count_s + prior_s) / total
```

Encoding a symbol selects a simplex face and pays the log-volume cost
`-log2(p_s)`. Updating the model is a deterministic finite posterior step.

The arithmetic/rANS layer is the terminal bitstream completion: it turns the
finite posterior into actual bits with integer renormalization. In T15 terms,
the finite posterior model is not a complete compressed object until its
real/metric code-length boundary is supplied.

So the all-native phrase should be:

```text
Apex posterior coder with rANS-style integer renormalization
```

not:

```text
borrow WebP's entropy model
```

## Codec Certificate From T13-T15

A native lossless stream should carry enough data to answer four certificate
questions:

1. **Retained sector:** Which gauge, predictor, context, and packet family were
   retained?
2. **Boundary exactness:** What residual/boundary stream restores the exact
   discrete bytes?
3. **Refinement compatibility:** If a packet was refined, what new boundary
   packet was introduced?
4. **Bit completion:** Which deterministic Apex posterior and integer
   arithmetic coder map the finite probabilities to bits?

If those four are present, decompression is native and exact:

```text
retained reconstruction + decoded boundary = original discrete file
```

## Implementation Consequences

For the next practical version:

- Keep the `g-bg-ravg` reversible gauge.
- Keep local tile predictors as the first retained sector.
- Keep small pooled entropy states: `ch-ctx-grad` and `ch-ctx-energy`.
- Stop treating whole-tile Kummer transport as the main copy tool.
- Add sub-tile transported residual strings as refinement-boundary packets.
- Implement the Apex posterior as the model and rANS/range coding as the
  terminal integer bitstream completion.

This is a sharper all-native stack:

```text
gauge lift
  -> retained local projection
  -> curvature/boundary certificate
  -> refinement-compatible transported strings
  -> finite Apex posterior
  -> integer bitstream completion
```

