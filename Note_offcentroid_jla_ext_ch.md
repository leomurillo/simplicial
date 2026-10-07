# Note: Off-Centroid JLA Expansion of $K^{CH}$ and the Location of $\operatorname{Ext}_{CH}$

**Status.** Pushes H7A/H8 off the centroid.  H8 established that the centroid
Jordan-Lie algebra of $K^{CH}$ is universal — both the commutator and the
Jordan product depend only on $N=|R|$ and give the same answer for every
finite ring $R$.  This note answers the next question:

> At what Taylor order in $h = p - p_*$ does $\operatorname{Ext}_{CH}$ first
> appear as a structural invariant in the JLA expansion of $K^{CH}$?

**Provisional answer.** It does not appear at any finite order in $h$.  The
position-coordinate Taylor coefficients $\delta^k K^{CH}$ are universal in
$R$ (depend only on $N$).  The character-basis matrix elements are
polynomial in additive convolutions of $\widehat u, \widehat v, \widehat h$
on the additive group $(R,+)$.  The conductor packet decomposition is
inherited from the conductor function $\chi\mapsto\operatorname{cond}(\chi)$
but the *multiplicative* (Hayes-normalizer) structure that defines
$\operatorname{Ext}_{CH}$ is invisible to the $K^{CH}$ JLA family.  Section
7 makes this precise as a Provisional Theorem; Section 8 spells out the
operational consequence — the cubic K^{CH} diagnostic (logit-vs-moment
chord, H13) is sensitive to additive conductor packets but \emph{not} to
$\operatorname{Ext}_{CH}$.  Detecting $\operatorname{Ext}_{CH}$ empirically
requires probes outside the $K^{CH}$ family.

---

## 1. The Off-Centroid $K^{CH}$ Formula

Let $p$ lie in the interior of the categorical simplex $\Delta_R^\circ$ and
let $u,v\in T_p\Delta_R = H_R$ (zero-sum tangent vectors).  The Amari-Chentsov
3-tensor at $p$ is

$$
T_p(u,v,w)
= \mathbb E_p\bigl[s_u(X)\,s_v(X)\,s_w(X)\bigr]
= \sum_{x\in R}\frac{u_x v_x w_x}{p_x^2},
$$

where $s_u = u/p$ is the score along the $m$-direction $u$.  Raising one index
with the Fisher metric $g^F_p(\cdot,\cdot)=\sum (\cdot)(\cdot)/p_x$ and
projecting back to $H_R$ gives:

$$
\boxed{\;K^{CH}_p(u)v \;=\; \frac{u\odot v}{p} \;-\; \langle u,v\rangle_p\cdot p\;}
$$

where $\odot$ is pointwise multiplication, $\langle u,v\rangle_p
=\sum_x u_x v_x/p_x$ is the Fisher inner product at $p$, and division and
multiplication by the probability vector $p$ are pointwise.

**Centroid check.**  At $p_*=N^{-1}\mathbf 1$: $u\odot v/p_*=N(u\odot v)$,
$\langle u,v\rangle_{p_*}=N\langle u,v\rangle_{\mathrm{Euc}}$,
$\langle u,v\rangle_{p_*}\cdot p_*=\langle u,v\rangle_{\mathrm{Euc}}\cdot\mathbf 1$.
So

$$
K^{CH}_{p_*}(u)v = N(u\odot v) - \langle u,v\rangle_{\mathrm{Euc}}\cdot\mathbf 1,
$$

which is the form consistent with Paper 11 Proposition 8.1's $N$-rescaled
sphere curvature commutator.  (The Note `Note_prime_cyclic_ext_ch.md`
displays this with an extra $N$ on the second term; the substitution it
uses in its own derivation drops that $N$, and Paper 11 Prop 8.1's
result requires the form above.  Treat this as a normalization fix.)

---

## 2. Taylor Expansion Around $p_*$

Write $p = p_* + h$ with $h\in H_R$ (so $p_x = N^{-1}+h_x$ and $\sum_x h_x=0$).
Expand $1/p_x$ as a geometric series:

$$
\frac{1}{p_x}
= \frac{N}{1+Nh_x}
= N\sum_{k\ge 0}(-Nh_x)^k
= N - N^2 h_x + N^3 h_x^2 - \cdots
$$

