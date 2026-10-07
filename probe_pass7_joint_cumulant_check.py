"""
Pass-7 sanity check: does the observed multiplicative apex trace at
(N=30, T=7) correspond to the JOINT cumulant ell_1^joint(30) over all
Dirichlet L-functions with conductor dividing 30?

Uses LMFDB-style approximate first zeros for primitive Dirichlet
characters with conductor in {1, 3, 5, 15}, plus the standard
zeta zeros.

NOTE: For a definitive check, replace estimated zeros with actual LMFDB
data. This script does order-of-magnitude consistency only.
"""

from mpmath import mp, mpf
mp.dps = 20

# Riemann zeros (first 30, from earlier scripts)
gammas_zeta = [
    14.134725141734693790, 21.022039638771554993,
    25.010857580145688763, 30.424876125859513210,
    32.935061587739189691, 37.586178158825671257,
    40.918719012147495187, 43.327073280914999519,
    48.005150881167159728, 49.773832477672302182,
    52.970321477714460644, 56.446247697063394804,
    59.347044002602353079, 60.831778524609809844,
    65.112544048081606660, 67.079810529494173714,
    69.546401711173979253, 72.067157674481907583,
    75.704690699083933168, 77.144840068874805373,
    79.337375020249367922, 82.910380854086030183,
    84.735492980517050106, 87.425274613125229407,
    88.809111207634465423, 92.491899270558484296,
    94.651344040519886967, 95.870634228245309831,
    98.831194218193198281, 101.317851005731391228,
]

# Approximate first zeros for primitive Dirichlet L-functions of conductor f
# (from LMFDB; these are the lowest imaginary parts of zeros on the critical line)
# Conductors dividing 30: 1, 2, 3, 5, 6, 10, 15, 30
# Primitive characters at each conductor:
# f=1: trivial (zeta)
# f=2: only trivial (lifts from f=1)
# f=3: 1 primitive (Legendre chi_{-3}, odd)
# f=4: doesn't divide 30
# f=5: 3 primitive (chi_5 quartic + conjugate, chi_5 quadratic)
# f=6: 1 primitive (chi_{-3} extension to mod 6 with even/odd flip)
# f=10: 2 primitive (lift from f=5 with mod-2 flip)
# f=15: 3 primitive (CRT product chi_3 x chi_5_nontriv)
# f=30: more primitive

# Known first zeros (approximations from LMFDB or analytic estimates):
first_zeros_by_conductor = {
    1: [14.135],     # zeta
    3: [8.040],      # L(chi_{-3}, s), real
    5: [6.183, 6.183, 6.647],  # 2 complex (conjugate pair) + 1 real quartic
    # Higher conductors: approximate first zeros
    6: [9.5],        # estimated; L(chi_6) primitive
    10: [8.5, 8.5],  # estimated
    15: [7.2, 7.2, 8.0],  # estimated
    30: [6.5, 6.5, 7.0, 7.0, 7.5, 7.5, 8.2, 8.2],  # rough estimates for 8 characters?
}

# Actually let me be more careful. Number of primitive characters per conductor f:
# count(f) = number of f-primitive Dirichlet characters
# Standard counting: count(1) = 1, count(2) = 0, count(3) = 1, count(5) = 3,
# count(6) = 1, count(10) = 2, count(15) = 3
# Total primitive characters with conductor | 30: 1 + 1 + 3 + 1 + 2 + 3 = 11
# But (Z/30)^* has only 8 characters. So conductor 30 itself contributes 0 primitive?
# Let me recount.

# Actually for cyclic-group dual:
# Total chars mod 30 = phi(30) = 8
# These distribute among primitive characters of conductors dividing 30:
# count(f) for each f|30 (where primitive Dirichlet chars exist):
# f=1: 1 (trivial)
# f=2: 0 (only trivial, lifted from f=1)
# f=3: phi*(3) = 2-1 = 1
# f=5: phi*(5) = 4-1 = 3
# f=6: number of primitive chars mod 6 not lifted: complicated; phi*(6) = 1
# f=10: phi*(10) = 2
# f=15: phi*(15) = ?
# f=30: phi*(30) = ?
# Sum of phi*(d) for d|n = phi(n) by Mobius

# phi*(1)=1, phi*(2)=0, phi*(3)=1, phi*(5)=3, phi*(6)=1, phi*(10)=2, phi*(15)=3, phi*(30)=?
# 1+0+1+3+1+2+3 = 11; phi(30)=8, so phi*(30) must be 8-11 = -3? Wrong.
# Let me reconsider.

# Actually the Mobius formula: phi*(n) = sum_{d|n} mu(n/d) phi(d)
# phi*(1) = phi(1) = 1
# phi*(2) = phi(2) - phi(1) = 1 - 1 = 0
# phi*(3) = phi(3) - phi(1) = 2 - 1 = 1
# phi*(5) = phi(5) - phi(1) = 4 - 1 = 3
# phi*(6) = phi(6) - phi(2) - phi(3) + phi(1) = 2 - 1 - 2 + 1 = 0  (not 1!)
# phi*(10) = phi(10) - phi(2) - phi(5) + phi(1) = 4 - 1 - 4 + 1 = 0
# phi*(15) = phi(15) - phi(3) - phi(5) + phi(1) = 8 - 2 - 4 + 1 = 3
# phi*(30) = phi(30) - phi(2) - phi(6) - phi(10) - phi(15) + phi(1) + phi(3) + phi(5) - phi(30)
#  Wait, this is getting tangled. Let me just use the formula for squarefree n:
# For n = 30 = 2*3*5 (squarefree), phi*(n) = phi(n) * prod_{p|n} (p-2)/(p-1)
#  Actually no. Let me just compute properly.

