# The Diagonal Cumulant Tower of Negative Entropy in Simplicial Coordinates: All-Orders Frozen-Geometry Factorization and the Legendre Bridge

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Draft 1 — June 2026*

**Companion note.** This is the order-$n$ extension of the information-geometric trilogy **01 / 01b / 01c**. Paper **01c** (*The Moving Amari–Chentsov Cubic in Simplicial Coordinates*) carried the order-$3$ object — the Amari–Chentsov cubic $T=\nabla^3\varphi$ — across the whole categorical simplex and isolated its position dependence as a single breathing diagonal $D_p=\operatorname{diag}(1/p_i)$. The present note climbs the **whole tower** $T^{(n)}=\nabla^n\varphi$ for the negative-entropy potential $\varphi(p)=\sum_i p_i\log p_i$, shows that the frozen-geometry $\times$ breathing-diagonal factorization **survives every order**, and welds the result to the program's cumulant-tower line (the $\heb{ל}2$ log-partition tower of *T2*) by Legendre duality. Numbers prefixed "01c." / "01." / "21." / "T2." refer to those manuscripts. Every displayed identity is certified exactly in `empirical_forward2/cert_cumulant_tower.py` (sympy only; **CERT GREEN**, 9 checks, residuals exact zeros over $\mathbb{Q}$ or $\mathbb{Q}(p_i)$).

---

## Abstract

The information geometry of the categorical $(N-1)$-simplex, written in simplicial (zero-sum, mixture-affine) coordinates, has a single convex potential $\varphi(p)=\sum_i p_i\log p_i$ whose Hessian is the Fisher metric (01c, Prop. 3.1) and whose third derivative is the moving Amari–Chentsov cubic (01c, Thm. 4.1). We compute the **entire derivative tower** $T^{(n)}=\nabla^n\varphi$ and prove three facts, all certified in exact arithmetic.

**(i) The tower is purely diagonal, with a factorial coefficient.** For every $n\ge2$,
$$T^{(n)}_{i_1\cdots i_n}=(-1)^n\,(n-2)!\;\frac{1}{p_i^{\,n-1}}\quad\text{when }i_1=\cdots=i_n=i,\qquad\text{and }0\text{ otherwise.}$$
The off-diagonal components vanish identically: $\nabla^n\varphi$ is supported on the main diagonal of the index lattice at all orders.

**(ii) The frozen-geometry factorization survives all orders.** The tower factors as
$$T^{(n)}=c_n\;\Delta^{(n)}\;D_p^{\,n-1},\qquad c_n=(-1)^n(n-2)!,\quad D_p=\operatorname{diag}(1/p_i),$$
where $\Delta^{(n)}$ is the **position-independent** fully-diagonal (all-equal-index) selector. The combinatorial part $\Delta^{(n)}$ is frozen across the simplex; the only object that breathes is the diagonal Fisher reweighting $D_p^{\,n-1}$; the coefficient is the pure integer $c_n$. At $n=2$ this is the Fisher metric ($\Delta^{(2)}=I$, $c_2=+1$); at $n=3$ it is the cubic ($c_3=-1$). This is the order-$n$ statement of the 01c picture: a fixed combinatorial skeleton listened to through a position-dependent diagonal gain.

**(iii) Legendre bridge to the log-partition tower.** $\varphi$ is the convex conjugate of the log-partition $\Phi(\eta)=\log\sum_i e^{\eta_i}$. The program's $\heb{ל}2$ tower (*T2*) lives on the $e$-affine ($\eta$) side and reads the **all-distinct-index** joint cumulant $\kappa_n=(-1)^{n-1}(n-1)!\,m^{-n}$ at the uniform point. The diagonal $\varphi$-tower of this note is the dual, $m$-affine, **all-equal-index** object. At the uniform point the two are sign-opposite at every order — the $e\!\leftrightarrow\!m$ (i.e. $\alpha\to-\alpha$) involution that is self-dual at order $2$ (Fisher) and flips at order $3$ (the cubic).

We are explicit about the novelty boundary (§6): the diagonal third-derivative formula and the closed cumulant tower are classical exponential-family facts; what is organized here is the **order-$n$ frozen $\times$ breathing factorization** in the overcomplete simplicial frame, its certified survival at all orders, and the precise placement of the diagonal $\varphi$-tower as the Legendre dual of the program's distinct-index $\Phi$-tower. We also assess, honestly and negatively, the relation to the $N=4$ quartic obstruction of Paper 21 (§5): the diagonal $\varphi$-tower does **not** reproduce that obstruction; it is the dual object in the complementary chart, and the very feature Paper 21 is about — the $2{+}2$ Wick block — is absent from the diagonal tower by construction.

**Keywords:** information geometry, categorical simplex, cumulant tower, negative entropy, Fisher metric, Amari–Chentsov tensor, higher cumulants, Legendre duality, dually flat, log-partition, simplicial coordinates, Quadray coordinates, conductor blind spot.

