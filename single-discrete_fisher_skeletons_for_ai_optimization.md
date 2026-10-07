# Discrete Fisher Skeletons for Categorical Behavior: Natural Gradient, the Amari-Chentsov Cubic, and Finite Output Algebras

**Leonardo Murillo Montero**

*May 13, 2026*

---

## Abstract

Modern AI optimization moves through smooth, continuous parameter spaces.  But
the behavior it produces is categorical: token probabilities, class
distributions, concept bins, and finite output summaries.  The usual
optimization story treats those probability spaces as smooth statistical
manifolds.  Natural gradient methods, Fisher preconditioning, variational
inference, Hellinger geometry, and representation-manifold probes all rely on
that local premise.

This paper argues that the smooth story is incomplete.  When output labels
carry a finite algebra \(R\), the Fisher geometry of behavior has a discrete
arithmetic skeleton.  At maximum entropy, that skeleton is hidden inside a
clean orthogonal decomposition of the Fisher tangent space.  As soon as the
model moves away from maximum entropy, the conductor packets begin to couple.
The coupling is not noise and not a coordinate artifact.  Its Taylor
coefficients are governed by a finite quotient-character adjacency algebra.

In ML language, natural gradient sees the quadratic Fisher metric.  This
paper studies the first structured correction it misses: the raised
Amari-Chentsov cubic

$$
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)}
$$

for the categorical behavior simplex.  For a learned activation-to-behavior
map

$$
F:A\to \Delta_R^\circ,
$$

the pullback metric

$$
J_F^\top g_y J_F
$$

is only the quadratic term.  The next term separates into behavior-side
Fisher curvature, activation-side distortion, Hessian terms of \(F\), and
parameterization error.  The quotient-character algebra supplies a finite
indexing system for those corrections.

The weekday task of Wurgaft et al. is the minimal prime control.  Its output
algebra is \(C_7\), so the nontrivial behavior tangent space is one
six-dimensional conductor packet, with no mixed tame/wild extension.  At the
uniform point,

$$
K^{CH}_{p_*}(h)v=7h*v-7\langle h,v\rangle p_*.
$$

Thus any nonzero weekday displacement is already conductor-total: there is
only one nontrivial conductor packet, and its convolution envelope reaches all
nontrivial quotient characters by order \(6\).  Accidental coefficient zeros
can still occur at selected orders, but they are not conductor boundaries.

The real transformer measurement is now in hand on **two independent model
families** at the same layer index (causalab `weekdays` pipeline, layer 28,
last token): Llama-3.1-8B (the Wurgaft et al.\ baseline model) and
Mistral-7B-v0.3 (cross-family replication).  Both produce the same
qualitative signature, with Llama showing it more starkly.  The
moment-Euclidean linear summary correlation drops from \(r=0.886\) on the
symmetric proxy to \(r=0.615\) (Llama) and \(r=0.715\) (Mistral), while the
Hellinger, logit, and Fisher Levi-Civita correlations remain near or above
their proxy values on both models.  The empirical centroids are also
visibly asymmetric: every weekday leaks more probability to its cyclic
predecessor than to its cyclic successor, breaking the dihedral symmetry
the proxy assumed.  The prime \(C_7\) row therefore confirms the
cubic-diagnostic signature: linear (moment-space) flattening pays the
largest visible price, while Fisher/Hellinger-aware coordinates retain the
cyclic structure.  The cross-model replication argues against the
signature being a single-model or single-layer artifact.  The activation
pullback audit (§7.2.1) closes most of the residual question on the weekday
row: at layer 28, Llama's activation-distance vs Hellinger-chord
correlation is \(r=0.937\) and the pullback metric coefficient of variation
is \(0.154\), so the activation embedding is nearly a rescaled isometry of
the behavior simplex.  The linear-versus-manifold gap measured on \(C_7\)
is therefore not attributable to activation distortion -- it is intrinsic
to the behavior simplex, and the behavior-side cubic \(K^{CH}\) carries it.

The month task is the next control.  Its output algebra
\(C_{12}\cong C_4\times C_3\) has a CRT conductor split and a \(2\)-primary
depth ladder before any local nilpotent carry appears.  The Llama-3.1-8B
measurement is also now in hand: the moment-Euclidean correlation
**collapses from \(r=0.696\) on the proxy to \(r=0.210\)** -- a far sharper
drop than the prime \(C_7\) row -- and the empirical CRT conductor energy
decomposition spreads the displacement weight across all five \(C_{12}\)
conductors (\(2,3,4,6,12\)) rather than concentrating it in the single
dihedral mode, with the mixed \(C_4\times C_3\) conductor 6 carrying
\(19.2\%\) of the energy.  This is the first transformer-level empirical
evidence for the predicted CRT conductor split.

The positive mixed tests begin with the small local algebra
\({\mathbb F}_4[u]/(u^2)\).  There the quotient-character adjacency algebra
keeps finite tame/wild extension data that the associated graded loses.  The
corresponding class \(\operatorname{Ext}_{CH}\) is the proposed finite
diagnostic for when a coarse output macrovariable is closed at the centroid
but leaks Fisher-geometric information off the centroid.

The practical optimization thesis is modest but concrete: a model's
continuous behavior manifold may have a finite arithmetic control layer, and
that layer can be used to diagnose when a Fisher or natural-gradient
quadratic approximation is missing structured cubic curvature channels.

**Keywords:** AI optimization, natural gradient, Fisher information,
information geometry, behavior manifolds, neural representation geometry,
pullback metric, Amari-Chentsov tensor, categorical simplex, quotient-character
adjacency algebra, conductor filtration, macrovariable closure.

---

## The Hidden Arithmetic of Behavior

The central claim is not merely that arithmetic language can be used to
describe an AI geometry after the fact.

> When a model makes categorical predictions on a structured output space, it
> is already moving through a finite arithmetic behavior geometry.  The
> arithmetic becomes visible precisely when the model leaves maximum entropy.

At the uniform distribution, conductor packets are Fisher-orthogonal and the
geometry looks cleanly quadratic.  This is the equilibrium picture.  Away from
uniformity, useful prediction begins, but so does curvature.  The same move
that makes the model informative also activates off-centroid coupling between
the finite character packets of the output algebra.

This turns the usual AI scaling intuition sideways.  Larger models and richer
concept spaces do not necessarily make behavior geometry more purely smooth.
At the output level, more structure can mean more finite arithmetic: more
packets, more conductor layers, more mixed support, and more ways for a
quadratic Fisher approximation to miss structured information.

The diagnostic question is therefore:

> When is a natural-gradient step locally faithful, and when is it flattening
> curvature that is already organized by the discrete output algebra?

The answer begins with the first non-quadratic object, \(K^{CH}\), and with
the finite quotient-character algebra that indexes its off-centroid channels.

## Reader's Guide

This is the AI-facing version of the Fisher-conductor program.

The intended reader knows words like natural gradient, Fisher information,
Hessian, pullback metric, logits, behavior manifold, and representation
geometry.  The paper introduces the arithmetic vocabulary only as needed:
additive characters are the Fourier modes of the finite output algebra;
conductors are frequency-depth packets; the quotient-character adjacency
algebra is the finite operator algebra controlling off-centroid Fisher
couplings; \(\operatorname{Ext}_{CH}\) is the first named obstruction to
closing a coarse output macrovariable under those couplings.

The paper has five jobs.

1. State, in ML language, a hidden-arithmetic diagnostic for AI behavior
   geometry: the categorical Fisher tangent space carries a finite
   discrete skeleton organized by the additive characters of the output
   label algebra.
2. State the natural-gradient-plus-cubic diagnostic, with the raised
   Amari-Chentsov tensor \(K^{CH}\) as the first object that natural
   gradient misses.
3. Turn the Wurgaft weekday task into the prime \(C_7\) control
   experiment, with real-transformer measurement on two model families.
4. Run the month \(C_{12}\) task as the CRT mixed-conductor control, also
   with real-transformer measurement.
5. Explain why the mixed finite rows, especially \({\mathbb F}_4[u]/(u^2)\),
   are the real positive tests for structured activation-to-behavior
   curvature, and lay out the experiment design.

## Status of Claims

This draft separates proved mathematics, computed finite evidence, and open
empirical claims.

> **Current status, May 13, 2026.**  The weekday \(C_7\) row is now a real
> transformer measurement on **two independent model families**:
> Llama-3.1-8B (the Wurgaft et al.\ baseline model) and Mistral-7B-v0.3
> (cross-family replication), both at layer 28 last-token features via the
> causalab `weekdays` pipeline.  The measured centroids and correlations
> are reported in §4.1.  The symmetric parametric proxy is retained as a
> calibration reference; the real measurement diverges from it in the same
> direction on both models.

> **Implementation update, May 14, 2026.**  The first \(K^{CH}\) local
> step-controller prototype has been implemented in
> `empirical/k_ch_step_controller.py`, with smoke tests in
> `empirical/_test_k_ch_step_controller.py`.  It wraps a proposed
> output-simplex step \(s\), computes \(K^{CH}_p(s)s\), reports the local
> cubic fraction, and damps the step when the cubic response exceeds a
> configured trust target.  The prototype has been run on the saved
> weekday and month Llama-3.1-8B centroid matrices in both
> uniform-to-centroid and adjacent-cycle modes.  With the conservative
> trust target `max_cubic_fraction = 0.10`, all tested real centroid
> steps damp and the controlled cubic fraction is capped at `0.098`.

**Established mathematics.**

1. At the uniform categorical distribution, the centered simplex score frame
   is the Fisher score frame.
2. In the \(N=4\) tetrahedral row, the uniform raised cubic
   \(K^{CH}_{p_*}\) is the symmetric product generated by the Gram pairing
   and the projector squares \(I+K(\tau_i)^2\).
3. For a finite quotient algebra \(R\), additive characters decompose the
   Fisher tangent space into conductor packets.
4. Along an \(m\)-flat ray \(p(t)=p_*+th\), the off-centroid Fisher coupling
   between character lines has exact Taylor coefficients governed by
   character convolution.
5. The correct conductor-block compression is operator-valued; it lives in a
   quotient-character adjacency algebra rather than in scalar block traces.
6. The global adjacency algebra factors by CRT after including the trivial
   character, while the nontrivial Fisher tangent algebra is the augmentation
   corner.
7. The \({\mathbb F}_4[u]/(u^2)\) local row gives the first mixed tame/wild
   test where associated-graded conductor data is not enough.

**Measured on real transformers (layer 28, last-token).**

1. The weekday \(C_7\) \(K^{CH}\) script is implemented and run against the
   empirical \(7\times 7\) output centroid matrices from both
   Llama-3.1-8B and Mistral-7B-v0.3.
2. Correlations with cyclic Hellinger arc (behavior-manifold reference):

   | Metric | Llama-3.1-8B | Mistral-7B-v0.3 | Symmetric proxy |
   |---|---|---|---|
   | Hellinger chord | \(0.899815\) | \(0.916873\) | \(0.910010\) |
   | Moment Euclidean chord | \(\mathbf{0.614547}\) | \(\mathbf{0.714715}\) | \(0.886448\) |
   | Natural/logit chord | \(0.944337\) | \(0.955300\) | \(0.941295\) |
   | Fisher Levi-Civita | \(0.903176\) | \(0.922202\) | \(0.911776\) |

