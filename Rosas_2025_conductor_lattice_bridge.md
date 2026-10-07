# Rosas 2025 Conductor-Lattice Bridge

**Implementation status:** Folded into the conductor program in May 2026.
Paper 9 now contains the conductor macrovariable framing and Problem 9.8;
Paper 10 now distinguishes closure levels and adds Problem 10.3; Paper 11 now
frames \(\operatorname{Ext}_{CH}\) as a macrovariable-closure obstruction and
adds Problem 11.8.

**Bridge note.**  This note records the cautious translation between Rosas et
al.'s symmetry/subgroup-lattice language for informationally closed
macrovariables and this program's conductor lattice, sufficiency tower,
Carlitz-Hayes normalizer, and \(\operatorname{Ext}_{CH}\) filtration.

The note uses only the Rosas-side features named in the working prompt:
symmetry subgroups, a subgroup lattice, and informationally closed
macrovariables.  It does not assume any unverified theorem from the Rosas PDF.

---

## 1. Safe Dictionary

The safe common object is not a single group, but a refinement lattice of
observable descriptions.

On the Rosas side, a macrovariable is understood as a coarse description of
microstates.  Informational closure means, at minimum, that the macrovariable
captures the information relevant to the chosen predictive or inferential
question without needing to refine back to the full microstate description.
When the macrovariable is symmetry-defined, its position is controlled by a
subgroup or orbit lattice.

On the present program's side, Paper 10 gives the exact finite categorical
model.  For a finite quotient

$$
R=A/I,
$$

and a divisor or ideal \(\mathfrak d\mid I\), the quotient

$$
\pi_{\mathfrak d}:R\to A/\mathfrak d
$$

defines a quotient sigma algebra \({\mathcal F}_{\mathfrak d}\).  The
\({\mathcal F}_{\mathfrak d}\)-measurable categorical subfamily has tangent
space

$$
L_{\le \mathfrak d}
=
\bigoplus_{\mathfrak e\mid\mathfrak d,\ \mathfrak e\ne1}
H_R^{[\mathfrak e]},
$$

and the new layer at \(\mathfrak d\) is the primitive conductor block
\(H_R^{[\mathfrak d]}\).  Thus the conductor lattice is a sufficiency tower:
it records which quotient statistics the model is allowed to see.

The careful bridge is therefore:

$$
\text{Rosas subgroup/orbit lattice of macrovariables}
\quad\leadsto\quad
\text{conductor lattice of quotient sufficient statistics}.
$$

This is a structural analogy with an exact local realization in the finite
quotient categorical models.  It should not be phrased as saying that every
Rosas subgroup lattice is already a conductor lattice.

---

## 2. Informational Closure vs. Conductor Sufficiency

The conductor lattice gives a mathematically rigid version of informational
closure.

For each \(\mathfrak d\mid I\), the quotient observation
\(\pi_{\mathfrak d}(x)\) is sufficient for the
\({\mathcal F}_{\mathfrak d}\)-measurable categorical subfamily.  It is not
sufficient for the full \(R\)-outcome family unless \(\pi_{\mathfrak d}\) is
injective.  This distinction is important: the program's claim is not that a
coarse macrovariable sees all microscopic information.  The claim is that,
once a model class is restricted to that macro-description, the conductor
quotient is exactly the sufficient statistic for that restricted family.

In Rosas language, this says:

> An informationally closed macrovariable should be modeled not as an
> arbitrary coarse grain, but as a closed layer in a refinement lattice of
> sufficient statistics.

The conductor blocks then measure what information enters when one refines
from lower macro-layers to a higher one.  The primitive block
\(H_R^{[\mathfrak d]}\) is the new tangent statistic made visible at that
refinement step.

---

## 3. Bayesian Belief Hierarchy

The Rosas belief hierarchy has a direct translation in this language.

If an observer only sees the quotient observation \(\pi_{\mathfrak d}(X)\),
then Bayesian updating takes place inside the categorical family measurable
with respect to \({\mathcal F}_{\mathfrak d}\).  The posterior can only move
in the tangent directions

$$
L_{\le \mathfrak d}
=
\bigoplus_{\mathfrak e\mid\mathfrak d,\ \mathfrak e\ne1}
H_R^{[\mathfrak e]}.
$$

Thus the abstract belief state at level \(\mathfrak d\) is the epistemic
shadow of the same conductor layer: the observer's sufficient statistic is
the quotient map, and the Fisher metric on that restricted family is the
geometry of belief change at that resolution.  Refining from
\(\mathfrak c\) to \(\mathfrak d\) adds the primitive block
\(H_R^{[\mathfrak d]}\), exactly as Rosas' subgroup-lattice picture adds new
distinctions between macrovariables.

This is the precise sense in which "hierarchical belief updating" becomes
"Fisher geometry at scale" inside the arithmetic categorical models.

---

## 4. Symmetry Groups and Normalizers

The subgroup lattice in Rosas et al. should be compared with two different
symmetry levels in this program.

First, at the centroid \(p_*=|R|^{-1}{\bf 1}\), the translation action of
\(R\) fixes the categorical distribution and acts unitarily on the Fisher
tangent space

