# Note: Archimedean Metaplectic Selection Resolution

Random suffix: `Q8vM3`

Mission: settle the remaining Archimedean lock:

\[
\text{Bures/Petz/projective limit}
\stackrel{?}{\Longrightarrow}
\text{Weyl/CCR positive-energy oscillator packet}.
\]

Verdict:

\[
\boxed{
\text{The implication is false from the current axioms.  The metaplectic
positive-energy packet must be assumed or supplied by a new Archimedean
selection theorem.}
}
\]

This is a resolution, not a retreat.  The finite/projective theory now
transports positivity to Poisson windows once the completed gamma/K
normalization is present.  What this note proves is that the existing
Bures/Petz/projective data do not themselves force the Weyl cocycle, the
metaplectic Fourier operator, the positive-energy number operator, or the
CM divisor measure.  The exact missing input is the Metaplectic Archimedean
Selection Axiom stated in Section 5.

## 1. What the Current Archimedean Data Force

The current Archimedean construction gives:

1. a projective Bures/Fisher closed-current limit;
2. a canonical branch reflection \(t\mapsto -t\);
3. Bures/Petz metric functoriality and energy preservation under the
   corresponding unitary/antiunitary real structure;
4. the gamma multiplier
   \[
   \gamma(t)
   =
   {\Gamma_{\mathbb R}(1/2+it)\over
    \Gamma_{\mathbb R}(1/2-it)};
   \]
5. compatibility with the finite occupation recovery and leakage projection.

These data force the Archimedean phase.  They do not force the spectral
measure or the representation carrying that phase.

For every even positive measure \(\mu\) on \(\mathbb R\), define
\[
{\mathcal H}_\mu=L^2(\mathbb R,d\mu),
\qquad
(U_\mu f)(t)=\gamma(t)f(-t).
\]
Since \(\mu\) is even and \(|\gamma(t)|=1\),
\[
\|U_\mu f\|_{L^2(\mu)}=\|f\|_{L^2(\mu)}.
\]
Also \(\gamma(t)\gamma(-t)=1\), so \(U_\mu^2=I\).  Thus the same gamma
branch reflection exists for all even measures \(\mu\).

## 2. Countermodel With No Weyl/CCR Branch

Let
\[
\mu_{\rm at}
=
\delta_0+\sum_{k\ge1}2^{-k}(\delta_k+\delta_{-k}).
\]
The packet
\[
{\mathcal H}_{\rm at}=L^2(\mathbb R,d\mu_{\rm at})
\]
has:

1. an even positive height measure;
2. the unitary gamma reflection \(U_{\mu_{\rm at}}\);
3. the usual Bures metric on density matrices over the packet;
4. Bures isometry under conjugation by \(U_{\mu_{\rm at}}\);
5. the same visible gamma phase as the oscillator packet.

Let \(T\) be the height operator:
\[
(Tf)(t)=t f(t).
\]
Its spectrum is the discrete set
\[
S=\mathbb Z.
\]

Suppose, for contradiction, that the current data forced a regular Weyl pair
whose position branch is this height operator \(T\).  Then there would be a
strongly continuous unitary group \(V(v)\) satisfying the Weyl covariance
\[
V(v)T V(v)^*=T+vI,
\]
or equivalently on spectral projections,
\[
V(v)E_T(B)V(v)^*=E_T(B+v).
\]

Take \(B=S=\mathbb Z\) and \(v=1/2\).  Since \(E_T(S)=I\), covariance gives
\[
I
=
V(1/2)E_T(S)V(1/2)^*
=
E_T(S+1/2).
\]
But \(S+1/2\) is disjoint from the support of \(\mu_{\rm at}\), so
\[
E_T(S+1/2)=0.
\]
Contradiction.

Therefore this Archimedean packet satisfies the gamma-reflection/Bures
visible requirements but cannot be the Weyl/CCR oscillator packet with height
as one branch.

\[
\boxed{
\text{Bures/Petz/projective data plus gamma phase do not force Weyl/CCR.}
}
\]

## 3. Why Petz/Bures Minimality Does Not Repair This

The Bures metric is the minimal monotone Petz metric and the symmetric
logarithmic derivative metric.  This selects a metric on a state manifold.
It does not select:

1. an antisymmetric symplectic form
   \[
   \omega((u,v),(u',v'))=uv'-vu';
   \]
2. a central Weyl multiplier
   \[
   e^{\pi i\omega};
   \]
3. an irreducible regular representation of the Heisenberg group;
4. a positive-energy complex structure;
5. a number operator \(N\ge0\).

Metric minimality is symmetric.  The CCR cocycle is antisymmetric.  No
antisymmetric two-cocycle is determined by the Petz order alone.

There is also a finite-dimensional obstruction at every row.  If finite
operators \(Q_n,P_n\) satisfied
\[
[Q_n,P_n]=i\hbar I,\qquad \hbar\ne0,
\]
then
\[
0=\operatorname{Tr}[Q_n,P_n]
=i\hbar\operatorname{Tr}I,
\]
which is impossible.  A nontrivial CCR can only appear after an additional
limit that selects unbounded generators and the central cocycle.  The current
projective data do not specify that limit.

