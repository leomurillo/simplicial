"""Verify: cluster c_2 for the diez §1 Beurling-sampled g.

The diez §1 g has widetilde g(1/2 + it) = phi(t) (Fejer kernel of bandwidth Omega).
At off-line cluster vertex rho_v = 1/2 + epsilon_delta delta + i epsilon_gamma gamma_0:
    widetilde g(rho_v) = phi(gamma_0 epsilon_gamma - i delta epsilon_delta)
                      = phi(gamma_0 - i delta epsilon_delta epsilon_gamma) approx (phi even in real argument)

For Fejer phi(x) = (sin(Omega x/2)/(Omega x/2))^2:
   phi(gamma_0 - i*eps) ~ phi(gamma_0) + O(eps^2) at small eps

The cluster c_2 should be approximately:
   c_2(g_[A1']; rho_0; sigma_eta) approx phi(gamma_0)^3 * c_2^{Mellin}(rho_0; sigma_eta)/8

where the /8 = 2^3 is because Mellin-bump g_0 has widetilde g_0 ~ 2 at cluster vertices.

If c_2(g_[A1']) < 0: we have a g in G with cluster contradiction at any off-line.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 30


def phi_fejer(x, Omega):
    """Fejer kernel of bandwidth Omega: phi(x) = (sin(Omega x/2)/(Omega x/2))^2."""
    arg = Omega * x / 2
    if abs(arg) < 1e-30:
        return mp.mpc(1)
    return (mp.sin(arg) / arg) ** 2


def widetilde_g_diez1(s, Omega):
    """Approximate diez §1 widetilde g(s).

    On critical line s = 1/2 + it: widetilde g = phi(t).
    Off critical line s = 1/2 + delta + i gamma: widetilde g ~ phi(gamma - i delta).
    """
    t_complex = mp.im(s) - 1j * (mp.re(s) - mp.mpf("0.5"))
    return phi_fejer(t_complex, Omega)


def cluster_c2_diez1(rho_0, Omega, sigma_eta):
    """Cluster c_2 coefficient for diez §1 Beurling-sampled g at hypothetical off-line rho_0."""
    gamma_0 = mp.im(rho_0)

    # widetilde g at delta=0 cluster vertices
    rho_on_p = mp.mpc(mp.mpf("0.5"), gamma_0)
    rho_on_n = mp.mpc(mp.mpf("0.5"), -gamma_0)
    g_at_p = widetilde_g_diez1(rho_on_p, Omega)
    g_at_n = widetilde_g_diez1(rho_on_n, Omega)
    g_factor = g_at_p * g_at_p * g_at_p

    # Second derivative of smearing widetilde eta_0 at i b gamma_0
    def eta_pp(y):
        return sigma_eta**2 * (sigma_eta**2 * y**2 - 1) * mp.exp(-y**2 * sigma_eta**2 / 2)

    eta_pp_3 = eta_pp(3j * gamma_0)
    eta_pp_1 = eta_pp(1j * gamma_0)

    c2 = 24 * eta_pp_3 * g_factor + 72 * eta_pp_1 * g_factor
    return c2, g_at_p


def spectral_sum_S_diez1(x, Omega, gammas):
    """S_g(x) = sum over on-line zeros of widetilde g(1/2 + i gamma) * e^{i gamma x}.

    For diez §1 Beurling-sampled g with widetilde g(1/2 + i gamma) = phi(gamma):
    S_g(x) = sum_gamma phi(gamma) e^{i gamma x}.
    """
    s = mp.mpc(0)
    for gamma in gammas:
        ph = phi_fejer(mp.mpf(gamma), Omega)
        s += ph * mp.exp(1j * gamma * x)
        # Also -gamma (conjugate zero)
        ph_n = phi_fejer(-mp.mpf(gamma), Omega)
        s += ph_n * mp.exp(-1j * gamma * x)
    return s


def main():
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
        52.970321477714461,
        56.446247697063394,
        59.347044003392213,
        60.831778524609810,
        65.112544048081607,
        67.079810529494173,
        69.546401711173978,
        72.067157674481907,
        75.704690699083933,
        77.144840068874805,
    ]

    print("=" * 100)
    print("diez §1 Beurling-sampled g: cluster c_2 sign verification")
    print("=" * 100)
    print()

    gamma_0_test = mp.mpf("14.134725141734693")  # at first zeta zero ordinate

    # Test for hypothetical off-line zero at gamma_0
    print("Part 1: Cluster c_2 for diez §1 g, hypothetical off-line at gamma_0 = first zeta zero ordinate")
    print("(Mostly the §1 g and the cluster are sensitive only to the imaginary part gamma_0)")
    print()

    Omega = mp.mpf("0.5")
    print(f"Fejer bandwidth Omega = {float(Omega)}")
    print(f"phi(gamma_0={float(gamma_0_test)}) = {float(phi_fejer(gamma_0_test, Omega)):.6e}")
    print()

    print(f"{'delta':>8}  {'sigma_eta':>10}  {'phi(gamma_0)':>12}  {'c_2 (real part)':>20}  {'sign':>6}")

    for delta in [mp.mpf("0.001"), mp.mpf("0.01"), mp.mpf("0.05")]:
        rho_0 = mp.mpc(mp.mpf("0.5") + delta, gamma_0_test)
        for sigma_eta in [mp.mpf("0.06"), mp.mpf("0.12"), mp.mpf("0.18"), mp.mpf("0.30"), mp.mpf("0.60")]:
            c2, g_val = cluster_c2_diez1(rho_0, Omega, sigma_eta)
            re_c2 = float(mp.re(c2))
            sign = "NEG" if re_c2 < 0 else "POS"
            print(
                f"  d={float(delta):.3f}  s_eta={float(sigma_eta):.2f}  "
                f"phi={float(mp.re(g_val)):>10.4f}  "
                f"Re c_2 = {re_c2:>+18.4e}  [{sign}]"
            )
        print()

    # Part 2: Verify diez §1 g satisfies S_g >= 0 on R+
    print()
    print("Part 2: Verify S_g(x) ~= phi(x) >= 0 for diez §1 g (= sum over on-line zeros)")
    print()
    print("Uses ONLY on-line zeros from gammas list — this is the diez §1 S^(1) construction.")
    print()

    bad_count = 0
    total = 0
    for x_val in np.linspace(0.5, 10, 25):
        x_mp = mp.mpf(float(x_val))
        s_val = spectral_sum_S_diez1(x_mp, Omega, known_gammas)
        re_s = float(mp.re(s_val))
        sign = "POS" if re_s >= 0 else "NEG"
        if re_s < 0:
            bad_count += 1
        total += 1
        if int(x_val * 5) % 3 == 0:
            print(f"  x={x_val:.2f}  Re S_g = {re_s:>+16.4e}  [{sign}]")

    print(f"\n  Sign violations: {bad_count} / {total} grid points")
    if bad_count == 0:
        print("  g is in G (positivity class) on tested range, on-line truncation.")
    else:
        print(f"  WARNING: diez §1 g (with this truncation) has {bad_count} sign violations.")

    # Part 3: Combined check
    print()
    print("Part 3: Strategic assessment")
    print("If Part 1 shows c_2 < 0 AND Part 2 shows g in G:")
    print("  Then diez §1 g + diez §2 cluster argument gives unconditional cluster contradiction")
    print("  at any hypothetical off-line zero, modulo the prime-side identity.")
    print()
    print("The prime-side identity C_zeta(g; eta) = integral of 2 eta * S_g^3 dx requires RH.")
    print("To prove cubic positivity unconditionally: need to derive non-negativity of the")
    print("prime-side cube from non-RH input (= [A3'] primorial BV bound).")


if __name__ == "__main__":
    main()
