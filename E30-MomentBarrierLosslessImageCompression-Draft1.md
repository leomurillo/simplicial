# E30: Moment-Barrier Lossless Image Compression

## Causal Hankel Gates, Apex Entropy Models, and a Path Toward Governed Compression Optimality

Draft 1  
May 2026

## Abstract

This paper introduces E30, a lossless image compression strategy that augments an adaptive arithmetic image codec with a causal moment-barrier gate. The method is motivated by a simple principle: a residual stream is not statistically homogeneous merely because it is locally predicted. Some residual histories signal a structural boundary in the finite moment geometry of the stream. E30 detects this boundary by computing a 3 by 3 Hankel determinant from the last five already decoded residual magnitudes. The sign of this determinant is used as a deterministic, no-payload context refinement inside an adaptive Apex entropy model.

The resulting codec remains exactly lossless. The encoder and decoder compute the same moment class from the same past residual magnitudes, so the gate does not require side information. In the tested implementation, E30 combines a reversible color gauge, tilewise predictor selection, adaptive Apex-seeded arithmetic coding, sign-split residual coding, and a Hankel moment-context refinement. On an expanded panel of natural, city, and satellite images, the best E30 rows beat WebP lossless on all tested crops. At 1024 by 1024, the hard moment gate improves all three tested images, with savings against WebP of 28,344 bytes, 56,582 bytes, and 107,518 bytes.

The paper also isolates the failure mode of the hard gate: context fragmentation when the moment split has not yet earned its statistical cost. This motivates the E31 governed extension, in which the moment gate is activated only after a causal regret score certifies that the split is useful. Thus E30 supplies the structural signal, and E31 supplies the governance principle. Together they suggest a compression program in which increasingly refined boundary detectors are admitted only when they pay for their projection cost.

## 1. Introduction

Classical lossless image compression depends on three interlocking operations:

1. choose a reversible representation of the image,
2. predict each sample from already decoded neighbors,
3. entropy-code the resulting residuals with a model that adapts to local statistics.

E30 keeps this contract but changes the meaning of "local statistics." The usual local context, such as edge strength or neighboring-pixel gradient, is a first-order geometric descriptor. It asks whether the nearby pixels are smooth, edged, or textured. E30 adds a different question: does the recent residual stream look compatible with a positive finite moment structure, or has it crossed a moment barrier?

For a short history of residual magnitudes

\[
b_0,b_1,b_2,b_3,b_4,
\]

E30 forms the Hankel determinant

\[
\Delta_2
=
\det
\begin{pmatrix}
b_0 & b_1 & b_2\\
b_1 & b_2 & b_3\\
b_2 & b_3 & b_4
\end{pmatrix}.
\]

If \(\Delta_2<0\), the local sequence fails the second Hankel positivity condition that any positive moment sequence must satisfy. E30 interprets this as a moment barrier. The barrier is not transmitted. It is computed causally by both encoder and decoder from previously decoded residual magnitudes.

The central thesis is:

\[
\boxed{
\text{compression improves when entropy contexts respect causal moment boundaries.}
}
\]

The first empirical result is already significant: the E30 hard moment-context model gives exact lossless roundtrips and beats WebP lossless on the tested image crops when paired with the existing Apex residual coder. The deeper result is structural: moment geometry supplies a deterministic way to refine entropy contexts without adding side information.

## 2. Codec Overview

Let an RGB image be

\[
X \in \{0,\ldots,255\}^{H\times W\times 3}.
\]

The implemented E30 pipeline is:

1. Apply a reversible integer color gauge.
2. Partition each transformed channel into tiles.
3. Select a local predictor per tile.
4. Encode residual magnitudes with an adaptive arithmetic model.
5. Encode signs separately for nonzero residuals.
6. Refine entropy contexts by a causal Hankel moment class.
7. Store enough deterministic metadata to reconstruct predictors, gauges, and residual stream.
8. Verify exact recovery by CRC and byte-for-byte RGB equality.

The tested configuration used:

\[
\texttt{transform}=\texttt{r-gr-bg}
\]

and

\[
\texttt{scheme}=\texttt{ch-ctx-energy-unitary-split-blend71-apex128}.
\]

The color gauge is

\[
(R,G,B)\mapsto (C_0,C_1,C_2)=(R,G-R,B-G),
\]

