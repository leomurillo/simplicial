#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit kappa anchor-gate verifier (settlement bookkeeping, runs locally; numpy only)
===================================================================================

Checks the retrieved layerwise sweep JSONs against the pre-registered anchors
before VM teardown (Paper 36 §3 P2 / §7 F1; errand sanity gate):

  1. months final-layer row vs the Paper 26 anchors reproduced in the audit
     kappa settlement record §2.1 (f2=0.050608, f3=0.066390, f4=0.059082,
     f6=0.166506, f12=0.657415) and the P2 band f12_final in [0.62, 0.69].
  2. months layer-28 row vs the P2 band f12_28 in [0.30, 0.40].
  3. weekdays final-layer row: f7 = 1.0 (prime-modulus degeneracy).
  4. Cross-check: lens score recomputed from the SAVED Paper 26 layer-28
     residuals (months/subspace/pca_k64/result/features/raw_features.safetensors,
     [84, 4096] BF16) with the retrieved W_U_VR slice -- this isolates the
     W_U acquisition + scoring from the new forward-pass reproduction.
     Scoring reuses packet_fractions_from_logits from the lens scorer
     (anchor-verified); no measurement code is duplicated here.

No thresholds here are new: bands are P2's, the six-digit anchors are the
settlement record's.  This script only REPORTS pass/fail; it changes nothing.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "empirical"))

from native_logit_lens_packet_score_layerwise import (  # noqa: E402
    load_safetensors_first,
    packet_fractions_from_logits,
)

MONTHS_FINAL_ANCHORS = {
    "2": 0.050608,
    "3": 0.066390,
    "4": 0.059082,
    "6": 0.166506,
    "12": 0.657415,
}
P2_BAND_FINAL = (0.62, 0.69)
P2_BAND_L28 = (0.30, 0.40)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    reports = ROOT / "empirical" / "reports"
    data = ROOT / "empirical" / "data"
    ok = True

    # --- 1+2: months layerwise sweep ---
    months_json = reports / "layerwise_packet_spectroscopy_months_llama31_8b.json"
    res = json.loads(months_json.read_text(encoding="utf-8"))
    n_layers = res["n_layers"]
    final_row = res["f_d_layerwise"][str(n_layers - 1)]
    print(f"# months sweep: {n_layers} layer rows, n_examples={res['n_examples']}")
    print("# final-layer row vs settlement anchors (tolerance: |delta| <= 5e-3):")
    for d, anchor in MONTHS_FINAL_ANCHORS.items():
        got = final_row[d]
        delta = got - anchor
        flag = "OK" if abs(delta) <= 5e-3 else "MISMATCH"
        if flag != "OK":
            ok = False
        print(f"#   f_{d}_final = {got:.6f}  anchor {anchor:.6f}  delta {delta:+.6f}  {flag}")
    f12_final = final_row["12"]
    band_ok = P2_BAND_FINAL[0] <= f12_final <= P2_BAND_FINAL[1]
    ok &= band_ok
    print(f"# P2 band final: f_12 = {f12_final:.6f} in [{P2_BAND_FINAL[0]}, {P2_BAND_FINAL[1]}]: "
          f"{'OK' if band_ok else 'FAIL'}")

    l28_row = res["f_d_layerwise"]["28"]
    f12_28 = l28_row["12"]
    band28_ok = P2_BAND_L28[0] <= f12_28 <= P2_BAND_L28[1]
    print(f"# P2 band layer-28: f_12 = {f12_28:.6f} in [{P2_BAND_L28[0]}, {P2_BAND_L28[1]}]: "
          f"{'OK' if band28_ok else 'FAIL'}")
    ok &= band28_ok

    # --- 3: weekdays final layer ---
    wd_json = reports / "layerwise_packet_spectroscopy_weekdays_llama31_8b.json"
    wd = json.loads(wd_json.read_text(encoding="utf-8"))
    wd_final = wd["f_d_layerwise"][str(wd["n_layers"] - 1)]
    f7 = wd_final["7"]
    wd_ok = abs(f7 - 1.0) < 1e-12
    ok &= wd_ok
    print(f"# weekdays final: f_7 = {f7}  (expected 1.0 by construction): {'OK' if wd_ok else 'FAIL'}")

    # --- 4: saved-L28-residuals cross-check ---
    raw_path = ROOT / "months" / "subspace" / "pca_k64" / "result" / "features" / "raw_features.safetensors"
    npz_path = data / "W_U_VR_months_llama31_8b.npz"
    H28, _ = load_safetensors_first(str(raw_path))  # [84, 4096]
    W_U_VR = np.load(npz_path)["W_U_VR"]            # [12, 4096]
    s28 = H28.astype(np.float32) @ W_U_VR.T.astype(np.float32)
    f28_saved = packet_fractions_from_logits(s28, 12)
    print("# layer-28 from SAVED Paper 26 residuals (cross-check vs sweep layer-28 row):")
    for d in ["2", "3", "4", "6", "12"]:
        print(f"#   f_{d}_28(saved) = {f28_saved[int(d)]:.6f}   sweep = {l28_row[d]:.6f}   "
              f"delta = {f28_saved[int(d)] - l28_row[d]:+.6f}")
    saved_band_ok = P2_BAND_L28[0] <= f28_saved[12] <= P2_BAND_L28[1]
    print(f"# P2 band layer-28 (saved residuals): f_12 = {f28_saved[12]:.6f}: "
          f"{'OK' if saved_band_ok else 'FAIL'}")

    out = {
        "months_final_row": final_row,
        "months_l28_row": l28_row,
        "months_l28_from_saved_residuals": {str(d): v for d, v in f28_saved.items()},
        "weekdays_final_row": wd_final,
        "anchors": MONTHS_FINAL_ANCHORS,
        "p2_band_final_ok": band_ok,
        "p2_band_l28_ok": band28_ok,
        "p2_band_l28_saved_ok": saved_band_ok,
        "anchor_gate_pass": bool(ok),
    }
    out_path = reports / "audit_kappa_anchor_gate.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"# wrote {out_path}")
    print(f"# ANCHOR GATE: {'PASS' if ok else 'FAIL'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
