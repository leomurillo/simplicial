#!/usr/bin/env python3
"""Rounding-cell spectral song codec, proof of concept.

This is the smallest version of the idea:

    bytes b_i define cells [b_i, b_i + 1)
    encode a sparse recursive Haar/Helmert song y
    decode by inverse projection and floor(y_i)

Internally the reconstruction is allowed to be "lossy" as a real vector. It
only has to land in the same unit rounding cell for every coordinate, which
makes the final byte output lossless.
"""

from __future__ import annotations

import argparse
import binascii
import math
import struct
import sys
from pathlib import Path


MAGIC = b"HCS0"
VERSION = 1
DEFAULT_BLOCK = 64
RAW = 0
SONG = 1


class CellSongError(RuntimeError):
    pass


def put_varint(value: int) -> bytes:
    out = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            out.append(byte | 0x80)
        else:
            out.append(byte)
            return bytes(out)


def get_varint(blob: bytes, offset: int) -> tuple[int, int]:
    value = 0
    shift = 0
    for i in range(offset, min(len(blob), offset + 10)):
        byte = blob[i]
        value |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            return value, i + 1
        shift += 7
    raise CellSongError("truncated varint")


def haar_transform(values: list[float]) -> list[float]:
    """Orthonormal recursive mean/difference transform."""
    n = len(values)
    out = values[:]
    temp = [0.0] * n
    length = n
    inv_sqrt2 = 1.0 / math.sqrt(2.0)
    while length > 1:
        half = length // 2
        for i in range(half):
            a = out[2 * i]
            b = out[2 * i + 1]
            temp[i] = (a + b) * inv_sqrt2
            temp[half + i] = (a - b) * inv_sqrt2
        out[:length] = temp[:length]
        length = half
    return out


def haar_inverse(coeffs: list[float]) -> list[float]:
    n = len(coeffs)
    out = coeffs[:]
    temp = [0.0] * n
    length = 1
    inv_sqrt2 = 1.0 / math.sqrt(2.0)
    while length < n:
        for i in range(length):
            avg = out[i]
            detail = out[length + i]
            temp[2 * i] = (avg + detail) * inv_sqrt2
            temp[2 * i + 1] = (avg - detail) * inv_sqrt2
        out[: 2 * length] = temp[: 2 * length]
        length *= 2
    return out


def floor_to_byte(value: float) -> int:
    if value < 0.0:
        return -1
    if value >= 256.0:
        return 256
    return int(math.floor(value))


def reconstruct_from_sparse(
    n: int,
    indices: list[int],
    coeff_values: list[float],
) -> list[float]:
    coeffs = [0.0] * n
    for idx, value in zip(indices, coeff_values):
        coeffs[idx] = value
    return haar_inverse(coeffs)


def sparse_song_for_block(block: bytes) -> tuple[list[int], list[float]] | None:
    n = len(block)
    if n == 0 or n & (n - 1):
        return None

    target = list(block)
    centers = [b + 0.5 for b in block]
    coeffs = haar_transform(centers)
    order = sorted(range(n), key=lambda i: abs(coeffs[i]), reverse=True)
    if 0 not in order:
        order.insert(0, 0)

    chosen: list[int] = []
    for idx in order:
        if idx not in chosen:
            chosen.append(idx)
        chosen_sorted = sorted(chosen)
        # Float32 is what the bitstream stores, so feasibility is tested after
        # the same quantization the decoder will see.
        packed_values = [
            struct.unpack("<f", struct.pack("<f", coeffs[i]))[0] for i in chosen_sorted
        ]
        recon = reconstruct_from_sparse(n, chosen_sorted, packed_values)
        decoded = [floor_to_byte(v) for v in recon]
        if decoded == target:
            return chosen_sorted, packed_values
    return None


