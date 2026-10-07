#!/usr/bin/env python3
"""Reversible local transform-stack POC for the Apex image codec.

This is the native analogue of a small VP8L-style transform command layer:

    local gauge command map
    -> reversible channel lifting per tile
    -> predictor residual planes
    -> Apex arithmetic residual tail
    -> exact inverse local gauges

The implementation is intentionally compact. It proves the round-trip contract
for per-tile reversible gauge choices while reusing the existing SIGA entropy
backend and metadata packing helpers.
"""

from __future__ import annotations

import argparse
import binascii
import io
import json
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

import apex_seeded_image_codec as apex
import benchmark_mined_strings_vs_webp as mined
import benchmark_sigi_vs_webp_fast as fast
import benchmark_subtile_transport_vs_webp as subtile
import cell_song_poc
import simplicial_image_codec as sigi


MAGIC = b"SGST"
VERSION = 2

DEFAULT_TRANSFORMS = (
    "r-gr-bg",
    "r-gr-bavg",
    "g-rg-bavg",
    "g-bg-ravg",
    "ycocg",
    "rgb",
)


@dataclass
class StackPlanes:
    residuals: list[np.ndarray]
    predictors: bytes
    energy: bytes
    unitary: bytes
    max_symbol: int
    predictor_counts: dict[str, int]


def tile_slices(width: int, height: int) -> list[tuple[slice, slice]]:
    tiles_x, tiles_y, _ = apex.tile_grid(width, height)
    slices: list[tuple[slice, slice]] = []
    for ty in range(tiles_y):
        ys = slice(ty * sigi.TILE, min((ty + 1) * sigi.TILE, height))
        for tx in range(tiles_x):
            xs = slice(tx * sigi.TILE, min((tx + 1) * sigi.TILE, width))
            slices.append((ys, xs))
    return slices


def transform_bank(rgb: bytes, width: int, height: int, transforms: tuple[str, ...]) -> dict[str, list[np.ndarray]]:
    bank: dict[str, list[np.ndarray]] = {}
    for transform in transforms:
        bank[transform] = mined.transform_channels(rgb, width, height, transform)
    return bank


def predictor_score_bits(
    channel: np.ndarray,
    left: np.ndarray,
    up: np.ndarray,
    up_left: np.ndarray,
    up_right: np.ndarray,
    left2: np.ndarray,
    up2: np.ndarray,
    contexts: np.ndarray,
    ys: slice,
    xs: slice,
) -> int:
    tile = channel[ys, xs]
    tile_contexts = contexts[ys, xs]
    best_bits: int | None = None
    for pred_id in apex.APEX_PREDICTORS:
        residual = tile - apex.predictor_tile_ext(pred_id, left, up, up_left, up_right, left2, up2, ys, xs)
        bits = fast.best_context_rice_bits(fast.zigzag_np(residual), tile_contexts)
        if best_bits is None or bits < best_bits:
            best_bits = bits
    if best_bits is None:
        raise RuntimeError("empty predictor set")
    return int(best_bits)


