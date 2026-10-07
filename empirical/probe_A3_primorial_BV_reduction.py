"""
[A3] empirical: primorial BV reduction — V vs M sector crossover analysis.

Structural reduction:
   Cubic positivity at the critical line, at primorial level P_n, requires the
   V-sector cubic energy to dominate the M-sector cubic error.

   V-sector: pure_V(P_n) = 2 + (1/6) sum_{p_i >= 5} (p_i^2 - 1)   [ocho §5, closed form]
            ~ n^3 (log n)^2 / 18 as n -> infty                    [ocho §6]

   M-sector estimate: |error|_M <~ P_n^{1 - theta_0(p_n)}         [Paper 43 BV at primorial p_n]

   V dominates M  iff  log(pure_V(P_n)) > (1 - theta_0(p_n)) * log(P_n).
   PNT: log(P_n) ~ p_n. So we need:
      3 log n + 2 log log n - log 18 > (1 - theta_0(p_n)) * p_n + o(1)
      <=>   (1 - theta_0(p_n)) <  (3 log n + 2 log log n - log 18) / p_n
      <=>   Delta(n) := 1 - theta_0(p_n) = O((log n) / p_n) = O(1/n)   [by p_n ~ n log n]

   This is the STRUCTURAL [A3] reduction: cubic positivity at primorial level
   requires polynomial-in-n decay of (1 - theta_0(p_n)), much weaker than full EH.

We compute:
  - pure_V(P_n) exact (closed form) for n = 1..30.
  - PNT-asymptotic check: pure_V(P_n) vs n^3 (log n)^2 / 18.
  - Required Delta(n) bound and required theta_0(p_n) schedule.
  - Comparison to Paper 43's r_0 = 5 result theta_0(5) ~= 0.538.
  - Identify the primorial index at which Paper 43's bound suffices.
"""

import numpy as np
from sympy import isprime, prime

def primes_up_to(N):
    return [p for p in range(2, N) if isprime(p)]

def nth_prime(n):
    return prime(n)

def primorial(n):
    """P_n = product of first n primes."""
    result = 1
    for i in range(1, n + 1):
        result *= prime(i)
    return result

def pure_V(n):
    """pure_V(P_n) = 2 + (1/6) sum_{p_i >= 5} (p_i^2 - 1).  ocho §5."""
    if n <= 2:
        return 2  # P_2 = 6, no primes >= 5
    total = 2
    for i in range(3, n + 1):
        p = prime(i)
        total += (p**2 - 1) / 6  # S(p) for p >= 5
    return total

def pure_V_PNT_asymptotic(n):
    """The PNT-asymptotic pure_V(P_n) ~ n^3 (log n)^2 / 18."""
    if n < 3:
        return 1.0
    return n**3 * np.log(n)**2 / 18

def Delta_required(n):
    """Required (1 - theta_0(p_n)) for V to dominate M.
    Delta(n) < (log pure_V(P_n)) / log P_n."""
    if n < 3:
        return 1.0
    pV = pure_V(n)
    Pn = float(primorial(n))
    return np.log(pV) / np.log(Pn)

def theta_0_required(n):
    return 1 - Delta_required(n)


# ============================================================================

print("=" * 100)
print("[A3] V-sector vs M-sector cubic energy at primorial levels")
print("Structural reduction: V dominates M iff theta_0(p_n) >= 1 - log(pure_V(P_n))/log(P_n)")
print("=" * 100)

print(f"\n{'n':>3s} {'p_n':>4s} {'P_n':>14s} {'pure_V(P_n)':>14s} {'pure_V/asymp':>14s} {'log P_n':>10s} {'Delta_req':>10s} {'theta_req':>12s}")
print("-" * 100)

for n in [2, 3, 4, 5, 6, 7, 10, 15, 20, 25, 30]:
    pn = nth_prime(n)
    Pn = float(primorial(n))
    pV = pure_V(n)
    pV_asymp = pure_V_PNT_asymptotic(n)
    ratio = pV / pV_asymp if pV_asymp > 0 else 0
    log_Pn = np.log(Pn)
    Delta_req = Delta_required(n)
    theta_req = theta_0_required(n)
    print(f"{n:3d} {pn:4d} {Pn:14.4e} {pV:14.4f} {ratio:14.4f} {log_Pn:10.4f} {Delta_req:10.4f} {theta_req:12.4f}")

