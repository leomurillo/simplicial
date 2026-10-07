#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CCSAE structural certificate (Paper 45 Theorems 4.1 + 4.2) -- deterministic, local
==================================================================================

Verifies, on the captured audit-kappa artifacts (per-layer last-token residual
streams + W_U_VR slices for Llama-3.1-8B and Mistral-7B-v0.3 on months/weekdays),
the two structural theorems of Paper 45 that the strongest abstract clause rests on:

  Thm 4.1 (Packet-Purity).  The hard-certification step (Paper 45 sec 3.2) makes
  every certified decoder column packet-pure: (I - P_S) pi(w') = 0 to machine
  precision, where pi = restrict-to-V_R + center and P_S = orthogonal projection
  onto the certified packet subspace (+)_{d in S} H_d in the character basis.

  Thm 4.2 (Reconstruction-Cost), idealized identity.  A decoder whose image lies
  in (+)_{d in S} H_d can reconstruct at most P_S pi(h) of the cyclic content;
  its reconstruction FLOOR on that content is E_h ||(I - P_S) pi(h)||^2.  We verify
  this floor equals the OUT-OF-SUPPORT packet content  sum_{d not in S} f_d  (the
  native packet fractions measured in audit kappa) -- i.e. the certification gap
  is EXACTLY the Paper 26 Pontryagin obstruction, no more, no less.  For Llama
  months this reproduces Paper 45 sec 4.2: S={12} -> 0.3426, S={2,6} -> 0.7829,
  S=full -> 0.

NOT torch.  NOT a trained SAE.  This is the exact-arithmetic structural spine; the
production-scale claim that a *trained* finite-width SAE attains this floor (Paper 45
P3) is the separate GPU confirmation (Phase B).  GPD tier: deterministic
exact-arithmetic settlement anchored to source objects.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "empirical"))

from native_logit_lens_packet_score_layerwise import (  # noqa: E402
    conductor_packets,
    load_safetensors_first,
    packet_fractions_from_logits,
)

DATA = ROOT / "empirical" / "data"
REPORTS = ROOT / "empirical" / "reports"

# Pre-registered closed supports (Paper 45 sec 5).
SUPPORTS = {
    "months": {"S_full_period": [12], "S_coarse": [2, 6], "S_all": [2, 3, 4, 6, 12]},
    "weekdays": {"S_all": [7]},
}
# Paper 45 sec 4.2 stated gaps for Llama months (cross-check target).
PAPER45_S42 = {"S_full_period": 0.3426, "S_coarse": 0.7829, "S_all": 0.0}

MODELS = {"llama31_8b": "Llama-3.1-8B", "mistral7b_v0_3": "Mistral-7B-v0.3"}


def dft_matrix(N: int) -> np.ndarray:
    """Unitary DFT: U[a, j] = exp(-2 pi i a j / N) / sqrt(N)."""
    a = np.arange(N)[:, None]
    j = np.arange(N)[None, :]
    return np.exp(-2j * math.pi * a * j / N) / math.sqrt(N)


def packet_projection(N: int, S: list[int]) -> np.ndarray:
    """Real N x N orthogonal projection onto (+)_{d in S} H_d.

    H_d = span of characters chi_a with conductor d.  The character index set for
    S is closed under a -> N-a (conductor is symmetric), so the complex projection
    U_A^dagger U_A is real on real inputs.
    """
    pk = conductor_packets(N)
    A = sorted({a for d in S for a in pk.get(d, [])})
    U = dft_matrix(N)
    UA = U[A, :]                      # |A| x N
    P = (UA.conj().T @ UA)            # N x N, Hermitian
    P_real = P.real
    # sanity: imaginary part must vanish (symmetric index set) and P must be an
    # idempotent symmetric real projector.
    assert np.max(np.abs(P.imag)) < 1e-10, "packet projection not real"
    assert np.max(np.abs(P_real - P_real.T)) < 1e-10, "P not symmetric"
    assert np.max(np.abs(P_real @ P_real - P_real)) < 1e-9, "P not idempotent"
    return P_real


def centering(N: int) -> np.ndarray:
    return np.eye(N) - np.ones((N, N)) / N


def thm41_check(W_U_VR: np.ndarray, N: int, S: list[int], rng: np.random.Generator,
                n_dirs: int = 64) -> float:
    """Return max forbidden-packet leakage over n_dirs certified decoder columns.

    pi = C @ W_U_VR  (N x d).  Hard certification (Paper 45 sec 3.2):
        w' = w - pi^+ (I - P_S) pi w.
    Then pi(w') has zero out-of-support packet energy, i.e. (I - P_S) pi w' = 0.
    """
    d = W_U_VR.shape[1]
    C = centering(N)
    pi = C @ W_U_VR                      # N x d
    pi_pinv = np.linalg.pinv(pi)         # d x N
    P_S = packet_projection(N, S)
    Q = np.eye(N) - P_S                  # forbidden projection
    # natural directions: random Gaussian in R^d (decoder columns live here)
    W = rng.standard_normal((d, n_dirs))
    # certify each column
    forbidden = Q @ pi                   # N x d : forbidden image of a raw column
    W_cert = W - pi_pinv @ (forbidden @ W)
    leak = Q @ (pi @ W_cert)             # should be ~0
    return float(np.max(np.abs(leak)))


