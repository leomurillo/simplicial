# The Chirality Boundary Theorem

### How Much of the Standard-Model Finite Grading Is Forced by Hypercharge, and Why Exactly One Bit Is Not

**Leonardo Murillo Montero**

*Draft v2 — restructured from the v1 agent-handoff draft. This version supersedes all "chirality is derived" language in Papers 14–16 and states the result in its mature form: the internal CRT/Fisher data forces the gauge skeleton, rigidifies the representation package, and compresses the finite chirality input to a single external $\mathbb{Z}_2$ — and the irreducibility of that one bit is **protected by color**, not accidental.*

---

## Abstract

We delimit, sharply and by explicit computation, the boundary between what a CRT Fisher/Bures gauge-completion framework determines internally about Standard-Model finite chirality and what it must receive from outside. Three facts are established. (i) The internally derived block hypercharge $Y=\tfrac12 P_2-\tfrac13 P_3$ resolves the anomaly-selected exterior package $\Lambda^2E\oplus E^\ast$ ($E=\mathbb{C}^2\oplus\mathbb{C}^3$) into five pairwise-inequivalent irreducible gauge modules; the linear gauge commutant is exactly $\mathbb{C}^5$, so the finite charge-conjugation structure is rigid up to gauge-trivial phases, and the conductor grading contributes nothing to this rigidity because it is strictly coarser than $Y$. (ii) The native real-cone conjugation has the commuting KO sign $J_{\mathrm{cone}}\Gamma=+\Gamma J_{\mathrm{cone}}$ for every real/permutation grading the program produces, so a Standard-Model finite chirality cannot be generated internally — this is a no-go, not a missing lemma. (iii) The same derived $Y$, gauge invariance, and a single Higgs slot force the one-Higgs Yukawa graph to have exactly the three edges $Q\!-\!u^c$, $Q\!-\!d^c$, $L\!-\!e^c$; requiring the finite Dirac operator to be odd fixes the grading **within** each connected component.

The contribution beyond the boundary statement is two theorems the v1 draft asserted but did not prove. First, an **Identification Theorem**: under the Connes product-triple structure, the residual freedom is locked to the single spacetime chirality operator $\gamma^5$, so the leftover bit is not an arbitrary convention but is exactly the one Lorentz datum no internal gauge structure can supply. Second, a **Color-Protection Theorem**: the quark and lepton Yukawa subgraphs are disconnected *because every cross-sector trilinear is forbidden by $SU(3)$ color for any color-singlet scalar*, and this disconnection is robust to adding a sterile neutrino with Dirac and Majorana couplings. The number of irreducible external chirality bits is therefore $2^{c-1}$ where $c$ is the number of color-protected Yukawa components; for the Standard-Model matter content $c=2$ and the count is exactly one. The Standard Model's external chirality input is one bit, and its irreducibility is a consequence of color confinement of the coupling structure.

We do not claim a derivation of the Standard Model. We claim a precise localization theorem in the spirit of the Connes reconstruction program: a proof of exactly how little must be postulated once the gauge data are in hand, and a proof that this minimum cannot be reduced below one color-protected bit.

---

## 1. Introduction and relation to prior work

### 1.1 The claim, stated precisely

The slogan "the Standard Model from the categorical simplex" is false and should not appear in any paper of this program. The defensible statement is both weaker and, in one respect, stronger than that slogan, and it is the subject of this paper:

> The CRT Fisher/Bures framework derives a $2\,|\,3$ gauge and representation skeleton. The internally derived hypercharge $Y$ resolves the finite generation package into five multiplicity-free irreducibles and rigidifies the finite charge conjugation up to gauge-trivial phases. The native real-cone structure has the wrong KO sign for internal chirality. Nevertheless the derived $Y$, gauge invariance, and a single Higgs slot force the finite Yukawa graph; oddness of the finite Dirac operator then fixes the chirality grading internally up to one residual $\mathbb{Z}_2$ — the relative orientation between the quark and lepton Yukawa components — and that residual bit is (a) identifiable with the spacetime $\gamma^5$ and (b) irreducible because it is protected by $SU(3)$ color.

The result is a boundary theorem with a sharp lower bound on the external input:

```text
Internal CRT / Fisher data:
    derive gauge skeleton                    (Papers 14–15)
    derive hypercharge contrast Y            (Theorem 1)
    resolve irreducibles, rigidify J_F       (Theorem 1, Cor. 1)
    forbid internal chirality (KO sign)      (Theorem 2)
    fix the entire allowed Yukawa graph      (Theorem 3)
    force chirality WITHIN each component    (Theorem 4)

External Lorentz / Clifford data:
    supply exactly one Z2 bit:
    relative quark–lepton chirality          (Theorem 5: identification)

Lower bound:
    that one bit CANNOT be removed because the
    components are disconnected by color      (Theorem 6: color protection)
```

### 1.2 Position relative to Connes' reconstruction program

This paper is best read as a contribution to the question that the noncommutative-geometry Standard-Model program leaves explicitly open. In Connes' real spectral triple for the Standard Model, the finite real structure $J_F$ and the finite grading $\gamma_F$ are *postulated*, with the finite space taken at KO-dimension $6$ so that the total space (spacetime $\oplus$ finite, $4+6\equiv 2 \bmod 8$) admits the simultaneous chirality and reality conditions that resolve fermion doubling [Connes 2006; Chamseddine–Connes–Marcolli 2007; Barrett 2007]. The classification work of Chamseddine–Connes–van Suijlekom narrows the admissible finite algebras but still takes the order-one real structure as defining data, not as a theorem.

The honest novelty here is not "we derive what Connes postulates." It is a *localization*: given the gauge and hypercharge data — which this program derives by the $2\,|\,3$ split and the determinant-mismatch $U(1)$ — we prove **how much of $(J_F,\gamma_F)$ is forced and how little remains free**. The answer, "everything except one $\mathbb{Z}_2$ that is the spacetime $\gamma^5$ and is protected by color," is a precise statement of the irreducible external content of the Standard-Model finite geometry, phrased in information-geometric rather than spectral-triple language but compatible with the spectral-triple framing. The Color-Protection Theorem (§7) is, to our knowledge, a sharper statement of *why* this minimum cannot be reduced than appears in the reconstruction literature, where the disconnection of the Yukawa structure between quarks and leptons is used implicitly but not isolated as a color-enforced lower bound on external chirality input.

### 1.3 Standing hypotheses (not hidden)

Every result below is conditional on the following, which belong to the program's own commitments and are stated as explicit hypotheses rather than treated as neutral:

* **(H1)** The block space is $E=V\oplus W$, $V=\mathbb{C}^2$, $W=\mathbb{C}^3$, with the internally derived hypercharge $Y=\tfrac12P_V-\tfrac13P_W$ (Papers 14–15, handoff Theorem 8).
* **(H2)** The one-generation matter content is the anomaly-selected exterior package $H_{\mathrm{gen}}=\Lambda^2E\oplus E^\ast$ (handoff Theorem 16).
* **(H3)** The scalar (Higgs) slot is the primitive doublet $\Phi=V=(\mathbf 2,\mathbf 1)_{+1/2}$ or its conjugate; couplings are restricted to one Higgs insertion (renormalizable Yukawa level).
* **(H4)** For the Identification Theorem only: the physical theory is the Connes product of a four-dimensional spacetime triple with this finite triple, with total grading $\gamma=\gamma^5\otimes\gamma_F$ and total real structure $J=J_M\otimes J_F$.

Results under (H1)–(H3) are representation-theoretic and basis-free. The Identification Theorem additionally requires (H4); its status is therefore "forced given the spectral-triple framing," not "forced from the simplex alone." This distinction is maintained throughout.

---

## 2. Setup

Write $V=\mathbb{C}^2$, $W=\mathbb{C}^3$, $E=V\oplus W$, and let the block gauge group be

$$
G=S\big(U(2)\times U(3)\big)\;\cong\;\frac{U(1)\times SU(2)\times SU(3)}{\mathbb{Z}_6},
\qquad
Y=\tfrac12 P_V-\tfrac13 P_W .
$$

Then $V=(\mathbf 2,\mathbf 1)_{+1/2}$ and $W=(\mathbf 1,\mathbf 3)_{-1/3}$. Expanding the exterior package,

