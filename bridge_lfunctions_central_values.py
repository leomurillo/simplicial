"""
bridge_lfunctions_central_values.py
====================================

Pass-8 step (2): compute the central-value contribution to the Cesaro-averaged
multiplicative-apex trace at N = 30.

For each non-trivial Dirichlet character chi mod 30, compute

    C(chi) := | L'/L(chi, 1/2) |^2

via Hurwitz-zeta decomposition of L(chi,s) and a high-order finite difference
for the logarithmic derivative.  Sum across the 7 non-trivial characters and
divide by phi(30) = 8 to get the central-value contribution

    C_central(N) := (1/phi(N)) sum_{chi != chi_0} |L'/L(chi, 1/2)|^2

which is the first additive term in the Cesaro-mean identity (Pass-7 Theorem):

    < trace(N, T) >_T  =  C_central(N) + ell_1^joint(N)/phi(N) + R(N, T_0, T_1).

Output is written as a small dictionary the validation script can ingest.

Conventions: a Dirichlet character chi mod q decomposes as
    L(chi, s) = q^{-s} sum_{a in U_q} chi(a) zeta(s, a/q),
which is what `compute_dirichlet_zeros_v3.py` uses.  We reuse that setup so the
central-value numbers are consistent with the zero data.
"""

import math
import sys
import io
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpc, mpf, zeta, log, sqrt

mp.dps = 40  # 40-digit working precision; finite-difference derivative is
             # accurate to roughly 30-35 digits at this dps

# ---------------------------------------------------------------------
# Dirichlet character setup at q in {3, 5, 15} (primitive characters
# with conductor dividing 30; conductor-1 trivial character is excluded)
# ---------------------------------------------------------------------

def L_chi(s, chi_vals, q):
    """Dirichlet L-function via Hurwitz-zeta decomposition.

    L(chi, s) = q^{-s} sum_{a=1}^{q-1} chi(a) zeta(s, a/q).
    Characters are passed as {a: chi(a)} on representatives 1..q-1.
    """
    s = mpc(s)
    total = mpc(0)
    for a, val in chi_vals.items():
        total += mpc(val) * zeta(s, mpf(a) / q)
    return total * mpc(q) ** (-s)

def Lprime_over_L(s, chi_vals, q, h=None):
    """Logarithmic derivative L'/L(chi, s) via centered finite difference.

    Uses a 4th-order central stencil to keep accuracy high:
        f'(s) ~ ( -f(s+2h) + 8 f(s+h) - 8 f(s-h) + f(s-2h) ) / (12 h)
    so that L'/L = f'/f at s = 1/2.
    """
    if h is None:
        h = mpf('1e-15')  # safe with dps=40
    h = mpf(h)
    f_p2 = L_chi(s + 2 * h, chi_vals, q)
    f_p1 = L_chi(s + h, chi_vals, q)
    f_m1 = L_chi(s - h, chi_vals, q)
    f_m2 = L_chi(s - 2 * h, chi_vals, q)
    f_0  = L_chi(s, chi_vals, q)
    f_prime = (-f_p2 + 8 * f_p1 - 8 * f_m1 + f_m2) / (12 * h)
    return f_prime / f_0

# Quadratic character mod 3 (Legendre / Kronecker -3)
chi_3 = {1: mpf(1), 2: mpf(-1)}

# Characters mod 5: 2 is a generator of (Z/5)^*
def chi_5_from_chi2(c):
    powers = {1: 0, 2: 1, 4: 2, 3: 3}
    return {a: c ** powers[a] for a in [1, 2, 3, 4]}

chi_5_quartic_a  = chi_5_from_chi2(mpc(0, 1))   # chi(2) = i (order 4)
chi_5_quadratic  = chi_5_from_chi2(mpf(-1))     # chi(2) = -1 (Legendre)
chi_5_quartic_b  = chi_5_from_chi2(mpc(0, -1))  # chi(2) = -i (order 4, conjugate)

# Characters mod 15 = 3 x 5 (CRT product)
def make_chi_15(chi5):
    out = {}
    for u in range(1, 15):
        if math.gcd(u, 15) == 1:
            out[u] = chi_3[u % 3] * chi5[u % 5]
    return out

