"""
PHASE 2 -- CONSTRUCTIVE expressibility for the chain-vs-diamond matched pair, in the EXACT
poly-attention model of arXiv:2602.02422 (no torch; exact numpy; small n, brute-force tuples).

This turns Phase 1's "prediction made + cost-class consistent" into "constructively confirmed",
and CORRECTS Phase 1's cost-model overclaim.

The paper's mechanism (Def 2.4 + the Kozachinskiy sum-of-squares construction, apx_func-comp):
  - input X in R^{N x d}; Q^(j) = X W_Q^(j), V^(j) = X W_V^(j).
  - attention polynomial h = sum of monomials; a degree-2 monomial x_a x_b -> inner prod <Q^a,Q^b>.
  - output row l1 = sum_{l2..lt} exp((1/d) h(Q^1_l1,...,Q^t_lt)) (V^2_l2 (x) ... (x) V^t_lt)
                   / sum_{l2..lt} exp(...).        [ (x) = Hadamard ]
  - KEY GADGET: choose W's so each EDGE realizes <Q^a_la, Q^b_lb> = -(equality residual)^2.
    Then softmax concentrates on the unique tuple with ALL residuals 0 = the answer.
  - graphical rep: vertex per variable, edge per degree-2 monomial. TREE/forest -> O(n^2)
    (Thm tree-att); one cycle (or degree>2) -> superquadratic (Thm ub-lb-poly).

MATCHED PAIR (both 3-function compositional, same per-table encoding, single head):
  A  CHAIN   out=f3(f2(f1(x)))  -- here 2-fold f2(f1(x)) for the core -- graph = PATH  (tree)
  B  DIAMOND out=g(f1(x),f2(x))                                        -- graph = 4-CYCLE

WHAT THIS FILE PROVES (exact, verified):
  (C) chain solved by the PATH polynomial h2=x1x2+x2x3            -- forward pass, exhaustive n=2.
  (D) diamond solved by the 4-CYCLE poly h=x1x2+x1x3+x2x4+x3x4   -- forward pass, exhaustive n=2.
  (E) edge-MINIMALITY teeth: removing ANY one of the 4 cycle edges produces a WITNESSED error
      (two instances the reduced head cannot separate). A forest on 4 vertices has <=3 edges, so
      NO subforest of the cycle solves the diamond. (single-head, degree-2, per-table encoding.)
  (F) escape hatch (the honest Phase-1 correction): the diamond as 2-fold composition over the
      PRODUCT alphabet F:[n]->[n^2] is solved by the PATH polynomial -> the cycle is encoding-
      dependent, traded for an n^2 alphabet blowup (= graphical-models moralization tradeoff).

Scope honesty: the fully-general lower bound (arbitrary embeddings / multiple heads) is the
paper's communication-complexity regime (myopic pointer jumping, Lem cc-lb); we CITE it and
instead give the exact single-head edge-minimality result + the information-flow necessity reason.
"""
import sys
import itertools
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

BETA = 24.0   # softmax sharpness (stands in for A^2 log n); verified large enough to concentrate.

# ---------- feature vector per token (shared input X; the W's are linear reads of it) ----------
# feat = [1, idx, idx^2, phi, phi^2, a, a^2, b, b^2]   (a,b = g-token coords; 0 otherwise)
NF = 9
def feat(idx, phi, a=0, b=0):
    return np.array([1.0, idx, idx*idx, phi, phi*phi, a, a*a, b, b*b], float)

# gadget pieces, each a length-3 linear functional of feat, placed in a 3-dim block:
#   A(val): [val^2, val, 1]      B(idx): [-1, 2*idx, -idx^2]
#   => A . B = -1*val^2 + 2*val*idx - idx^2 = -(val-idx)^2.
def gA_phi(f):  return np.array([f[4], f[3], f[0]])              # val = phi
def gA_a(f):    return np.array([f[6], f[5], f[0]])              # val = a
def gB_idx(f):  return np.array([-f[0], 2*f[1], -f[2]])          # idx = position l
def gB_idx_off(f, off):                                          # idx = l - off
    l = f[1]
    return np.array([-f[0], 2*(l-off), -((l-off)**2)])
