#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit lambda V/M binning post-hoc aggregation (v2insert-06 §2).

Reads the per-width sweep JSONs produced by label_smoothing_substitution_sweep.py
and aggregates over seeds to produce:

  * sigma_V(alpha, eps, W)   = f_2 + f_3 + f_4    (mean over seeds, SD)
  * sigma_M(alpha, eps, W)   = f_6 + f_12         (mean over seeds, SD)
  * rho_VM(alpha, eps, W)    = sigma_V / sigma_M  (per seed, then mean / SD)

ANCHORED [P] OBJECTS (v2insert-06 §2; v2insert-05 §1):
  V on Z/12 = H_2 + H_3 + H_4   (single-prime / prime-power axes)
  M on Z/12 = H_6 + H_12        (cross-prime carry)

P11 SETTLEMENT (v2insert-06 §2; v2insert-04 §3.1 three-outcome rule):
  K-branch: rho_VM varies monotonically with alpha along iso-loss contours
            G_IID(alpha, eps, W) = const.
  L-branch: rho_VM is iso-loss-invariant.
  joint-on-disjoint: non-monotone along the ridge (saddle, sign reversal).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

import numpy as np

SCRIPT_VERSION = "audit_lambda_VM_binning_v0.1_2026_05_20"

REPORT_DIR = Path(__file__).resolve().parent / "reports"


def aggregate(results: list[dict]) -> dict[tuple[float, float], dict[str, Any]]:
    """Group by (alpha, eps); collect seed lists for sigma_V, sigma_M, rho_VM, G_IID, ECE, gap, leakage."""
    grouped: dict[tuple[float, float], dict[str, list[Any]]] = {}
    for r in results:
        a = float(r["alpha"])
        e = float(r["epsilon"])
        key = (a, e)
        if key not in grouped:
            grouped[key] = {
                "sigma_V": [], "sigma_M": [], "rho_VM": [],
                "G_IID": [], "ECE": [], "gen_gap": [], "leakage": [],
                "test_acc": [], "train_loss": [],
                "f_2": [], "f_3": [], "f_4": [], "f_6": [], "f_12": [],
            }
        pf = r["packet_fractions_logit"]
        grouped[key]["sigma_V"].append(float(r["sigma_V"]))
        grouped[key]["sigma_M"].append(float(r["sigma_M"]))
        rho = r["rho_VM"]
        if isinstance(rho, str):
            # Was infinity
            rho_val = float("inf")
        else:
            rho_val = float(rho)
        grouped[key]["rho_VM"].append(rho_val)
        grouped[key]["G_IID"].append(float(r["final_test_loss"]))
        grouped[key]["ECE"].append(float(r["ece_test"]))
        grouped[key]["gen_gap"].append(float(r["gen_gap"]))
        grouped[key]["leakage"].append(float(r["leakage_logit"]))
        grouped[key]["test_acc"].append(float(r["final_test_acc"]))
        grouped[key]["train_loss"].append(float(r["final_train_loss"]))
        for d in (2, 3, 4, 6, 12):
            grouped[key][f"f_{d}"].append(float(pf.get(str(d), 0.0)))

    out: dict[tuple[float, float], dict[str, Any]] = {}
    for key, d in grouped.items():
        stats: dict[str, Any] = {}
        for name, vals in d.items():
            finite = [v for v in vals if math.isfinite(v)]
            stats[f"{name}_mean"] = float(np.mean(finite)) if finite else float("nan")
            stats[f"{name}_sd"] = float(np.std(finite, ddof=1)) if len(finite) > 1 else 0.0
            stats[f"{name}_n_finite"] = len(finite)
            stats[f"{name}_raw"] = vals
        out[key] = stats
    return out


def fmt(v: float, width: int = 8, prec: int = 4) -> str:
    if not math.isfinite(v):
        return f"{'inf':>{width}}"
    if abs(v) >= 10000 or (0 < abs(v) < 1e-4):
        return f"{v:>{width}.{prec}e}"
    return f"{v:>{width}.{prec}f}"


