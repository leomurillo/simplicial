"""Held-out displacement test for Helmert/NZSBTL frame reuse.

The amplitude frontier shows that mixed flags can beat the conductor prefix
on a single Fourier-pure displacement, especially in top/full-prefix rows.
This script asks the next question:

    Does a mixed flag that looks good on one displacement remain good when
    reused on other displacement directions in the same conductor prefix?

That is the empirical distinction Paper 25 needs.  A local eigenframe is a
one-point diagonalizer.  A conductor frame is meant to be a reusable arithmetic
linearization.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Hashable

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
    random_orthogonal,
    safe_probability,
    summarize,
)
from verify_per_row_carry_vs_depth import inverse_dft  # noqa: E402


Label = Hashable
DEFAULT_JSON = Path("empirical/reports/helmert_heldout_frame_test.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_heldout_frame_test.md")


def parse_csv(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


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


def prefix_labels(
    packets: dict[str, tuple[Label, ...]],
    cond_order: tuple[str, ...],
    target_index: int,
) -> tuple[Label, ...]:
    return tuple(
        label
        for conductor in cond_order[: target_index + 1]
        for label in packets[conductor]
    )


def random_displacement(
    *,
    ring: Any,
    chi: Any,
    packets: dict[str, tuple[Label, ...]],
    cond_order: tuple[str, ...],
    target_packet: str,
    support: str,
    rng: np.random.Generator,
) -> tuple[dict[Label, float], dict[Label, float]]:
    target_index = cond_order.index(target_packet)
    if support == "packet":
        labels = packets[target_packet]
    elif support == "prefix":
        labels = prefix_labels(packets, cond_order, target_index)
    else:
        raise ValueError("support must be 'packet' or 'prefix'")

    coeff = rng.normal(size=len(labels))
    norm = float(np.linalg.norm(coeff))
    if norm <= 1e-15:
        coeff[0] = 1.0
        norm = 1.0
    # Match the energy scale of the packet/prefix indicator.
    coeff = coeff * (np.sqrt(len(labels)) / norm)
    h_hat = {label: 0.0 for label in ring.labels}
    for label, value in zip(labels, coeff):
        h_hat[label] = float(value)
    h_hat[ring.zero] = 0.0
    h = inverse_dft(h_hat, ring, chi)
    return h, h_hat


def setup_context(row_key: str) -> dict[str, Any]:
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
    return {
        "spec": spec,
        "ring": ring,
        "chi": chi,
        "packets": packets,
        "cond_order": cond_order,
        "modes": modes,
        "sizes": sizes,
        "basis": character_matrix(ring, modes, chi),
        "add_tensor": addition_tensor(ring, modes),
    }


def ledger_for_displacement(
    *,
    q: np.ndarray,
    context: dict[str, Any],
    target_packet: str,
    h_values: dict[Label, float],
    h_hat: dict[Label, float],
    amplitude_fraction: float,
    weights: dict[str, float],
) -> dict[str, float]:
    ring = context["ring"]
    chi = context["chi"]
    modes = context["modes"]
    target_index = context["cond_order"].index(target_packet)
    probability, _amplitude = safe_probability(h_values, ring, amplitude_fraction)
    probability_by_label = {
        label: float(probability[i])
        for i, label in enumerate(ring.labels)
    }
    reciprocal_values = {
        label: 1.0 / probability_by_label[label]
        for label in ring.labels
    }
    reciprocal_hat = dft(reciprocal_values, ring, chi)
    gram = fisher_gram(probability, context["basis"])
    return flag_ledger(
        q=q,
        gram=gram,
        sizes=context["sizes"],
        target_index=target_index,
        h_hat_vector=coefficient_vector(h_hat, modes),
        reciprocal_vector=coefficient_vector(reciprocal_hat, modes),
        add_tensor=context["add_tensor"],
        weights=weights,
    )


def j_without_mix(ledger: dict[str, float], weights: dict[str, float]) -> float:
    return ledger["J"] - weights["mix"] * ledger["mix_impurity"]


def evaluate_case(
    *,
    row_key: str,
    target_packet: str,
    flags: int,
    holdouts: int,
    seed: int,
    amplitude_fraction: float,
    support: str,
    weights: dict[str, float],
) -> dict[str, Any]:
    context = setup_context(row_key)
    ring = context["ring"]
    chi = context["chi"]
    packets = context["packets"]
    cond_order = context["cond_order"]
    sizes = context["sizes"]
    target_index = cond_order.index(target_packet)
    rng = np.random.default_rng(seed)

    train_h, train_h_hat = fourier_pure_displacement(packets, ring, chi, target_packet)
    conductor_q = np.eye(sum(sizes))
    conductor_train = ledger_for_displacement(
        q=conductor_q,
        context=context,
        target_packet=target_packet,
        h_values=train_h,
        h_hat=train_h_hat,
        amplitude_fraction=amplitude_fraction,
        weights=weights,
    )

    holdout_displacements = [
        random_displacement(
            ring=ring,
            chi=chi,
            packets=packets,
            cond_order=cond_order,
            target_packet=target_packet,
            support=support,
            rng=rng,
        )
        for _ in range(holdouts)
    ]
    conductor_holdout_ledgers = [
        ledger_for_displacement(
            q=conductor_q,
            context=context,
            target_packet=target_packet,
            h_values=h,
            h_hat=h_hat,
            amplitude_fraction=amplitude_fraction,
            weights=weights,
        )
        for h, h_hat in holdout_displacements
    ]
    conductor_holdout_mean = float(
        np.mean([ledger["J"] for ledger in conductor_holdout_ledgers])
    )
    conductor_holdout_j0_mean = float(
        np.mean([j_without_mix(ledger, weights) for ledger in conductor_holdout_ledgers])
    )

    records: list[dict[str, float]] = []
    train_winners = 0
    heldout_winners = 0
    train_winners_heldout_winners = 0
    heldout_break_even: list[float] = []
    for _ in range(flags):
        q = random_orthogonal(sum(sizes), rng)
        train_ledger = ledger_for_displacement(
            q=q,
            context=context,
            target_packet=target_packet,
            h_values=train_h,
            h_hat=train_h_hat,
            amplitude_fraction=amplitude_fraction,
            weights=weights,
        )
        holdout_ledgers = [
            ledger_for_displacement(
                q=q,
                context=context,
                target_packet=target_packet,
                h_values=h,
                h_hat=h_hat,
                amplitude_fraction=amplitude_fraction,
                weights=weights,
            )
            for h, h_hat in holdout_displacements
        ]
        holdout_mean = float(np.mean([ledger["J"] for ledger in holdout_ledgers]))
        holdout_j0_mean = float(np.mean([j_without_mix(ledger, weights) for ledger in holdout_ledgers]))
        impurity = train_ledger["mix_impurity"]
        if holdout_j0_mean < conductor_holdout_j0_mean and impurity > 1e-12:
            heldout_break_even.append((conductor_holdout_j0_mean - holdout_j0_mean) / impurity)
        else:
            heldout_break_even.append(0.0)

        train_win = train_ledger["J"] < conductor_train["J"]
        holdout_win = holdout_mean < conductor_holdout_mean
        train_winners += int(train_win)
        heldout_winners += int(holdout_win)
        train_winners_heldout_winners += int(train_win and holdout_win)
        records.append(
            {
                "train_J": train_ledger["J"],
                "train_margin": train_ledger["J"] - conductor_train["J"],
                "holdout_mean_J": holdout_mean,
                "holdout_margin": holdout_mean - conductor_holdout_mean,
                "mix_impurity": impurity,
                "holdout_lambda": heldout_break_even[-1],
            }
        )

    train_margins = [record["train_margin"] for record in records]
    holdout_margins = [record["holdout_margin"] for record in records]
    return {
        "row_key": row_key,
        "row": context["spec"].display,
        "target_packet": target_packet,
        "target_depth": target_index + 1,
        "active_prefix_dimension": sum(sizes[: target_index + 1]),
        "total_dimension": sum(sizes),
        "packet_sizes": dict(zip(cond_order, sizes)),
        "support": support,
        "amplitude_fraction": amplitude_fraction,
        "flags": flags,
        "holdouts": holdouts,
        "seed": seed,
        "conductor_train_J": conductor_train["J"],
        "conductor_holdout_mean_J": conductor_holdout_mean,
        "train_winner_count": train_winners,
        "heldout_winner_count": heldout_winners,
        "train_winner_heldout_winner_count": train_winners_heldout_winners,
        "train_margin": summarize(train_margins),
        "holdout_margin": summarize(holdout_margins),
        "heldout_lambda": summarize(heldout_break_even),
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_csv(args.rows)
    weights = ledger_weights(args)
    results: list[dict[str, Any]] = []
    for row_offset, key in enumerate(rows):
        context = setup_context(key)
        cond_order = context["cond_order"]
        for packet_offset, target_packet in enumerate(cond_order):
            if args.skip_lowest and packet_offset == 0:
                continue
            results.append(
                evaluate_case(
                    row_key=key,
                    target_packet=target_packet,
                    flags=args.flags,
                    holdouts=args.holdouts,
                    seed=args.seed + 1000 * row_offset + 37 * packet_offset,
                    amplitude_fraction=args.amplitude_fraction,
                    support=args.support,
                    weights=weights,
                )
            )
    return {
        "purpose": (
            "Held-out displacement test for reusable arithmetic frames: "
            "compare mixed flags selected/evaluated on a Fourier-pure training "
            "displacement against their mean score on random held-out Fourier "
            "directions in the same packet or prefix."
        ),
        "config": {
            "rows": rows,
            "flags": args.flags,
            "holdouts": args.holdouts,
            "seed": args.seed,
            "amplitude_fraction": args.amplitude_fraction,
            "support": args.support,
            "skip_lowest": args.skip_lowest,
            "ledger_weights": weights,
        },
        "results": results,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Held-Out Frame Test",
        "",
        "This audit tests whether mixed flags that can beat conductor on one",
        "Fourier-pure displacement remain competitive when reused on held-out",
        "Fourier directions in the same conductor support.",
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
        "| row | packet | active dim | train wins | held-out wins | train wins that hold out | held-out lambda max | train margin median | hold-out margin median |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        lines.append(
            "| {row} | {packet} | {dim} | {train}/{flags} | {held}/{flags} | "
            "{both}/{flags} | {lam:.6g} | {tm:.6g} | {hm:.6g} |".format(
                row=result["row"],
                packet=result["target_packet"],
                dim=result["active_prefix_dimension"],
                train=result["train_winner_count"],
                held=result["heldout_winner_count"],
                both=result["train_winner_heldout_winner_count"],
                flags=result["flags"],
                lam=result["heldout_lambda"]["max"],
                tm=result["train_margin"]["median"],
                hm=result["holdout_margin"]["median"],
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "Negative margins mean the sampled mixed flag beats conductor.  If many",
        "training wins disappear on held-out displacements, the mixed flags are",
        "acting like one-point diagonalizers.  If they continue to win on held-out",
        "directions, the current arithmetic ledger is missing a real reusable-frame",
        "cost or the conductor claim must be narrowed further.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default="f2-u2,f2-u3,f4-u2")
    parser.add_argument("--flags", type=int, default=500)
    parser.add_argument("--holdouts", type=int, default=25)
    parser.add_argument("--seed", type=int, default=20260515)
    parser.add_argument("--amplitude-fraction", type=float, default=0.35)
    parser.add_argument("--support", choices=["packet", "prefix"], default="prefix")
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
            f"{result['row']} {result['target_packet']}: "
            f"train={result['train_winner_count']}/{result['flags']}, "
            f"heldout={result['heldout_winner_count']}/{result['flags']}, "
            f"both={result['train_winner_heldout_winner_count']}/{result['flags']}, "
            f"heldout_lambda_max={result['heldout_lambda']['max']:.6g}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
