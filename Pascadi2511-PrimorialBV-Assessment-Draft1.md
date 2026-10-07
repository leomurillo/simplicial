# Pascadi (arXiv:2511.08445) as the Primorial-BV Lever — Assessment

**Scope.** Pascadi, *Non-abelian amplification and bilinear forms with Kloosterman sums* (2511.08445v1, 11 Nov 2025), assessed against the program's open analytic obligation **[A3]** — the primorial-indexed Bombieri–Vinogradov bound that closes the discrete-to-continuous cubic-positivity bridge (*ocho* §7, *diez* Thm 3.3 / Cor 3.4, Paper 43). Verdict tier: **reduces the bounded-$n$ regime; does not close the obligation.** Honest, calibrated.

---

## 1. The obligation [A3], stated precisely

From *diez* Thm 3.3 + *ocho* §7 (V/M crossover) + Paper 43 Thm 9.1, the bridge closes iff, **uniformly in the primorial level $n$**,
$$\sum_{\substack{d \mid P_n \\ d \le X^\theta}} \max_{(a,d)=1}\max_{y\le X}\Big|\psi(y;d,a)-\tfrac{y}{\varphi(d)}\Big| \;\ll_{A,\theta}\; \frac{X}{(\log X)^A},\qquad \theta<\theta_0(p_n),$$
with the required rate (V-sector dominates M-sector, *ocho* §7 (553)–(563))
$$1-\theta_0(p_n) \;<\; \frac{\log \mathrm{pure}_V(P_n)}{\log P_n} \;=\; \frac{O(\log n)}{p_n} \;=\; O(1/n)\quad\Longrightarrow\quad \theta_0(p_n)\ge 1-\frac{C^*}{n},\ \ C^*\approx 2.80.$$

**What this is.** The moduli $d$ are squarefree divisors of $P_n$ (smooth, products of the first $n$ primes); the level $\theta$ is **relative to $X$** (Paper 43 (19),(294): $d\le X^\theta$). As $n\to\infty$ the rate forces $\theta_0(p_n)\to 1$. So [A3] is an **Elliott–Halberstam-strength level of distribution ($\theta\to 1$) restricted to smooth squarefree primorial moduli.**

**Honest calibration of the "structural reduction."** *ocho* §7 (561) frames this as "*not* full Elliott–Halberstam ($\theta\to1$ over all moduli), only polynomial-in-$n$ decay on squarefree primorial moduli." That reduction is real and is the correct arena — every unconditional beyond-$\tfrac12$ result (BFI, Zhang, Polymath8) lives precisely in the smooth/well-factorable-moduli world. **But $\theta\to1$ even on smooth moduli is open**: the record on smooth/well-factorable moduli is $\theta\approx 0.52\text{–}0.58$, and no approach reaches $\theta\to1$. The crossover constant $C^*\le 2.80$ is a *rate* on a target that is itself unattained for large $n$. The "specialist verification of $C^*\le 2.80$" framing therefore **understates** the difficulty: the bounded-$n$ part is Polymath-8-difficulty; the $n\to\infty$ tail is EH-on-smooth-moduli, open.

---

## 2. Current program status (Paper 43) — a flagged gap

Paper 43 (Hybrid Primorial BV, $r_0=5$) claims $\theta_0(5)\approx 0.538$ ($+0.038$ over classical BV), via iterated completion + **classical Vinogradov bilinear** (Lemma 8.1, Iwaniec–Kowalski Thm 13.9). Two issues the draft itself records:

- **The derivation is not rigorous in v0.1.** The proof sketch (Paper 43 (305)–(308)) yields $\theta_0(5)\approx 1.05$ — *exceeding* EH — flagged in-text as "wrong, the argument must lose a factor"; the closed-form (§7.2 (271)–(273)) yields $\theta_0(5)<\tfrac12$; the value $0.538$ is **asserted** as "what careful accounting would restore," not derived. So the program's "$n\le 6$ discharged" rests on an acknowledged-incomplete draft.
- **The method provably saturates.** Paper 43 Non-goals (66): the hybrid strategy "saturates at $\theta_0(r_0)$; increasing $r_0$ past the optimum *decreases* $\theta_0$. Further improvements require a different ingredient." The classical Vinogradov bilinear input caps the level at $\tfrac12+\varepsilon$; it cannot reach the $n\ge 6$ regime ($\theta_0>\tfrac12$) on its own, let alone $\theta\to1$.

