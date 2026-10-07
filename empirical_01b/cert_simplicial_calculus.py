"""
Exact-arithmetic certificate for the simplicial differential calculus (Paper 01b).
Verifies, over a general quadratic Cartesian vector field with symbolic coefficients:
  (P3.1) gauge-invariant scalar f has zero-sum coordinate differential.
  (T5.3) curl := normalized K(grad) is conjugate to the Cartesian curl, and finds the constant.
  (T6.1) curl grad = 0.
  (T6.2) div curl = 0.
  (T6.3) curl curl = grad div - Laplacian.
sympy only; no floating point.
"""
import sympy as sp

# Integer height synthesis matrix Shat (3x4): columns = tetra vertices scaled by sqrt(3).
Shat = sp.Matrix([
    [-1, 1,  1, -1],
    [-1, 1, -1,  1],
    [ 1, 1, -1, -1],
])
assert Shat * Shat.T == 4 * sp.eye(3), "Shat Shat^T must be 4 I_3"
s3 = sp.sqrt(3)
S = Shat / s3                      # true (G-normalized) synthesis matrix
G = sp.simplify(S.T * S)           # 4x4 simplicial Gram matrix

c = sp.Matrix(sp.symbols('c1 c2 c3 c4', real=True))
xvec = Shat * c                    # cartesian position x = Shat c  (gauge-invariant in c)
xs = sp.symbols('x1 x2 x3', real=True)

def to_c(expr_in_x):
    """substitute x_a -> (Shat c)_a so an x-expression becomes a gauge-invariant c-field"""
    return expr_in_x.subs({xs[a]: xvec[a] for a in range(3)})

def dcoord(f):
    return sp.Matrix([sp.diff(f, ci) for ci in c])

# raw cyclic-difference matrix in a symbolic axis
uu = sp.symbols('u1 u2 u3 u4')
def Ktilde(u):
    u1, u2, u3, u4 = u
    return sp.Matrix([
        [0,      u3-u4,  u4-u2,  u2-u3],
        [u4-u3,  0,      u1-u4,  u3-u1],
        [u2-u4,  u4-u1,  0,      u1-u2],
        [u3-u2,  u1-u3,  u2-u1,  0],
    ])
Kt_sym = Ktilde(uu)

def K_raw_action(F):
    """ (K_tilde(d)F)_i : replace axis u_k by d/dc_k, act on vector field F (4x1). """
    res = sp.zeros(4, 1)
    for i in range(4):
        expr = 0
        for j in range(4):
            entry = Kt_sym[i, j]
            for k in range(4):
                coeff = sp.diff(entry, uu[k])
                if coeff != 0:
                    expr += coeff * sp.diff(F[j], c[k])
        res[i] = sp.expand(expr)
    return res

# ---- general quadratic Cartesian vector field W(x) with symbolic coefficients ----
monos = [sp.Integer(1), xs[0], xs[1], xs[2],
         xs[0]**2, xs[1]**2, xs[2]**2, xs[0]*xs[1], xs[0]*xs[2], xs[1]*xs[2]]
W = []
coeffs = []
for a in range(3):
    cf = sp.symbols(f'a{a}_0:{len(monos)}')
    coeffs.append(cf)
    W.append(sum(cf[m] * monos[m] for m in range(len(monos))))
W = sp.Matrix(W)  # 3x1, functions of x

# Cartesian curl of W
def cart_curl(Wx):
    return sp.Matrix([
        sp.diff(Wx[2], xs[1]) - sp.diff(Wx[1], xs[2]),
        sp.diff(Wx[0], xs[2]) - sp.diff(Wx[2], xs[0]),
        sp.diff(Wx[1], xs[0]) - sp.diff(Wx[0], xs[1]),
    ])

# simplicial field F = Shat_H^{-1} W = (1/4) Shat^T W, expressed in c
F = sp.Matrix([sp.expand(to_c((sp.Rational(1,4) * Shat.T * W)[i])) for i in range(4)])

print("=== P3.1: gauge-invariant scalar has zero-sum differential ===")
ftest = to_c(W[0]*W[1] + xs[0]**3)   # some gauge-invariant scalar
print("  sum(d f) =", sp.simplify(sum(dcoord(ftest))))

print("=== T5.3: find curl normalization constant ===")
# raw curl action, then map back by Shat; compare to Cartesian curl (in c-coords)
raw = K_raw_action(F)
mapped = sp.Matrix([sp.expand((Shat * raw)[a]) for a in range(3)])
target = sp.Matrix([sp.expand(to_c(cart_curl(W)[a])) for a in range(3)])
# constant kappa with mapped*kappa = target : take ratio on first nonzero component
ratios = []
for a in range(3):
    if mapped[a] != 0:
        ratios.append(sp.simplify(target[a] / mapped[a]))
print("  Shat*(Ktilde(d)F) vs Cartesian curl, ratio kappa =", set(ratios))
# so curl := kappa * Ktilde(d) F with that kappa. Identify with K=(1/sqrt3)Ktilde and grad=(3/4)d:
print("  (3/4)*(1/sqrt3) =", sp.nsimplify(sp.Rational(3,4)/s3), " ; sqrt3/4 =", sp.simplify(s3/4))

kappa = ratios[0]
def curl(F):
    return kappa * K_raw_action(F)

# --- consistent M = 3G (height) normalization, conjugate to Cartesian via Shat ---
# grad_M = (1/4) d ,  div_M = sum d/dc_i ,  curl_M = (1/4) Ktilde(d) = kappa*Ktilde(d) , Lap_M = (1/4) sum d^2
GN = sp.Rational(1, 4)

print("=== T6.1: curl grad = 0 ===")
fsc = to_c(W[0]*W[2] + xs[1]**2*xs[2])   # gauge-invariant scalar field
gradf = GN * dcoord(fsc)                  # M-gradient
print("  curl grad f =", sp.simplify(curl(gradf).T))

print("=== T6.2: div curl = 0 ===")
cF = curl(F)
divcurl = sp.expand(sum(sp.diff(cF[i], c[i]) for i in range(4)))
print("  div curl F =", sp.simplify(divcurl))

print("=== T6.3: curl curl = grad div - Laplacian (consistent M-normalization) ===")
def div(Fv):
    return sp.expand(sum(sp.diff(Fv[i], c[i]) for i in range(4)))
def grad(fsc):
    return GN * dcoord(fsc)
def lap_vec(Fv):
    return sp.Matrix([GN*sum(sp.diff(Fv[i], ck, 2) for ck in c) for i in range(4)])

lhs = curl(curl(F))
rhs = grad(div(F)) - lap_vec(F)
print("  max |curl curl - (grad div - Lap)| =",
      sp.simplify(sum((sp.expand(lhs[i]-rhs[i]))**2 for i in range(4))))
