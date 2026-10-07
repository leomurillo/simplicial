#!/usr/bin/env python3
"""Transported Kummer-song estimator against WebP lossless.

This is the next native-codec POC:

    Kummer tile signature -> transported prior tile song -> exact residual
    -> Apex-ANS adaptive entropy.

It is still an estimator, not a final bitstream. The metadata cost includes
mode bytes, reference distances, shift/gain ids, and affine offsets. The exact
residual tail is estimated with the same no-codebook adaptive model used by
``benchmark_apex_ans_vs_webp.py``.
"""

from __future__ import annotations

import argparse
import io
import json
import math
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

import benchmark_sigi_vs_webp_fast as fast
import cell_song_poc
import simplicial_image_codec as sigi


TRANSFORM = "g-bg-ravg"
SEARCH_BACK = 8
PREFILTER_KEEP = 4
SHIFTS = ((0, 0), (0, -1), (0, 1))
GAINS = ((16, 16), (15, 16), (17, 16))
CONTEXT_FIELDS = (0, 1)


@dataclass
class TileRecord:
    index: int
    tile: np.ndarray
    residual: np.ndarray
    kummer_class: int


@dataclass(frozen=True)
class TileChoice:
    residual: np.ndarray
    metadata_bytes: int
    model: str
    local_score: int
    saved_vs_local: int
    kummer_class: int


@dataclass(frozen=True)
class ResidualStream:
    items: list[tuple[int, int, int, int, int, int]]
    metadata_bytes: int
    transport_tiles: int
    transport_saved_local_bytes: int
    model_counts: dict[str, int]
    kummer_counts: dict[int, int]


def literal_bits(symbol: int) -> int:
    return 8 * len(cell_song_poc.put_varint(symbol))


def signed_size(value: int) -> int:
    return sigi.signed_varint_size(int(value))


def varint_size(value: int) -> int:
    return len(cell_song_poc.put_varint(int(value)))


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


def kfun(centered_log: np.ndarray, m: int) -> float:
    return float(np.log(np.mean(np.exp(m * centered_log))))


def kummer_class(tile: np.ndarray) -> int:
    """Compact T10 gauge-corridor class for tile-level decisions.

    The class is intentionally coarse. It is used for candidate selection, not
    as a per-symbol entropy context, because that was too expensive.
    """

    arr = tile.astype(np.float64)
    ledger = np.abs(arr - np.median(arr)) + 1.0
    y = np.log(ledger)
    y -= float(np.mean(y))
    spread = float(np.max(y) - np.min(y))
    if spread < 0.12:
        return 0
    k2 = kfun(y, 2)
    k3 = kfun(y, 3)
    km3 = kfun(y, -3)
    k4 = kfun(y, 4)
    asym = k3 - km3
    if k4 > 3.0:
        return 1 if asym >= 0.0 else 2
    if abs(asym) > 0.7:
        return 3 if asym > 0.0 else 4
    if k2 < 0.25:
        return 5
    if k2 < 0.8:
        return 6
    return 7


def shift_tile(tile: np.ndarray, dy: int, dx: int) -> np.ndarray:
    if dy == 0 and dx == 0:
        return tile
    height, width = tile.shape
    yy = np.clip(np.arange(height) + dy, 0, height - 1)
    xx = np.clip(np.arange(width) + dx, 0, width - 1)
    return tile[np.ix_(yy, xx)]


def affine_prediction(ref: np.ndarray, tile: np.ndarray, gain_num: int, gain_den: int) -> tuple[np.ndarray, int]:
    scaled = np.rint(ref.astype(np.float64) * gain_num / gain_den).astype(np.int32)
    offset = int(np.rint(float(np.mean(tile - scaled))))
    return scaled + offset, offset


def residual_score_bytes(residual: np.ndarray, tile_contexts: np.ndarray) -> int:
    bits = fast.best_context_rice_bits(fast.zigzag_np(residual), tile_contexts)
    return (bits + 7) // 8


