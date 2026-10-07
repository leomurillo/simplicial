#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32.1  Audit 4  --  The boundary constant is a zeta ratio
==============================================================

Establishes the closed form of the conductor-weighted boundary share limit
(Audit 3, HORN B'):  beta_cond(inf) = prod_p (1 - 1/(p^2-p+1)).

----------------------------------------------------------------------------
CLAIM (Paper 32.1 Thm 11.1)
----------------------------------------------------------------------------
    beta_cond(inf) = prod_p (p^2-p)/(p^2-p+1)
                   = prod_p (1 - p^-2)/(1 + p^-3)        [per-prime identity]
                   = [1/zeta(2)] / [zeta(3)/zeta(6)]
                   = zeta(6) / (zeta(2) zeta(3))
                   = 2 pi^4 / (315 zeta(3))
                   ~ 0.514505...

----------------------------------------------------------------------------
WHY THE PER-PRIME IDENTITY HOLDS
----------------------------------------------------------------------------
p^3 + 1 = (p+1)(p^2 - p + 1), and p^3 - p = p(p-1)(p+1), so
    (1 - p^-2)/(1 + p^-3) = (p^2-1)/p^2 * p^3/(p^3+1)
                          = p(p^2-1)/(p^3+1)
                          = p(p-1)(p+1)/[(p+1)(p^2-p+1)]
                          = p(p-1)/(p^2-p+1) = (p^2-p)/(p^2-p+1).
Then prod(1-p^-2) = 1/zeta(2) and prod(1+p^-3) = zeta(3)/zeta(6) are
standard Euler products.

----------------------------------------------------------------------------
FIREWALL (Paper 32 sec 12)
----------------------------------------------------------------------------
beta_cond(inf) is a PURE NUMBER (a ratio of zeta values); no unit emitted.
The reading (order-2 / order-3 density; squarefree-density lead) is structural
only -- see the forced-match guard in Paper 32.1 sec 11.
"""

import sympy as sp
from sympy import primerange


def per_prime_identity():
    """Symbolically verify (p^2-p)/(p^2-p+1) == (1-p^-2)/(1+p^-3)."""
    p = sp.symbols('p', positive=True)
    lhs = (p**2 - p) / (p**2 - p + 1)
    rhs = (1 - 1/p**2) / (1 + 1/p**3)
    return sp.simplify(lhs - rhs) == 0


def closed_forms():
    """Return the three closed forms evaluated to high precision."""
    z2, z3, z6 = sp.zeta(2), sp.zeta(3), sp.zeta(6)
    beta_zeta = z6 / (z2 * z3)                      # zeta(6)/(zeta(2)zeta(3))
    beta_pi = 2 * sp.pi**4 / (315 * z3)             # using z2=pi^2/6, z6=pi^6/945
    sqfree = 1 / z2                                 # squarefree density 6/pi^2
    return (sp.N(beta_zeta, 25), sp.N(beta_pi, 25),
            sp.N(sqfree, 25), sp.N(z2, 25), sp.N(z3, 25), sp.N(z6, 25))


def truncated_product(P):
    """prod_{p<=P} (1 - 1/(p^2-p+1)) in double precision (convergence demo)."""
    val = 1.0
    for p in primerange(2, P + 1):
        val *= (1.0 - 1.0 / (p * p - p + 1))
    return val


def main():
    print("#" * 74)
    print("#  Paper 32.1  Audit 4 -- The boundary constant is a zeta ratio")
    print("#" * 74)

    # ---- (1) per-prime identity (the rigorous step) ----
    ok = per_prime_identity()
    print("\n(1) Per-prime identity  (p^2-p)/(p^2-p+1) == (1-p^-2)/(1+p^-3)")
    print(f"    sympy simplify(lhs - rhs) == 0 :  {ok}")

    # ---- (2) closed forms agree ----
    bz, bpi, sqf, z2, z3, z6 = closed_forms()
    print("\n(2) Closed forms (25-digit)")
    print(f"    zeta(2) = {z2}")
    print(f"    zeta(3) = {z3}")
    print(f"    zeta(6) = {z6}")
    print(f"    zeta(6)/(zeta(2)zeta(3)) = {bz}")
    print(f"    2 pi^4 / (315 zeta(3))   = {bpi}")
    print(f"    agree to 25 digits:        {sp.N(bz - bpi, 25) == 0 or abs(bz-bpi) < sp.Float('1e-23')}")
    print(f"    leading squarefree density 1/zeta(2) = 6/pi^2 = {sqf}")

    # ---- (3) numeric product converges (downward) to the closed form ----
    print("\n(3) Truncated product  prod_{p<=P}(1 - 1/(p^2-p+1))  vs closed form")
    print("-" * 74)
    target = float(bz)
    print(f"    {'P':>10} | {'product':>14} | {'product - target':>18}")
    print("-" * 74)
    for P in [10, 100, 1000, 10**4, 10**5, 10**6]:
        prod = truncated_product(P)
        print(f"    {P:>10} | {prod:>14.10f} | {prod - target:>18.2e}")
    print(f"    {'closed form':>10} | {target:>14.10f} | "
          f"{'(zeta(6)/(zeta(2)zeta(3)))':>18}")
    print("    (product approaches target from ABOVE; residual ~ prime tail "
          "sum 1/p^2)")

    # ---- VERDICT ----
    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    converged = abs(truncated_product(10**6) - target) < 1e-6
    print(f"  Per-prime identity verified symbolically:        {ok}")
    print(f"  beta_cond(inf) = zeta(6)/(zeta(2)zeta(3))")
    print(f"                 = 2 pi^4/(315 zeta(3)) = {target:.10f}")
    print(f"  Numeric product -> closed form (P=1e6):          {converged}")
    print(f"  Firewall: pure number (zeta ratio); no unit emitted.")
    print("\nAUDIT 4:", "ZETA-RATIO CLOSED FORM CONFIRMED"
          if (ok and converged) else "SEE ABOVE")


if __name__ == "__main__":
    main()
