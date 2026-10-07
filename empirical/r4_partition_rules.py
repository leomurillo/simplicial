"""Pure partition-lattice coefficients for the Paper 11 R^(4) verifier."""

from __future__ import annotations

from fractions import Fraction
from math import factorial


Partition = tuple[tuple[int, ...], ...]

TOP: Partition = ((0, 1, 2, 3),)
BIANCHI_MIDDLE_SPLIT: Partition = ((0, 2), (1, 3))
R4_NORMALIZATION = factorial(4)


def all_partitions(n: int) -> list[Partition]:
    partitions: list[Partition] = []

    def rec(index: int, blocks: list[list[int]]) -> None:
        if index == n:
            partitions.append(
                tuple(tuple(block) for block in sorted(blocks, key=lambda item: item[0]))
            )
            return

        for block in blocks:
            block.append(index)
            rec(index + 1, blocks)
            block.pop()

        blocks.append([index])
        rec(index + 1, blocks)
        blocks.pop()

    rec(0, [])
    return partitions


def refines(left: Partition, right: Partition) -> bool:
    right_blocks = [set(block) for block in right]
    return all(
        any(set(block).issubset(target) for target in right_blocks)
        for block in left
    )


def partition_lattice_mobius(left: Partition, right: Partition) -> Fraction:
    if not refines(left, right):
        return Fraction(0)

    value = Fraction(1)
    left_blocks = [set(block) for block in left]
    for target in right:
        target_set = set(target)
        inside = sum(1 for block in left_blocks if block.issubset(target_set))
        value *= Fraction(((-1) ** (inside - 1)) * factorial(inside - 1))
    return value


def leibniz_coefficient(partition: Partition) -> Fraction:
    return partition_lattice_mobius(partition, TOP)


def bianchi_correction(partition: Partition) -> Fraction:
    """Correction induced by the paired-slot Bianchi cancellation."""

    return partition_lattice_mobius(partition, BIANCHI_MIDDLE_SPLIT)


def projected_coefficient(partition: Partition) -> Fraction:
    return leibniz_coefficient(partition) + bianchi_correction(partition)
