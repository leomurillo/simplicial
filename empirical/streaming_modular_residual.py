"""Streaming modular residual reducer for large selected conductor leaves.

The ordinary per-leaf audit is intentionally simple and exact over Q.  This
script is the large-row companion: it works over a finite field, builds sparse
coboundary columns directly from quotient-shift incidence data, and decodes
only the final residual support into normalizer-orbit classes.

The output is modular residual evidence, not a rational finite-closure proof.
It is designed for rows such as F_2[u]/(u^6) and F_8[u]/(u^2), where the C2
coordinate volume is too large for the default exact audit.
"""

from __future__ import annotations

import argparse
import bisect
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any

from cocycle_reducer import CocycleReducer, SectionGenerator
from local_adjacency_constructor import (
    Label,
    LocalAdjacencyConstructor,
    QuotientShift,
    make_f8_u2_ring,
)
from per_leaf_coboundary_audit import (
    C2Key,
    c2_orbit_quotient,
    c2_volume_normalized_masses,
    canonical_c2_key,
    generator_in_leaf,
    leaf_pair_keys,
    orbit_volume_normalized_masses,
    path_in_leaf,
    split_leaf,
)
from tower_quotient_saturation import make_f2_u_ring, suffix_leaf


ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "empirical" / "reports"


TARGETS = {
    "f2-u6": ("F_2[u]/(u^6)", "u^5+u^6"),
    "f8-u2": ("F_8[u]/(u^2)", "u^2"),
}


@dataclass(frozen=True)
class PairBlock:
    base: int
    pair_key: tuple[Label, Label, str, str, str]
    outputs: tuple[Label, ...]
    inputs: tuple[Label, ...]

    @property
    def size(self) -> int:
        return len(self.outputs) * len(self.inputs)


class LeafC2Codec:
    def __init__(self, reducer: CocycleReducer, leaf: set[str]) -> None:
        constructor = reducer.constructor
        blocks: list[PairBlock] = []
        offsets: dict[
            tuple[Label, Label, str, str, str],
            tuple[int, dict[Label, int], dict[Label, int], int],
        ] = {}
        offset = 0
        for pair_key in leaf_pair_keys(reducer, leaf):
            _left_eta, _right_eta, source, _middle, target = pair_key
            outputs = constructor.packets[target]
            inputs = constructor.packets[source]
            output_indexes = {label: index for index, label in enumerate(outputs)}
            input_indexes = {label: index for index, label in enumerate(inputs)}
            offsets[pair_key] = (offset, output_indexes, input_indexes, len(inputs))
            blocks.append(PairBlock(offset, pair_key, outputs, inputs))
            offset += len(outputs) * len(inputs)

        self.dimension = offset
        self.pair_count = len(blocks)
        self.blocks = tuple(blocks)
        self.bases = tuple(block.base for block in blocks)
        self.offsets = offsets

    def index(self, key: C2Key) -> int | None:
        item = self.offsets.get(key[:5])
        if item is None:
            return None
        base, output_indexes, input_indexes, input_count = item
        output_index = output_indexes.get(key[5])
        input_index = input_indexes.get(key[6])
        if output_index is None or input_index is None:
            return None
        return base + output_index * input_count + input_index

    def decode(self, index: int) -> C2Key:
        block_position = bisect.bisect_right(self.bases, index) - 1
        if block_position < 0:
            raise IndexError(index)
        block = self.blocks[block_position]
        local = index - block.base
        if local < 0 or local >= block.size:
            raise IndexError(index)
        input_count = len(block.inputs)
        output_index, input_index = divmod(local, input_count)
        left_eta, right_eta, source, middle, target = block.pair_key
        return (
            left_eta,
            right_eta,
            source,
            middle,
            target,
            block.outputs[output_index],
            block.inputs[input_index],
        )


@dataclass(frozen=True)
class ShiftLookup:
    outputs_by_input: dict[Label, tuple[Label, ...]]
    inputs_by_output: dict[Label, tuple[Label, ...]]