$$
\Lambda^2E=\Lambda^2V\;\oplus\;(V\otimes W)\;\oplus\;\Lambda^2W
=(\mathbf 1,\mathbf 1)_{+1}\oplus(\mathbf 2,\mathbf 3)_{+1/6}\oplus(\mathbf 1,\bar{\mathbf 3})_{-2/3},
$$
$$
E^\ast=V^\ast\oplus W^\ast=(\mathbf 2,\mathbf 1)_{-1/2}\oplus(\mathbf 1,\bar{\mathbf 3})_{+1/3},
$$

using $\mathbf 2^\ast\cong\mathbf 2$ for $SU(2)$. In left-handed Weyl notation the package is

$$
H_{\mathrm{gen}}=Q\oplus u^c\oplus e^c\oplus L\oplus d^c,
$$

with

$$
Q=(\mathbf 2,\mathbf 3)_{+1/6},\quad
u^c=(\mathbf 1,\bar{\mathbf 3})_{-2/3},\quad
e^c=(\mathbf 1,\mathbf 1)_{+1},\quad
L=(\mathbf 2,\mathbf 1)_{-1/2},\quad
d^c=(\mathbf 1,\bar{\mathbf 3})_{+1/3}.
$$

This is one Standard-Model-like generation.

---

## 3. Hypercharge rigidity

### Theorem 1 (Hypercharge resolves the package into five multiplicity-free irreducibles)

Under $G=S(U(2)\times U(3))$ the five sectors $Q,u^c,e^c,L,d^c$ are pairwise inequivalent irreducible $G$-modules. Consequently the linear gauge commutant is

$$
\operatorname{End}_G(H_{\mathrm{gen}})\cong\mathbb{C}^5 ,
$$

a five-dimensional algebra of independent scalars on the five sectors.

**Proof.** The triple $(SU(2),SU(3),Y)$ separates the sectors:

| Sector | $SU(2)$ | $SU(3)$ | $Y$ |
|---|---:|---:|---:|
| $Q$ | $\mathbf 2$ | $\mathbf 3$ | $+1/6$ |
| $u^c$ | $\mathbf 1$ | $\bar{\mathbf 3}$ | $-2/3$ |
| $e^c$ | $\mathbf 1$ | $\mathbf 1$ | $+1$ |
| $L$ | $\mathbf 2$ | $\mathbf 1$ | $-1/2$ |
| $d^c$ | $\mathbf 1$ | $\bar{\mathbf 3}$ | $+1/3$ |

The only pair sharing a semisimple type is $\{u^c,d^c\}$, both $(\mathbf 1,\bar{\mathbf 3})$ under $SU(2)\times SU(3)$. Hypercharge distinguishes them: $Y(u^c)=-2/3\neq+1/3=Y(d^c)$. Hence the $G$-representation is multiplicity-free, and by Schur's lemma the commutant of a multiplicity-free sum of five irreducibles is $\mathbb{C}^5$. $\square$

This is confirmed numerically: the nullspace of the simultaneous commutation conditions for the $su(2)\oplus su(3)\oplus u(1)$ generators acting on the explicit $15$-dimensional package has dimension exactly $5$ (Appendix A, `jf_moduli.py`).

### Corollary 1 (Hypercharge is load-bearing; the conductor grading is not)

Restricting to $SU(2)\times SU(3)$ only, $u^c\oplus d^c\cong(\mathbf 1,\bar{\mathbf 3})^{\oplus 2}$ has multiplicity two; the commutant acquires a full $M_2(\mathbb{C})$ on the $\{u^c,d^c\}$ multiplicity space, and the numerical commutant jumps from $5$ to $7$ (Appendix A). Imposing the CRT conductor-block projectors — in **either** the block ($\mathbb{C}^2\oplus\mathbb{C}^3$) or tensor ($\mathbb{C}^2\otimes\mathbb{C}^3$) embedding — leaves the dimension at $7$: the conductor grading removes none of the freedom that $Y$ removes.

**Interpretation.** The conductor grading is strictly coarser than $Y$: it resolves nonabelian sectors but is blind to the hypercharge values that separate $u^c$ from $d^c$. The rigidity of the finite charge conjugation is therefore due entirely to the internally derived $Y$, not to the conductor structure that an earlier line of the program hoped to leverage. This closes, in the negative, the question "does CRT conductor structure pin $J_F$?": there was nothing left for it to pin, and what does the pinning is the part of the program that is genuinely derived.

