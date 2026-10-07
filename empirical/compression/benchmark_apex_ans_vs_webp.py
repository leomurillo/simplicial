#!/usr/bin/env python3
"""Apex-ANS estimator against WebP lossless.

This is the native analog of an adaptive rANS/arithmetic backend. It keeps the
SIGI gauge/predictor front-end, then estimates a deterministic no-codebook
adaptive entropy coder:

    context -> symbol counts, updated after each decoded residual

For a seen residual symbol, the coder pays -log2(count / (total + 1)).
For a new residual symbol, it pays an escape cost log2(total + 1) plus a
varint literal. This is intentionally simple, but it is implementable as a
real range/rANS stream and needs no per-image probability table.
"""

from __future__ import annotations

import argparse
import io
import json
import math
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

import benchmark_sigi_vs_webp_fast as fast
import cell_song_poc
import simplicial_image_codec as sigi


TRANSFORMS = ("ycocg", "green16", "g-bg-ravg")
CONTEXT_SCHEMES: dict[str, tuple[int, ...]] = {
    "ctx": (1,),
    "ch-ctx": (0, 1),
    "ch-ctx-pred": (0, 1, 2),
    "ch-ctx-pred-grad": (0, 1, 2, 3),
    "ch-ctx-pred-grad-energy": (0, 1, 2, 3, 4),
}


@dataclass(frozen=True)
class ResidualItems:
    items: list[tuple[int, int, int, int, int, int]]
    tile_headers: int


def universal_literal_bits(symbol: int) -> int:
    return 8 * len(cell_song_poc.put_varint(symbol))


def gradient_class(value: int) -> int:
    if value < 8:
        return 0
    if value < 32:
        return 1
    if value < 128:
        return 2
    return 3


def energy_class(value: float) -> int:
    if value < 1.5:
        return 0
    if value < 3.0:
        return 1
    if value < 7.0:
        return 2
    if value < 15.0:
        return 3
    return 4


def gather_residual_items(rgb: bytes, width: int, height: int, transform: str) -> ResidualItems:
    items: list[tuple[int, int, int, int, int, int]] = []
    tile_headers = 0
    channels = fast.transform_channels(rgb, width, height, transform)
    for channel_index, channel in enumerate(channels):
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        h, w = channel.shape
        for ty in range(0, h, sigi.TILE):
            for tx in range(0, w, sigi.TILE):
                ys = slice(ty, min(ty + sigi.TILE, h))
                xs = slice(tx, min(tx + sigi.TILE, w))
                tile = channel[ys, xs]
                tile_contexts = contexts[ys, xs]
                predictor, residual = fast.best_context_tile_residuals(
                    tile, tile_contexts, left, up, up_left, up_right, ys, xs
                )
                tile_headers += 1
                grad_class = gradient_class(int(np.mean(gradient[ys, xs])))
                res_energy_class = energy_class(float(np.mean(np.abs(residual))))
                for ctx, value in zip(tile_contexts.ravel(), residual.ravel()):
                    items.append(
                        (
                            channel_index,
                            int(ctx),
                            int(predictor),
                            grad_class,
                            res_energy_class,
                            sigi.zigzag(int(value)),
                        )
                    )
    return ResidualItems(items=items, tile_headers=tile_headers)


def adaptive_escape_bits(
    items: list[tuple[int, int, int, int, int, int]],
    fields: tuple[int, ...],
) -> tuple[float, int, int]:
    counts: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    totals: dict[tuple[int, ...], int] = defaultdict(int)
    bits = 0.0
    new_symbols = 0
    for item in items:
        key = tuple(item[index] for index in fields)
        symbol = item[-1]
        counter = counts[key]
        total = totals[key]
        if counter[symbol]:
            bits += -math.log2(counter[symbol] / (total + 1.0))
        else:
            bits += math.log2(total + 1.0) + universal_literal_bits(symbol)
            new_symbols += 1
        counter[symbol] += 1
        totals[key] = total + 1
    return bits, new_symbols, len(counts)


def static_ideal_bits(
    items: list[tuple[int, int, int, int, int, int]],
    fields: tuple[int, ...],
) -> tuple[float, int]:
    counts: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    for item in items:
        counts[tuple(item[index] for index in fields)][item[-1]] += 1
    bits = 0.0
    nonzero = 0
    for counter in counts.values():
        total = sum(counter.values())
        nonzero += len(counter)
        for count in counter.values():
            bits += count * math.log2(total / count)
    return bits, nonzero


