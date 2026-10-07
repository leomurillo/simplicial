"""Local-row nonuniform Fisher-conductor orthogonality loci.

This is the local finite-ring analogue of nonuniform_orthogonality_loci.py.
For each local row supported by the adjacency constructor, it enumerates the
reciprocal Fourier modes eta that preserve conductor labels under translation
on every nontrivial character label where eta + chi remains nontrivial.

These eta are the only modes allowed in the reciprocal density m_p = 1/p if
the fixed conductor packets are to remain mutually Fisher-orthogonal at p.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from local_adjacency_constructor import (
    FiniteLocalRing,
    make_f16_ring,
    make_f2_u4_ring,
    make_f2_u5_ring,
    make_f4_u2_ring,
    make_f4_u3_ring,
    make_f8_u2_ring,
)


DEFAULT_REPORT = Path("empirical/reports/nonuniform_orthogonality_loci_local.md")
DEFAULT_JSON = Path("empirical/reports/nonuniform_orthogonality_loci_local.json")

RING_FACTORIES: dict[str, Callable[[], FiniteLocalRing]] = {
    "f4-u2": make_f4_u2_ring,
    "f16": make_f16_ring,
    "f2-u4": make_f2_u4_ring,
    "f2-u5": make_f2_u5_ring,
    "f4-u3": make_f4_u3_ring,
    "f8-u2": make_f8_u2_ring,
}


def allowed_modes(ring: FiniteLocalRing) -> tuple[list[Any], dict[str, dict[str, str]]]:
    allowed: list[Any] = []
    witnesses: dict[str, dict[str, str]] = {}

    for eta in ring.labels:
        witness: dict[str, str] | None = None
        for source in ring.nontrivial:
            target = ring.add(eta, source)
            if target == ring.zero:
                continue
            source_conductor = ring.conductor(source)
            target_conductor = ring.conductor(target)
            if source_conductor != target_conductor:
                witness = {
                    "eta": ring.label_name(eta),
                    "source": ring.label_name(source),
                    "target": ring.label_name(target),
                    "source_conductor": source_conductor,
                    "target_conductor": target_conductor,
                }
                break

        if witness is None:
            allowed.append(eta)
        else:
            witnesses[ring.label_name(eta)] = witness

    return allowed, witnesses


def allowed_orbits(
    ring: FiniteLocalRing, allowed: list[Any]
) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    allowed_set = set(allowed)
    remaining = set(allowed)
    orbits: list[dict[str, object]] = []
    stability_failures: list[dict[str, str]] = []

    while remaining:
        seed = min(remaining, key=ring.label_name)
        orbit = {ring.apply(action, seed) for action in ring.normalizer_actions}
        for image in orbit:
            if image not in allowed_set:
                stability_failures.append(
                    {
                        "seed": ring.label_name(seed),
                        "image": ring.label_name(image),
                        "image_conductor": ring.conductor(image),
                    }
                )
        present = orbit & allowed_set
        remaining -= present
        orbits.append(
            {
                "representative": ring.label_name(seed),
                "size": len(present),
                "members": [ring.label_name(label) for label in sorted(present, key=ring.label_name)],
            }
        )

    return orbits, stability_failures


def row(key: str, ring: FiniteLocalRing) -> dict[str, object]:
    allowed, witnesses = allowed_modes(ring)
    orbits, stability_failures = allowed_orbits(ring, allowed)
    packets: dict[str, int] = {}
    for label in ring.nontrivial:
        conductor = ring.conductor(label)
        packets[conductor] = packets.get(conductor, 0) + 1

    if len(packets) == 1:
        reading = "single-packet: block orthogonality is vacuous"
    elif len(allowed) == 1 and allowed[0] == ring.zero:
        reading = "rigid: only constant reciprocal density preserves all blocks"
    else:
        reading = "structured locus: nonconstant reciprocal modes remain"

    return {
        "key": key,
        "ring": ring.name,
        "label_count": len(ring.labels),
        "packets": dict(sorted(packets.items())),
        "allowed_reciprocal_modes": [ring.label_name(label) for label in allowed],
        "allowed_count": len(allowed),
        "allowed_normalizer_orbits": orbits,
        "allowed_normalizer_orbit_count": len(orbits),
        "allowed_normalizer_stability_failures": stability_failures,
        "disallowed_count": len(ring.labels) - len(allowed),
        "disallowed_witnesses": witnesses,
        "reading": reading,
    }


def write_json(rows: list[dict[str, object]], path: Path) -> None:
    payload = {
        "criterion": (
            "A reciprocal mode eta is allowed iff translation chi -> eta+chi "
            "preserves conductor labels for every nontrivial chi whose image "
            "is nontrivial."
        ),
        "rows": rows,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def check_payload(rows: list[dict[str, object]], path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    recorded = {row["key"]: row for row in payload["rows"]}
    computed = {row["key"]: row for row in rows}
    if set(recorded) != set(computed):
        raise AssertionError(
            f"row keys differ: recorded={sorted(recorded)} computed={sorted(computed)}"
        )

    checked_fields = [
        "ring",
        "label_count",
        "packets",
        "allowed_reciprocal_modes",
        "allowed_count",
        "allowed_normalizer_orbit_count",
        "allowed_normalizer_stability_failures",
        "disallowed_count",
        "disallowed_witnesses",
        "reading",
    ]
    for key in sorted(computed):
        for field in checked_fields:
            if recorded[key].get(field) != computed[key].get(field):
                raise AssertionError(
                    f"{key}: field {field} differs\n"
                    f"recorded={recorded[key].get(field)!r}\n"
                    f"computed={computed[key].get(field)!r}"
                )
        if computed[key]["allowed_normalizer_stability_failures"]:
            raise AssertionError(f"{key}: allowed modes are not normalizer-stable")


def write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    lines = [
        "# Local Nonuniform Fisher-Conductor Orthogonality Loci",
        "",
        "## Criterion",
        "",
        "For a nonuniform categorical point `p`, set `m_p = 1/p`.  A fixed",
        "conductor-packet splitting remains mutually Fisher-orthogonal exactly",
        "when `hat(m_p)` is supported only on reciprocal modes `eta` whose",
        "translation action preserves conductor labels on all nontrivial",
        "character labels.",
        "",
        "This report enumerates those allowed reciprocal modes for local rows",
        "already supported by the quotient-character adjacency constructor.",
        "",
        "## Atlas",
        "",
        "| key | ring | packets | allowed reciprocal modes | normalizer orbits | reading |",
        "|---|---|---|---|---:|---|",
    ]

    for item in rows:
        packets = ", ".join(f"{name}:{size}" for name, size in item["packets"].items())
        allowed = ", ".join(item["allowed_reciprocal_modes"])
        lines.append(
            "| {key} | {ring} | {packets} | {allowed} | {orbits} | {reading} |".format(
                key=item["key"],
                ring=item["ring"],
                packets=packets,
                allowed=allowed,
                orbits=item["allowed_normalizer_orbit_count"],
                reading=item["reading"],
            )
        )

    lines += ["", "## Allowed-Mode Normalizer Orbits", ""]
    for item in rows:
        lines += [f"### {item['key']}", ""]
        lines += ["| representative | size | members |", "|---|---:|---|"]
        for orbit in item["allowed_normalizer_orbits"]:
            lines.append(
                "| {representative} | {size} | {members} |".format(
                    representative=orbit["representative"],
                    size=orbit["size"],
                    members=", ".join(orbit["members"]),
                )
            )
        failures = item["allowed_normalizer_stability_failures"]
        if failures:
            lines += ["", "**Normalizer stability failures:**"]
            for failure in failures:
                lines.append(
                    f"- {failure['seed']} -> {failure['image']} "
                    f"({failure['image_conductor']})"
                )
        lines.append("")

    lines += [
        "",
        "## First Bad Witnesses",
        "",
        "Each witness shows a reciprocal mode `eta` translating one nontrivial",
        "character label into a different conductor packet.",
        "",
    ]

    for item in rows:
        witnesses = item["disallowed_witnesses"]
        if not witnesses:
            continue
        lines += [f"### {item['key']}", "", "| eta | witness |", "|---|---|"]
        for eta, witness in sorted(witnesses.items()):
            lines.append(
                "| {eta} | {source} ({source_conductor}) -> "
                "{target} ({target_conductor}) |".format(**witness)
            )
        lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rings",
        default=",".join(RING_FACTORIES),
        help="comma-separated ring keys",
    )
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument(
        "--check",
        type=Path,
        default=None,
        help="recompute and compare against an existing JSON report",
    )
    args = parser.parse_args()

    keys = [key.strip() for key in args.rings.split(",") if key.strip()]
    unknown = sorted(set(keys) - set(RING_FACTORIES))
    if unknown:
        raise ValueError(f"unknown ring keys: {', '.join(unknown)}")

    rows = [row(key, RING_FACTORIES[key]()) for key in keys]
    if args.check is not None:
        check_payload(rows, args.check)
        print(f"checked {args.check}")
        return

    write_json(rows, args.json)
    write_markdown(rows, args.report)

    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
