#!/usr/bin/env python3
"""2D rounding-cell image song POC.

This is the first image-native version of the cell-song idea. For each 8x8
channel block, it tries to store a sparse 2D Haar song. The song is accepted
only if the inverse projection lands inside every pixel's unit rounding cell:

    pixel <= y < pixel + 1

Then decode is exact by floor(y).
"""

from __future__ import annotations

import binascii
import math
import struct

import numpy as np

import cell_song_poc


MAGIC = b"IH2D"
VERSION = 1
BLOCK = 8
BLOCK_PIXELS = BLOCK * BLOCK
RAW = 0
SONG = 1
PLANE = 2
QUAD = 3
STREAM_RAW = 0
STREAM_BLOCKS = 1
MAX_COEFFS = 14  # 1 kind + 8 mask + 14*4 = 65, so 14 is break-even-ish.


class Image2DError(RuntimeError):
    pass


def haar_matrix(n: int = BLOCK) -> np.ndarray:
    rows: list[np.ndarray] = []
    rows.append(np.ones(n, dtype=np.float64) / math.sqrt(n))

    scale = 1
    while scale < n:
        width = n // scale
        half = width // 2
        amp = 1.0 / math.sqrt(width)
        for start in range(0, n, width):
            row = np.zeros(n, dtype=np.float64)
            row[start : start + half] = amp
            row[start + half : start + width] = -amp
            rows.append(row)
        scale *= 2
    return np.vstack(rows)


H = haar_matrix()
ATOMS = np.stack(
    [np.outer(H[u], H[v]).reshape(-1) for u in range(BLOCK) for v in range(BLOCK)]
)


def polynomial_basis() -> tuple[np.ndarray, np.ndarray]:
    xs = np.linspace(-1.0, 1.0, BLOCK)
    ys = np.linspace(-1.0, 1.0, BLOCK)
    xx, yy = np.meshgrid(xs, ys)
    plane = np.stack(
        [
            np.ones(BLOCK_PIXELS),
            xx.reshape(-1),
            yy.reshape(-1),
        ],
        axis=1,
    )
    quad = np.stack(
        [
            np.ones(BLOCK_PIXELS),
            xx.reshape(-1),
            yy.reshape(-1),
            (xx * yy).reshape(-1),
            (xx * xx).reshape(-1),
            (yy * yy).reshape(-1),
        ],
        axis=1,
    )
    return plane, quad


PLANE_BASIS, QUAD_BASIS = polynomial_basis()
_LINPROG = None
_LINPROG_CHECKED = False


def optional_linprog():
    global _LINPROG, _LINPROG_CHECKED
    if not _LINPROG_CHECKED:
        _LINPROG_CHECKED = True
        try:
            from scipy.optimize import linprog  # type: ignore

            _LINPROG = linprog
        except Exception:
            _LINPROG = None
    return _LINPROG


def floor_bytes(values: np.ndarray) -> bytes:
    floored = np.floor(values)
    if np.any(floored < 0) or np.any(floored > 255):
        return b""
    return bytes(floored.astype(np.uint8).tolist())


def song_for_block(block: bytes) -> tuple[int, list[float]] | None:
    if len(block) != BLOCK_PIXELS:
        return None
    if len(set(block)) == 1:
        # Constant blocks are the ideal one-note song.
        pass
    elif max(block) - min(block) > 96 and len(set(block)) > 32:
        # Hard photographic texture almost never wins under the 14-coeff cap.
        return None

    target = block
    pixels = np.frombuffer(block, dtype=np.uint8).astype(np.float64)
    x = pixels.reshape(BLOCK, BLOCK) + 0.5
    coeff = H @ x @ H.T
    flat = coeff.reshape(-1)
    order = np.argsort(-np.abs(flat))

    recon = np.zeros(BLOCK_PIXELS, dtype=np.float64)
    mask = 0
    chosen: list[int] = []
    for rank, idx in enumerate(order[:MAX_COEFFS], start=1):
        value = struct.unpack("<f", struct.pack("<f", float(flat[idx])))[0]
        recon += value * ATOMS[int(idx)]
        mask |= 1 << int(idx)
        chosen.append(int(idx))
        if floor_bytes(recon) == target:
            values = [
                struct.unpack("<f", struct.pack("<f", float(flat[i])))[0]
                for i in sorted(chosen)
            ]
            return mask, values

        # The real cell-song test: can any coefficients on this sparse support
        # hit the unit rounding cells? Use a small interior margin so float32
        # coefficient storage is less likely to land exactly on a boundary.
        if rank >= 2:
            solved = solve_interval_song(pixels, sorted(chosen))
            if solved is not None:
                return solved
    return None


