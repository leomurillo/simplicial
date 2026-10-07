"""probe_quanta_nclass_chiral.py -- the n-ic generalization of the quanta object's shape
invariant, and the weld of index 3 to the chiral channel chi_3 = Q(zeta_3) = Q(sqrt(-3)).

THE GENERALIZATION. The quanta object's shape invariant at index n is the prime-exponent
vector MOD n: [N]_n in (+)_p (Z/n). n=2 recovers the square class (T4 sec 6). Extraction
N^(1/n) = s * M^(1/n) reduces exponents mod n (M n-th-power-free). The Galois closure of
Q(N^(1/n)) is Kummer: Q(zeta_n, N^(1/n)); the cyclotomic field zeta_n is summoned by the
index, and for prime index p its quadratic subfield is Q(sqrt(p*)), p* = (-1)^((p-1)/2) p,
the field of the quadratic character chi_p.

THE CHIRAL WELD (the point). index 2 -> zeta_2 = -1 -> the archimedean sign (reflection,
visible iff n even). index 3 -> zeta_3 -> Q(sqrt(-3)) = the chi_3 chiral field (c_2 < 0 via
L(1/2, chi_3); the RH program's order-3 channel). The cube root is the FIRST chiral radical.

PRE-REGISTERED (GPD):
  N1 (recovery + extraction mod n, exact):
     nclass(x,2) prime-part == square class; extraction: cbrt(54)=3 cbrt2, cbrt(250)=5 cbrt2,
     cbrt(162)=3 cbrt6, sqrt(8)=2 sqrt2; classes add mod n under product (cbrt2 * cbrt4 = 2).
     FALSIFIER: any mismatch (exact).
  N2 (archimedean visible iff n even): sign is a nontrivial class for even n, trivial for odd
     (cbrt(-8) = -2 rational; sqrt(-1) = i is a genuine generator). Demonstrated.
  N3 (the chiral discriminant -- the headline): disc(x^3 - 2) = -108, square class = [-3];
     so sqrt(-3) lies in the splitting field of every index-3 radical. zeta_3 = (-1+sqrt(-3))/2
     (verify (2 zeta_3 + 1)^2 = -3). Galois closure Q(cbrt2, zeta_3) has degree 6 = |S_3|.
     FALSIFIER: disc square class != [-3], or (2 zeta_3+1)^2 != -3.
  N4 (the index -> character ladder, Gauss sums): for p in {3,5,7}, the quadratic Gauss sum
     g_p^2 = p* = (-1)^((p-1)/2) p (verify to 1e-40); Q(sqrt(p*)) = quadratic subfield of
     Q(zeta_p) = field of chi_p. p=3 -> sqrt(-3) = chi_3 (CHIRAL); p=5 -> sqrt5; p=7 -> sqrt(-7).
     FALSIFIER: g_p^2 != p*.

Exact (sympy) + high-precision (mpmath) for the Gauss sums. Deterministic, instant.
"""
import sys
from sympy import (Rational, Integer, factorint, discriminant, symbols, legendre_symbol,
                   sqrt, I, simplify, expand)
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
x = symbols("x")


# ---------------- the n-ic class and extraction ----------------
def nclass(v, n):
    """shape invariant at index n: prime exponents mod n, + sign (order 2, live iff n even)."""
    v = Rational(v)
    sign = 1 if v < 0 else 0
    v = abs(v)
    cls = {}
    for p, e in factorint(v.p).items():
        cls[p] = (cls.get(p, 0) + e) % n
    for p, e in factorint(v.q).items():
        cls[p] = (cls.get(p, 0) + e) % n
    cls = {p: e for p, e in cls.items() if e}
    return cls, (sign if n % 2 == 0 else 0)


