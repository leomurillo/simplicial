#!/usr/bin/env python3
"""SCANS v0: a finite-ledger dictionary wrapper around raw deflate.

The design goal is asymmetry: compression may spend time mining repeated
"packets" from the whole file, while decompression remains a small straight
line path: read header, inflate the dictionary, raw-deflate decode, verify.

This is a prototype, not a new entropy coder. The archimedean/entropy backend
is zlib's C implementation of deflate; the simplicial experiment is the
per-file finite ledger used as a preset dictionary.
"""

from __future__ import annotations

import argparse
import binascii
import collections
import re
import struct
import sys
import time
import zlib
from pathlib import Path
from typing import Iterable


MAGIC = b"SCN1"
METHOD_IDENTITY = 0
METHOD_LZP = 1
METHOD_ZSTD = 2
VERSION = 1
MAX_ZDICT = 32_768
LZP_BITS = 16
LZP_SIZE = 1 << LZP_BITS
LZP_MASK = LZP_SIZE - 1


class ScansError(RuntimeError):
    pass


def _put_varint(value: int) -> bytes:
    if value < 0:
        raise ValueError("varint cannot encode negative values")
    out = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            out.append(byte | 0x80)
        else:
            out.append(byte)
            return bytes(out)


def _get_varint(blob: bytes, offset: int) -> tuple[int, int]:
    shift = 0
    value = 0
    for i in range(offset, min(len(blob), offset + 10)):
        byte = blob[i]
        value |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            return value, i + 1
        shift += 7
    raise ScansError("truncated or oversized varint")


def _make_header(
    *,
    original_size: int,
    method: int,
    dict_len: int,
    dict_z_len: int,
    crc: int,
) -> bytes:
    if method > 15:
        raise ValueError("method id must fit in four bits")
    version_method = (VERSION << 4) | method
    return b"".join(
        (
            MAGIC,
            bytes([version_method]),
            _put_varint(original_size),
            _put_varint(dict_len),
            _put_varint(dict_z_len),
            struct.pack("<I", crc),
        )
    )


def _parse_header(blob: bytes) -> tuple[int, int, int, int, int, int]:
    if len(blob) < len(MAGIC) + 1:
        raise ScansError("input too small for SCANS header")
    if blob[: len(MAGIC)] != MAGIC:
        raise ScansError("bad SCANS magic")
    version_method = blob[len(MAGIC)]
    version = version_method >> 4
    method = version_method & 0x0F
    if version != VERSION:
        raise ScansError(f"unsupported SCANS version {version}")
    offset = len(MAGIC) + 1
    original_size, offset = _get_varint(blob, offset)
    dict_len, offset = _get_varint(blob, offset)
    dict_z_len, offset = _get_varint(blob, offset)
    if len(blob) < offset + 4:
        raise ScansError("truncated SCANS CRC")
    expected_crc = struct.unpack("<I", blob[offset : offset + 4])[0]
    offset += 4
    return original_size, method, dict_len, dict_z_len, expected_crc, offset


def _raw_deflate(data: bytes, zdict: bytes, level: int = 9) -> bytes:
    if zdict:
        compressor = zlib.compressobj(
            level=level,
            method=zlib.DEFLATED,
            wbits=-15,
            memLevel=9,
            strategy=zlib.Z_DEFAULT_STRATEGY,
            zdict=zdict,
        )
    else:
        compressor = zlib.compressobj(
            level=level,
            method=zlib.DEFLATED,
            wbits=-15,
            memLevel=9,
            strategy=zlib.Z_DEFAULT_STRATEGY,
        )
    return compressor.compress(data) + compressor.flush()


def _raw_inflate(payload: bytes, zdict: bytes) -> bytes:
    if zdict:
        decompressor = zlib.decompressobj(wbits=-15, zdict=zdict)
    else:
        decompressor = zlib.decompressobj(wbits=-15)
    out = decompressor.decompress(payload) + decompressor.flush()
    if decompressor.unused_data:
        raise ScansError("payload has trailing unused deflate data")
    return out


