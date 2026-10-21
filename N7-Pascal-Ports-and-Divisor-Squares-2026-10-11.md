# Pascal coefficients, the updated port construction, and divisor squares

11 October 2026. Read alongside Paper 53, especially its updated §§4.6–4.8, and the preceding N7 arithmetic notes.

**Outcome.** The proposed combinatorial mechanism has been tested in three concrete forms. Pascal basis changes preserve the positivity obstruction; fixed binomial scale filters retain every off-line mode in the pole-canceling construction below; divisor squares supply a genuine positive arithmetic expression whose coefficients can be optimized. No identity with a sufficiently small remainder connects that expression to the required one-sided discrepancy yet. RH is not proved.

## 1. What changed in the latest manuscript

The newest substantive mathematical Markdown found in the workspace was `53_passive_ports_and_the_explicit_formula.md`. Later Markdown timestamps were publication metrics. I read the finite-port definition, Propositions 4.6–4.9, and the phase-counting identity and readout in §4.8. I did not independently certify its complete numerical zero counts or audit every claim in Paper 53.

Two parts directly matter here:

- The finite amplitude exp(L_X) is zero-free by construction, but Proposition 4.9 identifies convergence after pole compensation as the remaining RH-equivalent limit. Finite zero-freeness alone does not justify that convergence.
- The phase instrument retains the error Δ(S_X−S). Its numerical success on sampled windows does not supply a uniform bound on that error. It therefore cannot be used here as an already established global positivity theorem.

These distinguish the finite positive or balanced object from the uniform passage to the arithmetic target. The Pascal test must preserve that distinction.

## 2. Pascal change of basis: an exact obstruction

For indices 0≤j≤i≤m define the lower-triangular matrix

\[
B_m(t)_{ij}=\binom ij t^{i-j},
\]

with zero entries above the diagonal. The binomial theorem gives

\[
B_m(t)B_m(u)=B_m(t+u),\qquad B_m(t)^{-1}=B_m(-t),\qquad\det B_m(t)=1.
\tag{1}
\]

If P is any Hermitian Pick matrix, its expression in the new basis is

\[
P_t=B_m(t)P B_m(t)^*.
\]

For real t (and with the conjugate transpose as written for complex t), invertibility implies

\[
P_t\succeq0\iff P\succeq0.
\tag{2}
\]

More precisely, the numbers of positive, negative, and zero eigenvalues are preserved by congruence. If v*Pv<0, take v_t=B_m(t)^{-*}v. Then v_t*P_t v_t=v*Pv<0. This proves preservation without a numerical eigenvalue calculation.

For example,

\[
\begin{pmatrix}1&0\\t&1\end{pmatrix}
\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\begin{pmatrix}1&t\\0&1\end{pmatrix}
=\begin{pmatrix}1&t\\t&t^2-1\end{pmatrix},
\]

whose determinant remains −1 for every real t. Positive binomial coefficients in a basis matrix do not make an indefinite form positive.

The exact probe also uses Paper 53's type of planted quartet: Q(s)=(s²+1)(s²+z0²)(s²+conj(z0)²), z0=2+i/2, and Z=Q'/Q. At the sample s=3/8+2i, its positive-real Pick diagonal is

\[
-1129756486528/65755237275<0.
\]

The transported negative vector retains exactly that value under every real Pascal parameter. This is an algebraic control, not a statement that zeta has an off-line zero.

A rectangular projection can remove a negative direction from a sampled matrix. That is loss of information, not proof of positivity of the full form. Likewise, forming PP* is positive for every P, so it cannot discriminate the good and bad cases by itself.

## 3. Pascal coefficients across scales

Write t=log X and let T_h f(t)=f(t+h), h>0. The binomial filter is

\[
\mathcal D_{m,h,c}=(T_h-cI)^m
=\sum_{j=0}^m\binom mj(-c)^{m-j}T_h^j.
\tag{3}
\]

On a single mode e^{zt},

\[
\mathcal D_{m,h,c}e^{zt}=(e^{hz}-c)^m e^{zt}.
\tag{4}
\]

Choosing c=e^{h/2} exactly annihilates the smooth main term A e^{t/2} of P(e^t). However, every nontrivial zero mode has z=rho−1/2 with −1/2<Re z<1/2. Thus

\[
|e^{hz}|<e^{h/2},\qquad e^{hz}-e^{h/2}\ne0.
\]

So this filter removes the pole main term and retains every zero mode, with its original growth exponent. For any fixed m and h it does not turn e^{delta t} into polynomial growth. On the absolutely convergent expansion for K from the earlier N7 notes, applying the finite filter termwise is justified on compact t intervals.

Changing c can cancel selected modes: e^{hz}=c puts them on one vertical arithmetic progression. It cannot cancel an open set of possible displaced modes. More generally a nonzero finite shift filter has analytic multiplier H(z)=sum_j a_j e^{h_j z}; if it vanished throughout an open region, the identity theorem would make it identically zero.

