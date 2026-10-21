# Two-clock extension: the exact compatibility inequality

11 October 2026. Continuation directed at the two-clock / Castelnuovo–Severi proposal. Paper 53 on disk still ended its mathematical development at §4.8 when read; the peer's proposed §4.9 and finite-field claims were supplied in the user message. The dyadic ladder script and its current log were read without modifying or restarting that run.

**Result of this pass:** a direct prime-side computation of overlapping-packet correlations, a nine-point mixed-clock section, and the precise finite extension inequality. The all-section inequality is not established. No RH closure is claimed.

## 1. Fix the kernel, including its nonvanishing filter

Use f(x)=e^x 1_[0,a](x), a=log 2, and its autocorrelation

\[
g(v)=2e^{-|v|}-\tfrac12e^{|v|}\quad(|v|\le a),
\qquad G(z)=\frac{5-4\cosh(az)}{1-z^2}.
\]

Outside its stated support g is zero. The singularities of G at ±1 are removable. Set K=W*g and q=K(0)=0.29984744568842157736... . The preceding N7 notes established

\[
K(t)=\sum_\rho G(\rho-1/2)e^{(\rho-1/2)t}.
\tag{1}
\]

This is a real, even, continuous function; its zero sum converges locally uniformly and absolutely. G has no zero in |Re z|<1 and decays quadratically in height on the critical strip. Those properties are crucial: boundedness of this specific observable excludes displaced zeros through its Laplace poles.

## 2. The two-clock equivalence, with the needed quantifiers

Let H={m log2+n log3 : m,n in Z}. It is dense in R, since log2/log3 is irrational. Define the Hermitian kernel on Z² by

\[
M_{u,v}=K((u_1-v_1)\log2+(u_2-v_2)\log3).
\tag{2}
\]

For this K, the following are equivalent:

1. RH.
2. Every finite matrix from (2) is positive semidefinite.
3. Every two-point matrix with differences in H is positive semidefinite.
4. |K(t)|≤q for every real t.

**Proof.** Under RH, (1) becomes a positive Fourier series: G(i gamma)=(5−4cos(a gamma))/(1+gamma²)>0. Thus each matrix is a sum of positive rank-one matrices, proving 1⇒2. The implication 2⇒3 is immediate. The eigenvalues of a two-point matrix are q±K(h), so 3 gives |K(h)|≤q on H. Density and continuity prove 4. Finally, the Laplace transform sum_rho G(rho−1/2)/(s−(rho−1/2)) has a nonzero residue at every displaced zero. Boundedness of K makes its Laplace transform holomorphic for Re s>0, excluding those zeros. Functional-equation symmetry completes 4⇒1.

Strict positive definiteness is not needed anywhere in this proof. In the standard terminology, a positive-definite function often means precisely the semidefinite matrix condition above.

This validates the two-clock reduction; it does not prove its premise. The group law itself is unconditional, while positivity of its arithmetic kernel is the RH-content.

## 3. The exact extension rule

Suppose a finite section M on existing zooms is positive definite. For a new zoom, let b contain its correlations with those zooms. The enlarged matrix is

\[
\begin{pmatrix}M&b\\b^*&q\end{pmatrix}.
\]

Completing the square proves

\[
\boxed{\text{enlarged section}\succeq0
\iff q-b^*M^{-1}b\ge0.}
\tag{3}
\]

The residual on the right is the squared norm that an actual Hilbert-space realization would assign to the component of the new vector orthogonal to the old span. Calling it a squared norm before proving (3) would assume the sought realization.

If M is merely semidefinite, the correct rule is b in range(M) and q−b*M^+b≥0, where M^+ is its Moore–Penrose inverse. This explicitly permits a zero margin.

Two-point bounds on finitely many differences do not by themselves imply a mixed section is positive. For instance,

\[
\begin{pmatrix}1&0.9&0.9\\0.9&1&-0.9\\0.9&-0.9&1\end{pmatrix}
\]

has positive two-point principal minors but determinant −2.888. The equivalence in §2 works because it requires *all* differences in a dense group and uses the special explicit-formula kernel, not because arbitrary pairwise correlations automatically assemble.

## 4. A single realization follows once compatibility is proved

If every finite section is semidefinite, take formal vectors e_h, h in H, with inner product <e_h,e_k>=K(h−k), quotient the null space, and complete. Translation e_h↦e_(h+r) gives commuting unitaries U_r. With v=e_0,

\[
K(r)=\langle U_rv,v\rangle,\qquad
\|U_rv-v\|^2=2(q-\Re K(r)).
\]

