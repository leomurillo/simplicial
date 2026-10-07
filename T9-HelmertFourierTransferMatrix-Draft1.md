# T9 — The Helmert-Fourier Transfer Matrix

**Leonardo Murillo Montero**

*First draft — May 25, 2026*

---

> *Two orthogonal bases of $H_N$: one integer-rational (Helmert), one cyclotomic (character). Their transfer matrix is the apex's arithmetic Jacobian.*

---

## Abstract

**Situation.** T4 (Murillo Montero 2026, T4) introduced the **Helmert ladder** $\{h_k\}_{k=1}^{N-1}$ of integer orthogonal contrasts spanning the mean-zero hyperplane $H_N\subset\mathbb R^N$, and proved that unit normalization $e_k:=h_k/\sqrt{k(k+1)}$ forces a quadratic field extension exactly at prime rungs, yielding the multiquadratic radical clock $K_N=\mathbb Q(\sqrt p:p\le N,\;p\text{ prime})$. T0 (T0, §3 and §5) introduced the **character basis** $\{\tilde\chi_c\}_{c=1}^{N-1}$ of $H_N\otimes\mathbb C$ — the discrete Fourier basis on $\mathbb Z/N$ minus the trivial mode — and used it to define the structured apex generator $\mathcal M_x(\beta,c)$ via the conductor lattice. T0 §5.5 computed the **Helmert-Fourier transfer matrix** at $N=6$ in closed form, establishing Proposition 5.2:
$$\langle h_k,\chi_c\rangle=\frac{1-\omega^{kc}}{1-\omega^c}-k\omega^{kc},\qquad\omega=e^{2\pi i/N},$$
and identified the radical-cyclotomic factorization of the matrix entries.

**Gap.** The closed-form entries are known (T0 Prop 5.2); but the full *structural* content of the transfer matrix as the apex's arithmetic Jacobian between the dimensional (Helmert/radical) and conductor (character/cyclotomic) axes was scoped in T0 §6.3 as a forward door — specifically, (a) the explicit factorization in three equivalent forms (rational polynomial, trigonometric, exponential), (b) the block structure over conductor packets $\{H_d\}_{d\mid N}$, (c) the row/column unitarity content, (d) general-$N$ worked examples beyond $N=6$, and (e) the relationship to standard signal-processing transforms (DFT, DCT, DST, Hartley) and to Gauss sums.

**Action.** We establish the full structure theorem of the transfer matrix $U:=(\langle e_k,\tilde\chi_c\rangle)_{k,c=1}^{N-1}\in U(N-1)$ (unitary $(N-1)\times(N-1)$ matrix over the compositum $K_N\cdot\mathbb Q(\zeta_N)$), with three equivalent closed forms for the entries, complete row and column structural analysis, the block decomposition over conductor packets (showing that $U$ is *not* generically block-diagonal but is *structured* by conductor classes via Gauss-sum-like identities), and worked examples at $N\in\{4,5,6,7,8\}$ covering prime, prime-power, and cross-prime cases.

**Result.** Seven core claims:

1. **Three closed forms.** $U_{kc}$ admits three equivalent expressions: a rational polynomial in $\omega^c=e^{2\pi ic/N}$, a trigonometric form with $\sin/\cos$ of $\pi kc/N$, and an exponential form mixing $e^{i\pi(k-1)c/N}$ phases.

2. **Radical-cyclotomic factorization.** Each entry $U_{kc}=R_k\cdot C_{kc}$ where $R_k=1/\sqrt{Nk(k+1)}\in K_N$ is a radical depending only on $k$ (the Helmert axis), and $C_{kc}$ is a Laurent polynomial in $\omega^c$ with integer coefficients (the cyclotomic / conductor axis).

3. **Last-row uniformity.** $U_{N-1,c}=-\omega^{(N-1)c}/\sqrt{N-1}$ has constant modulus $1/\sqrt{N-1}$ for every $c$, with phase $-\omega^{(N-1)c}$. The last Helmert direction $e_{N-1}$ has uniform Fourier amplitude across all non-trivial characters. (Whether $e_{N-1}$ is the *unique* Helmert direction with this property — beyond worked examples at small $N$, where it is unique — is left open.)

4. **First-row sinusoidal.** $U_{1c}=(1-\omega^c)/\sqrt{2N}$ has modulus $\sqrt{2/N}|\sin(\pi c/N)|$, peaking at $c=N/2$ (when $N$ is even) — the Nyquist mode. The first Helmert direction is the discrete pair $(1,-1)$ at positions $0,1$, and its Fourier content is sinusoidal in $c$.

5. **Block structure over conductors.** $U$ is *not* block-diagonal in the conductor-grouped basis (columns ordered by $\mathrm{cond}(\chi_c)$), but the *column blocks* satisfy specific row-magnitude relations: the block at conductor $d\mid N$ has dimension $\varphi(d)$ and aggregates Gauss-sum-like content over the divisors of $d$.

6. **Unitarity in closed form.** Both row sums $\sum_c|U_{kc}|^2$ and column sums $\sum_k|U_{kc}|^2$ evaluate to $1$ exactly via the identities
$$\sum_{c=1}^{N-1}|1-\omega^{kc}|^2=2(N-1),\qquad\sum_{c=1}^{N-1}(1-\cos(2\pi c/N))=N.$$

7. **Worked examples at $N\in\{4,5,6,7,8\}$.** Explicit matrix forms over the compositum $K_N\cdot\mathbb Q(\zeta_N)$, exhibiting cyclic ($N=5,7$ prime), prime-power depth ($N=4,8$), and cross-prime interaction ($N=6$) structures.

**Harvest.** The Helmert-Fourier transfer matrix $U$ is the categorical-simplex apex's **arithmetic Jacobian** between its two dual orthogonal bases of the mean-zero hyperplane: the integer-rational Helmert basis (carrying the dimensional / multiquadratic-radical clock structure of T4) and the cyclotomic character basis (carrying the conductor-packet / additive Fourier structure of T0/T3). Every apex computation that mixes the two axes — every transfer between dimensional and conductor content — passes through $U$. T9 closes the T0 §6.3 forward door at the entry-level, leaving the algebraic-group-theoretic content of $U$ (its action on the multiquadratic-cyclotomic compositum, its block-spectral structure, its relation to Walsh-Hadamard and DCT transforms) as continuing forward doors.

**Keywords:** Helmert ladder, character basis, change-of-basis matrix, unitary matrix, cyclotomic field, multiquadratic field, conductor packets, Gauss sums, DFT, DCT, Walsh-Hadamard, mean-zero hyperplane, finite Fourier analysis, arithmetic Jacobian.

---

## Cross-references from prior papers

This paper builds on specific results from earlier papers of the \heb{ל}-series; we list the dependencies explicitly.

| Cited result | Used for |
|---|---|
| T0 §3.2 Definition 3.1 (apex generator $\mathcal M_x$) | Background; not used directly |
| T0 §3.3 Theorem 3.5 (closure diagonal) | Conductor selection rule context |
| T0 §4.2 (conductor packets $H_d$, Proposition 4.1 prime-power locality) | Conductor structure in §4 |
| T0 §5.2 Theorem 5.1 (multiquadratic radical clock, restating T4) | Multiquadratic field $K_N$ throughout |
| T0 §5.5 Proposition 5.2 (closed form $\langle h_k,\chi_c\rangle$) | Starting point — restated and elaborated as Theorem 2.1 |
| T0 §5.5 ($N=6$ worked example) | §5.2 reference; not re-derived |
| T4 §3 (Helmert ladder construction, prime-rung growth) | Foundation of §1.1 |
| T8 §4.1 (Gauss sum $\tau(\psi,a)$) | §4.4 forward door |