def write_per_width_report(width: int, summary: dict, out_path: Path, raw_results: list[dict],
                            sweep_meta: dict) -> None:
    """Per-Paper 37 §8 inventory: label_smoothing_substitution_months_width{W}.md."""
    alphas = sorted(sweep_meta.get("alphas", []))
    epsilons = sorted(sweep_meta.get("epsilons", []))
    seeds = sweep_meta.get("seeds", [])
    closed = sweep_meta.get("closed_support", [])

    lines: list[str] = []
    lines.append(f"# Label Smoothing Substitution Sweep -- months -- width {width}")
    lines.append("")
    lines.append(f"**Driver:** `empirical/label_smoothing_substitution_sweep.py`")
    lines.append(f"**Binning:** `empirical/label_smoothing_substitution_sweep_VM_binning.py`")
    lines.append(f"**Script versions:** sweep={sweep_meta.get('script_version','?')}, binning={SCRIPT_VERSION}")
    lines.append(f"**Pre-registered protocol:** Paper 37 §4 (5×6 grid), §8 inventory; v2insert-06 §2 V/M binning.")
    lines.append("")
    lines.append("## Setup")
    lines.append("")
    lines.append(f"- task: `months` (Z/12)")
    lines.append(f"- width (d_model): `{width}`")
    lines.append(f"- d_ff: `{2*width}`")
    lines.append(f"- epochs: `{sweep_meta.get('epochs', 300)}`")
    lines.append(f"- batch size: `{sweep_meta.get('batch_size', 16)}`")
    lines.append(f"- learning rate: `{sweep_meta.get('lr', 5e-4)}`")
    lines.append(f"- closed support S: `{closed}`")
    lines.append(f"- alphas: `{alphas}`")
    lines.append(f"- epsilons: `{epsilons}`")
    lines.append(f"- seeds: `{seeds}`")
    lines.append(f"- split: random, train_fraction=`{sweep_meta.get('train_fraction', 0.75)}`, split_seed=`{sweep_meta.get('split_seed', 4242)}`")
    lines.append("")
    lines.append("## V/M binning (Z/12, v2insert-06 §2)")
    lines.append("")
    lines.append("- V analog = H_2 + H_3 + H_4")
    lines.append("- M analog = H_6 + H_12")
    lines.append("- sigma_V = f_2 + f_3 + f_4 (logit packet fractions, mean over all cases)")
    lines.append("- sigma_M = f_6 + f_12")
    lines.append("- rho_VM = sigma_V / sigma_M, computed per-seed then averaged over seeds")
    lines.append("")

    # Anchor row
    anchor = summary.get((1.0, 0.0))
    lines.append("## Paper 12 anchor (Paper 37 §7; F2 falsifier band [3.5, 4.5])")
    lines.append("")
    if anchor is not None:
        anchor_mean = anchor['G_IID_mean']
        in_band = 3.5 <= anchor_mean <= 4.5
        lines.append(f"- (alpha=1, eps=0, W={width}): test loss mean = `{anchor_mean:.4f}` (per-seed: `{anchor['G_IID_raw']}`)")
        lines.append(f"- Paper 12 expected: `4.0514` at W=32; band `[3.5, 4.5]`")
        lines.append(f"- **Anchor in band:** `{in_band}`")
    else:
        lines.append("- anchor configuration (alpha=1, eps=0) not present in this run.")
    lines.append("")

    # Test loss heatmap
    lines.append("## G_IID(alpha, eps) heatmap (seed mean)")
    lines.append("")
    header = "| alpha\\eps |" + "|".join(f" eps={e:.2f} " for e in epsilons) + "|"
    sep = "|---:|" + "|".join("---:" for _ in epsilons) + "|"
    lines.append(header)
    lines.append(sep)
    for a in alphas:
        row = [f"a={a:.2f}"]
        for e in epsilons:
            s = summary.get((a, e))
            row.append(f"{s['G_IID_mean']:.4f}" if s is not None else "n/a")
        lines.append("|" + "|".join(row) + "|")
    lines.append("")

    # Rho_VM heatmap
    lines.append("## rho_VM(alpha, eps) heatmap (seed mean)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for a in alphas:
        row = [f"a={a:.2f}"]
        for e in epsilons:
            s = summary.get((a, e))
            if s is None:
                row.append("n/a")
            else:
                if math.isfinite(s["rho_VM_mean"]):
                    row.append(f"{s['rho_VM_mean']:.4f}")
                else:
                    row.append("inf")
        lines.append("|" + "|".join(row) + "|")
    lines.append("")

    # Sigma_V, sigma_M
    lines.append("## sigma_V(alpha, eps) heatmap")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for a in alphas:
        row = [f"a={a:.2f}"]
        for e in epsilons:
            s = summary.get((a, e))
            row.append(f"{s['sigma_V_mean']:.4f}" if s is not None else "n/a")
        lines.append("|" + "|".join(row) + "|")
    lines.append("")

    lines.append("## sigma_M(alpha, eps) heatmap")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for a in alphas:
        row = [f"a={a:.2f}"]
        for e in epsilons:
            s = summary.get((a, e))
            row.append(f"{s['sigma_M_mean']:.4f}" if s is not None else "n/a")
        lines.append("|" + "|".join(row) + "|")
    lines.append("")

    # Corner table (Paper 37 §9.4 decoupling diagnostic)
    lines.append("## Paper 37 §9.4 corner table")
    lines.append("")
    lines.append("| (alpha, eps) | G_IID | ECE | leakage | gen gap | sigma_V | sigma_M | rho_VM |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    corners = [(0.0, 0.0), (0.0, 0.1), (1.0, 0.0), (1.0, 0.1)]
    for (a, e) in corners:
        s = summary.get((a, e))
        if s is None:
            continue
        lines.append(
            f"| (a={a:.2f}, e={e:.2f}) | "
            f"{s['G_IID_mean']:.4f} | "
            f"{s['ECE_mean']:.4f} | "
            f"{s['leakage_mean']:.3e} | "
            f"{s['gen_gap_mean']:.4f} | "
            f"{s['sigma_V_mean']:.4f} | "
            f"{s['sigma_M_mean']:.4f} | "
            f"{s['rho_VM_mean']:.4f} |"
        )
    lines.append("")

    # Per-config detail
    lines.append("## Per-config detail (mean +/- sd over seeds)")
    lines.append("")
    lines.append("| alpha | eps | G_IID (sd) | ECE (sd) | leakage (sd) | sigma_V (sd) | sigma_M (sd) | rho_VM (sd) | f_2 | f_3 | f_4 | f_6 | f_12 |")
    lines.append("|---:|---:|---|---|---|---|---|---|---:|---:|---:|---:|---:|")
    for a in alphas:
        for e in epsilons:
            s = summary.get((a, e))
            if s is None:
                continue
            def mp(name): return f"{s[name+'_mean']:.4f} ({s[name+'_sd']:.4f})"
            lines.append(
                f"| {a:.2f} | {e:.2f} | "
                f"{mp('G_IID')} | {mp('ECE')} | {mp('leakage')} | "
                f"{mp('sigma_V')} | {mp('sigma_M')} | "
                f"{s['rho_VM_mean']:.4f} ({s['rho_VM_sd']:.4f}) | "
                f"{s['f_2_mean']:.4f} | {s['f_3_mean']:.4f} | {s['f_4_mean']:.4f} | "
                f"{s['f_6_mean']:.4f} | {s['f_12_mean']:.4f} |"
            )
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"# wrote {out_path}")


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="Audit lambda V/M binning aggregator")
    parser.add_argument("--input-dir", type=str, default=str(REPORT_DIR))
    parser.add_argument("--widths", type=str, default="16,32,64")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    widths = [int(w) for w in args.widths.split(",") if w.strip()]

    all_summaries: dict[int, dict[tuple[float, float], dict[str, Any]]] = {}
    sweep_metas: dict[int, dict[str, Any]] = {}

    for W in widths:
        json_path = input_dir / f"label_smoothing_substitution_months_width{W}.json"
        if not json_path.exists():
            print(f"# WARNING: {json_path} not found, skipping width {W}", file=sys.stderr)
            continue
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        results = payload["results"]
        summary = aggregate(results)
        all_summaries[W] = summary
        sweep_metas[W] = payload
        report_path = input_dir / f"label_smoothing_substitution_months_width{W}.md"
        write_per_width_report(W, summary, report_path, results, payload)

    if not all_summaries:
        print("# ERROR: no per-width JSONs found", file=sys.stderr)
        sys.exit(1)

    # Write the combined audit-lambda settlement record
    write_settlement_record(all_summaries, sweep_metas, input_dir)


