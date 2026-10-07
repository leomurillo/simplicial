# Paper 2 Citation Patch: Wurgaft et al. 2026

**Implementation status:** Folded into `paper2_draft.md` in May 2026.  The
patch file remains as provenance for the placement decisions and sign
convention warning.

**Target paper:** Daniel Wurgaft, Can Rager, Matthew Kowal, Vasudev Shyam, Sheridan Feucht, Usha Bhalla, Tal Haklay, Eric Bigelow, Raphael Sarfati, Thomas McGrath, Owen Lewis, Jack Merullo, Noah D. Goodman, Thomas Fel, Atticus Geiger, Ekdeep Singh Lubana. "Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior." arXiv:2605.05115v1, May 6, 2026.

## Citation Location 1: Introduction, After Native-Coordinate Claim

**Place after:** `paper2_draft.md` §1.1, immediately after the paragraph ending "making explicit a gauge structure that the usual reference-fixed presentation tends to hide."

**Patch paragraph:**

Recent empirical work on LLM representation geometry gives an external anchor for this coordinate claim. Wurgaft et al. fit paired manifolds in activation space and output-probability space for cyclic and sequential concept tasks, and find that geodesic distances on the activation manifold are nearly isometric to geodesic distances on the behavior manifold: for weekdays, the reported manifold correlation is \(r \approx 0.99\), while linear activation distances correlate more weakly with behavior-manifold distance. Their behavior manifold is built by aggregating probability mass over concept tokens and embedding the resulting categorical distributions by the Hellinger map \(p\mapsto \sqrt p\). Since this square-root map is the sphere pullback presentation of the Fisher-Rao metric, their \(r\approx 0.99\) result is an empirical confirmation of the present paper's native-coordinate/Fisher-Hellinger thesis: the behavioral object is not an arbitrary Euclidean cloud but the categorical simplex in its Fisher/Hellinger geometry, with the cyclic concept structure living in the zero-sum quotient \(H=\mathbb R^N/\langle 1\rangle\). The point is not that their paper proves the simplicial-coordinate thesis; rather, it supplies a clean neural-network phenomenology in which the thesis is the natural structural explanation.

## Citation Location 2: Sphere Pullback / Hellinger Coordinates

**Place after:** `paper2_draft.md` §3.2, after Proposition 3.1 or before Remark 3.5.

**Patch paragraph:**

This also clarifies a coordinate choice that appears in recent manifold-steering experiments. Wurgaft et al. use the square-root embedding \(p\mapsto \sqrt p\) to fit behavior manifolds in Hellinger geometry, then compare activation-manifold arc length with behavior-manifold arc length. Proposition 3.1 says exactly what this choice is: the positive orthant of the unit sphere pulls back to the Fisher-Rao metric on the open categorical simplex. It is therefore one admissible coordinate realization of the same object that the \(m\)- and \(e\)-flat coordinates present dually. Their cubic-spline curves should be read accordingly: depending on whether the interpolation parameter is treated as a probability/moment coordinate, a logit/natural coordinate, or a spherical Hellinger coordinate, the fitted path is approximating an \(m\)-flat, \(e\)-flat, or Fisher-Rao geodesic surrogate. The empirical fact that the Hellinger behavior manifold matches activation geometry is thus not a competing construction; it is a measured instance of the simplex geometry developed here.

## Citation Location 3: Pullback Through a Parameterized Map

**Place after:** `paper2_draft.md` §6.3, after the sentence "Away from initialization, this interpretation requires correction by the Amari-Chentsov curvature of the statistical manifold under the chosen connection, which we do not develop here." If §8.1 is expanded, the same paragraph can instead open §8.1.

**Patch paragraph:**

Wurgaft et al.'s pullback metric makes this "away from initialization" correction operational. They define a behavior map \(F:A\to Y\) from activations to output distributions and use the activation-space metric \(G_F(h)=J_F(h)^\top g_y(F(h))J_F(h)+\epsilon I\), where \(g_y\) is the behavior-space Hellinger/Fisher metric. In the notation of this paper, \(G_F\) is the leading quadratic Fisher pullback through the parameterized map \(F\). The next local term is governed by the Amari-Chentsov cubic pulled back along \(F\), together with the covariant Hessian of \(F\) when \(F\) is not locally affine. This is precisely the regime in which the centroid theorem stops being a mere initialization statement: at \(p_*\), the \(e\)- and \(m\)-webs, the Fisher metric, and the simplicial inner product coincide up to scale; off the centroid, their separation is predicted by the dually flat structure. Wurgaft et al.'s measured recovery of activation-manifold paths from behavior-manifold targets is therefore the experimental counterpart of the Fisher pullback story, not a surprise under it.

This gives a concrete name to the first nonlinear correction behind their linear-versus-manifold improvement. In the Paper 11 convention,
\[
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)},\qquad
g(K^{CH}(u)v,w)=T(u,v,w),
\]
so \(K^{CH}\) is the explicit cubic curvature operator measuring the separation between \(m\)-flat, \(e\)-flat, and Fisher/Hellinger-geodesic behavior. If an earlier table used the opposite \(e/m\) convention, the magnitudes remain valid but the displayed signs must be flipped.

## Converse Direction to State Explicitly

Add one sentence either at the end of §8.1 or in the conclusion:

The phenomenon measured by Wurgaft et al. should be expected from the dually flat categorical structure: if a model's activation map \(F:A\to\Delta_N^\circ\) is approximately a Riemannian quasi-isometry on a concept region, then Hellinger/Fisher geodesics in behavior space and density geodesics in activation space must agree to leading order, with the first systematic discrepancy controlled by the pulled-back Amari-Chentsov cubic \(K^{CH}\).

## Reference Entry

Add to references:

`[Wurgaft et al. 2026] Wurgaft, D., Rager, C., Kowal, M., Shyam, V., Feucht, S., Bhalla, U., Haklay, T., Bigelow, E., Sarfati, R., McGrath, T., Lewis, O., Merullo, J., Goodman, N. D., Fel, T., Geiger, A., and Lubana, E. S. "Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior." arXiv:2605.05115v1, 2026.`

## Reviewer-Visible Framing

The citation should be framed as empirical anchoring, not priority competition. Paper 2 supplies the coordinate theorem-language: \(H\), \(p_*\), \(e/m\) dual flatness, Fisher/Hellinger pullback, and \(K^{CH}\). Wurgaft et al. supply a clean measured case on real networks: cyclic weekdays/months and graph-structured in-context learning manifolds. A returning reviewer should see the two as the same object seen from opposite directions: Paper 2 from statistical geometry to neural phenomenology, Wurgaft et al. from neural phenomenology back to statistical geometry.
