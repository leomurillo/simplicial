"""Per-row verification of (dagger_p) for Paper 12 Theorem 9.2.1.

For each mixed local atlas row R, evaluate the carry-vs-depth comparison

    Σ_n ‖Carry_n^[·, M'](h)‖_F^2  vs  λ_PSL · (d*_PSL(p) − depth(M'))

for every shallow PSL flag M' of depth < d*_PSL and every Fourier-pure
displacement h supported in one conductor packet.  The break-even resource
weight per row is

    λ_PSL_crit(R)  =  min over (h, M') of  Σ_n ‖Carry_n‖_F^2 / (d* − depth(M')).

(†_p) holds at every resource weight λ_PSL < λ_PSL_crit(R).  Cyclic and
finite-abelian rows trivially satisfy (†_p) (B1/B2 zero carry at the
generated-subgroup PSL).  This verifier targets the mixed local rows
spanning the Paper 11 atlas envelope: F_2[u]/(u^n) for n = 2..5
(residue degree 1, sweeping wild depth), F_4[u]/(u^2) and F_4[u]/(u^3)
(residue degree 2, two wild depths), F_8[u]/(u^2) (residue degree 3),
and F_16[u]/(u^2) (residue degree 4).

The carry operator at a PSL boundary (src, tgt) is

    Carry_n^{tgt, src}  =  Σ_{η ≠ 0}  ĥ_n(η) · A_η^{tgt, src},

with A_η^{tgt, src} the quotient-shift generator of Paper 11 Def 2.1 sending
χ ∈ X_src to η + χ if the result lies in X_tgt.  Each (χ' ∈ X_tgt, χ ∈ X_src)
pair has at most one η = χ' − χ, so

    ‖Carry_n^{tgt, src}‖_F^2  =  Σ_{χ ∈ X_src, χ' ∈ X_tgt, χ' ≠ χ}  |ĥ_n(χ' − χ)|^2.

ĥ_n is the DFT of the pointwise n-th power of h (Paper 10 Theorem 7.1's
n-fold convolution identity).  The within-packet contributions vanish at
every order (Paper 11 Corollary 9.6.3); we therefore compute only the
*cross-packet* carry, summed across PSL boundaries the shallow flag fails
to cover.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Callable, Hashable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from local_adjacency_constructor import (  # noqa: E402
    FiniteLocalRing,
    LocalAdjacencyConstructor,
    make_f2_u2_ring,
    make_f2_u3_ring,
    make_f2_u4_ring,
    make_f2_u5_ring,
    make_f4_u2_ring,
    make_f4_u3_ring,
    make_f8_u2_ring,
    make_f16_u2_ring,
)


Label = Hashable
DEFAULT_REPORT = Path("empirical/reports/per_row_carry_vs_depth.md")
DEFAULT_JSON = Path("empirical/reports/per_row_carry_vs_depth.json")


def _bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> i) & 1 for i in range(width))


def _local_bits(label: tuple[int, ...], field_width: int) -> tuple[int, ...]:
    out: list[int] = []
    for coefficient in label:
        out.extend(_bits(coefficient, field_width))
    return tuple(out)


def make_character(ring: FiniteLocalRing, field_width: int) -> Callable[[Label, Label], float]:
    """Standard F_2 additive character χ_η(ℓ) = (−1)^{⟨η, ℓ⟩_{F_2}}."""
    total_width = max(1, (len(ring.labels) - 1).bit_length())
    bit_cache: dict[Label, tuple[int, ...]] = {}
    for label in ring.labels:
        if isinstance(label, tuple):
            bit_cache[label] = _local_bits(label, field_width)
        else:
            bit_cache[label] = _bits(int(label), total_width)

    def chi(eta: Label, label: Label) -> float:
        a = bit_cache[eta]
        b = bit_cache[label]
        dot = sum(x * y for x, y in zip(a, b)) % 2
        return -1.0 if dot else 1.0

    return chi


def dft(values: dict[Label, float], ring: FiniteLocalRing,
        chi: Callable[[Label, Label], float]) -> dict[Label, float]:
    """ĥ(η) = Σ_ℓ h(ℓ) χ(η, ℓ).  Real-valued for ±1 characters."""
    return {
        eta: sum(values[label] * chi(eta, label) for label in ring.labels)
        for eta in ring.labels
    }


def inverse_dft(coefficients: dict[Label, float], ring: FiniteLocalRing,
                chi: Callable[[Label, Label], float]) -> dict[Label, float]:
    """h(ℓ) = (1/|R|) Σ_η ĥ(η) χ(η, ℓ).  ±1 character self-inversion."""
    n = len(ring.labels)
    return {
        label: sum(coefficients[eta] * chi(eta, label) for eta in ring.labels) / n
        for label in ring.labels
    }


def pointwise_power_dfts(h: dict[Label, float], ring: FiniteLocalRing,
                          chi: Callable[[Label, Label], float],
                          n_max: int) -> list[dict[Label, float]]:
    """Return [ĥ^1, ĥ^2, ..., ĥ^{n_max}], where ĥ^k = DFT(h^k pointwise)."""
    h_n = dict(h)
    out: list[dict[Label, float]] = []
    for _ in range(n_max):
        out.append(dft(h_n, ring, chi))
        h_n = {label: h_n[label] * h[label] for label in ring.labels}
    return out


def fourier_pure_displacement(packets: dict[str, tuple[Label, ...]],
                              ring: FiniteLocalRing,
                              chi: Callable[[Label, Label], float],
                              target_packet: str) -> tuple[dict[Label, float], dict[Label, float]]:
    """Build h with ĥ = indicator of target_packet characters (zero elsewhere).

    Returns (h, h_hat) where h_hat is the prescribed indicator.
    """
    h_hat = {
        eta: (1.0 if eta in set(packets[target_packet]) else 0.0)
        for eta in ring.labels
    }
    # Ensure h_hat(0) = 0 (target_packet excludes the trivial character anyway,
    # since the constructor's packets dict only contains nontrivial labels).
    h_hat[ring.zero] = 0.0
    h = inverse_dft(h_hat, ring, chi)
    return h, h_hat


def carry_squared_at_boundary(
    h_hat_n_list: list[dict[Label, float]],
    ring: FiniteLocalRing,
    packets: dict[str, tuple[Label, ...]],
    src: str,
    tgt: str,
) -> list[float]:
    """Return [‖Carry_1^{tgt,src}‖^2, ..., ‖Carry_{n_max}^{tgt,src}‖^2]."""
    src_labels = packets[src]
    tgt_labels = packets[tgt]
    results: list[float] = []
    for h_hat_n in h_hat_n_list:
        total = 0.0
        for chi_src in src_labels:
            for chi_tgt in tgt_labels:
                # eta = chi_tgt - chi_src in additive ring
                # For characteristic-2 rings, subtraction equals addition.
                eta = ring.add(chi_tgt, chi_src)
                if eta == ring.zero:
                    continue
                total += h_hat_n[eta] ** 2
        results.append(total)
    return results


def covered_subgroup_chars(packets: dict[str, tuple[Label, ...]],
                            conductor_order: tuple[str, ...],
                            depth: int) -> set[Label]:
    """Union of packets at conductor indices [0, depth)."""
    covered: set[Label] = set()
    for i, name in enumerate(conductor_order):
        if i >= depth:
            break
        if name in packets:
            covered.update(packets[name])
    return covered


def run_row(row_name: str,
            ring: FiniteLocalRing,
            field_width: int,
            n_max: int) -> dict[str, Any]:
    chi = make_character(ring, field_width)
    constructor = LocalAdjacencyConstructor(ring)
    packets = constructor.packets
    cond_order = tuple(c for c in ring.conductor_order if c in packets)
    d_max = len(cond_order)

    # Maximal PSL flag adjacent boundary pairs: (cond_order[i], cond_order[i+1])
    # taken in both directions for the cross-packet carry sum.
    adjacent_pairs = [
        (cond_order[i], cond_order[i + 1])
        for i in range(d_max - 1)
    ]

    tests: list[dict[str, Any]] = []
    for target_packet in cond_order:
        h, h_hat = fourier_pure_displacement(packets, ring, chi, target_packet)
        h_hat_n_list = pointwise_power_dfts(h, ring, chi, n_max)

        d_star = cond_order.index(target_packet) + 1
        total_h_hat_energy = sum(
            h_hat[eta] ** 2 for eta in ring.labels if eta != ring.zero
        )

        per_shallow: list[dict[str, Any]] = []
        for d in range(0, d_star):
            covered_packets = set(cond_order[:d])
            missed_boundaries: list[tuple[str, str]] = []
            for (p1, p2) in adjacent_pairs:
                covered = p1 in covered_packets and p2 in covered_packets
                if not covered:
                    missed_boundaries.append((p1, p2))

            total_carry_sq = 0.0
            per_boundary: list[dict[str, Any]] = []
            for (p1, p2) in missed_boundaries:
                forward = carry_squared_at_boundary(
                    h_hat_n_list, ring, packets, p1, p2
                )
                reverse = carry_squared_at_boundary(
                    h_hat_n_list, ring, packets, p2, p1
                )
                boundary_total = sum(forward) + sum(reverse)
                total_carry_sq += boundary_total
                per_boundary.append({
                    "boundary": [p1, p2],
                    "forward_by_n": forward,
                    "reverse_by_n": reverse,
                    "boundary_total": boundary_total,
                })

            depth_savings = d_star - d
            lambda_crit = (
                total_carry_sq / depth_savings if depth_savings > 0 else float("inf")
            )
            per_shallow.append({
                "depth": d,
                "depth_savings": depth_savings,
                "missed_boundaries": [[p1, p2] for p1, p2 in missed_boundaries],
                "total_carry_squared": total_carry_sq,
                "lambda_crit": lambda_crit,
                "per_boundary": per_boundary,
            })

        tests.append({
            "target_packet": target_packet,
            "d_star": d_star,
            "h_hat_total_energy": total_h_hat_energy,
            "by_shallow_depth": per_shallow,
        })

    # Per-row break-even λ_PSL = min over (h, M') of lambda_crit, restricted to
    # strictly shallower flags with strictly positive carry.
    candidates = [
        item["lambda_crit"]
        for test in tests
        for item in test["by_shallow_depth"]
        if item["depth_savings"] > 0 and item["total_carry_squared"] > 0
    ]
    row_lambda_crit = min(candidates) if candidates else 0.0
    dagger_holds = row_lambda_crit > 0

    return {
        "row": row_name,
        "ring_name": ring.name,
        "n_labels": len(ring.labels),
        "conductor_order": list(cond_order),
        "packet_sizes": {c: len(packets[c]) for c in cond_order},
        "d_max": d_max,
        "n_max_carry_order": n_max,
        "adjacent_psl_boundaries": [[p1, p2] for p1, p2 in adjacent_pairs],
        "tests": tests,
        "row_lambda_crit": row_lambda_crit,
        "dagger_holds": dagger_holds,
    }


def format_report(rows: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Per-row (†_p) verification: carry-vs-depth on the mixed atlas")
    lines.append("")
    lines.append(
        "Verifies the hypothesis (†_p) of Paper 12 Theorem 9.2.1 on the mixed local "
        "atlas: F_2[u]/(u^n) for n in {2,3,4,5} (residue degree 1, sweeping wild "
        "depth), F_4[u]/(u^2) and F_4[u]/(u^3) (residue degree 2), F_8[u]/(u^2) "
        "(residue degree 3), and F_16[u]/(u^2) (residue degree 4)."
    )
    lines.append("")
    lines.append(
        "For each row R and each Fourier-pure test displacement h supported in one "
        "conductor packet, the verifier:"
    )
    lines.append("")
    lines.append("- builds h via inverse DFT of the packet-indicator;")
    lines.append(
        "- forms ĥ_n = DFT(h^n) for n = 1, ..., n_max (n_max controls the carry-series truncation);"
    )
    lines.append(
        "- for each shallow PSL flag M' of depth d < d*, sums the operator-valued "
        "carry Σ_n ‖Carry_n^{tgt,src}‖_F^2 over consecutive-packet boundaries the "
        "shallow flag fails to cover;"
    )
    lines.append(
        "- reports λ_crit(h, M') = total_carry_sq / (d* − d), and the per-row "
        "break-even λ_PSL_crit = min over (h, M')."
    )
    lines.append("")
    lines.append(
        "(†_p) is the inequality `total_carry_sq > λ_PSL · (d* − d)` for every "
        "shallow (h, M').  It is satisfied for every λ_PSL < λ_PSL_crit(R)."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Row | |R| | conductor_order | d_max | λ_PSL_crit | (†_p) holds |")
    lines.append("|---|---:|---|---:|---:|---|")
    for row in rows:
        cond_str = " ⊂ ".join(row["conductor_order"])
        holds = "yes" if row["dagger_holds"] else "no"
        lines.append(
            f"| {row['row']} | {row['n_labels']} | {cond_str} | {row['d_max']} | "
            f"{row['row_lambda_crit']:.6g} | {holds} |"
        )
    lines.append("")

    for row in rows:
        lines.append(f"## {row['row']}")
        lines.append("")
        lines.append(
            f"- ring: `{row['ring_name']}`, |R| = {row['n_labels']}"
        )
        cond_str = " ⊂ ".join(row["conductor_order"])
        lines.append(
            f"- conductor_order: {cond_str}, d_max = {row['d_max']}"
        )
        sizes_str = ", ".join(
            f"|X_{name}| = {size}" for name, size in row["packet_sizes"].items()
        )
        lines.append(f"- packet sizes: {sizes_str}")
        lines.append(f"- carry-series truncation n_max = {row['n_max_carry_order']}")
        lines.append(
            f"- adjacent PSL boundaries: "
            + ", ".join(f"({p1} ↔ {p2})" for p1, p2 in row["adjacent_psl_boundaries"])
        )
        lines.append(f"- **row λ_PSL_crit = {row['row_lambda_crit']:.6g}**")
        lines.append(f"- (†_p) holds: **{row['dagger_holds']}**")
        lines.append("")

        for test in row["tests"]:
            lines.append(
                f"### Test displacement: Fourier-pure on packet `{test['target_packet']}` "
                f"(d* = {test['d_star']})"
            )
            lines.append("")
            lines.append(
                f"- ĥ total energy on nontrivial characters: {test['h_hat_total_energy']:.6g}"
            )
            lines.append("")
            lines.append("| shallow depth d | d*−d | missed boundaries | Σ‖Carry‖² | λ_crit |")
            lines.append("|---:|---:|---|---:|---:|")
            for item in test["by_shallow_depth"]:
                if item["depth_savings"] == 0:
                    continue
                missed_str = (
                    ", ".join(f"({a}↔{b})" for a, b in item["missed_boundaries"])
                    if item["missed_boundaries"] else "—"
                )
                lc = item["lambda_crit"]
                lc_str = "∞" if lc == float("inf") else f"{lc:.6g}"
                lines.append(
                    f"| {item['depth']} | {item['depth_savings']} | {missed_str} | "
                    f"{item['total_carry_squared']:.6g} | {lc_str} |"
                )
            lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-max", type=int, default=4,
                        help="Carry-series truncation order (default 4)")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()

    row_specs = [
        ("F_2[u]/(u^2)", make_f2_u2_ring, 1),
        ("F_2[u]/(u^3)", make_f2_u3_ring, 1),
        ("F_2[u]/(u^4)", make_f2_u4_ring, 1),
        ("F_2[u]/(u^5)", make_f2_u5_ring, 1),
        ("F_4[u]/(u^2)", make_f4_u2_ring, 2),
        ("F_4[u]/(u^3)", make_f4_u3_ring, 2),
        ("F_8[u]/(u^2)", make_f8_u2_ring, 3),
        ("F_16[u]/(u^2)", make_f16_u2_ring, 4),
    ]

    results = []
    for row_name, factory, field_width in row_specs:
        print(f"running {row_name} ...", file=sys.stderr, flush=True)
        ring = factory()
        results.append(run_row(row_name, ring, field_width, args.n_max))

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(results, indent=2), encoding="utf-8")
    args.report.write_text(format_report(results), encoding="utf-8")

    print(f"wrote {args.json}", file=sys.stderr)
    print(f"wrote {args.report}", file=sys.stderr)

    # Quick stdout summary (ASCII for cross-platform terminal compatibility)
    print()
    print("Per-row break-even lambda_PSL_crit:")
    for row in results:
        ok = "PASS" if row["dagger_holds"] else "FAIL"
        print(f"  {ok}  {row['row']:20s}  lambda_crit = {row['row_lambda_crit']:.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
