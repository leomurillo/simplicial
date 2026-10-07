"""
Shared machinery for the A1 (compositionality tax) and A4 (dark structure) GCP experiments.

  *** RUNS ON GCP ONLY. ***  The activation-extraction functions import torch + transformers,
  which must NEVER run on the author's laptop (it has crashed the machine before). The kernel /
  regression math is pure numpy and is locally importable, but the experiment entry points are
  guarded: they refuse to run unless the environment variable GCP_RUN=1 is set (you set it on the
  GCP instance). The numpy kernel utilities below are unit-tested by `selftest_numpy()` which uses
  NO torch and is safe to run anywhere.

Design: an "order-m probe" is a degree-m polynomial-kernel ridge readout. The degree-m polynomial
kernel K_m(x,y) = (1 + <x,y>)^m (rows unit-normalized, so <x,y> in [-1,1]) spans exactly the
monomials of degree <= m in the activations -- i.e. all interactions up to order m. Cross-validated
R^2 (regression) or accuracy (classification) of the degree-m kernel is the order-m faithfulness.
"""
import os
import sys
import json
import numpy as np

SEED = 0


# ----------------------------------------------------------------------------- guards
def require_gcp():
    """Refuse to run the torch path anywhere but a GCP instance (hardware safety)."""
    if os.environ.get("GCP_RUN") != "1":
        sys.exit("GCP-ONLY: this script imports torch/transformers. Set GCP_RUN=1 on the GCP "
                 "instance to run. (Never run torch on the author's laptop.)")


# ----------------------------------------------------------------------------- numpy kernel core
def unit_normalize(X, eps=1e-8):
    """L2-normalize rows so the polynomial kernel is bounded: <x,y> in [-1,1]."""
    return X / (np.linalg.norm(X, axis=1, keepdims=True) + eps)


def pca_reduce(X, d_sub):
    """Top-d_sub principal components (centered). Real activations are high-dim; an injected or
    real order-k structure is only statistically isolable by an order-m kernel when the ambient
    dimension is small enough (see _tune_regime.py) -- so calibration runs in a low-d projection,
    and the degradation with d_sub is itself the practical obstruction we measure."""
    Xc = X - X.mean(0, keepdims=True)
    _, _, Vt = np.linalg.svd(Xc, full_matrices=False)
    return Xc @ Vt[:d_sub].T


def poly_gram(A, B, degree, c=1.0):
    """Degree-`degree` polynomial kernel Gram matrix. A:(n,d), B:(m,d), unit-normalized rows."""
    return (c + A @ B.T) ** degree


def krr_solve_predict(K_tr, y_tr, K_te, lam):
    """Kernel ridge: solve (K_tr + lam I) alpha = y_tr ; predict K_te @ alpha."""
    n = K_tr.shape[0]
    alpha = np.linalg.solve(K_tr + lam * np.eye(n), y_tr)
    return K_te @ alpha


def rbf_gram(A, B, gamma):
    """RBF (Gaussian) kernel: K=exp(-gamma||a-b||^2). All-order, but SMOOTHLY regularized -- unlike
    an explicit degree-4 polynomial kernel it does not blow up / overfit, so it is the right tool to
    ask 'is there order->=3 output-relevant structure?' without the degree-4 negative-R^2 pathology."""
    aa = np.sum(A * A, axis=1)[:, None]
    bb = np.sum(B * B, axis=1)[None, :]
    return np.exp(-gamma * np.maximum(aa + bb - 2 * A @ B.T, 0.0))


def median_gamma(X, seed=SEED, cap=600):
    rng = np.random.default_rng(seed)
    s = X[rng.permutation(len(X))[:min(len(X), cap)]]
    d2 = np.maximum(0.0, (s * s).sum(1)[:, None] + (s * s).sum(1)[None, :] - 2 * s @ s.T)
    med = np.median(d2[d2 > 1e-12])
    return 1.0 / (med + 1e-12)


def cv_reg_best(X, y, kernel_fn, lams=(1e-3, 1e-2, 1e-1, 1.0, 10.0), n_splits=4, seed=SEED):
    """k-fold CV R^2 of kernel-ridge regression, selecting lam by best OOF R^2 over a grid. The same
    selection is applied to every kernel, so the optimism cancels in a kernel-vs-kernel difference.
    Gridding includes large lam, so an over-flexible kernel regularizes instead of overfitting."""
    rng = np.random.default_rng(seed)
    X = np.asarray(X, np.float64)
    y = np.asarray(y, np.float64)
    n = len(y)
    folds = np.array_split(rng.permutation(n), n_splits)
    best = -1e18
    for lam in lams:
        preds = np.zeros(n)
        for f in range(n_splits):
            te = folds[f]
            tr = np.concatenate([folds[g] for g in range(n_splits) if g != f])
            K_tr = kernel_fn(X[tr], X[tr])
            K_te = kernel_fn(X[te], X[tr])
            mu, sd = y[tr].mean(), y[tr].std() + 1e-12
            preds[te] = krr_solve_predict(K_tr, (y[tr] - mu) / sd, K_te, lam) * sd + mu
        r2 = 1.0 - np.sum((y - preds) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12)
        best = max(best, r2)
    return float(best)


