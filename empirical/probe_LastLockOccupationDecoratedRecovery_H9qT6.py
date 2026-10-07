"""Probe the occupation-decorated Hayes-Mobius recovery theorem.

The script has two parts:
1. Show aliasing in compressed finite CRT labels.
2. Show exact von Mangoldt recovery in the occupation-decorated lift.
"""

from collections import defaultdict
import itertools
import math


def add_vec(a, b, mod=None):
    if mod is None:
        return tuple(x + y for x, y in zip(a, b))
    return tuple((x + y) % m for x, y, m in zip(a, b, mod))


def basis(i, n):
    return tuple(1 if j == i else 0 for j in range(n))


def enumerate_words(primes, degree):
    n = len(primes)
    gens = [basis(i, n) for i in range(n)]
    out = []
    for word in itertools.product(range(n), repeat=degree):
        occ = tuple(word.count(i) for i in range(n))
        label = tuple(occ[i] % primes[i] for i in range(n))
        support_size = sum(1 for x in occ if x)
        out.append((word, occ, label, support_size))
    return out


def alias_report(primes, degree):
    buckets = defaultdict(list)
    for word, occ, label, support_size in enumerate_words(primes, degree):
        buckets[label].append((occ, support_size))

    collisions = []
    for label, items in buckets.items():
        unique_items = sorted(set(items))
        has_single = any(s == 1 for _, s in unique_items)
        has_mixed = any(s > 1 for _, s in unique_items)
        if has_single and has_mixed:
            collisions.append((label, unique_items[:8], len(unique_items)))
    return collisions


def vm_coefficients(primes, s, kmax):
    recovered = {}
    for i, p in enumerate(primes):
        for r in range(1, kmax + 1):
            occ = tuple(r if j == i else 0 for j in range(len(primes)))
            # D_s (p^{-rs}/r) = log(p) p^{-rs}
            recovered[occ] = math.log(p) * p ** (-r * s)
    return recovered


def main():
    primes = [2, 3, 5]
    print("Compressed CRT aliasing check")
    print(f"local prime moduli: {primes}")
    for degree in range(2, 8):
        collisions = alias_report(primes, degree)
        print(f"degree={degree}: labels with single/mixed aliasing = {len(collisions)}")
        if collisions:
            label, examples, count = collisions[0]
            print(f"  example label={label}, distinct occupations={count}, examples={examples}")

    print()
    print("Occupation-decorated VM recovery")
    s = 2.0 + 0.3j
    kmax = 6
    coeffs = vm_coefficients(primes, s, kmax)
    max_err = 0.0
    for i, p in enumerate(primes):
        for r in range(1, kmax + 1):
            occ = tuple(r if j == i else 0 for j in range(len(primes)))
            expected = math.log(p) * p ** (-r * s)
            max_err = max(max_err, abs(coeffs[occ] - expected))
    print(f"s={s}, kmax={kmax}, max coefficient error={max_err:.3e}")
    print("sample coefficients:")
    for occ in sorted(coeffs)[:8]:
        val = coeffs[occ]
        print(f"  occ={occ}: {val.real: .12e}{val.imag:+.12e}j")


if __name__ == "__main__":
    main()
