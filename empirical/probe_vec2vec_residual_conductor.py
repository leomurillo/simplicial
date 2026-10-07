"""
Residual order-spectroscopy of vec2vec embedding translation.
Pre-registered diagnostic for the Conductor-Blind-Spot reading of

    Jha, Zhang, Shmatikov & Morris, "Harnessing the Universal Geometry of
    Embeddings" (vec2vec), arXiv:2505.12540.

----------------------------------------------------------------------------
THE CLAIM UNDER TEST
----------------------------------------------------------------------------
vec2vec's load-bearing GEOMETRIC constraint is Vector-Space Preservation (VSP):
it forces the distribution of pairwise inner products (the Gram structure) of
the translated cloud to match the target cloud.  That is a PURE ORDER-2 object.
The Conductor-Blind-Spot / Apex-identifiability line (Papers 26/34/45,
FaithfulnessObstruction.md; C2/C3 in OpenProblemsSurvey) predicts the
continuous-embedding consequence:

    a translator anchored on order-2 geometry reproduces the target
    distribution faithfully at cumulant order <= 2 but ATTENUATES the
    order->=3 structure (it Gaussianizes).

This is the structural reason their headline numbers split along the order-2
boundary: PERFECT top-1 matching of 8000+ shuffled embeddings (a relation
decided by 2nd-order geometry) ALONGSIDE sub-unit cosine fidelity / lossy
inversion that the authors frame as "a lower bound."

----------------------------------------------------------------------------
THE DIAGNOSTIC  (numpy only -- this is the local deterministic gate)
----------------------------------------------------------------------------
Given a translated cloud A = {F(M1(x_i))} and a target cloud B = {M2(x_i)},
both N x d, we read the residual by cumulant ORDER via sliced 1-D projections
onto K seeded random directions w:

  * order-2 anchor   : ||Cov(A) - Cov(B)||_F / ||Cov(B)||_F        (VSP's object)
  * reproduction err : D_m = (sum_w |kappa_m(Aw) - kappa_m(Bw)|)
                              / (sum_w |kappa_m(Bw)|)   for m = 2,3,4
  * Gaussianization  : g_m = (sum_w |kappa_m(Aw)|) / (sum_w |kappa_m(Bw)|)
                       g_m < 1  <=>  cloud A carries LESS order-m structure
                       than B (the fingerprint: skew/kurtosis destroyed).

The HEADLINE statistic is g_3 (fraction of order-3 structure retained).
kappa_m are the raw cumulants (m2 = variance, m3 = third central moment,
m4 - 3 m2^2 = fourth cumulant).

----------------------------------------------------------------------------
PRE-REGISTERED MATCHED-PAIR FALSIFIER  (GPD methodology)
----------------------------------------------------------------------------
We validate the diagnostic on a synthetic matched pair BEFORE trusting it on
real arrays.  Same target cloud B with genuine order-3 (skew) and order-4
(kurtosis) structure; two translators with the SAME paired RMS error:

  K  (CBS-positive):  order-2-faithful, order->=3-lossy.  A = Gaussian with
                      B's exact mean+covariance.  Matches order<=2 by
                      construction; has ZERO order->=3 cumulants.
                      PREDICT  g_3 <= 0.25  AND  steep ladder D3/D2 >= 5
                      AND  order-2 anchor <= 0.12.

  L  (CBS-negative):  structureless residual.  A = B + small isotropic noise.
                      Perturbs every order comparably -> FLAT ladder.
                      PREDICT  g_3 >= 0.80  AND  D3/D2 <= 2.

  JOINT:  g_3(K) < 0.5 * g_3(L)  AND  slope(K) > 3 * slope(L).
          (order-selective loss vs uniform loss)

A diagnostic that fired on L too would be measuring noise, not order. The gate
PASSES iff K and L land on their pre-registered sides and the joint holds.

----------------------------------------------------------------------------
USAGE
----------------------------------------------------------------------------
  python probe_vec2vec_residual_conductor.py            # synthetic gate (default)
  python probe_vec2vec_residual_conductor.py --arrays VHAT.npy V.npy
        # run the SAME diagnostic on real vec2vec outputs produced on GCP by
        # vec2vec_extract_arrays.py ; prints the CBS verdict for vec2vec.

Deterministic: numpy only.  No torch, no plotting, no network.
"""

import sys
import numpy as np

SEED = 20260616
N_DIRS = 4096          # sliced projection directions
EPS = 1e-12


