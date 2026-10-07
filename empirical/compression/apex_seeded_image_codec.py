#!/usr/bin/env python3
"""Round-trippable Apex-seeded simplicial image codec experiment.

This turns the prior estimator into an actual byte stream:

    reversible color gauge
    -> stored local predictor gauges
    -> exact integer residuals
    -> adaptive arithmetic coding seeded by a deterministic Apex prior.

It is intentionally experimental. Metadata is stored plainly so the first real
test is honest and easy to audit; packing predictor/packet side data can come
after the recovery contract is nailed down.
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

import benchmark_mined_strings_vs_webp as mined
import benchmark_sigi_vs_webp_fast as fast
import benchmark_subtile_transport_vs_webp as subtile
import cell_song_poc
import simplicial_image_codec as sigi


MAGIC = b"SIGA"
VERSION = 2
PRIOR_SCALE = 128
PRIOR_DENOMINATOR = 1 << 24

TRANSFORM_IDS = {
    "g-bg-ravg": 0,
    "g-rg-bavg": 1,
    "r-gr-bavg": 2,
    "b-rb-gavg": 3,
    "ycocg": 4,
    "green16": 5,
    "rgb": 6,
    "r-gr-bg": 7,
    "r-gr-bmix-a": 8,
    "r-gr-bmix-b": 9,
}
ID_TRANSFORMS = {value: key for key, value in TRANSFORM_IDS.items()}

PRED_LEFT2 = 22
PRED_UP2 = 23
PRED_BILINEAR2 = 24
PRED_LEFT_STRONG = 25
PRED_UP_STRONG = 26
APEX_PREDICTORS = sigi.PREDICTORS + (
    PRED_LEFT2,
    PRED_UP2,
    PRED_BILINEAR2,
    PRED_LEFT_STRONG,
    PRED_UP_STRONG,
)


@dataclass(frozen=True)
class Scheme:
    name: str
    use_grad: bool = False
    use_energy: bool = False
    use_unitary: bool = False
    use_y_phase4: bool = False
    split_sign: bool = False
    blend_parent: bool = False
    fine_weight: int = 3
    parent_weight: int = 1
    parent_kind: str = "base"


SCHEMES = {
    0: Scheme("ch-ctx-apex128"),
    1: Scheme("ch-ctx-energy-apex128", use_energy=True),
    2: Scheme("ch-ctx-energy-unitary-apex128", use_energy=True, use_unitary=True),
    3: Scheme("ch-ctx-grad-apex128", use_grad=True),
    4: Scheme("ch-ctx-grad-energy-unitary-apex128", use_grad=True, use_energy=True, use_unitary=True),
    5: Scheme(
        "ch-ctx-energy-unitary-blend31-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=3,
        parent_weight=1,
    ),
    6: Scheme(
        "ch-ctx-energy-unitary-blend11-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=1,
        parent_weight=1,
    ),
    7: Scheme(
        "ch-ctx-energy-unitary-blend13-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=1,
        parent_weight=3,
    ),
    8: Scheme(
        "ch-ctx-energy-unitary-eblend31-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=3,
        parent_weight=1,
        parent_kind="energy",
    ),
    9: Scheme(
        "ch-ctx-energy-unitary-eblend11-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=1,
        parent_weight=1,
        parent_kind="energy",
    ),
    10: Scheme(
        "ch-ctx-energy-unitary-blend71-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=7,
        parent_weight=1,
    ),
    11: Scheme(
        "ch-ctx-energy-unitary-blend151-apex128",
        use_energy=True,
        use_unitary=True,
        blend_parent=True,
        fine_weight=15,
        parent_weight=1,
    ),
    12: Scheme(
        "ch-ctx-energy-unitary-yphase4-blend31-apex128",
        use_energy=True,
        use_unitary=True,
        use_y_phase4=True,
        blend_parent=True,
        fine_weight=3,
        parent_weight=1,
    ),
    13: Scheme(
        "ch-ctx-energy-unitary-yphase4-blend71-apex128",
        use_energy=True,
        use_unitary=True,
        use_y_phase4=True,
        blend_parent=True,
        fine_weight=7,
        parent_weight=1,
    ),
    14: Scheme(
        "ch-ctx-energy-unitary-yphase4-blend11-apex128",
        use_energy=True,
        use_unitary=True,
        use_y_phase4=True,
        blend_parent=True,
        fine_weight=1,
        parent_weight=1,
    ),
    15: Scheme(
        "ch-ctx-energy-unitary-split-apex128",
        use_energy=True,
        use_unitary=True,
        split_sign=True,
    ),
    16: Scheme(
        "ch-ctx-energy-unitary-split-blend31-apex128",
        use_energy=True,
        use_unitary=True,
        split_sign=True,
        blend_parent=True,
        fine_weight=3,
        parent_weight=1,
    ),
    17: Scheme(
        "ch-ctx-energy-unitary-split-blend71-apex128",
        use_energy=True,
        use_unitary=True,
        split_sign=True,
        blend_parent=True,
        fine_weight=7,
        parent_weight=1,
    ),
}
SCHEME_IDS = {scheme.name: scheme_id for scheme_id, scheme in SCHEMES.items()}


class BitOut:
    def __init__(self) -> None:
        self.data = bytearray()
        self.cur = 0
        self.nbits = 0

    def write_bit(self, bit: int) -> None:
        self.cur = (self.cur << 1) | (bit & 1)
        self.nbits += 1
        if self.nbits == 8:
            self.data.append(self.cur)
            self.cur = 0
            self.nbits = 0

    def finish(self) -> bytes:
        if self.nbits:
            self.cur <<= 8 - self.nbits
            self.data.append(self.cur)
            self.cur = 0
            self.nbits = 0
        return bytes(self.data)


class BitIn:
    def __init__(self, data: bytes) -> None:
        self.data = data
        self.byte_pos = 0
        self.bit_pos = 0

    def read_bit(self) -> int:
        if self.byte_pos >= len(self.data):
            return 0
        bit = (self.data[self.byte_pos] >> (7 - self.bit_pos)) & 1
        self.bit_pos += 1
        if self.bit_pos == 8:
            self.byte_pos += 1
            self.bit_pos = 0
        return bit


class FenwickModel:
    def __init__(self, base: list[int]) -> None:
        self.n = len(base)
        self.tree = [0] + base[:]
        for index in range(1, self.n + 1):
            parent = index + (index & -index)
            if parent <= self.n:
                self.tree[parent] += self.tree[index]
        self.total = sum(base)

    def prefix(self, count: int) -> int:
        total = 0
        index = count
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def interval(self, symbol: int) -> tuple[int, int, int]:
        low = self.prefix(symbol)
        high = self.prefix(symbol + 1)
        return low, high, self.total

    def frequency(self, symbol: int) -> int:
        return self.prefix(symbol + 1) - self.prefix(symbol)

    def update(self, symbol: int) -> None:
        index = symbol + 1
        while index <= self.n:
            self.tree[index] += 1
            index += index & -index
        self.total += 1

    def find_symbol(self, value: int) -> int:
        target = value + 1
        index = 0
        bit = 1 << (self.n.bit_length() - 1)
        while bit:
            nxt = index + bit
            if nxt <= self.n and self.tree[nxt] < target:
                index = nxt
                target -= self.tree[nxt]
            bit >>= 1
        return index


class ApexPosterior:
    def __init__(self, max_symbol: int, prior_scale: int = PRIOR_SCALE) -> None:
        self.max_symbol = max_symbol
        self.base = [
            max(1, int(round(prior_scale / ((symbol + 1) * (symbol + 2)))))
            for symbol in range(max_symbol + 1)
        ]
        self.contexts: dict[tuple[int, ...], FenwickModel] = {}

    def context(self, key: tuple[int, ...]) -> FenwickModel:
        model = self.contexts.get(key)
        if model is None:
            model = FenwickModel(self.base)
            self.contexts[key] = model
        return model


class EscapeContext:
    def __init__(self, max_symbol: int, alpha: int = PRIOR_SCALE) -> None:
        self.max_symbol = max_symbol
        self.alpha = alpha
        self.counts = FenwickModel([0] * (max_symbol + 1))

    @property
    def total(self) -> int:
        return self.alpha + self.counts.total

    def encode_symbol(self, coder: ArithmeticEncoder, symbol: int) -> None:
        count = self.counts.frequency(symbol)
        total = self.total
        if count:
            low = self.alpha + self.counts.prefix(symbol)
            coder.encode(low, low + count, total)
        else:
            coder.encode(0, self.alpha, total)
            encode_gamma(coder, symbol + 1)
        self.counts.update(symbol)

    def decode_symbol(self, decoder: ArithmeticDecoder) -> int:
        value = decoder.value(self.total)
        if value < self.alpha:
            decoder.decode(0, self.alpha, self.total)
            symbol = decode_gamma(decoder) - 1
            if symbol < 0 or symbol > self.max_symbol:
                raise sigi.SimplicialImageError("escaped symbol outside alphabet")
        else:
            target = value - self.alpha
            symbol = self.counts.find_symbol(target)
            low = self.alpha + self.counts.prefix(symbol)
            high = low + self.counts.frequency(symbol)
            decoder.decode(low, high, self.total)
        self.counts.update(symbol)
        return symbol


class EscapePosterior:
    def __init__(self, max_symbol: int, alpha: int = PRIOR_SCALE) -> None:
        self.max_symbol = max_symbol
        self.alpha = alpha
        self.contexts: dict[tuple[int, ...], EscapeContext] = {}

    def context(self, key: tuple[int, ...]) -> EscapeContext:
        model = self.contexts.get(key)
        if model is None:
            model = EscapeContext(self.max_symbol, self.alpha)
            self.contexts[key] = model
        return model


def apex_prior_prefix(max_symbol: int, denominator: int = PRIOR_DENOMINATOR) -> list[int]:
    """Integer CDF for q(n)=1/((n+1)(n+2)), truncated to 0..max_symbol."""
    prefix = [0]
    normalizer_num = max_symbol + 2
    normalizer_den = max_symbol + 1
    for count in range(1, max_symbol + 2):
        # sum_{n=0}^{count-1} q(n) = count / (count + 1)
        value = round(denominator * count * normalizer_num / ((count + 1) * normalizer_den))
        prefix.append(max(prefix[-1] + 1, min(denominator, int(value))))
    prefix[-1] = denominator
    return prefix


class FractionalApexContext:
    def __init__(
        self,
        max_symbol: int,
        prior_prefix: list[int],
        alpha: int = PRIOR_SCALE,
        denominator: int = PRIOR_DENOMINATOR,
    ) -> None:
        self.max_symbol = max_symbol
        self.prior_prefix = prior_prefix
        self.alpha = alpha
        self.denominator = denominator
        self.counts = FenwickModel([0] * (max_symbol + 1))

    @property
    def total(self) -> int:
        return self.denominator * self.counts.total + self.alpha * self.denominator

    def interval(self, symbol: int) -> tuple[int, int, int]:
        low = self.denominator * self.counts.prefix(symbol) + self.alpha * self.prior_prefix[symbol]
        high = self.denominator * self.counts.prefix(symbol + 1) + self.alpha * self.prior_prefix[symbol + 1]
        return low, high, self.total

    def find_symbol(self, value: int) -> int:
        lo = 0
        hi = self.max_symbol
        while lo < hi:
            mid = (lo + hi) // 2
            high = (
                self.denominator * self.counts.prefix(mid + 1)
                + self.alpha * self.prior_prefix[mid + 1]
            )
            if value < high:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def encode_symbol(self, coder: ArithmeticEncoder, symbol: int) -> None:
        low, high, total = self.interval(symbol)
        coder.encode(low, high, total)
        self.counts.update(symbol)

    def decode_symbol(self, decoder: ArithmeticDecoder) -> int:
        value = decoder.value(self.total)
        symbol = self.find_symbol(value)
        low, high, total = self.interval(symbol)
        decoder.decode(low, high, total)
        self.counts.update(symbol)
        return symbol


class FractionalApexPosterior:
    def __init__(self, max_symbol: int, alpha: int = PRIOR_SCALE) -> None:
        self.max_symbol = max_symbol
        self.alpha = alpha
        self.prior_prefix = apex_prior_prefix(max_symbol)
        self.contexts: dict[tuple[int, ...], FractionalApexContext] = {}

    def context(self, key: tuple[int, ...]) -> FractionalApexContext:
        model = self.contexts.get(key)
        if model is None:
            model = FractionalApexContext(self.max_symbol, self.prior_prefix, self.alpha)
            self.contexts[key] = model
        return model


class BlendedApexPosterior:
    def __init__(self, max_symbol: int, fine_weight: int, parent_weight: int, alpha: int = PRIOR_SCALE) -> None:
        self.max_symbol = max_symbol
        self.fine_weight = fine_weight
        self.parent_weight = parent_weight
        self.alpha = alpha
        self.prior_prefix = apex_prior_prefix(max_symbol)
        self.children: dict[tuple[int, ...], FractionalApexContext] = {}
        self.parents: dict[tuple[int, ...], FractionalApexContext] = {}

    def _child(self, key: tuple[int, ...]) -> FractionalApexContext:
        model = self.children.get(key)
        if model is None:
            model = FractionalApexContext(self.max_symbol, self.prior_prefix, self.alpha)
            self.children[key] = model
        return model

    def _parent(self, key: tuple[int, ...]) -> FractionalApexContext:
        model = self.parents.get(key)
        if model is None:
            model = FractionalApexContext(self.max_symbol, self.prior_prefix, self.alpha)
            self.parents[key] = model
        return model

    def _interval(
        self,
        child: FractionalApexContext,
        parent: FractionalApexContext,
        symbol: int,
    ) -> tuple[int, int, int]:
        child_low, child_high, child_total = child.interval(symbol)
        parent_low, parent_high, parent_total = parent.interval(symbol)
        low = (
            self.fine_weight * child_low * parent_total
            + self.parent_weight * parent_low * child_total
        )
        high = (
            self.fine_weight * child_high * parent_total
            + self.parent_weight * parent_high * child_total
        )
        total = (self.fine_weight + self.parent_weight) * child_total * parent_total
        return low, high, total

    def encode_symbol(self, coder: ArithmeticEncoder, key: tuple[int, ...], parent_key: tuple[int, ...], symbol: int) -> None:
        child = self._child(key)
        parent = self._parent(parent_key)
        low, high, total = self._interval(child, parent, symbol)
        coder.encode(low, high, total)
        child.counts.update(symbol)
        parent.counts.update(symbol)

    def decode_symbol(self, decoder: ArithmeticDecoder, key: tuple[int, ...], parent_key: tuple[int, ...]) -> int:
        child = self._child(key)
        parent = self._parent(parent_key)
        total = (self.fine_weight + self.parent_weight) * child.total * parent.total
        value = decoder.value(total)
        lo = 0
        hi = self.max_symbol
        while lo < hi:
            mid = (lo + hi) // 2
            _, high, _ = self._interval(child, parent, mid)
            if value < high:
                hi = mid
            else:
                lo = mid + 1
        symbol = lo
        low, high, total = self._interval(child, parent, symbol)
        decoder.decode(low, high, total)
        child.counts.update(symbol)
        parent.counts.update(symbol)
        return symbol


class ArithmeticEncoder:
    MASK = (1 << 128) - 1
    HALF = 1 << 127
    FIRST_QTR = 1 << 126
    THIRD_QTR = 3 << 126

    def __init__(self) -> None:
        self.low = 0
        self.high = self.MASK
        self.pending = 0
        self.out = BitOut()

    def _bit_plus_pending(self, bit: int) -> None:
        self.out.write_bit(bit)
        inverse = 1 - bit
        while self.pending:
            self.out.write_bit(inverse)
            self.pending -= 1

    def encode(self, cum_low: int, cum_high: int, total: int) -> None:
        width = self.high - self.low + 1
        self.high = self.low + (width * cum_high // total) - 1
        self.low = self.low + (width * cum_low // total)
        while True:
            if self.high < self.HALF:
                self._bit_plus_pending(0)
            elif self.low >= self.HALF:
                self._bit_plus_pending(1)
                self.low -= self.HALF
                self.high -= self.HALF
            elif self.low >= self.FIRST_QTR and self.high < self.THIRD_QTR:
                self.pending += 1
                self.low -= self.FIRST_QTR
                self.high -= self.FIRST_QTR
            else:
                break
            self.low = (self.low << 1) & self.MASK
            self.high = ((self.high << 1) | 1) & self.MASK

    def finish(self) -> bytes:
        self.pending += 1
        if self.low < self.FIRST_QTR:
            self._bit_plus_pending(0)
        else:
            self._bit_plus_pending(1)
        return self.out.finish()


class ArithmeticDecoder:
    MASK = (1 << 128) - 1
    HALF = 1 << 127
    FIRST_QTR = 1 << 126
    THIRD_QTR = 3 << 126

    def __init__(self, data: bytes) -> None:
        self.low = 0
        self.high = self.MASK
        self.reader = BitIn(data)
        self.code = 0
        for _ in range(128):
            self.code = ((self.code << 1) | self.reader.read_bit()) & self.MASK

    def value(self, total: int) -> int:
        width = self.high - self.low + 1
        return ((self.code - self.low + 1) * total - 1) // width

    def decode(self, cum_low: int, cum_high: int, total: int) -> None:
        width = self.high - self.low + 1
        self.high = self.low + (width * cum_high // total) - 1
        self.low = self.low + (width * cum_low // total)
        while True:
            if self.high < self.HALF:
                pass
            elif self.low >= self.HALF:
                self.low -= self.HALF
                self.high -= self.HALF
                self.code -= self.HALF
            elif self.low >= self.FIRST_QTR and self.high < self.THIRD_QTR:
                self.low -= self.FIRST_QTR
                self.high -= self.FIRST_QTR
                self.code -= self.FIRST_QTR
            else:
                break
            self.low = (self.low << 1) & self.MASK
            self.high = ((self.high << 1) | 1) & self.MASK
            self.code = ((self.code << 1) | self.reader.read_bit()) & self.MASK


def encode_binary_bit(coder: ArithmeticEncoder, bit: int) -> None:
    coder.encode(bit & 1, (bit & 1) + 1, 2)


def decode_binary_bit(decoder: ArithmeticDecoder) -> int:
    bit = decoder.value(2)
    decoder.decode(bit, bit + 1, 2)
    return bit


def encode_gamma(coder: ArithmeticEncoder, value: int) -> None:
    if value <= 0:
        raise ValueError("gamma code value must be positive")
    bits = value.bit_length()
    for _ in range(bits - 1):
        encode_binary_bit(coder, 0)
    encode_binary_bit(coder, 1)
    for shift in range(bits - 2, -1, -1):
        encode_binary_bit(coder, (value >> shift) & 1)


def decode_gamma(decoder: ArithmeticDecoder) -> int:
    zeros = 0
    while decode_binary_bit(decoder) == 0:
        zeros += 1
        if zeros > 31:
            raise sigi.SimplicialImageError("gamma code too long")
    value = 1 << zeros
    for shift in range(zeros - 1, -1, -1):
        value |= decode_binary_bit(decoder) << shift
    return value


def unzigzag(value: int) -> int:
    return (value >> 1) if value % 2 == 0 else -((value + 1) >> 1)


def pack_values(values: bytes, bits: int) -> bytes:
    out = BitOut()
    mask = (1 << bits) - 1
    for value in values:
        if value & ~mask:
            raise ValueError(f"value {value} does not fit in {bits} bits")
        for shift in range(bits - 1, -1, -1):
            out.write_bit((value >> shift) & 1)
    return out.finish()


def unpack_values(blob: bytes, bits: int, count: int) -> bytes:
    reader = BitIn(blob)
    values = bytearray()
    for _ in range(count):
        value = 0
        for _ in range(bits):
            value = (value << 1) | reader.read_bit()
        values.append(value)
    return bytes(values)


def tile_grid(width: int, height: int) -> tuple[int, int, int]:
    tiles_x = (width + sigi.TILE - 1) // sigi.TILE
    tiles_y = (height + sigi.TILE - 1) // sigi.TILE
    return tiles_x, tiles_y, tiles_x * tiles_y


def predictor_value(
    pred_id: int,
    channel: np.ndarray,
    y: int,
    x: int,
) -> int:
    height, width = channel.shape
    left = int(channel[y, x - 1]) if x > 0 else 0
    left2 = int(channel[y, x - 2]) if x > 1 else left
    up = int(channel[y - 1, x]) if y > 0 else 0
    up2 = int(channel[y - 2, x]) if y > 1 else up
    up_left = int(channel[y - 1, x - 1]) if y > 0 and x > 0 else 0
    if y > 0 and x + 1 < width and ((x + 1) % sigi.TILE) != 0:
        up_right = int(channel[y - 1, x + 1])
    else:
        up_right = up
    if pred_id == sigi.PRED_ZERO:
        return 0
    if pred_id == sigi.PRED_LEFT:
        return left
    if pred_id == sigi.PRED_UP:
        return up
    if pred_id == sigi.PRED_AVG:
        return (left + up) // 2
    plane = left + up - up_left
    if pred_id == sigi.PRED_MEDIAN:
        if up_left >= max(left, up):
            return min(left, up)
        if up_left <= min(left, up):
            return max(left, up)
        return plane
    if pred_id == sigi.PRED_PAETH:
        pa = abs(plane - left)
        pb = abs(plane - up)
        pc = abs(plane - up_left)
        return left if pa <= pb and pa <= pc else (up if pb <= pc else up_left)
    if pred_id == sigi.PRED_PLANE:
        return plane
    if pred_id == sigi.PRED_LEFT_GRAD:
        return left + ((up - up_left) // 2)
    if pred_id == sigi.PRED_UP_GRAD:
        return up + ((left - up_left) // 2)
    if pred_id == sigi.PRED_LEFT_WEIGHT:
        return (3 * left + up) // 4
    if pred_id == sigi.PRED_UP_WEIGHT:
        return (left + 3 * up) // 4
    if pred_id == sigi.PRED_UP_RIGHT:
        return up_right
    if pred_id == sigi.PRED_LEFT_UP_RIGHT_AVG:
        return (left + up_right) // 2
    if pred_id == sigi.PRED_UP_UP_LEFT_AVG:
        return (up + up_left) // 2
    if pred_id == sigi.PRED_SELECT:
        return left if abs(plane - left) <= abs(plane - up) else up
    if pred_id == sigi.PRED_NE_PLANE:
        return left + up - up_right
    if pred_id == sigi.PRED_LEFT_UP_LEFT_AVG:
        return (left + up_left) // 2
    if pred_id == sigi.PRED_UP_UP_RIGHT_AVG:
        return (up + up_right) // 2
    if pred_id == sigi.PRED_LEFT_UP_UP_RIGHT_AVG:
        return (left + up + up_right) // 3
    if pred_id == sigi.PRED_FOUR_AVG:
        return (left + up + up_left + up_right) // 4
    if pred_id == sigi.PRED_LEFT2_UP_AVG:
        return (2 * left + up) // 3
    if pred_id == sigi.PRED_LEFT_UP2_AVG:
        return (left + 2 * up) // 3
    if pred_id == PRED_LEFT2:
        return 2 * left - left2
    if pred_id == PRED_UP2:
        return 2 * up - up2
    if pred_id == PRED_BILINEAR2:
        return ((2 * left - left2) + (2 * up - up2)) // 2
    if pred_id == PRED_LEFT_STRONG:
        return (7 * left + up) // 8
    if pred_id == PRED_UP_STRONG:
        return (left + 7 * up) // 8
    raise sigi.SimplicialImageError(f"bad predictor {pred_id}")


def pixel_context_and_gradient(channel: np.ndarray, y: int, x: int) -> tuple[int, int]:
    height, width = channel.shape
    left = int(channel[y, x - 1]) if x > 0 else 0
    up = int(channel[y - 1, x]) if y > 0 else 0
    up_left = int(channel[y - 1, x - 1]) if y > 0 and x > 0 else 0
    if y > 0 and x + 1 < width and ((x + 1) % sigi.TILE) != 0:
        up_right = int(channel[y - 1, x + 1])
    else:
        up_right = up
    gradient = abs(left - up) + abs(left - up_left) + abs(up - up_left) + abs(up - up_right)
    return int(np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right")), subtile.gradient_class(gradient)


def pixel_context(channel: np.ndarray, y: int, x: int) -> int:
    return pixel_context_and_gradient(channel, y, x)[0]


def shifted_left2_up2(channel: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    left = np.zeros_like(channel)
    left[:, 1:] = channel[:, :-1]
    left2 = left.copy()
    left2[:, 2:] = channel[:, :-2]
    up = np.zeros_like(channel)
    up[1:, :] = channel[:-1, :]
    up2 = up.copy()
    up2[2:, :] = channel[:-2, :]
    return left2, up2


def predictor_tile_ext(
    pred_id: int,
    left: np.ndarray,
    up: np.ndarray,
    up_left: np.ndarray,
    up_right: np.ndarray,
    left2: np.ndarray,
    up2: np.ndarray,
    ys: slice,
    xs: slice,
) -> np.ndarray:
    if pred_id in sigi.PREDICTORS:
        return fast.predictor_tile(pred_id, left, up, up_left, up_right, ys, xs)
    l = left[ys, xs]
    u = up[ys, xs]
    ll = left2[ys, xs]
    uu = up2[ys, xs]
    if pred_id == PRED_LEFT2:
        return 2 * l - ll
    if pred_id == PRED_UP2:
        return 2 * u - uu
    if pred_id == PRED_BILINEAR2:
        return ((2 * l - ll) + (2 * u - uu)) // 2
    if pred_id == PRED_LEFT_STRONG:
        return (7 * l + u) // 8
    if pred_id == PRED_UP_STRONG:
        return (l + 7 * u) // 8
    raise sigi.SimplicialImageError(f"bad predictor {pred_id}")


def inverse_transform(channels: list[np.ndarray], transform: str) -> bytes:
    c0, c1, c2 = channels
    if transform == "rgb":
        r, g, b = c0, c1, c2
    elif transform == "g-bg-ravg":
        g = c0
        b = c1 + g
        r = c2 + ((g + b) // 2)
    elif transform == "g-rg-bavg":
        g = c0
        r = c1 + g
        b = c2 + ((g + r) // 2)
    elif transform == "r-gr-bavg":
        r = c0
        g = c1 + r
        b = c2 + ((r + g) // 2)
    elif transform == "r-gr-bg":
        r = c0
        g = c1 + r
        b = c2 + g
    elif transform == "r-gr-bmix-a":
        r = c0
        g = c1 + r
        b = c2 + ((-10 * r + 42 * g) // 32)
    elif transform == "r-gr-bmix-b":
        r = c0
        g = c1 + r
        b = c2 + ((-12 * r + 44 * g) // 32)
    elif transform == "b-rb-gavg":
        b = c0
        r = c1 + b
        g = c2 + ((b + r) // 2)
    elif transform == "ycocg":
        y, co, cg = c0, c1, c2
        t = y - (cg >> 1)
        g = cg + t
        b = t - (co >> 1)
        r = co + b
    elif transform == "green16":
        g = c0
        r = c1 + ((16 * g) >> 5)
        b = c2 + g
    else:
        raise sigi.SimplicialImageError(f"unknown transform {transform}")
    arr = np.stack([r, g, b], axis=2)
    if np.any(arr < 0) or np.any(arr > 255):
        raise sigi.SimplicialImageError("inverse transform escaped byte range")
    return arr.astype(np.uint8).tobytes()


def context_key(
    scheme: Scheme,
    channel_index: int,
    ctx: int,
    grad: int,
    energy: int,
    unitary: int,
    y: int = 0,
) -> tuple[int, ...]:
    key: list[int] = [channel_index, ctx]
    if scheme.use_grad:
        key.append(grad)
    if scheme.use_energy:
        key.append(energy)
    if scheme.use_unitary:
        key.append(unitary)
    if scheme.use_y_phase4:
        key.append(y & 3)
    return tuple(key)


def parent_context_key(scheme: Scheme, channel_index: int, ctx: int, energy: int) -> tuple[int, ...]:
    if scheme.parent_kind == "energy":
        return channel_index, ctx, energy
    return channel_index, ctx


@dataclass
class EncodedPlanes:
    residuals: list[np.ndarray]
    predictors: bytes
    energy: bytes
    unitary: bytes
    max_symbol: int
    predictor_counts: dict[str, int]


def build_residual_planes(
    rgb: bytes,
    width: int,
    height: int,
    transform: str,
    scheme: Scheme,
) -> EncodedPlanes:
    channels = mined.transform_channels(rgb, width, height, transform)
    tiles_x, tiles_y, tile_count = tile_grid(width, height)
    predictor_bytes = bytearray()
    energy_bytes = bytearray()
    unitary_bytes = bytearray()
    residual_planes: list[np.ndarray] = []
    max_symbol = 0
    predictor_counts: Counter[str] = Counter()
    for channel in channels:
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        left2, up2 = shifted_left2_up2(channel)
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
                for pred_id in APEX_PREDICTORS:
                    residual = tile - predictor_tile_ext(pred_id, left, up, up_left, up_right, left2, up2, ys, xs)
                    bits = fast.best_context_rice_bits(fast.zigzag_np(residual), tile_contexts)
                    if best_bits is None or bits < best_bits:
                        best_pred = pred_id
                        best_residual = residual
                        best_bits = bits
                if best_residual is None:
                    raise RuntimeError("empty tile")
                pred_id = best_pred
                residual = best_residual
                predictor_bytes.append(pred_id)
                predictor_counts[f"pred-{pred_id}"] += 1
                residuals[ys, xs] = residual
                if scheme.use_energy:
                    energy_bytes.append(subtile.energy_class(float(np.mean(np.abs(residual)))))
                if scheme.use_unitary:
                    unitary_bytes.append(subtile.unitary_packet_class(residual))
        if predictor_bytes and len(predictor_bytes) % tile_count != 0:
            raise RuntimeError("predictor metadata misalignment")
        if scheme.split_sign:
            channel_max = int(np.max(np.abs(residuals)))
        else:
            channel_max = int(np.max(fast.zigzag_np(residuals)))
        max_symbol = max(max_symbol, channel_max)
        residual_planes.append(residuals)
    return EncodedPlanes(
        residuals=residual_planes,
        predictors=bytes(predictor_bytes),
        energy=bytes(energy_bytes),
        unitary=bytes(unitary_bytes),
        max_symbol=max_symbol,
        predictor_counts=dict(predictor_counts),
    )


def encode_entropy(
    planes: EncodedPlanes,
    width: int,
    height: int,
    scheme: Scheme,
) -> bytes:
    tiles_x, _, tile_count = tile_grid(width, height)
    posterior: FractionalApexPosterior | BlendedApexPosterior
    if scheme.blend_parent:
        posterior = BlendedApexPosterior(planes.max_symbol, scheme.fine_weight, scheme.parent_weight)
    else:
        posterior = FractionalApexPosterior(planes.max_symbol)
    sign_counts: dict[tuple[int, ...], list[int]] = defaultdict(lambda: [1, 1])
    coder = ArithmeticEncoder()
    pred_offset = energy_offset = unitary_offset = 0
    for channel_index, residuals in enumerate(planes.residuals):
        decoded_prefix = np.zeros((height, width), dtype=np.int32)
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                pred_id = planes.predictors[tile_index]
                ctx, grad = pixel_context_and_gradient(decoded_prefix, y, x)
                prediction = predictor_value(pred_id, decoded_prefix, y, x)
                decoded_prefix[y, x] = prediction + int(residuals[y, x])
                energy = planes.energy[tile_index] if scheme.use_energy else 0
                unitary = planes.unitary[tile_index] if scheme.use_unitary else 0
                key = context_key(scheme, channel_index, ctx, grad, energy, unitary, y)
                residual_value = int(residuals[y, x])
                symbol = abs(residual_value) if scheme.split_sign else sigi.zigzag(residual_value)
                if scheme.blend_parent:
                    assert isinstance(posterior, BlendedApexPosterior)
                    posterior.encode_symbol(coder, key, parent_context_key(scheme, channel_index, ctx, energy), symbol)
                else:
                    assert isinstance(posterior, FractionalApexPosterior)
                    posterior.context(key).encode_symbol(coder, symbol)
                if scheme.split_sign and symbol:
                    sign_key = key
                    counts = sign_counts[sign_key]
                    sign = 1 if residual_value < 0 else 0
                    total = counts[0] + counts[1]
                    low = counts[0] if sign else 0
                    high = low + counts[sign]
                    coder.encode(low, high, total)
                    counts[sign] += 1
    return coder.finish()


def encode_image_bytes(rgb: bytes, width: int, height: int, transform: str, scheme_id: int) -> tuple[bytes, dict[str, object]]:
    scheme = SCHEMES[scheme_id]
    planes = build_residual_planes(rgb, width, height, transform, scheme)
    entropy_start = time.perf_counter()
    entropy = encode_entropy(planes, width, height, scheme)
    entropy_s = time.perf_counter() - entropy_start
    packed_predictors = pack_values(planes.predictors, 5)
    packed_energy = pack_values(planes.energy, 3) if planes.energy else b""
    packed_unitary = pack_values(planes.unitary, 2) if planes.unitary else b""
    header = bytearray()
    header += MAGIC
    header.append(VERSION)
    header += cell_song_poc.put_varint(width)
    header += cell_song_poc.put_varint(height)
    header += int.to_bytes(binascii.crc32(rgb) & 0xFFFFFFFF, 4, "little")
    header.append(TRANSFORM_IDS[transform])
    header.append(scheme_id)
    header += cell_song_poc.put_varint(planes.max_symbol)
    header += cell_song_poc.put_varint(len(packed_predictors))
    header += packed_predictors
    header += cell_song_poc.put_varint(len(packed_energy))
    header += packed_energy
    header += cell_song_poc.put_varint(len(packed_unitary))
    header += packed_unitary
    blob = bytes(header) + entropy
    stats = {
        "transform": transform,
        "scheme": scheme.name,
        "bytes": len(blob),
        "header_metadata_bytes": len(header),
        "entropy_bytes": len(entropy),
        "predictor_metadata_bytes": len(packed_predictors),
        "energy_metadata_bytes": len(packed_energy),
        "unitary_metadata_bytes": len(packed_unitary),
        "max_symbol": planes.max_symbol,
        "entropy_encode_s": entropy_s,
        "predictors": planes.predictor_counts,
    }
    return blob, stats


def decode_image_bytes(blob: bytes) -> tuple[bytes, int, int, dict[str, object]]:
    if not blob.startswith(MAGIC):
        raise sigi.SimplicialImageError("bad Apex image magic")
    offset = len(MAGIC)
    version = blob[offset]
    offset += 1
    if version != VERSION:
        raise sigi.SimplicialImageError(f"unsupported version {version}")
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    expected_crc = int.from_bytes(blob[offset : offset + 4], "little")
    offset += 4
    transform_id = blob[offset]
    offset += 1
    scheme_id = blob[offset]
    offset += 1
    if transform_id not in ID_TRANSFORMS or scheme_id not in SCHEMES:
        raise sigi.SimplicialImageError("bad transform or scheme id")
    transform = ID_TRANSFORMS[transform_id]
    scheme = SCHEMES[scheme_id]
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

    tiles_x, _, tile_count = tile_grid(width, height)
    expected_tiles = tile_count * 3
    predictors = unpack_values(packed_predictors, 5, expected_tiles)
    energy = unpack_values(packed_energy, 3, expected_tiles) if scheme.use_energy else b""
    unitary = unpack_values(packed_unitary, 2, expected_tiles) if scheme.use_unitary else b""
    if len(predictors) != expected_tiles:
        raise sigi.SimplicialImageError("predictor metadata length mismatch")
    if scheme.use_energy and len(energy) != expected_tiles:
        raise sigi.SimplicialImageError("energy metadata length mismatch")
    if scheme.use_unitary and len(unitary) != expected_tiles:
        raise sigi.SimplicialImageError("unitary metadata length mismatch")

    decode_posterior: FractionalApexPosterior | BlendedApexPosterior
    if scheme.blend_parent:
        decode_posterior = BlendedApexPosterior(max_symbol, scheme.fine_weight, scheme.parent_weight)
    else:
        decode_posterior = FractionalApexPosterior(max_symbol)
    sign_counts: dict[tuple[int, ...], list[int]] = defaultdict(lambda: [1, 1])
    decoder = ArithmeticDecoder(entropy)
    channels: list[np.ndarray] = []
    for channel_index in range(3):
        channel = np.zeros((height, width), dtype=np.int32)
        for y in range(height):
            for x in range(width):
                tile_index = channel_index * tile_count + (y // sigi.TILE) * tiles_x + (x // sigi.TILE)
                ctx, grad = pixel_context_and_gradient(channel, y, x)
                energy_value = energy[tile_index] if scheme.use_energy else 0
                unitary_value = unitary[tile_index] if scheme.use_unitary else 0
                key = context_key(scheme, channel_index, ctx, grad, energy_value, unitary_value, y)
                if scheme.blend_parent:
                    assert isinstance(decode_posterior, BlendedApexPosterior)
                    symbol = decode_posterior.decode_symbol(
                        decoder,
                        key,
                        parent_context_key(scheme, channel_index, ctx, energy_value),
                    )
                else:
                    assert isinstance(decode_posterior, FractionalApexPosterior)
                    symbol = decode_posterior.context(key).decode_symbol(decoder)
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
                    residual = unzigzag(symbol)
                channel[y, x] = predictor_value(pred_id, channel, y, x) + residual
        channels.append(channel)
    rgb = inverse_transform(channels, transform)
    actual_crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if actual_crc != expected_crc:
        raise sigi.SimplicialImageError("CRC mismatch after Apex decode")
    stats = {
        "transform": transform,
        "scheme": scheme.name,
        "width": width,
        "height": height,
        "max_symbol": max_symbol,
        "metadata_bytes": offset,
        "entropy_bytes": len(entropy),
    }
    return rgb, width, height, stats


def webp_lossless_size(rgb: bytes, width: int, height: int) -> int:
    out = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(
        out,
        format="WEBP",
        lossless=True,
        quality=100,
        method=6,
    )
    return len(out.getvalue())


def benchmark_image(path: Path, crop_size: int, transform: str, scheme_name: str) -> dict[str, object]:
    with Image.open(path) as image:
        image = fast.center_crop(image.convert("RGB"), crop_size)
        width, height = image.size
        rgb = image.tobytes()
    scheme_id = SCHEME_IDS[scheme_name]
    start = time.perf_counter()
    encoded, encode_stats = encode_image_bytes(rgb, width, height, transform, scheme_id)
    encode_s = time.perf_counter() - start
    decode_start = time.perf_counter()
    decoded, decoded_width, decoded_height, decode_stats = decode_image_bytes(encoded)
    decode_s = time.perf_counter() - decode_start
    ok = decoded == rgb and decoded_width == width and decoded_height == height
    webp_size = webp_lossless_size(rgb, width, height)
    return {
        "file": str(path),
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "apex_bytes": len(encoded),
        "delta_vs_webp": len(encoded) - webp_size,
        "ratio_vs_webp": len(encoded) / webp_size,
        "roundtrip_ok": ok,
        "encode_s": encode_s,
        "decode_s": decode_s,
        "encode_stats": encode_stats,
        "decode_stats": decode_stats,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--crop-size", type=int, default=256)
    parser.add_argument("--transform", default="g-rg-bavg", choices=sorted(TRANSFORM_IDS))
    parser.add_argument("--scheme", default="ch-ctx-apex128", choices=sorted(SCHEME_IDS))
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/apex_seeded_roundtrip.json"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        sample = bytes((i * 17 + 3) % 256 for i in range(16 * 16 * 3))
        encoded, _ = encode_image_bytes(sample, 16, 16, "rgb", SCHEME_IDS["ch-ctx-apex128"])
        decoded, width, height, _ = decode_image_bytes(encoded)
        if decoded != sample or width != 16 or height != 16:
            raise SystemExit("self-test failed")
        print("self-test ok")
        return 0

    rows = []
    for path in args.images:
        print(f"roundtrip benchmarking {path}...", file=sys.stderr)
        rows.append(benchmark_image(path, args.crop_size, args.transform, args.scheme))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"wrote {args.json}")
    for row in rows:
        print(
            f"{Path(str(row['file'])).name}: apex={row['apex_bytes']:,} "
            f"webp={row['webp_lossless_bytes']:,} roundtrip={row['roundtrip_ok']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
