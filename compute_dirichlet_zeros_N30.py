"""
Compute first ~10-20 zeros of all primitive Dirichlet L-functions
with conductor dividing 30. Output ell_1^joint(30), ell_2^joint(30), etc.

Primitive characters by conductor (mod 30):
- f=1: 1 (trivial -> zeta)
- f=3: 1 (chi_{-3}, real odd)
- f=5: 3 (1 real quadratic + 2 complex quartic conjugates)
- f=15: 3 (CRT products chi_{-3} x non-trivial chi_5)
Total: 8 = phi(30)
"""

import math
from mpmath import mp, mpc, mpf, zeta, exp, pi, log, sqrt
from mpmath import findroot, fabs as mp_abs
mp.dps = 30

def L_chi(s, chi_vals, q):
    """L(s, chi) = q^{-s} sum_{a=1}^{q-1} chi(a) * zeta(s, a/q).
    chi_vals: dict mapping a (1..q-1) to chi(a)."""
    total = mpc(0)
    for a, val in chi_vals.items():
        if val != 0:
            total += val * zeta(s, mpf(a)/q)
    return total * q**(-s)

def find_zeros_on_critical_line(chi_vals, q, t_min=0.5, t_max=30.0, n_zeros=10, refine_dps=25):
    """Find first n_zeros zeros of L(chi, 1/2+it) for t in [t_min, t_max]."""
    # Step 1: coarse scan for sign changes / local minima of |L|
    candidates = []
    t = t_min
    dt = 0.05  # coarse step
    prev_L = L_chi(mpc(mpf('0.5'), t), chi_vals, q)
    prev_abs_sq = float(prev_L.real**2 + prev_L.imag**2)
    while t < t_max and len(candidates) < n_zeros * 3:
        t_next = t + dt
        L_next = L_chi(mpc(mpf('0.5'), t_next), chi_vals, q)
        next_abs_sq = float(L_next.real**2 + L_next.imag**2)
        # Look for local minima where |L|^2 is small
        if next_abs_sq < 1e-3 or (prev_abs_sq > next_abs_sq and len(candidates) > 0 and
                                   abs(t - candidates[-1]) > 1.0):
            # Maybe a zero is near
            candidates.append(t_next)
        # Sign change in real part (for real characters)
        if prev_L.real * L_next.real < 0:
            candidates.append((t + t_next) / 2)
        prev_L = L_next
        prev_abs_sq = next_abs_sq
        t = t_next

    # Step 2: refine each candidate with finer search
    zeros = []
    for t_cand in candidates:
        if len(zeros) >= n_zeros:
            break
        # Fine search around t_cand
        try:
            mp.dps = refine_dps
            f = lambda t: L_chi(mpc(mpf('0.5'), t), chi_vals, q)
            # Use secant method by bracketing
            best_t = t_cand
            best_abs = float(mp_abs(f(t_cand)))
            for delta in [0.5, 0.1, 0.02]:
                for trial_t in [t_cand - delta, t_cand, t_cand + delta]:
                    if trial_t < 0: continue
                    a = float(mp_abs(f(trial_t)))
                    if a < best_abs:
                        best_abs = a
                        best_t = trial_t
                t_cand = best_t
            # Final refinement via findroot
            if best_abs < 1e-2:
                try:
                    root = findroot(f, mpc(mpf('0.5'), best_t), tol=1e-15)
                    g = root.imag
                    if abs(float(root.real) - 0.5) < 1e-3 and g > 0:
                        if not zeros or abs(g - zeros[-1]) > 0.1:
                            zeros.append(g)
                except Exception:
                    if best_abs < 1e-5:
                        zeros.append(best_t)
        except Exception as e:
            pass

    # Deduplicate and sort
    zeros_clean = []
    for g in sorted([float(g) for g in zeros]):
        if not zeros_clean or g - zeros_clean[-1] > 0.05:
            zeros_clean.append(g)
    return zeros_clean[:n_zeros]

# --------------------------------------------------------------
# Define primitive characters with conductor dividing 30
# --------------------------------------------------------------
i = mpc(0, 1)

# Conductor 1: zeta (handled separately)

# Conductor 3: chi_{-3}, the Legendre mod 3
chi_3 = {1: mpf(1), 2: mpf(-1)}

# Conductor 5:
# (Z/5)^* = <2>, order 4. Generator g=2 with values 2, 4, 3, 1 (order 4)
# Character chi_5^k(2) = i^k for k=1,2,3
# chi_5(2^a) = i^(k*a)
def make_chi_5(k):
    """k = 1, 2, 3 for the three non-trivial characters mod 5."""
    gen_powers = {1: 0, 2: 1, 4: 2, 3: 3}  # 2^0=1, 2^1=2, 2^2=4, 2^3=3 mod 5
    return {a: exp(mpc(0, 2*pi*k*gen_powers[a]/4)) for a in [1, 2, 3, 4]}

