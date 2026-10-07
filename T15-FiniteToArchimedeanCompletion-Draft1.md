# T15 - Finite-to-Archimedean Completion

**Continuum Geometry as the Fixed Point of Closure-Compatible Apex Algebras**

**Leonardo Murillo Montero**

*First draft - May 26, 2026*

---

> *The continuum is what finite closure demands at infinity.*

---

## Abstract

**Situation.** T11 proved that finite apex interactions are governed by character conservation and conductor-fusion boundaries. T12 proved that apex towers are finite spectral objects. T13 proved that projection and renormalization are closure operations on conductor-packet sectors. T14 proved that curvature is projected nonclosure: flat lifted transport becomes curvature, Schur correction, beta source, and Noether defect after nonclosed projection.

**Gap.** These results are finite. Yet the framework keeps touching continuum geometry, Dirichlet and Mellin transforms, gamma factors, metaplectic normalization, and archimedean self-duality. This is not an accident. The missing theorem is not that finite systems approximate the continuum. The stronger claim is that closure-compatible finite systems have a forced completion, and the archimedean continuum is the terminal boundary required by that completion.

**Action.** We prove ten structure theorems. First, the **Apex Inverse-System Theorem**: for \(N\mid M\), reduction \(\mathbb Z/M\to\mathbb Z/N\) induces compatible pullbacks of ledgers, characters, conductor packets, apex generators, and finite apex algebras. Second, the **Refinement Boundary Theorem**: old packets embed under refinement and genuinely new packets are exactly the refinement boundary. Third, the **Closure Compatibility Theorem**: fusion closure commutes with refinement unless new refinement packets are forced. Fourth, the **Archimedean Boundary Theorem**: along a cofinal finite conductor tower, the real place is the terminal boundary correction required for global Fourier-Mellin compatibility. Fifth, the **Metaplectic Selection Theorem**: finite Fourier duality selects the self-dual real Fourier/metaplectic normalization and hence the gamma factor. Sixth, the **Continuum Fisher Limit Theorem**: finite Fisher and cumulant tensors converge to continuum information geometry under mesh-compatible refinement. Seventh, the **Curvature Limit Theorem**: smooth curvature is the limit of compatible finite projection-boundary defects. Eighth, the **Discretization Certificate Theorem**: faithful discretization is equivalent to refinement compatibility, closure compatibility, archimedean inclusion, and tensor convergence. Ninth, the **Finite-to-Archimedean Completion Theorem**: a compatible tower has a unique completed object. Tenth, the **Archimedean Fixed-Point Theorem**: completion is an idempotent closure operator, and completed continuum objects are its fixed points.

**Result.** The central compression is
\[
\boxed{
\text{continuum geometry}
=
\text{the fixed point of refinement, fusion closure, and real-place completion}.
}
\]
The finite conductor/Euler side is not globally self-complete by itself. The archimedean factor is the boundary term required for Fourier-Mellin self-duality.

**Harvest.** T15 turns finite-to-continuum passage into the same boundary logic developed in T11-T14. Refinement introduces new packets, projection introduces curvature, fusion closure removes finite boundary defects, and the real place supplies the terminal archimedean boundary. The theorem explains why the finite arithmetic skeleton repeatedly touches gamma factors, Poisson summation, completed \(L\)-functions, and smooth information geometry. Its simplest scalar instance is the **smooth primorial** פ (§12): the completion of the primorial magnitude, whose archimedean normalization \(1/2\pi\) *is* the real-place boundary, and whose moment obstruction (\(D_3<0\)) proves the real place is not a finite packet.

**Keywords:** finite-to-archimedean completion, apex inverse system, conductor packets, refinement boundary, archimedean place, gamma factor, metaplectic normalization, Poisson summation, Fisher limit, curvature limit, closure-compatible discretization, completed \(L\)-function, finite information geometry, smooth primorial פ, moment obstruction.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| T0 Fourier-Mellin simplex and apex generator | Base finite apex object |
| T1 native simplicial chart | Finite simplex and continuum information-geometric limit |
| T2 cumulant tower as effective action | Higher tensor convergence and cumulant language |
| T3 character orthogonality and conductor packets | Finite character/conductor labels |
| T8 multiplicative apex and Dirichlet polynomials | Finite Euler/Mellin side |
| T9 Helmert-Fourier transfer matrix | Basis transfer and finite Fourier compatibility |
| T10 Kummer clock and power hierarchy | Refinement along integer/gauge towers |
| T11 Apex Vertex Calculus | Conductor fusion under finite interactions |
| T12 Finite Apex Determinacy | Finite apex algebras and closure polynomials |
| T13 Exact Simplicial Renormalization | Closure operators and boundary adjunction |
| T14 Projected Flatness | Curvature as projection boundary and its continuum target |

---

## Notation

For positive integers \(N\mid M\), write
\[
M=kN.
\]
Let
\[
\pi_{M,N}:\mathbb Z/M\to\mathbb Z/N
\]
be reduction modulo \(N\).

At level \(N\), characters are
\[
\chi_a^{(N)}(s)=e^{2\pi ias/N},
\qquad a,s\in\mathbb Z/N.
\]
The additive conductor is
\[
\operatorname{cond}_N(a)=\frac{N}{\gcd(a,N)},
\]
with \(\operatorname{cond}_N(0)=1\). The nontrivial conductor set is
\[
\mathcal D_N=\{d:d\mid N,\ d>1\}.
\]
The conductor packet is
\[
H_d^{(N)}
=
\operatorname{span}_{\mathbb C}\{\chi_a^{(N)}:\operatorname{cond}_N(a)=d\}.
\]

