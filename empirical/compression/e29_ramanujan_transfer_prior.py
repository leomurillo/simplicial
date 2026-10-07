#!/usr/bin/env python3
"""E29 Ramanujan transfer prior experiment.

E28 showed that dense local gauge maps are expensive when transmitted. E29
tries the P5 lesson in the no-payload direction: keep the global reversible
gauge and use the Helmert-to-conductor transfer distribution R_k(d) as a
deterministic prior inside the Apex arithmetic model.

The residual stream, predictor metadata, and reversible color gauge are kept
fixed. Only the entropy posterior changes.
"""

from __future__ import annotations

import argparse
import binascii
import io
import json
import math
import sys
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np
from PIL import Image

import apex_seeded_image_codec as apex
import benchmark_sigi_vs_webp_fast as fast
import cell_song_poc
import simplicial_image_codec as sigi


MAGIC = b"SR29"
VERSION = 1

MODEL_BASELINE = 0
MODEL_HARD_RUNG_CONTEXT = 1
MODEL_SOFT_RAMANUJAN = 2
MODEL_SHUFFLED_RAMANUJAN = 3

MODEL_NAMES = {
    MODEL_BASELINE: "baseline",
    MODEL_HARD_RUNG_CONTEXT: "hard-rung-context",
    MODEL_SOFT_RAMANUJAN: "soft-ramanujan",
    MODEL_SHUFFLED_RAMANUJAN: "shuffled-ramanujan",
}
NAME_MODELS = {value: key for key, value in MODEL_NAMES.items()}


@dataclass(frozen=True)
class PriorConfig:
    model_id: int
    conductor_modulus: int
    mix_num: int
    mix_den: int
    rung_mode: str


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def phi(n: int) -> int:
    result = n
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            result -= result // p
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        result -= result // value
    return result


def ramanujan_sum(d: int, n: int) -> int:
    g = math.gcd(d, n)
    q = d // g
    return mobius(q) * phi(d) // phi(q)


def conductor(n: int, modulus: int) -> int:
    residue = n % modulus
    if residue == 0:
        return 1
    return modulus // math.gcd(residue, modulus)


def transfer_distribution(modulus: int, rung: int) -> dict[int, Fraction]:
    h = [0] * modulus
    for i in range(rung):
        h[i] = 1
    h[rung] = -rung
    denom = modulus * rung * (rung + 1)
    weights: dict[int, Fraction] = {}
    for d in divisors(modulus):
        if d == 1:
            continue
        total = 0
        for s, hs in enumerate(h):
            if hs == 0:
                continue
            for t, ht in enumerate(h):
                if ht == 0:
                    continue
                total += hs * ht * ramanujan_sum(d, s - t)
        weights[d] = Fraction(total, denom)
    return weights


def rung_at(x: int, y: int, modulus: int, mode: str) -> int:
    period = modulus - 1
    if mode == "x":
        raw = x
    elif mode == "y":
        raw = y
    elif mode == "diag":
        raw = x + y
    elif mode == "tile":
        raw = (y % sigi.TILE) * sigi.TILE + (x % sigi.TILE)
    elif mode == "linear":
        raw = y * 4096 + x
    else:
        raise ValueError(f"unknown rung mode {mode}")
    return 1 + (raw % period)


def normalized_prefix(masses: list[int], denominator: int = apex.PRIOR_DENOMINATOR) -> list[int]:
    total = sum(masses)
    if total <= 0:
        raise ValueError("empty prior mass")
    prefix = [0]
    running = 0
    for mass in masses:
        running += mass
        value = round(denominator * running / total)
        prefix.append(max(prefix[-1] + 1, min(denominator, int(value))))
    prefix[-1] = denominator
    return prefix


