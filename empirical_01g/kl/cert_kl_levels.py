"""Paper 01g, Section 12.10 (climbing the levels) -- certificate.

2026-10-17. Criteria declared before first execution. Exploratory probes (k <= 9) preceded
this script in the same session; the quadratic-gain band of L6 was declared for k = 10..12
in a dated prediction file before those levels were computed.

Operator (one-step form of Proposition 12.14), on live residues r mod 3^k (3 not dividing r):
    Phi_k(c)_r = 2^-g c_{2r} + [r = 2 mod 3] (3/2)^g min_{t in L_k(r)} c_t,
L_k(r) = the three lifts mod 3^k of (2r-1)/3 mod 3^(k-1); c = 0 on residues divisible by 3.
gamma_k = critical exponent, c_k = its Perron vector (Phi_k(c_k) = c_k), rho_k = lift retention
(principal classes, as in Proposition 12.16). c' = lift of c_k to level k+1, g = Phi_{k+1}(c') - c'
at gamma_k, u = left Perron vector of the optimal policy of Phi_{k+1} at gamma_k,
G_k = <u,g>/<u,c'>, H_k = sum g / sum c'.

L1  gamma_k strictly increasing for 3 <= k <= 13; gamma_9..gamma_13 agree with kl_cert_summary.json
    (critical values) to 5e-6.
L2  Lifted vector: g >= -1e-12 max c' everywhere, and g > 0 somewhere, for 3 <= k <= 12.
L3  Exact lift-gain formula: |(rho_{k+1}(gamma_k) - 1) - G_k| <= 1e-6 G_k for 3 <= k <= 12, where
    rho_{k+1}(gamma_k) is computed by power iteration on Phi_{k+1} and G_k from the left vector.
L4  Gain inequality: gamma_{k+1} - gamma_k >= log2(1 + G_k) for 3 <= k <= 12.
L5  Haar gain bound: H_k >= c0(gamma_k)(1 - rho_k), c0(g) = (3/2)^g / (3(1 + 2^-g)), 3 <= k <= 12;
    and c0 >= 1/4 on [0.6, 1].
L6  Quadratic gain law: G_k / (1 - rho_k)^2 lies in [0.60, 1.00] for 3 <= k <= 12.
L7  Identity function R(g) = 3(1 - 4^-g)/((3/2)^g + (3/4)^g): R(1) = 1, R < 1 on [0, 1), and
    R' >= 1/4 on [0.6, 1] (grid of 4001 points plus a Lipschitz bound on R').
L8  Frame horizon: n = 9591468737351909375 (OEIS A002072, p = 97) has n and n+1 97-smooth,
    2n+1 = 19182937474703818751 (Luca-Najman), and n < 2^68 / 3.
"""
import numpy as np, math, sys, json, time
from pathlib import Path
from sympy import factorint
sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows = []; t0 = time.perf_counter()
def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)

