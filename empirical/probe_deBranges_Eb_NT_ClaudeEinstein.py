"""Test the integrated de Branges phase / N(T) zero-counting agreement.

If E_B = Xi + i Xi' has the de Branges structure (equiv. to RH-for-Xi), then

    N(T) := #{Xi-zeros in (0, T]} = phi(T)/pi + (1/2) + O(1/log T),

where phi(T) = -arg E_B(T) on the real axis.  Equivalently,

    phi(T)/pi ~ (T / 2 pi) log(T / 2 pi e) + 7/8 + O(1/T).

This probe computes phi(T)/pi at several T values and compares to Riemann-von
Mangoldt N(T).  Cleaner than pointwise phi'(x) because the integrated version
averages over zero-density fluctuations.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 50


def xi(s: mp.mpc) -> mp.mpc:
    if abs(s) < mp.mpf("1e-30") or abs(s - 1) < mp.mpf("1e-30"):
        return mp.mpf("0.5")
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z: mp.mpc) -> mp.mpc:
    return xi(mp.mpf("0.5") + 1j * z)


def Xi_prime(z: mp.mpc) -> mp.mpc:
    h = mp.mpf("1e-6")
    return (Xi(z + h) - Xi(z - h)) / (2 * h)


def phase(x: mp.mpf) -> mp.mpf:
    z = mp.mpc(x, 0)
    xi_val = mp.re(Xi(z))
    xi_prime_val = mp.re(Xi_prime(z))
    return mp.atan2(-xi_prime_val, xi_val)


def unwrap_phase_at_T(T: mp.mpf, n_steps: int = 2000) -> mp.mpf:
    """Compute the unwrapped phase phi(T) - phi(0) by tracking through n_steps."""
    step = T / n_steps
    p0 = phase(mp.mpf("0.001"))  # avoid x=0 exactly
    p_prev = p0
    total = mp.mpf("0")
    for i in range(1, n_steps + 1):
        x = i * step
        p_cur = phase(x)
        delta = p_cur - p_prev
        # Unwrap: phase of E_B = Xi + i Xi' jumps by ~pi at each Xi-zero (since
        # E_B(gamma) = i Xi'(gamma) ne 0, but phi = arctan(-Xi'/Xi) jumps as Xi
        # crosses 0).
        while delta > mp.pi / 2:
            delta -= mp.pi
        while delta < -mp.pi / 2:
            delta += mp.pi
        total += delta
        p_prev = p_cur
    return total


def riemann_siegel_theta(t: mp.mpf) -> mp.mpf:
    """Riemann-Siegel theta(t) = arg Gamma(1/4 + i t/2) - (t/2) log pi."""
    gamma_arg = mp.arg(mp.gamma(mp.mpc(mp.mpf("0.25"), t / 2)))
    return gamma_arg - (t / 2) * mp.log(mp.pi)


def N_RvM(T: mp.mpf) -> mp.mpf:
    """Riemann-von Mangoldt: N(T) = theta(T)/pi + 1 + S(T), with S(T) = O(log T).
    Ignore S(T) here for asymptotic comparison."""
    return riemann_siegel_theta(T) / mp.pi + 1


def main() -> None:
    print("=" * 100)
    print("Integrated de Branges phase phi(T) vs Riemann-von Mangoldt N(T)")
    print("=" * 100)
    print()
    print("Expected: phi(T)/pi - (constant) = N(T) - (constant)")
    print("Both should follow (T/2 pi) log(T/2 pi e) asymptotically.")
    print()

    # First confirm known zero counts at a few heights
    # Number of zeros below T=14, 25, 50, 100, 200, 500, 1000:
    # Known: 0, 2, 10, 29, 79, 269, 649 (approx)
    Ts = [
        (mp.mpf(20), 0),
        (mp.mpf(40), 6),
        (mp.mpf(60), 15),
        (mp.mpf(100), 29),
        (mp.mpf(200), 79),
        (mp.mpf(500), 269),
    ]

    print(f"{'T':>8}  {'phi(T)/pi':>15}  {'theta(T)/pi':>15}  {'N_RvM(T)':>15}  {'known N(T)':>10}")
    for T, known in Ts:
        phi_T = unwrap_phase_at_T(T, n_steps=int(200 * float(T) / 20))
        phi_over_pi = phi_T / mp.pi
        theta_T = riemann_siegel_theta(T)
        N_rvm = N_RvM(T)
        print(
            f"  {float(T):>6.0f}  "
            f"{float(phi_over_pi):>15.6f}  "
            f"{float(theta_T / mp.pi):>15.6f}  "
            f"{float(N_rvm):>15.6f}  "
            f"{known:>10d}"
        )

    print()
    print("Differences (de Branges phase increment vs Riemann-Siegel theta):")
    print("If the de Branges phase tracks zero density, the rate should match")
    print("Riemann-Siegel theta to leading order (RvM density (T/2pi)log(T/2pi e)).")
    print()
    print("Note: numerical unwrapping may introduce phase jumps near zeros;")
    print("for an unconditional check use the analytical Stieltjes formula instead.")


if __name__ == "__main__":
    main()
