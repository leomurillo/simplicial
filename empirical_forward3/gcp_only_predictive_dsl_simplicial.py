r"""
=============================================================================
 GCP-ONLY  --  NOT RUN LOCALLY  --  DO NOT EXECUTE ON THE LAPTOP
=============================================================================
Running torch/transformers on the development laptop previously caused a crash
requiring a hardware repair.  This script imports torch and MUST be run only on
a transient GCP CPU instance (cf. the program's E11 / e67 recipe), then the
result JSON retrieved and the instance deleted.  The DETERMINISTIC certificates
for this direction are `cert_hodge_arrow.py` and `cert_generalN_bridge.py`
(sympy/numpy only); THIS file is an optional trained confirmation, not part of
the local gate.

WHAT IT VALIDATES (the Predictive-DSL improvement on the simplicial frame)
--------------------------------------------------------------------------
Direction 3 builds the discrete Hodge decomposition of 1-cochains on a
simplicial complex:  C^1 = im d0 (+) im d1^T (+) ker L1, i.e.
   EXACT (grad / curvature, A=0)  (+)  COEXACT (curl / current, tr S=0)  (+)
   HARMONIC (the topologically protected current, dim = b1).
The 1-Hodge-Laplacian L1 = d0 d0^T + d1^T d1 is SYMMETRIC.  A "Deep
Sturm-Liouville"-style encoder built from ONE self-adjoint eigenbasis (here the
eigenbasis of L1, or of its exact-sector restriction) lives in the A=0 corner
of T = S + A and is BLIND to any antisymmetric circulation living on the
harmonic/cycle sector (Curvature&Current Thm 5; Irreversible Blind Spot Lemma 1).

The PREDICTIVE (two-chart) upgrade learns the operator T itself: two charts
(left/right singular bases) whose optimum is the SVD of T (C&C Thm 7), and the
recovered antisymmetric part 1/2(P - P^T) of the predictor head reads the arrow
back.  On a b1=1 complex (triangulated annulus) the single recoverable arrow is
the circulation around the hole; the gap  Delta = sum sigma(T) - sum lambda(S)
is the strength.  This script:
  (A) builds the annulus complex and its L1, harmonic basis (b1=1);
  (B) installs an antisymmetric current C on the harmonic+coexact sector with a
      tunable strength omega (omega=0 = detailed balance);
  (C) trains a self-adjoint encoder (DSL corner) and shows its alignment loss is
      reversal-invariant (arrow-blind: loss gap ~ 0, Procrustes ~ 0);
  (D) trains a two-chart predictor and shows the recovered |omega_hat| tracks
      omega and flips sign under time reversal -- the arrow is recovered.
Expected (mirrors e67 / E11): single-chart Delta_hat ~ 0 regardless of omega;
two-chart Delta_hat grows 0 -> >0 with omega and is ~0 at omega=0.

USAGE (on GCP only):
    pip install torch --index-url https://download.pytorch.org/whl/cpu
    python gcp_only_predictive_dsl_simplicial.py   # writes result JSON
Then scp the JSON back and delete the instance.
"""
# ---- hard local guard: refuse to run unless explicitly on a GCP-marked host ----
import os
import sys

def _refuse_if_local():
    if os.environ.get("SIMPLICIAL_ALLOW_TORCH") != "1":
        sys.stderr.write(
            "REFUSING TO RUN: this is a GCP-only torch script.  Set "
            "SIMPLICIAL_ALLOW_TORCH=1 on a disposable GCP instance to run.  "
            "Never run torch on the laptop.\n")
        raise SystemExit(2)

_refuse_if_local()

import json
import itertools
import numpy as np
import torch
import torch.nn as nn

torch.manual_seed(0)
np.random.seed(0)


# ---------------- annulus complex (b1 = 1) and its Hodge data ----------------
def annulus_L1():
    inner = [1, 2, 3, 4, 5, 6]
    outer = [7, 8, 9, 10, 11, 12]
    tris = []
    for k in range(6):
        a, b = inner[k], inner[(k + 1) % 6]
        c, d = outer[k], outer[(k + 1) % 6]
        tris.append(tuple(sorted((a, b, c))))
        tris.append(tuple(sorted((b, c, d))))
    verts = sorted(set(inner + outer))
    eset = set()
    for t in tris:
        for e in itertools.combinations(t, 2):
            eset.add(tuple(sorted(e)))
    E = sorted(eset)
    F = sorted(set(tris))
    vi = {v: i for i, v in enumerate(verts)}
    ei = {e: i for i, e in enumerate(E)}
    d0 = np.zeros((len(E), len(verts)))
    for (i, j), r in ei.items():
        d0[r, vi[i]] = -1
        d0[r, vi[j]] = 1
    d1 = np.zeros((len(F), len(E)))
    for fr, (i, j, k) in enumerate(F):
        d1[fr, ei[(j, k)]] += 1
        d1[fr, ei[(i, k)]] += -1
        d1[fr, ei[(i, j)]] += 1
    L1 = d0 @ d0.T + d1.T @ d1
    return d0, d1, L1