### Remark 1 (Linear commutant vs. antilinear charge conjugation)

$J_F$ is antilinear. The object that rigidifies is, strictly, the space of antilinear $G$-equivariant maps $H_{\mathrm{gen}}\to H_{\mathrm{gen}}$, equivalently $\operatorname{Hom}_G(H_{\mathrm{gen}},\overline{H_{\mathrm{gen}}})$. The exterior package is constructed to be closed under conjugation up to the chiral relabeling $\Lambda^2E\leftrightarrow(\Lambda^2E)^\ast$, $E^\ast\leftrightarrow E$, so each irreducible's conjugate sits in the package. Multiplicity-freeness of the linear $G$-action (Theorem 1) implies that any $G$-equivariant antilinear involution is determined sector-by-sector up to a phase, with sector-to-conjugate-sector assignment fixed by the (now nondegenerate) gauge labels. The linear commutant computation is thus the faithful shadow of the antilinear statement: $J_F$ is rigid up to the $U(1)^5$ of gauge-trivial phases. We flag this explicitly because a spectral-triple referee will, correctly, ask for the antilinear version; it follows from Theorem 1 without additional input.

---

## 4. The native real-cone sign no-go

### Theorem 2 (Native CRT real structure has the commuting KO sign)

Let $K$ be complex conjugation in the character/conductor basis and let $\Gamma$ be any grading represented in that basis by a real diagonal operator or a real permutation (parity-dual, conductor-even/odd, and exterior-volume candidates all fall in this class). Then

$$
K\Gamma=\Gamma K,\qquad\text{and for }J_{\mathrm{cone}}=\Gamma K,\quad
J_{\mathrm{cone}}\Gamma=\Gamma\Gamma K=\Gamma J_{\mathrm{cone}} .
$$

Hence every native real-cone/permutation construction gives $J_{\mathrm{cone}}\Gamma=+\Gamma J_{\mathrm{cone}}$, whereas a Standard-Model finite real structure requires the KO-dimension-$6$ sign $J_F\gamma_F=-\gamma_F J_F$.

**Proof.** A real matrix $M$ satisfies $KMK^{-1}=\overline{M}=M$, so $K$ commutes with any real $\Gamma$. The composite $J_{\mathrm{cone}}=\Gamma K$ then satisfies $J_{\mathrm{cone}}\Gamma=\Gamma K\Gamma=\Gamma\Gamma K$ and $\Gamma J_{\mathrm{cone}}=\Gamma\Gamma K$, equal. $\square$

**Status.** This is a no-go, not a deferred construction. It says the native structure *preserves* the grading rather than *exchanging* it, and an operator that preserves the grading cannot impose the charge-conjugation structure of a Standard-Model finite spectral triple. No real or permutation $\Gamma$ — and these exhaust the gradings the program produces internally — escapes it. Earlier program drafts that claimed chirality via exterior-Clifford or parity-dual gradings alone are corrected by this theorem and should be revised to cite it.

---

## 5. The Yukawa graph is forced

### Theorem 3 (The hypercharge-rigidified one-Higgs Yukawa graph has exactly three edges)

Under (H1)–(H3), the only gauge-invariant trilinears with two matter sectors and one Higgs insertion are

$$
Q\!\cdot\! u^c\!\cdot\!\Phi,\qquad Q\!\cdot\! d^c\!\cdot\!\Phi^\ast,\qquad L\!\cdot\! e^c\!\cdot\!\Phi^\ast .
$$

The Yukawa graph on vertices $\{Q,u^c,d^c,L,e^c\}$ has edges $Q\!-\!u^c$, $Q\!-\!d^c$, $L\!-\!e^c$ and nothing else.

**Proof.** Gauge invariance requires an $SU(3)$ singlet, an $SU(2)$ singlet, and $\sum Y=0$. The Higgs is colorless, so color invariance must come from the two matter factors; with at most two colored matter fields the only color singlets are $\{\mathbf 3,\bar{\mathbf 3}\}$ or all-colorless. Enumerating the unordered matter pairs with each of $\Phi,\Phi^\ast$ and applying the three conditions yields exactly the three listed trilinears; every other pair fails color (a lone $\mathbf 3$ or $\bar{\mathbf 3}$ survives) or $SU(2)$ (a lone doublet survives) or hypercharge. The full enumeration is mechanical and is reproduced verbatim by direct computation over all pairs and both Higgs insertions (Appendix A, `yukawa_graph.py`), which returns precisely these three edges. $\square$

