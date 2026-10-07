# N10 — The Bures–Cayley Geometric Reduction of the Riemann Hypothesis and Its Ceiling

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*June 6, 2026*

<!--
Program record. N10 closes the geometric arc that began with the de Branges target (N0/N5–N6),
passed through the finite Z/6 Bures–Cayley carrier (Note_TetrahedralBuresCayleyBridge t6Yp3) and the
infinite divisor Hilbert space (Note_InfiniteCMDivisorHilbert Q2wL9, Note_ArchimedeanSelectionFrontier
L5zR1), and asked whether the simplex positivity of the Cayley–Menger determinant can FORCE the
de Branges/Pick positivity (= RH) the way Castelnuovo–Hodge forces |alpha|=sqrt q over F_q. The answer,
established here, is a clean negative with a precise reason: the relevant Hermitian Gram is a
generalized-Nevanlinna kernel whose negative index EQUALS the number of off-line zeros, so it has NO
fixed Hodge signature — its signature IS the count RH asks about. The free simplex positivity is the
on-axis shadow only. The paper records the reduction (real and sharp), the signature theorem (the
ceiling), and the exact object the geometric leap would require (a fixed-signature Hermitian form on a
fixed number-field surface — the missing F_1 geometry). It does NOT prove RH and does not claim to.
Certificates: empirical/probe_cayley_menger_hamiltonian.py (Pick=resolvent Gram; on-axis-free/off-axis
split), empirical/probe_complexified_cone_signature.py (kappa = #off-line zeros; fixed-signature
contrast).
-->

---

## Abstract

The Riemann Hypothesis is equivalent to the de Branges/Herglotz positivity of $m_B=-\Xi'/\Xi$ (equivalently $E_B=\Xi+i\Xi'$ Hermite–Biehler). The program's finite $\mathbb Z/6$ Bures–Cayley carrier realizes $\mathbb Z/6$ as the six-edge coordinate system of the $N=4$ tetrahedron, identifies the Cayley–Menger volume-square as a cubic curvature whose vanishing locus is the divisor of $\Xi$, and raises a geometric hope: that the *free* positivity of a Euclidean simplex (the Cayley–Menger cone) could force the Pick positivity, as Castelnuovo–Hodge forces $|\alpha|=\sqrt q$ over $\mathbb F_q$. We settle this hope. We prove $\mathsf{[P]}$ that the Pick kernel of $m_B$ equals the resolvent Gram in the divisor Hilbert space (so Pick positivity $\iff$ positive divisor measure $\iff$ RH); that on the critical line the Bures edges are real and the Cayley–Menger cone membership is automatic, but off the line the edge-squares are complex and cone membership reduces exactly to Pick positivity; and, centrally, that the Hermitian Bures–Cayley Gram is a **generalized-Nevanlinna kernel whose negative index $\kappa$ equals the number of zeros of $\Xi$ off the critical line**. Hence it has **no fixed Hodge-type signature**: its signature is the very count RH asks about, and $\kappa=0\iff$ RH. We then show $\mathsf{[A]}$, in signature form, why the $\mathbb F_q$ Hodge mechanism does not lift — the three failures (a $z$-parameterized rather than fixed surface; a continuous rather than finite-rank Frobenius substitute; a fixed-signature object available only on-axis) are one obstruction, the missing $\mathbb F_1$ self-product geometry. The Bures–Cayley route is thereby the sharpest *geometric* reduction of RH in the program — it names the exact missing object (a fixed-signature Hermitian form on a fixed number-field surface, on which the apex–archimedean class lands definitely) — but it does not supply it. This is a reduction-and-ceiling theorem, not a proof of RH.

**MSC 2020:** 11M26, 46E22, 47B32, 51K05, 30H15.

---

## 1. The target and the geometric question

