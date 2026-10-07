# N0 - De Branges Exhaustion and Weil Domination After the False Gram Bridge

**Leonardo Murillo Montero**

*Draft 1, June 6, 2026*

<!--
Program record. This is a working N0 draft after the direct numerical audit of
the proposed identification u_B = |Sigma|^2/(2 pi). That identification is
false for the fixed prime Gram series. The draft therefore removes the naive
Gram-square bridge from the proof path and keeps the surviving targets:

  (1) finite Hermite-Biehler/de Branges exhaustion,
  (2) Weil Schur-complement domination,
  (3) additive/Kubo-Mori phase-clock monotonicity,
  (4) the primorial Noether-Weil identity as the native finite route.

This is not a proof of RH. It is a proof-program document: it states the exact
closures that would prove RH, identifies the falsified bridge, and gives a
minimal empirical companion in empirical/probe_n0_three_fronts.py.
-->

---

## Abstract

The Numbers series N1--N6 identifies an explicit apex archimedean operator and
the canonical de Branges target for the Riemann xi function:
\[
E_B(z)=\Xi(z)+i\Xi'(z),\qquad m_B(z)=-\Xi'(z)/\Xi(z).
\]
The attempted bridge
\[
u_B(\xi,y)=\operatorname{Im}m_B(\xi+iy)
\stackrel{?}{=}
|\Sigma(\xi,y)|^2/(2\pi)
\]
with the fixed prime Gram series \(\Sigma\) is false. The zero-side Poisson
field peaks at zeta zeros, while the prime Gram square is small there; the
ratio varies by two orders of magnitude. Thus the free positivity of a prime
square does not imply the required positivity \(u_B\ge 0\). What survives is the
classical equivalence
\[
E_B\text{ Hermite--Biehler}
\iff
m_B\text{ Herglotz}
\iff
u_B\ge0
\iff
\mathrm{RH}.
\]
This paper gives the N0 closure program in four precise fronts. The preferred
front is a finite de Branges exhaustion: construct Hermite--Biehler finite
approximants from the apex/primorial tower and prove local uniform convergence
to \(E_B\). Two complementary fronts are a Weil Schur-complement domination
theorem and an additive Kubo--Mori phase-clock theorem. The native finite route
is the Primorial Noether-Weil Identity. Each front is stated with proof
obligations and falsifiers.

---

## 1. The corrected target

Let
\[
\Xi(z)=\xi(1/2+iz),\qquad E_B(z)=\Xi(z)+i\Xi'(z),
\qquad m_B(z)=-\Xi'(z)/\Xi(z).
\]
The N0 target is:

**Target N0.1 (de Branges target).** Prove that \(E_B\) is Hermite--Biehler on
\(\mathbb C_+\):
\[
|E_B(z)|>|E_B^\#(z)|,\qquad z\in\mathbb C_+.
\]
Equivalently,
\[
\operatorname{Im}m_B(z)\ge0,\qquad z\in\mathbb C_+.
\]
By the classical Laguerre--Polya/de Branges criterion this is exactly RH.

