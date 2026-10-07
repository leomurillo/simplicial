"""Local cross-packet rotation diagnostic for Helmert frame-price blowups.

The amplitude-frontier experiment found huge sampled frame prices on
F_2[u]/(u^2).  This script tests the local mechanism:

    J_0(I + theta A) improves at first order,
    packet impurity appears only at second order.

Then the break-even frame price scales like const / |theta|.  That turns the
observed large lambda values into a structural boundary phenomenon: the
conductor frame is not a local minimum of the unpriced one-point objective,
while the arithmetic impurity penalty is quadratically small near it.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from helmert_conductor_flag_baseline import (  # noqa: E402
    ROW_SPECS,
    LocalAdjacencyConstructor,
    addition_tensor,
    character_matrix,
    coefficient_vector,
    dft,
    fisher_gram,
    flag_ledger,
    fourier_pure_displacement,
    make_character,
    ordered_modes,
    safe_probability,
)


DEFAULT_JSON = Path("empirical/reports/helmert_local_rotation_obstruction.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_local_rotation_obstruction.md")


def parse_csv(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def parse_float_csv(text: str) -> list[float]:
    return [float(item.strip()) for item in text.split(",") if item.strip()]


def ledger_weights(args: argparse.Namespace) -> dict[str, float]:
    return {
        "block": args.block_weight,
        "mix": args.impurity_weight,
        "fisher_projection": args.fisher_projection_weight,
        "reciprocal_projection": args.reciprocal_projection_weight,
        "closure": args.closure_weight,
        "resource": args.resource_weight,
        "depth": args.depth_weight,
    }


def block_slices(sizes: list[int]) -> list[slice]:
    out: list[slice] = []
    start = 0
    for size in sizes:
        out.append(slice(start, start + size))
        start += size
    return out


def cross_packet_pairs(sizes: list[int]) -> list[tuple[int, int]]:
    slices = block_slices(sizes)
    pairs: list[tuple[int, int]] = []
    for a, left in enumerate(slices):
        for b, right in enumerate(slices):
            if a >= b:
                continue
            for i in range(left.start, left.stop):
                for j in range(right.start, right.stop):
                    pairs.append((i, j))
    return pairs


def plane_rotation(dim: int, i: int, j: int, theta: float) -> np.ndarray:
    q = np.eye(dim)
    c = float(np.cos(theta))
    s = float(np.sin(theta))
    q[i, i] = c
    q[j, j] = c
    q[i, j] = -s
    q[j, i] = s
    return q


def packet_of(index: int, sizes: list[int]) -> int:
    cumulative = 0
    for packet, size in enumerate(sizes):
        cumulative += size
        if index < cumulative:
            return packet
    raise ValueError(f"index {index} out of packet range {sizes}")


def first_order_packet_norm_for_plane(i: int, j: int, sizes: list[int]) -> float:
    """nu(A_ij) = sum_{a != b} ||P_a A_ij P_b||_F for the plane skew A_ij.

    The plane rotation exp(theta A_ij) has A_ij[i,j] = -1 and A_ij[j,i] = +1
    (zero elsewhere).  When i and j lie in different conductor packets, the
    only nonzero cross-packet blocks are (pkt(i), pkt(j)) and (pkt(j), pkt(i)),
    each contributing Frobenius norm 1.  Sum: 2 for cross-packet, 0 for
    within-packet.  Theorem 3.5 of paper 25 uses this nu(A) as the first-order
    packet-respect cost slope, and the per-pair required price is |a|/nu.
    """
    if packet_of(i, sizes) == packet_of(j, sizes):
        return 0.0
    return 2.0


def setup_case(
    row_key: str,
    target_packet: str,
    amplitude_fraction: float,
) -> dict[str, Any]:
    if row_key not in ROW_SPECS:
        raise ValueError(f"unknown row key {row_key!r}; choose from {sorted(ROW_SPECS)}")
    spec = ROW_SPECS[row_key]
    ring = spec.factory()
    chi = make_character(ring, spec.field_width)
    constructor = LocalAdjacencyConstructor(ring)
    packets = constructor.packets
    cond_order = tuple(c for c in ring.conductor_order if c in packets)
    modes = ordered_modes(packets, cond_order)
    sizes = [len(packets[c]) for c in cond_order]
    basis = character_matrix(ring, modes, chi)
    h_values, h_hat = fourier_pure_displacement(packets, ring, chi, target_packet)
    probability, actual_amplitude = safe_probability(h_values, ring, amplitude_fraction)
    probability_by_label = {
        label: float(probability[i])
        for i, label in enumerate(ring.labels)
    }
    reciprocal_values = {
        label: 1.0 / probability_by_label[label]
        for label in ring.labels
    }
    reciprocal_hat = dft(reciprocal_values, ring, chi)
    return {
        "spec": spec,
        "ring": ring,
        "packets": packets,
        "cond_order": cond_order,
        "modes": modes,
        "sizes": sizes,
        "target_index": cond_order.index(target_packet),
        "gram": fisher_gram(probability, basis),
        "h_hat_vector": coefficient_vector(h_hat, modes),
        "reciprocal_vector": coefficient_vector(reciprocal_hat, modes),
        "add_tensor": addition_tensor(ring, modes),
        "actual_amplitude": actual_amplitude,
        "probability_min": float(probability.min()),
        "probability_max": float(probability.max()),
    }


def ledger_at(
    context: dict[str, Any],
    q: np.ndarray,
    weights: dict[str, float],
) -> dict[str, float]:
    return flag_ledger(
        q=q,
        gram=context["gram"],
        sizes=context["sizes"],
        target_index=context["target_index"],
        h_hat_vector=context["h_hat_vector"],
        reciprocal_vector=context["reciprocal_vector"],
        add_tensor=context["add_tensor"],
        weights=weights,
    )


def j0(ledger: dict[str, float], weights: dict[str, float]) -> float:
    return ledger["J"] - weights["mix"] * ledger["mix_impurity"]


def evaluate_pair(
    *,
    context: dict[str, Any],
    weights: dict[str, float],
    i: int,
    j: int,
    epsilon: float,
    theta_grid: list[float],
) -> dict[str, Any]:
    dim = context["gram"].shape[0]
    base = ledger_at(context, np.eye(dim), weights)
    base_j0 = j0(base, weights)

    plus = ledger_at(context, plane_rotation(dim, i, j, epsilon), weights)
    minus = ledger_at(context, plane_rotation(dim, i, j, -epsilon), weights)
    plus_j0 = j0(plus, weights)
    minus_j0 = j0(minus, weights)
    d_j0 = (plus_j0 - minus_j0) / (2.0 * epsilon)
    d_impurity = (plus["mix_impurity"] - minus["mix_impurity"]) / (2.0 * epsilon)
    impurity_quadratic = (
        plus["mix_impurity"] + minus["mix_impurity"] - 2.0 * base["mix_impurity"]
    ) / (2.0 * epsilon * epsilon)
    singular_constant = (
        abs(d_j0) / impurity_quadratic
        if abs(d_j0) > 1e-8 and impurity_quadratic > 1e-12
        else 0.0
    )

    one_sided_descent_rate = max(
        (base_j0 - plus_j0) / epsilon,
        (base_j0 - minus_j0) / epsilon,
        0.0,
    )

    samples: list[dict[str, float]] = []
    max_lambda = 0.0
    best_theta = 0.0
    for theta in theta_grid:
        for signed_theta in (-theta, theta):
            ledger = ledger_at(context, plane_rotation(dim, i, j, signed_theta), weights)
            value_j0 = j0(ledger, weights)
            improvement = base_j0 - value_j0
            impurity = ledger["mix_impurity"]
            lambda_value = improvement / impurity if improvement > 0.0 and impurity > 1e-15 else 0.0
            if lambda_value > max_lambda:
                max_lambda = lambda_value
                best_theta = signed_theta
            samples.append(
                {
                    "theta": signed_theta,
                    "J0": value_j0,
                    "J0_improvement": improvement,
                    "mix_impurity": impurity,
                    "lambda": lambda_value,
                }
            )

    first_order_packet_norm = first_order_packet_norm_for_plane(
        i, j, context["sizes"]
    )
    first_order_required_price = (
        one_sided_descent_rate / first_order_packet_norm
        if first_order_packet_norm > 0.0 and one_sided_descent_rate > 0.0
        else 0.0
    )

    return {
        "pair": [i, j],
        "d_J0_at_zero": d_j0,
        "one_sided_descent_rate": one_sided_descent_rate,
        "d_impurity_at_zero": d_impurity,
        "impurity_quadratic_coefficient": impurity_quadratic,
        "singular_constant_abs_dJ0_over_c": singular_constant,
        "singular_direction": bool(abs(d_j0) > 1e-8 and impurity_quadratic > 1e-8),
        "first_order_packet_norm_nu": first_order_packet_norm,
        "first_order_required_price_mu_star": first_order_required_price,
        "max_lambda_on_grid": max_lambda,
        "best_theta": best_theta,
        "samples": samples,
    }


def evaluate_case(
    *,
    row_key: str,
    target_packet: str,
    amplitude_fraction: float,
    epsilon: float,
    theta_grid: list[float],
    weights: dict[str, float],
) -> dict[str, Any]:
    context = setup_case(row_key, target_packet, amplitude_fraction)
    dim = context["gram"].shape[0]
    base = ledger_at(context, np.eye(dim), weights)
    pair_results = [
        evaluate_pair(
            context=context,
            weights=weights,
            i=i,
            j=j,
            epsilon=epsilon,
            theta_grid=theta_grid,
        )
        for i, j in cross_packet_pairs(context["sizes"])
    ]
    singular_pairs = [item for item in pair_results if item["singular_direction"]]
    best = max(pair_results, key=lambda item: item["max_lambda_on_grid"]) if pair_results else None
    max_first_order_mu_star = max(
        (item["first_order_required_price_mu_star"] for item in pair_results),
        default=0.0,
    )
    return {
        "row_key": row_key,
        "row": context["spec"].display,
        "target_packet": target_packet,
        "target_depth": context["target_index"] + 1,
        "packet_sizes": dict(zip(context["cond_order"], context["sizes"])),
        "active_prefix_dimension": sum(context["sizes"][: context["target_index"] + 1]),
        "total_dimension": dim,
        "amplitude_fraction": amplitude_fraction,
        "actual_amplitude": context["actual_amplitude"],
        "probability_min": context["probability_min"],
        "probability_max": context["probability_max"],
        "base_J": base["J"],
        "base_J0": j0(base, weights),
        "base_block_coupling": base["block_coupling"],
        "base_mix_impurity": base["mix_impurity"],
        "cross_pair_count": len(pair_results),
        "singular_pair_count": len(singular_pairs),
        "max_lambda_on_grid": best["max_lambda_on_grid"] if best else 0.0,
        "best_pair": best["pair"] if best else None,
        "best_theta": best["best_theta"] if best else 0.0,
        "best_d_J0_at_zero": best["d_J0_at_zero"] if best else 0.0,
        "best_impurity_quadratic_coefficient": (
            best["impurity_quadratic_coefficient"] if best else 0.0
        ),
        "best_singular_constant_abs_dJ0_over_c": (
            best["singular_constant_abs_dJ0_over_c"] if best else 0.0
        ),
        "max_first_order_required_price_mu_star": max_first_order_mu_star,
        "pairs": pair_results,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_csv(args.rows)
    amplitudes = parse_float_csv(args.amplitudes)
    theta_grid = parse_float_csv(args.thetas)
    weights = ledger_weights(args)
    results: list[dict[str, Any]] = []
    for row_key in rows:
        spec = ROW_SPECS[row_key]
        ring = spec.factory()
        constructor = LocalAdjacencyConstructor(ring)
        cond_order = tuple(c for c in ring.conductor_order if c in constructor.packets)
        for packet_offset, target_packet in enumerate(cond_order):
            if args.skip_lowest and packet_offset == 0:
                continue
            for amplitude in amplitudes:
                results.append(
                    evaluate_case(
                        row_key=row_key,
                        target_packet=target_packet,
                        amplitude_fraction=amplitude,
                        epsilon=args.epsilon,
                        theta_grid=theta_grid,
                        weights=weights,
                    )
                )
    return {
        "purpose": (
            "Local cross-packet rotation diagnostic: detect first-order descent "
            "of the unpriced one-point objective against second-order packet "
            "impurity near the conductor flag."
        ),
        "config": {
            "rows": rows,
            "amplitudes": amplitudes,
            "thetas": theta_grid,
            "epsilon": args.epsilon,
            "skip_lowest": args.skip_lowest,
            "ledger_weights": weights,
        },
        "results": results,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Local Rotation Obstruction",
        "",
        "This diagnostic rotates the conductor flag by tiny cross-packet plane",
        "rotations.  A boundary obstruction is present when the unpriced",
        "one-point ledger \\(J_0\\) has a nonzero first derivative while packet",
        "impurity is quadratic.  Then the break-even frame price scales like",
        "`1/|theta|` near the conductor flag.",
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
        "| row | packet | amplitude | active dim | pairs | singular pairs | max lambda on grid | best pair | best theta | dJ0(0) | impurity theta^2 coeff | singular constant | max mu* (first-order cure) |",
        "|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        lines.append(
            "| {row} | {packet} | {amp:.6g} | {dim} | {pairs} | {singular} | "
            "{lam:.6g} | {best_pair} | {theta:.6g} | {dj:.6g} | {iq:.6g} | {sc:.6g} | {mu:.6g} |".format(
                row=result["row"],
                packet=result["target_packet"],
                amp=result["amplitude_fraction"],
                dim=result["active_prefix_dimension"],
                pairs=result["cross_pair_count"],
                singular=result["singular_pair_count"],
                lam=result["max_lambda_on_grid"],
                best_pair=result["best_pair"],
                theta=result["best_theta"],
                dj=result["best_d_J0_at_zero"],
                iq=result["best_impurity_quadratic_coefficient"],
                sc=result["best_singular_constant_abs_dJ0_over_c"],
                mu=result["max_first_order_required_price_mu_star"],
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "If `singular pairs` is nonzero, the conductor flag is not stationary for",
        "the unpriced one-point objective in at least one cross-packet direction.",
        "Because packet impurity is quadratic at the conductor flag, the sampled",
        "frame-price frontier can become arbitrarily large near that direction",
        "(Theorem 3.3 of paper 25).  The rightmost column `max mu* (first-order",
        "cure)` is the per-row maximum of (one-sided descent rate of J0) / nu(A)",
        "over sampled plane directions, where nu(A)=2 for cross-packet plane",
        "rotations.  Only pairs with an actual descent direction contribute;",
        "kinky pairs whose central derivative is nonzero but whose one-sided",
        "rate is nonpositive in both directions contribute 0.  By Theorem 3.5",
        "of paper 25, augmenting the ledger with the first-order packet cost",
        "N(Q)=sum_{a!=b}||P_a Q P_b||_F at weight mu >= max mu* restores local",
        "minimality at the conductor flag with bounded required price.  This",
        "refines the theorem by excluding or separately pricing one-point local",
        "diagonalizers.  Compare: under quadratic-only impurity, the sampled",
        "max lambda diverges (column `max lambda on grid` blows up as theta",
        "shrinks); under first-order impurity, mu* remains finite.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default="f2-u2,f2-u3,f4-u2")
    parser.add_argument("--amplitudes", default="0.1,0.35,0.5")
    parser.add_argument("--thetas", default="1e-5,3e-5,1e-4,3e-4,1e-3,3e-3,1e-2")
    parser.add_argument("--epsilon", type=float, default=1e-6)
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
        print(
            f"{result['row']} {result['target_packet']} amp={result['amplitude_fraction']}: "
            f"singular={result['singular_pair_count']}/{result['cross_pair_count']}, "
            f"max_lambda={result['max_lambda_on_grid']:.6g}, "
            f"best_pair={result['best_pair']}, "
            f"dJ0={result['best_d_J0_at_zero']:.6g}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
