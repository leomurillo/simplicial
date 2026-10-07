#!/usr/bin/env python3
"""Apex packet-song benchmark against WebP lossless.

This is a size experiment, not the finalized SIGI bitstream. It tests the T9
hunch:

    low conductor/Fourier packet song + exact residual tail

For each transformed channel tile, the compressor compares:

- current best SIGI local predictor + context Rice;
- a small set of Fourier packet songs, reconstructed from quantized low or
  dominant FFT coefficients, plus exact context-Rice residuals.

The reported packet-song size includes deterministic coefficient metadata,
tile headers, SIGI-style container overhead, and byte padding.
"""

from __future__ import annotations

import argparse
import binascii
import io
import json
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

import benchmark_sigi_vs_webp_fast as fast
import cell_song_poc
import simplicial_image_codec as sigi


SCALES = (1, 2, 4)
LOW_RADII = (0, 1, 2)
AXIS_RADII = (2, 3)
TOP_COUNTS = (4, 8, 16)


@dataclass(frozen=True)
class PacketChoice:
    bytes: int
    model: str
    scale: int
    saved_vs_context: int


def signed_varint_size(value: int) -> int:
    return sigi.signed_varint_size(int(value))


def coeff_size(real: int, imag: int) -> int:
    return signed_varint_size(real) + signed_varint_size(imag)


def low_rows(height: int, radius: int) -> list[int]:
    if radius == 0:
        return [0]
    rows = list(range(radius + 1))
    rows += list(range(height - radius, height))
    return sorted(set(row for row in rows if 0 <= row < height))


