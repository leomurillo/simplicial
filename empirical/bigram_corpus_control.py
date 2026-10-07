"""
Bigram-confound control for centroid asymmetric leakage.

Tests whether the observed predecessor-bias asymmetry in the Llama-3.1-8B
and Mistral-7B-v0.3 weekday and month centroid matrices is explained by
pretraining bigram frequency, or whether it is an independent signal
consistent with off-centroid finite arithmetic carry.

Design: see Note_bigram_confound_design.md.

Inputs
------
* Centroid matrices: per_class_output_dists.safetensors for each task and
  model, shape [N, N], rows = correct-answer class, cols = output label.
* Corpus: a plaintext file (one document per line, or arbitrarily long
  paragraphs). The script accepts EITHER:
    --corpus path/to/text.txt
  OR a HuggingFace streaming dataset name (requires `datasets`):
    --hf-dataset allenai/c4 --hf-config en --hf-split train --max-tokens 10000000

Outputs
-------
* empirical/reports/bigram_corpus_control_<task>_<model>.md

Statistics reported per (task, model, window-size):
    * Off-diagonal Pearson r:  leakage L_ij  vs  raw count C_ij
    * Asymmetry Pearson r:     A_ij = L_ij - L_ji  vs  Delta_ij = C_ij - C_ji
    * Sign-agreement rate of A_ij vs Delta_ij over off-diagonal pairs
    * Conditional Pearson r:   L_ij  vs  P(d_j | d_i, w) = C_ij / sum_k C_ik
    * Conductor-projection energy fractions of the asymmetry vector under
      the additive-character basis of C_N

Pre-registered interpretation thresholds (from the design note):
    "bigrams fully explain"       asymm-Pearson >= 0.70 AND sign-agree >= 18/21
    "bigrams do not explain"      asymm-Pearson <= 0.20 AND sign-agree <= 13/21
    otherwise: "consistent with both"

The core analysis depends only on numpy + scipy + stdlib. HuggingFace streaming
also requires `datasets`; use `--corpus` for a dependency-light plaintext run.
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path
from typing import Iterable, Iterator

import numpy as np
from scipy.stats import pearsonr


# ---------------------------------------------------------------------------
# 1. Safetensors loader (matches existing scripts in this directory)
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
# 2. Label vocabularies and morphological variants
# ---------------------------------------------------------------------------

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday"]

MONTHS = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]

# Match the bare canonical form. Possessives like "Monday's" and abbreviations
# ("Mon", "Jan") are deliberately excluded for the strict-form pass; a future
# variant pass can include them.
def make_label_pattern(labels: list[str]) -> re.Pattern:
    return re.compile(r"\b(" + "|".join(labels) + r")\b", re.IGNORECASE)


# ---------------------------------------------------------------------------
# 3. Corpus iterators
# ---------------------------------------------------------------------------

def iter_plaintext(path: Path) -> Iterator[str]:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if line:
                yield line


def iter_hf_streaming(dataset: str, config: str | None, split: str,
                      max_docs: int, text_field: str = "text") -> Iterator[str]:
    try:
        from datasets import load_dataset
    except ImportError as e:
        raise SystemExit(
            "HuggingFace datasets not installed; install with `pip install datasets` "
            "or use --corpus with a plaintext file."
        ) from e
    ds = load_dataset(dataset, config, split=split, streaming=True)
    for i, ex in enumerate(ds):
        if i >= max_docs:
            return
        text = ex.get(text_field)
        if text:
            yield text


# ---------------------------------------------------------------------------
# 4. Co-occurrence counting
#
# Strategy: scan a document. For each label hit, look ahead up to `window`
# tokens (in a whitespace-tokenized stream of the document) for the next
# label hit. Each ordered pair (label_i, label_j) at distance d <= window
# increments C^{(window)}[i][j].
#
# We do not count (i, i) self-co-occurrences in C (they swamp diagonals).
# We do not count crossing label-pair boundaries (only the *next* label after
# each hit). This is the strictest interpretation of "bigram" and gives the
# cleanest predecessor-bias signal.
# ---------------------------------------------------------------------------

def cooccurrence_matrix(corpus: Iterable[str], labels: list[str],
                        window: int) -> tuple[np.ndarray, np.ndarray, int]:
    """
    Returns:
        C         shape [N, N], C[i,j] = #(label_i followed-within-window by label_j)
        unigram   shape [N],   counts of each label
        n_docs    number of docs scanned
    """
    n = len(labels)
    label_to_idx = {lab: i for i, lab in enumerate(labels)}
    pattern = make_label_pattern(labels)

    C = np.zeros((n, n), dtype=np.int64)
    unigram = np.zeros(n, dtype=np.int64)
    n_docs = 0

    for doc in corpus:
        n_docs += 1
        text = doc.lower()
        # Tokenize on whitespace AND keep label boundaries; the regex finds
        # label spans directly so we don't need to align with whitespace tokens.
        hits: list[tuple[int, int]] = []   # (label_idx, whitespace_token_pos)
        ws_tokens = text.split()
        # Build a position map: token_index -> char_offset_start
        char_pos = 0
        token_starts = []
        for tok in ws_tokens:
            # advance through whitespace
            while char_pos < len(text) and text[char_pos].isspace():
                char_pos += 1
            token_starts.append(char_pos)
            char_pos += len(tok)
        # Find label spans (in char coords), assign to nearest enclosing token
        spans = [(m.start(), m.group().lower()) for m in pattern.finditer(text)]
        if not spans:
            continue
        # Convert char-start -> token-index via binary search
        import bisect
        for char_start, lab in spans:
            tok_idx = bisect.bisect_right(token_starts, char_start) - 1
            li = label_to_idx[lab]
            hits.append((li, tok_idx))
            unigram[li] += 1
        # Sequential pass: for each hit, find next hit at token-distance <= window
        for k in range(len(hits) - 1):
            li, ti = hits[k]
            lj, tj = hits[k + 1]
            if li == lj:
                continue
            d = tj - ti
            if 1 <= d <= window:
                C[li, lj] += 1

    return C, unigram, n_docs


# ---------------------------------------------------------------------------
# 5. Statistics
# ---------------------------------------------------------------------------

def offdiag_entries(M: np.ndarray) -> np.ndarray:
    n = M.shape[0]
    out = []
    for i in range(n):
        for j in range(n):
            if i != j:
                out.append(M[i, j])
    return np.asarray(out)


def upper_tri_pairs(M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Returns A and -A^T entries on i<j; used for asymmetry analyses."""
    n = M.shape[0]
    out_ij, out_ji = [], []
    for i in range(n):
        for j in range(i + 1, n):
            out_ij.append(M[i, j])
            out_ji.append(M[j, i])
    return np.asarray(out_ij), np.asarray(out_ji)


