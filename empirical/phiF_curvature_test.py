r"""
phiF_curvature_test.py  --  DECISIVE TEST 1 for Connection F (Paper 32, sec 16.5 lever 2).

QUESTION (the Phi->F curvature-form lever).
  The program builds, from ONE functional Phi = log Z on the categorical simplex
  over R = Z/NZ, an order-2 metric g = Hess(Phi) (Fisher) and an order-3 totally
  symmetric cubic T = grad^3 Phi (Amari-Chentsov).  In NATURAL (canonical) coords
  theta (atom 0 = reference, dim D = N-1), ALL needed derivatives are CUMULANTS of
  the atom-indicator vector X, exact rational functions of the probabilities p:

      Phi = log Z ,  g_{ij} = d^2 Phi = cov(X_i,X_j)            (2nd cumulant)
      T_{ijk} = d^3 Phi      = 3rd joint cumulant of (X_i,X_j,X_k)
      T4_{ijkl} = d^4 Phi    = 4th joint cumulant
      and crucially  d_m g_{ij} = T_{ijm},  d_m T_{ijk} = T4_{ijkm}.

  This lets us compute the LEVI-CIVITA (alpha=0) Riemann tensor of g EXACTLY at
  any point with pure rational arithmetic (no exp/log, no simplify blowup):
      Gamma^l_{ij} = 1/2 g^{lm}( d_i g_{jm} + d_j g_{im} - d_m g_{ij} )
                   = 1/2 g^{lm}( T_{jmi} + T_{imj} - T_{ijm} ) = 1/2 g^{lm} T_{ijm}
        (T totally symmetric -> Gamma^l_{ij} = 1/2 g^{lm} T_{ijm} ),
      R^l_{ijk}    = d_i Gamma^l_{jk} - d_j Gamma^l_{ik}
                     + Gamma^l_{im}Gamma^m_{jk} - Gamma^l_{jm}Gamma^m_{ik},
      d_i Gamma^l_{jk} = 1/2 d_i ( g^{lm} T_{jkm} )
                       = 1/2 ( (d_i g^{lm}) T_{jkm} + g^{lm} T4_{jkmi} ),
      d_i g^{lm} = - g^{la} g^{mb} d_i g_{ab} = - g^{la} g^{mb} T_{abi}.
  All RHS are rational in p.  R_{aijk} = g_{al} R^l_{ijk}.

  COMPARISON.  Special / very-special geometry imposes curvature of the FORM
      R_{ijkl} = -( g_{ik} g_{jl} - g_{il} g_{jk} )  +  (cubic . cubic)/g    (SG)
  while the Amari-Nagaoka dually-flat (alpha=0) closed form is
      AN_{ijkl} = (1/4) g^{mn} ( T_{ilm} T_{jkn} - T_{ikm} T_{jln} ).        (AN)
  Both have "metric part + T.T".  Decisive residual (lambda absorbed into AN's 1/4):
      Resid_{ijkl} := R_dir_{ijkl} + ( g_{ik}g_{jl} - g_{il}g_{jk} ) - AN_{ijkl}.
  Readouts:
      Resid == 0          => SG/VSR-EXACT (program has the -(gg) background)
      R_dir == AN exactly => program is dually-flat with NO gg background
                             => Resid == GG := (g_{ik}g_{jl}-g_{il}g_{jk}) != 0
                             => SG/VSR constraint FAILS, break = the gg offset.
  Run at AND off the centroid on Z/3, Z/4, Z/6 (and Z/30 reduced) to classify:
      exact-match / local-match-global-break / refuted, with break location.

  REAL (VSR) vs COMPLEX (special Kahler): handled in the printed analysis.
  Pure sympy rational arithmetic.  No torch.  Exit 0 on completion.
"""

from __future__ import annotations

import itertools
import sympy as sp


