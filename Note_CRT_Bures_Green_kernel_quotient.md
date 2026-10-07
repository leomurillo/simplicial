# CRT/Bures Green-Kernel Quotient

## Status

This note records the exact theorem needed for the Newtonian recovery step.
The theorem is conditional on a spectral/Dirichlet convergence hypothesis.  That
hypothesis is not cosmetic: without it, a bare CRT projective system can
converge to a profinite, adelic, toral, or anisotropic limit, and its Green
kernel need not be \(1/r\).  The inverse-square law is recovered only if the
residual-zero quotient of the Bures Dirichlet forms has three-dimensional
Euclidean principal symbol.

All no-go statements derived from this theorem are no-go statements for
reversible, detailed-balance CRT/Bures generators unless explicitly upgraded.
For a non-self-adjoint Markov generator the resolvent can be defined without a
symmetric Dirichlet form, and its Green kernel need not be controlled only by
\(\Gamma_{\mathcal L}\).  The coherent non-equilibrium route is therefore not
closed by any diagonal carre-du-champ computation below.  The corrected status
is:

1. The leg-local dissipative route is closed by the pinned fourth-moment
   certificates.
2. The diagonal-shadow off-diagonal audit is an identity check, not a
   coherent-sector no-go.
3. The first non-reversible quantum resolvent computation has now been built
   on \(Z_{30}\).  It gives a finite positive signal for the coherent route,
   but not yet a refinement theorem.

## Finite Bures Dirichlet Data

Let
\[
  R_n=\mathbb Z/P_n\mathbb Z,\qquad P_n=p_n\#,
\]
or another conductor-compatible CRT row, and let
\[
  \mathcal H_n=\mathbb C[R_n],\qquad
  \mathcal D_n=\mathcal D^\circ(\mathcal H_n)
\]
carry the Bures-Helstrom metric \(g^B_n\).  Fix a faithful reference state
\(\rho_{n,*}\), usually the maximally mixed state or a mass-participating
equilibrium state.  Let \(\mathcal L_n\) be a reversible, conductor-compatible
quantum Markov generator on observables, with carre-du-champ form
\[
  \mathcal E^B_n(A,B)
  =
  \langle A,-\mathcal L_n B\rangle_{B,\rho_{n,*}}.
\]
On the commuting diagonal quotient this reduces to the classical conductance
form
\[
  \mathcal E_n(f,g)
  =
  {1\over2}\sum_{x,y\in R_n} c_n(x,y)
  (f(x)-f(y))(g(x)-g(y)),
\]
where the conductances \(c_n(x,y)\) are the diagonal shadow of the Bures
reversible generator.

Let \(\xi_n:R_n\to M\) be the declared physical/shape quotient map into a
three-dimensional interior manifold \(M\), or into a local chart of that
manifold.  Let \(\nu_n=(\xi_n)_*\rho_{n,*}\) be the pushed measure.  The
residual-zero quotient identifies finite observables \(f_n\) and \(g_n\) when
\[
  \|f_n-g_n\|_{L^2(\nu_n)}^2+\mathcal E_n(f_n-g_n)\to0.
\]

## Euclidean Principal-Symbol Gate

The CRT/Bures tower has a Newtonian Green quotient if and only if the quotient
forms converge to the three-dimensional Laplace Dirichlet form
\[
  \mathcal E_\infty(f,g)
  =
  \int_M \langle \nabla f,\nabla g\rangle_{g_{\rm phys}}\,d{\rm vol}_{g_{\rm phys}}
\]
in the sense of Mosco convergence, with local Euclidean principal symbol.  In
coordinates this means that for every smooth compactly supported test function,
the diagonal generator satisfies
\[
  \mathcal L_n(f\circ\xi_n)(x)
  \longrightarrow
  \Delta_{g_{\rm phys}} f(\xi_n(x)),
\]
and locally the first two jump moments obey
\[
  \sum_y c_n(x,y)(\xi_n(y)-\xi_n(x))=o(1),
\]
\[
  \sum_y c_n(x,y)(\xi_n(y)-\xi_n(x))
       (\xi_n(y)-\xi_n(x))^T
  \longrightarrow 2\,g_{\rm phys}^{-1},
\]
with fourth moments tending to zero fast enough to remove nonlocal tails.