Write $\Xi(z)=\xi(\tfrac12+iz)$, $E_B(z)=\Xi(z)+i\Xi'(z)$, $m_B(z)=-\Xi'(z)/\Xi(z)$. The classical de Branges/Krein equivalences are unconditional:
$$
\mathrm{RH}\iff E_B\ \text{Hermite–Biehler}\iff m_B\ \text{Herglotz}\iff P_B\succeq0,
$$
where $P_B(z,w)=\dfrac{m_B(z)-\overline{m_B(w)}}{z-\overline w}$ is the Pick kernel.

Over a function field $\mathbb F_q$, the analogous positivity is *not* conjectural: it is forced by the Castelnuovo–Hodge index theorem on the fixed surface $C\times C$, whose intersection form has the fixed signature $(1,\rho-1)$, with Frobenius a finite-rank class landing in the definite part ([P4] settles this instance by counting). The geometric question of the program is whether a number-field substitute for that surface — the finite $\mathbb Z/6$ Bures–Cayley simplex — can supply the same forcing.

This paper answers it: the substitute exists and is sharp, but it carries **no fixed signature**, and that is exactly why it does not force RH.

---

## 2. The Bures–Cayley geometry

We recall the finite carrier ([t6Yp3]). Label the six edges of a tetrahedron $A,B,C,D$ by
$$
e_0=AB,\ e_1=AC,\ e_2=AD,\ e_3=CD,\ e_4=BD,\ e_5=BC,
$$
so the odd vertex transposition $A\leftrightarrow B$ acts as $e_1\!\leftrightarrow\!e_5,\ e_2\!\leftrightarrow\!e_4$, fixing $e_0,e_3$ — i.e. $r\mapsto -r\pmod6$, with $K$-orbits $\{0\},\{3\},\{1,5\},\{2,4\}$.

**Proposition 2.1 ($\mathbb Z/6$ is the tetrahedral edge system).** *The Bures $K$-involution $r\mapsto-r\pmod6$ is exactly the odd tetrahedral edge reflection; the orbit structure is the tetrahedron's.* $\mathsf{[P]}$

For squared edges $x_r=\ell(e_r)^2$ the Cayley–Menger determinant $\Delta_{\mathrm{CM}}(x)=288\,V^2$ is a homogeneous **cubic** in $x_0,\dots,x_5$ — the geometric twin of the cubic Amari–Chentsov tensor, both at third order on the six $\mathbb Z/6$ channels. In $K$-adapted coordinates $A=x_0,B=x_3,C=\tfrac{x_1+x_5}2,U=\tfrac{x_1-x_5}2,D=\tfrac{x_2+x_4}2,V=\tfrac{x_2-x_4}2$, every term of $\Delta_{\mathrm{CM}}$ has even $K$-odd degree. The physical interior is the **edge cone** cut out by face inequalities and $\Delta_{\mathrm{CM}}\ge0$.

**Proposition 2.2 (zeros are degenerations).** *With the normalized Bures edge packet $q_B(z)$, the curvature scalar $\kappa_{\mathrm{CM}}^B(z)=\tfrac1{288}\Delta_{\mathrm{CM}}(q_B(z))$ has its vanishing locus on the divisor of $\Xi$: the tetrahedron degenerates ($V=0$) exactly at the zeros.* (The finite carrier identifies the divisor: $\mathcal T_{\mathrm{CM}}=\Xi$, [Q2wL9].) $\mathsf{[A]}$

---

## 3. The infinite space and the Pick = Gram identity $\mathsf{[P]}$

Let $\mu=\sum_{\gamma}m_\gamma\,\delta_\gamma$ be the divisor measure of $\Xi$ and $\mathcal H=L^2(\mu)$, with $R_z(\gamma)=1/(\gamma-z)$.

**Theorem 3.1 (Pick kernel $=$ resolvent Gram).** *Under boundary support $m_B(z)=\sum_\gamma m_\gamma/(\gamma-z)$, and*
$$
P_B(z,w)=\sum_\gamma\frac{m_\gamma}{(\gamma-z)(\gamma-\overline w)}=\langle R_z,R_w\rangle_{\mathcal H}.
$$
*Hence $P_B\succeq0\iff\mu\ge0\iff$ all zeros real $\iff$ RH.* $\mathsf{[P]}$ (Certified `probe_cayley_menger_hamiltonian.py`: $P_B$ PSD for zeros on the line, $\min\mathrm{eig}=+8\times10^{-10}$; one off-line zero gives $\min\mathrm{eig}=-1.4\times10^{-2}$; $\|P_B-\text{Gram}\|=3\times10^{-16}$.)

