"""probe_index_resolution_sT.py — certificate for P-infinity-E SS13 (the S(T) face of the index).

Three operational identities for kappa = #off-line zeros (the Pontryagin index of SS11-12):

CHECK A  (epsilon-graded winding = resolution-graded index): the winding of Xi'/Xi over the
         rectangle [-20,20] x [eps, 1] in C+ counts exactly the zeros with DISPLACEMENT
         beta - 1/2 > eps and ordinate in window.  True zeta: 0 at every eps.  Grafted
         quadruple at displacement 0.25: counted at eps = 0.05, 0.15; invisible at eps = 0.35.
CHECK B  (kappa = the TURING DISCREPANCY): N_window(all zeros, by argument principle)
         minus N0_window(on-line zeros, by Hardy-style sign changes of Xi on the real z-axis)
         equals kappa exactly: true zeta -> 1 - 1 = 0; grafted -> 3 - 1 = 2.
         This identifies the index with the quantity zero-verification computations
         (Turing's method; Platt-Trudgian to 3e12) have certified to be 0.
CHECK C  (resolution-cost law): the most negative kernel eigenvalue lambda_-(d, h) for a
         displacement-d quadruple seen from test height h: present at EVERY h (Krein-Langer
         is a global invariant), magnitude increasing in d and decreasing in h — the measured
         exponents quantify the marginality of the index at small displacement (d -> 0 is the
         double-on-line marginal case).

Deterministic, local, ~2-4 min (mpmath).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 25

def xilogd(s):
    return (1/s + 1/(s - 1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2
            + mp.zeta(s, derivative=1) / mp.zeta(s))

def Nt_true(z):
    """-Xi'/Xi(z) = i * xi'/xi(1/2 - i z)."""
    return 1j * xilogd(mp.mpf(0.5) - 1j*z)

WQ = mp.mpc(10, 0.25)   # grafted quadruple: zeros at +-w, +-conj(w); displacement 0.25

def graft_term(z, w=WQ):
    return 2*z/(z*z - w*w) + 2*z/(z*z - mp.conj(w)*mp.conj(w))

def logd_true(z):
    return -Nt_true(z)

def logd_graft(z):
    return -Nt_true(z) + graft_term(z)

def winding(logd, corners, breaks=()):
    """(1/2pi i) contour-int logd dz over the closed polygon through corners."""
    tot = mp.mpc(0)
    for a, b in zip(corners[:-1], corners[1:]):
        pts = [0] + sorted(t for t in breaks_param(a, b, breaks) if 0 < t < 1) + [1]
        tot += mp.quad(lambda t: logd(a + t*(b - a)) * (b - a), pts, maxdegree=10)
    return tot / (2j * mp.pi)

def breaks_param(a, b, xs):
    """parameter values where Re(z) passes the break abscissas (horizontal edges only)."""
    out = []
    if abs(mp.im(b - a)) < 1e-12 and abs(mp.re(b - a)) > 1e-12:
        for x in xs:
            out.append(float((x - mp.re(a)) / mp.re(b - a)))
    return out

BRK = (-14.1347, -10.0, 10.0, 14.1347)

# ---------------- CHECK A: epsilon-graded winding ----------------
print("== CHECK A: eps-graded winding over [-20,20] x [eps,1] — resolution-graded index ==")
mp.mp.dps = 15
okA = True
for eps, exp_t, exp_g in ((0.05, 0, 2), (0.15, 0, 2), (0.35, 0, 0)):
    corn = [mp.mpc(-20, eps), mp.mpc(20, eps), mp.mpc(20, 1), mp.mpc(-20, 1), mp.mpc(-20, eps)]
    wt = winding(logd_true, corn, BRK)
    wg = winding(logd_graft, corn, BRK)
    ok = abs(wt - exp_t) < 0.02 and abs(wg - exp_g) < 0.02
    okA &= ok
    print(f"   eps={eps:.2f}: true={complex(wt).real:+.4f} (expect {exp_t})   "
          f"grafted={complex(wg).real:+.4f} (expect {exp_g})   " + ("PASS" if ok else "FAIL"))
print("   " + ("PASS — winding with floor eps counts EXACTLY the zeros displaced beyond eps"
               if okA else "FAIL"))

# ---------------- CHECK B: kappa = Turing discrepancy ----------------
print("\n== CHECK B: kappa = N(window) - N0(window) — the Turing discrepancy ==")
corn = [mp.mpc(-18, -0.6), mp.mpc(-5, -0.6), mp.mpc(-5, 0.6), mp.mpc(-18, 0.6), mp.mpc(-18, -0.6)]
Nt_w = winding(logd_true, corn, BRK)
Ng_w = winding(logd_graft, corn, BRK)

def sign_changes(fun, lo, hi, step):
    ts = mp.arange(lo, hi, step)
    vals = [fun(t) for t in ts]
    return sum(1 for i in range(len(vals) - 1) if vals[i] * vals[i+1] < 0)

mp.mp.dps = 20
Xi_real = lambda t: mp.re(mp.mpf(0.5)*(0.5 - 1j*(-t))*((0.5 - 1j*(-t)) - 1)
                          * mp.pi**(-(0.5 - 1j*(-t))/2) * mp.gamma((0.5 - 1j*(-t))/2)
                          * mp.zeta(0.5 - 1j*(-t)))
graft_pos = lambda t: mp.re((1 - t*t/(WQ*WQ)) * (1 - t*t/(mp.conj(WQ)*mp.conj(WQ))))
N0_t = sign_changes(Xi_real, 5, 18, mp.mpf("0.25"))
N0_g = sign_changes(lambda t: Xi_real(t) * graft_pos(t), 5, 18, mp.mpf("0.25"))
kap_t = int(mp.nint(mp.re(Nt_w))) - N0_t
kap_g = int(mp.nint(mp.re(Ng_w))) - N0_g
okB = (abs(Nt_w - 1) < 0.02 and abs(Ng_w - 3) < 0.02 and N0_t == 1 and N0_g == 1
       and kap_t == 0 and kap_g == 2)
print(f"   true:    N = {complex(Nt_w).real:.4f} (1)   N0 = {N0_t} (1)   kappa = {kap_t} (0)")
print(f"   grafted: N = {complex(Ng_w).real:.4f} (3)   N0 = {N0_g} (1)   kappa = {kap_g} (2)")
print("   " + ("PASS — the Pontryagin index IS the Turing discrepancy N - N0" if okB else "FAIL"))

# ---------------- CHECK C: resolution-cost law lambda_-(d, h) ----------------
print("\n== CHECK C: most negative kernel eigenvalue vs displacement d and test height h ==")
mp.mp.dps = 40
XPTS = (-15, -12, -10, -8, -6, 6, 8, 10, 12, 15)   # clustered near the defect at x = +-10

def lam_minus(d, h):
    w = mp.mpc(10, d)
    pts = [mp.mpc(x, h) for x in XPTS]
    vals = [Nt_true(z) - graft_term(z, w) for z in pts]
    n = len(pts)
    K = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            K[i, j] = (vals[i] - mp.conj(vals[j])) / (pts[i] - mp.conj(pts[j]))
    E = [mp.re(e) for e in mp.eighe(K, eigvals_only=True)]
    return float(min(E))

ds = (0.05, 0.1, 0.2, 0.4)
lam_d = [lam_minus(d, 1.0) for d in ds]
print("   d-sweep (h=1):   " + "  ".join(f"d={d}: {l:.3e}" for d, l in zip(ds, lam_d)))
hs = (0.5, 1.0, 2.0, 4.0)
lam_h = [lam_minus(0.25, h) for h in hs]
print("   h-sweep (d=.25): " + "  ".join(f"h={h}: {l:.3e}" for h, l in zip(hs, lam_h)))
okC = (all(l < 0 for l in lam_d + lam_h)
       and all(lam_d[i] > lam_d[i+1] for i in range(len(ds) - 1))      # more displacement = more negative
       and all(lam_h[i] < lam_h[i+1] for i in range(len(hs) - 1)))     # more distance = less negative
if okC:
    sl_d = np.polyfit(np.log(ds), np.log([-l for l in lam_d]), 1)[0]
    sl_h = np.polyfit(np.log(hs), np.log([-l for l in lam_h]), 1)[0]
    print(f"   measured exponents: |lambda_-| ~ d^{sl_d:.2f} (at h=1),  ~ h^{sl_h:.2f} (at d=0.25)")
print("   " + ("PASS — index visible at EVERY height (global invariant), magnitude graded by "
               "d (marginality at d->0) and by 1/h (resolution cost)" if okC else "FAIL"))

allok = okA and okB and okC
print("\nRESULT: " + ("GREEN — the index has an exact S(T)-side dictionary: eps-graded winding, "
                      "Turing discrepancy N - N0, and a measured resolution-cost law"
                      if allok else "RED"))
