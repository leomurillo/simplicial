"""
GCP-ONLY extraction stub for the vec2vec residual diagnostic.  NOT IN THE LOCAL
GATE -- imports torch / sentence-transformers / the vec2vec repo, which must
NEVER run on the laptop (torch crashes it).  Write here, run on GCP.

Produces the three paired arrays the numpy diagnostic
(probe_vec2vec_residual_conductor.py --arrays) consumes:

    U.npy     source embeddings      U_i    = M1(x_i)
    V.npy     target embeddings      V_i    = M2(x_i)      (ground truth)
    VHAT.npy  translations           Vhat_i = F_{1->2}(M1(x_i))

paired by text x_i on a HELD-OUT set (pairing is for EVALUATION only; vec2vec
itself is trained unsupervised).  Then, on the laptop:

    python probe_vec2vec_residual_conductor.py --arrays VHAT.npy V.npy

----------------------------------------------------------------------------
SETUP (GCP)
----------------------------------------------------------------------------
  git clone https://github.com/rjha18/vec2vec && cd vec2vec
  pip install -r requirements.txt sentence-transformers
  # drop this file in the repo root (it imports the repo's translator class)

  python vec2vec_extract_arrays.py \
      --m1 sentence-transformers/gtr-t5-base \
      --m2 thenlper/gte-base \
      --texts heldout.txt \
      --ckpt runs/gtr_gte/translator.pt \
      --out_dir arrays/

----------------------------------------------------------------------------
The two encoder lines are standard and concrete. The translator load + forward
(marked  >>> REPO-SPECIFIC <<< ) follow the repo's own eval script -- confirm
the class path / checkpoint key against the version you clone.
"""

import argparse
import numpy as np


def embed(model_name, texts, batch_size=256):
    """Concrete: sentence-transformers cosine-space embeddings."""
    from sentence_transformers import SentenceTransformer  # torch -- GCP only
    m = SentenceTransformer(model_name)
    emb = m.encode(
        texts,
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,        # these are cosine-space encoders
        show_progress_bar=True,
    )
    return emb.astype(np.float32)


def load_translator(ckpt_path, d_in, d_out, device):
    """>>> REPO-SPECIFIC <<<  Load the trained vec2vec translator F_{1->2}.

    Mirror the repo's eval. As of the public release the translator is the
    adapter+backbone module saved in the run dir; the forward that realizes
    F_1 = B_2 . T . A_1 is exposed by the repo's Transform/Translator class.
    Replace the body below with the repo's loader, e.g.:

        from vec2vec.models import Translator
        net = Translator(d_in=d_in, d_out=d_out, ...)
        net.load_state_dict(torch.load(ckpt_path, map_location=device))
        net.eval().to(device)
        return net
    """
    raise NotImplementedError(
        "Wire load_translator() to the cloned repo's translator class "
        "(see vec2vec eval script). d_in=%d d_out=%d" % (d_in, d_out)
    )


def translate(net, U, device, batch_size=1024):
    """>>> REPO-SPECIFIC <<<  Apply F_{1->2} to source embeddings U (N x d_in).

    Replace `net.translate_1_to_2(batch)` with the repo's forward for the
    1->2 direction (the method that composes B_2 . T . A_1)."""
    import torch
    outs = []
    with torch.no_grad():
        for s in range(0, len(U), batch_size):
            b = torch.from_numpy(U[s:s + batch_size]).float().to(device)
            v = net.translate_1_to_2(b)            # <-- repo's 1->2 forward
            outs.append(v.cpu().numpy())
    return np.concatenate(outs, 0).astype(np.float32)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m1", required=True, help="unknown/source encoder (HF id)")
    ap.add_argument("--m2", required=True, help="known/target encoder (HF id)")
    ap.add_argument("--texts", required=True, help="held-out texts, one per line")
    ap.add_argument("--ckpt", required=True, help="trained translator checkpoint")
    ap.add_argument("--out_dir", default=".")
    args = ap.parse_args()

    import os
    os.makedirs(args.out_dir, exist_ok=True)
    with open(args.texts, encoding="utf-8") as f:
        texts = [ln.strip() for ln in f if ln.strip()]
    print(f"{len(texts)} held-out texts")

    U = embed(args.m1, texts)
    V = embed(args.m2, texts)
    print("U", U.shape, "V", V.shape)

    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    net = load_translator(args.ckpt, U.shape[1], V.shape[1], device)
    Vhat = translate(net, U, device)
    print("Vhat", Vhat.shape)

    np.save(os.path.join(args.out_dir, "U.npy"), U)
    np.save(os.path.join(args.out_dir, "V.npy"), V)
    np.save(os.path.join(args.out_dir, "VHAT.npy"), Vhat)
    print(f"wrote U.npy / V.npy / VHAT.npy to {args.out_dir}/")
    print("Now (laptop): python probe_vec2vec_residual_conductor.py "
          "--arrays %s/VHAT.npy %s/V.npy" % (args.out_dir, args.out_dir))


if __name__ == "__main__":
    main()
