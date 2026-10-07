"""
kg_store.py — a persistent, usable Knowledge Graph with UMC-native operations.

This is the POC turned into a tool an agent can call. A node is a document; it lives on
the K=1/4 little sphere (Fisher-Rao metric, Paper 32.1), is placed at an ABCD/IVM lattice
point, and carries a conductor address (Boolean lattice, exact Janus complement). The
operation set is the CRUD analog of Fuller's RECEIVE/STORE/RETRIEVE/CONSTELLATE plus the
geometry-native ops (complement, meet/join, gaps) and the agentic op (context).

Persistent JSON store; pure numpy; no torch.  See kg.py for the CLI.
"""
import json, math
from pathlib import Path
import numpy as np
import fisher_kg as fk
import conductor_kg as ck
from poc import TOKEN, STOP

def _tok(text):
    return [w for w in TOKEN.findall(text.lower()) if w not in STOP]

class KnowledgeGraph:
    def __init__(self, store="kg_store.json"):
        self.store = Path(store)
        self.vocab = []; self.vidx = {}
        self.thresh = None                 # per-topic conductor thresholds (stable under add)
        self.nodes = []                    # list of dicts: id, source, snippet, counts{idx:ct}, coords, abcd, conductor
        self.P = None                      # (n, V) distributions, in memory
        if self.store.exists():
            self.load()

    # ---------- internal ----------
    def _matrix(self, smooth=0.5):
        V = len(self.vocab)
        P = np.full((len(self.nodes), V), smooth)
        for i, nd in enumerate(self.nodes):
            for j, c in nd["counts"].items():
                P[i, int(j)] += c
        return P / P.sum(axis=1, keepdims=True)

    def _dist_of(self, tokens, sharp=False):
        V = len(self.vocab)
        v = np.full(V, 1e-9 if sharp else 0.5)
        for w in tokens:
            j = self.vidx.get(w)
            if j is not None:
                v[j] += 1.0
        return v / v.sum()

    def _conductor_of(self, tokens):
        m = ck.topic_masses([tokens])[0]
        c = 1
        for j, p in enumerate(ck.PRIMES):
            if m[j] > self.thresh[j]:
                c *= p
        return c

    def _relayout(self):
        """CONSTELLATE: recompute the full Fisher-Rao placement (call after a batch build)."""
        self.P = self._matrix()
        D = fk.fisher_rao_matrix(self.P)
        coords, _ = fk.classical_mds(D, 3)
        freq = 10.0 / max(np.abs(coords).max(), 1e-9)
        L = fk.snap_to_lattice(fk.xyz_to_quadray(coords), freq)
        L[:, 3] = -(L[:, :3].sum(axis=1))
        for i, nd in enumerate(self.nodes):
            nd["coords"] = [round(float(x), 4) for x in coords[i]]
            nd["abcd"] = [int(x) for x in L[i]]

    # ---------- CREATE / STORE ----------
    def build(self, docs, vocab_size=1200):
        """docs: iterable of (id, text, source). Builds vocab, distributions, layout, addresses."""
        docs = list(docs)
        toklists = [_tok(t) for _, t, _ in docs]
        glob = {}
        for ts in toklists:
            for w in ts:
                glob[w] = glob.get(w, 0) + 1
        self.vocab = [w for w, _ in sorted(glob.items(), key=lambda kv: -kv[1])[:vocab_size]]
        self.vidx = {w: i for i, w in enumerate(self.vocab)}
        M = ck.topic_masses(toklists)
        self.thresh = [float(np.median(M[:, j])) for j in range(len(ck.PRIMES))]
        self.nodes = []
        for (nid, text, src), ts in zip(docs, toklists):
            counts = {}
            for w in ts:
                j = self.vidx.get(w)
                if j is not None:
                    counts[str(j)] = counts.get(str(j), 0) + 1
            self.nodes.append({"id": nid, "source": src, "snippet": text.strip()[:400].replace("\n", " "),
                               "counts": counts, "conductor": self._conductor_of(ts)})
        self._relayout()
        self.save()
        return self

    def add(self, nid, text, source=""):
        """RECEIVE: incremental insert (approximate placement; call rebuild() to re-constellate)."""
        ts = _tok(text)
        counts = {}
        for w in ts:
            j = self.vidx.get(w)
            if j is not None:
                counts[str(j)] = counts.get(str(j), 0) + 1
        nd = {"id": nid, "source": source, "snippet": text.strip()[:400].replace("\n", " "),
              "counts": counts, "conductor": self._conductor_of(ts)}
        # approximate placement: centroid of 3 Fisher-Rao nearest existing nodes, snapped
        self.P = self._matrix()
        d = self._dist_of(ts)
        bc = np.clip(np.sqrt(self.P) @ np.sqrt(d), 0, 1)
        near = np.argsort(2 * np.arccos(bc))[:3]
        coords = np.mean([self.nodes[i]["coords"] for i in near], axis=0)
        q = fk.xyz_to_quadray(coords.reshape(1, 3))
        L = fk.snap_to_lattice(q, 10.0)[0]; L[3] = -(L[:3].sum())
        nd["coords"] = [round(float(x), 4) for x in coords]; nd["abcd"] = [int(x) for x in L]
        self.nodes.append(nd); self.save()
        return nd

    def update(self, nid, text):
        self.delete(nid, save=False); return self.add(nid, text)

    def delete(self, nid, save=True):
        self.nodes = [n for n in self.nodes if n["id"] != nid]
        if save:
            self.save()

    def rebuild(self):
        """Re-CONSTELLATE the whole graph exactly (use after several add/update/delete)."""
        self._relayout(); self.save()

    # ---------- READ / RETRIEVE ----------
    def _byid(self, nid):
        for n in self.nodes:
            if n["id"] == nid:
                return n
        return None

    def get(self, nid):
        return self._byid(nid)

    def distance(self, a, b):
        self.P = self._matrix(); ids = [n["id"] for n in self.nodes]
        return float(fk.fisher_rao_matrix(self.P)[ids.index(a), ids.index(b)])

    def neighbors(self, nid, k=5):
        self.P = self._matrix(); ids = [n["id"] for n in self.nodes]
        i = ids.index(nid)
        D = fk.fisher_rao_matrix(self.P)[i]
        order = np.argsort(D)
        return [(ids[j], round(float(D[j]), 3)) for j in order if j != i][:k]

    def context(self, query, max_nodes=8):
        """The agentic op: minimal capacity-matched context for a query (improvement #4)."""
        self.P = self._matrix(); ids = [n["id"] for n in self.nodes]
        qt = _tok(query); cq = self._conductor_of(qt)
        d = self._dist_of(qt, sharp=True)
        bc = np.clip(np.sqrt(self.P) @ np.sqrt(d), 0, 1)
        fr = 2 * np.arccos(bc)
        cand = [i for i in range(len(ids)) if ck.meet(self.nodes[i]["conductor"], cq) > 1] or list(range(len(ids)))
        cand.sort(key=lambda i: fr[i])
        k = min(max(1, ck.omega(cq)), max_nodes)
        chosen = cand[:k]
        return {"query": query, "concepts": ck.factor_str(cq), "depth": k,
                "loaded_frac": round(k / len(ids), 3),
                "hits": [{"id": ids[i], "fr": round(float(fr[i]), 3),
                          "conductor": ck.factor_str(self.nodes[i]["conductor"]),
                          "snippet": self.nodes[i]["snippet"][:160]} for i in chosen]}

    # ---------- geometry-native ops ----------
    def complement(self, nid):
        """Exact Boolean Janus opposite: N/c, with occupants or 'vacant gap'."""
        nd = self._byid(nid); c = nd["conductor"]; comp = ck.complement(c)
        occ = [n["id"] for n in self.nodes if n["conductor"] == comp]
        return {"node": nid, "conductor": ck.factor_str(c), "complement": ck.factor_str(comp),
                "occupants": occ or None}

    def meet(self, a, b):
        return ck.factor_str(ck.meet(self._byid(a)["conductor"], self._byid(b)["conductor"]))

    def join(self, a, b):
        return ck.factor_str(ck.join(self._byid(a)["conductor"], self._byid(b)["conductor"]))

    def gaps(self):
        """Vacant conductor addresses (unfilled concept-combinations) — discovery op."""
        used = {n["conductor"] for n in self.nodes}
        allc = []
        for mask in range(1, 1 << len(ck.PRIMES)):
            c = 1
            for j, p in enumerate(ck.PRIMES):
                if mask & (1 << j):
                    c *= p
            allc.append(c)
        vac = sorted(c for c in allc if c not in used)
        return [ck.factor_str(c) for c in vac]

    def shells(self):
        """Bekenstein capacity per rank-shell: Q nodes -> log Q nats."""
        sh = {}
        for n in self.nodes:
            r = ck.omega(n["conductor"]); sh[r] = sh.get(r, 0) + 1
        return {r: {"Q": q, "capacity_logQ": round(fk.bekenstein_capacity(q), 3)} for r, q in sorted(sh.items())}

    # ---------- persistence ----------
    def save(self):
        self.store.write_text(json.dumps(
            {"vocab": self.vocab, "thresh": self.thresh, "nodes": self.nodes}, ensure_ascii=False), encoding="utf-8")

    def load(self):
        d = json.loads(self.store.read_text(encoding="utf-8"))
        self.vocab = d["vocab"]; self.vidx = {w: i for i, w in enumerate(self.vocab)}
        self.thresh = d["thresh"]; self.nodes = d["nodes"]
        return self

def build_from_repo(store="kg_store.json", vocab_size=1200):
    from poc import load_corpus, ROOT
    ids, stems, fams, texts = load_corpus()
    docs = [(ids[i], texts[i], str((ROOT / (stems[i] + ".md")))) for i in range(len(ids))]
    return KnowledgeGraph(store).build(docs, vocab_size=vocab_size)
