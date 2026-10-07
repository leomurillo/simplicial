r"""Exact check of P5 פoverlap (§4.3): is the real overlap K_N ∩ Q(zeta_N) trivial at N=12?

P5 §4.3 claims: "at N=12 the only odd prime 3≡3 (mod 4) gives the imaginary sqrt(-3) and the
real overlap is trivial." This script tests that exactly.

The subtlety P5 misses: the conductor-p Gauss sum sqrt(p*) is imaginary for p≡3 mod 4, but the
REAL radical sqrt(p) is a DIFFERENT element, with conductor 4p (not p) for p≡3 mod 4, and it
enters Q(zeta_N) whenever 4p | N. Correct criterion:

    sqrt(p) in Q(zeta_N)  <=>  cond(Q(sqrt p)) | N,
    cond = 8 (p=2),  p (p≡1 mod 4),  4p (p≡3 mod 4).

At N=12: p=3≡3, cond(Q(sqrt3)) = 12, and 12 | 12, so sqrt(3) in Q(zeta_12). The real overlap
is Q(sqrt3), NOT trivial. (sqrt3 = zeta_12 + zeta_12^{-1}, the real quadratic subfield
Q(zeta_12)^+; it arises as i * sqrt(-3), the product of the 4-part and the 3-part.)

No floating point in any decision; the cyclotomic check is exact integer polynomial arithmetic.
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def primes_upto(N):
    return [p for p in range(2, N + 1) if is_prime(p)]


def cond_sqrt(p):
    if p == 2:
        return 8
    return p if p % 4 == 1 else 4 * p


print(__doc__)
print("Real single-prime radicals genuinely in the overlap  K_N ∩ Q(zeta_N):")
print("  N  | sqrt(p) with cond(Q(sqrt p)) | N      | P5 §4.3 said")
print("  ---+---------------------------------------+------------------")
for N, claim in [(5, "sqrt5"), (8, "sqrt2"), (12, "TRIVIAL"), (15, "sqrt5"), (30, "sqrt5")]:
    ov = [p for p in primes_upto(N) if N % cond_sqrt(p) == 0]
    radicals = ["sqrt%d" % p for p in ov]
    print("  %2d | %-37s | %s" % (N, str(radicals), claim))

print()
print("Exact cyclotomic confirmation that sqrt(3) in Q(zeta_12):")


def reduce4(p):
    """Reduce an integer polynomial (coeffs low->high) modulo Phi_12 = x^4 - x^2 + 1,
    using x^4 = x^2 - 1.  Returns the 4 coefficients of the residue."""
    p = list(p)
    i = len(p) - 1
    while i >= 4:
        lead = p[i]
        if lead:
            p[i] = 0
            p[i - 2] += lead     # x^i = x^{i-2} - x^{i-4}
            p[i - 4] -= lead
        i -= 1
    return (p + [0, 0, 0, 0])[:4]


def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def powx(k):
    p = [0] * (k + 1)
    p[k] = 1
    return reduce4(p)


eta = [a + b for a, b in zip(powx(1), powx(11))]      # zeta_12 + zeta_12^{-1}
eta2 = reduce4(mul(eta, eta))
print("  eta = zeta_12 + zeta_12^{-1} in basis (1, x, x^2, x^3) = %s   (= 2x - x^3)" % eta)
print("  eta^2 mod Phi_12 = %s" % eta2)
print("  => eta^2 = 3 exactly: %s   hence sqrt(3) in Q(zeta_12), overlap NOT trivial."
      % (eta2 == [3, 0, 0, 0]))
print()
print("VERDICT: P5 §4.3's 'real overlap trivial at N=12' is FALSE; the overlap is Q(sqrt3).")
print("         The 'fusion real exactly for p≡1 mod 4' claim is incomplete: p≡3 primes")
print("         fuse real too, when 4p | N (here 4*3=12 | 12).")
