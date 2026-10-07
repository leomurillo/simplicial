# SCANS v0 Compression Prototype

SCANS v0 is a first practical codec experiment inspired by the T-series
finite-ledger/closure framing.

The standalone path uses:

- compact SCANS container with original size and CRC;
- optional per-file finite dictionary mined during compression;
- raw deflate payload;
- deterministic decode.

The optional optimized-backend path uses the same SCANS container with
Zstandard level 19 as a proxy for the fast entropy backend we would eventually
own directly.

## Commands

Rounding-cell spectral song proof of concept:

```powershell
python empirical\compression\cell_song_poc.py demo
python empirical\compression\cell_song_poc.py compress input.bin output.hcs
python empirical\compression\cell_song_poc.py decompress output.hcs restored.bin
```

Image benchmark for the rounding-cell POC:

```powershell
python -m venv empirical\compression\.imagevenv
empirical\compression\.imagevenv\Scripts\python.exe -m pip install pillow numpy
$env:PYTHONDONTWRITEBYTECODE='1'
empirical\compression\.imagevenv\Scripts\python.exe empirical\compression\benchmark_cell_song_images.py --crop-size 512
empirical\compression\.imagevenv\Scripts\python.exe empirical\compression\benchmark_cell_song_images.py --crop-size 256 --include-hcs2d
Remove-Item -Recurse -Force empirical\compression\.imagevenv
```

Standalone round trip:

```powershell
python empirical\compression\scans_codec.py compress input.bin output.scans
python empirical\compression\scans_codec.py decompress output.scans restored.bin
```

Benchmark against gzip:

```powershell
python empirical\compression\benchmark_scans.py
```

Optional optimized backend:

```powershell
python -m venv empirical\compression\.benchvenv
empirical\compression\.benchvenv\Scripts\python.exe -m pip install zstandard
$env:PYTHONDONTWRITEBYTECODE='1'
empirical\compression\.benchvenv\Scripts\python.exe empirical\compression\benchmark_scans.py
Remove-Item -Recurse -Force empirical\compression\.benchvenv
```

## Current Result

See `reports/scans_benchmark.md` for the optimized-backend run and
`reports/scans_benchmark_deflate_only.md` for the dependency-free run.

`cell_song_poc.py` is separate from SCANS v0. It is the first native
rounding-cell codec experiment: sparse recursive Haar/Helmert songs are
accepted when their inverse projection lands inside every byte's unit rounding
cell, and decoding returns `floor(y_i)`.

`cell_song_image2d_poc.py` is the first image-native variant: sparse 8x8 2D
Haar/polynomial songs are tried per color plane. It proves exact cell hits are
possible, but the interval solver is too slow and the block savings are still
too sparse for photographs.

`simplicial_image_codec.py` is the practical first native image codec. It uses
T4-style gauge removal in a cheap form: reversible color gauges, per-tile
local predictor gauges, and a custom Rice entropy stream over exact integer
residuals. On the three supplied image center crops at 512x512, see
`reports/sigi_images_512.md`, the first YCoCg version produced:

- SIGI total: `1,395,558` bytes
- gzip-on-RGB total: `1,825,215` bytes
- optimized PNG total: `1,641,105` bytes
- SIGI vs gzip: `-23.54%`
- SIGI vs PNG: `-14.96%`

The current implementation is pure Python and decompression is not yet
competitive with PNG/gzip timings. The promising part is the stream size and
the simple decode shape: predict, Rice-decode residual, add.

The current best mode is `g-bg-ravg-ctx-rice`: a reversible color gauge

```text
G
B - G
R - floor((G + B) / 2)
```

followed by eight-context per-tile Rice coding. T0-inspired ANOVA and
context-Huffman variants are also implemented; see
`reports/sigi_t0_anova_huffman_findings.md`. On the Costa Rica raw-RGB tests,
ANOVA did not fire because the existing plane predictor already removes the
row/column gauge locally, while context-Huffman gave a modest size improvement
on some regions but still did not beat WebP.

