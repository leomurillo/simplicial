# \heb[P]{פ}4 — From the Boundary: The Quantum Face, the Units, and the Proven Critical Line

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 30, 2026*

## Abstract

**Situation.** Two interior papers carry the apex into its richest registers. T7 (Complex Amplitudes and the Quantum Sector of the Apex) lets the apex weight be a density matrix rather than a probability vector: its diagonal is the old classical apex, its off-diagonal is genuinely quantum, and the Fisher metric — *unique* on the classical diagonal by Chentsov's theorem — splits into an entire family (the Petz monotone metrics, with the Bures/SLD member minimal and the RLD member maximal) the instant one leaves it. T8 (The Multiplicative Apex and Finite Dirichlet Polynomials) moves the apex onto the units $(\mathbb Z/N)^\times$, where its characters become Dirichlet characters, its Gauss and Jacobi sums sit at the magnitude $\sqrt N$, and the program's RH-shaped questions find their natural home.

**Gap.** Each is written from the centre: the quantum metric as the obstruction to classical uniqueness, the multiplicative apex as the centre pushed onto the units. The exterior question reverses it. Where is the *boundary* of the quantum apex — and what is the honest status of the critical line the multiplicative apex points at? The interior is scrupulous that its classical, number-field RH is unproven. But it leaves unsaid a sharper exterior fact: on the *function-field* face of the very same multiplicative apex, the critical line is not a conjecture. It is Weil's theorem, and it can be confirmed by counting points.

**Action.** We proceed under the grounded-paranoid-delusional method (Murillo Montero 2026): a fenced *Star* with no vote on truth (\hyperref[sec:2]{§2}); five matched-pair falsifiers pre-registered before any check (\hyperref[sec:3]{§3}); and one deterministic, exact-arithmetic artifact (`P4-settlements.py`) anchored to T7–T8's own objects (\hyperref[sec:4]{§4}). The exposition is Eulerian: smallest number first, theorem last.

**Result.** Five settlements. **\heb[P]{פ}7 ($\mathsf K$, joint).** The reduced-rank faces of a rank-$k$ apex form the Boolean lattice $B_k$, and on a surviving eigenvalue pair the monotone-metric coefficient collapses to one value $1/x$ on the classical diagonal (Bures $=$ RLD) but splits, Bures $<$ RLD, off it — the Petz ambiguity is supported *exactly* on the quantum off-diagonal. **\heb[P]{פ}8 ($\mathsf K$, joint).** The smallest clock whose units fail to be cyclic is $N=8$, where $(\mathbb Z/8)^\times$ is the Klein four-group with conductor signature $\{1,4,8,8\}$ — all powers of a *single* prime, the 2-adic anomaly; the smallest *cross-prime* case is $N=12$, signature $\{1,3,4,12\}$. Same abstract group, separated only by the boundary's conductors. **\heb[P]{פ}bridge ($\mathsf K$, joint).** For every prime $q\equiv1\ (\mathrm{mod}\ 3)$ the cubic Jacobi sum is an exact Eisenstein integer of norm *exactly* $q$: the scale $\sqrt q$ is an algebraic identity, not a numerical near-miss. **\heb[P]{פ}Weil ($\mathsf K$, joint).** The projective Fermat cubic over $\mathbb F_q$ is a genus-one curve whose point count gives a Frobenius trace $a=q+1-\#C$ obeying $a^2\le4q$ on the nose — Weil's Riemann Hypothesis — so its eigenvalues have modulus exactly $\sqrt q$ and the zeros of its zeta function lie on $\operatorname{Re}(s)=\tfrac12$. A proven critical line, landed by integer arithmetic, and tied to the Jacobi sum by $a=-(J+\bar J)$. **\heb[P]{פ}fork ($\mathsf K_1$, joint; $\mathsf K_2$ falsified).** The two faces meet exactly: a character $C_c$ is a shift in the Fourier basis, so the Petz fork-width of \hyperref[sec:4-1]{§4.1}, evaluated on $C_c$ in a conductor-graded apex state, collapses to a lattice sum $W(c)=\sum_j\Delta(\lambda_{j+c},\lambda_j)$ which — proven by the unit action — is a **class function on the conductor lattice**, $W(c)=\Phi(\operatorname{cond} c)$. The quantum metric's non-uniqueness factors through the conductor packets. The natural sharpening "$\Phi$ grows with the conductor" we pre-registered, and it *failed* ($\Phi(6)<\Phi(4)$ at $N=12$; retained); for the dimension weight the parity packet self-closes, $\Phi(2)=0$, echoing \heb[P]{פ}11.

