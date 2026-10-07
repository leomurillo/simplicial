# Note: Double-Cutoff Dominated Convergence on \(\mathcal D_{\delta,0}\)

Random suffix: `Q8vM3`

Mission: close the analytic double-cutoff lock in its cleanest form:

\[
G\in\mathcal D_{\delta,0}
\quad\Longrightarrow\quad
\sum_{\substack{p\le p_n\\r\le K_n\\p^r\le M_n}}
(\log p)G(r\log p)
\to
\sum_p\sum_{r\ge1}(\log p)G(r\log p).
\]

Verdict:

\[
\boxed{
\text{Closed by dominated convergence, with explicit uniform tail bounds.}
}
\]

This is purely analytic and independent of the Archimedean selection problem.
It uses only exponential log-side decay.

## 1. Detector Space

For \(\delta>0\), define
\[
\mathcal D_{\delta,0}
=
\left\{
G\in C(\mathbb R):
\|G\|_{\delta,0}:=
\sup_{u\in\mathbb R}e^{(1+\delta)|u|}|G(u)|<\infty
\right\}.
\]

Thus
\[
|G(u)|\le \|G\|_{\delta,0}e^{-(1+\delta)|u|}.
\]

For prime powers,
\[
|G(\pm r\log p)|
\le
\|G\|_{\delta,0}p^{-r(1+\delta)}.
\]

## 2. Absolute Majorant

Let
\[
a=1+\delta.
\]

Then
\[
\sum_p\sum_{r\ge1}(\log p)|G(r\log p)|
\le
\|G\|_{\delta,0}
\sum_p(\log p)\sum_{r\ge1}p^{-ar}.
\]

Since
\[
\sum_{r\ge1}p^{-ar}
=
{p^{-a}\over 1-p^{-a}}
\le
{p^{-a}\over 1-2^{-a}},
\]
we obtain
\[
\sum_p\sum_{r\ge1}(\log p)|G(r\log p)|
\le
{\|G\|_{\delta,0}\over 1-2^{-a}}
\sum_p{\log p\over p^a}.
\]

The final prime sum converges by comparison with
\[
\sum_{m\ge2}{\log m\over m^a}<\infty
\qquad (a>1).
\]

The same majorant controls the reflected term \(G(-r\log p)\).

## 3. Explicit Tail Bounds

For \(x\ge2\), set
\[
I_a(x)
=
\int_x^\infty{\log t\over t^a}\,dt
=
x^{1-a}
\left(
{\log x\over a-1}+{1\over(a-1)^2}
\right).
\]

For \(G\) with \(C_G=\|G\|_{\delta,0}\), the three cutoff tails satisfy:

### Axis Tail

\[
\sum_{p>P}\sum_{r\ge1}(\log p)|G(r\log p)|
\le
{C_G\over 1-2^{-a}}
\sum_{m>P}{\log m\over m^a}
\ll_{\delta}
C_G P^{-\delta}(\log P+1).
\]

### Occupation Tail

\[
\sum_p\sum_{r>K}(\log p)|G(r\log p)|
\le
C_G
\left(\sum_p{\log p\over p^a}\right)
{2^{-aK}\over 1-2^{-a}}
\ll_{\delta}
C_G2^{-aK}.
\]

Indeed,
\[
p^{-ar}=p^{-a}p^{-a(r-1)}
\le
p^{-a}2^{-a(r-1)}.
\]

### Dirichlet Prime-Power Tail

If \(p^r>M\), then with \(m=p^r\),
\[
(\log p)p^{-ar}
\le
(\log m)m^{-a}.
\]
Therefore
\[
\sum_{p^r>M}(\log p)|G(r\log p)|
\le
C_G\sum_{m>M}{\log m\over m^a}
\ll_{\delta}
C_G M^{-\delta}(\log M+1).
\]

Hence the union tail
\[
T_{P,K,M}(G)
=
\sum_{\substack{p>P\ \mathrm{or}\ r>K\ \mathrm{or}\ p^r>M}}
(\log p)|G(r\log p)|
\]
satisfies
\[
\boxed{
T_{P,K,M}(G)
\ll_\delta
C_G\left[
P^{-\delta}(\log P+1)
+2^{-(1+\delta)K}
+M^{-\delta}(\log M+1)
\right].
}
\]

This bound is uniform on every bounded subset of \(\mathcal D_{\delta,0}\).

## 4. Double-Cutoff Theorem

**Theorem 4.1 (double-cutoff dominated convergence).**  
Let \(G\in\mathcal D_{\delta,0}\).  Let
\[
p_n\to\infty,\qquad K_n\to\infty,\qquad M_n\to\infty.
\]
Then
\[
\sum_{\substack{p\le p_n\\1\le r\le K_n\\p^r\le M_n}}
(\log p)G(r\log p)
\longrightarrow
\sum_p\sum_{r\ge1}(\log p)G(r\log p).
\]
The convergence is locally uniform on bounded subsets of
\(\mathcal D_{\delta,0}\).  The same theorem holds for \(G(-u)\), and hence
for the completed reflected finite-place distribution
\[
\sum_p\sum_{r\ge1}(\log p)
\bigl(G(r\log p)+G(-r\log p)\bigr).
\]

*Proof.*  The summable majorant from Section 2 gives absolute convergence.
For each fixed pair \((p,r)\), the indicator
\[
1_{\{p\le p_n,\ r\le K_n,\ p^r\le M_n\}}
\]
converges to \(1\).  Dominated convergence on the countable index set
\(\{(p,r):p\text{ prime}, r\ge1\}\) gives the limit.

For local uniformity, let \(B\subset\mathcal D_{\delta,0}\) be bounded and set
\[
C_B=\sup_{G\in B}\|G\|_{\delta,0}.
\]
The common majorant
\[
C_B(\log p)p^{-r(1+\delta)}
\]
is summable, and the explicit tail bound in Section 3 tends to zero
independently of \(G\in B\).  \(\square\)

## 5. Interaction With the Occupation Lift

The finite algebraic theorem
`Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md` gives, before CRT
compression,
\[
\operatorname{VM}_{n,K}(G)
=
\sum_{p\le p_n}\sum_{1\le r\le K}
(\log p)G(r\log p).
\]

The present theorem proves that any cofinal cutoff \(p_n,K_n,M_n\to\infty\)
passes this exact finite occupation observable to the full finite-place
prime-power distribution on \(\mathcal D_{\delta,0}\).

Thus the analytic lock is closed:

\[
\boxed{
\text{exact upstairs occupation recovery}
+\mathcal D_{\delta,0}\text{ decay}
\Rightarrow
\text{completed finite-place double cutoff.}
}
\]

