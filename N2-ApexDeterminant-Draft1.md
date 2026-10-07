# N2 — The Apex Determinant: A Closed Form via Helmert–Fourier Factorization

**Leonardo Murillo Montero**

*June 5, 2026*

<!--
Program record (not part of the paper). Companion to
N1-ApexUnitaries-Draft1.md. Every assertion below is certified by exact
or 50-digit deterministic computation:
  empirical/probe_apex_convention_N1.py     (operative convention)
  empirical/probe_apex_determinant_N1.py    (det U_N = i^{-C(N-1,2)}, N<=30)
  empirical/probe_determinant_proof_N1.py   (Lemmas A,B,C + assembly)
  empirical/probe_helmert_lemmaB_N1.py      (det Htilde recursion, exact)
  empirical/probe_r_p_parity_N1.py          (conductor criterion for Cor 6.4)
The closed form (2.1) for the entries is from T9 (Helmert–Fourier transfer
matrix); this paper studies the matrix as an arithmetic object and is
self-contained from Section 2 onward.
-->

---

## Abstract

For each integer $N\ge 2$ let $U_N\in U(N-1)$ be the unitary matrix that intertwines the normalized Helmert basis and the nontrivial additive characters of $\mathbb Z/N$ on the mean-zero hyperplane of $\mathbb C^N$. We prove the closed form
$$\det U_N=i^{-\binom{N-1}{2}},$$
exhibiting the determinant as a fourth root of unity that depends only on $N$ modulo $8$. The proof realizes $U_N$ as the nontrivial diagonal block of the product $H F^{\mathsf T}$ of the full $N\times N$ Helmert matrix $H$ and the symmetric Fourier matrix $F$, which reduces $\det U_N$ to $\det H\cdot\det F$. We evaluate $\det H=(-1)^{N-1}$ in closed form by a cofactor recursion, and recall Schur's evaluation of the Fourier determinant. As arithmetic consequences we determine the exact field of the determinant: $\det U_N$ is a fourth root of unity for every $N$, equals $\pm 1$ when $N\equiv 1,2\pmod 4$ and $\pm i$ when $N\equiv 0,3\pmod 4$, and lies in the cyclotomic field $\mathbb Q(\zeta_N)$ if and only if $N\not\equiv 3\pmod 4$. The period-$8$ dependence on $N$ refines Schur's period-$4$ formula by exactly the Helmert reflection sign.

---

## 1. Introduction

The matrix studied here arises as the change of basis, on the mean-zero hyperplane of $\mathbb C^N$, between two natural orthonormal frames: the real Helmert frame, built from the nested contrasts $(1,\dots,1,-k,0,\dots,0)$, and the complex Fourier frame of nontrivial additive characters of $\mathbb Z/N$. The resulting unitary $U_N\in U(N-1)$ has entries in the compositum $K_N\cdot\mathbb Q(\zeta_N)$ of the multiquadratic field $K_N=\mathbb Q(\sqrt p:p\le N)$ and the cyclotomic field $\mathbb Q(\zeta_N)$; its entries individually carry both quadratic-radical and cyclotomic content. The companion paper [N1] establishes the basic structure of the family $\{U_N\}$ and computes $\det U_4=i$ by direct expansion.

This paper determines $\det U_N$ for all $N$ in closed form.

**Theorem 1.1.** For every integer $N\ge 2$,
$$\det U_N=i^{-\binom{N-1}{2}}=i^{-(N-1)(N-2)/2}.$$

In particular $\det U_N\in\{1,-1,i,-i\}$ for every $N$, and the value is periodic with period $8$ in $N$:

| $N\bmod 8$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|---|---|---|---|---|---|---|---|---|
| $\det U_N$ | $-i$ | $1$ | $1$ | $-i$ | $i$ | $-1$ | $-1$ | $i$ |

The proof is a factorization. Embedding $U_N$ into the full $N\times N$ Helmert and Fourier matrices realizes it as a diagonal block of their product (Proposition 3.1), so that $\det U_N=\det H\cdot\det F$. The Helmert factor is an elementary sign, $\det H=(-1)^{N-1}$ (Lemma 4.1), and the Fourier factor is the classical Schur determinant of the discrete Fourier transform (Lemma 5.1). Assembling the two and reducing the exponent modulo $4$ yields Theorem 1.1 (Section 6).

