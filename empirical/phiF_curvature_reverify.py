#!/usr/bin/env python
"""
Independent re-verify of the curvature result behind Connection F Remark 16.2b.

Goal (exact, rational arithmetic; numpy/sympy only, NO torch):
  For the categorical exponential family Phi = log Z on Z/N, in mixture
  coordinates p_1..p_{N-1} (p_N = 1 - sum), with
      Fisher metric         g_ij = delta_ij/p_i + 1/p_N
      Amari-Chentsov cubic  C_ijk = d^3(dual potential) = 1/p_N^2 - [i=j=k]/p_i^2
  verify, at the CENTROID and at a generic OFF-CENTROID rational point, for
  N in {3,4,5,6}:
    (A) constant curvature:  R_ijkl = (1/4)(g_ik g_jl - g_il g_jk)   => K = 1/4
    (B) R = AN:              R_ijkl = (1/4) g^{mn}(C_ikm C_jln - C_ilm C_jkn)
    (C) scalar curvature  = D(D-1)/4
    (D) the cubic FLOWS:    C(centroid) != C(off-centroid)   (the jerk obstruction)

(A)+(C) are the special-geometry/VSR "background" term; (B) is the literal
curvature=cubic-contraction identity; (D) is the named global obstruction.
This is an independent reimplementation of the result recovered from the
interrupted curvature run (agent a2f90), not a rerun of its code.
"""
import sympy as sp
import time, sys

def check_N(N, pvals, label):
    D = N - 1
    p = sp.symbols(f'p0:{D}', positive=True)
    pN = 1 - sum(p)
    g = sp.Matrix(D, D, lambda i, j: (1/p[i] if i == j else sp.Integer(0)) + 1/pN)
    ginv = sp.Matrix(D, D, lambda i, j: (p[i] if i == j else sp.Integer(0)) - p[i]*p[j])

    def C(i, j, k):
        return 1/pN**2 - ((1/p[i]**2) if (i == j == k) else sp.Integer(0))

    # Christoffel ^i_{jk} with closed-form inverse (no premature simplify)
    dg = [[[sp.diff(g[a, b], p[c]) for c in range(D)] for b in range(D)] for a in range(D)]
    Gam = [[[sum(ginv[i, m]*(dg[m][k][j] + dg[m][j][k] - dg[j][k][m]) for m in range(D))/2
             for k in range(D)] for j in range(D)] for i in range(D)]

    def Rup(i, j, k, l):  # R^i_{jkl}
        t = sp.diff(Gam[i][l][j], p[k]) - sp.diff(Gam[i][k][j], p[l])
        t += sum(Gam[i][k][m]*Gam[m][l][j] - Gam[i][l][m]*Gam[m][k][j] for m in range(D))
        return t

    subs = {p[i]: pvals[i] for i in range(D)}
    gv = g.subs(subs)
    giv = ginv.subs(subs)
    assert (gv*giv) == sp.eye(D), "closed-form inverse check failed"
    Cv = {(i, j, k): C(i, j, k).subs(subs) for i in range(D) for j in range(D) for k in range(D)}

    R = {}
    for i in range(D):
        for j in range(D):
            for k in range(D):
                for l in range(D):
                    R[(i, j, k, l)] = sp.together(sum(g[i, m]*Rup(m, j, k, l) for m in range(D)).subs(subs))

    K = sp.Rational(1, 4)
    okGG = all(sp.simplify(R[(i, j, k, l)] - K*(gv[i, k]*gv[j, l] - gv[i, l]*gv[j, k])) == 0
               for i in range(D) for j in range(D) for k in range(D) for l in range(D))

    def AN(i, j, k, l):
        # dually-flat (Amari-Nagaoka) curvature-from-cubic, standard sign:
        # R_ijkl = (1/4) g^{mn}(C_ilm C_jkn - C_ikm C_jln)
        return K*sum(giv[m, n]*(Cv[(i, l, m)]*Cv[(j, k, n)] - Cv[(i, k, m)]*Cv[(j, l, n)])
                     for m in range(D) for n in range(D))
    okAN = all(sp.simplify(R[(i, j, k, l)] - AN(i, j, k, l)) == 0
               for i in range(D) for j in range(D) for k in range(D) for l in range(D))

    Ric = sp.Matrix(D, D, lambda j, l: sum(giv[i, k]*R[(i, j, k, l)] for i in range(D) for k in range(D)))
    scal = sp.simplify(sum(giv[j, l]*Ric[j, l] for j in range(D) for l in range(D)))
    okScal = (scal == sp.Rational(D*(D-1), 4))
    return okGG, okAN, scal, okScal

def cubic_flows(N):
    D = N - 1
    cen = [sp.Rational(1, N)]*D
    T = N*(N+1)//2
    off = [sp.Rational(i+1, T) for i in range(D)]
    def Cval(pv):
        pN = 1 - sum(pv)
        return {(i, j, k): 1/pN**2 - ((1/pv[i]**2) if (i == j == k) else 0)
                for i in range(D) for j in range(D) for k in range(D)}
    return Cval(cen) != Cval(off)

print("=== Re-verify of Remark 16.2b: R = AN, K=1/4, scalar=D(D-1)/4, cubic flows ===")
allok = True
for N in [3, 4, 5, 6]:
    D = N - 1
    t0 = time.time()
    cen = [sp.Rational(1, N)]*D
    T = N*(N+1)//2
    off = [sp.Rational(i+1, T) for i in range(D)]
    try:
        for nm, pv in [("centroid", cen), ("off-centroid", off)]:
            okGG, okAN, scal, okScal = check_N(N, pv, nm)
            ok = okGG and okAN and okScal
            allok = allok and ok
            print(f"N={N} D={D} {nm:13s}: R==(1/4)(gg-gg)? {okGG}  R==AN? {okAN}  "
                  f"scalar={scal} (target {sp.Rational(D*(D-1),4)}) {okScal}  [{'PASS' if ok else 'FAIL'}]")
        cf = cubic_flows(N)
        allok = allok and cf
        print(f"N={N}            cubic flows (C_centroid != C_off)? {cf}   ({time.time()-t0:.1f}s)")
    except Exception as e:
        print(f"N={N}: ERROR {e}")
        allok = False
    sys.stdout.flush()

print("\nOVERALL:", "PASS - Remark 16.2b verified independently" if allok else "FAIL")