def _lzp_index(ctx: int) -> int:
    return ((ctx * 2_654_435_761) & 0xFFFFFFFF) >> (32 - LZP_BITS)


def lzp_encode(data: bytes) -> bytes:
    """Predictive residual transform with bit-packed hit flags.

    Each byte is predicted from a rolling 4-byte context. A hit costs one flag
    bit; a miss costs one flag bit plus the literal byte. The predictor table is
    rebuilt identically during decode, so no model is stored in the stream.
    """
    table = [-1] * LZP_SIZE
    out = bytearray()
    ctx = 0
    pos = 0
    n = len(data)
    while pos < n:
        flag_pos = len(out)
        out.append(0)
        flags = 0
        for bit in range(8):
            if pos >= n:
                break
            actual = data[pos]
            idx = _lzp_index(ctx)
            predicted = table[idx]
            if predicted == actual:
                flags |= 1 << bit
            else:
                out.append(actual)
            table[idx] = actual
            ctx = ((ctx << 8) | actual) & 0xFFFFFFFF
            pos += 1
        out[flag_pos] = flags
    return bytes(out)


def lzp_decode(encoded: bytes, original_size: int) -> bytes:
    table = [-1] * LZP_SIZE
    out = bytearray()
    out_extend = out.append
    ctx = 0
    pos = 0
    while len(out) < original_size:
        if pos >= len(encoded):
            raise ScansError("truncated LZP stream")
        flags = encoded[pos]
        pos += 1
        for bit in range(8):
            if len(out) >= original_size:
                break
            idx = _lzp_index(ctx)
            predicted = table[idx]
            if flags & (1 << bit):
                if predicted < 0:
                    raise ScansError("invalid LZP prediction hit")
                actual = predicted
            else:
                if pos >= len(encoded):
                    raise ScansError("truncated LZP literal")
                actual = encoded[pos]
                pos += 1
            out_extend(actual)
            table[idx] = actual
            ctx = ((ctx << 8) | actual) & 0xFFFFFFFF
    if pos != len(encoded):
        raise ScansError("LZP stream has trailing bytes")
    return bytes(out)


def _apply_transform(data: bytes, method: int) -> bytes:
    if method == METHOD_IDENTITY:
        return data
    if method == METHOD_LZP:
        return lzp_encode(data)
    raise ValueError(f"unknown transform method {method}")


def _reverse_transform(data: bytes, method: int, original_size: int) -> bytes:
    if method == METHOD_IDENTITY:
        return data
    if method == METHOD_LZP:
        return lzp_decode(data, original_size)
    raise ScansError(f"unsupported transform method {method}")


def _zstd_module():
    try:
        import zstandard as zstd  # type: ignore
    except ImportError as exc:
        raise ScansError(
            "zstandard is required for SCANS method 2; install with "
            "`python -m pip install zstandard` in a virtual environment"
        ) from exc
    return zstd


def pack_zstd(data: bytes, level: int = 19) -> tuple[bytes, dict[str, int]]:
    """Compress with an optimized Zstandard backend in the SCANS container."""
    zstd = _zstd_module()
    crc = binascii.crc32(data) & 0xFFFFFFFF
    compressor = zstd.ZstdCompressor(
        level=level,
        write_checksum=False,
        write_content_size=False,
    )
    payload = compressor.compress(data)
    header = _make_header(
        original_size=len(data),
        method=METHOD_ZSTD,
        dict_len=0,
        dict_z_len=0,
        crc=crc,
    )
    blob = header + payload
    return blob, {
        "method": METHOD_ZSTD,
        "transformed_size": len(data),
        "header_size": len(header),
        "dict_size": 0,
        "dict_z_size": 0,
        "payload_size": len(payload),
        "total_size": len(blob),
        "original_size": len(data),
        "zstd_level": level,
    }


