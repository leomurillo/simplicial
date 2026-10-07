# Computational Apex Transfer POC

The hunch is correct: T9's closed-form transfer matrix is directly implementable as software.

Implemented in `empirical/apex_transfer.py`:

- three equivalent formulas for `U_kc`: geometric/polynomial, trigonometric, and exponential;
- radical-cyclotomic factorization `U_kc = R_k C_kc`;
- conductor packet grouping by `cond(chi_c) = N / gcd(N,c)`;
- Helmert coordinates to Fourier/conductor coordinates via `b = U* a`;
- Fourier/conductor coordinates to Helmert coordinates via `a = U b`;
- `M_x(beta,c)` and full apex-surface evaluation;
- conductor-energy signatures for classifying where a ledger's mass lives.

## Numerical Checks

| N | meaning | max formula error | unitarity error | transfer roundtrip |
|---:|---|---:|---:|---:|
| 6 | cross-prime anchor | 2.06e-15 | 8.88e-16 | 7.45e-16 |
| 8 | prime-power depth | 2.46e-15 | 5.33e-15 | 5.36e-15 |
| 30 | conductor-rich test | 1.43e-14 | 7.59e-14 | 7.76e-14 |

These are floating-point zero. The closed forms agree with the basis definition, and the transfer matrix is unitary to numerical precision.

## Compression Relevance

This is more promising than the ANOVA tile gauge as a *classifier and model selector*:

- Helmert coordinates are local dimensional contrasts: cheap differences and reversible ladders.
- Fourier/conductor coordinates expose packet structure: low conductor, high conductor, prime-axis, and mixed-axis energy.
- A compressor can choose its tile model from the packet signature before entropy coding residuals.

The practical next SIGI experiment should not build a dense `U` for 32x32 tiles. It should use this module as the reference implementation, then use FFT/CRT factorization for the fast path:

1. transform the tile/gauge residual into conductor packets;
2. preserve the few dominant low-conductor packets as the song;
3. entropy-code only the high-conductor residual;
4. fall back to the current predictor when the packet signature is noisy.

That is the T0/T9 version of “smallest song”: not row/column ANOVA, but a conductor-sparse packet song with an exact residual tail.

## First WebP-Facing Test

I added `empirical/compression/benchmark_apex_packet_vs_webp.py` as the smallest packet-song size experiment. It compares the current SIGI context predictor against quantized low/dominant Fourier packet songs per tile, with an exact residual tail.

On the two Costa Rica 512x512 center crops:

| file | WebP lossless | SIGI context Rice | Apex packet | packet tiles |
|---|---:|---:|---:|---:|
| central-valley-san-jose-costa-rica.jpg | 307,430 | 321,726 | 321,726 | 0 |
| que-ver-en-costa-rica-correos-portada.jpg | 231,732 | 270,332 | 270,332 | 0 |

Totals: WebP `539,162`, apex packet `592,058`, so apex packet is `+52,896` bytes (`+9.81%`) behind WebP on this first raw-only packet-song POC.

Interpretation: the naive low-frequency packet song is still dominated by the existing local predictor on these photo tiles. The transfer engine is useful, but the compression win needs a sharper packet model: likely DCT/JPEG-block-aware gauges, adaptive arithmetic/rANS, or larger-scale copy/reference structure rather than raw low-FFT coefficient storage.

## Apex-ANS Follow-Up

The next native analog tested was adaptive apex-state entropy, implemented in `empirical/compression/benchmark_apex_ans_vs_webp.py`.

On the same Costa Rica 512x512 center crops:

| file | WebP lossless | Apex-ANS | result |
|---|---:|---:|---:|
| central-valley-san-jose-costa-rica.jpg | 307,430 | 307,000 | -430 (-0.14%) |
| que-ver-en-costa-rica-correos-portada.jpg | 231,732 | 253,505 | +21,773 (+9.40%) |

Totals: WebP `539,162`, Apex-ANS `560,505`, so the feasible adaptive estimate is still `+21,343` bytes (`+3.96%`) behind WebP.

But the ideal no-codebook ceiling for the same native context family is `538,166`, which is `-996` bytes (`-0.18%`) better than WebP. This is the first evidence that the native program reaches WebP's size regime.

Conclusion: entropy-state intelligence matters. To win robustly, pair Apex-ANS with transported song/copy gauges, because the remaining gap is likely reference structure, not local residual entropy alone.
