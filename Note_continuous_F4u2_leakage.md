# Note: Continuous \(K^{CH}\) Leakage for \({\mathbb F}_4[u]/(u^2)\)

**Status:** theory bridge from the moving-score formula to the mixed local
row.  This corrects one tempting but false shortcut: a strictly tame ray does
not leak into the wild packet.

Let

$$
R={\mathbb F}_4[u]/(u^2),
$$

viewed as an additive group of order \(N=16\).  Write additive character
labels as \(a+bu\).  The tame packet is

$$
T=\{bu:b\in{\mathbb F}_4^\times\},
$$

and the wild packet is

$$
W=\{a+bu:a\in{\mathbb F}_4^\times,\ b\in{\mathbb F}_4\}.
$$

For unnormalized additive characters \(\chi_\alpha\), let

$$
p(t)=p_*+tq,\qquad p_*=\frac1N{\bf 1},
$$

and expand \(q=\sum_{\lambda\ne0}a_\lambda\chi_\lambda\).  The exact
continuous cubic coefficient is

$$
\mathcal L_{\alpha,\beta,\gamma}(t)
:=
g_{p(t)}
\left(K^{CH}_{p(t)}(\chi_\alpha)\chi_\beta,\chi_\gamma\right)
=
\sum_{x\in R}
\frac{\chi_{\alpha+\beta+\gamma}(x)}{p(t)_x^2}.
$$

Using

$$
\frac1{p(t)_x^2}
=
N^2\sum_{n\ge0}(n+1)(-Nt)^nq(x)^n
$$

and character multiplication, this becomes the exact Fourier expansion

$$
\mathcal L_{\alpha,\beta,\gamma}(t)
=
N^3\sum_{n\ge0}
(n+1)(-Nt)^n
\bigl(a^{*n}\bigr)_{\alpha+\beta+\gamma},
$$

where \(a^{*0}\) is the delta mass at the trivial character and \(a^{*n}\)
is convolution in the additive character group.

## Pure-Tame No-Leakage Lemma

If \(q\) is supported on the tame subgroup \(T\), then every convolution power
\(a^{*n}\) is supported on \(T\cup\{0\}\).  If
\(\alpha,\beta\in T\) and \(\gamma\in W\), then
\(\alpha+\beta+\gamma\in W\).  Hence

$$
\mathcal L_{\alpha,\beta,\gamma}(t)=0
\qquad
(\alpha,\beta\in T,\ \gamma\in W,\ q\subset T).
$$

So a strictly tame \(m\)-flat ray cannot shear a tame input directly into the
wild packet.  This is the continuous negative control.

## Mixed-Ray First Leakage

Take an elementary mixed displacement

$$
q=s\chi_\tau+r\chi_\omega,
\qquad \tau\in T,\quad \omega\in W.
$$

Then

$$
\bigl(a^{*n}\bigr)_\delta
=
\sum_{m=0}^n
\binom{n}{m}s^{\,n-m}r^m\,
{\bf 1}_{\delta=(n-m)\tau+m\omega},
$$

where character labels are added in the characteristic-two additive group.
For \(\alpha,\beta\in T\), \(\gamma\in W\), the first raw wild leakage occurs
at \(n=1\):

$$
\mathcal L_{\alpha,\beta,\gamma}(t)
=
-2N^4\,t\,r\,
{\bf 1}_{\gamma=\alpha+\beta+\omega}
+O(t^2).
$$

The Paper 11 \(\operatorname{Ext}_{CH}\) diagnostic is sharper than this raw
leakage: it subtracts the pure tame and pure wild axes and applies the
composition defect

$$
K^{CH}(\alpha)K^{CH}(\beta)-K^{CH}(\alpha+\beta).
$$

In that defect, the \(srt\) term cancels by the Codazzi-symmetric first
variation.  The first surviving mixed coefficient is the measured
\(srt^2\) term recorded in the \({\mathbb F}_4[u]/(u^2)\) row.  Thus the
continuous formula and the finite quotient-character computation agree on
the conceptual split:

1. pure tame is closed;
2. raw mixed rays produce wild leakage immediately;
3. the intrinsic \(\operatorname{Ext}_{CH}\) obstruction is the surviving
   mixed composition/carry after pure-axis subtraction.
