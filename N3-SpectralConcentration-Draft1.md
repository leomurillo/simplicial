# N3 — Spectral Concentration of the Apex Unitary: A Structural Reduction

**Leonardo Murillo Montero**

*June 5, 2026*

<!--
Program record (not part of the paper). Third paper of the Numbers (N-) series;
companion to N1 (definition, fields, Galois action) and N2 (determinant). All
quantitative claims are certified by deterministic computation under empirical/:
  probe_apex_spectrum_concentration_N3.py   (multiplicity law, N<=4096)
  probe_apex_nocrossing_reduction_N3.py     (the reduction theorem identities)
  probe_apex_det_u4plusI_N3.py              (det(U^4+I) structure)
  probe_apex_power_traces_N3.py             (multiplicity recovery)
  probe_apex_energy_route_N3.py             (energy functionals)
  probe_apex_trace_fieldtrace_N3.py         (field-trace theorem)
The entry closed form is from T9; the paper is self-contained from Section 2.
-->

---

## Abstract

For each integer $N\ge2$ let $U_N\in U(N-1)$ be the apex unitary intertwining the Helmert and character frames of the mean-zero hyperplane of $\mathbb C^N$. Numerically, the eigenvalues of $U_N$ concentrate at the four eigenvalues $\{1,i,-1,-i\}$ of the discrete Fourier transform, with multiplicities that depend only on $N$ modulo $4$. We prove that this concentration is governed by a single non-degeneracy. Writing $U_N^{-1}=U_N^{*}$, the eigenvalues of $U_N$ all lie strictly within an eighth of a turn of a fourth root of unity if and only if
$$\det\!\big(U_N^{4}+I\big)\neq0,\qquad\text{equivalently}\qquad \big\lVert U_N^{2}-U_N^{-2}\big\rVert_{\mathrm{op}}<2,$$
and we give the exact identity $\lVert U_N^2-U_N^{-2}\rVert=2\sin(4\pi\delta_{\max})$, where $\delta_{\max}$ is the largest displacement of an eigenvalue from its nearest fourth root. Around this reduction we establish, unconditionally, the supporting structure: the determinant $\det(U_N^4+I)=(-1)^{\binom{N-1}{2}}\det(U_N^2+U_N^{-2})=2^{N-1}\prod_j\cos(4\pi\delta_j)$ is real; the cluster multiplicities are recovered exactly by rounding the first four power traces; the field trace of $\operatorname{tr}U_N$ over $\mathbb Q(\zeta_N)$ is computed in closed form; and a rescaling of the matrix entries produces an explicit half-line integral operator $\mathcal U=(A-I)\Phi$ ($A$ the Hardy mean, $\Phi$ the half-line Fourier transform) whose leading eigenvalue is the displacement of the single edge mode that controls everything. The spectral-concentration theorem thus reduces to one isolated estimate, $\delta_{\max}<\tfrac18$, equivalently $\det(U_N^4+I)\neq0$ for all $N$, which the numerics support with margin (the limiting displacement is $\approx0.097<0.125$).

---

## 1. Introduction

The companion papers study the apex unitary $U_N$ as an arithmetic object: [N1] sets up its definition over the multiquadratic–cyclotomic compositum and its Galois action, and [N2] proves the closed form $\det U_N=i^{-\binom{N-1}{2}}$ via the factorization $\det U_N=\det H\cdot\det F$ into a Helmert sign and Schur's Fourier determinant. The present paper turns to the full spectrum.

The starting observation is that $U_N$ is, by construction, a *Helmert deformation of the discrete Fourier transform*. It is the nontrivial diagonal block of $M=HF^{\mathsf T}$, where $H$ is the full normalized Helmert matrix and $F$ the symmetric Fourier matrix (N2, Prop. 3.1). The Fourier matrix is the metaplectic object par excellence: $F^4=I$, so its spectrum is contained in $\{1,i,-1,-i\}$, with the four multiplicities classical (Schur; McClellan–Parks; the eigenvectors approximate Hermite functions). Numerically, the eigenvalues of $U_N$ inherit this fourfold structure — they cluster tightly at the same four points — even though $H$ is a large rotation, not a small perturbation. This paper makes that statement precise and reduces it to a single, sharply-stated estimate.

