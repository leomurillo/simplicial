"""J7 / Addendum J: explicit cluster c_2 sign computation.

Following diez §2.1, the cluster bump for hypothetical off-line zero
   rho_0 = 1/2 + delta + i gamma_0
with FE-cluster Lambda = {rho_+, rho_-, bar rho_+, bar rho_-} is

   g_rho(x) := x^{rho - 1} eta_sigma(log x)  (Mellin bump at rho)
   g_0(x)  := sum_{v in Lambda} g_{rho_v}(x)

This probe:
  1. Checks whether g_0 in G (positivity class): is S_{g_0}(x) >= 0 on R_+?
  2. Computes the cluster c_2 contribution via the diez §2.6 formula
     for this specific g_0 and a specific smearing eta_0.
  3. Sign analysis: c_2 < 0 would close cubic positivity argument
     unconditionally if g_0 is in G.

We use:
   - Mellin bump width sigma = 0.5
   - Smearing eta_0 Gaussian with sigma_0 in {0.06, 0.12, 0.18}
   - hypothetical off-line at gamma_0 = 14.13473 with delta in {0.001, 0.01, 0.1}
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 30


def mellin_bump_widetilde_g(s_eval: complex, rho: complex, sigma: float) -> complex:
    """Mellin transform of g_rho(x) = x^{rho - 1} eta(log x) with eta = Gaussian.

    M[g_rho](s) = M[x^{rho-1} eta(log x)](s)
                = int x^{rho - 1} eta(log x) x^{s - 1} dx
    Let u = log x:
                = int e^{u(rho - 1)} eta(u) e^{u(s - 1)} e^u du
                = int e^{u(rho + s - 1)} eta(u) du
                = hat_eta(i(1 - rho - s))
    """
    arg = 1j * (1 - rho - s_eval)
    # hat_eta for unit Gaussian eta(u) = (sigma/sqrt(2pi)) e^{-sigma^2 u^2 / 2}:
    # hat_eta(y) = e^{-y^2 / (2 sigma^2)}
    # But here we use eta(u) = e^{-u^2/(2 sigma^2)} / (sigma sqrt(2pi)) so int eta = 1
    return mp.exp(-(arg**2) / (2 * sigma**2))


def widetilde_g_0(s_eval: complex, rho_0: complex, sigma: float) -> complex:
    """Cluster bump widetilde g_0 = sum over 4 cluster vertices."""
    rho_p = rho_0  # 1/2 + delta + i gamma_0
    rho_m = 1 - mp.conj(rho_p)  # 1/2 - delta + i gamma_0 by FE+conj
    bar_p = mp.conj(rho_p)  # 1/2 + delta - i gamma_0
    bar_m = mp.conj(rho_m)  # 1/2 - delta - i gamma_0

    total = mp.mpc(0)
    for rho in [rho_p, rho_m, bar_p, bar_m]:
        total += mellin_bump_widetilde_g(s_eval, rho, sigma)
    return total


def spectral_sum_S_g0(x: float, rho_0: complex, sigma: float, gammas_known: list) -> complex:
    """S_{g_0}(x) = sum over zeros rho of widetilde g_0(rho) e^{(rho - 1/2)x}.

    Computed over a finite set of known on-line zeros + the cluster vertices.
    """
    s = mp.mpc(0)
    # Cluster vertices
    rho_p = rho_0
    rho_m = 1 - mp.conj(rho_p)
    bar_p = mp.conj(rho_p)
    bar_m = mp.conj(rho_m)
    for rho in [rho_p, rho_m, bar_p, bar_m]:
        s += widetilde_g_0(rho, rho_0, sigma) * mp.exp((rho - mp.mpf("0.5")) * x)
    # On-line zeros (first 20)
    for gamma in gammas_known:
        # On-line zero is rho = 1/2 + i gamma and its conjugate 1/2 - i gamma
        rho_on_p = mp.mpc(mp.mpf("0.5"), gamma)
        rho_on_n = mp.mpc(mp.mpf("0.5"), -gamma)
        s += widetilde_g_0(rho_on_p, rho_0, sigma) * mp.exp((rho_on_p - mp.mpf("0.5")) * x)
        s += widetilde_g_0(rho_on_n, rho_0, sigma) * mp.exp((rho_on_n - mp.mpf("0.5")) * x)
    return s


def cluster_c2(rho_0: complex, sigma_g: float, sigma_eta: float) -> complex:
    """Compute the cluster c_2 coefficient for the specific (g_0, eta_0).

    From Addendum A8 / diez §2.6 / Step 0 cluster combinatorics:
       Re(C_Lambda^{delta^2}) = delta^2 * [24 Re(eta_0''(3 i gamma_0))
                                          + 72 Re(eta_0''(i gamma_0))]
    times (widetilde g_0(rho_v)|_{delta=0})^3 ~ 1 weight at each cluster vertex.

    For the specific g_0 (Mellin bumps), widetilde g_0 at delta=0 cluster
    vertex 1/2 + epsilon_gamma i gamma_0: pick up Gaussian bump peaks.
    """
    delta_re_rho = mp.re(rho_0) - mp.mpf("0.5")
    gamma_0 = mp.im(rho_0)

    # widetilde_g_0 at delta=0 cluster vertices: 1/2 + i epsilon gamma_0
    # By the Gaussian bump, this is approximately 1 (centered at cluster) plus
    # cross-terms from the other 3 bumps.
    rho_on_p = mp.mpc(mp.mpf("0.5"), gamma_0)
    g_at_on_p = widetilde_g_0(rho_on_p, rho_0, sigma_g)
    rho_on_n = mp.mpc(mp.mpf("0.5"), -gamma_0)
    g_at_on_n = widetilde_g_0(rho_on_n, rho_0, sigma_g)

    # eta_0''(i b gamma_0): second derivative of Gaussian smearing eta_0(x) at frequency b gamma_0.
    # eta_0(x) = exp(-sigma_eta^2 x^2 / 2) * positive_kernel.  Take hat_eta_0(y) = e^{-y^2 sigma_eta^2 / 2} for simplicity.
    # eta_0''(y) = d^2/dy^2 [e^{-y^2 sigma_eta^2 / 2}] = sigma_eta^2 (sigma_eta^2 y^2 - 1) e^{-y^2 sigma_eta^2 / 2}
    def eta_pp(y):
        return sigma_eta**2 * (sigma_eta**2 * y**2 - 1) * mp.exp(-y**2 * sigma_eta**2 / 2)

    eta_pp_3 = eta_pp(3j * gamma_0)
    eta_pp_1 = eta_pp(1j * gamma_0)

    # c_2 contribution: 24 eta_pp(3 i gamma_0) + 72 eta_pp(i gamma_0)
    # times the product of widetilde_g_0 at cluster vertices (approximately g_at_on^3 each)
    # The actual weight is more complicated; for leading order:
    g_factor = (g_at_on_p * g_at_on_p * g_at_on_p)  # 3-fold product approximation

    c2 = 24 * eta_pp_3 * g_factor + 72 * eta_pp_1 * g_factor

    return c2


def main():
    print("=" * 100)
    print("J7 cluster sign computation: c_2 for diez §2.1 Mellin-bump g_0 + Gaussian eta_0")
    print("=" * 100)
    print()

    known_gammas = [
        14.134725141734693,
        21.022039638771554,
        25.010857580145688,
        30.424876125859513,
        32.935061587739189,
        37.586178158825671,
        40.918719012147495,
        43.327073280914999,
        48.005150881167159,
        49.773832477672302,
    ]

    gamma_0 = mp.mpf("14.134725141734693")  # at first zeta zero
    sigma_g = mp.mpf("0.5")  # Mellin bump width

    print(f"gamma_0 = {float(gamma_0):.6f} (location of hypothetical off-line zero)")
    print(f"Mellin bump width sigma_g = {float(sigma_g)}")
    print()

    print("Part 1: Sign of widetilde g_0(rho_v) at cluster vertices")
    print("-" * 100)
    print(f"{'delta':>8}  {'rho_v':>30}  {'widetilde g_0(rho_v)':>40}")

    for delta in [mp.mpf("0.001"), mp.mpf("0.01"), mp.mpf("0.05"), mp.mpf("0.1")]:
        rho_0 = mp.mpc(mp.mpf("0.5") + delta, gamma_0)
        rho_p = rho_0
        rho_m = 1 - mp.conj(rho_p)
        bar_p = mp.conj(rho_p)
        bar_m = mp.conj(rho_m)
        for rho_v, name in [
            (rho_p, "rho_+"),
            (rho_m, "rho_-"),
            (bar_p, "bar_rho_+"),
            (bar_m, "bar_rho_-"),
        ]:
            g_val = widetilde_g_0(rho_v, rho_0, sigma_g)
            print(
                f"  d={float(delta):.3f}  "
                f"{name:>10}={complex(rho_v):>20}  "
                f"widetilde g_0={complex(g_val)}"
            )
        print()

    print()
    print("Part 2: Cluster c_2 vs sigma_eta")
    print("-" * 100)
    print(f"{'delta':>8}  {'sigma_eta':>10}  {'Re c_2':>20}  {'sign':>10}")

    for delta in [mp.mpf("0.001"), mp.mpf("0.01"), mp.mpf("0.05")]:
        rho_0 = mp.mpc(mp.mpf("0.5") + delta, gamma_0)
        for sigma_eta in [mp.mpf("0.06"), mp.mpf("0.12"), mp.mpf("0.18"), mp.mpf("0.30"), mp.mpf("0.60")]:
            c2 = cluster_c2(rho_0, sigma_g, sigma_eta)
            re_c2 = float(mp.re(c2))
            sign = "NEG" if re_c2 < 0 else "POS"
            print(
                f"  d={float(delta):.3f}  s_eta={float(sigma_eta):.2f}  "
                f"Re c_2 = {re_c2:>+18.6e}  [{sign}]"
            )
        print()

    print()
    print("Part 3: Is g_0 in G (positivity class)?  Test S_{g_0}(x) >= 0 on R_+")
    print("-" * 100)

    delta_test = mp.mpf("0.01")
    rho_0 = mp.mpc(mp.mpf("0.5") + delta_test, gamma_0)

    print(f"Testing at rho_0 = 1/2 + {float(delta_test)} + i {float(gamma_0)}:")
    print(f"{'x':>8}  {'Re S_{g_0}(x)':>20}  {'sign':>10}")

    bad_count = 0
    total = 0
    for x in np.linspace(0.5, 8, 30):
        x_mp = mp.mpf(float(x))
        s_val = spectral_sum_S_g0(x_mp, rho_0, sigma_g, known_gammas)
        re_s = float(mp.re(s_val))
        sign = "POS" if re_s >= 0 else "NEG"
        if re_s < 0:
            bad_count += 1
        total += 1
        if int(x * 10) % 5 == 0:  # sparse printing
            print(f"  x={x:.2f}  Re S_g0 = {re_s:>+18.6e}  [{sign}]")
    print(f"\n  Sign violations: {bad_count} / {total} grid points")
    print(f"  If 0: g_0 in G unconditionally on tested range.")
    print(f"  If > 0: g_0 not in G; refined construction needed.")


if __name__ == "__main__":
    main()
