# Native Simplicial Codec Program

Yes: the native program is larger than "DCT-like packets plus rANS-like entropy." That phrasing was useful for comparison with WebP, but the actual architecture should be the full T-series ladder.

## Native Pieces Already Available

| role in codec | native object | source |
|---|---|---|
| exact lossless contract | rounding cells / snapped residuals | T4/T15 direction |
| local contrasts | Helmert ladder | T4 |
| gauge search | power-mean / apex corridor | T0 |
| harmonic/RMS/polar pairs | reciprocal and quadratic gauges | T5/T6 |
| cubic/quartic interaction | m-fold conductor selection | T3/T10 |
| conductor coordinates | Helmert-Fourier transfer `U_kc` | T9 |
| m-power arithmetic ambient | Kummer clock `K_N^(m)` | T10 |
| complex/deck phase structure | Kummer cover / deck character | T7/T10 |
| entropy state | adaptive apex posterior | Apex-ANS POC |
| reference/copy structure | transported song / closure reuse | native analog of LZ |
| exact residual accounting | boundary source / fusion closure | T13 |
| residual routing | projected curvature / projection noncommutation | T14 |
| multi-scale packet design | refinement-compatible completion tower | T15 |
| spectral packet routing | apex unitary / Helmert-character transfer | N1 |

## The Real Native Codec Stack

The full native analog of WebP should be:

```text
Kummer gauge selection
  -> Helmert/conductor packet song
  -> transported closure reuse
  -> exact residual tail
  -> Apex-ANS adaptive entropy
```

This is not JPEG/DCT/rANS copied inward. It is the T-series read as an image codec:

- **T10 Kummer corridor** chooses which substance is additive:
  `m = -4, -3, -2, -1, 0, 1, 2, 3, 4`, plus tropical limits.
- **T9 transfer** says where the tile energy lives in conductor packets.
- **T4 Helmert** supplies reversible dimensional contrasts.
- **T3/T10 m-fold rules** identify nonlinear interaction content.
- **T5/T6 polar pairs** test direct vs reciprocal descriptions.
- **Apex-ANS** codes the residual with an adaptive posterior.

## Compression Interpretation of T10

For each tile, do not assume pixels themselves are the additive substance. Test a small gauge corridor:

| rung | codec meaning |
|---:|---|
| `m=1` | raw mass/intensity gauge |
| `m=2` | RMS/Born/energy gauge |
| `m=3` | cubic chirality/skew gauge |
| `m=4` | quartic tail/highlight gauge |
| `m=0` | log/geometric illumination gauge |
| `m=-1` | harmonic/shadow gauge |
| `m=-2` | inverse-energy/compliance gauge |
| `m=-3` | inverse-cubic shadow-tail gauge |
| `+/-infinity` | tropical support/max-min gauge |

The compressor should store a compact gauge id, then code a song plus exact residual:

```text
tile = lift(song in chosen m-gauge) + residual
```

The decompressor only needs the gauge id, song parameters, and residual stream.

## Direct Kummer Context Check

I tested a direct Kummer-corridor tile class as an extra Apex-ANS context on the two Costa Rica 512 crops.

| file | best Apex-ANS | with direct Kummer class | result |
|---|---:|---:|---:|
| `central-valley-san-jose-costa-rica.jpg` | 307,000 | 307,519 | worse by 519 |
| `que-ver-en-costa-rica-correos-portada.jpg` | 253,505 | 254,864 | worse by 1,359 |

That does **not** mean T10 is unhelpful. It means the Kummer state is too valuable to spend as a per-symbol context splitter, because it creates too many new-symbol escapes. It should be used one level higher:

- choose the tile gauge;
- choose predictor family;
- choose whether to attempt transported song reuse;
- choose a pooled entropy prior.

## Transported Kummer Result

The first Transported Kummer Song + Apex-ANS benchmark is implemented in `../benchmark_transported_kummer_vs_webp.py`; see `transported_kummer_codec_findings.md` and `transported_kummer_vs_webp_costa_rica_512.md`.

On the two Costa Rica 512x512 raw-RGB crops:

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| transported Kummer + Apex-ANS | 553,353 |
| gap | +14,191 (+2.63%) |
| ideal no-codebook ceiling | 542,636 (+0.64%) |

The important negative result: whole-tile transported songs almost never pay. Only three transported residual tiles were accepted across both 512 crops, and the final entropy estimate tied the non-transported baseline. The useful gain came instead from a compact residual-energy context, `ch-ctx-energy`, which improved the hard Correos crop from `253,368` bytes to `250,198` bytes.

## T13-T15 Correction

T13-T15 sharpen the codec architecture; see
`t13_t14_t15_codec_implications.md`.

The residual stream should be read as an exact boundary certificate, not as an
implementation failure:

```text
retained model + encoded boundary = exact file
```

T14 explains why residual-energy routing helped: after a lifted flat predictor
is projected back to a local packet, residual energy is observed boundary
curvature. T15 explains why the next copy mechanism should be a refinement
tower, not whole-tile reuse. New sub-tile packets are the genuine refinement
boundaries.