The closed form has clean arithmetic corollaries. The determinant is always a fourth root of unity (Corollary 7.1); it is real ($\pm1$) exactly for $N\equiv 1,2\pmod 4$ and imaginary ($\pm i$) exactly for $N\equiv 0,3\pmod 4$ (Corollary 7.2); and although every entry of $U_N$ involves quadratic radicals, the determinant lies in the cyclotomic field $\mathbb Q(\zeta_N)$ precisely when $N\not\equiv 3\pmod 4$ (Corollary 7.4). The last statement isolates the single residue class on which the multiquadratic content of the entries fails to cancel within $\mathbb Q(\zeta_N)$, and we identify the obstruction with the conductor of an explicit quadratic field (Proposition 7.5).

Throughout, $\omega=e^{2\pi i/N}$ and $\zeta_m=e^{2\pi i/m}$. We write $\binom{n}{2}=n(n-1)/2$.

---

## 2. The apex unitary

We fix the conventions used for the rest of the paper. They agree with the closed form of [N1, T9] and with the explicit matrices computed there.

### 2.1 Two orthonormal frames of the hyperplane

Let $H_N:=\{v\in\mathbb C^N:\sum_{j=0}^{N-1}v_j=0\}$, with the standard Hermitian inner product $\langle u,v\rangle=\sum_j u_j\overline{v_j}$.

The **Helmert vectors** $h_k$ ($k=1,\dots,N-1$) consist of $k$ leading ones, then the entry $-k$, then $N-1-k$ trailing zeros:
$$h_k:=(\,1,\dots,1,\,-k,\,0,\dots,0\,)\in\mathbb Z^N,\qquad k=1,\dots,N-1,$$
which are real, mutually orthogonal, mean-zero, with $\|h_k\|^2=k(k+1)$; the normalized vectors $e_k:=h_k/\sqrt{k(k+1)}$ form an orthonormal basis of $H_N$.

The **character vectors** are $\chi_c:=(\omega^{cj})_{j=0}^{N-1}$ for $c=1,\dots,N-1$; they are mean-zero and orthogonal, with $\|\chi_c\|^2=N$, and the normalized $\tilde\chi_c:=\chi_c/\sqrt N$ form a second orthonormal basis of $H_N$.

### 2.2 Definition and entry formula

**Definition 2.1.** The *apex unitary at level $N$* is the change-of-basis matrix $U_N\in\mathbb C^{(N-1)\times(N-1)}$ with entries
$$(U_N)_{kc}:=\langle \tilde\chi_c,e_k\rangle=\frac{1}{\sqrt{Nk(k+1)}}\left(\sum_{j=0}^{k-1}\omega^{cj}-k\,\omega^{ck}\right),\qquad k,c\in\{1,\dots,N-1\}.$$

Because $e_k$ is real, $\langle\tilde\chi_c,e_k\rangle=\frac1{\sqrt N}\sum_j\omega^{cj}\,(e_k)_j=R_k\sum_j h_k(j)\,\omega^{cj}$, where
$$R_k:=\frac{1}{\sqrt{Nk(k+1)}}.$$
Summing the geometric series gives the equivalent closed form
$$\boxed{\;(U_N)_{kc}=R_k\cdot\frac{1-(k+1)\,\omega^{kc}+k\,\omega^{(k+1)c}}{1-\omega^{c}}\;}\qquad(2.1)$$
used throughout. Since $U_N$ is the matrix of an orthonormal change of basis, $U_N\in U(N-1)$.

**Remark 2.2 (orientation of the pairing).** The determinant is sensitive to the conjugation convention. Definition 2.1 pairs the *character* $\tilde\chi_c$ against the (real) Helmert vector $e_k$, i.e. it is conjugate-linear in the character; equivalently it pairs $h_k$ bilinearly with $\chi_c(j)=\omega^{cj}$. This is the convention reproduced by the closed form $(2.1)$ and by the explicit level-$4$ matrix of [N1]. The opposite pairing $\langle e_k,\tilde\chi_c\rangle=\overline{(U_N)_{kc}}$ yields the complex-conjugate matrix $\overline{U_N}$, which is also unitary but has $\det\overline{U_N}=\overline{\det U_N}$; the two conventions differ by complex conjugation and hence give determinants $i^{\mp\binom{N-1}{2}}$.

