"""Audit the Prime Projection Conjecture presets against a local model.

This is not the original ARTexplorer search code.  It is a small independent
reconstruction from the v5.1 PDF:

* tetrahedral/Quadray point sets are generated locally;
* rational spreads are converted to algebraic float rotations;
* all plausible axis orders, sine signs, and projection axes are scanned;
* convex hull orientation tests use ``Fraction(float)`` exactly, matching the
  PDF's "Path C" verification model.

The goal is to separate robust geometric facts from convention-sensitive
claims.  If a claimed preset only works for one hidden Euler/projection
convention, this script should make that dependency visible.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
import json
import math
from pathlib import Path
from typing import Callable, Iterable


Point3 = tuple[float, float, float]
Point2 = tuple[float, float]

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "empirical" / "reports"
JSON_OUT = REPORT_DIR / "prime_projection_conjecture_audit.json"
MD_OUT = REPORT_DIR / "prime_projection_conjecture_audit.md"


@dataclass(frozen=True)
class Claim:
    name: str
    target: int
    spreads: tuple[Fraction, Fraction, Fraction]
    source_keys: tuple[str, ...]
    note: str


@dataclass(frozen=True)
class Convention:
    order: str
    signs: tuple[int, int, int]
    drop_axis: str


def add(a: Point3, b: Point3) -> Point3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def mul(k: float, p: Point3) -> Point3:
    return (k * p[0], k * p[1], k * p[2])


def norm(p: Point3) -> float:
    return math.sqrt(p[0] * p[0] + p[1] * p[1] + p[2] * p[2])


def normalize(p: Point3) -> Point3:
    r = norm(p)
    if r == 0:
        raise ValueError("cannot normalize zero point")
    return (p[0] / r, p[1] / r, p[2] / r)


def radial_normalize(points: Iterable[Point3]) -> list[Point3]:
    return [normalize(p) for p in points]


def dedup(points: Iterable[Point3], digits: int = 12) -> list[Point3]:
    seen: dict[tuple[float, float, float], Point3] = {}
    for p in points:
        key = (round(p[0], digits), round(p[1], digits), round(p[2], digits))
        seen.setdefault(key, p)
    return list(seen.values())


SQRT3 = math.sqrt(3.0)

# Same tetrahedral labeling as the local simplicial-vector scripts.
TETRA: tuple[Point3, ...] = (
    (-1.0 / SQRT3, -1.0 / SQRT3, 1.0 / SQRT3),
    (1.0 / SQRT3, 1.0 / SQRT3, 1.0 / SQRT3),
    (1.0 / SQRT3, -1.0 / SQRT3, -1.0 / SQRT3),
    (-1.0 / SQRT3, 1.0 / SQRT3, -1.0 / SQRT3),
)


def quadray_to_xyz(q: tuple[float, float, float, float]) -> Point3:
    out = (0.0, 0.0, 0.0)
    for coeff, basis in zip(q, TETRA):
        out = add(out, mul(coeff, basis))
    return out


def truncated_tetrahedron() -> list[Point3]:
    points: list[Point3] = []
    base = (2.0, 1.0, 0.0, 0.0)
    for perm in set(permutations(base)):
        points.append(quadray_to_xyz(tuple(v / 3.0 for v in perm)))
    return dedup(points)


def tetrahedron() -> list[Point3]:
    return list(TETRA)


def dual_tetrahedron() -> list[Point3]:
    return [mul(-1.0, p) for p in TETRA]


def icosahedron() -> list[Point3]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    points: list[Point3] = []
    for a in (-1.0, 1.0):
        for b in (-phi, phi):
            points.append((0.0, a, b))
            points.append((a, b, 0.0))
            points.append((b, 0.0, a))
    return radial_normalize(dedup(points))


def geodesic_tetrahedron(freq: int) -> list[Point3]:
    faces = ((0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2))
    points: list[Point3] = []
    for face in faces:
        a, b, c = (TETRA[i] for i in face)
        for i in range(freq + 1):
            for j in range(freq + 1 - i):
                k = freq - i - j
                p = add(add(mul(i / freq, a), mul(j / freq, b)), mul(k / freq, c))
                points.append(normalize(p))
    return dedup(points)


def make_sources() -> dict[str, list[Point3]]:
    trunc = truncated_tetrahedron()
    tet = tetrahedron()
    dual = dual_tetrahedron()
    ico = icosahedron()
    return {
        "trunc_tet_raw": trunc,
        "trunc_tet_radial": radial_normalize(trunc),
        "trunc_tet_plus_tet_raw": dedup([*trunc, *tet]),
        "trunc_tet_plus_tet_radial": dedup([*radial_normalize(trunc), *tet]),
        "trunc_tet_plus_dual_raw": dedup([*trunc, *dual]),
        "trunc_tet_plus_dual_radial": dedup([*radial_normalize(trunc), *dual]),
        "trunc_tet_plus_icosa_raw": dedup([*trunc, *ico]),
        "trunc_tet_plus_icosa_radial": dedup([*radial_normalize(trunc), *ico]),
        "geodesic_tet_f2": geodesic_tetrahedron(2),
        "geodesic_tet_f4": geodesic_tetrahedron(4),
    }


def rotate_axis(p: Point3, axis: str, c: float, s: float) -> Point3:
    x, y, z = p
    if axis == "X":
        return (x, c * y - s * z, s * y + c * z)
    if axis == "Y":
        return (c * x + s * z, y, -s * x + c * z)
    if axis == "Z":
        return (c * x - s * y, s * x + c * y, z)
    raise ValueError(axis)


def rotate_point(
    p: Point3,
    spreads: tuple[Fraction, Fraction, Fraction],
    convention: Convention,
) -> Point3:
    # Spreads are assigned to X, Y, Z; order controls application sequence.
    by_axis = {axis: spread for axis, spread in zip("XYZ", spreads)}
    sign_by_axis = {axis: sign for axis, sign in zip("XYZ", convention.signs)}
    out = p
    for axis in convention.order:
        spread = by_axis[axis]
        sin_value = sign_by_axis[axis] * math.sqrt(float(spread))
        cos_value = math.sqrt(max(0.0, 1.0 - float(spread)))
        out = rotate_axis(out, axis, cos_value, sin_value)
    return out


def project_point(p: Point3, drop_axis: str) -> Point2:
    x, y, z = p
    if drop_axis == "X":
        return (y, z)
    if drop_axis == "Y":
        return (x, z)
    if drop_axis == "Z":
        return (x, y)
    raise ValueError(drop_axis)


def frac_point(p: Point2) -> tuple[Fraction, Fraction]:
    return (Fraction(p[0]), Fraction(p[1]))


def cross_frac(
    o: tuple[Fraction, Fraction],
    a: tuple[Fraction, Fraction],
    b: tuple[Fraction, Fraction],
) -> Fraction:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points: list[Point2]) -> list[int]:
    # Deduplicate by the exact rational encoded by each Float64 coordinate.
    exact_to_index: dict[tuple[Fraction, Fraction], int] = {}
    for i, point in enumerate(points):
        exact_to_index.setdefault(frac_point(point), i)
    ordered = sorted(exact_to_index)
    if len(ordered) <= 1:
        return [exact_to_index[p] for p in ordered]

    def build_half(seq: list[tuple[Fraction, Fraction]]) -> list[tuple[Fraction, Fraction]]:
        half: list[tuple[Fraction, Fraction]] = []
        for point in seq:
            while len(half) >= 2 and cross_frac(half[-2], half[-1], point) <= 0:
                half.pop()
            half.append(point)
        return half

    lower = build_half(ordered)
    upper = build_half(list(reversed(ordered)))
    hull_exact = lower[:-1] + upper[:-1]
    return [exact_to_index[p] for p in hull_exact]


def interior_angles(points: list[Point2], hull: list[int]) -> list[float]:
    if len(hull) < 3:
        return []
    angles: list[float] = []
    for offset, index in enumerate(hull):
        prev_p = points[hull[offset - 1]]
        p = points[index]
        next_p = points[hull[(offset + 1) % len(hull)]]
        a = (prev_p[0] - p[0], prev_p[1] - p[1])
        b = (next_p[0] - p[0], next_p[1] - p[1])
        la = math.hypot(*a)
        lb = math.hypot(*b)
        if la == 0.0 or lb == 0.0:
            angles.append(180.0)
            continue
        dot = max(-1.0, min(1.0, (a[0] * b[0] + a[1] * b[1]) / (la * lb)))
        angles.append(math.degrees(math.acos(dot)))
    return angles


def audit_source(
    points: list[Point3],
    spreads: tuple[Fraction, Fraction, Fraction],
    convention: Convention,
) -> dict[str, object]:
    rotated = [rotate_point(p, spreads, convention) for p in points]
    projected = [project_point(p, convention.drop_axis) for p in rotated]
    hull = convex_hull(projected)
    angles = interior_angles(projected, hull)
    return {
        "hull_count": len(hull),
        "max_interior_angle": max(angles) if angles else None,
        "min_interior_angle": min(angles) if angles else None,
        "clean_under_179": bool(angles and max(angles) < 179.0),
        "hull_indices": hull,
    }


def conventions() -> list[Convention]:
    out: list[Convention] = []
    for order in ("".join(p) for p in permutations("XYZ")):
        for signs in product((-1, 1), repeat=3):
            for drop_axis in "XYZ":
                out.append(Convention(order=order, signs=signs, drop_axis=drop_axis))
    return out


def claims() -> list[Claim]:
    return [
        Claim(
            name="5_truncated_tet",
            target=5,
            spreads=(Fraction(0), Fraction(1, 2), Fraction(0)),
            source_keys=("trunc_tet_raw", "trunc_tet_radial"),
            note="PDF: truncated tetrahedron, s=(0,1/2,0).",
        ),
        Claim(
            name="7_trunc_tet_compound",
            target=7,
            spreads=(Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
            source_keys=(
                "trunc_tet_plus_dual_raw",
                "trunc_tet_plus_dual_radial",
                "trunc_tet_plus_tet_raw",
                "trunc_tet_plus_tet_radial",
            ),
            note="PDF: TruncTet plus DualTet/Tet, s=(1/2,1/2,1/2).",
        ),
        Claim(
            name="11_trunc_tet_icosa",
            target=11,
            spreads=(Fraction(3, 4), Fraction(1, 4), Fraction(1, 2)),
            source_keys=("trunc_tet_plus_icosa_raw", "trunc_tet_plus_icosa_radial"),
            note="PDF: TruncTet plus Icosahedron, s=(3/4,1/4,1/2).",
        ),
        Claim(
            name="13_trunc_tet_icosa",
            target=13,
            spreads=(Fraction(9, 10), Fraction(24, 25), Fraction(19, 20)),
            source_keys=("trunc_tet_plus_icosa_raw", "trunc_tet_plus_icosa_radial"),
            note="PDF: TruncTet plus Icosahedron, s=(9/10,24/25,19/20).",
        ),
        Claim(
            name="7_geodesic_tet_f2",
            target=7,
            spreads=(Fraction(0), Fraction(1, 3), Fraction(1, 3)),
            source_keys=("geodesic_tet_f2",),
            note="PDF: geodesic tetrahedron f=2, s=(0,1/3,1/3).",
        ),
        Claim(
            name="11_geodesic_tet_f4",
            target=11,
            spreads=(Fraction(3, 4), Fraction(1, 3), Fraction(1, 3)),
            source_keys=("geodesic_tet_f4",),
            note="PDF: geodesic tetrahedron f=4, s=(3/4,1/3,1/3).",
        ),
        Claim(
            name="13_geodesic_tet_f4_sqrt2",
            target=13,
            spreads=(Fraction(1, 2), Fraction(3, 4), Fraction(3, 4)),
            source_keys=("geodesic_tet_f4",),
            note="PDF: geodesic tetrahedron f=4, s=(1/2,3/4,3/4).",
        ),
        Claim(
            name="13_geodesic_tet_f4_alt",
            target=13,
            spreads=(Fraction(1, 3), Fraction(2, 3), Fraction(3, 4)),
            source_keys=("geodesic_tet_f4",),
            note="PDF table also lists a geodesic f=4 13-gon-like row, read as s=(1/3,2/3,3/4).",
        ),
    ]


def summarize_claim(
    claim: Claim,
    sources: dict[str, list[Point3]],
    all_conventions: list[Convention],
) -> dict[str, object]:
    target_matches: list[dict[str, object]] = []
    clean_target_matches: list[dict[str, object]] = []
    histogram: dict[str, int] = {}
    best_by_target_gap: tuple[int, str, Convention, dict[str, object]] | None = None

    for source_key in claim.source_keys:
        points = sources[source_key]
        for convention in all_conventions:
            result = audit_source(points, claim.spreads, convention)
            count = int(result["hull_count"])
            histogram[str(count)] = histogram.get(str(count), 0) + 1
            gap = abs(count - claim.target)
            if best_by_target_gap is None or gap < best_by_target_gap[0]:
                best_by_target_gap = (gap, source_key, convention, result)
            if count == claim.target:
                row = {
                    "source": source_key,
                    "order": convention.order,
                    "signs_xyz": convention.signs,
                    "drop_axis": convention.drop_axis,
                    **result,
                }
                target_matches.append(row)
                if result["clean_under_179"]:
                    clean_target_matches.append(row)

    assert best_by_target_gap is not None
    _, best_source, best_convention, best_result = best_by_target_gap
    return {
        "target": claim.target,
        "spreads": [str(s) for s in claim.spreads],
        "note": claim.note,
        "source_vertex_counts": {key: len(sources[key]) for key in claim.source_keys},
        "hull_count_histogram": dict(sorted(histogram.items(), key=lambda kv: int(kv[0]))),
        "target_match_count": len(target_matches),
        "clean_target_match_count": len(clean_target_matches),
        "sample_clean_target_matches": clean_target_matches[:12],
        "sample_target_matches": target_matches[:12],
        "nearest": {
            "source": best_source,
            "order": best_convention.order,
            "signs_xyz": best_convention.signs,
            "drop_axis": best_convention.drop_axis,
            **best_result,
        },
    }


def low_tier_pentagon_examples(
    sources: dict[str, list[Point3]],
    all_conventions: list[Convention],
    limit: int = 12,
) -> list[dict[str, object]]:
    """Find a few clean 5-hull examples for the truncated tetrahedron.

    This is a follow-up to the one failed preset.  It answers a narrower
    question: does the reconstructed truncated tetrahedron produce clean
    pentagonal shadows at nearby low-tier spreads at all?
    """
    values = (
        Fraction(0),
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 4),
        Fraction(1),
    )
    examples: list[dict[str, object]] = []
    for source_key in ("trunc_tet_raw", "trunc_tet_radial"):
        points = sources[source_key]
        for spreads in product(values, repeat=3):
            found_for_spread = False
            for convention in all_conventions:
                result = audit_source(points, spreads, convention)
                if result["hull_count"] == 5 and result["clean_under_179"]:
                    examples.append(
                        {
                            "source": source_key,
                            "spreads": [str(s) for s in spreads],
                            "order": convention.order,
                            "signs_xyz": convention.signs,
                            "drop_axis": convention.drop_axis,
                            "max_interior_angle": result["max_interior_angle"],
                        }
                    )
                    found_for_spread = True
                    break
            if len(examples) >= limit:
                return examples
            if found_for_spread:
                continue
    return examples


def write_markdown(results: dict[str, object]) -> None:
    lines: list[str] = [
        "# Prime Projection Conjecture Audit",
        "",
        "This report is generated by `empirical/prime_projection_conjecture_audit.py`.",
        "It is an independent reconstruction from the v5.1 PDF, not the original ARTexplorer search code.",
        "",
        "The audit scans all 6 axis orders, all 8 sine-sign choices, and all 3 coordinate projection axes.",
        "Hull signs use exact `Fraction(float)` arithmetic, matching the PDF's Path-C model.",
        "",
        "## Summary",
        "",
        "| claim | target | sources | target matches | clean target matches | nearest count | nearest convention |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    claims_result = results["claims"]
    assert isinstance(claims_result, dict)
    for name, item in claims_result.items():
        assert isinstance(item, dict)
        nearest = item["nearest"]
        assert isinstance(nearest, dict)
        source_counts = item["source_vertex_counts"]
        assert isinstance(source_counts, dict)
        convention = f"{nearest['source']} {nearest['order']} signs={tuple(nearest['signs_xyz'])} drop={nearest['drop_axis']}"
        lines.append(
            f"| `{name}` | {item['target']} | {len(source_counts)} | "
            f"{item['target_match_count']} | {item['clean_target_match_count']} | "
            f"{nearest['hull_count']} | `{convention}` |"
        )

    lines.extend(["", "## Clean Matches", ""])
    for name, item in claims_result.items():
        assert isinstance(item, dict)
        lines.append(f"### {name}")
        matches = item["sample_clean_target_matches"]
        assert isinstance(matches, list)
        if not matches:
            lines.append("")
            lines.append("No clean target match found in the scanned convention family.")
            lines.append("")
            continue
        for match in matches[:5]:
            lines.append(
                f"- `{match['source']}` order `{match['order']}`, signs `{tuple(match['signs_xyz'])}`, "
                f"drop `{match['drop_axis']}`, max angle `{float(match['max_interior_angle']):.3f}`"
            )
        lines.append("")

    followups = results.get("followups", {})
    assert isinstance(followups, dict)
    pentagon_examples = followups.get("truncated_tet_low_tier_pentagon_examples", [])
    assert isinstance(pentagon_examples, list)
    lines.extend(
        [
            "## Follow-Up: Truncated Tet 5-Hulls",
            "",
            "The stated `(0,1/2,0)` pentagon preset did not reproduce here, but the reconstructed truncated tetrahedron does produce clean pentagonal hulls at nearby low-tier rational spreads.",
            "",
        ]
    )
    for row in pentagon_examples[:8]:
        lines.append(
            f"- `{row['source']}` spreads `{tuple(row['spreads'])}`, order `{row['order']}`, "
            f"signs `{tuple(row['signs_xyz'])}`, drop `{row['drop_axis']}`, "
            f"max angle `{float(row['max_interior_angle']):.3f}`"
        )
    lines.append("")

    lines.extend(
        [
            "## Interpretation",
            "",
            "A clean match means the local reconstruction can reproduce the claimed prime hull count under at least one scanned convention and with maximum interior angle below 179 degrees.",
            "Failure to find a clean match is not a disproof of the PDF: it means the PDF's hidden implementation details, source geometry normalization, or projection convention are not captured by this reconstruction.",
            "",
        ]
    )
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    sources = make_sources()
    all_conventions = conventions()
    claim_results = {
        claim.name: summarize_claim(claim, sources, all_conventions)
        for claim in claims()
    }
    followups = {
        "truncated_tet_low_tier_pentagon_examples": low_tier_pentagon_examples(
            sources,
            all_conventions,
        )
    }
    results: dict[str, object] = {
        "metadata": {
            "source": "empirical/prime_projection_conjecture_audit.py",
            "model": "independent reconstruction from PDF v5.1",
            "conventions_scanned": len(all_conventions),
        },
        "sources": {key: len(value) for key, value in sources.items()},
        "claims": claim_results,
        "followups": followups,
    }
    JSON_OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    write_markdown(results)
    print(f"Wrote {JSON_OUT}")
    print(f"Wrote {MD_OUT}")
    for name, item in claim_results.items():
        print(
            name,
            "target_matches=",
            item["target_match_count"],
            "clean=",
            item["clean_target_match_count"],
            "nearest_count=",
            item["nearest"]["hull_count"],
        )


if __name__ == "__main__":
    main()
