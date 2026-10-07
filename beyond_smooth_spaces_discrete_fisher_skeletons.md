# Beyond Smooth Spaces: Discrete Fisher Skeletons in Large Language Model Behavior

**Leonardo Murillo Montero**

*May 15, 2026*

**Draft 0.1**

---

## Abstract

Large language models are usually described as moving through smooth,
high-dimensional spaces: parameter space, activation space, representation
manifolds, loss landscapes, and probability simplices.  This paper argues
that this smooth description is incomplete at the behavior level.  When a
model makes categorical predictions on labels with finite algebraic structure,
such as weekdays or months, the output simplex after unembedding and Softmax
becomes a place where a discrete arithmetic skeleton can be audited.

At maximum entropy, the Fisher tangent space splits into orthogonal packets
indexed by finite additive characters and grouped by conductor.  Away from
maximum entropy, these packets no longer remain invisible to one another:
their first structured coupling is governed by the raised Amari-Chentsov
cubic tensor, and higher Taylor coefficients are organized by a finite
quotient-character adjacency algebra.  Natural gradient methods see the
quadratic Fisher metric.  The arithmetic skeleton begins where that quadratic
approximation stops being faithful.

We test this claim on structured categorical behavior extracted from real
transformer outputs.  On the prime cyclic weekday task \(C_7\), both
Llama-3.1-8B and Mistral-7B-v0.3 preserve cyclic structure under
Fisher/Hellinger-aware metrics while ordinary moment-Euclidean summaries
collapse.  On the composite month task
\(C_{12}\cong C_4\times C_3\), Llama-3.1-8B shows a sharper moment collapse
and a conductor-energy distribution close to the per-character-uniform null
but tilted toward the high conductors \(6\) and \(12\).  This is suggestive
composite-control evidence, not yet a standalone proof of CRT-specific
routing.  An activation-pullback audit indicates that the weekday gap is not
primarily an activation-space distortion.  A corpus bigram control explains
part of the observed directional asymmetry, but not the main metric gap.

This places the paper next to, rather than against, the mechanistic
interpretability literature on grokking and modular arithmetic.  Prior work
has shown Fourier and representation-theoretic structure inside small networks
trained on modular addition and finite group composition.  The present paper
asks the complementary behavior-side question: after a large pretrained
transformer is projected through unembedding and Softmax onto a structured
finite label set, does the output simplex still expose the corresponding
finite Fourier/conductor structure as auditable behavior?

The practical thesis is modest and testable: structured categorical behavior
can expose finite arithmetic control channels inside apparently smooth neural
systems.  These channels can be used as diagnostics for when Fisher or natural
gradient approximations are overconfident, and as design constraints for
update-side projection rules that suppress leakage outside declared conductor
supports.  The paper does not claim a universal theory of neural cognition,
training dynamics, or intelligence.  It establishes a sharper behavior-level
object: discrete Fisher skeletons in large language model outputs.

**Keywords:** large language models, information geometry, Fisher geometry,
Hellinger geometry, natural gradient, Amari-Chentsov tensor, categorical
simplex, conductor packets, finite Fourier analysis, quotient characters,
AI optimization, behavior manifolds.

---

## 1. The Claim

The usual geometric language for modern AI is smooth.  We speak about
continuous parameter spaces, differentiable loss landscapes, activation
manifolds, representation geometry, natural gradients, and local quadratic
approximations.  That language is necessary.  It is not sufficient.

The reason is simple: the behavior of a language model is categorical.  A
model returns a probability distribution over tokens, answers, labels, bins,
or concepts.  If those labels carry structure, then the probability simplex is
not merely a featureless smooth manifold.  It is also a finite statistical
object with arithmetic coordinates.

This paper chooses a specific locus of investigation: the output simplex
\(\Delta_R^\circ\) after unembedding and Softmax.  That choice is deliberately
weaker than claiming that the skeleton primarily lives there.  Pre-Softmax
logits or internal activations may carry a sharper version of the same finite
structure.  The point of the output simplex is that it is where the structure
becomes auditable as categorical behavior: a probability distribution with a
Fisher metric, a Hellinger embedding, and finite character coordinates tied to
the label algebra.

This paper studies the following claim.

**Claim.**  Let a model produce probability distributions on a finite
structured label set \(R\).  If \(R\) has finite algebraic structure, then the
behavior simplex \(\Delta_R^\circ\) carries a discrete Fisher skeleton:

1. at maximum entropy, Fisher tangent directions split into orthogonal
   quotient-character packets;
2. those packets are grouped by conductor, giving a finite arithmetic
   resolution of behavior;
3. away from maximum entropy, the first structured correction to the
   quadratic Fisher picture is the raised Amari-Chentsov cubic;
4. real transformer outputs on structured tasks expose this skeleton in
   measurable metric gaps and conductor-energy decompositions.

The precise meaning is not that primes explain all cognition.  It is that
finite categorical behavior can decompose into prime and prime-power channels
before it becomes a smooth continuum.  In such settings, arithmetic is not
decoration on top of a neural manifold.  It is part of the behavior geometry.

