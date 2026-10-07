# Draft 0.3.1 Internal: \(\Delta^{(4)}\) as an \(NC_4\) Cumulant

**Status:** internal working note, now backed by a two-cell covariant
verification of Heaven's paired-slot recipe.
**Date:** May 11, 2026
**Purpose:** write the missing arity-4 lower-contraction formula explicitly
enough to support Theorem 9.3, with coefficient claims still limited to the
verified row described below.

## 1. Motivation

Section 9.1 writes the arity-2 mixed defect explicitly:

$$
C_\alpha M_\beta
+B_\alpha^\tau B_\beta^{\omega_0}
+B_\alpha^{\omega_0}B_\beta^\tau
+M_\alpha C_\beta
-C_{\alpha\beta}.
$$

Section 9.3 had used the phrase "all lower-order contractions" in

$$
\Delta^{(4)}(\alpha,\beta,\gamma,\delta)
=
\overline K^{CH}(\alpha)\overline K^{CH}(\beta)
\overline K^{CH}(\gamma)\overline K^{CH}(\delta)
-\text{all lower-order contractions}.
$$

That phrase is now replaced by a formula.  The independent verifier confirms
that the unrestricted product rule first gives the full partition-lattice
\(\Pi_4\) contraction, and the paired-slot Bianchi projection then converts it
to the \(NC_4\) contraction.

## 2. Verified Paired-Slot Formula

Let

$$
x_1=\alpha,\quad x_2=\beta,\quad x_3=\gamma,\quad x_4=\delta.
$$

For a block \(B\subseteq\{1,2,3,4\}\), define

$$
x_B=\sum_{i\in B}x_i,
$$

using the additive character-label group.  Let

$$
M_B=M_{x_B}
$$

be the centroid-normalized full-character multiplication operator, followed
by the augmentation-corner projection.

The unrestricted Leibniz expansion is

$$
\Delta_{\Pi}^{(4)}
=
\sum_{\pi\in\Pi_4}\mu_{\Pi}(\pi,1_4)M_\pi.
$$

Let

$$
m=\{\{1,3\},\{2,4\}\}
$$

be the middle pair-of-pairs split.  The paired-slot Bianchi projection applies
the correction

$$
{\bf 1}_{\pi\le m}\mu_{\Pi}(\pi,m)
$$

to each unrestricted Leibniz coefficient.  Thus the verified formula is

$$
\Delta_{\mathrm{pair}}^{(4)}
=
\sum_{\pi\in\Pi_4}
\left(
\mu_{\Pi}(\pi,1_4)
 +{\bf 1}_{\pi\le m}\mu_{\Pi}(\pi,m)
\right)M_\pi.
$$

Equivalently, for four slots this is the non-crossing contraction.  For a
non-crossing partition

$$
\pi=\{B_1,\ldots,B_k\}\in NC_4,
$$

order the blocks by their first index and define

$$
M_\pi=M_{B_1}M_{B_2}\cdots M_{B_k}.
$$

The arity-4 lower-contraction formula is the \(NC_4\) cumulant

$$
\kappa_4^{NC}(x_1,x_2,x_3,x_4)
=
\sum_{\pi\in NC_4}\mu_{NC}(\pi,1_4)M_\pi.
$$

Here \(1_4=\{\{1,2,3,4\}\}\), and \(\mu_{NC}\) is the Mobius function of
\(NC_4\).

Equivalently,

$$
\Delta_{NC}^{(4)}
=
M_{1234}
-\sum_{\substack{\pi\in NC_4\\|\pi|=2}}M_\pi
+\sum_{\substack{\pi\in NC_4\\|\pi|=3}}\mu_{NC}(\pi,1_4)M_\pi
-5M_1M_2M_3M_4,
$$

with the three-block coefficients inherited from \(NC_4\), not from \(\Pi_4\).

## 3. The 14 Terms

Using slot names

$$
(x_1,x_2,x_3,x_4)=(\tau,\omega,\beta,\iota)
$$

for the first size-12 witness, the \(NC_4\) terms are:

$$
\begin{array}{c|c}
\pi&\mu_{NC}(\pi,1_4)\\
\hline
\{\tau,\omega,\beta,\iota\}&1\\
\{\tau\}\mid\{\omega,\beta,\iota\}&-1\\
\{\tau,\omega\}\mid\{\beta,\iota\}&-1\\
\{\tau,\omega,\beta\}\mid\{\iota\}&-1\\
\{\tau,\omega,\iota\}\mid\{\beta\}&-1\\
\{\tau,\beta,\iota\}\mid\{\omega\}&-1\\
\{\tau,\iota\}\mid\{\omega,\beta\}&-1\\
\{\tau\}\mid\{\omega\}\mid\{\beta,\iota\}&2\\
\{\tau\}\mid\{\omega,\beta\}\mid\{\iota\}&2\\
\{\tau\}\mid\{\omega,\iota\}\mid\{\beta\}&1\\
\{\tau,\omega\}\mid\{\beta\}\mid\{\iota\}&2\\
\{\tau,\beta\}\mid\{\omega\}\mid\{\iota\}&1\\
\{\tau,\iota\}\mid\{\omega\}\mid\{\beta\}&2\\
\{\tau\}\mid\{\omega\}\mid\{\beta\}\mid\{\iota\}&-5.
\end{array}
$$

The unique crossing two-block partition

$$
\{\tau,\beta\}\mid\{\omega,\iota\}
$$

is omitted.  In the first witness this omitted crossing term is exactly the
difference between the \(\Pi_4\) value and the \(NC_4\) value.

## 4. Cancellation Interpretation

The cancellation structure is block-local.

For each block \(B\):

