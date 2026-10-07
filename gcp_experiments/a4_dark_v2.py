"""
A4-v2 -- DARK STRUCTURE via a regularized ALL-ORDER probe.   *** GCP ONLY (torch). ***

A4 v1 was INCONCLUSIVE: the explicit degree-4 polynomial kernel overfit (negative held-out R^2), so
it could not measure order->=3 structure. This version replaces it with an RBF (Gaussian) kernel --
all-order but smoothly regularized (lam selected by CV over a grid that includes large lam), so it
captures higher-order structure WITHOUT the degree-4 blow-up.

  visible(L) = R2_poly2(L)                        (order-2 readable output structure)
  total(L)   = R2_rbf(L)                          (all-order readable output structure)
  dark(L)    = R2_rbf(L) - R2_poly2(L)            (output structure beyond order 2)
  dark:visible(L) = dark(L)/max(visible(L), eps)

Target: next-token surprisal (a real output the model computes). Same lam-selection is applied to
poly2 and rbf, so the optimism cancels in the difference.

Verdict:
  CONFIRM  if dark:visible(L) > 0 meaningfully (RBF beats poly-2 -> genuine order->=3 output structure),
           strongest at early/mid layers and shrinking toward the last layer (output linearizes).
  FALSIFY  if RBF does not beat poly-2 anywhere (dark <= 0): order-2 is sufficient for the output.

Honesty: this is a PREDICTIVE (dependence) measure, not strictly causal; a Gaussian-surrogate causal
test is the next refinement. Writes results/a4_dark_v2.json.
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

MODEL = os.environ.get("A4_MODEL", "EleutherAI/pythia-410m")
N_TOK = int(os.environ.get("A4_NTOK", "3500"))
D_SUB = int(os.environ.get("A4_DSUB", "32"))
OUTDIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    kp.require_gcp()
    os.makedirs(OUTDIR, exist_ok=True)
    model, tok = kp.load_model(MODEL)
    nl = model.config.num_hidden_layers
    if "A4_LAYERS" in os.environ:
        LAYERS = [int(x) for x in os.environ["A4_LAYERS"].split(",")]
    else:
        LAYERS = sorted({max(1, min(nl, round(f * nl))) for f in (0.15, 0.4, 0.65, 0.9)})
    print(f"[A4v2] model={MODEL} ({nl} layers) layers={LAYERS} d_sub={D_SUB} n_tok={N_TOK}")
    acts, surprisal, meta = kp.extract(model, tok, kp.get_corpus(), layers=LAYERS, max_tokens=N_TOK)
    y = surprisal
    print(f"[A4v2] {meta}; surprisal mean={y.mean():.2f} std={y.std():.2f}")

    result = {"model": MODEL, "layers": LAYERS, "d_sub": D_SUB, "meta": meta,
              "target": "next-token surprisal", "by_layer": {}}
    dv_by_layer = {}
    for L in LAYERS:
        Z = kp.pca_reduce(acts[L], min(D_SUB, acts[L].shape[1]))
        Zs = (Z - Z.mean(0)) / (Z.std(0) + 1e-8)            # standardize for RBF
        gamma = kp.median_gamma(Zs)
        r2_p1 = kp.cv_reg_best(Zs, y, lambda A, B: kp.poly_gram(kp.unit_normalize(A), kp.unit_normalize(B), 1))
        r2_p2 = kp.cv_reg_best(Zs, y, lambda A, B: kp.poly_gram(kp.unit_normalize(A), kp.unit_normalize(B), 2))
        r2_rbf = kp.cv_reg_best(Zs, y, lambda A, B: kp.rbf_gram(A, B, gamma))
        visible = max(r2_p2, 1e-6)
        dark = r2_rbf - r2_p2
        dv = round(dark / visible, 3)
        dv_by_layer[L] = dv
        result["by_layer"][str(L)] = {"R2_poly1": round(r2_p1, 4), "R2_poly2": round(r2_p2, 4),
                                      "R2_rbf": round(r2_rbf, 4), "dark": round(dark, 4),
                                      "dark_visible": dv}
        print(f"[A4v2] L={L:<2} poly1={r2_p1:.3f} poly2={r2_p2:.3f} rbf={r2_rbf:.3f} "
              f"dark={dark:+.3f} dark:visible={dv}")

    early_mid = [dv_by_layer[L] for L in LAYERS[:-1]]
    last = dv_by_layer[LAYERS[-1]]
    dominates = any(d > 0.0 for d in early_mid)
    decreasing = (max(early_mid) > last) if early_mid else False
    result["dark_visible_by_layer"] = {str(L): dv_by_layer[L] for L in LAYERS}
    result["verdict"] = "CONFIRM" if (dominates and decreasing) else ("PARTIAL" if dominates else "FALSIFY")
    result["verdict_note"] = (f"RBF beats poly2 at early/mid (max dark:visible={max(early_mid) if early_mid else 0:.2f}), "
                              f"last-layer={last:.2f}; dominates={dominates}, decreasing={decreasing}")
    path = os.path.join(OUTDIR, "a4_dark_v2.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\n[A4v2] VERDICT: {result['verdict']} -- {result['verdict_note']}")
    print(f"[A4v2] wrote {path}")


if __name__ == "__main__":
    main()