This is the real physics gate.  It cannot be replaced by a sign test.

## Theorem: Green-Kernel Quotient

Assume:

1. The Bures forms \(\mathcal E^B_n\) are compatible with the CRT projective
   maps by CPTP coarse graining, and equality holds on the residual-zero
   quotient up to errors \(\epsilon_n\to0\).
2. Their diagonal quotient forms \(\mathcal E_n\) Mosco-converge to
   \(\mathcal E_\infty\) on a three-dimensional Riemannian manifold \(M\).
3. The associated heat kernels satisfy the local Gaussian bounds and local
   central-limit asymptotic of the Laplace-Beltrami heat kernel.
4. The quotient is taken away from collision diagonals, then extended to point
   sources by the usual capacity/renormalization limit.

Then the resolvents converge:
\[
  (\lambda-\mathcal L_n)^{-1}
  \longrightarrow
  (\lambda-\Delta_{g_{\rm phys}})^{-1}
\]
strongly on the residual-zero quotient for every \(\lambda>0\).  If \(M\) is
locally Euclidean at the scale of the source separation, the massless Green
kernels converge off the diagonal to
\[
  G(x,y)= {1\over4\pi\,d_{g_{\rm phys}}(x,y)}.
\]

### Proof

Mosco convergence of closed Dirichlet forms is equivalent to strong resolvent
convergence of the associated self-adjoint generators.  Therefore assumption
2 gives
\[
  (\lambda-\mathcal L_n)^{-1}F_n
  \to
  (\lambda-\Delta_{g_{\rm phys}})^{-1}F
\]
whenever \(F_n\to F\) in the residual-zero quotient.  Assumption 1 ensures that
the Bures lift and the diagonal quotient have the same limiting closed form
on the observables visible in the physical quotient; off-diagonal coherences
may affect recovery, but they leave no residual energy in the quotient.

Strong resolvent convergence gives semigroup convergence.  Assumption 3
upgrades this to heat-kernel convergence off the diagonal:
\[
  p_n(t;x_n,y_n)\to p_M(t;x,y).
\]
The Green kernel is the time integral of the heat kernel:
\[
  G_M(x,y)=\int_0^\infty p_M(t;x,y)\,dt.
\]
In a three-dimensional Euclidean chart,
\[
  p_M(t;x,y)
  \sim
  (4\pi t)^{-3/2}\exp\!\left(-{|x-y|^2\over4t}\right).
\]
Hence
\[
  \int_0^\infty
  (4\pi t)^{-3/2}\exp\!\left(-{r^2\over4t}\right)\,dt
  =
  {1\over4\pi r}.
\]
Uniform Gaussian bounds justify dominated convergence away from the collision
diagonal, and assumption 4 supplies the standard point-source extension.  Thus
the residual-zero quotient Green kernel is \(1/(4\pi r)\).  This proves the
claim.

## Corollary: Newtonian Pair Law

For point masses \(m_i\) represented by convergent quotient source sequences,
define the limiting pair potential by the Green quotient:
\[
  V(q)
  =
  -4\pi G
  \sum_{i<j}m_i m_j\,G(q_i,q_j).
\]
Using the theorem,
\[
  V(q)
  =
  -G\sum_{i<j}{m_i m_j\over r_{ij}}.
\]
Therefore
\[
  -\nabla_{q_i}V
  =
  \sum_{j\ne i}Gm_i m_j{q_j-q_i\over r_{ij}^3},
\]
which is the Newtonian inverse-square force.  In the Jacobi-Maupertuis metric
\[
  g_{\rm JM}=2(E-V)\,g_{\rm kin},
\]
the corresponding geodesic spray is Newtonian motion after the standard
Maupertuis time reparametrization.

Thus inverse-square gravity is recovered exactly when the CRT/Bures
residual-zero quotient has the three-dimensional Laplace Green kernel.

## Necessary Falsifier

