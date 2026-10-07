# N1 — Apex Unitaries: An Explicit Family in U(N−1) over Multiquadratic–Cyclotomic Compositums

**Leonardo Murillo Montero**

*May 28, 2026*

<!--
Program record (not part of the paper). Opening paper of the Numbers (N-)
series. The general determinant is proved in the companion paper
N2-ApexDeterminant-Draft1.md. Computations at level 4 are reproduced by the
certificates under empirical/ (probe_apex_convention_N1.py and the determinant
probes). The entry closed form (2.1) is from T9 (Helmert–Fourier transfer
matrix); this paper is self-contained.
-->

---

## Abstract

For each integer $N\ge 2$ we study the unitary matrix $U_N\in U(N-1)$ that intertwines the normalized Helmert basis and the nontrivial additive characters of $\mathbb Z/N$ on the mean-zero hyperplane of $\mathbb C^N$. Its entries lie in the compositum $K_N\cdot\mathbb Q(\zeta_N)$ of the multiquadratic field $K_N=\mathbb Q(\sqrt p:p\le N)$ and the cyclotomic field $\mathbb Q(\zeta_N)$, and split as a product of a quadratic-radical row scalar and a cyclotomic integer. We describe this arithmetic structure, compute the degree of the compositum, and determine the basic spectral invariants at $N=4$ in closed form: the determinant is $i$, the trace is an explicit element of $\mathbb Q(\sqrt2,\sqrt3,i)$ whose field trace over $\mathbb Q(\zeta_4)$ vanishes, and the characteristic polynomial is given explicitly; in particular not all eigenvalues of $U_4$ are roots of unity, although their product is. Finally we describe the action of the Galois group of the compositum on $U_N$ as a signed monomial transformation $U_N\mapsto D\,U_N\,P$, and use it to explain the rationality of $\det U_4$ over $\mathbb Q(\zeta_4)$. The determinant for general $N$ is obtained in closed form in the companion paper.

---

## 1. Introduction

Fix $N\ge 2$ and work on the mean-zero hyperplane
$$H_N:=\Big\{v\in\mathbb C^N:\textstyle\sum_{j=0}^{N-1}v_j=0\Big\}$$
with the standard Hermitian inner product $\langle u,v\rangle=\sum_j u_j\overline{v_j}$. The space $H_N$ carries two natural orthonormal frames: the real *Helmert frame* of nested contrasts, and the complex *character frame* of nontrivial additive characters of $\mathbb Z/N$. The unitary change of basis between them is a matrix $U_N\in U(N-1)$ whose entries are explicit algebraic numbers in the compositum $K_N\cdot\mathbb Q(\zeta_N)$, combining quadratic-radical and cyclotomic content.

This paper sets up the family $\{U_N\}_{N\ge2}$ as an arithmetic object and records its first invariants. Section 2 gives the definition, the field of definition, the factorization of the entries into a radical part and a cyclotomic part, and the degree of the compositum. Section 3 computes the determinant, trace, and characteristic polynomial at $N=4$ in closed form; a noteworthy point is that the trace fails to be an algebraic integer, which forces at least one eigenvalue of $U_4$ to be a non-root-of-unity even though the product of the eigenvalues is the root of unity $i$. Section 4 describes the action of $\mathrm{Gal}(K_N\cdot\mathbb Q(\zeta_N)/\mathbb Q)$ on $U_N$ as a signed monomial transformation and uses it to explain why $\det U_4$ lies in the cyclotomic field $\mathbb Q(\zeta_4)$ despite the radicals carried by the individual entries.

The determinant for general $N$ is determined in closed form in the companion paper [N2]: $\det U_N=i^{-\binom{N-1}{2}}$. Section 5 lists the invariants taken up in subsequent papers of the series.

Throughout, $\omega=e^{2\pi i/N}$ and $\zeta_m=e^{2\pi i/m}$; $\pi(N)$ is the number of primes $\le N$ and $\varphi$ is Euler's totient.

---

## 2. The apex unitary

### 2.1 Two orthonormal frames of the hyperplane

The **Helmert vectors** $h_k$ ($k=1,\dots,N-1$) consist of $k$ leading ones, then the entry $-k$, then $N-1-k$ trailing zeros:
$$h_k:=(\,1,\dots,1,\,-k,\,0,\dots,0\,)\in\mathbb Z^N.$$
They are real, mutually orthogonal, mean-zero, and satisfy $\|h_k\|^2=k(k+1)$; the normalized vectors $e_k:=h_k/\sqrt{k(k+1)}$ form an orthonormal basis of $H_N$.

