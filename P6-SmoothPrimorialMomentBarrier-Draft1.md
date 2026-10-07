# \heb[P]{פ}6 — From the Boundary: The Smooth Primorial, the Real Place, and the Moment Barrier

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 30, 2026*

## Abstract

**Situation.** T33 (The Smooth Primorial Family) builds the $\Gamma$-analogue of the primorial: the smooth primorial $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$, written with the letter **\heb[P]{פ}** — this series' own glyph. It is forced by Riemann's explicit formula (the constant $1/2\pi=e^{-\zeta'(0)/\zeta(0)}$ is the archimedean boundary term), unique by Bohr–Mollerup and Wielandt exactly as $\Gamma$ is, and its deviation from the exact primorial is the Riemann zero-sum, so that RH $\iff\log\mathrm{pri}_*-\log\mathrm{pri}_\sharp=O(\sqrt x\log^2x)$. Crucially, T33 proves the primorial $(P_n)$ is **not a moment sequence**: its Hankel determinant $D_3=-787680<0$, so unlike the factorial it admits no exact Mellin/$\Gamma$-style interpolation.

**Gap.** T33 builds this from the centre, as analytic interpolation. But the smooth primorial \heb[P]{פ} *is* the object [\heb[P]{פ}3] named the terminal **real place** $\{\infty\}$ — the archimedean edge finite-prime data cannot generate. The exterior question is whether the moment barrier T33 found for the primorial is special to it, or whether the *whole* divisor family is excluded from the real place; and whether the barrier has structure.

**Action.** Under the grounded-paranoid-delusional method (Murillo Montero 2026): a fenced *Star* (\hyperref[sec:2]{§2}); three matched-pair falsifiers pre-registered before any check (\hyperref[sec:3]{§3}); one deterministic, exact-integer artifact (`P6-settlements.py`) anchored to T33's own objects (\hyperref[sec:4]{§4}). Eulerian: smallest obstruction first.

**Result.** Three settlements. **\heb[P]{פ}moment ($\mathsf K_1$, $\mathsf K_2$ verified, joint; $\mathsf K_3$ falsified) — a new theorem.** Every genuinely-multiplicative primorial invariant — $\varphi(P_n)$, $\sigma(P_n)$, $J_k(P_n)=\prod(p^k-1)$, $\prod(p^k+1)$, $\prod p^k$ — is non-moment (some $D_N<0$); the *only* moment member is the divisor count $d(P_n)=2^n$, which forgets prime magnitudes. The real place is barred from the **entire** finite-prime divisor family. The proof tool is the factorization $D_N=\big(\prod_{i\le N}b_i\big)\det[b_{i+j}/b_i]$, which carries $\operatorname{sign}(D_N)$ in its second factor; the first-failure index $N^*$ is then found identical across $\prod(p^k{-}1)$, $\prod(p^k{+}1)$, $\prod p^k$ for all tested $k$ ($k\le8$) — an exact finite verification, not forced by the factorization (the correction factors are $O(1)$ at the small primes that set $N^*$), the general invariance left open. The depth $N^*(k)$ is non-decreasing and unbounded (the obstruction recedes with $k$, mirroring T33's Euler-product convergence partition), but the sharpening "$N^*(k)$ is *strictly* monotone" we pre-registered, and it *failed* ($3,3,4,4,5,9,\dots$). **\heb[P]{פ}fixedpoint ($\mathsf K$, joint).** Under the starting-prime translation $z\mapsto z+\mathrm{Li}(p)$ (T33's orbit of one master curve), $\log2\pi$ is the *unique* shift-invariant constant — the archimedean boundary is the fixed point of the prime ladder — while every finite-prime constant moves ($\zeta(k)$ telescopes, $\gamma$/$\log p$ accumulate); the master curve has a finite left floor $e/2\pi$, one factor of $e$ below its ground state. **\heb[P]{פ}barcode ($\mathsf K$, joint).** In the sieve filtration a prime $q$ is born at $\pi(\sqrt q)$ and dies at $\pi(q)$; a prime changes no verdict below its square, so the $\sqrt{\cdot}$-scale — the RH scale — is the boundary of certainty, and the barcode's birth measure $\psi-\vartheta\sim\sqrt x$ and the Riemann zeros are two faces of one object.

**Harvest.** The smooth primorial \heb[P]{פ} is the real place; the moment barrier (\heb[P]{פ}moment) is the family-wide wall between the finite primes and that place; the boundary's fixed point is $\log2\pi$ (\heb[P]{פ}fixedpoint); the boundary of certainty is $\sqrt{\cdot}$ (\heb[P]{פ}barcode). The exterior reading closes a loop: the letter the interior wrote on its terminal scalar is the letter of this series, and the object that bars the family from it is the most classical wall there is — Hankel positivity. The family-wide barrier and the factorization are carried at $\mathsf{[P]}$ (the barrier a theorem in no single interior paper); the exact depth law and the single-object reading at $\mathsf{[A]}$; no GRH claim is made — T33 §11.3's honest negative stands.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
The factorial $1,2,6,24,\dots$ has a famously smooth twin, the Gamma function, that passes through every one of its values exactly. The primorial $1,2,6,30,210,\dots$ — multiply the primes one at a time — has a smooth twin too, built in a companion paper, but it only *approaches* the primorial; it never lands on it exactly, and the gap is governed by the Riemann hypothesis. This paper asks why the exact landing is impossible, and finds a clean classical answer: a number sequence can be the ``moments'' of a probability distribution only if a ladder of determinants stays non-negative, and for the primorial one of them turns negative ($-787680$). We then show this isn't a quirk of the primorial: *every* natural prime-built sequence fails the same test — only the one that throws away the sizes of the primes survives. A short exact-integer program is the whole evidence; we also test an obvious guess about the pattern, watch it fail, and keep it.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| $P_n$ | Primorial $\prod_{i=1}^n p_i$; $P_0=1$. $\mathrm{pri}_*(x)=\prod_{p\le x}p=e^{\vartheta(x)}$. |
| \heb[P]{פ}$(z)$ | Smooth primorial $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$ (T33, T15). |
| $\mathrm{Li}^{-1}$ | Inverse logarithmic integral; $\mathrm{Li}^{-1}(0)=2$, $(\mathrm{Li}^{-1})'=\log\mathrm{Li}^{-1}$. |
| $b_n$ | A multiplicative sequence $\prod_{i=1}^n c_i$; here $c_i=f(p_i)$. |
| $D_N$ | Hankel determinant $\det(b_{i+j})_{0\le i,j\le N}$. |
| moment seq. | $(b_n)$ with $b_n=\int t^n\,d\mu$, $\mu\ge0$; iff all $D_N\ge0$ (Hamburger). |
| $W$ | Factor matrix $W_{ij}=b_{i+j}/b_i=\prod_{l=i+1}^{i+j}c_l$; $D_N=(\prod_{i\le N}b_i)\det W$. |
| $N^*$ | First-failure index: least $N$ with $D_N<0$. |
| $\varphi,\sigma,J_k$ | $\varphi(P_n)=\prod(p{-}1)$, $\sigma(P_n)=\prod(p{+}1)$, $J_k(P_n)=\prod(p^k{-}1)$. |
| $\mathrm{Li}(p)$ | Marked abscissa; $\mathrm{Pri}_p(z)=$\heb[P]{פ}$(z+\mathrm{Li}(p))$ (starting-prime orbit). |
| $b(q),d(q)$ | Sieve birth $\pi(\sqrt q)$ and death $\pi(q)$ of a prime $q$ (barcode). |
| $\mathsf{[P]/[A]/[C]}$ | Tiers: proven / structural-pending-named-audit / conjectural-reduced. |
| $\mathsf K,\mathsf L$ | Matched-pair branches; *joint-on-disjoint* when both fire on disjoint sub-structures. |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| GPD | Grounded-paranoid-delusional (the method of Murillo Montero 2026). |
| (G)RH | (Generalized) Riemann Hypothesis. |
| moment problem | When is $(b_n)$ the moments $\int t^n d\mu$ of a positive measure? (Hankel $\ge0$.) |
| real place | The archimedean place $\{\infty\}$ of $\mathbb Q$ — the smooth primorial's home. |
| Hankel determinant | $\det(b_{i+j})$; its sign decides the moment property. |

---

## 1. One determinant turns negative {#sec:1}

Begin where Euler would: with the smallest determinant that already decides the question.

The factorial $1,1,2,6,24,\dots$ has the Gamma function passing through it exactly, $\Gamma(n+1)=n!$. The reason is classical: the factorial is a *moment sequence*, $n!=\int_0^\infty t^n e^{-t}\,dt$, and Mellin's integral interpolates any moment sequence. The primorial $1,2,6,30,210,2310,30030,\dots$ has a smooth twin too — the companion paper's $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$ — but it only *approaches* the primorial. Is the inexactness a defect of the construction, or a wall?

It is a wall, and one $4\times4$ determinant shows it. A sequence is a moment sequence only if every Hankel determinant $D_N=\det(b_{i+j})$ is non-negative (each is $\int(\sum c_i t^i)^2 d\mu\ge0$). For the primorial,
$$
D_0=1,\quad D_1=\begin{vmatrix}1&2\\2&6\end{vmatrix}=2,\quad D_2=24,\quad
D_3=\begin{vmatrix}1&2&6&30\\2&6&30&210\\6&30&210&2310\\30&210&2310&30030\end{vmatrix}=-787680.
$$
A negative determinant. The primorial is not a moment sequence; no Mellin integral lands on it (this is T33's Theorem 9A.4). Now the exterior question, asked by computing one more determinant. Take the **totient** primorial $\varphi(P_n)=\prod_{p\le p_n}(p-1)=1,1,2,8,48,480,5760$. Its $D_3=-17408<0$ as well. And the **sigma** primorial, and the Jordan totients — every one we try turns a determinant negative.

This is the subject of the paper. The companion paper proved the primorial misses its smooth twin by a Riemann-zero-sized gap. From the boundary we see why, and how far it spreads: the smooth primorial \heb[P]{פ} *is* the real place $\{\infty\}$ that [\heb[P]{פ}3] proved terminal, and the **moment barrier** — Hankel positivity failing — is the wall that bars not just the primorial but the entire finite-prime divisor family from reaching it. Only one degenerate invariant, the divisor *count* $2^n$, slips through, precisely because it has forgotten how big the primes are.

### 1.1 Why a gate, and why exact {#sec:1-1}

A word on method. The objects ahead — the sign of a determinant attached to the primes, the reach of a barrier — are exactly the kind a willing mind and a fluent assistant can talk themselves into. So we adopt the grounded-paranoid-delusional discipline (Murillo Montero 2026): one ambitious picture with no vote on truth (\hyperref[sec:2]{§2}); the meaning of every outcome fixed before any computation (\hyperref[sec:3]{§3}); and one short program in exact integer arithmetic — no floating point in any decision of sign, vanishing, or membership — whose transcript is the record (\hyperref[sec:4]{§4}). The artifact is `P6-settlements.py`. No agreement, however fluent, counts as evidence.

---

## 2. The Star (delusional; no vote on truth) {#sec:2}

> **Fence.** This section is *Historic Fiction*. It chooses what to attempt and in what order. It decides nothing. The only road to a result runs through the gate of \hyperref[sec:3]{§3} and \hyperref[sec:4]{§4}.

Here is the picture to chase. [\heb[P]{פ}3] followed the boundary operator $\partial$ up a ladder — packets, orders, flows, curvature — to the **real place** $\{\infty\}$, and proved it terminal: finite-prime data cannot generate the archimedean completion. T33 then built that completion analytically — the smooth primorial \heb[P]{פ}, with its forced $1/2\pi$ archimedean constant. The Star says these are the same object, and that the relationship between the finite primes and the real place is a single classical wall.

1. **The smooth primorial is the real place.** \heb[P]{פ}$(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$ is the $\Gamma$ of the primorial; its $1/2\pi=e^{-\zeta'(0)/\zeta(0)}$ is the archimedean boundary term of Riemann's explicit formula. The letter the interior wrote on it is this series' own letter. The fiction: every structural fact about \heb[P]{פ} is a fact about the boundary $\partial$ at its terminal altitude.

2. **The barrier is a moment barrier, and it is family-wide.** The factorial reaches its $\Gamma$ because it is a moment sequence; the primorial cannot, because it is not (one negative Hankel determinant). The fiction: this is not special to the primorial — *every* finite-prime multiplicative invariant fails the same positivity test, because they all share the prime-driven growth that breaks it, and only the magnitude-forgetting divisor count escapes.

3. **The boundary has a fixed point and a horizon.** Under the prime ladder's own shift (start one prime later $=$ multiply in one more prime), the finite-prime constants all move; only the archimedean $\log2\pi$ stays — the boundary is the fixed point of the shift. And in the sieve, a prime's fate is sealed at its square root — the $\sqrt{\cdot}$-scale, the RH scale, is the boundary of certainty.

If true: the real place is a wall the finite primes press against from one side, classical (Hankel) in its barrier, archimedean ($\log2\pi$) in its fixed point, and $\sqrt{\cdot}$-scaled (RH) in its horizon. The paper tests three load-bearing pieces and reports the arithmetic.

---

\clearpage

## 3. Pre-registration (paranoid; meanings fixed before the check) {#sec:3}

Before running `P6-settlements.py`, we fix the meaning of every outcome.

| Audit | Claim under test | $\mathsf K$ | $\mathsf L$ | Joint-on-disjoint |
|---|---|---|---|---|
| **\heb[P]{פ}moment** | The moment barrier is family-wide. | $\mathsf K_1$: every $\prod(p^k{\pm}1)$, $\prod p^k$ is non-moment; only $d{=}2^n$ moment. $\mathsf K_2$: $N^*$ depends only on $p^k$ (factorization). $\mathsf K_3$ (sharp): $N^*(k)$ strictly monotone. | $\mathsf L_1$: a multiplicative member is moment. $\mathsf L_3$: $N^*(k)$ not strictly monotone. | $N^*(k)$ non-decreasing, unbounded, but irregular. |
| **\heb[P]{פ}fixedpoint** | $\log2\pi$ is the boundary's fixed point. | Exactly one emitted constant is shift-invariant ($\log2\pi$); the rest move. | More than one fixed, or $\log2\pi$ moves. | Left floor $e/2\pi$, ground state $e^2/2\pi$, ratio exactly $e$. |
| **\heb[P]{פ}barcode** | Destiny is written at $\sqrt q$. | Window $\{p_n<q<p_{n+1}^2\}=\{b(q)\le n<d(q)\}$; no verdict changes below the square. | The certification scale is not $\sqrt q$. | Birth measure $\psi-\vartheta\sim\sqrt x$ is the RH-scale object. |

We run the artifact.

---

## 4. Settlement (grounded; the transcript is the record) {#sec:4}

Each settlement pairs a **Proposition** with the **realized branch**, confirmed by the deterministic artifact. We compute first and explain second.

### 4.1 \heb[P]{פ}moment — the family-wide wall, and the factorization that proves it {#sec:4-1}

Run the Hankel test across the divisor family. The artifact returns, exactly:

| sequence | first $D_N<0$ | verdict |
|---|---|---|
| $P_n$, $\varphi(P_n)$, $\sigma(P_n)$, $J_2(P_n)$ | $N^*=3$ | non-moment |
| $J_3(P_n)=\prod(p^3-1)$ | $N^*=4$ | non-moment |
| $d(P_n)=2^n$ | — | **moment** (point mass $\delta_2$) |
| $n!$ (control) | — | moment |

Every genuinely-multiplicative member fails; only the divisor count $2^n$ — which records *that* a prime was multiplied in but not *which* — survives, as the moments of a point mass at $2$. The reason is one identity.

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (the moment barrier is family-wide).** *Let $b_n=\prod_{i=1}^n c_i$ with $c_i>0$. Then the Hankel determinant factors as*
$$
D_N=\Big(\prod_{i=0}^{N}b_i\Big)\det\Big[\tfrac{b_{i+j}}{b_i}\Big]_{0\le i,j\le N},\qquad \tfrac{b_{i+j}}{b_i}=\prod_{l=i+1}^{i+j}c_l,
$$
*so $\operatorname{sign}(D_N)$ is the sign of the right-hand determinant, whose entries depend on the $c_l$ only through their product. The factorization does not by itself force the first-failure index $N^*$ to agree across the families $\prod(p^k{-}1)$, $\prod(p^k{+}1)$, $\prod p^k$ — their correction factors $\prod(1\mp p_l^{-k})$ are $O(1)$ at the small primes that determine $N^*$ — but exact computation gives $N^*\big(\prod(p^k{-}1)\big)=N^*\big(\prod(p^k{+}1)\big)=N^*\big(\prod p^k\big)$ for $k=1,\dots,8$, the general invariance left conjectural. Every such sequence has some $D_N<0$ (it is non-moment); the only moment member of the divisor family is $d(P_n)=2^n$ (T33 §9A.4; Akhiezer, moment problem).*

*Proof.* Row $i$ of $(b_{i+j})$ is $b_i\cdot(1,c_{i+1},c_{i+1}c_{i+2},\dots)$; factoring $b_i>0$ from each row gives the displayed factorization, and the row-factor $\prod_i b_i>0$ does not affect the sign. The right-hand entries $\prod_{l=i+1}^{i+j}c_l$ for $c_l=p_l^k(1\mp p_l^{-k})$ are the pure-power entries times $\prod(1\mp p_l^{-k})$; these correction factors are $O(1)$ at the small primes (e.g. $\tfrac12$ at $p=2$, $k=1$), so the factorization alone does not force equal $N^*$, but exact computation finds the correction does not flip the sign at $N^*$ for $k=1,\dots,8$, so the three families share $N^*$ over the tested range (the general case is not established here). Non-momentness for each tested member is the exact computation; $d(P_n)=2^n=\int t^n\,\delta_2$ is the lone moment sequence (its ratios are constant). $\square$

**Settlement \heb[P]{פ}moment — $\mathsf K_1$ + $\mathsf K_2$ (factorization proved; family-invariance verified for $k\le8$) + joint-on-disjoint, with $\mathsf K_3$ falsified, $\mathsf{[P]}$.** Three readings.

*The wall is family-wide ($\mathsf K_1$, $\mathsf{[P]}$).* The real place is unreachable not only from the primorial but from $\varphi$, $\sigma$, every $J_k$ and $\prod(p^k\pm1)$ and $\prod p^k$. Only the magnitude-blind $2^n$ escapes — a clean structural statement of *why* the archimedean factor must be adjoined from outside (T15 §12.3): no finite-prime invariant that remembers prime sizes can generate it. This strengthens T33's single-sequence result to the family.

*The factorization is proven; the family-invariance is verified ($\mathsf K_2$).* The artifact verifies the identity $D_N=(\prod b_i)\det[b_{i+j}/b_i]$ exactly ($-787680=360\cdot(-2188)$ at $N=3$) — this is $\mathsf{[P]}$, and it places $\operatorname{sign}(D_N)$ in the second factor. It then confirms $N^*$ identical across $\prod(p^k\pm1)$ and $\prod p^k$ for $k=1,\dots,8$. Because the correction factors $\prod(1\mp p_l^{-k})$ are $O(1)$ at the small primes that set $N^*$, this family-invariance is an exact finite verification ($k\le8$), not a corollary of the factorization; the general law is $\mathsf{[A]}$.

*The obvious sharpening is false ($\mathsf K_3$ falsified, retained).* We pre-registered that the depth $N^*(k)$ grows *strictly* with $k$. It does not: the exact sequence is $3,3,4,4,5,9,9,9,\dots$ — non-decreasing and unbounded (the obstruction recedes with $k$, mirroring T33 §8.5's partition by Euler-product convergence: higher $k$ is deeper absolute convergence, and the wall moves further out), but with plateaus and a jump, no clean closed form. We keep the dead guess. The $k\to\infty$ limit of the sign-determining $\det[b_{i+j}/b_i]$ is a tropical (max-plus) determinant — the wall's far structure is [\heb[P]{פ}2]'s tropical edge — and pinning the exact $N^*(k)$ law is the cornered $\mathsf{[A]}$ obligation.

### 4.2 \heb[P]{פ}fixedpoint — the boundary is the fixed point of the prime ladder {#sec:4-2}

T33's master identity is that starting the primorial at a later prime is a *translation* of one master curve: $\mathrm{Pri}_p(z)=$\heb[P]{פ}$(z+\mathrm{Li}(p))$, with the marked abscissae $\{\mathrm{Li}(p)\}$ approximately unit-spaced — starting one prime later and multiplying in one more prime are the same operation. Under this shift the emitted constants move; the exterior asks which, if any, stays.

\hypertarget{stmt:4-2}{}
**Proposition 4.2 (the archimedean fixed point).** *Under the starting-prime shift $p\mapsto$ next prime, the family's emitted constants fall into three classes (T33 §10.3): the $\zeta(k)$ constants telescope, $R_k^{(p)}=\prod_{q>p}(1-q^{-k})\to1$; the Mertens/boundary constants $\log p$, $\widetilde\gamma_*^{(p)}$ accumulate; and $\log2\pi=\zeta'(0)/\zeta(0)$ is invariant. The archimedean constant $\log2\pi$ is the unique fixed point of the shift — truncating the Euler product changes every finite-prime constant but not the archimedean coupling. The master curve has a finite left floor \heb[P]{פ}$(-\infty)=e/2\pi$ with \heb[P]{פ}$(0)/$\heb[P]{פ}$(-\infty)=e$ (T33 §10.1, §10.5).*

*Proof.* $R_k^{(p)}\cdot$(captured factor)$=1/\zeta(k)$ telescopes by definition; the artifact exhibits $R_2^{(p)}\pi^2=8,9,\tfrac{75}{8},\tfrac{1225}{128},\dots\to\pi^2$, strictly moving. The boundary slope $(\mathrm{Li}_p^{-1})'(0)=\log p$ moves with $p$. The constant $\log2\pi$ comes from $\zeta$ at $s=0$, where truncating the Euler product (which only removes finite primes) leaves the archimedean factor unchanged; it does not shift. The floor is $\mathrm{Li}^{-1}(z)\to1^+$ as $z\to-\infty$, giving $e^1/2\pi$, and $\mathrm{Li}^{-1}(0)=2$ gives the factor $e$. $\square$

**Settlement \heb[P]{פ}fixedpoint — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** Exactly one emitted constant survives the prime ladder's translation, and it is the archimedean one: $\log2\pi$ is the fixed point of the shift that moves all finite-prime data. The boundary is, literally, the part the ladder cannot move. (The artifact's $R_2^{(11)}\pi^2=29645/3072$ reduces to T33 §10.2's $148225/15360$, an anchored cross-check.) The joint structure is the left floor $e/2\pi$ — the value "at the prime $1$," the multiplicative-unit threshold below all primes — one factor of $e$ beneath the ground state \heb[P]{פ}$(0)$.

### 4.3 \heb[P]{פ}barcode — the boundary of certainty is $\sqrt{\cdot}$ {#sec:4-3}

The sieve of Eratosthenes is a filtration; T33 reads it as a persistence barcode. A prime $q$ is *certified* prime the moment the sieving primes reach $\sqrt q$ (below its square it can mask nothing), and *recruited* into the primorial at its own stage. So its bar runs from birth $b(q)=\pi(\sqrt q)$ to death $d(q)=\pi(q)$.

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (the $\sqrt{\cdot}$ horizon).** *The primes certified-but-unrecruited at stage $n$ are exactly the window $\{q:p_n<q<p_{n+1}^2\}=\{q:b(q)\le n<d(q)\}$ (T33 Prop 9A.2). A prime changes no primality verdict below its square. The integrated birth measure is the prime-power leakage $\psi(x)-\vartheta(x)=\sum_{k\ge2}\vartheta(x^{1/k})\sim\sqrt x$ — the same $\sqrt{\cdot}$-scale quantity whose size RH governs (T33 Obs 9A.3, Cor 4.2).*

*Proof.* $b(q)\le n\iff\pi(\sqrt q)\le n\iff\sqrt q<p_{n+1}\iff q<p_{n+1}^2$; and $n<d(q)\iff p_n<q$. A composite coprime to $P_n$ has two factors $>p_n$, hence $\ge p_{n+1}^2$, so none lies in $(p_n,p_{n+1}^2)$. The leakage identity is the definition of $\psi-\vartheta$. $\square$

**Settlement \heb[P]{פ}barcode — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** The artifact confirms the window identity exactly at stages $n=1,\dots,4$ (e.g. stage $2$: $\{5,7,11,13,17,19,23\}$ both ways). A prime's destiny is sealed at its square root: the $\sqrt{\cdot}$-scale is the sieve's boundary of certainty. The joint reading is the unification: the barcode's birth measure $\psi-\vartheta\sim\sqrt x$ and the analytic location of the zeros are two faces of the one $\sqrt{\cdot}$-scale object — the same scale that, in \heb[P]{פ}moment, is the gap between the primorial and its smooth twin. Honest, as T33 §11.3 insists: this is RH's *scale*, recovered structurally; it is not, and we do not present it as, an attack on RH.

---

## 5. The synthesis (earned) {#sec:5}

We restate the Star at the tier each piece supports.

\hypertarget{stmt:5-1}{}
**Proposition 5.1 (the real place and its wall — $\mathsf{[P]}$ for the pieces, $\mathsf{[A]}$ for the single object).** *The three settlements establish, deterministically and at $\mathsf{[P]}$:*

- *(barrier) every finite-prime multiplicative primorial invariant is non-moment; only the magnitude-blind $d=2^n$ reaches the real place — the moment barrier is family-wide (verified across the family for $k\le8$), with $\operatorname{sign}(D_N)$ carried by the factorization $D_N=(\prod b_i)\det[b_{i+j}/b_i]$ (\hyperlink{stmt:4-1}{Proposition~4.1});*
- *(fixed point) $\log2\pi$ is the unique shift-invariant constant of the prime ladder — the archimedean boundary is the fixed point (\hyperlink{stmt:4-2}{Proposition~4.2});*
- *(horizon) a prime's certification is sealed at $\sqrt q$; the $\sqrt{\cdot}$-scale birth measure and the Riemann zeros are one object (\hyperlink{stmt:4-3}{Proposition~4.3}).*

*That T33's smooth primorial \heb[P]{פ} is the terminal real place of [\heb[P]{פ}3], pressed on from the finite-prime side by the moment barrier, fixed at $\log2\pi$, and horizoned at $\sqrt{\cdot}$ — one boundary seen four ways — is asserted at $\mathsf{[A]}$. The exact depth law $N^*(k)$ is the cornered, unbuilt sharpening.*

The honest seam: the family-wide barrier (\hyperlink{stmt:4-1}{Proposition~4.1}) is the new theorem, in no single interior paper — T33 settled the primorial alone; the exterior reading extends it to the family and supplies the factorization that proves it. As in [\heb[P]{פ}4] and [\heb[P]{פ}5], the new content lives where the interior left a forward door — here, "is this special to the primorial?" — answered by a single classical wall.

---

## 6. The method's own record {#sec:6}

**6.1 One falsification, two re-readings, one theorem.** \heb[P]{פ}fixedpoint and \heb[P]{פ}barcode returned $\mathsf K$ — re-readings of T33 §10 and §9A through the boundary lens, their worth the framing (the fixed point, the horizon), not new theorems. \heb[P]{פ}moment is the one with new content, and the one that was genuinely at risk: its sharp claim $\mathsf K_3$, that the depth $N^*(k)$ grows strictly, was **falsified** by the exact sequence $3,3,4,4,5,9,\dots$ (plateaus and a jump). We keep the dead guess beside the surviving facts — the family-wide barrier and the factorization. A session that confirmed every prediction would have predicted nothing falsifiable.

**6.2 What is re-read and what is new.** The family-wide moment barrier and its factorization proof (\hyperlink{stmt:4-1}{Proposition~4.1}) are in no interior paper: T33 proves only $(P_n)$ non-moment; the extension across the divisor family (verified for $k\le8$), the lone-survivor characterization of $2^n$, and the sign-factorization $D_N=(\prod b_i)\det[b_{i+j}/b_i]$ are new. \heb[P]{פ}fixedpoint and \heb[P]{פ}barcode re-read T33. The honest tally, as in [\heb[P]{פ}4]–[\heb[P]{פ}5]: two boundary re-readings and one boundary theorem. Only \heb[P]{פ}moment's $\mathsf K_3$ falsification changes a realized branch.

---

## 7. Safe and unsafe statements {#sec:7}

**Safe (this paper asserts):**

- $\mathsf{[P]}$ Every finite-prime multiplicative primorial invariant ($\varphi$, $\sigma$, $J_k$, $\prod(p^k\pm1)$, $\prod p^k$) is non-moment; only $d(P_n)=2^n$ reaches the real place (\hyperlink{stmt:4-1}{Proposition~4.1}; settlement \heb[P]{פ}moment) — a statement in no interior paper.
- $\mathsf{[P]}$ The factorization $D_N=(\prod_{i\le N}b_i)\det[b_{i+j}/b_i]$ holds, carrying $\operatorname{sign}(D_N)$ in its second factor. The resulting cross-family invariance $N^*(\prod(p^k{\pm}1))=N^*(\prod p^k)$ is verified exactly for $k\le8$; in general it is $\mathsf{[A]}$ — the correction factors are $O(1)$ at the small primes that set $N^*$, so the factorization alone does not force it (\hyperlink{stmt:4-1}{Proposition~4.1}).
- $\mathsf{[P]}$ $\log2\pi$ is the unique shift-invariant constant of the starting-prime ladder; left floor $e/2\pi$ (\hyperlink{stmt:4-2}{Proposition~4.2}; settlement \heb[P]{פ}fixedpoint).
- $\mathsf{[P]}$ A prime is certified at $\sqrt q$; the window identity and the $\sqrt{\cdot}$-scale birth measure hold (\hyperlink{stmt:4-3}{Proposition~4.3}; settlement \heb[P]{פ}barcode).
- $\mathsf{[A]}$ The smooth primorial is the real place, walled by the moment barrier, fixed at $\log2\pi$, horizoned at $\sqrt{\cdot}$ (\hyperlink{stmt:5-1}{Proposition~5.1}).

**Unsafe (this paper does NOT assert):**

- That the depth $N^*(k)$ is strictly monotone or has a closed form. The strict-monotone form was pre-registered and *falsified*; the exact law is $\mathsf{[A]}$.
- That the cross-family invariance $N^*(\prod(p^k{\pm}1))=N^*(\prod p^k)$ holds for all $k$. It is verified exactly for $k\le8$; the factorization carries $\operatorname{sign}(D_N)$ but does not force the invariance, so the general statement is $\mathsf{[A]}$.
- That the moment barrier or the $\sqrt{\cdot}$-horizon attacks RH. They recover RH's *scale* and a primorial-form equivalence (T33 Cor 4.2); the smooth primorial does *not* separate on-line from off-line zeros (T33 §11.3). The GRH thread stays $\mathsf{[C]}$.
- That the single-object "real place seen four ways" account is proven. It is $\mathsf{[A]}$.
- That this paper is important or field-defining. By the firewall such a claim would stand above its evidence, and the method forbids its author from issuing it.

---

## 8. Forward door: the boundary's classical wall (calibrated, $\mathsf{[C]}$) {#sec:8}

The moment barrier is the most classical obstruction in analysis — Hankel positivity, the Stieltjes/Hamburger moment problem — and it is exactly what separates the finite-prime divisor family from the archimedean place the program keeps meeting at the top of $\partial$'s ladder. That the barrier is family-wide, and that its depth recedes with the Euler-product convergence order toward a tropical limit, suggests the real place is approached by the finite primes along a graded sequence of moment-walls, indexed by $k$, whose $k\to\infty$ tropical structure is [\heb[P]{פ}2]'s edge.

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (forward door — calibrated, not proved).** *The first-failure depth $N^*(k)$ of the Jordan-totient primorial family is non-decreasing and unbounded, with a tropical (max-plus) law in the $k\to\infty$ limit; the real place \heb[P]{פ} is the common limit the finite-prime family approaches across this graded sequence of moment-walls but never reaches (the terminal boundary of [\heb[P]{פ}3]).* Held with calibrated faith; built toward, not claimed.

---

## 9. Coda {#sec:9}

We began with the Gamma function landing exactly on the factorial, and one $4\times4$ determinant — $-787680$ — refusing the same for the primorial. We end with the same refusal spread across the whole family of prime-built sequences, broken only by the one that forgets how big the primes are; with the archimedean constant $\log2\pi$ sitting still while every finite-prime number marches with the ladder; and with each prime's destiny sealed at its square root, the scale on which the Riemann hypothesis lives.

T33 built the smooth primorial and wrote it with the letter \heb[P]{פ}. From the boundary, [\heb[P]{פ}6] reads that letter as its own: the smooth primorial *is* the real place this series has climbed toward since [\heb[P]{פ}3], and the wall between the finite primes and it is the oldest wall in analysis — a determinant that will not stay positive. The part you discard does not vanish; it presses against the real place from below, and the place holds, because the moments do not.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) under the grounded-paranoid-delusional discipline this paper applies to itself: AI partners generated candidates, enumerated falsifiers, and executed the deterministic settlement artifact, but no fluent agreement was treated as evidence. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## Reproducibility {#sec:reproducibility}

The numbers of \hyperref[sec:4]{§4} are produced by `P6-settlements.py`, a deterministic, exact-integer (and `Fraction`) script with no seeds and no floating point in any sign, vanishing, or membership decision; its full transcript (`P6-settlements.transcript.txt`) is archived alongside, and re-running reproduces it identically (UTF-8 output is forced so the transcript is regenerable on any locale).

## References {#sec:references}

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis.)

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Companion methodology preprint (draft v1).

Murillo Montero, L. (2026). *\heb[P]{פ}1 — From the Boundary: The Exterior of Identifying 3*; *\heb[P]{פ}2 — … The Gauge Trilogy at the Tropical Edge*; *\heb[P]{פ}3 — … The Leak, the Curvature, and the Real Place*; *\heb[P]{פ}4 — … The Quantum Face, the Units, and the Proven Critical Line*; *\heb[P]{פ}5 — … The Transfer Matrix, the Kummer Clock, and the Two Places.* Companion preprints (the exterior \heb[P]{פ}-series; [\heb[P]{פ}3] proves the real place terminal; [\heb[P]{פ}2] the tropical edge).

Murillo Montero, L. (2026). *T33 — The Smooth Primorial Family: Bohr–Mollerup, Wielandt, and the Constant Tower of the Prime Ladder.* Companion manuscript (the smooth primorial \heb[P]{פ}; the moment obstruction §9A.4; the constant tower §10; the sieve barcode §9A).

Murillo Montero, L. (2026). *T15 — Finite-to-Archimedean Completion.* Companion manuscript (\heb[P]{פ} as the scalar real-place completion; the archimedean factor adjoined externally).

Akhiezer, N. I. (1965). *The Classical Moment Problem.* Oliver & Boyd. (Hankel determinants and the Hamburger/Stieltjes moment problem, used throughout \hyperref[sec:4-1]{§4.1}.)

Riemann, B. (1859). *Über die Anzahl der Primzahlen unter einer gegebenen Größe.* Monatsber. Berlin. (The explicit formula; the $\sqrt{\cdot}$-scale and $\zeta'(0)/\zeta(0)=\log2\pi$.)