def build(k):
    M = 3**k; r = np.arange(M, dtype=np.int64)
    q = ((2*r - 1)//3) % (M//3)
    return dict(k=k, M=M, dbl=(2*r) % M, live=(r % 3 != 0), odd=(r % 3 == 2),
                lifts=np.stack([q + j*(M//3) for j in range(3)], axis=1) % M)

def phi(B, g, c):
    return np.where(B['live'], 2.0**(-g)*c[B['dbl']] + np.where(B['odd'], 1.5**g*c[B['lifts']].min(1), 0.0), 0.0)

def perron(B, g, c=None, tol=1e-15, maxit=400000):
    c = B['live'].astype(float) if c is None else c.copy(); c /= c.sum(); s_old = 0.0
    for it in range(maxit):
        n = phi(B, g, c); s = n.sum(); n /= s
        if it > 60 and abs(s - s_old) < tol and np.abs(n - c).max() < 1e-13 * n.max():
            return s, n
        s_old = s; c = n
    raise RuntimeError("no convergence")

def critical(B, c=None, lo=0.3, hi=1.0):
    while hi - lo > 1e-11:
        mid = (lo + hi)/2; s, c2 = perron(B, mid, c)
        if s >= 1: lo, c = mid, c2
        else: hi = mid
    return lo, perron(B, lo, c)[1]

def left_vector(B, g, pol, tol=1e-15, maxit=400000):
    M = B['M']; lv = np.nonzero(B['live'])[0]; od = np.nonzero(B['odd'])[0]
    tgt = pol[od]; keep = (tgt % 3 != 0); od, tgt = od[keep], tgt[keep]   # arrows into dead classes carry c = 0
    u = B['live'].astype(float); u /= u.sum(); s_old = 0.0
    for it in range(maxit):
        n = np.bincount(B['dbl'][lv], weights=2.0**(-g)*u[lv], minlength=M) + np.bincount(tgt, weights=1.5**g*u[od], minlength=M)
        s = n.sum(); n /= s
        if it > 60 and abs(s - s_old) < tol and np.abs(n - u).max() < 1e-14 * n.max():
            return s, n
        s_old = s; u = n
    raise RuntimeError("no convergence (left)")

def retention(B, c):
    M = B['M']; r = np.arange(M); b = np.arange(M//3)
    aux = np.minimum(np.minimum(c[b], c[b + M//3]), c[b + 2*(M//3)])
    return (aux[b % 3 == 2].sum()/3**(B['k']-2)) / (c[r % 3 == 2].sum()/3**(B['k']-1))

KTOP = 13
Bs = {}; crit = {}
for k in range(3, KTOP + 1):
    Bs[k] = build(k); crit[k] = critical(Bs[k]); print(f"  level {k}: gamma = {crit[k][0]:.9f}", flush=True)
gam = [crit[k][0] for k in range(3, KTOP + 1)]
summ = json.loads((HERE / "kl_cert_summary.json").read_text())
agree = all(abs(crit[k][0] - summ[str(k)]["gamma_crit"]) < 5e-6 for k in range(9, 14) if str(k) in summ)
check("L1 strict monotonicity of gamma_k", all(b > a for a, b in zip(gam, gam[1:])) and agree,
      f"gamma_3..13 = {[round(x, 6) for x in gam]}; agree with Section 12.8 summary: {agree}")

data = []; ok2 = ok3 = ok4 = ok5 = ok6 = True
for k in range(3, KTOP):
    gk, ck = crit[k]; B1 = Bs[k+1]; M1 = B1['M']
    cl = ck[np.arange(M1) % 3**k]
    gain = phi(B1, gk, cl) - cl
    ok2 &= gain.min() >= -1e-12*cl.max() and gain.max() > 1e-9*cl.max()
    rho1, c1 = perron(B1, gk, cl)
    li = B1['lifts']; pol = li[np.arange(M1), c1[li].argmin(1)]
    lam_u, u = left_vector(B1, gk, pol)
    G = (u*gain).sum()/(u*cl).sum(); H = gain.sum()/cl.sum()
    rk = retention(Bs[k], ck); loss = 1 - rk
    c0 = 1.5**gk/(3*(1 + 2**(-gk)))
    dg = crit[k+1][0] - gk
    ok3 &= abs((rho1 - 1) - G) <= 1e-6*G
    ok4 &= dg >= math.log2(1 + G)
    ok5 &= H >= c0*loss
    q = G/loss**2; ok6 &= 0.60 <= q <= 1.00
    rk1 = retention(Bs[k+1], crit[k+1][1])
    data.append(dict(k=k, gamma=gk, dgamma=dg, loss=loss, G=G, H=H, nu=G/H, quad=q, logistic=(rk1-rk)/loss**2, rho_next_minus_1=rho1-1, policy_rho_minus_1=lam_u-1))
    print(f"  k={k}: dgamma={dg:.6f} 1-rho={loss:.5f} G={G:.4e} (rho_k+1-1={rho1-1:.4e}) H={H:.4e} nu={G/H:.4f} k*nu={k*G/H:.3f} G/(1-rho)^2={q:.4f} (rho_k+1 - rho_k)/(1-rho)^2={(rk1-rk)/loss**2:.4f}", flush=True)
check("L2 lifted vector is a supersolution with nonzero gain", ok2, "g >= 0, g != 0 for k = 3..12")
check("L3 exact lift-gain formula", ok3, "rho_{k+1}(gamma_k) - 1 = <u,g>/<u,c'> to 1e-6 relative")
check("L4 gain inequality", ok4, "gamma_{k+1} - gamma_k >= log2(1 + G_k)")
gg = np.linspace(0.6, 1.0, 4001); c0s = 1.5**gg/(3*(1 + 2**(-gg)))
check("L5 Haar gain bound", ok5 and c0s.min() >= 0.25, f"H_k >= c0 (1-rho_k); min c0 on [0.6,1] = {c0s.min():.4f}")
check("L6 quadratic gain law", ok6, f"G/(1-rho)^2 = {[round(d['quad'], 3) for d in data]}")

R = lambda g: 3*(1 - 4.0**(-g))/(1.5**g + 0.75**g)
def dR(g, h=1e-6): return (R(g + h) - R(g - h))/(2*h)
grid = np.linspace(0.6, 1.0, 4001); d = np.array([dR(x) for x in grid])
d2 = np.abs(np.diff(d)).max()/(grid[1] - grid[0])          # empirical Lipschitz constant of R'
lip_margin = d.min() - d2*(grid[1] - grid[0])
below = all(R(x) < 1 for x in np.linspace(0, 1 - 1e-6, 20001))
check("L7 identity function", abs(R(1) - 1) < 1e-15 and below and lip_margin >= 0.25,
      f"R(1)={R(1):.16f}; R<1 on [0,1); min R' on [0.6,1] = {d.min():.4f} (margin {lip_margin:.4f})")

n = 9591468737351909375
f1, f2 = factorint(n), factorint(n + 1)
check("L8 frame horizon at 97", max(f1) <= 97 and max(f2) <= 97 and 2*n + 1 == 19182937474703818751 and 3*n < 2**68,
      f"n = {f1}, n+1 = {f2}; 3n/2^68 = {3*n/2**68:.4f}")

el = time.perf_counter() - t0; npass = sum(r['pass'] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {el:.1f} s")
(HERE / "cert_kl_levels_results.json").write_text(json.dumps({"rows": rows, "levels": data, "elapsed_s": el}, indent=2))
sys.exit(0 if npass == len(rows) else 1)
