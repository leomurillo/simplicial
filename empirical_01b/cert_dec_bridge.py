"""
C1 certificate: K-tilde(u) as a Hodge-dual coboundary on the tetrahedron K4.
Resolves Paper 01 section 1.3.

Claims, verified in exact arithmetic:
  (1) M = 4I - J  equals the graph Laplacian L0 = d0^T d0 of K4.
  (2) ker(d0) = span(1)  (gauge direction = H^0 of the tetrahedron).
  (3) Ktilde(u) read as a 1-cochain equals star_E (d0 u), where star_E is the
      signed opposite-edge involution (combinatorial Hodge star from self-duality
      of the 3-simplex). Verified for symbolic u.
  (4) d1 d0 = 0 (discrete d^2 = 0): the discrete curl-grad identity.
sympy only; no floating point.
"""
import sympy as sp

# --- tetrahedron 1-skeleton K4 ---
V = [1, 2, 3, 4]
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]   # oriented i<j
faces = [(2, 3, 4), (1, 3, 4), (1, 2, 4), (1, 2, 3)]        # complementary to vertex 1,2,3,4

# coboundary d0 : C^0 (R^4) -> C^1 (R^6),  (d0 u)([ij]) = u_j - u_i
d0 = sp.zeros(6, 4)
for e, (i, j) in enumerate(edges):
    d0[e, i - 1] = -1
    d0[e, j - 1] = 1

# (1) graph Laplacian
L0 = d0.T * d0
M = 4 * sp.eye(4) - sp.ones(4, 4)
print("(1) M == L0(K4):", sp.simplify(L0 - M) == sp.zeros(4, 4))
print("    L0 =", L0.tolist())

# (2) kernel of d0
print("(2) ker(d0) =", d0.nullspace(), " (gauge direction 1 = H^0)")

# raw cyclic-difference generator
u = sp.symbols('u1 u2 u3 u4')
def Ktilde(uu):
    u1, u2, u3, u4 = uu
    return sp.Matrix([
        [0,      u3-u4,  u4-u2,  u2-u3],
        [u4-u3,  0,      u1-u4,  u3-u1],
        [u2-u4,  u4-u1,  0,      u1-u2],
        [u3-u2,  u1-u3,  u2-u1,  0],
    ])
Kt = Ktilde(u)

# read Ktilde as 1-cochain: value on edge [ij] (i<j) is Kt[i-1, j-1]
Kt_coch = sp.Matrix([Kt[i - 1, j - 1] for (i, j) in edges])
d0u = d0 * sp.Matrix(u)

# (3) opposite-edge signed involution
opp = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}  # edge idx -> opposite edge idx
signs = []
ok = True
for e in range(6):
    s = sp.simplify(Kt_coch[e] / d0u[opp[e]])
    signs.append(s)
    if s not in (sp.Integer(1), sp.Integer(-1)):
        ok = False
print("(3) Ktilde = star_E(d0 u): signed opposite-edge map, signs =", signs, " unit-signs:", ok)
# reconstruct star_E as a 6x6 signed permutation and confirm the matrix identity
starE = sp.zeros(6, 6)
for e in range(6):
    starE[e, opp[e]] = signs[e]
print("    Ktilde_cochain - starE*d0u =", sp.simplify(Kt_coch - starE * d0u).T)

# (4) d1 d0 = 0  (discrete d^2)
d1 = sp.zeros(4, 6)
eidx = {e: k for k, e in enumerate(edges)}
for f, (i, j, k) in enumerate(faces):
    # boundary of [ijk] = [jk] - [ik] + [ij]
    d1[f, eidx[(j, k)]] += 1
    d1[f, eidx[(i, k)]] += -1
    d1[f, eidx[(i, j)]] += 1
print("(4) d1 d0 =", (d1 * d0).tolist(), " (== zero matrix:", (d1 * d0) == sp.zeros(4, 4), ")")
