#!/usr/bin/env python3
"""Mined residual-string transport estimator against WebP lossless.

This is the next all-native target after the N1/T13-T15 pass:

    gauge lift -> local predictor -> residual strings
    -> mined transported boundary strings -> Apex posterior estimate.

The transport is deliberately narrower than whole-block search. It mines prior
row strings with compatible residual packet signatures, tries phase-aware copy
commands, and only deploys the mined stream if it beats direct residual coding.
"""

from __future__ import annotations

import argparse
import io
import json
import math
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

import benchmark_sigi_vs_webp_fast as fast
import benchmark_subtile_transport_vs_webp as subtile
import cell_song_poc
import simplicial_image_codec as sigi


TRANSFORM = "g-bg-ravg"
TRANSFORMS = (
    "g-bg-ravg",
    "g-rg-bavg",
    "r-gr-bavg",
    "r-gr-bg",
    "r-gr-bmix-a",
    "r-gr-bmix-b",
    "b-rb-gavg",
    "ycocg",
    "green16",
    "rgb",
)
DEFAULT_STRING_LEN = 32
SEARCH_BACK = 6
FALLBACK_BACK = 2
MIN_ACCEPT_SAVE = 3
MIN_COPY_DIRECT_SCORE = 10
APEX_PRIOR_STRENGTHS = (8.0, 32.0, 128.0, 512.0)


@dataclass(frozen=True)
class StringRecord:
    index: int
    values: np.ndarray
    signature: tuple[int, int, int]


@dataclass(frozen=True)
class StringChoice:
    values: np.ndarray
    mode_id: int
    metadata_bytes: int
    model: str
    direct_score: int
    saved_direct_score: int


@dataclass(frozen=True)
class ResidualStream:
    items: list[tuple[int, int, int, int, int, int, int]]
    metadata_bytes: int
    energy_metadata_bytes: int
    unitary_metadata_bytes: int
    strings: int
    copy_strings: int
    dc_strings: int
    saved_direct_score_bytes: int
    model_counts: dict[str, int]


def literal_bits(symbol: int) -> int:
    return 8 * len(cell_song_poc.put_varint(symbol))


def signed_size(value: int) -> int:
    return sigi.signed_varint_size(int(value))


def varint_size(value: int) -> int:
    return len(cell_song_poc.put_varint(int(value)))


def residual_score_bytes(values: np.ndarray, contexts: np.ndarray) -> int:
    bits = fast.best_context_rice_bits(fast.zigzag_np(values), contexts)
    return (bits + 7) // 8


