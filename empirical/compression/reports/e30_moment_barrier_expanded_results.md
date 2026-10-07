# E30 Expanded Moment-Barrier Results

This follow-up tests whether the E30 hard moment gate survives contact with other images and larger crops. The gate is causal and payload-free: the decoder computes the same Hankel sign from already decoded residual magnitudes, so no gate map is transmitted.

The benchmark used the native E30 baseline and the hard moment-context model only. Soft and inverted moment priors were excluded from this run because the prior E30 sweep showed that the useful action is context routing, not smooth prior mixing.

## 512 Panel

| image | crop | WebP lossless | E30 baseline | E30 hard gate | hard vs baseline | hard vs WebP | roundtrip |
|---|---:|---:|---:|---:|---:|---:|---|
| que-ver-en-costa-rica-correos-portada.jpg | 512x512 | 231,732 | 234,465 | 229,866 | -4,599 | -1,866 | true |
| central-valley-san-jose-costa-rica.jpg | 512x512 | 307,430 | 298,811 | 298,588 | -223 | -8,842 | true |
| 133925289798805247.jpg | 512x512 | 306,272 | 286,705 | 287,475 | +770 | -18,797 | true |
| 133893333653186297.jpg | 512x512 | 489,474 | 481,109 | 482,507 | +1,398 | -6,967 | true |
| 133921439458600606.jpg | 512x512 | 505,660 | 486,804 | 487,827 | +1,023 | -17,833 | true |

At 512, the hard moment gate improves both natural/city images, including the original Correos image, but loses slightly against the native baseline on the three satellite-style controls. Importantly, the native codec still beats WebP on every satellite control.

## 1024 Stress Panel

| image | crop | WebP lossless | E30 baseline | E30 hard gate | hard vs baseline | hard vs WebP | roundtrip |
|---|---:|---:|---:|---:|---:|---:|---|
| que-ver-en-costa-rica-correos-portada.jpg | 1024x1024 | 975,520 | 961,567 | 947,176 | -14,391 | -28,344 | true |
| central-valley-san-jose-costa-rica.jpg | 1024x1024 | 1,142,164 | 1,087,964 | 1,085,582 | -2,382 | -56,582 | true |
| 133925289798805247.jpg | 1024x1024 | 1,324,414 | 1,217,366 | 1,216,896 | -470 | -107,518 | true |

At 1024, the hard moment gate improves all tested images. The Correos gain scales from 4,599 bytes at 512 to 14,391 bytes at 1024. The city image remains a smaller but positive native-codec gain. The satellite control flips from a small 512 loss to a small 1024 gain, while the native baseline itself is already far ahead of WebP.

## Interpretation

The E30 result is stronger after expansion, but also more precise.

The hard moment sign is a real compression signal: it can improve a lossless entropy model without transmitted side information, and it now does so out-of-sample and at a larger crop size. This supports the P6 reading that a Hankel/moment barrier is not just a post-hoc diagnostic; it can act as a causal routing variable.

The signal is not universally beneficial at small sample scale. On the 512 satellite controls, hard context fragmentation costs more than it saves. At 1024, where each context family has more data and longer-range residual structure, the gate becomes positive even on the satellite control. This points to governance rather than rejection: the next codec should decide when the moment split is mature enough to expose as context.

## Next Compression Target

E31 should be a regret-governed moment gate. Instead of always splitting by Hankel class, the codec should keep causal online scores for baseline versus moment-split contexts and activate the split only when the decoder can independently infer that the split has earned its cost. That would preserve the 1024 wins while avoiding the 512 satellite losses, still with no explicit gate payload.

