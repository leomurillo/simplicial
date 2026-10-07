"""
BIGRADING PROBE: are the order axis (cumulant tower T^(n)=grad^n phi) and the
degree axis (Hodge complex L_k, beta_k) two coordinates of one bigraded object?

Tests, exact:
 A. DEGREE axis is N-flat: combinatorial Hodge L_k on the FILLED (N-1)-simplex has
    nonzero spectrum identically N, for ALL k (not just k=1). [extends forward3]
 B. ORDER axis GROWS: the order-n cumulant grad^n phi at the uniform point p_*=(1/N)1
    has diagonal value (-1)^n (n-2)! N^(n-1) -- NOT flat at N. [from forward2]
 C. THE BIGRADED OBJECT: polynomial differential forms P_n Lambda^k on R^d carry two
    grade-shifting differentials -- de Rham d (n->n-1, k->k+1) and Koszul/Euler
    contraction kappa=iota_E (n->n+1, k->k-1) -- with the CARTAN identity
        d kappa + kappa d = (n+k) * Id   on P_n Lambda^k,
    the Lie derivative along the Euler field. This is the precise sense in which
    order n and form-degree k are two coordinates of ONE bigraded object, with
    conserved total degree n+k. Also d^2=0, kappa^2=0.
 D. VERDICT numbers: the two towers share only the corner (order 2, degree 0) = the
    K_N graph Laplacian = N; above it they diverge (order ~ N^(n-1)(n-2)!, degree flat N).

numpy + sympy + integers only. No torch.
"""
import itertools
import numpy as np
import sympy as sp

PASS = []
def check(name, ok):
    PASS.append(ok)
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

# ----------------------------------------------------------------------------
# A. DEGREE axis: combinatorial Hodge L_k = N at every degree, filled simplex
# ----------------------------------------------------------------------------
print("A. degree axis -- Hodge L_k nonzero spectrum on the filled (N-1)-simplex")
def coboundary(N, k):
    ks = list(itertools.combinations(range(N), k + 1))
    k1s = list(itertools.combinations(range(N), k + 2))
    idx = {s: j for j, s in enumerate(ks)}
    D = np.zeros((len(k1s), len(ks)))
    for r, face in enumerate(k1s):
        for a in range(len(face)):
            D[r, idx[face[:a] + face[a + 1:]]] = (-1) ** a
    return D

for N in (4, 5, 6):
    cob = {k: coboundary(N, k) for k in range(0, N - 1)}
    for k in range(0, N - 1):
        up = cob[k].T @ cob[k] if k in cob else None
        down = cob[k - 1] @ cob[k - 1].T if (k - 1) in cob else None
        L = (up if up is not None else 0) + (down if down is not None else 0)
        ev = np.linalg.eigvalsh(L)
        nz = ev[np.abs(ev) > 1e-9]
        ok = (nz.size > 0) and np.allclose(nz, N, atol=1e-9)
        check(f"N={N} k={k}: L_k nonzero spectrum == N  ({nz.min():.3f}..{nz.max():.3f})", ok)

# ----------------------------------------------------------------------------
# B. ORDER axis: cumulant grad^n phi at uniform p_* scales as (-1)^n (n-2)! N^(n-1)
# ----------------------------------------------------------------------------
print("B. order axis -- cumulant scale at the uniform point")
p = sp.symbols('p', positive=True)
g = p * sp.log(p)
for N in (4, 5, 6):
    for n in range(2, 7):
        gn = sp.diff(g, p, n)
        val = sp.simplify(gn.subs(p, sp.Rational(1, N)))
        pred = (-1) ** n * sp.factorial(n - 2) * sp.Integer(N) ** (n - 1)
        check(f"N={N} n={n}: grad^n phi|_p* == (-1)^n (n-2)! N^(n-1)  (={val})",
              sp.simplify(val - pred) == 0)

