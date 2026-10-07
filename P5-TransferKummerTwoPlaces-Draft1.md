# \heb[P]{פ}5 — From the Boundary: The Transfer Matrix, the Kummer Clock, and the Two Places

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 30, 2026*

## Abstract

**Situation.** The mean-zero hyperplane $H_N$ carries two orthogonal bases. T9 (The Helmert–Fourier Transfer Matrix) names the change-of-basis between them: the integer-rational **Helmert** basis, whose unit normalizers $\sqrt{k(k+1)}$ build the multiquadratic **radical clock** $K_N=\mathbb Q(\sqrt p:p\le N)$ of T4 (the *dimensional* axis), and the **character** basis of cyclotomic Fourier modes, sorted by conductor (the *frequency* axis). Their transfer matrix $U$ — unitary over the compositum $K_N\cdot\mathbb Q(\zeta_N)$ — is the apex's arithmetic Jacobian; T9 leaves the conductor-block structure of $U$ as an explicit *unbuilt* forward door, calling it "Gauss-sum-like content." T10 (The Kummer Clock and the $m$-Power Gauge Hierarchy) lifts the radical clock to the whole gauge corridor: the **Kummer clock** $K_N^{(m)}=\mathbb Q(\zeta_m,\sqrt[m]{p}:p\le N)$, with the $m=2$ rung the radical clock of T4.

**Gap.** Both papers are written from the centre — $U$ as a coordinate change, the Kummer clock as a tower of normalizers. The exterior reading asks what *one boundary object* they are two faces of. The interior already named that boundary, in [\heb[P]{פ}3]: the **real place** $\{\infty\}$, the terminal archimedean edge that finite-prime data cannot generate. The radicals $\sqrt[m]{p}$ are real-place objects; the cyclotomic $\zeta$ are finite-prime objects; and $U$ and the Kummer clock are exactly where the two *places* of a number field meet.

**Action.** Under the grounded-paranoid-delusional method (Murillo Montero 2026): a fenced *Star* with no vote on truth (\hyperref[sec:2]{§2}); three matched-pair falsifiers pre-registered before any check (\hyperref[sec:3]{§3}); one deterministic, exact-arithmetic artifact (`P5-settlements.py`) anchored to T9–T10's own objects (\hyperref[sec:4]{§4}). The exposition is Eulerian: smallest number first.

**Result.** Three settlements. **\heb[P]{פ}transfer ($\mathsf K_1$, joint; $\mathsf K_2$ falsified) — a new theorem.** T9's "Gauss-sum-like content" is precisely the **Ramanujan sum**: each Helmert rung $k$ distributes its Fourier weight over the conductor packets $H_d$ as $R_k(d)=\sum_{c\in H_d}|U_{kc}|^2=\frac{1}{Nk(k+1)}\sum_{s,t}(h_k)_s(h_k)_t\,c_d(s-t)$, a *complete* distribution over conductors ($\sum_{d\mid N}R_k(d)=1$). The first rung is $(\varphi(d)-\mu(d))/N$ and the last is $\varphi(d)/(N-1)$ — totient and Möbius, the two conductor functions, in closed form. The natural sharpening "the distribution is the same for every rung" we pre-registered, and it *failed*. **\heb[P]{פ}Kummer ($\mathsf K$).** The Kummer-clock degree factors as $[K_N^{(m)}:\mathbb Q]=\varphi(m)\cdot m^{\pi(N)}$ — a finite-prime gauge factor $\varphi(m)$ times a real-place tower $m^{\pi(N)}$ that grows by exactly $m$ at each prime rung. **\heb[P]{פ}overlap ($\mathsf K$, joint).** The radical field $K_N$ and the cyclotomic $\mathbb Q(\zeta_N)$ are *not* linearly disjoint: they fuse on the real quadratic subfields of $\mathbb Q(\zeta_N)$, governed by the conductor $\operatorname{cond}\mathbb Q(\sqrt p)\mid N$ — $p$ for $p\equiv1$, $4p$ for $p\equiv3$ (the extra $2$-adic factor, tying to [\heb[P]{פ}4]'s $2$-adic anomaly), $8$ for $p=2$ — so e.g. $K_{12}\cap\mathbb Q(\zeta_{12})=\mathbb Q(\sqrt3)$, *not* trivial. (This corrects a first-draft criterion that tracked the Gauss sum $\sqrt{p^*}$ and wrongly called $N=12$ trivial; \hyperref[sec:6]{§6.3}.)

