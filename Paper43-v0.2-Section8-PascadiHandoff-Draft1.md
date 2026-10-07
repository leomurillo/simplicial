# Paper 43 v0.2 — §8 rewritten: the bilinear handoff via Pascadi (2511.08445)

**Supersedes** Paper 43 v0.1 §§7–9 (the iterated-completion → *classical Vinogradov* bilinear handoff, whose closed-form θ₀ derivation is internally inconsistent — §7.2 gives θ₀<½, the proof sketch §9 gives θ₀≈1.05, both flagged in-text). This rewrite installs the correct Type-II input — **Pascadi's non-abelian bilinear Kloosterman bound** — through the standard Bombieri–Friedlander–Iwaniec / Polymath8 dispersion architecture, and reports the honest unconditional level and its $n$-range.

Rigor labels: **[P]** proved here / **[S]** standard, cited / **[X]** standard-but-unexecuted (the Polymath8 bookkeeping). Certificate: `empirical/probe_pascadi_primorial_level_nrange.py` (exact $n$-range crossover).

---

## 8.0 What is being fixed

Paper 43 v0.1 routed the Type-II sums through Lemma 8.1 (Iwaniec–Kowalski Thm 13.9 + Vinogradov bilinear). That input is a **minor-arc exponential-sum bound**, and it caps the level at $\theta=\tfrac12+\varepsilon$: the classical large-sieve / Vinogradov barrier is not crossed by completion alone. To exceed $\tfrac12$ one must use the **dispersion method** with a genuine **bilinear-Kloosterman** input — exactly what Pascadi supplies, and exactly the "different ingredient" Paper 43's own Non-goals (line 66) said was required.

## 8.1 The reduction to a completed Type-II bilinear Kloosterman form [S]

Fix a primorial $P_n$, modulus level $Q=X^\theta$. By the Heath–Brown identity (depth $K\le 5$) the primorial-BV sum
$$E_n(X;\theta)=\sum_{\substack{d\mid P_n\\ d\le X^\theta}}\max_{(a,d)=1}\max_{y\le X}\Big|\psi(y;d,a)-\tfrac{y}{\varphi(d)}\Big|$$
decomposes into $O((\log X)^{10})$ Type-I, Type-II, Type-III pieces [S, Heath–Brown 1982]. The binding constraint in the range $\theta<0.6$ is **Type-II** (balanced bilinear, $M\asymp N\asymp X^{1/2}$); Type-I and Type-III are admissible at these levels for smooth moduli [S, Polymath8 §§4–5] — see §8.6 for the caveat.

