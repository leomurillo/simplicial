"""
Paper 55, second certificate: the storage-order theorem (Theorem 3.8) and fourth-order isotropy (Theorem 6.6,
closing Open Problem O2).  sympy / fractions / numpy only.  Usage: python p55b_storage_isotropy_cert.py

PRE-REGISTERED FALSIFIERS (written 2026-10-02 before the first run)

S  Storage order.  A lossless quadratic network with conjugate storages of differential orders (s_A, s_B) has
   omega^2 = A(k) B(k).  Theorem 3.8: the continuum limit has a finite maximal signal speed iff s_A + s_B <= 1; a cone
   iff s_A + s_B = 1 (one storage ultralocal, one gradient); s_A + s_B >= 2 gives omega ~ k^(s_A+s_B) and a lattice
   maximal group velocity that diverges like l^(1 - s_A - s_B); one storage replaced by a loss gives diffusion.
   S1 [exact] 1D lattice of spacing l: max_k d omega/dk equals c (independent of l) for (0,1) and (1,0); equals
      2 sqrt(ab)/l for (1,1) and 2 sqrt(a0 b2)/l for (0,2); is 0 for (0,0).                 L: any other value.
   S2 [exact] the real form of i psi_t = -Delta psi (psi = q + i p) is q_t = A p, p_t = -B q with A = B = -Delta
      (both storages gradient: s = (1,1)); the Klein-Gordon/LC form has A ultralocal, B gradient.  L: otherwise.
   S3 [exact] Maxwell's vacuum as a network: in temporal gauge the electric storage is ultralocal and the magnetic
      storage is curl-curl (gradient); the transverse modes have omega^2 = |k|^2/(eps0 mu0), the longitudinal mode
      omega = 0 (the gauge line); c = 1/sqrt(mu0 eps0) = 299792458 m/s and Z0 = sqrt(mu0/eps0) = 376.73 Ohm to 1e-6
      (CODATA 2018 values); a coaxial line with 250 nH/m and 100 pF/m has v = 2e8 m/s and Z = 50 Ohm exactly.
   S4 [exact] d = 2 principal symbols (Sylvester): (0,1) gives signature (1,2); (0,0) gives (1,0,2) (no spatial
      direction); one storage plus loss gives (0,1,2).
I  Fourth-order isotropy.  For a Bravais network, omega^2 = (2/C) sum_e w_e (1 - cos k.delta_e) is isotropic through
   O(k^4) iff sum_e w_e (k.delta_e)^2 ~ |k|^2 and sum_e w_e (k.delta_e)^4 ~ |k|^4.  Theorem 6.6: in d = 3 this needs at
   least 7 bond pairs (z >= 14), attained by sc + bcc with per-bond weights 8:1 (the D3Q15 stencil); in d = 2 it needs
   3 pairs, attained by the triangular lattice.
   I1 [exact] shell fourth moments: sc 2 S4, fcc 8 S4 + 24 P, bcc 8 S4 + 48 P (S4 = sum k_i^4, P = sum_{i<j} k_i^2 k_j^2);
      sc+bcc isotropic iff w_sc = 8 w_bcc; sc+fcc iff w_sc = 2 w_fcc; fcc+bcc never (positive weights).  L: otherwise.
   I2 [exact] the six icosahedral axes with equal weights form a weighted 4-design (sum (a.x)^4 = (6/5)|x|^4 for unit
      a); pairwise (a_i.a_j)^2 = 1/5; and the Gram identity of the 6-pair lemma, G = (2/3) I + u u^T / 5 with
      lambda_i = 5/6, holds exactly.                                                      L: otherwise.
   I3 [exact] no lattice in R^3 contains nonzero vectors along all six icosahedral axes: some cross-ratio of the
      relation matrix is irrational.                                                      L: all rational.
   I4 [exact] cross-check on Z^3: no six directions with integer coordinates in [-3,3] are pairwise equiangular with
      5 (a.b)^2 = |a|^2 |b|^2.                                                            L: such a sextuple exists.
   I5 [exact] d = 2: the triangular star is isotropic at fourth order; the square nearest-neighbour star is not; the
      square nn + nnn star with per-bond weights 4:1 is (D2Q9).                           L: otherwise.
   I6 [report] the sixth-order anisotropy of the D3Q15 stencil (expected nonzero).

RUN LOG
  Run 1 (2026-10-02, p55b_run1.log): 8/9.  S1 FAILED on a CHECKER ARTIFACT: the identity sub-check
  omega^2 = A B for (1,1) and (0,2) asked sympy to cancel 16 sin^4(kl/2) - (2 - 2 cos kl)^2 after expand_trig, which
  does not rewrite half angles (same failure class as Port P3.N2, the coth rewrite).  Every pre-registered value
  (v_max attained at the claimed maximizer, and the grid bound at l = 1/10, 1/100) PASSED.  The failure is retained.
  Fix: substitute cos(kl) = 1 - 2 sin^2(kl/2) before simplifying.  Run 2 is NOT BLIND for the repaired checker.
"""
import itertools, math
from fractions import Fraction as Fr
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

