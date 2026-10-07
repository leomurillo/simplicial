# N9 — The Cross-Prime Fusion Criterion: Euler Closure, the Davenport–Heilbronn No-Go, and the Archimedean Residue

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*June 6, 2026*

<!--
Program record. N9 is the honest outcome of the "No-Go audit" that followed N8. N8 attempted to
force Li-coefficient positivity (RG fixed-point stability) from the finite cubic Gram; the audit
showed the finite/algebraic structure cannot supply it (its moments are flat — Tr((G^(3))^n)=N-2 —
while lambda_n ~ (n/2)log n is irreducibly infinite/archimedean by T12+T15). N9 turns the
Davenport–Heilbronn trap into a positive result: it isolates the exact structural invariant that
separates the RH-respecting class from RH-violating Dirichlet series with a functional equation,
shows it is cross-prime multiplicativity (the Euler product / cross-prime fusion closure of T8 §3.4,
T11), discharges the Davenport–Heilbronn family by it, and proves it is NECESSARY but not SUFFICIENT
— the residue being the archimedean self-adjointness of N5 / Connes–Consani. It does NOT prove RH and
does not claim to. Certificates under empirical/: probe_fusion_closure_nogo.py (the invariant; the
No-Go; order-3=order-2), probe_n8_density_and_parity.py and probe_adelic_weil_margin.py (the
archimedean residue is marginal), probe_li_chiral_stability.py (the stability target is unitarity,
not positivity).
-->

---

## Abstract

A functional equation does not imply the Riemann Hypothesis: the Davenport–Heilbronn family has a functional equation yet infinitely many zeros off the critical line. We identify, and certify, the exact structural invariant that the genuine $\zeta$- and $L$-functions possess and the counterexamples lack: **cross-prime multiplicativity** $a_{mn}=a_ma_n$ on coprime arguments — equivalently the Euler product, equivalently the cross-prime fusion closure of the multiplicative apex ([T8] §3.4, [T11]). We prove three things. First $\mathsf{[P]}$, the invariant separates the classes exactly: $\zeta$ and every primitive Dirichlet $L$ have cross-prime defect $0$; the Davenport–Heilbronn function has defect bounded away from $0$. Second $\mathsf{[P]}$, the order-three fusion vertex imposes no constraint beyond order two — cross-prime closure is pairwise-generated. Third $\mathsf{[A]}$, cross-prime fusion closure is exactly the Euler/tensor factorization $H=\bigotimes_p H_p$ of the associated operator, which the Davenport–Heilbronn operator lacks. We then state the reduction precisely: within the fusion-closed (Selberg) class, RH is equivalent to the **archimedean self-adjointness** of the completed operator — eigenvalues on the line, not merely a positive form. Cross-prime fusion closure is **necessary** for this but does **not** supply it; the residue is the archimedean positivity of [N5] / Connes–Consani, which is open. N9 therefore characterizes the RH-respecting class and discharges the Davenport–Heilbronn obstruction; it does not prove the Riemann Hypothesis, and the residue it isolates is archimedean, not multiplicative.

**MSC 2020:** 11M26, 11M41, 11N37, 47A10, 11F66.

---

## 1. The question

The Riemann Hypothesis is often approached through the completed function $\xi(s)=\xi(1-s)$ and its positivity criteria (Weil, Li). A recurring temptation is to derive RH from the self-dual structure — the functional equation — alone. That cannot work, and the obstruction is classical.

**Fact 1.1 (Davenport–Heilbronn, 1936).** *Let $\chi$ be the order-four Dirichlet character modulo $5$ with $\chi(2)=i$, and set $\kappa=(\sqrt{10-2\sqrt5}-2)/(\sqrt5-1)\approx0.2841$. The function*
$$
f(s)=\tfrac{1-i\kappa}{2}\,L(s,\chi)+\tfrac{1+i\kappa}{2}\,L(s,\overline\chi)
$$
*satisfies a functional equation $s\leftrightarrow 1-s$ of Riemann type, yet has infinitely many zeros with $\operatorname{Re}(s)\neq\tfrac12$.*