## 2. Why Smooth Geometry Is Not Enough

Let \(p\in\Delta_R^\circ\) be a probability distribution over a finite set
\(R\), with

\[
\Delta_R^\circ =
\left\{
p\in{\mathbb R}_{>0}^R : \sum_{a\in R} p_a = 1
\right\}.
\]

The tangent space at any point is the zero-sum hyperplane

\[
T_p\Delta_R^\circ =
H_R =
\left\{
u\in{\mathbb R}^{R} : \sum_{a\in R} u_a = 0
\right\}.
\]

The Fisher metric is

\[
g_p(u,v)=\sum_{a\in R}\frac{u_a v_a}{p_a}.
\]

At the maximum-entropy point \(p_* = |R|^{-1}\mathbf{1}\), this becomes

\[
g_{p_*}(u,v)= |R|\sum_{a\in R} u_a v_a.
\]

Thus the local geometry at \(p_*\) is a scaled Euclidean geometry on the
zero-sum hyperplane.  This is the quadratic geometry used by Fisher
preconditioning and natural gradient methods.  It tells us how expensive an
infinitesimal displacement is.

But the Fisher metric is only the second-order object.  A categorical
exponential family also has a third-order tensor, the Amari-Chentsov tensor.
In raised form we write

\[
K^{CH} = \Gamma^{(m)}-\Gamma^{(e)},
\]

where \(\Gamma^{(m)}\) and \(\Gamma^{(e)}\) are the mixture and exponential
connection coefficients.  This cubic tensor measures the first failure of the
two flat affine structures to agree.  Operationally, it detects when a
straight line in one coordinate system is no longer locally faithful to the
Fisher/Hellinger geometry of the probability simplex.

Natural gradient sees \(g\).  The behavior skeleton begins to move at
\(K^{CH}\).

This distinction matters for AI because a model trained by cross-entropy does
not remain near maximum entropy.  It becomes useful by leaving the centroid.
The same movement that makes a model informative also activates cubic
behavior-side geometry.

## 3. The Finite Skeleton

Assume now that \(R\) is not just a finite set, but a finite abelian group or
finite quotient ring.  The examples in this paper are deliberately small:

\[
C_7=\mathbb Z/7\mathbb Z
\]

for weekdays, and

\[
C_{12}=\mathbb Z/12\mathbb Z\cong C_4\times C_3
\]

for months.

The additive characters of \(R\) provide a finite Fourier basis.  For the
cyclic case \(C_N\), a character is

\[
\chi_k(a)=\exp(2\pi i k a/N),
\qquad
k\in C_N.
\]

The trivial character \(k=0\) spans the normalization direction.  The
nontrivial characters span the Fisher tangent space at \(p_*\).  Their
conductors group the tangent directions into arithmetic packets.  In the
cyclic case the conductor of \(k\) is

\[
\operatorname{cond}(k)=\frac{N}{\gcd(k,N)}.
\]

At \(p_*\), these packets are Fisher-orthogonal.  This gives a finite
decomposition

\[
H_R\otimes{\mathbb C}
=
\bigoplus_{\mathfrak f\neq 1} X_{\mathfrak f},
\]

where \(X_{\mathfrak f}\) is the conductor packet associated with conductor
\(\mathfrak f\).

For \(C_7\), there is only one nontrivial conductor packet: conductor \(7\).
This makes weekdays the prime control.  There is no CRT split and no mixed
prime structure.

For \(C_{12}\), there are multiple conductor packets:

\[
2,\quad 3,\quad 4,\quad 6,\quad 12.
\]

This makes months the composite control.  The Chinese Remainder Theorem
predicts that behavior can distribute energy across separate \(2\)-primary,
\(3\)-primary, and mixed conductor channels.

The smooth simplex has not disappeared.  It is still the right ambient
statistical manifold.  The point is that structured labels add a finite
arithmetic atlas on its tangent and higher-order geometry.

This is also where the companion simplicial algebra paper matters.  That paper
works on the zero-sum hyperplane as a native coordinate object: an
overcomplete simplicial frame modulo the gauge direction \(\mathbf 1\).  The
probability simplex has the same linear tangent arena.  At \(p_*\), the Fisher
metric is just a scale multiple of the simplicial zero-sum metric:

\[
g_{p_*}(u,v)=|R|\sum_{a\in R}u_av_a.
\]

Thus the companion paper supplies the algebraic gauge language for the space
on which the present paper measures behavior.  In the \(N=4\) row, its
cross-product and projector identities also give a concrete finite model for
how a symmetric cubic can live intrinsically on a zero-sum simplex slice.  The
present paper does not need that \(N=4\) exception for the weekday and month
experiments, but it uses the same organizing principle: the meaningful
geometry is not the ambient coordinate box; it is the zero-sum statistical
hyperplane with its native finite symmetries.

## 4. The Cubic Correction Natural Gradient Misses