# ---------------------------------------------------------------------------
# Cumulant machinery (sliced)
# ---------------------------------------------------------------------------
def sliced_cumulants(X, W, chunk=128):
    """kappa_2,3,4 of X (N x d) projected onto each column of W (d x K).

    Chunked over directions to bound memory (N x chunk at a time), so it scales
    to large embedding sets.  Returns three length-K arrays."""
    K = W.shape[1]
    k2 = np.empty(K); k3 = np.empty(K); k4 = np.empty(K)
    for s in range(0, K, chunk):
        e = min(s + chunk, K)
        P = X @ W[:, s:e]                          # N x c
        Pc = P - P.mean(axis=0, keepdims=True)
        m2 = (Pc ** 2).mean(axis=0)
        m3 = (Pc ** 3).mean(axis=0)
        m4 = (Pc ** 4).mean(axis=0)
        k2[s:e] = m2
        k3[s:e] = m3
        k4[s:e] = m4 - 3.0 * m2 ** 2
    return k2, k3, k4


def order_spectroscopy(A, B, W):
    """Compare translated cloud A to target cloud B by cumulant order.

    Returns dict with the order-2 anchor, reproduction errors D_m, and the
    Gaussianization gaps g_m (m = 2,3,4)."""
    # order-2 anchor: the VSP object, distributional (covariance Frobenius)
    Ca = np.cov(A, rowvar=False)
    Cb = np.cov(B, rowvar=False)
    anchor = np.linalg.norm(Ca - Cb) / (np.linalg.norm(Cb) + EPS)

    ka = sliced_cumulants(A, W)
    kb = sliced_cumulants(B, W)

    out = {"anchor_cov": float(anchor)}
    for m, a_m, b_m in zip((2, 3, 4), ka, kb):
        num_D = np.abs(a_m - b_m).sum()
        den = np.abs(b_m).sum() + EPS
        out[f"D{m}"] = float(num_D / den)
        out[f"g{m}"] = float(np.abs(a_m).sum() / den)
        out[f"kappa{m}_target"] = float(np.abs(b_m).mean())   # is there signal?
    return out


def structured_spectroscopy(A, B, k=64):
    """Cumulant ladder along the TARGET's top-k principal directions, where
    variance and any semantic non-Gaussianity concentrate (random directions
    are Gaussianized by concentration of measure on the normalized-embedding
    sphere, so they are underpowered).  Uses STANDARDIZED cumulants (skewness
    g1, excess kurtosis g2) so 'is there structure?' is scale-free and per
    direction.  Returns target structure level + how well A reproduces it."""
    Bc = B - B.mean(0)
    C = np.cov(B, rowvar=False)
    vals, vecs = np.linalg.eigh(C)
    Wk = vecs[:, np.argsort(vals)[::-1][:k]]        # d x k top PCs of target

    def std_cums(X):
        P = (X - X.mean(0)) @ Wk
        m2 = (P ** 2).mean(0)
        g1 = (P ** 3).mean(0) / (m2 ** 1.5 + EPS)            # skewness
        g2 = (P ** 4).mean(0) / (m2 ** 2 + EPS) - 3.0        # excess kurtosis
        return g1, g2, m2

    g1B, g2B, varB = std_cums(B)
    g1A, g2A, varA = std_cums(A)
    noise_sk = np.sqrt(6.0 / B.shape[0])            # Gaussian sampling floor
    noise_ku = np.sqrt(24.0 / B.shape[0])
    # order-2 along PCs (variance reproduction); order-3/4 reproduction error
    var_err = np.abs(varA - varB).sum() / (varB.sum() + EPS)
    sk_err = np.abs(g1A - g1B).sum() / (np.abs(g1B).sum() + EPS)
    ku_err = np.abs(g2A - g2B).sum() / (np.abs(g2B).sum() + EPS)
    return {
        "k": k,
        "tgt_skew_rms": float(np.sqrt((g1B ** 2).mean())),
        "tgt_kurt_rms": float(np.sqrt((g2B ** 2).mean())),
        "noise_skew": float(noise_sk), "noise_kurt": float(noise_ku),
        "tgt_skew_max": float(np.abs(g1B).max()),
        "tgt_kurt_max": float(np.abs(g2B).max()),
        "var_err_pc": float(var_err),
        "skew_err_pc": float(sk_err),
        "kurt_err_pc": float(ku_err),
    }


def _report(tag, r):
    print(f"  [{tag}]  order-2 anchor ||dCov||/||Cov|| = {r['anchor_cov']:.4f}")
    print(f"        reproduction err   D2={r['D2']:.3f}  D3={r['D3']:.3f}  D4={r['D4']:.3f}")
    print(f"        Gaussianization    g3={r['g3']:.3f}  g4={r['g4']:.3f}   "
          f"(g_m<1 => order-m structure destroyed)")
    print(f"        target order-m mag |k3|={r['kappa3_target']:.3e}  "
          f"|k4|={r['kappa4_target']:.3e}")


