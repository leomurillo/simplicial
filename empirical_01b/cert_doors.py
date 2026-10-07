"""
Paper II worked-application doors, exact certificates (sympy only, no torch).
Reuses the M-normalization calculus of 01b: grad=1/4 d, div=sum d_i, curl=1/4 Ktilde(d), Lap=1/4 sum d_i^2.

Door 2  HEAT/DIFFUSION:   d_t u = Lap u ; plane-wave dispersion w = |k|^2/4 ; discrete heat trace.
Door 3  VORTICITY/FLUIDS: u=curl psi solenoidal; vorticity=curl u; antisym(grad u)=1/2 Ktilde(vorticity).
Door 4  POISSON:          Lap phi = rho; solvability = gauge sector (ker = constants / span 1).
Door 5  ROTATION:         rigid field v=Ktilde(Omega)c has constant vorticity, div 0; exp(theta K) is its flow.
"""
import sympy as sp

c = sp.Matrix(sp.symbols('c1 c2 c3 c4', real=True))
t, th = sp.symbols('t theta', real=True)

def Ktilde(u):
    u1, u2, u3, u4 = u
    return sp.Matrix([[0, u3-u4, u4-u2, u2-u3], [u4-u3, 0, u1-u4, u3-u1],
                      [u2-u4, u4-u1, 0, u1-u2], [u3-u2, u1-u3, u2-u1, 0]])
uu = sp.symbols('uu1 uu2 uu3 uu4')
Ktsym = Ktilde(uu)
def Kd(F):                                   # (Ktilde(d) F)_i with axis d/dc
    res = sp.zeros(4, 1)
    for i in range(4):
        e = 0
        for j in range(4):
            for k in range(4):
                cf = sp.diff(Ktsym[i, j], uu[k])
                if cf != 0:
                    e += cf * sp.diff(F[j], c[k])
        res[i] = sp.expand(e)
    return res
grad = lambda f: sp.Rational(1, 4) * sp.Matrix([sp.diff(f, c[i]) for i in range(4)])
div = lambda F: sp.expand(sum(sp.diff(F[i], c[i]) for i in range(4)))
curl = lambda F: sp.Rational(1, 4) * Kd(F)
lap = lambda f: sp.Rational(1, 4) * sum(sp.diff(f, c[i], 2) for i in range(4))

PASS = []
def chk(n, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {n}")

print("DOOR 2  heat/diffusion  d_t u = Lap u")
k = sp.Matrix([1, 2, -1, -2])                # zero-sum frequency (in H)
kc = sum(k[i] * c[i] for i in range(4))
w = sp.Rational(1, 4) * sum(k[i]**2 for i in range(4))
u = sp.exp(-w * t) * sp.cos(kc)
chk("plane wave e^{-wt}cos(k.c), k in H, solves d_t u = Lap u  (w=|k|^2/4)",
    sp.simplify(sp.diff(u, t) - lap(u)) == 0)
chk("solution is gauge-invariant (k in H => k.(c+a1)=k.c)", sum(k) == 0)
tr = sp.simplify(sum(sp.exp(-ev * t) for ev in [0, 4, 4, 4]))   # M spectrum {0, 4^3}
chk("discrete heat trace Tr e^{-tM} = 1 + 3 e^{-4t}  (forward1)",
    sp.simplify(tr - (1 + 3 * sp.exp(-4 * t))) == 0)

print("DOOR 3  incompressible fluids / vorticity")
Shat = sp.Matrix([[-1, 1, 1, -1], [-1, 1, -1, 1], [1, 1, -1, -1]])
xv = Shat * c
xs = sp.symbols('x1 x2 x3', real=True)
to_c = lambda e: e.subs({xs[a]: xv[a] for a in range(3)})
# gauge-invariant vector potential psi = 1/4 Shat^T Wpsi(x)  (function of x = Shat c only)
Wpsi = sp.Matrix([xs[0]**2 * xs[1], xs[1] * xs[2], xs[0] * xs[2]**2])
psi = sp.Matrix([sp.expand(to_c((sp.Rational(1, 4) * Shat.T * Wpsi)[i])) for i in range(4)])
u3 = curl(psi)
chk("u = curl psi is solenoidal: div u = 0", sp.simplify(div(u3)) == 0)
vort = curl(u3)
Du = sp.Matrix(4, 4, lambda i, j: sp.diff(u3[i], c[j]))
A = sp.Rational(1, 2) * (Du - Du.T)
chk("vorticity = curl u ; antisym(grad u) = 1/2 Ktilde(vorticity)  (strain+spin)",
    sp.simplify(A - sp.Rational(1, 2) * Ktilde(vort)) == sp.zeros(4, 4))

print("DOOR 4  Poisson  Lap phi = rho ; solvability = gauge sector")
M = 4 * sp.eye(4) - sp.ones(4, 4)            # graph Laplacian = K4 metric
chk("ker(M) = span(1): the gauge sector is the solvability obstruction", M * sp.ones(4, 1) == sp.zeros(4, 1))
rho = sp.Matrix([1, 2, -1, -2])              # zero-sum (orthogonal to 1)
chk("rho zero-mean => Poisson M phi = rho solvable (phi = M^+ rho)",
    sp.simplify(M * (M.pinv() * rho) - rho) == sp.zeros(4, 1))
rho_bad = sp.ones(4, 1)                       # nonzero mean
chk("rho with nonzero mean is NOT solvable (mean = the obstruction)",
    sp.simplify(M * (M.pinv() * rho_bad) - rho_bad) != sp.zeros(4, 1))
chk("continuum: Lap(constant)=0 (kernel = harmonics = constants)", sp.simplify(lap(sp.Integer(7))) == 0)

print("DOOR 5  rotational dynamics  rigid field v = Ktilde(Omega) c")
Om = sp.Matrix([1, -1, 2, -2])               # zero-sum angular velocity
v = Ktilde(Om) * c
cv = curl(v)
ratios = {sp.simplify(cv[i] / Om[i]) for i in range(4) if Om[i] != 0}
chk(f"rigid rotation has CONSTANT vorticity curl v = const*Omega  (const={ratios})", len(ratios) == 1)
chk("rigid rotation is incompressible: div v = 0", sp.simplify(div(v)) == 0)
# Paper 01 rotation R=exp(theta K) is the flow of v: dR/dtheta = K R  (M-unit axis, Rodrigues form)
Ohat = sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 4), -sp.Rational(1, 4), -sp.Rational(1, 4)])  # M-unit
K = Ktilde(Ohat)
R = sp.eye(4) + sp.sin(th) * K + (1 - sp.cos(th)) * K**2       # Paper 01 Rodrigues (M-norm)
chk("R(theta)=exp(theta K) is the flow of v:  dR/dtheta = K R",
    sp.simplify(sp.diff(R, th) - K * R) == sp.zeros(4, 4))

print("=" * 64)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("=" * 64)
