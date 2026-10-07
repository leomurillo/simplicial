"""
C4 certificate: the Helmholtz div/curl split as the symmetric/antisymmetric (S+A)
curvature/current split of the field Jacobian, in simplicial coordinates.
sympy only; exact.

For a vector field F on H with field Jacobian DF (4x4, entries d F_i / d c_j):
 (a) tr(DF) = div F           [symmetric part carries the divergence = curvature/source]
 (b) A := 1/2 (DF - DF^T) = kappa * Ktilde(curl F)   [antisym part = curl = vorticity/current];
     report kappa.  This uses the SAME Ktilde <-> vector iso as C1 (Thm 10.1).
 (c) Helmholtz alignment:  F = grad f  =>  A = 0  (symmetric Hessian, d^2=0);
                           F = curl B  =>  tr(DF) = 0 (div curl = 0).
"""
import sympy as sp

# integer height synthesis matrix
Shat = sp.Matrix([[-1, 1, 1, -1], [-1, 1, -1, 1], [1, 1, -1, -1]])
c = sp.Matrix(sp.symbols('c1 c2 c3 c4', real=True))
xvec = Shat * c
xs = sp.symbols('x1 x2 x3', real=True)
def to_c(e): return e.subs({xs[a]: xvec[a] for a in range(3)})

def Ktilde(u):
    u1, u2, u3, u4 = u
    return sp.Matrix([[0, u3-u4, u4-u2, u2-u3],
                      [u4-u3, 0, u1-u4, u3-u1],
                      [u2-u4, u4-u1, 0, u1-u2],
                      [u3-u2, u1-u3, u2-u1, 0]])
uu = sp.symbols('uu1 uu2 uu3 uu4')
Ktsym = Ktilde(uu)
def K_raw_action(F):              # (Ktilde(d) F)_i  with axis d/dc
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
def curl(F):                      # 01b curl = 1/4 Ktilde(d) F
    return sp.Rational(1, 4) * K_raw_action(F)

# general quadratic Cartesian field with symbolic coefficients
monos = [sp.Integer(1), xs[0], xs[1], xs[2], xs[0]**2, xs[1]**2, xs[2]**2,
         xs[0]*xs[1], xs[0]*xs[2], xs[1]*xs[2]]
W = []
for a in range(3):
    cf = sp.symbols(f'a{a}_0:{len(monos)}')
    W.append(sum(cf[m]*monos[m] for m in range(len(monos))))
W = sp.Matrix(W)
F = sp.Matrix([sp.expand(to_c((sp.Rational(1, 4)*Shat.T*W)[i])) for i in range(4)])

# field Jacobian in c
DF = sp.Matrix(4, 4, lambda i, j: sp.diff(F[i], c[j]))

# (a) trace = divergence
divF = sp.expand(sum(sp.diff(F[i], c[i]) for i in range(4)))
print("(a) tr(DF) - div F =", sp.simplify(sp.trace(DF) - divF))

# (b) antisymmetric part vs Ktilde(curl F)
A = sp.Rational(1, 2)*(DF - DF.T)
KcurlF = Ktilde(curl(F))
# find kappa: A = kappa * KcurlF  (compare a nonzero entry, then verify full matrix)
ratios = set()
for i in range(4):
    for j in range(4):
        if sp.simplify(KcurlF[i, j]) != 0:
            ratios.add(sp.simplify(A[i, j] / KcurlF[i, j]))
print("(b) A = kappa * Ktilde(curl F), kappa in", ratios)
kappa = list(ratios)[0] if len(ratios) == 1 else None
if kappa is not None:
    print("    A - kappa*Ktilde(curl F) == 0 :",
          sp.simplify(A - kappa*KcurlF) == sp.zeros(4, 4))

# (c) Helmholtz alignment
fsc = to_c(W[0]*W[1] + xs[2]**3)                     # scalar field
gradf = sp.Rational(1, 4)*sp.Matrix([sp.diff(fsc, c[i]) for i in range(4)])
DGf = sp.Matrix(4, 4, lambda i, j: sp.diff(gradf[i], c[j]))
Agrad = sp.Rational(1, 2)*(DGf - DGf.T)
print("(c) F=grad f  => antisym(D grad f) == 0 :", sp.simplify(Agrad) == sp.zeros(4, 4))

B = sp.Matrix([sp.expand(to_c((sp.Rational(1, 4)*Shat.T*W)[i])) for i in range(4)])
cB = curl(B)                                         # F = curl B is solenoidal
DcB = sp.Matrix(4, 4, lambda i, j: sp.diff(cB[i], c[j]))
print("    F=curl B => tr(D curl B) = div curl B == 0 :", sp.simplify(sp.trace(DcB)) == 0)