chi_15_quadratic = make_chi_15(chi_5_quadratic)
chi_15_quartic_a = make_chi_15(chi_5_quartic_a)
chi_15_quartic_b = make_chi_15(chi_5_quartic_b)

# ---------------------------------------------------------------------
# Inventory of non-trivial primitive characters with conductor | 30
# ---------------------------------------------------------------------
#
# Conductor 30 has divisor lattice {1, 2, 3, 5, 6, 10, 15, 30}.
# Primitive characters mod q for q | 30 contribute to L-functions of
# conductor q dividing the modulus.  phi(30) = 8 induced characters:
#   1 trivial   (excluded)
#   1 primitive mod 3   (Legendre)
#   1 primitive mod 5   (Legendre)
#   2 primitive mod 5   (quartic + conjugate)
#   1 primitive mod 15  (Legendre x Legendre)
#   2 primitive mod 15  (Legendre x quartic + conjugate)
#
# Total: 7 non-trivial primitive characters with conductor dividing 30.
# Their L-functions agree with the corresponding characters mod 30 up to
# Euler factors at primes 2 and 5 (resp. 2, 3, 5), which is the standard
# convention; the multiplicative apex restricts to units mod N anyway.

CHARACTERS = [
    ("chi_3  (Legendre mod 3)",            chi_3,             3),
    ("chi_5  (Legendre mod 5)",            chi_5_quadratic,   5),
    ("chi_5  (quartic_a mod 5)",           chi_5_quartic_a,   5),
    ("chi_5  (quartic_b mod 5, conj)",     chi_5_quartic_b,   5),
    ("chi_15 (Legendre mod 15)",           chi_15_quadratic,  15),
    ("chi_15 (Legendre x quartic_a mod 15)", chi_15_quartic_a, 15),
    ("chi_15 (Legendre x quartic_b mod 15)", chi_15_quartic_b, 15),
]

# ---------------------------------------------------------------------
# Compute central values and |L'/L(chi,1/2)|^2
# ---------------------------------------------------------------------

print("=" * 80)
print(" Pass-8 step 2:  central-value contribution at N = 30")
print(" |L'/L(chi, 1/2)|^2  for each non-trivial primitive chi, conductor | 30")
print("=" * 80)
print()
header_LpL = "|L'/L|^2"
print(f"  {'character':<40} {'L(chi, 1/2)':>16} {header_LpL:>16}")
print(f"  {'-'*40} {'-'*16} {'-'*16}")

results = []
sum_LpL_sq = mpf(0)

t_start = time.time()
for name, chi_vals, q in CHARACTERS:
    L_half  = L_chi(mpc(mpf('0.5')), chi_vals, q)
    LpL     = Lprime_over_L(mpc(mpf('0.5')), chi_vals, q)
    LpL_sq  = (LpL.real ** 2 + LpL.imag ** 2)
    sum_LpL_sq += LpL_sq

    results.append({
        "name": name,
        "conductor": q,
        "L_half_re": float(L_half.real),
        "L_half_im": float(L_half.imag),
        "L_half_abs": float(abs(L_half)),
        "LpL_re": float(LpL.real),
        "LpL_im": float(LpL.imag),
        "LpL_abs_sq": float(LpL_sq),
    })
    print(f"  {name:<40} {float(abs(L_half)):>16.6f} {float(LpL_sq):>16.6f}")

elapsed = time.time() - t_start
print(f"  {'-'*40} {'-'*16} {'-'*16}")
sum_label = "SUM_chi |L'/L(chi, 1/2)|^2"
print(f"  {sum_label:<40} {'':>16} {float(sum_LpL_sq):>16.6f}")
print()

phi_N = 8
C_central = sum_LpL_sq / mpf(phi_N)
print(f"  phi(N) = {phi_N}")
print(f"  C_central(N) = (1/phi(N)) sum |L'/L|^2 = {float(C_central):.6f}")
print(f"  (this is the central-value contribution to <trace(30, T)>_T)")
print()
print(f"  Compute time: {elapsed:.1f}s at dps = {mp.dps}")
print()

