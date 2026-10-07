# \heb[P]{פ}2 — From the Boundary: The Gauge Trilogy at the Tropical Edge

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 29, 2026*

## Abstract

**Situation.** The gauge trilogy [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) reads the mean-zero simplicial space through four observers — arithmetic (mass), geometric (scale), harmonic (reciprocal), and RMS (amplitude) — and finds, inside each, a clean interior structure: [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s subtract-the-mean Helmert ladder with the prime radical clock $K_N=\mathbb Q(\sqrt p:p\le N)$; [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s harmonic dual with the even/odd cumulant split $\log(A/H),\log(AH/G^2)$; [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s RMS/Born closure $p_i=x_i^2/\sum_j x_j^2$ with the $2\arccos$ Fisher–Rao distance. All three are $L^2$ phenomena, anchored at the centre.

**Gap.** Each paper names a boundary it does not inhabit. [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) canonicalizes subtract-the-mean and only gestures at the genesis's subtract-the-minimum (`massaction`). [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) attaches a *proviso* to its central theorem — "$\pm1$ may lie outside the zero-free Taylor domain, else read formally" — and stops. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) proves that iterated Born closure concentrates on the maximal-coordinate support (its Thm 10.1) but frames it as "the RMS cell," not as a flow to a face. The genesis's *Origin-and-Destination* — flow out from the balanced centre to the winner-take-all edge — is exactly this boundary.

**Action.** This paper is written under the grounded-paranoid-delusional method (Murillo Montero 2026, the methodology preprint): **diverge** into a fenced *Star* with no evidentiary vote (\hyperref[sec:2]{§2}); **bound** by pre-registering, for three load-bearing exterior claims, matched-pair falsifiers — $\mathsf K$ / $\mathsf L$ / joint-on-disjoint — with each branch's meaning fixed before any check (\hyperref[sec:3]{§3}); **ground** each on a single deterministic, exact-arithmetic artifact anchored to [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s own objects (`P2-settlements.py`; \hyperref[sec:4]{§4}). No fluent agreement is treated as evidence; only the reproducible transcript settles.

**Result.** Three settlements, all $\mathsf{[P]}$. **\heb[P]{פ}4 (joint-on-disjoint).** The prime radical clock is an Archimedean ($L^2$) artifact: along the $L^q$ norm corridor it survives at finite even $q$ (radical normalizers) and *vanishes* at the tropical endpoint $q=\infty$, where $\|h_k\|_\infty=k$ is rational — yet the integer incidence skeleton and the cubic incidence rule ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 7.3) survive tropicalization. **\heb[P]{פ}5 ($\mathsf K$).** The harmonic proviso *is* the Lee–Yang edge: for $N=2$, $y=(-a,a)$, the cumulant series for $\log(A/H)$ diverges once $a>\pi/2$ (the nearest zero of $\cosh$), while the exact identity $\log(A/H)=K_y(1)+K_y(-1)$ stays finite — the interior expansion fails, the exterior identity survives. **\heb[P]{פ}6 ($\mathsf K$).** Iterated Born closure $S_2^{\,n}$ climbs monotonically onto the uniform distribution on $\arg\max$ (ties kept) — the discrete $\beta\to\infty$ tropical limit landing on the Newton-polytope face $F_{\arg\max}$, the genesis Destination.

**Harvest.** The gauge corridor is $L^2$ in its interior and $L^\infty$ at its boundary. The three exteriors are one tropical skeleton seen three ways — arithmetically ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504): radical clock dissolves, incidence survives), analytically ([\heb{ל}5](https://doi.org/10.5281/zenodo.20388419): the cumulant tower's edge), dynamically ([\heb{ל}6](https://doi.org/10.5281/zenodo.20392428): the Origin$\to$Destination flow to the winner face). The record retains its two failures (an exact-arithmetic blow-up; a fluent-but-wrong annotation caught by the deterministic value), a safe/unsafe firewall, and a calibrated, forward-only GRH thread that is named, not claimed.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
Three earlier papers studied four ways of averaging a list of positive numbers --- ordinary, geometric, harmonic, and root-mean-square --- and found surprising structure hiding inside each. This paper asks what happens at the \emph{edge} of each: what survives when you push the averaging all the way to ``winner takes all.'' To keep itself honest, it follows a strict recipe borrowed from a companion methodology paper: first dream up the bold unifying picture but give it no vote on truth; then, \emph{before running any check}, write down exactly what each possible result will be taken to mean; then settle every question with a small exact-arithmetic program whose printout --- not any persuasive paragraph --- is the verdict. The three verdicts: the ``prime clock'' hidden in the geometric ladder is a feature of ordinary distance that disappears at the tropical edge, leaving only the integer skeleton; the fine-print caveat in the harmonic paper turns out to be precisely the place where a hidden infinity lives; and repeatedly squaring-and-renormalizing a probability really does march it onto its largest outcome --- the ``destination'' the project's very first 2025 notes were pointing at.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| $N$ | Number of slots / outcomes; integer $\geq 2$. |
| $H_N$ | Mean-zero hyperplane $\{q\in\mathbb R^N:\sum_i q_i=0\}$ ($=H_0$ of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)). |
| $\mathbf 1$ | All-ones vector; the gauge direction. |
| $h_k$ | Unnormalized Helmert vector $(1,\dots,1,-k,0,\dots,0)$, $k$ leading ones ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)). |
| $\|\cdot\|_q$ | $L^q$ norm; $\|h_k\|_2=\sqrt{k(k+1)}$, $\|h_k\|_\infty=k$. |
| $\operatorname{sf}(n)$ | Squarefree kernel of $n$ (square class). |
| $K_N$ | Multiquadratic field $\mathbb Q(\sqrt p:p\le N,\ p\text{ prime})$ ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 3.1). |
| $A,G,H,R$ | Arithmetic, geometric, harmonic, RMS means ([\heb{ל}5](https://doi.org/10.5281/zenodo.20388419), [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)). |
| $y$ | Centered log-ledger $y_i=\log x_i-\tfrac1N\sum_j\log x_j$; $\sum_i y_i=0$. |
| $K_y(t)$ | Directional log-partition $\log\!\big(\tfrac1N\sum_i e^{t y_i}\big)$; $\kappa_n=K_y^{(n)}(0)$. |
| $S_2$ | Born/square closure $S_2(p)_i=p_i^2/\sum_j p_j^2$ ([\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)). |
| $F_S$ | Face $\{p\in\Delta^{N-1}:\operatorname{supp}(p)\subseteq S\}$; the support stratum ([\heb[P]{פ}1]). |
| `massaction` | Genesis normalization $x\mapsto x-(\min_i x_i)\mathbf 1$ (subtract-the-minimum). |
| $\mathsf{[P]/[A]/[C]}$ | Evidence tiers: proven / structural-pending-named-audit / conjectural-reduced. |
| $\mathsf K,\mathsf L$ | Matched-pair branches: positive / negative (joint-on-disjoint when both, disjointly). |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| GPD | Grounded-paranoid-delusional (the method of Murillo Montero 2026). |
| RMS | Root mean square; the $L^2$ / amplitude gauge ([\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)). |
| AC | Amari–Chentsov (cubic tensor). |
| FR | Fisher–Rao. |
| LDP | Large-deviation principle. |
| GRH | Generalized Riemann Hypothesis (forward-door north star, \hyperref[sec:8]{§8}). |
| tropical | The min-plus / max-plus semiring; the $r=\pm\infty$ / $q=\infty$ boundary. |

---

## 1. The gauge trilogy, and the gate {#sec:1}

### 1.1 Three observers, one $L^2$ interior {#sec:1-1}

The gauge trilogy fixes one positive ledger $x\in\mathbb R_{>0}^N$ and varies the *observer*. [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) removes the arithmetic mean and canonicalizes the Helmert contrast vectors $h_k=(1,\dots,1,-k,0,\dots,0)$; on unit ($L^2$) normalization the constants $\sqrt{k(k+1)}$ generate the multiquadratic field $K_N=\mathbb Q(\sqrt p:p\le N)$, which grows *exactly* at prime rungs (its Thm 3.1). [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) adds the harmonic mean as the reciprocal partner of the arithmetic mean about the self-dual geometric mean, and reads the pair $(A,H)$ around $G$ as an even/odd cumulant split, $\log(A/H)=K_y(1)+K_y(-1)$ and $\log(AH/G^2)=K_y(1)-K_y(-1)$ (its Thm 4.2). [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) names the common mechanism: $L^2$-normalize the ray. Born closure $p_i=x_i^2/\sum_j x_j^2$ and the $\sqrt{k(k+1)}$ Helmert normalizers are two faces of one operation, and Fisher–Rao distance is twice the amplitude-ray angle, $d_{FR}=2\arccos\frac{x\cdot y}{\|x\|\|y\|}$.

All three are interior, analytic, and $L^2$. And all three name an edge they do not enter. That edge is this paper.

### 1.2 The gate (why this paper is structured the way it is) {#sec:1-2}

Per the launch of the exterior series ([\heb[P]{פ}1]), the boundary is where the program's hard objects live, and the boundary is precisely where conviction and a fluent assistant are most able to manufacture a believable-but-unchecked result. We therefore adopt the GPD discipline (Murillo Montero 2026) as the *structure* of the paper, not a remark about it:

- **Delusional (\hyperref[sec:2]{§2}).** Generate the high-variance unification — the *Star* — and fence it: it sets the direction of search and is **denied any vote on truth**.
- **Paranoid (\hyperref[sec:3]{§3}).** Before any check, pre-register the matched-pair falsifier of each load-bearing claim, $\mathsf K$ / $\mathsf L$ / joint-on-disjoint, fixing the meaning of each outcome while its truth value is unknown.
- **Grounded (\hyperref[sec:4]{§4}).** Settle each on a deterministic, exact-arithmetic artifact anchored to the sources' own objects. The transcript — not any sentence in this paper — is the record. Tiers $\mathsf{[P]/[A]/[C]}$ are firewalled against upward crossing (\hyperref[sec:7]{§7}).

The artifact is `P2-settlements.py` (archived with its transcript); every numeric claim below is reproduced by re-running it.

---

## 2. The Star (delusional; no evidentiary vote) {#sec:2}

> **Fence.** Everything in \hyperref[sec:2]{§2} is *Historic Fiction*: it determines what is worth attempting and in what order. It determines nothing about what is true. The only path from this section to a result runs through the gate of \hyperref[sec:3]{§§3}–4; narrative coherence, however strong, is not a second path.

The Star. The four gauges of the trilogy are samples of one power-mean corridor $M_r$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985); [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)): harmonic at $r=-1$, geometric at $r=0$, arithmetic at $r=1$, RMS at $r=2$, with the $L^2$ Helmert ladder ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)) the centred face of the same $L^2$. The corridor's *interior* (finite $r$, finite norm exponent $q$) is the analytic, Archimedean, $L^2$ world the trilogy mapped. Its *boundary* is the tropical limit $r,q\to\pm\infty$ — the genesis's `massaction` (subtract-the-minimum, the min-plus gauge) at one end and winner-take-all (max-plus) at the other.