For a ledger \(x_N:\mathbb Z/N\to\mathbb R_{>0}\), define the pullback ledger
\[
x_N^\uparrow=x_N\circ\pi_{M,N}.
\]
Its centered log-ledger is
\[
y_N(s)=\log x_N(s)-\frac1N\sum_{u\in\mathbb Z/N}\log x_N(u).
\]
The structured finite apex is
\[
\mathcal M_N(x_N;\beta,a)
=
\frac1N\sum_{s\in\mathbb Z/N}
e^{\beta y_N(s)}
\overline{\chi_a^{(N)}(s)}.
\]

For \(S\subseteq\mathcal D_N\), write \(S^\uparrow\subseteq\mathcal D_M\) for the same conductor labels viewed at level \(M\). The \(n\)-fusion closure at level \(N\) is
\[
\operatorname{Cl}_{N,n}(S),
\]
or simply \(\operatorname{Cl}_N(S)\) when \(n\) is fixed.

For a continuum density \(\rho\) on the circle \(\mathbb T=\mathbb R/\mathbb Z\), a mesh-compatible finite ledger is
\[
p_s^{(N)}=\frac1N\rho(s/N).
\]

---

## 1. Why the archimedean place enters

The finite tower can refine forever through \(N\):
\[
N\mid M\mid L\mid\cdots.
\]
The old finite data pull back exactly. New finite packets appear exactly as new conductors. Fusion closure decides which packets must be adjoined. T13 and T14 explain those finite boundary terms.

But a global Fourier-Mellin object has one more place:
\[
\{p\text{ prime}\}\cup\{\infty\}.
\]
A primorial tower exhausts the finite primes, but no finite \(N\) contains the real place. Therefore the archimedean term is not decorative. It is the terminal boundary required for the finite tower to become globally self-dual.

This paper's guiding slogan is:
\[
\boxed{
\text{finite conductor closure}+\text{real-place boundary}
=
\text{continuum completion}.
}
\]

---

## 2. Apex inverse systems

### Theorem 1. Apex Inverse-System Theorem

Let \(N\mid M\), write \(M=kN\), and let
\[
\pi_{M,N}:\mathbb Z/M\to\mathbb Z/N
\]
be reduction modulo \(N\). Then pullback along \(\pi_{M,N}\) sends ledgers, centered log-ledgers, characters, conductor packets, apex generators, and finite apex algebras at level \(N\) into compatible objects at level \(M\).

Moreover,
\[
\chi_a^{(N)}\circ\pi_{M,N}=\chi_{ka}^{(M)}
\]
and
\[
\operatorname{cond}_M(ka)=\operatorname{cond}_N(a).
\]
Thus the finite cyclic apex systems form an inverse-compatible architecture: groups reduce downward, while observables and apex algebras pull back upward.

**Proof.** Given a ledger
\[
x_N:\mathbb Z/N\to\mathbb R_{>0},
\]
define
\[
x_M=x_N^\uparrow=x_N\circ\pi_{M,N}.
\]
This ledger is constant on the fibers of \(\pi_{M,N}\), each of size \(k\).

For characters,
\[
(\chi_a^{(N)}\circ\pi_{M,N})(s)
=
e^{2\pi ia(s\bmod N)/N}
=
e^{2\pi ias/N}.
\]
Since \(M=kN\),
\[
e^{2\pi ias/N}
=
e^{2\pi i(ka)s/M}
=
\chi_{ka}^{(M)}(s).
\]
Hence
\[
\chi_a^{(N)}\circ\pi_{M,N}=\chi_{ka}^{(M)}.
\]

For conductors,
\[
\operatorname{cond}_M(ka)
=
\frac{kN}{\gcd(ka,kN)}
=
\frac{kN}{k\gcd(a,N)}
=
\frac{N}{\gcd(a,N)}
=
\operatorname{cond}_N(a).
\]
Therefore
\[
(H_d^{(N)})^\uparrow\subseteq H_d^{(M)}.
\]

For centered log-ledgers,
\[
\frac1M\sum_{s\in\mathbb Z/M}\log x_M(s)
=
\frac1{kN}\sum_{s\in\mathbb Z/M}\log x_N(\pi_{M,N}(s))
=
\frac1N\sum_{u\in\mathbb Z/N}\log x_N(u),
\]
because each \(u\) has \(k\) preimages. Hence
\[
y_M(s)=y_N(\pi_{M,N}(s)).
\]

For apex generators,
\[
\mathcal M_M(x_N^\uparrow;\beta,ka)
=
\frac1M\sum_{s\in\mathbb Z/M}
e^{\beta y_M(s)}
\overline{\chi_{ka}^{(M)}(s)}.
\]
Substitute the pullback identities and group by fibers:
\[
\mathcal M_M(x_N^\uparrow;\beta,ka)
=
\frac1M\sum_s
e^{\beta y_N(\pi_{M,N}(s))}
\overline{\chi_a^{(N)}(\pi_{M,N}(s))}
\]
\[
=
\frac{k}{kN}\sum_{t\in\mathbb Z/N}
e^{\beta y_N(t)}
\overline{\chi_a^{(N)}(t)}
=
\mathcal M_N(x_N;\beta,a).
\]

Finally, if \(y_N\) has distinct values \(\lambda_1,\ldots,\lambda_r\), then \(y_M=y_N\circ\pi_{M,N}\) has the same distinct values. Thus the T12 closure polynomial
\[
P_{x_N}(t)=\prod_{j=1}^r(t-\lambda_j)
\]
is unchanged:
\[
P_{x_M}(t)=P_{x_N}(t).
\]
Therefore
\[
\mathbb R[t]/(P_{x_N})
\cong
\mathbb R[t]/(P_{x_M})
\]
for pulled-back ledgers. \(\square\)

---

## 3. Refinement boundaries

### Theorem 2. Refinement Boundary Theorem