with inverse

\[
R=C_0,\qquad
G=C_1+C_0,\qquad
B=C_2+G.
\]

This transform is exactly reversible over the integer channel values produced by the image.

For each channel and tile, a predictor \(P\) is chosen from a finite predictor family. The residual at pixel \(t=(y,x,c)\) is

\[
r_t = C_t - P_t(C_{<t}),
\]

where \(C_{<t}\) denotes already decoded samples in raster order. In the sign-split model, the coded magnitude is

\[
m_t = |r_t|,
\]

and the sign is coded only when \(m_t>0\).

## 3. Apex-Seeding of the Entropy Model

The baseline E30 entropy model is an adaptive arithmetic coder with an Apex prior. Let the residual magnitude alphabet be

\[
\mathcal A=\{0,\ldots,M\}.
\]

For a context \(k\), let \(n_k(s)\) be the count of symbol \(s\) previously seen in that context, and let

\[
N_k=\sum_{s=0}^{M}n_k(s).
\]

The Apex prior used in the implementation is the normalized discrete law

\[
q_M(s)
=
\frac{M+2}{M+1}\frac{1}{(s+1)(s+2)},
\qquad
s=0,\ldots,M.
\]

This is a truncated telescoping prior:

\[
\sum_{s=0}^{M}\frac{1}{(s+1)(s+2)}
=
\frac{M+1}{M+2},
\]

so \(q_M\) sums to one. With prior strength \(\alpha=128\), the adaptive probability model is

\[
Q_k(s)
=
\frac{n_k(s)+\alpha q_M(s)}{N_k+\alpha}.
\]

The tested scheme also uses a parent-context blend. If \(k\) is the fine context and \(p(k)\) is its parent context, then the coded probability is

\[
Q(s\mid k,p)
=
\frac{w_f Q_k(s)+w_p Q_{p(k)}(s)}{w_f+w_p}.
\]

For the reported results,

\[
w_f:w_p=7:1.
\]

This blend protects sparse fine contexts by borrowing mass from a coarser parent.

## 4. The Moment-Barrier Gate

For each channel, E30 maintains the last five decoded residual magnitudes:

\[
H_t=(m_{t-5},m_{t-4},m_{t-3},m_{t-2},m_{t-1}).
\]

When fewer than five magnitudes are available, E30 assigns the initialization class

\[
c_t=0.
\]

Otherwise define

\[
\Delta_t
=
\det
\begin{pmatrix}
m_{t-5} & m_{t-4} & m_{t-3}\\
m_{t-4} & m_{t-3} & m_{t-2}\\
m_{t-3} & m_{t-2} & m_{t-1}
\end{pmatrix}.
\]

The E30 moment class is

\[
c_t
=
\begin{cases}
0, & |H_t|<5,\\
1, & \Delta_t\ge 0,\\
2, & \Delta_t<0.
\end{cases}
\]

The hard moment-context model replaces the baseline context key

\[
k_t
\]

with the refined key

\[
\widetilde{k}_t=(c_t,k_t).
\]

The context is refined by a causal moment packet. No extra bits are written for \(c_t\).

## 5. Why a Hankel Sign Is a Compression Signal

A positive measure \(\mu\) on the real line has moments

\[
a_j=\int x^j\,d\mu(x).
\]

Every finite Hankel matrix

\[
H_n=(a_{i+j})_{0\le i,j\le n}
\]

must be positive semidefinite. In particular,

\[
\det
\begin{pmatrix}
a_0&a_1&a_2\\
a_1&a_2&a_3\\
a_2&a_3&a_4
\end{pmatrix}
\ge 0.
\]

E30 does not claim that a five-symbol residual history is literally a moment sequence of an underlying positive measure. Instead, it uses the Hankel sign as a local algebraic diagnostic. A negative determinant is a finite obstruction to moment positivity. Empirically, that obstruction separates residual regimes with different entropy statistics.

Thus the determinant is not a smoothness prior. It is a boundary detector. This distinction matters. The E30 experiments found that soft moment priors were less effective than hard context routing. The successful action was not "make residuals smoother"; it was "do not model moment-compatible and moment-barrier histories as the same context."

## 6. Losslessness and Causal Decodability

### Theorem 1. Reversible Gauge Theorem

The color transform