def _sample_step(size: int) -> int:
    # Bound candidate mining cost on very large files without changing decode.
    return max(1, size // 2_000_000)


def _iter_ngram_candidates(data: bytes) -> Iterable[bytes]:
    size = len(data)
    if size < 64:
        return
    step = _sample_step(size)
    for n in (4, 5, 6, 8, 12, 16, 24, 32):
        if size < n * 3:
            continue
        for i in range(0, size - n + 1, step):
            chunk = data[i : i + n]
            # Skip all-zero-ish binary runs; deflate already handles them well
            # and they make poor preset dictionary entries.
            if len(set(chunk)) <= 1:
                continue
            yield chunk


def _iter_text_candidates(data: bytes) -> Iterable[bytes]:
    # Text and math-heavy corpora in this repo benefit from whole-token packets.
    token_re = re.compile(rb"[A-Za-z_\\][A-Za-z0-9_\\:\-\.\{\}]{3,63}")
    for match in token_re.finditer(data):
        token = match.group(0)
        yield token
        if len(token) + 1 <= 64:
            yield b" " + token
            yield token + b" "

    # Repeated Markdown/LaTeX punctuation packets.
    punct_re = re.compile(rb"[\$\{\}\\\[\]\(\)\|\-\*_`#:=,.;/ ]{4,48}")
    for match in punct_re.finditer(data):
        token = match.group(0)
        if len(set(token)) > 1:
            yield token


def build_dictionary(data: bytes, max_size: int = MAX_ZDICT) -> bytes:
    """Mine a zlib preset dictionary from repeated finite packets."""
    if max_size <= 0 or len(data) < 512:
        return b""
    max_size = min(max_size, MAX_ZDICT)

    counts: collections.Counter[bytes] = collections.Counter()
    counts.update(_iter_text_candidates(data))
    counts.update(_iter_ngram_candidates(data))

    scored: list[tuple[int, int, int, bytes]] = []
    for token, freq in counts.items():
        length = len(token)
        if freq < 3 or length < 4:
            continue
        # Approximate the value of making the packet available in the LZ window.
        # Header/dictionary cost is paid separately during model selection.
        gain = (freq - 1) * max(1, length - 3)
        if gain <= length:
            continue
        scored.append((gain, freq, length, token))

    if not scored:
        return b""

    # High-value packets should appear late in a zlib dictionary.
    scored.sort(key=lambda item: (item[0], item[1], item[2]))
    pieces: list[bytes] = []
    seen: set[bytes] = set()
    total = 0
    for _gain, _freq, _length, token in scored:
        if token in seen:
            continue
        seen.add(token)
        pieces.append(token)
        total += len(token)
        # Keep a little extra, then trim from the front so the best packets
        # remain closest to the dictionary end.
        if total > max_size * 2:
            joined = b"".join(pieces)
            joined = joined[-max_size:]
            pieces = [joined]
            total = len(joined)

    dictionary = b"".join(pieces)
    return dictionary[-max_size:]


def pack(
    data: bytes,
    level: int = 9,
    backend: str = "deflate",
) -> tuple[bytes, dict[str, int]]:
    """Compress bytes into SCANS format and return metadata."""
    if backend == "zstd":
        return pack_zstd(data, level=level)
    if backend != "deflate":
        raise ValueError(f"unknown SCANS backend: {backend}")

    full_dict = build_dictionary(data, MAX_ZDICT)

    dict_candidates: list[tuple[int, bytes]] = [(0, b"")]
    for size in (4_096, 8_192, 16_384, 32_768):
        if len(full_dict) >= max(512, size // 4):
            dict_candidates.append((min(size, len(full_dict)), full_dict[-size:]))

    best_blob: bytes | None = None
    best_meta: dict[str, int] | None = None
    crc = binascii.crc32(data) & 0xFFFFFFFF

    for method in (METHOD_IDENTITY, METHOD_LZP):
        transformed = _apply_transform(data, method)
        candidates = dict_candidates if method == METHOD_IDENTITY else [(0, b"")]
        for dict_size, zdict in candidates:
            payload = _raw_deflate(transformed, zdict, level=level)
            dict_z = zlib.compress(zdict, level) if zdict else b""
            header = _make_header(
                original_size=len(data),
                method=method,
                dict_len=len(zdict),
                dict_z_len=len(dict_z),
                crc=crc,
            )
            blob = header + dict_z + payload
            if best_blob is None or len(blob) < len(best_blob):
                best_blob = blob
                best_meta = {
                    "method": method,
                    "transformed_size": len(transformed),
                    "header_size": len(header),
                    "dict_size": dict_size,
                    "dict_z_size": len(dict_z),
                    "payload_size": len(payload),
                    "total_size": len(blob),
                    "original_size": len(data),
                }

    assert best_blob is not None and best_meta is not None
    return best_blob, best_meta


def unpack(blob: bytes) -> bytes:
    """Decompress SCANS bytes."""
    original_size, method, dict_len, dict_z_len, expected_crc, offset = _parse_header(blob)
    dict_z = blob[offset : offset + dict_z_len]
    payload = blob[offset + dict_z_len :]
    if len(dict_z) != dict_z_len or not payload:
        raise ScansError("truncated SCANS stream")

    if method == METHOD_ZSTD:
        if dict_len or dict_z_len:
            raise ScansError("SCANS-zstd does not use embedded zlib dictionaries")
        zstd = _zstd_module()
        decompressor = zstd.ZstdDecompressor()
        data = decompressor.decompress(payload, max_output_size=original_size)
        if len(data) != original_size:
            raise ScansError("original size mismatch")
        crc = binascii.crc32(data) & 0xFFFFFFFF
        if crc != expected_crc:
            raise ScansError("CRC mismatch")
        return data

    if method not in (METHOD_IDENTITY, METHOD_LZP):
        raise ScansError(f"unsupported transform method {method}")

    zdict = zlib.decompress(dict_z) if dict_z_len else b""
    if len(zdict) != dict_len:
        raise ScansError("dictionary length mismatch")

    transformed = _raw_inflate(payload, zdict)
    data = _reverse_transform(transformed, method, original_size)
    if len(data) != original_size:
        raise ScansError("original size mismatch")
    crc = binascii.crc32(data) & 0xFFFFFFFF
    if crc != expected_crc:
        raise ScansError("CRC mismatch")
    return data


def compress_file(input_path: Path, output_path: Path, level: int = 9) -> dict[str, int]:
    data = input_path.read_bytes()
    start = time.perf_counter()
    blob, meta = pack(data, level=level)
    meta["compress_seconds_x1000"] = int(round((time.perf_counter() - start) * 1000))
    output_path.write_bytes(blob)
    return meta


def decompress_file(input_path: Path, output_path: Path) -> int:
    blob = input_path.read_bytes()
    data = unpack(blob)
    output_path.write_bytes(data)
    return len(data)


def _main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="SCANS v0 codec")
    sub = parser.add_subparsers(dest="command", required=True)

    c = sub.add_parser("compress", help="compress a file")
    c.add_argument("input", type=Path)
    c.add_argument("output", type=Path)
    c.add_argument("--level", type=int, default=9)
    c.add_argument("--backend", choices=("deflate", "zstd"), default="deflate")

    d = sub.add_parser("decompress", help="decompress a file")
    d.add_argument("input", type=Path)
    d.add_argument("output", type=Path)

    args = parser.parse_args(argv)
    if args.command == "compress":
        data = args.input.read_bytes()
        start = time.perf_counter()
        blob, meta = pack(data, level=args.level, backend=args.backend)
        meta["compress_seconds_x1000"] = int(round((time.perf_counter() - start) * 1000))
        args.output.write_bytes(blob)
        print(
            "SCANS compressed "
            f"{meta['original_size']} -> {meta['total_size']} bytes "
            f"(method={meta['method']}, dict={meta['dict_size']}, "
            f"payload={meta['payload_size']})"
        )
        return 0
    if args.command == "decompress":
        size = decompress_file(args.input, args.output)
        print(f"SCANS decompressed {size} bytes")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