So the functional equation is not the operative content of RH. The natural program question — and the one the apex/cubic machinery is built to ask — is structural:

> **What property do $\zeta$ and the genuine $L$-functions possess, that a functional-equation series with off-line zeros must lack?**

We answer it. The property is cross-prime multiplicativity, and it is exactly the cross-prime fusion closure of the multiplicative apex.

---

## 2. Cross-prime fusion closure

Write a Dirichlet series as $D(s)=\sum_{n\ge1}a_n n^{-s}$.

**Definition 2.1.** $D$ is **cross-prime fusion-closed** if $a_{mn}=a_m a_n$ for all coprime $m,n$.

**Proposition 2.2 (closure $=$ Euler product).** *$D$ is cross-prime fusion-closed if and only if it admits an Euler product $D(s)=\prod_p D_p(s)$ with $D_p(s)=\sum_{k\ge0}a_{p^k}p^{-ks}$.* This is the standard correspondence between multiplicativity and Euler factorization; in the program's language it is the cross-prime sector of the multiplicative apex generator $\mathcal D_x(\beta,\psi)$ ([T8] Def. 2.1), separated from the intra-prime (prime-power) recurrence in [T8] §3.4 and realized as the conductor-fusion vertex of [T11].

The distinction [T8] §3.4 draws — intra-prime versus cross-prime — is exactly the one that matters here. The Davenport–Heilbronn coefficients **do** satisfy a per-prime (intra-prime) linear recurrence: writing $a_n=\operatorname{Re}\chi(n)+\kappa\operatorname{Im}\chi(n)$, the local sequence $\{a_{p^k}\}_k$ obeys a second-order recurrence (two geometric terms $\chi(p)^k,\overline\chi(p)^k$). What fails is **cross-prime** fusion.

**Lemma 2.3 (order three is downstream of order two).** *For cross-prime fusion-closed $D$, $a_{pqr}=a_pa_qa_r$ for distinct primes $p,q,r$, and this is a consequence of pairwise closure: $a_{pqr}=a_{(pq)r}=a_{pq}a_r=(a_pa_q)a_r$. Conversely, no relation among triples constrains $D$ beyond the pairwise relations.* Hence the order-three fusion vertex of [T11] carries no information about RH-class membership beyond order two; cross-prime closure is pairwise-generated.

(This is the precise sense in which the cubic apex calculus, while genuine, does not refine the multiplicative criterion: multiplicativity is an order-two phenomenon on coprime arguments.)

---

## 3. The Davenport–Heilbronn No-Go $\mathsf{[P]}$

**Theorem 3.1 (the invariant separates the classes).** *Cross-prime fusion closure separates the RH-respecting Dirichlet series from the Davenport–Heilbronn family:*

1. *$\zeta$ ($a_n=1$) and every primitive Dirichlet $L$-function ($a_n=\chi(n)$) are cross-prime fusion-closed: the defect $a_{mn}-a_ma_n$ is identically $0$.*
2. *The Davenport–Heilbronn function of Fact 1.1 is **not** cross-prime fusion-closed: $a_{mn}-a_ma_n\not\equiv0$. With the $\kappa$ above, the cross-prime defect equals $1+\kappa^2\approx1.081$ whenever $\chi(m),\chi(n)$ are both nontrivial, and the order-three defect is $\approx0.307$.*

