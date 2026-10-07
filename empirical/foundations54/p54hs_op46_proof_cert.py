r"""
Paper 54, Lemma 4.6 / Theorem 4.7 -- frequency-wise positivity of the total FDT violation (former Open Problem 4.6).
Certificate p54hs_op46_proof_cert.py.  The proof in the paper is general; this file checks its steps and consequences.
Exact arithmetic for every identity (sympy, Q(i)(l), l = log 2 a positive symbol); root locations are [witness] (mpmath
50 digits / float64 for random matrices).  No torch.

THE ARGUMENT BEING CHECKED.  P = -M - A real, M >= 0 symmetric, A antisymmetric, omega > 0, P + i omega invertible.
X := i omega - M (complex symmetric).  p(s) := det(X - sA) is even in s, so p(s) = q(s^2).  Jacobi:
    Delta := -Im Tr[(P + i omega)^-1 A] = Im[p'(1)/p(1)] = 2 Sum_r Im(u_r)/|1 - u_r|^2,   u_r = roots of q,
and every root has Im(u_r) = 2 omega |v|^2 v*Mv / beta^2 >= 0.

PRE-REGISTERED FALSIFIERS (written 2026-10-01 BEFORE the first run)
---------------------------------------------------------------------
P1 [exact, symbolic] n = 2, 3 with M = diag(m), generic A: Delta |det(P + i omega)|^2 equals
       2 omega Sum_{i<j} A_ij^2 (m_i + m_j) Prod_{k not in {i,j}} (m_k^2 + omega^2)   (nonnegative term by term).
   n = 4: the same identity FAILS (a Pfaffian term enters), yet Delta = Im[p'(1)/p(1)] holds exactly.  L: any other branch.
P2 [exact] For the Lindblad cells of p54hs_harada_sasa_cert.py (generators K, N, R, H; metrics as there), at the 12
   rational frequencies omega = k/3: p(s) = det(i omega + S_f - s A_f) (full superoperator; basis-independent) is even in
   s, and Im[p'(1)/p(1)] == Delta_tot(omega) computed independently via the Gram trace.  L: any mismatch or odd term.
P3 [witness, 50 digits] at those frequencies every root u_r of q has Im(u_r) >= -1e-40, and 2 Sum Im(u_r)/|1-u_r|^2
   reproduces Delta_tot to 1e-35.  L: a root with Im(u_r) < -1e-40.
P4 [witness, float64] 2000 random dissipative matrices (n = 2..12, antisymmetric part up to 100x, one in five with a
   rank-deficient symmetric part): every root of q has Im >= -1e-9 * scale, and the root formula reproduces Delta.
   L: a negative root imaginary part beyond tolerance.

RUN LOG (append-only)
---------------------
Run 1 (2026-10-01): STOPPED by hand after 30 min / 600 MB inside P1's fully symbolic n = 4 case; nothing printed, so
  no verdict was seen.  Checker change (falsifiers untouched): n = 2, 3 stay fully symbolic; n = 4 is checked with exact
  random rational parameters (3 seeds) -- one failing point suffices for "the closed form FAILS", and evenness / Jacobi
  are exact polynomial identities in (s, omega) at each point.
Run 2 (2026-10-01; p54hs_op46_run2.log): 3/4.  P1, P2, P3 PASS (P3: min Im u_r = 0.1667, formula error 2.7e-51).
  P4 FAILED as pre-registered: worst normalized Im u = -0.96.  RETAINED.  Diagnosis: the 3 offending values were spurious
  infinite generalized eigenvalues of the singular pencil at odd n (rank A = n - 1): |s| ~ 1e14, residual of X v = s A v
  0.16-0.94 (not eigenpairs), v in ker A (beta/(||A|| |v|^2) ~ 1e-18).  The lemma's q has degree rank(A)/2 and contains
  no such root: a checker artifact of the isfinite filter, not a counterexample.
Run 3 (p54hs_op46_run3.log): 4/5.  P4 fails again (retained); P4' (post-diagnosis, NOT blind: genuine eigenpairs only,
  count = rank A) PASSES on the same 1980 matrices: worst normalized Im u = +3.5e-13, formula = Delta throughout.
"""
import sys
import time
import numpy as np
import sympy as sp
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
T0 = time.time()
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

s, w = sp.symbols("s"), sp.symbols("omega", positive=True)
def rat(x): return sp.cancel(sp.together(sp.expand(x)))
def conjI(x): return x.subs(sp.I, -sp.I)

