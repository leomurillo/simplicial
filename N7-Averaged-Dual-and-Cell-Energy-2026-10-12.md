# Averaged dual constraints and the off-diagonal cell energy

12 October 2026. Continuation of the uniform-height mission through the averaged Stirling-envelope optimum. This note proves an unconditional bound for the diagonal contribution to the auxiliary's penalty and identifies the remaining signed correlation sum exactly. It does not establish the required bound for the off-diagonal contribution or prove RH.

## 1. Averaging the dual does not impose consistency across scales

For each integer x, let P_x be the dual feasible set from Paper 53 §4.12: a nonnegative vector z on J(x), with each factorial floor moment lying between the two Stirling bracket endpoints. Its objective is z_1, and E*(x)=sup_(z in P_x) z_1.

For a finite block of x, independence of these feasible sets gives the exact identity

\[
\sum_{X<x\le2X}E^*(x)
=\sup_{(z^{(x)})\in\prod_x P_x}\sum_{X<x\le2X}z^{(x)}_1.
\tag{1}
\]

No condition in this product requires the optimizing fake prime masses at two different x to come from one common arithmetic measure. Imposing such consistency creates a smaller problem; its upper bound would not automatically bound the original optimum. Thus an averaged proof needs either feasible primal certificates whose total cost is bounded or a dual estimate valid for every independently chosen family.

This observation does not prevent an averaged bound. It identifies a constraint that cannot silently be added to prove one.

## 2. A quadratic quantity controlling the Möbius penalty

Put L=floor(sqrt X), and for integer x define

\[
\Delta_m(x)=M(x/m)-M(x/(m+1)),\qquad
Q(X)=\sum_{X<x\le2X}\sum_{m=2}^{L}m\,\Delta_m(x)^2.
\tag{2}
\]

Let H_L=Σ_(m=2)^L 1/m. Cauchy–Schwarz over the pair (x,m) gives

\[
\sum_{X<x\le2X}\sum_{m=2}^{L}|\Delta_m(x)|
\le\sqrt{XH_L Q(X)}.
\tag{3}
\]

All cells with m>L together contain only integers k≤2X/(L+1), so their total absolute Möbius mass is O(sqrt X) at each x. Consequently

\[
\boxed{\sum_{X<x\le2X}V(x)
\le\sqrt{XH_L Q(X)}+O(X^{3/2}).}
\tag{4}
\]

This is unconditional. Together with the established envelope inequality, it bounds the penalty above the actual prime window:

\[
\sum_{X<x\le2X}\big(E^*(x)-W(x)\big)
\ll(\log X)\left[\sqrt{XH_LQ(X)}+X^{3/2}\right].
\tag{5}
\]

It is important that (5) is centered at W(x), not x/2. An estimate for the penalty alone must not be mistaken for an estimate for the complete prime discrepancy.

## 3. Exact expansion into diagonal and off-diagonal terms

For positive integers a≤b, let

\[
N_{m,X}(a,b)=
\max\left(0,\min\{2X,(m+1)a-1\}
             -\max\{X+1,mb\}+1\right).
\tag{6}
\]

This counts exactly the integer x in (X,2X] for which both a and b lie in (x/(m+1),x/m]. Indeed, membership of n in that cell is mn≤x<(m+1)n.

Expanding the square in (2) therefore proves

\[
Q(X)=D(X)+R(X),
\]
\[
D(X)=\sum_{m=2}^L m\sum_a\mu(a)^2N_{m,X}(a,a),
\]
\[
\boxed{R(X)=2\sum_{m=2}^L m\sum_{a<b}
                 \mu(a)\mu(b)N_{m,X}(a,b).}
\tag{7}
\]

Every weight is nonnegative and given by floor-free integer endpoints. A nonzero off-diagonal weight requires m(b−a)<a. Thus R is a particular weighted sum of additive Möbius correlations, not a generic appeal to random signs.