At maximum entropy, the Fisher metric diagonalizes cleanly in the character
basis.  Off maximum entropy, the packets begin to couple.  For a displacement

\[
h = p-p_*,
\]

the categorical cubic response at the centroid has the convolution form

\[
K^{CH}_{p_*}(h)v
=
|R|\, h*v
-
|R|\,\langle h,v\rangle p_*,
\]

where \(*\) denotes convolution in the finite output algebra, and the final
term removes the normalization direction.

This formula is the first place the finite algebra becomes dynamical.  In
Fourier coordinates, convolution becomes multiplication of characters.  The
cubic tensor therefore moves energy between character packets according to
finite arithmetic rules.  For prime cyclic \(C_7\), all nontrivial characters
belong to the same conductor packet.  For composite \(C_{12}\), products of
characters can cross between conductor packets in CRT-structured ways.

The conclusion is not that natural gradient is wrong.  Natural gradient is the
correct quadratic local approximation.  The conclusion is that the quadratic
approximation is blind to structured cubic response.  When the model moves far
enough from maximum entropy, a Fisher-aware optimizer needs a warning light:
is the local quadratic metric still faithful, or is the cubic response already
large and structured?

This is the role of \(K^{CH}\) in the present paper.  It is a behavior-side
curvature diagnostic.

## 5. Why Language Models Should Expose the Skeleton

For a labeled example with target \(y\), cross-entropy has logit gradient

\[
\nabla_z L = p-e_y.
\]

Near \(p_*\), this is

\[
p-e_y = h - (e_y-p_*),
\]

where \(h=p-p_*\).  Thus training repeatedly injects centered score-frame
directions

\[
e_y-p_* \in H_R.
\]

If the labels carry finite algebraic structure, those score-frame directions
already have a quotient-character decomposition.  The model's continuous
parameter dynamics decide which packets are easy to move, but the behavior
side supplies the finite coordinate system.

This gives the main AI-facing hypothesis.

**Hypothesis.**  On structured categorical tasks, a trained transformer's
output distributions should preserve Fisher/Hellinger geometry more faithfully
than ordinary moment-Euclidean summaries, and composite tasks should reveal
whether displacement energy is merely dimension-weighted across characters or
is additionally tilted by the finite conductor structure.

This is a behavior-level hypothesis.  It does not require that every hidden
unit or training trajectory explicitly factor into conductors.  It only claims
that when the model's outputs are projected onto a structured finite label
set, the resulting probability distributions can expose the arithmetic
skeleton of the output simplex.

## 6. Relation to Grokking and Modular Arithmetic

The closest existing dialogue partner is the mechanistic interpretability
literature on grokking.  Power et al. introduced grokking as delayed
generalization beyond overfitting on small algorithmic tasks
[Power-Burda-Edwards-Babuschkin-Misra].  Nanda et al. then reverse engineered
small transformers trained on modular addition, showing that the learned
algorithm uses discrete Fourier transforms and trigonometric identities, and
validating the circuit with Fourier-space ablations
[Nanda-Chan-Lieberum-Smith-Steinhardt].  Chughtai, Chan, and Nanda extended
this line to finite group composition, showing that small networks can
implement group operations using representation-theoretic structure
[Chughtai-Chan-Nanda].

Those papers look inside trained networks.  This paper looks at the behavior
simplex after a model has already produced categorical probabilities.  The two
views are complementary:

1. mechanistic work asks whether weights and activations implement Fourier or
   group-representation algorithms;
2. the present behavior-side test asks whether the final output distributions
   retain conductor-graded Fisher geometry.

The strongest future synthesis would measure both at once: decompose internal
Fourier features at a chosen layer, decompose output displacements into
conductor packets, and test whether internal packet energy predicts
output-side conductor energy after the unembedding and Softmax channel.

This distinction also clarifies a possible skeptical reading of the month
experiment.  If logit-space distances track cyclic structure better than
Fisher/Hellinger distances after Softmax, that does not refute the behavior
claim.  It suggests that some conductor structure may be sharper before the
final measurement channel and partially compressed by Softmax.  In that case
the output simplex is not the only place the structure lives; it is the place
where the structure becomes auditable as categorical behavior.  Closing this
loop requires the paired internal/output experiment above.

## 7. Empirical Tests

We use two structured output tasks.

The first is the weekday task, modeled as \(C_7\).  It is the prime control:
there is one nontrivial conductor packet, so the test is mainly a metric test.
Do Fisher/Hellinger-aware distances preserve the cyclic behavior geometry
when moment-Euclidean summaries collapse?

The second is the month task, modeled as \(C_{12}\).  It is the CRT control:
there are multiple conductor packets, so the test is both a metric test and an
energy-decomposition test.  Does the empirical displacement energy distribute
across the predicted conductors?

All measurements reported here are centroid-level behavior measurements.  They
are not yet a full training-time audit of how conductor packets emerge during
optimization.

### 7.1 Weekdays: the prime \(C_7\) control

