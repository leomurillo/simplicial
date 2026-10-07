"""
Activation Pullback Audit  (Paper 12 §7.2)
==========================================

For a learned map  F: A -> Delta_R°  decompose the linear-versus-manifold gap
observed in Paper 12 §4–§5 into:

    gap  =  behavior-side cubic  +  activation pullback distortion
                                  +  Hessian / parameterization residual

This script computes the *activation pullback distortion* component for the
saved causalab artifacts.

Inputs (per task):
  - subspace/.../features/raw_features.safetensors           [N, 4096]  BF16
  - baseline/per_class_output_dists.safetensors              [C, C]     F32
  - baseline/train_samples.json                              N samples
    (raw_output field gives result-class label for each sample)

Outputs:
  - activation centroid matrix A_c in R^{4096} for each class c
  - pairwise activation distances || A_i - A_j ||
  - pairwise output Hellinger distances  d_H( p_i, p_j )
  - correlation rho( activation distance, output Hellinger distance )
  - effective local pullback Lipschitz constant  L_F (slope)
  - variance-decomposition:  between-class / total  in activation space
  - report:  empirical/reports/activation_pullback_<task>_<model>.md
"""

import struct
import json
import sys
import numpy as np
from pathlib import Path
from itertools import combinations
from scipy.stats import pearsonr, linregress


