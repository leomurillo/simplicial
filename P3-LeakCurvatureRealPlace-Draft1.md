# \heb[P]{פ}3 — From the Boundary: The Leak, the Curvature, and the Real Place

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 29, 2026*

## Abstract

**Situation.** Five interior papers build a finite, exact field theory on the categorical simplex. T11 (Apex Vertex Calculus) gives the Feynman rule of the apex — an $n$-leg vertex fires iff the character indices sum to zero modulo $N$ — and proves that a *projected* sector closes iff it is closed under conductor fusion. T12 (Finite Apex Determinacy) proves the "infinite" moment/cumulant tower is the finite algebra $\mathbb R[t]/(P_x)$. T13 (Exact Simplicial Renormalization) integrates out the discarded sector and reads the renormalization-group flow as boundary adjunction. T14 (Projected Flatness) proves that curvature, the $\beta$-function, the Schur correction, and the Noether defect are one obstruction. T15 (Finite-to-Archimedean Completion) finds the real place as the terminal boundary, and names the **smooth primorial** \heb[P]{פ}.

**Gap.** Every one of these papers is, in its own words, a theory of a *boundary* — "leakage," a "boundary source," "boundary curvature," a "terminal archimedean boundary." But each names that boundary from the inside, as the obstruction to a projection it would rather not have made. The exterior question is the opposite one: take the boundary as the primary object, and ask what the interior's five obstructions look like when you do.

**Action.** We answer it under the grounded-paranoid-delusional method (Murillo Montero 2026): a fenced *Star* with no vote on truth (\hyperref[sec:2]{§2}); three — here, four — matched-pair falsifiers pre-registered before any check (\hyperref[sec:3]{§3}); and a single deterministic, exact-arithmetic artifact (`P3-settlements.py`) anchored to T11–T15's own objects (\hyperref[sec:4]{§4}). The exposition is deliberately Eulerian: we lead with the smallest concrete number, compute it by hand-checkable steps, and let the theorem arrive as the explanation of what we have already seen.

**Result.** Four settlements. **\heb[P]{פ}11 ($\mathsf K$, joint).** At $N=6$, multiply three characters drawn from the non-unit sector $H_2\oplus H_3$: the product lands, when it leaves the sector at all, *exactly* in the unit-indexed packet $H_6$. The leak is the conductor-fusion boundary $\partial_3\{2,3\}=\{6\}$ — and it is parity-asymmetric (the $3$-axis cancels to nothing, the $2$-axis is parity-locked). **\heb[P]{פ}12 ($\mathsf K$).** The tower that looks infinite has Hankel rank $3$ and obeys an exact degree-$3$ recurrence: it *is* $\mathbb R[t]/(P_x)$. **\heb[P]{פ}14 ($\mathsf K$, joint).** The curvature defect, the renormalization source, and the Noether defect are supported on the *same* set $\{1,5\}=H_6$ we already found — one boundary, five interior names. **\heb[P]{פ}15 ($\mathsf K$).** Euler completed the factorial with his $\Gamma$ because the factorial is a moment sequence; the primorial is *not* — its Hankel determinant $D_3=-787680<0$ — so the real place must be adjoined from outside, and the constant $1/2\pi$ in \heb[P]{פ} is that adjunction.