**Harvest.** T9's transfer matrix and T10's Kummer clock are the explicit arithmetic of P3's real-place / finite-prime seam: the boundary's coordinate is the **Ramanujan sum** (\heb[P]{פ}transfer), its tower is the **Kummer clock** (\heb[P]{פ}Kummer), and its fusion locus is the **Gauss sum** (\heb[P]{פ}overlap). The Ramanujan identification is carried at $\mathsf{[P]}$ — a theorem in no single interior paper; the single-object "two places, one apex" reading is $\mathsf{[A]}$; no GRH claim is made.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
A flat space can be described with two different rulers. One ruler is made of plain whole-number contrasts (``the first thing minus the second''); the other is made of waves (the frequencies a signal can carry). A companion paper wrote down the dictionary that translates between the two rulers. This paper asks what that dictionary is really made of, and finds a clean answer: a classical object from number theory called a *Ramanujan sum* — the same sums Ramanujan used to study how integers split into pieces. We show, by exact computation, that each whole-number contrast spreads across the wave-frequencies in exactly the proportions those sums dictate, and that two seemingly different kinds of number — the ``square-root'' kind and the ``root-of-unity'' kind — secretly overlap at precisely one place, the place mathematicians call a Gauss sum. We also test an obvious guess about the pattern, watch it fail, and keep the failure on the record. Every number below is the printout of a short exact program; no sentence here is the evidence.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| $N$ | Dimension; outcome labels $\mathbb Z/N$; the hyperplane $H_N=\{q:\sum q_i=0\}$ has $\dim N-1$. |
| $h_k$ | Helmert contrast $(\underbrace{1,\dots,1}_{k},-k,0,\dots,0)$, $1\le k\le N-1$. |
| $e_k$ | Unit Helmert vector $h_k/\sqrt{k(k+1)}$. |
| $\chi_c$ | Additive character $\chi_c(s)=\omega^{cs}$, $\omega=e^{2\pi i/N}$. |
| $U=(U_{kc})$ | Transfer matrix $U_{kc}=\langle e_k,\chi_c/\sqrt N\rangle$, unitary over $K_N\cdot\mathbb Q(\zeta_N)$ (T9). |
| $\operatorname{cond}(c)$ | Conductor $N/\gcd(c,N)$; packet $H_d=\{c:\operatorname{cond} c=d\}$, $\lvert H_d\rvert=\varphi(d)$ (T3). |
| $c_d(n)$ | Ramanujan sum $\sum_{\gcd(a,d)=1}e^{2\pi i an/d}=\mu(d/g)\,\varphi(d)/\varphi(d/g)$, $g=\gcd(d,n)$. |
| $R_k(d)$ | Conductor-block weight $\sum_{c\in H_d}\lvert U_{kc}\rvert^2$ (\hyperref[sec:4-1]{§4.1}). |
| $\varphi,\ \mu$ | Euler totient and Möbius function. |
| $\pi(N)$ | Number of primes $\le N$. |
| $K_N$ | Multiquadratic radical clock $\mathbb Q(\sqrt p:p\le N)$, $[K_N:\mathbb Q]=2^{\pi(N)}$ (T4). |
| $K_N^{(m)}$ | Kummer clock $\mathbb Q(\zeta_m,\sqrt[m]{p}:p\le N)$ (T10); $K_N^{(2)}=K_N$. |
| $\mathbb Q(\zeta_N)$ | $N$-th cyclotomic field; $[\mathbb Q(\zeta_N):\mathbb Q]=\varphi(N)$. |
| $p^*$ | $(-1)^{(p-1)/2}p$; Gauss: $\sqrt{p^*}\in\mathbb Q(\zeta_p)$. |
| $\mathsf{[P]/[A]/[C]}$ | Tiers: proven / structural-pending-named-audit / conjectural-reduced. |
| $\mathsf K,\mathsf L$ | Matched-pair branches; *joint-on-disjoint* when both fire on disjoint sub-structures. |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| GPD | Grounded-paranoid-delusional (the method of Murillo Montero 2026). |
| (G)RH | (Generalized) Riemann Hypothesis. |
| Ramanujan sum | $c_d(n)=\sum_{\gcd(a,d)=1}e^{2\pi i an/d}$, the canonical "sum over a conductor class." |
| Gauss sum | Here the quadratic Gauss sum, with $\sqrt{p^*}\in\mathbb Q(\zeta_p)$. |
| two places | The real (archimedean, $\sqrt[m]{p}$) and finite-prime (cyclotomic, $\zeta$) places of a number field. |

---

## 1. One contrast, spread across the frequencies {#sec:1}

Begin where Euler would: with the smallest contrast on the smallest interesting clock.

Work at $N=6$. The first Helmert contrast is the simplest difference there is, $h_1=(1,-1,0,0,0,0)$ — "first minus second." Ask how it looks in the *frequency* ruler: its overlap with the character $\chi_c$ is $\langle h_1,\chi_c\rangle=1-\omega^c$, of squared size $\lvert 1-\omega^c\rvert^2=2-2\cos(2\pi c/6)$. Now sort the five non-trivial frequencies by **conductor** — the smallest clock on which each is already periodic — into the packets $H_2=\{3\}$, $H_3=\{2,4\}$, $H_6=\{1,5\}$, and add up the squared overlaps in each packet (normalizing by $\lvert h_1\rvert^2=2$). The three packet weights come out
$$
R_1(2)=\tfrac13,\qquad R_1(3)=\tfrac12,\qquad R_1(6)=\tfrac16,
$$
and they sum to $1$: the single contrast $h_1$ is spread across the conductor packets as an honest probability distribution. Where do these fractions come from? Not from anything special about $6$. They are
$$
R_1(d)=\frac{\varphi(d)-\mu(d)}{N},
$$
the Euler totient minus the Möbius function: $R_1(2)=\frac{1-(-1)}{6}=\frac13$, $R_1(3)=\frac{2-(-1)}{6}=\frac12$, $R_1(6)=\frac{2-1}{6}=\frac16$. The two most basic functions of multiplicative number theory, appearing as the conductor profile of the most basic contrast. That is not a coincidence; it is the whole subject of this paper in miniature.