# ----------------------------------------------------------------------------
# C. THE BIGRADED OBJECT: polynomial differential forms, Cartan identity
#    d kappa + kappa d = (n+k) Id ;  d^2 = 0 ; kappa^2 = 0
# ----------------------------------------------------------------------------
print("C. bigraded object -- polynomial differential forms P_n Lambda^k, Cartan identity")
d = 3                                  # H for N=4 is 3-dimensional
xs = sp.symbols(f'x0:{d}')

# a form is a dict { sorted index tuple I : sympy polynomial }
def dRham(form):                       # d : P_n L^k -> P_{n-1} L^{k+1}
    out = {}
    for I, poly in form.items():
        for j in range(d):
            dp = sp.diff(poly, xs[j])
            if dp == 0 or j in I:
                continue
            newI = tuple(sorted(I + (j,)))
            sign = (-1) ** newI.index(j)
            out[newI] = sp.expand(out.get(newI, 0) + sign * dp)
    return {I: q for I, q in out.items() if q != 0}

def kappa(form):                       # iota_Euler : P_n L^k -> P_{n+1} L^{k-1}
    out = {}
    for I, poly in form.items():
        for pos, j in enumerate(I):
            newI = tuple(t for t in I if t != j)
            sign = (-1) ** pos
            out[newI] = sp.expand(out.get(newI, 0) + sign * xs[j] * poly)
    return {I: q for I, q in out.items() if q != 0}

def add(f, g_, c=1):
    out = dict(f)
    for I, q in g_.items():
        out[I] = sp.expand(out.get(I, 0) + c * q)
    return {I: q for I, q in out.items() if q != 0}

def monomials(n):                      # degree-n monomials in d vars
    if n == 0:
        return [sp.Integer(1)]
    return [sp.prod([xs[i] for i in c]) for c in
            itertools.combinations_with_replacement(range(d), n)]

cartan_ok = dd_ok = kk_ok = True
for n in range(0, 4):
    for k in range(0, d + 1):
        for I in itertools.combinations(range(d), k):
            for mono in monomials(n):
                form = {tuple(I): mono}
                lhs = add(dRham(kappa(form)), kappa(dRham(form)))      # (dk+kd) form
                # compare to (n+k)*form
                target = {tuple(I): sp.expand((n + k) * mono)} if (n + k) != 0 else {}
                if add(lhs, target, c=-1) != {}:
                    cartan_ok = False
                if dRham(dRham(form)) != {}:
                    dd_ok = False
                if kappa(kappa(form)) != {}:
                    kk_ok = False
check("Cartan: d.kappa + kappa.d == (n+k) Id on P_n L^k (n<=3,k<=3,d=3)", cartan_ok)
check("d^2 = 0 (de Rham)", dd_ok)
check("kappa^2 = 0 (Koszul)", kk_ok)

# the de Rham d carries the order column k=0 into the degree row k=1 (the bridge)
bridge = dRham({(): xs[0] ** 2})        # d of a degree-2 poly function -> 1-form
check("bridge: d maps P_n Lambda^0 (order column) into Lambda^1 (degree row)",
      all(len(I) == 1 for I in bridge))

# ----------------------------------------------------------------------------
# D. VERDICT numbers: shared corner, then divergence
# ----------------------------------------------------------------------------
print("D. verdict -- shared corner (order2,deg0)=N, divergence above it")
for N in (4, 5, 6):
    order2 = sp.simplify(sp.diff(g, p, 2).subs(p, sp.Rational(1, N)))   # == N
    order3 = sp.simplify(sp.diff(g, p, 3).subs(p, sp.Rational(1, N)))   # == -N^2
    check(f"N={N}: order-2 cumulant = N = L_0 graph-Laplacian eigenvalue (={order2})",
          sp.simplify(order2 - N) == 0)
    check(f"N={N}: order-3 cumulant = {order3} != N  (towers DIVERGE above the corner)",
          sp.simplify(order3 - N) != 0)

print("=" * 70)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} checks OK ->",
      "GREEN" if all(PASS) else "RED")
print("=" * 70)