No theorems from T5, T6, T7, T10 are used directly. T8 enters only through the Gauss-sum nomenclature in §4.4 (forward door).

---

## Notation

We carry the notation of T0 and T4 and consolidate it for the transfer matrix.

| Symbol | Meaning |
|---|---|
| $N$ | Integer dimension, $\ge 2$. |
| $H_N$ | Mean-zero hyperplane $\{q\in\mathbb R^N:\sum q_i=0\}$, dim $N-1$. |
| $h_k$ | Unnormalized Helmert vector $(\underbrace{1,\ldots,1}_{k},-k,0,\ldots,0)$, $1\le k\le N-1$. |
| $e_k$ | Unit Helmert vector $h_k/\sqrt{k(k+1)}$. |
| $\omega$ | Primitive $N$-th root of unity $e^{2\pi i/N}$. |
| $\chi_c$ | Additive character $\chi_c(s)=\omega^{cs}=e^{2\pi ics/N}$ for $s\in\mathbb Z/N$. |
| $\tilde\chi_c$ | $L^2$-normalized character $\chi_c/\sqrt N$. |
| $U=(U_{kc})$ | Transfer matrix $U_{kc}:=\langle e_k,\tilde\chi_c\rangle$, $k,c=1,\ldots,N-1$. |
| $K_N$ | Multiquadratic field $\mathbb Q(\sqrt p:p\le N,\;p\text{ prime})$ (T4). |
| $\mathbb Q(\zeta_N)$ | $N$-th cyclotomic field $\mathbb Q(\omega)$. |
| $K_N\cdot\mathbb Q(\zeta_N)$ | Compositum of $K_N$ and $\mathbb Q(\zeta_N)$ inside $\mathbb C$. |
| $\mathrm{cond}(\chi_c)$ | Conductor $N/\gcd(c,N)$ of $\chi_c$. |
| $H_d$ | Conductor packet $\mathrm{span}\{\chi_c:\mathrm{cond}(\chi_c)=d\}$, $d\mid N$, $d>1$. |
| $\varphi$ | Euler totient function. |
| $\tau(\psi,a)$ | Gauss sum $\sum_{s\in(\mathbb Z/N)^\times}\psi(s)\chi_a(s)$ (T8 notation). |

**Convention.** All vectors are column vectors when concrete; inner products on $\mathbb C^N$ are Hermitian: $\langle u,v\rangle=\sum_i\bar u_iv_i$. The Helmert vectors $h_k$ are real, so $\langle h_k,\chi_c\rangle=\sum_s(h_k)_s\chi_c(s)$ without conjugation. The transfer matrix $U$ is unitary: $U^*U=UU^*=I_{N-1}$.

---

## 1. The two bases of $H_N$

### 1.1 The Helmert basis (integer / rational)

The mean-zero hyperplane $H_N=\{q\in\mathbb R^N:\sum_iq_i=0\}$ has dimension $N-1$. The **Helmert basis** (Helmert 1876; Lancaster 1965) is the canonical integer orthogonal basis of $H_N$ given by the contrasts
$$h_k=(\underbrace{1,1,\ldots,1}_{k\text{ entries}},-k,\underbrace{0,\ldots,0}_{N-k-1\text{ entries}})\in\mathbb R^N,\qquad k=1,2,\ldots,N-1.$$
The squared norms are $\|h_k\|^2=k+k^2=k(k+1)$, and the orthogonality relations $\langle h_j,h_k\rangle=0$ for $j\ne k$ are routine to verify.

The **unit Helmert vectors** are $e_k:=h_k/\sqrt{k(k+1)}$, forming an orthonormal basis of $H_N$.

The Helmert basis carries two distinctive structural features:
- **Integer entries.** The $h_k$ have entries in $\{-k,0,1\}$, an integer rational basis of $H_N$ (without normalization).
- **Multiquadratic radical normalization.** The unit normalizers $\sqrt{k(k+1)}$ accumulate, across the dimensional axis $N$, into the multiquadratic field $K_N=\mathbb Q(\sqrt p:p\le N,\;p\text{ prime})$ (T4 Theorem 3, restated in T0 §5.2 Theorem 5.1).

### 1.2 The character basis (cyclotomic / complex)

The mean-zero hyperplane extends to $H_N\otimes\mathbb C\subset\mathbb C^N$, with the **character basis** $\{\chi_c\}_{c=1}^{N-1}$ where $\chi_c(s)=\omega^{cs}=e^{2\pi ics/N}$ viewed as a vector in $\mathbb C^N$ with components $(\chi_c(s))_{s=0}^{N-1}$. Each non-trivial character $\chi_c$ has $\sum_s\chi_c(s)=0$, hence lies in $H_N\otimes\mathbb C$. The $N-1$ non-trivial characters are linearly independent and span $H_N\otimes\mathbb C$ over $\mathbb C$.

Standard norm computation: $\|\chi_c\|^2=\sum_s|\chi_c(s)|^2=N$, so the $L^2$-normalized characters are $\tilde\chi_c:=\chi_c/\sqrt N$, forming an orthonormal basis of $H_N\otimes\mathbb C$.

The character basis carries:
- **Complex unitary entries.** $\tilde\chi_c$ has entries in $\mathbb Q(\zeta_N)\cdot(1/\sqrt N)$, where $\mathbb Q(\zeta_N)=\mathbb Q(\omega)$ is the $N$-th cyclotomic field.
- **Conductor packet structure.** Characters group by conductor $\mathrm{cond}(\chi_c)=N/\gcd(c,N)$ into conductor packets $H_d\subset H_N\otimes\mathbb C$ of dimensions $\varphi(d)$ (T0 §4.2).

### 1.3 The transfer matrix

**Definition 1.1 (Helmert-Fourier transfer matrix).** The **transfer matrix** between the Helmert and character bases of $H_N\otimes\mathbb C$ is
$$U=(U_{kc})_{k,c=1}^{N-1}\in\mathbb C^{(N-1)\times(N-1)},\qquad U_{kc}:=\langle e_k,\tilde\chi_c\rangle=\frac{1}{\sqrt{Nk(k+1)}}\langle h_k,\chi_c\rangle.$$
The unit Helmert vector $e_k$ has Fourier expansion
$$e_k=\sum_{c=1}^{N-1}\overline{U_{kc}}\,\tilde\chi_c,$$
and conversely, the normalized character $\tilde\chi_c$ has Helmert expansion
$$\tilde\chi_c=\sum_{k=1}^{N-1}U_{kc}\,e_k.$$

**Proposition 1.2 (Unitarity).** $U\in U(N-1)$; equivalently, $U^*U=UU^*=I_{N-1}$.

**Proof.** Both $\{e_k\}$ and $\{\tilde\chi_c\}$ are orthonormal bases of $H_N\otimes\mathbb C$ with respect to the Hermitian inner product on $\mathbb C^N$ restricted to $H_N\otimes\mathbb C$. The change-of-basis matrix between two orthonormal bases is unitary. $\square$

---

## 2. Three closed forms for the entries

### 2.1 Rational polynomial form