*Proof.* (1) is the multiplicativity of $\chi$ (and of $a_n\equiv1$). For (2), with $a_n=\alpha\chi(n)+\beta\overline\chi(n)$, $\alpha=\tfrac{1-i\kappa}2$, $\beta=\tfrac{1+i\kappa}2$,
$$
a_{mn}-a_ma_n=(\alpha-\alpha^2)\chi(mn)+(\beta-\beta^2)\overline{\chi(mn)}-\alpha\beta\big(\chi(m)\overline\chi(n)+\overline\chi(m)\chi(n)\big),
$$
which does not vanish when $\chi(m),\chi(n)\notin\{1\}$ (it vanishes only on the trivial coset $m\equiv1$ or $n\equiv1\pmod5$, where one factor is $1$). Certified to machine precision in `empirical/probe_fusion_closure_nogo.py` over the prime pairs $(2,3),(3,7),(2,7),(7,13),(3,13),(2,13)$ (defect $1.081$) and triples (defect $0.307$), with $\zeta,L(\cdot,\chi_3)$ at $0$ exactly. $\square$

**Corollary 3.2 (the No-Go).** *The functional equation does not imply cross-prime fusion closure (Fact 1.1 vs Theorem 3.1(2)). Equivalently: cross-prime fusion closure is a strictly stronger condition than self-duality, and it is the one the off-line-zero counterexamples violate. Any positivity/stability criterion intended to force RH must use cross-prime fusion closure, not merely the functional equation.*

This discharges the Davenport–Heilbronn obstruction in the program's own terms: DH is not a counterexample to "fusion-closed series satisfy RH," because DH is not fusion-closed. It **is** a counterexample to "self-dual series satisfy RH," which is why every functional-equation-only argument fails.

---

## 4. The operator meaning $\mathsf{[A]}$

**Proposition 4.1 (closure $=$ tensor factorization).** *Let $H$ be the operator whose Dirichlet-series data is $D$ (the assembled apex/Weil operator of [N1], [N5]). Cross-prime fusion closure of $D$ is equivalent to the Euler/tensor factorization*
$$
H=\bigotimes_p H_p,
$$
*the local operators $H_p$ governing the prime-power (intra-prime) sectors. The Davenport–Heilbronn operator admits no such factorization: being $\tfrac{1-i\kappa}2\,H_\chi\oplus\tfrac{1+i\kappa}2\,H_{\overline\chi}$ on the additive (linear-combination) side, it has no multiplicative/tensor decomposition over primes.*

This is the structural payoff. Cross-prime fusion closure supplies the **multiplicative skeleton** — the tensor structure over primes — that any spectral realization of the zeros must have, and that the function-field case has automatically (Frobenius acts diagonally on the prime-by-prime cohomology). It is the part of the Hilbert–Pólya/Connes architecture that the apex program genuinely contributes.

It is **not**, however, self-adjointness. A tensor product of local operators is unitarily structured prime-by-prime; whether the **global** completed operator has its spectrum **on the critical line** is a separate, archimedean question.

---

## 5. The reduction and the archimedean residue $\mathsf{[A]}+\mathsf{[C]}$

We can now state exactly what cross-prime fusion closure does and does not achieve for RH.

**Theorem 5.1 (reduction within the fusion-closed class).** *Let $D$ be cross-prime fusion-closed of Selberg type (Euler product, functional equation, Ramanujan bound, analytic continuation). Then RH for $D$ is equivalent to the **archimedean self-adjointness** of its completed operator: in the Li/spectral encoding, every spectral value $1-1/\rho$ lies on the unit circle $\iff$ every $\rho$ on the line; in the Weil encoding, the completed quadratic form is positive semidefinite in the archimedean limit.* $\mathsf{[A]}$

Two points fix the location of the difficulty, both established earlier in the program and re-certified here.

**Remark 5.2 (the target is unitarity, not positivity).** The Li values $1-1/\rho$ lie on the unit circle precisely when $\rho$ is on the line; the relevant operator is therefore **unitary** (spectrum on $|z|=1$), and $\lambda_n=\sum_\rho[1-(1-1/\rho)^n]\ge0$ holds termwise via $1-\cos n\phi_\rho\ge0$. A *positive* ($A^*A$, spectrum in $[0,\infty)$) operator is the wrong class — its spectrum is not the unit circle. This corrects the natural but mistaken "sum-of-squares" reading (cf. the N8 audit): the stability sought is unitarity of the infinite archimedean operator, which is RH. Certified in `empirical/probe_li_chiral_stability.py` (a single off-line zero drives $\lambda_n$ negative; on-line zeros contribute $2(1-\cos n\phi)\ge0$).