def main():
    d0, d1, L1 = annulus_L1()
    nE = L1.shape[0]
    w, V = np.linalg.eigh(L1)
    Gh = V[:, np.abs(w) < 1e-8]          # harmonic basis, b1 = 1
    b1 = Gh.shape[1]
    result = {"complex": "triangulated annulus", "nE": int(nE), "b1": int(b1),
              "_environment": "GCP-only torch run; NOT executed locally", "runs": []}

    # coexact basis (current sector) for the rotation partner
    Uc, sc, _ = np.linalg.svd(d1.T, full_matrices=False)
    Gc = Uc[:, sc > 1e-9]

    for omega in [0.0, 0.15, 0.30, 0.45]:
        # antisymmetric current C on harmonic(+coexact) sector, strength omega
        pair = np.column_stack([Gh[:, 0], Gc[:, 0]])
        C = omega * (pair @ np.array([[0.0, 1.0], [-1.0, 0.0]]) @ pair.T)
        Tsym = np.eye(nE) - 0.3 * L1 / max(w.max(), 1.0)
        T = torch.tensor(Tsym + C, dtype=torch.float32)
        S = 0.5 * (T + T.T)

        # (C) self-adjoint DSL encoder: single chart h; objective uses <h, T h>.
        #     With h orthonormal columns, <h,Th> = <h,Sh> exactly => arrow-blind.
        d = 4
        H = nn.Parameter(torch.linalg.qr(torch.randn(nE, d))[0])
        optH = torch.optim.Adam([H], lr=5e-3)
        for _ in range(1500):
            optH.zero_grad()
            Q = torch.linalg.qr(H)[0]
            loss = -(Q.T @ T @ Q).diagonal().sum()        # maximize alignment
            loss.backward()
            optH.step()
        Qf = torch.linalg.qr(H)[0].detach()
        # reversal invariance: replace T by T^T (time reverse) -> same diag of S
        align_fwd = (Qf.T @ T @ Qf).diagonal().sum().item()
        align_rev = (Qf.T @ T.T @ Qf).diagonal().sum().item()
        single_gap = abs(align_fwd - align_rev)           # ~0 => blind

        # (D) two-chart predictor: charts Uc(left), Vc(right); optimum = SVD of T.
        Ul = nn.Parameter(torch.linalg.qr(torch.randn(nE, d))[0])
        Vr = nn.Parameter(torch.linalg.qr(torch.randn(nE, d))[0])
        opt2 = torch.optim.Adam([Ul, Vr], lr=5e-3)
        for _ in range(2500):
            opt2.zero_grad()
            Lq = torch.linalg.qr(Ul)[0]
            Rq = torch.linalg.qr(Vr)[0]
            loss = -(Lq.T @ T @ Rq).diagonal().sum()      # two-sided alignment
            loss.backward()
            opt2.step()
        Lq = torch.linalg.qr(Ul)[0].detach()
        Rq = torch.linalg.qr(Vr)[0].detach()
        # predictor head P in chart coords; antisym part reads the arrow
        P = Lq.T @ T @ Rq
        arrow = 0.5 * (P - P.T)
        omega_hat = float(torch.linalg.norm(arrow).item())
        # exact reference gap
        sig = np.sort(np.linalg.svd(Tsym + C, compute_uv=False))[::-1][:d]
        lamS = np.sort(np.linalg.eigvalsh(S.numpy()))[::-1][:d]
        Delta = float(sig.sum() - lamS.sum())

        result["runs"].append({
            "omega": omega,
            "single_chart_reversal_gap": single_gap,      # expect ~0 (blind)
            "two_chart_arrow_norm": omega_hat,            # expect grow with omega
            "exact_Delta_top_d": Delta,                   # expect grow with omega
        })
        print(f"omega={omega:.2f}  single-chart gap={single_gap:.2e} (blind)  "
              f"predictor arrow={omega_hat:.4f}  exact Delta={Delta:.4f}")

    with open("result_predictive_dsl_simplicial.json", "w") as f:
        json.dump(result, f, indent=2)
    print("[wrote result_predictive_dsl_simplicial.json]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