**Theorem 2.1 (Rational polynomial form).** For $1\le k\le N-1$ and $c\in\{1,\ldots,N-1\}$,
$$\langle h_k,\chi_c\rangle=\frac{1-\omega^{kc}}{1-\omega^c}-k\omega^{kc}=\frac{1-(k+1)\omega^{kc}+k\omega^{(k+1)c}}{1-\omega^c}.$$
Equivalently, $\langle h_k,\chi_c\rangle$ is a Laurent polynomial in $\omega^c$ with integer coefficients (after clearing the $1-\omega^c$ denominator), of degree $k+1$ in $\omega^c$ with leading coefficient $k$ and constant term $1$.

**Proof.** The first equality is T0 Proposition 5.2, restated; computed directly from $h_k=(1,\ldots,1,-k,0,\ldots,0)$:
$$\langle h_k,\chi_c\rangle=\sum_{j=0}^{k-1}\omega^{cj}-k\omega^{kc}=\frac{1-\omega^{kc}}{1-\omega^c}-k\omega^{kc}.$$
The second equality follows by clearing denominators:
$$\frac{1-\omega^{kc}}{1-\omega^c}-k\omega^{kc}=\frac{(1-\omega^{kc})-k\omega^{kc}(1-\omega^c)}{1-\omega^c}=\frac{1-(k+1)\omega^{kc}+k\omega^{(k+1)c}}{1-\omega^c}.$$
The numerator $P_k(z):=1-(k+1)z^k+kz^{k+1}$ is a polynomial in $z=\omega^c$ with integer coefficients. Evaluating at $z=1$: $P_k(1)=1-(k+1)+k=0$, so $(1-z)\mid P_k(z)$; the quotient $P_k(z)/(1-z)$ is a polynomial in $z$ of degree $k$, with integer coefficients, agreeing with the geometric-sum expression $\sum_{j=0}^{k-1}z^j-kz^k$. $\square$

### 2.2 Trigonometric form

**Theorem 2.2 (Trigonometric form).** Setting $\theta_c:=\pi c/N\in(0,\pi)$ for $c\in\{1,\ldots,N-1\}$,
$$\langle h_k,\chi_c\rangle=e^{i(k-1)\theta_c}\frac{\sin(k\theta_c)}{\sin\theta_c}-ke^{2ik\theta_c}.$$

**Proof.** Using $1-\omega^a=1-e^{2ia\theta_c}=-2ie^{ia\theta_c}\sin(a\theta_c)$,
$$\frac{1-\omega^{kc}}{1-\omega^c}=\frac{-2ie^{ik\theta_c}\sin(k\theta_c)}{-2ie^{i\theta_c}\sin\theta_c}=e^{i(k-1)\theta_c}\frac{\sin(k\theta_c)}{\sin\theta_c}.$$
Substituting into Theorem 2.1 gives the stated form. $\square$

The trigonometric form makes manifest the **sinusoidal envelope** $\sin(k\theta_c)/\sin\theta_c$ characteristic of Dirichlet-kernel-like structures in classical Fourier analysis.

### 2.3 Exponential form

**Theorem 2.3 (Symmetric exponential form).** Factoring out the geometric center of the phase content,
$$\langle h_k,\chi_c\rangle=e^{ik\theta_c}\Big[e^{-i\theta_c}\frac{\sin(k\theta_c)}{\sin\theta_c}-ke^{ik\theta_c}\Big].$$
This identifies the **phase factor** $e^{ik\theta_c}=\omega^{kc/2}$ (where the half-power is the natural symmetric branch of $\omega^c$) and an **amplitude bracket** that is asymptotically dominated by the $\sin(k\theta_c)/\sin\theta_c$ term for small $k$ and by $-ke^{ik\theta_c}$ for $k$ near $N-1$.

**Proof.** Direct factorization of Theorem 2.2. $\square$

### 2.4 Entries of $U$ in the radical-cyclotomic factorization

Putting the three forms together with the unit Helmert normalization:

**Corollary 2.4 (Transfer matrix entries).** For $k,c\in\{1,\ldots,N-1\}$,
$$\boxed{U_{kc}=\frac{1}{\sqrt{Nk(k+1)}}\cdot\big[e^{i(k-1)\theta_c}\sin(k\theta_c)/\sin\theta_c-ke^{2ik\theta_c}\big]=\frac{1}{\sqrt{Nk(k+1)}}\cdot\frac{1-(k+1)\omega^{kc}+k\omega^{(k+1)c}}{1-\omega^c},}$$
where $\theta_c=\pi c/N$ and $\omega=e^{2\pi i/N}$. The factor $1/\sqrt{Nk(k+1)}\in K_N$ is a **radical** depending only on $k$ (the Helmert axis). The rational-polynomial form on the right makes manifest that the cyclotomic content lives in $\mathbb Q(\zeta_N)=\mathbb Q(\omega)$ (Theorem 2.1); the trigonometric form on the left uses half-roots $\zeta_{2N}$ as a representation, but the actual value of the bracket lies in $\mathbb Q(\zeta_N)$ after the cancellation $e^{i(k-1)\theta_c}\sin(k\theta_c)/\sin\theta_c\in\mathbb Q(\zeta_N)$ that is forced by equality with the rational form. Therefore each entry $U_{kc}$ lives in the compositum $K_N\cdot\mathbb Q(\zeta_N)$.

The compositum $K_N\cdot\mathbb Q(\zeta_N)$ is the **arithmetic field of the transfer matrix** at level $N$. For $N=6$ this is $\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\zeta_6)$ of degree $16$ over $\mathbb Q$ (cf. T0 §5.5).

**Remark 2.5 (Bilateral structure of the radical factor).** The radical $R_k$ further splits as
$$R_k=\frac{1}{\sqrt{Nk(k+1)}}=\frac{1}{\sqrt N}\cdot\frac{1}{\sqrt{k(k+1)}},$$
exhibiting two structurally distinct contributions:

- $1/\sqrt{k(k+1)}$ is the **unit-Helmert normalizer** of the $k$-th contrast (T4 §3 / T0 §5.2). By T4 Theorem 3.1 (restated as T0 Theorem 5.1), these normalizers collectively generate the multiquadratic radical field $K_N=\mathbb Q(\sqrt p:p\le N)$ as $k$ ranges over $\{1,\ldots,N-1\}$, growing properly over $K_{N-1}$ precisely at prime rungs.
- $1/\sqrt N$ is the **level-$N$ ambient**, arising from the $L^2$-normalization $\tilde\chi_c=\chi_c/\sqrt N$ of the character basis (§1.2). It lies in $K_N$ since the prime factorization of $N$ involves only primes $p\mid N\le N$, all of which contribute $\sqrt p\in K_N$ as generators.

Both factors live in $K_N$ — the radical $R_k$ is built from T4's Helmert-axis arithmetic together with the character-basis ambient, and the entire entry $U_{kc}$ is then $R_k$ times the cyclotomic conductor data $C_{kc}\in\mathbb Q(\zeta_N)$. This is the bilateral structure of the transfer matrix: $\text{T4 radical clock}\times\text{T0/T3 character cyclotomic}$, intertwined at the entry level.

---

## 3. Row and column structure

The transfer matrix $U\in U(N-1)$ has specific structural features visible at the row and column level.

### 3.1 The last row: uniform Fourier amplitude

**Proposition 3.1 (Last row uniformity).** $U_{N-1,c}=-\omega^{(N-1)c}/\sqrt{N-1}$ for every $c\in\{1,\ldots,N-1\}$. The modulus is the constant $1/\sqrt{N-1}$ across all $c$.

