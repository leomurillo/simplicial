# Note: The Completed Bures Transfer Ratio Is Not Herglotz/de Branges

Date: 2026-05-22  
Mission: classify the completed `L(s,chi3)/zeta(s)` Bures transfer ratio.

## Verdict

The natural completed K-normalized Bures transfer ratio built from

$$
\frac{L(s,\chi_3)}{\zeta(s)}
$$

is **not** Herglotz in the spectral upper half-plane. Consequently, the
associated two-function de Branges candidate is **not** Hermite-Biehler.

This is not a numerical failure. It is a short structural obstruction: after
the correct gamma/conductor/K normalization, the ratio is too symmetric. It is
K-real at interior points of the upper half-plane, whereas a nonconstant
Herglotz function cannot have real values inside the upper half-plane.

## Correct Completed Normalization

Use the spectral coordinate

$$
s=\frac12+iz,\qquad z\in\mathbb C.
$$

The zeta denominator should be the entire completed xi function

$$
\xi(s):=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
$$

and the primitive odd quadratic character modulo 3 should be completed as

$$
\Lambda_3(s):=
\left(\frac{3}{\pi}\right)^{(s+1)/2}
\Gamma\left(\frac{s+1}{2}\right)L(s,\chi_3).
$$

Here $\chi_3(1)=1$, $\chi_3(2)=-1$, and $\chi_3(-1)=-1$. Its Gauss sum is
$i\sqrt3$, so the root number is

$$
\varepsilon(\chi_3)=\frac{\tau(\chi_3)}{i\sqrt3}=1.
$$

Thus both completed functions are self-dual:

$$
\xi(s)=\xi(1-s),\qquad \Lambda_3(s)=\Lambda_3(1-s).
$$

Define the two real-entire spectral functions

$$
\Xi(z):=\xi\!\left(\frac12+iz\right),
\qquad
\mathcal L_3(z):=\Lambda_3\!\left(\frac12+iz\right).
$$

They satisfy

$$
\Xi^\#=\Xi,\qquad \mathcal L_3^\#=\mathcal L_3,
\qquad
F^\#(z):=\overline{F(\overline z)}.
$$

The completed scalar Bures transfer ratio is therefore

$$
\boxed{
M(z):=\frac{\mathcal L_3(z)}{\Xi(z)}
=
\frac{\Lambda_3(1/2+iz)}{\xi(1/2+iz)}.
}
$$

This is the K-normalized ratio: it is real-meromorphic on the spectral real
axis and carries the functional-equation symmetry correctly.

## Theorem 1: \(M\) Is Not Herglotz

**Claim.** No K-preserving real normalization of $M$ is a nonconstant Herglotz
function on the spectral upper half-plane $\mathbb C_+:=\{z:\operatorname{Im}z>0\}$.

Here "K-preserving real normalization" means $M$ itself or any real Mobius
transform

$$
M_{a,b,c,d}(z):=\frac{aM(z)+b}{cM(z)+d},
\qquad a,b,c,d\in\mathbb R,\quad ad-bc\ne0,
$$

on its domain of analyticity. These are exactly the scalar changes of real
basis compatible with the boundary reality required in de Branges theory.

**Proof.**

Take a point on the interior imaginary axis,

$$
z=iy,\qquad y>0.
$$

Then

$$
s=\frac12+i(iy)=\frac12-y\in\mathbb R.
$$

For real $s$, both $\xi(s)$ and $\Lambda_3(s)$ are real. Therefore

$$
M(iy)\in\mathbb R
$$

whenever $\Xi(iy)\ne0$.

For example $0<y<1/2$ gives $s\in(0,1/2)$, where $\xi(s)\ne0$, so such
interior points certainly exist.

If $M$ were Herglotz, then

$$
u(z):=\operatorname{Im}M(z)
$$

would be a nonnegative harmonic function on $\mathbb C_+$. But

$$
u(iy)=0
$$

at an interior point. By the strong minimum principle, $u\equiv0$ throughout
the connected domain. Then $M$ is real-valued on an open domain, hence constant
by the open mapping theorem. But $M$ is not constant; for instance, as real
$s\to+\infty$, the gamma/conductor quotient gives

$$
\frac{\Lambda_3(s)}{\xi(s)}
\sim
2\sqrt{\frac{3}{\pi}}\,
\frac{3^{s/2}\Gamma((s+1)/2)}
{s(s-1)\Gamma(s/2)}
\sim
C\,3^{s/2}s^{-3/2},
$$

