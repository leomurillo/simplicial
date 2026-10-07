#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CCSAE Phase B -- trained vanilla vs. hard-certified SAE (GCP-only; torch)
========================================================================

Trains a top-k sparse autoencoder on captured Llama-3.1-8B months activations in
three variants -- vanilla, certified at S={12}, certified at S=full {2,3,4,6,12} --
and tests Paper 45 P1 (packet purity survives training) and P3 (trained
reconstruction gap matches the obstruction floor delta_S within 10%).

The certified variant projects decoder columns AND the pre-bias through
(I - pi^+(I-P_S)pi) after every optimizer step (Paper 45 sec 3.2 + sec 9.3:
parameter projected post-step, Adam moments untouched), then renormalizes columns.

Reconstruction is evaluated IN THE CYCLIC READOUT pi(h) = center(W_U_VR h), where
Theorem 4.2 lives: a certified decoder's image lies in (+)_{d in S} H_d, so its
per-example cyclic reconstruction error is floored at delta_S; a vanilla decoder can
represent all packets, so its cyclic error -> 0.  The gap = certified - vanilla
cyclic error should equal delta_S.

NEVER run locally (torch). Run on the GCP L4 only.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def load_safetensors_acts(path: str):
    import struct
    import numpy as np
    with open(path, "rb") as f:
        hl = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(hl))
        data = f.read()
    key = [k for k in header if k != "__metadata__"][0]
    meta = header[key]
    s, e = meta["data_offsets"]
    raw = np.frombuffer(data[s:e], dtype=np.uint16).copy()  # BF16
    out = np.zeros(raw.size, dtype=np.uint32)
    out |= raw.astype(np.uint32) << 16
    return out.view(np.float32).reshape(meta["shape"]).copy()


