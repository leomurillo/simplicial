#!/usr/bin/env python3
"""Benchmark native lossless image-compression experiments on RGB pixels.

This is intentionally not a JPEG recompression test. It decodes source images
to RGB pixels and then compares exact lossless encodings of those pixels:

- PNG, via Pillow, as the serious lossless-image baseline;
- SIGI, our native predictive-gauge + Rice entropy image codec;
- HCS raw RGB bytes;
- HCS planar RGB bytes;
- HCS planar left-residual bytes, a tiny image-specific reversible transform.
"""

from __future__ import annotations

import argparse
import gzip
import io
import json
import statistics
import sys
import time
from pathlib import Path

import cell_song_poc
import cell_song_image2d_poc
import simplicial_image_codec


DEFAULT_IMAGES = [
    Path(r"C:\Users\leomu\OneDrive\Pictures\133925289798805247.jpg"),
    Path(r"C:\Users\leomu\OneDrive\Pictures\133893333653186297.jpg"),
    Path(r"C:\Users\leomu\OneDrive\Pictures\133921439458600606.jpg"),
]


def require_pillow():
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit(
            "Pillow is required for image benchmarks. Use a venv and run "
            "`python -m pip install pillow`."
        ) from exc
    return Image


def put_varint(value: int) -> bytes:
    return cell_song_poc.put_varint(value)


def image_container(width: int, height: int, transform: int, payload: bytes) -> bytes:
    return b"IHCS0" + put_varint(width) + put_varint(height) + bytes([transform]) + payload


def planar_rgb(rgb: bytes, width: int, height: int) -> bytes:
    n = width * height
    out = bytearray(len(rgb))
    pos = 0
    for c in range(3):
        for i in range(n):
            out[pos] = rgb[3 * i + c]
            pos += 1
    return bytes(out)


def unplanar_rgb(planar: bytes, width: int, height: int) -> bytes:
    n = width * height
    out = bytearray(len(planar))
    for c in range(3):
        plane = planar[c * n : (c + 1) * n]
        for i, value in enumerate(plane):
            out[3 * i + c] = value
    return bytes(out)


def planar_left_residual(rgb: bytes, width: int, height: int) -> bytes:
    out = bytearray()
    for c in range(3):
        for y in range(height):
            prev = 0
            row = y * width
            for x in range(width):
                value = rgb[3 * (row + x) + c]
                out.append((value - prev) & 0xFF)
                prev = value
    return bytes(out)


def inverse_planar_left_residual(residual: bytes, width: int, height: int) -> bytes:
    n = width * height
    out = bytearray(3 * n)
    pos = 0
    for c in range(3):
        for y in range(height):
            prev = 0
            row = y * width
            for x in range(width):
                residual_byte = residual[pos]
                pos += 1
                value = (prev + residual_byte) & 0xFF
                out[3 * (row + x) + c] = value
                prev = value
    return bytes(out)


def time_call(fn, min_seconds: float = 0.15, min_rounds: int = 3) -> tuple[float, int]:
    values: list[float] = []
    total = 0.0
    rounds = 0
    while rounds < min_rounds or total < min_seconds:
        start = time.perf_counter()
        fn()
        elapsed = time.perf_counter() - start
        values.append(elapsed)
        total += elapsed
        rounds += 1
        if rounds >= 100:
            break
    return statistics.median(values), rounds


def fmt_seconds(value: float) -> str:
    if value < 0.001:
        return f"{value * 1_000_000:.0f} us"
    if value < 1:
        return f"{value * 1000:.2f} ms"
    return f"{value:.2f} s"


def png_encode_decode(Image, rgb: bytes, width: int, height: int) -> tuple[bytes, float]:
    image = Image.frombytes("RGB", (width, height), rgb)
    start = time.perf_counter()
    buf = io.BytesIO()
    image.save(buf, format="PNG", optimize=True, compress_level=9)
    encoded = buf.getvalue()
    encode_s = time.perf_counter() - start
    return encoded, encode_s