chi_5_a = make_chi_5(1)  # order 4 quartic
chi_5_b = make_chi_5(2)  # order 2 quadratic (Legendre mod 5)
chi_5_c = make_chi_5(3)  # order 4 quartic (conjugate of chi_5_a)

# Conductor 15: CRT product chi_3 x non-trivial chi_5
# Units mod 15: {1,2,4,7,8,11,13,14}, |U|=8
# CRT: u mod 15 <-> (u mod 3, u mod 5)
# chi_{15}(u) = chi_3(u mod 3) * chi_5(u mod 5)
# Primitive iff both components non-trivial
def make_chi_15(chi5_func):
    """CRT product of chi_{-3} (mod 3 part) and chi5_func (mod 5 part)."""
    units_15 = [u for u in range(1, 15) if math.gcd(u, 15) == 1]
    return {u: chi_3[u % 3] * chi5_func[u % 5] for u in units_15}

chi_15_a = make_chi_15(chi_5_a)
chi_15_b = make_chi_15(chi_5_b)
chi_15_c = make_chi_15(chi_5_c)

# --------------------------------------------------------------
# Compute first zeros
# --------------------------------------------------------------
print("=== Computing first zeros of all primitive L-functions with conductor | 30 ===\n")

# Already-known data from LMFDB for chi_{-3}:
zeros_chi3 = [
    8.039737155681467, 11.249206207772935, 15.704619176721626,
    18.261997495693128, 20.455770807742493, 24.059414856493451,
    26.577868735774585, 28.218164506233386, 30.745040261382496,
    33.897388927259419,
]

# Zeta zeros (already used)
zeros_zeta = [
    14.134725141734694, 21.022039638771555, 25.010857580145689,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280915000, 48.005150881167160,
    49.773832477672302,
]

def report_zeros(name, zeros):
    print(f"{name}: first 10 zeros (imag parts):")
    for i, g in enumerate(zeros):
        print(f"  gamma_{i+1} = {float(g):.6f}")
    ell_1 = sum(1.0/g**2 for g in zeros)
    print(f"  sum 1/gamma^2 (first 10): {ell_1:.6e}")
    print()
    return ell_1

print("=== Known L-functions (from LMFDB and prior data) ===\n")
ell_zeta = report_zeros("L(s, 1) = zeta(s)", zeros_zeta)
ell_chi3 = report_zeros("L(s, chi_{-3}) [LMFDB]", zeros_chi3)

# --------------------------------------------------------------
# Compute remaining characters via mpmath
# --------------------------------------------------------------
print("=== Computing remaining L-function zeros via mpmath/Hurwitz ===\n")
print("(This takes a couple of minutes for each character.)\n")

# For real chi_5_b (Legendre mod 5): first zeros around 6.6, 9.2, 10.9, 14.0, 15.0, ...
# Computing first 10 by finding sign changes
print("L(s, chi_5 Legendre quadratic) - computing zeros...")
import sys; sys.stdout.flush()

# For mpmath direct computation, define test function and use sign-changes
def find_real_char_zeros(chi_vals, q, max_t=40, n_zeros=10):
    """For a REAL character, find zeros of L on critical line by sign changes."""
    zeros = []
    t = 0.1
    dt = 0.02
    f = lambda t: L_chi(mpc(mpf('0.5'), mpf(t)), chi_vals, q).real
    prev = f(t)
    while t < max_t and len(zeros) < n_zeros:
        t += dt
        curr = f(t)
        if prev * curr < 0:
            # Sign change, refine via bisection
            a, b = t - dt, t
            for _ in range(60):
                mid = (a + b) / 2
                fm = f(mid)
                if fm * prev < 0:
                    b = mid
                else:
                    a = mid
                    prev = fm
            zeros.append((a + b) / 2)
            prev = f(t)
        else:
            prev = curr
    return zeros

# chi_5_b: Legendre mod 5 (real)
mp.dps = 20
zeros_chi5_b = find_real_char_zeros(chi_5_b, 5, max_t=40, n_zeros=10)
ell_chi5_b = report_zeros("L(s, chi_5 Legendre quadratic)", zeros_chi5_b)