The **character vectors** are $\chi_c:=(\omega^{cj})_{j=0}^{N-1}$ for $c=1,\dots,N-1$. They are mean-zero and orthogonal with $\|\chi_c\|^2=N$, and the normalized $\tilde\chi_c:=\chi_c/\sqrt N$ form a second orthonormal basis of $H_N$.

### 2.2 Definition and entry formula

**Definition 2.1.** The *apex unitary at level $N$* is the change-of-basis matrix $U_N\in\mathbb C^{(N-1)\times(N-1)}$ with entries
$$(U_N)_{kc}:=\langle\tilde\chi_c,e_k\rangle=\frac1{\sqrt{Nk(k+1)}}\Big(\sum_{j=0}^{k-1}\omega^{cj}-k\,\omega^{ck}\Big),\qquad k,c\in\{1,\dots,N-1\}.$$

Because $e_k$ is real, $(U_N)_{kc}=R_k\sum_j h_k(j)\,\omega^{cj}$ with $R_k:=1/\sqrt{Nk(k+1)}$. Summing the geometric series gives the equivalent closed form (T9)
$$(U_N)_{kc}=R_k\cdot\frac{1-(k+1)\,\omega^{kc}+k\,\omega^{(k+1)c}}{1-\omega^{c}}.\qquad(2.1)$$
Since $U_N$ is the matrix of an orthonormal change of basis, it is unitary: $U_N\in U(N-1)$.

**Remark 2.2 (orientation of the pairing).** The determinant is sensitive to the conjugation convention. Definition 2.1 pairs the character $\tilde\chi_c$ against the real Helmert vector $e_k$, i.e. it is conjugate-linear in the character; equivalently it pairs $h_k$ bilinearly with $\chi_c(j)=\omega^{cj}$. This is the convention reproduced by the closed form $(2.1)$ and by the explicit matrix $(3.1)$ below. The opposite pairing $\langle e_k,\tilde\chi_c\rangle=\overline{(U_N)_{kc}}$ yields the complex-conjugate matrix $\overline{U_N}$, also unitary, with conjugate determinant. We fix the convention of Definition 2.1 once and for all.

### 2.3 The arithmetic field and the radical–cyclotomic split

Let $K_N:=\mathbb Q(\sqrt p:p\le N\text{ prime})$ be the multiquadratic field generated by the square roots of the primes up to $N$, and let $\mathbb Q(\zeta_N)$ be the $N$-th cyclotomic field. The compositum $L_N:=K_N\cdot\mathbb Q(\zeta_N)$ contains every entry of $U_N$.

**Proposition 2.3 (radical–cyclotomic split).** Each entry factors as
$$(U_N)_{kc}=R_k\,C_{kc},\qquad R_k=\frac1{\sqrt{Nk(k+1)}}\in K_N,\qquad C_{kc}=\frac{1-(k+1)\omega^{kc}+k\omega^{(k+1)c}}{1-\omega^{c}}\in\mathbb Z[\omega]\subset\mathbb Q(\zeta_N).\qquad(2.2)$$
The radical factor $R_k$ depends only on the row index $k$ and lies in the real multiquadratic field; the cyclotomic factor $C_{kc}$ is an algebraic integer in $\mathbb Q(\zeta_N)$.

*Proof.* Immediate from $(2.1)$: $R_k$ is a real quadratic radical, and clearing the denominator $1-\omega^c$ in the geometric sum shows $C_{kc}=\sum_{j=0}^{k-1}\omega^{cj}-k\,\omega^{ck}\in\mathbb Z[\omega]$. $\square$

### 2.4 The degree of the compositum

