# Apex Seeded Gauge Codec Findings

This pass is the next all-native target after the N1 unitary context result.
The change is small but important:

```text
reversible gauge selection
  -> local predictor gauges
  -> exact residual boundary stream
  -> deterministic Apex integer prior
  -> adaptive posterior updates
```

The goal was to remove the cold-start penalty that made high-cardinality
energy/unitary contexts look good in the ideal table but bad in the feasible
one-pass stream.

## What Was Implemented

`../benchmark_mined_strings_vs_webp.py` now supports:

- native reversible gauge selection with `--all-transforms` or `--transforms`;
- new reversible gauges:
  - `g-rg-bavg`: `G, R-G, B-floor((G+R)/2)`;
  - `r-gr-bavg`: `R, G-R, B-floor((R+G)/2)`;
  - `b-rb-gavg`: `B, R-B, G-floor((B+R)/2)`;
  - plus `g-bg-ravg`, `ycocg`, `green16`, and `rgb`;
- an Apex-seeded posterior over zigzag residual integers:

```text
q(n) = 1 / ((n + 1)(n + 2))
P(symbol | context) = (count(symbol) + alpha q(symbol)) / (total + alpha)
```

The decoder can share this prior with no histogram side table. The benchmark
tries `alpha = 8, 32, 128, 512` and charges the existing SIGI-style mode byte,
predictor bytes, and any residual energy/unitary side metadata.

The mined residual-string command path remains implemented, but for this pass
it is disabled with `--no-mine` because the prior run showed command flags and
copy metadata cost more than the few accepted copies saved.

## Costa Rica 256x256 Gauge Sweep

Command:

```powershell
python empirical\compression\benchmark_mined_strings_vs_webp.py `
  --crop-size 256 --string-len 32 --all-transforms --no-mine `
  --json empirical\compression\reports\apex_seeded_gauge_costa_rica_256_l32.json `
  --report empirical\compression\reports\apex_seeded_gauge_costa_rica_256_l32.md `
  C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg `
  C:\Users\leomu\Downloads\central-valley-san-jose-costa-rica.jpg
```

| total | bytes |
|---|---:|
| WebP lossless | 143,886 |
| native Apex-seeded gauge estimate | 143,343 |
| native vs WebP | -543 (-0.38%) |
| ideal no-codebook ceiling | 137,443 |
| ideal vs WebP | -6,443 (-4.48%) |

Per image:

| file | WebP | native | gauge | best posterior | result |
|---|---:|---:|---|---|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 63,034 | 65,936 | `r-gr-bavg` | `ch-ctx-energy-apex128` | +2,902 (+4.60%) |
| `central-valley-san-jose-costa-rica.jpg` | 80,852 | 77,407 | `g-rg-bavg` | `ch-ctx-grad-apex128` | -3,445 (-4.26%) |

## Costa Rica 512x512 Result

Command:

```powershell
python empirical\compression\benchmark_mined_strings_vs_webp.py `
  --crop-size 512 --string-len 32 `
  --transforms r-gr-bavg,g-rg-bavg,g-bg-ravg --no-mine `
  --json empirical\compression\reports\apex_seeded_gauge_costa_rica_512_l32.json `
  --report empirical\compression\reports\apex_seeded_gauge_costa_rica_512_l32.md `
  C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg `
  C:\Users\leomu\Downloads\central-valley-san-jose-costa-rica.jpg
```

| total | bytes |
|---|---:|
| WebP lossless | 539,162 |
| native Apex-seeded gauge estimate | 531,616 |
| native vs WebP | -7,546 (-1.40%) |
| ideal no-codebook ceiling | 520,238 |
| ideal vs WebP | -18,924 (-3.51%) |

Per image:

| file | WebP | native | gauge | best posterior | ideal | result |
|---|---:|---:|---|---|---:|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 231,732 | 237,192 | `r-gr-bavg` | `ch-ctx-energy-unitary-apex128` | 232,706 | +5,460 (+2.36%) |
| `central-valley-san-jose-costa-rica.jpg` | 307,430 | 294,424 | `g-rg-bavg` | `ch-ctx-grad-apex128` | 287,532 | -13,006 (-4.23%) |

## Interpretation

This is the first raw-RGB Costa Rica benchmark in this line where the native
estimate beats WebP lossless on the two-image total.

The useful ingredients were:

- T0-style gauge selection at the image level;
- T13/T14-style residual energy and unitary routing;
- N1 packet data used only when it pays;
- a deterministic Apex prior that avoids expensive first-symbol literals.

The hard Correos image still loses to WebP, but the new gauge reduces that
loss substantially. On the 512 crop, fixed `g-bg-ravg` was `248,047` bytes in
the same seeded posterior harness, while `r-gr-bavg` is `237,192`, a gain of
`10,855` bytes.

The central-valley image is now a clear native win: `294,424` bytes vs WebP's
`307,430`.

## Next Engineering Target

This result should move from estimator to round-trippable bitstream:

1. Implement the Apex-seeded posterior as a real range/rANS backend.
2. Store the winning image gauge id, tile predictor ids, and charged side
   packet data.
3. Decode with the same deterministic prior and adaptive updates.
4. Keep mined residual-string transport disabled until a stronger command
   family beats its own metadata.
5. Then test per-region gauge selection, where metadata is only paid when the
   gauge switch repays it.