For weekdays, the output algebra is \(C_7\).  We measured per-class output
distributions for Llama-3.1-8B and Mistral-7B-v0.3 at layer 28, last token,
and compared pairwise behavior distances to the cyclic arc distance.

The key correlation table is:

| Metric | Llama-3.1-8B | Mistral-7B-v0.3 | symmetric proxy |
|---|---:|---:|---:|
| Hellinger chord vs cyclic arc | \(0.899815\) | \(0.916873\) | \(0.910010\) |
| moment-Euclidean chord vs cyclic arc | \(0.614547\) | \(0.714715\) | \(0.886448\) |
| natural/logit chord vs cyclic arc | \(0.944337\) | \(0.955300\) | \(0.941295\) |
| Fisher Levi-Civita distance vs cyclic arc | \(0.903176\) | \(0.922202\) | \(0.911776\) |

The pattern is stable across two model families.  Moment-Euclidean summaries
pay the largest price.  Fisher/Hellinger-aware metrics preserve the cyclic
structure.

This is exactly what the Fisher-skeleton hypothesis predicts in the prime
case.  Since \(C_7\) has only one nontrivial conductor packet, the relevant
failure mode is not a split across multiple conductors.  It is the failure of
linear moment geometry to represent the curved behavior simplex.

### 7.2 Months: the composite \(C_{12}\) control

For months, the output algebra is

\[
C_{12}\cong C_4\times C_3.
\]

This task contains multiple conductors.  The measured Llama-3.1-8B
correlations are:

| Metric | real Llama-3.1-8B | symmetric proxy |
|---|---:|---:|
| Hellinger chord vs cyclic arc | \(0.708696\) | n/a |
| moment-Euclidean chord vs cyclic arc | \(0.210147\) | \(0.696128\) |
| natural/logit chord vs cyclic arc | \(0.870898\) | n/a |
| Fisher Levi-Civita distance vs cyclic arc | \(0.713899\) | n/a |

The moment summary collapses much more sharply than in the weekday case.  The
same measurement also gives a conductor-energy decomposition.  Averaged over
the 12 input classes, the empirical displacement energy is close to the
per-character-uniform null determined by packet dimensions
\((1,2,2,2,4)\), but with a small systematic high-conductor tilt:

| conductor | char. count | dimension null | observed | observed - null |
|---:|---:|---:|---:|---:|
| \(2\) | 1 | \(0.0909\) | \(0.0856\) | \(-0.0053\) |
| \(3\) | 2 | \(0.1818\) | \(0.1689\) | \(-0.0129\) |
| \(4\) | 2 | \(0.1818\) | \(0.1730\) | \(-0.0088\) |
| \(6\) | 2 | \(0.1818\) | \(0.1921\) | \(+0.0103\) |
| \(12\) | 4 | \(0.3636\) | \(0.3804\) | \(+0.0168\) |

This table changes the interpretation.  The aggregate split should not be
described, by itself, as proof that the model learned CRT-specific routing.
Most of the distribution is explained by packet dimension: conductor \(12\)
has four characters, conductors \(3,4,6\) have two, and conductor \(2\) has
one.  What remains is a modest but stable tilt away from conductors \(2,3,4\)
and toward \(6,12\).

A row bootstrap over the 12 input classes gives 95% confidence intervals for
the differences from the dimension null:

| conductor | bootstrap 95% CI for observed - null |
|---:|---:|
| \(2\) | \([-0.0102,-0.0013]\) |
| \(3\) | \([-0.0199,-0.0071]\) |
| \(4\) | \([-0.0155,-0.0036]\) |
| \(6\) | \([+0.0035,+0.0190]\) |
| \(12\) | \([+0.0088,+0.0260]\) |

A common output-label permutation null, which preserves the class probability
spectra while breaking the alignment with the \(C_{12}\) character basis,
places the observed conductor \(12\) fraction at the \(98.7\)th percentile and
the aggregate \(L^2\) distance from the dimension null at the \(98.0\)th
percentile.  This supports a cautious composite-control reading: the measured
month behavior is not random with respect to the \(C_{12}\) basis, but the
aggregate conductor table alone is not enough to claim CRT routing.

The class-level mixed conductor \(6\) row is more diagnostic.  Its mean is
\(0.1921\) against the dimension null \(2/11=0.1818\), but the largest
class-level elevations come from January (\(+0.045\)) and April (\(+0.035\)).
Thus the next empirical question is class anisotropy, not just aggregate
energy.  Prompt-level bootstraps, an unstructured 12-class control, and a
second model family are required before the composite result can carry the
same weight as the \(C_7\) replication.

The natural/logit chord result is also important.  On months it correlates
with the cyclic arc more strongly than Hellinger or Fisher endpoint distance.
This is consistent with the view that pre-Softmax coordinates retain a sharper
cyclic signal, while Softmax maps that signal into the curved probability
simplex where Fisher/Hellinger geometry becomes the correct output-side
metric.  Thus the logit result is not a nuisance to hide; it is evidence that
the conductor structure may straddle both sides of the final measurement
channel.  A paired internal-output conductor audit is the right test.

