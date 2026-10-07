# The de Bruijn–Newman constant Λ: the upper bound mechanism, the lower bound mechanism, the 0.22→0 gap, and a Lehmer-pair flow computation

**Script:** `empirical/verify_debruijn_flow.py` (run log embedded verbatim at the end; raw copy in `reports/rh_debruijn_newman_runlog.txt`).
**Front:** the heat-flow deformation $H_t$ of the Riemann $\xi$ function; $H_t$ real-rooted $\iff t \ge \Lambda$; **RH $\iff \Lambda \le 0$**, and combined with the lower bound, **RH $\iff \Lambda = 0$**.
**Proven bracket [P]:** $\Lambda \ge 0$ (Rodgers–Tao 2020) and $\Lambda \le 0.22$ (Polymath15, 2019), so $\Lambda \in [0, 0.22]$.
**This report:** (1) the precise Polymath15 upper-bound mechanism ($f_t/g_t$ approximation + barrier + flow propagation, with the actual $X$, $t_0$); (2) the Rodgers–Tao lower-bound mechanism (backward-heat over-regularization vs. real-zero fluctuation); (3) an assessment of what controls the $0.22$ and whether $0.22\to 0$ is a genuine analytic step or RH restated; (4) a concrete computation — the Calogero/Rodgers–Tao zero flow run backward on the first 50 zeros, plus the exact two-body Lehmer collision clock and a truncated-$\xi$ heat-PDE cross-check; (5) tiers, a micro-observation, and the precise residual.
**Nature:** numerical/exact (mpmath dps=30, numpy), every claim tiered. **NOT a proof of $\Lambda \le 0$.** Conservation of difficulty is respected throughout: the flow by itself yields only the *lower* side; the upper side is RH.

---

## 0. Setup and conventions [P]

The de Bruijn–Newman family is
$$
H_t(z) \;=\; \int_0^\infty e^{t u^2}\,\Phi(u)\,\cos(z u)\,du,
\qquad
\Phi(u) \;=\; \sum_{n\ge 1}\bigl(2\pi^2 n^4 e^{9u} - 3\pi n^2 e^{5u}\bigr)\,e^{-\pi n^2 e^{4u}},
$$
where $\Phi$ is the (super-exponentially decaying, positive, even) Pólya kernel. At $t=0$, $H_0(z) = \tfrac18\,\Xi(z/2)$ up to a positive constant, where $\Xi$ is the Riemann xi function on the critical line; the real zeros $x_j$ of $H_0$ are (a rescaling of) the ordinates $\gamma_j$ of the nontrivial zeta zeros. The kernel $e^{tu^2}$ is **backward heat in the spatial variable $z$**: writing $u_t(z)=H_t(z)$, one has $\partial_t u_t = -\partial_z^2 u_t$ formally on the Fourier side, i.e. *increasing $t$ de-focuses (spreads) the zeros*.

**de Bruijn (1950) / Newman (1976):** there is a constant $\Lambda\in\mathbb R$ with
$$
H_t \text{ has only real zeros} \iff t \ge \Lambda.
$$
Newman conjectured $\Lambda \ge 0$ ("RH, if true, is only barely so"). RH is the statement that $H_0$ is real-rooted, i.e. $\Lambda \le 0$. With the lower bound below, **RH $\iff \Lambda = 0$.**

The **phase clock** reading the program uses: write $\phi_t(x) = -\arg H_t(x)$ along the real axis. For $t>\Lambda$ all zeros are real and simple, the zeros are exactly the points where $\phi_t$ increases through multiples of $\pi$, and $\phi_t'(x)\ge 0$ (monotone phase = no zero off the line). RH is "the flow reaches $t=0$ with $\phi'\ge 0$ intact." The binding failure mode as $t\downarrow\Lambda$ is a **Lehmer pair**: two real zeros approaching collision, becoming a real double root at $t=\Lambda$, then splitting into a complex-conjugate pair for $t<\Lambda$.

---

## 1. The Polymath15 upper bound $\Lambda \le 0.22$ — precise mechanism [P, cited]

Reference: D.H.J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, **Research in the Mathematical Sciences** 6 (2019), no. 3, paper 31. (Earlier, the same project obtained $\Lambda \le 0.48$ in the companion *"Lehmer pairs and the de Bruijn–Newman constant"* before optimizing to $0.22$.) The proof has **three interlocking pieces.**