def transform_channels(rgb: bytes, width: int, height: int, mode: str) -> list[np.ndarray]:
    arr = fast.rgb_array(rgb, width, height)
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    if mode == "rgb":
        return [r, g, b]
    if mode in {"ycocg", "green16", "g-bg-ravg"}:
        return fast.transform_channels(rgb, width, height, mode)
    if mode == "g-rg-bavg":
        return [g, r - g, b - ((g + r) // 2)]
    if mode == "r-gr-bavg":
        return [r, g - r, b - ((r + g) // 2)]
    if mode == "r-gr-bg":
        return [r, g - r, b - g]
    if mode == "r-gr-bmix-a":
        return [r, g - r, b - ((-10 * r + 42 * g) // 32)]
    if mode == "r-gr-bmix-b":
        return [r, g - r, b - ((-12 * r + 44 * g) // 32)]
    if mode == "b-rb-gavg":
        return [b, r - b, g - ((b + r) // 2)]
    raise ValueError(f"unknown transform {mode}")


def command_metadata_size(distance: int, offset: int) -> int:
    # One command byte carries command family and phase. Then distance+offset.
    return 1 + varint_size(distance) + signed_size(offset)


def dc_metadata_size(offset: int) -> int:
    return 1 + signed_size(offset)


def string_signature(values: np.ndarray, context_values: np.ndarray) -> tuple[int, int, int]:
    energy = subtile.energy_class(float(np.mean(np.abs(values))))
    packet = subtile.unitary_packet_class(values.reshape(1, -1))
    context_mode = int(np.bincount(context_values.ravel(), minlength=sigi.RICE_CONTEXTS).argmax())
    return energy, packet, context_mode


def compatible_records(
    buckets: dict[tuple[int, int, int], deque[StringRecord]],
    all_records: deque[StringRecord],
    signature: tuple[int, int, int],
) -> list[StringRecord]:
    candidates: list[StringRecord] = []
    for key in (
        signature,
        (signature[0], signature[1], -1),
        (signature[0], -1, signature[2]),
    ):
        bucket = buckets.get(key)
        if bucket:
            candidates.extend(reversed(bucket))
        if len(candidates) >= SEARCH_BACK:
            return candidates[:SEARCH_BACK]
    return list(reversed(all_records))[: min(FALLBACK_BACK, len(all_records))]


def remember_record(
    buckets: dict[tuple[int, int, int], deque[StringRecord]],
    all_records: deque[StringRecord],
    record: StringRecord,
) -> None:
    all_records.append(record)
    energy, packet, ctx = record.signature
    for key in (record.signature, (energy, packet, -1), (energy, -1, ctx)):
        bucket = buckets[key]
        bucket.append(record)


def choose_string(
    values: np.ndarray,
    contexts: np.ndarray,
    buckets: dict[tuple[int, int, int], deque[StringRecord]],
    all_records: deque[StringRecord],
    string_index: int,
) -> StringChoice:
    direct_score = residual_score_bytes(values, contexts)
    best = StringChoice(
        values=values,
        mode_id=0,
        metadata_bytes=0,
        model="direct",
        direct_score=direct_score,
        saved_direct_score=0,
    )

    offset = int(np.rint(float(np.mean(values))))
    if offset:
        tail = values - offset
        metadata = dc_metadata_size(offset)
        score = metadata + residual_score_bytes(tail, contexts)
        if score <= direct_score - best.saved_direct_score - MIN_ACCEPT_SAVE:
            best = StringChoice(
                values=tail,
                mode_id=1,
                metadata_bytes=metadata,
                model="dc",
                direct_score=direct_score,
                saved_direct_score=direct_score - score,
            )

    if direct_score >= MIN_COPY_DIRECT_SCORE and all_records:
        signature = string_signature(values, contexts)
        for record in compatible_records(buckets, all_records, signature):
            if record.values.shape != values.shape:
                continue
            distance = string_index - record.index
            for sign, mode_id, model in ((1, 2, "copy+"), (-1, 3, "copy-")):
                prediction = sign * record.values
                copy_offset = int(np.rint(float(np.mean(values - prediction))))
                tail = values - prediction - copy_offset
                metadata = command_metadata_size(distance, copy_offset)
                coarse = metadata + float(np.mean(np.abs(tail))) * tail.size / 8.0
                if coarse > direct_score - best.saved_direct_score - MIN_ACCEPT_SAVE:
                    continue
                score = metadata + residual_score_bytes(tail, contexts)
                if score <= direct_score - best.saved_direct_score - MIN_ACCEPT_SAVE:
                    best = StringChoice(
                        values=tail,
                        mode_id=mode_id,
                        metadata_bytes=metadata,
                        model=model,
                        direct_score=direct_score,
                        saved_direct_score=direct_score - score,
                    )

    return best


def gather_stream(
    rgb: bytes,
    width: int,
    height: int,
    string_len: int,
    *,
    transform: str,
    mine: bool,
) -> ResidualStream:
    items: list[tuple[int, int, int, int, int, int, int]] = []
    metadata_bytes = 0
    tile_energy_units = 0
    string_count = 0
    copy_strings = 0
    dc_strings = 0
    saved_direct = 0
    model_counts: Counter[str] = Counter()

    channels = transform_channels(rgb, width, height, transform)
    for channel_index, channel in enumerate(channels):
        left, up, up_left, up_right = fast.shifted_neighbors(channel)
        gradient = np.abs(left - up) + np.abs(left - up_left) + np.abs(up - up_left) + np.abs(up - up_right)
        contexts = np.searchsorted(fast.CONTEXT_THRESHOLDS, gradient, side="right").astype(np.uint8)
        residuals, tile_energy, tile_unitary, tile_metadata, channel_energy_units, predictors = (
            subtile.gather_baseline_residuals(channel, contexts)
        )
        metadata_bytes += tile_metadata
        tile_energy_units += channel_energy_units
        model_counts.update(predictors)

        buckets: dict[tuple[int, int, int], deque[StringRecord]] = defaultdict(
            lambda: deque(maxlen=SEARCH_BACK * 4)
        )
        all_records: deque[StringRecord] = deque(maxlen=SEARCH_BACK * 8)

        h, w = channel.shape
        for y in range(h):
            for x in range(0, w, string_len):
                xs = slice(x, min(x + string_len, w))
                values = residuals[y, xs]
                string_contexts = contexts[y, xs]
                if mine:
                    choice = choose_string(values, string_contexts, buckets, all_records, string_count)
                else:
                    choice = StringChoice(
                        values=values,
                        mode_id=0,
                        metadata_bytes=0,
                        model="direct",
                        direct_score=0,
                        saved_direct_score=0,
                    )
                metadata_bytes += choice.metadata_bytes
                model_counts[choice.model] += 1
                saved_direct += choice.saved_direct_score
                if choice.mode_id == 1:
                    dc_strings += 1
                elif choice.mode_id in (2, 3):
                    copy_strings += 1

                tile_y = (y // sigi.TILE) * sigi.TILE
                tile_x = (x // sigi.TILE) * sigi.TILE
                grad_class = subtile.gradient_class(int(np.mean(gradient[y, xs])))
                energy_class = int(tile_energy[tile_y, tile_x])
                unitary_class = int(tile_unitary[tile_y, tile_x])
                for ctx, value in zip(string_contexts.ravel(), choice.values.ravel()):
                    items.append(
                        (
                            channel_index,
                            int(ctx),
                            choice.mode_id,
                            grad_class,
                            energy_class,
                            unitary_class,
                            sigi.zigzag(int(value)),
                        )
                    )

                if mine:
                    remember_record(
                        buckets,
                        all_records,
                        StringRecord(
                            index=string_count,
                            values=values.copy(),
                            signature=string_signature(values, string_contexts),
                        ),
                    )
                string_count += 1

    if mine:
        metadata_bytes += (string_count + 7) // 8

    return ResidualStream(
        items=items,
        metadata_bytes=metadata_bytes,
        energy_metadata_bytes=(tile_energy_units * 3 + 7) // 8,
        unitary_metadata_bytes=(tile_energy_units * 2 + 7) // 8,
        strings=string_count,
        copy_strings=copy_strings,
        dc_strings=dc_strings,
        saved_direct_score_bytes=saved_direct,
        model_counts=dict(model_counts),
    )


def adaptive_bits(items: list[tuple[int, int, int, int, int, int, int]], fields: tuple[int, ...]) -> tuple[float, int, int]:
    counts: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    totals: dict[tuple[int, ...], int] = defaultdict(int)
    bits = 0.0
    new_symbols = 0
    for item in items:
        key = tuple(item[index] for index in fields)
        symbol = item[-1]
        counter = counts[key]
        total = totals[key]
        if counter[symbol]:
            bits += -math.log2(counter[symbol] / (total + 1.0))
        else:
            bits += math.log2(total + 1.0) + literal_bits(symbol)
            new_symbols += 1
        counter[symbol] += 1
        totals[key] = total + 1
    return bits, new_symbols, len(counts)


def apex_integer_prior(symbol: int) -> float:
    # Telescoping native integer prior: q(n)=1/((n+1)(n+2)), sum q(n)=1.
    n = float(symbol) + 1.0
    return 1.0 / (n * (n + 1.0))


def apex_seeded_bits(
    items: list[tuple[int, int, int, int, int, int, int]],
    fields: tuple[int, ...],
    strength: float,
) -> tuple[float, int, int]:
    counts: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    totals: dict[tuple[int, ...], int] = defaultdict(int)
    bits = 0.0
    new_symbols = 0
    for item in items:
        key = tuple(item[index] for index in fields)
        symbol = item[-1]
        counter = counts[key]
        total = totals[key]
        if counter[symbol] == 0:
            new_symbols += 1
        probability = (counter[symbol] + strength * apex_integer_prior(symbol)) / (total + strength)
        bits += -math.log2(probability)
        counter[symbol] += 1
        totals[key] = total + 1
    return bits, new_symbols, len(counts)


def static_ideal_bits(items: list[tuple[int, int, int, int, int, int, int]], fields: tuple[int, ...]) -> float:
    counts: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    for item in items:
        counts[tuple(item[index] for index in fields)][item[-1]] += 1
    bits = 0.0
    for counter in counts.values():
        total = sum(counter.values())
        for count in counter.values():
            bits += count * math.log2(total / count)
    return bits


def estimate_stream(rgb: bytes, width: int, height: int, stream: ResidualStream) -> dict[str, object]:
    header = fast.sigi_header_size(rgb, width, height) + 1
    results: dict[str, dict[str, object]] = {}
    for name, fields in {
        "ch-ctx": (0, 1),
        "ch-ctx-grad": (0, 1, 3),
        "ch-ctx-mode": (0, 1, 2),
        "ch-ctx-mode-grad": (0, 1, 2, 3),
        "ch-ctx-energy": (0, 1, 4),
        "ch-ctx-unitary": (0, 1, 5),
        "ch-ctx-energy-unitary": (0, 1, 4, 5),
        "ch-ctx-grad-energy-unitary": (0, 1, 3, 4, 5),
    }.items():
        bits, new_symbols, context_count = adaptive_bits(stream.items, fields)
        ideal = static_ideal_bits(stream.items, fields)
        extra_metadata = 0
        if 4 in fields:
            extra_metadata += stream.energy_metadata_bytes
        if 5 in fields:
            extra_metadata += stream.unitary_metadata_bytes
        results[name] = {
            "bytes": header + stream.metadata_bytes + extra_metadata + math.ceil(bits / 8),
            "ideal_no_codebook_bytes": header + stream.metadata_bytes + extra_metadata + math.ceil(ideal / 8),
            "contexts": context_count,
            "new_symbols": new_symbols,
            "extra_metadata_bytes": extra_metadata,
        }
        for strength in APEX_PRIOR_STRENGTHS:
            seeded_bits, seeded_new_symbols, seeded_context_count = apex_seeded_bits(
                stream.items, fields, strength
            )
            seeded_name = f"{name}-apex{int(strength)}"
            results[seeded_name] = {
                "bytes": header + stream.metadata_bytes + extra_metadata + math.ceil(seeded_bits / 8),
                "ideal_no_codebook_bytes": header + stream.metadata_bytes + extra_metadata + math.ceil(ideal / 8),
                "contexts": seeded_context_count,
                "new_symbols": seeded_new_symbols,
                "extra_metadata_bytes": extra_metadata,
                "prior_strength": strength,
            }

    best_name, best = min(results.items(), key=lambda item: int(item[1]["bytes"]))
    ideal_name, ideal = min(results.items(), key=lambda item: int(item[1]["ideal_no_codebook_bytes"]))
    return {
        "best_scheme": best_name,
        "bytes": int(best["bytes"]),
        "ideal_best_scheme": ideal_name,
        "ideal_no_codebook_bytes": int(ideal["ideal_no_codebook_bytes"]),
        "metadata_bytes": stream.metadata_bytes,
        "energy_metadata_bytes": stream.energy_metadata_bytes,
        "unitary_metadata_bytes": stream.unitary_metadata_bytes,
        "strings": stream.strings,
        "copy_strings": stream.copy_strings,
        "dc_strings": stream.dc_strings,
        "saved_direct_score_bytes": stream.saved_direct_score_bytes,
        "model_counts": stream.model_counts,
        "schemes": results,
    }


def benchmark_transform(
    rgb: bytes,
    width: int,
    height: int,
    string_len: int,
    transform: str,
    *,
    mine: bool,
) -> dict[str, object]:
    direct = estimate_stream(
        rgb,
        width,
        height,
        gather_stream(rgb, width, height, string_len, transform=transform, mine=False),
    )
    if mine:
        mined = estimate_stream(
            rgb,
            width,
            height,
            gather_stream(rgb, width, height, string_len, transform=transform, mine=True),
        )
    else:
        mined = direct
    deployed = min((direct, mined), key=lambda estimate: int(estimate["bytes"]))
    return {
        "transform": transform,
        "direct_string_apex": direct,
        "mined_string_apex": mined,
        "deployed_apex": deployed,
    }


def benchmark_image(path: Path, crop_size: int, string_len: int, transforms: list[str], *, mine: bool) -> dict[str, object]:
    with Image.open(path) as image:
        image = fast.center_crop(image.convert("RGB"), crop_size)
        width, height = image.size
        rgb = image.tobytes()

    webp_start = time.perf_counter()
    buf = io.BytesIO()
    Image.frombytes("RGB", (width, height), rgb).save(
        buf,
        format="WEBP",
        lossless=True,
        quality=100,
        method=6,
    )
    webp_size = len(buf.getvalue())
    webp_s = time.perf_counter() - webp_start

    start = time.perf_counter()
    transform_results = [
        benchmark_transform(rgb, width, height, string_len, transform, mine=mine) for transform in transforms
    ]
    best_transform = min(transform_results, key=lambda result: int(result["deployed_apex"]["bytes"]))  # type: ignore[index]
    elapsed = time.perf_counter() - start

    return {
        "file": str(path),
        "crop_size": crop_size,
        "string_len": string_len,
        "width": width,
        "height": height,
        "raw_rgb_bytes": len(rgb),
        "webp_lossless_bytes": webp_size,
        "webp_lossless_encode_s": webp_s,
        "transform": best_transform["transform"],
        "direct_string_apex": best_transform["direct_string_apex"],
        "mined_string_apex": best_transform["mined_string_apex"],
        "deployed_apex": best_transform["deployed_apex"],
        "transform_results": transform_results,
        "estimate_s": elapsed,
    }


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# Mined Residual Strings + Apex Posterior vs WebP",
        "",
        "The model chooses among reversible native color gauges, keeps local tile predictors, then optionally mines row residual strings with compatible energy/unitary/context signatures. Coding uses either literal-start adaptive contexts or a deterministic Apex integer prior followed by posterior updates, so the decoder gets a shared native seed with no histogram side table. The deployed estimate is the smaller of direct residual strings and mined string commands.",
        "",
        "| file | dimensions | gauge | len | WebP | direct strings | mined strings | deployed | best state | ideal | vs WebP | DC | copy |",
        "|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|",
    ]
    total_webp = total_deployed = total_ideal = 0
    for row in rows:
        webp = int(row["webp_lossless_bytes"])
        direct = row["direct_string_apex"]  # type: ignore[assignment]
        mined = row["mined_string_apex"]  # type: ignore[assignment]
        deployed = row["deployed_apex"]  # type: ignore[assignment]
        direct_bytes = int(direct["bytes"])  # type: ignore[index]
        mined_bytes = int(mined["bytes"])  # type: ignore[index]
        deployed_bytes = int(deployed["bytes"])  # type: ignore[index]
        ideal = int(deployed["ideal_no_codebook_bytes"])  # type: ignore[index]
        total_webp += webp
        total_deployed += deployed_bytes
        total_ideal += ideal
        lines.append(
            f"| {Path(str(row['file'])).name} | {row['width']}x{row['height']} | `{row['transform']}` | "
            f"{row['string_len']} | {webp:,} | {direct_bytes:,} | {mined_bytes:,} | "
            f"{deployed_bytes:,} | `{deployed['best_scheme']}` | {ideal:,} | "
            f"{deployed_bytes - webp:+,} ({((deployed_bytes / webp) - 1.0) * 100.0:+.2f}%) | "
            f"{deployed['dc_strings']} | {deployed['copy_strings']} |"  # type: ignore[index]
        )
    lines += [
        "",
        "## Totals",
        "",
        f"- WebP lossless bytes: `{total_webp:,}`",
        f"- Deployed native bytes: `{total_deployed:,}`",
        f"- Deployed native vs WebP: `{total_deployed - total_webp:+,}` bytes "
        f"({((total_deployed / total_webp) - 1.0) * 100.0:+.2f}%)",
        f"- Ideal no-codebook bytes: `{total_ideal:,}`",
        f"- Ideal no-codebook vs WebP: `{total_ideal - total_webp:+,}` bytes "
        f"({((total_ideal / total_webp) - 1.0) * 100.0:+.2f}%)",
        "",
        "## Notes",
        "",
        "- This is an estimator, not a final bitstream.",
        "- Gauge selection is charged as part of the existing mode byte in the SIGI-style header.",
        "- Mined metadata includes predictor bytes, one sparse command-flag bit per string, and command bytes for DC/copy strings.",
        "- Unitary/energy packet contexts are charged as side metadata when used.",
        "- Apex-seeded schemes use `q(n)=1/((n+1)(n+2))` over zigzag residuals, mixed into each context before adaptive updates.",
    ]
    for row in rows:
        mined = row["mined_string_apex"]  # type: ignore[assignment]
        lines.append(
            f"- `{Path(str(row['file'])).name}` mined strings: `{mined['strings']}`, "
            f"copy: `{mined['copy_strings']}`, DC: `{mined['dc_strings']}`, "
            f"local score saved: `{mined['saved_direct_score_bytes']}`."  # type: ignore[index]
        )
        lines.append(
            f"- `{Path(str(row['file'])).name}` mined model counts: `{mined['model_counts']}`."  # type: ignore[index]
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--crop-size", type=int, default=512)
    parser.add_argument("--string-len", type=int, default=DEFAULT_STRING_LEN)
    parser.add_argument("--transforms", default=TRANSFORM)
    parser.add_argument("--all-transforms", action="store_true")
    parser.add_argument("--no-mine", action="store_true")
    parser.add_argument("--json", type=Path, default=Path("empirical/compression/reports/mined_strings_vs_webp.json"))
    parser.add_argument("--report", type=Path, default=Path("empirical/compression/reports/mined_strings_vs_webp.md"))
    args = parser.parse_args(argv)

    if args.string_len <= 0:
        raise SystemExit("--string-len must be positive")
    transforms = list(TRANSFORMS) if args.all_transforms else [item.strip() for item in args.transforms.split(",") if item.strip()]
    if not transforms:
        raise SystemExit("at least one transform is required")
    unknown = [transform for transform in transforms if transform not in TRANSFORMS]
    if unknown:
        raise SystemExit(f"unknown transform(s): {', '.join(unknown)}")

    rows = []
    for path in args.images:
        print(f"benchmarking {path}...", file=sys.stderr)
        rows.append(benchmark_image(path, args.crop_size, args.string_len, transforms, mine=not args.no_mine))
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_report(rows, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
