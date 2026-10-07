"""
Paper 53 — Passive Ports and the Explicit Formula: certificate.

Conventions. xi(w) = (1/2) w (w-1) pi^(-w/2) Gamma(w/2) zeta(w); the zeta port has impedance
    Z_xi(s) = (xi'/xi)(1/2 + s),   Re s > 0 (right half-plane = the "passive side").
Under RH, Hadamard gives the Foster form Z_xi(s) = sum_{gamma>0} 2s/(s^2+gamma^2): a series chain of parallel LC
tanks (C = 1/2, L_gamma = 2/gamma^2) resonating at the zero ordinates. Passive <=> positive-real <=> every
Pick (defect-Gram) matrix P_jk = (Z(s_j) + conj Z(s_k)) / (s_j + conj s_k) is positive semidefinite.

PRE-REGISTERED FALSIFIERS (written 2026-10-01, before the first run; every branch reportable)

K1 [exact, sympy] Port identities on a toy real-even polynomial P(z) with real zeros, E = P + iP', A = P, B = -P',
   Theta = E^#/E, m = B/A (z-plane, upper half-plane = passive side):
   (a) Cayley: m = i(1 - Theta)/(1 + Theta) identically;
   (b) kernel congruence: Pick_m(z, w) := (m(z) - m^#(wb))/(z - wb) equals pi K_E(w,z) / (A(z) A^#(wb)), where
       K_E(w,z) = [E(z)E^#(wb) - E^#(z)E(wb)] / (2 pi i (wb - z)) is the de Branges kernel (wb = conj w);
   (c) defect form: K_E(w,z) = E(z) E^#(wb) (1 - Theta(z) Theta^#(wb)) / (2 pi i (wb - z)) — the de Branges kernel is
       the defect Gram of the scattering function Theta;
   (d) s-plane: with s = -iz, Z(s) := -i m(is) equals Q'(s)/Q(s), Q(s) = P(is).
K2 [exact, sympy] Foster synthesis, matched pair.
   GOOD P = (z^2-1)(z^2-4)(z^2-9): Z(s) = sum_k 2s/(s^2+a_k^2) with every tank element L_k = 2/a_k^2, C_k = 1/2
   positive rational; the 10x10 Pick matrix on fixed Gaussian-rational points of Re s > 0 is positive definite
   (all leading principal minors > 0, exact).
   BAD P = (z^2-1)(z^2-z0^2)(z^2-conj(z0)^2), z0 = 2 + i/2: Z has a pole in Re s > 0 (exact), no positive Foster
   tank exists for that pair, and the Pick matrix on the same points plus s* = 1/2 + 2i - 1/8 is NOT positive
   definite (some leading minor <= 0, exact).
K3 [50-digit witness on zeta — necessary-only; a finite check cannot prove RH]
   (a) Re Z_xi(s) > 0 on the grid sigma in {0.01, 0.1, 0.5, 2}, t in {0, 0.5, ..., 100}  (Lagarias positivity);
   (b) the 12x12 Pick matrix at s_j = sigma_j + i gamma_k (k = 1..6, sigma in {0.05, 0.4}) is positive definite;
   (c) dissipation spectrum counts the zeros: (1/pi) int_0^{51.5} Re Z_xi(eps + i t) dt, eps = 0.01, is within 0.05
       of N = 10 (the number of zero ordinates in (0, 51.5));
   (d) Foster series check: at s = 0.5 + 10i, the truncated tank sum F_M = sum_{n<=M} 2s/(s^2+gamma_n^2) has error
       decreasing from M = 50 to M = 300, and with the standard zero-density tail 2s (log(g_M/2pi)+1)/(2 pi g_M)
       added, the relative error at M = 300 is < 0.01 (the tanks are the zeros);
   (e) CONTROL (matched pair): replace the zero pairs gamma_1, gamma_2 by the off-line quartet +-i z0, +-i conj z0,
       z0 = 17 + 0.5i (Z_bad = Z_xi + 2s/(s^2+z0^2) + 2s/(s^2+conj z0^2) - 2s/(s^2+g1^2) - 2s/(s^2+g2^2)):
       Re Z_bad < 0 at some grid point near s = 0.5 + 17i, and the Pick matrix of K3(b) augmented by
       s* = 0.25 + 17i is NOT positive definite. The detector must flag the control and pass zeta on the sample.
L: any failure of K1, K2, K3(a)-(e).
"""
import sys
import sympy as sp
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