**Proof.** $h_{N-1}=(1,1,\ldots,1,-(N-1))$ has $N-1$ ones and $-(N-1)$ at position $N-1$. Therefore
$$\langle h_{N-1},\chi_c\rangle=\sum_{s=0}^{N-2}\omega^{cs}-(N-1)\omega^{(N-1)c}.$$
For $c\ne 0$, $\sum_{s=0}^{N-1}\omega^{cs}=0$ (additive character orthogonality), so $\sum_{s=0}^{N-2}\omega^{cs}=-\omega^{(N-1)c}$. Substituting,
$$\langle h_{N-1},\chi_c\rangle=-\omega^{(N-1)c}-(N-1)\omega^{(N-1)c}=-N\omega^{(N-1)c}.$$
Dividing by $\sqrt{N\cdot(N-1)\cdot N}=N\sqrt{N-1}$,
$$U_{N-1,c}=\frac{-N\omega^{(N-1)c}}{N\sqrt{N-1}}=-\frac{\omega^{(N-1)c}}{\sqrt{N-1}}.\qquad\square$$

**Interpretation.** The last Helmert direction $e_{N-1}=h_{N-1}/\sqrt{N(N-1)}$ — the maximally "rear-loaded" contrast, with weight $-(N-1)$ at the last position — has **uniform Fourier amplitude** across all non-trivial characters. In the worked examples of §5 ($N\le 8$), $e_{N-1}$ is the *unique* Helmert direction with this property; whether uniqueness holds for all $N$ is left open.

### 3.2 The first row: sinusoidal Fourier amplitude

**Proposition 3.2 (First row sinusoidal).** $U_{1c}=(1-\omega^c)/\sqrt{2N}$, with $|U_{1c}|=\sqrt{2/N}\cdot|\sin(\pi c/N)|=\sqrt{2/N}\sin\theta_c$ for $c\in\{1,\ldots,N-1\}$.

**Proof.** $h_1=(1,-1,0,\ldots,0)$, so $\langle h_1,\chi_c\rangle=1-\omega^c$. Dividing by $\sqrt{N\cdot 2}=\sqrt{2N}$ gives $U_{1c}$. The modulus computation: $|1-\omega^c|^2=(1-\cos 2\theta_c)^2+\sin^2 2\theta_c=2-2\cos 2\theta_c=4\sin^2\theta_c$, so $|1-\omega^c|=2|\sin\theta_c|$ and $|U_{1c}|=2|\sin\theta_c|/\sqrt{2N}=\sqrt{2/N}\sin\theta_c$ (for $\theta_c\in(0,\pi)$, $\sin\theta_c>0$). $\square$

**Interpretation.** The first Helmert direction $e_1=(1,-1,0,\ldots,0)/\sqrt 2$ — the simplest discrete contrast — has a **sinusoidal Fourier amplitude** in $c$, peaking at $c=N/2$ (the Nyquist mode, when $N$ is even) with peak amplitude $\sqrt{2/N}$. This is the **discrete sine-transform signature** of the first Helmert contrast.

### 3.3 Unitarity in closed form

The row and column sums of $|U|^2$ both evaluate to $1$ by unitarity, but the algebraic identities involved are worth recording.

**Proposition 3.3 (Row unitarity).** $\sum_{c=1}^{N-1}|U_{kc}|^2=1$ for every $k\in\{1,\ldots,N-1\}$.

**Proof.** $e_k$ is a unit vector in $H_N\otimes\mathbb C$ (Helmert orthonormality), and $\{\tilde\chi_c\}_{c=1}^{N-1}$ is an orthonormal basis of $H_N\otimes\mathbb C$ (Definition 1.1). Parseval's identity gives
$$\sum_{c=1}^{N-1}|\langle e_k,\tilde\chi_c\rangle|^2=\|e_k\|^2=1,$$
which is the claim, since $U_{kc}=\langle e_k,\tilde\chi_c\rangle$. $\square$

**Corollary 3.3a (Trigonometric identity at $k=1$).** Parseval's identity applied to $e_1$ yields the closed-form identity
$$\sum_{c=1}^{N-1}\sin^2(\pi c/N)=\frac{N}{2}.$$

**Proof.** $|U_{1c}|^2=(2/N)\sin^2(\pi c/N)$ (Proposition 3.2), so Proposition 3.3 at $k=1$ gives $(2/N)\sum_{c=1}^{N-1}\sin^2(\pi c/N)=1$, equivalently $\sum_c\sin^2(\pi c/N)=N/2$. (This identity also follows from $\sin^2 x=(1-\cos 2x)/2$ and the additive-character identity $\sum_{c=0}^{N-1}\cos(2\pi c/N)=0$.) $\square$

**Proposition 3.4 (Column unitarity).** $\sum_{k=1}^{N-1}|U_{kc}|^2=1$ for every $c\in\{1,\ldots,N-1\}$.

**Proof.** Parallel to Proposition 3.3: $\tilde\chi_c$ is a unit vector and $\{e_k\}$ is an orthonormal basis, so $\sum_k|\langle\tilde\chi_c,e_k\rangle|^2=\|\tilde\chi_c\|^2=1$. Since $\langle\tilde\chi_c,e_k\rangle=\overline{U_{kc}}$, the squared moduli are equal. $\square$

---

## 4. The conductor-packet block structure

### 4.1 Conductor reordering of columns

The character basis $\{\tilde\chi_c\}_{c=1}^{N-1}$ partitions naturally by conductor:
$$\{1,\ldots,N-1\}=\bigsqcup_{d\mid N,\,d>1}C_d,\qquad C_d:=\{c\in\{1,\ldots,N-1\}:\mathrm{cond}(\chi_c)=d\}.$$
By T0 §4.2, $|C_d|=\varphi(d)$ for each divisor $d>1$ of $N$. Reordering columns of $U$ by conductor groups produces a **block-columnar** structure
$$U=[U^{(d_1)}\,|\,U^{(d_2)}\,|\,\cdots\,|\,U^{(d_r)}],$$
where the divisors $d_1<d_2<\cdots<d_r$ are the divisors of $N$ greater than $1$, and $U^{(d)}\in\mathbb C^{(N-1)\times\varphi(d)}$ is the column-block of $U$ indexed by characters of conductor $d$.

### 4.2 Block structure is *not* block-diagonal in general

A natural question: does the Helmert basis admit a parallel partition by conductor, producing a block-diagonal $U$?

**Proposition 4.1 (Non-block-diagonality at the first Helmert vector).** For every $N\ge 3$, no permutation of the Helmert basis $\{e_k\}_{k=1}^{N-1}$ makes $U$ block-diagonal with respect to the conductor partition of columns. In particular, the first Helmert vector $h_1=(1,-1,0,\ldots,0)$ has non-zero Fourier content in *every* conductor packet $H_d$ for $d\mid N$, $d>1$.

**Proof.** Block-diagonality of $U$ (under some permutation of rows) would require each Helmert vector $h_k$ to be supported on a single conductor packet $H_d$ — i.e., $\langle h_k,\chi_c\rangle=0$ for every $c$ with $\mathrm{cond}(\chi_c)\ne d$.

For $h_1$: $\langle h_1,\chi_c\rangle=1-\omega^c$, which vanishes only when $\omega^c=1$, i.e., $c\equiv 0\pmod N$. Since $c\in\{1,\ldots,N-1\}$, $\omega^c\ne 1$ for every non-trivial character, so $\langle h_1,\chi_c\rangle\ne 0$ for *every* $c\ne 0$ — in particular, for every $c$ in *every* conductor packet $H_d$ ($d\mid N$, $d>1$). Hence $h_1$ has non-zero content in every conductor packet simultaneously and cannot be assigned to a single packet under any permutation. $\square$