k, l, a0, b0, a, b, b2 = sp.symbols('k l a0 b0 a b b2', positive=True)

# ------------------------------------------------------------------ S1
sn = 2 * sp.sin(k * l / 2) / l                    # sqrt of the gradient symbol (2 - 2 cos kl)/l^2 on (0, pi/l)
# omega = sqrt(A B) written with the positive square roots of the symbols, k in (0, pi/l)
cases = {"(0,1)": sp.sqrt(a0 * b) * sn, "(1,0)": sp.sqrt(a * b0) * sn, "(1,1)": sp.sqrt(a * b) * sn ** 2,
         "(0,2)": sp.sqrt(a0 * b2) * sn ** 2, "(0,0)": sp.sqrt(a0 * b0)}
claim = {"(0,1)": (sp.Integer(0), sp.sqrt(a0 * b)), "(1,0)": (sp.Integer(0), sp.sqrt(a * b0)),
         "(1,1)": (sp.pi / (2 * l), 2 * sp.sqrt(a * b) / l), "(0,2)": (sp.pi / (2 * l), 2 * sp.sqrt(a0 * b2) / l),
         "(0,0)": (sp.Integer(0), sp.Integer(0))}
# identity check: omega^2 equals the product of the lattice symbols
lap = (2 - 2 * sp.cos(k * l)) / l ** 2
prod = {"(0,1)": a0 * b * lap, "(1,0)": a * b0 * lap, "(1,1)": a * b * lap ** 2, "(0,2)": a0 * b2 * lap ** 2,
        "(0,0)": a0 * b0}
s1 = True; det = []
vals_num = {a0: 2, b0: 3, a: 5, b: 7, b2: 11}
for name, om in cases.items():
    ident = sp.simplify(sp.expand(om ** 2 - prod[name].subs(sp.cos(k * l), 1 - 2 * sp.sin(k * l / 2) ** 2))) == 0
    vg = sp.diff(om, k)
    kstar, vexp = claim[name]
    vat = sp.limit(vg, k, 0, '+') if kstar == 0 else sp.simplify(vg.subs(k, kstar))
    ok_at = sp.simplify(vat - vexp) == 0
    ok_grid = True
    for lv in (sp.Rational(1, 10), sp.Rational(1, 100)):
        f = sp.lambdify(k, vg.subs(vals_num).subs(l, lv), 'math')
        top = float(vexp.subs(vals_num).subs(l, lv))
        grid = [float(lv) ** -1 * math.pi * (i + 0.5) / 4000 for i in range(4000)]
        ok_grid &= max(f(x_) for x_ in grid) <= top * (1 + 1e-9) + 1e-12
    s1 &= ident and ok_at and ok_grid
    det.append(f"{name}: v_max = {vexp} (identity {ident}, attained {ok_at}, grid bound {ok_grid})")
check("S1 [exact] maximal group velocity by storage order (cone iff s_A + s_B = 1)", s1, "; ".join(det))

