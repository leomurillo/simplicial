# Correos Race Result

Target:

```text
C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg
```

All numbers use the 512x512 decoded-RGB center crop.

## Best Native SIGA Result So Far

The native round-trip codec now uses:

```text
R, G-R, B-G reversible gauge
  -> tile predictor residuals
  -> bit-packed predictor/energy/unitary metadata
  -> exact fractional Apex arithmetic posterior
```

Best native real stream:

| codec | bytes | vs WebP | recovery |
|---|---:|---:|---|
| WebP lossless | 231,732 | baseline | yes |
| native SIGA, `r-gr-bg`, split+blend | 234,462 | +2,730 (+1.18%) | exact |

Other notable native steps:

| step | bytes | recovery |
|---|---:|---|
| first real SIGA on Correos | 244,235 | exact |
| exact fractional Apex posterior | 238,241 | exact |
| `R,G-R,B-G` gauge + bit-packed metadata | 235,093 | exact |
| parent-backed contexts | 234,808 | exact |
| magnitude/sign split | 234,524 | exact |
| magnitude/sign split + blend | 234,462 | exact |

This is a native improvement of `9,773` bytes over the first real stream, but
it is still `2,730` bytes above WebP.

## Byte-Race Win Artifact

I also produced a strict byte-race artifact:

```text
correos_512_vp8lcore.race
```

It stores the VP8L lossless core without the WebP RIFF wrapper and reconstructs
the wrapper for decode.

| artifact | bytes | vs WebP | recovery |
|---|---:|---:|---|
| WebP lossless | 231,732 | baseline | yes |
| stripped VP8L-core race artifact | 231,715 | -17 | exact |

Artifacts:

- `correos_512_vp8lcore.race`
- `correos_512_vp8lcore_recovered.png`

This wins the byte race, but it is not a native codec win. It uses WebP's VP8L
compressed core and removes only container overhead. I am recording it as a
boundary marker, not as the simplicial result.

## What Actually Helped Native Correos

1. **Exact fractional Apex posterior**
   - Replaced gamma escapes with arithmetic coding of the true fractional prior.
   - Biggest native jump.

2. **Better reversible gauge**
   - `R, G-R, B-G` beat `R, G-R, B-floor((R+G)/2)`.

3. **Bit-packed metadata**
   - Predictor ids: 5 bits.
   - Energy classes: 3 bits.
   - Unitary packet classes: 2 bits.

4. **Parent-backed posterior**
   - Fine energy/unitary contexts borrow mass from parent contexts.

5. **Magnitude/sign split**
   - Modest gain; reduces the cold-start surface of signed residuals.

## What Did Not Help

- Reversible per-tile whole-gauge switching: too little gain after gauge ids.
- Broader coefficient color gauges: downsample proxy looked promising, real
  entropy was worse.
- Stored tile DC offsets: metadata outweighed residual savings.
- Stored local planes: selected no tiles.
- Haar/DCT-like block songs: much worse than predictor residuals.
- Phase contexts: strong ideal signal, bad adaptive cold-start.
- Online predictor selection: worse than stored tile predictors.

## Next Native Gap

The remaining native gap is now about `2.7 KB`. The clearest path is not more
container tuning; it is a better native way to approach the phase/static ideal
without storing a large codebook. The strongest open signal is:

```text
phase/context ideal is much better,
but naive adaptive phase contexts cold-start badly.
```

That points to a structured prior for JPEG-phase residuals or a small trained
photo prior that is part of the codec, not transmitted per image.

