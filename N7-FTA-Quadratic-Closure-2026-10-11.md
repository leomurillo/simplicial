# An arithmetic quadratic closure problem from unique factorization

11 October 2026. Objective: pursue RH through a quadratic arithmetic construction permitting equality, with an explicit test distinguishing the zeta coefficients from Davenport–Heilbronn coefficients.

**Status.** The quadratic functional, its arithmetic formula, and the obstruction furnished by any off-line zero are derived below. Its finite-dimensional minima are computable. Convergence of these minima to zero is not established. The Hilbert-space framework is classical Nyman–Beurling theory, not a claimed new RH criterion or a proof of RH. This note supplies a concrete construction problem for the user's prime/spectral completeness intuition.

## 1. Unique factorization gives exact inverse coefficients

The arithmetic identity is

\[
\sum_{d\mid n}\mu(d)=\mathbf1_{n=1}.
\tag{1}
\]

Consequently, for Re s>1,

\[
\zeta(s)\sum_{n\ge1}\frac{\mu(n)}{n^s}=1.
\]

The coefficient identity is exact at every integer. The analytic question is whether suitable finite inverse approximations close in the norm below. Pointwise cancellation at finitely many integers does not yet give that norm convergence.

## 2. The pole must be canceled inside the same construction

Let

\[
V_N(s)=\sum_{n\le N}a_n n^{-s},\qquad V_N(1)=\sum_{n\le N}\frac{a_n}{n}=0.
\tag{2}
\]

For x>0 define

\[
f_a(x)=-\sum_{n\le N}a_n\left\{\frac1{nx}\right\},\qquad
e_a(x)=\mathbf1_{(0,1)}(x)-f_a(x).
\]

For x>1, the fractional parts equal 1/(nx), so (2) makes f_a(x)=0. Both f_a and e_a are bounded and supported in (0,1), up to endpoints of measure zero. Hence they belong to L²(0,1).

The Mellin identity

\[
\int_0^\infty\{1/(nx)\}x^{s-1}\,dx
=-\frac{\zeta(s)n^{-s}}s\quad(0<\Re s<1)
\]

gives

\[
\int_0^1 e_a(x)x^{s-1}\,dx
=\frac{1-\zeta(s)V_N(s)}s.
\tag{3}
\]

The constraint cancels the pole at s=1. This couples the inverse approximation and pole compensation, rather than treating the pole as a disposable term.

Mellin–Plancherel on Re s=1/2 yields the nonnegative energy

\[
\mathcal E_N(a)=\|e_a\|_2^2
=\frac1{2\pi}\int_{-\infty}^\infty
\frac{|1-\zeta(1/2+it)V_N(1/2+it)|^2}{1/4+t^2}\,dt.
\tag{4}
\]