The `g-bg-ravg-ctx-rice` mode now beats WebP
lossless on the second supplied satellite image crop:

- 512x512 crop, see `reports/sigi_beats_webp_image2_512.md`
  - WebP lossless: `489,474` bytes
  - SIGI: `484,907` bytes
  - SIGI vs WebP: `-4,567` bytes (`-0.93%`)
- 1024x1024 crop, see `reports/sigi_winning_mode_image2_1024.md`
  - WebP lossless: `1,872,748` bytes
  - SIGI: `1,835,857` bytes
  - SIGI vs WebP: `-36,891` bytes (`-1.97%`)

On a larger 1024x1024 crop of `133925289798805247.jpg`, see
`reports/sigi_image1_1024.md`, the first serious image-specific baseline shows
where the next target is:

- SIGI: `1,489,395` bytes
- gzip-on-RGB: `1,885,843` bytes
- optimized PNG: `1,642,726` bytes
- WebP lossless: `1,324,414` bytes
- SIGI vs gzip: `-21.02%`
- SIGI vs PNG: `-9.33%`
- SIGI vs WebP lossless: `+12.46%`

The next native entropy-backend experiment is `Apex-ANS`, an adaptive
no-codebook context model over SIGI residuals. See
`reports/apex_ans_codec_findings.md` and
`reports/apex_ans_vs_webp_costa_rica_512.md`. On the Costa Rica 512x512 crops,
the feasible estimate beats WebP on the central-valley crop by `430` bytes,
but loses the two-image total by `21,343` bytes (`+3.96%`). The ideal native
context ceiling beats WebP total by `996` bytes (`-0.18%`), suggesting the next
raw-only target is transported song/copy gauges plus the Apex-ANS backend.

`benchmark_transported_kummer_vs_webp.py` is the follow-up all-native reference
experiment. It uses a T10-style Kummer class as a tile-reference filter, tries
transported raw-tile and transported residual songs, and estimates the result
with Apex-ANS. The strongest 512x512 Costa Rica result is now:

- WebP lossless: `539,162` bytes
- transported Kummer + Apex-ANS estimate: `553,353` bytes
- result vs WebP: `+14,191` bytes (`+2.63%`)
- ideal no-codebook ceiling: `542,636` bytes (`+0.64%` vs WebP)

The useful improvement came from a compact residual-energy context
(`ch-ctx-energy`) on the hard Correos image. Whole-tile Kummer transport itself
was nearly inert, accepting only three transported tiles total on the 512 crops.
See `reports/transported_kummer_codec_findings.md` and
`reports/transported_kummer_vs_webp_costa_rica_512.md`.

For the all-native program, see `reports/native_simplicial_codec_program.md`.
The target stack is Kummer gauge selection, Helmert/conductor packet songs,
transported closure reuse, exact residuals, and Apex-ANS. T10's m-power
hierarchy should act as a gauge selector and prior, not as a naive per-symbol
context splitter.

T13-T15 refine that target. See
`reports/t13_t14_t15_codec_implications.md`. The new reading is:

- T13: residuals are exact boundary certificates of a retained model.
- T14: residual energy is projected curvature and should route compact contexts.
- T15: the next copy mechanism should be a refinement-compatible tower of
  sub-tile residual strings.
- Apex-ANS is native as a finite simplex posterior; rANS/range coding is the
  deterministic integer bitstream completion.

`benchmark_subtile_transport_vs_webp.py` deploys the first refinement-boundary
benchmark from that reading. The best current 512x512 Costa Rica run uses
direct block-refined Apex posterior coding at block size 32:

- WebP lossless: `539,162` bytes
- deployed native estimate: `553,641` bytes
- result vs WebP: `+14,479` bytes (`+2.69%`)
- improvement over first Apex-ANS estimate: `6,864` bytes