# ============================================================ K1 exact identities
z, wb, s = sp.symbols('z wb s')
P = (z**2 - 1) * (z**2 - 4) * (z**2 - 9)
Pp = sp.diff(P, z)
E = P + sp.I * Pp
Es = P - sp.I * Pp                          # E^#(z) for real-coefficient P
A, B = P, -Pp
Th = Es / E
m = B / A
Ew, Esw = E.subs(z, wb), Es.subs(z, wb)     # E^#(wb) = conj E(w),  E(wb) = conj E^#(w)
Aw = A.subs(z, wb)
mw = m.subs(z, wb)                          # m^#(wb) = conj m(w) (real coefficients)
K_E = (E * Esw - Es * Ew) / (2 * sp.pi * sp.I * (wb - z))
a = sp.simplify(m - sp.I * (1 - Th) / (1 + Th)) == 0
b = sp.simplify((m - mw) / (z - wb) - sp.pi * K_E / (A * Aw)) == 0
c = sp.simplify(K_E - E * Esw * (1 - Th * (Ew / Esw)) / (2 * sp.pi * sp.I * (wb - z))) == 0   # conj Theta(w) = E(wb)/E^#(wb)
Q = sp.expand(P.subs(z, sp.I * s))
d = sp.simplify(-sp.I * m.subs(z, sp.I * s) - sp.diff(Q, s) / Q) == 0
check("K1 [exact] Cayley, de Branges kernel = Pick congruence = defect Gram of Theta, s-plane impedance Z = Q'/Q",
      a and b and c and d, f"(a)={a} (b)={b} (c)={c} (d)={d}")

# ============================================================ K2 exact Foster matched pair
def foster_and_pick(Pz, pts):
    Qs = sp.expand(Pz.subs(z, sp.I * s))
    Zs = sp.cancel(sp.diff(Qs, s) / Qs)
    poles = sp.roots(sp.Poly(sp.denom(Zs), s))
    rhp = [r for r in poles if sp.re(r) > 0]
    pf = sp.apart(Zs, s, full=True).doit()
    # Pick matrix (positive-real form) at Gaussian-rational points
    Zv = [sp.nsimplify(sp.expand(Zs.subs(s, p))) for p in pts]
    n = len(pts)
    M = sp.Matrix(n, n, lambda j, k: sp.simplify((Zv[j] + sp.conjugate(Zv[k])) / (pts[j] + sp.conjugate(pts[k]))))
    minors = [sp.nsimplify(sp.simplify(M[:r, :r].det())) for r in range(1, n + 1)]
    return Zs, rhp, minors
pts = [sp.Rational(1, 4) + sp.I * sp.Rational(k, 2) for k in range(1, 6)] + [sp.Rational(3, 2) + sp.I * k for k in range(0, 5)]
Zg, rhp_g, min_g = foster_and_pick(P, pts)
# tank elements for GOOD: Z = sum 2s/(s^2+a^2) -> C = 1/2, L = 2/a^2
tanks = [(sp.Rational(1, 2), sp.Rational(2, a_**2)) for a_ in (1, 2, 3)]
foster_ok = sp.simplify(Zg - sum(2 * s / (s**2 + a_**2) for a_ in (1, 2, 3))) == 0 and all(L > 0 and C > 0 for C, L in tanks)
good_pd = all(sp.re(x) > 0 and sp.im(x) == 0 for x in min_g)
z0 = 2 + sp.I / 2
Pbad = sp.expand((z**2 - 1) * (z**2 - z0**2) * (z**2 - sp.conjugate(z0)**2))
assert all(sp.im(cf) == 0 for cf in sp.Poly(Pbad, z).all_coeffs())
pts_bad = pts + [sp.Rational(1, 2) + 2 * sp.I - sp.Rational(1, 8)]
Zb, rhp_b, min_b = foster_and_pick(Pbad, pts_bad)
bad_detected = len(rhp_b) > 0 and any(not (sp.re(x) > 0) for x in min_b)
check("K2 [exact] Foster matched pair: real zeros -> positive LC tanks + PD Pick; off-line pair -> RHP pole + Pick fails",
      foster_ok and good_pd and len(rhp_g) == 0 and bad_detected,
      f"GOOD tanks (C,L)={[(str(C), str(L)) for C, L in tanks]}, minors>0={good_pd}; BAD RHP poles={rhp_b}, "
      f"first nonpositive minor index={next((i for i, x in enumerate(min_b) if not (sp.re(x) > 0)), None)}")