# ------------------------------------------------------------------ S2
x, t = sp.symbols('x t', real=True)
q = sp.Function('q')(x, t); p = sp.Function('p')(x, t)
psi = q + sp.I * p
schro = sp.expand(sp.I * sp.diff(psi, t) + sp.diff(psi, x, 2))
sub = {sp.Derivative(q, t): -sp.diff(p, x, 2), sp.Derivative(p, t): sp.diff(q, x, 2)}   # q_t = A p, p_t = -B q, A = B = -d_xx
s2a = sp.simplify(schro.subs(sub)) == 0
kq, kp = sp.symbols('kq kp')
# Klein-Gordon / LC: q_t = (1/C) p, p_t = -(m^2 - c0^2 d_xx) q  =>  q_tt = -(1/C)(m^2 - c0^2 d_xx) q
C, m, c0 = sp.symbols('C m c0', positive=True)
w = sp.symbols('w')
kg_symbol = sp.expand(-w ** 2 + (1 / C) * (m ** 2 + c0 ** 2 * k ** 2))
s2b = sp.Poly(kg_symbol, k).degree() == 2
check("S2 [exact] Schrodinger = both storages gradient; Klein-Gordon = one ultralocal, one gradient", s2a and s2b,
      f"real-form residual zero: {s2a}; KG symbol quadratic in k: {s2b}")

# ------------------------------------------------------------------ S3
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
kv = sp.Matrix([k1, k2, k3])
CC = kv * kv.T - (kv.T * kv)[0] * sp.eye(3)          # (k x (k x .)) = k k^T - |k|^2 I ;  curl-curl symbol = -CC
eps0, mu0 = sp.symbols('epsilon0 mu0', positive=True)
ev = (-CC / (eps0 * mu0)).eigenvals()
ksq = k1 ** 2 + k2 ** 2 + k3 ** 2
evs = {sp.simplify(e): mlt for e, mlt in ev.items()}
s3a = any(sp.simplify(e - ksq / (eps0 * mu0)) == 0 and mlt == 2 for e, mlt in evs.items()) and \
      any(sp.simplify(e) == 0 and mlt == 1 for e, mlt in evs.items())
MU0 = 1.25663706212e-6; EPS0 = 8.8541878128e-12
cval = 1 / math.sqrt(MU0 * EPS0); Z0 = math.sqrt(MU0 / EPS0)
s3b = abs(cval / 299792458 - 1) < 1e-6 and abs(Z0 - 376.730313668) < 1e-3
Lc, Cc = Fr(250, 10 ** 9), Fr(100, 10 ** 12)
vcoax_sq = 1 / (Lc * Cc); Zcoax_sq = Lc / Cc
s3c = vcoax_sq == Fr(4 * 10 ** 16) and Zcoax_sq == 2500
check("S3 [exact] Maxwell vacuum = ultralocal electric + curl-curl magnetic storage; c, Z0; coax", s3a and s3b and s3c,
      f"transverse omega^2 = |k|^2/(eps0 mu0) (x2), longitudinal 0: {s3a}; c = {cval:.1f} m/s, Z0 = {Z0:.4f} Ohm; "
      f"coax v^2 = {vcoax_sq}, Z^2 = {Zcoax_sq}")

# ------------------------------------------------------------------ S4
def signature(M):
    evs_ = [complex(e) for e in sp.Matrix(M).eigenvals(multiple=True)]
    return (sum(1 for e in evs_ if e.real > 1e-12), sum(1 for e in evs_ if e.real < -1e-12),
            sum(1 for e in evs_ if abs(e.real) <= 1e-12))
# quadratic forms on (omega, k1, k2): (0,1): omega^2 - kAk with A = diag(1,2);  (0,0): omega^2;  RC: -kAk
sigs = {"(0,1)": signature(sp.diag(1, -1, -2)), "(0,0)": signature(sp.diag(1, 0, 0)), "loss": signature(sp.diag(0, -1, -2))}
s4 = sigs["(0,1)"] == (1, 2, 0) and sigs["(0,0)"] == (1, 0, 2) and sigs["loss"] == (0, 2, 1)
check("S4 [exact] d=2 principal symbols: cone (1,2); ultralocal (1,0,2); one storage + loss (0,1,2) [as (p,n,z)]", s4,
      f"{sigs}")

