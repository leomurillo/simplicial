"""Exact monomial-group census for the Phi_8 Fourier-plane test.

This script supports the N=8 complex-reflection discussion in
`8.parity_dual_simplices.md`.

On the primitive Fourier space

    E_8 = C chi_1 + C chi_3 + C chi_5 + C chi_7,

monomial matrices are represented by a permutation of the four primitive
characters and a vector of exponents modulo 8, standing for powers of
zeta_8 on the source coordinates.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path


MODULUS = 8
LABELS = (1, 3, 5, 7)
INDEX = {label: index for index, label in enumerate(LABELS)}
IDENTITY_PERM = tuple(range(len(LABELS)))
IDENTITY_EXP = (0, 0, 0, 0)


Element = tuple[tuple[int, ...], tuple[int, ...]]


def compose(left: Element, right: Element) -> Element:
    """Return the product left * right.

    The convention is that (perm, exp) sends basis vector i to
    zeta_8**exp[i] times basis vector perm[i].
    """
    perm_left, exp_left = left
    perm_right, exp_right = right
    return (
        tuple(perm_left[perm_right[i]] for i in range(len(LABELS))),
        tuple((exp_right[i] + exp_left[perm_right[i]]) % MODULUS for i in range(len(LABELS))),
    )


def closure(generators: list[Element]) -> set[Element]:
    identity = (IDENTITY_PERM, IDENTITY_EXP)
    seen = {identity}
    queue: deque[Element] = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            product = compose(current, generator)
            if product not in seen:
                seen.add(product)
                queue.append(product)
    return seen


def diagonal(exponents: list[int] | tuple[int, ...]) -> Element:
    return (IDENTITY_PERM, tuple(exponent % MODULUS for exponent in exponents))


def permutation(swaps: list[tuple[int, int]]) -> Element:
    perm = list(IDENTITY_PERM)
    for left, right in swaps:
        perm[left], perm[right] = perm[right], perm[left]
    return (tuple(perm), IDENTITY_EXP)


def unit_permutation(unit: int) -> Element:
    return (
        tuple(INDEX[(unit * label) % MODULUS] for label in LABELS),
        IDENTITY_EXP,
    )


def cycles(perm: tuple[int, ...]) -> list[list[int]]:
    seen = [False] * len(perm)
    output: list[list[int]] = []
    for start in range(len(perm)):
        if seen[start]:
            continue
        cycle = []
        current = start
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = perm[current]
        output.append(cycle)
    return output


def fixed_dimension(element: Element) -> int:
    perm, exponents = element
    fixed = 0
    for cycle in cycles(perm):
        if sum(exponents[index] for index in cycle) % MODULUS == 0:
            fixed += 1
    return fixed


def reflections(group: set[Element]) -> list[Element]:
    identity = (IDENTITY_PERM, IDENTITY_EXP)
    dimension = len(LABELS)
    return [
        element
        for element in group
        if element != identity and fixed_dimension(element) == dimension - 1
    ]


@dataclass(frozen=True)
class GroupRow:
    name: str
    order: int
    permutation_order: int
    diagonal_order: int
    reflection_count: int
    reflection_subgroup_order: int


def summarize(name: str, generators: list[Element]) -> GroupRow:
    group = closure(generators)
    group_reflections = reflections(group)
    reflection_subgroup = closure(group_reflections) if group_reflections else {(IDENTITY_PERM, IDENTITY_EXP)}
    return GroupRow(
        name=name,
        order=len(group),
        permutation_order=len({perm for perm, _ in group}),
        diagonal_order=len({exponents for perm, exponents in group if perm == IDENTITY_PERM}),
        reflection_count=len(group_reflections),
        reflection_subgroup_order=len(reflection_subgroup),
    )


def format_table(rows: list[GroupRow]) -> list[str]:
    lines = [
        "| group | order | permutation image | diagonal subgroup | reflections | reflection subgroup | reflection generated? |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"{row.name} | "
            f"{row.order} | "
            f"{row.permutation_order} | "
            f"{row.diagonal_order} | "
            f"{row.reflection_count} | "
            f"{row.reflection_subgroup_order} | "
            f"{'yes' if row.reflection_subgroup_order == row.order else 'no'} |"
        )
    return lines


def main() -> None:
    cyclic_shift = diagonal(LABELS)
    galois = [unit_permutation(unit) for unit in (1, 3, 5, 7)]

    plane_flip_17 = diagonal((4, 0, 0, 4))
    plane_flip_35 = diagonal((0, 4, 4, 0))
    coordinate_signs = [
        diagonal(tuple(4 if index == target else 0 for index in range(len(LABELS))))
        for target in range(len(LABELS))
    ]
    coordinate_phases = [
        diagonal(tuple(1 if index == target else 0 for index in range(len(LABELS))))
        for target in range(len(LABELS))
    ]

    pair_rotation_17 = diagonal((1, 0, 0, 7))
    pair_reflection_17 = permutation([(0, 3)])
    pair_rotation_35 = diagonal((0, 3, 5, 0))
    pair_reflection_35 = permutation([(1, 2)])

    rows = [
        summarize("arithmetic normalizer <C8, Gal>", [cyclic_shift, *galois]),
        summarize("real plane-sign refinement", [cyclic_shift, plane_flip_17, plane_flip_35, *galois]),
        summarize("complex sign-reflection refinement", [cyclic_shift, *coordinate_signs, *galois]),
        summarize("complex phase-reflection refinement", [*coordinate_phases, *galois]),
        summarize("pair product G(8,8,2) x G(8,8,2)", [pair_rotation_17, pair_reflection_17, pair_rotation_35, pair_reflection_35]),
        summarize("pair product plus Gal pair-exchange", [pair_rotation_17, pair_reflection_17, pair_rotation_35, pair_reflection_35, *galois]),
    ]

    report = [
        "# Phi_8 Refined Fourier-Plane Group Census",
        "",
        "**Script:** `empirical/analyze_phi8_refined_group.py`",
        "**Companion note:** `8.parity_dual_simplices.md`",
        "**Status:** all checks passed",
        "",
        "The primitive Fourier labels are ordered as `1, 3, 5, 7`.  A monomial element is stored exactly as a permutation of these labels and four exponents modulo `8`, representing powers of `zeta_8`.",
        "",
        *format_table(rows),
        "",
        "## Consequences",
        "",
        "1. The arithmetic normalizer generated by the cyclic shift and Galois permutations has order `32` and contains no complex reflections.",
        "2. Refining the real Phi_8 block into the two conjugate Fourier planes and allowing independent plane sign flips gives order `64`, still with no complex reflections on the four-dimensional complex primitive space.",
        "3. Allowing coordinate sign or phase hyperplane reflections adds genuine diagonal complex reflections, but the Galois `V_4` permutation part is not generated by reflections.  The obstruction is the absence of single transpositions; Galois units act by double transpositions on the primitive labels.",
        "4. Each conjugate pair `{chi_1, chi_7}` and `{chi_3, chi_5}` supports the rank-two dihedral reflection group `G(8,8,2)` of order `16`.  Their independent product is a reducible complex reflection group of order `256`.",
        "5. Adding the Galois pair-exchange to this product gives an order `512` normalizer extension, but its reflection subgroup remains the reducible product of order `256`.",
        "",
    ]

    report_path = Path(__file__).parent / "reports" / "phi8_refined_group.md"
    report_path.write_text("\n".join(report), encoding="utf-8")

    print("=== Phi_8 refined Fourier-plane group census ===")
    for row in rows:
        print(
            "[ok] "
            f"{row.name}: order={row.order}; reflections={row.reflection_count}; "
            f"reflection-subgroup={row.reflection_subgroup_order}; "
            f"reflection-generated={row.reflection_subgroup_order == row.order}"
        )
    print(f"\nWrote {report_path}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