Paper 43 names the missing ingredient ("averaged short-interval, Matomäki–Radziwiłł direction"). **Pascadi supplies a different — and more directly applicable — one: beyond-Pólya–Vinogradov Kloosterman bilinear bounds.**

---

## 3. What Pascadi delivers (exact)

- **Thm 1.1 (general moduli).** $\sum_{m,n}\alpha_m\beta_n S(am,n;c)\ll \|\alpha\|\|\beta\|\,c^{1-1/700+o(1)}$ (arbitrary $\beta$), $\sqrt M\|\beta\|c^{1-1/276+o(1)}$ ($|\alpha_m|\le1$), for $M,N\ll c^{1/2+o(1)}$ — **all** moduli, beyond the Pólya–Vinogradov range. (Near-prime $c=pq$ handled via Cor 7.3 / Kowalski–Michel–Sawin.)
- **Thm 1.2 / Ex 1.3 (factorizable).** $c=dd'e$ with $d\asymp\sqrt c$, $c/d$ squarefree $\Rightarrow$ saving $c^{-1/12}$. Specifically stated for $c\in\{p^2,pq\}$ ($p\asymp q$), the exact configurations that are **blind spots** of the $q$-van der Corput method.
- **Thm 7.4 (the level knob).** $\delta\in[0,\tfrac1{24}]$ interpolating; this is what optimizes to Thm 1.1.
- **Thm 1.5 (application, unconditional).** Averaged 2nd moment of $L(\tfrac12,f\otimes\chi)$ over **all** primitive $\chi\bmod q$, **arbitrary $q$**, error $q^{1-1/674+o(1)}$.

**Primorial divisors are in the strong case.** For $c=d_S\mid P_n$ (squarefree), pick $d\asymp\sqrt c$ as a sub-product of its primes; then $c/d$ is squarefree and $f=\max\{f:f^2\mid cd\}=d$, so
$$\Big(\tfrac{f}{\min(c,d^2)}\Big)^{1/6}=\Big(\tfrac{d}{c}\Big)^{1/6}\Big|_{d\asymp\sqrt c}=c^{-1/12}.$$
So **Pascadi's $c^{-1/12}$ applies to every primorial divisor**, not just $p^2,pq$. (Confirmed analytically.)

---

## 4. The interface

Pascadi is the **Type-II input**: it replaces Paper 43 Lemma 8.1's classical Vinogradov bilinear bound (level cap $\tfrac12+\varepsilon$) with beyond-PV Kloosterman bilinear bounds. The conversion *bilinear saving $\to$ level of distribution* is the **dispersion method** (Bombieri–Friedlander–Iwaniec / Zhang / Polymath8), which is **not** in Pascadi and must be executed — Polymath-8-difficulty bookkeeping (Heath-Brown identity $\to$ Type I/II/III $\to$ dispersion $\to$ Kloosterman).

---

## 5. Verdict — quantified reduction