# ---------------------------------------------------------------------
# Compare against ell_1^joint(N)/phi(N) (the spectral piece)
# ---------------------------------------------------------------------
# From compute_lmfdb_final_N30.py: ell_1^joint(30) ≈ 0.18 (truncated to
# first ~25 zeros of each L-function; LMFDB value).  We re-import and
# document the comparison without re-running the LMFDB script.

# Self-dual contributions (factor 2 from +/- gamma symmetry) and
# non-self-dual contributions are pre-summed in compute_lmfdb_final_N30.py.
# The value reported there is the truncated ell_1^joint(30) including
# zeta itself (conductor 1 sits inside the multiplicative apex through
# the trivial-character "structureless" mode -- it does NOT enter the
# non-trivial Cesaro identity below).
#
# For the apex Cesaro identity we want SUM over non-trivial primitive
# chi with conductor dividing 30, EXCLUDING chi_0 (zeta).  That equals
#   ell_1^joint(30)_{nontriv} = ell_1^joint(30)_{LMFDB} - 2*sum_zeta 1/g^2.

zeros_zeta = [
    14.134725141734694, 21.022039638771555, 25.010857580145689,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280915000, 48.005150881167160,
    49.773832477672302, 52.970321477714461, 56.446247697063395,
    59.347044002602353, 60.831778524609810, 65.112544048081607,
    67.079810529494174, 69.546401711173979, 72.067157674481908,
    75.704690699083933, 77.144840068874805, 79.337375020249368,
    82.910380854086030, 84.735492980517050, 87.425274613125229,
    88.809111207634465,
]
zeta_contribution = 2 * sum(1.0 / g ** 2 for g in zeros_zeta)
ell_1_joint_full = 0.18  # placeholder; will recompute below
# Re-derive directly here to keep this script self-contained:
zeros_chi3 = [
    8.039737155681467, 11.249206207772935, 15.704619176721626,
    18.261997495693128, 20.455770807742493, 24.059414856493451,
    26.577868735774585, 28.218164506233386, 30.745040261382496,
    33.897388927259419, 35.608412653938635, 37.551796556364627,
    39.485207260929351, 42.616379226157568, 44.120572912072202,
    46.274118023513140, 47.514104510117322, 50.375138650636266,
    52.496749599060754, 54.193843101551914,
]
zeros_chi5_leg = [
    6.64845334472771472, 9.83144443288666962, 11.95884562608351453,
    16.03382112838423567, 17.56699429232555520, 19.54073262278475025,
    22.22740545445941091, 24.58846621740819521, 26.77609594800414012,
    28.46103510017752248, 29.70790935048096557, 33.00045600687051437,
    34.72881297890480867, 35.86863837181227459, 38.12918472143653185,
    39.56057294640318171, 41.84243854579169431, 44.03129006144169504,
    45.42730008278228939, 46.49272715949140535, 48.34566182106784618,
    51.08775192674649136, 52.12590223131697419, 53.83044519544216335,
    55.58928033540481015,
]
zeros_chi15_leg = [
    3.05701820980868915, 5.34319209367996892, 7.26763059826680725,
    10.13374815522837580, 12.15969853381077082, 13.48938457315531804,
    15.24040852903903317, 16.63355841618558638, 19.10349718525469466,
    20.66236305141030677, 22.17639768821376109, 23.36799923867493538,
    24.90350116904296768, 26.31976601519719113, 28.65701374833144390,
    29.69227751983587214, 31.36470623994313229, 32.32338008181344539,
    33.78117919887043491, 35.09705568923789179, 36.99584669791703415,
    38.75734135997041883, 39.44089794397602895, 41.22823157698679018,
    41.99740257490063315,
]
# Non-self-dual quartic L-functions: paired zeros (positive + negative)
zeros_chi5_quart = [
    55.53255, 53.75667, 51.08999, 49.52011, 48.47766, 46.26641, 45.08582,
    43.12543, 40.50893, 39.09162, 37.84762, 36.09653, 33.30775, 31.71404,
    29.70278, 27.81247, 26.47279, 22.96558, 21.28305, 19.72905, 16.99590,
    14.11546, 11.28290, 9.44293, 4.13290,
    6.18358, 8.45723, 12.67495, 14.82503, 17.33780, 18.99859, 22.48758,
    24.36528, 25.53119, 27.98276, 30.46364, 32.19516, 34.45723, 35.49089,
    37.27195, 40.39611, 41.53646, 42.99209, 44.82618, 46.59016, 48.47785,
    50.66421, 51.97705, 53.44223, 54.48544,
]
zeros_chi15_quart = [
    42.88707, 41.80835, 40.40725, 39.02994, 36.85301, 35.99118, 34.37951,
    33.29703, 31.99774, 30.51935, 28.55272, 26.79624, 25.89259, 24.07186,
    23.14895, 21.28464, 19.13784, 17.44476, 16.17189, 14.46446, 13.02896,
    10.32620, 8.26450, 6.59078, 4.40670,
    2.73460, 5.24301, 8.41469, 10.18760, 11.90737, 13.33740, 15.36614,
    17.77239, 18.97700, 20.62763, 21.88397, 23.33848, 25.38803, 27.19473,
    28.39898, 29.66537, 31.19236, 32.15849, 34.25978, 35.81988, 37.22297,
    38.27968, 39.61718, 40.86974, 42.12516,
]

