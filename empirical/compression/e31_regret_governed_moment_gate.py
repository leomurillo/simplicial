#!/usr/bin/env python3
"""E31 regret-governed moment gate for the Apex image codec.

E30 showed that a causal Hankel/moment split can improve lossless coding, but
that exposing the split too early can fragment small-context statistics. E31
keeps both experts synchronized:

    baseline expert: native Apex context key
    moment expert:   Hankel class prepended to the native key

Both experts are updated on every decoded symbol. The actual stream follows the
moment expert only after past symbols have shown enough regret reduction. The
decision is therefore payload-free: decoder and encoder have identical expert
states and identical cumulative scores.
"""

from __future__ import annotations

import argparse
import binascii
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

import apex_seeded_image_codec as apex
import benchmark_sigi_vs_webp_fast as fast
import cell_song_poc
import e30_moment_barrier_gate as e30
import simplicial_image_codec as sigi


MAGIC = b"SM31"
VERSION = 1

MODE_GLOBAL = 0
MODE_CHANNEL = 1
MODE_CLASS = 2
MODE_CHANNEL_CLASS = 3

MODE_NAMES = {
    MODE_GLOBAL: "regret-global",
    MODE_CHANNEL: "regret-channel",
    MODE_CLASS: "regret-class",
    MODE_CHANNEL_CLASS: "regret-channel-class",
}
NAME_MODES = {value: key for key, value in MODE_NAMES.items()}


@dataclass(frozen=True)
class RegretConfig:
    mode_id: int
    threshold_millibits: int
    warmup: int

    @property
    def threshold_bits(self) -> float:
        return self.threshold_millibits / 1000.0

    @property
    def label(self) -> str:
        threshold = self.threshold_millibits / 1000.0
        if threshold.is_integer():
            threshold_text = str(int(threshold))
        else:
            threshold_text = f"{threshold:.3f}".rstrip("0").rstrip(".")
        return f"{MODE_NAMES[self.mode_id]}-t{threshold_text}-w{self.warmup}"


class OnlineApexExpert:
    def __init__(self, max_symbol: int, scheme: apex.Scheme) -> None:
        self.scheme = scheme
        if scheme.blend_parent:
            self.posterior: apex.BlendedApexPosterior | apex.FractionalApexPosterior = apex.BlendedApexPosterior(
                max_symbol,
                scheme.fine_weight,
                scheme.parent_weight,
            )
        else:
            self.posterior = apex.FractionalApexPosterior(max_symbol)
        self.max_symbol = max_symbol

    def interval(self, key: tuple[int, ...], parent_key: tuple[int, ...], symbol: int) -> tuple[int, int, int]:
        if self.scheme.blend_parent:
            assert isinstance(self.posterior, apex.BlendedApexPosterior)
            child = self.posterior._child(key)
            parent = self.posterior._parent(parent_key)
            return self.posterior._interval(child, parent, symbol)
        assert isinstance(self.posterior, apex.FractionalApexPosterior)
        return self.posterior.context(key).interval(symbol)

    def total(self, key: tuple[int, ...], parent_key: tuple[int, ...]) -> int:
        if self.scheme.blend_parent:
            assert isinstance(self.posterior, apex.BlendedApexPosterior)
            child = self.posterior._child(key)
            parent = self.posterior._parent(parent_key)
            return (self.scheme.fine_weight + self.scheme.parent_weight) * child.total * parent.total
        assert isinstance(self.posterior, apex.FractionalApexPosterior)
        return self.posterior.context(key).total

    def encode_symbol(
        self,
        coder: apex.ArithmeticEncoder,
        key: tuple[int, ...],
        parent_key: tuple[int, ...],
        symbol: int,
    ) -> None:
        low, high, total = self.interval(key, parent_key, symbol)
        coder.encode(low, high, total)

    def decode_symbol(
        self,
        decoder: apex.ArithmeticDecoder,
        key: tuple[int, ...],
        parent_key: tuple[int, ...],
    ) -> int:
        total = self.total(key, parent_key)
        value = decoder.value(total)
        lo = 0
        hi = self.max_symbol
        while lo < hi:
            mid = (lo + hi) // 2
            _, high, _ = self.interval(key, parent_key, mid)
            if value < high:
                hi = mid
            else:
                lo = mid + 1
        symbol = lo
        low, high, total = self.interval(key, parent_key, symbol)
        decoder.decode(low, high, total)
        return symbol

    def update(self, key: tuple[int, ...], parent_key: tuple[int, ...], symbol: int) -> None:
        if self.scheme.blend_parent:
            assert isinstance(self.posterior, apex.BlendedApexPosterior)
            self.posterior._child(key).counts.update(symbol)
            self.posterior._parent(parent_key).counts.update(symbol)
            return
        assert isinstance(self.posterior, apex.FractionalApexPosterior)
        self.posterior.context(key).counts.update(symbol)


