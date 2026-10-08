"""Generic loop-gas cluster engine for ice on 4-regular lattices (weights w = 3^-|E| 9^n4), clusters of <= 3 polymers."""
import itertools, time, sys, math
from collections import deque, Counter, defaultdict
from fractions import Fraction as Fr

E4 = [tuple(1 if t == j else 0 for t in range(4)) for j in range(4)]
def nbrs_dia(v):
    sg = 1 if sum(v) == 0 else -1
    return [tuple(a + sg * b for a, b in zip(v, e)) for e in E4]
def edge(a, b): return (a, b) if a < b else (b, a)
def verts(es): return frozenset(x for e in es for x in e)

class Lattice:
    def __init__(self, nbrs, allowed=None, girth=6):
        self.nbrs = nbrs; self.allowed = allowed; self.girth = girth; self.cyc_cache = {}; self.poly_cache = {}
    def N(self, v):
        ns = self.nbrs(v)
        return ns if self.allowed is None else [w for w in ns if w in self.allowed]
    def cycles_through(self, root, LM, store=True, counts=None):
        dist = {root: 0}; dq = deque([root])
        while dq:
            v = dq.popleft()
            if dist[v] >= LM // 2 + 1: continue
            for w in self.N(v):
                if w not in dist: dist[w] = dist[v] + 1; dq.append(w)
        out = []
        def dfs(v, path, onpath, depth):
            for w in self.N(v):
                if w == root and depth >= 3:
                    if depth + 1 <= LM and path[1] < path[-1]:
                        if counts is not None: counts[depth + 1] += 1
                        if store:
                            cyc = path + [root]
                            out.append(frozenset(edge(cyc[i], cyc[i + 1]) for i in range(len(cyc) - 1)))
                    continue
                if w in onpath or dist.get(w, 99) > LM - (depth + 1): continue
                onpath.add(w); path.append(w); dfs(w, path, onpath, depth + 1); path.pop(); onpath.remove(w)
        dfs(root, [root], {root}, 0); return out
    def cyc_at(self, v, LM):
        key = (v, LM)
        if key not in self.cyc_cache: self.cyc_cache[key] = self.cycles_through(v, LM)
        return self.cyc_cache[key]
    def polys_at(self, v, LM, cyc_max):
        """all connected even subgraphs through v with <= LM edges, as unions of edge-disjoint cycles of length <= cyc_max"""
        key = (v, LM, cyc_max)
        if key in self.poly_cache: return self.poly_cache[key]
        start = [c for c in self.cyc_at(v, min(LM, cyc_max))]
        found = set(start); frontier = list(start)
        while frontier:
            nxt = []
            for P in frontier:
                room = LM - len(P)
                if room < self.girth: continue
                for u in verts(P):
                    for c in self.cyc_at(u, min(room, cyc_max)):
                        if c & P: continue
                        U = P | c
                        if U not in found: found.add(U); nxt.append(U)
            frontier = nxt
        res = list(found); self.poly_cache[key] = res; return res

def weight(P):
    deg = Counter(x for e in P for x in e); n4 = sum(1 for d in deg.values() if d == 4)
    return Fr(9) ** n4 / Fr(3) ** len(P)

def cluster_series(lat, roots, K, cyc_store_max, count_only_from=None, rootweight=None):
    """sum over clusters (n<=3) of ordered tuples with first polymer through a root, weight distributed 1/|V(p1)|
       (per-vertex density if roots = [one representative of each vertex class]); returns Counter by order."""
    out = Counter()
    for root, rw in roots:
        P1 = lat.polys_at(root, K, cyc_store_max)
        near_cache = {}
        def near(P, LM):          # polymers incompatible with P (sharing a vertex) of size <= LM
            key = (P, LM)
            if key not in near_cache:
                s = set()
                for u in verts(P): s.update(lat.polys_at(u, LM, cyc_store_max))
                near_cache[key] = s
            return near_cache[key]
        for p in P1:
            wp = weight(p); Vp = len(verts(p)); base = rw * wp / Vp
            out[len(p)] += base                                            # n = 1
            room = K - len(p)
            g = lat.girth
            if room < g: continue
            Np = near(p, room)
            for q in Np:                                                   # n = 2: phi = -1, factor 1/2
                out[len(p) + len(q)] += base * Fr(-1, 2) * weight(q)
            if room < 2 * g: continue
            # n = 3: ordered (q, r); phi = 1 (path) or 2 (triangle); factor 1/6
            cand = set(Np)
            for q in Np:
                if K - len(p) - len(q) >= g: cand |= near(q, K - len(p) - len(q))
            cand = [c for c in cand if len(c) <= room - g]
            Vp_set = verts(p)
            for q in cand:
                for r in cand:
                    if len(p) + len(q) + len(r) > K: continue
                    a = bool(Vp_set & verts(q)); b = bool(Vp_set & verts(r)); c_ = bool(verts(q) & verts(r))
                    ne = a + b + c_
                    if ne < 2: continue
                    phi = 2 if ne == 3 else 1
                    out[len(p) + len(q) + len(r)] += base * Fr(phi, 6) * weight(q) * weight(r)
    return out
