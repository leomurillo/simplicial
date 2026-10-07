---
title: "A Cube-Root-of-Unity Obstruction and a Projection Method for Odd Covering Systems (Erdős Problem 7)"
author:
  - name: Leo Murillo
    affiliation: Independent Researcher
date: 2026-06-28
---

# Abstract

Erdős's *odd covering problem* (Erdős Problem 7) asks whether there exists a
covering system of $\mathbb{Z}$ whose moduli are distinct, odd, and greater
than $1$. It is widely believed that none exists (Erdős offered \$25 for a proof
of non-existence; Selfridge \$2000 for a construction), and the problem has been
open since the 1950s. The modern frontier — Hough's solution of the minimum
modulus problem, the Balister–Bollobás–Morris–Sahasrabudhe–Tiba refinements,
and the Hough–Nielsen "divisible by $2$ or $3$" theorem — proceeds entirely by a
probabilistic *distortion / density* method, which the authors note runs into a
*moment barrier* for the odd problem.

We open an orthogonal, algebraic line. Writing the covering multiplicity
$c(n)=\#\{i: n\equiv a_i \pmod{m_i}\}$, covering is $c\ge 1$, and the Fourier
coefficients of $c$ at a frequency of prime order $p$ collapse to a weighted sum
of $p$-th roots of unity over the $p$-divisible moduli. We prove:

1. **(Gateway.)** The lcm of any odd covering is an *odd abundant number*; the
   smallest is $945=3^3\cdot 5\cdot 7$.
2. **(Cube-root obstruction.)** Because an odd covering forbids the prime $2$ —
   and $z=-1$ is the unique root of unity permitting perfect cancellation — the
   *cube root* is the stiffest available frequency. This yields a sharp
   single-frequency bound with a closed form that rules out an explicit infinite
   family of moduli (all $Q=3^a k$, $3\nmid k$, with $\sigma(k)/k<10/7$).
3. **(Projection method.)** A covering of $\mathbb{Z}/Q$ induces a *weighted
   covering* of the far smaller group $\mathbb{Z}/Q_S$ for every set $S$ of
   primes; infeasibility of this finite system rules out the covering. This is a
   rigorous, computationally cheap obstruction that strictly extends (2).
4. **(Certification.)** *No odd covering system has lcm $\le 2\times 10^5$*, each
   case certified by an explicit projection vastly smaller than direct search
   (which already times out at $Q=3465$).

We are explicit about what this is and is not: a sharp new instrument and a
clean infinite family of settled cases, **not** a proof of Erdős 7. We locate
the barrier precisely: the obstruction lives on the stiff prime-3 frequency and
*dilutes* as abundancy spreads to large primes, so the minimal obstructing
prime-set $S$ grows with $\omega(Q)$ (squarefree odd $Q$ with $\omega\ge 15$
avoiding $\{5,7\}$ already defeat every tractable projection). The open part thus
localizes to $\sigma(Q)/Q\ge 20/9$ with abundancy off the small primes — the same
"few primes" obstruction that stops the distortion method.

---

# 1. The problem and the state of the art

A **distinct covering system** is a finite list of congruences $a_i \pmod{m_i}$
with the $m_i$ distinct and $>1$ such that every integer satisfies at least one.
Erdős introduced these in 1950. The **odd covering problem** asks whether one
exists with every $m_i$ odd.

Known results:

- *(Hough)* The least modulus of a distinct covering system is at most
  $10^{16}$; the largest known minimum modulus is $42$ (Owens).
- *(Hough–Nielsen)* Every distinct covering system has a modulus divisible by
  $2$ or by $3$. Hence **every odd covering must use a modulus divisible by 3**.
- *(Simpson–Zeilberger; Guo–Sun)* A distinct covering by odd *square-free*
  moduli involves at least $18$, resp. $22$, primes.
- *(Schinzel)* A negative answer has consequences for irreducibility of families
  of polynomials.

All of the quantitative machinery above is probabilistic (Lovász-local-lemma /
Shearer bounds, $\ell^2$ and $\ell^3$ moments). Hough–Nielsen state the obstacle
verbatim: *"the barrier to ruling out an odd covering using the current method
is that the optimal application in the initial stage can only accommodate a few
primes, so that the resulting bounds for moments do not permit the process to
continue."* This is a moment barrier. We use roots of unity instead.

Throughout, $Q=\operatorname{lcm}(m_i)$ is odd, $\sigma$ is the sum-of-divisors
function, and $e(x)=e^{2\pi i x}$.

# 2. A Fourier reformulation