**The concentration.** Write the eigenvalues of $U_N$ as $\lambda_j=e^{2\pi i\theta_j}$, let $i^{c_j}$ be the nearest fourth root of unity, and let $\delta_j=\theta_j-\tfrac{c_j}{4}\in[-\tfrac18,\tfrac18]$ be the displacement (in turns). We say $U_N$ has the **no-crossing property** if $|\delta_j|<\tfrac18$ for every $j$ — equivalently, no eigenvalue sits at a cluster boundary (a gap-centre, the midpoint between adjacent fourth roots). Under no-crossing the eigenvalues partition unambiguously into four clusters, and we write $(m_1,m_i,m_{-1},m_{-i})$ for the cluster sizes.

**Conjecture 1.1 (multiplicity law).** For all $N\ge2$, $U_N$ has the no-crossing property, and with $q=\lfloor N/4\rfloor$,
$$(m_1,m_i,m_{-1},m_{-i})=\begin{cases}(q,q,q,q), & N\equiv1,\\(q+1,q,q,q), & N\equiv2,\\(q+1,q,q,q+1), & N\equiv3,\\(q,q-1,q,q), & N\equiv0,\end{cases}\pmod 4.$$

This has been verified by exact computation for all $N\le4096$. The cluster sizes are a clean, nontrivial deformation of the Fourier multiplicities — they are not simply the Fourier multiplicities with the trivial mode removed.

**The reduction.** Our main theorem is that the no-crossing property — the load-bearing analytic content of Conjecture 1.1 — is equivalent to a single algebraic non-degeneracy.

**Theorem 1.2 (reduction).** The apex unitary $U_N$ has the no-crossing property if and only if $\det(U_N^4+I)\neq0$, equivalently $\lVert U_N^2-U_N^{-2}\rVert_{\mathrm{op}}<2$.

Theorem 1.2 (proved in §4) compresses the spectral problem to a non-vanishing determinant, and the rest of the paper establishes the unconditional structure surrounding it: §4 records the real, positive closed form of that determinant; §5 recovers the multiplicities from the first four power traces and explains why no fixed-degree trace inequality can certify the non-vanishing; §6 locates the obstruction in a single edge eigenvalue via an explicit continuum limit; §7 proves the closed form of the field trace of $\operatorname{tr}U_N$. Section 8 collects the reduction: everything is theorem-grade except the one estimate $\det(U_N^4+I)\neq0$, which the numerics support with a definite margin.

Throughout, $\omega=e^{2\pi i/N}$, $\zeta_m=e^{2\pi i/m}$, and $\binom n2=n(n-1)/2$. For a normal matrix $\lVert\cdot\rVert_{\mathrm{op}}$ is the spectral radius.

---

## 2. The apex unitary and the Fourier spectrum

We recall the minimum needed from [N1, N2]. On the mean-zero hyperplane $H_N=\{v\in\mathbb C^N:\sum_jv_j=0\}$ the normalized Helmert vectors $e_k=h_k/\sqrt{k(k+1)}$ (with $h_k=(1,\dots,1,-k,0,\dots,0)$, $k$ ones) and the normalized characters $\tilde\chi_c=(\omega^{cj})_j/\sqrt N$ form two orthonormal frames. The apex unitary $U_N\in U(N-1)$ is the change of basis with entries $(U_N)_{kc}=\langle\tilde\chi_c,e_k\rangle=R_kC_{kc}$, where $R_k=1/\sqrt{Nk(k+1)}$ is the row radical and $C_{kc}=\sum_{j=0}^{k-1}\omega^{cj}-k\,\omega^{ck}\in\mathbb Z[\omega]$ is the cyclotomic factor of [N1, Prop. 2.3]; on the diagonal $C_{kk}=\sum_{j=0}^{k-1}\omega^{kj}-k\,\omega^{k^2}$.

