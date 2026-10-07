# P∞-B — The Frobenius Correspondence Operator and the Order Dichotomy

## What Realizes the Arithmetic-Site Frobenius, and Why the Cubic Witness Is Its Order-2-Blind Shadow

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — June 10, 2026*

<!--
Program record (not part of the paper). Satellite B of P∞ (as P∞-A is satellite A). Answers the two
questions posed at the close of the spectral-Hodge-index assessment (2026-06-10): (1) what operator
realizes the Connes-Consani arithmetic-site Frobenius correspondences Psi_lambda — answered in four
layers, with the finite layer's index-freeness PROVED (Thm B.1, new, certified); (2) whether the cubic
(order-3) positivity of the dispersion route is the order-2-blind shadow of the missing spectral Hodge
index — answered YES in the two-layer form of Cor B.3: the WITNESS must be cubic (order-2 finite data
is provably arithmetic-free), while the WALL (T1) remains order-2 (the index shadow). Anchoring
certificate: empirical/p_infinity/probe_finite_frobenius_lattice.py (exact, GREEN, 30 checks). Does
NOT prove RH; the open step (CCM mu_lambda -> 0 = Weil positivity = the index) is untouched. Value:
necessity (third independent finite-witness exclusion, after the archimedean No-Go and P∞-A Prop
8.3a), unification (both program routes derived as the two shadows of one object), and the
degree-carrier identification (Frobenius scheme-degree = archimedean modulus).
-->

---

> *At second order the finite world is all gcd and ramification — real, even, blind. The first phase, the first chirality, the first arithmetic is cubic; and the certificate that would close it is not finite at all.*

---

## Abstract

**Situation.** P∞ established that the multiplicative second-order invariant is the intersection metric — Lorentzian, signature $(1,\rho-1)$ — with the archimedean place timelike and RH the causality of the primitive cone; and it left the construction over $\mathbb Q$ localized at one object, the $\mathbb F_1$ surface $\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}\mathrm{Spec}\,\mathbb Z$. The function-field door named what must live on that square: a *substitute Frobenius* whose graph classes the Hodge index forces onto the critical line. Connes–Consani have constructed the candidate square (the arithmetic/scaling site) and its one-parameter semigroup of **Frobenius correspondences** $\Psi_\lambda$. Two questions remain: *what operator realizes $\Psi_\lambda$ on the zeta side*, and *how the program's cubic (order-3) positivity route relates to the order-2 Hodge index that closes RH over $\mathbb F_q$*.

**Action.** We answer the first in four layers — topos ($\Psi_\lambda$, Connes–Consani), adelic ($\Psi_\lambda$ = the archimedean **scaling flow** $\theta_\lambda$ with generator $D$; trace pairing = Riemann–Weil explicit formula, Connes), prolate compression (CCM: positivity *proved* on the prolate-cutoff filtration; $\mu_\lambda\downarrow0$ the open limit), and the **finite apex compression** (the multiplication correspondences $\Gamma_a$ on $(\mathbb Z/m)^2$) — and we prove that the finite layer is *structurally incapable* of carrying the index: every order-2 invariant of the finite Frobenius lattice is a gcd / ramification-support function — real, conjugation-even, phase-free — and the finite Weil form has **empty positive sector** (Theorem B.1, certified). We then show the first arithmetic-bearing invariants of the same lattice are **order 3**: the Jacobi sums (= the abelian Frobenius eigenvalues; non-real phases in *every* admissible pair) and the V-sector mass $S(p)$, which we identify with the unordered selection-rule triple count of the unit lattice — *ocho*'s discrete cubic witness $\mathrm{pure}_V$ **is** the order-3 mass of the Frobenius lattice (Theorem B.2, certified).

**Result.**
$$\boxed{\ \text{Order 2 at finite level is arithmetic-free (no index, no phases); arithmetic enters at order 3; the index exists only spectrally.}\ }$$
Corollary B.3 (the two shadows): the dispersion route's **witness** must be cubic because no order-2 finite witness exists (Thm B.1) — while its **wall** (T1, the sparse-primorial variance) is still order-2, the analytic shadow of the same missing index whose spectral realization is the CCM prolate limit. The two program routes are the two shadows — finite-visible order-3 and spectral order-2 — of one object: the Hodge index on the $\mathbb F_1$ square, realized as Weil positivity of the scaling-correspondence algebra.

