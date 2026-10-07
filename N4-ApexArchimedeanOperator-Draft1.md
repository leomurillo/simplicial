# N4 — The Apex Operator and the Archimedean Place

**Leonardo Murillo Montero**

*June 5, 2026*

<!--
Program record (not part of the paper). Fourth paper of the Numbers (N-)
series; sequel to N3 (spectral concentration), which isolated the edge operator
of §6 but left it unidentified. Every quantitative claim is certified by the
deterministic computation
  empirical/probe_apex_archimedean_identification.py
(numpy + mpmath, no torch): the Mellin symbol (rel.err <= 5e-14 vs rotated-
contour quadrature), the reflection-product / Euler identity (<= 3e-41), the
parity-duplication lemma (<= 2e-41), and the finite U_N reproduction of the N3
concentration table. Cross-stream: the even sector matches the Hardy-Titchmarsh
intertwining of [PII, Thm 7.1]; the finite no-crossing positivity is the
discrete avatar of the de Branges phase clock of [PIII]; this exhibits the
explicit archimedean operator whose absence is noted in [T20].
-->

---

## Abstract

The companion paper [N3] showed that the eigenvalues of the apex unitary $U_N$ concentrate at the four fourth roots of unity, reducing the phenomenon to a single estimate on one edge mode, and exhibited — as the $N\to\infty$ low-frequency scaling limit of $U_N$ — an explicit integral operator $\mathcal U=(A-I)\Phi$ on $L^2[0,\infty)$, the Hardy averaging operator minus the identity composed with the half-line Fourier transform. That operator was left unidentified. We identify it. Its kernel depends only on the product of its arguments, so $\mathcal U$ is a *product-kernel* operator and acts on the Mellin transform as a multiplier composed with the reflection $s\mapsto1-s$ — the structural form of the archimedean scattering operator. We compute the multiplier in closed form,
$$\widetilde k(s)=\underbrace{\frac{s}{1-s}}_{\text{Hardy–Blaschke}}\cdot\underbrace{(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)}_{\text{archimedean }\Gamma\text{-factor}},$$
a Blaschke factor (zero at $s=0$, pole at $s=1$ — the trivial-zero and pole loci of $\zeta$) times the local $\Gamma$-factor of the additive character. In the reflection product that governs the eigenvalues the Blaschke factor cancels its mirror, leaving exactly **Euler's reflection formula**, $\widetilde k(s)\widetilde k(1-s)=i/(2\sin\pi s)=i\,\Gamma(s)\Gamma(1-s)/2\pi$; on the critical line the eigenvalue scale is $e^{i\pi/4}/\sqrt{2\cosh\pi t}$, so its argument is **exactly an eighth of a turn** — the cluster gap-centre that [N3] found as the no-crossing threshold is the phase of $\sqrt i$ supplied by the reflection formula, not a free geometric constant. A parity (duplication) lemma shows the even sector of $\mathcal U$ has Mellin symbol $\tfrac12\,\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(1-s)$, equal on the critical line to the Riemann–Siegel multiplier $\gamma(t)$ of the Hardy–Titchmarsh intertwining $\mathcal V\widehat{\mathcal F}\mathcal V^{-1}=\gamma(s)R$ of [PII, Thm 7.1]; the apex edge operator *is* the archimedean operator, times the Hardy–Blaschke factor that is the apex's own contribution. Consequently the apex unitary $U_N$ is an explicit finite model of the archimedean place, and the [N3] no-crossing reduction becomes a spectral-gap statement: the single edge eigenvalue lies strictly below the archimedean threshold $\tfrac18$ — the discrete, finite avatar of the de Branges phase-clock positivity of [PIII]. All identities are theorem-grade; the residual estimate $\delta_\infty<\tfrac18$ is reframed, exactly, as a bound on the top eigenvalue of an explicit bounded operator.

---

## 1. Introduction