Then

$$
\frac{u\odot v}{p}
= N(u\odot v) - N^2(u\odot v\odot h) + N^3(u\odot v\odot h^{\odot 2}) - \cdots,
$$

$$
\langle u,v\rangle_p
= N\langle u,v\rangle - N^2\langle u\odot v,h\rangle + N^3\langle u\odot v,h^{\odot 2}\rangle - \cdots,
$$

(throughout, $\langle a,b\rangle=\sum_x a_xb_x$ is the unweighted bilinear
pairing and $h^{\odot k}$ is the pointwise $k$-th power).  Combining with
$p=p_*+h$ and collecting by order:

**Order 0 (centroid).**

$$
K^{CH}_{p_*}(u)v = N(u\odot v) - \langle u,v\rangle\mathbf 1.
$$

**Order 1 (first off-centroid correction).**

$$
\boxed{\;\delta^1(u,v;h)
= -N^2(u\odot v\odot h)
+ N\langle u\odot v,h\rangle\mathbf 1
- N\langle u,v\rangle h\;}
$$

**Order 2.**

$$
\delta^2(u,v;h)
= N^3(u\odot v\odot h^{\odot 2})
- N^2\langle u\odot v,h^{\odot 2}\rangle\mathbf 1
+ N^2\langle u\odot v,h\rangle h.
$$

**Position-coordinate universality.** Each $\delta^k$ depends only on $N$
and pointwise products / Euclidean pairings of $u,v,h$.  No feature of $R$
beyond $N$ enters this formula.

---

## 3. The Lie Bracket at Order 1

Let $K_{p_*}(u): v\mapsto N(u\odot v)-\langle u,v\rangle\mathbf 1$ be the
centroid operator and $\delta^1_u(h): v\mapsto\delta^1(u,v;h)$ the order-1
correction (as an operator on $v$, for fixed $u, h$).  Compute the order-1
piece of $[K^{CH}_{p_*+h}(u), K^{CH}_{p_*+h}(v)]$:

$$
\bigl[\delta^1_u(h),\,K_{p_*}(v)\bigr](w)
+ \bigl[K_{p_*}(u),\,\delta^1_v(h)\bigr](w).
$$

Direct computation (expanding products, using $\langle\mathbf 1,u\rangle=0$
for $u\in H_R$, and the symmetry $\langle u,v\odot w\rangle
=\langle v,u\odot w\rangle=\sum u_xv_xw_x$): all $u\odot v\odot w\odot h$
and $\langle u\odot v\odot w,h\rangle\mathbf 1$ terms cancel as symmetric in
$u\leftrightarrow v$.  The residue is

$$
\boxed{\;
\bigl[K^{CH}_{p_*+h}(u),\,K^{CH}_{p_*+h}(v)\bigr](w)
=
\underbrace{N\bigl(\langle u,w\rangle v-\langle v,w\rangle u\bigr)}_{\text{order 0: sphere curvature}}
\;+\;
\underbrace{N^2\bigl(\langle v\odot w,h\rangle u - \langle u\odot w,h\rangle v\bigr)}_{\text{order 1 correction}}
+\;O(h^2).\;}
$$

**Structure of the order-1 correction.** It is a scalar
$\langle v\odot w,h\rangle = \sum_x v_xw_xh_x$ times $u$, minus the
$u\leftrightarrow v$ swap.  The scalar is the 3-fold pointwise integral
$\sum v_xw_xh_x$, which by character orthogonality is a 3-fold convolution
of $\widehat v,\widehat w,\widehat h$ evaluated at zero:

$$
\sum_x v_xw_xh_x = \frac{1}{N^2}\sum_{j+k+\ell\equiv 0\pmod N}\widehat v(j)\,\widehat w(k)\,\widehat h(\ell).
$$

(Using the convention $f_x=\sum_m\widehat f(m)e^{2\pi imx/N}$, so
$\widehat f(m)=N^{-1}\sum_x f_xe^{-2\pi imx/N}$.)

**Position-coordinate universality persists.** The formula depends only on
$N$ and pointwise products.  The conductor structure of $R$ is invisible at
this level — it enters only when we decompose by character packets.

---

## 4. The Jordan Product at Order 1

