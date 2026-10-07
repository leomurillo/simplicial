"""
A1-GRADED -- the compositionality tax as a CONTINUOUS effective order.   *** GCP ONLY (torch). ***

The sharp phase boundary (a1_compositionality_tax.py) was FALSIFIED on real Pythia activations: real
PCA coordinates are correlated/asymmetric, so a k-parity of them is NOT orthogonal to lower-order
polynomials and the accuracy RAMPS with probe order instead of stepping. This reformulation keeps the
*surviving* claim and makes it falsifiable:

  REFORMULATED PREDICTION: the COMPOSITIONAL CENTROID -- the order-mass-weighted mean probe order at
  which a behavior's readable signal lives -- increases MONOTONICALLY with the behavior's interaction
  order k. (A graded "effective order", not a threshold.)

    C(k) = sum_m m * dAcc(m) / sum_m dAcc(m),   dAcc(m) = max(0, acc(m) - acc(m-1)),  acc(0)=0.5

Verdict:
  CONFIRM  if C(k) is strictly increasing over k in {2,3,4,5} (Spearman rho = 1, means monotone).
  FALSIFY  if C(k) is flat or non-monotone (the compositionality-tax idea has no graded support either).

Also reports the centroid on ZCA-WHITENED features (decorrelated) as a secondary read -- does removing
order-2 correlation move C(k) closer to k (a sharper boundary)?

Writes results/a1_graded.json.
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

MODEL = os.environ.get("A1_MODEL", "EleutherAI/pythia-410m")
N_TOK = int(os.environ.get("A1_NTOK", "3000"))
KS = [2, 3, 4, 5]
MS = [1, 2, 3, 4, 5]
N_DRAWS = 6
LAM = 1e-4
OUTDIR = os.path.join(os.path.dirname(__file__), "results")


def whiten(Z):
    Zc = Z - Z.mean(0, keepdims=True)
    C = np.cov(Zc, rowvar=False) + 1e-6 * np.eye(Zc.shape[1])
    w, V = np.linalg.eigh(C)
    return Zc @ V @ np.diag(1.0 / np.sqrt(w)) @ V.T          # ZCA whitening


def centroid(Z, k, ms, n_draws, seed=0):
    """mean+/-std of the compositional centroid over random k-subsets of coords."""
    rng = np.random.default_rng(seed)
    d = Z.shape[1]
    cs = []
    curves = []
    for _ in range(n_draws):
        cols = rng.permutation(d)[:k]
        y = np.prod(np.sign(Z[:, cols]), axis=1)
        if not (0.2 < np.mean(y == 1) < 0.8):
            continue
        acc = {0: 0.5}
        for m in ms:
            acc[m] = kp.cv_metric(Z, y, m, "clf", lam=LAM, n_splits=3)
        dacc = np.array([max(0.0, acc[m] - acc[m - 1]) for m in ms])
        if dacc.sum() < 1e-6:
            continue
        c = float(np.sum(np.array(ms) * dacc) / dacc.sum())
        cs.append(c)
        curves.append({m: round(acc[m], 3) for m in ms})
    return (round(float(np.mean(cs)), 3), round(float(np.std(cs)), 3), cs, curves)


def spearman(a, b):
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
    ra = ra - ra.mean(); rb = rb - rb.mean()
    return float(np.sum(ra * rb) / (np.sqrt(np.sum(ra**2) * np.sum(rb**2)) + 1e-12))


def run(X, tag, result):
    cents = []
    for k in KS:
        Z = kp.pca_reduce(X, k + 1)
        if tag == "whitened":
            Z = whiten(Z)
        mean, std, _, curves = centroid(Z, k, MS, N_DRAWS)
        cents.append(mean)
        result.setdefault(tag, {})[f"k={k}"] = {"centroid": mean, "std": std, "example_curve": curves[0] if curves else None}
        print(f"[A1g][{tag}] k={k}  centroid={mean}+/-{std}  curve={curves[0] if curves else None}")
    rho = spearman(KS, cents)
    monotone = all(cents[i] < cents[i + 1] for i in range(len(cents) - 1))
    result[tag]["centroids"] = cents
    result[tag]["spearman_k"] = round(rho, 3)
    result[tag]["monotone"] = bool(monotone)
    return monotone, rho, cents


def main():
    kp.require_gcp()
    os.makedirs(OUTDIR, exist_ok=True)
    model, tok = kp.load_model(MODEL)
    nl = model.config.num_hidden_layers
    LAYER = int(os.environ["A1_LAYER"]) if "A1_LAYER" in os.environ else max(1, round(0.5 * nl))
    print(f"[A1g] model={MODEL} ({nl} layers) layer={LAYER} n_tok={N_TOK}")
    acts, _, meta = kp.extract(model, tok, kp.get_corpus(), layers=[LAYER], max_tokens=N_TOK)
    X = acts[LAYER]
    print(f"[A1g] activations {X.shape}")

    result = {"model": MODEL, "layer": LAYER, "meta": meta, "metric": "compositional centroid"}
    mono_pca, rho_pca, c_pca = run(X, "pca", result)
    mono_w, rho_w, c_w = run(X, "whitened", result)

    result["verdict"] = "CONFIRM" if mono_pca else "FALSIFY"
    result["verdict_note"] = (f"PCA centroids {c_pca} (monotone={mono_pca}, rho={rho_pca}); "
                              f"whitened {c_w} (monotone={mono_w}, rho={rho_w})")
    path = os.path.join(OUTDIR, "a1_graded.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\n[A1g] VERDICT: {result['verdict']} -- {result['verdict_note']}")
    print(f"[A1g] wrote {path}")


if __name__ == "__main__":
    main()