# ---------------------------------------------------------------- P1
def closed_form_check(n):
    m = sp.symbols(f"m1:{n+1}", nonnegative=True)
    av = sp.symbols(f"a1:{n*(n-1)//2+1}", real=True)
    A = sp.zeros(n, n); k = 0
    for i in range(n):
        for j in range(i + 1, n):
            A[i, j] = av[k]; A[j, i] = -av[k]; k += 1
    M = sp.diag(*m); P = -M - A
    Z = P + sp.I * w * sp.eye(n)
    dZ = sp.expand(Z.det())
    trAdjA = sp.expand((Z.adjugate() * A).trace())
    prod_ = sp.expand(trAdjA * conjI(dZ))
    Delta_num = sp.expand(-(prod_ - conjI(prod_)) / (2 * sp.I))     # Delta * |det Z|^2, a polynomial (no cancel)
    pred = 0
    for i in range(n):
        for j in range(i + 1, n):
            prod = 1
            for kk in range(n):
                if kk not in (i, j): prod *= (m[kk] ** 2 + w ** 2)
            pred += A[i, j] ** 2 * (m[i] + m[j]) * prod
    pred = sp.expand(2 * w * pred)
    X = sp.I * w * sp.eye(n) - M
    p = sp.expand((X - s * A).det())
    even = sp.expand(p - p.subs(s, -s)) == 0
    jacobi = sp.expand(trAdjA + sp.diff(p, s).subs(s, 1)) == 0 and sp.expand(p.subs(s, 1) - dZ) == 0   # Tr(adj Z A) = -p'(1)
    return sp.expand(Delta_num - pred) == 0, even, jacobi
def Im_s(p):
    r = rat(sp.diff(p, s).subs(s, 1) / p.subs(s, 1))
    return rat((r - conjI(r)) / (2 * sp.I))
def closed_form_check_numeric(n, seeds=(1, 2, 3)):
    """n = 4: the fully symbolic case is too heavy (run 1 stopped); use exact random rational parameters.
    Closed form: holds iff it holds at every sampled point (one failure suffices to show it FAILS);
    evenness and Jacobi are checked as exact polynomial identities in (s, omega) at each sampled point."""
    import random
    holds_all, even_all, jac_all = True, True, True
    for sd in seeds:
        rnd = random.Random(sd)
        m = [sp.Rational(rnd.randint(1, 9), rnd.randint(1, 5)) for _ in range(n)]
        A = sp.zeros(n, n)
        for i in range(n):
            for j in range(i + 1, n):
                v = sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 4)); A[i, j] = v; A[j, i] = -v
        M = sp.diag(*m); P = -M - A
        Z = P + sp.I * w * sp.eye(n)
        dZ = sp.expand(Z.det()); trAdjA = sp.expand((Z.adjugate() * A).trace())
        prod_ = sp.expand(trAdjA * conjI(dZ)); Delta_num = sp.expand(-(prod_ - conjI(prod_)) / (2 * sp.I))
        pred = 0
        for i in range(n):
            for j in range(i + 1, n):
                pr = 1
                for kk in range(n):
                    if kk not in (i, j): pr *= (m[kk] ** 2 + w ** 2)
                pred += A[i, j] ** 2 * (m[i] + m[j]) * pr
        holds_all &= sp.expand(Delta_num - 2 * w * pred) == 0
        X = sp.I * w * sp.eye(n) - M
        p = sp.expand((X - s * A).det())
        even_all &= sp.expand(p - p.subs(s, -s)) == 0
        jac_all &= sp.expand(trAdjA + sp.diff(p, s).subs(s, 1)) == 0 and sp.expand(p.subs(s, 1) - dZ) == 0
    return holds_all, even_all, jac_all
c2, e2, j2 = closed_form_check(2)
c3, e3, j3 = closed_form_check(3)
c4, e4, j4 = closed_form_check_numeric(4)
check("P1 closed form holds for n=2,3 and fails for n=4 (Pfaffian term); p even and Delta = Im p'(1)/p(1) for n=2,3,4",
      c2 and c3 and (not c4) and e2 and e3 and e4 and j2 and j3 and j4,
      f"closed form n=2,3,4: {c2},{c3},{c4}; even: {e2},{e3},{e4}; Jacobi: {j2},{j3},{j4}")