The interior wrote the dictionary between the two rulers — T9's transfer matrix $U$ — and noted that its conductor-block content was "Gauss-sum-like," leaving the precise object for later. The precise object is the **Ramanujan sum**, and once that is seen, every packet weight $R_k(d)$ has a closed form, the two boundary rungs are pure totient and totient-minus-Möbius, and the dimensional axis and the conductor axis are coupled by the canonical arithmetic of divisors. This is the exterior of T9 and T10: the transfer matrix and the Kummer clock are the explicit arithmetic of the boundary between a number field's two *places* — the real radicals and the finite-prime cyclotomics — and the coordinate on that boundary is Ramanujan's.

### 1.1 Why a gate, and why exact {#sec:1-1}

A word on method. The objects ahead — packet weights, field degrees, the overlap of two arithmetics — are exactly the kind a willing mind and a fluent assistant can talk themselves into. So we adopt the grounded-paranoid-delusional discipline (Murillo Montero 2026) as the *structure* of the paper: one ambitious picture with no vote on truth (\hyperref[sec:2]{§2}); the meaning of every outcome fixed before any computation (\hyperref[sec:3]{§3}); and one short program in exact integer and rational arithmetic — no floating point in any decision of sign, vanishing, or membership; floats appear only as explicitly-labelled non-voting witnesses — whose transcript is the record (\hyperref[sec:4]{§4}). The artifact is `P5-settlements.py`. No agreement, however fluent, counts as evidence.

---

## 2. The Star (delusional; no vote on truth) {#sec:2}

> **Fence.** This section is *Historic Fiction*. It chooses what to attempt and in what order. It decides nothing. The only road to a result runs through the gate of \hyperref[sec:3]{§3} and \hyperref[sec:4]{§4}.

Here is the picture to chase. A number field has two kinds of place: the **finite primes** (the $p$-adic, cyclotomic, conductor world) and the **real place** $\{\infty\}$ (the archimedean, radical, $\sqrt[m]{p}$ world). [\heb[P]{פ}3] followed the boundary operator $\partial$ to that real place and proved it is *terminal* — finite-prime data cannot generate it. The Star says: T9's transfer matrix and T10's Kummer clock are the explicit arithmetic of the seam between these two places, viewed twice.

1. **The transfer matrix is the seam, infinitesimally (T9).** $U$ changes rulers between the radical/Helmert basis (real place) and the cyclotomic/character basis (finite primes). It cannot be defined over either field alone; it genuinely lives over the compositum. The fiction: the *content* of $U$ across conductor packets is not arithmetically neutral — it should be the canonical "sum over a conductor class," the Ramanujan sum.

2. **The Kummer clock is the seam, globally (T10).** $K_N^{(m)}=\mathbb Q(\zeta_m,\sqrt[m]{p})$ is literally a finite-prime base ($\zeta_m$) with a real-place tower ($\sqrt[m]{p}$) adjoined. The fiction: its degree should *factor* into a finite-prime part and a real-place part, the latter growing only along the dimensional (prime-rung) axis.

3. **The two places fuse at the Gauss sum.** The radicals and the cyclotomics are not independent: Gauss's $\sqrt{p^*}\in\mathbb Q(\zeta_p)$ means a real square root already lives inside the cyclotomic field. The fiction: this fusion locus — the quadratic Gauss sum — is exactly the $\sqrt q$ scale that [\heb[P]{פ}4] found carrying the function-field critical line.

If true: the apex's two bases are the apex seen at its two places; the dictionary $U$ is coordinatized by Ramanujan sums; the tower $K_N^{(m)}$ is the two places as two factors of one degree; and the one place they share is the Gauss sum. The paper does not argue this. It tests three load-bearing pieces and reports the arithmetic.

---

\clearpage

## 3. Pre-registration (paranoid; meanings fixed before the check) {#sec:3}

Before running `P5-settlements.py`, we fix the meaning of every outcome. The *joint-on-disjoint* branch — both $\mathsf K$ and $\mathsf L$ realized on disjoint sub-structures — is the most informative the three-outcome rule can return.