### 7.3 Activation pullback audit

One possible objection is that the metric gap might come from activation space
rather than from the output simplex.  Let

\[
F:A\to\Delta_R^\circ
\]

be the learned activation-to-behavior map.  The quadratic pullback metric is

\[
J_F^\top g_y J_F.
\]

If this pullback varies strongly across class pairs, then the metric gap could
be dominated by activation-side distortion rather than behavior-side
Fisher geometry.

The Llama-3.1-8B activation pullback audit gives:

| task | activation distance vs Hellinger | activation distance vs cyclic arc | pullback coefficient of variation |
|---|---:|---:|---:|
| weekdays | \(0.936878\) | \(0.900147\) | \(0.1540\) |
| months | \(0.821285\) | \(0.651696\) | \(0.2331\) |

For weekdays, the activation centroids are close to a rescaled isometry of the
Fisher/Hellinger output geometry.  This supports the interpretation that the
weekday metric gap is primarily intrinsic to the behavior simplex.  For
months, the activation map still preserves Hellinger geometry substantially,
but the larger coefficient of variation indicates that activation-side
distortion contributes more visibly.

This is a single-layer audit at layer 28.  It should not be interpreted as a
layer-invariant theorem.  A layer sweep is a required robustness check before
submission, especially because different layers may carry different mixtures
of internal Fourier structure, task abstraction, and final readout geometry.

### 7.4 Bigram confound control

The weekday and month outputs also show directional asymmetries.  For example,
some weekday classes leak more probability toward their cyclic predecessor
than toward their successor.  Such asymmetry could reflect arithmetic
off-centroid structure, but it could also reflect ordinary language exposure:
"Sunday Monday", "Monday Tuesday", and related bigram patterns.

To test this, a C4 corpus bigram control was run on 10 million whitespace
tokens.  The registered weekday criterion for "fully explain" required both
large correlation and high sign agreement.  The control landed in the
intermediate band:

| target | best qualitative verdict |
|---|---|
| Llama weekdays | intermediate |
| Mistral weekdays | intermediate |
| Llama months | intermediate |

The consequence is important.  Directional predecessor leakage should not be
used as independent proof of arithmetic carry.  It is consistent with a
mixture of learned language priors and residual cyclic structure.

The main support for the present paper is therefore not the asymmetry alone.
It is the metric gap, the prime/composite contrast, the \(C_{12}\)
null-controlled high-conductor tilt, and the activation-pullback audit.

### 7.5 Optimizer pilots

The conductor picture also suggests update-side controls.  If a task is
supposed to remain inside a closed conductor support, then an optimizer can
project the applied update into that support while leaving the stochastic
gradient and moments unprojected.  The clean rule is:

\[
\text{project the applied update, not the raw gradient.}
\]

In a synthetic \({\mathbb F}_4[u]/(u^2)\) conductor-closed optimizer pilot,
full update projection improved the measured KL relative to the unprojected
setting, from \(0.036156\) to \(0.023031\).  The corresponding
machine-precision leakage value is only a sanity check that the projection
operator projected into its declared support; it is not independent evidence
for the hypothesis.

In the calendar-transformer month pilots, update-only conductor Adam also
enforced machine-precision leakage relative to declared supports.  The most
relevant run is the width-64 offset-OOD split with mixed support \(\{6,12\}\):
training examples use offsets \(1,\ldots,6\), while test examples use unseen
offsets \(7,\ldots,12\).  Against Adam, update-only conductor Adam improved
test accuracy by \(+0.013889\), reduced the generalization gap by \(0.203329\),
and reduced test loss from \(8.694958\) to \(8.570058\), while leaving raw
gradients and Adam moments unprojected.  By contrast, the conductor-12-only
offset-OOD run hurt test accuracy by \(-0.027778\), and the full-support run
is the identity control.

These are small pilot numbers, but they are not merely "the projection
projected."  They suggest that the choice of conductor support can matter on a
held-out structured split.  The evidence should still be read as preliminary:
strong support for leakage control, suggestive support for support selection,
not yet a general-purpose optimizer theorem.

## 8. What the Evidence Shows

The current evidence supports four statements.

First, structured categorical outputs can expose Fisher/Hellinger geometry
that ordinary moment-Euclidean summaries miss.  This is replicated on the
weekday \(C_7\) task across Llama-3.1-8B and Mistral-7B-v0.3.

Second, composite structured outputs can be audited against conductor
structure.  The month \(C_{12}\) task is close to the per-character dimension
null but shows a small stable tilt toward conductors \(6\) and \(12\).  This
is suggestive composite-control evidence, not yet proof of CRT-specific
routing.

Third, the weekday metric gap is not primarily explained by activation
distortion at the audited layer.  The activation pullback is close to a
rescaled isometry of the output Hellinger geometry on the class-centroid set.

Fourth, update-side conductor projection can suppress declared leakage to
machine precision in pilots.  This is already useful as a diagnostic and as a
design pattern, even before it becomes a mature optimizer.

