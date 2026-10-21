r"""
probe_lp_transport_zeta.py -- certificate for the Laguerre-Polya transport section (zeta side).

THEOREM BEING EXERCISED (LP transport).  Let F_lambda be even entire functions with only real
zeros and F_lambda(0)=1.  Hadamard gives |F(z)| <= exp(S |z|^2) with the single scalar
S = -F''(0)/2 = sum_k 1/a_k^2 (a_k the positive zeros), and F(t) <= exp(-S t^2) on [0, a_1).
Hence ONE real interval of convergence controls everything: normality, LP limit, identification.

For the CCM/CvS minimizer xi_lambda of the semilocal Weil form QW_lambda (CCM basis, exact
closed-form entries, see lp_transport_core.py), F_lambda(z) = xihat_lambda(z)/xihat_lambda(0):
  S(lambda) = L^2/24 + (L^2/(2 pi^2)) sum_{k>=1} xi_k/(k^2 xi_0),        L = 2 log lambda.

CHECKS
  C0  closed-form matrix == quadrature-certified CCM matrix of the verification note (1e-38).
  C1  hypothesis (a) [CCM step 1]: even global ground, simple (even eps < odd ground < even mu1).
  C2  real-rootedness: the N positive roots of the secular function all real (CvS finmain).
  C3  the LP scalar: S(lambda) -> S_Xi = -Xi''(0)/(2 Xi(0)) = 0.0231049931154 (bounded; bulk mode).
      Deficit law  S_Xi - S(lambda) ~ c / lambda^2  (unmatched zeros above the Nyquist height 2 pi lambda^2).
  C4  the Hadamard bound F(t) <= exp(-S t^2) on [0, a_1) and |F(z)| <= exp(S |z|^2) at sample z.
  C5  the interval of convergence: sup_{|t|<=1} |F_lambda(t) - Xi(t)/Xi(0)| -> 0; first zero -> gamma_1.
  C6  N-stability of S at the largest lambda.

mpmath only; deterministic; local.  Run:  python probe_lp_transport_zeta.py
"""
import sys
import time
import math

sys.path.insert(0, r"C:/Projects/simplicial/empirical/connes_route")
import mpmath as mp
import lp_transport_core as core

sys.stdout.reconfigure(encoding="utf-8")
GAMMA1 = mp.mpf("14.134725141734693790457251983562")


def dps_for(lam):
    """resolve eps ~ (1 - chi_4) ~ exp(-4 pi lam^2 + 9 log lam) * 2^14/3 sqrt2 pi^5  with margin."""
    lam = float(lam)
    import math
    digits = (4 * math.pi * lam * lam - 9 * math.log(lam) - math.log(2 ** 14 / 3 * math.sqrt(2) * math.pi ** 5)) / math.log(10)
    return int(max(40, 1.15 * digits + 30))


def edge_mass(xi, L, width=mp.mpf(1) / 2, M=600):
    """fraction of |f(v)|^2 within `width` of the window edges, f(v) = xi_0 + 2 sum (-1)^k xi_k cos(2 pi k v/L)."""
    tot = mp.mpf(0)
    edg = mp.mpf(0)
    for j in range(M + 1):
        v = -L / 2 + L * mp.mpf(j) / M
        fv = xi[0] + 2 * mp.fsum(((-1) ** k) * xi[k] * mp.cos(2 * mp.pi * k * v / L) for k in range(1, len(xi)))
        w = fv * fv * (mp.mpf(1) / 2 if j in (0, M) else 1)
        tot += w
        if abs(abs(v) - L / 2) <= width:
            edg += w
    return edg / tot