\[
(R,G,B)\mapsto (R,G-R,B-G)
\]

is exactly invertible over integer channel values.

Proof. Given \(C_0=R\), \(C_1=G-R\), and \(C_2=B-G\), reconstruct

\[
R=C_0,\qquad G=C_1+C_0,\qquad B=C_2+G.
\]

Substitution gives the original triple exactly. The implementation checks that reconstructed channel values lie in \(\{0,\ldots,255\}\). Therefore the gauge is lossless. \(\square\)

### Theorem 2. Causal Moment-Class Theorem

For every pixel/channel position \(t\), the E30 class \(c_t\) is computable by the decoder before decoding \(m_t\).

Proof. The class \(c_t\) depends only on the five prior magnitudes

\[
m_{t-5},\ldots,m_{t-1}.
\]

These magnitudes have already been decoded and appended to the decoder history before position \(t\). Therefore the decoder and encoder have identical inputs to the Hankel determinant at position \(t\), and compute the same \(c_t\). \(\square\)

### Theorem 3. No-Payload Gate Theorem

The hard moment-context gate requires no side information.

Proof. By Theorem 2, the decoder computes \(c_t\) before decoding \(m_t\). The refined key \(\widetilde{k}_t=(c_t,k_t)\) is therefore known to both encoder and decoder at the same time. The arithmetic interval for \(m_t\) is selected from \(\widetilde{k}_t\) without transmitting \(c_t\). \(\square\)

### Theorem 4. Exact Roundtrip Theorem

Assume the arithmetic coder is decoded with the same model update order used by the encoder, and assume stored metadata for image size, transform id, scheme id, predictor choices, residual alphabet bound, energy classes, and unitary packet classes is read correctly. Then E30 reconstructs the original RGB image exactly.

Proof. The decoder reconstructs each transformed channel in the same raster order used by the encoder. At each position it has the same prior decoded channel prefix, hence the same predictor, same context, same moment class, same arithmetic model state, and same sign model state. Arithmetic decoding returns the exact symbol encoded by the encoder. If the symbol is zero, the residual is zero; if nonzero, the sign substream recovers the exact sign. Thus each residual \(r_t\) is recovered exactly. Since

\[
C_t=P_t(C_{<t})+r_t,
\]

each transformed channel value is recovered exactly by induction over raster order. The reversible gauge theorem then recovers the original RGB values exactly. The implementation additionally verifies the CRC of the reconstructed RGB byte string. \(\square\)

## 7. Source-Coding Interpretation

Let \(Q_0\) be the baseline adaptive model and \(Q_1\) be the hard moment-refined model. At a coded symbol \(m_t\), the arithmetic cost is approximately

\[
\ell_i(t)=-\log_2 Q_i(m_t\mid\mathcal F_{t-1}),
\]

where \(\mathcal F_{t-1}\) is the decoded past. The hard moment split improves coding when

\[
\sum_t\bigl(\ell_0(t)-\ell_1(t)\bigr)>0
\]

after accounting for adaptation cost.

There is no explicit payload cost for the Hankel class, but there is an implicit statistical cost: splitting a context reduces the data available to each refined context. This is why the hard gate can lose on small or mismatched samples. Its benefit is not guaranteed by the existence of a boundary alone. The boundary must produce enough conditional distribution separation to overcome context fragmentation.

This observation leads directly to the governed extension:

\[
R_T=\sum_{t<T}\bigl(\ell_0(t)-\ell_1(t)\bigr).
\]

Activate the moment expert only when

\[
R_T>\tau
\]

for a causal threshold \(\tau\). E31 implements this rule and updates both experts on every symbol, so encoder and decoder remain synchronized without transmitting an activation map.

## 8. Experimental Method

The reported tests used center crops of real images. WebP lossless was encoded through Pillow/libwebp with lossless mode, quality 100, method 6. All E30/E31 rows marked true were verified by exact roundtrip.

The main E30 expanded panel used:

- `que-ver-en-costa-rica-correos-portada.jpg`
- `central-valley-san-jose-costa-rica.jpg`
- three 4K satellite-style images from the local image set

The implemented E30 files are:

- `empirical/compression/e30_moment_barrier_gate.py`
- `empirical/compression/reports/e30_moment_barrier_expanded_results.md`
- `empirical/compression/reports/e30_moment_panel_512.json`
- `empirical/compression/reports/e30_moment_panel_1024.json`

