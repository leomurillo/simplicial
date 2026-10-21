# A conditional repayment theorem and the unresolved forcing step

Status: proved sufficient condition, not a proof of universal repayment or Collatz.

This note continues `Collatz-Direct-Packet-Descent-2026-10-17.md`. It separates the cost of the affine corrections from the unproved assertion that an individual orbit must accumulate enough halving surplus. No independence, mixing, or typical-orbit assumption is used.

## Definitions

Let b_0>1 be an odd packet minimum, so 3 does not divide b_0+1. Along b_{i+1}=Q(b_i), write

\[
b_i+1=2^{M_i}q_i,\quad (q_i,6)=1,\qquad
h_i=v_2(3^{M_i}q_i-1),
\]
\[
z_i=(3^{M_i}q_i-1)/2^{h_i},\qquad
t_i=v_3(z_i+1),\qquad b_{i+1}=B(z_i).
\]

Define the coefficient surplus

\[
S_r=\sum_{i=0}^{r-1}\left[h_i\log2-(M_i-t_i)\log(3/2)\right]
\]

and the affine correction

\[
E_r=\sum_{i=0}^{r-1}
\log\left(1+\frac{2^{h_i}-1}{3^{M_i}q_i}\right).
\]

The exact identity is

\[
\log\frac{b_r+1}{b_0+1}=-S_r+E_r. \tag{1}
\]

## Theorem: a uniform correction budget before first descent

If b_j>=b_0 for every 1<=j<=r, then

\[
S_r\le E_r
<\sum_{i<r}\log\left(1+\frac{1-2^{-h_i}}{b_0}\right)
<r\log(1+1/b_0). \tag{2}
\]

Consequently, if some r>=1 satisfies

\[
S_r\ge r\log(1+1/b_0), \tag{3}
\]

then some b_j with 1<=j<=r lies below b_0. It is enough instead to exceed or equal the middle sum in (2), which is a slightly smaller budget.

### Proof

The packet minimum B(z_i) is at most z_i. Under the no-descent hypothesis,

\[
z_i\ge b_{i+1}\ge b_0.
\]

Since 3^{M_i}q_i=2^{h_i}z_i+1,

\[
0<\frac{2^{h_i}-1}{3^{M_i}q_i}
=\frac{1-2^{-h_i}}{z_i+2^{-h_i}}
<\frac{1-2^{-h_i}}{b_0}<\frac1{b_0}.
\]

Taking logarithms and summing proves the two strict upper bounds for E_r. The hypothesis b_r>=b_0 and (1) imply S_r<=E_r. Thus (3) contradicts no descent through r. This proves the theorem. ∎

No inference is made from coefficient contraction alone: S_r>0 is insufficient without paying E_r.

## Exact arithmetic formulation

Put H_r=sum h_i and D_r=sum(M_i-t_i). Condition (3) is equivalent to

\[
2^{H_r+D_r}b_0^r\ge3^{D_r}(b_0+1)^r. \tag{4}
\]

D_r may be negative. In that case, move the negative powers to the other side before comparing positive integers. Formula (4) is an exact sufficient certificate for descent by time r; it is not a necessary certificate. The sharper budget likewise uses a product of rational numbers and can be checked exactly.

## What would complete this approach

A sufficient additional theorem would be that every packet trajectory starting at b_0>1 has a prefix satisfying (3), or the sharper budget. Another sufficient statement is

\[
\limsup_{r\to\infty}\frac{S_r}{r}>\log(1+1/b_0).
\]

Neither assertion is proved here. They are not consequences of the correction estimate. In fact, the first sufficient assertion, when quantified over all starts, is itself equivalent to Collatz: sufficiency is proved above; conversely, assuming Collatz, Q eventually reaches 1. At 1 one has M=1, h=1, t=0 and hence surplus log(4/3) per step. Every allowed starting minimum b_0>1 satisfies b_0>=3, so its budget is at most log(4/3). For b_0>3 the eventual surplus slope is strictly larger than the budget. For b_0=3, Q(3)=1, and already S_1=log(32/9)>log(4/3). Thus eventual arrival at 1 gives a qualifying prefix. This equivalence must not be presented as a new independent solution.

The explicit expanding family in the previous note has M_i=2, h_i=1, t_i=0 through any prescribed finite number R of packet steps. On that segment,

\[
S_r=r\log(8/9)<0\quad(1\le r\le R).
\]

Its starting integer grows with R. It refutes any fixed waiting-time bound independent of the start, but does not refute eventual repayment for a fixed positive integer.

The unresolved arithmetic issue is control of the joint valuation sequence (M_i,h_i,t_i) across changing expanding patterns. Ending each pattern, bounding its individual duration, or establishing a negative mean in a random model does not prove the deterministic surplus condition. Nor does exact geometric encoding impose that condition by itself.

The actual advance of this note is the uniform, explicit bound (2) on correction cost before descent. The forcing step remains unproved.
