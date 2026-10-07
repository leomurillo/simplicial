"""Orchestrate the empirical C7 weekday row.

The script routes one real data source through the weekday centroid builder
and K^CH scorer:

* a supplied 7x7 centroid JSON,
* a supplied probability/logprob dump,
* a supplied Goodfire/Causalab ``per_class_output_dists.safetensors``, or
* a local Hugging Face causal LM that can expose next-token logits.

When no real source is available, it writes a blocker report and exits without
creating empirical centroid or K^CH artifacts.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "empirical/data/weekdays_probe_manifest.json"
DEFAULT_DUMP = ROOT / "empirical/data/weekdays_llama31_8b_probability_dump.json"
DEFAULT_CENTROIDS = ROOT / "empirical/data/weekdays_llama31_8b_centroids_7bin.json"
DEFAULT_EIGHT_BIN = ROOT / "empirical/data/weekdays_llama31_8b_centroids_8bin_with_other.json"
DEFAULT_BUILD_REPORT = ROOT / "empirical/reports/weekdays_centroid_build.md"
DEFAULT_KCH_REPORT = ROOT / "empirical/reports/weekdays_llama31_8b_K_CH.md"
DEFAULT_KCH_JSON = ROOT / "empirical/reports/weekdays_llama31_8b_K_CH.json"
DEFAULT_REPORT = ROOT / "empirical/reports/weekdays_c7_orchestration.md"
GOODFIRE_RELATIVE_ARTIFACT = Path(
    "artifacts/natural_domains_arithmetic/llama31_8b/weekdays/baseline/per_class_output_dists.safetensors"
)


@dataclass
class RunStep:
    name: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str


def rel(path: Path | None) -> str:
    if path is None:
        return "-"
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def run_step(name: str, command: list[str]) -> RunStep:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return RunStep(name, command, completed.returncode, completed.stdout, completed.stderr)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def find_default_goodfire_artifact() -> Path | None:
    candidates = [
        ROOT / GOODFIRE_RELATIVE_ARTIFACT,
        ROOT.parent / "causalab" / GOODFIRE_RELATIVE_ARTIFACT,
        Path.home() / "causalab" / GOODFIRE_RELATIVE_ARTIFACT,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def copy_centroids_for_standard_path(source: Path, target: Path) -> None:
    if source.resolve() == target.resolve():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def summarize_kch(json_path: Path) -> dict[str, Any] | None:
    if not json_path.exists():
        return None
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    correlations = payload.get("correlations", {})
    gap = payload.get("gap_accounting", {})
    adjacent = payload.get("adjacent") or {}
    nonadjacent = payload.get("nonadjacent") or {}
    return {
        "centroid_source": payload.get("centroid_source"),
        "centroids_path": payload.get("empirical_centroids_path"),
        "correlations": correlations,
        "gap_accounting": gap,
        "adjacent_K_norm": adjacent.get("fisher_norm_K_h_h"),
        "nonadjacent_K_norm": nonadjacent.get("fisher_norm_K_h_h"),
    }


def command_text(command: list[str]) -> str:
    return " ".join(f'"{part}"' if " " in part else part for part in command)


def make_report(
    status: str,
    source: str,
    steps: list[RunStep],
    blockers: list[str],
    kch_summary: dict[str, Any] | None,
    args: argparse.Namespace,
) -> str:
    lines = [
        "# Weekdays C7 Orchestration",
        "",
        "## Status",
        "",
        f"- outcome: `{status}`",
        f"- source: `{source}`",
        f"- timestamp: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
    ]

    if blockers:
        lines += ["## Blockers", ""]
        lines.extend(f"- {item}" for item in blockers)
        lines.append("")

    lines += [
        "## Artifact Targets",
        "",
        f"- manifest: `{rel(args.manifest)}`",
        f"- probability dump: `{rel(args.dump_json or DEFAULT_DUMP)}`",
        f"- seven-bin centroids: `{rel(args.out_centroids)}`",
        f"- eight-bin centroids: `{rel(DEFAULT_EIGHT_BIN)}`",
        f"- K_CH report: `{rel(args.kch_report)}`",
        f"- K_CH JSON: `{rel(args.kch_json)}`",
        "",
    ]

    if kch_summary is not None:
        corr = kch_summary.get("correlations", {})
        gap = kch_summary.get("gap_accounting", {})
        lines += [
            "## Measured Gap Summary",
            "",
            f"- moment chord vs cyclic arc: `{corr.get('moment_chord_vs_cyclic_arc')}`",
            f"- Hellinger chord vs cyclic arc: `{corr.get('hellinger_chord_vs_cyclic_arc')}`",
            f"- natural/logit chord vs cyclic arc: `{corr.get('natural_chord_vs_cyclic_arc')}`",
            f"- behavior linear residual vs Wurgaft text baseline: `{gap.get('residual_vs_wurgaft_text_linear_r')}`",
            f"- explained fraction of Wurgaft text gap: `{gap.get('explained_fraction_of_text_gap')}`",
            f"- adjacent ||K_CH(h)h||_F: `{kch_summary.get('adjacent_K_norm')}`",
            f"- nonadjacent ||K_CH(h)h||_F: `{kch_summary.get('nonadjacent_K_norm')}`",
            "",
        ]

    if steps:
        lines += ["## Commands", ""]
        for step in steps:
            lines += [
                f"### {step.name}",
                "",
                "```powershell",
                command_text(step.command),
                "```",
                "",
                f"return code: `{step.returncode}`",
                "",
            ]
            if step.stdout.strip():
                lines += ["stdout:", "", "```text", step.stdout.strip(), "```", ""]
            if step.stderr.strip():
                lines += ["stderr:", "", "```text", step.stderr.strip(), "```", ""]

    lines += [
        "## Boundary",
        "",
        "This orchestration treats a run as empirical only when a real dump, real centroids, a real safetensors artifact, or a successfully scored local model is supplied. Otherwise it stops at this report and does not overwrite empirical K_CH outputs.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", choices=("auto", "centroids-json", "dump-json", "per-class-safetensors", "hf"), default="auto")
    parser.add_argument("--centroids-json", type=Path, default=None)
    parser.add_argument("--dump-json", type=Path, default=None)
    parser.add_argument("--per-class-safetensors", type=Path, default=None)
    parser.add_argument("--hf-model", default=None)
    parser.add_argument("--hf-revision", default=None)
    parser.add_argument("--hf-device", default="cpu")
    parser.add_argument("--hf-device-map", default=None)
    parser.add_argument("--hf-dtype", default="auto")
    parser.add_argument("--hf-load-in-4bit", action="store_true")
    parser.add_argument("--hf-local-files-only", action="store_true")
    parser.add_argument("--hf-chat-template", action="store_true")
    parser.add_argument("--include-case-variants", action="store_true")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--out-centroids", type=Path, default=DEFAULT_CENTROIDS)
    parser.add_argument("--build-report", type=Path, default=DEFAULT_BUILD_REPORT)
    parser.add_argument("--kch-report", type=Path, default=DEFAULT_KCH_REPORT)
    parser.add_argument("--kch-json", type=Path, default=DEFAULT_KCH_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    steps: list[RunStep] = []
    blockers: list[str] = []
    source = args.source
    centroids_for_kch: Path | None = None

    if source == "auto":
        if args.centroids_json and args.centroids_json.exists():
            source = "centroids-json"
        elif DEFAULT_CENTROIDS.exists():
            args.centroids_json = DEFAULT_CENTROIDS
            source = "centroids-json"
        elif args.dump_json and args.dump_json.exists():
            source = "dump-json"
        elif DEFAULT_DUMP.exists():
            args.dump_json = DEFAULT_DUMP
            source = "dump-json"
        elif args.per_class_safetensors and args.per_class_safetensors.exists():
            source = "per-class-safetensors"
        else:
            goodfire_artifact = find_default_goodfire_artifact()
            if goodfire_artifact is not None:
                args.per_class_safetensors = goodfire_artifact
                source = "per-class-safetensors"
            elif args.hf_model:
                source = "hf"
            else:
                source = "blocked"

    if source == "centroids-json":
        if args.centroids_json is None or not args.centroids_json.exists():
            blockers.append("Requested centroids-json source, but the centroid JSON does not exist.")
        else:
            copy_centroids_for_standard_path(args.centroids_json, args.out_centroids)
            centroids_for_kch = args.out_centroids

    elif source == "dump-json":
        dump_path = args.dump_json
        if dump_path is None or not dump_path.exists():
            blockers.append("Requested dump-json source, but the probability dump does not exist.")
        else:
            steps.append(
                run_step(
                    "build centroids from dump",
                    [
                        sys.executable,
                        "empirical/build_weekday_centroids_from_dump.py",
                        "--dump-json",
                        str(dump_path),
                        "--out-7bin",
                        str(args.out_centroids),
                        "--out-8bin",
                        str(DEFAULT_EIGHT_BIN),
                        "--report",
                        str(args.build_report),
                    ],
                )
            )
            if steps[-1].returncode == 0 and args.out_centroids.exists():
                centroids_for_kch = args.out_centroids
            else:
                blockers.append("Centroid build from dump failed; see command stderr in this report.")

    elif source == "per-class-safetensors":
        tensor_path = args.per_class_safetensors
        if tensor_path is None or not tensor_path.exists():
            blockers.append("Requested per-class-safetensors source, but the tensor file does not exist.")
        else:
            steps.append(
                run_step(
                    "build centroids from safetensors",
                    [
                        sys.executable,
                        "empirical/build_weekday_centroids_from_dump.py",
                        "--per-class-safetensors",
                        str(tensor_path),
                        "--out-7bin",
                        str(args.out_centroids),
                        "--report",
                        str(args.build_report),
                    ],
                )
            )
            if steps[-1].returncode == 0 and args.out_centroids.exists():
                centroids_for_kch = args.out_centroids
            else:
                blockers.append("Centroid build from safetensors failed; see command stderr in this report.")

    elif source == "hf":
        if not args.hf_model:
            blockers.append("Requested hf source, but --hf-model was not supplied.")
        else:
            dump_path = args.dump_json or DEFAULT_DUMP
            command = [
                sys.executable,
                "empirical/collect_weekday_prob_dump_hf.py",
                "--model",
                args.hf_model,
                "--manifest",
                str(args.manifest),
                "--out",
                str(dump_path),
                "--device",
                args.hf_device,
                "--dtype",
                args.hf_dtype,
                "--progress",
            ]
            if args.hf_revision:
                command.extend(["--revision", args.hf_revision])
            if args.hf_device_map:
                command.extend(["--device-map", args.hf_device_map])
            if args.hf_load_in_4bit:
                command.append("--load-in-4bit")
            if args.hf_local_files_only:
                command.append("--local-files-only")
            if args.hf_chat_template:
                command.append("--chat-template")
            if args.include_case_variants:
                command.append("--include-case-variants")
            steps.append(run_step("collect HF probability dump", command))
            if steps[-1].returncode == 0 and dump_path.exists():
                args.dump_json = dump_path
                steps.append(
                    run_step(
                        "build centroids from HF dump",
                        [
                            sys.executable,
                            "empirical/build_weekday_centroids_from_dump.py",
                            "--dump-json",
                            str(dump_path),
                            "--out-7bin",
                            str(args.out_centroids),
                            "--out-8bin",
                            str(DEFAULT_EIGHT_BIN),
                            "--report",
                            str(args.build_report),
                        ],
                    )
                )
                if steps[-1].returncode == 0 and args.out_centroids.exists():
                    centroids_for_kch = args.out_centroids
                else:
                    blockers.append("Centroid build from HF dump failed; see command stderr in this report.")
            else:
                blockers.append("HF probability collection failed; see command stderr in this report.")

    else:
        blockers.extend(
            [
                "No real C7 data source was found in the workspace.",
                f"Expected Goodfire artifact, if present: {GOODFIRE_RELATIVE_ARTIFACT.as_posix()}",
                "Provide --centroids-json, --dump-json, --per-class-safetensors, or --hf-model with a runnable local Hugging Face model.",
            ]
        )

    if centroids_for_kch is not None and not blockers:
        steps.append(
            run_step(
                "compute K_CH gap report",
                [
                    sys.executable,
                    "empirical/compute_weekdays_K_CH.py",
                    "--centroids-json",
                    str(centroids_for_kch),
                    "--report",
                    str(args.kch_report),
                    "--json",
                    str(args.kch_json),
                ],
            )
        )
        if steps[-1].returncode != 0:
            blockers.append("K_CH computation failed; see command stderr in this report.")

    kch_summary = summarize_kch(args.kch_json) if args.kch_json.exists() and not blockers else None
    status = "measured" if kch_summary is not None and not blockers else "blocked"
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        make_report(status, source, steps, blockers, kch_summary, args),
        encoding="utf-8",
    )
    print(f"Wrote {args.report}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