The two factors of $L_N$ overlap in a multiquadratic field: a square root $\sqrt m$ (for $m\mid\prod_{p\le N}p$ squarefree) lies in $\mathbb Q(\zeta_N)$ exactly when the conductor of $\mathbb Q(\sqrt m)$ divides $N$, where $\operatorname{cond}(\mathbb Q(\sqrt m))=m$ if $m\equiv1\pmod4$ and $4m$ otherwise. The set of such $m$ forms an $\mathbb F_2$-vector space under multiplication modulo squares; let $t(N)$ be its dimension, so that $[K_N\cap\mathbb Q(\zeta_N):\mathbb Q]=2^{t(N)}$. By the degree formula for composita,
$$d(N):=[L_N:\mathbb Q]=\frac{[K_N:\mathbb Q]\,[\mathbb Q(\zeta_N):\mathbb Q]}{[K_N\cap\mathbb Q(\zeta_N):\mathbb Q]}=\frac{2^{\pi(N)}\,\varphi(N)}{2^{t(N)}}.$$

**Table 2.1.** The compositum degree for small $N$.

| $N$ | $\pi(N)$ | $\varphi(N)$ | $t(N)$ | $K_N\cap\mathbb Q(\zeta_N)$ | $d(N)$ |
|---|---|---|---|---|---|
| $2$ | $1$ | $1$ | $0$ | $\mathbb Q$ | $2$ |
| $3$ | $2$ | $2$ | $0$ | $\mathbb Q$ | $8$ |
| $4$ | $2$ | $2$ | $0$ | $\mathbb Q$ | $8$ |
| $5$ | $3$ | $4$ | $1$ | $\mathbb Q(\sqrt5)$ | $16$ |
| $6$ | $3$ | $2$ | $0$ | $\mathbb Q$ | $16$ |
| $7$ | $4$ | $6$ | $0$ | $\mathbb Q$ | $96$ |
| $8$ | $4$ | $4$ | $1$ | $\mathbb Q(\sqrt2)$ | $32$ |
| $30$ | $10$ | $8$ | $1$ | $\mathbb Q(\sqrt5)$ | $4096$ |

The sequence $d(N)$ is irregular: $d(7)=96$ dwarfs its neighbours because the real subfield of $\mathbb Q(\zeta_7)$ is cubic and therefore shares no quadratic subfield with any multiquadratic $K_N$, so $t(7)=0$.

---

## 3. Invariants at level four

We compute the determinant, trace, and characteristic polynomial of $U_4$. Here $\omega=i$ and, writing out $(2.1)$,
$$U_4=\begin{pmatrix}\dfrac{1-i}{2\sqrt 2}&\dfrac{1}{\sqrt 2}&\dfrac{1+i}{2\sqrt 2}\\[8pt] \dfrac{3+i}{2\sqrt 6}&\dfrac{-1}{\sqrt 6}&\dfrac{3-i}{2\sqrt 6}\\[8pt] \dfrac{i}{\sqrt 3}&\dfrac{1}{\sqrt 3}&\dfrac{-i}{\sqrt 3}\end{pmatrix}.\qquad(3.1)$$
Its entries lie in $\mathbb Q(\sqrt2,\sqrt3,i)=L_4$, of degree $8$ over $\mathbb Q$ (here $\sqrt6=\sqrt2\,\sqrt3$).

### 3.1 The determinant

**Proposition 3.1.** $\det U_4=i$.

*Proof.* Factor the common radical out of each row of $(3.1)$: pulling $1/(2\sqrt2)$, $1/(2\sqrt6)$, $1/\sqrt3$ from rows $1,2,3$ respectively leaves the integer matrix
$$M=\begin{pmatrix}1-i&2&1+i\\ 3+i&-2&3-i\\ i&1&-i\end{pmatrix},$$
and the product of the extracted scalars is $\dfrac{1}{2\sqrt2}\cdot\dfrac1{2\sqrt6}\cdot\dfrac1{\sqrt3}=\dfrac1{4\sqrt{36}}=\dfrac1{24}$. Expanding $\det M$ along the third row,
$$\det M=i\begin{vmatrix}2&1+i\\-2&3-i\end{vmatrix}-\begin{vmatrix}1-i&1+i\\3+i&3-i\end{vmatrix}-i\begin{vmatrix}1-i&2\\3+i&-2\end{vmatrix}=i(8)-(-8i)-i(-8)=24i.$$
Hence $\det U_4=\tfrac1{24}\det M=\tfrac{24i}{24}=i$. $\square$

The radicals $\sqrt2,\sqrt3,\sqrt6$ that appear throughout $(3.1)$ cancel completely: $\det U_4=i\in\mathbb Q(\zeta_4)$ carries no multiquadratic content. Section 4.4 gives the structural reason; the general statement, $\det U_N=i^{-\binom{N-1}{2}}$, is proved in [N2], of which Proposition 3.1 is the case $N=4$.