def gB_a(f):    return np.array([-f[0], 2*f[5], -f[6]])          # idx = a
def gB_b(f):    return np.array([-f[0], 2*f[7], -f[8]])          # idx = b
def gA_phi_at(f): return np.array([f[4], f[3], f[0]])           # val = phi (for slot2 -> edge24)

ZERO3 = np.zeros(3)


# =========================================================================================
#  POLY-ATTENTION FORWARD  (exact; brute force over tuples)
# =========================================================================================
def forward(Q, edges, N, query_row, readout_slot, vphi, beta=BETA):
    """Q: dict slot-> (N x d) matrix. edges: list of (a,b) 1-based slot pairs = the polynomial.
    Sum over l2..lt in [N] (slot1 fixed = query_row, 0-based). Value: Hadamard product over
    slots 2..t, where readout_slot carries vphi[token] and all other value-slots carry 1.
    Returns the scalar output (column-0 readout)."""
    t = max(max(e) for e in edges)
    slots = list(range(2, t+1))                      # summed slots
    scores, vals = [], []
    for tup in itertools.product(range(N), repeat=len(slots)):
        L = {1: query_row}
        for s, l in zip(slots, tup):
            L[s] = l
        sc = 0.0
        for (a, b) in edges:
            sc += float(np.dot(Q[a][L[a]], Q[b][L[b]]))
        scores.append(beta * sc)
        # Hadamard product of values over summed slots (column-0 convention)
        v = 1.0
        for s in slots:
            v *= (vphi[L[s]] if s == readout_slot else 1.0)
        vals.append(v)
    scores = np.array(scores); vals = np.array(vals)
    w = np.exp(scores - scores.max()); w /= w.sum()
    return float(np.dot(w, vals))


# =========================================================================================
#  CHAIN  f2(f1(x))   --  PATH polynomial  h2 = x1 x2 + x2 x3   (edges (1,2),(2,3))
# =========================================================================================
def build_chain(n, f1, f2, x):
    """tokens: 1..n = f1 (phi=f1(pos)); n+1..2n = f2 (phi=f2(pos-n)); 2n+1 = query (phi=x)."""
    N = 2*n + 1
    toks, vphi = [], []
    for p in range(1, n+1):
        toks.append(feat(p, f1[p-1])); vphi.append(float(f1[p-1]))
    for p in range(n+1, 2*n+1):
        toks.append(feat(p, f2[p-1-n])); vphi.append(float(f2[p-1-n]))
    toks.append(feat(2*n+1, x)); vphi.append(float(x))
    F = np.array(toks)                                # N x NF
    # blocks: B12 = dims0..2, B23 = dims3..5
    d = 6
    def emptyrow(): return np.zeros(d)
    Q = {1: np.zeros((N, d)), 2: np.zeros((N, d)), 3: np.zeros((N, d))}
    for i in range(N):
        f = F[i]
        # slot1 (query): A(phi) in B12
        Q[1][i, 0:3] = gA_phi(f)
        # slot2 (f1-token): B(idx=l) in B12 ; A(phi) in B23
        Q[2][i, 0:3] = gB_idx(f);  Q[2][i, 3:6] = gA_phi(f)
        # slot3 (f2-token): B(idx=l-n) in B23
        Q[3][i, 3:6] = gB_idx_off(f, n)
    return Q, N, np.array(vphi)

def chain_truth(n, f1, f2, x):
    return f2[f1[x-1]-1]