The same expansion for the anticommutator
$\{K^{CH}_{p_*+h}(u),K^{CH}_{p_*+h}(v)\}$ gives, after canceling the
symmetric pieces (none cancel — they all survive in the Jordan sum):

$$
\bigl\{K^{CH}_{p_*+h}(u),\,K^{CH}_{p_*+h}(v)\bigr\}(w)
= \bigl\{K^{CH}_{p_*}(u),K^{CH}_{p_*}(v)\bigr\}(w)
+ \delta^1_{\mathrm{Jord}}(u,v;h,w) + O(h^2),
$$

with the order-0 piece (from H8) equal to the universal Jordan formula
$2N^2(u\odot v\odot w) - N(\langle v,w\rangle u+\langle u,w\rangle v)
- 2N\langle u,v\odot w\rangle\mathbf 1$, and the order-1 correction

$$
\boxed{\;\delta^1_{\mathrm{Jord}}(u,v;h,w)
=
-4N^3(u\odot v\odot w\odot h)
+ 4N^2\langle u\odot v\odot w,h\rangle\mathbf 1
- 2N^2\langle u,v\odot w\rangle h
+ N^2\bigl(\langle u\odot w,h\rangle v+\langle v\odot w,h\rangle u\bigr).\;}
$$

**New structure in the Jordan correction.** The $-4N^3(u\odot v\odot w\odot h)$
term is a 4-fold pointwise product, with no analogue in the Lie bracket
correction (it was the symmetric piece that cancelled there).  Its
character-basis Fourier transform is the **4-fold convolution at zero**:

$$
\sum_x u_xv_xw_xh_x
= \frac{1}{N^3}\sum_{i+j+k+\ell\equiv 0\pmod N}
   \widehat u(i)\widehat v(j)\widehat w(k)\widehat h(\ell).
$$

So the Lie bracket sees 3-fold convolutions of $\widehat v,\widehat w,\widehat h$
at zero; the Jordan product sees 4-fold convolutions of
$\widehat u,\widehat v,\widehat w,\widehat h$ at zero, plus 3-fold pieces.
Both stay strictly within the additive arithmetic of $(R,+)$.

---

## 5. Character-Basis Matrix Elements

Fix the displacement $h$ and treat $\delta^1_u(h)$ as a linear operator on
$H_R$.  Its character-basis matrix entries are

$$
\bigl[\delta^1_u(h)\bigr]_{\chi_j,\chi_k}
= -N^2(\widehat u\ast\widehat h)(j-k) - N^2\,\widehat u(-k)\,\widehat h(j),
$$

(after dropping the trivial-character $\mathbf 1$ contributions that
project out of $H_R$).  Two structural features:

1. **Frequency-difference shift:** the first piece $(\widehat u\ast\widehat h)(j-k)$
   depends on $j-k\in R$ alone.  This is a generalized quotient-shift
   weighted by the 2-fold convolution of $\widehat u$ with $\widehat h$.
2. **Rank-one "trivial" piece:** the second piece factors as
   $\widehat h(j)\cdot\widehat u(-k)$, i.e. it is a rank-one matrix
   $|\widehat h\rangle\!\langle\widehat u^\vee|$.  It arises from the
   $-N\langle u,v\rangle h$ term in $\delta^1$.

In particular, the order-1 correction lives in the **additive convolution
subalgebra** of $\mathcal A_R$ — the subalgebra generated by

$$
\bigl\{M_\eta : \eta\in\widehat R\bigr\}\cup\{P_\mathfrak f : \mathfrak f\text{ a conductor level}\},
$$

together with the rank-one outer products $|\widehat h\rangle\!\langle\widehat u^\vee|$
that arise from Fisher inner-product projections.  All such operators are
determined by the additive group $(R,+)$ and the conductor function
$\operatorname{cond}:\widehat R\to\mathbb N$; none of them invokes the
multiplicative structure $(R,\cdot)$.

The same statement holds for $\delta^k_u(h_1,\dots,h_k)$ at every order $k$:
its character-basis matrix elements are polynomial in
$(k+1)$-fold convolutions of $\widehat u,\widehat{h_1},\dots,\widehat{h_k}$.

---

## 6. Conductor-Packet Decomposition and CRT Isolation