So the de Branges positivity is literally a Gram positivity in the divisor Hilbert space — the structure on which the Hilbert–Pólya operator is multiplication by $\gamma$ ([Q2wL9]).

---

## 4. On-axis free, off-axis RH $\mathsf{[P]}$

**Theorem 4.1 (the dichotomy).** *For real $z$ (the critical line) the Bures edge-squares $q_B(z)$ are real, $\Delta_{\mathrm{CM}}(q_B(z))$ is real, and cone membership $\Delta_{\mathrm{CM}}\ge0$ is automatic — Bures is a genuine metric, so the on-line tetrahedron is a real Euclidean cone member with positivity for free. For non-real $z$ the edge-squares are complex, $\Delta_{\mathrm{CM}}(q_B(z))$ is complex, and "cone membership" is no longer a real-simplex fact: it reduces to the Pick/Herglotz sign condition of §3.* $\mathsf{[P]}$ (Certified: at $z=10+i$, $\Delta_{\mathrm{CM}}=3.10+0.38i$ — not a real cone.)

The free metric positivity therefore lives precisely on the critical line, where it is silent about off-line zeros. The bridge needs positivity off the line, where it is RH.

---

## 5. The signature theorem: no fixed Hodge signature $\mathsf{[P]}$

This is the central result. Inject off-line zeros into the divisor and read the Hermitian signature of the Gram.

**Theorem 5.1 (generalized-Nevanlinna index).** *The Hermitian Bures–Cayley/Pick Gram is a generalized-Nevanlinna kernel (Kreĭn–Langer) whose number of negative squares equals the number of zeros of $\Xi$ in the open upper half-plane:*
$$
\kappa\big(P_B\big)=\#\{\text{zeros of }\Xi\text{ off the critical line, }\operatorname{Im}>0\}.
$$
*Consequently $P_B$ has no fixed signature: $\kappa=0\iff$ RH.* $\mathsf{[P]}$ (Certified `probe_complexified_cone_signature.py`: the count of negative eigenvalues equals the number of injected off-line zeros, $0,1,2,3,4,5$ on the nose.)

**Corollary 5.2 (no Hodge shortcut).** *A Castelnuovo–Hodge-type forcing requires a Hermitian/intersection form of fixed signature on which the distinguished class lands in a definite part. The Bures–Cayley Gram has no fixed signature — its negative index is exactly the off-line count — so it cannot force RH. The only fixed-signature object in the construction is the on-axis real Schoenberg/Bures Gram (signature $(3,0)$ for every Euclidean tetrahedron), which is the shadow of §4 and is silent off the line.* $\mathsf{[A]}$

---

## 6. Why the $\mathbb F_q$ mechanism does not lift $\mathsf{[A]}$

**Proposition 6.1 (the $\mathbb F_1$ obstruction in signature form).** *The Castelnuovo–Hodge forcing over $\mathbb F_q$ has three ingredients, each of which the number-field Bures–Cayley substitute lacks:*

1. *a **fixed** surface $C\times C$ with a topological intersection form of fixed signature $(1,\rho-1)$. The Bures–Cayley "surface" is **$z$-parameterized** — it moves with the spectral variable — so there is no fixed signature lattice (Theorem 5.1).*
2. *Frobenius as a **finite-rank** algebraic class landing in the definite part. The apex–archimedean operator (N4–N6) has **continuous/infinite** spectrum; the divisor is infinite ([T12] finite determinacy vs the $L^2(\operatorname{div}\Xi)$ limit, [T15] "not a finite packet").*
3. *the fixed-signature object available only as the **on-axis** real Gram (§4), which says nothing off the line.*

