#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cross-model spectroscopy figure for FaithfulnessObstruction.md §5.
Panel A: f_{12,ell} vs depth ell/L (Llama + Mistral), anchors + crystallization jump.
Panel B: sigma_d V/M saturation index with 2000-bootstrap 95% CIs, both models.

Run with `py` (3.13 has matplotlib); `python` (3.12) does not.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parents[1]
REP = ROOT / "empirical" / "reports"
FIG = REP / "figures"
FIG.mkdir(parents=True, exist_ok=True)

MODELS = {"llama31_8b": ("Llama-3.1-8B", "#1f77b4"), "mistral7b_v0_3": ("Mistral-7B-v0.3", "#d62728")}
V_PACKETS, M_PACKETS = [2, 3, 4], [6, 12]


def f12_curve(tag):
    r = json.loads((REP / f"layerwise_packet_spectroscopy_months_{tag}.json").read_text())
    L = r["n_layers"]
    return np.array([r["f_d_layerwise"][str(e)]["12"] for e in range(L)]), L


def main():
    boot = json.loads((REP / "vm_bootstrap_significance.json").read_text())
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11, 4.2))

    # ---- Panel A: f12 vs depth ----
    for tag, (pretty, col) in MODELS.items():
        f12, L = f12_curve(tag)
        x = np.arange(L) / (L - 1)
        axA.plot(x, f12, "-o", ms=3, lw=1.6, color=col, label=pretty)
        axA.plot(x[-1], f12[-1], "*", ms=14, color=col, mec="k", mew=0.5, zorder=5)
        if tag == "llama31_8b":  # causalab "L28" = row 29 lens anchor
            axA.annotate("lens 0.638\n(causalab L28 = row 29)", xy=(29 / (L - 1), f12[29]),
                         xytext=(0.42, 0.30), fontsize=7.5,
                         arrowprops=dict(arrowstyle="->", lw=0.7))
            axA.annotate("probe 0.356\n(same layer)", xy=(29 / (L - 1), 0.356),
                         xytext=(0.55, 0.12), fontsize=7.5, color="#555",
                         arrowprops=dict(arrowstyle="->", lw=0.7, color="#555"))
            axA.plot(29 / (L - 1), 0.356, "s", ms=6, color="#888", mec="k", mew=0.4, zorder=5)
    axA.set_xlabel("normalized depth  $\\ell / L$")
    axA.set_ylabel("$f_{12,\\ell}$  (full-period packet fraction)")
    axA.set_title("(A) Full-period concept vs depth: jump, overshoot, decline", fontsize=10)
    axA.set_ylim(0, 0.92)
    axA.legend(loc="lower right", fontsize=8.5, framealpha=0.95)
    axA.grid(alpha=0.25)
    axA.text(0.02, 0.86, "★ final-layer anchor (≤5e-4)", transform=axA.transAxes, fontsize=7.5)

    # ---- Panel B: sigma_d with bootstrap CIs ----
    packets = [2, 3, 4, 6, 12]
    xpos = np.arange(len(packets))
    width = 0.36
    for i, (tag, (pretty, col)) in enumerate(MODELS.items()):
        pp = boot["models"][tag]["per_packet"]
        means = np.array([pp[str(d)]["boot_mean"] for d in packets])
        los = np.array([pp[str(d)]["ci95"][0] for d in packets])
        his = np.array([pp[str(d)]["ci95"][1] for d in packets])
        off = (i - 0.5) * width
        axB.errorbar(xpos + off, means, yerr=[means - los, his - means], fmt="o",
                     color=col, ms=6, capsize=3, lw=1.3, label=pretty)
    axB.axvspan(-0.5, 2.5, color="#2ca02c", alpha=0.07)
    axB.axvspan(2.5, 4.5, color="#9467bd", alpha=0.07)
    axB.text(1.0, 0.66, "V (single-prime / prime-power)", ha="center", fontsize=8.5, color="#2ca02c")
    axB.text(3.5, 0.66, "M (cross-prime carry)", ha="center", fontsize=8.5, color="#9467bd")
    axB.set_xticks(xpos)
    axB.set_xticklabels([f"$H_{{{d}}}$" for d in packets])
    axB.set_ylabel("$\\sigma_d$  (depth-normalized saturation)")
    axB.set_title("(B) V/M separation: every $\\sigma_V>\\sigma_M$, $P=1.000$ (2000 boot.)", fontsize=10)
    axB.legend(loc="upper right", fontsize=8.5, framealpha=0.95)
    axB.grid(alpha=0.25, axis="y")
    axB.set_xlim(-0.5, 4.5)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"spectroscopy_cross_model.{ext}", dpi=160, bbox_inches="tight")
    print(f"# wrote {FIG / 'spectroscopy_cross_model.pdf'} (+ .png)")


if __name__ == "__main__":
    main()