def interval_bits(interval: tuple[int, int, int]) -> float:
    low, high, total = interval
    width = high - low
    return math.log2(total) - math.log2(width)


def sign_interval(sign_counts: dict[tuple[int, ...], list[int]], key: tuple[int, ...], sign: int) -> tuple[int, int, int]:
    counts = sign_counts.get(key)
    if counts is None:
        counts = [1, 1]
    total = counts[0] + counts[1]
    low = counts[0] if sign else 0
    high = low + counts[sign]
    return low, high, total


def encode_sign(
    coder: apex.ArithmeticEncoder,
    sign_counts: dict[tuple[int, ...], list[int]],
    key: tuple[int, ...],
    sign: int,
) -> None:
    low, high, total = sign_interval(sign_counts, key, sign)
    coder.encode(low, high, total)


def decode_sign(
    decoder: apex.ArithmeticDecoder,
    sign_counts: dict[tuple[int, ...], list[int]],
    key: tuple[int, ...],
) -> int:
    counts = sign_counts.get(key)
    if counts is None:
        counts = [1, 1]
    total = counts[0] + counts[1]
    value = decoder.value(total)
    sign = 0 if value < counts[0] else 1
    low = counts[0] if sign else 0
    high = low + counts[sign]
    decoder.decode(low, high, total)
    return sign


def update_sign(sign_counts: dict[tuple[int, ...], list[int]], key: tuple[int, ...], sign: int) -> None:
    counts = sign_counts.setdefault(key, [1, 1])
    counts[sign] += 1


def gate_key(config: RegretConfig, channel_index: int, cls: int) -> tuple[int, ...]:
    if config.mode_id == MODE_GLOBAL:
        return (0,)
    if config.mode_id == MODE_CHANNEL:
        return (channel_index,)
    if config.mode_id == MODE_CLASS:
        return (cls,)
    if config.mode_id == MODE_CHANNEL_CLASS:
        return (channel_index, cls)
    raise ValueError(f"unknown regret mode {config.mode_id}")


def should_use_hard(
    config: RegretConfig,
    scores: dict[tuple[int, ...], float],
    seen: dict[tuple[int, ...], int],
    key: tuple[int, ...],
) -> bool:
    return seen[key] >= config.warmup and scores[key] > config.threshold_bits