3. The moment chord correlation is substantially **below** both the
   symmetric proxy (\(r=0.886448\)) and the Wurgaft linear reference
   (\(r\approx 0.89\)) on both models, while the Hellinger, logit, and
   Fisher channels remain near or above the proxy.  This drop is consistent
   with the cubic diagnostic and consistent with the textbook
   categorical-Euclidean inadequacy; an extended-baseline comparison
   (§4.1.1) is reported as a control, showing that the moment-\(L^2\)
   drop is uniquely the worst but that the Fisher-equivalent family is
   not fully homogeneous at the chord level.
4. Both centroid matrices exhibit **asymmetric off-diagonal leakage**:
   most weekdays leak more probability to their cyclic predecessor than to
   their successor (Llama Monday\(\to\)Sunday \(0.271\) vs
   Monday\(\to\)Tuesday \(0.056\); Mistral Monday\(\to\)Sunday \(0.254\) vs
   Monday\(\to\)Tuesday \(0.043\)).  The pre-registered \(10^7\)-token C4
   bigram control (§4.1.2) lands in the intermediate band: corpus bigrams
   partially align with the transposed magnitude pattern, but sign
   agreement remains far below the "fully explain" threshold.  We
   therefore treat the asymmetry as consistent with both a learned sequence
   prior and residual off-centroid cyclic structure, not as standalone
   arithmetic evidence.
5. The month \(C_{12}\) cyclic script has been run on Llama-3.1-8B at
   layer 28 last-token features.  The moment-Euclidean chord correlation
   collapses from the proxy value \(r=0.696128\) to \(r=0.210147\) -- a
   much sharper drop than the \(C_7\) weekday row, as predicted when the
   output algebra acquires multiple conductors.
6. The CRT conductor energy decomposition of the empirical \(h_i\) places
   only \(0.380\) of the displacement energy in conductor 12 (full
   cyclic), with \(0.192\) in the mixed conductor 6 (\(C_4\times C_3\)),
   and the rest spread across conductors 2, 3, 4.  This is the first
   transformer measurement of the predicted CRT conductor split.
7. The activation pullback audit has been run on Llama-3.1-8B for both
   rows using the saved \(4096\)-dim residual-stream activations at
   layer 28.  On weekdays, the activation-distance vs Hellinger-chord
   correlation is \(r=0.937\) and the pullback metric coefficient of variation is
   \(0.154\); the embedding is therefore nearly a rescaled isometry of the
   behavior simplex, and the linear-versus-manifold gap measured in §4 is
   attributable primarily to the behavior-side \(K^{CH}\) cubic, not to
   activation distortion.  On months, activation-vs-Hellinger remains high
   (\(r=0.821\)) but activation-vs-cyclic-arc drops to \(r=0.652\) -- the
   activation embedding has CRT-structured geometry consistent with
   \(C_4\times C_3\), which is what makes both the pure-cyclic-arc
   reference and a moment linear summary underperform on months.
8. The **extended baseline comparison** (§4.1.1, §5.1.1) has been run on
   all three available centroid files (Llama-wd, Mistral-wd, Llama-mo)
   with nine metrics covering linear-\(L^p\), Fisher-equivalent
   quadratic, and cyclic-aware optimal-transport families.  Headline
   findings: moment-Euclidean drops are unique in magnitude but not in
   kind (total variation also drops); the Fisher-equivalent family is
   heterogeneous (symmetric-KL and Bhattacharyya drop more than
   Hellinger); and Wasserstein-1 with cyclic ground metric on
   \(\mathbb{Z}/N\) saturates at \(r\ge 0.986\) on both rows and both
   models — clean positive evidence that the centroids are genuine
   cyclic 1D distributions in the optimal-transport sense.

**Implemented optimizer diagnostic.**

1. The first local step-controller is implemented as
   `empirical/k_ch_step_controller.py`.  Its operational diagnostic is
   \[
   \rho_{\mathrm{frac}}(p,s)
   =
   {1\over2}
   {\|K^{CH}_p(s)s\|_{g_p}\over \|s\|_{g_p}},
   \]
   together with the scale-invariant directional ratio
   \[
   {\|K^{CH}_p(s)s\|_{g_p}\over \|s\|_{g_p}^2}.
   \]
   The default action is damping, not a claimed full optimizer:
   \(s\mapsto \alpha s\), where \(\alpha\) is chosen so that the
   controlled cubic fraction lies below the trust target and the step
   remains inside the simplex.
2. The smoke test verifies the raising identity
   \(g_p(K^{CH}_p(u)v,w)=T_p(u,v,w)\), the linear scaling of the cubic
   fraction under \(s\mapsto \alpha s\), the positivity guard near the
   simplex boundary, and the normalization of cyclic conductor packet
   energies.
3. On Llama-3.1-8B weekday centroids, the uniform-to-centroid run has
   raw cubic fractions from \(1.266\) to \(2.195\), with all seven
   steps damped to controlled cubic fraction \(0.098\).  The adjacent
   weekday run is more nonlinear, with raw cubic fractions up to
   \(10.298\).
4. On Llama-3.1-8B month centroids, the uniform-to-centroid run has raw
   cubic fractions from \(3.094\) to \(4.735\), and the adjacent-cycle
   run reaches \(56.427\).  The controller's conductor audit reproduces
   the CRT split: in the uniform month run, mean step-energy fractions
   are approximately \(0.380\) in conductor 12, \(0.192\) in conductor 6,
   \(0.173\) in conductor 4, \(0.169\) in conductor 3, and \(0.086\) in
   conductor 2.
5. The generated reports are
   `empirical/reports/weekdays_k_ch_step_controller_llama31_8b_uniform.md`,
   `empirical/reports/weekdays_k_ch_step_controller_llama31_8b_adjacent.md`,
   `empirical/reports/months_k_ch_step_controller_llama31_8b_uniform.md`,
   and
   `empirical/reports/months_k_ch_step_controller_llama31_8b_adjacent.md`.

**Open.**

1. Replicate the months CRT energy decomposition on a second model family
   (e.g.\ Mistral-7B).
2. Fit or estimate the Hessian terms of \(F\) (requires a local fit of
   \(F\) rather than centroid distances alone).
3. Sweep layer index on Llama and Mistral to test whether layer 28 is
   optimal for both, or whether the signature strength is layer-dependent.
4. Build an output task whose label algebra has at least two local layers,
   so that mixed support can be tested against the \({\mathbb F}_4[u]/(u^2)\)
   and higher local rows.
5. Benchmark the implemented local step-controller inside an actual
   training or steering loop, rather than only on saved output centroids.
6. Extend the C4 bigram-confound control beyond the completed \(10^7\)-token
   sample if desired.  The registered run over all three available centroid
   files lands in the intermediate band: it softens the §4.1 asymmetric-
   leakage interpretation but does not retract the §5.1 CRT conductor signal
   or the §7.2.1 pullback-isometry result.

## 1. The Optimization Question

A trained model turns internal states into output distributions.  On a local
concept region, write this as

$$
F:A\to \Delta_R^\circ,
$$

where \(A\) is an activation or representation manifold and
\(\Delta_R^\circ\) is the open categorical simplex on a finite output set
\(R\).  If the model assigns probabilities \(p_y\) to labels \(y\in R\), the
standard behavior-side information geometry is the Fisher metric

$$
g_p(u,v)=\sum_{y\in R}{u_yv_y\over p_y}.
$$

Natural gradient methods use this quadratic geometry to replace Euclidean
steps by statistically meaningful steps.  Equivalently, they precondition by
the Fisher information matrix rather than by a coordinate-dependent Euclidean
metric.

The dream of linear optimality is that a local coordinate system makes the
task flat enough for straight lines, quadratic losses, and scalar summaries
to be faithful.  Probability space does not generally grant that dream.  A
categorical simplex has a Fisher-Rao curvature, and the first place where
linear flattening pays a visible price is cubic order.

That quadratic object is necessary, but it is not the whole local geometry.
The loss of linearity begins at cubic order.  In information geometry, the
first cubic object is the Amari-Chentsov tensor

$$
T_p(u,v,w)=\sum_y {u_yv_yw_y\over p_y^2}.
$$

Raising one index by the Fisher metric gives the operator

$$
g_p(K^{CH}_p(u)v,w)=T_p(u,v,w),
$$

or, in moment coordinates on the categorical simplex,

$$
K^{CH}_p(u)v={uv\over p}-g_p(u,v)p.
$$

At the tetrahedral uniform point this coordinate expression has already
been stripped down to the intrinsic simplicial algebra of Murillo
[Murillo].  Let
\(p_*=\frac14{\bf 1}\), \(H=T_{p_*}\Delta_4^\circ\), \(M=4I-J\), and
\(\tau_i=e_i-\frac14{\bf 1}\).  Then \(g_{p_*}(u,v)=\langle u,v\rangle_M\),
and the centered vertex directions \(\tau_i\) are \(G\)-unit axes for the
intrinsic cross-product operator \(K(\tau_i)\) of that paper.  With
$$
P_i:=I+K(\tau_i)^2,
$$
the projector-square identity gives
$$
K^{CH}_{p_*}(u)v
=
\frac34\sum_{i=1}^4
\langle\tau_i,u\rangle_M P_i v.
$$
Equivalently,
$$
K^{CH}_{p_*}(u)v
=
\frac14\sum_{i=1}^4
\langle\tau_i,u\rangle_M\langle\tau_i,v\rangle_M\tau_i.
$$
In coordinates this is
\(4(u\odot v)-(\sum_i u_iv_i){\bf 1}\), but the displayed operator uses only the
Gram pairing and the symmetric projector squares \(I+K(\tau_i)^2\).  This is
the \(N=4\) calibration row: the antisymmetric cross-product algebra generates
the symmetric Amari-Chentsov cubic through its square/projector component.

Off the centroid, the exact deformation is controlled by the moving score
frame.  For any categorical point \(p\), define
\(\sigma_y(p)=e_y-p\).  Then
$$
K^{CH}_p(u)v
=
\sum_y p_y\,g_p(\sigma_y(p),u)\,g_p(\sigma_y(p),v)\,\sigma_y(p).
$$
If \(\Pi_y^p\) denotes the Fisher-orthogonal projector onto
\(\mathbb R\sigma_y(p)\), this becomes
$$
K^{CH}_p(u)v
=
\sum_y(1-p_y)\,g_p(\sigma_y(p),u)\,\Pi_y^p v.
$$
Thus the path \(p(t)=p_*+th\) does not merely change a scalar coefficient.
It moves the score axes, changes the Fisher metric, and changes the
projector weights.  In the tetrahedral \(N=4\) row,
\(\Pi_y^p=I+K_p(\widehat\sigma_y(p))^2\), where \(K_p\) is the
Fisher-Hodge cross-product operator at \(p\).  This is the precise
off-centroid version of the projector-square theorem.

Explicitly, for \(p\in\Delta_4^\circ\), write \(r_i=\sqrt{p_i}\).  With
\(\varepsilon_{1234}=+1\), the matrix entries are
$$
\bigl(K_p(u)\bigr)_{i\ell}
=
-\sum_{j,k=1}^4
\varepsilon_{ijk\ell}\frac{r_i r_j}{r_k r_\ell}u_k.
$$
For a \(g_p\)-unit axis \(u\), the local Fisher-Rodrigues tangent step is
$$
R_p(u,\theta)
=
I_H+\sin\theta\,K_p(u)+(1-\cos\theta)K_p(u)^2.
$$
At \(p_*=\frac14{\bf1}\), this reduces to the raw cyclic-difference matrix
\(\widetilde K(u)\), the \(M\)-normalized version of the original
simplicial cross product.

This is the first correction after the quadratic Fisher metric.  If the
Fisher metric is the local object that natural gradient sees, \(K^{CH}\) is
the first local object it does not see unless the optimizer is explicitly
cubic-aware.