Let \(N\mid M\). Under pullback, every level-\(N\) conductor packet embeds conductor-preservingly into level \(M\):
\[
(H_d^{(N)})^\uparrow\subseteq H_d^{(M)}.
\]
The genuinely new nontrivial conductor packets introduced by refinement are exactly
\[
\partial_{N\to M}^{\mathrm{new}}
=
\mathcal D_M\setminus\mathcal D_N.
\]
For a retained sector \(S\subseteq\mathcal D_N\), the full not-retained packet boundary at level \(M\) is
\[
\partial_{N\to M}^{S}
=
\mathcal D_M\setminus S^\uparrow
=
(\mathcal D_N\setminus S)
\cup
(\mathcal D_M\setminus\mathcal D_N).
\]
Thus refinement preserves old packets exactly and adds only new conductor packets. These new packets are the finite precursor of continuum new modes.

**Proof.** The first statement is Theorem 1:
\[
\operatorname{cond}_M(ka)=\operatorname{cond}_N(a),
\]
so level-\(N\) conductor-\(d\) characters pull back into level-\(M\) conductor-\(d\) characters.

The nontrivial packet labels at level \(N\) are
\[
\mathcal D_N=\{d:d\mid N,\ d>1\},
\]
and at level \(M\)
\[
\mathcal D_M=\{e:e\mid M,\ e>1\}.
\]
Since \(N\mid M\), every divisor of \(N\) is a divisor of \(M\), so
\[
\mathcal D_N\subseteq\mathcal D_M.
\]
The packets labeled by \(\mathcal D_N\) are old packets. The packets labeled by
\[
\mathcal D_M\setminus\mathcal D_N
\]
cannot be pullbacks from level \(N\), because their conductor labels do not divide \(N\). Therefore these are exactly the genuinely new packets.

For \(S\subseteq\mathcal D_N\), the pullback retained set is the same conductor set viewed inside \(\mathcal D_M\):
\[
S^\uparrow=S\subseteq\mathcal D_M.
\]
The complement at level \(M\) decomposes as
\[
\mathcal D_M\setminus S^\uparrow
=
(\mathcal D_N\setminus S)
\cup
(\mathcal D_M\setminus\mathcal D_N).
\]
The first term consists of old packets not retained by \(S\). The second term consists of genuinely new refinement packets. \(\square\)

---

## 4. Closure compatibility

### Theorem 3. Closure Compatibility Theorem

Fix an interaction order \(n\). Let \(N\mid M\), and let \(S\subseteq\mathcal D_N\). For pure pullback refinement,
\[
\operatorname{Cl}_M(S^\uparrow)
=
\big(\operatorname{Cl}_N(S)\big)^\uparrow.
\]
Equivalently, old conductor fusion forces no new conductor packet under refinement. If the refined model deliberately admits genuinely new level-\(M\) packets
\[
B\subseteq\mathcal D_M\setminus\mathcal D_N,
\]
then any failure of closure compatibility is exactly the T13 boundary generated by those new packets:
\[
\Delta_{N\to M}^{(n)}(S;B)
=
\operatorname{Cl}_M(S^\uparrow\cup B)
\setminus
\big((\operatorname{Cl}_N(S))^\uparrow\cup B\big).
\]

**Proof.** If \(d_1,\ldots,d_n\in\mathcal D_N\), character pullback sends
\[
\chi_{a_i}^{(N)}\mapsto \chi_{ka_i}^{(M)}
\]
and preserves conductors. Products are compatible because
\[
\chi_{ka_1}^{(M)}\cdots\chi_{ka_n}^{(M)}
=
\chi_{k(a_1+\cdots+a_n)}^{(M)}.
\]
Again by conductor preservation,
\[
\operatorname{cond}_M(k(a_1+\cdots+a_n))
=
\operatorname{cond}_N(a_1+\cdots+a_n).
\]
Thus
\[
\operatorname{Fuse}_M(d_1,\ldots,d_n)
=
\operatorname{Fuse}_N(d_1,\ldots,d_n)
\]
for old conductor labels, with the right-hand side viewed in \(\mathcal D_M\).

Let the closure iteration at level \(N\) be
\[
S_0=S,
\qquad
S_{r+1}=S_r\cup(\operatorname{Fuse}_N(S_r)\setminus\{1\}).
\]
At level \(M\), start with
\[
T_0=S^\uparrow.
\]
By fusion compatibility,
\[
T_1
=
S^\uparrow\cup(\operatorname{Fuse}_M(S^\uparrow)\setminus\{1\})
=
\left(S\cup(\operatorname{Fuse}_N(S)\setminus\{1\})\right)^\uparrow
=
S_1^\uparrow.
\]
Inductively,
\[
T_r=S_r^\uparrow
\]
for every \(r\). Both chains stabilize because the conductor lattices are finite. Therefore
\[
\operatorname{Cl}_M(S^\uparrow)
=
\big(\operatorname{Cl}_N(S)\big)^\uparrow.
\]

If new refined packets \(B\subseteq\mathcal D_M\setminus\mathcal D_N\) are added, pure pullback compatibility no longer describes the whole refined sector. The additional forced packets are, by definition of T13 fusion closure, exactly the difference
\[
\operatorname{Cl}_M(S^\uparrow\cup B)
\setminus
\big((\operatorname{Cl}_N(S))^\uparrow\cup B\big).
\]
This is the boundary generated by the new refinement modes. \(\square\)

---

## 5. The archimedean boundary

### Theorem 4. Archimedean Boundary Theorem

Let
\[
N_k=\prod_{p\le p_k}p
\]
be the primorial refinement tower. The finite apex systems over \(N_k\) account, in the limit, for all finite prime conductor packets. However, finite conductor compatibility alone is not closed under global Fourier-Mellin self-duality. The remaining terminal compatibility term is the real-place, or archimedean, boundary.

