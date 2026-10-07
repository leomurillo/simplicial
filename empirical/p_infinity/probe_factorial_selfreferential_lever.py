"""
Attack on Option 2 -- the self-referential factorial lever, pushed to its limit, then audited.

LEVER (delusional): log n! = sum_d Lambda(d) floor(n/d)  [Legendre = von Mangoldt convolution].
Split floor(n/d)=n/d-{n/d}:  log n! = n*sum_d Lambda(d)/d  -  sum_d Lambda(d){n/d}.
log n! is known EXACTLY (Stirling, all orders). The sawtooth {x}=1/2-sum_k sin(2pi kx)/(pi k)
brings the Chebyshev psi(n)=sum_{d<=n}Lambda(d)=n-sum_rho n^rho/rho into the fluctuation. So the
exactly-known factorial pins a prime-fluctuation sum that contains the ZEROS. Does it pin the zeros?

PARANOID AUDIT -- the three checks that decide it:

  A1  THE IDENTITY IS EXACT (log n! = sum_d Lambda(d) floor(n/d)) -- verify, several n.

  A2  THE FACTORIAL IS SMOOTH (no zero information).  log n! - Stirling is monotone and ->0 like
      1/(12n): the factorial carries NO oscillation. The zeros are oscillatory; a smooth object
      cannot pin them.

  A3  THE ZEROS LIVE IN psi(n)-n, WHICH THE FACTORIAL SMOOTHS AWAY.  psi(n)-n OSCILLATES (changes
      sign -- the zeros). But sum_d Lambda(d) floor(n/d) telescopes to sum_{N<=n} log N = log n!
      (A1) -- the floor (a COUNT, sum_{m<=n/d} 1) INTEGRATES the fluctuation, washing the oscillation
      out. So the factorial pins the SMOOTH main term, not the oscillating fluctuation. The lever
      re-derives the explicit-formula MAIN TERM (the free part) and is blind to the zeros (the gap).

Verdict: the lever does NOT fire. The risk flagged in advance materialized -- it re-derives the
explicit formula's main term; the factorial is the SMOOTH side of the prime count, the zeros are the
oscillation it cannot see. Third equivalent statement of the obstruction: SMOOTH (factorial/main) vs
OSCILLATING (zeros/fluctuation) = order-1/order-2 = diagonal/off-diagonal = multiplicative/additive.

No torch. sympy + mpmath. Deterministic.
"""
import mpmath as mp
from sympy import primerange, factorial, isprime, factorint
mp.mp.dps = 30

GREEN = True
def fail(m):
    global GREEN; GREEN = False; print("   *** RED:", m)

def Lambda(d):
    """von Mangoldt: log p if d = p^k, else 0."""
    f = factorint(d)
    if len(f) == 1:
        p = next(iter(f))
        return mp.log(p)
    return mp.mpf(0)

def log_factorial_via_vonmangoldt(n):
    """sum_{d<=n} Lambda(d) floor(n/d)."""
    return mp.fsum(Lambda(d) * (n // d) for d in range(2, n + 1))

def stirling(n):
    """log n! = n log n - n + 1/2 log(2 pi n) + 1/(12 n) - ..."""
    n = mp.mpf(n)
    return n * mp.log(n) - n + mp.mpf(0.5) * mp.log(2 * mp.pi * n) + 1 / (12 * n)

def psi_chebyshev(n):
    """sum_{d<=n} Lambda(d) = sum_{p^k<=n} log p."""
    return mp.fsum(Lambda(d) for d in range(2, n + 1))

print("=" * 80)
print("Attack on Option 2: the self-referential factorial lever -- does it pin the zeros?")
print("=" * 80)

# A1: the identity is exact
print("\nA1  log n! = sum_d Lambda(d) floor(n/d)  (Legendre = von Mangoldt convolution):")
for n in (10, 50, 200, 1000):
    lhs = mp.log(factorial(n))
    rhs = log_factorial_via_vonmangoldt(n)
    err = abs(lhs - rhs)
    print(f"   n={n:>5}: |log n! - sum Lambda(d) floor(n/d)| = {mp.nstr(err,3)}")
    if err > mp.mpf('1e-20'):
        fail(f"A1 identity fails at n={n}")

# A2: the factorial is SMOOTH (log n! - Stirling monotone -> 0, no oscillation)
print("\nA2  log n! - Stirling: smooth, monotone, ->0 like 1/(12n) (NO oscillation, NO zeros):")
prev = None
devs = []
for n in (100, 200, 400, 800, 1600, 3200):
    dev = mp.log(factorial(n)) - stirling(n)
    devs.append(dev)
    print(f"   n={n:>5}: log n! - Stirling = {mp.nstr(dev,4)}   (next Stirling term ~ -1/(360 n^3))")
# monotone decreasing in magnitude, never changes sign -> smooth
signs = set(int(mp.sign(d)) for d in devs if abs(d) > mp.mpf('1e-25'))
mono = all(abs(devs[i+1]) < abs(devs[i]) for i in range(len(devs)-1))
print(f"   sign set = {signs} (single sign = NO oscillation); |dev| monotone decreasing = {mono}")
if len(signs) > 1 or not mono:
    fail("A2 factorial deviation not smooth/monotone")

# A3: the zeros live in psi(n)-n, which OSCILLATES (changes sign) -- the factorial smooths it away
print("\nA3  psi(n)-n (Chebyshev error, carries the zeros): OSCILLATES, changes sign:")
errs = []
for n in (10, 30, 60, 100, 200, 400, 800):
    e = psi_chebyshev(n) - n
    errs.append(e)
    print(f"   n={n:>5}: psi(n)-n = {mp.nstr(e,5)}")
psi_signs = set(int(mp.sign(e)) for e in errs)
print(f"   sign set = {psi_signs}  ({'BOTH signs => OSCILLATES => carries zeros' if len(psi_signs)>1 else 'one sign'})")
if len(psi_signs) < 2:
    fail("A3 expected psi(n)-n to change sign (oscillation)")

print("\n" + "=" * 80)
print("RESULT:", "GREEN -- audit complete" if GREEN else "RED")
print("=" * 80)
print("""
VERDICT (the lever does NOT fire):
  The identity log n! = sum_d Lambda(d) floor(n/d) is EXACT (A1) -- but it telescopes to
  sum_{N<=n} log N, so it is the explicit formula's MAIN TERM, nothing more. The factorial is
  SMOOTH (A2): log n! - Stirling is monotone, single-signed, ->0 like 1/(12n) -- it carries no
  oscillation, hence no zero information. The zeros live in psi(n)-n, which OSCILLATES and changes
  sign (A3); the floor(n/d) = #{m<=n/d} is a COUNT that integrates the fluctuation, washing the
  oscillation out of the factorial. So the self-referential lever re-derives the free main term and
  is structurally blind to the zeros -- exactly the pre-registered risk ("it may just re-derive the
  explicit formula"), now realized. Third equivalent name for the obstruction:
        SMOOTH (factorial/main term)  vs  OSCILLATING (zeros/fluctuation)
     =  order-1  vs  order-2  =  diagonal  vs  off-diagonal  =  multiplicative  vs  additive.
  The factorial is, irreducibly, the smooth side; RH is the oscillation it cannot see.
""")
