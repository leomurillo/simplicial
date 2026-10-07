"""
Native Simplicial Investigation, Script 09:
Compute the Amari-Chentsov 3-tensor T at the primorial limit ledger,
decomposed in the character basis. Verify the selection rule a+b+c == 0 mod 6.

The 3-tensor is computed from the cumulant generating function. There are
two natural ways to read it:

Option (1): T2 §3 formula at the uniform u:
  T_{ijk}|_u = (1/N) delta_ij delta_ik - (1/N^2)(delta_ij + delta_ik + delta_jk) + 2/N^3

This is the cumulant tensor of the CATEGORICAL DISTRIBUTION at the uniform.
It's a universal object (doesn't depend on any ledger). Its character
decomposition gives the selection rule T(chi_a, chi_b, chi_c) = delta(a+b+c=0 mod N)
for non-trivial characters (T3 eq. (5)).

Option (2): The cumulant tensor of the LEDGER y, viewed as a random variable
on Z/N with uniform measure. This is the third cumulant of the apex generator
K_y(beta) and its Taylor jets.

The brief asks for the AMARI-CHENTSOV tensor at the uniform, decomposed in
character basis — that's Option (1), which is universal at fixed N.

Since the framework is at N=6, we compute T_{ijk}|_u directly and then
project onto character triples (a, b, c) to verify the selection rule.
"""

import mpmath as mp
import itertools
from math import gcd as _gcd

mp.mp.dps = 30

N = 6


def amari_chentsov_tensor_at_uniform():
    """T_{ijk}|_u = (1/N) delta_ij delta_ik - (1/N^2)(delta_ij + delta_ik + delta_jk) + 2/N^3."""
    T = [[[mp.mpf(0) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                val = mp.mpf(0)
                if i == j == k:
                    val += mp.mpf(1) / N
                if i == j:
                    val -= mp.mpf(1) / N**2
                if i == k:
                    val -= mp.mpf(1) / N**2
                if j == k:
                    val -= mp.mpf(1) / N**2
                val += mp.mpf(2) / N**3
                T[i][j][k] = val
    return T


def chi(c, s):
    """Character chi_c(s) = exp(2 pi i c s / N)."""
    return mp.exp(2j * mp.pi * c * s / N)


def T_chars(T, a, b, c):
    """T(chi_a, chi_b, chi_c) = sum_{ijk} T_{ijk} chi_a(i) chi_b(j) chi_c(k)."""
    s = mp.mpc(0)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                s += T[i][j][k] * chi(a, i) * chi(b, j) * chi(c, k)
    return s


def main():
    print("=" * 80)
    print(f"Amari-Chentsov tensor at uniform on N={N}, character-basis decomposition")
    print("=" * 80)
    T = amari_chentsov_tensor_at_uniform()

    # Print T tensor diagonal entries and an off-diagonal sample
    print(f"\nDirect tensor values at uniform (formula: T_iii = 1/N - 3/N^2 + 2/N^3, T_iij(i!=j) = -1/N^2 + 2/N^3, etc):")
    print(f"  T[0][0][0] = {mp.nstr(T[0][0][0], 8)}  (expected: 1/{N} - 3/{N**2} + 2/{N**3} = {mp.nstr(mp.mpf(1)/N - mp.mpf(3)/N**2 + mp.mpf(2)/N**3, 8)})")
    print(f"  T[0][0][1] = {mp.nstr(T[0][0][1], 8)}  (expected: -1/{N**2} + 2/{N**3} = {mp.nstr(-mp.mpf(1)/N**2 + mp.mpf(2)/N**3, 8)})")
    print(f"  T[0][1][2] = {mp.nstr(T[0][1][2], 8)}  (expected: 2/{N**3} = {mp.nstr(mp.mpf(2)/N**3, 8)})")

    print("\nSelection rule verification:")
    print(f"Enumerating ALL triples (a,b,c) in {{1,...,5}}^3 (non-trivial characters):")
    print(f"and reporting T(chi_a, chi_b, chi_c).")
    print()
    print(f"{'(a,b,c)':>10}  {'a+b+c':>5}  {'mod 6':>5}  {'satisfies?':>12}  {'T value (numeric)':>22}")
    print(f"(selection rule: a + b + c == 0 (mod {N}))")
    print("-" * 80)

    satisfied_triples = []
    not_satisfied_triples = []
    for a, b, c in itertools.product(range(1, 6), repeat=3):
        val = T_chars(T, a, b, c)
        sum_mod = (a + b + c) % N
        satisfies = (sum_mod == 0)
        if satisfies:
            satisfied_triples.append(((a, b, c), val))
        else:
            not_satisfied_triples.append(((a, b, c), val))

    print(f"\nTriples satisfying a+b+c == 0 (mod {N}) [{len(satisfied_triples)} total]:")
    for (abc, val) in satisfied_triples:
        a, b, c = abc
        ca = N // _gcd(a, N)
        cb = N // _gcd(b, N)
        cc = N // _gcd(c, N)
        print(f"  {abc}, conductors ({ca},{cb},{cc}), T = {mp.nstr(val.real, 10):>12} + {mp.nstr(val.imag, 6):>10} i")

    print(f"\nTriples NOT satisfying a+b+c == 0 (mod {N}) -- sample 10:")
    nonzero_count = 0
    for (abc, val) in not_satisfied_triples[:30]:
        if abs(val) > 1e-20:
            nonzero_count += 1
        a, b, c = abc
        print(f"  {abc}, (a+b+c) mod {N} = {(a+b+c)%N}, T = {mp.nstr(val.real, 10):>12} + {mp.nstr(val.imag, 6):>10} i  |T| = {mp.nstr(abs(val), 4)}")
    print(f"\n  Total non-selected triples in this sample with non-zero |T|: {nonzero_count}")

    # Count selected triples by conductor packets
    print("\nBreakdown of selected triples by conductor packets:")
    # H_2 = {3}, H_3 = {2, 4}, H_6 = {1, 5}
    packet = {1: "H_6", 5: "H_6", 2: "H_3", 4: "H_3", 3: "H_2"}
    breakdown = {}
    for (abc, val) in satisfied_triples:
        a, b, c = abc
        packets = tuple(sorted([packet[a], packet[b], packet[c]]))
        breakdown.setdefault(packets, []).append(abc)
    for packets, triples in sorted(breakdown.items()):
        print(f"   packets {packets}: {len(triples)} triples,  examples: {triples[:3]}")


if __name__ == "__main__":
    main()
