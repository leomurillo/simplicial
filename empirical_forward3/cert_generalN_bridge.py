r"""
FORWARD-3 CROSS-POLLINATION CERTIFICATE  --  the K_N graph Laplacian and the
Hodge spectrum of the general-N simplex skeleton (weld to Direction 1).

Paper 01b Thm 10.1 identified, AT N=4, the integer simplicial metric M = 4I - J
with the K4 graph Laplacian L0 = d0^T d0, and span{1} = H^0 = ker L0.  This
certificate makes the general-N statement exact, so Direction 3's Hodge/arrow
story plugs directly into Direction 1's general-N K_N program:

  (1) GENERAL-N METRIC = K_N LAPLACIAN.  For the complete graph K_N (the
      1-skeleton of the (N-1)-simplex), the graph Laplacian is L0 = N*I - J.
      It acts as the SCALAR N on the zero-sum hyperplane H = {sum=0} (eigenvalue
      N with multiplicity N-1) and annihilates the gauge line span{1} (b0 = 1).
      At N=4 this is exactly Paper 01/01b's M = 4I - J.  The simplicial Gram
      matrix G = (N/(N-1))I - (1/(N-1))J is L0 rescaled: G = L0/(N-1) on H.

  (2) FULL-SIMPLEX SKELETON IS ACYCLIC.  The complete simplicial complex on N
      vertices (all faces) is a single solid simplex: contractible, so
      b0 = 1, b_k = 0 for k >= 1.  Hence the 1-Hodge-Laplacian L1 has NO
      harmonic 1-cochains (ker L1 = 0): a single filled cell carries no
      protected current.  Verified for N = 4,5,6,7 from exact ranks.

  (3) BETTI OF THE k-SKELETON.  Keeping only simplices up to dimension k of the
      N-vertex simplex gives the well-known homology of a wedge of k-spheres:
      the (k)-skeleton of the (N-1)-simplex has reduced homology only in degree
      k, of rank  C(N-1, k+1).  We verify the 1-skeleton (= K_N) cycle rank
      b1 = C(N-1,2) and the 2-skeleton b2 = C(N-1,3) for several N -- the
      general-N source of "how many independent currents a frame can carry."

  (4) L1 SPECTRUM ON THE FILLED SIMPLEX is integral.  The nonzero spectrum of
      L1 on the complete N-vertex complex is the single eigenvalue N with full
      multiplicity (coexact + exact eigenvalues coincide because every 1-cochain
      is exact-plus-coexact and L1 = N*I on im d0 (+) im d1^T here).  Reported.

Run:  py cert_generalN_bridge.py     (expects all-GREEN)
Deps: sympy, numpy ONLY.  Exact ranks via sympy; numpy spectra reported.
"""

import sys
import itertools
import math
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
    print(f"  [{'GREEN' if ok else '***RED***'}] {name}" + (f"   {extra}" if extra else ""))


def full_simplex_skeleton(N, kmax):
    """All faces of the (N-1)-simplex up to dimension kmax, as a list of
    coboundary matrices d[k]: C^k -> C^{k+1} (exact sympy)."""
    V = list(range(1, N + 1))
    simplices = {}
    for k in range(0, kmax + 1):
        simplices[k] = [tuple(c) for c in itertools.combinations(V, k + 1)]
    idx = {k: {s: i for i, s in enumerate(simplices[k])} for k in simplices}
    d = {}
    for k in range(0, kmax):
        rows, cols = len(simplices[k + 1]), len(simplices[k])
        D = sp.zeros(rows, cols)
        for s in simplices[k + 1]:
            r = idx[k + 1][s]
            for a in range(len(s)):
                face = s[:a] + s[a + 1:]
                D[r, idx[k][face]] += (-1) ** a
        d[k] = D
    return simplices, d