def load_safetensors(path):
    with open(path, "rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        data = f.read()
    key = [k for k in header if k != "__metadata__"][0]
    meta = header[key]
    dtype_str = meta["dtype"]
    if dtype_str == "F32":
        dtype = np.float32
    elif dtype_str == "F64":
        dtype = np.float64
    elif dtype_str == "BF16":
        # bfloat16: read as uint16, shift to float32
        raw = np.frombuffer(data[meta["data_offsets"][0]:meta["data_offsets"][1]],
                            dtype=np.uint16).copy()
        out = np.zeros(raw.size, dtype=np.uint32)
        out |= raw.astype(np.uint32) << 16
        return out.view(np.float32).reshape(meta["shape"])
    else:
        raise ValueError(f"Unhandled dtype {dtype_str}")
    start, end = meta["data_offsets"]
    return np.frombuffer(data[start:end], dtype=dtype).reshape(meta["shape"]).copy()


def hellinger(p, q, eps=1e-12):
    return np.linalg.norm(np.sqrt(p + eps) - np.sqrt(q + eps))


def cyclic_hellinger_arc(centroids, i, j):
    n = len(centroids)
    fwd = (j - i) % n
    bwd = (i - j) % n
    direction = 1 if fwd <= bwd else -1
    arc = 0.0
    cur = i
    for _ in range(min(fwd, bwd)):
        nxt = (cur + direction) % n
        arc += hellinger(centroids[cur], centroids[nxt])
        cur = nxt
    return arc


def run_audit(task_dir: Path, class_names, model_pretty, report_path: Path):
    raw_path = task_dir / "subspace" / "pca_k64" / "result" / "features" / "raw_features.safetensors"
    centroid_path = task_dir / "baseline" / "per_class_output_dists.safetensors"
    samples_path = task_dir / "baseline" / "train_samples.json"

    A_raw = load_safetensors(str(raw_path))  # [N, 4096]
    P = load_safetensors(str(centroid_path))  # [C, C]
    P = P / P.sum(axis=1, keepdims=True)
    n_classes = len(class_names)
    assert P.shape == (n_classes, n_classes), f"Centroid shape mismatch: {P.shape}"

    with open(samples_path) as f:
        samples = json.load(f)["samples"]
    assert len(samples) == A_raw.shape[0], \
        f"samples={len(samples)} but activations={A_raw.shape[0]}"

    # Extract class labels for each sample from raw_output
    class_to_idx = {name.strip().lower(): i for i, name in enumerate(class_names)}
    sample_class = []
    for s in samples:
        out = s["raw_output"].strip().lower()
        if out not in class_to_idx:
            raise ValueError(f"Unknown output {out!r}; class_names = {class_names}")
        sample_class.append(class_to_idx[out])
    sample_class = np.array(sample_class)

    # ---- activation-space class centroids ----
    A_centroids = np.zeros((n_classes, A_raw.shape[1]), dtype=np.float32)
    for c in range(n_classes):
        mask = sample_class == c
        A_centroids[c] = A_raw[mask].mean(axis=0)
    samples_per_class = np.bincount(sample_class, minlength=n_classes)

    # ---- variance decomposition (activation space) ----
    overall_mean = A_raw.mean(axis=0)
    total_var = np.sum((A_raw - overall_mean) ** 2)
    between_var = sum(samples_per_class[c] * np.sum((A_centroids[c] - overall_mean) ** 2)
                      for c in range(n_classes))
    within_var = total_var - between_var
    between_frac = between_var / total_var
    within_frac = within_var / total_var

    # ---- pairwise comparisons ----
    pairs = list(combinations(range(n_classes), 2))
    act_dist, hell_dist, cyc_arc = [], [], []
    for i, j in pairs:
        act_dist.append(np.linalg.norm(A_centroids[i] - A_centroids[j]))
        hell_dist.append(hellinger(P[i], P[j]))
        cyc_arc.append(cyclic_hellinger_arc(P, i, j))
    act_dist = np.array(act_dist)
    hell_dist = np.array(hell_dist)
    cyc_arc = np.array(cyc_arc)

    # correlations
    r_act_hell, _ = pearsonr(act_dist, hell_dist)
    r_act_cyc, _ = pearsonr(act_dist, cyc_arc)

    # Lipschitz pullback slope:  hell ~ L_F * act
    slope_hell, _, _, _, _ = linregress(act_dist, hell_dist)
    slope_cyc, _, _, _, _ = linregress(act_dist, cyc_arc)

    # local pullback constants per pair  G_F^{ij} = (hell/act)^2
    g_f = (hell_dist / act_dist) ** 2
    g_f_mean = g_f.mean()
    g_f_std = g_f.std()
    g_f_cv = g_f_std / g_f_mean  # coefficient of variation; 0 = perfect isometry

    print(f"\n=== Activation Pullback Audit -- {model_pretty}, {task_dir.name} ===\n")
    print(f"Samples: {A_raw.shape[0]}   Classes: {n_classes}   Hidden dim: {A_raw.shape[1]}")
    print(f"Samples per class: {samples_per_class.tolist()}")
    print()
    print("Activation-space variance decomposition:")
    print(f"  Between-class fraction: {between_frac:.4f}")
    print(f"  Within-class fraction:  {within_frac:.4f}")
    print()
    print("Pairwise correlations:")
    print(f"  activation distance  vs  Hellinger output distance   r = {r_act_hell:.6f}")
    print(f"  activation distance  vs  cyclic Hellinger arc        r = {r_act_cyc:.6f}")
    print()
    print(f"Linear pullback slope (Hellinger ~ L_F * activation): {slope_hell:.6e}")
    print(f"Linear pullback slope (cyclic arc ~ L * activation):  {slope_cyc:.6e}")
    print()
    print(f"Per-pair G_F = (Hellinger / activation)^2 ")
    print(f"  mean = {g_f_mean:.4e}   std = {g_f_std:.4e}   CV = {g_f_cv:.4f}")
    print(f"  (CV -> 0 means F is locally isometric on this centroid set)")
    print()

    # ---- write report ----
    lines = [
        f"# Activation Pullback Audit -- {model_pretty}, `{task_dir.name}`",
        "",
        f"**Model:** {model_pretty} (layer 28, last token)",
        f"**Samples:** {A_raw.shape[0]} prompts grouped into {n_classes} result classes",
        f"**Hidden dim:** {A_raw.shape[1]}",
        f"**Source:** `{raw_path.as_posix()}`",
        "",
        "## Variance Decomposition in Activation Space",
        "",
        "Partition the total \\(L^2\\) variance of the saved activations across",
        "the result-class label.  Between-class variance is the part captured",
        "by the centroid representation \\(A_c\\); within-class variance is the",
        "irreducible noise visible to the K^CH centroid analysis.",
        "",
        f"| component | fraction of total |",
        f"|---|---|",
        f"| between-class | **{between_frac:.4f}** |",
        f"| within-class  | {within_frac:.4f} |",
        "",
        "## Pairwise Activation vs. Behavior Distances",
        "",
        f"There are \\({n_classes*(n_classes-1)//2}\\) inter-class pairs.  For each pair we compute",
        "the ambient activation-space distance and the output-space",
        "Hellinger distance.",
        "",
        f"| comparison | Pearson \\(r\\) |",
        f"|---|---|",
        f"| activation distance vs Hellinger chord | **{r_act_hell:.6f}** |",
        f"| activation distance vs cyclic Hellinger arc | **{r_act_cyc:.6f}** |",
        "",
        "## Effective Pullback Lipschitz",
        "",
        "Linear regression of behavior distance on activation distance gives",
        "the effective Lipschitz constant \\(L_F\\) for the activation->output",
        "map at this scale.",
        "",
        f"| regression | slope |",
        f"|---|---|",
        f"| Hellinger chord ~ \\(L_F\\) · activation distance | {slope_hell:.6e} |",
        f"| cyclic arc ~ \\(L\\) · activation distance | {slope_cyc:.6e} |",
        "",
        "## Local Pullback Metric Variation",
        "",
        "Per-pair pullback metric \\(G_F^{ij} = (d_H(p_i,p_j) / \\|A_i - A_j\\|)^2\\)",
        "summarises how the Fisher-Hellinger metric pulls back to activation",
        "space at the class-centroid scale.",
        "",
        f"| statistic | value |",
        f"|---|---|",
        f"| mean | {g_f_mean:.4e} |",
        f"| std  | {g_f_std:.4e} |",
        f"| coefficient of variation | **{g_f_cv:.4f}** |",
        "",
        "A coefficient of variation near zero indicates that the map \\(F\\)",
        "behaves as a (rescaled) local isometry on this centroid set: the",
        "*activation-pullback distortion residual* of Paper 12 §7.2 is small,",
        "and the linear-vs-manifold gap measured in §4–§5 is attributable",
        "primarily to the intrinsic behavior-side cubic.",
        "A large coefficient of variation means the activation embedding",
        "stretches and compresses pairs at different rates -- the activation",
        "pullback carries part of the gap and the K^CH cubic carries the rest.",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to {report_path}")

    return dict(
        between_frac=between_frac, within_frac=within_frac,
        r_act_hell=r_act_hell, r_act_cyc=r_act_cyc,
        slope_hell=slope_hell, slope_cyc=slope_cyc,
        g_f_mean=g_f_mean, g_f_std=g_f_std, g_f_cv=g_f_cv,
    )


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    MONTHS = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    run_audit(root / "weekdays", WEEKDAYS, "Llama-3.1-8B",
              reports_dir / "activation_pullback_weekdays_llama31_8b.md")

    run_audit(root / "months", MONTHS, "Llama-3.1-8B",
              reports_dir / "activation_pullback_months_llama31_8b.md")
