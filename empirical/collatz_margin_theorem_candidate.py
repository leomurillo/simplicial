"""Synthesis report for the Collatz margin-sign theorem candidate.

This script does not try to prove Collatz.  It packages the exact identities
behind the margin quotient

    q_w = (r_w(2^S - 3^m) - C_w) / 2^(S+1)

and stress-checks the proposed theorem:

    every nontrivial contracting carry word has q_w > 0.

The old cousin/path notes force a useful split.  The q=0 case is exactly the
positive periodic/cycle obstruction, already known to be the hard zero-orbit
problem.  The genuinely new descent-side candidate is therefore

    q_w >= 0 for every contracting carry word,

with equality handled by the cycle-side divisibility theory.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)


def log2_int(value: int) -> float:
    if value <= 0:
        return float("-inf")
    return math.log2(value)


def word_runs(word: tuple[int, ...]) -> list[tuple[int, int]]:
    if not word:
        return []
    runs: list[tuple[int, int]] = []
    current = word[0]
    count = 1
    for carry in word[1:]:
        if carry == current:
            count += 1
            continue
        runs.append((current, count))
        current = carry
        count = 1
    runs.append((current, count))
    return runs


def word_signature(word: tuple[int, ...], limit: int = 14) -> str:
    runs = word_runs(word)
    parts = [
        str(carry) if count == 1 else f"{carry}^{count}"
        for carry, count in runs
    ]
    if len(parts) <= limit:
        return "(" + " ".join(parts) + ")"
    head = " ".join(parts[: limit // 2])
    tail = " ".join(parts[-(limit // 2) :])
    return f"({head} ... {tail})"


def cocycle_for_word(word: tuple[int, ...]) -> tuple[int, int, int, int]:
    total_depth = 0
    cocycle = 0
    for carry in word:
        cocycle = 3 * cocycle + (1 << total_depth)
        total_depth += carry
    length = len(word)
    return length, total_depth, 3**length, cocycle


def margin_data(word: tuple[int, ...]) -> dict[str, Any] | None:
    length, total_depth, multiplier, cocycle = cocycle_for_word(word)
    denominator_power = 1 << total_depth
    denominator = denominator_power - multiplier
    if denominator <= 0:
        return None
    modulus = denominator_power << 1
    residue = ((denominator_power - cocycle) * pow(multiplier, -1, modulus)) % modulus
    first_n = residue if residue > 0 else modulus
    numerator = multiplier * first_n + cocycle
    if numerator % denominator_power:
        raise AssertionError("domain residue failed divisibility")
    image = numerator // denominator_power
    margin = first_n * denominator - cocycle
    if margin % modulus:
        raise AssertionError("margin quotient is not integral")
    q = margin // modulus
    return {
        "word": list(word),
        "signature": word_signature(word),
        "length": length,
        "total_depth": total_depth,
        "height": total_depth - length * LOG2_3,
        "cocycle": str(cocycle),
        "denominator": str(denominator),
        "residue": str(residue),
        "first_n": str(first_n),
        "image": str(image),
        "q": str(q),
        "q_int": q,
        "q_log2_abs": log2_int(abs(q)),
        "cap_log2": log2_int(cocycle // denominator),
        "first_n_log2": log2_int(first_n),
        "image_log2": log2_int(image),
        "descent": first_n - image,
    }


def theorem_family_rows(max_length: int) -> list[dict[str, Any]]:
    """Verify the q=1 lower-envelope family (1,4,2,...,2)."""

    rows = []
    for length in range(2, max_length + 1):
        word = (1, 4) + ((2,) * (length - 2))
        data = margin_data(word)
        if data is None:
            raise AssertionError("q=1 family unexpectedly noncontracting")
        rows.append(data)
    return rows


def trivial_zero_rows(max_length: int) -> list[dict[str, Any]]:
    rows = []
    for length in range(1, max_length + 1):
        data = margin_data((2,) * length)
        if data is None:
            raise AssertionError("trivial family unexpectedly noncontracting")
        rows.append(data)
    return rows


def random_word_with_total(length: int, total_depth: int, max_carry: int) -> tuple[int, ...]:
    word = [1] * length
    remaining = total_depth - length
    while remaining:
        index = random.randrange(length)
        if word[index] >= max_carry:
            continue
        word[index] += 1
        remaining -= 1
    random.shuffle(word)
    return tuple(word)


def stress_random(
    samples: int,
    max_length: int,
    max_carry: int,
    seed: int,
) -> dict[str, Any]:
    random.seed(seed)
    seen_contracting = 0
    min_positive: dict[str, Any] | None = None
    bad: dict[str, Any] | None = None

    for _ in range(samples):
        length = random.randint(1, max_length)
        if random.random() < 0.7:
            base = math.floor(length * LOG2_3) + random.randint(1, max(2, length // 3 + 2))
            total_depth = max(length, min(length * max_carry, base))
            word = random_word_with_total(length, total_depth, max_carry)
        else:
            word = tuple(random.randint(1, max_carry) for _index in range(length))

        data = margin_data(word)
        if data is None:
            continue
        seen_contracting += 1
        q = int(data["q_int"])
        if q <= 0 and not all(carry == 2 for carry in word):
            bad = data
            break
        if q > 0 and (
            min_positive is None or q < int(min_positive["q_int"])
        ):
            min_positive = data

    return {
        "samples": samples,
        "max_length": max_length,
        "max_carry": max_carry,
        "seed": seed,
        "contracting_seen": seen_contracting,
        "bad": bad,
        "min_positive": min_positive,
    }


def load_margin_summary(path: Path | None) -> dict[str, Any] | None:
    if path is None or not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        "path": str(path),
        "settings": payload.get("settings"),
        "expanding_words": payload.get("expanding_words"),
        "totals": payload.get("totals"),
    }


def rounded(value: object) -> object:
    if isinstance(value, float):
        if math.isinf(value):
            return "inf" if value > 0 else "-inf"
        return round(value, 10)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    return value


def make_family_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| word | m | S | q | n0 | image | descent |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['signature']}` | {row['length']} | {row['total_depth']} | "
            f"{row['q']} | {row['first_n']} | {row['image']} | {row['descent']} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    margin_summary = payload["margin_summary"]
    stress = payload["random_stress"]
    family_last = payload["q1_family"][-1]
    trivial_last = payload["trivial_zero_family"][-1]

    lines = [
        "# Collatz Margin Theorem Candidate",
        "",
        "## Theorem Split",
        "",
        "Candidate:",
        "",
        "```text",
        "For every nontrivial contracting carry word w, q_w > 0.",
        "```",
        "",
        "The old research notes force a sharper split.  The equality case `q_w = 0` is exactly the positive periodic/cycle obstruction: `U_w(r_w)=r_w`, equivalently `2^S-3^m` divides `C_w`.  That is the cycle-side zero-orbit problem from the notes.  The new descent-side theorem candidate is therefore:",
        "",
        "```text",
        "For every contracting carry word w, q_w >= 0.",
        "Equality occurs only on the trivial (2)^m family if the positive cycle conjecture holds.",
        "```",
        "",
        "## Exact Identities",
        "",
        "Let `D=2^S-3^m`, `M=2^(S+1)`, and choose the exact domain residue `r_w` by",
        "",
        "```text",
        "3^m r_w + C_w == 2^S mod M.",
        "```",
        "",
        "For contracting words `D>0`, define `y_w=U_w(r_w)`.  Then",
        "",
        "```text",
        "D r_w - C_w = M q_w",
        "q_w = (r_w - y_w) / 2",
        "```",
        "",
        "So the sign of `q_w` is not an approximation.  It is exactly the sign of descent at the first positive integer in the carry cylinder.",
        "",
        "## Heavy Census Imported",
        "",
    ]

    if margin_summary is None:
        lines += [
            "No margin-lattice census JSON was supplied.",
            "",
        ]
    else:
        totals = margin_summary["totals"]
        settings = margin_summary["settings"]
        lines += [
            f"- source: `{margin_summary['path']}`",
            f"- settings: `{settings}`",
            f"- contracting words: `{totals['contracting_words']}`",
            f"- positive q: `{totals['positive_q']}`",
            f"- zero q: `{totals['zero_q']}`",
            f"- trivial zero q: `{totals['trivial_zero_q']}`",
            f"- nontrivial zero q: `{totals['nontrivial_zero_q']}`",
            f"- negative q: `{totals['negative_q']}`",
            f"- primitive negative q: `{totals['primitive_negative_q']}`",
            "",
        ]

    lines += [
        "## Random Stress",
        "",
        f"- samples: `{stress['samples']}`",
        f"- contracting samples seen: `{stress['contracting_seen']}`",
        f"- max length: `{stress['max_length']}`",
        f"- max carry: `{stress['max_carry']}`",
        f"- seed: `{stress['seed']}`",
        f"- bad nontrivial q<=0 sample: `{stress['bad'] is not None}`",
        "",
    ]
    if stress["min_positive"] is not None:
        row = stress["min_positive"]
        lines += [
            "Smallest positive `q` seen in random stress:",
            "",
            f"- word: `{row['signature']}`",
            f"- length/depth: `{row['length']}, {row['total_depth']}`",
            f"- q: `{row['q']}`",
            "",
        ]

    lines += [
        "## Lower-Envelope Family",
        "",
        "The visible `q=1` lower envelope is not mysterious.  The word",
        "",
        "```text",
        "(1, 4, 2, 2, ..., 2)",
        "```",
        "",
        "maps `3 -> 5 -> 1 -> 1 -> ... -> 1`, so `q=(3-1)/2=1` for every length at least 2.  This gives an infinite positive-margin family exactly on the lower edge.",
        "",
        *make_family_table(payload["q1_family"][: min(12, len(payload["q1_family"]))]),
        "",
        f"Verified through length `{family_last['length']}`; last row has `q={family_last['q']}`.",
        "",
        "## Equality Family",
        "",
        "The trivial equality family is `(2)^m`, where the first representative is `1` and the image is also `1`.",
        "",
        *make_family_table(payload["trivial_zero_family"][: min(12, len(payload["trivial_zero_family"]))]),
        "",
        f"Verified through length `{trivial_last['length']}`; last row has `q={trivial_last['q']}`.",
        "",
        "## Proof Target",
        "",
        "A proof of the full candidate naturally decomposes into two lemmas:",
        "",
        "```text",
        "Descent-margin lemma: q_w >= 0 for every contracting carry word.",
        "Cycle-zero lemma: q_w = 0 only for the trivial (2)^m positive cycle.",
        "```",
        "",
        "The second lemma is exactly the old notes' cycle-side divisibility problem.  The first lemma is the new thing we can attack directly with the domain-cylinder algebra.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_margin_theorem_candidate.py --samples {payload['settings']['samples']} --max-length {payload['settings']['max_length']} --max-carry {payload['settings']['max_carry']} --family-length {payload['settings']['family_length']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_margin_json() -> Path:
    return Path("empirical/reports/collatz_margin_lattice_L12_S25_K8.json")


def default_report_path() -> Path:
    return Path("empirical/reports/collatz_margin_theorem_candidate.md")


def default_json_path() -> Path:
    return Path("empirical/reports/collatz_margin_theorem_candidate.json")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--margin-json", type=Path, default=default_margin_json())
    parser.add_argument("--samples", type=int, default=500000)
    parser.add_argument("--max-length", type=int, default=120)
    parser.add_argument("--max-carry", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260513)
    parser.add_argument("--family-length", type=int, default=120)
    parser.add_argument("--report", type=Path, default=default_report_path())
    parser.add_argument("--json", type=Path, default=default_json_path())
    args = parser.parse_args()

    if args.samples < 1:
        raise ValueError("--samples must be positive")
    if args.max_length < 1:
        raise ValueError("--max-length must be positive")
    if args.max_carry < 2:
        raise ValueError("--max-carry must be at least 2")
    if args.family_length < 2:
        raise ValueError("--family-length must be at least 2")

    payload = {
        "settings": {
            "margin_json": str(args.margin_json),
            "samples": args.samples,
            "max_length": args.max_length,
            "max_carry": args.max_carry,
            "seed": args.seed,
            "family_length": args.family_length,
        },
        "margin_summary": load_margin_summary(args.margin_json),
        "random_stress": stress_random(
            samples=args.samples,
            max_length=args.max_length,
            max_carry=args.max_carry,
            seed=args.seed,
        ),
        "q1_family": theorem_family_rows(args.family_length),
        "trivial_zero_family": trivial_zero_rows(args.family_length),
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(make_report(payload), encoding="utf-8")
    args.json.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(json.dumps(rounded(payload["random_stress"]), indent=2))


if __name__ == "__main__":
    main()