def transform_tile_score_vector(channels: list[np.ndarray], width: int, height: int) -> np.ndarray:
    _, _, tile_count = apex.tile_grid(width, height)
    scores = np.zeros(tile_count, dtype=np.int64)
    slices = tile_slices(width, height)
    for channel in channels:
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        left2, up2 = apex.shifted_left2_up2(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        for tile_index, (ys, xs) in enumerate(slices):
            scores[tile_index] += predictor_score_bits(
                channel,
                left,
                up,
                up_left,
                up_right,
                left2,
                up2,
                contexts,
                ys,
                xs,
            )
    return scores


def choose_tile_transforms(
    bank: dict[str, list[np.ndarray]],
    width: int,
    height: int,
    transforms: tuple[str, ...],
    command_span: int,
) -> tuple[bytes, bytes, dict[str, int]]:
    if command_span < 1:
        raise ValueError("command_span must be at least 1")
    tiles_x, tiles_y, tile_count = apex.tile_grid(width, height)
    score_vectors = {transform: transform_tile_score_vector(bank[transform], width, height) for transform in transforms}
    tile_choices = bytearray([0] * tile_count)
    command_choices = bytearray()
    counts: Counter[str] = Counter()
    for group_y in range(0, tiles_y, command_span):
        for group_x in range(0, tiles_x, command_span):
            group_indices = [
                ty * tiles_x + tx
                for ty in range(group_y, min(group_y + command_span, tiles_y))
                for tx in range(group_x, min(group_x + command_span, tiles_x))
            ]
            best_index = 0
            best_bits: int | None = None
            for index, transform in enumerate(transforms):
                score = int(score_vectors[transform][group_indices].sum())
                if best_bits is None or score < best_bits:
                    best_index = index
                    best_bits = score
            command_choices.append(best_index)
            for tile_index in group_indices:
                tile_choices[tile_index] = best_index
                counts[transforms[best_index]] += 1
    return bytes(tile_choices), bytes(command_choices), dict(counts)


def expand_command_choices(
    command_choices: bytes,
    width: int,
    height: int,
    command_span: int,
) -> bytes:
    tiles_x, tiles_y, tile_count = apex.tile_grid(width, height)
    choices = bytearray([0] * tile_count)
    offset = 0
    for group_y in range(0, tiles_y, command_span):
        for group_x in range(0, tiles_x, command_span):
            if offset >= len(command_choices):
                raise sigi.SimplicialImageError("short transform command map")
            choice = command_choices[offset]
            offset += 1
            for ty in range(group_y, min(group_y + command_span, tiles_y)):
                for tx in range(group_x, min(group_x + command_span, tiles_x)):
                    choices[ty * tiles_x + tx] = choice
    if offset != len(command_choices):
        raise sigi.SimplicialImageError("trailing transform command map entries")
    return bytes(choices)


def choose_tile_transforms_uncached(
    bank: dict[str, list[np.ndarray]],
    width: int,
    height: int,
    transforms: tuple[str, ...],
) -> tuple[bytes, dict[str, int]]:
    choices = bytearray()
    counts: Counter[str] = Counter()
    for ys, xs in tile_slices(width, height):
        best_index = 0
        best_bits: int | None = None
        for index, transform in enumerate(transforms):
            channels = bank[transform]
            score = 0
            for channel in channels:
                left, up, up_left, up_right = fast.shifted_neighbors(channel)
                left2, up2 = apex.shifted_left2_up2(channel)
                gradient = (
                    np.abs(left - up)
                    + np.abs(left - up_left)
                    + np.abs(up - up_left)
                    + np.abs(up - up_right)
                )
                contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
                score += predictor_score_bits(
                    channel,
                    left,
                    up,
                    up_left,
                    up_right,
                    left2,
                    up2,
                    contexts,
                    ys,
                    xs,
                )
            if best_bits is None or score < best_bits:
                best_index = index
                best_bits = score
        choices.append(best_index)
        counts[transforms[best_index]] += 1
    return bytes(choices), dict(counts)


def mixed_channels_from_choices(
    bank: dict[str, list[np.ndarray]],
    choices: bytes,
    width: int,
    height: int,
    transforms: tuple[str, ...],
) -> list[np.ndarray]:
    reference = next(iter(bank.values()))[0]
    mixed = [np.zeros_like(reference, dtype=np.int32) for _ in range(3)]
    for tile_index, (ys, xs) in enumerate(tile_slices(width, height)):
        channels = bank[transforms[choices[tile_index]]]
        for channel_index in range(3):
            mixed[channel_index][ys, xs] = channels[channel_index][ys, xs]
    return mixed


def build_residual_planes_from_channels(
    channels: list[np.ndarray],
    width: int,
    height: int,
    scheme: apex.Scheme,
) -> StackPlanes:
    tiles_x, tiles_y, tile_count = apex.tile_grid(width, height)
    predictor_bytes = bytearray()
    energy_bytes = bytearray()
    unitary_bytes = bytearray()
    residual_planes: list[np.ndarray] = []
    max_symbol = 0
    predictor_counts: Counter[str] = Counter()
    for channel in channels:
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        left2, up2 = apex.shifted_left2_up2(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        residuals = np.zeros_like(channel, dtype=np.int32)
        for ty in range(tiles_y):
            ys = slice(ty * sigi.TILE, min((ty + 1) * sigi.TILE, height))
            for tx in range(tiles_x):
                xs = slice(tx * sigi.TILE, min((tx + 1) * sigi.TILE, width))
                tile = channel[ys, xs]
                tile_contexts = contexts[ys, xs]
                best_pred = sigi.PRED_ZERO
                best_residual: np.ndarray | None = None
                best_bits: int | None = None
                for pred_id in apex.APEX_PREDICTORS:
                    residual = tile - apex.predictor_tile_ext(
                        pred_id,
                        left,
                        up,
                        up_left,
                        up_right,
                        left2,
                        up2,
                        ys,
                        xs,
                    )
                    bits = fast.best_context_rice_bits(fast.zigzag_np(residual), tile_contexts)
                    if best_bits is None or bits < best_bits:
                        best_pred = pred_id
                        best_residual = residual
                        best_bits = bits
                if best_residual is None:
                    raise RuntimeError("empty tile")
                predictor_bytes.append(best_pred)
                predictor_counts[f"pred-{best_pred}"] += 1
                residuals[ys, xs] = best_residual
                if scheme.use_energy:
                    energy_bytes.append(subtile.energy_class(float(np.mean(np.abs(best_residual)))))
                if scheme.use_unitary:
                    unitary_bytes.append(subtile.unitary_packet_class(best_residual))
        if predictor_bytes and len(predictor_bytes) % tile_count != 0:
            raise RuntimeError("predictor metadata misalignment")
        channel_max = int(np.max(np.abs(residuals))) if scheme.split_sign else int(np.max(fast.zigzag_np(residuals)))
        max_symbol = max(max_symbol, channel_max)
        residual_planes.append(residuals)
    return StackPlanes(
        residuals=residual_planes,
        predictors=bytes(predictor_bytes),
        energy=bytes(energy_bytes),
        unitary=bytes(unitary_bytes),
        max_symbol=max_symbol,
        predictor_counts=dict(predictor_counts),
    )


def decode_transformed_channels(
    entropy: bytes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    max_symbol: int,
    predictors: bytes,
    energy: bytes,
    unitary: bytes,
) -> list[np.ndarray]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    posterior: apex.FractionalApexPosterior | apex.BlendedApexPosterior
    if scheme.blend_parent:
        posterior = apex.BlendedApexPosterior(max_symbol, scheme.fine_weight, scheme.parent_weight)
    else:
        posterior = apex.FractionalApexPosterior(max_symbol)
    sign_counts: dict[tuple[int, ...], list[int]] = defaultdict(lambda: [1, 1])
    decoder = apex.ArithmeticDecoder(entropy)
    channels: list[np.ndarray] = []
    for channel_index in range(3):
        channel = np.zeros((height, width), dtype=np.int32)
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                ctx, grad = apex.pixel_context_and_gradient(channel, y, x)
                energy_value = energy[tile_index] if scheme.use_energy else 0
                unitary_value = unitary[tile_index] if scheme.use_unitary else 0
                key = apex.context_key(scheme, channel_index, ctx, grad, energy_value, unitary_value, y)
                if scheme.blend_parent:
                    assert isinstance(posterior, apex.BlendedApexPosterior)
                    symbol = posterior.decode_symbol(
                        decoder,
                        key,
                        apex.parent_context_key(scheme, channel_index, ctx, energy_value),
                    )
                else:
                    assert isinstance(posterior, apex.FractionalApexPosterior)
                    symbol = posterior.context(key).decode_symbol(decoder)
                pred_id = predictors[tile_index]
                if scheme.split_sign:
                    if symbol:
                        counts = sign_counts[key]
                        total = counts[0] + counts[1]
                        value = decoder.value(total)
                        sign = 0 if value < counts[0] else 1
                        low = counts[0] if sign else 0
                        high = low + counts[sign]
                        decoder.decode(low, high, total)
                        counts[sign] += 1
                        residual = -symbol if sign else symbol
                    else:
                        residual = 0
                else:
                    residual = apex.unzigzag(symbol)
                channel[y, x] = apex.predictor_value(pred_id, channel, y, x) + residual
        channels.append(channel)
    return channels


def inverse_mixed_channels(
    channels: list[np.ndarray],
    choices: bytes,
    width: int,
    height: int,
    transforms: tuple[str, ...],
) -> bytes:
    rgb = np.zeros((height, width, 3), dtype=np.uint8)
    for tile_index, (ys, xs) in enumerate(tile_slices(width, height)):
        transform = transforms[choices[tile_index]]
        tile_channels = [channel[ys, xs] for channel in channels]
        tile_bytes = apex.inverse_transform(tile_channels, transform)
        tile_h = ys.stop - ys.start
        tile_w = xs.stop - xs.start
        rgb[ys, xs, :] = np.frombuffer(tile_bytes, dtype=np.uint8).reshape(tile_h, tile_w, 3)
    return rgb.tobytes()


def encode_stack_image_bytes(
    rgb: bytes,
    width: int,
    height: int,
    scheme_id: int,
    transforms: tuple[str, ...] = DEFAULT_TRANSFORMS,
    command_span: int = 1,
) -> tuple[bytes, dict[str, object]]:
    if len(transforms) < 1 or len(transforms) > 16:
        raise ValueError("the POC stores transform commands as 4-bit indices")
    unknown = [name for name in transforms if name not in apex.TRANSFORM_IDS]
    if unknown:
        raise ValueError(f"unknown transform(s): {unknown}")

    scheme = apex.SCHEMES[scheme_id]
    select_start = time.perf_counter()
    bank = transform_bank(rgb, width, height, transforms)
    choices, command_choices, command_counts = choose_tile_transforms(bank, width, height, transforms, command_span)
    mixed = mixed_channels_from_choices(bank, choices, width, height, transforms)
    select_s = time.perf_counter() - select_start

    residual_start = time.perf_counter()
    planes = build_residual_planes_from_channels(mixed, width, height, scheme)
    residual_s = time.perf_counter() - residual_start

    entropy_start = time.perf_counter()
    entropy = apex.encode_entropy(planes, width, height, scheme)
    entropy_s = time.perf_counter() - entropy_start

    packed_choices = apex.pack_values(command_choices, 4)
    packed_predictors = apex.pack_values(planes.predictors, 5)
    packed_energy = apex.pack_values(planes.energy, 3) if planes.energy else b""
    packed_unitary = apex.pack_values(planes.unitary, 2) if planes.unitary else b""

    header = bytearray()
    header += MAGIC
    header.append(VERSION)
    header += cell_song_poc.put_varint(width)
    header += cell_song_poc.put_varint(height)
    header += int.to_bytes(binascii.crc32(rgb) & 0xFFFFFFFF, 4, "little")
    header.append(scheme_id)
    header.append(len(transforms))
    for transform in transforms:
        header.append(apex.TRANSFORM_IDS[transform])
    header += cell_song_poc.put_varint(command_span)
    header += cell_song_poc.put_varint(planes.max_symbol)
    header += cell_song_poc.put_varint(len(packed_choices))
    header += packed_choices
    header += cell_song_poc.put_varint(len(packed_predictors))
    header += packed_predictors
    header += cell_song_poc.put_varint(len(packed_energy))
    header += packed_energy
    header += cell_song_poc.put_varint(len(packed_unitary))
    header += packed_unitary

    blob = bytes(header) + entropy
    stats = {
        "codec": "SGST",
        "scheme": scheme.name,
        "transforms": list(transforms),
        "command_span": command_span,
        "bytes": len(blob),
        "header_metadata_bytes": len(header),
        "entropy_bytes": len(entropy),
        "command_metadata_bytes": len(packed_choices),
        "command_count": len(command_choices),
        "predictor_metadata_bytes": len(packed_predictors),
        "energy_metadata_bytes": len(packed_energy),
        "unitary_metadata_bytes": len(packed_unitary),
        "max_symbol": planes.max_symbol,
        "command_counts": command_counts,
        "predictors": planes.predictor_counts,
        "select_s": select_s,
        "residual_s": residual_s,
        "entropy_encode_s": entropy_s,
    }
    return blob, stats


def decode_stack_image_bytes(blob: bytes) -> tuple[bytes, int, int, dict[str, object]]:
    if not blob.startswith(MAGIC):
        raise sigi.SimplicialImageError("bad transform-stack image magic")
    offset = len(MAGIC)
    version = blob[offset]
    offset += 1
    if version != VERSION:
        raise sigi.SimplicialImageError(f"unsupported transform-stack version {version}")
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    expected_crc = int.from_bytes(blob[offset : offset + 4], "little")
    offset += 4
    scheme_id = blob[offset]
    offset += 1
    if scheme_id not in apex.SCHEMES:
        raise sigi.SimplicialImageError("bad scheme id")
    scheme = apex.SCHEMES[scheme_id]
    transform_count = blob[offset]
    offset += 1
    if transform_count < 1 or transform_count > 16:
        raise sigi.SimplicialImageError("bad transform count")
    transforms: list[str] = []
    for _ in range(transform_count):
        transform_id = blob[offset]
        offset += 1
        if transform_id not in apex.ID_TRANSFORMS:
            raise sigi.SimplicialImageError("bad transform id")
        transforms.append(apex.ID_TRANSFORMS[transform_id])
    transform_tuple = tuple(transforms)

    command_span, offset = cell_song_poc.get_varint(blob, offset)
    if command_span < 1:
        raise sigi.SimplicialImageError("bad command span")
    max_symbol, offset = cell_song_poc.get_varint(blob, offset)
    choices_len, offset = cell_song_poc.get_varint(blob, offset)
    packed_choices = blob[offset : offset + choices_len]
    offset += choices_len
    predictor_len, offset = cell_song_poc.get_varint(blob, offset)
    packed_predictors = blob[offset : offset + predictor_len]
    offset += predictor_len
    energy_len, offset = cell_song_poc.get_varint(blob, offset)
    packed_energy = blob[offset : offset + energy_len]
    offset += energy_len
    unitary_len, offset = cell_song_poc.get_varint(blob, offset)
    packed_unitary = blob[offset : offset + unitary_len]
    offset += unitary_len
    entropy = blob[offset:]

    tiles_x, tiles_y, tile_count = apex.tile_grid(width, height)
    command_count = ((tiles_x + command_span - 1) // command_span) * ((tiles_y + command_span - 1) // command_span)
    command_choices = apex.unpack_values(packed_choices, 4, command_count)
    choices = expand_command_choices(command_choices, width, height, command_span)
    if len(choices) != tile_count or any(choice >= transform_count for choice in choices):
        raise sigi.SimplicialImageError("bad transform command map")
    expected_plane_tiles = tile_count * 3
    predictors = apex.unpack_values(packed_predictors, 5, expected_plane_tiles)
    energy = apex.unpack_values(packed_energy, 3, expected_plane_tiles) if scheme.use_energy else b""
    unitary = apex.unpack_values(packed_unitary, 2, expected_plane_tiles) if scheme.use_unitary else b""
    if len(predictors) != expected_plane_tiles:
        raise sigi.SimplicialImageError("predictor metadata length mismatch")
    if scheme.use_energy and len(energy) != expected_plane_tiles:
        raise sigi.SimplicialImageError("energy metadata length mismatch")
    if scheme.use_unitary and len(unitary) != expected_plane_tiles:
        raise sigi.SimplicialImageError("unitary metadata length mismatch")

    channels = decode_transformed_channels(entropy, width, height, scheme, max_symbol, predictors, energy, unitary)
    rgb = inverse_mixed_channels(channels, choices, width, height, transform_tuple)
    actual_crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if actual_crc != expected_crc:
        raise sigi.SimplicialImageError("CRC mismatch after transform-stack decode")
    stats = {
        "codec": "SGST",
        "scheme": scheme.name,
        "transforms": list(transform_tuple),
        "width": width,
        "height": height,
        "max_symbol": max_symbol,
        "metadata_bytes": offset,
        "entropy_bytes": len(entropy),
    }
    return rgb, width, height, stats


def webp_lossless_size(rgb: bytes, width: int, height: int) -> int:
    out = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(out, format="WEBP", lossless=True, quality=100, method=6)
    return len(out.getvalue())


def benchmark_image(
    path: Path,
    crop_size: int,
    scheme_name: str,
    transforms: tuple[str, ...],
    command_span: int,
    artifact_dir: Path | None = None,
) -> dict[str, object]:
    with Image.open(path) as image:
        image = fast.center_crop(image.convert("RGB"), crop_size)
        width, height = image.size
        rgb = image.tobytes()
    scheme_id = apex.SCHEME_IDS[scheme_name]
    start = time.perf_counter()
    encoded, encode_stats = encode_stack_image_bytes(rgb, width, height, scheme_id, transforms, command_span)
    encode_s = time.perf_counter() - start
    decode_start = time.perf_counter()
    decoded, decoded_width, decoded_height, decode_stats = decode_stack_image_bytes(encoded)
    decode_s = time.perf_counter() - decode_start
    ok = decoded == rgb and decoded_width == width and decoded_height == height
    webp_size = webp_lossless_size(rgb, width, height)
    if artifact_dir is not None:
        artifact_dir.mkdir(parents=True, exist_ok=True)
        stem = path.stem.replace(" ", "_")
        encoded_path = artifact_dir / f"{stem}_{crop_size}_stack_s{command_span}.sgst"
        recovered_path = artifact_dir / f"{stem}_{crop_size}_stack_s{command_span}_recovered.png"
        encoded_path.write_bytes(encoded)
        Image.frombytes("RGB", (width, height), decoded).save(recovered_path)
    return {
        "file": str(path),
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "stack_bytes": len(encoded),
        "delta_vs_webp": len(encoded) - webp_size,
        "ratio_vs_webp": len(encoded) / webp_size,
        "roundtrip_ok": ok,
        "encode_s": encode_s,
        "decode_s": decode_s,
        "encode_stats": encode_stats,
        "decode_stats": decode_stats,
    }


def parse_transforms(value: str) -> tuple[str, ...]:
    transforms = tuple(part.strip() for part in value.split(",") if part.strip())
    if not transforms:
        raise argparse.ArgumentTypeError("at least one transform is required")
    if len(transforms) > 16:
        raise argparse.ArgumentTypeError("the POC stores at most 16 transforms")
    unknown = [name for name in transforms if name not in apex.TRANSFORM_IDS]
    if unknown:
        raise argparse.ArgumentTypeError(f"unknown transform(s): {', '.join(unknown)}")
    return transforms


def self_test() -> None:
    width = height = 32
    yy, xx = np.mgrid[0:height, 0:width]
    arr = np.stack(
        [
            (xx * 7 + yy * 3) & 255,
            (xx * 5 + yy * 11 + 17) & 255,
            (xx * yy + 23) & 255,
        ],
        axis=2,
    ).astype(np.uint8)
    rgb = arr.tobytes()
    scheme_id = apex.SCHEME_IDS["ch-ctx-energy-unitary-split-blend71-apex128"]
    encoded, _ = encode_stack_image_bytes(rgb, width, height, scheme_id)
    decoded, decoded_width, decoded_height, _ = decode_stack_image_bytes(encoded)
    if decoded != rgb or decoded_width != width or decoded_height != height:
        raise SystemExit("self-test failed")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument(
        "--scheme",
        default="ch-ctx-energy-unitary-split-blend71-apex128",
        choices=sorted(apex.SCHEME_IDS),
    )
    parser.add_argument("--transforms", type=parse_transforms, default=DEFAULT_TRANSFORMS)
    parser.add_argument(
        "--command-span",
        type=int,
        default=1,
        help="number of 32px tiles per transform-command side; 1 means per tile",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/compression/reports/transform_stack_poc.json"),
    )
    parser.add_argument("--write-artifacts", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        self_test()
        print("self-test ok")
        return 0

    rows = []
    artifact_dir = args.json.parent if args.write_artifacts else None
    for path in args.images:
        print(f"transform-stack benchmarking {path}...", file=sys.stderr)
        rows.append(
            benchmark_image(path, args.crop_size, args.scheme, args.transforms, args.command_span, artifact_dir)
        )
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"wrote {args.json}")
    for row in rows:
        print(
            f"{Path(str(row['file'])).name}: stack={row['stack_bytes']:,} "
            f"webp={row['webp_lossless_bytes']:,} "
            f"delta={row['delta_vs_webp']:+,} roundtrip={row['roundtrip_ok']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
