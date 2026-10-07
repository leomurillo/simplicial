"""
bridge_lfunctions_cesaro_validation.py
======================================

Pass-8 step (3): empirically verify the Cesaro-mean identity at N = 30 by
running the multiplicative-apex trace over a finer T-grid and averaging.

The Pass-7 claim (after correction) reads:

    < trace(N, T) >_{T in [T_0, T_1]}
        = (1/phi(N)) sum_{chi != chi_0} | L'/L(chi, 1/2) |^2          (central)
        + (1/phi(N)) ell_1^joint(N)                                    (spectral)
        + R(N, T_0, T_1)                                              (remainder)

with R -> 0 as T_0 -> infinity (rate depends on density of L-function zeros
near the bottom of the critical strip; classically R = O(1/T_1) under GRH).

This script:
 1. Loads central + spectral predictions from bridge_lfunctions_central_values.json.
 2. Runs the multiplicative-apex trace for T on a dense grid (dT = 0.1)
    spanning T in [4, 14].
 3. Computes Cesaro averages over several windows of widths W in {2, 4, 6, 10}.
 4. Compares to the predicted Cesaro mean.

Implementation note: at N = 30 with T up to 14, we cover primes up to
e^14 ~ 1.2 x 10^6.  Sieve cost dominates; we sieve once at T_max and
incrementally fill the truncated ledger at each smaller T.
"""

import math
import sys
import io
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi

mp.dps = 30

# ---------------------------------------------------------------------
# Sieve and ledger setup at N = 30
# ---------------------------------------------------------------------

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
            for j in range(i*i, n+1, i):
                sa[j] = False
    return [i for i, v in enumerate(sa) if v]

T_MAX = 14.0
print("Sieving primes up to e^{T_MAX} ...")
t0 = time.time()
sieve_max = int(math.exp(T_MAX)) + 1
primes_all = sieve_up_to(sieve_max)
primes_coprime = [p for p in primes_all if 30 % p != 0]
print(f"  sieve done in {time.time()-t0:.1f}s; {len(primes_coprime)} primes coprime to 30 up to e^{T_MAX}")

# Build prime-power list with (pk, p, k, log pk) for incremental ledger updates.
print("Enumerating prime powers ...")
t0 = time.time()
prime_powers = []
for p in primes_coprime:
    pk = p
    k = 1
    while pk <= math.exp(T_MAX):
        prime_powers.append((pk, p, k))
        pk *= p
        k += 1
prime_powers.sort()  # sort by pk so we can incrementally include
print(f"  {len(prime_powers)} prime powers <= e^{T_MAX}; sort done in {time.time()-t0:.1f}s")

# Precompute (log p) / sqrt(p^k) per prime power, with mpmath precision
print("Precomputing weights ...")
t0 = time.time()
pp_weights = []
for pk, p, k in prime_powers:
    w = log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
    r = pk % N
    pp_weights.append((pk, r, w))
