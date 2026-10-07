#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Native Logit-Lens Packet Score (Paper 36 §2.3 / §8 -- lens arm)
================================================================

Reads per-layer last-token residual streams (a safetensors file with shape
[N_examples, n_layers, d_model]) and the model unembedding W_U restricted to
V_R (the cyclic sub-vocabulary), then computes the packet-fraction spectrum
f_{d, ell}^{(lens)} per Paper 36 §2.3:

    s_ell^(lens)(x) = (W_U h_ell(x))_{V_R}   in R^N
    f_{d, ell}^{(lens)} = sum_{a: cond(a) = d}  E_x |hat s(x, a)|^2
                       / sum_{a != 0}          E_x |hat s(x, a)|^2

ANCHORED [P] OBJECTS:
  * Conductor packets on Z/N (paper 36 §2.1).
  * Lens score = native logits restricted to V_R; centered; normalized FFT.

ANCHOR REPRODUCTION (Paper 36 §3 P2, §1.2):
  Llama-3.1-8B, months:
    f_{12, 28}^{(lens)} in [0.30, 0.40]     (Paper 26 raw BF16 hidden-probe)
    f_{12, final}^{(lens)} in [0.62, 0.69]  (Paper 26 native final logits)

OPERATING MODES
---------------
The script supports two input regimes:
  (a) --residual-streams PATH    --unembedding PATH   --token-ids j1,j2,...
        Per-layer scoring (needs per-layer residual streams; needs a partial
        W_U slice for V_R).  This is the full Paper 36 sweep mode.
  (b) --final-probs PATH       --token-ids j1,j2,...
        Final-layer-only scoring from the saved full-vocab native probability
        distribution.  This is enough to compute f_{d, final}^{(lens)} and
        reproduce the Paper 26 final-layer anchor.  Layers other than final
        are deferred as 'requires per-layer residual streams' in the report.

