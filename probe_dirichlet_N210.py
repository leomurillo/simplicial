"""
N-scan probe: multiplicative Dirichlet apex at N = 210.

N = 210 = 2*3*5*7, phi(210) = 48 (6x more characters than N=30).
Test whether more character resolution improves moment match.

If max overshoot improves, atoms approach gamma_1^{-2}; supports Conjecture 6.2.
If calibration c moves toward 1, supports Conjecture 6.1.
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi
mp.dps = 30

N = 210
T = 7.0
e_T = exp(mpf(T))

# Unit residues mod 210: coprime to 2, 3, 5, 7
units = [u for u in range(1, N) if all(u % q != 0 for q in [2, 3, 5, 7])]
phi_N = len(units)
print(f"N = {N}, phi(N) = {phi_N}")
print(f"First 10 unit residues: {units[:10]}")

# Local generators: g_3 = 2 (Z/3), g_5 = 2 (Z/5), g_7 = 3 (Z/7)
# Z/2 trivial (only unit is 1)
generators_local = {3: 2, 5: 2, 7: 3}
local_orders = {3: 2, 5: 4, 7: 6}

def disc_log_local(u, p):
    """Discrete log of u mod p, base generator g_p."""
    g = generators_local[p]
    target = u % p
    for e in range(local_orders[p]):
        if pow(g, e, p) == target:
            return e
    raise ValueError(f"No disc log for {u} mod {p}")

def disc_log_crt(u):
    """Return (e_3, e_5, e_7) for u in (Z/210)^*."""
    return (disc_log_local(u, 3),
            disc_log_local(u, 5),
            disc_log_local(u, 7))

dlog = {u: disc_log_crt(u) for u in units}

# Character: chi_{(a,b,c)} with a in Z/2 (mod 3 part), b in Z/4 (mod 5 part), c in Z/6 (mod 7 part)
# chi(u) = (-1)^(a*e_3) * i^(b*e_5) * zeta_6^(c*e_7)
zeta_6 = exp(mpc(0, pi / 3))  # primitive 6th root of unity

def chi_func(a, b, c, u):
    e3, e5, e7 = dlog[u]
    return mpf((-1) ** (a * e3)) * exp(mpc(0, pi * b * e5 / 2)) * zeta_6 ** (c * e7)

chars = [(a, b, c) for a in range(2) for b in range(4) for c in range(6)]
trivial_char = (0, 0, 0)
nontriv = [k for k in chars if k != trivial_char]
print(f"Total characters: {len(chars)} ({len(nontriv)} non-trivial)")

# Quick orthonormality check
print("Quick character orthogonality check (random pair):")
k1, k2 = (0, 1, 0), (1, 2, 3)
s1 = sum(chi_func(*k1, u) * mpc(chi_func(*k1, u)).conjugate() for u in units)
s2 = sum(chi_func(*k1, u) * mpc(chi_func(*k2, u)).conjugate() for u in units)
print(f"  <chi_{k1}, chi_{k1}>: {float(abs(s1)):.4f} (expect {phi_N})")
print(f"  <chi_{k1}, chi_{k2}>: {float(abs(s2)):.4f} (expect 0)")

# Prime powers coprime to 210
def sieve(n):
    sa = [True] * (n + 1); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5)+1):
        if sa[i]:
            for j in range(i*i, n+1, i): sa[j] = False
    return [i for i, v in enumerate(sa) if v]

primes_all = sieve(int(float(e_T)) + 1)
primes_coprime = [p for p in primes_all if 210 % p != 0]
prime_powers = []
for p in primes_coprime:
    pk = p; k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k)); pk *= p; k += 1

print(f"\nPrime cutoff T = {T}, e^T = {float(e_T):.2f}")
print(f"Primes coprime to 210: {len(primes_coprime)} (from {primes_coprime[0]} to {primes_coprime[-1]})")
print(f"Prime powers: {len(prime_powers)}")

# Build ledger on units
y = {r: mpf(0) for r in units}
for pk, p, k in prime_powers:
    r = pk % N
    if r in y:
        y[r] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
y_bar = sum(y.values()) / phi_N
y_tilde = {r: y[r] - y_bar for r in units}

# Character coefficients
print(f"\nComputing {len(chars)} character coefficients over {phi_N} unit residues...")
hat_y = {}
for k in chars:
    val = mpc(0, 0)
    for r in units:
        val += y_tilde[r] * mpc(chi_func(*k, r)).conjugate()
    val /= sqrt(mpf(phi_N))
    hat_y[k] = val

lambdas = {k: abs(hat_y[k]) ** 2 for k in chars}
trace = sum(lambdas[k] for k in nontriv)

# Reference cumulants from first 50 zeros
gammas = [
    mpf("14.134725141734693790"), mpf("21.022039638771554993"),
    mpf("25.010857580145688763"), mpf("30.424876125859513210"),
    mpf("32.935061587739189691"), mpf("37.586178158825671257"),
    mpf("40.918719012147495187"), mpf("43.327073280914999519"),
    mpf("48.005150881167159728"), mpf("49.773832477672302182"),
    mpf("52.970321477714460644"), mpf("56.446247697063394804"),
    mpf("59.347044002602353079"), mpf("60.831778524609809844"),
    mpf("65.112544048081606660"), mpf("67.079810529494173714"),
    mpf("69.546401711173979253"), mpf("72.067157674481907583"),
    mpf("75.704690699083933168"), mpf("77.144840068874805373"),
    mpf("79.337375020249367922"), mpf("82.910380854086030183"),
    mpf("84.735492980517050106"), mpf("87.425274613125229407"),
    mpf("88.809111207634465423"), mpf("92.491899270558484296"),
    mpf("94.651344040519886967"), mpf("95.870634228245309831"),
    mpf("98.831194218193198281"), mpf("101.317851005731391228"),
    mpf("103.725538040478339416"), mpf("105.446623052087647076"),
    mpf("107.168611184276407515"), mpf("111.029535543018306543"),
    mpf("111.874659177002948212"), mpf("114.320220915452712780"),
    mpf("116.226680320857554382"), mpf("118.790782866263209222"),
    mpf("121.370125002420645918"), mpf("122.946829294678492525"),
    mpf("124.256818554345767565"), mpf("127.516683879596495124"),
    mpf("129.578704199956050985"), mpf("131.087688530932656723"),
    mpf("133.497737203718394113"), mpf("134.756509753373871136"),
    mpf("138.116042054533443200"), mpf("139.736208952121388017"),
    mpf("141.123707404021123761"), mpf("143.111845807895079352"),
]
ell = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas) for n in range(11)]

cal = sqrt(ell[0] / trace)
lambdas_cal = {k: lambdas[k] * cal ** 2 for k in chars}
pn_cal = [sum(lambdas_cal[k] ** (n + 1) for k in nontriv) for n in range(11)]

max_lam = max(float(lambdas_cal[k]) for k in nontriv)
overshoot = max_lam / float(mpf(1) / gammas[0] ** 2)

print(f"\n=== Results at (N, T) = (210, 7) ===")
print(f"Trace (non-trivial) = {float(trace):.6e}")
print(f"Calibration c       = {float(cal):.6f}")
print(f"Max calibrated lambda = {max_lam:.6e}")
print(f"gamma_1^-2            = {float(mpf(1) / gammas[0] ** 2):.6e}")
print(f"Overshoot factor    = {overshoot:.4f}")
print()

print(f"Top 10 calibrated atoms (sorted) vs first 10 gamma_k^-2:")
sorted_lams = sorted([float(lambdas_cal[k]) for k in nontriv], reverse=True)
gammas_inv_sq = [float(mpf(1) / g ** 2) for g in gammas[:10]]
print(f"  {'rank':>4} {'lambda':>14} {'gamma_k^-2':>14} {'ratio':>8}")
for i in range(min(10, len(sorted_lams))):
    if i < len(gammas_inv_sq):
        r = sorted_lams[i] / gammas_inv_sq[i]
        print(f"  {i+1:>4} {sorted_lams[i]:>14.4e} {gammas_inv_sq[i]:>14.4e} {r:>8.4f}")
    else:
        print(f"  {i+1:>4} {sorted_lams[i]:>14.4e}")

print()
print(f"Power sums vs ell_{{n+1}} (first 30 zeros reference):")
print(f"  {'n':>3} {'ell_{n+1}':>14} {'p_n (cal)':>14} {'ratio':>10} {'|log10|':>10}")
worst_log = 0
for n in range(11):
    r = float(pn_cal[n] / ell[n])
    log_dev = abs(float(log(pn_cal[n] / ell[n]) / log(10)))
    if log_dev > worst_log:
        worst_log = log_dev
    print(f"  {n:>3} {float(ell[n]):>14.4e} {float(pn_cal[n]):>14.4e} {r:>10.4f} {log_dev:>10.4f}")

print(f"\nWorst |log10(ratio)|: {worst_log:.4f}")
print()

# Compare to N=30
n30_data = {"trace": 1.5191, "c": 0.1064, "max_lam": 7.35e-3,
            "overshoot": 1.47, "worst_log": 1.836}
print(f"=== Comparison: N=30 vs N=210 (T=7) ===")
print(f"  {'metric':>20} {'N=30':>14} {'N=210':>14} {'change':>14}")
print(f"  {'trace':>20} {n30_data['trace']:>14.4e} {float(trace):>14.4e} "
      f"{(float(trace)/n30_data['trace']-1)*100:>+13.1f}%")
print(f"  {'calibration c':>20} {n30_data['c']:>14.4f} {float(cal):>14.4f} "
      f"{(float(cal)/n30_data['c']-1)*100:>+13.1f}%")
print(f"  {'max lambda':>20} {n30_data['max_lam']:>14.4e} {max_lam:>14.4e} "
      f"{(max_lam/n30_data['max_lam']-1)*100:>+13.1f}%")
print(f"  {'overshoot':>20} {n30_data['overshoot']:>14.4f} {overshoot:>14.4f} "
      f"{(overshoot/n30_data['overshoot']-1)*100:>+13.1f}%")
print(f"  {'worst |log10|':>20} {n30_data['worst_log']:>14.4f} {worst_log:>14.4f} "
      f"{(worst_log/n30_data['worst_log']-1)*100:>+13.1f}%")
