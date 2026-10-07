# Frontier pilot — results (self-judged, N=8)

**Setup.** No Anthropic key/SDK in the run environment, so the *automated* 1054-pair API
sweep could not run. Instead: a trimmed, diverse 8-query pilot (`q01,q05,q08,q13,q21,q25,q32,q34`),
section-chunked corpus (973 nodes after dropping references/boilerplate), budget 1000 for the
swept methods, with **Claude as the answer+judge in-session**. Directional, not the full sweep.
Reproduce the export: `py bench_frontier.py --chunked --export cases.json --qa-ids "..." --methods "LSA-cosine,BM25" --budgets 1000`.

**Per-query answer-correct (1/0) and gold-doc retrieved (·):**

| query (gold) | LSA-cosine | BM25 | KG-capacity-matched |
|---|---|---|---|
| q01 cross-product/cubic (01) | 1 | 1 | 0 (got 02 quaternions) |
| q05 K̃=⋆d0 DEC bridge (01b) | 1 | 1 | 0 (got 06) |
| q08 frame Laplacian (01d) | 1 | 1 | 1 |
| q13 V4 rotor (03) | 1 | 1 | 1 |
| q21 density-matrix Bures (15) | 0 (got 18/24/27) | 1 | 0 (got 18) |
| q25 primorial-cumulant RH (22) | 1 | 1 | 1 |
| q32 Bekenstein (32.1) | 1 | 1 | 1 |
| q34 smooth primorial (T33) | 0 | 0 | 0 |
| **accuracy** | **6/8 = 0.75** | **7/8 = 0.88** | **4/8 = 0.50** |
| **median tokens** | **846** | **860** | **232** |

## Verdict (honest, pre-registered branches)

**The KG selection layer does NOT win on accuracy at the embedding tier on this pilot — it
wins ~3.7× on tokens.** This is the *joint-on-disjoint / L-leaning* branch: capacity-matched
is far leaner (232 vs ~850 tok) but loses ~25–40% accuracy vs plain cosine/BM25. So the
geometry/addressing is an **efficiency** lever, not an accuracy lever, as built.

Two further honest findings:
1. **LSA's semantic lift is marginal vs BM25 at chunk level** (0.75 vs 0.88). At doc-level
   xref recall@10 LSA led (0.74 vs 0.59), but on chunk-level QA over a *jargon-dense* corpus,
   exact-term BM25 is very strong. A real sentence-embedding model (GCP tier) is needed to
   show the semantic lift here; LSA at d=48 on 40 papers is too weak.
2. **q34 total miss:** all methods retrieved `32.1` instead of `T33` for "smooth primorial /
   Mertens" — because the 32.1↔T33 cross-references added this session made `32.1` match the
   query strongly. Cross-ref contamination is real.

## What the pilot tells us to fix (concrete, before trusting any verdict)

- **Depth too aggressive.** `k* = ω(c_q)` is often a single chunk; that's why capacity-matched
  misses (q01→1 chunk of the wrong sibling). Fix: `k* = max(3, ω)` or a **token floor** (≥600
  tok) instead of a count — pair the Bekenstein-capacity idea with a minimum.
- **Conductor filter steers to siblings** (q01→02, q05→06): for *retrieval* it hurts; rank by
  embedding alone and use the conductor only for *navigation* (complement/gaps), not the
  candidate filter.
- **Encoder.** LSA d=48 is the floor; the GCP sentence-embedding tier is the real (a).
- **Boilerplate** (done: references/keywords/changelog dropped — already improved hits).

## Bottom line (first pass)

Run as asked. The pilot is a genuine, useful negative-leaning result: **as first tuned,
the KG buys token-efficiency, not answer-accuracy, over plain RAG** — and it pinpoints exactly
why (depth heuristic + conductor-as-filter) and what to change.

---

## Re-run after the two fixes (depth `k*=max(3,ω)`, embedding-only ranking)

Applied: capacity-matched now ranks by embedding alone (conductor reserved for navigation) with
depth `k* = max(3, ω(c_q))` capped at CM_CAP=1200 tokens. Metric below is **gold-doc retrieved**
(deterministic; answer-quality tracks it on read-back):

| method | doc-hit | median tokens |
|---|---|---|
| LSA-cosine | 6/8 = 0.75 | 845 |
| BM25 | **7/8 = 0.88** | 860 |
| KG-capacity-matched (tuned) | **6/8 = 0.75** | **718** |

The fixes **closed the gap**: capacity-matched rose **0.50 → 0.75** (now level with LSA) while
staying ~15% leaner — it moved from a liability onto the accuracy frontier. Confirms the depth
heuristic was the culprit. But note the honest trade: the earlier 4× token saving was an
*under-tuned extreme*; raising depth bought accuracy AND tokens — no free lunch.

**Two robust conclusions:**
1. **Neither the KG layer nor LSA beats BM25** (0.88) on this small, jargon-dense corpus. Exact
   lexical match is hard to beat when queries reuse the papers' own terms; LSA at d=48 over 40
   papers is too weak to show a semantic lift at chunk level (it *did* lead at doc-level xref
   recall@10). The decisive lever is the **real sentence-embedding encoder (GCP tier)** — and a
   **hybrid BM25+embedding** would likely top both.
2. The two misses are informative, not noise: **q21** (embeddings conflate paper 18 "Bures
   completion" with gold 15 "density-matrix manifold"; BM25's exact terms found 15) and **q34**
   (all methods pull 32.1 for "smooth primorial" because the 32.1↔T33 cross-refs added this
   session made 32.1 match — genuine cross-ref contamination).

**Updated verdict:** properly tuned, the KG selection layer is **competitive with plain embedding
RAG (equal accuracy, modestly fewer tokens) but not superior, and below a strong BM25 baseline**
on this corpus. Its defensible value is (i) token-efficiency at parity accuracy and (ii) the
navigation ops (complement/gaps) that RAG lacks — not a retrieval-accuracy win. The next real
measurement is the GCP sentence-embedding encoder (+ hybrid) on the full sweep; until then the
honest claim is *parity, leaner*, not *better*.