**Harvest.** A third, independent finite-witness exclusion (after the archimedean No-Go and P∞-A Prop 8.3a), this time *geometric*: the finite correspondences are degree-1 (unitary), and even the true Frobenius $x\mapsto x^q$ is a bijection on points — its degree $q$ lives in $dz^q=0$, invisible set-theoretically. The expansion that builds the hyperbolic pole plane ($e^{\pm x/2}$ in W1's $A_\infty$) is therefore not point data; **over $\mathbb Q$ its carrier is the archimedean modulus of the scaling flow** — N4's "archimedean $=\sqrt q$" receives its precise geometric referent.

**Keywords.** Frobenius correspondence, arithmetic site, scaling flow, Hodge index, order dichotomy, gcd circulant, ramification support, Jacobi sums, chirality, cubic witness, $\mathrm{pure}_V$, conductor blind spot, spectral realization, prolate operator.

---

## 1. The operator, in four layers

**Question (from the function-field door).** Over $\mathbb F_q$, RH is the Hodge-index confinement of the Frobenius graph classes on $C\times C$. Over $\mathbb Q$ the square and the Frobenius must be built. Connes–Consani built a candidate square — the arithmetic site $\mathscr A$, whose unreduced square carries a one-parameter semigroup of **Frobenius correspondences** $\Psi_\lambda$, $\lambda\in\mathbb R_+^\times$, $\Psi_\lambda\circ\Psi_\mu=\Psi_{\lambda\mu}$ [CC]. *What operator realizes $\Psi_\lambda$?*

**Layer 1 (topos; known).** $\Psi_\lambda\subset\mathscr A\times\mathscr A$ as congruence correspondences [CC, *The Arithmetic Site*; *Geometry of the Arithmetic Site*]. At rational $\lambda$ these are the multiplication correspondences.

**Layer 2 (adelic / spectral; known — this is the answer).** The points of $\mathscr A$ over $\mathbb R_+^{\max}$ form the adele class space $\mathbb Q^\times\backslash\mathbb A_\mathbb Q/\widehat{\mathbb Z}^\times$ [CC], and $\Psi_\lambda$ acts on points as the **scaling flow**. Its Hilbert realization is the scaling unitary group $\theta_\lambda=e^{i(\log\lambda)D}$ with generator $D$ — the timelike direction of P∞'s Lorentzian metric. The intersection pairing of the correspondence classes is the **trace pairing**: the distributional trace of $\int f(\lambda)\,\theta_\lambda\,d^\times\lambda$ is the Riemann–Weil explicit formula [Connes 1999], so
$$\langle\Psi_f,\Psi_f\rangle_\sigma\ \ge\ 0\ \text{ for all }f \iff \text{Weil positivity}\iff\mathrm{RH}.$$
The "spectral Hodge index on the $\mathbb F_1$ square" is precisely Weil positivity of the trace pairing on the $\theta$-correspondence algebra. The Frobenius eigenvalue $\sqrt q$ has no finite avatar; the flow's **modulus** (its measure expansion $d(\lambda x)=\lambda\,dx$) carries the degree (§2(iii)).

**Layer 3 (prolate compression; known, CCM).** Compressing the flow by the prolate projection yields CCM's operator frame: positivity is **proved** on the prolate-cutoff filtration ($\zeta$-zeros on the line at each finite cutoff), and RH $\iff$ the index survives the limit, $\mu_\lambda\downarrow0$ [CCM, *Zeta Spectral Triples*; *Zeta zeros and prolate wave operators*]. This is the proven *partial* index theorem; its limit is the program's one open step.

**Layer 4 (finite apex compression; this paper).** At level $m\mid P_n$ the correspondences compress to the multiplication graphs $\Gamma_a=\{(x,ax)\}\subset(\mathbb Z/m)^2$, $a\in(\mathbb Z/m)^\times$ — the unit rotations $U_a$ of the apex channel (T0, N14 §7.4). Theorem B.1 proves this layer cannot carry the index — which is *why* the realization is forced up to Layer 2/3.

---

## 2. Theorem B.1 — order-2 blindness of the finite Frobenius lattice $[\mathsf P$, certified$]$

Let $m$ be squarefree. All statements certified exactly in `empirical/p_infinity/probe_finite_frobenius_lattice.py` (GREEN, $m\in\{7,30,210\}$, $p\in\{7,13\}$).

**(i) The overlap Gram is the gcd circulant.** $\Gamma_a\cdot\Gamma_b=\#\{x:ax=bx\}=\gcd(a-b,m)$, an additive circulant with eigenvalues (additive characters $k$, by CRT per prime)
$$\lambda_k\;=\;\prod_{p\mid m}\big((p-1)+p\,[\,p\mid k\,]\big)\;>\;0 .$$
*Positive-definite* (Smith) — a genuine inner product, hence **no index**; even in $k\mapsto-k$; a function of $\gcd(k,m)$ only. *Order-2 set data sees the divisor lattice and nothing else.*

**(ii) The composition (Weil) pairing is ramification-support-only.** On units, $T(a,b)=\gcd(ab^{-1}-1,m)$ (the coincidence count of $\Gamma_a\circ\Gamma_b^{t}$ with the diagonal) is a multiplicative circulant with eigenvalues, for a Dirichlet character $\chi=\prod\chi_p$,
$$\mu_\chi\;=\;\prod_{p\mid m}(p-1)\,\big(1+[\,\chi_p=\chi_0^{(p)}\,]\big)\;>\;0,$$
*real, equal for $\chi$ and $\bar\chi$, and depending only on the set of primes where $\chi$ ramifies.* No Gauss phases, no $L$-values, no chirality: the order-2 multiplicative invariant is the conductor's **support**, full stop. (Proof: per prime, $\sum_{c}\gcd(c-1,p)\bar\chi_p(c)=\sum_c\bar\chi_p(c)+(p-1)\bar\chi_p(1)$.)

**(iii) The finite Weil form has empty positive sector.** With Weil's functional $\sigma(Z)=d_1+d_2-Z\cdot\Delta$ and the finite graphs ($d_1=d_2=1$), the form $Q(f)=\sigma(Z_f\circ Z_f^{t})$ diagonalizes with spectrum
$$\widehat\sigma(\chi)\;=\;2\varphi(m)\,[\chi=\chi_0]\;-\;\mu_\chi\;\le\;0,$$
with equality **iff** $m$ is prime and $\chi=\chi_0$ (the lightlike touch); for composite $m$ the whole lattice sits strictly inside the negative cone (certified: $\max=-16$ at $m=30$, $-96$ at $m=210$). The hyperbolic pole plane — Weil's lightlike fiber pair $f_1,f_2$, which on the $\zeta$ side is the certified $e^{\pm x/2}$ pole pair of W1's $A_\infty$ (N0 Lemma 6.10) — **cannot be generated at finite level**, because the finite correspondences are degree-1 (unitary). And this is not an artifact of the multiplicative model: even the true Frobenius $x\mapsto x^q$ on $\mathbb F_{q^2}$ is a **bijection on points** (certified: image $25/25$, fixed points $5=q$ on $\mathbb F_{25}$); its scheme degree $q$ lives in the cotangent collapse $dz^q=0$, invisible set-theoretically. **Degree/expansion is not point data.** Over $\mathbb Q$, the only carrier of that infinitesimal expansion is the archimedean modulus of the scaling flow — the measure expansion of $\theta_\lambda$ — which is N4's archimedean $\sqrt q$ made precise. $\square$

**Reading.** Every order-2 invariant of the finite Frobenius lattice is real, conjugation-even, and a function of $\{\gcd\}\cup\{\text{ramification support}\}$. The Conductor Blind Spot, at the level of the $\mathbb F_1$-square geometry: the quadratic layer of the finite world is *arithmetic-free*.

---

## 3. Theorem B.2 — arithmetic enters at order 3 $[\mathsf P$, certified; classical inputs as marked$]$

**(iv) The first phases are the Jacobi sums.** The order-3 additive-multiplicative contraction of the same lattice is $J(\chi,\psi)=\sum_x\chi(x)\psi(1-x)$. For $\chi,\psi,\chi\psi$ nonprincipal: $|J|=\sqrt p$ (elementary, Gauss-sum quotient — certified to $4\cdot10^{-15}$), the phases are **non-real in every admissible pair** (certified: $20/20$ at $p=7$, $110/110$ at $p=13$), and global conjugation flips them, $J(\bar\chi,\bar\psi)=\overline{J(\chi,\psi)}$ — the chirality involution. These are the **Frobenius eigenvalues of the abelian (Fermat) quotients** (Weil): the function-field door's identification *multiplicative apex amplitudes = Jacobi sums = Frobenius eigenvalues*, now placed as the **first** invariant layer of the finite Frobenius lattice that carries arithmetic.

**(v) The discrete cubic witness is the lattice's order-3 mass.** The V-sector count of *ocho* §5.1 — $S(p)=\#\{$unordered triples of nonzero residues, $a+b+c\equiv0\ (\mathrm{mod}\ p)\}$ — is exactly the order-3 selection-rule mass of the unit lattice ($S(2)=0$, $S(3)=2$, $S(p)=(p^2-1)/6$; brute-force re-certified through $p=13$, $\mathrm{pure}_V(P_n)=\sum_iS(p_i)$ reproducing *ocho* §5.2's table through $n=6$). So $\mathrm{pure}_V$ — the margin of the entire dispersion route, the right-hand side of the bridge inequality (*diez* Thm 4.3) — **is the order-3 invariant of the Frobenius lattice itself.** $\square$

