"""Native final-logit lens binning and conductor packet score.

This is the stronger T2-adjacent artifact because it begins with the model's
native full-vocabulary output distribution before applying any quotient map.
We extract the twelve month token log-scores from the saved final unembedding
distribution and score their conductor packets before binning.  The later
quotient binning/lifting zeros are analytic consequences of T1/T2 and should be
read as a projector sanity check, not as independent model evidence.

The stored artifact is probabilities, not raw logits.  We use log p(token) as
the score; after row-centering this differs from raw logits only by the
per-example log-partition constant, which has no nontrivial conductor energy.
"""

from __future__ import annotations

import argparse
import json
import math
import struct
from datetime import date
from pathlib import Path

import numpy as np


EPS = 1e-45
DEFAULT_QUOTIENTS = (2, 3, 4, 6, 12)
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
MONTH_TO_INDEX = {name: i for i, name in enumerate(MONTHS)}


def load_safetensors(path: Path) -> np.ndarray:
    with path.open("rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        data = f.read()
    key = next(k for k in header if k != "__metadata__")
    meta = header[key]
    dtype_map = {"F64": np.float64, "F32": np.float32, "F16": np.float16}
    if meta["dtype"] not in dtype_map:
        raise ValueError(f"Unsupported dtype: {meta['dtype']}")
    start, end = meta["data_offsets"]
    return np.frombuffer(data[start:end], dtype=dtype_map[meta["dtype"]]).reshape(meta["shape"]).copy()


def load_month_token_ids(path: Path) -> dict[str, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    found: dict[str, int] = {}
    for example in data["examples"]:
        for item in example["top_tokens"]:
            name = item["token"].strip()
            if name in MONTH_TO_INDEX:
                found[name] = int(item["token_id"])
    missing = [month for month in MONTHS if month not in found]
    if missing:
        raise ValueError(f"Could not recover token ids for months: {missing}")
    return {month: found[month] for month in MONTHS}


def load_month_labels(path: Path) -> np.ndarray:
    data = json.loads(path.read_text(encoding="utf-8"))
    labels = []
    for row in data["samples"]:
        label = row["raw_output"].strip()
        if label not in MONTH_TO_INDEX:
            raise ValueError(f"Unknown month label: {label}")
        labels.append(MONTH_TO_INDEX[label])
    return np.asarray(labels, dtype=int)


def conductor_packets(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {}
    for character in range(1, n):
        conductor = n // math.gcd(n, character)
        packets.setdefault(conductor, []).append(character)
    return {d: packets[d] for d in sorted(packets)}


def packet_energy(scores: np.ndarray, packets: dict[int, list[int]]) -> dict[int, float]:
    n = scores.shape[1]
    energy = {d: 0.0 for d in packets}
    for row in scores:
        centered = row - float(np.mean(row))
        coeff = np.fft.fft(centered) / math.sqrt(n)
        for d, indices in packets.items():
            energy[d] += float(np.sum(np.abs(coeff[indices]) ** 2).real)
    return energy


def energy_fractions(energy: dict[int, float]) -> dict[int, float]:
    total = sum(energy.values())
    if total <= 0.0:
        return {d: 0.0 for d in energy}
    return {d: energy[d] / total for d in energy}


def quotient_bin_log_scores(month_probs: np.ndarray, k: int) -> np.ndarray:
    """Bin month-token probabilities into C_k, log them, and lift to C_12."""

    n = month_probs.shape[1]
    coarse = np.zeros((month_probs.shape[0], k), dtype=float)
    for label in range(n):
        coarse[:, label % k] += month_probs[:, label]
    coarse_scores = np.log(np.maximum(coarse, EPS))
    lifted = np.zeros((month_probs.shape[0], n), dtype=float)
    for label in range(n):
        lifted[:, label] = coarse_scores[:, label % k]
    return lifted


def forbidden_fraction(fractions: dict[int, float], k: int) -> float:
    return float(sum(value for d, value in fractions.items() if k % d != 0))


def max_forbidden_energy(energy: dict[int, float], k: int) -> float:
    forbidden = [abs(value) for d, value in energy.items() if k % d != 0]
    return float(max(forbidden) if forbidden else 0.0)


def format_fraction_table(rows: dict[int | str, dict[int, float]]) -> list[str]:
    first = next(iter(rows.values()))
    conductors = sorted(first)
    lines = ["| condition | " + " | ".join(f"H_{d}" for d in conductors) + " |"]
    lines.append("|---|" + "|".join("---:" for _ in conductors) + "|")
    for name, values in rows.items():
        cells = " | ".join(f"{values[d]:.6f}" for d in conductors)
        lines.append(f"| {name} | {cells} |")
    return lines


def format_binning_table(rows: dict[int, dict]) -> list[str]:
    lines = [
        "| quotient k | native forbidden fraction before binning | after-bin forbidden fraction | after-bin max forbidden energy | quotient acc |",
        "|---:|---:|---:|---:|---:|",
    ]
    for k in sorted(rows):
        row = rows[k]
        lines.append(
            f"| {k} | {row['native_forbidden_fraction']:.6f} | "
            f"{row['after_forbidden_fraction']:.3e} | "
            f"{row['after_max_forbidden_energy']:.3e} | "
            f"{row['quotient_accuracy']:.3f} |"
        )
    return lines


def build_report(payload: dict) -> str:
    rows = {int(k): v for k, v in payload["quotient_results"].items()}
    fraction_rows: dict[int | str, dict[int, float]] = {
        "native full month logits": payload["native_packet_fractions"]
    }
    for k in sorted(rows):
        fraction_rows[f"after C12->C{k}->C12"] = rows[k]["after_packet_fractions"]

    token_lines = [
        f"- {month}: token id `{payload['month_token_ids'][month]}`"
        for month in MONTHS
    ]

    lines = [
        f"# Native Final-Logit Lens Binning Packet Score -- {payload['model_pretty']}",
        "",
        f"**Run date:** {payload['run_date']}",
        f"**Full-vocabulary distribution:** `{payload['full_output_dists']}`",
        f"**Samples:** `{payload['samples_path']}`",
        f"**Token-id source:** `{payload['top_logits_path']}`",
        f"**Examples:** {payload['n_examples']}",
        "",
        "## Experiment",
        "",
        "This uses the model's native final unembedding distribution.  The saved "
        "artifact stores probabilities over the full vocabulary; taking "
        "`log p(token)` gives logits up to a per-example additive constant, which "
        "vanishes after centering before conductor scoring.",
        "",
        "For each example, the twelve month token scores are packet-scored before "
        "binning.  That pre-bin packet profile is the model-facing measurement. "
        "Then the month-token probabilities are explicitly binned into the "
        "quotient classes `C_12 -> C_k`, converted back to log scores, lifted to "
        "twelve labels by `score_12[x] = score_k[x mod k]`, and packet-scored "
        "again as a projector sanity check.",
        "",
        "## Month Token IDs",
        "",
        *token_lines,
        "",
        "## Accuracy",
        "",
        f"- native twelve-month token accuracy: {payload['native_month_accuracy']:.3f}",
        "",
        "## Before/After Binning",
        "",
        *format_binning_table(rows),
        "",
        "## Packet Fractions",
        "",
        *format_fraction_table(fraction_rows),
        "",
        "## Reading",
        "",
        "Before binning, the native final month-token logits contain energy in "
        "all five nontrivial conductor packets; this is the falsifiable "
        "model-facing result.  After explicit quotient binning and lifting, "
        "every packet forbidden by `d not| k` is zero up to numerical floor, but "
        "that zero is forced by the bin-and-lift map.  The bridge to T2 is that "
        "the full native codomain can express the observed packet profile, while "
        "a binned quotient codomain discards exactly the packets excluded by its "
        "annihilator.",
        "",
        "This is a final-layer native logit-lens experiment, not a trained tuned "
        "lens across intermediate layers.  The remaining tuned-lens version would "
        "train layerwise affine translators to full vocabulary or month-token "
        "scores, then repeat this before/after quotient-binning packet score.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full-output-dists",
        type=Path,
        default=Path("months/baseline/full_output_dists.safetensors"),
    )
    parser.add_argument(
        "--samples",
        type=Path,
        default=Path("months/baseline/test_samples.json"),
    )
    parser.add_argument(
        "--top-logits",
        type=Path,
        default=Path("months/baseline/top_logits.json"),
    )
    parser.add_argument("--model-tag", default="llama31_8b")
    parser.add_argument("--model-pretty", default="Llama-3.1-8B")
    parser.add_argument(
        "--quotients",
        default=",".join(str(k) for k in DEFAULT_QUOTIENTS),
    )
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    n = 12
    quotients = [int(part.strip()) for part in args.quotients.split(",") if part.strip()]
    bad = [k for k in quotients if n % k != 0]
    if bad:
        raise ValueError(f"All quotients must divide {n}; got {bad}")

    full_probs = np.asarray(load_safetensors(args.full_output_dists), dtype=float)
    labels = load_month_labels(args.samples)
    token_ids = load_month_token_ids(args.top_logits)
    if full_probs.shape[0] != labels.size:
        raise ValueError(f"Distribution/sample mismatch: {full_probs.shape[0]} vs {labels.size}")

    month_ids = [token_ids[month] for month in MONTHS]
    month_probs = full_probs[:, month_ids]
    native_scores = np.log(np.maximum(month_probs, EPS))
    packets = conductor_packets(n)
    native_energy = packet_energy(native_scores, packets)
    native_fractions = energy_fractions(native_energy)
    native_pred = np.argmax(month_probs, axis=1)
    native_accuracy = float(np.mean(native_pred == labels))

    quotient_results: dict[int, dict] = {}
    for k in quotients:
        lifted_scores = quotient_bin_log_scores(month_probs, k)
        after_energy = packet_energy(lifted_scores, packets)
        after_fractions = energy_fractions(after_energy)
        coarse_probs = np.zeros((month_probs.shape[0], k), dtype=float)
        for label in range(n):
            coarse_probs[:, label % k] += month_probs[:, label]
        quotient_pred = np.argmax(coarse_probs, axis=1)
        quotient_labels = labels % k
        quotient_results[k] = {
            "native_forbidden_fraction": forbidden_fraction(native_fractions, k),
            "after_forbidden_fraction": forbidden_fraction(after_fractions, k),
            "after_max_forbidden_energy": max_forbidden_energy(after_energy, k),
            "quotient_accuracy": float(np.mean(quotient_pred == quotient_labels)),
            "after_packet_energy": after_energy,
            "after_packet_fractions": after_fractions,
        }

    payload = {
        "run_date": date.today().isoformat(),
        "full_output_dists": str(args.full_output_dists),
        "samples_path": str(args.samples),
        "top_logits_path": str(args.top_logits),
        "model_tag": args.model_tag,
        "model_pretty": args.model_pretty,
        "n_examples": int(full_probs.shape[0]),
        "month_token_ids": token_ids,
        "native_month_accuracy": native_accuracy,
        "native_packet_energy": native_energy,
        "native_packet_fractions": native_fractions,
        "quotient_results": quotient_results,
    }

    report_path = args.report or Path("empirical/reports") / f"native_logit_lens_binning_months_{args.model_tag}.md"
    json_path = args.json or Path("empirical/reports") / f"native_logit_lens_binning_months_{args.model_tag}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(f"Native month-token accuracy: {native_accuracy:.3f}")
    for k in quotients:
        row = quotient_results[k]
        print(
            f"k={k:2d} native_forbidden={row['native_forbidden_fraction']:.3f} "
            f"after_forbidden={row['after_forbidden_fraction']:.3e} "
            f"quotient_acc={row['quotient_accuracy']:.3f}"
        )


if __name__ == "__main__":
    main()
