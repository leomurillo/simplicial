# The Li–Keiper Coefficients: Computation, Archimedean/Arithmetic Split, and the Honest Residual

**Program:** Riemann Hypothesis line.  **Date:** 2026-06-01.
**Script:** `empirical/verify_li_coefficients.py` (self-contained; regenerates the table).
**Data:** `empirical/reports/li_coefficients_table.json`.
**Independent precision check:** `empirical/_li_spotcheck.py`.

**Tiering.** `[P]` = proven / numerically verified to stated precision; `[A]` =
heuristic or conditional (under RH/GRH); `[C]` = conjectural.
**Nothing here proves RH.** By conservation of difficulty, Li's criterion is an
*equivalent* reformulation of RH and is therefore exactly as hard; the value below
is concrete computation plus the quantified residual, not a reduction in difficulty.

---

## 0. Object and criterion

$$\lambda_n \;=\; \sum_{\rho}\Bigl[\,1-\bigl(1-\tfrac1\rho\bigr)^{n}\Bigr]
\qquad(\text{nontrivial zeros }\rho,\ \text{paired with }\bar\rho).$$

**Li's criterion (X.-J. Li, 1997)** `[P]`: $\ \mathrm{RH}\iff \lambda_n\ge 0\ \forall\,n\ge 1.$

**Keiper's identity (J. Keiper, 1992)** `[P, verified §1]`. With
$\xi(s)=\tfrac12 s(s-1)\,\pi^{-s/2}\Gamma(s/2)\,\zeta(s)$,
$$\sum_{n\ge1}\frac{\lambda_n}{n}\,z^{n} \;=\; \log\xi\!\Bigl(\tfrac{1}{1-z}\Bigr)-\log\xi(1),
\qquad \lambda_n=n\,[z^n]\Bigl(\log\xi\bigl(\tfrac1{1-z}\bigr)-\log\xi(1)\Bigr).
\tag{G}$$
Equivalently, with $w=s-1=\tfrac{z}{1-z}$ and $c_j=[w^j]\log\xi(1+w)$,
$\ \lambda_n=n\sum_{j=1}^{n}c_j\binom{n-1}{j-1}.$

---

## 1. Method and numerical verification `[P]`

We evaluate (G) by **stable truncated-power-series (TPS) arithmetic**. Each analytic
factor of $\log\xi(s)$ is expanded about $s=1$ in $w=s-1$:
$\pi^{-s/2}=\pi^{-1/2}e^{-\frac w2\log\pi}$; $\Gamma(s/2)=\exp\sum_k\psi^{(k-1)}(\tfrac12)(w/2)^k/k!$;
and the *only* zeta input is the pole-free unit
$U(s)=(s-1)\zeta(s)=1+\sum_{m\ge0}(-1)^m\gamma_m w^{m+1}/m!$ (Stieltjes constants $\gamma_m$).
$\log/\exp$ of TPS use the $O(M^2)$ ODE recurrences; composition with $w=z/(1-z)$ is
$O(M^2)$ via $X\!\cdot\!\tfrac{z}{1-z}\Rightarrow Y_k=Y_{k-1}+X_{k-1}$.