**MSC 2020:** 53B12, 62B10, 94A17, 15A72, 53A45.

---

## 1. Setup: one potential, two charts

Let $\Delta=\{p\in\mathbb{R}^N:p_i>0,\sum_ip_i=1\}$ be the open categorical $(N-1)$-simplex, with tangent space at every interior $p$ the zero-sum hyperplane $H=\{v:\sum_iv_i=0\}$ of Papers 01/01b/01c. Two convex potentials, Legendre-dual to each other, organize the geometry:

- the **mixture-chart** potential (negative Shannon entropy)
$$\varphi(p)=\sum_{i=1}^N p_i\log p_i,\qquad p\in\Delta\ \text{(the $m$-affine chart, 01c Prop. 3.1)};$$
- the **exponential-chart** potential (log-partition)
$$\Phi(\eta)=\log\sum_{i=1}^N e^{\eta_i},\qquad \eta\in H\ \text{(the $e$-affine chart, T2 §1)}.$$

They are conjugate, $\Phi^*=\varphi$ up to gauge, with $\nabla\Phi=p$ and $\nabla\varphi=\theta=\log p\bmod\mathbf 1$ (01c Prop. 3.1; T2 §1). The program's cumulant-tower paper *T2* (the trilogy's $\heb{ל}2$) develops the tower $\nabla^n\Phi$ on the $\eta$-side. **This note develops the dual tower $\nabla^n\varphi$ on the $p$-side**, and then connects the two.

The distinction matters and is the source of every honest caveat below: the two towers are different tensors, not coordinate re-expressions of one another. The $\Phi$-tower is the cumulant tower of the sufficient statistic (covariance, skewness, …); the $\varphi$-tower is the derivative tower of the entropy. They meet only through the Legendre map, and at the uniform point they are sign-related but not equal.

---

## 2. The diagonal cumulant tower

### 2.1 The scalar seed

The potential $\varphi$ is a **separable sum** $\varphi(p)=\sum_i g(p_i)$ of the single-variable seed $g(t)=t\log t$. Separability is the engine of everything: mixed partials across distinct coordinates vanish before any simplex structure is invoked.

**Lemma 2.1 (diagonal scalar law).** *For the seed $g(t)=t\log t$ and every integer $n\ge2$,*
$$\frac{d^n}{dt^n}\big(t\log t\big)=(-1)^n\,(n-2)!\;\frac{1}{t^{\,n-1}}.$$
*The coefficient $c_n:=(-1)^n(n-2)!$ runs $1,-1,2,-6,24,\dots$ for $n=2,3,4,5,6$.*

*Proof.* $g'(t)=\log t+1$, so $g''(t)=1/t=t^{-1}$. For $n\ge2$ write $g^{(n)}=\frac{d^{\,n-2}}{dt^{\,n-2}}t^{-1}$. The repeated derivative of $t^{-1}$ is $\frac{d^{k}}{dt^{k}}t^{-1}=(-1)^k\,k!\,t^{-(k+1)}$; setting $k=n-2$ gives $g^{(n)}=(-1)^{n-2}(n-2)!\,t^{-(n-1)}=(-1)^n(n-2)!\,t^{-(n-1)}$, using $(-1)^{n-2}=(-1)^n$. $\square$

Certified for $n=2,\dots,6$ over $\mathbb{Q}(t)$ as **C1** in the certificate, together with the explicit coefficient table.

### 2.2 The tower is purely diagonal

**Theorem 2.2 (diagonal tower).** *Let $\varphi(p)=\sum_ip_i\log p_i$ on the $N$-simplex. For every $n\ge2$ and every multi-index $(i_1,\dots,i_n)$,*
$$T^{(n)}_{i_1\cdots i_n}:=\frac{\partial^n\varphi}{\partial p_{i_1}\cdots\partial p_{i_n}}=\begin{cases}(-1)^n\,(n-2)!\,/\,p_i^{\,n-1}, & i_1=\cdots=i_n=i,\\[2pt]0,&\text{otherwise (any two indices differ).}\end{cases}$$
*Thus $T^{(n)}$ is supported entirely on the main diagonal of the index lattice, at all orders.*

*Proof.* By separability $\varphi=\sum_kg(p_k)$, so $\partial^n\varphi/\partial p_{i_1}\cdots\partial p_{i_n}=\sum_k\partial^n g(p_k)/\partial p_{i_1}\cdots\partial p_{i_n}$. The term $g(p_k)$ depends on $p_k$ alone, so its $n$-th mixed partial is nonzero only if every differentiation index equals $k$, i.e. only the all-equal multi-index $(k,\dots,k)$ survives, contributing $g^{(n)}(p_k)$. If the multi-index has two distinct entries, no single $k$ matches all of them and the whole sum vanishes. When $i_1=\cdots=i_n=i$, the surviving term is $g^{(n)}(p_i)=(-1)^n(n-2)!\,p_i^{-(n-1)}$ by Lemma 2.1. $\square$