def low_cols(width: int, radius: int) -> list[int]:
    return [col for col in range(radius + 1) if col <= width // 2]


def low_mask(shape: tuple[int, int], radius: int) -> list[tuple[int, int]]:
    height, width = shape
    return [(row, col) for row in low_rows(height, radius) for col in low_cols(width, radius)]


def axis_mask(shape: tuple[int, int], radius: int, axis: str) -> list[tuple[int, int]]:
    height, width = shape
    if axis == "row":
        return [(row, 0) for row in low_rows(height, radius)]
    if axis == "col":
        return [(0, col) for col in low_cols(width, radius)]
    raise ValueError(f"bad axis {axis!r}")


def top_mask(coeffs: np.ndarray, count: int) -> list[tuple[int, int]]:
    flat = np.abs(coeffs).ravel()
    count = min(count, flat.size)
    if count <= 0:
        return []
    indices = np.argpartition(flat, -count)[-count:]
    indices = indices[np.argsort(indices)]
    width = coeffs.shape[1]
    return [(int(index // width), int(index % width)) for index in indices]


def candidate_masks(coeffs: np.ndarray, shape: tuple[int, int]) -> list[tuple[str, list[tuple[int, int]], bool]]:
    masks: list[tuple[str, list[tuple[int, int]], bool]] = []
    for radius in LOW_RADII:
        masks.append((f"low-r{radius}", low_mask(shape, radius), False))
    for radius in AXIS_RADII:
        masks.append((f"row-r{radius}", axis_mask(shape, radius, "row"), False))
        masks.append((f"col-r{radius}", axis_mask(shape, radius, "col"), False))
    for count in TOP_COUNTS:
        masks.append((f"top-{count}", top_mask(coeffs, count), True))
    return masks


def packet_prediction(
    coeffs: np.ndarray,
    shape: tuple[int, int],
    mask: list[tuple[int, int]],
    scale: int,
) -> tuple[np.ndarray, int]:
    height, width = shape
    norm = float(np.sqrt(height * width))
    kept = np.zeros_like(coeffs)
    metadata = 0
    for row, col in mask:
        value = coeffs[row, col]
        qreal = int(np.rint(value.real * scale))
        qimag = int(np.rint(value.imag * scale))
        metadata += coeff_size(qreal, qimag)
        kept[row, col] = complex(qreal / scale, qimag / scale)
    pred = np.rint(np.fft.irfft2(kept * norm, s=shape)).astype(np.int32)
    return pred, metadata


def packet_tile_bytes(
    tile: np.ndarray,
    tile_ctx: np.ndarray,
    model_name: str,
    mask: list[tuple[int, int]],
    has_indices: bool,
    scale: int,
) -> int:
    coeffs = np.fft.rfft2(tile) / float(np.sqrt(tile.size))
    pred, metadata = packet_prediction(coeffs, tile.shape, mask, scale)
    if has_indices:
        last = 0
        for row, col in mask:
            index = row * coeffs.shape[1] + col
            metadata += len(cell_song_poc.put_varint(index - last))
            last = index
    bits = fast.best_context_rice_bits(fast.zigzag_np(tile - pred), tile_ctx)
    # 1 byte model/scale, 4 bytes context-Rice ks, coefficient metadata, padded bits.
    return 1 + 4 + metadata + ((bits + 7) // 8)


def best_packet_tile(tile: np.ndarray, tile_ctx: np.ndarray, context_bytes: int) -> PacketChoice:
    coeffs = np.fft.rfft2(tile) / float(np.sqrt(tile.size))
    best = PacketChoice(bytes=context_bytes, model="context", scale=0, saved_vs_context=0)
    for model_name, mask, has_indices in candidate_masks(coeffs, tile.shape):
        if not mask:
            continue
        for scale in SCALES:
            encoded = packet_tile_bytes(tile, tile_ctx, model_name, mask, has_indices, scale)
            if encoded < best.bytes:
                best = PacketChoice(
                    bytes=encoded,
                    model=model_name,
                    scale=scale,
                    saved_vs_context=context_bytes - encoded,
                )
    return best


def apex_packet_payload_size(channels: list[np.ndarray]) -> tuple[int, dict[str, object]]:
    total = 0
    total_tiles = 0
    packet_tiles = 0
    saved = 0
    model_counts: Counter[str] = Counter()
    for channel in channels:
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        height, width = channel.shape
        for ty in range(0, height, sigi.TILE):
            for tx in range(0, width, sigi.TILE):
                y2 = min(ty + sigi.TILE, height)
                x2 = min(tx + sigi.TILE, width)
                ys = slice(ty, y2)
                xs = slice(tx, x2)
                tile = channel[ys, xs]
                tile_ctx = contexts[ys, xs]
                context_bytes = fast.best_context_tile_bytes(
                    tile, tile_ctx, left, up, up_left, up_right, ys, xs
                )
                choice = best_packet_tile(tile, tile_ctx, context_bytes)
                total_tiles += 1
                total += choice.bytes
                if choice.model != "context":
                    packet_tiles += 1
                    saved += choice.saved_vs_context
                    model_counts[f"{choice.model}@{choice.scale}"] += 1
    return total, {
        "tiles": total_tiles,
        "packet_tiles": packet_tiles,
        "packet_saved_bytes": saved,
        "packet_models": dict(model_counts),
    }


def benchmark_image(path: Path, crop_size: int) -> dict[str, object]:
    with Image.open(path) as image:
        image = image.convert("RGB")
        image = fast.center_crop(image, crop_size)
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
    header = fast.sigi_header_size(rgb, width, height)
    rice_payload = fast.context_rice_payload_size(fast.transform_channels(rgb, width, height, "g-bg-ravg"))
    packet_payload, stats = apex_packet_payload_size(
        fast.transform_channels(rgb, width, height, "g-bg-ravg")
    )
    elapsed = time.perf_counter() - start
    rice_size = header + 1 + rice_payload
    packet_size = header + 1 + packet_payload
    return {
        "file": str(path),
        "crop_size": crop_size,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "webp_lossless_encode_s": webp_s,
        "sigi_context_rice_bytes": rice_size,
        "apex_packet_bytes": packet_size,
        "apex_packet_estimate_s": elapsed,
        "stats": stats,
    }


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# Apex Packet Song vs WebP Lossless",
        "",
        "Each JPG is decoded to RGB first. Apex packet sizes are exact estimates for the experimental packet-song model plus exact context-Rice residual tail.",
        "",
        "| file | dimensions | WebP lossless | SIGI context Rice | Apex packet | Apex vs WebP | packet tiles |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    total_webp = total_rice = total_packet = 0
    for row in rows:
        webp = int(row["webp_lossless_bytes"])
        rice = int(row["sigi_context_rice_bytes"])
        packet = int(row["apex_packet_bytes"])
        stats = row["stats"]  # type: ignore[assignment]
        total_webp += webp
        total_rice += rice
        total_packet += packet
        lines.append(
            f"| {Path(str(row['file'])).name} | {row['width']}x{row['height']} | "
            f"{webp:,} | {rice:,} | {packet:,} | "
            f"{packet - webp:+,} ({((packet / webp) - 1.0) * 100.0:+.2f}%) | "
            f"{stats['packet_tiles']} |"  # type: ignore[index]
        )
    lines += [
        "",
        "## Totals",
        "",
        f"- WebP lossless bytes: `{total_webp:,}`",
        f"- SIGI context Rice bytes: `{total_rice:,}`",
        f"- Apex packet bytes: `{total_packet:,}`",
        f"- Apex packet vs WebP: `{total_packet - total_webp:+,}` bytes "
        f"({((total_packet / total_webp) - 1.0) * 100.0:+.2f}%)",
        f"- Apex packet vs context Rice: `{total_packet - total_rice:+,}` bytes "
        f"({((total_packet / total_rice) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- This is a POC estimator, not the final SIGI stream.",
        "- Packet metadata includes quantized FFT coefficients and optional sparse indices.",
        "- Residuals are still exact; the final decoded RGB would be lossless.",
    ]
    for row in rows:
        stats = row["stats"]  # type: ignore[assignment]
        lines.append(f"- `{Path(str(row['file'])).name}` packet models: `{stats['packet_models']}`.")  # type: ignore[index]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/apex_packet_vs_webp.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/apex_packet_vs_webp.md"))
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
