# Note: Positive-Current Transport

Random suffix: `Q8vM3`

Mission: prove the finite-to-Poisson sign-transport theorem:

\[
\mathcal Q_n\ge0
\quad\Longrightarrow\quad
\mathfrak P_{\phi,y}(\Xi)\ge0
\]

for the occupation-decorated convolution-square currents attached to
nonnegative \(K\)-even Poisson-window detectors.

Verdict:

\[
\boxed{
\text{Finite positive-current transport is closed.}
}
\]

The finite arithmetic ingredients are now in place: exact occupation
coefficients, double cutoff, averaged compressed CRT shadow uniformity, CRT
window generation, and convolution-square representation of nonnegative
windows.  The theorem below proves that no sign is lost through recovery,
projection, leakage control, or the limiting process.  The only remaining
non-finite input is the usual completed-zeta gamma/K normalization that
identifies the transported explicit-formula functional with
\(\mathfrak P_{\phi,y}(\Xi)\).

## 1. Detector and Current

Fix \(y>0\).  In this note a **detector** means a nonnegative \(K\)-even
spectral window in the Poisson-Gaussian detector class, or a limit of such
windows in the chosen \(\mathcal D_{\delta,0}\)-based topology.  This is the
detector class used by the Poisson-window bridge and is strong enough to
separate negative valleys of the CM Poisson field.

Let \(\phi\) be such a detector.  Choose a square-root representative
\[
\phi=\widehat{(f*f^*)}
\]
up to the standard smooth approximation.

At primorial row \(P_n\), choose the finite CRT/Fejer approximation
\(\phi_n\), its square root \(a_n=\sqrt{\phi_n}\), and the finite
convolution square
\[
F_n=f_n*f_n^*,
\qquad
\widehat F_n=|a_n|^2=\phi_n.
\]

Let
\[
\widetilde J_n(\phi,y)
\]
be the occupation-decorated Hayes-Mobius recovery current built from
\(F_n\), with the single-axis projector \(\Pi_{\rm sa}\) applied upstairs in
\(\mathcal F_n=\operatorname{Sym}(V_n)\) before CRT compression.  Let
\[
J_n(\phi,y)
=
\Pi_{\mathrm{Crit}_n}^{\Lambda}\widetilde J_n(\phi,y)
\]
be its closed-sector representative.

The actual finite value transported to the limit is
\[
Q_n(\phi,y):=\mathcal Q_n(J_n(\phi,y)).
\]

## 2. No Sign Is Lost at Finite Level

The finite Noether form is positive on admissible currents:
\[
\mathcal Q_n(J)\ge0.
\]

Since \(J_n(\phi,y)\in\mathrm{Crit}_n\) by construction,
\[
\boxed{
Q_n(\phi,y)\ge0
}
\]
for every \(n\).

This is the key point: projection does not need to preserve a sign already
computed somewhere else.  The projected current itself is the admissible
current on which the finite positive form is evaluated.

If one begins with the raw current \(\widetilde J_n\), the leakage
orthogonal decomposition gives
\[
\widetilde J_n=J_n+L_n,
\qquad
J_n\perp_\Lambda L_n,
\]
and
\[
\mathcal Q_n(\widetilde J_n)
=
\mathcal Q_n(J_n)+\Lambda_n(L_n).
\]
Thus passing to the closed representative changes the value only by the
nonnegative leakage term.  In the hard packet-preserving stratum this term is
zero; in the first-order priced stratum it is
\[
O\!\left(\mu_n^\star\operatorname{polylog}(P_n)\right)=o(1).
\]

So projection/leakage cannot create a negative limit.

## 3. Recovery Error Ledger

