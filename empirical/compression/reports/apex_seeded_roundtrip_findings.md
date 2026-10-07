# Apex Seeded Round-Trip Findings

This pass turns the previous Apex-seeded gauge estimate into an actual
decompressible byte stream.

Implemented file:

```text
../apex_seeded_image_codec.py
```

The stream stores:

- SIGA magic/version, dimensions, and RGB CRC;
- image-level reversible gauge id;
- per-tile local predictor ids;
- optional side packet bytes;
- exact residual symbols compressed by adaptive arithmetic coding.

The arithmetic model is native and deterministic:

```text
seen-symbol posterior counts per simplicial context
  + Apex escape mass alpha=128
  + gamma-coded escaped residual integer song
```

The decoder reconstructs the transformed channels from predictors and decoded
residuals, applies the inverse gauge, and checks the CRC.

## Self Test

Command:

```powershell
python empirical\compression\apex_seeded_image_codec.py --self-test
```

Result:

```text
self-test ok
```

## Costa Rica 256x256 Real Round Trip

| file | gauge | scheme | WebP | SIGA real | result | round trip |
|---|---|---|---:|---:|---:|---|
| `que-ver-en-costa-rica-correos-portada.jpg` | `r-gr-bavg` | `ch-ctx-apex128` | 63,034 | 69,318 | +6,284 (+9.97%) | yes |
| `central-valley-san-jose-costa-rica.jpg` | `g-rg-bavg` | `ch-ctx-apex128` | 80,852 | 79,986 | -866 (-1.07%) | yes |

Total:

| total | bytes |
|---|---:|
| WebP lossless | 143,886 |
| SIGA real round-trip | 149,304 |
| gap | +5,418 (+3.77%) |

## Costa Rica 512x512 Real Round Trip

| file | gauge | scheme | WebP | SIGA real | result | encode | decode | round trip |
|---|---|---|---:|---:|---:|---:|---:|---|
| `que-ver-en-costa-rica-correos-portada.jpg` | `r-gr-bavg` | `ch-ctx-apex128` | 231,732 | 244,235 | +12,503 (+5.40%) | 26.17s | 13.41s | yes |
| `central-valley-san-jose-costa-rica.jpg` | `g-rg-bavg` | `ch-ctx-apex128` | 307,430 | 301,384 | -6,046 (-1.97%) | 26.12s | 13.95s | yes |

Total:

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| SIGA real round-trip | 545,619 |
| gap | +6,457 (+1.20%) |

Artifacts written:

- `apex_roundtrip_correos_512.siga`
- `apex_roundtrip_correos_512_recovered.png`
- `apex_roundtrip_central_512.siga`
- `apex_roundtrip_central_512_recovered.png`

## Interpretation

We now have the real recovery contract:

```text
decode(encode(decoded RGB crop)) == decoded RGB crop
```

Both 512 crops passed byte equality and CRC validation.

The estimate still beats WebP (`531,616` bytes vs `539,162`), but the first real
bitstream lands at `545,619` bytes. The gap comes from two honest costs that
the estimate treated optimistically:

- actual arithmetic escape coding is cruder than the ideal seeded posterior;
- side decisions are byte-stored rather than bit-packed or jointly modeled.

The important practical result is that the central-valley crop is already a
real lossless win over WebP:

```text
301,384 vs 307,430 bytes, exact recovery
```

The hard Correos crop still needs the next backend improvement.

## Next Target

Make the real stream match the estimator more closely:

1. Replace gamma escapes with an arithmetic implementation of the exact
   telescoping Apex prior `q(n)=1/((n+1)(n+2))`.
2. Bit-pack predictor and side packet metadata.
3. Add decoder-visible or bit-packed row-gradient contexts for the central
   `ch-ctx-grad` state.
4. Re-test per-region gauge selection only after metadata packing is in place.

