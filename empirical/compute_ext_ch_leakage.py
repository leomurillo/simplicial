"""Empirical Ext_CH leakage extractor for R = F_4[u]/(u^2).

This script does not query a model.  It consumes a 2D grid of 16-label logits
or probabilities and computes the character-basis contractions needed for the
mixed tame/wild diagnostic in Papers 11-12.

Accepted JSON shapes:

    {"logits_grid": [[[...16...], ... r-grid ...], ... s-grid ...]}
    {"probs_grid":  [[[...16...], ... r-grid ...], ... s-grid ...]}

The first two grid coordinates are tame intensity s and wild intensity r.
The minimal useful shape is 2x2x16; 3x3x16 is also accepted and currently uses
the lower-left 2x2 forward mixed difference for the first local estimate.

The output reports three related objects:

1. raw mixed cubic tensor:
       T(p11)-T(p10)-T(p01)+T(p00)
2. mixed composition defect:
       Delta(p11)-Delta(p10)-Delta(p01)+Delta(p00)
   where Delta_ab = Kbar(a)Kbar(b)-Kbar(a+b)
3. pure-tame negative-control leakage from p10 into wild output characters.

The character basis is the self-dual Walsh basis on the additive group
F_2^4, with labels written as a+b*u, a,b in F_4.  This choice preserves
character multiplication by label addition, which is the support datum used
by the Ext_CH atlas.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np


Label = tuple[int, int]

F4_NAMES = {
    0: "0",
    1: "1",
    2: "w",
    3: "w+1",
}

ZERO: Label = (0, 0)
LABELS: list[Label] = [(a, b) for a in range(4) for b in range(4)]
NONTRIVIAL: list[Label] = [x for x in LABELS if x != ZERO]
TAME: list[Label] = [(0, b) for b in range(1, 4)]
WILD: list[Label] = [(a, b) for a in range(1, 4) for b in range(4)]


@dataclass(frozen=True)
class TopEntry:
    value_abs: float
    value_real: float
    alpha: str
    beta: str
    input: str
    output: str


@dataclass(frozen=True)
class LeakageReport:
    grid_shape: tuple[int, int, int]
    base_entropy: float
    base_l1_from_uniform: float
    dominant_tame_mode: str
    dominant_wild_mode: str
    dominant_tame_coeff_abs: float
    dominant_wild_coeff_abs: float
    pure_tame_to_wild_max_abs: float
    pure_tame_to_wild_l2: float
    raw_mixed_wild_hits_threshold: float
    raw_mixed_wild_hits: int
    raw_mixed_expected_hits: int
    raw_mixed_expected_hit_mass: float
    defect_mixed_max_abs: float
    defect_mixed_l2: float
    defect_top_entries: list[TopEntry]


def f4_bits(x: int) -> tuple[int, int]:
    return (x & 1, (x >> 1) & 1)


def bit_dot_label(a: Label, x: Label) -> int:
    aa0, aa1 = f4_bits(a[0])
    ab0, ab1 = f4_bits(a[1])
    xa0, xa1 = f4_bits(x[0])
    xb0, xb1 = f4_bits(x[1])
    return (aa0 & xa0) ^ (aa1 & xa1) ^ (ab0 & xb0) ^ (ab1 & xb1)


def add_label(x: Label, y: Label) -> Label:
    return (x[0] ^ y[0], x[1] ^ y[1])


def conductor(x: Label) -> str:
    if x == ZERO:
        return "1"
    if x[0] == 0:
        return "u"
    return "u^2"


def label_name(x: Label) -> str:
    a, b = x
    if x == ZERO:
        return "0"

    def nil_name(value: int) -> str:
        if value == 0:
            return ""
        if value == 1:
            return "u"
        if value == 2:
            return "wu"
        return "(w+1)u"

    if b == 0:
        return F4_NAMES[a]
    if a == 0:
        return nil_name(b)
    return f"{F4_NAMES[a]}+{nil_name(b)}"


def softmax_last_axis(logits: np.ndarray) -> np.ndarray:
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exps = np.exp(shifted)
    return exps / np.sum(exps, axis=-1, keepdims=True)


def load_grid(path: Path) -> np.ndarray:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if "probs_grid" in payload:
        grid = np.asarray(payload["probs_grid"], dtype=float)
    elif "logits_grid" in payload:
        grid = softmax_last_axis(np.asarray(payload["logits_grid"], dtype=float))
    else:
        raise ValueError("JSON must contain either 'logits_grid' or 'probs_grid'")
    return validate_probs_grid(grid)


def validate_probs_grid(grid: np.ndarray) -> np.ndarray:
    if grid.ndim != 3 or grid.shape[-1] != 16:
        raise ValueError(f"expected grid shape SxRx16; got {grid.shape}")
    if grid.shape[0] < 2 or grid.shape[1] < 2:
        raise ValueError("need at least a 2x2 grid")
    if np.any(grid <= 0.0):
        raise ValueError("probabilities must be strictly positive")
    totals = np.sum(grid, axis=-1, keepdims=True)
    if not np.allclose(totals, 1.0, rtol=1e-8, atol=1e-8):
        grid = grid / totals
    return grid


def character_matrix() -> np.ndarray:
    """Rows are character labels, columns are outcome labels."""

    return np.asarray(
        [[1.0 if bit_dot_label(alpha, x) == 0 else -1.0 for x in LABELS] for alpha in LABELS],
        dtype=float,
    )


CHAR = character_matrix()
NONTRIVIAL_INDEX = {label: i for i, label in enumerate(NONTRIVIAL)}


def fourier_coeffs(vector: np.ndarray) -> np.ndarray:
    """Unnormalized-character coefficients c_alpha with vector=sum c_alpha chi_alpha."""

    return (CHAR @ vector) / 16.0


def fisher_inner(p: np.ndarray, u: np.ndarray, v: np.ndarray) -> float:
    return float(np.sum(u * v / p))


def ch_raise(p: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return (u * v / p) - fisher_inner(p, u, v) * p


def kbar_operator(p: np.ndarray, alpha: Label) -> np.ndarray:
    """Centroid-normalized Kbar_p(alpha) on nontrivial character coordinates.

    At p_*=1/16 this sends chi_beta to chi_{alpha+beta} with coefficient 1,
    unless alpha+beta is trivial, in which case the augmentation-corner output
    is zero.
    """

    matrix = np.zeros((15, 15), dtype=float)
    u = CHAR[LABELS.index(alpha)]
    for col, beta in enumerate(NONTRIVIAL):
        v = CHAR[LABELS.index(beta)]
        y = ch_raise(p, u, v)
        coeffs = fourier_coeffs(y) / 16.0
        for row, gamma in enumerate(NONTRIVIAL):
            matrix[row, col] = coeffs[LABELS.index(gamma)]
    return matrix


def defect_tensor(p: np.ndarray) -> np.ndarray:
    """Return D[alpha,beta,out,input] for K(a)K(b)-K(a+b)."""

    kops = {alpha: kbar_operator(p, alpha) for alpha in NONTRIVIAL}
    out = np.zeros((15, 15, 15, 15), dtype=float)
    for ia, alpha in enumerate(NONTRIVIAL):
        for ib, beta in enumerate(NONTRIVIAL):
            gamma = add_label(alpha, beta)
            direct = np.zeros((15, 15), dtype=float) if gamma == ZERO else kops[gamma]
            out[ia, ib] = kops[alpha] @ kops[beta] - direct
    return out


def raw_cubic_tensor(p: np.ndarray) -> np.ndarray:
    """Return C[alpha,beta,gamma] = g_p(K(alpha) beta, gamma), centroid-scaled."""

    # The 16^-2 scale makes the centroid coefficients O(1); support is unchanged.
    inv_p2 = 1.0 / (p * p)
    tensor = np.zeros((15, 15, 15), dtype=float)
    for ia, alpha in enumerate(NONTRIVIAL):
        ca = CHAR[LABELS.index(alpha)]
        for ib, beta in enumerate(NONTRIVIAL):
            cb = CHAR[LABELS.index(beta)]
            for ig, gamma in enumerate(NONTRIVIAL):
                cg = CHAR[LABELS.index(gamma)]
                tensor[ia, ib, ig] = float(np.sum(ca * cb * cg * inv_p2) / (16.0 * 16.0))
    return tensor


def forward_mixed_difference(values: np.ndarray) -> np.ndarray:
    """Lower-left 2x2 mixed finite difference: f11 - f10 - f01 + f00."""

    return values[1, 1] - values[1, 0] - values[0, 1] + values[0, 0]


def top_defect_entries(delta_defect: np.ndarray, limit: int) -> list[TopEntry]:
    flat = np.abs(delta_defect).ravel()
    if flat.size == 0:
        return []
    indices = np.argsort(flat)[::-1][:limit]
    entries: list[TopEntry] = []
    for flat_index in indices:
        ia, ib, out, inp = np.unravel_index(flat_index, delta_defect.shape)
        value = float(delta_defect[ia, ib, out, inp])
        entries.append(
            TopEntry(
                value_abs=abs(value),
                value_real=value,
                alpha=label_name(NONTRIVIAL[ia]),
                beta=label_name(NONTRIVIAL[ib]),
                input=label_name(NONTRIVIAL[inp]),
                output=label_name(NONTRIVIAL[out]),
            )
        )
    return entries


def dominant_modes(grid: np.ndarray) -> tuple[Label, Label, float, float]:
    p00, p10, p01 = grid[0, 0], grid[1, 0], grid[0, 1]
    hs = p10 - p00
    hr = p01 - p00
    cs = fourier_coeffs(hs)
    cr = fourier_coeffs(hr)
    tame = max(TAME, key=lambda x: abs(cs[LABELS.index(x)]))
    wild = max(WILD, key=lambda x: abs(cr[LABELS.index(x)]))
    return tame, wild, float(abs(cs[LABELS.index(tame)])), float(abs(cr[LABELS.index(wild)]))


def compute_ext_ch_leakage(probs_grid: np.ndarray, *, threshold: float = 1e-8, top: int = 20) -> LeakageReport:
    grid = validate_probs_grid(np.asarray(probs_grid, dtype=float))
    p00 = grid[0, 0]
    uniform = np.full(16, 1.0 / 16.0)
    tame_mode, wild_mode, tame_abs, wild_abs = dominant_modes(grid)

    raw_grid = np.empty(grid.shape[:2] + (15, 15, 15), dtype=float)
    defect_grid = np.empty(grid.shape[:2] + (15, 15, 15, 15), dtype=float)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            raw_grid[i, j] = raw_cubic_tensor(grid[i, j])
            defect_grid[i, j] = defect_tensor(grid[i, j])

    raw_mixed = forward_mixed_difference(raw_grid)
    defect_mixed = forward_mixed_difference(defect_grid)

    wild_rows = [NONTRIVIAL_INDEX[label] for label in WILD]
    tame_cols = [NONTRIVIAL_INDEX[label] for label in TAME]

    # Pure tame negative control: Kbar_{p10}(tame) maps tame input to wild output.
    p10 = grid[1, 0]
    pure_values = []
    for alpha in TAME:
        kop = kbar_operator(p10, alpha)
        pure_values.append(kop[np.ix_(wild_rows, tame_cols)])
    pure_arr = np.asarray(pure_values)

    # Raw mixed expected hits for dominant omega: gamma = alpha + beta + omega.
    expected_positions: list[tuple[int, int, int]] = []
    for ia, alpha in enumerate(TAME):
        for ib, beta in enumerate(TAME):
            gamma = add_label(add_label(alpha, beta), wild_mode)
            if gamma in NONTRIVIAL_INDEX and conductor(gamma) == "u^2":
                expected_positions.append(
                    (NONTRIVIAL_INDEX[alpha], NONTRIVIAL_INDEX[beta], NONTRIVIAL_INDEX[gamma])
                )

    raw_wild_mask = np.zeros_like(raw_mixed, dtype=bool)
    raw_wild_mask[:, :, wild_rows] = True
    raw_hits = int(np.count_nonzero(np.abs(raw_mixed[raw_wild_mask]) > threshold))
    expected_mass = float(sum(abs(raw_mixed[pos]) for pos in expected_positions))

    entropy = -float(np.sum(p00 * np.log(p00)))
    report = LeakageReport(
        grid_shape=tuple(int(x) for x in grid.shape),
        base_entropy=entropy,
        base_l1_from_uniform=float(np.sum(np.abs(p00 - uniform))),
        dominant_tame_mode=label_name(tame_mode),
        dominant_wild_mode=label_name(wild_mode),
        dominant_tame_coeff_abs=tame_abs,
        dominant_wild_coeff_abs=wild_abs,
        pure_tame_to_wild_max_abs=float(np.max(np.abs(pure_arr))),
        pure_tame_to_wild_l2=float(np.linalg.norm(pure_arr.ravel())),
        raw_mixed_wild_hits_threshold=threshold,
        raw_mixed_wild_hits=raw_hits,
        raw_mixed_expected_hits=len(expected_positions),
        raw_mixed_expected_hit_mass=expected_mass,
        defect_mixed_max_abs=float(np.max(np.abs(defect_mixed))),
        defect_mixed_l2=float(np.linalg.norm(defect_mixed.ravel())),
        defect_top_entries=top_defect_entries(defect_mixed, top),
    )
    return report


def compute_Ext_CH_leakage(logits_grid: Any, *, threshold: float = 1e-8, top: int = 20) -> LeakageReport:
    """Convenience wrapper requested by the paper notes.

    Pass a NumPy/PyTorch-like logits tensor with shape SxRx16.  The function
    softmaxes the last axis and returns the same report as compute_ext_ch_leakage.
    """

    probs = softmax_last_axis(np.asarray(logits_grid, dtype=float))
    return compute_ext_ch_leakage(probs, threshold=threshold, top=top)


def write_markdown(report: LeakageReport, path: Path) -> None:
    lines = [
        "# Ext_CH Leakage Extraction Report",
        "",
        f"- grid shape: `{report.grid_shape}`",
        f"- base entropy: `{report.base_entropy:.12g}`",
        f"- base L1 from uniform: `{report.base_l1_from_uniform:.12g}`",
        f"- dominant tame mode: `{report.dominant_tame_mode}` (`{report.dominant_tame_coeff_abs:.12g}`)",
        f"- dominant wild mode: `{report.dominant_wild_mode}` (`{report.dominant_wild_coeff_abs:.12g}`)",
        "",
        "## Pure-Tame Negative Control",
        "",
        f"- max wild output from tame-axis/tame-input: `{report.pure_tame_to_wild_max_abs:.12g}`",
        f"- L2 wild output from tame-axis/tame-input: `{report.pure_tame_to_wild_l2:.12g}`",
        "",
        "## Raw Mixed Cubic Leakage",
        "",
        f"- threshold: `{report.raw_mixed_wild_hits_threshold:.3g}`",
        f"- wild entries above threshold: `{report.raw_mixed_wild_hits}`",
        f"- expected dominant-omega hit positions: `{report.raw_mixed_expected_hits}`",
        f"- expected dominant-omega hit mass: `{report.raw_mixed_expected_hit_mass:.12g}`",
        "",
        "## Mixed Composition Defect",
        "",
        f"- max abs: `{report.defect_mixed_max_abs:.12g}`",
        f"- L2: `{report.defect_mixed_l2:.12g}`",
        "",
        "### Top Defect Entries",
        "",
        "| abs | value | alpha | beta | input | output |",
        "|---:|---:|---|---|---|---|",
    ]
    for entry in report.defect_top_entries:
        lines.append(
            f"| {entry.value_abs:.6g} | {entry.value_real:.6g} | "
            f"{entry.alpha} | {entry.beta} | {entry.input} | {entry.output} |"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid-json", type=Path, required=True)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--report", type=Path, default=Path("empirical/reports/ext_ch_leakage.md"))
    parser.add_argument("--threshold", type=float, default=1e-8)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    grid = load_grid(args.grid_json)
    report = compute_ext_ch_leakage(grid, threshold=args.threshold, top=args.top)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(report, args.report)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")

    print(f"wrote {args.report}")
    if args.json_out:
        print(f"wrote {args.json_out}")


if __name__ == "__main__":
    main()