A Type-II piece is $\sum_{m\sim M}\sum_{n\sim N}\alpha_m\beta_n\,(\mathbf 1_{mn\equiv a\,(d)}-\tfrac1{\varphi(d)}\mathbf 1_{(mn,d)=1})$, $MN\asymp X$. Writing $mn\equiv a\,(d)\iff n\equiv a\bar m\,(d)$ and **completing both variables modulo $d$** (this is precisely Paper 43 §5's iterated-completion step, converting a primary sum of length $L$ to a dual of length $\asymp d/L$):
$$\sum_{m,n}\alpha_m\beta_n\,\mathbf 1_{n\equiv a\bar m(d)}=\frac1{d}\sum_{k,h\bmod d}\widehat\alpha(k)\,\widehat\beta(h)\,S(ak,\,h;\,d)\;+\;(\text{main}),$$
where $\widehat\alpha(k)=\sum_{m\sim M}\alpha_m e(km/d)$ is concentrated on $|k|\le H_M:=d/M$, similarly $|h|\le H_N:=d/N$, and $S$ is the Kloosterman sum. **The completed Type-II sum is exactly Pascadi's object** $\sum_{k,h}\widehat\alpha(k)\widehat\beta(h)\,S(ak,h;d)$.

## 8.2 Regime check: the completion lands in Pascadi's range [P]

Pascadi Thm 1.1/1.2 require bilinear lengths $\ll d^{1/2+o(1)}$. The *primary* Type-II variables ($M,N\asymp X^{1/2}$) **violate** this ($X^{1/2}\gg d^{1/2}=X^{\theta/2}$ for $\theta<1$) — which is why an un-completed handoff is unsound. After completion the relevant lengths are the **duals**:
$$H_M=d/M\asymp X^{\theta-1/2},\qquad H_N=d/N\asymp X^{\theta-1/2},\qquad d^{1/2}=X^{\theta/2}.$$
$$H_M,H_N\ll d^{1/2}\iff \theta-\tfrac12\le\tfrac\theta2\iff \theta\le 1.\quad\checkmark$$
So for every sub-EH level $\theta<1$ the completed form lies in Pascadi's regime. The completion is mandatory and sufficient; this resolves the regime obstruction. $\;\blacksquare$

## 8.3 The Pascadi handoff and the divisor-penalty absorption [P/S]

Apply Pascadi to the completed form with modulus $c=d\mid P_n$ (squarefree), $a$-twist a unit.

- **General bound** [S, Pascadi Thm 1.1]: $\sum_{k,h}\widehat\alpha\,\widehat\beta\,S(ak,h;d)\ll\|\widehat\alpha\|\,\|\widehat\beta\|\,d^{1-1/700+o(1)}$ (arbitrary coefficients), or $d^{1-1/276+o(1)}$ for one $1$-bounded factor — beyond the Pólya–Vinogradov range.
- **Factorizable / primorial bound** [S, Pascadi Thm 1.2 + Ex 1.3]: a squarefree $d$ has a divisor $d'\asymp\sqrt d$ with $d/d'$ squarefree (choose a sub-product of its primes); then $f=\max\{f:f^2\mid d\,d'\}=d'$ and the saving is
$$\Big(\tfrac{f}{\min(d,d'^2)}\Big)^{1/6}\Big|_{d'\asymp\sqrt d}=\big(d^{-1/2}\big)^{1/6}=d^{-1/12}.$$
So on **every primorial divisor** the completed Type-II form saves $d^{-1/12}$ over the trivial $d^{1+o(1)}$. **[P]** (the factorization existence + exponent computation are elementary; verified analytically).

- **Divisor-penalty absorption** [P]: the trivial (Weil-pointwise) bound carries $\tau(d)=2^{\omega(d)}=2^n$. For $d\mid P_n$, $\log d\asymp p_n\asymp n\log n$, so $2^n=\exp(n\log2)=d^{\,\log2/\log n+o(1)}=d^{o(1)}$. Pascadi's $d^{o(1)}$ **absorbs the $2^n$ divisor penalty**. This is decisive: it removes the explicit $2^{r}$ penalty that forced Paper 43's iteration to *saturate* at $r_0=5$ (where increasing $r$ made $\theta_0$ worse). The Pascadi handoff has no such saturation.

## 8.4 The level: $\kappa$ pinned (regime-dependent) [P in regime / X for uniformity]

*Certificate: `empirical/probe_pascadi_kappa_dispersion.py` (exact).* §8.3 gives the per-modulus bound
$$|\Delta_d|\ \le\ \tfrac1{d^2}\,\|\widehat\alpha\|\,\|\widehat\beta\|\,d^{1+o(1)}d^{-\eta_{\mathrm{eff}}}\ \ll\ \sqrt X\,d^{-\eta_{\mathrm{eff}}+o(1)},\qquad \|\widehat\alpha\|\asymp\sqrt d\,\|\alpha\|,$$
and **summing over $d\le Q=X^\theta$ by the triangle inequality** (no variance step needed — the cancellation is *within* each modulus, in the completed bilinear form):
$$\sum_{d\le Q}|\Delta_d|\ \ll\ \sqrt X\,Q^{1-\eta_{\mathrm{eff}}}\ \ll\ \frac{X}{(\log X)^A}\quad\iff\quad \theta\big(1-\eta_{\mathrm{eff}}\big)<\tfrac12\quad\iff\quad \theta<\frac1{2(1-\eta_{\mathrm{eff}})}.$$

**The effective saving $\eta_{\mathrm{eff}}$ — the hinge [P].** Pascadi's $d^{-1/12}$ requires a divisor $d'\asymp\sqrt d$. For $d\mid P_n$ the divisor lattice has multiplicative gaps up to the largest prime $p_n=X^\beta$, so the best balanced divisor sits at $d'\in[\sqrt d/p_n,\sqrt d]$ and the saving degrades:
$$\Big(\tfrac{f}{\min(d,d'^2)}\Big)^{1/6}\Big|_{d'\asymp\sqrt d/p_n}=p_n^{1/6}d^{-1/12}=d^{-\eta_{\mathrm{eff}}},\qquad \eta_{\mathrm{eff}}=\tfrac1{12}-\tfrac{\beta}{6\theta}.$$
Thus the dispersion efficiency $\kappa:=(\theta_0-\tfrac12)/\eta_0$ ($\eta_0=\tfrac1{12}$) is **not a universal constant — it is set by $\beta=\log p_n/\log X$**:

| regime | $\beta$ | $\eta_{\mathrm{eff}}$ | $\theta_{\mathrm{ach}}=\tfrac1{2(1-\eta_{\mathrm{eff}})}$ | $\kappa$ |
|---|---|---|---|---|
| favorable (minimal $n$, $p_n=X^{o(1)}$) | $0$ | $1/12$ | $6/11\approx0.5455$ | $6/11\approx0.545$ |
| **$n=6$ threshold** | $\theta/8=1/15$ | $1/16$ | $8/15\approx0.5333$ | $0.40$ |
| Paper 43 constraint $p_n\le X^{\theta/5}$ | $\theta/5$ | $\approx0.050$ | $\approx0.526$ | $\approx0.31$ |

**Result [P, favorable regime].** In the favorable regime $\beta\to0$, $\boxed{\theta_0^{\mathrm{II}}<6/11\approx0.5455,\ \ \kappa=6/11}$ for the **Type-II** contribution. This *pins* the $\kappa$ left open above: the per-modulus completed-Pascadi route is genuinely beyond-BV, with efficiency $6/11$, on a correct architecture. **Against the EXACT V/M requirement (§8.7; $\theta_0(5)=0.545$, $\theta_0(6)=\tfrac35=0.600$ — not the asymptotic $8/15$ used in the tables above), $6/11$ clears $n\le5$ (tight) but is itself below $\theta_0(6)=\tfrac35$, so it does NOT reach $n=6$.** (The intermediate $\kappa$-tables above correctly compute the efficiency *at* level $6/11$; only their comparison to the asymptotic $\theta_0(6)=8/15$ is superseded.)

## 8.5 The honest $n$-range [P, exact]

The obligation needs $\theta_0(p_n)\ge1-C^*/n$, $C^*=2.80=\tfrac{14}5$ (*ocho* §7 V/M crossover). Required gain $g_{\mathrm{req}}(n)=\theta_0(n)-\tfrac12=\tfrac12-\tfrac{C^*}{n}$. Crossover $g_{\mathrm{req}}(n)\le\eta=\tfrac1{12}$:
$$\tfrac12-\tfrac{14}{5n}\le\tfrac1{12}\iff n\le\tfrac{C^*}{\,1/2-1/12\,}=\tfrac{168}{25}=6.72.$$

| $n$ | $\theta_0(n)$ | $g_{\mathrm{req}}$ | needs $\kappa\ge$ | status |
|----:|:----:|:----:|:----:|:---|
| $\le 5$ | $\le 11/25=0.44$ | $\le 0$ | — | **classical BV** (no Kloosterman) |
| $6$ | $8/15=0.533$ | $1/30$ | $0.40$ | **Pascadi-reachable** (if $\kappa\ge\tfrac25$) |
| $7$ | $3/5=0.60$ | $1/10$ | $1.20$ | **out** ($g_{\mathrm{req}}>\eta$, even at $\kappa=1$) |
| $\ge 8$ | $\ge 0.65$ | $\ge 3/20$ | $\ge1.8$ | out |
| $\to\infty$ | $\to 1$ | $\to\tfrac12$ | $\to 6$ | EH-tail, open |

**Result (corrected against the exact schedule, §8.7).** Pascadi's completed Type-II handoff, at the pinned level $6/11$, secures the primorial-BV obligation up to **$n\le5$** (razor-tight at $n=5$, $6/11>\theta_0(5)=0.545$), on a *correct* architecture, with Paper 43's flawed derivation and $r_0=5$ saturation removed. The asymptotic $\theta_0$ used in the tables above had suggested $n=6$; the **exact** $\theta_0(6)=\tfrac35=0.600$ is above the $6/11$ Type-II ceiling, so $n=6$ is *not* reached. Classical BV reaches $n\le3$.

## 8.6 What remains [X / open]

1. **[P, done in §8.4] The efficiency $\kappa$ is pinned: $\kappa=6/11\approx0.545$ in the favorable regime**, clearing the $2/5$ threshold for $n=6$. What remains is **not** $\kappa$ but the **coupling condition** $\beta\le\theta/8$, i.e. the binding moduli have largest prime $p_n\le X^{\theta/8}\approx X^{0.067}$. Whether the bridge's $n$–$X$ coupling (ocho §7: frequency scale $\log P_n$ matched to $X$) keeps the relevant moduli this smooth is a **bridge question, not a Pascadi question** — and Paper 43's looser $p_n\le X^{\theta/5}$ does *not* by itself guarantee it (worst case $\theta_{\mathrm{ach}}\approx0.526<0.533$). **Sub-task [X]:** verify the bridge only needs primorial moduli with $p_n\le X^{\theta/8}$ (very plausible: in the natural minimal-$n$ coupling $p_n\approx\log Q=X^{o(1)}$, deep inside the condition).
2. **[X] Type-III — now the binding constraint (§8.7).** See §8.7: Type-III binds *below* $\theta_0(6)$ on general moduli; $n=6$ needs the smooth-moduli Type-III gain in addition to Pascadi.
3. **[open] The EH-tail.** The obligation needs $\theta_0(p_n)\to1$ ($n\to\infty$): Elliott–Halberstam strength on smooth primorial moduli. Pascadi's saving is bounded ($\eta=1/12$), and even at $\beta=0$ the Type-II ceiling is $6/11<\theta_0(7)=0.60$, so $n\ge7$ is untouched. No current technology reaches $\theta\to1$ on smooth moduli; this is the real residual (Paper 43's own guess: averaged short-interval, Matomäki–Radziwiłł direction, combined with the Kloosterman input).

## 8.7 Type-III: the second, non-Pascadi gain that $n=6$ also needs [P, exact thresholds]

*Certificate: `empirical/probe_pascadi_typeIII_constraint.py` (exact).* The Heath–Brown identity at $K=5$ (§8.1) produces **Type-III** pieces — ternary convolutions, three factors $\asymp X^{1/3}$ — alongside Type-I/II. **diez §3.3 addressed only Type-I and Type-II; Type-III is an unaddressed gap.** Crucially, **Type-III is independent of Pascadi**: it is the ternary-divisor ($d_3$) sum, bounded via Deligne's RH for the relevant sheaf / hyper-Kloosterman $\mathrm{Kl}_3$, *not* the bilinear Kloosterman bound. The achievable level is $\theta=\min$ over the types:

| type | admissible $\theta$ (primorial regime) | tool |
|---|---|---|
| Type-I | $\gg0.55$ (easy for smooth moduli) | completion + Weil |
| Type-II | $6/11\approx0.5455$ | **Pascadi** (§8.4) |
| Type-III, general, fixed $a$ | $\tfrac12+\tfrac1{82}\approx0.512$ | Heath–Brown 1986 ($d_3$) |
| Type-III, **smooth** sqfree, fixed $a$ | $\tfrac12+\tfrac1{34}\approx0.5294$ | **Ping Xi 2018** ($q$-vdC + FKM trace fns) |
| Type-III, general, **averaged over $a$** | $2/3\approx0.667$ | Nguyen (8/11 for prime $q$, 2026) |
| **$n=5$ target (EXACT)** | $\theta_0(5)=0.5453$ | discharged by $6/11$ (tight) |
| **$n=6$ target (EXACT)** | $\theta_0(6)=\tfrac35=0.600$ | out of reach (both levers $<\tfrac35$) |

**Finding (CORRECTED 2026-06-08 — the exact $\theta_0$ schedule; the $1/255$ figure retracted).** Two corrections compound. *First* (d₃ constants): general fixed-$a$ $d_3$ is $\tfrac12+\tfrac1{82}$ (Heath–Brown 1986), while $\tfrac12+\tfrac1{34}$ is *itself* the **smooth-moduli, fixed-$a$** record (Ping Xi 2018, Mathematika) — so the smoothness is already spent, no free gain. *Second and decisive* (the requirement): the discharge frontier must use the **exact** V/M requirement $\theta_0(n)=1-\log\mathrm{pure}_V(P_n)/\log P_n$ ($\mathrm{pure}_V(P_n)=\sum_{p\le p_n}(p^2-1)/6$, *ocho* §5), **not** the asymptotic $1-C^\ast/n$ ($C^\ast\approx2.80$), which understates it by one to two rows at small $n$ (certified `empirical/probe_exact_discharge_schedule.py`). The exact schedule is $\theta_0(5)=0.5453$, $\theta_0(6)=\tfrac35=0.600$, $\theta_0(7)=0.642$. Hence the bilinear Pascadi level $6/11\approx0.5455$ discharges **$n\le5$** (razor-tight), classical BV reaches $n\le3$, and $n=6$ needs $\tfrac35$ — above **both** levers ($6/11=0.545$ and the smooth $d_3$ $\tfrac12+\tfrac1{34}=0.529$). *So $n=6$ is out of reach by a real margin $\sim0.05$–$0.07$, and the earlier "$1/255$ Type-III residual" — which used the asymptotic $\theta_0(6)=\tfrac8{15}$ — is **retracted**;* with the exact $\tfrac35$ the shortfall is at the Type-II level itself.

**Corrected status of $n=6$ (2026-06-08).** $n=6$ is *not* discharged by the max-over-$a$ Pascadi handoff (its Type-II ceiling $6/11<\theta_0(6)=\tfrac35$); the bridge-coupling check (§8.6) is verified but moot. The constructive route is the **variance reformulation** (N0 §§6.6–6.9, Lemma 6.8): the cubic transfer error is a *second moment*, so the genuine medium arc is the variance, Type-III becomes non-binding (Nguyen's averaged-$a$ $d_3=2/3$), and the terminus remaps to **sparse-primorial BDH** — under which $n=6$, like every $n$, reduces to that ($L^2$-density, open) target. **Net of the v0.2 handoff:** its unconditional contribution is the pinned Type-II level $6/11$, discharging $n\le5$; $n=6$ and the large-$n$ tail are the variance / sparse-primorial-BDH frontier.

**Logical-independence caveat (N15 §8).** By Gallagher–Mueller the level-of-distribution prong is logically independent of RH: lifting $\theta_0$ advances the *cubic-positivity bridge* [A3] (a program-internal reduction step) and the $\tau=1$ reading, but "moving the level" is not itself "crossing toward RH." This is a real, citable analytic advance on [A3]'s bounded-$n$ rows — not a step that converts to RH without the independent bridge content.

**Net advance over Paper 43 v0.1 / classical BV.** A correct (completion → Pascadi) architecture; the $2^n$ divisor penalty absorbed (no $r_0$ saturation); the Type-II efficiency *pinned* at $\kappa=6/11$. Against the **exact** V/M schedule (§8.7) this discharges **$n\le5$** (classical BV reaching only $n\le3$); $n=6$ needs $\theta_0(6)=\tfrac35$, above both the bilinear ($6/11$) and smooth-$d_3$ ($\tfrac12+\tfrac1{34}$) levers — out of reach (the earlier "$1/255$ residual / $+1$ row to $n=6$", from the asymptotic $\theta_0(6)=\tfrac8{15}$, is retracted). $n=6$ and the EH-tail are the variance / sparse-primorial-BDH frontier (N0 §§6.6–6.9).

---

**Anchors.** Pascadi 2511.08445 (Thm 1.1, 1.2, 7.1; Ex 1.3); BFI 1986 (dispersion); Polymath8 (Type I/II/III for smooth moduli); Heath–Brown 1982 (identity); Heath–Brown 1986 ($d_3$ in APs, $\theta=\tfrac12+\tfrac1{34}$); Fouvry–Kowalski–Michel ($d_3$ to smooth moduli, algebraic trace functions); Paper 43 v0.1 (§5 completion, §8 the slot, §9 the flagged derivation); *ocho* §7 (V/M crossover, $C^*=2.80$); *diez* Thm 3.3 / Cor 3.4; assessment `Pascadi2511-PrimorialBV-Assessment-Draft1.md`.