### 2.3 The radical–cyclotomic split

Each entry factors as $(U_N)_{kc}=R_k\,C_{kc}$ with $R_k\in K_N$ depending only on $k$, and
$$C_{kc}=\frac{1-(k+1)\omega^{kc}+k\omega^{(k+1)c}}{1-\omega^{c}}\in\mathbb Z[\omega]\subset\mathbb Q(\zeta_N).$$
Thus the quadratic radicals enter only through the row scalars $R_k$, and the cyclotomic content only through the integer matrix $C=(C_{kc})$. This split governs the field of the determinant in Section 7.

---

## 3. The block factorization

We pass to the full $N\times N$ picture, including the mean direction and the trivial character.

Let $H$ be the **full normalized Helmert matrix**: its rows, indexed $0,1,\dots,N-1$, are
$$\text{row }0=\tfrac1{\sqrt N}(1,\dots,1),\qquad \text{row }k=e_k\ (1\le k\le N-1).$$
$H$ is real orthogonal. Let $F$ be the **symmetric unitary Fourier matrix**
$$F_{cj}=\frac{\omega^{cj}}{\sqrt N},\qquad c,j=0,\dots,N-1,$$
so $F=F^{\mathsf T}$ and $F$ is unitary.

**Proposition 3.1 (block factorization).** The product $M:=HF^{\mathsf T}$ has the block form
$$M=\begin{pmatrix}1 & 0\\[2pt] 0 & U_N\end{pmatrix},$$
where the upper-left entry is the $(0,0)$ scalar, the off-diagonal blocks are zero, and the trailing $(N-1)\times(N-1)$ block is $U_N$ in the convention of Definition 2.1. Consequently
$$\det U_N=\det M=\det H\cdot\det F.$$

*Proof.* For $0\le r,c\le N-1$,
$$M_{rc}=\sum_{j=0}^{N-1}H_{rj}\,F_{cj}=\sum_{j}H_{rj}\,\frac{\omega^{cj}}{\sqrt N}.$$

*Row $0$.* With $H_{0j}=1/\sqrt N$, $M_{0c}=\frac1N\sum_{j}\omega^{cj}=\delta_{c0}$, since $\sum_j\omega^{cj}=N$ for $c\equiv0$ and $0$ otherwise.

*Column $0$.* With $F_{0j}=1/\sqrt N$, $M_{r0}=\frac1{\sqrt N}\sum_j H_{rj}$. The row sums of $H$ are $\sum_j H_{0j}=\sqrt N$ and, for $k\ge1$, $\sum_j H_{kj}=\frac{1}{\sqrt{k(k+1)}}\sum_j h_k(j)=0$. Hence $M_{00}=1$ and $M_{k0}=0$ for $k\ge1$.

*Trailing block.* For $k,c\ge1$,
$$M_{kc}=\sum_j\frac{h_k(j)}{\sqrt{k(k+1)}}\cdot\frac{\omega^{cj}}{\sqrt N}=R_k\sum_j h_k(j)\,\omega^{cj}=(U_N)_{kc}$$
by Definition 2.1. Therefore $M=1\oplus U_N$, and $\det M=\det U_N$. Finally $\det M=\det H\,\det F^{\mathsf T}=\det H\,\det F$. $\square$

This is the precise sense in which $U_N$ is "the discrete Fourier transform restricted to nontrivial modes, read in the Helmert frame": the mean mode and the trivial character split off as the $1\times1$ corner, and what remains is exactly $U_N$.

---

## 4. The Helmert determinant

**Lemma 4.1.** $\det H=(-1)^{N-1}$.

*Proof.* Write $H=D\,\tilde H$, where $D=\operatorname{diag}\!\big(1/\sqrt N,\,1/\sqrt{1\cdot2},\,\dots,\,1/\sqrt{(N-1)N}\big)$ and $\tilde H$ is the integer matrix with row $0=(1,\dots,1)$ and row $k=h_k$ for $1\le k\le N-1$. Then $\det H=\det D\cdot\det\tilde H$.

