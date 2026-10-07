"""Smoke tests for streaming_modular_residual.py."""

from __future__ import annotations

from cocycle_reducer import CocycleReducer
from local_adjacency_constructor import LocalAdjacencyConstructor, make_f2_u3_ring
from per_leaf_coboundary_audit import generator_in_leaf, split_leaf
from streaming_modular_residual import (
    LeafC2Codec,
    build_shift_lookups,
    fast_coboundary_column_mod,
)


def main() -> int:
    modulus = 101
    reducer = CocycleReducer(LocalAdjacencyConstructor(make_f2_u3_ring()))
    leaf = set(split_leaf("u^2+u^3"))
    codec = LeafC2Codec(reducer, leaf)
    lookups = build_shift_lookups(reducer.constructor)
    generators = [
        generator
        for generator in reducer.section_generators("full_block")
        if generator_in_leaf(generator, leaf)
    ]

    for generator in generators[:10]:
        fast = fast_coboundary_column_mod(reducer, generator, codec, lookups, modulus)
        slow = {}
        for key, value in reducer.coboundary_column(generator).items():
            index = codec.index(key)
            if index is None:
                continue
            entry = int(value) % modulus
            if entry:
                slow[index] = (slow.get(index, 0) + entry) % modulus
                if not slow[index]:
                    del slow[index]
        assert fast == slow

    first_key = codec.decode(0)
    assert codec.index(first_key) == 0
    last_key = codec.decode(codec.dimension - 1)
    assert codec.index(last_key) == codec.dimension - 1
    print("All streaming_modular_residual smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
