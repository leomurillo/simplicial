"""
Yukawa graph test.  Vertices = 5 SM sectors. Edges = gauge-invariant
trilinear  psi_i psi_j Phi^(+/-),  Phi = V = (2,1)_{+1/2}.

We (1) enumerate ALL gauge-invariant trilinears with one Higgs insertion
(confirm exactly 3 edges, no missing/extra), (2) test bipartiteness,
(3) determine whether the chiral 2-coloring is FORCED by the graph or
requires extra cross-component alignment input.
"""
import itertools, numpy as np

# rep encoding: SU(3) Dynkin (p,q); SU(2) isospin 2j (0 -> singlet, 1 -> doublet); Y
SECT = {
 'Q'  : ((1,0), 1, +1/6),   # (2,3)_{1/6}
 'uc' : ((0,1), 0, -2/3),   # (1,3bar)_{-2/3}
 'dc' : ((0,1), 0, +1/3),   # (1,3bar)_{1/3}
 'L'  : ((0,0), 1, -1/2),   # (2,1)_{-1/2}
 'ec' : ((0,0), 0, +1.0),   # (1,1)_{1}
}
PHI  = {'V': ((0,0), 1, +1/2), 'Vstar': ((0,0), 1, -1/2)}

def su3_has_singlet(reps):
    # product of (p,q) irreps contains (0,0)?  Use triality + a small
    # decomposition for the only reps we ever see: 1,3,3bar.
    # triality t = (p - q) mod 3 ; necessary: sum t == 0 mod 3.
    t = sum((p-q) for (p,q) in reps) % 3
    if t != 0:
        return False
    # sufficient check for our alphabet {(0,0),(1,0),(0,1)}:
    # singlet appears iff multiset is all-(0,0), or contains a 3 and a 3bar
    # with everything else (0,0), or three 3's / three 3bar's.
    from collections import Counter
    c = Counter(reps)
    nonsing = [r for r in reps if r != (0,0)]
    if not nonsing:
        return True
    if c[(1,0)] == c[(0,1)] and set(nonsing) <= {(1,0),(0,1)} and c[(1,0)]==c[(0,1)]:
        return True
    if c[(1,0)] in (0,3) and c[(0,1)] in (0,3) and (c[(1,0)]+c[(0,1)])==len(nonsing):
        return True
    return False

def su2_has_singlet(spins):
    # spins are 2j in {0,1}. product contains j=0 ?
    # combine iteratively: set of possible 2j values.
    poss = {0}
    for s in spins:
        nxt=set()
        for a in poss:
            # couple a (2j) with s (2j): |a-s| .. a+s step 2
            lo, hi = abs(a-s), a+s
            for v in range(lo, hi+1, 2):
                nxt.add(v)
        poss = nxt
    return 0 in poss

edges=[]
print("Enumerating gauge-invariant trilinears  psi_i psi_j Phi:")
for (i,j) in itertools.combinations_with_replacement(SECT,2):
    for pname,prep in PHI.items():
        r3 = [SECT[i][0], SECT[j][0], prep[0]]
        s2 = [SECT[i][1], SECT[j][1], prep[1]]
        Ysum = SECT[i][2]+SECT[j][2]+prep[2]
        if abs(Ysum)<1e-9 and su3_has_singlet(r3) and su2_has_singlet(s2):
            print("   %-3s . %-3s . %-6s   (Y sum = 0, SU3 ok, SU2 ok)"%(i,j,pname))
            if i!=j: edges.append((i,j))

print("\nEdges:", edges)

# build graph, components, bipartiteness
import collections
adj=collections.defaultdict(set)
V=list(SECT)
for a,b in edges:
    adj[a].add(b); adj[b].add(a)

color={}
def bfs(start, c0):
    q=[start]; color[start]=c0; comp=[start]
    while q:
        x=q.pop()
        for y in adj[x]:
            if y not in color:
                color[y]=1-color[x]; q.append(y); comp.append(y)
            elif color[y]==color[x]:
                return None
    return comp

comps=[]
ok=True
for v in V:
    if v not in color:
        c=bfs(v,0)
        if c is None: ok=False
        comps.append(c)

print("bipartite:", ok)
print("connected components:", comps)
print("# components:", len(comps))

# the proposed chiral partition
HL={'Q','L'}; HRc={'uc','dc','ec'}
# is it a valid 2-coloring?
valid = all(color_ok(a,b,HL,HRc) for a,b in edges) if False else \
        all((a in HL)!=(b in HL) for a,b in edges)
print("\nProposed partition HL={Q,L}, HRc={uc,dc,ec} is a valid 2-coloring:",
      valid)

# Forcedness: a bipartition of a graph with k components has 2^k global
# sign assignments (each component independently flippable). Within a
# component the coloring is forced up to one global sign.
print("\n# independent Z2 sign choices in the global 2-coloring = 2^%d = %d"
      % (len(comps), 2**len(comps)))
# which vertices are in which component
for idx,c in enumerate(comps):
    print("  component %d: %s   (internal coloring forced up to 1 sign)"%(idx,c))
print("\n=> The graph forces the partition WITHIN each component, but the")
print("   RELATIVE sign between the quark component and the lepton component")
print("   is a free Z2 not fixed by the Yukawa graph alone.")