def thm42_floor(H_layer: np.ndarray, W_U_VR: np.ndarray, N: int,
                S: list[int]) -> dict:
    """Idealized reconstruction floor of a certified decoder on the cyclic content.

    s = pi(h) restricted to V_R (centered logit profile).  A decoder with image in
    (+)_{d in S} H_d reconstructs at most P_S s; residual = (I - P_S) s.  The floor
    fraction = E||(I - P_S)s||^2 / E||s_nontrivial||^2, computed two independent ways:
      (a) spectral: sum_{d not in S} f_d   (native packet fractions),
      (b) direct: real-space projection (I - P_S) applied to s.
    They must agree to machine precision -- that agreement is the certificate that
    the gap EQUALS the obstruction.
    """
    s = H_layer.astype(np.float64) @ W_U_VR.T.astype(np.float64)   # [n, N]
    f = packet_fractions_from_logits(s, N)                          # native fractions
    out_of_support = [d for d in f if d not in S]
    gap_spectral = float(sum(f[d] for d in out_of_support))

    # direct real-space projection floor
    C = centering(N)
    s_c = (C @ s.T).T                       # centered, [n, N]
    P_S = packet_projection(N, S)
    resid = s_c - (P_S @ s_c.T).T           # (I - P_S) s_c
    E_resid = float(np.mean(np.sum(resid ** 2, axis=1)))
    E_total = float(np.mean(np.sum(s_c ** 2, axis=1)))
    gap_direct = E_resid / E_total

    return {
        "support_S": S,
        "packet_fractions": {str(d): f[d] for d in f},
        "gap_fraction_spectral": gap_spectral,
        "gap_fraction_direct": gap_direct,
        "gap_identity_abs_err": abs(gap_spectral - gap_direct),
    }


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    rng = np.random.default_rng(0)
    out: dict = {"theorem": "Paper45 Thm 4.1 + 4.2 structural certificate", "cells": []}
    worst_leak = 0.0
    worst_identity = 0.0

    for task in ["months", "weekdays"]:
        N = 12 if task == "months" else 7
        for tag, pretty in MODELS.items():
            res_path = DATA / f"residual_streams_{task}_{tag}.safetensors"
            npz_path = DATA / f"W_U_VR_{task}_{tag}.npz"
            if not res_path.exists() or not npz_path.exists():
                print(f"# SKIP {task}/{tag}: artifacts missing")
                continue
            H, _ = load_safetensors_first(str(res_path))     # [n, 33, d]
            W_U_VR = np.load(npz_path)["W_U_VR"]             # [N, d]
            n_layers = H.shape[1]
            H_final = H[:, n_layers - 1, :]                   # anchor layer
            print(f"\n# === {task} / {pretty}  (final layer = row {n_layers-1}, anchor) ===")
            for name, S in SUPPORTS[task].items():
                leak = thm41_check(W_U_VR, N, S, rng)
                floor = thm42_floor(H_final, W_U_VR, N, S)
                worst_leak = max(worst_leak, leak)
                worst_identity = max(worst_identity, floor["gap_identity_abs_err"])
                cell = {
                    "task": task, "model": tag, "support_name": name, "support_S": S,
                    "thm41_max_forbidden_leakage": leak,
                    **floor,
                }
                # cross-check vs Paper 45 sec 4.2 (Llama months only)
                if task == "months" and tag == "llama31_8b" and name in PAPER45_S42:
                    cell["paper45_s4.2_stated_gap"] = PAPER45_S42[name]
                    cell["paper45_s4.2_abs_err"] = abs(floor["gap_fraction_spectral"] - PAPER45_S42[name])
                out["cells"].append(cell)
                extra = ""
                if "paper45_s4.2_stated_gap" in cell:
                    extra = (f"  [Paper45 4.2 says {cell['paper45_s4.2_stated_gap']:.4f}, "
                             f"|err|={cell['paper45_s4.2_abs_err']:.2e}]")
                print(f"#  S={str(S):<18} Thm4.1 leak={leak:.2e}  "
                      f"gap(spectral)={floor['gap_fraction_spectral']:.6f}  "
                      f"gap(direct)={floor['gap_fraction_direct']:.6f}  "
                      f"identity|err|={floor['gap_identity_abs_err']:.2e}{extra}")

    out["worst_thm41_leakage"] = worst_leak
    out["worst_thm42_identity_err"] = worst_identity
    out["thm41_pass"] = worst_leak < 1e-9
    out["thm42_pass"] = worst_identity < 1e-9
    out_path = REPORTS / "ccsae_certificate.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\n# wrote {out_path}")
    print(f"# Thm 4.1 (packet purity)  worst forbidden leakage = {worst_leak:.2e}  "
          f"-> {'PASS' if out['thm41_pass'] else 'FAIL'}")
    print(f"# Thm 4.2 (gap = obstruction) worst identity error = {worst_identity:.2e}  "
          f"-> {'PASS' if out['thm42_pass'] else 'FAIL'}")
    sys.exit(0 if (out["thm41_pass"] and out["thm42_pass"]) else 1)


if __name__ == "__main__":
    main()
