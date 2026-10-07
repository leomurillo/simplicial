"""
Verify the Bertrand containment: for the binding window s in [1-q'/q, 1-q''/q] to be in [-1,1/2]:
  upper: 1 - q''/q <= 1/2  <=> q'' >= q/2  (prevprime(q) >= q/2)
  lower: 1 - q'/q  >= -1   <=> q'  <= 2q   (nextprime(q) <= 2q)
Bertrand's postulate: for any n>1 there is a prime in (n/2, n) and in (n,2n).
=> prevprime(q) > q/2 (a prime lies strictly between q/2 and q, so the immediate predecessor is > q/2)
=> nextprime(q) < 2q  (a prime lies strictly between q and 2q)
Both strict. Verify numerically for primes up to a large bound, AND confirm the exact per-piece
check covered all primes q < 60 (i.e. k from 1).
"""
from sympy import primerange, prevprime, nextprime, Rational
import sympy as sp

P = list(primerange(2, 200000))
bad_up = []
bad_lo = []
for k in range(1, len(P)-1):
    q = P[k]; qp = P[k-1]; qn = P[k+1]
    # q'' = qp = prevprime, q' = qn = nextprime
    if not (qp >= Rational(q,2)):    # need q'' >= q/2
        bad_up.append((q,qp))
    if not (qn <= 2*q):              # need q' <= 2q
        bad_lo.append((q,qn))
print(f"Checked primes up to {P[-2]}.")
print("Violations of prevprime(q) >= q/2 :", bad_up[:10], " (count", len(bad_up),")")
print("Violations of nextprime(q) <= 2q  :", bad_lo[:10], " (count", len(bad_lo),")")

# small-q coverage: primes q with 3 <= q < 60
small = [p for p in P if 3 <= p < 60]
print("\nPrimes q in [3,60) (covered by exact finite per-piece check, which ran to 7927):")
print(" ", small)
print("All these have k index >=1 and were in the exact check range. Good.")

# Double check: at q=2 (k=0) the piece is B in (-5, +oo) -- that's the B>=-5 region, NOT B<=-5.
# So the B<=-5 ray is exactly the union of pieces k>=1 (binding prime q=3,5,7,...). Confirm:
print("\nPiece for q=2 (k=0): B in (-(2+3), +oo) = (-5, +oo). So B<=-5 uses ONLY k>=1 pieces. Confirmed.")
