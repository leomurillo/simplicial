"""
A4 -- DARK STRUCTURE IN REPRESENTATIONS, on real transformer activations.  *** GCP ONLY (torch). ***

Pre-registered prediction (A4, `FALSIFIABLE_PREDICTIONS_REGISTRY.md`):
  Learned representations carry "dark structure": content that drives the OUTPUT (gravitates) but is
  invisible to an order-2 probe. The dark:visible ratio > 1 -- most output-relevant structure is
  order >= 3 (the dark-matter analogue, transplanted to its testable home).

Method: predict a real OUTPUT scalar -- the surprisal of the actual next token, -log p(next) computed
by the model -- from a layer's activations at order m (degree-m polynomial-kernel ridge, CV R^2),
across layers, in the statistically-accessible regime (PCA to d_sub). Define
   visible(L) = R2_2(L)              (what order-2 captures)
   dark(L)    = R2_4(L) - R2_2(L)    (additional output structure needing order 3-4)
   dark:visible(L) = dark(L)/max(visible(L), eps).

Pre-registered verdict:
  CONFIRM  if, in the accessible regime, dark:visible(L) > 1 at early/mid layers (order->=3 output
           structure dominates) AND it decreases toward the final layer (the output linearizes into
           the unembedding -- dark structure lives in the intermediate computation).
  FALSIFY  if order-2 captures the majority everywhere (dark:visible < 1 at all layers and d_sub).

Note (honesty): dark(L) is a LOWER BOUND -- structure of order > 4, or inaccessible at the chosen
d_sub (curse of dimensionality, see _tune_regime.py), is not counted. We report across d_sub so the
trend, not a single number, carries the claim.

Writes results/a4_dark_structure.json.
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

MODEL = os.environ.get("A4_MODEL", "EleutherAI/pythia-410m")   # ungated; override via A4_MODEL
N_TOK = int(os.environ.get("A4_NTOK", "3000"))
D_SUBS = [8, 16, 24]
MS = [1, 2, 3, 4]
LAM = 1e-3
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
    print(f"[A4] model={MODEL} ({nl} layers) layers={LAYERS} n_tok={N_TOK}")
    text = kp.get_corpus()
    acts, surprisal, meta = kp.extract(model, tok, text, layers=LAYERS, max_tokens=N_TOK)
    print(f"[A4] {meta}; surprisal mean={surprisal.mean():.2f} std={surprisal.std():.2f}")
    y = surprisal

    result = {"model": MODEL, "layers": LAYERS, "meta": meta, "target": "next-token surprisal",
              "by_layer": {}}

    best_dv_by_layer = {}
    for L in LAYERS:
        X = acts[L]
        result["by_layer"][str(L)] = {}
        for d_sub in D_SUBS:
            if d_sub > X.shape[1]:
                continue
            Z = kp.pca_reduce(X, d_sub)
            r2 = {m: round(kp.cv_metric(Z, y, m, "reg", lam=LAM, n_splits=4), 4) for m in MS}
            visible = max(r2[2], 1e-6)
            dark = r2[4] - r2[2]
            dv = round(dark / visible, 3)
            result["by_layer"][str(L)][f"d_sub={d_sub}"] = {"R2": r2, "dark": round(dark, 4),
                                                            "visible": round(visible, 4), "dark_visible": dv}
            print(f"[A4] L={L:<2} d_sub={d_sub:<2} R2={r2}  dark:visible={dv}")
        # best (max over d_sub) dark:visible at this layer
        dvs = [v["dark_visible"] for v in result["by_layer"][str(L)].values()]
        best_dv_by_layer[L] = max(dvs) if dvs else 0.0

    # verdict: dark:visible > 1 at an early/mid layer, decreasing toward the last
    early_mid = [best_dv_by_layer[L] for L in LAYERS[:-1]]
    last = best_dv_by_layer[LAYERS[-1]]
    dominates = any(d > 1.0 for d in early_mid)
    decreasing = max(early_mid) > last if early_mid else False
    confirm = dominates and decreasing
    result["best_dark_visible_by_layer"] = {str(L): best_dv_by_layer[L] for L in LAYERS}
    result["verdict"] = "CONFIRM" if confirm else ("PARTIAL" if dominates else "FALSIFY")
    result["verdict_note"] = (
        f"dark:visible>1 at early/mid (max={max(early_mid) if early_mid else 0:.2f}), "
        f"last-layer={last:.2f}; dominates={dominates}, decreasing={decreasing}")

    path = os.path.join(OUTDIR, "a4_dark_structure.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\n[A4] VERDICT: {result['verdict']} -- {result['verdict_note']}")
    print(f"[A4] wrote {path}")


if __name__ == "__main__":
    main()