This makes curvature an information signal rather than a nuisance term.  If a
linear summary erases the first within-block invariant, the lost term is not
merely aesthetic geometry.  It is structured behavior information that the
quadratic approximation has flattened.

For a learned map \(F\), the quadratic pullback is

$$
G_F=J_F^\top g_y J_F.
$$

A cubic-aware diagnostic asks for the next piece:

1. the intrinsic behavior-side cubic \(K^{CH}\) on \(\Delta_R^\circ\);
2. the activation-side distortion in \(J_F^\top g_yJ_F\);
3. the covariant Hessian terms of \(F\);
4. residual parameterization error from sampling, spline choice, or output
   directions outside the chosen quotient packet.

This is the diagnostic problem addressed in the present work.  When the output labels carry the structure of a finite algebra \(R\), the first structured correction beyond the quadratic Fisher metric is indexed by a finite quotient-character adjacency algebra.  The practical question for optimization and representation geometry then becomes: can we predict which nonlinear Fisher curvature channels will appear, and whether they concentrate on mixed tame/wild support, before measuring the full network?

## 2. Behavior Manifolds Are Fisher-Hellinger Manifolds

The map

$$
p\mapsto \sqrt p
$$

identifies the categorical Fisher-Rao metric with the round metric on the
positive orthant of the unit sphere, up to the standard factor of four.  This
is why Hellinger distances are not an arbitrary embedding trick.  They are a
spherical presentation of the same Fisher geometry.

For AI experiments that compare activation geometry with behavior geometry,
this matters.  If the behavior manifold is measured by Hellinger geodesics,
then the comparison is already an information-geometric comparison.  The
activation manifold is being asked whether its learned distances pull back the
Fisher/Hellinger geometry of output distributions.

The local failure mode is therefore precise.  A straight line in logits,
probabilities, or activations need not match a Fisher/Hellinger geodesic.  The
quadratic metric sees infinitesimal lengths, but the cubic tensor sees how
the flat affine structures and the Fisher sphere begin to diverge.

In the dually flat language, the categorical simplex has \(m\)-flat moment
coordinates and \(e\)-flat natural coordinates.  The raised cubic

$$
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)}
$$

records the gap between those flat connections.  In optimizer language, this
is a structured third-order correction to the local Fisher approximation.

## 3. The Discrete Skeleton Under the Smooth Geometry

If \(R\) is only a set of labels, the categorical simplex still has Fisher
geometry.  If \(R\) is a finite algebra, more structure appears.

At the uniform distribution

$$
p_* = |R|^{-1}{\bf 1},
$$

the zero-sum tangent space

$$
H_R=\{h\in {\mathbb C}^R:\sum_x h_x=0\}
$$

has an additive-character basis.  In ML terms, this is the finite Fourier
basis of the output algebra.  The Fisher metric at \(p_*\) is diagonal in
that basis.  Grouping characters by conductor gives conductor packets, which
act like arithmetic frequency-depth bands.

The centroid statement is clean:

> At maximum entropy, conductor packets are Fisher-orthogonal behavior
> directions.

The off-centroid statement is more important for optimization:

> Away from maximum entropy, the packets stop being orthogonal, but the
> packet coupling is controlled by finite character convolution.

Along an \(m\)-flat ray

$$
p(t)=p_*+th,
$$

the normalized Fisher matrix element between character lines
\({\mathbb C}\chi\) and \({\mathbb C}\psi\) has the exact expansion

$$
\bar g^F_{p(t)}(e_\chi,e_\psi)
=
\sum_{n\ge0}(-t)^n\widehat h^{*n}(\psi\chi^{-1}).
$$

This formula is the bridge.  The smooth Fisher tensor has discrete Taylor
indices: quotient characters \(\psi\chi^{-1}\) and their convolution powers.

The scalar conductor compression is not enough.  It can erase within-block
structure.  The right finite object is the quotient-character adjacency
algebra with partial shifts

$$
A_\eta^{\mathfrak f,\mathfrak e}e_\chi
=
\begin{cases}
e_{\eta\chi},&
\chi\in X_{\mathfrak e},\ \eta\chi\in X_{\mathfrak f},\\
0,&\text{otherwise.}
\end{cases}
$$

The \(n\)-th compressed coefficient is

$$
C_n^{[\mathfrak f,\mathfrak e]}(h)
=
\sum_\eta \widehat h^{*n}(\eta)
A_\eta^{\mathfrak f,\mathfrak e}.
$$

In ML language, this says that output-space Fisher couplings have a finite
operator basis.  The basis is not learned from the network.  It is supplied
by the finite label algebra.  The network only chooses the coefficient vector
through its output displacement \(h\) and through the activation-to-behavior
map \(F\).

This is the exact point where "curvature versus linear optimality" becomes a
finite statement.  Scalar trace compression asks for one flat number per
block interaction.  The quotient-character adjacency algebra keeps the
operator-valued carry data.  In the mixed rows, that difference is the
difference between seeing the first genuine within-block invariant and
averaging it away.

## 4. The Weekday Task as the Prime Control

The Wurgaft weekday experiment is the cleanest AI-facing control because the
label set has a natural cyclic structure:

$$
R=C_7.
$$

Since \(7\) is prime, the nontrivial tangent space is one six-dimensional
conductor packet.  There is no tame/wild split, no conductor-depth extension,
and no mixed local support.  That makes weekdays the no-\(\operatorname{Ext}_{CH}\)
control row.

At the uniform distribution,

$$
K^{CH}_{p_*}(h)v=7h*v-7\langle h,v\rangle p_*.
$$

Equivalently, for the normalized additive characters

$$
\phi_k(x)=7^{-1/2}\exp(2\pi ikx/7),
$$

one has, for \(\ell\ne0\),

$$
K^{CH}_{p_*}(h)\phi_\ell
=
\sqrt 7\sum_{k=1}^6 \widehat h_{k-\ell}\phi_k.
$$

This is as simple as the theory gets.  The full nontrivial curvature support
is one cyclic convolution operator.

The conductor reason is elementary.  Identify the character group of
\(C_7\) with \(\mathbb F_7\).  If
\(0\ne h\in H_{C_7}\), then
\(\operatorname{supp}\widehat h\subseteq\mathbb F_7^\times\) is nonempty, and
every nonzero character has conductor \(7\).  Choosing any
\(k\in\operatorname{supp}\widehat h\), the sums

$$
k,\;2k,\;\ldots,\;6k
$$

run through all of \(\mathbb F_7^\times\).  Therefore the convolution support
envelope through order \(6\) contains every nontrivial quotient character.
This is the exact sense in which prime cyclic off-centroid coupling is
eventually total: there is no conductor packet, CRT factor, or tame/wild layer
left to form a boundary.  Individual Taylor coefficients may still vanish by
coefficient cancellation; such zeros are sparsity inside the single packet, not
surviving conductor isolation.

The commutator of two \(K^{CH}\) operators at the centroid,
\([K^{CH}_{p_*}(u),K^{CH}_{p_*}(v)](w)=N(\langle u,w\rangle v-\langle v,w\rangle u)\),
is the round-sphere Levi-Civita curvature at scale \(N\).  This formula
holds for every \(N\), prime or composite; the fact that \(7\) is prime
introduces no simplification at the Riemannian level.  What \emph{is}
special about the prime row is algebraic: one conductor packet,
\(\operatorname{Ext}_{CH}(C_7)=0\), and irreducible Hayes-normalizer action.

A Jordan-Lie refinement makes the split sharper.  The Lie bracket of
\(K^{CH}\) controls the universal sphere-curvature baseline, while the
Jordan product keeps the symmetric quotient-shift terms in the
character-basis matrix.  At the centroid the abstract Jordan-Lie envelope
is still conductor-blind; conductor packets and possible
\(\operatorname{Ext}_{CH}\) carriers enter only after projecting that
symmetric part into the quotient-character adjacency algebra and
comparing the filtered local algebra with its associated graded.

**Diagnostic: zero cross-conductor cubic signal.**  The \(n=1\) diagonal
entry of the within-packet coupling operator equals \(\widehat h(0)=0\)
for any \(h\in H_{C_7}\) -- this tracelessness is universal across all
\(N\).  Beyond the diagonal, the stronger prime-row property is that
\(\mathcal A_{C_7}\) contains \emph{no cross-conductor operators} (there
is only one conductor packet).  Therefore the cross-conductor cubic
Fisher correction -- the first term in the off-centroid expansion of
\(g^F\) that could differ structurally between a prime and a composite
label group -- is identically absent for \(C_7\) at every Taylor order.
This is the \emph{zero-cross-cubic control} property: any measured
correlation residual in the \(C_7\) weekday row cannot be attributed to
conductor-filtration signal, and must instead arise from within-packet
Fisher coupling, Hessian-of-\(F\) geometry, or sampling error.

### 4.1 Real transformer measurement (Llama-3.1-8B and Mistral-7B-v0.3, layer 28)

The \(7\times 7\) weekday output centroid matrix was obtained by running the
causalab `weekdays` pipeline at layer 28 last-token features on two
independent model families:

1. **Llama-3.1-8B**, the model used by Wurgaft et al.
2. **Mistral-7B-v0.3**, included as a cross-family replication.

Each row \(i\) of a centroid matrix is the model's output distribution over
\(\{\text{Mon},\ldots,\text{Sun}\}\) when the input prompt encodes weekday
\(i\).

**Llama-3.1-8B centroids.**

| Input \ Output | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Monday    | **0.636** | 0.056 | 0.009 | 0.009 | 0.006 | 0.014 | 0.271 |
| Tuesday   | 0.116 | **0.749** | 0.073 | 0.015 | 0.009 | 0.015 | 0.023 |
| Wednesday | 0.018 | 0.110 | **0.737** | 0.062 | 0.026 | 0.020 | 0.026 |
| Thursday  | 0.015 | 0.012 | 0.069 | **0.773** | 0.097 | 0.015 | 0.020 |
| Friday    | 0.008 | 0.009 | 0.005 | 0.070 | **0.833** | 0.050 | 0.025 |
| Saturday  | 0.010 | 0.005 | 0.005 | 0.004 | 0.144 | **0.748** | 0.083 |
| Sunday    | 0.028 | 0.009 | 0.003 | 0.008 | 0.004 | 0.051 | **0.897** |

**Mistral-7B-v0.3 centroids.**

| Input \ Output | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Monday    | **0.665** | 0.043 | 0.006 | 0.005 | 0.008 | 0.019 | 0.254 |
| Tuesday   | 0.154 | **0.774** | 0.025 | 0.010 | 0.006 | 0.009 | 0.023 |
| Wednesday | 0.014 | 0.243 | **0.692** | 0.031 | 0.007 | 0.004 | 0.011 |
| Thursday  | 0.002 | 0.006 | 0.082 | **0.869** | 0.031 | 0.004 | 0.007 |
| Friday    | 0.002 | 0.001 | 0.004 | 0.191 | **0.782** | 0.014 | 0.006 |
| Saturday  | 0.005 | 0.003 | 0.001 | 0.008 | 0.274 | **0.687** | 0.022 |
| Sunday    | 0.047 | 0.006 | 0.003 | 0.005 | 0.020 | 0.284 | **0.634** |

The measured correlations with the cyclic Hellinger arc behavior-manifold
reference are