| Audit | Claim under test | $\mathsf K$ | $\mathsf L$ | Joint-on-disjoint |
|---|---|---|---|---|
| **\heb[P]{פ}transfer** | $U$'s conductor blocks are Ramanujan sums. | $\mathsf K_1$: $R_k(d)$ is the exact Ramanujan-sum form, complete ($\sum_d R_k(d)=1$). $\mathsf K_2$ (sharp): $\{R_k(d)\}_d$ same for all $k$. | $\mathsf L_1$: not the Ramanujan form or $\sum_d\ne1$. $\mathsf L_2$: $k$-dependent. | $k$-dependent, but the last rung is uniform: $R_{N-1}(d)=\varphi(d)/(N{-}1)$. |
| **\heb[P]{פ}Kummer** | The Kummer-clock degree is two places. | $[K_N^{(m)}{:}\mathbb Q]=\varphi(m)\cdot m^{\pi(N)}$, factoring finite-prime $\times$ real-place, growing $\times m$ at prime rungs. | Degree does not factor / grow this way. | — |
| **\heb[P]{פ}overlap** | The radicals and cyclotomics fuse on the real quadratic subfields. | $K_N\cap\mathbb Q(\zeta_N)=\mathbb Q(\sqrt p:\operatorname{cond}\mathbb Q(\sqrt p)\mid N)$; not disjoint. | Linearly disjoint (trivial overlap). | $p\equiv1$ at $p\mid N$; $p\equiv3$ at $4p\mid N$ (the $2$-adic factor $4$); $p{=}2$ at $8\mid N$. |

We run the artifact.

---

## 4. Settlement (grounded; the transcript is the record) {#sec:4}

Each settlement pairs a **Proposition** with the **realized branch**, confirmed by the deterministic artifact. We compute first and explain second.

### 4.1 \heb[P]{פ}transfer — the dictionary is made of Ramanujan sums {#sec:4-1}

Return to the packet weight $R_k(d)=\sum_{c\in H_d}\lvert U_{kc}\rvert^2$, the total Fourier energy that the Helmert rung $h_k$ deposits in conductor packet $H_d$. Expand the square: $\lvert U_{kc}\rvert^2=\frac{1}{Nk(k+1)}\sum_{s,t}(h_k)_s(h_k)_t\,\omega^{c(s-t)}$, and sum over the packet. The only arithmetic is the **packet character sum** $\sum_{c\in H_d}\omega^{c(s-t)}$. Writing $c=(N/d)b$ with $\gcd(b,d)=1$ collapses it to $\sum_{\gcd(b,d)=1}e^{2\pi i b(s-t)/d}=c_d(s-t)$ — Ramanujan's sum, on the nose. So
$$
R_k(d)=\frac{1}{Nk(k+1)}\sum_{s,t}(h_k)_s(h_k)_t\,c_d(s-t).
$$

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (the conductor blocks are Ramanujan sums).** *For the Helmert–Fourier transfer matrix $U$ at level $N$, the conductor-block weights $R_k(d)$ are the Ramanujan-sum quadratic form above, and each rung is a complete distribution over conductors:*
$$
\sum_{d\mid N}R_k(d)=1\qquad(1\le k\le N-1).
$$
*The two boundary rungs have closed forms $R_1(d)=\dfrac{\varphi(d)-\mu(d)}{N}$ and $R_{N-1}(d)=\dfrac{\varphi(d)}{N-1}$ (T9; Ramanujan 1918).*

*Proof.* The packet sum is the Ramanujan sum, as shown. Completeness uses $\sum_{d\mid N}c_d(n)=N\cdot\mathbf 1[N\mid n]$: the double sum collapses to $\frac{1}{k(k+1)}\sum_s(h_k)_s^2=\frac{k+k^2}{k(k+1)}=1$. For $k=1$, $h_1$ is supported on $\{0,1\}$, giving $\frac{1}{2N}(2c_d(0)-2c_d(1))=\frac{\varphi(d)-\mu(d)}{N}$ since $c_d(0)=\varphi(d)$, $c_d(1)=\mu(d)$. For $k=N-1$, T9's last-row uniformity gives $\lvert U_{N-1,c}\rvert^2=1/(N-1)$ for every $c$, so $R_{N-1}(d)=\varphi(d)/(N-1)$ ($\lvert H_d\rvert=\varphi(d)$). $\square$