The fiction is that **the three gauge papers have one exterior, and it is a single tropical skeleton seen three ways**:

- **Arithmetic face ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)).** The prime radical clock is the *interior* (finite-$q$) shadow; at the tropical endpoint $q=\infty$ the radicals flatten to integers and the clock dissolves, leaving the bare integer incidence skeleton — exactly the genesis's "metric trick" (keep the integer skeleton, carry the metric) read as a boundary statement.
- **Analytic face ([\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)).** The proviso on the cumulant split is the *Lee–Yang edge*: the interior Taylor tower converges only inside the zero-free radius; the exact mean-ratio identities are the boundary-robust survivors.
- **Dynamical face ([\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)).** Iterated Born closure is the discrete $\beta\to\infty$ flow from the RMS centre (Origin) to the winner-take-all face (Destination) — the genesis's *Origin-and-Destination*, made a dynamical system.

If true, the slogan is: *the gauge corridor is $L^2$ in its interior and $L^\infty$ at its boundary, and the three gauge papers' exteriors are the three projections of one Origin$\to$Destination flow onto the face lattice.* The remainder of the paper does not argue this. It tests its three load-bearing pieces and reports what the arithmetic says.

---

\clearpage

## 3. Pre-registration (paranoid; meaning fixed before the check) {#sec:3}

