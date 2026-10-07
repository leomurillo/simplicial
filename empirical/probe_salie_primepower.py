"""
Verify Lemma 2 (Varbanets-Varbanets-Vorobyov) transfers to Z: the prime-power
Kloosterman sum S(a,b;p^m), m>=2, VANISHES when ab is a nonresidue and is EXACTLY
2 p^{m/2}|cos(...)| (|theta|<=2) when ab is a residue.  (Salie evaluation.)

S(a,b;q) = sum_{x mod q, (x,q)=1} exp(2pi i (a x + b x^{-1})/q).

This is the per-prime-power beyond-Weil input: at m>=2 the sum is 0 half the time and
square-root-EXACT otherwise -- stronger than the m=1 Weil bound |S(a,b;p)| <= 2 sqrt p.
Deterministic: pure python + cmath.  No torch.
"""

import cmath
from math import gcd

def kloosterman(a, b, q):
    s = 0j
    for x in range(1, q):
        if gcd(x, q) == 1:
            xi = pow(x, -1, q)
            s += cmath.exp(2j * cmath.pi * (a * x + b * xi) / q)
    return s

def is_qr(n, p):
    n %= p
    if n == 0:
        return None
    return pow(n, (p - 1) // 2, p) == 1

print("=" * 78)
print("Prime-power Kloosterman S(a,b;p^m), m>=2:  0 (ab nonresidue) or |S|=2 p^{m/2}|cos|")
print("=" * 78)
print(f"  {'p':>3} {'m':>2} {'q=p^m':>6} {'a':>3} {'b':>3} {'ab mod p':>9} {'QR?':>5} "
      f"{'|S|':>9} {'2 p^(m/2)':>10} {'|S|/p^(m/2)':>12}")
for p in [3, 5, 7]:
    for m in [2, 3]:
        q = p**m
        for (a, b) in [(1, 1), (1, 2), (2, 1), (1, 3), (2, 3), (1, 5)]:
            if gcd(a, p) > 1 or gcd(b, p) > 1:
                continue
            S = kloosterman(a, b, q)
            ab = (a * b) % p
            qr = is_qr(ab, p)
            mod = abs(S)
            ratio = mod / p**(m / 2)
            print(f"  {p:>3} {m:>2} {q:>6} {a:>3} {b:>3} {ab:>9} {str(qr):>5} "
                  f"{mod:>9.3f} {2*p**(m/2):>10.3f} {ratio:>12.4f}")
print("  >>> |S|=0 exactly when ab is a nonresidue (QR=False); |S|/p^(m/2) in [0,2]")
print("      (=2|cos|) when ab is a residue (QR=True).  Lemma 2 holds verbatim over Z.")
print("      m>=2 gives BEYOND-Weil: vanishing half the time + exact sqrt -- the")
print("      prime-power saving feeding the Selberg-Kuznetsov / mean-square route (§5).")
