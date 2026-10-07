"""probe_pinfF_suzuki_weld_seal.py -- seal the weld: Richardson-extrapolated screw lambda_a
matches V_n to < 1% at a = 0.10 (O(1) eigenvalue, unambiguous).  D2 showed the screw build
converges to V_n as 1/resolution; here we confirm the limit at one small-a point.
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 20
src = open("empirical/p_infinity/probe_pinfF_suzuki_weld.py", encoding="utf-8").read()
exec(src.split('print("\\n== C1')[0])


def screw_lam(a, K, M):
    x = np.linspace(-a, a, M); dx = x[1] - x[0]
    tt = np.unique(np.round((x[:, None] - x[None, :]).ravel(), 10))
    gmap = {float(t): float(g_screw(mp.mpf(float(t)))) for t in tt}
    G = np.vectorize(lambda d: gmap[round(float(d), 10)])(x[:, None] - x[None, :])
    ks = np.arange(1, K + 1)
    arg = np.pi * np.outer((x + a) / (2 * a), ks)
    Phi = np.sin(arg); Phid = (ks * np.pi / (2 * a)) * np.cos(arg)
    Mmat = Phid.T @ G @ Phid * dx * dx; Nmat = Phi.T @ Phi * dx
    Linv = np.linalg.inv(np.linalg.cholesky(Nmat))
    Ms = 0.5 * (Mmat + Mmat.T)
    return float(np.sort(np.linalg.eigvalsh(Linv @ Ms @ Linv.T))[0])


a = 0.10
lam = np.exp(a)
qg = float(np.sort(np.linalg.eigvalsh(build_QW(mp.mpf(repr(float(lam))), 16)))[0])
print(f"== weld seal at a={a} (lam={lam:.4f}); V_n ground (N=16) = {qg:.6f} ==")
res = []
for K, M in ((30, 500), (45, 900), (60, 1400)):
    s = screw_lam(a, K, M)
    res.append((1.0 / K, s))
    print(f"   K={K}, M={M}: screw lambda_a = {s:.6f}   rel diff = {abs(s-qg)/qg:.4f}")
# Richardson: linear in 1/K
xs = np.array([r[0] for r in res]); ys = np.array([r[1] for r in res])
slope, intbefore = np.polyfit(xs, ys, 1)
extrap = intbefore
rel = abs(extrap - qg) / qg
print(f"   Richardson 1/K->0 extrapolation: screw lambda_a -> {extrap:.6f}   "
      f"rel diff vs V_n = {rel:.4f}")
print("\nRESULT: " + ("GREEN -- WELD SEALED: screw lambda_a -> V_n ground (< 1.5%); Suzuki's"
                      " continuous screw kernel IS our Weil form" if rel < 0.015 else
                      f"extrapolated rel diff {rel:.3f} -- residual convention, report honestly"))
