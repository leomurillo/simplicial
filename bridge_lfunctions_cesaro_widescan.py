"""
bridge_lfunctions_cesaro_widescan.py
====================================

Pass-8 step (3b): extended Cesaro validation with two goals:

(a) Push T_MAX up to 18-20 so that the longest zero-oscillation period of
    the smallest gamma_1 (~3.06 for chi_15 Legendre) is captured over many
    cycles in the Cesaro window.  The relevant cycle count is
        N_cycles = gamma_1 * (T_1 - T_0) / (2 pi).
    At T window [4, 18] that's 3.06 * 14 / (2 pi) ~ 6.8 cycles for gamma_1.
    At T window [4, 18] for gamma_2 of chi_15 (~5.34) we get 11.9 cycles.
    More cycles -> better Cesaro averaging of the oscillating term.

(b) Compute Cesaro averages over RECEDING windows [T_lo, T_max] with
    T_lo sweeping toward T_max; this isolates the long-T behavior.

(c) Decompose the trace into per-character |S_chi(T)|^2 to see the
    central-value baseline directly per chi.

The key empirical question: as the window pushes higher, does the Cesaro
mean approach
        C_central + C_spectral = 1.188

or does it stabilize closer to the central value alone (0.970)?

The answer should be:
  * In a TRULY asymptotic Cesaro limit (T_0 -> oo), the trace mean
    converges to predicted_mean = 1.188 because spectral term is the
    diagonal of the Hilbert space inner product of S_chi(T) with itself.
  * In FINITE Cesaro windows, the spectral term is undercounted because
    not all zero pairs (gamma_1, gamma_2) have completed enough mutual
    oscillation cycles for the off-diagonal to wash out, AND the truncated
    explicit-formula remainder R_chi(T) is non-negligible.

We measure the rate of convergence to test the Pass-7 corrected identity.
"""

import math
import sys
import io
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi

mp.dps = 30

N = 30
units = [1, 7, 11, 13, 17, 19, 23, 29]
phi_N = 8

def disc_log(u):
    for e1 in range(4):
        for e2 in range(2):
            if (pow(7, e1, 30) * pow(11, e2, 30)) % 30 == u:
                return (e1, e2)
dlog = {u: disc_log(u) for u in units}

def chi_func(a, b, u):
    e1, e2 = dlog[u]
    return exp(mpc(0, pi * a * e1 / 2)) * mpf((-1) ** (b * e2))

chars = [(a, b) for a in range(4) for b in range(2)]
nontriv = [c for c in chars if c != (0, 0)]

def sieve_up_to(n):
    sa = [True] * (n + 1); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sa[i]:
            for j in range(i*i, n+1, i): sa[j] = False
    return [i for i, v in enumerate(sa) if v]

# Push T_MAX to 17 (e^17 ~ 24 million); sieve cost ~10s
T_MAX = 17.0
print(f"Sieving primes up to e^{T_MAX} = {math.exp(T_MAX):.2e} ...")
t0 = time.time()
sieve_max = int(math.exp(T_MAX)) + 1
primes_all = sieve_up_to(sieve_max)
primes_coprime = [p for p in primes_all if 30 % p != 0]
print(f"  sieve done in {time.time()-t0:.1f}s; {len(primes_coprime)} primes coprime to 30 up to e^{T_MAX}")

t0 = time.time()
prime_powers = []
for p in primes_coprime:
    pk = p
    k = 1
    while pk <= math.exp(T_MAX):
        prime_powers.append((pk, p, k))
        pk *= p
        k += 1
prime_powers.sort()
print(f"  {len(prime_powers)} prime powers <= e^{T_MAX}; sort done in {time.time()-t0:.1f}s")

t0 = time.time()
pp_weights = []
for pk, p, k in prime_powers:
    w = log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
    r = pk % N
    pp_weights.append((pk, r, w))
print(f"  weights done in {time.time()-t0:.1f}s")

chi_table = {(a, b): {u: mpc(chi_func(a, b, u)) for u in units} for (a, b) in chars}

def trace_and_per_chi(T_val):
    """Return (trace, {chi: |hat_y_chi|^2})."""
    e_T = math.exp(T_val)
    y = {r: mpf(0) for r in units}
    for pk, r, w in pp_weights:
        if pk <= e_T:
            y[r] += w
        else:
            break
    y_bar = sum(y.values()) / phi_N
    y_tilde = {r: y[r] - y_bar for r in units}
    hat_y = {}
    for c in chars:
        tab = chi_table[c]
        val = mpc(0)
        for r in units:
            val += y_tilde[r] * tab[r].conjugate()
        val /= sqrt(mpf(phi_N))
        hat_y[c] = val
    lambdas = {c: float(abs(hat_y[c]) ** 2) for c in chars}
    trace = sum(lambdas[c] for c in nontriv)
    return trace, lambdas

# Dense T-grid for Cesaro averaging
dT = mpf("0.05")
T_grid = []
T = mpf("3.0")
while T <= mpf(T_MAX) + dT/2:
    T_grid.append(float(T))
    T = T + dT