def transport_metadata_size(ref_distance: int, offset: int, *, needs_predictor: bool = False) -> int:
    # mode/shift/gain byte + reference distance + affine offset
    return 1 + (1 if needs_predictor else 0) + varint_size(ref_distance) + signed_size(offset)


def compatible_records(records: deque[TileRecord], current_class: int) -> list[TileRecord]:
    out: list[TileRecord] = []
    for record in reversed(records):
        if record.kummer_class == current_class or abs(record.kummer_class - current_class) <= 1:
            out.append(record)
        if len(out) >= SEARCH_BACK:
            break
    return out


def choose_tile(
    tile: np.ndarray,
    tile_contexts: np.ndarray,
    baseline_residual: np.ndarray,
    baseline_predictor: int,
    records: deque[TileRecord],
    tile_index: int,
    current_class: int,
) -> TileChoice:
    baseline_score = 1 + residual_score_bytes(baseline_residual, tile_contexts)
    best = TileChoice(
        residual=baseline_residual,
        metadata_bytes=1,
        model=f"local-p{baseline_predictor}",
        local_score=baseline_score,
        saved_vs_local=0,
        kummer_class=current_class,
    )
    if not records:
        return best

    candidates = compatible_records(records, current_class)
    if not candidates:
        candidates = list(reversed(records))[: min(4, len(records))]

    coarse: list[tuple[float, np.ndarray, int, str]] = []
    for record in candidates:
        if record.tile.shape != tile.shape:
            continue
        ref_distance = tile_index - record.index
        for shift_id, (dy, dx) in enumerate(SHIFTS):
            shifted = shift_tile(record.tile, dy, dx)
            for gain_id, (gain_num, gain_den) in enumerate(GAINS):
                pred, offset = affine_prediction(shifted, tile, gain_num, gain_den)
                residual = tile - pred
                metadata = transport_metadata_size(ref_distance, offset)
                coarse_score = metadata + float(np.mean(np.abs(residual))) * residual.size / 8.0
                coarse.append((coarse_score, residual, metadata, f"tile-s{shift_id}-g{gain_id}"))

                pred_residual, res_offset = affine_prediction(
                    shift_tile(record.residual, dy, dx),
                    baseline_residual,
                    gain_num,
                    gain_den,
                )
                residual_tail = baseline_residual - pred_residual
                residual_metadata = transport_metadata_size(ref_distance, res_offset, needs_predictor=True)
                residual_coarse = (
                    residual_metadata + float(np.mean(np.abs(residual_tail))) * residual_tail.size / 8.0
                )
                coarse.append(
                    (
                        residual_coarse,
                        residual_tail,
                        residual_metadata,
                        f"residual-s{shift_id}-g{gain_id}",
                    )
                )

    for _, residual, metadata, model in sorted(coarse, key=lambda item: item[0])[:PREFILTER_KEEP]:
        score = metadata + residual_score_bytes(residual, tile_contexts)
        if score < best.local_score - best.saved_vs_local:
            best = TileChoice(
                residual=residual,
                metadata_bytes=metadata,
                model=model,
                local_score=baseline_score,
                saved_vs_local=baseline_score - score,
                kummer_class=current_class,
            )
    return best