The theorem also gives a sharp no-go test.  Let \(N_n(\Lambda)\) be the
eigenvalue counting function of the quotient generator.  A Newtonian quotient
requires Weyl scaling
\[
  N_n(\Lambda)\to C\,\Lambda^{3/2}
\]
on the physical quotient.  Equivalently, the heat trace must satisfy
\[
  {\rm Tr}\,e^{t\mathcal L}\sim C'\,t^{-3/2}.
\]
If the quotient has spectral dimension \(d_s\ne3\), then the Green singularity
is \(r^{2-d_s}\) for \(d_s\ne2\), logarithmic for \(d_s=2\), and not
Newtonian.  No choice of \(\lambda_{E5}\), Heron gate, or body-participation
multiplier can repair that.  The missing proof is therefore exactly the proof
that the conductor-compatible Bures Dirichlet quotient has spectral dimension
three and Euclidean isotropic principal symbol.

## First Finite Linearization Audit

The first computable gate is the principal-symbol anisotropy of the pushed
second jump moment.  For a finite quotient map
\(\xi_n:R_n\to\mathbb R^3\), define
\[
  M_n
  =
  \mathbb E_x\sum_y c_n(x,y)
  (\xi_n(y)-\xi_n(x))(\xi_n(y)-\xi_n(x))^T
\]
and
\[
  \mathcal A_n
  =
  {\lambda_{\max}(M_n)-\lambda_{\min}(M_n)\over
   \lambda_{\max}(M_n)+\lambda_{\min}(M_n)}.
\]

The finite audit in
`empirical/bures_isotropization_linear_audit.py` tests:

1. diagonal-only CRT leg cycles;
2. SLD-normalized leg-local Bures coherences, modeled by the complete
   matrix-unit graph on each CRT tensor leg;
3. an all-pairs complete graph as a non-CRT-local control.

With the conductor-compatible quotient columns
\[
  Z_6:\quad (p2:h1,\;p3:h1,\;p3:h2),
\]
and
\[
  Z_{30}:\quad (p2:h1,\;p3:h1,\;p5:h1),
\]
the measured anisotropies are:

| row | diagonal \(\mathcal A_n\) | Bures \(\mathcal A_n\) |
|---:|---:|---:|
| \(6\) | \(2.000000\times 10^{-1}\) | \(1.110223\times 10^{-16}\) |
| \(30\) | \(2.000000\times 10^{-1}\) | \(4.996004\times 10^{-16}\) |

This discharges the finite second-symbol gate for the declared SLD-normalized
leg-local model: Bures kills the CRT-sector anisotropy that remains visible in
the diagonal conductance tower.

The same audit also resolves the complete-leg locality question negatively.
It reports normalized fourth jump moments
\[
  q_4={\mathbb E_x\sum_y c_n(x,y)\|\delta\xi\|^4\over (\operatorname{tr}M_n)^2}
\]
of \(8.888889\times10^{-1}\) on \(Z_6\) and \(7.777778\times10^{-1}\) on
\(Z_{30}\).  Rerunning the same complete-leg model through the primorial tower
\[
  Z_6,\;Z_{30},\;Z_{210},\;Z_{2310},\;Z_{30030}
\]
keeps the prime-first value pinned at \(7.777778\times10^{-1}=7/9\).  The
sector-fill quotient similarly stays pinned at \(8/9\).  Thus the complete-leg
SLD-Bures model is settled:

\[
  M_n^{\rm Bures}=2I_3
  \quad\text{but}\quad
  q_{4,n}^{\rm Bures}\not\to0.
\]

This is a theorem-level finite obstruction for that model, not a pending
numerical trend.  Complete leg coherences isotropize by mean-field averaging
over each CRT fiber, and that same mean-field completeness prevents jump
localization.  Isotropy-by-completeness and Mosco locality are mutually
exclusive for this construction.

## Leg-Local No-Go

The banded interpolation problem is now resolved negatively for the
CRT-leg-local family encoded by the audit.

**Proposition (leg-local no-go, finite-certified).**  For the
conductor-compatible CRT-leg-local reversible Bures generators generated by
cyclic bands and matrix-unit leg coherences, the isotropic limit is the
mean-field complete graph on each active leg.  That limit has a normalized
fourth jump moment bounded away from zero.  Hence no generator in this
CRT-leg-local family yields the local Laplace Dirichlet form.

The finite certificate is:

1. `bures_isotropization_banded_largest_prime_modes`: three low Fourier modes
   on the largest prime leg.  The isotropic complete-leg value is
   \(q_4=49/36\).
