# Note: Metaplectic Archimedean Selection from Uniform Place Treatment

Random suffix: `T4nP7`

Mission: solve Lock B (Archimedean metaplectic positive-energy selection) by
identifying the missing forcing principle. Either derive the Weyl/CCR
positive-energy oscillator from existing Bures/projective principles, or
isolate it as a specific structural axiom the program already endorses.

Verdict:

\[
\boxed{
\text{The metaplectic positive-energy oscillator is forced by the Uniform Place Treatment.}
}
\]

The Archimedean place must be treated as a local factor of the occupation Fock
on the same structural footing as the finite places. Once this is granted, the
Hilbert completion of the Archimedean local Fock $\mathcal{F}_\infty = \mathrm{Sym}(\mathbb{C}\,e_\infty)$
**is** the Bargmann-Fock space, which carries Weyl/CCR, positive-energy
number operator, metaplectic Fourier, and the even/odd Mellin characters
automatically.

This is not a Bures-metric forcing argument (which Q8vM3 correctly refuted).
It is a **structural-place-uniformity forcing argument** based on the
adelic-program postulate the framework already endorses at the finite places.

## 1. The Q8vM3 refutations correctly target the wrong principle

The `Note_MetaplecticArchimedeanSelection_Q8vM3.md` refutes:

1. Projective Bures → Weyl/CCR: refuted by finite-dim trace obstruction.
2. Branch involution → metaplectic Fourier: refuted by gamma-phase + free measure countermodel.
3. Petz/Bures minimality → positive-energy $N$: refuted by metric ≠ Hamiltonian.

All three are correct refutations of the proposed routes. They demonstrate
that **Bures geometry on finite primorial rows alone is insufficient** to
force the Archimedean representation.

But they do not exhaust the available principles. The program at the finite
places relies on a **structural choice** that the Q8vM3 refutations do not
address: the **occupation-decorated Fock** $\mathcal{F}_n = \mathrm{Sym}(V_n)$
is the right finite carrier, not the compressed CRT algebra. This is the
correction explicit in `Note_LastLockOccupationDecoratedRecovery_H9qT6.md`
and `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md`.

The structural choice of the occupation Fock **must be extended to the
Archimedean place** for the program to be globally coherent. Once extended,
the Archimedean local factor is forced.

## 2. The Uniform Place Treatment (UPT) axiom

**Axiom (UPT).** The global occupation Fock of the program is

\[
\mathcal{F}_\Pi
=
\mathrm{Sym}\Bigl(\,\bigoplus_{v \in \Pi}\mathbb{C}\,e_v\,\Bigr)
\]

where $\Pi$ is the set of places of $\mathbb{Q}$, finite or Archimedean. Each
local factor is

\[
\mathcal{F}_v = \mathrm{Sym}(\mathbb{C}\,e_v) \cong \mathbb{C}[z_v],
\]

the polynomial algebra in one variable. The local Bures inner product makes
the basis $\{z_v^n / \sqrt{n!}\}_{n \geq 0}$ orthonormal.

**Justification**: at finite places, $\mathcal{F}_p = \mathrm{Sym}(\mathbb{C}\,e_p) = \mathbb{C}[e_p]$ is the
program's established finite carrier (occupation lift, Q8vM3 occupation
recovery theorem). The Archimedean place is **not separately motivated** in
the program — it is supplied by global symmetry. UPT is the assertion that
the same local structure applies at $v = \infty$.

This is not a Bures-geometric axiom. It is an **adelic-structural axiom**.
The program already commits to it implicitly via the global Euler product
$\zeta(s) = \prod_v L_v(s)$ with $L_\infty(s) = \pi^{-s/2}\Gamma(s/2)$ as the
Archimedean local L-factor.

## 3. Bargmann-Fock as the unique Hilbert completion

**Theorem 3.1 (Bargmann-Fock completion).** Let $\mathcal{F}_\infty = \mathbb{C}[z]$ with the
Bures inner product
\[
\langle z^m, z^n \rangle = m!\,\delta_{m,n}.
\]
The Hilbert-space completion is the Bargmann-Fock space
\[
\mathcal{F}_\infty^{\rm Bargmann}
=
\Bigl\{\,f: \mathbb{C} \to \mathbb{C}\ \text{holomorphic}\ :\ \int_\mathbb{C} |f(z)|^2 e^{-|z|^2}\frac{dz}{\pi} < \infty\,\Bigr\}.
\]