The certificate verifies this **exhaustively** for $N=4$ over all $4^n$ multi-indices, $n=2,\dots,6$ (**C2**), with an $N=5$ spot check at orders $2$–$4$ (**C2'**). Because these are exact identities in $\mathbb{Q}(p_i)$, they hold for all interior $p$, not a sampled family.

A clarifying contrast: the **mixture-chart** $\varphi$-tower is purely diagonal, but the **exponential-chart** $\Phi$-tower is *not* — $\Phi$ is non-separable ($Z=\sum_je^{\eta_j}$ couples all coordinates), so $\nabla^n\Phi$ has rich off-diagonal structure (it is, after all, the full joint cumulant tower of the sufficient statistic). Diagonality is a feature of the entropy potential, not of information geometry per se.

### 2.3 The frozen $\times$ breathing factorization, at all orders

Write $D_p=\operatorname{diag}(1/p_i)$ for the Fisher diagonal of 01c, and let $\Delta^{(n)}$ denote the **fully-diagonal selector** — the constant order-$n$ array with $\Delta^{(n)}_{i\cdots i}=1$ and all non-diagonal entries $0$. $\Delta^{(n)}$ is a pure combinatorial object: it encodes "all indices equal," carries no $p$-dependence, and is the same at every point of the simplex.

**Theorem 2.3 (all-orders frozen-geometry factorization).** *For every $n\ge2$,*
$$\boxed{\;T^{(n)}=c_n\,\Delta^{(n)}\,D_p^{\,n-1},\qquad c_n=(-1)^n(n-2)!\;}$$
*meaning $T^{(n)}_{i_1\cdots i_n}=c_n\,\Delta^{(n)}_{i_1\cdots i_n}\,(1/p_i^{\,n-1})$ on the diagonal $i_1=\cdots=i_n=i$ and $0$ off it. The factors carry the structure cleanly:*

- *the **scalar** $c_n$ is a pure integer (a factorial with sign): $\partial_{p_k}c_n\equiv0$;*
- *the **combinatorial** $\Delta^{(n)}$ is frozen — position-independent: $\partial_{p_k}\Delta^{(n)}\equiv0$;*
- *the **diagonal** $D_p^{\,n-1}=\operatorname{diag}(1/p_i^{\,n-1})$ is the only breathing piece, with $\partial_{p_i}(1/p_i^{\,n-1})=-(n-1)/p_i^{\,n}$.*

*Proof.* Immediate from Theorem 2.2: the displayed product reproduces the diagonal value $c_n/p_i^{\,n-1}$ and vanishes off the diagonal because $\Delta^{(n)}$ does. The three breathing/non-breathing statements are the elementary derivatives just listed. $\square$

Certified as **C3** (the product identity over all $4^n$ indices, plus the explicit position-independence of $\Delta^{(n)}$ and $c_n$ and the breathing law of $D_p^{\,n-1}$).

**Reading.** This is exactly the 01c moral — "the cross-product geometry is frozen; only the Fisher weights move" — promoted to every order. At order $2$ the geometry is trivial ($\Delta^{(2)}=I$, no skewness) and $D_p^{1}=\operatorname{diag}(1/p_i)$ is the Fisher metric. At order $3$ the geometry is still the diagonal selector but the breathing is $D_p^{2}$, and the raised version is the cross-product object of 01c (§4 below). At order $n$ the picture does not degrade: the combinatorial skeleton stays the single fixed diagonal selector, and *all* of the position dependence is the single diagonal $D_p^{\,n-1}$ with the factorial gain $c_n$. There is no "new geometry per order" in the mixture chart — a sharp statement that, as §5 explains, is precisely *why* the new order-$4$ content of Paper 21 lives in the **other** chart.

---

## 3. Order $2$ and order $3$: reduction to Fisher and to the cubic

The bottom two rungs reproduce the established objects, which both anchors the tower and pins the normalization.

**Proposition 3.1 ($n=2$: the Fisher metric).** *At order $2$, $\Delta^{(2)}=I$, $c_2=+1$, and*
$$T^{(2)}=D_p=\operatorname{diag}(1/p_i)=\operatorname{Hess}\varphi=g_p,$$
*the Fisher metric of 01c Prop. 3.1; on tangent vectors $g_p(u,v)=\sum_iu_iv_i/p_i$.*

*Proof.* Theorem 2.3 at $n=2$ gives $T^{(2)}_{ij}=\delta_{ij}/p_i$, the Hessian of $\varphi$ (01c). The bilinear form on $H$ is $\sum_{i}u_iv_i/p_i$. $\square$ (Certified **C4**.)

**Proposition 3.2 ($n=3$: the moving Amari–Chentsov cubic).** *At order $3$, $c_3=-1$ and the diagonal third cumulant is $T^{(3)}_{iii}=-1/p_i^2$. Its metric-raised form is the moving cubic of 01c Thm. 4.1,*
$$K^{CH}_p(u)v=D_p(u\odot v)-\langle u,v\rangle_{g_p}\,p,\qquad g_p\!\big(K^{CH}_p(u)v,\,w\big)=\sum_i\frac{u_iv_iw_i}{p_i^2}=T_p(u,v,w),$$
*a totally symmetric $3$-tensor on $H$ that reduces at $p_*=\tfrac14\mathbf 1$ to the Corollary 01.3.9 form $K^{CH}_{p_*}(u)v=4(u\odot v)-(\sum_iu_iv_i)\mathbf 1$.*

*Proof.* The diagonal value is Theorem 2.2 at $n=3$. The raising identity, total symmetry on $H$, and the $p_*$ reduction are 01c Thm. 4.1; we re-certify them here (the raised cubic equals the skewness tensor after imposing $\sum w_i=0$; symmetry under $u\!\leftrightarrow\!v$ and $v\!\leftrightarrow\!w$ with all three zero-sum; the $p_*$ reduction componentwise) as **C5**. $\square$

The covariant cubic $T_p(u,v,w)=\sum_iu_iv_iw_i/p_i^2$ has the same diagonal coefficient $c_3=-1$ as the abstract tower, now visible as the $1/p_i^2$ weight; the cross-product-square realization of $\odot$ (01.3.8) is the *frozen* part, $D_p^{2}$ the *breathing* part — Theorem 2.3 at $n=3$.

---

## 4. The conductor blind spot, made concrete at every order

The **conductor blind spot** (CBS) is the program's name for the failure of an order-$2$ instrument to see anything beyond the metric $g=T^{(2)}$ (01c §6; *T2* §4; Paper 34). The factorization gives a clean, certified worked instance of *what is invisible at order $2$, made explicit at order $n$*.

**Statement.** An order-$2$ instrument measures $T^{(2)}=D_p$, the Fisher metric, and is blind to $T^{(n)}$ for $n\ge3$. Theorem 2.3 says exactly what it is blind to: a *fixed* combinatorial skeleton $\Delta^{(n)}$, reweighted by $D_p^{\,n-1}$, with factorial gain $c_n$. The hidden content is therefore not a sequence of qualitatively new geometric objects — in the mixture chart it is the **same diagonal selector at every order**, only the diagonal gain $D_p^{\,n-1}$ and the integer $c_n$ change. The blind spot is one-dimensional per coordinate: along ray $i$, the invisible tower is the single scalar sequence $c_n/p_i^{\,n-1}$, i.e. the derivative tower of $g(p_i)=p_i\log p_i$ at $p_i$.

This sharpens the CBS reading in 01c §6. There the order-$2$/order-$3$ split was "metric versus cubic"; here the split is "metric versus the *entire* breathing-diagonal tower," and the tower has a closed form. The order-$2$ instrument sees $D_p$; the order-$n$ residual it misses is $c_n\Delta^{(n)}D_p^{\,n-1}$, a frozen skeleton modulated by a power of the same diagonal it already measures. The information missed at each higher order is, in the mixture chart, "the next power of the metric's own diagonal."

A complementary remark connects to the program's *moment-vs-cumulant* line. The uniform categorical has **fully diagonal moments** $\mathbb{E}[X_{i_1}\cdots X_{i_m}]|_u=N^{-1}[i_1=\cdots=i_m]$ (Paper 21 §5.1). The $\varphi$-tower's diagonality is the *entropy-side* shadow of that moment diagonality: both are supported only on all-equal indices. But the **cumulant** tower in the $\eta$-chart is *not* diagonal — that is where the Wick subtractions live (Paper 21), and it is the subject of §5.

---

## 5. The quartic obstruction (Paper 21): an honest non-match

Paper 21 (*The Quartic Force Law at Cumulant Order Four*) identifies a qualitatively new feature at order $4$: read in the **additive-character basis** of $\mathbb{Z}/N$, the fourth cumulant of the **log-partition** family carries a Gaussian (Wick) subtraction,
$$Q(\chi_a,\chi_b,\chi_c,\chi_d)\big|_u=\delta_{a+b+c+d\equiv0}-\delta_{a+b\equiv0}\delta_{c+d\equiv0}-\delta_{a+c\equiv0}\delta_{b+d\equiv0}-\delta_{a+d\equiv0}\delta_{b+c\equiv0},$$
and on $\mathbb{Z}/30$ supports $914$ connected three-prime quartic vertices with no quadratic or cubic shadow (Paper 21 §5). The natural question (01c open problem D3): does the order-$4$ rung of *this* note relate to that obstruction?

**The honest answer is no — and the reason is structural, certified, and informative.** Paper 21's $Q=\nabla^4\Phi$ is the **log-partition** ($\eta$-chart) tensor; it is **non-diagonal**, and its load-bearing feature is precisely the $2{+}2$ block (the Wick pairing). This note's $T^{(4)}=\nabla^4\varphi$ is the **Legendre-dual entropy** ($p$-chart) tensor; by Theorem 2.2 it is **purely diagonal** and therefore has **no $2{+}2$ block at all**.

**Proposition 5.1 (the towers part company at the $2{+}2$ block).** *At the uniform point $p_*=\tfrac14\mathbf 1$ on $N=4$:*

- *(entropy chart) every mixed component $T^{(4)}_{iijj}$ with $i\ne j$ of $\nabla^4\varphi$ vanishes — the $\varphi$-tower has no Wick block;*
- *(log-partition chart) the corresponding mixed component of $\nabla^4\Phi$ is nonzero (e.g. $\partial^4\Phi/\partial\eta_1^2\partial\eta_2^2|_{\eta=0}=-\tfrac{3}{128}$) — the $\Phi$-tower carries exactly the $2{+}2$ Wick structure Paper 21 isolates.*

*Proof.* The first is Theorem 2.2 ($i\ne j$ forces a mixed multi-index, hence $0$). The second is a direct fourth derivative of $\Phi=\log\sum_je^{\eta_j}$ evaluated at $\eta=0$. Both certified as **C8**. $\square$

So Paper 21's obstruction is a statement about the **non-diagonal** cumulants in the exponential chart; the diagonal entropy tower of this note is, by construction, exactly the part of the order-$4$ data that does **not** carry the obstruction. This is not a failure of either object — it is the cleanest possible illustration of why the program reads the quartic obstruction in the $\Phi$/character chart and not in the $\varphi$/mixture chart: **the obstruction lives off the diagonal, and the entropy tower is on the diagonal.**

What *does* survive across the Legendre map is the **scalar coefficient and its sign**: the diagonal $\varphi$-tower has $c_4=+2$ (so $T^{(4)}_{iii}=+2/p_i^3$), while the distinct-index $\Phi$-cumulant is $\kappa_4=-6/m^4$ at the uniform; the two are sign-opposite, the order-$4$ instance of the $\alpha\to-\alpha$ involution (§6 below; certified **C6**, **C8(c)**). The connection to Paper 21 is therefore at the level of *the dual involution and the factorial coefficients*, not at the level of the obstruction, which is genuinely a $\Phi$-chart phenomenon.

This corrects a tempting overclaim: one might hope the entropy tower "sees" the quartic obstruction because both are order-$4$ objects on the same simplex. It does not. The honest placement is that the entropy tower is the diagonal Legendre shadow, and the obstruction is the off-diagonal Wick content of the conjugate potential.

---

## 6. Legendre bridge to the program's $\Phi$-tower; novelty boundary

### 6.1 The two towers at the uniform point

The program's $\heb{ל}2$ paper (*T2*, Prop. 6.2) gives the **all-distinct-index** joint cumulant of the log-partition family on $m$ points,
$$\kappa_n=(-1)^{n-1}(n-1)!\,m^{-n},\qquad\text{CGF}=\log(1+t/m),$$
and identifies its $\alpha\to-\alpha$ dual involution: self-dual at $n=2$ (Fisher), flipped at $n=3$ (the cubic). The diagonal $\varphi$-tower of this note is the conjugate object. At the uniform point $p_i=1/m$:

| order $n$ | $\varphi$-tower (this note, $m$-chart, **diagonal** $i{=}\cdots{=}i$) | $\Phi$-tower (T2, $e$-chart, **distinct** indices) |
|---|---|---|
| $2$ | $T^{(2)}_{ii}=c_2 m^{1}=+m$ | $\kappa_2=-1/m^{2}\cdot$… (sign $-$) |
| $3$ | $T^{(3)}_{iii}=c_3 m^{2}=-m^2$ | $\kappa_3=+2/m^{3}$ (sign $+$) |
| $4$ | $T^{(4)}_{iiii}=c_4 m^{3}=+2m^3$ | $\kappa_4=-6/m^{4}$ (sign $-$) |
| $n$ | $c_n m^{\,n-1}$, $c_n=(-1)^n(n-2)!$ | $(-1)^{n-1}(n-1)!\,m^{-n}$ |

**Proposition 6.1 (dual sign involution).** *For every $n\ge2$, $\operatorname{sign}(c_n)=(-1)^n$ and $\operatorname{sign}(\kappa_n)=(-1)^{n-1}$; hence the diagonal $\varphi$-tower and the distinct-index $\Phi$-tower are **sign-opposite at every order**. The flip is the $e\!\leftrightarrow\!m$ (equivalently $\alpha\to-\alpha$) duality: the Fisher rung ($n=2$) is the self-dual axis, and the cubic rung ($n=3$) is the first flip.* (Certified **C6**, **C8(c)**.)

The structural content is that the *factorial growth* and the *alternating sign* are shared between the two charts (both are governed by derivatives of a $\log(1\pm\cdot)$-type seed: $\log(1+t/m)$ for $\Phi$, and $g=t\log t\Rightarrow g''=1/t$ generating $\pm(n-2)!$ for $\varphi$), while the *power of $m$* inverts ($m^{\,n-1}$ vs $m^{-n}$) — the Jacobian of the Legendre map acting order by order. This is the order-$n$ refinement of T2's Prop. 6.2: T2 states the involution on the distinct-index side; here we exhibit its diagonal dual partner explicitly and certify the sign law at every order.

### 6.2 Honest novelty versus organization

We weigh the contribution candidly, in the manner of 01c §1.3.

**Classical / already in the program (not claimed new).**
- The diagonal third-derivative formula $d^n(t\log t)/dt^n=(-1)^n(n-2)!/t^{n-1}$ is elementary calculus.
- That the cumulant tower of an exponential family is generated by one potential, with order-$2$ = Fisher and order-$3$ = Amari–Chentsov, is classical (Amari; Brillinger) and is the explicit subject of *T2*.
- The closed distinct-index tower $\kappa_n=(-1)^{n-1}(n-1)!\,m^{-n}$ and its $\alpha\to-\alpha$ involution are *T2* Prop. 6.2.
- The moving cubic and its frozen $\times$ breathing factorization at order $3$ are 01c Thm. 4.1.

**Organized / sharpened here.**
- **(O1)** The promotion of the 01c frozen $\times$ breathing factorization to **all orders**, with a certified closed form $T^{(n)}=c_n\Delta^{(n)}D_p^{\,n-1}$ and the exact identification of which factor breathes. This is re-presentation of classical material in the overcomplete simplicial frame, made all-orders and exact.
- **(O2)** The **purely diagonal** structure of the mixture-chart tower at all orders (Theorem 2.2), contrasted with the non-diagonal exponential-chart tower — a clean chart-dependent statement of where higher-order structure does and does not appear.
- **(O3)** The **explicit diagonal dual partner** of *T2*'s distinct-index tower, with the sign involution certified at every order (Prop. 6.1). T2 gives one side; this note gives the other and welds them.

**Genuinely informative (the one finding worth flagging).**
- **(N1)** The **honest non-match with Paper 21** (Prop. 5.1): the entropy tower is diagonal and therefore carries no Wick block, so the quartic obstruction is necessarily a phenomenon of the conjugate ($\Phi$/character) chart, not the entropy ($\varphi$/mixture) chart. This is a small but real *structural localization* of the obstruction — it says *which chart the obstruction can live in*, and certifies that the dual chart is obstruction-free at the $2{+}2$ level. It resolves 01c open problem D3 in the honest negative direction: the frozen-geometry factorization *does* survive at order $4$ (Theorem 2.3), but its survival is exactly the reason it cannot host Paper 21's obstruction.

Net: this note is **organization with one informative negative result.** It is the order-$n$ floor under the program's "frozen geometry $\times$ breathing diagonal" picture and the explicit $m$-chart dual of the *T2* tower; it is not a new theorem about the simplex's curvature, and it deliberately declines to claim a match it cannot certify.

---

## 7. SPECULATIVE: the diagonal tower, Legendre duality, and the adelic / functional-equation direction

> **Firewall.** Everything in §7 is **speculative orientation**, fenced off from the certified content of §§2–6. No claim here is certified, none is load-bearing for the theorems above, and the RH-adjacent material is flagged as such throughout. The program's RH spine (the N-series, the $P_\infty$ series, the Connes route) is careful, conditional, and not advanced by this note. Read §7 as a map of *where this object might connect*, not as a result.

### 7.1 The structural coincidence

The program has a standing slogan on its adelic-information-geometry direction: *global Legendre $=$ Tate/Poisson $=$ functional equation* (see the program's adelic-info-geometry line; $P_\infty$ "What Is Multiplicative?"). The mechanism there is that the global Legendre transform on a self-dual adelic object reproduces the $s\leftrightarrow1-s$ functional equation, with the dual involution $\alpha\to-\alpha$ playing the role of reflection.

This note furnishes, on the *finite categorical simplex*, a fully explicit, certified instance of the **two-sided Legendre pair** that the adelic slogan is about in the large:
$$\underbrace{\varphi=\sum p\log p}_{m\text{-chart, diagonal tower }c_nm^{\,n-1}}\ \xleftrightarrow{\ \text{Legendre}\ }\ \underbrace{\Phi=\log\textstyle\sum e^{\eta}}_{e\text{-chart, distinct tower }(-1)^{n-1}(n-1)!\,m^{-n}}$$
with the reflection $\alpha\to-\alpha$ realized as the certified sign involution of Prop. 6.1 (self-dual at $n=2$, flipped at $n=3$). The order-$2$ rung is the *self-dual* fixed point of the involution — the precise finite analogue of "$s=1/2$ is the fixed point of $s\leftrightarrow1-s$." The Fisher metric being the unique self-dual rung of the tower is, speculatively, the simplicial shadow of the critical line being the self-dual axis of the functional equation.

### 7.2 Where the chiral channel would enter

The program's RH route splits the categorical data on $\mathbb{Z}/6$ (and primorial $\mathbb{Z}/P_k$) into an **even / $\zeta$ channel** and a **chiral / odd / $L(s,\chi_3)$ channel** (program GUE→cumulant arc; N5 channel split). In the present diagonal tower, the chart that carries the *off-diagonal* character structure is the **$\Phi$-chart**, not the $\varphi$-chart — and it is exactly there that Paper 21's Wick subtraction and the conductor selection rule $a+b+c\equiv0$ live. The speculative reading of §5's honest non-match is then suggestive: **the entropy ($\varphi$) chart is the "even/metric" diagonal side, and the chiral/arithmetic content is carried entirely by the conjugate ($\Phi$) chart.** If so, the RH-relevant signal (the chiral-channel sign that the program's adelic line shrinks RH to) is *structurally invisible* to the diagonal entropy tower — which is consistent with, and a finite toy of, the program's repeated finding that RH content sits in the off-diagonal / multiplicative / archimedean-completion data, never in the order-$2$ metric.

### 7.3 The honest limits of the analogy

Three reasons not to overclaim, stated plainly:

1. **The simplex is finite and additive.** The functional equation is an archimedean/adelic completion statement; the program's own No-Go results (the archimedean place is not finitely-prime-generable) say a finite simplicial object cannot *contain* the FE. At best the diagonal/distinct Legendre pair is a **finite shadow** of the global Legendre = FE picture, in the same sense that the program treats $\mathbb{Q}$ as "the missing-Frobenius place."
2. **Self-duality of the metric is a triviality here.** That $n=2$ is the self-dual rung follows from $c_2=+1$ and $\kappa_2$'s sign by elementary calculus; reading it as a critical-line analogue is interpretation, not derivation. The genuine content on the RH side is the *positivity / energy condition* at the self-dual axis, which has no counterpart in this note.
3. **No spectral object is constructed.** The program's live RH route is operator-theoretic (CCM convergence, prolate $k̂_\lambda\to\Xi$); this note produces tensors, not an operator whose spectrum is the zeros. The Legendre pair here is a *bookkeeping* duality, not the spectral duality RH needs.

The defensible statement is the modest one: **the certified $\varphi\leftrightarrow\Phi$ Legendre pair, with its order-by-order sign involution and self-dual order-$2$ rung, is the cleanest finite worked example of the "global Legendre $=$ reflection" slogan the program uses on the adelic side — and its diagonal/off-diagonal split mirrors the program's metric/chiral split.** Whether this is more than an analogy is exactly the open question the adelic-info-geometry line is pursuing, and this note does not move it.

---

## 8. Conclusion and open sub-threads

The mixture-chart cumulant tower of the categorical simplex is, at every order, a single diagonal object: a frozen all-equal-index selector $\Delta^{(n)}$, a breathing diagonal $D_p^{\,n-1}$, and a factorial sign $c_n=(-1)^n(n-2)!$. Order $2$ is the Fisher metric, order $3$ is the moving Amari–Chentsov cubic, and no qualitatively new geometry appears at higher order in this chart — which is precisely why Paper 21's quartic obstruction must, and does, live in the conjugate exponential chart. The whole tower is the Legendre dual of the program's distinct-index $\Phi$-tower, sign-opposite at every order through the $\alpha\to-\alpha$ involution that fixes the metric and flips the cubic.

Open sub-threads for a follow-up pass:

- **S1 (general $N$ / Direction 1 weld).** Theorem 2.3 is $N$-uniform (the proof uses only separability). The order-$2$ rung is $D_p$, whose *uniform-point* value $4I$ on $H$ is the restriction of the **complete-graph $K_N$ Laplacian** $L=NI-J$ (certified **C7**: $\sum_{i<j}(u_i-u_j)^2=u^\top Lu$, spectrum $\{0;\,N^{(N-1)}\}$, the gauge direction $\mathbf 1$ in the kernel). Thread: identify the order-$n$ rung's uniform value with a *hypergraph* / higher Laplacian on $K_N$, and connect $D_p^{\,n-1}$ to Direction 1's Laplacian-spectrum program. (The $n=2$ case is already the bridge.)
- **S2 (raised higher tower).** Compute the metric-raised order-$n$ operator $K^{(n)}_p$ generalizing $K^{CH}_p$ (01c §4), and ask whether the cross-product-square realization of $\odot$ extends to an $n$-fold componentwise product with fixed projectors $I+K(\tau_i)^2$ — i.e. whether 01.3.8 has an order-$n$ analogue.
- **S3 (Paper 21 character chart).** Carry the diagonal/off-diagonal split of §5 into the additive-character basis on $\mathbb{Z}/N$ and certify, on $\mathbb{Z}/30$, that the $\varphi$-tower's diagonal maps to the *connected single-character* support while the $\Phi$-tower's Wick block maps to the $2{+}2$ pairings — making the §5 non-match a character-basis statement matching Paper 21 §5.2 directly.
- **S4 (reversibility / Direction 3).** The towers here are totally symmetric (cumulants), hence live entirely in the symmetric ($S$) sector of a would-be $T=S+A$ split. The Hodge-harmonic / antisymmetric ($A$) content — the program's arrow-of-time $\dim=\beta_1/b_1$ (Irreversible Blind Spot) — is **orthogonal** to the entire $\varphi$-tower by construction. Thread: pair the symmetric $\varphi$-tower with an antisymmetric companion on $H$ (e.g. via $K(u)$ of Paper 01, which is the antisymmetric generator) and ask whether "metric $\oplus$ cubic $\oplus\cdots$" (symmetric) $+$ "cross product" (antisymmetric) is the simplicial $S+A$ decomposition Direction 3 wants.
- **S5 (adelic, speculative).** Make §7 falsifiable: is there a finite positivity statement at the self-dual ($n=2$) rung that survives the $q\to1$ / archimedean completion the program studies? If not, §7 is confirmed to be analogy only.

---

## Appendix A: Exact-arithmetic certificate

The reference implementation `empirical_forward2/cert_cumulant_tower.py` (sympy only; deterministic local gate; run with `py`) verifies, exactly (**CERT GREEN**, 9 checks, all residuals exact zeros over $\mathbb{Q}$ or $\mathbb{Q}(p_i)$):

1. **C1** — diagonal scalar law $d^n(t\log t)/dt^n=(-1)^n(n-2)!/t^{\,n-1}$ and the coefficient table $1,-1,2,-6,24$, $n=2{-}6$ (Lemma 2.1).
2. **C2** — purely-diagonal tower on $N=4$, **exhaustive** over all $4^n$ multi-indices, $n=2{-}6$: diagonal value $c_n/p_i^{\,n-1}$, every mixed index $0$ (Theorem 2.2).
3. **C2'** — $N=5$ spot check, orders $2{-}4$, all $5^n$ indices.
4. **C3** — factorization $T^{(n)}=c_n\Delta^{(n)}D_p^{\,n-1}$ over all indices, plus position-independence of $\Delta^{(n)}$ and $c_n$ and the breathing law $\partial_{p_i}(1/p_i^{\,n-1})=-(n-1)/p_i^{\,n}$ (Theorem 2.3).
5. **C4** — $n=2$ reduction: $\operatorname{Hess}\varphi=\operatorname{diag}(1/p_i)=g_p$ and the bilinear form $\sum u_iv_i/p_i$ (Prop. 3.1).
6. **C5** — $n=3$ reduction: the raised cubic $K^{CH}_p(u)v=D_p(u\odot v)-\langle u,v\rangle_{g_p}p$ equals the skewness tensor on $H$, is totally symmetric, and reduces at $p_*$ to $4(u\odot v)-(\sum u_iv_i)\mathbf 1$ (Prop. 3.2; 01c Thm. 4.1).
7. **C6** — Legendre bridge: diagonal $\varphi$-value $c_nm^{\,n-1}$ at the uniform; $\Phi$-tower $\kappa_n=(-1)^{n-1}(n-1)!\,m^{-n}$ re-derived from the CGF $\log(1+t/m)$ (T2 Prop. 6.2); sign-opposition at every order (Prop. 6.1).
8. **C7** — Direction-1 weld: complete-graph $K_N$ Laplacian $L=NI-J$, Dirichlet form $\sum_{i<j}(u_i-u_j)^2=u^\top Lu$, $u^\top Lu=N\sum u_i^2$ on $H$, spectrum $\{0$ (gauge $\mathbf 1$)$;\,N$ (mult. $N-1$ on $H)\}$ ($N=3,4,5$).
9. **C8** — Paper 21 honest boundary: the $\varphi$-tower's $2{+}2$ mixed components vanish (no Wick block) while $\Phi$'s are nonzero at the uniform (e.g. $-3/128$); the order-$4$ coefficients are sign-opposite (Prop. 5.1).

---

## References

[01] Murillo Montero, L. *Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates*. v2, 2026. DOI 10.5281/zenodo.19689049.

[01b] Murillo Montero, L. *Intrinsic Differential Calculus on Simplicial (Quadray) Coordinates*. Draft 1, 2026.

[01c] Murillo Montero, L. *The Moving Amari–Chentsov Cubic in Simplicial Coordinates: Cross-Product-Square Factorization and the α-Connection Collapse*. Draft 1, 2026.

[21] Murillo Montero, L. *The Quartic Force Law at Cumulant Order Four*. Exploratory preprint, May 2026.

[T2] Murillo Montero, L. *$\heb{ל}2$ — Identifying 3: The Cumulant Tower as Effective Action*. Preprint v1.0, May 2026.

[Amari] Amari, S. *Information Geometry and Its Applications*. Springer, 2016.

[Brillinger] Brillinger, D. R. *Time Series: Data Analysis and Theory*. Holt, Rinehart and Winston, 1975.

[Chentsov] Chentsov, N. N. *Statistical Decision Rules and Optimal Inference*. AMS, 1982.

[Nielsen] Nielsen, F. "An elementary introduction to information geometry." *Entropy* 22(10), 1100 (2020).

---

*[End of Draft 1. Speculative §7 is fenced and non-load-bearing; certified content is §§2–6 + Appendix A.]*