The final-layer-only mode is the available regime in the present session
(no W_U download, no Llama forward pass, transformers not installed, CPU only).
"""

from __future__ import annotations

import argparse
import json
import math
import struct
import sys
from pathlib import Path
from typing import Any

import numpy as np


SCRIPT_VERSION = "audit_kappa_lens_v0.1_2026_05_20"
REPORT_DIR = Path(__file__).resolve().parent / "reports"


def load_safetensors_first(path: str) -> tuple[np.ndarray, str]:
    """Load the first non-metadata tensor from a safetensors file.  Returns
    (array, key_name).  Handles F32, F64, BF16.
    """
    with open(path, "rb") as f:
        hl = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(hl))
        data = f.read()
    key = [k for k in header if k != "__metadata__"][0]
    meta = header[key]
    start, end = meta["data_offsets"]
    dtype_str = meta["dtype"]
    if dtype_str == "F32":
        arr = np.frombuffer(data[start:end], dtype=np.float32).reshape(meta["shape"]).copy()
    elif dtype_str == "F64":
        arr = np.frombuffer(data[start:end], dtype=np.float64).reshape(meta["shape"]).copy()
    elif dtype_str == "BF16":
        raw = np.frombuffer(data[start:end], dtype=np.uint16).copy()
        out = np.zeros(raw.size, dtype=np.uint32)
        out |= raw.astype(np.uint32) << 16
        arr = out.view(np.float32).reshape(meta["shape"]).copy()
    else:
        raise ValueError(f"Unhandled dtype {dtype_str}")
    return arr, key


# ----- packet bookkeeping ----- #

def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conductor_packets(n: int) -> dict[int, list[int]]:
    out: dict[int, list[int]] = {}
    for d in divisors(n):
        chars = [k for k in range(1, n) if n // math.gcd(n, k) == d]
        if chars:
            out[d] = chars
    return out


def packet_fractions_from_logits(s: np.ndarray, N: int) -> dict[int, float]:
    """s: [N_examples, N] logit-like score restricted to V_R.
    Returns f_d = packet-d nontrivial energy share.
    """
    # Center per example
    s_c = s - s.mean(axis=-1, keepdims=True)
    # FFT (unitary)
    coeffs = np.fft.fft(s_c, axis=-1) / math.sqrt(N)
    energies = np.abs(coeffs) ** 2
    # Expectation over examples
    E_a = energies.mean(axis=0)  # [N]
    pk = conductor_packets(N)
    raw = {d: float(np.sum(E_a[ks])) for d, ks in pk.items()}
    tot = sum(raw.values())
    if tot <= 1e-30:
        return {d: 0.0 for d in raw}
    return {d: v / tot for d, v in raw.items()}


# ----- modes ----- #

def run_final_only(args) -> dict[str, Any]:
    """Final-layer measurement from a saved full-vocab probability distribution.
    The lens score per Paper 36 §2.3 is the centered logit restricted to V_R.
    For the final layer, the native log-probability log(p) differs from the
    logit by a per-example constant (the logsumexp), which the per-example
    centering removes.  We therefore use log(p[V_R]) as the lens score, exact
    up to the per-example constant.
    """
    P_full, key = load_safetensors_first(args.final_probs)
    N = args.N
    ids = [int(x) for x in args.token_ids.split(",")]
    if len(ids) != N:
        raise ValueError(f"--token-ids must list N={N} ids, got {len(ids)}")
    P_VR = P_full[:, ids]  # [n_examples, N]
    if (P_VR <= 0).any():
        # The dists are already prob dist; replace zeros with floor
        P_VR = np.maximum(P_VR, 1e-30)
    s = np.log(P_VR)  # logit up to per-example constant; centered FFT eliminates the constant
    f_final = packet_fractions_from_logits(s, N)
    return {
        "mode": "final_only",
        "key": key,
        "input": args.final_probs,
        "N": N,
        "n_examples": int(P_VR.shape[0]),
        "token_ids": ids,
        "f_d_final": {str(d): v for d, v in f_final.items()},
    }


def run_layerwise(args) -> dict[str, Any]:
    """Per-layer scoring with W_U restricted to V_R.
    Expects:
      args.residual_streams : safetensors path, tensor of shape [n_examples, n_layers, d_model].
      args.unembedding_VR  : numpy .npz with key 'W_U_VR' of shape [N, d_model], the
                              unembedding slice corresponding to V_R only.
    Returns f_{d, ell}^(lens) for every layer.
    """
    H, _ = load_safetensors_first(args.residual_streams)
    if H.ndim != 3:
        raise ValueError(f"residual streams must be 3-D [n_examples, n_layers, d_model], got {H.shape}")
    n_examples, n_layers, d_model = H.shape

    npz = np.load(args.unembedding_VR)
    W_U_VR = npz["W_U_VR"]  # [N, d_model]
    N = W_U_VR.shape[0]
    if N != args.N:
        raise ValueError(f"W_U_VR has N={N}, expected --N={args.N}")
    if W_U_VR.shape[1] != d_model:
        raise ValueError(f"W_U_VR last dim {W_U_VR.shape[1]} != residual d_model {d_model}")

    # Score per layer
    f_layerwise: dict[int, dict[int, float]] = {}
    for ell in range(n_layers):
        h_ell = H[:, ell, :]                  # [n_examples, d_model]
        s_ell = h_ell @ W_U_VR.T              # [n_examples, N]
        f_layerwise[ell] = packet_fractions_from_logits(s_ell, N)

    return {
        "mode": "layerwise",
        "input_residuals": args.residual_streams,
        "input_unembedding": args.unembedding_VR,
        "N": N,
        "n_examples": n_examples,
        "n_layers": n_layers,
        "d_model": d_model,
        "f_d_layerwise": {
            str(ell): {str(d): v for d, v in fs.items()}
            for ell, fs in f_layerwise.items()
        },
    }


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    p = argparse.ArgumentParser(description="Paper 36 native logit-lens packet-score (lens arm)")
    p.add_argument("--mode", required=True, choices=["final-only", "layerwise"])
    p.add_argument("--N", type=int, required=True, help="task algebra modulus (12=months, 7=weekdays, 10=digits)")
    p.add_argument("--token-ids", type=str, required=True, help="comma-separated V_R token ids in 0..N-1 order")
    p.add_argument("--final-probs", type=str, help="(final-only mode) safetensors path with [n_examples, |V|] native probs")
    p.add_argument("--residual-streams", type=str, help="(layerwise mode) safetensors path with [n_examples, n_layers, d_model] last-token residuals")
    p.add_argument("--unembedding-VR", type=str, help="(layerwise mode) .npz path with key W_U_VR of shape [N, d_model]")
    p.add_argument("--task", type=str, default="unknown")
    p.add_argument("--model-tag", type=str, default="unknown")
    p.add_argument("--output", type=str, required=True, help="path to write JSON result")
    args = p.parse_args()

    if args.mode == "final-only":
        if not args.final_probs:
            raise ValueError("final-only mode requires --final-probs")
        result = run_final_only(args)
    else:
        if not args.residual_streams or not args.unembedding_VR:
            raise ValueError("layerwise mode requires --residual-streams and --unembedding-VR")
        result = run_layerwise(args)

    result.update({
        "script_version": SCRIPT_VERSION,
        "task": args.task,
        "model_tag": args.model_tag,
    })
    Path(args.output).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"# wrote {args.output}")

    # Echo summary
    if result["mode"] == "final_only":
        print(f"# {args.task} on {args.model_tag} (final layer lens, N={result['N']}, n_examples={result['n_examples']}):")
        for d, v in sorted(result["f_d_final"].items(), key=lambda kv: int(kv[0])):
            print(f"#   f_{d}_final = {v}")
    else:
        n_layers = result["n_layers"]
        print(f"# {args.task} on {args.model_tag} (layerwise lens, N={result['N']}, {n_layers} layers):")
        ks = sorted({int(d) for d in result["f_d_layerwise"]["0"].keys()})
        head = "ell, " + ", ".join(f"f_{d}" for d in ks)
        print("#  " + head)
        for ell in range(n_layers):
            fs = result["f_d_layerwise"][str(ell)]
            row = ", ".join(f"{fs[str(d)]:.4f}" for d in ks)
            print(f"#  {ell:3d}, {row}")


if __name__ == "__main__":
    main()