whereas it is finite at $s=0$.

Thus $M$ is not Herglotz.

The same argument applies to every real Mobius transform of $M$: a real Mobius
transform sends real values to real values. Unless the transform has a pole at
the chosen point, it again has an interior real value; choosing another
$y\in(0,1/2)$ avoids any single exceptional point. Therefore no K-preserving
real scalar normalization of $M$ is Herglotz. $\square$

## Theorem 2: The Associated de Branges Candidate Fails

The natural Hermite-Biehler candidate from the pair $(\Xi,\mathcal L_3)$ is

$$
E(z):=\Xi(z)-i\mathcal L_3(z),
$$

with

$$
E^\#(z)=\Xi(z)+i\mathcal L_3(z).
$$

**Claim.** $E$ is not Hermite-Biehler; hence it does not generate a de Branges
space whose canonical Weyl ratio is the Bures transfer ratio.

**Proof.**

Hermite-Biehler requires the strict inequality

$$
|E^\#(z)|<|E(z)|\qquad (z\in\mathbb C_+)
$$

up to the opposite convention depending on the sign choice.

But at $z=iy$, $y>0$, both $\Xi(iy)$ and $\mathcal L_3(iy)$ are real. Hence

$$
|E(iy)|^2
=|\Xi(iy)-i\mathcal L_3(iy)|^2
=\Xi(iy)^2+\mathcal L_3(iy)^2,
$$

and

$$
|E^\#(iy)|^2
=|\Xi(iy)+i\mathcal L_3(iy)|^2
=\Xi(iy)^2+\mathcal L_3(iy)^2.
$$

Therefore

$$
|E(iy)|=|E^\#(iy)|
$$

at interior points of $\mathbb C_+$. The Hermite-Biehler inequality is strict
inside $\mathbb C_+$, so $E$ is not Hermite-Biehler.

The same obstruction applies to every real change of basis

$$
A=\alpha\Xi+\beta\mathcal L_3,\qquad
B=\gamma\Xi+\delta\mathcal L_3,
\qquad
\alpha\delta-\beta\gamma\ne0,
$$

because $A(iy),B(iy)\in\mathbb R$, and hence

$$
|A(iy)-iB(iy)|=|A(iy)+iB(iy)|.
$$

So no real K-preserving de Branges normalization of this two-function pair can
work. $\square$

## Numerical Witnesses

The companion script

```powershell
python empirical\probe_BuresTransfer_Herglotz_deBranges_a9Q7x.py
```

prints:

- `M(iy)` has imaginary part zero for several interior upper-half-plane points.
- `Im M(z)` takes both signs in the upper half-plane.
- The Hermite-Biehler delta

$$
|E(z)|^2-|E^\#(z)|^2
$$

is zero on the interior imaginary axis and changes sign elsewhere.

These computations are diagnostic only; the proof above is structural.

## Implication for RH Mission

This closes the specific Herglotz/de Branges attempt **negatively**:

$$
\boxed{
\frac{\Lambda_3(1/2+iz)}{\xi(1/2+iz)}
\text{ is not the Weyl/Herglotz function of the desired self-adjoint system.}
}
$$

The reason is instructive. The completed ratio has the right K-reality on the
spectral boundary, but it also has K-reality on the interior imaginary axis.
Herglotz/de Branges theory needs a dissipative orientation in $\mathbb C_+$;
the scalar ratio alone is too reversible.

The next viable operator-theoretic object should therefore not be the raw
ratio $L(s,\chi_3)/\zeta(s)$. Two nearby alternatives remain natural:

1. **A logarithmic derivative / spectral measure object**

   $$
   -\frac{d}{dz}\log\frac{\Xi(z)}{\mathcal L_3(z)}
   $$

   or a regularized variant. Logarithmic derivatives can be Herglotz/Stieltjes
   when zeros interlace or lie on the real spectral axis.

2. **A genuinely two-channel canonical system**

   using the vector packet

   $$
   F(s)=\zeta(s)E(s)+L(s,\chi_3)O(s)
   $$

   rather than the scalar quotient. The scalar quotient erases the symplectic
   orientation that a Weyl function needs.

So the mission does not die; it becomes more precise. The scalar completed
Bures transfer ratio is not the Hilbert-Polya Weyl function. The next object to
test is the Bures **log-derivative** or a two-channel canonical system retaining
both the K-even and K-odd packets.