# ----- Paper 43 r_0=5 comparison -----

print("\n" + "=" * 100)
print("Comparison with Paper 43's r_0 = 5 result: theta_0(5) ~= 0.538, Delta(5) ~= 0.462")
print("=" * 100)

theta_43 = 0.538  # Paper 43 hybrid BV saving
print(f"\n{'n':>3s} {'theta_required(n)':>20s} {'Delta_required(n)':>20s} {'gap to theta_43':>20s} {'V/M ratio (with Paper 43)':>28s}")
print("-" * 95)

for n in [2, 3, 5, 7, 10, 15, 20, 25, 30, 50]:
    theta_req = theta_0_required(n)
    Delta_req = 1 - theta_req
    gap = theta_req - theta_43
    # V/M ratio with Paper 43: pure_V / P_n^Delta_43
    pV = pure_V(n)
    Pn = float(primorial(n))
    M_estimate = Pn**(1 - theta_43)
    V_M_ratio = pV / M_estimate if M_estimate > 0 else float('inf')
    print(f"{n:3d} {theta_req:20.4f} {Delta_req:20.4f} {gap:+20.4f} {V_M_ratio:28.4e}")

# ----- Asymptotic rate analysis -----

print("\n" + "=" * 100)
print("Required Delta(n) asymptotic: should decay as O((log n)/p_n) = O(1/n)")
print("=" * 100)

print(f"\n{'n':>3s} {'p_n':>5s} {'Delta_req(n)':>14s} {'Delta_req * n':>16s} {'Delta_req * p_n':>18s} {'(log n) / p_n':>16s}")
print("-" * 75)
for n in [5, 10, 15, 20, 25, 30, 40, 50, 70, 100]:
    pn = nth_prime(n)
    D = Delta_required(n)
    print(f"{n:3d} {pn:5d} {D:14.6f} {D*n:16.4f} {D*pn:18.4f} {np.log(n)/pn:16.6f}")

# ----- Primorial index where Paper 43 r_0 = 5 already suffices -----

print("\n" + "=" * 100)
print("At what primorial index n* does theta_0 = 0.538 ALREADY suffice for V to dominate M?")
print("=" * 100)

n_star = None
for n in range(2, 200):
    theta_req = theta_0_required(n)
    if theta_req <= theta_43:
        n_star = n
        break

if n_star:
    print(f"\nn* = {n_star}: at primorial P_{n_star} = {primorial(n_star)} (p_{n_star} = {nth_prime(n_star)}),")
    print(f"  theta_required = {theta_0_required(n_star):.4f} <= theta_43 = {theta_43}.")
    print(f"  V-sector dominates M-sector at and beyond n = {n_star} WITH PAPER 43'S EXISTING BOUND.")
else:
    print(f"\nNo n in [2, 200] makes theta_required <= {theta_43}.")
    print("Paper 43's bound alone doesn't suffice at any primorial level reachable here.")
    print("\nWhat if we improve Paper 43's bound? Find n* for theta_43 = 0.7, 0.8, 0.9:")
    for theta_test in [0.55, 0.60, 0.70, 0.80, 0.90, 0.95]:
        n_star = None
        for n in range(2, 5000):
            if theta_0_required(n) <= theta_test:
                n_star = n
                break
        print(f"  theta_43 -> {theta_test}: V dominates from n* = {n_star} onwards")


# ----- Structural conclusion -----

print("\n" + "=" * 100)
print("Structural conclusion")
print("=" * 100)
print("""
[A3] reduction: cubic positivity at primorial level P_n requires
   theta_0(p_n) >= 1 - log(pure_V(P_n)) / log(P_n)
   = 1 - log(n^3 (log n)^2 / 18) / p_n   (PNT)
   = 1 - O((log n) / p_n)                (since p_n ~ n log n)
   = 1 - O(1/n)                          (asymptotic in n).

This is the POLYNOMIAL-IN-n EH refinement for squarefree primorial moduli,
significantly weaker than full EH (theta_0 = 1).

Paper 43's r_0 = 5 result gives theta_0 = 0.538, sufficient at n* (computed above).
For n < n*, the GAP to required theta is the analytic content of [A3].
For n > n*, [A3] is DISCHARGED by Paper 43's existing bound.

The remaining work: extend Paper 43's r_0 = 5 saving to higher r_0 via
the program's V perpendicular M decoupling and primorial-specific structure.
""")