*These are one obstruction: the absence of a fixed number-field self-product surface ($\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$).* $\mathsf{[A]}$

---

## 7. The ceiling, stated exactly $\mathsf{[C]}$

**Reduction (what the geometry achieves).** RH is equivalent, within this geometry, to the off-axis positivity of the Hermitian Bures–Cayley Gram — equivalently $\kappa=0$, equivalently the existence of a positive canonical-system Hamiltonian $H_{\mathrm{CM}}(t)\succeq0$ with Weyl function $m_B$ ([L5zR1] Law C). This is a sharp, concrete, geometric statement of RH.

**Ceiling (what it does not achieve).** The geometric leap would require a **fixed-signature Hermitian form on a fixed number-field "surface"**, on which the apex–archimedean class lands definitely — i.e. precisely the missing $\mathbb F_1$ self-product geometry that Connes–Consani seek. Theorem 5.1 shows the only Hermitian form the Bures–Cayley construction supplies has variable signature ($=$ the off-line count), and Proposition 6.1 shows why no fixed substitute is available. **The Bures–Cayley route sharpens the target to that object; it does not provide it.** This residue is RH and is open. $\mathsf{[C]}$

---

## 8. Honest status

What is **proved or certified** $\mathsf{[P]}$: the $\mathbb Z/6$–tetrahedron identification (Prop 2.1); the Pick $=$ resolvent Gram identity, hence Pick positivity $\iff$ RH (Thm 3.1); the on-axis-free / off-axis-RH dichotomy (Thm 4.1); the generalized-Nevanlinna index theorem $\kappa=\#$off-line zeros, hence no fixed Hodge signature (Thm 5.1). What is **structural** $\mathsf{[A]}$: zeros as degenerations (Prop 2.2); the no-shortcut corollary (5.2); the signature-form $\mathbb F_1$ obstruction (Prop 6.1). What is **open** $\mathsf{[C]}$: $\kappa=0$ itself — equivalently the off-axis Gram positivity, equivalently the fixed-signature number-field surface — which is RH.

This program does not prove the Riemann Hypothesis, and N10 does not claim it. N10 is a **geometric reduction-and-ceiling** theorem: it builds the sharpest geometric form of the de Branges target the program owns (a Hermitian Gram from simplex edge geometry, with the zeros as degenerations), and proves that this object cannot force RH because its signature is the off-line count rather than a fixed invariant. The leap requires the one object that does not exist in the finite/multiplicative world — a fixed-signature self-product surface at the archimedean place. The separation is the program's discipline: **structural reduction — real; proof of RH — not yet.**

---

## References

[N0] Murillo Montero, L. (2026). *De Branges Exhaustion and Weil Domination.*

[N5–N6] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form; The Unified Archimedean Operator.*

[N9] Murillo Montero, L. (2026). *The Cross-Prime Fusion Criterion.*

[P4] Murillo Montero, L. (2026). *The Quantum Face, the Units, and the Proven Critical Line.*

[T12] Murillo Montero, L. (2026). *The Finite Apex Determinacy Theorem.*

[T15] Murillo Montero, L. (2026). *Finite-to-Archimedean Completion.*

[t6Yp3] Program note, *Tetrahedral Bures–Cayley Bridge.*

[Q2wL9] Program note, *Infinite CM Divisor Hilbert Space.*

[L5zR1] Program note, *Archimedean Selection Frontier.*

[dB] de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice-Hall.

[KL] Kreĭn, M. G., Langer, H. (1977). *Über die Q-Funktion eines $\pi$-hermiteschen Operators im Raume $\Pi_\kappa$.* (Generalized Nevanlinna functions and negative squares.)

[Sch] Schoenberg, I. J. (1935). *Remarks to Maurice Fréchet's article.* Ann. of Math. 36 (Euclidean distance matrices and conditional positivity).

[CC] Connes, A., Consani, C. (2021). *Weil positivity and trace formula: the archimedean place.* Selecta Math. 27, art. 77.
