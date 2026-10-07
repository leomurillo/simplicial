#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V/M saturation-index significance via prompt bootstrap (Paper 36 §3.A P9)
=========================================================================

The audit-κ sweep gave the depth-normalized saturation index sigma_d as a single
point estimate per (model, packet) -- one checkpoint, one prompt set, no bands.
This settles the open significance leg WITHOUT any new model run: we bootstrap-
resample the captured per-example residual streams (the 84 months prompts) and
recompute the SAME pre-registered sigma_d on each resample, giving its sampling
distribution under prompt resampling.

Pre-registered statistic (unchanged, Paper 36 §3.A):
    sigma_d = mean_ell[ f_{d,ell} * ell / L ] / f_{d,final}
V = {2,3,4} (single-prime/prime-power, inclusive per audit χ_12); M = {6,12}.

Separation statistic: gap = min_{d in V} sigma_d - max_{d in M} sigma_d.
gap > 0 means every V packet saturates deeper-weighted than every M packet.

numpy only, local, no torch. Source: empirical/data/residual_streams_months_*.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "empirical"))
from native_logit_lens_packet_score_layerwise import (  # noqa: E402
    conductor_packets, load_safetensors_first,
)

DATA = ROOT / "empirical" / "data"
REPORTS = ROOT / "empirical" / "reports"
# All checkpoints with captured months residual streams are processed if present.
MODELS = {
    "llama31_8b": "Llama-3.1-8B (base)",
    "llama31_8b_instruct": "Llama-3.1-8B-Instruct",
    "mistral7b_v0_3": "Mistral-7B-v0.3 (base)",
    "mistral7b_v0_3_instruct": "Mistral-7B-Instruct-v0.3",
}
FAMILY = {"llama31_8b": "Llama", "llama31_8b_instruct": "Llama",
          "mistral7b_v0_3": "Mistral", "mistral7b_v0_3_instruct": "Mistral"}
N = 12
V_PACKETS = [2, 3, 4]
M_PACKETS = [6, 12]
N_BOOT = 2000
SEED = 0


def per_example_packet_energy(H, W_U_VR):
    """Return E[ex, layer, packet_d] nontrivial energies (centered logits, unitary FFT)."""
    n, L, d = H.shape
    pk = conductor_packets(N)
    packets = sorted(pk)  # [2,3,4,6,12]
    out = np.zeros((n, L, len(packets)), dtype=np.float64)
    for ell in range(L):
        s = H[:, ell, :].astype(np.float64) @ W_U_VR.T.astype(np.float64)  # [n,N]
        s = s - s.mean(axis=1, keepdims=True)
        coeff = np.fft.fft(s, axis=1) / np.sqrt(N)
        en = np.abs(coeff) ** 2  # [n,N]
        for pi, dd in enumerate(packets):
            out[:, ell, pi] = en[:, pk[dd]].sum(axis=1)
    return out, packets


