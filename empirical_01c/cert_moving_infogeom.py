"""
C3 certificate: moving information geometry on the categorical simplex in
simplicial-frame (zero-sum) coordinates. sympy only; exact.

Verifies:
 (1) Fisher metric = Hessian of the negative-entropy potential phi(p)=sum p_i log p_i
     in mixture (simplicial) coordinates  ->  dual-flat, simplicial coords = m-affine chart.
 (2) Moving Amari-Chentsov cubic  K_p(u)v = D_p(u.v) - <u,v>_{g_p} p   (D_p=diag(1/p_i))
     is totally symmetric (a genuine 3-tensor) and equals the raised AC tensor.
 (3) At p_* = (1/4)1 it reduces to Paper 01 Cor 3.9:  4(u.v) - (sum u_i v_i) 1.
 (4) The cross-product-square realization of the componentwise product (projectors
     I+K(tau_i)^2 from Cor 01.3.6/3.9) is POSITION-INDEPENDENT; only D_p moves.
 (5) Dual-flatness collapse: in the mixture chart the Levi-Civita connection of Fisher
     satisfies Gamma^(0) = -1/2 T, so Gamma^(m)=Gamma^(-1)=0 (manifestly m-flat) and the
     whole alpha-family is Gamma^(alpha) = -((1+alpha)/2) T  (pure Amari-Chentsov cubic).
"""
import sympy as sp

p1, p2, p3, p4 = sp.symbols('p1 p2 p3 p4', positive=True)
p = sp.Matrix([p1, p2, p3, p4])

# (1) Fisher = Hess(neg-entropy) in p-coordinates
phi = sum(pi * sp.log(pi) for pi in p)
Hess = sp.hessian(phi, (p1, p2, p3, p4))
Fisher_diag = sp.diag(1/p1, 1/p2, 1/p3, 1/p4)
print("(1) Hess(sum p log p) == diag(1/p_i):", sp.simplify(Hess - Fisher_diag) == sp.zeros(4, 4))

# (2)-(3) moving AC cubic
u = sp.Matrix(sp.symbols('u1 u2 u3 u4'))
v = sp.Matrix(sp.symbols('v1 v2 v3 v4'))
w = sp.Matrix(sp.symbols('w1 w2 w3 w4'))
Dp = sp.diag(*[1/pi for pi in p])

def g(a, b):                      # Fisher inner product at p
    return sum(a[i]*b[i]/p[i] for i in range(4))

def KCH(uu, vv):                  # raised Amari-Chentsov cubic at p
    comp = sp.Matrix([uu[i]*vv[i]/p[i] for i in range(4)])   # D_p (u . v)
    return comp - g(uu, vv) * p

# total symmetry:  T(u,v,w) = g(KCH(u,v), w) must be symmetric in u,v,w
def T(uu, vv, ww):
    return sp.simplify(g(KCH(uu, vv), ww))
T_uvw = T(u, v, w)
T_raw = sp.simplify(sum(u[i]*v[i]*w[i]/p[i]**2 for i in range(4)))   # diagonal AC tensor on H
# tangent vectors live in H: enforce zero-sum on ALL of u, v, w
zs = {u[3]: -(u[0]+u[1]+u[2]), v[3]: -(v[0]+v[1]+v[2]), w[3]: -(w[0]+w[1]+w[2])}
print("(2) KCH symmetric & == raised AC tensor (on H):",
      sp.simplify((T_uvw - T_raw).subs(zs)) == 0,
      "| u<->v sym:", sp.simplify((T(u, v, w) - T(v, u, w)).subs(zs)) == 0,
      "| v<->w sym:", sp.simplify((T(u, v, w) - T(u, w, v)).subs(zs)) == 0)

# (3) reduce at p_* = (1/4)1
star = {p1: sp.Rational(1, 4), p2: sp.Rational(1, 4), p3: sp.Rational(1, 4), p4: sp.Rational(1, 4)}
KCH_star = KCH(u, v).subs(star)
cor39 = sp.Matrix([4*u[i]*v[i] for i in range(4)]) - (sum(u[i]*v[i] for i in range(4))) * sp.ones(4, 1)
print("(3) KCH at p_* == Cor 01.3.9  [4(u.v)-(sum u_i v_i)1]:",
      sp.simplify(KCH_star - cor39) == sp.zeros(4, 1))

