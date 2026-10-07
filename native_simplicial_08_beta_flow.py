"""
Native Simplicial Investigation, Script 08:
Compute the beta-flow (escort trajectories) for the primorial ledger at N=6.

The escort family is P_beta(s) = e^{beta y_s} / sum_t e^{beta y_t}.
At beta = 0 it's the uniform; as beta -> +infty it concentrates on argmax y_s;
as beta -> -infty it concentrates on argmin y_s.

For the limit ledger y = (-a, b, -a, -a, -a, b) with a = 1/sqrt 2, b = sqrt 2,
  argmax y = {1, 5} (tied)
  argmin y = {0, 2, 3, 4} (tied)
so tropical limits are uniform over those subsets, by symmetry.

For the actual finite-cutoff ledger, y[1] and y[5] are slightly different,
so the tropical limits are sharply peaked on a single index (the bigger of 1 vs 5).
"""

import mpmath as mp
from native_simplicial_01_ledger import primorial_ledger, center

mp.mp.dps = 30


def escort(beta, y, N=6):
    """P_beta(s) = e^{beta y_s} / sum."""
    beta = mp.mpf(beta)
    weights = [mp.exp(beta * y[s]) for s in range(N)]
    Z = sum(weights)
    return [w / Z for w in weights]


def K(beta, y, N=6):
    """Cumulant generating function K_y(beta) = log Z_y(beta) = log (1/N sum e^{beta y_s})."""
    beta = mp.mpf(beta)
    Z = sum(mp.exp(beta * y[s]) for s in range(N)) / N
    return mp.log(Z)


def main():
    print("=" * 80)
    print("Beta-flow for the primorial ledger at N=6")
    print("=" * 80)

    # Test (a) limit ledger
    sqrt2 = mp.sqrt(2)
    y_lim = [-1/sqrt2, sqrt2, -1/sqrt2, -1/sqrt2, -1/sqrt2, sqrt2]

    # Test (b) actual cutoff = 10000 prime_power ledger
    y_raw = primorial_ledger(10000, variant="prime_power")
    y_finite = center(y_raw)
    sigma_y = mp.sqrt(sum(yi**2 for yi in y_finite) / 6)
    y_resc = [yi / sigma_y for yi in y_finite]  # rescaled to unit second moment

    print("\nLimit ledger y_lim:")
    print("  y_lim = (-1/sqrt 2, sqrt 2, -1/sqrt 2, -1/sqrt 2, -1/sqrt 2, sqrt 2)")
    print(f"  argmax: indices 1 and 5 (tied)")
    print(f"  argmin: indices 0, 2, 3, 4 (tied)")
    print(f"  values: a = 1/sqrt 2 = {mp.nstr(1/sqrt2, 8)},  b = sqrt 2 = {mp.nstr(sqrt2, 8)}")

    print("\nBeta-flow trajectory for y_lim (rescaled, unit variance):")
    print(f"{'beta':>8} {'K(beta)':>12}  " + " ".join(f"P[{s}]" for s in range(6)) + "  -- escort distribution")
    for beta in [-5, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 5]:
        P = escort(beta, y_lim)
        Kv = K(beta, y_lim)
        print(f"{beta:>8.2f} {mp.nstr(Kv, 8):>12}  " + " ".join(f"{mp.nstr(p, 4):>6}" for p in P))

    # tropical limit check
    print("\nTropical limits (Maslov dequantization):")
    for beta in [-30, -10, 10, 30]:
        P = escort(beta, y_lim)
        Kv = K(beta, y_lim)
        # F(beta) = K(beta)/beta -> max y_s as beta -> +infty
        Fv = Kv / beta
        print(f"  beta={beta:+4d}: K/beta = {mp.nstr(Fv, 8):>10}  P = " + " ".join(f"{mp.nstr(p, 3):>5}" for p in P))
    print(f"  Expected max y_s = sqrt 2 = {mp.nstr(sqrt2, 8)}")
    print(f"  Expected min y_s = -1/sqrt 2 = {mp.nstr(-1/sqrt2, 8)}")

    print("\nBeta-flow trajectory for FINITE cutoff = 10000 (rescaled):")
    print(f"  Rescaled tilde_y =", [mp.nstr(yi, 8) for yi in y_resc])
    print(f"{'beta':>8} {'K(beta)':>12}  " + " ".join(f"P[{s}]" for s in range(6)))
    for beta in [-5, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 5]:
        P = escort(beta, y_resc)
        Kv = K(beta, y_resc)
        print(f"{beta:>8.2f} {mp.nstr(Kv, 8):>12}  " + " ".join(f"{mp.nstr(p, 4):>6}" for p in P))

    print("\nCumulants of y_lim (Taylor coefs of K at beta = 0):")
    # K'(0) = mean y = 0; K''(0) = var(y); K'''(0) = kappa_3 etc.
    # We compute them by repeated differentiation.
    for n in range(1, 7):
        try:
            kn = mp.diff(lambda b: K(b, y_lim), mp.mpf(0), n)
            print(f"  kappa_{n} = {mp.nstr(kn, 10)}")
        except Exception as e:
            print(f"  kappa_{n}: error {e}")


if __name__ == "__main__":
    main()
