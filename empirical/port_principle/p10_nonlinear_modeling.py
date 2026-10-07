"""
P10 -- The modeling calculus beyond linear ports (PortPrinciple.md Proposition 11.2).  sympy only.
Usage: python p10_nonlinear_modeling.py

CLAIM (classical; credited in the manuscript).  For a nonlinear port-Hamiltonian system with storage H(x),
interconnection J(x) = -J(x)^T and dissipation R(x) = R(x)^T >= 0 at temperature theta = k_B T, the Ito equation
    dx = [ -(R - J) grad H + theta div (R - J)^T ] dt + sqrt(2 theta) sigma dW,   sigma sigma^T = R,
with (div M^T)_i = sum_j d_j M_ij, has the Gibbs density e^{-H/theta} as a stationary solution for EVERY H, J(x),
R(x); its stationary current is (J grad H - theta div J^T) e^{-H/theta} (divergence-free).  Without the divergence
("spurious drift") term, Gibbs stationarity fails in general once R or J depends on x.  Losses at two temperatures
leave no Gibbs stationary state.  A memory bath is a Foster (LC) port: eliminating N oscillators gives the
generalized Langevin equation with kernel gamma(t) = sum c_k^2/w_k^2 cos(w_k t), positive-real transform, and
thermal noise with <xi(t) xi(s)> = theta gamma(t - s) (Kubo's second FDT).

PRE-REGISTERED FALSIFIERS (written 2026-10-02 before the first run)
  N1 [exact] 2D and 3D symbolic instances (polynomial H, J(x), R(x) = B(x) B(x)^T): the Fokker-Planck right-hand side
     vanishes identically on p = e^{-H/theta}.                                            L: nonzero residual.
  N2 [exact] dropping the divergence term leaves a nonzero residual for state-dependent R or J, and a zero residual
     when R and J are constant.                                                           L: otherwise.
  N3 [exact] the stationary current equals (J grad H - theta div J^T) p and is divergence-free.
  N4 [exact] two loss temperatures theta1 != theta2 on a coupled nonlinear 2D system: e^{-H/theta} is not stationary
     for any theta (the residual cannot vanish identically).                              L: some theta works.
  N5 [exact] Foster bath with two oscillators (Ford-Kac-Mazur / Caldeira-Leggett): (a) the eliminated bath gives the
     kernel gamma(t) = sum c_k^2/w_k^2 cos(w_k t) (the solution identity is checked by substitution); (b) for
     thermal initial bath states <xi(t) xi(s)> = theta gamma(t - s); (c) the kernel's transform
     sum (c_k^2/w_k^2) s/(s^2 + w_k^2) is a Foster reactance (positive real; zero real part on the axis).

RUN LOG
  Run 1 (2026-10-02, p10_run1.log): N1-N4 PASS; N5 gave NO VERDICT -- sympy's heuristic integrator raised MemoryError
  on the fully symbolic memory integral (checker failure, same class as the Paper 54 run-1/2 blowups).  Fix: the
  identity in N5(a) is linear in each oscillator, so it is checked by exact integration at three rational parameter
  sets (w1, w2, c1, c2); (b) and (c) unchanged.  Run 2 is NOT BLIND for the repaired N5 checker.
  Run 2 (p10_run2.log): 4/5 -- N5(a) FAILED on a CHECKER BUG: some parameters were Python ints, so ck/wk became
  floats (1/2 -> 0.5) inside the symbolic expression and exact cancellation was impossible; (b), (c) passed.  A debug
  run with exact coefficients gives a residual that simplifies to 0 and evaluates to exactly 0 at t = 0.3, 1.1, 2.7.
  Fix: every parameter is a sympy Integer/Rational.  Run 3 is NOT BLIND for N5.
"""
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

th = sp.symbols('theta', positive=True)