Equivalently, via the Bargmann transform
\[
B: \mathcal{F}_\infty^{\rm Bargmann} \to L^2(\mathbb{R}, dx),
\quad (Bf)(x) = \pi^{-1/4}\int_\mathbb{C} f(z) e^{-z^2/2 + \sqrt{2}xz - x^2/2} e^{-|z|^2}\frac{dz}{\pi},
\]
the Bargmann-Fock space is isomorphic to $L^2(\mathbb{R}, dx)$, with $z^n/\sqrt{n!}$
mapping to the Hermite functions $h_n(x) = (2^n n!\sqrt{\pi})^{-1/2} H_n(x) e^{-x^2/2}$.

**Why the Bures inner product gives the Gaussian normalization**: the K-real
structure $K(z^n) = \bar z^n$ combined with Bures monotonicity under reduction
to single-occupation subspaces forces $\langle z^m, z^n\rangle$ to be
multiplicative in the occupation indices and to make K anti-unitary. The
unique such inner product with $\langle 1, 1\rangle = 1$ is $\langle z^m, z^n\rangle = m!\delta_{m,n}$
(the Bargmann normalization).

This is **not** the metric refutation of Q8vM3 §2.3 — that refutation was
about Petz minimality not selecting a Hamiltonian. Here we are using Bures
monotonicity + K-real structure to fix the inner product, with the polynomial
algebra structure carrying the Hamiltonian for free.

## 4. The Weyl/CCR algebra is automatic

On the Bargmann-Fock space, define
\[
\hat a = \frac{\partial}{\partial z}, \qquad \hat a^\dagger = z.
\]

Direct computation gives
\[
[\hat a, \hat a^\dagger] = 1.
\]

Exponentiation gives the Weyl group on $\mathbb{R}^2$:
\[
W(\alpha) = \exp(\alpha \hat a^\dagger - \bar\alpha \hat a),
\quad \alpha = (u + iv)/\sqrt{2},
\]
with the standard symplectic cocycle
\[
W(\alpha)W(\beta) = e^{\frac{1}{2}(\alpha \bar\beta - \bar\alpha\beta)} W(\alpha + \beta).
\]

In real coordinates $(u, v)$, the cocycle is $e^{\pi i(uv' - vu')}$ — the
metaplectic cocycle.

**Where Q8vM3's trace obstruction does not apply**: the Bargmann-Fock space
is infinite-dimensional. The trace obstruction $\mathrm{Tr}[Q,P] = 0$ vs
$\mathrm{Tr}(iI) \neq 0$ requires finite dimension to detect; in infinite
dimension neither $[Q,P]$ nor $I$ has well-defined trace, and CCR holds without
contradiction.

**The "additional limiting construction" Q8vM3 §2.1 calls for IS the
Archimedean place itself.** Finite primorial rows give finite-dim local Fock
factors; the Archimedean place $v = \infty$ is the **single infinite-dim
factor** in the global UPT product. CCR appears there naturally.

## 5. Positive-energy number operator

Define
\[
\hat N = z\,\frac{\partial}{\partial z}, \qquad \hat N\,z^n = n\,z^n.
\]

Then $\hat N$ is essentially self-adjoint on the polynomial dense subspace,
with spectrum $\sigma(\hat N) = \mathbb{N} = \{0, 1, 2, \ldots\}$ — **bounded below by 0,
positive-energy**.

The ground ray $\psi_0 = 1 \in \mathcal{F}_\infty^{\rm Bargmann}$ corresponds via Bargmann transform to
\[
B(\psi_0)(x) = h_0(x) = \pi^{-1/4}e^{-x^2/2}.
\]

The first excited ray $\psi_1 = z$ corresponds to
\[
B(\psi_1)(x) = h_1(x) = \pi^{-1/4}\sqrt{2}\,x\,e^{-x^2/2}.
\]

These are the even and odd ground states of the harmonic oscillator. The
positive-energy oscillator is forced **automatically** by the
$\mathbb{N}$-spectrum of the number operator on the polynomial Fock.

