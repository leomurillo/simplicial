"""Audit a quantum-lift signature in mod-6 transformer behavior.

This runner is designed for the Paper 14 -> Paper 15 question:

* collect final-residual activations on a synthetic Z/6Z arithmetic task;
* build an empirical six-state density matrix whose diagonal is the model's
  answer distribution and whose off-diagonal part is the residual covariance
  seen through the six answer readout directions;
* compare Cartan-style rotations with off-diagonal CRT-local rotations;
* measure how much hidden-space motion survives the LayerNorm + unembedding +
  Softmax measurement.

The primary mode is intentionally cheap.  It forwards each prompt once, captures
the requested residual layers, and evaluates final-layer interventions through
the final norm + lm_head.  Use ``--exact-suffix`` only for a heavier follow-up:
it reinjects layer-l activations into the model and runs the remaining layers.

This is an operational audit, not a claim that the residual stream is literally
a quantum state.  The density matrix below is the pre-registered measurement
object for testing whether off-diagonal CRT covariance is present and whether
it is squashed by the classical output simplex.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "empirical" / "data" / "mod6_addition_probe_manifest.json"
DEFAULT_OUTDIR = ROOT / "empirical" / "quantum_lift"
DEFAULT_REPORT = ROOT / "empirical" / "reports" / "quantum_lift_audit.md"

RESIDUES = tuple(str(i) for i in range(6))
EPS = 1e-12


@dataclass(frozen=True)
class PromptCase:
    x: int
    y: int
    result: int
    template_id: int
    prompt: str


@dataclass(frozen=True)
class GeneratorSpec:
    name: str
    family: str
    matrix: Any


PROMPT_TEMPLATES = (
    "What is ({x} + {y}) mod 6? Answer with one digit:",
    "Compute ({x}+{y}) modulo 6. Answer with one digit:",
    "In Z/6Z, {x} + {y} = ? Answer with one digit:",
    "Return only the residue: ({x} + {y}) mod 6 =",
    "Modulo 6 arithmetic. {x} plus {y} is",
    "Question: ({x} + {y}) mod 6. Digit answer:",
)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def generate_manifest(path: Path, templates: int = len(PROMPT_TEMPLATES)) -> list[PromptCase]:
    if templates < 1 or templates > len(PROMPT_TEMPLATES):
        raise ValueError(f"--templates must be in 1..{len(PROMPT_TEMPLATES)}")
    rows: list[dict[str, Any]] = []
    cases: list[PromptCase] = []
    for template_id, template in enumerate(PROMPT_TEMPLATES[:templates]):
        for x in range(6):
            for y in range(6):
                result = (x + y) % 6
                prompt = template.format(x=x, y=y, result=result)
                rows.append(
                    {
                        "x": x,
                        "y": y,
                        "result": result,
                        "template_id": template_id,
                        "prompt": prompt,
                    }
                )
                cases.append(PromptCase(x=x, y=y, result=result, template_id=template_id, prompt=prompt))
    write_json(
        path,
        {
            "task": "mod6_addition",
            "labels": list(RESIDUES),
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "templates": list(PROMPT_TEMPLATES[:templates]),
            "records": rows,
        },
    )
    return cases


def load_manifest(path: Path) -> list[PromptCase]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError(f"{path} must contain a nonempty records list")
    out: list[PromptCase] = []
    for row in records:
        x = int(row["x"])
        y = int(row["y"])
        result = int(row["result"])
        if result != (x + y) % 6:
            raise ValueError(f"bad mod-6 result in manifest row: {row}")
        out.append(
            PromptCase(
                x=x,
                y=y,
                result=result,
                template_id=int(row.get("template_id", 0)),
                prompt=str(row["prompt"]),
            )
        )
    return out


def render_prompt(tokenizer: Any, prompt: str, chat_template: bool) -> str:
    if not chat_template:
        return prompt
    if not hasattr(tokenizer, "apply_chat_template") or tokenizer.chat_template is None:
        raise ValueError("Requested --chat-template, but tokenizer has no chat template")
    return tokenizer.apply_chat_template(
        [{"role": "user", "content": prompt}],
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
        raise ValueError(f"unsupported dtype {dtype_name!r}") from exc


def common_prefix(sequences: list[list[int]]) -> list[int]:
    if not sequences:
        return []
    prefix = list(sequences[0])
    for seq in sequences[1:]:
        keep = 0
        for left, right in zip(prefix, seq):
            if left != right:
                break
            keep += 1
        prefix = prefix[:keep]
    return prefix


def resolve_digit_bins(tokenizer: Any, include_no_space: bool = True) -> tuple[dict[str, list[int]], list[int], dict[str, Any]]:
    """Resolve digit answer ids, allowing a tokenizer-wide shared prefix.

    Some tokenizers, including Mistral v0.3's, encode every bare digit answer as
    ``[shared_prefix, digit_token]``.  The audit appends that shared prefix to
    the prompt and scores the next-token distribution over the digit tokens.
    """

    primary_sequences: dict[str, list[int]] = {}
    audit: dict[str, Any] = {}
    for digit in RESIDUES:
        variants = [" " + digit]
        if include_no_space:
            variants.append(digit)
        rows = []
        for text in variants:
            token_ids = [int(i) for i in tokenizer.encode(text, add_special_tokens=False)]
            rows.append({"text": text, "token_ids": token_ids})
        primary_sequences[digit] = rows[0]["token_ids"]
        audit[digit] = {"variants": rows}

    answer_prefix = common_prefix(list(primary_sequences.values()))
    bins: dict[str, list[int]] = {}
    for digit, token_ids in primary_sequences.items():
        remainder = token_ids[len(answer_prefix) :]
        if len(remainder) != 1:
            raise ValueError(
                f"Digit {digit} does not reduce to one scored token after shared prefix "
                f"{answer_prefix}: token_ids={token_ids}, remainder={remainder}"
            )
        bins[digit] = [int(remainder[0])]
        audit[digit]["token_ids"] = bins[digit]

    audit["_answer_prefix"] = {
        "token_ids": answer_prefix,
        "decoded": tokenizer.decode(answer_prefix) if answer_prefix else "",
    }
    return bins, answer_prefix, audit


def residue_probs_from_logits(torch: Any, logits: Any, token_bins: dict[str, list[int]]) -> Any:
    probs = torch.softmax(logits.float(), dim=-1)
    cols = []
    for digit in RESIDUES:
        ids = token_bins[digit]
        cols.append(probs[..., ids].sum(dim=-1))
    out = torch.stack(cols, dim=-1)
    return out / out.sum(dim=-1, keepdim=True).clamp_min(1e-30)


def model_layers(model: Any) -> Any:
    # LlamaForCausalLM and MistralForCausalLM expose this path.  Keeping the
    # lookup centralized makes future architectures easy to add explicitly.
    if hasattr(model, "model") and hasattr(model.model, "layers"):
        return model.model.layers
    raise ValueError("Expected a Hugging Face decoder model with model.model.layers")


def final_norm(model: Any) -> Any:
    if hasattr(model, "model") and hasattr(model.model, "norm"):
        return model.model.norm
    raise ValueError("Expected a Hugging Face decoder model with model.model.norm")


def lm_head(model: Any) -> Any:
    if hasattr(model, "lm_head"):
        return model.lm_head
    raise ValueError("Expected a Hugging Face causal LM with lm_head")


def capture_layer_states(
    torch: Any,
    model: Any,
    tokenizer: Any,
    cases: list[PromptCase],
    layers: list[int],
    token_bins: dict[str, list[int]],
    answer_prefix: list[int],
    args: argparse.Namespace,
) -> dict[str, Any]:
    layer_modules = model_layers(model)
    max_layer = len(layer_modules) - 1
    bad = [layer for layer in layers if layer < 0 or layer > max_layer]
    if bad:
        raise ValueError(f"target layers out of range 0..{max_layer}: {bad}")

    captured: dict[int, list[Any]] = {layer: [] for layer in layers}
    handles = []

    def make_hook(layer: int):
        def hook(_module: Any, _inputs: Any, output: Any) -> None:
            hidden = output[0] if isinstance(output, tuple) else output
            captured[layer].append(hidden[:, -1, :].detach().float().cpu())

        return hook

    for layer in layers:
        handles.append(layer_modules[layer].register_forward_hook(make_hook(layer)))

    baseline_probs = []
    logits6 = []
    rendered_prompts = []
    correctness = []
    try:
        with torch.no_grad():
            for idx, case in enumerate(cases):
                rendered = render_prompt(tokenizer, case.prompt, args.chat_template)
                rendered_prompts.append(rendered)
                inputs = tokenizer(rendered, return_tensors="pt")
                if answer_prefix:
                    prefix = torch.tensor([answer_prefix], dtype=inputs["input_ids"].dtype)
                    inputs["input_ids"] = torch.cat([inputs["input_ids"], prefix], dim=1)
                    if "attention_mask" in inputs:
                        inputs["attention_mask"] = torch.cat(
                            [inputs["attention_mask"], torch.ones_like(prefix)],
                            dim=1,
                        )
                if not args.device_map:
                    inputs = {key: value.to(args.device) for key, value in inputs.items()}
                outputs = model(**inputs)
                logits = outputs.logits[:, -1, :]
                p6 = residue_probs_from_logits(torch, logits, token_bins)
                baseline_probs.append(p6.detach().float().cpu())
                logits_cols = []
                for digit in RESIDUES:
                    ids = token_bins[digit]
                    logits_cols.append(logits[:, ids].float().mean(dim=-1))
                logits6.append(torch.stack(logits_cols, dim=-1).detach().float().cpu())
                pred = int(torch.argmax(p6[0]).detach().cpu())
                correctness.append(pred == case.result)
                if args.progress and ((idx + 1) % max(1, args.progress_every) == 0 or idx + 1 == len(cases)):
                    print(f"[collect] {idx + 1}/{len(cases)} prompts")
    finally:
        for handle in handles:
            handle.remove()

    states = {str(layer): torch.cat(chunks, dim=0).numpy() for layer, chunks in captured.items()}
    return {
        "hidden": states,
        "probs": torch.cat(baseline_probs, dim=0).numpy(),
        "logits6": torch.cat(logits6, dim=0).numpy(),
        "rendered_prompts": rendered_prompts,
        "accuracy": float(sum(correctness) / len(correctness)),
        "predicted_correct": correctness,
    }


def readout_basis_from_unembedding(torch: Any, model: Any, token_bins: dict[str, list[int]]) -> Any:
    rows = []
    weight = lm_head(model).weight.detach().float()
    for digit in RESIDUES:
        ids = torch.tensor(token_bins[digit], device=weight.device, dtype=torch.long)
        rows.append(weight.index_select(0, ids).mean(dim=0))
    # D maps residue coordinates to residual-space readout directions.  We keep
    # the triangular factor R so CRT generators can be applied in residue-label
    # coordinates rather than in an arbitrary QR coordinate system.
    design = torch.stack(rows, dim=0).T.contiguous()  # [d_model, 6]
    q, r = torch.linalg.qr(design, mode="reduced")
    if q.shape[1] < 6 or float(torch.min(torch.abs(torch.diag(r))).detach().cpu()) < 1e-7:
        raise ValueError("The six answer readout directions are numerically rank deficient.")
    return {"q": q[:, :6].contiguous(), "r": r[:6, :6].contiguous()}


def crt_permutation_numpy(np: Any) -> Any:
    """Return P where x_crt = P x_residue, CRT order is (mod2, mod3)."""
    rows = []
    pairs = [(a, b) for a in range(2) for b in range(3)]
    for a, b in pairs:
        residue = next(r for r in range(6) if r % 2 == a and r % 3 == b)
        row = np.zeros(6)
        row[residue] = 1.0
        rows.append(row)
    return np.stack(rows, axis=0)


def skew_pair_numpy(np: Any, n: int, i: int, j: int) -> Any:
    A = np.zeros((n, n), dtype=float)
    A[i, j] = -1.0
    A[j, i] = 1.0
    return A


def real_dft_basis_numpy(np: Any) -> Any:
    n = 6
    rows = []
    rows.append(np.ones(n) / math.sqrt(n))
    rows.append(np.array([(-1.0) ** r for r in range(n)]) / math.sqrt(n))
    for k in (1, 2):
        rows.append(math.sqrt(2.0 / n) * np.cos(2.0 * math.pi * k * np.arange(n) / n))
        rows.append(math.sqrt(2.0 / n) * np.sin(2.0 * math.pi * k * np.arange(n) / n))
    return np.stack(rows, axis=1)


def make_generators(np: Any) -> list[GeneratorSpec]:
    generators: list[GeneratorSpec] = []
    F = real_dft_basis_numpy(np)
    # Cartan controls: the two real Fourier planes corresponding to the two
    # independent cyclic phase rotations in the C6 character basis.
    for name, i, j in (("cartan_fourier_k1", 2, 3), ("cartan_fourier_k2", 4, 5)):
        generators.append(GeneratorSpec(name=name, family="cartan", matrix=F @ skew_pair_numpy(np, 6, i, j) @ F.T))

    P = crt_permutation_numpy(np)
    K2 = skew_pair_numpy(np, 2, 0, 1)
    I2 = np.eye(2)
    I3 = np.eye(3)
    # CRT-local SU(2) real shadow: mixes the Z/2 factor at fixed Z/3 residue.
    generators.append(GeneratorSpec(name="su2_sigma_y_shadow", family="nonabelian_su2", matrix=P.T @ np.kron(K2, I3) @ P))
    # CRT-local SU(3) real shadows: three off-diagonal Gell-Mann rotation planes.
    for i, j in ((0, 1), (0, 2), (1, 2)):
        K3 = skew_pair_numpy(np, 3, i, j)
        generators.append(
            GeneratorSpec(name=f"su3_lambda_{i}{j}_shadow", family="nonabelian_su3", matrix=P.T @ np.kron(I2, K3) @ P)
        )
    return generators


def matrix_exp_skew(np: Any, scipy_linalg: Any, theta: float, A: Any) -> Any:
    return scipy_linalg.expm(theta * A)


def hellinger_np(np: Any, p: Any, q: Any) -> float:
    return float(np.linalg.norm(np.sqrt(np.maximum(p, 0.0)) - np.sqrt(np.maximum(q, 0.0))) / math.sqrt(2.0))


def kl_np(np: Any, p: Any, q: Any) -> float:
    p_safe = np.maximum(p, EPS)
    q_safe = np.maximum(q, EPS)
    return float(np.sum(p_safe * (np.log(p_safe) - np.log(q_safe))))


def js_np(np: Any, p: Any, q: Any) -> float:
    m = 0.5 * (p + q)
    return float(0.5 * kl_np(np, p, m) + 0.5 * kl_np(np, q, m))


def matrix_sqrt_psd(np: Any, mat: Any) -> Any:
    vals, vecs = np.linalg.eigh(0.5 * (mat + mat.T))
    vals = np.clip(vals, 0.0, None)
    return (vecs * np.sqrt(vals)) @ vecs.T


def bures_np(np: Any, rho: Any, sigma: Any) -> float:
    root = matrix_sqrt_psd(np, rho)
    middle = matrix_sqrt_psd(np, root @ sigma @ root)
    fidelity_root = float(np.trace(middle))
    return math.sqrt(max(0.0, 2.0 - 2.0 * min(1.0, fidelity_root)))


def nearest_psd_with_diagonal(np: Any, diag: Any, corr: Any, requested_gamma: float) -> tuple[Any, float]:
    sqrtp = np.sqrt(np.maximum(diag, EPS))
    off = np.outer(sqrtp, sqrtp) * corr
    np.fill_diagonal(off, 0.0)

    def build(gamma: float) -> Any:
        rho = np.diag(diag) + gamma * off
        return 0.5 * (rho + rho.T)

    lo, hi = 0.0, requested_gamma
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        eigmin = float(np.linalg.eigvalsh(build(mid)).min())
        if eigmin >= -1e-10:
            lo = mid
        else:
            hi = mid
    rho = build(lo)
    rho = rho / np.trace(rho)
    return rho, lo


def density_from_hidden(np: Any, probs: Any, coords: Any, requested_gamma: float) -> tuple[Any, dict[str, float]]:
    mean_p = probs.mean(axis=0)
    mean_p = mean_p / mean_p.sum()
    centered = coords - coords.mean(axis=0, keepdims=True)
    cov = np.cov(centered.T)
    std = np.sqrt(np.maximum(np.diag(cov), EPS))
    corr = cov / np.outer(std, std)
    corr = np.nan_to_num(corr, nan=0.0, posinf=0.0, neginf=0.0)
    np.fill_diagonal(corr, 0.0)
    rho, gamma_used = nearest_psd_with_diagonal(np, mean_p, corr, requested_gamma)
    off = rho - np.diag(np.diag(rho))
    stats = {
        "gamma_requested": float(requested_gamma),
        "gamma_used": float(gamma_used),
        "offdiag_fro": float(np.linalg.norm(off, ord="fro")),
        "diag_fro": float(np.linalg.norm(np.diag(np.diag(rho)), ord="fro")),
        "offdiag_to_diag_fro": float(np.linalg.norm(off, ord="fro") / max(EPS, np.linalg.norm(np.diag(np.diag(rho)), ord="fro"))),
        "min_eigenvalue": float(np.linalg.eigvalsh(rho).min()),
        "purity": float(np.trace(rho @ rho)),
    }
    return rho, stats


def layer_coordinates(torch: Any, basis: Any, hidden_np: Any, device: Any) -> dict[str, Any]:
    H = torch.tensor(hidden_np, device=device, dtype=torch.float32)
    center = H.mean(dim=0, keepdim=True)
    q_basis = basis["q"].to(device=device, dtype=torch.float32)
    readout_r = basis["r"].to(device=device, dtype=torch.float32)
    readout_r_t_inv = torch.linalg.inv(readout_r.T)
    Y = (H - center) @ q_basis
    C = Y @ readout_r_t_inv
    return {
        "H": H,
        "center": center,
        "Q": q_basis,
        "readout_r": readout_r,
        "Y": Y,
        "C": C,
    }


def rotated_hidden_from_label_rotation(torch: Any, coords: dict[str, Any], U: Any) -> tuple[Any, Any]:
    C = coords["C"]
    Y = coords["Y"]
    Q = coords["Q"]
    readout_r = coords["readout_r"]
    C_rot = C @ U.T
    Y_rot = C_rot @ readout_r.T
    H_rot = coords["H"] + (Y_rot - Y) @ Q.T
    pre = torch.linalg.norm(Y_rot - Y, dim=-1).detach().cpu().numpy()
    return H_rot, pre


def summarize(values: list[float]) -> dict[str, float]:
    if not values:
        return {"mean": float("nan"), "median": float("nan"), "std": float("nan")}
    import numpy as np

    arr = np.asarray(values, dtype=float)
    return {
        "mean": float(arr.mean()),
        "median": float(np.median(arr)),
        "std": float(arr.std(ddof=0)),
        "p05": float(np.percentile(arr, 5)),
        "p95": float(np.percentile(arr, 95)),
    }


def bootstrap_ci(values: list[float], n_boot: int, seed: int) -> tuple[float, float]:
    import numpy as np

    if not values:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    arr = np.asarray(values, dtype=float)
    means = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        means[b] = arr[rng.integers(0, len(arr), size=len(arr))].mean()
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def run_final_lens_interventions(
    np: Any,
    torch: Any,
    scipy_linalg: Any,
    model: Any,
    token_bins: dict[str, list[int]],
    hidden: dict[str, Any],
    probs: Any,
    basis: Any,
    layers: list[int],
    theta_values: list[float],
    coherence_gamma: float,
) -> dict[str, Any]:
    generators = make_generators(np)
    norm = final_norm(model)
    head = lm_head(model)
    device = next(model.parameters()).device

    layer_results: dict[str, Any] = {}
    with torch.no_grad():
        for layer in layers:
            coords = layer_coordinates(torch, basis, hidden[str(layer)], device)
            rho, density_stats = density_from_hidden(np, probs, coords["C"].detach().cpu().numpy(), coherence_gamma)
            layer_rows = []

            for spec in generators:
                for theta in theta_values:
                    U_np = matrix_exp_skew(np, scipy_linalg, theta, spec.matrix)
                    U = torch.tensor(U_np, device=device, dtype=torch.float32)
                    H_rot, pre = rotated_hidden_from_label_rotation(torch, coords, U)
                    logits = head(norm(H_rot.to(dtype=next(model.parameters()).dtype))).float()
                    p_rot = residue_probs_from_logits(torch, logits, token_bins).detach().cpu().numpy()

                    post_h = [hellinger_np(np, probs[i], p_rot[i]) for i in range(len(probs))]
                    post_js = [js_np(np, probs[i], p_rot[i]) for i in range(len(probs))]
                    post_kl = [kl_np(np, probs[i], p_rot[i]) for i in range(len(probs))]
                    ratios = [post_h[i] / max(float(pre[i]), EPS) for i in range(len(post_h))]

                    rho_rot = U_np @ rho @ U_np.T
                    diag_before = np.diag(rho)
                    diag_after = np.diag(rho_rot)
                    diag_after = np.maximum(diag_after, 0.0)
                    diag_after = diag_after / diag_after.sum()

                    layer_rows.append(
                        {
                            "generator": spec.name,
                            "family": spec.family,
                            "theta": float(theta),
                            "pre_chord": summarize([float(x) for x in pre]),
                            "post_hellinger": summarize(post_h),
                            "post_js": summarize(post_js),
                            "post_kl": summarize(post_kl),
                            "squash_ratio": summarize(ratios),
                            "squash_ratio_mean_ci95": bootstrap_ci(ratios, n_boot=400, seed=17),
                            "density_bures_pre": bures_np(np, rho, rho_rot),
                            "density_diag_hellinger_post": hellinger_np(np, diag_before, diag_after),
                            "density_diag_squash_ratio": hellinger_np(np, diag_before, diag_after) / max(bures_np(np, rho, rho_rot), EPS),
                        }
                    )
            layer_results[str(layer)] = {"density": density_stats, "interventions": layer_rows}
    return layer_results


def run_exact_suffix_interventions(
    np: Any,
    torch: Any,
    scipy_linalg: Any,
    model: Any,
    tokenizer: Any,
    token_bins: dict[str, list[int]],
    answer_prefix: list[int],
    hidden: dict[str, Any],
    probs: Any,
    rendered_prompts: list[str],
    basis: Any,
    layers: list[int],
    theta_values: list[float],
    coherence_gamma: float,
    args: argparse.Namespace,
) -> dict[str, Any]:
    generators = make_generators(np)
    layer_modules = model_layers(model)
    device = next(model.parameters()).device
    param_dtype = next(model.parameters()).dtype
    layer_results: dict[str, Any] = {}

    with torch.no_grad():
        for layer in layers:
            coords = layer_coordinates(torch, basis, hidden[str(layer)], device)
            rho, density_stats = density_from_hidden(np, probs, coords["C"].detach().cpu().numpy(), coherence_gamma)
            layer_rows = []

            for spec in generators:
                for theta in theta_values:
                    U_np = matrix_exp_skew(np, scipy_linalg, theta, spec.matrix)
                    U = torch.tensor(U_np, device=device, dtype=torch.float32)
                    H_rot, pre = rotated_hidden_from_label_rotation(torch, coords, U)
                    p_rot_rows = []

                    for idx, prompt in enumerate(rendered_prompts):
                        replacement = H_rot[idx : idx + 1].detach()

                        def patch_hook(_module: Any, _inputs: Any, output: Any) -> Any:
                            hidden_out = output[0] if isinstance(output, tuple) else output
                            patched = hidden_out.clone()
                            patched[:, -1, :] = replacement.to(device=hidden_out.device, dtype=hidden_out.dtype)
                            if isinstance(output, tuple):
                                return (patched,) + output[1:]
                            return patched

                        handle = layer_modules[layer].register_forward_hook(patch_hook)
                        try:
                            inputs = tokenizer(prompt, return_tensors="pt")
                            if answer_prefix:
                                prefix = torch.tensor([answer_prefix], dtype=inputs["input_ids"].dtype)
                                inputs["input_ids"] = torch.cat([inputs["input_ids"], prefix], dim=1)
                                if "attention_mask" in inputs:
                                    inputs["attention_mask"] = torch.cat(
                                        [inputs["attention_mask"], torch.ones_like(prefix)],
                                        dim=1,
                                    )
                            if not args.device_map:
                                inputs = {key: value.to(args.device) for key, value in inputs.items()}
                            outputs = model(**inputs)
                        finally:
                            handle.remove()
                        p6 = residue_probs_from_logits(torch, outputs.logits[:, -1, :].to(dtype=param_dtype), token_bins)
                        p_rot_rows.append(p6.detach().float().cpu())
                        if args.progress and ((idx + 1) % max(1, args.progress_every) == 0 or idx + 1 == len(rendered_prompts)):
                            print(
                                f"[exact] layer={layer} {spec.name} theta={theta:g} "
                                f"{idx + 1}/{len(rendered_prompts)} prompts"
                            )

                    p_rot = torch.cat(p_rot_rows, dim=0).numpy()
                    post_h = [hellinger_np(np, probs[i], p_rot[i]) for i in range(len(probs))]
                    post_js = [js_np(np, probs[i], p_rot[i]) for i in range(len(probs))]
                    post_kl = [kl_np(np, probs[i], p_rot[i]) for i in range(len(probs))]
                    ratios = [post_h[i] / max(float(pre[i]), EPS) for i in range(len(post_h))]

                    rho_rot = U_np @ rho @ U_np.T
                    diag_before = np.diag(rho)
                    diag_after = np.diag(rho_rot)
                    diag_after = np.maximum(diag_after, 0.0)
                    diag_after = diag_after / diag_after.sum()

                    layer_rows.append(
                        {
                            "generator": spec.name,
                            "family": spec.family,
                            "theta": float(theta),
                            "pre_chord": summarize([float(x) for x in pre]),
                            "post_hellinger": summarize(post_h),
                            "post_js": summarize(post_js),
                            "post_kl": summarize(post_kl),
                            "squash_ratio": summarize(ratios),
                            "squash_ratio_mean_ci95": bootstrap_ci(ratios, n_boot=400, seed=17),
                            "density_bures_pre": bures_np(np, rho, rho_rot),
                            "density_diag_hellinger_post": hellinger_np(np, diag_before, diag_after),
                            "density_diag_squash_ratio": hellinger_np(np, diag_before, diag_after) / max(bures_np(np, rho, rho_rot), EPS),
                        }
                    )
            layer_results[str(layer)] = {"density": density_stats, "interventions": layer_rows}
    return layer_results


def grouped_summary(results: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for layer, payload in results.items():
        groups: dict[str, list[float]] = defaultdict(list)
        density_groups: dict[str, list[float]] = defaultdict(list)
        for row in payload["interventions"]:
            groups[row["family"]].append(row["squash_ratio"]["mean"])
            density_groups[row["family"]].append(row["density_diag_squash_ratio"])
        out[layer] = {
            "families": {family: summarize(vals) for family, vals in sorted(groups.items())},
            "density_families": {family: summarize(vals) for family, vals in sorted(density_groups.items())},
        }
        cartan = out[layer]["families"].get("cartan", {}).get("mean", float("nan"))
        nonabelian_vals = [
            value
            for family, stats in out[layer]["families"].items()
            for value in ([stats["mean"]] if family.startswith("nonabelian") else [])
        ]
        out[layer]["nonabelian_to_cartan_squash_mean"] = (
            float(sum(nonabelian_vals) / len(nonabelian_vals) / cartan)
            if nonabelian_vals and math.isfinite(cartan) and abs(cartan) > EPS
            else float("nan")
        )
    return out


def make_report(payload: dict[str, Any]) -> str:
    lines: list[str] = [
        "# Quantum-Lift Audit: Z/6Z Modular Addition",
        "",
        "## Status",
        "",
        f"- model: `{payload['metadata']['model']}`",
        f"- prompts: {payload['metadata']['n_prompts']}",
        f"- layers: {', '.join(str(x) for x in payload['metadata']['layers'])}",
        f"- baseline six-bin accuracy: {payload['metadata']['accuracy']:.4f}",
        f"- mode: {payload['metadata']['mode']}",
        "",
        "This report tests an operational version of the Paper 15 lift.  The",
        "diagonal of the empirical density matrix is the six-answer softmax",
        "distribution; the off-diagonal entries come from residual covariance",
        "projected onto the six answer-readout directions, with the largest",
        "PSD-safe coherence scale allowed by the requested gamma.",
        "",
        "## Family Summary",
        "",
        "| layer | family | mean squash ratio | median | density diag/pre ratio |",
        "|---:|---|---:|---:|---:|",
    ]

    grouped = payload["grouped_summary"]
    for layer, layer_summary in grouped.items():
        density_families = layer_summary["density_families"]
        for family, stats in layer_summary["families"].items():
            d_stats = density_families.get(family, {})
            lines.append(
                f"| {layer} | {family} | {stats['mean']:.6g} | "
                f"{stats['median']:.6g} | {d_stats.get('mean', float('nan')):.6g} |"
            )
    lines += [
        "",
        "Interpretation: lower squash ratio means more hidden-space motion is lost",
        "after LayerNorm + unembedding + Softmax.  The decisive comparison is",
        "`nonabelian_*` versus `cartan` at matched theta on the same layer.",
        "",
        "## Density Coherence",
        "",
        "| layer | gamma used | offdiag/diag Frobenius | min eigenvalue | purity |",
        "|---:|---:|---:|---:|---:|",
    ]
    for layer, layer_payload in payload["layers"].items():
        d = layer_payload["density"]
        lines.append(
            f"| {layer} | {d['gamma_used']:.6g} | {d['offdiag_to_diag_fro']:.6g} | "
            f"{d['min_eigenvalue']:.3e} | {d['purity']:.6g} |"
        )

    lines += [
        "",
        "## Generator Details",
        "",
        "| layer | family | generator | theta | pre chord | post Hellinger | squash ratio | 95% CI | density Bures | density post H |",
        "|---:|---|---|---:|---:|---:|---:|---|---:|---:|",
    ]
    for layer, layer_payload in payload["layers"].items():
        for row in layer_payload["interventions"]:
            ci = row["squash_ratio_mean_ci95"]
            lines.append(
                f"| {layer} | {row['family']} | {row['generator']} | {row['theta']:.4g} | "
                f"{row['pre_chord']['mean']:.6g} | {row['post_hellinger']['mean']:.6g} | "
                f"{row['squash_ratio']['mean']:.6g} | [{ci[0]:.6g}, {ci[1]:.6g}] | "
                f"{row['density_bures_pre']:.6g} | {row['density_diag_hellinger_post']:.6g} |"
            )

    lines += [
        "",
        "## Pre-Registered Success Read",
        "",
        "- Cartan conservation: Cartan rows should have a stable, nonzero",
        "  post/pre slope across theta.",
        "- Nonabelian squash: nonabelian mean squash ratio below the Cartan mean",
        "  at matched theta and layer, ideally below 0.5x with bootstrap intervals",
        "  separated from the Cartan family.",
        "- Density coherence: offdiag/diag Frobenius should be materially above",
        "  random-label or shuffled-residual controls in a follow-up run.",
        "",
        "Boundary: this audit can support or fail to support the transformer",
        "analogy.  It does not by itself prove an actual SU(2) x SU(3) gauge",
        "action inside the model.",
    ]
    return "\n".join(lines)


def run(args: argparse.Namespace) -> dict[str, Any]:
    if args.write_manifest or not args.manifest.exists():
        cases = generate_manifest(args.manifest, args.templates)
        if args.write_manifest and not args.model:
            return {
                "metadata": {
                    "model": None,
                    "manifest": str(args.manifest),
                    "n_prompts": len(cases),
                    "status": "manifest_only",
                }
            }
    else:
        cases = load_manifest(args.manifest)

    if args.limit is not None:
        cases = cases[: args.limit]
    if not args.model:
        raise ValueError("Provide --model for an empirical run, or --write-manifest alone to only write prompts.")

    try:
        import numpy as np
        import scipy.linalg
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as exc:
        raise RuntimeError(
            "This audit requires numpy, scipy, torch, and transformers. "
            "Install them on the GPU VM before running the model audit."
        ) from exc

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    tokenizer = AutoTokenizer.from_pretrained(
        args.model,
        revision=args.revision,
        trust_remote_code=args.trust_remote_code,
        local_files_only=args.local_files_only,
    )
    token_bins, answer_prefix, token_audit = resolve_digit_bins(tokenizer)

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

    layers = [int(x) for x in args.layers.split(",") if x.strip()]
    collected = capture_layer_states(torch, model, tokenizer, cases, layers, token_bins, answer_prefix, args)
    basis = readout_basis_from_unembedding(torch, model, token_bins)
    theta_values = [float(x) for x in args.theta.split(",") if x.strip()]

    if args.exact_suffix:
        layer_results = run_exact_suffix_interventions(
            np=np,
            torch=torch,
            scipy_linalg=scipy.linalg,
            model=model,
            tokenizer=tokenizer,
            token_bins=token_bins,
            answer_prefix=answer_prefix,
            hidden=collected["hidden"],
            probs=collected["probs"],
            rendered_prompts=collected["rendered_prompts"],
            basis=basis,
            layers=layers,
            theta_values=theta_values,
            coherence_gamma=args.coherence_gamma,
            args=args,
        )
        mode = "exact suffix hook audit"
    else:
        layer_results = run_final_lens_interventions(
            np=np,
            torch=torch,
            scipy_linalg=scipy.linalg,
            model=model,
            token_bins=token_bins,
            hidden=collected["hidden"],
            probs=collected["probs"],
            basis=basis,
            layers=layers,
            theta_values=theta_values,
            coherence_gamma=args.coherence_gamma,
        )
        mode = "final residual readout/lift audit"

    metadata = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "revision": args.revision,
        "dtype": args.dtype,
        "device": args.device,
        "device_map": args.device_map,
        "load_in_4bit": args.load_in_4bit,
        "chat_template": args.chat_template,
        "manifest": str(args.manifest),
        "n_prompts": len(cases),
        "layers": layers,
        "theta": theta_values,
        "coherence_gamma": args.coherence_gamma,
        "accuracy": collected["accuracy"],
        "mode": mode,
        "token_bins": token_audit,
        "answer_prefix_ids": answer_prefix,
        "case_results": [
            {
                "x": case.x,
                "y": case.y,
                "result": case.result,
                "template_id": case.template_id,
                "predicted_correct": bool(collected["predicted_correct"][i]),
                "probs": {digit: float(collected["probs"][i, j]) for j, digit in enumerate(RESIDUES)},
            }
            for i, case in enumerate(cases)
        ],
    }
    payload = {
        "metadata": metadata,
        "grouped_summary": grouped_summary(layer_results),
        "layers": layer_results,
    }
    args.outdir.mkdir(parents=True, exist_ok=True)
    safe_model = args.model.replace("/", "__").replace(":", "_")
    json_path = args.outdir / f"quantum_lift_{safe_model}.json"
    write_json(json_path, payload)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(make_report(payload), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {args.report}")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=None, help="Hugging Face model id, e.g. meta-llama/Llama-3.1-8B")
    parser.add_argument("--revision", default=None)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--write-manifest", action="store_true")
    parser.add_argument("--templates", type=int, default=len(PROMPT_TEMPLATES))
    parser.add_argument("--limit", type=int, default=None, help="Optional prompt limit for smoke tests")
    parser.add_argument("--layers", default="28,29,30,31", help="Comma-separated decoder layer indices")
    parser.add_argument("--theta", default="0.02,0.05,0.1", help="Comma-separated rotation angles in radians")
    parser.add_argument("--coherence-gamma", type=float, default=0.35)
    parser.add_argument("--outdir", type=Path, default=DEFAULT_OUTDIR)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--device-map", default=None)
    parser.add_argument("--dtype", default="bfloat16")
    parser.add_argument("--load-in-4bit", action="store_true")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--trust-remote-code", action="store_true")
    parser.add_argument("--chat-template", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--progress-every", type=int, default=25)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--exact-suffix",
        action="store_true",
        help="Run the heavier hook-based intervention path through downstream layers.",
    )
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
