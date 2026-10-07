# Wurgaft/Rosas Cross-Paper Problem Map

**Date:** May 2026

This note records what the Wurgaft and Rosas bridges open inside Papers 2,
9, 10, and 11, after the Paper 2 citation patch was folded into the draft.

## Paper 2

**Action landed.**  Paper 2 now cites Wurgaft et al. as empirical anchoring
for the native-coordinate claim: their Hellinger behavior manifold is the
sphere-pullback presentation of Fisher-Rao geometry on the categorical
simplex.

**New question.**  Can the "beyond the uniform" section be made quantitative
by writing the second-order separation between linear/simplex-flat paths and
Hellinger/Fisher geodesics directly in terms of

$$
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)}?
$$

**Named open hook.**  Section 8.2 now isolates prime cyclic behavior
manifolds, especially \(C_7\), as the minimal empirical test.

## Paper 9

**Action landed.**  Problem 9.7 now names the prime cyclic Fisher-cubic
benchmark.

**New question.**  In a prime cyclic simplex \(C_\ell\), the nontrivial
Fisher tangent space is one conductor packet.  Does the closed character-basis
matrix for \(K^{CH}\) explain the full behavior-side linear-vs-manifold gap,
or only the portion intrinsic to \(M_y\)?

**Why this matters.**  This is the control case for the conductor-block
program: there are no mixed conductor packets and no local Ext obstruction.
Any leftover empirical gap must be activation-side distortion or an output
direction outside the pure \(C_\ell\) simplex, such as an `other` bin.

## Paper 10

**Action landed.**  Problem 10.2 now names the empirical Fisher-pullback
decomposition.

**New question.**  Given an activation-to-behavior map
\(F:A\to\Delta_R^\circ\), decompose a measured steering gap into:

1. intrinsic behavior cubic \(K^{CH}\);
2. activation-side distortion of \(J_F^\top g_yJ_F\);
3. spline, sampling, or non-quotient output residuals.

**Why this matters.**  Problem 10.1 gives the abstract Fisher-conductor
coupling tensor.  Problem 10.2 turns it into an empirical protocol.

## Paper 11

**Action landed.**  Problem 11.7 now names the empirical input-side lift of
\(K^{CH}\).

**New question.**  Can the input-side pullback residual of a real model be
matched to the quotient-character hyper-adjacency support theorem?

**Control and positive tests.**

- \(C_7\) weekdays are the no-\(\operatorname{Ext}_{CH}\) control: one
  conductor packet, no tame/wild split, pure character convolution.
- \(C_{12}\) months are the CRT mixed-conductor control:
  \(C_{12}\cong C_4\times C_3\), with \(2\)-primary conductor depths
  \(1,2,4\) paired with a tame \(3\)-factor.  This tests product conductor
  structure before the local finite-field row.
- Mixed local rows such as \({\mathbb F}_4[u]/(u^2)\) are the positive tests:
  the residual should land on the mixed TTWW/TWWW support selected by the
  \(592\)-orbit arity-4 theorem.

## Rosas Bridge

The Rosas note supplies the language of informationally closed macrovariables.
Inside this program, the conductor lattice is the quotient-statistic tower,
and the Carlitz-Hayes normalizer plus \(\operatorname{Ext}_{CH}\) filtration
measure when closure at the visible conductor level is not the whole story.

**Action landed.**  Papers 9-11 now frame conductor packets not only as
spectral blocks, but as closed information layers whose off-centroid failure
is measured by \(K^{CH}\) and the local filtered adjacency algebra.

**New problem hooks.**

- Paper 9, Problem 9.8: conductor macrovariable closure taxonomy.
- Paper 10, Problem 10.3: macrovariable closure audit.
- Paper 11, Problem 11.8: Rosas closure audit for
  \(\operatorname{Ext}_{CH}\).

**Closure ladder.**  The program now distinguishes partition closure,
sufficient-statistic closure, normalizer closure, and filtered
adjacency-algebra closure.  These are deliberately not the same assertion.

**Ext interpretation.**  \(\operatorname{Ext}_{CH}\) is now explicitly framed
as a macrovariable-closure obstruction: it measures when a conductor quotient
is closed as a visible information layer but does not split the full
off-centroid Fisher coupling algebra.

## Empirical Control Lane

The weekday script is ready for real data:

```powershell
python empirical/compute_weekdays_K_CH.py --centroids-json weekdays_centroids.json
```

What remains missing is the empirical Llama 3.1 8B weekday behavior-centroid
matrix.  A seven-token \(7\times7\) matrix gives the pure \(C_7\) diagnostic.
An eight-bin matrix including `other` would support the richer test separating
the cyclic packet from the extra output direction.

The month script is now also ready for real data:

```powershell
python empirical/build_cyclic_centroids_from_dump.py --preset months --per-class-safetensors path/to/per_class_output_dists.safetensors
python empirical/compute_cyclic_K_CH.py --preset months --centroids-json empirical/data/months_llama31_8b_centroids_12bin.json
```

The expected upstream artifact, by analogy with the weekday path, is
`artifacts/natural_domains_arithmetic/llama31_8b/months/baseline/per_class_output_dists.safetensors`.
That path is an inference until checked against a real Causalab run.

No empirical tensor is needed for the parallel theory task.  The new
`empirical/coefficient_rank_profile.py` runner computes the \(C_4\times C_3\)
coefficient rank profile through \(n=4\), showing the difference between
support-pattern spread and genuine tensor impurity inside a CRT corner.

This is no longer a program blocker.  It is a control and translation lane.
The exact finite quotient program is already alive in Paper 11: the measured
\({\mathbb F}_4[u]/(u^2)\) row shows that the associated graded closes too
early, while the filtered quotient-character adjacency algebra retains the
mixed tame/wild extension data.

If the weekday or month centroids arrive, run the appropriate control.  If
they do not, continue the finite arithmetic census and canonicalization
program.