This also settles the native status of Apex-ANS:

```text
finite Apex posterior = native simplex model
rANS/range renormalization = terminal integer bitstream completion
```

The bit engine is not the source of the codec's intelligence. The native content
is the finite posterior, gauge/projection choice, boundary certificate, and
refinement-compatible packet structure.

## Next Native Experiment

The first version of **sub-tile transported residual strings + Apex posterior**
is now deployed in `../benchmark_subtile_transport_vs_webp.py`; see
`subtile_transport_codec_findings.md`.

Current 512x512 Costa Rica result:

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| deployed block-refined Apex | 553,641 |
| gap | +14,479 (+2.69%) |
| ideal no-codebook ceiling | 543,211 (+0.75%) |

This is a `6,864` byte improvement over the first Apex-ANS estimate, but the
copy/DC sub-tile commands are not yet profitable. The deployed win comes from
posterior routing, especially the stored residual-energy state on the hard
Correos image.

## N1 Apex Unitary Result

N1 adds the explicit unitary bridge between Helmert/local contrast coordinates
and character/conductor packet coordinates. The codec benchmark now includes a
small `unitary_packet_class` over predictor residual tiles; see
`apex_unitary_codec_findings.md`.

On the same 512x512 Costa Rica run:

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| deployed feasible native | 553,641 |
| ideal with N1 unitary packets | 539,967 |
| ideal gap | +805 (+0.15%) |

The unitary packet data is strong in the static/ideal sense, but too expensive
as a naive one-pass context. Its next role should be model selection and
reference mining:

```text
use N1 packet class to choose/mine the retained sector,
not to split every residual posterior cold.
```

## Apex Seeded Gauge Result

The next all-native target is now implemented in
`../benchmark_mined_strings_vs_webp.py`; see
`apex_seeded_gauge_codec_findings.md`.

The key correction was to move T0 gauge selection back into the codec and to
replace cold new-symbol literals with a deterministic finite Apex seed prior:

```text
q(n) = 1 / ((n + 1)(n + 2))
P(symbol | context) = (count(symbol) + alpha q(symbol)) / (total + alpha)
```

The decoder can share this prior without a stored histogram. It is a native
simplex posterior, not a borrowed static codebook.

Current 512x512 Costa Rica result:

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| native Apex-seeded gauge estimate | 531,616 |
| native win | -7,546 (-1.40%) |
| ideal no-codebook ceiling | 520,238 (-3.51%) |

Per image:

| file | WebP | native | gauge | best posterior | result |
|---|---:|---:|---|---|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 231,732 | 237,192 | `r-gr-bavg` | `ch-ctx-energy-unitary-apex128` | +5,460 (+2.36%) |
| `central-valley-san-jose-costa-rica.jpg` | 307,430 | 294,424 | `g-rg-bavg` | `ch-ctx-grad-apex128` | -13,006 (-4.23%) |

This is the first point in the raw-RGB Costa Rica line where the native codec
estimate beats WebP lossless on the two-image total.

The mined residual-string command path was also tested. It remains inert:
copy/DC commands save too little locally to repay sparse command flags and
command metadata. The correct next role for mining is still higher-level model
selection, not byte-copy imitation.

## Real Round-Trip Bitstream

The first real bitstream is now implemented in
`../apex_seeded_image_codec.py`; see `apex_seeded_roundtrip_findings.md`.

It stores a `SIGA` stream:

```text
header + gauge id + predictor metadata + exact residual arithmetic stream
```

and verifies recovery by CRC after inverse gauge reconstruction.

Current 512x512 Costa Rica real round-trip result:

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| real SIGA round-trip | 545,619 |
| real gap | +6,457 (+1.20%) |

Per image:

| file | WebP | SIGA real | gauge | result |
|---|---:|---:|---|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 231,732 | 244,235 | `r-gr-bavg` | +12,503 (+5.40%) |
| `central-valley-san-jose-costa-rica.jpg` | 307,430 | 301,384 | `g-rg-bavg` | -6,046 (-1.97%) |

Both images recovered byte-exactly. The estimate still beats WebP, while the
first real backend is slightly above WebP. The difference is now concrete:
gamma escapes and byte-stored metadata are too crude compared with the ideal
Apex posterior.

## Next Engineering Target

The next benchmark should be **tightening the real Apex backend**:

1. Replace the gamma escape with exact arithmetic coding of
   `q(n)=1/((n+1)(n+2))`.
2. Bit-pack predictor ids and side packet metadata.
3. Add real support for row-gradient contexts without expensive byte side data.
4. Then revisit per-region gauge switching and mined residual strings, paying
   metadata only when the switch or command repays itself.

After that, the copy/reference analog can be upgraded from:

```text
copy bytes
```

becomes

```text
reuse a transported residual song inside the Kummer corridor
```

The immediate target is no longer recovery; recovery works. It is closing the
`545,619` real bytes down toward the `531,616` estimator bytes.
