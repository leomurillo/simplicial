#!/usr/bin/env python3
"""Benchmark SCANS v0 against gzip on local files."""

from __future__ import annotations

import argparse
import gzip
import json
import statistics
import sys
import time
from pathlib import Path

import scans_codec


DEFAULT_FILES = [
    "T7-ComplexAmplitudesQuantumSector-Draft1.md",
    "T15-FiniteToArchimedeanCompletion-Draft1.md",
    "T0-GaugeSelectionFourierMellinSimplex-Draft1.md",
    "T12-FiniteApexDeterminacy-Draft1.md",
    "T13-ExactSimplicialRenormalization-Draft1.md",
    "T14-ProjectedFlatnessCurvatureLinearization-Draft1.md",
    "empirical/three_gap_compression_safety_audit.py",
    "empirical/_tiny_canned_corpus.txt",
]


def _time_call(fn, min_seconds: float = 0.20, min_rounds: int = 5) -> tuple[float, int]:
    times: list[float] = []
    total = 0.0
    rounds = 0
    while rounds < min_rounds or total < min_seconds:
        start = time.perf_counter()
        fn()
        elapsed = time.perf_counter() - start
        times.append(elapsed)
        total += elapsed
        rounds += 1
        if rounds >= 200:
            break
    return statistics.median(times), rounds


def _gzip_compress(data: bytes) -> bytes:
    return gzip.compress(data, compresslevel=9, mtime=0)


def benchmark_file(path: Path) -> dict[str, object]:
    data = path.read_bytes()

    start = time.perf_counter()
    gzip_blob = _gzip_compress(data)
    gzip_compress_s = time.perf_counter() - start

    start = time.perf_counter()
    scans_blob, scans_meta = scans_codec.pack(data)
    scans_compress_s = time.perf_counter() - start

    zstd_blob = None
    zstd_meta = None
    zstd_compress_s = None
    try:
        start = time.perf_counter()
        zstd_blob, zstd_meta = scans_codec.pack(data, level=19, backend="zstd")
        zstd_compress_s = time.perf_counter() - start
    except scans_codec.ScansError:
        pass

    if gzip.decompress(gzip_blob) != data:
        raise RuntimeError(f"gzip round trip failed: {path}")
    if scans_codec.unpack(scans_blob) != data:
        raise RuntimeError(f"SCANS round trip failed: {path}")
    if zstd_blob is not None and scans_codec.unpack(zstd_blob) != data:
        raise RuntimeError(f"SCANS-zstd round trip failed: {path}")

    gzip_decomp_s, gzip_rounds = _time_call(lambda: gzip.decompress(gzip_blob))
    scans_decomp_s, scans_rounds = _time_call(lambda: scans_codec.unpack(scans_blob))
    zstd_decomp_s = None
    zstd_rounds = 0
    if zstd_blob is not None:
        zstd_decomp_s, zstd_rounds = _time_call(lambda: scans_codec.unpack(zstd_blob))

    size = len(data)
    gzip_size = len(gzip_blob)
    scans_size = len(scans_blob)
    row = {
        "file": str(path),
        "input_bytes": size,
        "gzip_bytes": gzip_size,
        "scans_bytes": scans_size,
        "scans_minus_gzip_bytes": scans_size - gzip_size,
        "scans_vs_gzip_percent": ((scans_size / gzip_size) - 1.0) * 100.0
        if gzip_size
        else 0.0,
        "gzip_compress_s": gzip_compress_s,
        "scans_compress_s": scans_compress_s,
        "gzip_decompress_median_s": gzip_decomp_s,
        "scans_decompress_median_s": scans_decomp_s,
        "gzip_decompress_mib_s": (size / (1024 * 1024)) / gzip_decomp_s
        if gzip_decomp_s
        else 0.0,
        "scans_decompress_mib_s": (size / (1024 * 1024)) / scans_decomp_s
        if scans_decomp_s
        else 0.0,
        "gzip_rounds": gzip_rounds,
        "scans_rounds": scans_rounds,
        "scans_method": scans_meta["method"],
        "scans_transformed_size": scans_meta["transformed_size"],
        "scans_dict_size": scans_meta["dict_size"],
        "scans_dict_z_size": scans_meta["dict_z_size"],
        "scans_payload_size": scans_meta["payload_size"],
    }
    if zstd_blob is not None and zstd_meta is not None and zstd_compress_s is not None:
        zstd_size = len(zstd_blob)
        row.update(
            {
                "zstd_bytes": zstd_size,
                "zstd_minus_gzip_bytes": zstd_size - gzip_size,
                "zstd_vs_gzip_percent": ((zstd_size / gzip_size) - 1.0) * 100.0
                if gzip_size
                else 0.0,
                "zstd_compress_s": zstd_compress_s,
                "zstd_decompress_median_s": zstd_decomp_s,
                "zstd_decompress_mib_s": (size / (1024 * 1024)) / zstd_decomp_s
                if zstd_decomp_s
                else 0.0,
                "zstd_rounds": zstd_rounds,
                "zstd_payload_size": zstd_meta["payload_size"],
            }
        )
    return row