In the Dirichlet/Mellin case, this boundary is the gamma factor
\[
\Gamma_\infty(s,\varepsilon)
=
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right),
\qquad
\varepsilon\in\{0,1\}.
\]
Thus
\[
\boxed{
\Gamma_\infty=\text{the real-place boundary correction required by Fourier-Mellin self-duality}.
}
\]
This is a completion theorem, not a proof of RH.

**Proof.** By Theorems 1-3, each refinement
\[
N_k\mid N_{k+1}
\]
preserves old finite conductor packets and adds only new finite prime conductor packets. Along the primorial tower, every finite prime eventually appears. Thus the tower exhausts the non-archimedean conductor side.

But global Fourier-Mellin self-duality uses all places of \(\mathbb Q\):
\[
\{p\text{ prime}\}\cup\{\infty\}.
\]
No finite primorial \(N_k\) contains the real place. Therefore after all finite refinement, one terminal compatibility boundary remains:
\[
\partial_{\mathrm{arch}}=\{\infty\}.
\]

At the real place, take the self-dual Gaussian
\[
\phi_\infty(x)=e^{-\pi x^2}.
\]
Its Mellin transform over \(\mathbb R^\times\) is
\[
Z_\infty(s)
=
\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\,d^\times x.
\]
Since \(d^\times x=dx/|x|\),
\[
Z_\infty(s)
=
2\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right).
\]
For odd parity, the real test vector carries one factor of \(x\), shifting \(s\mapsto s+1\):
\[
Z_\infty(s,1)
=
\pi^{-(s+1)/2}\Gamma\!\left(\frac{s+1}{2}\right).
\]
Thus, in parity \(\varepsilon\),
\[
Z_\infty(s,\varepsilon)
=
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right).
\]

The finite Euler/conductor product alone therefore lacks the real local factor required by Fourier-Mellin self-duality. Adding \(\Gamma_\infty\) supplies precisely this terminal boundary. In T13/T14 language, the finite conductor system is the retained sector, the real place is the terminal omitted boundary, and the gamma factor is the effective correction required for closure under the global transform. \(\square\)

---

## 6. Metaplectic selection

### Theorem 5. Metaplectic Selection Theorem

The archimedean boundary compatible with the finite character Fourier systems is unique up to the standard harmless phase: it is the self-dual Fourier/metaplectic operator
\[
(\mathcal F_\infty f)(\xi)
=
\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx
\]
with self-dual measure \(dx\). Under this normalization,
\[
\mathcal F_\infty(e^{-\pi x^2})=e^{-\pi \xi^2}.
\]
Consequently the real-place Mellin boundary is
\[
\Gamma_\infty(s,\varepsilon)
=
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right).
\]
Thus finite character duality selects Poisson/Gaussian self-duality at infinity.

**Proof.** At finite level \(N\), the normalized character transform is
\[
(\mathcal F_N f)(a)
=
\frac1{\sqrt N}\sum_{s\in\mathbb Z/N}
f(s)e^{-2\pi ias/N}.
\]
It satisfies
\[
\mathcal F_N^2f(s)=f(-s),
\qquad
\mathcal F_N^4=1,
\]
and exchanges translation and modulation:
\[
\mathcal F_NT_b\mathcal F_N^{-1}=M_b.
\]

A compatible real-place boundary must implement the same structural relation in the continuum Heisenberg representation: the symplectic rotation
\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
\]
exchanges position and frequency. By the Stone-von Neumann theorem, the irreducible unitary representation of the Heisenberg commutation relations is unique up to unitary equivalence. The operators implementing symplectic transformations form the metaplectic representation. Therefore the real operator compatible with finite Fourier transfer is the metaplectic lift of \(J\), namely the Fourier transform, up to phase.

The scale is fixed by self-dual Haar measure and Gaussian self-duality. With kernel
\[
e^{-2\pi ix\xi},
\]
one has
\[
\mathcal F_\infty(e^{-\pi x^2})=e^{-\pi \xi^2}.
\]
Any other scale sends the Gaussian to a differently scaled Gaussian and breaks the self-dual normalization required for Poisson summation.

The Mellin transform of the selected even real vector gives
\[
2\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right).
\]
Odd parity shifts \(s\mapsto s+1\). Hence
\[
\Gamma_\infty(s,\varepsilon)
=
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right).
\]
Therefore the archimedean boundary is selected by finite Fourier compatibility plus Gaussian self-duality. \(\square\)

---

## 7. Continuum Fisher limits

### Theorem 6. Continuum Fisher Limit Theorem

Let \(\rho\in C^1(\mathbb T)\) be a strictly positive probability density, and let \(\delta\rho\) be a tangent variation with
\[
\int_{\mathbb T}\delta\rho(x)\,dx=0.
\]
For mesh points
\[
x_s=\frac{s}{N},
\qquad s=0,\ldots,N-1,
\]
define
\[
p_s^{(N)}=\frac1N\rho(x_s),
\qquad
\delta p_s^{(N)}=\frac1N\delta\rho(x_s).
\]
Then
\[
\sum_{s=0}^{N-1}
\frac{(\delta p_s^{(N)})^2}{p_s^{(N)}}
\longrightarrow
\int_{\mathbb T}\frac{\delta\rho(x)^2}{\rho(x)}\,dx.
\]
More generally, for smooth tangent variations \(\delta_1\rho,\ldots,\delta_m\rho\),
\[
\sum_{s=0}^{N-1}
\frac{\delta_1p_s^{(N)}\cdots\delta_mp_s^{(N)}}{(p_s^{(N)})^{m-1}}
\longrightarrow
\int_{\mathbb T}
\frac{\delta_1\rho(x)\cdots\delta_m\rho(x)}
{\rho(x)^{m-1}}\,dx.
\]

