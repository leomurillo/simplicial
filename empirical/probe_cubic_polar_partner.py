"""
"What does r=-3 suggest, partners with cubic?" -- the cubic polar pair and [A3'].

Three facts that locate the cubic in the polar-pairing / arrow structure.

FACT 1  The gauge<->spectral map r ~ 2*sigma-1 puts the cubic polar pair r=+-3 as
        functional-equation partners bracketing the critical line:
          r=+3 <-> sigma=2 ,  r=-3 <-> sigma=-1 ,  1-2=-1 (FE),  midpoint sigma=1/2 (r=0).
        (Same shape as r=+-2 <-> sigma=3/2,-1/2 used before.)

FACT 2  The single self-dual Xi is EVEN in z, so its ODD-order cumulants VANISH
        (kappa_3^z = 0): the cubic/arrow content is NOT in a single L-function. It must
        live in the JOINT / cross-character structure -- which is exactly where [A3']
        and the cluster c_2<0 (via L(1/2,chi_3)) live.

FACT 3  On Z/6 the cubic selection rule k+l+m=0 (mod 6) COUPLES distinct conductor
        packets, while the quadratic rule k+l=0 is block-diagonal within a packet.
        This is the Conductor Blind Spot, order 3: the cubic sees cross-packet
        structure the quadratic is constitutionally blind to. The cubic carries a SIGN
        (chirality) the quadratic square cannot.

Deterministic: mpmath + pure python.  No torch.
"""

import mpmath as mp
mp.mp.dps = 30

# ---------------------------------------------------------------------------
print("=" * 80)
print("FACT 1 -- the cubic polar pair r=+-3 are FE partners bracketing the line")
print("=" * 80)
for r in [3, -3, 2, -2, 0]:
    sigma = (r + 1) / 2          # r = 2 sigma - 1  =>  sigma = (r+1)/2
    fe = 1 - sigma               # functional-equation image
    print(f"  r={r:>3}  <->  sigma={sigma:>4}   FE image 1-sigma={fe:>4}   "
          f"(partner r'={2*fe-1:>3})")
print("  >>> r=+3 (sigma=2) and r=-3 (sigma=-1) are FE partners; midpoint sigma=1/2 = r=0")
print("      the critical line is the geometric center of the cubic polar pair.")

# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("FACT 2 -- single even Xi has NO odd cumulants: kappa_3 = 0 (cubic is JOINT)")
print("=" * 80)
def xi(s):
    return mp.mpf(1) / 2 * s * (s - 1) * mp.pi**(-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
def Xi(z):
    return xi(mp.mpf(1) / 2 + 1j * z)
def logXi(z):
    return mp.log(Xi(z))
# Taylor coefficients of log Xi(z) at z=0 (cumulants of the single object)
coeffs = mp.taylor(logXi, 0, 5, method='quad', radius=mp.mpf('3.0'))
print("  Taylor coefficients of log Xi(z) at z=0 (the single-Xi cumulants):")
for n, c in enumerate(coeffs):
    tag = "  <- ODD (should be 0)" if n % 2 == 1 else ""
    print(f"    z^{n}: {mp.nstr(mp.re(c), 6):>14}  (|im|={float(abs(mp.im(c))):.1e}){tag}")
odd_max = max(abs(coeffs[n]) for n in (1, 3, 5))
print(f"  >>> max |odd cumulant| (z^1,z^3,z^5) = {float(odd_max):.1e} ~ 0: single Xi is even,")
print("      so the cubic/odd-arrow content vanishes for ONE L-function. The cubic lives")
print("      in the JOINT/cross structure (conductor lattice; c_2<0 via L(1/2,chi_3)).")

# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("FACT 3 -- on Z/6 the cubic couples conductor packets; the quadratic does not")
print("=" * 80)
from math import gcd
N = 6
def cond(c):
    return N // gcd(c, N)
packets = {}
for c in range(N):
    packets.setdefault(cond(c), []).append(c)
print(f"  conductor packets of Z/6: " + ", ".join(f"H_{d}={v}" for d, v in sorted(packets.items())))

# quadratic selection k+l=0 mod 6
quad = [(k, l) for k in range(N) for l in range(N) if (k + l) % N == 0]
quad_cross = sum(1 for k, l in quad if cond(k) != cond(l))
print(f"  quadratic pairs (k+l=0 mod 6): {len(quad)} total, {quad_cross} cross-packet "
      f"-> BLOCK-DIAGONAL (c pairs with -c, same conductor)")

# cubic selection k+l+m=0 mod 6
cub = [(k, l, m) for k in range(N) for l in range(N) for m in range(N) if (k + l + m) % N == 0]
cub_cross = sum(1 for k, l, m in cub if len({cond(k), cond(l), cond(m)}) > 1)
print(f"  cubic triples (k+l+m=0 mod 6): {len(cub)} total, {cub_cross} cross-packet "
      f"-> COUPLES distinct conductors (the Conductor Blind Spot, order 3)")
# show a few cross-packet cubic vertices
ex = [(k, l, m) for k, l, m in cub if len({cond(k), cond(l), cond(m)}) == 3][:4]
for k, l, m in ex:
    print(f"      e.g. ({k},{l},{m}): conductors ({cond(k)},{cond(l)},{cond(m)}) "
          f"= three different packets")
print(f"  >>> {cub_cross}/{len(cub)} cubic vertices cross conductor packets; the quadratic")
print("      has ZERO cross-coupling. The cubic is the order at which cross-prime / GUE")
print("      structure becomes visible -- and it carries a sign (chirality) the square lacks.")

print()
print("=" * 80)
print("READING")
print("=" * 80)
print("""  The cubic polar pair r=+-3 (sigma=2, -1) brackets the critical line (r=0, sigma=1/2)
  as functional-equation partners -- the order-3 version of r=+-2.  But the cubic is not
  a bigger square: it is the ODD / antisymmetric / ARROW part of the gauge corridor
  (K(b)-K(-b) = odd cumulants, led by kappa_3), the gauge-level twin of the de Branges
  arrow Xi'.  For a single even Xi the odd cumulants vanish (Fact 2), so the cubic
  content is intrinsically JOINT -- cross-character, cross-prime (Fact 3) -- which is
  exactly why [A3'] lives at primorial (multi-prime) moduli and carries the cluster
  c_2<0 via L(1/2,chi_3).  The quadratic (r=2, Bures, GBP) is block-diagonal and
  zero-blind; the cubic (r=3, chirality) couples packets and carries the GUE-3-point
  sign -- the teeth the quadratic lacks.

  What r=-3 suggests: the FE-partner of the cubic prime side, i.e. the RECIPROCAL /
  Moebius / inverse-cube dual (T8.4 Cor 2.7: negative gauge = reciprocal ledger).  [A3']
  -- the primorial-BV variance -- is the cubic-arrow positivity; r=-3 is its dual face
  (BV for mu vs BV for Lambda), and the chirality (sign of the cubic) is where the
  unconditional content (c_2<0) already lives.  The break-point is the cubic arrow's
  uniform sign-alignment = [A3']; r=+-3 says attack it as a polar pair across the line,
  on the JOINT structure, with the Moebius dual in hand.""")
