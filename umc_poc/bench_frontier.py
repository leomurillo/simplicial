"""
bench_frontier.py — (b) the LLM answer-quality-vs-context-budget harness (scaffold).

THE utilitarian benchmark: does the KG let an LLM answer correctly with fewer tokens?
Representation-agnostic and model-agnostic by design, so it serves before AND after
improvement (a): swap the node representation, re-run, read the lift.

What is fully implemented here (LLM-free):
  - the retrieval methods + budget truncation (KG Fisher-Rao, KG capacity-matched,
    BM25, random, full-corpus) — and a registration point for cosine-embeddings (post-(a));
  - the budget sweep, the per-(method,budget) context assembly, and the metric aggregation
    (accuracy@budget curve; tokens@target; the capacity-matched operating point);
  - a --dry-run that exercises retrieval and prints the plan + a sample context, with ZERO
    LLM calls, so you can see the wiring before spending tokens.

What YOU plug in (two callables + a QA set):
  - answer_fn(query, context) -> str
  - judge_fn(query, gold_answer, prediction) -> float in [0,1]
  - QA set: JSON list of {"id","query","gold_doc_ids","gold_answer"} (see qa_example.json).
  An Anthropic implementation is provided, gated on ANTHROPIC_API_KEY + the SDK; supply your
  own callables to use any model. The harness never hard-codes a provider.

Run:  py bench_frontier.py --dry-run
      py bench_frontier.py --run --qa qa_example.json            # needs answer/judge wired
"""
import os, sys, json, argparse
import numpy as np
import fisher_kg as fk
import conductor_kg as ck
import embed
import chunks as chunkmod
from poc import load_corpus, build_distributions, TOKEN, STOP

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BUDGETS = [500, 1000, 2000, 4000, 8000, 16000]     # context budgets (token proxy = whitespace words)
CM_CAP = 1200                                       # capacity-matched per-query token cap (see GRANULARITY note)

# GRANULARITY note: this scaffold indexes WHOLE manuscripts. A manuscript is ~10-30k tokens,
# so "load k* whole docs" is not token-minimal. For a real deployment, index at PASSAGE/SECTION
# granularity (one node per section); then capacity-matched depth genuinely yields minimal
# context. The cores (fisher_kg, conductor_kg) are unchanged -- only the node = section, not file.
# Until then we cap the capacity-matched point at CM_CAP tokens to keep the comparison fair.

def count_tokens(s):
    return len(s.split())

# ---------------- corpus + lexical/geometry indices ----------------

