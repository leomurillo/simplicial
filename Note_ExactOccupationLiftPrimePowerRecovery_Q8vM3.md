# Note: Exact Occupation-Lift Prime-Power Recovery

Random suffix: `Q8vM3`

Mission: solve the finite algebraic lock:

\[
\text{occupation lift}
\quad\Longrightarrow\quad
\text{exact upstairs prime-power coefficients before CRT compression}.
\]

Verdict:

\[
\boxed{
\text{Solved exactly in the occupation-decorated symmetric algebra.}
}
\]

No analytic estimate is involved.  The von Mangoldt coefficient
\(\Lambda(p^r)=\log p\) appears because the logarithmic coefficient \(1/r\)
is cancelled by the derivative of \(p^{-rs}\).  The single-axis projector must
act before CRT compression, because compression aliases occupation histories.

## 1. The Carrier

Fix a finite prime set
\[
\mathcal P_n=\{p\le p_n\}.
\]

Let
\[
V_n=\bigoplus_{p\in\mathcal P_n}\mathbb C e_p
\]
and use the polynomial symmetric algebra
\[
\mathcal F_n
=
\operatorname{Sym}(V_n)
\cong
\mathbb C[\mathbb N^{\mathcal P_n}].
\]

Its monomial basis is
\[
e_\alpha=\prod_{p\in\mathcal P_n}e_p^{\alpha_p},
\qquad
\alpha=(\alpha_p)_{p\in\mathcal P_n}\in\mathbb N^{\mathcal P_n},
\]
with product
\[
e_\alpha e_\beta=e_{\alpha+\beta}.
\]

This basis convention matters: \(e_p^r=e_{r e_p}\) with coefficient \(1\).
All multinomial coefficients occur only on mixed occupations in expansions of
\((\sum_p x_p e_p)^r\), and those are killed by the single-axis projector.

Define the log-height dictionary
\[
e_{r e_p}\longleftrightarrow p^r,
\qquad
|r e_p|_{\log}=r\log p.
\]

## 2. Single-Axis Projector

Define
\[
\Pi_{\rm sa}e_\alpha
=
\begin{cases}
e_\alpha,& \alpha=r e_p\text{ for some }p,\ r\ge1,\\
0,& \text{otherwise}.
\end{cases}
\]

This is the upstairs version of the von-Mangoldt support rule:

1. keep prime powers \(p^r\);
2. discard mixed integers with at least two distinct prime factors.

## 3. Logarithmic Occupation Series

Let
\[
H_s=\sum_{p\in\mathcal P_n}p^{-s}e_p.
\]

For a finite occupation cutoff \(K\), set
\[
L_{n,K}(s)
=
\sum_{k=1}^{K}{1\over k}H_s^k.
\]

Then
\[
H_s^k
=
\sum_{\alpha:\ |\alpha|=k}
{k!\over\prod_p\alpha_p!}
\prod_p p^{-s\alpha_p}e_\alpha.
\]

Applying \(\Pi_{\rm sa}\) keeps only \(\alpha=k e_p\).  For this
single-axis multi-index the multinomial coefficient is \(1\).  Hence
\[
\Pi_{\rm sa}H_s^k
=
\sum_{p\in\mathcal P_n}p^{-ks}e_{k e_p}.
\]

Therefore
\[
\Pi_{\rm sa}L_{n,K}(s)
=
\sum_{p\in\mathcal P_n}\sum_{1\le r\le K}
{1\over r}p^{-rs}e_{r e_p}.
\]

## 4. Exact Von Mangoldt Coefficient

Let
\[
D_s=-{\partial\over\partial s}.
\]

Then
\[
D_s\left({1\over r}p^{-rs}\right)
=
{1\over r}(r\log p)p^{-rs}
=
(\log p)p^{-rs}.
\]

Thus:

**Theorem 4.1 (exact upstairs von Mangoldt recovery).**  
For every finite prime set \(\mathcal P_n\) and every occupation cutoff \(K\),
\[
\boxed{
D_s\Pi_{\rm sa}L_{n,K}(s)
=
\sum_{p\in\mathcal P_n}\sum_{1\le r\le K}
(\log p)p^{-rs}e_{r e_p}.
}
\]
Equivalently,
\[
D_s\Pi_{\rm sa}
\sum_{k=1}^{K}{1\over k}H_s^k
=
\sum_{p\le p_n}\sum_{1\le r\le K}
\Lambda(p^r)(p^r)^{-s}e_{r e_p}.
\]

This proves the prime-power coefficients exactly upstairs.

## 5. Test-Function Form

