"""
Cert: exact-rational FEEC element matrices on rational-coordinate (Quadray/IVM) cells.

Claim (Paper 01d, new section): on any d-simplex whose vertices have rational
Cartesian/Quadray coordinates, every lowest-order FEEC element matrix is exactly
rational -- no quadrature, no sqrt -- because barycentric coords, the gradient
Gram, the volume, and the Whitney-form moments are all rational in the vertices.
Cleanest case: the regular tetrahedron, where the P1 stiffness = rational * (4I-J).

Tested cells (both integer Cartesian, i.e. rational Quadray):
  - regular tet  : Tom Ace vertices (+-1,+-1,+-1) with even # of minus signs
  - IVM octa-1/4 : (0,0,0),(2,0,0),(0,2,0),(0,0,2)  (a triangulated octahedron cell)

Deterministic sympy gate. All assertions are exact (Rational), zero tolerance.
"""
import sympy as sp

def bary(vertices):
    """Affine barycentric coords lambda_i(x)=A[i].x+b[i] for a 3-simplex; exact."""
    V = sp.Matrix(vertices)                       # 4 x 3
    # solve [v_i 1] coefficients: lambda_i are affine, sum to 1, lambda_i(v_j)=delta_ij
    Aug = V.row_join(sp.ones(4, 1))               # 4 x 4  (homogeneous)
    C = Aug.inv()                                 # columns give affine coeffs
    grads = [sp.Matrix(C[0:3, i]) for i in range(4)]   # grad lambda_i (constant)
    consts = [C[3, i] for i in range(4)]
    return grads, consts, V

def volume(vertices):
    V = [sp.Matrix(v) for v in vertices]
    return sp.Abs((V[1]-V[0]).dot((V[2]-V[0]).cross(V[3]-V[0]))) / 6

def moment(vol, i, j):
    """integral_T lambda_i lambda_j  = vol*(1+delta_ij)/((d+1)(d+2)),  d=3 -> /20."""
    return vol * (1 + (1 if i == j else 0)) / 20

def p1_matrices(vertices):
    grads, _, _ = bary(vertices)
    vol = volume(vertices)
    G = sp.Matrix(4, 4, lambda i, j: grads[i].dot(grads[j]))   # gradient Gram
    stiff = vol * G
    mass = sp.Matrix(4, 4, lambda i, j: moment(vol, i, j))
    return sp.nsimplify(stiff), sp.nsimplify(mass), sp.nsimplify(G), vol

def whitney1_mass(vertices):
    """Lowest-order Whitney 1-form (edge) mass matrix, exact via barycentric moments.
       W_e = lam_i grad lam_j - lam_j grad lam_i for edge e=[i,j]."""
    grads, _, _ = bary(vertices)
    vol = volume(vertices)
    edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    def integral_W_dot_W(e, f):
        i,j = e; k,l = f
        gi,gj,gk,gl = grads[i],grads[j],grads[k],grads[l]
        # W_e.W_f = sum over the four (lam_a)(lam_b)(grad_p.grad_q) terms
        terms = [( i,k, gj.dot(gl)), ( i,l,-gj.dot(gk)),
                 ( j,k,-gi.dot(gl)), ( j,l, gi.dot(gk))]
        return sum(moment(vol,a,b)*c for a,b,c in terms)
    return sp.Matrix(6,6, lambda r,c: sp.nsimplify(integral_W_dot_W(edges[r],edges[c])))

reg = [(-1,-1, 1),( 1, 1, 1),( 1,-1,-1),(-1, 1,-1)]   # regular tet, edge^2 = 8
octq= [( 0, 0, 0),( 2, 0, 0),( 0, 2, 0),( 0, 0, 2)]   # IVM octahedron quarter

def all_rational(M):
    return all(sp.nsimplify(e).is_rational for e in M)

M_metric = 4*sp.eye(4) - sp.ones(4,4)            # the frame metric M = 4I - J

print("=== regular tetrahedron (Tom Ace integer coords) ===")
S,Mass,G,vol = p1_matrices(reg)
W1 = whitney1_mass(reg)
print("  volume (tetravolume-proportional) =", vol, " rational:", vol.is_rational)
print("  P1 stiffness rational:", all_rational(S))
print("  P1 mass      rational:", all_rational(Mass))
print("  Whitney-1 mass rational:", all_rational(W1))
# stiffness = rational * (4I - J) ?
ratio = sp.simplify(S[0,0]/M_metric[0,0])
print("  stiffness == (", ratio, ")*(4I-J) :", sp.simplify(S - ratio*M_metric) == sp.zeros(4,4))

print("\n=== IVM octahedron-quarter (integer coords, NOT regular) ===")
S2,Mass2,G2,vol2 = p1_matrices(octq)
W12 = whitney1_mass(octq)
print("  volume =", vol2, " rational:", vol2.is_rational)
print("  P1 stiffness rational:", all_rational(S2))
print("  P1 mass      rational:", all_rational(Mass2))
print("  Whitney-1 mass rational:", all_rational(W12))

print("\n=== moment-formula spot check  int_T lam_i lam_j ===")
# d=3 reference: int 1 = vol; int lam_i = vol/4; int lam_i^2 = vol/10; int lam_i lam_j = vol/20
print("  int lam_0^2 =", moment(vol,0,0), " (= vol/10 =", vol/10, ")")
print("  int lam_0 lam_1 =", moment(vol,0,1), " (= vol/20 =", vol/20, ")")

ok = (all_rational(S) and all_rational(Mass) and all_rational(W1)
      and all_rational(S2) and all_rational(Mass2) and all_rational(W12)
      and sp.simplify(S - ratio*M_metric) == sp.zeros(4,4))
print("\nCERT", "PASS" if ok else "FAIL")