# For complex characters, need |L|^2 minima, more delicate
def find_complex_char_zeros(chi_vals, q, max_t=40, n_zeros=10):
    """For a COMPLEX character, find zeros of L on critical line by |L|^2 minimization."""
    zeros = []
    t = 0.5
    dt = 0.05
    f_abs = lambda t: float(abs(L_chi(mpc(mpf('0.5'), mpf(t)), chi_vals, q)))
    f = lambda t: L_chi(mpc(mpf('0.5'), mpf(t)), chi_vals, q)
    # Scan for local minima
    a_prev = f_abs(t)
    a_curr = f_abs(t + dt)
    while t < max_t - dt and len(zeros) < n_zeros:
        a_next = f_abs(t + 2*dt)
        if a_curr < a_prev and a_curr < a_next and a_curr < 0.1:
            # Local min, likely a zero
            t_min = t + dt
            # Refine
            for shrink in [0.025, 0.01, 0.005, 0.001]:
                best_t = t_min
                best = f_abs(best_t)
                for ddt in [-shrink, 0, shrink]:
                    a2 = f_abs(t_min + ddt)
                    if a2 < best:
                        best = a2
                        best_t = t_min + ddt
                t_min = best_t
            if f_abs(t_min) < 1e-6:
                if not zeros or t_min - zeros[-1] > 0.5:
                    zeros.append(t_min)
        t += dt
        a_prev = a_curr
        a_curr = a_next
    return zeros

print("L(s, chi_5 quartic_a) - computing zeros...")
sys.stdout.flush()
zeros_chi5_a = find_complex_char_zeros(chi_5_a, 5, max_t=40, n_zeros=10)
ell_chi5_a = report_zeros("L(s, chi_5 quartic_a) [complex]", zeros_chi5_a)

print("L(s, chi_5 quartic_c) - computing zeros...")
sys.stdout.flush()
zeros_chi5_c = find_complex_char_zeros(chi_5_c, 5, max_t=40, n_zeros=10)
ell_chi5_c = report_zeros("L(s, chi_5 quartic_c) [complex, conjugate]", zeros_chi5_c)

# Conductor 15 characters
print("L(s, chi_15_a) - computing zeros...")
sys.stdout.flush()
# chi_15 with chi_5_a part is complex (since chi_5_a is complex)
zeros_chi15_a = find_complex_char_zeros(chi_15_a, 15, max_t=30, n_zeros=8)
ell_chi15_a = report_zeros("L(s, chi_15_a) [complex]", zeros_chi15_a)

print("L(s, chi_15_b) - computing zeros...")
sys.stdout.flush()
# chi_15 with chi_5_b is real (chi_3 * chi_5_b both real)
zeros_chi15_b = find_real_char_zeros(chi_15_b, 15, max_t=30, n_zeros=8)
ell_chi15_b = report_zeros("L(s, chi_15_b) [real]", zeros_chi15_b)

print("L(s, chi_15_c) - computing zeros...")
sys.stdout.flush()
zeros_chi15_c = find_complex_char_zeros(chi_15_c, 15, max_t=30, n_zeros=8)
ell_chi15_c = report_zeros("L(s, chi_15_c) [complex, conjugate]", zeros_chi15_c)

# --------------------------------------------------------------
# Total ell_1^joint(30)
# --------------------------------------------------------------
ell_1_joint_30 = (ell_zeta + ell_chi3 + ell_chi5_a + ell_chi5_b + ell_chi5_c
                  + ell_chi15_a + ell_chi15_b + ell_chi15_c)
print(f"=== TOTAL ===")
print(f"ell_1^joint(30) [first 10 zeros each]:")
print(f"  zeta:        {ell_zeta:.6e}")
print(f"  chi_{{-3}}:    {ell_chi3:.6e}")
print(f"  chi_5_a:     {ell_chi5_a:.6e}")
print(f"  chi_5_b:     {ell_chi5_b:.6e}")
print(f"  chi_5_c:     {ell_chi5_c:.6e}")
print(f"  chi_15_a:    {ell_chi15_a:.6e}")
print(f"  chi_15_b:    {ell_chi15_b:.6e}")
print(f"  chi_15_c:    {ell_chi15_c:.6e}")
print(f"  TOTAL:       {ell_1_joint_30:.6e}")

print(f"\n=== Comparison to observed N=30 trace ===")
trace_obs = 1.5191
print(f"Observed trace at N=30, T=7: {trace_obs:.4f}")
print(f"ell_1^joint(30) [first 10 each]: {ell_1_joint_30:.4f}")
print(f"Ratio (trace/joint): {trace_obs/ell_1_joint_30:.4f}")
print()
print("Note: ell_1^joint should be computed over ALL zeros, not just first 10.")
print("Each truncated sum underestimates true ell_1 (tail contributions).")
print("Including tail, true ell_1^joint will be larger than computed above.")
