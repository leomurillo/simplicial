#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 36 Layerwise Packet Spectroscopy -- top-level driver
==========================================================

Per Paper 36 §8 script inventory.

INTENDED USAGE
--------------
    python empirical\layerwise_packet_spectroscopy.py \
        --model-tag llama31_8b --task months --layers all --output-dir empirical\reports

The driver loads a HuggingFace checkpoint, runs forward passes over the
task dataset, and saves per-layer last-token residual streams to a
safetensors file.  Then the lens-arm and probe-arm scorers consume those
files and produce the f_{d,ell} spectra.

STATUS IN THE PRESENT SESSION
-----------------------------
The present session's compute environment is CPU-only with no
`transformers` package installed and no Llama-3.1-8B / Mistral-7B-v0.3
checkpoint downloaded.  Per the PROMPT's HuggingFace-download deferral
rule (Paper 35 §3.6: "the deferred state is a recorded fact, not a
silent skip"), this driver does not attempt to download the model or run
a forward pass.  Instead it documents the deferral and points to the
final-layer-only measurement that the lens-arm scorer can still produce
from the saved native probability distributions in
`months/baseline/full_output_dists.safetensors` and
`weekdays/baseline/full_output_dists.safetensors`.

When `transformers` and a GPU become available, this driver should:
1. Load model = AutoModelForCausalLM.from_pretrained(model_id, output_hidden_states=True)
2. Load tokenizer and the task prompts (months/baseline/train_samples.json, etc.)
3. For each prompt, run model(prompt) capturing every layer's last-token
   residual stream (model.config.num_hidden_layers + 1 layers, each
   d_model-dim).
4. Stack -> H of shape [n_examples, n_layers, d_model], save to
   empirical/data/residual_streams_<task>_<model_tag>.safetensors.
5. Save W_U restricted to V_R as a .npz with key 'W_U_VR' of shape
   [N, d_model], where V_R is the cyclic sub-vocabulary's token ids.
6. Then invoke native_logit_lens_packet_score_layerwise.py
   with --mode layerwise.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


SCRIPT_VERSION = "audit_kappa_driver_v0.2_2026_06_12"

MODEL_IDS = {
    "llama31_8b": "meta-llama/Llama-3.1-8B",
    "mistral7b_v0_3": "mistralai/Mistral-7B-v0.3",
    "llama31_8b_instruct": "meta-llama/Llama-3.1-8B-Instruct",
    "mistral7b_v0_3_instruct": "mistralai/Mistral-7B-Instruct-v0.3",
}

# Cyclic label order is load-bearing (the FFT is over this order).
TASK_LABELS = {
    "months": ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"],
    "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                 "Saturday", "Sunday"],
    "digits": [str(i) for i in range(10)],
}


def detect_transformers() -> bool:
    try:
        import transformers  # noqa: F401
        return True
    except Exception:
        return False


def run_capture(args) -> None:
    """Forward-pass capture per the module docstring, steps 1-6.

    Capture only: saves per-layer last-token residual streams (BF16, matching
    the Paper 26 'raw BF16' regime) and the W_U slice for V_R, then invokes the
    lens scorer.  No measured quantity is computed here; all packet fractions
    come from native_logit_lens_packet_score_layerwise.py (anchor-verified)."""
    import numpy as np
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from safetensors.torch import save_file

    model_id = MODEL_IDS[args.model_tag]
    root = Path(__file__).resolve().parents[1]
    samples_path = Path(args.samples) if args.samples else (
        root / args.task / "baseline" / "train_samples.json")
    with open(samples_path, encoding="utf-8") as f:
        samples = json.load(f)["samples"]
    prompts = [s["raw_input"] for s in samples]
    labels = TASK_LABELS[args.task]
    N = len(labels)

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
    model.to(device)
    model.eval()

    # V_R token ids in cyclic 0..N-1 order: passed explicitly (--token-ids,
    # pinned by the prior final-only lens JSONs for Llama) or derived from the
    # tokenizer as the single token for ' ' + label.  Either way, assert the
    # single-token identity so a wrong sub-vocabulary cannot pass silently.
    derived = []
    for lab in labels:
        enc = tokenizer.encode(" " + lab, add_special_tokens=False)
        if len(enc) != 1:
            raise ValueError(
                f"label {lab!r} is not a single token under {model_id}: {enc}")
        derived.append(enc[0])
    if args.token_ids:
        ids = [int(x) for x in args.token_ids.split(",")]
        if ids != derived:
            raise ValueError(
                f"--token-ids {ids} != tokenizer-derived {derived} for {model_id}")
    else:
        ids = derived

    n_rows = model.config.num_hidden_layers + 1  # embedding row + each block
    H = torch.zeros((len(prompts), n_rows, model.config.hidden_size),
                    dtype=torch.bfloat16)
    with torch.no_grad():
        for i, prompt in enumerate(prompts):
            inputs = tokenizer(prompt, return_tensors="pt").to(device)
            out = model(**inputs, output_hidden_states=True)
            for ell, h in enumerate(out.hidden_states):
                H[i, ell] = h[0, -1, :].to(torch.bfloat16).cpu()
            if (i + 1) % 20 == 0 or i == len(prompts) - 1:
                print(f"# forward {i + 1}/{len(prompts)}")

    data_dir = root / "empirical" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    res_path = data_dir / f"residual_streams_{args.task}_{args.model_tag}.safetensors"
    save_file({"residual_streams": H}, str(res_path))
    print(f"# wrote {res_path}  shape={tuple(H.shape)} dtype=BF16")

    W_U = model.get_output_embeddings().weight.detach()  # [|V|, d_model]
    W_U_VR = W_U[ids].to(torch.float32).cpu().numpy()
    npz_path = data_dir / f"W_U_VR_{args.task}_{args.model_tag}.npz"
    np.savez(npz_path, W_U_VR=W_U_VR)
    print(f"# wrote {npz_path}  shape={W_U_VR.shape}")

    import transformers
    manifest = {
        "script_version": SCRIPT_VERSION,
        "model_id": model_id,
        "model_tag": args.model_tag,
        "task": args.task,
        "samples_path": str(samples_path),
        "n_examples": len(prompts),
        "n_layer_rows": n_rows,
        "d_model": model.config.hidden_size,
        "token_ids": ids,
        "labels": labels,
        "residual_dtype": "BF16",
        "device": device,
        "torch_version": torch.__version__,
        "transformers_version": transformers.__version__,
        "add_special_tokens": True,
    }
    man_path = data_dir / f"capture_manifest_{args.task}_{args.model_tag}.json"
    man_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"# wrote {man_path}")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / f"layerwise_packet_spectroscopy_{args.task}_{args.model_tag}.json"
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "native_logit_lens_packet_score_layerwise.py"),
        "--mode", "layerwise",
        "--N", str(N),
        "--token-ids", ",".join(str(t) for t in ids),
        "--residual-streams", str(res_path),
        "--unembedding-VR", str(npz_path),
        "--task", args.task,
        "--model-tag", args.model_tag,
        "--output", str(out_json),
    ]
    print("# invoking lens scorer: " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    p = argparse.ArgumentParser(description="Paper 36 layerwise packet spectroscopy driver")
    p.add_argument("--model-tag", required=True,
                   choices=["llama31_8b", "mistral7b_v0_3",
                            "llama31_8b_instruct", "mistral7b_v0_3_instruct"])
    p.add_argument("--task", required=True, choices=["months", "weekdays", "digits"])
    p.add_argument("--layers", default="all")
    p.add_argument("--output-dir", default="empirical/reports")
    p.add_argument("--samples", default=None,
                   help="path to train_samples.json (default <task>/baseline/train_samples.json)")
    p.add_argument("--token-ids", default=None,
                   help="comma-separated V_R token ids in cyclic 0..N-1 order; "
                        "verified against (and defaulting to) the tokenizer's single token for ' '+label")
    p.add_argument("--check-environment", action="store_true",
                   help="Check whether transformers and a GPU are available; print status and exit.")
    args = p.parse_args()

    has_trans = detect_transformers()

    # Even without --check-environment, refuse to run if transformers is missing.
    print(f"# layerwise_packet_spectroscopy version {SCRIPT_VERSION}")
    print(f"# model-tag={args.model_tag}  task={args.task}  layers={args.layers}")
    print(f"# transformers available: {has_trans}")

    if not has_trans:
        print("# Audit kappa forward-pass arm is DEFERRED.")
        print("# Reason: `transformers` is not installed in the present Python")
        print("# environment.  Per the PROMPT's deferral rule and Paper 35 §3.6,")
        print("# this is a stated outcome, not a silent skip.")
        print("#")
        print("# To complete this arm later:")
        print("#   1. pip install transformers")
        print("#   2. Acquire HuggingFace access to meta-llama/Llama-3.1-8B")
        print("#   3. Re-run with the same arguments; this driver will then")
        print("#      perform the forward passes and save per-layer residual")
        print("#      streams to empirical/data/residual_streams_<task>_<model>.safetensors.")
        print("#")
        print("# In the meantime, the FINAL-LAYER lens fractions can be computed")
        print("# from the saved full-vocab native probabilities via:")
        print("#   python empirical\\native_logit_lens_packet_score_layerwise.py \\")
        print("#       --mode final-only \\")
        print("#       --N <12|7|10> \\")
        print("#       --token-ids <v_R token ids> \\")
        print("#       --final-probs <task>/baseline/full_output_dists.safetensors \\")
        print("#       --task <task> --model-tag llama31_8b \\")
        print("#       --output empirical/reports/lens_finalonly_<task>_llama31_8b.json")
        sys.exit(0)

    if args.check_environment:
        try:
            import torch
            print(f"# torch {torch.__version__}, cuda available: {torch.cuda.is_available()}")
        except Exception as exc:
            print(f"# torch import failed: {exc}")
        sys.exit(0)

    # transformers IS available: follow the inventory.
    # (1) load model with output_hidden_states; (2) load prompts; (3) run forwards;
    # (4) save per-layer last-token residual streams + W_U_VR slice; (5) call the scorer.
    run_capture(args)
    sys.exit(0)


if __name__ == "__main__":
    main()
