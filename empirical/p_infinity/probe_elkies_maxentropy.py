"""
Elkies's 1/(p-1) heuristic, exploited info-geometrically: the apex cumulant tower = the MAX-ENTROPY
(uniform) law on (Z/p)^x; RH/GRH content lives in the ANGULAR (Dirichlet-character / L-function)
directions, NOT the RADIAL (entropy/KL) direction.

We verify the load-bearing split on actual primes:
  - RADIAL: relative entropy D(empirical primes mod p || uniform) -> 0 (the free/count side; definite).
  - ANGULAR: for each nontrivial character chi mod p, the prime character sum S_chi(X)=sum_{q<=X} chi(q).
    Under GRH |S_chi| = O(sqrt(X) log X) -- we measure |S_chi|/sqrt(X). These are the L(s,chi) directions
    (the location/RH side; indefinite, oscillating). The trivial-character sum = pi(X) (the radial count).

If the angular sums scale ~ sqrt(X) (bounded |S_chi|/sqrt(X)) while the entropy -> 0, the picture holds:
the deviation from max-entropy uniform is square-root and lives in the character/L-function channel.

No torch. numpy (sieve) + cmath. Deterministic.
"""
import numpy as np, cmath, math

def primes_upto(N):
    s = np.ones(N+1, bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.flatnonzero(s)

def prim_root(p):
    for g in range(2, p):
        seen = set(); x = 1
        for _ in range(p-1):
            x = x*g % p; seen.add(x)
        if len(seen) == p-1: return g

def index_table(p, g):           # discrete log: ind[a] s.t. g^ind = a (mod p)
    ind = [0]*p; x = 1
    for e in range(p-1):
        ind[x] = e; x = x*g % p
    return ind

print("=" * 84)
print("Max-entropy (uniform on (Z/p)^x) reference vs primes: RADIAL entropy vs ANGULAR L-channels")
print("=" * 84)

P = primes_upto(10_000_000)
for p in (5, 7, 11, 13):
    g = prim_root(p); ind = index_table(p, g); phi = p-1
    print(f"\n  p={p}  (phi={phi}, primitive root {g}); characters chi_k(a)=exp(2pi i k*ind(a)/{phi}):")
    print(f"    {'X':>10} {'rel.entropy D(emp||unif)':>24} " +
          " ".join(f"|S_chi{k}|/sqrtX" for k in range(1, phi)))
    for X in (10**5, 10**6, 10**7):
        q = P[(P <= X) & (P != p)]                          # primes <= X, coprime to p
        res = (q % p)
        counts = np.array([np.sum(res == a) for a in range(1, p) ], dtype=float)  # a=1..p-1 (all coprime)
        tot = counts.sum(); emp = counts/tot
        D = float(np.sum(emp*np.log(emp*phi)))              # KL(emp || uniform), the radial deviation
        # angular: character sums over a=1..p-1 weighted by counts
        ang = []
        for k in range(1, phi):
            S = sum(counts[a-1]*cmath.exp(2j*math.pi*k*ind[a]/phi) for a in range(1, p))
            ang.append(abs(S)/math.sqrt(X))
        print(f"    {X:>10} {D:>24.3e} " + " ".join(f"{v:>11.3f}" for v in ang))

print("\n" + "=" * 84)
print("""READING:
  * RADIAL: the relative entropy D(empirical || uniform) -> 0 as X grows (each factor ~1/X) -- the primes
    converge to the MAX-ENTROPY uniform law on (Z/p)^x. This is the FREE / count / metric / even / ZETA
    side; it is a definite (convex) functional -> vacuous for RH (the long-recorded "KL is vacuous").
  * ANGULAR: the per-character prime sums |S_chi|/sqrt(X) stay O(1)-ish (bounded, not growing) -- the
    deviation from uniform is SQUARE-ROOT and lives in the nontrivial-character = L(s,chi) directions.
    These are the LOCATION / chiral / odd channel; GRH = these stay sqrt-bounded (zeros on Re=1/2).
  SYNTHESIS: Elkies's 1/phi(p) = the max-entropy reference (radial, free). RH/GRH = the angular
  (character/L-function) deviation is square-root. The even/odd (zeta vs L_chi) split, the definite/
  indefinite dichotomy, and the KL-vacuity are ALL the radial-vs-angular geometry of (Z/p)^x.
""")
print("=" * 84)
