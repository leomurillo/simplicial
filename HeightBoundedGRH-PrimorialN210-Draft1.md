# Height-Bounded GRH at Primorial $N = 210$: Detection Sensitivity of the Hankel Test

**Leonardo Murillo Montero**

*First draft — May 25, 2026*

---

> **Correction notice (2026-10-08).**  Earlier drafts called Theorems B and C an "unconditional" zero-localization theorem.  **They are withdrawn as theorems.**  Each of the three defects below was checked on 2026-10-08.
>
> 1. *The rejection test is circular.*  The "empirical" matrices $H_n,J_n$ are built from the LMFDB zero list: $\mu_k=\sum_\rho2\gamma_\rho^{-2(k+1)}$ over 1195 listed zeros, all on the critical line, $|\gamma|\le88.8$ (`probe_arch_prime_N210_joint.py`).  So they are moment matrices of a positive measure, and they are PSD *by construction*: $v^{\mathsf T}H_nv=\sum_\rho2\gamma_\rho^{-2}\bigl(\sum_iv_i\gamma_\rho^{-2i}\bigr)^2\ge0$ (identity re-verified to $10^{-300}$).  A hypothetical off-line zero is exactly what the list leaves out, so the "empirical margin" cannot see it.  The premise of §4.1, that the measured matrix "already includes any hypothetical off-line contributions", is false.
> 2. *Even the conditional form is incomplete.*  Suppose the true cumulants were computed independently of any zero list.  The argument would still need an upper bound on the on-line projection $\langle v_-,H^{\mathrm{on\text{-}line}}v_-\rangle$, and §5.2 concedes that none is available.
> 3. *Numerical labels.*  The PSD margins are floating-point numerics at dps 300.  The abstract's "$\sim0.84$" was the prime-part pivot of $J_{14}$, not the total margin.  The §1.3 table's $J$ column and its $n=8$ entry were wrong; the recomputed values are in §1.3.
>
> What survives: Theorem A, the exact closed form of the rank-2 off-line perturbation, and the sensitivity function $\beta(\gamma_0,\delta;n)$.  Read the would-be "rejection map" as a statement about *how strongly* a hypothetical off-line 4-tuple would perturb a Hankel test on the true cumulants.  Certified knowledge about these zeros comes from rigorous zero verification (Platt 2016, §4.4a).  At all heights it also comes from the strip $\delta\le3/8$ ([A], OpenAI 2026, §4.4).

---

## Abstract

**Situation.** ArchStruct (Theorem 1, Corollary 2) supplies the unconditional closed-form arch atomic measure $\sigma_N^{\mathrm{arch}}$ on $(-\infty, 0)$ at every primorial $N \ge 30$ with $H_n^{\mathrm{arch,joint}}(N) \succeq 0$, $J_n^{\mathrm{arch,joint}}(N) \preceq 0$. Pass-5 Theorem 16.2 gives RH $\iff$ the folded-$\Xi$ Hankel gates, for $\zeta$.  A primorial-$N$ version has not been proved (`GRH-Apex-Integration-AdversarialAudit-Draft1.md`, F1); Pass-5 Lemma 16.4 supplies the *constructive sensitivity direction*: off-line zero $\Rightarrow$ finite negative Hankel witness, with the construction following Mergelyan polynomial approximation. The joint primorial probe `probe_arch_prime_N210_joint.py` at mpmath dps=300 over the full LMFDB anchor (48 L-functions of conductor dividing 210) computed $H_n^{\mathrm{total,joint}}(210), J_n^{\mathrm{total,joint}}(210)$ from the LMFDB zero list.  They are PSD at every rung $n \in \{0, 1, 2, 3, 5, 8, 10, 14\}$, as they must be (correction notice, item 1).  At $n=14$ the minimum LDL pivots are $1.3\times10^{-5}$ ($H$) and $1.8\times10^{-6}$ ($J$), and the minimum eigenvalues are $3.3\times10^{-15}$ and $3.8\times10^{-16}$.  (Earlier drafts quoted $\sim0.84$; that is the prime-part pivot of $J_{14}$.)

**Action (as originally planned).** We attempt to turn the finite-rung PSD data into a zero-localization statement by quantifying Pass-5 Lemma 16.4's Mergelyan degree bound and the off-line-zero rank-2 Hankel perturbation kernel. The key technical inputs:

1. **Off-line zero perturbation kernel (§3).** A hypothetical off-line zero of $L(\chi, s)$ at $\rho_0 = 1/2 + \delta + i\gamma_0$ with $\delta > 0$ contributes (via FE 4-tuple) to the joint cumulant $\mu_k^{\mathrm{total,joint}}(210)$ a complex 4-atom whose Hankel perturbation $\Delta H_n^{(\gamma_0, \delta)}$ is rank-2 with signed eigenvalues $\pm \beta(\gamma_0, \delta; n)$, with $\beta$ explicit in $\gamma_0, \delta, n$.

2. **Mergelyan-Christoffel detection threshold (§4).** A polynomial $q$ of degree $n$ exists with $q^T \Delta H_n^{(\gamma_0, \delta)} q < -\eta\|q\|^2$ for $\eta > 0$ explicit in $(\gamma_0, \delta, n, K_{\mathrm{supp}})$, where $K_{\mathrm{supp}}$ is the support of the on-line zero atomic measure (bounded by $1/\gamma_{\min}(210)^2 \approx 50.3$).

3. **Off-line rejection via empirical margin (§5).** If $\eta > \epsilon_{\mathrm{emp}}(n) := \lambda_{\min}(H_n^{\mathrm{total,joint}}(210)) - 0$, then the hypothesized off-line zero would force $\lambda_{\min}(H_n^{\mathrm{total,joint}}(210))$ to be more negative than the empirical floor — contradicting the verified PSD margin. The off-line zero with parameters $(\gamma_0, \delta)$ was claimed to be ruled out at empirical rung $n$.  *(Withdrawn: the margin is computed from on-line zeros only and cannot rule anything out.)*

4. **Solving for the explicit $(T_*, \delta_*)$ region (§6).** The detection-margin inequality $\eta(\gamma_0, \delta; n) > \epsilon_{\mathrm{emp}}(n)$ defines a region $\mathcal R_n \subset \{(\gamma_0, \delta) : \gamma_0 > 0, 0 < \delta < 1/2\}$ in parameter space such that no off-line zero with $(\gamma_0, \delta) \in \mathcal R_n$ was claimed to exist.  *(Withdrawn, as above.)* The complement $\mathcal R_n^c$ is the residual unconstrained region.

**Result.** Three core claims.

1. **Theorem A (Off-line zero perturbation closed form).** For every $\gamma_0 > 0$, $\delta \in (0, 1/2)$, and $n \ge 0$, the rank-2 perturbation $\Delta H_n^{(\gamma_0, \delta)} \in \mathrm{Sym}(\mathbb R^{n+1})$ contributed by an off-line FE 4-tuple at $(\gamma_0, \delta)$ admits the closed-form decomposition
$$\Delta H_n^{(\gamma_0, \delta)} = 4r\bigl[\cos\theta\,(\vec c\,\vec c^T - \vec s\,\vec s^T) - \sin\theta\,(\vec c\,\vec s^T + \vec s\,\vec c^T)\bigr],$$
where $r = 1/(\gamma_0^2 + \delta^2)$, $\theta = \arctan(2\gamma_0\delta/(\gamma_0^2 - \delta^2))$, $\vec c_i = r^i\cos(\theta i)$, $\vec s_i = r^i\sin(\theta i)$. The eigenvalues of $\Delta H_n^{(\gamma_0, \delta)}$ restricted to the 2-dimensional subspace spanned by $\vec c, \vec s$ are $\pm\beta(\gamma_0, \delta; n)$ with
$$\beta(\gamma_0, \delta; n) = 4r\cdot G(r, \theta; n),\qquad G(r, \theta; n) := \sqrt{\|\vec c\|^2\|\vec s\|^2 - \langle\vec c, \vec s\rangle^2 + ...}.$$
(The full expression is computed explicitly in §3.4.)