### 3.2 The trace and its field trace

Summing the diagonal of $(3.1)$ and rationalizing,
$$\operatorname{tr}U_4=\frac{1-i}{2\sqrt2}-\frac1{\sqrt6}-\frac i{\sqrt3}=\frac{(3\sqrt2-2\sqrt6)-i\,(3\sqrt2+4\sqrt3)}{12}.\qquad(3.2)$$
Numerically $\operatorname{tr}U_4\approx-0.0547-0.9310\,i$, consistent with $|\operatorname{tr}U_4|<\sqrt3$.

Thus $\operatorname{tr}U_4$ has genuine multiquadratic content: it lies in $L_4\setminus\mathbb Q(\zeta_4)$. Nevertheless its field trace over the cyclotomic part vanishes.

**Proposition 3.2.** $\operatorname{Tr}_{L_4/\mathbb Q(\zeta_4)}(\operatorname{tr}U_4)=0$.

*Proof.* The extension $L_4/\mathbb Q(\zeta_4)$ has degree $4$, since $K_4=\mathbb Q(\sqrt2,\sqrt3)$ is degree $4$ over $\mathbb Q$ and $K_4\cap\mathbb Q(\zeta_4)=\mathbb Q$ (the field $\mathbb Q(\zeta_4)=\mathbb Q(i)$ is imaginary quadratic and contains no real quadratic field). Its Galois group $\mathrm{Gal}(L_4/\mathbb Q(\zeta_4))\cong(\mathbb Z/2)^2$ fixes $i$ and acts by independent sign changes $\sqrt2\mapsto\pm\sqrt2$, $\sqrt3\mapsto\pm\sqrt3$. Summing the four conjugates of $(3.2)$, each of $\sqrt2,\sqrt3,\sqrt6$ occurs with both signs and cancels; hence the field trace is $0$. $\square$

### 3.3 The characteristic polynomial and the spectrum

For a $3\times3$ matrix, $\chi_{U_4}(t)=t^3-(\operatorname{tr}U_4)\,t^2+(\operatorname{tr}\textstyle\bigwedge^2U_4)\,t-\det U_4$. For a unitary matrix $\operatorname{tr}\bigwedge^2U_4=\det U_4\cdot\operatorname{tr}(U_4^{-1})=\det U_4\cdot\overline{\operatorname{tr}U_4}$. With $\det U_4=i$ and $(3.2)$,
$$\chi_{U_4}(t)=t^3-\frac{(3\sqrt2-2\sqrt6)-i\,(3\sqrt2+4\sqrt3)}{12}\,t^2+\frac{-(3\sqrt2+4\sqrt3)+i\,(3\sqrt2-2\sqrt6)}{12}\,t-i,\qquad(3.3)$$
an explicit cubic with coefficients in $L_4$.

**Proposition 3.3.** Not every eigenvalue of $U_4$ is a root of unity, although the product of the eigenvalues is the root of unity $\det U_4=i$.

*Proof.* A sum of roots of unity is an algebraic integer. The element $\operatorname{tr}U_4$ of $(3.2)$ is not an algebraic integer: for instance the component $\sqrt2/4$ has minimal polynomial $16t^2-2$ over $\mathbb Z$, with leading coefficient $>1$, so $\operatorname{tr}U_4\notin\mathcal O_{L_4}$. If all three eigenvalues were roots of unity their sum $\operatorname{tr}U_4$ would be an algebraic integer; hence at least one eigenvalue is not a root of unity. The product of the eigenvalues equals $\det U_4=i$ by Proposition 3.1. $\square$

The explicit factorization of $(3.3)$, and with it the precise position of the three eigenvalues on the unit circle, is not pursued here.

---

## 4. The Galois action on $U_N$

The Galois group of the compositum acts on $U_N$ entry by entry. Through the split $(2.2)$ this action takes a transparent form: the cyclotomic part permutes columns, and the multiquadratic part rescales rows by signs.

### 4.1 The Galois group of the compositum