The Numbers series studies the apex unitary $U_N\in U(N-1)$, the change of basis between the Helmert and character frames of the mean-zero hyperplane of $\mathbb C^N$: [N1] sets up its arithmetic, [N2] proves $\det U_N=i^{-\binom{N-1}{2}}$, and [N3] proves that its spectrum concentrates at $\{1,i,-1,-i\}$ and reduces the concentration to one *edge mode*. In the course of that reduction, [N3, §6] rescaled the matrix entries ($k=\sqrt N\,u$, $c=\sqrt N\,v$) and obtained the continuum limit
$$\sqrt N\,(U_N)_{kc}\longrightarrow K(u,v)=\frac{e^{2\pi i uv}-1}{2\pi i\,uv}-e^{2\pi i uv},\qquad (\mathcal U\psi)(u)=\int_0^\infty K(u,v)\psi(v)\,dv,$$
and factored the limiting operator as
$$\mathcal U=(A-I)\,\Phi,\qquad (\Phi\psi)(u)=\int_0^\infty e^{2\pi iuv}\psi(v)\,dv,\quad (Ag)(u)=\frac1u\int_0^u g(t)\,dt,$$
the half-line Fourier transform $\Phi$ composed with the Hardy averaging operator $A$ minus the identity. [N3] observed that the leading eigenvalue of $\mathcal U$ controls the entire spectral concentration, that its displacement converges to $\delta_\infty\approx0.097<\tfrac18$, and that no closed form was available.

This paper identifies $\mathcal U$ as an *archimedean operator*. The point of entry is a structural observation that [N3] did not use: the kernel $K(u,v)=k(uv)$ depends only on the product $uv$,
$$k(w)=\frac{e^{2\pi iw}-1}{2\pi i w}-e^{2\pi iw}.\tag{1.1}$$
Operators with product kernels are exactly those diagonalized by the Mellin transform up to the reflection $s\mapsto1-s$; they are the natural home of the functional equation. Carrying this through gives the closed form of the symbol (Theorem 3.1), its factorization into a Hardy–Blaschke factor and the archimedean $\Gamma$-factor, the Euler-reflection identity that fixes the eigenvalue scale and *derives* the threshold $\tfrac18$ (Theorem 4.2), and the identification of the even sector with the archimedean scattering operator of the right-carrier paper [PII] (Theorem 5.2). Section 6 reframes the residual [N3] estimate as a spectral gap and places it against the de Branges clock of [PIII] and the operator question of [T20].

We work throughout on $L^2[0,\infty)$. The Mellin transform is $\widetilde\psi(s)=\int_0^\infty\psi(u)u^{s-1}\,du$, an isometry $L^2[0,\infty)\to L^2(\tfrac12+i\mathbb R)$; $\Gamma_{\mathbb R}(s):=\pi^{-s/2}\Gamma(s/2)$ is the real local factor; $\omega=e^{2\pi i/N}$.

---

## 2. The edge operator is a product-kernel operator

**Proposition 2.1.** *The edge kernel of [N3, §6] depends only on the product $uv$: $K(u,v)=k(uv)$ with $k$ as in $(1.1)$. Equivalently, $\mathcal U=(A-I)\Phi$ has the product-kernel form $(\mathcal U\psi)(u)=\int_0^\infty k(uv)\psi(v)\,dv$.*

*Proof.* With $g=\Phi\psi$, $(Ag)(u)=\tfrac1u\int_0^u\!\int_0^\infty e^{2\pi itv}\psi(v)\,dv\,dt=\int_0^\infty\big[\tfrac1u\int_0^u e^{2\pi itv}\,dt\big]\psi(v)\,dv=\int_0^\infty\tfrac{e^{2\pi iuv}-1}{2\pi iuv}\psi(v)\,dv$, while $(I\Phi\psi)(u)=\int_0^\infty e^{2\pi iuv}\psi(v)\,dv$. Subtracting gives the kernel $(1.1)$ evaluated at $w=uv$. $\square$

The relevance is the following standard computation, which we record as a lemma because the reflection it produces is the whole point.

**Lemma 2.2 (Mellin action of a product kernel).** *Let $(T\psi)(u)=\int_0^\infty k(uv)\psi(v)\,dv$ and let $\widetilde k(s)=\int_0^\infty k(w)w^{s-1}\,dw$ converge on a strip $\sigma_-<\operatorname{Re}s<\sigma_+$. Then on that strip*
$$\widetilde{(T\psi)}(s)=\widetilde k(s)\,\widetilde\psi(1-s).$$
*That is, $T$ acts on the Mellin side as multiplication by $\widetilde k$ followed by the reflection $R:\ \widetilde\psi(s)\mapsto\widetilde\psi(1-s)$: $\ \widetilde T=M_{\widetilde k}\,R$.*