### (a) The $f_t + g_t$ approximation (the analytic skeleton)

The engine is an **effective Riemann–Siegel-type expansion** of the heat-flowed function. Working with $H_t(x+iy)$ for $x$ large and $0 < y \le 1$ (the upper half of a thin strip; reality of zeros = "no zeros with $y>0$"), one writes
$$
H_t(x+iy) \;=\; B_t(x+iy)\,\bigl(f_t(x+iy) + g_t(x+iy)\bigr) \;+\; (\text{error}),
$$
where, schematically,
$$
f_t(s) \;=\; \sum_{n=1}^{N} \frac{e^{\,t\,(\text{log-quadratic in }n)}}{n^{\,s'}},
\qquad
g_t \;=\; \text{the functional-equation conjugate of } f_t,
$$
$s'$ a shifted/rescaled argument, $B_t$ an explicit non-vanishing gamma/exponential prefactor, and $N \asymp \sqrt{x/4\pi}$ the Riemann–Siegel truncation length. The crucial feature: the heat flow multiplies the $n$-th coefficient by $\exp\bigl(t\cdot\tfrac14\log^2 n + \cdots\bigr)$ — a **Gaussian mollifier in $\log n$** that *damps* the high terms, which is exactly what makes the $t>0$ series better-behaved (more dominated by its leading term) than the $t=0$ series. The error (terms called $e_A,e_B,e_C$ plus a tail in the paper) is bounded by **fully explicit, rigorously evaluable** expressions in $x,y,t,N$ — the bulk of the technical work, a mechanized "toolkit" of triangle-inequality / saddle-point bounds checked in interval arithmetic.

### (b) The barrier (the local certificate that zeros are real)

On a finite rectangle $R = [X, X+H]\times(\,\varepsilon, 1\,]$ in the $(x,y)$ upper strip, one proves
$$
|f_t(x+iy) + g_t(x+iy)| \;>\; |\text{error bound}(x,y,t)| \qquad \text{for all } (x,y)\in R,
$$
i.e. the leading two-term approximation **dominates the error** throughout the box. Because $f_t+g_t$ is itself explicit, one then certifies — via a winding-number / argument-principle count executed in rigorous interval arithmetic over a fine mesh of the box boundary — that $f_t+g_t$, hence $H_t$, has **no zeros with $y>0$ inside $R$**. This is the **barrier**: a wall in $(x,t)$-space across which a complex zero cannot pass.

### (c) Flow propagation (the dynamics that turn local into global)

The barrier and the explicit approximation are stitched together by the **zero dynamics** (§4):

1. Pick a seed time $t_0 > 0$ and a height $X$. Verify (via (a)+(b) and a Riemann–von Mangoldt zero count) that **all** zeros of $H_{t_0}$ with $0 \le x \le X$ are real, *and* that the barrier at the right edge $x\approx X$ holds for **all** $t$ in the range $0 < t \le t_0$.
2. The zeros of $H_t$ move continuously and obey the repulsive flow (FLOW). A new complex pair can be born **only** by two real zeros colliding (a real double root) *in the interior* $x<X$. The barrier at $x\approx X$ prevents zeros from crossing the right edge; the explicit lower bounds on $|H_t|$ off the real axis (a quantitative repulsion / non-degeneracy estimate) prevent an interior collision while $t$ stays in $(0,t_0]$.
3. Therefore reality at the seed $t_0$ **propagates downward** to all $t\in(0, t_0]$, so $H_t$ is real-rooted for every $t>0$ — giving $\Lambda \le 0$ in the idealized limit. With **finite, explicit** barrier strength and finite $X$, propagation is only guaranteed down to $t_0$ minus a provable margin, yielding the concrete numerical constant.

### The actual quantities [P, cited]

- The barrier rectangle was placed at height $X \approx 6\times 10^{10}$ — the regime to which the zeros of $\xi$ had been numerically certified real (the project leaned on Platt's verified zero database and on its own interval-arithmetic barrier computation). This mesh-and-winding certification at this $X$ is the heavy numerical lift.
- Optimization produced the final published constant $\boxed{\Lambda \le 0.22}$ (the intermediate, pre-optimization value was $0.48$).
- **Where the $0.22$ comes from:** it is essentially "$t_0$ minus the guaranteed downward-propagation margin." The dominant contribution is the **dynamics/propagation bound** — how far down in $t$ the flow can be *certified* to create no interior collision — **not** the numerical height $X$. (Quantified in §3.)

---

## 2. The Rodgers–Tao lower bound $\Lambda \ge 0$ — precise mechanism [P, cited]

Reference: B. Rodgers and T. Tao, *The de Bruijn–Newman constant is non-negative*, **Forum of Mathematics, Pi** 8 (2020), e6. This **closes Newman's conjecture** and, with §1, pins $\Lambda\in[0,0.22]$.

The mechanism is a contradiction argument driven by the **dynamics of the zeros and a comparison of actual vs. flowed gap statistics.**

**The dichotomy.** Suppose for contradiction $\Lambda < 0$. Then $H_t$ is real-rooted for all $t \ge \Lambda$, in particular on the whole interval $[\Lambda, 0]$ with $\Lambda<0$. View the zeros as an interacting log-gas under (FLOW). Two facts collide:

- **(Over-regularization from below.)** If the zeros are real and evolving by the repulsive flow already at the *negative* time $\Lambda$, then running **forward** from $\Lambda$ to $0$ is backward-heat smoothing over a *positive-length* time window *before* reaching $t=0$. Rodgers–Tao show this forces the $t=0$ ensemble to be **anomalously rigid / over-regularized**: its local statistics (gaps, pair correlations, the gas "energy") must be *closer to a rigid lattice* (the minimal-energy Calogero configuration) than a generic real configuration. Concretely, $\Lambda<0$ implies the zeros at $t=0$ have *too small* a local mean-square fluctuation / a pair correlation *too depleted at short range*.
- **(Actual fluctuation from below.)** But the **true** zeta zeros at $t=0$ fluctuate by a *definite* amount: the explicit formula plus known second-moment / pair-correlation information about $\{\gamma_n\}$ gives an **unconditional lower bound** on the local variance of the zero counting function (equivalently, the gas energy; equivalently, Montgomery-type pair correlation is *not* depleted below a certain level). This is a theorem about $\zeta$, not a conjecture.

The two are incompatible: the hypothesized over-regularization undercuts the proven fluctuation. Hence $\Lambda \ge 0$.

**The Lehmer-pair reading (mechanistic).** Equivalently and more vividly: a Lehmer-tight pair at $t=0$ — a pair far closer than the mean spacing, which provably **exists in the required averaged sense** (the zeros are *not* uniformly spread; close pairs occur with the right density) — **cannot** have arisen from a flow that was already real-rooted at some $t<0$. Under (FLOW) the squared separation of an isolated pair only *grows* going forward ($s(t)=s(0)+8t$, §4 PART B), so a pair that is tight at $t=0$ must have been *even tighter* (indeed collided) at some negative time — contradicting real-rootedness for all $t>\Lambda$ when $\Lambda<0$. The existence of sufficiently tight pairs pins the seed up against $0$ from below.

This is the **non-circular** half: settled, using only proven facts about $\zeta$, and giving the *opposite* inequality to RH.

---

## 3. Assessing the gap $0.22 \to 0$ — genuine analytic step, or RH restated? [A]

**Honest verdict: $\Lambda = 0$ is exactly RH, so closing $0.22\to 0$ in full is the hard problem restated. But the bound $0.22$ is *not* limited by how high the numerical verification reaches — it is limited by a dynamics constant — and that is the precise locus where a genuine analytic mechanism would have to act.** Both halves are true and not in tension; here is the quantitative anatomy.

### 3a. Why $0.22$ is dynamics-limited, not height-limited [A]

Inspect §1(c). Raising the barrier height $X$ certifies reality of **more** zeros at the fixed seed $t_0$ — it pushes the right wall further out. It does **not** shorten the time interval $(0, t_0]$ over which the flow must be controlled, and it does **not** strengthen the *interior* repulsion estimate that prevents a collision as $t$ descends. The final constant is, schematically,
$$
\Lambda \;\le\; t_0 \;-\; (\text{guaranteed downward-propagation margin}),
$$
where the margin is governed by a **uniform-in-height repulsion lower bound** (a "triangle of influence" / heat-kernel constant controlling how strongly nearby zeros push apart). That constant is an $O(1)$ analytic quantity that **does not improve by computing higher**. Consequence: even $X\to\infty$ leaves a **positive** residual $\Lambda \le c$ with $c\approx 0.22$, unless the *dynamics constant itself* is improved to give propagation all the way to $t=0$.

This is the sense in which the problem is **not** "just verify more zeros." If it were height-limited, more computation would drive $0.22\to 0$; it does not. The bottleneck is analytic.

### 3b. Why driving the dynamics constant to $0$ is RH [P/C]

To make the propagation margin reach $t=0$ one needs a **uniform-in-height** statement:
$$
\text{(FLOW) creates no complex pair for every } t\in(0,0.22] \text{ at every height } x,
$$
i.e. a guarantee that **no Lehmer pair ever actually collides** as $t\downarrow 0$. Equivalently in phase-clock language: $\phi_t'(x)\ge 0$ is *maintained uniformly* as $t\downarrow 0$. But "$H_0$ has no double-or-complex zero, at every height" **is** RH (it is $\Lambda\le 0$). So a full closure of the dynamics margin to $0$ is logically equivalent to RH — conservation of difficulty, exactly.

### 3c. The precise gap between proven and needed [A]

The two proven facts sit on opposite sides and **stop short of meeting**:

| | what it controls | what it gives |
|---|---|---|
| Rodgers–Tao (lower) | *averaged / statistical* fluctuation of zeros (pair correlation, gas energy) | $\Lambda \ge 0$ |
| Polymath15 (upper) | *individual* reality up to height $X$ + finite downward propagation | $\Lambda \le 0.22$ |

The missing ingredient is the **average $\to$ individual** upgrade of the repulsion: Rodgers–Tao show the zeros *on average* repel enough to forbid $\Lambda<0$; RH needs that **every** pair, at **every** height, repels enough to forbid a single collision at $t=0$. The statistical repulsion (GUE / Montgomery, $P(\text{gap}\to 0)\sim \text{gap}^2$) is *sufficient on average* but does not supply the *per-pair, per-height* guarantee. This is the same "soft statistical bound is the wrong instrument for an individual integrality" obstruction the program meets on the other faces (Born/Bures/CRT blindness; the Siegel average$\to$individual core). **No known mechanism converts the one into the other.**

**So:** the $0.22$ is a real analytic frontier (dynamics-limited, not a computation away), and the residual to $0$ is RH itself.

---

## 4. The computation: backward zero flow, the Lehmer collision clock, and a heat-PDE cross-check [P-num / P]

Script `verify_debruijn_flow.py`, mpmath dps=30 + numpy. Four parts; full output embedded below.

### PART A — the Calogero / Rodgers–Tao zero flow, run backward [P-num]

The zeros $x_j(t)$ of $H_t$ obey the first-order interacting ODE (Csordas–Smith–Varga 1994; the DBN backward-heat-in-$z$ convention)
$$
\frac{dx_j}{dt} \;=\; +2\sum_{k\ne j}\frac{1}{x_j - x_k}. \tag{FLOW}
$$
As $t$ **increases**, the zeros **repel** and stay real; as $t$ **decreases** toward $\Lambda$, they **attract** and a pair can collide. Seeding $x_j(0)=\gamma_j$ with the true first **50** ordinates and integrating **backward** (RK4, $dt=-0.002$):

- The **global tightest pair** is the **index-34 pair** ($\gamma_{34}\approx 111.0295$, $\gamma_{35}\approx 111.8747$), gap $0.84512$, normalized gap $0.3868$.
- Backward in $t$, that gap collapses **roughly linearly in $(-t)$** (the two-body law, PART B): gap $0.8451\,(t{=}0)\to 0.7572\,(t{=}{-}0.02)\to 0.5949\,(t{=}{-}0.05)$, then a near-collision (gap $<10^{-4}$) at $\boxed{t\approx -0.096}$.
- **Reading:** the margin is thinnest at the tightest pair; the collision time scales as $t_{\text{coll}}\approx -\text{gap}(0)^2/8$. The full 50-body collision ($-0.096$) sits *slightly later* than the isolated two-body prediction for this pair ($-0.089$, below) — the surrounding zeros supply extra repulsion that delays collision, exactly as the gas picture demands.

### PART B — the exact two-body Lehmer collision clock [P]

For an **isolated** pair, (FLOW) reduces *exactly*. Let $s=(x_2-x_1)^2$. Then
$$
\dot s = 2(\dot x_2-\dot x_1)(x_2-x_1) = 2\Bigl[\tfrac{2}{x_2-x_1}-\tfrac{2}{x_1-x_2}\Bigr](x_2-x_1) = 2\cdot\tfrac{4}{x_2-x_1}\cdot(x_2-x_1) = +8,
$$
so $s(t)=\text{gap}(0)^2 + 8t$ and the pair **collides** ($s=0$) at
$$
\boxed{\,t_{\text{coll}} = -\,\text{gap}(0)^2/8\,.}
$$
This is the **Csordas–Smith–Varga "Lehmer pair" lower-bound engine** in closed form: an isolated real pair forces $\Lambda \ge t_{\text{coll}} = -\text{gap}^2/8$ (a negative number), and a *tighter* pair pushes $\Lambda$ **up toward 0 from below**. Evaluated:

| pair | gap | norm. gap | $t_{\text{coll}}=-\text{gap}^2/8$ |
|---|---|---|---|
| live tightest (first 50, idx 34) | $0.84512$ | $0.3868$ | $-0.089279$ |
| **Lehmer 1956, zeros #6709/#6710** ($\gamma\approx 7005.063,\,7005.101$) | $0.037698$ | $0.042098$ | $\mathbf{-1.7765\times10^{-4}}$ |

(The Lehmer pair ordinates are **verified in-script** under `VERIFY_LEHMER=1`: `mpmath.zetazero(6709/6710)` returns $7005.06286617$, $7005.10056467$, matching to dps=30.) The historical Lehmer pair pins $\Lambda \ge -1.78\times10^{-4}$ — the kind of bound that drove the lower side toward $0$ before Rodgers–Tao closed it. **The isolated-pair law alone never reaches $0$ from below with finitely many zeros**: that would require an actual gap$\to 0$, i.e. a collision at $t=0$, i.e. a counterexample to RH. Conservation of difficulty.

### PART C — direct backward heat flow on a truncated $\xi$ (exact, ODE-free) [P-num]

Independent cross-check of (FLOW) from the genuine heat PDE. Build $P_0(x)=\prod_{j\le 12}(x^2-\gamma_j^2)$ (real, even, degree 24, all roots real $=\pm\gamma_j$) and evolve it under the **DBN backward heat equation** $P_t=-P_{xx}$ via the *finite* exact series $P(x,t)=e^{-t\partial_x^2}P_0 = \sum_k \frac{(-t)^k}{k!}P_0^{(2k)}(x)$. Tracking #real roots and $\max|\mathrm{Im}(\text{root})|$:

| $t$ | #real / 24 | $\max|\mathrm{Im}|$ |
|---|---|---|
| $+0.6$ | 24 | $0$ (outer gaps **grow**) |
| $0.0$ | 24 | $0$ |
| $-0.3$ | 24 | $0$ |
| $-0.5$ | **20** | $0.327$  ← complex pair (reality lost) |
| $-1.0$ | 12 | $1.162$ |

Forward $t>0$: all roots real, gaps spread (repulsion). Backward: reality is lost near $t\approx-0.5$. **Crucial caveat [P]:** the first pair to go complex is the **outermost** (truncation-edge) pair — truncation removed the outer zeros' repulsive support — so the collision time $\approx -0.5$ is an **artifact of $M=12$, not an estimate of $\Lambda$**. The *qualitative* direction (spread up / collide down) is the robust, $M$-independent content, and it confirms (FLOW) with no ODE integration. (This is precisely *why* the true $\Xi$, with infinitely many zeros supplying repulsion, has $\Lambda$ near $0$ and not at any finite-$M$ value.)

### PART D — what controls 0.22, and the residual

The script states §1's mechanism, §3's anatomy, and §5's residual in machine-checkable prose; see the embedded log.

---

## 5. Tiers, micro-observation, and the precise residual

### Tier summary
- **[P]** $\Lambda \in [0, 0.22]$; **RH $\iff \Lambda = 0$**. (Rodgers–Tao 2020; Polymath15 2019.)
- **[P]** Zero flow $\dot x_j = +2\sum_{k\ne j}1/(x_j-x_k)$; the isolated-pair law $s(t)=\text{gap}^2+8t$, $t_{\text{coll}}=-\text{gap}^2/8$, is exact and is the literal engine of the rigorous lower bounds.
- **[P-num]** Backward flow on the first 50 zeros contracts the index-34 tightest pair to collision at $t\approx-0.096$ (vs. two-body $-0.089$, delayed by ambient repulsion); the truncated heat PDE independently reproduces "spread up / collide down."
- **[A]** The $0.22$ is **dynamics-limited** (the downward-propagation margin / a uniform-in-height repulsion constant), **not height-limited**: more zero-verification does not lower it.
- **[C]** No non-circular handle on $\Lambda\le 0$ exists; the missing step is the average$\to$individual upgrade of repulsion, which equals RH.

### Micro-observation [P-num]
Among the first 50 zeros the global margin is **thinnest at the index-34 pair** ($\gamma\approx111.03$), normalized gap $\approx 0.386$ — the *same* pair `lehmer_criticality.py` flags. Its two-body collision time $-\text{gap}^2/8\approx -0.0893$ is the (weak) finite-data lower bound, **$\sim\!500\times$ weaker** than the historical $\sim\!7005$ Lehmer pair's $-1.78\times10^{-4}$. The finite-data bound is dominated by the *single* tightest pair, and that pair's gap *is* the entire margin. The thinness scales as **$\text{gap}^2$**, so closing the bound to $0$ demands an actual gap$\to 0$ — precisely a violation of RH. The finite flow can **approach** $\Lambda=0$ from below arbitrarily closely (find an ever-tighter Lehmer pair) but can **never certify** $\Lambda\le 0$.

### The precise residual
> To push $\Lambda \le 0.22$ to $\Lambda \le 0$ one needs a **uniform-in-height** guarantee that the flow (FLOW) creates **no** complex pair for **all** $t\in(0,0.22]$ at **every** height — equivalently, that the phase $\phi_t'(x)\ge 0$ is maintained uniformly as $t\downarrow 0$, equivalently that **no Lehmer pair ever collides at $t=0$**. The current obstruction is **quantitative**: the proven downward-propagation margin from a seed $t_0>0$ is an $O(1)$ quantity ($\approx 0.22$) bounded by the dynamics/repulsion constant, and that constant is **not** improved by higher numerical verification. There is no known mechanism converting the *averaged* repulsion (GUE / pair-correlation, which already yields $\Lambda\ge 0$) into the *per-pair, per-height* repulsion that would yield $\Lambda\le 0$. **$\Lambda\le 0$ is RH; this last step cannot be cheaper than RH itself.**

---

## 6. References [cited]
- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17 (1950), 197–226.
- C. M. Newman, *Fourier transforms with only real zeros*, Proc. AMS 61 (1976), 245–251.
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10 (1994), 107–129.
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, Res. Math. Sci. 6 (2019), no. 3, 31. (Upper bound $\Lambda \le 0.22$; barrier at $X\approx 6\times10^{10}$; the $f_t,g_t$ approximation and explicit error toolkit.)
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), e6. (Lower bound $\Lambda \ge 0$ via dynamics + actual-vs-flowed gap statistics.)
- Companions in this program: `reports/lehmer_criticality.md` (qualitative knife-edge), `reports/born_heat_flow.md` (Born-cone / phase-leakage framing).

---

## Appendix — run log (verbatim excerpt, `verify_debruijn_flow.py`)

```text
================  PART A : the Calogero / Rodgers-Tao zero flow (backward in t)  ============
  d x_j/dt = +2 sum_{k!=j} 1/(x_j - x_k).  Seed x_j(0)=gamma_j (true zeros).  Integrate t<0.
  seed: N=50 true ordinates; tightest pair at index 34 (gamma_34=111.02954, gamma_35=111.87466),
        gap(0)=0.845124, normalized gap(0)=0.3868.
     t           min gap        min norm.gap     tightest-pair index
        0.0   0.8451236   0.3868002   pair(34,35)
      -0.02   0.7571532   0.3465346   pair(34,35)
      -0.05   0.594877    0.2722606   pair(34,35)
   ---> COLLISION imminent at t ~ -0.096 (gap < 1e-4); reality about to be lost.

================  PART B : the Lehmer-pair collision clock (exact two-body law)  ============
  s=(x2-x1)^2 obeys ds/dt = +8  =>  s(t) = gap(0)^2 + 8 t,  t_coll = - gap(0)^2 / 8.
  LIVE tightest pair (first 50 zeros): gap=0.845124 -> t_coll = -0.0892792.
     pair (ordinates)                         gap         norm.gap     t_coll=-gap^2/8
   Lehmer 1956, zeros #6709/#6710           0.037698   0.042098   -0.00017765
   live tightest (first 50, idx 34)         0.84512    0.3868     -0.089279
  STRONGEST lower bound among these: Lehmer 1956, zeros #6709/#6710 with t_coll = -0.00017765.
  (VERIFY_LEHMER=1 recomputes #6709/#6710: gamma=7005.06286617 / 7005.10056467, matches: True)
  [P] The two-body collision law is the literal engine of the rigorous Lambda>=-eps lower bounds;
      pushing it to Lambda>=0 needs an ACTUAL gap->0 (a collision at t=0) = a counterexample to RH.

================  PART C : direct backward heat flow on a truncated Xi (exact)  =============
  P_0(x)=prod_{j<=12}(x^2-gamma_j^2), degree 24; evolve P_t = -P_xx exactly (finite series).
       t          #real roots   tightest gap     max|Im(root)|
      0.600       24 /  24       2.509518     0.000e+00
      0.000       24 /  24       1.768654     0.000e+00
     -0.300       24 /  24       1.061187     0.000e+00
     -0.500       20 /  24       1.764607     3.267e-01  <-- COMPLEX PAIR (reality lost)
     -1.000       12 /  24       2.903093     1.162e+00  <-- COMPLEX PAIR (reality lost)
  CAVEAT: the first pair to go complex is the OUTERMOST (truncation-edge) pair; t~-0.5 is an
  ARTIFACT of M=12, NOT an estimate of Lambda.  Spread-up/collide-down is the robust content.

================  PART D : what controls the 0.22, and the residual (honest)  ===============
  POLYMATH15: (i) H_t ~ B_t(f_t+g_t)+error, explicit error (e_A,e_B,e_C); (ii) barrier |f_t+g_t|>error
  on a rectangle via Rouche/interval arithmetic at height X ~ 6e10; (iii) flow propagates reality from
  seed t_0 down to ~Lambda.  Final 0.22 (intermediate 0.48).  DOMINANT term = dynamics bound, NOT X.
  WHY 0.22 IS DYNAMICS-LIMITED: raising X certifies more zeros at t_0 but does not shrink (0,t_0] nor
  the interior repulsion margin (an O(1) heat-kernel/triangle constant); X->inf leaves a positive residual.
  RODGERS-TAO Lambda>=0: if Lambda<0 the backward-heat over (Lambda,0) over-regularizes the t=0 zeros
  (gaps too rigid / energy too low) vs the PROVEN GUE-type fluctuation of the actual zeros => contradiction.
  RESIDUAL: 0.22 -> 0 needs uniform-in-height "(FLOW) makes no complex pair for all t in (0,0.22]" =
  phi'_t>=0 to t=0 = no Lehmer pair ever collides = RH.  Averaged repulsion (=>>=0) does not upgrade to
  per-pair/per-height (=><=0).  Conservation of difficulty.

================  TIER SUMMARY  =============================================================
  [P] Lambda in [0,0.22]; RH <=> Lambda=0.   [P] flow + t_coll=-gap^2/8.
  [P-num] backward collision (t~-0.096) + heat-PDE cross-check.
  [A] 0.22 dynamics-limited not height-limited.   [C] no non-circular Lambda<=0.
  MICRO [P-num]: thinnest margin = index-34 pair (gamma~111.03), norm.gap ~0.386, t_coll~-0.0893;
  ~500x weaker than the ~7005 Lehmer pair (-1.8e-4).  Margin ~ gap^2; closing to 0 = an actual collision = RH violation.
```

_(The complete, unabridged run log is in `reports/rh_debruijn_newman_runlog.txt`.)_