# (4) cross-product-square projectors are position-independent (built from fixed tau_i)
# tau_i = e_i - 1/4 * 1 ; Ktilde raw; P_i = I + (1/3) Ktilde(tau_i)^2 is the G-orthogonal
# projector onto R tau_i (Cor 01.3.6, with normalized K=(1/sqrt3)Ktilde so K^2=(1/3)Ktilde^2).
def Ktilde(a):
    a1, a2, a3, a4 = a
    return sp.Matrix([
        [0, a3-a4, a4-a2, a2-a3],
        [a4-a3, 0, a1-a4, a3-a1],
        [a2-a4, a4-a1, 0, a1-a2],
        [a3-a2, a1-a3, a2-a1, 0]])
one = sp.ones(4, 1)
tau = [sp.Matrix([1 if j == i else 0 for j in range(4)]) - sp.Rational(1, 4)*one for i in range(4)]
# componentwise product via projectors at p_*: u o v = sum_i <tau_i,u>_M (I+K(tau_i)^2) v   (Prop 3.8 form)
M = 4*sp.eye(4) - sp.ones(4, 4)
def Knorm_sq(a):
    return sp.Rational(1, 3) * (Ktilde(a) * Ktilde(a))
lhs = sp.zeros(4, 1)
for i in range(4):
    Pi = sp.eye(4) + Knorm_sq(tau[i])
    coeff = (tau[i].T * M * u)[0]
    lhs += coeff * (Pi * v)
lhs = sp.Rational(3, 4) * lhs   # Prop 3.8 prefactor (G-form 9/4 * <.,.>_G = 3/4 * <.,.>_M)
# Cor 01.3.9 / Prop 3.8 hold for u,v in H: enforce zero-sum
zsuv = {u[3]: -(u[0]+u[1]+u[2]), v[3]: -(v[0]+v[1]+v[2])}
print("(4) projector form (pos-indep) == 4(u.v)-(sum)1 :",
      sp.simplify((lhs - cor39).subs(zsuv)) == sp.zeros(4, 1))

# (5) dual-flatness collapse in mixture chart (p1,p2,p3 free, p4=1-p1-p2-p3)
x = [p1, p2, p3]
p4e = 1 - p1 - p2 - p3
pe = [p1, p2, p3, p4e]
# Fisher in chart: g_ab = sum_i (dp_i/dx_a)(dp_i/dx_b)/p_i
def dpi_dx(i, a):
    if i < 3:
        return 1 if i == a else 0
    return -1
gch = sp.Matrix(3, 3, lambda a, b: sum(dpi_dx(i, a)*dpi_dx(i, b)/pe[i] for i in range(4)))
ginv = gch.inv()
# Levi-Civita Christoffels (lowered): Gamma0_{ab,c} = 1/2(d_a g_bc + d_b g_ac - d_c g_ab)
def Gamma0(a, b, c):
    return sp.Rational(1, 2)*(sp.diff(gch[b, c], x[a]) + sp.diff(gch[a, c], x[b]) - sp.diff(gch[a, b], x[c]))
# AC tensor in chart: T_{abc} = sum_i (dp_i/dx_a)(dp_i/dx_b)(dp_i/dx_c)/p_i^2
def Tch(a, b, c):
    return sum(dpi_dx(i, a)*dpi_dx(i, b)*dpi_dx(i, c)/pe[i]**2 for i in range(4))
# check Gamma0 = -1/2 T  (=> Gamma^m = Gamma0 + 1/2 T = 0 ; Gamma^e = Gamma0 - 1/2 T = -T)
maxres = 0
for a in range(3):
    for b in range(3):
        for c in range(3):
            maxres = sp.simplify(maxres + (Gamma0(a, b, c) + sp.Rational(1, 2)*Tch(a, b, c))**2)
print("(5) Gamma^(0) + 1/2 T  (== 0 => m-flat, alpha-family = -((1+a)/2)T):", maxres)
