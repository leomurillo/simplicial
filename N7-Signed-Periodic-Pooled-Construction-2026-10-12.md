# Signed periodic coefficients: feasibility, improved cost, and the exact remaining gap

12 October 2026. Companion to the explicit pooled coefficient note. This construction escapes the nonnegative divisor-square family and improves the uniform leading constant. It does not attain the RH-closing bound. All asymptotic claims below follow from displayed identities; the finite search supplies candidates only.

## 1. A general explicit conversion

Let L be a positive integer, and choose rational a_d supported on divisors d of L such that

\[
a_1=1,\qquad \sum_{d\mid L}a_d/d=0,\qquad
g(j):=\sum_{d\mid L}a_d\lfloor j/d\rfloor\ge0
\quad(0\le j<L).
\tag{1}
\]

Extend g to real arguments by the same floor formula. It is constant between consecutive integers, and balance gives g(y+L)=g(y). Also g(y)=1 on [1,2), and g(y)=0 on [0,1). Thus g(y) majorizes the window indicator on the entire nonnegative real axis.

For any block X define, explicitly,

\[
c_k=\sum_{\substack{j\ge0\\2^j\mid k}}a_{k/2^j}
\quad(1\le k\le X),\qquad c_k=0\quad(k>X).
\tag{2}
\]

Absent a entries mean zero. The recursion c_k-c_{k/2}=a_k, with c at nonintegers zero, proves for 0≤y≤X

\[
\sum_{k\le X}c_k(\lfloor y/k\rfloor-\lfloor y/(2k)\rfloor)=g(y).
\tag{3}
\]

For every n≥2 and X<x≤2X, y=x/n≤X. Summing (3) proves every pooled inequality, with no primes or optimization required. The finite conditions (1) are an all-X certificate.

The pooled height is exactly

\[
H_X(c)=\sum_{X<x\le2X}\sum_{d\mid L}a_d\log(\lfloor x/d\rfloor!).
\tag{4}
\]