We pre-commit, before running `P2-settlements.py`, to the following three matched-pair falsifiers. Each branch is a genuine, reportable result; the joint-on-disjoint branch (binding from [\heb[P]{פ}1]'s methodology onward) is stated wherever the structure admits both $\mathsf K$ and $\mathsf L$ on disjoint sub-structures.

| Audit | Claim under test | $\mathsf K$ (positive) | $\mathsf L$ (negative) | Joint-on-disjoint |
|---|---|---|---|---|
| **\heb[P]{פ}4** | The prime radical clock is Archimedean; tropical boundary keeps only the skeleton. | Some tropical ($q\to\infty$) norm still yields a quadratic-field prime clock. | No tropical norm yields a clock; $\|h_k\|_\infty=k$ is rational, field $=\mathbb Q$. | Clock vanishes at $q=\infty$ ($\mathsf L$ on the radical) **and** the integer incidence skeleton + cubic rule ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 7.3) survive ($\mathsf K$ on the skeleton). |
| **\heb[P]{פ}5** | The harmonic proviso *is* the Lee–Yang edge. | A ledger exists where $\pm1$ is outside the radius: the cumulant series **diverges** while the exact identity holds. | No such ledger; whenever the identity holds the series converges (proviso vacuous). | — (binary suffices). |
| **\heb[P]{פ}6** | Iterated Born closure flows to the winner face. | $S_2^{\,n}(p)\to\mathrm{Unif}(\arg\max p)$, a single face $F_{\arg\max}$, ties kept. | It does not (breaks ties, wanders, or limits off $\arg\max$). | Converges onto $F_{\arg\max}$ but resolves ties otherwise than "uniform on the tied max set." |

