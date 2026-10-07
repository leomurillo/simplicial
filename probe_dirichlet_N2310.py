"""
A: N = 2310 multiplicative Dirichlet apex probe.

N = 2310 = 2 * 3 * 5 * 7 * 11, phi(2310) = 480.
Tests whether the convergence pattern N=30 -> 210 -> 2310 continues monotonically.

Uses numpy for heavy character computation, mpmath only for cumulant precision.
"""

import numpy as np
from mpmath import mp, mpf, log
mp.dps = 30

import time

N = 2310
T = 7.0
e_T = float(np.exp(T))

# Unit residues mod 2310: coprime to 2, 3, 5, 7, 11
primes_of_N = [2, 3, 5, 7, 11]
units = [u for u in range(1, N) if all(u % q != 0 for q in primes_of_N)]
phi_N = len(units)
print(f"N = {N}, phi(N) = {phi_N}")
assert phi_N == 480, f"Expected phi(2310) = 480, got {phi_N}"

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
    raise ValueError

# Precompute discrete logs as arrays
print("Computing discrete logs...")
dlog = np.zeros((phi_N, 4), dtype=np.int32)
for i, u in enumerate(units):
    for j, p in enumerate([3, 5, 7, 11]):
        dlog[i, j] = disc_log_local(u, p)

# Character indexing: (a, b, c, d) in Z/2 x Z/4 x Z/6 x Z/10
char_index = []
for a in range(2):
    for b in range(4):
        for c in range(6):
            for d in range(10):
                char_index.append((a, b, c, d))
assert len(char_index) == phi_N, f"char count = {len(char_index)}"

# Build character matrix M[j, i] = chi_j(u_i)
# chi_(a,b,c,d)(u) = (-1)^(a*e3) * exp(2pi*i*b*e5/4) * exp(2pi*i*c*e7/6) * exp(2pi*i*d*e11/10)
print(f"Building {phi_N} x {phi_N} character matrix...")
t0 = time.time()
M = np.zeros((phi_N, phi_N), dtype=np.complex128)
for j, (a, b, c, d) in enumerate(char_index):
    # For each character, compute its values on all units
    # Vectorize over i
    e3 = dlog[:, 0]
    e5 = dlog[:, 1]
    e7 = dlog[:, 2]
    e11 = dlog[:, 3]
    phase = ((np.pi * a * e3) +
             (2 * np.pi * b * e5 / 4) +
             (2 * np.pi * c * e7 / 6) +
             (2 * np.pi * d * e11 / 10))
    M[j, :] = np.exp(1j * phase)
print(f"  built in {time.time()-t0:.2f}s")

# Spot-check orthogonality: M @ M^H should be diagonal phi_N * I
print("Spot-check orthonormality (random 3 pairs):")
for _ in range(3):
    i = np.random.randint(phi_N)
    j = np.random.randint(phi_N)
    val = np.dot(M[i, :], np.conj(M[j, :]))
    expected = phi_N if i == j else 0
    print(f"  <chi_{i}, chi_{j}> = {abs(val):.4f} (expect {expected})")

# ----------------------------------------------------------------------
# Build prime-power ledger
# ----------------------------------------------------------------------
print("\nSieving primes and prime powers...")
def sieve(n):
    sa = np.ones(n + 1, dtype=bool); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sa[i]:
            sa[i*i::i] = False
    return np.where(sa)[0].tolist()

primes_all = sieve(int(e_T) + 1)
primes_coprime = [p for p in primes_all if N % p != 0]

prime_powers = []
for p in primes_coprime:
    pk = p; k = 1
    while pk <= e_T:
        prime_powers.append((pk, p, k))
        pk *= p; k += 1
print(f"Primes coprime to {N}: {len(primes_coprime)}")
print(f"Prime powers <= e^T: {len(prime_powers)}")

# Build y(r) for r in units (use dict, then array)
unit_index = {u: i for i, u in enumerate(units)}
y = np.zeros(phi_N, dtype=np.float64)
for pk, p, k in prime_powers:
    r = pk % N
    if r in unit_index:
        y[unit_index[r]] += np.log(p) / (p ** (k / 2.0))

y_bar = y.mean()
y_tilde = y - y_bar
print(f"\nMean y_bar = {y_bar:.6f}")
print(f"sum y_tilde = {y_tilde.sum():.2e}")

# Character coefficients via matrix-vector product
# hat_y_j = (1/sqrt(phi_N)) sum_i conj(chi_j(u_i)) * y_tilde_i
print("\nComputing character coefficients...")
hat_y = (np.conj(M) @ y_tilde) / np.sqrt(phi_N)
lambdas = np.abs(hat_y) ** 2

trace = lambdas.sum() - lambdas[0]  # subtract trivial-character mode
nontriv_lambdas = np.delete(lambdas, 0)  # remove (0,0,0,0) which is trivial
# Actually we should identify which index is trivial; trivial char is (0,0,0,0) = index 0
# (since char_index[0] = (0,0,0,0))

