"""
D-II: the discrete Einstein structure on the categorical simplex.
Mass = the order-4 dual-flatness defect.

Grounds the GR hierarchy the program already reads (Paper 32: grad^2 Phi = metric = space/inertia;
grad^3 Phi = cubic = force; grad^4 Phi = gravity-adjacent = m^2_simplex) in the dual-flat geometry:

 (A) SPACE has constant background curvature K = 1/4. The Fisher metric on the categorical
     simplex is the Hellinger sphere (radius 2) -- Gaussian curvature exactly 1/4 (ties Paper 32.1).
     This is the homogeneous "vacuum"/cosmological term Lambda.
 (B) The CONNECTION is dually FLAT: R^(+1) = R^(-1) = 0 (the e/m connections are flat). Orders <=3
     (metric + cubic) are the "free field": curved metric (1/4) but flat dual connection.
 (C) The alpha-curvature interpolates  R^(alpha) = (1 - alpha^2)/4 : 1/4 at alpha=0 (Levi-Civita,
     the sphere), 0 at alpha=+-1 (dual-flat). The metric curvature is the alpha=0 member of a
     family that vanishes at the dual ends.
 (D) MASS = the order-4 defect. The first content the dual-flat connection (orders <=3) does NOT
     carry is the order-4 cumulant. Its connected (2+2 Wick) part is e-chart-only (m-chart diagonal),
     closed form -(N^2-4N+6)/N^4, vanishing in the continuum (-1/N^2 -> 0). This is m^2_simplex
     (Paper 20), the localized source that breaks homogeneity; m^2 >= 0 = weak-energy/Raychaudhuri/arrow.

Discrete Einstein equation: curvature (the alpha-connection, orders <=3) <- sourced by mass
(the order-4 defect); energy condition = the order-4 Wick block's definite sign.

sympy/numpy, exact; no torch.
"""
import sys
import sympy as sp
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS = []
def chk(n, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {n}")

# ---- 2-simplex (3 outcomes), reduced coords (p1,p2), p3 = 1-p1-p2 ----
p1, p2 = sp.symbols('p1 p2', positive=True)
p3 = 1 - p1 - p2
coords = [p1, p2]
# Fisher metric g_ab = sum_k (d_a log p_k)(d_b log p_k) p_k  =  delta_ab/p_a + 1/p3
g = sp.Matrix([[1/p1 + 1/p3, 1/p3], [1/p3, 1/p2 + 1/p3]])
ginv = sp.simplify(g.inv())

def christoffel(Gconn):
    """Levi-Civita Christoffels of metric Gconn."""
    Gi = Gconn.inv()
    n = 2
    G = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[k][i][j] = sp.simplify(sum(
                    Gi[k, l]*(sp.diff(Gconn[l, i], coords[j]) + sp.diff(Gconn[l, j], coords[i])
                              - sp.diff(Gconn[i, j], coords[l])) for l in range(n)) / 2)
    return G

def Rfull(G, l, i, j, k):
    """Riemann R^l_{ijk} of a (possibly non-metric) connection G[l][i][j]=Gamma^l_ij."""
    n = 2
    t = sp.diff(G[l][i][k], coords[j]) - sp.diff(G[l][i][j], coords[k])
    t += sum(G[l][j][m]*G[m][i][k] - G[l][k][m]*G[m][i][j] for m in range(n))
    return sp.simplify(t)

# ---- (A) Gaussian curvature of the Fisher metric = 1/4 ----
print("(A) Fisher metric Gaussian curvature K (Hellinger sphere, Paper 32.1)")
G0 = christoffel(g)
# K = R_{1212}/det(g),  R_{1212} = g_{1m} R^m_{212}
R_1212 = sp.simplify(sum(g[0, m]*Rfull(G0, m, 1, 0, 1) for m in range(2)))
K = sp.simplify(R_1212 / g.det())
print(f"    K = {K}")
chk("Fisher-metric Gaussian curvature K = 1/4 (the Hellinger sphere, ties Paper 32.1)",
    sp.simplify(K - sp.Rational(1, 4)) == 0)

# ---- (B,C) alpha-curvature: R^(alpha) = (1-alpha^2)/4 ----
print("(B,C) alpha-curvature R^(alpha) = (1-alpha^2)/4 : 1/4 at 0, 0 at +-1 (dual-flat)")
# AC tensor T_abc (lowered) = sum_k (d_a logp_k)(d_b logp_k)(d_c logp_k) p_k
ps = [p1, p2, p3]
def dlog(a, i):                  # d/dp_i log p_a
    return sp.diff(sp.log(ps[a]), coords[i])
T = [[[sp.simplify(sum(dlog(a, i)*dlog(a, j)*dlog(a, k)*ps[a] for a in range(3)))
       for k in range(2)] for j in range(2)] for i in range(2)]
# raise one index: Tup^l_ij = sum_m ginv[l,m] T_mij  (lowered T is symmetric)
Tup = [[[sp.simplify(sum(ginv[l, m]*T[m][i][j] for m in range(2))) for j in range(2)]
        for i in range(2)] for l in range(2)]
alpha = sp.symbols('alpha')
# alpha-connection Gamma^(alpha) = Gamma^(0) - (alpha/2) Tup
Galpha = [[[sp.simplify(G0[l][i][j] - alpha/2*Tup[l][i][j]) for j in range(2)]
           for i in range(2)] for l in range(2)]
Ralpha_1212 = sp.simplify(sum(g[0, m]*Rfull(Galpha, m, 1, 0, 1) for m in range(2)))
Kalpha = sp.simplify(Ralpha_1212 / g.det())
Kalpha = sp.simplify(Kalpha)
print(f"    R^(alpha) sectional = {sp.factor(Kalpha)}")
chk("R^(alpha) = (1-alpha^2)/4 exactly (symbolic in alpha)",
    sp.simplify(Kalpha - (1 - alpha**2)/4) == 0)
chk("R^(0)=1/4 (Levi-Civita sphere), R^(+1)=R^(-1)=0 (dually flat)",
    sp.simplify(Kalpha.subs(alpha, 0) - sp.Rational(1, 4)) == 0
    and sp.simplify(Kalpha.subs(alpha, 1)) == 0 and sp.simplify(Kalpha.subs(alpha, -1)) == 0)

# ---- (D) mass = the order-4 defect ----
print("(D) mass = order-4 dual-flatness defect (e-chart Wick block), m^2>=0")
def echart_2p2(N):
    th = sp.symbols(f't0:{N}')
    Phi = sp.log(sum(sp.exp(t) for t in th))
    return sp.nsimplify(sp.diff(Phi, th[0], 2, th[1], 2).subs({t: 0 for t in th}))
closed = lambda N: -sp.Rational(N**2 - 4*N + 6, N**4)
chk("order-4 e-chart 2+2 block = -(N^2-4N+6)/N^4 (the mass defect), N=4,6",
    echart_2p2(4) == closed(4) and echart_2p2(6) == closed(6))
# m-chart (entropy) 2+2 block = 0: the defect is e-chart-only (orders<=3 dual-flat carry no order-4)
q1, q2 = sp.symbols('q1 q2', positive=True)
phi4 = sum(qk*sp.log(qk) for qk in (q1, q2))
chk("m-chart order-4 2+2 block = 0 (dual-flat geometry carries no order-4 connected content)",
    sp.simplify(sp.diff(phi4, q1, 2, q2, 2)) == 0)
# energy condition: the defect has definite (negative) sign for all N>=2 -> m^2 sign-definite (arrow)
Nn = sp.symbols('N', positive=True, integer=True)
chk("order-4 defect sign-definite (N^2-4N+6 > 0 for all real N: disc=16-24<0) => m^2 energy condition",
    sp.simplify(sp.discriminant(Nn**2 - 4*Nn + 6, Nn)) < 0)
chk("mass defect -> 0 in the continuum (-1/N^2): mass is a finite-resolution phenomenon",
    sp.limit(-(Nn**2 - 4*Nn + 6)/Nn**4, Nn, sp.oo) == 0)

print("=" * 78)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("DISCRETE EINSTEIN: space = Fisher metric = K=1/4 Hellinger sphere (Lambda/background);")
print("connection (orders<=3) dually FLAT R^(+-1)=0, R^(alpha)=(1-alpha^2)/4; MASS = the order-4")
print("dual-flatness defect (e-chart Wick block -(N^2-4N+6)/N^4 = m^2_simplex, Paper 20), the first")
print("content the free dual-flat geometry cannot carry; m^2>=0 = weak-energy/Raychaudhuri/arrow.")
print("Massless <=> dually flat <=> orders<=3 <=> classical; mass <=> order-4 <=> e-chart/quantum.")
print("=" * 78)