*Proof.* $\int_0^\infty(T\psi)(u)u^{s-1}\,du=\int_0^\infty\!\int_0^\infty k(uv)\psi(v)u^{s-1}\,dv\,du$. Substitute $w=uv$ at fixed $v$ ($u=w/v$, $du=dw/v$): $=\int_0^\infty\psi(v)\big[\int_0^\infty k(w)(w/v)^{s-1}\,dw/v\big]dv=\int_0^\infty\psi(v)v^{-s}\,dv\cdot\int_0^\infty k(w)w^{s-1}\,dw=\widetilde\psi(1-s)\widetilde k(s)$. $\square$

Lemma 2.2 already places $\mathcal U$ in the same operator class as the archimedean intertwiner $\mathcal V\widehat{\mathcal F}\mathcal V^{-1}=\gamma(s)R$ of [PII, Thm 7.1]: a Mellin multiplier composed with the reflection $s\mapsto1-s$. The remaining content is the explicit multiplier $\widetilde k(s)$.

---

## 3. The Mellin symbol

**Theorem 3.1 (symbol).** *On the critical strip $0<\operatorname{Re}s<1$ the Mellin symbol of the edge kernel $(1.1)$ is*
$$\boxed{\ \widetilde k(s)=(2\pi)^{-s}\,e^{i\pi s/2}\,\Gamma(s)\cdot\frac{s}{1-s}\ }\tag{3.1}$$
*and it factors as $\widetilde k(s)=g(s)\cdot\dfrac{s}{1-s}$, where $g(s)=(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$ is the Mellin transform of the additive-character kernel $e^{2\pi iw}$, and $\dfrac{s}{1-s}$ is the Mellin symbol of $A-I$.*

*Proof.* Write $k=f_1+f_2$ with $f_1(w)=(e^{2\pi iw}-1)/(2\pi iw)$ and $f_2(w)=-e^{2\pi iw}$. Near $0$, $f_1\to1$ and near $\infty$, $f_1=-\tfrac1{2\pi iw}+O(w^{-1}e^{2\pi iw})$, so $\widetilde f_1$ converges for $0<\operatorname{Re}s<1$; $\widetilde f_2$ converges there conditionally. Use the two evaluations, valid for $0<\operatorname{Re}s<1$ and $\operatorname{Re}p>0$ continued to $p=-2\pi i=2\pi e^{-i\pi/2}$:
$$\int_0^\infty(e^{-pw}-1)\,w^{s-2}\,dw=\Gamma(s-1)\,p^{1-s},\qquad \int_0^\infty e^{-pw}\,w^{s-1}\,dw=\Gamma(s)\,p^{-s}.$$
With $p^{-s}=(2\pi)^{-s}e^{i\pi s/2}$ and $p^{1-s}=(2\pi)^{1-s}e^{-i\pi(1-s)/2}$,
$$\widetilde f_1(s)=\frac1{2\pi i}\,\Gamma(s-1)\,(2\pi)^{1-s}e^{-i\pi(1-s)/2}=-(2\pi)^{-s}e^{i\pi s/2}\,\frac{\Gamma(s)}{s-1},\qquad \widetilde f_2(s)=-(2\pi)^{-s}e^{i\pi s/2}\Gamma(s),$$
the first after simplifying $\tfrac1{2\pi i}(2\pi)^{1-s}=-i(2\pi)^{-s}$, $e^{-i\pi(1-s)/2}=-i\,e^{i\pi s/2}$, and $\Gamma(s-1)=\Gamma(s)/(s-1)$. Summing,
$$\widetilde k(s)=-(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)\Big(\tfrac1{s-1}+1\Big)=-(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)\,\frac{s}{s-1}=(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)\,\frac{s}{1-s},$$
which is $(3.1)$. The factor $g(s)=(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$ is $\int_0^\infty e^{2\pi iw}w^{s-1}\,dw$. Finally $A-I$: the Hardy operator has Mellin symbol $\tfrac1{1-s}$ (by Lemma 2.2's computation applied to $A$, whose averaging kernel gives $\int_t^\infty u^{s-2}\,du=t^{s-1}/(1-s)$), so $A-I$ has symbol $\tfrac1{1-s}-1=\tfrac{s}{1-s}$. $\square$

The closed form $(3.1)$ agrees with direct rotated-contour quadrature of $\widetilde k(s)$ to relative error $\le5\times10^{-14}$ across the strip (program record). The two factors carry disjoint content: $g(s)$ is the archimedean local factor of the standard additive character — the half-line Fourier transform $\Phi$ — and $s/(1-s)$ is a *Blaschke factor* with a single zero at $s=0$ and a single pole at $s=1$, precisely the trivial-zero seed and the pole of $\zeta$. The Blaschke factor is the apex's own contribution, supplied by the Helmert averaging $A$; the bare Fourier transform carries only $g$.

---

## 4. The reflection product and Euler's formula

By Lemma 2.2 the operator is $\widetilde{\mathcal U}=M_{\widetilde k}R$. On the reflection-paired two-dimensional space spanned by the Mellin modes at $s$ and $1-s$, this is the off-diagonal matrix $\left(\begin{smallmatrix}0&\widetilde k(s)\\ \widetilde k(1-s)&0\end{smallmatrix}\right)$, whose eigenvalues are $\pm\sqrt{\widetilde k(s)\widetilde k(1-s)}$. The product that fixes the eigenvalue scale is therefore $\widetilde k(s)\widetilde k(1-s)$, and in it the Blaschke factor cancels its own reflection.

**Theorem 4.1 (reflection product = Euler reflection).** *For all $s$,*
$$\widetilde k(s)\,\widetilde k(1-s)=g(s)\,g(1-s)=\frac{i}{2\sin\pi s}=\frac{i\,\Gamma(s)\Gamma(1-s)}{2\pi}.$$

*Proof.* From $(3.1)$, $\widetilde k(s)\widetilde k(1-s)=g(s)g(1-s)\cdot\dfrac{s}{1-s}\cdot\dfrac{1-s}{s}=g(s)g(1-s)$. Then
$$g(s)g(1-s)=(2\pi)^{-1}e^{i\pi(s+1-s)/2}\Gamma(s)\Gamma(1-s)=\frac{e^{i\pi/2}}{2\pi}\,\Gamma(s)\Gamma(1-s)=\frac{i}{2\pi}\cdot\frac{\pi}{\sin\pi s}=\frac{i}{2\sin\pi s},$$
using $e^{i\pi/2}=i$ and Euler's reflection formula $\Gamma(s)\Gamma(1-s)=\pi/\sin\pi s$. $\square$

Theorem 4.1 is the structural heart of the identification: the archimedean content of the apex edge operator is *Euler's reflection formula*, with the single quarter-turn $i=e^{i\pi/2}$ in front. The phase of that $i$ is what sets the cluster geometry of [N3].

**Theorem 4.2 (the threshold $\tfrac18$ is the reflection phase).** *On the critical line $s=\tfrac12+it$ the eigenvalue scale is*
$$\lambda(t)=\pm\sqrt{\widetilde k(\tfrac12+it)\,\widetilde k(\tfrac12-it)}=\pm\frac{e^{i\pi/4}}{\sqrt{2\cosh\pi t}},$$
*so $\arg\lambda(t)\equiv\tfrac\pi4$ is constant. In turns this is exactly $\tfrac18$ — the midpoint between adjacent fourth roots of unity, i.e. the cluster gap-centre that defines the no-crossing threshold of [N3, Thm 1.2].*

*Proof.* On the line $\sin\pi s=\sin(\tfrac\pi2+i\pi t)=\cos(i\pi t)=\cosh\pi t$, so by Theorem 4.1 $\lambda^2=i/(2\cosh\pi t)$ and $\lambda=\pm e^{i\pi/4}/\sqrt{2\cosh\pi t}$. The argument $\pi/4$ rad $=\tfrac18$ turn. $\square$

Thus the constant $\tfrac18$ that appears in [N3] as a *geometric* gap half-width is, intrinsically, the phase of $\sqrt i$ — the square root of the quarter turn produced by Euler's reflection formula. The modulus $1/\sqrt{2\cosh\pi t}$ decays away from $t=0$, the hallmark of a scattering (continuous) family: the reflection-paired modes accumulate at the gap-centre phase $\tfrac18$ with vanishing weight. The actual *clusters* of $U_N$ are produced by the discrete edge mode, addressed next.

**Remark 4.3 (the threshold is a finite cyclotomic landmark: $\sqrt i$ absorbs into the prime-2 metric).** *The constant phase of Theorem 4.2 is $\sqrt i=\zeta_8=e^{i\pi/4}=(1+i)/\sqrt2$, the bisector of the fourth-roots cluster $\{1,i,-1,-i\}$ at which the eigenvalues concentrate ([N3]). Since $\det U_N=i^{-\binom{N-1}2}$ is a power of $\zeta_4=i$ ([N2]), $\sqrt i$ is the square root of the determinant's quarter-turn unit; its only surd is the prime-$2$ normalizer $\sqrt2=\sqrt{1\cdot2}$, the first Helmert rung and the first prime at which the radical ladder grows ([T4]).* This surd is **absorbable**. In $\mathbb Z[\zeta_8]$, with $\zeta_8$ carried by the companion matrix $C$ of $\Phi_8(x)=x^4+1$, multiplication by $\sqrt i=\zeta_8$ is the exact **integer orthogonal** matrix $C$ (with $C^2=$ "$i$", $C^4=-I$, $C^8=I$, $C^{\mathsf T}C=I$); the surd $\sqrt2=\zeta_8+\zeta_8^{-1}=C+C^7$ is the exact integer matrix with $(C+C^7)^2=2I$; and the cyclotomic trace form is the integer metric $M=4I$, under which $C$ is an isometry. So neither $\sqrt i$ nor $\sqrt2$ leaves a coordinate surd — both are absorbed into the prime-$2$ cyclotomic metric, exactly as the engineering metric $M=4I-J$ absorbs the $\sqrt3$ of the tetrahedral rotor calculus [Thomson]. **Consequence.** The threshold $\tfrac18$ — the *constant* argument of $\lambda(t)$ — is a finite, algebraic, cyclotomic landmark, not a transcendental obstruction; the entire transcendental content of the eigenvalue scale $\lambda(t)=\sqrt i\,/\sqrt{2\cosh\pi t}$ is its modulus, the scattering envelope $1/\sqrt{2\cosh\pi t}$. (Certified `empirical/probe_sqrt_i_absorption.py`.)

**Remark 4.4 (the cyclotomic tower: clusters, gap-centres, and the prime-2 meeting).** The three cyclotomic invariants of $U_N$ assemble into one $2$-power tower. The eigenvalues live on the eighth-root lattice, which splits as
$$x^8-1=\underbrace{(x^4-1)}_{\text{clusters: 4th roots }\{1,i,-1,-i\}}\cdot\underbrace{(x^4+1)}_{\Phi_8:\ \text{gap-centres }\{\zeta_8,\zeta_8^3,\zeta_8^5,\zeta_8^7\}},$$
with the determinant $\det U_N=i^{-\binom{N-1}2}\in\langle\zeta_4\rangle$ and the spectral concentration ([N3]) on the cluster factor $x^4-1$, and the no-crossing threshold (Remark 4.3, Theorem 4.2) on the gap-centre factor $\Phi_8=x^4+1$. The two floors are linked by a chain of square roots driven by the functional equation: the reflection $R:s\mapsto1-s$ is an involution (order $2$); its reflection product is Euler's formula with the quarter-turn $i=e^{i\pi/2}=\zeta_4$ in front (Theorem 4.1, order $4$); and the eigenvalue scale is its square root, of phase $\zeta_8=\sqrt{\zeta_4}$ (Theorem 4.2, order $8$). The doubling $2\to4\to8$ is the metaplectic/Maslov modulus — the Weil index $e^{i\pi/4}$ of the Gaussian over $\mathbb R$, the source of Berry–Keating's $\tfrac78=1-\tfrac18$.

Field-theoretically this is the tower
$$\mathbb Q\ \subset\ \mathbb Q(i)=\mathbb Q(\zeta_4)\ \subset\ \mathbb Q(\zeta_8)=\mathbb Q(i,\sqrt2),$$
whose top floor is the compositum of the **functional-equation reflection field** $\mathbb Q(i)$ and the **first prime rung** $\mathbb Q(\sqrt2)$ of the Helmert ladder ([T4]): the apex's archimedean Gauss phase inherits its $\sqrt2$ from rung $1$, so the cyclotomic and the multiquadratic arithmetics meet at the prime $2$. The whole tower is finite and absorbable (Remark 4.3); its Galois group $\mathrm{Gal}(\mathbb Q(\zeta_8)/\mathbb Q)\cong(\mathbb Z/8)^\times$ is realized concretely by signed permutations of the threshold operator $C$ — each twist $C^b$ ($b\in\{1,3,5,7\}$) by eight of them, with $\langle C\rangle$ (order $8$) the centralizer. (Certified `empirical/probe_v4_galois_edgeaxis.py`.)

This locates the apex precisely in the program's finite-versus-archimedean dichotomy: the entire **algebraic backbone** of the apex is the single $2$-power cyclotomic floor $\mathbb Q(\zeta_8)$ — determinant, concentration lattice, and threshold alike — generated at the prime $2$ and exactly absorbable; the multiplicative content of the remaining primes enters separately through the conductor blocks (the multiquadratic rungs $\sqrt p$, $p\ge3$); and the transcendental $\Gamma$-envelope begins exactly where this finite tower ends. The threshold $\tfrac18$ is the last finite landmark before the archimedean completion.

---

## 5. The even sector is the Paper II scattering operator

The kernel $e^{2\pi iw}=\cos2\pi w+i\sin2\pi w$ splits $\Phi$ into its even (cosine) and odd (sine) parts. The archimedean scattering operator of [PII] is the metaplectic Fourier transform restricted to even functions — the Fourier–cosine transform. We show the even sector of $\mathcal U$ matches it on the nose.

**Lemma 5.1 (parity/duplication).** *The even (cosine) symbol $c(s):=\int_0^\infty\cos(2\pi w)\,w^{s-1}\,dw=(2\pi)^{-s}\Gamma(s)\cos\tfrac{\pi s}2$ satisfies*
$$\Gamma(s)\cos\tfrac{\pi s}2=2^{s-1}\sqrt\pi\,\frac{\Gamma(s/2)}{\Gamma((1-s)/2)},\qquad\text{hence}\qquad c(s)=\tfrac12\,\frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)}.$$

*Proof.* Legendre duplication $\Gamma(s)=2^{s-1}\pi^{-1/2}\Gamma(s/2)\Gamma(\tfrac{s+1}2)$ and the reflection $\Gamma(\tfrac{1+s}2)\Gamma(\tfrac{1-s}2)=\pi/\cos\tfrac{\pi s}2$ give $\Gamma(s)\cos\tfrac{\pi s}2=2^{s-1}\pi^{-1/2}\Gamma(\tfrac s2)\Gamma(\tfrac{s+1}2)\cdot\pi/[\Gamma(\tfrac{1+s}2)\Gamma(\tfrac{1-s}2)]=2^{s-1}\sqrt\pi\,\Gamma(\tfrac s2)/\Gamma(\tfrac{1-s}2)$. Multiplying by $(2\pi)^{-s}$ and using $\Gamma(\tfrac s2)=\pi^{s/2}\Gamma_{\mathbb R}(s)$, $\Gamma(\tfrac{1-s}2)=\pi^{(1-s)/2}\Gamma_{\mathbb R}(1-s)$ collapses the powers of $\pi$ and $2$ to $\tfrac12\,\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(1-s)$. $\square$

**Theorem 5.2 (identification with [PII, Thm 7.1]).** *Let $\mathcal U_{\mathrm{ev}}=(A-I)\Phi_{\mathrm{ev}}$ be the even sector of the apex edge operator, $\Phi_{\mathrm{ev}}$ the Fourier–cosine transform. Its Mellin symbol is $\widetilde k_{\mathrm{ev}}(s)=\tfrac{s}{1-s}\cdot\tfrac12\,\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(1-s)$, and on the critical line*
$$2\,c(\tfrac12+it)=\frac{\Gamma_{\mathbb R}(\tfrac12+it)}{\Gamma_{\mathbb R}(\tfrac12-it)}=\gamma(t),\qquad |\gamma(t)|=1,$$
*the Riemann–Siegel multiplier of the Hardy–Titchmarsh intertwining $\mathcal V\widehat{\mathcal F}\mathcal V^{-1}=\gamma(s)R$ of [PII, Thm 7.1]. Hence the even apex edge operator is the [PII] archimedean scattering operator $\gamma(s)R$, multiplied by the Hardy–Blaschke factor $s/(1-s)$.*

*Proof.* Lemma 5.1 gives $c(s)=\tfrac12\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(1-s)$, so $2c(\tfrac12+it)=\Gamma_{\mathbb R}(\tfrac12+it)/\Gamma_{\mathbb R}(\tfrac12-it)$; this is unimodular because $\Gamma_{\mathbb R}(\tfrac12-it)=\overline{\Gamma_{\mathbb R}(\tfrac12+it)}$, and it is by definition the multiplier $\gamma$ of [PII]. The even symbol is $\widetilde k_{\mathrm{ev}}=\tfrac{s}{1-s}c(s)$ by Theorem 3.1 with $g$ replaced by its even part $c$; Lemma 2.2 makes $M_{c}R$ the operator $\gamma(s)R$. $\square$

**Remark 5.3 (the Connes–Consani archimedean operator).** The multiplier $\gamma(t)$ equals $e^{2i\vartheta(t)}$, the unitary $u_\infty$ of the Connes–Consani archimedean trace formula [CC20, eq. (26)], $\vartheta$ the Riemann–Siegel angular function. Thus the even apex edge operator is, up to the Hardy–Blaschke factor $s/(1-s)$, exactly the archimedean operator of [CC20]. The full identification — the convolution kernel $k^u$, the trace-remainder $\delta(\rho)$, and the Weil positivity $\widehat\delta+2\vartheta'\ge0$ read as the apex phase clock — is established in [N5], where the apex Weil quadratic form is assembled and verified against the zeta zeros.

This is the identification in full. The numerical match is to relative error $\le2\times10^{-41}$ (program record). The apex edge operator is, sector by sector, the archimedean operator: the even sector is exactly the [PII] scattering phase $\gamma(s)R$, and the only difference between the two objects is the Hardy–Blaschke factor $s/(1-s)$ — the apex's own arithmetic content, carrying the pole and trivial-zero data. The one-sided ($\Gamma(s)$) versus even ($\Gamma_{\mathbb R}$, i.e. $\Gamma(s/2)$) normalizations differ only by the Legendre duplication of Lemma 5.1.

---

## 6. The no-crossing reduction as a spectral gap

We can now restate the residual estimate of [N3] in operator terms. Recall [N3, Thm 1.2]: $U_N$ has the no-crossing property iff $\det(U_N^4+I)\neq0$ iff $\lVert U_N^2-U_N^{-2}\rVert<2$, with $\lVert U_N^2-U_N^{-2}\rVert=2\sin(4\pi\delta_{\max})$. Theorem 4.2 identifies $\tfrac18$ as the archimedean (reflection-formula) phase. Combining,

**Proposition 6.1 (spectral-gap form).** *No-crossing for $U_N$ is the statement that the leading displacement $\delta_{\max}(N)$ — the displacement of the single edge eigenvalue of $\sqrt N\,(U_N)$, which converges to the top eigenvalue of the explicit bounded operator $\mathcal U=(A-I)\Phi$ — stays strictly below the archimedean scattering threshold $\tfrac18$ at which the reflection-paired continuum accumulates (Theorem 4.2). Equivalently, the discrete edge mode of $\mathcal U$ is a bound state separated from the continuum by the gap $\tfrac18-\delta_\infty\approx0.028$.*

The estimate $\delta_\infty<\tfrac18$ of [N3, §8] is thereby reframed, exactly, as a bound on the top eigenvalue of a single explicit operator — not a numerical observation about a family of matrices. Two structural readings follow.

**(a) A de Branges phase clock.** The no-crossing condition is a monotone-phase statement. The function $\det(U_N^4+I)=2^{N-1}\prod_j\cos(4\pi\delta_j)$ of [N3, Prop. 4.2] is positive iff every eigenphase stays on its own side of the gap-centre — a discrete winding/monotonicity condition. This is the finite-$N$ avatar of the de Branges phase clock of [PIII], where the Hermite–Biehler function $E_B=\Xi+i\Xi'$ is globally of Hermite–Biehler class — equivalently $m_B=-\Xi'/\Xi$ is Herglotz — precisely under the Riemann Hypothesis, its boundary phase $\varphi$ then monotone with $\varphi(T)/\pi=N(T)$ counting zeros. (The pointwise velocity inequality $\varphi'\ge0$ — the first Laguerre inequality $(\Xi')^2-\Xi\Xi''\ge0$ — is the necessary boundary trace; the global absence of zeros of $E_B$ in $\mathbb C_+$ is the full Riemann-Hypothesis statement, since an off-line zero contributes a sign-reversing term to the phase velocity that can be masked on the line by the on-line zeros.) The apex furnishes a finite model of that clock, with the archimedean threshold made explicit as $\tfrac18$.

