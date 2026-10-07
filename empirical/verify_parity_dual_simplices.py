"""Verify parity-dual simplex identities.

This script supports `8.parity_dual_simplices.md`.
It uses exact rational arithmetic via Fraction.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import permutations


def mat_eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(1 if i == j else 0, 1) for j in range(n)] for i in range(n)]


def mat_mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = len(b[0])
    kdim = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(kdim)) for j in range(m)]
        for i in range(n)
    ]


def mat_transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def mat_eq(a: list[list[Fraction]], b: list[list[Fraction]]) -> bool:
    return a == b


def vec_dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum(x * y for x, y in zip(a, b))


def mat_vec(a: list[list[Fraction]], v: list[Fraction]) -> list[Fraction]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def vec_sub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [x - y for x, y in zip(a, b)]


def vec_scale(c: Fraction, v: list[Fraction]) -> list[Fraction]:
    return [c * x for x in v]


def vec_neg(v: list[Fraction]) -> list[Fraction]:
    return [-x for x in v]


def vec_key(v: list[Fraction]) -> tuple[Fraction, ...]:
    return tuple(v)


def permute_vec(perm: tuple[int, ...], v: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0, 1) for _ in v]
    for i, target in enumerate(perm):
        out[target] = v[i]
    return out


def shift_matrix(n: int) -> list[list[Fraction]]:
    c = [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        c[(i + 1) % n][i] = Fraction(1, 1)
    return c


def simplex_vertices(n: int) -> list[list[Fraction]]:
    vertices = []
    for i in range(n):
        v = [Fraction(-1, n) for _ in range(n)]
        v[i] += Fraction(1, 1)
        vertices.append(v)
    return vertices


def parity_vector(n: int) -> list[Fraction]:
    return [Fraction(1 if i % 2 == 0 else -1, 1) for i in range(n)]


def parity_reflection(n: int) -> list[list[Fraction]]:
    s = parity_vector(n)
    return [
        [
            Fraction(1 if i == j else 0, 1) - Fraction(2, n) * s[i] * s[j]
            for j in range(n)
        ]
        for i in range(n)
    ]


def gram(vertices_a: list[list[Fraction]], vertices_b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[vec_dot(a, b) for b in vertices_b] for a in vertices_a]


def expected_simplex_gram(n: int) -> list[list[Fraction]]:
    return [
        [Fraction(1 if i == j else 0, 1) - Fraction(1, n) for j in range(n)]
        for i in range(n)
    ]


def expected_cross_gram(n: int) -> list[list[Fraction]]:
    s = parity_vector(n)
    return [
        [
            Fraction(1 if i == j else 0, 1)
            - Fraction(1, n)
            - Fraction(2, n) * s[i] * s[j]
            for j in range(n)
        ]
        for i in range(n)
    ]


def determinant_fraction(a: list[list[Fraction]]) -> Fraction:
    m = [row[:] for row in a]
    n = len(m)
    det = Fraction(1, 1)
    for i in range(n):
        pivot = None
        for r in range(i, n):
            if m[r][i] != 0:
                pivot = r
                break
        if pivot is None:
            return Fraction(0, 1)
        if pivot != i:
            m[i], m[pivot] = m[pivot], m[i]
            det *= -1
        pivot_val = m[i][i]
        det *= pivot_val
        for r in range(i + 1, n):
            factor = m[r][i] / pivot_val
            for c in range(i, n):
                m[r][c] -= factor * m[i][c]
    return det


def unordered_gram_profile(vertices: list[list[Fraction]]) -> Counter[Fraction]:
    profile: Counter[Fraction] = Counter()
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            profile[vec_dot(vertices[i], vertices[j])] += 1
    return profile


def coordinate_permutation_symmetries(
    vertices: list[list[Fraction]],
) -> list[tuple[int, ...]]:
    n = len(vertices[0])
    vertex_set = {vec_key(v) for v in vertices}
    symmetries = []
    for perm in permutations(range(n)):
        image = {vec_key(permute_vec(perm, v)) for v in vertices}
        if image == vertex_set:
            symmetries.append(perm)
    return symmetries


def verify_n6_compound() -> None:
    n = 6
    v = simplex_vertices(n)
    rho = parity_reflection(n)
    w = [mat_vec(rho, vertex) for vertex in v]
    compound = v + w
    compound_set = {vec_key(vertex) for vertex in compound}
    v_set = {vec_key(vertex) for vertex in v}
    w_set = {vec_key(vertex) for vertex in w}

    assert len(compound_set) == 2 * n
    assert all(vec_dot(vertex, vertex) == Fraction(n - 1, n) for vertex in compound)
    assert w[0] == [
        Fraction(1, 2),
        Fraction(1, 6),
        Fraction(-1, 2),
        Fraction(1, 6),
        Fraction(-1, 2),
        Fraction(1, 6),
    ]
    assert all(vec_key(vertex) not in v_set for vertex in w)
    assert all(vec_key(vec_neg(vertex)) not in v_set for vertex in w)

    gram_profile = unordered_gram_profile(compound)
    expected_profile = Counter(
        {
            Fraction(-1, 2): 12,
            Fraction(-1, 6): 30,
            Fraction(1, 6): 18,
            Fraction(1, 2): 6,
        }
    )
    assert gram_profile == expected_profile

    # Ambient coordinate permutations preserving the compound are exactly the
    # permutations that preserve or swap the even/odd coordinate classes.
    symmetries = coordinate_permutation_symmetries(compound)
    s = parity_vector(n)
    parity_block_symmetries = [
        perm
        for perm in permutations(range(n))
        if permute_vec(perm, s) == s or permute_vec(perm, s) == vec_neg(s)
    ]
    assert len(symmetries) == 72
    assert set(symmetries) == set(parity_block_symmetries)

    rho_v = {vec_key(mat_vec(rho, vertex)) for vertex in v}
    rho_w = {vec_key(mat_vec(rho, vertex)) for vertex in w}
    assert rho_v == w_set
    assert rho_w == v_set
    assert {vec_key(vec_neg(vertex)) for vertex in compound} != compound_set

    print(f"[info] N=6 compound unordered Gram profile={dict(sorted(gram_profile.items()))}")
    print(
        "[info] N=6 coordinate-permutation symmetries="
        f"{len(symmetries)} = 2*(3!)^2"
    )
    print("[info] N=6 central inversion is not a compound symmetry; rho_2 exchanges the two simplices")


def verify_even_n(n: int) -> None:
    assert n % 2 == 0
    s = parity_vector(n)
    c = shift_matrix(n)
    rho = parity_reflection(n)
    ident = mat_eye(n)

    assert sum(s) == 0
    assert mat_vec(c, s) == vec_scale(Fraction(-1, 1), s)
    assert mat_eq(mat_mul(rho, rho), ident)
    assert mat_eq(mat_mul(mat_transpose(rho), rho), ident)
    assert mat_eq(mat_mul(rho, c), mat_mul(c, rho))

    v = simplex_vertices(n)
    w = [mat_vec(rho, vertex) for vertex in v]

    assert gram(w, w) == expected_simplex_gram(n)
    assert gram(v, w) == expected_cross_gram(n)

    # Reflection is orientation reversing on H_N: it flips one eigendirection.
    # On full R^N it fixes the gauge direction and has determinant -1.
    assert determinant_fraction(rho) == Fraction(-1, 1)

    if n == 4:
        for i in range(n):
            expected = vec_scale(Fraction(-1, 1), v[(i + 2) % n])
            assert w[i] == expected

    values = sorted(set(x for row in gram(v, w) for x in row))
    print(f"[ok] N={n}: parity-dual simplex verified; cross-Gram values={values}")


def verify_odd_n(n: int) -> None:
    assert n % 2 == 1
    c = shift_matrix(n)
    ident = mat_eye(n)

    # C^k != -I for every k witness isn't enough; directly check that the
    # alternating candidate is not in H_N and not a -1 eigenvector.
    s = parity_vector(n)
    assert sum(s) == 1
    assert mat_vec(c, s) != vec_scale(Fraction(-1, 1), s)

    # Check C + I is invertible on the full space for odd n by determinant.
    c_plus_i = [
        [c[i][j] + ident[i][j] for j in range(n)]
        for i in range(n)
    ]
    assert determinant_fraction(c_plus_i) != 0
    print(f"[ok] N={n}: no Phi_2 parity component")


def main() -> None:
    print("=== Parity-dual simplex verifier ===")
    for n in [2, 4, 6, 8, 10, 12]:
        verify_even_n(n)
    verify_n6_compound()
    print()
    for n in [3, 5, 7, 9, 11, 13]:
        verify_odd_n(n)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
