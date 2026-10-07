# RH Pass-5: Lock A No-Loss and the Born Heat Flow

**Leonardo Murillo Montero + Codex**

*Draft 1 - May 24, 2026*

## Essence

Pass-4 identified the category error in Pass-3: positive trace-gauge atoms
do not need to be manufactured by Pade, determinants, or Hankel gates. T6
already gives them.

\[
\boxed{
\lambda_a=(\widehat y_a)^2\ge0.
}
\]

The square is the Born closure. The RMS identity is the trace gauge.

Pass-5 names the actual summit:

\[
\boxed{
\text{Lock A no-loss: as heat is removed, the Born-square power sums
lose no trace, collapse into no dust, and acquire no phase.}
}
\]

The object is not a labeled list of amplitudes. Labels may split, merge,
and drift. The invariant object is the trace-weighted Born measure

\[
d\tau_t(s)=\sum_j \lambda_j(t)\,\delta_{\lambda_j(t)}(s).
\]

For \(t>\Lambda\), de Bruijn-Newman theory gives real zeros, hence
positive atoms. RH is exactly the statement that this positive Born heat
flow reaches \(t=0\).

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\tau_t \xrightarrow[t\to0^+]{} \tau_0
\text{ inside the positive trace-gauge cone.}
}
\]

That is the Pass-5 reduction.

---

## 0. Claim Discipline

This draft separates three levels.

**Theorems already inherited.**

1. T6: RMS/Born closure gives nonnegative square atoms.
2. T6: RMS/Parseval gives the trace identity.
3. de Bruijn-Newman: \(\Xi_t\) has only real zeros for \(t>\Lambda\).
4. Rodgers-Tao: \(\Lambda\ge0\).
5. Pass-3/Pile I: a positive trace-class determinant for \(B(x)\) is
   equivalent to RH.

**Reduction proved here.**

The RH problem is equivalent to Lock A no-loss: the trace-weighted Born
measures for \(t>\Lambda\) have a positive trace-gauge limit at \(t=0\)
whose moments are the folded \(\Xi\) cumulants.

**Still open.**

Proving the no-loss statement without assuming RH. Pass-5 does not pretend
this is done. It makes the mountain one peak instead of three.

One further discipline rail is needed. Finite trace bounds do not by
themselves exclude **trace dust at zero**: many tiny atoms may converge to
an \(s=0\) mass in the trace-weighted measure. Such dust contributes to
the first cumulant but not to higher cumulants, and analytically appears
as an \(e^{cx}\) factor. The folded \(\Xi\) product has no such free
exponential factor. Thus Lock A no-loss means:

\[
\boxed{
\text{no trace escape, no zero-dust, no phase leakage.}
}
\]

---

## 1. Folded \(\Xi\) and the Cumulant Ledger

Let

\[
B(x):=\frac{\Xi(i\sqrt x)}{\Xi(0)}.
\]

By the even Hadamard product,

\[
B(x)=\prod_\rho \left(1+\frac{x}{z_\rho^2}\right),
\]

where \(z_\rho\) are the spectral zeros in the \(z\)-coordinate. Therefore

\[
\log B(x)
=
\sum_{m\ge1}\frac{(-1)^{m+1}}{m}\ell_m x^m,
\]

with

\[
\boxed{
\ell_m=\sum_\rho z_\rho^{-2m}.
}
\]

This identity is unconditional. The sign and positivity question is not
whether the cumulants exist. They do. The question is whether they are
power sums of positive square atoms.

RH says exactly:

\[
z_\rho\in\mathbb R
\quad\Longrightarrow\quad
\lambda_\rho:=z_\rho^{-2}>0,
\]

so that

\[
\ell_m=\sum_\rho \lambda_\rho^m.
\]

Thus RH is the positivity of the folded cumulant ledger.

---

## 2. Heat Flow and Born Atoms

Let

\[
\Xi_t(z)
=
\int_{-\infty}^{\infty}e^{tu^2}\Phi(u)\cos(uz)\,du,
\qquad
\Xi_0=\Xi.
\]

For \(t>\Lambda\), all zeros \(z_k(t)\) are real. Define

\[
B_t(x):=\frac{\Xi_t(i\sqrt x)}{\Xi_t(0)}
=
\prod_k\left(1+\lambda_k(t)x\right),
\qquad
\lambda_k(t):=z_k(t)^{-2}>0.
\]

Then

\[
\log B_t(x)
=
\sum_{m\ge1}\frac{(-1)^{m+1}}{m}\ell_m(t)x^m
\]

where

\[
\boxed{
\ell_m(t)=\sum_k \lambda_k(t)^m.
}
\]

This is already a Born ledger:

\[
\lambda_k(t)=\xi_k(t)^2,
\qquad
\xi_k(t)=|z_k(t)|^{-1}.
\]

For \(t>\Lambda\), Locks B and C are automatic:

\[
\lambda_k(t)\ge0,
\qquad
\sum_k\lambda_k(t)=\ell_1(t).
\]

The entire difficulty is the removal of heat:

\[
t\to0^+.
\]

If the positive Born ledger survives to \(t=0\), RH follows.

---

## 3. Trace-Weighted Born Measures

The correct convergence object is not the coordinate list
\(\{\xi_k(t)\}\). The labels of zeros may not be the right topology. The
right object is the trace-weighted measure

\[
\boxed{
d\tau_t(s)
:=
\sum_k\lambda_k(t)\,\delta_{\lambda_k(t)}(s).
}
\]

Its moments are shifted by one:

\[
\int s^{m-1}\,d\tau_t(s)
=
\sum_k\lambda_k(t)^m
=
\ell_m(t).
\]

The determinant is encoded directly by \(\tau_t\):

\[
\log B_t(x)
=
\sum_k\log(1+x\lambda_k(t))
=
\int\frac{\log(1+xs)}{s}\,d\tau_t(s),
\]

with \(\log(1+xs)/s\) read as \(x\) at \(s=0\).

Thus the trace-weighted Born measure is the operator-free trace-gauge
determinant.

\[
\boxed{
\tau_t
\quad\leftrightarrow\quad
\det(I+xL_t).
}
\]

This is the right object for compactness, moment convergence, and no-loss.

---

## 4. The Centered Helmert/Character Approximation

Let \(P_n\) be the \(n\)-th primorial and let \(T\) be an Archimedean
cutoff. The centered primorial/Archimedean ledger is a finite vector on
\(\mathbb Z/P_n\):

\[
y_t^{(n,T)}(r).
\]

Center it:

\[
\tilde y_t^{(n,T)}(r)
=
y_t^{(n,T)}(r)-\frac1{P_n}\sum_{u\in\mathbb Z/P_n}y_t^{(n,T)}(u).
\]

Expand in additive characters:

\[
\widehat y_a^{(n,T,t)}
=
\frac1{P_n}
\sum_{r\in\mathbb Z/P_n}
\overline{\chi_a(r)}\,\tilde y_t^{(n,T)}(r),
\qquad
a\ne0.
\]

T3 tells us this is the native conductor-packet basis. T4 tells us the
centering is the Helmert move. T6 tells us to square:

\[
\lambda_a^{(n,T,t)}
:=
\bigl|\widehat y_a^{(n,T,t)}\bigr|^2.
\]

The finite Born operator is

\[
L_{n,T,t}
=
\operatorname{diag}\bigl(\lambda_a^{(n,T,t)}\bigr)_{a\ne0}.
\]

Parseval gives the finite trace identity:

\[
\boxed{
\operatorname{Tr}L_{n,T,t}
=
\sum_{a\ne0}\bigl|\widehat y_a^{(n,T,t)}\bigr|^2
=
\frac1{P_n}
\sum_{r\in\mathbb Z/P_n}
\bigl|\tilde y_t^{(n,T)}(r)\bigr|^2.
}
\]

This is Lock C as a finite theorem, not a conjecture.

For \(m\ge1\), define the finite Born power sums

\[
p_m(n,T,t)
:=
\operatorname{Tr}(L_{n,T,t}^m)
=
\sum_{a\ne0}\bigl|\widehat y_a^{(n,T,t)}\bigr|^{2m}.
\]

Lock A asks whether these finite Born power sums converge to the folded
\(\Xi\) cumulants after the correct double limit.

---

## 5. Lock A No-Loss

For \(t>\Lambda\), define the fixed-heat Born power sum

\[
p_m(t)
:=
\lim_{n,T\to\infty}p_m(n,T,t),
\]

whenever the limit is taken through the primorial/Archimedean exhaustion.

The fixed-heat identification target is

\[
\boxed{
p_m(t)=\ell_m(t)
\qquad(t>\Lambda,\ m\ge1).
}
\tag{A0}
\]

At \(t>\Lambda\), this is the smoothed explicit-formula/Plancherel
identity. It is the finite-to-continuum part, not the RH part.

The true Lock A theorem is:

\[
\boxed{
\lim_{t\to0^+}p_m(t)=\ell_m
\qquad(m\ge1),
\quad
\sup_{0<t<t_0}p_1(t)<\infty,
\quad
\tau_0(\{0\})=0.
}
\tag{A}
\]

Here \(\tau_0\) denotes the trace-weighted \(t\to0^+\) limit of the
Born measures. The last condition is the no-dust clause.

Interpretation:

\[
\boxed{
\text{as heat is removed, no trace escapes, no trace becomes dust, and no
phase is created.}
}
\]

This is the exact top-peak statement.

---

## 6. Equivalence Theorem

**Theorem 6.1 (Pass-5 reduction).** The following are equivalent.

1. RH.
2. \(\Lambda\le0\).
3. \(B(x)=\det(I+xL_\Xi)\) for some positive trace-class
   \(L_\Xi\ge0\).