Write $L_N=K_N\cdot\mathbb Q(\zeta_N)$ and $G_N=\mathrm{Gal}(L_N/\mathbb Q)$. Restriction gives a short exact sequence
$$1\longrightarrow \mathrm{Gal}(L_N/\mathbb Q(\zeta_N))\longrightarrow G_N\longrightarrow(\mathbb Z/N)^\times\longrightarrow 1,$$
where $\mathrm{Gal}(L_N/\mathbb Q(\zeta_N))\cong\mathrm{Gal}(K_N/K_N\cap\mathbb Q(\zeta_N))\cong(\mathbb Z/2)^{\pi(N)-t(N)}$ consists of sign changes on the quadratic radicals not already in $\mathbb Q(\zeta_N)$, and $(\mathbb Z/N)^\times=\mathrm{Gal}(\mathbb Q(\zeta_N)/\mathbb Q)$ acts by $\omega\mapsto\omega^a$. At $N=4$ one has $G_4\cong(\mathbb Z/2)^2\times(\mathbb Z/4)^\times\cong(\mathbb Z/2)^3$ of order $8=d(4)$, generated by $\sigma_2:\sqrt2\mapsto-\sqrt2$, $\sigma_3:\sqrt3\mapsto-\sqrt3$, and $\sigma_{-1}:i\mapsto-i$.

### 4.2 The cyclotomic action: column permutations

Let $\sigma\in G_N$ restrict to $\omega\mapsto\omega^a$, $a\in(\mathbb Z/N)^\times$, and fix the radicals $R_k$ (such $\sigma$ exist precisely as the lifts that act trivially on $K_N$). Then $\sigma(R_k)=R_k$ and, from $(2.2)$, $\sigma(C_{kc})=\sum_j h_k(j)\,\omega^{acj}=C_{k,ac}$. Multiplication by the unit $a$ permutes the index set $\{1,\dots,N-1\}$, so
$$\sigma(U_N)=U_N\,P_a,$$
where $P_a$ is the permutation matrix of $c\mapsto ac$ on $\{1,\dots,N-1\}\subset\mathbb Z/N$.

At $N=4$, $(\mathbb Z/4)^\times=\{1,3\}$ and $\sigma_{-1}$ ($a=3$) swaps columns $1$ and $3$ of $(3.1)$ while fixing column $2$ (the real character $\chi_2(j)=(-1)^j$); direct inspection confirms $\sigma_{-1}(U_4)=U_4\,P_3$.

### 4.3 The multiquadratic action: row sign changes

Let $\tau\in\mathrm{Gal}(L_N/\mathbb Q(\zeta_N))$ fix $\omega$ and act by sign changes on the radicals. Then $\tau$ fixes each $C_{kc}$ and sends $R_k\mapsto\varepsilon_k(\tau)\,R_k$ with $\varepsilon_k(\tau)\in\{\pm1\}$, where $\varepsilon_k(\tau)=-1$ exactly when $\tau$ flips the squarefree part of $Nk(k+1)$. Hence
$$\tau(U_N)=D_\tau\,U_N,\qquad D_\tau=\operatorname{diag}\big(\varepsilon_1(\tau),\dots,\varepsilon_{N-1}(\tau)\big).$$

At $N=4$ the row radicals are $R_1=1/(2\sqrt2)$, $R_2=1/(2\sqrt6)$, $R_3=1/(4\sqrt3)$, so $\sigma_2$ gives $D=\operatorname{diag}(-1,-1,+1)$ and $\sigma_3$ gives $D=\operatorname{diag}(+1,-1,-1)$. For instance $\sigma_2\big((U_4)_{11}\big)=\sigma_2\!\big(\tfrac{1-i}{2\sqrt2}\big)=-\tfrac{1-i}{2\sqrt2}$, consistent with the sign on row $1$.

### 4.4 Cyclotomic rationality of the determinant

Combining the two actions, a general $\sigma\in G_N$ acts by a signed monomial transformation
$$\sigma(U_N)=D_\sigma\,U_N\,P_\sigma,$$
with $D_\sigma$ a diagonal sign matrix and $P_\sigma$ a permutation matrix. Taking determinants,
$$\sigma(\det U_N)=\det(\sigma(U_N))=\det(D_\sigma)\,\det(U_N)\,\operatorname{sgn}(P_\sigma).$$
In particular, $\det U_N$ is fixed by the multiquadratic subgroup $\mathrm{Gal}(L_N/\mathbb Q(\zeta_N))$—equivalently $\det U_N\in\mathbb Q(\zeta_N)$—precisely when $\det(D_\tau)=+1$ for every such $\tau$.

