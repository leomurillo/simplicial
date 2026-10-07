"""Reusable finite local quotient-character adjacency constructor.

This module is the algebra-first replacement for row-specific orbit scripts.
It builds the finite ingredients

    R_p -> (A_Rp, gr A_Rp, kappa, Gamma_Rp)

for concrete finite local rows.  The first target is F_4[u]/(u^2), but the
same interface also covers the F_16 tame control and the F_2[u]/(u^4) wild
control used in Paper 11.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import permutations, product
from typing import Callable, Hashable, Iterable, Literal, Mapping


Label = Hashable
Matrix = dict[tuple[Label, Label], int]


@dataclass(frozen=True)
class NormalizerAction:
    """A label action, stored as images aligned with ring.labels."""

    name: str
    images: tuple[Label, ...]


@dataclass(frozen=True)
class FiniteFieldSpec:
    """Binary finite field declaration for residue/coefficient arithmetic."""

    degree: int
    modulus: int
    symbol: str = "a"
    name: str | None = None

    def __post_init__(self) -> None:
        if self.degree < 1:
            raise ValueError("finite-field degree must be positive")
        if not (self.modulus & (1 << self.degree)):
            raise ValueError("field modulus must include the leading term")


ConductorConvention = Literal["reverse_valuation", "field"]


@dataclass(frozen=True)
class FiniteRingSpec:
    """Declarative finite local ring row for the adjacency constructor.

    The factory below currently implements the Paper 11 characteristic-two
    rows: a residue field F_{2^m} and one nilpotent generator u with relation
    u^e = 0.  Optional Frobenius and generator-substitution automorphism
    generators are closed into a finite action group before unit multiplication
    is added.
    """

    name: str
    coefficient_field: FiniteFieldSpec
    nilpotency: int
    variable: str = "u"
    frobenius_generators: tuple[int, ...] = ()
    automorphism_generators: tuple[tuple[int, ...], ...] = ()
    include_all_unipotent_automorphisms: bool = False
    conductor_convention: ConductorConvention = "reverse_valuation"

    @property
    def nilpotent_relation(self) -> str:
        return f"{self.variable}^{self.nilpotency}=0"

    @property
    def residue_extension_polynomial(self) -> int:
        return self.coefficient_field.modulus

    def __post_init__(self) -> None:
        if self.nilpotency < 1:
            raise ValueError("nilpotency must be positive")
        if self.conductor_convention == "field" and self.nilpotency != 1:
            raise ValueError("field conductor convention requires nilpotency 1")


class FiniteLocalRing:
    """Small finite ring model sufficient for adjacency construction."""

    def __init__(
        self,
        *,
        name: str,
        labels: Iterable[Label],
        zero: Label,
        add: Callable[[Label, Label], Label],
        conductor: Callable[[Label], str],
        label_name: Callable[[Label], str],
        normalizer_actions: Iterable[NormalizerAction],
        conductor_order: Iterable[str],
        conductor_letter: Callable[[Label], str] | None = None,
        local_signature: Callable[[tuple[Label, ...]], tuple[tuple[object, ...], ...]]
        | None = None,
    ) -> None:
        self.name = name
        self.labels = tuple(labels)
        self.zero = zero
        self.add = add
        self.conductor = conductor
        self.label_name = label_name
        self.normalizer_actions = tuple(normalizer_actions)
        self.conductor_order = tuple(conductor_order)
        self.conductor_letter = conductor_letter or conductor
        self.local_signature = local_signature
        self.label_index = {label: index for index, label in enumerate(self.labels)}
        if len(self.label_index) != len(self.labels):
            raise ValueError(f"{name}: labels are not unique")
        if zero not in self.label_index:
            raise ValueError(f"{name}: zero label is absent")

    @property
    def nontrivial(self) -> tuple[Label, ...]:
        return tuple(label for label in self.labels if label != self.zero)

    def add_many(self, labels: Iterable[Label]) -> Label:
        out = self.zero
        for label in labels:
            out = self.add(out, label)
        return out

    def apply(self, action: NormalizerAction, label: Label) -> Label:
        return action.images[self.label_index[label]]

    def transform_tuple(
        self,
        cell: tuple[Label, ...],
        action: NormalizerAction,
        permutation: tuple[int, ...] | None = None,
    ) -> tuple[Label, ...]:
        acted = tuple(self.apply(action, label) for label in cell)
        if permutation is None:
            return acted
        return tuple(acted[index] for index in permutation)

    def sort_key(self, label: Label) -> tuple[str, str]:
        return self.conductor(label), self.label_name(label)


@dataclass(frozen=True)
class QuotientShift:
    """One nonzero partial quotient-shift generator."""

    eta: Label
    source: str
    target: str
    matrix: tuple[tuple[Label, Label], ...]

    @property
    def support_size(self) -> int:
        return len(self.matrix)


@dataclass(frozen=True)
class CarryRecord:
    """Carry of a composable pair relative to the direct quotient-shift section."""

    left_eta: Label
    right_eta: Label
    source: str
    middle: str
    target: str
    product_support: int
    direct_support: int
    positive_delta: int
    negative_delta: int

    @property
    def path_word(self) -> str:
        return f"{self.source}->{self.middle}->{self.target}"


class LocalAdjacencyConstructor:
    """Build adjacency, graded packets, normalizer, and carry data."""

    def __init__(self, ring: FiniteLocalRing) -> None:
        self.ring = ring
        self.packets = self._build_packets()
        self.shifts = self._build_shifts()
        self.shift_by_key = {
            (shift.eta, shift.source, shift.target): shift for shift in self.shifts
        }
        self.shifts_by_source: dict[str, list[QuotientShift]] = {}
        for shift in self.shifts:
            self.shifts_by_source.setdefault(shift.source, []).append(shift)

    def _build_packets(self) -> dict[str, tuple[Label, ...]]:
        packets: dict[str, list[Label]] = {name: [] for name in self.ring.conductor_order}
        for label in self.ring.nontrivial:
            conductor = self.ring.conductor(label)
            if conductor not in packets:
                packets[conductor] = []
            packets[conductor].append(label)
        return {
            conductor: tuple(sorted(labels, key=self.ring.sort_key))
            for conductor, labels in packets.items()
            if labels
        }

    def _shift_matrix(self, eta: Label, source: str, target: str) -> Matrix:
        matrix: Matrix = {}
        for input_label in self.packets[source]:
            output_label = self.ring.add(eta, input_label)
            if output_label == self.ring.zero:
                continue
            if self.ring.conductor(output_label) == target:
                matrix[(output_label, input_label)] = 1
        return matrix

    def _build_shifts(self) -> tuple[QuotientShift, ...]:
        shifts: list[QuotientShift] = []
        for eta in self.ring.labels:
            for source in self.packets:
                for target in self.packets:
                    matrix = self._shift_matrix(eta, source, target)
                    if matrix:
                        shifts.append(
                            QuotientShift(
                                eta=eta,
                                source=source,
                                target=target,
                                matrix=self._matrix_tuple(matrix),
                            )
                        )
        return tuple(shifts)

    def _matrix_tuple(self, matrix: Mapping[tuple[Label, Label], int]) -> tuple[tuple[Label, Label], ...]:
        return tuple(
            sorted(
                (key for key, value in matrix.items() if value),
                key=lambda item: (
                    self.ring.label_name(item[0]),
                    self.ring.label_name(item[1]),
                ),
            )
        )

    @staticmethod
    def matrix_from_tuple(matrix: tuple[tuple[Label, Label], ...]) -> Matrix:
        return {entry: 1 for entry in matrix}

    @staticmethod
    def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
        by_middle: dict[Label, list[tuple[Label, int]]] = {}
        for (middle, col), value in right.items():
            by_middle.setdefault(middle, []).append((col, value))

        out: Matrix = {}
        for (row, middle), left_value in left.items():
            for col, right_value in by_middle.get(middle, []):
                out[(row, col)] = out.get((row, col), 0) + left_value * right_value
        return {key: value for key, value in out.items() if value}

    @staticmethod
    def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
        keys = set(left) | set(right)
        return {
            key: left.get(key, 0) - right.get(key, 0)
            for key in keys
            if left.get(key, 0) - right.get(key, 0)
        }

    def carry_records(self) -> tuple[CarryRecord, ...]:
        """Return nonzero section defects for composable quotient-shifts."""

        records: list[CarryRecord] = []
        for right in self.shifts:
            for left in self.shifts_by_source.get(right.target, []):
                product_matrix = self.matrix_mul(
                    self.matrix_from_tuple(left.matrix),
                    self.matrix_from_tuple(right.matrix),
                )
                direct_eta = self.ring.add(left.eta, right.eta)
                direct = self.shift_by_key.get((direct_eta, right.source, left.target))
                direct_matrix = self.matrix_from_tuple(direct.matrix) if direct else {}
                delta = self.matrix_sub(product_matrix, direct_matrix)
                if not delta:
                    continue
                records.append(
                    CarryRecord(
                        left_eta=left.eta,
                        right_eta=right.eta,
                        source=right.source,
                        middle=right.target,
                        target=left.target,
                        product_support=len(product_matrix),
                        direct_support=len(direct_matrix),
                        positive_delta=sum(1 for value in delta.values() if value > 0),
                        negative_delta=sum(1 for value in delta.values() if value < 0),
                    )
                )
        return tuple(records)

    def associativity_failures(self) -> int:
        """Check associativity on all composable triples of shift generators."""

        failures = 0
        for first in self.shifts:
            first_matrix = self.matrix_from_tuple(first.matrix)
            for second in self.shifts_by_source.get(first.target, []):
                second_matrix = self.matrix_from_tuple(second.matrix)
                for third in self.shifts_by_source.get(second.target, []):
                    third_matrix = self.matrix_from_tuple(third.matrix)
                    left = self.matrix_mul(
                        self.matrix_mul(third_matrix, second_matrix),
                        first_matrix,
                    )
                    right = self.matrix_mul(
                        third_matrix,
                        self.matrix_mul(second_matrix, first_matrix),
                    )
                    if left != right:
                        failures += 1
        return failures

    def closed_cells(self, arity: int) -> tuple[tuple[Label, ...], ...]:
        cells: list[tuple[Label, ...]] = []
        for prefix in product(self.ring.nontrivial, repeat=arity - 1):
            final = self.ring.add_many(prefix)
            if final != self.ring.zero:
                cells.append(tuple(prefix) + (final,))
        return tuple(cells)

    def tuple_orbits(
        self,
        tuples: Iterable[tuple[Label, ...]],
        *,
        permutations_to_use: Iterable[tuple[int, ...] | None] | None = None,
    ) -> tuple[set[tuple[Label, ...]], ...]:
        tuple_set = set(tuples)
        if not tuple_set:
            return tuple()
        arity = len(next(iter(tuple_set)))
        if permutations_to_use is None:
            permutations_to_use = tuple(permutations(range(arity)))

        remaining = set(tuple_set)
        orbits: list[set[tuple[Label, ...]]] = []
        while remaining:
            seed = min(remaining, key=self.tuple_name)
            orbit = {
                self.ring.transform_tuple(seed, action, permutation)
                for action in self.ring.normalizer_actions
                for permutation in permutations_to_use
            }
            present = orbit & tuple_set
            orbits.append(present)
            remaining -= present
        return tuple(orbits)

    def tuple_name(self, cell: tuple[Label, ...]) -> tuple[str, ...]:
        return tuple(self.ring.label_name(label) for label in cell)

    def conductor_word(self, cell: tuple[Label, ...]) -> str:
        return "".join(self.ring.conductor_letter(label) for label in cell)

    def conductor_family(self, cell: tuple[Label, ...]) -> str:
        return "".join(sorted(self.conductor_word(cell)))

    def summary(self) -> dict[str, object]:
        carry = self.carry_records()
        support_distribution = Counter(shift.support_size for shift in self.shifts)
        carry_paths = Counter(record.path_word for record in carry)
        return {
            "ring": self.ring.name,
            "label_count": len(self.ring.labels),
            "nontrivial_label_count": len(self.ring.nontrivial),
            "packets": {
                conductor: len(labels) for conductor, labels in self.packets.items()
            },
            "gamma_size": len(self.ring.normalizer_actions),
            "quotient_shift_count": len(self.shifts),
            "quotient_shift_support_distribution": dict(sorted(support_distribution.items())),
            "carry_record_count": len(carry),
            "carry_path_distribution": dict(sorted(carry_paths.items())),
            "associativity_failures": self.associativity_failures(),
        }


# ---------------------------------------------------------------------------
# Declarative truncated-polynomial local-ring factory


class BinaryExtensionField:
    """Arithmetic in F_2[x]/(modulus)."""

    def __init__(self, spec: FiniteFieldSpec) -> None:
        self.spec = spec
        self.degree = spec.degree
        self.modulus = spec.modulus
        self.size = 1 << spec.degree
        self.mask = self.size - 1

    @staticmethod
    def add(x: int, y: int) -> int:
        return x ^ y

    def mul(self, x: int, y: int) -> int:
        product_bits = 0
        left = x
        right = y
        while right:
            if right & 1:
                product_bits ^= left
            right >>= 1
            left <<= 1

        for product_degree in range(2 * self.degree - 2, self.degree - 1, -1):
            if product_bits & (1 << product_degree):
                product_bits ^= self.modulus << (product_degree - self.degree)
        return product_bits & self.mask

    def square(self, x: int) -> int:
        return self.mul(x, x)

    def frobenius(self, x: int, power: int) -> int:
        out = x
        for _ in range(power % self.degree):
            out = self.square(out)
        return out

    def label_name(self, x: int) -> str:
        if x == 0:
            return "0"
        if x == 1:
            return "1"

        parts: list[str] = []
        if x & 1:
            parts.append("1")
        for degree in range(1, self.degree):
            if not (x & (1 << degree)):
                continue
            if degree == 1:
                parts.append(self.spec.symbol)
            else:
                parts.append(f"{self.spec.symbol}^{degree}")
        return "+".join(parts)


class TruncatedPolynomialRingModel:
    """Concrete operations for k[u]/(u^e) labels."""

    def __init__(self, spec: FiniteRingSpec) -> None:
        self.spec = spec
        self.field = BinaryExtensionField(spec.coefficient_field)
        self.nilpotency = spec.nilpotency
        self.zero = tuple(0 for _ in range(self.nilpotency))
        self.one = (1,) + tuple(0 for _ in range(self.nilpotency - 1))
        self.labels = tuple(product(range(self.field.size), repeat=self.nilpotency))
        self.label_index = {label: index for index, label in enumerate(self.labels)}

    def add(self, x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(self.field.add(a, b) for a, b in zip(x, y))

    def scalar_mul(self, scalar: int, x: tuple[int, ...]) -> tuple[int, ...]:
        if scalar == 0:
            return self.zero
        return tuple(self.field.mul(scalar, coefficient) for coefficient in x)

    def mul(self, x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
        out = [0 for _ in range(self.nilpotency)]
        for left_degree, left_coeff in enumerate(x):
            if left_coeff == 0:
                continue
            for right_degree, right_coeff in enumerate(y):
                total_degree = left_degree + right_degree
                if total_degree >= self.nilpotency or right_coeff == 0:
                    continue
                out[total_degree] = self.field.add(
                    out[total_degree],
                    self.field.mul(left_coeff, right_coeff),
                )
        return tuple(out)

    def pow(self, x: tuple[int, ...], exponent: int) -> tuple[int, ...]:
        out = self.one
        for _ in range(exponent):
            out = self.mul(out, x)
        return out

    def frobenius(self, x: tuple[int, ...], power: int) -> tuple[int, ...]:
        return tuple(self.field.frobenius(coefficient, power) for coefficient in x)

    def substitute_generator(
        self,
        x: tuple[int, ...],
        image_u: tuple[int, ...],
    ) -> tuple[int, ...]:
        powers = [self.one]
        for _ in range(1, self.nilpotency):
            powers.append(self.mul(powers[-1], image_u))

        out = self.zero
        for degree, coefficient in enumerate(x):
            if coefficient == 0:
                continue
            out = self.add(out, self.scalar_mul(coefficient, powers[degree]))
        return out

    def valuation(self, x: tuple[int, ...]) -> int | None:
        for degree, coefficient in enumerate(x):
            if coefficient != 0:
                return degree
        return None

    def conductor_exponent(self, x: tuple[int, ...]) -> int:
        valuation = self.valuation(x)
        if valuation is None:
            return 0
        return self.nilpotency - valuation

    def conductor(self, x: tuple[int, ...]) -> str:
        if x == self.zero:
            return "1"
        if self.spec.conductor_convention == "field":
            return "field"

        exponent = self.conductor_exponent(x)
        if exponent == 1:
            return self.spec.variable
        return f"{self.spec.variable}^{exponent}"

    def conductor_order(self) -> tuple[str, ...]:
        if self.spec.conductor_convention == "field":
            return ("field",)
        return tuple(
            self.spec.variable if exponent == 1 else f"{self.spec.variable}^{exponent}"
            for exponent in range(1, self.nilpotency + 1)
        )

    def conductor_letter(self, x: tuple[int, ...]) -> str:
        if self.spec.conductor_convention == "field":
            return "F"
        return str(self.conductor_exponent(x))

    def label_name(self, x: tuple[int, ...]) -> str:
        if x == self.zero:
            return "0"

        parts: list[str] = []
        for degree, coefficient in enumerate(x):
            if coefficient == 0:
                continue
            coefficient_name = self.field.label_name(coefficient)
            if degree == 0:
                parts.append(coefficient_name)
                continue

            monomial = self.spec.variable if degree == 1 else f"{self.spec.variable}^{degree}"
            if coefficient == 1:
                parts.append(monomial)
                continue
            if "+" in coefficient_name:
                coefficient_name = f"({coefficient_name})"
            parts.append(f"{coefficient_name}*{monomial}")
        return "+".join(parts)

    def unit_action(self, unit: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
        return tuple(self.mul(unit, label) for label in self.labels)

    def automorphism_action(
        self,
        image_u: tuple[int, ...],
    ) -> tuple[tuple[int, ...], ...]:
        self._validate_generator_image(image_u)
        return tuple(self.substitute_generator(label, image_u) for label in self.labels)

    def frobenius_action(self, power: int) -> tuple[tuple[int, ...], ...]:
        return tuple(self.frobenius(label, power) for label in self.labels)

    def _validate_generator_image(self, image_u: tuple[int, ...]) -> None:
        if len(image_u) != self.nilpotency:
            raise ValueError("automorphism generator image has the wrong length")
        if image_u[0] != 0:
            raise ValueError("automorphism generator image must have zero constant term")
        if self.nilpotency > 1 and image_u[1] == 0:
            raise ValueError("automorphism generator image must have nonzero u coefficient")

    def unipotent_generator_images(self) -> tuple[tuple[int, ...], ...]:
        if self.nilpotency == 1:
            return (self.zero,)

        tails = product(range(self.field.size), repeat=max(0, self.nilpotency - 2))
        return tuple((0, 1, *tail) for tail in tails)


def _compose_label_actions(
    first: tuple[Label, ...],
    second: tuple[Label, ...],
    label_index: Mapping[Label, int],
) -> tuple[Label, ...]:
    """Compose two action signatures, applying first and then second."""

    return tuple(second[label_index[label]] for label in first)


def _close_action_group(
    *,
    labels: tuple[Label, ...],
    generators: Iterable[tuple[Label, ...]],
    label_index: Mapping[Label, int],
) -> tuple[tuple[Label, ...], ...]:
    identity = tuple(labels)
    generator_tuple = tuple(dict.fromkeys(generators))
    seen = {identity}
    frontier = [identity]

    while frontier:
        current = frontier.pop()
        for generator in generator_tuple:
            candidate = _compose_label_actions(current, generator, label_index)
            if candidate in seen:
                continue
            seen.add(candidate)
            frontier.append(candidate)

    return tuple(sorted(seen, key=lambda action: tuple(str(label) for label in action)))


def _frobenius_powers(field_degree: int, generators: tuple[int, ...]) -> tuple[int, ...]:
    if not generators:
        return (0,)
    seen = {0}
    frontier = [0]
    normalized_generators = tuple(power % field_degree for power in generators)
    while frontier:
        current = frontier.pop()
        for generator in normalized_generators:
            candidate = (current + generator) % field_degree
            if candidate in seen:
                continue
            seen.add(candidate)
            frontier.append(candidate)
    return tuple(sorted(seen))


def make_finite_local_ring(
    spec: FiniteRingSpec,
    *,
    local_signature: Callable[[tuple[Label, ...]], tuple[tuple[object, ...], ...]]
    | None = None,
) -> FiniteLocalRing:
    """Build a `FiniteLocalRing` from a declarative truncated-polynomial spec."""

    model = TruncatedPolynomialRingModel(spec)
    labels = model.labels
    label_index = {label: index for index, label in enumerate(labels)}

    automorphism_generators = [
        model.automorphism_action(tuple(image_u))
        for image_u in spec.automorphism_generators
    ]
    if spec.include_all_unipotent_automorphisms:
        automorphism_generators.extend(
            model.automorphism_action(image_u)
            for image_u in model.unipotent_generator_images()
        )
    automorphism_actions = _close_action_group(
        labels=labels,
        generators=automorphism_generators,
        label_index=label_index,
    )

    frobenius_powers = _frobenius_powers(
        spec.coefficient_field.degree,
        spec.frobenius_generators,
    )
    units = tuple(label for label in labels if label != model.zero and label[0] != 0)

    normalizer_actions: list[NormalizerAction] = []
    seen: set[tuple[Label, ...]] = set()
    for unit in units:
        unit_images = model.unit_action(unit)
        for automorphism_index, automorphism_images in enumerate(automorphism_actions):
            unit_automorphism_images = _compose_label_actions(
                unit_images,
                automorphism_images,
                label_index,
            )
            for frobenius_power in frobenius_powers:
                images = tuple(
                    model.frobenius(label, frobenius_power)
                    for label in unit_automorphism_images
                )
                if images in seen:
                    continue
                seen.add(images)
                normalizer_actions.append(
                    NormalizerAction(
                        name=(
                            f"unit={model.label_name(unit)}"
                            f";aut={automorphism_index}"
                            f";frob={frobenius_power}"
                        ),
                        images=images,
                    )
                )

    return FiniteLocalRing(
        name=spec.name,
        labels=labels,
        zero=model.zero,
        add=model.add,
        conductor=model.conductor,
        label_name=model.label_name,
        normalizer_actions=normalizer_actions,
        conductor_order=model.conductor_order(),
        conductor_letter=model.conductor_letter,
        local_signature=local_signature,
    )


def make_f2_u2_ring() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_2[u]/(u^2)",
            coefficient_field=FiniteFieldSpec(degree=1, modulus=0b11, symbol="a", name="F_2"),
            nilpotency=2,
            include_all_unipotent_automorphisms=True,
        )
    )


def make_f2_u3_ring() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_2[u]/(u^3)",
            coefficient_field=FiniteFieldSpec(degree=1, modulus=0b11, symbol="a", name="F_2"),
            nilpotency=3,
            include_all_unipotent_automorphisms=True,
        )
    )


def make_f2_u5_ring() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_2[u]/(u^5)",
            coefficient_field=FiniteFieldSpec(degree=1, modulus=0b11, symbol="a", name="F_2"),
            nilpotency=5,
            include_all_unipotent_automorphisms=True,
        )
    )


def make_f4_u3_ring() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_4[u]/(u^3)",
            coefficient_field=FiniteFieldSpec(degree=2, modulus=0b111, symbol="w", name="F_4"),
            nilpotency=3,
            frobenius_generators=(1,),
        )
    )


def make_f8_u2_ring() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_8[u]/(u^2)",
            coefficient_field=FiniteFieldSpec(degree=3, modulus=0b1011, symbol="b", name="F_8"),
            nilpotency=2,
            frobenius_generators=(1,),
        )
    )


def make_f16_u2_ring() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_16[u]/(u^2)",
            coefficient_field=FiniteFieldSpec(degree=4, modulus=0b10011, symbol="a", name="F_16"),
            nilpotency=2,
            frobenius_generators=(1,),
        )
    )


def make_f4_u2_ring_from_spec() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_4[u]/(u^2) [spec]",
            coefficient_field=FiniteFieldSpec(degree=2, modulus=0b111, symbol="w", name="F_4"),
            nilpotency=2,
            frobenius_generators=(1,),
        ),
        local_signature=f4u2_signature,
    )


def make_f16_ring_from_spec() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_16 [spec]",
            coefficient_field=FiniteFieldSpec(degree=4, modulus=0b10011, symbol="a", name="F_16"),
            nilpotency=1,
            frobenius_generators=(1,),
            conductor_convention="field",
        )
    )


def make_f2_u4_ring_from_spec() -> FiniteLocalRing:
    return make_finite_local_ring(
        FiniteRingSpec(
            name="F_2[u]/(u^4) [spec]",
            coefficient_field=FiniteFieldSpec(degree=1, modulus=0b11, symbol="a", name="F_2"),
            nilpotency=4,
            include_all_unipotent_automorphisms=True,
        )
    )


# ---------------------------------------------------------------------------
# F_4[u]/(u^2)


F4_NAMES = {0: "0", 1: "1", 2: "w", 3: "w+1"}


def f4_add(a: int, b: int) -> int:
    return a ^ b


def f4_mul(a: int, b: int) -> int:
    a0, a1 = a & 1, (a >> 1) & 1
    b0, b1 = b & 1, (b >> 1) & 1
    c0 = a0 & b0
    c1 = (a0 & b1) ^ (a1 & b0)
    c2 = a1 & b1
    return (c0 ^ c2) | ((c1 ^ c2) << 1)


def f4_inv(a: int) -> int:
    if a == 0:
        raise ZeroDivisionError("0 has no inverse in F_4")
    for candidate in range(1, 4):
        if f4_mul(a, candidate) == 1:
            return candidate
    raise AssertionError("unreachable")


def f4_div(a: int, b: int) -> int:
    return f4_mul(a, f4_inv(b))


def f4_square(a: int) -> int:
    return f4_mul(a, a)


def f4u2_add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return (f4_add(x[0], y[0]), f4_add(x[1], y[1]))


def f4u2_mul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    a, b = x
    c, d = y
    return (f4_mul(a, c), f4_add(f4_mul(a, d), f4_mul(b, c)))


def f4u2_frobenius(x: tuple[int, int]) -> tuple[int, int]:
    return (f4_square(x[0]), f4_square(x[1]))


def f4u2_conductor(x: Label) -> str:
    lead, tail = x  # type: ignore[misc]
    if (lead, tail) == (0, 0):
        return "1"
    if lead == 0:
        return "u"
    return "u^2"


def f4u2_conductor_letter(x: Label) -> str:
    return "T" if f4u2_conductor(x) == "u" else "W"


def f4u2_label_name(x: Label) -> str:
    lead, tail = x  # type: ignore[misc]
    if (lead, tail) == (0, 0):
        return "0"
    if tail == 0:
        return F4_NAMES[lead]
    nil_names = {1: "u", 2: "wu", 3: "(w+1)u"}
    if lead == 0:
        return nil_names[tail]
    return f"{F4_NAMES[lead]}+{nil_names[tail]}"


def f4u2_normalizer_actions(labels: tuple[tuple[int, int], ...]) -> tuple[NormalizerAction, ...]:
    actions: list[NormalizerAction] = []
    seen: set[tuple[tuple[int, int], ...]] = set()
    for leading_unit in range(1, 4):
        for nilpotent_unit in range(4):
            unit = (leading_unit, nilpotent_unit)
            for frob in (False, True):
                images = []
                for label in labels:
                    image = f4u2_mul(unit, label)
                    if frob:
                        image = f4u2_frobenius(image)
                    images.append(image)
                signature = tuple(images)
                if signature in seen:
                    continue
                seen.add(signature)
                actions.append(
                    NormalizerAction(
                        name=(
                            f"unit={f4u2_label_name(unit)}"
                            + (";frob" if frob else "")
                        ),
                        images=signature,
                    )
                )
    return tuple(actions)


def f4u2_signature(cell: tuple[Label, ...]) -> tuple[tuple[object, ...], ...]:
    labels = tuple(label for label in cell)  # type: ignore[assignment]
    signatures: list[tuple[tuple[object, ...], ...]] = []
    for permutation in permutations(range(len(labels))):
        ordered = tuple(labels[index] for index in permutation)
        wild = [label for label in ordered if f4u2_conductor(label) == "u^2"]
        if not wild:
            signature = tuple(("T",) for _ in ordered)
            signatures.append(signature)
            continue
        base = wild[0]
        base_lead = base[0]
        base_tail_ratio = f4_div(base[1], base_lead)
        coords: list[tuple[object, ...]] = []
        for lead, tail in ordered:
            if lead == 0:
                coords.append(("T", f4_div(tail, base_lead)))
            else:
                coords.append(
                    (
                        "W",
                        f4_div(lead, base_lead),
                        f4_add(f4_div(tail, lead), base_tail_ratio),
                    )
                )
        signature = tuple(coords)
        signatures.append(signature)
        signatures.append(
            tuple(
                (item[0], f4_square(item[1]), f4_square(item[2]))
                if item[0] == "W"
                else (
                    (item[0], f4_square(item[1]))
                    if len(item) == 2
                    else item
                )
                for item in signature
            )
        )
    return min(signatures)


def make_f4_u2_ring() -> FiniteLocalRing:
    labels = tuple((lead, tail) for lead in range(4) for tail in range(4))
    return FiniteLocalRing(
        name="F_4[u]/(u^2)",
        labels=labels,
        zero=(0, 0),
        add=f4u2_add,
        conductor=f4u2_conductor,
        label_name=f4u2_label_name,
        normalizer_actions=f4u2_normalizer_actions(labels),
        conductor_order=("u", "u^2"),
        conductor_letter=f4u2_conductor_letter,
        local_signature=f4u2_signature,
    )


# ---------------------------------------------------------------------------
# F_16 field control


F16_MODULUS = 0b10011
F16_DEGREE = 4


def gf16_add(x: int, y: int) -> int:
    return x ^ y


def gf16_mul(x: int, y: int) -> int:
    product_bits = 0
    left = x
    right = y
    while right:
        if right & 1:
            product_bits ^= left
        right >>= 1
        left <<= 1
    for degree in range(2 * F16_DEGREE - 2, F16_DEGREE - 1, -1):
        if product_bits & (1 << degree):
            product_bits ^= F16_MODULUS << (degree - F16_DEGREE)
    return product_bits & ((1 << F16_DEGREE) - 1)


def gf16_square(x: int) -> int:
    return gf16_mul(x, x)


def gf16_frobenius(x: int, power: int) -> int:
    out = x
    for _ in range(power % F16_DEGREE):
        out = gf16_square(out)
    return out


def gf16_label_name(x: Label) -> str:
    value = int(x)
    if value == 0:
        return "0"
    parts: list[str] = []
    if value & 1:
        parts.append("1")
    if value & 2:
        parts.append("a")
    if value & 4:
        parts.append("a^2")
    if value & 8:
        parts.append("a^3")
    return "+".join(parts)


def gf16_normalizer_actions(labels: tuple[int, ...]) -> tuple[NormalizerAction, ...]:
    actions: list[NormalizerAction] = []
    seen: set[tuple[int, ...]] = set()
    for unit in range(1, 16):
        for frob_power in range(F16_DEGREE):
            images = tuple(gf16_mul(unit, gf16_frobenius(label, frob_power)) for label in labels)
            if images in seen:
                continue
            seen.add(images)
            actions.append(NormalizerAction(name=f"unit={unit};frob={frob_power}", images=images))
    return tuple(actions)


def make_f16_ring() -> FiniteLocalRing:
    labels = tuple(range(16))
    return FiniteLocalRing(
        name="F_16",
        labels=labels,
        zero=0,
        add=gf16_add,
        conductor=lambda label: "field" if label else "1",
        label_name=gf16_label_name,
        normalizer_actions=gf16_normalizer_actions(labels),
        conductor_order=("field",),
        conductor_letter=lambda _label: "F",
    )


# ---------------------------------------------------------------------------
# F_2[u]/(u^4) wild control


F2U4_DEGREE = 4


def f2u4_add(x: int, y: int) -> int:
    return x ^ y


def f2u4_mul(x: int, y: int) -> int:
    out = 0
    for i in range(F2U4_DEGREE):
        if not (x & (1 << i)):
            continue
        for j in range(F2U4_DEGREE - i):
            if y & (1 << j):
                out ^= 1 << (i + j)
    return out


def f2u4_pow(x: int, exponent: int) -> int:
    out = 1
    for _ in range(exponent):
        out = f2u4_mul(out, x)
    return out


def f2u4_substitute_u(label: int, image_u: int) -> int:
    out = 0
    for degree in range(F2U4_DEGREE):
        if label & (1 << degree):
            out ^= f2u4_pow(image_u, degree)
    return out


def f2u4_conductor_exponent(label: Label) -> int:
    value = int(label)
    if value == 0:
        return 0
    for degree in range(F2U4_DEGREE):
        if value & (1 << degree):
            return F2U4_DEGREE - degree
    raise AssertionError("unreachable")


def f2u4_conductor(label: Label) -> str:
    exponent = f2u4_conductor_exponent(label)
    if exponent == 0:
        return "1"
    if exponent == 1:
        return "u"
    return f"u^{exponent}"


def f2u4_label_name(label: Label) -> str:
    value = int(label)
    if value == 0:
        return "0"
    parts: list[str] = []
    for degree in range(F2U4_DEGREE):
        if not (value & (1 << degree)):
            continue
        if degree == 0:
            parts.append("1")
        elif degree == 1:
            parts.append("u")
        else:
            parts.append(f"u^{degree}")
    return "+".join(parts)


def f2u4_unit_action(unit: int, labels: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(f2u4_mul(unit, label) for label in labels)


def f2u4_automorphism_action(image_u: int, labels: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(f2u4_substitute_u(label, image_u) for label in labels)


def f2u4_compose(first: tuple[int, ...], second: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(second[first[label]] for label in range(len(first)))


def f2u4_normalizer_actions(labels: tuple[int, ...]) -> tuple[NormalizerAction, ...]:
    seen: set[tuple[int, ...]] = set()
    actions: list[NormalizerAction] = []
    units = [label for label in labels if label & 1]
    image_us = [0b0010 ^ (a << 2) ^ (b << 3) for a in (0, 1) for b in (0, 1)]
    for unit in units:
        unit_images = f2u4_unit_action(unit, labels)
        for image_u in image_us:
            automorphism_images = f2u4_automorphism_action(image_u, labels)
            images = f2u4_compose(unit_images, automorphism_images)
            if images in seen:
                continue
            seen.add(images)
            actions.append(
                NormalizerAction(
                    name=f"unit={f2u4_label_name(unit)};u->{f2u4_label_name(image_u)}",
                    images=images,
                )
            )
    return tuple(actions)


def make_f2_u4_ring() -> FiniteLocalRing:
    labels = tuple(range(1 << F2U4_DEGREE))
    return FiniteLocalRing(
        name="F_2[u]/(u^4)",
        labels=labels,
        zero=0,
        add=f2u4_add,
        conductor=f2u4_conductor,
        label_name=f2u4_label_name,
        normalizer_actions=f2u4_normalizer_actions(labels),
        conductor_order=("u", "u^2", "u^3", "u^4"),
        conductor_letter=lambda label: str(f2u4_conductor_exponent(label)),
    )