def fp_residual(xs, H, Jm, Rm, with_div=True):
    """Fokker-Planck RHS divided by p, for p = exp(-H/theta): drift -(R - J) grad H (+ theta div (R - J)^T),
    diffusion matrix theta R (Ito)."""
    n = len(xs)
    M = Rm - Jm
    gH = sp.Matrix([sp.diff(H, v) for v in xs])
    divMT = sp.Matrix([sum(sp.diff(M[i, j], xs[j]) for j in range(n)) for i in range(n)])
    D = th * Rm
    b = -M * gH + (th * divMT if with_div else sp.zeros(n, 1))
    p = sp.exp(-H / th)
    expr = -sum(sp.diff(b[i] * p, xs[i]) for i in range(n)) + sum(sp.diff(D[i, j] * p, xs[i], xs[j])
                                                                   for i in range(n) for j in range(n))
    return sp.simplify(sp.expand(expr / p))

# ------------------------------------------------------------------ N1
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
H2 = x1 ** 4 / 4 + x2 ** 2 / 2 + x1 * x2 / 3 + x1 ** 2 * x2 ** 2 / 5
J2 = (1 + x1 ** 2 + x2 / 2) * sp.Matrix([[0, 1], [-1, 0]])
B2 = sp.Matrix([[1 + x2 ** 2 / 2, x1 / 3], [0, 1 + x1 ** 2]])
R2 = B2 * B2.T
r1 = fp_residual([x1, x2], H2, J2, R2)
H3 = x1 ** 2 / 2 + x2 ** 4 / 4 + x3 ** 2 / 2 + x1 * x2 * x3 / 7
a12, a13, a23 = 1 + x3 ** 2, x2 / 2, 2 + x1
J3 = sp.Matrix([[0, a12, a13], [-a12, 0, a23], [-a13, -a23, 0]])
B3 = sp.Matrix([[1, x2 / 2, 0], [x3 / 3, 1 + x1 ** 2 / 4, 0], [0, x1 / 5, 1 + x2 ** 2]])
R3 = B3 * B3.T
r3 = fp_residual([x1, x2, x3], H3, J3, R3)
check("N1 [exact] Gibbs is stationary for nonlinear H, J(x), R(x) with the divergence drift (2D and 3D)",
      r1 == 0 and r3 == 0, f"residuals: 2D {r1}, 3D {r3}")

# ------------------------------------------------------------------ N2
r1n = fp_residual([x1, x2], H2, J2, R2, with_div=False)
Jc = sp.Matrix([[0, 2], [-2, 0]]); Rc = sp.Matrix([[2, 1], [1, 3]])
rcn = fp_residual([x1, x2], H2, Jc, Rc, with_div=False)
check("N2 [exact] without the divergence drift: nonzero residual for state-dependent R, J; zero for constant",
      r1n != 0 and rcn == 0, f"state-dependent residual nonzero: {r1n != 0}; constant residual {rcn}")

# ------------------------------------------------------------------ N3
xs = [x1, x2, x3]
p3 = sp.exp(-H3 / th)
gH3 = sp.Matrix([sp.diff(H3, v) for v in xs])
divJT = sp.Matrix([sum(sp.diff(J3[i, j], xs[j]) for j in range(3)) for i in range(3)])
M3 = R3 - J3
divMT = sp.Matrix([sum(sp.diff(M3[i, j], xs[j]) for j in range(3)) for i in range(3)])
b3 = -M3 * gH3 + th * divMT
curr = sp.Matrix([b3[i] * p3 - th * sum(sp.diff(R3[i, j] * p3, xs[j]) for j in range(3)) for i in range(3)])
claimed = (J3 * gH3 - th * divJT) * p3
diffc = sp.simplify((curr - claimed) / p3)
divc = sp.simplify(sum(sp.diff(claimed[i], xs[i]) for i in range(3)) / p3)
check("N3 [exact] stationary current = (J grad H - theta div J^T) e^{-H/theta}, divergence-free",
      diffc == sp.zeros(3, 1) and divc == 0, f"current difference {list(diffc)}; divergence {divc}")