def base_and_hard_keys(
    scheme: apex.Scheme,
    channel_index: int,
    channel: np.ndarray,
    y: int,
    x: int,
    energy_value: int,
    unitary_value: int,
    cls: int,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    ctx, grad = apex.pixel_context_and_gradient(channel, y, x)
    base_key = apex.context_key(scheme, channel_index, ctx, grad, energy_value, unitary_value, y)
    parent_key = apex.parent_context_key(scheme, channel_index, ctx, energy_value)
    hard_key = (cls,) + base_key
    return base_key, hard_key, parent_key


def score_summary(scores: dict[tuple[int, ...], float]) -> dict[str, float]:
    if not scores:
        return {"keys": 0, "min_bits": 0.0, "max_bits": 0.0, "sum_bits": 0.0}
    values = list(scores.values())
    return {
        "keys": len(values),
        "min_bits": min(values),
        "max_bits": max(values),
        "sum_bits": sum(values),
    }


def encode_entropy_e31(
    planes: apex.EncodedPlanes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    config: RegretConfig,
) -> tuple[bytes, dict[str, object]]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    baseline = OnlineApexExpert(planes.max_symbol, scheme)
    hard = OnlineApexExpert(planes.max_symbol, scheme)
    baseline_sign_counts: dict[tuple[int, ...], list[int]] = {}
    hard_sign_counts: dict[tuple[int, ...], list[int]] = {}
    scores: defaultdict[tuple[int, ...], float] = defaultdict(float)
    seen: defaultdict[tuple[int, ...], int] = defaultdict(int)
    class_counts: Counter[int] = Counter()
    selected_counts: Counter[str] = Counter()
    selected_by_class: Counter[str] = Counter()
    baseline_loss_bits = 0.0
    hard_loss_bits = 0.0
    chosen_loss_bits = 0.0
    activations = 0

    coder = apex.ArithmeticEncoder()
    for channel_index, residuals in enumerate(planes.residuals):
        decoded_prefix = np.zeros((height, width), dtype=np.int32)
        history: list[int] = []
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                cls = e30.moment_class(history)
                class_counts[cls] += 1
                pred_id = planes.predictors[tile_index]
                energy_value = planes.energy[tile_index] if scheme.use_energy else 0
                unitary_value = planes.unitary[tile_index] if scheme.use_unitary else 0
                base_key, hard_key, parent_key = base_and_hard_keys(
                    scheme,
                    channel_index,
                    decoded_prefix,
                    y,
                    x,
                    energy_value,
                    unitary_value,
                    cls,
                )
                gkey = gate_key(config, channel_index, cls)
                active = should_use_hard(config, scores, seen, gkey)
                selected_counts["hard" if active else "baseline"] += 1
                selected_by_class[f"{cls}:{'hard' if active else 'baseline'}"] += 1
                if active:
                    activations += 1

                prediction = apex.predictor_value(pred_id, decoded_prefix, y, x)
                residual_value = int(residuals[y, x])
                decoded_prefix[y, x] = prediction + residual_value
                symbol = abs(residual_value) if scheme.split_sign else sigi.zigzag(residual_value)

                base_interval = baseline.interval(base_key, parent_key, symbol)
                hard_interval = hard.interval(hard_key, parent_key, symbol)
                if active:
                    coder.encode(*hard_interval)
                else:
                    coder.encode(*base_interval)
                base_loss = interval_bits(base_interval)
                hard_loss = interval_bits(hard_interval)
                chosen_loss = hard_loss if active else base_loss

                if scheme.split_sign and symbol:
                    sign = 1 if residual_value < 0 else 0
                    base_sign_interval = sign_interval(baseline_sign_counts, base_key, sign)
                    hard_sign_interval = sign_interval(hard_sign_counts, hard_key, sign)
                    if active:
                        coder.encode(*hard_sign_interval)
                    else:
                        coder.encode(*base_sign_interval)
                    base_loss += interval_bits(base_sign_interval)
                    hard_loss += interval_bits(hard_sign_interval)
                    chosen_loss += interval_bits(hard_sign_interval if active else base_sign_interval)
                    update_sign(baseline_sign_counts, base_key, sign)
                    update_sign(hard_sign_counts, hard_key, sign)

                scores[gkey] += base_loss - hard_loss
                seen[gkey] += 1
                baseline_loss_bits += base_loss
                hard_loss_bits += hard_loss
                chosen_loss_bits += chosen_loss
                baseline.update(base_key, parent_key, symbol)
                hard.update(hard_key, parent_key, symbol)

                history.append(symbol)
                if len(history) > 5:
                    history.pop(0)

    return coder.finish(), {
        "moment_class_counts": {str(k): v for k, v in sorted(class_counts.items())},
        "selected_counts": dict(selected_counts),
        "selected_by_class": dict(selected_by_class),
        "gate_activations": activations,
        "gate_scores": score_summary(scores),
        "baseline_expert_loss_bits": baseline_loss_bits,
        "hard_expert_loss_bits": hard_loss_bits,
        "chosen_loss_bits": chosen_loss_bits,
        "hard_expert_advantage_bits": baseline_loss_bits - hard_loss_bits,
        "chosen_vs_baseline_bits": baseline_loss_bits - chosen_loss_bits,
        "chosen_vs_hard_bits": hard_loss_bits - chosen_loss_bits,
    }


def decode_entropy_e31(
    entropy: bytes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    max_symbol: int,
    predictors: bytes,
    energy: bytes,
    unitary: bytes,
    config: RegretConfig,
) -> list[np.ndarray]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    baseline = OnlineApexExpert(max_symbol, scheme)
    hard = OnlineApexExpert(max_symbol, scheme)
    baseline_sign_counts: dict[tuple[int, ...], list[int]] = {}
    hard_sign_counts: dict[tuple[int, ...], list[int]] = {}
    scores: defaultdict[tuple[int, ...], float] = defaultdict(float)
    seen: defaultdict[tuple[int, ...], int] = defaultdict(int)
    decoder = apex.ArithmeticDecoder(entropy)
    channels: list[np.ndarray] = []

    for channel_index in range(3):
        channel = np.zeros((height, width), dtype=np.int32)
        history: list[int] = []
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                cls = e30.moment_class(history)
                energy_value = energy[tile_index] if scheme.use_energy else 0
                unitary_value = unitary[tile_index] if scheme.use_unitary else 0
                base_key, hard_key, parent_key = base_and_hard_keys(
                    scheme,
                    channel_index,
                    channel,
                    y,
                    x,
                    energy_value,
                    unitary_value,
                    cls,
                )
                gkey = gate_key(config, channel_index, cls)
                active = should_use_hard(config, scores, seen, gkey)
                if active:
                    symbol = hard.decode_symbol(decoder, hard_key, parent_key)
                else:
                    symbol = baseline.decode_symbol(decoder, base_key, parent_key)

                base_interval = baseline.interval(base_key, parent_key, symbol)
                hard_interval = hard.interval(hard_key, parent_key, symbol)
                base_loss = interval_bits(base_interval)
                hard_loss = interval_bits(hard_interval)

                if scheme.split_sign:
                    if symbol:
                        if active:
                            sign = decode_sign(decoder, hard_sign_counts, hard_key)
                        else:
                            sign = decode_sign(decoder, baseline_sign_counts, base_key)
                        base_sign_interval = sign_interval(baseline_sign_counts, base_key, sign)
                        hard_sign_interval = sign_interval(hard_sign_counts, hard_key, sign)
                        base_loss += interval_bits(base_sign_interval)
                        hard_loss += interval_bits(hard_sign_interval)
                        residual = -symbol if sign else symbol
                        update_sign(baseline_sign_counts, base_key, sign)
                        update_sign(hard_sign_counts, hard_key, sign)
                    else:
                        residual = 0
                else:
                    residual = apex.unzigzag(symbol)

                scores[gkey] += base_loss - hard_loss
                seen[gkey] += 1
                baseline.update(base_key, parent_key, symbol)
                hard.update(hard_key, parent_key, symbol)
                pred_id = predictors[tile_index]
                channel[y, x] = apex.predictor_value(pred_id, channel, y, x) + residual
                history.append(symbol)
                if len(history) > 5:
                    history.pop(0)
        channels.append(channel)
    return channels


def encode_image_bytes_e31(
    rgb: bytes,
    width: int,
    height: int,
    transform: str,
    scheme_id: int,
    config: RegretConfig,
    planes: apex.EncodedPlanes | None = None,
) -> tuple[bytes, dict[str, object]]:
    scheme = apex.SCHEMES[scheme_id]
    residual_start = time.perf_counter()
    if planes is None:
        planes = apex.build_residual_planes(rgb, width, height, transform, scheme)
    residual_s = time.perf_counter() - residual_start
    entropy_start = time.perf_counter()
    entropy, gate_stats = encode_entropy_e31(planes, width, height, scheme, config)
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
    header.append(config.mode_id)
    header += cell_song_poc.put_varint(config.threshold_millibits)
    header += cell_song_poc.put_varint(config.warmup)
    header += cell_song_poc.put_varint(planes.max_symbol)
    header += cell_song_poc.put_varint(len(packed_predictors))
    header += packed_predictors
    header += cell_song_poc.put_varint(len(packed_energy))
    header += packed_energy
    header += cell_song_poc.put_varint(len(packed_unitary))
    header += packed_unitary
    blob = bytes(header) + entropy
    return blob, {
        "codec": "SM31",
        "model": config.label,
        "mode": MODE_NAMES[config.mode_id],
        "threshold_bits": config.threshold_bits,
        "warmup": config.warmup,
        "transform": transform,
        "scheme": scheme.name,
        "bytes": len(blob),
        "header_metadata_bytes": len(header),
        "entropy_bytes": len(entropy),
        "predictor_metadata_bytes": len(packed_predictors),
        "energy_metadata_bytes": len(packed_energy),
        "unitary_metadata_bytes": len(packed_unitary),
        "max_symbol": planes.max_symbol,
        "predictors": planes.predictor_counts,
        "residual_s": residual_s,
        "entropy_encode_s": entropy_s,
        **gate_stats,
    }


def decode_image_bytes_e31(blob: bytes) -> tuple[bytes, int, int, dict[str, object]]:
    if not blob.startswith(MAGIC):
        raise sigi.SimplicialImageError("bad E31 magic")
    offset = len(MAGIC)
    version = blob[offset]
    offset += 1
    if version != VERSION:
        raise sigi.SimplicialImageError(f"unsupported E31 version {version}")
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    expected_crc = int.from_bytes(blob[offset : offset + 4], "little")
    offset += 4
    transform = apex.ID_TRANSFORMS[blob[offset]]
    offset += 1
    scheme_id = blob[offset]
    offset += 1
    scheme = apex.SCHEMES[scheme_id]
    mode_id = blob[offset]
    offset += 1
    threshold_millibits, offset = cell_song_poc.get_varint(blob, offset)
    warmup, offset = cell_song_poc.get_varint(blob, offset)
    config = RegretConfig(mode_id, threshold_millibits, warmup)
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
    channels = decode_entropy_e31(entropy, width, height, scheme, max_symbol, predictors, energy, unitary, config)
    rgb = apex.inverse_transform(channels, transform)
    actual_crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if actual_crc != expected_crc:
        raise sigi.SimplicialImageError("CRC mismatch after E31 decode")
    return rgb, width, height, {
        "codec": "SM31",
        "model": config.label,
        "mode": MODE_NAMES[mode_id],
        "threshold_bits": config.threshold_bits,
        "warmup": warmup,
        "metadata_bytes": offset,
        "entropy_bytes": len(entropy),
        "max_symbol": max_symbol,
    }


def webp_lossless_size(rgb: bytes, width: int, height: int) -> int:
    out = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(out, format="WEBP", lossless=True, quality=100, method=6)
    return len(out.getvalue())


def load_references(paths: list[Path]) -> dict[tuple[str, int, int], dict[str, int]]:
    references: dict[tuple[str, int, int], dict[str, int]] = {}
    for path in paths:
        if not path.exists():
            continue
        for doc in json.loads(path.read_text(encoding="utf-8")):
            key = (str(Path(doc["file"])), int(doc["width"]), int(doc["height"]))
            rows = references.setdefault(key, {})
            for row in doc["rows"]:
                rows[row["model"]] = int(row["bytes"])
    return references


def parse_configs(modes: str, thresholds: str, warmups: str) -> list[RegretConfig]:
    mode_ids = []
    for item in modes.split(","):
        name = item.strip()
        if not name:
            continue
        if name not in NAME_MODES:
            raise SystemExit(f"unknown E31 mode {name!r}; choices: {', '.join(NAME_MODES)}")
        mode_ids.append(NAME_MODES[name])
    threshold_values = [round(float(item.strip()) * 1000) for item in thresholds.split(",") if item.strip()]
    warmup_values = [int(item.strip()) for item in warmups.split(",") if item.strip()]
    if not mode_ids or not threshold_values or not warmup_values:
        raise SystemExit("at least one mode, threshold, and warmup are required")
    return [
        RegretConfig(mode_id, threshold_millibits, warmup)
        for mode_id in mode_ids
        for threshold_millibits in threshold_values
        for warmup in warmup_values
    ]


def benchmark_image(
    path: Path,
    crop_size: int,
    transform: str,
    scheme_name: str,
    configs: list[RegretConfig],
    references: dict[tuple[str, int, int], dict[str, int]],
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
    rows = []
    reference_rows = references.get((str(path), width, height), {})

    for name, size in sorted(reference_rows.items()):
        rows.append(
            {
                "model": f"E30 {name}",
                "bytes": size,
                "delta_vs_webp": size - webp_size,
                "roundtrip_ok": True,
                "reference": True,
            }
        )

    for config in configs:
        print(f"E31 {config.label}", file=sys.stderr)
        start = time.perf_counter()
        blob, encode_stats = encode_image_bytes_e31(rgb, width, height, transform, scheme_id, config, planes=planes)
        encode_stats["shared_residual_build_s"] = residual_build_s
        encode_s = time.perf_counter() - start
        decode_start = time.perf_counter()
        decoded, decoded_width, decoded_height, decode_stats = decode_image_bytes_e31(blob)
        decode_s = time.perf_counter() - decode_start
        ok = decoded == rgb and decoded_width == width and decoded_height == height
        if artifact_dir is not None:
            artifact_dir.mkdir(parents=True, exist_ok=True)
            safe_model = config.label.replace("-", "_").replace(".", "_")
            stem = path.stem.replace(" ", "_")
            out = artifact_dir / f"{stem}_{crop_size}_e31_{safe_model}.sm31"
            out.write_bytes(blob)
        rows.append(
            {
                "model": config.label,
                "bytes": len(blob),
                "delta_vs_webp": len(blob) - webp_size,
                "roundtrip_ok": ok,
                "reference": False,
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
        "# E31 Regret-Governed Moment Gate",
        "",
        "E31 keeps the E30 hard Hankel/moment split but governs it by causal expert regret. The decoder computes the same regret state from prior decoded symbols, so no gate payload is transmitted.",
        "",
    ]
    for doc in docs:
        baseline = next((row for row in doc["rows"] if row["model"] == "E30 baseline"), None)
        lines += [
            f"## {Path(doc['file']).name}",
            "",
            f"- crop: `{doc['width']}x{doc['height']}` RGB",
            f"- transform: `{doc['transform']}`",
            f"- scheme: `{doc['scheme']}`",
            f"- WebP lossless: `{doc['webp_lossless_bytes']:,}` bytes",
            "",
            "| rank | model | bytes | vs E30 baseline | vs WebP | roundtrip |",
            "|---:|---|---:|---:|---:|---|",
        ]
        for rank, row in enumerate(doc["rows"], start=1):
            if baseline is None:
                vs_baseline = ""
            else:
                vs_baseline = f"{row['bytes'] - baseline['bytes']:+,}"
            lines.append(
                f"| {rank} | {row['model']} | {row['bytes']:,} | {vs_baseline} | "
                f"{row['delta_vs_webp']:+,} | {row['roundtrip_ok']} |"
            )
        best = doc["rows"][0]
        e31_rows = [row for row in doc["rows"] if not row.get("reference")]
        if e31_rows:
            best_e31 = min(e31_rows, key=lambda row: row["bytes"])
            stats = best_e31["encode_stats"]
            selected = stats.get("selected_counts", {})
            score = stats.get("gate_scores", {})
            lines += [
                "",
                "### Gate Diagnostics",
                "",
                f"- best row: `{best['model']}` at `{best['bytes']:,}` bytes",
                f"- best E31 row: `{best_e31['model']}` at `{best_e31['bytes']:,}` bytes",
                f"- selected counts: `{selected}`",
                f"- final gate score summary: `{score}`",
                f"- hard expert advantage: `{stats.get('hard_expert_advantage_bits', 0.0):.1f}` bits",
                f"- chosen vs baseline: `{stats.get('chosen_vs_baseline_bits', 0.0):.1f}` bits",
                "",
            ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--transform", default="r-gr-bg", choices=sorted(apex.TRANSFORM_IDS))
    parser.add_argument("--scheme", default="ch-ctx-energy-unitary-split-blend71-apex128", choices=sorted(apex.SCHEME_IDS))
    parser.add_argument("--modes", default="regret-global", help="Comma-separated E31 modes")
    parser.add_argument("--threshold-bits", default="512", help="Comma-separated activation thresholds in bits")
    parser.add_argument("--warmups", default="2048", help="Comma-separated per-gate warmup counts")
    parser.add_argument("--reference-json", action="append", type=Path, default=[])
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/e31_regret_governed_moment_gate.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/e31_regret_governed_moment_gate.md"))
    parser.add_argument("--write-artifacts", action="store_true")
    args = parser.parse_args(argv)

    configs = parse_configs(args.modes, args.threshold_bits, args.warmups)
    references = load_references(args.reference_json)
    artifact_dir = args.json.parent if args.write_artifacts else None
    docs = []
    for path in args.images:
        docs.append(
            benchmark_image(
                path,
                args.crop_size,
                args.transform,
                args.scheme,
                configs,
                references,
                artifact_dir,
            )
        )
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(docs, indent=2), encoding="utf-8")
    write_report(args.json, args.report)
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for doc in docs:
        best = doc["rows"][0]
        print(
            f"{Path(doc['file']).name}: best={best['bytes']:,} model={best['model']} "
            f"webp={doc['webp_lossless_bytes']:,} delta={best['delta_vs_webp']:+,} "
            f"roundtrip={best['roundtrip_ok']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