**(b) The exhibited operator.** [T20] formulates the simplicial route to RH as a governed admission and notes, in contrast to the Hilbert–Pólya program, that no spectral operator is exhibited. The apex unitary $U_N$, with its archimedean limit $\mathcal U=(A-I)\Phi$ identified here, is such an operator: an explicit unitary family whose spectral concentration is controlled by an archimedean scattering operator, with a Hilbert–Pólya-type gap separating the arithmetic edge mode from the archimedean threshold. We claim no proof of RH; we record that the operator whose absence was noted is now in hand, with its archimedean place computed.

---

## 7. Synthesis

The results assemble as follows. The apex unitary $U_N$ is a Helmert deformation of the discrete Fourier transform ([N2]); its spectrum concentrates at the fourth roots of unity ([N3]); the deformation's single obstruction is one edge mode, whose $N\to\infty$ limit is the product-kernel operator $\mathcal U=(A-I)\Phi$ (Proposition 2.1). That operator's Mellin symbol is a Hardy–Blaschke factor times the archimedean $\Gamma$-factor (Theorem 3.1); its reflection product is Euler's formula and *derives* the threshold $\tfrac18$ as the phase of $\sqrt i$ (Theorems 4.1–4.2); and its even sector is exactly the archimedean scattering operator $\gamma(s)R$ of the right-carrier paper [PII] (Theorem 5.2). The finite no-crossing positivity is the discrete de Branges clock of the closure paper [PIII], and the family $\{U_N\}$ is the explicit operator sought in [T20] (§6).