# ------------------------------------------------------------------ N4
t1, t2 = sp.symbols('theta1 theta2', positive=True)
H4 = x1 ** 2 / 2 + x2 ** 2 / 2 + x1 ** 2 * x2 ** 2 / 4
J4 = sp.Matrix([[0, 1], [-1, 0]])
R4 = sp.diag(1, 1)
# losses at theta1 on x1, theta2 on x2:  dx = (J - R) grad H dt + sqrt(2 theta_i) dW_i  (constant R, J: no div term)
gH4 = sp.Matrix([sp.diff(H4, v) for v in (x1, x2)])
b4 = (J4 - R4) * gH4
p4 = sp.exp(-H4 / th)
expr4 = -sum(sp.diff(b4[i] * p4, v) for i, v in enumerate((x1, x2))) + \
        t1 * sp.diff(p4, x1, 2) + t2 * sp.diff(p4, x2, 2)
res4 = sp.expand(sp.simplify(expr4 / p4))
coeffs = sp.Poly(res4, x1, x2).coeffs()
sol = sp.solve(coeffs, th, dict=True)
ok4 = all(sp.simplify(s_[th] - t1) != 0 or sp.simplify(t1 - t2) == 0 for s_ in sol) if sol else True
# stronger: the system of coefficient equations has a solution only when theta1 = theta2 = theta
sol2 = sp.solve(coeffs + [t1 - t2 - 1], [th, t1, t2], dict=True)
check("N4 [exact] two loss temperatures: no Gibbs stationary state for any theta (theta1 != theta2)",
      not sol2, f"solutions with theta1 - theta2 = 1: {sol2}")

# ------------------------------------------------------------------ N5
t, s, s0 = sp.symbols('t s s0', real=True)
w1, w2, c1, c2 = sp.symbols('w1 w2 c1 c2', positive=True)
X = sp.Function('X')
q10, q20, p10, p20, x0 = sp.symbols('q10 q20 p10 p20 x0', real=True)
# bath oscillator k: q_k'' = -w_k^2 q_k + c_k X(t).  Solution with initial data (q_k0, p_k0):
def q_sol(wk, ck, qk0, pk0):
    tau = sp.symbols('tau', real=True)
    return (qk0 * sp.cos(wk * t) + pk0 / wk * sp.sin(wk * t)
            + ck / wk * sp.Integral(sp.sin(wk * (t - tau)) * X(tau), (tau, 0, t)))
q1 = q_sol(w1, c1, q10, p10)
lhs = sp.diff(q1, t, 2) + w1 ** 2 * q1 - c1 * X(t)
n5a_ode = sp.simplify(lhs.doit()) == 0
# kernel identity: sum c_k q_k - (c_k^2/w_k^2) X = -int gamma(t-tau) X'(tau) dtau - gamma(t) X(0) + xi(t)
# (integration by parts of the memory term), with gamma(t) = sum c_k^2/w_k^2 cos(w_k t): checked on X(t) = cos(3t)/2 + t
Xs = sp.cos(3 * t) / 2 + t
tau = sp.symbols('tau', real=True)
def qk_explicit(wk, ck, qk0, pk0):
    return (qk0 * sp.cos(wk * t) + pk0 / wk * sp.sin(wk * t)
            + ck / wk * sp.integrate(sp.sin(wk * (t - tau)) * Xs.subs(t, tau), (tau, 0, t)))