**Settlement \heb[P]{פ}transfer — $\mathsf K_1$ + joint-on-disjoint, with $\mathsf K_2$ falsified, $\mathsf{[P]}$.** The artifact confirms completeness $\sum_{d\mid N}R_k(d)=1$ for every rung at $N=6,12,30$, and an independent floating-point evaluation of $\sum_{c\in H_d}\lvert U_{kc}\rvert^2$ agrees with the exact Ramanujan form (a non-voting witness that the identity is the matrix's, not just an abstraction). This builds T9's forward door and corrects its label: the content is **Ramanujan**, not Gauss. The honest readings:

*The sharpening is false ($\mathsf K_2$ falsified, retained).* We pre-registered that the distribution $\{R_k(d)\}_d$ is the same for every Helmert rung. It is not: at $N=6$, $R_1=(\tfrac13,\tfrac12,\tfrac16)$ but $R_5=(\tfrac15,\tfrac25,\tfrac25)$ over $(H_2,H_3,H_6)$. Each rung couples to the conductor lattice differently. We keep the dead guess.

*The last rung is clean — but not in the way I guessed (joint-on-disjoint).* The pre-registered joint said the last rung "concentrates in a single packet." It does the opposite: $R_{N-1}(d)=\varphi(d)/(N-1)$ spreads over *all* packets, weighting each by its dimension $\varphi(d)$ — the uniform-amplitude rung of T9's last-row theorem. The guess's instinct (the last rung is special) was right; its content (concentration) was wrong. The actual closed form is reported, the guess retained as written.

### 4.2 \heb[P]{פ}Kummer — the degree is two places {#sec:4-2}

Climb from the transfer matrix to the field tower. The Kummer clock $K_N^{(m)}=\mathbb Q(\zeta_m,\sqrt[m]{2},\sqrt[m]{3},\dots,\sqrt[m]{p_{\pi(N)}})$ adjoins the $m$-th roots of the primes up to $N$ to the cyclotomic base $\mathbb Q(\zeta_m)$.

\hypertarget{stmt:4-2}{}
**Proposition 4.2 (the Kummer-clock degree factors into two places).** *The generic degree is*
$$
[K_N^{(m)}:\mathbb Q]=\underbrace{\varphi(m)}_{\text{finite-prime gauge}}\cdot\underbrace{m^{\pi(N)}}_{\text{real-place tower}},
$$
*the cyclotomic base of degree $\varphi(m)$ times one factor of $m$ per adjoined prime root; the real-place tower grows by exactly $m$ at each prime rung $N$ and is unchanged at composite $N$. For $m=2$ this is the radical clock $[K_N:\mathbb Q]=2^{\pi(N)}$ of T4, exact and unconditional (Murillo Montero 2026, T4; Lang, Kummer theory).*

*Proof.* $[\mathbb Q(\zeta_m):\mathbb Q]=\varphi(m)$; adjoining each $\sqrt[m]{p}$ multiplies the degree by $m$ when the Kummer extensions are independent, which holds unconditionally at $m=2$ (multiquadratic independence of distinct primes) and generically for $m\ge3$. The tower factor $m^{\pi(N)}$ increases iff $\pi(N)$ does, i.e. iff $N$ is prime. $\square$

**Settlement \heb[P]{פ}Kummer — $\mathsf K$, $\mathsf{[P]}$ at $m=2$ / $\mathsf{[A]}$ for $m\ge3$.** The artifact tabulates $\varphi(m)\cdot m^{\pi(N)}$ for $m\in\{2,3,4,6\}$ and $N\le12$, confirming the factorization and the prime-rung growth law ($\times m$ at each prime, $\times1$ at composites) exactly. The exterior content is the *split*: the degree is a finite-prime gauge factor $\varphi(m)$, fixed by the gauge $m$, times a real-place tower $m^{\pi(N)}$ that lives entirely on the dimensional (prime) axis — P3's two places as the two factors of one number. One honest caution: the *equality* of $\varphi(m)\cdot m^{\pi(N)}$ with the true field degree is unconditional only at $m=2$; for $m\ge3$ it is the generic degree, and the precise independence criterion (the unbuilt part of T10's claim 5) is carried at $\mathsf{[A]}$, not settled here.

### 4.3 \heb[P]{פ}overlap — the two places fuse on the real quadratic subfields {#sec:4-3}

Are the two arithmetics independent? The transfer matrix lives over $K_N\cdot\mathbb Q(\zeta_N)$; if the real field $K_N$ and the cyclotomic field $\mathbb Q(\zeta_N)$ were linearly disjoint, the compositum would simply be their product and the two places would never touch. They are *not* disjoint — but the overlap is governed by a *conductor* criterion, not the Gauss sum the first draft of this settlement mistook for it (\hyperref[sec:6]{§6.3}).

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (the radicals meet the cyclotomics by the conductor criterion).** *A real radical $\sqrt p$ lies in $\mathbb Q(\zeta_N)$ iff the conductor of $\mathbb Q(\sqrt p)$ divides $N$, where $\operatorname{cond}\mathbb Q(\sqrt p)=8$ for $p=2$, $\ p$ for $p\equiv1\ (\mathrm{mod}\ 4)$, and $4p$ for $p\equiv3\ (\mathrm{mod}\ 4)$ (conductor–discriminant theorem). Hence $K_N$ and $\mathbb Q(\zeta_N)$ are not linearly disjoint: their intersection is the real multiquadratic field $\mathbb Q\bigl(\sqrt p:p\le N,\ \operatorname{cond}\mathbb Q(\sqrt p)\mid N\bigr)$ — the real quadratic subfields of $\mathbb Q(\zeta_N)$ that $K_N$ carries (Gauss; Washington, Cyclotomic Fields).*

*Proof.* By Kronecker–Weber for quadratic fields, $\mathbb Q(\sqrt p)\subseteq\mathbb Q(\zeta_N)$ iff its conductor — the absolute value of its discriminant, namely $p$ for $p\equiv1$, $4p$ for $p\equiv3$, and $8$ for $p=2$ — divides $N$. Concretely, for $p\equiv1$ the Gauss sum gives $\sqrt p=\sqrt{p^*}\in\mathbb Q(\zeta_p)$; for $p\equiv3$, $\sqrt p=\sqrt{-1}\cdot\sqrt{-p}\in\mathbb Q(\zeta_4)\mathbb Q(\zeta_p)=\mathbb Q(\zeta_{4p})$, so $\sqrt p\in\mathbb Q(\zeta_N)$ iff $4p\mid N$. $\square$