| Metric | Llama-3.1-8B | Mistral-7B-v0.3 | Symmetric proxy |
|---|---|---|---|
| Hellinger chord vs cyclic arc | \(r=0.899815\) | \(r=0.916873\) | \(0.910010\) |
| Moment Euclidean chord vs cyclic arc | \(r=\mathbf{0.614547}\) | \(r=\mathbf{0.714715}\) | \(0.886448\) |
| Natural/logit chord vs cyclic arc | \(r=0.944337\) | \(r=0.955300\) | \(0.941295\) |
| Fisher Levi-Civita distance vs cyclic arc | \(r=0.903176\) | \(r=0.922202\) | \(0.911776\) |

Three structural observations.

First, the **moment Euclidean chord correlation drops sharply on both
models**: from the proxy value \(r=0.886\) to \(r=0.615\) on Llama and
\(r=0.715\) on Mistral.  All three Fisher/Hellinger-aware metrics either
match or exceed their proxy values on both models.  In information
geometry it is a textbook result that Euclidean-on-\(p\) is a poor
descriptor of statistical distance, so this drop, taken alone, only
re-establishes that well-known inadequacy.  The extended baseline
comparison in §4.1.1 sharpens the picture: the moment drop is uniquely
the largest in a wider family of metrics, but not the only one that
falls, and the cubic-specific claim of this paper rests on the §5.1 CRT
conductor energy decomposition rather than on this chord correlation.

Second, both centroid matrices are visibly **asymmetric**: every weekday
leaks substantially more probability to its cyclic predecessor than to its
cyclic successor on Mistral (Monday→Sunday \(0.254\) vs Monday→Tuesday
\(0.043\); Wednesday→Tuesday \(0.243\) vs Wednesday→Thursday \(0.031\)).
On Llama the predecessor bias is still present but weaker and partially
mixed with successor bias (Thursday→Wednesday \(0.069\) vs
Thursday→Friday \(0.097\)).  We ran the pre-registered linguistic-bigram
control on a \(10^7\)-token C4 English sample, comparing the empirical
centroid asymmetry against both same-alignment and transposed-alignment
corpus asymmetries.  The result lands in the pre-registered intermediate
band: on the \(w=3\) window, Llama gives transposed-alignment
\(r=0.424\) with sign agreement \(9/21\), while Mistral gives
\(r=0.690\) with sign agreement \(10/21\); at \(w=5\), Mistral reaches
\(r=0.739\) but still only \(10/21\) sign agreement.  Thus ordinary
pretraining sequences explain part of the magnitude pattern, especially
for Mistral, but do not fully determine the asymmetry under the
pre-registered joint criterion.  The asymmetric leakage should therefore
be read as consistent with both a learned sequence prior and an
off-centroid cyclic signal, rather than as independent evidence by itself.

Third, the **cross-model replication argues against the signature being a
layer-selection artifact**.  Layer 28 was originally chosen for Llama, and
its applicability to Mistral was a working hypothesis.  The fact that both
models produce the same correlation ordering — Fisher/logit/Hellinger near
proxy, moment far below — at the same layer index suggests the signature
is structural to the prime \(C_7\) row, not specific to either model's
internal layout.  A formal layer sweep is still warranted to rule out the
possibility that layer 28 is simultaneously suboptimal for both.

Computed \(K^{CH}_{p_*}(h_i)\) Frobenius norms per input centroid (in the
centroid-normalized character convention of Appendix A):

| Weekday | Llama-3.1-8B | Mistral-7B-v0.3 |
|---|---|---|
| Monday | \(40.3\) | \(41.9\) |
| Tuesday | \(45.8\) | \(48.1\) |
| Wednesday | \(44.9\) | \(43.6\) |
| Thursday | \(47.5\) | \(54.6\) |
| Friday | \(51.8\) | \(49.2\) |
| Saturday | \(46.2\) | \(44.1\) |
| Sunday | \(\mathbf{56.5}\) | \(40.5\) |

The largest displacement on Llama lands on Sunday, which has the highest
self-confidence in the matrix (peak \(0.897\)); on Mistral it lands on
Thursday (peak \(0.869\)).  The norm distribution thus tracks which
weekday each model has crystallized most confidently, consistent with
\(h_i = p_i - p_*\) determining the operator scale.

(See §12 for reproduction details.)

The empirical interpretation should remain strict:

> Weekdays test whether the prime \(C_7\) behavior-side cubic explains
> the simple cyclic output geometry.  They do not test the mixed
> arithmetic extension class, because no such class exists in the prime
> row.  The activation-pullback residual is closed in §7.2.1; the
> Hessian-of-\(F\) residual remains open.

### 4.1.1 Extended metric baseline comparison

The four-metric table of §4.1 invites a methodological objection: that
the moment-Euclidean drop only re-establishes the well-known inadequacy
of \(L^2\) on the categorical simplex rather than isolating any
cubic-specific signal.  To probe this, we ran the same pairwise
correlation analysis using nine metrics rather than four.  The added
baselines span three independent axes: (i) order in \(p-q\) — linear
(moment, total variation) versus quadratic (Hellinger, Jensen-Shannon,
symmetric KL, Bhattacharyya, Fisher Levi-Civita, natural/logit);
(ii) Fisher-equivalence at small distance; and (iii) explicit awareness
of the cyclic ground structure on \(\mathbb{Z}/7\) — the
Wasserstein-1 distance with unit cyclic ground metric is the only
baseline in the family that uses the \(C_7\) algebra directly without
being Fisher-equivalent.

The expanded correlations against the cyclic Hellinger arc are
(\(\Delta = r_{\text{real}} - r_{\text{proxy}}\); proxy values from
`extended_metric_baselines.py` at \(\beta=2.5\), so they differ
slightly from the §4.1 proxy column):

| Metric | Category | Fisher-eq | Cyclic-aware | Proxy r | Llama r | Mistral r | Llama \(\Delta\) | Mistral \(\Delta\) |
|---|---|---|---|---:|---:|---:|---:|---:|
| Moment Euclidean | linear-\(L^2\) | no | no | \(0.883\) | \(\mathbf{0.615}\) | \(\mathbf{0.715}\) | \(\mathbf{-0.27}\) | \(\mathbf{-0.17}\) |
| Total variation | linear-\(L^1\) | no | no | \(1.000\) | \(0.894\) | \(0.863\) | \(-0.11\) | \(-0.14\) |
| Hellinger chord | quad-Fisher | yes | no | \(0.923\) | \(0.900\) | \(0.917\) | \(-0.02\) | \(-0.01\) |
| Jensen-Shannon distance | quad-Fisher | yes | no | \(0.938\) | \(0.895\) | \(0.898\) | \(-0.04\) | \(-0.04\) |
| Symmetric KL | quad-Fisher | yes | no | \(1.000\) | \(0.901\) | \(0.943\) | \(-0.10\) | \(-0.06\) |
| Bhattacharyya | quad-Fisher | yes | no | \(0.987\) | \(0.925\) | \(0.961\) | \(-0.06\) | \(-0.03\) |
| Fisher Levi-Civita | quad-Fisher | yes | no | \(0.928\) | \(0.903\) | \(0.922\) | \(-0.03\) | \(-0.01\) |
| Natural/logit chord | quad-natural | (\(\sim\)quad) | no | \(0.982\) | \(0.944\) | \(0.955\) | \(-0.04\) | \(-0.03\) |
| **Wasserstein-1 cyclic** | OT, ground \(=\mathbb{Z}/7\) | no | **yes** | \(1.000\) | \(\mathbf{0.992}\) | \(\mathbf{0.986}\) | \(\mathbf{-0.01}\) | \(\mathbf{-0.01}\) |

Three readings.

*First,* the moment-\(L^2\) chord drop is **not** a uniform
\(L^p\)-on-\(p\) phenomenon.  Total variation also drops, but by less
than half as much on Llama (\(-0.27\) versus \(-0.11\)) and by a slightly
smaller margin on Mistral (\(-0.17\) versus \(-0.14\)).  The
moment-Euclidean chord is uniquely the worst-correlating metric across
both models — consistent with, but stronger than, the textbook
expectation alone would predict.

*Second,* the Fisher-equivalent family is itself heterogeneous at the
chord level.  Hellinger, Fisher-Levi-Civita, and natural/logit-chord
stay essentially at their proxy values (\(|\Delta| \le 0.04\) across
both models), but symmetric-KL drops by \(0.10\) on Llama and
Bhattacharyya by \(0.06\).  Infinitesimal Fisher-equivalence does not
preclude divergent chord-level behavior on the empirical centroids; the
most sensitive metrics — those that emphasize ratios or low-overlap
regions — drop the most.  This is itself a small departure from the
strict "Fisher good / Euclidean bad" framing the four-metric table
suggested.

*Third,* the strongest correlation with the cyclic-Hellinger-arc
reference is the **Wasserstein-1 distance with unit cyclic ground
metric on \(\mathbb{Z}/7\)**: \(r=0.992\) on Llama, \(r=0.986\) on
Mistral, essentially saturating its proxy value.  This metric is *not*
Fisher-equivalent — it is optimal transport on a cyclic graph — but it
is the only baseline that explicitly uses the \(C_7\) ground structure.
Its near-perfect agreement with the cyclic-Hellinger arc on both real
models says the empirical centroids are genuine cyclic 1D distributions
in the transport-cost sense, independent of any Fisher-Hellinger
choice.  This is the cleanest single-metric piece of evidence in the
table that the relevant geometric structure is the cyclic algebra of
\(\mathbb{Z}/7\), and it does not depend on cubic curvature for its
interpretation.

The honest reading of the full table is therefore: the moment-Euclidean
drop is consistent with — and slightly sharper than — the textbook
categorical-Euclidean inadequacy, while the Wasserstein-1 cyclic
saturation gives clean positive evidence that the empirical centroids
respect the \(C_7\) ground structure.  Neither result alone isolates
the cubic Amari-Chentsov tensor as the agent.  The cubic-specific
empirical evidence in this paper is in §5.1 (CRT conductor energy
decomposition) and in the predicted conductor-block isolation, both
of which require the additive-character basis of the output algebra
and have no chord-metric analogue.

### 4.1.2 Linguistic-bigram control (C4 run completed)

The predecessor-bias asymmetry observed above could in principle be
explained by pretraining-bigram frequencies: sequences such as "Sunday
Monday" and "from Saturday to Sunday" are common in English web text,
so a model trained on that text would have correspondingly asymmetric
adjacency representations.  We therefore pre-registered a corpus control
in `Note_bigram_confound_design.md`.  The completed run scans
10,000,000 whitespace tokens from the C4 English train stream
(`allenai/c4`, `en`; 27,548 documents) and compares the empirical centroid
asymmetry \(A^{\text{emp}} = M_{\text{cent}} - M_{\text{cent}}^\top\)
against both same-alignment and transposed-alignment corpus asymmetries.
The transposed alignment corresponds to the reviewer's specific
hypothesis: a pretraining "\(d_i\) followed by \(d_j\)" co-occurrence
deposits mass at \(M_{\text{corp}}[i,j]\), which would manifest in the
confusion matrix at \(M_{\text{cent}}[j,i]\).

The pre-registered thresholds were: "fully explain" if Pearson
\(r \ge 0.70\) and sign agreement \(\ge 18/21\); "do not explain" if
\(r \le 0.20\) and sign agreement \(\le 13/21\); otherwise
"intermediate."  The C4 run lands in the **intermediate** band on all
three available centroid files:

| target | window | alignment | asymmetry \(r\) | sign agreement | verdict |
|---|---:|---|---:|---:|---|
| Llama weekdays | \(w=3\) | transposed | \(0.424\) | \(9/21\) | intermediate |
| Llama weekdays | \(w=5\) | transposed | \(0.392\) | \(9/21\) | intermediate |
| Mistral weekdays | \(w=3\) | transposed | \(0.690\) | \(10/21\) | intermediate |
| Mistral weekdays | \(w=5\) | transposed | \(0.739\) | \(10/21\) | intermediate |
| Llama months | \(w=3\) | transposed | \(0.359\) | \(35/60\) | intermediate |
| Llama months | \(w=5\) | transposed | \(0.320\) | \(38/65\) | intermediate |

Thus corpus bigrams carry real explanatory power for the magnitude of the
transposed asymmetry, especially on Mistral, but they do not fully explain
the sign pattern under the joint pre-registered criterion.  We therefore
weaken the qualitative claim: the asymmetric off-diagonal structure
reflects both a learned pretraining-sequence prior and a residual
off-centroid cyclic signal registered by the empirical cubic diagnostic.
The orthogonal evidence -- the moment-vs-Hellinger/Fisher metric gap,
the CRT conductor-energy spread on \(C_{12}\), and the activation-pullback
near-isometry -- does not depend on the directional asymmetry and is
unaffected by this finding.  Full reports are
`empirical/reports/bigram_corpus_control_weekdays_llama31_8b_c4_10M.md`,
`empirical/reports/bigram_corpus_control_weekdays_mistral_7b_c4_10M.md`,
`empirical/reports/bigram_corpus_control_months_llama31_8b_c4_10M.md`,
and `empirical/reports/bigram_corpus_control_c4_10M_summary.md`.

## 5. The Month Task as the CRT Control

The next neural-facing control should be month-of-year reasoning.  Its label
set is

$$
C_{12}\cong C_4\times C_3.
$$

This is not yet a local finite-field row, but it is no longer prime.  The
nontrivial additive-character packets split by conductor:

| conductor | dimension | \(2\)-part | \(3\)-part |
|---:|---:|---:|---:|
| \(2\) | \(1\) | \(2\) | \(1\) |
| \(3\) | \(2\) | \(1\) | \(3\) |
| \(4\) | \(2\) | \(4\) | \(1\) |
| \(6\) | \(2\) | \(2\) | \(3\) |
| \(12\) | \(4\) | \(4\) | \(3\) |

Thus the \(C_4\) factor already sees \(2\)-primary conductor depths
\(1,2,4\), while the \(C_3\) factor supplies a tame companion.  This makes
months the right second control: one step above the prime \(C_7\) weekday
row and one step below the genuinely local
\({\mathbb F}_4[u]/(u^2)\) positive row.

The boundary is important.  \(C_{12}\) tests mixed conductor splitting in a
semisimple cyclic label algebra.  It does not by itself test nilpotent carry,
principal units, or the \(\operatorname{Ext}_{CH}\) obstruction.  A month
measurement would say whether the Wurgaft-style activation/behavior pipeline
sees the CRT product structure before we invoke local tame/wild carry data.

**CRT isolation prediction.**  As a consequence of the CRT factorization
of the adjacency algebra (Appendix A), the Fisher Taylor coupling
between the 4-primary character packet
\(\{3,6,9\}\subset\mathbb{Z}/12\) and the 3-primary packet \(\{4,8\}\) is
identically zero at every order \(n\ge 1\), as long as the model's
centroid displacement \(h=p_i-p_*\) is supported on only one CRT primary
block.  Concretely: if the transformer's confusion between months is
purely "quarterly" (displacement Fourier-supported on multiples of 3) or
purely "trimestral" (multiples of 4), the Fisher adjacency matrix is
block-diagonal between these two families.  Mixed displacements break
the isolation starting at the quadratic term.  This is the first
structural prediction that requires \(N\) to be composite and that has
no analogue in the weekday \(C_7\) row -- the prime group has no proper
nontrivial subgroup and therefore no isolated block.

The parametric \(C_{12}\) proxy is retained as a calibration reference.
With the symmetric month proxy it gives:

1. Hellinger chord versus cyclic Hellinger arc: \(r=0.729101\);
2. moment Euclidean chord versus cyclic Hellinger arc: \(r=0.696128\);
3. natural/logit chord versus cyclic Hellinger arc: \(r=0.773256\);
4. Fisher Levi-Civita endpoint distance versus cyclic Hellinger arc:
   \(r=0.732249\).

### 5.1 Real transformer measurement (Llama-3.1-8B, layer 28)

The \(12\times 12\) months output centroid matrix was obtained by running
the causalab `months_8b_pipeline` on Llama-3.1-8B, last-token features at
layer 28.

The measured correlations are

| Metric | Llama-3.1-8B | Symmetric proxy |
|---|---|---|
| Hellinger chord vs cyclic arc | \(r=0.708696\) | \(0.729101\) |
| Moment Euclidean chord vs cyclic arc | \(r=\mathbf{0.210147}\) | \(0.696128\) |
| Natural/logit chord vs cyclic arc | \(r=0.870898\) | \(0.773256\) |
| Fisher Levi-Civita distance vs cyclic arc | \(r=0.713899\) | \(0.732249\) |

**The moment-Euclidean correlation collapses from the proxy value
\(r=0.696\) to \(r=0.210\)** -- a much more dramatic drop than the
\(C_7\) row's collapse from \(0.886\) to \(0.615\).  The Hellinger and
Fisher channels also drop relative to their proxy values, by a few points
each; only the logit channel slightly improves (\(0.773 \to 0.871\)).
This is the expected sharpening of the cubic signature when the output
algebra acquires multiple conductors: moment-coordinate linear summaries
are maximally penalized when the geometry to be summarized is no longer a
single cyclic loop but a CRT-decomposed product manifold.

**CRT conductor energy decomposition.**  Each empirical displacement
\(h_i=p_i-p_*\) decomposes under the unitary discrete Fourier transform
into the conductor packets of \(C_{12}\).  Aggregated over the twelve
input months, the energy fractions are

| conductor | aggregate fraction |
|---|---|
| \(2\) (global up/down) | \(0.086\) |
| \(3\) (\(C_3\) tame factor) | \(0.169\) |
| \(4\) (\(C_4\) 2-part) | \(0.173\) |
| \(6\) (\(C_4\times C_3\) mixed) | \(\mathbf{0.192}\) |
| \(12\) (full cycle) | \(0.380\) |

A purely dihedral signal would place all weight in conductor 12.  Instead
the empirical displacements spread across the full CRT ladder, with the
mixed conductor-6 packet carrying slightly more energy than either the
pure conductor-3 or conductor-4 packet.  This is the first transformer
measurement of the predicted CRT conductor split, and it is a structural
feature that the symmetric parametric proxy could not see at all: the
proxy lives entirely in conductor 12 by construction.

**Centroid asymmetries.**  Most months show very high self-confidence
(diagonal entries \(0.86\)--\(0.95\)), with January as the visible outlier
(diagonal \(0.667\), leakage \(0.149\) to December -- the same
predecessor-bias pattern observed on weekdays).  April unusually leaks
backward to March (\(0.113\)) rather than forward to May (\(0.048\)).

\(K^{CH}_{p_*}(h_i)\) Frobenius norms per input month range from
\(127.3\) (Jan) to \(184.7\) (Nov), tracking self-confidence: the most
confidently predicted months produce the largest off-centroid
displacements.  The norm spread is roughly \(3\times\) the \(C_7\) range,
consistent with the larger ambient dimension and richer conductor
structure.

### 5.1.1 Extended metric baselines on \(C_{12}\)

The extended-baselines analysis introduced in §4.1.1 was rerun on the
\(C_{12}\) months centroid; the drop pattern is qualitatively the same
as on weekdays but sharper.

| Metric | Category | Cyclic-aware | Proxy r | Llama r | Llama \(\Delta\) |
|---|---|---|---:|---:|---:|
| Moment Euclidean | linear-\(L^2\) | no | \(0.690\) | \(\mathbf{0.210}\) | \(\mathbf{-0.48}\) |
| Total variation | linear-\(L^1\) | no | \(0.845\) | \(0.643\) | \(-0.20\) |
| Hellinger chord | quad-Fisher | no | \(0.741\) | \(0.709\) | \(-0.03\) |
| Jensen-Shannon distance | quad-Fisher | no | \(0.756\) | \(0.666\) | \(-0.09\) |
| Symmetric KL | quad-Fisher | no | \(0.902\) | \(0.752\) | \(-0.15\) |
| Bhattacharyya | quad-Fisher | no | \(0.973\) | \(0.742\) | \(\mathbf{-0.23}\) |
| Fisher Levi-Civita | quad-Fisher | no | \(0.748\) | \(0.714\) | \(-0.03\) |
| Natural/logit chord | quad-natural | no | \(0.960\) | \(0.871\) | \(-0.09\) |
| **Wasserstein-1 cyclic** | OT, ground \(=\mathbb{Z}/12\) | **yes** | \(0.999\) | \(\mathbf{0.993}\) | \(\mathbf{-0.01}\) |

Moment-Euclidean drops by \(-0.48\) — the largest drop in the table —
and total variation by \(-0.20\), both in the "drops sharply" band.
Bhattacharyya drops by \(-0.23\), more than any other Fisher-equivalent
metric, which is consistent with the much higher per-class
self-confidence on months (most diagonals \(\ge 0.86\)): low-overlap
regions amplify log-likelihood-style distances.  Hellinger,
Fisher-Levi-Civita, Jensen-Shannon, and natural/logit-chord stay within
\(0.09\) of proxy.  The Wasserstein-1 cyclic metric again essentially
saturates at \(r=0.993\), confirming on the \(C_{12}\) row what was
visible on \(C_7\): the model's centroids are genuine cyclic 1D
distributions in the optimal-transport sense, whether the cyclic
structure is prime or composite.  As on weekdays, the
cubic-specific empirical content of this paper rests on the CRT
conductor energy decomposition above and not on the chord-correlation
table.

## 6. Tame Motion, Wild Motion, and the Positive Test

The minimal positive local test is

$$
{\mathbb F}_4[u]/(u^2).
$$

This tiny algebra is the first row where two mechanisms meet:

1. a tame Frobenius layer from \({\mathbb F}_4\);
2. a wild principal-unit depth layer from \(u^2=0\).

The terminology is useful beyond the arithmetic specialists.

**Tame motion** is the clean rotational motion coming from the residue field:
Frobenius symmetry, cyclic packets, and predictable finite Fourier behavior.
The weekday \(C_7\) row is pure tame motion.  There is one nontrivial packet
and no extension class.

**Wild motion** is the depth motion coming from nilpotent or higher
congruence layers: principal units, conductor filtration, and nested
distortion inside a finite local algebra.

The real drama begins when tame and wild motion occupy the same behavior
algebra.  In the arithmetic language,
\({\mathbb F}_4[u]/(u^2)\) is the first mixed tame/wild local row.  In ML
language, it is the first finite behavior space where "frequency band" is not
enough.  There is an internal extension datum telling us how the coarse
layers glue together off the centroid.

That datum is called

$$
\operatorname{Ext}_{CH}.
$$

The subscript records its role in the Carlitz-Hayes or conductor-Hayes
quotient-character setting.  Conceptually, it measures whether a
macrovariable that looks closed at the centroid remains closed for the
off-centroid Fisher adjacency algebra.

This is the right kind of object for AI diagnostics.  Neural networks often
look linear or separable under one probe, then leak structured information
under a more sensitive probe.  \(\operatorname{Ext}_{CH}\) is a finite
version of that phenomenon:

> A quotient output macrovariable can be closed as a coarse statistic while
> still leaking Fisher-geometric information through off-centroid coupling.

