"""Build empirical weekday centroids from a model probability dump.

This is the handoff script for the Wurgaft/Paper 9 weekday probe.  It does
not run a model.  Instead it records the 49 prompt cases and turns a raw
next-token probability/logprob dump into the seven-by-seven centroid matrix
expected by ``compute_weekdays_K_CH.py``.

Accepted dump shape:

    {
      "metadata": {...},
      "token_bins": {"Monday": [" Monday", "Monday"], ...},  # optional
      "records": [
        {
          "start_day": "Monday",
          "offset": 1,
          "weekday_probs": {"Monday": 0.01, ...}
        }
      ]
    }

The records may also use ``weekday_logprobs``, ``token_probs``, or
``token_logprobs``.  Token dictionaries are binned by exact token text using
the provided top-level ``token_bins`` or the default leading-space/no-space
weekday names.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from compute_weekdays_K_CH import WEEKDAYS


DAY_TO_INDEX = {day: index for index, day in enumerate(WEEKDAYS)}
DEFAULT_TEMPLATE = (
    "What day of the week is {offset} {day_word} after {start_day}? "
    "Answer with one weekday name:"
)


@dataclass(frozen=True)
class BinnedRecord:
    start_day: str
    offset: int | None
    correct_day: str
    weekday_probs: list[float]
    other_probability: float | None


def normalize_day(value: Any, field_name: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a weekday string")
    folded = value.strip().casefold()
    for day in WEEKDAYS:
        if day.casefold() == folded:
            return day
    raise ValueError(f"{field_name} is not a recognized weekday: {value!r}")


def correct_day_from_case(record: dict[str, Any]) -> tuple[str, int | None, str]:
    start_day = normalize_day(record.get("start_day"), "start_day")
    offset_value = record.get("offset")
    if offset_value is None:
        correct_raw = (
            record.get("correct_day")
            or record.get("answer_day")
            or record.get("target_day")
        )
        return start_day, None, normalize_day(correct_raw, "correct_day")

    offset = int(offset_value)
    if offset < 1 or offset > 7:
        raise ValueError(f"offset must be in 1..7, got {offset}")
    correct_day = WEEKDAYS[(DAY_TO_INDEX[start_day] + offset) % len(WEEKDAYS)]
    explicit_correct = (
        record.get("correct_day")
        or record.get("answer_day")
        or record.get("target_day")
    )
    if explicit_correct is not None:
        explicit_day = normalize_day(explicit_correct, "correct_day")
        if explicit_day != correct_day:
            raise ValueError(
                f"record says correct_day={explicit_day}, but "
                f"{offset} after {start_day} is {correct_day}"
            )
    return start_day, offset, correct_day


def default_token_bins(include_case_variants: bool) -> dict[str, list[str]]:
    bins: dict[str, list[str]] = {}
    for day in WEEKDAYS:
        variants = [day, " " + day]
        if include_case_variants:
            variants.extend([day.lower(), " " + day.lower(), day.upper(), " " + day.upper()])
        bins[day] = variants
    return bins


def load_payload(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return {"records": payload}
    if not isinstance(payload, dict):
        raise ValueError("dump JSON must be a list of records or an object")
    return payload


def as_probability_map(values: Any, field_name: str, log_values: bool) -> dict[str, float]:
    if not isinstance(values, dict):
        raise ValueError(f"{field_name} must be an object/dictionary")
    out: dict[str, float] = {}
    for key, raw in values.items():
        value = float(raw)
        if log_values:
            value = math.exp(value)
        if value < 0.0 or not math.isfinite(value):
            raise ValueError(f"{field_name}[{key!r}] is not a finite nonnegative value")
        out[str(key)] = value
    return out


def bin_weekday_probs(
    record: dict[str, Any],
    token_bins: dict[str, list[str]],
) -> tuple[list[float], float | None]:
    if "weekday_probs" in record:
        values = as_probability_map(record["weekday_probs"], "weekday_probs", False)
        probs = [values.get(day, values.get(day.lower(), 0.0)) for day in WEEKDAYS]
    elif "weekday_logprobs" in record:
        values = as_probability_map(record["weekday_logprobs"], "weekday_logprobs", True)
        probs = [values.get(day, values.get(day.lower(), 0.0)) for day in WEEKDAYS]
    elif "token_probs" in record:
        values = as_probability_map(record["token_probs"], "token_probs", False)
        probs = [sum(values.get(token, 0.0) for token in token_bins[day]) for day in WEEKDAYS]
    elif "token_logprobs" in record:
        values = as_probability_map(record["token_logprobs"], "token_logprobs", True)
        probs = [sum(values.get(token, 0.0) for token in token_bins[day]) for day in WEEKDAYS]
    else:
        raise ValueError(
            "each record needs weekday_probs, weekday_logprobs, token_probs, "
            "or token_logprobs"
        )

    weekday_mass = sum(probs)
    if weekday_mass <= 0.0:
        raise ValueError("weekday bin mass is zero for a record")

    other_raw = record.get("other_probability", record.get("other_prob"))
    if other_raw is not None:
        other_probability = float(other_raw)
    else:
        total_probability = record.get("total_probability", record.get("total_prob"))
        if total_probability is None:
            other_probability = None
        else:
            other_probability = max(0.0, float(total_probability) - weekday_mass)

    return probs, other_probability


def load_records(
    dump_path: Path,
    include_case_variants: bool,
) -> tuple[list[BinnedRecord], dict[str, Any], dict[str, list[str]]]:
    payload = load_payload(dump_path)
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("dump must contain a nonempty records list")

    token_bins = payload.get("token_bins")
    if token_bins is None:
        token_bins = default_token_bins(include_case_variants)
    else:
        token_bins = {
            normalize_day(day, "token_bins key"): [str(token) for token in tokens]
            for day, tokens in token_bins.items()
        }
        missing = set(WEEKDAYS) - set(token_bins)
        if missing:
            raise ValueError(f"token_bins missing weekday keys: {sorted(missing)}")

    binned: list[BinnedRecord] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"record {index} is not an object")
        start_day, offset, correct_day = correct_day_from_case(record)
        probs, other_probability = bin_weekday_probs(record, token_bins)
        binned.append(
            BinnedRecord(
                start_day=start_day,
                offset=offset,
                correct_day=correct_day,
                weekday_probs=probs,
                other_probability=other_probability,
            )
        )

    metadata = payload.get("metadata", {})
    if not isinstance(metadata, dict):
        raise ValueError("metadata must be an object when present")
    return binned, metadata, token_bins


def centroid_outputs(
    records: list[BinnedRecord],
) -> tuple[list[list[float]], list[list[float]] | None, dict[str, Any]]:
    sums = [[0.0 for _ in WEEKDAYS] for _ in WEEKDAYS]
    other_sums = [0.0 for _ in WEEKDAYS]
    other_available = True
    counts = [0 for _ in WEEKDAYS]
    case_counts: dict[str, int] = defaultdict(int)

    for record in records:
        row = DAY_TO_INDEX[record.correct_day]
        counts[row] += 1
        if record.offset is not None:
            case_counts[f"{record.start_day}+{record.offset}"] += 1
        else:
            case_counts[f"{record.start_day}->{record.correct_day}"] += 1
        for col, value in enumerate(record.weekday_probs):
            sums[row][col] += value
        if record.other_probability is None:
            other_available = False
        else:
            other_sums[row] += record.other_probability

    missing_rows = [WEEKDAYS[index] for index, count in enumerate(counts) if count == 0]
    if missing_rows:
        raise ValueError(f"no records for answer rows: {missing_rows}")

    centroids: list[list[float]] = []
    eight_bin: list[list[float]] | None = [] if other_available else None
    row_checks = []
    for row_index, count in enumerate(counts):
        raw_row = [value / count for value in sums[row_index]]
        weekday_mass = sum(raw_row)
        if weekday_mass <= 0.0:
            raise ValueError(f"row {WEEKDAYS[row_index]} has zero weekday mass")
        row = [value / weekday_mass for value in raw_row]
        centroids.append(row)

        other_mean = None
        if eight_bin is not None:
            other_mean = other_sums[row_index] / count
            total_mass = weekday_mass + other_mean
            eight_bin.append([value / total_mass for value in raw_row] + [other_mean / total_mass])

        row_checks.append(
            {
                "row": WEEKDAYS[row_index],
                "records": count,
                "raw_weekday_mass": weekday_mass,
                "other_probability": other_mean,
                "normalized_sum": sum(row),
                "min_probability": min(row),
                "max_probability": max(row),
            }
        )

    checks = {
        "record_count": len(records),
        "counts_by_answer_day": dict(zip(WEEKDAYS, counts)),
        "case_counts": dict(sorted(case_counts.items())),
        "row_checks": row_checks,
    }
    return centroids, eight_bin, checks


def centroids_from_per_class_matrix(
    matrix: list[list[float]],
    source_name: str,
) -> tuple[list[list[float]], dict[str, Any]]:
    if len(matrix) != len(WEEKDAYS):
        raise ValueError(f"{source_name} must have 7 rows, got {len(matrix)}")

    centroids: list[list[float]] = []
    row_checks = []
    for row_index, raw_row in enumerate(matrix):
        if len(raw_row) != len(WEEKDAYS):
            raise ValueError(
                f"{source_name} row {row_index} must have 7 columns; got {len(raw_row)}. "
                "If this is a full-vocabulary tensor, extract the weekday token bins first."
            )
        row = [float(value) for value in raw_row]
        if any(value < 0.0 or not math.isfinite(value) for value in row):
            raise ValueError(f"{source_name} row {row_index} has invalid probabilities")
        weekday_mass = sum(row)
        if weekday_mass <= 0.0:
            raise ValueError(f"{source_name} row {row_index} has zero weekday mass")
        normalized = [value / weekday_mass for value in row]
        centroids.append(normalized)
        row_checks.append(
            {
                "row": WEEKDAYS[row_index],
                "records": None,
                "raw_weekday_mass": weekday_mass,
                "other_probability": None,
                "normalized_sum": sum(normalized),
                "min_probability": min(normalized),
                "max_probability": max(normalized),
            }
        )

    checks = {
        "record_count": None,
        "counts_by_answer_day": {day: None for day in WEEKDAYS},
        "case_counts": {},
        "row_checks": row_checks,
    }
    return centroids, checks


def load_per_class_safetensors(path: Path) -> list[list[float]]:
    try:
        from safetensors.torch import load_file
    except ImportError as exc:
        raise RuntimeError(
            "Reading safetensors requires the `safetensors` Python package. "
            "Install it in the runtime that has access to the artifact, or "
            "export the tensor to JSON and use --dump-json."
        ) from exc

    tensors = load_file(str(path))
    if "dists" in tensors:
        tensor = tensors["dists"]
    elif len(tensors) == 1:
        tensor = next(iter(tensors.values()))
    else:
        raise ValueError(
            f"{path} contains multiple tensors and no `dists` key: {sorted(tensors)}"
        )
    return tensor.detach().cpu().float().tolist()


def manifest_records(template: str) -> list[dict[str, Any]]:
    rows = []
    for start_day in WEEKDAYS:
        for offset in range(1, 8):
            correct_day = WEEKDAYS[(DAY_TO_INDEX[start_day] + offset) % len(WEEKDAYS)]
            prompt = template.format(
                start_day=start_day,
                offset=offset,
                correct_day=correct_day,
                day_word="day" if offset == 1 else "days",
                plural_s="" if offset == 1 else "s",
            )
            rows.append(
                {
                    "start_day": start_day,
                    "offset": offset,
                    "correct_day": correct_day,
                    "prompt": prompt,
                }
            )
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def matrix_text(matrix: list[list[float]]) -> str:
    return "\n".join(
        "[" + ", ".join(f"{value:.10f}" for value in row) + "]"
        for row in matrix
    )


def make_report(
    centroids: list[list[float]] | None,
    eight_bin: list[list[float]] | None,
    checks: dict[str, Any] | None,
    metadata: dict[str, Any] | None,
    token_bins: dict[str, list[str]],
    manifest_path: Path | None,
    out_7bin: Path | None,
    out_8bin: Path | None,
) -> str:
    lines = [
        "# Weekday Centroid Build Report",
        "",
        "## Status",
        "",
    ]

    if centroids is None:
        lines += [
            "No probability dump was supplied.  The script only wrote the prompt manifest.",
            "",
        ]
    else:
        assert checks is not None
        lines += [
            f"- records consumed: {checks['record_count']}",
            f"- seven-bin centroid JSON: `{out_7bin}`",
            f"- eight-bin JSON: `{out_8bin}`" if eight_bin is not None else "- eight-bin JSON: not written; no per-record `other` mass was available",
            "",
            "Rows and columns are Monday through Sunday.  The seven-bin matrix is conditioned on total weekday-token mass.",
            "",
            "```text",
            matrix_text(centroids),
            "```",
            "",
            "## Row Checks",
            "",
            "| row | records | raw weekday mass | other probability | normalized sum | min | max |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
        for row in checks["row_checks"]:
            other = row["other_probability"]
            other_text = "-" if other is None else f"{other:.10f}"
            lines.append(
                "| "
                + " | ".join(
                    [
                        row["row"],
                        str(row["records"]),
                        f"{row['raw_weekday_mass']:.10f}",
                        other_text,
                        f"{row['normalized_sum']:.10f}",
                        f"{row['min_probability']:.10f}",
                        f"{row['max_probability']:.10f}",
                    ]
                )
                + " |"
            )
        lines.append("")

    lines += [
        "## Token Bins",
        "",
        "These are exact next-token strings expected in the dump unless the dump already provides `weekday_probs`.",
        "",
    ]
    for day in WEEKDAYS:
        lines.append(f"- {day}: " + ", ".join(f"`{token}`" for token in token_bins[day]))
    lines.append("")

    if metadata:
        lines += [
            "## Metadata",
            "",
            "```json",
            json.dumps(metadata, indent=2),
            "```",
            "",
        ]

    if manifest_path is not None:
        lines += [
            "## Prompt Manifest",
            "",
            f"Wrote `{manifest_path}`.",
            "",
        ]

    lines += [
        "## Next Command",
        "",
        "```powershell",
        "C:\\Users\\leomu\\.local\\bin\\python.exe empirical\\compute_weekdays_K_CH.py --centroids-json empirical\\data\\weekdays_llama31_8b_centroids_7bin.json --report empirical\\reports\\weekdays_llama31_8b_K_CH.md --json empirical\\reports\\weekdays_llama31_8b_K_CH.json",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dump-json", type=Path, default=None, help="Model probability/logprob dump to aggregate.")
    parser.add_argument("--per-class-safetensors", type=Path, default=None, help="Goodfire/causalab 7x7 per-class output distribution artifact.")
    parser.add_argument("--write-manifest", type=Path, default=None, help="Write the 49-case prompt manifest.")
    parser.add_argument("--prompt-template", default=DEFAULT_TEMPLATE)
    parser.add_argument("--include-case-variants", action="store_true")
    parser.add_argument("--out-7bin", type=Path, default=Path("empirical/data/weekdays_llama31_8b_centroids_7bin.json"))
    parser.add_argument("--out-8bin", type=Path, default=Path("empirical/data/weekdays_llama31_8b_centroids_8bin_with_other.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/reports/weekdays_centroid_build.md"))
    args = parser.parse_args()

    token_bins = default_token_bins(args.include_case_variants)
    metadata: dict[str, Any] | None = None
    centroids: list[list[float]] | None = None
    eight_bin: list[list[float]] | None = None
    checks: dict[str, Any] | None = None

    if args.write_manifest is not None:
        write_json(
            args.write_manifest,
            {
                "weekdays": list(WEEKDAYS),
                "prompt_template": args.prompt_template,
                "records": manifest_records(args.prompt_template),
            },
        )

    if args.dump_json is not None and args.per_class_safetensors is not None:
        raise ValueError("Use either --dump-json or --per-class-safetensors, not both")

    if args.dump_json is not None:
        records, metadata, token_bins = load_records(args.dump_json, args.include_case_variants)
        centroids, eight_bin, checks = centroid_outputs(records)
        write_json(
            args.out_7bin,
            {
                "weekdays": list(WEEKDAYS),
                "centroids": centroids,
                "source_dump": str(args.dump_json),
                "normalization": "conditioned_on_seven_weekday_bins",
                "checks": checks,
                "metadata": metadata,
                "token_bins": token_bins,
            },
        )
        if eight_bin is not None:
            write_json(
                args.out_8bin,
                {
                    "columns": list(WEEKDAYS) + ["other"],
                    "centroids": eight_bin,
                    "source_dump": str(args.dump_json),
                    "normalization": "weekday_bins_plus_record_other_probability",
                    "checks": checks,
                    "metadata": metadata,
                    "token_bins": token_bins,
                },
            )

    if args.per_class_safetensors is not None:
        matrix = load_per_class_safetensors(args.per_class_safetensors)
        centroids, checks = centroids_from_per_class_matrix(
            matrix,
            str(args.per_class_safetensors),
        )
        metadata = {
            "source": "per_class_safetensors",
            "source_path": str(args.per_class_safetensors),
            "note": (
                "Rows were row-normalized over the seven weekday columns. "
                "This is appropriate for causalab's per_class_output_dists "
                "when saved with full-vocabulary softmax restricted to score tokens."
            ),
        }
        write_json(
            args.out_7bin,
            {
                "weekdays": list(WEEKDAYS),
                "centroids": centroids,
                "source_dump": str(args.per_class_safetensors),
                "normalization": "row_normalized_from_per_class_weekday_tensor",
                "checks": checks,
                "metadata": metadata,
                "token_bins": token_bins,
            },
        )

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        make_report(
            centroids,
            eight_bin,
            checks,
            metadata,
            token_bins,
            args.write_manifest,
            args.out_7bin if centroids is not None else None,
            args.out_8bin if eight_bin is not None else None,
        ),
        encoding="utf-8",
    )

    if args.write_manifest is not None:
        print(f"Wrote {args.write_manifest}")
    if centroids is not None:
        print(f"Wrote {args.out_7bin}")
        if eight_bin is not None:
            print(f"Wrote {args.out_8bin}")
    print(f"Wrote {args.report}")


if __name__ == "__main__":
    main()
