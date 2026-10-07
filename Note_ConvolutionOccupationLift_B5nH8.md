# Note: Convolution Occupation Lift and the Von Mangoldt Weight

Random suffix: `B5nH8`

Mission: make the "Convolution" hint algebraically explicit.

The previous note showed that Poisson-window detectors are Fourier shadows of
convolution squares.  This note proves the next convolution law: repeated
convolution along one prime axis is exactly the prime-power occupation lift,
and the logarithmic cumulant coefficient produces the von Mangoldt weight.

## 1. The Free Prime-Axis Convolution Algebra

Fix the finite prime set
\[
{\mathcal P}_n=\{p\le p_n\}.
\]

Let
\[
{\mathcal A}_n
=
{\mathbb C}[\mathbb N^{{\mathcal P}_n}]
\]
be the free commutative convolution algebra with basis vectors
\[
e_\alpha,\qquad
\alpha=(\alpha_p)_{p\in{\mathcal P}_n}\in\mathbb N^{{\mathcal P}_n},
\]
and product
\[
e_\alpha*e_\beta=e_{\alpha+\beta}.
\]

The single-prime axes are \(e_p:=e_{\mathbf 1_p}\).  An occupation
\[
r e_p
\]
means "the prime axis \(p\) occupied \(r\) times," i.e. the integer \(p^r\).

Define the single-axis projector
\[
\Pi_{\rm sa}e_\alpha
=
\begin{cases}
e_\alpha,& \#\{p:\alpha_p\ne0\}=1,\\
0,& \text{otherwise}.
\end{cases}
\]

This is the formal version of the primitive/von-Mangoldt support projector:
it keeps prime powers and kills integers with two or more distinct prime
factors.

## 2. The Logarithmic Convolution Series

For complex \(s\) with \(\operatorname{Re}s>1\), define
\[
H_s=\sum_{p\in{\mathcal P}_n}p^{-s}e_p.
\]

The formal logarithmic Euler object is
\[
{\mathcal L}_{n}(s)
=
\sum_{m\ge1}{1\over m}H_s^{*m}
=
-\log(1-H_s).
\]

Expanding the \(m\)-fold convolution,
\[
H_s^{*m}
=
\sum_{p_1,\ldots,p_m\in{\mathcal P}_n}
(p_1\cdots p_m)^{-s}
e_{p_1+\cdots+p_m}.
\]

The single-axis projector keeps only the tuples where all \(p_i\) are equal:
\[
\Pi_{\rm sa}H_s^{*m}
=
\sum_{p\in{\mathcal P}_n}p^{-ms}e_{m e_p}.
\]

Therefore
\[
\Pi_{\rm sa}{\mathcal L}_n(s)
=
\sum_{p\in{\mathcal P}_n}
\sum_{r\ge1}
{1\over r}p^{-rs}e_{r e_p}.
\]

## 3. The Von Mangoldt Weight Appears

Apply the logarithmic derivative
\[
D_s=-{\partial\over\partial s}.
\]

Then
\[
D_s\left({1\over r}p^{-rs}\right)
=
{1\over r}\,(r\log p)\,p^{-rs}
=
(\log p)p^{-rs}.
\]

The \(1/r\) from the logarithm and the \(r\) from the derivative cancel.
Thus
\[
\boxed{
D_s\Pi_{\rm sa}{\mathcal L}_n(s)
=
\sum_{p\in{\mathcal P}_n}
\sum_{r\ge1}
(\log p)p^{-rs}e_{r e_p}.
}
\]

Under the map
\[
e_{r e_p}\longmapsto p^r,
\]
this is exactly
\[
\sum_{p\le p_n}\sum_{r\ge1}\Lambda(p^r)(p^r)^{-s},
\qquad
\Lambda(p^r)=\log p.
\]

So the von Mangoldt distribution is the differentiated, single-axis part of
the logarithmic convolution series.

## 4. Interpretation for the Primorial Program

This proves the formal occupation-lift law in the free prime-axis algebra:

\[
\boxed{
\text{squarefree prime axes}
\xrightarrow{\text{convolution powers}}
\text{prime-power occupations}
\xrightarrow{-\partial_s\log}
\text{von Mangoldt weights}.
}
\]

The finite CRT row \(P_n\) supplies the squarefree axes.  The all-order
cumulant/convolution tower supplies the repeated occupations.  The closed
single-axis projector supplies the primitive/von-Mangoldt support.  The
logarithmic cumulant coefficient \(1/r\) supplies exactly the factor needed
for \(-\partial_s\) to produce \(\log p\).

This is the clean algebraic heart of Paper 22 Lemma 8.1a.

## 5. What Is Closed and What Remains

Closed here:

1. repeated convolution of a single prime axis is prime-power occupation;
2. the logarithmic coefficient \(1/r\) is forced by the Euler log;
3. the derivative \(-\partial_s\) turns \(p^{-rs}/r\) into
   \((\log p)p^{-rs}\);
4. the single-axis projector kills mixed-prime occupations, matching
   support of \(\Lambda(n)\).

Still open in the finite primorial Noether system:

1. prove that the Hayes-Mobius current realizes this free occupation algebra
   after CRT/Ramanujan/Mobius conductor isolation;
2. prove leakage/projection kills the mixed-axis terms in the actual finite
   critical leaf;
3. prove the cutoff and character-uniformity estimates that let
   \(n,K,M\to\infty\);
4. attach the Archimedean gamma/K completion.

## 6. The New Compact Law

The missing arithmetic recovery law can now be written in one line:

\[
\boxed{
\operatorname{VM}
=
-\partial_s\,\Pi_{\rm sa}\log(1-H_s)^{-1}.
}
\]

This is the convolutional origin of the von Mangoldt side of the completed
explicit formula.  Once the finite primorial Noether recovery maps are shown
to implement this identity, the Poisson-window convolution-square bridge has
the arithmetic weights it needs.