For $R = C_N$ and $\widehat h$ supported on the $a$-primary subgroup
$P_a=b\cdot\mathbb Z/N$ ($N=ab$, $\gcd(a,b)=1$), the convolution
$\widehat u\ast\widehat h$ at any point inherits the subgroup structure of
$\widehat u$.  Specifically:

- If $\widehat u\subseteq P_a$ and $\widehat h\subseteq P_a$, then
  $(\widehat u\ast\widehat h)(j-k)\ne0$ requires $j-k\in P_a$.
- Therefore $[\delta^1_u(h)]_{\chi_j,\chi_k}\ne0$ requires $j-k\in P_a$
  (the frequency-difference part) or $j\in\operatorname{supp}\widehat h$,
  $-k\in\operatorname{supp}\widehat u$ (the rank-one part).
- The cross-conductor block $[\mathfrak f,\mathfrak e]$ with
  $\mathfrak f$ in the $b$-primary level and $\mathfrak e$ in the
  $a$-primary level remains zero at order 1 when both $\widehat u$ and
  $\widehat h$ are pure $a$-primary — extending Paper 11 Corollary 1.3
  (CRT conductor isolation, established at the $n=1$ Taylor coefficient)
  to the order-1 off-centroid $K^{CH}$ correction.

**Corollary.** The Paper 11 Cor 1.3 vanishing carries over verbatim to
the first off-centroid $K^{CH}$ correction.  Composite-cyclic rings exhibit
block-diagonal off-centroid Fisher coupling whenever the displacement
$h$ is pure CRT-primary.

For prime $R=C_p$: the additive group has no proper subgroups, so the
order-1 correction has no conductor-block vanishing structure — every
character pair $(j,k)$ in $\widehat{C_p}\times\widehat{C_p}$ can receive a
nonzero contribution.  This is the same single-packet picture as
Paper 11 Corollary 1.4.

---

## 7. The Location of $\operatorname{Ext}_{CH}$

Recall the precise definition: $\operatorname{Ext}_{CH}(R)$ is the
obstruction class for the conductor filtration of $H_R$ to split as a
$\Gamma_R$-equivariant direct sum, where $\Gamma_R$ is the Hayes normalizer
$R^\times$ acting by multiplication on characters.  For $R=C_N$, the
filtration always splits ($\operatorname{Ext}_{CH}=0$).  For the minimal
mixed local ring $R=\mathbb F_4[u]/(u^2)$, the wild/tame extension is
non-split ($\operatorname{Ext}_{CH}\ne 0$), and the obstruction is carried
by a swap operator $2bc\cdot X_N$ between the tame characters
(factoring through $\mathbb F_4$) and the wild characters (genuine
$u$-dependence); see Paper 11 §3.2.

**The structural observation.** The position-coordinate Taylor coefficients
$\delta^k(u,v;h_1,\dots,h_k)$ and their JLA brackets are polynomial
expressions in $u,v,h_1,\dots,h_k$ built from pointwise products $\odot$ and
Euclidean pairings $\langle\cdot,\cdot\rangle$.  In character basis, these
become polynomial expressions in finite-order convolutions of
$\widehat u,\widehat v,\widehat{h_1},\dots,\widehat{h_k}$ on $(R,+)$.  The
Hayes-normalizer action $R^\times\curvearrowright\widehat R$ enters this
expression only via the conductor function $\operatorname{cond}$ that
labels packets — it does not enter the **algebraic form** of the operator
entries.

In particular, **the swap operator $2bc\cdot X_N$ from Paper 11 §3.2 is not
in the subalgebra generated by $\{\delta^k K^{CH}_{p_*}\}_{k\ge 0}$.** That
operator is defined by its action under the Hayes normalizer's tame Galois
$\times$ wild generator structure, not by additive convolution arithmetic.
It can only be reached by an operator that knows the multiplicative
ring structure of $R$ — which $K^{CH}$, as a Riemannian object built from
the Fisher metric and AC tensor, does not.

**Provisional Theorem (K^{CH} is $\operatorname{Ext}_{CH}$-transparent).**
Let $R$ be a finite commutative local ring with maximal ideal
$\mathfrak m$, Hayes normalizer $\Gamma_R=R^\times$, and adjacency algebra
$\mathcal A_R\subseteq\operatorname{End}(H_R)$.  Let
$\mathcal A_R^{\mathrm{add}}\subseteq\mathcal A_R$ denote the subalgebra
generated by:

(i) multiplication operators $M_\eta$ by additive characters $\eta\in\widehat R$;
(ii) conductor projectors $P_\mathfrak f$ for each conductor level
$\mathfrak f$;
(iii) rank-one outer products $|\widehat h\rangle\!\langle\widehat u^\vee|$
for $u,h\in H_R$.

Then for every Taylor order $k\ge 0$ and every displacement vectors
$u,h_1,\dots,h_k\in H_R$, the operator
$\delta^k K^{CH}_{p_*}(u;h_1,\dots,h_k)\in\mathcal A_R^{\mathrm{add}}$.
Consequently, every iterated commutator and Jordan-product of $K^{CH}$
operators evaluated at any point $p$ in a formal neighborhood of $p_*$ lies
in $\mathcal A_R^{\mathrm{add}}$.  The extension class
$\operatorname{Ext}_{CH}(R)\in H^1_{\Gamma_R}(\operatorname{gr}\mathcal A_R)$
is detected by Hayes-equivariant cross-packet operators in
$\mathcal A_R\setminus\mathcal A_R^{\mathrm{add}}$; in particular it is
detected by the swap operator of Paper 11 §3.2 which does not lie in
$\mathcal A_R^{\mathrm{add}}$.  Therefore the $K^{CH}$ JLA tower at $p_*$
does not detect $\operatorname{Ext}_{CH}$ at any finite Taylor order.

**Sketch.** Closure of $\mathcal A_R^{\mathrm{add}}$ under composition is
immediate: $M_\eta M_\zeta=M_{\eta+\zeta}$, $P_\mathfrak f^2=P_\mathfrak f$,
and outer products compose to outer products.  The Taylor coefficients
$\delta^k$ are built (Section 2) from $(u\odot v\odot h^{\odot k})/p_*^k$
and inner products $\langle u,v\rangle$, $\langle u\odot v,h^{\odot j}\rangle$.
Pointwise products in position correspond to character convolutions, which
generate $M_\eta$ operators by Section 5; Euclidean pairings against
displacements generate rank-one operators by Section 5.  Composing $K^{CH}$
operators (Lie bracket or Jordan product) preserves $\mathcal A_R^{\mathrm{add}}$
by the closure argument.  The swap operator of Paper 11 §3.2 cannot be
written in this form because its defining Hayes-equivariance under
$R^\times=\mathbb F_4^\times\times(1+u\mathbb F_4)$ involves the wild
generator $1+u\mathbb F_4$, which acts by a multiplicative twist that is
not realized by additive characters or conductor projections. $\square$

---

## 8. Diagnostic Consequences for Paper 12

The Provisional Theorem has a sharp empirical reading for the
Paper 12 program:

1. **The H13 cubic diagnostic (logit vs moment chord) measures
   $K^{CH}$ universally.** Its predicted ratio
   $(1-r_{\mathrm{moment}}):(1-r_{\mathrm{logit}})$ is determined by the
   first off-centroid correction $\delta^1 K^{CH}$ and the universal
   sphere curvature from $[K^{CH},K^{CH}]$.  Both pieces lie in
   $\mathcal A_R^{\mathrm{add}}$.  The diagnostic is therefore valid as a
   test of the Amari-Chentsov cubic — but it is *blind to
   $\operatorname{Ext}_{CH}$*.

2. **For $C_7$ (the weekday row):** $\operatorname{Ext}_{CH}(C_7)=0$
   trivially.  The Provisional Theorem implies $K^{CH}$ cannot create a
   false positive: there is no $\operatorname{Ext}_{CH}$ signal for it to
   miss.  The prime cyclic row remains the clean zero-cross-cubic control.

3. **For $C_{12}$ (the months row):**
   $\operatorname{Ext}_{CH}(C_{12})=0$, but the conductor packet structure
   is nontrivial.  The Provisional Theorem predicts the order-1 and order-2
   off-centroid corrections respect CRT isolation exactly (extending
   Cor 1.3 from the $n=1$ Taylor coefficient).  This is the testable
   prediction for months data when it arrives.