print(f"\nComputing trace on T-grid of {len(T_grid)} points (dT={dT}) ...")
t0 = time.time()
trace_vals = []
per_chi_vals = []
for i, T_val in enumerate(T_grid):
    tr, lam = trace_and_per_chi(T_val)
    trace_vals.append(tr)
    per_chi_vals.append(lam)
    if (i + 1) % 50 == 0:
        print(f"  done {i+1}/{len(T_grid)}: T={T_val:.2f} trace={tr:.4f} ({time.time()-t0:.1f}s)")
elapsed = time.time() - t0
print(f"  T-scan complete in {elapsed:.1f}s\n")

# ---------------------------------------------------------------------
# Cesaro and per-chi Cesaro analysis
# ---------------------------------------------------------------------

def cesaro_grid(values, T_lo, T_hi):
    pts = [(T, v) for T, v in zip(T_grid, values) if T_lo <= T <= T_hi]
    if len(pts) < 2:
        return None
    s = 0.0
    for i in range(len(pts) - 1):
        s += 0.5 * (pts[i][1] + pts[i+1][1]) * (pts[i+1][0] - pts[i][0])
    return s / (pts[-1][0] - pts[0][0])

with open(r"C:\Projects\simplicial\bridge_lfunctions_central_values.json") as f:
    pred = json.load(f)

# Per-character predicted Cesaro means: |L'/L(chi,1/2)|^2 + sum 1/gamma^2 (for that chi)
# We need per-chi |L'/L|^2 (from JSON) and per-chi 1/gamma^2 sums (from LMFDB zero data).

char_LpL_sq = {r["name"]: r["LpL_abs_sq"] for r in pred["characters"]}

# Map our (a,b) characters to the named primitive characters.
# The 8 characters (a,b) in Z/4 x Z/2 mod 30 induce L-functions whose
# zero spectrum equals that of their primitive ancestor (which may be of
# conductor 3, 5, 15, or 30); chi_0 is excluded.
#
# To match (a,b) to a primitive character, compute the character's order
# and which subgroup it factors through.  We use the discrete-log table
# (e1 in Z/4 from g_1=7, e2 in Z/2 from g_2=11).
#   g_1 = 7  -> mod 5: 7 == 2, so g_1 mod 5 is the order-4 generator;
#                mod 3: 7 == 1, trivial on (Z/3)^*.
#   g_2 = 11 -> mod 5: 11 == 1, trivial on (Z/5)^*;
#                mod 3: 11 == 2 == -1, so g_2 is the generator of (Z/3)^*.
#
# So  chi_{(a,b)}(g_1) = i^a   <-> on (Z/5)^*, chi(2) = i^a
#     chi_{(a,b)}(g_2) = (-1)^b <-> on (Z/3)^*, chi(-1) = (-1)^b
#
# Mapping:
#   a = 0, b = 0: trivial
#   a = 0, b = 1: chi_3                    (Legendre mod 3)
#   a = 2, b = 0: chi_5 quadratic          (Legendre mod 5)
#   a = 2, b = 1: chi_15 quadratic         (Legendre x Legendre, mod 15)
#   a = 1, b = 0: chi_5 quartic_a
#   a = 1, b = 1: chi_15 (Leg x quartic_a)
#   a = 3, b = 0: chi_5 quartic_b
#   a = 3, b = 1: chi_15 (Leg x quartic_b)

ab_to_name = {
    (0, 1): "chi_3  (Legendre mod 3)",
    (2, 0): "chi_5  (Legendre mod 5)",
    (2, 1): "chi_15 (Legendre mod 15)",
    (1, 0): "chi_5  (quartic_a mod 5)",
    (1, 1): "chi_15 (Legendre x quartic_a mod 15)",
    (3, 0): "chi_5  (quartic_b mod 5, conj)",
    (3, 1): "chi_15 (Legendre x quartic_b mod 15)",
}

# Per-chi zero-sums (sum 1/gamma^2 over all zeros, including +/- pair where applicable)
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

# Map name -> zero spectrum (full +/- gamma sum)
zero_sums = {
    "chi_3  (Legendre mod 3)":            2 * sum(1.0/g**2 for g in zeros_chi3),
    "chi_5  (Legendre mod 5)":            2 * sum(1.0/g**2 for g in zeros_chi5_leg),
    "chi_15 (Legendre mod 15)":           2 * sum(1.0/g**2 for g in zeros_chi15_leg),
    "chi_5  (quartic_a mod 5)":           sum(1.0/g**2 for g in zeros_chi5_quart),
    "chi_5  (quartic_b mod 5, conj)":     sum(1.0/g**2 for g in zeros_chi5_quart),
    "chi_15 (Legendre x quartic_a mod 15)": sum(1.0/g**2 for g in zeros_chi15_quart),
    "chi_15 (Legendre x quartic_b mod 15)": sum(1.0/g**2 for g in zeros_chi15_quart),
}