See `reports/subtile_transport_codec_findings.md` and
`reports/subtile_transport_vs_webp_costa_rica_512_b32_direct.md`. The DC/copy
sub-tile command path is implemented but not yet selected for the 512
deployment because command metadata still outweighs local savings.

`N1-ApexUnitaries-Draft1.md` adds a conductor/Fourier packet lens. The benchmark
now includes an N1-inspired `unitary_packet_class` over residual tiles. It does
not improve the one-pass feasible stream yet, but it moves the ideal ceiling
close to WebP:

- deployed feasible native estimate: `553,641` bytes (`+2.69%`)
- ideal with N1 unitary packet class: `539,967` bytes (`+0.15%`)

See `reports/apex_unitary_codec_findings.md` and
`reports/apex_unitary_context_costa_rica_512_b32.md`. The result says unitary
packet data should drive static/two-pass modeling and reference mining, not
naive high-cardinality one-pass contexts.

The next all-native target is now implemented in
`benchmark_mined_strings_vs_webp.py`: reversible T0-style gauge selection plus
a deterministic Apex integer prior over zigzag residuals,
`q(n)=1/((n+1)(n+2))`, followed by adaptive posterior updates. This removes the
cold-start literal penalty without storing a histogram side table.

On the Costa Rica raw-RGB benchmarks:

- 256x256 all-gauge sweep, see
  `reports/apex_seeded_gauge_costa_rica_256_l32.md`
  - WebP lossless: `143,886` bytes
  - native Apex-seeded gauge estimate: `143,343` bytes
  - native vs WebP: `-543` bytes (`-0.38%`)
- 512x512 focused gauge run, see
  `reports/apex_seeded_gauge_costa_rica_512_l32.md`
  - WebP lossless: `539,162` bytes
  - native Apex-seeded gauge estimate: `531,616` bytes
  - native vs WebP: `-7,546` bytes (`-1.40%`)

See `reports/apex_seeded_gauge_codec_findings.md`. The remaining gap is no
longer "can the native math beat WebP on size?" on this pair; it is turning the
posterior estimate into a real round-trippable range/rANS bitstream and then
testing broader images.

`apex_seeded_image_codec.py` is that first real round-trip bitstream. It writes
a `SIGA` stream with gauge id, predictor metadata, exact residuals, and an
adaptive arithmetic backend using Apex escape mass. It verifies recovery by
CRC after inverse gauge reconstruction.

On the same Costa Rica 512x512 crops, see
`reports/apex_seeded_roundtrip_findings.md`:

- WebP lossless: `539,162` bytes
- real SIGA round-trip: `545,619` bytes
- real SIGA vs WebP: `+6,457` bytes (`+1.20%`)
- both images recovered byte-exactly
- central-valley is already a real win: `301,384` vs WebP `307,430`

This is now a working lossless codec path, not just a size estimator. The next
compression target is to make the real arithmetic backend match the exact
telescoping Apex prior more closely and bit-pack metadata.

Correos-specific sprint: see `reports/correos_race_result.md`. The native
SIGA path improved from `244,235` bytes to `234,462` bytes with exact recovery
using the `R,G-R,B-G` gauge, bit-packed metadata, exact fractional Apex coding,
parent-backed contexts, and magnitude/sign splitting. That is still `+2,730`
bytes versus WebP on Correos. A separate byte-race artifact,
`correos_512_vp8lcore.race`, is `231,715` bytes and recovers exactly, beating
the WebP file by `17` bytes by stripping the WebP RIFF wrapper around the VP8L
core. It is recorded as a boundary marker, not a native codec win.

Stronger size baselines than PNG to add next:

- WebP lossless (`cwebp -lossless -z 9` or Pillow/libwebp)
- JPEG XL lossless (`cjxl -d 0 -e 9`)
- AVIF lossless (`avifenc --lossless --speed 0`)
- optimized PNG tools (`zopflipng`, `oxipng`, `pngcrush`)