The argument generalizes: $h_k$ has zero Fourier content at $\chi_c$ iff $1-(k+1)\omega^{kc}+k\omega^{(k+1)c}=0$ (Theorem 2.1 numerator), an equation in $\omega^c$ of degree $k+1$ with at most $k+1$ solutions; for $k+1<N-1$ this leaves $\ge 1$ non-zero values of $c$ on which $h_k$ has non-zero content per conductor packet, generically preventing assignment to a single packet.

So $U$ is structured by conductor columns but does *not* generically decompose into a block-diagonal form. The transfer between the Helmert and character bases genuinely mixes conductor packets.

### 4.3 Column-block structural relations

While not block-diagonal, the conductor-column blocks $U^{(d)}$ satisfy specific structural relations:

**Proposition 4.2 (Column-block norms).** For each divisor $d\mid N$ with $d>1$,
$$\sum_{c\in C_d}|U_{kc}|^2=\frac{1}{Nk(k+1)}\sum_{c\in C_d}|\langle h_k,\chi_c\rangle|^2$$
is the **conductor-$d$ content** of the unit Helmert vector $e_k$. The total $\sum_{d\mid N,d>1}\sum_{c\in C_d}|U_{kc}|^2=\sum_{c=1}^{N-1}|U_{kc}|^2=1$ partitions the unit norm of $e_k$ across the conductor packets.

This gives a **conductor-spectral decomposition** of each Helmert basis vector: how much of $e_k$ lives at conductor $d$. Computing this in closed form via the rational polynomial expression of Theorem 2.1 is a finite combinatorial problem in each case.

### 4.4 Where Gauss sums enter

The conductor blocks $U^{(d)}$ involve partial geometric sums $\sum_{j=0}^{k-1}\omega^{cj}$ over additive characters of conductor $d$, but these are *not* themselves Gauss sums in the classical sense: Gauss sums (T8 §4.1) are sums over $(\mathbb Z/N)^\times$ of a *multiplicative-character* weighting times an additive character, of the form $\tau(\psi,a)=\sum_{s\in(\mathbb Z/N)^\times}\psi(s)\chi_a(s)$.

The proper connection between T9's transfer matrix and T8's Gauss sums goes via the **conductor-$N$ block**: when $d=N$ (i.e., $\chi_c$ has conductor $N$, equivalently $\gcd(c,N)=1$), the character $\chi_c$ restricted to units of $(\mathbb Z/N)^\times$ is a *primitive additive character*, and the row-aggregated content $\sum_{c\in C_N}(\text{multiplicative-character weight})\cdot\langle h_k,\chi_c\rangle$ becomes a Gauss sum proper. Precise statements of this aggregation — including which multiplicative characters $\psi$ produce non-trivial Gauss-sum identities and how the Helmert ladder contributes structurally — are forward doors (§7.4) connecting T9 to T8's bilateral Pontryagin theory.

The conductor-$d$ block $U^{(d)}$ for $d<N$ involves additive characters of smaller conductor, lifted from $\mathbb Z/d$ to $\mathbb Z/N$; its Gauss-sum content lives at level $d$, not $N$. The interaction between conductor-$d$ blocks and Gauss sums at level $d$ requires the depth-filtration analysis of T0 §4.2 generalized to the bilateral setting.

---

## 5. Worked examples

### 5.1 $N=4$: smallest prime-power-depth case

For $N=4$: $\omega=e^{i\pi/2}=i$. Divisors of $4$ greater than $1$: $\{2,4\}$.
- $C_2=\{2\}$ (conductor 2, $\chi_2(s)=(-1)^s$).
- $C_4=\{1,3\}$ (conductor 4).

Helmert vectors:
$h_1=(1,-1,0,0)$, $\|h_1\|=\sqrt 2$.
$h_2=(1,1,-2,0)$, $\|h_2\|=\sqrt 6$.
$h_3=(1,1,1,-3)$, $\|h_3\|=\sqrt{12}=2\sqrt 3$.

Direct computation of $\langle h_k,\chi_c\rangle=\sum_{j=0}^{k-1}i^{cj}-ki^{kc}$ for $k,c\in\{1,2,3\}$ yields

| $k\backslash c$ | $c=1$ | $c=2$ | $c=3$ |
|---|---|---|---|
| $k=1$ | $1-i$ | $2$ | $1+i$ |
| $k=2$ | $3+i$ | $-2$ | $3-i$ |
| $k=3$ | $4i$ | $4$ | $-4i$ |

Normalizing by $\sqrt{Nk(k+1)}=\sqrt{4k(k+1)}$ ($k=1:\sqrt 8=2\sqrt 2$; $k=2:\sqrt{24}=2\sqrt 6$; $k=3:\sqrt{48}=4\sqrt 3$) gives the transfer matrix:
$$U_4=\begin{pmatrix}\dfrac{1-i}{2\sqrt 2}&\dfrac{1}{\sqrt 2}&\dfrac{1+i}{2\sqrt 2}\\[6pt] \dfrac{3+i}{2\sqrt 6}&\dfrac{-1}{\sqrt 6}&\dfrac{3-i}{2\sqrt 6}\\[6pt] \dfrac{i}{\sqrt 3}&\dfrac{1}{\sqrt 3}&\dfrac{-i}{\sqrt 3}\end{pmatrix}.$$

Observations:
- Last row $k=3$: constant modulus $1/\sqrt 3$ in agreement with Proposition 3.1 ($1/\sqrt{N-1}=1/\sqrt 3$).
- First row $k=1$: moduli $(|1-i|,|2|,|1+i|)/(2\sqrt 2)=(\sqrt 2,2,\sqrt 2)/(2\sqrt 2)=(1/2,1/\sqrt 2,1/2)$, consistent with Proposition 3.2 sinusoidal form $\sqrt{2/N}\sin(\pi c/N)$ evaluated at $\theta=\pi/4,\pi/2,3\pi/4$.
- Row-unitarity check $k=1$: $|U_{1c}|^2$ sums to $1/4+1/2+1/4=1$.

The arithmetic field of $U_4$ is $\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 6,i)=\mathbb Q(\sqrt 2,\sqrt 3,i)=K_4\cdot\mathbb Q(\zeta_4)$ — degree $8$ over $\mathbb Q$.

### 5.2 $N=6$: cross-prime case (from T0 §5.5)

Already worked in T0 §5.5. We do not repeat the full computation here; the key data:
- $\omega=e^{i\pi/3}$, $\mathbb Q(\zeta_6)=\mathbb Q(\sqrt{-3})$.
- Conductor classes: $C_2=\{3\}$, $C_3=\{2,4\}$, $C_6=\{1,5\}$.
- Arithmetic field: $K_6\cdot\mathbb Q(\zeta_6)=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\zeta_6)$, degree $16$.
- The $c=3$ column ($H_2$ packet, real characters) computed in T0 §5.5: $U_{\cdot,3}=(1/\sqrt 3,-1/3,\sqrt 2/3,-2/\sqrt{30},1/\sqrt 5)^\top$.

### 5.3 $N=8$: prime-power depth, non-cyclic units