2. **Criterion B (Empirical-anchored off-line rejection).** Let $\epsilon_{\mathrm{emp}}(n)$ be the minimum LDL diagonal of $H_n^{\mathrm{total,joint}}(210)$ measured at rung $n$. If $\beta(\gamma_0, \delta; n) > \epsilon_{\mathrm{emp}}(n)$ for some $n \le n_{\max}^{\mathrm{probe}}$, then no L-function $L(\chi, s)$ with $\chi$ of conductor dividing 210 has a non-trivial zero at $\rho_0 = 1/2 + \delta + i\gamma_0$.

3. **Target C (Explicit height-bounded GRH region at $n = 14$).** Define
$$\mathcal R_{14} := \{(\gamma_0, \delta) : 0 < \gamma_0 \le T_*(14), \delta_*(14) \le \delta < 1/2, \beta(\gamma_0, \delta; 14) > \epsilon_{\mathrm{emp}}(14)\}.$$
For every $(\gamma_0, \delta) \in \mathcal R_{14}$, no non-trivial zero of any $L(\chi, s)$ of conductor dividing 210 has imaginary part $\gamma_0$ and real-part shift $\delta$. Equivalently:
$$\text{For every }\chi\text{ of conductor }f\mid 210\text{, every non-trivial zero }\rho = 1/2 + \delta + i\gamma\text{ of }L(\chi, s)\text{ with }|\gamma| \le T_*(14)\text{ satisfies }\delta < \delta_*(14).$$
Both $T_*(14)$ and $\delta_*(14)$ would be explicit constants determined by $\epsilon_{\mathrm{emp}}(14)$ (measured: $\lambda_{\min}(H_{14})=3.3\times10^{-15}$) and the closed-form $\beta$. The probe `probe_height_bounded_GRH_N210.py` (to be implemented per this paper) computes the (T_*, $\delta_*$) frontier exactly.

**Harvest (corrected 2026-10-08).** The deliverables are the closed form of Theorem A and the sensitivity function $\beta$.  The claimed "unconditional height-bounded GRH theorem" is withdrawn.  The Hankel data are built from on-line zeros and are PSD by construction, so they reject no off-line configuration.  Zero-localization for $f\mid210$ is already known far beyond this range by rigorous verification (Platt 2016).  At all heights the strip $\delta\le3/8$ holds at tier [A] (OpenAI 2026).

**Keywords:** Generalized Riemann Hypothesis, primorial modulus, Hankel positivity, Mergelyan polynomial approximation, off-line zero, FE cluster, arch atomic measure, joint Dirichlet L-function product, empirical anchor.

---

## 1. Setup

We carry the notation of ArchStruct (Theorem 1, Corollary 2) and the joint primorial probe (`probe_arch_prime_N210_joint.py`).

### 1.1 Joint completed product at $N = 210$

The joint completed L-function at $N = 210$:
$$\Xi_{210}(z) := \xi(1/2 + iz)\prod_{\chi\in\hat X_{210}^\times}\Lambda(\chi, 1/2 + iz).$$
$\hat X_{210}^\times$ contains 47 primitive Dirichlet characters of conductor dividing 210, with parity counts $N_E = 23$, $N_O = 24$ (ArchStruct §6.2). The joint zero set (in folded $z$-coordinate) is the union of zero sets of $\xi$ and $\Lambda(\chi, \cdot)$ for $\chi \in \hat X_{210}^\times$.

### 1.2 Folded cumulants and Hankel matrices

$$\mu_k^{\mathrm{total,joint}}(210) := \sum_{\chi\in\hat X_{210}}\sum_\rho \frac{1}{(-i(\rho - 1/2))^{2(k+1)}}$$
where the inner sum runs over non-trivial zeros of $\Lambda(\chi, s)$ (with $\Lambda(\chi_0, s) := \xi(s)$ for the trivial character).

$\mu_k^{\mathrm{total,joint}}(210) = \mu_k^{\mathrm{arch,joint}}(210) + \mu_k^{\mathrm{prime,joint}}(210)$ (ArchStruct §1.3).

$H_n^{\bullet}(210) := (\mu_{i+j}^{\bullet}(210))_{0\le i,j\le n}$, $J_n^{\bullet}(210) := (\mu_{i+j+1}^{\bullet}(210))_{0\le i,j\le n}$ (Hankel and shifted-Hankel).

### 1.3 Empirical anchor

Recomputed 2026-10-08 at dps 300 from the 1195 listed zeros (`zero_data_N210.py`; minimum $|\gamma|=0.14097$, maximum $88.81$).  Earlier drafts had the $J$ column and the $n=8$ entry wrong.

| $n$ | $\lambda_{\min}(H_n^{\mathrm{total,joint}}(210))$ | $\lambda_{\min}(J_n^{\mathrm{total,joint}}(210))$ |
|---|---|---|
| 0 | 160.0 | 5150 |
| 1 | 55.8 | 74.0 |
| 2 | 29.7 | 11.5 |
| 5 | 0.143 | 0.0463 |
| 8 | 8.0e-5 | 1.7e-5 |
| 10 | 5.8e-8 | 7.1e-9 |
| 14 | 3.3e-15 | 3.8e-16 |

Define $\epsilon_{\mathrm{emp}}^H(n) := \lambda_{\min}(H_n^{\mathrm{total,joint}}(210))$ and $\epsilon_{\mathrm{emp}}^J(n) := \lambda_{\min}(J_n^{\mathrm{total,joint}}(210))$.  At $n = 14$: $\epsilon_{\mathrm{emp}}^H \approx 3.3 \times 10^{-15}$ and $\epsilon_{\mathrm{emp}}^J \approx 3.8 \times 10^{-16}$.  The minimum LDL pivots are larger ($1.3\times10^{-5}$ and $1.8\times10^{-6}$), since a pivot only bounds $\lambda_{\min}$ from above.  These numbers are eigenvalues of moment matrices of a positive measure, the listed zeros, so they are positive by construction.  Their size reflects conditioning ($\lambda_{\max}/\lambda_{\min}\approx10^{64}$ for $H_{14}$), not arithmetic.

### 1.4 Off-line zero parameter space

An *off-line zero* of $L(\chi, s)$ is a non-trivial zero $\rho = 1/2 + \delta + i\gamma$ with $\delta \ne 0$. By the functional equation $\Lambda(\chi, s) = W(\chi)\Lambda(\bar\chi, 1 - s)$, $\rho$ is paired with $1 - \rho = 1/2 - \delta - i\gamma$ (a zero of $\Lambda(\bar\chi, s)$). By complex conjugation in the joint completed product, $\bar\rho = 1/2 + \delta - i\gamma$ is also a zero. So the joint zero set is invariant under the **FE 4-tuple group** $\{(\delta, \gamma) \mapsto (\pm\delta, \pm\gamma)\}$, producing 4 distinct zeros for $\delta \ne 0$, $\gamma \ne 0$.

(For real characters $\chi = \bar\chi$, $\rho$ is also a zero of $\Lambda(\chi, s)$ itself, so the 4-tuple lies in a single L-function; for non-real $\chi$, the 4-tuple is distributed between $L(\chi, s)$ and $L(\bar\chi, s)$.)

We parametrize off-line zeros by $(\gamma_0, \delta)$ with $\gamma_0 > 0$ (WLOG, by FE symmetry) and $\delta \in (0, 1/2)$ (the open critical strip excluding the critical line; WLOG $\delta > 0$).

---

## 2. The folded-coordinate atomic structure

### 2.1 On-line zero atomic representation