class Index:
    def __init__(self, units=None):
        # units: list of (unit_id, text, doc_id). Default = whole manuscripts.
        if units is None:
            ids, stems, fams, texts = load_corpus()
            units = [(ids[i], texts[i], ids[i]) for i in range(len(ids))]
        self.ids = [u[0] for u in units]
        self.texts = [u[1] for u in units]
        self.doc_of = [u[2] for u in units]
        texts = self.texts
        self.P, self.vocab = build_distributions(texts, vocab_size=1200)
        self.vidx = {w: i for i, w in enumerate(self.vocab)}
        self.n = len(self.ids)
        self.C = np.zeros((self.n, len(self.vocab)))
        toks_per = []
        for i, t in enumerate(texts):
            ts = [w for w in TOKEN.findall(t.lower()) if w not in STOP]
            toks_per.append(ts)
            for w in ts:
                j = self.vidx.get(w)
                if j is not None:
                    self.C[i, j] += 1
        self.dl = self.C.sum(1)
        _M = ck.topic_masses(toks_per)
        self.cond = [int(c) for c in ck.conductors(_M)[0]]
        self.topic_median = np.median(_M, axis=0)         # cached conductor threshold
        self.doc_tokens = np.array([count_tokens(t) for t in texts])
        self.lsa = embed.build_lsa(self.C, dim=48)        # improvement (a), laptop tier

    def _qcounts(self, query):
        v = np.zeros(len(self.vocab))
        for w in TOKEN.findall(query.lower()):
            j = self.vidx.get(w)
            if j is not None:
                v[j] += 1.0
        return v

    def rank_lsa(self, query):
        """Improvement (a): rank by LSA-embedding cosine (= KG Fisher-Rao on embeddings)."""
        qe = embed.encode_query(self._qcounts(query), self.lsa)
        return list(np.argsort(embed.cosine_to(qe, self.lsa["doc_emb"]))[::-1])

    def _qdist(self, query):
        v = np.full(len(self.vocab), 1e-9)
        for w in TOKEN.findall(query.lower()):
            j = self.vidx.get(w)
            if j is not None:
                v[j] += 1.0
        return v / v.sum()

    def rank_kg(self, query):
        bc = np.clip(np.sqrt(self.P) @ np.sqrt(self._qdist(query)), 0, 1)
        return list(np.argsort(2 * np.arccos(bc)))

    def rank_bm25(self, query, k1=1.5, b=0.75):
        df = (self.C > 0).sum(0); idf = np.log((self.n - df + 0.5) / (df + 0.5) + 1.0)
        avgdl = self.dl.mean(); s = np.zeros(self.n)
        for w in TOKEN.findall(query.lower()):
            j = self.vidx.get(w)
            if j is not None:
                tf = self.C[:, j]
                s += idf[j] * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * self.dl / avgdl))
        return list(np.argsort(s)[::-1])

    def rank_random(self, query, seed=0):
        o = list(range(self.n)); np.random.default_rng(seed).shuffle(o); return o

    # registration point for improvement (a): set self.embeddings (n, d) then use this.
    def rank_cosine(self, query, query_vec=None):
        if not hasattr(self, "embeddings"):
            raise NotImplementedError("set Index.embeddings + a query encoder after improvement (a)")
        q = query_vec
        sims = self.embeddings @ q / (np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(q) + 1e-9)
        return list(np.argsort(sims)[::-1])

    def capacity_matched(self, query, max_nodes=8):
        # KG operating point (pilot-tuned): embedding-only ranking -- the conductor is reserved
        # for NAVIGATION (complement/gaps), not used as a retrieval filter (it steered to sibling
        # concepts) -- with breadth-adaptive depth k* = max(3, omega(c_q)) (a floor, not a single
        # chunk). Capped by CM_CAP tokens at assembly time.
        ranked = self.rank_lsa(query)
        k = min(max(3, ck.omega(self._cond_of(query))), max_nodes)
        return ranked[:k]

    def _cond_of(self, query):
        toks = [w for w in TOKEN.findall(query.lower()) if w not in STOP]
        m = ck.topic_masses([toks])[0]
        c = 1
        for j, p in enumerate(ck.PRIMES):
            if m[j] > self.topic_median[j]:
                c *= p
        return c

    def context_by_budget(self, ranked, budget):
        out, used = [], 0
        for i in ranked:
            tk = int(self.doc_tokens[i])
            if used + tk > budget and out:
                break
            out.append(i); used += min(tk, budget)
            if used >= budget:
                break
        return out

    def assemble(self, idxs, budget=None):
        parts, used = [], 0
        for i in idxs:
            t = self.texts[i]
            if budget is not None:
                room = budget - used
                t = " ".join(t.split()[:max(0, room)])
            parts.append(f"[{self.ids[i]}]\n{t}")
            used += count_tokens(t)
        return "\n\n".join(parts), used

# ---------------- methods (swept by budget, except the capacity-matched point) ----------------

SWEPT = {
    "KG-FisherRao": lambda ix, q: ix.rank_kg(q),         # lexical (bag-of-words)
    "LSA-cosine":   lambda ix, q: ix.rank_lsa(q),        # improvement (a), laptop tier
    "BM25":         lambda ix, q: ix.rank_bm25(q),
    "random":       lambda ix, q: ix.rank_random(q),
    "full-corpus":  lambda ix, q: list(range(ix.n)),
}

# ---------------- LLM hooks (plug in your model) ----------------

def anthropic_answer(query, context, model="claude-opus-4-8"):
    import anthropic
    c = anthropic.Anthropic()
    msg = c.messages.create(model=model, max_tokens=512, messages=[{"role": "user",
        "content": f"Answer ONLY from the context. If absent, say 'not in context'.\n\n"
                   f"CONTEXT:\n{context}\n\nQUESTION: {query}"}])
    return msg.content[0].text

def anthropic_judge(query, gold, pred, model="claude-opus-4-8"):
    import anthropic
    c = anthropic.Anthropic()
    msg = c.messages.create(model=model, max_tokens=8, messages=[{"role": "user",
        "content": f"Q: {query}\nGOLD: {gold}\nANSWER: {pred}\n"
                   f"Is ANSWER correct vs GOLD? Reply 1 for yes, 0 for no."}])
    return 1.0 if "1" in msg.content[0].text else 0.0

# ---------------- runner ----------------

def run_frontier(ix, qa, answer_fn, judge_fn, budgets=BUDGETS):
    results = {}                                   # method -> {budget: [scores]}
    for q in qa:
        for name, ranker in SWEPT.items():
            ranked = ranker(ix, q["query"])
            for B in budgets:
                ctx, _ = ix.assemble(ix.context_by_budget(ranked, B), budget=B)
                score = judge_fn(q["query"], q.get("gold_answer", ""), answer_fn(q["query"], ctx))
                results.setdefault(name, {}).setdefault(B, []).append(score)
        # capacity-matched operating point
        cm = ix.capacity_matched(q["query"])
        ctx, used = ix.assemble(cm, budget=CM_CAP)
        score = judge_fn(q["query"], q.get("gold_answer", ""), answer_fn(q["query"], ctx))
        results.setdefault("KG-capacity-matched", {}).setdefault("pt", []).append((used, score))
    return results