**Proof.** For the Fisher form,
\[
\frac{(\delta p_s^{(N)})^2}{p_s^{(N)}}
=
\frac{(N^{-1}\delta\rho(x_s))^2}
{N^{-1}\rho(x_s)}
=
\frac1N\frac{\delta\rho(x_s)^2}{\rho(x_s)}.
\]
Therefore
\[
\sum_s\frac{(\delta p_s^{(N)})^2}{p_s^{(N)}}
=
\frac1N\sum_s
\frac{\delta\rho(x_s)^2}{\rho(x_s)}.
\]
Since \(\rho>0\) and the variation is smooth, the summand is continuous. This Riemann sum converges to
\[
\int_{\mathbb T}\frac{\delta\rho(x)^2}{\rho(x)}\,dx.
\]

For the \(m\)-tensor,
\[
\frac{\delta_1p_s^{(N)}\cdots\delta_mp_s^{(N)}}{(p_s^{(N)})^{m-1}}
=
\frac{N^{-m}\delta_1\rho(x_s)\cdots\delta_m\rho(x_s)}
{N^{-(m-1)}\rho(x_s)^{m-1}}
\]
\[
=
\frac1N
\frac{\delta_1\rho(x_s)\cdots\delta_m\rho(x_s)}
{\rho(x_s)^{m-1}}.
\]
Again this is a Riemann sum, hence converges to the stated integral. For \(m=2\) this is the Fisher metric; for \(m=3\) it is the continuum cubic information tensor; higher \(m\) give the corresponding continuum categorical tensor limits. \(\square\)

Closure-compatible refinement ensures these are not isolated numerical approximations, but compatible finite Fisher skeletons whose tensor algebra persists through the limit.

---

## 8. Curvature limits

### Theorem 7. Curvature Limit Theorem

Let \(X_N\) be a compatible refinement tower of finite meshes converging to a smooth space \(X\). Let \(E_N\to X_N\) be finite apex/ledger bundles with flat lifted finite connections \(\nabla_N\), and let
\[
\Pi_N:E_N\to E_N
\]
be retained-sector projections. Assume:

1. \(\Pi_N\to\Pi_\infty\);
2. \(\nabla_N\to\nabla_\infty\), where \(\nabla_\infty\) is flat;
3. the projected sectors are closure-compatible, so finite boundary defects refine coherently.

Define finite projected curvature by
\[
\mathcal R_N(X,Y)
=
\Pi_N\left(
[\nabla^N_X,\Pi_N][\nabla^N_Y,\Pi_N]
-
[\nabla^N_Y,\Pi_N][\nabla^N_X,\Pi_N]
\right)\Pi_N.
\]
Then
\[
\mathcal R_N(X,Y)\longrightarrow R_\infty(X,Y),
\]
where
\[
R_\infty(X,Y)
=
\Pi_\infty\left(
[\nabla^\infty_X,\Pi_\infty][\nabla^\infty_Y,\Pi_\infty]
-
[\nabla^\infty_Y,\Pi_\infty][\nabla^\infty_X,\Pi_\infty]
\right)\Pi_\infty.
\]
Thus smooth projected curvature is the compatible refinement limit of finite conductor-boundary curvature defects.

**Proof.** By T14, finite projected curvature has the projection-commutator form
\[
\mathcal R_N
=
\Pi_N\,d_N\Pi_N\wedge d_N\Pi_N\,\Pi_N.
\]
Equivalently,
\[
\mathcal R_N(X,Y)
=
\Pi_N\left(
[\nabla^N_X,\Pi_N][\nabla^N_Y,\Pi_N]
-
[\nabla^N_Y,\Pi_N][\nabla^N_X,\Pi_N]
\right)\Pi_N.
\]
The assumptions give
\[
\Pi_N\to\Pi_\infty
\]
and
\[
[\nabla^N_X,\Pi_N]\to[\nabla^\infty_X,\Pi_\infty]
\]
for each smooth limiting direction \(X\). Hence products converge:
\[
[\nabla^N_X,\Pi_N][\nabla^N_Y,\Pi_N]
\to
[\nabla^\infty_X,\Pi_\infty][\nabla^\infty_Y,\Pi_\infty],
\]
and similarly with \(X,Y\) reversed. Multiplying by the convergent projections on left and right yields
\[
\mathcal R_N(X,Y)\to R_\infty(X,Y).
\]

At every finite level, T14's Boundary Curvature Theorem says \(\mathcal R_N\) is supported exactly on the conductor-fusion boundary \(\partial_nS_N\). Closure compatibility ensures these supports refine coherently rather than appearing as unrelated discretization artifacts. Therefore the continuum tensor \(R_\infty\) is the limiting boundary flux:
\[
R_\infty=\lim_N\mathcal R_N.
\]
If every \(S_N\) is fusion-closed, then \(\mathcal R_N=0\) for all \(N\), hence \(R_\infty=0\). Otherwise, compatible nonzero finite boundaries converge to smooth curvature. \(\square\)

---

## 9. Discretization certificates

### Theorem 8. Discretization Certificate Theorem

Let \(\mathcal M_\infty\) be a continuum information-geometric model with Fisher/cumulant tensors and, when relevant, an archimedean Fourier-Mellin boundary. Let
\[
\{\mathcal M_N\}_{N\in\mathcal I}
\]
be a cofinal tower of finite apex discretizations. The tower is a faithful discretization of \(\mathcal M_\infty\) if and only if it satisfies:

1. refinement compatibility;
2. fusion closure compatibility;
3. archimedean boundary inclusion;
4. Fisher/cumulant convergence.

If any condition fails, the failure is localized by a boundary certificate: a refinement boundary, fusion boundary, archimedean boundary, or tensor-convergence boundary.