**Settlement \heb[P]{פ}overlap — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$ (criterion corrected).** The artifact reports the real overlap for $N\in\{5,8,12,15,24,30\}$ by the conductor criterion: $\sqrt5$ at $N=5,15,30$ ($\operatorname{cond}5$), $\sqrt2$ at $N=8$ ($\operatorname{cond}8$), and — the case to watch — $\sqrt3$ at $N=12$, since $\operatorname{cond}\mathbb Q(\sqrt3)=4\cdot3=12\mid12$ and $\sqrt3=\zeta_{12}+\zeta_{12}^{-1}=2\cos\tfrac{\pi}{6}$ is *real* in $\mathbb Q(\zeta_{12})$. So $K_{12}\cap\mathbb Q(\zeta_{12})=\mathbb Q(\sqrt3)=\mathbb Q(\zeta_{12})^+$ — **not** trivial. The two arithmetics fuse on the real quadratic subfields, and the fusion still passes through the $\sqrt q$ scale [\heb[P]{פ}4]'s \heb[P]{פ}bridge found. The joint-on-disjoint is a parity *distinction*, but not "$p\equiv1$ only": the $p\equiv1$ primes fuse at $p\mid N$, the $p\equiv3$ primes at $4p\mid N$ — they require the extra $2$-adic factor $4$, the prime $2$'s ramification, tying to [\heb[P]{פ}4]'s $2$-adic anomaly; $p=2$ enters at $8\mid N$. The first draft tracked the Gauss sum $\sqrt{p^*}$ (imaginary for $p\equiv3$) and wrongly called $N=12$ trivial — the gate passed it because the artifact encoded the wrong criterion (\hyperref[sec:6]{§6.3}).

---

## 5. The synthesis (earned) {#sec:5}

We may now restate the Star as a result, at the tier each piece supports.

\hypertarget{stmt:5-1}{}
**Proposition 5.1 (two places, three boundary objects — $\mathsf{[P]}$ for the pieces, $\mathsf{[A]}$ for the single object).** *The three settlements establish, deterministically and at $\mathsf{[P]}$:*

- *(coordinate) the transfer matrix's conductor-block content is the Ramanujan-sum distribution $R_k(d)$, complete over conductors, with totient/Möbius closed forms at the boundary rungs (\hyperlink{stmt:4-1}{Proposition~4.1});*
- *(tower) the Kummer-clock degree factors into a finite-prime gauge $\varphi(m)$ and a real-place tower $m^{\pi(N)}$ growing at prime rungs (\hyperlink{stmt:4-2}{Proposition~4.2}; unconditional at $m=2$);*
- *(fusion) the radical and cyclotomic fields meet on the real quadratic subfields of $\mathbb Q(\zeta_N)$, by the conductor criterion (\hyperlink{stmt:4-3}{Proposition~4.3}).*

*That T9's transfer matrix and T10's Kummer clock are two faces of one boundary — the seam between the real place (radicals) and the finite primes (cyclotomics) that [\heb[P]{פ}3] proved terminal — is asserted at $\mathsf{[A]}$. The Ramanujan coordinate, the two-factor degree, and the Gauss-sum fusion are its three exact shadows; the single-object account is the cornered, unbuilt obligation.*

The honest seam is the point. Three boundary facts are settled by exact arithmetic — one of them, the Ramanujan identification, a theorem in no single interior paper; their unification into one place-theoretic object is carried at its true tier. As in [\heb[P]{פ}4]'s conductor-lattice bridge, the new content lives precisely where two interior faces are forced to meet — here, the dimensional (radical) axis and the conductor (cyclotomic) axis, coupled by Ramanujan sums.

---

## 6. The method's own record {#sec:6}

A history of only confirmations has been performed, not tested. We record this session honestly.

**6.1 One genuine falsification, one corrected guess.** Of the three audits, \heb[P]{פ}Kummer and \heb[P]{פ}overlap returned $\mathsf K$ — re-derivations of classical facts (the Kummer degree, the radical–cyclotomic overlap) read through the two-places lens, their worth the exterior framing, not new theorems. \heb[P]{פ}transfer is the one with new content, and it is also the one that was genuinely at risk twice. Its sharp claim $\mathsf K_2$ — that the conductor distribution is the same for every Helmert rung — was **falsified** by the exact values ($R_1\ne R_5$ at $N=6$). And its pre-registered *joint* guessed the wrong shape for the last rung: "concentrates in a single packet," where the truth is the totient spread $\varphi(d)/(N-1)$. We keep both the dead sharpening and the wrong-shaped guess, beside the closed form that replaced it. A settlement that confirmed every prediction would have predicted nothing falsifiable.

