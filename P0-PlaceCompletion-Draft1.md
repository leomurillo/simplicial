# \heb[P]{פ}0 — From the Boundary: The Place-Completion of the Apex

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 30, 2026*

## Abstract

**Situation.** Six exterior papers read the categorical apex through its boundary, one local arithmetic at a time: the conductor packets and units (\heb[P]{פ}3, \heb[P]{פ}4), the Gauss sums at scale $\sqrt N$ (\heb[P]{פ}4), the radical–cyclotomic seam (\heb[P]{פ}5), the archimedean wall — the smooth primorial and its moment barrier (\heb[P]{פ}3, \heb[P]{פ}6). Each is a *local place* of $\mathbb Q$. In parallel, the interior's Paper 27 assembles a conditional Riemann-Hypothesis reduction on the primorial tower: a canonical involution implementing $s\leftrightarrow1-s$, recovery of the Weil explicit-formula prime sum (Thm 3.1, under hypotheses PC1–PC4), and an archimedean completion isolated in Axioms A1–A5.

**Gap.** The six papers study *discs* — one place, fixed $N$. Neither they nor Paper 27 assemble the **single object over all places** of which the local boundaries are the factors. That object is the adele $\mathbb A_{\mathbb Q}=\mathbb R\times{\prod'_p}\mathbb Q_p$, self-dual under Fourier, from which the completed $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and its functional equation descend (Tate). This keystone — written after \heb[P]{פ}1–\heb[P]{פ}6 as \heb{ל}0 was written after \heb{ל}1–\heb{ל}6 — assembles it.

**Action.** Under the grounded-paranoid-delusional method (Murillo Montero 2026): a fenced *Star* (\hyperref[sec:2]{§2}); four matched-pair falsifiers (\hyperref[sec:3]{§3}); one deterministic exact artifact (`P0-settlements.py`) catching the *unconditional* shadows of Paper 27's reduction (\hyperref[sec:4]{§4}). The classical global theorems (Tate, Weil) are **cited, not claimed**; RH is **named, not claimed**.

**Result.** The **Place-Completion Principle**: each local boundary of \heb[P]{פ}1–\heb[P]{פ}6 is the local factor of one self-dual adelic object, whose self-duality *is* the functional equation; the exterior $\partial$, globalized, is the diagonal $\mathbb Q\hookrightarrow\mathbb A$. Four exact catches anchor it. **\heb[P]{פ}0-involution ($\mathsf K$).** Paper 27's canonical involution $\iota$ (frequency reversal $a\mapsto-a$) is exactly $F^2$, the *square of the finite Fourier transform* ($F^4=I$); its $+1$-eigenspace — the finite critical-line sector — has dimension $\lfloor N/2\rfloor+1$. **\heb[P]{פ}0-rootnumber ($\mathsf K$, joint; naive falsified).** $\operatorname{tr}(F)=g/\sqrt N$ is the quadratic Gauss sum; for odd $N$, $|g|^2=N$ — \heb[P]{פ}4's $\sqrt N$ root-number scale — but the naive "always $\sqrt N$" is *false*: $g=0$ for $N\equiv2\ (4)$. **\heb[P]{פ}0-positivity ($\mathsf K$).** $F$ is unitary ($F^*F=I$ exactly), so the finite recovered energy is a norm, $\ge0$ for free; Paper 27's "joint" positivity (A5) sharpens to: RH is positivity *surviving the projective limit* once the archimedean $\Gamma$-kernel is adjoined — the kernel \heb[P]{פ}6 proved is not finitely generable. **\heb[P]{פ}0-functionfield ($\mathsf K$).** The Fermat cubic obeys $a^2\le4q$ (Weil) for all tested $q$: where there is no archimedean place, Paper 27's A1–A5 are all *theorems* and RH holds.

**Harvest.** The keystone gives the exterior series its completion as T0 gave the interior its coordinate: the local boundaries are one self-dual object; its functional equation is Tate's self-duality; and RH is the positivity of that object once the one archimedean term — the terminal boundary of \heb[P]{פ}3/\heb[P]{פ}6 — is adjoined. That the gap is *exactly* that one term is shown by \heb[P]{פ}0-functionfield: with $\infty$ removed, the whole reduction closes (Weil). The four catches and the function-field validation are $\mathsf{[P]}$; the place-dictionary is $\mathsf{[A]}$; RH, and Paper 27's hypotheses PC1–PC4 / Axioms A1–A5, stay $\mathsf{[C]}$ — named, built toward, not claimed.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
Six earlier papers each studied the prime numbers from one angle. This one shows the angles are views of a single object — the way local weather maps assemble into one planet. The object has a perfect mirror symmetry (a known classical theorem); a celebrated unsolved problem, the Riemann Hypothesis, asks whether its hidden resonances all sit on the mirror's axis. We make three things exact and one thing honest. Exact: the ``mirror'' operation is literally the square of a Fourier transform; the number that measures it is a classical Gauss sum; and the easy half of the hard problem (a positivity) is automatic. Honest: the entire difference between the solved cousin of the problem (over finite systems of arithmetic, settled by André Weil) and the open original is a single ingredient — the ``point at infinity'' — which an earlier paper proved cannot be built from the primes alone. We do not solve the problem; we locate it, precisely, on that one ingredient. Every number below is the printout of a short exact program.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| place $v$ | a prime $p$ (local field $\mathbb Q_p$) or $\infty$ (the field $\mathbb R$). |
| $\mathbb A$ | adele ring $\mathbb R\times{\prod'_p}\mathbb Q_p$; finite part $\varprojlim\mathbb Z/P_k=\hat{\mathbb Z}$. |
| $\mathbb Q\hookrightarrow\mathbb A$ | diagonal, discrete, self-annihilating ($\mathbb Q^\perp=\mathbb Q$) — the global $\partial$. |
| $\xi(s)$ | completed zeta $\pi^{-s/2}\Gamma(s/2)\zeta(s)$; $\xi(s)=\xi(1-s)$ (Tate). |
| $F$ | finite Fourier transform on $\mathbb Z/N$, $F_{jk}=\omega^{jk}/\sqrt N$, $\omega=e^{2\pi i/N}$. |
| $\iota$ | the canonical involution $s\leftrightarrow1-s$; finite form $x\mapsto-x$ $=F^2$ (Paper 27). |
| $g$ | quadratic Gauss sum $\sum_{k}\omega^{k^2}$; $\operatorname{tr}(F)=g/\sqrt N$. |
| $Z_v(s)$ | local Tate factor: $(1-p^{-s})^{-1}$ at $p$; $\pi^{-s/2}\Gamma(s/2)$ at $\infty$. |
| $a,\,q$ | Frobenius trace $a=q+1-\#C(\mathbb F_q)$ of the Fermat cubic; Weil $a^2\le4q$. |
| PC1–4, A1–5 | Paper 27's projective-closure hypotheses and Archimedean-limit axioms (conditional). |
| $\mathsf{[P]/[A]/[C]}$ | Tiers: proven / structural-pending-named-audit / conjectural-reduced. |
| $\mathsf K,\mathsf L$ | Matched-pair branches; *joint-on-disjoint* when both fire on disjoint sub-structures. |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| GPD | Grounded-paranoid-delusional (the method of Murillo Montero 2026). |
| (G)RH | (Generalized) Riemann Hypothesis. |
| adele / idele | $\mathbb A={\prod'_v}\mathbb Q_v$ and its units — the object holding all places at once. |
| Tate's thesis | the derivation of $\xi(s)=\xi(1-s)$ from adelic Fourier self-duality. |
| local factor | the per-place contribution $Z_v(s)$ to $\xi(s)=\prod_v Z_v$. |

---

## 1. The reflection is a Fourier square {#sec:1}

Begin where Euler would: with the smallest exact fact that already names the whole object.

The functional equation of the zeta function is a *reflection*, $s\leftrightarrow1-s$. Its finite avatar — the one the interior's Paper 27 builds, with some care, out of Bures geometry — is frequency reversal: send each character $\chi_a$ to $\chi_{-a}$, equivalently send a function on the $N$-hour clock to its mirror $x\mapsto-x$. Compute what operator that is. The finite Fourier transform $F$ has $(F^2)_{jl}=\frac1N\sum_k\omega^{k(j+l)}=[\,l\equiv-j\,]$ — i.e. $F^2$ *is* the mirror $x\mapsto-x$. So the reflection is nothing exotic: it is the **square of the Fourier transform**, an order-two element of the order-four cyclic group generated by $F$ ($F^4=I$). One line replaces a section of construction.

That is the key in miniature. The reflection that the Riemann Hypothesis lives under is the self-duality of the Fourier transform; globally, across all places of $\mathbb Q$, it is the self-duality of the adele ring, and the completed zeta function is the object it fixes. The six exterior papers each found one local face of that object — one place. This keystone, written after them as the interior's \heb{ל}0 was written after \heb{ל}1–\heb{ל}6, assembles the faces into the object, names the principle, and locates — precisely, and without claiming — where the Hypothesis sits.

### 1.1 Why a gate, and why exact {#sec:1-1}

A word on method, sharpened here because the destination is the most over-claimable in mathematics. We permit one unifying picture but give it no vote (\hyperref[sec:2]{§2}); we fix the meaning of every outcome before computing (\hyperref[sec:3]{§3}); we settle each question with one short exact-arithmetic program — decisions by orthogonality, bijection, and integer point-counting, floating point only as a labelled non-voting witness (\hyperref[sec:4]{§4}). Two classical global theorems are used and **cited, not reproved**: Tate's functional equation and Weil's bound for curves. The Riemann Hypothesis is **named and not claimed**, and Paper 27's enabling hypotheses (PC1–4) and axioms (A1–5) are carried at $\mathsf{[C]}$, never promoted. The keystone's whole contribution is the honest separation of what is assembled from what remains.

---

## 2. The Star (delusional; no vote on truth) {#sec:2}

> **Fence.** This section is *Historic Fiction*. It chooses what to attempt. It decides nothing. The road to a result runs through \hyperref[sec:3]{§3} and \hyperref[sec:4]{§4}.

Here is the picture. A number field has two kinds of place: the finite primes $p$ (local fields $\mathbb Q_p$) and the real place $\infty$ ($\mathbb R$). The adele $\mathbb A$ holds them all at once, as a restricted product; $\mathbb Q$ sits inside it diagonally as a *self-annihilating* discrete subgroup ($\mathbb Q^\perp=\mathbb Q$). The exterior boundary $\partial$ that the whole series chases is, at this altitude, that diagonal — the local–global boundary.

**The Place-Completion Principle (the fiction to chase).** Each local boundary of \heb[P]{פ}1–\heb[P]{פ}6 is the local factor of one global object:
$$
\begin{gathered}
\xi(s)=\prod_v Z_v(s),\\[2pt]
Z_p=(1-p^{-s})^{-1}\quad(\text{the packets/units of }\heb[P]{פ}3,\heb[P]{פ}4),\\[2pt]
Z_\infty=\pi^{-s/2}\Gamma(s/2)\quad(\text{the }\log2\pi\text{ of }\heb[P]{פ}6).
\end{gathered}
$$
The single Mellin variable that T0/T23 already isolated as "dual to global scale, shared by all CRT factors, split by none" is the **idele-norm exponent $s$**; T0 chose a section of it (the gauge $\beta$), and this keystone completes it globally. The object is **self-dual**: $\mathbb A$ is its own Fourier dual, the standard test state is its own transform, and the completed $\xi$ is *fixed under the reflection* $s\leftrightarrow1-s$. That self-duality, integrated against the idele norm (Tate), **is** the functional equation. Its zeros are a discrete spectrum, symmetric about the axis $\operatorname{Re}(s)=\tfrac12$ — the fixed locus of the reflection. The fiction: the Hypothesis is the statement that this spectrum is *real* — that the object is not merely symmetric but self-adjoint, every resonance on the axis.

If true: the six local boundaries are one self-dual whole; its functional equation is the self-duality made an identity (Tate, classical); and RH is the positivity of that whole once the one archimedean factor is folded in. The paper does not argue this. It catches four exact, unconditional shadows of it and reports the arithmetic.

---

\clearpage

## 3. Pre-registration (paranoid; meanings fixed before the check) {#sec:3}

| Audit | Claim under test | $\mathsf K$ | $\mathsf L$ | Joint-on-disjoint |
|---|---|---|---|---|
| **\heb[P]{פ}0-involution** | The reflection $\iota$ is the Fourier square. | $F^2=$ parity $x\mapsto-x=\iota$ (orthogonality), $F^4=I$; $+1$-eigenspace dim $=\lfloor N/2\rfloor+1$. | $\iota\ne F^2$ / needs the Bures construction. | — |
| **\heb[P]{פ}0-rootnumber** | $\operatorname{tr}(F)$ is the Gauss sum $=$ \heb[P]{פ}4's scale. | odd $N$: $\lvert g\rvert^2=N$ (bijection) $\Rightarrow\lvert\operatorname{tr}F\rvert=1$, the $\sqrt N$ scale. | naive: $\lvert g\rvert^2=N$ for *all* $N$. | mod-4 trichotomy; naive $\mathsf L$ falsified ($g=0$ at $N\equiv2$). |
| **\heb[P]{פ}0-positivity** | Finite positivity is free; RH $=$ limit-positivity. | $F^*F=I$ exact $\Rightarrow$ finite energy $\ge0$ automatically. | finite Gram not PSD. | RH $=$ positivity surviving the limit $+$ the archimedean term. |
| **\heb[P]{פ}0-functionfield** | With $\infty$ absent, A1–A5 are theorems. | Fermat cubic $a^2\le4q$ (Weil) for all $q$; $\iota=T\mapsto1/(qT)$; A2 empty. | $a^2>4q$ some $q$ (impossible). | — |

We run the artifact.

---

## 4. Settlement (grounded; the transcript is the record) {#sec:4}

### 4.1 \heb[P]{פ}0-involution — the reflection is $F^2$ {#sec:4-1}

The finite avatar of $s\leftrightarrow1-s$ is the mirror $x\mapsto-x$ on $\mathbb Z/N$.

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (the involution is the Fourier square).** *On $\mathbb Z/N$, $F^2$ is the parity permutation $x\mapsto-x$, hence $F^2=\iota$ and $F^4=I$. The $+1$-eigenspace of $\iota$ — the reflection-symmetric (finite critical-line) sector — has dimension $\lfloor N/2\rfloor+1$.*

*Proof.* $(F^2)_{jl}=\frac1N\sum_{k}\omega^{k(j+l)}=[\,l\equiv-j\,]$ by the orthogonality $\sum_k\omega^{kt}=N\,[t\equiv0]$ (the artifact verifies this integer relation exactly for every $t$). Thus $F^2$ permutes $|x\rangle\mapsto|-x\rangle=\iota$, and $F^4=\iota^2=I$. The $+1$-eigenspace consists of even functions $f(x)=f(-x)$, of dimension equal to the number of orbits of $x\mapsto-x$, namely $\lfloor N/2\rfloor+1$. $\square$

**Settlement \heb[P]{פ}0-involution — $\mathsf K$, $\mathsf{[P]}$.** Exact at $N=6,12,30$ (orthogonality holds; dims $4,7,16=\lfloor N/2\rfloor+1$; witnesses $\|F^2-\text{parity}\|,\|F^4-I\|\sim10^{-15}$). Paper 27 builds $\iota$ from Bures geometry and verifies four properties; the exterior reading collapses that to one identity — **the canonical involution is the square of the Fourier transform**, unconditionally. The reflection that RH lives under is Fourier self-duality, finitely.

### 4.2 \heb[P]{פ}0-rootnumber — the Fourier trace is the Gauss sum {#sec:4-2}

The operator whose square is the reflection carries, in its trace, the program's $\sqrt N$ scale.

\hypertarget{stmt:4-2}{}
**Proposition 4.2 (trace $=$ Gauss sum; the odd-conductor scale).** *$\operatorname{tr}(F)=\frac1{\sqrt N}\sum_k\omega^{k^2}=g/\sqrt N$. For odd $N$, $\lvert g\rvert^2=N$, so $\lvert\operatorname{tr}F\rvert=1$ — the $\sqrt N$ scale of \heb[P]{פ}4's Gauss sums, the local root number. The naive extension "$\lvert g\rvert^2=N$ for all $N$" is false: $g=0$ for $N\equiv2\ (\mathrm{mod}\ 4)$ (Gauss's evaluation).*

*Proof.* $\operatorname{tr}(F)=\sum_k F_{kk}=\frac1{\sqrt N}\sum_k\omega^{k^2}$ by definition. For odd $N$, $2$ is invertible, so $(k,m)\mapsto(k-m,k+m)$ is a bijection of $(\mathbb Z/N)^2$ (verified exactly: the image has $N^2$ elements); since $k^2-m^2=(k-m)(k+m)$, $\lvert g\rvert^2=\sum_{k,m}\omega^{k^2-m^2}=\sum_{a,b}\omega^{ab}=\sum_a N\,[a\equiv0]=N$. For $N=2M$ with $M$ odd, $(k+M)^2\equiv k^2+M\ (\mathrm{mod}\ N)$ (exact integer identity, verified) and $\omega^{M}=\omega^{N/2}=-1$, so $\omega^{k^2}+\omega^{(k+M)^2}=\omega^{k^2}(1-1)=0$, and pairing $k\leftrightarrow k+N/2$ gives $g=0$. $\square$

**Settlement \heb[P]{פ}0-rootnumber — $\mathsf K$ + joint-on-disjoint, naive $\mathsf L$ falsified, $\mathsf{[P]}$.** Odd $N=3,5,7,11,13$: bijection holds, $\lvert g\rvert^2=N$, the $\sqrt N$ scale of \heb[P]{פ}4. Even $N$: $g=0$ at $N\equiv2$ ($N=6,30$), $\lvert g\rvert^2=2N$ at $N\equiv0$ ($N=8,12$) — Gauss's mod-4 trichotomy, the honest refinement that kills the naive claim. The reflection operator's trace is exactly the Gauss sum the function-field side (\heb[P]{פ}4) found carrying the critical scale; here it is the local root number of the local functional equation.

### 4.3 \heb[P]{פ}0-positivity — the finite half is free {#sec:4-3}

Paper 27's A5 asks for *joint* positivity (finite closure and the archimedean involution together). One half is automatic.

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (finite positivity is unconditional).** *$F$ is unitary, $F^*F=I$ exactly (orthogonality), so every finite recovered energy is a squared norm and is $\ge0$ without hypothesis. Consequently the positivity of the limiting Weil form is not "joint": its finite part is free, and its entire content is whether positivity is preserved in the projective limit once the archimedean factor $1/\lvert\Gamma(\tfrac12+it)\rvert^2$ is adjoined.*

*Proof.* $(F^*F)_{jl}=\frac1N\sum_k\omega^{k(l-j)}=[\,l\equiv j\,]=\delta_{jl}$ (verified exactly). A Gram form $G^*G$ is positive semidefinite; the finite Noether/leakage energy of Paper 27 is of this type. $\square$

**Settlement \heb[P]{פ}0-positivity — $\mathsf K$, $\mathsf{[P]}$ finite / $\mathsf{[C]}$ limit.** $F^*F=I$ exactly at $N=12,30$; the finite Gram is the identity, eigenvalues all $1$. So RH is the positivity that must *survive the limit* — and the term whose adjunction is in question is exactly the archimedean $\Gamma$-factor that \heb[P]{פ}6 proved cannot be generated from the finite primes (the moment barrier). One honest caution, carried forward from \heb[P]{פ}6: this Weil-form positivity is *not* \heb[P]{פ}6's Hankel/moment positivity — they are cousins at the same place, not the same condition, and neither is claimed to settle RH.

**Settlement \heb[P]{פ}0-archimedean-operator — the missing factor exhibited, $\mathsf{[P]}$.** The archimedean $\Gamma$-factor that \heb[P]{פ}6 proves the finite primes cannot *generate* is realized, on the apex side, as a *scaling limit* of finite unitaries — precisely a completion, as a place at infinity should be. The apex unitary $U_N$ ([N1]–[N3]) has an edge operator $(A-I)\Phi$ (half-line Fourier transform dressed by the Hardy averaging operator) with Mellin symbol $\tfrac{s}{1-s}\,(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$, whose even sector equals the archimedean scattering operator $\gamma(s)R=\Gamma_{\mathbb R}(\tfrac12+it)/\Gamma_{\mathbb R}(\tfrac12-it)\cdot R$ exactly ([N4], certified to machine precision). This is complementary to the moment barrier, not in tension with it: the $\Gamma$-factor is the $N\to\infty$ limit of finite-prime apex data, not a finite combination of it. The apex's extra Hardy–Blaschke factor $s/(1-s)$ carries the pole at $s=1$ and trivial zero at $s=0$ of $\zeta$.

### 4.4 \heb[P]{פ}0-functionfield — the gap is exactly $\infty$ {#sec:4-4}

The cleanest evidence for where RH lives is the case where there is no archimedean place at all.

\hypertarget{stmt:4-4}{}
**Proposition 4.4 (with $\infty$ absent, the reduction closes).** *For the Fermat cubic $C:x^3+y^3+z^3=0$ over $\mathbb F_q$, the Frobenius trace $a=q+1-\#C(\mathbb F_q)$ satisfies $a^2\le4q$ (Weil), so $\lvert\alpha\rvert=\sqrt q$ and RH holds. In this setting Paper 27's Axioms become theorems: the involution is the Frobenius functional equation $T\mapsto1/(qT)$, the infinite-place packet (A2) is empty, and positivity (A5) is automatic.*

*Proof.* The point count is exact integer arithmetic; $a^2\le4q$ is Weil's theorem for the genus-one curve, verified by counting (the artifact confirms it for $q=5,\dots,43$, with the ordinary/supersingular split). With no place at $\infty$ there is no $\Gamma$-factor to adjoin; the explicit formula is purely finite (Plancherel), positive by \hyperref[sec:4-3]{§4.3}. $\square$

**Settlement \heb[P]{פ}0-functionfield — $\mathsf K$, $\mathsf{[P]}$.** $a^2\le4q$ holds for every tested $q$. The function-field case is Paper 27's roadmap *unconditionally completed* — A1–A5 all theorems, RH true — and it differs from the number field by exactly one term: the archimedean place, the terminal boundary of \heb[P]{פ}3/\heb[P]{פ}6. **\heb[P]{פ}4 is Paper 27 done, minus $\infty$.** This is the keystone's sharpest honest statement: the entire distance from proven RH to open RH is the single factor the program has independently proved is not finitely generable.

---

## 5. The synthesis (earned) {#sec:5}

\hypertarget{stmt:5-1}{}
**Proposition 5.1 (the Place-Completion Principle, at its tiers).** *The local boundaries of \heb[P]{פ}1–\heb[P]{פ}6 are the local factors $Z_v$ of the self-dual completed object $\xi=\prod_v Z_v$; its self-duality is the functional equation $\xi(s)=\xi(1-s)$ ($\mathsf{[P]}$, Tate); the reflection is the Fourier square (\hyperref[sec:4-1]{§4.1}, $\mathsf{[P]}$); its trace is the Gauss-sum root number (\hyperref[sec:4-2]{§4.2}, $\mathsf{[P]}$); the finite positivity is free (\hyperref[sec:4-3]{§4.3}, $\mathsf{[P]}$). That these factors assemble the program's apex into Tate's adelic object is the place-dictionary, $\mathsf{[A]}$. That the spectrum lies on the axis (RH) is $\mathsf{[C]}$, with the gap pinned to archimedean positivity (\hyperref[sec:4-3]{§4.3}) and validated, where $\infty$ is absent, by Weil (\hyperref[sec:4-4]{§4.4}).*

The keystone is to the exterior series what \heb{ל}0 is to the interior: \heb{ל}0 gave the local theory its *coordinate* (the gauge $\beta$); \heb[P]{פ}0 gives it its *completion* (the place-product and its self-duality). The relation to the interior's Paper 27 is exact and dual: Paper 27 is the conditional RH-reduction *from inside* (recovery maps, Bures involution, Axioms A1–A5); \heb[P]{פ}0 is its *boundary reading* — the same involution as a Fourier square, the same positivity with its finite half free, the same archimedean gap identified with \heb[P]{פ}6's barrier, and the same conclusion proven where there is no $\infty$. Two frames, one object; and the honest seam is that the object's mirror symmetry is classical while its self-adjointness is open.

---

## 6. The method's own record {#sec:6}

**6.1 Four confirmations, and why that is honest here.** All four audits returned $\mathsf K$. As a keystone assembling known local arithmetic into one object, that is expected: \hyperref[sec:4-1]{§4.1}–\hyperref[sec:4-3]{§4.3} re-derive exact, elementary facts (Fourier orthogonality, the Gauss-sum evaluation, unitarity) and \hyperref[sec:4-4]{§4.4} re-counts Weil's theorem — the new content is the *assembly* and the *identifications* (the dictionary, the $\iota=F^2$ collapse, the localization of the RH gap), not new theorems about $\zeta$. The genuine test content sat in the one place a guess could fail and did: \heb[P]{פ}0-rootnumber pre-registered the naive "$\lvert g\rvert^2=N$ always," and it was **falsified** ($g=0$ for $N\equiv2\ (4)$) — Gauss's trichotomy survives, the naive scale does not.

**6.2 What the keystone does NOT inherit.** Paper 27 is a genuine but *conditional* reduction (hypotheses PC1–PC4, axioms A1–A5, open Phases 1–4 including a primorial-moduli Bombieri–Vinogradov estimate). \heb[P]{פ}0 cites it as the interior twin and asserts only the *unconditional* catches at $\mathsf{[P]}$; PC1–4, A1–5, Phases 1–4, and RH remain $\mathsf{[C]}$. The keystone's value is precisely the separation — and the demonstration (\hyperref[sec:4-4]{§4.4}) that the lone obstruction is the archimedean place — not the roadmap.

---

## 7. Safe and unsafe statements {#sec:7}

**Safe (this paper asserts):**

- $\mathsf{[P]}$ The canonical involution is the Fourier square, $\iota=F^2$, $F^4=I$; the finite critical-line (reflection-symmetric) sector has dimension $\lfloor N/2\rfloor+1$ (\hyperlink{stmt:4-1}{Proposition~4.1}).
- $\mathsf{[P]}$ $\operatorname{tr}(F)=g/\sqrt N$; for odd $N$, $\lvert g\rvert^2=N$ — \heb[P]{פ}4's $\sqrt N$ root-number scale — and the naive all-$N$ version is *false* ($g=0$ at $N\equiv2$) (\hyperlink{stmt:4-2}{Proposition~4.2}).
- $\mathsf{[P]}$ Finite positivity is unconditional ($F^*F=I$); RH is positivity surviving the projective limit with the archimedean $\Gamma$-factor adjoined (\hyperlink{stmt:4-3}{Proposition~4.3}).
- $\mathsf{[P]}$ Where $\infty$ is absent (function field), $a^2\le4q$ (Weil): Paper 27's A1–A5 are theorems and RH holds (\hyperlink{stmt:4-4}{Proposition~4.4}).
- $\mathsf{[A]}$ The local boundaries of \heb[P]{פ}1–\heb[P]{פ}6 are the local factors of one self-dual adelic object (the Place-Completion Principle; \hyperlink{stmt:5-1}{Proposition~5.1}); the functional equation $\xi(s)=\xi(1-s)$ is its self-duality (Tate, cited).
- $\mathsf{[P]}$ On the Jensen/Pólya log-profile, the archimedean $\Gamma$-curvature is exact and sign-definite ($\Delta^kC_n=-\Delta^{k-1}\log(2n+1)$, sign $(-1)^{k+1}$) and the arithmetic moment-load is log-convex ($\Delta^2\log a_n\ge0$); the $d{=}2$ hyperbolicity rung is the exact Turán place-split $a_{n+2}a_n/a_{n+1}^2<\tfrac{2n+3}{2n+1}$ (\hyperlink{stmt:8-2}{Propositions~8.2}–\hyperlink{stmt:8-3}{8.3}).
- $\mathsf{[P]}$ The de Branges/Krein canonical system of the Hermite–Biehler associate $E_B=\Xi+i\Xi'$ is the rank-one projector $H(t)=P_{\varphi(t)}$ ($\succeq0$ automatically); RH $\iff$ the phase clock $\varphi'\ge0$, with closed form $\varphi'=(\Xi'^2-\Xi\Xi'')/(\Xi^2+\Xi'^2)$ ($=1$ at each zero), and $\varphi(T)/\pi=N(T)$ the integer zero-count (\hyperlink{stmt:8-5canon}{Proposition~8.5a}).
- $\mathsf{[P]}$ The clock decomposes exactly as $-\xi'/\xi=[\text{archimedean }\Gamma\text{-drift}]+[\sum_n\Lambda(n)n^{-s}]$ with $\Lambda\ge0$, converging for $\operatorname{Re}s>1$ (the easy half-plane) and continuing to the line (\hyperlink{stmt:8-6}{Proposition~8.6}); and the heat-smoothed clock is provably monotone for $t>\Lambda\ge0$ (Rodgers–Tao; \hyperlink{stmt:8-7}{Proposition~8.7}).

**Unsafe (this paper does NOT assert):**

- That RH is proved, or reduced to anything strictly easier. It is located on archimedean positivity (\hyperref[sec:4-3]{§4.3}); nothing here crosses that step.
- That Paper 27's PC1–PC4 or A1–A5 are theorems. They are carried at $\mathsf{[C]}$; only the unconditional shadows are claimed.
- That the function-field success (\hyperref[sec:4-4]{§4.4}) transports to $\mathbb Q$. It is precisely the place $\infty$ that does not, by \heb[P]{פ}6.
- That the Place-Completion Principle is a new theorem about $\zeta$. The global self-duality and functional equation are classical (Tate); the new content is the exterior assembly and the exact catches.
- That the place-decomposition (\hyperref[sec:8-2]{§8.2}) makes RH easier. Its uniform-in-degree domination $r_k(n)<1$ *is* RH; only the lowest rung (Turán) and the two place-factors are unconditional.
- That the operator form $H=N_\infty+V_{\text{arith}}$ (\hyperref[sec:8-3]{§8.3}) makes RH easier. The canonical-system positivity is free (rank-one) and the count is an integer, but **self-adjointness of $H$ — equivalently $\varphi'\ge0$ from the arithmetic, equivalently $\Lambda\le0$ — is RH itself**, not a reduction to anything strictly easier; nothing here crosses that step.
- That $H$ is constructed self-adjoint, or that the Kubo–Mori assembly is more than the identification of the correct additive geometry. The geometry is $\mathsf{[A]}$; the self-adjoint operator and the arithmetic clock stay $\mathsf{[C]}$ (\hyperlink{stmt:8-5}{Conjecture~8.5}).
- That this paper is important or field-defining. By the firewall such a claim would stand above its evidence, and the method forbids its author from issuing it.

---

## 8. Forward door: the one open step (calibrated, $\mathsf{[C]}$) {#sec:8}

The keystone reduces the program's distance to RH to a single, precisely-stated step. By \hyperref[sec:4-3]{§4.3} the finite half of the Weil positivity is free; by \hyperref[sec:4-1]{§4.1}–\hyperref[sec:4-2]{§4.2} the reflection and its root number are exact and classical; by \hyperref[sec:4-4]{§4.4} the whole reduction closes wherever the archimedean place is absent. What remains is one statement: **that positivity is preserved when the archimedean factor $1/\lvert\Gamma(\tfrac12+it)\rvert^2$ is adjoined in the projective limit** — the factor \heb[P]{פ}6 proved the finite primes cannot generate. In the spectral language toward which this points (Connes), that is the self-adjointness of the assembled object — the reality of its spectrum. We give that one step two readings: a spectral one (\hyperref[sec:8-1]{§8.1}), and a peaks-side *place-decomposition* (\hyperref[sec:8-2]{§8.2}) that writes the step as an explicit archimedean engine against an arithmetic load and makes its lowest rung a theorem.

### 8.1 The spectral form (Connes) {#sec:8-1}

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (the archimedean positivity step — calibrated, not proved).** *The completed self-dual object of \hyperlink{stmt:5-1}{Proposition~5.1} has its spectrum on the axis $\operatorname{Re}(s)=\tfrac12$ iff the limiting Weil quadratic form remains positive once the archimedean $\Gamma$-factor is adjoined; the finite part is unconditionally positive (\hyperref[sec:4-3]{§4.3}), and the function-field analogue (no $\infty$) is a theorem (\hyperref[sec:4-4]{§4.4}). The remaining step is the positivity of that one term.* Held with calibrated faith; built toward, not claimed.

### 8.2 The peaks-side place-decomposition of the archimedean step {#sec:8-2}

Pólya's criterion gives the same step a second, sharper face — one whose finite structure splits cleanly by place. Write $\Xi(t)=\xi(\tfrac12+it)=\int_0^\infty\Phi(u)\cos(ut)\,du$ with Pólya's kernel $\Phi>0$, and set $a_n=\int_0^\infty u^{2n}\Phi(u)\,du>0$, so $\Xi(t)=\sum_n\frac{(-1)^n a_n}{(2n)!}t^{2n}$. The Jensen polynomials $J^{d,n}(X)=\sum_{j=0}^d\binom{d}{j}b_{n+j}X^j$, with $b_n=a_n\,n!/(2n)!$, are hyperbolic (all roots real) for every $d,n$ **iff RH** ($\Xi$ in the Laguerre–Pólya class; Pólya). On the log-profile $L_n=\log b_n$ this hyperbolicity is governed, order by order, by the finite differences $\Delta^k L_n$ — and $L_n$ splits by place,
$$L_n=\log b_n=\underbrace{\log\tfrac{n!}{(2n)!}}_{C_n}\ +\ \underbrace{\log a_n}_{A_n},\qquad C_n=\log\Gamma(n{+}1)-\log\Gamma(2n{+}1).$$
Here $C_n$ is the **archimedean** part — the fingerprint of the $\Gamma$-factor of \hyperref[sec:4-3]{§4.3}, the place $\infty$ — and $A_n=\log a_n$ is the **arithmetic** part, carried by the moments of $\Phi$.

\hypertarget{stmt:8-2}{}
**Proposition 8.2 (the archimedean engine is exact and sign-definite — $\mathsf{[P]}$).** *For all $k\ge1$, $\Delta^kC_n=-\Delta^{k-1}\log(2n+1)$; explicitly $\Delta^1C_n=-\log(4n+2)$, $\Delta^2C_n=\log\frac{2n+1}{2n+3}<0$, $\Delta^3C_n=\log\frac{(2n+3)^2}{(2n+1)(2n+5)}>0$, and in general $\operatorname{sign}\Delta^kC_n=(-1)^{k+1}$ with $\lvert\Delta^kC_n\rvert\sim(k-2)!\,/\,n^{k-1}$ for $k\ge2$. This is the Hermite/oscillator (Bargmann–Fock) curvature — the metaplectic factor at $\infty$ — written elementarily and independent of any arithmetic.*

*Proof.* $\Delta C_n=\log\frac{(n+1)!/(2n+2)!}{n!/(2n)!}=\log\frac{1}{2(2n+1)}=-\log(4n+2)$; the constant $\log 2$ is annihilated by any further difference, so $\Delta^kC_n=-\Delta^{k-1}\log(2n+1)$ for $k\ge1$. As $\log(2n+1)$ is increasing and concave with $\operatorname{sign}\Delta^m\log(2n+1)=(-1)^{m+1}$, $\Delta^kC_n$ has sign $-(-1)^{(k-1)+1}=(-1)^{k+1}$; the magnitude follows from $\psi^{(k-1)}(x)\sim(-1)^k(k-2)!/x^{k-1}$. The closed forms are verified to $10^{-59}$ against the differences (companion artifact). $\square$

\hypertarget{stmt:8-3}{}
**Proposition 8.3 (the arithmetic load is log-convex; the $k{=}2$ rung is Turán, place-split — $\mathsf{[P]}$ / cited).** *$A_n=\log a_n$ is convex, $\Delta^2 A_n\ge0$: since $a_n=\int_0^\infty s^n\,d\nu(s)$ with $d\nu(s)=\Phi(\sqrt s)\,ds/(2\sqrt s)\ge0$, Cauchy–Schwarz gives $a_{n+1}^2\le a_n a_{n+2}$. The arithmetic curvature thus OPPOSES the archimedean ($\operatorname{sign}\Delta^kA_n=(-1)^k$, opposite to Proposition 8.2). The lowest hyperbolicity rung is the exact place-split*
$$\Delta^2L_n<0\ \ (\text{Tur\'an})\ \iff\ \frac{a_{n+2}\,a_n}{a_{n+1}^2}\ <\ \frac{2n+3}{2n+1},$$
*the arithmetic log-convexity (left side $\ge1$) beaten by the archimedean ratio (right side $>1$). For $\Xi$ this holds (Csordas–Norfolk–Varga); both sides $\to1$, so the margin $\to0$ — the marginality of RH, place-resolved.*

*Proof.* The moment representation and Cauchy–Schwarz give $\Delta^2 A_n=\log\frac{a_{n+2}a_n}{a_{n+1}^2}\ge0$. By \hyperlink{stmt:8-2}{Proposition~8.2}, $\Delta^2C_n=\log\frac{2n+1}{2n+3}$, so $\Delta^2L_n<0\iff\Delta^2A_n<-\Delta^2C_n=\log\frac{2n+3}{2n+1}$, which is the displayed inequality. That it holds for $\Xi$ is the Turán inequality (Csordas–Norfolk–Varga). $\square$

The cancellation hyperbolicity needs at *every* order is now named. Because the two curvatures oppose, the net difference $\Delta^kL_n$ keeps the oscillator sign $(-1)^{k+1}$ exactly when the **domination ratio** $r_k(n)=\lvert\Delta^kA_n\rvert/\lvert\Delta^kC_n\rvert<1$ — the explicit archimedean $\Gamma$-curvature outweighing the arithmetic moment-convexity at order $k$. Numerically $r_k(n)<1$ throughout the tested range, but $r_k(n)\nearrow1$ as $k$ grows at fixed $n$ (and $\searrow$ as $n$ grows): the domination margin closes at higher degree. This is, place-resolved, why hyperbolicity is a theorem only up to a finite degree — Griffin–Ono–Rolen–Zagier prove $J^{d,n}\to H_d$ (Hermite) for every $d$ and hyperbolicity for all $n$ at $d\le8$ — past which the shrinking oscillator gap ($\sim1/d$, the $\Delta^kC_n\sim(k-2)!/n^{k-1}$ of \hyperlink{stmt:8-2}{Proposition~8.2}) no longer dominates by size, and only the arithmetic *structure* can carry the matching.

\hypertarget{stmt:8-4}{}
**Conjecture 8.4 (the archimedean step, place-decomposed — calibrated, not proved).** *RH ($\Xi$ in Laguerre–Pólya; all $J^{d,n}$ hyperbolic) is, on the log-profile $L_n=C_n+A_n$, the uniform domination of the arithmetic moment-convexity by the explicit archimedean $\Gamma$-curvature: at $k=2$ the theorem of \hyperlink{stmt:8-3}{Proposition~8.3}, and at every higher order the surviving sign-domination $r_k(n)<1$, uniformly in $k$ and $n$. The archimedean engine (\hyperlink{stmt:8-2}{Proposition~8.2}) and the log-convex arithmetic load (\hyperlink{stmt:8-3}{Proposition~8.3}) are unconditional; the uniform-in-degree domination is the open content — and it is RH itself, not a reduction to anything easier.* Held with calibrated faith; built toward, not claimed.

**Settlement note ($\mathsf{[C]}$ forward-door).** \hyperlink{stmt:8-2}{Propositions~8.2}–\hyperlink{stmt:8-3}{8.3} are $\mathsf{[P]}$ (elementary identities; Cauchy–Schwarz; closed forms checked to $10^{-59}$); the $k{=}2$ inequality for $\Xi$ is Csordas–Norfolk–Varga (cited). The higher $r_k<1$ are the place-separated *controlling quantities*, **not** asserted term-by-term equivalent to hyperbolicity (a whole-polynomial condition) — their uniform control is RH. The reading sharpens \hyperref[sec:4-3]{§4.3} (the finite half is free) and \hyperref[sec:4-4]{§4.4} (no $\infty$, no obstruction): the lone obstruction — the archimedean factor of \heb[P]{פ}6's moment barrier — is here written as an explicit $\Gamma$-curvature, and the open step as a single uniform inequality against it. Companion numerical verification: `empirical/verify_cancellation_place_decomposition.py`.

### 8.3 The operator form: $H=N_\infty+V_{\text{arith}}$ and the monotone phase clock {#sec:8-3}

\hyperref[sec:8-1]{§8.1} read the one open step spectrally (Connes); \hyperref[sec:8-2]{§8.2} read it on the Jensen log-profile (Pólya). A third reading writes the step as an *operator* and reduces it to the monotonicity of a single explicit phase — the form toward which the Hilbert–Pólya tradition points. We give the operator, make the de Branges/Krein canonical system it generates fully explicit, and locate the open step as one local inequality. The discipline of \hyperref[sec:7]{§7} is in force throughout: **the operator form does not make RH easier**; in it, self-adjointness *is* RH (\hyperlink{stmt:8-5}{Conjecture~8.5}).

**The operator.** On the Mellin Hilbert space $L^2(\mathbb R_+,dx/x)\cong L^2(\mathbb R,ds)$ — the same line the interior's KU-3 carrier sat on, here scalar — set
$$
H \;=\; N_\infty \;+\; V_{\text{arith}},\qquad
V_{\text{arith}} \;=\; m_B \;=\; -\,\frac{\Xi'}{\Xi},\qquad \Xi(t):=\xi(\tfrac12+it).
$$
Here $N_\infty=\hat a^\dagger\hat a=z\partial_z$ is the archimedean (Bargmann–Fock) number operator forced by Uniform Place Treatment at $v=\infty$: under UPT-structure $+$ UPT-Heisenberg, Stone–von Neumann selects the Bargmann–Fock completion, $N_\infty$ has spectrum $\mathbb N$ with ground state $\psi_0\propto e^{-\pi x^2}$ (Tate–Weil $\hbar=1/2\pi$), and the Tate local zeta integral of that ground state is exactly the archimedean factor
$$
\int_{\mathbb R}\psi_0(x)\,|x|^{s-1}\,dx \;=\; \pi^{-s/2}\Gamma(s/2)\;=\;Z_\infty(s)
$$
(the metaplectic Archimedean-selection companion Note, Thm 8.1, parts 1–4). So $N_\infty$ *is* the place-$\infty$ factor of \hyperref[sec:4-3]{§4.3}/\hyperref[sec:8-2]{§8.2} read as a self-adjoint generator, and its ground-state Tate integral reproduces the luminous $\Gamma$-factor of \hyperlink{stmt:5-1}{Proposition~5.1}. The arithmetic part $V_{\text{arith}}=m_B=-\Xi'/\Xi$ is the additive (log-derivative) object carrying the zeros. Formally the operator's spectral determinant is the completed object of \hyperref[sec:5]{§5},
$$
\det(H-t)\;\sim\;\Xi(t)\;=\;\xi(\tfrac12+it)\;=\;\prod_v Z_v(\tfrac12+it),
$$
tying \hyperref[sec:8-3]{§8.3} back to the place-product of \hyperref[sec:5]{§5}/\hyperref[sec:4-3]{§4.3}: the archimedean factor $Z_\infty$ from the $N_\infty$ ground state, the finite factors $Z_p$ from the prime content of $m_B$ (the von Mangoldt sum, below). This $H$ is a candidate, not a theorem; what *is* exact is the canonical system it generates and the clock that reads it.

**The de Branges/Krein associate.** The correct Hermite–Biehler associate of $\Xi$ is the derivative-polarized entire function
$$
E_B(z)\;=\;\Xi(z)+i\,\Xi'(z),\qquad
|E_B|^2-|E_B^\#|^2 \;=\; 4\,|\Xi|^2\,\operatorname{Im}m_B,
$$
so that $E_B$ is Hermite–Biehler $\iff m_B$ Herglotz on $\mathbb C_+$ $\iff$ RH (a known de Branges/Laguerre–Pólya equivalence; here read in the program's coordinates). The first proposition makes its canonical system explicit and shows the de Branges positivity is *free*, exactly as the finite positivity of \hyperref[sec:4-3]{§4.3} is free.

\hypertarget{stmt:8-5canon}{}
**Proposition 8.5a (the canonical system is a rank-one projector; positivity is free — $\mathsf{[P]}$).** *The de Branges/Krein canonical system $J\,\frac{dM}{dt}=z\,H(t)\,M$, $J=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, for the Hermite–Biehler associate $E_B=\Xi+i\Xi'$ is, in its phase parametrization, the rank-one projector*
$$
H(t)\;=\;\begin{pmatrix}\cos^2\varphi & \sin\varphi\cos\varphi\\[2pt]\sin\varphi\cos\varphi & \sin^2\varphi\end{pmatrix}\;=\;P_{\varphi(t)},
\qquad \varphi(x)=-\arg E_B(x)=-\operatorname{atan2}\bigl(\Xi'(x),\Xi(x)\bigr),
$$
*with clock $dt=\varphi'(x)\,dx$. Since $H(t)=P_{\varphi(t)}$ has eigenvalues $\{0,1\}$, it is $\succeq0$ automatically: the de Branges positivity carries no content. The entire content of "$H(t)\succeq0$ independent of RH" is therefore the single local inequality*
$$
\varphi'(x)\;\ge\;0\quad(\text{the phase clock is monotone})\qquad\Longleftrightarrow\qquad \mathrm{RH},
$$
*with the closed form*
$$
\varphi'(x)\;=\;\frac{\Xi'(x)^2-\Xi(x)\,\Xi''(x)}{\Xi(x)^2+\Xi'(x)^2}\qquad(=1\ \text{exactly at each zero of }\Xi).
$$
*Moreover the clock counts: $\varphi(T)/\pi=N(T)$, the integer number of zeros up to $T$.*

*Proof.* In the phase parametrization of a Hermite–Biehler $E$-function the trace-normalized Hamiltonian of its canonical system is the orthogonal projector onto the phase direction $(\cos\varphi,\sin\varphi)$, $\varphi=-\arg E_B$ the increasing de Branges phase; this is the standard rank-one normalization (Krein; de Branges 1968). Its eigenvalues are $\{0,1\}$, so $H(t)\succeq0$ identically. Writing $\varphi=-\arg(\Xi+i\Xi')=-\operatorname{atan2}(\Xi',\Xi)$ and differentiating, $\varphi'=(\Xi'^2-\Xi\Xi'')/(\Xi^2+\Xi'^2)$; at a zero $\Xi(\gamma)=0$ this is $\Xi'^2/\Xi'^2=1$. The de Branges chain has real spectrum (equivalently $\Xi$ in the Laguerre–Pólya class) iff the clock $dt=\varphi'\,dx$ is a non-negative reparametrization, i.e. $\varphi'\ge0$; that is RH. Finally the increasing phase gains exactly $\pi$ as $x$ crosses each real zero, so $\varphi(T)/\pi$ equals the number of zeros up to $T$ — an integer. $\square$

**Settlement (front (a)/(b), $\mathsf{[P]}$ structure / $\mathsf{[C]}$ clock).** The canonical system is explicit and its positivity is free (rank-one), the exact spectral analogue of the unconditional finite positivity of \hyperref[sec:4-3]{§4.3}: there as $F^*F=I$, here as $\operatorname{eig}P_\varphi=\{0,1\}$. The two fronts of the program's strategy meet in the one clock $\varphi'$: it is a functional of the *additive* log-derivative $m_B=-\Xi'/\Xi$ (front (a)), and $\varphi(T)/\pi=N(T)$ is the *integer* count (front (b)). Numerically (companion `empirical/verify_canonical_system_phase.py`) $\varphi'\ge0$ at every tested $x$ with $\varphi'\to1$ at $\gamma_1,\gamma_2$, and the sign-changes of $\Xi$ match $N(T)=1,3,6,10$ at $T=20,30,40,50$. The open step is the *arithmetic* construction of $\varphi'\ge0$ — addressed next.

\hypertarget{stmt:8-6}{}
**Proposition 8.6 (the clock's explicit-formula decomposition; arithmetic non-negative, off-line — $\mathsf{[P]}$).** *The clock's log-derivative $m=-\xi'/\xi$ decomposes exactly, for $\operatorname{Re}s>1$, into an archimedean drift and a prime sum:*
$$
-\frac{\xi'}{\xi}(s)\;=\;\underbrace{\Bigl(-\tfrac1s-\tfrac1{s-1}+\tfrac12\log\pi-\tfrac12\psi(\tfrac s2)\Bigr)}_{\text{archimedean }\Gamma\text{-drift}}\;+\;\underbrace{\sum_{n\ge1}\Lambda(n)\,n^{-s}}_{\text{arithmetic, }=-\zeta'/\zeta}\,,\qquad \Lambda(n)\ge0.
$$
*The prime sum converges for $\operatorname{Re}s>1$ and gives the easy half-plane there; on $s=\tfrac12+iz$ it is the von Mangoldt sum $\sum_n\Lambda(n)n^{-1/2-iz}$ — the multiplicative basis carrying the zeros — and continues to the line, where the continuation has poles exactly at the zeros (residue $=$ multiplicity).*

*Proof.* Logarithmic differentiation of $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ gives the displayed split: $-1/s-1/(s-1)$ from the factor $s(s-1)$, $\tfrac12\log\pi-\tfrac12\psi(s/2)$ from $\pi^{-s/2}\Gamma(s/2)$, and $-\zeta'/\zeta=\sum_n\Lambda(n)n^{-s}$ (Euler product, $\operatorname{Re}s>1$) from $\zeta$. Non-negativity $\Lambda(n)\ge0$ is the definition of the von Mangoldt function. Convergence of the Dirichlet series for $\operatorname{Re}s>1$ and meromorphic continuation with poles at the nontrivial zeros are classical. The identity is verified to $6.5\times10^{-27}$ at $s=2$ in the companion `empirical/verify_arithmetic_clock.py`. $\square$

**Settlement ($\mathsf{[P]}$ identity / $\mathsf{[C]}$ strip-crossing).** This writes $V_{\text{arith}}=m_B$ as archimedean $\Gamma$-drift plus a non-negative prime sum, the operator-level shadow of the place-product $\det(H-t)\sim\prod_vZ_v$: the drift is the $N_\infty$/$Z_\infty$ part, the $\Lambda$-sum the $Z_p$ part. The prime positivity $\Lambda\ge0$ delivers $\operatorname{Re}s>1$ for free (as \hyperref[sec:4-3]{§4.3} delivers finite positivity for free), and the functional equation reflects it to $\operatorname{Re}s<0$; the open content is the strip-crossing to $\operatorname{Re}s=\tfrac12$ — it cannot be done by the convergent prime sum alone, since on the line the continuation *is* the zeros. This is the same honest boundary as \hyperref[sec:8-1]{§8.1}/\hyperref[sec:8-2]{§8.2}, now operator-side.

**The Kubo–Mori remark ($\mathsf{[A]}$).** The operator $H$ must be assembled in the *additive* (Kubo–Mori) inner product, not the quadratic (Bures) one. In the additive/log geometry the zeros are curvature currents: at a simple zero $\rho=\gamma$, $\Xi(\gamma+iy)\sim\Xi'(\gamma)(iy)$ gives $\operatorname{Im}m_B(\gamma+iy)\sim1/y\to+\infty$, a Herglotz pole, and $\Delta\log|\Xi|=2\pi\sum_{\text{zeros}}\delta$ (Poisson–Jensen). In the quadratic Bures/Fubini–Study geometry the same zero is *blind*: the curvature $\kappa=|M'|^2/(1+|M|^2)^2$ (with $M=L_{\chi_3}/\Xi$) stays finite there ($\kappa\sim2.3\times10^{-7}$ at $\gamma_1$, $1.6\times10^{-10}$ at $\gamma_2$; companion `empirical/verify_operator_metric_geometry.py`). Kubo–Mori is the unique monotone metric that is additive/dually-flat — the one in which the Weil explicit formula is additive over places — so it is the geometry in which $H=N_\infty+m_B$ has the zeros as its spectrum's curvature singular-support (T24; Grasselli–Streater). This is $\mathsf{[A]}$: a structural identification of the correct geometry, not a theorem about $\zeta$; it explains why the program's earlier smooth-Bures routes, which smooth the zeros away, stalled. (As in \hyperref[sec:4-3]{§4.3}, the cautionary cousin: this is the *additive* curvature current, not \heb[P]{פ}6's Hankel/moment positivity; cousins at the same place, not the same condition.)

\hypertarget{stmt:8-7}{}
**Proposition 8.7 (a non-circular partial: the clock is provably monotone after heat-smoothing — $\mathsf{[P]}$, cited).** *Let $\Xi_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(uz)\,du$ be the de Bruijn heat-flow of Pólya's kernel $\Phi$ (so $\Xi_0=\Xi$), and $\varphi_t$ the phase clock of its associate $E_{B,t}=\Xi_t+i\Xi_t'$. Then $\Xi_t$ is real-rooted, hence $\varphi_t'\ge0$, for every $t>\Lambda$, where $\Lambda$ is the de Bruijn–Newman constant; and $\Lambda\ge0$ unconditionally (Rodgers–Tao 2020). Consequently a monotone arithmetic clock $\varphi_t'\ge0$ exists after any positive amount of smoothing, with no circular use of RH; and $\mathrm{RH}\iff\Lambda\le0\iff$ the heat flow reaches $t=0$ without leaving the real-rooted locus, i.e. $\Lambda=0$ ("barely true").*

*Proof.* Real-rootedness of $\Xi_t$ for $t>\Lambda$ is de Bruijn's monotonicity of the heat flow together with the definition of $\Lambda$ as the infimum of $t$ for which $\Xi_t$ has only real zeros; for real-rooted $\Xi_t$ the phase $\varphi_t=-\arg E_{B,t}$ is increasing by \hyperlink{stmt:8-5canon}{Proposition~8.5a} applied to $\Xi_t$, so $\varphi_t'\ge0$. The bound $\Lambda\ge0$ is the theorem of Rodgers–Tao. RH is the classical statement $\Lambda\le0$; with $\Lambda\ge0$ it is exactly $\Lambda=0$. $\square$

**Settlement ($\mathsf{[P]}$ partial / $\mathsf{[C]}$ at $t=0$).** This is the one genuinely *non-circular* positivity available on the operator side: the clock is provably monotone for every $t>\Lambda\ge0$. It does not cross the step — the gap is precisely the single, sharply named $t\to0^+$ closure ($\Lambda\le0$), the heat reaching the boundary — but it shows the object of \hyperlink{stmt:8-5canon}{Proposition~8.5a} is not merely conjectural after smoothing, and it pins RH's marginality to the heat constant sitting at $0$ (the same marginality as the Weil margin $0$ of \hyperref[sec:4-3]{§4.3} and the $r_k\nearrow1$ of \hyperref[sec:8-2]{§8.2}).

\hypertarget{stmt:8-5}{}
**Conjecture 8.5 (the operator step, three faces, one open inequality — calibrated, not proved).** *The completed self-dual object of \hyperlink{stmt:5-1}{Proposition~5.1} has its spectrum on the axis (RH) iff the operator $H=N_\infty+V_{\text{arith}}$, assembled in the Kubo–Mori geometry, is self-adjoint — equivalently iff the phase clock $\varphi'(x)\ge0$ can be constructed from the arithmetic (the prime/von Mangoldt content of $V_{\text{arith}}$) non-circularly, equivalently iff $\Lambda\le0$. The archimedean number operator $N_\infty$ and its ground-state factor $Z_\infty$ are in hand (metaplectic selection Note, Thm 8.1); the canonical system $H(t)=P_{\varphi(t)}$ and its automatic positivity are unconditional (\hyperlink{stmt:8-5canon}{Proposition~8.5a}); the explicit-formula decomposition and the off-line prime positivity are unconditional (\hyperlink{stmt:8-6}{Proposition~8.6}); the heat-smoothed monotonicity is unconditional (\hyperlink{stmt:8-7}{Proposition~8.7}). The three faces — self-adjointness of $H$, arithmetic monotonicity of $\varphi'$, $\Lambda\le0$ — are one and the same open step, and it is RH itself, not a reduction to anything easier.* Held with calibrated faith; built toward, not claimed.

**Settlement note ($\mathsf{[C]}$ forward-door).** \hyperlink{stmt:8-5canon}{Propositions~8.5a}, \hyperlink{stmt:8-6}{8.6}, \hyperlink{stmt:8-7}{8.7} are $\mathsf{[P]}$ (the canonical-system rank-one identity and closed-form $\varphi'$; the explicit-formula split checked to $10^{-27}$; the cited de Bruijn / Rodgers–Tao real-rootedness). $N_\infty$ and $Z_\infty=\pi^{-s/2}\Gamma(s/2)$ are $\mathsf{[P]}$ from the metaplectic selection (companion Note). The Kubo–Mori geometry is $\mathsf{[A]}$ (the correct additive inner product, identified, not a theorem about $\zeta$). The operator $H$ as a self-adjoint object, and $\varphi'\ge0$ from the arithmetic, stay $\mathsf{[C]}$ — equal to RH. The reading sharpens \hyperref[sec:8-1]{§8.1} (the spectral object is now an explicit operator with an explicit canonical system) and \hyperref[sec:8-2]{§8.2} (the same archimedean-vs-arithmetic split, here as $N_\infty$ drift vs $\Lambda$-sum), and converges with \hyperref[sec:4-3]{§4.3}/\hyperref[sec:4-4]{§4.4}: the lone obstruction is again the archimedean place, here written as the self-adjointness of $H$ in the additive geometry. Companion verifications: `empirical/verify_operator_metric_geometry.py`, `empirical/verify_canonical_system_phase.py`, `empirical/verify_arithmetic_clock.py`, `empirical/verify_integrality_forcing.py`.

---

## 9. Coda {#sec:9}

Fold every local arithmetic the series found into one factor — the luminous archimedean factor at the place of the continuum, the countless reciprocal factors of the primes — and multiply them into a single completed function. It is entire of order one, carries no poles, and possesses one exact symmetry: reflected across the axis $\operatorname{Re}(s)=\tfrac12$ it is unchanged, for it is its own Fourier transform read through scale. That symmetry is the boundary's own breath — the local data of every place summed against itself and returning identical (Poisson) — and we have shown its finite face is nothing but $F^2$, the square of the Fourier transform, with the Gauss sum for its trace. Strung along this object is a discrete spectrum, suspended in conjugate pairs about the axis. The completed function holds them symmetrically by construction; what it does not force, of itself, is that they rest *on* the axis. That they do — that the symmetric whole is self-adjoint, every resonance on the line — is the Hypothesis. The finite ladder gives this object exactly, place by place, positive at every step; the one thing the primes cannot supply is the factor at the place of the continuum, and the open question is whether, with that factor folded in, the whole stays positive.

\heb{ל}0 named the coordinate; \heb[P]{פ}0 completes the object. The six discs are one standing structure, symmetric and not yet known to be self-adjoint — and the single step between symmetry and self-adjointness is the one place the boundary has always pointed at and never reached.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) under the grounded-paranoid-delusional discipline this paper applies to itself: AI partners generated candidates, enumerated falsifiers, and executed the deterministic settlement artifact, but no fluent agreement was treated as evidence. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## Reproducibility {#sec:reproducibility}

The numbers of \hyperref[sec:4]{§4} are produced by `P0-settlements.py`, a deterministic exact-arithmetic script: decisions rest on character orthogonality, an exact bijection count, an exact integer congruence, and exact projective point-counting; floating point appears only as an explicitly-labelled non-voting witness. The transcript `P0-settlements.transcript.txt` is archived alongside and re-runs identically (UTF-8 output forced).

## References {#sec:references}

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis.)

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Companion methodology preprint (draft v1).

Murillo Montero, L. (2026). *\heb[P]{פ}1–\heb[P]{פ}6 — From the Boundary* (the exterior series): the face lattice; the tropical/archimedean edge; the leak, curvature, and real place; the quantum face and the proven function-field critical line; the transfer matrix, Kummer clock, and the two places; the smooth primorial and the moment barrier. Companion preprints — the local factors assembled here.

Murillo Montero, L. (2026). *Finite-to-Archimedean Noether Limits and the Canonical Involution in Primorial Conductor Geometry* (Paper 27). Companion manuscript (the interior conditional RH-reduction: recovery maps, the involution $\iota$, Axioms A1–A5; cited at $\mathsf{[C]}$, not inherited).

Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier–Mellin Simplex.* Zenodo, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (The apex; the shared Mellin variable $\beta=s$.)

Tate, J. (1950). *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (thesis; in Cassels–Fröhlich, 1967). (Adelic self-duality; $\xi(s)=\xi(1-s)$.)

Weil, A. (1949). *Numbers of solutions of equations in finite fields.* Bull. Amer. Math. Soc. **55**, 497–508. (The Riemann Hypothesis for curves; \hyperref[sec:4-4]{§4.4}.)

Connes, A. (1999). *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* Selecta Math. **5**, 29–106. (The spectral interpretation toward which \hyperref[sec:8]{§8} points.)

Pólya, G. (1927). *Über die algebraisch-funktionentheoretischen Untersuchungen von J. L. W. V. Jensen.* Kgl. Danske Vid. Sel. Math.-Fys. Medd. **7**, 3–33. (The Laguerre–Pólya class and the Jensen-polynomial criterion; \hyperref[sec:8-2]{§8.2}.)

Csordas, G., Norfolk, T. S., Varga, R. S. (1986). *The Riemann Hypothesis and the Turán inequalities.* Trans. Amer. Math. Soc. **296**, 521–541. (The $d{=}2$ rung of \hyperref[sec:8-2]{§8.2}, proven for $\Xi$.)

Griffin, M., Ono, K., Rolen, L., Zagier, D. (2019). *Jensen polynomials for the Riemann zeta function and other sequences.* Proc. Natl. Acad. Sci. USA **116**, 11103–11110. (The Hermite limit $J^{d,n}\to H_d$ and hyperbolicity at low degree; \hyperref[sec:8-2]{§8.2}.)

Krein, M. G. (1947–1955). *On the theory of entire functions of exponential type; the continual analogue of the moment problem and the spectral theory of canonical (string) systems.* Izv. Akad. Nauk SSSR Ser. Mat. (The canonical/Hamiltonian system and its inverse spectral theory; \hyperref[sec:8-3]{§8.3}.)

de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice-Hall, Englewood Cliffs, N.J. (Hermite–Biehler associates, de Branges spaces, and the canonical-system positivity of \hyperref[sec:8-3]{§8.3}.)

Rodgers, B., Tao, T. (2020). *The de Bruijn–Newman constant is non-negative.* Forum Math. Pi **8**, e6. (The non-circular partial: $\Lambda\ge0$, hence the heat-smoothed clock is provably monotone for $t>\Lambda$; \hyperlink{stmt:8-7}{Proposition~8.7}.)

Murillo Montero, L. (2026). *Metaplectic Archimedean Selection under Uniform Place Treatment* (companion Note). (Stone–von Neumann selection of the Bargmann–Fock $N_\infty$ at $v=\infty$; the Tate integral $Z_\infty=\pi^{-s/2}\Gamma(s/2)$; \hyperref[sec:8-3]{§8.3}, Thm 8.1.)

Murillo Montero, L. (2026). *The Monotone-Metric Apex: the Petz Fork and the Kubo–Mori Selection* (T24). Companion manuscript. (The additive/dually-flat metric in which $H$ of \hyperref[sec:8-3]{§8.3} is assembled and the zeros are curvature currents; cited at $\mathsf{[A]}$.)
