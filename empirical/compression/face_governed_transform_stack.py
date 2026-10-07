#!/usr/bin/env python3
"""E28 face-governed transform-stack experiment.

The E27 transform stack chose one reversible gauge per tile or per fixed grid
span. This experiment makes the command map itself boundary-aware:

    tile gauge score vectors
    -> tropical regrets / near-optimal faces
    -> Potts-smoothed command field
    -> run-length command stream
    -> existing Apex residual entropy backend

The encoded stream is intentionally close to SGST, but stores an arbitrary
tile-command map with row-major run-length coding instead of fixed spans.
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

import apex_seeded_image_codec as apex
import benchmark_sigi_vs_webp_fast as fast
import cell_song_poc
import simplicial_image_codec as sigi
import transform_stack_poc as stack


MAGIC = b"SGF8"
VERSION = 2
FLAG_LABEL_CONTEXT = 1


@dataclass(frozen=True)
class LabelField:
    labels: bytes
    lambda_bits: int
    unary_bits: int
    boundary_edges: int
    objective_bits: int
    changed_edges_by_pair: dict[str, int]
    label_counts: dict[str, int]
    face_hit_rate: float
    mean_regret_bits: float
    max_regret_bits: int
    rle_bytes: int
    rle_runs: int


def parse_int_list(value: str) -> list[int]:
    items = []
    for part in value.split(","):
        part = part.strip()
        if part:
            items.append(int(part))
    if not items:
        raise argparse.ArgumentTypeError("at least one integer is required")
    return items


def parse_transforms(value: str) -> tuple[str, ...]:
    return stack.parse_transforms(value)


def neighbor_indices(tiles_x: int, tiles_y: int) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    for ty in range(tiles_y):
        for tx in range(tiles_x):
            i = ty * tiles_x + tx
            if tx + 1 < tiles_x:
                edges.append((i, i + 1))
            if ty + 1 < tiles_y:
                edges.append((i, i + tiles_x))
    return edges


def score_matrix(
    bank: dict[str, list[np.ndarray]],
    width: int,
    height: int,
    transforms: tuple[str, ...],
) -> np.ndarray:
    vectors = []
    for transform in transforms:
        vectors.append(stack.transform_tile_score_vector(bank[transform], width, height))
    return np.stack(vectors, axis=1).astype(np.int64)


def rle_encode_choices(labels: bytes) -> bytes:
    if not labels:
        return b""
    out = bytearray()
    run_value = labels[0]
    run_len = 1
    for value in labels[1:]:
        if value == run_value:
            run_len += 1
        else:
            out += cell_song_poc.put_varint(run_len)
            out.append(run_value)
            run_value = value
            run_len = 1
    out += cell_song_poc.put_varint(run_len)
    out.append(run_value)
    return bytes(out)


def rle_decode_choices(blob: bytes, expected_count: int, transform_count: int) -> bytes:
    out = bytearray()
    offset = 0
    while offset < len(blob):
        run_len, offset = cell_song_poc.get_varint(blob, offset)
        if offset >= len(blob):
            raise sigi.SimplicialImageError("short face-governed command run")
        value = blob[offset]
        offset += 1
        if value >= transform_count:
            raise sigi.SimplicialImageError("bad face-governed transform index")
        out.extend([value] * run_len)
        if len(out) > expected_count:
            raise sigi.SimplicialImageError("face-governed command map too long")
    if len(out) != expected_count:
        raise sigi.SimplicialImageError("face-governed command map length mismatch")
    return bytes(out)


def boundary_stats(labels: np.ndarray, edges: list[tuple[int, int]], transforms: tuple[str, ...]) -> tuple[int, dict[str, int]]:
    changed = 0
    pairs: Counter[str] = Counter()
    for a, b in edges:
        la = int(labels[a])
        lb = int(labels[b])
        if la != lb:
            changed += 1
            left, right = sorted((transforms[la], transforms[lb]))
            pairs[f"{left}|{right}"] += 1
    return changed, dict(pairs)


def icm_smooth_labels(
    unary: np.ndarray,
    tiles_x: int,
    tiles_y: int,
    lambda_bits: int,
    starts: list[np.ndarray],
    max_iter: int = 30,
) -> np.ndarray:
    tile_count, transform_count = unary.shape
    neighbors: list[list[int]] = [[] for _ in range(tile_count)]
    for a, b in neighbor_indices(tiles_x, tiles_y):
        neighbors[a].append(b)
        neighbors[b].append(a)

    best_labels: np.ndarray | None = None
    best_energy: int | None = None
    orders = [
        list(range(tile_count)),
        list(reversed(range(tile_count))),
        [ty * tiles_x + tx for tx in range(tiles_x) for ty in range(tiles_y)],
    ]

    for start in starts:
        labels = start.astype(np.int16).copy()
        for _ in range(max_iter):
            changed = False
            for order in orders:
                for tile in order:
                    neighbor_labels = [int(labels[n]) for n in neighbors[tile]]
                    best_label = int(labels[tile])
                    best_local: int | None = None
                    for label in range(transform_count):
                        pair_cost = lambda_bits * sum(1 for n_label in neighbor_labels if n_label != label)
                        local = int(unary[tile, label]) + pair_cost
                        if best_local is None or local < best_local or (local == best_local and label < best_label):
                            best_local = local
                            best_label = label
                    if best_label != int(labels[tile]):
                        labels[tile] = best_label
                        changed = True
            if not changed:
                break
        energy = int(unary[np.arange(tile_count), labels].sum())
        for a, b in neighbor_indices(tiles_x, tiles_y):
            if labels[a] != labels[b]:
                energy += lambda_bits
        if best_energy is None or energy < best_energy:
            best_energy = energy
            best_labels = labels.copy()

    if best_labels is None:
        raise RuntimeError("no label field produced")
    return best_labels


def build_label_field(
    unary: np.ndarray,
    tiles_x: int,
    tiles_y: int,
    transforms: tuple[str, ...],
    lambda_bits: int,
    tau_bits: int,
) -> LabelField:
    tile_count, _ = unary.shape
    per_tile_best = unary.argmin(axis=1).astype(np.int16)
    global_best = np.full(tile_count, int(unary.sum(axis=0).argmin()), dtype=np.int16)

    starts = [per_tile_best, global_best]
    for span in (2, 4, 8):
        labels = np.zeros(tile_count, dtype=np.int16)
        for group_y in range(0, tiles_y, span):
            for group_x in range(0, tiles_x, span):
                group = [
                    ty * tiles_x + tx
                    for ty in range(group_y, min(group_y + span, tiles_y))
                    for tx in range(group_x, min(group_x + span, tiles_x))
                ]
                choice = int(unary[group, :].sum(axis=0).argmin())
                labels[group] = choice
        starts.append(labels)

    labels = icm_smooth_labels(unary, tiles_x, tiles_y, lambda_bits, starts)
    edges = neighbor_indices(tiles_x, tiles_y)
    boundary_edges, pair_counts = boundary_stats(labels, edges, transforms)
    unary_bits = int(unary[np.arange(tile_count), labels].sum())
    objective_bits = unary_bits + lambda_bits * boundary_edges

    best = unary.min(axis=1)
    regret = unary[np.arange(tile_count), labels] - best
    face_hit = regret <= tau_bits
    label_bytes = bytes(int(v) for v in labels)
    rle = rle_encode_choices(label_bytes)
    counts = Counter(transforms[int(v)] for v in labels)
    return LabelField(
        labels=label_bytes,
        lambda_bits=lambda_bits,
        unary_bits=unary_bits,
        boundary_edges=boundary_edges,
        objective_bits=objective_bits,
        changed_edges_by_pair=pair_counts,
        label_counts=dict(counts),
        face_hit_rate=float(face_hit.mean()),
        mean_regret_bits=float(regret.mean()),
        max_regret_bits=int(regret.max()),
        rle_bytes=len(rle),
        rle_runs=sum(1 for _ in iter_rle(rle)),
    )


def iter_rle(blob: bytes):
    offset = 0
    while offset < len(blob):
        run_len, offset = cell_song_poc.get_varint(blob, offset)
        if offset >= len(blob):
            break
        value = blob[offset]
        offset += 1
        yield run_len, value


def field_summary(field: LabelField) -> dict[str, object]:
    return {
        "lambda_bits": field.lambda_bits,
        "unary_bits": field.unary_bits,
        "boundary_edges": field.boundary_edges,
        "objective_bits": field.objective_bits,
        "changed_edges_by_pair": field.changed_edges_by_pair,
        "label_counts": field.label_counts,
        "face_hit_rate": field.face_hit_rate,
        "mean_regret_bits": field.mean_regret_bits,
        "max_regret_bits": field.max_regret_bits,
        "rle_bytes": field.rle_bytes,
        "rle_runs": field.rle_runs,
    }


def maybe_label_key(key: tuple[int, ...], label: int, enabled: bool) -> tuple[int, ...]:
    if not enabled:
        return key
    return (label,) + key


def encode_entropy_with_labels(
    planes: stack.StackPlanes,
    labels: bytes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    label_context: bool,
) -> bytes:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    if len(labels) != tile_count:
        raise ValueError("label map length mismatch")
    if scheme.blend_parent:
        posterior: apex.FractionalApexPosterior | apex.BlendedApexPosterior = apex.BlendedApexPosterior(
            planes.max_symbol,
            scheme.fine_weight,
            scheme.parent_weight,
        )
    else:
        posterior = apex.FractionalApexPosterior(planes.max_symbol)
    sign_counts: dict[tuple[int, ...], list[int]] = {}
    coder = apex.ArithmeticEncoder()
    for channel_index, residuals in enumerate(planes.residuals):
        decoded_prefix = np.zeros((height, width), dtype=np.int32)
        for y in range(height):
            for x in range(width):
                base_tile = (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                tile_index = channel_index * tile_count + base_tile
                label = labels[base_tile]
                pred_id = planes.predictors[tile_index]
                ctx, grad = apex.pixel_context_and_gradient(decoded_prefix, y, x)
                prediction = apex.predictor_value(pred_id, decoded_prefix, y, x)
                decoded_prefix[y, x] = prediction + int(residuals[y, x])
                energy = planes.energy[tile_index] if scheme.use_energy else 0
                unitary = planes.unitary[tile_index] if scheme.use_unitary else 0
                base_key = apex.context_key(scheme, channel_index, ctx, grad, energy, unitary, y)
                key = maybe_label_key(base_key, label, label_context)
                residual_value = int(residuals[y, x])
                symbol = abs(residual_value) if scheme.split_sign else sigi.zigzag(residual_value)
                if scheme.blend_parent:
                    assert isinstance(posterior, apex.BlendedApexPosterior)
                    # Keep the parent ungated by label so sparse face labels borrow
                    # mass from the global channel/context model.
                    posterior.encode_symbol(coder, key, apex.parent_context_key(scheme, channel_index, ctx, energy), symbol)
                else:
                    assert isinstance(posterior, apex.FractionalApexPosterior)
                    posterior.context(key).encode_symbol(coder, symbol)
                if scheme.split_sign and symbol:
                    counts = sign_counts.setdefault(key, [1, 1])
                    sign = 1 if residual_value < 0 else 0
                    total = counts[0] + counts[1]
                    low = counts[0] if sign else 0
                    high = low + counts[sign]
                    coder.encode(low, high, total)
                    counts[sign] += 1
    return coder.finish()


def decode_transformed_channels_with_labels(
    entropy: bytes,
    labels: bytes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    max_symbol: int,
    predictors: bytes,
    energy: bytes,
    unitary: bytes,
    label_context: bool,
) -> list[np.ndarray]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    if len(labels) != tile_count:
        raise ValueError("label map length mismatch")
    if scheme.blend_parent:
        posterior: apex.FractionalApexPosterior | apex.BlendedApexPosterior = apex.BlendedApexPosterior(
            max_symbol,
            scheme.fine_weight,
            scheme.parent_weight,
        )
    else:
        posterior = apex.FractionalApexPosterior(max_symbol)
    sign_counts: dict[tuple[int, ...], list[int]] = {}
    decoder = apex.ArithmeticDecoder(entropy)
    channels: list[np.ndarray] = []
    for channel_index in range(3):
        channel = np.zeros((height, width), dtype=np.int32)
        for y in range(height):
            for x in range(width):
                base_tile = (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                tile_index = channel_index * tile_count + base_tile
                label = labels[base_tile]
                ctx, grad = apex.pixel_context_and_gradient(channel, y, x)
                energy_value = energy[tile_index] if scheme.use_energy else 0
                unitary_value = unitary[tile_index] if scheme.use_unitary else 0
                base_key = apex.context_key(scheme, channel_index, ctx, grad, energy_value, unitary_value, y)
                key = maybe_label_key(base_key, label, label_context)
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
                        counts = sign_counts.setdefault(key, [1, 1])
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


def encode_face_image_bytes(
    rgb: bytes,
    width: int,
    height: int,
    scheme_id: int,
    transforms: tuple[str, ...],
    bank: dict[str, list[np.ndarray]],
    labels: bytes,
    label_context: bool = False,
) -> tuple[bytes, dict[str, object]]:
    if len(transforms) < 1 or len(transforms) > 16:
        raise ValueError("the experiment stores transform indices in one byte but keeps the SGST <=16 contract")
    if any(name not in apex.TRANSFORM_IDS for name in transforms):
        raise ValueError("unknown transform")

    scheme = apex.SCHEMES[scheme_id]
    _, _, tile_count = apex.tile_grid(width, height)
    if len(labels) != tile_count:
        raise ValueError("label map length mismatch")

    residual_start = time.perf_counter()
    mixed = stack.mixed_channels_from_choices(bank, labels, width, height, transforms)
    planes = stack.build_residual_planes_from_channels(mixed, width, height, scheme)
    residual_s = time.perf_counter() - residual_start

    entropy_start = time.per_counter() if False else time.perf_counter()
    entropy = encode_entropy_with_labels(planes, labels, width, height, scheme, label_context)
    entropy_s = time.perf_counter() - entropy_start

    rle_choices = rle_encode_choices(labels)
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
    header.append(FLAG_LABEL_CONTEXT if label_context else 0)
    header += cell_song_poc.put_varint(planes.max_symbol)
    header += cell_song_poc.put_varint(len(rle_choices))
    header += rle_choices
    header += cell_song_poc.put_varint(len(packed_predictors))
    header += packed_predictors
    header += cell_song_poc.put_varint(len(packed_energy))
    header += packed_energy
    header += cell_song_poc.put_varint(len(packed_unitary))
    header += packed_unitary

    blob = bytes(header) + entropy
    return blob, {
        "codec": "SGF8",
        "scheme": scheme.name,
        "label_context": label_context,
        "transforms": list(transforms),
        "bytes": len(blob),
        "header_metadata_bytes": len(header),
        "entropy_bytes": len(entropy),
        "command_rle_bytes": len(rle_choices),
        "command_rle_runs": sum(1 for _ in iter_rle(rle_choices)),
        "predictor_metadata_bytes": len(packed_predictors),
        "energy_metadata_bytes": len(packed_energy),
        "unitary_metadata_bytes": len(packed_unitary),
        "max_symbol": planes.max_symbol,
        "predictors": planes.predictor_counts,
        "residual_s": residual_s,
        "entropy_encode_s": entropy_s,
    }


def decode_face_image_bytes(blob: bytes) -> tuple[bytes, int, int, dict[str, object]]:
    if not blob.startswith(MAGIC):
        raise sigi.SimplicialImageError("bad face-governed stack magic")
    offset = len(MAGIC)
    version = blob[offset]
    offset += 1
    if version not in (1, VERSION):
        raise sigi.SimplicialImageError(f"unsupported face-governed stack version {version}")
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
    transforms: list[str] = []
    for _ in range(transform_count):
        transform_id = blob[offset]
        offset += 1
        if transform_id not in apex.ID_TRANSFORMS:
            raise sigi.SimplicialImageError("bad transform id")
        transforms.append(apex.ID_TRANSFORMS[transform_id])
    flags = 0
    if version >= 2:
        flags = blob[offset]
        offset += 1
    label_context = bool(flags & FLAG_LABEL_CONTEXT)
    max_symbol, offset = cell_song_poc.get_varint(blob, offset)
    rle_len, offset = cell_song_poc.get_varint(blob, offset)
    rle_choices = blob[offset : offset + rle_len]
    offset += rle_len

    tiles_x, _, tile_count = apex.tile_grid(width, height)
    choices = rle_decode_choices(rle_choices, tile_count, transform_count)

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

    expected_plane_tiles = tile_count * 3
    predictors = apex.unpack_values(packed_predictors, 5, expected_plane_tiles)
    energy = apex.unpack_values(packed_energy, 3, expected_plane_tiles) if scheme.use_energy else b""
    unitary = apex.unpack_values(packed_unitary, 2, expected_plane_tiles) if scheme.use_unitary else b""
    channels = decode_transformed_channels_with_labels(
        entropy,
        choices,
        width,
        height,
        scheme,
        max_symbol,
        predictors,
        energy,
        unitary,
        label_context,
    )
    rgb = stack.inverse_mixed_channels(channels, choices, width, height, tuple(transforms))
    actual_crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if actual_crc != expected_crc:
        raise sigi.SimplicialImageError("CRC mismatch after face-governed decode")
    return rgb, width, height, {
        "codec": "SGF8",
        "scheme": scheme.name,
        "label_context": label_context,
        "transforms": transforms,
        "width": width,
        "height": height,
        "max_symbol": max_symbol,
        "metadata_bytes": offset,
        "entropy_bytes": len(entropy),
        "command_rle_bytes": len(rle_choices),
    }


def webp_lossless_size(rgb: bytes, width: int, height: int) -> int:
    out = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(out, format="WEBP", lossless=True, quality=100, method=6)
    return len(out.getvalue())


def benchmark_image(
    path: Path,
    crop_size: int,
    scheme_name: str,
    transforms: tuple[str, ...],
    lambdas: list[int],
    tau_bits: int,
    encode_top: int,
    label_context: bool,
    artifact_dir: Path | None,
) -> dict[str, object]:
    with Image.open(path) as image:
        image = fast.center_crop(image.convert("RGB"), crop_size)
        width, height = image.size
        rgb = image.tobytes()
    tiles_x, tiles_y, tile_count = apex.tile_grid(width, height)
    scheme_id = apex.SCHEME_IDS[scheme_name]

    select_start = time.perf_counter()
    bank = stack.transform_bank(rgb, width, height, transforms)
    unary = score_matrix(bank, width, height, transforms)
    fields = [
        build_label_field(unary, tiles_x, tiles_y, transforms, lambda_bits=value, tau_bits=tau_bits)
        for value in lambdas
    ]
    # Deduplicate identical command fields, preserving the best objective label.
    unique: dict[bytes, LabelField] = {}
    for field in fields:
        prior = unique.get(field.labels)
        if prior is None or field.objective_bits < prior.objective_bits:
            unique[field.labels] = field
    ranked = sorted(unique.values(), key=lambda f: (f.unary_bits + 8 * f.rle_bytes, f.boundary_edges, f.lambda_bits))
    select_s = time.perf_counter() - select_start

    if artifact_dir is not None:
        artifact_dir.mkdir(parents=True, exist_ok=True)

    webp_size = webp_lossless_size(rgb, width, height)
    encoded_rows = []
    for rank, field in enumerate(ranked[:encode_top], start=1):
        encode_start = time.perf_counter()
        blob, encode_stats = encode_face_image_bytes(
            rgb,
            width,
            height,
            scheme_id,
            transforms,
            bank,
            field.labels,
            label_context=label_context,
        )
        encode_s = time.perf_counter() - encode_start
        decode_start = time.perf_counter()
        decoded, decoded_width, decoded_height, decode_stats = decode_face_image_bytes(blob)
        decode_s = time.perf_counter() - decode_start
        ok = decoded == rgb and decoded_width == width and decoded_height == height
        if artifact_dir is not None:
            stem = path.stem.replace(" ", "_")
            encoded_path = artifact_dir / f"{stem}_{crop_size}_face_gov_l{field.lambda_bits}.sgf8"
            recovered_path = artifact_dir / f"{stem}_{crop_size}_face_gov_l{field.lambda_bits}_recovered.png"
            labels_path = artifact_dir / f"{stem}_{crop_size}_face_gov_l{field.lambda_bits}_labels.json"
            encoded_path.write_bytes(blob)
            Image.frombytes("RGB", (width, height), decoded).save(recovered_path)
            labels_grid = np.frombuffer(field.labels, dtype=np.uint8).reshape(tiles_y, tiles_x).tolist()
            labels_path.write_text(json.dumps(labels_grid, indent=2), encoding="utf-8")
        encoded_rows.append(
            {
                "rank": rank,
                "lambda_bits": field.lambda_bits,
                "bytes": len(blob),
                "delta_vs_webp": len(blob) - webp_size,
                "ratio_vs_webp": len(blob) / webp_size,
                "roundtrip_ok": ok,
                "encode_s": encode_s,
                "decode_s": decode_s,
                "field": field_summary(field),
                "encode_stats": encode_stats,
                "decode_stats": decode_stats,
            }
        )

    return {
        "file": str(path),
        "width": width,
        "height": height,
        "tile_count": tile_count,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "scheme": scheme_name,
        "transforms": list(transforms),
        "tau_bits": tau_bits,
        "label_context": label_context,
        "lambdas": lambdas,
        "selection_s": select_s,
        "selection_fields": [field_summary(field) for field in fields],
        "encoded": encoded_rows,
    }


def write_report(json_path: Path, report_path: Path) -> None:
    rows = json.loads(json_path.read_text(encoding="utf-8"))
    lines = [
        "# E28 Face-Governed Transform Stack",
        "",
        "This experiment tests the Pe-series reading of the compression stack: a local gauge command map is a face/boundary object, not inert metadata.",
        "",
    ]
    for row in rows:
        lines += [
            f"## {Path(row['file']).name}",
            "",
            f"- crop: {row['width']}x{row['height']} RGB",
            f"- WebP lossless baseline: `{row['webp_lossless_bytes']:,}` bytes",
            f"- transforms: `{', '.join(row['transforms'])}`",
            f"- tropical face threshold: `{row['tau_bits']}` bits",
            f"- command-label posterior context: `{row.get('label_context', False)}`",
            f"- selection time: `{row['selection_s']:.2f}` s",
            "",
            "| rank | lambda bits | bytes | vs WebP | boundary edges | RLE bytes | face hit | mean regret | labels | roundtrip |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
        ]
        for encoded in row["encoded"]:
            field = encoded["field"]
            counts = ", ".join(f"{k}:{v}" for k, v in sorted(field["label_counts"].items()))
            lines.append(
                f"| {encoded['rank']} | {encoded['lambda_bits']} | {encoded['bytes']:,} | "
                f"{encoded['delta_vs_webp']:+,} | {field['boundary_edges']} | {field['rle_bytes']} | "
                f"{field['face_hit_rate']:.3f} | {field['mean_regret_bits']:.2f} | {counts} | "
                f"{encoded['roundtrip_ok']} |"
            )
        lines += [
            "",
            "## Interpretation",
            "",
            "E28 prices the exterior boundary explicitly. Per-tile scores are first converted to tropical regrets; the near-minimal gauges form a local face. The deployed command field is then selected by trading unary residual score against gauge-boundary crossings.",
            "",
            "A pass is not only a byte win. A strong joint-on-disjoint result is also informative: if boundary governance produces smoother, auditable face maps but the exact byte stream still loses, then the face labels should drive priors or reference mining rather than be transmitted directly as a command map.",
            "",
        ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--scheme", default="ch-ctx-energy-unitary-split-blend71-apex128", choices=sorted(apex.SCHEME_IDS))
    parser.add_argument("--transforms", type=parse_transforms, default=stack.DEFAULT_TRANSFORMS)
    parser.add_argument("--lambdas", type=parse_int_list, default=[0, 8, 16, 32, 64, 128, 256])
    parser.add_argument("--tau-bits", type=int, default=16)
    parser.add_argument("--encode-top", type=int, default=4)
    parser.add_argument("--label-context", action="store_true")
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/e28_face_governed_transform_stack.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/e28_face_governed_transform_stack.md"))
    parser.add_argument("--write-artifacts", action="store_true")
    args = parser.parse_args(argv)

    rows = []
    artifact_dir = args.json.parent if args.write_artifacts else None
    for path in args.images:
        print(f"E28 face-governed benchmarking {path}...", file=sys.stderr)
        rows.append(
            benchmark_image(
                path=path,
                crop_size=args.crop_size,
                scheme_name=args.scheme,
                transforms=args.transforms,
                lambdas=args.lambdas,
                tau_bits=args.tau_bits,
                encode_top=args.encode_top,
                label_context=args.label_context,
                artifact_dir=artifact_dir,
            )
        )
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(args.json, args.report)
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for row in rows:
        best = min(row["encoded"], key=lambda item: item["bytes"]) if row["encoded"] else None
        if best is not None:
            print(
                f"{Path(row['file']).name}: best SGF8={best['bytes']:,} "
                f"webp={row['webp_lossless_bytes']:,} "
                f"delta={best['delta_vs_webp']:+,} lambda={best['lambda_bits']} "
                f"roundtrip={best['roundtrip_ok']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