Finite computations over \({\mathbb F}_4[u]/(u^2)\) (summarized in
Appendix B) show that the quotient-character adjacency algebra retains
mixed support information that the associated graded can lose.  The
lesson for the AI-facing story is not that every neural task literally
has the local algebra \({\mathbb F}_4[u]/(u^2)\).  The lesson is that
multi-layer output algebras can have finite curvature channels that a
scalar coarse statistic cannot see.

The finite audit matters because it removes vagueness from the story.  The
program does not merely gesture at curvature; it enumerates the board on
which curvature moves.  In the \({\mathbb F}_4[u]/(u^2)\) row, the local
constructor reproduces the mixed support counts \(4438/592\), the
cohomological orbit data \(210/5\), the arity-4 orbit data \(3165/18\), and
the paired-slot distribution \(-1:44,\ 1:504,\ 2:44\).  Those numbers are not
the headline for an ML reader, but they are the trust anchor: the tame/wild
collision is a finite object that can be audited cell by cell.

The mixed empirical prediction is:

> If an output task has at least two local layers, then the residual after the
> behavior-side prime controls should not be structureless noise.  It should
> land on the mixed support channels selected by the quotient-character tower.

There is a useful continuous negative control.  For
\(R={\mathbb F}_4[u]/(u^2)\), a strictly tame ray keeps \(p(t)\) constant on
nilpotent fibers.  The moving-score formula then preserves the tame
subspace: tame inputs tested against wild characters have zero
\(K^{CH}_{p(t)}\) coefficient to all orders.  Therefore the desired leakage
is not "pure tame bends into wild."  It is a mixed derivative phenomenon:
once a wild component is present, the raw continuous cubic has wild
coefficients, and after subtracting the pure tame and pure wild axes the
surviving \(srt^2\) composition/carry is the \(\operatorname{Ext}_{CH}\)
signal.

## 7. The Experimental Program

The empirical program is organized as a four-stage pipeline.

### 7.1 Behavior-Side Cubic Control

Input:

1. a finite output label algebra \(R\);
2. empirical output centroids \(p_i\in\Delta_R^\circ\);
3. pairwise behavior-manifold distances, preferably Fisher/Hellinger
   geodesic distances;
4. pairwise linear baselines in logits, probabilities, or local output
   coordinates.

Computation:

1. center the task near a reference distribution, often \(p_*\);
2. compute \(K^{CH}\) on the empirical output displacements;
3. predict the local linear-versus-manifold path discrepancy;
4. compare the prediction with observed behavior-side gaps.

Output:

1. the amount of the gap explained by intrinsic behavior curvature;
2. the unexplained residual assigned to activation-side or
   parameterization-side effects.

### 7.2 Activation Pullback Audit

Input:

1. activation centroids or sampled activation paths;
2. the learned map \(F:A\to\Delta_R^\circ\), explicitly fitted or locally
   approximated;
3. behavior-side Fisher/Hellinger metric \(g_y\).

Computation:

1. estimate

   $$
   G_F=J_F^\top g_yJ_F;
   $$

2. compare \(G_F\) with the fitted activation-manifold metric;
3. estimate the covariant Hessian terms of \(F\);
4. subtract the intrinsic behavior-side cubic already accounted for.

Output:

1. activation-side distortion;
2. Hessian contribution;
3. residual parameterization error.

#### 7.2.1 Real measurement: Llama-3.1-8B activation pullback

The audit was run on both the \(C_7\) weekdays and \(C_{12}\) months
causalab runs using the saved \(4096\)-dim residual-stream activations at
layer 28 (49 prompts in 7 result-classes for weekdays; 84 prompts in 12
result-classes for months).  For each result class \(c\) we compute the
activation centroid \(A_c\) by averaging within-class, and compare the
pairwise activation-centroid distances to the corresponding output-side
Hellinger and cyclic-Hellinger-arc distances.

| quantity | weekdays \(C_7\) | months \(C_{12}\) |
|---|---|---|
| between-class fraction of activation variance | \(0.377\) | \(0.586\) |
| within-class fraction (irreducible per-class noise) | \(0.623\) | \(0.414\) |
| Pearson \(r\): activation dist vs Hellinger chord | \(\mathbf{0.937}\) | \(0.821\) |
| Pearson \(r\): activation dist vs cyclic Hellinger arc | \(0.900\) | \(0.652\) |
| local pullback CV: \(\operatorname{std}(G_F)/\operatorname{mean}(G_F)\) | \(0.154\) | \(0.233\) |

Three structural readings.

First, **on the prime \(C_7\) row the activation embedding is nearly a
rescaled isometry of the Fisher-Hellinger output geometry**.  The
activation-distance vs.\ Hellinger correlation is \(r=0.937\); the local
pullback coefficient of variation is \(0.154\).  In residual terms: the
linear-versus-cyclic-arc gap measured in §4.1 (\(1-0.615=0.385\) for the
moment chord) is **not** explained by activation distortion.  Almost all
of it is intrinsic to the behavior simplex -- exactly what the central
thesis of this paper predicts.  The behavior-side cubic \(K^{CH}\)
carries the gap.

Second, **on the composite \(C_{12}\) row the activation embedding is
preserving Hellinger geometry but not the pure cyclic structure**.  The
activation-vs-Hellinger correlation remains high (\(0.821\)), but the
activation-vs-cyclic-arc correlation drops to \(0.652\).  This is the
same CRT signal seen in the energy decomposition of §5.1: the activation
manifold is **not** a single 1D loop, because the underlying output
algebra is not.  The activation manifold's geometry tracks
\(C_{12} \cong C_4 \times C_3\), which is what makes both the
pure-cyclic-arc reference and a moment-coordinate linear summary perform
worse on this row than on weekdays.  The activation pullback distortion
is somewhat larger here (CV \(=0.233\) vs \(0.154\)), but the dominant
effect is still on the behavior side: the model has learned a
CRT-structured embedding consistent with the output algebra.

Third, the **within-class variance share inverts between the two rows**:
weekdays carry \(62\%\) of their activation variance inside the result
class (noise from differing prompt phrasings that all land on the same
answer day), while months carry only \(41\%\) within-class -- the
activation embedding is more sharply class-separated for months.  This
matches the much higher per-class self-confidence observed in the months
centroid matrix (most diagonals \(\ge 0.86\)).

The Hessian and parameterization-residual terms remain to be estimated
separately; they require a local fit of \(F\) (e.g.\ a linear probe at
the chosen layer) rather than centroid distances alone.

### 7.3 Mixed Output Algebra Test

Input:

1. a task whose output labels carry a product or prime-power algebra;
2. empirical output centroids;
3. a conductor-packet decomposition of the output tangent space.

Computation:

1. compute quotient-character coefficient profiles;
2. project residual curvature onto support channels;
3. compare against the mixed local support predicted by the finite atlas;
4. test whether an associated-graded model loses information retained by the
   filtered quotient-character adjacency algebra.

Output:

1. a measured closure-deficit profile;
2. a finite support map for activation-to-behavior curvature leakage.

Concrete first mixed design:

1. use the \(16\)-label local ring
   \(R={\mathbb F}_4[u]/(u^2)\), with labels written as \(a+bu\);
2. prompt an in-context arithmetic task whose answer is a single element of
   \(R\), for example multiplication by a context-specified element
   \(c+du\);
3. vary tame and wild directions independently.  The product law
   \[
   (a+bu)(c+du)=ac+(ad+bc)u
   \]
   makes the residue \(ac\) look closed under the coarse tame macrovariable,
   while the wild coefficient \(ad+bc\) carries the mixed tame/wild leakage;
4. collect output probabilities over all \(16\) labels, not just the coarse
   tame residue;
5. compare the full \(16\)-label Fisher residual against the associated
   graded model that keeps only tame/wild scalar blocks.

The success condition is not high task accuracy.  The first success condition
is geometric: after subtracting the prime and CRT controls, the residual
should concentrate on the mixed support channels predicted by the
\({\mathbb F}_4[u]/(u^2)\) atlas.  That would be the empirical signature of
\(\operatorname{Ext}_{CH}\).

### 7.4 Optimizer Prototype

The conservative first prototype is now implemented.  It is still not a new
full training method.  It is a local step controller for Fisher-based
optimization, designed to answer the narrower geometric question first:

1. use the Fisher metric for the quadratic natural-gradient direction;
2. compute or estimate the \(K^{CH}\) cubic correction in the relevant output
   packet;
3. damp, curve-correct, or reparameterize the step when the cubic norm is
   large relative to the Fisher norm;
4. use conductor packets as blockwise preconditioner groups when \(R\) has
   nontrivial arithmetic structure;
5. report whether the correction improves local path prediction before
   claiming training improvements.

The current implementation lives in `empirical/k_ch_step_controller.py`.
For a proposed output-simplex step \(s\) at base distribution \(p\), it
computes

\[
K^{CH}_p(s)s={s\odot s\over p}-g_p(s,s)p
\]

and the local cubic fraction

\[
\rho_{\mathrm{frac}}(p,s)
=
{1\over2}
{\|K^{CH}_p(s)s\|_{g_p}\over \|s\|_{g_p}}.
\]

If \(\rho_{\mathrm{frac}}\) exceeds the configured trust target, the
controller dampens the step \(s\mapsto \alpha s\), also respecting a
simplex-boundary positivity guard and any optional Fisher-radius cap.  The
script also reports a second-order curve-correction vector
\(-\frac12\alpha^2 K^{CH}_p(s)s\), but the default action remains damping
until path-prediction tests justify applying the correction as an update.

The smoke test `empirical/_test_k_ch_step_controller.py` verifies the
raising identity, the linear scaling of \(\rho_{\mathrm{frac}}\) under step
rescaling, the positivity guard, and the cyclic conductor packet energy
normalization.  On the saved Llama-3.1-8B weekday and month centroids, a
trust target of `0.10` dampens all tested uniform-to-centroid and
adjacent-cycle steps and caps the controlled cubic fraction at `0.098`.
This is exactly the intended first artifact: a programmable warning light
for when the Fisher quadratic approximation is locally overconfident.

The first success criterion is geometric, not benchmark-chasing:

> Does the cubic arithmetic diagnostic predict when a Fisher quadratic step
> is locally trustworthy?

## 8. Figure Architecture

Two figures should carry the paper for readers who will not follow every
finite-algebra definition on first pass.

**Figure 1: Pullback and residual decomposition.**  This should show the
activation region \(A\), the learned map \(F\), and the behavior simplex
\(\Delta_R^\circ\).  The quadratic arrow is \(J_F^\top g_yJ_F\).  The cubic
behavior-side correction is \(K^{CH}\).  The residual box splits into
activation pullback distortion, Hessian terms of \(F\), and sampling or
parameterization error.