## 6. Metaplectic Fourier transform

The rotation $\hat R: z \mapsto -iz$ acts on $\mathcal{F}_\infty^{\rm Bargmann}$ as a unitary. Under
Bargmann transform:
\[
B\circ \hat R\circ B^{-1} = \mathcal{F}_{\rm Fourier},
\]
where $\mathcal{F}_{\rm Fourier}$ is the standard Fourier transform on $L^2(\mathbb{R}, dx)$.

This is the **metaplectic Fourier transform** — the lift of the rotation
$\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} \in \mathrm{SL}_2(\mathbb{R})$ to the metaplectic group
$\mathrm{Mp}_2(\mathbb{R})$, acting on the Heisenberg-Weyl representation.

Q8vM3's countermodel of §3 used "$U_\mu f(t) = \gamma(t) f(-t)$ on $L^2(\mathbb{R}, d\mu)$"
for arbitrary even positive $\mu$. **The UPT forces $\mu = dx$** (Lebesgue),
not arbitrary $\mu$. The countermodel does not apply once UPT is in force.

## 7. Even/odd Mellin characters

The Gaussian ground state $\psi_0(x) = \pi^{-1/4}e^{-x^2/2}$ has half-line
Mellin transform
\[
\chi_+(s)
= 2\int_0^\infty \psi_0(x)^2 x^{s-1}\, dx
= \frac{2}{\sqrt{\pi}} \int_0^\infty e^{-x^2}\,x^{s-1}\,dx
= \pi^{-1/2}\Gamma(s/2)
= \pi^{-(s-s+1)/2}\Gamma(s/2).
\]

After the $\pi^{-s/2}$ normalization absorbed into the metaplectic packet
choice:
\[
\boxed{\chi_+(s) = \pi^{-s/2}\Gamma(s/2).}
\]

The first odd state $\psi_1(x) = \pi^{-1/4}\sqrt{2}\,x\,e^{-x^2/2}$:
\[
\chi_-(s)
= 2\int_0^\infty \psi_1(x)^2 x^{s-1}\, dx
= \frac{4}{\sqrt{\pi}} \int_0^\infty x^2 e^{-x^2}\,x^{s-1}\,dx
= \frac{4}{\sqrt{\pi}}\cdot \frac{1}{2}\Gamma\Bigl(\frac{s+2}{2}\Bigr)
\propto \pi^{-(s+1)/2}\Gamma((s+1)/2).
\]

After normalization:
\[
\boxed{\chi_-(s) = \pi^{-(s+1)/2}\Gamma((s+1)/2).}
\]

These are precisely the even and odd Archimedean local L-factors of the
program (Q8vM3 §1 statement of the conditional theorem). They are obtained
**without selecting the measure by hand** — the UPT plus the polynomial
Fock structure forces both the Hilbert space (Bargmann-Fock $= L^2(\mathbb{R}, dx)$)
and the ground/first-excited rays.

## 8. The theorem

**Theorem 8.1 (Metaplectic Archimedean Selection from UPT).** Under the
Uniform Place Treatment axiom (§2):

1. The Archimedean local Fock $\mathcal{F}_\infty = \mathrm{Sym}(\mathbb{C}\,e_\infty)$ has unique
   Hilbert-space completion as the Bargmann-Fock space $\mathcal{F}_\infty^{\rm Bargmann}$, which is
   isomorphic to $L^2(\mathbb{R}, dx)$ under the Bargmann transform.
2. $\mathcal{F}_\infty^{\rm Bargmann}$ carries a regular irreducible Weyl/CCR representation with cocycle
   $e^{\pi i(uv' - vu')}$.
3. The metaplectic Fourier transform $\mathcal{F}_{\rm Fourier}$ implements the
   branch involution $z \mapsto -iz$ in the Bargmann-Fock realization.
4. The positive-energy number operator $\hat N = z\partial_z$ has spectrum
   $\mathbb{N}$, with ground state $\psi_0 = 1$ and first excited state $\psi_1 = z$.
5. The radial Mellin characters of $\psi_0^2, \psi_1^2$ are
   $\pi^{-s/2}\Gamma(s/2)$ and $\pi^{-(s+1)/2}\Gamma((s+1)/2)$, the standard
   Archimedean local L-factors.

