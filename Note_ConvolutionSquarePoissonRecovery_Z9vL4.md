# Note: Convolution-Square Poisson Recovery

Random suffix: `Z9vL4`

Mission: follow the hint "Convolution."

The previous note proved that primorial CRT characters can approximate
Poisson-window *shapes*.  This note strengthens the bridge: the relevant
positive windows are precisely Fourier shadows of convolution squares.  This
aligns the CM Poisson-window test with the classical Weil test class
\(F=f*f^*\).

## 1. The Spectral Window Functional

Let
\[
m_B(z)=-{\Xi'(z)\over\Xi(z)},\qquad
u_B(x,y)=\operatorname{Im}m_B(x+iy).
\]

CM Poisson Monotonicity is
\[
u_B(x,y)\ge0,\qquad x\in{\mathbb R},\; y>0.
\]

The weak form is:
\[
{\mathfrak P}_{\phi,y}(\Xi)
=
\int_{\mathbb R}\phi(x)u_B(x,y)\,dx\ge0
\]
for every nonnegative spectral window \(\phi\ge0\).

The word "spectral" matters.  The variable \(x\) is zero height.  Thus
\(\phi\) is the zero-spectrum weight.  In the Weil explicit-formula language,
zero-spectrum weights arise as Fourier transforms of convolution squares.

## 2. The Convolution-Square Lemma

Use the additive Fourier transform convention
\[
\widehat F(\xi)=\int_{\mathbb R}F(t)e^{-i\xi t}\,dt.
\]

**Lemma 2.1 (positive spectral windows are convolution squares).**  
Let \(\phi\in C_c^\infty({\mathbb R})\), \(\phi\ge0\).  Choose
\[
a(\xi)=\sqrt{\phi(\xi)}
\]
with smooth square root after replacing \(\phi\) by a standard smooth
nonnegative detector such as a Gaussian, or by approximating \(\sqrt\phi\) in
Schwartz norm.  Let \(f=\mathcal F^{-1}a\), and define
\[
F=f*f^*,\qquad f^*(t)=\overline{f(-t)}.
\]

Then
\[
\widehat F(\xi)=\widehat f(\xi)\overline{\widehat f(\xi)}
=
|a(\xi)|^2
=
\phi(\xi).
\]

Therefore
\[
{\mathfrak P}_{\phi,y}(\Xi)
=
\int_{\mathbb R}\widehat{(f*f^*)}(x)u_B(x,y)\,dx.
\]

So the Poisson-window test uses exactly the same autocorrelation shape
\(F=f*f^*\) that appears in Weil positivity.

*Proof.*  This is the Fourier convolution theorem. \(\square\)

## 3. K-Even Detectors

The completed zeta object \(\Xi(z)\) is real-even.  The \(K\)-covariant
detectors are therefore even spectral windows:
\[
\phi(-x)=\phi(x),\qquad \phi(x)\ge0.
\]

For a detector centered at \(x_0>0\), take
\[
\phi_{x_0,\sigma}(x)
=
\exp\!\left(-{(x-x_0)^2\over2\sigma^2}\right)
+
\exp\!\left(-{(x+x_0)^2\over2\sigma^2}\right).
\]

Then \(a=\sqrt{\phi}\) may also be chosen even and real.  The inverse Fourier
representative \(f\) is \(K\)-real:
\[
f^*=f.
\]

Thus the convolution square is compatible with the Bures/K normalization.

## 4. Finite CRT Version

Let \(G_N=\mathbb Z/N\mathbb Z\), \(N=P_n\), with dual
\(\widehat G_N\cong G_N\).  For a nonnegative array
\[
\phi_N(k)\ge0,\qquad k\in\widehat G_N,
\]
define
\[
a_N(k)=\sqrt{\phi_N(k)},\qquad
f_N=\mathcal F_N^{-1}a_N.
\]

Let cyclic autocorrelation be
\[
F_N=f_N*f_N^*,\qquad
f_N^*(r)=\overline{f_N(-r)}.
\]

Then the finite Fourier transform gives the exact identity
\[
\widehat{F_N}(k)=|a_N(k)|^2=\phi_N(k).
\]

This is the finite convolution-square law.  No limiting argument is needed.
The primorial limit enters only when \(\phi_N\) is sampled from a smooth
spectral window and \(N=P_n\to\infty\).

If \(\phi_N\) is \(K\)-even, i.e.
\[
\phi_N(-k)=\phi_N(k),
\]
then \(a_N\) is \(K\)-even and \(F_N\) is \(K\)-real.

## 5. Compatibility With Paper 10/11 Convolution

Paper 10's conductor-flat Fisher expansion has the exact rule
\[
\widehat{h^n}=Q^{1-n}\widehat h^{*n}.
\]

Paper 11 packages the same law into the Hayes-Mobius coefficient vector
\[
\mathsf C_n(h)
=
\sum_{\mathfrak e,\mathfrak f}
\sum_{\eta}
\widehat h^{*n}(\eta)
A_\eta^{\mathfrak f,\mathfrak e}.
\]

Thus the finite information-geometric side is already convolutional.
The Poisson-window side is also convolutional by Lemma 2.1.  The bridge does
not need a new type of object; it needs a proof that the two convolution
structures are the same after:

1. CRT/Ramanujan/Mobius conductor isolation;
2. Hayes-Mobius occupation lift from squarefree axes to prime powers;
3. the Archimedean gamma/K completion;
4. the primorial limit.

## 6. The New Form of the Missing Law

The missing theorem can now be sharpened:

\[
\boxed{
\textbf{Convolution-Square Recovery Theorem.}
}
\]

For every \(K\)-even nonnegative spectral detector \(\phi\), choose finite
CRT samples \(\phi_N\), square roots \(a_N=\sqrt{\phi_N}\), and convolution
squares \(F_N=f_N*f_N^*\).  Then the completed primorial Noether-Weil
recovery should satisfy
\[
\lim_{N=P_n\to\infty}
\mathcal Q_N(\mathscr R_N F_N)
=
{\mathfrak P}_{\phi,y}(\Xi)
=
\int_{\mathbb R}\phi(x)u_B(x,y)\,dx.
\]

Since every \(\mathcal Q_N\) is nonnegative on convolution-square currents,
this would imply
\[
{\mathfrak P}_{\phi,y}(\Xi)\ge0
\]
for every nonnegative \(K\)-even spectral detector.  These detectors separate
negative valleys of \(u_B\).  Therefore CM Poisson Monotonicity follows, and
then RH follows.

## 7. Why This Is Sharper Than the Previous Window Statement

The previous window theorem used arbitrary nonnegative \(\phi\).  One might
worry that Weil positivity only sees autocorrelations \(F=f*f^*\), which is a
smaller class.

Lemma 2.1 removes the worry:

\[
\phi\ge0
\quad\Longleftrightarrow\quad
\phi=\widehat{(f*f^*)}
\]
up to the standard smooth square-root approximation.

So the Poisson-window detectors are not outside the Weil class.  They are the
zero-spectrum side of the Weil class.

## 8. Status

Closed here:

1. nonnegative spectral windows are Fourier transforms of convolution squares;
2. the finite CRT version is exact:
   \[
   \widehat{f_N*f_N^*}=|\widehat f_N|^2=\phi_N;
   \]
3. the construction respects the \(K\)-even Bures symmetry.

Still open:

1. prove the primorial recovery maps preserve this convolution-square
   structure through Hayes-Mobius occupation lift;
2. prove the recovered finite forms converge to the completed CM
   Poisson-window functional with the gamma/K normalization;
3. at natural scale, prove the required primorial character uniformity.

The one small big thing is now visible:

\[
\boxed{
\text{Poisson positivity is Weil autocorrelation positivity viewed from the
zero-spectrum side.}
}
\]

