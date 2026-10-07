# umc_poc — Fisher–Rao placement for the UMC Knowledge Graph (proof of concept)

A runnable proof-of-concept of **improvement #1** from
[`../references/umc_program_connections.md`](../references/umc_program_connections.md):
give the Synergetics-Cookbook Knowledge Graph (UMC, §18) the *semantic metric layer*
it lacks, using the information geometry of **Paper 32.1** (the little sphere) and
**01c** (the categorical-simplex Fisher metric).

The Cookbook KG is a **structural index**: it places a module by abstraction layer on an
FCC/RD shell and fills lattice points by inventory order — there is no content-aware
distance between nodes (Cookbook §18.1–18.2). This POC supplies that distance and shows
it does real work, against the repo's **own manuscripts** as the node inventory.

## What it demonstrates

| step | claim | result (40 manuscripts) |
|---|---|---|
| little sphere literal | Hellinger `p ↦ 2√p` lands on radius-2, curvature **K = 1/4** | radius = 2.000000 exact; symbolic K = **1/4** (Brioschi) |
| semantic metric | Fisher–Rao `d = 2·arccos(BC)` ∈ [0, π] gives coherent neighbours | `01b → {01d, 01, 01c}`, `32.1 → {32, 32, 20}`, `12 → {11, 10, 25}` |
| beats structural index | k-NN purity from **content**, order-invariant | FR **0.67** vs shuffled-inventory **0.35** vs random **0.25** |
| capacity | shell capacity = **log Q** (finite Bekenstein, 32.1 Thm 4.1) | per-shell log Q reported; occupancy near saturation |
| placement | MDS → **ABCD/IVM lattice** snap preserves proximity | FR↔lattice Spearman ρ = **0.79** |
| retrieval | coarse-graining is a **monotone contraction** (DPI, 32.1 §6) | coarse/fine FR ratio mean **0.22** ≤ 1 |

**The honest headline.** Fisher–Rao recovers the corpus topology *from content alone*
(purity 0.67, chance 0.25), and is invariant to inventory order. The Cookbook's
lattice-fill matches it (0.67) **only because these filenames are already hand-sorted by
topic**; on a realistic un-sorted inventory the structural index falls toward chance
(0.35). FR gives you the sort for free — which is exactly what a UMC needs when module
names don't encode topic.

## Files

- `fisher_kg.py` — core, pure numpy: Hellinger embed, Bhattacharyya/Fisher–Rao matrix,
  Bekenstein capacity, classical MDS, Tom-Ace `xyz → zero-sum Quadray` map (`q = ¼ B·xyz`,
  Cookbook §6) + lattice snap (§12.3), M-metric distance, k-NN purity, DPI contraction.
- `poc.py` — improvement #1 driver: builds vocabulary distributions from the repo's `*.md`
  manuscripts, runs the Fisher–Rao pipeline, prints the report, writes `kg_layout.csv`.
- `conductor_kg.py` — improvement #3 core: concept-prime topics, content → squarefree
  **conductor**, Boolean-lattice operations (complement `N/c`, meet `gcd`, join `lcm`, rank `ω`).
- `poc_conductor.py` — improvement #3 driver: assigns each manuscript a conductor address,
  exhibits the exact Boolean Janus complement, checks #1↔#3 agreement, writes
  `conductor_addresses.csv`.
