import sys
sys.stdout.reconfigure(encoding='utf-8')

import sympy as sp
from sympy.utilities.iterables import multiset_partitions

p = sp.symbols('p')

# ---------------------------------------------------------------------------
# Per-prime "moment" factor on squarefree support (all shifts distinct mod p):
#   M_s(p) = (1 - s/p) / (1 - 1/p)^s ,  M_1 = 1.
# ---------------------------------------------------------------------------
def M(s):
    if s == 1:
        return sp.Integer(1)
    return (1 - sp.Rational(1) * s / p) / (1 - sp.Rational(1) / p) ** s


def fact(n):
    return sp.factorial(n)


# ---------------------------------------------------------------------------
# Connected n-tuple cumulant via Mobius inversion on the partition lattice:
#   C_n(p) = sum_{pi in partitions of {1..n}} (-1)^{|pi|-1} (|pi|-1)! * prod_B M_{|B|}
# ---------------------------------------------------------------------------
def C(n):
    total = sp.Integer(0)
    elements = list(range(1, n + 1))
    for part in multiset_partitions(elements):
        k = len(part)                       # number of blocks |pi|
        coeff = (-1) ** (k - 1) * fact(k - 1)
        prod = sp.Integer(1)
        for block in part:
            prod *= M(len(block))
        total += coeff * prod
    return sp.cancel(sp.simplify(total))


def classify(expr, order):
    """Return (holds, c, exponent) describing whether expr = c/(p-1)^order with c const."""
    expr = sp.cancel(expr)
    num, den = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    den = sp.expand(den)
    # Multiply by (p-1)^order and see if it is free of p.
    test = sp.cancel(expr * (p - 1) ** order)
    test_s = sp.simplify(test)
    is_const = (test_s.free_symbols == set())
    return is_const, test_s, sp.factor(den)


def main():
    print("=" * 70)
    print("Hardy-Littlewood k-tuple singular series: connected cumulant test")
    print("=" * 70)
    print()
    print("Per-prime moment factor (squarefree support):")
    print("  M_s(p) = (1 - s/p) / (1 - 1/p)^s ,  M_1 = 1")
    for s in range(1, 5):
        print(f"  M_{s}(p) = {sp.simplify(M(s))}")
    print()

    # --- Order 2 anchor ---------------------------------------------------
    C2 = C(2)
    print("-" * 70)
    print("ORDER 2 (anchor):")
    print(f"  C_2(p)            = {C2}")
    target2 = -1 / (p - 1) ** 2
    anchor_ok = sp.simplify(C2 - target2) == 0
    print(f"  expected -1/(p-1)^2 = {sp.cancel(target2)}")
    print(f"  C_2 == -1/(p-1)^2 ?  {anchor_ok}")
    if not anchor_ok:
        print("  *** ANCHOR FAILED -- M_s or partition formula is wrong. Aborting. ***")
        print("VERDICT: FAIL (anchor broken)")
        print("PASS/FAIL (computation determined): FAIL")
        return
    c2_const = sp.simplify(C2 * (p - 1) ** 2)
    print(f"  c_2 = C_2*(p-1)^2 = {c2_const}")
    print()

    # --- Order 3 ----------------------------------------------------------
    C3 = C(3)
    print("-" * 70)
    print("ORDER 3:")
    print(f"  C_3(p)            = {C3}")
    holds3, test3, den3 = classify(C3, 3)
    print(f"  denominator factor = {den3}")
    print(f"  C_3*(p-1)^3        = {test3}   (const? {holds3})")
    if holds3:
        print(f"  => C_3 = {test3}/(p-1)^3 ,  c_3 = {test3}")
    print()

    # --- Order 4 ----------------------------------------------------------
    C4 = C(4)
    print("-" * 70)
    print("ORDER 4 (the test):")
    print(f"  C_4(p)            = {C4}")
    holds4, test4, den4 = classify(C4, 4)
    print(f"  denominator factor = {den4}")
    print(f"  C_4*(p-1)^4        = {test4}   (const? {holds4})")
    print()

    # --- Verdict ----------------------------------------------------------
    print("=" * 70)
    if holds4:
        verdict = "HOLD"
        print("VERDICT: HOLD -- C_4 = c_4/(p-1)^4 with c_4 constant.")
        print(f"  c_2 = {c2_const}")
        if holds3:
            print(f"  c_3 = {test3}")
        else:
            print("  c_3 = (C_3 is NOT of the form c_3/(p-1)^3 -- see above)")
        print(f"  c_4 = {test4}")
    else:
        verdict = "FAIL"
        print("VERDICT: FAIL -- C_4 is NOT of the form c_4/(p-1)^4.")
        print("  The clean 1/phi(p)^n totient-power identity does NOT extend to order 4.")
        print(f"  Actual simplified C_4(p) = {C4}")
        print(f"  Denominator factors as   = {den4}")
        print(f"  c_2 = {c2_const} (order-2 identity holds)")
        print(f"  C_3(p) = {C3}  (holds as c_3/(p-1)^3? {holds3})")
    print()
    print(f"VERDICT: {verdict}")
    print("PASS/FAIL (computation determined): PASS")
    print("=" * 70)


if __name__ == "__main__":
    main()