def sigma_from_energy(E_sub, packets, L):
    """E_sub: [layer, packet] energies averaged over a (resampled) example set."""
    tot = E_sub.sum(axis=1, keepdims=True)            # [L,1] total nontrivial
    f = E_sub / np.clip(tot, 1e-30, None)             # f_{d,ell}, [L,packets]
    ell = np.arange(L)[:, None]
    f_final = f[-1]                                    # [packets]
    sigma = (f * ell / (L - 1)).mean(axis=0) / np.clip(f_final, 1e-30, None)
    return {packets[i]: float(sigma[i]) for i in range(len(packets))}


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    rng = np.random.default_rng(SEED)
    out = {"statistic": "sigma_d (Paper36 §3.A), prompt bootstrap", "n_boot": N_BOOT,
           "V": V_PACKETS, "M": M_PACKETS, "models": {}}

    for tag, pretty in MODELS.items():
        res_path = DATA / f"residual_streams_months_{tag}.safetensors"
        if not res_path.exists():
            continue
        H, _ = load_safetensors_first(str(res_path))
        W_U_VR = np.load(DATA / f"W_U_VR_months_{tag}.npz")["W_U_VR"]
        n, L, _ = H.shape
        E, packets = per_example_packet_energy(H, W_U_VR)   # [n,L,packets]

        point = sigma_from_energy(E.mean(axis=0), packets, L)
        boot = {d: np.zeros(N_BOOT) for d in packets}
        gaps = np.zeros(N_BOOT)
        for b in range(N_BOOT):
            idx = rng.integers(0, n, size=n)               # resample with replacement
            sig = sigma_from_energy(E[idx].mean(axis=0), packets, L)
            for d in packets:
                boot[d][b] = sig[d]
            gaps[b] = min(sig[d] for d in V_PACKETS) - max(sig[d] for d in M_PACKETS)

        def ci(x):
            return [float(np.percentile(x, 2.5)), float(np.percentile(x, 97.5))]

        per_packet = {str(d): {"point": point[d], "boot_mean": float(boot[d].mean()),
                               "ci95": ci(boot[d])} for d in packets}
        # H_2 defector test (Llama): does sigma_2 CI sit above the whole M cluster?
        sig2_above_M = float(np.mean(
            [min(boot[d][b] for d in [2]) > max(boot[m][b] for m in M_PACKETS)
             for b in range(N_BOOT)]))
        res = {
            "n_examples": int(n), "n_layers": int(L),
            "per_packet": per_packet,
            "gap_min_V_minus_max_M": {"point": min(point[d] for d in V_PACKETS) - max(point[d] for d in M_PACKETS),
                                       "boot_mean": float(gaps.mean()), "ci95": ci(gaps),
                                       "P_gap_gt_0": float(np.mean(gaps > 0))},
            "P_sigma2_above_all_M": sig2_above_M,
        }
        out["models"][tag] = res
        print(f"\n# === {pretty} (months, n={n}, {N_BOOT} bootstraps) ===")
        for d in packets:
            grp = "V" if d in V_PACKETS else "M"
            pp = per_packet[str(d)]
            print(f"#  sigma_{d:<2} [{grp}]  point={pp['point']:.4f}  "
                  f"boot {pp['boot_mean']:.4f}  CI95 [{pp['ci95'][0]:.4f}, {pp['ci95'][1]:.4f}]")
        g = res["gap_min_V_minus_max_M"]
        print(f"#  gap = min(σ_V) - max(σ_M): point={g['point']:.4f}  "
              f"CI95 [{g['ci95'][0]:.4f}, {g['ci95'][1]:.4f}]  P(gap>0)={g['P_gap_gt_0']:.3f}")
        print(f"#  P(σ_2 > all M)  (Llama H_2-defector test) = {sig2_above_M:.3f}")

    # ---- cross-checkpoint robustness summary (weight variance) ----
    tags = list(out["models"].keys())
    if len(tags) > 1:
        gaps_pt = {t: out["models"][t]["gap_min_V_minus_max_M"]["point"] for t in tags}
        pgt0 = {t: out["models"][t]["gap_min_V_minus_max_M"]["P_gap_gt_0"] for t in tags}
        kbranch_all = all(g > 0 for g in gaps_pt.values())
        sig_all = all(p >= 0.975 for p in pgt0.values())
        out["cross_checkpoint"] = {
            "checkpoints": tags, "families": {t: FAMILY[t] for t in tags},
            "gap_point_per_checkpoint": gaps_pt,
            "P_gap_gt_0_per_checkpoint": pgt0,
            "gap_range": [min(gaps_pt.values()), max(gaps_pt.values())],
            "K_branch_on_all": bool(kbranch_all),
            "significant_on_all": bool(sig_all),
        }
        print("\n# === CROSS-CHECKPOINT (weight variance) ===")
        for t in tags:
            print(f"#  {MODELS[t]:<28} gap={gaps_pt[t]:+.4f}  P(gap>0)={pgt0[t]:.3f}  [{FAMILY[t]}]")
        print(f"#  K-branch (gap>0) on ALL {len(tags)} checkpoints: {kbranch_all}; "
              f"significant on all: {sig_all}; gap range [{min(gaps_pt.values()):.3f}, {max(gaps_pt.values()):.3f}]")

    (REPORTS / "vm_bootstrap_significance.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\n# wrote {REPORTS / 'vm_bootstrap_significance.json'}")


if __name__ == "__main__":
    main()
