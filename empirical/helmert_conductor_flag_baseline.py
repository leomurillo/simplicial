"""Random mixed-flag baseline for conductor-respecting Helmert/NZSBTL flags.

This audit asks a narrow finite question:

    Given the same block sizes as the conductor packets, do Haar-random
    orthogonal flags that mix packets produce larger off-centroid Fisher
    block coupling than conductor-respecting flags?

The test is deliberately a baseline, not a theorem.  It treats a Helmert/
NZSBTL flag as an orthogonal basis of the nontrivial character tangent space,
grouped into blocks of the same sizes as the conductor packets.  At the
centroid every orthogonal flag is equivalent.  Off centroid, a fixed
displacement h produces a Fisher Gram matrix G_h.  The block-coupling cost

    sum_{a != b} ||B_a^T G_h B_b||_F^2

measures how much the chosen gauge blocks fail to remain Fisher-orthogonal.
Conductor-respecting blocks are compared against random mixed blocks with the
same dimensions.  An oracle eigenbasis is also reported as a sanity check:
it can diagonalize a single G_h, but is p-dependent and is not a fixed
arithmetic discretization.

The full ledger is a subspace analogue of the B0/J_infty terms.  For a target
conductor packet, the active resource is the prefix subspace through that
packet.  A random flag therefore competes with the same active dimension and
same block-size budget as the conductor prefix.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Hashable

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from local_adjacency_constructor import (  # noqa: E402
    FiniteLocalRing,
    LocalAdjacencyConstructor,
    make_f2_u2_ring,
    make_f2_u3_ring,
    make_f2_u4_ring,
    make_f2_u5_ring,
    make_f4_u2_ring,
    make_f4_u3_ring,
    make_f8_u2_ring,
)
from verify_per_row_carry_vs_depth import (  # noqa: E402
    dft,
    fourier_pure_displacement,
    make_character,
)


Label = Hashable
DEFAULT_JSON = Path("empirical/reports/helmert_conductor_flag_baseline.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_conductor_flag_baseline.md")


@dataclass(frozen=True)
class RowSpec:
    key: str
    display: str
    factory: Callable[[], FiniteLocalRing]
    field_width: int


ROW_SPECS: dict[str, RowSpec] = {
    "f2-u2": RowSpec("f2-u2", "F_2[u]/(u^2)", make_f2_u2_ring, 1),
    "f2-u3": RowSpec("f2-u3", "F_2[u]/(u^3)", make_f2_u3_ring, 1),
    "f2-u4": RowSpec("f2-u4", "F_2[u]/(u^4)", make_f2_u4_ring, 1),
    "f2-u5": RowSpec("f2-u5", "F_2[u]/(u^5)", make_f2_u5_ring, 1),
    "f4-u2": RowSpec("f4-u2", "F_4[u]/(u^2)", make_f4_u2_ring, 2),
    "f4-u3": RowSpec("f4-u3", "F_4[u]/(u^3)", make_f4_u3_ring, 2),
    "f8-u2": RowSpec("f8-u2", "F_8[u]/(u^2)", make_f8_u2_ring, 3),
}


def ordered_modes(
    packets: dict[str, tuple[Label, ...]],
    conductor_order: tuple[str, ...],
) -> tuple[Label, ...]:
    return tuple(
        label
        for conductor in conductor_order
        if conductor in packets
        for label in packets[conductor]
    )


def block_slices(block_sizes: list[int]) -> list[slice]:
    out: list[slice] = []
    start = 0
    for size in block_sizes:
        out.append(slice(start, start + size))
        start += size
    return out


def character_matrix(
    ring: FiniteLocalRing,
    modes: tuple[Label, ...],
    chi: Callable[[Label, Label], float],
) -> np.ndarray:
    n = len(ring.labels)
    matrix = np.empty((n, len(modes)), dtype=float)
    for i, label in enumerate(ring.labels):
        for j, mode in enumerate(modes):
            matrix[i, j] = chi(mode, label) / np.sqrt(n)
    return matrix


def fisher_gram(probability: np.ndarray, character_basis: np.ndarray) -> np.ndarray:
    n = probability.shape[0]
    weighted = character_basis / probability[:, None]
    gram = character_basis.T @ weighted / n
    return 0.5 * (gram + gram.T)


def coefficient_vector(
    coefficients: dict[Label, complex | float],
    modes: tuple[Label, ...],
) -> np.ndarray:
    return np.array([float(np.real(coefficients[mode])) for mode in modes], dtype=float)


def addition_tensor(ring: FiniteLocalRing, modes: tuple[Label, ...]) -> np.ndarray:
    """Tensor T[k,i,j]=1 when modes[i]+modes[j]=modes[k] nonzero."""
    index = {mode: i for i, mode in enumerate(modes)}
    tensor = np.zeros((len(modes), len(modes), len(modes)), dtype=float)
    for i, left in enumerate(modes):
        for j, right in enumerate(modes):
            target = ring.add(left, right)
            if target == ring.zero:
                continue
            k = index.get(target)
            if k is not None:
                tensor[k, i, j] = 1.0
    return tensor


def safe_probability(
    h_values: dict[Label, float],
    ring: FiniteLocalRing,
    amplitude_fraction: float,
) -> tuple[np.ndarray, float]:
    h = np.array([h_values[label] for label in ring.labels], dtype=float)
    uniform = 1.0 / len(ring.labels)
    min_h = float(h.min())
    max_abs = float(np.max(np.abs(h)))
    if max_abs == 0.0:
        return np.full(len(ring.labels), uniform), 0.0
    if min_h < 0.0:
        max_amplitude = 0.95 * uniform / (-min_h)
    else:
        max_amplitude = 1.0 / max_abs
    amplitude = amplitude_fraction * max_amplitude
    probability = np.full(len(ring.labels), uniform) + amplitude * h
    if float(probability.min()) <= 0.0:
        raise ValueError("amplitude produced a non-positive probability")
    return probability, amplitude


def off_block_energy(matrix: np.ndarray, sizes: list[int]) -> float:
    total = 0.0
    slices = block_slices(sizes)
    for i, rows in enumerate(slices):
        for j, cols in enumerate(slices):
            if i == j:
                continue
            block = matrix[rows, cols]
            total += float(np.sum(block * block))
    return total


def prefix_width(sizes: list[int], target_index: int) -> int:
    return sum(sizes[: target_index + 1])


def active_subspace(q: np.ndarray, sizes: list[int], target_index: int) -> np.ndarray:
    return q[:, :prefix_width(sizes, target_index)]


def projection_error_subspace(vector: np.ndarray, basis: np.ndarray) -> float:
    total = float(vector @ vector)
    if total <= 1e-15:
        return 0.0
    inside = basis.T @ vector
    inside_energy = float(inside @ inside)
    return max(0.0, 1.0 - inside_energy / total)


def closure_leakage_subspace(add_tensor: np.ndarray, basis: np.ndarray) -> float:
    """Expected nonzero additive-product energy outside the active subspace."""
    if basis.shape[1] == basis.shape[0]:
        return 0.0
    products = np.einsum("kij,ia,jb->kab", add_tensor, basis, basis, optimize=True)
    denominator = float(np.sum(products * products))
    if denominator <= 1e-15:
        return 0.0
    projected = np.einsum("ca,kab->cab", basis, products, optimize=True)
    inside = float(np.sum(projected * projected))
    return max(0.0, 1.0 - inside / denominator)


def flag_ledger(
    *,
    q: np.ndarray,
    gram: np.ndarray,
    sizes: list[int],
    target_index: int,
    h_hat_vector: np.ndarray,
    reciprocal_vector: np.ndarray,
    add_tensor: np.ndarray,
    weights: dict[str, float],
) -> dict[str, float]:
    active = active_subspace(q, sizes, target_index)
    block_coupling = off_block_energy(q.T @ gram @ q, sizes)
    mix_impurity = packet_commutator_impurity(q, sizes)
    fisher_projection = projection_error_subspace(h_hat_vector, active)
    reciprocal_projection = projection_error_subspace(reciprocal_vector, active)
    closure = closure_leakage_subspace(add_tensor, active)
    resource = active.shape[1] / q.shape[0]
    depth = (target_index + 1) / len(sizes)
    j_value = (
        weights["block"] * block_coupling
        + weights["mix"] * mix_impurity
        + weights["fisher_projection"] * fisher_projection
        + weights["reciprocal_projection"] * reciprocal_projection
        + weights["closure"] * closure
        + weights["resource"] * resource
        + weights["depth"] * depth
    )
    return {
        "J": j_value,
        "block_coupling": block_coupling,
        "mix_impurity": mix_impurity,
        "fisher_projection_error": fisher_projection,
        "reciprocal_projection_error": reciprocal_projection,
        "closure_leakage": closure,
        "resource_cost": resource,
        "depth_cost": depth,
    }


def random_orthogonal(dim: int, rng: np.random.Generator) -> np.ndarray:
    sample = rng.normal(size=(dim, dim))
    q, r = np.linalg.qr(sample)
    signs = np.sign(np.diag(r))
    signs[signs == 0.0] = 1.0
    return q * signs


def block_random_orthogonal(sizes: list[int], rng: np.random.Generator) -> np.ndarray:
    dim = sum(sizes)
    out = np.zeros((dim, dim), dtype=float)
    for span in block_slices(sizes):
        size = span.stop - span.start
        out[span, span] = random_orthogonal(size, rng)
    return out


def packet_purity(q: np.ndarray, sizes: list[int]) -> float:
    """Return weighted max packet concentration of candidate blocks.

    A conductor-respecting block decomposition has purity 1.  A mixed random
    decomposition has lower purity because each candidate block spreads across
    several conductor packets.
    """
    spans = block_slices(sizes)
    dim = q.shape[0]
    weighted = 0.0
    for block_span in spans:
        block = q[:, block_span]
        block_size = block_span.stop - block_span.start
        energies = []
        for packet_span in spans:
            sub = block[packet_span, :]
            energies.append(float(np.sum(sub * sub)))
        weighted += max(energies)
    return weighted / dim


def packet_commutator_impurity(q: np.ndarray, sizes: list[int]) -> float:
    """Measure failure of candidate flag blocks to commute with packet projectors."""
    spans = block_slices(sizes)
    dim = q.shape[0]
    total = 0.0
    for block_span in spans:
        block = q[:, block_span]
        p_block = block @ block.T
        for packet_span in spans:
            p_packet = np.zeros((dim, dim), dtype=float)
            p_packet[packet_span, packet_span] = np.eye(packet_span.stop - packet_span.start)
            commutator = p_block @ p_packet - p_packet @ p_block
            total += float(np.sum(commutator * commutator))
    return total / dim


def summarize(values: list[float]) -> dict[str, float]:
    arr = np.array(values, dtype=float)
    return {
        "min": float(arr.min()),
        "p05": float(np.quantile(arr, 0.05)),
        "median": float(np.median(arr)),
        "mean": float(arr.mean()),
        "p95": float(np.quantile(arr, 0.95)),
        "max": float(arr.max()),
    }


def evaluate_packet(
    *,
    ring: FiniteLocalRing,
    row_key: str,
    row_display: str,
    field_width: int,
    target_packet: str,
    samples: int,
    seed: int,
    amplitude_fraction: float,
    impurity_weight: float,
    weights: dict[str, float],
) -> dict[str, Any]:
    chi = make_character(ring, field_width)
    constructor = LocalAdjacencyConstructor(ring)
    cond_order = tuple(c for c in ring.conductor_order if c in constructor.packets)
    packets = constructor.packets
    modes = ordered_modes(packets, cond_order)
    sizes = [len(packets[c]) for c in cond_order]
    basis = character_matrix(ring, modes, chi)

    h_values, h_hat_indicator = fourier_pure_displacement(packets, ring, chi, target_packet)
    probability, amplitude = safe_probability(h_values, ring, amplitude_fraction)
    probability_by_label = {
        label: float(probability[i])
        for i, label in enumerate(ring.labels)
    }
    reciprocal_values = {
        label: 1.0 / probability_by_label[label]
        for label in ring.labels
    }
    reciprocal_hat = dft(reciprocal_values, ring, chi)
    h_hat_vector = coefficient_vector(h_hat_indicator, modes)
    reciprocal_vector = coefficient_vector(reciprocal_hat, modes)
    add_tensor = addition_tensor(ring, modes)
    gram = fisher_gram(probability, basis)

    target_index = cond_order.index(target_packet)
    identity_flag = np.eye(len(modes))
    conductor_ledger = flag_ledger(
        q=identity_flag,
        gram=gram,
        sizes=sizes,
        target_index=target_index,
        h_hat_vector=h_hat_vector,
        reciprocal_vector=reciprocal_vector,
        add_tensor=add_tensor,
        weights=weights,
    )
    conductor_energy = off_block_energy(gram, sizes)
    total_offdiag = off_block_energy(gram, [1] * gram.shape[0])

    rng = np.random.default_rng(seed)
    random_energies: list[float] = []
    random_purities: list[float] = []
    random_impurities: list[float] = []
    block_random_energies: list[float] = []
    random_total_costs: list[float] = []
    break_even_mix_weights: list[float] = []
    random_ledgers: list[dict[str, float]] = []
    for _ in range(samples):
        q = random_orthogonal(gram.shape[0], rng)
        rotated = q.T @ gram @ q
        random_energy = off_block_energy(rotated, sizes)
        purity = packet_purity(q, sizes)
        impurity = packet_commutator_impurity(q, sizes)
        random_energies.append(random_energy)
        random_purities.append(purity)
        random_impurities.append(impurity)
        random_total_costs.append(random_energy + impurity_weight * impurity)
        if random_energy < conductor_energy and impurity > 1e-12:
            break_even_mix_weights.append((conductor_energy - random_energy) / impurity)
        else:
            break_even_mix_weights.append(0.0)
        random_ledgers.append(
            flag_ledger(
                q=q,
                gram=gram,
                sizes=sizes,
                target_index=target_index,
                h_hat_vector=h_hat_vector,
                reciprocal_vector=reciprocal_vector,
                add_tensor=add_tensor,
                weights=weights,
            )
        )

        q_block = block_random_orthogonal(sizes, rng)
        block_rotated = q_block.T @ gram @ q_block
        block_random_energies.append(off_block_energy(block_rotated, sizes))

    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    oracle = eigenvectors.T @ gram @ eigenvectors
    oracle_energy = off_block_energy(oracle, sizes)
    random_better = sum(value < conductor_energy for value in random_energies)
    random_better_with_mix_price = sum(value < conductor_energy for value in random_total_costs)
    random_j_values = [ledger["J"] for ledger in random_ledgers]
    random_better_j = sum(value < conductor_ledger["J"] for value in random_j_values)
    conductor_j_without_mix = conductor_ledger["J"]
    full_j_break_even_mix_weights = []
    for ledger in random_ledgers:
        random_j_without_mix = ledger["J"] - weights["mix"] * ledger["mix_impurity"]
        if random_j_without_mix < conductor_j_without_mix and ledger["mix_impurity"] > 1e-12:
            full_j_break_even_mix_weights.append(
                (conductor_j_without_mix - random_j_without_mix) / ledger["mix_impurity"]
            )
        else:
            full_j_break_even_mix_weights.append(0.0)
    block_spread = max(block_random_energies) - min(block_random_energies)

    return {
        "row_key": row_key,
        "row": row_display,
        "ring_name": ring.name,
        "target_packet": target_packet,
        "conductor_order": list(cond_order),
        "packet_sizes": dict(zip(cond_order, sizes)),
        "samples": samples,
        "seed": seed,
        "amplitude_fraction": amplitude_fraction,
        "actual_amplitude": amplitude,
        "probability_min": float(probability.min()),
        "probability_max": float(probability.max()),
        "h_hat_indicator_energy": float(
            sum(h_hat_indicator[eta] ** 2 for eta in ring.labels if eta != ring.zero)
        ),
        "target_depth": target_index + 1,
        "active_prefix_dimension": prefix_width(sizes, target_index),
        "ledger_weights": weights,
        "conductor_full_ledger": conductor_ledger,
        "random_mixed_J": summarize(random_j_values),
        "random_mixed_better_J_count": random_better_j,
        "random_mixed_better_J_fraction": random_better_j / samples,
        "full_J_break_even_mix_weight": summarize(full_j_break_even_mix_weights),
        "random_mixed_ledger_terms": {
            key: summarize([ledger[key] for ledger in random_ledgers])
            for key in conductor_ledger
            if key != "J"
        },
        "conductor_block_coupling": conductor_energy,
        "canonical_axis_offdiag_energy": total_offdiag,
        "packet_respecting_block_random_spread": block_spread,
        "packet_respecting_block_random_summary": summarize(block_random_energies),
        "random_mixed_block_coupling": summarize(random_energies),
        "random_mixed_packet_purity": summarize(random_purities),
        "random_mixed_packet_commutator_impurity": summarize(random_impurities),
        "mix_impurity_weight": impurity_weight,
        "random_mixed_total_cost": summarize(random_total_costs),
        "random_mixed_better_with_mix_price_count": random_better_with_mix_price,
        "random_mixed_better_with_mix_price_fraction": random_better_with_mix_price / samples,
        "break_even_mix_weight": summarize(break_even_mix_weights),
        "random_mixed_better_count": random_better,
        "random_mixed_better_fraction": random_better / samples,
        "oracle_eigenbasis_block_coupling": oracle_energy,
        "gram_eigenvalue_min": float(eigenvalues.min()),
        "gram_eigenvalue_max": float(eigenvalues.max()),
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = [key.strip() for key in args.rows.split(",") if key.strip()]
    results: list[dict[str, Any]] = []
    weights = {
        "block": args.block_weight,
        "mix": args.impurity_weight,
        "fisher_projection": args.fisher_projection_weight,
        "reciprocal_projection": args.reciprocal_projection_weight,
        "closure": args.closure_weight,
        "resource": args.resource_weight,
        "depth": args.depth_weight,
    }
    for row_offset, key in enumerate(rows):
        if key not in ROW_SPECS:
            raise ValueError(f"unknown row key {key!r}; choose from {sorted(ROW_SPECS)}")
        spec = ROW_SPECS[key]
        ring = spec.factory()
        constructor = LocalAdjacencyConstructor(ring)
        cond_order = tuple(c for c in ring.conductor_order if c in constructor.packets)
        for packet_offset, target_packet in enumerate(cond_order):
            if args.skip_lowest and packet_offset == 0:
                continue
            results.append(
                evaluate_packet(
                    ring=ring,
                    row_key=spec.key,
                    row_display=spec.display,
                    field_width=spec.field_width,
                    target_packet=target_packet,
                    samples=args.samples,
                    seed=args.seed + 1000 * row_offset + 17 * packet_offset,
                    amplitude_fraction=args.amplitude_fraction,
                    impurity_weight=args.impurity_weight,
                    weights=weights,
                )
            )
    return {
        "purpose": (
            "Baseline for Helmert/NZSBTL flags: compare conductor-respecting "
            "packet blocks with Haar-random mixed orthogonal blocks at equal "
            "block sizes using off-centroid Fisher block coupling."
        ),
        "config": {
            "rows": rows,
            "samples": args.samples,
            "seed": args.seed,
            "amplitude_fraction": args.amplitude_fraction,
            "ledger_weights": weights,
            "skip_lowest": args.skip_lowest,
        },
        "results": results,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Conductor-Flag Baseline",
        "",
        "This audit compares conductor-respecting gauge blocks against Haar-random",
        "orthogonal blocks with the same block sizes.  It reports both raw",
        "off-centroid Fisher block coupling and a fuller subspace J ledger with",
        "projection, closure, packet-respect, and resource terms.",
        "",
        "The oracle eigenbasis is shown only as a sanity check.  It diagonalizes",
        "the single tested Fisher matrix and is not a fixed arithmetic descent.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Summary",
        "",
        "| row | target packet | active dim | conductor J | random J median | random better J | full-J frame price max | raw frame price max | conductor coupling | random better raw |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        random_summary = result["random_mixed_block_coupling"]
        random_j = result["random_mixed_J"]
        impurity_summary = result["random_mixed_packet_commutator_impurity"]
        break_even = result["break_even_mix_weight"]
        full_break_even = result["full_J_break_even_mix_weight"]
        lines.append(
            "| {row} | {packet} | {active_dim} | {conductor_j:.6g} | {random_j:.6g} | "
            "{better_j}/{samples} | {full_be_max:.6g} | {be_max:.6g} | "
            "{conductor:.6g} | {better}/{samples} |".format(
                row=result["row"],
                packet=result["target_packet"],
                active_dim=result["active_prefix_dimension"],
                conductor_j=result["conductor_full_ledger"]["J"],
                random_j=random_j["median"],
                better_j=result["random_mixed_better_J_count"],
                full_be_max=full_break_even["max"],
                conductor=result["conductor_block_coupling"],
                better=result["random_mixed_better_count"],
                samples=result["samples"],
                be_max=break_even["max"],
            )
        )

    lines += [
        "",
        "## Detail",
        "",
    ]
    for result in payload["results"]:
        random_summary = result["random_mixed_block_coupling"]
        random_j = result["random_mixed_J"]
        purity_summary = result["random_mixed_packet_purity"]
        impurity_summary = result["random_mixed_packet_commutator_impurity"]
        block_summary = result["packet_respecting_block_random_summary"]
        total_summary = result["random_mixed_total_cost"]
        break_even = result["break_even_mix_weight"]
        full_break_even = result["full_J_break_even_mix_weight"]
        conductor_ledger = result["conductor_full_ledger"]
        ledger_terms = result["random_mixed_ledger_terms"]
        lines += [
            f"### {result['row']} target `{result['target_packet']}`",
            "",
            f"- probability range: `{result['probability_min']:.6g}` to `{result['probability_max']:.6g}`",
            f"- actual displacement amplitude: `{result['actual_amplitude']:.6g}`",
            f"- active prefix dimension: `{result['active_prefix_dimension']}` at depth `{result['target_depth']}`",
            f"- conductor full J: `{conductor_ledger['J']:.12g}`",
            f"- random mixed better fraction by full J: `{result['random_mixed_better_J_fraction']:.6g}`",
            f"- max full-J frame price among sampled random flags: `{full_break_even['max']:.6g}`",
            f"- conductor block coupling: `{result['conductor_block_coupling']:.12g}`",
            f"- random mixed better fraction: `{result['random_mixed_better_fraction']:.6g}`",
            f"- mix impurity weight: `{result['mix_impurity_weight']:.6g}`",
            f"- random mixed better fraction after mix price: `{result['random_mixed_better_with_mix_price_fraction']:.6g}`",
            f"- max break-even mix price among sampled random flags: `{break_even['max']:.6g}`",
            f"- packet-respecting random spread: `{result['packet_respecting_block_random_spread']:.3e}`",
            f"- oracle eigenbasis block coupling: `{result['oracle_eigenbasis_block_coupling']:.3e}`",
            "",
            "| distribution | min | p05 | median | mean | p95 | max |",
            "|---|---:|---:|---:|---:|---:|---:|",
            "| random mixed coupling | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**random_summary),
            "| random mixed full J | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**random_j),
            "| full-J frame price | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**full_break_even),
            "| random mixed total cost | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**total_summary),
            "| break-even mix weight | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**break_even),
            "| packet-respecting coupling | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**block_summary),
            "| packet-commutator impurity | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**impurity_summary),
            "| random mixed packet purity | {min:.6g} | {p05:.6g} | {median:.6g} | {mean:.6g} | {p95:.6g} | {max:.6g} |".format(**purity_summary),
            "",
            "| J term | conductor | random median | random p05 | random p95 |",
            "|---|---:|---:|---:|---:|",
        ]
        for key in [
            "block_coupling",
            "mix_impurity",
            "fisher_projection_error",
            "reciprocal_projection_error",
            "closure_leakage",
            "resource_cost",
            "depth_cost",
        ]:
            summary = ledger_terms[key]
            lines.append(
                f"| {key} | {conductor_ledger[key]:.6g} | "
                f"{summary['median']:.6g} | {summary['p05']:.6g} | {summary['p95']:.6g} |"
            )
        lines += [
            "",
        ]

    lines += [
        "## Reading",
        "",
        "A zero `random better raw` count is evidence that generic mixed Helmert",
        "flags are worse even before pricing conductor respect.  A nonzero raw",
        "count shows that Fisher block coupling alone is not the right structural",
        "objective: a p-dependent or mixed flag can partially diagonalize one",
        "local Fisher matrix.  The break-even mix price reports how much packet",
        "respect must be worth before the conductor flag beats every sampled",
        "mixed flag under this two-term score.  Here packet respect is measured",
        "by projector-commutator impurity against the conductor packet",
        "decomposition.  The full J columns add prefix-subspace projection,",
        "reciprocal projection, additive closure leakage, resource, and depth",
        "costs.  The decisive falsifier is therefore a sampled mixed flag with",
        "lower full J than the conductor prefix at the same active dimension.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default="f4-u2,f2-u4")
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260515)
    parser.add_argument("--amplitude-fraction", type=float, default=0.35)
    parser.add_argument("--impurity-weight", type=float, default=1.0)
    parser.add_argument("--block-weight", type=float, default=1.0)
    parser.add_argument("--fisher-projection-weight", type=float, default=1.0)
    parser.add_argument("--reciprocal-projection-weight", type=float, default=1.0)
    parser.add_argument("--closure-weight", type=float, default=1.0)
    parser.add_argument("--resource-weight", type=float, default=0.1)
    parser.add_argument("--depth-weight", type=float, default=0.1)
    parser.add_argument("--skip-lowest", action="store_true", default=True)
    parser.add_argument("--include-lowest", dest="skip_lowest", action="store_false")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for result in payload["results"]:
        random_summary = result["random_mixed_block_coupling"]
        print(
            f"{result['row']} {result['target_packet']}: "
            f"J_conductor={result['conductor_full_ledger']['J']:.6g}, "
            f"J_random_median={result['random_mixed_J']['median']:.6g}, "
            f"better_J={result['random_mixed_better_J_count']}/{result['samples']}, "
            f"fullJ_mix_price_max={result['full_J_break_even_mix_weight']['max']:.6g}, "
            f"conductor={result['conductor_block_coupling']:.6g}, "
            f"random_min={random_summary['min']:.6g}, "
            f"random_median={random_summary['median']:.6g}, "
            f"better_raw={result['random_mixed_better_count']}/{result['samples']}, "
            f"better_priced={result['random_mixed_better_with_mix_price_count']}/{result['samples']}, "
            f"mix_price_max={result['break_even_mix_weight']['max']:.6g}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