*The scalar.* Using $\prod_{k=1}^{N-1}k(k+1)=(N-1)!\,N!$ and $N\cdot(N-1)!=N!$,
$$\det D=\Big(N\prod_{k=1}^{N-1}k(k+1)\Big)^{-1/2}=\big((N!)^2\big)^{-1/2}=\frac1{N!}.$$

*The integer determinant.* We claim
$$\det\tilde H_N=(-1)^{N-1}N!.\qquad(4.1)$$
We prove $(4.1)$ by establishing the exact recursion $\det\tilde H_N=-N\,\det\tilde H_{N-1}$ for $N\ge 2$, with base $\det\tilde H_1=1$.

Expand $\det\tilde H_N$ along the last column (column $N-1$). Its entries are: $1$ in row $0$ (the all-ones row); $0$ in rows $1,\dots,N-2$ (the vector $h_k$ is supported on columns $0,\dots,k$ with $k\le N-2$); and $-(N-1)$ in row $N-1$ (the pivot of $h_{N-1}$). Hence the Laplace expansion has only two terms,
$$\det\tilde H_N=1\cdot(-1)^{0+(N-1)}\,M_{0,N-1}\;+\;\big(-(N-1)\big)\cdot(-1)^{(N-1)+(N-1)}\,M_{N-1,N-1},\qquad(4.2)$$
where $M_{r,c}$ denotes the $(r,c)$ minor and $(-1)^{2(N-1)}=1$.

The minor $M_{N-1,N-1}$ deletes the last row and column, leaving rows $0,\dots,N-2$ over columns $0,\dots,N-2$. Row $0$ is the all-ones row of length $N-1$, and each $h_k$ with $1\le k\le N-2$ is unchanged (its support lies in columns $0,\dots,k$). This is exactly $\tilde H_{N-1}$:
$$M_{N-1,N-1}=\det\tilde H_{N-1}.$$

The minor $M_{0,N-1}$ deletes row $0$ and the last column, leaving rows $1,\dots,N-1$ over columns $0,\dots,N-2$. The rows $h_1,\dots,h_{N-2}$ are unchanged; the row $h_{N-1}=(1,\dots,1,-(N-1))$ loses its last entry, becoming the all-ones row of length $N-1$. Thus this block has rows $(h_1,\dots,h_{N-2},\mathbf 1)$, while $\tilde H_{N-1}$ has rows $(\mathbf 1,h_1,\dots,h_{N-2})$. The two differ by moving the top row past the $N-2$ rows below it, i.e. by $N-2$ transpositions, so
$$M_{0,N-1}=(-1)^{N-2}\det\tilde H_{N-1}.$$

Substituting into $(4.2)$ and using $(-1)^{(N-1)+(N-2)}=(-1)^{2N-3}=-1$,
$$\det\tilde H_N=(-1)^{N-1}(-1)^{N-2}\det\tilde H_{N-1}-(N-1)\det\tilde H_{N-1}=-\det\tilde H_{N-1}-(N-1)\det\tilde H_{N-1}=-N\,\det\tilde H_{N-1}.$$
With $\det\tilde H_1=1$ this telescopes to $\det\tilde H_N=\prod_{m=2}^N(-m)=(-1)^{N-1}N!$, proving $(4.1)$.

Therefore $\det H=\det D\cdot\det\tilde H_N=\frac1{N!}\cdot(-1)^{N-1}N!=(-1)^{N-1}$. $\square$

---

## 5. The Fourier determinant

The determinant of the symmetric Fourier matrix is classical (Schur, 1921). We record the evaluation in the unreduced form that is convenient for assembly.

**Lemma 5.1.** $\det F=i^{\,E_N}$, where $E_N=\binom N2+(N-1)^2=\dfrac{N(N-1)}2+(N-1)^2$.