**6.2 What is re-read and what is new.** \heb[P]{פ}transfer's Ramanujan identification (\hyperlink{stmt:4-1}{Proposition~4.1}) is in no interior paper: T9 named the content "Gauss-sum-like" and deferred it; the precise object is the Ramanujan sum, and the boundary-rung closed forms $(\varphi-\mu)/N$ and $\varphi/(N-1)$ are consequences. \heb[P]{פ}Kummer and \heb[P]{פ}overlap re-derive T10/T4 and the conductor criterion through the place-theoretic reading. The honest tally: two boundary re-readings and one boundary theorem — the same shape as [\heb[P]{פ}4].

**6.3 An error the gate did not catch, corrected.** \heb[P]{פ}overlap as first settled was *wrong*, and the wrongness is the instructive part. The first draft asked whether the quadratic *Gauss sum* $\sqrt{p^*}$ is real — true iff $p\equiv1\ (\mathrm{mod}\ 4)$ — and concluded the real overlap at $N=12$ is trivial. But the object that actually lives in $K_N$ is the real *radical* $\sqrt p$, a different element: for $p\equiv3$ it has conductor $4p$, and $\sqrt3=\zeta_{12}+\zeta_{12}^{-1}$ is real in $\mathbb Q(\zeta_{12})$, so $K_{12}\cap\mathbb Q(\zeta_{12})=\mathbb Q(\sqrt3)$ — *not* trivial, at the very $N=12$ the settlement had spotlighted. The deterministic gate passed the false claim as $\mathsf{[P]}$ because the artifact and the prose agreed: **the gate certifies that the computation matches the words, not that the computation asks the right question.** \heb[P]{פ}transfer's $\mathsf K_2$ was a falsifier the gate *caught*; this is one it structurally could not, because no falsifier was pre-registered against the *criterion* itself. We record it as the method's sharpest limitation; the correction (the conductor criterion, \hyperlink{stmt:4-3}{Proposition~4.3}) replaces it, and the settlement transcript retains the failure.

\heb[P]{פ}transfer's $\mathsf K_2$ falsification and \heb[P]{פ}overlap's criterion correction (§6.3) change realized branches; the rest are notes on method.

---

## 7. Safe and unsafe statements {#sec:7}

**Safe (this paper asserts):**

- $\mathsf{[P]}$ The transfer matrix's conductor-block weights are the Ramanujan-sum distribution $R_k(d)$, complete over conductors, with $R_1(d)=(\varphi(d)-\mu(d))/N$ and $R_{N-1}(d)=\varphi(d)/(N-1)$ (\hyperlink{stmt:4-1}{Proposition~4.1}; settlement \heb[P]{פ}transfer) — a statement in no interior paper.
- $\mathsf{[P]}$ The Kummer-clock degree is $\varphi(m)\cdot m^{\pi(N)}$, a finite-prime gauge times a real-place tower; unconditional at $m=2$ (\hyperlink{stmt:4-2}{Proposition~4.2}; settlement \heb[P]{פ}Kummer).
- $\mathsf{[P]}$ The radical and cyclotomic fields fuse on the real quadratic subfields of $\mathbb Q(\zeta_N)$ by the conductor criterion ($p\equiv1$ at $p\mid N$, $p\equiv3$ at $4p\mid N$, $p{=}2$ at $8\mid N$); e.g. $K_{12}\cap\mathbb Q(\zeta_{12})=\mathbb Q(\sqrt3)$ (\hyperlink{stmt:4-3}{Proposition~4.3}; settlement \heb[P]{פ}overlap).
- $\mathsf{[A]}$ T9's transfer matrix and T10's Kummer clock are two faces of the real-place / finite-prime seam (\hyperlink{stmt:5-1}{Proposition~5.1}). Here "real place" means the totally-real *finite algebraic* field $K_N=\mathbb Q(\sqrt p)$ — exact, hence $\mathsf{[P]}$-settleable — not the analytic archimedean place of [\heb[P]{פ}3]/[\heb[P]{פ}6]; the link between the two is heuristic, held at $\mathsf{[A]}$.

**Unsafe (this paper does NOT assert):**

- That the rung distribution $\{R_k(d)\}_d$ is rung-independent. It is not — the sharpening was pre-registered and *falsified*.
- That the Kummer-clock degree $\varphi(m)\cdot m^{\pi(N)}$ equals the true field degree for $m\ge3$. That requires the independence criterion T10 left open; it is $\mathsf{[A]}$. Only $m=2$ is unconditional.
- That the radical–cyclotomic fusion says anything about $\zeta$ or GRH. It locates where two finite arithmetics overlap; the GRH thread is owned by the function-field side of [\heb[P]{פ}4] and held at $\mathsf{[C]}$.
- That P5's "real place" is the analytic archimedean place. $K_N=\mathbb Q(\sqrt p)$ is a totally-real *finite algebraic* field, exact in every part; the genuine archimedean place — the $\Gamma$-factor, the moment wall [\heb[P]{פ}6] proves terminal — is *not* touched here. The "two places" is a finite algebraic seam in place-theoretic dress; the link is heuristic, $\mathsf{[A]}$.
- That the single-object "two places, one apex" account is proven. It is $\mathsf{[A]}$; the three exact shadows are settled, the unification is not.
- That this paper is important or field-defining. By the firewall such a claim would stand above its evidence, and the method forbids its author from issuing it.

