"""
Improved Dirichlet L-function zero finder using direct findroot on
complex-valued L(chi, 1/2 + it). Works for both real and complex characters.
"""

import math
from mpmath import mp, mpc, mpf, zeta, exp, pi, log, sqrt
from mpmath import findroot, fabs as mp_abs
mp.dps = 25

def L_chi(s, chi_vals, q):
    """L(s, chi) = q^{-s} sum chi(a) zeta(s, a/q)"""
    total = mpc(0)
    for a, val in chi_vals.items():
        if val != 0:
            total += val * zeta(s, mpf(a)/q)
    return total * q**(-s)

def find_zeros_universal(chi_vals, q, t_max=50, n_zeros=15, fine_dt=0.05):
    """Find zeros of L(chi, 1/2+it) for t in [0, t_max] via |L|^2 minimization."""
    # Scan fine grid for local minima of |L|^2
    t_grid = []
    val_grid = []
    t = mpf('0.5')
    while t < t_max:
        s = mpc(mpf('0.5'), t)
        val = abs(L_chi(s, chi_vals, q))
        t_grid.append(float(t))
        val_grid.append(float(val))
        t += fine_dt

    # Find local minima below threshold
    candidates = []
    for i in range(1, len(t_grid) - 1):
        if val_grid[i] < val_grid[i-1] and val_grid[i] < val_grid[i+1]:
            if val_grid[i] < 0.1:  # only "small" minima
                candidates.append((t_grid[i], val_grid[i]))

    # Refine each candidate
    zeros = []
    for t_cand, _ in candidates:
        if len(zeros) >= n_zeros:
            break
        # Local bisection/refinement
        try:
            # Use findroot with start point
            root = findroot(
                lambda t: L_chi(mpc(mpf('0.5'), t), chi_vals, q),
                mpf(t_cand),
                tol=1e-12,
                maxsteps=50,
            )
            if isinstance(root, mpc):
                g = float(root.imag)
                # Check real part is ~1/2
                if abs(float(root.real) - 0.5) < 1e-3 and g > 0:
                    if not zeros or g - zeros[-1] > 0.1:
                        zeros.append(g)
            else:
                # Returned real value (could be ImagPart of zero)
                g = float(root)
                if g > 0 and (not zeros or g - zeros[-1] > 0.1):
                    zeros.append(g)
        except Exception:
            pass

    zeros.sort()
    return zeros[:n_zeros]

# --------------------------------------------------------------
# Characters definition
# --------------------------------------------------------------
i = mpc(0, 1)

# Conductor 3: chi_{-3}
chi_3 = {1: mpf(1), 2: mpf(-1)}

# Conductor 5: three primitive characters
def make_chi_5(k):
    gen_powers = {1: 0, 2: 1, 4: 2, 3: 3}
    return {a: exp(mpc(0, 2*pi*k*gen_powers[a]/4)) for a in [1, 2, 3, 4]}

chi_5_quartic_1 = make_chi_5(1)  # complex order 4
chi_5_quadratic = make_chi_5(2)   # real order 2 (Legendre)
chi_5_quartic_2 = make_chi_5(3)  # complex order 4 (conjugate)

# Conductor 15
def make_chi_15(chi5_func):
    units_15 = [u for u in range(1, 15) if math.gcd(u, 15) == 1]
    return {u: chi_3[u % 3] * chi5_func[u % 5] for u in units_15}

chi_15_qq = make_chi_15(chi_5_quadratic)   # real
chi_15_q1 = make_chi_15(chi_5_quartic_1)    # complex
chi_15_q2 = make_chi_15(chi_5_quartic_2)    # complex

# --------------------------------------------------------------
# Compute zeros
# --------------------------------------------------------------
print("=== Improved Dirichlet L-function zero finder ===\n")

# Pre-loaded data
known_zeros = {
    "zeta": [
        14.134725141734694, 21.022039638771555, 25.010857580145689,
        30.424876125859513, 32.935061587739190, 37.586178158825671,
        40.918719012147495, 43.327073280915000, 48.005150881167160,
        49.773832477672302, 52.970321477714461, 56.446247697063395,
        59.347044002602353, 60.831778524609810, 65.112544048081607,
    ],
    "chi_{-3}": [
        8.039737155681467, 11.249206207772935, 15.704619176721626,
        18.261997495693128, 20.455770807742493, 24.059414856493451,
        26.577868735774585, 28.218164506233386, 30.745040261382496,
        33.897388927259419, 35.608412653938635, 37.551796556364627,
        39.485207260929351, 42.616379226157568, 44.120572912072202,
    ],
}