class TransferPriorTable:
    def __init__(
        self,
        max_symbol: int,
        conductor_modulus: int,
        mix_num: int,
        mix_den: int,
        shuffled: bool,
    ) -> None:
        if conductor_modulus < 2:
            raise ValueError("conductor modulus must be >= 2")
        if mix_num < 0 or mix_den <= 0 or mix_num > mix_den:
            raise ValueError("mix must satisfy 0 <= mix_num <= mix_den")
        self.max_symbol = max_symbol
        self.modulus = conductor_modulus
        self.mix_num = mix_num
        self.mix_den = mix_den
        self.divs = divisors(conductor_modulus)
        self.nontrivial = [d for d in self.divs if d > 1]
        self.symbol_cond = [conductor(symbol, conductor_modulus) for symbol in range(max_symbol + 1)]
        base_prefix = apex.apex_prior_prefix(max_symbol)
        base_mass = [base_prefix[i + 1] - base_prefix[i] for i in range(max_symbol + 1)]
        base_by_d = {d: 0 for d in self.divs}
        for symbol, d in enumerate(self.symbol_cond):
            base_by_d[d] += base_mass[symbol]
        nontriv_base_total = sum(base_by_d[d] for d in self.nontrivial)
        if nontriv_base_total <= 0:
            raise ValueError("no nontrivial conductor mass")

        permuted = list(self.nontrivial)
        if shuffled:
            # A deterministic wrong seam: same mass histogram, wrong packet names.
            permuted = permuted[1:] + permuted[:1]

        self.priors: dict[int, list[int]] = {}
        self.dominant: dict[int, int] = {}
        for rung in range(1, conductor_modulus):
            transfer = transfer_distribution(conductor_modulus, rung)
            clean_transfer = {d: max(Fraction(0), transfer.get(d, Fraction(0))) for d in self.nontrivial}
            total_transfer = sum(clean_transfer.values())
            if total_transfer <= 0:
                clean_transfer = {d: Fraction(1, len(self.nontrivial)) for d in self.nontrivial}
                total_transfer = Fraction(1)
            desired_by_d = dict(base_by_d)
            for original_d, target_d in zip(self.nontrivial, permuted):
                desired_by_d[target_d] = int(round(nontriv_base_total * clean_transfer[original_d] / total_transfer))
            # Correct any rounding drift on the largest desired packet.
            drift = nontriv_base_total - sum(desired_by_d[d] for d in self.nontrivial)
            if drift:
                best_d = max(self.nontrivial, key=lambda d: desired_by_d[d])
                desired_by_d[best_d] += drift

            masses: list[int] = []
            for symbol, d in enumerate(self.symbol_cond):
                base = base_mass[symbol]
                if base_by_d[d] <= 0:
                    target = base
                else:
                    target = max(1, int(round(base * desired_by_d[d] / base_by_d[d])))
                mixed = ((mix_den - mix_num) * base + mix_num * target + mix_den // 2) // mix_den
                masses.append(max(1, mixed))
            self.priors[rung] = normalized_prefix(masses)
            self.dominant[rung] = max(clean_transfer, key=lambda d: (clean_transfer[d], d))

    def prior_prefix(self, rung: int) -> list[int]:
        return self.priors[rung]

    def dominant_conductor(self, rung: int) -> int:
        return self.dominant[rung]


class DynamicTransferContext:
    def __init__(self, max_symbol: int, alpha: int = apex.PRIOR_SCALE) -> None:
        self.max_symbol = max_symbol
        self.alpha = alpha
        self.denominator = apex.PRIOR_DENOMINATOR
        self.counts = apex.FenwickModel([0] * (max_symbol + 1))

    @property
    def total(self) -> int:
        return self.denominator * self.counts.total + self.alpha * self.denominator

    def interval(self, symbol: int, prior_prefix: list[int]) -> tuple[int, int, int]:
        low = self.denominator * self.counts.prefix(symbol) + self.alpha * prior_prefix[symbol]
        high = self.denominator * self.counts.prefix(symbol + 1) + self.alpha * prior_prefix[symbol + 1]
        return low, high, self.total

    def find_symbol(self, value: int, prior_prefix: list[int]) -> int:
        lo = 0
        hi = self.max_symbol
        while lo < hi:
            mid = (lo + hi) // 2
            high = self.denominator * self.counts.prefix(mid + 1) + self.alpha * prior_prefix[mid + 1]
            if value < high:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def encode_symbol(self, coder: apex.ArithmeticEncoder, symbol: int, prior_prefix: list[int]) -> None:
        low, high, total = self.interval(symbol, prior_prefix)
        coder.encode(low, high, total)
        self.counts.update(symbol)

    def decode_symbol(self, decoder: apex.ArithmeticDecoder, prior_prefix: list[int]) -> int:
        value = decoder.value(self.total)
        symbol = self.find_symbol(value, prior_prefix)
        low, high, total = self.interval(symbol, prior_prefix)
        decoder.decode(low, high, total)
        self.counts.update(symbol)
        return symbol


class DynamicTransferBlendedPosterior:
    def __init__(self, max_symbol: int, fine_weight: int, parent_weight: int) -> None:
        self.max_symbol = max_symbol
        self.fine_weight = fine_weight
        self.parent_weight = parent_weight
        self.base_prior = apex.apex_prior_prefix(max_symbol)
        self.children: dict[tuple[int, ...], DynamicTransferContext] = {}
        self.parents: dict[tuple[int, ...], DynamicTransferContext] = {}

    def _child(self, key: tuple[int, ...]) -> DynamicTransferContext:
        model = self.children.get(key)
        if model is None:
            model = DynamicTransferContext(self.max_symbol)
            self.children[key] = model
        return model

    def _parent(self, key: tuple[int, ...]) -> DynamicTransferContext:
        model = self.parents.get(key)
        if model is None:
            model = DynamicTransferContext(self.max_symbol)
            self.parents[key] = model
        return model

    def _interval(
        self,
        child: DynamicTransferContext,
        parent: DynamicTransferContext,
        symbol: int,
        child_prior: list[int],
    ) -> tuple[int, int, int]:
        child_low, child_high, child_total = child.interval(symbol, child_prior)
        parent_low, parent_high, parent_total = parent.interval(symbol, self.base_prior)
        low = self.fine_weight * child_low * parent_total + self.parent_weight * parent_low * child_total
        high = self.fine_weight * child_high * parent_total + self.parent_weight * parent_high * child_total
        total = (self.fine_weight + self.parent_weight) * child_total * parent_total
        return low, high, total

    def encode_symbol(
        self,
        coder: apex.ArithmeticEncoder,
        key: tuple[int, ...],
        parent_key: tuple[int, ...],
        symbol: int,
        child_prior: list[int],
    ) -> None:
        child = self._child(key)
        parent = self._parent(parent_key)
        low, high, total = self._interval(child, parent, symbol, child_prior)
        coder.encode(low, high, total)
        child.counts.update(symbol)
        parent.counts.update(symbol)

    def decode_symbol(
        self,
        decoder: apex.ArithmeticDecoder,
        key: tuple[int, ...],
        parent_key: tuple[int, ...],
        child_prior: list[int],
    ) -> int:
        child = self._child(key)
        parent = self._parent(parent_key)
        total = (self.fine_weight + self.parent_weight) * child.total * parent.total
        value = decoder.value(total)
        lo = 0
        hi = self.max_symbol
        while lo < hi:
            mid = (lo + hi) // 2
            _, high, _ = self._interval(child, parent, mid, child_prior)
            if value < high:
                hi = mid
            else:
                lo = mid + 1
        symbol = lo
        low, high, total = self._interval(child, parent, symbol, child_prior)
        decoder.decode(low, high, total)
        child.counts.update(symbol)
        parent.counts.update(symbol)
        return symbol


def event_key_and_prior(
    scheme: apex.Scheme,
    config: PriorConfig,
    table: TransferPriorTable | None,
    channel_index: int,
    channel: np.ndarray,
    y: int,
    x: int,
    energy_value: int,
    unitary_value: int,
) -> tuple[tuple[int, ...], tuple[int, ...], list[int] | None]:
    ctx, grad = apex.pixel_context_and_gradient(channel, y, x)
    key = apex.context_key(scheme, channel_index, ctx, grad, energy_value, unitary_value, y)
    parent_key = apex.parent_context_key(scheme, channel_index, ctx, energy_value)
    prior = None
    if config.model_id in (MODEL_HARD_RUNG_CONTEXT, MODEL_SOFT_RAMANUJAN, MODEL_SHUFFLED_RAMANUJAN):
        rung = rung_at(x, y, config.conductor_modulus, config.rung_mode)
        if table is None:
            raise RuntimeError("missing transfer table")
        if config.model_id == MODEL_HARD_RUNG_CONTEXT:
            key = (table.dominant_conductor(rung),) + key
        else:
            prior = table.prior_prefix(rung)
    return key, parent_key, prior


def encode_entropy_e29(
    planes: apex.EncodedPlanes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    config: PriorConfig,
) -> bytes:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    table = None
    if config.model_id != MODEL_BASELINE:
        table = TransferPriorTable(
            planes.max_symbol,
            config.conductor_modulus,
            config.mix_num,
            config.mix_den,
            shuffled=(config.model_id == MODEL_SHUFFLED_RAMANUJAN),
        )
    if config.model_id in (MODEL_SOFT_RAMANUJAN, MODEL_SHUFFLED_RAMANUJAN):
        if not scheme.blend_parent:
            raise ValueError("E29 dynamic prior currently expects a blended scheme")
        posterior: apex.BlendedApexPosterior | DynamicTransferBlendedPosterior = DynamicTransferBlendedPosterior(
            planes.max_symbol,
            scheme.fine_weight,
            scheme.parent_weight,
        )
    elif scheme.blend_parent:
        posterior = apex.BlendedApexPosterior(planes.max_symbol, scheme.fine_weight, scheme.parent_weight)
    else:
        posterior = apex.FractionalApexPosterior(planes.max_symbol)

    sign_counts: dict[tuple[int, ...], list[int]] = {}
    coder = apex.ArithmeticEncoder()
    for channel_index, residuals in enumerate(planes.residuals):
        decoded_prefix = np.zeros((height, width), dtype=np.int32)
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                pred_id = planes.predictors[tile_index]
                energy_value = planes.energy[tile_index] if scheme.use_energy else 0
                unitary_value = planes.unitary[tile_index] if scheme.use_unitary else 0
                key, parent_key, prior = event_key_and_prior(
                    scheme,
                    config,
                    table,
                    channel_index,
                    decoded_prefix,
                    y,
                    x,
                    energy_value,
                    unitary_value,
                )
                prediction = apex.predictor_value(pred_id, decoded_prefix, y, x)
                residual_value = int(residuals[y, x])
                decoded_prefix[y, x] = prediction + residual_value
                symbol = abs(residual_value) if scheme.split_sign else sigi.zigzag(residual_value)
                if isinstance(posterior, DynamicTransferBlendedPosterior):
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
    return coder.finish()


def decode_entropy_e29(
    entropy: bytes,
    width: int,
    height: int,
    scheme: apex.Scheme,
    max_symbol: int,
    predictors: bytes,
    energy: bytes,
    unitary: bytes,
    config: PriorConfig,
) -> list[np.ndarray]:
    tiles_x, _, tile_count = apex.tile_grid(width, height)
    table = None
    if config.model_id != MODEL_BASELINE:
        table = TransferPriorTable(
            max_symbol,
            config.conductor_modulus,
            config.mix_num,
            config.mix_den,
            shuffled=(config.model_id == MODEL_SHUFFLED_RAMANUJAN),
        )
    if config.model_id in (MODEL_SOFT_RAMANUJAN, MODEL_SHUFFLED_RAMANUJAN):
        posterior: apex.BlendedApexPosterior | DynamicTransferBlendedPosterior = DynamicTransferBlendedPosterior(
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
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                energy_value = energy[tile_index] if scheme.use_energy else 0
                unitary_value = unitary[tile_index] if scheme.use_unitary else 0
                key, parent_key, prior = event_key_and_prior(
                    scheme,
                    config,
                    table,
                    channel_index,
                    channel,
                    y,
                    x,
                    energy_value,
                    unitary_value,
                )
                if isinstance(posterior, DynamicTransferBlendedPosterior):
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
        channels.append(channel)
    return channels


def encode_image_bytes_e29(
    rgb: bytes,
    width: int,
    height: int,
    transform: str,
    scheme_id: int,
    config: PriorConfig,
    planes: apex.EncodedPlanes | None = None,
) -> tuple[bytes, dict[str, object]]:
    scheme = apex.SCHEMES[scheme_id]
    residual_start = time.perf_counter()
    if planes is None:
        planes = apex.build_residual_planes(rgb, width, height, transform, scheme)
    residual_s = time.perf_counter() - residual_start
    entropy_start = time.perf_counter()
    entropy = encode_entropy_e29(planes, width, height, scheme, config)
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
    header += cell_song_poc.put_varint(config.conductor_modulus)
    header += cell_song_poc.put_varint(config.mix_num)
    header += cell_song_poc.put_varint(config.mix_den)
    header.append({"x": 0, "y": 1, "diag": 2, "tile": 3, "linear": 4}[config.rung_mode])
    header += cell_song_poc.put_varint(planes.max_symbol)
    header += cell_song_poc.put_varint(len(packed_predictors))
    header += packed_predictors
    header += cell_song_poc.put_varint(len(packed_energy))
    header += packed_energy
    header += cell_song_poc.put_varint(len(packed_unitary))
    header += packed_unitary

    blob = bytes(header) + entropy
    return blob, {
        "codec": "SR29",
        "model": MODEL_NAMES[config.model_id],
        "transform": transform,
        "scheme": scheme.name,
        "conductor_modulus": config.conductor_modulus,
        "mix": f"{config.mix_num}/{config.mix_den}",
        "rung_mode": config.rung_mode,
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
    }


def decode_image_bytes_e29(blob: bytes) -> tuple[bytes, int, int, dict[str, object]]:
    if not blob.startswith(MAGIC):
        raise sigi.SimplicialImageError("bad E29 magic")
    offset = len(MAGIC)
    version = blob[offset]
    offset += 1
    if version != VERSION:
        raise sigi.SimplicialImageError(f"unsupported E29 version {version}")
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
    conductor_modulus, offset = cell_song_poc.get_varint(blob, offset)
    mix_num, offset = cell_song_poc.get_varint(blob, offset)
    mix_den, offset = cell_song_poc.get_varint(blob, offset)
    rung_mode = {0: "x", 1: "y", 2: "diag", 3: "tile", 4: "linear"}[blob[offset]]
    offset += 1
    config = PriorConfig(model_id, conductor_modulus, mix_num, mix_den, rung_mode)
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
    channels = decode_entropy_e29(entropy, width, height, scheme, max_symbol, predictors, energy, unitary, config)
    rgb = apex.inverse_transform(channels, transform)
    actual_crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if actual_crc != expected_crc:
        raise sigi.SimplicialImageError("CRC mismatch after E29 decode")
    return rgb, width, height, {
        "codec": "SR29",
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
    as_float = float(value)
    den = 1000
    return round(as_float * den), den


def benchmark_image(
    path: Path,
    crop_size: int,
    transform: str,
    scheme_name: str,
    conductor_modulus: int,
    rung_modes: list[str],
    mixes: list[tuple[int, int]],
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

    configs: list[PriorConfig] = [PriorConfig(MODEL_BASELINE, conductor_modulus, 0, 1, "tile")]
    for rung_mode in rung_modes:
        configs.append(PriorConfig(MODEL_HARD_RUNG_CONTEXT, conductor_modulus, 0, 1, rung_mode))
        for mix_num, mix_den in mixes:
            configs.append(PriorConfig(MODEL_SOFT_RAMANUJAN, conductor_modulus, mix_num, mix_den, rung_mode))
            configs.append(PriorConfig(MODEL_SHUFFLED_RAMANUJAN, conductor_modulus, mix_num, mix_den, rung_mode))

    rows = []
    seen: set[tuple[int, int, int, str]] = set()
    for config in configs:
        key = (config.model_id, config.mix_num, config.mix_den, config.rung_mode)
        if key in seen:
            continue
        seen.add(key)
        print(
            f"E29 {MODEL_NAMES[config.model_id]} mix={config.mix_num}/{config.mix_den} mode={config.rung_mode}",
            file=sys.stderr,
        )
        start = time.perf_counter()
        blob, encode_stats = encode_image_bytes_e29(rgb, width, height, transform, scheme_id, config, planes=planes)
        encode_stats["shared_residual_build_s"] = residual_build_s
        encode_s = time.perf_counter() - start
        decode_start = time.perf_counter()
        decoded, decoded_width, decoded_height, decode_stats = decode_image_bytes_e29(blob)
        decode_s = time.perf_counter() - decode_start
        ok = decoded == rgb and decoded_width == width and decoded_height == height
        if artifact_dir is not None:
            artifact_dir.mkdir(parents=True, exist_ok=True)
            safe_model = MODEL_NAMES[config.model_id].replace("-", "_")
            stem = path.stem.replace(" ", "_")
            out = artifact_dir / (
                f"{stem}_{crop_size}_e29_{safe_model}_m{config.mix_num}-{config.mix_den}_{config.rung_mode}.sr29"
            )
            out.write_bytes(blob)
        rows.append(
            {
                "model": MODEL_NAMES[config.model_id],
                "mix": f"{config.mix_num}/{config.mix_den}",
                "rung_mode": config.rung_mode,
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
        "conductor_modulus": conductor_modulus,
        "rows": rows,
    }


def write_report(json_path: Path, report_path: Path) -> None:
    docs = json.loads(json_path.read_text(encoding="utf-8"))
    lines = [
        "# E29 Ramanujan Transfer Prior",
        "",
        "E29 tests the P5 reading in codec form: the conductor boundary should govern the entropy prior without being transmitted as a dense command map.",
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
            f"- conductor modulus: `{doc['conductor_modulus']}`",
            f"- WebP lossless: `{doc['webp_lossless_bytes']:,}` bytes",
            f"- E29 baseline: `{baseline['bytes']:,}` bytes",
            "",
            "| rank | model | mix | rung mode | bytes | vs E29 baseline | vs WebP | roundtrip |",
            "|---:|---|---:|---|---:|---:|---:|---|",
        ]
        for rank, row in enumerate(doc["rows"], start=1):
            lines.append(
                f"| {rank} | {row['model']} | {row['mix']} | {row['rung_mode']} | "
                f"{row['bytes']:,} | {row['bytes'] - baseline['bytes']:+,} | "
                f"{row['delta_vs_webp']:+,} | {row['roundtrip_ok']} |"
            )
        best = doc["rows"][0]
        lines += [
            "",
            "## Interpretation",
            "",
            f"The best E29 row is `{best['model']}` with mix `{best['mix']}` and rung mode `{best['rung_mode']}`, at `{best['bytes']:,}` bytes.",
            "",
            "The key comparison is against both the baseline and the shuffled control. A genuine Ramanujan-transfer effect should beat the baseline and also beat a prior with the same mass histogram assigned to the wrong conductor packets.",
            "",
        ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--transform", default="r-gr-bg", choices=sorted(apex.TRANSFORM_IDS))
    parser.add_argument("--scheme", default="ch-ctx-energy-unitary-split-blend71-apex128", choices=sorted(apex.SCHEME_IDS))
    parser.add_argument("--conductor-modulus", type=int, default=30)
    parser.add_argument("--rung-modes", default="tile,x")
    parser.add_argument("--mixes", default="1/4,1/2,3/4")
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/e29_ramanujan_transfer_prior.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/e29_ramanujan_transfer_prior.md"))
    parser.add_argument("--write-artifacts", action="store_true")
    args = parser.parse_args(argv)

    rung_modes = [item.strip() for item in args.rung_modes.split(",") if item.strip()]
    mixes = [parse_mix(item.strip()) for item in args.mixes.split(",") if item.strip()]
    rows = []
    artifact_dir = args.json.parent if args.write_artifacts else None
    for path in args.images:
        rows.append(
            benchmark_image(
                path,
                args.crop_size,
                args.transform,
                args.scheme,
                args.conductor_modulus,
                rung_modes,
                mixes,
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
            f"mix={best['mix']} mode={best['rung_mode']} webp={doc['webp_lossless_bytes']:,} "
            f"delta={best['delta_vs_webp']:+,} roundtrip={best['roundtrip_ok']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
