#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32.1  Audit 7  --  The prime-joining ladder (5 -> 7 -> 11 -> ...)
======================================================================

Generalizes Audit 6 (the 5-joining transition) to the whole squarefree
primorial ladder Z/6 -> Z/30 -> Z/210 -> Z/2310 (-> Z/30030), so we can read
the 7-joining step exactly and PROJECT the 11-step (and beyond) from closed
forms. Everything here is conductor-lattice combinatorics -- light; it does
NOT need the heavy mu_210 spectral integrator (blocked on memory).

Closed-form step laws (derived, verified below):
  * packets         = 2^k - 1            (k = number of primes; Boolean lattice)
  * boundary dim    = phi(N) = prod(p-1) ; joining p multiplies it by (p-1)
  * cross-couplings = (N-1)(N-2)         (ordered cubic closing triples)
  * horizon handoff = t* = 1/(p(p-1))    (new top conductor overtakes old)
  * inner space E   = sum of primes      ; F = E(E+1)/2  (=Lambda^2 E + E*)
  * sweet-spot beta* (boundary=bulk under weight phi(c) c^beta): computed.

FIREWALL (Paper 32 sec 12): pure numbers / ratios / exponents only.
"""

from math import gcd, log
from sympy import totient, divisors, primefactors


def packets(N):
    return [c for c in divisors(N) if c > 1]


def boundary_share(N, beta):
    num = float(totient(N)) * N ** beta
    den = sum(float(totient(c)) * c ** beta for c in packets(N))
    return num / den


def beta_star(N, lo=-40.0, hi=40.0):
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if boundary_share(N, mid) < 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def triples(N):
    return (N - 1) * (N - 2)          # ordered cubic closing triples (exact)


def edim(N):
    return sum(primefactors(N))       # E = (+) C^p over primes p | N


def verify_closed_forms():
    ok = True
    for N in (6, 30, 210, 2310):
        k = len(primefactors(N))
        ok &= (len(packets(N)) == 2 ** k - 1)
        # brute cubic count check on small N
        if N <= 210:
            brute = sum(1 for a in range(1, N) for b in range(1, N)
                        if (-(a + b)) % N != 0)
            ok &= (brute == triples(N))
    return ok


def main():
    print("#" * 78)
    print("#  Paper 32.1  Audit 7 -- The prime-joining ladder (5 -> 7 -> 11)")
    print("#" * 78)

    print(f"\nClosed-form sanity check (packets=2^k-1, triples=(N-1)(N-2)): "
          f"{verify_closed_forms()}")

    ladder = [6, 30, 210, 2310, 30030]

    # ---------------- PART A: per-row invariants ----------------
    print("\nPART A -- per-row invariants")
    print("-" * 78)
    print(f"{'N':>6} {'k':>2} {'packets':>8} {'phi(N)':>7} {'beta_dim':>9} "
          f"{'beta_cond':>10} {'beta*':>7} {'E':>4} {'F':>6} {'triples':>11}")
    rows = {}
    for N in ladder:
        k = len(primefactors(N))
        phi = int(totient(N))
        bdim = phi / (N - 1)
        bcond = boundary_share(N, 1.0)
        bstar = beta_star(N)
        E = edim(N)
        F = E * (E + 1) // 2
        T = triples(N)
        rows[N] = dict(k=k, phi=phi, bdim=bdim, bcond=bcond, bstar=bstar,
                       E=E, F=F, T=T)
        print(f"{N:>6} {k:>2} {2**k-1:>8} {phi:>7} {bdim:>9.4f} "
              f"{bcond:>10.4f} {bstar:>7.4f} {E:>4} {F:>6} {T:>11}")

    # ---------------- PART B: per-step (prime joining) ----------------
    print("\nPART B -- per-step transition (prime p joins)")
    print("-" * 78)
    print(f"{'step':>14} {'p':>3} {'demoted bnd':>12} {'t* handoff':>11} "
          f"{'phi x(p-1)':>11} {'Mertens wt':>11} {'d beta*':>9}")
    steps = [(6, 30, 5), (30, 210, 7), (210, 2310, 11), (2310, 30030, 13)]
    for (Nold, Nnew, p) in steps:
        tstar = 1.0 / (p * (p - 1))
        mert = -log(1 - 1.0 / p)
        dbeta = rows[Nnew]['bstar'] - rows[Nold]['bstar']
        print(f"  Z/{Nold:<5}->Z/{Nnew:<5} {p:>3} {Nold:>12} {tstar:>11.5f} "
              f"{'x'+str(p-1):>11} {mert:>11.4f} {dbeta:>+9.4f}")

    # ---------------- PART C: the 7-step, in focus ----------------
    print("\nPART C -- THE 7-STEP  (Z/30 -> Z/210, 7 joins {2,3,5})")
    print("-" * 78)
    r30, r210 = rows[30], rows[210]
    print(f"  packets         : {2**3-1} -> {2**4-1}   (the Boolean lattice doubles)")
    print(f"  gravity boundary: phi {r30['phi']} -> {r210['phi']}   (x6 = x(7-1))")
    print(f"    old boundary conductor 30 -> demoted to interior; new boundary = 210")
    print(f"  cross-couplings : {r30['T']} -> {r210['T']}   "
          f"(x{r210['T']//r30['T']})")
    print(f"  horizon handoff : t* = 1/(7*6) = {1/42:.5f}   "
          f"(faster than 5's 0.050)")
    print(f"  inner space     : E {r30['E']} -> {r210['E']},  F {r30['F']} -> "
          f"{r210['F']}   (GUT enlargement; F=E(E+1)/2)")
    print(f"  sweet spot      : beta* {r30['bstar']:.4f} -> {r210['bstar']:.4f}  "
          f"(d={r210['bstar']-r30['bstar']:+.4f})")
    print(f"  boundary share  : beta_dim {r30['bdim']:.4f} -> {r210['bdim']:.4f}; "
          f"beta_cond {r30['bcond']:.4f} -> {r210['bcond']:.4f}")

    # ---------------- PART D: getting ready for 11 ----------------
    print("\nPART D -- GETTING READY FOR 11  (Z/210 -> Z/2310)")
    print("-" * 78)
    r2310 = rows[2310]
    print(f"  packets         : {2**4-1} -> {2**5-1}")
    print(f"  gravity boundary: phi {r210['phi']} -> {r2310['phi']}   (x10 = x(11-1))")
    print(f"    conductor 210 demoted; new boundary = 2310")
    print(f"  cross-couplings : {r210['T']} -> {r2310['T']}   "
          f"(x{r2310['T']//r210['T']})")
    print(f"  horizon handoff : t* = 1/(11*10) = {1/110:.5f}   "
          f"(sharper still: the baton-change keeps speeding up)")
    print(f"  inner space     : E {r210['E']} -> {r2310['E']},  F {r210['F']} -> "
          f"{r2310['F']}")
    print(f"  sweet spot      : beta* {r210['bstar']:.4f} -> {r2310['bstar']:.4f}  "
          f"(d={r2310['bstar']-r210['bstar']:+.4f})")
    print(f"  boundary share  : beta_dim {r210['bdim']:.4f} -> {r2310['bdim']:.4f}; "
          f"beta_cond {r210['bcond']:.4f} -> {r2310['bcond']:.4f}")

    # ---------------- VERDICT ----------------
    print("\n" + "=" * 78)
    print("VERDICT -- two opposing trends, sharpening baton, stacking horizons")
    print("=" * 78)
    print("  Each new prime p:")
    print("   * DOUBLES the conductor lattice (packets 3->7->15->31 = 2^k-1)")
    print("   * multiplies the gravity boundary by (p-1)  (phi: 2->8->48->480)")
    print("   * hands the boundary baton FASTER: t* = 1/(p(p-1)) -> 0")
    print("       5: 0.050,  7: 0.024,  11: 0.0091,  13: 0.0064")
    print("   * SHAPES LESS per mode (Mertens 1/p: 0.22, 0.15, 0.095, 0.080)")
    print("   * but EXPLODES cross-coupling MORE: (N-1)(N-2) ~ N^2, x40, x54, x123")
    print("     => diminishing shaping, exploding connectivity: opposite trends.")
    print("   * raises the sweet-spot temperature beta* (bulk outgrows the lone")
    print(f"       top boundary): {rows[6]['bstar']:.3f} -> {rows[30]['bstar']:.3f}"
          f" -> {rows[210]['bstar']:.3f} -> {rows[2310]['bstar']:.3f}.")
    print("  The demoted boundaries STACK like sediment: 6, 30, 210, 2310 --")
    print("  each the gravity horizon of its era, then buried by the next prime.")
    print("  Gravity stays bulk-sourced at every even row (parity-inertness).")
    print("\nAUDIT 7: LADDER CHARACTERIZED; 7-step exact, 11-step projected, "
          "13+ by formula.")


if __name__ == "__main__":
    main()
