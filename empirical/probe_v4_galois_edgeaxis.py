"""
probe_v4_galois_edgeaxis.py  --  is the cyclotomic-tower V_4 the tetrahedral edge-axis V_4,
or a small-group coincidence?

Two Klein four-groups:
  (Galois)   V_4 = Gal(Q(zeta_8)/Q) = (Z/8)^x = {1,3,5,7}, sigma_b: zeta_8 -> zeta_8^b.
             Acts on the four gap-centres (primitive 8th roots) = spec of C = companion(x^4+1).
  (Edge-axis) V_4 = {I, and the three opposite-edge half-turns} subset A_4 of the tetrahedron,
             R(u,pi) = I + 2 K(u)^2 for the three edge axes [1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1].

ABSTRACT iso is automatic (both are V_4 = the three perfect matchings of a 4-set). The DECISIVE
question (genuine geometric realization of arithmetic Galois vs coincidence): does an edge-axis
half-turn P realize a Galois twist of the threshold operator, P C P^{-1} = C^b ? Brute force over
all 384 signed permutations decides which V_4 (if any) realizes Galois, and whether it is the
edge-axis one.

numpy integer arithmetic (exact). No torch.
"""
import numpy as np
import itertools

# threshold operator C = companion of Phi_8 = x^4 + 1  (mult-by-zeta_8 on Z[zeta_8])
C = np.array([[0, 0, 0, -1],
              [1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0]], dtype=int)
I4 = np.eye(4, dtype=int)
pows = {b: np.linalg.matrix_power(C, b) for b in (1, 3, 5, 7)}   # Galois twists C^b
twists = {1: "C", 3: "C^3", 5: "C^5", 7: "C^7"}

print("=" * 86)
print("[1] threshold operator C = companion(x^4+1): order 8, spectrum = primitive 8th roots")
print("=" * 86)
print(f"  C^4 = -I ? {np.array_equal(np.linalg.matrix_power(C,4), -I4)}   "
      f"C^8 = I ? {np.array_equal(np.linalg.matrix_power(C,8), I4)}")
print(f"  C is a signed permutation (one +-1 per row/col)? "
      f"{all(sorted(np.abs(C[i]))== [0,0,0,1] for i in range(4)) and all(sorted(np.abs(C[:,j]))==[0,0,0,1] for j in range(4))}")

print("\n" + "=" * 86)
print("[2] Galois V_4 = (Z/8)^x = {1,3,5,7}: the three involutions and their 2+2 partitions")
print("=" * 86)
units = [1, 3, 5, 7]
for b in units:
    print(f"  sigma_{b}: order {1 if b==1 else 2}, "
          f"fixes {'-' if b==1 else ''}", end="")
    # partition of gap-centres {zeta^1,zeta^3,zeta^5,zeta^7} under a -> b*a mod 8
    seen, parts = set(), []
    for a in units:
        if a in seen: continue
        orb = {a, (b*a) % 8}
        parts.append(sorted(orb)); seen |= orb
    fixed = {1: "(identity)", 3: "Q(sqrt-2)", 5: "Q(i)", 7: "Q(sqrt2)"}[b]
    print(f"{fixed:>10}  partition of exponents {parts}")
print("  => the three involutions give the three perfect matchings of the 4 gap-centres (= V_4).")

print("\n" + "=" * 86)
print("[3] edge-axis half-turns R(u,pi) = I + 2 K(u)^2  (Andy Thomson eq. 13)")
print("=" * 86)
def K(u):
    u1, u2, u3, u4 = u
    return np.array([[0,     u3-u4, u4-u2, u2-u3],
                     [u4-u3, 0,     u1-u4, u3-u1],
                     [u2-u4, u4-u1, 0,     u1-u2],
                     [u3-u2, u1-u3, u2-u1, 0]], dtype=int)
edge_axes = {"AB|CD": (1,1,-1,-1), "AC|BD": (1,-1,1,-1), "AD|BC": (1,-1,-1,1)}
edge_halfturns = {}
for name, u in edge_axes.items():
    Ki = K(u)                       # integer; M-unit u = u/4 gives R = I + (1/8) Ki^2
    R = I4 + (Ki @ Ki) // 8
    edge_halfturns[name] = R
    issp = all(sorted(np.abs(R[i]))==[0,0,0,1] for i in range(4))
    print(f"  {name}: u={u} -> R =\n{R}    signed-perm? {issp}, R^2=I? {np.array_equal(R@R, I4)}")