\begin{figure}[!h]
\centering
\begin{tikzpicture}[
  >=Stealth,
  every node/.style={draw, rounded corners, font=\small, align=center, inner sep=4pt},
  arrow/.style={->, thick},
  node distance=0.7cm and 0.9cm
]
  \node (A) {activation\\ region $A$};
  \node[right=of A] (B) {behavior simplex\\ $\Delta_R^\circ$};
  \node[right=of B] (C) {Fisher/Hellinger\\ metric $g_y$};
  \node[right=1.2cm of C, yshift=1.1cm] (D) {$J_F^\top g_y J_F$};
  \node[right=1.2cm of C, yshift=-1.1cm] (E) {$K^{CH}$};
  \node[right=2.8cm of C] (R) {residual\\ audit};
  \node[right=of R, yshift=1.2cm]  (R1) {activation\\ distortion};
  \node[right=of R]                (R2) {Hessian\\ terms of $F$};
  \node[right=of R, yshift=-1.2cm] (R3) {sampling /\\ parameterization};
  \draw[arrow] (A) -- node[draw=none, fill=none, above, font=\scriptsize] {$F$} (B);
  \draw[arrow] (B) -- (C);
  \draw[arrow] (C.east) -- node[draw=none, fill=none, sloped, above, font=\scriptsize, pos=0.55] {quadratic} (D.west);
  \draw[arrow] (C.east) -- node[draw=none, fill=none, sloped, below, font=\scriptsize, pos=0.55] {cubic} (E.west);
  \draw[arrow] (D) -- (R);
  \draw[arrow] (E) -- (R);
  \draw[arrow] (R) -- (R1);
  \draw[arrow] (R) -- (R2);
  \draw[arrow] (R) -- (R3);
\end{tikzpicture}
\caption{\textbf{Pullback and residual decomposition.} The quadratic pullback $J_F^\top g_y J_F$ and the cubic behavior-side term $K^{CH}$ together account for the leading local behavior-side geometry; the residual audit attributes the remaining gap to activation pullback distortion, Hessian terms of $F$, and sampling or parameterization error.}
\label{fig:pullback}
\end{figure}

**Figure 2: Control ladder toward mixed collision.**  The left side should
show \(C_7\) as one clean nontrivial conductor packet: pure tame motion, no
\(\operatorname{Ext}_{CH}\).  The middle should show \(C_{12}\) as a CRT
control with \(C_4\times C_3\) conductor splitting but no nilpotent carry.
The right side should show \({\mathbb F}_4[u]/(u^2)\) with a tame
residue-field layer, a wild nilpotent depth layer, and a carry arrow labeled
\(\operatorname{Ext}_{CH}\).

\begin{figure}[!h]
\centering
\begin{tikzpicture}[
  >=Stealth,
  every node/.style={draw, rounded corners, font=\small, align=center, inner sep=4pt},
  arrow/.style={->, thick},
  node distance=0.7cm and 0.9cm
]
  % Row 1: C_7 (single horizontal chain)
  \node (C7) {$C_7$ weekday\\ control};
  \node[right=of C7] (P) {one nontrivial\\ packet};
  \node[right=of P]  (N) {no $\operatorname{Ext}_{CH}$};
  % Row 2: C_12 (split into two branches that merge into Y)
  \node[below=2.6cm of C7] (C12) {$C_{12}$ month\\ control};
  \node[right=1.0cm of C12, yshift=0.9cm] (C4) {$C_4$ ($p{=}2$,\\ depth $1,2,4$)};
  \node[right=1.0cm of C12, yshift=-0.9cm] (C3) {$C_3$ tame\\ factor};
  \node[right=4.0cm of C12] (Y) {CRT split,\\ no nilpotent carry};
  % Row 3: F_4[u]/(u^2) (split into two branches that merge into X, then to M)
  \node[below=2.8cm of C12] (F4) {$\mathbb{F}_4[u]/(u^2)$\\ mixed row};
  \node[right=1.0cm of F4, yshift=0.9cm] (T) {tame Frobenius\\ layer};
  \node[right=1.0cm of F4, yshift=-0.9cm] (W) {wild nilpotent\\ depth};
  \node[right=4.0cm of F4] (X) {$\operatorname{Ext}_{CH}$\\ carry};
  \node[right=of X] (M) {mixed Fisher\\ curvature channels};
  % Arrows
  \draw[arrow] (C7) -- (P);
  \draw[arrow] (P)  -- (N);
  \draw[arrow] (C12.east) -- (C4.west);
  \draw[arrow] (C12.east) -- (C3.west);
  \draw[arrow] (C4.east)  -- (Y.west);
  \draw[arrow] (C3.east)  -- (Y.west);
  \draw[arrow] (F4.east) -- (T.west);
  \draw[arrow] (F4.east) -- (W.west);
  \draw[arrow] (T.east)  -- (X.west);
  \draw[arrow] (W.east)  -- (X.west);
  \draw[arrow] (X) -- (M);
\end{tikzpicture}
\caption{\textbf{Control ladder toward mixed collision.} Left-to-right: the prime $C_7$ weekday row has a single nontrivial conductor packet and no extension class; the $C_{12}$ month row has a CRT $C_4\times C_3$ conductor split with no nilpotent carry; the $\mathbb{F}_4[u]/(u^2)$ row collides a tame residue-field layer with a wild nilpotent depth layer, producing the first $\operatorname{Ext}_{CH}$ carry.}
\label{fig:control-ladder}
\end{figure}

These figures should make the story visible before the reader has internalized
the notation: smooth activation geometry maps into categorical behavior
geometry; prime rows are clean controls; CRT rows test product conductor
structure; mixed local rows reveal the first finite carry data.

## 9. What This Could Buy AI Optimization

The direct payoff is diagnostic before algorithmic.

**Natural-gradient trust regions.**  Natural gradient is quadratic.  The
raised Amari-Chentsov cubic gives a finite, behavior-side way to estimate
when the quadratic approximation is starting to bend.

**Output-space preconditioning.**  If output labels carry a finite algebra,
conductor packets give canonical blocks for Fisher preconditioners.  This is
not a learned clustering of labels.  It is a symmetry-resolved decomposition
of the categorical Fisher tangent space.

**Residual attribution.**  The decomposition

$$
\text{gap}
=
\text{behavior cubic}
+\text{activation pullback distortion}
+\text{Hessian/parameterization residual}
$$

prevents a common interpretive error: calling every linear-versus-manifold
gap an activation geometry phenomenon.  Some of the gap may already be
intrinsic to the behavior simplex.

**Macrovariable closure.**  Coarse labels, features, or task abstractions may
look closed at maximum entropy or under scalar summaries.  The
quotient-character adjacency algebra tests whether they remain closed for
off-centroid Fisher couplings.

**Model comparison.**  Two models can have similar output accuracy but
different activation pullback residuals.  A finite support profile gives a
more structured comparison than one scalar correlation.

**Information-investment pricing.**  The finite skeleton also gives a bounded
way to price a discretization choice.  On finite abelian rows the zero-carry
baseline is the subgroup generated by the observed reciprocal support; a
normalizer-saturated support is worth paying for only when expected transfer
gain beats its resource-weighted symmetry premium.  On certified local rows,
support closure is not enough: the \({\mathbb F}_4[u]/(u^2)\) bounded atlas
has
\[
\mathrm{full}/\mathrm{support}/H4/H3/\mathrm{remaining}=1569/0/72/1470/27,
\]
and the current exact local ledger has
\[
180555/0/6648/173404/503.
\]
A task may price the full filtered residual directly, or price the H4/H3/hidden
visibility partition, but these channels should not be collapsed into the
support residual.

The deeper practical claim is a trust diagnostic:

> This is not primarily a new optimizer.  It is a way to tell when a
> Fisher-quadratic approximation is locally trustworthy, and when it is
> leaking structured geometric information through channels the metric alone
> cannot see.

## 10. Boundaries Against Overclaiming

This paper does not claim that all neural loss landscapes are controlled
by finite rings.  The finite algebra lives first in the categorical
behavior space and in tasks where the labels carry a usable algebraic
structure.

The transformer measurements reported here are at a single layer (layer
28, last-token) of two open-weight base models (Llama-3.1-8B and
Mistral-7B-v0.3).  A formal layer sweep remains open; layer 28 was
inherited from the source causalab pipeline that targeted Llama-3.1-8B.
The cross-family replication is evidence against layer 28 being
simultaneously suboptimal for both models, but it is not a proof of
layer-optimality.

This paper does not claim that the binary simplicial cross product exists
in the weekday \(C_7\) tangent space.  The \(I+K(\tau_i)^2\) presentation
is the \(N=4\), uniform tetrahedral calibration theorem.  The \(C_7\)
weekday row is its higher-dimensional arithmetic analogue, expressed as
character-basis convolution rather than as a single binary cross-product
operator.

The \({\mathbb F}_4[u]/(u^2)\) positive test for nonzero
\(\operatorname{Ext}_{CH}\) has not been run on a real transformer in this
paper.  The mixed-row finite results in Appendix B are exact enumerations
over the finite algebra itself; the corresponding neural task design is a
required next step before any \(\operatorname{Ext}_{CH}\) claim is made
about a transformer.

This paper does not lead with quantum analogies.  Tensor factors and
cross-prime coefficient rank are real in the quotient-character algebra,
but the manuscript does not need quantum language to be compelling.

The moment-Euclidean correlation drop reported in §4.1 should not be
read, by itself, as direct evidence of cubic Amari-Chentsov curvature.
The extended-baseline comparison of §4.1.1 shows that the moment drop
is uniquely the largest in a nine-metric family but that total
variation also drops, that the Fisher-equivalent family is heterogeneous
at the chord level, and that the Wasserstein-1 metric with cyclic
ground structure essentially saturates at the proxy value.  The
chord-level evidence is therefore consistent with cubic curvature *and*
with the textbook categorical-Euclidean inadequacy.  The
cubic-specific empirical content of the paper lives in the CRT
conductor energy decomposition (§5.1), in the predicted CRT block
isolation, and in the operator-valued quotient-character adjacency
algebra — none of which has a chord-metric analogue.  Likewise, the
asymmetric off-diagonal leakage observed in the weekday centroids is now
scoped by the completed §4.1.2 C4 control: it is partially aligned with
pretraining bigram statistics and should be read as an intermediate,
mixed-origin signal rather than as standalone arithmetic evidence.

The strongest headline is:

> Smooth AI behavior manifolds can have a finite arithmetic Fisher skeleton.

The strongest sober version is:

> For categorical behavior spaces with finite algebraic output structure,
> Fisher curvature has finite quotient-character coordinates that can
> diagnose when natural-gradient geometry misses structured cubic terms.

## 11. The Launch Pitch

Modern AI systems are trained by moving through enormous continuous parameter
spaces, but the behavior we measure is often finite: a model assigns
probabilities to tokens, classes, labels, or concept bins.  Optimization
methods usually treat the resulting probability space as a smooth statistical
manifold.  Natural gradient, Fisher preconditioning, and Hellinger geometry
all live in that world.

This paper argues that the smooth manifold is not the whole story.  When
finite output labels carry arithmetic structure, the Fisher geometry of the
categorical simplex has a hidden discrete skeleton.  At maximum entropy, this
skeleton decomposes the behavior tangent space into finite Fourier packets.
Away from maximum entropy, the model begins making useful predictions, and
those packets start coupling.  The coupling is still governed by a finite
quotient-character adjacency algebra.

The AI consequence is practical.  Natural gradient sees the quadratic Fisher
metric.  It does not automatically see the first cubic correction, the raised
Amari-Chentsov tensor.  That cubic term measures where straight-line output
interpolations begin to miss the Fisher/Hellinger behavior manifold.  In
neural representation experiments, the same term helps separate three effects
that are often conflated: intrinsic curvature of the output behavior space,
distortion introduced by the activation-to-behavior map, and residual error
from sampling or parameterization.