def dry_run(ix, qa, budgets=BUDGETS):
    print(f"corpus: {ix.n} docs; QA queries: {len(qa)}; budgets: {budgets}")
    n_calls = len(qa) * (len(SWEPT) * len(budgets) + 1)
    print(f"planned LLM (answer,judge) pairs for a full run: {n_calls}")
    q = qa[0]["query"]
    print(f"\nsample query: \"{q}\"")
    for name, ranker in SWEPT.items():
        ranked = ranker(ix, q)
        sel = ix.context_by_budget(ranked, 2000)
        print(f"  {name:>14}  @2000tok -> {[ix.ids[i] for i in sel]}")
    cm = ix.capacity_matched(q)
    _, used = ix.assemble(cm, budget=CM_CAP)
    sel_show = [f"{ix.ids[i]}({ix.doc_of[i]})" for i in cm]
    print(f"  {'KG-cap-matched':>14}  point   -> {sel_show}  (~{used} tok)")
    print("\nretrieval wired OK. Plug answer_fn/judge_fn + a QA set, then --run.")

def export_cases(ix, qa, methods, budgets, path):
    """Write (query, retrieved context, gold) cases to JSON -- no LLM. For external or
    in-session answer+judge. Swept methods at each budget + the capacity-matched point."""
    cases = []
    for q in qa:
        for name, ranker in methods.items():
            ranked = ranker(ix, q["query"])
            for B in budgets:
                sel = ix.context_by_budget(ranked, B)
                ctx, used = ix.assemble(sel, budget=B)
                cases.append({"q_id": q.get("id"), "query": q["query"], "gold": q.get("gold_answer", ""),
                              "gold_docs": q.get("gold_doc_ids", []), "method": name, "budget": B,
                              "tokens": used, "retrieved": [ix.ids[i] for i in sel], "context": ctx})
        cm = ix.capacity_matched(q["query"]); ctx, used = ix.assemble(cm, budget=CM_CAP)
        cases.append({"q_id": q.get("id"), "query": q["query"], "gold": q.get("gold_answer", ""),
                      "gold_docs": q.get("gold_doc_ids", []), "method": "KG-capacity-matched", "budget": "pt",
                      "tokens": used, "retrieved": [ix.ids[i] for i in cm], "context": ctx})
    json.dump(cases, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"exported {len(cases)} cases -> {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--export", default=None, help="write retrieval cases (query+context+gold) to JSON; no LLM")
    ap.add_argument("--qa", default="qa_set.json")
    ap.add_argument("--qa-ids", default=None, help="comma-separated subset of QA ids")
    ap.add_argument("--max-qa", type=int, default=None)
    ap.add_argument("--budgets", default=None, help="comma-separated token budgets (override sweep)")
    ap.add_argument("--methods", default=None, help="comma-separated subset of swept methods")
    ap.add_argument("--chunked", action="store_true", help="index by section (token-minimal); recommended")
    args = ap.parse_args()
    units = chunkmod.load_chunks() if args.chunked else None
    ix = Index(units)
    print(f"index: {ix.n} {'section-chunks' if args.chunked else 'whole-doc'} nodes")
    qa = json.load(open(args.qa, encoding="utf-8")) if os.path.exists(args.qa) else \
        [{"id": "q0", "query": "what is the intrinsic cross product on quadray coordinates",
          "gold_doc_ids": ["01"], "gold_answer": "the operator K(u)"}]
    if args.qa_ids:
        keep = set(args.qa_ids.split(",")); qa = [q for q in qa if q.get("id") in keep]
    if args.max_qa:
        qa = qa[:args.max_qa]
    budgets = [int(x) for x in args.budgets.split(",")] if args.budgets else BUDGETS
    methods = {k: SWEPT[k] for k in args.methods.split(",")} if args.methods else SWEPT
    if args.export:
        export_cases(ix, qa, methods, budgets, args.export); return
    if args.run:
        if "ANTHROPIC_API_KEY" not in os.environ:
            print("set ANTHROPIC_API_KEY (or pass your own answer_fn/judge_fn) to --run"); return
        res = run_frontier(ix, qa, anthropic_answer, anthropic_judge)
        print("\nfrontier (accuracy@budget):")
        for name, by_b in res.items():
            if name == "KG-capacity-matched":
                pts = by_b["pt"]; tok = np.mean([t for t, _ in pts]); acc = np.mean([s for _, s in pts])
                print(f"  {name:>20}: point  ~{tok:.0f} tok  acc {acc:.2f}")
            else:
                row = "  ".join(f"{B}:{np.mean(by_b[B]):.2f}" for B in BUDGETS)
                print(f"  {name:>20}: {row}")
    else:
        dry_run(ix, qa)

if __name__ == "__main__":
    main()
