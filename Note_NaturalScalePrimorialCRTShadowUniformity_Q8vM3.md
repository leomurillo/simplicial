# Note: Natural-Scale Primorial CRT Shadow Uniformity

Random suffix: `Q8vM3`

Mission: solve the natural-scale primorial character-uniformity gap for the
**compressed CRT shadow** of the occupation-decorated observable.

Verdict:

\[
\boxed{
\text{The compressed CRT shadow has natural-scale uniformity by BDH/large
sieve mean-square control.}
}
\]

The overstrong pointwise demand
\[
\max_{\chi\bmod q}|\psi(X,\chi)|
=o(X)
\qquad(q\mid P_n,\ X\asymp P_n^A)
\]
is not the right target and cannot be proved unconditionally in this range
without excluding exceptional real characters.  The compressed shadow is an
averaged residue/character observable.  Its natural norm is \(L^2\), and the
Barban-Davenport-Halberstam theorem gives exactly the required mean-square
control at polynomial scale.

## 1. The Target Must Be the Shadow, Not the Worst Character

Let
\[
P=P_n=p_n\#.
\]
For a modulus \(q\mid P\), define
\[
\Delta(X;q,a)
=
\psi(X;q,a)-{X\over\varphi(q)}
\qquad ((a,q)=1),
\]
with the standard harmless convention that the principal/local Euler factors
are separated before the coprime residue-class analysis.

The compressed CRT shadow is not a request to control every character
separately.  It is a weighted residue observable
\[
\mathcal E_P(W;X)
=
\sum_{q\mid P} c_q
{1\over\varphi(q)}
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
W_q(a)\Delta(X;q,a),
\]
where \(W_q\) is the finite CRT/Fejer detector shadow and \(c_q\) are the
Mobius/Ramanujan conductor coefficients from the compressed observable.

The right shadow norm is
\[
\|W\|_{\mathrm{sh}}^2
:=
\sum_{q\mid P}
{|c_q|^2\over \varphi(q)^2}
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|W_q(a)|^2.
\]

For bounded Fejer/CRT detector shadows and the usual Mobius/Ramanujan
coefficients \(|c_q|\le1\), this norm satisfies
\[
\|W\|_{\mathrm{sh}}^2
\ll
\sum_{q\mid P}{1\over\varphi(q)}
=
\prod_{p\le p_n}\left(1+{1\over p-1}\right)
\ll \log p_n.
\]

Thus \(\|W\|_{\mathrm{sh}}\ll(\log p_n)^{1/2}\), not exponentially large in
the number of CRT characters.  This is the compression advantage.

## 2. BDH Input

Use the standard Barban-Davenport-Halberstam mean-square estimate: for
\(1\le Q\le X\),
\[
\sum_{q\le Q}
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
|\Delta(X;q,a)|^2
\ll
XQ(\log X)^C
\]
for an absolute constant \(C\) in the form needed here.  Smooth weights
\(G(\log m)\) are handled by dyadic partition and partial summation, changing
only the power of \(\log X\) and replacing \(X\) by the largest dyadic block.

This is classical averaged distribution of primes in arithmetic progressions.
No Elliott-Halberstam input and no Paper 43 \(r_0=5\) improvement is needed.

## 3. Natural-Scale Theorem

**Theorem 3.1 (natural-scale compressed CRT shadow uniformity).**  
Let \(P=P_n\).  Let \(X_n\) satisfy
\[
X_n\ge P_n^{1+\varepsilon}
\]
for some fixed \(\varepsilon>0\).  For every \(K\)-even CRT/Fejer detector
shadow \(W=\{W_q\}_{q\mid P_n}\) satisfying
\[
\|W\|_{\rm sh}=P_n^{o(1)},
\]
\[
\frac{\mathcal E_{P_n}(W;X_n)}{X_n}
\longrightarrow0.
\]
More quantitatively,
\[
|\mathcal E_{P_n}(W;X_n)|
\ll
X_n^{1/2}P_n^{1/2}(\log X_n)^{C/2}\|W\|_{\mathrm{sh}},
\]
and therefore
\[
{|\mathcal E_{P_n}(W;X_n)|\over X_n}
\ll
P_n^{-\varepsilon/2+o(1)}
\]
for primorial detector shadows.

In particular this applies to bounded Fejer/CRT detector shadows with the
standard Mobius/Ramanujan normalization \(|c_q|\le1\).