def gather_stream(rgb: bytes, width: int, height: int, *, transport: bool) -> ResidualStream:
    items: list[tuple[int, int, int, int, int, int]] = []
    metadata_bytes = 0
    transport_tiles = 0
    transport_saved = 0
    model_counts: Counter[str] = Counter()
    kummer_counts: Counter[int] = Counter()

    channels = fast.transform_channels(rgb, width, height, TRANSFORM)
    for channel_index, channel in enumerate(channels):
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        records: deque[TileRecord] = deque(maxlen=SEARCH_BACK * 4)
        tile_index = 0
        h, w = channel.shape
        for ty in range(0, h, sigi.TILE):
            for tx in range(0, w, sigi.TILE):
                ys = slice(ty, min(ty + sigi.TILE, h))
                xs = slice(tx, min(tx + sigi.TILE, w))
                tile = channel[ys, xs]
                tile_contexts = contexts[ys, xs]
                predictor, baseline_residual = fast.best_context_tile_residuals(
                    tile, tile_contexts, left, up, up_left, up_right, ys, xs
                )
                current_class = kummer_class(tile)
                if transport:
                    choice = choose_tile(
                        tile,
                        tile_contexts,
                        baseline_residual,
                        predictor,
                        records,
                        tile_index,
                        current_class,
                    )
                else:
                    choice = TileChoice(
                        residual=baseline_residual,
                        metadata_bytes=1,
                        model=f"local-p{predictor}",
                        local_score=1 + residual_score_bytes(baseline_residual, tile_contexts),
                        saved_vs_local=0,
                        kummer_class=current_class,
                    )

                metadata_bytes += choice.metadata_bytes
                model_counts[choice.model] += 1
                kummer_counts[current_class] += 1
                if not choice.model.startswith("local"):
                    transport_tiles += 1
                    transport_saved += choice.saved_vs_local

                grad_class = gradient_class(int(np.mean(gradient[ys, xs])))
                res_energy_class = energy_class(float(np.mean(np.abs(choice.residual))))
                for ctx, value in zip(tile_contexts.ravel(), choice.residual.ravel()):
                    items.append(
                        (
                            channel_index,
                            int(ctx),
                            0 if choice.model.startswith("local") else 1,
                            grad_class,
                            res_energy_class,
                            sigi.zigzag(int(value)),
                        )
                    )

                records.append(
                    TileRecord(
                        index=tile_index,
                        tile=tile.copy(),
                        residual=baseline_residual.copy(),
                        kummer_class=current_class,
                    )
                )
                tile_index += 1

    return ResidualStream(
        items=items,
        metadata_bytes=metadata_bytes,
        transport_tiles=transport_tiles,
        transport_saved_local_bytes=transport_saved,
        model_counts=dict(model_counts),
        kummer_counts=dict(kummer_counts),
    )


def adaptive_bits(items: list[tuple[int, int, int, int, int, int]], fields: tuple[int, ...]) -> tuple[float, int, int]:
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
            bits += math.log2(total + 1.0) + literal_bits(symbol)
            new_symbols += 1
        counter[symbol] += 1
        totals[key] = total + 1
    return bits, new_symbols, len(counts)


def static_ideal_bits(items: list[tuple[int, int, int, int, int, int]], fields: tuple[int, ...]) -> float:
    counts: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    for item in items:
        counts[tuple(item[index] for index in fields)][item[-1]] += 1
    bits = 0.0
    for counter in counts.values():
        total = sum(counter.values())
        for count in counter.values():
            bits += count * math.log2(total / count)
    return bits