For an on-line zero $\rho = 1/2 + i\gamma$ ($\gamma > 0$) of any $\Lambda(\chi, s)$ in the joint product, the FE-conjugate pair $\{\rho, \bar\rho\}$ contributes to the cumulant:
$$\Delta\mu_k^{(\mathrm{on}, \gamma)} = \frac{1}{(-i(i\gamma))^{2(k+1)}} + \frac{1}{(-i(-i\gamma))^{2(k+1)}} = \frac{1}{\gamma^{2(k+1)}} + \frac{1}{\gamma^{2(k+1)}} = \frac{2}{\gamma^{2(k+1)}}.$$
This is the moment sequence of two atoms at $\lambda = 1/\gamma^2 \in (0, \infty)$, each with mass $1$ (or equivalently one atom with mass 2). The atom location is $\lambda(\gamma) = 1/\gamma^2$.

### 2.2 Off-line zero atomic representation

For an off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$, the FE 4-tuple $\{1/2 \pm \delta \pm i\gamma_0\}$ has $-i(\rho - 1/2)$ values $\{\gamma_0 \mp i\delta, -\gamma_0 \pm i\delta\}$, equivalently $\{w, -w, \bar w, -\bar w\}$ with $w := \gamma_0 - i\delta$. Their $-2(k+1)$ powers:
$$w^{-2(k+1)},\;(-w)^{-2(k+1)} = w^{-2(k+1)},\;\bar w^{-2(k+1)},\;(-\bar w)^{-2(k+1)} = \bar w^{-2(k+1)}.$$
(Even powers wash out the sign.) Sum:
$$\Delta\mu_k^{(\mathrm{off}, \gamma_0, \delta)} = 2w^{-2(k+1)} + 2\bar w^{-2(k+1)} = 4\,\mathrm{Re}\,w^{-2(k+1)}.\qquad(2.1)$$

This is a real moment sequence (corresponding to a complex pair of atoms at $z_0 = w^{-2}$ and $\bar z_0 = \bar w^{-2}$, each with mass 2).

### 2.3 Polar form

Let $w = \gamma_0 - i\delta$, so $|w|^2 = \gamma_0^2 + \delta^2 =: \rho^{-1}$. Then $w^{-2} = \bar w^2/|w|^4 = (\gamma_0 + i\delta)^2/(\gamma_0^2 + \delta^2)^2$. Write $w^{-2} = re^{i\theta}$ where
$$r := \frac{1}{|w|^2} = \frac{1}{\gamma_0^2 + \delta^2}, \qquad \theta := 2\arg(\gamma_0 + i\delta) = 2\arctan(\delta/\gamma_0).$$
Then $w^{-2(k+1)} = r^{k+1}e^{i\theta(k+1)}$ and
$$\Delta\mu_k^{(\mathrm{off}, \gamma_0, \delta)} = 4r^{k+1}\cos(\theta(k+1)).\qquad(2.2)$$

**Special cases.**
- $\delta = 0$ (on-line): $\theta = 0$, $r = 1/\gamma_0^2$, $\Delta\mu_k = 4r^{k+1} = 4/\gamma_0^{2(k+1)}$. This is twice the on-line FE-pair contribution (formula 2.1 reduces to a double zero in the degenerate limit). Discontinuity at $\delta = 0$ in zero count.
- $\delta = \gamma_0$ ("close to imaginary axis"): $\theta = \pi/2$, $r = 1/(2\gamma_0^2)$, $\Delta\mu_k = 4r^{k+1}\cos((k+1)\pi/2)$, oscillating $\{4r, 0, -4r^3, 0, 4r^5, ...\}$.

---

## 3. Theorem A — The rank-2 Hankel perturbation closed form

### 3.1 Statement

**Theorem A.** *For every $\gamma_0 > 0$, $\delta \in (0, 1/2)$, $n \ge 0$, the off-line FE 4-tuple at $(\gamma_0, \delta)$ contributes a rank-2 perturbation $\Delta H_n^{(\gamma_0, \delta)} \in \mathrm{Sym}(\mathbb R^{n+1})$ to the Hankel matrix $H_n^{\mathrm{total,joint}}(210)$, with closed-form*
$$\Delta H_n^{(\gamma_0,\delta)}_{ij} = 4r^{i+j+1}\cos(\theta(i+j+1)) = 4r\bigl[r^i\cos(\theta i)\cdot r^j\cos(\theta j)\bigr]\,\cos\theta - 4r\bigl[r^i\sin(\theta i)\cdot r^j\sin(\theta j)\bigr]\,\cos\theta - \ldots$$

*The matrix decomposes in the form*
$$\Delta H_n^{(\gamma_0, \delta)} = 4r\bigl[(\cos\theta)\vec c\vec c^T - (\cos\theta)\vec s\vec s^T - (\sin\theta)(\vec c\vec s^T + \vec s\vec c^T)\bigr] \qquad(3.1)$$
*where $\vec c, \vec s \in \mathbb R^{n+1}$ have components $\vec c_i := r^i\cos(\theta i)$, $\vec s_i := r^i\sin(\theta i)$.*

### 3.2 Proof

By (2.2), $\Delta H_n^{(\gamma_0,\delta)}_{ij} = 4r^{i+j+1}\cos(\theta(i+j+1))$.

Apply the addition formula $\cos(\theta(i+j+1)) = \cos(\theta(i+j))\cos\theta - \sin(\theta(i+j))\sin\theta$, then $\cos(\theta(i+j)) = \cos\theta i\cos\theta j - \sin\theta i\sin\theta j$ and $\sin(\theta(i+j)) = \sin\theta i\cos\theta j + \cos\theta i\sin\theta j$:

$$\cos(\theta(i+j+1)) = \cos\theta[\cos\theta i\cos\theta j - \sin\theta i\sin\theta j] - \sin\theta[\sin\theta i\cos\theta j + \cos\theta i\sin\theta j].$$

Multiply by $r^{i+j+1} = r\cdot r^i\cdot r^j$ and collect:

$$r^{i+j+1}\cos(\theta(i+j+1)) = r\bigl[\cos\theta\,(\vec c_i\vec c_j - \vec s_i\vec s_j) - \sin\theta\,(\vec c_i\vec s_j + \vec s_i\vec c_j)\bigr].$$

Multiplying by 4 and recognizing the outer-product form gives (3.1). $\square$

### 3.3 Rank and eigenvalues

The matrix in (3.1) lies in the rank-2 subspace $\mathrm{span}(\vec c, \vec s)\otimes\mathrm{span}(\vec c, \vec s)$. Restricted to this 2-dimensional subspace and expressed in the (in general non-orthonormal) basis $\{\vec c, \vec s\}$, the matrix is
$$4r\begin{pmatrix}\cos\theta\,\|\vec c\|^2 - \sin\theta\,\langle\vec c,\vec s\rangle & -\cos\theta\,\langle\vec c,\vec s\rangle - \sin\theta\,\|\vec s\|^2 \\ -\cos\theta\,\langle\vec c,\vec s\rangle - \sin\theta\,\|\vec c\|^2 & -\cos\theta\,\|\vec s\|^2 - \sin\theta\,\langle\vec c,\vec s\rangle\end{pmatrix}.$$

Wait — that's the Gram-matrix representation. The eigenvalues of $\Delta H_n^{(\gamma_0,\delta)}$ as an $(n+1)\times(n+1)$ symmetric matrix (not in $\{\vec c, \vec s\}$ basis) are computed from the matrix elements directly.

Cleaner approach. Define $\vec u := (1, e^{i\theta}, e^{2i\theta}, \ldots, e^{ni\theta})^T \in \mathbb C^{n+1}$. Then $\vec u = \vec c + i\vec s$. We have:
$$\Delta H_n^{(\gamma_0,\delta)} = 2r e^{i\theta}\vec u\vec u^T + 2r e^{-i\theta}\bar{\vec u}\bar{\vec u}^T = 2\mathrm{Re}[2re^{i\theta}\vec u\vec u^T].\qquad(3.2)$$

