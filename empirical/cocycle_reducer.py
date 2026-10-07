"""Canonical Ext_CH cocycle reducer for local adjacency constructors.

The local adjacency constructor gives a normalized section of the associated
graded by choosing partial quotient-shifts.  The product of two section
generators can differ from the direct section generator; that finite carry is
the raw Ext_CH 2-cocycle.

This reducer does three things:

1. materialize the raw carry as atom-level 2-cochain data;
2. quotient those atoms and carry pairs by the Hayes normalizer to get a
   deterministic canonical representative;
3. provide a finite linear coboundary engine for explicit section-change
   models.  The default report records the normalized representative; the
   coboundary engine is available when a particular gauge model is selected.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Literal

from local_adjacency_constructor import Label, LocalAdjacencyConstructor, Matrix


GaugeMode = Literal["full_block", "support", "off_support"]
C2Scope = Literal["full_block", "raw_support"]


@dataclass(frozen=True)
class CocycleAtom:
    """One matrix-entry atom of the raw carry 2-cocycle."""

    left_eta: Label
    right_eta: Label
    source: str
    middle: str
    target: str
    output: Label
    input: Label
    coefficient: int

    @property
    def pair_key(self) -> tuple[Label, Label, str, str, str]:
        return (self.left_eta, self.right_eta, self.source, self.middle, self.target)

    @property
    def c2_key(self) -> tuple[Label, Label, str, str, str, Label, Label]:
        return (
            self.left_eta,
            self.right_eta,
            self.source,
            self.middle,
            self.target,
            self.output,
            self.input,
        )

    @property
    def path_word(self) -> str:
        return f"{self.source}->{self.middle}->{self.target}"


@dataclass(frozen=True)
class SectionGenerator:
    """One elementary section-change generator phi(q)."""

    eta: Label
    source: str
    target: str
    output: Label
    input: Label

    @property
    def shift_key(self) -> tuple[Label, str, str]:
        return (self.eta, self.source, self.target)


class CocycleReducer:
    """Reduce raw carry cocycles to canonical finite representatives."""

    def __init__(self, constructor: LocalAdjacencyConstructor) -> None:
        self.constructor = constructor
        self.ring = constructor.ring
        self._composable_pairs = None
        self._pair_indexes = None
        self._raw_atoms = None
        self._section_generators: dict[GaugeMode, tuple[SectionGenerator, ...]] = {}
        self._c2_basis_keys = None
        self._raw_c2_basis_keys = None
        self._full_block_c2_indexer = None

    @property
    def composable_pairs(self):
        if self._composable_pairs is None:
            pairs = []
            for right in self.constructor.shifts:
                for left in self.constructor.shifts_by_source.get(right.target, []):
                    pairs.append((left, right))
            self._composable_pairs = tuple(pairs)
        return self._composable_pairs

    @property
    def pair_indexes(self):
        if self._pair_indexes is None:
            by_right = {}
            by_left = {}
            by_direct = {}
            for left, right in self.composable_pairs:
                right_key = (right.eta, right.source, right.target)
                left_key = (left.eta, left.source, left.target)
                direct_key = (self.ring.add(left.eta, right.eta), right.source, left.target)
                by_right.setdefault(right_key, []).append((left, right))
                by_left.setdefault(left_key, []).append((left, right))
                by_direct.setdefault(direct_key, []).append((left, right))
            self._pair_indexes = (
                {key: tuple(value) for key, value in by_right.items()},
                {key: tuple(value) for key, value in by_left.items()},
                {key: tuple(value) for key, value in by_direct.items()},
            )
        return self._pair_indexes

    def label_key(self, label: Label) -> tuple[str, str]:
        return (self.ring.conductor(label), self.ring.label_name(label))

    def atom_sort_key(self, atom: CocycleAtom) -> tuple[object, ...]:
        return (
            atom.path_word,
            self.label_key(atom.left_eta),
            self.label_key(atom.right_eta),
            self.label_key(atom.output),
            self.label_key(atom.input),
            atom.coefficient,
        )

    def c2_sort_key(self, key: tuple[Label, Label, str, str, str, Label, Label]) -> tuple[object, ...]:
        left_eta, right_eta, source, middle, target, output, input_label = key
        return (
            f"{source}->{middle}->{target}",
            self.label_key(left_eta),
            self.label_key(right_eta),
            self.label_key(output),
            self.label_key(input_label),
        )

    def pair_sort_key(self, key: tuple[Label, Label, str, str, str]) -> tuple[object, ...]:
        left_eta, right_eta, source, middle, target = key
        return (
            f"{source}->{middle}->{target}",
            self.label_key(left_eta),
            self.label_key(right_eta),
        )

    def raw_atoms(self) -> tuple[CocycleAtom, ...]:
        if self._raw_atoms is not None:
            return self._raw_atoms

        atoms: list[CocycleAtom] = []
        for left, right in self.composable_pairs:
            product_matrix = self.constructor.matrix_mul(
                self.constructor.matrix_from_tuple(left.matrix),
                self.constructor.matrix_from_tuple(right.matrix),
            )
            direct_eta = self.ring.add(left.eta, right.eta)
            direct = self.constructor.shift_by_key.get((direct_eta, right.source, left.target))
            direct_matrix = self.constructor.matrix_from_tuple(direct.matrix) if direct else {}
            delta = self.constructor.matrix_sub(product_matrix, direct_matrix)
            for (output, input_label), coefficient in delta.items():
                atoms.append(
                    CocycleAtom(
                        left_eta=left.eta,
                        right_eta=right.eta,
                        source=right.source,
                        middle=right.target,
                        target=left.target,
                        output=output,
                        input=input_label,
                        coefficient=coefficient,
                    )
                )
        self._raw_atoms = tuple(sorted(atoms, key=self.atom_sort_key))
        return self._raw_atoms

    def raw_vector(self) -> dict[tuple[Label, Label, str, str, str, Label, Label], Fraction]:
        return {atom.c2_key: Fraction(atom.coefficient) for atom in self.raw_atoms()}

    def transform_atom(self, atom: CocycleAtom, action) -> CocycleAtom:
        return CocycleAtom(
            left_eta=self.ring.apply(action, atom.left_eta),
            right_eta=self.ring.apply(action, atom.right_eta),
            source=atom.source,
            middle=atom.middle,
            target=atom.target,
            output=self.ring.apply(action, atom.output),
            input=self.ring.apply(action, atom.input),
            coefficient=atom.coefficient,
        )

    def transform_pair(
        self,
        pair_key: tuple[Label, Label, str, str, str],
        action,
    ) -> tuple[Label, Label, str, str, str]:
        left_eta, right_eta, source, middle, target = pair_key
        return (
            self.ring.apply(action, left_eta),
            self.ring.apply(action, right_eta),
            source,
            middle,
            target,
        )

    def atom_orbits(self) -> list[dict[str, object]]:
        atoms = self.raw_atoms()
        atom_set = set(atoms)
        remaining = set(atoms)
        orbits: list[dict[str, object]] = []

        while remaining:
            seed = min(remaining, key=self.atom_sort_key)
            ambient = {self.transform_atom(seed, action) for action in self.ring.normalizer_actions}
            present = ambient & atom_set
            representative = min(present, key=self.atom_sort_key)
            coefficients = Counter(atom.coefficient for atom in present)
            orbits.append(
                {
                    "representative": representative,
                    "size": len(present),
                    "ambient_size": len(ambient),
                    "missing": len(ambient - atom_set),
                    "coefficients": coefficients,
                    "path": representative.path_word,
                }
            )
            remaining -= present

        return sorted(orbits, key=lambda orbit: self.atom_sort_key(orbit["representative"]))

    def pair_orbits(self) -> list[dict[str, object]]:
        pair_to_atoms: dict[tuple[Label, Label, str, str, str], list[CocycleAtom]] = {}
        for atom in self.raw_atoms():
            pair_to_atoms.setdefault(atom.pair_key, []).append(atom)

        pair_set = set(pair_to_atoms)
        remaining = set(pair_set)
        orbits: list[dict[str, object]] = []

        while remaining:
            seed = min(remaining, key=self.pair_sort_key)
            ambient = {self.transform_pair(seed, action) for action in self.ring.normalizer_actions}
            present = ambient & pair_set
            representative = min(present, key=self.pair_sort_key)
            atom_count = sum(len(pair_to_atoms[pair]) for pair in present)
            coefficient_counter: Counter[int] = Counter()
            for pair in present:
                coefficient_counter.update(atom.coefficient for atom in pair_to_atoms[pair])
            orbits.append(
                {
                    "representative": representative,
                    "size": len(present),
                    "ambient_size": len(ambient),
                    "missing": len(ambient - pair_set),
                    "atom_count": atom_count,
                    "coefficients": coefficient_counter,
                    "path": f"{representative[2]}->{representative[3]}->{representative[4]}",
                }
            )
            remaining -= present

        return sorted(orbits, key=lambda orbit: self.pair_sort_key(orbit["representative"]))

    def section_generators(self, mode: GaugeMode) -> tuple[SectionGenerator, ...]:
        cached = self._section_generators.get(mode)
        if cached is not None:
            return cached

        generators: list[SectionGenerator] = []
        for shift in self.constructor.shifts:
            support = set(shift.matrix)
            for output in self.constructor.packets[shift.target]:
                for input_label in self.constructor.packets[shift.source]:
                    entry = (output, input_label)
                    if mode == "support" and entry not in support:
                        continue
                    if mode == "off_support" and entry in support:
                        continue
                    generators.append(
                        SectionGenerator(
                            eta=shift.eta,
                            source=shift.source,
                            target=shift.target,
                            output=output,
                            input=input_label,
                        )
                    )
        self._section_generators[mode] = tuple(generators)
        return self._section_generators[mode]

    def c2_basis_keys(self) -> tuple[tuple[Label, Label, str, str, str, Label, Label], ...]:
        if self._c2_basis_keys is not None:
            return self._c2_basis_keys

        keys = []
        for left, right in self.composable_pairs:
            for output in self.constructor.packets[left.target]:
                for input_label in self.constructor.packets[right.source]:
                    keys.append(
                        (
                            left.eta,
                            right.eta,
                            right.source,
                            right.target,
                            left.target,
                            output,
                            input_label,
                        )
                    )
        self._c2_basis_keys = tuple(sorted(keys, key=self.c2_sort_key))
        return self._c2_basis_keys

    def full_block_c2_indexer(
        self,
    ) -> tuple[
        int,
        Callable[[tuple[Label, Label, str, str, str, Label, Label]], int],
    ]:
        """Return the full C2 dimension and an implicit row-index map.

        The stress rows have tens of millions of full-block C2 coordinates.
        Materializing those keys as Python tuples is unnecessary: the global
        order is lexicographic by carry pair, then output label, then input
        label.  This indexer reproduces that order from per-pair offsets.
        """

        if self._full_block_c2_indexer is not None:
            return self._full_block_c2_indexer

        pair_keys = [
            (left.eta, right.eta, right.source, right.target, left.target)
            for left, right in self.composable_pairs
        ]
        pair_keys.sort(key=self.pair_sort_key)

        offsets: dict[
            tuple[Label, Label, str, str, str],
            tuple[int, dict[Label, int], dict[Label, int], int],
        ] = {}
        offset = 0
        for pair_key in pair_keys:
            _left_eta, _right_eta, source, _middle, target = pair_key
            outputs = self.constructor.packets[target]
            inputs = self.constructor.packets[source]
            output_indexes = {label: index for index, label in enumerate(outputs)}
            input_indexes = {label: index for index, label in enumerate(inputs)}
            offsets[pair_key] = (offset, output_indexes, input_indexes, len(inputs))
            offset += len(outputs) * len(inputs)

        def indexer(
            key: tuple[Label, Label, str, str, str, Label, Label],
        ) -> int:
            pair_key = key[:5]
            output = key[5]
            input_label = key[6]
            base, output_indexes, input_indexes, input_count = offsets[pair_key]
            return base + output_indexes[output] * input_count + input_indexes[input_label]

        self._full_block_c2_indexer = (offset, indexer)
        return self._full_block_c2_indexer

    def raw_c2_basis_keys(self) -> tuple[tuple[Label, Label, str, str, str, Label, Label], ...]:
        if self._raw_c2_basis_keys is None:
            self._raw_c2_basis_keys = tuple(
                sorted(self.raw_vector(), key=self.c2_sort_key)
            )
        return self._raw_c2_basis_keys

    def scoped_c2_basis_keys(
        self,
        scope: C2Scope,
    ) -> tuple[tuple[Label, Label, str, str, str, Label, Label], ...]:
        if scope == "full_block":
            return self.c2_basis_keys()
        if scope == "raw_support":
            return self.raw_c2_basis_keys()
        raise ValueError(f"unknown C2 scope: {scope}")

    def scoped_c2_indexer(
        self,
        scope: C2Scope,
    ) -> tuple[
        int,
        Callable[[tuple[Label, Label, str, str, str, Label, Label]], int | None],
    ]:
        if scope == "full_block":
            dimension, full_indexer = self.full_block_c2_indexer()
            return dimension, full_indexer
        if scope == "raw_support":
            c2_keys = self.raw_c2_basis_keys()
            key_to_index = {key: index for index, key in enumerate(c2_keys)}
            return len(c2_keys), key_to_index.get
        raise ValueError(f"unknown C2 scope: {scope}")

    def _add_matrix_to_column(
        self,
        column: dict[tuple[Label, Label, str, str, str, Label, Label], Fraction],
        *,
        pair_key: tuple[Label, Label, str, str, str],
        matrix: Matrix,
        sign: int,
    ) -> None:
        left_eta, right_eta, source, middle, target = pair_key
        for (output, input_label), value in matrix.items():
            key = (left_eta, right_eta, source, middle, target, output, input_label)
            column[key] = column.get(key, Fraction(0)) + sign * Fraction(value)
            if not column[key]:
                del column[key]

    def coboundary_column(
        self,
        generator: SectionGenerator,
    ) -> dict[tuple[Label, Label, str, str, str, Label, Label], Fraction]:
        """Linearized section-change coboundary for one phi generator."""

        column: dict[tuple[Label, Label, str, str, str, Label, Label], Fraction] = {}
        elementary = {(generator.output, generator.input): 1}
        generator_shift_key = generator.shift_key
        by_right, by_left, by_direct = self.pair_indexes

        for left, right in by_right.get(generator_shift_key, ()):
            pair_key = (left.eta, right.eta, right.source, right.target, left.target)
            matrix = self.constructor.matrix_mul(
                self.constructor.matrix_from_tuple(left.matrix),
                elementary,
            )
            self._add_matrix_to_column(column, pair_key=pair_key, matrix=matrix, sign=1)

        for left, right in by_left.get(generator_shift_key, ()):
            pair_key = (left.eta, right.eta, right.source, right.target, left.target)
            matrix = self.constructor.matrix_mul(
                elementary,
                self.constructor.matrix_from_tuple(right.matrix),
            )
            self._add_matrix_to_column(column, pair_key=pair_key, matrix=matrix, sign=1)

        for left, right in by_direct.get(generator_shift_key, ()):
            pair_key = (left.eta, right.eta, right.source, right.target, left.target)
            self._add_matrix_to_column(column, pair_key=pair_key, matrix=elementary, sign=-1)

        return column

    @staticmethod
    def _reduce_vector(
        vector: dict[int, Fraction],
        basis: dict[int, dict[int, Fraction]],
    ) -> dict[int, Fraction]:
        vector = dict(vector)
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                break
            coefficient = vector[pivot]
            for index, value in basis[pivot].items():
                vector[index] = vector.get(index, Fraction(0)) - coefficient * value
                if not vector[index]:
                    del vector[index]
        return vector

    @staticmethod
    def _reduce_vector_mod(
        vector: dict[int, int],
        basis: dict[int, dict[int, int]],
        modulus: int,
    ) -> dict[int, int]:
        vector = {index: value % modulus for index, value in vector.items() if value % modulus}
        while vector:
            pivot = min(vector)
            row = basis.get(pivot)
            if row is None:
                break
            coefficient = vector[pivot]
            for index, value in row.items():
                updated = (vector.get(index, 0) - coefficient * value) % modulus
                if updated:
                    vector[index] = updated
                else:
                    vector.pop(index, None)
        return vector

    def coboundary_reduction(
        self,
        mode: GaugeMode,
        *,
        c2_scope: C2Scope = "full_block",
        field_modulus: int | None = None,
    ) -> dict[str, object]:
        """Compute rank and normal form of the raw cocycle for a gauge model."""

        c2_dimension, c2_index = self.scoped_c2_indexer(c2_scope)

        if field_modulus is not None:
            basis_mod: dict[int, dict[int, int]] = {}
            for generator in self.section_generators(mode):
                column: dict[int, int] = {}
                for key, value in self.coboundary_column(generator).items():
                    index = c2_index(key)
                    if index is None:
                        continue
                    entry = int(value) % field_modulus
                    if entry:
                        column[index] = (column.get(index, 0) + entry) % field_modulus
                        if not column[index]:
                            del column[index]
                reduced = self._reduce_vector_mod(column, basis_mod, field_modulus)
                if not reduced:
                    continue
                pivot = min(reduced)
                pivot_value = reduced[pivot]
                inverse = pow(pivot_value, -1, field_modulus)
                basis_mod[pivot] = {
                    index: (value * inverse) % field_modulus
                    for index, value in reduced.items()
                    if (value * inverse) % field_modulus
                }

            raw_mod: dict[int, int] = {}
            for key, value in self.raw_vector().items():
                index = c2_index(key)
                if index is None:
                    continue
                entry = int(value) % field_modulus
                if entry:
                    raw_mod[index] = (raw_mod.get(index, 0) + entry) % field_modulus
                    if not raw_mod[index]:
                        del raw_mod[index]
            residual_mod = self._reduce_vector_mod(raw_mod, basis_mod, field_modulus)
            rational_rank_certified = len(basis_mod) == len(self.section_generators(mode))

            return {
                "mode": mode,
                "c2_scope": c2_scope,
                "coefficient_field": f"F_{field_modulus}",
                "c1_generators": len(self.section_generators(mode)),
                "c2_dimension": c2_dimension,
                "coboundary_rank": len(basis_mod),
                "residual_dimension": c2_dimension - len(basis_mod),
                "raw_support": len(raw_mod),
                "residual_support": len(residual_mod),
                "residual_equal_raw": residual_mod == raw_mod,
                "raw_is_coboundary": len(residual_mod) == 0,
                "rational_rank_certified": rational_rank_certified,
                "raw_non_coboundary_over_q_certified": (
                    rational_rank_certified and len(residual_mod) > 0
                ),
            }

        basis: dict[int, dict[int, Fraction]] = {}
        for generator in self.section_generators(mode):
            column: dict[int, Fraction] = {}
            for key, value in self.coboundary_column(generator).items():
                index = c2_index(key)
                if index is None:
                    continue
                column[index] = column.get(index, Fraction(0)) + value
                if not column[index]:
                    del column[index]
            reduced = self._reduce_vector(column, basis)
            if not reduced:
                continue
            pivot = min(reduced)
            pivot_value = reduced[pivot]
            basis[pivot] = {index: value / pivot_value for index, value in reduced.items()}

        raw: dict[int, Fraction] = {}
        for key, value in self.raw_vector().items():
            index = c2_index(key)
            if index is None:
                continue
            raw[index] = raw.get(index, Fraction(0)) + value
            if not raw[index]:
                del raw[index]
        residual = self._reduce_vector(raw, basis)

        return {
            "mode": mode,
            "c2_scope": c2_scope,
            "coefficient_field": "Q",
            "c1_generators": len(self.section_generators(mode)),
            "c2_dimension": c2_dimension,
            "coboundary_rank": len(basis),
            "residual_dimension": c2_dimension - len(basis),
            "raw_support": len(raw),
            "residual_support": len(residual),
            "residual_equal_raw": residual == raw,
            "raw_is_coboundary": len(residual) == 0,
            "rational_rank_certified": True,
            "raw_non_coboundary_over_q_certified": len(residual) > 0,
        }

    def atom_json(self, atom: CocycleAtom) -> dict[str, object]:
        return {
            "left_eta": self.ring.label_name(atom.left_eta),
            "right_eta": self.ring.label_name(atom.right_eta),
            "source": atom.source,
            "middle": atom.middle,
            "target": atom.target,
            "output": self.ring.label_name(atom.output),
            "input": self.ring.label_name(atom.input),
            "coefficient": atom.coefficient,
        }

    def pair_json(self, pair: tuple[Label, Label, str, str, str]) -> dict[str, object]:
        left_eta, right_eta, source, middle, target = pair
        return {
            "left_eta": self.ring.label_name(left_eta),
            "right_eta": self.ring.label_name(right_eta),
            "source": source,
            "middle": middle,
            "target": target,
        }

    @staticmethod
    def counter_json(counter: Counter[int]) -> dict[str, int]:
        return {str(key): counter[key] for key in sorted(counter)}

    def summary(self, *, coboundary_mode: GaugeMode | None = None) -> dict[str, object]:
        atoms = self.raw_atoms()
        atom_orbits = self.atom_orbits()
        pair_orbits = self.pair_orbits()
        raw_pairs = {atom.pair_key for atom in atoms}
        payload: dict[str, object] = {
            "ring": self.ring.name,
            "gamma_size": len(self.ring.normalizer_actions),
            "raw_atom_count": len(atoms),
            "raw_pair_count": len(raw_pairs),
            "raw_coefficient_distribution": self.counter_json(
                Counter(atom.coefficient for atom in atoms)
            ),
            "raw_path_distribution": dict(
                sorted(Counter(atom.path_word for atom in atoms).items())
            ),
            "atom_orbit_count": len(atom_orbits),
            "atom_orbit_size_distribution": dict(
                sorted(Counter(int(orbit["size"]) for orbit in atom_orbits).items())
            ),
            "atom_orbit_missing_total": sum(int(orbit["missing"]) for orbit in atom_orbits),
            "pair_orbit_count": len(pair_orbits),
            "pair_orbit_size_distribution": dict(
                sorted(Counter(int(orbit["size"]) for orbit in pair_orbits).items())
            ),
            "pair_orbit_missing_total": sum(int(orbit["missing"]) for orbit in pair_orbits),
            "canonical_atom_orbits": [
                {
                    "representative": self.atom_json(orbit["representative"]),
                    "size": orbit["size"],
                    "coefficients": self.counter_json(orbit["coefficients"]),
                    "path": orbit["path"],
                }
                for orbit in atom_orbits
            ],
            "canonical_pair_orbits": [
                {
                    "representative": self.pair_json(orbit["representative"]),
                    "size": orbit["size"],
                    "atom_count": orbit["atom_count"],
                    "coefficients": self.counter_json(orbit["coefficients"]),
                    "path": orbit["path"],
                }
                for orbit in pair_orbits
            ],
        }
        if coboundary_mode is not None:
            payload["coboundary_reduction"] = self.coboundary_reduction(coboundary_mode)
        return payload


def render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Ext_CH Cocycle Reducer",
        "",
        f"- ring: {payload['ring']}",
        f"- Gamma size: {payload['gamma_size']}",
        f"- raw atom count: {payload['raw_atom_count']}",
        f"- raw carry pair count: {payload['raw_pair_count']}",
        f"- atom orbit count: {payload['atom_orbit_count']}",
        f"- pair orbit count: {payload['pair_orbit_count']}",
        f"- atom orbit missing total: {payload['atom_orbit_missing_total']}",
        f"- pair orbit missing total: {payload['pair_orbit_missing_total']}",
        f"- raw coefficient distribution: {payload['raw_coefficient_distribution']}",
        "",
        "## Raw Path Distribution",
        "",
    ]
    for path, count in payload["raw_path_distribution"].items():
        lines.append(f"- {path}: {count}")

    lines += [
        "",
        "## Canonical Pair-Orbit Representative Table",
        "",
        "| orbit | size | atoms | path | representative | coeffs |",
        "|---:|---:|---:|---|---|---|",
    ]

    for index, orbit in enumerate(payload["canonical_pair_orbits"], 1):
        rep = orbit["representative"]
        rep_text = (
            f"{rep['left_eta']} <- {rep['right_eta']} "
            f"({rep['source']}->{rep['middle']}->{rep['target']})"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(index),
                    str(orbit["size"]),
                    str(orbit["atom_count"]),
                    str(orbit["path"]),
                    "`" + rep_text + "`",
                    "`" + str(orbit["coefficients"]) + "`",
                ]
            )
            + " |"
        )

    if "coboundary_reduction" in payload:
        reduction = payload["coboundary_reduction"]
        lines += [
            "",
            "## Coboundary Reduction",
            "",
            f"- mode: {reduction['mode']}",
            f"- C1 generators: {reduction['c1_generators']}",
            f"- C2 dimension: {reduction['c2_dimension']}",
            f"- coboundary rank: {reduction['coboundary_rank']}",
            f"- raw support: {reduction['raw_support']}",
            f"- residual support: {reduction['residual_support']}",
            f"- raw is coboundary: {reduction['raw_is_coboundary']}",
        ]

    lines += [
        "",
        "## Interpretation",
        "",
        "The canonical pair-orbit table is the normalized Ext_CH representative",
        "for the current section of the filtered adjacency algebra.  The",
        "coboundary engine is explicit and finite; a selected gauge model can be",
        "used to test which section changes preserve or trivialize the carry.",
        "",
    ]
    return "\n".join(lines)


def write_reports(
    payload: dict[str, object],
    *,
    json_path: Path,
    markdown_path: Path,
) -> None:
    import json

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    markdown_path.write_text(render_markdown(payload), encoding="utf-8")
