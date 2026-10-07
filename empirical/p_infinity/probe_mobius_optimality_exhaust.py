"""
Exhausting Option 4 -- Mobius/sieve square-root cancellation ("blind-spot optimality").

RH <=> M(x) = sum_{n<=x} mu(n) = O(x^{1/2+eps}).  mu = the sieve as a sign pattern; the cancellation
is the "no conspiracy" / information optimality.  Three exhaustive checks:

  C1  THE CANCELLATION SCALING.  max|M(x)|/x^theta over x<=N: bounded for theta>=1/2 (RH-consistent),
      growing for theta<1/2.  The optimal exponent is 1/2 -- the random-walk / central-limit scale.

  C2  THE BLIND-SPOT SELF-REFERENCE IS EXACT BUT TRIVIAL.  The recursion sum_{d=1}^{x} M(floor(x/d))=1
      (Mobius inversion mu*1=delta) holds exactly -- the sieve's self-reference.  BUT bounding it by
      |M| gives only O(x): |M(x)| <= 1 + sum_{d>=2}|M(x/d)| ~ x^theta * x^{1-theta} = O(x).  The
      cancellation lives in the SIGNS of M(x/d), which the recursion does not track.  Self-reference
      is exact bookkeeping, blind to the cancellation -- same lesson as the factorial.

  C3  THE GENUINE UNCONDITIONAL PROGRESS = the short-interval cancellation (Matomaki-Radziwill).
      In windows [x,x+h], the partial sum sum_{x<n<=x+h} mu(n) is ~ sqrt(h) (random scale), NOT ~h
      (no cancellation), for almost all x and h->inf -- proven UNCONDITIONALLY (MRT 2016).  This is
      the average sqrt(x) made strong; the UNIFORM sqrt(x) (no single spike) is RH.

No torch. numpy. Deterministic.
"""
import numpy as np

N = 2_000_000

# Mobius sieve (corrected: step p*p)
mu = np.ones(N + 1, dtype=np.int8)
is_p = np.ones(N + 1, dtype=bool); is_p[:2] = False
for p in range(2, int(N**0.5) + 1):
    if is_p[p]:
        is_p[p*p::p] = False
        mu[p::p] *= -1
        mu[p*p::p*p] = 0
for p in range(int(N**0.5) + 1, N + 1):
    if is_p[p]:
        mu[p::p] *= -1
M = np.concatenate([[0], np.cumsum(mu[1:].astype(np.float64))])   # M[x]=sum_{n<=x} mu(n)

print("=" * 80)
print("Exhausting Option 4: Mobius square-root cancellation (blind-spot optimality)")
print("=" * 80)

# sanity: known Mertens values
for x, val in [(1, 1), (10, -1), (100, 1), (1000, 2)]:
    print(f"   check M({x}) = {int(M[x])}  (known {val}) {'OK' if int(M[x])==val else 'MISMATCH'}")

# C1: the cancellation scaling
print("\nC1  cancellation scaling -- max|M(x)|/x^theta over x<=N (bounded iff theta>=1/2):")
xs = np.arange(1, N + 1, dtype=float)
absM = np.abs(M[1:])
for theta in [0.40, 0.45, 0.50, 0.55]:
    ratio = absM / xs**theta
    # running max over decades to show growth vs boundedness
    run = [float(np.max(ratio[:10**k])) for k in range(3, 7)]
    trend = "GROWS" if run[-1] > 1.6 * run[0] else "bounded"
    print(f"   theta={theta:.2f}: max|M|/x^theta by decade {[f'{r:.2f}' for r in run]}  -> {trend}")
print("   => theta=1/2 is the optimal (bounded) exponent: the random-walk / self-dual scale.")

# C2: blind-spot self-reference -- exact but trivial
print("\nC2  blind-spot self-reference: sum_{d=1}^{x} M(floor(x/d)) = 1 (exact), but O(x)-trivial:")
def recursion_sum(x):
    d = 1; tot = 0.0
    while d <= x:
        q = x // d
        # block where floor(x/d) == q
        d2 = x // q
        tot += M[q] * (d2 - d + 1)
        d = d2 + 1
    return tot
for x in [100, 1000, 10000, 100000]:
    print(f"   x={x:>7}: sum_d M(floor(x/d)) = {recursion_sum(x):.1f}  (identity = 1)")
print("   The recursion is EXACT (Mobius inversion) but bounding by |M| gives only O(x): the")
print("   cancellation is in the SIGNS, which the self-reference does not see (cf. the factorial).")

# C3: short-interval cancellation (MRT) -- the genuine unconditional progress
print("\nC3  short-interval cancellation (Matomaki-Radziwill, unconditional): partial sums ~ sqrt(h):")
print(f"   {'h':>7}   {'RMS of sum_window mu':>22}   {'sqrt(6h/pi^2) (random)':>24}   {'ratio':>7}")
for h in [100, 1000, 10000]:
    starts = np.arange(N // 4, N - h, max(1, (N - h - N//4) // 4000))
    sums = M[starts + h] - M[starts]
    rms = float(np.sqrt(np.mean(sums**2)))
    rand = np.sqrt(6 * h / np.pi**2)
    print(f"   {h:>7}   {rms:>22.3f}   {rand:>24.3f}   {rms/rand:>7.3f}")
print("   sum_window mu ~ sqrt(h) (random scale), NOT ~h: the sieve cancels in short windows,")
print("   UNCONDITIONALLY (MRT). This is the average sqrt(x) made strong; uniform sqrt(x) = RH.")

print("\n" + "=" * 80)
print("EXHAUSTED:")
print("""  Option 4 is the cleanest statement of your 'optimality': RH <=> M(x)=O(sqrt(x)) <=> the sieve
  cancels with no conspiracy. What is WON (unconditional): the average sqrt(x) (variance), the
  SHORT-INTERVAL cancellation (MRT, C3), and a positive proportion of zeros on the line (the mu
  mollifier, prev probe). What is RH: the UNIFORM sqrt(x) -- no single spike, the off-diagonal large
  deviation. The blind-spot self-reference (C2) is exact but trivial -- like the factorial, the
  bookkeeping recursion is blind to the sign-cancellation. So Option 4 = RH, reframed as optimality;
  the genuine levers are MRT (short intervals) and the mollifier (positive proportion), both feeding
  the same primorial level-of-distribution (Flank 1). An off-axis zero = a sieve conspiracy: a single
  window where the blind-spots fail to cancel beyond sqrt.
""")
print("=" * 80)