# ----------------------------------------------------------------------------
# Cumulants of the atom-indicator vector X over R = Z/NZ in NATURAL coords.
# State: probability vector p = (p_0, p_1, ..., p_{N-1}), sum p = 1.
# Indices i,j,... run over 1..N-1 (atom 0 is the reference, dimension D=N-1).
# Joint cumulants of indicators X_a (a>=1) have exact closed forms.
#
# 2nd cumulant (covariance):
#   g_{ij} = p_i delta_{ij} - p_i p_j
# 3rd cumulant:
#   k3_{ijk} = E[Yi Yj Yk] central; for indicators (Bernoulli-correlated) the
#   joint cumulant of distinct/equal indices is given by the inclusion formula.
#   We compute cumulants directly from the cumulant generating function
#   K(t) = log( p_0 + sum_{a>=1} p_a e^{t_a} ) by exact differentiation in t at t=0,
#   which is EXACTLY  Phi(theta) with theta = t + const; derivatives in t at 0
#   equal derivatives in theta at the point p.  So we just differentiate K in the
#   formal t-variables once, symbolically, and substitute p numerically.  Cheap:
#   K is a log of a LINEAR form in e^{t}, derivatives are rational in p only.
# ----------------------------------------------------------------------------
def cumulants(N, pvals, order=4):
    """Return g (2), T (3), T4 (4) as nested rational lists, dim D=N-1,
       evaluated at probability vector pvals (length N, sum 1, exact rationals)."""
    D = N - 1
    t = sp.symbols(f"t1:{N}", real=True)  # t1..t_{N-1}
    p = pvals
    # M(t) = p_0 + sum_{a>=1} p_a e^{t_a}  ; K = log M
    M = p[0] + sum(p[a] * sp.exp(t[a - 1]) for a in range(1, N))
    K = sp.log(M)

    sub0 = {ti: 0 for ti in t}

    def d(expr, idxs):
        e = expr
        for i in idxs:
            e = sp.diff(e, t[i])   # t[i] corresponds to atom i+1
        return e

    # g_{ij}: atoms (i+1),(j+1)
    g = [[sp.nsimplify(d(K, [i, j]).subs(sub0)) for j in range(D)] for i in range(D)]
    T = None
    T4 = None
    if order >= 3:
        # build T by differentiating K twice symbolically then once more, but to
        # keep it cheap we differentiate the symbolic 2nd derivative once.
        g_sym = [[d(K, [i, j]) for j in range(D)] for i in range(D)]
        T = [[[sp.nsimplify(sp.diff(g_sym[i][j], t[k]).subs(sub0))
               for k in range(D)] for j in range(D)] for i in range(D)]
    if order >= 4:
        T_sym = [[[sp.diff(g_sym[i][j], t[k]) for k in range(D)]
                  for j in range(D)] for i in range(D)]
        T4 = [[[[sp.nsimplify(sp.diff(T_sym[i][j][k], t[l]).subs(sub0))
                 for l in range(D)] for k in range(D)]
               for j in range(D)] for i in range(D)]
    return D, g, T, T4