The governed extension is:

- `empirical/compression/e31_regret_governed_moment_gate.py`
- `empirical/compression/reports/e31_regret_governed_moment_gate_findings.md`

## 9. E30 Results Against WebP Lossless

The following table takes the best E30 row among the baseline Apex model and the hard moment-context model.

| Image | Crop | WebP lossless | Best E30 | Best E30 model | Saved vs WebP |
|---|---:|---:|---:|---|---:|
| Correos | 512x512 | 231,732 | 229,866 | hard moment-context | 1,866 bytes, 0.805% |
| Central Valley | 512x512 | 307,430 | 298,588 | hard moment-context | 8,842 bytes, 2.876% |
| Satellite 133925 | 512x512 | 306,272 | 286,705 | baseline Apex | 19,567 bytes, 6.389% |
| Satellite 133893 | 512x512 | 489,474 | 481,109 | baseline Apex | 8,365 bytes, 1.709% |
| Satellite 133921 | 512x512 | 505,660 | 486,804 | baseline Apex | 18,856 bytes, 3.729% |
| Correos | 1024x1024 | 975,520 | 947,176 | hard moment-context | 28,344 bytes, 2.906% |
| Central Valley | 1024x1024 | 1,142,164 | 1,085,582 | hard moment-context | 56,582 bytes, 4.954% |
| Satellite 133925 | 1024x1024 | 1,324,414 | 1,216,896 | hard moment-context | 107,518 bytes, 8.118% |

The tested best E30 rows beat WebP lossless in all eight cases.

## 10. What the Hard Gate Revealed

At 512 by 512, the hard moment gate improves the two natural/city images but loses slightly against the native baseline on the three satellite-style controls:

| Image | Crop | E30 baseline | E30 hard gate | Hard vs baseline |
|---|---:|---:|---:|---:|
| Correos | 512x512 | 234,465 | 229,866 | -4,599 |
| Central Valley | 512x512 | 298,811 | 298,588 | -223 |
| Satellite 133925 | 512x512 | 286,705 | 287,475 | +770 |
| Satellite 133893 | 512x512 | 481,109 | 482,507 | +1,398 |
| Satellite 133921 | 512x512 | 486,804 | 487,827 | +1,023 |

At 1024 by 1024, the same hard gate improves all tested images:

| Image | Crop | E30 baseline | E30 hard gate | Hard vs baseline |
|---|---:|---:|---:|---:|
| Correos | 1024x1024 | 961,567 | 947,176 | -14,391 |
| Central Valley | 1024x1024 | 1,087,964 | 1,085,582 | -2,382 |
| Satellite 133925 | 1024x1024 | 1,217,366 | 1,216,896 | -470 |

The interpretation is precise. The Hankel sign is a real compression signal, but it is not universally profitable at all sample scales. At larger scale, the refined contexts receive enough data for the split to pay. At smaller scale, some image families require governance.

## 11. Governed Moment Admission

E31 was designed as the immediate refinement of E30. It keeps the E30 signal but admits it only when causal regret certifies value. With a global regret score, threshold \(\tau=512\) bits, and warmup of 2048 symbols, E31 obtained:

| Image | Crop | E30 baseline | E30 hard | E31 governed | E31 behavior |
|---|---:|---:|---:|---:|---|
| Correos | 512x512 | 234,465 | 229,866 | 229,933 | follows hard after threshold |
| Central Valley | 512x512 | 298,811 | 298,588 | 298,655 | follows hard after threshold |
| Satellite 133925 | 512x512 | 286,705 | 287,475 | 286,708 | stays baseline |
| Satellite 133893 | 512x512 | 481,109 | 482,507 | 481,112 | stays baseline |
| Satellite 133921 | 512x512 | 486,804 | 487,827 | 486,807 | stays baseline |
| Correos | 1024x1024 | 961,567 | 947,176 | 947,243 | follows hard after threshold |
| Central Valley | 1024x1024 | 1,087,964 | 1,085,582 | 1,085,649 | follows hard after threshold |
| Satellite 133925 | 1024x1024 | 1,217,366 | 1,216,896 | 1,216,963 | follows hard after threshold |

