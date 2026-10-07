"""
Smoke test for bigram_corpus_control.py.

Three synthetic scenarios test that the script correctly distinguishes:

  A. Corpus and centroid asymmetries AGREE     -> asymm Pearson r near +1
  B. Corpus and centroid asymmetries OPPOSITE -> asymm Pearson r near -1
  C. Corpus has NO asymmetry (uniform corpus)  -> asymm Pearson r near 0

This is a sanity check on the analysis machinery, not a science test.
"""

import tempfile
import struct
import json
import subprocess
import sys
from pathlib import Path
import numpy as np


def write_safetensors(path: Path, arr: np.ndarray, name: str = "centroid"):
    arr = np.ascontiguousarray(arr.astype(np.float32))
    header = {name: {"dtype": "F32", "shape": list(arr.shape),
                     "data_offsets": [0, arr.nbytes]}}
    hdr = json.dumps(header).encode("utf-8")
    with open(path, "wb") as f:
        f.write(struct.pack("<Q", len(hdr)))
        f.write(hdr)
        f.write(arr.tobytes())


def predecessor_bias_centroid(N: int) -> np.ndarray:
    M = np.full((N, N), 0.05 / max(N - 3, 1))
    np.fill_diagonal(M, 0.6)
    for i in range(N):
        M[i, (i - 1) % N] = 0.25
        M[i, (i + 1) % N] = 0.05
    return M / M.sum(axis=1, keepdims=True)


def predecessor_bias_corpus(labels_full: list[str], n_reps: int = 100) -> list[str]:
    """Sentences where pred(i) is followed near i: 'Yesterday {pred} then {i}.'"""
    s = []
    N = len(labels_full)
    for _ in range(n_reps):
        for i in range(N):
            pred = (i - 1) % N
            s.append(f"Yesterday {labels_full[pred]} then {labels_full[i]} came.")
    return s


def successor_bias_corpus(labels_full: list[str], n_reps: int = 100) -> list[str]:
    s = []
    N = len(labels_full)
    for _ in range(n_reps):
        for i in range(N):
            succ = (i + 1) % N
            s.append(f"Yesterday {labels_full[succ]} then {labels_full[i]} came.")
    return s


def uniform_corpus(labels_full: list[str], n_reps: int = 200) -> list[str]:
    """Each label appears next to each other label equally often."""
    s = []
    N = len(labels_full)
    for _ in range(n_reps):
        for i in range(N):
            for j in range(N):
                if i != j:
                    s.append(f"On day {labels_full[i]} {labels_full[j]} appears.")
    return s


def run_one(name: str, centroid: np.ndarray, sentences: list[str],
            task: str, tmp: Path) -> str:
    cpath = tmp / f"{name}_centroid.safetensors"
    write_safetensors(cpath, centroid)
    corpus_path = tmp / f"{name}_corpus.txt"
    corpus_path.write_text("\n".join(sentences), encoding="utf-8")
    out_path = tmp / f"{name}_report.md"
    res = subprocess.run([
        sys.executable,
        str(Path(__file__).parent / "bigram_corpus_control.py"),
        "--centroid", str(cpath),
        "--task", task,
        "--model", f"Synthetic_{name}",
        "--corpus", str(corpus_path),
        "--windows", "3", "5",
        "--out", str(out_path),
    ], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED for {name}:")
        print(res.stderr)
        raise SystemExit(1)
    return out_path.read_text(encoding="utf-8")


def parse_asymm_r(report: str, window: int) -> tuple[float, float, int, str]:
    """Returns (headline asymm_r, sign agreement fraction, count, alignment)."""
    in_table = False
    for line in report.splitlines():
        if line.startswith("| window | alignment |"):
            in_table = True
            continue
        if not in_table:
            continue
        if "---" in line:
            continue
        if not line.startswith("| "):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        try:
            w = int(cells[0])
        except ValueError:
            continue
        if w != window:
            continue
        alignment = cells[1]
        asymm = float(cells[2])
        sign_frac_text = cells[3]
        count = int(sign_frac_text.split("/")[0])
        frac = float(sign_frac_text.split("(")[-1].rstrip(")"))
        return asymm, frac, count, alignment
    return float("nan"), float("nan"), 0, ""


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="bigram_smoke_"))
    print(f"workdir: {tmp}")

    days_full = ["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"]
    months_full = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November",
                   "December"]

    # ---------- A: reviewer-hypothesis test ----------
    # Centroid: predecessor leakage (M_centroid[Mon][Sun] large).
    # Corpus: "Yesterday Sun then Mon" -> M_corpus[Sun][Mon] large.
    # Reviewer's claim: this is the same phenomenon viewed via transposed indexes.
    # Expected: TRANSPOSED alignment shows high positive r.
    print("\n--- A: centroid predecessor leakage matched by corpus 'Sun-then-Mon' ---")
    cent = predecessor_bias_centroid(7)
    rep = run_one("A_revhyp_wd", cent, predecessor_bias_corpus(days_full),
                  "weekdays", tmp)
    asymm, frac, count, align = parse_asymm_r(rep, 3)
    print(f"  weekdays w=3: asymm_r={asymm:+.3f}  sign_agree={count}/21 ({frac:.3f}) [{align}]")
    assert asymm > 0.7, f"Expected high positive correlation, got {asymm}"
    assert align == "transposed", f"Expected transposed alignment, got {align}"

    # ---------- B: uniform corpus, no asymmetry ----------
    print("\n--- B: uniform corpus, predecessor-biased centroid ---")
    rep = run_one("B_uniform_wd", cent, uniform_corpus(days_full, n_reps=30),
                  "weekdays", tmp)
    asymm, frac, count, align = parse_asymm_r(rep, 3)
    print(f"  weekdays w=3: asymm_r={asymm:+.3f}  sign_agree={count}/21 ({frac:.3f}) [{align}]")
    import math
    assert math.isnan(asymm) or abs(asymm) < 0.5, \
        f"Expected weak/NaN correlation on uniform corpus, got {asymm}"

    # ---------- C: months sanity ----------
    print("\n--- C: months, reviewer-hypothesis test ---")
    cent_m = predecessor_bias_centroid(12)
    rep = run_one("C_revhyp_mo", cent_m,
                  predecessor_bias_corpus(months_full, n_reps=50),
                  "months", tmp)
    asymm, frac, count, align = parse_asymm_r(rep, 3)
    print(f"  months   w=3: asymm_r={asymm:+.3f}  sign_agree={count}/66 ({frac:.3f}) [{align}]")
    assert asymm > 0.7, f"Expected high positive correlation, got {asymm}"
    assert align == "transposed", f"Expected transposed alignment, got {align}"

    print("\nAll smoke-test assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