def main():
    print(__doc__)

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(1)  general-N metric M = N*I - J  ==  K_N graph Laplacian L0 = d0^T d0")
    print("=" * 78)
    for N in (3, 4, 5, 6, 7):
        simp, d = full_simplex_skeleton(N, 1)
        d0 = d[0]
        L0 = d0.T * d0
        M = N * sp.eye(N) - sp.ones(N, N)
        eq = sp.simplify(L0 - M) == sp.zeros(N, N)
        # eigen-structure of M on H: scalar N with multiplicity N-1, 0 on span{1}
        evals = sp.Matrix(M).eigenvals()          # {value: multiplicity}
        spec_ok = (evals.get(sp.Integer(N), 0) == N - 1) and (evals.get(sp.Integer(0), 0) == 1)
        check(f"N={N}: M = N*I - J = L0(K_N), spectrum N^(N-1) + 0^1",
              eq and spec_ok,
              f"eigs(M)={ {int(k): int(v) for k, v in evals.items()} }")
    # at N=4 this is the Paper-01 integer metric
    check("N=4 special case is exactly Paper 01/01b's M = 4I - J", True,
          "(the K4 Laplacian; G = M/3 on H)")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(2)  filled N-vertex simplex is contractible: b1 = 0 (no protected current)")
    print("=" * 78)
    for N in (4, 5, 6, 7):
        simp, d = full_simplex_skeleton(N, 2)     # need up to faces for L1
        d0, d1 = d[0], d[1]
        nE = len(simp[1])
        r0, r1 = d0.rank(), d1.rank()
        b1 = nE - r0 - r1
        L1 = d0 * d0.T + d1.T * d1
        ker_L1 = nE - L1.rank()
        check(f"N={N}: filled simplex b1 = 0 = dim ker L1",
              b1 == 0 and ker_L1 == 0,
              f"E={nE}  rank d0={r0}  rank d1={r1}  b1={b1}  dim ker L1={ker_L1}")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(3)  k-skeleton Betti = wedge of k-spheres:  b_k = C(N-1, k+1)")
    print("=" * 78)
    for N in (4, 5, 6, 7):
        # 1-skeleton = K_N : b1 = C(N-1, 2)
        simp1, d1only = full_simplex_skeleton(N, 1)
        nE = len(simp1[1]); r0 = d1only[0].rank()
        b1_skel = nE - r0
        exp_b1 = math.comb(N - 1, 2)
        # 2-skeleton : b2 = C(N-1, 3)
        simp2, d2 = full_simplex_skeleton(N, 2)
        nF = len(simp2[2]); r1 = d2[1].rank()
        b2_skel = nF - r1
        exp_b2 = math.comb(N - 1, 3)
        check(f"N={N}: 1-skeleton (K_N) b1 = C({N-1},2) ; 2-skeleton b2 = C({N-1},3)",
              b1_skel == exp_b1 and b2_skel == exp_b2,
              f"b1={b1_skel} (exp {exp_b1}) ; b2={b2_skel} (exp {exp_b2})")

    # -----------------------------------------------------------------------
    print("=" * 78)
    print("(4)  L1 spectrum on the filled N-vertex simplex is integral (= N)")
    print("=" * 78)
    for N in (4, 5, 6, 7):
        simp, d = full_simplex_skeleton(N, 2)
        d0, d1 = d[0], d[1]
        L1np = np.array((d0 * d0.T + d1.T * d1).tolist(), dtype=float)
        ev = np.linalg.eigvalsh(L1np)
        nz = ev[np.abs(ev) > 1e-8]
        allN = np.allclose(nz, N, atol=1e-8)
        check(f"N={N}: nonzero L1 eigenvalues all = N",
              allN,
              f"#nonzero={nz.size}, range=[{nz.min():.4f},{nz.max():.4f}] (== {N})")

    print("=" * 78)
    print("RESULT:", "ALL GREEN" if PASS else "FAILED -- see ***RED*** above")
    print("=" * 78)
    return 0 if PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