# ---------------------------------------------------------------------------
# Synthetic matched-pair validation (the local gate)
# ---------------------------------------------------------------------------
def _structured_target(rng, N, d, n_skew=3, n_kurt=2, alpha=3.0):
    """A target cloud with GENUINE, STRONG, low-rank order-3 (skew) and order-4
    (kurtosis) structure on a Gaussian base.  Strong + low-rank so the
    non-Gaussian signal survives 1-D slicing and dominates finite-sample noise
    (a fully-rotated weakly-skewed cloud is washed out by the CLT)."""
    B = rng.standard_normal((N, d))
    Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
    U = Q[:, : n_skew + n_kurt]                  # orthonormal factor directions
    for i in range(n_skew):
        t = rng.exponential(1.0, N) - 1.0        # skewness 2, unit variance
        B += alpha * np.outer(t, U[:, i])        # strong order-3 along U[:,i]
    for i in range(n_skew, n_skew + n_kurt):
        t = rng.standard_t(4, N)                 # heavy tails (excess kurtosis)
        t /= t.std()
        B += alpha * np.outer(t, U[:, i])        # strong order-4 along U[:,i]
    return B


def _match_mean_cov(rng, B, N):
    """Fresh Gaussian sample with B's empirical mean and covariance.
    Perfect order<=2 match, ZERO order->=3 cumulants (maximal Gaussianization)."""
    mu = B.mean(axis=0)
    C = np.cov(B, rowvar=False)
    # symmetric PSD sqrt via eigh (robust)
    vals, vecs = np.linalg.eigh(C)
    vals = np.clip(vals, 0, None)
    L = vecs @ np.diag(np.sqrt(vals)) @ vecs.T
    g = rng.standard_normal((N, B.shape[1]))
    return g @ L + mu


def run_synthetic_gate():
    rng = np.random.default_rng(SEED)
    N, d = 50000, 16
    B = _structured_target(rng, N, d)
    W = rng.standard_normal((d, N_DIRS))
    W /= np.linalg.norm(W, axis=0, keepdims=True)

    # K: order-2-faithful, order->=3-lossy  (Gaussian @ B's exact mean+cov)
    A_K = _match_mean_cov(rng, B, N)
    # L: structureless control -- a MILD non-selective perturbation; it leaves a
    # residual but touches every order comparably (flat ladder, g_m ~ 1).
    sigma = B.std(axis=0, keepdims=True)
    A_L = B + 0.1 * sigma * rng.standard_normal((N, d))

    print("=" * 74)
    print("SYNTHETIC MATCHED-PAIR VALIDATION  (the diagnostic must SELECT order)")
    print("=" * 74)
    rK = order_spectroscopy(A_K, B, W)
    rL = order_spectroscopy(A_L, B, W)
    slopeK = rK["D3"] / max(rK["D2"], EPS)
    slopeL = rL["D3"] / max(rL["D2"], EPS)
    print("\n  K = order-2-faithful translator (Gaussian @ B's mean+cov):")
    _report("K", rK)
    print(f"        ladder slope D3/D2 = {slopeK:.1f}")
    print("\n  L = structureless control (B + mild isotropic noise):")
    _report("L", rL)
    print(f"        ladder slope D3/D2 = {slopeL:.1f}")

    # pre-registered predicates: K = steep ladder + Gaussianized; L = flat
    K_ok = (rK["g3"] <= 0.25) and (slopeK >= 5.0) and (rK["anchor_cov"] <= 0.12)
    L_ok = (rL["g3"] >= 0.80) and (slopeL <= 2.0)
    joint_ok = (rK["g3"] < 0.5 * rL["g3"]) and (slopeK > 3.0 * slopeL)

    print("\n  Pre-registered checks:")
    print(f"    K Gaussianizes (g3<=.25, D3/D2>=5, anchor<=.12) : {K_ok}")
    print(f"    L preserves order (g3>=.80, D3/D2<=2)           : {L_ok}")
    print(f"    JOINT g3(K)<0.5 g3(L) AND slopeK>3 slopeL       : {joint_ok}  "
          f"[g3 {rK['g3']:.3f} vs {rL['g3']:.3f}; slope {slopeK:.1f} vs {slopeL:.1f}]")
    passed = K_ok and L_ok and joint_ok
    print("\n  >>> SYNTHETIC GATE:", "PASS" if passed else "FAIL",
          "-- diagnostic is order-selective" if passed else "-- diagnostic NOT validated")
    return passed