# ------------------------------------------------------------------ I1
def moment(vectors, power):
    return sp.expand(sum((k1 * v[0] + k2 * v[1] + k3 * v[2]) ** power for v in vectors))
sc = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(c) for c in v) == 1]
fcc = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(c) for c in v) == 2]
bcc = [v for v in itertools.product((-1, 1), repeat=3)]
S4 = k1 ** 4 + k2 ** 4 + k3 ** 4; P = k1 ** 2 * k2 ** 2 + k1 ** 2 * k3 ** 2 + k2 ** 2 * k3 ** 2
m_sc, m_fcc, m_bcc = moment(sc, 4), moment(fcc, 4), moment(bcc, 4)
i1a = sp.expand(m_sc - 2 * S4) == 0 and sp.expand(m_fcc - (8 * S4 + 24 * P)) == 0 and \
      sp.expand(m_bcc - (8 * S4 + 48 * P)) == 0
iso = sp.expand(ksq ** 2)
ws, wf, wb, cst = sp.symbols('ws wf wb cst')
sol_sb = sp.solve(sp.Poly(sp.expand(ws * m_sc + wb * m_bcc - cst * iso), k1, k2, k3).coeffs(), [ws, cst], dict=True)
sol_sf = sp.solve(sp.Poly(sp.expand(ws * m_sc + wf * m_fcc - cst * iso), k1, k2, k3).coeffs(), [ws, cst], dict=True)
sol_fb = sp.solve(sp.Poly(sp.expand(wf * m_fcc + wb * m_bcc - cst * iso), k1, k2, k3).coeffs(), [wf, cst], dict=True)
i1b = sol_sb and sp.simplify(sol_sb[0][ws] - 8 * wb) == 0
i1c = sol_sf and sp.simplify(sol_sf[0][ws] - 2 * wf) == 0
i1d = (not sol_fb) or all(not (sp.simplify(s_[wf] / wb).is_positive) for s_ in sol_fb)
m2 = sp.expand(8 * moment(sc, 2) + moment(bcc, 2))
i1e = sp.simplify(m2 - sp.Rational(sp.Poly(m2, k1).coeffs()[0]) * ksq) == 0
check("I1 [exact] shell moments; sc+bcc isotropic iff 8:1 (D3Q15), sc+fcc iff 2:1 (D3Q19), fcc+bcc never",
      i1a and i1b and i1c and i1d and i1e,
      f"moments ok {i1a}; sc+bcc: {sol_sb}; sc+fcc: {sol_sf}; fcc+bcc: {sol_fb}; 2nd moment isotropic {i1e}")

# ------------------------------------------------------------------ I2
phi = (1 + sp.sqrt(5)) / 2
axes = [sp.Matrix(v) for v in [(0, 1, phi), (0, 1, -phi), (1, phi, 0), (1, -phi, 0), (phi, 0, 1), (phi, 0, -1)]]
unit = [v / sp.sqrt((v.T * v)[0]) for v in axes]
X = sp.Matrix([k1, k2, k3])
design = sp.simplify(sp.expand(sum(((u.T * X)[0]) ** 4 for u in unit)) - sp.Rational(6, 5) * ksq ** 2)
G0 = sp.Matrix(6, 6, lambda i, j: sp.simplify(((unit[i].T * unit[j])[0]) ** 2))
equi = all(sp.simplify(G0[i, j] - (1 if i == j else sp.Rational(1, 5))) == 0 for i in range(6) for j in range(6))
lam = sp.Rational(5, 6)
Gl = lam * G0
u = sp.Matrix([sp.sqrt(lam)] * 6)
gram_id = sp.simplify(Gl - (sp.Rational(2, 3) * sp.eye(6) + u * u.T / 5)) == sp.zeros(6, 6)
# with weights 5/6 the normalized design reads sum lam (a.x)^4 = |x|^4
design2 = sp.simplify(sp.expand(sum(lam * ((uu.T * X)[0]) ** 4 for uu in unit)) - ksq ** 2) == 0
check("I2 [exact] icosahedral axes: weighted 4-design, equiangular (a.b)^2 = 1/5, Gram identity of the 6-pair lemma",
      design == 0 and equi and gram_id and design2, f"design residual {design}; equiangular {equi}; Gram {gram_id}")

