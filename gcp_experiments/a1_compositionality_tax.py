"""
A1 -- THE COMPOSITIONALITY TAX, on real transformer activations.   *** GCP ONLY (torch). ***

Pre-registered prediction (A1, `FALSIFIABLE_PREDICTIONS_REGISTRY.md`):
  An order-m probe is faithful to an order-k behavior IFF m >= k -- a sharp PHASE BOUNDARY, not a
  gradient; the compositionality tax tau(k) = k (the order at which faithfulness saturates).

Method: extract GPT-2 activations at a layer; PCA-reduce to d_sub dims (the statistically-accessible
regime; see _tune_regime.py); define an order-k behavior as the parity of the top-k PCA coordinates
(a genuine degree-k function of the REAL activation values); probe with degree-m polynomial kernels
(m=1..4). Two reads:
  (CAL)  calibration at small d_sub=k+1: is the boundary sharp and tau(k)=k?  -> the pre-registered test.
  (DEG)  sweep d_sub up: the boundary degrades -> the practical faithfulness obstruction (a 2nd finding).

Pre-registered verdict:
  CONFIRM  if at d_sub=k+1, for every k in {2,3,4}: acc(m<k) <= 0.65, acc(m>=k) >= 0.80, a single
           0->1 step (tau(k)=k).
  FALSIFY  if any k shows a gradient (no sharp step) or tau(k) != k in the accessible regime.

Writes results/a1_compositionality_tax.json.
"""
import os
import sys
import json
import numpy as np
import kernel_probe as kp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MODEL = os.environ.get("A1_MODEL", "EleutherAI/pythia-410m")   # ungated; override via A1_MODEL
N_TOK = int(os.environ.get("A1_NTOK", "2500"))
KS = [2, 3, 4]
MS = [1, 2, 3, 4]
N_FEATURE_DRAWS = 4                                    # error bars over which PCA coords are "the features"
LAM = 1e-4
OUTDIR = os.path.join(os.path.dirname(__file__), "results")


def acc_matrix(Z, k, ms, n_draws):
    """Mean+/-std accuracy over n_draws random orderings of which coords form the k-parity."""
    rng = np.random.default_rng(0)
    d = Z.shape[1]
    out = {m: [] for m in ms}
    for _ in range(n_draws):
        cols = rng.permutation(d)[:k]
        y = np.prod(np.sign(Z[:, cols]), axis=1)
        if np.mean(y == 1) < 0.2 or np.mean(y == 1) > 0.8:   # skip degenerate (imbalanced) draws
            continue
        for m in ms:
            out[m].append(kp.cv_metric(Z, y, m, "clf", lam=LAM, n_splits=3))
    return {m: (round(float(np.mean(v)), 3), round(float(np.std(v)), 3)) for m, v in out.items() if v}


def main():
    kp.require_gcp()
    os.makedirs(OUTDIR, exist_ok=True)
    model, tok = kp.load_model(MODEL)
    nl = model.config.num_hidden_layers
    LAYER = int(os.environ["A1_LAYER"]) if "A1_LAYER" in os.environ else max(1, round(0.5 * nl))
    print(f"[A1] model={MODEL} ({nl} layers) layer={LAYER} n_tok={N_TOK}")
    text = kp.get_corpus()
    acts, _, meta = kp.extract(model, tok, text, layers=[LAYER], max_tokens=N_TOK)
    X = acts[LAYER]
    print(f"[A1] activations {X.shape}; {meta}")

    result = {"model": MODEL, "layer": LAYER, "meta": meta, "calibration": {}, "degradation": {}}

    # (CAL) calibration: d_sub = k+1, the accessible regime -- the pre-registered test
    confirm = True
    for k in KS:
        Z = kp.pca_reduce(X, k + 1)
        am = acc_matrix(Z, k, MS, N_FEATURE_DRAWS)
        means = {m: am[m][0] for m in am}
        tau = next((m for m in MS if means.get(m, 0) >= 0.75), None)
        below = max(means.get(m, 0) for m in MS if m < k) if k > 1 else 0.5
        sharp = (means.get(k, 0) >= 0.80) and (below <= 0.65) and (tau == k)
        confirm = confirm and sharp
        result["calibration"][f"k={k}"] = {"d_sub": k + 1, "acc": am, "tau": tau, "sharp": bool(sharp)}
        print(f"[A1][CAL] k={k} d_sub={k+1}  acc={means}  tau={tau}  sharp={sharp}")

    # (DEG) degradation sweep: fix k=3, grow d_sub -> boundary washes out (the practical obstruction)
    for d_sub in [3, 5, 8, 16, 32]:
        if d_sub > X.shape[1]:
            continue
        Z = kp.pca_reduce(X, d_sub)
        am = acc_matrix(Z, 3, MS, N_FEATURE_DRAWS)
        means = {m: am[m][0] for m in am}
        result["degradation"][f"d_sub={d_sub}"] = {"k": 3, "acc": am}
        print(f"[A1][DEG] k=3 d_sub={d_sub:<3} acc={means}  jump@3={means.get(3,0)-means.get(2,0):+.2f}")

    result["verdict"] = "CONFIRM" if confirm else "FALSIFY"
    result["verdict_note"] = ("sharp phase boundary tau(k)=k at d_sub=k+1 for all k"
                              if confirm else "boundary not sharp / tau!=k in accessible regime")
    path = os.path.join(OUTDIR, "a1_compositionality_tax.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\n[A1] VERDICT: {result['verdict']} -- {result['verdict_note']}")
    print(f"[A1] wrote {path}")


if __name__ == "__main__":
    main()