*Proof.* Let $V=\sqrt N\,F$, so $V_{cj}=\omega^{cj}=(\omega^c)^{\,j}$ is the Vandermonde matrix in the nodes $\omega^0,\omega^1,\dots,\omega^{N-1}$. Hence
$$\det V=\prod_{0\le a<b\le N-1}(\omega^{b}-\omega^{a}).$$
Using $e^{i\theta}-1=2i\sin(\theta/2)\,e^{i\theta/2}$ with $\theta=2\pi(b-a)/N$,
$$\omega^{b}-\omega^{a}=\omega^{a}\big(\omega^{b-a}-1\big)=2i\,\sin\!\frac{\pi(b-a)}{N}\;e^{\,i\pi(a+b)/N}.$$
There are $\binom N2$ factors, so
$$\det V=(2i)^{\binom N2}\Big(\prod_{a<b}\sin\tfrac{\pi(b-a)}{N}\Big)\exp\!\Big(\frac{i\pi}{N}\sum_{a<b}(a+b)\Big).$$
Each index appears in $N-1$ unordered pairs, whence $\sum_{a<b}(a+b)=(N-1)\sum_{m=0}^{N-1}m=\tfrac{N(N-1)^2}{2}$, and the exponential equals $e^{\,i\pi(N-1)^2/2}=i^{(N-1)^2}$. Separating the modulus from the phase,
$$\det V=\rho_N\cdot i^{\binom N2}\cdot i^{(N-1)^2},\qquad \rho_N:=2^{\binom N2}\prod_{a<b}\sin\tfrac{\pi(b-a)}{N}\ >\ 0.$$
The factor $\rho_N$ is a positive real number; since $V=\sqrt N\,F$ with $F$ unitary, its value is $\rho_N=|\det V|=(\sqrt N)^{N}=N^{N/2}$. Therefore
$$\det V=N^{N/2}\,i^{\binom N2+(N-1)^2},\qquad \det F=\frac{\det V}{N^{N/2}}=i^{\binom N2+(N-1)^2}=i^{\,E_N}. \qquad\square$$

(Each $\sin\frac{\pi m}{N}$ with $1\le m\le N-1$ is positive, so the modulus is fixed by unitarity and no sign ambiguity enters; only the explicit phase $i^{E_N}$ remains.)

---

## 6. Proof of Theorem 1.1

Combining Proposition 3.1 with Lemmas 4.1 and 5.1,
$$\det U_N=\det H\cdot\det F=(-1)^{N-1}\,i^{\,E_N}=i^{\,2(N-1)+E_N},$$
since $(-1)^{N-1}=i^{2(N-1)}$. It remains to reduce the exponent modulo $4$ to the target $-\binom{N-1}{2}$. Compute the difference exactly as a polynomial in $N$:
$$\Big(2(N-1)+E_N\Big)-\Big(-\tbinom{N-1}{2}\Big)=2(N-1)+\frac{N(N-1)}2+(N-1)^2+\frac{(N-1)(N-2)}2.$$
The two half-integer terms combine to $\frac{(N-1)\big(N+(N-2)\big)}2=(N-1)^2$, so the difference equals
$$2(N-1)+2(N-1)^2=2(N-1)\big(1+(N-1)\big)=2N(N-1).$$
Because $N(N-1)$ is a product of consecutive integers it is even, hence $2N(N-1)\equiv 0\pmod 4$. As $i$ has order $4$,
$$\det U_N=i^{\,2(N-1)+E_N}=i^{-\binom{N-1}{2}}.\qquad\blacksquare$$

As a check, at $N=4$: $\det H=(-1)^3=-1$, $E_4=6+9=15$, $\det F=i^{15}=-i$, so $\det U_4=(-1)(-i)=i$, agreeing with the direct computation of [N1].

---

## 7. Arithmetic consequences

We record the consequences of Theorem 1.1 for the value, the periodicity, and the field of the determinant. Write $D_N:=\binom{N-1}{2}=\frac{(N-1)(N-2)}{2}$, so $\det U_N=i^{-D_N}$.

**Corollary 7.1 (torsion).** For every $N\ge2$, $\det U_N$ is a fourth root of unity; in particular $U_N$ has determinant of finite order dividing $4$, and $\det U_N\in\{1,-1,i,-i\}$.

*Proof.* Immediate from $\det U_N=i^{-D_N}$ with $D_N\in\mathbb Z$. $\square$

**Corollary 7.2 (real vs. imaginary).** $\det U_N\in\{1,-1\}$ if $N\equiv 1,2\pmod 4$, and $\det U_N\in\{i,-i\}$ if $N\equiv 0,3\pmod 4$. Equivalently, $\det U_N$ is imaginary iff $D_N$ is odd.