**Harvest.** The program's RH question is, on the function-field face, already answered: the critical line is a *counted* fact. What classical $\zeta$ lacks is precisely what \heb[P]{פ}15 of [\heb[P]{פ}3] identified as a terminal boundary — the archimedean place, which the finite primes provably cannot supply. So the exterior reading sets the proven and the open critical lines side by side and names the one ingredient between them. The function-field instance is carried at $\mathsf{[P]}$, and \heb[P]{פ}fork discharges one concrete *piece* of the two-faces unification to $\mathsf{[P]}$ as well — the quantum fork-width provably factors through the conductor lattice; the full single-object claim stays $\mathsf{[A]}$ and classical GRH $\mathsf{[C]}$, named and not claimed.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
A density matrix is a way of describing uncertainty that remembers more than a list of probabilities does: it keeps the ``off-diagonal'' information that makes quantum physics quantum. The first half of this paper asks where the edge of that richer description is, and finds two clean answers --- the ways it can collapse form a tidy ladder of cubes, and the famous non-uniqueness of its natural geometry lives exactly on the quantum part and nowhere else. The second half turns to the prime numbers. There is a celebrated unsolved problem, the Riemann Hypothesis, about a ``critical line.'' It turns out that a cousin of that problem --- set not over the ordinary whole numbers but over a finite system of arithmetic --- was proved long ago by André Weil, and its truth can be checked by literally counting the solutions of an equation. We count them; the line is there, exactly where it should be. We then say, as plainly as we can, what the ordinary primes are missing that keeps the original problem open: an ingredient a companion paper proved cannot be manufactured from the primes alone. Every number below is the printout of a short exact program; no sentence here is the evidence.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| $\mathcal M_z$ | Complex/quantum apex: the weight is a density matrix $\rho$, not a probability vector (T7). |
| $z_s$ | Eigenvalue (level) of the apex weight; the face $\{z_s=0\}$ is reduced rank. |
| $B_k$ | Boolean lattice of subsets of $\{1,\dots,k\}$ — the reduced-rank face strata. |
| $c(x,y)$ | Monotone-metric coefficient on an eigenvalue pair $(x,y)$ (Petz / Morozova–Chentsov). |
| Bures, RLD | Minimal $\bigl(2/(x{+}y)\bigr)$ and maximal $\bigl((x{+}y)/2xy\bigr)$ monotone metrics (SLD / RLD). |
| $\Delta(x,y)$ | Fork-width $c_{\mathrm{RLD}}-c_{\mathrm{SLD}}=\dfrac{(x-y)^2}{2xy(x+y)}\ge0$; $=0$ iff $x=y$ (\hyperref[sec:4-5]{§4.5}). |
| $W(c),\ \Phi$ | Character fork-width $W(c)=\sum_j\Delta(\lambda_{j+c},\lambda_j)$; conductor-graded $\Rightarrow W(c)=\Phi(\operatorname{cond} c)$ (\hyperref[sec:4-5]{§4.5}). |
| $(\mathbb Z/N)^\times$ | Units mod $N$; the multiplicative apex's support (T8). |
| $\chi$ | Dirichlet character; $\operatorname{cond}(\chi)$ its conductor (smallest modulus it lives on). |
| $\tau(\chi)$ | Gauss sum; $\lvert\tau(\chi)\rvert=\sqrt N$ for primitive $\chi$ (T8). |
| $J(\chi,\chi)$ | Jacobi sum $\sum_t\chi(t)\chi(1-t)$ — an algebraic integer. |
| $\omega,\ \mathbb Z[\omega]$ | Primitive cube root, $\omega^2=-1-\omega$; the Eisenstein integers. |
| $N(a+b\omega)$ | Eisenstein norm $a^2-ab+b^2$ (exact integer). |
| $C_3$ | Fermat cubic $x^3+y^3+z^3=0$ in $\mathbb P^2$ — smooth of genus $1$ (char $\ne3$). |
| $\#C(\mathbb F_q)$ | Projective point count; Frobenius trace $a=q+1-\#C(\mathbb F_q)$. |
| $\alpha,\bar\alpha$ | Frobenius eigenvalues; $\alpha\bar\alpha=q$ and $\alpha+\bar\alpha=a$. |
| $Z(C/\mathbb F_q,T)$ | Curve zeta $\dfrac{1-aT+qT^2}{(1-T)(1-qT)}$; Weil's RH: $\lvert\alpha\rvert=\sqrt q$. |
| $\mathsf{[P]/[A]/[C]}$ | Tiers: proven / structural-pending-named-audit / conjectural-reduced. |
| $\mathsf K,\mathsf L$ | Matched-pair branches; *joint-on-disjoint* when both fire on disjoint sub-structures. |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| GPD | Grounded-paranoid-delusional (the method of Murillo Montero 2026). |
| (G)RH | (Generalized) Riemann Hypothesis. |
| SLD / RLD | Symmetric / right logarithmic derivative — the Bures and the maximal monotone metric. |
| CRT | Chinese Remainder Theorem. |
| Frob | The Frobenius endomorphism (the $q$-power map) of a curve over $\mathbb F_q$. |
| function field | The arithmetic of a curve over a finite field, where the Riemann Hypothesis is Weil's *theorem*. |

---

## 1. A metric that splits, and a line that does not move {#sec:1}

Begin, as Euler would, with the smallest object that already shows the thing.