---

## 4. Corollary B.3 — the two shadows of one index $[\mathsf A$ structure; components as tagged$]$

The Weil-surface dictionary, each row anchored where marked:

| $\mathbb F_q$ surface $C\times C$ | $\zeta$ side | anchor |
|---|---|---|
| lightlike fiber pair $f_1,f_2$ | poles $\rho=0,1$: the $e^{\pm x/2}$ pair in $A_\infty$ | W1 $=$ N0 Lemma 6.10, certified $10^{-21}$ $[\mathsf P]$ |
| $Z\cdot\Delta$ (fixed points) | prime side of the explicit formula | Connes trace pairing $[\mathsf P]$ |
| primitive part of $\mathrm{NS}$ | fluctuations $\Delta(a)=\psi(X;d,a)-\mu$ | Lemma 6.8 $[\mathsf P]$ |
| primitive self-intersection | variance $V(d)=\sum_a\Delta(a)^2$ | $[\mathsf A]$ |
| Hodge-index spacelike bound | **T1**: sparse-primorial BDH, $V\ll X\log X$ | the binding wall $[\mathsf C]$ |
| Frobenius-angle (Sato–Tate) layer | **T2**: signed third moment, CLT scale | true-with-room $[\mathsf E]$ |
| fiber-pure effective order-3 mass | $\mathrm{pure}_V(P_n)$ | Thm B.2 $[\mathsf P]$ |
| index proved on a filtration | CCM prolate-cutoff positivity | $[\mathsf P]$, published |
| the index itself | Weil positivity $=\mu_\lambda\downarrow0$ $=$ RH | the open step $[\mathsf C]$ |