## 4. The diagonal has the required size without RH

For fixed m, at most 2X/m positive integers a can contribute, and N_(m,X)(a,a)≤a≤2X/m. Since μ(a)²≤1,

\[
D(X)\le4X^2\sum_{m=2}^L\frac1m
\ll X^2\log X.
\tag{8}
\]

If R had an upper bound O(X² log^B X), then (4) would give the corresponding averaged square-root bound for V, with logarithmic losses. In the diagonal-only estimate the penalty in (5) is O(X^(3/2) log² X), already of the required order. The missing input is an upper bound for the signed R; absolute values of its summands discard the cancellation.

Positivity Q≥0 is automatic because Q is a sum of squares. It provides a lower bound R≥−D, not the upper bound needed here. Thus merely constructing a positive quadratic form does not settle this cost estimate.

## 5. How much arithmetic strength the energy bound contains

Under RH, the direct Mellin proof in the preceding note gives Q(X)≪_ε X^(2+ε). For m≤sqrt(X)/2 use the cell mean-square bound O(X^(2+ε)/m²), multiply by m, and sum. For the remaining m≤L each cell has O(1) integers, so its aggregate contribution is O(X²).

Conversely, suppose Q(X)≪_ε X^(2+ε) for every ε>0. The m=2 term alone implies

\[
\sum_{X<x\le2X}|M(x/2)-M(x/3)|^2\ll_\varepsilon X^{2+\varepsilon}.
\tag{9}
\]

The exact step-function sum-to-integral identity from the preceding note changes this into the analogous bound for S(y)=M(3y/2)−M(y). Endpoint intervals contribute at most O(X²) by the elementary bound |M(u)|≤u, which is harmless in (9).

For every σ>1/2, dyadic summation of (9) gives

\[
\int_1^\infty|S(y)|^2y^{-2\sigma-1}\,dy<\infty.
\]

Cauchy–Schwarz with a slightly smaller σ shows that the Mellin transform of S converges absolutely and is holomorphic on Re s>1/2. Initially for Re s>1 it equals

\[
\int_0^\infty S(y)y^{-s-1}\,dy
=\frac{(3/2)^s-1}{s\zeta(s)}.
\tag{10}
\]

The numerator is nonzero for Re s>0. Thus holomorphy excludes zeta zeros with real part greater than 1/2; functional-equation symmetry gives RH.

Accordingly the energy estimate itself is RH-equivalent. The decomposition (7) identifies its precise signed arithmetic input, but does not reduce its logical strength below RH. In particular, it cannot be justified by importing reciprocal-zeta bounds that already assume RH.

## 6. Exact small-scale checks

`empirical/connes_route/check_averaged_cell_energy.py` computes (2) and independently expands (7) with integer arithmetic. Its JSON records:

| X | Q | D | positive off-diagonal part | negative off-diagonal part |
|---:|---:|---:|---:|---:|
| 100 | 9,487 | 13,979 | 36,404 | −40,896 |
| 300 | 127,728 | 165,324 | 1,132,776 | −1,170,372 |
| 1,000 | 1,857,588 | 2,333,650 | 43,893,894 | −44,369,956 |

The identities hold exactly. These samples show cancellation between large positive and negative contributions. They do not establish R≤0 in general, a uniform bound for R, or a limiting exponent.

## 7. What this pass establishes

The averaged dual contains no automatic cross-scale consistency. For the explicit Möbius certificate, the diagonal part of its controlling quadratic quantity is bounded unconditionally at the required scale, while all unproved cancellation is isolated in (7).

A direct bound for the original LP might avoid this particular energy criterion by choosing better certificates than the Möbius vector. That remains a live option: bounding Q is sufficient and RH-equivalent, but is not a necessary intermediate step for an LP proof. The outstanding task is still an unconditional averaged or uniform envelope bound. No such bound at square-root scale is proved in this pass.