**Proof.** First assume the tower is faithful. Faithfulness means the finite objects are compatible finite shadows of one continuum object. Therefore if \(N\mid M\), reducing level \(M\) to level \(N\) and evaluating the level-\(N\) model must agree with the old observables. This is refinement compatibility.

Closure must also be compatible. If a sector closes at level \(N\), its pullback cannot become falsely nonclosed at level \(M\) unless genuinely new refinement packets have appeared. Thus fusion closure compatibility is necessary.

For a global Fourier-Mellin continuum model, finite conductor/Euler data alone cannot be faithful to the completed continuum object, because the real place is not contained in any finite level. The archimedean boundary term must be included. In the Dirichlet/Mellin case this is \(\Gamma_\infty\).

Finally, faithfulness requires geometric convergence:
\[
\sum_s\frac{\delta p_s^2}{p_s}
\to
\int\frac{\delta\rho^2}{\rho},
\]
and similarly for higher tensors. Otherwise the finite tower may be algebraically compatible but geometrically wrong.

Conversely, suppose the four conditions hold. Refinement compatibility gives a coherent tower of finite apex systems. Fusion closure compatibility ensures that projected sectors do not generate unexplained packets under refinement; any new packets are explicitly marked as boundaries. Archimedean boundary inclusion completes the finite conductor tower at the real place. Fisher/cumulant convergence guarantees that the finite information geometry converges to the claimed continuum geometry. Hence every structural component of \(\mathcal M_\infty\) is recovered by compatible finite data, so the tower is faithful.

If refinement compatibility fails, the defect is a refinement boundary. If fusion closure compatibility fails, the defect is
\[
\Delta_{N\to M}^{(n)}(S)
=
\operatorname{Cl}_M(S^\uparrow)
\setminus
(\operatorname{Cl}_N(S))^\uparrow.
\]
If archimedean inclusion fails, the missing boundary is
\[
\partial_{\mathrm{arch}}=\{\infty\}.
\]
If tensor convergence fails, the defect is the tensor residual
\[
\mathcal E_N^{(m)}
=
T_m^{(N)}-T_m^\infty
\]
under the chosen refinement map. Thus failure is diagnosed as a named boundary. \(\square\)

---

## 10. Finite-to-archimedean completion

### Theorem 9. Finite-to-Archimedean Completion Theorem

Let
\[
\{\mathcal A_N\}_{N\in\mathcal I}
\]
be a cofinal refinement tower of finite apex systems satisfying the Discretization Certificate. Then there exists a unique completed object
\[
\widehat{\mathcal A}
\]
determined by:
\[
\boxed{
\widehat{\mathcal A}
=
\text{finite conductor data}
+
\text{refinement limits}
+
\text{archimedean boundary term}.
}
\]
Moreover, its continuum geometry is the limit of projected-flat finite apex geometries:
\[
G_\infty=\lim_NG_N,
\qquad
T_{m,\infty}=\lim_NT_{m,N},
\qquad
R_\infty=\lim_N\mathcal R_N.
\]

**Proof.** By Theorem 1, the finite apex systems form a compatible tower: for \(N\mid M\), old ledgers, characters, conductor packets, apex generators, and finite apex algebras pull back compatibly. Thus the finite conductor data have a coherent refinement system.

By Theorems 2 and 3, refinement adds only identifiable new conductor packets, and fusion closure commutes with refinement unless explicitly new refinement packets are admitted. Thus all finite non-archimedean boundary data are tracked by refinement and fusion closure.

By Theorems 4 and 5, a cofinal finite-prime tower still lacks one terminal boundary: the real place. The archimedean term is selected by metaplectic/Gaussian self-duality. In the Mellin case it is
\[
\Gamma_\infty(s,\varepsilon)
=
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right).
\]

By Theorem 6,
\[
G_N\to G_\infty,
\qquad
T_{m,N}\to T_{m,\infty}.
\]
By Theorem 7,
\[
\mathcal R_N\to R_\infty.
\]
Therefore the continuum geometry is recovered as the limit of finite projected-flat apex geometries.

Define \(\widehat{\mathcal A}\) to consist of the compatible finite conductor data, the limiting Fisher/cumulant/curvature tensors, and the archimedean boundary term. Existence follows from the certificate assumptions.

For uniqueness, suppose \(\widehat{\mathcal A}'\) has the same finite conductor data, refinement limits, and archimedean boundary. Then its finite shadows agree at every \(N\), its limiting tensors agree with \(G_\infty,T_{m,\infty},R_\infty\), and its real-place Fourier-Mellin boundary agrees with \(\Gamma_\infty\). Hence all structural components agree, so
\[
\widehat{\mathcal A}'=\widehat{\mathcal A}
\]
up to the canonical equivalence of the chosen category of apex systems. \(\square\)

---

## 11. The archimedean fixed point

### Theorem 10. The Archimedean Fixed-Point Theorem

Let \(\mathcal A\) be a cofinal tower of finite apex systems. Define the finite-to-archimedean completion operator
\[
\widehat{(\cdot)}
\]
by adjoining:

1. all refinement limits;
2. all fusion-closure completions;
3. the archimedean boundary term required for Fourier-Mellin self-duality.

Then \(\widehat{(\cdot)}\) is an idempotent closure operator:
\[
\widehat{\widehat{\mathcal A}}=\widehat{\mathcal A}.
\]
Its fixed points are exactly the globally completed apex systems: those with no unresolved finite refinement boundary, no unresolved conductor-fusion boundary, and no missing archimedean boundary.

In the Dirichlet/Mellin case, the fixed-point completion is the completed \(L\)-object
\[
\Lambda(s,\chi)
=
q^{(s+\varepsilon)/2}
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right)
L(s,\chi),
\]
where the gamma factor is the real-place boundary required for self-duality.

**Proof.** Define completion in three stages.

