# Note: Are the \(K^{CH}\)-Operators Free?

**Date:** May 11, 2026  
**Status:** parallel structural question; not blocking Draft 0.3.1.

## Question

At the centroid \(p_*\), the normalized raised cubic operators satisfy

$$
\overline K^{CH}_{p_*}(\alpha)=M_\alpha
$$

in the full character algebra, followed by the Fisher tangent
augmentation-corner projection.  The arity-4 Mobius probe suggests that
non-crossing partitions \(NC_4\), not the full partition lattice \(\Pi_4\),
govern the lower-contraction formula.

The structural question is:

> Are the operators \(K^{CH}\), viewed against the centroid state on \(H_R\),
> free in the Voiculescu-Speicher sense, with \(\Delta^{(n)}\) given by their
> free cumulants?

## Why This Matters

If the answer is yes, then Theorem 9.3 is not an isolated cancellation
phenomenon.  It becomes a corollary of free probability:

$$
\Delta^{(n)}
=
\kappa_n^{\mathrm{free}}(K^{CH}(x_1),\ldots,K^{CH}(x_n)),
$$

with \(NC_n\) as the natural cumulant poset.

If the answer is no, then the \(NC_n\)-like structure is native to the
Carlitz-Hayes augmentation-corner geometry.  That would be just as important:
it would mean the conductor-depth filtration produces a non-crossing
partition calculus without importing freeness.

## Evidence So Far

For the size-12 TTWW witness

$$
(\tau,\omega,\alpha,\beta,\iota,\rho)=(u,1,u,1,u,u),
$$

with lift

$$
(\tau,\omega,\beta,\iota)=(u,1,1,u),
$$

the tested diagonal gives

$$
\Pi_4=-2,\qquad NC_4=-1,\qquad \text{inherited commutator}=-1.
$$

The discrepancy is exactly the unique crossing partition

$$
\{\tau,\beta\}\mid\{\omega,\iota\}.
$$

For a TTWW size-24 witness, the same pattern occurs:

$$
\Pi_4=-2,\qquad NC_4=-1,\qquad \text{inherited commutator}=-1.
$$

For the minimal TWWW witness found so far, both \(\Pi_4\) and \(NC_4\) give
\(+1\).  That witness is consistent with \(NC_4\), but it is not
discriminating.

## What Would Count as Freeness Here?

One candidate centroid state is the normalized trace on the Fisher tangent
space:

$$
\varphi(A)=\frac{1}{|R|-1}\operatorname{Tr}_{H_R}(A).
$$

But the trace is already known to erase conductor-block data.  A stronger
candidate may be an operator-valued state over the conductor-graded algebra:

$$
E:\operatorname{End}(H_R)\to \operatorname{End}\left(
\bigoplus_{\mathfrak d} \operatorname{span} X_{\mathfrak d}
\right)_{\mathrm{graded}}.
$$

The question then becomes whether the tame and wild pieces are free with
amalgamation over the associated graded conductor algebra.

## Minimal Tests

1. Compute \(\kappa_3\) and \(\kappa_4\) using scalar normalized trace.
   If scalar freeness fails immediately, scalar freeness is not the right
   notion.

2. Compute the same cumulants using conductor-block operator-valued
   expectation.  Check whether mixed tame/wild alternating centered products
   vanish except on the measured noncentral twist support.

3. Compare the \(NC_4\) cumulant support with the seven mixed arity-4 orbits.
   If the supports agree but scalar trace cumulants vanish, the correct
   structure is operator-valued or augmentation-corner-native, not scalar
   free probability.

## Current Posture

Do not use "free" language in Paper 11 yet.  Use "non-crossing cumulant" only
as a provisional internal model for \(\Delta^{(4)}\).  The public paper can
say \(NC_4\) only after either:

- a free-probability state is identified and checked; or
- the Carlitz-Hayes-native cancellation formula is written independently of
  free-probability terminology.

