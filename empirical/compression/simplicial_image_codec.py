#!/usr/bin/env python3
"""Tiny lossless image codec inspired by T4 gauge removal.

This is a practical counterpoint to ``cell_song_image2d_poc.py``. Instead of
solving expensive spectral interval programs, it removes cheap local gauges:

- optional reversible RGB -> YCoCg-R color gauge;
- per-tile predictive gauge from already decoded neighbors;
- Rice coding of the snapped integer residuals.

The decompressor is intentionally simple: predict, read Rice residual, add.
"""

from __future__ import annotations

import binascii
import heapq
import struct

import cell_song_poc


MAGIC = b"SIGI"
VERSION = 1
TILE = 32

MODE_RAW = 0
MODE_RGB_RICE = 1
MODE_YCOCG_RICE = 2
MODE_YCOCG_HUFF = 3
MODE_RGB_HUFF = 4
MODE_YCOCG_CTX_RICE = 5
MODE_RGB_CTX_RICE = 6
MODE_GREEN_CTX_RICE = 7
MODE_GREEN_CTX_HUFF = 8
MODE_YCOCG_CTX_HUFF = 9
MODE_G_BG_RAVG_CTX_RICE = 10
MODE_G_BG_RAVG_ANOVA_RICE = 11
MODE_G_BG_RAVG_CTX_HUFF = 12

PRED_ZERO = 0
PRED_LEFT = 1
PRED_UP = 2
PRED_AVG = 3
PRED_MEDIAN = 4
PRED_PAETH = 5
PRED_PLANE = 6
PRED_LEFT_GRAD = 7
PRED_UP_GRAD = 8
PRED_LEFT_WEIGHT = 9
PRED_UP_WEIGHT = 10
PRED_UP_RIGHT = 11
PRED_LEFT_UP_RIGHT_AVG = 12
PRED_UP_UP_LEFT_AVG = 13
PRED_SELECT = 14
PRED_NE_PLANE = 15
PRED_LEFT_UP_LEFT_AVG = 16
PRED_UP_UP_RIGHT_AVG = 17
PRED_LEFT_UP_UP_RIGHT_AVG = 18
PRED_FOUR_AVG = 19
PRED_LEFT2_UP_AVG = 20
PRED_LEFT_UP2_AVG = 21
PREDICTORS = (
    PRED_ZERO,
    PRED_LEFT,
    PRED_UP,
    PRED_AVG,
    PRED_MEDIAN,
    PRED_PAETH,
    PRED_PLANE,
    PRED_LEFT_GRAD,
    PRED_UP_GRAD,
    PRED_LEFT_WEIGHT,
    PRED_UP_WEIGHT,
    PRED_UP_RIGHT,
    PRED_LEFT_UP_RIGHT_AVG,
    PRED_UP_UP_LEFT_AVG,
    PRED_SELECT,
    PRED_NE_PLANE,
    PRED_LEFT_UP_LEFT_AVG,
    PRED_UP_UP_RIGHT_AVG,
    PRED_LEFT_UP_UP_RIGHT_AVG,
    PRED_FOUR_AVG,
    PRED_LEFT2_UP_AVG,
    PRED_LEFT_UP2_AVG,
)
MAX_RICE_K = 14
RICE_CONTEXTS = 8
ANOVA_MARKER = 0x80
ANOVA_CONST = 0
ANOVA_ROW = 1
ANOVA_COL = 2
ANOVA_ROWCOL = 3
ANOVA_SUBMODES = (ANOVA_CONST, ANOVA_ROW, ANOVA_COL, ANOVA_ROWCOL)


class SimplicialImageError(RuntimeError):
    pass


class BitWriter:
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

    def write_bits(self, value: int, nbits: int) -> None:
        for shift in range(nbits - 1, -1, -1):
            self.write_bit((value >> shift) & 1)

    def write_unary(self, value: int) -> None:
        for _ in range(value):
            self.write_bit(0)
        self.write_bit(1)

    def align_byte(self) -> None:
        if self.nbits:
            self.cur <<= 8 - self.nbits
            self.data.append(self.cur)
            self.cur = 0
            self.nbits = 0

    def write_aligned_byte(self, value: int) -> None:
        self.align_byte()
        self.data.append(value & 0xFF)

    def finish(self) -> bytes:
        self.align_byte()
        return bytes(self.data)


class BitReader:
    def __init__(self, data: bytes) -> None:
        self.data = data
        self.byte_pos = 0
        self.bit_pos = 0

    def read_bit(self) -> int:
        if self.byte_pos >= len(self.data):
            raise SimplicialImageError("truncated bitstream")
        bit = (self.data[self.byte_pos] >> (7 - self.bit_pos)) & 1
        self.bit_pos += 1
        if self.bit_pos == 8:
            self.byte_pos += 1
            self.bit_pos = 0
        return bit

    def read_bits(self, nbits: int) -> int:
        value = 0
        for _ in range(nbits):
            value = (value << 1) | self.read_bit()
        return value

    def read_unary(self) -> int:
        value = 0
        while self.read_bit() == 0:
            value += 1
        return value

    def align_byte(self) -> None:
        if self.bit_pos:
            self.byte_pos += 1
            self.bit_pos = 0

    def read_aligned_byte(self) -> int:
        self.align_byte()
        if self.byte_pos >= len(self.data):
            raise SimplicialImageError("truncated byte header")
        value = self.data[self.byte_pos]
        self.byte_pos += 1
        return value


def zigzag(value: int) -> int:
    return value * 2 if value >= 0 else -value * 2 - 1


