# RH Pass-2: Centered Gauge Theorems

**Leonardo Murillo Montero + Codex**

*Working note - May 24, 2026*

## Purpose

This note records the cleaner Pass-2 target produced by the T4
Helmert-simplicial residue ladder.

The goal is not to pretend that the Riemann Hypothesis has been proved
by a change of notation. The goal is to isolate the exact theorem-level
corrections that T4 forces on the Paper I--III RH-Done sequence.

The old Pass-1 obstruction was the Gram-Bures-Poisson identity

\[
\frac{|\Sigma(y,\xi)|^2}{2\pi}\,d\xi
\stackrel{?}{=}
u_B(\xi,y)\,d\xi,
\qquad
u_B(\xi,y)=\operatorname{Im}\left(-\frac{\Xi'}{\Xi}(\xi+iy)\right).
\]

Paper III correctly observes that this identity is generally false as
stated: the Gram side is a positive Bochner square built from
\(\sqrt{\Lambda}\), while the Bures side is the Poisson field of
\(-\Xi'/\Xi\), linear in the explicit-formula divisor.

T4 explains the structural reason: raw Gram positivity measures before
removing the shared simplicial gauge. The corrected objects are
centered covariance forms, pair-current coordinates, and the primorial
Helmert carrier.

---

## Theorem 1. Finite Centered Noether / Fisher Gauge Theorem

Let \(A\) be a finite index set and let \(w_a>0\) for \(a\in A\). Put

\[
W=\sum_{a\in A}w_a.
\]

Define the centered covariance operator

\[
C_w:=\operatorname{diag}(w)-\frac{1}{W}ww^T,
\]

where \(w\) is the column vector of weights. Then:

1. \(C_w\mathbf 1=0\).
2. \(C_w\) is positive semidefinite.
3. If all \(w_a>0\), then \(\ker C_w=\langle \mathbf 1\rangle\).
4. For every real vector \(g=(g_a)_{a\in A}\),

\[
g^T C_w g
=
\sum_a w_a(g_a-\bar g_w)^2
=
\frac{1}{2W}\sum_{a,b}w_aw_b(g_a-g_b)^2,
\]

where

\[
\bar g_w=\frac1W\sum_a w_ag_a.
\]

For complex \(g\), the Hermitian form is

\[
g^*C_w g
=
\sum_a w_a|g_a-\bar g_w|^2
=
\frac{1}{2W}\sum_{a,b}w_aw_b|g_a-g_b|^2
\ge 0.
\]

### Proof

The identity \(C_w\mathbf 1=0\) is immediate:

\[
\operatorname{diag}(w)\mathbf 1=w,\qquad
\frac1Www^T\mathbf 1=\frac1WwW=w.
\]

For the quadratic form,

\[
g^TC_wg
=
\sum_aw_ag_a^2-\frac1W\left(\sum_aw_ag_a\right)^2.
\]

Substituting \(\bar g_w=W^{-1}\sum_aw_ag_a\) gives

\[
\sum_aw_a(g_a-\bar g_w)^2.
\]

Expanding the pairwise expression gives the same value:

\[
\frac{1}{2W}\sum_{a,b}w_aw_b(g_a-g_b)^2
=
\sum_aw_ag_a^2-\frac1W\left(\sum_aw_ag_a\right)^2.
\]

The complex Hermitian version is identical with conjugates inserted.
Positivity follows. If all weights are positive, equality forces
\(g_a=\bar g_w\) for every \(a\), so \(g\in\langle\mathbf 1\rangle\).
\(\square\)

### Prime-Power Specialization

Let

\[
A_{n,K}=\{(p,r):p\le p_n,\ 1\le r\le K\},
\qquad
u_{p,r}=r\log p,
\]

and choose

\[
w_{p,r}(y)=(\log p)e^{-2y r\log p}.
\]

Then Theorem 1 gives a finite positive form

\[
\mathcal F_{n,K}^{\circ}(g;y)
=
\sum_{p,r}w_{p,r}(y)|g_{p,r}-\bar g_w|^2
\ge0,
\]

with the shared additive gauge removed.

For Fourier phases \(g_{p,r}=e^{-i\xi r\log p}\),

\[
\mathcal F_{n,K}^{\circ}(\xi;y)
=
W_{n,K}(y)
-
\frac{1}{W_{n,K}(y)}
\left|
\sum_{p\le p_n}\sum_{r\le K}
(\log p)e^{-(2y+i\xi)r\log p}
\right|^2.
\]

This is a genuine centered/Fisher-Noether finite positivity theorem.
It is closer to information geometry than the raw Gram square because
it is the covariance form

\[
\operatorname{diag}(w)-\frac1Www^T,
\]

the finite analogue of the categorical Fisher matrix

\[
\operatorname{diag}(p)-pp^T.
\]

---

## Theorem 2. Geometric-Mean Pair-Current Decomposition

Let

\[
\alpha_y=\sum_{a\in A}\sqrt{w_a}\,\delta_{u_a}
\]

be a square-root amplitude current on the height line. Its pair current is

\[
\Gamma_y:=\alpha_y\otimes \alpha_y
=
\sum_{a,b}\sqrt{w_aw_b}\,\delta_{(u_a,u_b)}.
\]

Introduce pair coordinates

\[
m=\frac{u+v}{2},\qquad d=u-v.
\]

Then:

1. The raw Gram / Bochner density is the Fourier transform of the
   \(d\)-pushforward of \(\Gamma_y\):

\[
\left|\sum_a\sqrt{w_a}e^{-i\xi u_a}\right|^2
=
\sum_{a,b}\sqrt{w_aw_b}e^{-i\xi(u_a-u_b)}.
\]

2. The diagonal \(d=0\) subcurrent is exactly the linear weight current:

\[
\Gamma_y\big|_{d=0}
=
\sum_a w_a\,\delta_{m=u_a}.
\]

3. In prime-power variables \(u_a=r\log p=\log(p^r)\), the pair
   coordinates are

\[
m=\frac{r\log p+r'\log p'}{2}
=
\log\operatorname{GM}(p^r,p'^{r'}),
\]

\[
d=r\log p-r'\log p'
=
\log\frac{p^r}{p'^{r'}}.
\]

Thus the Gram pair current naturally lives in
geometric-mean / ratio coordinates.

### Proof

The first identity is expansion of the absolute square. The change of
variables \((u,v)\mapsto(m,d)\) is invertible:

\[
u=m+\frac d2,\qquad v=m-\frac d2.
\]

The diagonal \(d=0\) is exactly the subset \(u=v\). Restricting
\(\Gamma_y\) to \(u=v\) forces \(a=b\) when the heights are distinct,
and gives weights \(\sqrt{w_a}\sqrt{w_a}=w_a\), located at
\(m=u_a\). The prime-power formulas are just logarithm laws. \(\square\)

### Consequence

The old Gram form compressed the pair current along the difference
coordinate \(d\) and discarded the geometric-mean coordinate \(m\).
The explicit-formula prime side is a linear current on the height
coordinate. It is recovered from the diagonal \(d=0\) section of the
pair current, not from the difference-only pushforward alone.

Therefore a Pass-2 transport theorem must keep the two-variable pair
geometry long enough to choose the correct gauge section. The
difference-only Bochner density cannot, by itself, be expected to equal
the Bures Poisson field.

---

## Theorem 3. Primorial Helmert Carrier Field Theorem

Let

\[
K_N=\mathbb Q(\sqrt p:p\le N,\ p\text{ prime})
\]

be the real multiquadratic field generated by the unit-normalization
constants of the Helmert-simplicial ladder through rung \(N\). Let

\[
L_6=\mathbb Q(\sqrt{-3})=\mathbb Q(\zeta_6)
\]

be the cyclotomic degree-2 field of the \(\mathbb Z/6\) Bures fiber
appearing in Paper I.

Then

\[
K_N\cap L_6=\mathbb Q,
\]

and the compositum

\[
\mathcal K_N:=K_NL_6
=
\mathbb Q(\sqrt{-3},\sqrt p:p\le N)
\]

has degree

\[
[\mathcal K_N:\mathbb Q]=2^{\pi(N)+1}.
\]

Moreover,

\[
\operatorname{Gal}(\mathcal K_N/\mathbb Q)
\cong
(\mathbb Z/2\mathbb Z)^{\pi(N)+1}.
\]

### Proof

The field \(K_N\) is totally real, since it is generated by square
roots of positive rational primes. The field \(L_6=\mathbb Q(\sqrt{-3})\)
is imaginary quadratic. Hence their intersection is a subfield of the
quadratic field \(L_6\) and is also totally real. The only totally real
subfield of the imaginary quadratic field \(L_6\) is \(\mathbb Q\).
Thus \(K_N\cap L_6=\mathbb Q\).

The square classes

\[
-3,\quad p\le N,\ p\text{ prime}
\]

are independent in \(\mathbb Q^\times/(\mathbb Q^\times)^2\): the
positive prime classes are independent, and the class \(-3\) includes
the sign class \(-1\), which is absent from the subgroup generated by
positive prime classes. Therefore adjoining these square roots gives a
multiquadratic extension of degree \(2^{\pi(N)+1}\), with elementary
abelian Galois group. \(\square\)

### Consequence

The \(\mathbb Z/6\) Bures fiber is a local cyclotomic gauge factor, not
the whole arithmetic carrier. The full Pass-2 carrier suggested by T4
is the primorial Helmert tower with this local Bures gauge adjoined:

\[
\mathcal K_N=\mathbb Q(\sqrt{-3},\sqrt p:p\le N).
\]

This does not replace the Paper I \(\mathbb Q(\sqrt{-3})\) mechanism.
It embeds it into a growing primorial metric-residue carrier.

---

## What These Theorems Do Not Prove

The three theorems above do not prove the Riemann Hypothesis.

They prove that the old Pass-1 target was comparing objects in the
wrong gauge:

1. Raw Gram positivity should be replaced by centered Fisher-Noether
   covariance positivity.
2. Difference-only Bochner transport should be lifted to the full
   geometric-mean / ratio pair current before choosing a gauge section.
3. The fixed \(\mathbb Z/6\) Bures fiber should be embedded into the
   primorial Helmert carrier rather than treated as the global carrier.

The remaining RH-strength statement would have to identify the Bures
Poisson field

\[
u_B(\xi,y)=\operatorname{Im}\left(-\frac{\Xi'}{\Xi}(\xi+iy)\right)
\]

as the positivity field of the corrected centered pair-current
construction, or prove its positivity by another argument. That is the
true Pass-2 target.

---

## Guardrail Theorem. The Simple Centered Phase Density Is Still Not \(u_B\)

The centered Fisher-Noether theorem gives a canonical positive finite
density for Fourier phases. It is tempting to declare this density the
new Bures Poisson field. That is still false.

For \(y>1/2\), define the absolutely convergent prime-power sums

\[
W_y:=\sum_{p,r\ge1}(\log p)e^{-2yr\log p}
=-\frac{\zeta'}{\zeta}(2y),
\]

and

\[
L_y(\xi):=\sum_{p,r\ge1}(\log p)e^{-(2y+i\xi)r\log p}
=-\frac{\zeta'}{\zeta}(2y+i\xi).
\]

The infinite centered phase-density suggested by Theorem 1 is

\[
V_y(\xi):=
W_y-\frac{|L_y(\xi)|^2}{W_y}.
\]

Then

\[
0\le V_y(\xi)\le W_y
\qquad\text{for all real }\xi.
\]

In contrast, under RH the Bures Poisson field has the Herglotz pole
expansion

\[
u_B(\xi,y)=\sum_{\gamma}
\frac{y}{(\xi-\gamma)^2+y^2},
\]

where \(\gamma\) ranges over the real ordinates of the non-trivial
zeros of \(\Xi\), with multiplicity. By the Riemann-von Mangoldt zero
density, its local average grows like

\[
u_B(\xi,y)\sim \frac12\log\frac{|\xi|}{2\pi}
\]

in the averaged Poisson sense as \(|\xi|\to\infty\). Hence \(u_B\) is
not bounded in \(\xi\), while \(V_y\) is bounded.

Therefore the simple centered covariance density \(V_y\) cannot equal
the Bures Poisson field \(u_B\).

### Meaning

Theorem 1 fixes the gauge error in the finite Noether form, but it is
not yet the RH-closing object. The correct Pass-2 object must include
the two-variable pair-current geometry and the Archimedean/divisor
normalization that produces the unbounded Herglotz field of \(\Xi\).

This guardrail prevents the false replacement

\[
|\Sigma|^2/(2\pi)=u_B
\]

from being reborn as the equally false replacement

\[
V_y=u_B.
\]

The real target remains a gauge-selected centered pair-current
identity, not a one-variable phase-variance identity.

---

## Theorem 4. Bures Pick-Kernel Identity

Let

\[
m_B(z):=-\frac{\Xi'(z)}{\Xi(z)}
\]

on the spectral upper half-plane away from zeros of \(\Xi\). Define the
Bures Pick kernel

\[
\mathcal K_B(z,w)
:=
\frac{m_B(z)-\overline{m_B(w)}}{z-\overline w}.
\]

Then for \(z=\xi+iy\), \(y>0\),

\[
\boxed{\;
u_B(\xi,y)
=
\operatorname{Im}m_B(\xi+iy)
=
y\,\mathcal K_B(\xi+iy,\xi+iy).
\;}
\]

Moreover, the following are equivalent:

1. \(u_B(\xi,y)\ge0\) for all \(\xi\in\mathbb R\), \(y>0\).
2. \(m_B\) is a Herglotz/Pick function on \(\mathbb C_+\).
3. The kernel \(\mathcal K_B\) is positive semidefinite on
   \(\mathbb C_+\):

\[
\sum_{i,j}c_i\overline{c_j}\mathcal K_B(z_i,z_j)\ge0
\]

   for every finite set \(z_i\in\mathbb C_+\) and coefficients \(c_i\).
4. The Riemann Hypothesis holds.

### Proof

For \(z=\xi+iy\),

\[
z-\overline z=2iy,
\]

and since \(m_B(\overline z)=\overline{m_B(z)}\) off the divisor by the
real-entire symmetry of \(\Xi\),

\[
\mathcal K_B(z,z)
=
\frac{m_B(z)-\overline{m_B(z)}}{z-\overline z}
=
\frac{2i\,\operatorname{Im}m_B(z)}{2iy}
=
\frac{u_B(\xi,y)}{y}.
\]

This proves the diagonal identity.

A holomorphic function maps \(\mathbb C_+\) to \(\overline{\mathbb C_+}\)
iff it is Herglotz/Pick. The Nevanlinna-Pick theorem gives the
equivalence between the Herglotz property and positive semidefiniteness
of the kernel \(\mathcal K_B\). Paper II Theorem T6.3 gives the
equivalence

\[
m_B\text{ Herglotz on }\mathbb C_+
\quad\Longleftrightarrow\quad
\mathrm{RH}.
\]

Thus all four statements are equivalent. \(\square\)

### Interpretation

The Bures Poisson field has now been identified as a positivity field:
it is the diagonal of the Bures Pick pair-current kernel.

But this does not lower the difficulty. It is the exact RH-strength
object. Proving positivity of \(\mathcal K_B\) or of its diagonal
\(u_B\) is precisely proving RH.

---

## Theorem 5. Bures Divisor Pair-Current Representation Under RH

Assume RH. Let

\[
\mu_\Xi:=\sum_{\gamma\in\Gamma}m_\gamma\,\delta_\gamma
\]

be the positive divisor measure of the spectral-coordinate completed
\(\Xi\), supported on the real zero ordinates \(\Gamma\) with
multiplicity \(m_\gamma\). Then

\[
m_B(z)=\int_{\mathbb R}\frac{d\mu_\Xi(t)}{t-z}
\]

in the standard symmetrized Hadamard/Stieltjes sense, and

\[
\mathcal K_B(z,w)
=
\int_{\mathbb R}
\frac{d\mu_\Xi(t)}{(t-z)(t-\overline w)}.
\]

Consequently,

\[
\boxed{\;
u_B(\xi,y)
=
y\int_{\mathbb R}
\frac{d\mu_\Xi(t)}{(t-\xi)^2+y^2}
\ge0.
\;}
\]

Conversely, if \(m_B\) admits such a representation by a positive
measure supported on \(\mathbb R\), then all zeros of \(\Xi\) are real,
hence RH holds.

### Proof

Under RH, every zero of the real entire even function \(\Xi\) lies on
the real spectral axis. The Hadamard product gives

\[
\Xi(z)=\Xi(0)\prod_{\gamma\in\Gamma_+}
\left(1-\frac{z^2}{\gamma^2}\right)^{m_\gamma},
\]

with symmetric convergence. Logarithmic differentiation yields

\[
-\frac{\Xi'(z)}{\Xi(z)}
=
\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z},
\]

again in the standard symmetrized sense. This is the displayed
Stieltjes representation.

Substituting into Theorem 4's kernel gives

\[
\frac{1}{z-\overline w}
\left[
\int\frac{d\mu_\Xi(t)}{t-z}
-
\int\frac{d\mu_\Xi(t)}{t-\overline w}
\right]
=
\int
\frac{d\mu_\Xi(t)}{(t-z)(t-\overline w)}.
\]

Taking \(w=z=\xi+iy\) gives

\[
u_B(\xi,y)
=
y\,\mathcal K_B(z,z)
=
y\int\frac{d\mu_\Xi(t)}{|t-z|^2}
=
y\int\frac{d\mu_\Xi(t)}{(t-\xi)^2+y^2}.
\]

This is nonnegative because \(\mu_\Xi\) is positive.

Conversely, if such a positive real-line measure represents \(m_B\),
then \(m_B\) is Herglotz and has no poles in \(\mathbb C_+\) away from
the real support. But poles of \(m_B=-\Xi'/\Xi\) are exactly zeros of
\(\Xi\). Therefore no zero of \(\Xi\) lies off the real spectral axis.
This is RH. \(\square\)

### Interpretation

This is the corrected centered pair-current construction in its
spectral form:

\[
\text{feature at }z:\quad
\kappa_z(t)=\frac{1}{t-z},
\]

\[
\mathcal K_B(z,w)=\langle \kappa_z,\kappa_w\rangle_{L^2(d\mu_\Xi)}.
\]

The Bures Poisson field is the diagonal squared length:

\[
u_B(\xi,y)=y\,\|\kappa_{\xi+iy}\|^2_{L^2(d\mu_\Xi)}.
\]

This is exactly the kind of centered pair-current positivity field
Pass-2 was seeking. The catch is unavoidable: the measure \(d\mu_\Xi\)
is positive on the real line iff RH holds.

---

## Theorem 6. Local-Pole Criterion for the Bures Positivity Field

Let

\[
m_B(z):=-\frac{\Xi'(z)}{\Xi(z)},\qquad
u_B(\xi,y):=\operatorname{Im}m_B(\xi+iy).
\]

Then the following are equivalent:

1. \(u_B(\xi,y)\ge0\) for every \(\xi\in\mathbb R\), \(y>0\).
2. \(m_B\) has no pole in \(\mathbb C_+\).
3. Every zero of \(\Xi\) lies on the real spectral axis.
4. RH holds.

When these equivalent conditions hold, \(u_B\) is the positivity field of
the Bures divisor pair-current:

\[
u_B(\xi,y)
=
y\,\|\kappa_{\xi+iy}\|^2_{L^2(d\mu_\Xi)},
\qquad
\kappa_z(t)=\frac1{t-z}.
\]

Equivalently,

\[
\mathcal K_B(z,w)
=
\langle \kappa_z,\kappa_w\rangle_{L^2(d\mu_\Xi)}
=
\int_{\mathbb R}\frac{d\mu_\Xi(t)}{(t-z)(t-\overline w)}
\]

is positive semidefinite, and \(u_B(\xi,y)=y\mathcal K_B(z,z)\).

### Proof

The poles of \(m_B=-\Xi'/\Xi\) are exactly the zeros of \(\Xi\). If
\(\rho=a+ib\), \(b>0\), is a zero of multiplicity \(m\), then near
\(\rho\)

\[
m_B(z)=\frac{m}{\rho-z}+O(1).
\]

Take \(z=a+i(b-\varepsilon)\), with \(0<\varepsilon<b\). Then

\[
\frac{m}{\rho-z}
=
\frac{m}{i\varepsilon}
=
-\frac{im}{\varepsilon},
\]

so

\[
\operatorname{Im}m_B(a+i(b-\varepsilon))
=
-\frac{m}{\varepsilon}+O(1)<0
\]

for sufficiently small \(\varepsilon\). Therefore positivity of \(u_B\)
on \(\mathbb C_+\) excludes every pole of \(m_B\) in \(\mathbb C_+\).

Conversely, if all zeros of \(\Xi\) lie on the real spectral axis, then
Theorem 5 gives the positive real-line divisor measure

\[
\mu_\Xi=\sum_\gamma m_\gamma\delta_\gamma
\]

and hence

\[
u_B(\xi,y)
=
y\int_{\mathbb R}\frac{d\mu_\Xi(t)}{(t-\xi)^2+y^2}
\ge0.
\]

Since \(\Xi\) is real entire in the spectral coordinate, non-real zeros
occur with their conjugates. Thus excluding upper-half-plane poles
excludes all non-real zeros. This is exactly RH. \(\square\)

### Meaning

This is the remaining RH-strength statement in its cleanest local form.
The Bures field is not the old difference-only Gram density. It is the
diagonal of the Bures divisor pair-current after the Bures gauge has
selected the spectral zero-divisor current.

The obstruction is now visible at microscope scale: a single off-line
zero creates a negative well immediately below its pole. Therefore any
non-circular proof of \(u_B\ge0\) must explain why the corrected
primorial/Archimedean centered pair-current converges to the real-line
divisor current \(d\mu_\Xi\), rather than to a divisor current with mass
in the upper half-plane.

---

## Summit Criterion. What Would Count as the Proof

Let \(\mathcal K_B\) be the Bures Pick kernel

\[
\mathcal K_B(z,w)
:=
\frac{m_B(z)-\overline{m_B(w)}}{z-\overline w},
\qquad
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}.
\]

Suppose one constructs, from the corrected centered primorial
pair-current with Archimedean normalization, a sequence of kernels

\[
\mathcal K_{n,T}^{\circ}(z,w)
\]

on \(\mathbb C_+\) satisfying:

1. **Finite positivity.** For every \(n,T\), the kernel
   \(\mathcal K_{n,T}^{\circ}\) is positive semidefinite:

\[
\sum_{i,j}c_i\overline{c_j}\mathcal K_{n,T}^{\circ}(z_i,z_j)\ge0.
\]

2. **Bures convergence.** For every compact
   \(C\subset\mathbb C_+\times\mathbb C_+\),

\[
\mathcal K_{n,T}^{\circ}(z,w)
\longrightarrow
\mathcal K_B(z,w)
\]

locally uniformly on \(C\), along a cutoff regime
\((n,T)\to\infty\).

Then RH follows.

### Proof

Positive semidefiniteness is closed under locally uniform limits on
finite Gram matrices. Therefore \(\mathcal K_B\) is positive
semidefinite on \(\mathbb C_+\). By Theorem 4, this is equivalent to
\(m_B\) being Herglotz/Pick, hence to

\[
u_B(\xi,y)=y\,\mathcal K_B(\xi+iy,\xi+iy)\ge0.
\]

By Theorem 6, this is equivalent to RH. \(\square\)

### Meaning

This is the exact summit route. The finite centered covariance theorem
already gives positive kernels; Theorem 2 explains why the raw
difference-only Gram density lost the needed geometric-mean coordinate.
The missing proof is the **Bures convergence theorem**: the corrected
primorial pair-current, after the right gauge section and Archimedean
normalization, must converge to \(\mathcal K_B\), not merely to a
bounded phase-variance density.

Victory is therefore not the slogan

\[
\text{positive finite objects} \Rightarrow \text{RH}.
\]

Victory is the precise bridge

\[
\boxed{
\mathcal K_{n,T}^{\circ}\succeq0
\quad\text{and}\quad
\mathcal K_{n,T}^{\circ}\to\mathcal K_B
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

The first half is finite information geometry. The second half is the
mountain.

---

## Theorem 7. Bures-Wronskian / de Branges Kernel Lift

Let

\[
A(z):=\Xi(z),
\qquad
m_B(z):=-\frac{A'(z)}{A(z)}.
\]

Define the entire two-variable Wronskian kernel

\[
\mathcal D_B(z,w)
:=
\frac{A(z)A'(\overline w)-A'(z)A(\overline w)}
{z-\overline w},
\]

with the diagonal interpreted by removable continuation. Then, away
from zeros of \(A\),

\[
\boxed{\;
\mathcal D_B(z,w)
=
A(z)A(\overline w)\,\mathcal K_B(z,w).
\;}
\]

Equivalently, if

\[
E(z):=A(z)+iA'(z),
\]

then \(\mathcal D_B\) is, up to the conventional positive constant, the
de Branges kernel of \(E\):

\[
K_E(z,w)
=
\frac{1}{\pi}\,\mathcal D_B(z,w).
\]

Consequently the following are equivalent:

1. \(\mathcal K_B\) is positive semidefinite on \(\mathbb C_+\).
2. \(\mathcal D_B\) is positive semidefinite on \(\mathbb C_+\).
3. \(E(z)=\Xi(z)+i\Xi'(z)\) is Hermite-Biehler.
4. RH holds.

### Proof

By definition,

\[
\mathcal K_B(z,w)
=
\frac{-A'(z)/A(z)+A'(\overline w)/A(\overline w)}
{z-\overline w}.
\]

Multiplying by \(A(z)A(\overline w)\) gives

\[
A(z)A(\overline w)\mathcal K_B(z,w)
=
\frac{A(z)A'(\overline w)-A'(z)A(\overline w)}
{z-\overline w}
=
\mathcal D_B(z,w).
\]

Positive semidefiniteness is unchanged by this nonzero diagonal
congruence on finite point sets away from zeros of \(A\), and the
general statement follows by continuation.

For \(E=A+iA'\), the real-entire conjugate is

\[
E^\#(z):=\overline{E(\overline z)}=A(z)-iA'(z).
\]

The de Branges kernel is

\[
K_E(z,w)
:=
\frac{E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}}
{2\pi i(\overline w-z)}.
\]

Expanding the numerator gives

\[
E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}
=
2i\bigl(A'(z)A(\overline w)-A(z)A'(\overline w)\bigr).
\]

Substitution gives

\[
K_E(z,w)=\frac1\pi\,\mathcal D_B(z,w).
\]

The Hermite-Biehler equivalence is the classical de Branges/Pólya
criterion for a real entire \(A\): \(A\) has only real zeros iff
\(A+iA'\) is Hermite-Biehler iff the de Branges kernel is positive on
\(\mathbb C_+\). For \(A=\Xi\), this is RH. \(\square\)

### Meaning

This removes the quotient noise. Instead of approximating the meromorphic
field \(m_B=-\Xi'/\Xi\) directly, Pass-2 can target the entire kernel

\[
\mathcal D_B(z,w)
=
\frac{\Xi(z)\Xi'(\overline w)-\Xi'(z)\Xi(\overline w)}
{z-\overline w}.
\]

This is the Bures positivity field with the divisor denominator
cleared. It is better suited to a centered pair-current construction:
the product terms \(\Xi(z)\Xi'(\overline w)\) and
\(\Xi'(z)\Xi(\overline w)\) are two-sided currents, and the division by
\(z-\overline w\) is the Wronskian normalization, not the dangerous
logarithmic quotient.

So the summit theorem may be sharpened:

\[
\boxed{
\mathcal D_{n,T}^{\circ}\succeq0,
\qquad
\mathcal D_{n,T}^{\circ}\to\mathcal D_B
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

This is the cleaner climb: prove convergence of entire Wronskian
kernels, then recover

\[
u_B(\xi,y)
=
y\,\frac{\mathcal D_B(\xi+iy,\xi+iy)}
{|\Xi(\xi+iy)|^2}.
\]

---

## Corollary 8. Real-Rooted Approximation Criterion

Let \(A_j(z)\) be real entire functions with only real zeros, and define

\[
\mathcal D_j(z,w)
:=
\frac{A_j(z)A_j'(\overline w)-A_j'(z)A_j(\overline w)}
{z-\overline w}.
\]

If

\[
A_j\longrightarrow \Xi
\]

locally uniformly on \(\mathbb C\), and the convergence is locally
uniform after one derivative as well, then

\[
\mathcal D_j\longrightarrow \mathcal D_B
\]

locally uniformly on \(\mathbb C\times\mathbb C\). Since every
\(\mathcal D_j\) is positive semidefinite on \(\mathbb C_+\), the limit
\(\mathcal D_B\) is positive semidefinite. Hence RH holds.

### Proof

Each \(A_j\) has only real zeros, so Theorem 7 applied to \(A_j\) gives
positive semidefiniteness of \(\mathcal D_j\). Local uniform convergence
of \(A_j\) and \(A_j'\) passes the Wronskian formula to the limit, so
\(\mathcal D_j\to\mathcal D_B\) locally uniformly. Positivity of finite
Gram matrices is closed under entrywise limits. Theorem 7 then gives
RH. \(\square\)

### Meaning

This is the classical Laguerre-Pólya route rewritten in Bures language.
It gives an equivalent form of the mountain:

\[
\boxed{
\Xi
\text{ is a local-uniform limit of real-rooted finite centered
primorial divisors}
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

So the corrected primorial pair-current must do more than produce a
positive density. It must produce a **real-rooted divisor approximation**
to \(\Xi\), or an equivalent positive Wronskian kernel approximation.

This is why the geometric-mean coordinate matters. A difference-only
Bochner square produces a positive Fourier density, but real-rootedness
is a two-sided divisor statement. It needs the pair-current before
collapsing:

\[
(u,v)
\quad\leftrightarrow\quad
\left(
m=\frac{u+v}{2},\ d=u-v
\right).
\]

The \(d\)-coordinate sees ratios. The \(m\)-coordinate carries the
geometric-mean placement of divisor mass. Losing \(m\) loses the ability
to reconstruct the real-rooted divisor approximation.

---

## Theorem 9. Hermite-Biehler Modulus Form of the Bures Field

Let

\[
A(z):=\Xi(z),
\qquad
E(z):=A(z)+iA'(z),
\qquad
E^\#(z):=\overline{E(\overline z)}=A(z)-iA'(z).
\]

Then, away from zeros of \(A\),

\[
\boxed{\;
u_B(z)
:=
\operatorname{Im}\left(-\frac{A'(z)}{A(z)}\right)
=
\frac{|E(z)|^2-|E^\#(z)|^2}{4|A(z)|^2}.
\;}
\]

Therefore

\[
u_B(z)\ge0
\quad\Longleftrightarrow\quad
|E(z)|\ge |E^\#(z)|
\qquad (z\in\mathbb C_+).
\]

Strict inequality off the real axis is the Hermite-Biehler condition,
and hence is equivalent to RH for \(A=\Xi\).

### Proof

Write \(B=A'\). Since \(E=A+iB\) and \(E^\#=A-iB\),

\[
|E|^2-|E^\#|^2
=
|A+iB|^2-|A-iB|^2.
\]

Expanding gives

\[
|A+iB|^2-|A-iB|^2
=
-4\,\operatorname{Im}(B\overline A).
\]

But

\[
u_B(z)
=
\operatorname{Im}\left(-\frac{B}{A}\right)
=
\operatorname{Im}\left(-\frac{B\overline A}{|A|^2}\right)
=
-\frac{\operatorname{Im}(B\overline A)}{|A|^2}.
\]

Combining the two identities yields the formula. The final equivalence
is the classical Hermite-Biehler criterion. \(\square\)

### Meaning

The Bures field is not merely a Poisson-looking scalar. It is the
normalized dominance gap between an entire function and its reflected
partner:

\[
\text{Bures positivity}
\quad\Longleftrightarrow\quad
\text{upper-half-plane dominance of }E=\Xi+i\Xi'.
\]

This gives the corrected centered pair-current target a very concrete
shape. A finite stage should produce a real entire or polynomial
\(A_{n,T}^{\circ}\), then

\[
E_{n,T}^{\circ}
:=
A_{n,T}^{\circ}+i(A_{n,T}^{\circ})',
\]

and prove the finite dominance

\[
|E_{n,T}^{\circ}(z)|
\ge
|(E_{n,T}^{\circ})^\#(z)|
\qquad (z\in\mathbb C_+)
\]

by centered pair-current positivity. If, in addition,
\(A_{n,T}^{\circ}\to\Xi\) locally uniformly with derivatives, the
dominance survives the limit and gives RH.

---

## Guardrail 10. Heat-Flow Real-Rootedness Is the Boundary, Not the Proof

Let \(\Phi\) denote the standard even rapidly decaying Fourier kernel
for \(\Xi\), so that

\[
\Xi(z)=\int_{-\infty}^{\infty}\Phi(t)e^{izt}\,dt.
\]

The de Bruijn-Newman deformation is

\[
H_\tau(z)
:=
\int_{-\infty}^{\infty}e^{\tau t^2}\Phi(t)e^{izt}\,dt,
\qquad
H_0=\Xi.
\]

There is a real constant \(\Lambda\), the de Bruijn-Newman constant,
such that

\[
H_\tau\text{ has only real zeros}
\quad\Longleftrightarrow\quad
\tau\ge\Lambda.
\]

RH is equivalent to

\[
\Lambda\le0.
\]

Newman's conjecture, now a theorem, gives

\[
\Lambda\ge0.
\]

Thus RH is equivalent to the boundary statement

\[
\boxed{\Lambda=0.}
\]

### Meaning

This explains why the real-rooted approximation criterion is powerful
but dangerous. It is easy to find nearby heat-deformed functions with
real zeros on the safe side of the heat flow. That does not prove RH.
The required proof must land exactly at the undeformed Bures object
\(H_0=\Xi\), or produce a different finite real-rooted approximation
whose limit is \(\Xi\) without adding heat that changes the target.

In the language of the program:

\[
\text{heat smoothing}
\ne
\text{simplicial gauge correction}.
\]

The centered primorial pair-current must correct the gauge while
preserving the target \(\Xi\). It cannot win by moving to a different
function \(H_\tau\) with \(\tau>0\).

---

## Theorem 11. Self-Adjoint Compression Criterion

Let \(H_j\) be finite-dimensional self-adjoint operators with real
eigenvalues \(\lambda_{j,k}\). Define

\[
A_j(z):=\det(H_j-zI)
=
\prod_k(\lambda_{j,k}-z)
\]

and

\[
m_j(z):=-\frac{A_j'(z)}{A_j(z)}
=
\operatorname{Tr}(H_j-zI)^{-1}
=
\sum_k\frac1{\lambda_{j,k}-z}.
\]

Then each \(m_j\) is Herglotz on \(\mathbb C_+\), because

\[
\operatorname{Im}m_j(\xi+iy)
=
\sum_k\frac{y}{(\lambda_{j,k}-\xi)^2+y^2}
\ge0.
\]

If

\[
m_j(z)\longrightarrow m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}
\]

locally uniformly on \(\mathbb C_+\), then \(m_B\) is Herglotz on
\(\mathbb C_+\), hence RH holds.

Equivalently, if normalized characteristic functions built from
self-adjoint \(H_j\) converge locally uniformly to \(\Xi\), then RH
holds.

### Proof

For finite self-adjoint \(H_j\), the spectral theorem gives the displayed
partial-fraction expansion. Each summand maps \(\mathbb C_+\) into
\(\mathbb C_+\), so \(m_j\) is Herglotz. The locally uniform limit of
Herglotz functions is Herglotz or degenerate. The asserted convergence
on every compact subset of \(\mathbb C_+\) already forces \(m_B\) to be
holomorphic on \(\mathbb C_+\); since \(m_B\) is nonconstant, it is
Herglotz. By Theorem 6, this is equivalent to RH.
\(\square\)

### Meaning

This is the operator version of Corollary 8. It gives the most concrete
Hilbert-Polya summit target:

\[
\boxed{
\text{construct finite self-adjoint centered primorial compressions }
H_{n,T}^{\circ}
\text{ with }
\operatorname{Tr}(H_{n,T}^{\circ}-zI)^{-1}
\to
-\Xi'(z)/\Xi(z).
}
\]

The centered pair-current is then not merely a positive scalar density.
It should be the finite spectral measure

\[
\mu_{n,T}^{\circ}
=
\sum_k \delta_{\lambda_{n,T,k}},
\]

with

\[
m_{n,T}^{\circ}(z)
=
\int_{\mathbb R}\frac{d\mu_{n,T}^{\circ}(t)}{t-z}.
\]

The Bures convergence theorem becomes weak/resolvent convergence:

\[
\mu_{n,T}^{\circ}
\Longrightarrow
\mu_\Xi
\quad\text{through Cauchy transforms.}
\]

This is the peak in operator language. The finite objects are positive
because they are self-adjoint. The unsolved content is to build them
from the corrected primorial/Archimedean centered pair-current and prove
that their resolvent trace is exactly the Bures limit.

---

## Theorem 12. Jensen-Hyperbolicity Ladder Criterion

Let

\[
\Xi(z)=\sum_{n=0}^{\infty}\frac{a_n}{n!}z^n
\]

be the Taylor expansion of the real entire spectral-coordinate xi
function. For \(n\ge0\) and \(d\ge1\), define the Jensen polynomial

\[
J_{\Xi}^{n,d}(X)
:=
\sum_{k=0}^{d}\binom{d}{k}a_{n+k}X^k.
\]

Then the following are equivalent:

1. RH holds.
2. \(\Xi\) belongs to the Laguerre-Pólya class.
3. Every Jensen polynomial \(J_{\Xi}^{n,d}\) is hyperbolic, meaning all
   of its zeros are real.
4. For every \(n,d\), \(J_{\Xi}^{n,d}\) is the characteristic polynomial
   of a finite self-adjoint compression.

### Proof

The equivalence between RH and \(\Xi\in\mathcal{LP}\) is the classical
Pólya-Laguerre characterization in spectral coordinates. The
Jensen theorem says that a real entire function is in the
Laguerre-Pólya class iff all of its Jensen polynomials are hyperbolic.
Finally, a polynomial with real zeros is the characteristic polynomial
of a finite self-adjoint operator: take the diagonal matrix with those
zeros, or any unitarily equivalent self-adjoint model. \(\square\)

### Meaning

This gives a finite ladder version of the mountain:

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\text{every finite Jensen coefficient ledger of }\Xi\text{ is
real-rooted.}
}
\]

This is not merely another equivalent statement. It is structurally
native to the simplicial program:

- the coefficient packet \((a_n,a_{n+1},\ldots,a_{n+d})\) is a finite
  ledger;
- hyperbolicity is finite self-adjointness;
- the Jensen transform is a finite binomial/Helmert-style rebalancing of
  the coefficient ladder;
- the infinite problem becomes preservation of real-rootedness at every
  finite rung.

Known asymptotic Jensen results say that for each fixed degree \(d\),
the high-\(n\) tail eventually becomes hyperbolic. In this language,
the far tail of each fixed finite rung already behaves like the Hermite
self-adjoint model. The remaining obstruction is global uniform control
as both \(n\) and \(d\) climb.

---

## Theorem 13. Finite Bures Gram-Matrix Criterion

For any finite set of spectral points

\[
Z=\{z_1,\ldots,z_N\}\subset\mathbb C_+,
\]

define the Bures-Wronskian Gram matrix

\[
G_B(Z)_{ij}
:=
\mathcal D_B(z_i,z_j)
=
\frac{\Xi(z_i)\Xi'(\overline{z_j})
-\Xi'(z_i)\Xi(\overline{z_j})}
{z_i-\overline{z_j}}.
\]

Then RH is equivalent to

\[
G_B(Z)\succeq0
\]

for every finite \(Z\subset\mathbb C_+\).

### Proof

This is Theorem 7 restricted to finite Gram matrices. Positive
semidefiniteness of the kernel \(\mathcal D_B\) means exactly positivity
of all such finite matrices. By Theorem 7, this is equivalent to
Hermite-Biehler dominance for \(E=\Xi+i\Xi'\), hence to RH. \(\square\)

### Meaning

This is the point-sampling version of the same mountain. It gives a
finite detector family:

\[
\det G_B(Z)\ge0,\qquad
\text{all principal minors, all finite }Z\subset\mathbb C_+.
\]

The Jensen ladder tests coefficient packets. The Bures Gram tests
spectral point packets. They are dual finite faces of the same
Laguerre-Pólya condition.

The corrected centered pair-current should explain why these finite
matrices are limits of manifestly positive centered primorial matrices.
That is the concrete Pass-3 convergence theorem.

---

## Theorem 14. Hermite-Moment Matrix Form of the Jensen Ladder

Let

\[
P(X)=c_dX^d+c_{d-1}X^{d-1}+\cdots+c_0
\]

be a real polynomial of degree \(d\), with complex roots
\(\alpha_1,\ldots,\alpha_d\) counted with multiplicity. Define the
Newton sums

\[
s_m(P):=\sum_{\ell=1}^{d}\alpha_\ell^m,
\qquad m\ge0,
\]

which are computable from the coefficients by Newton's identities.
Define the Hermite moment matrix

\[
\mathsf H(P):=
\bigl(s_{i+j}(P)\bigr)_{i,j=0}^{d-1}.
\]

Then \(P\) has only real zeros iff

\[
\mathsf H(P)\succeq0.
\]

Consequently, RH is equivalent to

\[
\mathsf H\!\left(J_{\Xi}^{n,d}\right)\succeq0
\qquad
\text{for every }n\ge0,\ d\ge1.
\]

### Proof

If all roots are real, then for any coefficient vector
\(q=(q_0,\ldots,q_{d-1})\),

\[
q^T\mathsf H(P)q
=
\sum_{i,j}q_iq_j s_{i+j}
=
\sum_{\ell=1}^{d}
\left(\sum_i q_i\alpha_\ell^i\right)^2
\ge0.
\]

Conversely, Hermite's theorem on real-root counting states that the
signature of \(\mathsf H(P)\) records the number of real roots, counted
with the appropriate multiplicity convention; in particular
\(\mathsf H(P)\succeq0\) iff no non-real conjugate pair contributes an
indefinite direction. Hence \(P\) is hyperbolic. Applying this to every
Jensen polynomial and using Theorem 12 gives the RH equivalence.
\(\square\)

### Meaning

This is the coefficient-side positive-current form:

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\text{every Jensen coefficient packet produces a positive Hermite
moment matrix.}
}
\]

Now the program has three equivalent finite positivity faces:

\[
\begin{array}{c}
\text{Bures Pick/Wronskian Gram matrices} \\
\text{Jensen hyperbolic polynomial ledgers} \\
\text{Hermite moment matrices from coefficient packets}
\end{array}
\]

The third form is especially compatible with T4. It says the missing
positivity is not a vague analytic aura; it is a concrete finite matrix
positivity statement built from coefficient ledgers after binomial
rebalancing.

The next non-circular task is therefore:

\[
\boxed{
\text{derive }
\mathsf H\!\left(J_{\Xi}^{n,d}\right)\succeq0
\text{ from centered primorial/Archimedean cumulant geometry.}
}
\]

That would turn the simplicial cumulant ladder into the Jensen
hyperbolicity ladder, and the Jensen ladder into RH.

---

## Theorem 15. Even-Fold Total-Positivity Criterion

Because \(\Xi\) is even, define the folded entire function

\[
\Theta(x):=\Xi(i\sqrt{x}).
\]

Equivalently, if

\[
\Xi(z)=\sum_{n=0}^{\infty}c_n z^{2n},
\]

then

\[
\Theta(x)=\sum_{n=0}^{\infty}b_nx^n,
\qquad
b_n:=(-1)^n c_n.
\]

Then RH is equivalent to the statement that \(\Theta\) has all its zeros
on the negative real axis. In that case

\[
\Theta(x)=\Xi(0)\prod_{\gamma>0}
\left(1+\frac{x}{\gamma^2}\right),
\]

where \(\gamma\) ranges over the positive spectral ordinates of the
non-trivial zeros.

Let \(b_n=0\) for \(n<0\), and form the infinite Toeplitz coefficient
ledger

\[
\mathsf T_\Theta:=
\bigl(b_{j-i}\bigr)_{i,j\ge0}.
\]

Then RH is equivalent to total positivity of this ledger:

\[
\boxed{\;
\text{every finite minor of }\mathsf T_\Theta\text{ is nonnegative.}
\;}
\]

### Proof

If RH holds, the Hadamard product of the even real entire function
\(\Xi\) is

\[
\Xi(z)=\Xi(0)\prod_{\gamma>0}
\left(1-\frac{z^2}{\gamma^2}\right).
\]

Substituting \(z=i\sqrt{x}\) gives

\[
\Theta(x)=\Xi(0)\prod_{\gamma>0}
\left(1+\frac{x}{\gamma^2}\right),
\]

so all zeros of \(\Theta\) are negative real numbers. Conversely, if all
zeros of \(\Theta\) are negative real numbers, then every zero of
\(\Xi(z)=\Theta(-z^2)\) lies on the real \(z\)-axis. This is RH.

The Aissen-Schoenberg-Whitney-Edrei theorem says that an entire
ordinary generating function has only real nonpositive zeros exactly
when its coefficient sequence is a Pólya-frequency sequence of infinite
order, equivalently when the Toeplitz matrix
\(\mathsf T_\Theta=(b_{j-i})\) is totally positive. Applying this to
\(\Theta\) gives the criterion. \(\square\)

### Meaning

This is the most finite-ledger formulation so far:

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\Theta(x)=\Xi(i\sqrt{x})
\text{ has a totally positive coefficient ledger.}
}
\]

The Bures/Pick route tests positivity by spectral points. The Jensen
route tests positivity by hyperbolic coefficient packets. The folded
Pólya-frequency route tests positivity by **all minors of one Toeplitz
ledger**.

This is extremely compatible with the simplicial language:

- \(b=(b_0,b_1,b_2,\ldots)\) is an infinite coefficient ray;
- finite Toeplitz minors are finite simplicial packets;
- total positivity is positivity preserved under every finite
  coordinate projection;
- the negative-real zero condition is the one-dimensional shadow of the
  real-spectral-zero condition for \(\Xi\).

So the Pass-3 target can be sharpened again:

\[
\boxed{
\text{derive total positivity of }\mathsf T_\Theta
\text{ from the centered primorial/Archimedean cumulant ledger.}
}
\]

This would bypass pointwise Poisson positivity and prove the
Laguerre-Pólya condition directly on the folded coefficient ray.

---

## Theorem 16. Folded Divisor-Cumulant Hankel Test

Normalize the folded function by

\[
B(x):=\frac{\Theta(x)}{\Theta(0)}
=
1+\sum_{n\ge1}p_nx^n.
\]

Define its logarithmic divisor cumulants \(\ell_m\) by

\[
\log B(x)
=
\sum_{m\ge1}(-1)^{m+1}\frac{\ell_m}{m}x^m.
\]

Equivalently,

\[
\ell_m
=
(-1)^{m+1}m[x^m]\log B(x).
\]

If RH holds, then

\[
\ell_m=\sum_{\gamma>0}\gamma^{-2m},
\qquad m\ge1.
\]

Consequently the shifted cumulant sequence

\[
r_n:=\ell_{n+1},\qquad n\ge0,
\]

is a Stieltjes moment sequence:

\[
r_n=\int_0^\infty t^n\,d\sigma(t),
\qquad
d\sigma(t)=\sum_{\gamma>0}\gamma^{-2}\delta_{\gamma^{-2}}(t).
\]

Therefore every Hankel matrix

\[
\mathsf M_k^{(0)}
:=
\bigl(r_{i+j}\bigr)_{i,j=0}^{k}
\]

and every shifted Hankel matrix

\[
\mathsf M_k^{(1)}
:=
\bigl(r_{i+j+1}\bigr)_{i,j=0}^{k}
\]

is positive semidefinite.

### Proof

Under RH, Theorem 15 gives

\[
B(x)=\prod_{\gamma>0}\left(1+\frac{x}{\gamma^2}\right).
\]

Taking the logarithm,

\[
\log B(x)
=
\sum_{\gamma>0}\log\left(1+\frac{x}{\gamma^2}\right)
=
\sum_{\gamma>0}\sum_{m\ge1}
(-1)^{m+1}\frac{x^m}{m\gamma^{2m}},
\]

with the usual local convergence near \(x=0\). Comparing coefficients
gives

\[
\ell_m=\sum_{\gamma>0}\gamma^{-2m}.
\]

For \(r_n=\ell_{n+1}\),

\[
r_n
=
\sum_{\gamma>0}\gamma^{-2n-2}
=
\int_0^\infty t^n\,d\sigma(t),
\qquad
d\sigma(t)=\sum_{\gamma>0}\gamma^{-2}\delta_{\gamma^{-2}}(t).
\]

Stieltjes moment sequences have positive ordinary and shifted Hankel
matrices, proving the claim. \(\square\)

### Meaning

The folded coefficient ray has two coordinate systems:

\[
\text{coefficient ledger }(p_1,p_2,\ldots)
\quad\longleftrightarrow\quad
\text{divisor cumulant ledger }(\ell_1,\ell_2,\ldots).
\]

The first is elementary-symmetric data of the folded zero divisors. The
second is power-sum data. Newton identities move between them:

\[
\ell_1=p_1,\qquad
\ell_2=p_1^2-2p_2,\qquad
\ell_3=p_1^3-3p_1p_2+3p_3,\quad\ldots
\]

This is exactly the kind of coefficient/cumulant duality T2 prepared:

\[
\log B
\quad\text{is the effective action,}
\qquad
\ell_m
\quad\text{are its divisor cumulants.}
\]

But this theorem is deliberately one-way. Hankel positivity of the
divisor cumulants is necessary under RH; by itself it is not yet
sufficient for RH, because a moment sequence does not automatically
reconstruct an entire function with an integer atomic divisor. The full
sufficient condition is total positivity of the Toeplitz coefficient
ledger from Theorem 15.

---

## Theorem 17. Folded PF Limit Criterion

Suppose there exists a sequence of polynomials

\[
B_j(x)=1+\sum_{n=1}^{N_j}p_{j,n}x^n
\]

such that:

1. every \(B_j\) has all zeros on the negative real axis;
2. \(B_j\to B=\Theta/\Theta(0)\) locally uniformly on \(\mathbb C\).

Then RH holds.

Equivalently, suppose the coefficient ledgers \(p^{(j)}\) are finite
Pólya-frequency sequences of infinite order, and their generating
polynomials converge locally uniformly to \(B\). Then the limiting
coefficient ledger of \(B\) is \(PF_\infty\), so RH holds.

### Proof

The class of entire functions obtained as local-uniform limits of
polynomials with only real nonpositive zeros is closed. Hence \(B\) has
only real nonpositive zeros. Since \(B(x)=\Theta(x)/\Theta(0)\), Theorem
15 gives RH. Equivalently, finite \(PF_\infty\) coefficient ledgers have
totally positive Toeplitz matrices, and total positivity of every finite
minor survives coefficientwise limits. \(\square\)

### Meaning

This is the folded version of the summit theorem:

\[
\boxed{
\text{finite centered primorial cumulant ledgers}
\longrightarrow
PF_\infty\text{ polynomials}
\longrightarrow
B(x)=\Theta(x)/\Theta(0)
\longrightarrow
\mathrm{RH}.
}
\]

This is now the cleanest victory path in coefficient language. We do not
need to push a signed explicit-formula distribution directly into
\(u_B\). We can instead build finite folded coefficient ledgers that are
already total-positive, prove local-uniform convergence to the folded
\(\Xi\), and let the Aissen-Schoenberg-Whitney-Edrei theorem carry the
last step.

The remaining mathematical task is exact:

\[
\boxed{
\text{construct }B_{n,T}^{\circ}\text{ from the centered
primorial/Archimedean cumulant ledger, prove }B_{n,T}^{\circ}\in
PF_\infty,\text{ and prove }B_{n,T}^{\circ}\to B.
}
\]

---

## Theorem 18. Positive Fredholm Determinant Criterion

Let

\[
B(x):=\frac{\Theta(x)}{\Theta(0)}
=
\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

RH is equivalent to the existence of a positive trace-class operator
\(L_\Xi\ge0\) such that

\[
\boxed{\;
B(x)=\det(I+xL_\Xi).
\;}
\]

When RH holds, one may take \(L_\Xi\) to be the diagonal positive
operator with eigenvalues

\[
\alpha_\gamma:=\gamma^{-2},
\qquad \gamma>0,
\]

where \(\gamma\) ranges over the positive spectral ordinates of the
zeros of \(\Xi\), counted with multiplicity.

Moreover, if finite positive operators \(L_j\ge0\) satisfy

\[
\det(I+xL_j)\longrightarrow B(x)
\]

locally uniformly on \(\mathbb C\), then RH holds.

### Proof

If RH holds, Theorem 15 gives

\[
B(x)=\prod_{\gamma>0}\left(1+\frac{x}{\gamma^2}\right).
\]

The Riemann-von Mangoldt zero count implies

\[
\sum_{\gamma>0}\gamma^{-2}<\infty,
\]

so the diagonal operator with eigenvalues \(\gamma^{-2}\) is positive
trace-class. Its Fredholm determinant is exactly the displayed product.

Conversely, if \(B(x)=\det(I+xL_\Xi)\) for a positive trace-class
operator, then

\[
B(x)=\prod_k(1+\lambda_k x),
\qquad \lambda_k\ge0,
\]

so every zero of \(B\) is real and nonpositive. By Theorem 15, RH holds.

The finite-operator convergence statement follows because every
\(\det(I+xL_j)\) has all zeros real and nonpositive, and this property is
closed under local-uniform limits. \(\square\)

### Cumulant Form

For a positive trace-class \(L\),

\[
\log\det(I+xL)
=
\sum_{m\ge1}(-1)^{m+1}\frac{\operatorname{Tr}(L^m)}{m}x^m.
\]

Thus the folded divisor cumulants are operator traces:

\[
\ell_m=\operatorname{Tr}(L_\Xi^m).
\]

Finite stages become

\[
B_j(x)=\det(I+xL_j),
\qquad
\ell_m^{(j)}=\operatorname{Tr}(L_j^m).
\]

### Meaning

This is the strongest operator-coefficient form of the mountain:

\[
\boxed{
\text{build positive finite-rank operators }L_{n,T}^{\circ}
\text{ from the centered primorial cumulant ledger}
}
\]

such that

\[
\det(I+xL_{n,T}^{\circ})
\longrightarrow
\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Then RH follows.

This is cleaner than seeking the zeros directly. The zeros become
eigenvalues of a positive operator after folding:

\[
\gamma
\quad\longmapsto\quad
\gamma^{-2}.
\]

The Bures positivity field, the Jensen ladder, the Toeplitz total
positivity, and the positive Fredholm determinant are now four views of
the same target:

\[
\begin{array}{c}
u_B\ge0 \\
\mathcal D_B\succeq0 \\
\mathsf T_\Theta \text{ totally positive} \\
B(x)=\det(I+xL_\Xi),\ L_\Xi\ge0
\end{array}
\qquad\Longleftrightarrow\qquad
\mathrm{RH}.
\]

The primorial program's victory condition can now be stated with no
poetic fog:

\[
\boxed{
\text{the centered primorial/Archimedean cumulant tower must converge
to a positive trace-class determinant model for }\Theta.
}
\]

---

## Theorem 19. Archimedean Moment Ledger of the Folded Xi

Let \(\Phi(t)\) be the standard even real kernel in the Fourier
representation of the spectral xi function:

\[
\Xi(z)=\int_{-\infty}^{\infty}\Phi(t)e^{izt}\,dt
=
2\int_0^\infty \Phi(t)\cos(zt)\,dt.
\]

The kernel \(\Phi\) is positive and rapidly decreasing. Therefore the
folded function

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

has the unconditional representation

\[
\boxed{\;
B(x)
=
\int_{-\infty}^{\infty}\cosh(\sqrt{x}\,t)\,d\nu(t),
\;}
\]

where

\[
d\nu(t):=\frac{\Phi(t)\,dt}{\int\Phi(t)\,dt}
\]

is a probability measure. Consequently

\[
B(x)=\sum_{n=0}^{\infty}b_nx^n,
\qquad
b_n=\frac{1}{(2n)!}\int t^{2n}\,d\nu(t)>0.
\]

Thus the scaled coefficient ledger

\[
m_n:=(2n)!\,b_n
\]

is an even moment sequence:

\[
m_n=\int t^{2n}\,d\nu(t).
\]

In particular, for every \(k\ge0\),

\[
\bigl(m_{i+j}\bigr)_{i,j=0}^{k}\succeq0.
\]

### Proof

Substitute \(z=i\sqrt{x}\) into the Fourier representation:

\[
\Xi(i\sqrt{x})
=
\int\Phi(t)e^{-\sqrt{x}t}\,dt.
\]

Since \(\Phi\) is even, the odd part cancels and this is

\[
\int\Phi(t)\cosh(\sqrt{x}\,t)\,dt.
\]

Dividing by \(\Xi(0)=\int\Phi(t)\,dt\) gives the probability-measure
representation. Expanding

\[
\cosh(\sqrt{x}\,t)
=
\sum_{n=0}^{\infty}\frac{t^{2n}}{(2n)!}x^n
\]

and exchanging summation and integration, justified by rapid decay,
gives the coefficient formula.

For any real vector \(q=(q_0,\ldots,q_k)\),

\[
\sum_{i,j}q_iq_jm_{i+j}
=
\int\left(\sum_iq_it^{2i}\right)^2d\nu(t)\ge0.
\]

So the Hankel matrices of \(m_n\) are positive. \(\square\)

### Meaning

This is the natural/exponential bridge:

\[
\underbrace{B(x)}_{\text{folded xi}}
\quad=\quad
\underbrace{\int\cosh(\sqrt{x}t)\,d\nu(t)}_{\text{natural moment view}}
\quad=\quad
\underbrace{\exp\left(
\sum_{m\ge1}(-1)^{m+1}\frac{\ell_m}{m}x^m
\right)}_{\text{exponential cumulant view}}.
\]

The Archimedean kernel already gives a positive moment ledger. But this
is not RH. Moment/Hankel positivity is weaker than the folded
Toeplitz-total-positivity condition of Theorem 15.

The gap can now be named exactly:

\[
\boxed{
\text{Hankel moment positivity is unconditional;}
\qquad
\text{Toeplitz total positivity is RH-strength.}
}
\]

The remaining climb is the upgrade

\[
\bigl((2(i+j))!b_{i+j}\bigr)\succeq0
\quad\Longrightarrow?\quad
\bigl(b_{j-i}\bigr)\text{ totally positive}.
\]

That implication is false in general. The program must use the
additional primorial/cumulant/Noether structure of this specific
Archimedean ledger, not merely its positivity as a moment sequence.

---

## Theorem 20. Toeplitz Upgrade Criterion

Let

\[
B(x)=\sum_{n\ge0}b_nx^n
\]

be the folded xi ledger from Theorem 19. Suppose the centered
primorial/Archimedean cumulant construction proves that the coefficient
sequence \(b=(b_0,b_1,\ldots)\) is a \(PF_\infty\) sequence, i.e.

\[
\det\bigl(b_{j_\beta-i_\alpha}\bigr)_{\alpha,\beta=1}^{r}\ge0
\]

for every \(r\ge1\) and every increasing pair of index sets

\[
i_1<\cdots<i_r,
\qquad
j_1<\cdots<j_r,
\]

with \(b_n=0\) for \(n<0\). Then RH holds.

Equivalently, if every finite Toeplitz minor of the folded coefficient
ledger is obtained as the limit of a manifestly nonnegative centered
primorial determinant, then RH holds.

### Proof

This is Theorem 15 in operational form. Total positivity of the Toeplitz
matrix \((b_{j-i})\) says exactly that \(b\) is \(PF_\infty\). By the
Aissen-Schoenberg-Whitney-Edrei theorem, the generating function \(B\)
has only real nonpositive zeros. Since

\[
B(x)=\Xi(i\sqrt{x})/\Xi(0),
\]

Theorem 15 gives RH. \(\square\)

### Meaning

The finite determinant that must be transported is no longer vague:

\[
\Delta_{I,J}(b)
:=
\det\bigl(b_{j_\beta-i_\alpha}\bigr)_{\alpha,\beta=1}^{r}.
\]

The Pass-3 proof target is:

\[
\boxed{
\Delta_{I,J}(b)
=
\lim_{n,T\to\infty}
\Delta^{\circ}_{I,J}(n,T),
\qquad
\Delta^{\circ}_{I,J}(n,T)\ge0
\text{ by centered primorial geometry.}
}
\]

This is the finite-minor version of the positive Fredholm determinant
criterion. It is local enough to attack one determinant shape at a time,
but global enough that proving all of them is exactly RH.

---

## Theorem 21. Variation-Diminishing Form of RH

Let \(b=(b_0,b_1,\ldots)\) be the folded coefficient ledger of

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}
=
\sum_{n\ge0}b_nx^n,
\]

with \(b_n=0\) for \(n<0\). Define the Toeplitz convolution operator

\[
(C_bv)_j:=\sum_i b_{j-i}v_i
\]

on finitely supported real sequences \(v\). Let \(V(v)\) denote the
number of sign changes in \(v\), after deleting zeros.

Then RH is equivalent to the variation-diminishing property

\[
\boxed{\;
V(C_bv)\le V(v)
\quad
\text{for every finitely supported real sequence }v.
\;}
\]

### Proof

The classical Schoenberg variation-diminishing theorem says that a
Toeplitz convolution operator is variation-diminishing exactly when its
kernel sequence is \(PF_\infty\), equivalently when its Toeplitz matrix
is totally positive. By Theorem 15, \(b\in PF_\infty\) is equivalent to
RH. \(\square\)

### Meaning

This is the observer-language form of the folded RH target:

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\text{the folded coefficient ledger cannot create new sign changes.}
\]

So total positivity is not only a determinant condition. It is a
monotonicity law for finite observations of the coefficient ray.

The simplicial interpretation is direct:

- a finite test sequence \(v\) is a signed observer contrast;
- convolution by \(b\) is the folded xi response;
- RH says this response is variation-diminishing;
- no new alternation may be created by the completed zeta ledger.

This is a strong domain-language upgrade: the Bures positivity field,
after folding, becomes a **variation non-creation law**.

---

## Theorem 22. Schur-Minor Form of the Positive Determinant Model

Let

\[
B_N(x)=\prod_{a=1}^{N}(1+\lambda_ax)
=
\sum_{k=0}^{N}e_k(\lambda)x^k,
\qquad
\lambda_a\ge0.
\]

Let \(b_k=e_k(\lambda)\), with \(b_k=0\) for \(k<0\) or \(k>N\). Then
every Toeplitz minor

\[
\Delta_{I,J}(b)
=
\det\bigl(b_{j_\beta-i_\alpha}\bigr)_{\alpha,\beta=1}^{r}
\]

is a skew Schur polynomial in the nonnegative variables
\(\lambda_1,\ldots,\lambda_N\). In particular,

\[
\Delta_{I,J}(b)\ge0.
\]

### Proof

The Jacobi-Trudi identities express minors of the Toeplitz matrix built
from elementary symmetric functions as skew Schur functions, up to the
standard indexing convention. Skew Schur functions have expansions as
sums of semistandard Young tableaux:

\[
s_{\lambda/\mu}(\lambda_1,\ldots,\lambda_N)
=
\sum_T \lambda^T,
\]

a sum of monomials with nonnegative integer coefficients. Since
\(\lambda_a\ge0\), every such minor is nonnegative. \(\square\)

### Meaning

This is the combinatorial face of the positive Fredholm determinant.
If a finite folded approximant has the form

\[
B_N(x)=\det(I+xL_N),
\qquad
L_N\ge0,
\]

then all Toeplitz minors are not merely nonnegative by abstract theory:
they are explicit Schur-positive sums in the eigenvalue ledger of
\(L_N\).

Thus the Pass-3 construction can aim for a stronger finite statement:

\[
\boxed{
\Delta^{\circ}_{I,J}(n,T)
=
s_{\lambda/\mu}\bigl(\lambda_1^{(n,T)},\ldots,
\lambda_{N(n,T)}^{(n,T)}\bigr)
\ge0
}
\]

where the \(\lambda_a^{(n,T)}\) are eigenvalues of the finite positive
operator produced by the centered primorial cumulant tower.

The route is now:

\[
\text{centered primorial geometry}
\to
L_{n,T}^{\circ}\ge0
\to
\text{Schur-positive minors}
\to
\mathsf T_\Theta\text{ totally positive}
\to
\mathrm{RH}.
\]

---

## Theorem 23. Newton Bridge from Cumulants to Eigenvalue Ledgers

Let \(L\ge0\) be a finite positive operator with eigenvalues
\(\lambda_1,\ldots,\lambda_N\ge0\). Define the power sums

\[
\ell_m:=\operatorname{Tr}(L^m)
=
\sum_{a=1}^{N}\lambda_a^m
\]

and the determinant coefficients

\[
\det(I+xL)
=
1+\sum_{k=1}^{N}p_kx^k.
\]

Then the two ledgers are connected by Newton's identities:

\[
kp_k
=
\sum_{m=1}^{k}(-1)^{m-1}p_{k-m}\ell_m,
\qquad
p_0=1.
\]

Equivalently,

\[
\log\det(I+xL)
=
\sum_{m\ge1}(-1)^{m+1}\frac{\ell_m}{m}x^m.
\]

Conversely, if a finite cumulant ledger

\[
(\ell_1,\ldots,\ell_{2N})
\]

is represented by \(N\) nonnegative atoms,

\[
\ell_m=\sum_{a=1}^{N}\lambda_a^m,\qquad \lambda_a\ge0,
\]

then Newton's identities produce a polynomial

\[
1+\sum_{k=1}^{N}p_kx^k
=
\prod_{a=1}^{N}(1+\lambda_ax)
\]

with only real nonpositive zeros and a totally positive coefficient
ledger.

### Proof

The logarithmic identity follows from

\[
\log(1+\lambda x)
=
\sum_{m\ge1}(-1)^{m+1}\frac{\lambda^m}{m}x^m
\]

and summing over eigenvalues. Exponentiating and comparing coefficients
gives Newton's identities. The converse is immediate from the assumed
atomic representation. \(\square\)

### Meaning

This is the exact bridge between T2-style cumulants and T15-style
coefficient total positivity:

\[
\text{power-sum cumulants }(\ell_m)
\quad\xleftrightarrow{\text{Newton}}
\quad
\text{coefficient ledger }(p_k).
\]

So the centered primorial/Archimedean cumulant tower does not have to
guess zeros. It can attempt to prove that its finite cumulant packets are
power sums of nonnegative eigenvalue ledgers:

\[
\ell_m^{(n,T)}
=
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr),
\qquad
L_{n,T}^{\circ}\ge0.
\]

Newton then builds

\[
B_{n,T}^{\circ}(x)
=
\det(I+xL_{n,T}^{\circ})
\in PF_\infty.
\]

The convergence target becomes:

\[
\ell_m^{(n,T)}
\longrightarrow
\ell_m
\quad\text{for every }m,
\]

together with enough growth control to upgrade coefficientwise
convergence to local-uniform convergence of determinants.

This is the finite algebraic spine of the victory route:

\[
\boxed{
\text{positive cumulant traces}
\xrightarrow{\text{Newton}}
\text{PF}_\infty\text{ determinant ledgers}
\xrightarrow{\text{limit}}
\Theta
\xrightarrow{\text{ASW-Edrei}}
\mathrm{RH}.
}
\]

---

## Theorem 24. Edrei Order-Collapse Criterion

Let

\[
B(x)=\sum_{n\ge0}b_nx^n
=
\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Then \(B\) is an entire function of order \(1/2\). If its coefficient
ledger \(b\) is \(PF_\infty\), then Edrei's representation collapses to

\[
\boxed{\;
B(x)=\prod_{a\ge1}(1+\alpha_ax),
\qquad
\alpha_a\ge0,\qquad
\sum_a\alpha_a<\infty.
\;}
\]

Conversely, any product of this form has a \(PF_\infty\) coefficient
ledger. Therefore RH is equivalent to the existence of nonnegative
summable Edrei parameters \(\alpha_a\) for the folded xi function.

### Proof

Edrei's theorem classifies \(PF_\infty\) ordinary generating functions:

\[
\sum_{n\ge0}b_nx^n
=
Cx^m e^{\gamma x}
\frac{\prod_a(1+\alpha_ax)}
{\prod_b(1-\beta_bx)},
\]

with \(C,\gamma,\alpha_a,\beta_b\ge0\) and
\(\sum_a\alpha_a+\sum_b\beta_b<\infty\), in the appropriate domain.
Since \(B\) is entire and \(B(0)=1\), there is no pole denominator, no
initial power \(x^m\), and \(C=1\). Since \(B(x)=\Xi(i\sqrt{x})/\Xi(0)\)
has order \(1/2\), the exponential factor \(e^{\gamma x}\) is impossible
unless \(\gamma=0\). Thus the representation reduces to the displayed
product.

The converse is standard: products of factors \(1+\alpha x\) with
\(\alpha\ge0\), and locally uniform limits of such products, are
\(PF_\infty\). Combining this with Theorem 15 gives the RH equivalence.
\(\square\)

### Meaning

The folded xi ledger is too small, by growth order, to hide an
exponential drift. If total positivity holds, then \(B\) must be a pure
positive determinant product:

\[
B(x)=\det(I+xL_\Xi),
\qquad
L_\Xi\ge0,\quad \operatorname{Tr}L_\Xi<\infty.
\]

So the possible victory form is forced. There is no extra Edrei gauge
left to remove.

---

## Theorem 25. Trace-Moment Convergence Implies Determinant Convergence

For each \(j\), let \(L_j\ge0\) be a finite-rank positive operator.
Assume:

1. the traces are uniformly bounded:

\[
\sup_j\operatorname{Tr}L_j<\infty;
\]

2. for every \(m\ge1\), the power traces converge:

\[
\operatorname{Tr}(L_j^m)\longrightarrow \ell_m,
\]

where \(\ell_m\) are the folded divisor cumulants of

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Then

\[
\det(I+xL_j)\longrightarrow B(x)
\]

locally uniformly on \(\mathbb C\). Consequently, RH holds.

### Proof

The uniform trace bound gives, for every \(x\in\mathbb C\),

\[
|\det(I+xL_j)|
\le
\prod_a(1+|x|\lambda_{j,a})
\le
\exp\left(|x|\sum_a\lambda_{j,a}\right)
\le
\exp(C|x|)
\]

with \(C=\sup_j\operatorname{Tr}L_j\). Hence the determinant family is
locally bounded and normal.

The logarithm near \(x=0\) is

\[
\log\det(I+xL_j)
=
\sum_{m\ge1}(-1)^{m+1}
\frac{\operatorname{Tr}(L_j^m)}{m}x^m.
\]

By the assumed trace convergence, the Taylor coefficients of the
logarithms converge to those of \(\log B(x)\). Equivalently, Newton's
identities give coefficientwise convergence of
\(\det(I+xL_j)\) to \(B(x)\). Every locally uniform subsequential limit
therefore has the same Taylor series as \(B\) at the origin, hence is
\(B\). Normality upgrades this to local-uniform convergence of the whole
sequence.

Since each \(L_j\ge0\), every determinant \(\det(I+xL_j)\) has only
real nonpositive zeros. The locally uniform limit \(B\) therefore has
only real nonpositive zeros. By Theorem 15, RH holds. \(\square\)

### Meaning

This is the clean analytic convergence theorem the program needs:

\[
\boxed{
L_{n,T}^{\circ}\ge0,\quad
\sup\operatorname{Tr}L_{n,T}^{\circ}<\infty,\quad
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)\to\ell_m
\ \forall m
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

So the problem becomes a trace-cumulant realization problem. The
centered primorial/Archimedean cumulant tower must produce finite
positive operators whose power traces converge to the folded divisor
cumulants of \(\Xi\).

---

## Theorem 26. Flat Hankel Finite-Atom Test

Let

\[
\ell_1,\ldots,\ell_{2N}
\]

be a finite folded cumulant packet. Put

\[
r_k:=\ell_{k+1},\qquad 0\le k\le 2N-1.
\]

If the truncated Hankel matrices

\[
\mathsf M^{(0)}=(r_{i+j})_{i,j=0}^{N-1},
\qquad
\mathsf M^{(1)}=(r_{i+j+1})_{i,j=0}^{N-1}
\]

are positive semidefinite and admit a flat Stieltjes extension of rank
\(R\le N\), then there exist nonnegative atoms

\[
\lambda_1,\ldots,\lambda_R\ge0
\]

and positive weights \(w_a>0\) such that

\[
r_k=\sum_{a=1}^{R}w_a\lambda_a^k
\]

for all available \(k\). If moreover \(w_a=\lambda_a\) after the
program's trace gauge selection, then

\[
\ell_m=\sum_{a=1}^{R}\lambda_a^m
\]

and Newton's identities construct a finite positive determinant

\[
B_N(x)=\prod_{a=1}^{R}(1+\lambda_ax).
\]

### Proof

The first statement is the truncated Stieltjes moment theorem with flat
extension: positivity of the ordinary and shifted Hankel forms plus
flatness gives a representing measure on \([0,\infty)\) with at most
\(R\) atoms. The final statement is substitution of the trace-gauge
condition \(w_a=\lambda_a\), which converts the Stieltjes moment measure
for \(r_k=\ell_{k+1}\) into a trace ledger for \(\ell_m\). Newton's
identities then give the determinant polynomial. \(\square\)

### Meaning

This theorem names a subtle but important gauge point. Hankel positivity
alone gives a positive measure

\[
r_k=\int t^k\,d\sigma(t).
\]

To become a Fredholm determinant trace ledger, the measure must have the
special trace form

\[
d\sigma(t)=t\,d\nu_{\mathrm{count}}(t),
\]

so that

\[
r_k=\sum_a\lambda_a^{k+1}.
\]

That is the **trace gauge**. It is the multiplicative/Archimedean
counterpart of the additive centering gauge earlier in the ladder.

The Pass-3 finite task is therefore not just:

\[
\text{prove Hankel positivity.}
\]

It is:

\[
\boxed{
\text{prove flat positive Stieltjes representation plus trace gauge.}
}
\]

Then Newton builds a \(PF_\infty\) determinant approximant.

---

## Theorem 27. Log-Determinant Curvature Linearization

Let \(L\ge0\) be a positive trace-class operator and define

\[
B_L(x):=\det(I+xL),
\qquad
S_L(x):=\log B_L(x).
\]

Then

\[
S_L(x)=\operatorname{Tr}\log(I+xL)
\]

and, for \(x>0\),

\[
S_L'(x)
=
\operatorname{Tr}\bigl(L(I+xL)^{-1}\bigr).
\]

Moreover, \(S_L'\) is completely monotone:

\[
(-1)^k\frac{d^k}{dx^k}S_L'(x)
=
k!\operatorname{Tr}\!\left(
L^{k+1}(I+xL)^{-(k+1)}
\right)
\ge0.
\]

Equivalently, if the eigenvalues of \(L\) are \(\lambda_a\ge0\), then

\[
S_L'(x)
=
\sum_a\frac{\lambda_a}{1+\lambda_ax},
\]

and

\[
S_L(x)
=
\sum_a\log(1+\lambda_ax).
\]

### Proof

Functional calculus gives

\[
\log(I+xL)
\]

as a trace-class operator for \(x\ge0\), and the Fredholm determinant
identity gives \(S_L=\operatorname{Tr}\log(I+xL)\). Differentiating by
functional calculus yields

\[
S_L'(x)=\operatorname{Tr}\bigl(L(I+xL)^{-1}\bigr).
\]

Repeated differentiation gives

\[
\frac{d^k}{dx^k}S_L'(x)
=
(-1)^k k!\operatorname{Tr}\!\left(
L^{k+1}(I+xL)^{-(k+1)}
\right).
\]

The operator inside the trace is positive, so the displayed
complete-monotonicity inequality follows. \(\square\)

### Meaning

This is the precise linearization of curvature:

\[
\text{multiplicative determinant geometry}
\quad\xrightarrow{\log}\quad
\text{additive trace cumulants}.
\]

The determinant product is curved/multiplicative:

\[
B_L(x)=\prod_a(1+\lambda_ax).
\]

The logarithm turns it into the linear trace action:

\[
S_L(x)=\sum_a\log(1+\lambda_ax).
\]

The derivatives are the curvature ledger:

\[
\ell_m=\operatorname{Tr}(L^m).
\]

So the RH target can be read as:

\[
\boxed{
\text{the folded xi action }\log B
\text{ must be the trace-log of a positive operator.}
}
\]

---

## Theorem 28. Continuous-to-Discrete Quadrature Is Not Enough

Let \(\sigma\) be a positive finite measure on \([0,\infty)\) with
finite moments, and define

\[
S_\sigma(x):=\int_0^\infty \log(1+tx)\,d\sigma(t).
\]

Finite positive quadrature rules can approximate \(S_\sigma\) on compact
subsets away from the negative support by functions of the form

\[
S_Q(x)=\sum_{a=1}^{N}w_a\log(1+\lambda_ax),
\qquad
w_a>0,\quad \lambda_a\ge0.
\]

However,

\[
\exp S_Q(x)=\prod_{a=1}^{N}(1+\lambda_ax)^{w_a}
\]

is a polynomial with a \(PF_\infty\) coefficient ledger only when the
weights \(w_a\) are nonnegative integers, or when the expression is
realized as a genuine Fredholm determinant with eigenvalue
multiplicities.

Therefore positive quadrature discretizes the continuous curvature, but
does not by itself produce the determinant/PF structure needed for RH.

### Proof

Positive quadrature for a finite moment problem gives atoms
\(\lambda_a\ge0\) and positive weights \(w_a\) matching finitely many
moments of \(\sigma\), hence matching the Taylor expansion of
\(S_\sigma\) to finite order. Standard weak convergence or increasing
quadrature order gives convergence of the logarithmic potentials on
compact sets avoiding the cut.

But exponentiating a weighted logarithmic sum gives

\[
\prod_a(1+\lambda_ax)^{w_a}.
\]

If the \(w_a\) are not integers, this is not an ordinary polynomial and
does not have a Toeplitz coefficient ledger of finite \(PF_\infty\)
type. A Fredholm determinant corresponds to integer spectral
multiplicity: each eigenvalue appears once per dimension of its
eigenspace. Thus arbitrary positive quadrature is weaker than the
positive determinant model. \(\square\)

### Meaning

This is the discretization guardrail:

\[
\text{positive continuous measure}
\to
\text{positive quadrature}
\]

is easy compared with

\[
\text{positive quadrature}
\to
\text{positive Fredholm determinant}.
\]

The latter requires the trace gauge / multiplicity gauge. This is the
same lesson as before in sharper language:

\[
\boxed{
\text{moment positivity is continuous;}
\qquad
\text{PF determinant positivity is discretized trace geometry.}
}
\]

---

## Theorem 29. Bidirectional Discretization-Curvature Ladder

The folded RH program has the following bidirectional ladder:

\[
\begin{array}{ccccc}
\text{positive eigenvalue ledger}
&\xrightarrow{\det(I+xL)}&
\text{coefficient ledger }B
&\xrightarrow{\text{ASW-Edrei}}&
\text{negative-real zeros}
\\[4pt]
\lambda_a
&&
b_n
&&
\gamma_a^2
\\[4pt]
\downarrow\scriptstyle{\operatorname{Tr}(L^m)}
&&
\downarrow\scriptstyle{\log}
&&
\downarrow\scriptstyle{\gamma\mapsto\gamma^{-2}}
\\[4pt]
\text{power traces}
&\xleftarrow{\text{Newton}}&
\text{divisor cumulants}
&\xleftarrow{\log}&
\text{folded divisor product.}
\end{array}
\]

In formulas:

\[
B(x)=\det(I+xL)
\quad\Longleftrightarrow\quad
\log B(x)=
\sum_{m\ge1}(-1)^{m+1}\frac{\operatorname{Tr}(L^m)}{m}x^m.
\]

The upward direction discretizes the continuous curvature into finite
eigenvalue packets. The downward direction linearizes the determinant
curvature into trace cumulants. The RH-strength assertion is that the
specific folded xi action lies in the image of this bidirectional
ladder with \(L\ge0\).

### Meaning

This is the sentence matching the intuition:

\[
\boxed{
\text{discretization of the continuous}
\quad\leftrightarrow\quad
\text{linearization of curvature}.
}
\]

The program's job is to prove that the centered primorial/Archimedean
cumulant tower is not merely a continuous moment model. It must land in
the determinant image:

\[
\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
=
\operatorname{Tr}\log(I+xL_\Xi)
\quad
\text{for some }L_\Xi\ge0.
\]

Then RH follows by every equivalent route above.

---

## Theorem 30. Diagnostic Triad: Sensitivity, Specificity, Precision

Let \(\mathcal C\) be a proposed criterion for the folded xi ledger

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

We use the following diagnostic language:

\[
\text{sensitivity / recall}
\quad:\quad
\mathrm{RH}\Rightarrow\mathcal C,
\]

\[
\text{specificity}
\quad:\quad
\mathcal C\Rightarrow\mathrm{RH},
\]

\[
\text{precision}
\quad:\quad
\mathcal C\text{ identifies the intended determinant object, not a
larger positivity lookalike.}
\]

Then the criteria in this note have the following status:

\[
\begin{array}{c|c|c|c}
\text{criterion} & \text{sensitive} & \text{specific} & \text{precise} \\
\hline
\text{Archimedean Hankel moment positivity} & \checkmark & \times & \times \\
\text{complete monotonicity of a continuous log-potential} & \checkmark & \times & \times \\
\text{finite positive quadrature} & \checkmark & \times & \times \\
\text{Toeplitz total positivity }(PF_\infty) & \checkmark & \checkmark & \checkmark \\
\text{positive Fredholm determinant for }B & \checkmark & \checkmark & \checkmark \\
\text{Bures Pick/Wronskian positivity} & \checkmark & \checkmark & \checkmark \\
\text{trace-moment convergence with bounded trace} & \checkmark & \checkmark & \checkmark
\end{array}
\]

### Proof

Archimedean Hankel positivity follows unconditionally from Theorem 19,
so it is sensitive but not specific: it holds whether or not RH is true.
The same is true for generic continuous positive log-potentials and
generic positive quadrature by Theorem 28; they model positivity but do
not force a \(PF_\infty\) coefficient ledger.

Toeplitz total positivity is equivalent to \(PF_\infty\), and by the
Aissen-Schoenberg-Whitney-Edrei theorem plus Theorem 15 it is equivalent
to RH. Positive Fredholm determinant form is equivalent by Theorem 18
and the Edrei collapse in Theorem 24. Bures Pick/Wronskian positivity is
equivalent by Theorems 4, 7, and 9. Trace-moment convergence with bounded
trace is sufficient by Theorem 25, and is sensitive because under RH the
diagonal operator with eigenvalues \(\gamma^{-2}\) supplies the limiting
positive trace-class model.

The precision column records whether the criterion lands specifically
in the determinant/PF/Bures object rather than in a wider class of
positive moment-like objects. \(\square\)

### Meaning

This is the statistical diagnostic discipline of the proof search.

The false summit pattern is:

\[
\text{high sensitivity}
\quad+\quad
\text{low specificity}
\quad=\quad
\text{a beautiful necessary condition, not RH.}
\]

The victory pattern is:

\[
\boxed{
\text{sensitivity}
\quad+\quad
\text{specificity}
\quad+\quad
\text{precision}
\quad=\quad
\text{RH-strength criterion.}
}
\]

The third prime is precision. It prevents the proof from accepting a
generic positive continuous model when the target is the sharper
positive determinant trace model.

---

## Theorem 31. No False-Positive Ladder for Pass-3

A Pass-3 proof by centered primorial/Archimedean cumulants must produce
finite objects \(L_{n,T}^{\circ}\) satisfying all three diagnostic
requirements:

1. **Sensitivity / recall.** The construction must preserve every
   structural contribution of the folded xi action:

\[
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)
\longrightarrow
\ell_m
\qquad(m\ge1).
\]

2. **Specificity.** The limiting object must force RH:

\[
\det(I+xL_{n,T}^{\circ})
\longrightarrow
\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\quad\Longrightarrow\quad
\mathrm{RH}.
\]

3. **Precision.** Each finite object must live in the determinant class:

\[
L_{n,T}^{\circ}\ge0,
\qquad
\sup_{n,T}\operatorname{Tr}L_{n,T}^{\circ}<\infty.
\]

Equivalently, the finite approximants must be

\[
B_{n,T}^{\circ}(x)=\det(I+xL_{n,T}^{\circ}),
\]

not merely exponentials of positive quadrature sums with arbitrary
weights.

### Proof

The first condition is the trace-cumulant matching required by Theorem
25. The second condition is the local-uniform determinant convergence
that places the folded xi function in the \(PF_\infty\) / negative-real
zero class. The third condition prevents the quadrature false positive
from Theorem 28: arbitrary weights \(w_a>0\) give positive
log-potentials but not necessarily determinant polynomials or Fredholm
determinants. Together, Theorem 25 applies and RH follows. \(\square\)

### Meaning

The proof target is no longer:

\[
\text{find positivity somewhere.}
\]

It is:

\[
\boxed{
\text{find the right positivity, in the right finite class, converging
to the right folded object.}
}
\]

That is sensitivity, specificity, and precision in mathematical form.

---

## Pass-3 Target. The Positive Determinant Trace Model

The Pass-3 target is to construct, from the centered
primorial/Archimedean cumulant tower, a two-parameter family of finite
positive operators

\[
L_{n,T}^{\circ}\ge0
\]

such that their Fredholm determinant polynomials

\[
B_{n,T}^{\circ}(x)
:=
\det(I+xL_{n,T}^{\circ})
\]

converge to the folded xi function

\[
B(x):=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

The construction must satisfy four explicit requirements.

### P3.1 Finite Determinant Class

For every finite stage \((n,T)\),

\[
L_{n,T}^{\circ}
\]

is finite-rank and positive. Therefore

\[
B_{n,T}^{\circ}(x)
=
\prod_{a=1}^{N(n,T)}
\left(1+\lambda_a^{(n,T)}x\right),
\qquad
\lambda_a^{(n,T)}\ge0.
\]

Equivalently, every finite coefficient ledger of
\(B_{n,T}^{\circ}\) is \(PF_\infty\), every Toeplitz minor is
nonnegative, and convolution by its coefficients is variation
diminishing.

### P3.2 Uniform Trace Control

The positive eigenvalue ledgers have uniformly bounded total mass:

\[
\sup_{n,T}\operatorname{Tr}L_{n,T}^{\circ}
=
\sup_{n,T}\sum_a\lambda_a^{(n,T)}
<\infty.
\]

This is the compactness condition that prevents determinant mass from
escaping in the limit.

### P3.3 Cumulant / Trace Matching

Let

\[
\log B(x)
=
\sum_{m\ge1}(-1)^{m+1}\frac{\ell_m}{m}x^m
\]

define the folded divisor cumulants of \(\Xi\). For every \(m\ge1\),
Pass-3 must prove

\[
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)
\longrightarrow
\ell_m.
\]

Equivalently,

\[
\log B_{n,T}^{\circ}(x)
=
\operatorname{Tr}\log(I+xL_{n,T}^{\circ})
\]

must converge coefficientwise to

\[
\log B(x).
\]

### P3.4 Local-Uniform Determinant Convergence

The trace control and cumulant matching must be strong enough to give

\[
B_{n,T}^{\circ}(x)
\longrightarrow
B(x)
\]

locally uniformly on \(\mathbb C\).

By Theorem 25, P3.2 and P3.3 are a sufficient analytic route to this
condition.

---

## Pass-3 Main Conditional Theorem

If P3.1--P3.4 hold, then RH holds.

### Proof

By P3.1,

\[
B_{n,T}^{\circ}(x)
\]

has only real nonpositive zeros for every \((n,T)\). By P3.4, these
polynomials converge locally uniformly to

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

The Laguerre-Pólya class with zeros on \((-\infty,0]\) is closed under
local-uniform limits. Therefore \(B\) has only real nonpositive zeros.
By Theorem 15, this is equivalent to RH. \(\square\)

### The Exact Technical Core

The whole Pass-3 proof is therefore reduced to one construction:

\[
\boxed{
\text{build }L_{n,T}^{\circ}\ge0
\text{ from centered primorial/Archimedean cumulants and prove }
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)\to\ell_m
\text{ with bounded trace.}
}
\]

Everything else is already theorem-level machinery.

---

## Pass-3 Input Ledger

The construction must start from the folded xi action

\[
S(x):=\log B(x)
=
\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

and its cumulant ledger

\[
\ell_m
=
(-1)^{m+1}m[x^m]S(x).
\]

The finite primorial/Archimedean model must produce finite cumulants

\[
\ell_m^{(n,T)}
\]

with a trace realization

\[
\ell_m^{(n,T)}
=
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr),
\qquad
L_{n,T}^{\circ}\ge0.
\]

This is stronger than proving that the \(\ell_m^{(n,T)}\) form a
positive Hankel moment packet. Pass-3 requires the **trace gauge**:

\[
\ell_m^{(n,T)}
=
\sum_a\left(\lambda_a^{(n,T)}\right)^m
\]

with no arbitrary quadrature weights.

---

## Pass-3 Rejection Tests

A proposed Pass-3 construction fails if any of the following occurs.

1. It gives only Hankel positivity:

\[
\bigl(\ell_{i+j+1}^{(n,T)}\bigr)\succeq0.
\]

This is sensitive but not specific.

2. It gives only a positive quadrature log-potential:

\[
\sum_aw_a\log(1+\lambda_ax),
\qquad
w_a>0.
\]

This is not precise unless the weights are realized as determinant
multiplicities.

3. It proves convergence only on a heat-deformed target

\[
H_\tau,\qquad \tau>0,
\]

instead of the undeformed target \(H_0=\Xi\).

4. It builds positive finite objects but lacks uniform trace control.

5. It matches finitely many cumulants without a diagonal regime that
gives all cumulants and local-uniform determinant convergence.

---

## Pass-3 Victory Statement

The exact victory statement is:

\[
\boxed{
\exists\,L_{n,T}^{\circ}\ge0
\quad
\text{finite-rank, centered-primorial/Archimedean,}
\quad
\sup\operatorname{Tr}L_{n,T}^{\circ}<\infty,
}
\]

\[
\boxed{
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)\to
(-1)^{m+1}m[x^m]\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\quad
\forall m\ge1.
}
\]

Then

\[
\det(I+xL_{n,T}^{\circ})
\to
\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

locally uniformly, the folded coefficient ledger is \(PF_\infty\), and
RH follows.

This is the nailed Pass-3 target:

\[
\boxed{
\text{centered primorial cumulants}
\to
\text{positive trace operators}
\to
\text{PF}_\infty\text{ folded xi}
\to
\mathrm{RH}.
}
\]

---

## Pass-2 Target

The corrected target is no longer

\[
|\Sigma(y,\xi)|^2/(2\pi)=u_B(\xi,y).
\]

The corrected target should be a centered pair-current statement of
the form

\[
\boxed{
u_B(\xi,y)\,d\xi
=
\text{a gauge-selected centered covariance / diagonal transport
of the primorial pair current}.
}
\]

Equivalently:

\[
\text{RH}
\quad\Longleftrightarrow\quad
\text{the Bures gauge section of the centered primorial pair current
is positive}.
\]

This is a strictly cleaner formulation than Pass-1. It is also honest:
the positivity of that Bures gauge section is still the RH-strength
content.