2. `bures_isotropization_banded_largest_primes`: one low Fourier mode on each
   of the three largest prime legs.  The isotropic complete-leg value is
   \(q_4=3/4\).
3. The original prime-first and sector-fill quotients pin at \(7/9\) and
   \(8/9\), respectively.

Across \(Z_{30}\), \(Z_{210}\), \(Z_{2310}\), and \(Z_{30030}\), the simple
uniform positive bands tested so far show the expected tradeoff: narrow bands
have nonzero anisotropy, while bands wide enough to isotropize fall back to the
complete-model \(q_4\) floor.  The obstruction is conceptual: leg-locality is
locality in the source CRT product, while Mosco convergence to
\(\Delta_{g_{\rm phys}}\) requires locality after pushforward to the target
\(\xi_n(R_n)\subset\mathbb R^3\).  Widening a leg band restores leg symmetry,
but only by becoming mean-field on that leg.

## Target-Local Bures Realizability

The remaining bridge is therefore:

**Target-local Bures realizability problem.**  Does there exist a
CPTP-compatible, conductor-compatible reversible Bures generator on the CRT
tower whose diagonal carre-du-champ shadow is asymptotic to a target-local
kernel
\[
  c_n(x,y)
  =
  \mathbf 1\{\|\xi_n(x)-\xi_n(y)\|\le h_n\},
  \qquad
  h_n\to0,
\]
or to a smooth compactly supported variant of this kernel?

The audit now includes `--target-local`.  This is a diagonal-shadow diagnostic,
not a full CPTP feasibility test.  It measures:

1. the target-local symbol and fourth moment;
2. the support residual against the generous matrix-unit cone, where any
   single-leg edge may vary independently;
3. the class-cone residual against the stricter conductor-compatible cone,
   where weights are tied by leg and cyclic distance.

For the residue-grid quotient on the three largest prime legs, the target-local
kernel at \(Z_{2310}\) with `--target-h-scale 8` has
\[
  \mathcal A=5.294703\times10^{-3},
  \qquad
  q_4=5.083107\times10^{-3},
\]
but the Bures class-cone residual is
\[
  \rho_{\rm class}=9.767551\times10^{-1}.
\]
At \(Z_{30030}\), with the same residue-grid target and radius scale, the
target-local support residual is already
\[
  \rho_{\rm support}=9.933233\times10^{-1},
  \qquad
  \rho_{\rm class}=9.937966\times10^{-1}.
\]

These residuals should not be misread as distance to the full CPTP/Bures cone.
They are distances to leg-matrix-unit diagonal-shadow cones.  Thus the large
values above restate, in target-local form, that source-leg matrix units cannot
span the target-local kernel.  They do not by themselves disprove the existence
of a CRT-entangling Bures lift whose diagonal residual-zero shadow is
target-local.

## Honest Off-Diagonal Generator Check

The next audit, `empirical/bures_offdiagonal_generator_audit.py`, instantiates
an actual off-diagonal Hermitian generator.  Let
\[
  X_\mu=\operatorname{diag}(\xi^\mu)
\]
be diagonal physical coordinate observables and let \(H=H^*\) be supported on
target-local pairs.  At the maximally mixed state \(\rho_*=I/N\), the
SLD/Bures inner product is
\[
  \langle A,B\rangle_B=N\,\operatorname{Tr}(A^*B).
\]
The coherent derivation is
\[
  \delta_H(X)=i[H,X],
\]
and its Bures second tensor is exactly
\[
  \langle \delta_H X_\mu,\delta_H X_\nu\rangle_B
  =
  N\sum_{i,j}|H_{ij}|^2
  (\xi_j^\mu-\xi_i^\mu)(\xi_j^\nu-\xi_i^\nu).
\]

The pure Hamiltonian generator \(i[H,\cdot]\) is skew-adjoint and contributes
zero symmetric Dirichlet form.  The Hermitian Lindblad dissipator
\[
  D_H(A)=HAH-\frac12\{H^2,A\}
       =-\frac12[H,[H,A]]
\]
contributes one half of the derivation quadratic form.  Therefore, for
diagonal physical observables at \(\rho_*=I/N\), this honest off-diagonal
Bures generator realizes the same edge-weight shadow with weights
\(|H_{ij}|^2\).  It does not create a new fourth-moment channel at this level.