def solve_fixed_basis(block: bytes, basis: np.ndarray) -> list[float] | None:
    linprog = optional_linprog()
    if linprog is None:
        return None
    pixels = np.frombuffer(block, dtype=np.uint8).astype(np.float64)
    lower = pixels + 0.02
    upper = pixels + 0.98
    a_ub = np.vstack([basis, -basis])
    b_ub = np.concatenate([upper, -lower])
    result = linprog(
        np.zeros(basis.shape[1], dtype=np.float64),
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(None, None)] * basis.shape[1],
        method="highs",
    )
    if not result.success:
        return None
    values = [struct.unpack("<f", struct.pack("<f", float(v)))[0] for v in result.x]
    recon = basis @ np.asarray(values, dtype=np.float64)
    if floor_bytes(recon) != block:
        return None
    return values


def poly_song_for_block(block: bytes) -> tuple[int, list[float]] | None:
    if len(block) != BLOCK_PIXELS:
        return None
    if max(block) - min(block) > 80 and len(set(block)) > 24:
        return None
    plane = solve_fixed_basis(block, PLANE_BASIS)
    if plane is not None:
        return PLANE, plane
    quad = solve_fixed_basis(block, QUAD_BASIS)
    if quad is not None:
        return QUAD, quad
    return None


def solve_interval_song(pixels: np.ndarray, support: list[int]) -> tuple[int, list[float]] | None:
    linprog = optional_linprog()
    if linprog is None:
        return None

    basis = ATOMS[support].T
    lower = pixels + 0.02
    upper = pixels + 0.98
    a_ub = np.vstack([basis, -basis])
    b_ub = np.concatenate([upper, -lower])
    # Prefer smaller coefficients very weakly by minimizing the DC-free scale
    # proxy. This is not yet a real bit-cost objective; it just avoids some
    # huge feasible boundary points.
    c = np.zeros(len(support), dtype=np.float64)
    result = linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=[(None, None)] * len(support), method="highs")
    if not result.success:
        return None

    values = [struct.unpack("<f", struct.pack("<f", float(v)))[0] for v in result.x]
    recon = np.zeros(BLOCK_PIXELS, dtype=np.float64)
    for idx, value in zip(support, values):
        recon += value * ATOMS[idx]
    if floor_bytes(recon) != bytes(pixels.astype(np.uint8).tolist()):
        return None
    mask = 0
    for idx in support:
        mask |= 1 << idx
    return mask, values


def encode_block(block: bytes) -> bytes:
    poly = poly_song_for_block(block)
    if poly is not None:
        kind, values = poly
        out = bytearray([kind])
        for value in values:
            out += struct.pack("<f", value)
        if len(out) < 1 + len(block):
            return bytes(out)

    song = song_for_block(block)
    if song is None:
        return bytes([RAW]) + block
    mask, values = song
    out = bytearray([SONG])
    out += struct.pack("<Q", mask)
    for value in values:
        out += struct.pack("<f", value)
    if len(out) >= 1 + len(block):
        return bytes([RAW]) + block
    return bytes(out)


def decode_block(blob: bytes, offset: int) -> tuple[bytes, int]:
    kind = blob[offset]
    offset += 1
    if kind == RAW:
        return blob[offset : offset + BLOCK_PIXELS], offset + BLOCK_PIXELS
    if kind in (PLANE, QUAD):
        basis = PLANE_BASIS if kind == PLANE else QUAD_BASIS
        values = []
        for _ in range(basis.shape[1]):
            values.append(struct.unpack("<f", blob[offset : offset + 4])[0])
            offset += 4
        decoded = floor_bytes(basis @ np.asarray(values, dtype=np.float64))
        if len(decoded) != BLOCK_PIXELS:
            raise Image2DError("decoded polynomial block escaped byte range")
        return decoded, offset
    if kind != SONG:
        raise Image2DError(f"unknown block kind {kind}")
    mask = struct.unpack("<Q", blob[offset : offset + 8])[0]
    offset += 8
    recon = np.zeros(BLOCK_PIXELS, dtype=np.float64)
    for idx in range(BLOCK_PIXELS):
        if mask & (1 << idx):
            value = struct.unpack("<f", blob[offset : offset + 4])[0]
            offset += 4
            recon += value * ATOMS[idx]
    decoded = floor_bytes(recon)
    if len(decoded) != BLOCK_PIXELS:
        raise Image2DError("decoded block escaped byte range")
    return decoded, offset


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