4. **For $\mathbb F_4[u]/(u^2)$ (the positive mixed test):**
   $\operatorname{Ext}_{CH}\ne 0$, but the $K^{CH}$ JLA tower at the
   centroid does not see it.  A positive experimental signal for
   $\operatorname{Ext}_{CH}$ therefore *cannot* come from a moment-vs-logit
   chord correlation gap.  It must come from a Hayes-equivariant probe —
   specifically a measurement that distinguishes the swap operator's
   contribution to the cross-tame/wild Fisher coupling from the
   block-diagonal contribution that any $\mathcal A_R^{\mathrm{add}}$
   operator would predict.  This sharpens what the
   $\mathbb F_4[u]/(u^2)$ positive test must look like.

The note therefore re-locates $\operatorname{Ext}_{CH}$ in the experimental
program: it is **not** the next-order term in the $K^{CH}$ Taylor
expansion (which is what one might naively hope from the H7A→H8→H13 chain).
It is a separate, multiplicative invariant that requires its own probe
construction.

---

## 9. What Remains to be Done

The Provisional Theorem is supported by:

- explicit position-coordinate formulas (Sections 2–4, rigorous);
- explicit character-basis matrix elements (Section 5, rigorous);
- conductor decomposition (Section 6, rigorous);
- closure-and-non-detection argument (Section 7, sketched).

To upgrade to a Theorem proper, the following are needed:

(a) A clean definition of $\mathcal A_R^{\mathrm{add}}$ that admits a
    universally valid closure lemma (the rank-one outer-product piece
    should be checked for closure under composition with $M_\eta$).

(b) A precise statement of which elements of $\mathcal A_R$ are
    *not* in $\mathcal A_R^{\mathrm{add}}$, ideally a cohomological
    characterization tied to the $\operatorname{Ext}_{CH}$ class.

(c) An explicit verification on $\mathbb F_4[u]/(u^2)$: write the swap
    operator $2bc\cdot X_N$ and check that no finite-order $\delta^k K^{CH}$
    has any character-basis matrix entry matching its non-zero entries
    up to a polynomial in $\{\widehat u,\widehat h\}$.

Item (c) is a finite check that could close the theorem.  It is also the
right next computational target in this line of work.

---

## Appendix: Summary of Identities

| Order | Lie correction | Jordan correction |
|:---:|:---|:---|
| 0 | $N(\langle u,w\rangle v - \langle v,w\rangle u)$ | $2N^2(u{\odot}v{\odot}w) - N(\langle v,w\rangle u+\langle u,w\rangle v) - 2N\langle u,v{\odot}w\rangle\mathbf 1$ |
| 1 in $h$ | $N^2(\langle v{\odot}w,h\rangle u - \langle u{\odot}w,h\rangle v)$ | $-4N^3(u{\odot}v{\odot}w{\odot}h) + 4N^2\langle u{\odot}v{\odot}w,h\rangle\mathbf 1 - 2N^2\langle u,v{\odot}w\rangle h + N^2(\langle u{\odot}w,h\rangle v + \langle v{\odot}w,h\rangle u)$ |

| Character-basis convolution order |
|:---|
| Centroid commutator: 2-fold (in $\widehat v, \widehat w$ at $\langle\cdot\rangle$) |
| Centroid Jordan: 3-fold (in $\widehat u,\widehat v,\widehat w$) |
| Order-1 commutator: 3-fold (in $\widehat v,\widehat w,\widehat h$) |
| Order-1 Jordan: 4-fold (in $\widehat u,\widehat v,\widehat w,\widehat h$), plus 3-fold pieces |

All convolutions are on $(R,+)$ alone.  The multiplicative structure
$(R,\cdot)$ — equivalently the Hayes normalizer $R^\times$ — never enters
the algebraic form.

---

**Cross-references.**
- Paper 11 Proposition 8.1 — universal commutator (sphere curvature).
- Paper 11 Proposition 8.2 — Jordan product at centroid (H8).
- Paper 11 Corollary 1.3 — CRT conductor isolation at $n=1$.
- Paper 11 Corollary 1.4 — prime cyclic conductor saturation.
- Paper 11 Corollary 1.5 — diagonal vanishing and prime-row cross-conductor absence.
- Paper 11 §3.2 — the $\mathbb F_4[u]/(u^2)$ swap operator.
- `Note_H8_jordan_lie_algebra.md` — centroid JLA closure and structure.