**Remark 5.3 (the residue is archimedean, and fusion closure does not supply it).** Cross-prime fusion closure is finite/multiplicative; the archimedean self-adjointness is infinite. The assembled completed form is **marginal**, not manifestly self-adjoint: its minimal eigenvalue is $\approx-10^{-5}$ and drifts negative as primes enter (`empirical/probe_adelic_weil_margin.py`), the marginal direction being sculpted by the zeros ([N5] §6). The finite apex algebra is determinate ([T12], $\cong\mathbb R[t]/(P_x)$) and its moments are flat, so it **cannot** generate the $\tfrac n2\log n$ growth of $\lambda_n$; that growth is the infinite accumulation of zeros, which [T15] proves is "not a finite packet." Hence the residue — archimedean self-adjointness — is exactly the open Connes–Consani archimedean positivity, and no multiplicative (fusion) structure produces it.

**Main statement (N9).** *Cross-prime fusion closure is **necessary** for RH (Theorem 3.1, Corollary 3.2) and is the precise invariant the Davenport–Heilbronn counterexamples violate; it supplies the multiplicative/tensor skeleton (Proposition 4.1); but it is **not sufficient** (Remark 5.3). Within the fusion-closed Selberg class, RH reduces to archimedean self-adjointness (Theorem 5.1), which is open.* $\mathsf{[A]}+\mathsf{[C]}$

The conjecture "Selberg class $\Rightarrow$ RH" is the residual content marked $\mathsf{[C]}$; it is equivalent to the Riemann Hypothesis for the relevant $D$ and is not proved here.

**Conjecture 5.4 (the fusion-contingent metric — the forward door) $\mathsf{[C]}$.** *Let $\mathcal U$ be the apex–archimedean operator ([N5]) and, for a completed Dirichlet series $D$ of Riemann type, let $\eta_D$ be the de Branges/divisor metric: the inner product of $L^2(\mathrm{div}\,D)$ in which the resolvent states $R_z=1/(\gamma-z)$ have Gram $P_D$ (the Pick $=$ resolvent-Gram identity, [N10]). For every Selberg-class $D$, $\eta_D$ is positive — equivalently $P_D\succeq0$, equivalently $\mathcal U$ is quasi-Hermitian on the test space of $D$ (the non-normal archimedean phase $\sqrt i$ resolved into real spectrum), equivalently RH for $D$.*

By Theorem 5.1 this is equivalent to the residue "Selberg $\Rightarrow$ RH"; its content is not a weakening but a **shape constraint**. The same positivity is *false* for the non-fusion-closed $f$ of Fact 1.1: $\eta_f$ is indefinite, carrying exactly one negative square per off-line zero (the generalized-Nevanlinna signature theorem, [N10]). Hence any proof of Conjecture 5.4 must use cross-prime fusion closure (Definition 2.1) essentially. It is the unique form of the residue that is at once **fusion-sighted** — so the Davenport–Heilbronn No-Go (§3) bars the counterexamples from impersonating $\zeta$ — and **archimedean** — it concerns the positivity of the metric / the self-adjointness of $\mathcal U$, not merely the functional equation. Every functional-equation-only or on-axis reformulation closed in [N11] is fusion-blind, and Davenport–Heilbronn refutes each; Conjecture 5.4 it does not refute. It is the correctly-shaped target for the archimedean realization of [N5]/Connes–Consani consolidated in [N11].

