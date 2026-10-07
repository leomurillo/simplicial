"""
THE COMPOUNDING-VS-SATURATION CRUX, reduced to a computable object: the cubic central values L(1/2, chi_3).

Chain: forward door (rho_E<=1) -> center-anchored mollifier on friable PRIMORIAL moduli -> level theta->1
needs the well-factorable gains to COMPOUND (not saturate ~0.64). The program's anchor is CUBIC (trilinear
Kloosterman = triply-well-factorable = today's record 66/107). Non-saturation (theta_0(p_n)=1-C*/n->1)
requires the cubic teeth c_2 ~ |L(1/2,chi_3)|^2 to stay bounded BELOW uniformly over the primorial's primes.
So:  compounding -> 1   <=>   a uniform floor on L(1/2, chi_3) over conductor.

We MEASURE the distribution of |L(1/2, chi_3)| over cubic characters chi mod p (p == 1 mod 3, growing p):
  * if NO near-zero tail (values stay bounded below) -> a uniform floor is plausible -> compounding supported.
  * if a near-zero tail appears (some values small, shrinking with p) -> a uniform floor FAILS -> the route
    needs only POSITIVE-PROPORTION non-vanishing (hopeful; David et al >=14%) OR uniform (then it SATURATES).

L(1/2,chi) = p^{-1/2} sum_{a=1}^{p-1} chi(a) zeta(1/2, a/p)  (Hurwitz). chi(a) = zeta_3^{ind(a)} (cubic).

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 20
W3 = mp.e**(2j*mp.pi/3)

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5)+1))
def prim_root(p):
    for g in range(2, p):
        seen = set(); x = 1
        for _ in range(p-1):
            x = x*g % p; seen.add(x)
        if len(seen) == p-1: return g
def ind_table(p, g):
    ind = [0]*p; x = 1
    for e in range(p-1):
        ind[x] = e; x = x*g % p
    return ind

def Lhalf_cubic(p):
    """|L(1/2, chi)| for a cubic character chi mod p (p==1 mod 3)."""
    g = prim_root(p); ind = ind_table(p, g)
    # chi(a) = W3^{ind(a)} has order 3 (since 3 | p-1); take the primitive cubic character
    s = mp.mpf(1)/2
    tot = mp.mpf(0)*1j
    for a in range(1, p):
        chi = W3**(ind[a] % 3)
        tot += chi * mp.zeta(s, mp.mpf(a)/p)
    return abs(p**(-s) * tot)

print("=" * 82)
print("Cubic central values |L(1/2, chi_3)| over growing conductor: is there a uniform FLOOR?")
print("=" * 82)
ps = [p for p in range(7, 260) if is_prime(p) and p % 3 == 1]
vals = []
print(f"\n  {'p (cond.)':>10} {'|L(1/2,chi_3)|':>16}")
for p in ps:
    L = Lhalf_cubic(p); vals.append((p, L))
    if p <= 80 or p > 230 or float(L) < 0.45:
        print(f"  {p:>10} {mp.nstr(L,7):>16}")
fl = [float(v) for _, v in vals]
import statistics
mn = min(fl); mx = max(fl); md = statistics.median(fl); mean = statistics.mean(fl)
argmin_p = vals[fl.index(mn)][0]
small = [(p, v) for p, v in vals if float(v) < 0.4]
print(f"\n  over {len(vals)} cubic characters (p in [7,257], p==1 mod 3):")
print(f"    min |L| = {mn:.4f} (at p={argmin_p});  median = {md:.4f};  mean = {mean:.4f};  max = {mx:.4f}")
print(f"    count |L| < 0.40 : {len(small)}   {[ (p, round(float(v),3)) for p,v in small ]}")
# trend of the running minimum vs p (does the floor erode as conductor grows?)
print(f"    running min over first k conductors (does it ERODE with conductor?):")
import math
for k in (5, 10, 20, 30, len(fl)):
    rm = min(fl[:k])
    print(f"      first {k:>3} conductors: running min |L| = {rm:.4f}")

print("\n" + "=" * 82)
print(f"""READING:
  * If the running minimum STABILIZES (stops eroding) and min|L| stays well above 0, a uniform floor on the
    cubic central values is plausible -> the cubic teeth do NOT decay -> the well-factorable gains COMPOUND
    -> theta_0(p_n) = 1 - C*/n -> 1 is supported, and the center-anchored primorial route is NOT capped.
  * If the running minimum keeps ERODING toward 0 as conductor grows (a near-zero tail), a UNIFORM floor
    FAILS: some cubic central values are small. Then the route survives ONLY IF it needs positive-PROPORTION
    non-vanishing (David et al >=14% [P]) rather than a uniform bound -- and if it genuinely needs uniform,
    it SATURATES (the saturation flag was right).
  This converts the abstract 'compounding vs saturation' into a measured statement about |L(1/2,chi_3)|:
  the single quantity gating RH-via-this-door is whether the cubic central values have a uniform floor or a
  near-zero tail. (Whether the route needs uniform or positive-proportion is the next structural question --
  positive-proportion is KNOWN, uniform is GRH-strength.)
""")
print("=" * 82)