## 9. What the Evidence Does Not Show

The evidence does not show that all neural cognition is arithmetic.

It does not show that stochastic gradient descent universally decomposes into
conductor packets during training.  The current measurements are mostly final
behavior probes and small optimizer pilots.  A full training-time audit remains
future work.

It does not show that \(K^{CH}\) detects every filtered obstruction.  The cubic
tensor is a visible Fisher shadow.  Some extension data requires the
operator-valued quotient-character adjacency algebra rather than scalar
conductor summaries.

It does not show that linguistic confounds are absent.  The bigram control
shows that sequence priors explain part of the directional asymmetry.  The
stronger evidence is metric and null-controlled conductor-energetic, not
merely directional.

It does not show that a conductor-projected optimizer is ready to replace
Adam.  The optimizer evidence shows leakage control and promising local rows.
It is not yet a broad training benchmark.

It also does not yet separate two possible sources of the measured structure.
One possibility is behavior-simplex universality: any accurate model on a
structured categorical task will expose the same conductor geometry because
the output simplex and label algebra force it.  Another possibility is learned
representation specificity: only models that internally discover matching
Fourier or representation-theoretic features will show the conductor split
cleanly.  The decisive experiment is paired: measure internal Fourier/conductor
energy at several layers and output-side conductor energy on the same prompts,
then compare against label-permuted and unstructured 12-class controls.

These boundaries are not cosmetic.  They are the reason the narrower claim is
strong:

> Some large language model behavior manifolds contain measurable discrete
> Fisher skeletons.

That sentence is already enough.

## 10. Consequences for AI Diagnostics

The practical diagnostic question is:

> When is the quadratic Fisher approximation locally faithful, and when is it
> flattening structured cubic response?

This can be turned into concrete measurements.

1. Choose a structured output algebra \(R\).
2. Measure per-class output distributions.
3. Compare moment-Euclidean, logit, Hellinger, and Fisher distances.
4. Decompose displacements \(h_i=p_i-p_*\) into conductor packets.
5. Estimate \(K^{CH}_{p_*}(h_i)\) and cubic step fractions.
6. Audit activation pullback distortion via \(J_F^\top g_yJ_F\).
7. Run corpus or prompt controls for obvious confounds.

For the bounded information-investment version, the same audit keeps separate
prices for generated-subgroup descent, optional normalizer symmetry, PSL depth,
full filtered carry, support-visible carry, H4/H3 Fisher-shadow visibility,
remaining hidden residual, and resource cost.  This separation matters because
the certified local rows currently have zero support residual while retaining
positive full filtered residual.  The first \({\mathbb F}_4[u]/(u^2)\) ledger
is \(1569/0/72/1470/27\), and the current exact local aggregate is
\(180555/0/6648/173404/503\).

If the moment geometry collapses while Fisher/Hellinger geometry remains
stable, and if composite tasks distribute energy across predicted conductors,
then the behavior manifold is not being faithfully described by a featureless
smooth picture.

This matters for interpretability because it supplies a finite set of
behavior-side channels.  It matters for optimization because it supplies a
finite warning system for overconfident quadratic steps.  It matters for model
auditing because it separates three things that are often conflated:

1. output-side information geometry;
2. activation-side pullback distortion;
3. linguistic or dataset confounds.

## 11. Conclusion

Large language models are continuous systems trained by continuous
optimization, but their behavior is often categorical.  When those categories
carry finite algebraic structure, the behavior simplex after Softmax can
expose more than a smooth Fisher manifold.  It can expose a finite arithmetic
skeleton.

At maximum entropy, this skeleton appears as Fisher-orthogonal
quotient-character conductor packets.  Away from maximum entropy, the
Amari-Chentsov cubic gives the first structured correction that natural
gradient misses.  In real transformer outputs, the skeleton is visible most
cleanly in the prime control: weekday behavior preserves Fisher/Hellinger
geometry while moment summaries collapse across two model families.  The
composite month control adds a sharper moment collapse and a small, stable
high-conductor tilt relative to the per-character dimension null; it is a
promising but not yet decisive CRT-routing signal.

The conclusion is deliberately scoped.  This is not a universal claim about
all intelligence.  It is a sharper claim about structured categorical
behavior:

> Beyond smooth spaces, large language model behavior can contain discrete
> Fisher skeletons.

That is already a new object for AI diagnostics, optimization, and
interpretability.

## Data and Code Availability

The empirical artifacts summarized in this paper are stored in the companion
GitHub repository for this project.  The key checked-in reports are listed in
Appendix B.  The repository contains the scripts, report markdown files, JSON
payloads, and local artifact paths used to produce the tables above.  Some
large model-output tensors are stored as local safetensor artifacts and should
be mirrored or regenerated before archival release.

## Acknowledgments

The author used large language models extensively as research collaborators
while developing this manuscript and the surrounding program.  Their role was
to assist with derivation checking, adversarial review, exposition,
implementation planning, and synthesis across drafts.  The mathematical
claims, empirical framing, and remaining errors are the author's
responsibility.