# ---------------------------------------------------------------- P2, P3 on the Lindblad cells
print("(loading the Lindblad generators: executes p54hs_harada_sasa_cert.py's verbatim helper block)")
src = open("p54q_lindblad_cert.py", encoding="utf-8").read()
i0 = src.index("\nI = sp.I\n") + 1
i1 = src.index("# ================================================================================================\nprint(\"== K6a")
ldl_src = src[src.index("def ldl_psd(M):"):src.index("# ----------------------------------------------------------------------------------------------", src.index("def ldl_psd(M):"))]
ns = {"sp": sp, "mp": mp}
exec(ldl_src, ns)
exec(src[i0:i1], ns)
G_, K_, N_, Rg_, Hh_, E_, vec_, unvec_, ell = ns["G"], ns["K"], ns["N"], ns["Rg"], ns["Hh"], ns["E"], ns["vec"], ns["unvec"], ns["ell"]
sx_, sy_ = ns["sx"], ns["sy"]
WB = [E_(0, 0), sx_, sy_]
def delta_tot_gram(g, f, wv):
    Bs = [g.Vbar(B) for B in WB]
    Gi = sp.Matrix(3, 3, lambda k, l: g.ip(f, Bs[k], Bs[l])).inv()
    Mi = (sp.I * wv * sp.eye(4) + g.Lt(f)).inv()
    tot = 0
    for l in range(3):
        for m_ in range(3):
            tot += Gi[l, m_] * (vec_(Bs[l]).H * g.C[f] * (Mi * (g.A(f) * vec_(Bs[m_]))))[0]
    tot = rat(tot)
    return rat(-(tot - conjI(tot)) / (2 * sp.I))
CELLS = [("K", "SLD", K_), ("K", "BKM", K_), ("N", "SLD", N_), ("N", "KMS", N_), ("N", "BKM", N_),
         ("R", "SLD", Rg_), ("H", "SLD", Hh_)]
WPTS = [sp.Rational(k, 3) for k in range(1, 13)]
ok2 = True; ok3 = True; worst_im = mp.mpf(1); maxerr = mp.mpf(0)
mp.mp.dps = 50
for gn, f, g in CELLS:
    Sf, Af = g.S(f), g.A(f)
    for wv in WPTS:
        Xs = sp.I * wv * sp.eye(4) + Sf - s * Af
        p = sp.expand(Xs.det())
        ok2 &= rat(p - p.subs(s, -s)) == 0
        r = rat(sp.diff(p, s).subs(s, 1) / p.subs(s, 1))
        imr = rat((r - conjI(r)) / (2 * sp.I))
        dt = delta_tot_gram(g, f, wv)
        ok2 &= rat(imr - dt) == 0
        # P3: roots of q(u) = p(sqrt u), as a polynomial in u, at l = log 2 (50 digits)
        pl = sp.Poly(p.subs(ell, sp.log(2)), s)
        coeffs = []
        for k in range(pl.degree(), -1, -1):
            coeffs.append(pl.coeff_monomial(s ** k))
        qc = [coeffs[k] for k in range(0, len(coeffs), 2)] if pl.degree() % 2 == 0 else None
        if qc is None:
            ok3 = False; continue
        def mpc_of(x):
            x = sp.sympify(x)
            return mp.mpc(mp.mpf(str(sp.N(sp.re(x), 60))), mp.mpf(str(sp.N(sp.im(x), 60))))
        qc = [mpc_of(x) for x in qc]
        while len(qc) > 1 and abs(qc[0]) < mp.mpf(10) ** -45: qc = qc[1:]
        roots = mp.polyroots(qc, maxsteps=200, extraprec=200) if len(qc) > 1 else []
        val = 2 * sum(mp.im(u) / abs(1 - u) ** 2 for u in roots) if roots else mp.mpf(0)
        dnum = mpc_of(dt.subs(ell, sp.log(2)))
        maxerr = max(maxerr, abs(val - dnum))
        for u in roots:
            worst_im = min(worst_im, mp.im(u))
            ok3 &= mp.im(u) >= -mp.mpf(10) ** -40
    ok3 &= maxerr < mp.mpf(10) ** -35
check("P2 [exact] p(s) even and Im[p'(1)/p(1)] == Delta_tot (Gram trace) at 12 frequencies, 7 Lindblad cells", ok2)
check("P3 [witness, 50 digits] all roots u_r of q in the closed upper half-plane; root formula reproduces Delta_tot", ok3,
      f"min Im u_r = {mp.nstr(worst_im, 5)}, max |formula - Delta| = {mp.nstr(maxerr, 3)}")