The explicit \(Z_{30}\) check gives:
\[
  \max|\langle\delta X,\delta X\rangle_B-M_{\rm edge}|
  =
  2.47\times10^{-13},
\]
\[
  \max|\langle X,-i[H,X]\rangle_B|=0,
\]
and
\[
  \max|E_{D_H}-\tfrac12\langle\delta X,\delta X\rangle_B|
  =
  1.82\times10^{-12}.
\]
The scale-invariant unit-symbol fourth ratio agrees exactly between the
off-diagonal Bures realization and the diagonal edge shadow.  The \(Z_{210}\)
explicit check gives the same conclusion, with agreement at \(10^{-10}\)
level.

This does not rule out CRT-entangling CPTP lifts or coherent non-reversible
generators.  It only records what happens after restricting the readout to the
commuting diagonal coordinate algebra.  On that slice, the off-diagonal
Hamiltonian either contributes zero to the symmetric Dirichlet form
\(i[H,\cdot]\), or, when squared as a Hermitian Lindblad channel, collapses to
the same edge shadow.

The non-maximally mixed check is likewise a consistency identity, not an
independent measurement of a missing channel.  With
\(\rho_i\propto e^{-\beta\|\xi_i\|^2}\), \(\beta=0.75\), the SLD norm of the
generator image \((i[H,\cdot]+D_H)(X)\) does acquire a large
Hamiltonian/dissipative cross term.  But the Markov carre-du-champ is not
\(\|(i[H,\cdot]+D_H)X\|_B^2\).  It is
\[
  \Gamma_{\mathcal L}(A,B)
  =
  \frac12\{\mathcal L(A^*B)-\mathcal L(A^*)B-A^*\mathcal L(B)\},
\]
which is linear in \(\mathcal L\).  Therefore the reported quantity
\[
  \Gamma_{H+D}-\Gamma_H-\Gamma_D
\]
is algebraically zero before numerical evaluation.  Since \(i[H,\cdot]\) is a
derivation,
\[
  \Gamma_{i[H,\cdot]}=0,
  \qquad
  \Gamma_{i[H,\cdot]+D_H}=\Gamma_{D_H}.
\]
The audit verifies the resulting identities on the diagonal observables:

| row | \(\operatorname{cond}(\rho)\) | max \(|\Gamma_H|\) | max \(|\Gamma_{\rm cross}|\) | SLD image cross |
|---:|---:|---:|---:|---:|
| \(30\) | \(1.380457\times10^1\) | \(2.22\times10^{-16}\) | \(1.78\times10^{-15}\) | \(3.79\times10^3\) |
| \(210\) | \(7.462682\times10^1\) | \(1.11\times10^{-16}\) | \(1.78\times10^{-15}\) | \(1.78\times10^5\) |

Thus the cross term exists in the SLD norm of the generator image, but not in
the carre-du-champ/Dirichlet form whose resolvent produces a Green kernel.
Using the image norm would define a different higher-order diagnostic, not the
Dirichlet form in the Green-kernel theorem.  It is evidence for the reversible
Dirichlet-form reduction, not evidence that the coherent non-reversible
resolvent route fails.

## Non-Reversible Escape-Hatch Audit

The remaining adversarial question is whether a non-self-adjoint quantum
generator can have a \(1/r\) non-symmetric resolvent while its symmetric
locality diagnostic remains pinned.  The finite audit
`empirical/nonreversible_resolvent_audit.py` is only a classical positive-jump
stress test of this possibility.  It solves, on a periodic \(9^3\) target grid,
\[
  -\mathcal L g=\delta_0-\mathbf 1/N,\qquad \sum_x g(x)=0
\]
for the non-symmetric generator \(\mathcal L\), then fitting the off-source
kernel to \(a/r+b\).  The tested generators are:

1. local reversible nearest-neighbor diffusion;
2. local diffusion with a persistent directed current;
3. complete mean-field jumps;
4. complete mean-field jumps plus a directed local current.

Representative results are:

| model | unit fourth | current flux | \(1/r\) fit \(R^2\) | meaning |
|---|---:|---:|---:|---|
| local reversible | \(4.115226\times10^{-3}\) | \(0\) | \(0.984159\) | local Gamma gives the expected Green profile |
| local drift, weak current | \(4.115226\times10^{-3}\) | \(0.05\) | \(0.961156\) | small current does not destroy the local singularity |
| local drift, strong current | \(4.115226\times10^{-3}\) | \(0.35\) | \(0.525932\) | advection distorts the radial fit |
| complete mean-field | \(1.034294\times10^{-1}\) | \(0\) | \(-15.2988\) | off-source kernel is essentially flat, not \(1/r\) |
| complete plus current | \(1.005406\times10^{-1}\) | \(0.35625\) | \(0.301065\) | current does not rescue the pinned nonlocal geometry |
| complete plus strong local diffusion | \(2.896933\times10^{-2}\) | \(0.034426\) | \(0.967143\) | \(1/r\) returns only after local diffusion dominates Gamma |

This does not prove a universal no-go for non-reversible quantum Markov
semigroups.  It only says that, in a classical current-carrying jump model,
adding persistent probability current to a nonlocal mean-field generator does
not turn its Green kernel into \(1/r\) while keeping the symmetric locality
diagnostic pinned.  The no-go should therefore be stated, conservatively and
correctly, as a no-go for reversible CRT/Bures generators.  A genuine
non-equilibrium route would have to exhibit a conductor-compatible, cross-CRT
non-self-adjoint quantum generator whose antisymmetric/coherent sector yields
a local elliptic resolvent even though its reversible carre-du-champ shadow
remains nonlocal.  That is now the only door left, and it is not tested by the
diagonal-shadow off-diagonal audit.

The finite reason is also visible: in a positive jump generator, directed
current on an edge is bounded by the edge activity on that same support.  A
current strong enough to alter the resolvent therefore injects symmetric local
activity unless it is supplied by a genuinely quantum non-commutative channel.
That is exactly the remaining class, and it lies outside reversible
Dirichlet-form recovery.  The audit below gives the first finite measurement
of that class, so the "CRT/Bures localization no-go" remains a conjecture
beyond the leg-local dissipative family, not a theorem for the coherent sector.

## Quantum Projected-Resolvent Audit

The missing experiment is now implemented in
`empirical/quantum_nonreversible_resolvent_audit.py`.  It works on the full
matrix algebra for \(Z_{30}\) and splits
\[
  \mathcal A=P\mathcal A\oplus Q\mathcal A
\]
into diagonal physical readout and off-diagonal coherences.  For
\[
  \mathcal L(A)=i[H,A]+D_{\rm dephase}(A)+D_{\rm classical}(A),
\]
it compares:

1. the diagonal-only Green kernel from \(L_{PP}\);
2. the full projected kernel \(P(-\mathcal L)^{-1}P\);
3. the Schur/Feshbach kernel from
   \[
     L_{\rm eff}=L_{PP}-L_{PQ}L_{QQ}^{-1}L_{QP}.
   \]

This is the first audit in this chain that actually measures the coherent
sector through the non-symmetric resolvent rather than through
\(\Gamma\) on diagonal observables.

The default mean-field diagonal dissipator keeps the diagonal Gamma shadow
nonlocal:
\[
  q^{\Gamma}_{\rm unit}=2.8,\qquad
  R^2_{\rm diagonal\ only}\simeq -0.006.
\]
With a broad target-local coherent support (`--target-h-scale 8`) the Schur
correction is real but weak:
\[
  R^2_{P(-L)^{-1}P}=0.0477.
\]
With a mid-radius coherent support (`--target-h-scale 4`, `--h-strength 3`,
`--dephase-gamma 5`, real phase), the result changes qualitatively:
\[
  q^{\Gamma}_{\rm unit}=2.8,\qquad
  q^{H{\rm -support}}_{\rm unit}=0.4048,
\]
\[
  R^2_{\rm diagonal\ only}\simeq -0.006,\qquad
  R^2_{P(-L)^{-1}P}=0.8797,
\]
and the direct full projected kernel agrees with the Schur kernel at
\[
  \frac{\|P(-L)^{-1}P-G_{\rm Schur}\|}{\|P(-L)^{-1}P\|}
  =
  8.16\times10^{-16}.
\]
Thus the finite \(Z_{30}\) audit does **not** support a coherent-sector no-go.
It shows the opposite finite fact: an off-diagonal coherent block can strongly
reshape the projected physical Green kernel while the diagonal Gamma shadow
remains mean-field and nonlocal.

