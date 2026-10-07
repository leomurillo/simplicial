"""Probe the tetrahedral edge/Cayley-Menger bridge for the Z/6 Bures carrier.

Random suffix: t6Yp3

This script verifies:
1. The edge labelling AB, AC, AD, CD, BD, BC realizes K:r -> -r mod 6
   as the vertex transposition A <-> B.
2. The tetrahedral Cayley-Menger determinant is cubic in the six squared
   edge variables.
3. The determinant is K-invariant.
4. Its K-even/K-odd expansion contains no odd total K-odd degree.
5. The raw Cayley-Menger monomial support is not identical to the pure
   cyclic Z/6 additive-character selection rule.
"""

from __future__ import annotations

import itertools

import sympy as sp


VERTICES = ("A", "B", "C", "D")
CANONICAL_EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
BRIDGE_EDGE_ORDER = ((0, 1), (0, 2), (0, 3), (2, 3), (1, 3), (1, 2))
K_PERM = (0, 5, 4, 3, 2, 1)


def edge_name(edge: tuple[int, int]) -> str:
    return "".join(VERTICES[i] for i in edge)


def edge_index() -> dict[tuple[int, int], int]:
    index = {edge: i for i, edge in enumerate(CANONICAL_EDGES)}
    index.update({(b, a): i for i, (a, b) in enumerate(CANONICAL_EDGES)})
    return index


def cayley_menger_polynomial() -> tuple[sp.Expr, tuple[sp.Symbol, ...]]:
    x = sp.symbols("x0:6")
    idx = edge_index()
    matrix = sp.Matrix(
        [
            [0, 1, 1, 1, 1],
            [1, 0, x[idx[(0, 1)]], x[idx[(0, 2)]], x[idx[(0, 3)]]],
            [1, x[idx[(1, 0)]], 0, x[idx[(1, 2)]], x[idx[(1, 3)]]],
            [1, x[idx[(2, 0)]], x[idx[(2, 1)]], 0, x[idx[(2, 3)]]],
            [1, x[idx[(3, 0)]], x[idx[(3, 1)]], x[idx[(3, 2)]], 0],
        ]
    )
    return sp.expand(matrix.det()), x


def induced_edge_perm(vertex_perm: tuple[int, int, int, int]) -> list[int]:
    idx = edge_index()
    induced = []
    for edge in CANONICAL_EDGES:
        a, b = vertex_perm[edge[0]], vertex_perm[edge[1]]
        if a > b:
            a, b = b, a
        induced.append(idx[(a, b)])
    return induced


def bridge_order_indices() -> list[int]:
    idx = edge_index()
    return [idx[edge] for edge in BRIDGE_EDGE_ORDER]


def relabel_to_bridge(expr: sp.Expr, x: tuple[sp.Symbol, ...]) -> tuple[sp.Expr, tuple[sp.Symbol, ...]]:
    y = sp.symbols("y0:6")
    order = bridge_order_indices()
    relabelled = expr.subs({x[order[pos]]: y[pos] for pos in range(6)})
    return sp.expand(relabelled), y


def all_terms_obey_z6_selection(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> bool:
    poly = sp.Poly(expr, *variables)
    for monomial, _coeff in poly.terms():
        index_sum = sum(i * power for i, power in enumerate(monomial))
        if index_sum % 6 != 0:
            return False
    return True


def search_pure_z6_orders(expr: sp.Expr, x: tuple[sp.Symbol, ...]) -> list[tuple[tuple[int, int], ...]]:
    y = sp.symbols("y0:6")
    winners = []
    for order in itertools.permutations(range(6)):
        relabelled = sp.expand(expr.subs({x[order[pos]]: y[pos] for pos in range(6)}))
        if all_terms_obey_z6_selection(relabelled, y):
            winners.append(tuple(CANONICAL_EDGES[i] for i in order))
    return winners


def main() -> None:
    determinant, x = cayley_menger_polynomial()
    poly = sp.Poly(determinant, *x)

    print("canonical_edges:", [edge_name(edge) for edge in CANONICAL_EDGES])
    print("bridge_edge_order:", [edge_name(edge) for edge in BRIDGE_EDGE_ORDER])
    print("degree:", poly.total_degree())
    print("term_count:", len(poly.terms()))

    swap_ab = (1, 0, 2, 3)
    induced = induced_edge_perm(swap_ab)
    order = bridge_order_indices()
    induced_in_bridge_positions = []
    for pos, canonical_idx in enumerate(order):
        image_canonical_idx = induced[canonical_idx]
        induced_in_bridge_positions.append(order.index(image_canonical_idx))

    print("A<->B induced permutation in bridge positions:", induced_in_bridge_positions)
    print("expected K permutation:", list(K_PERM))
    print("matches_K:", tuple(induced_in_bridge_positions) == K_PERM)

    bridge_det, y = relabel_to_bridge(determinant, x)
    k_subs = {y[pos]: y[K_PERM[pos]] for pos in range(6)}
    k_invariant = sp.simplify(bridge_det.subs(k_subs, simultaneous=True) - bridge_det) == 0
    print("K_invariant:", k_invariant)

    A, B, C, D, U, V = sp.symbols("A B C D U V")
    even_odd_subs = {
        y[0]: A,
        y[3]: B,
        y[1]: C + U,
        y[5]: C - U,
        y[2]: D + V,
        y[4]: D - V,
    }
    even_odd = sp.Poly(sp.expand(bridge_det.subs(even_odd_subs)), A, B, C, D, U, V)
    odd_k_terms = []
    for monomial, coeff in even_odd.terms():
        if (monomial[4] + monomial[5]) % 2:
            odd_k_terms.append((monomial, coeff))
    print("K_odd_parity_violations:", len(odd_k_terms))
    print("even_odd_factor:")
    print(sp.factor(even_odd.as_expr()))

    pure_z6_orders = search_pure_z6_orders(determinant, x)
    print("pure_Z6_selection_edge_orders:", len(pure_z6_orders))

    regular_value = determinant.subs({symbol: sp.Rational(8, 3) for symbol in x})
    print("regular_l2_8_over_3_CM_det:", sp.factor(regular_value))
    print("regular_l2_8_over_3_volume_squared:", sp.factor(regular_value / 288))


if __name__ == "__main__":
    main()