gam = lambda u: c1 ** 2 / w1 ** 2 * sp.cos(w1 * u) + c2 ** 2 / w2 ** 2 * sp.cos(w2 * u)
n5a_inst = []
for pars in ({w1: 2, w2: 5, c1: 1, c2: 3}, {w1: sp.Rational(3, 2), w2: 7, c1: 2, c2: sp.Rational(1, 2)},
             {w1: 1, w2: sp.Rational(5, 3), c1: sp.Rational(4, 3), c2: 1}):
    W1, W2, C1, C2 = (sp.Rational(pars[v]) for v in (w1, w2, c1, c2))
    def qk_num(wk, ck, qk0, pk0):
        return (qk0 * sp.cos(wk * t) + pk0 / wk * sp.sin(wk * t)
                + ck / wk * sp.integrate(sp.sin(wk * (t - tau)) * Xs.subs(t, tau), (tau, 0, t)))
    force = sum(ck * qk_num(wk, ck, qk0, pk0) - ck ** 2 / wk ** 2 * Xs
                for (wk, ck, qk0, pk0) in ((W1, C1, q10, p10), (W2, C2, q20, p20)))
    gnum = lambda u: C1 ** 2 / W1 ** 2 * sp.cos(W1 * u) + C2 ** 2 / W2 ** 2 * sp.cos(W2 * u)
    x0v = Xs.subs(t, 0)
    xi = sum(ck * ((qk0 - ck * x0v / wk ** 2) * sp.cos(wk * t) + pk0 / wk * sp.sin(wk * t))
             for (wk, ck, qk0, pk0) in ((W1, C1, q10, p10), (W2, C2, q20, p20)))
    memory = -sp.integrate(gnum(t - tau) * sp.diff(Xs, t).subs(t, tau), (tau, 0, t))
    n5a_inst.append(sp.simplify(sp.expand_trig(sp.expand(force - (memory + xi)))) == 0)
n5a = n5a_ode and all(n5a_inst)
# (b) thermal bath conditional on x0: q_k0 - c_k x0/w_k^2 ~ N(0, theta/w_k^2), p_k0 ~ N(0, theta), independent
dq1, dq2 = sp.symbols('dq1 dq2', real=True)
xi_t = sum(ck * (dqk * sp.cos(wk * t) + pk0 / wk * sp.sin(wk * t))
           for (wk, ck, dqk, pk0) in ((w1, c1, dq1, p10), (w2, c2, dq2, p20)))
xi_s = xi_t.subs(t, s)
prod_ = sp.expand(xi_t * xi_s)
moments = {dq1 ** 2: th / w1 ** 2, dq2 ** 2: th / w2 ** 2, p10 ** 2: th, p20 ** 2: th}
avg = 0
for term in sp.Add.make_args(prod_):
    cf, mon = term.as_coeff_Mul()
    pw = mon.as_powers_dict()
    rv = {v: pw.get(v, 0) for v in (dq1, dq2, p10, p20)}
    if sum(rv.values()) != 2 or any(e == 1 for e in rv.values()):
        continue
    val = term
    for v, e in rv.items():
        if e == 2:
            val = val / v ** 2 * moments[v ** 2]
    avg += val
n5b = sp.simplify(sp.expand_trig(avg - th * gam(t - s))) == 0
# (c) Foster reactance
z = sp.symbols('z')
Zs = c1 ** 2 / w1 ** 2 * z / (z ** 2 + w1 ** 2) + c2 ** 2 / w2 ** 2 * z / (z ** 2 + w2 ** 2)
a_, b_ = sp.symbols('a b', real=True)
ReZ = sp.simplify(sp.re(sp.expand_complex(Zs.subs(z, a_ + sp.I * b_))))
n5c_axis = sp.simplify(ReZ.subs(a_, 0)) == 0
# positivity of Re Z on Re z > 0: each term z/(z^2+w^2) has Re = a(|z|^2 + w^2)/|z^2 + w^2|^2 >= 0
term_re = sp.simplify(sp.re(sp.expand_complex((a_ + sp.I * b_) / ((a_ + sp.I * b_) ** 2 + w1 ** 2))))
target = a_ * (a_ ** 2 + b_ ** 2 + w1 ** 2) / ((a_ ** 2 - b_ ** 2 + w1 ** 2) ** 2 + 4 * a_ ** 2 * b_ ** 2)
n5c = n5c_axis and sp.simplify(term_re - target) == 0
check("N5 [exact] memory bath = Foster port: GLE kernel, <xi xi> = theta gamma (second FDT), positive-real transform",
      n5a and n5b and n5c, f"(a) {n5a}; (b) {n5b}; (c) axis {n5c_axis}, term form {sp.simplify(term_re - target) == 0}")

print(f"\nTOTAL: {sum(res)}/{len(res)} PASS")
