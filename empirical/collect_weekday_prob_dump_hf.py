"""Collect next-token weekday probabilities from a Hugging Face causal LM.

This script is the empirical C7 collector.  It reads the 49-case weekday
manifest, scores the next token under a local Hugging Face model, bins the
probability mass assigned to weekday answer tokens, and writes the JSON dump
accepted by ``build_weekday_centroids_from_dump.py``.

It intentionally fails fast when ``torch``/``transformers`` or the requested
model are unavailable.  It does not fabricate centroids.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from compute_weekdays_K_CH import WEEKDAYS


DEFAULT_MANIFEST = Path("empirical/data/weekdays_probe_manifest.json")
DEFAULT_OUT = Path("empirical/data/weekdays_llama31_8b_probability_dump.json")


def load_manifest(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != 49:
        raise ValueError(f"{path} must contain the 49-case weekday manifest")
    return records


def token_variants(include_case_variants: bool) -> dict[str, list[str]]:
    bins: dict[str, list[str]] = {}
    for day in WEEKDAYS:
        variants = [day, " " + day]
        if include_case_variants:
            variants.extend([day.lower(), " " + day.lower(), day.upper(), " " + day.upper()])
        bins[day] = variants
    return bins


def resolve_token_bins(tokenizer: Any, include_case_variants: bool) -> tuple[dict[str, list[int]], dict[str, Any]]:
    """Map weekday string variants to one-token answer ids.

    The experiment is a next-token probe.  A variant that tokenizes to multiple
    ids is recorded but omitted from the one-step probability bin.
    """

    bins: dict[str, list[int]] = {}
    audit: dict[str, Any] = {}
    for day, variants in token_variants(include_case_variants).items():
        ids: OrderedDict[int, None] = OrderedDict()
        variant_rows = []
        for variant in variants:
            token_ids = tokenizer.encode(variant, add_special_tokens=False)
            single_token = len(token_ids) == 1
            if single_token:
                ids[int(token_ids[0])] = None
            variant_rows.append(
                {
                    "text": variant,
                    "token_ids": [int(x) for x in token_ids],
                    "single_next_token": single_token,
                }
            )
        if not ids:
            raise ValueError(
                f"No one-token answer variant found for {day}; this next-token "
                "collector cannot score the weekday bin for this tokenizer."
            )
        bins[day] = list(ids.keys())
        audit[day] = {
            "token_ids": bins[day],
            "variants": variant_rows,
        }
    return bins, audit


def prompt_text(tokenizer: Any, raw_prompt: str, use_chat_template: bool) -> str:
    if not use_chat_template:
        return raw_prompt
    if not hasattr(tokenizer, "apply_chat_template") or tokenizer.chat_template is None:
        raise ValueError("Requested --chat-template, but tokenizer has no chat template")
    return tokenizer.apply_chat_template(
        [{"role": "user", "content": raw_prompt}],
        tokenize=False,
        add_generation_prompt=True,
    )


def load_torch_dtype(torch: Any, dtype_name: str) -> Any:
    if dtype_name == "auto":
        return "auto"
    aliases = {
        "float32": torch.float32,
        "fp32": torch.float32,
        "float16": torch.float16,
        "fp16": torch.float16,
        "bfloat16": torch.bfloat16,
        "bf16": torch.bfloat16,
    }
    try:
        return aliases[dtype_name]
    except KeyError as exc:
        raise ValueError(f"Unsupported dtype {dtype_name!r}") from exc


def weekday_probs_from_logits(torch: Any, logits: Any, token_id_bins: dict[str, list[int]]) -> tuple[dict[str, float], float]:
    probs = torch.softmax(logits.float(), dim=-1)
    weekday_probs = {}
    weekday_mass = 0.0
    vocab_size = int(probs.shape[-1])
    for day, token_ids in token_id_bins.items():
        valid_ids = [token_id for token_id in token_ids if 0 <= token_id < vocab_size]
        if len(valid_ids) != len(token_ids):
            raise ValueError(f"Token id out of vocabulary for {day}: {token_ids}")
        value = float(probs[valid_ids].sum().detach().cpu())
        if not math.isfinite(value) or value < 0.0:
            raise ValueError(f"Invalid probability for {day}: {value}")
        weekday_probs[day] = value
        weekday_mass += value
    other_probability = max(0.0, 1.0 - weekday_mass)
    return weekday_probs, other_probability


def collect(args: argparse.Namespace) -> dict[str, Any]:
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as exc:
        raise RuntimeError(
            "This collector requires `torch` and `transformers` in the active "
            "Python environment. Install them in a runtime with model access, "
            "or provide an existing dump/centroid artifact to the orchestrator."
        ) from exc

    manifest = load_manifest(args.manifest)
    tokenizer = AutoTokenizer.from_pretrained(
        args.model,
        revision=args.revision,
        trust_remote_code=args.trust_remote_code,
        local_files_only=args.local_files_only,
    )
    token_id_bins, token_audit = resolve_token_bins(tokenizer, args.include_case_variants)

    model_kwargs: dict[str, Any] = {
        "revision": args.revision,
        "trust_remote_code": args.trust_remote_code,
        "local_files_only": args.local_files_only,
    }
    if args.device_map:
        model_kwargs["device_map"] = args.device_map
    model_kwargs["torch_dtype"] = load_torch_dtype(torch, args.dtype)
    if args.load_in_4bit:
        model_kwargs["load_in_4bit"] = True

    model = AutoModelForCausalLM.from_pretrained(args.model, **model_kwargs)
    if not args.device_map:
        model.to(args.device)
    model.eval()

    output_records = []
    with torch.no_grad():
        for index, case in enumerate(manifest):
            raw_prompt = str(case["prompt"])
            rendered_prompt = prompt_text(tokenizer, raw_prompt, args.chat_template)
            inputs = tokenizer(rendered_prompt, return_tensors="pt")
            if not args.device_map:
                inputs = {key: value.to(args.device) for key, value in inputs.items()}
            outputs = model(**inputs)
            logits = outputs.logits[0, -1, :]
            weekday_probs, other_probability = weekday_probs_from_logits(torch, logits, token_id_bins)
            record = {
                "start_day": case["start_day"],
                "offset": case["offset"],
                "correct_day": case["correct_day"],
                "prompt": raw_prompt,
                "rendered_prompt": rendered_prompt,
                "weekday_probs": weekday_probs,
                "other_probability": other_probability,
                "weekday_probability_mass": sum(weekday_probs.values()),
            }
            output_records.append(record)
            if args.progress:
                print(
                    f"[{index + 1:02d}/49] {case['start_day']} + {case['offset']} -> "
                    f"{case['correct_day']} weekday_mass={record['weekday_probability_mass']:.6g}"
                )

    metadata = {
        "collector": "collect_weekday_prob_dump_hf.py",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "revision": args.revision,
        "dtype": args.dtype,
        "device": args.device,
        "device_map": args.device_map,
        "load_in_4bit": args.load_in_4bit,
        "local_files_only": args.local_files_only,
        "chat_template": args.chat_template,
        "manifest": str(args.manifest),
        "token_id_bins": token_audit,
        "normalization_note": (
            "Records store raw next-token probability mass for weekday bins plus "
            "the residual non-weekday mass. The centroid builder conditions rows "
            "on total weekday-bin mass for the seven-bin matrix."
        ),
    }
    return {
        "metadata": metadata,
        "records": output_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="meta-llama/Llama-3.1-8B")
    parser.add_argument("--revision", default=None)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--device-map", default=None)
    parser.add_argument("--dtype", default="auto")
    parser.add_argument("--load-in-4bit", action="store_true")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--trust-remote-code", action="store_true")
    parser.add_argument("--chat-template", action="store_true")
    parser.add_argument("--include-case-variants", action="store_true")
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()

    payload = collect(args)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