---

## 8. Forward door: the boundary's own coordinate (calibrated, $\mathsf{[C]}$) {#sec:8}

The Ramanujan sum is not an accident of the transfer matrix; it is the canonical Fourier coordinate of the divisor lattice, and the divisor lattice is where the finite-prime place organizes itself. That the apex's change-of-basis between its real-radical and finite-prime rulers is coordinatized by Ramanujan sums suggests the boundary $\partial$ of the \heb[P]{פ}-series has a natural *harmonic analysis* — a Ramanujan–Fourier expansion on the conductor lattice — into which the curvature, the leak, and the fork-width of the earlier papers should all expand.

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (forward door — calibrated, not proved).** *The boundary objects of the \heb[P]{פ}-series — the conductor-fusion leak (\heb[P]{פ}3), the fork-width class function (\heb[P]{פ}4), the transfer-matrix blocks (\heb[P]{פ}5) — admit a common Ramanujan–Fourier expansion on the conductor lattice, with the real place entering as the $d=\infty$ limit that the finite sums approach but never reach (the terminal boundary of [\heb[P]{פ}3]).* Held with calibrated faith; built toward, not claimed.

---

## 9. Coda {#sec:9}

We began with one contrast on a six-hour clock — first minus second — and watched it fall across the conductor packets in the proportions $(\varphi(d)-\mu(d))/N$, the totient and the Möbius function keeping the books. We end with two arithmetics, the real radicals and the cyclotomic roots, that looked independent and turned out to share exactly one room: the quadratic Gauss sum, the same scale on which the function-field critical line sits. In between, the dictionary the interior wrote between its two rulers turned out to be written in Ramanujan's sums, and the tower over the seam turned out to factor into the two places it joins.

T9 said the apex has two bases. T10 said the gauge has a Kummer tower. From the boundary, [\heb[P]{פ}5] says they are the same seam seen twice — the place where a number field's real and finite arithmetics meet — and the boundary keeps its books in the most classical hand there is: $c_d(n)$, the Ramanujan sum, $\varphi$ and $\mu$ at the edges, the Gauss sum at the join. The part you discard does not vanish; it is coordinatized, and the coordinate was Ramanujan's all along.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) under the grounded-paranoid-delusional discipline this paper applies to itself: AI partners generated candidates, enumerated falsifiers, and executed the deterministic settlement artifact, but no fluent agreement was treated as evidence. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## Reproducibility {#sec:reproducibility}

The numbers of \hyperref[sec:4]{§4} are produced by `P5-settlements.py`, a deterministic, exact-arithmetic (integer / `Fraction`) script with no seeds and no floating point in any sign, vanishing, or membership decision (a single floating-point evaluation appears only as an explicitly-labelled non-voting cross-check of the Ramanujan identity); its full transcript (`P5-settlements.transcript.txt`) is archived alongside, and re-running reproduces it identically (UTF-8 output is forced so the transcript is regenerable on any locale).

## References {#sec:references}

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis.)

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Companion methodology preprint (draft v1).

Murillo Montero, L. (2026). *\heb[P]{פ}1 — From the Boundary: The Exterior of Identifying 3*; *\heb[P]{פ}2 — From the Boundary: The Gauge Trilogy at the Tropical Edge*; *\heb[P]{פ}3 — From the Boundary: The Leak, the Curvature, and the Real Place*; *\heb[P]{פ}4 — From the Boundary: The Quantum Face, the Units, and the Proven Critical Line.* Companion preprints (the exterior \heb[P]{פ}-series; [\heb[P]{פ}3] proves the real place terminal, [\heb[P]{פ}4] the conductor-lattice fork-width bridge and the $\sqrt q$ scale).

Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier–Mellin Simplex.* Zenodo, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (The character basis; conductor packets; the $N=6$ transfer-matrix worked example.)

Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo, DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049). (Conductor packets $H_d$.)

Murillo Montero, L. (2026). *[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — The Helmert Simplicial Residue Ladder.* Zenodo, DOI [10.5281/zenodo.20383504](https://doi.org/10.5281/zenodo.20383504). (The Helmert basis; the multiquadratic radical clock $K_N$.)

Murillo Montero, L. (2026). *T9 — The Helmert–Fourier Transfer Matrix*; *T10 — The Kummer Clock and the $m$-Power Gauge Hierarchy.* Companion manuscripts (the transfer matrix $U$ and its conductor-block forward door; the Kummer clock $K_N^{(m)}$).

Ramanujan, S. (1918). *On certain trigonometrical sums and their applications in the theory of numbers.* Transactions of the Cambridge Philosophical Society **22**, 259–276. (The sums $c_d(n)$ and Hölder's evaluation.)

Washington, L. C. (1997). *Introduction to Cyclotomic Fields*, 2nd ed. Graduate Texts in Mathematics **83**. Springer. (Gauss sums; $\sqrt{p^*}\in\mathbb Q(\zeta_p)$; Kummer theory of the radical and cyclotomic fields.)
