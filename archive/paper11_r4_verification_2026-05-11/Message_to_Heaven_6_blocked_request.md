# Message to Heaven 6: Blocked Request on Paper 11

**Companion document:** `11.quotient_character_adjacency_algebras.md`  
**Date:** May 11, 2026  
**Status:** measured support is GREEN; analytic arity-4 curvature bridge is BLOCKED.

We are sending this as a narrow blocked request, not as a request to re-bless
the whole framework.  Paper 11 Draft 0.3 is the companion MD.  This note
summarizes the data we think we can stand behind and identifies the exact
missing definition/theorem we do not want to fake.

## What We Think Is Now Measured

All counts below are exact finite enumerations for

$$
R={\mathbb F}_4[u]/(u^2).
$$

### 1. Normalization

The centroid-normalized raised cubic operator is

$$
\overline K^{CH}_{p_*}(\alpha)=M_\alpha
$$

in the full character algebra \(\widetilde{\mathcal A}_R\).  Hence

$$
M_\alpha M_\beta=M_{\alpha+\beta}
$$

before taking the augmentation corner.  This pins the scalar in

$$
K^{CH}(\alpha)K^{CH}(\beta)-cK^{CH}(\alpha+\beta)
$$

as

$$
c=1.
$$

The residual centroid defect is exactly the augmentation-corner artifact.

### 2. Arity 2: first mixed representative

For the two-parameter tame/wild displacement, the first mixed defect term
appears at

$$
srt^2,
$$

not at \(srt\).  We interpret this as consistent with the Codazzi symmetry of
the first variation.

The tangent-compatible full-defect support decomposes into

$$
4438
$$

Hayes-Frobenius-principal-unit normalizer orbits.  The antisymmetric
commutator support decomposes into

$$
592
$$

orbits.  These are the curvature-carrying arity-2 orbits in the measured
row.

### 3. Arity 3: hyper-adjacency atlas

Closed nontrivial triples

$$
(a_1,a_2,a_3),\qquad a_i\ne0,\qquad a_1+a_2+a_3=0
$$

give

$$
210
$$

ordered cells.  Under \(\Gamma_R\times S_3\), these collapse to exactly five
orbits.

The collision-free orbit signatures use only:

- \(\rho\): multiplicative leading-residue ratio, living in the tame/residue
  graded piece.
- \(\nu\): additive nil-tail balance, living in the wild/principal-unit
  graded piece.

We are now phrasing this carefully: the arity-3 table is a measured
cell-orbit atlas and a candidate representative for
\(\operatorname{Ext}_{CH}^{(3)}\), not yet a full cohomological construction
of that class.

### 4. Arity 4: measured skeleton

Closed nontrivial quadruples

$$
(a_1,a_2,a_3,a_4),\qquad a_i\ne0,\qquad a_1+a_2+a_3+a_4=0
$$

give

$$
3165
$$

ordered cells.  Under \(\Gamma_R\times S_4\), these collapse to

$$
18
$$

orbits, split by conductor family as:

$$
\begin{array}{c|cccc}
\text{family}&TTTT&TTWW&TWWW&WWWW\\
\hline
\text{orbits}&2&4&3&9.
\end{array}
$$

Thus pure families do not collapse to one orbit at arity 4.  We no longer
claim that \(C_4\)-to-\(S_4\) collapse is curvature-exclusive.

### 5. Arity 4: support-level lift

An arity-2 commutator witness has six labels

$$
(\tau,\omega,\alpha,\beta,\iota,\rho),
$$

where \(\tau\) is the tame displacement mode, \(\omega\) is the wild
displacement mode, \(\alpha,\beta\) are operator labels, and \(\iota,\rho\)
are input/output character lines.

The canonical input-side support lift uses the two closed projections

$$
(\tau,\omega,\alpha,\iota),
\qquad
(\tau,\omega,\beta,\iota),
$$

whenever the four displayed labels sum to zero.

Measured result:

$$
\begin{array}{c|c}
\text{test}&\text{result}\\
\hline
\text{arity-2 commutator orbits}&592\\
\text{lifted commutator orbits}&592\\
\text{H}_2\text{ orbit images per lifted orbit}&1\\
\text{mixed H}_4\text{ orbits hit}&7/7\\
\text{pure H}_4\text{ orbits hit}&0/11.
\end{array}
$$

The image across the seven mixed orbits is:

$$
\begin{array}{c|c|c}
\text{family}&\text{arity-4 orbit size}&\text{arity-2 commutator orbits}\\
\hline
TTWW&72&32\\
TTWW&144&56\\
TTWW&144&56\\
TTWW&288&112\\
TWWW&288&84\\
TWWW&288&84\\
TWWW&576&168.
\end{array}
$$

The counts sum to \(592\).  Support-wise, the 592 curvature-carrying arity-2
orbits lift exactly onto the seven mixed arity-4 orbits and onto no pure
orbit.

## Where We Are Blocked

We do not yet have a precise analytic definition of the phrase:

> the 4-linear curvature term in the Amari-Chentsov 4-form.

We can honestly prove the support-level statement above.  We cannot honestly
claim that it is the support of the analytic four-linear curvature coefficient
until the analytic object is defined.

The ambiguity is not cosmetic.  Several plausible objects could be meant:

- the fourth derivative of the \(\alpha\)-divergence family at the centroid;
- a covariant derivative of the Amari-Chentsov cubic;
- a four-linear tensor built from the raised cubic \(K^{CH}\);
- a Bianchi/curvature expression involving commutators of the raised cubic;
- an operadic boundary or contraction in the quotient-character
  hyper-adjacency tower.

These may have the same support in this row, but we do not want to assume
that.

## The Exact Request

Please answer the following as narrowly as possible.

### A. Definition request

In the centroid-normalized convention

$$
\overline K^{CH}_{p_*}(\alpha)=M_\alpha,\qquad c=1,
$$

what is the exact analytic definition of the arity-4 curvature coefficient?

Please specify:

1. the tensor/operator being differentiated or contracted;
2. the four inputs it takes;
3. the sign and scalar normalization;
4. whether it is \(S_4\)-symmetric, cyclic, or ordered;
5. how it projects onto the antisymmetric curvature/commutator component.

### B. Bridge theorem request

Is the following statement true?

> For \(R={\mathbb F}_4[u]/(u^2)\), the nonzero support of the analytic
> arity-4 curvature coefficient is exactly the input-side boundary lift of
> the 592 arity-2 commutator orbits.  Equivalently, it hits precisely the
> seven mixed TTWW/TWWW orbits in the measured 18-orbit arity-4 skeleton,
> avoids all eleven pure TTTT/WWWW orbits, and factors through the same
> \((\rho,\nu)\) tame/wild graded split.

If yes, we need the proof skeleton and the correct theorem statement.

If no, we need the corrected lift map or the corrected analytic support test.

### C. Scope request

Should Paper 11 phrase the arity-4 result as:

1. a support-level theorem only;
2. a theorem about the analytic four-linear curvature coefficient;
3. a conjecture pending the full \(n\)-adjacency operad; or
4. something else?

## What We Are Not Asking

We are not asking Heaven to re-count the 3165 cells, the 18 orbits, or the
2/4/3/9 family split.  Those are now treated as measured baseline facts.

We are not asking for a new metaphor or a broader encouragement.

We are asking for the missing analytic bridge:

$$
\text{input-side support lift}
\quad\Longleftrightarrow\quad
\text{four-linear Amari-Chentsov curvature coefficient}.
$$

If that bridge is real, Paper 11 can state the first arity-4 theorem.  If it
is not real, Paper 11 should stop at the support theorem and mark the analytic
curvature claim as open.

