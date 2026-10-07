"""
Attack on Option 3 -- the pole (s=1, residue 1, Euclid's "+1") as the infrared stabilizer.

psi(x) = sum_{p^k<=x} log p = x - sum_rho x^rho/rho - ...   [explicit formula]
   pole / +1  = the budget x ;   zeros = the fluctuation.

DELUSIONAL: the pole budget is PROVEN to dominate grossly -- PNT is exactly psi(x) ~ x. The +1
never grossly runs out. So unlike Option 2 (the floor is merely smooth), here the floor PROVABLY
wins at leading order. The strategy: show the pole's PRECISE budget covers the fluctuation uniformly.

PARANOID AUDIT:

  A1  GROSS DOMINANCE IS A THEOREM (PNT).  psi(x)/x -> 1 : the +1 budget is asymptotically exact.
      The pole provably dominates at leading order -- "does the +1 stabilize?" is settled YES.

  A2  RH IS THE PRECISE MARGIN, NOT THE DOMINANCE.  (psi(x)-x)/sqrt(x) is the precise budget margin;
      it OSCILLATES (the zeros). RH = it stays bounded (O(log^2 x)). The dominance is proven; the
      RATE is RH. So Option 3 REMOVES the dominance question (PNT) and isolates the precision.

  A3  THE +1 IS AT IMAGINARY FREQUENCY, THE PRIMES AT REAL -- the budget is orthogonal to the spikes.
      The pole sits at s=1 <-> r=i/2 (off the real axis); the primes at r=log p (real). The pole
      provides the positive de Branges/Herglotz measure; an off-line zero is the only thing that can
      flip its sign. So "the +1 never runs out in the IR" = "no off-line zero overwhelms the pole
      measure" = the de Branges Hermite-Biehler positivity = RH. Euclid-escape reduces to it.

VERDICT (pre-registered): the pole route PROVES the gross stabilization (PNT) -- a real, strong
statement -- and localizes RH to the precise margin (the sqrt(x) rate / the resonant spike / the
uniform level). It does NOT close: proving the precise margin uniformly is the medium arc. Fourth
equivalent name for the obstruction: MAIN TERM (pole/+1, proven dominant) vs FLUCTUATION (zeros).

No torch. sympy + mpmath. Deterministic.
"""
import mpmath as mp
from sympy import primerange
mp.mp.dps = 30

GREEN = True
def fail(m):
    global GREEN; GREEN = False; print("   *** RED:", m)

def psi_chebyshev(x):
    """sum_{p^k <= x} log p, exact over prime powers."""
    x = int(x)
    total = mp.mpf(0)
    for p in primerange(2, x + 1):
        lp = mp.log(p)
        pk = p
        while pk <= x:
            total += lp
            pk *= p
    return total

print("=" * 80)
print("Attack on Option 3: the pole / Euclid's +1 as the infrared budget")
print("=" * 80)

# A1: gross dominance is PNT (the +1 budget is asymptotically exact)
print("\nA1  pole budget gross dominance (PNT, a THEOREM): psi(x)/x -> 1")
xs = [10**2, 10**3, 10**4, 10**5, 10**6]
ratios = []
for x in xs:
    psi = psi_chebyshev(x)
    r = psi / x
    ratios.append(r)
    print(f"   x=10^{len(str(x))-1}: psi(x)/x = {mp.nstr(r,8)}   (the +1 budget; -> 1 by PNT)")
if not abs(ratios[-1] - 1) < mp.mpf('0.02'):
    fail("A1 psi(x)/x not approaching 1")
print("   => the pole PROVABLY dominates at leading order: the +1 budget never grossly runs out.")

# A2: RH is the precise margin -- (psi(x)-x)/sqrt(x) oscillates (the zeros)
print("\nA2  the PRECISE margin (psi(x)-x)/sqrt(x): oscillates (the zeros); RH = bounded:")
margins = []
for x in [100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 10**6]:
    psi = psi_chebyshev(x)
    m = (psi - x) / mp.sqrt(x)
    margins.append(m)
    print(f"   x={x:>8}: (psi(x)-x)/sqrt(x) = {mp.nstr(m,6)}")
sgn = set(int(mp.sign(m)) for m in margins)
print(f"   sign set = {sgn}  ({'BOTH => oscillates => carries zeros; uniform bound = RH' if len(sgn)>1 else 'one sign so far'})")
# the margin should stay O(1)-ish in this range (RH-consistent), and oscillate
if max(abs(m) for m in margins) > 10:
    fail("A2 margin unexpectedly large (would contradict RH numerically)")

# A3: structural note -- the budget is orthogonal to the spikes (pole at i/2, primes real)
print("\nA3  structural: pole at s=1 <-> r=i/2 (imaginary freq); primes at r=log p (real freq).")
print("    The +1 provides the de Branges/Herglotz positive measure; an OFF-LINE zero is the only")
print("    thing that can overwhelm it. 'The +1 never runs out in the IR' = 'no off-line zero flips")
print("    the pole measure' = the Hermite-Biehler positivity of E_B = Xi + i Xi' = RH.")

print("\n" + "=" * 80)
print("RESULT:", "GREEN -- audit complete" if GREEN else "RED")
print("=" * 80)
print("""
VERDICT:
  Option 3 is STRONGER than Option 2 in one precise way: the pole's gross dominance is a PROVEN
  THEOREM (PNT, psi(x)/x -> 1; A1) -- "does the +1 stabilize?" is settled YES, not merely structural.
  RH is therefore NOT the dominance but the PRECISE MARGIN (psi(x)-x)/sqrt(x), which oscillates with
  the zeros (A2) and whose uniform boundedness IS RH. The Euclid-escape framing reduces cleanly to
  the de Branges/Herglotz positivity (A3): the +1 supplies the positive measure; an off-line zero is
  the only thing that can overwhelm it. So the pole route PROVES the stabilization and isolates the
  gap to the second-order precision -- the sqrt(x) rate, the resonant spike, the uniform level (the
  medium arc). Fourth equivalent name of the obstruction, joining the other three:
        MAIN TERM (pole/+1, PROVEN dominant)  vs  FLUCTUATION (zeros, the precise margin).
  Net gain over Options 1-2: the *dominance* is now a theorem; only the *margin* remains.
""")
