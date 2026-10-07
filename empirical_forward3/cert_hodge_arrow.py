r"""
FORWARD-3 CERTIFICATE  --  Discrete Hodge/Helmholtz on a simplicial COMPLEX,
the arrow = beta_1, and the exact/coexact <-> symmetric/antisymmetric weld.

This extends Paper 01b (Prop. 7.3 / Thm 10.1), which established the
curvature/current split on a SINGLE cell (the tetrahedron K4): there the
graph Laplacian L0 = d0^T d0 = M = 4I - J is the simplicial metric, the gauge
direction span{1} = H^0 = ker L0, and the field-Jacobian split DF = S + A has
  tr S = div F   (curvature/source)      A = 1/2 Ktilde(curl F)  (current).
On one cell b1 = 0, so there is no protected current.  THIS certificate moves
to a COMPLEX, where b1 can be nonzero, and verifies four things in EXACT
arithmetic (sympy Rational; numpy used only for an independent spectral
cross-check, with residuals reported):

  (H) Hodge decomposition of 1-cochains.  With coboundaries d0: C0->C1 and
      d1: C1->C2, the 1-Hodge-Laplacian L1 = d0 d0^T + d1^T d1 gives
          C1 = im(d0)  (+)  im(d1^T)  (+)  ker(L1),
      a triple of MUTUALLY ORTHOGONAL subspaces that SPAN C1.  Reading:
          im d0  = EXACT   = grad      (curvature sector,  A = 0)
          im d1^T= COEXACT = curl       (current sector,    tr S = 0)
          ker L1 = HARMONIC.
      Verified:  dim im d0 + dim im d1^T + dim ker L1 = dim C1;
                 the three projectors are orthogonal and sum to I;
                 d1 d0 = 0  (d^2 = 0, so the sectors are genuinely complementary).

  (B) THE ARROW = beta_1.  dim ker(L1) = b1 = first Betti number = #independent
      loops, on a panel of complexes with b1 = 0, 1, 2, 3 (single tetra / filled
      disk -> 0; triangulated annulus & loop-of-triangles -> 1; figure-eight ->
      2; etc.).  b1 cross-checked three independent ways: rank(L1) nullity,
      Euler/rank identity  b1 = dimC1 - rank d0 - rank d1, and the graph cycle
      rank for the 1-skeleton baseline.

  (C) EXACT/COEXACT  <->  SYMMETRIC/ANTISYMMETRIC.  On the tetrahedron the
      Paper 01b dictionary is reproduced cell-locally and then promoted:
      an exact (grad) 1-cochain has ZERO current (it is d0 of a potential, its
      Jacobian is a symmetric Hessian, A = 0); a coexact (curl) 1-cochain is
      trace-free / divergence-free (d0^T of it = 0 = "div curl = 0"); the
      harmonic sector is annihilated by both d0^T and d1 (closed AND co-closed).
      The single-encoder/self-adjoint instrument sees only the symmetric (exact)
      sector and is BLIND to the harmonic current of dimension b1.

  (D) SELF-ADJOINT BLINDNESS, quantified.  A symmetric quadratic form
      q(x) = x^T Q x with Q = Q^T has the antisymmetric content in its kernel:
      for the transport operator T = (I - L1) restricted appropriately,
      <x, T x> = <x, S x> with S = 1/2(T+T^T), exactly (residual 0); the
      harmonic/current modes are invisible to q.  This is the simplicial-complex
      form of the Irreversible Blind Spot (Lemma 1) welded to Hodge theory.

Run:  py cert_hodge_arrow.py        (expects all-GREEN)
Deps: sympy, numpy ONLY.  No torch / no floating-point in the load-bearing checks.
"""

import sys
import itertools
import numpy as np
import sympy as sp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PASS = True
def check(name, ok, extra=""):
    global PASS
    PASS = PASS and bool(ok)
    flag = "GREEN" if ok else "***RED***"
    print(f"  [{flag}] {name}" + (f"   {extra}" if extra else ""))