**Harvest.** One operator, $\partial$, runs through all five papers, climbing: from the conductor packets (T11), through the finite order algebra (T12) and the renormalization flow (T13) to the projected geometry (T14), and out to the real place $\{\infty\}$ (T15), where it meets the completed $L$-function and the smooth primorial \heb[P]{פ} — the scalar on which the interior, working from the centre, had already written this series' own glyph. The unification of the five interior obstructions into this one climbing $\partial$ is carried at $\mathsf{[A]}$; the GRH thread it points to is held at $\mathsf{[C]}$, named and not claimed.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
Suppose you build a theory out of a few simple pieces, then throw some of the pieces away and keep only a part. The kept part no longer behaves simply: forces appear from nowhere, conservation laws fail by a little, the geometry looks curved. Five companion papers showed, on a finite arithmetic model, that all of these ``corrections'' are the same thing wearing different costumes --- they are exactly the pieces you threw away, leaking back in. This paper takes that leak as the real subject. We work the smallest example by hand (three characters on the six-hour clock), watch where the product spills, and find one boundary doing all the work. We then chase that boundary up a ladder --- packets, orders, flows, curvature --- until it walks off the finite arithmetic entirely and lands on the real line, where it becomes the gamma factor Euler would recognise: the very ingredient the factorial has and the primorial provably lacks. Every number below is produced by a short exact-arithmetic program whose printout, not any sentence here, is the verdict.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| $N$ | Modulus; the outcome labels are $\mathbb Z/N$. |
| $\chi_a$ | Additive character $\chi_a(s)=e^{2\pi i a s/N}$; index $a\in\mathbb Z/N$. |
| $\operatorname{cond}(a)$ | Conductor $N/\gcd(a,N)$ for $a\ne0$; $\operatorname{cond}(0)=1$ (T3). |
| $H_d$ | Conductor-$d$ packet $\operatorname{span}\{\chi_a:\operatorname{cond}(a)=d\}$; $\dim_{\mathbb C}H_d=\varphi(d)$. |
| $H_S$ | $\bigoplus_{d\in S}H_d$, for a set $S$ of nontrivial divisors; $\Pi_S$ its projection. |
| $V_n$ | Apex $n$-leg vertex $V_n(a_1,\dots,a_n;c)=\mathbf 1[a_1+\cdots+a_n\equiv c]$ (T11). |
| $\operatorname{Fuse}_n,\ \partial_n S$ | $n$-fold conductor fusion and its **boundary** $\operatorname{Fuse}_n(S)\setminus(S\cup\{1\})$ (T11). |
| $\operatorname{Cl}_n(S)$ | Minimal $n$-fusion-closed set containing $S$ (T11). |
| $\lambda_j,\ P_x$ | Distinct centered-ledger levels; closure polynomial $P_x(t)=\prod_j(t-\lambda_j)$ (T12). |
| $\mu_n$ | Moment $\mu_n=\sum_j W_j\lambda_j^n$; Hankel matrix $(\mu_{i+j})$ (T12). |
| $D_k$ | Hankel determinant $\det(s_{i+j})_{0\le i,j\le k}$ of a scalar sequence $(s_n)$. |
| \heb[P]{פ}$(z)$ | Smooth primorial $e^{\operatorname{Li}^{-1}(z)}/2\pi$ (T15, T33); $\operatorname{Li}^{-1}$ inverts $\int_2^x dt/\log t$. |
| $\Gamma_\infty$ | Archimedean factor $\pi^{-(s+\varepsilon)/2}\Gamma((s+\varepsilon)/2)$ — the real-place boundary (T15). |
| $\mathsf{[P]/[A]/[C]}$ | Tiers: proven / structural-pending-named-audit / conjectural-reduced. |
| $\mathsf K,\mathsf L$ | Matched-pair branches; *joint-on-disjoint* when both fire on disjoint sub-structures. |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| GPD | Grounded-paranoid-delusional (the method of Murillo Montero 2026). |
| RG | Renormalization group. |
| AC | Amari–Chentsov (cubic tensor). |
| GRH | Generalized Riemann Hypothesis (forward-door north star, \hyperref[sec:8]{§8}). |
| moment seq. | A sequence $(s_n)$ with $s_n=\int t^n\,d\mu$ for a positive measure $\mu$ (Hankel determinants $\ge0$). |

---

## 1. A small puzzle, and a gate {#sec:1}

Let us begin where Euler would: with a number too small to hide anything.

Work on the six-hour clock, $N=6$. Its nonzero Fourier characters $\chi_1,\dots,\chi_5$ sort into three families by their conductor — the smallest clock on which the character is already periodic:
$$
H_2=\{\chi_3\},\qquad H_3=\{\chi_2,\chi_4\},\qquad H_6=\{\chi_1,\chi_5\}.
$$
Now keep only the first two families, $H_2\oplus H_3$, and discard $H_6$. This is an honest thing to want: $H_6$ is indexed by the *units* $\{1,5\}=(\mathbb Z/6)^\times$, and one often wishes to model only the "structured" non-unit part. The question is innocent: **if I multiply three characters from the part I kept, does the product stay in the part I kept?**

Multiply $\chi_2\cdot\chi_2\cdot\chi_3$. Characters multiply by adding indices, so this is $\chi_{2+2+3}=\chi_7=\chi_1$. But $\chi_1$ is in $H_6$ — the family we threw away. The product *leaked*. Try $\chi_3\cdot\chi_4\cdot\chi_4=\chi_{11}=\chi_5$: again $H_6$. Try a few more and a pattern asserts itself: when the product leaves $H_2\oplus H_3$ at all, it lands in $H_6$, never anywhere else.