The governed codec trails the better expert by a small fixed cost: approximately 64 bytes from the 512-bit threshold plus roughly 3 bytes of stream configuration overhead. This is the expected cost of causal confidence.

## 12. Toward Compression Optimality

Lossless compression approaches optimality when its coding distribution approaches the true conditional distribution of the source:

\[
L(Q)-H(P)
=
\sum_t
D_{\mathrm{KL}}
\bigl(P_t(\cdot\mid\mathcal F_{t-1})
\Vert
Q_t(\cdot\mid\mathcal F_{t-1})\bigr).
\]

Every useful context refinement reduces this excess code length by making \(Q_t\) closer to the true conditional law. But every refinement also risks sparse statistics. E30 contributes a new class of refinements: algebraic moment-boundary refinements. E31 contributes the admission law: use a refinement only when causal regret shows that it pays.

This suggests a general compression architecture:

1. Maintain a base adaptive source model.
2. Generate candidate boundary refinements from structural detectors.
3. Keep all candidate experts synchronized where computationally feasible.
4. Admit a refinement only after its causal regret exceeds a maturity threshold.
5. Compose admitted refinements with existing codecs, predictors, transforms, and container formats.

In this architecture, the goal is not to replace mature codecs such as WebP, PNG, AVIF lossless modes, or specialized transforms. The goal is to supply a new layer of mathematically governed context discovery that can be combined with strong existing predictors and entropy coders.

## 13. Algorithmic Summary

### Encoding

For each channel \(c\), row \(y\), column \(x\):

1. Compute local predictor \(P_t\) from decoded prefix.
2. Compute residual \(r_t=C_t-P_t\).
3. Set \(m_t=|r_t|\).
4. Compute local context \(k_t\) from channel, gradient, energy, unitary packet, and parent context.
5. Compute Hankel class \(c_t\) from the previous five magnitudes.
6. Use refined key \(\widetilde{k}_t=(c_t,k_t)\) in the hard E30 model.
7. Arithmetic-code \(m_t\).
8. If \(m_t>0\), arithmetic-code the sign of \(r_t\).
9. Update the residual history and all adaptive counts.

### Decoding

For the same position \(t\):

1. Recompute \(k_t\) from the decoded prefix.
2. Recompute \(c_t\) from the decoded magnitude history.
3. Decode \(m_t\) from the same arithmetic interval.
4. Decode sign if \(m_t>0\).
5. Reconstruct \(r_t\).
6. Reconstruct \(C_t=P_t+r_t\).
7. Update histories and adaptive counts.
8. Apply inverse color gauge after all channels are reconstructed.

## 14. Limitations

The current implementation is a research prototype in Python. The decoder is slow because the hot path is per-symbol adaptive arithmetic coding with Python dictionary lookups and dynamic integer arithmetic. This does not indicate an inherent algorithmic bottleneck. The Hankel gate itself is cheap: it uses a rolling five-symbol history and a small integer determinant. A C or C++ implementation should pack context keys, use cache-friendly tables, and compile the arithmetic coder and predictor loops.

The empirical panel is promising but not yet a corpus-scale benchmark. The claim is therefore not that E30 universally dominates WebP. The claim is stronger in mechanism but narrower in evidence: a causal moment-boundary context can improve exact lossless compression without side information, and it has already produced out-of-sample wins against WebP lossless on the tested panel.

## 15. Conclusion

E30 introduces a new compression primitive: the causal moment-barrier gate. It detects a finite Hankel obstruction in the residual magnitude stream and uses that obstruction to refine adaptive entropy contexts without sending gate bits. The method is exactly lossless, decoder-reproducible, and empirically useful.

The important lesson is not merely that one determinant improved a prototype codec. The important lesson is that algebraic boundary diagnostics can become compression operators. Once such operators are governed by causal regret, a codec can safely expand its model class and then converge back toward the most useful retained contexts.

This is the compression analogue of a broader principle:

\[
\boxed{
\text{expand by structural boundary discovery, converge by causal compression gain.}
}
\]

E30 supplies the first moment-boundary discovery. E31 supplies the first governed admission rule. The natural next generation is a multi-scale governed codec that composes moment gates with stronger transforms, mature predictors, and production entropy engines. That path is a credible route toward compression systems that approach source optimality with increasing confidence rather than with ad hoc context growth.