The weekday task studied by Wurgaft et al. is the first control.  The seven
weekday labels form the prime cyclic algebra \(C_7\), so the nontrivial
behavior tangent space is one clean six-dimensional packet.  The real
transformer measurement is now in hand on **two independent model families
at layer 28**: Llama-3.1-8B (the Wurgaft et al.\ baseline model) and
Mistral-7B-v0.3 (cross-family replication), both via the causalab
`weekdays` pipeline.  The moment-Euclidean linear summary correlation
drops from \(r=0.886\) on the symmetric parametric proxy to \(r=0.615\) on
Llama and \(r=0.715\) on Mistral, while the Hellinger, logit, and Fisher
Levi-Civita correlations remain near or above the proxy values on both
models.  An extended-baseline comparison (§4.1.1) places this drop in a
broader nine-metric family: total variation also drops mildly, the
Fisher-equivalent family is heterogeneous at the chord level, and
Wasserstein-1 with cyclic ground metric on \(\mathbb{Z}/7\) saturates
near the proxy value on both models.  The chord-level story is therefore
consistent with both the cubic diagnostic and the standard
categorical-Euclidean inadequacy; the cubic-specific empirical content
of this paper is in §5.1.  Both centroid matrices also show an
asymmetric off-diagonal leakage pattern, in the predecessor-cyclic
direction.  The completed \(10^7\)-token C4 bigram control (§4.1.2)
places this directionality in the intermediate band: corpus sequence
statistics partially explain the magnitude pattern but fail the
pre-registered sign-agreement threshold for "fully explain."  The
cross-family replication of the correlation ordering across both models
is therefore the stronger single-row indication that the metric signature
is structural rather than a single-model artifact.

The month task is the second control.  Its \(C_{12}\cong C_4\times C_3\)
label algebra has a \(2\)-primary conductor ladder \(1,2,4\) paired with a
tame \(3\)-factor, and the Llama-3.1-8B measurement is now in hand.  The
moment-chord correlation collapses to \(r=0.210\) (proxy \(0.696\)) -- a
much sharper drop than the prime \(C_7\) row, exactly as predicted when
the output algebra acquires multiple conductors.  The CRT conductor
energy decomposition is even more diagnostic: the empirical displacement
energy is spread across all five conductors (\(2,3,4,6,12\)), with only
\(38\%\) in the single dihedral mode (conductor 12) and \(19\%\) in the
mixed \(C_4\times C_3\) packet (conductor 6).  This is the first
transformer measurement of the predicted CRT split, and it shows up
before any nilpotent carry is invoked.

The activation pullback audit closes most of the residual question on the
\(C_7\) row.  At layer 28, Llama's activation-distance vs.\ Hellinger
correlation is \(r=0.937\) with a pullback metric coefficient of
variation of \(0.154\): the embedding is nearly a rescaled isometry of
the Fisher-Hellinger output geometry.  The linear-versus-manifold gap is
therefore not an activation-side artifact; it is intrinsic to the
behavior simplex, carried by the cubic \(K^{CH}\).  On the \(C_{12}\)
row the embedding still preserves Hellinger geometry well
(\(r=0.821\)) but its correlation with the pure cyclic-arc reference
drops to \(r=0.652\) -- the activation manifold has learned the
CRT-product structure of the output algebra, not a single 1D loop.

The deeper tests come from mixed finite algebras such as
\({\mathbb F}_4[u]/(u^2)\), where tame and wild motion first collide.  There
the new extension class \(\operatorname{Ext}_{CH}\) measures when a coarse
output macrovariable is closed at the centroid but leaks Fisher-geometric
information off the centroid.

If this program works, it gives AI optimization a new kind of diagnostic: not
just a smoother optimizer, but a finite map of the curvature channels that a
Fisher quadratic approximation is missing.

## 12. Reproducibility

All transformer measurements reported in §4.1, §5.1, and §7.2.1 use
publicly available open-weight base models and the open-source causalab
inference pipeline of Wurgaft et al.  Specifically:

- **Models.** `meta-llama/Llama-3.1-8B` and `mistralai/Mistral-7B-v0.3`,
  loaded via the HuggingFace `transformers` library in bfloat16.
- **Pipeline.** The causalab `weekdays_8b_pipeline` and
  `months_8b_pipeline` runners (with a parallel `mistral_7b` model
  configuration that swaps in the Mistral checkpoint, leaving layer index
  28 and last-token feature extraction unchanged).
- **Hardware.** A single NVIDIA L4 GPU (24 GB VRAM) on a Google Cloud
  Compute Engine VM.  Total inference wall time ~2.5 hours per
  (model, task) pair.
- **Artifacts.** Each run produces a `per_class_output_dists.safetensors`
  file (the \(C\times C\) result-conditioned output centroid matrix used
  for the \(K^{CH}\) diagnostic) and a `raw_features.safetensors` file
  (the per-prompt last-token residual-stream activation at layer 28 used
  for the activation pullback audit).
- **Analysis scripts.** Five Python scripts compute the diagnostics from
  the saved safetensors:
  `compute_weekdays_K_CH_real.py` (§4.1),
  `compute_months_K_CH_real.py` (§5.1, including CRT conductor energy),
  `activation_pullback_audit.py` (§7.2.1),
  `extended_metric_baselines.py` (§4.1.1, §5.1.1 — adds total variation,
  Jensen-Shannon, symmetric KL, Bhattacharyya, and Wasserstein-1 with
  cyclic ground metric to the four existing chord-correlation metrics),
  and `bigram_corpus_control.py` (§4.1.2 — pre-registered
  pretraining-bigram control, accepts either a plaintext corpus or a
  HuggingFace streaming dataset).
  All five depend only on `numpy` and `scipy`; the bigram control
  optionally uses the `datasets` library for HuggingFace streaming.
  Design notes for the latter two are
  `Note_metric_baselines_design.md` and `Note_bigram_confound_design.md`.

## Acknowledgments

Standard.

## References

[Amari] Amari, S. *Information Geometry and Its Applications*. Applied Mathematical Sciences, vol. 194. Springer, 2016.

[Chentsov] Chentsov, N.N. *Statistical Decision Rules and Optimal Inference* (English translation). American Mathematical Society, 1982.

[Murillo] Murillo Montero, L. *Simplicial Vector Calculus on the Zero-Sum Hyperplane*. Preprint, 2026.

[Wurgaft] Wurgaft, M. et al. *Causal Manifold Geometry of Concepts in Large Language Models* (causalab). Goodfire AI technical report, 2026. Code: <https://github.com/goodfire-ai/causalab>.

## Appendices

### Appendix A: Arithmetic Toolkit (Self-Contained Summary)

This appendix supplies the minimal definitions and statements needed for
the main text.  Full developments of the off-centroid Fisher Taylor
expansion, the quotient-character adjacency algebra, the CRT
factorization, and the local Carlitz-Hayes extension class are deferred
to a separate technical manuscript by the author; the statements below
are quoted, with proofs deferred there.

**A.1 Conductor packets and the Fisher tangent space.**  
Let \(R\) be a finite quotient ring of cardinality \(Q\). The categorical probability simplex is \(\Delta_R^\circ\). Its tangent space at any point is identified with the zero-sum hyperplane \(H_R = \{ h \in \mathbb{C}^R : \sum h_a = 0 \}\). At the uniform (maximum-entropy) distribution \(p_* = Q^{-1}\mathbf{1}\), additive characters furnish a Fourier basis of \(H_R\). Grouping nontrivial characters by their conductor yields **conductor packets** \(H_R^{[\mathfrak{d}]}\). These packets are Fisher-orthogonal at \(p_*\).

**A.2 Off-centroid coupling and the quotient-character adjacency algebra.**  
Along an \(m\)-flat ray \(p(t) = p_* + t h\), the normalized Fisher matrix elements between character lines admit an exact Taylor expansion whose coefficients are governed by convolution in the dual character group. The natural finite compression of these coefficients from conductor packet \(X_{\mathfrak{e}}\) to packet \(X_{\mathfrak{f}}\) is **operator-valued**. For a quotient character \(\eta\), the partial quotient-shift operator is defined by
\[
A_\eta^{\mathfrak{f},\mathfrak{e}} e_\chi =
\begin{cases}
e_{\eta\chi} & \text{if }\chi\in X_{\mathfrak{e}}\text{ and }\eta\chi\in X_{\mathfrak{f}},\\
0 & \text{otherwise.}
\end{cases}
\]
The \(n\)-th Taylor coefficient compressed between packets is then the operator
\[
C_n^{[\mathfrak{f},\mathfrak{e}]}(h) = \sum_\eta \widehat{h}^{*n}(\eta) \, A_\eta^{\mathfrak{f},\mathfrak{e}}
\]
living in the finite **quotient-character adjacency algebra** generated by these partial shifts. Scalar trace compression can erase the first nontrivial within-block invariants; the operator-valued form retains them.

**A.3 The Carlitz-Hayes extension class \(\operatorname{Ext}_{CH}\).**  
Each local factor of the adjacency algebra carries a depth filtration whose associated graded separates tame (residue-field) action from wild (nilpotent congruence) action. The obstruction to a splitting of this filtration is a finite extension class \(\operatorname{Ext}_{CH}(R_{\mathfrak{p}})\) in the local Carlitz-Hayes sense. It is represented concretely by the 2-cocycle of any filtered section of the associated graded. In the first mixed row \(R = \mathbb{F}_4[u]/(u^2)\), this class is nontrivial and is detected by the first mixed \(srt^2\) term in the cubic defect together with the support theorems at higher arity.

**A.4 Key structural facts used in the main text.**

- Prime cyclic rows (\(R = C_p\)) have a single nontrivial conductor packet; off-centroid coupling eventually saturates the whole nontrivial dual group.
- CRT rows factor the global algebra; the Fisher tangent algebra decomposes as a direct sum over nonempty support-pattern corners.
- Mixed local rows are the first place where associated-graded conductor data is provably insufficient; the full filtered adjacency algebra is required.

### Appendix B: Finite Results for the Control Cases

All statements below are exact enumerations or theorems established by direct computation over the indicated small algebras.

**B.1 Prime control row \(C_7\)** (weekday task).  
Single nontrivial conductor packet of dimension 6. At the uniform point the raised cubic is pure character convolution: \(K^{CH}_{p_*}(h)v = 7 h * v - 7 \langle h,v\rangle p_*\). No tame/wild extension; the row serves as the clean no-\(\operatorname{Ext}_{CH}\) control.

**B.2 Mixed local row \(\mathbb{F}_4[u]/(u^2)\)** (first positive test).

- Centroid-normalized full character algebra has \(c=1\).
- First mixed defect term appears at order \(srt^2\); the tangent-compatible full-defect support comprises 4438 Hayes-normalizer orbits, of which 592 are commutator orbits.
- Arity-3 hyper-adjacency atlas: 210 closed cells collapsing to 5 \(\Gamma_R \times S_3\)-orbits, canonically labeled by a multiplicative residue ratio \(\rho\) and an additive nil-tail balance \(\nu\).
- Arity-4 skeleton: 3165 closed cells collapsing to 18 \(\Gamma_R \times S_4\)-orbits. The analytic four-linear curvature support is exactly the input-side lift of the 592 commutator orbits onto the seven mixed TTWW/TWWW orbits (and onto no pure orbit). After paired-slot Bianchi projection the coefficient distribution on these lifted records is \(-1:44\), \(1:504\), \(2:44\).
- Binary \(\operatorname{Ext}_{CH}\) representative: the collision-free \((\rho,\nu)\) signature selects a canonical filtered section; the resulting carry table has 1569 raw atoms on 369 nonzero carry pairs, reduced by the Hayes normalizer to 71 atom orbits and 20 canonical pair orbits. Full-block coboundary diagnostic confirms the carry is nontrivial (residual support 1569 after maximal section change).

These finite facts supply the concrete signatures against which empirical behavior-side curvature on tasks with matching output algebra can be compared.

---

*End of paper.*
