"""
Paper 56, Section 4.4 — post-diagnosis (NOT BLIND) regression form of the 3+1 Regge hinge test.

Criteria were written into the RUN LOG of p56b_regge_cert.py before this script was first run:
  R3'  slope of dS on (eta_par dc_par + eta_perp dc_perp), through the origin, all R in [3, 7.5], k = 5, 7 jointly,
       in [0.85, 1.15];
  R4'  slope of dc_total on sigma_b (-(2/3) delta R^2), same data, in [0.75, 1.3];
  R5'  HEADLINE slope of dS on eta (-(2/3) delta R^2), same data, in [0.75, 1.3]; per-k slopes and standard errors reported.
Data: the per-ball rows of the run-1 transcript p56b_run1.log (k, R, n, S, c_par, c_perp); the reference fits and the
coefficients are recomputed exactly as in p56b_regge_cert.py (the fit helper is copied verbatim).
"""
import sys
import re
import math
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

def fit(xs, ys, powers):
    X = np.vstack([xs ** p for p in powers]).T
    coef, *_ = np.linalg.lstsq(X, ys, rcond=None)
    resid = ys - X @ coef
    dof = max(len(xs) - len(powers), 1)
    cov = np.linalg.inv(X.T @ X) * float(resid @ resid) / dof
    return coef, np.sqrt(np.diag(cov))

rows = {5: [], 6: [], 7: []}
pat = re.compile(r"k=(\d) R=([\d.]+) n=\s*(\d+) S=([\d.]+) c_par=(\d+) c_perp=(\d+)")
for line in open("p56b_run1.log", encoding="utf-8"):
    m = pat.search(line)
    if m:
        k, R, n, S, cp, cq = m.groups()
        rows[int(k)].append((float(R), float(n), float(S), float(cp), float(cq)))
D = {k: np.array(v) for k, v in rows.items()}
assert all(len(D[k]) == 19 for k in D), {k: len(D[k]) for k in D}

R6, n6, S6, cp6, cq6 = D[6].T
A = np.vstack([cp6, cq6, np.ones_like(cp6)]).T
(eta_par, eta_perp, s0), *_ = np.linalg.lstsq(A, S6, rcond=None)
x13 = n6 ** (1 / 3)
fS, _ = fit(x13, S6, [2, 1, 0]); fp_, _ = fit(x13, cp6, [2, 1, 0]); fq_, _ = fit(x13, cq6, [2, 1, 0])
ref = lambda f, n: f[0] * (n ** (1 / 3)) ** 2 + f[1] * n ** (1 / 3) + f[2]
aS, _ = fit(R6, S6, [2, 1, 0]); eta_c = aS[0] / (4 * math.pi)
sig_b = float(np.mean((cp6 + cq6) / (4 * math.pi * R6 ** 2)))

def slope0(x, y):
    b = float(x @ y / (x @ x))
    r = y - b * x
    se = math.sqrt(float(r @ r) / max(len(x) - 1, 1) / float(x @ x))
    return b, se

X3, Y3, X4, Y4, X5, Y5 = [], [], [], [], [], []
per_k = {}
for k, dl in ((5, math.pi / 3), (7, -math.pi / 3)):
    Rk, nk, Sk, cpk, cqk = D[k].T
    dS = Sk - ref(fS, nk); dcp = cpk - ref(fp_, nk); dcq = cqk - ref(fq_, nk)
    jac = -(2 / 3) * dl * Rk ** 2
    per_k[k] = (slope0(eta_par * dcp + eta_perp * dcq, dS), slope0(sig_b * jac, dcp + dcq), slope0(eta_c * jac, dS))
    X3 += list(eta_par * dcp + eta_perp * dcq); Y3 += list(dS)
    X4 += list(sig_b * jac); Y4 += list(dcp + dcq)
    X5 += list(eta_c * jac); Y5 += list(dS)
s3 = slope0(np.array(X3), np.array(Y3)); s4 = slope0(np.array(X4), np.array(Y4)); s5 = slope0(np.array(X5), np.array(Y5))
print(f"   eta_par={eta_par:.6f} eta_perp={eta_perp:.6f} eta(continuum area)={eta_c:.6f} sigma_b={sig_b:.4f}")
for k in (5, 7):
    a, b, c = per_k[k]
    print(f"   k={k}: R3' slope {a[0]:.3f}+-{a[1]:.3f}; R4' slope {b[0]:.3f}+-{b[1]:.3f}; R5' slope {c[0]:.3f}+-{c[1]:.3f}")
check("R3' [numerics, NOT BLIND] dS = eta x bond deficit (joint slope in [0.85, 1.15])", 0.85 <= s3[0] <= 1.15,
      f"slope {s3[0]:.4f} +- {s3[1]:.4f}")
check("R4' [counting + fit, NOT BLIND] bond deficit = sigma_b x Jacobson area deficit (joint slope in [0.75, 1.3])",
      0.75 <= s4[0] <= 1.3, f"slope {s4[0]:.4f} +- {s4[1]:.4f}")
check("R5' [numerics, NOT BLIND] HEADLINE dS|_n = eta x delta A|_V (joint slope in [0.75, 1.3])", 0.75 <= s5[0] <= 1.3,
      f"slope {s5[0]:.4f} +- {s5[1]:.4f}")
print()
print(f"TOTAL (post-diagnosis): {sum(res)}/{len(res)} PASS")