# RUN LOG (2026-10-01): K2 FAILED as pre-registered — the GOOD Pick matrix is not positive DEFINITE. Diagnosis: a finite
# LC network with 3 tanks has McMillan degree 6, so its Pick (defect-Gram) kernel has rank exactly 6; a 10x10 sample
# is PSD and singular. The pre-registration demanded the wrong criterion (PD instead of PSD). Retained.
# K2' below is POST-DIAGNOSIS (not blind): it tests the correct statement exactly.
def pick_exact(Zs, pts_):
    Zv = [sp.nsimplify(sp.expand(Zs.subs(s, p))) for p in pts_]
    n = len(pts_)
    return sp.Matrix(n, n, lambda j, k: sp.simplify((Zv[j] + sp.conjugate(Zv[k])) / (pts_[j] + sp.conjugate(pts_[k]))))
Mg = pick_exact(Zg, pts)
poles_g = [sp.I * a_ for a_ in (1, 2, 3)] + [-sp.I * a_ for a_ in (1, 2, 3)]
Fm = sp.Matrix(len(pts), 6, lambda j, c: 1 / (pts[j] - poles_g[c]))
gram_ok = sp.simplify(Mg - Fm * Fm.H) == sp.zeros(len(pts), len(pts))
rank_g = Fm.rank()
Mb = pick_exact(Zb, pts_bad)
diag_neg = sp.nsimplify(sp.simplify(Mb[len(pts_bad) - 1, len(pts_bad) - 1]))
check("K2' [exact, post-diagnosis] GOOD Pick = F F^* exactly (PSD) with rank 6 = 2 x tanks = minimal ledger dimension; "
      "BAD has a negative diagonal entry (not PSD)",
      gram_ok and rank_g == 6 and diag_neg < 0, f"Gram identity={gram_ok}, rank={rank_g}, BAD diagonal at s*={diag_neg}")