This is the whole subject of the paper, in miniature. The interior series ([\heb{ל}11], …, [\heb{ל}15]) discovered that this leak is universal, exact, and the same object that, elsewhere, *looks* like curvature, like a running coupling, like a failed conservation law, and finally like the gamma factor of a completed $L$-function. Five faces; one boundary. The exterior ([\heb[P]{פ}1], [\heb[P]{פ}2]) is built to take that boundary as the primary thing, so this is its natural third chapter.

### 1.1 Why a gate, and why exact {#sec:1-1}

A word on method before any claim. The objects ahead — leaks, curvatures, the sign of a determinant attached to the primes — are exactly the kind a willing mind and a fluent assistant can talk themselves into. So we adopt, as the *structure* of the paper, the grounded-paranoid-delusional discipline (Murillo Montero 2026): we permit one ambitious unifying picture but give it no vote on truth (\hyperref[sec:2]{§2}); we write down, before computing anything, what each possible outcome will be taken to mean (\hyperref[sec:3]{§3}); and we settle every question with one short program in exact integer or rational arithmetic — no floating point in any decision of sign, vanishing, or membership — whose transcript, not our prose about it, is the record (\hyperref[sec:4]{§4}). The artifact is `P3-settlements.py`; everything numerical below is its output. No agreement, however fluent, counts as evidence.

---

## 2. The Star (delusional; no vote on truth) {#sec:2}

> **Fence.** This section is *Historic Fiction*. It chooses what to attempt and in what order. It decides nothing. The only road from here to a result runs through the gate of \hyperref[sec:3]{§§3}–4.

Here is the picture to chase. There is one operator, $\partial$, the boundary the interior keeps meeting, and the five papers are five *altitudes* of it:

1. **Packets (T11).** $\partial$ is the conductor-fusion boundary $\partial_nS$: the set of packets a projected $n$-vertex leaks into. Closure means $\partial_nS=\varnothing$.
2. **Orders (T12).** Climb to the order axis. The tower of moments looks like an infinite reservoir; in fact $\partial$ has quotiented it down to the finite algebra $\mathbb R[t]/(P_x)$. "Higher order" is the part $\partial$ has already discarded.
3. **Flow (T13).** Let the retained sector grow. The renormalization-group flow is nothing but *adjoining* $\partial$ until it is empty; the fixed points are the fusion-closed sectors.
4. **Geometry (T14).** Look at the kept sector as a curved space. Its curvature, its $\beta$-function, its Noether defect are all supported on the *same* $\partial$. Curvature is the shadow a flat thing casts when seen through a boundary it has crossed.
5. **Place (T15).** Climb past every finite modulus, along the primorials $N_k=2\cdot3\cdot5\cdots$. One boundary refuses to be a finite packet: the **real place** $\{\infty\}$. The gamma factor is $\partial$ at infinity, and its scalar shadow is the smooth primorial \heb[P]{פ}.

The fiction is that these are one object. If true: *the boundary the interior calls leakage, curvature, $\beta$, and Noether defect is a single $\partial$ that climbs from the conductor lattice to the real line, and the program's zeros live where it lands.* The rest of the paper does not argue this. It tests four load-bearing pieces of it and reports the arithmetic.

---

\clearpage

## 3. Pre-registration (paranoid; meanings fixed before the check) {#sec:3}

Before running `P3-settlements.py`, we fix the meaning of every outcome. Each branch is a real, reportable result; the *joint-on-disjoint* branch — both $\mathsf K$ and $\mathsf L$ realized on disjoint sub-structures — is the most informative the three-outcome rule can return.