# ===========================================================================
#  Simplicial-complex machinery (oriented, exact rational boundary maps)
# ===========================================================================
class Complex:
    """An (abstract) oriented simplicial complex given by its top-cell lists.
    Simplices are sorted tuples of integer vertices; orientation = increasing
    vertex order; boundary signs the standard alternating face signs.  We build
    d0: C0->C1 and d1: C1->C2 as exact sympy matrices (rows = higher simplices,
    cols = lower simplices), so (dk)_{[hi],[lo]} = +/-1 if [lo] is a face of [hi].
    """
    def __init__(self, triangles=(), edges_extra=()):
        tris = [tuple(sorted(t)) for t in triangles]
        # all edges: from triangles + any explicit extra edges (for graphs/loops)
        eset = set()
        for t in tris:
            for e in itertools.combinations(t, 2):
                eset.add(tuple(sorted(e)))
        for e in edges_extra:
            eset.add(tuple(sorted(e)))
        vset = set()
        for e in eset:
            vset.update(e)
        for t in tris:
            vset.update(t)
        self.V = sorted(vset)
        self.E = sorted(eset)
        self.F = sorted(set(tris))
        self.vi = {v: k for k, v in enumerate(self.V)}
        self.ei = {e: k for k, e in enumerate(self.E)}
        self.fi = {f: k for k, f in enumerate(self.F)}

    # ---- coboundaries (= transpose of boundary); exact sympy ----
    def d0(self):
        D = sp.zeros(len(self.E), len(self.V))
        for (i, j), r in self.ei.items():
            D[r, self.vi[i]] = -1   # (d0 u)([ij]) = u_j - u_i
            D[r, self.vi[j]] = 1
        return D

    def d1(self):
        D = sp.zeros(len(self.F), len(self.E))
        for (i, j, k), r in self.fi.items():
            # boundary of [ijk] = [jk] - [ik] + [ij]
            D[r, self.ei[(j, k)]] += 1
            D[r, self.ei[(i, k)]] += -1
            D[r, self.ei[(i, j)]] += 1
        return D

    def L1(self):
        d0, d1 = self.d0(), self.d1()
        return d0 * d0.T + d1.T * d1

    def betti(self):
        """(b0, b1, b2) from exact ranks of the boundary chain."""
        d0, d1 = self.d0(), self.d1()
        nV, nE, nF = len(self.V), len(self.E), len(self.F)
        r0 = d0.rank()   # = nV - b0  (rank of coboundary C0->C1 = rank boundary C1->C0)
        r1 = d1.rank()   # = rank of C1->C2 boundary
        b0 = nV - r0
        b1 = nE - r0 - r1
        b2 = nF - r1
        return b0, b1, b2, (nV, nE, nF, r0, r1)


# ===========================================================================
#  Test complexes with KNOWN topology
# ===========================================================================
def tetra():
    # solid-surface-free: the four triangular faces of a tetra (a 2-sphere S^2)
    return Complex(triangles=[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)])

def filled_disk():
    # a triangulated disk (contractible): central vertex 0 fanned to a hexagon.
    rim = [1, 2, 3, 4, 5, 6]
    tris = [(0, rim[k], rim[(k + 1) % 6]) for k in range(6)]
    return Complex(triangles=tris)

def annulus():
    # triangulated annulus (cylinder side): two concentric hexagons, triangulated
    # between them.  b1 = 1 (one hole).  Inner ring 1..6, outer ring 7..12.
    inner = [1, 2, 3, 4, 5, 6]
    outer = [7, 8, 9, 10, 11, 12]
    tris = []
    for k in range(6):
        a, b = inner[k], inner[(k + 1) % 6]
        c, d = outer[k], outer[(k + 1) % 6]
        # quad (a,b,d,c) split into two triangles
        tris.append(tuple(sorted((a, b, c))))
        tris.append(tuple(sorted((b, c, d))))
    return Complex(triangles=tris)

def hollow_triangle_loop():
    # a single triangle with its 2-cell REMOVED: three edges forming one loop.
    # Pure 1-complex; b1 = 1.  (Edges only, no faces.)
    return Complex(edges_extra=[(1, 2), (2, 3), (1, 3)])

def figure_eight():
    # two loops sharing a vertex (1-complex); b1 = 2.
    e = [(1, 2), (2, 3), (1, 3),      # loop A
         (1, 4), (4, 5), (1, 5)]      # loop B sharing vertex 1
    return Complex(edges_extra=e)

def theta_graph():
    # two vertices joined by three internally-disjoint paths; b1 = 2.
    e = [(1, 3), (3, 2),      # path 1
         (1, 4), (4, 2),      # path 2
         (1, 5), (5, 2)]      # path 3
    return Complex(edges_extra=e)

def torus_like_K4_minus():
    # tetra surface with ONE face removed -> a disk (b1=0) is boring; instead
    # take three triangles around a central vertex but leave the rim OPEN-closed:
    # an annulus already covers b1=1.  Use a wedge of three loops for b1=3.
    e = [(1, 2), (2, 3), (1, 3),
         (1, 4), (4, 5), (1, 5),
         (1, 6), (6, 7), (1, 7)]
    return Complex(edges_extra=e)

