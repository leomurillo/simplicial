# The Order-4 Rung: One Object, Five Readings

*Synthesis note, 2026-06-23.* Consolidates the convergence surfaced by the leverage pass
(items A2, B1, B2, C2): the quartic obstruction (Paper 21), the jerk / simplex mass
(Paper 20) and its Cartan obstruction (Paper 17), the conductor-fusion connected vertex
(T11), and the quantum order-4 coherence-leakage (Paper 44) are all readings of **one rung**
of the cumulant tower — and that rung is where the tower bifurcates. Cert:
`empirical_leverage/order4_synthesis.py` (9/9 **GREEN**, sympy + exact combinatorics, no torch).
*Staging note — folds into Papers 20/21/17/44 and Paper III §7 when those are next touched.*

## The statement

The cumulant tower has two Legendre-dual charts: the **m-chart** (negative entropy
$\varphi=\sum_i p_i\log p_i$, mixture/classical/real-cone) and the **e-chart** (log-partition
$\Phi=\log\sum_i e^{\theta_i}$, exponential/character/coherence). **Order 4 is the first rung
on which they diverge on connected content**, and that single fact is the source of five
program objects.

**The hinge (Paper III §7, Prop 7.2).** The m-chart tower $\nabla^n\varphi$ is *purely diagonal*
at every order (separability: $\partial^4\varphi/\partial p_i^2\partial p_j^2=0$ for $i\neq j$,
certified). So the connected order-4 content — the $2{+}2$ Wick block — **cannot live in the
m-chart**; it lives only in the e-chart $\nabla^4\Phi$. Order 3 has no such block (the first
all-blocks-$\ge2$ set partition is $2{+}2$, which appears at $n=4$, certified). Below order 4
the two charts carry the same connected content; at order 4 they split.

## The five readings of the one rung

| Reading | Object | Branch |
|---|---|---|
| **Paper 21** (quartic obstruction) | the e-chart $2{+}2$ Wick block itself, $\partial^4\Phi/\partial\theta_i^2\partial\theta_j^2\big|_0$ | e-chart |
| **T11** (conductor fusion) | the connected vertex $V_4^{\mathrm{conn}}$ — its character realization (914 three-prime quadruples on $\mathbb Z/30$) | e-chart |
| **Paper 20** (jerk / simplex mass) | the *dynamical* face: the order-4 leakage $m^2_{\text{simplex}}$ that the real-cone dynamics cannot avoid, **because** the connected content is e-chart-only | the obstruction's classical shadow |
| **Paper 17** (cubic Noether) | the *no-classical-quartic-charge* result (Cartan obstruction) — the same e-chart-only-ness, read as "no real conserved quartic charge exists" | why the classical branch fails |
| **Paper 44 / C2** (quantum lift) | the off-diagonal coherence the Bures-stationary trajectory grows (= the jerk on projection), carried by the dual-flat **Kubo–Mori** metric; order 4 is the **first non-dually-flat rung** (D4/O) | the quantum recovery |

The m-chart's order-4 *diagonal* coefficient ($c_4=+2$, $\partial^4\varphi/\partial p^4=2/p^3$,
certified) is the real/classical branch the dynamics *can* carry; everything in the table above
is what it *cannot*. The classical theory carries the diagonal branch and is obstructed on the
Wick branch (Papers 17/20); the quantum lift accesses the Wick branch as coherence (Paper 44),
and the metric that carries it is Kubo–Mori, not Bures (this session's D4 and Open-Problem-O
resolutions). So order 4 is exactly the rung where the program's "what is dual-flat / additive?"
answer (Kubo–Mori, valid for orders $\le3$) first becomes load-bearing: it is the first place the
dually-flat structure is *needed* and the minimal (Bures) metric provably fails.

## The closed form (closes A2's open follow-up)

The e-chart $2{+}2$ Wick block at the uniform point has the exact closed form
$$\boxed{\ \frac{\partial^4\Phi}{\partial\theta_i^2\,\partial\theta_j^2}\Big|_0=-\frac{N^2-4N+6}{N^4}\quad(i\neq j)\ }$$
verified $N=4,\dots,10$ and $N=30$, reproducing A2's tabulated values $-3/128,\,-11/625,\,-1/72,\,
-19/2048,\,-131/135000$. It is **negative** (the connected content is a *subtraction* below the
Gaussian floor — the Wick sign), and it **vanishes as $-1/N^2$** as $N\to\infty$: the order-4
obstruction is a genuinely *finite/discrete* phenomenon that disappears in the continuum, which is
why it is invisible to any continuum (order-$\le2$, Gaussian) instrument — the conductor blind spot
read at order 4.

## Why this matters

This is the single point where the program's order axis (the cumulant tower), chart axis (m vs e),
conductor/prime axis ($\mathbb Z/N$ packets), and quantum axis (Bures vs Kubo–Mori) all say the same
thing. Five separate results — an obstruction (21), a force/mass term and its energy-condition role
(20, whose $m^2_{\text{simplex}}\ge0$ is the program's weak-energy/arrow/Raychaudhuri/RH-bridge hinge),
a no-go (17), a combinatorial census (T11/Paper 21's 914), and a quantum leakage (44) — are one rung
viewed five ways, hinged on Paper III §7. The order-4 bifurcation is also the program's "why
quantization is forced": the real-cone dynamics cannot carry the e-chart-only Wick block, so the
density-matrix lift is not optional but mandatory at order 4, and the metric it must use is the
dual-flat Kubo–Mori member.

## Suggested manuscript touches (deferred, per "papers lead")

- **Paper 21 / Paper III §7**: insert the A2 cross-reference (already drafted) plus the closed form
  $-(N^2-4N+6)/N^4$ and its $N\to\infty$ vanishing.
- **Paper 20 / Paper 17**: note that the jerk's existence and the Cartan no-go are two faces of the
  e-chart-only-ness of the order-4 connected content (Paper III §7); the jerk is the obstruction's
  dynamical shadow.
- **Paper 44 / Paper III D4**: order 4 is the first non-dually-flat rung; the quantum carrier is
  Kubo–Mori (D4 + Open-Problem-O resolutions).

## Files

- `empirical_leverage/order4_synthesis.py` (9/9 GREEN).
- Pieces: `leverage_A2_paper21_chart_localization.md`, `leverage_B2_t11_vertex_calculus.md`,
  `D4_resolution_bures_kubo_mori.md`, `OpenProblemO_resolution.md`. Hinge: Paper III §7 (`01c`).