The telescoping terms omitted beyond X have floor arguments at most 1, so their log-factorials are zero. For integral a, these factorial ratios are integers by Legendre's formula and g≥0; they majorize the prime window even at each individual scale. This uses the classical floor-function mechanism behind Landau's factorial-ratio criterion, not a new integrality principle. See [Soundararajan, Integral Factorial Ratios](https://arxiv.org/abs/1901.05133).

## 2. A simple rule that escapes the earlier obstruction

Take

\[
(a_1,a_2,a_3,a_4,a_6,a_{12})=(1,-2,-1,1,1,-1).
\tag{5}
\]

Its values on one period j=0,...,11 are

\[
(0,1,0,0,0,1,0,1,1,1,0,1).
\]

Balance is exact. Formula (2) simplifies to

\[
c_1=1,\quad c_2=c_3=-1,\quad
c_{3\cdot2^j}=-1\ (j\ge2,\ 3\cdot2^j\le X),
\tag{6}
\]

with all other entries zero and entries above X omitted. This has logarithmically many nonzero integer coefficients. Its divisor transform b(n)=Σ_{d|n}c_d has b(6)=-1 when X≥6. Hence it genuinely lies outside the nonnegative divisor-square family excluded in the previous note.

The associated integer at scale x is

\[
\frac{x!\,\lfloor x/4\rfloor!\,\lfloor x/6\rfloor!}
{(\lfloor x/2\rfloor!)^2\,\lfloor x/3\rfloor!\,\lfloor x/12\rfloor!}.
\tag{7}
\]

## 3. A uniform cost theorem, including dependence on the rule

Write

\[
C(a)=-\sum_d\frac{a_d\log d}{d},\qquad
S(a)=\sum_d|a_d|,\qquad A_X=X(3X+1)/4.
\]

For every u>0,

\[
|\log(\lfloor u\rfloor!)-(u\log u-u)|
\le1+2\log\max(1,u).
\]

For u<1 this follows directly; for u≥1 use the integral bounds on log(n!) and compare u log u-u with n log n-n for n=floor(u). Substituting u=x/d, the x log x and linear x terms cancel by balance. Therefore

\[
\boxed{|H_X(c)-2C(a)A_X|
\le S(a)X[1+2\log(4X)].}
\tag{8}
\]

This bound is uniform in both X and the chosen rule, even if L depends on X.

For (5), S=7 and C=(log 2)/2+(log 3)/4. In particular,

\[
H_X(c)\le(\log2+\tfrac12\log3)A_X
+7X[1+2\log(4X)].
\tag{9}
\]

The leading multiplier is 1.242453324894..., improved from the dyadic rule's 1.386294361120....

## 4. A stronger finite certificate

A finite linear-program search on divisors of 2520 produced the following integral rule. Optimality of that search is not needed or claimed. Every omitted divisor has coefficient zero:

```text
1:1, 2:-2, 3:-1, 4:1, 5:-1, 6:2, 7:-1, 10:2, 12:-2,
14:1, 15:1, 18:-1, 20:-1, 21:1, 24:1, 30:-3, 35:1, 36:2,
42:-2, 60:2, 70:-2, 72:-1, 84:1, 90:2, 105:-2, 120:-1,
126:1, 140:2, 168:-1, 180:-3, 210:4, 252:-3, 280:-1,
315:1, 360:1, 420:-1, 504:1, 630:-2, 1260:-1, 2520:-3
```

Exact rational balance and all 2520 integer values were checked: 0≤g(j)≤7 and g(1)=1. Thus periodicity proves feasibility for every X, not merely for tested blocks. Here S=63 and

\[
C=-\sum_d a_d\log(d)/d=0.565549150526273\ldots,
\]

so (8) gives a main multiplier 2C=1.131098301052546.... The exact logarithmic expression, rather than its rounded decimal, defines the bound.

`empirical/connes_route/signed_periodic_majorant.py` contains the fixed rules and checks balance, full-period nonnegativity, and exact pooled inequalities for X=2,7,37,100,1000. Its JSON records the results. Heights and printed logarithmic constants are floating-point diagnostics; the finite feasibility certificates are integer/rational calculations. All checks passed.

## 5. Exact identification of the leading-cost gap

The remaining leading constant has a useful exact interpretation:

\[
\boxed{C(a)-\tfrac12
=\int_1^\infty
\frac{g(y)-\mathbf1_{[1,2)}(y)}{y^2}\,dy.}
\tag{10}
\]

Indeed, for q=floor(R/d),

\[
\int_1^R\frac{\lfloor y/d\rfloor}{y^2}\,dy
=\frac{H_q}{d}-\frac qR.
\]

Taking the finite weighted sum and R→∞, the common log R, Euler-constant, and constant terms cancel by balance, leaving -Σ a_d log(d)/d. The indicator integral is 1/2. This proof uses no prime distribution theorem.

Thus the exact leading excess is a nonnegative weighted approximation error. Periodicity forces g=1 on [L+1,L+2), so

\[
C(a)-\tfrac12\ge\frac1{(L+1)(L+2)}>0.
\tag{11}
\]

Every fixed-period rule has a strictly positive quadratic excess as X→∞. Consequently neither displayed fixed rule closes RH. Improving a numerical constant at finitely many periods does not prove the required growth law.

## 6. The quantitative construction still needed

This family would attain the RH-closing pooled height if one constructed rules a=a_X satisfying (1) and, for some fixed m≥1,

\[
\int_1^\infty\frac{g_X(y)-\mathbf1_{[1,2)}(y)}{y^2}\,dy
\ll X^{-1/2}(\log X)^m,
\qquad
S(a_X)\ll X^{1/2}(\log X)^{m-1}.
\tag{12}
\]

Equation (8) would then give H_X≤A_X+O(X^{3/2}(log X)^m). These are sufficient estimates, not necessary conditions on every possible pooled construction. The first estimate and (11) require periods at least of order X^{1/4}/(log X)^{m/2}, up to constants; they do not provide such a family.

The achieved result is a signed, explicitly certified all-X construction with a strictly improved uniform leading cost. The unresolved step is simultaneous control of the weighted residual and coefficient norm as the period grows. No unconditional square-root bound or RH proof is established here.
