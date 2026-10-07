"""GCP-side extractor: dump paired U/V/VHAT embeddings for one vec2vec run.
Run from inside the cloned vec2vec repo with its venv. CPU-only OK.

  python _gcp_dump_arrays.py <run_dir> <N> <out_dir>

<run_dir> has config.toml + model.pt (e.g. ckpt/final_model_release/gte_gtr).
Produces out_dir/{U,V,VHAT}.npy  (source=unsup, target=sup, Vhat=F(unsup->sup)).
"""
import os, sys, json
from types import SimpleNamespace
import numpy as np
import torch
import toml
from datasets import load_dataset

from utils.model_utils import load_encoder, get_sentence_embedding_dimension
# Replicate utils.utils.load_n_translator's res_mlp branch inline (avoids that
# module's optional-dep chain: diffusers/vec2text/wandb). Verified identical to
# the repo's construction for style='res_mlp'.
from translators.MLPWithResidual import MLPWithResidual
from translators.TransformTranslator import TransformTranslator


def load_n_translator(cfg, encoder_dims):
    assert cfg.style == "res_mlp", f"this extractor only handles res_mlp, got {cfg.style}"
    transform = MLPWithResidual(
        depth=cfg.transform_depth, in_dim=cfg.d_adapter, hidden_dim=cfg.d_transform,
        out_dim=cfg.d_adapter, norm_style=cfg.norm_style, weight_init=cfg.weight_init)
    return TransformTranslator(
        encoder_dims=encoder_dims, d_adapter=cfg.d_adapter, d_hidden=cfg.d_hidden,
        transform=transform, weight_init=cfg.weight_init, depth=cfg.depth,
        use_small_output_adapters=getattr(cfg, "use_small_output_adapters", False),
        norm_style=getattr(cfg, "norm_style", "batch"))

run_dir = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 10000
out_dir = sys.argv[3] if len(sys.argv) > 3 else "arrays"
os.makedirs(out_dir, exist_ok=True)

cfg = SimpleNamespace(**toml.load(os.path.join(run_dir, "config.toml")))
sup, unsup = cfg.sup_emb, cfg.unsup_emb          # target (known), source (unknown)
max_len = int(getattr(cfg, "max_seq_length", 64))
print(f"run={run_dir}  source(unsup)={unsup}  target(sup)={sup}  "
      f"style={cfg.style}  max_seq_length={max_len}")

# ---- NQ text, streamed (avoids multi-GB full download). In-distribution text
# is the CONSERVATIVE choice: it is best-case for order-2 fidelity, so an
# order-3 deficit measured here is structural, not a train/test-gap artifact. ----
ds = load_dataset("jxm/nq_corpus_dpr", split="train", streaming=True)
it = iter(ds)
first = next(it)
col = "text" if "text" in first else next(c for c, v in first.items() if isinstance(v, str))
texts = [first[col]]
for row in it:
    texts.append(row[col])
    if len(texts) >= N:
        break
print(f"nq_corpus_dpr streamed {len(texts)} passages, using column '{col}'")

# ---- encoders (same 64-token truncation the translator was trained with) ----
enc_sup = load_encoder(sup); enc_sup.max_seq_length = max_len
enc_unsup = load_encoder(unsup); enc_unsup.max_seq_length = max_len
ekw = dict(batch_size=128, normalize_embeddings=True,
           convert_to_numpy=True, show_progress_bar=True)
print("embedding target (sup) ..."); V = enc_sup.encode(texts, **ekw).astype(np.float32)
print("embedding source (unsup) ..."); U = enc_unsup.encode(texts, **ekw).astype(np.float32)
print("U", U.shape, "V", V.shape)

# ---- translator F: unsup -> sup (mirrors eval.py construction) ----
tr = load_n_translator(cfg, {sup: get_sentence_embedding_dimension(enc_sup)})
tr.add_encoders({unsup: get_sentence_embedding_dimension(enc_unsup)},
                overwrite_embs=[unsup])
sd = torch.load(os.path.join(run_dir, "model.pt"), map_location="cpu")
missing, unexpected = tr.load_state_dict(sd, strict=False)
print(f"load_state_dict: {len(missing)} missing, {len(unexpected)} unexpected keys")
tr.eval()
with torch.no_grad():
    Vhat = tr.translate_embeddings(torch.from_numpy(U).float(), unsup, sup).numpy().astype(np.float32)
print("Vhat", Vhat.shape)

np.save(f"{out_dir}/U.npy", U); np.save(f"{out_dir}/V.npy", V); np.save(f"{out_dir}/VHAT.npy", Vhat)
cos = (Vhat * V).sum(1) / (np.linalg.norm(Vhat, 1, 1) * np.linalg.norm(V, 1, 1) + 1e-12) \
    if False else (Vhat * V).sum(1) / (np.linalg.norm(Vhat, axis=1) * np.linalg.norm(V, axis=1) + 1e-12)
meta = {"run": run_dir, "source": unsup, "target": sup, "N": int(N), "d": int(V.shape[1]),
        "paired_cos_mean": float(cos.mean()), "paired_cos_median": float(np.median(cos))}
json.dump(meta, open(f"{out_dir}/meta.json", "w"), indent=2)
print("META", json.dumps(meta))
print("saved U/V/VHAT.npy ->", out_dir)