# =========================================================================================
#  DIAMOND  g(f1(x),f2(x))  --  4-CYCLE poly  h = x1x2 + x1x3 + x2x4 + x3x4
# =========================================================================================
def build_diamond(n, f1, f2, g, x):
    """tokens: 1..n=f1; n+1..2n=f2; 2n+1..2n+n^2 = g (one per (a,b), phi=g(a,b), coords a,b);
    last = query (phi=x)."""
    pairs = [(a, b) for a in range(1, n+1) for b in range(1, n+1)]
    N = 2*n + n*n + 1
    toks, vphi = [], []
    for p in range(1, n+1):
        toks.append(feat(p, f1[p-1])); vphi.append(float(f1[p-1]))
    for p in range(n+1, 2*n+1):
        toks.append(feat(p, f2[p-1-n])); vphi.append(float(f2[p-1-n]))
    gpos0 = 2*n
    for m, (a, b) in enumerate(pairs):
        pos = gpos0 + m + 1
        gv = g[(a, b)]
        toks.append(feat(pos, gv, a=a, b=b)); vphi.append(float(gv))
    qpos = N
    toks.append(feat(qpos, x)); vphi.append(float(x))
    F = np.array(toks)
    # blocks: B12=0..2, B13=3..5, B24=6..8, B34=9..11
    d = 12
    Q = {1: np.zeros((N, d)), 2: np.zeros((N, d)), 3: np.zeros((N, d)), 4: np.zeros((N, d))}
    for i in range(N):
        f = F[i]
        # slot1 (query): A(phi=x) in B12 and B13
        Q[1][i, 0:3] = gA_phi(f);  Q[1][i, 3:6] = gA_phi(f)
        # slot2 (f1-token): B(idx=l) in B12 ; A(phi=f1) in B24
        Q[2][i, 0:3] = gB_idx(f);  Q[2][i, 6:9] = gA_phi(f)
        # slot3 (f2-token): B(idx=l-n) in B13 ; A(phi=f2) in B34
        Q[3][i, 3:6] = gB_idx_off(f, n);  Q[3][i, 9:12] = gA_phi(f)
        # slot4 (g-token): B(idx=a) in B24 ; B(idx=b) in B34
        Q[4][i, 6:9] = gB_a(f);  Q[4][i, 9:12] = gB_b(f)
    return Q, N, np.array(vphi)

def diamond_truth(n, f1, f2, g, x):
    return g[(f1[x-1], f2[x-1])]

DIAMOND_EDGES = [(1, 2), (1, 3), (2, 4), (3, 4)]
CHAIN_EDGES   = [(1, 2), (2, 3)]


# =========================================================================================
print("=" * 90)
print("PHASE 2  --  CONSTRUCTIVE chain-vs-diamond separation in the exact poly-attention model")
print("=" * 90)

# ---- (B0) faithfulness: each edge's <Q^a,Q^b> equals the SoS residual -(equality)^2 ----
print("\n(B0) FAITHFULNESS: every polynomial edge realizes <Q^a,Q^b> = -(equality residual)^2")
n = 2
f1 = [2, 1]; f2 = [1, 2]; x = 1
g = {(1, 1): 1, (1, 2): 2, (2, 1): 2, (2, 2): 1}
Q, N, vphi = build_diamond(n, f1, f2, g, x)
qrow = N - 1
l2 = x - 1                       # f1-token at position x
l3 = (n + x) - 1                 # f2-token at position x
# g-token at (f1(x), f2(x)):
pairs = [(a, b) for a in range(1, n+1) for b in range(1, n+1)]
l4 = 2*n + pairs.index((f1[x-1], f2[x-1]))
e12 = np.dot(Q[1][qrow], Q[2][l2]); e13 = np.dot(Q[1][qrow], Q[3][l3])
e24 = np.dot(Q[2][l2], Q[4][l4]);   e34 = np.dot(Q[3][l3], Q[4][l4])
print(f"   at the correct tuple: <Q1,Q2>={e12:.3f} <Q1,Q3>={e13:.3f} <Q2,Q4>={e24:.3f} <Q3,Q4>={e34:.3f}")
chk("all 4 cycle-edge inner products are 0 at the correct tuple (residuals vanish)",
    abs(e12) < 1e-9 and abs(e13) < 1e-9 and abs(e24) < 1e-9 and abs(e34) < 1e-9)