Continuity of K at zero and density of the span of translates extend this to a strongly continuous unitary representation of R. Thus all zooms are carried by one positive realization once the finite compatibility inequalities hold. The completion is standard; its missing input is arithmetic positivity, not a further convergence margin.

The analogy with Hodge index suggests seeking a geometric proof of that input. It does not make a Q-analogue of Riemann–Roch logically necessary: a direct arithmetic proof of (3), or the global pairwise barrier in §2, would also suffice.

## 5. What a local certificate covers

A finite combination of translates of f has support contained in an interval of length

\[
a+\max_j t_j-\min_j t_j.
\]

Translation invariance lets us center that interval. Therefore a Weil-positivity theorem for support [-L,L] proves positivity of every such section with span at most 2L−a, regardless of its cardinality.

For L=0.8 this span is 1.6−log2≈0.90685. The pair {0,log2} fits. The pair {0,log3} for this particular packet does not: its combined support has length log6≈1.79176>1.6. The fact that the prime comb contains both primes 2 and 3 inside a certified autocorrelation window is different from certifying all translates of this packet by those zooms.

[Zhu's abstract](https://arxiv.org/abs/2608.24827) reports an unconditional lower certificate on [-0.8,0.8], unconditional numerical upper bounds at selected larger windows, an empirical decay law, and an asymptotic upper bound exp(−L e^L) conditional on RH. These statuses should remain distinct. I inspected the abstract, not the complete interval-arithmetic proof.

Shrinking positive margins do not logically prevent a limit proof: positivity for *every* finite support already implies Weil positivity. The difficulty is proving infinitely many required inequalities, rather than maintaining a margin bounded away from zero. Finite numerical checks, however many, do not supply that quantifier.

## 6. Prime-side formula including overlapping packets

To test mixed clocks we need t<log2 as well as disjoint translates. For t≥0 define

\[
h_t(v)=\frac{g(v-t)+g(v+t)}2,\quad R=t+a,\quad A=G(1/2),\quad h_t(0)=g(t).
\]

The regularized explicit formula gives

\[
\begin{aligned}
K(t)={}&2A\cosh(t/2)
-g(t)\big(\gamma_E+\log(4\pi)+\log\tanh(R/2)\big)\\
&-\int_0^R\frac{e^{v/2}h_t(v)-g(t)}{\sinh v}\,dv\\
&-\sum_{n\le e^R}\frac{\Lambda(n)}{\sqrt n}
\big(g(\log n-t)+g(\log n+t)\big).
\end{aligned}
\tag{4}
\]

The integral is finite at zero by the subtraction. It is evaluated piecewise at the kinks of g. At t=0 it returns the earlier q; at t>a it reduces to the prime-discrepancy formula from the earlier notes. It uses no spectral zero data.

For the ordered zooms 1,2,3,6,4,9,12,18,36, all nine Schur pivots divided by q were numerically positive:

\[
1,\ .66142245,\ .77384653,\ .53621555,\ .55791010,
\ .72944557,\ .44314154,\ .47981580,\ .40801623.
\]

The smallest eigenvalue of this nine-by-nine matrix divided by q was approximately 0.08845112. Evaluations at 40 and 70 digits differed in matrix entries by less than 9.5e−40. This is a precision cross-check, not a rigorous interval enclosure.

The overlapping entries, which do not occur in the one-clock ladder, include

\[
K(\log(3/2))=0.07270259683411477498\ldots,
\qquad
K(\log(4/3))=-0.03094297665374064289\ldots.
\]

Files: `empirical/connes_route/probe_two_clock_schur.py` and its JSON output. The peer's ongoing DH computation was not changed or used as a completed certificate. Its script uses a truncated zero set, so a reported negative eigenvalue would need a tail estimate before being a rigorous statement about the full DH form.

## 7. The remaining arithmetic theorem

An all-clock extension theorem must control b*M^+b and the null-space compatibility directly from the explicit prime formula for every finite section, or prove the global pairwise barrier. Positivity on a bounded window supplies starting sections but not their correlations with arbitrarily distant new zooms. Commutativity of the 2 and 3 translations specifies their algebra, not positivity of the prescribed state on that algebra.

This pass establishes the exact extension problem and a reproducible mixed-clock witness. It does not establish the uniform extension inequality. That is the remaining RH-level step in this frame.

The other cited sources were checked at abstract level: [Suzuki](https://arxiv.org/abs/2606.09096) offers an unconditional finite-interval framework and a conjectural limiting spectral realization; [CCM](https://arxiv.org/abs/2511.22755) supplies the spectral-triple setting; [Connes–Consani](https://arxiv.org/abs/2006.13771) treats the archimedean positivity mechanism and its semi-local direction. None is used here as an established all-clock positivity theorem.