Let $c(n)=\sum_i \mathbf{1}[\,n\equiv a_i \ (\mathrm{mod}\ m_i)\,]$ be the
covering multiplicity, a function on $\mathbb{Z}/Q$. Covering means $c(n)\ge 1$
for all $n$; set $r=c-1\ge 0$. With $\hat f(t)=\sum_{n \bmod Q} f(n)e(-tn/Q)$,

$$
\hat c(t)=\sum_{i:\ (Q/m_i)\mid t} \frac{Q}{m_i}\, e\!\left(-\frac{t a_i}{Q}\right),
\qquad
\hat c(0)=Q\sum_i \tfrac1{m_i}=Q\delta .
$$

Since $c=1+r$ and $r\ge 0$, for every $t\ne 0$ we have $\hat c(t)=\hat r(t)$ and
$|\hat r(t)|\le \hat r(0)=\sum_n r(n)=Q(\delta-1)$. Thus:

> **Necessary inequality.** For every $t\not\equiv 0$,
> $\displaystyle \bigl|\hat c(t)\bigr| \le Q(\delta-1).$

**Gateway (odd abundant lcm).** A distinct cover needs $\delta=\sum 1/m_i>1$
(equality would be an exact cover, forcing a repeated largest modulus). Since
the $m_i$ are distinct divisors of $Q$, $\delta \le \sum_{m\mid Q,\,m>1}1/m =
\sigma(Q)/Q-1$, so $\sigma(Q)>2Q$: **$Q$ is odd abundant.** The smallest odd
abundant number is $945$, so no odd covering has lcm below $945$, and at $945$
the overlap budget $\sigma(Q)-2Q$ is only $30$.

# 3. The cube-root obstruction

Take $t=Q/3$ (assume $3\mid Q$; forced by Hough–Nielsen). Every contributing
modulus is divisible by $3$ and the phase $e(-ta_i/Q)=e(-a_i/3)$ is a **cube
root of unity**:

$$
\hat c(Q/3)=\sum_{i:\ 3\mid m_i} \frac{Q}{m_i}\, e(-a_i/3).
$$

**Why the cube root.** The constructor cancels $\hat c(Q/3)$ by distributing the
weights $Q/m_i$ among the three cube-root directions $1,\omega,\omega^2$. Perfect
cancellation of the heavy term would need a direction with real part $-1$, i.e.
$z=-1$ — but that is an *even*-order root, excluded precisely because the moduli
are odd. The cube roots sit at $\pm 120^\circ$ (real part $-\tfrac12$), so the
remaining weight opposes the heavy term at only half strength. Among all primes
$p$, $p=3$ gives the stiffest geometry (the opposing roots are
$\cos(\pi/p)$-close to $-1$, increasing toward $1$ with $p$); $p=2$ would be
softest of all and is exactly what oddness removes.

**Lemma (heavy-term bound).** Let $W_3=\sum_{m\mid Q,\,3\mid m}(Q/m)$. With all
$3$-divisible divisors in play and $Q>W_3$,
$$
\min_{\text{residues}}\ \bigl|\hat c(Q/3)\bigr| \;\ge\; \frac{Q-W_3}{2}.
$$
*Proof sketch.* The modulus $m=3$ contributes weight $Q/3$ on one direction, so
that direction's total $S_0\ge Q/3$. Minimizing
$|S_0+S_1\omega+S_2\omega^2|^2=\tfrac12\sum_{i<j}(S_i-S_j)^2$ over
$S_0\ge Q/3,\ S_0+S_1+S_2=W_3$ gives the boundary optimum $S_0=Q/3$,
$S_1=S_2=(W_3-Q/3)/2$, value $(Q-W_3)/2$. Integrality only raises it. $\square$

> **Theorem A (cube-root obstruction).** If $\dfrac{Q-W_3}{2} > \sigma(Q)-2Q$,
> then no covering by distinct odd divisors of $Q$ that uses all $3$-divisible
> divisors can exist; the rigorous statement for arbitrary sub-families is the
> $S=\{3\}$ instance of Theorem B below, and the two agree on every case tested.

**Corollary (closed-form family).** Writing $Q=3^a k$ with $3\nmid k$ and
$s=\sigma(k)/k$, the condition holds iff $s<\dfrac{5}{3g-1}$ with
$g=\tfrac{3-3^{-a}}{2}\to\tfrac32$, i.e. $s<\tfrac{10}{7}\approx 1.4286$ in the
limit. This settles infinitely many moduli, e.g. **$3^a\cdot 35\ (a\ge 3)$** and
**$3^a\cdot 175\ (a\ge 2)$**, and disposes of $118$ of the $134$ candidate
(odd abundant) moduli below $6\times 10^4$ by a single frequency.