def make_constructor(target: str) -> tuple[str, str, LocalAdjacencyConstructor]:
    if target == "f2-u6":
        ring_name, leaf_name = TARGETS[target]
        return ring_name, leaf_name, LocalAdjacencyConstructor(make_f2_u_ring(6))
    if target == "f8-u2":
        ring_name, leaf_name = TARGETS[target]
        return ring_name, leaf_name, LocalAdjacencyConstructor(make_f8_u2_ring())
    raise ValueError(f"unknown target: {target}")


def shift_key(shift: QuotientShift) -> tuple[Label, str, str]:
    return (shift.eta, shift.source, shift.target)


def build_shift_lookups(constructor: LocalAdjacencyConstructor) -> dict[tuple[Label, str, str], ShiftLookup]:
    lookups: dict[tuple[Label, str, str], ShiftLookup] = {}
    for shift in constructor.shifts:
        outputs_by_input: dict[Label, list[Label]] = {}
        inputs_by_output: dict[Label, list[Label]] = {}
        for output, input_label in shift.matrix:
            outputs_by_input.setdefault(input_label, []).append(output)
            inputs_by_output.setdefault(output, []).append(input_label)
        lookups[shift_key(shift)] = ShiftLookup(
            outputs_by_input={
                label: tuple(values)
                for label, values in outputs_by_input.items()
            },
            inputs_by_output={
                label: tuple(values)
                for label, values in inputs_by_output.items()
            },
        )
    return lookups


def add_mod_entry(
    column: dict[int, int],
    *,
    index: int | None,
    sign: int,
    modulus: int,
) -> None:
    if index is None:
        return
    entry = sign % modulus
    if not entry:
        return
    column[index] = (column.get(index, 0) + entry) % modulus
    if not column[index]:
        del column[index]


def fast_coboundary_column_mod(
    reducer: CocycleReducer,
    generator: SectionGenerator,
    codec: LeafC2Codec,
    shift_lookups: dict[tuple[Label, str, str], ShiftLookup],
    modulus: int,
) -> dict[int, int]:
    column: dict[int, int] = {}
    by_right, by_left, by_direct = reducer.pair_indexes
    generator_key = generator.shift_key

    for left, right in by_right.get(generator_key, ()):
        lookup = shift_lookups[shift_key(left)]
        for output in lookup.outputs_by_input.get(generator.output, ()):
            add_mod_entry(
                column,
                index=codec.index(
                    (
                        left.eta,
                        right.eta,
                        right.source,
                        right.target,
                        left.target,
                        output,
                        generator.input,
                    )
                ),
                sign=1,
                modulus=modulus,
            )

    for left, right in by_left.get(generator_key, ()):
        lookup = shift_lookups[shift_key(right)]
        for input_label in lookup.inputs_by_output.get(generator.input, ()):
            add_mod_entry(
                column,
                index=codec.index(
                    (
                        left.eta,
                        right.eta,
                        right.source,
                        right.target,
                        left.target,
                        generator.output,
                        input_label,
                    )
                ),
                sign=1,
                modulus=modulus,
            )

    for left, right in by_direct.get(generator_key, ()):
        add_mod_entry(
            column,
            index=codec.index(
                (
                    left.eta,
                    right.eta,
                    right.source,
                    right.target,
                    left.target,
                    generator.output,
                    generator.input,
                )
            ),
            sign=-1,
            modulus=modulus,
        )

    return column


