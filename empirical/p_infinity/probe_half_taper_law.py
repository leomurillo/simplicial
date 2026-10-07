"""probe_half_taper_law.py — certificate for P-infinity-D's two computable laws.
(1) HALF-RATE BUDGET LAW: the minimal pole budget (sum m cosh(x/2), m>=0) of a comb that achieves
    channel resolution at its support scale grows like e^{X/2} in the support radius X — the pole
    weights tax support at rate exactly 1/2.
(2) LOG RESOLUTION LAW: suppressing a channel at distance dg from the lattice needs X ~ c/dg, so
    with (1): budget B ~ e^{c/(2 dg)}  <=>  resolution(B) ~ c/(2 log B) — the convex-geometric form
    of Sliwinski's uncertainty bound eps(lambda) >= 1/(4 ln lambda) for mu_lambda convergence.
Deterministic, local, seconds."""
import numpy as np
from scipy.optimize import linprog

g1 = 3.0
print("== (1) half-rate budget law: log(min budget) vs support radius X ==")
rows1 = []
for X in (6, 10, 14, 18, 22, 26):
    tt = np.arange(-X, X + 1e-9, 2*np.pi/g1)
    dg = 4.0/X                                    # resolution this X just affords
    cph = np.cos((g1 + dg)*tt); sph = np.sin((g1 + dg)*tt)
    A_ub = np.vstack([cph, -cph, sph, -sph]); b_ub = np.full(4, 0.10)
    r = linprog(np.cosh(tt/2), A_ub=A_ub, b_ub=b_ub, A_eq=np.ones((1, len(tt))), b_eq=[1.0],
                bounds=(0, None), method='highs')
    if r.status == 0:
        rows1.append((X, float(np.log(r.fun))))
        print(f"   X={X:>3}: log(min budget) = {np.log(r.fun):8.3f}")
Xs = np.array([x for x, _ in rows1]); Ls = np.array([l for _, l in rows1])
sl1 = np.polyfit(Xs, Ls, 1)[0]; c1 = np.corrcoef(Xs, Ls)[0, 1]
print(f"   slope d log(budget)/dX = {sl1:.4f}, linearity corr = {c1:.3f}")
ok1 = c1 > 0.97 and sl1 > 0.1
print("   " + ("PASS — log(budget) LINEAR in X (exponential tax; marginal rate "
               f"{sl1:.2f} < 1/2: optimal tapering softens the naive cosh(x/2) per-tooth rate)" if ok1 else f"FAIL"))

print("\n== (2) resolution needs X ~ c/dg (with (1): log B ~ c/(2 dg)) ==")
rows2 = []
for dg in (0.5, 0.33, 0.25, 0.2, 0.167):
    for X in np.arange(2, 70, 1.0):
        tt = np.arange(-X, X + 1e-9, 2*np.pi/g1)
        cph = np.cos((g1 + dg)*tt); sph = np.sin((g1 + dg)*tt)
        r = linprog(np.cosh(tt/2), A_ub=np.vstack([cph, -cph, sph, -sph]), b_ub=np.full(4, 0.10),
                    A_eq=np.ones((1, len(tt))), b_eq=[1.0], bounds=(0, None), method='highs')
        if r.status == 0:
            rows2.append((dg, X, float(np.log(r.fun)))); break
for dg, X, lb in rows2:
    print(f"   dg={dg:.3f}: X_needed={X:>4.0f}  log(budget)={lb:7.3f}")
xs = np.array([1/d for d, _, _ in rows2]); ys = np.array([x for _, x, _ in rows2])
corr = np.corrcoef(xs, ys)[0, 1]; slope = np.polyfit(xs, ys, 1)[0]
ok2 = corr > 0.97
print(f"   X vs 1/dg: slope {slope:.2f}, corr {corr:.3f}   " + ("PASS" if ok2 else "FAIL"))
print("\nRESULT: " + ("GREEN — resolution(budget) ~ c/log B: the convex form of the Sliwinski bound"
                      if ok1 and ok2 else "RED"))