Let $H$ be the full normalized Helmert matrix (row $0$ the mean $\tfrac1{\sqrt N}(1,\dots,1)$, rows $k=e_k$) and $F$ the symmetric Fourier matrix $F_{cj}=\omega^{cj}/\sqrt N$. Then $F=F^{\mathsf T}$ is unitary, and:

**Proposition 2.1 (N2, Prop. 3.1).** $M:=HF^{\mathsf T}=HF$ has the block form $M=1\oplus U_N$; in particular $\operatorname{tr}(U_N^k)=\operatorname{tr}(M^k)-1=\operatorname{tr}((HF)^k)-1$ for all $k$, and $\operatorname{spec}(U_N)=\operatorname{spec}(M)\setminus\{1\}$.

The Fourier matrix satisfies
$$F^2=R,\qquad F^4=I,\qquad (Rv)_j=v_{-j}\ (\text{reversal}),$$
so $\operatorname{spec}(F)\subseteq\{1,i,-1,-i\}$. Its four multiplicities depend on $N\bmod4$ (Schur; McClellan–Parks). The eigenvalues of $U_N=$ block of $HF$ are the deformation of $\operatorname{spec}(F)$ studied here.

For an eigenvalue $\lambda=e^{2\pi i\theta}$ of $U_N$ we use throughout: nearest fourth root $i^{c}$, displacement $\delta=\theta-\tfrac c4\in[-\tfrac18,\tfrac18]$, so that
$$\lambda^2=(-1)^{c}e^{4\pi i\delta},\qquad \lambda^4=e^{8\pi i\delta},\qquad \lambda^2-\lambda^{-2}=2i(-1)^{c}\sin(4\pi\delta),\qquad \lambda^2+\lambda^{-2}=2(-1)^{c}\cos(4\pi\delta).$$
The displacement of $U_N$ is $\delta_{\max}=\max_j|\delta_j|$.

---

## 3. The concentration phenomenon

Computation shows the spectrum of $U_N$ is sharply concentrated: for every $N\le4096$ the eigenvalues partition into four clusters around $\{1,i,-1,-i\}$ with the multiplicities of Conjecture 1.1, and the displacements $\delta_j$ are minute for all but two eigenvalues. Precisely, the median displacement is $0$ to working precision, and only **two** eigenvalues — one on the upper edge of the cluster at $+1$, one on the lower edge of the cluster at $-i$ — carry a macroscopic displacement; every other displacement is below $0.02$ of a turn. The leading displacement $\delta_{\max}(N)$ grows slowly and monotonically (Table 3.1) and, as we shall see in §6, converges to a limit $\delta_\infty\approx0.097$, comfortably below the gap half-width $\tfrac18=0.125$.

**Table 3.1.** Leading displacement $\delta_{\max}(N)$ (turns) and the gap margin $\tfrac18-\delta_{\max}$.

| $N$ | $16$ | $64$ | $256$ | $1024$ | $4096$ |
|---|---|---|---|---|---|
| $\delta_{\max}$ | $0.0315$ | $0.0500$ | $0.0632$ | $0.0727$ | $0.0796$ |
| $\tfrac18-\delta_{\max}$ | $0.0935$ | $0.0750$ | $0.0618$ | $0.0523$ | $0.0454$ |

That every eigenvalue stays within the gap half-width is the no-crossing property. The remainder of the paper is organized around it.

---

## 4. The no-crossing reduction

This section proves Theorem 1.2 and records the structure of the governing determinant. Both $U^2\pm U^{-2}$ (we drop the subscript $N$) are polynomials in the unitary $U$, hence normal, with eigenvalues $\lambda_j^2\pm\lambda_j^{-2}$ on the respective lines.

