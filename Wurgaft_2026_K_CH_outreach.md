# Wurgaft 2026 K^CH Outreach Note

**Subject:** Weekday Hellinger manifold as Fisher pullback; K^CH diagnostic

Dear Wurgaft et al.,

I have been reading "Manifold Steering Reveals the Shared Geometry of Neural
Network Representation and Behavior" through the information geometry of the
categorical simplex.  Your behavior manifold construction is especially clean:
the map \(p\mapsto \sqrt p\) is the positive-sphere presentation of the
Fisher-Rao metric on the open categorical simplex.  In that language, the
reported weekday isometry between activation-manifold geodesic distances and
behavior-manifold Hellinger geodesic distances is direct empirical evidence
that the activation and behavior manifolds are two presentations of the same
Fisher/Hellinger object.

There is a compact curvature diagnostic for the linear-vs-manifold gap.  In
moment coordinates on the simplex, the Amari-Chentsov cubic is

\[
T_p(u,v,w)=\sum_i {u_i v_i w_i\over p_i^2},
\]

and the raised cubic operator is

\[
g_p(K^{CH}_p(u)v,w)=T_p(u,v,w),\qquad
K^{CH}_p(u)v={u v\over p}-g_p(u,v)p.
\]

I use the convention

\[
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)}.
\]

With this sign convention, same-initial-velocity \(m\)-flat endpoint
deviation carries \(-\frac14K^{CH}(h,h)\), while the \(e\)-flat deviation
carries \(+\frac14K^{CH}(h,h)\).

For the seven weekday tokens, \(7\) is prime, so the nontrivial Fisher tangent
space is a single six-dimensional C7 conductor packet.  At the uniform point
\(p_*=(1/7){\bf 1}\),

\[
K^{CH}_{p_*}(h)v=7h*v-7\langle h,v\rangle p_*.
\]

Equivalently, in the additive-character basis
\(\phi_k(x)=7^{-1/2}\exp(2\pi i kx/7)\), with
\(\hat h_r=\langle\phi_r,h\rangle\),

\[
K^{CH}_{p_*}(h)\phi_\ell
=
\sqrt7\sum_{k=1}^6 \hat h_{k-\ell}\phi_k,\qquad \ell\ne0.
\]

Thus the weekday case is the simplest possible test: the full nontrivial
curvature support is one C7 character-convolution operator.

Using a parametric seven-day centroid proxy, the intrinsic behavior-side
calculation already reproduces the text-level linear correlation:

- moment chord vs cyclic Hellinger arc: \(r=0.886448\);
- Hellinger chord vs cyclic Hellinger arc: \(r=0.910010\);
- Fisher/Hellinger manifold reference: \(r\approx0.99\) in your report.

This suggests the immediate quantitative decomposition:

1. compute \(K^{CH}\) on your actual Llama 3.1 8B weekday output centroids;
2. measure how much of the \(0.99\) vs linear gap is intrinsic behavior
   cubic curvature on \(M_y\);
3. attribute the residual to activation-side distortion in the fitted
   pullback \(J_F^\top g_y J_F\) and to spline/parameterization effects.

I can run this directly if you can share the seven weekday behavior centroids
as a \(7\times7\) probability matrix, rows and columns ordered Monday through
Sunday.  If your stored centroids include the `other` bin, either format is
useful: the seven-token normalized matrix gives the pure C7 diagnostic, while
the eight-bin matrix gives the full behavior-simplex diagnostic with the
extra invariant `other` direction separated from the C7 packet.

The local script in my notes now accepts:

```powershell
python empirical/compute_weekdays_K_CH.py --centroids-json weekdays_centroids.json
```

where `weekdays_centroids.json` is either a top-level `7x7` array or
`{"centroids": [...]}`.

Best,

Leonardo
