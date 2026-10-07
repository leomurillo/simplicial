"""
C5 certificate: gauge curvature of varying simplicial frames.
Distinguishes the continuous abelian R*1 gauge (trivial) from the discrete
orientation Z/2 = S4/A4 gauge (genuinely nontrivial). sympy/numpy, exact.

Verdict tested:
 A. The abelian R*1 connection (shift along the gauge line 1) has curvature
    F = dA == 0 identically: the structure group S4 fixes 1 (P_sigma 1 = 1), and
    the mean-subtraction (zero-sum) section is GLOBAL, so the bundle is trivial.
 B. The orientation Z/2 lattice gauge field (edge variable sgn(sigma_e)) DOES carry
    nontrivial curvature: the plaquette product F_f = prod_{e in df} sgn(sigma_e) is
    gauge-invariant and can be -1 (an orientation defect / disclination). Linked to
    Paper 01 Prop 2.2: net-odd holonomy negates the cross product (P_h^-1 K(P_h u) P_h = -K(u)).
 C. The full frame bundle is a FLAT S4 bundle whose holonomy can be nontrivial
    (non-orientable "Mobius" gluing has no global orientation: w1 != 0).
"""
import itertools
import sympy as sp

S4 = list(itertools.permutations(range(4)))
one = sp.ones(4, 1)

def Pmat(s):                       # (P_s)_{ij} = delta_{s(j), i}
    P = sp.zeros(4, 4)
    for j in range(4):
        P[s[j], j] = 1
    return P

def sgn(s):
    p = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if s[i] > s[j]:
                p = -p
    return p

def comp(s, t):                    # (s o t)(i) = s(t(i))
    return tuple(s[t[i]] for i in range(4))

def inv(s):
    r = [0] * 4
    for i in range(4):
        r[s[i]] = i
    return tuple(r)

def Ktilde(u):
    u1, u2, u3, u4 = u
    return sp.Matrix([[0, u3-u4, u4-u2, u2-u3], [u4-u3, 0, u1-u4, u3-u1],
                      [u2-u4, u4-u1, 0, u1-u2], [u3-u2, u1-u3, u2-u1, 0]])

print("A. continuous abelian R*1 gauge")
A1 = all(Pmat(s) * one == one for s in S4)
print("   P_sigma . 1 = 1  for all 24 sigma in S4:", A1, "  => R*1 sub-bundle is S4-invariant")
c = sp.Matrix(sp.symbols('c1 c2 c3 c4'))
sec = c - (sum(c) / 4) * one
print("   mean-subtraction section is GLOBAL (zero-sum everywhere):", sp.simplify(sum(sec)) == 0)
print("   => abelian curvature F = dA == 0 identically; holonomy trivial.\n")

print("B. discrete orientation Z/2 = S4/A4 gauge field")
odd = (1, 0, 2, 3)     # transposition, sgn = -1
even = (0, 1, 2, 3)    # identity, sgn = +1

def plaq(sigmas):
    p = 1
    for s in sigmas:
        p *= sgn(s)
    return p

defect = [odd, even, even, even]      # one odd gluing around a 4-cell loop
flat = [odd, odd, even, even]
print("   plaquette curvature F (one odd gluing) =", plaq(defect), " (-1 = orientation DEFECT)")
print("   plaquette curvature F (two odd gluings) =", plaq(flat), " (+1 = flat)")

# gauge invariance under cell-orientation flips tau_c : sigma_e -> tau_{c'} sigma_e tau_c^{-1}
taus = [(0, 1, 2, 3), (1, 0, 2, 3), (2, 1, 0, 3), (0, 2, 1, 3)]   # one per cell (deterministic)
# plaquette cells 0,1,2,3 in a cycle; edge i: cell i -> cell i+1 (mod 4)
def gauge_transform(sigmas, taus):
    m = len(sigmas)
    return [comp(comp(taus[(i + 1) % m], sigmas[i]), inv(taus[i])) for i in range(m)]
print("   gauge-invariance of F (defect): before =", plaq(defect),
      " after cell-flips =", plaq(gauge_transform(defect, taus)))
print("   gauge-invariance of F (flat):   before =", plaq(flat),
      " after cell-flips =", plaq(gauge_transform(flat, taus)))

# link to Prop 2.2: net-odd holonomy negates the cross product
u = sp.Matrix(sp.symbols('u1 u2 u3 u4'))
h = odd                                # an odd net holonomy
lhs = Pmat(inv(h)) * Ktilde(Pmat(h) * u) * Pmat(h)
print("   Prop 2.2 / transport: P_h^-1 K(P_h u) P_h = sgn(h) K(u) for odd h:",
      sp.simplify(lhs - sgn(h) * Ktilde(u)) == sp.zeros(4, 4), " (h odd => returns -K)\n")

print("C. flat S4 bundle with nontrivial holonomy (non-orientable mesh)")
# Mobius loop of cells: net holonomy = product of gluings around the non-contractible loop
loop = [(1, 2, 3, 0), (0, 1, 2, 3), (3, 0, 1, 2)]    # 3-cycle gluings
hol = (0, 1, 2, 3)
for s in loop:
    hol = comp(s, hol)
print("   net S4 holonomy around the loop:", hol, " (identity? ", hol == (0, 1, 2, 3), ")")
orient_hol = plaq(loop)
print("   orientation holonomy sgn(prod) =", orient_hol)
# a genuinely non-orientable loop: net holonomy odd
mobius = [(1, 0, 2, 3)]                 # single odd gluing closing a loop
print("   Mobius loop (one odd gluing closing up): orientation holonomy =", plaq(mobius),
      " => w1 != 0, NO global orientation")
print("   each cell is locally consistent (flat); the obstruction is global (topological).")
print("\nVERDICT: abelian R*1 curvature == 0 (trivial); orientation Z/2 curvature can be -1")
print("         (defect) with global holonomy w1 = the orientability class. Discrete gauge theory.")
