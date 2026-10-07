# [HF SANDBOX] A Firewall Crossing: The Inertial Projector and Its Consistency Checks

> **FENCED — Historic-Fiction / sandbox.** This note *deliberately* violates the Paper 32 §12
> dimensional firewall, which permanently forbids dimensionful cash-out. **Nothing here is a claim
> about physical reality.** It is a *consistency test*: if we inject exactly one unit, does the
> dimensionless structure behave like a self-consistent natural-units physical theory? Result: yes —
> modulo exactly one undetermined scale, which is precisely what the firewall protects. Cert:
> `empirical_leverage/firewall_crossing.py` (10/10 GREEN).

## The inertial projector

In natural units (ℏ = c = 1) every quantity is a power of one mass anchor M₀. The e-chart natural
parameter θ carries dimension [M]⁻¹, so ∂ⁿΦ/∂θⁿ — the n-th cumulant — has dimension [M]ⁿ. Define
$$P_{M_0}:\ (\text{dimensionless } X \text{ of cumulant-grade } n)\ \longmapsto\ X\cdot M_0^{\,n}\ \ (\text{dimension } [M]^n).$$
It is a **graded-ring homomorphism** fixed by a single scale, and it is *inertial* because fixing the
order-2 rung (the Fisher metric = inertia, Paper 32) **is** fixing M₀². One unit, injected at the
inertia rung, propagates up the whole tower.

## What the crossing reveals (all certified in the sandbox)

1. **Einstein's two sides land on the right rungs.** order-2 → [M]² = **curvature** (the geometry,
   the LHS); order-4 → [M]⁴ = **energy density** (the source, the RHS). This is non-trivial and it
   *holds* — the cumulant grading and the GR dimensions agree without being made to.
2. **The Einstein equation closes and emits G.** R = 8πG ρ ⟹ G = K/(8π m² M₀²), dimension [M]⁻²,
   and **G > 0 because m² > 0** — the energy condition (D-II) becomes *attractive* gravity.
3. **The Planck-to-anchor ratio is a pure number the structure fixes**: M_Pl/M₀ = √(8π m²/K),
   M₀-free — 1.535 at N=4, 1.182 at N=6. (Firewall-legal as a *ratio*; the anchor itself is not.)
4. **ρ_Λ ~ M₀⁴** — the vacuum-energy density carries the **quartic UV-sensitivity**, the exact
   signature of the cosmological-constant problem. The sandbox reproduces a recognized feature of
   real physics rather than evading it.
5. **A real tension surfaces, honestly.** Since m² ~ 1/N² → 0, the three scales {G, ρ_Λ, M₀} cannot
   all stay finite in the continuum (G·M₀² ~ N² diverges — gravity strong at fine resolution). The
   crossing does not hide this; it is the lattice/UV analogue of the CC problem.

## What it sharpens, and what it honors

- **"Mass" is energy density.** The loose D-II label "order-4 = mass" sharpens under units to
  **order-4 = energy density [M]⁴** — the *source* T_μν, not a mass [M]¹. The crossing corrects the
  word.
- **The firewall is vindicated, not defeated.** Everything — G, Λ, ρ_Λ, M_Pl — comes out as
  (dimensionless structure) × M₀^k. **Exactly one scale, M₀, is undetermined**, and that is precisely
  the absolute scale §12 says is permanently out of scope. The crossing shows the structure is a
  *complete natural-units theory waiting for one anchor* — and that it cannot, and must not, supply
  the anchor itself.

## Honest tier

Entirely **[HF]** — a fenced sandbox consistency test. The *dimensional algebra* is exact (10/10);
the *interpretation* (these rungs are physical curvature / energy density / G) is the firewall
correspondence taken one deliberate step past where the program normally stops, purely to check
self-consistency. The takeaways that survive back on the legal side of the firewall: (i) order-2 and
order-4 are dimensionally the curvature and the source — a structural fact; (ii) M_Pl/M₀ = √(8π m²/K)
is a genuine dimensionless ratio; (iii) the lone free scale M₀ is exactly the firewall's content.

## Files
- `empirical_leverage/firewall_crossing.py` (10/10 GREEN). Companion to `D2_discrete_einstein.md`,
  `cosmo_hunt.py`, `PREREG_w_eq_minus1_DESI.md`. Anchors: Paper 32 §12 (the firewall), Paper 32.1
  (K=¼), Paper 20 (m² energy condition).