| Audit | Claim under test | $\mathsf K$ | $\mathsf L$ | Joint-on-disjoint |
|---|---|---|---|---|
| **\heb[P]{פ}11** | The leak is the fusion boundary $\partial_3 S$. | At $N=6$, $\partial_3\{2,3\}=\{6\}$ exactly. | $\partial_3\{2,3\}\ne\{6\}$ (empty, or other packets). | $\{6\}$, but parity-asymmetric: the $2$-axis is parity-locked, the $3$-axis cancels freely. |
| **\heb[P]{פ}12** | The tower is the finite algebra $\mathbb R[t]/(P_x)$. | Hankel rank $=r$ (=\#levels) and the exact degree-$r$ recurrence holds. | Rank grows past $r$; no finite recurrence. | — |
| **\heb[P]{פ}14** | Curvature $=$ leak $=$ Noether defect. | The cubic curvature support is exactly $\{1,5\}=H_6=\partial_3\{2,3\}$. | The supports differ. | $\{1,5\}$, reached only by specific witness multisets. |
| **\heb[P]{פ}15** | The real place is not a finite packet. | $D_3(\text{primorial})<0$ (primorial not a moment sequence); factorial all $D_k>0$. | $D_3\ge0$ (primorial is a moment sequence; the real place self-completes). | — |

We run the artifact.

---

## 4. Settlement (grounded; the transcript is the record) {#sec:4}

Each settlement pairs a **Proposition** (proved) with the **realized branch**, confirmed by the deterministic artifact. We compute first and explain second, in the Eulerian manner.

### 4.1 \heb[P]{פ}11 — the leak, and where it goes {#sec:4-1}

Return to the six-hour clock. We kept $H_2\oplus H_3$, i.e. the indices $\{2,3,4\}$. Run over *every* ordered triple $(a,b,c)$ from $\{2,3,4\}$, form $a+b+c \bmod 6$, and ask its conductor. The artifact does this and reports: the outputs that leave $H_2\oplus H_3$ are exactly the indices $\{1,5\}$, both of conductor $6$. So
$$
\partial_3\{2,3\}=\{6\}.
$$
Why $6$ and nothing else? Because the product index is a *sum*, and a sum of indices of conductor $2$ or $3$ can have conductor $1,2,3$, or $6$; the closed outputs ($1,2,3$) are kept or are pure gauge, and only the leak ($6$) is new. That is the content of:

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (the leak is the fusion boundary).** *For any modulus $N$, sector $S$, and order $n$, the universal residual support of the projected vertex $(1-\Pi_S-\Pi_1)\,V_n|_{H_S^{\otimes n}}$ is the conductor-fusion boundary $\partial_nS=\operatorname{Fuse}_n(S)\setminus(S\cup\{1\})$ ([\heb{ל}11] Thm 4.1); it is empty iff $S$ is fusion-closed, and the smallest closed sector containing $H_S$ is $H_{\operatorname{Cl}_n(S)}$. At $N=6$, $\partial_3\{2,3\}=\{6\}$ and $\operatorname{Cl}_3\{2,3\}=\{2,3,6\}$.*

*Proof.* A product of $n$ characters with indices $a_i$ is the single character $\chi_{a_1+\cdots+a_n}$; its conductor ranges over $\operatorname{Fuse}_n(\{\operatorname{cond}(a_i)\})$. Outputs in $S\cup\{1\}$ stay in $H_S\oplus H_1$; the rest, by definition $\partial_nS$, do not, and each is attained by choosing the indices realizing it ([\heb{ל}11] Thm 3.1, 4.1). The $N=6$ value is the computation above. $\square$

Now the pretty part — the **parity asymmetry**, which the binary "it leaks to $\{6\}$" would have hidden. Look at the two pure axes. Three copies of the conductor-$3$ index: $\chi_2\cdot\chi_2\cdot\chi_2=\chi_6=\chi_0$ — they *cancel to nothing*, the trivial gauge packet. Three copies of the conductor-$2$ index: $\chi_3\cdot\chi_3\cdot\chi_3=\chi_9=\chi_3$ — they *stay put*, conductor $2$. Both pure axes are cubically self-closed ($\partial_3\{2\}=\partial_3\{3\}=\varnothing$), but by opposite mechanisms: at the odd prime $3$ a sum of three units can cancel freely, while at the prime $2$ a sum of an *odd* number of odd units is odd and cannot — parity locks it. This is exactly [\heb{ל}11] Thm 3.1's special role for $p=2$, and it is why, on the cross-prime clock $N=6$, the $2$-axis and the $3$-axis are not mirror images.

**Settlement \heb[P]{פ}11 — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** The artifact confirms $\partial_3\{2,3\}=\{6\}$, $\operatorname{Cl}_3\{2,3\}=\{2,3,6\}$, and the parity asymmetry ($\chi_2^{\,3}\to$ conductor $1$, $\chi_3^{\,3}\to$ conductor $2$). One honest caution, also computed: the *single-packet* leak is special to $N=6$. At $N=12$, $\partial_3\{3,4\}=\{6,12\}$; at $N=30$, $\partial_3\{2,3,5\}=\{6,10,15,30\}$. In general the boundary is a *set* of packets, not one — the clean $N=6$ slogan is the cross-prime minimum, not the rule.

### 4.2 \heb[P]{פ}12 — the tower that only looks infinite {#sec:4-2}

Take a centered ledger with a handful of distinct values — say $y=(-1,-1,0,2)$, whose levels are $\{-1,0,2\}$, three of them. Its moments $\mu_n=\frac14\sum_s y_s^{\,n}=\tfrac12(-1)^n+\tfrac14\cdot0^n+\tfrac14\cdot2^n$ form an endless sequence $1,0,\tfrac32,\tfrac32,\tfrac92,\dots$. It *looks* like an infinite reservoir of independent numbers. Count, as Euler would, how much is really there. Stack the moments into Hankel matrices $(\mu_{i+j})$ and measure their rank: the artifact reports $1,2,3,3,3,3$ — the rank stops growing at $3$. And the moments obey, exactly, a three-term recurrence:
$$
\mu_{n+3}=\mu_{n+2}+2\,\mu_{n+1}\qquad(\text{residuals all }0).
$$
Three numbers of information, not infinitely many. The reason is algebra, not luck.

\hypertarget{stmt:4-2}{}
**Proposition 4.2 (the order axis is finite).** *If the centered ledger takes $r$ distinct values $\lambda_1,\dots,\lambda_r$, then with $P_x(t)=\prod_j(t-\lambda_j)$ the entire apex tower is the finite quotient algebra $\mathbb R[t]/(P_x)$ ([\heb{ל}12] Thm 6): the moment Hankel matrices have rank exactly $r$, and $\mu_{n}$ satisfies the degree-$r$ recurrence with coefficients of $P_x$. Higher order carries no new information.*

*Proof.* The evaluation map $\mathbb R[t]\to\{q(y)\}$ has kernel $(P_x)$ since $q(y)=0\iff q$ vanishes on all $\lambda_j\iff P_x\mid q$; so the algebra is $\mathbb R[t]/(P_x)$, in which $t^r$ reduces to lower degree, giving the recurrence and Hankel rank $r$ ([\heb{ל}12] Thm 6). The displayed $P_x(t)=(t+1)t(t-2)=t^3-t^2-2t$ gives $\mu_{n+3}=\mu_{n+2}+2\mu_{n+1}$. $\square$

**Settlement \heb[P]{פ}12 — $\mathsf K$, $\mathsf{[P]}$.** Hankel rank stabilizes at $3=$\#levels and the exact recurrence residuals vanish: the tower is the finite algebra $\mathbb R[t]/(P_x)$. In the boundary language of \hyperref[sec:2]{§2}: the order axis is $\partial$ at a second altitude — everything past degree $r$ is the part $\partial$ quotients away.

### 4.3 \heb[P]{פ}14 — one set, five names {#sec:4-3}

Now the equivalence that gives the paper its spine. The geometer, asked why the kept sector is curved, points to a curvature defect $\mathcal R_S$. The physicist, asked why a conservation law fails, points to a Noether defect. The field theorist, asked what runs, points to a $\beta$-function. T14's equivalence theorem says these are one object; the exterior says that object is $\partial$. Let us *see* it, on the same six-hour clock.

The cubic curvature defect is $\mathcal R_S(u,v,w)=(1-\Pi_S-\Pi_1)(u\,v\,w)$ — the part of a triple product that lands outside the kept sector. Run over basis triples from $\{2,3,4\}$ and collect the off-sector outputs: the artifact returns the index set $\{1,5\}$, conductor $6$, with witnesses $\chi_2\chi_2\chi_3=\chi_1$ and $\chi_3\chi_4\chi_4=\chi_5$. This is *the same set* $\{1,5\}=H_6$ that \hyperref[sec:4-1]{§4.1} found as the leak. The curvature is the leak.

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (curvature is the boundary).** *For the retained sector $H_S$ and order $n$, the projected curvature defect $\mathcal R_S^{(n)}$, the renormalization (Schur/cumulant) source, the discrete $\beta$-source, and the inherited $n$-order Noether defect are all the operator $(1-\Pi_S-\Pi_1)V_n|_{H_S^{\otimes n}}$, whose universal support is $\partial_nS$ ([\heb{ל}14] Thm 6; [\heb{ל}13] Thm 1, 3, 5). At $N=6$, $S=\{2,3\}$, all four are supported exactly on $\{1,5\}=H_6=\partial_3\{2,3\}$.*

*Proof.* [\heb{ל}14] Thm 6 proves the four defects share the omitted component $(1-\Pi_S-\Pi_1)V_n$, sharp-supported on $\partial_nS$ by \hyperlink{stmt:4-1}{Proposition~4.1}; the $N=6$ support is the computation above. $\square$

**Settlement \heb[P]{פ}14 — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** The curvature support equals the fusion boundary, $\{1,5\}=H_6$, on the nose; the joint structure is that only the witness multisets $\{2,2,3\}$ and $\{3,4,4\}$ (and their orderings) reach it. Five interior names — curvature, projection-noncommutation, $\beta$-source, Schur correction, Noether defect — one exterior boundary. This is the heart of the Star, made one concrete set of two numbers.

### 4.4 \heb[P]{פ}15 — Euler's gamma, the factorial, and the primorial {#sec:4-4}

Climb now past every finite clock. Euler completed the factorial: the discrete $n!$ became the smooth $\Gamma(s)$, because — and this is the precise reason — the factorial *is a moment sequence*,
$$
n!=\int_0^\infty t^n e^{-t}\,dt ,
$$
an integral over the real half-line. A moment sequence is an archimedean object by birth. Ask the same of the *primorial* $P_n=\prod_{p\le p_n}p=1,2,6,30,210,\dots$, the pure finite-prime (Euler-product) counterpart. Is *it* a moment sequence — can it complete itself the way the factorial does? The test is classical: a sequence is a moment sequence only if all its Hankel determinants are non-negative. The artifact computes them exactly:
$$
D_0=1,\quad D_1=2,\quad D_2=24,\quad \boxed{D_3=-787680<0}.
$$
A *negative* Hankel determinant. The primorial is not a moment sequence; it admits no integral $\int t^n\,d\mu$ over the real line. The factorial, by contrast, returns $D_0,\dots,D_3=1,1,4,\dots$, all positive, exactly as a moment sequence must. (The value $D_3=-787680$ is [\heb{ל}15] Prop 12.2; our independent exact computation reproduces it — an anchored check that could have exposed an error, and did not.)

\hypertarget{stmt:4-4}{}
**Proposition 4.4 (the real place is a terminal boundary).** *The primorial $(P_n)$ is not a moment sequence: $D_3=-787680<0$. Hence the smooth primorial \heb[P]{פ}$(z)=e^{\operatorname{Li}^{-1}(z)}/2\pi$ has no Mellin/moment representation, and the archimedean factor — the real-place boundary $\Gamma_\infty=\pi^{-(s+\varepsilon)/2}\Gamma((s+\varepsilon)/2)$, whose scalar trace is the constant $1/2\pi$ — must be adjoined from outside ([\heb{ל}15] Thm 4, Prop 12.1–12.2). The factorial, being a moment sequence, completes itself through $\Gamma$; the primorial does not.*

*Proof.* A Stieltjes moment sequence has all Hankel determinants $\ge0$; $D_3<0$ refutes this for the primorial. The $\Gamma_\infty$ identification and the scalar constant $\log(2\pi)=-\zeta'(0)/\zeta(0)$ are [\heb{ל}15] Thm 4 and Prop 12.1. $\square$

**Settlement \heb[P]{פ}15 — $\mathsf K$, $\mathsf{[P]}$.** The real place is $\partial$ at its highest altitude: a boundary that provably cannot be reduced to any finite packet, because the finite-prime data fails the moment test by a definite negative sign. And here the exterior reading collects a gift it did not arrange. The scalar that the interior built to *name* this completion — the smooth primorial — the interior already wrote with this series' own letter, \heb[P]{פ}. The \heb[P]{פ} of *pe/primorial* and the \heb[P]{פ} of the exterior boundary are, it turns out, the same character on the same object: the completion of a finite-prime magnitude by its real-place boundary.

---

## 5. The synthesis (earned) {#sec:5}

We may now restate the Star as a result, at the tier each piece supports and no higher.

\hypertarget{stmt:5-1}{}
**Proposition 5.1 (one $\partial$, climbing — $\mathsf{[P]}$ for the rungs, $\mathsf{[A]}$ for the ladder).** *The four settlements establish, deterministically and at $\mathsf{[P]}$:*

- *(packets) the projected-vertex leak is the conductor-fusion boundary $\partial_nS$ (Prop 4.1);*
- *(orders) the order tower is the finite algebra $\mathbb R[t]/(P_x)$ (Prop 4.2);*
- *(geometry) the curvature, $\beta$, Schur, and Noether defects are that same boundary (Prop 4.3);*
- *(place) the terminal boundary is the real place, provably not a finite packet (Prop 4.4).*

*That these are one operator $\partial$ — a single boundary climbing from the conductor lattice (T11), through the finite order algebra (T12) and the fusion-closure RG flow (T13), to the projected geometry (T14) and out to the archimedean place (T15) — is asserted at $\mathsf{[A]}$. [\heb{ל}14] Thm 6 proves the finite-level identification (packets = geometry); the climb to the place level and the single-generator account remain a named, unbuilt audit, not claimed at $\mathsf{[P]}$.*

The honest seam is the point. Four boundary facts are settled by exact arithmetic; their unification into one climbing $\partial$ — and in particular the jump from the finite altitudes (T11–T14), where T14's equivalence already lives, to the place altitude (T15) — is the cornered next obligation, carried at its true tier.

This is also the natural closure of the exterior series so far. [\heb[P]{פ}1] made the support/face lattice primary and named the deferred $\partial$; [\heb[P]{פ}2] found the tropical/$L^\infty$ edge and, at the very end, the Archimedean place behind it; [\heb[P]{פ}3] now identifies that $\partial$ concretely — it is the conductor-fusion boundary — and follows it to the real line, where [\heb[P]{פ}2]'s $L^2$-versus-$L^\infty$ split and this paper's finite-prime-versus-archimedean split are the same split seen twice.

---

## 6. The method's own record {#sec:6}

A history of only confirmations has been performed, not tested. We record this session honestly.

**6.1 All four landed positive — why that is, and is not, a worry.** Every audit returned $\mathsf K$ (two of them $\mathsf K$ + joint-on-disjoint). That is expected and not alarming *here*, for a specific reason: these settlements are not open conjectures but *deterministic re-derivations* of already-proven interior theorems, run to (a) confirm them on their own objects by exact arithmetic and (b) extract the finer joint-on-disjoint structure the interior's statements did not foreground. The genuine test content is therefore not "did $\mathsf K$ fire" but the two places the computation could have embarrassed us and did not: the anchored value $D_3=-787680$ (a single wrong sign in [\heb{ל}15] Prop 12.2 would have shown here), and the joint-on-disjoint findings that the binary claims omitted — the $p=2$ parity asymmetry (\hyperref[sec:4-1]{§4.1}) and the $N=6$-is-special caution that $\partial_nS$ is generally several packets (also \hyperref[sec:4-1]{§4.1}), which corrects a natural over-reading of the clean $N=6$ slogan.

**6.2 A portability failure, retained.** The first run of `P3-settlements.py` aborted: the transcript prints the glyphs \heb[P]{פ} and $\partial$, and the platform's default code page (cp1252) cannot encode them, so Python raised a `UnicodeEncodeError` before any audit ran. The fix was to force UTF-8 on the output stream, not to strip the glyphs — the exact-output discipline should not be quietly degraded for the platform's convenience. The episode is retained because it is the reproducibility requirement (\hyperref[sec:3]{§3}) doing its job: a transcript that cannot be regenerated is not a transcript.

Neither item changes a realized branch.

---

## 7. Safe and unsafe statements {#sec:7}

**Safe (this paper asserts):**

- $\mathsf{[P]}$ The projected $n$-vertex leak is the conductor-fusion boundary $\partial_nS$; at $N=6$, $\partial_3\{2,3\}=\{6\}$, parity-asymmetric; in general $\partial_nS$ is a *set* of packets (Prop 4.1; settlement \heb[P]{פ}11).
- $\mathsf{[P]}$ A finite-level ledger's apex tower is $\mathbb R[t]/(P_x)$; Hankel rank $=$ \#levels (Prop 4.2; settlement \heb[P]{פ}12).
- $\mathsf{[P]}$ Curvature, $\beta$, Schur, and Noether defects share the support $\partial_nS$; at $N=6$ it is $\{1,5\}=H_6$ (Prop 4.3; settlement \heb[P]{פ}14).
- $\mathsf{[P]}$ The primorial is not a moment sequence ($D_3=-787680<0$); the real place is a terminal boundary, the gamma factor its completion (Prop 4.4; settlement \heb[P]{פ}15).
- $\mathsf{[A]}$ These four are one $\partial$ climbing from the packets to the real place (Prop 5.1) — structural, cornered to one named audit, not proven here.

**Unsafe (this paper does NOT assert):**

- That the climbing-$\partial$ unification is proven. It is $\mathsf{[A]}$; the finite-level equivalence is [\heb{ל}14]'s, the place-level jump is the unbuilt audit.
- That $\partial_nS$ is a single packet in general. It is, only at $N=6$; the artifact exhibits several packets at $N=12,30$.
- That the smooth primorial's analytic construction is done here. It is owned by T33; we use only its completion meaning (T15) and the exact $D_3<0$.
- Any claim that this settles, or is required by, GRH. The forward thread (\hyperref[sec:8]{§8}) is $\mathsf{[C]}$, named as a destination, not delivered.
- That this paper is important or field-defining. By the firewall such a claim would stand above its evidence; the method forbids its author from issuing it.

---

## 8. Forward door: where the boundary lands (calibrated, $\mathsf{[C]}$) {#sec:8}

Follow $\partial$ to the top of its ladder and it walks off the finite arithmetic onto the real place $\{\infty\}$, where — by T15 — it *is* the gamma factor, and the gamma factor is precisely the local data that turns a Dirichlet $L$-function into a *completed* $L$-function $\Lambda(s,\chi)$ whose zeros are the GRH locus. The same boundary that, downstairs, is a cubic leak on the six-hour clock is, upstairs, the archimedean factor of the object whose zeros the program is after. And the smooth primorial \heb[P]{פ} is its scalar shadow: a magnitude that provably cannot complete itself (Prop 4.4), so that the completion must be supplied — exactly the situation in which a functional equation, and therefore a critical line, can exist at all.

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (forward door — calibrated, not proved).** *The climbing $\partial$ of \hyperlink{stmt:5-1}{Proposition~5.1} reaches, at the real place, the archimedean factor of the completed $L$-function; the program's RH-shaped questions live where it lands, on the multiplicative apex (T8). [\heb[P]{פ}3] establishes the finite rungs and the place-level obstruction ($D_3<0$); the multiplicative/boundary \heb[P]{פ}-papers are charged with reaching the zeros.* Held with calibrated faith; built toward, not claimed.

---

## 9. Coda {#sec:9}

We began with three characters on a six-hour clock and a product that spilled into the family we had discarded. We end with a determinant attached to the primes whose sign is negative, and a gamma factor on the real line. In between, the same boundary wore five costumes — leak, finite quotient, RG flow, curvature, Noether defect — and the exterior reading was only ever the decision to take the boundary, rather than the centre, as the thing one is studying.

[\heb{ל}11] said the obstruction to closure is conductor fusion. [\heb{ל}14] said curvature is the cost of a nonclosed projection. [\heb{ל}15] said the continuum is what finite closure demands at infinity. From the boundary, [\heb[P]{פ}3] says all three are one sentence: *the part you discard does not vanish; it climbs.* It climbs from the packets to the real place, and the letter the interior wrote on its terminal scalar — \heb[P]{פ} — was, all along, the letter of the boundary itself.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) under the grounded-paranoid-delusional discipline this paper applies to itself: AI partners generated candidates, enumerated falsifiers, and executed the deterministic settlement artifact, but no fluent agreement was treated as evidence. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## Reproducibility {#sec:reproducibility}

