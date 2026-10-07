"""
Robust Dirichlet L-function zero finder via fine-grid |L|^2 minimization,
followed by refinement.

Computes ell_n^joint(30) for n = 1..10 from first ~10 zeros of each L-function.
"""

import math
import sys
import time
from mpmath import mp, mpc, mpf, zeta, exp, pi
mp.dps = 20

def L_chi(s, chi_vals, q):
    total = mpc(0)
    for a, val in chi_vals.items():
        total += val * zeta(s, mpf(a)/q)
    return total * q**(-s)

def find_zeros(chi_vals, q, t_max=30, n_zeros=10, dt=0.01, thresh=0.05):
    """Find zeros via fine-grid local minima of |L|."""
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
            # Refine: 3 levels of bisection in [t, next_t]
            t_lo, t_hi = t, next_t
            for _ in range(20):
                t_mid = (t_lo + t_hi) / 2
                v_mid = float(abs(L_chi(mpc(mpf('0.5'), mpf(t_mid)), chi_vals, q)))
                # Local search around mid
                t_minus = t_mid - dt/2
                t_plus = t_mid + dt/2
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
            dt = 0.01  # reset for next zero
            t = zeros[-1] + 0.5  # skip ahead
            prev_val = float(abs(L_chi(mpc(mpf('0.5'), mpf(t)), chi_vals, q)))
        else:
            t = curr_t
            prev_val = curr_val
    return zeros

# Characters
chi_3 = {1: mpf(1), 2: mpf(-1)}

# Conductor 5 characters: parameterize by chi(2) value (generator)
# 2 generates (Z/5)^*; powers 2^0=1, 2^1=2, 2^2=4, 2^3=3
def chi_5_from_chi2(c):
    """chi_5 with chi(2) = c; chi(a) = c^k where 2^k = a mod 5."""
    powers = {1: 0, 2: 1, 4: 2, 3: 3}
    return {a: c**powers[a] for a in [1, 2, 3, 4]}

chi_5_quartic_a = chi_5_from_chi2(mpc(0, 1))   # chi(2)=i, order 4
chi_5_quadratic = chi_5_from_chi2(mpf(-1))     # chi(2)=-1, order 2 (Legendre)
chi_5_quartic_b = chi_5_from_chi2(mpc(0, -1))  # chi(2)=-i, order 4 (conj)

# Conductor 15
def make_chi_15(chi5):
    return {u: chi_3[u % 3] * chi5[u % 5] for u in range(1, 15) if math.gcd(u, 15) == 1}

chi_15_q1 = make_chi_15(chi_5_quartic_a)
chi_15_qq = make_chi_15(chi_5_quadratic)
chi_15_q2 = make_chi_15(chi_5_quartic_b)

# Known data
zeros_zeta = [
    14.134725141734694, 21.022039638771555, 25.010857580145689,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280915000, 48.005150881167160,
    49.773832477672302,
]
zeros_chi3 = [
    8.039737155681467, 11.249206207772935, 15.704619176721626,
    18.261997495693128, 20.455770807742493, 24.059414856493451,
    26.577868735774585, 28.218164506233386, 30.745040261382496,
    33.897388927259419,
]

print("=== Robust Dirichlet L-function zero finder ===\n")

results = {
    "zeta": (zeros_zeta, "known"),
    "chi_{-3} (cond 3)": (zeros_chi3, "LMFDB"),
}

# Compute remaining
for name, chi, q in [
    ("chi_5 quadratic (Legendre)", chi_5_quadratic, 5),
    ("chi_5 quartic_a", chi_5_quartic_a, 5),
    ("chi_5 quartic_b (conj)", chi_5_quartic_b, 5),
    ("chi_15 (chi_3 x chi_5_quad)", chi_15_qq, 15),
    ("chi_15 (chi_3 x chi_5_quart_a)", chi_15_q1, 15),
    ("chi_15 (chi_3 x chi_5_quart_b)", chi_15_q2, 15),
]:
    print(f"Computing {name}... ", end="", flush=True)
    t0 = time.time()
    zeros = find_zeros(chi, q, t_max=30, n_zeros=10, dt=0.01)
    print(f"{len(zeros)} zeros in {time.time()-t0:.1f}s")
    results[name] = (zeros, "computed")

print()
print(f"=== Per-L-function first zeros and ell_1 ===\n")
print(f"  {'L-function':<35} {'n':>3} {'first zeros':<50} {'ell_1 (truncated)':>16}")
print("  " + "-" * 110)
total_ell_1 = 0.0
for name, (zeros, src) in results.items():
    if zeros:
        e1 = sum(1.0/z**2 for z in zeros)
        total_ell_1 += e1
        first5 = ", ".join(f"{z:.2f}" for z in zeros[:5])
        print(f"  {name:<35} {len(zeros):>3} {first5:<50} {e1:>16.6e}")
    else:
        print(f"  {name:<35} 0   (no zeros found)")

print()
print(f"=== Joint cumulant ell_1^joint(30) ===")
print(f"  Truncated sum (first ~10 each): {total_ell_1:.6e}")
print()
print(f"=== Comparison ===")
trace = 1.5191
print(f"  Observed trace at N=30, T=7: {trace:.4f}")
print(f"  Estimated ell_1^joint(30):   {total_ell_1:.4f}")
print(f"  Ratio (trace/joint):         {trace/total_ell_1:.4f}")
print()
print(f"  With tail correction factor 1.5: ell_1^joint ~ {total_ell_1 * 1.5:.4f},  ratio: {trace/(total_ell_1*1.5):.3f}")
print(f"  With tail correction factor 2.0: ell_1^joint ~ {total_ell_1 * 2.0:.4f},  ratio: {trace/(total_ell_1*2.0):.3f}")

# Higher cumulants (better convergence since dominated by smallest zeros)
print()
print(f"=== Higher cumulants (better convergence) ===")
for n in [1, 2, 3, 5, 10]:
    total = 0.0
    for name, (zeros, _) in results.items():
        if zeros:
            total += sum(1.0/z**(2*n) for z in zeros)
    print(f"  ell_{n}^joint(30) [truncated] = {total:.6e}")
