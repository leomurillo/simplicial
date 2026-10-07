"""
Follow-up to P1 success: check if a single scalar rescaling
of the multiplicative Dirichlet ledger brings ALL moments toward ell_n.

If yes: only calibration remains; the structural form is correct.
If no: per-character structure also needs adjustment.
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi
mp.dps = 30

N = 30
T = 7.0
e_T = exp(mpf(T))

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

def sieve(n):
    sa = [True] * (n + 1); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5)+1):
        if sa[i]:
            for j in range(i*i, n+1, i): sa[j] = False
    return [i for i, v in enumerate(sa) if v]

primes = sieve(int(float(e_T)) + 1)
primes_coprime = [p for p in primes if 30 % p != 0]
prime_powers = []
for p in primes_coprime:
    pk = p; k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k)); pk *= p; k += 1

y = {r: mpf(0) for r in units}
for pk, p, k in prime_powers:
    r = pk % N
    if r in y:
        y[r] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
y_bar = sum(y.values()) / phi_N
y_tilde = {r: y[r] - y_bar for r in units}

chars = [(a, b) for a in range(4) for b in range(2)]
nontriv = [c for c in chars if c != (0, 0)]

hat_y = {}
for (a, b) in chars:
    val = mpc(0, 0)
    for r in units:
        val += y_tilde[r] * mpc(chi_func(a, b, r)).conjugate()
    val /= sqrt(mpf(phi_N))
    hat_y[(a, b)] = val
lambdas = {k: abs(hat_y[k]) ** 2 for k in chars}

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
]
ell = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas) for n in range(11)]

# Original (no calibration)
trace = sum(lambdas[c] for c in nontriv)
pn_orig = [sum(lambdas[c] ** (n + 1) for c in nontriv) for n in range(11)]

# Calibration: pick c such that p_0 = ell_1 exactly, i.e. c^2 = ell_1 / trace
cal = sqrt(ell[0] / trace)
print(f"=== Calibration probe ===")
print(f"Original trace = {float(trace):.4e}")
print(f"ell_1 = {float(ell[0]):.4e}")
print(f"Calibration factor c = sqrt(ell_1 / trace) = {float(cal):.6f}")
print()

# Apply calibration
lambdas_cal = {k: lambdas[k] * cal ** 2 for k in chars}
pn_cal = [sum(lambdas_cal[c] ** (n + 1) for c in nontriv) for n in range(11)]

print(f"Calibrated lambda_chi values (sorted):")
for k in sorted(nontriv, key=lambda c: float(lambdas_cal[c]), reverse=True):
    print(f"  chi_{k}: lambda = {float(lambdas_cal[k]):.4e}")

print()
print(f"Atoms vs first folded zero eigenvalues:")
print(f"  Largest cal-lambda: {float(max(lambdas_cal[c] for c in nontriv)):.4e}")
print(f"  gamma_1^-2          = {float(mpf(1)/gammas[0]**2):.4e}")
print()

print(f"Power sums after calibration (matched p_0 by construction):")
print(f"  {'n':>3} {'ell_{n+1}':>14} {'p_n (cal)':>14} {'ratio':>10}")
for n in range(11):
    r = float(pn_cal[n] / ell[n])
    print(f"  {n:>3} {float(ell[n]):>14.4e} {float(pn_cal[n]):>14.4e} {r:>10.4f}")

print()
print(f"=== Summary ===")
print(f"After single-scalar calibration:")
all_within_factor_10 = all(0.1 <= float(pn_cal[n] / ell[n]) <= 10 for n in range(11))
all_within_factor_100 = all(0.01 <= float(pn_cal[n] / ell[n]) <= 100 for n in range(11))
print(f"  All 11 moment ratios within factor 10:  {all_within_factor_10}")
print(f"  All 11 moment ratios within factor 100: {all_within_factor_100}")
worst = max(abs(float(log(pn_cal[n] / ell[n]) / log(10))) for n in range(11))
print(f"  Worst |log10(ratio)| across n: {worst:.3f}")