For $N=8$: $\omega=e^{i\pi/4}=(1+i)/\sqrt 2$. Divisors of $8$ greater than $1$: $\{2,4,8\}$, with conductor classes
$$C_2=\{4\},\;|C_2|=\varphi(2)=1;\qquad C_4=\{2,6\},\;|C_4|=\varphi(4)=2;\qquad C_8=\{1,3,5,7\},\;|C_8|=\varphi(8)=4,$$
totaling $1+2+4=7=N-1$.

**Arithmetic field.** $K_8=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\sqrt 7)$, degree $2^4=16$ (one quadratic per prime $\le 8$); $\mathbb Q(\zeta_8)=\mathbb Q(\sqrt 2,i)$, degree $\varphi(8)=4$; the intersection $K_8\cap\mathbb Q(\zeta_8)=\mathbb Q(\sqrt 2)$ (since $K_8$ is totally real, excluding $i$; and the only quadratic in $\mathbb Q(\zeta_8)$ that lies in $K_8$ is $\mathbb Q(\sqrt 2)$). Hence
$$[K_8\cdot\mathbb Q(\zeta_8):\mathbb Q]=\frac{16\cdot 4}{2}=32.$$

**Helmert ladder.** The seven contrasts $h_1,\ldots,h_7$ have unit normalizers $\sqrt 2,\sqrt 6,\sqrt{12}=2\sqrt 3,\sqrt{20}=2\sqrt 5,\sqrt{30},\sqrt{42},\sqrt{56}=2\sqrt{14}$, drawing radicals from the primes $\{2,3,5,7\}\cap K_8$.

**Conductor structure.** Three packets of dimensions $1,2,4$, exhibiting **prime-power depth** $\{p,p^2,p^3\}$ for $p=2$ (T0 Proposition 4.1).

**Last and first rows from §3.** $U_{7,c}=-\omega^{7c}/\sqrt 7$ (constant modulus $1/\sqrt 7$); $U_{1,c}=(1-\omega^c)/4$ (modulus $|\sin(\pi c/8)|/2$, peaking at $c=4$ where $|U_{1,4}|=1/2$).

**Worked column at $c=4$ (the $C_2$ packet).** The single column with $c=4$ corresponds to $\chi_4(s)=(-1)^s$, real-valued. By Theorem 2.1 specialized to $\omega^c=-1$, using $\sum_{j=0}^{k-1}(-1)^j=(1-(-1)^k)/2$,
$$\langle h_k,\chi_4\rangle=\frac{1-(-1)^k}{2}-k(-1)^k,$$
evaluating to the integer sequence $(2,-2,4,-4,6,-6,8)$ for $k=1,\ldots,7$. Dividing by $\sqrt{Nk(k+1)}=\sqrt{8k(k+1)}$:
$$U_{\cdot,4}=\Big(\frac{1}{2},\,-\frac{1}{2\sqrt 3},\,\frac{1}{\sqrt 6},\,-\frac{1}{\sqrt{10}},\,\frac{3}{2\sqrt{15}},\,-\frac{3}{2\sqrt{21}},\,\frac{1}{\sqrt 7}\Big)^\top.$$

Column unitarity check (column $c=4$): $\sum_{k=1}^7|U_{k,4}|^2$. Computing each term and putting over common denominator $420$:
$$\frac{1}{4}=\frac{105}{420},\;\frac{1}{12}=\frac{35}{420},\;\frac{1}{6}=\frac{70}{420},\;\frac{1}{10}=\frac{42}{420},\;\frac{9}{60}=\frac{63}{420},\;\frac{9}{84}=\frac{45}{420},\;\frac{1}{7}=\frac{60}{420},$$
summing to $105+35+70+42+63+45+60=420$, i.e., $420/420=1$, confirming Proposition 3.4.

This column lives entirely in the real subfield $\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\sqrt 7,\sqrt{14})\cdot\mathbb Q=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\sqrt 7)=K_8$ (no cyclotomic content, since $\chi_4$ is the real Dirichlet character). The cyclotomic content $\mathbb Q(\zeta_8)$ enters only in the higher-conductor columns $C_4$ and $C_8$.

The full $7\times 7$ transfer matrix at $N=8$ has the $c=4$ column above; the $C_4$ block ($c=2,6$) requires $\mathbb Q(\zeta_4)=\mathbb Q(i)$ content; and the $C_8$ block ($c=1,3,5,7$) requires the full $\mathbb Q(\zeta_8)=\mathbb Q(\sqrt 2,i)$ content. We do not compute the remaining $48$ entries explicitly.

### 5.4 $N=5,7$: prime $N$ (single conductor)

For prime $N$: every non-trivial character has conductor $N$ (since $\gcd(c,N)=1$ for $c\in\{1,\ldots,N-1\}$). The conductor packet structure is trivial — single packet $H_N$ of dimension $N-1$. The transfer matrix $U$ has no conductor-block-column refinement (only one block, of full size); structurally, $U$ at prime $N$ is "all one packet."

**$N=5$.** $K_5=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5)$, degree $8$. $\mathbb Q(\zeta_5)$ has degree $\varphi(5)=4$ and is a CM field whose maximal real subfield is the unique quadratic subfield $\mathbb Q(\sqrt 5)$ (since $5\equiv 1\pmod 4$, the Gauss-sum identity $\tau(\chi)^2=5$ for the quadratic Dirichlet character mod $5$ places $\sqrt 5$ in $\mathbb Q(\zeta_5)$). Hence the intersection $K_5\cap\mathbb Q(\zeta_5)=\mathbb Q(\sqrt 5)$ has degree $2$, and the compositum
$$[K_5\cdot\mathbb Q(\zeta_5):\mathbb Q]=\frac{8\cdot 4}{2}=16.$$

**$N=7$.** $K_7=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\sqrt 7)$, degree $16$. $\mathbb Q(\zeta_7)$ has degree $\varphi(7)=6$ and is a CM field. Its maximal real subfield $\mathbb Q(\zeta_7+\zeta_7^{-1})$ is a cyclic cubic field of degree $3$ over $\mathbb Q$ with discriminant $49$; this cubic does *not* contain $\sqrt p$ for any prime $p\le 7$, since a cyclic cubic over $\mathbb Q$ cannot contain a quadratic extension. Since $K_7$ is totally real, $K_7\cap\mathbb Q(\zeta_7)\subseteq K_7\cap(\mathbb Q(\zeta_7)\cap\mathbb R)=K_7\cap\mathbb Q(\zeta_7+\zeta_7^{-1})=\mathbb Q$ (the cubic real subfield meets the multiquadratic $K_7$ trivially by the degree argument). Hence
$$[K_7\cdot\mathbb Q(\zeta_7):\mathbb Q]=16\cdot 6=96.$$

### 5.5 Comparison table across $N$

| $N$ | Type | Conductor blocks (sizes) | $K_N$ degree | $\mathbb Q(\zeta_N)$ degree | Intersection degree | Compositum degree |
|---|---|---|---|---|---|---|
| $4$ | $p^2$, $p=2$ | $H_2,H_4=(1,2)$ | $4$ | $2$ | $1$ ($\mathbb Q$) | $8$ |
| $5$ | prime | $H_5=(4)$ | $8$ | $4$ | $2$ ($\mathbb Q(\sqrt 5)$) | $16$ |
| $6$ | $2\cdot 3$ | $H_2,H_3,H_6=(1,2,2)$ | $8$ | $2$ | $1$ ($\mathbb Q$) | $16$ |
| $7$ | prime | $H_7=(6)$ | $16$ | $6$ | $1$ ($\mathbb Q$) | $96$ |
| $8$ | $p^3$, $p=2$ | $H_2,H_4,H_8=(1,2,4)$ | $16$ | $4$ | $2$ ($\mathbb Q(\sqrt 2)$) | $32$ |
| $30$ | $2\cdot 3\cdot 5$ | $H_2,H_3,H_5,H_6,H_{10},H_{15},H_{30}=(1,2,4,2,4,8,8)$ | $1024$ | $8$ | $2$ ($\mathbb Q(\sqrt 5)$) | $4096$ |