def unzigzag(value: int) -> int:
    return value // 2 if value % 2 == 0 else -(value // 2) - 1


def round_div_nearest(value: int, divisor: int) -> int:
    if divisor <= 0:
        raise ValueError("divisor must be positive")
    if value >= 0:
        return (value + divisor // 2) // divisor
    return -((-value + divisor // 2) // divisor)


def signed_varint_bytes(value: int) -> bytes:
    return cell_song_poc.put_varint(zigzag(value))


def signed_varint_size(value: int) -> int:
    return len(signed_varint_bytes(value))


def write_signed_varint(writer: BitWriter, value: int) -> None:
    writer.align_byte()
    writer.data += signed_varint_bytes(value)


def read_unsigned_varint(reader: BitReader) -> int:
    reader.align_byte()
    value = 0
    shift = 0
    for _ in range(10):
        byte = reader.read_aligned_byte()
        value |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            return value
        shift += 7
    raise SimplicialImageError("truncated varint")


def read_signed_varint(reader: BitReader) -> int:
    return unzigzag(read_unsigned_varint(reader))


def rice_bits(mapped: int, k: int) -> int:
    return (mapped >> k) + 1 + k


def write_rice(writer: BitWriter, signed_value: int, k: int) -> None:
    mapped = zigzag(signed_value)
    writer.write_unary(mapped >> k)
    if k:
        writer.write_bits(mapped & ((1 << k) - 1), k)


def read_rice(reader: BitReader, k: int) -> int:
    quotient = reader.read_unary()
    remainder = reader.read_bits(k) if k else 0
    return unzigzag((quotient << k) | remainder)


def huffman_code_lengths(frequencies: list[int]) -> list[int]:
    lengths = [0] * len(frequencies)
    heap: list[tuple[int, int]] = []
    nodes: list[tuple[int, int | None, int | None, int | None]] = []
    for symbol, frequency in enumerate(frequencies):
        if frequency:
            node_id = len(nodes)
            nodes.append((frequency, None, None, symbol))
            heapq.heappush(heap, (frequency, node_id))
    if not heap:
        return lengths
    if len(heap) == 1:
        lengths[nodes[heap[0][1]][3] or 0] = 1
        return lengths
    while len(heap) > 1:
        freq_a, node_a = heapq.heappop(heap)
        freq_b, node_b = heapq.heappop(heap)
        node_id = len(nodes)
        nodes.append((freq_a + freq_b, node_a, node_b, None))
        heapq.heappush(heap, (freq_a + freq_b, node_id))
    root = heap[0][1]
    stack = [(root, 0)]
    while stack:
        node_id, depth = stack.pop()
        _, left, right, symbol = nodes[node_id]
        if symbol is not None:
            lengths[symbol] = max(depth, 1)
        else:
            if left is not None:
                stack.append((left, depth + 1))
            if right is not None:
                stack.append((right, depth + 1))
    return lengths


def canonical_huffman_codes(lengths: list[int]) -> dict[int, tuple[int, int]]:
    codes: dict[int, tuple[int, int]] = {}
    code = 0
    prev_len = 0
    for symbol, length in sorted(
        ((symbol, length) for symbol, length in enumerate(lengths) if length),
        key=lambda item: (item[1], item[0]),
    ):
        code <<= length - prev_len
        codes[symbol] = (code, length)
        code += 1
        prev_len = length
    return codes


def canonical_huffman_decode_table(lengths: list[int]) -> tuple[dict[tuple[int, int], int], int]:
    codes = canonical_huffman_codes(lengths)
    table = {(length, code): symbol for symbol, (code, length) in codes.items()}
    max_len = max(lengths, default=0)
    return table, max_len


def write_huffman(writer: BitWriter, symbol: int, codes: dict[int, tuple[int, int]]) -> None:
    code, length = codes[symbol]
    writer.write_bits(code, length)


def read_huffman(reader: BitReader, table: dict[tuple[int, int], int], max_len: int) -> int:
    code = 0
    for length in range(1, max_len + 1):
        code = (code << 1) | reader.read_bit()
        symbol = table.get((length, code))
        if symbol is not None:
            return symbol
    raise SimplicialImageError("bad Huffman code")


def predict(channel: list[int], width: int, x: int, y: int, pred_id: int) -> int:
    left = channel[y * width + x - 1] if x > 0 else 0
    up = channel[(y - 1) * width + x] if y > 0 else 0
    up_left = channel[(y - 1) * width + x - 1] if x > 0 and y > 0 else 0
    up_right_available = y > 0 and x + 1 < width and (x + 1) % TILE != 0
    up_right = channel[(y - 1) * width + x + 1] if up_right_available else up

    if pred_id == PRED_ZERO:
        return 0
    if pred_id == PRED_LEFT:
        return left
    if pred_id == PRED_UP:
        return up
    if pred_id == PRED_AVG:
        return (left + up) // 2
    if pred_id == PRED_MEDIAN:
        if up_left >= max(left, up):
            return min(left, up)
        if up_left <= min(left, up):
            return max(left, up)
        return left + up - up_left
    if pred_id == PRED_PAETH:
        p = left + up - up_left
        pa = abs(p - left)
        pb = abs(p - up)
        pc = abs(p - up_left)
        if pa <= pb and pa <= pc:
            return left
        if pb <= pc:
            return up
        return up_left
    if pred_id == PRED_PLANE:
        return left + up - up_left
    if pred_id == PRED_LEFT_GRAD:
        return left + ((up - up_left) // 2)
    if pred_id == PRED_UP_GRAD:
        return up + ((left - up_left) // 2)
    if pred_id == PRED_LEFT_WEIGHT:
        return (3 * left + up) // 4
    if pred_id == PRED_UP_WEIGHT:
        return (left + 3 * up) // 4
    if pred_id == PRED_UP_RIGHT:
        return up_right
    if pred_id == PRED_LEFT_UP_RIGHT_AVG:
        return (left + up_right) // 2
    if pred_id == PRED_UP_UP_LEFT_AVG:
        return (up + up_left) // 2
    if pred_id == PRED_SELECT:
        p = left + up - up_left
        return left if abs(p - left) <= abs(p - up) else up
    if pred_id == PRED_NE_PLANE:
        return left + up - up_right
    if pred_id == PRED_LEFT_UP_LEFT_AVG:
        return (left + up_left) // 2
    if pred_id == PRED_UP_UP_RIGHT_AVG:
        return (up + up_right) // 2
    if pred_id == PRED_LEFT_UP_UP_RIGHT_AVG:
        return (left + up + up_right) // 3
    if pred_id == PRED_FOUR_AVG:
        return (left + up + up_left + up_right) // 4
    if pred_id == PRED_LEFT2_UP_AVG:
        return (2 * left + up) // 3
    if pred_id == PRED_LEFT_UP2_AVG:
        return (left + 2 * up) // 3
    raise SimplicialImageError(f"bad predictor {pred_id}")


def residual_context(channel: list[int], width: int, x: int, y: int) -> int:
    left = channel[y * width + x - 1] if x > 0 else 0
    up = channel[(y - 1) * width + x] if y > 0 else 0
    up_left = channel[(y - 1) * width + x - 1] if x > 0 and y > 0 else 0
    up_right_available = y > 0 and x + 1 < width and (x + 1) % TILE != 0
    up_right = channel[(y - 1) * width + x + 1] if up_right_available else up
    gradient = abs(left - up) + abs(left - up_left) + abs(up - up_left) + abs(up - up_right)
    for ctx, threshold in enumerate((4, 8, 16, 32, 64, 128, 256)):
        if gradient < threshold:
            return ctx
    return 7


def rgb_channels(rgb: bytes) -> list[list[int]]:
    channels = [[], [], []]
    for i in range(0, len(rgb), 3):
        channels[0].append(rgb[i])
        channels[1].append(rgb[i + 1])
        channels[2].append(rgb[i + 2])
    return channels


def channels_to_rgb(channels: list[list[int]]) -> bytes:
    out = bytearray()
    for r, g, b in zip(channels[0], channels[1], channels[2]):
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise SimplicialImageError("RGB channel escaped byte range")
        out += bytes((r, g, b))
    return bytes(out)


def rgb_to_ycocg(rgb: bytes) -> list[list[int]]:
    y_plane: list[int] = []
    co_plane: list[int] = []
    cg_plane: list[int] = []
    for i in range(0, len(rgb), 3):
        r = rgb[i]
        g = rgb[i + 1]
        b = rgb[i + 2]
        co = r - b
        t = b + (co >> 1)
        cg = g - t
        y = t + (cg >> 1)
        y_plane.append(y)
        co_plane.append(co)
        cg_plane.append(cg)
    return [y_plane, co_plane, cg_plane]


def rgb_to_green_mul(rgb: bytes, mr: int = 16, mb: int = 32) -> list[list[int]]:
    g_plane: list[int] = []
    r_plane: list[int] = []
    b_plane: list[int] = []
    for i in range(0, len(rgb), 3):
        r = rgb[i]
        g = rgb[i + 1]
        b = rgb[i + 2]
        g_plane.append(g)
        r_plane.append(r - ((mr * g) >> 5))
        b_plane.append(b - ((mb * g) >> 5))
    return [g_plane, r_plane, b_plane]


def rgb_to_g_bg_ravg(rgb: bytes) -> list[list[int]]:
    g_plane: list[int] = []
    bg_plane: list[int] = []
    r_plane: list[int] = []
    for i in range(0, len(rgb), 3):
        r = rgb[i]
        g = rgb[i + 1]
        b = rgb[i + 2]
        g_plane.append(g)
        bg_plane.append(b - g)
        r_plane.append(r - ((g + b) // 2))
    return [g_plane, bg_plane, r_plane]


def ycocg_to_rgb(channels: list[list[int]]) -> bytes:
    out = bytearray()
    for y, co, cg in zip(channels[0], channels[1], channels[2]):
        t = y - (cg >> 1)
        g = cg + t
        b = t - (co >> 1)
        r = b + co
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise SimplicialImageError("YCoCg inverse escaped byte range")
        out += bytes((r, g, b))
    return bytes(out)


def g_bg_ravg_to_rgb(channels: list[list[int]]) -> bytes:
    out = bytearray()
    for g, bg, r_delta in zip(channels[0], channels[1], channels[2]):
        b = bg + g
        r = r_delta + ((g + b) // 2)
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise SimplicialImageError("G/BG/Ravg inverse escaped byte range")
        out += bytes((r, g, b))
    return bytes(out)


def green_mul_to_rgb(channels: list[list[int]], mr: int = 16, mb: int = 32) -> bytes:
    out = bytearray()
    for g, r_delta, b_delta in zip(channels[0], channels[1], channels[2]):
        r = r_delta + ((mr * g) >> 5)
        b = b_delta + ((mb * g) >> 5)
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise SimplicialImageError("green-multiplier inverse escaped byte range")
        out += bytes((r, g, b))
    return bytes(out)


def tile_residuals(
    channel: list[int],
    width: int,
    height: int,
    tx: int,
    ty: int,
    pred_id: int,
) -> list[int]:
    residuals: list[int] = []
    xmax = min(tx + TILE, width)
    ymax = min(ty + TILE, height)
    for y in range(ty, ymax):
        row = y * width
        for x in range(tx, xmax):
            residuals.append(channel[row + x] - predict(channel, width, x, y, pred_id))
    return residuals


def choose_tile_code(residuals: list[int]) -> tuple[int, int]:
    mapped = [zigzag(v) for v in residuals]
    best_k = 0
    best_bits = sum(rice_bits(v, 0) for v in mapped)
    for k in range(1, MAX_RICE_K + 1):
        bits = sum(rice_bits(v, k) for v in mapped)
        if bits < best_bits:
            best_k = k
            best_bits = bits
    return best_k, best_bits


def encode_channels(channels: list[list[int]], width: int, height: int) -> bytes:
    writer = BitWriter()
    for channel in channels:
        for ty in range(0, height, TILE):
            for tx in range(0, width, TILE):
                best_pred = PRED_ZERO
                best_k = 0
                best_residuals: list[int] | None = None
                best_bits: int | None = None
                for pred_id in PREDICTORS:
                    residuals = tile_residuals(channel, width, height, tx, ty, pred_id)
                    k, bits = choose_tile_code(residuals)
                    if best_bits is None or bits < best_bits:
                        best_pred = pred_id
                        best_k = k
                        best_residuals = residuals
                        best_bits = bits
                if best_residuals is None:
                    raise SimplicialImageError("empty tile")
                writer.write_aligned_byte((best_pred << 4) | best_k)
                for residual in best_residuals:
                    write_rice(writer, residual, best_k)
    return writer.finish()


def tile_context_residuals(
    channel: list[int],
    width: int,
    height: int,
    tx: int,
    ty: int,
    pred_id: int,
) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    xmax = min(tx + TILE, width)
    ymax = min(ty + TILE, height)
    for y in range(ty, ymax):
        row = y * width
        for x in range(tx, xmax):
            ctx = residual_context(channel, width, x, y)
            pairs.append((ctx, channel[row + x] - predict(channel, width, x, y, pred_id)))
    return pairs


def choose_context_ks(pairs: list[tuple[int, int]]) -> tuple[list[int], int]:
    grouped: list[list[int]] = [[] for _ in range(RICE_CONTEXTS)]
    for ctx, residual in pairs:
        grouped[ctx].append(zigzag(residual))
    ks: list[int] = []
    total_bits = 0
    for symbols in grouped:
        if not symbols:
            ks.append(0)
            continue
        best_k = 0
        best_bits = sum(rice_bits(symbol, 0) for symbol in symbols)
        for k in range(1, MAX_RICE_K + 1):
            bits = sum(rice_bits(symbol, k) for symbol in symbols)
            if bits < best_bits:
                best_k = k
                best_bits = bits
        ks.append(best_k)
        total_bits += best_bits
    return ks, total_bits


def best_context_tile(
    channel: list[int],
    width: int,
    height: int,
    tx: int,
    ty: int,
) -> tuple[int, list[int], list[tuple[int, int]]]:
    best_pred = PRED_ZERO
    best_ks = [0] * RICE_CONTEXTS
    best_pairs: list[tuple[int, int]] | None = None
    best_bits: int | None = None
    for pred_id in PREDICTORS:
        pairs = tile_context_residuals(channel, width, height, tx, ty, pred_id)
        ks, bits = choose_context_ks(pairs)
        if best_bits is None or bits < best_bits:
            best_pred = pred_id
            best_ks = ks
            best_pairs = pairs
            best_bits = bits
    if best_pairs is None:
        raise SimplicialImageError("empty tile")
    return best_pred, best_ks, best_pairs


def context_tile_encoded_bytes(pairs: list[tuple[int, int]]) -> int:
    _, bits = choose_context_ks(pairs)
    return 5 + ((bits + 7) // 8)


def anova_tile_models(
    channel: list[int],
    width: int,
    height: int,
    tx: int,
    ty: int,
) -> list[tuple[int, int, list[int], list[int], list[int]]]:
    xmax = min(tx + TILE, width)
    ymax = min(ty + TILE, height)
    tw = xmax - tx
    th = ymax - ty
    values: list[list[int]] = []
    row_sums: list[int] = []
    col_sums = [0] * tw
    total = 0
    for y in range(ty, ymax):
        row_values = [channel[y * width + x] for x in range(tx, xmax)]
        values.append(row_values)
        row_sum = sum(row_values)
        row_sums.append(row_sum)
        total += row_sum
        for dx, value in enumerate(row_values):
            col_sums[dx] += value

    base = round_div_nearest(total, tw * th)
    row_effects = [round_div_nearest(row_sum, tw) - base for row_sum in row_sums]
    col_effects = [round_div_nearest(col_sum, th) - base for col_sum in col_sums]
    models: list[tuple[int, int, list[int], list[int], list[int]]] = []

    for submode in ANOVA_SUBMODES:
        stored_rows = row_effects if submode in (ANOVA_ROW, ANOVA_ROWCOL) else []
        stored_cols = col_effects if submode in (ANOVA_COL, ANOVA_ROWCOL) else []
        residuals: list[int] = []
        for dy, row_values in enumerate(values):
            row_effect = row_effects[dy] if submode in (ANOVA_ROW, ANOVA_ROWCOL) else 0
            for dx, value in enumerate(row_values):
                col_effect = col_effects[dx] if submode in (ANOVA_COL, ANOVA_ROWCOL) else 0
                residuals.append(value - (base + row_effect + col_effect))
        models.append((submode, base, stored_rows, stored_cols, residuals))
    return models


def anova_tile_encoded_bytes(base: int, row_effects: list[int], col_effects: list[int], bits: int) -> int:
    metadata = signed_varint_size(base)
    metadata += sum(signed_varint_size(value) for value in row_effects)
    metadata += sum(signed_varint_size(value) for value in col_effects)
    return 1 + metadata + ((bits + 7) // 8)


def best_anova_tile(
    channel: list[int],
    width: int,
    height: int,
    tx: int,
    ty: int,
) -> tuple[int, int, list[int], list[int], list[int], int, int]:
    best: tuple[int, int, list[int], list[int], list[int], int, int] | None = None
    for submode, base, row_effects, col_effects, residuals in anova_tile_models(
        channel, width, height, tx, ty
    ):
        k, bits = choose_tile_code(residuals)
        encoded_bytes = anova_tile_encoded_bytes(base, row_effects, col_effects, bits)
        if best is None or encoded_bytes < best[6]:
            best = (submode, base, row_effects, col_effects, residuals, k, encoded_bytes)
    if best is None:
        raise SimplicialImageError("empty ANOVA tile")
    return best


def encode_context_rice_channels(channels: list[list[int]], width: int, height: int) -> bytes:
    writer = BitWriter()
    for channel in channels:
        for ty in range(0, height, TILE):
            for tx in range(0, width, TILE):
                pred_id, ks, pairs = best_context_tile(channel, width, height, tx, ty)
                writer.write_aligned_byte(pred_id)
                for i in range(0, RICE_CONTEXTS, 2):
                    writer.write_aligned_byte(ks[i] | (ks[i + 1] << 4))
                for ctx, residual in pairs:
                    write_rice(writer, residual, ks[ctx])
    return writer.finish()


def encode_anova_rice_channels(channels: list[list[int]], width: int, height: int) -> bytes:
    writer = BitWriter()
    for channel in channels:
        for ty in range(0, height, TILE):
            for tx in range(0, width, TILE):
                pred_id, ks, pairs = best_context_tile(channel, width, height, tx, ty)
                context_bytes = context_tile_encoded_bytes(pairs)
                submode, base, row_effects, col_effects, residuals, k, anova_bytes = best_anova_tile(
                    channel, width, height, tx, ty
                )
                if anova_bytes < context_bytes:
                    writer.write_aligned_byte(ANOVA_MARKER | (submode << 4) | k)
                    write_signed_varint(writer, base)
                    for value in row_effects:
                        write_signed_varint(writer, value)
                    for value in col_effects:
                        write_signed_varint(writer, value)
                    for residual in residuals:
                        write_rice(writer, residual, k)
                else:
                    writer.write_aligned_byte(pred_id)
                    for i in range(0, RICE_CONTEXTS, 2):
                        writer.write_aligned_byte(ks[i] | (ks[i + 1] << 4))
                    for ctx, residual in pairs:
                        write_rice(writer, residual, ks[ctx])
    return writer.finish()


def best_tile_residuals(
    channel: list[int],
    width: int,
    height: int,
    tx: int,
    ty: int,
) -> tuple[int, list[int]]:
    best_pred = PRED_ZERO
    best_residuals: list[int] | None = None
    best_bits: int | None = None
    for pred_id in PREDICTORS:
        residuals = tile_residuals(channel, width, height, tx, ty, pred_id)
        _, bits = choose_tile_code(residuals)
        if best_bits is None or bits < best_bits:
            best_pred = pred_id
            best_residuals = residuals
            best_bits = bits
    if best_residuals is None:
        raise SimplicialImageError("empty tile")
    return best_pred, best_residuals


def encode_huffman_channel(channel: list[int], width: int, height: int) -> bytes:
    tile_preds = bytearray()
    symbols: list[int] = []
    frequencies: list[int] = [0]
    for ty in range(0, height, TILE):
        for tx in range(0, width, TILE):
            pred_id, residuals = best_tile_residuals(channel, width, height, tx, ty)
            tile_preds.append(pred_id)
            for residual in residuals:
                symbol = zigzag(residual)
                symbols.append(symbol)
                if symbol >= len(frequencies):
                    frequencies.extend([0] * (symbol + 1 - len(frequencies)))
                frequencies[symbol] += 1

    lengths = huffman_code_lengths(frequencies)
    max_symbol = len(lengths) - 1
    while max_symbol > 0 and lengths[max_symbol] == 0:
        max_symbol -= 1
    lengths = lengths[: max_symbol + 1]
    codes = canonical_huffman_codes(lengths)

    writer = BitWriter()
    for symbol in symbols:
        write_huffman(writer, symbol, codes)
    bitstream = writer.finish()

    out = bytearray()
    out += cell_song_poc.put_varint(max_symbol)
    out += bytes(lengths)
    out += tile_preds
    out += bitstream
    return bytes(out)


def encode_huffman_channels(channels: list[list[int]], width: int, height: int) -> bytes:
    out = bytearray()
    for channel in channels:
        encoded = encode_huffman_channel(channel, width, height)
        out += cell_song_poc.put_varint(len(encoded))
        out += encoded
    return bytes(out)


def encode_lengths_rle(lengths: list[int]) -> bytes:
    out = bytearray()
    out += cell_song_poc.put_varint(len(lengths))
    i = 0
    while i < len(lengths):
        value = lengths[i]
        run = 1
        while i + run < len(lengths) and lengths[i + run] == value:
            run += 1
        out.append(value)
        out += cell_song_poc.put_varint(run)
        i += run
    return bytes(out)


def decode_lengths_rle(blob: bytes, offset: int) -> tuple[list[int], int]:
    count, offset = cell_song_poc.get_varint(blob, offset)
    lengths: list[int] = []
    while len(lengths) < count:
        if offset >= len(blob):
            raise SimplicialImageError("truncated Huffman lengths")
        value = blob[offset]
        offset += 1
        run, offset = cell_song_poc.get_varint(blob, offset)
        lengths.extend([value] * run)
    if len(lengths) != count:
        raise SimplicialImageError("bad Huffman length RLE")
    return lengths, offset


def encode_context_huffman_channel(channel: list[int], width: int, height: int) -> bytes:
    tile_preds = bytearray()
    tile_pairs: list[list[tuple[int, int]]] = []
    frequencies: list[list[int]] = [[0] for _ in range(RICE_CONTEXTS)]

    for ty in range(0, height, TILE):
        for tx in range(0, width, TILE):
            pred_id, _, pairs = best_context_tile(channel, width, height, tx, ty)
            tile_preds.append(pred_id)
            tile_pairs.append(pairs)
            for ctx, residual in pairs:
                symbol = zigzag(residual)
                freq = frequencies[ctx]
                if symbol >= len(freq):
                    freq.extend([0] * (symbol + 1 - len(freq)))
                freq[symbol] += 1

    codebooks: list[dict[int, tuple[int, int]]] = []
    encoded_lengths = bytearray()
    for freq in frequencies:
        lengths = huffman_code_lengths(freq)
        max_symbol = len(lengths) - 1
        while max_symbol > 0 and lengths[max_symbol] == 0:
            max_symbol -= 1
        lengths = lengths[: max_symbol + 1]
        encoded_lengths += encode_lengths_rle(lengths)
        codebooks.append(canonical_huffman_codes(lengths))

    writer = BitWriter()
    for pairs in tile_pairs:
        for ctx, residual in pairs:
            write_huffman(writer, zigzag(residual), codebooks[ctx])

    out = bytearray()
    out += tile_preds
    out += encoded_lengths
    out += writer.finish()
    return bytes(out)


def encode_context_huffman_channels(channels: list[list[int]], width: int, height: int) -> bytes:
    out = bytearray()
    for channel in channels:
        encoded = encode_context_huffman_channel(channel, width, height)
        out += cell_song_poc.put_varint(len(encoded))
        out += encoded
    return bytes(out)


def decode_channels(payload: bytes, width: int, height: int) -> list[list[int]]:
    reader = BitReader(payload)
    channels: list[list[int]] = []
    for _ in range(3):
        channel = [0] * (width * height)
        for ty in range(0, height, TILE):
            for tx in range(0, width, TILE):
                packed = reader.read_aligned_byte()
                pred_id = packed >> 4
                k = packed & 0x0F
                if pred_id not in PREDICTORS or k > MAX_RICE_K:
                    raise SimplicialImageError("bad tile header")
                xmax = min(tx + TILE, width)
                ymax = min(ty + TILE, height)
                for y in range(ty, ymax):
                    row = y * width
                    for x in range(tx, xmax):
                        channel[row + x] = predict(channel, width, x, y, pred_id) + read_rice(reader, k)
        channels.append(channel)
    return channels


def decode_context_rice_channels(payload: bytes, width: int, height: int) -> list[list[int]]:
    reader = BitReader(payload)
    channels: list[list[int]] = []
    for _ in range(3):
        channel = [0] * (width * height)
        for ty in range(0, height, TILE):
            for tx in range(0, width, TILE):
                pred_id = reader.read_aligned_byte()
                ks = []
                for _ in range(0, RICE_CONTEXTS, 2):
                    packed = reader.read_aligned_byte()
                    ks.append(packed & 0x0F)
                    ks.append(packed >> 4)
                if pred_id not in PREDICTORS or any(k > MAX_RICE_K for k in ks):
                    raise SimplicialImageError("bad context Rice tile header")
                xmax = min(tx + TILE, width)
                ymax = min(ty + TILE, height)
                for y in range(ty, ymax):
                    row = y * width
                    for x in range(tx, xmax):
                        ctx = residual_context(channel, width, x, y)
                        channel[row + x] = predict(channel, width, x, y, pred_id) + read_rice(
                            reader, ks[ctx]
                        )
        channels.append(channel)
    return channels


def decode_anova_rice_channels(payload: bytes, width: int, height: int) -> list[list[int]]:
    reader = BitReader(payload)
    channels: list[list[int]] = []
    for _ in range(3):
        channel = [0] * (width * height)
        for ty in range(0, height, TILE):
            for tx in range(0, width, TILE):
                first = reader.read_aligned_byte()
                xmax = min(tx + TILE, width)
                ymax = min(ty + TILE, height)
                tw = xmax - tx
                th = ymax - ty
                if first & ANOVA_MARKER:
                    submode = (first >> 4) & 0x07
                    k = first & 0x0F
                    if submode not in ANOVA_SUBMODES or k > MAX_RICE_K:
                        raise SimplicialImageError("bad ANOVA tile header")
                    base = read_signed_varint(reader)
                    row_effects = (
                        [read_signed_varint(reader) for _ in range(th)]
                        if submode in (ANOVA_ROW, ANOVA_ROWCOL)
                        else [0] * th
                    )
                    col_effects = (
                        [read_signed_varint(reader) for _ in range(tw)]
                        if submode in (ANOVA_COL, ANOVA_ROWCOL)
                        else [0] * tw
                    )
                    for dy, y in enumerate(range(ty, ymax)):
                        row = y * width
                        row_effect = row_effects[dy]
                        for dx, x in enumerate(range(tx, xmax)):
                            channel[row + x] = base + row_effect + col_effects[dx] + read_rice(
                                reader, k
                            )
                else:
                    pred_id = first
                    ks = []
                    for _ in range(0, RICE_CONTEXTS, 2):
                        packed = reader.read_aligned_byte()
                        ks.append(packed & 0x0F)
                        ks.append(packed >> 4)
                    if pred_id not in PREDICTORS or any(k > MAX_RICE_K for k in ks):
                        raise SimplicialImageError("bad mixed Rice tile header")
                    for y in range(ty, ymax):
                        row = y * width
                        for x in range(tx, xmax):
                            ctx = residual_context(channel, width, x, y)
                            channel[row + x] = predict(channel, width, x, y, pred_id) + read_rice(
                                reader, ks[ctx]
                            )
        channels.append(channel)
    return channels


def tile_count(width: int, height: int) -> int:
    return ((width + TILE - 1) // TILE) * ((height + TILE - 1) // TILE)


def decode_huffman_channel(payload: bytes, width: int, height: int) -> list[int]:
    offset = 0
    max_symbol, offset = cell_song_poc.get_varint(payload, offset)
    lengths = list(payload[offset : offset + max_symbol + 1])
    offset += max_symbol + 1
    count = tile_count(width, height)
    tile_preds = payload[offset : offset + count]
    if len(tile_preds) != count:
        raise SimplicialImageError("truncated Huffman tile headers")
    offset += count
    table, max_len = canonical_huffman_decode_table(lengths)
    if max_len == 0:
        raise SimplicialImageError("empty Huffman table")
    reader = BitReader(payload[offset:])
    channel = [0] * (width * height)
    pred_pos = 0
    for ty in range(0, height, TILE):
        for tx in range(0, width, TILE):
            pred_id = tile_preds[pred_pos]
            pred_pos += 1
            if pred_id not in PREDICTORS:
                raise SimplicialImageError("bad Huffman predictor")
            xmax = min(tx + TILE, width)
            ymax = min(ty + TILE, height)
            for y in range(ty, ymax):
                row = y * width
                for x in range(tx, xmax):
                    symbol = read_huffman(reader, table, max_len)
                    channel[row + x] = predict(channel, width, x, y, pred_id) + unzigzag(symbol)
    return channel


def decode_huffman_channels(payload: bytes, width: int, height: int) -> list[list[int]]:
    offset = 0
    channels: list[list[int]] = []
    for _ in range(3):
        channel_size, offset = cell_song_poc.get_varint(payload, offset)
        channel_blob = payload[offset : offset + channel_size]
        if len(channel_blob) != channel_size:
            raise SimplicialImageError("truncated Huffman channel")
        offset += channel_size
        channels.append(decode_huffman_channel(channel_blob, width, height))
    if offset != len(payload):
        raise SimplicialImageError("trailing Huffman payload")
    return channels


def decode_context_huffman_channel(payload: bytes, width: int, height: int) -> list[int]:
    offset = 0
    count = tile_count(width, height)
    tile_preds = payload[offset : offset + count]
    if len(tile_preds) != count:
        raise SimplicialImageError("truncated context Huffman tile headers")
    offset += count

    tables: list[dict[tuple[int, int], int]] = []
    max_lens: list[int] = []
    for _ in range(RICE_CONTEXTS):
        lengths, offset = decode_lengths_rle(payload, offset)
        table, max_len = canonical_huffman_decode_table(lengths)
        tables.append(table)
        max_lens.append(max_len)

    reader = BitReader(payload[offset:])
    channel = [0] * (width * height)
    pred_pos = 0
    for ty in range(0, height, TILE):
        for tx in range(0, width, TILE):
            pred_id = tile_preds[pred_pos]
            pred_pos += 1
            if pred_id not in PREDICTORS:
                raise SimplicialImageError("bad context Huffman predictor")
            xmax = min(tx + TILE, width)
            ymax = min(ty + TILE, height)
            for y in range(ty, ymax):
                row = y * width
                for x in range(tx, xmax):
                    ctx = residual_context(channel, width, x, y)
                    symbol = read_huffman(reader, tables[ctx], max_lens[ctx])
                    channel[row + x] = predict(channel, width, x, y, pred_id) + unzigzag(symbol)
    return channel


def decode_context_huffman_channels(payload: bytes, width: int, height: int) -> list[list[int]]:
    offset = 0
    channels: list[list[int]] = []
    for _ in range(3):
        channel_size, offset = cell_song_poc.get_varint(payload, offset)
        channel_blob = payload[offset : offset + channel_size]
        if len(channel_blob) != channel_size:
            raise SimplicialImageError("truncated context Huffman channel")
        offset += channel_size
        channels.append(decode_context_huffman_channel(channel_blob, width, height))
    if offset != len(payload):
        raise SimplicialImageError("trailing context Huffman payload")
    return channels


def make_header(rgb: bytes, width: int, height: int) -> bytes:
    return (
        MAGIC
        + bytes((VERSION,))
        + cell_song_poc.put_varint(width)
        + cell_song_poc.put_varint(height)
        + struct.pack("<I", binascii.crc32(rgb) & 0xFFFFFFFF)
    )


def compress_rgb(rgb: bytes, width: int, height: int) -> bytes:
    if len(rgb) != width * height * 3:
        raise ValueError("RGB payload length does not match dimensions")

    header = make_header(rgb, width, height)
    candidates = [(MODE_RAW, rgb)]
    candidates.append((MODE_RGB_RICE, encode_channels(rgb_channels(rgb), width, height)))
    candidates.append((MODE_YCOCG_RICE, encode_channels(rgb_to_ycocg(rgb), width, height)))
    candidates.append((MODE_YCOCG_CTX_RICE, encode_context_rice_channels(rgb_to_ycocg(rgb), width, height)))
    candidates.append((MODE_GREEN_CTX_RICE, encode_context_rice_channels(rgb_to_green_mul(rgb), width, height)))
    candidates.append(
        (MODE_G_BG_RAVG_CTX_RICE, encode_context_rice_channels(rgb_to_g_bg_ravg(rgb), width, height))
    )
    candidates.append(
        (MODE_G_BG_RAVG_ANOVA_RICE, encode_anova_rice_channels(rgb_to_g_bg_ravg(rgb), width, height))
    )
    candidates.append(
        (MODE_G_BG_RAVG_CTX_HUFF, encode_context_huffman_channels(rgb_to_g_bg_ravg(rgb), width, height))
    )
    candidates.append((MODE_YCOCG_CTX_HUFF, encode_context_huffman_channels(rgb_to_ycocg(rgb), width, height)))
    candidates.append((MODE_GREEN_CTX_HUFF, encode_context_huffman_channels(rgb_to_green_mul(rgb), width, height)))
    mode, payload = min(candidates, key=lambda item: len(item[1]))
    return header + bytes((mode,)) + payload


def decompress_rgb(blob: bytes) -> tuple[bytes, int, int]:
    if len(blob) < 6 or blob[:4] != MAGIC:
        raise SimplicialImageError("bad SIGI magic")
    if blob[4] != VERSION:
        raise SimplicialImageError("unsupported SIGI version")
    offset = 5
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    expected_crc = struct.unpack("<I", blob[offset : offset + 4])[0]
    offset += 4
    if offset >= len(blob):
        raise SimplicialImageError("missing SIGI mode")
    mode = blob[offset]
    payload = blob[offset + 1 :]

    if mode == MODE_RAW:
        rgb = payload
    elif mode == MODE_RGB_RICE:
        rgb = channels_to_rgb(decode_channels(payload, width, height))
    elif mode == MODE_YCOCG_RICE:
        rgb = ycocg_to_rgb(decode_channels(payload, width, height))
    elif mode == MODE_RGB_CTX_RICE:
        rgb = channels_to_rgb(decode_context_rice_channels(payload, width, height))
    elif mode == MODE_YCOCG_CTX_RICE:
        rgb = ycocg_to_rgb(decode_context_rice_channels(payload, width, height))
    elif mode == MODE_GREEN_CTX_RICE:
        rgb = green_mul_to_rgb(decode_context_rice_channels(payload, width, height))
    elif mode == MODE_G_BG_RAVG_CTX_RICE:
        rgb = g_bg_ravg_to_rgb(decode_context_rice_channels(payload, width, height))
    elif mode == MODE_G_BG_RAVG_ANOVA_RICE:
        rgb = g_bg_ravg_to_rgb(decode_anova_rice_channels(payload, width, height))
    elif mode == MODE_G_BG_RAVG_CTX_HUFF:
        rgb = g_bg_ravg_to_rgb(decode_context_huffman_channels(payload, width, height))
    elif mode == MODE_GREEN_CTX_HUFF:
        rgb = green_mul_to_rgb(decode_context_huffman_channels(payload, width, height))
    elif mode == MODE_YCOCG_CTX_HUFF:
        rgb = ycocg_to_rgb(decode_context_huffman_channels(payload, width, height))
    elif mode == MODE_RGB_HUFF:
        rgb = channels_to_rgb(decode_huffman_channels(payload, width, height))
    elif mode == MODE_YCOCG_HUFF:
        rgb = ycocg_to_rgb(decode_huffman_channels(payload, width, height))
    else:
        raise SimplicialImageError(f"unknown SIGI mode {mode}")

    if len(rgb) != width * height * 3:
        raise SimplicialImageError("decoded size mismatch")
    crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if crc != expected_crc:
        raise SimplicialImageError("CRC mismatch")
    return rgb, width, height


def mode_name(blob: bytes) -> str:
    offset = 5
    _, offset = cell_song_poc.get_varint(blob, offset)
    _, offset = cell_song_poc.get_varint(blob, offset)
    offset += 4
    mode = blob[offset]
    return {
        MODE_RAW: "raw",
        MODE_RGB_RICE: "rgb-rice",
        MODE_YCOCG_RICE: "ycocg-rice",
        MODE_YCOCG_HUFF: "ycocg-huff",
        MODE_RGB_HUFF: "rgb-huff",
        MODE_YCOCG_CTX_RICE: "ycocg-ctx-rice",
        MODE_RGB_CTX_RICE: "rgb-ctx-rice",
        MODE_GREEN_CTX_RICE: "green16-ctx-rice",
        MODE_GREEN_CTX_HUFF: "green16-ctx-huff",
        MODE_YCOCG_CTX_HUFF: "ycocg-ctx-huff",
        MODE_G_BG_RAVG_CTX_RICE: "g-bg-ravg-ctx-rice",
        MODE_G_BG_RAVG_ANOVA_RICE: "g-bg-ravg-anova-rice",
        MODE_G_BG_RAVG_CTX_HUFF: "g-bg-ravg-ctx-huff",
    }.get(mode, f"unknown-{mode}")
