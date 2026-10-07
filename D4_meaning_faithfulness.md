# D-IV — Meaning is Gauge-Invariant Connected Content (and Why Interpretability Can't Be Faithful)

*Development note, 2026-06-24.* The capstone seed — it asks what of the whole structure is *objective*
and what is *perspectival*, and answers with a three-rung hierarchy of meaning that closes the forest
quartet. Cert: `empirical_leverage/D4_meaning_faithfulness.py` (11/11 **GREEN**, numpy/sympy, no torch).
The faithfulness-obstruction philosophy made exact; ties FaithfulnessObstruction.md, CBS, vec2vec.

## The thesis

Meaning is **gauge-invariant connected content**. Two qualifiers, each a rung:

| order | content | status | meaning |
|---|---|---|---|
| 1 | absolute coordinate $c_i$ | **gauge** | none — the overflow line $\mathbf 1$ |
| 2 | the metric (Fisher / $K_N$) | **objective** | the faithful core; both charts agree |
| $\ge3$ | connected (cubic, Wick) | **perspectival** | compositional; e-chart-only; *hidden* |

- **Gauge-invariant**: only the *differences* $c_i-c_j$ carry meaning; the absolute coordinate is a
  gauge direction (the null line $\mathbf 1$). Meaning is relational, never absolute.
- **Connected**: the metric (order-2) is the objective core both observers agree on, but the
  *compositional* meaning — the connected order-$\ge3$ cross-content — lives in the blind spot of any
  order-2 instrument. That is the **faithfulness obstruction**.

## The certified skeleton

**(1) Meaning is gauge-invariant.** $M_N\mathbf 1=0$: the absolute/uniform coordinate is the null
direction of the metric (certified), with spectrum $\{0$ on $\mathbf 1$, $N$ on $H\}$. Meaning lives on
the zero-sum hyperplane $H$ — the differences $c_i-c_j$ have positive $M$-norm; the gauge line $\mathbf 1$
has none. *The absolute is meaningless; only relations mean.*

**(2) Objective meaning is the order-2 self-dual rung.** The order-2 cumulant at $p_*$ equals $1/p_*=N$,
which equals the $K_N$ Hodge-Laplacian eigenvalue on $H$ — the rung where cumulant, metric, and Laplacian
*coincide*. The order-2 metric is a symmetric tensor, chart-covariant: $g$ and its Legendre dual $g^{-1}$
are the same bilinear form. **Order-2 is the one rung both the m-chart (inside) and e-chart (outside)
observer agree on** — the objective, self-dual core.

**(3) Perspectival meaning is order-$\ge3$ connected, e-chart-only.** The m-chart (classical) connected
cross blocks vanish at orders 3 and 4 (certified) — the classical reading has *no* compositional content.
The e-chart carries them (the order-4 Wick block $-(N^2-4N+6)/N^4$). **Compositional meaning is
chart-dependent and hidden from the inside observer.**

**(4) The faithfulness obstruction.** The kernel of the order-$\le2$ moment map $[\,1,v,v^2\,]$ is spanned
by the **third finite difference** $[-1,3,-3,1]=(1-1)^3$ — the order-3 direction. Adding it to a
distribution leaves mean and variance *exactly* fixed while changing the third cumulant. So two genuine
distributions ($p=[.20,.40,.10,.30]$, $q=[.30,.10,.40,.20]$) are **identical to every order-2 instrument**
(same mean, same variance) yet differ in their order-3 (skew). The compositional meaning is invisible to
the order-2 probe. (The program instance: the Fisher form is circulant in $k-\ell$, a two-frequency object;
the cubic lives on $k+\ell+m\equiv0$, three-frequency — no order-2 operator represents it, CBS-P4 18/18.)

## What it means: interpretability's faithfulness crisis is structural [A]

Probes, lenses, and SAEs are **order-2 instruments** — they read correlations, Gram matrices, linear
structure. By (2) they faithfully recover the *objective* meaning (the metric, the self-dual core). By
(4) they are *provably blind* to the *compositional* meaning — the connected order-$\ge3$ content, which
is most of what "meaning" colloquially is (context, composition, binding). The faithfulness crisis is
therefore **not a tooling problem to be engineered away** — it is the structural fact that an order-2
readout of an order-$\ge3$ world loses the connected content by construction, and capturing it requires
climbing the order axis (obstructed at order 4, D-II; e-chart-only, D-III). This is the exact, finite
backbone of FaithfulnessObstruction.md and the vec2vec order-2 floor.

## The quartet closes: four seeds, one cumulant tower

D-IV is the reading that reveals the other three as facets of one object — the gauge-quotiented,
connected cumulant tower on the categorical simplex:

- **order-2** = the metric = **space** (D-II background) = **objective meaning** (D-IV) = what the
  **inside observer sees** (D-III) — the self-dual, both-charts-agree core.
- **order-3** = the **surprise debt** (D-I, intelligence) = the first compositional/perspectival meaning.
- **order-4** = the **mass** (D-II, gravity) = the dual-flatness defect.
- the **antisymmetric** sector = the **arrow** (D-III, time).
- **order-1** = position = **gauge** = meaningless absolute.

Meaning, mass, intelligence, measurement, and time are five names for the structure of one finite
categorical cumulant tower. The objective is order-2 (and gauge-invariant); everything that *moves* —
the debt, the mass, the arrow, the compositional meaning — is the connected, chart-dependent content
above it, and it is exactly what a finite inside observer pays surprise to see. *That is the forest, whole.*

## Honest tiers

- [P] **The skeleton**: gauge-invariance ($M_N\mathbf 1=0$, spectrum $\{0,N\}$); the order-2 self-dual
  coincidence ($1/p_*=N=$ eigenvalue); m-chart connected blocks vanish while e-chart carries the Wick
  block; the faithfulness obstruction (order-2-matched, order-3-distinct distributions; the third-finite-
  difference kernel). All certified.
- [A] **The meaning reading**: objective = order-2 / gauge-invariant; perspectival = connected order-$\ge3$;
  interpretability = order-2 readout of an order-$\ge3$ world. A faithful structural identification.
- [C] **The colloquial-"meaning" identification** (context/composition/binding $\leftrightarrow$ connected
  higher cumulants): a correspondence, not a theory of semantics.

## What D-IV adds to the program

1. **The meaning hierarchy** — order-1 gauge / order-2 objective / order-$\ge3$ perspectival — placing the
   gauge-quotient, the self-dual metric, and the connected tower on one axis of "what is objective."
2. **A clean, self-contained faithfulness obstruction** (the third-finite-difference kernel; two
   order-2-matched distributions) — the exact statement that interpretability's crisis is structural.
3. **The closure of the quartet**: meaning, mass, intelligence, measurement, time as five readings of one
   finite cumulant tower, with the objective core at order-2 and everything dynamical above it.

## Files

- `empirical_leverage/D4_meaning_faithfulness.py` (11/11 GREEN).
- Companions: `D1_surprise_debt.md`, `D2_discrete_einstein.md`, `D3_observer_measurement.md`,
  `FOREST-Brainstorm-MeaningMeasurementObserver-Draft1.md` (§4). Anchors: FaithfulnessObstruction.md,
  ConductorBlindSpot.md (the order-2-vs-3 gap), the vec2vec order-2 floor, Paper 01b/IV (gauge line
  $\mathbf 1$, $H^0$, the universal eigenvalue $N$), Paper 01c/III (the m/e charts, the cumulant tower).