def safe_pearson(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return float("nan"), float("nan")
    r, p = pearsonr(x, y)
    return float(r), float(p)


def conditional_matrix(C: np.ndarray) -> np.ndarray:
    """P(j | i, window) = C[i,j] / sum_k C[i,k]; rows summing to 1."""
    row_sums = C.sum(axis=1, keepdims=True)
    row_sums = np.where(row_sums == 0, 1, row_sums)
    return C / row_sums


def cyclic_character_basis(n: int) -> np.ndarray:
    """
    Unitary DFT basis on Z/n: columns are the additive characters
    psi_k(x) = exp(2*pi*i*k*x/n) / sqrt(n).
    Returns an n x n complex matrix B; the k-th column is psi_k as a vector.
    """
    x = np.arange(n)
    k = np.arange(n).reshape(-1, 1)
    return np.exp(2j * np.pi * k * x / n) / np.sqrt(n)  # rows = characters


def conductor_groups_C7() -> dict[str, list[int]]:
    # C_7 has only the trivial character (k=0) and one nontrivial conductor.
    return {
        "trivial (k=0)": [0],
        "conductor 7 (nontrivial)": [1, 2, 3, 4, 5, 6],
    }


def conductor_groups_C12() -> dict[str, list[int]]:
    # For C_12: conductor of character k is 12 / gcd(12, k).
    # k=0  -> conductor 1 (trivial)
    # k=6  -> conductor 2
    # k=4,8 -> conductor 3
    # k=3,9 -> conductor 4
    # k=2,10 -> conductor 6
    # k=1,5,7,11 -> conductor 12
    groups: dict[str, list[int]] = {
        "trivial (k=0)": [0],
        "conductor 2": [6],
        "conductor 3": [4, 8],
        "conductor 4": [3, 9],
        "conductor 6 (mixed)": [2, 10],
        "conductor 12": [1, 5, 7, 11],
    }
    return groups


def conductor_energy(vec: np.ndarray, groups: dict[str, list[int]]) -> dict[str, float]:
    """Project a real n-vector onto each conductor packet under the DFT basis."""
    n = len(vec)
    B = cyclic_character_basis(n)        # rows are characters
    coeffs = B @ vec                     # complex amplitudes per character
    energies = (np.abs(coeffs) ** 2)
    total = energies.sum()
    if total < 1e-30:
        return {name: 0.0 for name in groups}
    out = {}
    for name, ks in groups.items():
        out[name] = float(energies[ks].sum() / total)
    return out


def conductor_energy_aggregate(rows: np.ndarray,
                               groups: dict[str, list[int]]) -> dict[str, float]:
    """
    Aggregate conductor energy across all per-row displacements.

    `rows[i]` should be the displacement h_i = p_i - p_* of row i from the
    uniform distribution. The trivial-character coefficient is automatically
    zero because each h_i sums to zero.

    Energy per packet is summed over rows and over characters in the packet,
    then normalized so the totals across packets sum to 1.

    This mirrors the §5.1 CRT conductor energy decomposition in the manuscript.
    """
    n = rows.shape[1]
    B = cyclic_character_basis(n)
    # complex amplitudes: rows x characters
    coeffs = rows @ B.T  # (n_rows, n_chars)
    energies = np.abs(coeffs) ** 2
    per_packet_total = {}
    for name, ks in groups.items():
        per_packet_total[name] = float(energies[:, ks].sum())
    total = sum(per_packet_total.values())
    if total < 1e-30:
        return {name: 0.0 for name in groups}
    return {name: v / total for name, v in per_packet_total.items()}


# ---------------------------------------------------------------------------
# 6. Report generation
# ---------------------------------------------------------------------------

THRESHOLD_FULL = dict(asymm_r=0.70, sign_agree_frac=18 / 21)
THRESHOLD_NONE = dict(asymm_r=0.20, sign_agree_frac=13 / 21)


def interpret(asymm_r: float, sign_agree_frac: float, n_pairs: int) -> str:
    if n_pairs < 3 or np.isnan(asymm_r) or np.isnan(sign_agree_frac):
        return "INSUFFICIENT DATA at this window — too few co-occurrences."
    if asymm_r >= THRESHOLD_FULL["asymm_r"] and sign_agree_frac >= THRESHOLD_FULL["sign_agree_frac"]:
        return "BIGRAMS FULLY EXPLAIN — manuscript §4.1 'arithmetic carry' framing must be retracted."
    if asymm_r <= THRESHOLD_NONE["asymm_r"] and sign_agree_frac <= THRESHOLD_NONE["sign_agree_frac"]:
        return "BIGRAMS DO NOT EXPLAIN — manuscript §4.1 framing supported."
    return "INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'."


def make_report(task: str, model: str, labels: list[str],
                centroid: np.ndarray, results_per_window: list[dict],
                cooccur_per_window: dict[int, np.ndarray],
                unigram: np.ndarray, n_docs: int, token_count: int,
                corpus_desc: str) -> str:
    lines = []
    lines.append(f"# Bigram-confound control — {task}, {model}")
    lines.append("")
    lines.append(f"**Corpus:** {corpus_desc}")
    lines.append(f"**Documents scanned:** {n_docs}")
    lines.append(f"**Whitespace tokens scanned:** {token_count}")
    lines.append(f"**Unigram counts:** " +
                 ", ".join(f"{lab}={c}" for lab, c in zip(labels, unigram)))
    lines.append("")
    lines.append("**Pre-registered thresholds:**")
    lines.append(f"- Fully explain:  asymm Pearson r >= {THRESHOLD_FULL['asymm_r']:.2f} AND "
                 f"sign agreement >= {THRESHOLD_FULL['sign_agree_frac']:.3f}")
    lines.append(f"- Do not explain: asymm Pearson r <= {THRESHOLD_NONE['asymm_r']:.2f} AND "
                 f"sign agreement <= {THRESHOLD_NONE['sign_agree_frac']:.3f}")
    lines.append("- Intermediate: anything else.")
    lines.append("")

    lines.append("## Per-window statistics — headline (max-|r| alignment)")
    lines.append("")
    lines.append("Two alignments are considered for each window:")
    lines.append("- **same:** centroid M[i,j] vs corpus M[i,j]")
    lines.append("- **transposed:** centroid M[i,j] vs corpus M[j,i]")
    lines.append("")
    lines.append("The headline row reports whichever alignment has larger |asymm r|.")
    lines.append("If the reviewer's hypothesis 'pretraining \"Sun Mon\" bigram explains")
    lines.append("Mon→Sun centroid leakage' holds, the transposed alignment will")
    lines.append("show high correlation; if same-direction bigrams drive the bias,")
    lines.append("the same alignment will. Either is bad for the manuscript claim.")
    lines.append("")
    lines.append("| window | alignment | asymm r | sign agree | verdict |")
    lines.append("|---:|---|---:|---:|---|")
    for r in results_per_window:
        lines.append(
            f"| {r['window']} | "
            f"{r['head_alignment']} | "
            f"{r['asymm_r']:.3f} | "
            f"{r['sign_agree_count']}/{r['n_pairs']} ({r['sign_agree_frac']:.3f}) | "
            f"{interpret(r['asymm_r'], r['sign_agree_frac'], r['n_pairs'])} |"
        )
    lines.append("")
    lines.append("## Per-window statistics — full")
    lines.append("")
    lines.append("| window | offdiag r same (raw) | offdiag r trans (raw) | "
                 "offdiag r same (cond) | offdiag r trans (cond) | "
                 "asymm r same | asymm r trans | "
                 "sign same | sign trans |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in results_per_window:
        sa_s = r["sign_same"]
        sa_t = r["sign_trans"]
        lines.append(
            f"| {r['window']} | "
            f"{r['offdiag_r_raw_same']:.3f} | "
            f"{r['offdiag_r_raw_trans']:.3f} | "
            f"{r['offdiag_r_cond_same']:.3f} | "
            f"{r['offdiag_r_cond_trans']:.3f} | "
            f"{r['asymm_r_same']:.3f} | "
            f"{r['asymm_r_trans']:.3f} | "
            f"{sa_s[0]}/{sa_s[1]} | "
            f"{sa_t[0]}/{sa_t[1]} |"
        )
    lines.append("")

    lines.append("## Conductor-packet energy decomposition (per-row displacements)")
    lines.append("")
    lines.append("Each row i of the centroid (resp. row-normalized corpus matrix)")
    lines.append("is a probability distribution p_i on Z/N. The displacement from")
    lines.append("uniform h_i = p_i - p_* lives in the zero-sum hyperplane and")
    lines.append("decomposes under the additive-character basis. Energy is summed")
    lines.append("across rows and across characters within each conductor packet,")
    lines.append("then normalized to sum to 1.")
    lines.append("")
    lines.append("This is the §5.1 conductor energy decomposition applied")
    lines.append("symmetrically to both the centroid and the corpus co-occurrence.")
    lines.append("If the bigram corpus carries the same conductor signature as the")
    lines.append("centroid, the two decompositions should agree.")
    lines.append("")
    n = len(labels)
    if n == 7:
        groups = conductor_groups_C7()
    elif n == 12:
        groups = conductor_groups_C12()
    else:
        groups = {f"k={k}": [k] for k in range(n)}
    uniform = np.ones(n) / n
    h_centroid = centroid - uniform[None, :]
    centroid_pkts = conductor_energy_aggregate(h_centroid, groups)
    lines.append("**Centroid h_i conductor energy fractions:**")
    for name, frac in centroid_pkts.items():
        lines.append(f"- {name}: {frac:.4f}")
    lines.append("")
    for w, C in cooccur_per_window.items():
        Cd = C.astype(np.float64)
        row_sums = Cd.sum(axis=1, keepdims=True)
        row_sums = np.where(row_sums < 1e-12, 1.0, row_sums)
        Pcorp = Cd / row_sums
        h_corp = Pcorp - uniform[None, :]
        corp_pkts = conductor_energy_aggregate(h_corp, groups)
        lines.append(f"**Corpus h_i conductor energy fractions (window={w}):**")
        for name, frac in corp_pkts.items():
            lines.append(f"- {name}: {frac:.4f}")
        lines.append("")

    lines.append("## Centroid matrix")
    lines.append("")
    lines.append("| | " + " | ".join(labels) + " |")
    lines.append("|---|" + "|".join(["---"] * len(labels)) + "|")
    for i, lab in enumerate(labels):
        lines.append("| " + lab + " | " +
                     " | ".join(f"{x:.4f}" for x in centroid[i]) + " |")
    lines.append("")

    lines.append("## Corpus co-occurrence matrix (window=3)")
    lines.append("")
    C3 = cooccur_per_window.get(3, list(cooccur_per_window.values())[0])
    lines.append("| | " + " | ".join(labels) + " |")
    lines.append("|---|" + "|".join(["---"] * len(labels)) + "|")
    for i, lab in enumerate(labels):
        lines.append("| " + lab + " | " +
                     " | ".join(str(x) for x in C3[i]) + " |")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 7. Driver
# ---------------------------------------------------------------------------

def analyze(centroid: np.ndarray, labels: list[str], corpus_iter_fn,
            windows: list[int], max_tokens: int | None = None
            ) -> tuple[list[dict], dict[int, np.ndarray], np.ndarray, int, int]:
    # We need to scan the corpus once per window, OR accumulate co-occurrences
    # at the *maximum* window and downsample to each smaller window post-hoc.
    # We do a single pass at max(windows) by tracking the actual token distance
    # of each consecutive label-pair.
    max_w = max(windows)
    n = len(labels)

    label_to_idx = {lab: i for i, lab in enumerate(labels)}
    pattern = make_label_pattern(labels)

    # Distance histogram per ordered pair (i,j): D[i,j,d] for d in 1..max_w
    D = np.zeros((n, n, max_w + 1), dtype=np.int64)
    unigram = np.zeros(n, dtype=np.int64)
    n_docs = 0
    token_count = 0

    import bisect
    for doc in corpus_iter_fn():
        text = doc.lower()
        ws_tokens = text.split()
        if not ws_tokens:
            continue
        if max_tokens is not None:
            remaining = max_tokens - token_count
            if remaining <= 0:
                break
            if len(ws_tokens) > remaining:
                ws_tokens = ws_tokens[:remaining]
                text = " ".join(ws_tokens)
        n_docs += 1
        token_count += len(ws_tokens)
        char_pos = 0
        token_starts = []
        for tok in ws_tokens:
            while char_pos < len(text) and text[char_pos].isspace():
                char_pos += 1
            token_starts.append(char_pos)
            char_pos += len(tok)
        spans = [(m.start(), m.group().lower()) for m in pattern.finditer(text)]
        if not spans:
            continue
        hits: list[tuple[int, int]] = []
        for char_start, lab in spans:
            tok_idx = bisect.bisect_right(token_starts, char_start) - 1
            li = label_to_idx[lab]
            hits.append((li, tok_idx))
            unigram[li] += 1
        for k in range(len(hits) - 1):
            li, ti = hits[k]
            lj, tj = hits[k + 1]
            d = tj - ti
            if li != lj and 1 <= d <= max_w:
                D[li, lj, d] += 1

    cooccur_per_window: dict[int, np.ndarray] = {}
    for w in windows:
        C = D[:, :, 1:w + 1].sum(axis=2)
        cooccur_per_window[w] = C

    results = []
    for w in windows:
        C = cooccur_per_window[w]
        Cd = C.astype(np.float64)
        # off-diagonal raw correlation, same alignment
        x = offdiag_entries(centroid)
        y_same = offdiag_entries(Cd)
        y_trans = offdiag_entries(Cd.T)
        r_raw_same, _ = safe_pearson(x, y_same)
        r_raw_trans, _ = safe_pearson(x, y_trans)
        # conditional (row-normalized)
        Pcond = conditional_matrix(Cd)
        Pcond_t = conditional_matrix(Cd.T)
        r_cond_same, _ = safe_pearson(x, offdiag_entries(Pcond))
        r_cond_trans, _ = safe_pearson(x, offdiag_entries(Pcond_t))
        # asymmetry — same alignment
        A_emp_ij, A_emp_ji = upper_tri_pairs(centroid)
        A_corp_ij, A_corp_ji = upper_tri_pairs(Cd)
        a_emp = A_emp_ij - A_emp_ji          # centroid asymmetry
        a_corp_same = A_corp_ij - A_corp_ji  # corpus asymmetry, same indexing
        r_asymm_same, _ = safe_pearson(a_emp, a_corp_same)
        # transposed alignment: corpus M[Sun][Mon] in slot (Sun,Mon) should
        # be compared against centroid M[Mon][Sun] -> centroid asymmetry has
        # opposite sign relative to a corpus that swaps roles.
        a_corp_trans = -a_corp_same
        r_asymm_trans, _ = safe_pearson(a_emp, a_corp_trans)

        def _sign_stats(a, b):
            mask = (np.abs(a) > 1e-9) & (np.abs(b) > 1e-9)
            if mask.sum() == 0:
                return 0, 0, float("nan")
            cnt = int(np.sum(np.sign(a[mask]) == np.sign(b[mask])))
            n = int(mask.sum())
            return cnt, n, cnt / n
        sa_same = _sign_stats(a_emp, a_corp_same)
        sa_trans = _sign_stats(a_emp, a_corp_trans)

        # For asymmetry, r_trans = -r_same exactly (since a_corp_trans = -a_corp_same).
        # The bigram-explanation hypothesis is supported by the alignment whose
        # asymm Pearson is POSITIVE. Pick that one as the headline.
        if np.isnan(r_asymm_same):
            head_r, head_sa = r_asymm_same, sa_same
            head_alignment = "same"
        elif r_asymm_same >= 0:
            head_r, head_sa = r_asymm_same, sa_same
            head_alignment = "same"
        else:
            head_r, head_sa = r_asymm_trans, sa_trans
            head_alignment = "transposed"

        results.append(dict(
            window=w,
            offdiag_r_raw_same=r_raw_same,
            offdiag_r_raw_trans=r_raw_trans,
            offdiag_r_cond_same=r_cond_same,
            offdiag_r_cond_trans=r_cond_trans,
            asymm_r_same=r_asymm_same,
            asymm_r_trans=r_asymm_trans,
            sign_same=sa_same,
            sign_trans=sa_trans,
            asymm_r=head_r,
            sign_agree_count=head_sa[0],
            n_pairs=head_sa[1],
            sign_agree_frac=head_sa[2],
            head_alignment=head_alignment,
        ))
    return results, cooccur_per_window, unigram, n_docs, token_count


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--centroid", required=True, type=Path,
                   help="Path to per_class_output_dists.safetensors")
    p.add_argument("--task", required=True, choices=["weekdays", "months"])
    p.add_argument("--model", required=True,
                   help="Model name for the report header, e.g. 'Llama-3.1-8B'")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--corpus", type=Path,
                     help="Plaintext corpus (one document per line)")
    src.add_argument("--hf-dataset", type=str,
                     help="HuggingFace streaming dataset id, e.g. 'allenai/c4'")
    p.add_argument("--hf-config", type=str, default=None)
    p.add_argument("--hf-split", type=str, default="train")
    p.add_argument("--hf-max-docs", type=int, default=100_000)
    p.add_argument("--hf-text-field", type=str, default="text")
    p.add_argument("--max-tokens", type=int, default=None,
                   help="Stop after this many whitespace tokens (applies to either corpus source)")
    p.add_argument("--windows", type=int, nargs="+", default=[1, 3, 5, 10])
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    labels = WEEKDAYS if args.task == "weekdays" else MONTHS
    centroid = load_safetensors(args.centroid)
    if centroid.shape != (len(labels), len(labels)):
        raise SystemExit(
            f"Centroid shape {centroid.shape} does not match task {args.task} "
            f"(expected {len(labels)}x{len(labels)})"
        )
    # Row normalize defensively in case the file is unnormalized
    row_sums = centroid.sum(axis=1, keepdims=True)
    row_sums = np.where(row_sums < 1e-12, 1.0, row_sums)
    centroid = centroid / row_sums

    if args.corpus:
        corpus_desc = f"plaintext file: {args.corpus}"
        def corpus_iter_fn():
            return iter_plaintext(args.corpus)
    else:
        corpus_desc = (f"HuggingFace streaming dataset: {args.hf_dataset} "
                       f"(config={args.hf_config}, split={args.hf_split}, "
                       f"max_docs={args.hf_max_docs}, "
                       f"max_tokens={args.max_tokens})")
        def corpus_iter_fn():
            return iter_hf_streaming(args.hf_dataset, args.hf_config,
                                     args.hf_split, args.hf_max_docs,
                                     args.hf_text_field)

    results, cooccur_per_window, unigram, n_docs, token_count = analyze(
        centroid, labels, corpus_iter_fn, args.windows, args.max_tokens)

    report = make_report(args.task, args.model, labels, centroid,
                         results, cooccur_per_window, unigram, n_docs,
                         token_count, corpus_desc)

    if args.out:
        out_path = args.out
    else:
        out_dir = Path(__file__).parent / "reports"
        out_dir.mkdir(exist_ok=True)
        safe_model = args.model.lower().replace(" ", "_").replace(".", "_").replace("-", "_")
        out_path = out_dir / f"bigram_corpus_control_{args.task}_{safe_model}.md"

    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote {out_path}")
    print()
    # Print only the headline table to stdout (full report in the file)
    in_table = False
    for line in report.splitlines():
        if line.startswith("## Per-window statistics"):
            in_table = True
        elif line.startswith("## ") and in_table:
            break
        if in_table:
            try:
                print(line)
            except UnicodeEncodeError:
                print(line.encode("ascii", "replace").decode("ascii"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