## 4. Conditional Selection Theorem

The correct positive theorem is the sharp conditional statement already
foreshadowed by Paper 22.

**Theorem 4.1 (conditional metaplectic selection).**  
Assume the projective Bures completion of the surviving closed \(A_2\) class
is equipped with:

1. a regular irreducible Weyl representation
   \[
   W(u,v)W(u',v')
   =
   e^{\pi i(uv'-vu')}W(u+u',v+v');
   \]
2. identification of the two closed Cartan branches with the infinitesimal
   position and momentum branches;
3. implementation of the critical branch involution by the metaplectic
   Fourier lift
   \[
   {\mathcal F}W(u,v){\mathcal F}^{-1}=W(v,-u);
   \]
4. a positive-energy oscillator polarization with cyclic even ground ray
   \[
   \psi_0(x)=e^{-\pi x^2}
   \]
   and first odd ray
   \[
   \psi_1(x)=x e^{-\pi x^2};
   \]
5. no extra unaccounted Cartan factor, or else an explicitly separated
   positive-energy factor.

Then the Archimedean packet is the Schrodinger oscillator packet on the cyclic
closed sector.  Its even and odd Mellin characters are
\[
2\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-s/2}\Gamma(s/2),
\]
and
\[
2\int_0^\infty x e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-(s+1)/2}\Gamma((s+1)/2).
\]

*Proof.*  Assumptions 1 and 2 give a regular irreducible Weyl system on the
cyclic closed sector.  By Stone-von Neumann, it is unitarily equivalent to
the Schrodinger representation.  Assumption 3 identifies the branch
involution with the metaplectic lift of the symplectic quarter-turn.  Assumption
4 chooses the positive-energy oscillator complex structure and parity split.
The displayed Mellin integrals follow by the substitution \(u=\pi x^2\).
Assumption 5 prevents a hidden factor from modifying the character. \(\square\)

## 5. The Required Axiom

The remaining Archimedean input should now be named without ambiguity.

**Axiom MAS (Metaplectic Archimedean Selection).**  
The projective Bures completion of the surviving closed \(A_2\) current class
selects a regular irreducible Weyl representation whose central cocycle is
\[
e^{\pi i(uv'-vu')},
\]
whose branch involution is the metaplectic Fourier lift, and whose Bures
positive-energy polarization sends the two closed Cartan branches to the even
ground oscillator ray and the first odd oscillator ray.  No extra Cartan
factor contributes to the completed zeta normalization except through a
separately accounted positive-energy factor.

Under MAS, Theorem 4.1 supplies exactly the completed Archimedean gamma/K
packet needed by the positive-current transport theorem
`Note_PositiveCurrentTransport_Q8vM3.md`.

Without MAS, the atomic countermodel of Section 2 and the measure freedom of
Section 1 show that the current axioms admit Archimedean packets that have
the correct gamma phase but are not the oscillator packet and do not select
the CM divisor measure.

## 6. Connection to the RH Chain

With MAS:

1. the Archimedean gamma/K normalization is no longer inserted by hand;
2. `Note_PositiveCurrentTransport_Q8vM3.md` gives
   \[
   \mathfrak P_{\phi,y}(\Xi)\ge0
   \]
   for every nonnegative \(K\)-even detector in the Poisson-window detector
   topology;
3. the Poisson-window bridge gives
   \[
   \operatorname{Im}m_B(x+iy)\ge0;
   \]
4. CM Poisson monotonicity is equivalent to RH.

Thus the conditional final theorem is:

\[
\boxed{
\text{Finite Noether positivity + MAS}
\Longrightarrow
\mathfrak P_{\phi,y}(\Xi)\ge0
\Longrightarrow
\mathrm{RH}.
}
\]

Without MAS or an equivalent new Archimedean selection theorem, the same
finite/projective/gamma data admit non-oscillator packets.  Therefore the
unconditional implication from Bures/Petz/projective principles to the
positive-energy oscillator packet is not proved and is in fact false for the
current axiom list.

## 7. Final Status

Closed in this note:

1. the no-go theorem for automatic Weyl/CCR selection from the current
   Bures/Petz/projective data;
2. the concrete atomic gamma-reflection countermodel;
3. the precise conditional Stone-von Neumann/metaplectic theorem;
4. the exact axiom, MAS, that must be assumed or independently proved.

Remaining only if one wants an unconditional RH theorem from internal
principles:

1. replace MAS by a new proof that the projective Bures limit forces the
   antisymmetric Weyl cocycle, metaplectic Fourier branch involution, and
   positive-energy oscillator polarization.

Addendum Q8vM3 proof boundary:
`Note_MASProofBoundary_Q8vM3.md` proves the exact boundary theorem.  Over the
current Bures/Petz/projective package, MAS is equivalent to adding ASC
(Archimedean Symplectic Covariance: the regular irreducible Weyl multiplier
and metaplectic quarter-turn) plus PEP (Positive-Energy Polarization: the
oscillator complex structure and parity split).  The atomic gamma-reflection
packet shows that ASC+PEP cannot be derived from the present axioms.