**(a) The witness must be cubic.** By Thm B.1 there is *no* order-2 finite witness: the quadratic invariants of the finite Frobenius lattice contain no arithmetic to witness. The minimal finite-visible arithmetic-bearing invariant is order 3 (Thm B.2) — hence the dispersion route's discrete witness is $\mathrm{pure}_V$, a cubic object, *necessarily*.

**(b) The wall is still quadratic.** Inside the cubic functional, the binding estimate (T1) is the variance — the primitive-part norm — i.e. the quantitative shadow of the Hodge index. The cubic detour relocates the *witness*, not the *difficulty*: square-root cancellation in the fluctuations is what the index outputs over $\mathbb F_q$ ($|a_n|\le 2g\,q^{n/2}$), and it is what T1 demands over $\mathbb Q$.

**(c) The certificate is necessarily spectral.** Thm B.1(iii) is a third, independent exclusion of finite witnesses — *geometric* this time (empty positive sector; degree invisible on points) — after the archimedean No-Go (the archimedean place is not finitely-prime-generable) and P∞-A Prop 8.3a (no finite modular witness: $[\log\Delta,P]=2\pi iP\Rightarrow P=0$ finite-dimensionally). Three different formalisms, one verdict: **the order-2 certificate exists, if at all, only on the archimedean/spectral completion** — the scaling flow's correspondence algebra, where CCM's prolate filtration has already proved every finite stage.

