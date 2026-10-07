"""Cyclic Amari-Chentsov cubic probe for finite label tasks.

This is the generic version of the weekday control.  It supports a cyclic
label algebra C_n, with built-in presets for weekdays (C7) and months (C12),
and computes the intrinsic behavior-side Fisher/Hellinger/K^CH diagnostics.

The script does not run a model.  It either consumes an empirical n-by-n
centroid matrix or uses a symmetric cyclic proxy so the algebraic row can be
audited before the upstream model artifacts arrive.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PRESETS: dict[str, tuple[str, ...]] = {
    "weekdays": (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ),
    "months": (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
}


Vector = list[float]
Matrix = list[list[float]]


@dataclass(frozen=True)
class PairResult:
    start: str
    end: str
    cyclic_separation: int
    h_moment: Vector
    h_natural_delta: Vector
    h_hellinger_tangent_at_uniform: Vector
    fisher_norm_h: float
    cubic_T_hhh: float
    cubic_T_unit: float
    K_h_h: Vector
    fisher_norm_K_h_h: float
    endpoint_deviation_norm: float
    midpoint_deviation_norm: float
    exact_max_m_vs_lc_hellinger: float
    exact_max_e_vs_lc_hellinger: float
    exact_mean_m_vs_lc_hellinger: float
    exact_mean_e_vs_lc_hellinger: float
    exact_m_path_length_hellinger: float
    exact_e_path_length_hellinger: float
    exact_lc_path_length_hellinger: float


def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))


def add(a: Vector, b: Vector) -> Vector:
    return [x + y for x, y in zip(a, b)]


def sub(a: Vector, b: Vector) -> Vector:
    return [x - y for x, y in zip(a, b)]


def scale(c: float, a: Vector) -> Vector:
    return [c * x for x in a]


def mean(a: Vector) -> float:
    return sum(a) / len(a)


def centered(a: Vector) -> Vector:
    m = mean(a)
    return [x - m for x in a]


def norm(a: Vector) -> float:
    return math.sqrt(dot(a, a))


def softmax(logits: Vector) -> Vector:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    total = sum(exps)
    return [x / total for x in exps]


def symmetric_centroid(n: int, index: int, peak: float, neighbor: float) -> Vector:
    floor = (1.0 - peak - 2.0 * neighbor) / (n - 3)
    if floor <= 0.0:
        raise ValueError("peak + 2 * neighbor must be less than 1")
    p = [floor] * n
    p[index] = peak
    p[(index - 1) % n] = neighbor
    p[(index + 1) % n] = neighbor
    return p


def fisher_inner(p: Vector, u: Vector, v: Vector) -> float:
    return sum(ui * vi / pi for pi, ui, vi in zip(p, u, v))


def fisher_norm(p: Vector, u: Vector) -> float:
    return math.sqrt(max(0.0, fisher_inner(p, u, u)))


def ch_cubic(p: Vector, u: Vector, v: Vector, w: Vector) -> float:
    return sum(ui * vi * wi / (pi * pi) for pi, ui, vi, wi in zip(p, u, v, w))


def ch_raise(p: Vector, u: Vector, v: Vector) -> Vector:
    guv = fisher_inner(p, u, v)
    return [(ui * vi / pi) - guv * pi for pi, ui, vi in zip(p, u, v)]


def sqrt_embed(p: Vector) -> Vector:
    return [math.sqrt(x) for x in p]


def hellinger(p: Vector, q: Vector) -> float:
    return norm(sub(sqrt_embed(p), sqrt_embed(q))) / math.sqrt(2.0)


def normalize_probability(p: Vector) -> Vector:
    total = sum(p)
    return [max(0.0, x / total) for x in p]


def m_path(pa: Vector, pb: Vector, t: float) -> Vector:
    return add(scale(1.0 - t, pa), scale(t, pb))


def e_path(pa: Vector, pb: Vector, t: float) -> Vector:
    logits = add(scale(1.0 - t, [math.log(x) for x in pa]), scale(t, [math.log(x) for x in pb]))
    return softmax(logits)


def lc_path(pa: Vector, pb: Vector, t: float) -> Vector:
    xa = sqrt_embed(pa)
    xb = sqrt_embed(pb)
    cos_omega = max(-1.0, min(1.0, dot(xa, xb)))
    omega = math.acos(cos_omega)
    if omega < 1e-12:
        return pa[:]
    sin_omega = math.sin(omega)
    left = math.sin((1.0 - t) * omega) / sin_omega
    right = math.sin(t * omega) / sin_omega
    x = add(scale(left, xa), scale(right, xb))
    return normalize_probability([xi * xi for xi in x])


def path_length(path_fn, pa: Vector, pb: Vector, samples: int) -> float:
    points = [path_fn(pa, pb, k / samples) for k in range(samples + 1)]
    return sum(hellinger(points[i], points[i + 1]) for i in range(samples))


def path_deviation(path_fn, pa: Vector, pb: Vector, samples: int) -> tuple[float, float]:
    distances = []
    for k in range(samples + 1):
        t = k / samples
        distances.append(hellinger(path_fn(pa, pb, t), lc_path(pa, pb, t)))
    return max(distances), sum(distances) / len(distances)


def pearson(xs: Vector, ys: Vector) -> float:
    mx = mean(xs)
    my = mean(ys)
    x0 = [x - mx for x in xs]
    y0 = [y - my for y in ys]
    denom = norm(x0) * norm(y0)
    if denom == 0.0:
        return float("nan")
    return dot(x0, y0) / denom


def cyclic_arc_distance(centroids: list[Vector], i: int, j: int) -> float:
    n = len(centroids)
    if i == j:
        return 0.0
    forward = 0.0
    k = i
    while k != j:
        nxt = (k + 1) % n
        forward += hellinger(centroids[k], centroids[nxt])
        k = nxt
    backward = 0.0
    k = i
    while k != j:
        nxt = (k - 1) % n
        backward += hellinger(centroids[k], centroids[nxt])
        k = nxt
    return min(forward, backward)


def pair_result(labels: tuple[str, ...], centroids: list[Vector], i: int, j: int, samples: int) -> PairResult:
    n = len(labels)
    p_star = [1.0 / n] * n
    pa = centroids[i]
    pb = centroids[j]
    h = sub(pb, pa)
    h_eta = sub(centered([math.log(x) for x in pb]), centered([math.log(x) for x in pa]))
    h_x_uniform = [math.sqrt(n) * x / 2.0 for x in h]
    h_norm = fisher_norm(p_star, h)
    T_hhh = ch_cubic(p_star, h, h, h)
    h_unit = scale(1.0 / h_norm, h) if h_norm > 0.0 else h
    T_unit = ch_cubic(p_star, h_unit, h_unit, h_unit)
    K_h_h = ch_raise(p_star, h, h)
    K_norm = fisher_norm(p_star, K_h_h)
    m_max, m_mean = path_deviation(m_path, pa, pb, samples)
    e_max, e_mean = path_deviation(e_path, pa, pb, samples)
    return PairResult(
        start=labels[i],
        end=labels[j],
        cyclic_separation=min((j - i) % n, (i - j) % n),
        h_moment=h,
        h_natural_delta=h_eta,
        h_hellinger_tangent_at_uniform=h_x_uniform,
        fisher_norm_h=h_norm,
        cubic_T_hhh=T_hhh,
        cubic_T_unit=T_unit,
        K_h_h=K_h_h,
        fisher_norm_K_h_h=K_norm,
        endpoint_deviation_norm=0.25 * K_norm,
        midpoint_deviation_norm=(1.0 / 16.0) * K_norm,
        exact_max_m_vs_lc_hellinger=m_max,
        exact_max_e_vs_lc_hellinger=e_max,
        exact_mean_m_vs_lc_hellinger=m_mean,
        exact_mean_e_vs_lc_hellinger=e_mean,
        exact_m_path_length_hellinger=path_length(m_path, pa, pb, samples),
        exact_e_path_length_hellinger=path_length(e_path, pa, pb, samples),
        exact_lc_path_length_hellinger=path_length(lc_path, pa, pb, samples),
    )


def character_coefficients(h: Vector) -> list[complex]:
    n = len(h)
    coeffs = []
    root = cmath.exp(-2j * math.pi / n)
    scale_factor = math.sqrt(n)
    for k in range(n):
        coeffs.append(sum(h[x] * (root ** (k * x)) for x in range(n)) / scale_factor)
    return coeffs


def character_operator(h: Vector) -> list[list[complex]]:
    n = len(h)
    h_hat = character_coefficients(h)
    return [
        [math.sqrt(n) * h_hat[(k - ell) % n] for ell in range(1, n)]
        for k in range(1, n)
    ]


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_power_part(value: int, prime: int) -> int:
    part = 1
    while value % prime == 0:
        part *= prime
        value //= prime
    return part


def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    remaining = n
    while d * d <= remaining:
        if remaining % d == 0:
            factors.append(d)
            while remaining % d == 0:
                remaining //= d
        d += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


def conductor_packets(n: int) -> list[dict[str, Any]]:
    packets = []
    for d in divisors(n):
        chars = [k for k in range(1, n) if n // math.gcd(n, k) == d]
        if chars:
            packets.append(
                {
                    "conductor": d,
                    "dimension": len(chars),
                    "character_indices": chars,
                }
            )
    return packets


def crt_packet_table(n: int) -> list[dict[str, Any]]:
    primes = prime_factors(n)
    rows = []
    for packet in conductor_packets(n):
        conductor = int(packet["conductor"])
        row: dict[str, Any] = {
            "conductor": conductor,
            "dimension": packet["dimension"],
            "character_indices": packet["character_indices"],
        }
        for prime in primes:
            row[f"p{prime}_part"] = prime_power_part(conductor, prime)
        rows.append(row)
    return rows


def validate_centroids(rows: Any, labels: tuple[str, ...]) -> list[Vector]:
    n = len(labels)
    if not isinstance(rows, list) or len(rows) != n:
        raise ValueError(f"centroids must contain {n} rows")
    out = []
    for row_index, row in enumerate(rows):
        if not isinstance(row, list) or len(row) != n:
            raise ValueError(f"centroid row {row_index} must contain {n} probabilities")
        values = [float(x) for x in row]
        if any(x <= 0.0 or not math.isfinite(x) for x in values):
            raise ValueError(f"centroid row {row_index} must be strictly positive")
        total = sum(values)
        if not math.isclose(total, 1.0, rel_tol=1e-8, abs_tol=1e-8):
            raise ValueError(f"centroid row {row_index} must sum to 1; got {total}")
        out.append(values)
    return out


def load_labels(path: Path | None, preset: str) -> tuple[str, ...]:
    if path is None:
        return PRESETS[preset]
    payload = json.loads(path.read_text(encoding="utf-8"))
    labels = payload.get("labels") if isinstance(payload, dict) else payload
    if not isinstance(labels, list) or len(labels) < 4:
        raise ValueError("labels JSON must be a list of at least four label strings")
    return tuple(str(label) for label in labels)


def load_centroids_json(path: Path, labels: tuple[str, ...]) -> list[Vector]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("centroids") if isinstance(payload, dict) else payload
    return validate_centroids(rows, labels)


def format_vector(v: Vector, digits: int = 6) -> str:
    return "[" + ", ".join(f"{x:.{digits}f}" for x in v) + "]"


def format_matrix(matrix: Matrix, digits: int = 6) -> str:
    return "\n".join("[" + ", ".join(f"{x:.{digits}f}" for x in row) + "]" for row in matrix)


def format_complex(z: complex, digits: int = 6) -> str:
    real = 0.0 if abs(z.real) < 10 ** (-(digits + 1)) else z.real
    imag = 0.0 if abs(z.imag) < 10 ** (-(digits + 1)) else z.imag
    sign = "+" if imag >= 0.0 else "-"
    return f"{real:.{digits}f}{sign}{abs(imag):.{digits}f}i"


def format_complex_matrix(matrix: list[list[complex]], digits: int = 4) -> str:
    return "\n".join(
        "[" + ", ".join(format_complex(x, digits) for x in row) + "]"
        for row in matrix
    )


def complex_json(z: complex) -> dict[str, float]:
    return {"real": round(z.real, 10), "imag": round(z.imag, 10)}


def rounded_json(obj: Any) -> Any:
    if isinstance(obj, float):
        return round(obj, 10)
    if isinstance(obj, list):
        return [rounded_json(x) for x in obj]
    if isinstance(obj, dict):
        return {k: rounded_json(v) for k, v in obj.items()}
    return obj


def compute(labels: tuple[str, ...], peak: float, neighbor: float, samples: int, centroids: list[Vector] | None):
    n = len(labels)
    if centroids is None:
        centroids = [symmetric_centroid(n, i, peak, neighbor) for i in range(n)]
    probes = sorted({1, 2, n // 2 if n % 2 == 0 else min(3, n - 1)})
    pair_results = [pair_result(labels, centroids, 0, offset % n, samples) for offset in probes]

    cyclic_arcs = []
    hellinger_chords = []
    moment_chords = []
    natural_chords = []
    lc_distances = []
    for i in range(n):
        for j in range(i + 1, n):
            cyclic_arcs.append(cyclic_arc_distance(centroids, i, j))
            hellinger_chords.append(hellinger(centroids[i], centroids[j]))
            moment_chords.append(norm(sub(centroids[i], centroids[j])))
            natural_chords.append(norm(sub(centered([math.log(x) for x in centroids[i]]), centered([math.log(x) for x in centroids[j]]))))
            lc_distances.append(path_length(lc_path, centroids[i], centroids[j], samples))

    correlations = {
        "hellinger_chord_vs_cyclic_arc": pearson(hellinger_chords, cyclic_arcs),
        "moment_chord_vs_cyclic_arc": pearson(moment_chords, cyclic_arcs),
        "natural_chord_vs_cyclic_arc": pearson(natural_chords, cyclic_arcs),
        "lc_distance_vs_cyclic_arc": pearson(lc_distances, cyclic_arcs),
    }
    return centroids, pair_results, correlations


def make_report(
    labels: tuple[str, ...],
    centroids: list[Vector],
    pair_results: list[PairResult],
    correlations: dict[str, float],
    peak: float,
    neighbor: float,
    samples: int,
    source: str,
    centroids_path: Path | None,
) -> str:
    n = len(labels)
    p_star = [1.0 / n] * n
    floor = (1.0 - peak - 2.0 * neighbor) / (n - 3)
    reference_direction = sub(centroids[0], p_star)
    packets = conductor_packets(n)
    crt_rows = crt_packet_table(n)
    operator = character_operator(reference_direction)

    title = f"{labels[0]}-Cycle C{n} K^CH Probe"
    if labels == PRESETS["weekdays"]:
        title = "Weekdays C7 K^CH Probe"
    elif labels == PRESETS["months"]:
        title = "Months C12 K^CH Probe"

    setup = [
        f"- label count: `{n}`",
        f"- centroid source: `{source}`" + (f" from `{centroids_path}`" if centroids_path else ""),
    ]
    if source == "parametric":
        setup.extend(
            [
                f"- peak mass on target label: `{peak:.6f}`",
                f"- mass on adjacent labels: `{neighbor:.6f}` each",
                f"- uniform floor on other labels: `{floor:.6f}`",
            ]
        )

    lines = [
        f"# {title}",
        "",
        "## Status",
        "",
        *setup,
        "",
        "This report is intrinsic to the output simplex.  It measures the behavior-side Fisher cubic available before any activation pullback, Hessian, or steering-path residual is estimated.",
        "",
        "## Label Order",
        "",
        ", ".join(f"`{label}`" for label in labels),
        "",
        "## Character Conductors",
        "",
        "| conductor | dimension | character indices |",
        "|---:|---:|---|",
    ]
    for packet in packets:
        chars = ", ".join(str(k) for k in packet["character_indices"])
        lines.append(f"| {packet['conductor']} | {packet['dimension']} | `{chars}` |")

    if len(prime_factors(n)) > 1:
        primes = prime_factors(n)
        header = "| conductor | dimension | " + " | ".join(f"p={prime} part" for prime in primes) + " |"
        divider = "|---:|---:|" + "---:|" * len(primes)
        lines += ["", "## CRT Packet Table", "", header, divider]
        for row in crt_rows:
            parts = " | ".join(str(row[f"p{prime}_part"]) for prime in primes)
            lines.append(f"| {row['conductor']} | {row['dimension']} | {parts} |")
        if n == 12:
            lines += [
                "",
                "For C12, the CRT view is C4 x C3.  The p=2 part takes values 1, 2, and 4 across the nontrivial tangent packets, so the month row is an intermediate mixed-conductor control: less local than F4[u]/(u^2), but already richer than prime C7.",
            ]

    lines += [
        "",
        "## Centroids",
        "",
        "Rows and columns use the label order above.",
        "",
        "```text",
        format_matrix(centroids, 6),
        "```",
        "",
        "## K^CH at the Uniform Centroid",
        "",
        "At p_* = (1/n) 1,",
        "",
        "```text",
        "T_{p_*}(u,v,w) = n^2 sum_i u_i v_i w_i",
        "K^CH_{p_*}(u)v = n u*v - n <u,v>_Euc p_*",
        "```",
        "",
        "In the nontrivial character basis, the first-label displacement acts by cyclic convolution.  The matrix below omits the constant character row and column.",
        "",
        "```text",
        format_complex_matrix(operator, 4),
        "```",
        "",
        "## Pair Probes",
        "",
    ]

    for result in pair_results:
        lines += [
            f"### {result.start} -> {result.end}",
            "",
            f"- cyclic separation: `{result.cyclic_separation}`",
            f"- theta displacement: `{format_vector(result.h_moment)}`",
            f"- eta endpoint difference: `{format_vector(result.h_natural_delta)}`",
            f"- Fisher norm ||h||_F: `{result.fisher_norm_h:.6f}`",
            f"- cubic scalar T(h,h,h): `{result.cubic_T_hhh:.6f}`",
            f"- unit-direction cubic T(hat h,hat h,hat h): `{result.cubic_T_unit:.6f}`",
            f"- ||K^CH(h)h||_F: `{result.fisher_norm_K_h_h:.6f}`",
            f"- second-order endpoint deviation norm coefficient: `{result.endpoint_deviation_norm:.6f}`",
            f"- exact max m-flat vs Fisher LC path, Hellinger units: `{result.exact_max_m_vs_lc_hellinger:.6f}`",
            f"- exact max e-flat vs Fisher LC path, Hellinger units: `{result.exact_max_e_vs_lc_hellinger:.6f}`",
            f"- path lengths (m, e, LC), Hellinger units: `({result.exact_m_path_length_hellinger:.6f}, {result.exact_e_path_length_hellinger:.6f}, {result.exact_lc_path_length_hellinger:.6f})`",
            "",
        ]

    lines += [
        "## Intrinsic Linear-vs-Manifold Prediction",
        "",
        f"- Hellinger chord vs cyclic Hellinger arc: `r = {correlations['hellinger_chord_vs_cyclic_arc']:.6f}`",
        f"- moment Euclidean chord vs cyclic Hellinger arc: `r = {correlations['moment_chord_vs_cyclic_arc']:.6f}`",
        f"- natural/logit chord vs cyclic Hellinger arc: `r = {correlations['natural_chord_vs_cyclic_arc']:.6f}`",
        f"- Fisher LC endpoint distance vs cyclic Hellinger arc: `r = {correlations['lc_distance_vs_cyclic_arc']:.6f}`",
        "",
        "## Interpretation",
        "",
    ]
    if n == 7:
        lines.append("C7 is the prime control: one nontrivial conductor packet and no tame/wild extension class.")
    elif n == 12:
        lines.append("C12 should be run before claiming a local finite-field row in the neural setting.  It is already present in Wurgaft-style month geometry, has CRT structure C4 x C3, and tests whether the activation/behavior pipeline sees a mixed conductor split before the genuinely local Ext_CH rows are invoked.")
    else:
        lines.append("This row is a cyclic behavior-side control.  Its conductor packets show which finite channels exist before activation pullback residuals are assigned.")
    lines += [
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/compute_cyclic_K_CH.py --preset {'months' if labels == PRESETS['months'] else 'weekdays' if labels == PRESETS['weekdays'] else 'weekdays'}",
        "python empirical/compute_cyclic_K_CH.py --labels-json path/to/labels.json --centroids-json path/to/centroids.json",
        "```",
        "",
        f"Path comparisons used `{samples}` intervals.",
        "",
    ]
    return "\n".join(lines)


def default_report_path(preset: str, centroids_json: Path | None) -> Path:
    suffix = "empirical" if centroids_json else "prediction"
    return Path(f"empirical/reports/{preset}_cyclic_K_CH_{suffix}.md")


def default_json_path(preset: str, centroids_json: Path | None) -> Path:
    suffix = "empirical" if centroids_json else "prediction"
    return Path(f"empirical/reports/{preset}_cyclic_K_CH_{suffix}.json")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=sorted(PRESETS), default="months")
    parser.add_argument("--labels-json", type=Path, default=None)
    parser.add_argument("--centroids-json", type=Path, default=None)
    parser.add_argument("--peak", type=float, default=0.76)
    parser.add_argument("--neighbor", type=float, default=0.09)
    parser.add_argument("--samples", type=int, default=400)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    labels = load_labels(args.labels_json, args.preset)
    empirical_centroids = load_centroids_json(args.centroids_json, labels) if args.centroids_json else None
    source = "empirical" if empirical_centroids is not None else "parametric"
    centroids, pair_results, correlations = compute(labels, args.peak, args.neighbor, args.samples, empirical_centroids)

    report_path = args.report or default_report_path(args.preset, args.centroids_json)
    json_path = args.json or default_json_path(args.preset, args.centroids_json)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(
        make_report(
            labels,
            centroids,
            pair_results,
            correlations,
            args.peak,
            args.neighbor,
            args.samples,
            source,
            args.centroids_json,
        ),
        encoding="utf-8",
    )

    raw = {
        "labels": list(labels),
        "n": len(labels),
        "peak": args.peak,
        "neighbor": args.neighbor,
        "floor": (1.0 - args.peak - 2.0 * args.neighbor) / (len(labels) - 3),
        "centroid_source": source,
        "empirical_centroids_path": str(args.centroids_json) if args.centroids_json else None,
        "centroids": centroids,
        "conductor_packets": conductor_packets(len(labels)),
        "crt_packet_table": crt_packet_table(len(labels)),
        "pair_results": [result.__dict__ for result in pair_results],
        "correlations": correlations,
        "character_basis": {
            "reference_direction_hat": [complex_json(z) for z in character_coefficients(sub(centroids[0], [1.0 / len(labels)] * len(labels)))],
            "reference_operator_nontrivial": [
                [complex_json(z) for z in row]
                for row in character_operator(sub(centroids[0], [1.0 / len(labels)] * len(labels)))
            ],
        },
    }
    json_path.write_text(json.dumps(rounded_json(raw), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded_json(correlations), indent=2))


if __name__ == "__main__":
    main()