First, apply refinement completion. This adjoins all compatible limits of the cofinal finite tower. By Theorems 1 and 2, old data pull back compatibly and new finite modes are exactly named as refinement boundaries. Once all refinement limits are adjoined, applying refinement completion again adds nothing.

Second, apply fusion closure at every finite level and along the limiting tower. By T13, fusion closure is an extensive, monotone, idempotent closure operator:
\[
\operatorname{Cl}_n(\operatorname{Cl}_n(S))=\operatorname{Cl}_n(S).
\]
Therefore once all conductor-fusion completions are adjoined, applying fusion closure again adds nothing.

Third, apply archimedean completion. By Theorem 4, a cofinal finite-prime tower still misses the real place. By Theorem 5, finite Fourier compatibility and Gaussian self-duality select a unique real-place boundary term, up to the standard phase normalization. Once this term is adjoined, global Fourier-Mellin self-duality has no missing real-place boundary. Applying archimedean completion again adds nothing.

The Discretization Certificate ensures these stages are compatible: refinement maps commute with finite apex structure, fusion closure commutes with refinement except at explicitly adjoined boundaries, and the archimedean term supplies the terminal boundary required for global self-duality. Hence their composite is idempotent:
\[
\widehat{\widehat{\mathcal A}}=\widehat{\mathcal A}.
\]

If
\[
\widehat{\mathcal A}=\mathcal A,
\]
then completion adds nothing. Therefore there is no unresolved finite refinement boundary, no unresolved conductor-fusion boundary, and no missing archimedean boundary; the Fisher/cumulant/curvature limits already exist and agree with the tower.

Conversely, if a tower has these properties, then each completion stage adds nothing, so
\[
\widehat{\mathcal A}=\mathcal A.
\]
Thus the fixed points of the completion operator are exactly the globally completed apex systems.

For Dirichlet/Mellin data, the bare finite Euler object \(L(s,\chi)\) is not a fixed point of Fourier-Mellin completion by itself, because it lacks conductor normalization and the real-place gamma boundary. The completed object
\[
\Lambda(s,\chi)
=
q^{(s+\varepsilon)/2}\Gamma_\infty(s,\varepsilon)L(s,\chi)
\]
with
\[
\Gamma_\infty(s,\varepsilon)
=
\pi^{-(s+\varepsilon)/2}
\Gamma\!\left(\frac{s+\varepsilon}{2}\right)
\]
includes the real-place boundary and is the object carrying the global functional-equation/self-duality relation. Therefore \(\Lambda\), not bare \(L\), is the fixed-point object. \(\square\)

---

## 12. The smooth primorial פ — the scalar archimedean completion

Theorems 9 and 10 stated completion and its fixed point for the full apex/\(L\)-object. Their simplest nontrivial instance is the **scalar** completion of the primorial magnitude carried by each tower level. We isolate it here and name it פ (Hebrew *pe*, for *primorial*).

### 12.1 Definition

Along the primorial tower \(N_k=\prod_{p\le p_k}p\), the scalar at each level is the primorial magnitude
\[
\operatorname{pri}_*(x)=\prod_{p\le x}p=e^{\vartheta(x)},
\qquad
\vartheta(x)=\sum_{p\le x}\log p,
\]
a step function — a pure finite-prime (Euler-product) object. Its finite-to-archimedean completion is the smooth function
\[
\boxed{\;פ(z):=\frac{e^{\operatorname{Li}^{-1}(z)}}{2\pi},\;}
\]
where \(\operatorname{Li}^{-1}\) inverts the logarithmic integral \(\operatorname{Li}(x)=\int_2^x dt/\log t\). We call פ the **smooth primorial**. Its analytic construction — closed form, Bohr–Mollerup and Wielandt uniqueness, Stirling-type decay, the divisor-lattice family, the constant tower, the translation orbit \(פ_p(z)=פ(z+\operatorname{Li}(p))\) — is carried out in T33. **T15 owns the completion meaning of פ; T33 owns its construction.**

### 12.2 The normalization is the archimedean boundary

**Proposition 12.1.** The constant \(1/(2\pi)\) in פ is exactly the archimedean boundary term of Theorems 4–5. In the explicit formula for the Chebyshev function,
\[
\psi_0(x)=\underbrace{x}_{s=1\text{ pole}}-\underbrace{\log(2\pi)}_{\text{archimedean}}-\underbrace{\sum_\rho\frac{x^\rho}{\rho}}_{\text{zeros}}-\tfrac12\log(1-x^{-2}),
\]
the constant \(\log(2\pi)=-\zeta'(0)/\zeta(0)\) is the real-place contribution, descending from \(\zeta'(0)=-\tfrac12\log(2\pi)\) — i.e. from the functional equation's \(\Gamma\)-factor. Hence
\[
פ(z)=\underbrace{e^{\operatorname{Li}^{-1}(z)}}_{\text{finite-prime main term}}\times\underbrace{\frac{1}{2\pi}}_{\text{archimedean boundary}},
\]
the scalar realization of this paper's slogan **finite conductor closure + real-place boundary = completion**. פ is the scalar shadow of the completed object \(\Lambda(s,\chi)\) of Theorem 10.