At $N=4$ this holds: $\det D=(-1)(-1)(+1)=+1$ for $\sigma_2$ and $\det D=(+1)(-1)(-1)=+1$ for $\sigma_3$. Thus $\det U_4$ is fixed by $\langle\sigma_2,\sigma_3\rangle$ and lies in $\mathbb Q(\zeta_4)$, which is the structural reason behind the cancellation observed after Proposition 3.1. For general $N$ the sign product $\det(D_\tau)$ need not be $+1$: it is shown in [N2] that $\det U_N\in\mathbb Q(\zeta_N)$ if and only if $N\not\equiv3\pmod4$, the obstruction in the remaining class being a single non-cyclotomic quadratic radical.

---

## 5. Further directions

The family $\{U_N\}$ supports several arithmetic invariants beyond those computed here, each the subject of a subsequent paper in the series.

- **The determinant.** Determined in closed form in [N2]: $\det U_N=i^{-\binom{N-1}{2}}$, a fourth root of unity, lying in $\mathbb Q(\zeta_N)$ exactly when $N\not\equiv3\pmod4$.
- **The trace.** The vanishing of Proposition 3.2 does *not* persist for all $N$. The general field trace is
$$\operatorname{Tr}_{L_N/\mathbb Q(\zeta_N)}(\operatorname{tr}U_N)=2^{\,s}\!\!\sum_{k\in S_N}\!(U_N)_{kk},\qquad s=\pi(N)-t(N),\quad S_N=\{k:\sqrt{\operatorname{sf}(Nk(k+1))}\in\mathbb Q(\zeta_N)\},$$
  obtained by Galois sign-character orthogonality: each $\tau\in\operatorname{Gal}(L_N/\mathbb Q(\zeta_N))$ fixes $C_{kk}$ and rescales $R_k$ by a sign, so $\operatorname{Tr}_{L_N/\mathbb Q(\zeta_N)}\big((U_N)_{kk}\big)=2^s(U_N)_{kk}$ for $k\in S_N$ and $0$ otherwise. Thus the genuinely non-cyclotomic part $\sum_{k\notin S_N}(U_N)_{kk}$ *always* has vanishing field trace — the correct generalization of Proposition 3.2 — while the field trace of $\operatorname{tr}U_N$ itself vanishes iff $\sum_{k\in S_N}(U_N)_{kk}=0$. The case $N=4$ vanishes because $S_4=\varnothing$; the first $N\ge3$ with nonvanishing field trace is $N=5$, where $\operatorname{Tr}_{L_5/\mathbb Q(\zeta_5)}(\operatorname{tr}U_5)=-2\zeta_5$. The power traces $\operatorname{tr}U_N^m$ governing the characteristic-polynomial coefficients are a natural next object.
- **The spectrum.** Proposition 3.3 shows the spectrum need not consist of roots of unity. Its conductor-block structure for composite $N$, and its description at prime $N$ via Gauss sums, are natural next objects. The global spectral concentration at the fourth roots of unity is established in [N3], and the controlling edge mode is identified in [N4] as an archimedean operator — the half-line Fourier transform dressed by the Hardy averaging operator — whose even sector is the Riemann–Siegel scattering multiplier; thus the spectral side of $\{U_N\}$ is the operator-theoretic incarnation of the archimedean place.
- **The Galois module.** The signed monomial action of Section 4 makes $\{U_N\}$ a module over $G_N$; its orbit structure and Galois-stable invariants connect the spectral data to the cyclotomic units and real class numbers of $\mathbb Q(\zeta_N)$.

---

## References

[N2] Murillo Montero, L. (2026). *The Apex Determinant: A Closed Form via Helmert–Fourier Factorization.* First draft, June 5, 2026.

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary: A Structural Reduction.* First draft, June 5, 2026.

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* First draft, June 5, 2026.

[T9] Murillo Montero, L. (2026). *The Helmert–Fourier Transfer Matrix.* First draft, May 26, 2026.

Lang, S. (2002). *Algebra.* Revised third edition. Graduate Texts in Mathematics 211. Springer.

Washington, L. C. (1997). *Introduction to Cyclotomic Fields.* Second edition. Graduate Texts in Mathematics 83. Springer.
