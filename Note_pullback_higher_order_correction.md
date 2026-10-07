# Note: Pullback Higher-Order Corrections

**Status:** parallel watch note; not blocking Wurgaft outreach.

Wurgaft et al.'s pullback metric

$$
G_F(h)=J_F(h)^\top g_y(F(h))J_F(h)+\epsilon I
$$

is the quadratic term of the behavior-space Fisher geometry pulled back through the activation-to-behavior map \(F:A\to Y\). In local coordinates, it is the order-2 term in the expansion of a behavior-space divergence

$$
D_y(F(h+\delta),F(h)).
$$

The first correction is cubic. If \(F\) is locally affine in the chosen chart, it is simply the pulled-back Amari-Chentsov cubic

$$
F^*K^{CH}_y(u,v,w)
=
K^{CH}_y(J_Fu,J_Fv,J_Fw).
$$

For a genuinely nonlinear \(F\), the same order also contains the covariant Hessian of \(F\), i.e. the second fundamental form of the activation-to-behavior map relative to the chosen behavior-space connection. Thus the clean slogan is:

> \(G_F\) is the leading Fisher pullback; \(F^*K^{CH}\) is the first intrinsic correction; Hessian-\(F\) terms measure non-affineness of the steering map.

Paper 11 then becomes the arity bookkeeping for these corrections. Arity 2 is the metric/pullback level. Arity 3 is the raised Amari-Chentsov cubic \(K^{CH}\), equivalently the \(e/m\) connection-separation term. Arity 4 is where lower contractions and commutator curvature enter; this is the same structural slot as the current \(\Delta^{(4)}\) / \(NC_4\) cumulant work in §9.3.

This is not a contact point to push yet. Wurgaft et al. are using \(G_F\) operationally and are not asking for fourth-order steering corrections. The reason to track it is recognition: if they later measure a systematic residual between behavior-pullback paths and activation-density geodesics, the next object to name is not another metric but the cubic-pulled-back residual, followed by the four-linear \(\Delta^{(4)}\)-type correction.
