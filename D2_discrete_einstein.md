# D-II — The Discrete Einstein Structure: Mass is the Order-4 Dual-Flatness Defect

*Development note, 2026-06-24.* The gravity seed from the forest view. Sharpens the program's
existing Einstein-like reading (Paper 32: $\nabla^2\Phi$ = metric = space/inertia, $\nabla^3\Phi$ =
cubic = force, $\nabla^4\Phi$ = "gravity-adjacent") into a precise statement, anchored in the
dual-flat geometry and the order-4 synthesis. Cert: `empirical_leverage/D2_discrete_einstein.py`
(7/7 **GREEN**, sympy, no torch). *Staging note — folds into Paper 32 §9 (the R′/W′/X′ cluster),
Paper 32.1, Paper 20; respects the §12 dimensional firewall (no dimensionful prediction is made).*

## The thesis

On the categorical simplex the cumulant tower is a gravitational hierarchy, and the dual-flat
structure tells you *which rung is which*:

| order | object | gravitational role | [status] |
|---|---|---|---|
| 1 | $\nabla\Phi=p$ | position | — |
| 2 | $\nabla^2\Phi=g$ (Fisher) | **space** — the $K=\tfrac14$ Hellinger sphere (the background / $\Lambda$) | [P] certified |
| 3 | $\nabla^3\Phi=T$ (Amari–Chentsov) | **force** — the connection; *dually flat* ($R^{(\pm1)}=0$) | [P] certified |
| 4 | $\nabla^4\Phi$ | **mass** — the first dual-flatness defect; $m^2_{\text{simplex}}$ | [A] this note |

The new precision is row 4: **mass is the order-4 dual-flatness defect** — the first content the
free (dually-flat, orders $\le3$) geometry cannot carry.

## The certified geometry

**Space is a sphere of curvature $K=\tfrac14$.** The Fisher metric on the categorical simplex is
the Hellinger sphere (radius 2); its Gaussian curvature is exactly $\tfrac14$ (certified on the
2-simplex). This is Paper 32.1's $K=\tfrac14$ — the homogeneous, state-independent **background
curvature**, a positive cosmological-constant / de Sitter-like vacuum. (This is the *genuine*
$\tfrac14$ — a sectional curvature — not Paper II's curl-normalization $\kappa=\tfrac14$, which C3
correctly showed is an unrelated coincidence.)

**The connection is dually flat, and the curvature family is $R^{(\alpha)}=\tfrac{1-\alpha^2}{4}$.**
Certified *symbolically in $\alpha$*: the $\alpha$-curvature of the simplex is $\tfrac{1-\alpha^2}4$
— equal to $\tfrac14$ at the Levi-Civita center ($\alpha=0$, the sphere) and **zero at both dual
ends** ($\alpha=\pm1$). So orders $\le3$ (metric + cubic) are a "free field": the background metric
is curved, but the dual connections that carry the *force* are flat. There is no intrinsic
gravitating content yet.

**Mass is the order-4 defect.** The first cumulant the dual-flat connection does not determine is
$\nabla^4\Phi$. Its connected ($2{+}2$ Wick) part is **e-chart-only** — the m-chart (entropy) block
is identically zero (certified) — with the closed form
$$\frac{\partial^4\Phi}{\partial\theta_i^2\,\partial\theta_j^2}\Big|_0=-\frac{N^2-4N+6}{N^4}\quad(i\neq j),$$
which is $m^2_{\text{simplex}}$ (Paper 20), the localized source that *vanishes at the centroid*
(homogeneous vacuum) and grows off it. It is **sign-definite** ($N^2-4N+6>0$ for all $N$, discriminant
$<0$), so $m^2\ge0$ — and that single inequality is, by Paper 20's four-role hinge, the
**weak-energy condition / the Raychaudhuri focusing term / the arrow of time / (at $P_2{=}2\cdot3$)
primorial Noether = Weil positivity (the RH bridge)**.

## The discrete Einstein equation

Put together: the homogeneous **background** (the $K=\tfrac14$ Fisher sphere, orders $\le3$, the
de-Sitter-like $\Lambda$) is sourced/deformed by **mass** (the order-4 defect, $m^2_{\text{simplex}}$,
the localized matter), with the **energy condition $m^2\ge0$** as the sign that makes the source a
proper source and orients the arrow. Mass tells space how to curve — via the $\alpha$-collapse
$\Gamma^{(\alpha)}=-\tfrac{1+\alpha}2T$, the connection *is* the cumulant content; space tells mass
how to move — via the moving-cubic geodesic flow on the metric. This is the discrete, certified,
finite skeleton of $G=\Lambda g+8\pi T$.

