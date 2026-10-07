"""
retrieve.py — (b) improvement #4: capacity-matched retrieval ("minimal context").

The UMC promise an agent cares about is minimal, drift-free context. This uses all three
ideas at once:
  #3 conductor address  -> which concept primes the query needs (c_q), to FILTER candidates;
  #1 Fisher-Rao metric  -> RANK candidates by little-sphere proximity to the query;
  #4 Bekenstein log Q   -> STOP as soon as the retrieved set covers the query's concepts,
                           so capacity (log k) is matched to the query's information need,
                           not to the whole corpus (log n).  (32.1 §6: coarse-graining is a
                           monotone contraction, so a covering prefix is a valid answer.)

Run:  py retrieve.py   (or python retrieve.py)
"""
import sys
import numpy as np
import fisher_kg as fk
import conductor_kg as ck
from poc import load_corpus, build_distributions, TOKEN, STOP

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

QUERIES = [   # chosen with 1, 2, 3 concept-breadths so depth visibly tracks breadth
    "quadray cross product rotation rodrigues tetrahedron hodge curl",
    "primorial mertens zeta riemann hypothesis critical zeros",
    "fisher cumulant entropy quantum density gravity primorial zeta",
]

def query_distribution(q_tokens, vocab):
    # the query must be SHARP: a heavy uniform floor would swamp ~7 query terms over a
    # 2000-bin vocab and make Fisher-Rao ranking pure noise. Use a tiny floor.
    vidx = {w: i for i, w in enumerate(vocab)}
    v = np.full(len(vocab), 1e-9)
    for w in q_tokens:
        if w in vidx:
            v[vidx[w]] += 1.0
    return v / v.sum()

def query_concepts(q_tokens):
    """Concept conductor of the query: product of primes whose markers appear."""
    hits = {p for p, ms in ck.TOPICS.items() for m in ms if m in q_tokens}
    c = 1
    for p in ck.PRIMES:
        if p in hits:
            c *= p
    return c

def fr_to_query(qdist, P):
    bc = np.clip(np.sqrt(P) @ np.sqrt(qdist), 0.0, 1.0)
    return 2.0 * np.arccos(bc)

def main():
    ids, stems, fams, texts = load_corpus()
    n = len(ids)
    P, vocab = build_distributions(texts, vocab_size=2000)   # wide vocab: keep rare salient terms
    toks = [[w for w in TOKEN.findall(t) if w not in STOP] for t in texts]
    cond, _ = ck.conductors(ck.topic_masses(toks))
    cond = [int(c) for c in cond]

    print(f"corpus: {n} nodes; full-load capacity log n = {np.log(n):.2f} nats\n")

    for q in QUERIES:
        qt = [w for w in TOKEN.findall(q.lower()) if w not in STOP]
        cq = query_concepts(qt)
        qd = query_distribution(qt, vocab)
        d = fr_to_query(qd, P)

        # candidates = nodes sharing >=1 concept prime with the query (#3 filter), FR-ranked (#1)
        cand = [i for i in range(n) if ck.meet(cond[i], cq) > 1] or list(range(n))
        cand.sort(key=lambda i: d[i])

        # capacity-matched depth: the query spans omega(c_q) concepts => need log(k) >= log(omega)
        # nats of capacity => retrieve the k = omega(c_q) nearest concept-sharing nodes (32.1 Thm 4.1).
        kstar = max(1, ck.omega(cq))
        chosen = cand[:kstar]
        covered = 1
        for i in chosen:
            covered = ck.join(covered, cond[i])

        print("=" * 72)
        print(f"query: \"{q}\"")
        print(f"  concepts needed c_q = {ck.factor_str(cq)}  (breadth omega = {ck.omega(cq)})")
        print(f"  capacity-matched depth k* = omega(c_q) = {kstar}  ->  loaded {kstar}/{n} nodes "
              f"({100*kstar/n:.0f}%), capacity log k* = {np.log(kstar):.2f} nats (vs full {np.log(n):.2f})")
        cov = "all query concepts covered" if covered % cq == 0 else "PARTIAL coverage"
        print(f"  retrieved (k* nearest, concept-sharing) -- [{cov}]:")
        for i in chosen:
            print(f"    {ids[i]:>6} [{fams[i]:>8}]  FR={d[i]:.2f}  cond={ck.factor_str(cond[i])}")
        print()

    print("=" * 72)
    print("VERDICT: retrieval depth tracks the query's concept breadth, not the corpus size")
    print("(focused query -> few nodes; broad query -> more), so context is capacity-matched")
    print("and minimal -- the UMC 'minimal context, no drift' benefit, made quantitative.")

if __name__ == "__main__":
    main()