Two consequences for the wider program. First, the archimedean place — the local factor $Z_\infty=\pi^{-s/2}\Gamma(s/2)$ that [P0] proves the finite primes cannot generate, and that the No-Go isolates as the one true obstruction — is here realized as the scaling limit of finite apex unitaries: a *completion*, not a finite combination, exactly as a place at infinity should be. The No-Go and the present construction are complementary, not in tension. Second, the apex carries one factor more than the bare archimedean operator: the Blaschke factor $s/(1-s)$, with the pole and trivial zero of $\zeta$ built in. Assembling the finite-place ($U_N$ conductor-block) data with this archimedean edge into a single object is the natural next step, taken up elsewhere in the program.

We close on calibration. Every identity in §§2–5 is theorem-grade and certified to machine precision. What is *not* claimed is any statement about the zeros of $\zeta$: the identification is of the apex edge operator with the archimedean scattering operator — the functional-equation factor, the place at infinity — and not of $\delta_\infty$ with any zeta quantity. The residual estimate of [N3] survives, now as the cleanly-posed spectral gap of Proposition 6.1.

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$ over Multiquadratic–Cyclotomic Compositums.* First draft, May 28, 2026.

[N2] Murillo Montero, L. (2026). *The Apex Determinant: A Closed Form via Helmert–Fourier Factorization.* First draft, June 5, 2026.

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary: A Structural Reduction.* First draft, June 5, 2026.