# ============================================================ K3 zeta witness (50 digits)
mp.mp.dps = 50
def xi_logderiv(w):
    if abs(w - 1) < mp.mpf(10) ** (-mp.mp.dps // 2):     # removable: 1/(w-1) + zeta'/zeta(w) -> Euler gamma at w = 1
        return 1 / w + mp.euler - mp.log(mp.pi) / 2 + mp.digamma(w / 2) / 2
    return 1 / w + 1 / (w - 1) - mp.log(mp.pi) / 2 + mp.digamma(w / 2) / 2 + mp.zeta(w, derivative=1) / mp.zeta(w)
# RUN LOG (2026-10-01): first run raised ZeroDivisionError at s = 0.5 (w = 1), a removable singularity of the
# formula (xi'/xi is analytic there; the polar term cancels zeta's pole). Checker artifact, fixed; K/L text unchanged.
def Zxi(s_):
    return xi_logderiv(mp.mpf(1) / 2 + s_)

# (a) positivity grid
ok_a, worst = True, mp.inf
for sig in ['0.01', '0.1', '0.5', '2']:
    for k in range(0, 201):
        v = mp.re(Zxi(mp.mpc(sig, k * mp.mpf('0.5'))))
        worst = min(worst, v); ok_a &= v > 0
check("K3(a) [50-digit witness] Re Z_xi(s) > 0 on the grid (Lagarias positivity)", ok_a, f"min Re Z = {mp.nstr(worst, 6)}")

gam = [mp.zetazero(n).imag for n in range(1, 7)]
def pick(vals, pts_):
    n = len(pts_)
    M = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            M[j, k] = (vals[j] + mp.conj(vals[k])) / (pts_[j] + mp.conj(pts_[k]))
    return M
pts_z = [mp.mpc(sg, g) for g in gam for sg in ('0.05', '0.4')]
vals_z = [Zxi(p) for p in pts_z]
ev = mp.eighe(pick(vals_z, pts_z), eigvals_only=True)
check("K3(b) [50-digit witness] Pick (defect-Gram) matrix of the zeta port near the first six zeros is PD", min(ev) > 0,
      f"min eigenvalue = {mp.nstr(min(ev), 6)}")

# (c) dissipation spectrum counts zeros
mp.mp.dps = 20
eps = mp.mpf('0.01')
gam_all = [mp.zetazero(n).imag for n in range(1, 12)]
bps = [mp.mpf(0)]
for g in gam_all:
    if g < 51.5:
        bps += [g - 1, g - eps * 20, g, g + eps * 20, g + 1]
bps = sorted(set([b for b in bps if 0 <= b <= 51.5])) + [mp.mpf('51.5')]
integral = mp.quad(lambda t: mp.re(Zxi(mp.mpc(eps, t))), bps) / mp.pi
Nexpect = sum(1 for g in gam_all if g < 51.5)
check("K3(c) [witness] (1/pi) * int Re Z_xi(eps+it) dt counts the zeros (the port's dissipation spectrum)",
      abs(integral - Nexpect) < 0.05, f"integral = {mp.nstr(integral, 8)}, N = {Nexpect}")

# (d) Foster series = the zeros as tanks
s0 = mp.mpc('0.5', '10')
target = Zxi(s0)
gm = [mp.zetazero(n).imag for n in range(1, 301)]
def foster(M_):
    return sum(2 * s0 / (s0**2 + g**2) for g in gm[:M_])
def tail(M_):
    G = gm[M_ - 1]
    return 2 * s0 * (mp.log(G / (2 * mp.pi)) + 1) / (2 * mp.pi * G)
e50, e300 = abs(foster(50) - target) / abs(target), abs(foster(300) - target) / abs(target)
e300t = abs(foster(300) + tail(300) - target) / abs(target)
check("K3(d) [witness] Foster tanks at the zero ordinates reproduce Z_xi (error shrinks; tail-corrected < 1%)",
      e300 < e50 and e300t < 0.01, f"rel.err M=50: {mp.nstr(e50, 4)}, M=300: {mp.nstr(e300, 4)}, M=300+tail: {mp.nstr(e300t, 4)}")

# (e) control: an off-line quartet replaces gamma_1, gamma_2
mp.mp.dps = 50
g1, g2 = gam[0], gam[1]
z0m = mp.mpc(17, '0.5')
def Zbad(s_):
    return (Zxi(s_) + 2 * s_ / (s_**2 + z0m**2) + 2 * s_ / (s_**2 + mp.conj(z0m)**2)
            - 2 * s_ / (s_**2 + g1**2) - 2 * s_ / (s_**2 + g2**2))
neg = min(mp.re(Zbad(mp.mpc(sg, t))) for sg in ('0.1', '0.25', '0.4', '0.6') for t in ('16.8', '17', '17.2'))
pts_c = pts_z + [mp.mpc('0.25', 17)]
ev_c = mp.eighe(pick([Zbad(p) for p in pts_c], pts_c), eigvals_only=True)
check("K3(e) [control] off-line quartet: Re Z_bad < 0 near s = 0.5+17i and the augmented Pick matrix is not PD",
      neg < 0 and min(ev_c) <= 0, f"min Re Z_bad = {mp.nstr(neg, 6)}, min eigenvalue = {mp.nstr(min(ev_c), 6)}")

print(f"\nP53: {sum(res)}/{len(res)} PASS")