def s2(zs):
    return sum(1.0 / g ** 2 for g in zs)

# Non-trivial conductor | 30 piece: chi_3, chi_5(Leg), chi_15(Leg) self-dual,
# plus quartic pairs at mod 5 and mod 15.
ell1_nontriv = (
    2 * s2(zeros_chi3)
    + 2 * s2(zeros_chi5_leg)
    + 2 * s2(zeros_chi15_leg)
    + 2 * s2(zeros_chi5_quart)
    + 2 * s2(zeros_chi15_quart)
)

C_spectral = ell1_nontriv / phi_N

print("=" * 80)
print(" Spectral contribution at N = 30 (LMFDB-truncated)")
print("=" * 80)
print()
print(f"  2 * sum 1/g^2 contributions:")
print(f"    chi_3   (cond 3, self-dual):       {2*s2(zeros_chi3):.6f}")
print(f"    chi_5   (cond 5, Legendre):        {2*s2(zeros_chi5_leg):.6f}")
print(f"    chi_15  (cond 15, Legendre):       {2*s2(zeros_chi15_leg):.6f}")
print(f"    chi_5   (cond 5, quartic pair):    {2*s2(zeros_chi5_quart):.6f}")
print(f"    chi_15  (cond 15, quartic pair):   {2*s2(zeros_chi15_quart):.6f}")
print(f"  ell_1^joint(30) [non-trivial only]:  {ell1_nontriv:.6f}")
print(f"  Note: this EXCLUDES zeta contribution {zeta_contribution:.6f}")
print()
print(f"  C_spectral(N) = ell_1^joint(N)/phi(N) = {C_spectral:.6f}")
print()

# ---------------------------------------------------------------------
# Cesaro-mean prediction = central + spectral
# ---------------------------------------------------------------------
predicted_mean = float(C_central) + C_spectral
print("=" * 80)
print(" Pass-8 Cesaro-mean prediction at N = 30")
print("=" * 80)
print()
print(f"  <trace(30, T)>_T  =  C_central(30) + ell_1^joint(30)/phi(30) + R")
print(f"                    =  {float(C_central):.6f}   +  {C_spectral:.6f}   + R")
print(f"                    =  {predicted_mean:.6f} + R(30, T_0, T_1)")
print()

# Persist for the validation script
with open(r"C:\Projects\simplicial\bridge_lfunctions_central_values.json", "w") as f:
    json.dump({
        "N": 30,
        "phi_N": phi_N,
        "characters": results,
        "sum_LpL_sq": float(sum_LpL_sq),
        "C_central": float(C_central),
        "ell1_joint_nontriv": ell1_nontriv,
        "C_spectral": C_spectral,
        "predicted_cesaro_mean": predicted_mean,
    }, f, indent=2)

print("  Wrote: bridge_lfunctions_central_values.json")
