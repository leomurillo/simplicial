r"""
probe_lp_transport_offaxis.py -- certificate for N7 Remark 5.11 (the Hadamard Gaussian off the axis).

Inside the critical strip the CCM/CvS approximant F_lambda = xihat_lambda/xihat_lambda(0) differs from
Xi/Xi(0) mainly by the Gaussian exp((S_Xi - S(lambda)) z^2): F_lambda lacks the zeros above the
Nyquist height, and their Hadamard factors contribute exp(-(S_Xi - S) z^2) at leading order.
The multiplier exp(-c z^2), c = S_Xi - S(lambda) >= 0, is itself Laguerre-Polya, so the corrected
family F_lambda(z) exp(-c z^2) is still real-rooted and still normalized at 0.

CHECKS (zeta, lambda = 3.0 and 4.0, sample points in 0 < Im z < 1/2):
  O1  the corrected error is at least 100x smaller than the raw error at every sample point;
  O2  both errors decrease from lambda = 3 to lambda = 4 at every sample point.

mpmath only; deterministic; local; ~3 min.
"""
import sys
import math

sys.path.insert(0, r"C:/Projects/simplicial/empirical/connes_route")
import mpmath as mp
import lp_transport_core as core
import probe_lp_transport_zeta as pz

sys.stdout.reconfigure(encoding="utf-8")


def Xi_c(z):
    s = mp.mpf(1) / 2 + 1j * z
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def main():
    mp.mp.dps = 40
    S_Xi = -mp.diff(core.Xi_zeta, mp.mpf(0), 2) / (2 * core.Xi_zeta(mp.mpf(0)))
    pts = [mp.mpc(5, "0.3"), mp.mpc(10, "0.45"), mp.mpc(13, "0.25"), mp.mpc(20, "0.2"), mp.mpc(30, "0.4")]
    res = {}
    for lam_s in ("3.0", "4.0"):
        lam = mp.mpf(lam_s)
        N = int(2 * float(lam_s) ** 2 * 2 * math.log(float(lam_s))) + 24
        mp.mp.dps = pz.dps_for(lam)
        r = pz.run_one(lam, N)
        xi, L, S = r["xi"], r["L"], r["S"]
        X0 = Xi_c(mp.mpf(0))
        c = S_Xi - S
        raw, cor = [], []
        for z in pts:
            F = core.F_of(xi, L, z)
            G = Xi_c(z) / X0
            raw.append(abs(F - G) / abs(G))
            cor.append(abs(F * mp.exp(-c * z * z) - G) / abs(G))
        res[lam_s] = (raw, cor)
        print(f"lambda={lam_s}  c = S_Xi - S = {mp.nstr(c, 5)}")
        for z, a, b in zip(pts, raw, cor):
            print(f"   z = {mp.nstr(z, 4):>14s}   raw {mp.nstr(a, 3):>9s}   corrected {mp.nstr(b, 3):>9s}   gain x{mp.nstr(a / b, 3)}")
    ok = True
    for lam_s, (raw, cor) in res.items():
        ok &= all(a > 100 * b for a, b in zip(raw, cor))
    ok &= all(res["4.0"][0][i] < res["3.0"][0][i] and res["4.0"][1][i] < res["3.0"][1][i] for i in range(len(pts)))
    print("O1 corrected error >= 100x smaller than raw at every point; O2 both decrease from lambda 3 to 4:",
          "PASS" if ok else "FAIL")
    print("\nRESULT:", "GREEN" if ok else "RED")
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