**Remark 5.5 (the fusion-sighted half is realized, exactly) $\mathsf{[P]}$.** The fusion-closure side of Conjecture 5.4 is now an exact finite signature. Over $(\mathbb Z/N)^\times$ the fusion matrix $\Phi_{mn}=a(mn)$ is rank-one (positive) for fusion-closed data ($\zeta$, a primitive character $\chi$) and carries an exact negative square for the non-fusion-closed Davenport–Heilbronn coefficients $a=\operatorname{Re}\chi+\kappa\operatorname{Im}\chi$ — there $\operatorname{tr}\Phi=\sum_m a(m^2)=0$ with $\Phi\neq0$, forcing indefiniteness. A positive archimedean weight $W\succ0$ is Sylvester-neutral on $\Phi$ ($\operatorname{inertia}(W\Phi W)=\operatorname{inertia}\Phi$), so the multiplicative half of the metric is finite, exact, and well-conditioned while only the archimedean half is transcendental ([N5, Rem. 8.1]). The caveat of Theorem 3.1 persists at the signature level — positive semidefiniteness is necessary but not sufficient for fusion-closure (a positive combination of characters is also PSD), so the sharp invariant is rank-one, not mere PSD. (Certified `empirical/probe_helmert_fourier_fusion_metric.py`.)

---

## 6. Honest status

What is **proved or certified** $\mathsf{[P]}$: cross-prime fusion closure separates $\zeta$ and primitive $L$ (defect $0$) from the Davenport–Heilbronn family (defect $\ge1$), so the functional equation does not imply RH while fusion closure is the violated invariant (Theorem 3.1, Corollary 3.2); the order-three vertex adds nothing beyond order two (Lemma 2.3). What is **structural** $\mathsf{[A]}$: fusion closure is the Euler/tensor factorization $H=\bigotimes_pH_p$ (Proposition 4.1); within the Selberg class RH reduces to archimedean self-adjointness, and the target is unitarity, not positivity (Theorem 5.1, Remark 5.2). What is **open** $\mathsf{[C]}$: archimedean self-adjointness itself — equivalently Selberg-class $\Rightarrow$ RH, equivalently the Connes–Consani archimedean positivity, equivalently the fusion-contingent metric (Conjecture 5.4) — which fusion closure does not supply (Remark 5.3).

This program does not prove the Riemann Hypothesis, and N9 does not claim it. N9 is a **characterization-and-No-Go** result: it names the invariant that defines the RH-respecting class, certifies that the standard counterexamples fail it, and proves that the difficulty that remains is archimedean rather than multiplicative. The separation is the program's discipline: **structural reduction — real; proof of RH — not yet.**

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries.*

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.*

[N8] Murillo Montero, L. (2026). *The Summit* (superseded in its positivity claim by the present audit).

[N10] Murillo Montero, L. (2026). *The Bures–Cayley Geometric Reduction of RH and Its Ceiling.*

[N11] Murillo Montero, L. (2026). *The Capstone: One Wall, Mapped.*

[T8] Murillo Montero, L. (2026). *The Multiplicative Apex and Finite Dirichlet Polynomials.*

[T11] Murillo Montero, L. (2026). *Apex Vertex Calculus.*

[T12] Murillo Montero, L. (2026). *The Finite Apex Determinacy Theorem.*

[T15] Murillo Montero, L. (2026). *Finite-to-Archimedean Completion.*

[DH] Davenport, H., Heilbronn, H. (1936). *On the zeros of certain Dirichlet series.* J. London Math. Soc. 11, 181–185, 307–312.

[Sel] Selberg, A. (1992). *Old and new conjectures and results about a class of Dirichlet series.* Proc. Amalfi Conf. Analytic Number Theory, 367–385.

[CC] Connes, A., Consani, C. (2021). *Weil positivity and trace formula: the archimedean place.* Selecta Math. 27, art. 77.

[Li] Li, X.-J. (1997). *The positivity of a sequence of numbers and the Riemann Hypothesis.* J. Number Theory 65, 325–333.