[T9] Murillo Montero, L. (2026). *The Helmert–Fourier Transfer Matrix.* First draft, May 26, 2026.

[T4] Murillo Montero, L. (2026). *The Helmert–Simplicial Residue Ladder.* First draft, May 24, 2026 (the prime-rung radical field $K_N=\mathbb Q(\sqrt p:p\le N)$).

[T20] Murillo Montero, L. (2026). *A Simplicial Route to RH: Conformal Admission and the Cofinal Lift.* First draft.

[P0] Murillo Montero, L. (2026). *Place Completion: The Adelic Apex.* First draft, May 30, 2026.

[PII] Murillo Montero, L. (2026). *The Right Carrier* (RH trilogy, Paper II), Thm 7.1 (Hardy–Titchmarsh intertwining). Second draft.

[PIII] Murillo Montero, L. (2026). *Closure* (RH trilogy, Paper III), de Branges phase clock and the (GBP) positivity. Second draft.

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.* First draft, June 5, 2026.

[CC20] Connes, A., and Consani, C. (2020). *Weil positivity and Trace formula: the archimedean place.* arXiv:2006.13771.

[Thomson] Thomson, A. (2026). *Spread-Quadray Rotors: A Rational, Tetrahedral-Native Algebra for 3D Rotation.* Thomson Architecture, Inc. / ABCD.Earth Project (the metric $M=4I-J$ absorbing $\sqrt3$; builds on the present series' simplicial vector calculus).

de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice–Hall.

Hardy, G. H., Littlewood, J. E., and Pólya, G. (1934). *Inequalities.* Cambridge University Press.

Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function.* Second edition, revised by D. R. Heath-Brown. Oxford University Press.

Schur, I. (1921). Über die Gauss'schen Summen. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 147–153.