1. **Codazzi kill.**  First-order antisymmetric pickups inside \(B\) vanish
   because \(\nabla^{(0)}K^{CH}\) is totally symmetric at \(p_*\).  Thus a
   block contributes only through its symmetric centroid-normalized
   multiplication route unless at least two independent mixed directions
   survive after the block contraction.

2. **\(c=1\) augmentation kill.**  Any route whose only obstruction is the
   trivial-character line is removed by the centroid normalization
   \(\overline K^{CH}_{p_*}(\alpha)=M_\alpha\) and the choice \(c=1\).  These
   are the direct arity-4 analogues of the arity-2 augmentation-corner
   baseline subtraction.

After these two kills, the only support that survives on the measured row is
the input-side boundary lift of the arity-2 commutator support.

## 5. Witness Checks So Far

### TTWW size-12

Archived diagnostic:
`archive/paper11_r4_verification_2026-05-11/h4_mobius_witness.md`

Witness:

$$
(\tau,\omega,\alpha,\beta,\iota,\rho)=(u,1,u,1,u,u).
$$

Lift:

$$
(\tau,\omega,\beta,\iota)=(u,1,1,u).
$$

At \(u\leftarrow u\):

$$
\Pi_4=-2,\qquad NC_4=-1,\qquad \text{inherited commutator}=-1.
$$

Here \(NC_4\) matches and \(\Pi_4\) overshoots by the omitted crossing
partition.

### TTWW size-24

Archived diagnostic:
`archive/paper11_r4_verification_2026-05-11/h4_mobius_witness_size24.md`

At the chosen witness:

$$
\Pi_4=-2,\qquad NC_4=-1,\qquad \text{inherited commutator}=-1.
$$

Again \(NC_4\) matches and \(\Pi_4\) overshoots by the crossing partition.

### TWWW minimal witness

Archived diagnostic:
`archive/paper11_r4_verification_2026-05-11/h4_mobius_witness_twww.md`

There is no TWWW size-12 class under the measured input-side lift:

$$
\#(TWWW,\text{ arity-2 orbit size }12)=0.
$$

The minimal TWWW class has arity-2 orbit size \(24\).  At the chosen positive
witness:

$$
\Pi_4=1,\qquad NC_4=1,\qquad \text{inherited commutator}=1.
$$

This witness is consistent with \(NC_4\), but it does not distinguish
\(NC_4\) from \(\Pi_4\).  Across the full TWWW size-24 class, the cumulant
value at the tested diagonal is \(+1\) for both \(\Pi_4\) and \(NC_4\), while
the inherited commutator sign splits \(168/168\).  Therefore the TWWW family
requires an orientation/sign convention before it can be used as a signed
coefficient test.

## 6. Current Conclusion

The first TTWW size-12 probe showed:

$$
\Pi_4=-2,\qquad NC_4=-1,\qquad \text{inherited commutator}=-1.
$$

At that single cell, \(NC_4\) matches the inherited commutator target while
\(\Pi_4\) overshoots by the unique crossing partition.

The follow-up class scan prevents one mistaken reading.  In the TTWW size-24
class, the inherited commutator coefficient and the cumulant values are not
aligned as class functions:

$$
\begin{array}{c|c}
\text{quantity}&\text{TTWW size-24 class}\\
\hline
\text{records}&248\\
\text{inherited coefficient distribution}&-1:124,\ +1:124\\
\Pi_4\text{ value distribution}&-2:40,\ +1:168,\ +2:40\\
NC_4\text{ value distribution}&-1:40,\ +1:168,\ +2:40\\
\Pi_4\text{ matches inherited}&84/248\\
NC_4\text{ matches inherited}&104/248.
\end{array}
$$

The \(104/248\) match count is exactly the independence expectation on the
records where matching is even possible.  Thus the cumulant and the inherited
lift coefficient are measuring different things on this row.  The inherited
coefficient is not the signed target for the coefficient-level curvature
formula.

The independent covariant verifier now supplies the missing datum.  File:
`empirical/compute_R4_covariant_at_cell.py`.

At the sealed target cell,

$$
(\tau,\omega,\beta,\iota)=(u,1,1,u),\qquad u\leftarrow u,
$$

the unrestricted Leibniz expansion gives

$$
\frac{-48}{4!}=-2,
$$

and the paired-slot Bianchi projection cancels the middle split
\(\{\tau,\beta\}\mid\{\omega,\iota\}\), giving

$$
R^{(4)}(u,1,1,u)_{u\leftarrow u}
=\frac{-24}{4!}=-1.
$$

At the TTWW arity-2 orbit-size-24 \(+2\) discriminator cell,

$$
(\tau,\omega,\beta,\iota)=(wu,w,wu,w),\qquad w\leftarrow w,
$$

the same recipe gives

$$
R^{(4)}(wu,w,wu,w)_{w\leftarrow w}
=\frac{48}{4!}=2.
$$

The full mixed-lift table then scans all \(592\) support records over the
seven mixed arity-4 orbits.  It gives

$$
\begin{array}{c|ccc}
\text{value}&-1&1&2\\
\hline
\text{records}&44&504&44.
\end{array}
$$

The correct current posture is therefore:

$$
NC_4\text{ tracks the paired-slot covariant }R^{(4)}
\text{ on the full mixed lift,}
$$

while the inherited arity-2 lift coefficient remains a support selector rather
than a signed coefficient formula.  This is enough to unseal the target-cell
anchor and to rewrite Paper 11's arity-4 discussion around the paired-slot
\(NC_4\) contraction on the seven mixed support orbits, without promoting the
inherited lift coefficient itself to a coefficient-level theorem.