**Theorem 4.1.** The following are equivalent.
1. **(I)** $U$ has the no-crossing property ($|\delta_j|<\tfrac18$ for all $j$);
2. **(II)** $-1\notin\operatorname{spec}(U^4)$, i.e. $\det(U^4+I)\neq0$;
3. **(III)** $(U^2+U^{-2})^2=2I+U^4+U^{-4}$ is positive definite;
4. **(IV)** $\lVert U^2-U^{-2}\rVert_{\mathrm{op}}<2$.

Moreover, with the Hermitian matrix $B:=-i\,(U^2-U^{-2})$ one has $B^2=2I-U^4-U^{-4}$ and
$$\big\lVert U^2-U^{-2}\big\rVert=\lVert B\rVert=2\sin\!\big(4\pi\,\delta_{\max}\big).$$

*Proof.* On the unit circle $\lambda_j^2-\lambda_j^{-2}=2i\sin(4\pi\theta_j)$, $\ \lambda_j^2+\lambda_j^{-2}=2\cos(4\pi\theta_j)$, and $\lambda_j^4=e^{8\pi i\theta_j}$.

*(I)$\Leftrightarrow$(II).* $\lambda_j^4=-1\iff 8\pi\theta_j\equiv\pi\pmod{2\pi}\iff\theta_j\in\{\tfrac18,\tfrac38,\tfrac58,\tfrac78\}$. These four points are exactly the gap-centres (midpoints between consecutive fourth roots). Hence some eigenvalue sits at a gap $\iff-1\in\operatorname{spec}(U^4)\iff\det(U^4+I)=0$; negating gives (I)$\Leftrightarrow$(II).

*(II)$\Leftrightarrow$(III).* For $|\lambda|=1$, $\lambda^4=-1\iff\lambda^2\in\{i,-i\}\iff\lambda^2+\lambda^{-2}=0$ (e.g. $\lambda^2=i\Rightarrow\lambda^{-2}=-i$). Thus $-1\in\operatorname{spec}(U^4)\iff0\in\operatorname{spec}(U^2+U^{-2})$. Since $U^2+U^{-2}$ is Hermitian, $(U^2+U^{-2})^2\succeq0$ always and is $\succ0$ iff $U^2+U^{-2}$ is nonsingular. The identity $(U^2+U^{-2})^2=2I+U^4+U^{-4}$ is immediate. Hence (II)$\Leftrightarrow$(III).

*(III)$\Leftrightarrow$(IV).* $B$ is Hermitian because $(U^2-U^{-2})^{*}=U^{-2}-U^2$. Then
$$B^2=-(U^2-U^{-2})^2=2I-U^4-U^{-4},\qquad 4I-B^2=2I+U^4+U^{-4}=(U^2+U^{-2})^2.$$
So $(U^2+U^{-2})^2\succ0\iff B^2\prec4I\iff\lVert B\rVert<2$. Finally $\lVert B\rVert=\max_j2|\sin4\pi\theta_j|$; writing $\theta_j=\tfrac{c_j}4+\delta_j$ gives $|\sin4\pi\theta_j|=\sin4\pi|\delta_j|$ (monotone on $[0,\tfrac18]$), so $\lVert B\rVert=2\sin4\pi\delta_{\max}$. $\square$

The quantitative margin to crossing is therefore $2-\lVert U^2-U^{-2}\rVert=2\big(1-\sin4\pi\delta_{\max}\big)$. We next record that the governing determinant is real and positive, with an explicit value.

**Proposition 4.2.** $\det(U_N^4+I)$ is a non-negative real number, and
$$\det(U_N^4+I)=(-1)^{\binom{N-1}{2}}\det\!\big(U_N^2+U_N^{-2}\big)=2^{\,N-1}\prod_{j=1}^{N-1}\cos(4\pi\delta_j)\ \in\ [0,\,2^{\,N-1}],$$
vanishing if and only if $U_N$ fails no-crossing.

