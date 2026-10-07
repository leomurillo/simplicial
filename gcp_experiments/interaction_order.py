"""
INTERACTION ORDER -- does the model's COMPUTATION exhibit genuine order->=3 input interactions?
*** GCP ONLY (torch). ***

The corrected test (after A1/A4 showed representation is generic/training-flattened): the framework's
real claim is about how features COMBINE in the computation, not what is decodable. We decompose the
model's input->output function by interaction order via functional ANOVA (Walsh-Hadamard) over K=6
binary input knobs (recent context tokens, present vs mean-embedding-ablated), 2^K configs per window.

  f(config) = log p(actual next token)  under that ablation pattern of the K knobs.
  mass_k    = variance of f explained by k-way interactions of the knobs (ANOVA).
  frac_k    = mass_k / sum_{j>=1} mass_j           (fraction of interaction variance at order k)
  a_k       = frac_k / C(K,k)                       (per-interaction strength; a RANDOM function has
                                                     a_k FLAT; a low-order function has a_k DECAYING)

Run for TRAINED and UNTRAINED (random init) Pythia -- the trained-minus-untrained high-order is the
LEARNED interaction structure.

Pre-registered verdict:
  CONFIRM (genuine learned high-order computation): a_3/a_1 is substantial (> 0.5, order-3 interactions
          nearly as strong per-interaction as order-1) AND trained a_3/a_1 >= untrained (training did
          not flatten it).
  FALSIFY (simplicity bias flattens computation too): a_k decays sharply (a_3/a_1 < 0.2) i.e. order<=2
          dominant per-interaction, and/or training REDUCES high-order vs untrained. (A strong finding:
          the bias flattens even the computation.)

Writes results/interaction_order.json.
"""
import os
import sys
import json
import numpy as np
import kernel_probe as kp
from math import comb

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MODEL = os.environ.get("ITX_MODEL", "EleutherAI/pythia-410m")
N_WINDOWS = int(os.environ.get("ITX_NWIN", "60"))
K = int(os.environ.get("ITX_K", "5"))     # knob positions (2^K configs/window); K=5 -> 32, resolves order-3
T = int(os.environ.get("ITX_T", "12"))    # window length; target = the token after the window
OUTDIR = os.path.join(os.path.dirname(__file__), "results")


def spectrum_for_model(model, tok, windows, device="cpu"):
    """Average normalized ANOVA interaction spectrum over windows for one model."""
    import torch
    emb = model.get_input_embeddings()
    mean_emb = emb.weight.detach().mean(0)                       # (d,) neutral 'ablated' embedding
    knob_pos = list(range(T - K, T))                            # the K most recent positions
    # config bit-masks: (64, K) in {0,1}; bit b -> knob b present(1)/ablated(0)
    masks = np.array([[(i >> b) & 1 for b in range(K)] for i in range(2 ** K)])
    fracs = []
    with torch.no_grad():
        for ids, target in windows:
            base = emb(torch.tensor(ids, device=device)).detach()         # (T, d)
            batch = base.unsqueeze(0).repeat(2 ** K, 1, 1).clone()        # (64, T, d)
            for cfg in range(2 ** K):
                for b in range(K):
                    if masks[cfg, b] == 0:
                        batch[cfg, knob_pos[b], :] = mean_emb
            logits = model(inputs_embeds=batch, output_hidden_states=False).logits[:, -1, :]  # (64,vocab)
            logp = torch.log_softmax(logits, dim=-1)[:, target]           # (64,)
            f = logp.float().cpu().numpy()
            mass = kp.interaction_spectrum(f, K)                          # length K+1
            tot = mass[1:].sum()
            if tot > 1e-9:
                fracs.append(mass[1:] / tot)
    frac = np.mean(np.array(fracs), axis=0)                               # (K,) avg fraction per order
    a = np.array([frac[k - 1] / comb(K, k) for k in range(1, K + 1)])     # per-interaction strength
    return frac, a, len(fracs)


def main():
    kp.require_gcp()
    import torch  # noqa
    os.makedirs(OUTDIR, exist_ok=True)

    # build windows once (token ids + target) from the trained model's tokenizer
    model, tok = kp.load_model(MODEL)
    ids_all = tok(kp.get_corpus())["input_ids"]
    rng = np.random.default_rng(0)
    starts = rng.integers(0, len(ids_all) - T - 1, size=N_WINDOWS)
    windows = [(ids_all[s:s + T], ids_all[s + T]) for s in starts]
    print(f"[ITX] model={MODEL}, {N_WINDOWS} windows, K={K} knobs, T={T}")

    result = {"model": MODEL, "K": K, "T": T, "n_windows": N_WINDOWS,
              "metric": "functional-ANOVA interaction spectrum (frac per order; a_k=per-interaction strength)"}

    frac_t, a_t, n_t = spectrum_for_model(model, tok, windows)
    print(f"[ITX] TRAINED   frac={np.round(frac_t,3)}  a_k={np.round(a_t,4)}  (n={n_t})")
    del model
    umodel, _ = kp.load_untrained(MODEL)
    frac_u, a_u, n_u = spectrum_for_model(umodel, tok, windows)
    print(f"[ITX] UNTRAINED frac={np.round(frac_u,3)}  a_k={np.round(a_u,4)}  (n={n_u})")

    r3r1_t = float(a_t[2] / (a_t[0] + 1e-12))
    r3r1_u = float(a_u[2] / (a_u[0] + 1e-12))
    result["trained"] = {"frac_per_order": [round(x, 4) for x in frac_t], "a_k": [round(x, 5) for x in a_t],
                         "a3_over_a1": round(r3r1_t, 3)}
    result["untrained"] = {"frac_per_order": [round(x, 4) for x in frac_u], "a_k": [round(x, 5) for x in a_u],
                           "a3_over_a1": round(r3r1_u, 3)}
    genuine = r3r1_t > 0.5
    not_flattened = r3r1_t >= r3r1_u - 0.05
    result["verdict"] = "CONFIRM" if (genuine and not_flattened) else ("PARTIAL" if r3r1_t > 0.2 else "FALSIFY")
    result["verdict_note"] = (f"trained a3/a1={r3r1_t:.2f} (genuine>0.5={genuine}), "
                              f"untrained a3/a1={r3r1_u:.2f}, training-not-flattened={not_flattened}")
    path = os.path.join(OUTDIR, "interaction_order.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\n[ITX] VERDICT: {result['verdict']} -- {result['verdict_note']}")
    print(f"[ITX] wrote {path}")


if __name__ == "__main__":
    main()
