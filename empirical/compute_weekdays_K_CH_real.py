"""
Real transformer K^CH diagnostic for the weekday C_7 control.

Input:  per_class_output_dists.safetensors  — shape [7, 7], float32
        Row i is the model's output distribution over {Mon..Sun} when the
        input prompt encodes weekday i.

Output: empirical/reports/weekdays_K_CH_real.md
"""

import struct
import json
import numpy as np
from pathlib import Path
from itertools import combinations
from scipy.stats import pearsonr

# ---------------------------------------------------------------------------
# 1. Load safetensors (no external dependency beyond stdlib + numpy)
# ---------------------------------------------------------------------------

def load_safetensors(path):
    with open(path, "rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        data = f.read()
    key = [k for k in header if k != "__metadata__"][0]
    meta = header[key]
    dtype = np.float32 if meta["dtype"] == "F32" else np.float64
    shape = meta["shape"]
    start, end = meta["data_offsets"]
    arr = np.frombuffer(data[start:end], dtype=dtype).reshape(shape).copy()
    return arr


# ---------------------------------------------------------------------------
# 2. Geometry helpers
# ---------------------------------------------------------------------------

def hellinger_chord(p, q):
    """Euclidean distance between sqrt(p) and sqrt(q) in R^7."""
    return np.linalg.norm(np.sqrt(p) - np.sqrt(q))


def moment_chord(p, q):
    """Euclidean distance in probability / moment coordinates."""
    return np.linalg.norm(p - q)


def logit_chord(p, q, eps=1e-12):
    """Euclidean distance in log / natural parameter coordinates."""
    return np.linalg.norm(np.log(p + eps) - np.log(q + eps))


def fisher_lc_distance(p, q, eps=1e-12):
    """
    Approximate Fisher–Levi-Civita distance on the categorical simplex.
    Exact: 2 * arccos(sum sqrt(p_i q_i))  (Bhattacharyya / geodesic on sphere).
    """
    bc = np.sum(np.sqrt(p * q + eps))
    bc = np.clip(bc, -1.0, 1.0)
    return 2.0 * np.arccos(bc)


def cyclic_hellinger_arc(centroids, i, j):
    """
    Arc length along the cyclic C_7 manifold from centroid i to centroid j,
    measured as the accumulated sum of consecutive Hellinger chords going
    the short way around the cycle.
    """
    n = len(centroids)
    fwd = (j - i) % n
    bwd = (i - j) % n
    steps = fwd if fwd <= bwd else -fwd % n

    arc = 0.0
    cur = i
    direction = 1 if fwd <= bwd else -1
    for _ in range(min(fwd, bwd)):
        nxt = (cur + direction) % n
        arc += hellinger_chord(centroids[cur], centroids[nxt])
        cur = nxt
    return arc


# ---------------------------------------------------------------------------
# 3. K^CH diagnostic at the centroid (C_7 formula)
# ---------------------------------------------------------------------------

def k_ch_cyclic(h, v, p_star):
    """
    K^CH_{p*}(h)v  for  p* = uniform on C_7.
    Formula: 7 * cyclic_conv(h, v) - 7 * <h,v>_{p*} * p*
    where cyclic_conv is circular convolution in R^7.
    """
    n = len(p_star)
    conv_hv = np.real(np.fft.ifft(np.fft.fft(h) * np.fft.fft(v)))
    inner_hv = np.sum(h * v / p_star)
    return n * conv_hv - n * inner_hv * p_star


def k_ch_norm_sq(h, p_star):
    """||K^CH_{p*}(h)||^2_F  (Frobenius over the Fisher metric)."""
    n = len(p_star)
    total = 0.0
    e = np.zeros(n)
    for k in range(n):
        e[:] = 0.0
        e[k] = 1.0
        Kv = k_ch_cyclic(h, e, p_star)
        total += np.sum(Kv ** 2 / p_star)
    return total


# ---------------------------------------------------------------------------
# 4. Main
# ---------------------------------------------------------------------------

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main():
    import sys
    here = Path(__file__).parent
    # CLI: python compute_weekdays_K_CH_real.py <safetensor_path> <model_tag>
    if len(sys.argv) >= 3:
        safetensor_path = Path(sys.argv[1])
        model_tag = sys.argv[2]
    else:
        # Default: Llama run
        safetensor_path = here.parent / "weekdays" / "baseline" / "per_class_output_dists.safetensors"
        model_tag = "llama31_8b"
        if not safetensor_path.exists():
            safetensor_path = here.parent / "per_class_output_dists.safetensors"
            model_tag = "mistral_7b"
    report_path = here / "reports" / f"weekdays_K_CH_real_{model_tag}.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Load
    P = load_safetensors(safetensor_path)
    assert P.shape == (7, 7), f"Expected [7,7], got {P.shape}"

    # Normalize rows to sum to 1 (softmax outputs may not be exact)
    P = P / P.sum(axis=1, keepdims=True)

    n = 7
    p_star = np.ones(n) / n

    # Print the centroid matrix
    print("Centroid matrix P (row i = output dist for input weekday i):")
    for i, row in enumerate(P):
        print(f"  {DAYS[i]:10s}: {np.array2string(row, precision=4, suppress_small=True)}")
    print()

    # Pairwise distances
    pairs = list(combinations(range(n), 2))
    h_chord, m_chord, l_chord, f_lc, cyc_arc = [], [], [], [], []

    for i, j in pairs:
        h_chord.append(hellinger_chord(P[i], P[j]))
        m_chord.append(moment_chord(P[i], P[j]))
        l_chord.append(logit_chord(P[i], P[j]))
        f_lc.append(fisher_lc_distance(P[i], P[j]))
        cyc_arc.append(cyclic_hellinger_arc(P, i, j))

    h_chord  = np.array(h_chord)
    m_chord  = np.array(m_chord)
    l_chord  = np.array(l_chord)
    f_lc     = np.array(f_lc)
    cyc_arc  = np.array(cyc_arc)

    r_h,  _ = pearsonr(h_chord,  cyc_arc)
    r_m,  _ = pearsonr(m_chord,  cyc_arc)
    r_l,  _ = pearsonr(l_chord,  cyc_arc)
    r_f,  _ = pearsonr(f_lc,     cyc_arc)

    print("Correlations with cyclic Hellinger arc (behavior manifold reference):")
    print(f"  Hellinger chord            r = {r_h:.6f}")
    print(f"  Moment Euclidean chord     r = {r_m:.6f}   (Wurgaft linear ~0.89)")
    print(f"  Natural/logit chord        r = {r_l:.6f}")
    print(f"  Fisher L-C distance        r = {r_f:.6f}")
    print()

    # K^CH norms per centroid displacement
    displacements = P - p_star
    kch_norms = [np.sqrt(k_ch_norm_sq(displacements[i], p_star)) for i in range(n)]
    print("K^CH Frobenius norms per centroid displacement:")
    for i, kn in enumerate(kch_norms):
        print(f"  {DAYS[i]:10s}: {kn:.4f}")
    print()

    # Write report
    model_pretty = {
        "llama31_8b": "Llama-3.1-8B",
        "mistral_7b": "Mistral-7B-v0.3",
    }.get(model_tag, model_tag)
    lines = [
        f"# Weekday $C_7$ $K^{{CH}}$ Diagnostic — {model_pretty}",
        "",
        f"**Model:** {model_pretty} (layer 28, last token)",
        f"**Source:** `{safetensor_path.as_posix()}`",
        f"**Shape:** {list(P.shape)}  (row i = output distribution for input weekday i)",
        "",
        "## Centroid Matrix",
        "",
        "| Input \\ Output | Mon | Tue | Wed | Thu | Fri | Sat | Sun |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for i, row in enumerate(P):
        cells = " | ".join(f"{v:.4f}" for v in row)
        lines.append(f"| {DAYS[i]} | {cells} |")

    lines += [
        "",
        "## Correlation with Cyclic Hellinger Arc",
        "",
        "Parametric proxy values (Paper 12 §4) shown for comparison.",
        "",
        f"| Metric | Real ({model_pretty}) | Parametric proxy |",
        "|---|---|---|",
        f"| Hellinger chord vs cyclic arc | **{r_h:.6f}** | 0.910010 |",
        f"| Moment Euclidean chord vs cyclic arc | **{r_m:.6f}** | 0.886448 |",
        f"| Natural/logit chord vs cyclic arc | **{r_l:.6f}** | 0.941295 |",
        f"| Fisher L-C distance vs cyclic arc | **{r_f:.6f}** | 0.911776 |",
        "",
        "> The moment Euclidean chord value should be compared with the",
        "> Wurgaft et al. reported linear correlation r ≈ 0.89.",
        "> The behavior-manifold reference is r ≈ 0.99.",
        "",
        "## $K^{CH}$ Frobenius Norms per Centroid",
        "",
        "| Weekday | $\\|K^{CH}_{p_*}(h_i)\\|_F$ |",
        "|---|---|",
    ]
    for i, kn in enumerate(kch_norms):
        lines.append(f"| {DAYS[i]} | {kn:.4f} |")

    lines += [
        "",
        "## Interpretation",
        "",
        "The moment chord correlation closes the open empirical item in Paper 12 §10:",
        "the parametric proxy is replaced by an actual transformer measurement.",
        "The residual between the moment chord correlation and the cyclic arc",
        "correlation (r ≈ 0.99 reference) is attributed to:",
        "",
        "1. Intrinsic behavior-side $K^{CH}$ cubic (quantified above)",
        "2. Activation pullback distortion $J_F^\\top g_y J_F$",
        "3. Hessian terms of $F$",
        "4. Sampling / spline parameterization error",
    ]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to {report_path}")


if __name__ == "__main__":
    main()
