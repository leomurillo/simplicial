# The Ultra Micro Computer (UMC) ↔ the program — connections + engineering path

**Scope.** Fuller's UMC (*Synergetics* §427.16–17, verbatim in
[fuller_synergetics_427_ultra_micro_computer.md](fuller_synergetics_427_ultra_micro_computer.md))
is the spec Andy Thomson's ABCD.EARTH **Knowledge Graph** (KG) instantiates
(Synergetics Cookbook §18; full text + notes in
[synergetics_cookbook_v0.14_fulltext.txt](synergetics_cookbook_v0.14_fulltext.txt),
[synergetics_cookbook_notes.md](synergetics_cookbook_notes.md)). This note records
(1) how our papers connect to the UMC, (2) how the Cookbook implements it, and
(3) where our information-geometry can improve it. Tiers as in the program:
**[grounded]** = real structural correspondence; **[design]** = plausible untested
proposal; **[spec]** = speculative; **[forced-match]** = flagged, not asserted.

Stripped to function, the UMC is: *a finite, geometric, addressable information
substrate — RECEIVE / STORE / RETRIEVE / CONSTELLATE — on closest-packed little
spheres, routed through fixed channels, keyed by a unit-volume control element.*
That is Fuller's geometric-hardware encoding of the program's own
**finite-grid-with-designated-channel thesis**.

---

## 1. UMC verbs → program objects

| UMC verb | program object |
|---|---|
| RECEIVE / STORE | finite capacity **log Q** of the little sphere — the Bekenstein bound (Paper 32.1 Thm 4.1) |
| RETRIEVE | the sieve / destiny window — info forced at P_n, read off the ladder (T33 §9) |
| **CONSTELLATE** | the **conductor lattice 𝒟_N** (32.1) / barcode + constant tower (T33): addressable arithmetic placement, exact complements |
| "keyed by the unit-volume Couplers" | residual keyed to the boundary **M = (ℤ/N)^× = the multiplicative units** (32.1 §7; T33 §12.3 "gravity localizes to the units") |

**Tightest [grounded]: Paper 32.1 is the capacity law of the UMC's little sphere.**
The Bekenstein bound *is* "how much information fits in a little sphere of given
energy"; the UMC *is* "a computer on closest-packed little spheres." 32.1 proves the
categorical state space is a literal little sphere (Hellinger image, curvature K=¼,
radius 2) with capacity **log Q = log(dim)**, saturated at the centroid, and exhibits
the strong-holographic signature *capacity grows while the sphere stays bounded
(R_F < π)* — exactly the UMC claim of vast capacity in an invisibly small sphere.
Caveat: 32.1's sphere is a statistical-manifold sphere, Fuller's a packing of physical
spheres — same slogan, different realization. Structural, not identical.

**CONSTELLATE [grounded].** Both papers realize the distinctive fourth verb — place
each item at a position so relationships are *addressable*: 32.1 on the conductor
lattice (Boolean 2^k prime-subset packets, each with an exact complement = Andy's
"Janus coin"); T33 via the barcode (birth π(√q) / death π(q)) and the constant tower
(each constant at a marked abscissa Li(p)).

**Meta-connection [grounded].** The UMC = Fuller's hardware picture of the finite-grid
thesis: *finite grid* = IVM / conductor lattice / categorical simplex; *strict
arithmetic capacity* = 32.1 Bekenstein log Q + finite-alphabet floor (§12.4);
*designated channel* = boundary M = units; *constellate* = exact complemented
addressing. **32.1 = capacity law + overflow channel; T33 = clock + addressing.**

**Forced-match ledger.**
- *[forced-match]* "unit-volume Couplers" ↔ "multiplicative units (ℤ/N)^×" — a real
  "control sits on the units" theme but partly a pun on *unit*; flagged, not asserted.
- *[belongs to 01d, not 32.1/T33]* the **25 / 31 / 12 great-circle channel geometry**
  is the IVM contact-routing layer = the complete-graph K_N of the 12-coordination
  (01d spine). The counts 25, 31 do **not** match the primorial ladder (6, 30, 210…);
  no numerical bridge — claiming one is a forced match. UMC *channels* = 01d; UMC
  *capacity + clock* = 32.1 + T33.

---

## 2. How the Cookbook implements the KG (as-built, §18)

A **structural / geometric index**, not (yet) a semantic one:

- **Layout (§18.1).** Each module/concept is a **Quadray lattice object** — placed at an
  integer/rational **ABCD lattice point** and projected to screen by the same
  `abcd_to_clip` matrix the geometry uses (no Cartesian roundtrip). `knowledge_graph.rs`
  reads a module inventory → generates the 3D scene (run: Cmd+Shift+K).
- **Nested cosmology (§18.2).** Concentric shells = **abstraction layers**. Shell 0 =
  *Alpha* (regular tetrahedron, "precondition for conceivability"); interior
  **tetrahedral** shell = math primitives (quadrance, spread, rotation coeffs);
  **rhombic-dodecahedral (RD / FCC) nuclear** shell = concrete polyhedra (forms);
  **outer RD** shell = application layer (instances). Shell capacities are exact integer
  formulas: **RD/FCC shell = 10ν²+2** (the FCC coordination numbers 12, 42, 92, 162, 252),
  **tetrahedral shell = ⅙ν(ν+1)(ν+2)**; inter-shell nesting ratio = a constant fixed by
  test. Reading the codebase becomes *"which layer — idea/form/instance"*, not *"which
  filename."*
- **Corpus shell (§18.3).** The whole Synergetics corpus sits on an **outer RD shell
  (252 = 10·5²+2 slots)**, each node carrying §-references that must **resolve in the
  embedded fulltext** (else "provenance regression") and the name of a **test** that runs
  any executable claim. *Claims are run, not cited.*