*Proof.* $\det U_N=i^{-D_N}$ is real iff $D_N$ is even and imaginary iff $D_N$ is odd. Reducing $D_N=\frac{(N-1)(N-2)}2$ modulo $2$ by cases on $N\bmod 4$: for $N\equiv1$, $N-1\equiv0\ (4)$ so $D_N$ is even; for $N\equiv2$, $N-2\equiv0\ (4)$ so $D_N$ is even; for $N\equiv0$, $(N-1)$ is odd and $(N-2)/2$ is odd, so $D_N$ is odd; for $N\equiv3$, both $(N-1)/2$ and $N-2$ are odd, so $D_N$ is odd. $\square$

**Corollary 7.3 (periodicity).** The map $N\mapsto\det U_N$ has minimal period $8$ in $N$, as tabulated in Section 1.

*Proof.* $\det U_N$ depends only on $D_N\bmod 4$, and $D_N=\binom{N-1}{2}$ is a quadratic in $N$; a quadratic modulo $4$ has period dividing $8$, and the tabulated values show all eight residues are realized, so the period is exactly $8$. $\square$

We now turn to the field generated by the determinant. Recall that the group of roots of unity contained in $\mathbb Q(\zeta_N)$ is $\mu_N$ if $N$ is even and $\mu_{2N}$ if $N$ is odd; in particular $i\in\mathbb Q(\zeta_N)$ if and only if $4\mid N$.

**Corollary 7.4 (cyclotomic field of the determinant).** $\det U_N\in\mathbb Q(\zeta_N)$ if and only if $N\not\equiv 3\pmod 4$. In the exceptional case $N\equiv 3\pmod 4$ one has $\det U_N=\pm i\in\mathbb Q(\zeta_4)\setminus\mathbb Q(\zeta_N)$, and $\det U_N\in\mathbb Q(\zeta_{4N})$.

*Proof.* By Corollary 7.2, $\det U_N\in\{\pm1\}\subset\mathbb Q\subset\mathbb Q(\zeta_N)$ when $N\equiv1,2\pmod4$. When $N\equiv0,3\pmod4$ we have $\det U_N=\pm i$, which lies in $\mathbb Q(\zeta_N)$ iff $i\in\mathbb Q(\zeta_N)$ iff $4\mid N$. Among $N\equiv0,3\pmod4$ this holds for $N\equiv0$ and fails for $N\equiv3$. Combining the cases, $\det U_N\notin\mathbb Q(\zeta_N)$ exactly when $N\equiv3\pmod4$. There $\det U_N=\pm i\in\mathbb Q(\zeta_4)$, and $\mathbb Q(\zeta_4),\mathbb Q(\zeta_N)\subseteq\mathbb Q(\zeta_{4N})$. $\square$

Corollary 7.4 is striking in view of the entry structure of $U_N$: every entry carries multiquadratic radicals through the scalars $R_k$, yet the determinant collapses to a fourth root of unity that is cyclotomically clean except on a single residue class. The next proposition locates the obstruction precisely, in terms of the squarefree part of an explicit integer.

**Proposition 7.5 (the radical obstruction).** Let
$$P_N:=\prod_{k=1}^{N-1}N k(k+1)=N^{\,N-1}\,(N-1)!\,N!,$$
and let $\operatorname{sf}(P_N)$ denote its squarefree part. Then
$$\det U_N\in\mathbb Q(\zeta_N)\iff \sqrt{\operatorname{sf}(P_N)}\in\mathbb Q(\zeta_N)\iff \operatorname{cond}\!\big(\mathbb Q(\sqrt{\operatorname{sf}(P_N)})\big)\mid N,$$
where $\operatorname{cond}(\mathbb Q(\sqrt m))=m$ if $m\equiv1\pmod4$ and $4m$ otherwise (and $1$ if $m=1$). In particular, combined with Corollary 7.4, the conductor divides $N$ precisely when $N\not\equiv3\pmod4$.

