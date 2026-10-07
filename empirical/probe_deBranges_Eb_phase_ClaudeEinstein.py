"""Phase function of the derivative-polarized de Branges associate
E_B(z) = Xi(z) + i Xi'(z).

On the real axis, the de Branges phase is

    phi(x) = -arg E_B(x) = arctan(-Xi'(x)/Xi(x)).

Three classical de Branges facts equivalent to RH-for-Xi:

  (1) phi is monotone increasing on R;
  (2) consecutive Xi-zeros satisfy phi(gamma_{n+1}) - phi(gamma_n) = pi;
  (3) phi'(x) ~ (1/2) log(x / (2 pi e)) as x -> infty (Riemann-von Mangoldt).

This probe checks all three numerically.
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


def deriv(f, z: mp.mpc, h: mp.mpf = None) -> mp.mpc:
    if h is None:
        h = mp.mpf("1e-6")
    return (f(z + h) - f(z - h)) / (2 * h)


def Xi_prime(z: mp.mpc, h: mp.mpf = None) -> mp.mpc:
    return deriv(Xi, z, h)


def phase(x: mp.mpf) -> mp.mpf:
    """Continuous-branch phase phi(x) of E_B(x) = Xi(x) + i Xi'(x).

    Returns arctan2(-Xi'(x), Xi(x)) (principal branch).
    """
    z = mp.mpc(x, 0)
    xi_val = mp.re(Xi(z))
    xi_prime_val = mp.re(Xi_prime(z))
    return mp.atan2(-xi_prime_val, xi_val)


def unwrap_phase(xs: list[mp.mpf]) -> list[mp.mpf]:
    """Unwrap the principal-branch phase so it's continuous."""
    phis = [phase(x) for x in xs]
    unwrapped = [phis[0]]
    for i in range(1, len(phis)):
        delta = phis[i] - phis[i - 1]
        # Adjust by multiples of pi (since arctan branch is mod pi for phi
        # of a real function whose ratio jumps at zeros).
        while delta > mp.pi / 2:
            delta -= mp.pi
        while delta < -mp.pi / 2:
            delta += mp.pi
        unwrapped.append(unwrapped[-1] + delta)
    return unwrapped


def phi_derivative(x: mp.mpf, h: mp.mpf = mp.mpf("1e-4")) -> mp.mpf:
    """phi'(x) by finite difference of unwrapped phase."""
    p_plus = phase(x + h)
    p_minus = phase(x - h)
    delta = p_plus - p_minus
    # Unwrap small jump
    while delta > mp.pi / 2:
        delta -= mp.pi
    while delta < -mp.pi / 2:
        delta += mp.pi
    return delta / (2 * h)


def main() -> None:
    gammas = [
        mp.mpf("14.134725141734693790457251983562"),
        mp.mpf("21.022039638771554992628479593897"),
        mp.mpf("25.010857580145688763213790992562"),
        mp.mpf("30.424876125859513210311897530585"),
        mp.mpf("32.935061587739189690662368964075"),
        mp.mpf("37.586178158825671257217763480705"),
        mp.mpf("40.918719012147495187398126914634"),
        mp.mpf("43.327073280914999519496122165407"),
        mp.mpf("48.005150881167159727942472749427"),
        mp.mpf("49.773832477672302181916784678563"),
    ]

    print("=" * 100)
    print("de Branges phase function phi(x) = -arg E_B(x) for E_B = Xi + i Xi'")
    print("=" * 100)

    # (1) Monotonicity: phi'(x) > 0 on a sampled grid
    print("\n(1) Monotonicity: sample phi'(x) on a grid")
    grid_xs = [mp.mpf(x) for x in [1, 3, 5, 8, 10, 13, 15, 18, 22, 27, 35, 50, 100, 200]]
    min_phi_prime = mp.inf
    for x in grid_xs:
        phi_prime = phi_derivative(x)
        rvm_density = mp.log(x / (2 * mp.pi)) / 2 if x > 2 * mp.pi else mp.mpf("nan")
        if phi_prime < min_phi_prime:
            min_phi_prime = phi_prime
        print(
            f"  x={float(x):6.1f}  phi'(x)={float(phi_prime):+.6e}  "
            f"RvM (1/2)log(x/2pi)={float(rvm_density):+.6e}"
        )
    print(f"  Minimum phi' sampled: {float(min_phi_prime):+.6e}")
    if min_phi_prime > 0:
        print("  All sampled phi' positive — monotonicity holds on grid.")
    else:
        print("  WARNING: phi' negative somewhere — would refute monotonicity.")

    # (2) Zero indexing: phi(gamma_{n+1}) - phi(gamma_n) = pi
    print("\n(2) Zero indexing: phi(gamma_{n+1}) - phi(gamma_n) compared to pi")
    pi_val = mp.pi
    # Sample phi just above and just below each zero (small offset to avoid arctan branch)
    # Better: use unwrapped phase across a fine grid spanning the zeros.

    # Build a fine grid spanning the first 10 zeros
    fine_grid = []
    x_start = mp.mpf("13.5")
    x_end = gammas[-1] + mp.mpf("1")
    n_steps = 200
    step = (x_end - x_start) / n_steps
    for i in range(n_steps + 1):
        fine_grid.append(x_start + i * step)

    unwrapped = unwrap_phase(fine_grid)

    # Sample phi at the zero ordinates by interpolation
    def phi_at(target):
        # Find bracketing grid points
        for i in range(len(fine_grid) - 1):
            if fine_grid[i] <= target <= fine_grid[i + 1]:
                t = (target - fine_grid[i]) / (fine_grid[i + 1] - fine_grid[i])
                return unwrapped[i] + t * (unwrapped[i + 1] - unwrapped[i])
        return None

    phi_at_zeros = [phi_at(g) for g in gammas]
    for i in range(len(gammas) - 1):
        delta_phi = phi_at_zeros[i + 1] - phi_at_zeros[i]
        delta_div_pi = delta_phi / pi_val
        print(
            f"  gamma_{i+1}={float(gammas[i]):.4f}  gamma_{i+2}={float(gammas[i+1]):.4f}  "
            f"phi diff/pi={float(delta_div_pi):.4f}"
        )

    # (3) Asymptotic phi'(x) ~ (1/2) log(x / (2 pi))
    print("\n(3) Asymptotic check: phi'(x) vs (1/2) log(x / (2 pi))")
    for x in [mp.mpf(50), mp.mpf(100), mp.mpf(200), mp.mpf(500), mp.mpf(1000)]:
        phi_prime = phi_derivative(x, h=mp.mpf("1e-3"))
        rvm = mp.log(x / (2 * mp.pi)) / 2
        ratio = phi_prime / rvm
        print(
            f"  x={float(x):6.0f}  phi'(x)={float(phi_prime):+.6e}  "
            f"(1/2)log(x/2pi)={float(rvm):+.6e}  ratio={float(ratio):.6f}"
        )

    print("\nConclusion:")
    print("  If all three checks pass, the de Branges phase function for E_B has")
    print("  exactly the structure required for RH-for-Xi.  This is consistent with")
    print("  RH being verified numerically to enormous height; it is not a proof.")


if __name__ == "__main__":
    main()