- **Janus coins (§18.4).** A concept is the *other face* of the module embodying it;
  complement = **central inversion** (scaling frequency through zero, P ↦ −P; only the
  tetrahedron turns inside out, §953.25) — an **exact involution**: navigate to a
  concept's opposite and *check you arrived*, vs. an embedding's fuzzy "opposite"
  direction that needn't return home when applied twice.
- **The Knot (§18.5).** Module + corpus inventories = source of truth; renderer draws
  them; "witnesses" (tests) keep them honest. Continuity across sessions = the graph.

**What the Cookbook leaves unspecified (the openings):** (i) the **intra-shell
placement metric** — *which* lattice point a module gets within its layer is inventory
fill, not semantic; (ii) any **distance / relatedness** between nodes (the layout is
structural, not content-aware); (iii) a **promotion rule** beyond geometric slot count
(10ν²+2); (iv) **overflow behavior** when a shell fills or a node fits no layer. These
are exactly what information-geometry supplies.

---

## 3. Info-geometric improvement path

Each item maps a program result onto one of §2's openings.

1. **Intra-shell placement = Fisher–Rao / Hellinger metric [grounded → design].**
   Represent each node as a distribution p (over imports / API surface / token or
   co-occurrence profile = a categorical row). Hellinger-embed `p ↦ 2√p` onto 32.1's
   round K=¼ sphere; then **node distance = Fisher–Rao geodesic = round-sphere angle** —
   the *unique* reparameterization-invariant similarity (Chentsov). Place each node at the
   IVM/ABCD lattice point nearest its Fisher position. This makes the KG's "little sphere"
   literal **and** semantic: neighbors = statistically similar modules. Upgrades "which of
   3 layers" → "where on the layer's sphere."

2. **Shell sizing / promotion = Bekenstein capacity log Q [grounded → design].**
   The Cookbook's capacity is *geometric* (10ν²+2 slots); 32.1 gives the *information*
   capacity: Q distinguishable nodes ⇒ ≤ **log Q nats**, saturated at the centroid
   (uniform spread). So (a) optimal packing spreads nodes toward the centroid (maximize
   distinguishability, don't clump); (b) the "shell full" trigger is **information
   saturation** (approaching the finite-alphabet floor §12.4), not slot exhaustion —
   promote / join the next prime on the ladder (32.1 §13 prime-joining = T33 destiny
   window) when log Q saturates. The strong-holographic signature (capacity grows,
   radius bounded) is the property you *want*: absorb information without the layout
   blowing up.

3. **Addressing = conductor lattice on the primorial ladder [grounded → design].**
   Replace shell-index ν addressing by **conductor (squarefree integer) addressing**: a
   node's address is a subset of primes = a position in the Boolean lattice 𝒟_N, with the
   **primorial ladder** ℤ/6 → ℤ/30 → … as the shell structure (a prime joining = a new
   shell) and T33's smooth `pri(z)` as the continuous index. Payoff over the Cookbook's
   single global Janus inversion: the conductor lattice has an **exact Boolean complement
   at every node** — a *complemented lattice of addressable opposites*, strictly more of
   the "addressable structure" §18.4 says it is maximizing, all exact and self-inverse.

4. **Retrieval depth = capacity-matched via the data-processing contraction [grounded → design].**
   32.1 §6: zooming out to a shell is a **monotone-metric contraction** (DPI) — it sheds
   distinguishability by a *quantified* amount. So for a query needing ~H nats, retrieve
   to the **shallowest shell with log Q ≈ H**. This operationalizes the UMC's promised
   benefit — *minimal context, resource-efficient LLM use* — as a capacity-matched
   retrieval policy: load the least context that still answers.

5. **Designated overflow channel = the boundary / units [grounded → design].**
   The Cookbook is silent on overflow; the program's thesis (and 32.1's
   boundary-localization, §7 / Prop 7.1: bulk-sourced, boundary-supported) gives the
   answer — route what fits no lattice point/layer (cross-cutting concerns, orphans, the
   off-lattice "√x residual") into a **designated units channel**. No-crash overflow into a
   named channel = the finite-grid thesis applied; it also makes the KG honest about its
   blind spot instead of silently dropping it.

6. **Edges should be order-3, not order-2 [grounded → spec].** A KG with only pairwise
   edges (cosine / Gram = the order-2 truncation) has the program's **Conductor Blind
   Spot**; the cubic (Amari–Chentsov, order-3) captures triple relationships pairwise
   misses. This matches Fuller's own substrate: the **tetrahedron is the minimum system
   (4 vertices, order-3 closure)**, so first-class **2-simplex (triangle) edges** serve
   both Fuller's tetrahedral minimum and the program's cubic. (Cf. higher-order /
   2-simplicial attention reference.)

7. **Dual charts [spec].** 01c's dual-flat (m-affine / e-affine, Legendre-dual)
   coordinates give two navigable views: m-affine = *what a node is made of* (content),
   e-affine = *how it couples* (relationship). Two charts of one KG, richer than a single
   ABCD layout.

**One-line summary.** The Cookbook builds the UMC as a *structural* index (place by
abstraction layer on FCC/RD shells, address by shell, complement by one global
inversion). Our information-geometry supplies the missing *metric* layer: Fisher–Rao
placement (literal little sphere), Bekenstein log Q capacity/promotion, conductor-lattice
addressing with exact complements everywhere, DPI-quantified capacity-matched retrieval,
a units overflow channel, and order-3 edges. 32.1 + T33 are the UMC's capacity law and
clock; 01d is its great-circle contact routing.