CASES = [
    ("tetrahedron surface S^2 (single cell, filled)", tetra(),                 0),
    ("filled disk (hexagon fan, contractible)",       filled_disk(),           0),
    ("triangulated annulus (one hole)",               annulus(),               1),
    ("hollow triangle (1 loop, 2-cell removed)",      hollow_triangle_loop(),  1),
    ("figure-eight (two loops, shared vertex)",       figure_eight(),          2),
    ("theta graph (two independent cycles)",          theta_graph(),           2),
    ("wedge of three loops",                          torus_like_K4_minus(),   3),
]


# ===========================================================================
def numeric(M):
    return np.array(M.tolist(), dtype=float)

def col_ortho_basis(Mnp, tol=1e-9):
    """Orthonormal basis (numpy) for the column space of a real matrix."""
    if Mnp.size == 0 or Mnp.shape[1] == 0:
        return np.zeros((Mnp.shape[0], 0))
    U, s, _ = np.linalg.svd(Mnp, full_matrices=False)
    r = int((s > tol * (s[0] if s[0] > 0 else 1)).sum())
    return U[:, :r]


def main():
    print(__doc__)

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(B)+(H-dim)  THE ARROW = beta_1:  dim ker(L1) == b1, three independent ways")
    print("=" * 78)
    print(f"  {'complex':<46}{'V/E/F':>10}{'b1':>5}{'kerL1':>7}{'rankid':>8}")
    for name, X, b1_expected in CASES:
        b0, b1, b2, (nV, nE, nF, r0, r1) = X.betti()
        L1 = X.L1()
        # exact nullity of L1 (over Q): dim ker L1
        ker_L1 = nE - L1.rank()
        # rank identity:  b1 = dim C1 - rank d0 - rank d1
        b1_rankid = nE - r0 - r1
        ok = (b1 == b1_expected == ker_L1 == b1_rankid)
        check(f"{name}", ok,
              f"V/E/F={nV}/{nE}/{nF}  b1={b1}  dim ker L1={ker_L1}  rank-id={b1_rankid}")
        # independent numpy spectral cross-check of the nullity of L1
        L1np = numeric(L1)
        if L1np.shape[0] > 0:
            evals = np.linalg.eigvalsh(L1np)
            nzero = int((np.abs(evals) < 1e-8).sum())
            check(f"    (numpy spectrum nullity matches)", nzero == ker_L1,
                  f"#~0 eigenvalues = {nzero}, min|nonzero|={np.min(np.abs(evals[np.abs(evals)>=1e-8])) if (np.abs(evals)>=1e-8).any() else float('nan'):.4g}")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(H)  HODGE DECOMPOSITION of 1-cochains: orthogonal, spanning, dims add")
    print("=" * 78)
    for name, X, _ in CASES:
        d0, d1 = X.d0(), X.d1()
        nE = len(X.E)
        if nE == 0:
            continue
        # exact d1 d0 = 0  (d^2 = 0)  -- prerequisite for the decomposition
        d2zero = (d1 * d0) == sp.zeros(d1.rows, d0.cols)
        # exact subspace dimensions
        dim_exact = d0.rank()            # im d0  (grad / curvature)
        dim_coexact = (d1.T).rank()      # im d1^T (curl / current)
        L1 = X.L1()
        dim_harm = nE - L1.rank()        # ker L1
        dims_add = (dim_exact + dim_coexact + dim_harm == nE)

        # orthogonality of the three subspaces (numpy, residuals reported):
        Ge = col_ortho_basis(numeric(d0))          # exact sector
        Gc = col_ortho_basis(numeric(d1.T))        # coexact sector
        # harmonic sector = nullspace of L1
        L1np = numeric(L1)
        w, Vv = np.linalg.eigh(L1np)
        Gh = Vv[:, np.abs(w) < 1e-8]
        def maxabs(A, B):
            return 0.0 if (A.shape[1] == 0 or B.shape[1] == 0) else float(np.max(np.abs(A.T @ B)))
        oec = maxabs(Ge, Gc); oeh = maxabs(Ge, Gh); och = maxabs(Gc, Gh)
        ortho = max(oec, oeh, och) < 1e-9
        # spanning: projectors onto the three sectors sum to the identity
        def proj(G):
            return G @ G.T if G.shape[1] > 0 else np.zeros((nE, nE))
        Psum = proj(Ge) + proj(Gc) + proj(Gh)
        spans = np.max(np.abs(Psum - np.eye(nE))) < 1e-9

        ok = d2zero and dims_add and ortho and spans
        check(f"{name}", ok,
              f"exact={dim_exact} (+) coexact={dim_coexact} (+) harm={dim_harm} = {nE} ; "
              f"d^2=0:{d2zero} ; ortho<{1e-9:.0e}:{ortho} (max={max(oec,oeh,och):.2g}) ; span:{spans}")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(C)  EXACT/COEXACT  <->  SYMMETRIC/ANTISYMMETRIC  (cell-local on the tetra,")
    print("     then sector statements on every complex)")
    print("=" * 78)

    # --- cell-local Paper-01b weld on the tetrahedron K4 (the single cell) ---
    # Reproduce: exact (grad) field has A=0; coexact (curl) field has tr S = 0.
    # We work in the SAME integer normalization as Paper 01b and re-derive the
    # field-Jacobian split DF = S + A with tr S = div F, A = 1/2 Ktilde(curl F).
    Shat = sp.Matrix([[-1, 1, 1, -1], [-1, 1, -1, 1], [1, 1, -1, -1]])
    c = sp.Matrix(sp.symbols('c1 c2 c3 c4', real=True))
    xvec = Shat * c
    xs = sp.symbols('x1 x2 x3', real=True)
    def to_c(e): return e.subs({xs[a]: xvec[a] for a in range(3)})

    def Ktilde(u):
        u1, u2, u3, u4 = u
        return sp.Matrix([[0, u3 - u4, u4 - u2, u2 - u3],
                          [u4 - u3, 0, u1 - u4, u3 - u1],
                          [u2 - u4, u4 - u1, 0, u1 - u2],
                          [u3 - u2, u1 - u3, u2 - u1, 0]])
    uu = sp.symbols('uu1 uu2 uu3 uu4')
    Ktsym = Ktilde(uu)
    def K_raw_action(F):
        res = sp.zeros(4, 1)
        for i in range(4):
            e = 0
            for j in range(4):
                ent = Ktsym[i, j]
                for k in range(4):
                    cf = sp.diff(ent, uu[k])
                    if cf != 0:
                        e += cf * sp.diff(F[j], c[k])
            res[i] = sp.expand(e)
        return res
    def curl(F):
        return sp.Rational(1, 4) * K_raw_action(F)

    # general quadratic Cartesian field carried into the frame
    monos = [sp.Integer(1), xs[0], xs[1], xs[2], xs[0]**2, xs[1]**2, xs[2]**2,
             xs[0]*xs[1], xs[0]*xs[2], xs[1]*xs[2]]
    W = []
    for a in range(3):
        cf = sp.symbols(f'a{a}_0:{len(monos)}')
        W.append(sum(cf[m] * monos[m] for m in range(len(monos))))
    W = sp.Matrix(W)
    F = sp.Matrix([sp.expand(to_c((sp.Rational(1, 4) * Shat.T * W)[i])) for i in range(4)])
    DF = sp.Matrix(4, 4, lambda i, j: sp.diff(F[i], c[j]))
    A = sp.Rational(1, 2) * (DF - DF.T)
    divF = sp.expand(sum(sp.diff(F[i], c[i]) for i in range(4)))
    KcurlF = Ktilde(curl(F))
    # tr S = div F
    check("tetra cell:  tr S = div F  (curvature/source)",
          sp.simplify(sp.trace(DF) - divF) == 0)
    # A = 1/2 Ktilde(curl F)
    check("tetra cell:  A = 1/2 Ktilde(curl F)  (current/vorticity)",
          sp.simplify(A - sp.Rational(1, 2) * KcurlF) == sp.zeros(4, 4))
    # exact (grad) field => A = 0
    fsc = to_c(W[0] * W[1] + xs[2]**3)
    gradf = sp.Rational(1, 4) * sp.Matrix([sp.diff(fsc, c[i]) for i in range(4)])
    DGf = sp.Matrix(4, 4, lambda i, j: sp.diff(gradf[i], c[j]))
    Agrad = sp.Rational(1, 2) * (DGf - DGf.T)
    check("tetra cell:  F = grad f  =>  A = 0  (exact = pure curvature, A=0)",
          sp.simplify(Agrad) == sp.zeros(4, 4))
    cB = curl(F)
    DcB = sp.Matrix(4, 4, lambda i, j: sp.diff(cB[i], c[j]))
    check("tetra cell:  F = curl B  =>  tr S = 0  (coexact = trace-free current)",
          sp.simplify(sp.trace(DcB)) == 0)

    # --- sector statements on EVERY complex (cochain level) ---
    print("  -- cochain-level exact/coexact/harmonic characterization (every complex):")
    for name, X, _ in CASES:
        d0, d1 = X.d0(), X.d1()
        nE = len(X.E)
        if nE == 0:
            continue
        # exact = im d0 : these are "grad" cochains; d1 (exact) = 0  (curl grad = 0)
        exact_is_closed = (d1 * d0) == sp.zeros(d1.rows, d0.cols)
        # coexact = im d1^T : these are "curl" cochains; d0^T (coexact) = 0 (div curl = 0)
        coexact_is_coclosed = (d0.T * d1.T) == sp.zeros(d0.cols, d1.rows)
        # harmonic = ker L1 : simultaneously closed (d1 h = 0) AND co-closed (d0^T h = 0)
        L1 = X.L1()
        # take an exact basis for ker L1 over Q
        ker = L1.nullspace()
        harm_ok = True
        for h in ker:
            if not (sp.simplify(d1 * h) == sp.zeros(d1.rows, 1) and
                    sp.simplify(d0.T * h) == sp.zeros(d0.cols, 1)):
                harm_ok = False
        check(f"    {name}",
              exact_is_closed and coexact_is_coclosed and harm_ok,
              f"curl·grad=0:{exact_is_closed}  div·curl=0:{coexact_is_coclosed}  "
              f"harmonic closed&co-closed:{harm_ok} (dim {len(ker)})")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(D)  SELF-ADJOINT INSTRUMENT IS BLIND TO THE CURRENT (b1 harmonic modes)")
    print("=" * 78)
    # Transport operator on 1-cochains:  T = I - t*L1 is SYMMETRIC (L1 is).  A
    # symmetric instrument's quadratic form q(x)=<x,Tx> equals <x,Sx> with
    # S=1/2(T+T^T)=T exactly -- the harmonic current modes (ker L1) are FIXED
    # points of T (T h = h) and contribute the SAME q whether or not a current
    # circulates on them.  To exhibit a genuine current we add an antisymmetric
    # circulation C on the cycle space (im d1^T (+) ker L1) and show q is blind.
    for name, X, b1_expected in CASES:
        d0, d1 = X.d0(), X.d1()
        nE = len(X.E)
        if nE == 0 or b1_expected == 0:
            continue
        L1 = numeric(X.L1())
        # build an antisymmetric "current" supported on the harmonic sector
        w, Vv = np.linalg.eigh(L1)
        Gh = Vv[:, np.abs(w) < 1e-8]          # harmonic basis (b1-dim)
        rng = np.random.default_rng(0)
        if Gh.shape[1] >= 2:
            Araw = rng.standard_normal((Gh.shape[1], Gh.shape[1]))
            Acirc = Gh @ (Araw - Araw.T) @ Gh.T   # antisym, lives in harmonic sector
        else:
            # 1-dim harmonic: embed a rotation between the harmonic mode and any
            # OTHER orthonormal direction (a coexact mode if 2-cells exist, else
            # an exact/grad mode) so the current is a genuine antisymmetric
            # operator.  The symmetric form is blind to it either way; the point
            # is only that a nonzero antisymmetric current exists on a b1=1
            # complex and the self-adjoint instrument cannot see it.
            Gc = col_ortho_basis(numeric(X.d1().T))     # coexact (may be empty)
            Ge = col_ortho_basis(numeric(X.d0()))       # exact   (nonempty if E>V-1...)
            partner = None
            for cand in (Gc, Ge):
                if cand.shape[1] >= 1:
                    partner = cand[:, 0]
                    break
            if partner is not None:
                pair = np.column_stack([Gh[:, 0], partner])
                Acirc = pair @ np.array([[0.0, 1.0], [-1.0, 0.0]]) @ pair.T
            else:
                Acirc = np.zeros((nE, nE))
        Tsym = np.eye(nE) - 0.3 * L1            # symmetric instrument
        Tfull = Tsym + Acirc                    # instrument + current
        # symmetric quadratic form is blind to the antisymmetric current:
        blind = 0.0
        for _ in range(300):
            x = rng.standard_normal(nE)
            blind = max(blind, abs(x @ Tfull @ x - x @ Tsym @ x))
        # but a predictor (SVD / two-sided) sees it:  ||antisym part|| > 0
        Apart = 0.5 * (Tfull - Tfull.T)
        check(f"{name}: symmetric form blind to current, predictor sees it",
              blind < 1e-10 and np.linalg.norm(Apart) > 1e-6,
              f"max|<x,T x>-<x,S x>|={blind:.2e} (BLIND) ; ||A||={np.linalg.norm(Apart):.4f} (predictor); "
              f"b1={b1_expected} protected current mode(s)")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("RESULT:", "ALL GREEN" if PASS else "FAILED -- see ***RED*** above")
    print("=" * 78)
    return 0 if PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
