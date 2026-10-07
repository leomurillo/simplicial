"""
C9 -- The function-field apex lift: Weil's 1/2 as the sqrt(q) tilt.

The deep version of the C8 bridge. C5/C8 showed the ADDITIVE apex has unit-modulus
(character) coefficients -> zeros pile on Re=0 for trivial (unitarity) reasons; an
arithmetic ledger (units indicator) moves the line via unequal moduli phi vs N-phi,
but to no special place. Here we change the base ring Z/N -> F_q. The multiplicative-
apex coefficients become Gauss / Jacobi sums, whose modulus is sqrt(q) (NOT 1). The
Jacobi sums ARE the Frobenius eigenvalues alpha_i of the Fermat curve x^N+y^N+z^N=0,
and Weil's theorem |alpha_i| = sqrt(q) is the curve RH. Under T = q^{-s}:

      |alpha_i| = sqrt(q)   <=>   Re s = log|alpha_i| / log q = 1/2.

So the "1/2" is LITERALLY the 1/2 in sqrt(q): the tilt exponent of the coefficient
modulus. Equal-modulus 1 -> tilt 0 (additive, trivial line); modulus sqrt(q) ->
tilt 1/2 (function field, Weil's line). This is the program's worked, PROVABLE
RH-shaped instance (T7 7.6); the classical zeta target is the archimedean place
where this sqrt(q) purity must be manufactured rather than supplied by Frobenius.

Certified (deterministic, mpmath + exact point counts):
  P1  Gauss sums:  |g(chi^a)| = sqrt q, tilt = 1/2, all a.
  P2  Jacobi sums: |J(chi^a,chi^b)| = sqrt q (= Weil), tilt = 1/2, all 2g=(N-1)(N-2) pairs.
  P3  N=3 worked zeta: brute #E(F_q) -> a_q -> Frobenius alpha (|alpha|=sqrt q);
      alpha = -J(chi,chi); brute #E(F_{q^2}) = q^2+1-(alpha^2+conj^2); functional eq.
  P4  the tilt ladder: 0 (additive) vs arithmetic (units) vs 1/2 (Weil).
"""

import math
import numpy as np
import mpmath as mp
from ff_core import (is_prime, make_chars, gauss_sum, jacobi_sum,
                     fermat_count_Fp, fermat_count_Fq2)

mp.mp.dps = 30


def tilt(modulus, base):
    return mp.log(modulus) / mp.log(base)


def jacobi_pairs(N):
    return [(a, b) for a in range(1, N) for b in range(1, N) if (a + b) % N != 0]


# ---- P1: Gauss-sum sqrt(q) tilt -------------------------------------------
def test_gauss(cases):
    print("  P1 -- Gauss sums |g(chi^a)| = sqrt(q),  tilt = log|g|/log q = 1/2")
    ok = True
    for q, N in cases:
        g, dl = make_chars(q)
        worst_mod, worst_tilt = mp.mpf(0), mp.mpf(0)
        for a in range(1, N):
            gv = gauss_sum(q, dl, N, a)
            worst_mod = max(worst_mod, abs(abs(gv) - mp.sqrt(q)))
            worst_tilt = max(worst_tilt, abs(tilt(abs(gv), q) - mp.mpf(1) / 2))
        good = worst_mod < mp.mpf("1e-22") and worst_tilt < mp.mpf("1e-22")
        ok = ok and good
        print(f"     q={q:3d} N={N}: max||g|-sqrt q|={float(worst_mod):.1e} "
              f"max|tilt-1/2|={float(worst_tilt):.1e} {'OK' if good else 'FAIL'}")
    return ok


# ---- P2: Jacobi-sum sqrt(q) = Weil ----------------------------------------
def test_jacobi(cases):
    print("  P2 -- Jacobi sums |J| = sqrt(q) (Weil eigenvalue modulus), tilt = 1/2")
    ok = True
    for q, N in cases:
        g, dl = make_chars(q)
        pairs = jacobi_pairs(N)
        worst_mod = mp.mpf(0)
        for a, b in pairs:
            jv = jacobi_sum(q, dl, N, a, b)
            worst_mod = max(worst_mod, abs(abs(jv) - mp.sqrt(q)))
        twog = (N - 1) * (N - 2)
        good = worst_mod < mp.mpf("1e-22") and len(pairs) == twog
        ok = ok and good
        print(f"     q={q:3d} N={N}: #pairs={len(pairs)} (2g={twog}) "
              f"max||J|-sqrt q|={float(worst_mod):.1e} tilt=1/2 {'OK' if good else 'FAIL'}")
    return ok