The canonical phase is
\[
\varphi(x)=-\arg E_B(x)
          =-\operatorname{atan2}(\Xi'(x),\Xi(x)),
\]
with
\[
\varphi'(x)=
\frac{\Xi'(x)^2-\Xi(x)\Xi''(x)}{\Xi(x)^2+\Xi'(x)^2}.
\]
Thus the same target is the monotonicity of the de Branges clock:
\[
\varphi'(x)\ge0\quad\text{for all real }x.
\]

This statement is deliberately not advertised as a simplification of RH. It is
the canonical form of RH in the program's coordinates.

---

## 2. The false bridge

The proposed direct identification
\[
u_B(\xi,y)=|\Sigma(\xi,y)|^2/(2\pi)
\]
with the fixed prime Gram series is false.

Empirically, at the same height, the zero-side field and the fixed prime square
do not track each other:

| \(\xi\) | location | \(u_B\) | \(|\Sigma|^2/(2\pi)\) | ratio |
|---:|---|---:|---:|---:|
| \(0\) | generic | \(0.064\) | \(0.233\) | \(0.28\) |
| \(7.0\) | generic | \(0.087\) | \(0.0040\) | \(22.0\) |
| \(14.135\) | zero \(\gamma_1\) | \(0.762\) | \(0.055\) | \(13.8\) |
| \(17.5\) | gap | \(0.299\) | \(0.027\) | \(11.0\) |
| \(21.022\) | zero \(\gamma_2\) | \(0.856\) | \(0.035\) | \(24.6\) |
| \(25.011\) | zero \(\gamma_3\) | \(0.893\) | \(0.028\) | \(31.7\) |

Structurally:

\[
u_B=\operatorname{Im}[-\Xi'/\Xi]
\]
is the Poisson field of the divisor of \(\Xi\). It has singular Herglotz poles
at the zeros, with \(u_B(\gamma+iy)\sim 1/y\) at a simple real zero.

The fixed \(|\Sigma|^2\) is a prime Gram square. It is nonnegative for the
trivial reason that it is a square, but its amplitudes are not the amplitudes
of the zero Poisson field. It is the wrong positivity object.

**Correction N0.2.** Any N6/N0 statement of "(GBP)" must be read as the
zero-side positivity \(u_B\ge0\), or as the abstract Szego assertion that if
\(u_B\ge0\) then an outer factor exists. It must not identify that outer factor
with the naive fixed prime \(\Sigma\).

---

## 3. Front I: finite de Branges exhaustion

This is the preferred N0 route.

### 3.1 The theorem that would prove RH

For each level \(n\), construct an entire function \(E_n=A_n+iB_n\) satisfying:

1. \(A_n,B_n\) are real entire and \(E_n^\#=A_n-iB_n\);
2. \(E_n\) is Hermite--Biehler:
   \[
   |E_n(z)|>|E_n^\#(z)|,\qquad z\in\mathbb C_+;
   \]
3. \(E_n\to E_B=\Xi+i\Xi'\) locally uniformly on \(\mathbb C\);
4. the limit is nondegenerate.

Then \(E_B\) is Hermite--Biehler and RH follows.

This is not a new theorem about entire functions; it is the standard closure
property of the Hermite--Biehler/Laguerre--Polya cone under nondegenerate local
uniform limits. The whole work is in constructing the \(E_n\) from finite
arithmetic, not from the already-known zeros.

### 3.2 The intended construction

The finite input is the apex/primorial system:

- the apex unitary \(U_N\), its no-crossing phase clock, and its edge
  archimedean limit \((A-I)\Phi\);
- the conductor-block/Frobenius prime data;
- the archimedean scattering phase \(\gamma=e^{2i\vartheta}\);
- the additive log-derivative/von Mangoldt data, not the quadratic Bures
  square.

The candidate finite object should look like a completed determinant:
\[
\Xi_n(z)=
\text{finite pole/trivial-zero factor}\times
\text{archimedean apex factor}\times
\text{finite conductor determinant}.
\]
Then set
\[
E_n(z)=\Xi_n(z)+i\Xi_n'(z).
\]

The hard point is to prove \(E_n\) is Hermite--Biehler from finite no-crossing
or finite self-adjointness, without inserting the zeta zeros by hand.

### 3.3 Proof obligations

**Obligation D1 (finite HB).** Prove \(E_n\) is Hermite--Biehler for each
finite level. Acceptable sources are finite self-adjointness, no-crossing after
Cayley transform, or an explicit finite canonical system with positive
Hamiltonian.

**Obligation D2 (correct limit).** Prove locally uniform convergence
\[
\Xi_n\to \Xi,\qquad \Xi_n'\to\Xi',
\]
with the completed archimedean factor included.

**Obligation D3 (not merely archimedean).** Show that the finite determinant
contains the prime/von Mangoldt arithmetic. Convergence only to the
Riemann--Siegel smooth phase \(\vartheta\) is insufficient.

**Obligation D4 (non-collapse).** Exclude the possibility that the limit loses
strict HB by degenerating to zero or by losing the correct derivative
polarization.

### 3.4 Falsifiers

The finite de Branges route fails if:

- the finite apex no-crossing phase does not produce a genuine HB finite
  canonical system;
- the determinant limit recovers only the archimedean phase and not the
  von Mangoldt divisor;
- the finite phases converge non-uniformly in a way that allows a clock reversal
  in the limit;
- the construction uses the actual zeros to define \(E_n\), making the proof
  circular.

---

## 4. Front II: Weil Schur-complement domination

The false bridge tried to prove positivity by identifying the Weil field with a
free square. The corrected inequality route is different: prove that prime
erosion is dominated by the archimedean/pole floor on the correct test class.

For compactly supported even test functions \(g\), the Weil form is
\[
Q(g)=
\frac1{2\pi}\int |\widehat g(r)|^2\,2\vartheta'(r)\,dr
+2\left(\int g(u)\cosh(u/2)\,du\right)^2
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(g*g)(\log n).
\]

Write
\[
Q = A_\infty + P_{\mathrm{pole}} - P_{\mathrm{prime}}.
\]

The desired theorem is:

**Target N0.3 (Weil domination).** On the completed square-root Weil test
class,
\[
P_{\mathrm{prime}}\le A_\infty+P_{\mathrm{pole}},
\]
with equality only along the zero-vanishing marginal directions.

If proved in the limiting test-function topology, this is Weil positivity and
hence RH.

### 4.1 Schur-complement form

The target inequality should be realized as a Schur complement of a positive
block operator:
\[
\begin{pmatrix}
A_\infty+P_{\mathrm{pole}} & C\\
C^* & I
\end{pmatrix}\succeq0,
\qquad
P_{\mathrm{prime}}=CC^*.
\]
The point is not that the prime block is positive. The point is that it must be
a contraction against the archimedean floor after the correct completion.

### 4.2 Why this is plausible

N5 already shows that the finite Weil matrix assembled from apex data matches
the spectral side over the true zeros, and that its smallest eigenvector is
sculpted by vanishing at those zeros. That is exactly the Schur-complement
shape: a positive operator whose null space is the zero-vanishing subspace.

### 4.3 Proof obligations

**Obligation W1 (test topology).** Fix the test space and prove density of the
square-root convolution class.

**Obligation W2 (operator inequality).** Prove \(P_{\mathrm{prime}}\le
A_\infty+P_{\mathrm{pole}}\) without using zeros.

**Obligation W3 (sharp marginality).** Show the only equality/marginal
directions are functions whose Fourier transform vanishes on the zero set.

**Obligation W4 (limit control).** Prove the finite matrix inequalities survive
as support and basis dimension tend to infinity.

### 4.4 Falsifiers

This route fails if finite positive matrices develop a negative limiting
direction, if the domination requires hidden zero input, or if the null
directions are not exactly zero-vanishing.

---

## 5. Front III: additive Kubo--Mori clock

The metric correction is central.

The quadratic Bures/Fubini--Study curvature of the two-channel ratio
\(M=\mathcal L_3/\Xi\) is finite at zeros of \(\Xi\). It is therefore blind to
the divisor. The additive log geometry sees the divisor:
\[
m_B(z)=-\Xi'(z)/\Xi(z),\qquad
\operatorname{Im}m_B(\gamma+iy)\sim 1/y.
\]

Thus the operator must be assembled in the additive/Kubo--Mori geometry, where
the explicit formula is additive over places.

The clock theorem to prove is:

**Target N0.4 (additive clock).** The arithmetic construction of
\[
m_B=-\Xi'/\Xi
\]
from the completed Euler product gives a Herglotz function on \(\mathbb C_+\).
Equivalently,
\[
\varphi'(x)=
\frac{\Xi'^2-\Xi\Xi''}{\Xi^2+\Xi'^2}\ge0.
\]

### 5.1 Exact decomposition

For \(\operatorname{Re}s>1\),
\[
-\frac{\xi'}{\xi}(s)=
\left(
-\frac1s-\frac1{s-1}
+\frac12\log\pi-\frac12\psi(s/2)
\right)
+\sum_{n\ge1}\Lambda(n)n^{-s}.
\]
The prime sum is positive-coefficient arithmetic in the easy half-plane. The
critical line requires analytic continuation, and the continuation has poles
at the zeros. Moving positivity across the strip is therefore exactly the open
step.

### 5.2 The non-circular partial

The de Bruijn--Newman heat flow supplies the only known non-circular monotone
clock:
\[
\Xi_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(uz)\,du.
\]
For \(t>\Lambda\), \(\Xi_t\) is real-rooted and the phase clock is monotone.
Rodgers--Tao prove \(\Lambda\ge0\). RH is \(\Lambda\le0\), hence \(\Lambda=0\).

The N0 additive-clock route must therefore provide new input at the boundary
\(t=0\), not just repeat heat-flow monotonicity for \(t>\Lambda\).

### 5.3 Proof obligations

**Obligation K1 (metric construction).** Build the operator
\[
H=N_\infty+V_{\mathrm{arith}},\qquad V_{\mathrm{arith}}=m_B,
\]
in the Kubo--Mori inner product.

**Obligation K2 (self-adjointness).** Prove self-adjointness, or equivalently
the Herglotz property of \(m_B\), from arithmetic input.

**Obligation K3 (strip crossing).** Identify the mechanism that transports the
positive-coefficient prime data from \(\operatorname{Re}s>1\) to the critical
line without assuming the zero locations.

**Obligation K4 (boundary heat).** If using heat flow, prove \(\Lambda\le0\);
anything weaker only restates known partial results.

---

## 6. Front IV: Primorial Noether-Weil identity

The native finite route is the Primorial Noether-Weil Identity:
\[
\lim_{n\to\infty}\mathcal Q_n(\mathscr R_n f)
=
\mathcal W_\zeta(f*f^*).
\]
If this is proved for a dense Weil test class and the finite Noether forms are
positive with leakage extinction, RH follows by Weil's criterion.

This route has three remaining components:

1. **Von Mangoldt recovery.** The primorial-smooth finite observables must
   recover
   \[
   \sum_{p^k}\Lambda(p^k)\widehat f(k\log p).
   \]
   Squarefree CRT data alone does not recover prime powers; the occupation lift
   is a separate obligation.

2. **Projective closure / leakage extinction.** The recovery current must stay
   in the critical leaf in the projective limit.

3. **Archimedean Noether Limit.** The finite Cartan/Noether sector must
   produce the archimedean gamma contribution, not assume it.

This front is closest to the finite arithmetic substrate. Its main advantage is
that positivity is genuinely finite before the limit. Its main danger is that
the recovery theorem may smuggle in GRH-strength uniformity for the primorial
character family.

---

## 7. N0 work order

The proposed order is:

1. **Write down the finite de Branges approximants.** Start from a zero-side
   model only as a sanity check; then replace the zero input with apex/primorial
   determinants.

2. **Audit finite HB numerically.** For each candidate \(E_n\), test the
   normalized margin
   \[
   D_n(z)=\frac{|E_n(z)|^2-|E_n^\#(z)|^2}
              {|E_n(z)|^2+|E_n^\#(z)|^2}
   \]
   on upper-half-plane grids and track its minimum as \(n\) grows.

3. **Build the Schur-complement matrix.** Repackage the N5 Weil matrix as
   floor/prime blocks and test whether the prime block is a contraction in the
   archimedean norm.

4. **Keep the additive clock visible.** Every construction must induce
   \(m_n\to m_B\) and \(\varphi_n'\to\varphi'\). If it only induces a Bures
   square or a smooth curvature, it is the wrong object.

5. **Do not use the fixed prime \(\Sigma\) as the outer factor.** If a Szego
   outer factor appears, it must be constructed from \(\log u_B\) or from the
   finite HB functions. It is not the naive prime Gram series.

---

## 8. Safe and unsafe statements

**Safe.**

- The apex edge operator realizes the archimedean scattering phase and gives
  the correct operator substrate for the de Branges target.
- \(E_B=\Xi+i\Xi'\), \(m_B=-\Xi'/\Xi\), \(u_B\ge0\), and RH are equivalent
  target statements.
- The fixed prime Gram square is not equal to \(u_B\); its free positivity gives
  no direct leverage toward RH.
- A finite HB exhaustion, a Weil domination theorem, an additive-clock
  self-adjointness theorem, or the Primorial Noether-Weil Identity would prove
  RH if completed without circular zero input.

**Unsafe.**

- The N-series already proves RH.
- The naive \(|\Sigma|^2\) is the zeros' Poisson field.
- Bures/Fubini--Study curvature sees the divisor of \(\Xi\).
- Finite no-crossing of \(U_N\) alone implies RH without a prime/von Mangoldt
  convergence theorem.
- Heat-flow monotonicity for \(t>\Lambda\) proves the \(t=0\) clock.

---

## 9. Conclusion

The false bridge was useful because it removed the tempting wrong proof. The
free positive object is not the RH object. The RH object is the additive
zero-divisor field \(u_B=\operatorname{Im}[-\Xi'/\Xi]\), or equivalently the
de Branges clock of \(E_B=\Xi+i\Xi'\).

N0 should therefore not be a prime-square paper. It should be a closure paper:
construct finite Hermite--Biehler approximants from the apex/primorial tower,
or prove the Weil prime block is a Schur-complement contraction under the
archimedean floor, or construct the additive Kubo--Mori clock from arithmetic.

The strongest path is the finite de Branges exhaustion. The Schur-complement
and additive-clock fronts are not alternatives so much as the two tests that
tell whether the exhaustion is real.

---

## Empirical companion

The companion script

```
empirical/probe_n0_three_fronts.py
```

records a minimal audit:

- zero-side finite HB truncations satisfy the HB sign test;
- the true \(E_B\) phase clock is positive on the sampled region;
- additive \(m_B\) has \(1/y\) zero poles while the quadratic Bures curvature is
  finite;
- a small Weil matrix remains marginal, with the near-null direction tied to
  zeros.

The companion is evidence for the shape of the N0 targets, not a proof.