In matrix form, $\Delta H_n^{(\gamma_0,\delta)} = 2\mathrm{Re}[\xi\vec u\vec u^T]$ where $\xi := 2re^{i\theta}$. The (n+1)$\times$2 real matrix $M := (\vec c\;|\;\vec s)$ satisfies
$$\Delta H_n^{(\gamma_0,\delta)} = M\,P\,M^T$$
where $P \in \mathrm{Sym}(\mathbb R^2)$ is
$$P = 4r\begin{pmatrix}\cos\theta & -\sin\theta\\ -\sin\theta & -\cos\theta\end{pmatrix}.$$
$P$ has trace 0, determinant $-4r^2$, eigenvalues $\pm 2r$.

Letting $M = QR$ be the QR-decomposition of $M$ (with $Q \in \mathbb R^{(n+1)\times 2}$ orthonormal, $R$ upper triangular), $\Delta H_n^{(\gamma_0,\delta)} = Q(R P R^T)Q^T$ and the non-zero eigenvalues of $\Delta H_n^{(\gamma_0,\delta)}$ are the eigenvalues of $RPR^T$.

$\det(RPR^T) = \det(R)^2\det(P) = -4r^2\det(R)^2$. So the non-zero eigenvalues are $\pm\sqrt{4r^2\det(R)^2} = \pm 2r|\det R|$.

$\det R = $ (signed area of parallelogram spanned by $\vec c, \vec s$) $= \sqrt{\|\vec c\|^2\|\vec s\|^2 - \langle\vec c,\vec s\rangle^2}$.

So the rank-2 perturbation has signed eigenvalues:
$$\boxed{\lambda_\pm(\Delta H_n^{(\gamma_0,\delta)}) = \pm 2r\sqrt{\|\vec c\|^2\|\vec s\|^2 - \langle\vec c,\vec s\rangle^2} =: \pm\beta(\gamma_0, \delta; n).}\qquad(3.3)$$

### 3.4 The closed-form $\beta(\gamma_0, \delta; n)$

Compute:
$$\|\vec c\|^2 = \sum_{i=0}^n r^{2i}\cos^2(\theta i) = \frac{1}{2}\sum_i r^{2i}(1 + \cos(2\theta i)) = \frac{1}{2}\Bigl[\frac{1-r^{2(n+1)}}{1-r^2} + \mathrm{Re}\,\frac{1 - (r^2e^{2i\theta})^{n+1}}{1-r^2e^{2i\theta}}\Bigr].$$
$$\|\vec s\|^2 = \frac{1}{2}\Bigl[\frac{1-r^{2(n+1)}}{1-r^2} - \mathrm{Re}\,\frac{1-(r^2e^{2i\theta})^{n+1}}{1-r^2e^{2i\theta}}\Bigr].$$
$$\langle\vec c, \vec s\rangle = \sum r^{2i}\cos(\theta i)\sin(\theta i) = \frac{1}{2}\mathrm{Im}\,\frac{1-(r^2e^{2i\theta})^{n+1}}{1-r^2e^{2i\theta}}.$$

Letting $A := (1-r^{2(n+1)})/(1-r^2)$ (the diagonal geometric sum) and $B + iC := (1-(r^2e^{2i\theta})^{n+1})/(1-r^2e^{2i\theta})$:
$$\|\vec c\|^2 = (A + B)/2,\quad \|\vec s\|^2 = (A - B)/2,\quad \langle\vec c, \vec s\rangle = C/2.$$
Then
$$\|\vec c\|^2\|\vec s\|^2 - \langle\vec c, \vec s\rangle^2 = (A^2 - B^2)/4 - C^2/4 = (A^2 - (B^2 + C^2))/4.$$
$B^2 + C^2 = |B + iC|^2 = \frac{|1 - (r^2e^{2i\theta})^{n+1}|^2}{|1 - r^2e^{2i\theta}|^2} = \frac{1 - 2r^{2(n+1)}\cos(2\theta(n+1)) + r^{4(n+1)}}{1 - 2r^2\cos(2\theta) + r^4}.$
$A^2 = (1-r^{2(n+1)})^2/(1-r^2)^2$.

Therefore:
$$\beta(\gamma_0, \delta; n) = 2r\sqrt{\frac{A^2 - (B^2 + C^2)}{4}} = r\sqrt{A^2 - (B^2 + C^2)}.\qquad(3.4)$$

### 3.5 Sharp asymptotic regimes

**Regime I: $r < 1$ (i.e., $|w|^2 > 1$, i.e., $\gamma_0^2 + \delta^2 > 1$), $n \to \infty$.**

$A \to 1/(1-r^2)$, $B^2 + C^2 \to 1/(1 - 2r^2\cos 2\theta + r^4)$.

$$\beta(\gamma_0, \delta; \infty) = r\sqrt{\frac{1}{(1-r^2)^2} - \frac{1}{1 - 2r^2\cos 2\theta + r^4}}.$$

For $\delta$ small (so $\theta \approx 2\delta/\gamma_0$ small, $\cos 2\theta \approx 1 - 2\theta^2$, $r \approx 1/\gamma_0^2$):
$1 - 2r^2\cos 2\theta + r^4 \approx 1 - 2r^2 + 4r^2\theta^2 + r^4 = (1 - r^2)^2 + 4r^2\theta^2$.
$\beta \approx r\sqrt{1/(1-r^2)^2 - 1/((1-r^2)^2 + 4r^2\theta^2)} \approx r\cdot\frac{2r\theta}{(1-r^2)^2}\cdot$ (Taylor)
$= \frac{2r^2\theta}{(1-r^2)^2}$
$\approx \frac{2(\delta/\gamma_0)/\gamma_0^4}{(1-1/\gamma_0^4)^2}\cdot 2$
$= \frac{4\delta/\gamma_0^5}{(1-\gamma_0^{-4})^2}$.

For $\gamma_0 \gg 1$: $\beta \approx 4\delta/\gamma_0^5$.

**Regime II: $r > 1$ (i.e., $\gamma_0^2 + \delta^2 < 1$), $n \ge 1$.**

$A = (r^{2(n+1)} - 1)/(r^2 - 1) \sim r^{2(n+1)}/(r^2 - 1)$.
$B^2 + C^2 \sim r^{4(n+1)}/[(r^2-1)^2 + 4r^2\sin^2\theta]$ for $\theta$ moderate.
$\beta \approx r\cdot r^{2(n+1)}\sqrt{1/(r^2-1)^2 - 1/[(r^2-1)^2 + 4r^2\sin^2\theta]} \sim r^{2n+3}\cdot\theta\cdot$ (constants).

Exponential growth in $n$. Off-line zeros with $\gamma_0$ small (near imaginary axis) produce **massively detectable** perturbations.

**Regime III: $r = 1$ exactly (i.e., $\gamma_0^2 + \delta^2 = 1$), $n \to \infty$.**