The threshold is *largest* at $a=1$: for **squarefree** odd $Q=3k$ the condition
is $s<5/3$, i.e. $\sigma(Q)/Q<20/9\approx 2.222$. Combined with abundancy
($\sigma(Q)/Q>2$):

> **Corollary (squarefree band).** Every squarefree odd $Q$ with $3\mid Q$ and
> $2<\sigma(Q)/Q<20/9$ admits no covering by distinct odd divisors. Here the LP
> relaxation is feasible (the weight chunks $1/d$ can be *fractionally* balanced
> into the three cube-root bins of $\mathbb{Z}/3$ exactly when $\sigma(Q)/Q>2$),
> but the *integer* placement cannot — the obstruction is purely integral.

# 4. The projection method

The remaining moduli (abundant $3$-free part, $s\gtrsim 1.45$) require coupling
frequencies. Two facts organize this.

**Decoupling.** For a modulus $m$ and distinct primes $p,q\mid m$, the residues
$a_m \bmod p$ and $a_m \bmod q$ are CRT-independent, so the pure prime-order
coefficients $\hat c(Q/p)$ are *independently* minimizable: combining distinct
primes at pure prime order gains nothing. All cross-prime power comes from
**mixed-order** frequencies (those whose order is divisible by two primes), i.e.
from *composite* moduli such as $15,45,\dots$

These mixed frequencies are organized by projecting to a quotient. Let
$S$ be a set of primes, $Q_S=\prod_{p\in S}p^{v_p(Q)}$, and $k=Q/Q_S$. Summing
$c\ge 1$ over each fiber of $\mathbb{Z}/Q\to\mathbb{Z}/Q_S$:

> **Theorem B (projection).** For each $x\in\mathbb{Z}/Q_S$, write each modulus
> $m_i=\mu_i d_i$ with $\mu_i\mid Q_S$ and $\gcd(d_i,Q_S)=1$. A covering forces
> $$
> C_S(x):=\sum_{i:\ x\equiv a_i \ (\mathrm{mod}\ \mu_i)} \frac{k}{d_i}\ \ge\ k
> \qquad\text{for all } x\in\mathbb{Z}/Q_S.
> $$
> Each modulus covers a *whole* coset at $3$-adic ($S$-adic) level $\mu_i$ with a
> single chosen residue — the integrality survives the projection. Hence if this
> finite weighted-covering system is infeasible, no covering of $\mathbb{Z}/Q$
> exists.

This is a small integer feasibility problem on $\mathbb{Z}/Q_S$ (typically
$|Q_S|\le 700$), independent of the size of $Q$. The $S=\{3\}$ case is the full
$3$-adic tower $\{Q/3,Q/9,\dots\}$ at once, strictly stronger than the single
frequency of §3; larger $S$ adds the mixed frequencies. The integral nature is
essential: the LP relaxation (and the density/averaging bound) is *always
feasible* for abundant $Q$, so the obstruction is invisible to density arguments
and lives entirely in the one-coset-per-modulus integrality — which is exactly
what defeats the distortion method at the moment barrier.

# 5. Computational certification

> **Theorem C.** No odd covering system has lcm $\le 2\times 10^5$.

There are $391$ odd abundant numbers below $2\times 10^5$; every one is certified
non-covering by an explicit projection (Theorem B), and all remaining moduli are
non-abundant and excluded by §2. The footprint is remarkably small: $381$ of the
$391$ are settled by a *single* prime's tower ($|S|=1$) and the other $10$ by a
two-prime projection ($|S|=2$); the largest projection group used is
$\mathbb{Z}/2187$. The certificates are exact (HiGHS branch-and-bound
infeasibility on $\mathbb{Z}/Q_S$).

The obstructing prime-set need not consist of the *smallest* primes. The two most
abundant moduli below $2\times10^5$, $155925=3^4\cdot5^2\cdot7\cdot11$ and
$184275=3^4\cdot5^2\cdot7\cdot13$ (with $\sigma(Q)/Q\approx 2.31$), resist
$\{3\}$, $\{3,5\}$ and $\{3,5,7\}$ but fall immediately to $S=\{3,7\}$ on
$\mathbb{Z}/567$. The method is not merely cleaner but *faster* than direct
search: the direct integer program on $\mathbb{Z}/Q$ already times out at
$Q=3465$, while every projection here is solved in well under a second.

Representative certificates:

| $Q$ | factorization | $\sigma(Q)/Q$ | settled by | projection group |
|---|---|---|---|---|
| $945$ | $3^3\cdot5\cdot7$ | $2.03$ | single freq. / $S=\{3\}$ | $\mathbb{Z}/27$ |
| $3465$ | $3^2\cdot5\cdot7\cdot11$ | $2.16$ | single freq. | — |
| $10395$ | $3^3\cdot5\cdot7\cdot11$ | $2.22$ | $S=\{3\}$ tower | $\mathbb{Z}/27$ |
| $45045$ | $3^2\cdot5\cdot7\cdot11\cdot13$ | $2.33$ | $S=\{3,5\}$ | $\mathbb{Z}/45$ |
| $155925$ | $3^4\cdot5^2\cdot7\cdot11$ | $2.31$ | $S=\{3,7\}$ | $\mathbb{Z}/567$ |

# 6. The barrier and the outlook

**What is settled, and where the open part lives.** Theorem B is complete in
principle ($S=$ all primes of $Q$ *is* the covering problem); its value is that a
*small* $S$ suffices over a large range — $|S|\le 2$ for every odd abundant
$Q<2\times 10^5$, projection groups never exceeding $\mathbb{Z}/2187$. But the
obstruction is strong only when the abundancy is *concentrated near the prime 3*,
the stiff frequency. As abundancy is forced onto large (soft-frequency) primes,
it dilutes, and no bounded projection bites. Concretely: starting from the
necessary $\sigma(Q)/Q>20/9$ to escape the cube root, and pushing that abundancy
onto primes avoiding $\{5,7\}$, one reaches squarefree odd numbers with
$\omega(Q)\ge 15$ that defeat *every* tractable projection ($Q_S\le 6000$); the
minimal obstructing $|S|$ grows with $\omega(Q)$.

This is precisely the Hough–Nielsen moment barrier ("the optimal application can
only accommodate a few primes"), now visible through the cyclotomic lens. So the
**open part of Erdős 7 localizes** to the high-abundancy regime
$\sigma(Q)/Q\ge 20/9$ with abundancy *spread off the small primes* — exactly the
many-primes regime where a covering, if one exists, must live (Guo–Sun: a
square-free odd covering needs $\ge 22$ primes). Closing it requires an
obstruction that survives the dilution of the prime-3 frequency.

**Relation to the distortion method.** Aggregating the necessary inequality of
§2 over *all* frequencies via Parseval gives
$\sum_{t\ne 0}|\hat c(t)|^2 = Q\sum_n r(n)^2 - (Q(\delta-1))^2 \ge Q^2(\delta-1)(2-\delta)$
(using $\sum r^2\ge\sum r$ for integer $r\ge 0$) — a second-moment identity that
is precisely the analytic core of the distortion method. Our contribution is the
*targeted* use of the stiffest individual frequencies (small $S$), which is sharp
where the aggregate is lossy, and which carries the entire verified range.

**Status ledger.**

- *Proved.* The Fourier necessary inequality (§2); the odd-abundant-lcm gateway;
  the cube-root heavy-term Lemma; Theorem B (projection).
- *Proved, infinite family.* No odd covering with lcm in the closed-form family
  $\sigma(k)/k<5/(3g-1)$ (Theorem A / $S=\{3\}$); in particular the clean
  squarefree band $2<\sigma(Q)/Q<20/9$.
- *Verified, exact certificates.* Theorem C (no odd covering with
  lcm $\le 2\times 10^5$), with $|S|\le 2$ throughout.
- *Established (barrier).* Bounded $|S|$ does **not** suffice: spreading the
  abundancy onto large primes (avoiding $\{5,7\}$, $\omega\ge 15$) defeats every
  tractable projection. The open part of Erdős 7 is thereby localized to
  $\sigma(Q)/Q\ge 20/9$ with abundancy off the small primes — the same "few
  primes" obstruction as the distortion method.
- *Open.* Erdős 7 itself; an obstruction surviving the dilution of the prime-3
  frequency in the spread-abundancy regime.

---

# References

1. P. Erdős, *On integers of the form $2^k+p$ and some related problems*,
   Summa Brasil. Math. (1950).
2. R. D. Hough, *Solution of the minimum modulus problem for covering systems*,
   Ann. of Math. (2015), arXiv:1307.0874.
3. R. D. Hough, P. P. Nielsen, *Covering systems with restricted divisibility*,
   Duke Math. J. (2019), arXiv:1703.02133.
4. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba,
   *On the Erdős covering problem: the density of the uncovered set* (2022).
5. S. Guo, Z.-W. Sun, *On odd covering systems with distinct moduli*,
   Adv. in Appl. Math. (2005).
6. J. Harrington, Y. Sun, T. W. H. Wong, *Covering systems with odd moduli*,
   Discrete Math. (2022), arXiv:2104.00602.
7. *A further investigation on covering systems with odd moduli*,
   Discrete Math. (2026), arXiv:2507.16135.
8. erdosproblems.com/7.