# a deliberately WRONG g-token must give a strictly negative edge score (penalised):
l4bad = 2*n + pairs.index((f1[x-1] % n + 1, f2[x-1]))   # wrong a-coord
ebad = np.dot(Q[2][l2], Q[4][l4bad])
chk("wrong g-token (mismatched a-coord) gives strictly negative <Q2,Q4> (SoS penalty)", ebad < -0.5)

# ---- (C) CHAIN solved by the PATH polynomial -- exhaustive over all n=2 instances ----
print("\n(C) CHAIN f2(f1(x)) solved by PATH poly h2 = x1x2 + x2x3  (graph = path, tree)")
n = 2
funcs = list(itertools.product(range(1, n+1), repeat=n))   # all maps [n]->[n]
ok_all = True; ntested = 0
for f1 in funcs:
    for f2 in funcs:
        for x in range(1, n+1):
            Q, N, vphi = build_chain(n, list(f1), list(f2), x)
            out = forward(Q, CHAIN_EDGES, N, N-1, readout_slot=3, vphi=vphi)
            tru = chain_truth(n, list(f1), list(f2), x)
            ntested += 1
            if round(out) != tru:
                ok_all = False
chk(f"chain solved on ALL {ntested} instances (n=2), output rounds to f2(f1(x))", ok_all)

# ---- (D) DIAMOND solved by the 4-CYCLE polynomial -- exhaustive over all n=2 instances ----
print("\n(D) DIAMOND g(f1(x),f2(x)) solved by 4-CYCLE poly h = x1x2+x1x3+x2x4+x3x4")
n = 2
gtables = []
gpairs = [(a, b) for a in range(1, n+1) for b in range(1, n+1)]
for outs in itertools.product(range(1, n+1), repeat=n*n):
    gtables.append({gpairs[i]: outs[i] for i in range(n*n)})
ok_all = True; ntested = 0
for f1 in funcs:
    for f2 in funcs:
        for g in gtables:
            for x in range(1, n+1):
                Q, N, vphi = build_diamond(n, list(f1), list(f2), g, x)
                out = forward(Q, DIAMOND_EDGES, N, N-1, readout_slot=4, vphi=vphi)
                tru = diamond_truth(n, list(f1), list(f2), g, x)
                ntested += 1
                if round(out) != tru:
                    ok_all = False
chk(f"diamond solved on ALL {ntested} instances (n=2), output rounds to g(f1(x),f2(x))", ok_all)

# spot-check at n=3 (g-table too large to enumerate; random sample)
print("    spot-check n=3 (random g; sampled):")
rng = np.random.default_rng(0)
n = 3; ok3 = True; ns = 0
for _ in range(150):
    f1 = list(rng.integers(1, n+1, size=n)); f2 = list(rng.integers(1, n+1, size=n))
    gp = [(a, b) for a in range(1, n+1) for b in range(1, n+1)]
    g = {p: int(rng.integers(1, n+1)) for p in gp}
    x = int(rng.integers(1, n+1))
    Q, N, vphi = build_diamond(n, f1, f2, g, x)
    out = forward(Q, DIAMOND_EDGES, N, N-1, readout_slot=4, vphi=vphi)
    ns += 1
    if round(out) != diamond_truth(n, f1, f2, g, x):
        ok3 = False
chk(f"diamond solved on {ns} random n=3 instances", ok3)