**Reduces (real):**
1. Pascadi removes the $p^2,pq$ blind spots $\Rightarrow$ the dispersion method now covers **every** primorial-divisor factorization configuration — the precise sense in which it is "the lever."
2. Redoing Paper 43 §8's bilinear handoff with Pascadi's Kloosterman input would **(a)** repair the flagged v0.1 derivation with a genuine bound and **(b)** push the unconditional level from the hoped-for $0.538$ toward $\approx 0.55\text{–}0.60$ (heuristic; the $c^{-1/12}$ saving is strong — $1/12\approx 0.083$, well above Polymath8's $\varpi$ — but the exact level needs the dispersion computation), discharging a few more primorial rows.
3. Thm 1.5 is an **unconditional, directly citable** input for any cubic-moment / GRH($\chi_3$) step that reduces to a twisted modular second moment over all $\chi\bmod q$.

**Does not close (the genuine residual):**
4. Pascadi's saving exponents ($1/700$ general, $1/12$ balanced) translate to a level **bounded away from $1$** ($\theta\lesssim 0.6$). The obligation needs $\theta_0(p_n)\to1$. Reaching $\theta\to1$ even on smooth moduli is **open for all current technology** (it is EH-on-smooth-moduli; would require essentially full square-root cancellation in the bilinear forms at length $\sqrt c$ with no dispersion loss — Linnik/Kloosterman-conjecture territory).
5. Net: the **bounded-$n$** regime (roughly up to where $\theta_0(n)\lesssim 0.6$, i.e. $n\lesssim 2C^*/(1-0.6)\sim$ single digits) is advanced and made rigorous; the **$n\to\infty$ tail** ($\theta_0\to1$) is untouched and is the real open problem.

**Reduction, stated as a scale (not "the wall"):** before — classical BV gives $\theta=\tfrac12$, i.e. only $n\le 2C^*\approx 5$, with the $n\ge6$ outline (Paper 43) non-rigorous and method-capped. After Pascadi — a rigorous Kloosterman handoff covers all divisor configurations and lifts the unconditional level to $\approx 0.6$, discharging a few more rows; the open problem shrinks to "$\theta\to1$ on smooth primorial moduli as $n\to\infty$," cleanly isolated as EH-strength.

---

## 5.1 Concrete level → primorial-row mapping (how far, exactly)

The rate $\theta_0(p_n)\ge 1-C^*/n$ ($C^*\approx2.80$) inverts to: an achievable unconditional level $\theta$ discharges every primorial row up to
$$n_{\max}(\theta)\;=\;\Big\lfloor \frac{C^*}{1-\theta}\Big\rfloor\qquad(C^*\approx2.80).$$

The exact n-range bookkeeping is the N1 handoff (`Paper43-v0.2-Section8-PascadiHandoff`, cert `empirical/probe_pascadi_primorial_level_nrange.py`): Pascadi's saving on primorial divisors is $\eta=1/12$, so the achievable level is $\theta=\tfrac12+\kappa\eta$ with $\kappa\in(0,1]$ the dispersion efficiency (the one open constant) — hence $\theta\le\tfrac12+\tfrac1{12}\approx0.583$, a hard ceiling.

| input | level $\theta$ | $n_{\max}$ | top modulus discharged | gain |
|---|---|---|---|---|
| classical Bombieri–Vinogradov | $0.500$ | $5$ | $P_5=2310$ | baseline |
| Polymath8 (well-factorable) | $0.523$ | $5$ | $P_5=2310$ | $0$ rows |
| **Pascadi handoff** | $\tfrac12+\tfrac\kappa{12}\le0.583$ | **$6$** (iff $\kappa\ge\tfrac25$) | $P_6=30030$ | **$+1$ row** |
| $n=7$ target | needs $\theta-\tfrac12>\tfrac1{12}$ | $7$ | $P_7=510510$ | **OUT** — beyond Pascadi's $\eta=1/12$ even at $\kappa=1$ |
| EH-on-smooth ($\theta\to1$) | $\to1$ | $\to\infty$ | all | closes the tail (OPEN) |

**Concrete reading.** The realized movement is **exactly $+1$ row**: from $n\le5$ (classical) to $n\le6$ (Pascadi), conditional on the dispersion efficiency $\kappa\ge2/5$ (a single well-posed constant, the residual [X] of the handoff). $n=7$ is **out** — Pascadi's $\eta=1/12$ caps $\theta$ at $\approx0.583$, and $n=7$ would need $\theta-\tfrac12>\tfrac1{12}$. The naive conversion $\theta=\tfrac12+2\cdot\tfrac1{12}=0.667$ **overstates** the level (it ignores the dispersion loss $\kappa<1$ and double-counts the saving). The program-relevant fact: **$n=6$ ($P_6=30030$, the primes-$\le13$ / Connes-reproduction modulus) crosses from "non-rigorous outline" (Paper 43 v0.1) to "rigorously dischargeable"** under the handoff — once $\kappa\ge2/5$ is certified — while the $n\ge7\to\infty$ tail is untouched.

**Two honesty checks on "how far."** (i) The realized $\theta$ is **heuristic until the dispersion handoff is done** (Polymath8-difficulty); the table's Pascadi row is a target, not a theorem. (ii) The level-of-distribution prong is, by Gallagher–Mueller, **logically independent of RH** (N15 §8): moving $\theta$ on primorial moduli advances the *cubic-positivity bridge* [A3] (program-internal reduction step) and the Montgomery/Goldston–Montgomery $\tau=1$ reading (N15 §7) as a *thematic* bridge — but "moving the level" is not, by itself, "crossing toward RH." Pascadi advances a real, citable analytic frontier; it does not convert into RH through this prong without the independent bridge content.

## 6. Concrete next actions

- **(N1, tractable, real).** Rewrite Paper 43 §8 (the bilinear handoff) using Pascadi Thm 1.1/1.2 in place of Lemma 8.1, threaded through the BFI/Polymath8 dispersion setup. Deliverable: a *rigorous* unconditional $\theta_0(p_n)$ on primorial moduli (replacing the flagged $0.538$), with the honest $n$-range it covers. This is the genuine lever-pull.
- **(N2, RESOLVED — Thm 1.5 does NOT match a current obligation; do not cite it as hoped).** Checked (2026-06-08) whether the program's cubic-moment / GRH($\chi_3$) obligations reduce to Pascadi Thm 1.5 (averaged 2nd moment of $L(\tfrac12,f\otimes\chi)$, $f$ a **GL(2)** cusp form, over primitive $\chi\bmod q$). **They do not.** The *power* matches — the cubic-positivity bridge reduces to a **second** moment, not the third moment $M_3$ (N0 Thm 5.1 / RH-Pass8: "the cubic Plancherel object is governed by the second moment of $\zeta$ on the critical line, $\int_T^{2T}|\zeta(\tfrac12+it)|^2\sim T\log T$"). But the *object* mismatches on two axes:
  1. **GL(1) vs GL(2).** The program's engine is "tied to GL(1) Dirichlet characters; the cubic constraint algebra at higher rank is an **open extension**" (GRH-Apex-Integration §3.3). Its second moments are $\zeta$ (metric channel, N7 Thm 4.1) and cubic **Dirichlet** $L$ (chiral channel, GL(1) — cf. the twisted 2nd moment of primitive *cubic Dirichlet* $L$-functions, arXiv:2506.14656). Pascadi Thm 1.5 is GL(2) ($f\otimes\chi$).
  2. **Critical-line integral vs family-averaged central value.** The program's anchors are $t$-integrals of a *fixed* $L$ on the critical line; Thm 1.5 is the central value at $\tfrac12$ averaged over the *family* $\chi\bmod q$.
  Moreover the program's GL(1) second moments ($\int|\zeta|^2$ Hardy–Littlewood 1918; $\int|\zeta|^4$ Ingham/Heath-Brown) are **classical and already unconditional** — they need no Pascadi. **Net: Thm 1.5 is Pascadi's showcase *application*, not the part the program needs.** It would become relevant only under the program's explicitly-open GL(2)/higher-rank extension. The citable Pascadi input remains **Thm 1.1/1.2** (bilinear Kloosterman $\to$ primorial-BV level), for the [A3] level-of-distribution obligation (§§3–5 above) — the genuine lever.
- **(N3, do not expect).** Do **not** budget Pascadi to close [A3]. The $\theta\to1$ tail needs a genuinely new ingredient; Paper 43's own guess (Matomäki–Radziwiłł averaged short-interval) plus Pascadi-type Kloosterman is the most plausible combination, but no current route reaches $\theta\to1$ on smooth moduli.

**External anchors.** Pascadi 2511.08445 (Thm 1.1, 1.2, 7.1, 7.4, 1.5; Ex 1.3); Milićević–Qin–Wu 2511.07550 (independent, complementary — better for general moduli, no Ramanujan dependence). Program: *ocho* §7, *diez* Thm 3.3/Cor 3.4, Paper 43 Thm 9.1, RH-DirectionB-Polymath-Roadmap (B-1).
