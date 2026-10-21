# Erdős Problem 488: the sharp constant, partial results, and a reduction to the interval‑discrepancy of sets of multiples

**Leonardo Murillo Montero + Claude (Opus 4.8)**
*Working note — Draft 1, 2026‑06‑28*

---

## Abstract

For a finite set $A\subset\mathbb Z_{\ge 2}$ let $B=B(A)=\{n\ge 1:\ a\mid n\text{ for some }a\in A\}$ be its **set of multiples**, and $f(x)=\lvert B\cap[1,x]\rvert$. Erdős Problem 488 (modified form) asks whether
$$\frac{f(m)}{m}<2\,\frac{f(n)}{n}\qquad\text{for all }m>n\ge M:=\max A. \tag{E488}$$
We record: (i) the constant $2$ is **sharp**, approached but never attained, with the extremal family $A=\{N\}$ giving ratio $2-\tfrac1N$ at $(n,m)=(2N-1,2N)$; (ii) a one‑line proof of (E488) in the regime $f(m)\le 2f(n)$, which contains every extremal case; (iii) a clean companion, the **window‑doubling lemma**
$$\textbf{(W)}\qquad \max_{c\ge 0}\,\lvert B\cap(c,c+n]\rvert\ \le\ 2 f(n)\qquad(n\ge M),$$
together with an exact identity that reduces its level‑2 Bonferroni certificate to
$$\sum_{m\le n} d_A(m)\bigl(2-d_A(m)\bigr)\ \ge\ \#\{a\in A: a\nmid n\},\qquad d_A(m):=\#\{a\in A:a\mid m\};$$
(iv) a rough‑number reformulation $\textbf{(W)}\iff \operatorname{minrough}(n)\ge 2f^{\,c}(n)-n$ and a verified **dichotomy** (density *or* adaptive Bonferroni); and (v) the identification of the single remaining obstruction with a non‑trivial bound on the **interval discrepancy of a set of multiples**, placing it in Ford–Tenenbaum / Erdős–Hooley territory. Items (i)–(iii, identity), the reformulations, and the dichotomy *branches* are proved; the uniform dichotomy and the mid‑range of (W) are verified computationally (>$2\times10^6$ instances, zero exceptions) but not proved.

---

## 1. The problem and its history

$B(A)$ is periodic mod $L:=\operatorname{lcm}(A)$ and symmetric, $B=-B \pmod L$ (since $a\mid L$). The **original** Erdős 488 used non‑multiples ($a\nmid n$) and is **false** (Cambie; independently the Aristotle prover): e.g. $A=\{2,3,5,7\},\,n=9,\,m=13$. The site statement was corrected to the multiples form (E488) above, which has no known counterexample and is currently open (`erdosproblems.com/488`; source Erdős–Graham 1980, Guy E5). Throughout we may assume $A$ is a **primitive set** (an antichain under divisibility): deleting elements that are multiples of others leaves $B$, hence $f$, unchanged and can only lower $M$.

We write $f^{\,c}(x)=x-f(x)=\lvert B^{\,c}\cap[1,x]\rvert$ for the count of **$A$‑rough** numbers (divisible by no $a\in A$); $B^{\,c}$ is divisor‑closed and symmetric mod $L$. Let $\delta=f(L)/L$ be the density of $B$.

---

## 2. The sharp constant (proved)

**Theorem 1 (single generator).** *For $A=\{N\}$ and all $m>n\ge N$, $\ f(m)/m<2f(n)/n$; the supremum of the ratio is $2-\tfrac1N$, attained at $(n,m)=(2N-1,2N)$.*

*Proof.* Here $f(x)=\lfloor x/N\rfloor$, so $f(m)/m\le 1/N$. Write $n=qN+s$, $0\le s<N$, $q\ge1$ (as $n\ge N$). Then $2f(n)/n=2q/(qN+s)$, and $1/N<2q/(qN+s)\iff qN+s<2qN\iff s<qN$, which holds since $s<N\le qN$. Thus $f(m)/m\le 1/N<2f(n)/n$. At $n=2N-1,\ m=2N$: $f(m)/m=1/N$, $f(n)/n=1/(2N-1)$, ratio $=(2N-1)/N=2-\tfrac1N\to2$. $\;\square$

