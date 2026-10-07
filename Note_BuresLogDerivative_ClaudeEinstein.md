# Note: The Bures Log-Derivative Object

Date: 2026-05-22  
Mission: find the Bures log-derivative object after the scalar ratio failed to
be Herglotz/de Branges.

## Verdict

The correct Bures log-derivative object is the **K-odd-covariant logarithmic
derivative** of the completed transfer ratio:

$$
\boxed{
m_B(z):=
\frac{d}{dz}\log\frac{\mathcal L_3(z)}{\Xi(z)}
-
\frac{d}{dz}\log\mathcal L_3(z)
=
-\frac{\Xi'(z)}{\Xi(z)}.
}
$$

Here

$$
\Xi(z):=\xi\left(\frac12+iz\right),
$$

and

$$
\mathcal L_3(z):=
\Lambda_3\left(\frac12+iz\right),
$$

with

$$
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
$$

and

$$
\Lambda_3(s)=
\left(\frac3\pi\right)^{(s+1)/2}
\Gamma\left(\frac{s+1}{2}\right)L(s,\chi_3).
$$

In words: the ordinary log derivative of the scalar Bures transfer ratio has a
signed divisor. The Bures covariant derivative subtracts the K-odd channel
connection and leaves exactly the zeta divisor.

## Why the Ordinary Log Derivative Is Not the Object

Let

$$
M(z):=\frac{\mathcal L_3(z)}{\Xi(z)}.
$$

Then

$$
\frac{M'(z)}{M(z)}
=
\frac{\mathcal L_3'(z)}{\mathcal L_3(z)}
-
\frac{\Xi'(z)}{\Xi(z)}.
$$

This has two different divisor contributions:

- poles of $M$, i.e. zeros of $\Xi$, with the Herglotz sign;
- zeros of $M$, i.e. zeros of $\mathcal L_3$, with the opposite sign.

So $M'/M$ is not a positive spectral measure for the zeta zeros. It is the
signed divisor of the ratio.

The Bures geometry supplies the missing instruction: the numerator
$\mathcal L_3$ is the K-odd channel/gauge. Its own logarithmic connection must
be subtracted. That gives

$$
\nabla_B\log M
:=
d\log M-d\log\mathcal L_3
=
-d\log\Xi.
$$

Thus

$$
\boxed{m_B(z)=-\Xi'(z)/\Xi(z).}
$$

This is the Bures-covariant transfer log derivative.

## Divisor Formula

The completed xi function in spectral coordinates is real entire and even:

$$
\Xi^\#=\Xi,\qquad \Xi(-z)=\Xi(z),
\qquad F^\#(z):=\overline{F(\overline z)}.
$$

If RH holds, its zeros are real and occur in pairs $\pm\gamma_n$. The canonical
Hadamard product gives

$$
\Xi(z)=\Xi(0)\prod_{n\ge1}\left(1-\frac{z^2}{\gamma_n^2}\right)
$$

with multiplicity. Therefore

$$
\boxed{
m_B(z)
=-\frac{\Xi'(z)}{\Xi(z)}
=
\sum_{n\ge1} m_n\,\frac{2z}{\gamma_n^2-z^2}
}
$$

where $m_n$ is the multiplicity of the zero at $\pm\gamma_n$.

Equivalently,

$$
m_B(z)=
\sum_{\gamma\in\Gamma}
\frac{m_\gamma}{\gamma-z}
$$

with the symmetric zeta-zero spectrum

$$
\Gamma=\{\ldots,-\gamma_2,-\gamma_1,\gamma_1,\gamma_2,\ldots\}.
$$

This is the exact Herglotz/Stieltjes pole expansion of the zeta-zero spectral
measure.

## Theorem: \(m_B\) Is Herglotz If and Only If RH Holds

**Claim.**

$$
\boxed{
m_B(z)=-\Xi'(z)/\Xi(z)
\text{ is Herglotz on }\mathbb C_+
\iff
\text{RH}.
}
$$

Here Herglotz means analytic on $\mathbb C_+$ and

$$
\operatorname{Im}m_B(z)\ge0
\qquad(z\in\mathbb C_+).
$$

**Proof: RH implies Herglotz.**

Assume RH. Then all zeros of $\Xi$ are real. For a real zero $\gamma$,

$$
\operatorname{Im}\frac1{\gamma-z}
=
\frac{\operatorname{Im}z}{(\operatorname{Re}z-\gamma)^2+(\operatorname{Im}z)^2}
>0
\qquad (z\in\mathbb C_+).
$$

The symmetric product gives the locally uniformly convergent sum

$$
m_B(z)=\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z},
$$

or, pairing $\pm\gamma_n$,

$$
m_B(z)=\sum_{n\ge1}m_n\frac{2z}{\gamma_n^2-z^2}.
$$

The convergence follows from

$$
\sum_n\gamma_n^{-2}<\infty,
$$

which is a direct consequence of Riemann-von Mangoldt counting. Hence
$m_B$ is a locally uniform limit of Herglotz functions and is Herglotz.

**Proof: Herglotz implies RH.**

If RH fails, then $\zeta$ has a zero

$$
\rho=\beta+i\gamma,\qquad \beta\ne\frac12.
$$

In the spectral coordinate $s=1/2+iz$, this gives a zero of $\Xi$ at

$$
z_\rho=\gamma-i\left(\beta-\frac12\right).
$$

By the functional equation, the reflected zero

$$
1-\rho=1-\beta+i\gamma
$$

gives the spectral point

$$
z_{1-\rho}=\gamma+i\left(\beta-\frac12\right).
$$

One of these two points lies in $\mathbb C_+$. Thus $m_B=-\Xi'/\Xi$ has a pole
inside $\mathbb C_+$. A Herglotz function must be analytic in $\mathbb C_+$.
Contradiction. Therefore all zeros of $\Xi$ are real, which is RH. $\square$

## What This Means for the RH Mission

This is the object the previous scalar ratio was trying to reveal:

$$
\boxed{
m_B(z)=-\frac{d}{dz}\log\Xi(z).
}
$$

It is not a proof of RH by itself. Instead, it gives the exact equivalent
operator-theoretic target:

> Prove the Bures-covariant log derivative $m_B$ is Herglotz.

That statement is equivalent to RH.

The advantage of the Bures derivation is conceptual and tactical:

1. The `Z/6` Hurwitz decomposition shows that the Bures transfer ratio has a
   K-odd numerator and a zeta denominator.
2. The failed scalar Herglotz test showed that the raw quotient is too
   reversible.
3. The covariant log derivative subtracts the K-odd numerator connection and
   isolates the positive spectral divisor.

Thus the Bures lift does not replace $\xi$; it explains why the right
Hilbert-Polya Weyl object is the covariant logarithmic derivative of $\xi$.

## Local Numerical Probe

The companion script is:

```powershell
python empirical\probe_BuresLogDerivative_mN4pR.py
```

It checks:

- the identity

  $$
  d\log(\mathcal L_3/\Xi)-d\log\mathcal L_3=-d\log\Xi;
  $$

- the sampled Herglotz sign $\operatorname{Im}m_B(z)>0$ in the upper
  half-plane;
- the signed-divisor behavior of the ordinary transfer log derivative
  $M'/M$;
- the growth of the pole term near the first zeta-zero ordinate.

The script is a diagnostic, not the proof. The theorem above is the structural
classification.