# OK using sum_{d|30} phi*(d) = phi(30) = 8:
# d=1: phi*(1) = 1
# d=2: phi*(2) = 0
# d=3: phi*(3) = 1
# d=5: phi*(5) = 3
# d=6: phi*(6) = phi(6) - phi*(1) - phi*(2) - phi*(3) = 2 - 1 - 0 - 1 = 0
# d=10: phi*(10) = phi(10) - phi*(1) - phi*(2) - phi*(5) = 4 - 1 - 0 - 3 = 0
# d=15: phi*(15) = phi(15) - phi*(1) - phi*(3) - phi*(5) = 8 - 1 - 1 - 3 = 3
# d=30: phi*(30) = phi(30) - phi*(1) - phi*(2) - phi*(3) - phi*(5) - phi*(6) - phi*(10) - phi*(15)
#  = 8 - 1 - 0 - 1 - 3 - 0 - 0 - 3 = 0

# So primitive characters distribute as: f=1: 1, f=3: 1, f=5: 3, f=15: 3.
# Total = 1 + 1 + 3 + 3 = 8 = phi(30). ✓

# Hence the L-functions contributing to Xi_30 are:
# - zeta (f=1, trivial character) — contributes the zeta zeros
# - L(chi_{-3}, s) (f=3, quadratic) — 1 L-function
# - L(chi_5, s) variants (f=5) — 3 L-functions
# - L(chi_15, s) variants (f=15) — 3 L-functions

# Total: 8 L-functions in the joint product Xi_30.
# Among non-trivial (7): 1 from mod 3, 3 from mod 5, 3 from mod 15

print("=== Pass-7 consistency check: ell_1^joint(30) ===\n")
print("Primitive characters with conductor dividing 30:")
print("  f=1: 1 (zeta)")
print("  f=3: 1 (Legendre chi_{-3}, real odd)")
print("  f=5: 3 (1 real chi_{5,quad} + 1 complex chi_{5,quart} + conjugate)")
print("  f=15: 3 (CRT products chi_{-3} x chi_5_nontriv)")
print("  Total: 8 = phi(30)\n")

# Compute ell_1 for each component
def sum_inverse_sq(gammas):
    return sum(mpf(1) / g ** 2 for g in gammas)

# zeta contribution
ell_zeta = sum(mpf(1) / mpf(repr(g)) ** 2 for g in gammas_zeta)
print(f"Zeta ell_1 (from 30 zeros): {float(ell_zeta):.6e}")

# Approximate Dirichlet L-function contributions
# Using approximate first zeros and assuming sum_k 1/gamma_k^2 is dominated by first few zeros
# For a Dirichlet L-function with first zero gamma_1, sum_k 1/gamma_k^2 ~ 1/gamma_1^2 * (1 + epsilon)
# where epsilon depends on zero density. For low-conductor L-functions, sum is roughly 2*gamma_1^{-2}.

dirichlet_first_zeros = {
    "L(chi_{-3})": 8.04,      # f=3, real
    "L(chi_5_quartic_1)": 6.18,    # f=5, complex
    "L(chi_5_quartic_2)": 6.18,    # f=5, complex conjugate
    "L(chi_5_quadratic)": 6.64,    # f=5, real
    "L(chi_15_a)": 7.2,            # f=15, estimate
    "L(chi_15_b)": 7.5,            # f=15, estimate
    "L(chi_15_c)": 7.8,            # f=15, estimate
}

# Each L-function contributes approximately 2 * (gamma_1)^{-2} for the first cumulant
# (using factor ~2 to account for higher zeros; true factor depends on zero density)
ell_dirichlet_estimates = {}
for name, g1 in dirichlet_first_zeros.items():
    est = 2.0 * (1.0 / g1 ** 2)  # rough: 1st zero plus tail factor
    ell_dirichlet_estimates[name] = est
    print(f"  {name}: gamma_1 ~ {g1}, est ell_1 ~ {est:.4f}")

print()
ell_joint_estimate = float(ell_zeta) + sum(ell_dirichlet_estimates.values())
print(f"Estimated ell_1^joint(30) (zeta + 7 L-functions): {ell_joint_estimate:.4f}")

# Compare to observed trace at N=30, T=7
trace_observed = 1.5191
print(f"\nObserved trace at N=30, T=7: {trace_observed:.4f}")
print(f"Ratio observed / estimated: {trace_observed / ell_joint_estimate:.2f}")

print()
print("=== Interpretation ===")
ratio = trace_observed / ell_joint_estimate
if 0.5 < ratio < 3:
    print(f"Match within factor 3. Pass-7 reframe is CONSISTENT.")
    print(f"Residual factor {ratio:.2f} likely from:")
    print(f"  - Approximate first-zero values (estimates only)")
    print(f"  - Tail factor for higher zeros (used 2, true is 1.5-3)")
    print(f"  - Finite-T explicit-formula remainder")
elif 3 <= ratio < 10:
    print(f"Match within factor {ratio:.1f}. AMBIGUOUS.")
    print(f"Need LMFDB-quality data for full validation.")
else:
    print(f"Ratio {ratio:.2f} outside 0.3-10 range. Pass-7 may not be consistent.")

print()
print("=== Required next step ===")
print("Replace estimated first zeros with actual LMFDB values for:")
for name in dirichlet_first_zeros:
    print(f"  {name}")
print("Then compute full ell_1^joint(30) from first 20+ zeros of each L-function.")
print("Expected: structural calibration c_30 = sqrt(ell_1^joint(30) / trace)")
print("should be a clean arithmetic constant (e.g., 1, 1/sqrt(phi(30)), etc.)")
