# Matomäki–Radziwiłł as the EH-Tail Ingredient — Assessment

**Scope.** Paper 43's Non-goals (line 66) names the missing ingredient for the EH-tail — pushing the primorial level $\theta_0(p_n)\to1$ as $n\to\infty$ — as "*averaged short-interval technology in the Matomäki–Radziwiłł direction*." This scopes that guess against the actual obligation. **Verdict: half-right.** MR is genuinely relevant technology, but for the program's *short-interval / $\tau=1$* face (N15 §7), **not** the level-of-distribution [A3] face; and on either reading it is **blocked by the Faltings–Hriljac guillotine** from closing the tail. It can furnish unconditional *partial* control (bounded-$n$, on-average, Möbius-sector), never $\theta\to1$.

---

## 1. The EH-tail, precisely

[A3]'s residual (after N1/N1b/N1c): a level of distribution $\theta_0(p_n)\to1$ as $n\to\infty$, on smooth squarefree primorial moduli (level relative to $X$). This is **Elliott–Halberstam strength on smooth moduli** — open for *all* current technology; the records (BFI, Zhang, Polymath8, Pascadi $\approx6/11$) cap at $\theta\approx0.52\text{–}0.55$.

## 2. What Matomäki–Radziwiłł actually is

**MR (Annals 183 (2016), 1015–1056).** For a *bounded* multiplicative $f:\mathbb N\to[-1,1]$,
$$\frac1H\!\!\sum_{x<n\le x+H}\!\!f(n)\ =\ \frac1X\sum_{n\le X}f(n)\ +\ o(1)\quad\text{for almost all }x\le X,$$
for **any** $H=H(X)\to\infty$ (with $H/X\to0$). It broke the $x^{1/6}$ short-interval barrier *on average*. Mechanism: reduce to Dirichlet-polynomial mean values via the Ramaré/parabola identity (almost every $n$ has a prime factor in a chosen range) — a **multiplicativity-exploiting, $L^2$/almost-all** method. Extensions (MRT: Chowla-on-average, sign patterns, Fourier uniformity; function fields) all share two features: **(a) bounded multiplicative inputs, (b) on-average / almost-all (not pointwise) conclusions.**

## 3. Reading A — "MR $\Rightarrow$ level of distribution $\theta_0\to1$": **No (wrong axis).**

MR controls **short intervals** $[x,x+H]$; [A3] needs **large moduli** $q\le X^\theta$. These are *different axes* (short-interval length $H$ vs AP modulus $q$), dual only loosely via the explicit formula. MR has **never** produced a level-of-distribution improvement: every beyond-$\tfrac12$ level result comes from **dispersion + Kloosterman** (a disjoint toolset), not MR. And $\theta\to1$ on *any* natural moduli family is open regardless of MR (it is EH). So as a literal level-of-distribution tool, MR is **misidentified** — it does not push $\theta$, and cannot reach the tail. Paper 43's guess, read this way, is wrong.

## 4. Reading B — "MR $\Rightarrow$ control the cubic-tensor convergence directly": the right home, three obstacles.

The charitable reading bypasses the level formulation. By *ocho* §6 the cubic-tensor convergence is governed by the **second moment of $\zeta$ at frequency scale $T\sim\log P_n$**, and (N15 §7, Goldston–Montgomery / $\tau=1$) by the **variance of arithmetic functions in short intervals** of relative length $\sim1/T$. As $n\to\infty$, $T\to\infty$ — *shrinking-relative-length short intervals*, which **is** MR's home. So MR is structurally the right technology for the program's **short-interval / $\tau=1$ face**, and the M-sector error (the convergence defect) is plausibly a multiplicative short-interval variance MR-type bounds address. Three obstacles, in increasing severity:

1. **Multiplicativity fork [technical].** MR needs *bounded* multiplicative inputs. If the M-sector is a **Möbius** sum ($\mu$, the Hayes–Möbius currents of *ocho* §5 — bounded multiplicative ✓), MR applies directly. If it is a **von Mangoldt** ($\Lambda$, unbounded, not multiplicative), MR needs the harder $\Lambda$-adaptations (weaker, partial). *Which one the M-sector is decides whether MR even engages.*
2. **Variance, not pointwise [structural].** MR is $L^2$/almost-all (over $x$, or over the frequency $T$). It controls the convergence **on average**, never pointwise (every $s$ on the line / every zero). Viable only if the bridge tolerates on-average closure — *ocho* §7's requirement must be checked; the contrapositive in *diez* §4.1 (a single off-line zero at distance $\delta$) looks **pointwise**, which MR cannot deliver.
3. **The Faltings–Hriljac guillotine [decisive].** MR is **unconditional**. [A3] closing gives (with constructive cubic positivity, A1) cubic positivity $\Rightarrow$ RH, i.e. **[A3] is RH-hard**. By the program's standing principle — *an unconditional tool cannot supply the RH-content of an RH-equivalent step* (the same guillotine that sank Faltings–Hriljac, Tomita–Takesaki, and capped Pascadi at bounded $n$) — **MR cannot close the tail.** It can at most furnish the *unconditional, partial* part (bounded-$n$ rows; the Möbius-sector variance on-average), exactly as Pascadi furnishes the Type-II gain for bounded $n$.

## 5. The unifying verdict (why every unconditional lever caps here)

Pascadi (Kloosterman/level), Tomita–Takesaki (modular), Faltings–Hriljac (Arakelov), and now MR (short-interval) are all **unconditional**, and all hit the same wall: they restructure and discharge the *partial / bounded / on-average* regime, but the **RH-content concentrates in a limit they cannot cross** — for [A3] that limit is $\theta\to1$ ($n\to\infty$), the EH-tail. MR is special only in that it is the *correct unconditional technology at the $\tau=1$ short-interval-variance wall* that the program's GUE/cumulant arc independently localized (project: GUE→cumulant, $\tau=1$ the single wall point). MR approaches $\tau=1$ from the unconditional side; it does not pass it.

## 6. Net and recommendation

- **Paper 43's "MR direction" guess is half-right:** right *technology*, wrong *target*. MR does not move the BV level (Reading A fails); it belongs to the program's **short-interval / $\tau=1$ / Goldston–Montgomery face (N15 §7)**, where it is genuinely the state-of-the-art unconditional tool (Reading B).
- **It does not close the EH-tail.** FH-guillotine + the variance-vs-pointwise obstacle + the $\Lambda$-multiplicativity fork. The tail's genuine new ingredient remains **absent** — MR is not it.
- **The one real forward door it opens (bounded, unconditional):** recast the **Möbius** M-sector of *ocho* §5–§7 as a bounded-multiplicative short-interval variance and apply MR(-Tao) to get unconditional *on-average* control of the cubic-tensor defect at bounded $n$ — a companion to Pascadi's bounded-$n$ Type-II gain, on the $\tau=1$ side. This banks partial rows / an averaged statement; it is **not** a route to $\theta\to1$.
- **Recommendation:** do not budget MR to close [A3]. If pursued, pursue it as the **N15 §7 / $\tau=1$** connection (Möbius short-interval variance), explicitly bounded-$n$/on-average, with the pointwise gap and FH-guillotine flagged. The high-value redirection for the *tail itself* is not an existing unconditional tool at all — by the guillotine, closing the tail needs the same RH-content every face points to (the CCM convergence / arch-domination), not a new analytic-NT lever.

---

**Anchors.** Matomäki–Radziwiłł, *Multiplicative functions in short intervals*, Ann. Math. 183 (2016); MRT (Chowla on average / Fourier uniformity). Program: Paper 43 Non-goals (line 66, the guess); *ocho* §5–§7 (Möbius M-sector, 2nd-moment-of-$\zeta$ convergence); N15 §7–§8 (Goldston–Montgomery $\tau=1$; Gallagher–Mueller logical independence); *diez* §4.1 (pointwise contrapositive); project GUE→cumulant ($\tau=1$ wall); `Pascadi2511-PrimorialBV-Assessment-Draft1.md`, `Paper43-v0.2-Section8-PascadiHandoff-Draft1.md` (the FH-guillotine pattern across unconditional levers).
