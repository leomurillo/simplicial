"""Fisher-jet functor over a local quotient-character adjacency constructor.

The local adjacency constructor owns the finite arithmetic skeleton:
labels, conductor packets, quotient-shifts, normalizer action, and carry.
This module puts the Fisher Taylor formulas behind that skeleton.  For the
current Paper 11 rows, the formulas are the centroid-normalized
character-additive formulas used in the F_4[u]/(u^2) diagnostics.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Hashable, Iterable, Literal

from local_adjacency_constructor import Label, LocalAdjacencyConstructor


JetMatrix = dict[tuple[Label, Label], Fraction]
Witness = dict[str, object]


@dataclass(frozen=True)
class ElementaryExpansion:
    """Pieces of Kbar through a mixed second-order coefficient."""

    order0: JetMatrix
    left_order1: JetMatrix
    right_order1: JetMatrix
    mixed_order2: JetMatrix

    @property
    def tame_order1(self) -> JetMatrix:
        """Compatibility alias for the first F4 mode."""

        return self.left_order1

    @property
    def wild_order1(self) -> JetMatrix:
        """Compatibility alias for the second F4 mode."""

        return self.right_order1


class FisherJet:
    """Compute Fisher Taylor pieces functorially from a constructor."""

    def __init__(self, constructor: LocalAdjacencyConstructor) -> None:
        self.constructor = constructor
        self.ring = constructor.ring
        self._expansion_cache: dict[tuple[Hashable, Hashable, Hashable], ElementaryExpansion] = {}
        self._mixed_product_cache: dict[tuple[Hashable, Hashable, Hashable, Hashable], JetMatrix] = {}

    @staticmethod
    def matrix_add(*matrices: JetMatrix) -> JetMatrix:
        keys = set().union(*(matrix.keys() for matrix in matrices))
        out: JetMatrix = {}
        for key in keys:
            value = sum((matrix.get(key, Fraction(0)) for matrix in matrices), Fraction(0))
            if value:
                out[key] = value
        return out

    @staticmethod
    def matrix_neg(matrix: JetMatrix) -> JetMatrix:
        return {key: -value for key, value in matrix.items()}

    @classmethod
    def matrix_sub(cls, left: JetMatrix, right: JetMatrix) -> JetMatrix:
        return cls.matrix_add(left, cls.matrix_neg(right))

    @staticmethod
    def matrix_scale(matrix: JetMatrix, scalar: Fraction) -> JetMatrix:
        return {key: scalar * value for key, value in matrix.items() if scalar * value}

    @staticmethod
    def matrix_mul(left: JetMatrix, right: JetMatrix) -> JetMatrix:
        by_middle: dict[Label, list[tuple[Label, Fraction]]] = {}
        for (middle, col), value in right.items():
            by_middle.setdefault(middle, []).append((col, value))

        out: JetMatrix = {}
        for (row, middle), left_value in left.items():
            for col, right_value in by_middle.get(middle, []):
                key = (row, col)
                out[key] = out.get(key, Fraction(0)) + left_value * right_value
        return {key: value for key, value in out.items() if value}

    def product(self, matrices: Iterable[JetMatrix]) -> JetMatrix:
        matrices = list(matrices)
        if not matrices:
            return {(label, label): Fraction(1) for label in self.ring.nontrivial}
        out = matrices[0]
        for matrix in matrices[1:]:
            out = self.matrix_mul(out, matrix)
        return out

    def first_order_coeff(self, mode: Label, gamma: Label, rho: Label) -> Fraction:
        """Coefficient of an elementary mode in the t-linear term."""

        if gamma == self.ring.zero:
            return Fraction(-2 if mode == rho else 0)
        return Fraction(-1 if mode == self.ring.add(rho, gamma) else 0)

    def mixed_second_order_coeff(
        self,
        left_mode: Label,
        right_mode: Label,
        gamma: Label,
        rho: Label,
    ) -> Fraction:
        """Coefficient of s*r in the t^2 term for output rho.

        The convolution term contributes two ordered products when
        rho + gamma = left_mode + right_mode.  The moving tangent projection
        contributes one more mixed product when {gamma, rho} is the two-mode
        set.  This is the characteristic-two elementary-mode formula used by
        the current exact rows.
        """

        value = Fraction(0)
        if self.ring.add(rho, gamma) == self.ring.add(left_mode, right_mode):
            value += 2
        if (gamma == left_mode and rho == right_mode) or (
            gamma == right_mode and rho == left_mode
        ):
            value += 1
        return value

    def elementary_expansion(
        self,
        alpha: Label,
        left_mode: Label,
        right_mode: Label,
    ) -> ElementaryExpansion:
        key = (alpha, left_mode, right_mode)
        cached = self._expansion_cache.get(key)
        if cached is not None:
            return cached

        order0: JetMatrix = {}
        left_order1: JetMatrix = {}
        right_order1: JetMatrix = {}
        mixed_order2: JetMatrix = {}

        for beta in self.ring.nontrivial:
            gamma = self.ring.add(alpha, beta)
            if gamma != self.ring.zero:
                order0[(gamma, beta)] = Fraction(1)

            for rho in self.ring.nontrivial:
                left = self.first_order_coeff(left_mode, gamma, rho)
                right = self.first_order_coeff(right_mode, gamma, rho)
                mixed = self.mixed_second_order_coeff(left_mode, right_mode, gamma, rho)
                if left:
                    left_order1[(rho, beta)] = left
                if right:
                    right_order1[(rho, beta)] = right
                if mixed:
                    mixed_order2[(rho, beta)] = mixed

        expansion = ElementaryExpansion(order0, left_order1, right_order1, mixed_order2)
        self._expansion_cache[key] = expansion
        return expansion

    def mixed_product_order2(
        self,
        alpha: Label,
        beta: Label,
        left_mode: Label,
        right_mode: Label,
    ) -> JetMatrix:
        key = (alpha, beta, left_mode, right_mode)
        cached = self._mixed_product_cache.get(key)
        if cached is not None:
            return cached

        ka = self.elementary_expansion(alpha, left_mode, right_mode)
        kb = self.elementary_expansion(beta, left_mode, right_mode)
        out = self.matrix_add(
            self.matrix_mul(ka.mixed_order2, kb.order0),
            self.matrix_mul(ka.left_order1, kb.right_order1),
            self.matrix_mul(ka.right_order1, kb.left_order1),
            self.matrix_mul(ka.order0, kb.mixed_order2),
        )
        self._mixed_product_cache[key] = out
        return out

    def mixed_defect_order2(
        self,
        alpha: Label,
        beta: Label,
        left_mode: Label,
        right_mode: Label,
    ) -> JetMatrix:
        direct = self.elementary_expansion(
            self.ring.add(alpha, beta),
            left_mode,
            right_mode,
        ).mixed_order2
        return self.matrix_sub(
            self.mixed_product_order2(alpha, beta, left_mode, right_mode),
            direct,
        )

    def mixed_symmetric_order2(
        self,
        alpha: Label,
        beta: Label,
        left_mode: Label,
        right_mode: Label,
    ) -> JetMatrix:
        direct = self.elementary_expansion(
            self.ring.add(alpha, beta),
            left_mode,
            right_mode,
        ).mixed_order2
        sym_product = self.matrix_scale(
            self.matrix_add(
                self.mixed_product_order2(alpha, beta, left_mode, right_mode),
                self.mixed_product_order2(beta, alpha, left_mode, right_mode),
            ),
            Fraction(1, 2),
        )
        return self.matrix_sub(sym_product, direct)

    def mixed_commutator_order2(
        self,
        alpha: Label,
        beta: Label,
        left_mode: Label,
        right_mode: Label,
    ) -> JetMatrix:
        return self.matrix_scale(
            self.matrix_sub(
                self.mixed_product_order2(alpha, beta, left_mode, right_mode),
                self.mixed_product_order2(beta, alpha, left_mode, right_mode),
            ),
            Fraction(1, 2),
        )

    def mixed_product_operator(
        self,
        labels: tuple[Label, ...],
        left_mode: Label,
        right_mode: Label,
    ) -> JetMatrix:
        """Mixed s*r*t^2 coefficient of an ordered product of Kbar labels."""

        pieces = [self.elementary_expansion(label, left_mode, right_mode) for label in labels]
        out: JetMatrix = {}

        for mixed_index in range(len(pieces)):
            matrices = [
                piece.mixed_order2 if index == mixed_index else piece.order0
                for index, piece in enumerate(pieces)
            ]
            out = self.matrix_add(out, self.product(matrices))

        for left_index in range(len(pieces)):
            for right_index in range(len(pieces)):
                if left_index == right_index:
                    continue
                matrices = []
                for index, piece in enumerate(pieces):
                    if index == left_index:
                        matrices.append(piece.left_order1)
                    elif index == right_index:
                        matrices.append(piece.right_order1)
                    else:
                        matrices.append(piece.order0)
                out = self.matrix_add(out, self.product(matrices))

        return out

    def moment_operator(
        self,
        labels: tuple[Label, ...],
        left_mode: Label,
        right_mode: Label,
    ) -> JetMatrix:
        return self.product(
            self.elementary_expansion(label, left_mode, right_mode).order0
            for label in labels
        )

    def witnesses(
        self,
        kind: Literal["defect", "symmetric", "commutator"] = "defect",
        *,
        left_modes: Iterable[Label],
        right_modes: Iterable[Label],
    ) -> list[Witness]:
        extractors = {
            "defect": self.mixed_defect_order2,
            "symmetric": self.mixed_symmetric_order2,
            "commutator": self.mixed_commutator_order2,
        }
        extractor = extractors[kind]
        witnesses: list[Witness] = []
        for left_mode in left_modes:
            for right_mode in right_modes:
                for alpha in self.ring.nontrivial:
                    for beta in self.ring.nontrivial:
                        entries = extractor(alpha, beta, left_mode, right_mode)
                        for (row, col), coefficient in entries.items():
                            witnesses.append(
                                {
                                    "left_mode": left_mode,
                                    "right_mode": right_mode,
                                    "tau": left_mode,
                                    "omega": right_mode,
                                    "alpha": alpha,
                                    "beta": beta,
                                    "input": col,
                                    "output": row,
                                    "coefficient": coefficient,
                                    "input_conductor": self.ring.conductor(col),
                                    "output_conductor": self.ring.conductor(row),
                                }
                            )
        return witnesses

    def tangent_compatible(self, witnesses: Iterable[Witness]) -> list[Witness]:
        return [
            witness
            for witness in witnesses
            if self.ring.add(witness["alpha"], witness["beta"]) != self.ring.zero
        ]

    @staticmethod
    def witness_key(witness: Witness) -> tuple[Label, Label, Label, Label, Label, Label]:
        return (
            witness["tau"],
            witness["omega"],
            witness["alpha"],
            witness["beta"],
            witness["input"],
            witness["output"],
        )

    def coefficient_by_key(self, witnesses: Iterable[Witness]) -> dict[tuple[Label, ...], Fraction]:
        return {self.witness_key(witness): witness["coefficient"] for witness in witnesses}