The meaning of each outcome is now fixed. We run the artifact.

---

## 4. Settlement (grounded; the transcript is the record) {#sec:4}

Each settlement below pairs a **Proposition** (proved) with the **realized branch** of \hyperref[sec:3]{§3}, confirmed by the deterministic artifact. The proof is the deductive ground; the artifact is the independent, re-runnable check demanded by the method (a proof one is attached to is exactly what most needs an adversary's re-run). All arithmetic is exact (integer / `Fraction`); no floating point enters any vanishing or membership decision.

### 4.1 \heb[P]{פ}4 — the prime clock dissolves at the tropical boundary {#sec:4-1}

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (Tropical flattening of the Helmert normalizer).** *For the Helmert vector $h_k$ and $q\in[2,\infty]$, $\|h_k\|_q=\big(k+k^{q}\big)^{1/q}$ for finite $q$ and $\|h_k\|_\infty=k$. Hence $\|h_k\|_2=\sqrt{k(k+1)}$ is a radical generating the square class $\operatorname{sf}(k(k+1))$, while the tropical endpoint $\|h_k\|_\infty=k$ is rational. Consequently the prime radical clock $K_N=\mathbb Q(\sqrt p:p\le N)$ of [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 3.1 — which grows exactly at prime $N$ — is a finite-$q$ (Archimedean) phenomenon: at $q=\infty$ the normalizers generate only $\mathbb Q$, and there is no clock.*

*Proof.* $h_k$ has $k$ entries equal to $1$ and one equal to $-k$, so $\|h_k\|_q^q=k\cdot1^q+k^q$ for finite $q$, giving $(k+k^q)^{1/q}$; letting $q\to\infty$ gives $\max(1,k)=k$. At $q=2$ this is $\sqrt{k+k^2}=\sqrt{k(k+1)}$, the [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) normalizer, whose square class is $\operatorname{sf}(k(k+1))$; [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 3.1 assembles these into $K_N=\mathbb Q(\sqrt p:p\le N)$. At $q=\infty$ the normalizer $k\in\mathbb Q$ generates no quadratic extension. $\square$

\hypertarget{stmt:4-2}{}
**Proposition 4.2 (Gauge-independence of the incidence skeleton).** *The integer vectors $h_k$ and the cubic incidence values $T_u(h_a,h_b,h_c)=\tfrac1N\sum_i (h_a)_i(h_b)_i(h_c)_i$ ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 7.3) are defined over $\mathbb Z[\tfrac1N]$ and depend on no metric or norm; they are unchanged under tropicalization.*

*Proof.* $h_k$ is an integer vector and the contraction is an integer combination divided by $N$; neither references a norm. $\square$

**Settlement \heb[P]{פ}4 — JOINT-ON-DISJOINT $\mathsf{[P]}$.** The artifact computes, exactly: (a) the square classes $\operatorname{sf}(k(k+1))$ for $N\le16$, confirming $K_N\ne K_{N-1}\iff N$ prime with field-growth rungs exactly $\{2,3,5,7,11,13\}$ (the primes $\le16$) — [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 3.1 reproduced; (b) $\|h_k\|_\infty=k$ for $N\in\{4,7,12,16\}$, rational, field $=\mathbb Q$, **no clock**; (c) [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 7.3's incidence formula reproduced exactly over all triples at $N=7$. The realized branch is joint-on-disjoint: $\mathsf L$ on the radical clock (Archimedean, gone at $q=\infty$) **and** $\mathsf K$ on the integer skeleton (gauge-free, survives). This is the genesis `metric trick` as a boundary statement: the integer skeleton is the tropical face; the radical residue is the Archimedean face; *the prime clock lives only on the Archimedean face.* Per the methodology, the joint-on-disjoint outcome is the most informative of the three — it is the precise content the binary $\mathsf K/\mathsf L$ framing would have hidden.

*Scope (firewall).* "$q=\infty$ has no clock" is $\mathsf{[P]}$ for the $L^q$ corridor's two computed endpoints ($q=2$ radical, $q=\infty$ rational). The stronger "no min-plus normalization convention whatsoever admits a prime clock" is $\mathsf{[A]}$ (a named, not-yet-performed audit over tropical normalization conventions), not asserted here.

### 4.2 \heb[P]{פ}5 — the harmonic proviso is the Lee–Yang edge {#sec:4-2}

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (Boundary-robust identity vs. interior series).** *For $N=2$ and $y=(-a,a)$, $K_y(t)=\log\cosh(at)$, and:*

1. *(Exterior, boundary-robust.) The identity $\log(A/H)=K_y(1)+K_y(-1)=2\log\cosh(a)$ holds for every $a$ (the geometric mean cancels), and is finite for every $a$.*
2. *(Interior, edge-limited.) The cumulant series $2\sum_{m\ge1}\kappa_{2m}/(2m)!=2\sum_{m\ge1}\ell_{2m}a^{2m}$, with $\ell_{2m}=[u^{2m}]\log\cosh u$, has radius of convergence (in $a$) equal to $\pi/2$ — the modulus of the nearest zero of $\cosh$, i.e. the Lee–Yang point of $Z_y$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Prop 2.5). It converges to $2\log\cosh a$ for $a<\pi/2$ and diverges for $a>\pi/2$.*

*Proof.* For $x=(e^{-a},e^a)$: $A=\cosh a$, $H=1/\cosh a$ (since $H=2/(e^a+e^{-a})$), so $A/H=\cosh^2 a$ and $\log(A/H)=2\log\cosh a$; and $K_y(\pm1)=\log\cosh a$, so the identity is algebraic in $\cosh a$ and finite for all $a$. The series is the Taylor expansion of $2\log\cosh(au)$ at $u=0$ evaluated at $u=1$; $\log\cosh$ is holomorphic on $|u|<\pi/2$ with a logarithmic singularity at the nearest zero $u=i\pi/2$ of $\cosh$, so its radius in the argument is $\pi/2$, i.e. in $a$ (at the harmonic point) it is $\pi/2$. $\square$

**Settlement \heb[P]{פ}5 — $\mathsf K$, $\mathsf{[P]}$.** The artifact computes the exact rational coefficients $\ell_{2m}$ ($\ell_2=\tfrac12,\ \ell_4=-\tfrac1{12},\ \ell_6=\tfrac1{45},\ \ell_8=-\tfrac{17}{2520},\dots$) and the exact rational partial sums at $a=1$ and $a=2$, deciding convergence float-free by whether the tail of $|$terms$|$ shrinks or grows. At $a=1<\pi/2$ the series **converges** ($|$terms$|\to0$, partial sum $\to0.8675617=2\log\cosh1$). At $a=2>\pi/2$ it **diverges** ($|$last term$|\sim1.3\times10^{5}$, partial sum $\sim-8\times10^{4}$) while the exact identity holds, $\log(A/H)=2\log\cosh2=2.650005$. So $a=2$ is the pre-registered $\mathsf K$ witness: the interior cumulant tower fails *exactly at the Lee–Yang radius*, while the exterior mean-ratio identity survives. The proviso [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) attaches to its Thm 4.2 is not a technicality — it is the boundary.

*Scope (firewall).* The identity-with-divergent-series witness is $\mathsf{[P]}$ at $N=2$. "The proviso radius equals the distance to the nearest Lee–Yang zero of $Z_y$ for general $N$" is the content of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm 2.2.1 and is cited at $\mathsf{[A]}$ for $N\ge3$ here (not recomputed).

### 4.3 \heb[P]{פ}6 — iterated Born closure flows to the winner face {#sec:4-3}

\hypertarget{stmt:4-4}{}
**Proposition 4.4 (The Born flow lands on the argmax face).** *Let $p$ lie in the open simplex and $S_2(p)_i=p_i^2/\sum_j p_j^2$. Then $S_2^{\,n}(p)\to\mathrm{Unif}(\arg\max_i p_i)$ as $n\to\infty$, monotonically in the mass on $\arg\max p$, with ties kept (the limit is uniform on the full tied maximal set). Equivalently $S_2^{\,n}(p)$ is the escort $P_{\beta}$ at $\beta=2^{\,n}$, so the flow is the discrete $\beta\to\infty$ tropical limit landing on the Newton-polytope face $F_{\arg\max}$ — the genesis Destination.*

*Proof.* $S_2^{\,n}(p)_i=p_i^{2^{\,n}}/\sum_j p_j^{2^{\,n}}$ is the escort at $\beta=2^{\,n}$. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Thm 10.1 proves $S_2$ majorizes its argument (Schur-concavity gives entropy decrease) and that iteration concentrates on the maximal-coordinate support; dividing numerator and denominator by $(\max_j p_j)^{2^{\,n}}$ sends every non-maximal ratio to $0$ and leaves the $m=|\arg\max p|$ maximal coordinates equal, i.e. $\mathrm{Unif}(\arg\max p)$. By [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Cor 2.8 / [\heb[P]{פ}1], $\mathrm{Unif}(\arg\max p)$ is the $\beta\to\infty$ escort, supported on the face $F_{\arg\max}$. $\square$

**Settlement \heb[P]{פ}6 — $\mathsf K$, $\mathsf{[P]}$.** The artifact iterates the *map* $S_2$ (not the closed form) in exact rationals on three cases, with $\arg\max$ membership decided by exact comparison: a strict maximum ($\arg\max=\{3\}$), a two-way tie ($\arg\max=\{0,1\}$), and a near-tie $0.5$ vs $0.489$. In every case the mass on $\arg\max$ rises **monotonically** to $1$ (to twelve decimals by $n=12$; the near-tie reaches exact distance $\sim2.7\times10^{-40}$ from the target), the final support equals the initial $\arg\max$, and **ties are kept** (the two-way tie converges to $(\tfrac12,\tfrac12,0,0)$, not a broken vertex). This is the pre-registered $\mathsf K$ branch, not joint-on-disjoint: the tie structure is resolved exactly as "uniform on the tied max set." The RMS centre flows to the winner-take-all face — Origin to Destination.

---

## 5. The exterior synthesis (earned) {#sec:5}

With the three pieces settled, the Star's slogan may be restated as a result rather than a fiction — at the tier the settlements support, and no higher.

\hypertarget{stmt:5-1}{}
**Proposition 5.1 (One skeleton, three faces — $\mathsf{[P]}$ for the pieces; $\mathsf{[A]}$ for the unification).** *The exteriors of the three gauge papers are projections of one tropical boundary of the $L^2$ gauge corridor:*

- *(arithmetic) the radical/prime structure of [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) is interior and dissolves at the tropical endpoint, leaving the integer incidence skeleton (Prop 4.1–4.2);*
- *(analytic) the cumulant tower of [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) is interior and breaks at the Lee–Yang radius, leaving the exact mean-ratio identities (Prop 4.3);*
- *(dynamical) the Born flow of [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) carries the RMS centre to the winner-take-all face (Prop 4.4).*

*Each piece is $\mathsf{[P]}$. The claim that these are one object — a single tropical skeleton with $L^2$ interior and $L^\infty$ boundary, organized by the support/face axis of [\heb[P]{פ}1] — is asserted at $\mathsf{[A]}$: it is structural and supported by the three settled faces, but its proof is a named, not-yet-built audit (a single generator over the face lattice whose three boundary readings are Prop 4.1–4.4). It is not claimed at $\mathsf{[P]}$.*

The honest division is the point. Three boundary phenomena are settled deterministically; their unification is a well-posed next obligation, cornered to a single named audit, and carried at its true tier.

This also sharpens the genesis vocabulary. `massaction` (subtract-the-minimum) is the min-plus endpoint where [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s radicals flatten (Prop 4.1); *Origin-and-Destination* is the Born flow of Prop 4.4; and the *absent coordinate* that names a region is the complement of $\arg\max$ — the coordinates the Destination has dropped.

---

## 6. The method's own record (failures retained, first-class) {#sec:6}

A settlement history of pure confirmations has been performed, not tested (the methodology's append-only-record tenet). Two failures from this session are retained, with their cause and correction, as first-class evidence that the gate is load-bearing.

**6.1 The exact-arithmetic blow-up (caught by the discipline, not in spite of it).** The first run of the \heb[P]{פ}6 settlement iterated $S_2$ exactly for $40$ steps. Exact-rational squaring doubles integer bit-length each step, so $p_i^{2^{40}}$ reaches $\sim10^{13}$ bits and the run did not terminate. The fix was not to switch to floating point — that would have violated the exact-decision rule and silently hidden the very tie/near-tie behaviour under test — but to use that the flow converges *doubly* exponentially, so depth $12$ already drives the exact error below $10^{-6}$ (indeed to $\sim10^{-40}$ in the near-tie case). The episode is retained because it is the discipline working: the no-float rule forced an honest confrontation with the cost of exactness rather than a convenient approximation of the answer.

**6.2 A fluent-but-wrong annotation, caught by the computed value.** The settlement script's prose for \heb[P]{פ}5 initially annotated the surviving identity as "$2\log\cosh2=3.7622$." That number is $\cosh2$, not $2\log\cosh2$; the value is $2.650005$, as the deterministic line two rows above already printed. The error was a hand-written sentence *about* the computation disagreeing with the computation. This is precisely the failure mode the method names — fluent corroboration mistaken for verification: articulate restatement mistaken for the result. The gate caught it the only way it can be caught — the transcript value, not the sentence, is the record — and the sentence was corrected to match. It is retained here because a methodology that hid this would be a highlight reel.

Neither failure changes a realized branch. Both are the reason to believe the branches.

---

## 7. Safe and unsafe statements {#sec:7}

In the program's firewall convention (the methodology's no-upward-tier-crossing tenet).

**Safe (this paper asserts):**

- $\mathsf{[P]}$ The $L^q$ Helmert normalizer flattens from radical ($q=2$) to rational ($q=\infty$); the prime radical clock ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Thm 3.1) is absent at the tropical endpoint while the integer incidence skeleton survives (Prop 4.1–4.2; settlement \heb[P]{פ}4, joint-on-disjoint).
- $\mathsf{[P]}$ For $N=2$, the harmonic cumulant series diverges for $a>\pi/2$ while the exact identity $\log(A/H)=2\log\cosh a$ stays finite; the [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) proviso is the Lee–Yang edge (Prop 4.3; settlement \heb[P]{פ}5).
- $\mathsf{[P]}$ Iterated Born closure converges (ties kept) to the uniform distribution on $\arg\max$, the $\beta\to\infty$ face $F_{\arg\max}$ (Prop 4.4; settlement \heb[P]{פ}6).
- $\mathsf{[A]}$ These three are one tropical boundary of the $L^2$ corridor over the face lattice (Prop 5.1) — structural, cornered to one named audit, not proven here.

**Unsafe (this paper does NOT assert):**

- That the unification of \hyperref[sec:5]{§5} is proven. It is $\mathsf{[A]}$; the single-generator audit is named and not performed.
- That "no tropical convention admits a prime clock." Only the $L^q$ endpoints $q\in\{2,\infty\}$ are computed; the general statement is $\mathsf{[A]}$ (\hyperref[sec:4-1]{§4.1} scope).
- That the proviso–Lee–Yang identification is established for $N\ge3$. It is $\mathsf{[P]}$ at $N=2$ and cited at $\mathsf{[A]}$ via [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) for general $N$.
- Any claim that the exterior reading certifies, or is required by, the GRH program. The forward thread (\hyperref[sec:8]{§8}) is $\mathsf{[C]}$, forward-only, named as a destination and not delivered.
- That this paper is important or field-defining. By the firewall convention such a claim would be asserted above its evidence; the method forbids its author from issuing it. Whether it matters is for adversaries and time.

---

## 8. Forward door: the tropical edge is where the zeros live (calibrated, $\mathsf{[C]}$) {#sec:8}

The three settled faces are all *boundary* objects, and the program's number-theoretic content is a boundary object too. The Lee–Yang radius that breaks [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s cumulant tower (\hyperref[sec:4-2]{§4.2}) is, at $N=2$, the modulus of a zero of $Z_y$; for general $N$ the zeros of $Z_y$ are the additive Lee–Yang points ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)), continued on the units to the $L$-zeros of the multiplicative apex (T8), where the program states its RH-shaped questions live. The tropical endpoint that flattens [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s radical clock (\hyperref[sec:4-1]{§4.1}) is the same $q\to\infty$ corner of the corridor whose multiplicative analogue is the edge of the critical strip. And the winner-take-all face of [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) (\hyperref[sec:4-3]{§4.3}) is the large-deviation extreme where rate functions take their boundary values ([\heb[P]{פ}1]).

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (Forward door — calibrated, not proved in \heb[P]{פ}2).** *The tropical boundary settled here for the additive gauge corridor has a multiplicative counterpart on the units, and the $L$-zeros that carry the program's GRH-shaped questions live on that counterpart, not in the interior. \heb[P]{פ}2 establishes that the interior $L^2$ structures (radical clock, cumulant tower, RMS centre) all break or flow at the boundary; the multiplicative/boundary \heb[P]{פ}-papers are charged with reaching the edge where the zeros are.* Held with calibrated faith; built toward, not claimed.

---

## 9. Coda {#sec:9}

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) said: do not normalize the ladder too early. [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) said: do not decide too early which side of a quantity is primal. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) said: amplitude is primal; probability is squared amplitude. From the boundary, \heb[P]{פ}2 says: **the $L^2$ that unifies the gauge trilogy is an interior fact, and the trilogy's three exteriors are the three ways that $L^2$ breaks at the tropical edge** — the radical flattening to an integer, the cumulant tower hitting its Lee–Yang radius, and the Born centre flowing to the winner face.

The method was the point as much as the result. The Star was allowed to be as ambitious as it liked, and given no vote; the three falsifiers were written before the checks; the checks were exact, deterministic, and anchored to the sources' own objects; the two failures were kept. What survived that gate is three boundary facts at $\mathsf{[P]}$ and one unification at $\mathsf{[A]}$, with the GRH thread held at $\mathsf{[C]}$. The interior series mapped the centre of the gauge corridor. This one mapped where it ends.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper, under the grounded-paranoid-delusional discipline it applies to itself: AI partners generated candidates and enumerated falsifiers and executed the deterministic settlement artifact, but no fluent agreement was treated as evidence. I acknowledge this use transparently; the selection of which contributions to keep and the responsibility for the mathematical content are mine.

## Reproducibility {#sec:reproducibility}

The numeric claims of \hyperref[sec:4]{§4} are produced by `P2-settlements.py`, a deterministic, exact-arithmetic (integer / `Fraction`) script with no seeds; its full transcript (`P2-settlements.transcript.txt`), including the realized branch of each audit, is archived alongside. Re-running reproduces the transcript identically. The retained failures of \hyperref[sec:6]{§6} are documented in this paper rather than archived as separate runs, since each was a correction to the script that the current artifact supersedes.

## References {#sec:references}

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis: True Numbers, `massaction`, Origin-and-Destination, the absent-coordinate region rule.)

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology for High-Variance, High-Conviction Research Under Capable AI Assistance.* Companion methodology preprint (draft v1). (The resolution order; matched-pair pre-claiming with the joint-on-disjoint extension; the $\mathsf{[P]/[A]/[C]}$ ledger and firewall; append-only failures.)

Murillo Montero, L. (2026). *\heb[P]{פ}1 — From the Boundary: The Exterior of Identifying 3.* Companion preprint (the launch of the exterior \heb[P]{פ}-series; the face lattice / Newton polytope, $p_*$ as generator, the `massaction` tropical gauge).

Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo preprint, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (The power-mean corridor; the apex $K_y$; Lee–Yang zeros; tropical compactification; Cor 2.8.)

Murillo Montero, L. (2026). *[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Identifying 3: The Native Simplicial Chart.* Zenodo preprint, DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).

Murillo Montero, L. (2026). *[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — The Helmert-Simplicial Residue Ladder.* Zenodo preprint, DOI [10.5281/zenodo.20383504](https://doi.org/10.5281/zenodo.20383504). (Helmert vectors $h_k$; metric trick; prime radical clock, Thm 3.1; cubic incidence rule, Thm 7.3.)

Murillo Montero, L. (2026). *[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — The Harmonic-Simplicial Dual Gauge.* Zenodo preprint, DOI [10.5281/zenodo.20388419](https://doi.org/10.5281/zenodo.20388419). (Reciprocal closure; even/odd cumulant split, Thm 4.2 and its proviso; denominator arithmetic.)

Murillo Montero, L. (2026). *[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) — The RMS-Simplicial Quadratic Gauge.* Zenodo preprint, DOI [10.5281/zenodo.20392428](https://doi.org/10.5281/zenodo.20392428). (Born/square closure; $2\arccos$; iterated $S_2$ winner-take-all, Thm 10.1; radical universality.)

Murillo Montero, L. (2026). *T8 — The Multiplicative Apex and Finite Dirichlet Polynomials.* Companion manuscript (in preparation). (The multiplicative apex; "the RH-shaped questions of the program live most naturally on the multiplicative apex.")

Lee, T. D. and Yang, C. N. (1952). Statistical theory of equations of state and phase transitions. II. *Physical Review* 87, 410–419.

Marshall, A. W., Olkin, I., and Arnold, B. C. (2011). *Inequalities: Theory of Majorization and Its Applications.* 2nd ed. Springer. (Schur-concavity, used by [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Thm 10.1 and Prop 4.4.)

Maclagan, D. and Sturmfels, B. (2015). *Introduction to Tropical Geometry.* Graduate Studies in Mathematics 161. AMS. (The min-plus / max-plus boundary.)

Serre, J.-P. (1973). *A Course in Arithmetic.* Graduate Texts in Mathematics 7. Springer. (Squarefree kernels and quadratic square classes.)