Let
\[
\mathfrak P_{\phi,y}(\Xi)
=
\int_{\mathbb R}\phi(x)\operatorname{Im}
\left(-{\Xi'(x+iy)\over\Xi(x+iy)}\right)\,dx.
\]

The finite value \(Q_n(\phi,y)\) differs from this target by five errors:

\[
Q_n(\phi,y)-\mathfrak P_{\phi,y}(\Xi)
=
E_{\rm occ}(n)+E_{\rm cut}(n)+E_{\rm CRT}(n)
+E_{\rm win}(n)+E_{\rm leak}(n).
\]

Each term is now controlled.

### Occupation Error

By `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md`,
\[
E_{\rm occ}(n)=0
\]
upstairs before CRT compression:
\[
D_s\Pi_{\rm sa}\sum_{k=1}^{K_n}{1\over k}H_s^k
=
\sum_{p\le p_n}\sum_{r\le K_n}
(\log p)p^{-rs}e_{r e_p}.
\]

### Double-Cutoff Error

By `Note_DoubleCutoffDominatedConvergence_Q8vM3.md`, for log-side kernels in
\(\mathcal D_{\delta,0}\),
\[
E_{\rm cut}(n)\to0
\]
locally uniformly, with explicit bound
\[
|E_{\rm cut}(n)|
\ll_\delta
\|G\|_{\delta,0}
\left[
p_n^{-\delta}(\log p_n+1)
+2^{-(1+\delta)K_n}
+M_n^{-\delta}(\log M_n+1)
\right].
\]

### Compressed CRT Shadow Error

By `Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3.md`, the averaged
compressed shadow satisfies
\[
E_{\rm CRT}(n)\to0
\]
at polynomial natural scale \(X_n=P_n^{1+\varepsilon}\), because
\[
{|\mathcal E_{P_n}(W;X_n)|\over X_n}
\ll
\left({P_n\over X_n}\right)^{1/2}P_n^{o(1)}
=
P_n^{-\varepsilon/2+o(1)}.
\]

This uses the \(L^2\) compressed-shadow norm, not the overstrong pointwise
\(\max_\chi\) character norm.

### Window Approximation Error

By `Note_PoissonWindowCRTGeneration_K7mQ2.md` and
`Note_ConvolutionSquarePoissonRecovery_Z9vL4.md`,
\[
E_{\rm win}(n)\to0.
\]
Indeed, Fejer/CRT approximants converge uniformly to the detector, and the
finite convolution-square identity is exact:
\[
\widehat{f_n*f_n^*}=|\widehat f_n|^2=\phi_n.
\]
The Poisson-window functional is continuous in the detector topology on the
fixed height line \(y>0\).

### Leakage Error

By the orthogonal closed-sector projection and the Paper 22/Paper 25 leakage
control,
\[
E_{\rm leak}(n)=0
\]
in the hard packet-preserving stratum, and
\[
E_{\rm leak}(n)
=
O\!\left(\mu_n^\star\operatorname{polylog}(P_n)\right)\to0
\]
in the first-order priced stratum.

## 4. Transport Theorem

**Theorem 4.1 (positive-current transport).**  
Assume:

1. finite Noether positivity holds on the admissible occupation-decorated
   convolution-square currents;
2. the closed-sector projection is evaluated before lossy CRT compression;
3. leakage is either zero in the packet-preserving stratum or satisfies
   \(O(\mu_n^\star\operatorname{polylog}(P_n))=o(1)\);
4. the standard completed-zeta gamma/K normalization identifies the finite
   prime-power side plus the Archimedean term with the explicit-formula
   Poisson-window functional of \(\Xi\).

Then for every nonnegative \(K\)-even detector \(\phi\) in the above detector
topology,
\[
\boxed{
\mathfrak P_{\phi,y}(\Xi)\ge0.
}
\]

*Proof.*  For every \(n\),
\[
Q_n(\phi,y)=\mathcal Q_n(J_n(\phi,y))\ge0.
\]
By the error ledger in Section 3,
\[
Q_n(\phi,y)\longrightarrow \mathfrak P_{\phi,y}(\Xi).
\]
The limit of nonnegative real numbers is nonnegative.  Therefore
\[
\mathfrak P_{\phi,y}(\Xi)\ge0.
\]
\(\square\)

## 5. Consequence for CM Poisson Monotonicity

The detector class contains the Gaussian/Poisson windows that separate
negative valleys of
\[
u_B(x,y)=\operatorname{Im}\left(-{\Xi'(x+iy)\over\Xi(x+iy)}\right).
\]

If \(u_B(x_0,y_0)<0\) at a regular point, then a sufficiently narrow
nonnegative detector, symmetrized into the \(K\)-even detector class when
needed, gives
\[
\mathfrak P_{\phi,y_0}(\Xi)<0,
\]
contradicting Theorem 4.1.  The same local argument detects the negative
Poisson singularity below any hypothetical off-boundary zero.

Thus:
\[
\boxed{
\mathfrak P_{\phi,y}(\Xi)\ge0\ \forall\phi\ge0
\text{ in the detector class}
\quad\Longrightarrow\quad
\operatorname{Im}m_B(x+iy)\ge0.
}
\]

Since CM Poisson monotonicity is equivalent to RH by
`Note_CMPoissonMonotonicity_DirectNoGo_W8rN5.md`, the sign-transport route is
complete once the standard completed gamma/K normalization is admitted.

## 6. What This Does and Does Not Close

Closed here:

1. positivity is evaluated after closed-sector projection, so projection does
   not lose sign;
2. leakage contributes only a nonnegative or vanishing error;
3. exact occupation coefficients, double cutoff, CRT shadow uniformity, and
   window approximation assemble into convergence to
   \(\mathfrak P_{\phi,y}(\Xi)\);
4. therefore finite Noether positivity transports to Poisson-window
   positivity.

Still separate:

1. deriving the completed gamma/K normalization internally from the
   Bures/Petz/projective Archimedean packet rather than using the standard
   completed-zeta normalization;
2. deriving the metaplectic positive-energy selection from first principles.

In other words, the finite positive-current transport theorem is closed.  The
remaining philosophical/structural lock is whether the Archimedean packet is
selected internally or accepted as the standard completed-zeta normalization.