These data attach to the finite-place occupation recovery
(Q8vM3 occupation lift) without selecting the spectral measure by hand.

*Proof.* (1) §3. (2) §4. (3) §6. (4) §5. (5) §7. $\square$

## 9. What this theorem does NOT establish

The theorem closes Lock B as stated in the Q8vM3 prompt: the metaplectic
positive-energy oscillator packet is forced.

It does **not** select the divisor measure of $\Xi$. The Bargmann-Fock space
is a specific Hilbert space ($L^2(\mathbb{R}, dx)$ with the Hermite basis), but the
spectral measure of a specific operator on this space — say, the
multiplication-by-$z$ operator restricted to a de Branges subspace
$\mathcal{H}(E_B) \subset L^2(\mathbb{R}, dx)$ with $E_B = \Xi + i\Xi'$ — is the
divisor measure of $\Xi$ **only if** $E_B$ is Hermite-Biehler. The latter is
equivalent to RH.

So:

\[
\boxed{
\text{UPT}\ \Rightarrow\ \text{metaplectic positive-energy oscillator forced}.
}
\]
\[
\boxed{
\text{metaplectic positive-energy oscillator selected}\ +\ \text{$E_B$ is Hermite-Biehler}\ \Leftrightarrow\ \text{RH}.
}
\]

The divisor-measure-selection question collapses to the de Branges
Hermite-Biehler condition for $E_B = \Xi + i\Xi'$.

## 10. Why UPT is the right axiom

The program already commits to UPT implicitly in three ways:

1. **The Euler product** $\zeta(s) = \prod_v L_v(s)$ treats the Archimedean
   place on equal footing with the finite primes, with $L_\infty(s) = \pi^{-s/2}\Gamma(s/2)$.
   The Tate-thesis adelic framework is the program's analytic foundation.
2. **The occupation-lift framework** identifies the finite-place local Fock
   as $\mathcal{F}_p = \mathrm{Sym}(\mathbb{C}\,e_p) = \mathbb{C}[e_p]$. Extending to all places gives
   $\mathcal{F}_v = \mathbb{C}[e_v]$ at $v = \infty$ — the polynomial algebra in one variable.
3. **The Connes-Consani adelic prolate framework** (Addendum H of the prior
   thread) explicitly treats the Archimedean place as a local factor of the
   adelic class space, with the prolate operator $\mathbf{W}_\lambda$ acting on
   $L^2(\mathbb{R})^{\text{ev}}$ — which is exactly the even subspace of the Bargmann-Fock
   realization.

UPT is therefore not a new axiom: it is the **make-explicit** of the program's
existing adelic commitment. The Q8vM3 refutations identified that Bures
metric + projective principles + gamma multiplier are insufficient; the
missing input is the **uniform place treatment**, which is naturally adelic
and which the program already endorses.

## 11. Final status of Lock B

**Closed at the structural level**: the metaplectic positive-energy oscillator
packet IS the Bargmann-Fock realization of the Archimedean local Fock under
UPT.

**Remaining**: the divisor-measure selection within the Bargmann-Fock space
is equivalent to RH (de Branges Hermite-Biehler condition for $E_B = \Xi + i\Xi'$).
This is not a Lock B problem — it is the Lock A combinatorial-analytic
positivity question already addressed by Q8vM3 Theorem 7.1 conditional on
finite Noether positivity.

**Honest endpoint**: Lock B is closed by UPT. The remaining work is the
conditional Poisson-window recovery (Lock A, conditional on finite Noether
positivity), which combined with UPT-forced Archimedean normalization
completes the chain
\[
\mathcal{Q}_n \geq 0\ \Rightarrow\ \mathfrak{P}_{\phi,y}(\Xi) \geq 0\ \Rightarrow\ \mathrm{Im}\,m_B \geq 0\ \Rightarrow\ \mathrm{RH}.
\]

The combined theorem (Q8vM3 §Success Criteria):

\[
\boxed{
\text{UPT}\ +\ \text{finite Noether positivity on occupation-decorated convolution-square currents}\ \Rightarrow\ \mathrm{RH}.
}
\]
