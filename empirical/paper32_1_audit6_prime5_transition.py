#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32.1  Audit 6  --  The 5-joining transition (Z/6 -> Z/30)
===============================================================

"If classical physics is the 2-and-3 play, what happens when 5 joins?"
We study the 6 -> 30 step AS A TRANSITION (the logit / critical-point lens),
honestly distinguishing the ATOMIC structural step from the smooth logit that
appears only under a weighting temperature.

----------------------------------------------------------------------------
PARTS
----------------------------------------------------------------------------
A. The discrete step (deterministic anchor): packet lattice, boundary growth,
   cross-coupling explosion, parity-inertness. A quantum -- no interior
   critical point in the jump itself.
B. The weighting-temperature logit: the boundary (units) share as a function
   of the conductor-weighting exponent beta. A genuine sigmoid 0 -> 1 with a
   critical point beta* (boundary = bulk). The "sweet spot."
C. The horizon handoff: grade prime 5 by t in [0,1]; find t* where the NEW
   boundary (conductor 30) overtakes the OLD (conductor 6). + packet richness.
D. Diminishing returns: the Mertens shaping weight -log(1-1/p) per prime.

FIREWALL (Paper 32 sec 12): only pure numbers / ratios / exponents. No unit.
"""

import numpy as np
from math import gcd, log
from sympy import totient, divisors


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def packets(N):
    """conductor c -> (dim phi(c), primes dividing c)."""
    out = {}
    for c in divisors(N):
        if c == 1:
            continue
        dim = sum(1 for k in range(1, N) if N // gcd(k, N) == c)
        primes = tuple(p for p in (2, 3, 5, 7, 11) if c % p == 0)
        out[c] = (dim, primes)
    return out


def closing_triples(N):
    return sum(1 for k in range(1, N) for l in range(1, N) if (-(k + l)) % N != 0)


def unit_triples(N):
    U = [k for k in range(1, N) if gcd(k, N) == 1]
    return sum(1 for k in U for l in U if (-(k + l)) % N in U)


def boundary_share(N, beta):
    """units (conductor N) share with each packet weighted by phi(c)*c^beta."""
    num = float(totient(N)) * N ** beta
    den = sum(float(totient(c)) * c ** beta for c in divisors(N) if c > 1)
    return num / den


def beta_star(N, lo=-30.0, hi=30.0):
    """beta where boundary_share = 1/2 (monotone increasing -> bisection)."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if boundary_share(N, mid) < 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def participation(weights):
    """effective number of active packets = (sum w)^2 / sum w^2."""
    w = np.array(weights, float)
    return float(w.sum() ** 2 / (w * w).sum())