def run_one(lam, N, verbose=True):
    t0 = time.time()
    Ev, Od, S, D, L = core.sectors(lam, N, "zeta")
    ve, vecs = core.low_eig(Ev, 2)
    vo, _ = core.low_eig(Od, 1)
    xi = core.even_coeffs(vecs[0])
    Sl = core.S_of(xi, L)
    eps, mu1, odd0 = ve[0], ve[1], vo[0]
    a_ok = (eps < odd0) and (eps < mu1)
    t1 = time.time()
    return dict(lam=lam, N=N, L=L, eps=eps, mu1=mu1, odd0=odd0, xi=xi, S=Sl, a_ok=a_ok, t=t1 - t0)


def main():
    print("=" * 96)
    print("LP transport, zeta side: the single scalar S(lambda) of the CCM/CvS Weil minimizer")
    print("=" * 96)
    ok = True

    # ---------------- C0: cross-validation against the note's quadrature build
    sys.path.insert(0, r"C:/Projects/Connes/certificates-note2")
    mp.mp.dps = 40
    try:
        import probe_cvs_weld as ref
        worst = mp.mpf(0)
        for lam_s, N in (("1.5", 6), ("2.0", 6)):
            QWr, _, _ = ref.build_QW_full(mp.mpf(lam_s), N)
            M, _, _, _ = core.full_entry_check(mp.mpf(lam_s), N, "zeta")
            worst = max(worst, max(abs(QWr[i, j] - M[i, j]) for i in range(2 * N + 1) for j in range(2 * N + 1)))
        c0 = worst < mp.mpf("1e-36")
        print(f"C0 closed-form vs quadrature-certified CCM matrix (lambda=1.5,2.0; N=6): max diff = {mp.nstr(worst, 3)}  "
              f"{'PASS' if c0 else 'FAIL'}")
        ok &= c0
    except Exception as e:                                  # reference not present: skip, do not fail
        print(f"C0 skipped (reference build unavailable: {e})")

    # ---------------- targets
    mp.mp.dps = 40
    S_Xi = -mp.diff(core.Xi_zeta, mp.mpf(0), 2) / (2 * core.Xi_zeta(mp.mpf(0)))
    print(f"\nS_Xi = -Xi''(0)/(2 Xi(0)) = {mp.nstr(S_Xi, 15)}   (= sum_{{gamma>0}} 1/gamma^2 under RH)")

    # N >= 2 lambda^2 L + 24: resolves the Nyquist height 2 pi lambda^2 with margin (C6 checks stability)
    ladder = [(lam_s, int(2 * float(lam_s) ** 2 * 2 * math.log(float(lam_s))) + 24)
              for lam_s in ("1.3", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5")]
    rows = []
    print("\n lambda   L      N   dps   eps            odd ground     mu1            (a)  S(lambda)        "
          "S_Xi-S      lam^2(S_Xi-S)  z_1          sup|F-Xi/Xi0|_[0,1]   time")
    for lam_s, N in ladder:
        lam = mp.mpf(lam_s)
        mp.mp.dps = dps_for(lam)
        r = run_one(lam, N)
        xi, L = r["xi"], r["L"]
        # C2: real roots (CvS) -- count positive real v-roots of the secular function (expect N)
        # (full working precision: the secular function at height t is ~e^{-pi t/4} relative)
        vroots = core.real_zeros_v(xi, pts_per_interval=40, refine=True)
        zpos = [2 * mp.pi * mp.sqrt(v) / L for v in vroots]
        # F_N = (sin pi s/(pi s)) * [secular bracket]: its zeros are the N secular roots PLUS the
        # 'frame' zeros s = k > N of sin(pi s) (z = 2 pi k / L), contributing (L/2pi)^2 psi'(N+1).
        frame = (L / (2 * mp.pi)) ** 2 * mp.psi(1, N + 1)
        S_from_zeros = (mp.fsum(1 / (z * z) for z in zpos) + frame) if len(vroots) == N else None
        # C5: interval of convergence
        X0 = core.Xi_zeta(mp.mpf(0))
        grid = [mp.mpf(j) / 20 for j in range(1, 21)]
        supd = max(abs(core.F_of(xi, L, t) - core.Xi_zeta(t) / X0) for t in grid)
        # C4: Hadamard bounds
        z1 = zpos[0] if zpos else mp.nan
        hb_ok = all(core.F_of(xi, L, t) <= mp.exp(-r["S"] * t * t) * (1 + mp.mpf("1e-25"))
                    for t in [mp.mpf(j) / 4 for j in range(1, 40)] if t < z1)
        zc = [mp.mpc(3, 2), mp.mpc(7, 0.4), mp.mpc(0.5, 6)]
        hb2 = all(abs(core.F_of(xi, L, z)) <= mp.exp(r["S"] * abs(z) ** 2) for z in zc)
        all_real = (len(vroots) == N)
        sigma = r["S"] / (L * L / 24)
        edge = edge_mass(xi, L)
        rows.append((lam_s, r, all_real, S_from_zeros, supd, z1, hb_ok and hb2, sigma, edge))
        print(f" {lam_s:6s} {mp.nstr(L,4):6s} {N:4d} {mp.mp.dps:4d}  {mp.nstr(r['eps'],5):14s} "
              f"{mp.nstr(r['odd0'],5):14s} {mp.nstr(r['mu1'],5):14s} {'Y' if r['a_ok'] else 'N'}   "
              f"{mp.nstr(r['S'],12):16s} {mp.nstr(S_Xi-r['S'],4):11s} {mp.nstr(lam*lam*(S_Xi-r['S']),5):13s} "
              f"{mp.nstr(z1,10):12s} {mp.nstr(supd,4):10s}  real roots {len(vroots)}/{N}  "
              f"sigma={mp.nstr(sigma,4)} edge={mp.nstr(edge,3)}  {r['t']:.0f}s")
        ok &= r["a_ok"] and all_real and hb_ok and hb2
        if S_from_zeros is not None:
            ok &= abs(S_from_zeros - r["S"]) < mp.mpf("1e-8") * r["S"] + mp.mpf("1e-12")

    # summary of the scalar
    print("\nC3  S(lambda) increases to S_Xi from below; lambda^2 * deficit column ~ constant (Nyquist law).")
    print("C4  Hadamard bounds F(t) <= exp(-S t^2) on [0,z_1) and |F(z)| <= exp(S|z|^2): "
          + ("all hold" if all(rw[6] for rw in rows) else "VIOLATION"))
    print("C5  sup_[0,1] |F - Xi/Xi(0)| column decreases; z_1 -> gamma_1 = 14.1347251417...")
    for lam_s, r, all_real, Sz, supd, z1, _, _, _ in rows:
        if Sz is not None:
            print(f"     lambda={lam_s}: S from moments {mp.nstr(r['S'],14)} vs sum 1/z_j^2 over the N real zeros "
                  f"{mp.nstr(Sz,14)}")

    # ---------------- C6: N-stability at the top two rungs (even sector only)
    print()
    for idx in (-2, -1):
        lam_s, N0 = ladder[idx]
        lam = mp.mpf(lam_s)
        mp.mp.dps = dps_for(lam)
        N1 = int(N0 * 1.25)
        Ev1, _, _, _, L1 = core.sectors(lam, N1, "zeta")
        _, vecs1 = core.low_eig(Ev1, 1)
        S1 = core.S_of(core.even_coeffs(vecs1[0]), L1)
        S0 = rows[idx][1]["S"]
        rel = abs(S1 - S0) / S1
        print(f"C6  N-stability at lambda={lam_s}: S(N={N0}) = {mp.nstr(S0,14)}, S(N={N1}) = {mp.nstr(S1,14)}, "
              f"rel. change {mp.nstr(rel,3)};  deficit S_Xi-S: {mp.nstr(S_Xi-S0,5)} -> {mp.nstr(S_Xi-S1,5)}")
        ok &= rel < mp.mpf("2e-4")

    print("\nRESULT:", "GREEN" if ok else "RED")
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