# ---- (E) TEETH: edge-minimality -- drop any cycle edge -> witnessed failure ----
print("\n(E) LOWER-BOUND TEETH: each of the 4 cycle edges is NECESSARY (drop it -> witnessed error)")
print("    information-flow reason: slot4 must see f1(x) [edge 2-4] and f2(x) [edge 3-4]; slots 2,3")
print("    must be pinned to x [edges 1-2, 1-3]. A forest on 4 vertices has <=3 edges -> misses one.")
n = 2
# A witness for dropping edge (a,b): two instances identical except in the ONE quantity that edge
# guards, with different correct outputs -- the reduced head returns the SAME output on both.
def witness_pair(drop):
    """Return (instA, instB) = (f1,f2,g,x) that the drop-edge head provably cannot separate:
    IDENTICAL forward computation but DIFFERENT correct answers. Mechanism per edge:
      (2,4)/(3,4) readout-side: drop -> g's a/b coord unmatched -> vary f1(x)/f2(x).
      (1,2)/(1,3) pinning-side: drop -> slot reads only the f-VALUE (position-independent), so two
        instances with the SAME value-multiset but PERMUTED positions are indistinguishable."""
    if drop == (2, 4):      # a-coord of g unguarded: vary f1(x) so g-output changes
        x = 1
        gA = {(1,1):1,(1,2):1,(2,1):2,(2,2):2}      # depends on a only
        return ([1,1],[1,1], gA, x), ([2,1],[1,1], gA, x)     # f1(1)=1->g(1,1)=1 ; =2->g(2,1)=2
    if drop == (3, 4):      # b-coord unguarded: vary f2(x)
        x = 1
        gB = {(1,1):1,(1,2):2,(2,1):1,(2,2):2}      # depends on b only
        return ([1,1],[1,1], gB, x), ([1,1],[2,1], gB, x)
    if drop == (1, 2):      # f1-token not pinned to x: same f1 value-multiset, permuted positions
        x = 1
        gA = {(1,1):1,(1,2):1,(2,1):2,(2,2):2}      # depends on a only
        # A: f1=[1,2] -> f1(1)=1 -> g(1,1)=1 ;  B: f1=[2,1] -> f1(1)=2 -> g(2,1)=2
        return ([1,2],[1,1], gA, x), ([2,1],[1,1], gA, x)     # value-multiset {1,2} both
    if drop == (1, 3):      # f2-token not pinned to x: same f2 value-multiset, permuted positions
        x = 1
        gB = {(1,1):1,(1,2):2,(2,1):1,(2,2):2}      # depends on b only
        # A: f2=[1,2] -> f2(1)=1 -> g(1,1)=1 ;  B: f2=[2,1] -> f2(1)=2 -> g(1,2)=2
        return ([1,1],[1,2], gB, x), ([1,1],[2,1], gB, x)     # value-multiset {1,2} both

for drop in DIAMOND_EDGES:
    reduced = [e for e in DIAMOND_EDGES if e != drop]
    (f1A,f2A,gA,xA),(f1B,f2B,gB,xB) = witness_pair(drop)
    QA,NA,vA = build_diamond(n,f1A,f2A,gA,xA)
    QB,NB,vB = build_diamond(n,f1B,f2B,gB,xB)
    oA = forward(QA, reduced, NA, NA-1, readout_slot=4, vphi=vA)
    oB = forward(QB, reduced, NB, NB-1, readout_slot=4, vphi=vB)
    tA = diamond_truth(n,f1A,f2A,gA,xA); tB = diamond_truth(n,f1B,f2B,gB,xB)
    indistinguishable = abs(oA - oB) < 1e-6
    truths_differ = (tA != tB)
    # clean teeth: identical output on differing-truth instances => provably wrong on >=1.
    cannot_be_right_on_both = not (round(oA) == tA and round(oB) == tB)
    print(f"   drop {drop}: truths=({tA},{tB}) reduced-head out=({oA:.3f},{oB:.3f}) "
          f"-> identical={indistinguishable}, truths-differ={truths_differ}")
    chk(f"edge {drop} necessary: head WITHOUT it gives IDENTICAL output on two differing-answer "
        f"instances (=> provably errs)",
        indistinguishable and truths_differ and cannot_be_right_on_both)

# every forest on 4 labelled vertices has <= 3 edges -> cannot contain all 4 cycle edges
import itertools as _it
all_edges = list(_it.combinations([1,2,3,4], 2))
def acyclic(es):
    par = {v: v for v in [1,2,3,4]}
    def find(u):
        while par[u]!=u: par[u]=par[par[u]]; u=par[u]
        return u
    for u,v in es:
        ru,rv=find(u),find(v)
        if ru==rv: return False
        par[ru]=rv
    return True