print(f"\nTrivial-char amplitude (should be ~0 after centering): {lambdas[0]:.4e}")
print(f"Sum non-trivial lambda = {trace:.6e}")

# ----------------------------------------------------------------------
# Comparison to ell_n
# ----------------------------------------------------------------------
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
    103.725538040478339416, 105.446623052087647076,
    107.168611184276407515, 111.029535543018306543,
    111.874659177002948212, 114.320220915452712780,
    116.226680320857554382, 118.790782866263209222,
    121.370125002420645918, 122.946829294678492525,
    124.256818554345767565, 127.516683879596495124,
    129.578704199956050985, 131.087688530932656723,
    133.497737203718394113, 134.756509753373871136,
    138.116042054533443200, 139.736208952121388017,
    141.123707404021123761, 143.111845807895079352,
]
ell_np = np.array([sum(1.0 / g ** (2 * (n + 1)) for g in gammas_list) for n in range(11)])

# Use mpmath for ell precision
gammas_mp = [mpf(repr(g)) for g in gammas_list]
ell_mp = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas_mp) for n in range(11)]

# Calibration
cal_sq = float(ell_mp[0]) / trace
cal = np.sqrt(cal_sq)
lambdas_cal = nontriv_lambdas * cal_sq

# Largest atoms (sorted)
sorted_lams = np.sort(lambdas_cal)[::-1]

print(f"\nCalibration c = {cal:.6f}")
print(f"Max calibrated lambda = {sorted_lams[0]:.6e}")
print(f"gamma_1^-2            = {1/gammas_list[0]**2:.6e}")
print(f"Overshoot factor    = {sorted_lams[0] / (1/gammas_list[0]**2):.4f}")
print()

# Top 20 atom comparison
print(f"Top 20 calibrated atoms vs first 20 gamma_k^-2:")
print(f"  {'rank':>4} {'lambda_cal':>14} {'gamma_k^-2':>14} {'ratio':>8}")
for i in range(20):
    if i < len(sorted_lams) and i < len(gammas_list):
        gk_inv_sq = 1.0 / gammas_list[i] ** 2
        ratio = sorted_lams[i] / gk_inv_sq
        print(f"  {i+1:>4} {sorted_lams[i]:>14.4e} {gk_inv_sq:>14.4e} {ratio:>8.4f}")

# Power sums (use mpmath for precision at large n)
print(f"\nPower sums vs ell_{{n+1}}:")
print(f"  {'n':>3} {'ell_{n+1}':>14} {'p_n (cal)':>14} {'ratio':>10} {'|log10|':>10}")
lambdas_mp = [mpf(float(l)) for l in lambdas_cal]
power_sums = []
worst_log = 0
for n in range(11):
    pn = sum(l ** (n + 1) for l in lambdas_mp)
    power_sums.append(pn)
    ratio = float(pn / ell_mp[n])
    log_dev = abs(float(log(pn / ell_mp[n]) / log(10)))
    if log_dev > worst_log:
        worst_log = log_dev
    print(f"  {n:>3} {float(ell_mp[n]):>14.4e} {float(pn):>14.4e} {ratio:>10.4f} {log_dev:>10.4f}")

print(f"\nWorst |log10(ratio)|: {worst_log:.4f}")

# ----------------------------------------------------------------------
# Comparison: N = 30, 210, 2310
# ----------------------------------------------------------------------
print()
print("=" * 80)
print("Convergence pattern N = 30 -> 210 -> 2310 (T = 7)")
print("=" * 80)
data = [
    ("N = 30",    8, 1.5191, 0.1064, 7.35e-3, 1.4700, 1.8360),
    ("N = 210",  48, 4.7048, 0.0628, 3.04e-3, 0.6075, 2.0786),
    ("N = 2310", 480, trace, cal,    sorted_lams[0], sorted_lams[0]/(1/gammas_list[0]**2), worst_log),
]
print(f"  {'label':>10} {'phi(N)':>8} {'trace':>10} {'c':>8} {'max_lam':>10} {'overshoot':>10} {'worst |log10|':>14}")
for (label, phi, tr, c, ml, os, wl) in data:
    print(f"  {label:>10} {phi:>8} {tr:>10.4e} {c:>8.4f} {ml:>10.4e} {os:>10.4f} {wl:>14.4f}")

print()
print("=== Interpretation ===")
overshoots = [1.47, 0.61, sorted_lams[0] / (1/gammas_list[0]**2)]
print(f"Overshoot trajectory: {overshoots[0]:.2f} -> {overshoots[1]:.2f} -> {overshoots[2]:.2f}")
if abs(overshoots[2] - 1) < abs(overshoots[1] - 1):
    print("  -> Converging toward 1 (Conjecture 6.2 supported)")
elif overshoots[2] < overshoots[1]:
    print("  -> Continuing to decrease past 1 (atoms shrinking faster than expected)")
else:
    print("  -> Pattern unclear; needs more data")

worst_logs = [1.84, 2.08, worst_log]
print(f"Worst log10 trajectory: {worst_logs[0]:.2f} -> {worst_logs[1]:.2f} -> {worst_logs[2]:.2f}")