$A = n+1$ (sum of 1's). $B + iC = (n+1)$ if $\theta = 0$, otherwise bounded.
$\beta \sim (n+1)\cdot\theta \cdot$ constants. Linear growth in $n$.

### 3.6 The detection condition

A Hankel test at rung $14$ on the *true* cumulants would register an off-line zero with parameters $(\gamma_0, \delta)$ if $\beta(\gamma_0, \delta; 14) > \epsilon_{\mathrm{emp}}^H(14) \approx 3 \times 10^{-15}$.

This is the **detection inequality**.  It is a sensitivity statement, and the current data cannot apply it (correction notice, item 1).

---

## 4. The Mergelyan-Christoffel detection threshold

### 4.1 The naive bound

§3 establishes $\beta(\gamma_0, \delta; n)$ as the worst-case eigenvalue of the rank-2 off-line perturbation. But $\Delta H_n^{(\gamma_0, \delta)}$ is added to the empirical $H_n^{\mathrm{total,joint}}(210)$. The question: when does adding this rank-2 perturbation to an otherwise-positive Hankel matrix break PSD?

**Worst-case bound.** If $\lambda_-(\Delta H_n^{(\gamma_0, \delta)}) = -\beta$ and this eigenvalue is aligned with the smallest direction of $H_n^{\mathrm{total,joint}}(210)$, then
$$\lambda_{\min}(H_n^{\mathrm{total,joint}}(210)) \le \lambda_{\min}(H_n^{\mathrm{total,joint without off-line}}) - \beta.$$

But we don't know $H_n^{\mathrm{total,joint without off-line}}$ separately. The empirical PSD bound applies to the *actual* $H_n^{\mathrm{total,joint}}(210)$ which already includes any hypothetical off-line contributions.

**The correct framing (sensitivity test).** The question becomes: **given the empirical $H_n^{\mathrm{actual}}$ is observed PSD with margin $\epsilon_{\mathrm{emp}}$, what off-line zero configurations are *consistent* with this observation?**

A hypothetical off-line zero at $(\gamma_0, \delta)$ is *consistent* iff there exists an on-line-zero configuration $\{(\gamma_i)_{i \in I}, m_i\}$ such that
$$H_n^{\mathrm{arch}}(210) + H_n^{\mathrm{on-line}}\bigl(\{\gamma_i\}\bigr) + \Delta H_n^{(\gamma_0, \delta)} = H_n^{\mathrm{actual}}(210).$$

The on-line part is *positive semidefinite* (Stieltjes); the arch part is positive semidefinite (ArchStruct Cor 2(i)); the off-line part has rank-2 with eigenvalues $\pm\beta$.

For the actual $H_n^{\mathrm{actual}}$ to satisfy $\lambda_{\min} \ge \epsilon_{\mathrm{emp}}$, the on-line part must *compensate* the negative eigenvalue of the off-line perturbation:
$$H_n^{\mathrm{on-line}}\bigl(\{\gamma_i\}\bigr) \ge \epsilon_{\mathrm{emp}} I + \beta\cdot\vec v_-\vec v_-^T - H_n^{\mathrm{arch}}(210)$$
where $\vec v_-$ is the unit eigenvector for the negative eigenvalue of $\Delta H_n^{(\gamma_0, \delta)}$.

**Compatibility constraint.** This requires the on-line measure $\sigma^{\mathrm{on-line}}$ to have sufficient mass at locations $\lambda = 1/\gamma_i^2$ to produce the required positivity. By the moment problem, this is possible iff the prescribed positivity is *compatible* with a positive measure on $(0, \infty)$.

The structural fact: positive measures on $(0, \infty)$ have ALL Hankel signatures non-negative, including $J_n$ (shifted). So if the prescribed compensation makes $J_n^{\mathrm{on-line, compensation}}$ non-PSD, no on-line measure achieves it — the off-line configuration is **incompatible** with the empirical anchor.

### 4.2 The Mergelyan-Christoffel obstruction

The structural test is: does adding $\Delta H_n^{(\gamma_0, \delta)}$ to a positive Stieltjes Hankel sequence destroy the Stieltjes property?

By Pass-5 Theorem 16.2 (forward Stieltjes), a Stieltjes Hankel sequence has $H_n, J_n \succeq 0$ for all $n$. Adding a rank-2 sign-indefinite perturbation produces a sequence that is **not Stieltjes**. The question: at what rung $n$ does the Stieltjes failure manifest?

By Pass-5 Lemma 16.4 + Mergelyan: a non-real atom at $z_0$ produces a negative Hankel form at degree
$$D(z_0, \epsilon) = O\!\left(\frac{1}{\mathrm{dist}(z_0, \mathbb R_{\ge 0})}\cdot\log\frac{\mathrm{diam}(K)}{\epsilon}\right)$$
where $K \subset \mathbb C$ is a compact set containing all atoms and $\epsilon$ is the target margin.

For $z_0 = w^{-2} = r e^{i\theta}$, $\mathrm{dist}(z_0, \mathbb R_{\ge 0}) = |z_0|\sin|\theta| = r|\sin\theta|$. For small $\delta$: $\theta \approx 2\delta/\gamma_0$, $r \approx 1/\gamma_0^2$, so $\mathrm{dist}(z_0, \mathbb R_{\ge 0}) \approx 2\delta/\gamma_0^3$.

Mergelyan-Christoffel degree:
$$D(\gamma_0, \delta; \epsilon) \approx \frac{\gamma_0^3}{2\delta}\cdot\log\frac{\mathrm{diam}(K)}{\epsilon}.\qquad(4.1)$$

With $\mathrm{diam}(K) \le 1/\gamma_{\min}(210)^2 = 1/0.141^2 \approx 50.3$ (the largest on-line atom at $N = 210$ being chi_105(44)'s $1/\gamma_{\min}^2$) and $\epsilon = \epsilon_{\mathrm{emp}}^H(n_{\mathrm{emp}})$:

$$D(\gamma_0, \delta; \epsilon_{\mathrm{emp}}(14)) \approx \frac{\gamma_0^3}{2\delta}\cdot\log\frac{50.3}{3 \times 10^{-15}} \approx \frac{\gamma_0^3}{2\delta}\cdot 38.$$

### 4.3 The rejection inequality

*(Would-be detection; not applicable to the current data.)*  An off-line zero at $(\gamma_0, \delta)$ would be *flagged at rung $n_{\mathrm{emp}}$* iff
$$D(\gamma_0, \delta; \epsilon_{\mathrm{emp}}(n_{\mathrm{emp}})) \le n_{\mathrm{emp}}.\qquad(4.2)$$

Combining (4.1) and (4.2) with $n_{\mathrm{emp}} = 14$:
$$\frac{\gamma_0^3}{2\delta}\cdot 38 \le 14 \quad\Longleftrightarrow\quad \delta \ge \frac{38\gamma_0^3}{28} = \frac{19\gamma_0^3}{14} \approx 1.36\gamma_0^3.\qquad(4.3)$$

This is the would-be detection condition at $n = 14$ for $\delta \ge 1.36\gamma_0^3$.  Nothing is ruled out by it.

### 4.4 The Vinogradov-Korobov upper bound

Classical unconditional zero-free region for Dirichlet L-functions (Heath-Brown 1992, Theorem 1):
$$L(\chi, \sigma + it) \ne 0 \quad\text{for}\quad \sigma > 1 - \frac{c_{\mathrm{VK}}(N)}{(\log(N(|t|+2)))^{2/3}(\log\log(N(|t|+2)))^{1/3}},$$
with $c_{\mathrm{VK}}(N)$ explicit. At $N = 210$ and $|t| \le T_*$: $\delta < 1/2 - (1 - c_{\mathrm{VK}}/(\log(210 T_*))^{2/3}) = -1/2 + c_{\mathrm{VK}}/(\log(210 T_*))^{2/3}$.

For $T_* = O(1)$ this gives $\delta < 1/2$ (vacuous since $\delta \in (0, 1/2)$ already). For very large $T_*$, the Vinogradov-Korobov region gives $\delta < 1/2 - o(1)$, approaching the edge of the strip. But for our purposes, the VK bound is *not* the binding constraint; we're combining with the empirical-rejection lower bound on $\delta$.

**Uniform strip at all heights ([A], OpenAI 2026).**  OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\operatorname{Re}(s)>7/8$* (30 Sep 2026, `github.com/openai/math`, family 003, Theorem 1.1) states that every Dirichlet $L$-function is zero-free in $\operatorname{Re}s>7/8$.  The result is model-generated.  OpenAI reports that the core statement is Lean-formalized; we have not refereed it.  With the functional equation, every nontrivial zero of every $L(\chi,s)$ with $f\mid 210$ satisfies
$$|\beta - \tfrac12| = \delta \le \tfrac38\qquad\text{at every height }\gamma.$$
This bound is independent of $T_*$, $N$ and $\chi$.  It replaces the vacuous small-height VK bound and the large-height VK bound by the single constant $3/8$.  The bound for $\delta$ here is therefore $\delta\le3/8$, not $\delta<1/2$.

### 4.4a What the strip adds, and what was already known

- *Inside $|\gamma|\le T_*$.*  The strip removes the band $3/8<\delta<1/2$ from the empirical rejection region.  The content specific to Target C becomes $\delta\in[1.36\gamma_0^3,\,3/8]$ (see §4.5).
- *Beyond $T_*$.*  Target C says nothing at $|\gamma|>T_*$.  The strip gives $\delta\le3/8$ there, uniformly and with no height loss.  That is everything this paper's method can currently say above $T_*$, and it comes from 003, not from the Hankel data.
- *Classical numerical verification.*  Rigorous interval-arithmetic computations already verify GRH, with $\delta=0$ exactly, for every primitive character of conductor $q\le 400{,}000$ up to height of order $10^8/q$ (Platt, *Numerical computations concerning the GRH*, Math. Comp. 85 (2016)).  For $f\mid210$ that is height $\gtrsim 4\times10^5$.  So both Target C's region ($|\gamma|\lesssim0.72$) and the strip are strictly contained in what is already known for $f\mid210$.  The value of Target C is methodological: it tests the Hankel/Mergelyan detection mechanism against a known answer.  It adds no knowledge about these zeros.

### 4.5 The compatible $(T_*, \delta_*)$ region

Combining (4.3) (empirical lower bound on $\delta$ to be rejected) with the natural upper bound $\delta < 1/2$ (zero in critical strip):
$$\delta \in [1.36\gamma_0^3,\, 1/2].$$
This is non-empty iff $1.36\gamma_0^3 \le 1/2$, i.e., $\gamma_0 \le (7/19)^{1/3} \approx 0.717$.  (Earlier drafts printed $\approx 0.66$, which was an arithmetic slip: $(1/(2\cdot 19/14))^{1/3}=0.7169$.)

So at rung $n = 14$, the would-be detection region is
$$\mathcal R_{14}^{\mathrm{rough}} = \{(\gamma_0, \delta) : 0 < \gamma_0 \le 0.717,\,\,1.36\gamma_0^3 \le \delta < 1/2\}.$$

With the uniform strip of §4.4 ($\delta\le3/8$, [A] on OpenAI 2026), only the band below $3/8$ would be new:
$$\mathcal R_{14}^{\mathrm{rough},\,\mathrm{new}} = \{(\gamma_0, \delta) : 0 < \gamma_0 \le (21/76)^{1/3}\approx 0.651,\,\,1.36\gamma_0^3 \le \delta \le 3/8\}.$$

**Sharper analysis** using the exact $\beta(\gamma_0, \delta; n)$ from §3.4 (rather than the Mergelyan asymptotic) extends $T_*(14)$ upward. The probe `probe_height_bounded_GRH_N210.py` (to be implemented per §7) computes the exact rejection frontier numerically.

---

## 5. Criterion B — Empirical-anchored off-line rejection (withdrawn as a theorem)

### 5.1 Statement

> *Withdrawn as a theorem (2026-10-08).*  Its hypothesis, a margin "measured empirically", is a property of the matrix of listed on-line zeros, which is PSD by construction.  The proof below also concedes a missing bound.  The statement is kept as a record of the attempted criterion.

**Criterion B.** *Let $\epsilon_{\mathrm{emp}}^H(n) := \lambda_{\min}(H_n^{\mathrm{total,joint}}(210)) > 0$ be measured empirically at mpmath dps=300 via* `probe_arch_prime_N210_joint.py`. *If for some $n \le 14$ the rank-2 perturbation $\Delta H_n^{(\gamma_0, \delta)}$ from a hypothetical off-line FE 4-tuple satisfies*
$$\beta(\gamma_0, \delta; n) > \epsilon_{\mathrm{emp}}^H(n) + \langle\vec v_-, H_n^{\mathrm{arch,joint}}(210)\vec v_-\rangle,$$
*where $\vec v_-$ is the unit negative-eigenvector of $\Delta H_n^{(\gamma_0, \delta)}$, then no L-function $L(\chi, s)$ with $\chi$ of conductor dividing 210 has a non-trivial zero at $1/2 + \delta + i\gamma_0$.*

### 5.2 Proof

Suppose $L(\chi_0, s)$ has a non-trivial zero at $\rho_0 = 1/2 + \delta + i\gamma_0$ for some $\chi_0$ of conductor dividing 210. Then the FE 4-tuple $\{\rho_0, 1-\rho_0, \bar\rho_0, 1-\bar\rho_0\}$ is in the joint zero set, contributing $\Delta H_n^{(\gamma_0, \delta)}$ to the Hankel matrix (§3).

The on-line zeros of $\Lambda(\chi_0, s)$ and of all other $\Lambda(\chi, s)$ in the joint product contribute $H_n^{\mathrm{on-line}}$, a positive semidefinite matrix (atomic measure on $(0, \infty)$). The arch part contributes $H_n^{\mathrm{arch,joint}}(210)$ (ArchStruct, positive semidefinite). Therefore:
$$H_n^{\mathrm{total,joint}}(210) = H_n^{\mathrm{arch,joint}}(210) + H_n^{\mathrm{on-line}} + \Delta H_n^{(\gamma_0, \delta)}.$$

Project onto the unit negative-eigenvector $\vec v_-$ of $\Delta H_n^{(\gamma_0, \delta)}$:
$$\langle\vec v_-, H_n^{\mathrm{total,joint}}(210)\vec v_-\rangle = \langle\vec v_-, H_n^{\mathrm{arch}}\vec v_-\rangle + \langle\vec v_-, H_n^{\mathrm{on-line}}\vec v_-\rangle - \beta(\gamma_0, \delta; n).$$

Since $H_n^{\mathrm{on-line}} \succeq 0$, $\langle\vec v_-, H_n^{\mathrm{on-line}}\vec v_-\rangle \ge 0$. Therefore:
$$\langle\vec v_-, H_n^{\mathrm{total,joint}}(210)\vec v_-\rangle \le \langle\vec v_-, H_n^{\mathrm{arch}}\vec v_-\rangle + \langle\vec v_-, H_n^{\mathrm{on-line}}\vec v_-\rangle - \beta.$$

The LHS is $\ge \epsilon_{\mathrm{emp}}^H(n)$ by the empirical PSD margin (smallest eigenvalue lower bound).  *(This step is the error.  The empirical margin belongs to the matrix of listed zeros, not to $H^{\mathrm{total}}$ including the hypothetical zero.)*

Setting $\alpha := \langle\vec v_-, H_n^{\mathrm{arch}}\vec v_-\rangle$ (computable from ArchStruct, $\ge 0$) and $\gamma := \langle\vec v_-, H_n^{\mathrm{on-line}}\vec v_-\rangle$ (unknown, $\ge 0$):
$$\epsilon_{\mathrm{emp}}^H(n) \le \alpha + \gamma - \beta\quad\Longrightarrow\quad \gamma \ge \epsilon_{\mathrm{emp}}^H(n) - \alpha + \beta.$$

The on-line eigenvalue projection $\gamma$ is bounded above by the on-line total trace, which is bounded by the explicit formula (independent of GRH): $\mathrm{tr}(H_n^{\mathrm{on-line}}) = \sum_k \mu_k^{\mathrm{on-line}}(210) \le \mu_0^{\mathrm{on-line}}(210) \cdot $ (poly factor); but see the next paragraph. $H_n^{\mathrm{on-line}}_{ii} = \mu_{2i}^{\mathrm{on-line}}(210)$.

But there's no explicit upper bound on $\gamma$ without further input — different on-line configurations produce different $\gamma$.

**Closing the proof requires:** showing $\gamma$ cannot grow beyond an explicit upper bound consistent with the other empirical data. This is provided by the *joint shifted Hankel* $J_n^{\mathrm{total,joint}}(210) \succeq 0$ (empirically) — which constrains the on-line part via the Stieltjes condition $H + J \succeq 0$.

**Sharper statement.** If $\beta(\gamma_0, \delta; n) > \epsilon_{\mathrm{emp}}^H(n) + \mathrm{tr}(H_n^{\mathrm{arch,joint}}(210))$, then $\gamma > \mathrm{tr}(H_n^{\mathrm{arch}})$, forcing the on-line contribution to be incompatibly large with the empirical $\mathrm{tr}(H_n^{\mathrm{total}})$. Refinement: the empirical $\mathrm{tr}(H_n^{\mathrm{total}}) = \mathrm{tr}(H_n^{\mathrm{arch}}) + \mathrm{tr}(H_n^{\mathrm{on-line}}) + \mathrm{tr}(\Delta H^{(4)})$, with $\mathrm{tr}(\Delta H^{(4)}) = 0$ (rank-2, traceless). So $\mathrm{tr}(H_n^{\mathrm{on-line}}) = \mathrm{tr}(H_n^{\mathrm{total}}) - \mathrm{tr}(H_n^{\mathrm{arch}})$, computable from data + ArchStruct.

The refined off-line rejection: $\beta(\gamma_0, \delta; n)$ must be compatible with the *spectral* structure of the on-line part, not just the trace. The full compatibility is a generalized moment problem.

For the present paper, we state the rough form of Criterion B and indicate the sharpening via the joint $H + J$ Stieltjes condition. The exact rejection frontier is computed numerically by the probe.

### 5.3 The robust form

**Criterion B (robust form).** *Suppose at empirical rung $n_{\mathrm{emp}} = 14$ the joint Hankel and shifted-Hankel matrices satisfy*
$$H_{14}^{\mathrm{total,joint}}(210), J_{14}^{\mathrm{total,joint}}(210) \succeq \epsilon_{\mathrm{emp}}\cdot I_{15}, \qquad \epsilon_{\mathrm{emp}} \sim 10^{-15}.$$
*Then no L-function $L(\chi, s)$ of conductor $f | 210$ has a non-trivial zero $\rho = 1/2 + \delta + i\gamma_0$ with $\beta(\gamma_0, \delta; 14) > \epsilon_{\mathrm{emp}}$, where $\beta$ is the closed-form expression of $(3.3)$.*

The exact $(\gamma_0, \delta)$ region satisfying $\beta > \epsilon_{\mathrm{emp}}$ is the **rejection frontier** $\mathcal F_{14}$.

---

## 6. Target C — Explicit height-bounded GRH region (not established)

### 6.1 The rejection frontier at $n = 14$

Solve $\beta(\gamma_0, \delta; 14) > \epsilon_{\mathrm{emp}}^H(14) \approx 3 \times 10^{-15}$ for the $(\gamma_0, \delta)$ region.

Using the closed-form $(3.4)$:
$$\beta = r\sqrt{A^2 - (B^2 + C^2)},$$
with explicit $A, B, C$ in terms of $r, \theta, n = 14$.

Numerical solution (to be implemented in `probe_height_bounded_GRH_N210.py`):
- For each grid point $(\gamma_0, \delta) \in (0, T_{\mathrm{max}}] \times (0, 1/2)$, compute $\beta(\gamma_0, \delta; 14)$ via (3.4).
- Mark $(\gamma_0, \delta)$ as "rejected" iff $\beta > \epsilon_{\mathrm{emp}}^H(14)$.
- The rejection region is the union of all such marked points.

**Expected qualitative shape.** From §3.5 asymptotics:
- Regime II ($r > 1$, $\gamma_0^2 + \delta^2 < 1$): $\beta$ grows exponentially in $n$, so $\beta(\gamma_0, \delta; 14)$ is large; rejection is automatic for $\gamma_0$ small.
- Regime I ($r < 1$, large $\gamma_0$): $\beta \sim 4\delta/\gamma_0^5$, small; rejection requires $\delta \gtrsim \epsilon_{\mathrm{emp}}\cdot\gamma_0^5/4 \sim 10^{-15}\gamma_0^5$.

The frontier is roughly: $\delta_*(\gamma_0) \sim \max(10^{-15}\gamma_0^5, 0)$ for $\gamma_0$ moderate; rejection at all $\delta > 0$ for $\gamma_0$ small.

### 6.2 The height-bounded GRH theorem (qualitative)

**Target C.** *There exist explicit positive constants $T_*$ and $\delta_*(\cdot)$ such that, for every primitive Dirichlet character $\chi$ of conductor $f | 210$ and every non-trivial zero $\rho = \beta + i\gamma$ of $L(\chi, s)$:*

- *If $|\gamma| \le T_*$ and $|\beta - 1/2| > \delta_*(|\gamma|)$, this would force $\lambda_{\min}(H_{14}^{\mathrm{total,joint}}(210)) < \epsilon_{\mathrm{emp}}^H(14) \sim 10^{-15}$, contradicting the empirical anchor.*

- *Therefore: every non-trivial zero with $|\gamma| \le T_*$ has $|\beta - 1/2| \le \delta_*(|\gamma|)$.*

*The numerical values of $T_*$ and $\delta_*(\gamma)$ are computed by* `probe_height_bounded_GRH_N210.py`. *Heuristic estimate:* $T_* \approx O(1)$, $\delta_*(\gamma) \approx 10^{-15}\cdot\gamma^5$ *for $\gamma \in (0.1, 1)$.*

*(Withdrawn 2026-10-08.)*  This was presented as an unconditional partial GRH at $N=210$.  It is not; see the correction notice.  The statement is kept as the target the detection mechanism would have to reach.

### 6.3 Scaling with extended empirical anchor

**Extension to $n_{\mathrm{emp}} = 30, 60, 100$.** Each additional empirical rung extends the rejection region. The Mergelyan-Christoffel bound (4.1) gives $D(\gamma_0, \delta; \epsilon) \sim \gamma_0^3/(2\delta)\cdot\log(1/\epsilon)$, so the rejection condition $D \le n$ becomes $\delta \ge \gamma_0^3\log(1/\epsilon)/(2n)$. Doubling $n$ halves the $\delta$ threshold. Doubling again halves further.

At $n = 60$: $\delta_*(\gamma_0) \approx \gamma_0^3 \cdot 38/(2 \cdot 60) \approx 0.32\gamma_0^3$. $T_*(60)$ extended to $\gamma_0 \le (1/(2 \cdot 0.32))^{1/3} \approx 1.16$.

At $n = 100$: $T_*(100) \le 1.36$ etc. Logarithmic-rate scaling.

**Extension to $N = 2310$ (next primorial).** $\gamma_{\min}(2310)$ likely smaller than $\gamma_{\min}(210)$, giving $\mathrm{diam}(K)$ larger and $\epsilon_{\mathrm{emp}}$ different. The combined analysis at $N = 2310$ would extend $T_*$ further, especially for $\gamma_0$ matching $\gamma_{\min}(2310)$.

---

## 7. The implementation probe

`probe_height_bounded_GRH_N210.py`:

```python
"""
Height-bounded GRH theorem at N = 210, empirical anchor at n_emp = 14.

Computes the rejection frontier (gamma_0, delta) for off-line zeros via
the rank-2 perturbation eigenvalue beta(gamma_0, delta; 14) compared to
the empirical PSD margin epsilon_emp(14) = min eigenvalue of H_14 at N=210.

Output: explicit (T_*, delta_*) constants and the rejection region map.
"""

import mpmath
import numpy as np
from zero_data_N210 import sd_all, nsd_all  # LMFDB data

mp.dps = 100

# Step 1: compute epsilon_emp from H_14 at N=210
H14 = compute_H_n_total_joint(N=210, n=14)
eps_emp = min_LDL_diagonal(H14)
print(f"epsilon_emp(14) = {eps_emp}")

# Step 2: for grid of (gamma_0, delta), compute beta
gamma_grid = np.linspace(0.05, 3.0, 100)
delta_grid = np.linspace(0.001, 0.499, 100)
rejection = np.zeros((len(gamma_grid), len(delta_grid)), dtype=bool)
beta_values = np.zeros((len(gamma_grid), len(delta_grid)))

for i, gamma in enumerate(gamma_grid):
    for j, delta in enumerate(delta_grid):
        r = 1 / (gamma**2 + delta**2)
        theta = 2 * mpmath.atan(delta / gamma)
        # Compute A, B, C from §3.4
        A = (1 - r**(2*15)) / (1 - r**2)
        B_plus_iC = (1 - (r**2 * mpmath.exp(2j*theta))**15) / (1 - r**2 * mpmath.exp(2j*theta))
        B = mpmath.re(B_plus_iC)
        C = mpmath.im(B_plus_iC)
        beta = r * mpmath.sqrt(A**2 - (B**2 + C**2))
        beta_values[i, j] = float(beta)
        rejection[i, j] = beta > eps_emp

# Step 3: extract T_* and delta_*(gamma)
T_star = max(gamma_grid[i] for i in range(len(gamma_grid)) if any(rejection[i, :]))
delta_star = {gamma: min(delta for delta in delta_grid if rejection[gamma, delta])
              for gamma in gamma_grid[gamma_grid <= T_star]}

print(f"T_*(14) = {T_star}")
for gamma, delta in delta_star.items():
    print(f"  gamma = {gamma:.3f}: delta_*(gamma) = {delta:.6e}")

# Output: explicit table for paper inclusion.
```

The probe outputs the explicit $(T_*, \delta_*(\cdot))$ values that make Target C concrete.

---

## 8. Discussion and program impact

### 8.1 What this delivers

- **Theorem A** [P, exact algebra]: the closed form of the rank-2 off-line perturbation $\Delta H_n^{(\gamma_0,\delta)}$ and its eigenvalues $\pm\beta$.
- **The sensitivity map** $\beta(\gamma_0,\delta;n)$ [numerics]: how strongly a Hankel test on the *true* cumulants would register a hypothetical off-line 4-tuple.
- **A diagnosis.**  A finite-rung Hankel test built from a zero list is PSD by construction.  It cannot reject zeros the list omits.

Withdrawn 2026-10-08: the "new unconditional theorem", the "computer-verified partial GRH", and the scaling claim that extending $n$ on these matrices extends $T_*$.

### 8.2 What this does not deliver

- **Not full GRH at $N = 210$.** Off-line zeros with very small $\delta$ (close to the critical line) escape the empirical detection.
- **Not new knowledge about these zeros.** Platt's rigorous verification (2016) already places every zero of $L(\chi,s)$, $f\mid210$, on the critical line up to height $\gtrsim4\times10^5$. The uniform strip $\delta\le3/8$ at all heights is OpenAI 2026 ([A], §4.4). Target C is a calibration of the detection mechanism against known ground truth (§4.4a).
- **Not GRH at higher primorials** without re-running the probe at $N = 2310, 30030, \ldots$
- **Not RH for $\zeta$** directly. The joint product at $N = 210$ includes only Dirichlet L-functions of conductor $f | 210$, plus $\xi$ (which is the trivial-character L-function). RH for $\zeta$ at heights $|\gamma| \le T_*$ is included.

### 8.3 What this does for the program

- It shows where the finite Hankel route needs independent input.  The true cumulants $\mu_k$ must come from the arithmetic side, not from a zero list.  That means primes plus the archimedean term via the explicit formula, or the Taylor coefficients of $\log\Lambda(\chi,\cdot)$ at $s=1/2$.
- Given that input plus certified completeness of the low zeros, the test reduces to classical zero verification, which already settles $f\mid210$ far beyond this range.  So the route offers calibration of the detector, not new zero-localization.
- It is a worked instance of the program's own rule: numerics are not theorems, and a positivity check must be run on an object that could have failed.

### 8.4 Relationship to classical GRH literature

The theorem is *complementary* to classical zero-density estimates:
- Classical (Heath-Brown 1992): bounds the *number* of off-line zeros in a region; does not exclude individual zeros.
- This paper, as first drafted, aimed to *exclude individual off-line zeros* in a region.  That exclusion is withdrawn (correction notice).

The "explicit-formula-free" framing of earlier drafts was the source of the error.  Without the explicit formula, or another zero-free evaluation of $\mu_k$, the cumulants can only be built from a zero list.  A zero list already presupposes where the zeros are.

### 8.5 Path to extension

Three concrete next steps:

0. **Make the cumulants zero-free first.**  Compute $\mu_k$ from the arithmetic side (explicit formula, or derivatives of $\log\Lambda(\chi,s)$ at $s=1/2$), independently of `zero_data_N210.py`.  Only then is a PSD check a test.  Extending $n$ on the zero-list matrices adds nothing.
1. **Run `probe_height_bounded_GRH_N210.py`** to compute the explicit $(T_*, \delta_*)$ numerical values.
2. **Extend the empirical probe to $n_{\mathrm{emp}} = 30, 60$** at $N = 210$ (computational: $\sim$ days at dps=400).
3. **Replicate at $N = 2310$** with appropriate LMFDB zero data (computational: $\sim$ weeks of zero computation + analysis).

The sequence delivers progressively stronger height-bounded GRH theorems.

---

## 9. References

- ArchStruct: `Arch-Structural-Theorems-Draft1.md`. Theorem 1, Corollary 2 — unconditional arch atomic measure.
- Pass-5 Theorem 16.2 + Lemma 16.4: `RH-Pass5-LockANoLoss-BornHeatFlow-Draft1.md` §16. Apex Lemma$_{HJ}$ equivalence + Mergelyan sensitivity.
- Joint primorial probe: `probe_arch_prime_N210_joint.py` + `zero_data_N210.py`. Empirical anchor at $n \le 14$.
- §17 audit: `PassFive-Section17-Audit-Draft1.md`. Mergelyan-Christoffel construction.
- Cubic-shift bypass: `Unconditional-Positivity-CubicShiftBypass-Draft1.md`. Structural framing of why this is the right next-step deliverable.
- OpenAI (2026). The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\operatorname{Re}(s)>7/8$. 30 September 2026, `github.com/openai/math`, family 003 (model-generated; Lean formalization reported by OpenAI). Tier [A].
- Platt, D. J. (2016). Numerical computations concerning the GRH. *Math. Comp.* 85, 3009–3027.
- Heath-Brown, D. R. (1992). Zero-free regions for Dirichlet L-functions. *Proc. London Math. Soc.* 64, 265–338.
- Iwaniec, H. and Kowalski, E. (2004). *Analytic Number Theory*. AMS Colloquium 53.
- Mergelyan, S. N. (1952). Uniform approximations of functions of a complex variable. *Uspekhi Mat. Nauk* 7.

## 10. Files

- This note: `HeightBoundedGRH-PrimorialN210-Draft1.md`.
- Implementation probe: `probe_height_bounded_GRH_N210.py` (to be implemented).
- Empirical anchor: `probe_arch_prime_N210_joint.py` + `zero_data_N210.py` (existing).

---

*Correction, 2026-10-08.  The closing line of May 25 read: "The simplicial framework + empirical anchor delivers a genuine unconditional partial-GRH theorem at primorial $N = 210$."  It does not.  The empirical anchor is PSD by construction, because it is built from on-line zeros, so it carries no information about off-line ones.  What is real is Theorem A, the sensitivity function $\beta$, and the diagnosis of §8.3.  The next step that could make the route a test is to compute the cumulants from the arithmetic side, independently of any zero list.*

— Director, May 25, 2026; corrected October 8, 2026