def _fmt_seconds(value: float) -> str:
    if value < 0.001:
        return f"{value * 1_000_000:.0f} us"
    if value < 1:
        return f"{value * 1000:.2f} ms"
    return f"{value:.2f} s"


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    total_input = sum(int(r["input_bytes"]) for r in rows)
    total_gzip = sum(int(r["gzip_bytes"]) for r in rows)
    total_scans = sum(int(r["scans_bytes"]) for r in rows)
    has_zstd = all("zstd_bytes" in r for r in rows)
    total_zstd = sum(int(r.get("zstd_bytes", 0)) for r in rows)

    lines = [
        "# SCANS v0 Benchmark",
        "",
        "Baseline: Python `gzip.compress(..., compresslevel=9, mtime=0)`.",
        "SCANS-deflate: per-file mined finite dictionary + raw deflate payload + CRC.",
    ]
    if has_zstd:
        lines.append(
            "SCANS-zstd19: same SCANS container with Zstandard level 19 as an optimized entropy-backend proxy."
        )
    lines.append("")
    if has_zstd:
        lines += [
            "| file | input | gzip | gzip decode | SCANS-deflate | delta | deflate decode | SCANS-zstd19 | delta | zstd decode |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    else:
        lines += [
            "| file | input | gzip | SCANS-deflate | delta | gzip decode | deflate decode | method | dict |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    for row in rows:
        file_name = Path(str(row["file"])).name
        if has_zstd:
            lines.append(
                "| "
                f"{file_name} | "
                f"{int(row['input_bytes']):,} | "
                f"{int(row['gzip_bytes']):,} | "
                f"{_fmt_seconds(float(row['gzip_decompress_median_s']))} | "
                f"{int(row['scans_bytes']):,} | "
                f"{int(row['scans_minus_gzip_bytes']):+,} "
                f"({float(row['scans_vs_gzip_percent']):+.2f}%) | "
                f"{_fmt_seconds(float(row['scans_decompress_median_s']))} | "
                f"{int(row['zstd_bytes']):,} | "
                f"{int(row['zstd_minus_gzip_bytes']):+,} "
                f"({float(row['zstd_vs_gzip_percent']):+.2f}%) | "
                f"{_fmt_seconds(float(row['zstd_decompress_median_s']))} |"
            )
        else:
            lines.append(
                "| "
                f"{file_name} | "
                f"{int(row['input_bytes']):,} | "
                f"{int(row['gzip_bytes']):,} | "
                f"{int(row['scans_bytes']):,} | "
                f"{int(row['scans_minus_gzip_bytes']):+,} "
                f"({float(row['scans_vs_gzip_percent']):+.2f}%) | "
                f"{_fmt_seconds(float(row['gzip_decompress_median_s']))} | "
                f"{_fmt_seconds(float(row['scans_decompress_median_s']))} | "
                f"{int(row['scans_method'])} | "
                f"{int(row['scans_dict_size']):,} |"
            )

    lines += [
        "",
        "## Totals",
        "",
        f"- Input bytes: `{total_input:,}`",
        f"- gzip bytes: `{total_gzip:,}`",
        f"- SCANS bytes: `{total_scans:,}`",
        f"- SCANS delta: `{total_scans - total_gzip:+,}` bytes "
        f"({((total_scans / total_gzip) - 1.0) * 100.0:+.2f}%)",
    ]
    if has_zstd:
        lines += [
            f"- SCANS-zstd19 bytes: `{total_zstd:,}`",
            f"- SCANS-zstd19 delta: `{total_zstd - total_gzip:+,}` bytes "
            f"({((total_zstd / total_gzip) - 1.0) * 100.0:+.2f}%)",
        ]
    lines += [
        "",
        "## Notes",
        "",
        "- This is an intentionally conservative first prototype. It does not yet include a custom rANS backend or blockwise packet closure.",
        "- Method `0` is identity/raw deflate. Method `1` is the LZP predictive-residual transform.",
        "- Method `2` is the optional Zstandard backend proxy. It requires the `zstandard` Python package for this benchmark; in production this maps to the optimized entropy backend.",
        "- Decode time includes Python header parsing, optional dictionary inflation, entropy decode, inverse transform, and CRC verification.",
        "- The current per-file dictionary is stored inside the stream, so these mid-sized files correctly fall back to no embedded dictionary.",
    ]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Benchmark SCANS v0 against gzip")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/compression/reports/scans_benchmark.json"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/compression/reports/scans_benchmark.md"),
    )
    args = parser.parse_args(argv)

    paths = args.files or [Path(p) for p in DEFAULT_FILES]
    rows = []
    for path in paths:
        if not path.exists():
            print(f"skip missing file: {path}", file=sys.stderr)
            continue
        print(f"benchmarking {path}...", file=sys.stderr)
        rows.append(benchmark_file(path))

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(rows, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