def cv_metric(X, y, degree, task, lam=1e-2, n_splits=4, seed=SEED, c=1.0):
    """
    k-fold cross-validated score of a degree-`degree` polynomial-kernel ridge readout.
      task='clf' : y in {-1,+1}; returns balanced accuracy (sign of prediction).
      task='reg' : y real; returns out-of-fold R^2.
    The inner products are recomputed per fold (degree applied to the same base <x,y>).
    """
    rng = np.random.default_rng(seed)
    X = unit_normalize(np.asarray(X, dtype=np.float64))
    y = np.asarray(y, dtype=np.float64)
    n = len(y)
    idx = rng.permutation(n)
    folds = np.array_split(idx, n_splits)
    preds = np.zeros(n)
    for f in range(n_splits):
        te = folds[f]
        tr = np.concatenate([folds[g] for g in range(n_splits) if g != f])
        K_tr = poly_gram(X[tr], X[tr], degree, c)
        K_te = poly_gram(X[te], X[tr], degree, c)
        if task == "reg":
            mu, sd = y[tr].mean(), y[tr].std() + 1e-12
            p = krr_solve_predict(K_tr, (y[tr] - mu) / sd, K_te, lam)
            preds[te] = p * sd + mu
        else:
            preds[te] = krr_solve_predict(K_tr, y[tr], K_te, lam)
    if task == "reg":
        ss_res = np.sum((y - preds) ** 2)
        ss_tot = np.sum((y - y.mean()) ** 2) + 1e-12
        return float(1.0 - ss_res / ss_tot)
    # balanced accuracy
    yhat = np.sign(preds)
    yhat[yhat == 0] = 1
    pos = y == 1
    neg = y == -1
    acc_pos = np.mean(yhat[pos] == 1) if pos.any() else 0.0
    acc_neg = np.mean(yhat[neg] == -1) if neg.any() else 0.0
    return float(0.5 * (acc_pos + acc_neg))


def fwht(a):
    """Fast Walsh-Hadamard transform, normalized so the output are ANOVA Fourier coefficients
    c_S = 2^{-K} sum_x chi_S(x) f(x). Then Var(f)=sum_{S!=0} c_S^2 (Parseval)."""
    a = np.array(a, dtype=np.float64).copy()
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            x = a[i:i + h].copy()
            y = a[i + h:i + 2 * h].copy()
            a[i:i + h] = x + y
            a[i + h:i + 2 * h] = x - y
        h *= 2
    return a / n


def interaction_spectrum(f, K):
    """f: length-2^K array, f[i] = output when knob-config = bits of i. Returns the functional-ANOVA
    variance at each interaction order k=0..K (mass[0]=mean^2; mass[k>=1]=variance from k-way
    interactions of the K binary knobs)."""
    c = fwht(np.asarray(f, np.float64))
    orders = np.array([bin(i).count("1") for i in range(len(c))])
    return np.array([float(np.sum(c[orders == k] ** 2)) for k in range(K + 1)])


def selftest_interaction():
    """No torch. The ANOVA spectrum must peak at the true interaction order of known functions."""
    K = 6
    X = np.array([[1.0 if (i >> b) & 1 else -1.0 for b in range(K)] for i in range(2 ** K)])
    tests = {"linear(x0)": X[:, 0], "pair(x0 x1)": X[:, 0] * X[:, 1],
             "parity3(x0x1x2)": X[:, 0] * X[:, 1] * X[:, 2],
             "parity4": X[:, 0] * X[:, 1] * X[:, 2] * X[:, 3]}
    ok = True
    for name, f in tests.items():
        m = interaction_spectrum(f, K)
        peak = int(np.argmax(m[1:])) + 1
        expect = {"linear(x0)": 1, "pair(x0 x1)": 2, "parity3(x0x1x2)": 3, "parity4": 4}[name]
        ok = ok and peak == expect
        print(f"[itx] {name:<18} mass={np.round(m, 3)} peak-order={peak} (expect {expect})")
    print("[itx]", "PASS" if ok else "FAIL")
    return ok


def selftest_numpy():
    """No torch. Validate the instrument in the statistically-accessible regime (low d_sub): a
    k-parity is recovered iff degree >= k -- the sharp phase boundary, tau(k)=k."""
    rng = np.random.default_rng(SEED)
    n = 1500
    results, ok = {}, True
    for k in (2, 3, 4):
        d_sub = k + 1
        Z = rng.standard_normal((n, d_sub)) + 0.5 * rng.standard_t(3, size=(n, d_sub))
        y = np.prod(np.sign(Z[:, :k]), axis=1)         # k-parity (order-k)
        accs = {m: round(cv_metric(Z, y, m, "clf", lam=1e-4, n_splits=3), 3) for m in (1, 2, 3, 4)}
        results[f"k={k}"] = accs
        ok = ok and accs[k] >= 0.80 and (accs[k - 1] if k > 1 else 0.5) <= 0.65
    print("[selftest] parity recovered iff degree>=k (chance below k, high at/above), tau(k)=k:")
    print(json.dumps(results, indent=2))
    print("[selftest]", "PASS -- sharp phase boundary" if ok else "FAIL -- boundary not clean")
    return results, ok