def extract_n(N, n):
    """N^(1/n) = s * M^(1/n), M n-th-power-free (exponents reduced mod n)."""
    N = Rational(N)
    assert N.q == 1 and N > 0
    s, M = 1, 1
    for p, e in factorint(N.p).items():
        s *= p ** (e // n)
        M *= p ** (e % n)
    return Rational(s), Integer(M)


def cadd(c1, c2, n):
    """add two n-ic classes (vector add mod n)."""
    cl1, s1 = c1
    cl2, s2 = c2
    keys = set(cl1) | set(cl2)
    out = {p: (cl1.get(p, 0) + cl2.get(p, 0)) % n for p in keys}
    out = {p: e for p, e in out.items() if e}
    return out, (s1 + s2) % 2 if n % 2 == 0 else 0


# ---------------- N1: recovery + extraction mod n ----------------
print("== N1: n-ic class recovery + extraction mod n (exact) ==")
# recover square class at n=2
def sqclass_primepart(v):
    v = Rational(v); v = abs(v); cls = {}
    for p, e in factorint(v.p).items(): cls[p] = (cls.get(p,0)+e)%2
    for p, e in factorint(v.q).items(): cls[p] = (cls.get(p,0)+e)%2
    return {p:e for p,e in cls.items() if e}
rec = all(nclass(v, 2)[0] == sqclass_primepart(v) for v in [8, 12, Rational(19,100), 50, 7])
print(f"   nclass(.,2) prime-part == square class: {rec}")

ex = {
    "cbrt(54)":  (extract_n(54, 3),  (Integer(3), Integer(2))),   # 54=2*3^3
    "cbrt(250)": (extract_n(250, 3), (Integer(5), Integer(2))),   # 250=2*5^3
    "cbrt(162)": (extract_n(162, 3), (Integer(3), Integer(6))),   # 162=2*3^4 -> 3*cbrt(2*3)
    "sqrt(8)":   (extract_n(8, 2),   (Integer(2), Integer(2))),
}
ex_ok = True
for name, (got, want) in ex.items():
    ok = (got == want)
    ex_ok &= ok
    print(f"   {name}: s={got[0]}, M={got[1]}  (want s={want[0]}, M={want[1]}): {ok}")

# composition: cbrt2 * cbrt4 = cbrt8 = 2 (classes add mod 3 -> trivial)
c_prod = cadd(nclass(2, 3), nclass(4, 3), 3)
comp_ok = (c_prod == ({}, 0))   # 2^1 * 2^2 = 2^3 -> exp 0 mod 3 -> rational
print(f"   cbrt2 * cbrt4 = cbrt8: class = {c_prod[0]} (trivial -> rational 2): {comp_ok}")
N1 = rec and ex_ok and comp_ok
print(f"   N1: {'PASS' if N1 else 'FAIL'}")


# ---------------- N2: archimedean visible iff n even ----------------
print("\n== N2: the archimedean place (sign) is in the class iff n is even ==")
neg_sq = nclass(-1, 2)    # sqrt(-1) = i, a genuine generator: sign live
neg_cb = nclass(-8, 3)    # cbrt(-8) = -2, rational: sign trivial
s8, M8 = extract_n(8, 3)
print(f"   n=2: [-1] = {neg_sq}  (sign live -> sqrt(-1)=i is a generator)")
print(f"   n=3: [-8] prime-part trivial, sign component = {neg_cb[1]} (cbrt(-8) = -2, real)")
N2 = (neg_sq[1] == 1) and (neg_cb[1] == 0)
print(f"   N2: archimedean visible iff n even: {'PASS' if N2 else 'FAIL'}")


# ---------------- N3: the chiral discriminant (headline) ----------------
print("\n== N3: index 3 summons sqrt(-3) = Q(zeta_3) = the chi_3 chiral field ==")
disc3 = discriminant(x**3 - 2, x)
dc = nclass(disc3, 2)     # square class of the discriminant
print(f"   disc(x^3 - 2) = {disc3};  square class = (primes {dc[0]}, sign {dc[1]})  -> [-3]")
chiral_class = (dc[0] == {3: 1} and dc[1] == 1)   # [-3] = {sign, prime 3}

# zeta_3 = (-1 + sqrt(-3))/2 : verify (2*zeta_3 + 1)^2 = -3
mp.mp.dps = 50
zeta3 = mp.e ** (2j * mp.pi / 3)
val = (2 * zeta3 + 1) ** 2
z3_ok = abs(val - (-3)) < mp.mpf(10) ** (-40)
print(f"   zeta_3 = exp(2pi i/3): (2 zeta_3 + 1)^2 = {complex(val):.6f}  (= -3: {z3_ok})")

# Galois closure degree: Q(cbrt2) deg 3 (not normal) -> closure Q(cbrt2, zeta_3) deg 6 = |S_3|
deg_cbrt2 = 3        # x^3-2 irreducible over Q
deg_closure = 6      # adjoin zeta_3 (deg 2): 3*2 = 6 = |S_3|
print(f"   Q(cbrt2) deg {deg_cbrt2} (not normal); Galois closure Q(cbrt2, zeta_3) deg {deg_closure} = |S_3|")
N3 = chiral_class and z3_ok
print(f"   N3: the cube root's splitting field carries sqrt(-3) = chi_3: {'PASS' if N3 else 'FAIL'}")


# ---------------- N4: the index -> character ladder (Gauss sums) ----------------
print("\n== N4: index p -> zeta_p -> Q(sqrt(p*)) = chi_p  (quadratic Gauss sum g_p^2 = p*) ==")
mp.mp.dps = 50
N4 = True
rows = []
for p in [3, 5, 7]:
    g = mp.fsum(legendre_symbol(k, p) * mp.e ** (2j * mp.pi * k / p) for k in range(1, p))
    pstar = ((-1) ** ((p - 1) // 2)) * p
    err = abs(g ** 2 - pstar)
    ok = err < mp.mpf(10) ** (-40)
    N4 &= ok
    fld = f"Q(sqrt({pstar}))"
    tag = "  <-- CHIRAL (the RH program's order-3 channel)" if p == 3 else ""
    rows.append((p, pstar, fld, float(err), ok, tag))
    print(f"   p={p}: p* = {pstar:+d}; g_p^2 = {complex(g**2):.4f}; field {fld}{tag}")
print(f"   (p=2 is the boundary: zeta_2 = -1 -> the sign/reflection; zeta_4 = i -> Q(i))")
print(f"   N4: all Gauss sums g_p^2 = p* to 1e-40: {'PASS' if N4 else 'FAIL'}")


print("\n== the ladder, assembled ==")
print("   index 2  ->  zeta_2 = -1   ->  archimedean sign / reflection   (the +/- of T4)")
print("   index 3  ->  zeta_3        ->  Q(sqrt(-3)) = chi_3   = the CHIRAL channel (c_2<0)")
print("   index 5  ->  zeta_5        ->  Q(sqrt(5))  = chi_5")
print("   index 7  ->  zeta_7        ->  Q(sqrt(-7)) = chi_7")
print("   The quanta object's INDEX is the channel selector; index 3 is the first chiral radical,")
print("   the same Q(sqrt(-3)) = Q(zeta_3) the RH cubic strike lives on.")

print("\nRESULT: " + ("GREEN -- n-ic class generalizes the square class; index 3 lands on "
                      "Q(zeta_3)=Q(sqrt(-3))=chi_3; the cube root is the first chiral radical"
                      if (N1 and N2 and N3 and N4) else "PARTIAL -- see blocks"))