- `build_kg.py` — **(a) unified export**: runs #1 and #3 and writes one drop-in `kg.csv`.
- `retrieve.py` — **(b) improvement #4**: capacity-matched retrieval (minimal context).
- `kg_layout.csv` / `conductor_addresses.csv` — per-improvement exports.
- `kg.csv` — **the unified KG**: one row per node with little-sphere `x,y,z` [#1], ABCD
  lattice `A,B,C,D` on H [#1], `conductor/factorization/rank` + `complement` [#3], and the
  top-3 Fisher–Rao neighbours [#1]. This is the single artifact a renderer/agent consumes.

## Run

```
cd umc_poc
py poc.py             # improvement #1: Fisher–Rao placement
py poc_conductor.py   # improvement #3: conductor-lattice addressing + Boolean Janus
py build_kg.py        # (a) unified export -> kg.csv
py retrieve.py        # (b) improvement #4: capacity-matched retrieval
```

## The KG as a tool — operations (`kg_store.py` / `kg.py`)

A **persistent** (JSON-backed) `KnowledgeGraph` with a CLI, so an agent can call it. The
operation set is the CRUD analog of Fuller's RECEIVE / STORE / RETRIEVE / CONSTELLATE plus
the geometry-native ops.

| group | operations |
|---|---|
| create / store | `build(docs)`, `add(id,text)` (RECEIVE), `update`, `delete` (leaves a gap), `rebuild` (re-CONSTELLATE) |
| read / retrieve | `get`, `neighbors`, `distance`, **`context(query)`** (capacity-matched minimal context) |
| geometry-native | `complement` (exact Boolean Janus), `meet`/`join` (concept lattice), `gaps` (vacant addresses), `shells` (Bekenstein log Q) |
| persistence | `save`/`load` (JSON store) |

```
py kg.py build                                  # constellate the repo's manuscripts
py kg.py context "fisher quantum bekenstein"    # -> ranked docs + snippets at minimal depth
py kg.py neighbors 01b                          # 01d, 01, 01c, 04
py kg.py complement 01                          # -> opposite address + occupants (or a gap)
py kg.py gaps                                    # vacant concept-combinations (what's missing)
py kg.py add mydoc path/to/file.md              # RECEIVE a new document
```

**Agentic use.** `context(query)` is the retrieval tool: it returns the *least* set of
documents (ids + snippets, ranked by Fisher–Rao, depth set by query breadth) that covers the
query's concepts — the minimal context to hand an LLM. Wire it as an agent tool
`kg_context(query) -> docs`. The store is persistent, so build once and query repeatedly.

**Honest limits.** Bag-of-words distributions (swap in import/call-graph or embedding
distributions for production); the vocabulary is fixed after `build` (so `add` projects onto
it and its placement is approximate — call `rebuild` to re-constellate exactly); the concept
primes / thresholds are editable design choices.

Pure `numpy`; `sympy` optional (only the K = 1/4 curvature check). No torch (local gate).

## Tiers / honesty

- **[grounded]** the math: K = 1/4 little sphere, Fisher–Rao = unique monotone metric
  (Chentsov), log Q capacity, DPI contraction, the exact `q = ¼ B·xyz` ABCD map.
- **[design]** the engineering choices: bag-of-words distributions (a real system would
  use call-graph / import / embedding distributions), top-400 vocab, coarse 3-family
  ground-truth labels (author-supplied, for the purity metric only — editable in `poc.py`).
- **limitations:** 3-D MDS is a lossy projection of a 400-dim sphere (ρ = 0.79, not 1);
  lattice collisions remain at low frequency (raise `freq`); families are coarse and have
  genuine cross-talk (01c is both frame and info-geom). None of this is tuned to flatter
  the result — the verdict is the content-vs-shuffle gap, which is robust.

## Improvement #3 — conductor-lattice addressing + exact Boolean Janus

The Cookbook gives each node **one** global complement (central inversion, §18.4). Here a
node's *address* is a content-derived squarefree **conductor** c | N: assign six "concept
primes" (2 geometry, 3 primorial, 5 info-geometry, 7 RH/zeros, 11 characters, 13
quantum/physics), each a topic of marker terms; a node gets prime p iff it is above-average
on that topic; its conductor is the product. The address *factors into the node's concepts*.

Run against the 40 manuscripts (`poc_conductor.py`):

| node | conductor | reads as |
|---|---|---|
| `01` vector algebra | **2** | geometry only |
| `32.1` Bekenstein | **3·5·13** | primorial · info-geom · physics |
| `22` primorial-cumulant-RH | **3·7·11·13** | primorial · RH · characters · quantum |
| `15` density-matrix mechanics | **13** | quantum only |

- The address space is the **Boolean lattice 2⁶** (23 of 64 points used; ranks ω=0..4
  populated) — the Cookbook's "packets = 2^k", made content-addressable.
- **Exact Boolean Janus:** complement `N/c` is an involution (`comp(comp(c))=c`, verified
  for all nodes) and rank-complemented (`ω(c)+ω(c̄)=6`), giving **23 addressable opposites**
  vs **1** global inversion. Lattice algebra: meet = `gcd` (shared concepts), join = `lcm`.
- **Navigate-and-check (the UMC promise):** `01`'s opposite (3·5·7·11·13 = "everything but
  geometry") resolves to a **vacant address** — you arrive *and* learn it's an unfilled gap.
- **#1 ↔ #3 agree:** Fisher–Rao neighbours share **1.24** concept-primes on average vs
  **0.57** random — the continuous metric (little sphere) and the discrete address (Boolean
  lattice) are consistent.

[grounded] the Boolean-lattice algebra and the involution; [design] the six concept-prime
topics and z>0 thresholding (editable in `conductor_kg.py`).

## Improvement #4 — capacity-matched retrieval (minimal context)

`retrieve.py` uses all three ideas at once: #3 picks the query's concept primes (filter),
#1 ranks candidates by little-sphere proximity, and the Bekenstein **log Q** law sets the
depth — retrieve the `k* = ω(c_q)` nearest concept-sharing nodes, so capacity is matched to
the query's breadth, not the corpus size (32.1 §6: coarse-graining is a valid monotone
contraction). Against the 40 manuscripts:

| query (breadth) | concepts c_q | depth k* | loaded | top hits |
|---|---|---|---|---|
| quadray / rotation / hodge / curl | 2 (ω=1) | 1 | 2% | `01b` |
| primorial / mertens / RH / zeros | 3·7 (ω=2) | 2 | 5% | `05`, `22` |
| fisher / quantum / gravity / primorial | 3·5·13 (ω=3) | 3 | 8% | `32.1`, `01c`, `15` |

Depth tracks breadth (1→2→3), loading 2–8% of the corpus, all query concepts covered, with
on-target hits (`32.1`'s conductor 3·5·13 exactly matches the third query). This is the UMC
"minimal context, no drift" benefit made quantitative. (Query distributions are kept *sharp*
— a heavy uniform floor would swamp the few query terms and make the ranking noise.)

## Benchmarks — does it actually help? (before / after improvement (a))

The value claim is "an LLM answers correctly with *less* context." Two harnesses test it,
both **representation-agnostic** so they serve before and after the embedding swap (a).

**Deterministic pre-check — `bench_xref.py` (free, no LLM).** Cross-reference recovery:
ground truth = the corpus's own inter-paper links; given a doc, rank the others; gold = the
docs it references (40 docs, 209 gold edges):

| method | MRR | recall@5 | recall@10 | med tok-to-first |
|---|---|---|---|---|
| KG Fisher–Rao (lexical) | 0.687 | 0.454 | 0.655 | 7936 |
| BM25 (lexical) | **0.742** | 0.380 | 0.591 | 11295 |
| **LSA-cosine — (a), laptop** | **0.742** | 0.437 | **0.742** | **7936** |
| random | 0.351 | 0.150 | 0.287 | 14162 |

At the lexical tier KG ≈ BM25 (KG wins recall + efficiency, BM25 edges MRR). **Improvement
(a)** — LSA embeddings (`embed.py`, TF-IDF→SVD, pure numpy, no torch) — matches the best MRR
*and* lifts recall@10 to **0.74** (vs 0.59 / 0.66) at the best token-efficiency: a real
semantic lift even at 40 docs. *KG Fisher–Rao on these embeddings ranks identically to cosine*
(arccos is monotone in cosine), so the KG's residual value over plain cosine-RAG is the
**selection layer** (capacity-matched depth, conductor filter, Janus, gaps) — that's what the
frontier tests. The GCP sentence-embedding tier should widen the lift. Caveat: citation ≠
content-similarity; a ranking pre-check, not the answer verdict.

**The utilitarian frontier — `bench_frontier.py` (LLM-judged).** Answer-quality vs
context-tokens, matched-pair: KG-FisherRao (lexical), **LSA-cosine (improvement (a))**, BM25,
random, full-corpus, plus the **KG-capacity-matched** operating point (LSA ranking + conductor
filter + depth k\*). With `--chunked` a node is a **section** (`chunks.py` → 986 section-nodes),
so capacity-matched loads ~100–500 tokens, not whole papers. QA set: `qa_set.json` (34
hand-authored Q→gold across the corpus). Headline = **tokens@target-accuracy** (left-shift =
win) and **accuracy@tiny-budget**. Run:

```
py bench_frontier.py --dry-run --chunked                       # LLM-free wiring check (verified)
ANTHROPIC_API_KEY=...  py bench_frontier.py --run --chunked    # the verdict
```

`--run` uses the provided Anthropic `answer_fn`/`judge_fn` (or supply your own callables, any
model). Cost: the full sweep is ~1054 (answer,judge) pairs; trim `BUDGETS` or the QA set for a
cheaper first pass. **Falsifiers:** K = KG-capacity-matched left-shifts vs LSA-cosine-top-k
(fewer tokens at equal accuracy); L = indistinguishable → the selection layer is decorative;
ablations decompose the win (embedding metric vs conductor filter vs capacity-matched depth).

**Staged plan:** run both now (bag-of-words) → do (a) → re-run; (a) is justified iff the
edge persists or grows at the embedding tier — and the benchmark doubles as the regression
test that the swap helped.

## What this is a step toward (the remaining improvements)

#1 (Fisher–Rao placement), #3 (conductor addressing + Boolean Janus), and #4
(capacity-matched retrieval) are implemented above, with a unified `kg.csv` export. Still
open: #2 capacity-triggered shell promotion (log Q saturation), #5 a units overflow channel,
#6 order-3 (2-simplex) edges. See
[`../references/umc_program_connections.md`](../references/umc_program_connections.md) §3.
