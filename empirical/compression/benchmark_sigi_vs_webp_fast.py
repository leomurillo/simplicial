#!/usr/bin/env python3
"""Focused SIGI-vs-WebP lossless benchmark for decoded RGB images.

The regular benchmark emits full SIGI streams in pure Python. That is useful
for verification, but slow on multi-megapixel photos. This script computes the
exact byte size of SIGI's context-Rice modes tile-by-tile, including SIGI
container bytes, tile headers, and byte-padding. It still encodes WebP
lossless for the actual baseline size.
"""

from __future__ import annotations

import argparse
import binascii
import io
import json
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

import cell_song_poc
import simplicial_image_codec as sigi


CONTEXT_THRESHOLDS = np.asarray([4, 8, 16, 32, 64, 128, 256], dtype=np.int32)


def sigi_header_size(rgb: bytes, width: int, height: int) -> int:
    return len(
        sigi.MAGIC
        + bytes((sigi.VERSION,))
        + cell_song_poc.put_varint(width)
        + cell_song_poc.put_varint(height)
        + int.to_bytes(binascii.crc32(rgb) & 0xFFFFFFFF, 4, "little")
    )


def shifted_neighbors(channel: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    height, width = channel.shape
    left = np.zeros_like(channel)
    left[:, 1:] = channel[:, :-1]
    up = np.zeros_like(channel)
    up[1:, :] = channel[:-1, :]
    up_left = np.zeros_like(channel)
    up_left[1:, 1:] = channel[:-1, :-1]
    up_right = up.copy()
    if width > 1:
        candidate = np.zeros_like(channel)
        candidate[1:, :-1] = channel[:-1, 1:]
        x = np.arange(width)
        available = (x + 1 < width) & (((x + 1) % sigi.TILE) != 0)
        up_right[:, available] = candidate[:, available]
    return left, up, up_left, up_right


def predictor_tile(
    pred_id: int,
    left: np.ndarray,
    up: np.ndarray,
    up_left: np.ndarray,
    up_right: np.ndarray,
    ys: slice,
    xs: slice,
) -> np.ndarray:
    l = left[ys, xs]
    u = up[ys, xs]
    ul = up_left[ys, xs]
    ur = up_right[ys, xs]
    if pred_id == sigi.PRED_ZERO:
        return np.zeros_like(l)
    if pred_id == sigi.PRED_LEFT:
        return l
    if pred_id == sigi.PRED_UP:
        return u
    if pred_id == sigi.PRED_AVG:
        return (l + u) // 2
    p = l + u - ul
    if pred_id == sigi.PRED_MEDIAN:
        return np.where(ul >= np.maximum(l, u), np.minimum(l, u), np.where(ul <= np.minimum(l, u), np.maximum(l, u), p))
    if pred_id == sigi.PRED_PAETH:
        pa = np.abs(p - l)
        pb = np.abs(p - u)
        pc = np.abs(p - ul)
        return np.where((pa <= pb) & (pa <= pc), l, np.where(pb <= pc, u, ul))
    if pred_id == sigi.PRED_PLANE:
        return p
    if pred_id == sigi.PRED_LEFT_GRAD:
        return l + ((u - ul) // 2)
    if pred_id == sigi.PRED_UP_GRAD:
        return u + ((l - ul) // 2)
    if pred_id == sigi.PRED_LEFT_WEIGHT:
        return (3 * l + u) // 4
    if pred_id == sigi.PRED_UP_WEIGHT:
        return (l + 3 * u) // 4
    if pred_id == sigi.PRED_UP_RIGHT:
        return ur
    if pred_id == sigi.PRED_LEFT_UP_RIGHT_AVG:
        return (l + ur) // 2
    if pred_id == sigi.PRED_UP_UP_LEFT_AVG:
        return (u + ul) // 2
    if pred_id == sigi.PRED_SELECT:
        return np.where(np.abs(p - l) <= np.abs(p - u), l, u)
    if pred_id == sigi.PRED_NE_PLANE:
        return l + u - ur
    if pred_id == sigi.PRED_LEFT_UP_LEFT_AVG:
        return (l + ul) // 2
    if pred_id == sigi.PRED_UP_UP_RIGHT_AVG:
        return (u + ur) // 2
    if pred_id == sigi.PRED_LEFT_UP_UP_RIGHT_AVG:
        return (l + u + ur) // 3
    if pred_id == sigi.PRED_FOUR_AVG:
        return (l + u + ul + ur) // 4
    if pred_id == sigi.PRED_LEFT2_UP_AVG:
        return (2 * l + u) // 3
    if pred_id == sigi.PRED_LEFT_UP2_AVG:
        return (l + 2 * u) // 3
    raise ValueError(f"bad predictor {pred_id}")


def context_plane(channel: np.ndarray) -> np.ndarray:
    left, up, up_left, up_right = shifted_neighbors(channel)
    gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
    return np.searchsorted(CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)


def zigzag_np(values: np.ndarray) -> np.ndarray:
    return np.where(values >= 0, values * 2, -values * 2 - 1).astype(np.int32, copy=False)


def best_context_rice_bits(mapped: np.ndarray, contexts: np.ndarray) -> int:
    total = 0
    for ctx in range(sigi.RICE_CONTEXTS):
        values = mapped[contexts == ctx]
        if values.size == 0:
            continue
        best = int(np.sum(values + 1, dtype=np.int64))
        for k in range(1, sigi.MAX_RICE_K + 1):
            bits = int(np.sum((values >> k) + 1 + k, dtype=np.int64))
            if bits < best:
                best = bits
        total += best
    return total


def best_rice_code(mapped: np.ndarray) -> tuple[int, int]:
    best_k = 0
    best_bits = int(np.sum(mapped + 1, dtype=np.int64))
    for k in range(1, sigi.MAX_RICE_K + 1):
        bits = int(np.sum((mapped >> k) + 1 + k, dtype=np.int64))
        if bits < best_bits:
            best_k = k
            best_bits = bits
    return best_k, best_bits


def signed_varint_size(value: int) -> int:
    return sigi.signed_varint_size(int(value))


def best_context_tile_bytes(
    tile: np.ndarray,
    tile_ctx: np.ndarray,
    left: np.ndarray,
    up: np.ndarray,
    up_left: np.ndarray,
    up_right: np.ndarray,
    ys: slice,
    xs: slice,
) -> int:
    best_bits: int | None = None
    for pred_id in sigi.PREDICTORS:
        residual = tile - predictor_tile(pred_id, left, up, up_left, up_right, ys, xs)
        bits = best_context_rice_bits(zigzag_np(residual), tile_ctx)
        if best_bits is None or bits < best_bits:
            best_bits = bits
    if best_bits is None:
        raise RuntimeError("empty tile")
    return 5 + ((best_bits + 7) // 8)


def best_context_tile_residuals(
    tile: np.ndarray,
    tile_ctx: np.ndarray,
    left: np.ndarray,
    up: np.ndarray,
    up_left: np.ndarray,
    up_right: np.ndarray,
    ys: slice,
    xs: slice,
) -> tuple[int, np.ndarray]:
    best_pred = sigi.PRED_ZERO
    best_residual: np.ndarray | None = None
    best_bits: int | None = None
    for pred_id in sigi.PREDICTORS:
        residual = tile - predictor_tile(pred_id, left, up, up_left, up_right, ys, xs)
        bits = best_context_rice_bits(zigzag_np(residual), tile_ctx)
        if best_bits is None or bits < best_bits:
            best_pred = pred_id
            best_residual = residual
            best_bits = bits
    if best_residual is None:
        raise RuntimeError("empty tile")
    return best_pred, best_residual


def anova_model_bytes(
    tile: np.ndarray,
    base: int,
    row_effects: np.ndarray | None,
    col_effects: np.ndarray | None,
) -> int:
    prediction = np.full(tile.shape, base, dtype=np.int32)
    metadata = signed_varint_size(base)
    if row_effects is not None:
        prediction += row_effects[:, None]
        metadata += sum(signed_varint_size(value) for value in row_effects)
    if col_effects is not None:
        prediction += col_effects[None, :]
        metadata += sum(signed_varint_size(value) for value in col_effects)
    _, bits = best_rice_code(zigzag_np(tile - prediction))
    return 1 + metadata + ((bits + 7) // 8)


def best_anova_tile_bytes(tile: np.ndarray) -> int:
    height, width = tile.shape
    base = sigi.round_div_nearest(int(np.sum(tile, dtype=np.int64)), width * height)
    row_sums = np.sum(tile, axis=1, dtype=np.int64)
    col_sums = np.sum(tile, axis=0, dtype=np.int64)
    row_effects = np.asarray(
        [sigi.round_div_nearest(int(value), width) - base for value in row_sums],
        dtype=np.int32,
    )
    col_effects = np.asarray(
        [sigi.round_div_nearest(int(value), height) - base for value in col_sums],
        dtype=np.int32,
    )
    return min(
        anova_model_bytes(tile, base, None, None),
        anova_model_bytes(tile, base, row_effects, None),
        anova_model_bytes(tile, base, None, col_effects),
        anova_model_bytes(tile, base, row_effects, col_effects),
    )


def context_rice_payload_size(channels: list[np.ndarray]) -> int:
    total = 0
    for channel in channels:
        left, up, up_left, up_right = shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        height, width = channel.shape
        for ty in range(0, height, sigi.TILE):
            for tx in range(0, width, sigi.TILE):
                y2 = min(ty + sigi.TILE, height)
                x2 = min(tx + sigi.TILE, width)
                ys = slice(ty, y2)
                xs = slice(tx, x2)
                tile = channel[ys, xs]
                tile_ctx = contexts[ys, xs]
                total += best_context_tile_bytes(tile, tile_ctx, left, up, up_left, up_right, ys, xs)
    return total


def context_huffman_payload_size(channels: list[np.ndarray]) -> int:
    total = 0
    for channel in channels:
        left, up, up_left, up_right = shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        height, width = channel.shape
        frequencies: list[list[int]] = [[0] for _ in range(sigi.RICE_CONTEXTS)]
        tiles = 0
        for ty in range(0, height, sigi.TILE):
            for tx in range(0, width, sigi.TILE):
                y2 = min(ty + sigi.TILE, height)
                x2 = min(tx + sigi.TILE, width)
                ys = slice(ty, y2)
                xs = slice(tx, x2)
                tile = channel[ys, xs]
                tile_ctx = contexts[ys, xs]
                _, residual = best_context_tile_residuals(
                    tile, tile_ctx, left, up, up_left, up_right, ys, xs
                )
                tiles += 1
                flat_ctx = tile_ctx.ravel()
                flat_residual = residual.ravel()
                for ctx, value in zip(flat_ctx, flat_residual):
                    symbol = sigi.zigzag(int(value))
                    freq = frequencies[int(ctx)]
                    if symbol >= len(freq):
                        freq.extend([0] * (symbol + 1 - len(freq)))
                    freq[symbol] += 1

        encoded_lengths_size = 0
        bitstream_bits = 0
        for freq in frequencies:
            lengths = sigi.huffman_code_lengths(freq)
            max_symbol = len(lengths) - 1
            while max_symbol > 0 and lengths[max_symbol] == 0:
                max_symbol -= 1
            lengths = lengths[: max_symbol + 1]
            encoded_lengths_size += len(sigi.encode_lengths_rle(lengths))
            bitstream_bits += sum(frequency * lengths[symbol] for symbol, frequency in enumerate(freq[: len(lengths)]))

        channel_size = tiles + encoded_lengths_size + ((bitstream_bits + 7) // 8)
        total += len(cell_song_poc.put_varint(channel_size)) + channel_size
    return total


def anova_rice_payload_size(channels: list[np.ndarray]) -> tuple[int, dict[str, int]]:
    total = 0
    total_tiles = 0
    anova_tiles = 0
    anova_saved_bytes = 0
    for channel in channels:
        left, up, up_left, up_right = shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        height, width = channel.shape
        for ty in range(0, height, sigi.TILE):
            for tx in range(0, width, sigi.TILE):
                y2 = min(ty + sigi.TILE, height)
                x2 = min(tx + sigi.TILE, width)
                ys = slice(ty, y2)
                xs = slice(tx, x2)
                tile = channel[ys, xs]
                tile_ctx = contexts[ys, xs]
                context_bytes = best_context_tile_bytes(
                    tile, tile_ctx, left, up, up_left, up_right, ys, xs
                )
                anova_bytes = best_anova_tile_bytes(tile)
                total_tiles += 1
                if anova_bytes < context_bytes:
                    anova_tiles += 1
                    anova_saved_bytes += context_bytes - anova_bytes
                    total += anova_bytes
                else:
                    total += context_bytes
    return total, {
        "tiles": total_tiles,
        "anova_tiles": anova_tiles,
        "anova_saved_bytes": anova_saved_bytes,
    }


def center_crop(image: Image.Image, crop_size: int) -> Image.Image:
    if crop_size <= 0:
        return image
    width, height = image.size
    crop = min(crop_size, width, height)
    left = (width - crop) // 2
    top = (height - crop) // 2
    return image.crop((left, top, left + crop, top + crop))


def rgb_array(rgb: bytes, width: int, height: int) -> np.ndarray:
    return np.frombuffer(rgb, dtype=np.uint8).reshape(height, width, 3).astype(np.int32)


def transform_channels(rgb: bytes, width: int, height: int, mode: str) -> list[np.ndarray]:
    arr = rgb_array(rgb, width, height)
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    if mode == "ycocg":
        co = r - b
        t = b + (co >> 1)
        cg = g - t
        y = t + (cg >> 1)
        return [y, co, cg]
    if mode == "green16":
        return [g, r - ((16 * g) >> 5), b - g]
    if mode == "g-bg-ravg":
        return [g, b - g, r - ((g + b) // 2)]
    raise ValueError(f"unknown mode {mode}")


SIGI_MODES: dict[str, tuple[str, str]] = {
    "ycocg-ctx-rice": ("ctx", "ycocg"),
    "green16-ctx-rice": ("ctx", "green16"),
    "g-bg-ravg-ctx-rice": ("ctx", "g-bg-ravg"),
    "g-bg-ravg-anova-rice": ("anova", "g-bg-ravg"),
    "ycocg-ctx-huff": ("huff", "ycocg"),
    "green16-ctx-huff": ("huff", "green16"),
    "g-bg-ravg-ctx-huff": ("huff", "g-bg-ravg"),
}


def benchmark_image(path: Path, mode_filter: str | None = None, crop_size: int = 0) -> dict[str, object]:
    with Image.open(path) as image:
        image = image.convert("RGB")
        image = center_crop(image, crop_size)
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
    webp = buf.getvalue()
    webp_s = time.perf_counter() - webp_start

    sigi_modes = SIGI_MODES if mode_filter is None else {mode_filter: SIGI_MODES[mode_filter]}
    sigi_results: dict[str, dict[str, object]] = {}
    header = sigi_header_size(rgb, width, height)
    for name, (codec, transform) in sigi_modes.items():
        start = time.perf_counter()
        channels = transform_channels(rgb, width, height, transform)
        stats: dict[str, int] | None = None
        if codec == "anova":
            payload_size, stats = anova_rice_payload_size(channels)
        elif codec == "huff":
            payload_size = context_huffman_payload_size(channels)
        else:
            payload_size = context_rice_payload_size(channels)
        elapsed = time.perf_counter() - start
        result: dict[str, object] = {
            "bytes": header + 1 + payload_size,
            "estimate_s": elapsed,
        }
        if stats is not None:
            result.update(stats)
        sigi_results[name] = result

    best_name, best = min(sigi_results.items(), key=lambda item: int(item[1]["bytes"]))
    return {
        "file": str(path),
        "crop_size": crop_size,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "source_jpeg_bytes": path.stat().st_size,
        "webp_lossless_bytes": len(webp),
        "webp_lossless_encode_s": webp_s,
        "sigi_best_mode": best_name,
        "sigi_bytes": int(best["bytes"]),
        "sigi_estimate_s": float(best["estimate_s"]),
        "sigi_modes": sigi_results,
    }


def write_report(
    rows: list[dict[str, object]],
    output: Path,
    mode_filter: str | None = None,
    crop_size: int = 0,
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# SIGI vs WebP Lossless Raw-RGB Benchmark",
        "",
        "Each JPG is decoded to RGB bytes first. WebP lossless and SIGI are measured on those exact decoded pixels.",
        "",
        "| file | dimensions | raw RGB | WebP lossless | SIGI | SIGI mode | SIGI vs WebP |",
        "|---|---:|---:|---:|---:|---|---:|",
    ]
    total_raw = total_webp = total_sigi = 0
    for row in rows:
        raw = int(row["raw_rgb_bytes"])
        webp = int(row["webp_lossless_bytes"])
        sigi_bytes = int(row["sigi_bytes"])
        total_raw += raw
        total_webp += webp
        total_sigi += sigi_bytes
        lines.append(
            f"| {Path(str(row['file'])).name} | {row['width']}x{row['height']} | "
            f"{raw:,} | {webp:,} | {sigi_bytes:,} | {row['sigi_best_mode']} | "
            f"{sigi_bytes - webp:+,} ({((sigi_bytes / webp) - 1.0) * 100.0:+.2f}%) |"
        )
    lines += [
        "",
        "## Totals",
        "",
        f"- Raw RGB bytes: `{total_raw:,}`",
        f"- WebP lossless bytes: `{total_webp:,}`",
        f"- SIGI bytes: `{total_sigi:,}`",
        f"- SIGI vs WebP lossless: `{total_sigi - total_webp:+,}` bytes "
        f"({((total_sigi / total_webp) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- SIGI sizes are exact byte counts including SIGI header, mode byte, tile headers, entropy metadata, and padding.",
        "- This fast benchmark does not emit full SIGI files; it measures size for the current estimated modes.",
    ]
    if mode_filter is not None:
        lines.append(f"- This run used only SIGI mode `{mode_filter}`.")
    if crop_size > 0:
        lines.append(f"- This run used center crops with requested size `{crop_size}`.")
    for row in rows:
        mode = row["sigi_best_mode"]
        stats = row["sigi_modes"].get(mode, {})  # type: ignore[index,union-attr]
        if "anova_tiles" in stats:
            lines.append(
                f"- `{Path(str(row['file'])).name}` ANOVA tiles: `{stats['anova_tiles']}` / "
                f"`{stats['tiles']}`, saved `{stats['anova_saved_bytes']}` payload bytes."
            )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/sigi_vs_webp_fast.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/sigi_vs_webp_fast.md"))
    parser.add_argument("--mode", choices=sorted(SIGI_MODES), default=None)
    parser.add_argument("--crop-size", type=int, default=0)
    args = parser.parse_args(argv)

    rows = []
    for path in args.images:
        print(f"benchmarking {path}...", file=sys.stderr)
        rows.append(benchmark_image(path, args.mode, args.crop_size))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(rows, args.report, args.mode, args.crop_size)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