def compress_rgb(rgb: bytes, width: int, height: int) -> bytes:
    if width % BLOCK or height % BLOCK:
        raise ValueError("image dimensions must be multiples of 8 for this POC")
    if len(rgb) != width * height * 3:
        raise ValueError("RGB payload length does not match dimensions")

    planar = planar_rgb(rgb, width, height)
    header = bytearray()
    header += MAGIC
    header.append(VERSION)
    header += cell_song_poc.put_varint(width)
    header += cell_song_poc.put_varint(height)
    header += struct.pack("<I", binascii.crc32(rgb) & 0xFFFFFFFF)

    stream = bytearray()
    plane_size = width * height
    for c in range(3):
        plane = planar[c * plane_size : (c + 1) * plane_size]
        for by in range(0, height, BLOCK):
            for bx in range(0, width, BLOCK):
                block = bytearray()
                for y in range(BLOCK):
                    row = (by + y) * width + bx
                    block += plane[row : row + BLOCK]
                stream += encode_block(bytes(block))

    raw_stream = bytes([STREAM_RAW]) + rgb
    block_stream = bytes([STREAM_BLOCKS]) + bytes(stream)
    return bytes(header) + (raw_stream if len(raw_stream) < len(block_stream) else block_stream)


def decompress_rgb(blob: bytes) -> tuple[bytes, int, int]:
    if len(blob) < 5 or blob[:4] != MAGIC:
        raise Image2DError("bad image2d magic")
    if blob[4] != VERSION:
        raise Image2DError("unsupported version")
    offset = 5
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    expected_crc = struct.unpack("<I", blob[offset : offset + 4])[0]
    offset += 4
    if width % BLOCK or height % BLOCK:
        raise Image2DError("invalid dimensions")

    if offset >= len(blob):
        raise Image2DError("missing stream mode")
    mode = blob[offset]
    offset += 1
    if mode == STREAM_RAW:
        size = width * height * 3
        rgb = blob[offset : offset + size]
        offset += size
        if offset != len(blob):
            raise Image2DError("trailing bytes")
        crc = binascii.crc32(rgb) & 0xFFFFFFFF
        if crc != expected_crc:
            raise Image2DError("CRC mismatch")
        return rgb, width, height
    if mode != STREAM_BLOCKS:
        raise Image2DError(f"unknown stream mode {mode}")

    planes = [bytearray(width * height) for _ in range(3)]
    for c in range(3):
        plane = planes[c]
        for by in range(0, height, BLOCK):
            for bx in range(0, width, BLOCK):
                block, offset = decode_block(blob, offset)
                pos = 0
                for y in range(BLOCK):
                    row = (by + y) * width + bx
                    plane[row : row + BLOCK] = block[pos : pos + BLOCK]
                    pos += BLOCK
    if offset != len(blob):
        raise Image2DError("trailing bytes")
    rgb = unplanar_rgb(b"".join(bytes(p) for p in planes), width, height)
    crc = binascii.crc32(rgb) & 0xFFFFFFFF
    if crc != expected_crc:
        raise Image2DError("CRC mismatch")
    return rgb, width, height


def stats(blob: bytes) -> tuple[int, int]:
    offset = 5
    width, offset = cell_song_poc.get_varint(blob, offset)
    height, offset = cell_song_poc.get_varint(blob, offset)
    offset += 4
    mode = blob[offset]
    offset += 1
    if mode == STREAM_RAW:
        return (width // BLOCK) * (height // BLOCK) * 3, 0
    if mode != STREAM_BLOCKS:
        raise Image2DError(f"unknown stream mode {mode}")
    raw = 0
    song = 0
    blocks = (width // BLOCK) * (height // BLOCK) * 3
    for _ in range(blocks):
        kind = blob[offset]
        offset += 1
        if kind == RAW:
            raw += 1
            offset += BLOCK_PIXELS
        elif kind == PLANE:
            song += 1
            offset += 3 * 4
        elif kind == QUAD:
            song += 1
            offset += 6 * 4
        elif kind == SONG:
            song += 1
            mask = struct.unpack("<Q", blob[offset : offset + 8])[0]
            offset += 8 + 4 * mask.bit_count()
        else:
            raise Image2DError(f"unknown block kind {kind}")
    return raw, song