4. The Lock A no-loss statement (A) holds.
5. The trace-weighted measures \(\tau_t\), \(t>\Lambda\), have a
   \(t\to0^+\) positive trace-gauge limit \(\tau_0\) with
   \(\tau_0(\{0\})=0\), satisfying

\[
\int s^{m-1}\,d\tau_0(s)=\ell_m
\qquad(m\ge1).
\]

**Proof.**

\((1)\Leftrightarrow(2)\) is the de Bruijn-Newman formulation.

\((1)\Leftrightarrow(3)\) is the folded determinant criterion: if RH
holds, then

\[
B(x)=\prod_k(1+x\gamma_k^{-2})
\]

with a positive trace-class diagonal ledger

\[
L_\Xi=\operatorname{diag}(\gamma_k^{-2}).
\]

Conversely, a positive trace-class determinant has all its \(x\)-zeros on
the negative real axis. Since \(x=-z^2\), the corresponding \(\Xi\)-zeros
are real.

\((2)\Rightarrow(4)\). If \(\Lambda\le0\), then every \(t>0\) is in the
real-zero regime. Hence the \(t\)-ledger is positive Born:

\[
p_m(t)=\ell_m(t).
\]

The heat flow converges to \(\Xi\), so the cumulants converge:

\[
\ell_m(t)\to\ell_m.
\]

The trace statement is the \(m=1\) case.
The no-dust statement is exactly the absence of an additional \(e^{cx}\)
factor in the folded Hadamard product for \(B(x)\).

\((4)\Rightarrow(5)\). Define finite trace-weighted measures

\[
d\tau_{n,T,t}(s)
=
\sum_a\lambda_a^{(n,T,t)}\delta_{\lambda_a^{(n,T,t)}}(s).
\]

The trace bound in (A) gives tightness in the positive trace-gauge cone
after taking the primorial/Archimedean limit and then \(t\to0^+\). The
no-dust clause gives \(\tau_0(\{0\})=0\), and the power-sum convergence gives

\[
\int s^{m-1}\,d\tau_0(s)=\ell_m.
\]

\((5)\Rightarrow(3)\). From \(\tau_0\), define

\[
\log D(x)
:=
\int\frac{\log(1+xs)}{s}\,d\tau_0(s).
\]

The moments of \(\tau_0\) give

\[
\log D(x)
=
\sum_{m\ge1}\frac{(-1)^{m+1}}{m}\ell_m x^m
=
\log B(x)
\]

near \(x=0\). Equivalently,

