"""Cyclic nonuniform Fisher-conductor orthogonality loci.

For a finite cyclic output algebra C_N, conductor-block Fisher orthogonality at
a nonuniform categorical point p is controlled by the Fourier support of 1/p.
This script enumerates the reciprocal Fourier modes r for which multiplication
by character r never sends a nontrivial character from one conductor packet to
a different conductor packet.

Those modes are exactly the modes allowed to appear in the reciprocal density
m_p = 1/p if the fixed conductor packets are to remain mutually
Fisher-orthogonal.  The positivity/normalization locus is then:

    p_x = (1 / m_x) / sum_y (1 / m_y),

where m is positive and its Fourier support is contained in the allowed modes.
"""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path


DEFAULT_REPORT = Path("empirical/reports/nonuniform_orthogonality_loci_cyclic.md")
DEFAULT_JSON = Path("empirical/reports/nonuniform_orthogonality_loci_cyclic.json")


def conductor(n: int, k: int) -> int:
    """Conductor of the character k on C_n."""

    k %= n
    if k == 0:
        return 1
    return n // gcd(n, k)


def allowed_reciprocal_modes(n: int) -> tuple[list[int], dict[int, dict[str, int]]]:
    """Return allowed modes and one bad witness for every disallowed mode."""

    allowed: list[int] = []
    witnesses: dict[int, dict[str, int]] = {}

    for r in range(n):
        witness: dict[str, int] | None = None
        for source in range(1, n):
            target = (source + r) % n
            if target == 0:
                continue
            source_conductor = conductor(n, source)
            target_conductor = conductor(n, target)
            if source_conductor != target_conductor:
                witness = {
                    "source": source,
                    "target": target,
                    "source_conductor": source_conductor,
                    "target_conductor": target_conductor,
                }
                break
        if witness is None:
            allowed.append(r)
        else:
            witnesses[r] = witness

    return allowed, witnesses


def row(n: int) -> dict[str, object]:
    allowed, witnesses = allowed_reciprocal_modes(n)
    conductors = sorted({conductor(n, k) for k in range(1, n)})

    if len(conductors) == 1:
        reading = "prime/single-packet: block orthogonality is vacuous"
    elif allowed == [0]:
        reading = "rigid: only constant reciprocal density preserves all blocks"
    else:
        reading = "structured locus: nonconstant reciprocal modes remain"

    return {
        "group": f"C_{n}",
        "n": n,
        "conductors": conductors,
        "allowed_reciprocal_modes": allowed,
        "disallowed_witnesses": witnesses,
        "reading": reading,
    }


def write_json(rows: list[dict[str, object]], path: Path) -> None:
    payload = {
        "theorem_assist": (
            "Conductor blocks B_d and B_e are Fisher-orthogonal at p iff "
            "the Fourier transform of m_p=1/p vanishes on every quotient "
            "psi*chi^{-1} with chi in B_d, psi in B_e, d != e."
        ),
        "rows": rows,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    lines = [
        "# Cyclic Nonuniform Fisher-Conductor Orthogonality Loci",
        "",
        "## Criterion",
        "",
        "Let `m_p = 1/p`.  In additive-character coordinates,",
        "",
        "```text",
        "g_p(chi, psi) = hat(m_p)(psi chi^{-1}).",
        "```",
        "",
        "Therefore two conductor packets remain Fisher-orthogonal at a",
        "nonuniform point exactly when `hat(m_p)` vanishes on every quotient",
        "`psi chi^{-1}` connecting the two packets.  Equivalently, the allowed",
        "reciprocal Fourier modes are those that preserve conductor labels on",
        "all nontrivial character lines.",
        "",
        "The actual probability locus is nonlinear: choose a positive reciprocal",
        "density `m` supported only on allowed modes, then normalize",
        "`p_x = (1/m_x) / sum_y (1/m_y)`.",
        "",
        "## Cyclic Atlas",
        "",
        "| group | conductors | allowed reciprocal modes | reading |",
        "|---|---|---|---|",
    ]

    for item in rows:
        lines.append(
            "| {group} | {conductors} | {allowed} | {reading} |".format(
                group=item["group"],
                conductors=", ".join(str(x) for x in item["conductors"]),
                allowed=", ".join(str(x) for x in item["allowed_reciprocal_modes"]),
                reading=item["reading"],
            )
        )

    lines += [
        "",
        "## First Bad Witnesses",
        "",
        "For each disallowed reciprocal mode `r`, the witness `k -> k+r` shows",
        "a conductor-changing character translation.",
        "",
    ]

    for item in rows:
        witnesses = item["disallowed_witnesses"]
        if not witnesses:
            continue
        lines += [f"### {item['group']}", ""]
        lines += ["| mode r | witness |", "|---:|---|"]
        for mode, witness in sorted(witnesses.items(), key=lambda kv: int(kv[0])):
            lines.append(
                "| {mode} | {source} cond {source_conductor} -> "
                "{target} cond {target_conductor} |".format(
                    mode=mode,
                    source=witness["source"],
                    target=witness["target"],
                    source_conductor=witness["source_conductor"],
                    target_conductor=witness["target_conductor"],
                )
            )
        lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-n", type=int, default=2)
    parser.add_argument("--max-n", type=int, default=24)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()

    if args.min_n < 2:
        raise ValueError("--min-n must be at least 2")
    if args.max_n < args.min_n:
        raise ValueError("--max-n must be >= --min-n")

    rows = [row(n) for n in range(args.min_n, args.max_n + 1)]
    write_json(rows, args.json)
    write_markdown(rows, args.report)

    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
