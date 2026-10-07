"""
A1-CONTROLS -- is the observed order-k RAMP a product of the layered architecture?   *** GCP ONLY ***

Question (raised 2026-06-25): the ramp (vs the sharp boundary) could be (a) a fundamental property of
correlated representations, or (b) an artifact of the layered NN architecture mixing features. A1
alone cannot tell. Two controls decide it:

  DEPTH SWEEP   -- the SAME imposed order-k behavior, probed at embedding / early / mid / late layers.
                   If the compositional centroid tracks k BETTER at shallow depth and smears with depth,
                   the LAYERING is doing the smearing (hypothesis (b)).
  UNTRAINED     -- identical architecture, RANDOM weights (learned nothing). If the ramp is the SAME as
                   trained, the smearing is pure architectural feature-mixing, NOT learned structure.

Metric: compositional centroid C(k) = sum_m m*dAcc(m)/sum_m dAcc(m) (as in a1_graded). We report, per
condition, the centroids over k and how well they track k (slope of C(k) vs k; ideal independent
features give C(k)=k, slope 1).

Writes results/a1_controls.json.
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
KS = [2, 3, 4]
MS = [1, 2, 3, 4, 5]
N_DRAWS = 6
LAM = 1e-4
OUTDIR = os.path.join(os.path.dirname(__file__), "results")


def centroid(Z, k, seed=0):
    rng = np.random.default_rng(seed)
    d = Z.shape[1]
    cs = []
    for _ in range(N_DRAWS):
        cols = rng.permutation(d)[:k]
        y = np.prod(np.sign(Z[:, cols]), axis=1)
        if not (0.2 < np.mean(y == 1) < 0.8):
            continue
        acc = {0: 0.5}
        for m in MS:
            acc[m] = kp.cv_metric(Z, y, m, "clf", lam=LAM, n_splits=3)
        dacc = np.array([max(0.0, acc[m] - acc[m - 1]) for m in MS])
        if dacc.sum() < 1e-6:
            continue
        cs.append(float(np.sum(np.array(MS) * dacc) / dacc.sum()))
    return round(float(np.mean(cs)), 3) if cs else None


def slope(ks, cs):
    ks = np.array(ks, float); cs = np.array(cs, float)
    return round(float(np.polyfit(ks, cs, 1)[0]), 3)   # 1.0 = perfectly tracks k


def condition(X, label, result):
    cs = [centroid(kp.pca_reduce(X, k + 1), k) for k in KS]
    s = slope(KS, cs)
    result[label] = {"centroids": dict(zip([f"k={k}" for k in KS], cs)), "slope_vs_k": s}
    print(f"[A1c] {label:<16} centroids={cs}  slope_vs_k={s}")
    return s


def main():
    kp.require_gcp()
    os.makedirs(OUTDIR, exist_ok=True)
    result = {"model": MODEL, "metric": "compositional-centroid slope vs k (1.0=tracks k)"}

    print("=== TRAINED: depth sweep ===")
    model, tok = kp.load_model(MODEL)
    nl = model.config.num_hidden_layers
    depth_layers = sorted({0, max(1, round(0.17 * nl)), max(1, round(0.5 * nl)), max(1, round(0.92 * nl))})
    text = kp.get_corpus()
    acts, _, meta = kp.extract(model, tok, text, layers=depth_layers, max_tokens=N_TOK)
    print(f"[A1c] {MODEL} ({nl} layers), depth layers={depth_layers}, {meta}")
    for L in depth_layers:
        tag = "embed" if L == 0 else ("early" if L <= 0.25 * nl else ("mid" if L <= 0.6 * nl else "late"))
        condition(acts[L], f"trained_L{L}_{tag}", result)

    print("=== UNTRAINED (random init): mid layer ===")
    umodel, utok = kp.load_untrained(MODEL)
    mid = max(1, round(0.5 * nl))
    uacts, _, _ = kp.extract(umodel, utok, text, layers=[mid], max_tokens=N_TOK)
    condition(uacts[mid], f"untrained_L{mid}_mid", result)

    # interpretation
    trained_mid = result.get(f"trained_L{mid}_mid", {}).get("slope_vs_k")
    untrained_mid = result.get(f"untrained_L{mid}_mid", {}).get("slope_vs_k")
    embed = result.get("trained_L0_embed", {}).get("slope_vs_k")
    note = []
    if embed is not None and trained_mid is not None:
        note.append(f"depth: slope embed={embed} vs mid={trained_mid} "
                    f"({'sharper shallow -> layering smears' if embed > trained_mid else 'not sharper shallow'})")
    if untrained_mid is not None and trained_mid is not None:
        note.append(f"untrained mid slope={untrained_mid} vs trained mid={trained_mid} "
                    f"({'~same -> architectural mixing, not learned' if abs(untrained_mid-trained_mid) < 0.15 else 'differ -> training shapes it'})")
    result["interpretation"] = "; ".join(note)
    path = os.path.join(OUTDIR, "a1_controls.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\n[A1c] {result['interpretation']}")
    print(f"[A1c] wrote {path}")


if __name__ == "__main__":
    main()