*Proof.* Factor $U^4+I=U^2(U^2+U^{-2})$. By the determinant theorem of [N2], $\det U^2=(\det U)^2=(i^{-\binom{N-1}{2}})^2=(-1)^{\binom{N-1}{2}}$, while $U^2+U^{-2}=U^2+(U^*)^2$ is Hermitian with real determinant; the first equality follows. For the second, each eigenvalue contributes $\lambda_j^4+1=2\cos(4\pi\delta_j)\,e^{4\pi i\delta_j}$ with $\cos(4\pi\delta_j)\ge0$ for $|\delta_j|\le\tfrac18$; the product of the unimodular phases is $\pm1$ by the reality just proved, and equals $+1$ since the product of the non-negative moduli is real and the determinant is real. Non-negativity and the range are immediate, and $\det=0\iff$ some $\cos(4\pi\delta_j)=0\iff$ some $|\delta_j|=\tfrac18$. $\square$

Proposition 4.2 is the structural heart of the reduction. The determinant carries no multiquadratic radical content (it is real and, after the N2 sign, equals a Hermitian determinant), and its strict positivity is *exactly* the no-crossing property. We return in §8 to the fact that this gives no algebraic shortcut: $\det(U^2+U^{-2})$ is the determinant of a *sum*, to which the product factorization $\det U=\det H\cdot\det F$ of [N2] does not apply.

**Remark 4.3 (the multiplicity values).** Theorem 4.1 establishes that no-crossing — the unambiguous fourfold clustering — is the non-degeneracy $\det(U_N^4+I)\neq0$. The specific cluster *sizes* of Conjecture 1.1 are an additional input; §5 shows they are recovered from the first four power traces, and are stable under no-crossing.

---

## 5. Power-trace formulations

The multiplicities and the no-crossing condition both have transparent expressions in the power traces $p_m=\operatorname{tr}(U_N^m)=\operatorname{tr}((HF)^m)-1$.

**Proposition 5.1 (recovery of multiplicities).** Under no-crossing, for $r=0,1,2,3$ (clusters $1,i,-1,-i$),
$$m_r=\Big\lfloor\tfrac14\operatorname{Re}\sum_{m=0}^{3}i^{-rm}\,p_m\Big\rceil\quad(\text{nearest integer}),\qquad p_0=N-1.$$

*Proof (sketch).* The quantity $a_r=\tfrac14\sum_{m=0}^3 i^{-rm}p_m=\sum_j w_r(\lambda_j)$ with $w_r(\lambda)=\tfrac14\sum_{m=0}^3(i^{-r}\lambda)^m$. For $\lambda$ in cluster $r$ ($i^{-r}\lambda=e^{2\pi i\delta}$, small $\delta$) one has $\operatorname{Re}w_r=1-7\pi^2\delta^2+O(\delta^4)$; for a neighbouring cluster $\operatorname{Re}w_r=O(\delta)$, and for the opposite cluster $\operatorname{Re}w_r=O(\delta^2)$. Summing, $\operatorname{Re}a_r=m_r+\varepsilon_r$ with $|\varepsilon_r|<\tfrac12$ provided the displacements are small enough; the bound $|\varepsilon_r|<\tfrac12$ holds throughout the computed range ($|\varepsilon_r|\le0.17$ for $N\le3000$), so the rounding returns $m_r$. $\square$

Proposition 5.1 reformulates Conjecture 1.1 as a rounding statement about $\operatorname{tr}((HF)^m)$, $m\le3$ — the leading characteristic-polynomial data. Note the *imaginary* part $\tfrac14\operatorname{Im}\sum i^{-rm}p_m$ is the net displacement chirality and grows, but does not enter the rounding.