These statements concern fixed filters and exact elimination, not every adaptive construction. Letting m,h,c depend on X requires a fresh uniform estimate, including recovery of the unfiltered discrepancy. The sum of the absolute binomial coefficients is (1+|c|)^m, so high order can amplify an uncontrolled remainder exponentially. No such adaptive estimate has been established here.

## 4. A genuinely positive use of distributivity

Choose real coefficients lambda_d, supported on 1≤d≤D, and define

\[
Q_D(n)=\left(\sum_{d\mid n}\lambda_d\right)^2\ge0.
\]

Distributivity and counting multiples give an exact identity:

\[
\begin{aligned}
\sum_{n\le Y}Q_D(n)
&=\sum_{d,e\le D}\lambda_d\lambda_e
\left\lfloor\frac{Y}{[d,e]}\right\rfloor\\
&=Y\,\mathcal Q_D(\lambda)+\mathcal R_D(Y),\\
\mathcal Q_D(\lambda)&=\sum_{d,e\le D}\frac{\lambda_d\lambda_e}{[d,e]},
\qquad |\mathcal R_D(Y)|\le\left(\sum_{d\le D}|\lambda_d|\right)^2.
\end{aligned}
\tag{5}
\]

The main form is manifestly positive because gcd(d,e)=sum_{r|d,r|e}phi(r):

\[
\mathcal Q_D(\lambda)=\sum_{r\le D}\varphi(r)
\left(\sum_{\substack{d\le D\\r\mid d}}\frac{\lambda_d}{d}\right)^2.
\tag{6}
\]

This is a concrete way to turn a multiplicative identity into a positive quadratic expression. It is the mechanism of the classical Selberg sieve, rather than a new positivity theorem. See [Tao's sieve notes, the Selberg upper-bound construction](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/).

The parameters really can be optimized. Let H_de=1/[d,e]. Equation (6) shows H is positive definite: the triangular map lambda↦(sum_{r|d}lambda_d/d)_r is invertible. Under lambda_1=1, the exact minimum and minimizer are

\[
\min\mathcal Q_D=\frac1{e_1^T H^{-1}e_1},\qquad
\lambda_{\rm opt}=\frac{H^{-1}e_1}{e_1^TH^{-1}e_1}.
\tag{7}
\]

The probe compares this optimizer with raw alternating Pascal weights lambda_d=(−1)^{d−1} binom(D−1,d−1). Both have lambda_1=1. This is one specified embedding of Pascal coefficients into divisor weights, not a test of every combinatorial choice.

| D | optimized main form | Pascal main form | optimized floor-error bound | Pascal floor-error bound |
|---|---:|---:|---:|---:|
| 4 | 2/5 | 21/4 | 144/25 | 64 |
| 8 | 12/41 | 5285/8 | 31684/1681 | 16384 |
| 12 | 30/113 | 322861/3 | 379456/12769 | 4194304 |

All entries are exact rationals. The optimizer minimizes the main form only; it is not asserted to minimize the combined finite-Y expression or its error bound. In these samples the raw Pascal coefficients are poor divisor weights.

## 5. What would make this an RH argument

The nonnegative square in (5) is an auxiliary arithmetic expression. It is not yet the discrepancy E(X) or the completed port's Pick form. A proof would need an independently established identity or comparison such as

\[
E(X)=\mathcal P_X+\mathcal E_X,\qquad
\mathcal P_X\ge0,\qquad
\mathcal E_X\ge-C(1+\log X)^m,
\tag{8}
\]

or the analogous statement for −E. Equation (8) is a specification of what is missing, not a claimed decomposition. The main term must match A sqrt X at the required precision; a fixed excess proportional to sqrt X is too large.

Even for the simple unweighted square in (5), after normalization by sqrt X at Y comparable to X, the elementary floor bound is small enough only if

\[
\|\lambda\|_1^2\ll\sqrt X(1+\log X)^m.
\]

That controls just this auxiliary floor error. It does not establish the missing comparison to primes, nor estimate all errors of a smoothed construction. Those are separate requirements.

This is where the proposal has become testable: coefficient optimization is legitimate, but it must deliver both the arithmetic comparison and a uniform error estimate. Pascal congruence alone cannot do that, and cancellation of the smooth main term alone cannot do it either.

## 6. Reproducibility and scope

`empirical/connes_route/probe_pascal_ports.py` and its JSON output record six exact symbolic checks: Pascal composition and inversion, binomial filter expansion, an indefinite 2-by-2 control, a negative Pick diagonal for the planted quartet, and preservation of its negative witness. The divisor-weight comparisons are exact rational calculations. All checks passed.

The original manuscripts were not modified. The latest port construction is used to select relevant tests, not treated as a proof of the needed global bound. This pass has identified a real positive combinatorial mechanism and quantified two unsuccessful alternatives; the one-sided discrepancy estimate remains unproved.
