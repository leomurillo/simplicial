#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CCSAE Phase B -- cyclic activation corpus capture (GCP-only; torch)
===================================================================

Captures last-token residual streams of Llama-3.1-8B at a chosen layer over a
LARGE templated months-prediction prompt set, to give a real (few-thousand-vector)
training corpus for the trained-SAE confirmation of Paper 45 Theorem 4.2 / P3.

NEVER run locally (torch). Run on the GCP L4 only.

Output (empirical/data/):
  ccsae_corpus_months_llama31_8b.safetensors   tensor 'acts' [M, L_keep, d] BF16
  ccsae_corpus_months_llama31_8b_WU.npz         key 'W_U_VR' [12, d] fp32
  ccsae_corpus_months_llama31_8b_manifest.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
OFFSET_WORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}

# Paraphrase templates; {s}=start month, {ow}=offset word, {on}=offset number.
TEMPLATES = [
    "Q: What month is {ow} months after {s}?\nA:",
    "Q: What month comes {ow} months after {s}?\nA:",
    "Q: Starting from {s}, what month is it {ow} months later?\nA:",
    "Q: {ow} months after {s} it will be the month of\nA:",
    "Q: If the current month is {s}, then {ow} months later it is\nA:",
    "The month {ow} months after {s} is",
    "Counting {ow} months forward from {s} lands on",
    "{s} plus {ow} months is",
    "Q: What is the month {on} months after {s}?\nA:",
    "Q: Add {on} months to {s}. The resulting month is\nA:",
    "Six months after {s} is not the answer; {ow} months after {s} is",
    "Calendar: from {s}, advancing {ow} months reaches",
    "After {s}, count {ow} months ahead to get",
    "Q: Beginning in {s} and moving {ow} months forward, the month is\nA:",
    "In a normal year, {ow} months past {s} is",
    "{s} -> (+{on} months) ->",
    "The month that follows {s} by {ow} months is",
    "Q: Name the month {ow} months after {s}.\nA:",
    "Travelling {ow} months on from {s}, we arrive in",
    "From {s}, {ow} months later the calendar reads",
    "Q: {s}, then {ow} months pass. What month?\nA:",
    "Skipping {ow} months ahead of {s} gives",
    "Q: Which month is {ow} months subsequent to {s}?\nA:",
    "Set the month to {s}; {ow} months afterward it becomes",
]


def build_prompts():
    rows = []
    for s_idx, s in enumerate(MONTHS):
        for off in range(1, 13):
            tgt = MONTHS[(s_idx + off) % 12]
            for t in TEMPLATES:
                rows.append({
                    "prompt": t.format(s=s, ow=OFFSET_WORD[off], on=off),
                    "start": s, "offset": off, "target": tgt,
                })
    return rows


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    import argparse
    import numpy as np
    import torch
    import transformers
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from safetensors.torch import save_file

    ap = argparse.ArgumentParser()
    ap.add_argument("--model-id", default="meta-llama/Llama-3.1-8B")
    ap.add_argument("--layers", default="30,32", help="hidden_states rows to keep (comma-sep)")
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--out-dir", default="empirical/data")
    args = ap.parse_args()

    keep = [int(x) for x in args.layers.split(",")]
    rows = build_prompts()
    prompts = [r["prompt"] for r in rows]
    print(f"# corpus: {len(prompts)} prompts ({len(TEMPLATES)} templates x 12 starts x 12 offsets)")

    tok = AutoTokenizer.from_pretrained(args.model_id)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(args.model_id, torch_dtype=torch.bfloat16)
    model.to(device).eval()

    # months V_R token ids: single token for ' '+month, asserted
    ids = []
    for m in MONTHS:
        enc = tok.encode(" " + m, add_special_tokens=False)
        if len(enc) != 1:
            raise ValueError(f"{m!r} not single-token: {enc}")
        ids.append(enc[0])

    d = model.config.hidden_size
    M = len(prompts)
    acts = torch.zeros((M, len(keep), d), dtype=torch.bfloat16)
    with torch.no_grad():
        for b in range(0, M, args.batch_size):
            chunk = prompts[b:b + args.batch_size]
            enc = tok(chunk, return_tensors="pt", padding=True).to(device)
            out = model(**enc, output_hidden_states=True)
            # last non-pad token index per row
            lengths = enc["attention_mask"].sum(dim=1) - 1
            for ki, row in enumerate(keep):
                h = out.hidden_states[row]                  # [B, T, d]
                sel = h[torch.arange(h.shape[0]), lengths]  # [B, d]
                acts[b:b + len(chunk), ki] = sel.to(torch.bfloat16).cpu()
            if (b // args.batch_size) % 20 == 0:
                print(f"# {b+len(chunk)}/{M}")

    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    acts_path = out_dir / "ccsae_corpus_months_llama31_8b.safetensors"
    save_file({"acts": acts}, str(acts_path))
    W_U = model.get_output_embeddings().weight.detach()
    W_U_VR = W_U[ids].to(torch.float32).cpu().numpy()
    np.savez(out_dir / "ccsae_corpus_months_llama31_8b_WU.npz", W_U_VR=W_U_VR)
    (out_dir / "ccsae_corpus_months_llama31_8b_manifest.json").write_text(json.dumps({
        "model_id": args.model_id, "n_prompts": M, "n_templates": len(TEMPLATES),
        "layers_kept": keep, "d_model": d, "token_ids": ids,
        "torch": torch.__version__, "transformers": transformers.__version__,
        "padding_side": tok.padding_side, "note": "last non-pad token residual per row",
    }, indent=2), encoding="utf-8")
    print(f"# wrote {acts_path} shape={tuple(acts.shape)} (rows kept = {keep})")


if __name__ == "__main__":
    main()