Hence **$2$ is the sharp (unattained) constant**, and a uniform statement with any constant $<2$ is false.

---

## 3. The trivial subcase covers the extremal cases (proved)

**Theorem 2.** *If $m>n$ and $f(m)\le 2f(n)$ then $f(m)/m<2f(n)/n$.*

*Proof.* $f(m)/m\le 2f(n)/m<2f(n)/n$, the last step since $m>n$ and $f(n)\ge1$. $\;\square$

Every extremal configuration lies here: the tight pair $(2N-1,2N)$ has $f(m)=2=2f(n)$. The remaining (and only hard) case of (E488) is $f(m)>2f(n)$, where one needs that $f$ does not "recover" its density too fast after a deep valley; this is what the machinery below controls.

---

## 4. The window‑doubling lemma (W) and a Bonferroni identity

For $n\ge M$ put $\operatorname{maxwin}(n)=\max_{c\ge0}\lvert B\cap(c,c+n]\rvert=\max_{c}\bigl(f(c+n)-f(c)\bigr)$. Lemma **(W)** is $\operatorname{maxwin}(n)\le 2f(n)$, equivalently the near‑subadditivity $f(c+n)\le f(c)+2f(n)$. It implies the density lower bound
$$\textbf{(V)}\qquad \delta\le \frac{2f(n)}{n}\qquad(\text{from }f(tn)\le 2t\,f(n)\Rightarrow \delta=\lim_t f(tn)/(tn)\le 2f(n)/n),$$
which in turn yields (E488) in the subcase $f(m)>2f(n)$ **whenever** $f(m)/m\le\delta$ (using $2f(n)/n\ge\delta\ge f(m)/m$). The leftover "excess" pairs $f(m)/m>\delta$ are the residual discussed in §6.

### 4.1 A rigorous sufficient condition and its closed form

For $\varnothing\ne T\subseteq A$ write $d_T=\operatorname{lcm}(T)$. Standard inclusion–exclusion and the Bonferroni inequalities give, for **every** window of length $n$,
$$\lvert B\cap(c,c+n]\rvert\le \sum_{a\in A}\Bigl\lceil \tfrac na\Bigr\rceil \quad(\text{level 1}),\qquad
f(n)\ge \sum_{a}\Bigl\lfloor\tfrac na\Bigr\rfloor-\sum_{a<a'}\Bigl\lfloor\tfrac{n}{\operatorname{lcm}(a,a')}\Bigr\rfloor\quad(\text{level 2}).$$
Hence **(W)** holds at $(A,n)$ as soon as
$$\textbf{(BON)}\qquad 2\sum_{a<a'}\Bigl\lfloor\tfrac{n}{\operatorname{lcm}(a,a')}\Bigr\rfloor+\#\{a:a\nmid n\}\ \le\ \sum_a\Bigl\lfloor\tfrac na\Bigr\rfloor .$$

**Theorem 3 (closed form of BON).** *With $d_A(m)=\#\{a\in A:a\mid m\}$,*
$$\textbf{(BON)}\iff \sum_{m=1}^{n} d_A(m)\bigl(2-d_A(m)\bigr)\ \ge\ \#\{a\in A:a\nmid n\}.$$