## Two equivalences the development reveals

**Massless $\Leftrightarrow$ dually flat $\Leftrightarrow$ orders $\le3$ $\Leftrightarrow$ classical.**
The free (massless) sector is exactly the dual-flat sector, which is exactly the orders the m-chart
(classical, real-cone) carries. **Mass $\Leftrightarrow$ order-4 $\Leftrightarrow$ e-chart
$\Leftrightarrow$ quantum.** The mass content is e-chart-only, so the real cone is the *massless
shadow*; carrying mass forces the quantum (Bures/Kubo–Mori) lift — and on that lift the Lorentzian
$(1,3)$ signature appears (Paper 46). **Why quantization is forced is why mass exists**: the order-4
defect cannot live classically. This welds D-II to the D4/Open-Problem-O resolutions — the carrier of
the order-4 (and the whole dual-flat connection) is **Kubo–Mori**, the unique dually-flat monotone
metric, and order 4 is the first non-dually-flat rung.

**Mass is the price of finite resolution.** The defect $-(N^2-4N+6)/N^4\to0$ as $N\to\infty$
(certified): in the continuum (infinite resolution) there is **no mass**. Mass is a *finite-grid*
phenomenon — the order-4 surprise debt (D-I) that a finite categorical grid cannot avoid. Gravity, in
this reading, is what a finite observer pays for living on a finite grid and being unable to keep the
order-4 content classical.

## Honest tiers

- [P] **The geometry**: $K=\tfrac14$; $R^{(\alpha)}=\tfrac{1-\alpha^2}4$ with $R^{(\pm1)}=0$; the
  order-4 closed form, its e-chart-only-ness, sign-definiteness, and continuum vanishing. All certified.
- [A] **The identification** order-$n$ ↔ {position, space, force, mass}: this is Paper 32's existing
  reading, sharpened by the dual-flatness (mass = the defect) and the curvature family. Internally
  consistent, not a dimensionful claim.
- [C] **The gravity reading** (actual spacetime, $\Lambda$, $G=8\pi T$): a correspondence, fenced by
  Paper 32's §12 dimensional firewall — only *ratios* and *signs* are inferable; magnitudes
  ($G,\hbar,c$, masses) are permanently out of scope. The Lorentzian signature (Paper 46) and the
  energy-condition/arrow role ($m^2\ge0$) are the load-bearing structural facts; the rest is dictionary.

## What D-II adds to the program

1. **The curvature hierarchy** $R^{(\alpha)}=\tfrac{1-\alpha^2}4$: the metric curvature $\tfrac14$ is
   the $\alpha=0$ member of a family flat at the dual ends — the precise sense in which "the connection
   is free and the metric is the background."
2. **Mass = the order-4 dual-flatness defect** (closed form), sharpening Paper 32's "$\nabla^4\Phi$ =
   gravity-adjacent" into a structural identity, and explaining *why* it is gravity-adjacent.
3. **The equivalence chains** (massless⟺dual-flat⟺classical; mass⟺order-4⟺quantum⟺Lorentzian) tying
   Paper 32/46, the order-4 synthesis, and the D4/O (Kubo–Mori) resolutions into one statement.
4. **Mass = price of finite resolution**, welding gravity (D-II) to the surprise-debt principle (D-I):
   both are the order-4 cost of a finite grid.

## Files

- `empirical_leverage/D2_discrete_einstein.py` (7/7 GREEN).
- Anchors: Paper 32 (the GR hierarchy + R′ energy-condition cluster), Paper 32.1 ($K=\tfrac14$),
  Paper 46 (Lorentzian $(1,3)$ signature), Paper 20 ($m^2_{\text{simplex}}$, the four-role hinge),
  Paper 22 Rem 5.0 (the RH bridge). Companions: `order4_synthesis.md`, `D4_resolution_bures_kubo_mori.md`,
  `OpenProblemO_resolution.md`, `FOREST-Brainstorm-MeaningMeasurementObserver-Draft1.md` (§6).