Let \(G\) be a log-side detector.  The coefficient distribution in Theorem
4.1 acts on \(G\) by the height map
\[
e_{r e_p}\mapsto G(r\log p).
\]

Therefore the finite occupation observable is
\[
\boxed{
\operatorname{VM}_{n,K}(G)
=
\sum_{p\le p_n}\sum_{1\le r\le K}
(\log p)G(r\log p).
}
\]

The reflected completed finite-place term is obtained by applying the same
upstairs extractor to the reflected detector \(G^\#(u)=G(-u)\):
\[
\operatorname{VM}_{n,K}(G^\#)
=
\sum_{p\le p_n}\sum_{1\le r\le K}
(\log p)G(-r\log p).
\]

## 6. Why Compression Must Come Later

At primorial level \(P_n\), choose local prime-axis characters \(\chi_p\) and
define the CRT compression map
\[
\pi_{\rm CRT}:\mathcal F_n\to\mathbb C[\widehat R_n],
\qquad
\pi_{\rm CRT}(e_\alpha)=\prod_{p\le p_n}\chi_p^{\alpha_p}.
\]

Since each local \(\chi_p\) has finite order \(p\),
\[
\pi_{\rm CRT}(e_{r e_p})
=
\pi_{\rm CRT}(e_{(r+p)e_p}).
\]

So unbounded prime-power occupation depth is not recoverable from the
compressed character label.  Worse, mixed occupations may share the same
compressed label as a single-axis occupation.  For example, in the row
\(\{2,3,5\}\),
\[
5e_5
\quad\text{and}\quad
2e_2+3e_3
\]
both compress to the trivial local label:
\[
(0,0,5)\equiv(2,3,0)\equiv(0,0,0)\pmod{(2,3,5)}.
\]

But upstairs they are different:

1. \(5e_5\) represents the prime power \(5^5\) and carries coefficient
   \((\log 5)5^{-5s}\) after \(\Pi_{\rm sa}\);
2. \(2e_2+3e_3\) is mixed and must be killed by \(\Pi_{\rm sa}\).

Therefore
\[
\boxed{
\Pi_{\rm sa}\text{ is well-defined on }\mathcal F_n
\text{ and not well-defined after CRT compression.}
}
\]

The correct order is:
\[
\mathcal F_n
\xrightarrow{\Pi_{\rm sa}}
\text{single-axis occupations}
\xrightarrow{D_s}
\text{von Mangoldt coefficients}
\xrightarrow{\pi_{\rm CRT}}
\text{compressed shadow}.
\]

The wrong order,
\[
\mathcal F_n
\xrightarrow{\pi_{\rm CRT}}
\mathbb C[\widehat R_n]
\xrightarrow{?}
\text{single-axis extraction},
\]
has no canonical final arrow.

## 7. Relation to Hayes-Mobius Currents

The compressed Hayes-Mobius coefficient vector records convolution shadows
\[
\widehat h^{*k}
\]
on finite CRT labels.  The occupation-decorated lift refines this shadow by
storing the pre-compression occupation path
\[
\widetilde{\widehat h^{*k}}
=
\sum_{\alpha:\ |\alpha|=k}
{k!\over\prod_p\alpha_p!}
\prod_p h_p^{\alpha_p}e_\alpha
\in\operatorname{Sym}^k(V_n).
\]

Compression recovers the old finite current:
\[
\pi_{\rm CRT}\widetilde{\widehat h^{*k}}
=
\widehat h^{*k}.
\]

Thus the lift adds no external arithmetic data.  It remembers exactly the
occupation history that the finite CRT shadow forgets.

For von Mangoldt recovery, this remembered history is not optional: it is the
only place where the distinction between \(p^r\) and mixed products survives.

## 8. Final Closure Statement

**Theorem 8.1 (occupation lift closes the finite prime-power coefficient
lock).**  
At every finite primorial row and finite occupation cutoff \(K\), the
occupation-decorated symmetric algebra \(\mathcal F_n=\operatorname{Sym}(V_n)\)
implements the exact formula
\[
\operatorname{VM}_{n,K}
=
D_s\Pi_{\rm sa}
\sum_{k=1}^{K}{1\over k}H_s^k.
\]
Under the log-height dictionary this is precisely
\[
\operatorname{VM}_{n,K}(G)
=
\sum_{p\le p_n}\sum_{1\le r\le K}
(\log p)G(r\log p).
\]
CRT compression is allowed only after this extraction.  If compression is
performed first, occupation depth is aliased modulo local prime orders and
mixed occupations can collide with single-axis occupations.

So the finite algebraic lock is closed:

\[
\boxed{
\text{exact prime-power coefficients before CRT compression.}
}
\]