# ----------------------------------------------------------------------------- torch / model path
def load_model(name="gpt2", device="cpu"):
    require_gcp()
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(name)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    # force float32: many models ship fp16 weights, but CPU + numpy.linalg need fp32.
    model = AutoModelForCausalLM.from_pretrained(name, output_hidden_states=True,
                                                 torch_dtype=torch.float32)
    model.eval().to(device)
    return model, tok


def load_untrained(name, device="cpu"):
    """Same architecture, RANDOM weights (learned nothing). Control for: is the observed ramp a
    product of the layered architecture's feature-mixing rather than learned structure?"""
    require_gcp()
    import torch  # noqa: F401
    from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(name)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    cfg = AutoConfig.from_pretrained(name)
    cfg.output_hidden_states = True
    model = AutoModelForCausalLM.from_config(cfg)   # random init, float32 by default
    model.eval().to(device)
    return model, tok


def get_corpus(n_chars=200000, seed=SEED):
    """Diverse English text for activation diversity. Try a direct urllib fetch (most robust), then
    the datasets library, then a built-in fallback. A *repetitive* corpus would make activations
    degenerate, so we insist on real varied text when any network is available."""
    import urllib.request
    for url in (
        "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt",
        "https://www.gutenberg.org/files/1342/1342-0.txt",   # Pride and Prejudice (prose)
    ):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                text = r.read().decode("utf-8", errors="ignore")
            if len(text) > 20000:
                print(f"[corpus] fetched {len(text)} chars from {url}")
                return text[:n_chars]
        except Exception as e:
            print(f"[corpus] fetch failed ({url}): {e}")
    try:
        from datasets import load_dataset
        ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
        text = "\n".join(t for t in ds["text"] if t.strip())
        if len(text) > 20000:
            return text[:n_chars]
    except Exception as e:
        print(f"[corpus] datasets unavailable ({e}); using built-in fallback corpus.")
    if True:
        base = (
            "The history of science is a record of revised certainties. A theory earns trust not "
            "by its beauty but by the predictions it risks. When the river rose, the engineers who "
            "had measured the old floods slept poorly. Language compresses a world into a line, and "
            "the listener must expand it again. Markets, like weather, are easy to narrate and hard "
            "to forecast. A proof is a path that any careful reader can walk without falling. The "
            "child sorted the stones by color, then by size, then grew bored and built a tower. "
            "Memory is not a recording but a reconstruction, edited each time it is read. Gravity "
            "tells matter how to move; matter tells gravity where to gather. Every measurement pays "
            "a small tax in disturbance, and the bill comes due at the smallest scales. "
        )
        reps = (n_chars // len(base)) + 1
        return (base * reps)[:n_chars]


def extract(model, tok, text, layers, max_tokens=2500, batch_tokens=512, device="cpu"):
    """
    Tokenize `text`, run the model in non-overlapping windows, and collect per-position hidden
    states at the requested `layers` plus the per-position surprisal of the actual next token
    (a real scalar output the model computed). Returns:
        acts: dict layer -> ndarray (N, d)
        surprisal: ndarray (N,)   (-log p(next token), the A4 target)
        meta: dict
    Positions are flattened across windows; the last position of each window (no next token) is
    dropped. N <= max_tokens.
    """
    require_gcp()
    import torch
    ids = tok(text, return_tensors="pt")["input_ids"][0]
    acts = {L: [] for L in layers}
    surpr = []
    collected = 0
    with torch.no_grad():
        for s in range(0, len(ids) - 1, batch_tokens):
            window = ids[s:s + batch_tokens]
            if len(window) < 2:
                break
            out = model(window.unsqueeze(0).to(device))
            hs = out.hidden_states               # tuple: (emb, layer1, ..., layerLast)
            logits = out.logits[0]               # (T, vocab)
            T = window.shape[0]
            logp = torch.log_softmax(logits[:-1], dim=-1)   # predict positions 1..T-1
            nxt = window[1:].to(device)
            sp = -logp[torch.arange(T - 1), nxt]            # surprisal per position (T-1,)
            for L in layers:
                acts[L].append(hs[L][0, :-1, :].float().cpu().numpy())   # fp32; drop last position
            surpr.append(sp.float().cpu().numpy())
            collected += (T - 1)
            if collected >= max_tokens:
                break
    acts = {L: np.concatenate(v, axis=0)[:max_tokens] for L, v in acts.items()}
    surpr = np.concatenate(surpr)[:max_tokens]
    meta = {"n_tokens": int(len(surpr)), "hidden_dim": int(next(iter(acts.values())).shape[1]),
            "layers": list(layers)}
    return acts, surpr, meta


if __name__ == "__main__":
    # safe: numpy-only self test (no torch)
    selftest_numpy()