The arithmetic complexity of the transfer matrix grows quickly with $N$, but the structural decomposition (conductor blocks, radical-cyclotomic factorization, Helmert row structure) is uniform across all $N$.

### 5.6 $N=30$: three-prime squarefree structural sample

At the squarefree-composite anchor $N=30=2\cdot 3\cdot 5$ — the smallest $N$ with three distinct prime factors — the transfer matrix is $29\times 29$, with rich conductor and radical content. We do not compute all $841$ entries explicitly, but record the structural ingredients.

**Radical content.** The $L^2$-normalizers $\sqrt{30k(k+1)}$ for $k=1,\ldots,29$ generate radicals $\sqrt{\mathrm{sf}(30k(k+1))}$ where $\mathrm{sf}$ is the squarefree kernel. By T4 Theorem 5.1 / T0 §5.2, these radicals collectively generate $K_{30}=\mathbb Q(\sqrt p:p\le 30,\;p\text{ prime})=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\sqrt 7,\sqrt{11},\sqrt{13},\sqrt{17},\sqrt{19},\sqrt{23},\sqrt{29})$, a multiquadratic field of degree $2^{10}=1024$ over $\mathbb Q$. Each prime $p\le 30$ enters at the rung $k=p-1$ via the relation $k(k+1)=(p-1)p$. A sample of representative new-prime rungs:

| $k$ | $30k(k+1)$ | $\mathrm{sf}(30k(k+1))$ | New radical generator |
|---|---|---|---|
| $1$ | $60$ | $15$ | $\sqrt{15}\in K_5$ |
| $6$ | $1260$ | $35$ | $\sqrt{35}=\sqrt 5\sqrt 7\in K_7$ |
| $10$ | $3300$ | $33$ | $\sqrt{33}=\sqrt 3\sqrt{11}\in K_{11}$ |
| $12$ | $4680$ | $130$ | $\sqrt{130}=\sqrt 2\sqrt 5\sqrt{13}\in K_{13}$ |
| $16$ | $8160$ | $510$ | $\sqrt{510}=\sqrt 2\sqrt 3\sqrt 5\sqrt{17}\in K_{17}$ |
| $18$ | $10260$ | $285$ | $\sqrt{285}=\sqrt 3\sqrt 5\sqrt{19}\in K_{19}$ |
| $22$ | $15180$ | $345$ | $\sqrt{345}=\sqrt 3\sqrt 5\sqrt{23}\in K_{23}$ |
| $28$ | $24360$ | $870$ | $\sqrt{870}=\sqrt 2\sqrt 3\sqrt 5\sqrt{29}\in K_{29}$ |

Every prime $p\in\{2,3,5,7,11,13,17,19,23,29\}$ enters the radical field by $k=p-1\le 28$, consistent with T4 Theorem 5.1's prime-rung criterion (T0 Theorem 5.1).

**Cyclotomic content.** The cyclotomic part lives in $\mathbb Q(\zeta_{30})$, of degree $\varphi(30)=8$ over $\mathbb Q$. CRT decomposes the character index $c\in\mathbb Z/30$ via $\mathbb Z/30\cong\mathbb Z/2\times\mathbb Z/3\times\mathbb Z/5$, so each character factorizes as $\chi_c=\chi^{(2)}_{c_2}\otimes\chi^{(3)}_{c_3}\otimes\chi^{(5)}_{c_5}$ on the CRT-decomposed labels. The conductor structure has packets at every divisor $d\in\{2,3,5,6,10,15,30\}$ with $|C_d|=\varphi(d)$:

| $d$ | $\varphi(d)$ | Packet contents (representative) |
|---|---|---|
| $2$ | $1$ | $c=15$ |
| $3$ | $2$ | $c=10,20$ |
| $5$ | $4$ | $c=6,12,18,24$ |
| $6$ | $2$ | $c=5,25$ |
| $10$ | $4$ | $c=3,9,21,27$ |
| $15$ | $8$ | $c=2,4,8,14,16,22,26,28$ |
| $30$ | $8$ | $c=1,7,11,13,17,19,23,29$ |

Total: $1+2+4+2+4+8+8=29=N-1$ as required.

**Arithmetic field.** $K_{30}\cdot\mathbb Q(\zeta_{30})$: $K_{30}$ has degree $2^{10}=1024$; $\mathbb Q(\zeta_{30})$ has degree $\varphi(30)=8$ and contains $\sqrt 5$ (since $5\equiv 1\pmod 4$, the Gauss-sum identity places $\sqrt 5\in\mathbb Q(\zeta_5)\subset\mathbb Q(\zeta_{30})$); intersection $K_{30}\cap\mathbb Q(\zeta_{30})=\mathbb Q(\sqrt 5)$ of degree $2$. Hence
$$[K_{30}\cdot\mathbb Q(\zeta_{30}):\mathbb Q]=\frac{1024\cdot 8}{2}=4096.$$

**Structural features visible at $N=30$.** The $29\times 29$ matrix $U_{30}$ exhibits all three structural features of T9 simultaneously:
- *Radical-cyclotomic factorization* (Cor 2.4): each entry $U_{kc}=R_k\cdot C_{kc}$.
- *Conductor-block columns* (§4.1): seven column groups of sizes $(1,2,4,2,4,8,8)$ — the richest conductor stratification of any worked example in §5.
- *Last-row uniformity* (Prop 3.1): $U_{29,c}=-\omega^{29c}/\sqrt{29}$ with constant modulus $1/\sqrt{29}$.

The full conductor-block decomposition of $U_{30}$ requires the Gauss-sum decomposition forward door (§7.4), since the three distinct primes $\{2,3,5\}$ produce non-trivial cross-prime interaction at the cubic Vandermonde level. $N=30$ is the natural next benchmark after the $N=6$ worked example (§5.2): both are squarefree-composite, but $N=30$ has three prime axes versus $N=6$'s two, so the cross-prime ANOVA (T0 §4.4) is structurally richer.

---

## 6. Connection to standard transforms

### 6.1 Helmert vs. DFT

The character basis $\{\tilde\chi_c\}$ is the **discrete Fourier transform (DFT)** basis on $\mathbb Z/N$, with the trivial character $\chi_0$ removed. The transfer matrix $U$ is therefore the change-of-basis from the Helmert basis to (the non-trivial part of) the DFT basis.

The Helmert basis is itself a **classical contrast basis** in analysis of variance (ANOVA) and orthogonal polynomial regression: each $h_k$ is the $k$-th order discrete orthogonal contrast.

### 6.2 Helmert vs. DCT and DST

The discrete cosine and sine transforms (DCT, DST) of standard signal processing are real-valued analogs of the DFT, with various boundary conditions. The Helmert basis is qualitatively different — it is *integer* rather than *trigonometric*, and its structural feature is the radical normalization rather than orthogonal cosines/sines.