def png_decode(Image, blob: bytes) -> bytes:
    with Image.open(io.BytesIO(blob)) as image:
        return image.convert("RGB").tobytes()


def webp_encode_decode(Image, rgb: bytes, width: int, height: int) -> tuple[bytes | None, float | None]:
    image = Image.frombytes("RGB", (width, height), rgb)
    start = time.perf_counter()
    buf = io.BytesIO()
    try:
        image.save(buf, format="WEBP", lossless=True, quality=100, method=6)
    except Exception:
        return None, None
    return buf.getvalue(), time.perf_counter() - start


def webp_decode(Image, blob: bytes) -> bytes:
    with Image.open(io.BytesIO(blob)) as image:
        return image.convert("RGB").tobytes()


def center_crop(image, crop_size: int):
    if crop_size <= 0:
        return image
    width, height = image.size
    size = min(crop_size, width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    return image.crop((left, top, left + size, top + size))


def bench_image(path: Path, block_size: int, crop_size: int, include_hcs2d: bool) -> dict[str, object]:
    Image = require_pillow()
    with Image.open(path) as image:
        rgb_image = image.convert("RGB")
        original_width, original_height = rgb_image.size
        rgb_image = center_crop(rgb_image, crop_size)
        width, height = rgb_image.size
        rgb = rgb_image.tobytes()

    png_blob, png_encode_s = png_encode_decode(Image, rgb, width, height)
    png_decode_s, _ = time_call(lambda: png_decode(Image, png_blob))
    if png_decode(Image, png_blob) != rgb:
        raise RuntimeError(f"PNG round trip failed: {path}")

    webp_blob, webp_encode_s = webp_encode_decode(Image, rgb, width, height)
    webp_decode_s = None
    if webp_blob is not None:
        webp_decode_s, _ = time_call(lambda: webp_decode(Image, webp_blob))
        if webp_decode(Image, webp_blob) != rgb:
            raise RuntimeError(f"WebP lossless round trip failed: {path}")

    gzip_start = time.perf_counter()
    gzip_blob = gzip.compress(rgb, compresslevel=9, mtime=0)
    gzip_encode_s = time.perf_counter() - gzip_start
    gzip_decode_s, _ = time_call(lambda: gzip.decompress(gzip_blob))

    sigi_start = time.perf_counter()
    sigi_blob = simplicial_image_codec.compress_rgb(rgb, width, height)
    sigi_encode_s = time.perf_counter() - sigi_start

    def decode_sigi() -> bytes:
        decoded, decoded_width, decoded_height = simplicial_image_codec.decompress_rgb(sigi_blob)
        if decoded_width != width or decoded_height != height:
            raise RuntimeError("SIGI dimensions changed")
        return decoded

    if decode_sigi() != rgb:
        raise RuntimeError(f"SIGI round trip failed: {path}")
    sigi_decode_s, _ = time_call(decode_sigi)

    variants = {}
    transforms = {
        "hcs_rgb": (0, rgb, lambda data: data),
        "hcs_planar": (
            1,
            planar_rgb(rgb, width, height),
            lambda data: unplanar_rgb(data, width, height),
        ),
        "hcs_left_residual": (
            2,
            planar_left_residual(rgb, width, height),
            lambda data: inverse_planar_left_residual(data, width, height),
        ),
    }

    for name, (transform_id, transformed, inverse) in transforms.items():
        start = time.perf_counter()
        payload = cell_song_poc.compress_bytes(transformed, block_size=block_size)
        encoded = image_container(width, height, transform_id, payload)
        encode_s = time.perf_counter() - start

        def decode_variant() -> bytes:
            # Strip image header in this benchmark container.
            offset = len(b"IHCS0")
            _w, offset = cell_song_poc.get_varint(encoded, offset)
            _h, offset = cell_song_poc.get_varint(encoded, offset)
            _transform = encoded[offset]
            payload2 = encoded[offset + 1 :]
            transformed2 = cell_song_poc.decompress_bytes(payload2)
            return inverse(transformed2)

        if decode_variant() != rgb:
            raise RuntimeError(f"{name} round trip failed: {path}")
        decode_s, _ = time_call(decode_variant)
        variants[name] = {
            "bytes": len(encoded),
            "encode_s": encode_s,
            "decode_s": decode_s,
        }

    hcs2d_bytes = None
    hcs2d_encode_s = None
    hcs2d_decode_s = None
    raw_2d_blocks = None
    song_2d_blocks = None
    if include_hcs2d:
        start = time.perf_counter()
        hcs2d_blob = cell_song_image2d_poc.compress_rgb(rgb, width, height)
        hcs2d_encode_s = time.perf_counter() - start
        raw_2d_blocks, song_2d_blocks = cell_song_image2d_poc.stats(hcs2d_blob)

        def decode_hcs2d() -> bytes:
            decoded, decoded_width, decoded_height = cell_song_image2d_poc.decompress_rgb(hcs2d_blob)
            if decoded_width != width or decoded_height != height:
                raise RuntimeError("HCS2D dimensions changed")
            return decoded

        if decode_hcs2d() != rgb:
            raise RuntimeError(f"HCS2D round trip failed: {path}")
        hcs2d_decode_s, _ = time_call(decode_hcs2d)
        hcs2d_bytes = len(hcs2d_blob)

    return {
        "file": str(path),
        "original_width": original_width,
        "original_height": original_height,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "source_jpeg_bytes": path.stat().st_size,
        "png_bytes": len(png_blob),
        "png_encode_s": png_encode_s,
        "png_decode_s": png_decode_s,
        "webp_lossless_bytes": len(webp_blob) if webp_blob is not None else None,
        "webp_lossless_encode_s": webp_encode_s,
        "webp_lossless_decode_s": webp_decode_s,
        "gzip_rgb_bytes": len(gzip_blob),
        "gzip_rgb_encode_s": gzip_encode_s,
        "gzip_rgb_decode_s": gzip_decode_s,
        "sigi_bytes": len(sigi_blob),
        "sigi_mode": simplicial_image_codec.mode_name(sigi_blob),
        "sigi_encode_s": sigi_encode_s,
        "sigi_decode_s": sigi_decode_s,
        "hcs2d_bytes": hcs2d_bytes,
        "hcs2d_encode_s": hcs2d_encode_s,
        "hcs2d_decode_s": hcs2d_decode_s,
        "hcs2d_raw_blocks": raw_2d_blocks,
        "hcs2d_song_blocks": song_2d_blocks,
        **variants,
    }


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Native Lossless Image Benchmark",
        "",
        "Input images are decoded to exact RGB pixels first. Sizes below are lossless encodings of those decoded pixels.",
        "",
        "| file | pixels | raw RGB | PNG | WebP lossless | gzip RGB | SIGI | SIGI mode | SIGI decode | HCS1D residual | HCS2D |",
        "|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    total_raw = total_png = total_webp = total_gzip = total_sigi = total_hcs = total_hcs2d = 0
    webp_available = True
    any_hcs2d = False
    for row in rows:
        name = Path(str(row["file"])).name
        pixels = int(row["width"]) * int(row["height"])
        raw = int(row["raw_rgb_bytes"])
        png = int(row["png_bytes"])
        webp_value = row["webp_lossless_bytes"]
        gzip_size = int(row["gzip_rgb_bytes"])
        sigi = int(row["sigi_bytes"])
        hcs_residual = int(row["hcs_left_residual"]["bytes"])  # type: ignore[index]
        hcs2d_value = row["hcs2d_bytes"]
        total_raw += raw
        total_png += png
        webp_text = "n/a"
        if webp_value is None:
            webp_available = False
        else:
            webp_size = int(webp_value)
            total_webp += webp_size
            webp_text = f"{webp_size:,}"
        total_gzip += gzip_size
        total_sigi += sigi
        total_hcs += hcs_residual
        hcs2d_text = "skipped"
        if hcs2d_value is not None:
            any_hcs2d = True
            hcs2d = int(hcs2d_value)
            total_hcs2d += hcs2d
            raw_blocks = int(row["hcs2d_raw_blocks"])
            song_blocks = int(row["hcs2d_song_blocks"])
            hcs2d_text = f"{hcs2d:,} ({song_blocks:,}/{raw_blocks + song_blocks:,} songs)"
        lines.append(
            "| "
            f"{name} | {pixels:,} | {raw:,} | {png:,} | "
            f"{webp_text} | "
            f"{gzip_size:,} | "
            f"{sigi:,} | "
            f"{row['sigi_mode']} | "
            f"{fmt_seconds(float(row['sigi_decode_s']))} | "
            f"{hcs_residual:,} | "
            f"{hcs2d_text} |"
        )

    lines += [
        "",
        "## Totals",
        "",
        f"- Raw RGB bytes: `{total_raw:,}`",
        f"- PNG bytes: `{total_png:,}`",
        f"- WebP lossless bytes: `{total_webp:,}`" if webp_available else "- WebP lossless bytes: `n/a`",
        f"- gzip RGB bytes: `{total_gzip:,}`",
        f"- SIGI bytes: `{total_sigi:,}`",
        f"- SIGI vs gzip RGB: `{total_sigi - total_gzip:+,}` bytes "
        f"({((total_sigi / total_gzip) - 1.0) * 100.0:+.2f}%)",
        f"- SIGI vs PNG: `{total_sigi - total_png:+,}` bytes "
        f"({((total_sigi / total_png) - 1.0) * 100.0:+.2f}%)",
        f"- SIGI vs WebP lossless: `{total_sigi - total_webp:+,}` bytes "
        f"({((total_sigi / total_webp) - 1.0) * 100.0:+.2f}%)"
        if webp_available
        else "- SIGI vs WebP lossless: `n/a`",
        f"- HCS residual bytes: `{total_hcs:,}`",
        f"- HCS residual vs PNG: `{total_hcs - total_png:+,}` bytes "
        f"({((total_hcs / total_png) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- By default this benchmark uses a center crop to keep the POC runtime reasonable. Pass `--crop-size 0` for full decoded images.",
        "- `WebP lossless` is encoded through Pillow/libwebp when available.",
        "- `SIGI` is the native predictive-gauge image codec: reversible color transform, local predictor choice, and Rice entropy coding.",
        "- `HCS1D residual` is planar RGB with a reversible left-prediction byte residual, then the 1D rounding-cell song POC.",
    ]
    if any_hcs2d:
        lines += [
            f"- HCS2D bytes: `{total_hcs2d:,}`",
            f"- HCS2D vs PNG: `{total_hcs2d - total_png:+,}` bytes "
            f"({((total_hcs2d / total_png) - 1.0) * 100.0:+.2f}%)",
            "- `HCS2D` uses sparse 8x8 2D Haar/polynomial songs per color plane, accepted only when the song floors back to the exact original pixels.",
        ]
    else:
        lines.append("- `HCS2D` was skipped here because the interval-song compressor is currently much slower than the predictive codec.")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Benchmark cell-song POC on images")
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--block-size", type=int, default=64)
    parser.add_argument(
        "--crop-size",
        type=int,
        default=512,
        help="center-crop square size before lossless benchmarking; use 0 for full image",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/compression/reports/cell_song_images.json"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/compression/reports/cell_song_images.md"),
    )
    parser.add_argument(
        "--include-hcs2d",
        action="store_true",
        help="also run the slow 2D interval-song image codec",
    )
    args = parser.parse_args(argv)

    paths = args.images or DEFAULT_IMAGES
    rows = []
    for path in paths:
        print(f"benchmarking {path}...", file=sys.stderr)
        rows.append(bench_image(path, args.block_size, args.crop_size, args.include_hcs2d))

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(rows, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