---

## References

[Amari] Amari, S. *Information Geometry and Its Applications*. Applied
Mathematical Sciences, vol. 194. Springer, 2016.

[Chentsov] Chentsov, N.N. *Statistical Decision Rules and Optimal Inference*
(English translation). American Mathematical Society, 1982.

[Chughtai-Chan-Nanda] Chughtai, B., Chan, L., and Nanda, N. "A Toy Model of
Universality: Reverse Engineering how Networks Learn Group Operations."
Proceedings of the 40th International Conference on Machine Learning, PMLR
202:6243--6267, 2023.

[Murillo-Simplicial] Murillo Montero, L. *Intrinsic Vector Algebra on
Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum
Hyperplane*. Zenodo concept DOI 10.5281/zenodo.19689049, 2026.

[Nanda-Chan-Lieberum-Smith-Steinhardt] Nanda, N., Chan, L., Lieberum, T.,
Smith, J., and Steinhardt, J. "Progress Measures for Grokking via Mechanistic
Interpretability." arXiv:2301.05217, 2023.

[Power-Burda-Edwards-Babuschkin-Misra] Power, A., Burda, Y., Edwards, H.,
Babuschkin, I., and Misra, V. "Grokking: Generalization Beyond Overfitting on
Small Algorithmic Datasets." arXiv:2201.02177, 2022.

---

## Appendix A: Notation and Minimal Definitions

### A.1 The simplex and tangent space

For a finite output set \(R\), the open probability simplex is

\[
\Delta_R^\circ =
\left\{
p\in{\mathbb R}_{>0}^R : \sum_{a\in R}p_a=1
\right\}.
\]

The tangent space is the zero-sum hyperplane

\[
H_R =
\left\{
u\in{\mathbb R}^R : \sum_{a\in R}u_a=0
\right\}.
\]

The maximum-entropy point is

\[
p_* = |R|^{-1}\mathbf 1.
\]

### A.2 Fisher metric

For \(u,v\in H_R\), the Fisher metric is

\[
g_p(u,v)=\sum_{a\in R}\frac{u_a v_a}{p_a}.
\]

At \(p_*\),

\[
g_{p_*}(u,v)=|R|\sum_{a\in R}u_a v_a.
\]

This is the point at which the zero-sum simplicial gauge language of the
companion algebra paper becomes identical, up to scale, with the Fisher
tangent geometry of the categorical simplex.

### A.3 Characters and conductors

For \(C_N=\mathbb Z/N\mathbb Z\), the additive character indexed by \(k\) is

\[
\chi_k(a)=\exp(2\pi i k a/N).
\]

The trivial character \(k=0\) corresponds to the normalization direction.  The
nontrivial characters span \(H_R\otimes{\mathbb C}\).  The conductor of
\(\chi_k\) is

\[
\operatorname{cond}(k)=\frac{N}{\gcd(k,N)}.
\]

Characters with the same conductor form a conductor packet.

### A.4 Hellinger coordinates

The square-root map

\[
p\mapsto \sqrt{p}
\]

embeds the open simplex into the positive orthant of the unit sphere.  This is
why Hellinger distances are Fisher-aware rather than arbitrary Euclidean
features.  The Hellinger chord distance is the Euclidean chord distance after
the square-root embedding, up to the conventional normalization scale.

### A.5 Raised Amari-Chentsov cubic

The raised Amari-Chentsov tensor is written

\[
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)}.
\]

At the centroid of a finite group algebra, its first convolution form is

\[
K^{CH}_{p_*}(h)v
=
|R|\,h*v
-
|R|\,\langle h,v\rangle p_*.
\]

This is the cubic behavior-side correction emphasized in the main text.

---

## Appendix B: Empirical Artifact Ledger

This appendix lists the local reports behind the main empirical tables.  The
paths are repository-relative.  All files listed below live under
`empirical/reports/`; filenames are given without repeating that directory in
every row so the PDF tables stay readable.

### B.1 Weekday behavior reports

- Llama-3.1-8B \(C_7\) metric gap:
  `weekdays_K_CH_real_llama31_8b.md`.
- Mistral-7B-v0.3 \(C_7\) metric gap:
  `weekdays_K_CH_real_mistral_7b.md`.

The key result is cross-family replication: Fisher/Hellinger-aware metrics
remain near the cyclic geometry while moment-Euclidean summaries fall.

### B.2 Month behavior reports

- Llama-3.1-8B \(C_{12}\) metric gap:
  `months_K_CH_real_llama31_8b.md`.
- \(C_{12}\) conductor energy fractions:
  `months_K_CH_real_llama31_8b.md`.
- \(C_{12}\) per-character and permutation null comparison:
  the `months_conductor_null` report in `empirical/reports`.

The raw aggregate conductor split is:

\[
(0.0856,\ 0.1689,\ 0.1730,\ 0.1921,\ 0.3804)
\]