This belongs to the classical approximation approach: see [Báez-Duarte, *A strengthening of the Nyman–Beurling criterion*](https://arxiv.org/abs/math/0202141) and [Darses and Hillion, *Polynomial approximations in a generalized Nyman–Beurling criterion*](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1227.pdf). For our pole-constrained integer family, only the sufficiency proved directly below is needed; no unproved converse for a restricted coefficient choice is used.

## 3. The energy is an explicit arithmetic sum

Substitute y=1/x. Because (2) cancels the linear parts of the fractional parts,

\[
e_a(1/y)=1-\sum_{n\le N}a_n\lfloor y/n\rfloor\quad(y\ge1).
\]

All jumps occur at integers. Integration over [k,k+1) therefore gives

\[
\boxed{\mathcal E_N(a)=\sum_{k=1}^\infty
\frac{\left|1-\sum_{n\le N}a_n\lfloor k/n\rfloor\right|^2}{k(k+1)}.}
\tag{5}
\]

This is a one-sided quadratic object with no strict positive margin required. It is nonnegative for every coefficient vector satisfying (2). The proof obligation is an upper estimate tending to zero for a constructed sequence, not another proof that a square is nonnegative.

If rho=beta+i gamma is a zeta zero with beta>1/2, equation (3) gives

\[
\int_0^1e_a(x)x^{\rho-1}\,dx=\frac1\rho.
\]

Cauchy–Schwarz implies

\[
\boxed{\mathcal E_N(a)\ge\frac{2\beta-1}{|\rho|^2}.}
\tag{6}
\]

Thus any construction with E_N(a^(N))→0 excludes every such zero; the functional equation then gives RH. The proof requires neither a strict stability gap, simplicity of zeros, nor a finite exceptional set.

Equation (6) also quantifies why a finite small energy does not prove RH: it bounds displacement in relation to zero height, but remains compatible with sufficiently high or sufficiently small displacement.

## 4. A finite coefficient optimization, without numerical zeta zeros

Eliminate a1=−sum_{n=2}^N a_n/n. At integers k the error becomes

\[
e_a(1/k)=1+\sum_{n=2}^N a_n\{k/n\}.
\]

For real coefficients, set

\[
b_n=\sum_{k\ge1}\frac{\{k/n\}}{k(k+1)}=\frac{\log n}{n},\qquad
H_{mn}=\sum_{k\ge1}\frac{\{k/m\}\{k/n\}}{k(k+1)}.
\]

Then

\[
\mathcal E_N(a)=1+2b^Ta+a^THa.
\tag{7}
\]

The formula for b follows by telescoping on residue classes, or by integrating the corresponding fractional-part difference. The periodic functions involved also give an efficient exact expression for H: with L=lcm(m,n),

\[
H_{mn}=\frac1L\sum_{r=1}^{L}\{r/m\}\{r/n\}
\left[\psi\left(\frac{r+1}{L}\right)-\psi\left(\frac rL\right)\right],
\tag{8}
\]

where psi in (8) is the digamma function. This follows from summing 1/((r+jL)(r+1+jL)) over j≥0.

H is positive definite. If a linear combination of {k/n} vanished at every positive integer k, introduce a1 to cancel sum a_n/n. Then sum a_n floor(k/n)=0 for every k. Taking consecutive differences gives sum_{n|k}a_n=0, and induction on k forces all a_n=0. Positive weights in H finish the proof.

The exact finite minimizer and minimum therefore satisfy

\[
a_*=-H^{-1}b,\qquad d_N^2=1-b^TH^{-1}b\ge0.
\tag{9}
\]

The minima are nonincreasing because adding a coefficient enlarges the admissible space. Monotonicity and nonnegativity give existence of a limit, not that the limit is zero.

The numerical probe, which uses no zeta zeros, gave:

| N | squared minimum |
|---|---:|
| 4 | 0.0659516942 |
| 8 | 0.0242445253 |
| 12 | 0.0204981473 |
| 24 | 0.0155777780 |

A 60-digit evaluation of H_(3,8) differed from the double-precision formula by 1.6e−17 or less. The table is not an interval certificate or evidence sufficient to conclude a zero limit. Numerical coefficient vectors and condition numbers are retained in the JSON output.

## 5. What the FTA cancellation does and does not pay for

For 1≤k≤N, (1) gives

\[
\sum_{n\le N}\mu(n)\lfloor k/n\rfloor=1.
\]

Raw Möbius coefficients give exact cancellation on that initial range, but generally violate (2). Put c_N=sum_{n≤N}mu(n)/n and correct a1=1−c_N while retaining a_n=mu(n) for n≥2. The pole constraint then holds, but the error on the initial range becomes c_N k. Its contribution to the energy is exactly

\[
|c_N|^2\sum_{k=1}^N\frac{k}{k+1}
=|c_N|^2(N+1-H_{N+1}).
\tag{10}
\]

Thus even the region of exact FTA cancellation acquires a norm cost when the pole is correctly coupled. This is a quantitative design constraint for coefficient selection. Logarithmic smoothing, binomial weights, or the optimizer (9) can change that cost, but each needs a uniform bound on the whole sum (5).

## 6. Davenport–Heilbronn distinguishes the arithmetic identity

In Paper 53's standard normalization, the DH Dirichlet coefficients are periodic modulo 5 with values (1,kappa,−kappa,−1,0). At the coprime pair 2 and 3,

\[
a(6)=1\ne-\kappa^2=a(2)a(3).
\]

For the same fixed Möbius inverse used for zeta,

\[
(\mu*a)(6)=a(6)-a(3)-a(2)+a(1)=2,
\]

whereas (mu*1)(6)=0. This is an exact coefficient-level matched-pair failure. It demonstrates that the inverse cancellation being used is arithmetic, not a consequence of the functional equation alone.

Scope: DH has its own formal Dirichlet inverse, so failure of the fixed Möbius inverse is not by itself a theorem of critical-norm nonconvergence for every DH approximation. Nor is the ordinary fractional-part Gram matrix a DH Gram matrix: its Mellin transform specifically contains zeta. A full comparison of alternative DH approximation families would require their own kernels. No such extra theorem is being assumed here.

## 7. The next proof obligation

One must establish d_N²→0 in (9), or exhibit explicit pole-constrained coefficients in (5) whose energies tend to zero. This requires controlling the cumulative weighted tail, not just increasing the number of exactly canceled integer coefficients. The quadratic form is explicit and the finite minima are fully specified; a uniform analytic estimate on their limit remains to be proved.

Files: `empirical/connes_route/probe_fta_quadratic_closure.py` and its JSON output. The original manuscripts were left unchanged.