The absences are the content: there is **no** $Q\!-\!L$, $u^c\!-\!d^c$, $Q\!-\!Q$, $L\!-\!L$, $u^c\!-\!e^c$, or $d^c\!-\!e^c$ edge. The graph is therefore a forest with two connected components,

$$
G_q=\{u^c,Q,d^c\}\ \ (\text{path }u^c\!-\!Q\!-\!d^c),\qquad
G_\ell=\{L,e^c\}\ \ (\text{single edge}).
$$

---

## 6. Internal chirality up to one bit

### Theorem 4 (Yukawa oddness fixes chirality within components; the residue is $\mathbb{Z}_2^{\,c-1}$)

Let $\gamma_F$ assign each sector a sign $\gamma_i\in\{\pm1\}$ and let $D_F$ have support exactly on the Yukawa edges. Then $D_F\gamma_F=-\gamma_F D_F$ iff adjacent vertices carry opposite signs, i.e. iff $\gamma_F$ is a proper $2$-colouring of the Yukawa graph. A graph with $c$ connected components has $2^{c}$ proper $2$-colourings; modulo the physically irrelevant global flip $\gamma_F\mapsto-\gamma_F$ there remain $2^{\,c-1}$ inequivalent gradings. For the Standard-Model graph $c=2$, so exactly **one** $\mathbb{Z}_2$ remains: the relative orientation between $G_q$ and $G_\ell$.

**Proof.** A matrix element of $D_F$ between sectors $i,j$ anticommutes with $\gamma_F$ iff $\gamma_i=-\gamma_j$. Since $D_F$ is supported on the edges, oddness is exactly proper $2$-colouring. Within a connected component a proper $2$-colouring is unique up to one global sign; independent components contribute independent signs, giving $2^c$ colourings and $2^{c-1}$ after the overall flip. With $c=2$ the count is $2^{1}=2$, a single bit. $\square$

The two inequivalent gradings are the Standard-Model orientation $H_+=Q\oplus L$, $H_-=u^c\oplus d^c\oplus e^c$ (weak doublets vs. singlets), and the alternative $\gamma_Q=+1,\gamma_L=-1,\gamma_{u^c}=\gamma_{d^c}=-1,\gamma_{e^c}=+1$. Both make $D_F$ odd; the Yukawa graph alone cannot reject the second.

---

## 7. The residual bit is identified, and it is irreducible

The v1 draft stopped at Theorem 4 and *asserted* (i) that the residual bit "is precisely $\gamma^5$" and (ii) that the disconnection is a structural feature. Both are theorems, and proving them is the substantive upgrade of this version.

### Theorem 5 (Identification: the residual bit is the spacetime $\gamma^5$)