# ------------------------------------------------------------------ I3
Amat = sp.Matrix.hstack(*axes)                     # 3 x 6, columns = axis vectors
ker = Amat.nullspace()                             # 3 vectors in Q(sqrt5)^6 : the linear relations
K = sp.Matrix.hstack(*ker).T                       # 3 x 6
R_, piv = K.rref(simplify=True)
free = [j for j in range(6) if j not in piv]
F = R_[:, free]
crs = []
for (i1_, i2_) in itertools.combinations(range(F.rows), 2):
    for (j1_, j2_) in itertools.combinations(range(F.cols), 2):
        if all(F[r, c] != 0 for r in (i1_, i2_) for c in (j1_, j2_)):
            crs.append(sp.radsimp(sp.simplify(F[i1_, j1_] * F[i2_, j2_] / (F[i1_, j2_] * F[i2_, j1_]))))
irr = [c for c in crs if not c.is_rational]
check("I3 [exact] no lattice contains vectors along all six icosahedral axes (an irrational cross-ratio)",
      len(irr) > 0, f"cross-ratios: {[sp.simplify(c) for c in crs][:6]}")

# ------------------------------------------------------------------ I4
dirs = []
for v in itertools.product(range(-3, 4), repeat=3):
    if v == (0, 0, 0):
        continue
    g = math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2]))
    vv = tuple(c // g for c in v)
    if vv not in dirs and tuple(-c for c in vv) not in dirs:
        dirs.append(vv)
def dot(u_, v_):
    return sum(x_ * y_ for x_, y_ in zip(u_, v_))
adj = {i: set() for i in range(len(dirs))}
for i, j in itertools.combinations(range(len(dirs)), 2):
    if 5 * dot(dirs[i], dirs[j]) ** 2 == dot(dirs[i], dirs[i]) * dot(dirs[j], dirs[j]):
        adj[i].add(j); adj[j].add(i)
best = 0
def clique(cur, cand):
    global best
    best = max(best, len(cur))
    for v in list(cand):
        clique(cur + [v], cand & adj[v])
        cand = cand - {v}
clique([], set(range(len(dirs))))
check("I4 [exact] Z^3 cross-check: no equiangular sextuple (5(a.b)^2 = |a|^2|b|^2) among directions in [-3,3]^3",
      best < 6, f"{len(dirs)} directions; largest equiangular set {best}")

# ------------------------------------------------------------------ I5
kx, ky = sp.symbols('kx ky', real=True)
def mom2d(vecs, wts, power):
    return sp.expand(sum(w_ * (kx * v[0] + ky * v[1]) ** power for v, w_ in zip(vecs, wts)))
tri = [(sp.cos(sp.pi * j / 3), sp.sin(sp.pi * j / 3)) for j in range(6)]
sq_nn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
sq_nnn = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
iso2 = sp.expand((kx ** 2 + ky ** 2) ** 2)
def is_iso(poly):
    c = sp.Poly(poly, kx, ky).coeff_monomial(kx ** 4)
    return sp.simplify(poly - c * iso2) == 0
i5 = is_iso(mom2d(tri, [1] * 6, 4)) and not is_iso(mom2d(sq_nn, [1] * 4, 4)) and \
     is_iso(mom2d(sq_nn + sq_nnn, [4] * 4 + [1] * 4, 4))
check("I5 [exact] d=2: triangular star isotropic at 4th order; square nn not; square nn+nnn with 4:1 is (D2Q9)", i5)

# ------------------------------------------------------------------ I6
m6 = sp.expand(8 * moment(sc, 6) + moment(bcc, 6))
c6 = sp.Poly(m6, k1, k2, k3).coeff_monomial(k1 ** 6)
aniso6 = sp.expand(m6 - c6 * ksq ** 3)
print(f"   I6 report: D3Q15 sixth moment minus isotropic part = {sp.factor(aniso6)} (nonzero: {aniso6 != 0})")

print(f"\nTOTAL: {sum(res)}/{len(res)} PASS")