# ---- P3: N=3 worked zeta function -----------------------------------------
def test_elliptic(qs, q2s):
    print("  P3 -- Fermat cubic (g=1): zeta -> |alpha|=sqrt q = Re s = 1/2; alpha = -J")
    ok = True
    for q in qs:
        g, dl = make_chars(q)
        c = fermat_count_Fp(q, 3)
        a_q = q + 1 - c
        alpha = np.roots([1.0, -a_q, q])             # X^2 - a X + q  (Frobenius eigenvalues)
        mod_ok = all(abs(abs(al) - math.sqrt(q)) < 1e-9 for al in alpha)
        re_s = [math.log(abs(al)) / math.log(q) for al in alpha]   # should all be 1/2
        re_ok = all(abs(r - 0.5) < 1e-9 for r in re_s)
        # alpha = -J(chi,chi):
        J = complex(jacobi_sum(q, dl, 3, 1, 1))
        match = min(abs(al - (-J)) for al in alpha)
        # functional eq: eigenvalue set closed under alpha -> q/conj(alpha) (here just |.|=sqrt q)
        fe_ok = abs(alpha[0] * alpha[1] - q) < 1e-9    # product = q
        extra = ""
        if q in q2s:
            cF2 = fermat_count_Fq2(q, 3)
            pred = q ** 2 + 1 - (alpha[0] ** 2 + alpha[1] ** 2).real
            f2_ok = abs(cF2 - pred) < 1e-6
            extra = f" | #E(F_{q*q})brute={cF2}=pred({pred:.0f}):{f2_ok}"
        else:
            f2_ok = True
        good = mod_ok and re_ok and match < 1e-9 and fe_ok and f2_ok
        ok = ok and good
        print(f"     q={q:3d}: a_q={a_q:+d} |alpha|={abs(alpha[0]):.4f}=sqrt q "
              f"Re s={re_s[0]:.6f} alpha=-J:{match:.1e}{extra} {'OK' if good else 'FAIL'}")
    return ok


# ---- P4: the tilt ladder ---------------------------------------------------
def test_ladder():
    print("  P4 -- the tilt ladder: line position = log|coeff modulus| / log(base)")
    q, N = 13, 3
    g, dl = make_chars(q)
    # rung 1: additive character coefficient, modulus 1
    t_add = float(tilt(mp.mpf(1), q))
    # rung 2: units-indicator arithmetic weights phi vs N-phi (C8), an arithmetic value
    Nu = 30; phi = sum(1 for s in range(Nu) if math.gcd(s, Nu) == 1)
    t_units = float(mp.log(mp.mpf(Nu - phi) / phi))        # the C8 off-line displacement (beta units)
    # rung 3: function-field Gauss/Jacobi, modulus sqrt(q)
    t_ff = float(tilt(abs(jacobi_sum(q, dl, N, 1, 1)), q))
    print(f"     additive (|coeff|=1)        -> tilt = {t_add:.4f}  (trivial line Re=0; C2/C5)")
    print(f"     units-indicator (phi-weights) -> arith displacement {t_units:.4f} (C8; not special)")
    print(f"     function field (|coeff|=sqrt q) -> tilt = {t_ff:.6f}  (Weil's 1/2; PROVABLE)")
    good = abs(t_add) < 1e-12 and abs(t_ff - 0.5) < 1e-12
    print(f"     => the '1/2' is exactly log(sqrt q)/log q {'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 78)
    print("C9 -- function-field apex lift: Weil's 1/2 = the sqrt(q) coefficient tilt")
    print("=" * 78)
    cases = [(7, 3), (13, 3), (19, 3), (31, 5), (61, 5), (43, 7)]
    # all q here are 1 mod N
    for q, N in cases:
        assert is_prime(q) and (q - 1) % N == 0, (q, N)
    ok = True
    ok = test_gauss(cases) and ok
    ok = test_jacobi(cases) and ok
    ok = test_elliptic([7, 13, 19, 31, 61], q2s=[7, 13]) and ok
    ok = test_ladder() and ok
    print("-" * 78)
    print("C9:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