Assume (H4): the physical theory is the Connes product of a $4$-dimensional spacetime triple with the finite triple, total grading $\gamma=\gamma^5\otimes\gamma_F$, total real structure $J=J_M\otimes J_F$, with finite space at KO-dimension $6$ so that the total KO-dimension is $4+6\equiv 2\bmod 8$ and the simultaneous chirality/reality projection (Connes' fermion-doubling resolution) is consistent. Then the residual $\mathbb{Z}_2$ of Theorem 4 is not a free convention: it is the choice of which finite Yukawa component is aligned with the $+1$ eigenspace of the **single** spacetime operator $\gamma^5$, and this choice is supplied by the spacetime Clifford structure, not by any internal gauge datum.

**Proof.** The physical one-particle space is the $+1$ eigenspace of the total grading under the reality projection. There $\gamma=\gamma^5\otimes\gamma_F=+1$ pairs $(\gamma^5{=}+1,\gamma_F{=}+1)$ with $(\gamma^5{=}-1,\gamma_F{=}-1)$: a finite sector with $\gamma_F=+1$ carries spacetime chirality $\gamma^5=+1$ and one with $\gamma_F=-1$ carries $\gamma^5=-1$. Crucially there is exactly one spacetime factor and hence one $\gamma^5$ common to every finite sector — quarks and leptons do not have independent spacetime chirality operators. Fix the overall sign of $\gamma_F$ on $G_q$ by convention. Theorem 4 leaves free precisely the overall sign of $\gamma_F$ on $G_\ell$. By the pairing above, that sign decides whether the lepton doublet $L$ carries the *same* spacetime chirality as the quark doublet $Q$ or the opposite, *relative to the one shared $\gamma^5$*. The Yukawa graph is silent on it because $G_q$ and $G_\ell$ are disconnected (Theorem 3); the only structure that fixes a uniform notion of "left-handed" across disconnected finite components is the single spacetime $\gamma^5$, which is external to the finite gauge data by Theorem 2. Hence the residual bit *is* the alignment of the finite grading with the spacetime $\gamma^5$. $\square$

So the leftover is not "an undetermined convention." It is the one Lorentz datum: the program cannot manufacture a global left/right orientation tying disconnected finite components together, because doing so is exactly what the single external $\gamma^5$ does and what Theorem 2 forbids internally. This is the precise, proved form of the v1 assertion.

### Theorem 6 (Color protection: the residual bit cannot be removed)

Under the Standard-Model gauge group with any **color-singlet** scalar sector and one-Higgs couplings, every trilinear connecting a quark-sector vertex $\{Q,u^c,d^c\}$ to a lepton-sector vertex $\{L,e^c\}$ is forbidden by $SU(3)$. Consequently the Yukawa graph has $c\ge 2$ disconnected color sectors, and the residual external chirality count $2^{\,c-1}\ge 2^{1}$ cannot be reduced to zero by any color-singlet Higgs content. The disconnection is moreover robust to a sterile neutrino: adding $\nu^c=(\mathbf 1,\mathbf 1)_0$ with the Dirac coupling $L\!\cdot\!\nu^c\!\cdot\!\Phi$ (and/or a Majorana $\nu^c\nu^c$ term) places $\nu^c$ inside the lepton component, leaving $c=2$.

**Proof.** A cross-sector edge requires a gauge-invariant trilinear with one factor from $\{Q,u^c,d^c\}$ (color $\mathbf 3$ or $\bar{\mathbf 3}$), one from $\{L,e^c\}$ (color $\mathbf 1$), and one colorless Higgs. The color content is then a single $\mathbf 3$ or $\bar{\mathbf 3}$ tensored with singlets, which contains no $SU(3)$ singlet; the trilinear cannot be gauge invariant. This holds for every quark/lepton pair and every color-singlet scalar (the six cases are checked exhaustively in Appendix A, `disconnection.py`, all returning "no color singlet"). Hence no color-singlet Higgs sector connects the two color sectors, $c\ge 2$, and $2^{c-1}\ge 2$. For the sterile neutrino: $\nu^c$ is colorless, so $L\!\cdot\!\nu^c\!\cdot\!\Phi$ is color-trivial and gauge-invariant, adding an edge $L\!-\!\nu^c$ interior to $G_\ell$; a Majorana $\nu^c\nu^c$ term is a self-loop on $\nu^c\in G_\ell$. Neither connects $G_q$ to $G_\ell$. The component count remains $c=2$ (Appendix A, "SM + nu_R" case). $\square$

**Interpretation — the conceptual climax.** The single external chirality bit is not an accident of the minimal matter content; it is *protected by color*. Quarks carry $SU(3)$ and leptons do not, so no color-singlet scalar can ever build a Yukawa bridge between them. The quark and lepton Yukawa worlds are confined into separate components by the same color symmetry that confines quarks themselves, and therefore the relative chirality orientation of the two worlds is structurally beyond the reach of any internal, color-singlet, Yukawa-level datum. To eliminate the bit one would need a colored scalar (a leptoquark) bridging the sectors — i.e. physics outside the Standard Model. Within the Standard Model the external chirality input is exactly one bit, and it is one bit *because of color*.

---

## 8. The Chirality Boundary Theorem

### Main Theorem

Under (H1)–(H3), and (H4) for clause 7:

1. $Y$ resolves $H_{\mathrm{gen}}$ into five multiplicity-free irreducibles $Q,u^c,d^c,L,e^c$ (Thm 1).
2. The gauge commutant is $\mathbb{C}^5$; the finite charge conjugation is rigid up to gauge-trivial phases; the CRT conductor grading adds nothing to this rigidity (Thm 1, Cor 1).
3. The native real-cone structure has the commuting sign $J_{\mathrm{cone}}\Gamma=+\Gamma J_{\mathrm{cone}}$ and cannot supply SM finite chirality (Thm 2).
4. Derived $Y$ + gauge invariance + one Higgs slot force exactly the edges $Q\!-\!u^c$, $Q\!-\!d^c$, $L\!-\!e^c$ (Thm 3).
5. Oddness of $D_F$ forces the grading within each connected component (Thm 4).
6. Exactly one $\mathbb{Z}_2$ remains: the relative quark–lepton orientation (Thm 4, $c=2$).
7. That bit is the alignment of $\gamma_F$ with the single spacetime $\gamma^5$ — external by construction (Thm 5).
8. The bit is irreducible: the two components are disconnected by $SU(3)$ color for any color-singlet Higgs, robustly including a sterile neutrino (Thm 6).

Therefore: **the internal CRT/Fisher data compress the Standard-Model finite chirality input to exactly one external $\mathbb{Z}_2$ bit, identify that bit with the spacetime $\gamma^5$, and prove the bit irreducible because it is protected by color. They do not eliminate the bit, and no color-singlet internal structure can.** $\square$

---

## 9. Why this is the mature form, and what it is not

The earlier honest claim, "chirality is external," was correct but coarse: it placed the entire finite grading outside. This theorem is sharper in both directions. Upward: all relative chirality signs along color-allowed Yukawa edges are forced internally; the external content is compressed from "a grading on a $15$-dimensional space" to "one bit." Downward: that one bit is shown irreducible — not merely "currently underived" but provably unremovable by any color-singlet internal datum, because color protects the disconnection. The result has the shape of a Connes-type reconstruction statement: a proof of exactly how little must be postulated and a proof that the minimum is a genuine floor.

What this is **not**, stated to forestall the predictable misreadings: it is not a derivation of the Standard Model; it is not a derivation of three generations, masses, the Higgs potential, Yukawa magnitudes, or electroweak symmetry breaking; the Identification Theorem is conditional on the spectral-triple product framing (H4), and is "forced given that framing," not "forced from the simplex." The Color-Protection Theorem is unconditional given (H1)–(H3) and the Standard-Model gauge group.

---

## 10. Scope and limitations

* **Conditional on the program's package.** (H1)–(H2) are inputs from Papers 14–15 (the $2\,|\,3$ split, the determinant-mismatch $Y$, the anomaly-selected $\Lambda^2E\oplus E^\ast$). This paper does not re-derive them; it takes them as the hypothesis and asks what they then force about chirality.
* **Higgs slot is an assumption.** (H3) fixes $\Phi=V$. A different scalar sector changes the Yukawa graph. The Color-Protection Theorem is robust across *all color-singlet* scalar choices, but a colored (leptoquark) scalar would change $c$ and is explicitly outside scope.
* **Renormalizable level.** Only one-Higgs trilinears are considered. Higher-dimension operators are not treated; they do not arise at the Yukawa level that defines $D_F$ in the spectral-triple correspondence.
* **Identification needs the product triple.** Theorem 5 requires (H4). Without the Connes product structure the residual bit is still well-defined and still irreducible by color (Theorems 4, 6), but its identification *with $\gamma^5$ specifically* is not available; one would only be able to say "an irreducible external $\mathbb{Z}_2$ remains."
* **No dynamical content.** Nothing here addresses masses, mixing, CP, or the number of generations. The family index is orthogonal to this theorem and is treated elsewhere; it is deliberately excluded here to keep the boundary statement clean.

---

## 11. Conclusion

The clean final line, and the strongest version that survives the computations:

> The CRT Fisher program derives the gauge skeleton and, via the internally derived hypercharge, every Yukawa-forced relative chirality sign. Exactly one global quark–lepton orientation bit remains external; it is the single spacetime $\gamma^5$; and it is irreducible because $SU(3)$ color forbids any color-singlet Yukawa bridge between the quark and lepton sectors. The Standard Model's external chirality input is one bit, and color is the reason it is exactly one.

---

## Appendix A — Reproducible computations

All claims marked "verified" are reproduced by three short scripts (developed alongside this paper; available with the artifact bundle). Each is a direct enumeration or nullspace computation, not a fit.

**A.1 `jf_moduli.py` — Theorem 1 and Corollary 1.** Builds the explicit $15$-dimensional package as a representation of $su(2)\oplus su(3)\oplus u(1)_Y$; computes the dimension of the simultaneous commutant by solving $\big(I\otimes X-X^{\mathsf T}\otimes I\big)\,\mathrm{vec}(T)=0$ over all generators. Output: gauge-only commutant dimension $=5$ (multiplicity-free, Thm 1). Removing $U(1)_Y$: dimension $=7$. Adding the CRT conductor projectors (block or tensor): dimension stays $7$ (Cor 1 — conductor grading contributes nothing). Robustness: artificially setting $Y(u^c)=Y(d^c)$ reproduces the jump to $7$, confirming $Y$ is the separating datum. *Independent reproduction note (Paper 32 §12 item U1FM, 2026-05-20).* `jf_moduli.py` was run end-to-end by the editing team and reproduced Theorem 1 / Corollary 1 exactly (the $5/7/7$ commutant pattern plus the robustness collapse to $7$); a parallel from-scratch reconstruction returned $5/5/5$ and the audit's own pre-claimed anchor-failure branch fired (the failure was traced to a block-separation modelling error in the *reconstruction*, not to this paper, whose own artifact is the authority and reproduces). The U1FM settlement uses the reproduced pattern to establish that the prime-reciprocal hypercharge $Y$ is a *distinct, internally-derived, physically-active fourth internal face* (Face D) of Paper 32's V′ recount — **not** the Paper 18 Proposition 5.1 trace mode.

**A.2 `yukawa_graph.py` — Theorem 3 and Theorem 4.** Enumerates every unordered matter pair against $\{\Phi,\Phi^\ast\}$ with explicit $SU(3)$-triality, $SU(2)$-isospin, and hypercharge tests. Output: exactly the three edges $Q\!-\!u^c$, $Q\!-\!d^c$, $L\!-\!e^c$; graph bipartite; two connected components $\{u^c,Q,d^c\}$ and $\{L,e^c\}$; proper $2$-colourings $=2^2$, inequivalent gradings $=2^{2-1}=2$ (one residual bit).

**A.3 `disconnection.py` — Theorem 6.** Tests every quark-sector/lepton-sector pair with a colorless Higgs for an $SU(3)$ singlet: all six return "no color singlet" (color protection). Recomputes components for SM-minimal ($c=2$) and SM $+\,\nu_R$ Dirac ($c=2$, the new edge $L\!-\!\nu^c$ interior to the lepton component), confirming robustness of the single residual bit.

---

## Appendix B — Theorem list

1. **Hypercharge-Rigidity Theorem** — $Y$ resolves $H_{\mathrm{gen}}$ into five multiplicity-free irreducibles; commutant $\mathbb{C}^5$; without $Y$, $u^c,d^c$ mix; conductor grading does not substitute.
2. **Native Real-Cone KO No-Go** — every real/permutation $\Gamma$ gives the commuting sign; SM finite chirality is not internal.
3. **Yukawa Edge Enumeration** — exactly $Qu^c\Phi$, $Qd^c\Phi^\ast$, $Le^c\Phi^\ast$.
4. **Yukawa Bipartition Compression** — oddness of $D_F$ fixes chirality within each component; residue $2^{c-1}$; $c=2\Rightarrow$ one bit.
5. **Identification Theorem** — under the Connes product triple, the residual bit is the single spacetime $\gamma^5$.
6. **Color-Protection Theorem** — the components are disconnected by $SU(3)$ for any color-singlet Higgs, robustly including a sterile neutrino; the one bit is irreducible.
7. **Chirality Boundary Theorem** — internal data compress the chirality input to one color-protected external bit and identify it; they cannot remove it.

---

*Draft v2. The substantive additions over v1 are Theorems 5 and 6 (proved, not asserted), the explicit Connes/Barrett/Chamseddine–van Suijlekom positioning, the antilinear refinement of the rigidity statement (Remark 1), and a disciplined Scope section. The agent-handoff scaffolding and the $\mathbb{Z}_{36}$ generation aside have been removed; the latter is a separate question and does not belong in the boundary theorem.*
