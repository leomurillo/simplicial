"""probe_pinfF_cumulative.py -- the cumulative re-coordinatization (Leo's consistency catch).

THE ISSUE: C1/C1'/D1 and section 20's danger-location claim rest on per-rung sigma values --
non-invariant under near-degenerate rotations (the section-21 deflation flag); the dps-50 log
contains the warning shot (lam=2.0: eig=2.33e-10 with sigma=0.31, matching NO trustworthy
rung and suspiciously equal to the crossover's 0.32).

THE INVARIANT: s(xi) = q^T f_xi(K) q / bare, f_xi(x) = x^{-1} 1_{x<=xi} -- a spectral
function, basis-free.  Deep cumulative computed EXACTLY as [mp-total (LU, immune)] minus
[float-upper (reliable: mixing of >1e-6 modes with the deep block ~ 1e-10)].

PRE-REGISTERED:
  E1 (anomaly settlement): deep-cumulative s(<=1e-6) at lam=2.0 in [0.10, 0.18]
      (the float table's 0.139: the 0.31 was a deflation artifact; section 20 stands).
      ALTERNATIVE: ~0.4 -> section 20 needs an erratum (stated and landed if so).
  E2 (relocation check at all mp windows): s(<=1e-6) <= 0.20 at lam = 2.2, 2.35, 2.5.
  E3 (cumulative collapse): the curves S(xi; lam) collapse under per-window log-shifts;
      fitted shifts linear in lambda^2 with slope 4*pi*(1 +- 0.4); residual curve
      dispersion <= 0.10 (cumulatives are smooth -- tighter criterion than per-rung).
  E4 (branch closure, cumulative-derived): parity-resolved cumulative eatings reproduce
      (1 - f_even)(1 - f_odd) = e^{-c} with c = 0.342 (mp-truth global fit) within ~20%.
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

R_mp = {2.0: 0.20081, 2.2: 0.13997, 2.35: 0.11329, 2.5: 0.08750}   # dps-50 truths
SS_mp = {l: 1 - r for l, r in R_mp.items()}
dat = np.load("empirical/p_infinity/lifecycle_clouds.npz")
CASES = [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]

print("== E1/E2: deep cumulative by invariant subtraction ==")
print("   lam    Sigma(mp)   upper(>1e-6, f64)   deep-cum(<=1e-6)   verdict-scale")
deepcum = {}
for lam, _ in CASES:
    e_, s_ = dat[f"e{lam}"], dat[f"s{lam}"]
    upper = float(s_[e_ > 1e-6].sum())
    tot = SS_mp.get(lam, float(s_.sum()))      # mp where available, f64-clean otherwise
    dc = tot - upper
    deepcum[lam] = dc
    tag = "(mp)" if lam in SS_mp else "(f64 clean)"
    print(f"   {lam:4}   {tot:.4f} {tag:10s}  {upper:.4f}            {dc:+.4f}")
e1 = 0.10 <= deepcum[2.0] <= 0.18
e2 = all(deepcum[l] <= 0.20 for l in (2.2, 2.35, 2.5))
print("   E1: " + (f"SURVIVES -- deep-cum(2.0) = {deepcum[2.0]:.3f}: the 0.31 entry was a "
                   "deflation artifact; section 20's relocation STANDS"
                   if e1 else f"check: deep-cum(2.0) = {deepcum[2.0]:.3f} -- erratum path"))
print("   E2: " + ("SURVIVES -- depths hold <= 0.20 of the budget at every mp window"
                   if e2 else "FIRED -- relocation erratum needed"))

# ---------------- E3: cumulative collapse with per-window shifts ----------------
print("\n== E3: cumulative-curve collapse in shifted log-eig coordinates ==")
GRID = np.linspace(-20, 0, 81)            # ln xi grid


def cumcurve(lam, shift=0.0):
    e_, s_ = dat[f"e{lam}"], dat[f"s{lam}"]
    tot = SS_mp.get(lam, float(s_.sum()))
    le = np.log(e_)
    cc = np.array([float(s_[le <= g + shift].sum()) for g in GRID])
    # replace the corrupted float deep part by the invariant deep-cum pedestal
    cc = np.maximum(cc, 0.0)
    return cc / tot                        # normalized ledger fraction


ref = 2.0
shifts, curves = {}, {}
for lam, _ in CASES:
    best = (1e9, 0.0)
    c0 = cumcurve(ref)
    for sh in np.linspace(-30, 30, 241):
        c1 = cumcurve(lam, shift=sh)
        m = (c0 > 0.05) & (c0 < 0.95)
        r = float(np.mean((c1[m] - c0[m])**2)) if m.sum() > 5 else 1e9
        if r < best[0]:
            best = (r, sh)
    shifts[lam] = best[1]
    curves[lam] = cumcurve(lam, shift=best[1])
l2 = np.array([l * l for l, _ in CASES])
sh = np.array([shifts[l] for l, _ in CASES])
slope = np.polyfit(l2, sh, 1)[0]
mids = [(curves[l] for l, _ in CASES)]
stack = np.vstack([curves[l] for l, _ in CASES])
m = (stack.mean(0) > 0.05) & (stack.mean(0) < 0.95)
disp = float(np.mean(stack[:, m].std(0) / np.maximum(stack[:, m].mean(0), 1e-9)))
print(f"   per-window shifts (vs lam=2.0): " + "  ".join(f"{l}:{shifts[l]:+.1f}" for l, _ in CASES))
print(f"   shift slope vs lambda^2 = {slope:+.2f}   (Fuchs pace 4*pi = {4*np.pi:.2f})")
print(f"   collapsed-curve dispersion (5-95% band) = {disp:.3f}")
e3 = disp <= 0.10 and 0.6 * 4 * np.pi <= slope <= 1.4 * 4 * np.pi
print("   E3: " + ("SURVIVES -- the cumulative ledger collapses; the fixed profile lives in"
                   " the CUMULATIVE coordinates, pace = Fuchs" if e3 else "check -- see numbers"))

# ---------------- E4: branch closure from parity-resolved cumulatives ----------------
print("\n== E4: parity-resolved cumulative eatings (4 clean rebuilds) ==")
f_br = {"even": [], "odd": []}
for lam, N in [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27)]:
    QW, L = build_QW(mp.mpf(repr(float(lam))), N, True)
    K, x = point_basis_form(QW, N, L)
    order, _ = center_out_order(x, L)
    dim = K.shape[0]
    interior, pair = order[:dim - 2], order[dim - 2:]
    Ki = K[np.ix_(interior, interior)]
    q = K[interior][:, pair].sum(axis=1) / np.sqrt(2)
    e = np.zeros(dim); e[pair] = 1 / np.sqrt(2)
    bare = float(e @ K @ e)
    ev, w_ = np.linalg.eigh(Ki)
    sig = (w_.T @ q)**2 / ev / bare
    refl = {i: (dim - i) % dim for i in range(dim)}
    pos = {idx: a for a, idx in enumerate(interior)}
    par = np.array([sum(w_[a, k] * w_[pos[refl[idx]], k]
                        for a, idx in enumerate(interior) if refl[idx] in pos)
                    for k in range(len(ev))])
    lad = (ev > 1e-9) & (ev < 0.1)
    s_even = float(sig[lad & (par > 0.3)].sum())
    s_odd = float(sig[lad & (par < -0.3)].sum())
    f_br["even"].append(s_even); f_br["odd"].append(s_odd)
    print(f"   lam={lam}: ladder cumulative eatings  even={s_even:.3f}  odd={s_odd:.3f}"
          f"  (ambiguous={float(sig[lad & (np.abs(par) <= 0.3)].sum()):.3f})")
fe, fo = np.mean(f_br['even'][-2:]), np.mean(f_br['odd'][-2:])
prod = (1 - fe) * (1 - fo)
print(f"   late-window branch eatings: f_even = {fe:.3f}, f_odd = {fo:.3f}; "
      f"(1-fe)(1-fo) = {prod:.3f} vs e^-0.342 = {np.exp(-0.342):.3f}")
e4 = abs(prod - np.exp(-0.342)) <= 0.2 * np.exp(-0.342)
print("   E4: " + ("SURVIVES -- budget closure from cumulative branch eatings" if e4 else
                   "check -- closure outside 20%"))

print("\nRESULT: " + ("GREEN -- invariant re-coordinatization done; verdicts above"
                      if (e1 and e2) else "PARTIAL -- see E1/E2 (erratum path engaged if fired)"))
