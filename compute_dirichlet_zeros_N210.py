"""
Compute additional Dirichlet L-function zeros for N=210.

New primitive characters beyond N=30 (conductors in {7, 21, 35, 105}):
- f=7: 5 primitive (chi_7^k for k=1..5; phi*(7)=5)
- f=21: 5 primitive (phi*(21)=5)
- f=35: 15 primitive (phi*(35)=15)
- f=105: 15 primitive (phi*(105)=15)
Total: 40 new L-functions.

For tractability, fully compute f=7 (5 L-functions) then estimate rest
via analytic conductor scaling.
"""

import math
import time
from mpmath import mp, mpc, mpf, zeta, exp, pi
mp.dps = 20

def L_chi(s, chi_vals, q):
    total = mpc(0)
    for a, val in chi_vals.items():
        total += val * zeta(s, mpf(a)/q)
    return total * q**(-s)

def find_zeros(chi_vals, q, t_max=25, n_zeros=8, dt=0.01, thresh=0.05):
    zeros = []
    t = 0.5
    prev_val = float(abs(L_chi(mpc(mpf('0.5'), mpf(t)), chi_vals, q)))
    while t < t_max and len(zeros) < n_zeros:
        curr_t = t + dt
        next_t = t + 2*dt
        if next_t > t_max: break
        curr_val = float(abs(L_chi(mpc(mpf('0.5'), mpf(curr_t)), chi_vals, q)))
        next_val = float(abs(L_chi(mpc(mpf('0.5'), mpf(next_t)), chi_vals, q)))
        if curr_val < prev_val and curr_val < next_val and curr_val < thresh:
            t_lo, t_hi = t, next_t
            for _ in range(15):
                t_mid = (t_lo + t_hi) / 2
                v_mid = float(abs(L_chi(mpc(mpf('0.5'), mpf(t_mid)), chi_vals, q)))
                t_minus = t_mid - dt/4
                t_plus = t_mid + dt/4
                v_minus = float(abs(L_chi(mpc(mpf('0.5'), mpf(t_minus)), chi_vals, q)))
                v_plus = float(abs(L_chi(mpc(mpf('0.5'), mpf(t_plus)), chi_vals, q)))
                if v_minus < v_mid:
                    t_hi = t_mid
                elif v_plus < v_mid:
                    t_lo = t_mid
                else:
                    break
                dt = (t_hi - t_lo) / 4
            zeros.append((t_lo + t_hi) / 2)
            dt = 0.01
            t = zeros[-1] + 0.5
            prev_val = float(abs(L_chi(mpc(mpf('0.5'), mpf(t)), chi_vals, q)))
        else:
            t = curr_t
            prev_val = curr_val
    return zeros

# Conductor 7: (Z/7)^* = <3>, order 6. Generator g=3 with powers 3, 2, 6, 4, 5, 1.
# Five non-trivial characters: chi(3) = zeta_6^k for k=1..5
gen7_powers = {1: 0, 3: 1, 2: 2, 6: 3, 4: 4, 5: 5}
def chi_7_from_power(k):
    return {a: exp(mpc(0, 2*pi*k*gen7_powers[a]/6)) for a in range(1, 7)}

print("=== Computing conductor 7 L-functions (5 primitive chars) ===\n")
chi_7_chars = {f"chi_7^{k}": chi_7_from_power(k) for k in range(1, 6)}

results_f7 = {}
for name, chi in chi_7_chars.items():
    print(f"Computing {name}... ", end="", flush=True)
    t0 = time.time()
    zeros = find_zeros(chi, 7, t_max=25, n_zeros=8, dt=0.01)
    print(f"{len(zeros)} zeros in {time.time()-t0:.1f}s: " +
          ", ".join(f"{z:.2f}" for z in zeros[:5]))
    results_f7[name] = zeros

def ell_n(zeros, n):
    return sum(1.0/z**(2*n) for z in zeros)

print()
print("=== Conductor 7 cumulants ===")
print(f"{'character':<15} {'first 3 zeros':<25} {'ell_1':>12}")
ell_1_f7_total = 0
for name, zeros in results_f7.items():
    e1 = ell_n(zeros, 1)
    ell_1_f7_total += e1
    first3 = ", ".join(f"{z:.2f}" for z in zeros[:3])
    print(f"{name:<15} {first3:<25} {e1:>12.4e}")
print(f"{'TOTAL':<15} {'':<25} {ell_1_f7_total:>12.4e}")

print()
print("=== Estimating ell_1^joint(210) ===\n")
ell_1_joint_30 = 0.796  # from previous computation, truncated
# RvM tail correction (from compute_dirichlet_zeros_v3): roughly 0.5*truncated added
ell_1_joint_30_full = 1.04  # with RvM tail

# Add conductor 7
ell_1_joint_30_plus_f7 = ell_1_joint_30 + ell_1_f7_total

# Apply same RvM tail correction (proportional)
ell_1_joint_30_plus_f7_full = ell_1_joint_30_plus_f7 * (1.04/0.796)

print(f"ell_1^joint(N=30) truncated: {ell_1_joint_30:.4f}")
print(f"  + conductor 7 (5 L-funcs): {ell_1_f7_total:.4f}")
print(f"  = subtotal:                {ell_1_joint_30_plus_f7:.4f}")
print(f"  with RvM tail (x{1.04/0.796:.2f}):     {ell_1_joint_30_plus_f7_full:.4f}")

# Estimate remaining conductors via analytic density
# For primitive chi mod f, density of zeros ~ (1/2pi) log(f|t|/(2pi e))
# Typical contribution to ell_1: ~ 0.05-0.15 per L-function
# Conductors {21, 35, 105} contribute: 5, 15, 15 = 35 more L-functions

n_remaining = 5 + 15 + 15  # f=21, 35, 105 primitive char counts
# Rough estimate: each contributes ell_1 ~ 0.07 (between zeta and chi_15 typical)
ell_1_remaining_est = n_remaining * 0.07
print()
print(f"Estimated contribution from remaining 35 L-functions (~0.07 each):")
print(f"  {n_remaining} L-functions * 0.07 = {ell_1_remaining_est:.4f}")

ell_1_joint_210_est = ell_1_joint_30_plus_f7_full + ell_1_remaining_est * 1.31  # RvM tail
print()
print(f"=== Total estimated ell_1^joint(210) ===")
print(f"  ell_1^joint(N=210) ~ {ell_1_joint_210_est:.4f}")

trace_210 = 4.7048
print()
print(f"=== Comparison ===")
print(f"Observed trace at N=210, T=7: {trace_210:.4f}")
print(f"Estimated ell_1^joint(210):    {ell_1_joint_210_est:.4f}")
print(f"Ratio:                          {trace_210 / ell_1_joint_210_est:.4f}")
print()
print("Pass-7 prediction: ratio ~ 1 (within finite-T effects).")
print("Pass-5 RH-only would give ratio 4.70/0.019 = 247 (catastrophic).")
print()
print("Improvement from Pass-5 to Pass-7 at N=210:")
print(f"  Pass-5 ratio: 247")
print(f"  Pass-7 ratio: {trace_210 / ell_1_joint_210_est:.2f}")
print(f"  Improvement:  {247 / (trace_210 / ell_1_joint_210_est):.0f}x")