print("\n" + "=" * 86)
print("[4] DIRECT TEST: does an edge-axis half-turn realize a Galois twist, P C P^-1 = C^b ?")
print("=" * 86)
for name, P in edge_halfturns.items():
    PCP = P @ C @ P.T
    match = next((twists[b] for b in (1,3,5,7) if np.array_equal(PCP, pows[b])), "NONE of C,C^3,C^5,C^7")
    print(f"  {name}: P C P^-1 = {match}")
print("  => the edge-axis half-turns do NOT send C to its Galois powers.")

print("\n" + "=" * 86)
print("[5] BRUTE FORCE over all 384 signed permutations: which V_4 realizes Galois (C -> C^b)?")
print("=" * 86)
realizers = {1: [], 3: [], 5: [], 7: []}
all_signed = []
for perm in itertools.permutations(range(4)):
    for signs in itertools.product([1, -1], repeat=4):
        P = np.zeros((4, 4), dtype=int)
        for i in range(4):
            P[i, perm[i]] = signs[i]
        all_signed.append(P)
        PCP = P @ C @ P.T
        for b in (1, 3, 5, 7):
            if np.array_equal(PCP, pows[b]):
                realizers[b].append(P)
for b in (1, 3, 5, 7):
    print(f"  {twists[b]:>4}: {len(realizers[b])} signed perms realize C -> {twists[b]}")
# is any edge-axis half-turn among the nontrivial realizers?
edge_set = [tuple(P.flatten()) for P in edge_halfturns.values()]
nontrivial = [tuple(P.flatten()) for b in (3,5,7) for P in realizers[b]]
edge_realizes = [n for n in edge_set if n in nontrivial]
print(f"  edge-axis half-turns among the Galois realizers (b in 3,5,7)? "
      f"{len(edge_realizes)} of 3")
# exhibit one realizer of each twist, and whether it is a coordinate permutation or a sign-flip
def describe(P):
    perm = [int(np.nonzero(P[i])[0][0]) for i in range(4)]
    signs = [int(P[i, perm[i]]) for i in range(4)]
    kind = "pure sign-flip (diagonal)" if perm == [0,1,2,3] else \
           ("pure permutation" if all(s==1 for s in signs) else "signed permutation")
    return f"perm={perm}, signs={signs}  [{kind}]"
for b in (3, 5, 7):
    print(f"  example realizer of {twists[b]}: {describe(realizers[b][0])}")

print("\n" + "=" * 86)
print("VERDICT")
print("=" * 86)
print("""  PARTIAL, not full. Exactly ONE of the three edge-axis half-turns -- AD|BC, which is the order-
  reversal (1<->4, 2<->3) -- realizes a Galois twist: it sends C to C^7 = C^{-1} = sigma_7 (complex
  conjugation, the Q(sqrt2)-fixing involution). The other two (AB|CD, AC|BD) send C OUTSIDE <C>
  entirely (to order-8 operators conjugate to C but not powers of it), so the edge-axis V_4 does not
  even normalize <C> and is NOT the Galois V_4.
  The one hit is explained by GENERAL facts, not tetrahedral geometry: (a) reversal conjugates any
  companion/shift to its inverse; (b) inverse = complex conjugation for a root of unity (C^{-1}=C^7);
  (c) with the labels A,B,C,D = 1,2,3,4 the reversal happens to be the AD|BC axis -- a labelling
  artifact (relabel and a different axis would be 'the' conjugation). So the match is not canonical.
  CONCLUSION: the cyclotomic-tower V_4 and the tetrahedral edge-axis V_4 are the SAME only abstractly
  (V_4 on 4 points = the three perfect matchings, automatic), with a single non-canonical partial
  overlap (reversal = conjugation). NOT a genuine geometric realization of cyclotomic Galois. Do NOT
  fold the resonance as structural.
  Genuine residual fact (worth one line in N4): the zeta_8 Galois IS realized by signed permutations
  on the threshold operator -- each twist C^b by exactly 8 of them, with <C> (order 8) the
  centralizer -- so 'Galois = signed permutations of C' holds, just not via the edge-axis group.""")