# Per-character predicted Cesaro mean (the |S_chi(T)|^2 mean is
# |L'/L|^2 + sum 1/gamma^2, before averaging across characters and /phi(N)).
predicted_per_chi = {}
for c in nontriv:
    name = ab_to_name[c]
    LpL2 = char_LpL_sq[name]
    spec = zero_sums[name]
    predicted_per_chi[c] = LpL2 + spec

print("=" * 80)
print(" Per-character |S_chi(T)|^2 Cesaro analysis")
print("=" * 80)
print()
print(f"  {'chi':<10} {'name':<40} {'<|S|^2/phi>':>13} {'predicted':>11} {'ratio':>8}")
print(f"  {'-'*10} {'-'*40} {'-'*13} {'-'*11} {'-'*8}")
# Cesaro of per-chi |hat_y_chi|^2 = |S_chi|^2 / phi (with our normalization)
T_lo_global = 4.0
T_hi_global = T_MAX
total_predicted = 0.0
total_observed = 0.0
for c in nontriv:
    vals_c = [pcv[c] for pcv in per_chi_vals]
    avg_c = cesaro_grid(vals_c, T_lo_global, T_hi_global)
    pred_c = predicted_per_chi[c] / phi_N  # because hat_y_chi = S_chi/sqrt(phi)
    name = ab_to_name[c]
    total_observed += avg_c
    total_predicted += pred_c
    print(f"  {str(c):<10} {name:<40} {avg_c:>13.5f} {pred_c:>11.5f} {avg_c/pred_c:>8.3f}")

print(f"  {'-'*10} {'-'*40} {'-'*13} {'-'*11} {'-'*8}")
print(f"  {'TOTAL':<51} {total_observed:>13.5f} {total_predicted:>11.5f} {total_observed/total_predicted:>8.3f}")
print()

# ---------------------------------------------------------------------
# Receding-window Cesaro: how does the average behave as T_lo grows?
# ---------------------------------------------------------------------

print("=" * 80)
print(" Receding-window Cesaro: <trace>_T over [T_lo, T_max]")
print("=" * 80)
print()
C_central = pred["C_central"]
C_spectral = pred["C_spectral"]
print(f"  predicted = C_central + C_spectral = {C_central:.4f} + {C_spectral:.4f} = {C_central + C_spectral:.4f}")
print(f"  predicted (central only) = {C_central:.4f}")
print()
print(f"  {'T_lo':>6} {'<trace>':>10} {'predicted':>10} {'(/predicted)':>14} {'(/central)':>13}")
print(f"  {'-'*6} {'-'*10} {'-'*10} {'-'*14} {'-'*13}")
for T_lo in [4.0, 6.0, 8.0, 10.0, 12.0, 14.0]:
    if T_lo + 1.0 >= T_MAX:
        continue
    avg = cesaro_grid(trace_vals, T_lo, T_MAX)
    print(f"  {T_lo:>6.1f} {avg:>10.4f} {C_central+C_spectral:>10.4f} {avg/(C_central+C_spectral):>14.4f} {avg/C_central:>13.4f}")

# ---------------------------------------------------------------------
# Diagnostic: variance of trace_vals about the empirical mean
# ---------------------------------------------------------------------
import statistics
print()
print("=" * 80)
print(" Trace oscillation statistics on [4, T_max]")
print("=" * 80)
print()
vals_in_window = [v for T, v in zip(T_grid, trace_vals) if 4.0 <= T <= T_MAX]
print(f"  mean       = {statistics.mean(vals_in_window):.4f}")
print(f"  stdev      = {statistics.stdev(vals_in_window):.4f}")
print(f"  min, max   = {min(vals_in_window):.4f}, {max(vals_in_window):.4f}")
print(f"  predicted  = {C_central + C_spectral:.4f}")
print(f"  central    = {C_central:.4f}")
print(f"  spectral   = {C_spectral:.4f}")

# ---------------------------------------------------------------------
# Save artifact
# ---------------------------------------------------------------------
out = {
    "N": 30,
    "T_MAX": T_MAX,
    "dT": float(dT),
    "T_grid": T_grid,
    "trace_vals": trace_vals,
    "C_central": C_central,
    "C_spectral": C_spectral,
    "predicted_mean": C_central + C_spectral,
    "receding_windows": [
        {"T_lo": T_lo, "T_hi": T_MAX,
         "cesaro": cesaro_grid(trace_vals, T_lo, T_MAX)}
        for T_lo in [4.0, 6.0, 8.0, 10.0, 12.0]
    ],
    "per_chi_cesaro": {
        str(c): {
            "name": ab_to_name[c],
            "cesaro_mean": cesaro_grid([pcv[c] for pcv in per_chi_vals], T_lo_global, T_hi_global),
            "predicted": predicted_per_chi[c] / phi_N,
        }
        for c in nontriv
    },
}
with open(r"C:\Projects\simplicial\bridge_lfunctions_cesaro_widescan.json", "w") as f:
    json.dump(out, f, indent=2)
print()
print("  Wrote: bridge_lfunctions_cesaro_widescan.json")
