# D-I — The Surprise-Debt Theorem: Why You Pay Early

*Development note, 2026-06-24.* The freest, most program-central forest seed. Turns the CBS-P4
collision weight $C_2(p)=\sum_y p_y^{-2}$ into a thermodynamic principle: the cost of capturing the
order-3 structure a second-order model is blind to is a **Schur-convex surprise debt**, minimized at
maximum entropy and compounding with commitment — so exploration captures structure cheaply and
exploitation pays a premium. The explore-then-exploit ordering is *forced* by the geometry. Cert:
`empirical_leverage/D1_surprise_debt.py` (13/13 **GREEN**, sympy/numpy, no torch). Twin of D-II
([D2_discrete_einstein.md](D2_discrete_einstein.md)): D-I is the order-3 rung, D-II the order-4.

## The functional, and its three faces

The carrier is one functional with three identities (faces (b),(c) certified here; (a) is CBS-P4):

$$C_2(p)\;=\;\sum_y \frac1{p_y^2}\;=\;\underbrace{T_p(\chi_k,\chi_\ell,\chi_m)}_{\text{(a) blind cubic coupling [P4]}}\;=\;\underbrace{\sum_y\Big|\tfrac{\partial^3\varphi}{\partial p_y^3}\Big|}_{\text{(b) }L^1\text{ third-cumulant mass}}\;=\;\underbrace{\operatorname{tr}(g^2)=\|\operatorname{Hess}\varphi\|_F^2}_{\text{(c) squared Fisher norm}}$$

with $\varphi=\sum_y p_y\log p_y$ the negative entropy (the potential) and $g=\operatorname{Hess}\varphi=\operatorname{diag}(1/p_y)$ the Fisher metric. So the surprise debt is *simultaneously*:
(a) the Amari–Chentsov cubic on every cross-packet selection-rule triple — the exact order-3 content
the circulant (two-frequency) Fisher form cannot represent (CBS-P4, 18/18); (b) the $L^1$ mass of the
diagonal third cumulant $\partial^3\varphi/\partial p_y^3=-1/p_y^2$ — the total "blind cubic"; (c) the
squared Frobenius norm of the Fisher metric, i.e. the curvature scalar of the free-energy potential.
**The order-3 blind spot, the third cumulant, and the Fisher norm are one number.**

## The theorem

**Surprise-Debt Theorem.** On the open simplex:

1. $C_2$ is **strictly Schur-convex**, with the manifest sum-of-squares certificate
   $$(p_i-p_j)\big(\partial_i-\partial_j\big)C_2=\frac{2\,(p_i-p_j)^2(p_i^2+p_ip_j+p_j^2)}{p_i^3p_j^3}\ge0,$$
   uniquely minimized at the barycenter $p_*$ with $C_2(p_*)=n^3$ (certified $n=4,6,30\to64,216,27000$),
   and $C_2\to+\infty$ at every face.
2. The entropy $H=-\varphi$ is **strictly Schur-concave**, uniquely maximized at $p_*$.
3. **Co-extremality.** $\nabla C_2$ and $\nabla H$ are both parallel to $\mathbf1$ at $p_*$: the debt
   and the entropy are stationary at the *same* point. Along any sharpening (majorization-increasing)
   trajectory $C_2$ strictly rises and $H$ strictly falls; the global minimum of the debt along the
   path is at the start ($\arg\min_t C_2(p(t))=0$).

**Corollary (explore-then-exploit is forced).** Maximizing short-term surprise (entropy / exploration)
*is* minimizing the surprise debt $C_2$ — they are one optimization, both pointing to $p_*$. An agent
that must end at a sharpened (exploited) belief pays the least to capture the order-3 structure by
capturing it while still exploring; certainty compounds the debt. **Pay early.**

## The user's principle, made exact

*"To minimize long-term surprise, maximize short-term surprise; surprise is a debt, cheapest paid
early."* This is exactly the co-extremality of a Schur-concave $H$ and a Schur-convex $C_2$:

- **Short-term surprise = entropy $H$.** High $H$ = exploratory = near $p_*$.
- **The debt = $C_2$**, the price of the still-uncaptured order-3 structure.
- Because $H$ is Schur-*concave* and $C_2$ Schur-*convex* with the *same* extremizer, **the act of
  maximizing short-term surprise is the act of minimizing the long-term debt.** There is no trade-off
  to balance — they are the same move. The "debt compounds with certainty" is $\mathrm dC_2/\mathrm dt>0$
  along sharpening; the "cheapest paid early" is $\arg\min_t C_2=0$. Both certified.

## FEP / active-inference reading [C]

$\Phi=\log Z$ is negative free energy; $\varphi=\sum p\log p$ is negative entropy (negated expected
surprise); the $\varphi\leftrightarrow\Phi$ Legendre duality is the entropy↔free-energy duality. The
surprise debt $C_2=\|\operatorname{Hess}\varphi\|_F^2$ is the *curvature* of the free-energy potential —
the epistemic cost an active-inference agent pays to resolve order-3 structure. The Free-Energy
Principle's "minimize long-term surprise" then reads: stay near $p_*$ (high entropy, exploratory) to
keep the debt minimal, and capture structure before committing. This is the program's E-series /
B-series / T17–T19 active-inference line given an exact, finite, geometric cost function. *(Tier [C]:
the identification with FEP/active-inference is a correspondence, not a derivation of those frameworks.)*

## Twin to D-II: the finite-resolution debt tower

The diagonal cumulant magnitudes are $|\partial^k\varphi/\partial p_y^k|=(k-2)!/p_y^{\,k-1}$ (certified
$k=2,3,4$): order-2 $=1/p_y$ (the Fisher metric / **space**), order-3 $=1/p_y^2$ (the surprise debt
$C_2$ / **D-I**), order-4 $=2/p_y^3$ (the mass defect $m^2_{\text{simplex}}$ / **D-II**). D-I and D-II
are adjacent rungs of one tower: the **order-3 cost of finite resolution is the surprise debt; the
order-4 cost is mass.** Both diverge as $p$ sharpens toward a face and both are absent only in the
infinite-resolution continuum. *Gravity and intelligence are the same finite-grid bill, one order
apart* — the unification the forest view promised.

## Honest tiers

- [P] **The geometry**: the three faces, Schur-convexity (SOS), minimizer $n^3$, entropy
  Schur-concavity, co-extremality, the pay-early monotonicity, the cumulant-debt tower. All certified.
- [A] **The surprise-debt reading**: identifying $C_2$ as "the price of order-3 capture" and deriving
  the explore-then-exploit ordering from Schur-convexity. Internally exact; rests on the [P] geometry.
- [C] **The FEP / active-inference identification**: a correspondence to the program's E/B/T17–T19
  lines, not a derivation of active inference.

## What D-I adds to the program

1. **The three-faces identity** $C_2=\sum1/p^2=\sum|T^{(3)}|=\operatorname{tr}(g^2)$ — unifies the
   CBS blind-cubic coupling, the third cumulant, and the Fisher norm as one functional.
2. **The Surprise-Debt Theorem**: Schur-convexity + co-extremality with entropy ⟹ explore-then-exploit
   is geometrically forced, not a heuristic. An exact, finite cost function for the explore–exploit
   tradeoff and the FEP.
3. **The debt tower** welding D-I (order-3, intelligence/surprise) to D-II (order-4, mass/gravity) as
   adjacent rungs of one finite-resolution cumulant hierarchy.

## Files

- `empirical_leverage/D1_surprise_debt.py` (13/13 GREEN).
- Source object: CBS `P4_OFFCENTER_RESULT.md` + `empirical/cbs_p4_offcenter_moving_cubic.py` (18/18),
  the off-centroid closed form $C_2(p)=\sum1/p^2$, $C_2(p_*)=n^3$.
- Anchors: ConductorBlindSpot.md §6 (Def 6.1 $\rho_\times$), Paper 01c/III (the cumulant tower),
  the FEP/active-inference line (E-series, B-series, T17–T19). Companions:
  `D2_discrete_einstein.md`, `FOREST-Brainstorm-MeaningMeasurementObserver-Draft1.md` (§2).