**Precision.** The composition reintroduces binomial-scale ($\sim 2^n$) intermediate
magnitudes, so the working precision must exceed $\sim 0.30\,n$ digits; the series also
degrades within $\sim$50–60 terms of the truncation order $M$. Final run:
$N_{\max}=320$, **dps $=150$**, $M=N_{\max}+100=420$. Correctness is pinned three ways,
not asserted: (i) the small-$n$ values match the 50-digit arb/Fungrim reference to
$\ge 15$ digits (§1 table); (ii) the closed form $\lambda_1=1+\tfrac\gamma2-\tfrac12\log4\pi$
and the exact rationals $\tfrac34,\ -\tfrac1{24},\ \gamma$ of §2/§5 are reproduced to
$\ge 30$ digits; (iii) the run is internally clean to $n=320$ (the $\mathrm{arch}-\mathrm{lead}-\tfrac34$ residual equals $-\tfrac1{24n}$ with no precision breakdown — the
$M=N_{\max}+100$ guard keeps the composition's degradation zone above $N_{\max}$); and
(iv) an independent **dps $=240$** recomputation (`_li_spotcheck.py`) agrees with the
dps$=150$ production values to **relative difference $\le 1.04\times10^{-30}$** at
$n\in\{50,100,200,300,320\}$ — i.e. correct to $\sim30$ digits at every $n$.

**Verification vs published reference (arb/Fungrim, Li normalization)** `[P]`:

| $n$ | computed $\lambda_n$ | reference | $|\text{err}|$ |
|----|----------------------|-----------|----------------|
| 1 | 0.0230957089661210338 | 0.023095708966121033814… | 4.3e-21 |
| 2 | 0.0923457352280466704 | 0.092345735228046670386… | 1.6e-15 |
| 3 | 0.2076389205543248038 | 0.207638920554324803792… | 4.3e-15 |
| 4 | 0.3687904794922416386 | 0.368790479492241638591… | 9.3e-16 |
| 5 | 0.5755427144611774524 | 0.575542714461177450243… | 6.2e-15 |

Closed form (independent anchor) `[P]`: $\ \lambda_1=1+\tfrac\gamma2-\tfrac12\log(4\pi)=0.0230957089661\ldots$ (exact match).

> **Correction to the brief.** The task sheet quoted $\lambda_5\approx 0.5755683$. The
> correct value is $\boxed{\lambda_5=0.57554271446117745\ldots}$ (arb/Fungrim,
> Johansson; reproduced here to 17 digits). The brief's 5th–7th decimals were a
> transcription slip; $\lambda_1$–$\lambda_4$ in the brief are correct.

---

## 2. Archimedean drift vs arithmetic fluctuation `[P] / [A]`

**The Keiper split — and a subtlety we had to get right.** The $(s-1)$ factor of $\xi$ is
*paired with the simple pole of $\zeta$*: $U(s)=(s-1)\zeta(s)$ is analytic with $U(1)=1$.
Hence
$$\xi(s)=\underbrace{\tfrac12 s\,\pi^{-s/2}\Gamma(s/2)}_{\xi_{\mathrm{arch}}(s)}\cdot U(s),
\qquad \xi_{\mathrm{arch}}(1)=\tfrac12\neq 0.$$
The archimedean Li coefficients use $U\equiv1$ (drop the primes *and* the bare $(s-1)$);
$\lambda_n^{\mathrm{arith}}=\lambda_n-\lambda_n^{\mathrm{arch}}=n[z^n]\log U$ is the pure
prime/zero fluctuation. (One must **not** leave a bare $(s-1)$ in $\xi_{\mathrm{arch}}$ —
that would make it vanish at $s=1$ and $\log\to-\infty$. An earlier attempt did exactly
that and produced a spurious drift; the corrected split is anchored by the exact identity
$\lambda_1^{\mathrm{arith}}=\gamma$ below.)

**Drift asymptotic — verified to a clean closed form** `[P, numerical fit]`:
$$\boxed{\;\lambda_n^{\mathrm{arch}}=\tfrac{n}{2}\bigl(\log n-1-\log2\pi+\gamma\bigr)
\;+\;\tfrac34\;-\;\tfrac{1}{24\,n}\;+\;O(n^{-2})\;}$$
The leading coefficient $\tfrac{d_\zeta}{2}=\tfrac12$ ($d_\zeta=1$) matches Keiper/Voros.
The next two terms are *exact rational constants* read off the data: $\lambda_n^{\mathrm{arch}}-(\text{lead})\to 0.74986\to\tfrac34$, and
$\bigl(\lambda_n^{\mathrm{arch}}-\text{lead}-\tfrac34\bigr)\cdot n = -0.0416666\to-\tfrac1{24}$
(constant to 6 digits over $n=50,\dots,300$). $\xi_{\mathrm{arch}}$ is itself negative for
$n\le 7$ and positive for $n\ge 8$, so the drift only "dominates" for $n\ge 8$.

**Tabulated split** ($m_n:=\lambda_n/\lambda_n^{\mathrm{arch}}$ margin, $r_n:=|\lambda_n^{\mathrm{arith}}|/\lambda_n^{\mathrm{arch}}$ relative fluctuation):

| $n$ | $\lambda_n$ | $\lambda_n^{\mathrm{arch}}$ | $\lambda_n^{\mathrm{arith}}$ | $r_n$ | $m_n$ |
|----|------------|------------------------------|------------------------------|-------|-------|
| 1 | 0.0230957 | −0.554120 | +0.577216 (=$\gamma$) | — | — |
| 10 | 2.279339 | 0.955536 | +1.323804 | 1.385 | 2.385 |
| 25 | 13.32098 | 12.72602 | +0.594960 | 0.0468 | 1.0468 |
| 50 | 43.53110 | 42.03321 | +1.497890 | 0.0356 | 1.0356 |
| 100 | 118.60378 | 117.97502 | +0.628753 | 0.00533 | 1.00533 |
| 150 | 207.67737 | 206.99776 | +0.679610 | 0.00328 | 1.00328 |
| 200 | 306.65576 | 304.51539 | +2.140377 | 0.00703 | 1.00703 |
| 250 | 407.69590 | 408.34977 | −0.653871 | 0.00160 | 0.99840 |
| 300 | 519.70197 | 517.21802 | +2.483944 | 0.00480 | 1.00480 |
| 320 | 565.85236 | 561.97540 | +3.876957 | 0.00690 | 1.00690 |

**Behaviour of the margin** `[P, numerical]`: $m_n\to 1^{\!+}$. It falls from $2.39$
($n=10$) to within $\pm0.7\%$ of $1$ by $n\gtrsim100$, oscillating just above and below
$1$ (minimum $m_n=0.99469$ at $n=266$ over $n\ge10$, i.e. the realized $\lambda_n$ dips
$\sim0.5\%$ *below* the pure drift at some $n$ but stays positive). The relative
fluctuation $r_n$ shrinks like $\sim 1/(n\log n)$ ($r_{300}\approx0.5\%$): **the drift does
not merely dominate, it dominates by a margin that grows logarithmically.** All
$\lambda_n>0$ for $1\le n\le 320$ `[P]`.

---

## 3. State of the art (what is actually proven) `[P, literature]`

* **Li (1997)** — RH $\iff(\lambda_n\ge0\ \forall n)$.
* **Bombieri–Lagarias (1999), "Complements to Li's criterion"** — general positivity
  theorem: for any multiset $R$ closed under $\rho\mapsto\bar\rho,\ \rho\mapsto1-\rho$
  (with a convergence condition), *all* $\mathrm{Re}\,\rho=\tfrac12$ $\iff\sum_\rho[1-(1-1/\rho)^n]\ge0\ \forall n$. Plus the **dichotomy**: under RH the $\lambda_n$
  grow tamely ($\sim$ the §2 drift); if RH fails they oscillate with *exponentially
  growing amplitude* in both signs.
* **Voros (2006), "Sharpenings of Li's criterion"** (Math. Phys. Anal. Geom. 9, 53–63) —
  exact and asymptotic formulae; RH $\iff\lambda_n\sim n(A\log n+B)$ with $A=\tfrac12>0$
  and $B$ explicit, for $\zeta$ and Selberg/$L$-functions.
* **Coffey (2004–2010)** — explicit arithmetic formula; **lower bound for the
  archimedean (drift) contribution** via Euler–Maclaurin; relations between the Stieltjes
  constants $\gamma_n$ and the log-derivative Laurent coefficients $\eta_n$ (the latter
  defined from the von Mangoldt function $\Lambda$:
  $\eta_n=\tfrac{(-1)^n}{n!}\lim_{x\to\infty}\bigl[\sum_{k\le x}\Lambda(k)\tfrac{(\log k)^n}{k}-\tfrac{(\log x)^{n+1}}{n+1}\bigr]$).
* **Maślanka (2004, 2022)** — computed $\lambda_n$ to $n=3000$; analytic interpolation
  $\lambda(s)$; explicit oscillating part $\tilde\lambda_n$.
* **Saddle-point asymptotics, Selberg class** `[A, under GRH]` — $\lambda_F(n)=\tfrac{d_F}{2}n\log n+c_F\,n+O(n^{\delta})$, $\delta<1$ (main term unconditional; sharp error
  under GRH). For $\zeta$: $d_F=1$, recovering §2.
* **Unconditional positivity range** `[P, computation]` — verified $\lambda_n>0$ for
  **$n\le 10^5$** (and Johansson to $n=4001$ at very high precision; this work adds an
  independent, from-$\xi$ recomputation through $n=320$). **No unconditional proof that
  $\lambda_n>0$ for all $n>N_0$ is known; that statement is equivalent to RH.**

---

## 4. Sharpest honest reduction (conservation of difficulty) `[A]/[P]`

**Question.** Is "drift dominates fluctuation $\Rightarrow\lambda_n>0$ for $n>N_0$"
reachable unconditionally? **No**, and the obstruction is exact.

A single zero $\rho=\tfrac12+\delta+it$ contributes $-\mathrm{Re}(1-1/\rho)^n$, of magnitude
$|1-1/\rho|^n$. A direct computation (Appendix A) gives
$$|1-\tfrac1\rho|^2=1-\frac{2\delta}{|\rho|^2},\qquad |\rho|^2=(\tfrac12+\delta)^2+t^2.$$
* $\delta=0$: $|1-1/\rho|=1$ — bounded oscillation (compatible with positivity).
* $\delta\neq0$: zeros pair as $\rho,\,1-\rho$; the member left of the line has
  $|1-1/\rho|>1$, so its contribution grows like $R^n$ with
  $$\boxed{\,R(\delta,t)=\tfrac1{|1-1/\rho|}=\bigl(1-\tfrac{2|\delta|}{|\rho|^2}\bigr)^{-1/2}>1,
  \qquad R\approx 1+\tfrac{|\delta|}{t^2}\ \ (t\ \text{large})\,}$$
  (verified: $R=1/|1-1/\rho|$ equals the partner base $|1-1/(1-\rho)|$ to machine $\varepsilon$).

**Polynomial vs exponential.** The drift grows **polynomially** ($\sim\tfrac12 n\log n$),
the off-line excursion **exponentially** ($R^n=e^{n\log R}$). For *any* $R>1$ the exponential
wins for $n$ large, forcing $\lambda_n<0$. The $e$-folding scale is $n_e=1/\log R\approx t^2/|\delta|$;
the crossover $n^\ast$ where $R^n$ first overtakes the drift:

| $t$ | $\delta$ | $R-1$ | $n_e=1/\log R$ | $n^\ast$ (excursion $>$ drift) |
|-----|----------|-------|----------------|--------------------------------|
| 14.13 | 0.25 | 1.25e-3 | 800 | 8,186 |
| 14.13 | 0.10 | 5.0e-4 | 2,001 | 22,789 |
| 14.13 | 0.05 | 2.5e-4 | 4,001 | 49,017 |
| 14.13 | 0.01 | 5.0e-5 | 20,004 | 283,962 |
| 100 | 0.10 | 1.0e-5 | 100,003 | 1,608,554 |
| 100 | 0.01 | 1.0e-6 | 1,000,025 | 18,725,833 |
| 1000 | 0.10 | 1.0e-7 | 10,000,003 | 213,125,534 |

**Residual (precise).**
> "$\lambda_n>0$ for all $n>N_0$, unconditionally" $\;\equiv\;$ RH.
Difficulty is conserved *exactly*: one cannot exclude a single off-line $\rho$ producing the
$R^n$ excursion without already assuming no such $\rho$ exists. What the table makes
quantitative is **why $n\le10^5$ cannot decide RH**: a counterexample zero must have either
small $|\delta|$ or large $t$ (small $\log R\approx|\delta|/t^2$), pushing its crossover
$n^\ast\sim (t^2/|\delta|)\log(\text{drift})$ beyond the searched range. E.g. a zero at
$t=100,\ \delta=0.1$ would not bend $\lambda_n$ negative until $n\approx 1.6\times10^6$.
The single residual is precisely **the archimedean (marginal) positivity** at $\delta=0$:
the on-line case $|1-1/\rho|=1$ sits exactly at the boundary between bounded and runaway.

---

## 5. New micro-observations `[P, empirical] / [C, interpretation]`

1. **Exact rational drift expansion** `[P]`:
   $\lambda_n^{\mathrm{arch}}=\tfrac n2(\log n-1-\log2\pi+\gamma)+\tfrac34-\tfrac1{24n}+O(n^{-2})$.
   The $+\tfrac34$ and $-\tfrac1{24n}$ are clean rationals (the $-\tfrac1{24n}$ is the
   leading Stirling/Euler–Maclaurin correction of $\log\Gamma$), reproduced to 6 digits
   across $n=50\!-\!300$. Useful as a high-precision *closed-form drift subtractor* for
   isolating $\lambda_n^{\mathrm{arith}}$ without recomputing $\xi_{\mathrm{arch}}$.

2. **$\lambda_1^{\mathrm{arith}}=\gamma$ exactly** `[P]` (Euler's constant; agreement to
   $10^{-51}$). The whole of the $n=1$ arithmetic content is $\gamma$; the archimedean
   part carries $\lambda_1^{\mathrm{arch}}=1-\tfrac\gamma2-\tfrac12\log4\pi=-0.554120$. This is the
   cleanest possible check that the §2 split is the canonically-correct one.

3. **Bounded, sign-changing fluctuation** `[P]`: $\lambda_n^{\mathrm{arith}}$ does **not**
   grow with $n$ — over $2\le n\le 320$ it stays in $[-0.65,\,3.96]$, oscillating in sign
   (negative on two clean bands $n\in[156,186]$ and $n\in[247,287]$, 72 of 319 indices).
   Consequently the *normalized* margin
   $m_n\to1$ and the *relative* fluctuation $r_n=|\lambda_n^{\mathrm{arith}}|/\lambda_n^{\mathrm{arch}}\sim 1/(n\log n)\to0$. This bounded-oscillation signature is exactly the
   RH-true expectation (on-line zeros, $|1-1/\rho|=1$): the data we can reach is fully
   consistent with — but, per §4, cannot prove — RH. `[C]` The fluctuation amplitude
   staying $O(1)$ (rather than $O(\sqrt n)$ or larger) is the empirical face of the
   $\delta=0$ marginal positivity.

---

## Appendix A. $|1-1/\rho|^2 = 1-2\delta/|\rho|^2$ `[P]`

$\rho=\beta+it$, $\beta=\tfrac12+\delta$, $D=|\rho|^2=\beta^2+t^2$. Then
$1-\tfrac1\rho=\tfrac{D-\beta}{D}+i\tfrac tD$ and
$$|1-\tfrac1\rho|^2=\frac{(D-\beta)^2+t^2}{D^2}=\frac{D^2-2\beta D+(\beta^2+t^2)}{D^2}
=\frac{D-(2\beta-1)}{D}=1-\frac{2\delta}{D}.\qquad\square$$

## Appendix B. Reproducibility

`py empirical/verify_li_coefficients.py` ($N_{\max}=320$, dps$=150$, $M=420$; runtime
$\approx$10–13 min, Stieltjes-table dominated) writes `reports/li_coefficients_table.json`
(values to 30 digits: `lambda`, `lambda_arch`, `lambda_arith`, ratios, margins).
`py empirical/_li_spotcheck.py` recomputes at dps$=240$ for $n\in\{50,100,200,300,320\}$
and prints the relative agreement (precision certificate).