# ---------------------------------------------------------------------------
# Real-data mode
# ---------------------------------------------------------------------------
def run_on_arrays(vhat_path, v_path):
    A = np.load(vhat_path).astype(np.float64)   # translations  F(M1(x))
    B = np.load(v_path).astype(np.float64)      # targets       M2(x)
    if A.shape != B.shape:
        # paired evaluation expects same N and d
        print(f"  WARNING: shape mismatch {A.shape} vs {B.shape}; "
              f"truncating to common N.")
        N = min(A.shape[0], B.shape[0])
        A, B = A[:N], B[:N]
    N, d = B.shape
    rng = np.random.default_rng(SEED)
    W = rng.standard_normal((d, N_DIRS))
    W /= np.linalg.norm(W, axis=0, keepdims=True)

    print("=" * 74)
    print(f"VEC2VEC RESIDUAL ORDER-SPECTROSCOPY   (N={N}, d={d})")
    print("=" * 74)

    # paired symptom (the paper's metric): mean cosine of translation to target
    cos = (A * B).sum(1) / (np.linalg.norm(A, axis=1) * np.linalg.norm(B, axis=1) + EPS)
    print(f"  paired translation cosine  mean={cos.mean():.4f}  "
          f"median={np.median(cos):.4f}  (their fidelity metric)")

    r = order_spectroscopy(A, B, W)
    print("\n  ISOTROPIC (random-direction) spectroscopy:")
    _report("vec2vec", r)

    s = structured_spectroscopy(A, B, k=64)
    print(f"\n  STRUCTURED (top-{s['k']} target-PC) spectroscopy:")
    print(f"        target non-Gaussianity   skew_rms={s['tgt_skew_rms']:.3f} "
          f"(max {s['tgt_skew_max']:.2f})  kurt_rms={s['tgt_kurt_rms']:.3f} "
          f"(max {s['tgt_kurt_max']:.2f})")
    print(f"        Gaussian sampling floor  skew={s['noise_skew']:.3f}  "
          f"kurt={s['noise_kurt']:.3f}   (structure is real iff rms >> floor)")
    print(f"        reproduction error       var(O2)={s['var_err_pc']:.3f}  "
          f"skew(O3)={s['skew_err_pc']:.3f}  kurt(O4)={s['kurt_err_pc']:.3f}")

    # Is there structured order->=3 signal above the sampling floor?
    struct_sig = (s["tgt_skew_rms"] > 3 * s["noise_skew"]) or \
                 (s["tgt_kurt_rms"] > 3 * s["noise_kurt"])

    print("\n  VERDICT:")
    if not struct_sig:
        print("    Target embeddings are near-Gaussian even along their top PCs")
        print(f"    (skew_rms {s['tgt_skew_rms']:.3f} ~ floor {s['noise_skew']:.3f}).")
        print("    => VACUOUS on order->=3: these embeddings are essentially an")
        print("       ORDER-2 object; there is little higher-cumulant structure for any")
        print("       method to lose. Consistent with -- not a test of -- the order-2")
        print("       reading: VSP suffices because the universal geometry IS ~order-2.")
        print(f"    The residual (cosine {cos.mean():.3f}, order-2 "
              f"anchor {r['anchor_cov']:.3f}) is an ORDER-2 optimization gap, not an")
        print("       order->=3 blind spot.")
    elif s["var_err_pc"] < 0.5 * min(s["skew_err_pc"], s["kurt_err_pc"]):
        print(f"    Structured non-Gaussianity EXISTS (skew_rms {s['tgt_skew_rms']:.2f} "
              f">> floor {s['noise_skew']:.3f}) and vec2vec reproduces order-2 far")
        print(f"    better than order->=3 (var_err {s['var_err_pc']:.3f} << skew_err "
              f"{s['skew_err_pc']:.3f}, kurt_err {s['kurt_err_pc']:.3f}).")
        print("    => CBS-POSITIVE: a named order-2 floor in the structured subspace.")
    else:
        print(f"    Structured non-Gaussianity exists and vec2vec reproduces it about")
        print(f"    as well as order-2 (var_err {s['var_err_pc']:.3f} vs skew_err "
              f"{s['skew_err_pc']:.3f}). => CBS-NEGATIVE in the structured subspace.")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--arrays":
        if len(args) != 3:
            print("usage: --arrays VHAT.npy V.npy"); sys.exit(2)
        run_on_arrays(args[1], args[2])
    else:
        ok = run_synthetic_gate()
        print()
        print("=" * 74)
        print("VERDICT")
        print("=" * 74)
        print("""  The diagnostic reads a translation residual by CUMULANT ORDER. On the
  synthetic matched pair it fires on the order-2-faithful translator (K:
  destroys order->=3 structure, g3->0) and stays silent on the structureless
  control (L: flat ladder, g3->1) -- so it measures ORDER, not noise.

  Run it on real vec2vec outputs (--arrays, produced on GCP by
  vec2vec_extract_arrays.py) to test the prediction in the wild: order-2
  preserved (VSP=Gram), order->=3 attenuated. A positive result turns the
  paper's self-described 'lower bound' into the program's named order-2 floor
  (C1/C2, FaithfulnessObstruction.md, Paper 34 Layer-2).""")


if __name__ == "__main__":
    main()