The numbers of \hyperref[sec:4]{§4} are produced by `P3-settlements.py`, a deterministic, exact-arithmetic (integer / `Fraction`) script with no seeds and no floating point in any sign, vanishing, or membership decision; its full transcript (`P3-settlements.transcript.txt`), with the realized branch of each audit, is archived alongside, and re-running reproduces it identically (UTF-8 output is forced so the transcript is regenerable on any locale; see \hyperref[sec:6]{§6.2}).

## References {#sec:references}

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis.)

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Companion methodology preprint (draft v1).

Murillo Montero, L. (2026). *\heb[P]{פ}1 — From the Boundary: The Exterior of Identifying 3*; *\heb[P]{פ}2 — From the Boundary: The Gauge Trilogy at the Tropical Edge.* Companion preprints (the exterior \heb[P]{פ}-series: the face/support lattice and the deferred $\partial$; the tropical/$L^\infty$ edge and the Archimedean place).

Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (The apex $\mathcal M_x(\beta,c)$; conductor packets.)

Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo, DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049). (Conductors; the cubic selection rule.)

Murillo Montero, L. (2026). *T11 — The Apex Vertex Calculus*; *T12 — The Finite Apex Determinacy Theorem*; *T13 — Exact Simplicial Renormalization*; *T14 — Projected Flatness and Curvature Linearization*; *T15 — Finite-to-Archimedean Completion.* Companion manuscripts (the finite-apex boundary calculus anchored here: Thm references as cited in \hyperref[sec:4]{§4}).

Murillo Montero, L. (2026). *T33 — The Smooth Primorial Family.* Companion manuscript (construction of \heb[P]{פ}; the exact $D_3<0$ computation).

Murillo Montero, L. (2026). *T8 — The Multiplicative Apex and Finite Dirichlet Polynomials.* Companion manuscript (the multiplicative apex; "the RH-shaped questions live most naturally on the multiplicative apex").

Akhiezer, N. I. (1965). *The Classical Moment Problem.* Oliver & Boyd. (Hankel determinants and moment sequences, used in \hyperref[sec:4-4]{§4.4}.)

Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function.* 2nd ed., Oxford. (The explicit formula and $\zeta'(0)=-\tfrac12\log 2\pi$, used in \hyperref[sec:4-4]{§4.4}.)