def promising_block(block: bytes) -> bool:
    """Cheap gate before the expensive sparse feasibility search."""
    if not block:
        return False
    unique = len(set(block))
    if unique <= min(16, max(2, len(block) // 4)):
        return True
    if max(block) - min(block) <= 16:
        return True
    return False


def mask_bytes(indices: list[int], block_size: int) -> bytes:
    mask = bytearray(block_size // 8)
    for idx in indices:
        mask[idx // 8] |= 1 << (idx % 8)
    return bytes(mask)


def indices_from_mask(mask: bytes, block_size: int) -> list[int]:
    indices: list[int] = []
    for idx in range(block_size):
        if mask[idx // 8] & (1 << (idx % 8)):
            indices.append(idx)
    return indices


def compress_bytes(data: bytes, block_size: int = DEFAULT_BLOCK) -> bytes:
    if block_size < 2 or block_size & (block_size - 1):
        raise ValueError("block size must be a power of two")
    if block_size > 2048:
        raise ValueError("POC block size cap is 2048")

    header = bytearray()
    header += MAGIC
    header.append(VERSION)
    header += put_varint(len(data))
    header += put_varint(block_size)
    header += struct.pack("<I", binascii.crc32(data) & 0xFFFFFFFF)

    stream = bytearray()
    mask_len = block_size // 8
    pos = 0
    while pos < len(data):
        block = data[pos : pos + block_size]
        if len(block) == block_size and promising_block(block):
            song = sparse_song_for_block(block)
        else:
            song = None

        if song is not None:
            indices, coeff_values = song
            song_size = 1 + mask_len + 4 * len(indices)
            raw_size = 1 + len(put_varint(len(block))) + len(block)
            if song_size < raw_size:
                stream.append(SONG)
                stream += mask_bytes(indices, block_size)
                for value in coeff_values:
                    stream += struct.pack("<f", value)
                pos += len(block)
                continue

        stream.append(RAW)
        stream += put_varint(len(block))
        stream += block
        pos += len(block)

    raw_stream = bytearray()
    raw_stream.append(RAW)
    raw_stream += put_varint(len(data))
    raw_stream += data
    if len(raw_stream) < len(stream):
        stream = raw_stream

    return bytes(header + stream)


def decompress_bytes(blob: bytes) -> bytes:
    if len(blob) < len(MAGIC) + 1 or blob[:4] != MAGIC:
        raise CellSongError("bad cell-song magic")
    version = blob[4]
    if version != VERSION:
        raise CellSongError(f"unsupported version {version}")

    offset = 5
    original_size, offset = get_varint(blob, offset)
    block_size, offset = get_varint(blob, offset)
    if len(blob) < offset + 4:
        raise CellSongError("missing CRC")
    expected_crc = struct.unpack("<I", blob[offset : offset + 4])[0]
    offset += 4

    mask_len = block_size // 8
    out = bytearray()
    while len(out) < original_size:
        if offset >= len(blob):
            raise CellSongError("truncated block stream")
        kind = blob[offset]
        offset += 1

        if kind == RAW:
            size, offset = get_varint(blob, offset)
            out += blob[offset : offset + size]
            offset += size
        elif kind == SONG:
            mask = blob[offset : offset + mask_len]
            offset += mask_len
            indices = indices_from_mask(mask, block_size)
            coeff_values = []
            for _ in indices:
                if offset + 4 > len(blob):
                    raise CellSongError("truncated coefficient stream")
                coeff_values.append(struct.unpack("<f", blob[offset : offset + 4])[0])
                offset += 4
            recon = reconstruct_from_sparse(block_size, indices, coeff_values)
            out += bytes(floor_to_byte(v) for v in recon)
        else:
            raise CellSongError(f"unknown block kind {kind}")

    if len(out) != original_size:
        raise CellSongError("decoded length mismatch")
    if offset != len(blob):
        raise CellSongError("trailing bytes")
    crc = binascii.crc32(out) & 0xFFFFFFFF
    if crc != expected_crc:
        raise CellSongError("CRC mismatch")
    return bytes(out)


def block_stats(data: bytes, block_size: int = DEFAULT_BLOCK) -> tuple[int, int, int]:
    raw_blocks = 0
    song_blocks = 0
    song_coeffs = 0
    pos = 0
    while pos < len(data):
        block = data[pos : pos + block_size]
        song = (
            sparse_song_for_block(block)
            if len(block) == block_size and promising_block(block)
            else None
        )
        if song is None:
            raw_blocks += 1
        else:
            indices, _values = song
            mask_len = block_size // 8
            song_size = 1 + mask_len + 4 * len(indices)
            raw_size = 1 + len(put_varint(len(block))) + len(block)
            if song_size < raw_size:
                song_blocks += 1
                song_coeffs += len(indices)
            else:
                raw_blocks += 1
        pos += len(block)
    return raw_blocks, song_blocks, song_coeffs


def demo() -> None:
    constant = bytes([123] * 1024)
    smooth = bytes(90 + (i // 8) % 32 for i in range(1024))
    noisy = bytes((i * 73 + 19) & 255 for i in range(1024))
    for name, data in (("constant", constant), ("smooth-stairs", smooth), ("noisy", noisy)):
        packed = compress_bytes(data)
        restored = decompress_bytes(packed)
        raw_blocks, song_blocks, coeffs = block_stats(data)
        print(
            f"{name}: {len(data)} -> {len(packed)} bytes; "
            f"song_blocks={song_blocks}, raw_blocks={raw_blocks}, coeffs={coeffs}; "
            f"roundtrip={restored == data}"
        )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Rounding-cell spectral song POC")
    sub = parser.add_subparsers(dest="command", required=True)

    c = sub.add_parser("compress")
    c.add_argument("input", type=Path)
    c.add_argument("output", type=Path)
    c.add_argument("--block-size", type=int, default=DEFAULT_BLOCK)

    d = sub.add_parser("decompress")
    d.add_argument("input", type=Path)
    d.add_argument("output", type=Path)

    sub.add_parser("demo")

    args = parser.parse_args(argv)
    if args.command == "compress":
        data = args.input.read_bytes()
        packed = compress_bytes(data, args.block_size)
        args.output.write_bytes(packed)
        raw_blocks, song_blocks, coeffs = block_stats(data, args.block_size)
        print(
            f"cell-song compressed {len(data)} -> {len(packed)} bytes "
            f"(song_blocks={song_blocks}, raw_blocks={raw_blocks}, coeffs={coeffs})"
        )
        return 0
    if args.command == "decompress":
        data = decompress_bytes(args.input.read_bytes())
        args.output.write_bytes(data)
        print(f"cell-song decompressed {len(data)} bytes")
        return 0
    if args.command == "demo":
        demo()
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
