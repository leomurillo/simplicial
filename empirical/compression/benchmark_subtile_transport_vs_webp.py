#!/usr/bin/env python3
"""Sub-tile transported residual-string estimator against WebP lossless.

This is the T13-T15 refinement-boundary prototype:

    reversible gauge -> local tile predictor -> residual subblocks
    -> optional transported residual strings -> Apex posterior estimate.

It also tests an N1-inspired residual-tile unitary packet class: a tiny stored
summary of where residual energy lives in character/Fourier packets.

It is still an estimator, not a final compressed bitstream. Unlike the earlier
whole-tile transport benchmark, this script refines the exact residual boundary
into small blocks and only stores a reference command when the exact residual
tail plus command metadata beats direct residual coding locally.
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
DEFAULT_BLOCK_SIZE = 8
SEARCH_BACK = 8
FALLBACK_BACK = 3
MIN_COPY_DIRECT_SCORE = 12
MIN_ACCEPT_SAVE = 2


@dataclass(frozen=True)
class BlockRecord:
    index: int
    residual: np.ndarray
    energy_class: int
    mean: int


@dataclass(frozen=True)
class BlockChoice:
    residual_tail: np.ndarray
    mode_id: int
    metadata_bytes: int
    model: str
    direct_score: int
    saved_direct_score: int


@dataclass(frozen=True)
class ResidualStream:
    items: list[tuple[int, int, int, int, int, int, int]]
    metadata_bytes: int
    energy_metadata_bytes: int
    unitary_metadata_bytes: int
    blocks: int
    transported_blocks: int
    dc_blocks: int
    saved_direct_score_bytes: int
    model_counts: dict[str, int]


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


def unitary_packet_class(tile: np.ndarray) -> int:
    """Small N1-inspired conductor/Fourier packet class for residual tiles.

    N1 treats the Helmert-to-character transfer as an apex unitary. For the
    codec, the practical question is whether residual energy lives mostly in
    low, middle, or high conductor packets. This class is stored as side
    metadata when used by an entropy context.
    """

    arr = tile.astype(np.float64)
    arr -= float(np.mean(arr))
    spatial_energy = float(np.sum(arr * arr))
    if spatial_energy < max(1.0, tile.size * 0.75):
        return 0

    spectrum = np.abs(np.fft.rfft2(arr)) ** 2
    if spectrum.size:
        spectrum[0, 0] = 0.0
    height, width = tile.shape
    fy = np.fft.fftfreq(height)[:, None]
    fx = np.fft.rfftfreq(width)[None, :]
    radius = np.sqrt(fy * fy + fx * fx)
    low = float(np.sum(spectrum[(radius > 0.0) & (radius <= 0.18)]))
    mid = float(np.sum(spectrum[(radius > 0.18) & (radius <= 0.36)]))
    high = float(np.sum(spectrum[radius > 0.36]))
    band = int(np.argmax([low, mid, high]))
    return band + 1


def residual_score_bytes(residual: np.ndarray, contexts: np.ndarray) -> int:
    bits = fast.best_context_rice_bits(fast.zigzag_np(residual), contexts)
    return (bits + 7) // 8


def transport_metadata_size(ref_distance: int, offset: int) -> int:
    # One command byte plus reference distance and signed affine/DC offset.
    return 1 + varint_size(ref_distance) + signed_size(offset)


def dc_metadata_size(offset: int) -> int:
    # One command byte plus signed block-DC correction.
    return 1 + signed_size(offset)


def compatible_records(records: deque[BlockRecord], current_energy: int) -> list[BlockRecord]:
    out: list[BlockRecord] = []
    for record in reversed(records):
        if abs(record.energy_class - current_energy) <= 1:
            out.append(record)
        if len(out) >= SEARCH_BACK:
            break
    if out:
        return out
    return list(reversed(records))[: min(FALLBACK_BACK, len(records))]


def choose_block(
    block: np.ndarray,
    block_contexts: np.ndarray,
    records: deque[BlockRecord],
    block_index: int,
) -> BlockChoice:
    direct_score = residual_score_bytes(block, block_contexts)
    best = BlockChoice(
        residual_tail=block,
        mode_id=0,
        metadata_bytes=0,
        model="direct",
        direct_score=direct_score,
        saved_direct_score=0,
    )

    # Sub-tile Schur/DC correction: integrate out a constant boundary mode.
    offset = int(np.rint(float(np.mean(block))))
    if offset:
        tail = block - offset
        metadata = dc_metadata_size(offset)
        score = metadata + residual_score_bytes(tail, block_contexts)
        if score <= direct_score - best.saved_direct_score - MIN_ACCEPT_SAVE:
            best = BlockChoice(
                residual_tail=tail,
                mode_id=1,
                metadata_bytes=metadata,
                model="dc",
                direct_score=direct_score,
                saved_direct_score=direct_score - score,
            )

    if records and direct_score >= MIN_COPY_DIRECT_SCORE:
        current_energy = energy_class(float(np.mean(np.abs(block))))
        for record in compatible_records(records, current_energy):
            if record.residual.shape != block.shape:
                continue
            ref_distance = block_index - record.index
            ref = record.residual
            copy_offset = int(np.rint(float(np.mean(block - ref))))
            tail = block - ref - copy_offset
            metadata = transport_metadata_size(ref_distance, copy_offset)
            coarse_score = metadata + float(np.mean(np.abs(tail))) * tail.size / 8.0
            if coarse_score > direct_score - best.saved_direct_score - MIN_ACCEPT_SAVE:
                continue
            score = metadata + residual_score_bytes(tail, block_contexts)
            if score <= direct_score - best.saved_direct_score - MIN_ACCEPT_SAVE:
                best = BlockChoice(
                    residual_tail=tail,
                    mode_id=2,
                    metadata_bytes=metadata,
                    model="copy",
                    direct_score=direct_score,
                    saved_direct_score=direct_score - score,
                )

    return best


def gather_baseline_residuals(
    channel: np.ndarray,
    contexts: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, int, int, Counter[str]]:
    left, up, up_left, up_right = fast.shifted_neighbors(channel)
    residuals = np.zeros_like(channel, dtype=np.int32)
    tile_energy = np.zeros_like(contexts, dtype=np.uint8)
    tile_unitary = np.zeros_like(contexts, dtype=np.uint8)
    tile_metadata = 0
    tile_energy_units = 0
    predictors: Counter[str] = Counter()
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
            residuals[ys, xs] = residual
            tile_energy[ys, xs] = energy_class(float(np.mean(np.abs(residual))))
            tile_unitary[ys, xs] = unitary_packet_class(residual)
            tile_metadata += 1
            tile_energy_units += 1
            predictors[f"pred-{predictor}"] += 1
    return residuals, tile_energy, tile_unitary, tile_metadata, tile_energy_units, predictors


def gather_stream(rgb: bytes, width: int, height: int, block_size: int, *, refine: bool) -> ResidualStream:
    items: list[tuple[int, int, int, int, int, int]] = []
    metadata_bytes = 0
    tile_energy_units = 0
    block_count = 0
    transported_blocks = 0
    dc_blocks = 0
    saved_direct = 0
    model_counts: Counter[str] = Counter()

    channels = fast.transform_channels(rgb, width, height, TRANSFORM)
    for channel_index, channel in enumerate(channels):
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        residuals, tile_energy, tile_unitary, tile_metadata, channel_energy_units, predictors = gather_baseline_residuals(
            channel, contexts
        )
        metadata_bytes += tile_metadata
        tile_energy_units += channel_energy_units
        model_counts.update(predictors)

        records: deque[BlockRecord] = deque(maxlen=SEARCH_BACK * 4)
        h, w = channel.shape
        for by in range(0, h, block_size):
            for bx in range(0, w, block_size):
                ys = slice(by, min(by + block_size, h))
                xs = slice(bx, min(bx + block_size, w))
                block = residuals[ys, xs]
                block_contexts = contexts[ys, xs]
                if refine:
                    choice = choose_block(block, block_contexts, records, block_count)
                else:
                    choice = BlockChoice(
                        residual_tail=block,
                        mode_id=0,
                        metadata_bytes=0,
                        model="direct",
                        direct_score=0,
                        saved_direct_score=0,
                    )
                metadata_bytes += choice.metadata_bytes
                model_counts[choice.model] += 1
                saved_direct += choice.saved_direct_score
                if choice.mode_id == 1:
                    dc_blocks += 1
                elif choice.mode_id == 2:
                    transported_blocks += 1

                grad_class = gradient_class(int(np.mean(gradient[ys, xs])))
                tile_energy_class = int(tile_energy[by, bx])
                unitary_class = int(tile_unitary[by, bx])
                for ctx, value in zip(block_contexts.ravel(), choice.residual_tail.ravel()):
                    items.append(
                        (
                            channel_index,
                            int(ctx),
                            choice.mode_id,
                            grad_class,
                            tile_energy_class,
                            unitary_class,
                            sigi.zigzag(int(value)),
                        )
                    )

                if refine:
                    records.append(
                        BlockRecord(
                            index=block_count,
                            residual=block.copy(),
                            energy_class=energy_class(float(np.mean(np.abs(block)))),
                            mean=int(np.rint(float(np.mean(block)))),
                        )
                    )
                block_count += 1

    if refine:
        # Command presence flags for subblock modes. The direct mode uses zero
        # bits in an ideal command stream, but a real stream needs a sparse flag.
        metadata_bytes += (block_count + 7) // 8

    return ResidualStream(
        items=items,
        metadata_bytes=metadata_bytes,
        energy_metadata_bytes=(tile_energy_units * 3 + 7) // 8,
        unitary_metadata_bytes=(tile_energy_units * 2 + 7) // 8,
        blocks=block_count,
        transported_blocks=transported_blocks,
        dc_blocks=dc_blocks,
        saved_direct_score_bytes=saved_direct,
        model_counts=dict(model_counts),
    )


def adaptive_bits(items: list[tuple[int, int, int, int, int, int, int]], fields: tuple[int, ...]) -> tuple[float, int, int]:
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


def static_ideal_bits(items: list[tuple[int, int, int, int, int, int, int]], fields: tuple[int, ...]) -> float:
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
        "ch-ctx-grad": (0, 1, 3),
        "ch-ctx-mode": (0, 1, 2),
        "ch-ctx-mode-grad": (0, 1, 2, 3),
        "ch-ctx-energy": (0, 1, 4),
        "ch-ctx-grad-energy": (0, 1, 3, 4),
        "ch-ctx-mode-energy": (0, 1, 2, 4),
        "ch-ctx-unitary": (0, 1, 5),
        "ch-ctx-grad-unitary": (0, 1, 3, 5),
        "ch-ctx-energy-unitary": (0, 1, 4, 5),
        "ch-ctx-grad-energy-unitary": (0, 1, 3, 4, 5),
    }.items():
        bits, new_symbols, context_count = adaptive_bits(stream.items, fields)
        ideal = static_ideal_bits(stream.items, fields)
        extra_metadata = 0
        if 4 in fields:
            extra_metadata += stream.energy_metadata_bytes
        if 5 in fields:
            extra_metadata += stream.unitary_metadata_bytes
        results[name] = {
            "bytes": header + stream.metadata_bytes + extra_metadata + math.ceil(bits / 8),
            "ideal_no_codebook_bytes": header + stream.metadata_bytes + extra_metadata + math.ceil(ideal / 8),
            "contexts": context_count,
            "new_symbols": new_symbols,
            "extra_metadata_bytes": extra_metadata,
        }
    best_name, best = min(results.items(), key=lambda item: int(item[1]["bytes"]))
    ideal_name, ideal = min(results.items(), key=lambda item: int(item[1]["ideal_no_codebook_bytes"]))
    return {
        "best_scheme": best_name,
        "bytes": int(best["bytes"]),
        "ideal_best_scheme": ideal_name,
        "ideal_no_codebook_bytes": int(ideal["ideal_no_codebook_bytes"]),
        "metadata_bytes": stream.metadata_bytes,
        "energy_metadata_bytes": stream.energy_metadata_bytes,
        "unitary_metadata_bytes": stream.unitary_metadata_bytes,
        "blocks": stream.blocks,
        "transported_blocks": stream.transported_blocks,
        "dc_blocks": stream.dc_blocks,
        "saved_direct_score_bytes": stream.saved_direct_score_bytes,
        "model_counts": stream.model_counts,
        "schemes": results,
    }


def benchmark_image(path: Path, crop_size: int, block_size: int, *, direct_only: bool) -> dict[str, object]:
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
    direct_stream = gather_stream(rgb, width, height, block_size, refine=False)
    direct_estimate = estimate_stream(rgb, width, height, direct_stream)
    if direct_only:
        refined_estimate = direct_estimate
    else:
        refined_stream = gather_stream(rgb, width, height, block_size, refine=True)
        refined_estimate = estimate_stream(rgb, width, height, refined_stream)
    deployed_estimate = min(
        (direct_estimate, refined_estimate),
        key=lambda estimate: int(estimate["bytes"]),
    )
    elapsed = time.perf_counter() - start

    return {
        "file": str(path),
        "crop_size": crop_size,
        "block_size": block_size,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "webp_lossless_encode_s": webp_s,
        "direct_block_apex_ans": direct_estimate,
        "refined_subtile_apex_ans": refined_estimate,
        "subtile_apex_ans": deployed_estimate,
        "direct_only": direct_only,
        "estimate_s": elapsed,
    }


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# Sub-Tile Transported Residual Strings + Apex Posterior vs WebP",
        "",
        "Each image is decoded to RGB first. The codec model keeps the `g-bg-ravg` gauge and local tile predictors, then refines the exact residual boundary into sub-tile blocks. Blocks may use direct residuals, a DC boundary correction, or a transported prior residual string.",
        "",
        "| file | dimensions | block | WebP | direct block Apex | refined sub-tile | deployed | best state | ideal | vs WebP | DC blocks | copy blocks |",
        "|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|",
    ]
    total_webp = total_subtile = total_ideal = 0
    for row in rows:
        webp = int(row["webp_lossless_bytes"])
        direct = row["direct_block_apex_ans"]  # type: ignore[assignment]
        refined = row["refined_subtile_apex_ans"]  # type: ignore[assignment]
        result = row["subtile_apex_ans"]  # type: ignore[assignment]
        direct_bytes = int(direct["bytes"])  # type: ignore[index]
        refined_bytes = int(refined["bytes"])  # type: ignore[index]
        subtile = int(result["bytes"])  # type: ignore[index]
        ideal = int(result["ideal_no_codebook_bytes"])  # type: ignore[index]
        total_webp += webp
        total_subtile += subtile
        total_ideal += ideal
        lines.append(
            f"| {Path(str(row['file'])).name} | {row['width']}x{row['height']} | "
            f"{row['block_size']} | {webp:,} | {direct_bytes:,} | {refined_bytes:,} | {subtile:,} | "
            f"`{result['best_scheme']}` | "
            f"{ideal:,} | {subtile - webp:+,} ({((subtile / webp) - 1.0) * 100.0:+.2f}%) | "
            f"{result['dc_blocks']} | {result['transported_blocks']} |"  # type: ignore[index]
        )
    lines += [
        "",
        "## Totals",
        "",
        f"- WebP lossless bytes: `{total_webp:,}`",
        f"- Deployed sub-tile/direct Apex bytes: `{total_subtile:,}`",
        f"- Deployed sub-tile/direct Apex vs WebP: `{total_subtile - total_webp:+,}` bytes "
        f"({((total_subtile / total_webp) - 1.0) * 100.0:+.2f}%)",
        f"- Ideal no-codebook bytes: `{total_ideal:,}`",
        f"- Ideal no-codebook vs WebP: `{total_ideal - total_webp:+,}` bytes "
        f"({((total_ideal / total_webp) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- This is an estimator, not a final bitstream.",
        "- The deployed value is the smaller of direct block-refined posterior coding and command-refined sub-tile transport.",
        "- When `direct_only` is true in JSON, the refined column is intentionally equal to the direct column to skip the currently unprofitable command-search pass.",
        "- Refined metadata includes local tile predictor bytes, one sparse command-flag bit per subblock, and command bytes for DC/copy subblocks.",
        "- Energy-context schemes include 3 stored side bits per predictor tile; N1 unitary-packet schemes include 2 stored side bits per predictor tile. Other contexts are decoder-visible: channel, local residual context, subblock mode, and spatial gradient class.",
    ]
    for row in rows:
        result = row["subtile_apex_ans"]  # type: ignore[assignment]
        refined = row["refined_subtile_apex_ans"]  # type: ignore[assignment]
        lines.append(
            f"- `{Path(str(row['file'])).name}` deployed blocks: `{result['blocks']}`, metadata bytes: "
            f"`{result['metadata_bytes']}`, energy metadata bytes if used: `{result['energy_metadata_bytes']}`, "
            f"unitary metadata bytes if used: `{result['unitary_metadata_bytes']}`."  # type: ignore[index]
        )
        lines.append(
            f"- `{Path(str(row['file'])).name}` refined saved local-score bytes: "
            f"`{refined['saved_direct_score_bytes']}`, refined model counts: `{refined['model_counts']}`."  # type: ignore[index]
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--block-size", type=int, default=DEFAULT_BLOCK_SIZE)
    parser.add_argument("--direct-only", action="store_true")
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/subtile_transport_vs_webp.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/subtile_transport_vs_webp.md"))
    args = parser.parse_args(argv)

    if args.block_size <= 0:
        raise SystemExit("--block-size must be positive")

    rows = []
    for path in args.images:
        print(f"benchmarking {path}...", file=sys.stderr)
        rows.append(benchmark_image(path, args.crop_size, args.block_size, direct_only=args.direct_only))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(rows, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
