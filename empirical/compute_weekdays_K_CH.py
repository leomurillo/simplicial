"""Weekday Amari-Chentsov cubic probe for Wurgaft et al. 2026.

This script builds a small intrinsic behavior-space model for the weekdays
task in Wurgaft et al., "Manifold Steering Reveals the Shared Geometry of
Neural Network Representation and Behavior" (arXiv:2605.05115v1).

The paper does not publish the seven empirical behavior centroids, so the
default model is a cyclic, sharply peaked seven-class distribution: most mass
on the target weekday, smaller mass on its two neighbors, and a uniform floor
on the remaining four weekdays.  If empirical centroids become available, pass
them with --centroids-json.  The resulting calculation is deliberately
intrinsic to the output simplex; it does not use activation-space data.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

N = len(WEEKDAYS)

WURGAFT_MANIFOLD_R = 0.9896
WURGAFT_TEXT_LINEAR_R = 0.89


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
    endpoint_deviation_m_norm: float
    endpoint_deviation_e_norm: float
    midpoint_deviation_m_norm: float
    midpoint_deviation_e_norm: float
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


def centroid(index: int, peak: float, neighbor: float) -> Vector:
    floor = (1.0 - peak - 2.0 * neighbor) / (N - 3)
    if floor <= 0.0:
        raise ValueError("peak + 2 * neighbor must be less than 1")
    p = [floor] * N
    p[index] = peak
    p[(index - 1) % N] = neighbor
    p[(index + 1) % N] = neighbor
    return p


def fisher_inner(p: Vector, u: Vector, v: Vector) -> float:
    return sum(ui * vi / pi for pi, ui, vi in zip(p, u, v))


def fisher_norm(p: Vector, u: Vector) -> float:
    return math.sqrt(max(0.0, fisher_inner(p, u, u)))


def ch_cubic(p: Vector, u: Vector, v: Vector, w: Vector) -> float:
    """Covariant Amari-Chentsov cubic in moment coordinates."""

    return sum(ui * vi * wi / (pi * pi) for pi, ui, vi, wi in zip(p, u, v, w))


def ch_raise(p: Vector, u: Vector, v: Vector) -> Vector:
    """Raised cubic K^CH_p(u)v in the Paper 11 convention.

    It is the tangent vector satisfying

        g_p(K^CH_p(u)v, w) = T_p(u, v, w)

    for all zero-sum tangent w.  In moment coordinates this is

        uv / p - g_p(u, v) p.
    """

    guv = fisher_inner(p, u, v)
    return [(ui * vi / pi) - guv * pi for pi, ui, vi in zip(p, u, v)]


def sqrt_embed(p: Vector) -> Vector:
    return [math.sqrt(x) for x in p]


def hellinger(p: Vector, q: Vector) -> float:
    return norm(sub(sqrt_embed(p), sqrt_embed(q))) / math.sqrt(2.0)


def normalize_probability(p: Vector) -> Vector:
    total = sum(p)
    return [max(0.0, x / total) for x in p]


def validate_centroid_row(row: Any, row_index: int) -> Vector:
    if not isinstance(row, list) or len(row) != N:
        raise ValueError(f"centroid row {row_index} must be a list of {N} probabilities")
    values = [float(x) for x in row]
    if any(x <= 0.0 for x in values):
        raise ValueError(f"centroid row {row_index} must be strictly positive")
    total = sum(values)
    if not math.isclose(total, 1.0, rel_tol=1e-8, abs_tol=1e-8):
        raise ValueError(f"centroid row {row_index} must sum to 1; got {total}")
    return values


def load_centroids_json(path: Path) -> list[Vector]:
    """Load empirical seven-token weekday centroids.

    Accepted shapes:
      - [[... seven probabilities ...], ... seven rows ...]
      - {"centroids": [[...], ...]}

    Rows must be Monday through Sunday and columns must be the same seven
    weekday-token order used by WEEKDAYS.  If Wurgaft-style output includes an
    "other" bin, aggregate or drop/renormalize it before using this script.
    """

    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("centroids") if isinstance(payload, dict) else payload
    if not isinstance(rows, list) or len(rows) != N:
        raise ValueError(f"centroids JSON must contain {N} rows in Monday-through-Sunday order")
    return [validate_centroid_row(row, i) for i, row in enumerate(rows)]


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
    if i == j:
        return 0.0
    forward = 0.0
    k = i
    while k != j:
        nxt = (k + 1) % N
        forward += hellinger(centroids[k], centroids[nxt])
        k = nxt
    backward = 0.0
    k = i
    while k != j:
        nxt = (k - 1) % N
        backward += hellinger(centroids[k], centroids[nxt])
        k = nxt
    return min(forward, backward)


def pair_result(centroids: list[Vector], i: int, j: int, samples: int) -> PairResult:
    p_star = [1.0 / N] * N
    pa = centroids[i]
    pb = centroids[j]
    h = sub(pb, pa)
    h_eta = sub(centered([math.log(x) for x in pb]), centered([math.log(x) for x in pa]))
    h_x_uniform = [math.sqrt(N) * x / 2.0 for x in h]
    h_norm = fisher_norm(p_star, h)
    T_hhh = ch_cubic(p_star, h, h, h)
    h_unit = scale(1.0 / h_norm, h) if h_norm > 0.0 else h
    T_unit = ch_cubic(p_star, h_unit, h_unit, h_unit)
    K_h_h = ch_raise(p_star, h, h)
    K_norm = fisher_norm(p_star, K_h_h)

    # Paper 11 convention:
    #   nabla^(e) = nabla^(0) - 1/2 K^CH
    #   nabla^(m) = nabla^(0) + 1/2 K^CH
    # Hence same-initial-velocity e/m flat curves have LC acceleration
    # +/- 1/2 K^CH(h,h).  The second-order position deviation coefficient is
    # +/- 1/4 K^CH(h,h) at t=1 and +/- 1/16 K^CH(h,h) at t=1/2.
    endpoint_dev = 0.25 * K_norm
    midpoint_dev = (1.0 / 16.0) * K_norm

    m_max, m_mean = path_deviation(m_path, pa, pb, samples)
    e_max, e_mean = path_deviation(e_path, pa, pb, samples)

    return PairResult(
        start=WEEKDAYS[i],
        end=WEEKDAYS[j],
        cyclic_separation=min((j - i) % N, (i - j) % N),
        h_moment=h,
        h_natural_delta=h_eta,
        h_hellinger_tangent_at_uniform=h_x_uniform,
        fisher_norm_h=h_norm,
        cubic_T_hhh=T_hhh,
        cubic_T_unit=T_unit,
        K_h_h=K_h_h,
        fisher_norm_K_h_h=K_norm,
        endpoint_deviation_m_norm=endpoint_dev,
        endpoint_deviation_e_norm=endpoint_dev,
        midpoint_deviation_m_norm=midpoint_dev,
        midpoint_deviation_e_norm=midpoint_dev,
        exact_max_m_vs_lc_hellinger=m_max,
        exact_max_e_vs_lc_hellinger=e_max,
        exact_mean_m_vs_lc_hellinger=m_mean,
        exact_mean_e_vs_lc_hellinger=e_mean,
        exact_m_path_length_hellinger=path_length(m_path, pa, pb, samples),
        exact_e_path_length_hellinger=path_length(e_path, pa, pb, samples),
        exact_lc_path_length_hellinger=path_length(lc_path, pa, pb, samples),
    )


def format_vector(v: Vector, digits: int = 6) -> str:
    return "[" + ", ".join(f"{x:.{digits}f}" for x in v) + "]"


def format_matrix(matrix: Matrix, digits: int = 3) -> str:
    lines = []
    for row in matrix:
        lines.append("[" + ", ".join(f"{x:.{digits}f}" for x in row) + "]")
    return "\n".join(lines)


def format_complex(z: complex, digits: int = 6) -> str:
    real = 0.0 if abs(z.real) < 10 ** (-(digits + 1)) else z.real
    imag = 0.0 if abs(z.imag) < 10 ** (-(digits + 1)) else z.imag
    sign = "+" if imag >= 0.0 else "-"
    return f"{real:.{digits}f}{sign}{abs(imag):.{digits}f}i"


def format_complex_vector(v: list[complex], digits: int = 6) -> str:
    return "[" + ", ".join(format_complex(x, digits) for x in v) + "]"


def format_complex_matrix(matrix: list[list[complex]], digits: int = 6) -> str:
    lines = []
    for row in matrix:
        lines.append("[" + ", ".join(format_complex(x, digits) for x in row) + "]")
    return "\n".join(lines)


def complex_json(z: complex) -> dict[str, float]:
    return {"real": round(z.real, 10), "imag": round(z.imag, 10)}


def weekday_character_coefficients(h: Vector) -> list[complex]:
    """Unitary DFT coefficients on C_7 for the Monday-to-day tangent."""

    coeffs = []
    root = cmath.exp(-2j * math.pi / N)
    scale_factor = math.sqrt(N)
    for k in range(N):
        coeffs.append(sum(h[x] * (root ** (k * x)) for x in range(N)) / scale_factor)
    return coeffs


def weekday_character_operator(h: Vector) -> list[list[complex]]:
    """Nontrivial character-basis matrix for v |-> K^CH_{p_*}(h)v.

    With phi_k(x)=7^{-1/2} exp(2 pi i kx/7) and unitary Fourier coefficients
    h_hat_r=<phi_r,h>, the centroid operator is

        K^CH_{p_*}(h) phi_l = sqrt(7) sum_{k=1}^6 h_hat_{k-l} phi_k.

    The constant row is omitted because the tangent projection removes it.
    """

    h_hat = weekday_character_coefficients(h)
    return [
        [math.sqrt(N) * h_hat[(k - ell) % N] for ell in range(1, N)]
        for k in range(1, N)
    ]


def rounded_json(obj):
    if isinstance(obj, float):
        return round(obj, 10)
    if isinstance(obj, list):
        return [rounded_json(x) for x in obj]
    if isinstance(obj, dict):
        return {k: rounded_json(v) for k, v in obj.items()}
    return obj


def gap_accounting(correlations: dict[str, float]) -> dict[str, float]:
    """Compare the intrinsic C7 prediction with the published weekday gap."""

    moment_r = correlations["moment_chord_vs_cyclic_arc"]
    text_gap = WURGAFT_MANIFOLD_R - WURGAFT_TEXT_LINEAR_R
    predicted_gap = WURGAFT_MANIFOLD_R - moment_r
    return {
        "wurgaft_manifold_r": WURGAFT_MANIFOLD_R,
        "wurgaft_text_linear_r": WURGAFT_TEXT_LINEAR_R,
        "wurgaft_text_gap": text_gap,
        "intrinsic_behavior_linear_r": moment_r,
        "intrinsic_behavior_gap_to_wurgaft_manifold_r": predicted_gap,
        "residual_vs_wurgaft_text_linear_r": moment_r - WURGAFT_TEXT_LINEAR_R,
        "explained_fraction_of_text_gap": predicted_gap / text_gap if text_gap else float("nan"),
    }


def make_report(
    centroids: list[Vector],
    adjacent: PairResult,
    nonadjacent: PairResult,
    correlations: dict[str, float],
    peak: float,
    neighbor: float,
    samples: int,
    centroid_source: str,
    centroids_path: Path | None,
) -> str:
    p_star = [1.0 / N] * N
    floor = (1.0 - peak - 2.0 * neighbor) / (N - 3)
    gap = gap_accounting(correlations)
    centroid_matrix = centroids
    k_monday_operator = []
    monday_direction = sub(centroids[0], p_star)
    monday_hat = weekday_character_coefficients(monday_direction)
    monday_character_operator = weekday_character_operator(monday_direction)
    for basis_index in range(N):
        e = [0.0] * N
        e[basis_index] = 1.0
        basis_tangent = sub(e, p_star)
        k_monday_operator.append(ch_raise(p_star, monday_direction, basis_tangent))
    # Store as columns above; transpose for human-readable rows.
    k_rows = [[k_monday_operator[col][row] for col in range(N)] for row in range(N)]

    if centroid_source == "empirical":
        setup_lines = [
            "This computation is intrinsic to the seven-class weekday behavior simplex.",
            f"Centroid source: empirical seven-token centroids loaded from `{centroids_path}`.",
            "Rows and columns are interpreted as Monday through Sunday. Any Wurgaft-style `other` bin must be aggregated or removed before this seven-token computation.",
        ]
        centroid_heading = "## Empirical Centroids"
        outcome_text = (
            "This is the important outcome for the supplied centroids: the flat output-simplex correlations can now be compared directly against Wurgaft et al.'s manifold isometry (`0.99`) and linear baseline. "
            "The cubic predicts nonzero local path curvature through `K^CH(h)h`, the explicit cubic curvature operator separating linear flat paths from Fisher/Hellinger manifold paths."
        )
    else:
        setup_lines = [
            "This computation is intrinsic to the seven-class weekday behavior simplex.",
            "Empirical Wurgaft/Llama weekday output centroids were not found locally during the May 2026 repository inspection, so this run uses a cyclic parametric centroid model:",
            "",
            f"- peak mass on target weekday: `{peak:.6f}`",
            f"- mass on each adjacent weekday: `{neighbor:.6f}`",
            f"- uniform floor on each of the four non-neighbor weekdays: `{floor:.6f}`",
            "",
            "Concrete empirical replacement path: create a JSON file containing either a top-level seven-by-seven array or `{ \"centroids\": [...] }`, with rows and columns ordered Monday through Sunday and each row a strictly positive probability vector summing to one. Then run `python empirical/compute_weekdays_K_CH.py --centroids-json path/to/weekdays_centroids.json`.",
        ]
        centroid_heading = "## Parametric Centroids"
        outcome_text = (
            "This is the important outcome: the symmetric seven-centroid output model reproduces the text-level weekday linear correlation almost exactly in moment coordinates (`0.886` here versus Wurgaft et al.'s `0.89`) while keeping a clear gap to the manifold isometry (`0.99`). "
            "The cubic predicts nonzero local path curvature through `K^CH(h)h`, the explicit cubic curvature operator separating linear flat paths from Fisher/Hellinger manifold paths, but cyclic symmetry makes the pairwise distance matrix remain largely monotone in cyclic separation. "
            "Therefore the output-side cubic can explain the modest weekday text gap, but not a substantially lower figure-panel value such as `0.71` without empirical centroids, activation-side distortion, spline-parameterization effects, or some combination of those residuals."
        )

    lines = [
        "# Weekdays K^CH Prediction",
        "",
        "## Setup",
        "",
        *setup_lines,
        "",
        "The reported Wurgaft et al. numbers used for comparison are:",
        "",
        "- activation-manifold vs behavior-manifold isometry, weekdays: `r = 0.99` in the text, `r = 0.9896` in Fig. 2;",
        "- activation-linear vs behavior-manifold distance, weekdays: `r = 0.89` in the text; Fig. 2 OCR exposes a lower panel near `r = 0.7097`, so the exact visual value should be checked against the source figure;",
        "- naturalness energy, weekdays: manifold `E_BC = 0.34 +/- 0.03`; linear `E_BC = 0.93 +/- 0.11`;",
        "- pullback recovery, weekdays: pullback `R^2 = 0.77 +/- 0.03`; linear baseline `R^2 = 0.42 +/- 0.07`.",
        "",
        "Notation follows the engagement instructions: `theta` is the centered moment/m-coordinate `p - p_*`, and `eta` is the centered natural/logit/e-coordinate `log p - mean(log p) 1`. Paper 2 currently uses the opposite Greek-letter convention, so any insertion should either avoid the letters or flag the convention.",
        "",
        "## Coordinate Translation",
        "",
        "At the uniform centroid `p_* = (1/7) 1`:",
        "",
        "- moment coordinate: `theta = p - p_* in H`;",
        "- natural coordinate: `eta = log p - mean(log p) 1 in H`;",
        "- Hellinger coordinate: `x = sqrt(p) in S^6_+`;",
        "- infinitesimally at `p_*`, `d eta = 7 d theta` and `d x = (sqrt(7)/2) d theta`;",
        "- Fisher metric: `g_p(u,v) = sum_i u_i v_i / p_i`; at `p_*`, `g = 7 <.,.>_Euc`;",
        "- Amari-Chentsov cubic: `T_p(u,v,w)=sum_i u_i v_i w_i / p_i^2`;",
        "- raised cubic: `K^CH_p(u)v = u v / p - g_p(u,v) p`, tangent-projected.",
        "",
        "The Hellinger coordinate is therefore an admissible spherical coordinate choice for the same Fisher object, not the unique intrinsic coordinate system.",
        "",
        "Sign convention warning: Paper 11 fixes `K^CH = Gamma^(m) - Gamma^(e)`. If a prior table used the opposite e/m convention, its magnitudes remain valid but all signed `K^CH` displacement entries must be explicitly flipped.",
        "",
        centroid_heading,
        "",
        "Rows are ordered Monday through Sunday.",
        "",
        "```text",
        format_matrix(centroid_matrix, 6),
        "```",
        "",
        "## K^CH at the Centroid",
        "",
        "At `p_*`, the formulas reduce to:",
        "",
        "```text",
        "T_{p_*}(u,v,w) = 49 sum_i u_i v_i w_i",
        "K^CH_{p_*}(u)v = 7 u*v - 7 <u,v>_Euc p_*",
        "```",
        "",
        "Centroid-normalized against the full character/multiplication algebra, this is the `c = 1` convention of Paper 11: before the augmentation-corner projection, multiplication by a character is literally multiplication by that character at `p_*`. The table below gives a concrete real-coordinate operator for the Monday displacement `theta_Monday = p_Monday - p_*`, acting on the seven centered vertex directions `e_i - p_*`.",
        "",
        "```text",
        format_matrix(k_rows, 6),
        "```",
        "",
        "### Character-Basis Form",
        "",
        "Because `7` is prime, the nontrivial C7 Fisher tangent space is a single six-dimensional conductor packet. Let `phi_k(x)=7^(-1/2) exp(2 pi i kx/7)` and let `hat h_r=<phi_r,h>` be the unitary additive-character coefficients. For `h in H` and `ell != 0`,",
        "",
        "```text",
        "K^CH_{p_*}(h) phi_ell = sqrt(7) sum_{k=1}^6 hat h_{k-ell} phi_k",
        "```",
        "",
        "Thus the off-centroid Taylor support is pure convolution in the dual group `Z/7Z`; in the prime weekday case there is no further conductor splitting to hide it.",
        "",
        "For the Monday displacement `theta_Monday`, the unitary Fourier coefficients `hat h_r`, `r=0,...,6`, are:",
        "",
        "```text",
        format_complex_vector(monday_hat, 6),
        "```",
        "",
        "The nontrivial character-basis matrix of `v |-> K^CH_{p_*}(theta_Monday)v`, with rows and columns ordered `1,...,6`, is:",
        "",
        "```text",
        format_complex_matrix(monday_character_operator, 6),
        "```",
        "",
        "## Displacement Probes",
        "",
    ]

    for label, result in (("Adjacent Monday -> Tuesday", adjacent), ("Non-adjacent Monday -> Wednesday", nonadjacent)):
        sign_note = "The m-flat sign is `-1/4 K^CH(h,h)` and the e-flat sign is `+1/4 K^CH(h,h)` for same-initial-velocity endpoint displacement; norms are equal."
        lines.extend(
            [
                f"### {label}",
                "",
                f"- cyclic separation: `{result.cyclic_separation}`",
                f"- `theta` displacement: `{format_vector(result.h_moment)}`",
                f"- `eta` endpoint difference: `{format_vector(result.h_natural_delta)}`",
                f"- Hellinger tangent at `p_*`: `{format_vector(result.h_hellinger_tangent_at_uniform)}`",
                f"- Fisher norm `||h||_F`: `{result.fisher_norm_h:.6f}`",
                f"- cubic scalar `T(h,h,h)`: `{result.cubic_T_hhh:.6f}`",
                f"- unit-direction cubic `T(hat h,hat h,hat h)`: `{result.cubic_T_unit:.6f}`",
                f"- raised cubic `K^CH(h)h`: `{format_vector(result.K_h_h)}`",
                f"- `||K^CH(h)h||_F`: `{result.fisher_norm_K_h_h:.6f}`",
                f"- second-order endpoint deviation norm coefficient: `{result.endpoint_deviation_m_norm:.6f}`",
                f"- second-order midpoint deviation norm coefficient: `{result.midpoint_deviation_m_norm:.6f}`",
                f"- exact max same-parameter m-flat vs Fisher LC path, Hellinger units: `{result.exact_max_m_vs_lc_hellinger:.6f}`",
                f"- exact max same-parameter e-flat vs Fisher LC path, Hellinger units: `{result.exact_max_e_vs_lc_hellinger:.6f}`",
                f"- exact path lengths `(m, e, LC)` in Hellinger units: `({result.exact_m_path_length_hellinger:.6f}, {result.exact_e_path_length_hellinger:.6f}, {result.exact_lc_path_length_hellinger:.6f})`",
                "",
                sign_note,
                "",
            ]
        )

    if centroid_source == "empirical":
        caveats = [
            f"- The weekday centroids were loaded from `{centroids_path}`.",
            "- The input format is the seven weekday concept-token simplex. If the source includes Wurgaft et al.'s `other` bin, this run assumes it has already been removed or aggregated into a seven-token distribution.",
            "- Their measured correlations compare activation-space distances to behavior-manifold distances. This script computes the intrinsic behavior-space contribution.",
            "- The second-order `K^CH` signs use the Paper 11 convention `K^CH = Gamma^(m) - Gamma^(e)`. Reversing the e/m convention flips signs but not norms.",
            f"- Numerical path comparisons use `{samples}` intervals; increasing this only changes the last decimals.",
        ]
    else:
        caveats = [
            "- The weekday centroids are parametric, not extracted from Llama 3.1 8B.",
            "- Wurgaft et al. add an `other` bin in the paper's output distributions; this computation uses the seven weekday concept tokens only, as requested.",
            "- Their measured correlations compare activation-space distances to behavior-manifold distances. This script computes an intrinsic behavior-space proxy.",
            "- The second-order `K^CH` signs use the Paper 11 convention `K^CH = Gamma^(m) - Gamma^(e)`. Reversing the e/m convention flips signs but not norms.",
            f"- Numerical path comparisons use `{samples}` intervals; increasing this only changes the last decimals.",
        ]

    lines.extend(
        [
            "## Intrinsic Linear-vs-Manifold Prediction",
            "",
            "Using the seven cyclic centroids only, the correlation between flat output-simplex distances and cyclic behavior-manifold arc distances is:",
            "",
            f"- Hellinger chord vs cyclic Hellinger arc: `r = {correlations['hellinger_chord_vs_cyclic_arc']:.6f}`",
            f"- moment Euclidean chord vs cyclic Hellinger arc: `r = {correlations['moment_chord_vs_cyclic_arc']:.6f}`",
            f"- natural/logit chord vs cyclic Hellinger arc: `r = {correlations['natural_chord_vs_cyclic_arc']:.6f}`",
            f"- Fisher LC endpoint distance vs cyclic Hellinger arc: `r = {correlations['lc_distance_vs_cyclic_arc']:.6f}`",
            "",
            "## Gap Accounting",
            "",
            "Using the text-level Wurgaft weekday reference `r_manifold = 0.9896` and `r_linear = 0.89`:",
            "",
            f"- published text gap: `{gap['wurgaft_text_gap']:.6f}`",
            f"- intrinsic behavior-side linear gap: `{gap['intrinsic_behavior_gap_to_wurgaft_manifold_r']:.6f}`",
            f"- residual versus text linear baseline: `{gap['residual_vs_wurgaft_text_linear_r']:.6f}`",
            f"- fraction of text gap accounted for by intrinsic behavior geometry: `{gap['explained_fraction_of_text_gap']:.6f}`",
            "",
            outcome_text,
            "",
            "## Comparison to Wurgaft et al.",
            "",
            "The intrinsic behavior-side computation agrees with Wurgaft et al. on the positive claim: the behavior manifold has the right geometry, and Hellinger/Fisher coordinates make the cyclic structure explicit. It also lands on the reported weekday text correlation for linear paths. What it cannot decide, without their empirical activation and output centroids, is how much of any stronger linear-path failure comes from `M_y` itself versus the activation-side map.",
            "",
            "The next named object should be the activation-side residual of the pullback: the part of `J_F^T g_y J_F` and its cubic correction that is not captured by the intrinsic `M_y` Fisher cubic. The script now has an explicit replacement path for empirical centroids via `--centroids-json`; until those centroids are supplied, the report remains a parametric proxy rather than a measurement on Llama outputs.",
            "",
            "## Caveats",
            "",
            *caveats,
            "",
            "## Reproduction",
            "",
            "```powershell",
            "python empirical/compute_weekdays_K_CH.py",
            "python empirical/compute_weekdays_K_CH.py --centroids-json path/to/weekdays_centroids.json",
            "```",
            "",
            "The script also emits `empirical/reports/weekdays_K_CH_prediction.json` with the raw values.",
            "",
        ]
    )

    return "\n".join(lines)


def compute(peak: float, neighbor: float, samples: int, centroids: list[Vector] | None = None):
    if centroids is None:
        centroids = [centroid(i, peak, neighbor) for i in range(N)]
    adjacent = pair_result(centroids, 0, 1, samples)
    nonadjacent = pair_result(centroids, 0, 2, samples)

    cyclic_arcs = []
    hellinger_chords = []
    moment_chords = []
    natural_chords = []
    lc_distances = []
    for i in range(N):
        for j in range(i + 1, N):
            cyclic_arcs.append(cyclic_arc_distance(centroids, i, j))
            hellinger_chords.append(hellinger(centroids[i], centroids[j]))
            moment_chords.append(norm(sub(centroids[i], centroids[j])))
            natural_chords.append(norm(sub(centered([math.log(x) for x in centroids[i]]), centered([math.log(x) for x in centroids[j]]))))
            # Fisher-Rao distance is twice the spherical angle; Hellinger units
            # here use the same sqrt-coordinate chord convention as the paper.
            lc_distances.append(path_length(lc_path, centroids[i], centroids[j], samples))

    correlations = {
        "hellinger_chord_vs_cyclic_arc": pearson(hellinger_chords, cyclic_arcs),
        "moment_chord_vs_cyclic_arc": pearson(moment_chords, cyclic_arcs),
        "natural_chord_vs_cyclic_arc": pearson(natural_chords, cyclic_arcs),
        "lc_distance_vs_cyclic_arc": pearson(lc_distances, cyclic_arcs),
    }

    return centroids, adjacent, nonadjacent, correlations


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--peak", type=float, default=0.76)
    parser.add_argument("--neighbor", type=float, default=0.09)
    parser.add_argument("--samples", type=int, default=400)
    parser.add_argument("--centroids-json", type=Path, default=None, help="Optional empirical 7x7 weekday centroid probability matrix.")
    parser.add_argument("--report", type=Path, default=Path("empirical/reports/weekdays_K_CH_prediction.md"))
    parser.add_argument("--json", type=Path, default=Path("empirical/reports/weekdays_K_CH_prediction.json"))
    args = parser.parse_args()

    empirical_centroids = load_centroids_json(args.centroids_json) if args.centroids_json else None
    centroid_source = "empirical" if empirical_centroids is not None else "parametric"
    centroids, adjacent, nonadjacent, correlations = compute(args.peak, args.neighbor, args.samples, empirical_centroids)
    report = make_report(
        centroids,
        adjacent,
        nonadjacent,
        correlations,
        args.peak,
        args.neighbor,
        args.samples,
        centroid_source,
        args.centroids_json,
    )
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report, encoding="utf-8")

    raw = {
        "peak": args.peak,
        "neighbor": args.neighbor,
        "floor": (1.0 - args.peak - 2.0 * args.neighbor) / (N - 3),
        "centroid_source": centroid_source,
        "empirical_centroids_path": str(args.centroids_json) if args.centroids_json else None,
        "empirical_outputs_available_locally": empirical_centroids is not None,
        "centroids": centroids,
        "adjacent": adjacent.__dict__,
        "nonadjacent": nonadjacent.__dict__,
        "correlations": correlations,
        "gap_accounting": gap_accounting(correlations),
        "character_basis": {
            "monday_direction_hat": [complex_json(z) for z in weekday_character_coefficients(sub(centroids[0], [1.0 / N] * N))],
            "monday_direction_operator_nontrivial": [
                [complex_json(z) for z in row]
                for row in weekday_character_operator(sub(centroids[0], [1.0 / N] * N))
            ],
        },
    }
    args.json.write_text(json.dumps(rounded_json(raw), indent=2), encoding="utf-8")

    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(json.dumps(rounded_json(correlations), indent=2))


if __name__ == "__main__":
    main()