**Proof.** Theorem 4 identifies \(\Gamma_\infty\) as the real-place boundary; its scalar trace in the explicit formula is the constant \(-\zeta'(0)/\zeta(0)=\log(2\pi)\) (Titchmarsh §3). Exponentiating the non-oscillatory part of \(\psi_0\) gives \(e^{x}/(2\pi)\) on the prime side; the index-side reparameterization \(x\mapsto\operatorname{Li}^{-1}(z)\) (T33) gives פ. \(\square\)

### 12.3 The real place is not a finite packet — quantified

§13.4 below asserts that the archimedean place cannot be reduced to a finite prime packet. The smooth primorial turns this assertion into a computation.

**Proposition 12.2.** The discrete primorial sequence \((P_n)=1,2,6,30,210,\ldots\) is **not a moment sequence**: its Hankel determinants are
\[
D_0=1,\quad D_1=2,\quad D_2=24,\quad D_3=-787680<0.
\]
Hence no positive measure \(\mu\) satisfies \(P_n=\int_0^\infty t^n\,d\mu\), and פ admits no Mellin/integral representation \(\int_0^\infty t^{z-1}\,d\mu(t)\). (Computation: T33 §9A.5.)

**Interpretation.** A Mellin/moment representation is an *archimedean* object — an integral over \(\mathbb R^+\). The factorial has one, \(n!=\int_0^\infty t^n e^{-t}\,dt\), which is precisely why \(\Gamma\) exists and matches it exactly. The primorial does not. This is the analytic proof of §13.4: a pure finite-prime object **cannot generate its own real-place completion**; the archimedean factor \(\Gamma_\infty\) must be adjoined externally (Theorem 4) and cannot be recovered as a moment measure of finite-prime data. The obstruction \(D_3<0\) is the precise sense in which the real place is a terminal external boundary, not a finite packet. Equivalently: the completion theorem (Theorem 9) is not optional bookkeeping for the primorial — the scalar tower is provably non-self-completing, and פ exists only because the archimedean boundary is supplied from outside.

### 12.4 Refinement error budget

§14.2 asks for finite certificates of which conductor packets are missing at a primorial cutoff. פ supplies them. At cutoff \(P_n\), the primes certified prime by the level-\(n\) sieve are exactly those in the **certification window** \((p_n,\,p_{n+1}^2)\): a prime \(q\) enters the tower at refinement level \(\pi(\sqrt q)\) and is absorbed at level \(\pi(q)\) (T33 §9, §9A). The refinement boundary \(\mathcal D_{N_{k+1}}\setminus\mathcal D_{N_k}\) of Theorem 2 is thereby quantified by the growth of פ: \(\log פ(z)\sim\operatorname{Li}^{-1}(z)\), with the deviation from the discrete primorial controlled by the Riemann zeros (T33 §4.4).

---

## 13. What T15 does not claim

1. **It does not prove RH or GRH.** It explains why completed \(L\)-objects, gamma factors, and real-place terms appear as completion boundaries. Zeros require additional analytic input.

2. **It does not say every continuum model comes from cyclic finite apex systems.** It gives a precise route for closure-compatible finite towers and a diagnostic when a proposed discretization fails.

3. **It does not treat numerical convergence as automatic.** Fisher and tensor convergence are hypotheses to be certified.

4. **It does not reduce the archimedean place to a finite prime.** The real place is a terminal boundary, not another finite packet.

5. **It does not erase continuum analysis.** It reframes continuum structures as fixed points of finite closure plus real-place completion.

6. **It does not replace T16.** T15 owns continuum and archimedean completion. T16 will study learned representations and intelligence as closure-seeking finite systems.

---

## 14. Forward doors

### 14.1 Explicit completed apex functional equations

The next technical layer is to write the completed apex object whose finite conductor part and archimedean gamma boundary satisfy a precise functional equation.

### 14.2 Primorial error budgets

For \(N_k=\prod_{p\le p_k}p\), the refinement boundary
\[
\mathcal D_{N_{k+1}}\setminus\mathcal D_{N_k}
\]
can be measured. This gives finite certificates for which conductor packets are missing at a given primorial cutoff. This budget is now realized by the smooth primorial פ (§12.4): the certification window \((p_n,\,p_{n+1}^2)\) and the per-prime birth/death levels \(\pi(\sqrt q),\,\pi(q)\) give the explicit refinement budget (T33 §9).

### 14.3 Curvature convergence examples

T14 predicts curvature as boundary leakage. T15 asks for explicit examples where finite boundary curvature converges to known smooth curvature tensors.

### 14.4 Metaplectic packet transfer

The finite Fourier transfer of T9 and the metaplectic real-place transfer should be placed in one diagram.

### 14.5 Intelligence as finite completion pressure

T16 can now inherit a mature pattern: finite systems seek closure, boundaries become residuals, and completion is a fixed point. Learned representations are the next arena.

---

## 15. Coda

The finite-to-continuum bridge is no longer a vague limiting intuition. It has a structure:
\[
\text{refinement}
\quad+\quad
\text{fusion closure}
\quad+\quad
\text{archimedean boundary}
\quad=\quad
\text{completion}.
\]

The final compression is:
\[
\boxed{
\text{The continuum is the fixed point of finite closure at infinity.}
}
\]

---

## References and anchors

This draft uses standard facts from:

1. finite Fourier analysis on \(\mathbb Z/N\);
2. conductor packets and refinement by divisibility;
3. finite moment and apex algebra closure;
4. Poisson summation and self-dual Fourier normalization;
5. gamma factors in completed Dirichlet \(L\)-functions;
6. the metaplectic representation and Gaussian self-duality;
7. Fisher information and continuum information geometry;
8. curvature of projected flat connections;
9. closure operators on finite lattices;
10. the preceding lamed-series papers T0-T14.

Internal anchors:

| Object | Location |
|---|---|
| apex inverse system | Theorem 1 |
| refinement boundary | Theorem 2 |
| closure compatibility | Theorem 3 |
| archimedean boundary | Theorem 4 |
| metaplectic selection | Theorem 5 |
| continuum Fisher limit | Theorem 6 |
| curvature limit | Theorem 7 |
| discretization certificate | Theorem 8 |
| finite-to-archimedean completion | Theorem 9 |
| archimedean fixed point | Theorem 10 |
| smooth primorial פ (scalar completion) | §12 |