# ---------------------------------------------------------------------------
def main():
    print("#" * 76)
    print("#  Paper 32.1  Audit 6 -- The 5-joining transition (Z/6 -> Z/30)")
    print("#" * 76)

    # ---------------- PART A ----------------
    p6, p30 = packets(6), packets(30)
    print("\nPART A -- the discrete step (atomic)")
    print("-" * 60)
    print(f"  packets: {len(p6)} (Z/6) -> {len(p30)} (Z/30)   (+{len(p30)-len(p6)})")
    print(f"  conductors Z/6 : {sorted(p6)}   (boundary = 6)")
    print(f"  conductors Z/30: {sorted(p30)}   (boundary = 30; c=6 -> interior)")
    print(f"  new conductors (carry 5): {sorted(c for c in p30 if c not in p6)}")
    print(f"  boundary (units) dim: {int(totient(6))} -> {int(totient(30))}  "
          f"(x{int(totient(30))//int(totient(6))} = x(5-1))")
    print(f"  cubic 3-body cross-couplings: {closing_triples(6)} -> "
          f"{closing_triples(30)}  (x{closing_triples(30)//closing_triples(6)})")
    print(f"  pure-unit closing triples: Z/6={unit_triples(6)}  "
          f"Z/30={unit_triples(30)}  (0 = gravity stays BULK-SOURCED)")
    print("  => the structural step is a QUANTUM (no interior critical point).")

    # ---------------- PART B ----------------
    print("\nPART B -- the weighting-temperature logit  S_N(beta)")
    print("   boundary share with packet weight phi(c)*c^beta  (sigmoid 0->1)")
    print("-" * 60)
    print(f"  {'beta':>6} | {'S_6':>8} | {'S_30':>8}")
    for b in (-4, -2, -1, 0, 1, 2, 4):
        print(f"  {b:>6} | {boundary_share(6,b):>8.4f} | {boundary_share(30,b):>8.4f}")
    b6, b30 = beta_star(6), beta_star(30)
    print(f"\n  critical (sweet spot) beta* where boundary = bulk = 1/2:")
    print(f"     Z/6 : beta* = {b6:+.4f}   [S(0)={boundary_share(6,0):.3f} "
          f"(dim), S(1)={boundary_share(6,1):.3f} (Landau-cond)]")
    print(f"     Z/30: beta* = {b30:+.4f}   [S(0)={boundary_share(30,0):.3f} "
          f"(dim), S(1)={boundary_share(30,1):.3f} (Landau-cond)]")
    print(f"  5 joining shifts the sweet spot by  delta beta* = {b30-b6:+.4f}")
    print(f"  (beta* > 0 both rows: you must OVER-weight conductor to make the")
    print(f"   boundary balance the bulk; 5 joining pushes beta* "
          f"{'up' if b30>b6 else 'down'}.)")

    # ---------------- PART C ----------------
    print("\nPART C -- the horizon handoff  (grade prime 5 by t in [0,1])")
    print("-" * 60)
    # old boundary c=6 (NOT graded by t); new boundary c=30 (graded by t).
    # conductor weighting (beta=1): contribution = phi(c)*c*(t if 5|c else 1)
    c6w = float(totient(6)) * 6           # = 12, constant
    c30w = float(totient(30)) * 30        # = 240, scaled by t
    t_star_cond = c6w / c30w
    # dimension weighting (beta=0): phi(c)*(t if 5|c)
    t_star_dim = float(totient(6)) / float(totient(30))   # 2/8
    print(f"  conductor weight: new boundary (c=30, w=240t) overtakes")
    print(f"     old boundary (c=6, w=12) at  t* = {t_star_cond:.3f}")
    print(f"  dimension weight: c=30 (dim 8t) overtakes c=6 (dim 2) at "
          f"t* = {t_star_dim:.3f}")
    print(f"  => the boundary RELABELS c=6 -> c=30 almost immediately "
          f"(t* ~ {t_star_cond:.2f}): a fast baton-change, not a slow swell.")
    # richness: effective number of active packets, t=0 vs t=1
    def weights(N, beta, t):
        w = []
        for c in divisors(N):
            if c == 1:
                continue
            g = t if (c % 5 == 0) else 1.0
            w.append(float(totient(c)) * c ** beta * g)
        return [x for x in w if x > 0] if t > 0 else \
               [float(totient(c)) * c ** beta for c in divisors(N)
                if c > 1 and c % 5 != 0]
    pr0_dim = participation([float(totient(c)) for c in divisors(6) if c > 1])
    pr1_dim = participation([float(totient(c)) for c in divisors(30) if c > 1])
    pr0_cd = participation([float(totient(c))*c for c in divisors(6) if c > 1])
    pr1_cd = participation([float(totient(c))*c for c in divisors(30) if c > 1])
    print(f"  packet participation (effective # active packets):")
    print(f"     dimension weight: {pr0_dim:.2f} -> {pr1_dim:.2f}")
    print(f"     conductor weight: {pr0_cd:.2f} -> {pr1_cd:.2f}  "
          f"(weight concentrates on the new top boundary)")

    # ---------------- PART D ----------------
    print("\nPART D -- diminishing returns (Mertens shaping weight -log(1-1/p))")
    print("-" * 60)
    for p in (2, 3, 5, 7):
        print(f"     p={p}: shaping weight = {-log(1-1/p):.4f}")
    w2, w3, w5 = -log(0.5), -log(2/3), -log(4/5)
    print(f"  5 shapes ~{w5/w2:.2f}x as much as 2 and ~{w5/w3:.2f}x as much "
          f"as 3: confirms the 2,3 SWEET SPOT (Z/6 is where the action is).")

    # ---------------- VERDICT ----------------
    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    print("  SHARP BATON-CHANGE, not a smooth swell:")
    print(f"   - structure jumps atomically (3->7 packets; boundary x4; "
          f"cross-coupling x40);")
    print(f"   - the gravity boundary relabels c=6 -> c=30 at t* ~ "
          f"{t_star_cond:.2f} (near-immediate);")
    print(f"   - the LOGIT/sweet-spot exists only under a weighting temperature")
    print(f"     (Part B): critical beta* = {b6:.3f} (Z/6) -> {b30:.3f} (Z/30).")
    print("  The swell is the (archimedean) smoothing of an atomic event --")
    print("  exactly the step-vs-logit duality of the philosophy: the step is")
    print("  the truth, the logit is the temperature's gentle lie about it.")
    print("  Observed invariants (3+1 dim, Weinberg 3/8) sit on the 2,3 side;")
    print("  5 builds the GUT wing (E: 5->10, F: 15->55) and the receded,")
    print("  quadrupled gravity boundary -- the unobserved register.")
    print("\nAUDIT 6: TRANSITION CHARACTERIZED (sharp step + temperature-logit).")


if __name__ == "__main__":
    main()