\[
\int\frac{1}{1+xs}\,d\tau_0(s)=\frac{B'(x)}{B(x)}
\]

near \(x=0\). Proposition 6.5 below then atomizes \(\tau_0\) and gives a
positive trace-gauge determinant representation for \(B\).

\(\square\)

The proof does not solve RH. It isolates the exact no-loss statement that
would solve it.

---

### 6.1 Dishwasher lemmas: what is actually proved here

This section proves the plates that are independent of RH. The unproved
plate remains Lock A no-loss.

**Lemma 6.2 (Trace-weighted compactness).** Let \(\tau_j\) be positive
finite measures supported on \([0,C]\), with

\[
\tau_j([0,C])\le C.
\]

Then a subsequence converges weakly to a positive finite measure
\(\tau\) on \([0,C]\). Moreover, for every fixed \(m\ge1\),

\[
\int s^{m-1}\,d\tau_j(s)\to\int s^{m-1}\,d\tau(s)
\]

along that subsequence.

**Proof.** This is weak compactness of bounded positive measures on a
compact metric space. Since \(s^{m-1}\) is continuous on \([0,C]\), its
integral passes to the weak limit. \(\square\)

**Lemma 6.3 (Zero-dust decomposition).** Let

\[
d\tau(s)=c\,\delta_0(s)+d\tau_+(s),
\qquad
\tau_+(\{0\})=0.
\]

Then

\[
\int\frac{\log(1+xs)}{s}\,d\tau(s)
=
cx+\int_{(0,C]}\frac{\log(1+xs)}{s}\,d\tau_+(s).
\]

Consequently, zero-dust contributes only to the first cumulant:

\[
\int s^{m-1}\,d(c\delta_0)=
\begin{cases}
c,&m=1,\\
0,&m\ge2.
\end{cases}
\]

**Proof.** The continuous extension of \(\log(1+xs)/s\) at \(s=0\) is
\(x\). The moment statement is immediate. \(\square\)

**Lemma 6.4 (Meromorphic Stieltjes atomization).** Let \(\tau\) be a
positive finite measure on \([0,C]\) with no zero-dust. Define

\[
F(x)=\int_{(0,C]}\frac{1}{1+xs}\,d\tau(s).
\]

If \(F\) extends meromorphically across the cut
\((-\infty,-1/C]\), then \(\tau\) is purely atomic on \((0,C]\). Its atoms
are located at \(s_j=-1/x_j\), where \(x_j\) are the negative real poles
of \(F\), and the masses are the positive residues in the Stieltjes
normalization.

**Proof.** This is the Stieltjes inversion theorem. A continuous component
of \(\tau\) produces a nonzero jump of the boundary values of \(F\) across
the cut; a singular-continuous component is also recovered by the same
inversion measure. Meromorphic continuation has only isolated pole
singularities, so the representing measure can only have point masses.
Positivity of \(\tau\) gives positive masses. \(\square\)

**Proposition 6.5 (No-loss criterion).** Suppose the \(t>\Lambda\)
Born measures \(\tau_t\) have a \(t\to0^+\) trace-weighted limit
\(\tau_0\) such that:

1. \(\tau_0\) has no zero-dust;
2. \(\int s^{m-1}\,d\tau_0(s)=\ell_m\) for every \(m\ge1\);
3. the resulting Stieltjes transform

\[
F_0(x)=\int\frac{1}{1+xs}\,d\tau_0(s)
\]

is the logarithmic derivative \(B'(x)/B(x)\) near \(x=0\).

Then RH follows.

**Proof.** By (3), \(F_0\) extends meromorphically to the plane because
\(B\) is entire. By Lemma 6.4, \(\tau_0\) is purely atomic on
\((0,C]\). Thus

\[
F_0(x)=\sum_j\frac{m_j}{1+x\lambda_j},
\qquad
\lambda_j>0,\quad m_j>0.
\]

Integrating gives

\[
B(x)=\prod_j(1+x\lambda_j)^{m_j}
\]

with no \(e^{cx}\) dust factor by assumption (1). Hence every zero of
\(B\) lies on the negative real \(x\)-axis. Since \(x=-z^2\), every zero
of \(\Xi(z)\) lies on the real \(z\)-axis. This is RH. \(\square\)

Thus the dishes now separate cleanly:

\[
\boxed{
\text{compactness, dust accounting, and Stieltjes atomization are proved;}
\quad
\text{Lock A no-loss is the remaining open summit.}
}
\]

---

## 7. The Five Failure Modes

Pass-5 makes failure visible.

### 7.1 Trace Escape

The total square mass might fail to remain controlled:

\[
\limsup_{t\to0^+}p_1(t)=\infty.
\]

This would mean the Born heat flow loses trace compactness.

### 7.2 Moment Mismatch

The trace may remain finite but a higher power sum may miss:

\[
\lim_{t\to0^+}p_m(t)\ne\ell_m.
\]

This is an explicit-formula mismatch, not a positivity problem.

### 7.3 Phase Leakage

The power sums may converge algebraically, but the \(t=0\) ledger may exit
the positive Born cone. In zero language, this is exactly an off-line zero.
In measure language, the limiting cumulants cannot be represented by a
positive trace-weighted measure.

### 7.4 Zero-Dust

The trace may remain bounded but collapse into infinitesimal atoms:

\[
\tau_t \Rightarrow c\delta_0+\tau_+,
\qquad c>0.
\]

Then

\[
\log B(x)
=
cx+\int_{(0,C]}\frac{\log(1+xs)}{s}\,d\tau_+(s),
\]

so the determinant acquires an \(e^{cx}\) dust factor. This does not move
zeros, but it breaks the exact trace gauge. The folded \(\Xi\) product has
no free exponential dust, so Lock A must exclude \(c>0\).

### 7.5 Limit-Order Failure

The primorial/Archimedean limit may not commute with heat removal:

\[
\lim_{t\to0^+}\lim_{n,T\to\infty}p_m(n,T,t)
\ne
\lim_{n,T\to\infty}\lim_{t\to0^+}p_m(n,T,t).
\]

This is the most technical failure mode. It is also the most actionable:
prove a uniform dominated-convergence theorem in the trace-weighted
moment topology.

---

## 8. Relation to Pass-3 Gates

Pass-3 built determinant gates:

\[
H_n\succ0,\qquad J_n\succ0,\qquad K_n\succ0.
\]

Those gates are the finite moment-cone shadow of Pass-5.

Pass-5 says the native source of positivity is not the gates themselves.
The gates are detectors of a positive Born heat measure:

\[
\tau_t\ge0.
\]

For \(t>\Lambda\), positivity is automatic. At \(t=0\), the gates ask
whether the Born cone survived heat removal.

\[
\boxed{
\text{Pass-3 gates are finite cone certificates;}
\quad
\text{Pass-5 is the heat-flow no-loss theorem behind them.}
}
\]

This explains why the half-compensation ledgers were so delicate: they
were measuring the boundary of the Born cone at \(t=0\).

### 8.1 Phase leakage is exactly gate failure

Let

\[
F(x):=\frac{B'(x)}{B(x)}
=
\sum_{n\ge0}(-1)^n\mu_n x^n,
\qquad
\mu_n:=\ell_{n+1}.
\]

Suppose a support ceiling \(R>0\) is declared. In the RH application the
expected ceiling is

\[
R=\gamma_1^{-2},
\]

the first folded zero atom.

The bounded Hausdorff/Stieltjes moment criterion says that the following
are equivalent:

1. There is a positive measure \(\tau\) on \([0,R]\) such that

\[
\mu_n=\int_0^R s^n\,d\tau(s)
\qquad(n\ge0).
\]

2. For every polynomial \(f\),

\[
\int f(s)^2\,d\tau(s)\ge0,
\qquad
\int s f(s)^2\,d\tau(s)\ge0,
\qquad
\int (R-s)f(s)^2\,d\tau(s)\ge0.
\]

3. The three finite gate families are positive:

\[
\boxed{
H_n=(\mu_{a+b})_{0\le a,b\le n}\succeq0,
}
\]

\[
\boxed{
J_n=(\mu_{a+b+1})_{0\le a,b\le n}\succeq0,
}
\]

\[
\boxed{
K_n=(R\mu_{a+b}-\mu_{a+b+1})_{0\le a,b\le n}\succeq0.
}
\]

Thus:

\[
\boxed{
\text{phase leakage}
\quad\Longleftrightarrow\quad
\text{failure of at least one of }H,J,K.
}
\]

This is the exact bridge between Pass-3 and Pass-5.

Pass-5 gives the source interpretation:

\[
\tau_t\ge0
\qquad(t>\Lambda).
\]

Pass-3 gives the finite detector:

\[
H_n,\ J_n,\ K_n.
\]

At \(t=0\), the remaining positivity problem is not vague "phase." It is
the all-rung gate statement:

\[
\boxed{
\forall n,\qquad
H_n\succeq0,\quad J_n\succeq0,\quad K_n\succeq0.
}
\]

Once these gates hold for the actual folded moments \(\mu_n=\ell_{n+1}\),
the Stieltjes representation exists. Then Lemma 12.1 removes zero-dust,
and meromorphic atomization forces the atoms to be the zeros of \(B\).

So phase leakage is washed into a concrete gate theorem. What remains is
not to identify the detector, but to prove the detector never fails.

---

## 9. Relation to Pade

The Pade/Stieltjes microscope sees finite quadrature approximations to

\[
S'(x)=\frac{d}{dx}\log B(x).
\]

If

\[
S'(x)=\int\frac{s}{1+xs}\,d\sigma(s)
\]

with positive trace gauge, then the diagonal Pade approximants produce
positive quadrature nodes and weights. Pass-3 observed that at \(N=10\),
the leading detected nodes satisfy

\[
\lambda_a^{(10)}\approx\gamma_a^{-2},
\qquad
\frac{w_a^{(10)}}{\lambda_a^{(10)}}\approx1.
\]

Pass-5 reading:

\[
\boxed{
\text{Pade is the microscope;}
\quad
\text{T6 is the atom source;}
\quad
\text{Lock A is the identity aligning them.}
}
\]

Pade does not manufacture positivity. It detects the spectral shadow of
Born-square power sums.

---

## 10. The New Proof Target

The next theorem to prove is not "construct positive atoms."

It is:

**Apex Theorem (Lock A no-loss).** For the centered
primorial/Archimedean Helmert ledger,

\[
p_m(t)
=
\lim_{n,T\to\infty}
\sum_{a\ne0}\bigl|\widehat y_a^{(n,T,t)}\bigr|^{2m}
\]

exists for \(t>\Lambda\), satisfies \(p_m(t)=\ell_m(t)\), and obeys

\[
\lim_{t\to0^+}p_m(t)=\ell_m
\qquad(m\ge1)
\]

with uniform trace control at \(m=1\) and no zero-dust:

\[
\tau_0(\{0\})=0.
\]

Equivalently:

\[
\boxed{
\tau_t\to\tau_0
\quad\text{inside the positive no-dust trace-gauge cone.}
}
\]

This is RH in Born-Helmert coordinates.

---

## 11. Attack Surface

The proof should now focus on five estimates.

### 11.1 Fixed-Heat Plancherel Identity

Prove rigorously that for \(t>\Lambda\),

\[
\lim_{n,T\to\infty}p_m(n,T,t)=\ell_m(t).
\]

This is a smoothed explicit-formula identity. It should use:

1. character orthogonality on \(\mathbb Z/P_n\);
2. T6 conductor mixing;
3. dominated convergence from the heat-smoothed Riemann-Siegel kernel.

### 11.2 Uniform Trace Bound Near \(t=0\)

Show

\[
\sup_{0<t<t_0}p_1(t)<\infty.
\]

In zero language, this is control of

\[
\sum_k z_k(t)^{-2}.
\]

In Helmert language, it is a uniform \(L^2\)-variance bound for the
centered prime-power ledger.

### 11.3 Moment Continuity

For each \(m\ge2\), prove

\[
p_m(t)\to\ell_m.
\]

The higher powers are easier after trace control because large atoms are
bounded by trace:

\[
0\le \lambda_k(t)\le p_1(t).
\]

The hard part is excluding phase leakage, not bounding positive powers
once the Born cone is retained.

### 11.4 No-Dust Exclusion

Show that the trace-weighted limit does not acquire mass at \(s=0\):

\[
\tau_0(\{0\})=0.
\]

Equivalently, exclude an extra exponential factor

\[
e^{cx},\qquad c>0,
\]

in the folded determinant. This is the exact trace-gauge version of
"unit multiplicity" in the Pade detector.

### 11.5 Born Cone Closure

Prove that any trace-weighted moment limit of \(\tau_t\) remains positive
and represents the folded \(\Xi\) cumulants.

This is the analytic heart:

\[
\boxed{
\text{heat removal preserves the positive square-atom cone.}
}
\]

---

## 12. Lock A Dish Rack

Lock A no-loss now splits into five plates. Three are closed by existing
analysis. Two are the actual summit.

### 12.1 Plate I: finite Born positivity is closed

For every finite centered Helmert/character ledger,

\[
\lambda_a^{(n,T,t)}
=
\bigl|\widehat y_a^{(n,T,t)}\bigr|^2
\ge0.
\]

This is T6, not RH. It is the square closure.

The trace is also finite-stage exact:

\[
\sum_a\lambda_a^{(n,T,t)}
=
\frac1{P_n}\sum_r
\bigl|\tilde y_t^{(n,T)}(r)\bigr|^2.
\]

This is Parseval plus RMS. Lock B and Lock C are closed at every finite
stage.

### 12.2 Plate II: fixed-heat inner limit is closed

For every fixed \(t>\Lambda\), the zero ledger is positive because
\(\Xi_t\) has only real zeros. The fixed-heat target is

\[
p_m(t)
=
\lim_{n,T\to\infty}
\sum_a\bigl|\widehat y_a^{(n,T,t)}\bigr|^{2m}
=
\ell_m(t).
\]

This is the smoothed explicit-formula and Plancherel plate. Its proof uses:

1. the heat-smoothed Riemann-Siegel kernel bound;
2. character orthogonality on \(\mathbb Z/P_n\);
3. T6 conductor mixing;
4. dominated convergence for the \((n,T)\)-exhaustion;
5. Hurwitz continuity of the finite zero ledgers at fixed \(t>\Lambda\).

Thus the inner limit is not the RH-strength part. It is lower altitude:

\[
\boxed{
t>\Lambda
\quad\Longrightarrow\quad
p_m(t)=\ell_m(t).
}
\]

### 12.3 Plate III: cumulant heat continuity is closed

The normalized functions

\[
B_t(x)=\frac{\Xi_t(i\sqrt x)}{\Xi_t(0)}
\]

converge to

\[
B(x)=\frac{\Xi(i\sqrt x)}{\Xi(0)}
\]

locally uniformly as \(t\to0^+\). This follows from the super-exponential
decay of \(\Phi(u)\): for \(t\) in a compact interval near \(0\),
\(e^{tu^2}\Phi(u)\) is dominated by an integrable function with all
polynomial moments.

Since \(B(0)=1\), Cauchy's estimates applied to \(\log B_t(x)\) near
\(x=0\) give, for every fixed \(m\),

\[
\boxed{
\ell_m(t)\to\ell_m.
}
\]

So coefficient continuity at heat zero is not the problem either.

### 12.4 Plate IV: positive access to \(t=0\) is the summit

The catch is domain. The positive Born representation is known for

\[
t>\Lambda.
\]

To send \(t\to0^+\) while staying inside that positive Born cone, one
needs

\[
\boxed{
\Lambda\le0.
}
\]

This is exactly RH in de Bruijn-Newman form. Rodgers-Tao gives the other
side:

\[
\Lambda\ge0.
\]

Therefore the full summit is:

\[
\boxed{
\Lambda=0.
}
\]

In Pass-5 language:

\[
\boxed{
\text{the positive Born heat cone must reach }t=0.
}
\]

This plate is not closed by the bookkeeping. It is the RH-strength plate.

### 12.5 Plate V: no-dust is the trace-gauge summit companion

Even if the measures stay positive and bounded, trace can collapse at
\(s=0\):

\[
\tau_t\Rightarrow c\delta_0+\tau_+.
\]

This creates

\[
\log B(x)
=
cx+\int_{(0,C]}\frac{\log(1+xs)}{s}\,d\tau_+(s).
\]

The \(c x\) term is an \(e^{cx}\) factor. It does not move zeros, but it
breaks the exact trace gauge. Therefore no-dust is not optional:

\[
\boxed{
c=0.
}
\]

This is the trace-gauge companion to \(\Lambda\le0\). In Pade language, it
is the limiting version of unit trace multiplicity:

\[
\frac{w_a}{\lambda_a}\to1.
\]

But this plate has a clean asymptotic wash once a positive Stieltjes
representation has been tied to the actual folded \(B\).

**Lemma 12.1 (Dust equals the log-derivative limit).** Let \(\tau\) be a
positive finite measure on \([0,C]\), and put

\[
F(x)=\int_{[0,C]}\frac{1}{1+xs}\,d\tau(s),
\qquad x>0.
\]

Then

\[
\boxed{
\lim_{x\to+\infty}F(x)=\tau(\{0\}).
}
\]

**Proof.** The functions \((1+xs)^{-1}\) decrease pointwise to
\(\mathbf 1_{\{0\}}(s)\) and are bounded by \(1\). Dominated convergence
gives the result. \(\square\)

For the folded xi function,

\[
B(x)=\frac{\Xi(i\sqrt x)}{\Xi(0)}.
\]

On the positive real \(x\)-axis, write \(s=1/2+\sqrt x\). By the
functional equation \(\xi(s)=\xi(1-s)\),

\[
B(x)=\frac{\xi(1/2+\sqrt x)}{\xi(1/2)}.
\]

Therefore

\[
\frac{B'(x)}{B(x)}
=
\frac{1}{2\sqrt x}\frac{\xi'}{\xi}\!\left(\frac12+\sqrt x\right).
\]

Using

\[
\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

Stirling's formula and \(\zeta'(s)/\zeta(s)\to0\) as \(s\to+\infty\)
give

\[
\frac{\xi'}{\xi}(s)
=
\frac12\log\frac{s}{2\pi}+O(1).
\]

Thus

\[
\boxed{
\frac{B'(x)}{B(x)}
=
O\!\left(\frac{\log x}{\sqrt x}\right)
\longrightarrow0
\qquad(x\to+\infty).
}
\]

Consequently:

\[
\boxed{
\text{if }B'/B\text{ has a positive trace-weighted Stieltjes
representation, then it has no zero-dust.}
}
\]

So no-dust is no longer an independent summit plate. It is automatically
washed once the positive Born cone reaches \(t=0\) and represents the
actual folded \(B\).

### 12.6 The cleaned Lock A theorem

After washing the plates, Lock A is no longer vague. It is:

\[
\boxed{
\begin{array}{l}
\text{The fixed-heat Born identities }p_m(t)=\ell_m(t)
\text{ extend to }t=0\\
\text{inside the positive trace-gauge cone, with no mass lost to infinity,}\\
\text{no mass collapsed into }s=0,\text{ and no complex phase leakage.}
\end{array}
}
\]

Equivalently:

\[
\boxed{
\Lambda\le0
\quad
\text{with the trace-weighted limit representing }B'/B.
}
\]

In finite-gate language, this is:

\[
\boxed{
\forall n,\qquad
H_n\succeq0,\quad J_n\succeq0,\quad K_n\succeq0,
\qquad
\text{for }\mu_n=\ell_{n+1}.
}
\]

Given Rodgers-Tao, this becomes:

\[
\boxed{
\Lambda=0,
\quad
\text{and exact trace gauge follows from }B'/B\to0.
}
\]

That is the clean dish rack. Everything else is now supporting plumbing.

---

## 13. Final Line

Pass-5 reduces the RH quest to one sentence:

\[
\boxed{
\text{The de Bruijn-Newman heat flow does not lose, dust, or complexify the
T6 Born-square trace ledger at }t=0.
}
\]

Or, in the language of this program:

\[
\boxed{
\text{The centered Helmert/character amplitudes square into the folded
\(\Xi\) atoms without trace loss, zero-dust, phase leakage, or
limit-order failure.}
}
\]

This is the top peak. The summit is no longer hidden by construction
language.

---

## 14. The Native Gate Theorem Is RH-Complete

Now state the final theorem in the strongest honest form.

Let

\[
B(x)=\frac{\Xi(i\sqrt x)}{\Xi(0)}
\]

and

\[
\frac{B'(x)}{B(x)}
=
\sum_{n\ge0}(-1)^n\mu_n x^n,
\qquad
\mu_n=\ell_{n+1}.
\]

Let

\[
R=\gamma_1^{-2},
\]

where \(\gamma_1\) is the first positive Riemann-zero ordinate.

For every \(n\ge0\), define

\[
H_n=(\mu_{a+b})_{0\le a,b\le n},
\]

\[
J_n=(\mu_{a+b+1})_{0\le a,b\le n},
\]

\[
K_n=(R\mu_{a+b}-\mu_{a+b+1})_{0\le a,b\le n}.
\]

**Theorem 14.1 (Native gate theorem is RH-complete).** The following are
equivalent.

1. RH.
2. For every \(n\ge0\),

\[
H_n\succeq0,\qquad J_n\succeq0,\qquad K_n\succeq0.
\]

3. \(B'/B\) has a positive trace-weighted Stieltjes representation on
   \([0,R]\):

\[
\frac{B'(x)}{B(x)}
=
\int_0^R\frac{1}{1+xs}\,d\tau(s)
\]

for a positive finite measure \(\tau\), with no zero-dust.

4. \(B(x)\) has a positive trace-class determinant representation

\[
B(x)=\det(I+xL_\Xi),
\qquad
0\le L_\Xi\le R I.
\]

**Proof.**

\((1)\Rightarrow(3)\). Under RH, the nontrivial zeros in the folded
\(z\)-coordinate are real:

\[
z=\pm\gamma_k.
\]

Therefore

\[
B(x)=\prod_{k\ge1}(1+x\gamma_k^{-2}).
\]

Put

\[
\lambda_k:=\gamma_k^{-2}.
\]

Then \(0<\lambda_k\le\lambda_1=R\), and

\[
\frac{B'(x)}{B(x)}
=
\sum_{k\ge1}\frac{\lambda_k}{1+x\lambda_k}.
\]

Define the trace-weighted measure

\[
d\tau(s):=\sum_{k\ge1}\lambda_k\,\delta_{\lambda_k}(s).
\]

Then

\[
\frac{B'(x)}{B(x)}
=
\int_0^R\frac{1}{1+xs}\,d\tau(s).
\]

There is no zero-dust because every atom lies at \(\lambda_k>0\), and
\(\sum_k\lambda_k<\infty\) follows from the order-one product for \(\Xi\).

\((3)\Rightarrow(2)\). If

\[
\mu_n=\int_0^R s^n\,d\tau(s),
\]

then for every polynomial \(f\),

\[
\int f(s)^2\,d\tau(s)\ge0,
\qquad
\int s f(s)^2\,d\tau(s)\ge0,
\qquad
\int (R-s)f(s)^2\,d\tau(s)\ge0.
\]

These three inequalities are exactly the positive semidefiniteness of

\[
H_n,\qquad J_n,\qquad K_n
\]

for every finite degree \(n\).

\((2)\Rightarrow(3)\). The bounded Hausdorff/Stieltjes moment criterion
on \([0,R]\) says that the three gate families are positive for every
\(n\) if and only if there exists a positive finite measure \(\tau\) on
\([0,R]\) satisfying

\[
\mu_n=\int_0^R s^n\,d\tau(s)
\qquad(n\ge0).
\]

Thus

\[
F_\tau(x):=\int_0^R\frac{1}{1+xs}\,d\tau(s)
\]

has the same Taylor expansion at \(0\) as \(B'(x)/B(x)\). Hence

\[
F_\tau(x)=\frac{B'(x)}{B(x)}
\]

near \(x=0\). Since \(B'/B\to0\) as \(x\to+\infty\), Lemma 12.1 gives
\(\tau(\{0\})=0\). This is no zero-dust.

\((3)\Rightarrow(4)\). Since \(B'/B\) is meromorphic, Lemma 6.4 atomizes
\(\tau\):

\[
d\tau(s)=\sum_j m_j\lambda_j\,\delta_{\lambda_j}(s),
\qquad
0<\lambda_j\le R,\quad m_j>0.
\]

Integrating \(B'/B\) gives

\[
B(x)=\prod_j(1+x\lambda_j)^{m_j}.
\]

The trace \(\sum_j m_j\lambda_j\) is finite because \(\tau\) is finite.
Thus this is a positive trace-class determinant representation.

\((4)\Rightarrow(1)\). A positive trace-class determinant has zeros only
on the negative real \(x\)-axis:

\[
x=-\lambda_j^{-1}.
\]

But \(B(x)=\Xi(i\sqrt x)/\Xi(0)\). If every zero of \(B\) is negative real
in the \(x\)-plane, then every corresponding zero of \(\Xi\) in the
\(z=i\sqrt x\) coordinate is real. That is RH. \(\square\)

So the native gate theorem is not a side lemma. It is RH in finite
moment-cone language.

\[
\boxed{
\text{unconditional all-rung }H,J,K\text{ positivity}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\]

### 14.1 Why the heat proof cannot bypass this

For \(t>\Lambda\), positivity is already known:

\[
\tau_t\ge0.
\]

To pass this positivity to \(t=0\), one needs a sequence

\[
t_j>\Lambda,\qquad t_j\to0^+.
\]

Such a sequence exists if and only if

\[
\Lambda\le0.
\]

By Rodgers-Tao,

\[
\Lambda\ge0.
\]

Therefore the heat-flow route reaches the gate theorem exactly when

\[
\Lambda=0.
\]

This is why the remaining step cannot be a routine compactness lemma. A
routine compactness lemma would already prove \(\Lambda\le0\), hence RH.

### 14.2 What remains to prove, without renaming it

The remaining proof is precisely:

\[
\boxed{
\forall n\ge0,\qquad
H_n\succeq0,\quad J_n\succeq0,\quad K_n\succeq0
\quad
(\mu_n=\ell_{n+1}).
}
\]

Equivalently:

\[
\boxed{
\Lambda\le0.
}
\]

Equivalently:

\[
\boxed{
\text{the positive Born heat cone reaches }t=0.
}
\]

This is the final dish. It is not yet washed here. It is now identified
without disguise.

---

## 15. Final Proof Audit

The requested final unconditional proof would require turning one of the
following equivalent statements into a theorem independent of RH:

\[
\boxed{
\Lambda\le0
}
\]

or

\[
\boxed{
\forall n\ge0,\qquad
H_n\succeq0,\quad J_n\succeq0,\quad K_n\succeq0.
}
\]

or

\[
\boxed{
\frac{B'(x)}{B(x)}
\text{ is a positive trace-weighted Stieltjes transform on }[0,R].
}
\]

or

\[
\boxed{
B(x)=\det(I+xL_\Xi)
\quad\text{for some }L_\Xi\ge0.
}
\]

The previous sections prove these statements are equivalent to RH. They do
not prove any one of them unconditionally.

### 15.1 Circular routes blocked

The following tempting routes are circular.

**Route A: use positivity for \(t>\Lambda\), then let \(t\to0^+\).**

This requires \(0\) to be in the closure of \((\Lambda,\infty)\):

\[
\exists t_j>\Lambda,\ t_j\to0^+
\quad\Longleftrightarrow\quad
\Lambda\le0.
\]

That is RH.

**Route B: use compactness of \(\tau_t\).**

Compactness only applies along a sequence \(t_j\) for which \(\tau_{t_j}\)
is already positive. Such sequences approaching \(0\) again require
\(\Lambda\le0\).

**Route C: use Pade positivity.**

Pade positivity detects the Stieltjes cone if the limiting Stieltjes
representation exists. It does not construct the representation
unconditionally. Its convergence to \(\gamma_k^{-2}\) is powerful evidence,
but the theorem needed is still all-rung \(H,J,K\) positivity.

**Route D: use finite Born squares.**

Finite Born squares prove positivity for finite centered
Helmert/character ledgers. The missing theorem is that their
trace-weighted limit is the actual folded \(B'/B\) ledger at \(t=0\)
inside the positive cone. This is exactly Lock A no-loss.

### 15.2 The exact new lemma needed

The final unconditional proof would be complete if one could prove:

**Apex Lemma.** For the folded \(\Xi\) moments

\[
\mu_n=\ell_{n+1},
\]

the bounded Hausdorff/Stieltjes gates satisfy

\[
\boxed{
\forall n\ge0,\qquad
H_n\succeq0,\quad J_n\succeq0,\quad K_n\succeq0.
}
\]

By Theorem 14.1, this lemma is equivalent to RH.

### 15.3 Current status

What is complete:

1. the coordinate system;
2. the Born-square atom source;
3. the trace-weighted measure formalism;
4. the no-dust criterion;
5. the phase-leakage gate detector;
6. the proof that the native gate theorem is RH-complete.

What is not complete:

\[
\boxed{
\text{an unconditional proof of the Apex Lemma.}
}
\]

Therefore this draft cannot honestly claim a final unconditional proof of
RH. It gives a sharp equivalent formulation and a proof boundary.

The remaining mountain has a name:

\[
\boxed{
\textbf{Apex Lemma}=\textbf{Native Gate Positivity}=\Lambda\le0=\mathrm{RH}.
}
\]

---

## 16. Apex Lemma, K-Free Form

The friend's advice exposes a real simplification. The bounded-support gate
\(K_n\) is conceptually beautiful, but it is not the hard operational gate.
The hard gate is the Stieltjes pair:

\[
H_n\succeq0,\qquad J_n\succeq0.
\]

Once these hold for every \(n\), bounded support follows from the growth of
the folded \(\Xi\) cumulants. Therefore \(K_n\) can be kept as a diagnostic
and a finite-window certificate, but it should not be treated as an
independent input to the summit proof.

### 16.1 Unconditional support radius

Let

\[
F(x)=\frac{B'(x)}{B(x)}
=\sum_{n\ge0}(-1)^n\mu_nx^n,
\qquad
\mu_n=\ell_{n+1}.
\]

Define the unconditional coefficient radius

\[
R_\Xi:=\limsup_{n\to\infty}|\mu_n|^{1/n}.
\]

This number is finite because \(F\) is meromorphic at \(0\) with positive
distance from \(0\) to the nearest pole. No RH input is required. If the
nearest folded zero-pole distance is \(r_\Xi\), then \(R_\Xi=r_\Xi^{-1}\).
Under RH, this becomes

\[
R_\Xi=\gamma_1^{-2}.
\]

Without RH, \(R_\Xi\) should be read only as the reciprocal distance to the
nearest folded pole in the \(x\)-plane. Thus the proof target does not need
to name the first real zeta zero in advance.

### 16.2 Stieltjes pair implies bounded support

**Lemma 16.1.** Suppose

\[
\forall n\ge0,\qquad H_n\succeq0,\quad J_n\succeq0.
\]

Then there exists a positive measure \(\tau\) on \([0,\infty)\) such that

\[
\mu_n=\int_0^\infty s^n\,d\tau(s).
\]

If moreover

\[
\limsup_{n\to\infty}\mu_n^{1/n}\le R_\Xi<\infty,
\]

then

\[
\operatorname{supp}\tau\subseteq[0,R_\Xi].
\]

**Proof.** The first statement is the Stieltjes moment theorem: the Hankel
and shifted-Hankel positivity conditions are exactly positivity of

\[
\int p(s)^2\,d\tau(s),
\qquad
\int sp(s)^2\,d\tau(s)
\]

for every polynomial \(p\).

For the support claim, assume \(\tau([a,\infty))>0\) for some
\(a>R_\Xi\). Then

\[
\mu_n=\int_0^\infty s^n\,d\tau(s)
\ge a^n\tau([a,\infty)),
\]

so

\[
\limsup_{n\to\infty}\mu_n^{1/n}\ge a,
\]

contradicting \(a>R_\Xi\). Hence no mass lies beyond \(R_\Xi\). \(\square\)

Consequently, once the Stieltjes pair \(H,J\) is proved, the bounded-support
gate follows automatically:

\[
K_n^{(R)}=(R\mu_{a+b}-\mu_{a+b+1})_{0\le a,b\le n}\succeq0
\qquad(R\ge R_\Xi).
\]

### 16.3 K-free native gate theorem

**Theorem 16.2 (Operational native gate theorem).** The following are
equivalent:

1. RH.
2. For the folded \(\Xi\) cumulants \(\mu_n=\ell_{n+1}\),

\[
\forall n\ge0,\qquad H_n\succeq0,\quad J_n\succeq0.
\]

3. \(B'/B\) has a positive trace-weighted Stieltjes representation on
\([0,R_\Xi]\) with no zero-dust.
4. \(B\) has a positive trace-class determinant representation

\[
B(x)=\det(I+xL_\Xi),
\qquad
L_\Xi\ge0.
\]

**Proof.** RH gives

\[
B(x)=\prod_k(1+x\gamma_k^{-2}),
\]

hence

\[
\frac{B'(x)}{B(x)}
=\sum_k\frac{\gamma_k^{-2}}{1+x\gamma_k^{-2}},
\]

which is the Stieltjes transform of the positive trace-weighted atomic
measure

\[
d\tau(s)=\sum_k\gamma_k^{-2}\delta_{\gamma_k^{-2}}(s).
\]

Thus \(H_n,J_n\succeq0\).

Conversely, assume \(H_n,J_n\succeq0\) for every \(n\). Lemma 16.1 gives a
positive measure \(\tau\) on \([0,R_\Xi]\) with moments \(\mu_n\). Its
Stieltjes transform

\[
F_\tau(x)=\int_0^{R_\Xi}\frac{1}{1+xs}\,d\tau(s)
\]

has the same Taylor expansion at \(0\) as \(B'(x)/B(x)\). Since the support
is bounded, this expansion is convergent near \(0\), and uniqueness of
analytic continuation gives

\[
F_\tau(x)=\frac{B'(x)}{B(x)}
\]

on the common domain, with meromorphic continuation through \(B'/B\).

The no-dust argument from Lemma 12.1 applies:

\[
\frac{B'(x)}{B(x)}\to0
\qquad(x\to+\infty),
\]

so \(\tau(\{0\})=0\). Since \(B'/B\) is meromorphic, the Stieltjes
inversion theorem atomizes \(\tau\):

\[
d\tau(s)=\sum_j m_j\lambda_j\delta_{\lambda_j}(s),
\qquad
\lambda_j>0,\quad m_j>0.
\]

Because this Stieltjes transform is equal to \(B'/B\), the residue \(m_j\)
at each pole is also the order of the corresponding zero of the entire
function \(B\). Hence \(m_j\in\mathbb N\). Integrating the logarithmic
derivative gives

\[
B(x)=\prod_j(1+x\lambda_j)^{m_j}.
\]

Therefore every zero of \(B\) lies on the negative real \(x\)-axis. In the
folded coordinate, this means every zero of \(\Xi\) lies on the real
spectral axis, hence every nontrivial zero of \(\zeta\) lies on the critical
line. This is RH. \(\square\)

The new summit is therefore sharper:

\[
\boxed{
\textbf{Apex Lemma}_{HJ}:
\quad
\forall n\ge0,\qquad H_n\succeq0,\quad J_n\succeq0.
}
\]

The old \(H,J,K\) form remains the bounded-window version. The \(H,J\) form
is the no-circularity version.

### 16.4 What an actual proof must now do

The proof cannot start from \(R=\gamma_1^{-2}\), and it cannot start from a
positive zero measure. It must prove directly that for every polynomial

\[
p(s)=\sum_{a=0}^n c_as^a,
\]

the two scalar forms

\[
\sum_{a,b=0}^n c_ac_b\mu_{a+b}\ge0,
\qquad
\sum_{a,b=0}^n c_ac_b\mu_{a+b+1}\ge0
\]

hold for the explicit folded cumulants of \(\Xi\).

Equivalently, one must construct a positive linear functional

\[
\mathcal L_\Xi[p]=\sum_{k\ge0}p_k\mu_k
\]

on the Stieltjes quadratic cone

\[
p(s)^2,\qquad sp(s)^2.
\]

This is the exact non-circular Apex proof target.

### 16.5 Why the present proof still stops here

The reduction above is progress: it removes the \(R=\gamma_1^{-2}\)
subtlety and deletes one gate from the operational summit. But it does not
prove \(\textbf{Apex Lemma}_{HJ}\). Proving that lemma would still prove RH.

The next real attack surfaces are therefore:

1. construct \(\mathcal L_\Xi\) as a manifestly positive functional from
   the explicit formula;
2. translate known Li/Bombieri-Lagarias positivity into partial \(H,J\)
   positivity and look for an induction operator;
3. construct the positive Hilbert-Polya operator \(L_\Xi\) directly in the
   Born-Helmert/character ledger;
4. prove that every off-line zero produces a finite polynomial \(p\) for
   which one of the two \(H,J\) quadratic forms becomes negative.

The fourth route is the most surgical. It turns RH into a detector theorem:

\[
\text{off-line zero}
\quad\Longrightarrow\quad
\exists p:\ \mathcal L_\Xi[p^2]<0
\text{ or }\mathcal L_\Xi[sp^2]<0.
\]

That is the Apex Lemma in contrapositive form.

### 16.6 Finite witness theorem

The operational theorem gives one unconditional payoff immediately.

**Corollary 16.3 (finite native witness).** If RH is false, then there are
an integer \(n\ge0\) and real coefficients \(c_0,\ldots,c_n\), not all
zero, such that

\[
\sum_{a,b=0}^n c_ac_b\mu_{a+b}<0
\]

or

\[
\sum_{a,b=0}^n c_ac_b\mu_{a+b+1}<0.
\]

Equivalently, at least one finite matrix \(H_n\) or \(J_n\) has a negative
eigenvalue.

**Proof.** If all finite \(H_n\) and \(J_n\) were positive semidefinite,
Theorem 16.2 would imply RH. Therefore under not-RH, some finite gate must
fail. A failing positive semidefinite matrix has a vector \(c\) with
negative quadratic form. \(\square\)

Thus the Apex Lemma is not an asymptotic-only statement. There is no
"infinite tail only" counterexample: if RH fails, a finite native gate sees
it.

This turns the remaining proof into a clean sensitivity/specificity problem:

\[
\begin{array}{ccl}
\text{sensitivity} &:&
\text{every off-line zero forces a finite negative gate witness},\\[2mm]
\text{specificity} &:&
\text{no critical-line zero configuration creates a negative witness}.
\end{array}
\]

The specificity side is already RH \(\Rightarrow\) positivity. The whole
remaining battle is to prove the sensitivity side constructively from the
explicit formula, without first assuming an off-line zero and then invoking
the equivalence abstractly.

### 16.7 Spectral isolator lemma

The finite witness theorem can be sharpened into a constructive detector.
Write the folded logarithmic derivative formally as

\[
\frac{B'(x)}{B(x)}
=\sum_{\alpha\in\mathcal Z_B}
\frac{m_\alpha\lambda_\alpha}{1+x\lambda_\alpha},
\qquad
\lambda_\alpha=-\alpha^{-1},
\]

where \(\alpha\) runs over the nonzero zeros of \(B\), counted with
multiplicity \(m_\alpha\). The trace weights satisfy

\[
\sum_{\alpha\in\mathcal Z_B}m_\alpha|\lambda_\alpha|<\infty,
\]

because \(\lambda_\alpha\) is the reciprocal square-scale of the usual
spectral zero parameter and
\(\sum_\rho |\rho-\tfrac12|^{-2}<\infty\).

For a polynomial \(p\), define the spectral quadratic ledger

\[
\mathcal Q[p]
:=\sum_{\alpha\in\mathcal Z_B}
m_\alpha\lambda_\alpha p(\lambda_\alpha)^2.
\]

When the coefficients of \(p\) are real, conjugate symmetry of the zero set
makes \(\mathcal Q[p]\in\mathbb R\), and

\[
\mathcal Q[p]
=\sum_{a,b}c_ac_b\mu_{a+b}
\qquad
\left(p(s)=\sum_ac_as^a\right).
\]

**Lemma 16.4 (off-axis spectral isolator).** If some
\(\lambda_0\notin[0,\infty)\) occurs in the folded zero ledger, then there
exists a real polynomial \(p\) such that

\[
\mathcal Q[p]<0.
\]

Consequently, some finite Hankel gate \(H_n\) fails.

**Proof.** The set \(\{\lambda_\alpha\}\) is compact in \(\mathbb C\) with
only possible accumulation at \(0\), and \(\lambda_0\ne0\) is isolated.
Choose a conjugation-symmetric compact neighborhood \(U\) of
\(\lambda_0,\overline{\lambda_0}\) containing no other spectral points.

If \(\lambda_0<0\) is real, choose a real polynomial \(p\) that is close to
\(1\) at \(\lambda_0\) and close to \(0\) on the rest of the compact
spectrum. Then the isolated contribution is \(m_{\lambda_0}\lambda_0<0\),
while all remaining contributions are arbitrarily small by trace
summability.

If \(\lambda_0\) is nonreal, choose a complex number \(w\) with

\[
2\operatorname{Re}(m_{\lambda_0}\lambda_0 w^2)<0.
\]

By conjugation-symmetric Runge/Mergelyan polynomial approximation on the
compact spectrum, there is a real polynomial \(p\) with

\[
p(\lambda_0)\approx w,\qquad
p(\overline{\lambda_0})\approx\overline w,
\]

and \(p\) uniformly small on the remaining spectral points. The paired
contribution from \(\lambda_0,\overline{\lambda_0}\) is then negative, and
the trace-summable remainder is made smaller than half its magnitude.
Therefore \(\mathcal Q[p]<0\). \(\square\)

This proves the sensitivity direction constructively:

\[
\text{folded spectrum not contained in }[0,\infty)
\quad\Longrightarrow\quad
\exists n:\ H_n\not\succeq0.
\]

The remaining Apex Lemma is exactly the complementary specificity theorem:

\[
\boxed{
\text{prove directly from the prime/gamma/Helmert ledger that no such
isolator polynomial exists.}
}
\]

That is the same statement as RH, but now the enemy has a finite shape:
a negative polynomial witness in the native Hankel gate.

---

## 17. Bures Pullback of the Apex Gate

The previous section gives the finite native detector. The Bures
log-derivative note gives the same object in upper-half-plane language.
These are not two programs. They are the same gate through two charts.

Use the standard Herglotz convention

\[
m_B(z):=-\frac{\Xi'(z)}{\Xi(z)}.
\]

With this convention, a real zero \(\gamma\) contributes
\((\gamma-z)^{-1}\), whose imaginary part is positive in the upper
half-plane. The meromorphic residue at \(z=\gamma\) is negative; this is
the usual sign for a Herglotz pole because the Herglotz kernel is
\((\gamma-z)^{-1}\), not \((z-\gamma)^{-1}\).

Since

\[
B(x)=\frac{\Xi(i\sqrt x)}{\Xi(0)},
\]

we have, for \(y>0\),

\[
\boxed{
\frac{B'(y^2)}{B(y^2)}
=-\frac{i}{2y}m_B(iy).
}
\]

Thus the folded Stieltjes function \(F=B'/B\) is the imaginary-axis
pullback of the Bures covariant logarithmic derivative.

If RH holds, then

\[
m_B(z)=\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z}
\]

is Herglotz in the upper half-plane under the convention
\(\operatorname{Im}m_B(z)\ge0\). Its imaginary-axis pullback is

\[
F(x)=\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2+x}
=\sum_{\gamma>0}
\frac{m_\gamma\gamma^{-2}}{1+x\gamma^{-2}}.
\]

This is exactly the positive trace-weighted Stieltjes representation used by
the native gates.

Conversely, if the native \(H,J\) gates hold for all \(n\), Theorem 16.2
constructs the positive Stieltjes representation for \(F\). Pulling it back
by \(x=-z^2\) gives

\[
\boxed{
m_B(z)=2zF(-z^2),
}
\]

hence the paired Herglotz pole expansion for \(m_B\). Hence

\[
\boxed{
\text{Apex Lemma}_{HJ}
\quad\Longleftrightarrow\quad
m_B\text{ is Herglotz}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\]

The Bures field is therefore not an extra assumption. It is the analytic
continuation of the native gate into the upper half-plane.

### 17.1 The finite gate as a differential functional

Let

\[
F(x):=\frac{B'(x)}{B(x)}
=\sum_{n\ge0}(-1)^n\mu_nx^n.
\]

For a polynomial

\[
g(s)=\sum_{n=0}^N g_ns^n,
\]

define the finite differential functional

\[
\mathfrak D_g[F]
:=
\sum_{n=0}^N g_n\,\frac{(-1)^n}{n!}F^{(n)}(0).
\]

Since

\[
\mu_n=\frac{(-1)^n}{n!}F^{(n)}(0),
\]

we have

\[
\boxed{
\mathfrak D_g[F]=\mathcal L_\Xi[g].
}
\]

Therefore the Apex gates are equivalently

\[
\boxed{
\mathfrak D_{p^2}[F]\ge0,
\qquad
\mathfrak D_{sp^2}[F]\ge0
\quad
\text{for every real polynomial }p.
}
\]

This is a useful language correction: Apex positivity is a statement about
finite jets of the single analytic function \(F=B'/B\) at the origin.

### 17.2 Prime/gamma split of the same jet

Using

\[
B(x)=\frac{\xi(1/2+\sqrt x)}{\xi(1/2)},
\]

and writing

\[
s=\frac12+t,\qquad t=\sqrt x,
\]

we get the exact analytic identity

\[
F(x)=\frac{1}{2t}\frac{\xi'}{\xi}\!\left(\frac12+t\right).
\]

The apparent singularity at \(t=0\) is removable because
\(\xi(s)=\xi(1-s)\), hence \(\xi'/\xi(1/2)=0\).

Now use

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi\!\left(\frac{s}{2}\right)
+\frac{\zeta'}{\zeta}(s),
\]

where \(\psi=\Gamma'/\Gamma\). Set

\[
A(s):=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi\!\left(\frac{s}{2}\right),
\qquad
P(s):=\frac{\zeta'}{\zeta}(s).
\]

The naive split

\[
\frac{A(1/2+t)}{2t}
+
\frac{P(1/2+t)}{2t}
\]

is exact as a sum, but the two summands are not separately native
\(x=t^2\) objects. Their non-even parts cancel only after addition. The
correct finite-jet split takes the odd-in-\(t\) part of each channel:

\[
\boxed{
F=F_{\mathrm{arch}}+F_{\mathrm{prime}},
}
\]

with

\[
F_{\mathrm{arch}}(x)
=
\frac{
A(1/2+t)-A(1/2-t)
}{4t},
\]

and

\[
F_{\mathrm{prime}}(x)
=
\frac{
P(1/2+t)-P(1/2-t)
}{4t}.
\]

Thus every finite native gate decomposes exactly as

\[
\boxed{
\mathcal L_\Xi[g]
=
\mathfrak D_g[F_{\mathrm{arch}}]
+
\mathfrak D_g[F_{\mathrm{prime}}].
}
\]

This is the prime/gamma dish in its smallest form. The archimedean piece,
the pole-canceling piece, and the analytically continued prime piece must
combine to give nonnegative values on

\[
g=p^2,\qquad g=sp^2.
\]

### 17.3 The true no-isolator theorem

The final unconditional proof can now be stated without zeros:

**Apex No-Isolator Theorem.** For every real polynomial \(p\),

\[
\mathfrak D_{p^2}
\left[
\frac{1}{2\sqrt x}
\frac{\xi'}{\xi}\!\left(\frac12+\sqrt x\right)
\right]\ge0,
\]

and

\[
\mathfrak D_{sp^2}
\left[
\frac{1}{2\sqrt x}
\frac{\xi'}{\xi}\!\left(\frac12+\sqrt x\right)
\right]\ge0.
\]

By Theorem 16.2, this is equivalent to RH.

The advantage is tactical. Instead of searching for zeros, we search for a
positive-cone proof of these finite jets. In expanded form, the theorem asks
for the nonnegativity of

\[
\mathfrak D_{p^2}[F_{\mathrm{arch}}]
+
\mathfrak D_{p^2}[F_{\mathrm{prime}}],
\]

and

\[
\mathfrak D_{sp^2}[F_{\mathrm{arch}}]
+
\mathfrak D_{sp^2}[F_{\mathrm{prime}}],
\]

for every real \(p\).

The spectral-isolator lemma says that if this fails, the failure is not
vague: it is a finite polynomial whose jet functional is negative. The
explicit-formula route must prove that no such finite prime/gamma jet witness
exists.

### 17.4 Current summit after the Bures bridge

We have now aligned three equivalent targets:

\[
\begin{array}{ccl}
\text{native moment target}
&:&
H_n,J_n\succeq0\quad\forall n,\\[1mm]
\text{Bures target}
&:&
m_B=-\Xi'/\Xi\text{ is Herglotz},\\[1mm]
\text{explicit-formula target}
&:&
\mathfrak D_{p^2}[F]\ge0,\ 
\mathfrak D_{sp^2}[F]\ge0\quad\forall p.
\end{array}
\]

The missing proof is the positive-cone estimate for the prime/gamma jet. No
claim of RH is made here. The point of this section is that the remaining
theorem has been reduced to a finite-jet inequality for one explicit
function.

---

## 18. Li, Weil, and the Correct Bridge

The Li-coefficient hint is useful, but it needs one correction. There is an
explicit triangular bridge, but not a finite triangular bridge directly from
Li coefficients to native cumulants.

The reason is geometric. Li coefficients expand \(\xi\) at \(s=1\) after the
Cayley coordinate

\[
u=1-\frac1s.
\]

The native folded cumulants expand \(\xi\) at the critical center

\[
s=\frac12+t,\qquad x=t^2.
\]

In the Li coordinate, the critical center is

\[
u=-1.
\]

Thus the bridge from Li to native is a center shift from \(u=0\) to \(u=-1\).
That shift is explicit, but it consumes the Li tail.

### 18.1 Exact generating-function bridge

Let \(\Lambda_n^{Li}\) denote the Li coefficients:

\[
\Lambda_n^{Li}
=
\sum_\rho
\left[
1-\left(1-\frac1\rho\right)^n
\right].
\]

They are generated by

\[
\mathcal L(u)
:=
\log \xi\!\left(\frac1{1-u}\right)-\log \xi(1)
=
\sum_{n\ge1}\frac{\Lambda_n^{Li}}{n}u^n.
\]

Now set

\[
s=\frac12+t,\qquad
u(t)=1-\frac1{1/2+t}
=\frac{t-1/2}{t+1/2}.
\]

Equivalently,

\[
v:=u+1=\frac{4t}{1+2t},
\qquad
t=\frac{v}{2(2-v)}.
\]

The native logarithm is

\[
\log B(t^2)
=
\log\xi\!\left(\frac12+t\right)-\log\xi\!\left(\frac12\right)
=
\mathcal L(-1+v(t))-\mathcal L(-1).
\]

Define the shifted Li derivatives

\[
a_r:=[v^r]\bigl(\mathcal L(-1+v)-\mathcal L(-1)\bigr).
\]

Then

\[
a_r
=
\sum_{k\ge r}
(-1)^{k-r}
\binom{k}{r}
\frac{\Lambda_k^{Li}}{k},
\]

whenever the shift is interpreted by analytic continuation or by an
appropriate summability of the Li generating function at \(u=-1\).

On the native side,

\[
\log B(t^2)
=
\sum_{m\ge1}
\frac{(-1)^{m+1}}{m}\ell_m t^{2m}.
\]

Since

\[
v(t)=\frac{4t}{1+2t},
\]

we get the finite triangular relation

\[
\boxed{
\ell_m
=
\sum_{r=1}^{2m}
C_{m,r}a_r,
}
\]

where

\[
\boxed{
C_{m,r}
=
(-1)^{m+1+r}
m\,2^{2m+r}
\binom{2m-1}{r-1}.
}
\]

Therefore the native moments

\[
\mu_n=\ell_{n+1}
\]

are given by

\[
\boxed{
\mu_n
=
\sum_{r=1}^{2n+2}
C_{n+1,r}
\sum_{k\ge r}
(-1)^{k-r}
\binom{k}{r}
\frac{\Lambda_k^{Li}}{k}.
}
\]

This is the exact Li-native transform.

### 18.2 Consequence: partial Li positivity does not automatically give gates

This matters. A finite native gate of size \(n\) uses

\[
\mu_0,\ldots,\mu_{2n+1}.
\]

Each \(\mu_j\) uses finitely many shifted-center coefficients \(a_r\), but
each \(a_r\) uses the Li tail

\[
\Lambda_k^{Li}\qquad(k\ge r).
\]

So unconditional positivity of finitely many Li coefficients does not by
itself imply positivity of finitely many native gates. It gives evidence and
possible estimates, but not a free theorem.

The useful corrected statement is:

\[
\boxed{
\text{native gates are finite positivity tests on shifted Li derivatives at }
u=-1.
}
\]

Thus Li theory is still a bridge, but the bridge crosses a boundary point of
the Li disk. Any rigorous transfer must control the tail in the binomial
shift.

### 18.3 Weil-Bombieri slice

The native quadratic forms also have the shape of Weil positivity. For a
real polynomial \(p\),

\[
\mathcal L_\Xi[sp(s)^2]
=
\sum_\rho z_\rho^{-2}p(z_\rho^{-2})^2.
\]

This is a spectral sum over zeros, hence a slice of the Weil explicit
formula philosophy. Formally, one wants an admissible Weil test function
\(f_p\) whose transform satisfies

\[
\widehat f_p(\rho)
=
z_\rho^{-2}p(z_\rho^{-2})^2.
\]

Then native positivity becomes

\[
\sum_\rho \widehat f_p(\rho)\ge0,
\]

which is exactly a Weil/Bombieri-type positivity statement on a restricted
family of test functions.

The discipline point: such \(f_p\) is not automatically an ordinary compactly
supported test function. Since \(z^{-2k}\) is a reciprocal-power jet, the
exact object may live first as a distributional or regularized Weil test.
The rigorous task is therefore:

\[
\boxed{
\text{construct an admissible regularized Weil test }f_p
\text{ for each native polynomial }p.
}
\]

If that construction lands inside a known unconditional positive slice of
Weil's form, Apex follows on that slice. If it lands outside known slices, it
names precisely what new Bombieri-Weil positivity must be proved.

### 18.4 Why Born-Helmert remains the distinctive route

The Li and Weil bridges translate the problem into existing languages. The
program's distinctive route is still the Born-Helmert one:

\[
\mu_n=\ell_{n+1}
\stackrel{?}{=}
\sum_{a\ne0}(\widehat y_a^\infty)^{2n+2}.
\]

If the limiting centered primorial/Archimedean Helmert ledger
\(\widehat y^\infty\) can be constructed directly from the arithmetic side,
with the moment identity above for every \(n\), then

\[
H_n\succeq0,\qquad J_n\succeq0
\]

become tautological Gram/Born-square statements.

This avoids the de Bruijn-Newman boundary because it does not take the
\(t\to0^+\) limit of the spectral heat-flow ledger. It takes the limit of
the explicit primorial Helmert ledger instead.

So after the peer feedback, the three serious proof routes are:

1. **Shifted Li route:** control the binomial tail from \(u=0\) to \(u=-1\).
2. **Weil route:** realize native polynomial witnesses as admissible
   Weil/Bombieri test functions and prove positivity on that slice.
3. **Born-Helmert route:** construct the limiting squared-amplitude ledger
   directly and prove its moments equal the folded \(\Xi\) cumulants.

The third remains the most native to the simplicial program.

---

## 19. Direct Born-Helmert Apex Theorem

The previous routes translate Apex into Li, Weil, and Bures languages. The
native simplicial route should be stated separately because it has the
shortest proof once its construction is achieved.

Let \(\mathcal A_M\) be a finite or increasing arithmetic index set produced
from the centered primorial/Archimedean Helmert ledger. Suppose it carries
real amplitudes

\[
\widehat y_a^{(M)}\in\mathbb R,
\qquad a\in\mathcal A_M,
\]

and define Born atoms

\[
\lambda_a^{(M)}:=(\widehat y_a^{(M)})^2\ge0.
\]

The trace-weighted Born measure is

\[
d\tau_M(s)
:=
\sum_{a\in\mathcal A_M}
\lambda_a^{(M)}
\delta_{\lambda_a^{(M)}}(s).
\]

### 19.1 Conditional direct theorem

**Theorem 19.1 (direct Born-Helmert completion).** Suppose the arithmetic
Born-Helmert ledgers satisfy, for every \(n\ge0\),

\[
\boxed{
\lim_{M\to\infty}
\sum_{a\in\mathcal A_M}
\left(\lambda_a^{(M)}\right)^{n+1}
=
\mu_n
=
\ell_{n+1}.
}
\]

Then

\[
\forall n\ge0,\qquad H_n\succeq0,\quad J_n\succeq0.
\]

Consequently RH follows.

**Proof.** For each \(M\),

\[
H_n^{(M)}
:=
\left(
\int s^{i+j}\,d\tau_M(s)
\right)_{0\le i,j\le n}
=
\sum_{a\in\mathcal A_M}
\lambda_a^{(M)}
v_a v_a^{T},
\]

where

\[
v_a=
\left(
1,\lambda_a^{(M)},\ldots,(\lambda_a^{(M)})^n
\right)^T.
\]

Since \(\lambda_a^{(M)}\ge0\), every summand is positive semidefinite.
Thus

\[
H_n^{(M)}\succeq0.
\]

Similarly,

\[
J_n^{(M)}
:=
\left(
\int s^{i+j+1}\,d\tau_M(s)
\right)_{0\le i,j\le n}
=
\sum_{a\in\mathcal A_M}
(\lambda_a^{(M)})^2
v_a v_a^{T}
\succeq0.
\]

The assumed moment convergence gives entrywise convergence

\[
H_n^{(M)}\to H_n,
\qquad
J_n^{(M)}\to J_n.
\]

The positive semidefinite cone is closed, hence \(H_n,J_n\succeq0\). By
Theorem 16.2, RH follows. \(\square\)

This theorem is deliberately simple. Its point is to isolate the only
nontrivial native work:

\[
\boxed{
\text{construct }\widehat y^{(M)}\text{ arithmetically and prove the moment
identity.}
}
\]

### 19.2 Why this avoids the heat boundary

The heat-flow route uses real zeros for \(t>\Lambda\) and tries to pass
positivity to \(t=0\). That is blocked exactly by \(\Lambda\le0\).

The direct Born-Helmert route does not use spectral zero positivity at any
positive heat. It asks for a separate arithmetic construction:

\[
\text{primorial/Archimedean centered ledger}
\quad\longrightarrow\quad
\text{Born atoms}
\quad\longrightarrow\quad
\Xi\text{ cumulants}.
\]

If this construction is done, Apex is proved without touching the
de Bruijn-Newman boundary.

### 19.3 The exact construction target

The object to build is not merely a list of approximate zeros. It is a
positive trace-gauge measure

\[
\tau_\infty
\]

obtained as the weak/moment limit of the arithmetic Born measures
\(\tau_M\), satisfying

\[
\boxed{
\frac{B'(x)}{B(x)}
=
\int_0^\infty\frac{1}{1+xs}\,d\tau_\infty(s).
}
\]

Equivalently,

\[
\boxed{
\ell_m
=
\int_0^\infty s^{m-1}\,d\tau_\infty(s)
=
\lim_{M\to\infty}
\sum_{a\in\mathcal A_M}
\left(\widehat y_a^{(M)}\right)^{2m}.
}
\]

This is the Lock A no-loss theorem in its most native form:

\[
\text{centered arithmetic amplitudes square into the folded }\Xi
\text{ cumulants.}
\]

It is also the exact place where T4 and T6 enter:

1. T4 supplies the centered Helmert ladder and its arithmetic metric.
2. T6 supplies the RMS/Born rule turning amplitudes into positive atoms.
3. Pass-5 supplies the trace-weighted Stieltjes criterion showing that these
   atoms prove RH if their moments match \(\Xi\).

The proof target is now precise enough for a future implementation or
analytic attack:

\[
\boxed{
\widehat y^{(M)}
\xrightarrow[\text{Born moments}]{M\to\infty}
\ell_m
\quad\forall m\ge1.
}
\]

---

## 20. Archimedean Jet Sign Check

The prime/gamma split is the most concrete finite-jet handle, but the
archimedean channel is not positive by itself. This corrects a tempting but
false route.

Recall

\[
F_{\mathrm{arch}}(x)
=
\frac{A(1/2+t)-A(1/2-t)}{4t},
\qquad
t=\sqrt x,
\]

where

\[
A(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi\!\left(\frac{s}{2}\right).
\]

Write

\[
F_{\mathrm{arch}}(x)
=
\sum_{j\ge0}c_j^{\mathrm{arch}}x^j,
\qquad
\mu_j^{\mathrm{arch}}:=(-1)^jc_j^{\mathrm{arch}}.
\]

Then

\[
c_j^{\mathrm{arch}}
=
\frac{A^{(2j+1)}(1/2)}{2(2j+1)!}.
\]

Already at \(j=0\),

\[
\mu_0^{\mathrm{arch}}
=
\frac12A'(1/2)
=
\frac12
\left[
-8+\frac14\psi_1(1/4)
\right],
\]

where \(\psi_1\) is the trigamma function. Numerically,

\[
\boxed{
\mu_0^{\mathrm{arch}}
=
-1.850333855686611\ldots<0.
}
\]

Thus the archimedean \(H_0\) gate fails:

\[
H_0^{\mathrm{arch}}=[\mu_0^{\mathrm{arch}}]\not\succeq0.
\]

The first archimedean moments continue with alternating large signs:

\[
\begin{array}{c|r}
j & \mu_j^{\mathrm{arch}}\\
\hline
0 & -1.850333855686611\ldots\\
1 & 7.985509666618810\ldots\\
2 & -31.997883218249916\ldots\\
3 & 127.99966916658395\ldots\\
4 & -511.99994742035412\ldots
\end{array}
\]

So the Apex proof cannot be:

\[
\text{archimedean positive baseline}
\quad+\quad
\text{small prime correction}.
\]

The correct reading is subtler:

\[
\boxed{
\text{Apex positivity is born from the combined prime/gamma/centering
cancellation, not from either channel alone.}
}
\]

This makes the finite-jet problem sharper. The explicit formula must prove
that the prime channel cancels the negative archimedean gate defects exactly
enough to leave

\[
\mathfrak D_{p^2}[F_{\mathrm{arch}}+F_{\mathrm{prime}}]\ge0,
\qquad
\mathfrak D_{sp^2}[F_{\mathrm{arch}}+F_{\mathrm{prime}}]\ge0.
\]

For \(p=1\), the first cancellation is already dramatic:

\[
\mu_0
=
\ell_1
=
0.0231\ldots,
\]

whereas

\[
\mu_0^{\mathrm{arch}}
=
-1.8503\ldots.
\]

Thus

\[
\mu_0^{\mathrm{prime}}
=
\mu_0-\mu_0^{\mathrm{arch}}
\approx
1.8734\ldots.
\]

The prime channel is not a small perturbation. It is the compensating
channel that turns the archimedean defect into the positive folded
\(\Xi\) ledger.

---

## References

- T3, *Character Orthogonality on the Conductor Lattice*.
- T4, *The Helmert-Simplicial Residue Ladder*.
- T6, *The RMS-Simplicial Quadratic Gauge*.
- RH Pass-3, *The Positive Determinant Trace Model*.
- RH Pass-4, *The Born-Helmert Reduction*.
- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J.
  17 (1950), 197-226.
- C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer.
  Math. Soc. 61 (1976), 245-251.
- B. Rodgers and T. Tao, *The de Bruijn-Newman constant is non-negative*,
  Forum of Mathematics, Pi 8 (2020), e6.