def reduce_vector_mod(
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


def normalize_row_mod(vector: dict[int, int], modulus: int) -> tuple[int, dict[int, int]]:
    pivot = min(vector)
    inverse = pow(vector[pivot], -1, modulus)
    return pivot, {
        index: (value * inverse) % modulus
        for index, value in vector.items()
        if (value * inverse) % modulus
    }


def raw_vector_mod(
    reducer: CocycleReducer,
    leaf: set[str],
    codec: LeafC2Codec,
    modulus: int,
) -> tuple[dict[int, int], dict[int, C2Key]]:
    raw: dict[int, int] = {}
    raw_keys_by_index: dict[int, C2Key] = {}
    for key, value in reducer.raw_vector().items():
        if not path_in_leaf(key, leaf):
            continue
        index = codec.index(key)
        if index is None:
            continue
        entry = int(value) % modulus
        if not entry:
            continue
        raw[index] = (raw.get(index, 0) + entry) % modulus
        raw_keys_by_index[index] = key
        if not raw[index]:
            del raw[index]
            raw_keys_by_index.pop(index, None)
    return raw, raw_keys_by_index


def orbit_support_count_from_indexes(
    reducer: CocycleReducer,
    indexes: set[int] | dict[int, Any],
    codec: LeafC2Codec,
    *,
    known_keys: dict[int, C2Key] | None = None,
) -> int:
    known_keys = known_keys or {}
    return len(
        {
            canonical_c2_key(reducer, known_keys.get(index) or codec.decode(index))
            for index in indexes
        }
    )


def reduce_leaf_modular(
    target: str,
    *,
    modulus: int,
    max_generators: int | None,
    progress_every: int,
    orbit_quotient_limit: int,
) -> dict[str, Any]:
    started = perf_counter()
    ring_name, leaf_name, constructor = make_constructor(target)
    reducer = CocycleReducer(constructor)
    leaf = set(split_leaf(leaf_name))
    codec = LeafC2Codec(reducer, leaf)
    orbit_summary, _keys_by_index = c2_orbit_quotient(
        reducer,
        leaf,
        orbit_quotient_limit=orbit_quotient_limit,
    )
    c2_orbit_volume = int(orbit_summary["c2_orbit_quotient_volume"])
    shift_lookups = build_shift_lookups(constructor)
    generators = [
        generator
        for generator in reducer.section_generators("full_block")
        if generator_in_leaf(generator, leaf)
    ]
    if max_generators is not None:
        generators = generators[:max_generators]

    basis: dict[int, dict[int, int]] = {}
    row_size_counter: Counter[int] = Counter()
    column_size_counter: Counter[int] = Counter()
    zero_columns = 0
    processed = 0
    for generator in generators:
        processed += 1
        column = fast_coboundary_column_mod(
            reducer,
            generator,
            codec,
            shift_lookups,
            modulus,
        )
        column_size_counter[len(column)] += 1
        if not column:
            zero_columns += 1
            continue
        reduced = reduce_vector_mod(column, basis, modulus)
        if not reduced:
            continue
        pivot, row = normalize_row_mod(reduced, modulus)
        basis[pivot] = row
        row_size_counter[len(row)] += 1
        if progress_every and processed % progress_every == 0:
            print(
                json.dumps(
                    {
                        "target": target,
                        "processed_generators": processed,
                        "basis_rank": len(basis),
                        "last_pivot": pivot,
                        "elapsed_seconds": round(perf_counter() - started, 3),
                    }
                ),
                flush=True,
            )

    raw, raw_keys_by_index = raw_vector_mod(reducer, leaf, codec, modulus)
    residual = reduce_vector_mod(raw, basis, modulus)
    raw_orbits = orbit_support_count_from_indexes(
        reducer,
        raw,
        codec,
        known_keys=raw_keys_by_index,
    )
    residual_orbits = orbit_support_count_from_indexes(reducer, residual, codec)
    masses = c2_volume_normalized_masses(len(raw), len(residual), codec.dimension)
    row = {
        "target": target,
        "ring": ring_name,
        "leaf": leaf_name,
        "coefficient_field": f"F_{modulus}",
        "modular_residual_status": "complete" if max_generators is None else "generator_limited",
        "processed_generators": processed,
        "total_leaf_generators": len(
            [
                generator
                for generator in reducer.section_generators("full_block")
                if generator_in_leaf(generator, leaf)
            ]
        ),
        "c2_dimension": codec.dimension,
        "leaf_pair_count": codec.pair_count,
        "coboundary_rank": len(basis),
        "residual_dimension": codec.dimension - len(basis),
        "raw_support": len(raw),
        "residual_support": len(residual),
        "residual_deficit": 0.0 if len(raw) == 0 else len(residual) / len(raw),
        "raw_orbit_quotient_support": raw_orbits,
        "residual_orbit_quotient_support": residual_orbits,
        **orbit_summary,
        **orbit_volume_normalized_masses(raw_orbits, residual_orbits, c2_orbit_volume),
        **masses,
        "raw_is_coboundary": len(residual) == 0,
        "residual_equal_raw": residual == raw,
        "zero_columns": zero_columns,
        "column_size_distribution": dict(sorted(column_size_counter.items())),
        "basis_row_size_distribution": dict(sorted(row_size_counter.items())),
        "elapsed_seconds": round(perf_counter() - started, 3),
        "interpretation": (
            "modular full-block residual orbit data; not a rational closure proof"
        ),
    }
    return row


def json_ready(obj: Any) -> Any:
    if isinstance(obj, float):
        return round(obj, 12)
    if isinstance(obj, list):
        return [json_ready(item) for item in obj]
    if isinstance(obj, dict):
        return {str(key): json_ready(value) for key, value in obj.items()}
    return obj


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def make_report(rows: list[dict[str, Any]], output_json: Path) -> str:
    lines = [
        "# Streaming Modular Residual Audit",
        "",
        f"- JSON artifact: `{output_json}`",
        "- Scope: selected conductor leaf, full-block C2 coordinates, full-block section changes inside the leaf.",
        "- Coefficients are finite-field modular; rows are residual evidence, not rational finite-closure proofs.",
        "",
        "| target | field | status | C2 dim | C1 processed | rank | raw support | residual support | deficit | C2 orbit vol | residual orbit support | orbit residual mass | nu_E residual | raw=coboundary | seconds |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['target']} | {row['coefficient_field']} | {row['modular_residual_status']} | "
            f"{row['c2_dimension']} | {row['processed_generators']} | {row['coboundary_rank']} | "
            f"{row['raw_support']} | {row['residual_support']} | {fmt(row['residual_deficit'])} | "
            f"{row['c2_orbit_quotient_volume']} | {row['residual_orbit_quotient_support']} | "
            f"{fmt(row['orbit_quotient_residual_mass'])} | {fmt(row['nu_lambda_E_residual_mass'])} | "
            f"{row['raw_is_coboundary']} | {fmt(row['elapsed_seconds'])} |"
        )
    lines += [
        "",
        "## Reading",
        "",
        "These rows convert quotient pressure into modular residual-orbit data when status is `complete`.  A generator-limited row is only a progress artifact and must not be read as a full residual result.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--from-json",
        action="append",
        type=Path,
        default=None,
        help="Merge existing streaming residual JSON artifacts instead of recomputing.",
    )
    parser.add_argument(
        "--target",
        action="append",
        choices=sorted(TARGETS),
        default=None,
        help="Target row to reduce. May repeat. Defaults to both large frontier rows.",
    )
    parser.add_argument("--field-prime", type=int, default=1_000_003)
    parser.add_argument("--max-generators", type=int, default=None)
    parser.add_argument("--progress-every", type=int, default=5000)
    parser.add_argument("--orbit-quotient-limit", type=int, default=0)
    parser.add_argument("--report", type=Path, default=REPORTS / "streaming_modular_residual.md")
    parser.add_argument("--json", type=Path, default=REPORTS / "streaming_modular_residual.json")
    args = parser.parse_args()

    if args.from_json:
        rows = []
        seen: set[str] = set()
        for path in args.from_json:
            payload = json.loads(path.read_text(encoding="utf-8"))
            for row in payload.get("rows", []):
                target = str(row["target"])
                if target in seen:
                    continue
                seen.add(target)
                rows.append(row)
    else:
        targets = args.target or sorted(TARGETS)
        rows = [
            reduce_leaf_modular(
                target,
                modulus=args.field_prime,
                max_generators=args.max_generators,
                progress_every=args.progress_every,
                orbit_quotient_limit=args.orbit_quotient_limit,
            )
            for target in targets
        ]

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(json_ready({"rows": rows}), indent=2), encoding="utf-8")
    args.report.write_text(make_report(rows, args.json), encoding="utf-8")
    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(
        json.dumps(
            json_ready(
                {
                    row["target"]: {
                        "status": row["modular_residual_status"],
                        "coboundary_rank": row["coboundary_rank"],
                        "raw_support": row["raw_support"],
                        "residual_support": row["residual_support"],
                        "residual_orbit_quotient_support": row[
                            "residual_orbit_quotient_support"
                        ],
                        "orbit_quotient_residual_mass": row[
                            "orbit_quotient_residual_mass"
                        ],
                        "nu_lambda_E_residual_mass": row["nu_lambda_E_residual_mass"],
                    }
                    for row in rows
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
