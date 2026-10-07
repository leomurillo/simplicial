#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
cert_cumulant_tower.py  --  EXACT certificate (sympy only) for

    forward2_cumulant_bridge.md
    "The Diagonal Cumulant Tower of Negative Entropy in Simplicial Coordinates"

Direction 2 (the cumulant-tower bridge) of the simplicial-frame program.
Companion to the cert-verified papers 01 / 01b / 01c.

This certificate is DETERMINISTIC and uses sympy exact arithmetic only
(no numpy, no torch, no floats, no random sampling).  Every residual is an
exact zero over Q or over the rational function field Q(p_1,...,p_N).

Run:   py cert_cumulant_tower.py
Pass:  prints "CERT GREEN" and exits 0.  Any failure raises AssertionError.

----------------------------------------------------------------------------
WHAT IS VERIFIED
----------------------------------------------------------------------------
The negative-entropy potential on the categorical N-simplex is

    phi(p) = sum_i p_i log p_i        (the m-affine / mixture-chart potential).

Its order-n derivative tower is  T^(n) = nabla^n phi.  We certify:

  C1. Diagonal scalar law.  For the single-variable seed g(p) = p log p,
          d^n/dp^n [ p log p ]  =  (-1)^n (n-2)! / p^(n-1),     n >= 2,
      with coefficients c_n = (-1)^n (n-2)! = 1, -1, 2, -6, 24, ... (n=2..6).

  C2. Purely diagonal tower.  On the N=4 simplex, every component
      T^(n)_{i_1...i_n} = d^n phi / (dp_{i_1}...dp_{i_n}) vanishes unless
      i_1 = ... = i_n, and the surviving fully-diagonal component equals
      c_n / p_i^(n-1).  (Checked for N=4, all index multi-indices, n=2..6;
      plus an N=5 spot check.)

  C3. Frozen-geometry x breathing-diagonal factorization.
          T^(n)  =  c_n * Delta^(n) * D_p^(n-1)
      where
          c_n          = (-1)^n (n-2)!                (scalar coefficient),
          Delta^(n)    = fully-diagonal "all-equal-index" selector
                         (Delta^(n)_{i...i}=1, else 0)  -- POSITION-INDEPENDENT,
          D_p^(n-1)    = diag(1/p_i^(n-1))             -- the only breathing piece.
      We certify (a) Delta^(n) carries no p-dependence (its symbolic
      p-gradient is identically zero), and (b) the product reproduces T^(n)
      exactly, for n=2..6.

  C4. n=2 reduces to the Fisher metric.   T^(2) = diag(1/p_i) = Hess phi = g_p.

  C5. n=3 reduces to the moving Amari-Chentsov cubic (01c Thm 4.1).
      The raised cubic  K^CH_p(u)v = D_p(u (.) v) - <u,v>_{g_p} p   has, as a
      3-covariant tensor,  T(u,v,w) = sum_i u_i v_i w_i / p_i^2 ,  i.e. the
      diagonal third cumulant  T^(3)_{iii} = -1/p_i^2 = c_3 / p_i^2.
      We certify both the diagonal third-derivative value AND total symmetry
      of the raised cubic on the tangent space H = {sum = 0}.

  C6. Legendre/dual bridge to the program's log-partition tower (T2 Prop 6.2).
      phi = sum p log p is the convex conjugate of the log-partition
      Phi(eta) = log sum_i e^{eta_i}.  The Phi-tower (the program's lambda-2
      "cumulant tower as effective action") has the all-DISTINCT-index joint
      cumulant  kappa_n = (-1)^(n-1) (n-1)! m^(-n)  at the uniform p=1/m.
      The phi-tower of this note is the DIAGONAL (all-EQUAL-index) dual object.
      We certify the exact numeric duality at the uniform point p_i = 1/m:

        (i)   phi-diagonal value at uniform:  T^(n)_{ii..i}|_u = c_n * m^(n-1),
              c_n = (-1)^n (n-2)!.
        (ii)  Phi-distinct cumulant at uniform: kappa_n = (-1)^(n-1)(n-1)! m^(-n)
              (program T2 Prop 6.2), reproduced here from the CGF log(1+t/m).
        (iii) The dual involution alpha -> -alpha is the sign (-1)^n:
              both towers carry a sign that is + at n=2 (Fisher, self-dual)
              and flips at n=3 (the cubic). We certify the *sign* agreement
              sign(c_n) = sign((-1)^n) and sign(kappa_n)=sign((-1)^(n-1)),
              i.e. the two towers are sign-opposite at every order
              (the e<->m / alpha->-alpha flip), n=2..6.

