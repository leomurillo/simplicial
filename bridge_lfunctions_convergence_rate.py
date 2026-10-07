"""
bridge_lfunctions_convergence_rate.py
=====================================

Pass-8 step (3c): Quantify the rate at which the empirical Cesaro mean
converges to its predicted asymptote.

From bridge_lfunctions_cesaro_widescan.py we observed:

  Predicted (central + spectral) : 1.1880
  Cesaro mean over [4, 17]       : 0.9704 (matches CENTRAL piece to 4 dp)
  Cesaro mean over [14, 17]      : 1.0735 (slow drift up toward predicted)

This script reads the persisted T-scan data and fits

  R(T_lo) := < trace(N, T) >_{T in [T_lo, T_max]}  -  C_central

against power-law / log models to identify the convergence rate of the
spectral remainder.  Pass-7's identity predicts R(T_lo) -> C_spectral
asymptotically.

Two interesting tests:

(1) Does R(T_lo) approach C_spectral with rate 1/T_lo, 1/sqrt(T_lo),
    1/log(T_lo), or something else?

(2) Is the empirical asymptote C_central + C_spectral, or just C_central?
    The former says the bridge is L'/L AND spectral; the latter says the
    bridge is ONLY L'/L (and the spectral term is suppressed by some
    additional truncation effect).
"""

import sys
import io
import json
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np

with open(r"C:\Projects\simplicial\bridge_lfunctions_cesaro_widescan.json") as f:
    data = json.load(f)

T_grid = data["T_grid"]
trace_vals = data["trace_vals"]
C_central = data["C_central"]
C_spectral = data["C_spectral"]
predicted = data["predicted_mean"]
T_MAX = data["T_MAX"]

print(f"  C_central(30)  = {C_central:.6f}")
print(f"  C_spectral(30) = {C_spectral:.6f}")
print(f"  predicted      = {predicted:.6f}")
print()

# ---------------------------------------------------------------------
# Cesaro on receding window [T_lo, T_MAX] for fine grid of T_lo
# ---------------------------------------------------------------------
def cesaro(T_lo, T_hi):
    pts = [(T, v) for T, v in zip(T_grid, trace_vals) if T_lo <= T <= T_hi]
    if len(pts) < 2:
        return None
    s = 0.0
    for i in range(len(pts) - 1):
        s += 0.5 * (pts[i][1] + pts[i+1][1]) * (pts[i+1][0] - pts[i][0])
    return s / (pts[-1][0] - pts[0][0])

# Fine sweep of T_lo
T_lo_vals = np.arange(4.0, 15.5, 0.5)
print("=" * 80)
print(" Cesaro mean on receding window [T_lo, T_MAX = 17]")
print("=" * 80)
print()
print(f"  {'T_lo':>6} {'<trace>':>10} {'(/central)':>12} {'(/predicted)':>14}")
print(f"  {'-'*6} {'-'*10} {'-'*12} {'-'*14}")
data_for_fit = []
for T_lo in T_lo_vals:
    avg = cesaro(T_lo, T_MAX)
    if avg is not None:
        print(f"  {T_lo:>6.1f} {avg:>10.4f} {avg/C_central:>12.4f} {avg/predicted:>14.4f}")
        data_for_fit.append((T_lo, avg))

# ---------------------------------------------------------------------
# Also: forward window [T_MAX_minus, T_MAX] (smaller windows at high T)
# ---------------------------------------------------------------------
print()
print("=" * 80)
print(f" Cesaro mean on forward windows [T_lo, T_lo + dT] at T_MAX side")
print("=" * 80)
print()
print(f"  {'T_lo':>6} {'<trace>':>10} {'(/central)':>12} {'window_width':>14}")
print(f"  {'-'*6} {'-'*10} {'-'*12} {'-'*14}")
for T_lo in [4.0, 6.0, 8.0, 10.0, 12.0, 14.0]:
    T_hi = min(T_lo + 2.0, T_MAX)
    avg = cesaro(T_lo, T_hi)
    if avg is not None:
        print(f"  {T_lo:>6.1f} {avg:>10.4f} {avg/C_central:>12.4f} {T_hi - T_lo:>14.2f}")