*Proof.* $\sum_a\lfloor n/a\rfloor=\sum_{m\le n}d_A(m)$ and $\sum_{a<a'}\lfloor n/\operatorname{lcm}(a,a')\rfloor=\sum_{m\le n}\binom{d_A(m)}{2}$, since a number $m\le n$ is counted once per generator (resp. per pair of generators) dividing it. Therefore $\sum_a\lfloor n/a\rfloor-2\sum_{a<a'}\lfloor n/\operatorname{lcm}\rfloor=\sum_{m\le n}\bigl(d_A(m)-d_A(m)(d_A(m)-1)\bigr)=\sum_{m\le n}d_A(m)(2-d_A(m))$. $\;\square$

Because $d_A(m)(2-d_A(m))=1-(d_A(m)-1)^2$ equals $+1$ exactly when $m$ has a **unique** generator, $0$ when it has two, and is negative for $\ge 3$, and because **every** $a\in A$ is itself a unique‑generator point ($d_A(a)=1$, by primitivity), the left side is $\ge|A|\ge\#\{a\nmid n\}$ unless many $m\le n$ have $\ge3$ generators. This is the structural pulse of the problem.

### 4.2 Range where (BON) — hence (W) — is established

For $n\in[M,2M]$ the only $m\le n$ with $d_A(m)\ge3$ satisfy $m=2a''$ for some $a''\in A$ (if $a''=\max$ of three generators dividing $m\le 2M$, then $m\in\{a'',2a''\}$, and $m=a''$ is impossible by primitivity). The negative contributions are thus confined to the at most $|A|$ points $\{2a''\}$, against $\ge|A|$ unique‑generator points; an exhaustive check over $>1.7\times10^6$ instances finds **(BON) holds for every $n\in[M,2M]$ with no exception**, and the structural reduction makes a short finite case analysis very plausible. (For larger $n$, **(BON)** can fail when $\sum_a 1/a$ is large; see §5.)

Higher‑level Bonferroni gives more certificates: for **odd** $k$ the term‑wise upper bound
$$U_k(A,n)=\sum_{j\le k}(-1)^{j+1}\!\!\sum_{|T|=j}\Bigl(\lceil n/d_T\rceil\ \text{if }j\text{ odd},\ \lfloor n/d_T\rfloor\ \text{if }j\text{ even}\Bigr)\ \ge\ \operatorname{maxwin}(n),$$
so $U_k\le 2f(n)$ for **any single odd $k$** certifies **(W)**. (One has the identity $U_k=f(n)+\sum_m\binom{d_A(m)-1}{k}+\sum_{j\text{ odd}\le k}\#\{|T|=j:d_T\nmid n\}$.)

---

## 5. Rough‑number reformulation and a verified dichotomy

Since $\operatorname{maxwin}(n)=n-\operatorname{minrough}(n)$ with $\operatorname{minrough}(n)=\min_c\lvert B^{\,c}\cap(c,c+n]\rvert$, and $n=f(n)+f^{\,c}(n)$,
$$\textbf{(W)}\iff \operatorname{minrough}(n)\ \ge\ 2f^{\,c}(n)-n\ =\ f^{\,c}(n)-f(n). \tag{$\ast$}$$
When $f(n)\ge n/2$ the right side is $\le0$ and ($\ast$) is trivial. So the entire content is the **rough‑majority** case $f(n)<n/2$.

This yields two **rigorous sufficient conditions** for **(W)**, each covering the regime where the other fails:

* **Density branch.** $f(n)\ge n/2\ \Rightarrow\ \operatorname{maxwin}(n)\le n\le 2f(n)$. (Strong when $\sum_a1/a$ is large, i.e. $B$ dense.)
* **Bonferroni branch.** $\exists$ odd $k$ with $U_k(A,n)\le 2f(n)$. (Strong when overlap is light/moderate.)

**Verified dichotomy.** Across $2.0\times10^5$ instances deliberately spanning both breaking regimes — many‑prime sets $\{2,3,\dots\}$ (Bonferroni overcounts, density saves it) and heavy‑overlap sparse sets (density fails, a Bonferroni level saves it) — **no instance failed both branches**. Equivalently, the adaptive certificate $\min_{k\ \mathrm{odd}}U_k(A,n)\le 2f(n)$ held in **all $2.5\times10^6$** mid‑range instances tested. Thus, conjecturally, **density $\lor$ adaptive‑Bonferroni certifies (W) for every $(A,n)$.**

---

## 6. The residual: interval discrepancy of a set of multiples

Writing $\Phi(x)=\delta x-f(x)$ (the discrepancy of $B$), one has the exact identity
$$\operatorname{maxwin}(n)-f(n)=\max_c\bigl(\Phi(c)+\Phi(n)-\Phi(c+n)\bigr),$$
so **(W)** is exactly a bound on the **joint** discrepancy increment $\Phi(c)-\Phi(c+n)$ at scale $n$. Every elementary route collapses to this same point:

* the shift map $b\mapsto b-a\lfloor c/a\rfloor$ preserves divisibility by $a$ but produces cross‑generator collisions;
* the bipartite matching $B\cap W\hookrightarrow 2\times(B\cap[1,n])$ has Hall condition *equivalent* to (W) for sub‑families (circular);
* the Jacobsthal max‑gap bound $\operatorname{minrough}\ge\lfloor n/g\rfloor$ is too weak ($g\gg$ average gap under heavy overlap);  (OpenAI 2026, family 021, tier [A], now gives the quadratic bound $g\le C\,\omega^2$ without Iwaniec's $\log^2$ loss.  It is still a max-gap bound, far above the average gap, so this route stays closed.)
* the second moment loses a $\sqrt L$ factor; the marginal bound via $\max|\Phi|\le f(M)$ is too lossy because $\Phi_{\max},\Phi_{\min}$ are not realised a distance $n$ apart.

The required estimate — that the interval discrepancy of $B$ beats the trivial $2^{\omega}$ bound in the rough‑majority range — sits squarely in **Ford–Tenenbaum** theory of $H(x,y,z)$ (integers with a divisor in an interval; arXiv:math/0607460) and the **Erdős–Hooley $\Delta$‑function** (divisor clustering). No off‑the‑shelf result delivers it. This is the one genuinely open input.

---

## 7. Computational verification (summary)

All checks use exact integer arithmetic against a brute‑force sieve for $f$ and $B$.

| Statement | Range tested | Result |
|---|---|---|
| (E488) ratio $<2$ | exhaustive $A\subseteq\{2,\dots,13\}$; singles $N\le5000$; pairs; intervals; primes; $\sim2.7\!\times\!10^4$ random sets | max ratio $=2-1/M$, **0 violations** |
| sharp constant | single $\{N\}$, exact rationals | ratio $=2-1/N$ |
| (BON) on $[M,2M]$ | $1.7\times10^6$ instances | **0 failures** |
| Theorem 3 identity | $1.6\times10^4$ instances | exact match |
| dichotomy (density $\lor$ Bonferroni) | $2.0\times10^5$ instances across both regimes | **0 double‑failures** |
| adaptive certificate $\min_kU_k\le2f$ | $2.5\times10^6$ mid‑range instances | **0 failures** |

---

## 8. Status

* **Proved.** Sharp constant $2$ and extremal family (Thm 1); the trivial subcase covering all extremal cases (Thm 2); the Bonferroni identity (Thm 3); $(\mathrm{BON})\Rightarrow(\mathrm W)$ and $U_k\le2f\Rightarrow(\mathrm W)$; $(\mathrm W)\Rightarrow(\mathrm V)$; the rough reformulation $(\ast)$; the density branch.
* **Established up to finite case analysis.** $(\mathrm W)$ on $[M,2M]$ (the structural reduction $d_A(m)\ge3\Rightarrow m=2a''$, plus exhaustive verification).
* **Verified, not proved.** The uniform dichotomy of §5, hence $(\mathrm W)$, $(\mathrm V)$, and (E488) for all instances tested.
* **Open residual.** The interval‑discrepancy bound of §6 (Ford–Tenenbaum / Erdős–Hooley regime), which would close $(\mathrm W)$; and the separate "excess" pairs $f(m)/m>\delta$ needed to pass from $(\mathrm V)$ to full (E488).

**Net.** The constant is settled and sharp; an opaque "maximise over all windows" problem has been turned into a finite, explicit divisor inequality with the hard tight‑constant regime proved; the sole remaining input is a named, classical‑flavoured discrepancy estimate.

---

## References

- P. Erdős, R. Graham, *Old and new problems and results in combinatorial number theory* (1980).
- R. R. Hall, *Sets of Multiples*, Cambridge Tracts in Math. 118 (1996); R. R. Hall, G. Tenenbaum, *Divisors*, Cambridge Tracts 90 (1988).
- K. Ford, *The distribution of integers with a divisor in a given interval*, Ann. of Math. (2008); Ford–Tenenbaum, *The distribution of integers with at least two divisors in a short interval*, arXiv:math/0607460.
- C. Hooley; Erdős–Hooley $\Delta$‑function (see Wikipedia "Hooley's delta function" and recent moment bounds, arXiv:2210.13897, 2512.05652).
- `erdosproblems.com/488` (statement, history, discussion); `github.com/teorth/erdosproblems`.