This is not yet gravity recovery.  The observed \(R^2\) is a finite-row signal,
not a Mosco or ephemeris-level theorem; shell isotropy and refinement remain
to be tested.  It is also not yet a conservative-force result.  The generator
used in this audit is non-self-adjoint and contains dephasing/dissipative
terms; it has not been derived from the conservative
\(K^{CH}(D\eta v,D\eta v)\), \(\Pi_{\rm EL}\), or Nambu-Bures dynamics of
Paper 28.  The next question is therefore no longer "does diagonal Gamma
localize?"  It splits in two:

**Coherent Schur localization problem.**  Does there exist a
conductor-compatible sequence of non-self-adjoint CRT/Bures generators whose
Schur correction
\[
  L_{PQ}L_{QQ}^{-1}L_{QP}
\]
converges to a target-local elliptic operator on the residual-zero quotient,
while the diagonal dissipative Gamma shadow remains nonlocal?

If yes, the coherent non-equilibrium route supplies the Bures-to-Laplacian
quotient the reversible program could not supply.  To make it
load-bearing for Paper 28's conservative mechanics, however, one must also
derive the non-symmetric Schur operator from a time-symmetric Bures/Nambu
variational reduction or show that its projected resolvent reduces to a
conservative potential on the physical quotient.  If no such bridge exists,
the Schur signal remains a neighboring Bures-resolvent model, not evidence for
the conservative ternary force law.  If the route fails, the no-go must be
proved at the level of Schur complements/non-symmetric resolvents, not at the
level of diagonal carre-du-champ identities.

The exact conservative bridge condition is recorded in
`Note_conservative_schur_bridge.md`: if the linearized Bures/Nambu generator
has Hamiltonian form \(L=JK\) and the \(P/Q\) split is symplectically
block-compatible, then
\[
  L_{PP}-L_{PQ}L_{QQ}^{-1}L_{QP}
  =
  J_P(K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}),
\]
so the Schur correction is the Hamiltonian lift of a symmetric stiffness
Schur complement.  The current \(Z_{30}\) audit does not yet satisfy those
hypotheses.

The follow-up `empirical/hamiltonian_schur_audit.py` verifies the Hamiltonian
version directly as an existence construction.  On the connected \(Z_{210}\)
run with `--target-h-scale 7.5`,
\[
  R^2(K_{PP}^{-1})=-0.066235,\qquad
  R^2(K_{\rm eff}^{-1})=0.772276,
\]
with Schur error \(2.38\times10^{-15}\) and
\[
  \max|L^TK+KL|=0.
\]
Thus conservative Hamiltonian algebra can carry Schur localization.  The
remaining issue is no longer reversible versus non-reversible algebra; it is
whether the required \(K_{PQ}\) can be derived from a structured CRT/Bures
Noether Hessian rather than chosen by spectral completion.

The subsequent split gate is now implemented in
`empirical/bures_hamiltonian_split_audit.py`.  It tests whether the declared
physical sector is symplectically block-compatible with the Bures/KKS Poisson
tensor before the Schur identity is used.  On the default \(Z_{30}\) unitary
leaf the equilibrium and Poisson gates pass:
\[
  \|-i[H_{\rm eq},\rho_*]\|=0,\qquad
  \max|J+J^T|=0,\qquad
  \operatorname{rank}J=870.
\]
The split results are decisive: diagonal population readout is not tangent to
the unitary orbit, target \(q\)-only and naive \(\xi\)-coordinate readouts fail
block compatibility, and only complete target matrix-unit quadrature pairs pass
with
\[
  \dim P=338,\qquad \operatorname{rank}J_{PP}=338,\qquad
  \|J_{PQ}\|/\|J\|=0.
\]
So the conservative Schur bridge is not available on the diagonal \(\xi\)
shadow.  The next conservative audit must either build a Darboux physical
sector that projects to \(\xi\), or work in the passing target-symplectic-pair
sector and only then ask whether a structured CRT/Bures Hessian supplies the
needed \(K_{PQ}\).
