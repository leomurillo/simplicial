"""probe_pinfF_f7_diagnose.py -- criterion-vs-mathematics diagnosis of the two fired falsifiers.

D1 (R2 identity): rebuild the lambda=3 off-E full-form minimizer; zero-side partial sums to
    J=80 with the convergence curve.  HYPOTHESIS: the 9% gap at J=40 is the slow tail of a
    SPREAD profile (unlike rep_1's 98% self-spike); the curve should keep climbing toward
    QW(min) = 0.6111.  Decision: |QW - S_80| < |QW - S_40| and a fitted 1/T-type tail
    extrapolation closing the gap -> criterion (tail), not mathematics.
D2 (R2 share): report the per-zero anatomy of the minimizer's zero-side mass (which zeros
    carry it) -- the near-critical-sampling reading predicts mass SPREAD over many resolved
    zeros (no single spike), with partial cancellation everywhere.
D3 (R4 exponent): extend the gap-collapse model to gaps far below resolution and fit ONLY
    sub-resolution rows.  PREDICTION: exponent -> 2.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

exec(open("empirical/p_infinity/probe_pinfF_f7_absorption.py").read().split(
    'print("harvesting zeros')[0])      # reuse builders: build_QW, cell_count_and_cells, etc.

print("harvesting zeros (mp.zetazero, 80)...")
mp.mp.dps = 15
GAMMAS = [float(mp.im(mp.zetazero(k))) for k in range(1, 81)]
mp.mp.dps = 30

# ---- D1/D2: lambda = 3 minimizer, zero side to J=80 ----
lam_f, N = 3.0, 18
QWf, L = build_QW(mp.mpf("3.0"), N, True)
Ebas = Ebas_of(N)
Qf_e = Ebas.T @ QWf @ Ebas
K, H, defects, x = cell_count_and_cells(lam_f)
I0 = np.trapezoid(H[0], x)
cols = []
for n in sorted(defects):
    if n == 0 or defects[n] >= 0.05 or n > 36:
        continue
    cc = cell_coeffs(lam_f, L, N, H[n] - (np.trapezoid(H[n], x) / I0) * H[0], x)
    if cc is not None:
        cols.append(Ebas.T @ cc.real)
C = np.column_stack(cols)
Qc, _ = np.linalg.qr(C)
wo, vo = np.linalg.eigh(np.eye(N + 1) - Qc @ Qc.T)
Qo = vo[:, wo > 0.5]
evf, evecf = np.linalg.eigh(Qo.T @ Qf_e @ Qo)
v = Qo @ evecf[:, 0]
qwv = float(evf[0])
terms = [2 * abs(fhat_of(v, Ebas, N, L, g))**2 for g in GAMMAS]
S = np.cumsum(terms)
omega_N = 2 * np.pi * N / L
print(f"\n== D1: QW(min) = {qwv:.4f} (lambda=3); zero-side partial sums ==")
for J in (10, 20, 30, 40, 50, 60, 70, 80):
    print(f"   J={J:2d} (gamma<={GAMMAS[J-1]:6.1f}): S_J = {S[J-1]:.4f}   gap = {qwv - S[J-1]:+.4f}")
# 1/T tail extrapolation from the last stretch: terms ~ c/gamma^2 * density
lo, hi = 60, 80
csum = S[hi - 1] - S[lo - 1]
g_lo, g_hi = GAMMAS[lo - 1], GAMMAS[hi - 1]
c_eff = csum / (1 / g_lo - 1 / g_hi)         # if sum_{>T} ~ c/T
tail_est = c_eff / g_hi
S_inf = S[hi - 1] + tail_est
closing = abs(qwv - S_inf) < abs(qwv - S[39]) * 0.5
print(f"   1/T-extrapolated S_inf = {S_inf:.4f}  (tail beyond gamma_80 ~ {tail_est:.4f})"
      f"   |QW - S_inf| = {abs(qwv - S_inf):.4f} vs |QW - S_40| = {abs(qwv - S[39]):.4f}")
print("   D1: " + ("CRITERION (slow tail of a spread profile) -- identity intact"
                   if closing else "NOT closed by tail -- escalate (possible mathematics)"))

print("\n== D2: anatomy -- per-zero mass of the minimizer (resolved zeros) ==")
res_terms = [(GAMMAS[j], terms[j]) for j in range(len(GAMMAS)) if GAMMAS[j] <= omega_N]
tot_res = sum(t for _, t in res_terms)
print("   " + "  ".join(f"g={g:.1f}:{t:.3f}" for g, t in res_terms))
mx_share = max(t for _, t in res_terms) / max(tot_res, 1e-30)
print(f"   resolved total = {tot_res:.4f}; largest single-zero share of it = {mx_share:.2f}"
      f"  -> {'SPREAD (near-critical partial cancellation)' if mx_share < 0.5 else 'SPIKE'}")

# ---- D3: gap-collapse exponent, sub-resolution rows only ----
print("\n== D3: gap-collapse exponent, sub-resolution fit ==")
Lx = np.log(3.0)
base = [g for g in GAMMAS if g <= 51.5]


def gram_min(gap_scale):
    gs = list(base)
    gs[1] = gs[0] + (base[1] - base[0]) * gap_scale
    n = len(gs)
    G = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            d, s = gs[i] - gs[j], gs[i] + gs[j]
            G[i, j] = np.sinc(Lx * d / np.pi) + np.sinc(Lx * s / np.pi)
    return float(np.min(np.linalg.eigvalsh(G)))


res_lim = np.pi / Lx
scales = [0.125, 0.0625, 0.03125, 0.015625]
gaps = [(base[1] - base[0]) * s for s in scales]
mins = [gram_min(s) for s in scales]
print(f"   window resolution pi/L_x = {res_lim:.3f}; collapse begins below it (plateau above ✓)")
print("   gap: " + "  ".join(f"{g:8.4f}" for g in gaps))
print("   min: " + "  ".join(f"{m:8.5f}" for m in mins))
expo = np.polyfit(np.log(gaps), np.log(np.maximum(mins, 1e-14)), 1)[0]
print(f"   sub-resolution exponent = {expo:.3f}  -> "
      + ("CRITERION (fit window) -- order-2 collapse confirmed" if 1.7 <= expo <= 2.3
         else f"exponent {expo:.2f}: investigate"))
