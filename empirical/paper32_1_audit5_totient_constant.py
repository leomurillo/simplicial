#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32.1  Audit 5  --  The boundary constant "out there" = Landau totient
===========================================================================

Identifies the boundary constant zeta(6)/(zeta(2)zeta(3)) (Thm 11.1) with a
classical object: zeta(2)zeta(3)/zeta(6) is LANDAU'S TOTIENT CONSTANT -- the
asymptotic MEAN of n/phi(n):

    (1/x) sum_{n<=x} n/phi(n)  ->  A = zeta(2)zeta(3)/zeta(6)
                                     = prod_p (1 + 1/(p(p-1)))   (Landau 1900)

so the Bekenstein boundary constant is its reciprocal,
    beta_cond(inf) = zeta(6)/(zeta(2)zeta(3)) = 1 / <n/phi(n)>.

This is STRUCTURALLY apt, not a coincidence: the conductor-fusion boundary
M = (Z/N)^x is the UNIT GROUP, of size phi(N); a constant governing the units'
asymptotic weighted share is necessarily a totient-ratio constant.

Verifies the identity deterministically by sieving phi(n) up to 10^6.
Firewall (Paper 32 sec 12): pure number, no unit.
"""

import numpy as np
import sympy as sp


def totient_sieve(N):
    """phi(n) for n=0..N via the standard sieve."""
    phi = np.arange(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if phi[p] == p:                       # p is prime
            phi[p::p] -= phi[p::p] // p
    return phi


def main():
    print("#" * 74)
    print("#  Paper 32.1  Audit 5 -- boundary constant = 1/Landau-totient-const")
    print("#" * 74)

    A_exact = sp.N(sp.zeta(2) * sp.zeta(3) / sp.zeta(6), 20)
    beta_exact = sp.N(sp.zeta(6) / (sp.zeta(2) * sp.zeta(3)), 20)
    print(f"\n  A      = zeta(2)zeta(3)/zeta(6) = {A_exact}   (Landau totient const)")
    print(f"  1/A    = zeta(6)/(zeta(2)zeta(3)) = {beta_exact}   (boundary const, Thm 11.1)")

    N = 10**6
    print(f"\n  Sieving phi(n) up to N = {N} ...")
    phi = totient_sieve(N)
    n = np.arange(1, N + 1, dtype=np.float64)
    ratio = n / phi[1:]                        # n/phi(n)
    csum = np.cumsum(ratio)

    print("\n  Running mean (1/x) sum_{n<=x} n/phi(n)  ->  A")
    print("-" * 60)
    print(f"  {'x':>10} | {'mean n/phi(n)':>16} | {'mean - A':>14}")
    print("-" * 60)
    Af = float(A_exact)
    for x in [10**3, 10**4, 10**5, 10**6]:
        mean = csum[x - 1] / x
        print(f"  {x:>10} | {mean:>16.8f} | {mean - Af:>14.2e}")
    print(f"  {'A (closed)':>10} | {Af:>16.8f} | {'zeta(2)zeta(3)/zeta(6)':>14}")

    print("\n  Euler-product cross-check  A = prod_p (1 + 1/(p(p-1)))")
    prodA = 1.0
    for p in sp.primerange(2, 10**6):
        prodA *= (1 + 1.0 / (p * (p - 1)))
    print(f"    prod_{{p<=1e6}} (1+1/(p(p-1))) = {prodA:.10f}  vs A = {Af:.10f}")

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    mean_1e6 = csum[N - 1] / N
    ok = abs(mean_1e6 - Af) < 1e-4
    print(f"  mean n/phi(n) at x=1e6 = {mean_1e6:.6f}  ->  A = {Af:.6f}: "
          f"{'MATCH' if ok else 'NO'}")
    print(f"  => boundary constant zeta(6)/(zeta(2)zeta(3)) = 1/<n/phi(n)>")
    print(f"     = reciprocal of LANDAU'S TOTIENT CONSTANT.")
    print(f"  Structurally forced: boundary M = (Z/N)^x = units, |M| = phi(N).")
    print("\nAUDIT 5:", "LANDAU TOTIENT IDENTIFICATION CONFIRMED" if ok else "SEE ABOVE")


if __name__ == "__main__":
    main()