# Compute new ones
print("Computing chi_5 quadratic (Legendre mod 5)...")
import sys; sys.stdout.flush()
zeros_chi5_qq = find_zeros_universal(chi_5_quadratic, 5, t_max=40, n_zeros=10)
print(f"  Found {len(zeros_chi5_qq)} zeros: {[f'{z:.3f}' for z in zeros_chi5_qq]}")

print("Computing chi_5 quartic_1...")
sys.stdout.flush()
zeros_chi5_q1 = find_zeros_universal(chi_5_quartic_1, 5, t_max=40, n_zeros=10)
print(f"  Found {len(zeros_chi5_q1)} zeros: {[f'{z:.3f}' for z in zeros_chi5_q1]}")

print("Computing chi_5 quartic_2 (conjugate of chi_5 quartic_1)...")
sys.stdout.flush()
zeros_chi5_q2 = find_zeros_universal(chi_5_quartic_2, 5, t_max=40, n_zeros=10)
print(f"  Found {len(zeros_chi5_q2)} zeros: {[f'{z:.3f}' for z in zeros_chi5_q2]}")

print("Computing chi_15 with chi_5_quadratic (real)...")
sys.stdout.flush()
zeros_chi15_qq = find_zeros_universal(chi_15_qq, 15, t_max=30, n_zeros=10)
print(f"  Found {len(zeros_chi15_qq)} zeros: {[f'{z:.3f}' for z in zeros_chi15_qq]}")

print("Computing chi_15 with chi_5_quartic_1...")
sys.stdout.flush()
zeros_chi15_q1 = find_zeros_universal(chi_15_q1, 15, t_max=30, n_zeros=10)
print(f"  Found {len(zeros_chi15_q1)} zeros: {[f'{z:.3f}' for z in zeros_chi15_q1]}")

print("Computing chi_15 with chi_5_quartic_2...")
sys.stdout.flush()
zeros_chi15_q2 = find_zeros_universal(chi_15_q2, 15, t_max=30, n_zeros=10)
print(f"  Found {len(zeros_chi15_q2)} zeros: {[f'{z:.3f}' for z in zeros_chi15_q2]}")

# --------------------------------------------------------------
# Summary and joint cumulant
# --------------------------------------------------------------
def ell1(zeros):
    return sum(1.0/z**2 for z in zeros)

all_data = [
    ("zeta", known_zeros["zeta"]),
    ("chi_{-3} [LMFDB]", known_zeros["chi_{-3}"]),
    ("chi_5 quad (Legendre)", zeros_chi5_qq),
    ("chi_5 quartic_1", zeros_chi5_q1),
    ("chi_5 quartic_2 (conj)", zeros_chi5_q2),
    ("chi_15 (chi_3 x chi_5_quad)", zeros_chi15_qq),
    ("chi_15 (chi_3 x chi_5_quart_1)", zeros_chi15_q1),
    ("chi_15 (chi_3 x chi_5_quart_2)", zeros_chi15_q2),
]

print(f"\n=== Per-L-function ell_1 (truncated to first ~10 zeros) ===")
print(f"  {'L-function':<35} {'n_zeros':>8} {'first':>10} {'ell_1':>14}")
total_ell_1 = 0.0
for name, zeros in all_data:
    if zeros:
        e = ell1(zeros)
        total_ell_1 += e
        print(f"  {name:<35} {len(zeros):>8} {zeros[0]:>10.3f} {e:>14.6e}")
    else:
        print(f"  {name:<35} {0:>8} {'N/A':>10} {'N/A':>14}")

print(f"\nell_1^joint(30) [first ~10 zeros each]: {total_ell_1:.6e}")
print(f"\n=== Comparison ===")
trace = 1.5191
print(f"Observed trace at N=30, T=7: {trace:.4f}")
print(f"ell_1^joint estimated:       {total_ell_1:.4f}")
print(f"Ratio trace/joint:           {trace/total_ell_1:.4f}")
print()
print("Truncation: each L-function's ell_1 from first 10 zeros UNDERESTIMATES.")
print("True ell_1 includes tail contributions, possibly 1.5x-2x larger.")
print(f"Rough corrected joint (x1.5): {total_ell_1 * 1.5:.4f}, ratio: {trace/(total_ell_1*1.5):.4f}")
print(f"Rough corrected joint (x2.0): {total_ell_1 * 2.0:.4f}, ratio: {trace/(total_ell_1*2.0):.4f}")
