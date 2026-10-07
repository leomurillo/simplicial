#!/usr/bin/env python3
"""E30 causal moment-barrier gate for the Apex image codec.

P6 says finite-prime structure cannot simply smooth-complete itself: a negative
Hankel determinant is a real barrier. E30 turns that into a no-payload codec
test. For each channel, the decoder already knows the previous residual
magnitudes. We form the local Hankel determinant

    det [[b0,b1,b2],[b1,b2,b3],[b2,b3,b4]]

from the last five decoded magnitudes. If it is negative, the stream is routed
through a "barrier" prior; if non-negative, through a smoother zero-biased
prior. No gate bits are transmitted.
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
import e29_ramanujan_transfer_prior as e29
import simplicial_image_codec as sigi


MAGIC = b"SM30"
VERSION = 1

MODEL_BASELINE = 0
MODEL_HARD_CONTEXT = 1
MODEL_SOFT_MOMENT = 2
MODEL_INVERTED_MOMENT = 3

MODEL_NAMES = {
    MODEL_BASELINE: "baseline",
    MODEL_HARD_CONTEXT: "hard-moment-context",
    MODEL_SOFT_MOMENT: "soft-moment-prior",
    MODEL_INVERTED_MOMENT: "inverted-moment-prior",
}
NAME_MODELS = {value: key for key, value in MODEL_NAMES.items()}


@dataclass(frozen=True)
class MomentConfig:
    model_id: int
    mix_num: int
    mix_den: int


def hankel_d2(values: list[int]) -> int:
    """3x3 Hankel determinant from the five most recent magnitudes."""
    a0, a1, a2, a3, a4 = values[-5:]
    return (
        a0 * (a2 * a4 - a3 * a3)
        - a1 * (a1 * a4 - a2 * a3)
        + a2 * (a1 * a3 - a2 * a2)
    )


def moment_class(history: list[int]) -> int:
    if len(history) < 5:
        return 0
    return 2 if hankel_d2(history) < 0 else 1


def normalize_prefix(masses: list[int], denominator: int = apex.PRIOR_DENOMINATOR) -> list[int]:
    total = sum(masses)
    if total <= 0:
        raise ValueError("empty mass table")
    prefix = [0]
    running = 0
    for mass in masses:
        running += mass
        value = round(denominator * running / total)
        prefix.append(max(prefix[-1] + 1, min(denominator, int(value))))
    prefix[-1] = denominator
    return prefix


class MomentPriorTable:
    def __init__(self, max_symbol: int, mix_num: int, mix_den: int, inverted: bool = False) -> None:
        if mix_num < 0 or mix_den <= 0 or mix_num > mix_den:
            raise ValueError("mix must satisfy 0 <= mix_num <= mix_den")
        self.max_symbol = max_symbol
        self.mix_num = mix_num
        self.mix_den = mix_den
        base_prefix = apex.apex_prior_prefix(max_symbol)
        base = [base_prefix[i + 1] - base_prefix[i] for i in range(max_symbol + 1)]
        # Smooth: more weight near zero. Barrier: heavier tail. Both are mixed
        # back into the native Apex prior so the test is conservative.
        smooth_raw = [max(1, base[s] * (max_symbol + 1 - s)) for s in range(max_symbol + 1)]
        barrier_raw = [max(1, base[s] * (s + 1)) for s in range(max_symbol + 1)]
        smooth = self._mix(base, smooth_raw)
        barrier = self._mix(base, barrier_raw)
        if inverted:
            smooth, barrier = barrier, smooth
        self.base_prefix = base_prefix
        self.smooth_prefix = normalize_prefix(smooth)
        self.barrier_prefix = normalize_prefix(barrier)

    def _mix(self, base: list[int], target: list[int]) -> list[int]:
        # Normalize target to the same rough total before mixing.
        base_total = sum(base)
        target_total = sum(target)
        scaled = [max(1, round(t * base_total / target_total)) for t in target]
        return [
            max(1, ((self.mix_den - self.mix_num) * b + self.mix_num * s + self.mix_den // 2) // self.mix_den)
            for b, s in zip(base, scaled)
        ]

    def prior_for_class(self, cls: int) -> list[int]:
        if cls == 1:
            return self.smooth_prefix
        if cls == 2:
            return self.barrier_prefix
        return self.base_prefix


def key_and_prior(
    scheme: apex.Scheme,
    config: MomentConfig,
    table: MomentPriorTable | None,
    channel_index: int,
    channel: np.ndarray,
    y: int,
    x: int,
    energy_value: int,
    unitary_value: int,
    cls: int,
) -> tuple[tuple[int, ...], tuple[int, ...], list[int] | None]:
    ctx, grad = apex.pixel_context_and_gradient(channel, y, x)
    key = apex.context_key(scheme, channel_index, ctx, grad, energy_value, unitary_value, y)
    parent_key = apex.parent_context_key(scheme, channel_index, ctx, energy_value)
    prior = None
    if config.model_id == MODEL_HARD_CONTEXT:
        key = (cls,) + key
    elif config.model_id in (MODEL_SOFT_MOMENT, MODEL_INVERTED_MOMENT):
        if table is None:
            raise RuntimeError("missing moment prior table")
        prior = table.prior_for_class(cls)
    return key, parent_key, prior


def encode_entropy_e30(
    planes: apex.EncodedPlanes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    config: MomentConfig,
) -> tuple[bytes, dict[str, int]]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    table = None
    if config.model_id in (MODEL_SOFT_MOMENT, MODEL_INVERTED_MOMENT):
        table = MomentPriorTable(
            planes.max_symbol,
            config.mix_num,
            config.mix_den,
            inverted=(config.model_id == MODEL_INVERTED_MOMENT),
        )
        posterior: apex.BlendedApexPosterior | e29.DynamicTransferBlendedPosterior = e29.DynamicTransferBlendedPosterior(
            planes.max_symbol,
            scheme.fine_weight,
            scheme.parent_weight,
        )
    elif scheme.blend_parent:
        posterior = apex.BlendedApexPosterior(planes.max_symbol, scheme.fine_weight, scheme.parent_weight)
    else:
        posterior = apex.FractionalApexPosterior(planes.max_symbol)

    sign_counts: dict[tuple[int, ...], list[int]] = {}
    class_counts: Counter[int] = Counter()
    coder = apex.ArithmeticEncoder()
    for channel_index, residuals in enumerate(planes.residuals):
        decoded_prefix = np.zeros((height, width), dtype=np.int32)
        history: list[int] = []
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                cls = moment_class(history)
                class_counts[cls] += 1
                pred_id = planes.predictors[tile_index]
                energy_value = planes.energy[tile_index] if scheme.use_energy else 0
                unitary_value = planes.unitary[tile_index] if scheme.use_unitary else 0
                key, parent_key, prior = key_and_prior(
                    scheme,
                    config,
                    table,
                    channel_index,
                    decoded_prefix,
                    y,
                    x,
                    energy_value,
                    unitary_value,
                    cls,
                )
                prediction = apex.predictor_value(pred_id, decoded_prefix, y, x)
                residual_value = int(residuals[y, x])
                decoded_prefix[y, x] = prediction + residual_value
                symbol = abs(residual_value) if scheme.split_sign else sigi.zigzag(residual_value)
                if isinstance(posterior, e29.DynamicTransferBlendedPosterior):
                    assert prior is not None
                    posterior.encode_symbol(coder, key, parent_key, symbol, prior)
                elif scheme.blend_parent:
                    assert isinstance(posterior, apex.BlendedApexPosterior)
                    posterior.encode_symbol(coder, key, parent_key, symbol)
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
                history.append(symbol)
                if len(history) > 5:
                    history.pop(0)
    return coder.finish(), {str(k): v for k, v in sorted(class_counts.items())}


def decode_entropy_e30(
    entropy: bytes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    max_symbol: int,
    predictors: bytes,
    energy: bytes,
    unitary: bytes,
    config: MomentConfig,
) -> list[np.ndarray]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    table = None
    if config.model_id in (MODEL_SOFT_MOMENT, MODEL_INVERTED_MOMENT):
        table = MomentPriorTable(
            max_symbol,
            config.mix_num,
            config.mix_den,
            inverted=(config.model_id == MODEL_INVERTED_MOMENT),
        )
        posterior: apex.BlendedApexPosterior | e29.DynamicTransferBlendedPosterior = e29.DynamicTransferBlendedPosterior(
            max_symbol,
            scheme.fine_weight,
            scheme.parent_weight,
        )
    elif scheme.blend_parent:
        posterior = apex.BlendedApexPosterior(max_symbol, scheme.fine_weight, scheme.parent_weight)
    else:
        posterior = apex.FractionalApexPosterior(max_symbol)

    sign_counts: dict[tuple[int, ...], list[int]] = {}
    decoder = apex.ArithmeticDecoder(entropy)
    channels: list[np.ndarray] = []
    for channel_index in range(3):
        channel = np.zeros((height, width), dtype=np.int32)
        history: list[int] = []
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                cls = moment_class(history)
                energy_value = energy[tile_index] if scheme.use_energy else 0
                unitary_value = unitary[tile_index] if scheme.use_unitary else 0
                key, parent_key, prior = key_and_prior(
                    scheme,
                    config,
                    table,
                    channel_index,
                    channel,
                    y,
                    x,
                    energy_value,
                    unitary_value,
                    cls,
                )
                if isinstance(posterior, e29.DynamicTransferBlendedPosterior):
                    assert prior is not None
                    symbol = posterior.decode_symbol(decoder, key, parent_key, prior)
                elif scheme.blend_parent:
                    assert isinstance(posterior, apex.BlendedApexPosterior)
                    symbol = posterior.decode_symbol(decoder, key, parent_key)
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
                history.append(symbol)
                if len(history) > 5:
                    history.pop(0)
        channels.append(channel)
    return channels


def encode_image_bytes_e30(
    rgb: bytes,
    width: int,
    height: int,
    transform: str,
    scheme_id: int,
    config: MomentConfig,
    planes: apex.EncodedPlanes | None = None,
) -> tuple[bytes, dict[str, object]]:
    scheme = apex.SCHEMES[scheme_id]
    residual_start = time.perf_counter()
    if planes is None:
        planes = apex.build_residual_planes(rgb, width, height, transform, scheme)
    residual_s = time.perf_counter() - residual_start
    entropy_start = time.perf_counter()
    entropy, class_counts = encode_entropy_e30(planes, width, height, scheme, config)
    entropy_s = time.perf_counter() - entropy_start

    packed_predictors = apex.pack_values(planes.predictors, 5)
    packed_energy = apex.pack_values(planes.energy, 3) if planes.energy else b""
    packed_unitary = apex.pack_values(planes.unitary, 2) if planes.unitary else b""

    header = bytearray()
    header += MAGIC
    header.append(VERSION)
    header += cell_song_poc.put_varint(width)
    header += cell_song_poc.put_varint(height)
    header += int.to_bytes(binascii.crc32(rgb) & 0xFFFFFFFF, 4, "little")
    header.append(apex.TRANSFORM_IDS[transform])
    header.append(scheme_id)
    header.append(config.model_id)
    header += cell_song_poc.put_varint(config.mix_num)
    header += cell_song_poc.put_varint(config.mix_den)
    header += cell_song_poc.put_varint(planes.max_symbol)
    header += cell_song_poc.put_varint(len(packed_predictors))
    header += packed_predictors
    header += cell_song_poc.put_varint(len(packed_energy))
    header += packed_energy
    header += cell_song_poc.put_varint(len(packed_unitary))
    header += packed_unitary
    blob = bytes(header) + entropy
    return blob, {
        "codec": "SM30",
        "model": MODEL_NAMES[config.model_id],
        "transform": transform,
        "scheme": scheme.name,
        "mix": f"{config.mix_num}/{config.mix_den}",
        "bytes": len(blob),
        "header_metadata_bytes": len(header),
        "entropy_bytes": len(entropy),
        "predictor_metadata_bytes": len(packed_predictors),
        "energy_metadata_bytes": len(packed_energy),
        "unitary_metadata_bytes": len(packed_unitary),
        "max_symbol": planes.max_symbol,
        "moment_class_counts": class_counts,
        "predictors": planes.predictor_counts,
        "residual_s": residual_s,
        "entropy_encode_s": entropy_s,
    }


def decode_image_bytes_e30(blob: bytes) -> tuple[bytes, int, int, dict[str, object]]:
    if not blob.startswith(MAGIC):
        raise sigi.SimplicialImageError("bad E30 magic")
    offset = len(MAGIC)
    version = blob[offset]
    offset += 1
    if version != VERSION:
        raise sigi.SimplicialImageError(f"unsupported E30 version {version}")
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    expected_crc = int.from_bytes(blob[offset : offset + 4], "little")
    offset += 4
    transform = apex.ID_TRANSFORMS[blob[offset]]
    offset += 1
    scheme_id = blob[offset]
    offset += 1
    scheme = apex.SCHEMES[scheme_id]
    model_id = blob[offset]
    offset += 1
    mix_num, offset = cell_song_poc.get_varint(blob, offset)
    mix_den, offset = cell_song_poc.get_varint(blob, offset)
    config = MomentConfig(model_id, mix_num, mix_den)
    max_symbol, offset = cell_song_poc.get_varint(blob, offset)
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

    _, _, tile_count = apex.tile_grid(width, height)
    expected_plane_tiles = tile_count * 3
    predictors = apex.unpack_values(packed_predictors, 5, expected_plane_tiles)
    energy = apex.unpack_values(packed_energy, 3, expected_plane_tiles) if scheme.use_energy else b""
    unitary = apex.unpack_values(packed_unitary, 2, expected_plane_tiles) if scheme.use_unitary else b""
    channels = decode_entropy_e30(entropy, width, height, scheme, max_symbol, predictors, energy, unitary, config)
    rgb = apex.inverse_transform(channels, transform)
    actual_crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if actual_crc != expected_crc:
        raise sigi.SimplicialImageError("CRC mismatch after E30 decode")
    return rgb, width, height, {
        "codec": "SM30",
        "model": MODEL_NAMES[model_id],
        "transform": transform,
        "scheme": scheme.name,
        "metadata_bytes": offset,
        "entropy_bytes": len(entropy),
        "max_symbol": max_symbol,
    }


def webp_lossless_size(rgb: bytes, width: int, height: int) -> int:
    out = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(out, format="WEBP", lossless=True, quality=100, method=6)
    return len(out.getvalue())


def parse_mix(value: str) -> tuple[int, int]:
    if "/" in value:
        left, right = value.split("/", 1)
        return int(left), int(right)
    den = 1000
    return round(float(value) * den), den


def benchmark_image(
    path: Path,
    crop_size: int,
    transform: str,
    scheme_name: str,
    mixes: list[tuple[int, int]],
    model_ids: list[int],
    artifact_dir: Path | None,
) -> dict[str, object]:
    with Image.open(path) as image:
        image = fast.center_crop(image.convert("RGB"), crop_size)
        width, height = image.size
        rgb = image.tobytes()
    scheme_id = apex.SCHEME_IDS[scheme_name]
    webp_size = webp_lossless_size(rgb, width, height)
    residual_start = time.perf_counter()
    planes = apex.build_residual_planes(rgb, width, height, transform, apex.SCHEMES[scheme_id])
    residual_build_s = time.perf_counter() - residual_start

    configs = []
    if MODEL_BASELINE in model_ids:
        configs.append(MomentConfig(MODEL_BASELINE, 0, 1))
    if MODEL_HARD_CONTEXT in model_ids:
        configs.append(MomentConfig(MODEL_HARD_CONTEXT, 0, 1))
    for mix_num, mix_den in mixes:
        if MODEL_SOFT_MOMENT in model_ids:
            configs.append(MomentConfig(MODEL_SOFT_MOMENT, mix_num, mix_den))
        if MODEL_INVERTED_MOMENT in model_ids:
            configs.append(MomentConfig(MODEL_INVERTED_MOMENT, mix_num, mix_den))
    unique: dict[tuple[int, int, int], MomentConfig] = {
        (cfg.model_id, cfg.mix_num, cfg.mix_den): cfg for cfg in configs
    }
    rows = []
    for config in unique.values():
        print(f"E30 {MODEL_NAMES[config.model_id]} mix={config.mix_num}/{config.mix_den}", file=sys.stderr)
        start = time.perf_counter()
        blob, encode_stats = encode_image_bytes_e30(rgb, width, height, transform, scheme_id, config, planes=planes)
        encode_stats["shared_residual_build_s"] = residual_build_s
        encode_s = time.perf_counter() - start
        decode_start = time.perf_counter()
        decoded, decoded_width, decoded_height, decode_stats = decode_image_bytes_e30(blob)
        decode_s = time.perf_counter() - decode_start
        ok = decoded == rgb and decoded_width == width and decoded_height == height
        if artifact_dir is not None:
            artifact_dir.mkdir(parents=True, exist_ok=True)
            safe_model = MODEL_NAMES[config.model_id].replace("-", "_")
            stem = path.stem.replace(" ", "_")
            out = artifact_dir / f"{stem}_{crop_size}_e30_{safe_model}_m{config.mix_num}-{config.mix_den}.sm30"
            out.write_bytes(blob)
        rows.append(
            {
                "model": MODEL_NAMES[config.model_id],
                "mix": f"{config.mix_num}/{config.mix_den}",
                "bytes": len(blob),
                "delta_vs_webp": len(blob) - webp_size,
                "roundtrip_ok": ok,
                "encode_s": encode_s,
                "decode_s": decode_s,
                "encode_stats": encode_stats,
                "decode_stats": decode_stats,
            }
        )
    rows.sort(key=lambda row: row["bytes"])
    return {
        "file": str(path),
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "transform": transform,
        "scheme": scheme_name,
        "rows": rows,
    }


def write_report(json_path: Path, report_path: Path) -> None:
    docs = json.loads(json_path.read_text(encoding="utf-8"))
    lines = [
        "# E30 Moment-Barrier Gate",
        "",
        "E30 tests the P6 moment-barrier lesson in the image codec: use a causal Hankel sign from already-decoded residual magnitudes to choose whether the entropy model should lean smooth or rough, with no transmitted gate map.",
        "",
    ]
    for doc in docs:
        baseline = next(row for row in doc["rows"] if row["model"] == "baseline")
        lines += [
            f"## {Path(doc['file']).name}",
            "",
            f"- crop: `{doc['width']}x{doc['height']}` RGB",
            f"- transform: `{doc['transform']}`",
            f"- scheme: `{doc['scheme']}`",
            f"- WebP lossless: `{doc['webp_lossless_bytes']:,}` bytes",
            f"- E30 baseline: `{baseline['bytes']:,}` bytes",
            "",
            "| rank | model | mix | bytes | vs E30 baseline | vs WebP | roundtrip |",
            "|---:|---|---:|---:|---:|---:|---|",
        ]
        for rank, row in enumerate(doc["rows"], start=1):
            lines.append(
                f"| {rank} | {row['model']} | {row['mix']} | {row['bytes']:,} | "
                f"{row['bytes'] - baseline['bytes']:+,} | {row['delta_vs_webp']:+,} | {row['roundtrip_ok']} |"
            )
        best = doc["rows"][0]
        counts = baseline["encode_stats"].get("moment_class_counts", {})
        lines += [
            "",
            "## Interpretation",
            "",
            f"The best E30 row is `{best['model']}` at `{best['bytes']:,}` bytes.",
            f"The baseline causal Hankel classes were `{counts}` where `1` is nonnegative Hankel and `2` is negative Hankel/barrier.",
            "",
            "A pass would mean the causal moment barrier improves compression without payload. A useful joint result would mean the moment sign is diagnostic but the current prior/context action is too blunt.",
            "",
        ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--transform", default="r-gr-bg", choices=sorted(apex.TRANSFORM_IDS))
    parser.add_argument("--scheme", default="ch-ctx-energy-unitary-split-blend71-apex128", choices=sorted(apex.SCHEME_IDS))
    parser.add_argument("--mixes", default="1/4,1/2")
    parser.add_argument(
        "--models",
        default="baseline,hard-moment-context,soft-moment-prior,inverted-moment-prior",
        help="Comma-separated model names to run. Use names from baseline, hard-moment-context, soft-moment-prior, inverted-moment-prior.",
    )
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/e30_moment_barrier_gate.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/e30_moment_barrier_gate.md"))
    parser.add_argument("--write-artifacts", action="store_true")
    args = parser.parse_args(argv)

    mixes = [parse_mix(item.strip()) for item in args.mixes.split(",") if item.strip()]
    model_ids = []
    for item in args.models.split(","):
        name = item.strip()
        if not name:
            continue
        if name not in NAME_MODELS:
            raise SystemExit(f"unknown E30 model {name!r}; choices: {', '.join(NAME_MODELS)}")
        model_ids.append(NAME_MODELS[name])
    if not model_ids:
        raise SystemExit("at least one E30 model must be selected")
    rows = []
    artifact_dir = args.json.parent if args.write_artifacts else None
    for path in args.images:
        rows.append(
            benchmark_image(
                path,
                args.crop_size,
                args.transform,
                args.scheme,
                mixes,
                model_ids,
                artifact_dir,
            )
        )
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(args.json, args.report)
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for doc in rows:
        best = doc["rows"][0]
        print(
            f"{Path(doc['file']).name}: best={best['bytes']:,} model={best['model']} "
            f"mix={best['mix']} webp={doc['webp_lossless_bytes']:,} "
            f"delta={best['delta_vs_webp']:+,} roundtrip={best['roundtrip_ok']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
