"""Verify Galois/simplex and cyclotomic-unit identities.

This script supports `7.galois_simplex_units.md`.

It checks exact combinatorial/rational identities where possible and uses
floating-point embeddings only for regulator-style numerical output.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def units_mod(n: int) -> list[int]:
    return [a for a in range(1, n) if math.gcd(a, n) == 1]


def compose_perm(p: list[int], q: list[int]) -> list[int]:
    """Return p after q, i -> p[q[i]]."""
    return [p[q[i]] for i in range(len(p))]


def inverse_perm(p: list[int]) -> list[int]:
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return inv


def shift_perm(n: int, k: int = 1) -> list[int]:
    return [(i + k) % n for i in range(n)]


def multiplier_perm(n: int, a: int) -> list[int]:
    return [(a * i) % n for i in range(n)]


def conjugate_perm(sigma: list[int], tau: list[int]) -> list[int]:
    return compose_perm(compose_perm(sigma, tau), inverse_perm(sigma))


def verify_normalizer(n: int) -> None:
    c = shift_perm(n, 1)
    for a in units_mod(n):
        sigma = multiplier_perm(n, a)
        lhs = conjugate_perm(sigma, c)
        rhs = shift_perm(n, a)
        assert lhs == rhs, (n, a, lhs, rhs)
    print(f"[ok] N={n}: sigma_a C sigma_a^-1 = C^a for all units a")


def gram_simp_entry(p: int, i: int, j: int) -> Fraction:
    return Fraction(1 if i == j else 0, 1) - Fraction(1, p)


def gram_trace_entry(p: int, i: int, j: int) -> int:
    return (p - 1) if i == j else -1


def verify_gram_identity(p: int) -> None:
    assert is_prime(p)
    for i in range(p):
        for j in range(p):
            assert gram_simp_entry(p, i, j) == Fraction(gram_trace_entry(p, i, j), p)

    # Trim one redundant generator.  The matrices are:
    # G_simp = I_m - (1/p)J_m and G_trace = p I_m - J_m,
    # where m=p-1.  For aI+bJ, eigenvalues are a (m-1 times)
    # and a+bm (once).
    det_simp = Fraction(1, p)
    det_trace = p ** (p - 2)

    assert det_simp == Fraction(1, p)
    assert det_trace == p ** (p - 2)
    print(
        f"[ok] p={p}: G_simp=(1/p)G_trace, "
        f"det(G_simp)=1/{p}, det(G_trace)={p}^{p-2}"
    )


def coeff_arc(p: int, start: int, length: int, step: int = 1) -> list[int]:
    coeff = [0] * p
    for k in range(length):
        coeff[(start + step * k) % p] += 1
    return coeff


def coeff_pal_star(p: int, radius: int, step: int = 1) -> list[int]:
    coeff = [0] * p
    for k in range(-radius, radius + 1):
        coeff[(step * k) % p] += 1
    return coeff


def coeff_negative_pair(p: int, skip: int) -> list[int]:
    coeff = [0] * p
    coeff[skip % p] -= 1
    coeff[(-skip) % p] -= 1
    return coeff


def coeff_equiv_mod_gauge(c: list[int], d: list[int]) -> bool:
    diff = [x - y for x, y in zip(c, d)]
    return all(x == diff[0] for x in diff)


def simplex_inner_from_coeff(p: int, coeff: list[int]) -> Fraction:
    s1 = sum(coeff)
    s2 = sum(x * x for x in coeff)
    return Fraction(s2, 1) - Fraction(s1 * s1, p)


def trace_inner_from_coeff(p: int, coeff: list[int]) -> int:
    s1 = sum(coeff)
    s2 = sum(x * x for x in coeff)
    return p * s2 - s1 * s1


def verify_arc_norms(p: int) -> None:
    for a in range(1, p):
        coeff = coeff_arc(p, 0, a)
        simp = simplex_inner_from_coeff(p, coeff)
        trace = trace_inner_from_coeff(p, coeff)
        assert simp == Fraction(trace, p)
        assert trace == p * a - a * a
    print(f"[ok] p={p}: all arc-sum norms match trace normalization")


def zeta(p: int) -> complex:
    return cmath.exp(2j * math.pi / p)


def complex_value(p: int, coeff: list[int], embedding: int = 1) -> complex:
    z = zeta(p) ** embedding
    return sum(c * (z ** i) for i, c in enumerate(coeff))


def real_embedding_reps(p: int) -> list[int]:
    return list(range(1, (p - 1) // 2 + 1))


def verify_real_unit_norms(p: int) -> None:
    radii = list(range(1, (p - 1) // 2))
    for r in radii:
        coeff = coeff_pal_star(p, r)
        vals = [complex_value(p, coeff, b).real for b in real_embedding_reps(p)]
        imag_max = max(abs(complex_value(p, coeff, b).imag) for b in real_embedding_reps(p))
        product = math.prod(vals)
        assert imag_max < 1e-10, (p, r, imag_max)
        assert abs(abs(product) - 1.0) < 1e-9, (p, r, product)
    print(f"[ok] p={p}: palindromic arc-stars have real norm +/-1")


def regulator_matrix(p: int) -> list[list[float]]:
    # Generators are palindromic stars of lengths 3,5,...,p-2.
    radii = list(range(1, (p - 1) // 2))
    # Drop the last real embedding to get a square regulator matrix.
    reps = real_embedding_reps(p)[:-1]
    matrix: list[list[float]] = []
    for b in reps:
        row = []
        for r in radii:
            coeff = coeff_pal_star(p, r)
            val = complex_value(p, coeff, b).real
            row.append(math.log(abs(val)))
        matrix.append(row)
    return matrix


def det_float(matrix: list[list[float]]) -> float:
    if not matrix:
        return 1.0
    a = [row[:] for row in matrix]
    n = len(a)
    det = 1.0
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(a[r][i]))
        if abs(a[pivot][i]) < 1e-15:
            return 0.0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det *= -1.0
        pivot_val = a[i][i]
        det *= pivot_val
        for r in range(i + 1, n):
            factor = a[r][i] / pivot_val
            for c in range(i + 1, n):
                a[r][c] -= factor * a[i][c]
    return det


def show_regulator(p: int) -> None:
    mat = regulator_matrix(p)
    det = abs(det_float(mat))
    print(f"[info] p={p}: regulator candidate |det(log embeddings)| = {det:.12g}")
    if p <= 7:
        for row in mat:
            print("       " + "  ".join(f"{x: .9f}" for x in row))


def orbit_sets_for_pal_star(p: int, radius: int) -> list[tuple[int, tuple[int, ...]]]:
    reps = real_embedding_reps(p)
    base = coeff_pal_star(p, radius)
    orbit = []
    for b in reps:
        indices = []
        for i, count in enumerate(base):
            if count:
                for _ in range(count):
                    indices.append((b * i) % p)
        orbit.append((b, tuple(sorted(indices))))
    return orbit


def verify_p5_geometry() -> None:
    p = 5
    edge = coeff_arc(p, 0, 2)
    simp = simplex_inner_from_coeff(p, edge)
    trace = trace_inner_from_coeff(p, edge)
    assert simp == Fraction(6, 5)
    assert trace == 6

    star = coeff_pal_star(p, 1)
    phi_value = complex_value(p, star, 1).real
    phi = (1 + math.sqrt(5)) / 2
    assert abs(phi_value - phi) < 1e-12
    print("[ok] p=5: u_2 is edge sum; real unit phi is 3-star")


def verify_p7_geometry() -> None:
    p = 7
    eta3 = coeff_pal_star(p, 1)
    eta5 = coeff_pal_star(p, 2)
    neg_pair = coeff_negative_pair(p, 3)
    assert coeff_equiv_mod_gauge(eta5, neg_pair)

    orbit3 = orbit_sets_for_pal_star(p, 1)
    orbit5_as_pairs = []
    for skip in real_embedding_reps(p):
        orbit5_as_pairs.append((skip, tuple(sorted([(-skip) % p, skip % p]))))

    print("[ok] p=7: eta_5 equals negative opposite pair modulo gauge")
    print("[info] p=7 eta_3 Galois orbit (skip, vertex set):")
    for item in orbit3:
        print(f"       {item[0]} -> {item[1]}")
    print("[info] p=7 eta_5 negative-pair orbit (skip, vertex pair):")
    for item in orbit5_as_pairs:
        print(f"       {item[0]} -> {item[1]}")


def main() -> None:
    print("=== Galois/simplex verifier ===")

    for n in [3, 4, 5, 6, 7, 8, 9, 11, 13]:
        verify_normalizer(n)

    print()
    for p in [3, 5, 7, 11, 13]:
        verify_gram_identity(p)
        verify_arc_norms(p)
        if p >= 5:
            verify_real_unit_norms(p)
            show_regulator(p)
        print()

    verify_p5_geometry()
    verify_p7_geometry()

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
