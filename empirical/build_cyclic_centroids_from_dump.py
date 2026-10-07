"""Build cyclic label centroids from a model probability dump.

This is the generic handoff for C_n behavior probes.  It writes a prompt
manifest and converts raw next-token probabilities/logprobs, or a Causalab
``per_class_output_dists.safetensors`` tensor, into the centroid JSON consumed
by ``compute_cyclic_K_CH.py``.

Built-in presets:

* weekdays: C7, compatible with the older weekday-specific scripts.
* months: C12, the mixed-conductor control between prime C7 and local rows.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from compute_cyclic_K_CH import PRESETS


@dataclass(frozen=True)
class LabelSpec:
    name: str
    labels: tuple[str, ...]
    noun: str
    unit: str
    default_template: str


SPECS: dict[str, LabelSpec] = {
    "weekdays": LabelSpec(
        name="weekdays",
        labels=PRESETS["weekdays"],
        noun="weekday",
        unit="day",
        default_template=(
            "What day of the week is {offset} {unit_word} after {start_label}? "
            "Answer with one weekday name:"
        ),
    ),
    "months": LabelSpec(
        name="months",
        labels=PRESETS["months"],
        noun="month",
        unit="month",
        default_template=(
            "What month is {offset} {unit_word} after {start_label}? "
            "Answer with one month name:"
        ),
    ),
}


@dataclass(frozen=True)
class BinnedRecord:
    start_label: str
    offset: int | None
    correct_label: str
    label_probs: list[float]
    other_probability: float | None


def load_spec(preset: str, labels_json: Path | None) -> LabelSpec:
    if labels_json is None:
        return SPECS[preset]
    payload = json.loads(labels_json.read_text(encoding="utf-8"))
    labels = payload.get("labels") if isinstance(payload, dict) else payload
    if not isinstance(labels, list) or len(labels) < 4:
        raise ValueError("labels JSON must contain at least four labels")
    noun = str(payload.get("noun", "label")) if isinstance(payload, dict) else "label"
    unit = str(payload.get("unit", noun)) if isinstance(payload, dict) else noun
    template = (
        str(payload.get("prompt_template"))
        if isinstance(payload, dict) and payload.get("prompt_template")
        else "What label is {offset} {unit_word} after {start_label}? Answer with one label:"
    )
    return LabelSpec("custom", tuple(str(label) for label in labels), noun, unit, template)


def label_to_index(labels: tuple[str, ...]) -> dict[str, int]:
    return {label: index for index, label in enumerate(labels)}


def normalize_label(value: Any, field_name: str, labels: tuple[str, ...]) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a label string")
    folded = value.strip().casefold()
    for label in labels:
        if label.casefold() == folded:
            return label
    raise ValueError(f"{field_name} is not recognized: {value!r}")


def first_present(record: dict[str, Any], keys: tuple[str, ...]) -> Any:
    for key in keys:
        if key in record:
            return record[key]
    return None


def correct_label_from_case(record: dict[str, Any], spec: LabelSpec) -> tuple[str, int | None, str]:
    labels = spec.labels
    index = label_to_index(labels)
    start_raw = first_present(record, ("start_label", "start_day", "start_month", "source_label"))
    start_label = normalize_label(start_raw, "start_label", labels)
    offset_value = record.get("offset")
    correct_raw = first_present(
        record,
        (
            "correct_label",
            "answer_label",
            "target_label",
            "correct_day",
            "answer_day",
            "target_day",
            "correct_month",
            "answer_month",
            "target_month",
            "result",
        ),
    )

    if offset_value is None:
        return start_label, None, normalize_label(correct_raw, "correct_label", labels)

    offset = int(offset_value)
    if offset < 1 or offset > len(labels):
        raise ValueError(f"offset must be in 1..{len(labels)}, got {offset}")
    correct_label = labels[(index[start_label] + offset) % len(labels)]
    if correct_raw is not None:
        explicit = normalize_label(correct_raw, "correct_label", labels)
        if explicit != correct_label:
            raise ValueError(
                f"record says correct_label={explicit}, but {offset} after "
                f"{start_label} is {correct_label}"
            )
    return start_label, offset, correct_label


def default_token_bins(labels: tuple[str, ...], include_case_variants: bool) -> dict[str, list[str]]:
    bins: dict[str, list[str]] = {}
    for label in labels:
        variants = [label, " " + label]
        if include_case_variants:
            variants.extend([label.lower(), " " + label.lower(), label.upper(), " " + label.upper()])
        bins[label] = variants
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
            raise ValueError(f"{field_name}[{key!r}] is not finite and nonnegative")
        out[str(key)] = value
    return out


def map_by_label(values: dict[str, float], labels: tuple[str, ...]) -> list[float]:
    out = []
    for label in labels:
        out.append(values.get(label, values.get(label.lower(), 0.0)))
    return out


def bin_label_probs(
    record: dict[str, Any],
    spec: LabelSpec,
    token_bins: dict[str, list[str]],
) -> tuple[list[float], float | None]:
    noun = spec.noun
    labels = spec.labels
    direct_prob_keys = ("label_probs", f"{noun}_probs", "weekday_probs", "month_probs")
    direct_logprob_keys = ("label_logprobs", f"{noun}_logprobs", "weekday_logprobs", "month_logprobs")
    token_prob_keys = ("token_probs",)
    token_logprob_keys = ("token_logprobs",)

    key = next((candidate for candidate in direct_prob_keys if candidate in record), None)
    if key is not None:
        probs = map_by_label(as_probability_map(record[key], key, False), labels)
    else:
        key = next((candidate for candidate in direct_logprob_keys if candidate in record), None)
        if key is not None:
            probs = map_by_label(as_probability_map(record[key], key, True), labels)
        elif any(candidate in record for candidate in token_prob_keys):
            key = next(candidate for candidate in token_prob_keys if candidate in record)
            values = as_probability_map(record[key], key, False)
            probs = [sum(values.get(token, 0.0) for token in token_bins[label]) for label in labels]
        elif any(candidate in record for candidate in token_logprob_keys):
            key = next(candidate for candidate in token_logprob_keys if candidate in record)
            values = as_probability_map(record[key], key, True)
            probs = [sum(values.get(token, 0.0) for token in token_bins[label]) for label in labels]
        else:
            raise ValueError(
                "each record needs label/month/weekday probs, label/month/weekday "
                "logprobs, token_probs, or token_logprobs"
            )

    label_mass = sum(probs)
    if label_mass <= 0.0:
        raise ValueError("label bin mass is zero for a record")

    other_raw = record.get("other_probability", record.get("other_prob"))
    if other_raw is not None:
        other_probability = float(other_raw)
    else:
        total_probability = record.get("total_probability", record.get("total_prob"))
        other_probability = None if total_probability is None else max(0.0, float(total_probability) - label_mass)
    return probs, other_probability


def load_records(
    dump_path: Path,
    spec: LabelSpec,
    include_case_variants: bool,
) -> tuple[list[BinnedRecord], dict[str, Any], dict[str, list[str]]]:
    payload = load_payload(dump_path)
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("dump must contain a nonempty records list")

    token_bins_payload = payload.get("token_bins")
    if token_bins_payload is None:
        token_bins = default_token_bins(spec.labels, include_case_variants)
    else:
        token_bins = {
            normalize_label(label, "token_bins key", spec.labels): [str(token) for token in tokens]
            for label, tokens in token_bins_payload.items()
        }
        missing = set(spec.labels) - set(token_bins)
        if missing:
            raise ValueError(f"token_bins missing labels: {sorted(missing)}")

    binned = []
    for record_index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"record {record_index} is not an object")
        start_label, offset, correct_label = correct_label_from_case(record, spec)
        probs, other_probability = bin_label_probs(record, spec, token_bins)
        binned.append(BinnedRecord(start_label, offset, correct_label, probs, other_probability))

    metadata = payload.get("metadata", {})
    if not isinstance(metadata, dict):
        raise ValueError("metadata must be an object when present")
    return binned, metadata, token_bins


def centroid_outputs(records: list[BinnedRecord], spec: LabelSpec) -> tuple[list[list[float]], list[list[float]] | None, dict[str, Any]]:
    labels = spec.labels
    index = label_to_index(labels)
    sums = [[0.0 for _ in labels] for _ in labels]
    other_sums = [0.0 for _ in labels]
    other_available = True
    counts = [0 for _ in labels]
    case_counts: dict[str, int] = defaultdict(int)

    for record in records:
        row = index[record.correct_label]
        counts[row] += 1
        case_key = (
            f"{record.start_label}+{record.offset}"
            if record.offset is not None
            else f"{record.start_label}->{record.correct_label}"
        )
        case_counts[case_key] += 1
        for col, value in enumerate(record.label_probs):
            sums[row][col] += value
        if record.other_probability is None:
            other_available = False
        else:
            other_sums[row] += record.other_probability

    missing_rows = [labels[i] for i, count in enumerate(counts) if count == 0]
    if missing_rows:
        raise ValueError(f"no records for answer rows: {missing_rows}")

    centroids = []
    with_other: list[list[float]] | None = [] if other_available else None
    row_checks = []
    for row_index, count in enumerate(counts):
        raw_row = [value / count for value in sums[row_index]]
        label_mass = sum(raw_row)
        if label_mass <= 0.0:
            raise ValueError(f"row {labels[row_index]} has zero label mass")
        row = [value / label_mass for value in raw_row]
        centroids.append(row)
        other_mean = None
        if with_other is not None:
            other_mean = other_sums[row_index] / count
            total_mass = label_mass + other_mean
            with_other.append([value / total_mass for value in raw_row] + [other_mean / total_mass])
        row_checks.append(
            {
                "row": labels[row_index],
                "records": count,
                "raw_label_mass": label_mass,
                "other_probability": other_mean,
                "normalized_sum": sum(row),
                "min_probability": min(row),
                "max_probability": max(row),
            }
        )

    checks = {
        "record_count": len(records),
        "counts_by_answer_label": dict(zip(labels, counts)),
        "case_counts": dict(sorted(case_counts.items())),
        "row_checks": row_checks,
    }
    return centroids, with_other, checks


def centroids_from_per_class_matrix(matrix: list[list[float]], spec: LabelSpec, source_name: str) -> tuple[list[list[float]], dict[str, Any]]:
    labels = spec.labels
    if len(matrix) != len(labels):
        raise ValueError(f"{source_name} must have {len(labels)} rows, got {len(matrix)}")
    centroids = []
    row_checks = []
    for row_index, raw_row in enumerate(matrix):
        if len(raw_row) != len(labels):
            raise ValueError(f"{source_name} row {row_index} must have {len(labels)} columns")
        row = [float(value) for value in raw_row]
        if any(value < 0.0 or not math.isfinite(value) for value in row):
            raise ValueError(f"{source_name} row {row_index} has invalid probabilities")
        label_mass = sum(row)
        if label_mass <= 0.0:
            raise ValueError(f"{source_name} row {row_index} has zero label mass")
        normalized = [value / label_mass for value in row]
        centroids.append(normalized)
        row_checks.append(
            {
                "row": labels[row_index],
                "records": None,
                "raw_label_mass": label_mass,
                "other_probability": None,
                "normalized_sum": sum(normalized),
                "min_probability": min(normalized),
                "max_probability": max(normalized),
            }
        )
    checks = {
        "record_count": None,
        "counts_by_answer_label": {label: None for label in labels},
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
            "Export the tensor to JSON if that package is unavailable."
        ) from exc

    tensors = load_file(str(path))
    if "dists" in tensors:
        tensor = tensors["dists"]
    elif len(tensors) == 1:
        tensor = next(iter(tensors.values()))
    else:
        raise ValueError(f"{path} contains multiple tensors and no `dists` key: {sorted(tensors)}")
    return tensor.detach().cpu().float().tolist()


def manifest_records(spec: LabelSpec, template: str) -> list[dict[str, Any]]:
    labels = spec.labels
    rows = []
    for start_label in labels:
        for offset in range(1, len(labels) + 1):
            correct_label = labels[(label_to_index(labels)[start_label] + offset) % len(labels)]
            unit_word = spec.unit if offset == 1 else spec.unit + "s"
            prompt = template.format(
                start_label=start_label,
                offset=offset,
                correct_label=correct_label,
                unit_word=unit_word,
                noun=spec.noun,
            )
            rows.append(
                {
                    "start_label": start_label,
                    "offset": offset,
                    "correct_label": correct_label,
                    "prompt": prompt,
                }
            )
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def matrix_text(matrix: list[list[float]]) -> str:
    return "\n".join("[" + ", ".join(f"{value:.10f}" for value in row) + "]" for row in matrix)


def make_report(
    spec: LabelSpec,
    centroids: list[list[float]] | None,
    with_other: list[list[float]] | None,
    checks: dict[str, Any] | None,
    metadata: dict[str, Any] | None,
    token_bins: dict[str, list[str]],
    manifest_path: Path | None,
    out_nbin: Path | None,
    out_with_other: Path | None,
) -> str:
    labels = spec.labels
    n = len(labels)
    lines = [
        f"# {spec.noun.title()} C{n} Centroid Build Report",
        "",
        "## Status",
        "",
    ]
    if centroids is None:
        lines += ["No probability dump was supplied.  The script only wrote the prompt manifest.", ""]
    else:
        assert checks is not None
        lines += [
            f"- records consumed: {checks['record_count']}",
            f"- {n}-bin centroid JSON: `{out_nbin}`",
            f"- with-other JSON: `{out_with_other}`" if with_other is not None else "- with-other JSON: not written; no per-record `other` mass was available",
            "",
            f"Rows and columns are {', '.join(labels)}.  The {n}-bin matrix is conditioned on total label-token mass.",
            "",
            "```text",
            matrix_text(centroids),
            "```",
            "",
            "## Row Checks",
            "",
            "| row | records | raw label mass | other probability | normalized sum | min | max |",
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
                        f"{row['raw_label_mass']:.10f}",
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
        "These are exact next-token strings expected in the dump unless the dump already provides label probabilities.",
        "",
    ]
    for label in labels:
        lines.append(f"- {label}: " + ", ".join(f"`{token}`" for token in token_bins[label]))
    lines.append("")

    if metadata:
        lines += ["## Metadata", "", "```json", json.dumps(metadata, indent=2), "```", ""]

    if manifest_path is not None:
        lines += ["## Prompt Manifest", "", f"Wrote `{manifest_path}`.", ""]

    lines += [
        "## Next Command",
        "",
        "```powershell",
        f"C:\\Users\\leomu\\.local\\bin\\python.exe empirical\\compute_cyclic_K_CH.py --preset {spec.name if spec.name in SPECS else 'months'} --centroids-json {out_nbin or '<centroids.json>'}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_out_paths(spec: LabelSpec) -> tuple[Path, Path, Path]:
    n = len(spec.labels)
    stem = spec.name if spec.name != "custom" else f"cyclic_{n}"
    return (
        Path(f"empirical/data/{stem}_probe_manifest.json"),
        Path(f"empirical/data/{stem}_llama31_8b_centroids_{n}bin.json"),
        Path(f"empirical/data/{stem}_llama31_8b_centroids_{n + 1}bin_with_other.json"),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=sorted(SPECS), default="months")
    parser.add_argument("--labels-json", type=Path, default=None)
    parser.add_argument("--dump-json", type=Path, default=None)
    parser.add_argument("--per-class-safetensors", type=Path, default=None)
    parser.add_argument("--write-manifest", type=Path, default=None)
    parser.add_argument("--prompt-template", default=None)
    parser.add_argument("--include-case-variants", action="store_true")
    parser.add_argument("--out-nbin", type=Path, default=None)
    parser.add_argument("--out-with-other", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    spec = load_spec(args.preset, args.labels_json)
    default_manifest, default_nbin, default_with_other = default_out_paths(spec)
    manifest_path = args.write_manifest
    out_nbin = args.out_nbin or default_nbin
    out_with_other = args.out_with_other or default_with_other
    report_path = args.report or Path(f"empirical/reports/{spec.name if spec.name != 'custom' else 'cyclic'}_centroid_build.md")
    token_bins = default_token_bins(spec.labels, args.include_case_variants)
    metadata: dict[str, Any] | None = None
    centroids: list[list[float]] | None = None
    with_other: list[list[float]] | None = None
    checks: dict[str, Any] | None = None

    if args.dump_json is not None and args.per_class_safetensors is not None:
        raise ValueError("Use either --dump-json or --per-class-safetensors, not both")

    template = args.prompt_template or spec.default_template
    if manifest_path is not None:
        write_json(
            manifest_path,
            {
                "labels": list(spec.labels),
                "noun": spec.noun,
                "unit": spec.unit,
                "prompt_template": template,
                "records": manifest_records(spec, template),
            },
        )
    elif args.dump_json is None and args.per_class_safetensors is None:
        manifest_path = default_manifest
        write_json(
            manifest_path,
            {
                "labels": list(spec.labels),
                "noun": spec.noun,
                "unit": spec.unit,
                "prompt_template": template,
                "records": manifest_records(spec, template),
            },
        )

    if args.dump_json is not None:
        records, metadata, token_bins = load_records(args.dump_json, spec, args.include_case_variants)
        centroids, with_other, checks = centroid_outputs(records, spec)
        write_json(
            out_nbin,
            {
                "labels": list(spec.labels),
                "centroids": centroids,
                "source_dump": str(args.dump_json),
                "normalization": f"conditioned_on_{len(spec.labels)}_{spec.noun}_bins",
                "checks": checks,
                "metadata": metadata,
                "token_bins": token_bins,
            },
        )
        if with_other is not None:
            write_json(
                out_with_other,
                {
                    "columns": list(spec.labels) + ["other"],
                    "centroids": with_other,
                    "source_dump": str(args.dump_json),
                    "normalization": "label_bins_plus_record_other_probability",
                    "checks": checks,
                    "metadata": metadata,
                    "token_bins": token_bins,
                },
            )

    if args.per_class_safetensors is not None:
        matrix = load_per_class_safetensors(args.per_class_safetensors)
        centroids, checks = centroids_from_per_class_matrix(matrix, spec, str(args.per_class_safetensors))
        metadata = {
            "source": "per_class_safetensors",
            "source_path": str(args.per_class_safetensors),
            "note": "Rows were row-normalized over the cyclic label columns.",
        }
        write_json(
            out_nbin,
            {
                "labels": list(spec.labels),
                "centroids": centroids,
                "source_dump": str(args.per_class_safetensors),
                "normalization": "row_normalized_from_per_class_label_tensor",
                "checks": checks,
                "metadata": metadata,
                "token_bins": token_bins,
            },
        )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        make_report(
            spec,
            centroids,
            with_other,
            checks,
            metadata,
            token_bins,
            manifest_path,
            out_nbin if centroids is not None else None,
            out_with_other if with_other is not None else None,
        ),
        encoding="utf-8",
    )

    if manifest_path is not None:
        print(f"Wrote {manifest_path}")
    if centroids is not None:
        print(f"Wrote {out_nbin}")
        if with_other is not None:
            print(f"Wrote {out_with_other}")
    print(f"Wrote {report_path}")


if __name__ == "__main__":
    main()
