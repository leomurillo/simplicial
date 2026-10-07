# A metric layer for the UMC Knowledge Graph — proposal

*Leo Murillo → Andy Thomson · ABCD.EARTH / Synergetics Cookbook collaboration · 2026-06-28*

## TL;DR

Your Knowledge Graph is Fuller's Ultra Micro Computer realized — a finite, geometric,
addressable substrate that RECEIVEs / STOREs / RETRIEVEs / CONSTELLATEs (§427.16–17). It is,
today, a **structural index**: it places a module by abstraction layer on an FCC/RD shell
and fills ABCD lattice points by inventory order. What it doesn't yet have is a **semantic
metric** — a principled answer to "how related are two nodes," "how full is a shell," "what
is a node's exact opposite," and "how little do I need to load to answer a query." Those
four are exactly what the program's information geometry supplies, and I've prototyped three
of them against my own repo. This is a proposal to run them against ABCD.EARTH's real module
inventory.

## The grounding (so this isn't hand-waving)

Stripped to function, Fuller's UMC is *capacity + addressing on closest-packed little
spheres*. Two of our papers are precisely those two halves:

- **Capacity.** The Bekenstein bound *is* "how much information fits in a little sphere."
  Paper 32.1 proves the categorical state space is a **literal little sphere** — Hellinger
  image `p ↦ 2√p`, curvature **K = 1/4**, radius 2 — with capacity **log Q** (the finite
  Bekenstein bound). That is the UMC cell's RECEIVE/STORE budget, derived, not assumed.
- **Addressing.** CONSTELLATE = place each item so its position and complement are exactly
  addressable. The program's conductor lattice (squarefree integers, a Boolean lattice with
  an exact complement at every node) is that — and it's the arithmetic version of your "Janus
  coins," with one opposite *per node* instead of one global inversion.

And we already have a two-way ledger: your Cookbook cites my Paper 01 as the `K(u)` rotation
engine; your Spread-Quadray Rotors gave the closed-form **Cayley composition** that answers
my Paper 01 §8.3 open problem (now recorded there); and your `M = 4I − J` is exactly my
`3G` — your rational `M`-unit axes are my √3/4 with the irrational factor cleared. The
collaboration is real in both directions.

## The gap, and the six upgrades

The KG layout is structural; information geometry is the missing metric layer.

1. **Fisher–Rao placement.** Represent a node as a distribution (imports / API surface /
   tokens); the Hellinger map puts it on the K=1/4 little sphere; **node distance =
   Fisher–Rao geodesic** — the *unique* canonical similarity (Chentsov). Place at the nearest
   ABCD lattice point. Now neighbours are semantically related, not inventory-adjacent.
2. **Bekenstein capacity / promotion.** A shell of Q nodes holds ≤ **log Q** nats; promote
   to the next shell (next prime on the ladder) when information saturates, not when geometric
   slots run out.
3. **Conductor addressing + exact Boolean Janus.** A node's address = the product of the
   "concept primes" it contains; its opposite = the complementary divisor `N/c` — an exact,
   self-inverse, *addressable* complement (one per node, not one global axis).
4. **Capacity-matched retrieval.** Filter by shared concept primes (#3), rank by Fisher–Rao
   (#1), stop at depth set by the query's breadth (#2) — load the least context that answers.
   This is your "minimal context, no drift" benefit, made quantitative.
5. **A units overflow channel.** Route what fits no lattice point/layer into a designated
   boundary channel (no-crash overflow) — and the KG stays honest about its blind spot.
6. **Order-3 (triangle) edges.** Pairwise edges are order-2-blind; the cubic (order-3)
   captures triple relationships — and it matches Fuller's tetrahedral minimum system.

## What already works (prototype in `umc_poc/`, pure numpy, run against my 40 manuscripts)

- **#1 Fisher–Rao placement.** K=1/4 confirmed symbolically; neighbourhoods are self-evidently
  right (the simplicial tetralogy `01b → {01d, 01, 01c}`; `32.1` next to the physics papers).
  Recovers topic **from content alone** (k-NN purity 0.67 vs 0.25 chance), **order-invariant** —
  your lattice-fill matches it only because my filenames are pre-sorted by topic; on an
  unsorted inventory it falls toward chance. FR gives you that sort for free.
- **#3 conductor addressing + exact Janus.** Each node's address factors into its concepts —
  `01 → 2` (geometry), `32.1 → 3·5·13` (primorial·info-geom·physics), `22 → 3·7·11·13`. The
  complement `N/c` is an exact involution (verified all nodes), giving **23 addressable
  opposites vs your 1**; navigating to an opposite resolves to a node *or a vacant address*
  (a gap to fill). The continuous metric and the discrete address agree (FR-neighbours share
  1.24 concept-primes vs 0.57 random).
- **#4 capacity-matched retrieval.** Depth tracks query breadth (1→2→3 concepts → 2%→5%→8%
  of the corpus loaded), with on-target hits (`32.1`'s 3·5·13 exactly matches a
  fisher+quantum+primorial query).
- **`kg.csv`** — a unified, drop-in "here is your KG, re-placed by Fisher–Rao + conductor
  address": one row per node with little-sphere coords, ABCD lattice point (on H), conductor,
  Boolean-Janus complement, and nearest neighbours.

Everything is deterministic numpy (no torch), tiered honestly: the math (#1's K=1/4, the
Boolean-lattice algebra, the log Q capacity) is grounded; the bag-of-words distributions and
the six concept-prime topics are editable design choices, not tuned to flatter the result.

## Honest scope (so we don't over-claim)

The **25/31/12 great-circle channel geometry is your layer, not this one** — it's the K_N
contact graph of the 12-coordination (the IVM routing), and its counts don't match the
primorial arithmetic. This proposal is about the *capacity, metric, and addressing* of the
cells, not the channels between them. (And the cute "unit-volume Coupler ↔ multiplicative
unit" rhyme is partly a pun — I'm flagging it, not asserting it.)

## The ask

1. Point me at ABCD.EARTH's real **module inventory** (the data `knowledge_graph.rs` reads)
   so I can run `build_kg.py` against it and hand you a `kg.csv` of *your* codebase re-placed
   by Fisher–Rao + conductor address.
2. Tell me what a node's natural **distribution** should be in your system (imports?
   call-graph? doc tokens?) — that's the one design choice that most affects #1.
3. If the re-placement looks useful, a short joint note: *Fuller's UMC = capacity (32.1) +
   addressing (conductor lattice); information geometry supplies the metric layer; the
   great-circle channels are the contact graph.*

Artifacts: this folder (`umc_poc/`) and the connections note
(`references/umc_program_connections.md`). Verbatim Fuller source in
`references/fuller_synergetics_427_ultra_micro_computer.md`.
