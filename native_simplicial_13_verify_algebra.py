"""
Native Simplicial Investigation, Script 13:
Verify the key algebraic computation S_A(c), S_B(c) at N=6.

S_A(c) = chi_c(0)^* + chi_c(2)^* + chi_c(3)^* + chi_c(4)^*   (non-units residues)
S_B(c) = chi_c(1)^* + chi_c(5)^*                              (units residues)

where chi_c(s) = e^{2 pi i c s / 6}.

The CORE THEOREM is:  S_A(c) + S_B(c) = 0 for every non-trivial c, by character orthogonality:
   sum_{s in Z/6} chi_c(s)^* = 0  for c != 0.
   So sum over non-units + sum over units = 0  ==>  S_A(c) = -S_B(c).

This is THE algebraic reason for the critical-line statement.
"""

import mpmath as mp

mp.mp.dps = 30


def chi(c, s, N=6):
    return mp.exp(2j * mp.pi * c * s / N)


def main():
    N = 6
    non_units = [0, 2, 3, 4]  # residues NOT coprime to 6
    units = [1, 5]            # residues coprime to 6

    print("=" * 70)
    print(f"Algebraic verification at N={N}:")
    print(f"  non-units residues = {non_units}")
    print(f"  units residues = {units}")
    print()
    print(f"  S_A(c) := sum over non-units of chi_c(s)^*")
    print(f"  S_B(c) := sum over units of chi_c(s)^*")
    print()
    print(f"  CLAIM: For c != 0, S_A(c) = -S_B(c) (character orthogonality).")
    print(f"  CONSEQUENCE: For limit ledger M(beta, c) = (S_A A + S_B B)/6,")
    print(f"               zero condition is A = B, i.e. exp{{-beta a}} = exp{{beta b}},")
    print(f"               which forces beta on the IMAGINARY AXIS.")
    print()

    print(f"{'c':>3}  {'S_A(c)':>30}  {'S_B(c)':>30}  {'S_A + S_B':>20}")
    print("-" * 90)
    for c in range(N):
        S_A = sum(mp.conj(chi(c, s)) for s in non_units)
        S_B = sum(mp.conj(chi(c, s)) for s in units)
        S_sum = S_A + S_B
        print(f"{c:>3}  ({mp.nstr(S_A.real, 8):>12} + {mp.nstr(S_A.imag, 6):>6} i)  "
              f"({mp.nstr(S_B.real, 8):>12} + {mp.nstr(S_B.imag, 6):>6} i)  "
              f"{mp.nstr(abs(S_sum), 6):>20}")

    print()
    print(f"For c=0: S_A = 4 (sum of 4 ones), S_B = 2 (sum of 2 ones), sum = 6 (= N).")
    print(f"For c != 0: |S_A + S_B| ~= 0 to machine precision, confirming S_A(c) = -S_B(c).")
    print()

    # Now verify the zero condition algebraically
    print("ZERO CONDITION at limit ledger y = (-a, b, -a, -a, -a, b), a=1/sqrt2, b=sqrt2:")
    a = 1 / mp.sqrt(2)
    b = mp.sqrt(2)
    print(f"   a + b = {mp.nstr(a + b, 12)} = 3/sqrt(2) = {mp.nstr(3/mp.sqrt(2), 12)}")
    print(f"   For c != 0: zero <=> S_A A + S_B B = 0")
    print(f"               <=> A = -(S_B/S_A) B = +1 * B  (since S_A = -S_B)")
    print(f"               <=> exp{{-beta a}} = exp{{beta b}}")
    print(f"               <=> exp{{beta(a+b)}} = 1")
    print(f"               <=> beta(a+b) in 2 pi i Z")
    print(f"               <=> beta = 2 pi i k / (a+b) = 2 pi i k sqrt(2) / 3")
    print(f"   Spacing:    2 pi sqrt(2) / 3 = {mp.nstr(2 * mp.pi * mp.sqrt(2) / 3, 14)}")
    print()
    print(f"   For c = 0: zero <=> 4 A + 2 B = 0")
    print(f"             <=> 2 A + B = 0")
    print(f"             <=> exp{{beta(a+b)}} = -2")
    print(f"             <=> beta(a+b) = log(2) + i pi (2k+1)")
    print(f"             <=> beta = (sqrt 2/3) * (log 2 + i pi (2k+1))")
    print(f"   Re(beta_k) = sqrt(2) log(2) / 3 = {mp.nstr(mp.sqrt(2) * mp.log(2) / 3, 14)}")
    print()

    # The structural fact, restated:
    print("STRUCTURAL FACT:")
    print("  The critical-line statement Re(beta) = 0 for non-trivial c at N=6")
    print("  reduces to the IDENTITY:  sum_{s in (Z/6)^*} chi_c(s) = -sum_{s notin (Z/6)^*} chi_c(s).")
    print("  This is character orthogonality + the limit ledger's two-valued structure.")
    print()
    print("  At general primorial N, the same identity holds (Mobius inversion):")
    print("    sum_{s in (Z/N)^*} chi_c(s) = mu(N) (Ramanujan sum c_N(1) for c=1)")
    print("    sum_{s in Z/N} chi_c(s) = 0 (c != 0)")
    print("    so sum_{s notin (Z/N)^*} chi_c(s) = -mu(N) (when c=1; analogous for other c).")
    print()
    print("  More generally: sum_{s in (Z/N)^*} chi_c(s) is a Ramanujan sum c_N(c),")
    print("  and sum_{s notin (Z/N)^*} chi_c(s) = -c_N(c).")
    print("  So |S_A(c)| = |S_B(c)| iff |c_N(c)| = |c_N(c)| ... trivially.")
    print("  AND S_A(c) = -S_B(c) <=> c != 0  (since the only difference is one is over the units).")


if __name__ == "__main__":
    main()