def estimate_models(rgb: bytes, width: int, height: int) -> dict[str, dict[str, object]]:
    header = fast.sigi_header_size(rgb, width, height) + 1
    results: dict[str, dict[str, object]] = {}
    for transform in TRANSFORMS:
        gathered = gather_residual_items(rgb, width, height, transform)
        for scheme, fields in CONTEXT_SCHEMES.items():
            start = time.perf_counter()
            adaptive_bits, new_symbols, context_count = adaptive_escape_bits(gathered.items, fields)
            ideal_bits, ideal_nonzero = static_ideal_bits(gathered.items, fields)
            elapsed = time.perf_counter() - start
            key = f"{transform}/{scheme}"
            results[key] = {
                "bytes": header + gathered.tile_headers + math.ceil(adaptive_bits / 8),
                "ideal_no_codebook_bytes": header + gathered.tile_headers + math.ceil(ideal_bits / 8),
                "transform": transform,
                "scheme": scheme,
                "tile_header_bytes": gathered.tile_headers,
                "contexts": context_count,
                "new_symbols": new_symbols,
                "ideal_nonzero_symbols": ideal_nonzero,
                "estimate_s": elapsed,
            }
    return results


def benchmark_image(path: Path, crop_size: int) -> dict[str, object]:
    with Image.open(path) as image:
        image = fast.center_crop(image.convert("RGB"), crop_size)
        width, height = image.size
        rgb = image.tobytes()

    webp_start = time.perf_counter()
    buf = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(
        buf,
        format="WEBP",
        lossless=True,
        quality=100,
        method=6,
    )
    webp_size = len(buf.getvalue())
    webp_s = time.perf_counter() - webp_start

    start = time.perf_counter()
    modes = estimate_models(rgb, width, height)
    elapsed = time.perf_counter() - start
    best_name, best = min(modes.items(), key=lambda item: int(item[1]["bytes"]))
    ideal_name, ideal = min(modes.items(), key=lambda item: int(item[1]["ideal_no_codebook_bytes"]))
    return {
        "file": str(path),
        "crop_size": crop_size,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "webp_lossless_encode_s": webp_s,
        "apex_ans_best_mode": best_name,
        "apex_ans_bytes": int(best["bytes"]),
        "apex_ans_ideal_best_mode": ideal_name,
        "apex_ans_ideal_no_codebook_bytes": int(ideal["ideal_no_codebook_bytes"]),
        "apex_ans_estimate_s": elapsed,
        "modes": modes,
    }


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# Apex-ANS vs WebP Lossless",
        "",
        "Each image is decoded to RGB first. Apex-ANS is a no-codebook adaptive entropy estimate over SIGI residuals using native gauge/context state.",
        "",
        "| file | dimensions | WebP lossless | Apex-ANS | mode | vs WebP | ideal no-codebook |",
        "|---|---:|---:|---:|---|---:|---:|",
    ]
    total_webp = total_ans = total_ideal = 0
    for row in rows:
        webp = int(row["webp_lossless_bytes"])
        ans = int(row["apex_ans_bytes"])
        ideal = int(row["apex_ans_ideal_no_codebook_bytes"])
        total_webp += webp
        total_ans += ans
        total_ideal += ideal
        lines.append(
            f"| {Path(str(row['file'])).name} | {row['width']}x{row['height']} | "
            f"{webp:,} | {ans:,} | `{row['apex_ans_best_mode']}` | "
            f"{ans - webp:+,} ({((ans / webp) - 1.0) * 100.0:+.2f}%) | "
            f"{ideal:,} |"
        )
    lines += [
        "",
        "## Totals",
        "",
        f"- WebP lossless bytes: `{total_webp:,}`",
        f"- Apex-ANS bytes: `{total_ans:,}`",
        f"- Apex-ANS vs WebP: `{total_ans - total_webp:+,}` bytes "
        f"({((total_ans / total_webp) - 1.0) * 100.0:+.2f}%)",
        f"- Ideal no-codebook Apex entropy bytes: `{total_ideal:,}`",
        f"- Ideal no-codebook vs WebP: `{total_ideal - total_webp:+,}` bytes "
        f"({((total_ideal / total_webp) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- This is a feasible entropy-model estimate, not a final rANS bitstream.",
        "- New residual symbols are encoded as adaptive escapes plus varint literals, so the estimate does not rely on stored codebooks.",
        "- The `ideal no-codebook` column removes adaptation/escape friction and measures the model ceiling.",
    ]
    for row in rows:
        best = row["modes"][row["apex_ans_best_mode"]]  # type: ignore[index]
        lines.append(
            f"- `{Path(str(row['file'])).name}` best contexts: `{best['contexts']}`, "
            f"new symbols: `{best['new_symbols']}`."
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/apex_ans_vs_webp.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/apex_ans_vs_webp.md"))
    args = parser.parse_args(argv)

    rows = []
    for path in args.images:
        print(f"benchmarking {path}...", file=sys.stderr)
        rows.append(benchmark_image(path, args.crop_size))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(rows, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