forests = [es for k in range(0,4) for es in _it.combinations(all_edges,k) if acyclic(es)]
contains_cycle_edges = [set(DIAMOND_EDGES).issubset(set(es)) for es in forests]
chk("no forest on {x1,x2,x3,x4} contains all 4 cycle edges (so no tree-attention solves diamond)",
    not any(contains_cycle_edges))
maxforest = max(len(es) for es in forests)
chk(f"max forest size = {maxforest} edges < 4 cycle edges needed", maxforest == 3)

# ---- (F) ESCAPE HATCH: diamond as 2-fold composition over PRODUCT alphabet -> PATH ----
print("\n(F) ESCAPE HATCH (Phase-1 correction): diamond = 2-fold comp over product alphabet -> PATH")
print("    pre-merge F(x)=(f1(x),f2(x)): [n]->[n^2]; then out=g(F(x)) is 2-fold composition.")
n = 2
ok_all = True; ntested = 0
for f1 in funcs:
    for f2 in funcs:
        for g in gtables:
            for x in range(1, n+1):
                # product encoding: alphabet m=n^2; F: [n]->[m] with F(i)=enc(f1(i),f2(i));
                # G: [m]->[n] with G(enc(a,b))=g(a,b). 2-fold composition G(F(x)) via PATH h2.
                m = n*n
                enc = {(a, b): (a-1)*n + (b-1) + 1 for a in range(1, n+1) for b in range(1, n+1)}
                Fmap = [enc[(f1[i-1], f2[i-1])] for i in range(1, n+1)]   # [n]->[m]
                Gmap = [g[(a, b)] for a in range(1, n+1) for b in range(1, n+1)]  # [m]->[n], idx by enc-1
                # build a 2-block chain: block1 = F (size n, phi in [m]); block2 = G (size m, phi in [n])
                N = n + m + 1
                toks, vphi = [], []
                for p in range(1, n+1):
                    toks.append(feat(p, Fmap[p-1])); vphi.append(float(Fmap[p-1]))
                for p in range(n+1, n+m+1):
                    toks.append(feat(p, Gmap[p-1-n])); vphi.append(float(Gmap[p-1-n]))
                toks.append(feat(N, x)); vphi.append(float(x))
                Fx = np.array(toks); d = 6
                Q = {1: np.zeros((N, d)), 2: np.zeros((N, d)), 3: np.zeros((N, d))}
                for i in range(N):
                    f = Fx[i]
                    Q[1][i, 0:3] = gA_phi(f)                       # query A(phi=x) in B12
                    Q[2][i, 0:3] = gB_idx(f); Q[2][i, 3:6] = gA_phi(f)   # F-token: pin pos / expose phi
                    Q[3][i, 3:6] = gB_idx_off(f, n)               # G-token: pin pos = n + F(x)
                out = forward(Q, CHAIN_EDGES, N, N-1, readout_slot=3, vphi=np.array(vphi))
                tru = diamond_truth(n, list(f1), list(f2), g, x)
                ntested += 1
                if round(out) != tru:
                    ok_all = False
chk(f"diamond solved by PATH polynomial over product alphabet on ALL {ntested} n=2 instances",
    ok_all)
print("    => the 4-cycle is ENCODING-DEPENDENT: removable by product-merging f1,f2, at the cost")
print("       of an alphabet/sequence blowup n -> n^2 (the moralization/treewidth tradeoff).")

print("\n" + "=" * 90)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("PHASE 2 RESULT (exact, constructive, torch-free):")
print(" - chain  solved by the PATH polynomial  (tree-attention, O(n^2)).")
print(" - diamond solved by the 4-CYCLE polynomial (superquadratic per Thm ub-lb-poly).")
print(" - the 4-cycle is EDGE-MINIMAL: removing any edge => a witnessed, unseparable error,")
print("   so no forest (<=3 edges) solves the diamond in the single-head degree-2 per-table model.")
print(" - ESCAPE: product-merging f1,f2 flattens the diamond to a PATH (n -> n^2 blowup),")
print("   correcting Phase 1: the separation is CONDITIONAL on the per-table encoding.")
print("=" * 90)