*Proof.* By the split of Section 2.3, $\det U_N=\big(\prod_{k=1}^{N-1}R_k\big)\det C$ with $\det C\in\mathbb Q(\zeta_N)$, since $C$ has entries in $\mathbb Z[\omega]$. The scalar is
$$\prod_{k=1}^{N-1}R_k=\prod_{k=1}^{N-1}\frac1{\sqrt{Nk(k+1)}}=\frac1{\sqrt{P_N}}=\frac{1}{q\sqrt{\operatorname{sf}(P_N)}}$$
for a positive rational $q$ (write $P_N=q^2\operatorname{sf}(P_N)$). As $U_N$ is unitary, $\det C=\det U_N\cdot q\sqrt{\operatorname{sf}(P_N)}\ne 0$. Hence $\det U_N=\det C/(q\sqrt{\operatorname{sf}(P_N)})$ lies in $\mathbb Q(\zeta_N)$ iff $\sqrt{\operatorname{sf}(P_N)}\in\mathbb Q(\zeta_N)$, because $\det C\in\mathbb Q(\zeta_N)$ and the field is closed under nonzero division. The quadratic field $\mathbb Q(\sqrt m)$ is contained in $\mathbb Q(\zeta_N)$ iff its conductor divides $N$, by the conductor–discriminant correspondence for quadratic subfields of cyclotomic fields; this gives the stated conductor criterion. The final clause is Corollary 7.4. $\square$

Proposition 7.5 is the precise form of the "radicals cancel" phenomenon: the multiquadratic radicals appearing throughout the entries of $U_N$ contribute to the determinant only through the single radical $\sqrt{\operatorname{sf}(P_N)}$, and this radical is cyclotomic—so the determinant is cyclotomically clean—exactly when $N\not\equiv3\pmod4$. The criterion is genuinely about the *combined* radical $\sqrt{\operatorname{sf}(P_N)}$ rather than its prime factors individually: distinct non-cyclotomic prime radicals may combine into a cyclotomic one, as at $N=21$, where $\operatorname{sf}(P_{21})=21\equiv1\pmod4$ has conductor $21\mid 21$ even though neither $\sqrt3$ nor $\sqrt7$ lies in $\mathbb Q(\zeta_{21})$.

**Remark 7.6 (relation to Schur's formula).** Schur's determinant $\det F=i^{E_N}$ depends on $N$ only modulo $4$ (the exponent $E_N=\binom N2+(N-1)^2$ is quadratic in $N$, but its parity pattern realizes only four values). The apex determinant $\det U_N=i^{-D_N}$ depends on $N$ modulo $8$ (Corollary 7.3). The refinement from period $4$ to period $8$ is supplied entirely by the Helmert reflection sign $(-1)^{N-1}=i^{2(N-1)}$, whose exponent $2(N-1)$ is the odd-order term that doubles the period. Thus the additional arithmetic content of $U_N$ over the bare Fourier transform is exactly one factor of the orientation of the real Helmert frame.

---

## 8. Summary

The determinant of the apex unitary is the fourth root of unity $\det U_N=i^{-\binom{N-1}{2}}$, established by the factorization $\det U_N=\det H\cdot\det F$ into an elementary Helmert sign and Schur's Fourier determinant. The value is periodic of period $8$ in $N$; it is a square root of unity for $N\equiv1,2\pmod4$ and a primitive fourth root for $N\equiv0,3\pmod4$; and it is cyclotomically clean—lying in $\mathbb Q(\zeta_N)$—if and only if $N\not\equiv3\pmod4$, the obstruction in the remaining class being the single radical $\sqrt{\operatorname{sf}(N^{N-1}(N-1)!\,N!)}$.

The trace and the spectrum of $U_N$, whose analysis is governed by the conductor decomposition of $\mathbb Z/N$ rather than by a single determinantal sign, are taken up in subsequent papers of the series: the spectral concentration at the fourth roots of unity in [N3], and the identification of its controlling edge mode with an archimedean operator in [N4].

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family $\{U_N\}_{N\ge2}$ in $U(N-1)$ over Multiquadratic–Cyclotomic Compositums.* First draft, May 28, 2026.

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary: A Structural Reduction.* First draft, June 5, 2026.

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* First draft, June 5, 2026.

[T9] Murillo Montero, L. (2026). *The Helmert–Fourier Transfer Matrix.* First draft, May 26, 2026.

Lang, S. (2002). *Algebra.* Revised third edition. Graduate Texts in Mathematics 211. Springer.

Schur, I. (1921). Über die Gauss'schen Summen. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 147–153.

Washington, L. C. (1997). *Introduction to Cyclotomic Fields.* Second edition. Graduate Texts in Mathematics 83. Springer.