print(f"  weights done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------
# Trace(N, T) computation for any T
# ---------------------------------------------------------------------

# Precompute character values on each unit residue (complex)
chi_table = {(a, b): {u: mpc(chi_func(a, b, u)) for u in units} for (a, b) in chars}

def trace_at_T(T_val, max_idx_cache=[0]):
    """Compute the apex trace at gauge T using the incremental ledger.

    max_idx_cache is a list-as-mutable holding the prior cutoff index; this
    helper is only called with monotonically nondecreasing T_val in our
    main loop so we can incrementally extend the ledger.
    """
    e_T = math.exp(T_val)
    # Build y as a dict on units
    y = {r: mpf(0) for r in units}
    # We rebuild from scratch (cheap once weights are cached, ~1e5 entries)
    # rather than incremental cache to keep helper pure.
    for pk, r, w in pp_weights:
        if pk <= e_T:
            y[r] += w
        else:
            break
    y_bar = sum(y.values()) / phi_N
    y_tilde = {r: y[r] - y_bar for r in units}

    # Character coefficients hat_y_chi = (1/sqrt(phi)) sum_r y_tilde(r) chi(r)bar
    hat_y = {}
    for c in chars:
        tab = chi_table[c]
        val = mpc(0)
        for r in units:
            val += y_tilde[r] * tab[r].conjugate()
        val /= sqrt(mpf(phi_N))
        hat_y[c] = val

    # Born squares; trace excludes trivial character
    lambdas = {c: abs(hat_y[c]) ** 2 for c in chars}
    trace = sum(lambdas[c] for c in nontriv)
    return float(trace)

# ---------------------------------------------------------------------
# Dense T-grid and Cesaro averages
# ---------------------------------------------------------------------

dT = mpf("0.1")  # density of grid; coarser dT is OK because trace is bandlimited
T_grid = []
T = mpf("4.0")
while T <= mpf("14.0") + dT/2:
    T_grid.append(float(T))
    T = T + dT

print(f"\nComputing trace on T-grid of {len(T_grid)} points (dT={dT}) ...")
t0 = time.time()
trace_vals = []
for i, T_val in enumerate(T_grid):
    tr = trace_at_T(T_val)
    trace_vals.append(tr)
    if (i + 1) % 10 == 0:
        print(f"  done {i+1}/{len(T_grid)}: T={T_val:.2f} trace={tr:.4f} ({time.time()-t0:.1f}s)")
elapsed = time.time() - t0
print(f"  T-scan complete in {elapsed:.1f}s")

# ---------------------------------------------------------------------
# Cesaro averages over windows
# ---------------------------------------------------------------------
# Numerical average over [T_lo, T_hi] of trace, using trapezoidal rule on grid.

def cesaro(T_lo, T_hi):
    pts = [(T, tr) for T, tr in zip(T_grid, trace_vals) if T_lo <= T <= T_hi]
    if len(pts) < 2:
        return None
    s = 0.0
    for i in range(len(pts) - 1):
        T0, tr0 = pts[i]
        T1, tr1 = pts[i+1]
        s += 0.5 * (tr0 + tr1) * (T1 - T0)
    return s / (pts[-1][0] - pts[0][0])

# Load predictions
with open(r"C:\Projects\simplicial\bridge_lfunctions_central_values.json") as f:
    pred = json.load(f)

C_central = pred["C_central"]
C_spectral = pred["C_spectral"]
predicted_mean = pred["predicted_cesaro_mean"]

print()
print("=" * 80)
print(f" Cesaro-mean validation: predicted = {predicted_mean:.4f}")
print(f"   central = {C_central:.4f}, spectral = {C_spectral:.4f}")
print("=" * 80)
print()

windows = [
    (4, 6), (4, 8), (4, 10), (4, 12), (4, 14),
    (6, 10), (6, 14),
    (8, 14),
    (10, 14),
]
print(f"  {'window':<15} {'<trace>':>10} {'predicted':>10} {'ratio':>10} {'remainder':>12}")
print(f"  {'-'*15} {'-'*10} {'-'*10} {'-'*10} {'-'*12}")
for T_lo, T_hi in windows:
    avg = cesaro(T_lo, T_hi)
    ratio = avg / predicted_mean
    remainder = avg - predicted_mean
    print(f"  [{T_lo:>4.1f},{T_hi:>4.1f}]   {avg:>10.4f} {predicted_mean:>10.4f} {ratio:>10.4f} {remainder:>12.4f}")

# ---------------------------------------------------------------------
# Save the trace-vs-T data for the writeup
# ---------------------------------------------------------------------
out = {
    "N": 30,
    "T_grid": T_grid,
    "trace_vals": trace_vals,
    "C_central": C_central,
    "C_spectral": C_spectral,
    "predicted_mean": predicted_mean,
    "windows": [
        {"T_lo": T_lo, "T_hi": T_hi, "cesaro": cesaro(T_lo, T_hi)}
        for (T_lo, T_hi) in windows
    ],
}
with open(r"C:\Projects\simplicial\bridge_lfunctions_cesaro_validation.json", "w") as f:
    json.dump(out, f, indent=2)
print()
print("  Wrote: bridge_lfunctions_cesaro_validation.json")