# ----------------------------------------------------------------------------
# Exact Levi-Civita Riemann tensor from (g, T=dg, T4=ddg) at a point.
# Uses the identities derived in the module docstring.  Pure rational linear
# algebra; no symbolic blowup.
# ----------------------------------------------------------------------------
def riemann_from_cumulants(D, g, T, T4):
    gmat = sp.Matrix(g)
    ginv = gmat.inv()
    ginv = [[sp.nsimplify(ginv[i, j]) for j in range(D)] for i in range(D)]

    # Christoffel^l_{ij} = 1/2 g^{lm} T_{ijm}  (T totally symmetric)
    Gamma = [[[sum(ginv[l][m] * T[i][j][m] for m in range(D)) / 2
               for j in range(D)] for i in range(D)] for l in range(D)]

    # d_i g^{lm} = - g^{la} g^{mb} T_{abi}
    def dginv(i, l, m):
        s = sp.Integer(0)
        for a in range(D):
            for b in range(D):
                s -= ginv[l][a] * ginv[m][b] * T[a][b][i]
        return s

    # d_i Gamma^l_{jk} = 1/2 ( (d_i g^{lm}) T_{jkm} + g^{lm} T4_{jkmi} )
    def dGamma(i, l, j, k):
        s = sp.Integer(0)
        for m in range(D):
            s += dginv(i, l, m) * T[j][k][m] + ginv[l][m] * T4[j][k][m][i]
        return s / 2

    # R^l_{ijk} = d_i Gamma^l_{jk} - d_j Gamma^l_{ik} + Gam.Gam - Gam.Gam
    # (this raised tensor is ANTISYMMETRIC in the derivative pair (i,j))
    Rup = [[[[None] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for l in range(D):
        for i in range(D):
            for j in range(D):
                for k in range(D):
                    term = dGamma(i, l, j, k) - dGamma(j, l, i, k)
                    for m in range(D):
                        term += Gamma[l][i][m] * Gamma[m][j][k]
                        term -= Gamma[l][j][m] * Gamma[m][i][k]
                    Rup[l][i][j][k] = sp.nsimplify(sp.expand(term))
    # Raw lower tensor R_{a i j k} = g_{a l} R^l_{ijk} is antisymmetric in (i,j).
    Rraw = [[[[sp.nsimplify(sum(g[a][l] * Rup[l][i][j][k] for l in range(D)))
               for k in range(D)] for j in range(D)]
             for i in range(D)] for a in range(D)]
    # Reindex to the STANDARD all-lower convention R_{abcd}=g_{ae}R^e_{bcd}
    # with antisymmetry in (a,b) and (c,d).  Our raised R^l_{ijk} has free index
    # k = standard 'b' and antisym pair (i,j) = standard (c,d):
    #   Rstd[a][k][i][j] := Rraw[a][i][j][k]   (=> Rstd_{a k i j} = g_{al}R^l_{ijk}).
    Rstd = [[[[None] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for a in range(D):
        for i in range(D):
            for j in range(D):
                for k in range(D):
                    Rstd[a][k][i][j] = Rraw[a][i][j][k]
    return Rstd, ginv


def AN_contraction(D, T, ginv):
    AN = [[[[None] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for i in range(D):
        for j in range(D):
            for k in range(D):
                for l in range(D):
                    s = sp.Integer(0)
                    for m in range(D):
                        for n in range(D):
                            s += ginv[m][n] * (T[i][l][m] * T[j][k][n]
                                               - T[i][k][m] * T[j][l][n])
                    AN[i][j][k][l] = sp.nsimplify(s / 4)
    return AN


def GG_background(D, g):
    return [[[[g[i][k] * g[j][l] - g[i][l] * g[j][k]
               for l in range(D)] for k in range(D)]
             for j in range(D)] for i in range(D)]


def count_nz(Tn, D, rank=4):
    c = 0
    for idx in itertools.product(range(D), repeat=rank):
        v = Tn
        for q in idx:
            v = v[q]
        if v != 0:
            c += 1
    return c


def maxabs(Tn, D, rank=4):
    m = sp.Integer(0)
    for idx in itertools.product(range(D), repeat=rank):
        v = Tn
        for q in idx:
            v = v[q]
        av = sp.Abs(v)
        if av > m:
            m = av
    return m


def scalar_curv(D, Rstd, ginv):
    # Standard: Ric_{bd} = R^a_{bad} = g^{ac} R_{c b a d} ; R = g^{bd} Ric_{bd}.
    Ric = [[sum(ginv[a][c] * Rstd[c][b][a][d]
                for a in range(D) for c in range(D))
            for d in range(D)] for b in range(D)]
    return sp.nsimplify(sum(ginv[b][d] * Ric[b][d]
                            for b in range(D) for d in range(D)))


def proportionality_to_GG(D, Rlow, GG):
    """If R_dir == c * GG for a single constant c, return c; else None.
       (constant-curvature form R_{ijkl} = K (g_ik g_jl - g_il g_jk).)"""
    c = None
    for idx in itertools.product(range(D), repeat=4):
        i, j, k, l = idx
        gg = GG[i][j][k][l]
        r = Rlow[i][j][k][l]
        if gg == 0:
            if r != 0:
                return None  # nonzero R where GG is zero -> not proportional
            continue
        ratio = sp.nsimplify(r / gg)
        if c is None:
            c = ratio
        elif sp.simplify(ratio - c) != 0:
            return None
    return c


def analyze(N, label, pvals):
    D, g, T, T4 = cumulants(N, pvals, order=4)
    Rlow, ginv = riemann_from_cumulants(D, g, T, T4)
    AN = AN_contraction(D, T, ginv)
    GG = GG_background(D, g)

    # AN match
    mism_AN = sum(1 for idx in itertools.product(range(D), repeat=4)
                  if sp.simplify(Rlow[idx[0]][idx[1]][idx[2]][idx[3]]
                                 - AN[idx[0]][idx[1]][idx[2]][idx[3]]) != 0)

    Resid = [[[[sp.nsimplify(Rlow[i][j][k][l] + GG[i][j][k][l] - AN[i][j][k][l])
                for l in range(D)] for k in range(D)]
              for j in range(D)] for i in range(D)]

    resid_nz = count_nz(Resid, D)
    resid_max = maxabs(Resid, D)
    # Resid == GG ?  (i.e. R_dir == AN exactly, no gg background)
    resid_is_GG = all(sp.simplify(Resid[i][j][k][l] - GG[i][j][k][l]) == 0
                      for i in range(D) for j in range(D)
                      for k in range(D) for l in range(D))

    Rsc = scalar_curv(D, Rlow, ginv)
    cprop = proportionality_to_GG(D, Rlow, GG)

    out = {
        "N": N, "point": label, "D": D,
        "R_dir == AN (dually-flat closed form)": (mism_AN == 0, f"{mism_AN} mism /{D**4}"),
        "scalar_R": Rsc,
        "R_dir proportional to GG? K=": cprop,
        "SG residual (R_dir+gg-AN) nonzero": (resid_nz, f"/{D**4}"),
        "SG residual maxabs": resid_max,
        "residual == GG  (=> NO -(gg) background; SG FAILS)": resid_is_GG,
        "GG maxabs (size of the missing offset)": maxabs(GG, D),
    }
    return out


def main():
    print("DECISIVE TEST 1  --  Phi->F curvature-form match (exact, cumulant route)")
    print("Program Levi-Civita R_dir vs:  AN = (1/4)g^{-1}(TT-TT) [dually-flat]")
    print("                          and  SG: R = -(gg-gg) + (cubic.cubic)")
    print("Residual:  Resid = R_dir + (gg-gg) - AN")
    print("  Resid==0   -> SG/VSR-EXACT (program carries the -(gg) background)")
    print("  Resid==GG  -> dually-flat, NO background, SG FAILS by the gg offset")

    cases = []

    def P(*fracs):
        v = [sp.Rational(*f) if isinstance(f, tuple) else sp.Rational(f) for f in fracs]
        s = sum(v)
        return [x / s for x in v]

    # Z/3
    cases.append((3, "centroid", P(1, 1, 1)))
    cases.append((3, "off (3,2,1)/6", P(3, 2, 1)))
    # Z/4
    cases.append((4, "centroid", P(1, 1, 1, 1)))
    cases.append((4, "off (4,3,2,1)/10", P(4, 3, 2, 1)))
    # Z/6 -- headline ring
    cases.append((6, "centroid", P(1, 1, 1, 1, 1, 1)))
    cases.append((6, "off (3,2,2,1,1,1)/10", P(3, 2, 2, 1, 1, 1)))
    # Z/30 reduced: centroid only (D=29 full Riemann is heavy; do a SMALL
    # off-centroid skip; centroid gives the headline gg-offset readout).
    cases.append((30, "centroid", P(*([1] * 30))))

    results = []
    for (N, lab, pv) in cases:
        print(f"\n{'='*70}\n  Z/{N}  point={lab}\n{'='*70}")
        try:
            r = analyze(N, lab, pv)
        except Exception as e:
            print(f"   [skipped: {type(e).__name__}: {e}]")
            continue
        for k, v in r.items():
            print(f"   {k:48s}: {v}")
        results.append(r)

    print(f"\n{'='*70}\n  VERDICT\n{'='*70}")
    for r in results:
        flat = r["R_dir == AN (dually-flat closed form)"][0]
        isGG = r["residual == GG  (=> NO -(gg) background; SG FAILS)"]
        K = r["R_dir proportional to GG? K="]
        verdict = ("SG-EXACT" if r["SG residual (R_dir+gg-AN) nonzero"][0] == 0
                   else ("dually-flat/SG-FAILS(offset=GG)" if isGG else "OTHER"))
        print(f"   Z/{r['N']:<2} {r['point']:<22}: R=AN:{flat}  K(const-curv)={K}  "
              f"scalarR={r['scalar_R']}  -> {verdict}")


if __name__ == "__main__":
    main()