def write_settlement_record(
    summaries: dict[int, dict[tuple[float, float], dict[str, Any]]],
    metas: dict[int, dict[str, Any]],
    out_dir: Path,
) -> None:
    """Synthesizes the P11 branch determination from the per-width sweeps.

    P11 branches (v2insert-06 §2):
      K: rho_VM varies monotonically with alpha along iso-loss contours.
      L: rho_VM is iso-loss-invariant (within seed noise).
      joint-on-disjoint: non-monotone along the ridge.

    Heuristic settlement (operating on what the sweep returned):
      We look at the rho_VM heatmap as a function of (alpha, eps) per width.
      Iso-loss contours are detected by binning G_IID into level bands and
      checking the rho_VM range and monotonicity inside each band.
    """
    lines: list[str] = []
    lines.append("# Audit lambda settlement record -- (alpha, eps) V/M packet signature on months")
    lines.append("")
    lines.append(f"**Binning script version:** `{SCRIPT_VERSION}`")
    lines.append("**Pre-registered protocol:** Paper 37 §4 (5×6 grid); v2insert-06 §2 P11.")
    lines.append("**Three-outcome rule (v2insert-04 §3.1):** K / L / joint-on-disjoint.")
    lines.append("")
    lines.append("## V/M definitions on Z/12 (v2insert-05 §1; v2insert-06 §2)")
    lines.append("")
    lines.append("- V analog = H_2 + H_3 + H_4 (single-prime / prime-power axes)")
    lines.append("- M analog = H_6 + H_12 (cross-prime carry)")
    lines.append("- rho_VM = sigma_V / sigma_M  (logit packet fractions, seed mean)")
    lines.append("")

    # Anchor reproductions
    lines.append("## Paper 12 anchor (Paper 37 §6 F2 falsifier)")
    lines.append("")
    lines.append("| width | (alpha=1, eps=0) test loss mean (sd) | per-seed | in band [3.5, 4.5]? |")
    lines.append("|---:|---|---|---:|")
    for W, summary in summaries.items():
        s = summary.get((1.0, 0.0))
        if s is None:
            continue
        ok = "yes" if 3.5 <= s["G_IID_mean"] <= 4.5 else "no"
        lines.append(f"| {W} | {s['G_IID_mean']:.4f} ({s['G_IID_sd']:.4f}) | {s['G_IID_raw']} | {ok} |")
    lines.append("")
    lines.append("Reference: Paper 12 §7.4.1 reports (alpha=1, eps=0, W=32) -> 4.0514 (mean over three seeds 9101/9102/9103).")
    lines.append("")

    # The plain-Adam corner check
    lines.append("## Plain-Adam corner (alpha=0, eps=0) reference")
    lines.append("")
    lines.append("| width | (alpha=0, eps=0) test loss mean (sd) |")
    lines.append("|---:|---|")
    for W, summary in summaries.items():
        s = summary.get((0.0, 0.0))
        if s is None:
            continue
        lines.append(f"| {W} | {s['G_IID_mean']:.4f} ({s['G_IID_sd']:.4f}) |")
    lines.append("")
    lines.append("Reference: Paper 12 §7.4.1 reports (alpha=0, eps=0, W=32) -> 6.125 and W=64 -> 9.0838.")
    lines.append("")

    # Per-width rho_VM(alpha, eps) and G_IID(alpha, eps) heatmap reproduced
    for W, summary in summaries.items():
        meta = metas[W]
        alphas = sorted({float(a) for (a, _) in summary.keys()})
        epsilons = sorted({float(e) for (_, e) in summary.keys()})
        lines.append(f"## Width {W}")
        lines.append("")
        lines.append("### G_IID(alpha, eps) (seed mean)")
        lines.append("")
        h1 = "| alpha\\eps |" + "|".join(f" {e:.2f} " for e in epsilons) + "|"
        s1 = "|---:|" + "|".join("---:" for _ in epsilons) + "|"
        lines.append(h1)
        lines.append(s1)
        for a in alphas:
            row = [f"{a:.2f}"]
            for e in epsilons:
                s = summary.get((a, e))
                row.append(f"{s['G_IID_mean']:.3f}" if s is not None else "n/a")
            lines.append("|" + "|".join(row) + "|")
        lines.append("")

        lines.append("### rho_VM(alpha, eps) (seed mean)")
        lines.append("")
        lines.append(h1)
        lines.append(s1)
        for a in alphas:
            row = [f"{a:.2f}"]
            for e in epsilons:
                s = summary.get((a, e))
                if s is None:
                    row.append("n/a")
                elif math.isfinite(s["rho_VM_mean"]):
                    row.append(f"{s['rho_VM_mean']:.4f}")
                else:
                    row.append("inf")
            lines.append("|" + "|".join(row) + "|")
        lines.append("")

        # Seed noise scale: median sd of rho_VM across cells where finite
        sds = [s["rho_VM_sd"] for s in summary.values()
               if math.isfinite(s["rho_VM_mean"]) and s["rho_VM_n_finite"] >= 2]
        if sds:
            sd_med = float(np.median(sds))
            lines.append(f"- median seed SD of rho_VM across (alpha, eps) cells (where finite): `{sd_med:.4f}`")
        lines.append("")

        # Iso-loss-band analysis
        lines.append("### Iso-loss band analysis")
        lines.append("")
        # Build flat array of (alpha, eps, G, rho)
        flat = []
        for (a, e), s in summary.items():
            rho = s["rho_VM_mean"]
            if math.isfinite(rho):
                flat.append((a, e, s["G_IID_mean"], rho, s["rho_VM_sd"]))
        if flat:
            g_vals = np.array([f[2] for f in flat])
            g_min, g_max = float(g_vals.min()), float(g_vals.max())
            lines.append(f"- G_IID range: [{g_min:.4f}, {g_max:.4f}]")
            # Three bands
            bands = [
                ("low", g_min, g_min + (g_max - g_min) * 0.33),
                ("mid", g_min + (g_max - g_min) * 0.33, g_min + (g_max - g_min) * 0.67),
                ("high", g_min + (g_max - g_min) * 0.67, g_max + 1e-9),
            ]
            lines.append("")
            lines.append("| band | G range | n configs | rho_VM mean | rho_VM range (min, max) | alpha range in band |")
            lines.append("|---|---|---:|---:|---|---|")
            for name, lo, hi in bands:
                inside = [f for f in flat if lo <= f[2] <= hi]
                if not inside:
                    continue
                rhos = [f[3] for f in inside]
                alphas_in = [f[0] for f in inside]
                lines.append(
                    f"| {name} | [{lo:.3f}, {hi:.3f}] | {len(inside)} | "
                    f"{np.mean(rhos):.4f} | ({min(rhos):.4f}, {max(rhos):.4f}) | "
                    f"alpha=[{min(alphas_in):.2f}, {max(alphas_in):.2f}] |"
                )
            lines.append("")

        # alpha-fixed-eps and eps-fixed-alpha slices
        lines.append("### Monotonicity slices (does rho_VM track alpha at fixed eps?)")
        lines.append("")
        lines.append("| eps | (rho at alpha=0) | (rho at alpha=1) | sign of d(rho)/d(alpha) cumulative | strictly monotone in alpha? |")
        lines.append("|---:|---:|---:|---:|:---:|")
        for e in epsilons:
            row_a = sorted([(a, summary[(a, e)]["rho_VM_mean"]) for a in alphas
                            if (a, e) in summary and math.isfinite(summary[(a, e)]["rho_VM_mean"])])
            if len(row_a) < 2:
                continue
            rho0 = row_a[0][1]; rho_end = row_a[-1][1]
            diffs = [row_a[i+1][1] - row_a[i][1] for i in range(len(row_a)-1)]
            all_neg = all(d < -1e-9 for d in diffs)
            all_pos = all(d > 1e-9 for d in diffs)
            sign = "decreasing" if (rho_end < rho0) else ("increasing" if (rho_end > rho0) else "flat")
            monotone = "yes-dec" if all_neg else ("yes-inc" if all_pos else "no")
            lines.append(f"| {e:.2f} | {rho0:.4f} | {rho_end:.4f} | {sign} | {monotone} |")
        lines.append("")

    # Cross-width branch classification heuristic
    lines.append("## P11 branch classification (heuristic)")
    lines.append("")
    lines.append("**Method (Paper 37 §9.7 V/M-tracks-ridge diagnostic, simplified):**")
    lines.append("Per width, compute the seed-noise scale = median per-cell SD of rho_VM.")
    lines.append("Compute the signal scale = max(rho_VM mean) - min(rho_VM mean) over the grid.")
    lines.append("Classify:")
    lines.append("  * If signal/noise > 2 AND rho_VM is monotone in alpha at each fixed eps -> K-branch.")
    lines.append("  * If signal/noise < 1 -> L-branch (iso-packet within seed noise).")
    lines.append("  * Otherwise -> joint-on-disjoint or ambiguous (record range).")
    lines.append("")

    lines.append("| width | seed-noise scale (SD of rho) | signal scale (range of rho) | signal/noise | monotone? | provisional branch |")
    lines.append("|---:|---:|---:|---:|:---:|---|")
    branches_per_width: dict[int, str] = {}
    for W, summary in summaries.items():
        rhos_finite = [s["rho_VM_mean"] for s in summary.values() if math.isfinite(s["rho_VM_mean"])]
        sds = [s["rho_VM_sd"] for s in summary.values()
               if math.isfinite(s["rho_VM_mean"]) and s["rho_VM_n_finite"] >= 2]
        if not rhos_finite or not sds:
            continue
        noise = float(np.median(sds))
        signal = float(max(rhos_finite) - min(rhos_finite))
        snr = signal / max(noise, 1e-9)
        epsilons = sorted({float(e) for (_, e) in summary.keys()})
        alphas = sorted({float(a) for (a, _) in summary.keys()})
        # Check monotonicity at each fixed eps
        any_mono = True
        for e in epsilons:
            row_a = sorted([(a, summary[(a, e)]["rho_VM_mean"]) for a in alphas
                            if (a, e) in summary and math.isfinite(summary[(a, e)]["rho_VM_mean"])])
            if len(row_a) < 2:
                continue
            diffs = [row_a[i+1][1] - row_a[i][1] for i in range(len(row_a)-1)]
            all_neg = all(d < -1e-9 for d in diffs)
            all_pos = all(d > 1e-9 for d in diffs)
            if not (all_neg or all_pos):
                any_mono = False
                break
        if snr > 2 and any_mono:
            branch = "K"
        elif snr < 1:
            branch = "L"
        else:
            branch = "joint-on-disjoint or ambiguous"
        branches_per_width[W] = branch
        lines.append(
            f"| {W} | {noise:.4f} | {signal:.4f} | {snr:.2f} | "
            f"{'yes' if any_mono else 'no'} | {branch} |"
        )
    lines.append("")

    # Final settlement
    lines.append("## Settlement (P11)")
    lines.append("")
    if not branches_per_width:
        lines.append("No widths analyzed. Settlement deferred.")
    else:
        # Aggregate: K if all K, L if all L, otherwise mixed/joint-on-disjoint
        vals = list(branches_per_width.values())
        if all(v == "K" for v in vals):
            verdict = "K-branch realized (rho_VM monotone in alpha at every eps slice, signal exceeds seed noise by >2x)."
        elif all(v == "L" for v in vals):
            verdict = "L-branch realized (rho_VM iso-loss-invariant within seed noise on every width)."
        elif all("joint-on-disjoint" in v or "ambiguous" in v for v in vals):
            verdict = "joint-on-disjoint realized (non-monotone or signal-comparable-to-noise on all widths)."
        else:
            verdict = "Mixed across widths: " + "; ".join(f"W={W}: {b}" for W, b in branches_per_width.items())
        lines.append(f"**P11 realized branch:** {verdict}")
        lines.append("")
        lines.append("Notes:")
        lines.append("- This classification is heuristic; the per-width tables above carry the raw data.")
        lines.append("- At alpha=1 with S={12}, the projector forces all nontrivial logit energy into H_12 ⊂ M, so sigma_V = 0 and rho_VM = 0 by construction. This is not a deflated signal -- it is the alpha=1 boundary of the V/M ratio.")
        lines.append("- A monotone decrease of rho_VM with alpha along any fixed-eps row is the K-branch prediction direction (alpha-mechanism injects M-content; the V share shrinks).")
    lines.append("")

    out_path = out_dir / "label_smoothing_substitution_VM_audit_lambda.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"# wrote {out_path}")


if __name__ == "__main__":
    main()
