"""probe_pinfF_lifecycle_parity.py -- lifecycle supplement: the two-branch (parity) collapse.

DIAGNOSIS UNDER TEST: C1' fired (dispersion 0.79, normalization-independent) because the
interior ladder interleaves TWO parity towers; at fixed eig an even rung and an odd rung
have different ages -> sigma(eig) is double-valued.  Split by eigenvector parity and
re-test the collapse per branch.

PRE-REGISTERED:
  D1: within-parity median dispersion <= 0.35 in the safe bins (vs 0.79 mixed) at the four
      clean windows  ->  TWO-BRANCH master curve data-established.
      FALSIFIER: stays >= 0.6  ->  scatter is not parity; self-similarity survives only at
      the aggregate level (laws c and flow median) -- reported as the honest endpoint.
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

src2 = open("empirical/p_infinity/probe_pinfF_f5_sampling.py", encoding="utf-8").read()
exec(src2.split('# ---- zeros')[0])
src3 = open("empirical/p_infinity/probe_pinfF_innovation_chain.py", encoding="utf-8").read()
block = src3[src3.index("def point_basis_form"):src3.index('print("== building')]
exec(block)

CASES = [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27)]
cl = {}
print("== parity-resolved clouds (four clean windows) ==")
for lam, N in CASES:
    QW, L = build_QW(mp.mpf(repr(float(lam))), N, True)
    K, x = point_basis_form(QW, N, L)
    order, _ = center_out_order(x, L)
    dim = K.shape[0]
    interior, pair = order[:dim - 2], order[dim - 2:]
    e = np.zeros(dim); e[pair] = 1 / np.sqrt(2)
    Ki = K[np.ix_(interior, interior)]
    q = K[interior][:, pair].sum(axis=1) / np.sqrt(2)
    bare = float(e @ K @ e)
    ev, w_ = np.linalg.eigh(Ki)
    sig = (w_.T @ q)**2 / ev / bare
    # parity scores: reflection i -> (dim - i) mod dim on the grid; restrict to interior
    refl_full = {i: (dim - i) % dim for i in range(dim)}
    pos = {idx: a for a, idx in enumerate(interior)}
    par = np.zeros(len(ev))
    for k in range(len(ev)):
        v = w_[:, k]
        s_ = 0.0
        for a, idx in enumerate(interior):
            r = refl_full[idx]
            if r in pos:
                s_ += v[a] * v[pos[r]]
        par[k] = s_              # ~ +1 even, ~ -1 odd
    keep = ev > 1e-11
    cl[lam] = dict(eig=ev[keep], sig=sig[keep], par=par[keep])
    ne = int((par[keep] > 0.3).sum()); no = int((par[keep] < -0.3).sum())
    amb = int(keep.sum() - ne - no)
    print(f"   lam={lam}: points={keep.sum()} (even {ne}, odd {no}, ambiguous {amb})")


def disp_table(branch):
    bins = 10.0**np.arange(-6, -0.9, 1.0)
    disp = []
    rows = []
    for b0, b1 in zip(bins, bins[1:]):
        mus = []
        for lam, _ in CASES:
            d = cl[lam]
            if branch == "even":
                m = (d['eig'] >= b0) & (d['eig'] < b1) & (d['sig'] > 1e-7) & (d['par'] > 0.3)
            else:
                m = (d['eig'] >= b0) & (d['eig'] < b1) & (d['sig'] > 1e-7) & (d['par'] < -0.3)
            if m.sum():
                mus.append(float(np.mean(d['sig'][m])))
        if len(mus) >= 2:
            mu, sd = np.mean(mus), np.std(mus)
            disp.append(sd / mu)
            rows.append((b0, mu, sd / mu, len(mus)))
    return disp, rows


print("\n== D1: collapse per parity branch ==")
meds = {}
for br in ("even", "odd"):
    disp, rows = disp_table(br)
    med = float(np.median(disp)) if disp else np.nan
    meds[br] = med
    print(f"   {br:5s}: median dispersion = {med:.3f}   "
          + "  ".join(f"[1e{int(np.log10(b0)):+d}] mu={mu:.3f} d={dd:.2f} (n={n})"
                      for b0, mu, dd, n in rows))
ok = all(np.isfinite(m) and m <= 0.35 for m in meds.values())
partial = any(np.isfinite(m) and m <= 0.35 for m in meds.values())
print("\n   D1: " + ("SURVIVES -- TWO-BRANCH master curve data-established"
                     if ok else ("PARTIAL -- one branch collapses; see tables"
                                 if partial else
                                 "FIRED -- scatter is not parity; aggregate-only self-similarity")))