$$
H_R=\{x\in{\mathbb C}^R:\sum_a x_a=0\}.
$$

The additive-character decomposition, grouped by conductor, is the
conductor-block decomposition of Paper 9.  This is the exact point where the
macro-lattice has an orthogonal Fisher meaning: conductor packets are
translation-isotypic Fisher tangent packets at maximum entropy.

Second, Paper 9 deliberately leaves the full Carlitz-Hayes symmetry as the
next layer: identify the enlarged normalizer acting on Hayes characters,
conductor blocks, block signs, kernels, and convex hull structure.  Paper 11
then makes that layer operational by replacing scalar conductor compression
with the quotient-character adjacency algebra.  The global normalizer has the
expected local-global form: local Hayes normalizers, plus wreath-product
symmetries for repeated local factors.

Thus the Rosas subgroup lattice suggests a useful external question:

> Which subgroup actions preserve the macrovariable as a closed information
> layer, and which subgroup actions only preserve its conductor-graded shadow?

The second clause is exactly where the Carlitz-Hayes normalizer becomes
relevant.

---

## 5. The Ext_CH Filtration as Hidden Macro-Structure

The Rosas bridge becomes more interesting off the centroid or inside
nonsemisimple local factors.

Paper 11 says conductor blocks alone are too coarse once the Fisher tensor is
studied off the centroid.  The correct compressed object is not a scalar
indexed by two conductors.  It is an operator-valued coefficient in the
quotient-character adjacency algebra.  Locally, this algebra has a depth
filtration whose associated graded separates tame residue behavior from wild
congruence behavior.

The finite filtered extension datum is called

$$
\operatorname{Ext}_{CH}(R_{\mathfrak p}).
$$

Locally confirmed scope: this is not asserted to be a derived functor.  It is
the filtered-isomorphism class of the local quotient-character adjacency
algebra over its tame/wild associated graded.  Its slogan in Paper 11 is that
it is not new data beyond the local ring, but it is new data beyond the
conductor-graded shadow.

In Rosas terms, this gives a warning and an opportunity.

The warning: a macrovariable may look closed at the level of subgroup or
conductor grading while still hiding internal filtered structure.

The opportunity: informational closure can be stratified.  A first pass asks
whether the macro-layer is closed in the conductor lattice.  A sharper pass
asks whether the adjacency algebra inside that layer splits over its graded
tame/wild shadow.  Failure to split is an \(\operatorname{Ext}_{CH}\)-type
macro-internal invariant.

---

## 6. Recommend to Rosas Team

Recommend that the Rosas team test their subgroup-lattice construction on
finite quotient categorical systems \(R=A/I\), using conductor quotients
\(\pi_{\mathfrak d}:R\to A/\mathfrak d\) as the benchmark examples of
informationally closed macrovariables.

Ask them to separate three claims:

1. **Closure claim.**  A macrovariable is closed relative to a chosen model
   class or predictive task, not absolutely closed relative to the full
   microstate family.
2. **Lattice claim.**  The relevant lattice should be a lattice of quotient
   sufficient statistics or orbit sigma algebras; in the arithmetic benchmark,
   this is exactly the conductor lattice.
3. **Normalizer claim.**  The symmetry group of the macrovariable is not just
   the subgroup fixing a partition.  The sharper object is the normalizer of
   the character or adjacency algebra preserving the closed macro-layer.

Concretely, propose the following joint test case:

> Take \(R={\mathbb F}_4[u]/(u^2)\).  Compare Rosas-style subgroup-generated
> macrovariables with the conductor layers, the tame/wild depth filtration,
> and the local Hayes-Frobenius normalizer orbits computed in Paper 11.  Ask
> which macrovariables are closed at conductor level and which remain
> sensitive to the \(\operatorname{Ext}_{CH}\) filtered extension datum.

This test is small enough for exact enumeration and rich enough that
conductor grading, tame residue action, wild nilpotent tails, normalizer
orbits, and the first nontrivial \(\operatorname{Ext}_{CH}\) representative
all appear.

---

## 7. What This Imports Back Into the Program

The Rosas vocabulary imports three useful disciplines back into the
conductor program.

First, it gives a better external name for Paper 10's sufficiency tower:
conductor layers are informationally closed macrovariables for quotient
categorical subfamilies.

Second, it suggests that the program should distinguish closure levels:
partition closure, sufficient-statistic closure, normalizer closure, and
filtered adjacency-algebra closure.  These are not the same assertion.

Third, it motivates a Rosas-style audit of \(\operatorname{Ext}_{CH}\):
for each local row, list which conductor macrovariables are closed at the
graded level and which require the full filtered local adjacency algebra.
That would turn \(\operatorname{Ext}_{CH}\) from an internal arithmetic
diagnostic into a macrovariable-closure obstruction.

The bridge claim should therefore be stated modestly:

> Rosas et al.'s subgroup-lattice macrovariables provide the external
> language of informational closure; the conductor lattice gives this program
> an exact arithmetic family of such closures; the Carlitz-Hayes normalizer and
> \(\operatorname{Ext}_{CH}\) filtration measure when closure at the visible
> conductor level is not the whole story.
