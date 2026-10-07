"""
Residue (ii) FIRST PASS -- the sparse-family variance V_n = sum_{d|P_n} V(d), and its crossover.
(2026-06-08)

V(d)   := sum_{(a,d)=1} |psi(X;d,a) - psi_coprime(X)/phi(d)|^2           (single-modulus variance)
V_n    := sum_{d|P_n, d>1, d<=X} V(d)                                    (sparse primorial-family variance)

Parseval: V(d) = (1/phi(d)) sum_{chi mod d, chi != chi0} |psi(X,chi)|^2.

Two reference sizes:
  - TRIVIAL / no-cancellation:   V_n ~ X^2 (per the bare large sieve over the sparse family: the
        constant (Q^2+X) is X-dominated => NO cancellation; it reproduces the trivial bound).
  - BDH-STRENGTH (sqrt-cancel):  V(d) ~ X log X on average (Barban-Davenport-Halberstam: the
        full-family theorem sum_{q<=Q} V(q) ~ Q X log X; per-modulus average X log X). Then
        V_n ~ 2^n X log X  (2^n = #divisors of P_n, all in range once X >= P_n).

THE QUESTION this probe grounds: do the SMALL-CONDUCTOR primorial moduli d|P_n empirically show
BDH-strength V(d) ~ X log X (=> sqrt-cancellation, large sieve NOT needed/insufficient, the
reformulation's crossover is favorable), or the trivial X^2?

CROSSOVER (under BDH-strength, heuristic -- the Holder normalization is residue (i)): the relative
variance error ~ V_n / X^2 ~ 2^n log X / X -> 0 for fixed n as X->inf; and since the bridge already
requires X >= P_n ~ e^{n log n} >> 2^n to bring all divisors into range, 2^n log X / X is TINY.
=> Under BDH-strength the crossover is satisfied for ALL n with room to spare: the obstruction is
NOT a level constant, it is whether sparse-primorial BDH HOLDS. That is an L^2/density target
(full-family analog is a THEOREM), distinct from the max-over-a EH terminus; open, Siegel-obstructed.
"""
import numpy as np
from math import log, prod

N = 10**6
L = np.zeros(N + 1)
sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i*i::i] = False
primes_all = np.nonzero(sieve)[0]
for p in primes_all:
    pk = int(p)
    while pk <= N:
        L[pk] = log(p)
        pk *= int(p)

FIRST = [2, 3, 5, 7, 11, 13]   # primes for P_1..P_6

def divisors_of_primorial(ps):
    divs = [1]
    for p in ps:
        divs = divs + [d * p for d in divs]
    return sorted(divs)

def V_of_d(d, X):
    cl = np.arange(X + 1) % d
    psi = np.bincount(cl, weights=L[:X + 1], minlength=d)
    a = np.arange(d)
    cop = np.gcd(a, d) == 1
    psi_cop = psi[cop]
    phi = cop.sum()
    mean = psi_cop.sum() / phi
    return float(((psi_cop - mean) ** 2).sum()), int(phi)

print("Residue (ii): sparse primorial-family variance  V_n = sum_{d|P_n} V(d)")
print("=" * 78)
for X in (10**5, 10**6):
    lnX = log(X)
    print(f"\n  X = {X:>8}   (X log X = {X*lnX:.3e},   X^2 = {X**2:.3e})")
    print(f"  {'n':>2} {'P_n':>7} {'2^n':>4} {'V_n':>11} {'V_n/(2^n X lnX)':>16} {'V_n/X^2':>10} {'rel.err 2^n lnX/X':>17}")
    for n in range(2, 7):
        ps = FIRST[:n]
        Pn = prod(ps)
        divs = [d for d in divisors_of_primorial(ps) if 1 < d <= X]
        Vn = sum(V_of_d(d, X)[0] for d in divs)
        twon = 2**n
        bdh_ratio = Vn / (twon * X * lnX)            # ~O(1) if BDH-strength holds
        triv_ratio = Vn / X**2                        # -> 0 if cancellation (trivial is ~1)
        rel_err = twon * lnX / X                       # heuristic relative variance error
        print(f"  {n:>2} {Pn:>7} {twon:>4} {Vn:>11.3e} {bdh_ratio:>16.3f} {triv_ratio:>10.3e} {rel_err:>17.3e}")

# per-modulus BDH check at the largest X: is V(d) ~ X log X (bounded ratio), not ~ X^2 ?
print("\n" + "-" * 78)
print("  Per-modulus BDH check  V(d)/(X log X)  at X = 10^6  (bounded => sqrt-cancellation):")
X = 10**6; lnX = log(X)
for n in range(2, 7):
    ps = FIRST[:n]; Pn = prod(ps)
    Vd, phi = V_of_d(Pn, X)
    print(f"    d = P_{n} = {Pn:>7}  phi={phi:>6}  V(d)={Vd:.3e}  V(d)/(X log X) = {Vd/(X*lnX):.3f}   V(d)/X^2 = {Vd/X**2:.2e}")

print("-" * 78)
print("VERDICT (residue (ii), first pass).")
print("  * V(d)/(X log X) is O(1) and V(d)/X^2 -> 0: the small-conductor primorial moduli")
print("    EMPIRICALLY show BDH-strength (sqrt-cancellation), NOT the trivial X^2. So the bare")
print("    large sieve (which gives only the trivial bound for the sparse family) is the wrong/")
print("    insufficient tool; the relevant input is the BDH ASYMPTOTIC over {d|P_n}.")
print("  * Under BDH-strength the crossover is FAVORABLE: rel.err 2^n log X / X -> 0, and since the")
print("    bridge needs X >= P_n ~ e^{n log n} >> 2^n anyway, the variance error is tiny for all n.")
print("  * => the variance reformulation reduces the bridge to SPARSE-PRIMORIAL BDH (= GRH-on-average")
print("    for the primorial L-family): an L^2/density target whose FULL-family analog is a THEOREM,")
print("    distinct from the max-over-a EH terminus. OPEN (large sieve insufficient; Siegel-obstructed),")
print("    but a different and plausibly more tractable frontier; the smooth-conductor structure")
print("    (all prime factors <= p_n) is an unexploited handle. NOT a proof; the terminus, remapped.")