def conductor_packets(n: int):
    out = {}
    for d in [x for x in range(1, n + 1) if n % x == 0]:
        chars = [k for k in range(1, n) if n // math.gcd(n, k) == d]
        if chars:
            out[d] = chars
    return out


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    import numpy as np
    import torch

    ap = argparse.ArgumentParser()
    ap.add_argument("--acts", default="empirical/data/ccsae_corpus_months_llama31_8b.safetensors")
    ap.add_argument("--wu", default="empirical/data/ccsae_corpus_months_llama31_8b_WU.npz")
    ap.add_argument("--layer-index", type=int, default=0, help="index into the kept-layers axis (0 = first kept, default row 30)")
    ap.add_argument("--N", type=int, default=12)
    ap.add_argument("--width", type=int, default=1024)
    ap.add_argument("--k", type=int, default=32)
    ap.add_argument("--steps", type=int, default=4000)
    ap.add_argument("--batch", type=int, default=256)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="empirical/reports/ccsae_train_months_llama31_8b.json")
    args = ap.parse_args()

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    torch.manual_seed(args.seed)
    N = args.N

    acts_np = load_safetensors_acts(args.acts)          # [M, L_keep, d]
    H = torch.tensor(acts_np[:, args.layer_index, :], dtype=torch.float32, device=dev)  # [M, d]
    M, d = H.shape
    W_U_VR = torch.tensor(np.load(args.wu)["W_U_VR"], dtype=torch.float32, device=dev)  # [N, d]
    print(f"# corpus M={M}, d={d}, layer-index={args.layer_index}, width={args.width}, k={args.k}")

    # cyclic readout pi = C @ W_U_VR ; packet projections in the character basis
    C = torch.eye(N, device=dev) - torch.ones((N, N), device=dev) / N
    pi = C @ W_U_VR                                      # [N, d]
    pi_pinv = torch.linalg.pinv(pi)                      # [d, N]
    a = torch.arange(N, device=dev)
    U = torch.exp(-2j * math.pi * a[:, None] * a[None, :] / N) / math.sqrt(N)  # [N,N] complex
    pk = conductor_packets(N)

    def P_support(S):
        A = sorted({c for dd in S for c in pk.get(dd, [])})
        UA = U[A, :]
        P = (UA.conj().T @ UA).real.to(torch.float32)   # [N,N]
        return P

    SUPPORTS = {"vanilla": None, "cert_S12": [12], "cert_Sfull": [2, 3, 4, 6, 12]}

    # delta_S target (certificate quantity) on this corpus/layer
    s_all = (H @ W_U_VR.T)                               # [M, N]
    s_c = (C @ s_all.T).T                                # centered per example
    E_total = (s_c ** 2).sum(dim=1).mean().item()
    delta = {}
    for name, S in SUPPORTS.items():
        if S is None:
            continue
        P = P_support(S)
        resid = s_c - (P @ s_c.T).T
        delta[name] = (resid ** 2).sum(dim=1).mean().item() / E_total
    print(f"# delta_S target (cyclic out-of-support fraction): "
          f"S12={delta['cert_S12']:.6f}  Sfull={delta['cert_Sfull']:.6e}")

    def cert_matrix(S):
        P = P_support(S)
        Q = pi_pinv @ ((torch.eye(N, device=dev) - P) @ pi)   # [d,d]
        return torch.eye(d, device=dev) - Q                   # apply to W_d cols + b_pre

    def train(name, S):
        g = torch.Generator(device=dev).manual_seed(args.seed)
        b_pre = H.mean(dim=0).clone()
        W_e = torch.randn(args.width, d, generator=g, device=dev) * (1.0 / math.sqrt(d))
        W_d = torch.randn(d, args.width, generator=g, device=dev) * (1.0 / math.sqrt(args.width))
        W_d = W_d / W_d.norm(dim=0, keepdim=True)
        b_pre.requires_grad_(True); W_e.requires_grad_(True); W_d.requires_grad_(True)
        opt = torch.optim.Adam([b_pre, W_e, W_d], lr=args.lr)
        Mc = cert_matrix(S) if S is not None else None
        if Mc is not None:  # certify initial decoder + pre-bias
            with torch.no_grad():
                W_d.copy_(Mc @ W_d); W_d /= W_d.norm(dim=0, keepdim=True)
                b_pre.copy_(Mc @ b_pre)
        for step in range(args.steps):
            idx = torch.randint(0, M, (args.batch,), generator=g, device=dev)
            h = H[idx]
            pre = h - b_pre
            z = W_e @ pre.T                               # [F, B]
            topv, topi = torch.topk(z, args.k, dim=0)
            topv = torch.relu(topv)
            zsp = torch.zeros_like(z).scatter(0, topi, topv)
            hhat = b_pre[None, :] + (W_d @ zsp).T          # [B, d]
            loss = ((h - hhat) ** 2).sum(dim=1).mean()
            opt.zero_grad(); loss.backward(); opt.step()
            with torch.no_grad():
                if Mc is not None:                         # parameter projection post-step
                    W_d.copy_(Mc @ W_d); b_pre.copy_(Mc @ b_pre)
                W_d /= W_d.norm(dim=0, keepdim=True).clamp_min(1e-8)
        # eval on full corpus
        with torch.no_grad():
            pre = H - b_pre
            z = W_e @ pre.T
            topv, topi = torch.topk(z, args.k, dim=0)
            topv = torch.relu(topv)
            zsp = torch.zeros_like(z).scatter(0, topi, topv)
            Hhat = b_pre[None, :] + (W_d @ zsp).T
            fvu = ((H - Hhat) ** 2).sum(dim=1).mean().item() / (H - H.mean(0)).pow(2).sum(1).mean().item()
            # cyclic readout recon error fraction
            ph = (C @ (H @ W_U_VR.T).T).T
            phat = (C @ (Hhat @ W_U_VR.T).T).T
            cyc_err = ((ph - phat) ** 2).sum(dim=1).mean().item() / E_total
            # P1 leakage: forbidden cyclic content of the reconstruction
            if S is not None:
                P = P_support(S)
                leak = (phat - (P @ phat.T).T).pow(2).sum(1).sqrt() / phat.pow(2).sum(1).sqrt().clamp_min(1e-9)
                leak = float(leak.max())
            else:
                leak = None
        return {"name": name, "support": S, "final_loss": loss.item(), "fvu_full_h": fvu,
                "cyclic_recon_err_frac": cyc_err, "p1_max_forbidden_leak": leak}

    results = {}
    for name, S in SUPPORTS.items():
        print(f"# training {name} ...")
        results[name] = train(name, S)
        r = results[name]
        print(f"#   {name}: FVU(full h)={r['fvu_full_h']:.4f}  cyclic_err_frac={r['cyclic_recon_err_frac']:.6f}"
              + (f"  P1 leak={r['p1_max_forbidden_leak']:.2e}" if r['p1_max_forbidden_leak'] is not None else ""))

    # P3: gap = certified - vanilla cyclic error == delta_S within 10%
    van = results["vanilla"]["cyclic_recon_err_frac"]
    p3 = {}
    for name in ["cert_S12", "cert_Sfull"]:
        gap = results[name]["cyclic_recon_err_frac"] - van
        tgt = delta[name]
        rel = abs(gap - tgt) / tgt if tgt > 1e-6 else abs(gap)
        p3[name] = {"measured_gap": gap, "delta_S_target": tgt, "rel_err": rel,
                    "within_10pct": (rel <= 0.10 if tgt > 1e-6 else gap <= 0.02)}
        print(f"# P3 {name}: gap={gap:.6f}  delta_S={tgt:.6f}  rel_err={rel:.3f}  "
              f"-> {'PASS' if p3[name]['within_10pct'] else 'CHECK'}")

    out = {"config": vars(args), "M": M, "d": d, "delta_S_target": delta,
           "vanilla_cyclic_err": van, "results": results, "P3": p3}
    Path(args.out).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"# wrote {args.out}")


if __name__ == "__main__":
    main()