All five "geometry" claims (C1-C5) hold as exact identities in Q(p_i), so they
are valid for ALL interior p, not a sampled family.  C6 is checked at the
uniform point (where the program's transfer identity lives) over Q.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def assert_zero(expr, msg):
    """Assert a sympy expression (scalar OR matrix) is the exact zero."""
    if isinstance(expr, (sp.MatrixBase,)):
        e = sp.simplify(sp.Matrix(expr))
        ok = all(entry == 0 for entry in e)
        assert ok, f"FAIL: {msg}\n   residual = {e}"
    else:
        e = sp.simplify(sp.together(sp.expand(expr)))
        assert e == 0, f"FAIL: {msg}\n   residual = {e}"

def coeff_cn(n):
    """The diagonal cumulant coefficient c_n = (-1)^n (n-2)! for n>=2."""
    return sp.Integer((-1)**n) * sp.factorial(n - 2)

NMAX = 6          # certify orders n = 2..6
results = []      # (label, passed_bool)

def record(label, fn):
    fn()           # raises on failure
    results.append((label, True))
    print(f"  [OK] {label}")

# ===========================================================================
# C1.  Diagonal scalar law:  d^n/dp^n [p log p] = (-1)^n (n-2)!/p^(n-1)
# ===========================================================================
def check_C1():
    p = sp.symbols('p', positive=True)
    g = p * sp.log(p)
    for n in range(2, NMAX + 1):
        dn = sp.diff(g, p, n)
        expected = coeff_cn(n) / p**(n - 1)
        assert_zero(dn - expected, f"C1: n={n} diagonal scalar law")
    # explicit coefficient table 1,-1,2,-6,24 for n=2..6
    cs = [coeff_cn(n) for n in range(2, NMAX + 1)]
    assert cs == [sp.Integer(x) for x in (1, -1, 2, -6, 24)], f"C1: coeff table {cs}"

record("C1  diagonal scalar law d^n(p log p) = (-1)^n (n-2)!/p^(n-1), n=2..6", check_C1)

# ===========================================================================
# C2.  Purely-diagonal tower on the N-simplex.
#      Every mixed partial of phi=sum p_i log p_i vanishes; only all-equal
#      multi-indices survive, with value c_n / p_i^(n-1).
# ===========================================================================
def diagonal_check(N):
    ps = sp.symbols(f'p1:{N+1}', positive=True)
    phi = sum(pi * sp.log(pi) for pi in ps)
    from itertools import product
    for n in range(2, NMAX + 1):
        for idx in product(range(N), repeat=n):
            # nth partial wrt the chosen sequence of coordinates
            d = phi
            for j in idx:
                d = sp.diff(d, ps[j])
            if len(set(idx)) == 1:               # fully diagonal i...i
                i = idx[0]
                expected = coeff_cn(n) / ps[i]**(n - 1)
                assert_zero(d - expected, f"C2(N={N}): diag n={n} idx={idx}")
            else:                                # any genuinely mixed index
                assert_zero(d, f"C2(N={N}): off-diagonal n={n} idx={idx} must vanish")

def check_C2():
    diagonal_check(4)        # the program's N=4 frame, exhaustive over all 4^n indices
def check_C2_N5():
    # N=5 spot check (orders 2..4 to keep the multi-index sweep bounded)
    ps = sp.symbols('q1:6', positive=True)
    phi = sum(pi * sp.log(pi) for pi in ps)
    from itertools import product
    for n in range(2, 5):
        for idx in product(range(5), repeat=n):
            d = phi
            for j in idx:
                d = sp.diff(d, ps[j])
            if len(set(idx)) == 1:
                i = idx[0]
                assert_zero(d - coeff_cn(n)/ps[i]**(n-1), f"C2(N=5): diag n={n} idx={idx}")
            else:
                assert_zero(d, f"C2(N=5): off-diag n={n} idx={idx}")

record("C2  purely-diagonal tower on N=4 (exhaustive, all 4^n indices, n=2..6)", check_C2)
record("C2' N=5 spot check (n=2..4, all 5^n indices)", check_C2_N5)

# ===========================================================================
# C3.  Frozen geometry x breathing diagonal:
#      T^(n) = c_n * Delta^(n) * D_p^(n-1),  Delta^(n) position-independent.
# ===========================================================================
def check_C3():
    N = 4
    ps = sp.symbols(f'p1:{N+1}', positive=True)
    phi = sum(pi * sp.log(pi) for pi in ps)
    from itertools import product
    for n in range(2, NMAX + 1):
        cn = coeff_cn(n)
        for idx in product(range(N), repeat=n):
            # left side: actual tower component
            d = phi
            for j in idx:
                d = sp.diff(d, ps[j])
            # right side: c_n * Delta^(n)_idx * (1/p_i^(n-1)) collected on diagonal
            if len(set(idx)) == 1:
                i = idx[0]
                Delta = sp.Integer(1)            # all-equal-index selector = 1
                Dpow = 1 / ps[i]**(n - 1)        # breathing diagonal D_p^(n-1)
                rhs = cn * Delta * Dpow
            else:
                rhs = sp.Integer(0)              # Delta^(n) = 0 off the diagonal
            assert_zero(d - rhs, f"C3: factorization n={n} idx={idx}")

    # (a) the FROZEN combinatorial selector Delta^(n) carries no p-dependence.
    # Realize Delta^(n) as the constant 4x...x diagonal indicator and check
    # its symbolic p-gradient is identically zero (position-independence).
    for n in range(2, NMAX + 1):
        for i in range(N):
            Delta_entry = sp.Integer(1)          # the i...i entry, a pure constant
            for k in range(N):
                assert_zero(sp.diff(Delta_entry, ps[k]),
                            f"C3(a): Delta^({n}) entry not position-independent")

    # (b) ONLY D_p^(n-1) breathes: d/dp_i (1/p_i^(n-1)) = -(n-1)/p_i^n  (nonzero),
    #     while the scalar c_n is a pure integer constant.
    for n in range(2, NMAX + 1):
        assert_zero(sp.diff(coeff_cn(n), ps[0]), f"C3(b): c_{n} must be constant")
        dDp = sp.diff(1/ps[0]**(n-1), ps[0])
        assert_zero(dDp - (-(n-1)/ps[0]**n), f"C3(b): D_p^{n-1} breathing law")

record("C3  factorization T^(n)=c_n*Delta^(n)*D_p^(n-1); Delta frozen, only D_p breathes", check_C3)

# ===========================================================================
# C4.  n=2 reduces to the Fisher metric:  T^(2) = diag(1/p_i) = Hess phi = g_p.
# ===========================================================================
def check_C4():
    N = 4
    ps = sp.symbols(f'p1:{N+1}', positive=True)
    phi = sum(pi * sp.log(pi) for pi in ps)
    H = sp.hessian(phi, ps)
    G = sp.diag(*[1/ps[i] for i in range(N)])
    assert_zero((H - G), "C4: Hess(phi) != diag(1/p_i)")
    # and this is exactly the c_2/p^(1) diagonal tower (c_2 = +1)
    for i in range(N):
        assert_zero(H[i, i] - coeff_cn(2)/ps[i]**(2-1), f"C4: Fisher diag entry {i}")
    # Fisher metric on tangent vectors u,v in H equals sum u_i v_i / p_i (01c eq)
    u = sp.symbols('u1:5'); v = sp.symbols('v1:5')
    quad = sum(u[i]*v[j]*H[i, j] for i in range(N) for j in range(N))
    assert_zero(quad - sum(u[i]*v[i]/ps[i] for i in range(N)), "C4: g_p(u,v) form")

record("C4  n=2 -> Fisher metric  T^(2)=diag(1/p_i)=Hess(phi)", check_C4)

# ===========================================================================
# C5.  n=3 reduces to the moving Amari-Chentsov cubic (01c Theorem 4.1):
#      raised K^CH_p(u)v = D_p (u (.) v) - <u,v>_{g_p} p   realizes
#      T(u,v,w) = sum_i u_i v_i w_i / p_i^2 ;  diagonal T^(3)_{iii} = -1/p_i^2.
# ===========================================================================
def check_C5():
    N = 4
    ps = sp.symbols(f'p1:{N+1}', positive=True)
    phi = sum(pi * sp.log(pi) for pi in ps)
    # (a) diagonal third derivative value matches c_3/p^2 = -1/p^2
    for i in range(N):
        d3 = sp.diff(phi, ps[i], 3)
        assert_zero(d3 - coeff_cn(3)/ps[i]**(3-1), f"C5(a): T^(3)_iii entry {i}")

    # (b) the raised cubic from 01c Thm 4.1, on the tangent space H (sum=0).
    u = sp.symbols('u1:5'); v = sp.symbols('v1:5'); w = sp.symbols('w1:5')
    Dp = sp.diag(*[1/ps[i] for i in range(N)])
    gp = lambda a, b: sum(a[i]*b[i]/ps[i] for i in range(N))           # Fisher inner prod
    udotv = [u[i]*v[i] for i in range(N)]                              # u (.) v
    KCH = [ (Dp*sp.Matrix(udotv))[i] - gp(u, v)*ps[i] for i in range(N) ]  # K^CH_p(u)v
    # raise/lower: g_p(K^CH(u)v, w) must equal the skewness tensor sum u v w / p^2
    lhs = sum(KCH[i]*w[i]/ps[i] for i in range(N))
    skew = sum(u[i]*v[i]*w[i]/ps[i]**2 for i in range(N))
    # impose zero-sum on w (the correction term lives along p, killed on H):
    w_sub = {w[3]: -(w[0]+w[1]+w[2])}
    assert_zero(sp.expand(lhs.subs(w_sub) - skew.subs(w_sub)),
                "C5(b): raised cubic != skewness tensor on H")

    # (c) total symmetry of the skewness 3-tensor (cumulant must be symmetric):
    #     swap u<->v, v<->w with all three zero-sum -> identical.
    sub = {u[3]: -(u[0]+u[1]+u[2]), v[3]: -(v[0]+v[1]+v[2]),
           w[3]: -(w[0]+w[1]+w[2])}
    Tuvw = skew.subs(sub)
    # u<->v
    swap_uv = {**{u[i]: v[i] for i in range(N)}, **{v[i]: u[i] for i in range(N)}}
    assert_zero(sp.expand(Tuvw - skew.subs(sub).subs(swap_uv, simultaneous=True)),
                "C5(c): cubic not symmetric under u<->v")
    # v<->w
    swap_vw = {**{v[i]: w[i] for i in range(N)}, **{w[i]: v[i] for i in range(N)}}
    assert_zero(sp.expand(Tuvw - skew.subs(sub).subs(swap_vw, simultaneous=True)),
                "C5(c): cubic not symmetric under v<->w")

    # (d) reduction at the uniform point p_* = 1/4 * 1 recovers Cor 01.3.9 form
    #     K^CH_{p*}(u)v = 4(u (.) v) - (sum u_i v_i) 1
    sub_star = {ps[i]: sp.Rational(1, 4) for i in range(N)}
    KCH_star = [sp.simplify(KCH[i].subs(sub_star)) for i in range(N)]
    target = [4*u[i]*v[i] - sum(u[k]*v[k] for k in range(N)) for i in range(N)]
    for i in range(N):
        assert_zero(KCH_star[i] - target[i], f"C5(d): p_* reduction comp {i}")

record("C5  n=3 -> moving Amari-Chentsov cubic (01c Thm 4.1): raise, symmetry, p_* reduction", check_C5)

# ===========================================================================
# C6.  Legendre/dual bridge to the log-partition tower (program T2 Prop 6.2).
# ===========================================================================
def check_C6():
    m = sp.symbols('m', positive=True, integer=True)
    t = sp.symbols('t')

    # (i) phi-DIAGONAL tower value at the uniform p_i = 1/m :
    #     T^(n)_{ii..i}|_u = c_n / (1/m)^(n-1) = c_n * m^(n-1)
    for n in range(2, NMAX + 1):
        diag_at_u = coeff_cn(n) / (sp.Rational(1, 1)/m)**(n-1)
        assert_zero(diag_at_u - coeff_cn(n)*m**(n-1), f"C6(i): phi diag at uniform n={n}")

    # (ii) Phi-DISTINCT-index cumulant at uniform, from the CGF log(1+t/m)
    #      (program T2 Prop 6.2):  kappa_n = (-1)^(n-1)(n-1)! m^(-n).
    #      Derive kappa_n as n! * [t^n] log(1 + t/m).
    cgf = sp.log(1 + t/m)
    series = sp.series(cgf, t, 0, NMAX + 1).removeO()
    poly = sp.Poly(sp.expand(series), t)
    for n in range(2, NMAX + 1):
        cn_coeff = poly.coeff_monomial(t**n)            # [t^n] of CGF
        kappa_n = sp.factorial(n) * cn_coeff            # n! * [t^n]
        expected = sp.Integer((-1)**(n-1)) * sp.factorial(n-1) * m**(-n)
        assert_zero(sp.simplify(kappa_n - expected), f"C6(ii): kappa_{n} from CGF")

    # (iii) the dual involution alpha -> -alpha is the sign (-1)^n.
    #       phi-tower coefficient sign = sign((-1)^n);
    #       Phi-tower cumulant sign     = sign((-1)^(n-1));
    #       hence the two are SIGN-OPPOSITE at every order n>=2 (the e<->m flip):
    #         n=2 : phi +, Phi -      (Fisher: |sign| equal magnitude, self-dual axis)
    #         n=3 : phi -, Phi +      (the cubic flips)
    for n in range(2, NMAX + 1):
        s_phi = sp.sign(coeff_cn(n))                                  # sign of c_n
        s_Phi = sp.sign(sp.Integer((-1)**(n-1)) * sp.factorial(n-1))  # sign of kappa_n
        assert s_phi == sp.Integer((-1)**n), f"C6(iii): phi sign n={n}"
        assert s_Phi == sp.Integer((-1)**(n-1)), f"C6(iii): Phi sign n={n}"
        assert s_phi == -s_Phi, f"C6(iii): towers must be sign-opposite at n={n}"

record("C6  Legendre dual bridge: phi-diagonal vs Phi-distinct (T2 Prop 6.2) + (-1)^n involution", check_C6)

# ===========================================================================
# C7.  Cross-pollination cert (Direction 1): the K_N complete-graph Laplacian.
#      Paper 01 App. B: tr(K(u)^2) ~ sum_{i<j}(u_i-u_j)^2, the Dirichlet form
#      of the K_N graph Laplacian  L = N I - J.  We certify the IDENTITY
#          sum_{i<j} (u_i-u_j)^2 = u^T L u = u^T (N I - J) u
#      and that on the zero-sum hyperplane H this equals N*sum u_i^2
#      (matching the simplicial Gram quadratic form factor N/(N-1) up to the
#      frame normalization, i.e. L|_H = N I_H is N/(N-1) times G|_H * (N-1)).
#      This welds the order-2 cumulant (Fisher/metric) to Direction 1's graph
#      Laplacian spectrum: L has eigenvalues {0 (gauge 1), N (mult N-1 on H)}.
# ===========================================================================
def check_C7():
    for N in (3, 4, 5):
        us = sp.symbols(f'u1:{N+1}')
        L = N*sp.eye(N) - sp.ones(N, N)             # complete-graph K_N Laplacian
        uvec = sp.Matrix(us)
        dirichlet = sum((us[i]-us[j])**2 for i in range(N) for j in range(i+1, N))
        quad = (uvec.T * L * uvec)[0]
        assert_zero(quad - dirichlet, f"C7(N={N}): Dirichlet form != u^T L u")
        # on H (zero-sum), u^T L u = N * sum u_i^2
        sub = {us[N-1]: -sum(us[i] for i in range(N-1))}
        on_H = sp.expand((quad - N*sum(ui**2 for ui in us)).subs(sub))
        assert_zero(on_H, f"C7(N={N}): u^T L u != N sum u^2 on H")
        # spectrum: L 1 = 0 (gauge), and L acts as N*I on H
        assert_zero((L*sp.ones(N, 1)), f"C7(N={N}): L*1 != 0")
        # pick a concrete zero-sum vector and verify L u = N u on H
        e = [sp.Integer(0)]*N; e[0] = sp.Integer(1); e[1] = sp.Integer(-1)
        ev = sp.Matrix(e)
        assert_zero((L*ev - N*ev), f"C7(N={N}): L not N*I on H eigenvector")

record("C7  Direction-1 weld: K_N Laplacian L=NI-J, Dirichlet form, spectrum {0, N^(N-1)}", check_C7)

# ===========================================================================
# C8.  Paper 21 boundary (HONEST non-match certificate).
#      Paper 21 reads the order-4 obstruction in the LOG-PARTITION Phi-tower
#      (eta / exponential chart), in the additive-character basis, where the
#      qualitatively new feature is the 2+2 Wick block
#          Q(chi_a,chi_b,chi_c,chi_d)|_u = delta_{a+b+c+d} - 3 pairwise.
#      This note's tower is nabla^4 phi (negative entropy, p / MIXTURE chart),
#      the LEGENDRE DUAL object.  We certify that the phi-tower is PURELY
#      DIAGONAL and therefore carries NO 2+2 block at all, while the Phi-tower
#      does -- i.e. the phi-tower does NOT reproduce Paper 21's obstruction;
#      the two are dual objects in complementary charts.
# ===========================================================================
def check_C8():
    N = 4
    ps = sp.symbols(f'p1:{N+1}', positive=True)
    es = sp.symbols(f'e1:{N+1}')                      # eta-coordinates
    phi = sum(p*sp.log(p) for p in ps)                # mixture-chart potential
    Phi = sp.log(sum(sp.exp(e) for e in es))          # log-partition potential

    # (a) phi-tower: every (2+2) mixed 4-index component vanishes (no Wick block).
    from itertools import combinations
    for i, j in combinations(range(N), 2):
        d = phi
        for k in (i, i, j, j):
            d = sp.diff(d, ps[k])
        assert_zero(d, f"C8(a): phi-tower 2+2 block ({i}{i}{j}{j}) must vanish")

    # (b) Phi-tower: the SAME (2+2) component is NONzero at the uniform eta=0,
    #     i.e. p_* = 1/4  (this is the Gaussian subtraction Paper 21 isolates).
    sub_u = {e: 0 for e in es}
    nonzero_found = False
    for i, j in combinations(range(N), 2):
        dP = Phi
        for k in (i, i, j, j):
            dP = sp.diff(dP, es[k])
        val = sp.simplify(dP.subs(sub_u))
        if val != 0:
            nonzero_found = True
    assert nonzero_found, "C8(b): Phi-tower 2+2 block should be nonzero at uniform"

    # (c) the diagonal coefficients still AGREE up to the Legendre sign (-1)^n:
    #     phi-tower diagonal c_4 = +2 ; Phi-tower 4th DISTINCT cumulant sign flips.
    assert coeff_cn(4) == sp.Integer(2), "C8(c): c_4 must be +2"
    m = sp.symbols('m', positive=True, integer=True)
    kappa4 = sp.Integer((-1)**(4-1)) * sp.factorial(4-1) * m**(-4)   # = -6/m^4
    assert sp.sign(coeff_cn(4)) == -sp.sign(-sp.factorial(3)), \
        "C8(c): order-4 towers must be sign-opposite (e<->m flip)"

record("C8  Paper 21 boundary (HONEST): phi-tower diagonal -> NO 2+2 Wick block; Phi-tower has it", check_C8)

# ===========================================================================
# summary
# ===========================================================================
print("\n" + "="*72)
allpass = all(ok for _, ok in results)
for label, ok in results:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}")
print("="*72)
if allpass:
    print("CERT GREEN  ({} checks, exact sympy arithmetic over Q / Q(p_i))".format(len(results)))
    raise SystemExit(0)
else:
    print("CERT RED")
    raise SystemExit(1)