for conductors \(2,3,4,6,12\), respectively.  The null report compares this
against the packet-dimension null
\((0.0909,0.1818,0.1818,0.1818,0.3636)\) and records the small high-conductor
tilt toward \(6\) and \(12\).

### B.3 Activation pullback reports

- Weekday activation pullback:
  `activation_pullback_weekdays_llama31_8b.md`.
- Month activation pullback:
  `activation_pullback_months_llama31_8b.md`.

The weekday pullback coefficient of variation is \(0.1540\), supporting the
interpretation that the weekday metric gap is primarily behavior-side.

### B.4 Corpus confound reports

- C4 10M bigram summary:
  `bigram_corpus_control_c4_10M_summary.md`.
- Llama weekday detail:
  `bigram_corpus_control_weekdays_llama31_8b_c4_10M.md`.
- Mistral weekday detail:
  `bigram_corpus_control_weekdays_mistral_7b_c4_10M.md`.
- Llama month detail:
  `bigram_corpus_control_months_llama31_8b_c4_10M.md`.

The control lands in the intermediate band.  It partially explains
directional asymmetry and prevents overclaiming from predecessor leakage
alone.

### B.5 Optimizer and projection reports

- Synthetic conductor-closed optimizer:
  `conductor_closed_optimizer_f4_u2.md`.
- Projection Pareto sweep:
  `conductor_projection_pareto_f4_u2.md`.
- Month calendar transformer default split:
  `conductor_calendar_transformer_months.md`.
- Month calendar transformer offset-OOD, mixed support:
  \path{conductor_calendar_transformer_months_d64_offset_ood_c6_c12.md}.

The mixed-support offset-OOD pilot improves test accuracy by \(+0.013889\) and
reduces the generalization gap by \(0.203329\) against Adam on the same split.
The optimizer evidence supports leakage control and makes support selection
worth testing.  Broader performance claims require larger benchmarks.

---

## Appendix C: Falsifiers and Next Measurements

The discrete Fisher skeleton hypothesis is meant to be falsifiable.  The
following outcomes would weaken or narrow it.

1. On replicated structured tasks, Fisher/Hellinger distances collapse at the
   same rate as moment-Euclidean summaries.
2. Month-like composite tasks reduce entirely to the per-character-uniform
   null, with no stable high-conductor tilt and no class-level anisotropy.
3. Label-permutation and unstructured 12-class controls reproduce the same
   \(C_{12}\) conductor pattern.
4. Month-like composite tasks fail to show any stable conductor-energy
   decomposition across model families or prompt sets.
5. Activation-pullback distortion explains essentially all of the metric gap.
6. Corpus controls fully explain the observed geometry, including the metric
   gap and conductor-energy pattern, not merely directional asymmetry.
7. Training-time checkpoint audits show no conductor emergence from
   initialization through convergence.
8. Update-side conductor projections suppress leakage only by destroying task
   performance under fair baselines.

The next high-value measurements are:

1. replicate the \(C_{12}\) month null-controlled high-conductor tilt on a
   second model family;
2. add prompt-level bootstrap confidence intervals for the \(C_{12}\)
   conductor fractions;
3. run an unstructured 12-class control, such as colors or foods;
4. run layer sweeps for both weekdays and months;
5. run a paired internal-output conductor audit comparing hidden Fourier
   features with output-side conductor energy;
6. run checkpoint audits from initialization to convergence on a small
   transformer trained on structured labels;
7. mirror or regenerate all large safetensor artifacts for public archival
   release.

---

## Appendix D: Scope Boundaries

This paper uses the following restricted meanings.

**Behavior manifold.**  The finite set of measured output distributions and
the Fisher/Hellinger geometry they inherit from the probability simplex.

**Discrete Fisher skeleton.**  The character/conductor decomposition of the
Fisher tangent space at maximum entropy, together with its off-centroid cubic
and finite-adjacency corrections.

This paper assumes the algebraic frame of [Murillo-Simplicial] and tests its
statistical instantiation on model behavior.  The fuller dually-flat
\((\theta,\eta)\) development of simplicial coordinates is treated elsewhere;
it is not the main claim of this paper.

**Conductor packet.**  A group of nontrivial additive characters sharing the
same conductor.

**Cubic diagnostic.**  The use of \(K^{CH}\) to estimate when the quadratic
Fisher approximation is missing structured behavior-side response.

**Not claimed.**  The paper does not claim that every neural representation is
arithmetic, that every task has a useful finite quotient structure, that
ordinary Adam should be replaced, or that final-output measurements by
themselves prove training-time conductor dynamics.

---

## Appendix E: Pandoc and LaTeX Notes

This manuscript is written as Pandoc-compatible Markdown with LaTeX math.
Displayed equations use

```tex
\[
...
\]
```

and inline equations use `\(...\)`.  Tables are plain Markdown pipe tables.
The top title block follows the same convention as the companion manuscript:
an H1 title, a bold author line, an italic date line, an abstract block, and a
horizontal rule before the main body.