*Proof.*  By Cauchy-Schwarz,
\[
|\mathcal E_P(W;X)|
\le
\left(
\sum_{q\mid P}
{|c_q|^2\over\varphi(q)^2}
\sum_{a}|W_q(a)|^2
\right)^{1/2}
\left(
\sum_{q\mid P}\sum_a|\Delta(X;q,a)|^2
\right)^{1/2}.
\]
The first factor is \(\|W\|_{\rm sh}\).  Since \(q\mid P\) implies
\(q\le P\), the second factor is bounded by the BDH sum with \(Q=P\):
\[
\left(
\sum_{q\le P}\sum_a|\Delta(X;q,a)|^2
\right)^{1/2}
\ll
(XP)^{1/2}(\log X)^{C/2}.
\]
For bounded detector shadows,
\[
\|W\|_{\rm sh}^2\ll\sum_{q\mid P}{1\over\varphi(q)}
\ll\log p_n=P_n^{o(1)}.
\]
Thus
\[
{|\mathcal E_P(W;X)|\over X}
\ll
\left({P\over X}\right)^{1/2}P^{o(1)}.
\]
With \(X=P^{1+\varepsilon}\), this is
\[
P^{-\varepsilon/2+o(1)}\to0.
\]
\(\square\)

## 4. Full-Modulus Shadow Is Even Easier

If the compressed observable is supported only at the full row \(q=P_n\),
then
\[
\mathcal E_P(W;X)
=
{1\over\varphi(P)}
\sum_{a\bmod P}^{*}W(a)\Delta(X;P,a),
\]
and the same argument gives
\[
|\mathcal E_P(W;X)|
\ll
X^{1/2}(\log X)^{C/2}
\left({P\over\varphi(P)}\right)^{1/2}
\|W\|_{2,\mathrm{avg}}.
\]
Hence the full-modulus compressed shadow is \(o(X)\) already for
\[
X\to\infty
\]
with \(P\le X\).  The \(P^{1+\varepsilon}\) condition in Theorem 3.1 is only
needed to control the whole divisor-lattice shadow uniformly.

## 5. Character-Side Translation

By finite multiplicative character orthogonality,
\[
{1\over\varphi(q)}\sum_{a}^{*}W_q(a)\Delta(X;q,a)
\]
is the same object as an \(L^2\)-weighted character average
\[
\sum_{\chi\bmod q}\widehat W_q(\chi)\psi(X,\chi)
\]
with Parseval control
\[
\sum_{\chi\bmod q}|\widehat W_q(\chi)|^2
=
{1\over\varphi(q)}\sum_a^{*}|W_q(a)|^2.
\]

Thus Theorem 3.1 is exactly natural-scale primorial **character** uniformity
for the compressed shadow, but in the correct averaged norm.  It is not
pointwise character uniformity.

## 6. Why the Pointwise Version Is Not Solved

Suppose a real primitive character \(\chi_D\) has a Landau-Siegel zero
\[
\beta_D=1-{\lambda\over\log D}.
\]
Once \(P_n\) contains the squarefree conductor \(D\), the character appears in
the primorial divisor family.  At natural scale \(X=D^A\), the explicit
formula gives a contribution of size
\[
{X^{\beta_D}\over \beta_D}
=
X\exp(-A\lambda+o(1)).
\]
For fixed \(A\), this is a fixed positive fraction of \(X\), not \(o(X)\).
Therefore a theorem of the form
\[
\max_{\chi\bmod q,\ q\mid P_n}|\psi(X,\chi)|=o(X)
\qquad (X=P_n^A)
\]
would exclude exceptional characters in a range where classical
Siegel-Walfisz deliberately does not.  That is a different and much harder
problem.

The compressed shadow avoids this obstruction because an individual
exceptional character has negligible mass in the \(L^2\)-averaged CRT shadow
unless the detector is adversarially chosen to isolate it.  Poisson-Gaussian
CRT/Fejer detectors are bounded smooth windows, not exceptional-character
spikes.

## 7. Relation to Lock A

The finite-place analytic bridge now splits cleanly:

1. **Occupation lift:** exact upstairs prime-power coefficients before CRT
   compression.
2. **Double cutoff:** closed on \(\mathcal D_{\delta,0}\) by dominated
   convergence.
3. **Compressed CRT shadow uniformity:** closed at natural polynomial scale
   \(X=P_n^{1+\varepsilon}\) by BDH/large-sieve mean-square control.
4. **Natural-scale pointwise max over characters:** not needed for the
   compressed shadow and not available unconditionally.

This solves the natural-scale primorial character-uniformity problem in the
form required by the compressed CRT observable.

## 8. Remaining Boundary

This note does not prove the independent Archimedean metaplectic
positive-energy selection.  It also does not validate Paper 43's claimed
Elliott-Halberstam-direction pointwise exponent.  It bypasses that route for
Lock A by using the correct averaged compressed-shadow norm.