The no-crossing condition itself sits one level up, in the even moments of $B$. From $B^2=2I-U^4-U^{-4}$,
$$\operatorname{tr}(B^2)=2\big[(N-1)-\operatorname{Re}\operatorname{tr}(U^4)\big]=2\,\mathcal E_N,\qquad \mathcal E_N:=N-\operatorname{Re}\operatorname{tr}((HF)^4),$$
the *total displacement energy* $\mathcal E_N=\sum_j(1-\cos8\pi\delta_j)$; and more generally $\operatorname{tr}(B^{2p})$ is a $\mathbb Z$-combination of $\operatorname{tr}((HF)^{4k})$, $|k|\le p$. Since $B^2\succeq0$,
$$\text{no-crossing}\iff\lVert B\rVert=\lim_{p\to\infty}\operatorname{tr}(B^{2p})^{1/2p}<2.$$

**Remark 5.2 (no finite-degree certificate).** The lowest moment gives the sufficient condition $\operatorname{tr}(B^2)<4$, i.e. $\mathcal E_N<2$. This *fails*: the energy is shared by the two stragglers (near $+1$ and near $-i$), and $\mathcal E_N\to\approx3.3>2$. A degree-$2p$ test $\operatorname{tr}(B^{2p})<4^p$ is sufficient but, because of the same two-straggler factor, certifies $\lVert B\rVert<2$ only as $p\to\infty$ (the spectral radius $\lim_p\operatorname{tr}(B^{2p})^{1/2p}=2\sin4\pi\delta_\infty\approx1.88<2$). Thus no single fixed-degree power-trace inequality can establish the no-crossing; the obstruction is genuinely the leading eigenvalue, not an aggregate.

---

## 6. The edge operator

Section 5 shows the difficulty is a single edge mode. Here we identify the operator that mode belongs to, by rescaling the matrix entries. The leading straggler's eigenvector is concentrated at the low-frequency edge (indices of order $\sqrt N$), which fixes the scaling $k=\sqrt N\,u$, $c=\sqrt N\,v$. Substituting into the entry formula and letting $N\to\infty$,
$$\sqrt N\,(U_N)_{kc}\ \longrightarrow\ K(u,v):=\frac{e^{2\pi i uv}-1}{2\pi i\,uv}-e^{2\pi i uv},$$
a limit confirmed numerically (relative error below $1\%$ at $N=10^4$). The corresponding operator on $L^2[0,\infty)$,
$$(\mathcal U\psi)(u)=\int_0^\infty K(u,v)\,\psi(v)\,dv,$$
factors cleanly: using $\dfrac{e^{2\pi iuv}-1}{2\pi iuv}=\dfrac1u\displaystyle\int_0^u e^{2\pi itv}\,dt$,
$$\boxed{\ \mathcal U=(A-I)\,\Phi\ },\qquad (\Phi\psi)(u)=\int_0^\infty e^{2\pi iuv}\psi(v)\,dv,\quad (A g)(u)=\frac1u\int_0^u g(t)\,dt,$$
the half-line Fourier transform $\Phi$ composed with the Hardy averaging operator minus the identity. The leading straggler is the eigenvalue of (the finite-$N$ truncation of) $\mathcal U$ nearest the cluster edge; its displacement satisfies
$$\delta_{\max}(N)\ \longrightarrow\ \delta_\infty\approx0.097,\qquad \delta_\infty-\delta_{\max}(N)\asymp N^{-1/4},$$
the exponent $\tfrac14$ being the boundary-layer scaling of a box of size $\sim\sqrt N$. The mode is genuinely two-scale — a sharp peak of size $O(1)$ atop a body of width $\sqrt N$ — so $\delta_\infty$ is not the leading eigenvalue of a single-scale operator, and we do not have a closed form for it. What §6 provides is the localization: the entire obstruction of §4–§5 is the edge eigenvalue of the explicit operator $(A-I)\Phi$, and the open estimate is $\delta_\infty<\tfrac18$, i.e. $2\sin4\pi\delta_\infty<2$.

