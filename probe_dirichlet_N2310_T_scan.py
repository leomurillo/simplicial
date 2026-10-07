"""
N = 2310 at multiple T values to find the regime where the apex converges.

Hypothesis: at N = 2310 (phi = 480), need T large enough that prime powers
densely populate residue classes. Heuristic: T such that pi(e^T) >> phi(N).
"""

import numpy as np
from mpmath import mp, mpf, log as mp_log
mp.dps = 30

N = 2310
primes_of_N = [2, 3, 5, 7, 11]
units = [u for u in range(1, N) if all(u % q != 0 for q in primes_of_N)]
phi_N = len(units)
unit_index = {u: i for i, u in enumerate(units)}

# Local generators
gens = {3: 2, 5: 2, 7: 3, 11: 2}
orders = {3: 2, 5: 4, 7: 6, 11: 10}

def disc_log_local(u, p):
    target = u % p
    g = gens[p]
    val = 1
    for e in range(orders[p]):
        if val == target:
            return e
        val = (val * g) % p

dlog = np.zeros((phi_N, 4), dtype=np.int32)
for i, u in enumerate(units):
    for j, p in enumerate([3, 5, 7, 11]):
        dlog[i, j] = disc_log_local(u, p)

char_index = [(a, b, c, d) for a in range(2) for b in range(4) for c in range(6) for d in range(10)]

# Build character matrix once
print(f"Building {phi_N} x {phi_N} character matrix...")
M = np.zeros((phi_N, phi_N), dtype=np.complex128)
for j, (a, b, c, d) in enumerate(char_index):
    e3 = dlog[:, 0]; e5 = dlog[:, 1]; e7 = dlog[:, 2]; e11 = dlog[:, 3]
    phase = (np.pi * a * e3 +
             2 * np.pi * b * e5 / 4 +
             2 * np.pi * c * e7 / 6 +
             2 * np.pi * d * e11 / 10)
    M[j, :] = np.exp(1j * phase)
print("done.")

def sieve(n):
    sa = np.ones(n + 1, dtype=bool); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sa[i]:
            sa[i*i::i] = False
    return np.where(sa)[0].tolist()

# Reference cumulants from first 50 zeros
gammas_list = [
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
gammas_mp = [mpf(repr(g)) for g in gammas_list]
ell_mp = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas_mp) for n in range(11)]

def probe_at_T(T_val, verbose=False):
    e_T = float(np.exp(T_val))
    primes_all = sieve(int(e_T) + 1)
    primes_coprime = [p for p in primes_all if N % p != 0]
    prime_powers = []
    for p in primes_coprime:
        pk = p; k = 1
        while pk <= e_T:
            prime_powers.append((pk, p, k))
            pk *= p; k += 1

    y = np.zeros(phi_N, dtype=np.float64)
    for pk, p, k in prime_powers:
        r = pk % N
        if r in unit_index:
            y[unit_index[r]] += np.log(p) / (p ** (k / 2.0))

    # Count nonzero residue classes
    n_nonzero = np.sum(y > 0)

    y_bar = y.mean()
    y_tilde = y - y_bar

    hat_y = (np.conj(M) @ y_tilde) / np.sqrt(phi_N)
    lambdas = np.abs(hat_y) ** 2
    trace = lambdas.sum() - lambdas[0]
    nontriv_lambdas = np.delete(lambdas, 0)

    cal_sq = float(ell_mp[0]) / trace
    cal = np.sqrt(cal_sq)
    lambdas_cal = nontriv_lambdas * cal_sq
    sorted_lams = np.sort(lambdas_cal)[::-1]

    overshoot = sorted_lams[0] / (1.0 / gammas_list[0] ** 2)

    lambdas_mp = [mpf(float(l)) for l in lambdas_cal]
    worst_log = 0
    pn_list = []
    for n in range(11):
        pn = sum(l ** (n + 1) for l in lambdas_mp)
        pn_list.append(pn)
        log_dev = abs(float(mp_log(pn / ell_mp[n]) / mp_log(10)))
        if log_dev > worst_log:
            worst_log = log_dev

    return {
        "T": T_val,
        "n_pp": len(prime_powers),
        "n_primes": len(primes_coprime),
        "n_nonzero": n_nonzero,
        "trace": trace,
        "c": cal,
        "max_lam": sorted_lams[0],
        "overshoot": overshoot,
        "worst_log": worst_log,
        "lams_top10": sorted_lams[:10].tolist(),
        "pn_top5": [float(pn_list[n] / ell_mp[n]) for n in range(6)],
    }

print(f"\n=== T-scan at N = 2310 (phi = 480) ===")
print(f"{'T':>5} {'n_pp':>7} {'n_nonzero':>10} {'trace':>10} "
      f"{'c':>10} {'max_lam':>11} {'overshoot':>10} {'worst_log':>10}")
print("-" * 90)

results = []
for T_val in [7, 9, 11, 13, 15]:
    r = probe_at_T(T_val)
    results.append(r)
    print(f"{r['T']:>5} {r['n_pp']:>7} {r['n_nonzero']:>10} {r['trace']:>10.4e} "
          f"{r['c']:>10.4f} {r['max_lam']:>11.4e} {r['overshoot']:>10.4f} "
          f"{r['worst_log']:>10.4f}")

# Detailed report on best T
best = min(results, key=lambda r: r['worst_log'])
print(f"\n=== Best T = {best['T']} for N = 2310 ===")
print(f"n_pp = {best['n_pp']}; n_nonzero unit residues = {best['n_nonzero']}/{phi_N}")
print(f"Calibration c = {best['c']:.6f}")
print(f"Overshoot = {best['overshoot']:.4f}")
print(f"Worst |log10(ratio)| = {best['worst_log']:.4f}")
print()
print("Top 10 atoms vs gamma_k^-2:")
print(f"  {'k':>3} {'lambda':>14} {'gamma_k^-2':>14} {'ratio':>8}")
for i in range(10):
    g_inv_sq = 1.0 / gammas_list[i] ** 2
    ratio = best['lams_top10'][i] / g_inv_sq
    print(f"  {i+1:>3} {best['lams_top10'][i]:>14.4e} {g_inv_sq:>14.4e} {ratio:>8.4f}")

print()
print(f"Power-sum ratios (first 6):")
for n in range(6):
    print(f"  n = {n}: {best['pn_top5'][n]:.4f}")

# Compare to N=210 best
print()
print("=== Comparison: N=30, 210, 2310 (each at their best T) ===")
n30 = {"phi": 8, "T": 7, "trace": 1.52, "c": 0.106, "max_lam": 7.35e-3,
       "overshoot": 1.47, "worst_log": 1.84}
n210 = {"phi": 48, "T": 7, "trace": 4.70, "c": 0.063, "max_lam": 3.04e-3,
        "overshoot": 0.61, "worst_log": 2.08}
n2310 = {"phi": 480, "T": best['T'], "trace": best['trace'], "c": best['c'],
         "max_lam": best['max_lam'], "overshoot": best['overshoot'], "worst_log": best['worst_log']}

print(f"  {'label':>10} {'phi':>6} {'T':>4} {'trace':>10} {'c':>8} "
      f"{'max_lam':>11} {'overshoot':>10} {'worst_log':>10}")
for label, d in [("N=30", n30), ("N=210", n210), ("N=2310", n2310)]:
    print(f"  {label:>10} {d['phi']:>6} {d['T']:>4.1f} {d['trace']:>10.4e} "
          f"{d['c']:>8.4f} {d['max_lam']:>11.4e} {d['overshoot']:>10.4f} "
          f"{d['worst_log']:>10.4f}")
