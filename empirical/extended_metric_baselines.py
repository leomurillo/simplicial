"""
Extended metric baselines for the §4.1 / §5.1 correlation tables.

Addresses the "moment-Euclidean strawman" reviewer critique: the existing
§4.1 table shows that moment-Euclidean correlation drops sharply while
Hellinger / logit / Fisher-LC hold near proxy. The reviewer correctly
observes that this only re-establishes the textbook information-geometry
finding that Euclidean is wrong on the simplex.

This script adds non-cubic baselines that respect categorical structure
along different axes:

  * Total variation (L^1 in p) — categorical-native but linear in (p-q)
  * Jensen-Shannon distance (Fisher-equivalent, quadratic in p)
  * Symmetric KL (Fisher-equivalent, quadratic, sensitive to ratios)
  * Bhattacharyya distance (Fisher-equivalent, ~ Hellinger)
  * Wasserstein-1 with cyclic ground metric on Z/N (cyclic-aware, non-Fisher)

All eight metrics are reported against the cyclic Hellinger arc reference,
together with the existing four. Output is a unified Markdown table.

Inputs: same per_class_output_dists.safetensors files used by
compute_weekdays_K_CH_real.py and compute_months_K_CH_real.py.

Design rationale: see Note_metric_baselines_design.md.
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr


# ---------------------------------------------------------------------------
# 1. Safetensors loader
# ---------------------------------------------------------------------------

def load_safetensors(path: Path) -> np.ndarray:
    with open(path, "rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        data = f.read()
    key = next(k for k in header if k != "__metadata__")
    meta = header[key]
    dtype = np.float32 if meta["dtype"] == "F32" else np.float64
    shape = meta["shape"]
    start, end = meta["data_offsets"]
    return np.frombuffer(data[start:end], dtype=dtype).reshape(shape).copy()


# ---------------------------------------------------------------------------
# 2. Metric definitions
# ---------------------------------------------------------------------------

EPS = 1e-12


def hellinger_chord(p, q):
    return float(np.linalg.norm(np.sqrt(p) - np.sqrt(q)))


def moment_chord(p, q):
    return float(np.linalg.norm(p - q))


def logit_chord(p, q):
    return float(np.linalg.norm(np.log(p + EPS) - np.log(q + EPS)))


def fisher_lc_distance(p, q):
    """2 * arccos(Bhattacharyya coefficient): geodesic on the sphere of sqrt(p)."""
    bc = float(np.sum(np.sqrt(p * q + EPS)))
    bc = np.clip(bc, -1.0, 1.0)
    return float(2.0 * np.arccos(bc))


def total_variation(p, q):
    """TV(p, q) = 0.5 * ||p - q||_1. Probability-native, linear in (p-q)."""
    return float(0.5 * np.sum(np.abs(p - q)))


def symmetric_kl(p, q):
    """sqrt(KL(p||q) + KL(q||p)). Fisher-equivalent infinitesimally."""
    p_safe = np.maximum(p, EPS)
    q_safe = np.maximum(q, EPS)
    kl_pq = np.sum(p_safe * (np.log(p_safe) - np.log(q_safe)))
    kl_qp = np.sum(q_safe * (np.log(q_safe) - np.log(p_safe)))
    return float(np.sqrt(max(kl_pq + kl_qp, 0.0)))


def jensen_shannon_distance(p, q):
    """sqrt(JSD(p, q)) — a proper metric, Fisher-equivalent at small distance."""
    m = 0.5 * (p + q)
    p_safe = np.maximum(p, EPS)
    q_safe = np.maximum(q, EPS)
    m_safe = np.maximum(m, EPS)
    kl_pm = np.sum(p_safe * (np.log(p_safe) - np.log(m_safe)))
    kl_qm = np.sum(q_safe * (np.log(q_safe) - np.log(m_safe)))
    jsd = 0.5 * (kl_pm + kl_qm)
    return float(np.sqrt(max(jsd, 0.0)))


def bhattacharyya_distance(p, q):
    """-log(sum sqrt(p_i q_i)). Related to Hellinger by BC = 1 - H^2/2."""
    bc = float(np.sum(np.sqrt(p * q + EPS)))
    bc = max(bc, EPS)
    return float(-np.log(bc))


def wasserstein_1_cyclic(p, q):
    """
    1-Wasserstein distance on Z/N with unit cyclic ground metric.

    Closed form (Werman et al.): let F_i = cumsum(p - q)[i] for i = 0..N-1.
    Then W1_cyc(p, q) = sum_i |F_i - median(F_0, ..., F_{N-1})|.

    This baseline is uniquely "cyclic-aware" among the metrics tested
    while not being Fisher-equivalent.
    """
    n = len(p)
    F = np.cumsum(p - q)[:n]  # F_N = 0 since totals match
    med = float(np.median(F))
    return float(np.sum(np.abs(F - med)))


METRICS = {
    # name                       : (function, category, fisher_equiv, cyclic_aware)
    "Moment Euclidean":           (moment_chord,            "linear-L2",     False, False),
    "Total variation":            (total_variation,         "linear-L1",     False, False),
    "Hellinger chord":            (hellinger_chord,         "quad-Fisher",   True,  False),
    "Jensen-Shannon distance":    (jensen_shannon_distance, "quad-Fisher",   True,  False),
    "Symmetric KL":               (symmetric_kl,            "quad-Fisher",   True,  False),
    "Bhattacharyya":              (bhattacharyya_distance,  "quad-Fisher",   True,  False),
    "Fisher Levi-Civita":         (fisher_lc_distance,      "quad-Fisher",   True,  False),
    "Natural/logit chord":        (logit_chord,             "quad-natural",  False, False),
    "Wasserstein-1 cyclic":       (wasserstein_1_cyclic,    "OT-cyclic",     False, True),
}


# ---------------------------------------------------------------------------
# 3. Cyclic Hellinger arc reference
# ---------------------------------------------------------------------------

def cyclic_hellinger_arc(centroids, i, j):
    n = len(centroids)
    fwd = (j - i) % n
    bwd = (i - j) % n
    if fwd <= bwd:
        path_len = fwd
        direction = 1
    else:
        path_len = bwd
        direction = -1
    arc = 0.0
    cur = i
    for _ in range(path_len):
        nxt = (cur + direction) % n
        arc += hellinger_chord(centroids[cur], centroids[nxt])
        cur = nxt
    return arc


# ---------------------------------------------------------------------------
# 4. Symmetric parametric proxy
#
# Reproduce the §4.1 / §5.1 symmetric proxy values so that the report can
# show real-vs-proxy drops with all baselines on the same footing.
#
# The proxy is the cyclic-confidence-matrix family used in Paper 12 §4:
#   p_i[j] = softmax over Hamming-style cyclic distance from i to j with
#   inverse-temperature beta.
# ---------------------------------------------------------------------------

def cyclic_proxy_centroids(n: int, beta: float = 2.5) -> np.ndarray:
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            d = min((i - j) % n, (j - i) % n)
            P[i, j] = np.exp(-beta * d * d)
        P[i] /= P[i].sum()
    return P


# ---------------------------------------------------------------------------
# 5. Driver
# ---------------------------------------------------------------------------

def compute_all_metrics(centroids: np.ndarray) -> tuple[dict, np.ndarray]:
    """Returns (metric_name -> array of pair distances, cyclic-arc reference)."""
    n = centroids.shape[0]
    pairs = list(combinations(range(n), 2))
    out: dict[str, np.ndarray] = {}
    for name, (fn, *_unused) in METRICS.items():
        out[name] = np.array([fn(centroids[i], centroids[j]) for i, j in pairs])
    arc = np.array([cyclic_hellinger_arc(centroids, i, j) for i, j in pairs])
    return out, arc


def correlations_against_arc(metric_arrays: dict, arc: np.ndarray) -> dict:
    out = {}
    for name, vals in metric_arrays.items():
        if np.std(vals) < 1e-12 or np.std(arc) < 1e-12:
            r, p = float("nan"), float("nan")
        else:
            r, p = pearsonr(vals, arc)
        out[name] = (float(r), float(p))
    return out


def bootstrap_ci(metric_vals: np.ndarray, arc: np.ndarray,
                 n_boot: int = 2000, rng: np.random.Generator | None = None
                 ) -> tuple[float, float]:
    """95% bootstrap CI on Pearson r over pair indices."""
    if rng is None:
        rng = np.random.default_rng(0)
    n = len(metric_vals)
    rs = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        x = metric_vals[idx]
        y = arc[idx]
        if np.std(x) < 1e-12 or np.std(y) < 1e-12:
            rs[b] = float("nan")
        else:
            rs[b], _ = pearsonr(x, y)
    rs = rs[~np.isnan(rs)]
    if len(rs) == 0:
        return float("nan"), float("nan")
    return float(np.percentile(rs, 2.5)), float(np.percentile(rs, 97.5))


def classify_drop(delta: float) -> str:
    a = abs(delta)
    if a < 0.03:
        return "holds"
    if a < 0.15:
        return "drops mildly"
    return "drops sharply"


def make_report(task: str, model: str, centroid: np.ndarray,
                proxy_corrs: dict, real_corrs: dict, real_ci: dict,
                kch_norms: np.ndarray | None) -> str:
    n = len(centroid)
    lines: list[str] = []
    lines.append(f"# Extended metric baselines — {task}, {model}")
    lines.append("")
    lines.append(f"**Centroid shape:** {n} x {n}")
    lines.append("")
    lines.append("Each metric is computed pairwise across the N centroids; the")
    lines.append("Pearson correlation is taken against the cyclic Hellinger arc")
    lines.append("reference (the canonical behavior-manifold-aware geodesic).")
    lines.append("")
    lines.append("The 'proxy' column uses the symmetric cyclic-confidence")
    lines.append("centroid family of Paper 12 §4 at beta=2.5; it is the parametric")
    lines.append("calibration reference, not an empirical measurement.")
    lines.append("")
    lines.append("Δ = real − proxy. Classification:")
    lines.append("- |Δ| < 0.03: **holds**")
    lines.append("- 0.03 ≤ |Δ| < 0.15: **drops mildly**")
    lines.append("- |Δ| ≥ 0.15: **drops sharply**")
    lines.append("")
    lines.append("| Metric | Category | Fisher-equiv | Cyclic-aware | Proxy r | Real r | 95% CI | Δ | Class |")
    lines.append("|---|---|---|---|---:|---:|---|---:|---|")
    for name, (_, cat, fe, cy) in METRICS.items():
        pr, _ = proxy_corrs[name]
        rr, _ = real_corrs[name]
        lo, hi = real_ci[name]
        d = rr - pr
        lines.append(
            f"| {name} | {cat} | "
            f"{'yes' if fe else 'no'} | "
            f"{'yes' if cy else 'no'} | "
            f"{pr:.4f} | **{rr:.4f}** | "
            f"[{lo:.3f}, {hi:.3f}] | "
            f"{d:+.3f} | {classify_drop(d)} |"
        )
    lines.append("")
    lines.append("## Drop-pattern summary")
    lines.append("")
    drops = {name: real_corrs[name][0] - proxy_corrs[name][0] for name in METRICS}
    moment_d = drops["Moment Euclidean"]
    tv_d = drops["Total variation"]
    helli_d = drops["Hellinger chord"]
    fisher_eq_drops = [drops[name] for name, (_, _, fe, _) in METRICS.items() if fe]
    fisher_eq_max = max(abs(d) for d in fisher_eq_drops) if fisher_eq_drops else 0.0
    lines.append(f"- Moment Euclidean Δ = {moment_d:+.4f} ({classify_drop(moment_d)})")
    lines.append(f"- Total variation Δ = {tv_d:+.4f} ({classify_drop(tv_d)})")
    lines.append(f"- Max |Δ| across Fisher-equivalent metrics = {fisher_eq_max:.4f}")
    lines.append(f"- Hellinger chord Δ = {helli_d:+.4f}")
    lines.append(f"- Wasserstein-1 cyclic Δ = "
                 f"{drops['Wasserstein-1 cyclic']:+.4f}")
    lines.append("")
    lines.append("**Reading (see Note_metric_baselines_design.md §3):**")
    if abs(moment_d) >= 0.15 and abs(tv_d) >= 0.15 and fisher_eq_max < 0.05:
        lines.append("- *Both linear-in-p metrics drop sharply while all Fisher-equivalent")
        lines.append("  metrics hold.* This matches the reviewer's 'Euclidean strawman'")
        lines.append("  framing. The moment drop reflects the standard categorical-Euclidean")
        lines.append("  inadequacy; it is not a cubic-specific signature on its own.")
        lines.append("  The cubic-specific evidence rests on the CRT conductor energy")
        lines.append("  decomposition in §5.1 and the operator-valued conductor structure,")
        lines.append("  not on this chord correlation.")
    elif abs(moment_d) >= 0.15 and abs(tv_d) < 0.05:
        lines.append("- *Only moment Euclidean drops; Total variation holds.* The drop is")
        lines.append("  specifically L^2-quadratic in p. Worth investigating but the")
        lines.append("  result still does not isolate a cubic-specific signature.")
    elif fisher_eq_max >= 0.15:
        lines.append("- *Some Fisher-equivalent metric drops by ≥0.15.* Heterogeneous")
        lines.append("  Fisher-equivalent metric behavior at the chord level is unusual;")
        lines.append("  identify which metric drops and test whether the per-pair residual")
        lines.append("  correlates with the K^CH(h_i) Frobenius norm.")
    else:
        lines.append("- *Mixed or mild pattern.* Inspect the table; report row-by-row.")
    lines.append("")
    lines.append("## Centroid matrix")
    lines.append("")
    head = " | ".join(str(k) for k in range(n))
    lines.append(f"| | {head} |")
    lines.append("|---|" + "|".join(["---"] * n) + "|")
    for i in range(n):
        row = " | ".join(f"{x:.4f}" for x in centroid[i])
        lines.append(f"| {i} | {row} |")
    lines.append("")
    if kch_norms is not None:
        lines.append("## K^CH Frobenius norms per row")
        lines.append("")
        for i, v in enumerate(kch_norms):
            lines.append(f"- row {i}: {v:.4f}")
        lines.append("")
    return "\n".join(lines)


def k_ch_cyclic_op(h, v, p_star):
    n = len(p_star)
    conv = np.real(np.fft.ifft(np.fft.fft(h) * np.fft.fft(v)))
    inner = np.sum(h * v / p_star)
    return n * conv - n * inner * p_star


def k_ch_frob_norms(centroids: np.ndarray) -> np.ndarray:
    n = centroids.shape[0]
    p_star = np.ones(n) / n
    norms = np.zeros(n)
    e = np.eye(n)
    for i in range(n):
        h = centroids[i] - p_star
        total = 0.0
        for k in range(n):
            Kv = k_ch_cyclic_op(h, e[k], p_star)
            total += float(np.sum(Kv ** 2 / p_star))
        norms[i] = np.sqrt(total)
    return norms


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--centroid", required=True, type=Path,
                   help="Path to per_class_output_dists.safetensors")
    p.add_argument("--task", required=True, choices=["weekdays", "months"])
    p.add_argument("--model", required=True,
                   help="Model name for the report header")
    p.add_argument("--proxy-beta", type=float, default=2.5,
                   help="Inverse temperature for the symmetric cyclic proxy")
    p.add_argument("--out", type=Path, default=None)
    p.add_argument("--bootstrap", type=int, default=2000,
                   help="Bootstrap iterations for the 95% CI on each Pearson r")
    args = p.parse_args()

    n_expected = 7 if args.task == "weekdays" else 12
    centroid = load_safetensors(args.centroid)
    if centroid.shape != (n_expected, n_expected):
        raise SystemExit(
            f"Centroid shape {centroid.shape} does not match task {args.task} "
            f"(expected {n_expected}x{n_expected})"
        )
    row_sums = centroid.sum(axis=1, keepdims=True)
    row_sums = np.where(row_sums < 1e-12, 1.0, row_sums)
    centroid = centroid / row_sums

    # Proxy correlations
    proxy_centroids = cyclic_proxy_centroids(n_expected, beta=args.proxy_beta)
    proxy_metrics, proxy_arc = compute_all_metrics(proxy_centroids)
    proxy_corrs = correlations_against_arc(proxy_metrics, proxy_arc)

    # Real correlations
    real_metrics, real_arc = compute_all_metrics(centroid)
    real_corrs = correlations_against_arc(real_metrics, real_arc)

    # Bootstrap CIs on real
    rng = np.random.default_rng(0)
    real_ci = {
        name: bootstrap_ci(vals, real_arc, n_boot=args.bootstrap, rng=rng)
        for name, vals in real_metrics.items()
    }

    # K^CH norms (informational; not used in correlation comparison)
    kch_norms = k_ch_frob_norms(centroid)

    report = make_report(args.task, args.model, centroid,
                         proxy_corrs, real_corrs, real_ci, kch_norms)

    if args.out:
        out_path = args.out
    else:
        out_dir = Path(__file__).parent / "reports"
        out_dir.mkdir(exist_ok=True)
        safe_model = args.model.lower().replace(" ", "_").replace(".", "_").replace("-", "_")
        out_path = out_dir / f"extended_baselines_{args.task}_{safe_model}.md"

    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote {out_path}")

    # Headline summary to stdout
    print()
    print(f"# Headline summary — {args.task}, {args.model}")
    print(f"{'Metric':28s} {'proxy r':>9s} {'real r':>9s} {'delta':>9s}  class")
    for name in METRICS:
        pr = proxy_corrs[name][0]
        rr = real_corrs[name][0]
        d = rr - pr
        try:
            print(f"{name:28s} {pr:9.4f} {rr:9.4f} {d:+9.4f}  {classify_drop(d)}")
        except UnicodeEncodeError:
            safe_name = name.encode("ascii", "replace").decode("ascii")
            print(f"{safe_name:28s} {pr:9.4f} {rr:9.4f} {d:+9.4f}  {classify_drop(d)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