# ---------------------------------------------------------------------
# Convergence-rate fit: R(T_lo) := <trace>[T_lo, T_max] - C_central
# Try: R = a / T_lo + b, R = a / sqrt(T_lo) + b, R = a / log T_lo + b
# ---------------------------------------------------------------------
print()
print("=" * 80)
print(" Convergence-rate fit:  R(T_lo) = <trace>_{[T_lo, T_max]} - C_central")
print("=" * 80)
print()

T_arr = np.array([t for t, _ in data_for_fit])
R_arr = np.array([v - C_central for _, v in data_for_fit])
print(f"  R(T_lo) range: [{R_arr.min():.4f}, {R_arr.max():.4f}]")
print(f"  Target if Pass-7 identity holds: R -> C_spectral = {C_spectral:.4f}")
print()

# Three models: R = a + b * (1/T_lo), R = a + b * (1/sqrt(T_lo)), R = a + b * (1/log T_lo)
def linreg(X, y):
    """Simple OLS for y = a + b * X."""
    X_mean = X.mean()
    y_mean = y.mean()
    b = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
    a = y_mean - b * X_mean
    y_pred = a + b * X
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y_mean) ** 2)
    R2 = 1 - ss_res / ss_tot
    return a, b, R2

models = {
    "R = a + b * (1 / T_lo)":         1.0 / T_arr,
    "R = a + b * (1 / sqrt(T_lo))":   1.0 / np.sqrt(T_arr),
    "R = a + b * (1 / log T_lo)":     1.0 / np.log(T_arr),
    "R = a + b * (log T_lo / T_lo)":  np.log(T_arr) / T_arr,
}

print(f"  {'model':<40} {'asymptote a':>13} {'slope b':>10} {'R^2':>8}")
print(f"  {'-'*40} {'-'*13} {'-'*10} {'-'*8}")
for label, X in models.items():
    a, b, R2 = linreg(X, R_arr)
    print(f"  {label:<40} {a:>13.4f} {b:>10.4f} {R2:>8.4f}")
print()
print(f"  Target asymptote: a -> C_spectral = {C_spectral:.4f}")
print()

# ---------------------------------------------------------------------
# Also fit <trace>[T_lo, T_max] directly to predicted = C_central + C_spectral
# ---------------------------------------------------------------------
y_arr = R_arr + C_central
print("=" * 80)
print(" Direct asymptote fit: <trace>[T_lo, T_max] = a + b * (1 / sqrt(T_lo))")
print("=" * 80)
print()
a, b, R2 = linreg(1.0 / np.sqrt(T_arr), y_arr)
print(f"  asymptote a = {a:.4f}   slope b = {b:.4f}   R^2 = {R2:.4f}")
print(f"  predicted asymptote (central + spectral) = {predicted:.4f}")
print(f"  fit-vs-predicted ratio = {a/predicted:.4f}")
print()

a, b, R2 = linreg(1.0 / T_arr, y_arr)
print(f"  model: a + b / T_lo")
print(f"  asymptote a = {a:.4f}   slope b = {b:.4f}   R^2 = {R2:.4f}")

a, b, R2 = linreg(np.log(T_arr) / T_arr, y_arr)
print(f"  model: a + b * (log T_lo) / T_lo")
print(f"  asymptote a = {a:.4f}   slope b = {b:.4f}   R^2 = {R2:.4f}")
print()

# ---------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------
out = {
    "T_grid": list(T_arr),
    "R_arr": list(R_arr),
    "C_central": C_central,
    "C_spectral": C_spectral,
    "predicted": predicted,
    "fit_models": {
        label: {
            "a": linreg(X, R_arr)[0],
            "b": linreg(X, R_arr)[1],
            "R2": linreg(X, R_arr)[2],
        }
        for label, X in models.items()
    },
}
with open(r"C:\Projects\simplicial\bridge_lfunctions_convergence_rate.json", "w") as f:
    json.dump(out, f, indent=2)
print("  Wrote: bridge_lfunctions_convergence_rate.json")