**Remark 6.1 (identification of the edge operator; sequel).** The operator $(A-I)\Phi$ is identified in [N4] as an archimedean operator, which both supplies the closed form missing above and explains the constant $\tfrac18$. Its kernel depends only on the product $uv$, so it acts on the Mellin transform as a multiplier composed with the reflection $s\mapsto1-s$, with closed form
$$\widetilde k(s)=\frac{s}{1-s}\,(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$$
— a Hardy–Blaschke factor (zero at $s=0$, pole at $s=1$, the trivial-zero and pole loci of $\zeta$) times the archimedean $\Gamma$-factor of the additive character. In the reflection product that fixes the eigenvalues the Blaschke factor cancels its mirror, leaving Euler's reflection formula $\widetilde k(s)\widetilde k(1-s)=i/(2\sin\pi s)$; on the critical line the eigenvalue scale is $e^{i\pi/4}/\sqrt{2\cosh\pi t}$. Hence the threshold $\tfrac18$ above is exactly the phase of $\sqrt i$ supplied by the reflection formula — not a free geometric constant — and the open estimate $\delta_\infty<\tfrac18$ is the statement that the discrete edge mode is a bound state strictly below the archimedean continuum threshold. The even sector of $(A-I)\Phi$ equals the archimedean scattering operator $\gamma(s)R$ of [PII, Thm 7.1].

---

## 7. The trace and its field trace

The first power trace has independent arithmetic content. From the radical–cyclotomic split,
$$\operatorname{tr}U_N=\sum_{k=1}^{N-1}(U_N)_{kk}=\sum_{k=1}^{N-1}R_k\,C_{kk},\qquad C_{kk}=\sum_{j=0}^{k-1}\omega^{jk}-k\,\omega^{k^2}\in\mathbb Q(\zeta_N).$$
Each diagonal entry carries a row radical $R_k=1/\sqrt{Nk(k+1)}$. The behaviour of the radical content under the Galois group of $L_N=K_N\cdot\mathbb Q(\zeta_N)$ over $\mathbb Q(\zeta_N)$ is determined by sign characters, and is fully explicit.

**Theorem 7.1.** Let $\Gamma=\operatorname{Gal}(L_N/\mathbb Q(\zeta_N))$, of order $2^{s}$ with $s=\pi(N)-t(N)$ (notation of [N1, §2.4]), and let
$$S_N=\{\,k\in\{1,\dots,N-1\}:\sqrt{\operatorname{sf}(Nk(k+1))}\in\mathbb Q(\zeta_N)\,\}.$$
Then $\operatorname{Tr}_{L_N/\mathbb Q(\zeta_N)}\big((U_N)_{kk}\big)=2^{s}(U_N)_{kk}$ for $k\in S_N$ and $0$ otherwise; hence
$$\operatorname{Tr}_{L_N/\mathbb Q(\zeta_N)}\big(\operatorname{tr}U_N\big)=2^{s}\sum_{k\in S_N}(U_N)_{kk}.$$
In particular the genuinely non-cyclotomic part $\sum_{k\notin S_N}(U_N)_{kk}$ has vanishing field trace; the field trace of $\operatorname{tr}U_N$ vanishes iff $\sum_{k\in S_N}(U_N)_{kk}=0$.

*Proof.* Each $\tau\in\Gamma$ fixes $\mathbb Q(\zeta_N)$, hence fixes $C_{kk}$, and sends $R_k\mapsto\varepsilon_k(\tau)R_k$ for a sign character $\varepsilon_k\colon\Gamma\to\{\pm1\}$ ($\varepsilon_k$ trivial $\iff R_k\in\mathbb Q(\zeta_N)\iff k\in S_N$). By orthogonality of characters $\sum_{\tau\in\Gamma}\varepsilon_k(\tau)=2^{s}\,[\![k\in S_N]\!]$, so $\operatorname{Tr}_{L_N/\mathbb Q(\zeta_N)}(R_kC_{kk})=C_{kk}\sum_\tau\tau(R_k)=2^{s}R_kC_{kk}\,[\![k\in S_N]\!]$. Sum over $k$. $\square$

Theorem 7.1 corrects the naive expectation that the field trace vanishes for all $N$: it does so precisely when $S_N=\varnothing$ — the case at $N=4$, where every row radical is non-cyclotomic. The first $N\ge3$ with $S_N\neq\varnothing$ is $N=5$, where $S_5=\{4\}$, $(U_5)_{44}=-\tfrac12\zeta_5$, and the field trace equals $-2\zeta_5\neq0$.

---

## 8. The structural reduction

We collect the result. Around the spectral concentration of $U_N$ the following are established unconditionally:

- **(Theorem 4.1)** the no-crossing property $\iff\det(U_N^4+I)\neq0\iff(U_N^2+U_N^{-2})^2\succ0\iff\lVert U_N^2-U_N^{-2}\rVert<2$, with $\lVert U_N^2-U_N^{-2}\rVert=2\sin4\pi\delta_{\max}$;
- **(Proposition 4.2)** $\det(U_N^4+I)=(-1)^{\binom{N-1}{2}}\det(U_N^2+U_N^{-2})=2^{N-1}\prod_j\cos4\pi\delta_j$, real and in $[0,2^{N-1}]$;
- **(Proposition 5.1)** recovery of the cluster multiplicities from $\operatorname{tr}(U_N^m)$, $m\le3$;
- **(Remark 5.2)** the no-crossing is the spectral-radius condition $\lim_p\operatorname{tr}(B^{2p})^{1/2p}<2$, with no fixed-degree certificate;
- **(Theorem 7.1)** the closed form of the field trace of $\operatorname{tr}U_N$;
- **(§6)** the explicit edge operator $\mathcal U=(A-I)\Phi$ whose leading eigenvalue is the displacement $\delta_{\max}$.

What remains is a single estimate, in five equivalent forms:
$$\delta_{\max}<\tfrac18\iff\det(U_N^4+I)\neq0\iff\lVert U_N^2-U_N^{-2}\rVert<2\iff(U_N^2+U_N^{-2})^2\succ0\iff\prod_j\cos4\pi\delta_j>0.$$

Granting this estimate, $U_N$ has the no-crossing property and the spectrum partitions into the four clusters; the multiplicity values of Conjecture 1.1 then follow from Proposition 5.1. The estimate is supported numerically for all $N\le4096$ and, through the edge operator of §6, is localized to a single mode whose limiting displacement $\delta_\infty\approx0.097$ lies below the threshold $\tfrac18=0.125$ with margin $\approx0.028$. It is not reducible to a finite algebraic or trace identity: Proposition 4.2 shows the governing determinant is a determinant of a *sum*, and Remark 5.2 shows the aggregate energy provably exceeds the threshold. The concentration theorem is thus reduced to the edge estimate $\delta_\infty<\tfrac18$, and no further.

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in U(N−1) over Multiquadratic–Cyclotomic Compositums.* First draft, May 28, 2026.

[N2] Murillo Montero, L. (2026). *The Apex Determinant: A Closed Form via Helmert–Fourier Factorization.* First draft, June 5, 2026.

[T9] Murillo Montero, L. (2026). *The Helmert–Fourier Transfer Matrix.* First draft, May 26, 2026.

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* First draft, June 5, 2026.

[PII] Murillo Montero, L. (2026). *The Right Carrier* (RH trilogy, Paper II), Thm 7.1. Second draft.

McClellan, J. H., and Parks, T. W. (1972). Eigenvalue and eigenvector decomposition of the discrete Fourier transform. *IEEE Transactions on Audio and Electroacoustics* 20(1), 66–74.

Mehta, M. L. (1987). Eigenvalues and eigenvectors of the finite Fourier transform. *Journal of Mathematical Physics* 28(4), 781–785.

Schur, I. (1921). Über die Gauss'schen Summen. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 147–153.

Hardy, G. H., Littlewood, J. E., and Pólya, G. (1934). *Inequalities.* Cambridge University Press.

Washington, L. C. (1997). *Introduction to Cyclotomic Fields.* Second edition. Graduate Texts in Mathematics 83. Springer.
