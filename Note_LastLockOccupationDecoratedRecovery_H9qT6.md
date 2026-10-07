# Note: Last Lock — Occupation-Decorated Hayes-Mobius Recovery

Random suffix: `H9qT6`

Mission: solve the last finite-place lock:

\[
\text{Does Hayes-Mobius/CRT recovery implement }
-\partial_s\Pi_{\rm sa}\log(1-H_s)^{-1}
\text{ with the correct von Mangoldt weights?}
\]

Verdict:

\[
\boxed{
\text{Yes, but only in the occupation-decorated convolution lift.}
}
\]

The compressed quotient-character convolution algebra is too small: it
aliases occupation histories.  The correct carrier is the bosonic/Fock
occupation lift of the prime-axis CRT character space.  In that lift the
von Mangoldt law is exact.

## 1. The Problem With the Compressed CRT Algebra

At primorial level \(P_n=p_n\#\), the finite dual group is
\[
\widehat R_n\cong\prod_{p\le p_n}\mathbb Z/p\mathbb Z.
\]

A prime-axis generator at \(p\) has finite order \(p\).  Therefore repeated
convolution is periodic:
\[
r e_p\mapsto r\pmod p.
\]

But the Euler product needs the free occupation labels
\[
r e_p,\qquad r=1,2,3,\ldots,
\]
because they represent the prime powers \(p^r\).

Thus finite CRT labels alone cannot be the final storage layer for the
occupation variable \(r\).  They see \(r\pmod p\); the von Mangoldt
distribution needs \(r\) itself.

This is not cosmetic.  Mixed words and single-axis words can share the same
final finite character label after compression.  Once the convolution has
been summed only as
\[
\widehat h^{*r}(\eta),
\]
the path/occupation decomposition is not generally recoverable.

So the old compressed target
\[
\mathsf C_r(h)=
\sum_{\mathfrak e,\mathfrak f}\sum_\eta
\widehat h^{*r}(\eta)A_\eta^{\mathfrak f,\mathfrak e}
\]
is the right *shadow*, but not the right *carrier*, for prime-power recovery.

## 2. The Forced Lift

Let \(V_n\) be the prime-axis vector space
\[
V_n=\bigoplus_{p\le p_n}{\mathbb C}e_p.
\]

Define the bosonic occupation algebra
\[
{\mathcal F}_n
=
\operatorname{Sym}(V_n)
=
\bigoplus_{r\ge0}\operatorname{Sym}^r(V_n),
\]
with product
\[
e_\alpha e_\beta=e_{\alpha+\beta},
\qquad
\alpha,\beta\in\mathbb N^{\{p\le p_n\}}.
\]

There is a compression map
\[
\pi_{\rm CRT}:{\mathcal F}_n\to{\mathbb C}[\widehat R_n]
\]
given on basis vectors by
\[
\pi_{\rm CRT}(e_\alpha)
=
\prod_{p\le p_n}\chi_p^{\alpha_p},
\]
where \(\chi_p\) is a chosen local prime-axis character.  This map forgets
occupation depth modulo the local prime orders.  The point is to apply the
von Mangoldt extraction before this forgetting.

Define the occupation-decorated Hayes-Mobius current
\[
\widetilde{\mathsf C}_r(h)
=
h^{\odot r}\in\operatorname{Sym}^r(V_n).
\]

Its compressed shadow is the old convolution coefficient:
\[
\pi_{\rm CRT}\widetilde{\mathsf C}_r(h)
=
\widehat h^{*r}.
\]

So the lift is not new external data.  It is the pre-compression object whose
shadow Paper 10/11 already uses.

## 3. Single-Axis Projector

Define
\[
\Pi_{\rm sa}e_\alpha
=
\begin{cases}
e_\alpha,& \alpha=r e_p\text{ for some }p,\ r\ge1,\\
0,& \text{otherwise}.
\end{cases}
\]

This is the exact algebraic form of the primitive/von-Mangoldt support rule:
keep prime powers, discard mixed-prime integers.

In compressed CRT language, this projector is not well-defined after
\(\pi_{\rm CRT}\), because the distinction between \(r e_p\) and other paths
may have been lost.  Therefore
\[
\boxed{
\Pi_{\rm sa}\text{ must act in }{\mathcal F}_n\text{ before CRT compression.}
}
\]

This is the last-lock correction.

## 4. The Exact Von Mangoldt Theorem

Let
\[
H_s=\sum_{p\le p_n}p^{-s}e_p\in{\mathcal F}_n.
\]

Define the logarithmic occupation series
\[
L_n(s)
=
\log(1-H_s)^{-1}
=
\sum_{r\ge1}{1\over r}H_s^r.
\]

Then
\[
\Pi_{\rm sa}H_s^r
=
\sum_{p\le p_n}p^{-rs}e_{r e_p}.
\]

Therefore
\[
\Pi_{\rm sa}L_n(s)
=
\sum_{p\le p_n}\sum_{r\ge1}{1\over r}p^{-rs}e_{r e_p}.
\]

Apply \(D_s=-\partial_s\):
\[
D_s\Pi_{\rm sa}L_n(s)
=
\sum_{p\le p_n}\sum_{r\ge1}
(\log p)p^{-rs}e_{r e_p}.
\]

Under the dictionary \(e_{r e_p}\leftrightarrow p^r\),
\[
\boxed{
D_s\Pi_{\rm sa}\log(1-H_s)^{-1}
=
\sum_{p\le p_n}\sum_{r\ge1}\Lambda(p^r)(p^r)^{-s}e_{r e_p}.
}
\]

This proves the finite-place occupation lift exactly.

## 5. Test-Function Form

Let \(G_f(u)=\widehat f(u)\) be the log-Fourier transform in the Weil
test-function convention.  Applying \(G_f\) to the occupation height
\[
|r e_p|_{\log}=r\log p
\]
gives
\[
\operatorname{VM}_{n,K}(f)
=
\sum_{p\le p_n}\sum_{1\le r\le K}
(\log p)G_f(r\log p).
\]

Letting \(K\to\infty\), \(p_n\to\infty\), and applying the tail condition
from Paper 22 Lemma 8.1b gives
\[
\operatorname{VM}_{\infty}(f)
=
\sum_p\sum_{r\ge1}
(\log p)G_f(r\log p).
\]

Running the same construction on the reflected test function gives the
completed finite-place distribution
\[
\sum_p\sum_{r\ge1}
(\log p)\left(G_f(r\log p)+G_f(-r\log p)\right).
\]

This closes the algebraic content of Paper 22 Lemma 8.1a, provided the
recovery current is understood as occupation-decorated before compression.

## 6. Relation to Hayes-Mobius Coefficient Vectors

Paper 10 proves the all-order conductor-convolution law:
\[
\widehat{h^r}=Q^{1-r}\widehat h^{*r}.
\]

Paper 11 packages this as Hayes-Mobius coefficient vectors:
\[
\mathsf C_r(h)=
\sum_{\mathfrak e,\mathfrak f}\sum_\eta
\widehat h^{*r}(\eta)A_\eta^{\mathfrak f,\mathfrak e}.
\]

The present lift refines this by replacing the group convolution coefficient
\(\widehat h^{*r}(\eta)\) with its occupation-resolved preimage:
\[
\widetilde{\widehat h^{*r}}
=
\sum_{\alpha:\ |\alpha|=r}
\left(\prod_p h_p^{\alpha_p}\right)e_\alpha.
\]

Then
\[
\pi_{\rm CRT}\widetilde{\widehat h^{*r}}=\widehat h^{*r}.
\]

Thus the old Hayes-Mobius current is the image of the decorated current under
CRT compression.  For conductor support and finite Fisher geometry, the
compressed object is enough.  For von Mangoldt recovery, the decorated object
is necessary.

## 7. Gamma/K Completion

The finite-place result above supplies
\[
-{\zeta'\over\zeta}(s)
\quad\text{on the finite side.}
\]

The completed object is
\[
-{\xi'\over\xi}(s)
=
-{\zeta'\over\zeta}(s)
-{1\over s}
-{1\over s-1}
{+}
{1\over2}\log\pi
-{1\over2}{\Gamma'\over\Gamma}(s/2)
\]
up to the chosen completed-zeta normalization convention.

The \(K\)-normalization is compatible with the occupation lift because:

1. finite \(K\) sends \(e_{r e_p}\) to its reflected/conjugate occupation;
2. the reflected test-function term \(G_f(-r\log p)\) is produced by running
   the same extractor on \(f^\#\);
3. the Archimedean gamma terms live in the independent infinite-place packet
   and tensor with the finite occupation algebra.

So the finite occupation theorem does not obstruct gamma/K completion.  It
hands the finite Euler side to the Archimedean packet.

What remains outside this note is the already-isolated Archimedean selection
problem: prove that the projective Bures limit selects the metaplectic
positive-energy oscillator packet, rather than merely allowing the gamma
multiplier.  That is not a finite-place von Mangoldt issue.

## 8. Final Theorem

**Theorem (Occupation-decorated primorial von Mangoldt recovery).**  
At primorial level \(P_n\), the occupation-decorated Hayes-Mobius lift
\({\mathcal F}_n=\operatorname{Sym}(V_n)\) implements
\[
\operatorname{VM}_{n,K}(f)
=
\sum_{p\le p_n}\sum_{1\le r\le K}
(\log p)G_f(r\log p)
\]
exactly by the formula
\[
\operatorname{VM}_{n,K}
=
D_s\Pi_{\rm sa}
\sum_{1\le r\le K}{1\over r}H_s^r.
\]
The compressed quotient-character Hayes-Mobius current is the CRT shadow of
this lift.  Therefore the finite-place recovery lock closes exactly in the
occupation-decorated lift and cannot close in the compressed finite CRT
algebra alone.

## 9. What Is Actually Solved

Solved:

1. the algebraic occupation lift from squarefree prime axes to prime powers;
2. the exact von Mangoldt coefficient \(\Lambda(p^r)=\log p\);
3. the necessity of applying \(\Pi_{\rm sa}\) before finite CRT compression;
4. compatibility with \(K\)-reflection and the reflected finite-place term.

Still separate:

1. the analytic double-cutoff limit \(n,K,M\to\infty\);
2. primorial character uniformity at natural scale;
3. the Archimedean metaplectic positive-energy selection;
4. positivity of the resulting completed spectral measure.

This is the finite-place last lock, but not yet an unconditional RH proof.