def estimate_stream(rgb: bytes, width: int, height: int, stream: ResidualStream) -> dict[str, object]:
    header = fast.sigi_header_size(rgb, width, height) + 1
    results: dict[str, dict[str, object]] = {}
    for name, fields in {
        "ch-ctx": (0, 1),
        "ch-ctx-transport": (0, 1, 2),
        "ch-ctx-grad": (0, 1, 3),
        "ch-ctx-energy": (0, 1, 4),
        "ch-ctx-grad-energy": (0, 1, 3, 4),
    }.items():
        bits, new_symbols, context_count = adaptive_bits(stream.items, fields)
        ideal = static_ideal_bits(stream.items, fields)
        results[name] = {
            "bytes": header + stream.metadata_bytes + math.ceil(bits / 8),
            "ideal_no_codebook_bytes": header + stream.metadata_bytes + math.ceil(ideal / 8),
            "contexts": context_count,
            "new_symbols": new_symbols,
        }
    best_name, best = min(results.items(), key=lambda item: int(item[1]["bytes"]))
    ideal_name, ideal = min(results.items(), key=lambda item: int(item[1]["ideal_no_codebook_bytes"]))
    return {
        "best_scheme": best_name,
        "bytes": int(best["bytes"]),
        "ideal_best_scheme": ideal_name,
        "ideal_no_codebook_bytes": int(ideal["ideal_no_codebook_bytes"]),
        "metadata_bytes": stream.metadata_bytes,
        "transport_tiles": stream.transport_tiles,
        "transport_saved_local_bytes": stream.transport_saved_local_bytes,
        "model_counts": stream.model_counts,
        "kummer_counts": stream.kummer_counts,
        "schemes": results,
    }


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
    baseline = estimate_stream(rgb, width, height, gather_stream(rgb, width, height, transport=False))
    transported = estimate_stream(rgb, width, height, gather_stream(rgb, width, height, transport=True))
    elapsed = time.perf_counter() - start

    return {
        "file": str(path),
        "crop_size": crop_size,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "webp_lossless_encode_s": webp_s,
        "baseline_apex_ans": baseline,
        "transported_kummer_apex_ans": transported,
        "estimate_s": elapsed,
    }


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# Transported Kummer Song + Apex-ANS vs WebP",
        "",
        "Each image is decoded to RGB first. The transported model searches previous Kummer-compatible tiles, stores a compact reference/shift/gain/offset song, and entropy-codes the exact residual tail with Apex-ANS.",
        "",
        "| file | dimensions | WebP | baseline Apex-ANS | transported Kummer | best state | ideal | vs WebP | transport tiles |",
        "|---|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    total_webp = total_base = total_transport = total_ideal = 0
    for row in rows:
        webp = int(row["webp_lossless_bytes"])
        baseline = row["baseline_apex_ans"]  # type: ignore[assignment]
        transported = row["transported_kummer_apex_ans"]  # type: ignore[assignment]
        base_bytes = int(baseline["bytes"])  # type: ignore[index]
        transport_bytes = int(transported["bytes"])  # type: ignore[index]
        ideal_bytes = int(transported["ideal_no_codebook_bytes"])  # type: ignore[index]
        total_webp += webp
        total_base += base_bytes
        total_transport += transport_bytes
        total_ideal += ideal_bytes
        lines.append(
            f"| {Path(str(row['file'])).name} | {row['width']}x{row['height']} | "
            f"{webp:,} | {base_bytes:,} | {transport_bytes:,} | "
            f"`{transported['best_scheme']}` | {ideal_bytes:,} | "
            f"{transport_bytes - webp:+,} ({((transport_bytes / webp) - 1.0) * 100.0:+.2f}%) | "
            f"{transported['transport_tiles']} |"  # type: ignore[index]
        )
    lines += [
        "",
        "## Totals",
        "",
        f"- WebP lossless bytes: `{total_webp:,}`",
        f"- Baseline Apex-ANS bytes: `{total_base:,}`",
        f"- Transported Kummer Apex-ANS bytes: `{total_transport:,}`",
        f"- Transported Kummer vs WebP: `{total_transport - total_webp:+,}` bytes "
        f"({((total_transport / total_webp) - 1.0) * 100.0:+.2f}%)",
        f"- Transported Kummer vs baseline Apex-ANS: `{total_transport - total_base:+,}` bytes "
        f"({((total_transport / total_base) - 1.0) * 100.0:+.2f}%)",
        f"- Transported ideal no-codebook bytes: `{total_ideal:,}`",
        f"- Transported ideal vs WebP: `{total_ideal - total_webp:+,}` bytes "
        f"({((total_ideal / total_webp) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- This is an estimator, not a final bitstream.",
        "- Kummer state is used for tile-level reference search, not as a per-symbol context.",
        "- The entropy estimator now tries `channel+context`, `channel+context+gradient`, `channel+context+energy`, and their small transport/gradient-energy variants.",
        "- A transport is accepted only when its local residual score plus metadata beats the local predictor score.",
    ]
    for row in rows:
        transported = row["transported_kummer_apex_ans"]  # type: ignore[assignment]
        lines.append(
            f"- `{Path(str(row['file'])).name}` transport saved local-score bytes: "
            f"`{transported['transport_saved_local_bytes']}`, metadata bytes: `{transported['metadata_bytes']}`."  # type: ignore[index]
        )
        lines.append(
            f"- `{Path(str(row['file'])).name}` transport model counts: `{transported['model_counts']}`."  # type: ignore[index]
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/transported_kummer_vs_webp.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/transported_kummer_vs_webp.md"))
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