A classical apex weight on two outcomes is a pair $(p_1,p_2)$ with $p_1+p_2=1$. Its Fisher metric — the unique notion of statistical distance compatible with coarse-graining (Chentsov's theorem) — is forced; there are no choices to make. Now let the weight be a $2\times2$ *density matrix*: a positive matrix $\rho$ of trace $1$. On its diagonal nothing has changed. But $\rho$ may carry an off-diagonal entry, and there the question "what is the Fisher metric?" no longer has a single answer. The smallest witness: on eigenvalues $x=1$ and $y=3$, the minimal (Bures) metric weights the off-diagonal direction by $2/(x+y)=\tfrac12$, while the maximal (RLD) metric weights it by $(x+y)/2xy=\tfrac23$. Two different geometries, on the same matrix, differing only off the diagonal.

Now turn to the primes. The multiplicative apex (T8) lives on the units $(\mathbb Z/N)^\times$, and the program's RH-shaped questions live there too — as the statement that a completed $L$-function's zeros sit on a critical line. Over the rational field that statement is open. But ask it over a *function field* — a curve over a finite field — and it becomes a theorem of Weil, which one can confirm by counting. The smallest case is the Fermat cubic over the seven-element field: it has exactly nine projective points, its Frobenius trace is $-1$, and its eigenvalues have modulus exactly $\sqrt7$. The zeros are on the line, and we found them by counting to nine.

This paper is the exterior of those two interior chapters — T7's quantum apex and T8's multiplicative apex. From the boundary, the quantum metric's non-uniqueness and the function-field critical line are both *boundary* facts; and the second is the rare place where the program's north-star question is, on one face, already answered.

### 1.1 Why a gate, and why exact {#sec:1-1}

A word on method before any claim. The objects ahead — a forking metric, a critical line attached to the primes — are exactly the kind a willing mind and a fluent assistant can talk themselves into. So we adopt, as the *structure* of the paper, the grounded-paranoid-delusional discipline (Murillo Montero 2026): we permit one ambitious unifying picture but give it no vote on truth (\hyperref[sec:2]{§2}); we write down, before computing anything, what each possible outcome will be taken to mean (\hyperref[sec:3]{§3}); and we settle every question with one short program in exact integer, rational, and Eisenstein-integer arithmetic — no floating point in any decision of sign, vanishing, membership, or norm — whose transcript, not our prose about it, is the record (\hyperref[sec:4]{§4}). The artifact is `P4-settlements.py`; everything numerical below is its output. No agreement, however fluent, counts as evidence.

---

## 2. The Star (delusional; no vote on truth) {#sec:2}

> **Fence.** This section is *Historic Fiction*. It chooses what to attempt and in what order. It decides nothing. The only road from here to a result runs through the gate of \hyperref[sec:3]{§3} and \hyperref[sec:4]{§4}.

Here is the picture to chase. The apex has two faces, and one of them carries a line the program has been after from the start.

1. **The quantum face (T7).** Let the apex weight be a density matrix and then let it *decohere* — drive the off-diagonal to zero. You fall back onto the classical apex; the reduced-rank limits, where eigenvalues hit $0$, are the faces of a cone — a Boolean lattice. The non-uniqueness of the quantum metric is itself a boundary phenomenon: it disappears on the decohered (classical) diagonal, where Chentsov's uniqueness rules, and lives *only* off it, on the genuinely quantum part.

2. **The multiplicative face (T8).** Push the apex onto the units $(\mathbb Z/N)^\times$. Its characters are Dirichlet characters; its Gauss and Jacobi sums sit at the magnitude $\sqrt N$; and — the fiction — the program's RH question is the assertion that a completed $L$-function's zeros sit on the critical line $\operatorname{Re}(s)=\tfrac12$.

3. **The seam.** If these are truly two faces of one object, something computed on one face should be *governed* by the other. The sharpest joint test the faces afford: the genuinely quantum datum — the non-uniqueness (fork-width) of the metric, face 1 — evaluated on a genuinely multiplicative datum — an additive character, face 2. The fiction says this fork-width is not arithmetically neutral; it should see the conductor lattice.

The leap is this. There are *two arithmetics* of that multiplicative face. Over the rational field, the completed $L$-function needs an archimedean factor — a place at infinity — and whether its zeros lie on the line is the open Riemann Hypothesis. Over a function field there is *no archimedean place to supply*: the curve is already complete, the Frobenius endomorphism accounts for every zero, and Weil proved that they lie on the line. The same critical-line question, asked on the same multiplicative face, is a *theorem* on one arithmetic and a *conjecture* on the other — and the single ingredient separating them is exactly the terminal archimedean boundary that [\heb[P]{פ}3] showed the finite primes cannot generate.

If true: the boundary $\partial$ that climbed, in [\heb[P]{פ}3], to the real place $\{\infty\}$ is the precise obstruction to classical RH; remove that place — pass to a function field — and the obstruction is gone, the critical line proven. *The exterior of T7–T8 is the face on which the program's north star is a counted fact, and the place from which the one missing ingredient for the number-field face has a name.*

The paper does not argue this. It tests five load-bearing pieces of it and reports the arithmetic.

---

\clearpage

## 3. Pre-registration (paranoid; meanings fixed before the check) {#sec:3}

Before running `P4-settlements.py`, we fix the meaning of every outcome. Each branch is a real, reportable result; the *joint-on-disjoint* branch — both $\mathsf K$ and $\mathsf L$ realized on disjoint sub-structures — is the most informative the three-outcome rule can return.

| Audit | Claim under test | $\mathsf K$ | $\mathsf L$ | Joint-on-disjoint |
|---|---|---|---|---|
| **\heb[P]{פ}7** | The quantum boundary is a Boolean face-lattice carrying a Petz fork blind on the diagonal. | Strata $=B_k$ *and* Bures $=$ RLD on $x{=}y$, Bures $<$ RLD off it. | Strata not Boolean, *or* the fork fails to collapse on $x{=}y$. | Collapse on the classical diagonal, split on the quantum off-diagonal. |
| **\heb[P]{פ}8** | The first non-cyclic unit group is intra-prime ($N{=}8$); the first cross-prime is $N{=}12$. | $(\mathbb Z/8)^\times{=}V_4$, conductors $\{1,4,8,8\}$ (2-powers); $(\mathbb Z/12)^\times{=}V_4$, $\{1,3,4,12\}$. | Smallest non-cyclic $\ne8$, *or* its conductors not all one prime's powers. | Same $V_4$, separated only by the conductor signature. |
| **\heb[P]{פ}bridge** | The cubic Jacobi sum sits at scale $\sqrt q$ as an exact norm. | $N(J)=a^2{-}ab{+}b^2=q$ for all $q\equiv1\,(3)$. | $N(J)\ne q$ for some such $q$. | Scale rigid $(\sqrt q)$; direction $(a,b)$ free per prime. |
| **\heb[P]{פ}Weil** | The Fermat-cubic point count lands the critical line. | $a^2\le4q$ all $q$; strict with $a\ne0$ ordinary; $a=0$ inert; $a=-(J{+}\bar J)$. | $a^2>4q$ some $q$, *or* $a\ne0$ at an inert prime. | $\lvert\alpha\rvert=\sqrt q$ in both regimes, by disjoint mechanisms. |
| **\heb[P]{פ}fork** | The quantum fork-width of a character, in a conductor-graded apex state, lives on the conductor lattice. | $\mathsf K_1$: $W(c)=\Phi(\operatorname{cond} c)$, a class function (via the unit action). $\mathsf K_2$ (sharp): $\Phi$ monotone in $d$. | $\mathsf L_1$: $W$ varies within a packet. $\mathsf L_2$: $\Phi$ non-monotone. | Class function, but $w=\varphi$ self-closes the parity packet: $\Phi(2)=0$. |

We run the artifact.

---

## 4. Settlement (grounded; the transcript is the record) {#sec:4}

Each settlement pairs a **Proposition** with the **realized branch**, confirmed by the deterministic artifact. We compute first and explain second, in the Eulerian manner.

### 4.1 \heb[P]{פ}7 — the metric that splits, and the faces that stack {#sec:4-1}

Return to the $2\times2$ density matrix, eigenvalues $x,y>0$. The quantum Fisher metric assigns the off-diagonal direction a weight $c(x,y)$, and the deep fact (Petz's classification) is that $c$ is *not* determined: it ranges over a whole family, pinned between two extremes. The artifact computes both as exact rationals. On the diagonal $x=y$ they agree — both equal $1/x$ — but off it they separate:

$$
c_{\mathrm{Bures}}(x,y)=\frac{2}{x+y}=\mathrm{HM}\!\Bigl(\tfrac1x,\tfrac1y\Bigr),
\qquad
c_{\mathrm{RLD}}(x,y)=\frac{x+y}{2xy}=\mathrm{AM}\!\Bigl(\tfrac1x,\tfrac1y\Bigr),
$$

the harmonic and arithmetic means of the reciprocal eigenvalues. At $(x,y)=(1,3)$ the artifact returns $\tfrac12$ and $\tfrac23$; at $(2,5)$, $\tfrac27$ and $\tfrac{7}{20}$; on every diagonal pair, exact equality. Since $\mathrm{HM}\le\mathrm{AM}$ with equality iff the two numbers coincide, the fork is open precisely when $x\ne y$.

Now the faces. A rank-$k$ diagonal apex degenerates wherever an eigenvalue vanishes; the stratum killing exactly the coordinates in $T\subseteq\{1,\dots,k\}$ is the face $\{z_s=0:s\in T\}$. The artifact enumerates them: $2^k$ strata, graded by codimension $\lvert T\rvert$ into the binomial profile $\binom{k}{\cdot}$, closed under intersection and union, with Möbius function $(-1)^{\lvert T\rvert}$ — the Boolean lattice $B_k$.

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (the quantum boundary).** *The reduced-rank face strata of a rank-$k$ apex form the Boolean lattice $B_k$: $2^k$ elements graded by codimension, meet $=$ intersection, join $=$ union, Möbius $\mu(\varnothing,T)=(-1)^{\lvert T\rvert}$. The monotone (quantum Fisher) metrics form the Petz family, whose coefficient on an eigenvalue pair obeys*
$$
c_{\mathrm{Bures}}(x,y)=\frac{2}{x+y}\ \le\ c(x,y)\ \le\ \frac{x+y}{2xy}=c_{\mathrm{RLD}}(x,y),
$$
*with equality throughout iff $x=y$; on the diagonal every member equals $1/x$ (T7; Petz 1996).*

*Proof.* The strata are indexed by the killed coordinate set $T$, so as a poset they are $(2^{\{1,\dots,k\}},\subseteq)$, the Boolean lattice, whose Möbius function is $(-1)^{\lvert T\rvert}$. For the metric, the Morozova–Chentsov classification writes $c(x,y)=1/\bigl(y\,f(x/y)\bigr)$ for an operator-monotone $f$ with $f(1)=1$; the Bures/SLD choice $f(t)=(1+t)/2$ gives $2/(x+y)$ and is minimal, the RLD choice $f(t)=2t/(1+t)$ gives $(x+y)/2xy$ and is maximal. These are the harmonic and arithmetic means of $1/x,1/y$, so $\mathrm{HM}\le\mathrm{AM}$ gives the inequality, with equality iff $1/x=1/y$, i.e. $x=y$, where both equal $1/x$. $\square$

**Settlement \heb[P]{פ}7 — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** The faces are $B_3$ exactly, and the metric coefficient collapses on the classical diagonal (Bures $=$ RLD $=1/x$) while splitting off it (Bures $<$ RLD). The Petz ambiguity is supported *precisely* on the quantum off-diagonal: classical statistics is Chentsov-unique, the quantum part is not, and the boundary between them is the diagonal itself. One honest caution, also printed: the family is a *continuum*, not two points — the Kubo–Mori metric (the dually-flat, "additive" member that [\heb{ל}24] singles out) is the logarithmic mean, strictly between Bures and RLD. We settle only the two exact rational extremes and their diagonal collapse; the float value of Kubo–Mori is shown as a non-voting witness.

### 4.2 \heb[P]{פ}8 — the first clock whose units fail {#sec:4-2}

Walk up the clocks and ask, at each, whether the units form a single cycle. For $N=2,3,4,5,6,7$ they do: there is always a primitive root, one generator turning out every unit. At $N=8$ this breaks. The units are $\{1,3,5,7\}$, and the artifact reports their orders: $3^2=5^2=7^2\equiv1\ (\mathrm{mod}\ 8)$ — every non-identity unit squares to $1$. There is no generator; the group is the Klein four-group $V_4=\mathbb Z/2\times\mathbb Z/2$. This is the smallest non-cyclic $(\mathbb Z/N)^\times$, and its character conductors, also computed, are $\{1,4,8,8\}$ — *all powers of the single prime $2$*.

Climb a little further to $N=12$. Again $V_4$ (the units $\{1,5,7,11\}$ all square to $1$) — but now the conductors are $\{1,3,4,12\}$, mixing the primes $2$ and $3$. Same abstract group, different boundary.

\hypertarget{stmt:4-2}{}
**Proposition 4.2 (the 2-adic anomaly).** *$(\mathbb Z/N)^\times$ is non-cyclic first at $N=8$, where it is $V_4$ with conductor signature $\{1,4,8,8\}$ — all powers of the single prime $2$ (intra-prime). The smallest non-cyclic unit group spread across distinct primes is $N=12$, again $V_4$, with signature $\{1,3,4,12\}$. The two realize the same abstract group; only the conductor signature tells them apart (T8; Gauss).*

*Proof.* $(\mathbb Z/2^a)^\times\cong\mathbb Z/2\times\mathbb Z/2^{a-2}$ for $a\ge3$, non-cyclic from $a=3$ (i.e. $N=8$); the moduli $2,4,p^a$ ($p$ odd) are cyclic, and by CRT $(\mathbb Z/N)^\times$ is cyclic iff $N\in\{1,2,4,p^a,2p^a\}$. Hence $N=8$ is the least non-cyclic case and is single-prime, while $N=12=4\cdot3$ is the least with two distinct primes. The conductor of a character is the product of its local conductors over the prime-power factors; for $N=8$ these are powers of $2$ only, giving $\{1,4,8,8\}$, and for $N=12$ they cross $\{2,3\}$, giving $\{1,3,4,12\}$. $\square$

**Settlement \heb[P]{פ}8 — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** The artifact confirms $N=8$ as the first non-cyclic unit group (intra-prime, $\{1,4,8,8\}$) and $N=12$ as the first cross-prime one ($\{1,3,4,12\}$), both $V_4$. The joint structure is the point: the *interior* datum (the abstract group) cannot distinguish the two, while the *exterior* datum (the conductor signature) separates a single-prime $2$-adic ramification from a cross-prime CRT split. One honest caution, also computed: $N=8$ is only the *first*. Both families continue — $N=16$, $(\mathbb Z/16)^\times\cong\mathbb Z/2\times\mathbb Z/4$, is again intra-prime $2$-adic, while $N=15=3\cdot5$ is cross-prime. The anomaly worth naming is not that non-cyclicity occurs but that its *earliest* occurrence is the single prime $2$ doing it alone.

### 4.3 \heb[P]{פ}bridge — the Jacobi sum holds the scale $\sqrt q$ {#sec:4-3}

We now build the bridge from the multiplicative apex to the function field, and it is made of Jacobi sums. Fix the smallest prime on which a cubic character exists, $q=7\equiv1\ (\mathrm{mod}\ 3)$. With generator $3$ of $\mathbb F_7^\times$ define the cubic character $\chi(3^k)=\omega^{\,k\bmod 3}$, and form the Jacobi sum $J(\chi,\chi)=\sum_{t}\chi(t)\chi(1-t)$. The artifact carries the sum exactly in $\mathbb Z[\omega]$ and reduces it with $\omega^2=-1-\omega$:
$$
J(\chi,\chi)=2+0\cdot\omega+3\cdot\omega^2=-1-3\omega,
\qquad
N(J)=(-1)^2-(-1)(-3)+(-3)^2=7 .
$$
The norm is $q$ on the nose. The same holds, the artifact reports, for $q=7,13,19,31,37,43,61,67$: in every case $N(J)=q$ exactly, with the integer pair $(a,b)$ varying from prime to prime.

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (the $\sqrt q$ scale is an exact norm).** *For a prime $q\equiv1\ (\mathrm{mod}\ 3)$ with cubic character $\chi$, the Jacobi sum lies in $\mathbb Z[\omega]$ and*
$$
N\bigl(J(\chi,\chi)\bigr)=\lvert J(\chi,\chi)\rvert^2=q
\quad\Longleftrightarrow\quad
4q=L^2+27M^2,\ \ L=J+\bar J ,
$$
*so $\lvert J\rvert=\sqrt q$ is an algebraic identity (T8; Ireland–Rosen 1990).*

*Proof.* $\chi$ takes values in $\{1,\omega,\omega^2\}$, so $J(\chi,\chi)\in\mathbb Z[\omega]$. For a nontrivial character with $\chi^3=\mathbf 1$ and $\chi\cdot\chi$ nontrivial, the standard identity $\lvert J(\chi,\chi)\rvert^2=q$ holds, i.e. $N(J)=q$. Writing $J=a+b\omega$ gives $N(J)=a^2-ab+b^2$ and $L=J+\bar J=2a-b$, whence $4q=4(a^2-ab+b^2)=(2a-b)^2+3b^2=L^2+27M^2$ with $b=3M$ (the cubic Jacobi sum has $b\equiv0\,(3)$, $L\equiv1\,(3)$). $\square$

**Settlement \heb[P]{פ}bridge — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** $N(J)=q$ exactly for all eight tested primes. The magnitude is rigid — always $\sqrt q$ — while the lattice direction $(a,b)$ is free, disjoint prime by prime. That direction is not decorative: it *is*, up to sign, the Frobenius eigenvalue of the Fermat curve, which the last settlement counts.

### 4.4 \heb[P]{פ}Weil — the critical line, proven and counted {#sec:4-4}

Take the projective Fermat cubic $C_3:\ x^3+y^3+z^3=0$ over $\mathbb F_7$. The artifact counts its projective points by exact enumeration: there are $9$. The Frobenius trace is therefore $a=q+1-\#C=7+1-9=-1$, and $a^2=1\le28=4q$. The zeta numerator $1-aT+qT^2=1+T+7T^2$ has roots whose product is $1/q$ and whose reciprocals $\alpha,\bar\alpha$ satisfy $\alpha\bar\alpha=7$ and $\alpha+\bar\alpha=-1$; since $a^2<4q$ they are complex conjugates of modulus exactly $\sqrt7$. The zeros of $Z(C/\mathbb F_7,q^{-s})$ thus lie on $\operatorname{Re}(s)=\tfrac12$. And the bridge closes: $a=-1=-(J+\bar J)$, the trace of the Jacobi sum of \hyperref[sec:4-3]{§4.3}.

The artifact runs this for $q=5,7,11,13,17,19,23,31,37,43$. For every $q\equiv1\ (\mathrm{mod}\ 3)$ the trace is nonzero with $a^2<4q$ (ordinary), and $a=-(J+\bar J)$ matches the Jacobi sum each time. For every $q\equiv2\ (\mathrm{mod}\ 3)$ the cubing map is a bijection, the cubic character is absent, and the count gives $a=0$ exactly (supersingular) — the curve is "inert," carrying no Jacobi sum.

\hypertarget{stmt:4-4}{}
**Proposition 4.4 (a proven critical line).** *The Fermat cubic $C_3$ over $\mathbb F_q$ ($\mathrm{char}\ne3$) is smooth of genus $1$; with $a=q+1-\#C(\mathbb F_q)$ its zeta function is*
$$
Z(C/\mathbb F_q,T)=\frac{1-aT+qT^2}{(1-T)(1-qT)},
$$
*and Weil's Riemann Hypothesis holds: $a^2\le4q$, so the Frobenius eigenvalues satisfy $\lvert\alpha\rvert=\sqrt q$ and the zeros of $Z$ lie on $\operatorname{Re}(s)=\tfrac12$. For $q\equiv1\,(3)$, $a=-(J(\chi,\chi)+\overline{J(\chi,\chi)})$ ties the count to \hyperlink{stmt:4-3}{Proposition~4.3}; for $q\equiv2\,(3)$, $a=0$ (supersingular) (Weil 1949; T8).*

*Proof.* A diagonal Fermat curve of degree $d$ is smooth when $\mathrm{char}\nmid d$, of genus $\binom{d-1}{2}$; for $d=3$ this is $1$. Weil's theorem gives the rational zeta with numerator $1-aT+qT^2$ and the eigenvalue bound; $\alpha\bar\alpha=q$ is the constant term, so $\lvert\alpha\rvert=\sqrt q$ is equivalent to $a^2\le4q$ (real-coefficient quadratic with non-real roots). The point count of a diagonal cubic is $q+1+(J+\bar J)$ via Jacobi sums for $q\equiv1\,(3)$, giving $a=-(J+\bar J)$; for $q\equiv2\,(3)$ the cubing bijection collapses the count to that of a line, $a=0$ (Ireland–Rosen 1990, ch. 8, 11). The settlement verifies $a^2\le4q$ by exact counting and the tie $a=-(J+\bar J)$ on every ordinary prime. $\square$

**Settlement \heb[P]{פ}Weil — $\mathsf K$ + joint-on-disjoint, $\mathsf{[P]}$.** Hasse–Weil holds for every tested $q$; the ordinary primes ($q\equiv1$) give strict $a^2<4q$ with $a\ne0$, the inert primes ($q\equiv2$) give $a=0$ exactly, and the bridge tie $a=-(J+\bar J)$ matches throughout. The joint-on-disjoint structure is the whole content: the critical line $\lvert\alpha\rvert=\sqrt q$ holds in *both* regimes, by *disjoint* mechanisms — genuine complex-conjugate Frobenius where the cubic character exists, and a forced supersingular $a=0$ where it does not. This is the program's RH-shaped question, answered on the function-field face by counting integers.

### 4.5 \heb[P]{פ}fork — where the two faces meet: the fork on the conductor lattice {#sec:4-5}

The four settlements so far work the two faces *separately* — the quantum metric (\hyperref[sec:4-1]{§4.1}) and the multiplicative arithmetic (\hyperref[sec:4-2]{§4.2}–4.4). The Star promised they are one object. Here we make a piece of that promise exact, by asking the one question that needs both faces at once: **what is the quantum-metric ambiguity of an additive character?**

Two ingredients meet. From \hyperref[sec:4-1]{§4.1}, the Petz family has a *width*: on an eigenvalue pair the maximal minus the minimal monotone-metric coefficient is
$$
\Delta(x,y)\;:=\;c_{\mathrm{RLD}}(x,y)-c_{\mathrm{SLD}}(x,y)\;=\;\frac{x+y}{2xy}-\frac{2}{x+y}\;=\;\frac{(x-y)^2}{2xy(x+y)}\;\ge\;0,
$$
zero exactly on the diagonal $x=y$ (the collapse of \hyperref[sec:4-1]{§4.1}). From \hyperref[sec:4-2]{§4.2}–4.4, the natural observables are the additive characters $C_c=\sum_s\chi_c(s)\,|s\rangle\langle s|$, *diagonal* in the computational basis.

Now the one computation that joins them. A diagonal operator is a *shift* in the dual (Fourier) basis: writing $|j\rangle$ for the frequency vectors, $C_c|j\rangle=|j+c\rangle$, so $\langle i|C_c|j\rangle=\mathbf 1[i\equiv j+c]$. Take the apex state $\rho$ diagonal in this frequency basis with eigenvalues $\lambda_j$. Then the **character fork-width** — the gap between the largest and smallest quantum-Fisher costs the program could assign $C_c$ — collapses to an exact lattice sum,
$$
W(c)\;:=\;\bigl(g^{\mathrm{RLD}}_\rho-g^{\mathrm{SLD}}_\rho\bigr)(C_c,C_c)\;=\;\sum_{j\in\mathbb Z/N}\Delta(\lambda_{j+c},\lambda_j).
$$
This object is in no interior paper: it is T24's quantum fork, evaluated on T8's character, summed over T3's frequency lattice. The exterior question is whether it carries conductor arithmetic. Grade the state by conductor — $\lambda_j=w(\operatorname{cond} j)$, constant on each packet (T3) — and the answer is yes.

\hypertarget{stmt:4-5}{}
**Proposition 4.5 (the fork lives on the conductor lattice).** *Let $\rho$ be diagonal in the Fourier basis with conductor-graded spectrum $\lambda_j=w(\operatorname{cond} j)$. Then the character fork-width is a class function on the conductor lattice — there is a $\Phi$ with*
$$
W(c)=\Phi\bigl(\operatorname{cond} c\bigr)\qquad(c\in\mathbb Z/N),
$$
*and the class-function property holds for every graded weight $w$ (the values $\Phi(d)$ depend on $w$). The Petz ambiguity of the additive characters — the genuinely quantum content of \hyperref[sec:4-1]{§4.1} — therefore factors through the conductor packets of \hyperref[sec:4-2]{§4.2}–4.4 (T24; T3; T8).*

*Proof.* The conductor is unit-invariant: $\operatorname{cond}(uj)=\operatorname{cond}(j)$ for every unit $u\in(\mathbb Z/N)^\times$, so $\lambda_{uj}=\lambda_j$. Re-indexing the sum by the bijection $j\mapsto uj$,
$$
W(uc)=\sum_j\Delta(\lambda_{j+uc},\lambda_j)=\sum_k\Delta(\lambda_{u(k+c)},\lambda_{uk})=\sum_k\Delta(\lambda_{k+c},\lambda_k)=W(c),
$$
so $W$ is constant on each orbit of the unit action $c\mapsto uc$. Those orbits are exactly the conductor packets $H_d=\{c:\operatorname{cond} c=d\}$, since the units act transitively on $H_d$ (reduction $(\mathbb Z/N)^\times\twoheadrightarrow(\mathbb Z/(N/g))^\times$, $g=N/d$, is surjective). Hence $W$ depends on $c$ only through $\operatorname{cond} c$. $\square$

**Settlement \heb[P]{פ}fork — $\mathsf K_1$ + joint-on-disjoint, with $\mathsf K_2$ falsified, $\mathsf{[P]}$.** Four honest readings, all from the transcript.

*The bridge holds ($\mathsf K_1$, $\mathsf{[P]}$).* At $N=12$ and $N=30$, $W$ is a class function for every weight tried, and the proof's mechanism $W(uc)=W(c)$ is confirmed exactly. The quantum fork of the additive characters lives on the conductor lattice — the two faces meet there.

*But it barely shows at $N=6$ (honest scope).* The would-be smallest witness is degenerate. At $N=6$ every conductor packet is a $\pm$ pair $\{c,N-c\}$, so the trivial reflection $W(c)=W(N-c)$ already forces the class-function property — for *any* state, graded or not. The content appears only at $N\ge12$, where a *generic* (non-graded) $\rho$ gives a non-class-function $W$ and only the conductor grading restores it. It is the grading, not the fork alone, that does the work — exactly the exterior claim, and exactly what a single small example would have hidden.

*And the obvious sharpening is false ($\mathsf K_2$ falsified, retained).* We pre-registered the natural guess that $\Phi$ grows with the conductor — bigger character, wider fork. It does not: at $N=12$ with $w(d)=d$, $\Phi(6)<\Phi(4)$. The fork-width is a class function but *not* monotone in the conductor; the packet-transition structure is finer than "more conductor, more ambiguity." We keep the dead guess.

*The parity packet self-closes (joint-on-disjoint).* For the dimension weight $w=\varphi$ (each packet weighted by its size $\varphi(d)$), $\Phi(2)=0$ at $N=6,12,30$: the conductor-$2$ character — the half-shift $c=N/2$ — has *zero* fork-width, its quantum ambiguity vanishing even though the state is fully coherent. The fork closes on exactly the parity axis that \heb[P]{פ}11 of [\heb[P]{פ}3] found parity-locked. The $2$-axis is special on both faces.

This is the settlement that earns \hyperref[sec:2]{§2}'s "two faces, one apex" as more than a slogan: on a concrete, exact, conductor-graded state the quantum metric's non-uniqueness is a function on the conductor lattice, and its one identically-vanishing packet is the parity packet the boundary calculus had already singled out.

---

## 5. The synthesis (earned) {#sec:5}

We may now restate the Star as a result, at the tier each piece supports and no higher.

\hypertarget{stmt:5-1}{}
**Proposition 5.1 (two faces, one proven line — $\mathsf{[P]}$ for the pieces, $\mathsf{[A]}$ for the bridge, $\mathsf{[C]}$ for the classical line).** *The five settlements establish, deterministically and at $\mathsf{[P]}$:*

- *(quantum boundary) the reduced-rank faces are the Boolean lattice $B_k$, and the metric fork lives only off the classical diagonal (\hyperlink{stmt:4-1}{Proposition~4.1});*
- *(units) the multiplicative apex first goes non-cyclic at the 2-adic anomaly $N=8$, distinguished from the cross-prime $N=12$ only by its conductors (\hyperlink{stmt:4-2}{Proposition~4.2});*
- *(scale) the cubic Jacobi sum sits at the exact Eisenstein norm $\sqrt q$ (\hyperlink{stmt:4-3}{Proposition~4.3});*
- *(line) the Fermat-cubic Frobenius eigenvalues have modulus $\sqrt q$ — the function-field critical line, proven and counted (\hyperlink{stmt:4-4}{Proposition~4.4});*
- *(seam) on a conductor-graded apex state the quantum fork-width is a class function on the conductor lattice, $W(c)=\Phi(\operatorname{cond} c)$ — the two faces provably meet there (\hyperlink{stmt:4-5}{Proposition~4.5}).*

*That the additive/number-field apex and the multiplicative/function-field apex are two faces of one object — with the classical RH the same critical-line statement awaiting the single archimedean place that [\heb[P]{פ}3] proved finite primes cannot supply — is asserted at $\mathsf{[A]}$; \hyperlink{stmt:4-5}{Proposition~4.5} discharges one concrete piece of it to $\mathsf{[P]}$, the quantum fork-width provably living on the conductor lattice. That classical GRH itself holds is $\mathsf{[C]}$: named, built toward, not claimed. Weil's theorem is $\mathsf{[P]}$; its transport to $\mathbb Q$ is the cornered, unbuilt obligation.*

The honest seam is the point. We land a real critical line — the function-field one — by counting points, and we name precisely what stands between it and Riemann's. We do not claim to have crossed that gap.

This is also the natural place in the exterior series for the north star to first appear from the side on which it is settled. [\heb[P]{פ}1] made the support/face lattice primary; [\heb[P]{פ}2] found the tropical/$L^\infty$ edge and the Archimedean place behind it; [\heb[P]{פ}3] followed $\partial$ to the real place and proved the place is a *terminal* boundary ($D_3=-787680<0$); [\heb[P]{פ}4] now exhibits the one arithmetic — the function field — where that boundary is *absent*, and finds the critical line already proven there. The missing place of [\heb[P]{פ}3] and the proven line of [\heb[P]{פ}4] are the same fact stated twice. And in \heb[P]{פ}fork the series takes its first step past *re-reading* the interior: the conductor-lattice bridge (\hyperlink{stmt:4-5}{Proposition~4.5}) is a theorem that belongs to neither the quantum apex (T7/T24) nor the multiplicative apex (T8) alone — the first object here that is exterior in substance, not only in viewpoint.

---

## 6. The method's own record {#sec:6}

A history of only confirmations has been performed, not tested. We record this session honestly.

**6.1 Four confirmations and one genuine falsification.** Four of the five audits returned $\mathsf K$ — and, as in [\heb[P]{פ}3], that is expected rather than reassuring, because \heb[P]{פ}7, \heb[P]{פ}8, \heb[P]{פ}bridge, and \heb[P]{פ}Weil are deterministic re-derivations of already-proven facts (Petz's metric ordering, Gauss's cyclicity criterion, the Jacobi-sum norm, Weil's RH for a curve). Their test content is not "did $\mathsf K$ fire" but the places the computation could have embarrassed us and did not: the eight independent norms $N(J)=q$; the trace identity $a=-(J+\bar J)$ on every ordinary prime; the Hasse–Weil bound holding with the predicted ordinary/supersingular split; the conductor signatures $\{1,4,8,8\}$ versus $\{1,3,4,12\}$. The fifth audit, \heb[P]{פ}fork, is the one that was genuinely at risk — and the risk fired: its pre-registered sharp claim $\mathsf K_2$ (that $\Phi$ grows with the conductor) was **falsified** by the exact values, $\Phi(6)<\Phi(4)$ at $N=12$. We keep the dead guess. A session in which every pre-registered sharpening survived would be a session that pre-registered nothing falsifiable.

**6.2 A degenerate-modulus nontermination, retained.** The first run of `P4-settlements.py` did not finish. The unit-group scan began at $N=1$, and the naive order-finder loops forever there: $(\mathbb Z/1)^\times$ is the one-point group, where everything is $\equiv0\ (\mathrm{mod}\ 1)$, so the search for "the power that returns to $1$" — testing $\mathrm{cur}\ne1$ — never terminates, because $\mathrm{cur}$ is always $0$. The fix was to exclude the trivial modulus (start the scan at $N=2$) and to guard the order function at $N=1$. The episode is retained because it is the paper's own theme in miniature: the degenerate boundary — the one-point clock at the very bottom of the modulus ladder — needs separate handling, and a procedure tuned for the generic interior silently hangs at the edge. The exact-arithmetic discipline caught it as a *hang*, not a wrong answer, which is the honest failure mode.

**6.3 One modulus would have lied.** \heb[P]{פ}fork's bridge looks settled at $N=6$ — but $N=6$ cannot witness it: there every conductor packet is a reflection pair $\{c,N-c\}$, so $W(c)=W(N-c)$ forces the class-function property for *any* state, graded or not. Only at $N\ge12$, where a generic state breaks the property and the conductor grading restores it, does \hyperlink{stmt:4-5}{Proposition~4.5} have content. Had we tested the single smallest example, we would have recorded a theorem that was really a triviality. Three moduli, not one, separate the bridge from the reflection.

**6.4 What is re-read and what is new.** Honesty about novelty belongs in the ledger. \heb[P]{פ}7 in particular reproduces [\heb{ל}24] \hyperref[sec:3]{§3} — the Petz fork's collapse on the decoherent face and the harmonic–arithmetic ordering of the metrics — here reached independently; \heb[P]{פ}8, \heb[P]{פ}bridge, and \heb[P]{פ}Weil likewise re-derive classical facts. Their worth is the exterior *reading* and the exact joint structure, not new theorems. The exception is \heb[P]{פ}fork: \hyperlink{stmt:4-5}{Proposition~4.5} sits in no interior paper and in neither apex alone. The reader should weight the paper accordingly — four boundary re-readings and one boundary theorem.

Of these notes, only \heb[P]{פ}fork's $\mathsf K_2$ falsification (\hyperref[sec:6]{§6.1}) changes a realized branch; the rest are records of method.

---

## 7. Safe and unsafe statements {#sec:7}

**Safe (this paper asserts):**

- $\mathsf{[P]}$ The reduced-rank faces of the apex are the Boolean lattice $B_k$; the quantum Fisher metric forks (Bures $\le\cdot\le$ RLD), collapsing to a single value iff on the classical diagonal (\hyperlink{stmt:4-1}{Proposition~4.1}; settlement \heb[P]{פ}7).
- $\mathsf{[P]}$ $(\mathbb Z/N)^\times$ is first non-cyclic at $N=8$, intra-prime conductors $\{1,4,8,8\}$; $N=12$ is the first cross-prime case, $\{1,3,4,12\}$ (\hyperlink{stmt:4-2}{Proposition~4.2}; settlement \heb[P]{פ}8).
- $\mathsf{[P]}$ The cubic Jacobi sum is an Eisenstein integer of norm exactly $q$ (\hyperlink{stmt:4-3}{Proposition~4.3}; settlement \heb[P]{פ}bridge).
- $\mathsf{[P]}$ The Fermat-cubic critical line is proven and counted: $a^2\le4q$, $\lvert\alpha\rvert=\sqrt q$, zeros on $\operatorname{Re}(s)=\tfrac12$, with $a=-(J+\bar J)$ (\hyperlink{stmt:4-4}{Proposition~4.4}; settlement \heb[P]{פ}Weil). The program's RH question is, on this face, a counted theorem.
- $\mathsf{[P]}$ On a conductor-graded apex state the character fork-width is a class function on the conductor lattice, $W(c)=\Phi(\operatorname{cond} c)$, by the unit action (\hyperlink{stmt:4-5}{Proposition~4.5}; settlement \heb[P]{פ}fork) — the first statement here in neither interior apex alone.
- $\mathsf{[A]}$ The additive/number-field and multiplicative/function-field apices are two faces of one object; the classical RH is the same line missing the archimedean place (\hyperlink{stmt:5-1}{Proposition~5.1}).

**Unsafe (this paper does NOT assert):**

- That classical or number-field GRH is proven. Weil's RH is the function-field instance only; its transport to $\mathbb Q$ is $\mathsf{[C]}$, obstructed by the very place [\heb[P]{פ}3] named.
- That the quantum metric is unique, or that the fork is merely two metrics. It is unique only on the classical diagonal; off it the Petz family is a continuum, with Kubo–Mori strictly between Bures and RLD.
- That the $\sqrt q$ scale of the Jacobi sum, by itself, says anything about $\zeta$. It fixes the function-field eigenvalue modulus; the number-field statement stays heuristic — the "missing-Frobenius place."
- That $N=8$'s anomaly is generic. It is the *first* non-cyclic case; both the 2-adic and the cross-prime families continue ($N=15,16,\dots$).
- That the fork-width $\Phi$ is monotone in the conductor, or has a claimed closed form. The monotone guess was pre-registered and *falsified* ($\Phi(6)<\Phi(4)$ at $N=12$); the values are weight-dependent rationals.
- That $N=6$ witnesses the conductor-lattice bridge. It does not: at $N=6$ the class-function property is forced by reflection alone, and the content lives at $N\ge12$ (\hyperref[sec:4-5]{§4.5}, \hyperref[sec:6]{§6.3}).
- That this paper is important or field-defining. By the firewall such a claim would stand above its evidence, and the method forbids its author from issuing it.

---

## 8. Forward door: the proven line and the missing place (calibrated, $\mathsf{[C]}$) {#sec:8}

Here is the cleanest statement the program can make about its north star, and it is not a claim of proof. Over a function field — a curve over a finite field — the Riemann Hypothesis is Weil's theorem, and \hyperref[sec:4-4]{§4.4} confirmed an instance of it by counting the points of a cubic. The reason the proof exists there and not over $\mathbb Q$ is structural and, by now, named: the function-field curve is *complete* — it has no archimedean place — so the Frobenius endomorphism accounts for every zero and $\lvert\alpha\rvert=\sqrt q$ is forced. Over $\mathbb Q$ the completed $L$-function requires an archimedean factor, a place at infinity, and [\heb[P]{פ}3] proved that this place is a *terminal* boundary: the finite-prime data fails the moment test by a definite negative sign ($D_3=-787680<0$), so the place cannot be manufactured from the primes. The classical critical line is the function-field critical line plus the one ingredient that provably cannot be supplied from below.

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (forward door — calibrated, not proved).** *The program's RH-shaped question lives on the multiplicative apex (T8); on its function-field face it is Weil's theorem, here counted (\hyperlink{stmt:4-4}{Proposition~4.4}); on its number-field face it awaits the archimedean place that [\heb[P]{פ}3] proved finite primes cannot generate. The exterior \heb[P]{פ}-papers are charged with the missing place, not with re-proving Weil.* Held with calibrated faith; built toward, not claimed.

---

## 9. Coda {#sec:9}

We began with a $2\times2$ matrix whose geometry refused to be unique, and a cubic on a seven-element clock with exactly nine points. We end with a critical line that is, on one arithmetic, a theorem you can count to, and on another the most famous open problem in mathematics — separated by a single place at infinity that a companion paper proved cannot be built from the primes. The quantum metric forks only off the classical diagonal; the multiplicative units first fork at the prime $2$; the Jacobi sum holds the scale $\sqrt q$ exactly; the Fermat eigenvalue sits on the line; and where the two faces touch, the quantum fork-width of a character is one more class function on the conductor lattice — vanishing, for the dimension weight, on exactly the parity packet the boundary calculus had already marked.

T7 said the classical metric is the diagonal of a quantum one. T8 said the RH-questions live on the multiplicative apex. From the boundary, [\heb[P]{פ}4] says: that apex has a face on which the critical line is a *counted* fact, and the distance from there to Riemann's is exactly one place — the real place — which the boundary, climbing from below, can name but not reach. The part you discard does not vanish; it climbs, and where it finally lands is the one place that the proven line is missing.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) under the grounded-paranoid-delusional discipline this paper applies to itself: AI partners generated candidates, enumerated falsifiers, and executed the deterministic settlement artifact, but no fluent agreement was treated as evidence. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## Reproducibility {#sec:reproducibility}

The numbers of \hyperref[sec:4]{§4} are produced by `P4-settlements.py`, a deterministic, exact-arithmetic (integer / `Fraction` / Eisenstein-integer) script with no seeds and no floating point in any sign, vanishing, membership, or norm decision; its full transcript (`P4-settlements.transcript.txt`), with the realized branch of each audit, is archived alongside, and re-running reproduces it identically (UTF-8 output is forced so the transcript is regenerable on any locale; the single non-ASCII-driven failure of this session is recorded in \hyperref[sec:6]{§6.2}).

## References {#sec:references}

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis.)

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Companion methodology preprint (draft v1).

Murillo Montero, L. (2026). *\heb[P]{פ}1 — From the Boundary: The Exterior of Identifying 3*; *\heb[P]{פ}2 — From the Boundary: The Gauge Trilogy at the Tropical Edge*; *\heb[P]{פ}3 — From the Boundary: The Leak, the Curvature, and the Real Place.* Companion preprints (the exterior \heb[P]{פ}-series; [\heb[P]{פ}3] establishes the real place as a terminal boundary, $D_3=-787680<0$).

Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier–Mellin Simplex.* Zenodo, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (The apex $\mathcal M_x(\beta,c)$; conductor packets.)

Murillo Montero, L. (2026). *[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector of the Apex.* Zenodo, DOI [10.5281/zenodo.20392442](https://doi.org/10.5281/zenodo.20392442). (The quantum apex; reduced-rank faces; the Petz monotone-metric family.)

Murillo Montero, L. (2026). *T8 — The Multiplicative Apex and Finite Dirichlet Polynomials.* Companion manuscript (the multiplicative apex on $(\mathbb Z/N)^\times$; Gauss and Jacobi sums; "the RH-shaped questions live most naturally on the multiplicative apex").

Murillo Montero, L. (2026). *T24 — The Monotone-Metric Apex: The Petz Fork and the Kubo–Mori Selection.* Companion manuscript (the Petz family; Kubo–Mori as the dually-flat member, used in \hyperref[sec:4-1]{§4.1}).

Petz, D. (1996). *Monotone metrics on matrix spaces.* Linear Algebra and its Applications **244**, 81–96. (Classification of monotone quantum Fisher metrics; Bures minimal, RLD maximal.)

Weil, A. (1949). *Numbers of solutions of equations in finite fields.* Bulletin of the American Mathematical Society **55**, 497–508. (The Riemann Hypothesis for curves over finite fields, used in \hyperref[sec:4-4]{§4.4}.)

Ireland, K. & Rosen, M. (1990). *A Classical Introduction to Modern Number Theory*, 2nd ed. Springer GTM **84**. (Gauss and Jacobi sums; the Fermat curve point count; chapters 8 and 11.)