# ---------------------------------------------------------------- P4 random dissipative matrices
rng = np.random.default_rng(46)
ok4, cnt, worst = True, 0, np.inf
for n in range(2, 13):
    for t in range(180):
        Gm = rng.normal(size=(n, n)); Mm = (Gm @ Gm.T) * rng.choice([0.01, 0.1, 1.0])
        if t % 5 == 0:
            k = max(1, n // 3); Gk = rng.normal(size=(n, k)); Mm = Gk @ Gk.T
        Ar = rng.normal(size=(n, n)); Am = (Ar - Ar.T) / 2 * rng.choice([0.1, 1, 10, 100])
        P = -Mm - Am
        if np.max(np.linalg.eigvals(P).real) > -1e-9: continue
        omg = 10 ** rng.uniform(-2, 2)
        X = 1j * omg * np.eye(n) - Mm
        # roots s of det(X - sA) = generalized eigenvalues of (X, A): A^-1 X may not exist; use eig of pencil
        from scipy.linalg import eigvals as geig
        sr = geig(X, Am)
        sr = sr[np.isfinite(sr)]
        u = sr ** 2
        u = u[np.argsort(-np.abs(u))]
        # each u appears twice (s and -s): keep every second after sorting by value
        u_sorted = np.sort_complex(u)
        uniq = u_sorted[::2] if len(u_sorted) % 2 == 0 else u_sorted
        scale = max(1.0, np.abs(uniq).max()) if len(uniq) else 1.0
        cnt += 1
        if len(uniq):
            worst = min(worst, (np.imag(uniq) / scale).min())
            ok4 &= (np.imag(uniq) >= -1e-9 * scale).all()
        Dd = -np.imag(np.trace(np.linalg.solve(P + 1j * omg * np.eye(n), Am)))
        Df = 2 * np.sum(np.imag(uniq) / np.abs(1 - uniq) ** 2) if len(uniq) else 0.0
        ok4 &= abs(Dd - Df) <= 1e-6 * max(1.0, abs(Dd))
check("P4 [witness, float64] random dissipative matrices: roots in the closed upper half-plane; root formula = Delta", ok4,
      f"{cnt} matrices, worst normalized Im u = {worst:.2e}")

# ---------------------------------------------------------------- P4' POST-DIAGNOSIS (NOT blind)
# Diagnosis of the P4 failure (run 2): the 3 offending values were spurious infinite generalized eigenvalues of the
# singular pencil (X, A) at odd n (rank A = n - 1): |s| ~ 1e14, relative residual of X v = s A v 0.16-0.94 (not
# eigenpairs), beta/(||A|| |v|^2) ~ 1e-18 (v in ker A).  q has degree rank(A)/2 and never contains them.
# Fix: keep only genuine finite eigenpairs (relative residual < 1e-8); their number must equal rank(A).
from scipy.linalg import eig as geig2
rng = np.random.default_rng(46)
ok4p, cnt, worst, nspur = True, 0, np.inf, 0
for n in range(2, 13):
    for t in range(180):
        Gm = rng.normal(size=(n, n)); Mm = (Gm @ Gm.T) * rng.choice([0.01, 0.1, 1.0])
        if t % 5 == 0:
            k = max(1, n // 3); Gk = rng.normal(size=(n, k)); Mm = Gk @ Gk.T
        Ar = rng.normal(size=(n, n)); Am = (Ar - Ar.T) / 2 * rng.choice([0.1, 1, 10, 100])
        P = -Mm - Am
        if np.max(np.linalg.eigvals(P).real) > -1e-9: continue
        omg = 10 ** rng.uniform(-2, 2)
        X = 1j * omg * np.eye(n) - Mm
        lam, V = geig2(X, Am)
        keep = []
        for idx in range(n):
            s_ = lam[idx]; v = V[:, idx]
            if not np.isfinite(s_): continue
            r = np.linalg.norm(X @ v - s_ * Am @ v) / (np.linalg.norm(X @ v) + abs(s_) * np.linalg.norm(Am @ v))
            if r < 1e-8: keep.append(s_)
            else: nspur += 1
        rk = np.linalg.matrix_rank(Am)
        ok4p &= (len(keep) == rk)
        u = np.sort_complex(np.array(keep) ** 2)
        uniq = u[::2]
        cnt += 1
        if len(uniq):
            scale = max(1.0, np.abs(uniq).max())
            worst = min(worst, (np.imag(uniq) / scale).min())
            ok4p &= (np.imag(uniq) >= -1e-9 * scale).all()
        Dd = -np.imag(np.trace(np.linalg.solve(P + 1j * omg * np.eye(n), Am)))
        Df = 2 * np.sum(np.imag(uniq) / np.abs(1 - uniq) ** 2) if len(uniq) else 0.0
        ok4p &= abs(Dd - Df) <= 1e-6 * max(1.0, abs(Dd))
check("P4' [post-diagnosis, NOT blind] genuine finite eigenpairs only: count = rank A; roots in closed upper half-plane; formula = Delta",
      ok4p, f"{cnt} matrices, {nspur} spurious infinite eigenvalues discarded, worst normalized Im u = {worst:.2e}")

print(f"\nSUMMARY: {sum(res)}/{len(res)} checks passed  ({time.time() - T0:.1f}s)")
