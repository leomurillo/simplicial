# A sharp factorial envelope: uniform calibration without Möbius cancellation

12 October 2026. A revised construction for the factorial-majorant route. This changes the envelope cost; it does not prove a bound for the earlier coarse-envelope optimum E*.

**Proved here:** the revised optimum is uniformly within O(sqrt x) of the actual prime window, without RH or a short-interval Möbius estimate. A larger exact prefix makes this gap O(1). **Not proved:** that the prime window, or the revised optimum, is at most x/2 plus a square-root error. Thus the absolute height bound and RH remain open in this work.

## 1. Retain the integer and parity information in Stirling's formula

For m≥2 set l=floor(m/2) and

\[
F(m)=\log(m!)-\log(l!),\qquad
A(n)=(n+\tfrac12)\log n-n.
\]

[Robbins's bounds](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf) give

\[
\log(n!)=A(n)+\tfrac12\log(2\pi)+r_n,
\qquad \frac1{12n+1}<r_n<\frac1{12n}.
\]

Define

\[
L_m=A(m)-A(l)+\frac1{12m+1}-\frac1{12l},
\]
\[
U_m=A(m)-A(l)+\frac1{12m}-\frac1{12l+1}.
\]

Then L_m<F(m)<U_m, and their width is exactly

\[
\delta_m=U_m-L_m
=\frac1{12m(12m+1)}+\frac1{12l(12l+1)}
\le\frac5{72m^2},                                         \tag{1}
\]

since l≥m/3. In particular, the uncertainty is O(m^(−2)), rather than the O(log m) allowance obtained by discarding the integer/parity information.

Choose an integer cutoff B≥2. For 2≤m≤B replace the bracket by the exact value F(m), so L_m=U_m=F(m) on that prefix. Those values can be obtained from the recurrence log(n!)=log((n−1)!)+log n. This explicitly permits exact small-factorial data; it is a modification of the preceding envelope's input specification.

## 2. The revised finite polytope

Fix integer x≥2. Group k≤x/2 by m=floor(x/k). Choose one representative k_m in each nonempty group and put

\[
J(x)=\{\lfloor x/n\rfloor:2\le n\le x\},
\quad A_{j,m}=\lfloor j/k_m\rfloor-\lfloor j/(2k_m)\rfloor.
\]

The column is independent of the representative on J(x). For grouped coefficients d_m, impose

\[
\sum_m A_{j,m}d_m\ge\mathbf1_{\{j=1\}}\quad(j\in J(x)).
\tag{2}
\]

Define the revised upper-envelope cost

\[
\mathcal E_B(d;x)=\sum_m(d_m^+U_m-d_m^-L_m),
\quad d_m^+=\max(d_m,0),\quad d_m^-=\max(-d_m,0),
\]

and let \(\mathcal E_B^*(x)\) be its infimum over (2). Splitting d into positive and negative parts expresses this as an ordinary finite linear program.

The factorial identity and nonnegativity of Λ give, for every feasible d,

\[
W(x):=\psi(x)-\psi(\lfloor x/2\rfloor)
\le\sum_m d_mF(m)\le\mathcal E_B(d;x).                     \tag{3}
\]

This establishes a lower bound W(x) for the revised optimum without assuming RH.

## 3. Uniform calibration theorem

**Theorem.** For every integer x≥2 and B≥2,

\[
\boxed{0\le\mathcal E_B^*(x)-W(x)
\le\frac5{72}\left(\frac{x}{3B^3}+\frac1B\right).}          \tag{4}
\]

**Proof.** Use the grouped full Möbius vector

\[
d_m=\sum_{x/(m+1)<k\le x/m}\mu(k).
\]

It satisfies (2) with equality, and Möbius inversion gives Σ_m d_mF(m)=W(x). The bracket cost therefore satisfies

\[
0\le\mathcal E_B(d;x)-W(x)
\le\sum_{m>B}|d_m|\delta_m.
\]

No cancellation estimate is needed: the elementary cell-length bound is

\[
|d_m|\le\left\lfloor\frac xm\right\rfloor
          -\left\lfloor\frac x{m+1}\right\rfloor
\le\frac{x}{m(m+1)}+1.
\]

Using (1), extending the sum to all integers m>B, and applying integral bounds for decreasing positive series gives

\[
\sum_{m>B}|d_m|\delta_m
\le\frac5{72}\left(x\sum_{m>B}m^{-4}+\sum_{m>B}m^{-2}\right)
\le\frac5{72}\left(\frac{x}{3B^3}+\frac1B\right).
\]

Combine this feasible upper bound with (3). ∎

Two choices illustrate the result:

* B=max(2,ceil(x^(1/6))) gives a uniform O(sqrt x) gap.
* B=max(2,ceil(x^(1/3))) gives a uniform O(1) gap.

The number of exact prefix values, the work to compute grouped Möbius coefficients, and numerical precision are separate complexity costs. This theorem is not a claim of a fast algorithm for the full arithmetic problem.

## 4. The pointwise conditional gap is removed for this revised cost

Under RH, W(x)=x/2+O(sqrt x log²x). Taking B=ceil(x^(1/6)) in (4) proves

\[
\mathcal E_B^*(x)=x/2+O(\sqrt x\log^2x)
\quad\text{for every integer }x.                           \tag{5}
\]

Thus the revised envelope has the desired pointwise estimate under RH alone. No pointwise square-root estimate for Möbius sums on the hyperbola cells is required. The earlier conditional exponent 2/3 arose in bounding the coarse absolute-value penalty; it is not an unavoidable obstruction for all envelope definitions.

Conversely, an unconditional upper bound of the form (5), or with any fixed power of log x, would imply the same upper bound for W by (3), and hence RH by the established dyadic telescoping and one-sided Landau argument.

This is a pointwise equivalence for the revised construction. It must not be attributed to the original coarse-envelope optimum without an additional comparison theorem. In particular, a sharper envelope can have a smaller optimum, so its upper bound does not upper-bound the old optimum.

## 5. Numerical consistency checks

The script `empirical/connes_route/check_sharp_stirling_envelope.py` evaluates the explicit grouped Möbius certificate at 60 decimal digits, checks the brackets, independently computes W from prime powers, and compares with the analytic bound (4).

| x | B | certificate excess above W, approximately | bound from (4) |
|---:|---:|---:|---:|
| 1,000 | 4 | 0.010023 | 0.379051 |
| 10,000 | 5 | 0.024477 | 1.865741 |
| 100,000 | 7 | 0.027501 | 6.758652 |

The Möbius identity residual was below 10^(−55) in the last row. These are high-precision consistency checks, not interval certificates. The all-x result is the analytic proof of (4), not extrapolation from this table. The table concerns the explicit certificate, not a numerical solution of the revised LP.

## 6. What changed in the research target

The proposed local coefficient correction turned out not to be necessary for controlling the envelope's calibration error: correcting the local factorial brackets already makes the full Möbius certificate inexpensive relative to W. This removes an artificial need to prove stronger cell-by-cell cancellation merely to pay for Stirling uncertainty.

It does not remove the arithmetic discrepancy. In the identity

\[
\mathcal E_B^*(x)-x/2
=\bigl(W(x)-x/2\bigr)+\bigl(\mathcal E_B^*(x)-W(x)\bigr),
\]

only the second term has been bounded unconditionally at square-root scale here. The first is still the RH-strength prime-window estimate.

The revised LP uses elementary logarithms and floor functions, plus a small exact factorial prefix. That does not make its optimum arithmetically independent of the primes: (4) shows how closely it encodes their window count. Re-expressing this count or computing a narrow envelope around it is not a proof of its deviation from x/2.

The concrete outcome is a uniform calibration theorem and a pointwise RH equivalence for the revised cost. The remaining closure step is an independent upper bound for that cost relative to x/2, or an arithmetic positivity theorem yielding the same estimate. Neither is proved in this note.