**Conclusion of the corollary.** The dispersion route (finite-visible, order-3 witness, order-2 wall) and the CCM route (spectral, order-2 index, $\mu_\lambda\downarrow0$) are not parallel attacks; they are the **two shadows of the single missing object** — the Hodge index on $\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}\mathrm{Spec}\,\mathbb Z$, realized as Weil positivity of the scaling-correspondence trace pairing. P∞'s allocation verdict (the program's edge is the spectral/CCM side) is hereby *derived*: the finite side is provably blind to what must be certified.

---

## 5. Honest status

| claim | tier |
|---|---|
| $\Psi_\lambda$ realized by the scaling flow $\theta_\lambda$ (points level) | $[\mathsf P]$ — Connes–Consani, cited |
| trace pairing $=$ explicit formula; Weil positivity $\iff$ RH | $[\mathsf P]$ — Connes, cited |
| prolate-cutoff positivity (partial index) | $[\mathsf P]$ — CCM, cited |
| Thm B.1 (i)–(iii): order-2 finite blindness, empty positive sector, degree-1 | $[\mathsf P]$ — this paper, certified GREEN |
| Thm B.2 (iv)–(v): order-3 first visibility; $\mathrm{pure}_V$ $=$ lattice order-3 mass | $[\mathsf P]$ — this paper, certified GREEN |
| Cor B.3 dictionary and two-shadows reading | $[\mathsf A]$ — structural |
| the index itself ($\mu_\lambda\downarrow0$ $=$ Weil positivity $=$ RH) | $[\mathsf C]$ — open, untouched here |

This paper proves nothing about the open step. Its contribution is **necessity** (the certificate cannot be finite — third independent proof), **unification** (both program routes derived as shadows of one object, the allocation verdict turned from choice into theorem), and the **degree-carrier identification** (the Frobenius scheme-degree, invisible on points, is carried over $\mathbb Q$ by the archimedean modulus of the scaling flow). What would close RH is unchanged and now singly-located: the spectral Hodge index — positivity of the trace pairing on the full scaling-correspondence algebra, equivalently the CCM limit $\mu_\lambda\downarrow0$.

---

## References and anchors

- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999).
- A. Connes, C. Consani, *The Arithmetic Site* / *Geometry of the Arithmetic Site* (the Frobenius correspondences $\Psi_\lambda$; points over $\mathbb R_+^{\max}$ = adele class space).
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators* (Ann. Funct. Anal. 15, 2024); *Zeta Spectral Triples* (arXiv:2511.22755).
- A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent* (the surface proof; Jacobi sums as Frobenius eigenvalues).
- Program: P∞ (the Lorentzian intersection metric; §1.5 the open object); P∞-A (Prop 8.3a); T0/T8 (apex frames); N4 (archimedean $\sqrt q$, the $1/8$-turn); N0 Lemma 6.8, Lemma 6.10 (W1); *ocho* §5 ($\mathrm{pure}_V$); *diez* Thm 4.3 (T1/T2); N11-2 (the moment/L-P closure).
- Certificate: `empirical/p_infinity/probe_finite_frobenius_lattice.py` — GREEN, 30 checks, exact arithmetic.
