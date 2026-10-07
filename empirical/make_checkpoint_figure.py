#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure 2 for FaithfulnessObstruction.md §5.4: V/M separation gap across 4
checkpoints (base + Instruct for two families), with bootstrap 95% CIs and the
zero line. Visualizes the Llama-Instruct break (parity collapse).
Run with `py -3.13`.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
REP = ROOT / "empirical" / "reports"
FIG = REP / "figures"; FIG.mkdir(parents=True, exist_ok=True)

ORDER = ["llama31_8b", "llama31_8b_instruct", "mistral7b_v0_3", "mistral7b_v0_3_instruct"]
LABEL = {"llama31_8b": "Llama-3.1-8B\n(base)", "llama31_8b_instruct": "Llama-3.1-8B\nInstruct",
         "mistral7b_v0_3": "Mistral-7B-v0.3\n(base)", "mistral7b_v0_3_instruct": "Mistral-7B\nInstruct-v0.3"}
COL = {"llama31_8b": "#1f77b4", "llama31_8b_instruct": "#1f77b4",
       "mistral7b_v0_3": "#d62728", "mistral7b_v0_3_instruct": "#d62728"}


def main():
    d = json.loads((REP / "vm_bootstrap_significance.json").read_text())
    tags = [t for t in ORDER if t in d["models"]]
    gaps = [d["models"][t]["gap_min_V_minus_max_M"]["point"] for t in tags]
    cis = [d["models"][t]["gap_min_V_minus_max_M"]["ci95"] for t in tags]
    pgt = [d["models"][t]["gap_min_V_minus_max_M"]["P_gap_gt_0"] for t in tags]

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    x = np.arange(len(tags))
    for i, t in enumerate(tags):
        lo, hi = cis[i]
        ax.errorbar(x[i], gaps[i], yerr=[[gaps[i] - lo], [hi - gaps[i]]], fmt="o", ms=9,
                    color=COL[t], capsize=4, lw=1.6,
                    markerfacecolor=("white" if "instruct" in t else COL[t]),
                    markeredgecolor=COL[t], markeredgewidth=1.8)
        ax.annotate(f"P(>0)={pgt[i]:.3f}", (x[i], hi), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=8)
    ax.axhline(0, color="k", lw=1, ls="--", alpha=0.7)
    ax.text(len(tags) - 0.5, 0.02, "K-branch threshold", ha="right", va="bottom", fontsize=8, color="#444")
    ax.set_xticks(x)
    ax.set_xticklabels([LABEL[t] for t in tags], fontsize=8.5)
    ax.set_ylabel("V/M separation gap  $\\min(\\sigma_V)-\\max(\\sigma_M)$")
    ax.set_title("Figure 2. V/M separation across checkpoints: robust except under Llama instruct-tuning",
                 fontsize=9.5)
    ax.grid(alpha=0.25, axis="y")
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="o", color="gray", markerfacecolor="gray", ls="", label="base", ms=8),
                       Line2D([0], [0], marker="o", color="gray", markerfacecolor="white", ls="", label="instruct", ms=8)],
              loc="upper right", fontsize=8.5, framealpha=0.95)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"vm_checkpoint_gap.{ext}", dpi=160, bbox_inches="tight")
    print(f"# wrote {FIG / 'vm_checkpoint_gap.pdf'} (+ .png)")


if __name__ == "__main__":
    main()