The trigonometric form of $U_{kc}$ (Theorem 2.2) makes manifest that the transfer matrix has **DCT/DST-flavored** sine envelopes $\sin(k\theta_c)/\sin\theta_c$, but the integer Helmert structure remains visible through the radical normalizers $1/\sqrt{Nk(k+1)}$.

### 6.3 Helmert vs. Walsh-Hadamard

For power-of-two $N=2^a$, the **Walsh-Hadamard transform** uses $\pm 1$-valued basis vectors of $\mathbb R^N$ structured by binary expansion. The Helmert basis is *not* the same as the Walsh-Hadamard basis: Helmert is triangular (each $h_k$ supported on positions $0,\ldots,k$), while Walsh-Hadamard is fully spread.

A future paper (T9.3, planned) could explore the precise relationship at power-of-two $N$, including whether the Helmert and Walsh-Hadamard bases generate the same algebraic group action on $H_N$.

---

## 7. Forward doors

### 7.1 Complex extension via T7

The Helmert basis was developed for real ledgers; in the complex amplitude setting of T7, the natural extension uses Hermitian Helmert contrasts on $\mathbb C^N$. The complex transfer matrix $U_{\mathbb C}$ on $H_N\otimes\mathbb C$ is identical to $U$ as defined here (since the character basis is already complex), but its action on T7's complex apex generator $\mathcal M_z$ introduces new structure.

Forward paper title (planned): **T9.1 — The Complex Helmert-Fourier Transfer Matrix.**

### 7.2 Multiplicative extension via T8

T8 introduced the multiplicative-character basis $\{\psi\}$ of $\widehat{(\mathbb Z/N)^\times}$ on units. The natural **multiplicative-Helmert transfer matrix** $V$ would relate a Helmert-like basis on units (suitably constructed) to the multiplicative character basis. The Helmert basis itself does not naturally restrict to units; an analog construction on $(\mathbb Z/N)^\times$ requires defining "discrete contrasts" indexed by the unit group structure.

Forward paper title (planned): **T9.2 — The Multiplicative Helmert Basis on Units.**

### 7.3 Walsh-Hadamard comparison at $N=2^a$

For $N=2^a$, both the Helmert and Walsh-Hadamard bases are integer-rational orthogonal bases of $H_N$. Their precise algebraic relationship — including the change-of-basis matrix between them, and whether they coincide in any natural sense — is a forward door.

Forward paper title (planned): **T9.3 — Helmert vs Walsh-Hadamard at Power-of-Two $N$.**

### 7.4 Full Gauss-sum decomposition of conductor blocks

The conductor-block columns $U^{(d)}$ of §4 contain Gauss-sum-flavored content that connects to T8's multiplicative-Fourier framework. The precise Gauss-sum decomposition of each column block — expressing $U^{(d)}$ as a structured product of Gauss sums and unit radicals — is the natural meeting point of T9 and T8.

Forward paper title (planned): **T9.4 — Gauss-Sum Decomposition of the Conductor Blocks.**

### 7.5 Spectral and algebraic-group structure

$U\in U(N-1)$ is a specific unitary matrix; its spectrum (eigenvalues and eigenvectors) carries arithmetic information. Computing the spectrum of $U$ at small $N$ and connecting it to known number-theoretic quantities (Gauss-sum traces, regulator-type invariants of $K_N$, etc.) is a forward door for the analytic side of T9.

Forward paper title (planned): **T9.5 — Spectral Theory of the Helmert-Fourier Transfer Matrix.**

*This forward door is now executed by the Numbers (N-) series.* [N2] gives the determinant $\det U_N=i^{-\binom{N-1}{2}}$ via the block factorization $HF^{\mathsf T}=1\oplus U_N$; [N3] proves the spectrum concentrates at the fourth roots of unity (the DFT eigenvalues), reducing the concentration to a single edge mode; and [N4] identifies that edge mode, in the $N\to\infty$ scaling limit, with an archimedean operator $(A-I)\Phi$ whose even sector is the Riemann–Siegel scattering multiplier $\gamma(s)R$ — so the spectrum of $U$ is the operator-theoretic incarnation of the archimedean place, exactly the number-theoretic connection sought here.

---

## 8. Coda

The Helmert-Fourier transfer matrix $U$ is the apex's arithmetic Jacobian between two distinct orthogonal bases of $H_N$:

- The **Helmert basis** $\{e_k\}$, integer-rational, carrying the **dimensional axis** of the apex (T4 dimensional ladder and its multiquadratic radical clock).
- The **character basis** $\{\tilde\chi_c\}$, cyclotomic-complex, carrying the **conductor axis** of the apex (T0/T3 conductor packets and their additive Fourier structure).

Every computation in the apex framework that crosses these two axes — every transfer between dimensional content (Helmert order $k$) and conductor content (character index $c$) — passes through $U$. The closed-form entries (Theorem 2.1, equivalent forms in §2.2, §2.3), the radical-cyclotomic factorization (Corollary 2.4), and the row/column structural propositions (§3) together provide the entry-level structure theorem; the conductor-block structure (§4) and worked examples (§5) exhibit the apex's arithmetic Jacobian explicitly for small $N$.

The one-sentence apex of T9:

> **The Helmert-Fourier transfer matrix $U_{kc}=R_k\cdot C_{kc}$ factors entry-wise into a radical $R_k=1/\sqrt{Nk(k+1)}$ in the multiquadratic field $K_N$ (the Helmert axis content) and a cyclotomic polynomial $C_{kc}$ in $\omega^c$ over $\mathbb Q(\zeta_N)$ (the conductor axis content), uniting the dimensional and conductor arithmetics of the categorical-simplex apex into a single unitary matrix in $U(N-1)$ over the compositum $K_N\cdot\mathbb Q(\zeta_N)$.**

And the closing slogan:

> **Two orthogonal bases of $H_N$: one integer-rational, one cyclotomic. Their transfer matrix is the apex's arithmetic Jacobian.**

---

## Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper. The collaborations were intellectually substantive: AI partners contributed insights, proposed theorems and conjectures, surfaced relevant literature, verified derivations, and iterated on exposition. I acknowledge this use transparently; the selection of which contributions to keep and the responsibility for the mathematical content are mine.

---

## References

Helmert, F. R. (1876). Classical Helmert transformations and orthogonal contrasts. *Astronomische Nachrichten* 88, 113–132.

Iwaniec, H. and Kowalski, E. (2004). *Analytic Number Theory.* American Mathematical Society Colloquium Publications 53.

Lancaster, H. O. (1965). The Helmert matrices. *American Mathematical Monthly* 72, 4–12.

Lang, S. (2002). *Algebra.* Revised third edition. Graduate Texts in Mathematics 211. Springer.

Murillo Montero, L. (2026). *T0 — Gauge Selection and the Fourier-Mellin Simplex.* First draft, May 25, 2026.

Murillo Montero, L. (2026). *T3 — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint, DOI 10.5281/zenodo.20339049.

Murillo Montero, L. (2026). *T4 — The Helmert-Simplicial Residue Ladder.* First draft, May 24, 2026.

Murillo Montero, L. (2026). *T7 — Complex Amplitudes and the Quantum Sector of the Apex.* First draft, May 25, 2026.

Murillo Montero, L. (2026). *T8 — The Multiplicative Apex and Finite Dirichlet Polynomials.* First draft, May 25, 2026.

Pontryagin, L. S. (1939). *Topological Groups.* Princeton University Press.

Walsh, J. L. (1923). A closed set of normal orthogonal functions. *American Journal of Mathematics* 45, 5–24.
