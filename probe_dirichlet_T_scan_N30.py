"""
T-scan at fixed N = 30: how does the calibration constant c(30, T) behave?

Conjecture 6.1: as N, T jointly grow, c -> 1 (i.e. Var_U(y) -> ell_1).
At fixed N = 30, only finite resolution (8 chars) is available, so we
cannot expect full moment match. But we CAN test:
  (a) Does c stabilize, grow, or shrink with T?
  (b) Does max atom approach gamma_1^{-2}?
  (c) Does the worst moment ratio improve?

If c stabilizes at some c_inf(30) != 1, the limit is genuinely joint.
If c -> 1 at fixed N = 30, that would be remarkable.
"""

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

def sieve(n):
    sa = [True] * (n + 1); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5)+1):
        if sa[i]:
            for j in range(i*i, n+1, i): sa[j] = False
    return [i for i, v in enumerate(sa) if v]

# Reference cumulants
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

def probe_at_T(T_val):
    e_T = exp(mpf(T_val))
    primes_all = sieve(int(float(e_T)) + 1)
    primes_coprime = [p for p in primes_all if 30 % p != 0]
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

    hat_y = {}
    for (a, b) in chars:
        val = mpc(0, 0)
        for r in units:
            val += y_tilde[r] * mpc(chi_func(a, b, r)).conjugate()
        val /= sqrt(mpf(phi_N))
        hat_y[(a, b)] = val
    lambdas = {k: abs(hat_y[k]) ** 2 for k in chars}

    trace = sum(lambdas[c] for c in nontriv)
    cal = sqrt(ell[0] / trace)
    lambdas_cal = {k: lambdas[k] * cal ** 2 for k in chars}
    pn_cal = [sum(lambdas_cal[c] ** (n + 1) for c in nontriv) for n in range(11)]

    max_lam = max(float(lambdas_cal[c]) for c in nontriv)
    overshoot = max_lam / float(mpf(1) / gammas[0] ** 2)

    worst_log = max(abs(float(log(pn_cal[n] / ell[n]) / log(10))) for n in range(11))

    return {
        "T": T_val,
        "n_primes": len(primes_coprime),
        "n_pp": len(prime_powers),
        "trace": float(trace),
        "calibration_c": float(cal),
        "c_squared": float(cal ** 2),
        "max_lam_cal": max_lam,
        "overshoot": overshoot,
        "worst_log_ratio": worst_log,
    }

print("=== T-scan at fixed N = 30 ===")
print()
print(f"{'T':>5} {'n_primes':>9} {'n_pp':>6} {'trace':>10} {'c':>10} "
      f"{'max_lam':>11} {'overshoot':>11} {'worst |log10|':>14}")
print("-" * 95)

T_values = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
results = []
for T_val in T_values:
    r = probe_at_T(T_val)
    results.append(r)
    print(f"{r['T']:>5.1f} {r['n_primes']:>9} {r['n_pp']:>6} "
          f"{r['trace']:>10.4e} {r['calibration_c']:>10.4f} "
          f"{r['max_lam_cal']:>11.4e} {r['overshoot']:>11.4f} "
          f"{r['worst_log_ratio']:>14.4f}")

print()
print("=== Trend analysis ===")
print()
print("Calibration constant c(30, T):")
for i, r in enumerate(results):
    bar = "#" * int(min(80, r['calibration_c'] * 200))
    print(f"  T = {r['T']:>4.1f}: c = {r['calibration_c']:.4f}  {bar}")

print()
print("Atom overshoot lambda_max / gamma_1^-2:")
for r in results:
    bar = "#" * int(min(80, r['overshoot'] * 30))
    print(f"  T = {r['T']:>4.1f}: overshoot = {r['overshoot']:.4f}  {bar}")

print()
print("Worst |log10(ratio)| across 11 moments:")
for r in results:
    bar = "#" * int(min(80, r['worst_log_ratio'] * 20))
    print(f"  T = {r['T']:>4.1f}: worst = {r['worst_log_ratio']:.4f}  {bar}")

# Trend test: is c stabilizing? going to 1? going to 0?
print()
print("=== Interpretation ===")
cs = [r['calibration_c'] for r in results]
trace_seq = [r['trace'] for r in results]
overshoots = [r['overshoot'] for r in results]

# Check if c monotone
if all(cs[i] <= cs[i+1] for i in range(len(cs)-1)):
    print("  Calibration c is monotonically INCREASING with T.")
elif all(cs[i] >= cs[i+1] for i in range(len(cs)-1)):
    print("  Calibration c is monotonically DECREASING with T.")
else:
    print("  Calibration c is NON-MONOTONE with T.")

# Trace asymptotic
print(f"  Trace at T=4:  {trace_seq[0]:.4e}")
print(f"  Trace at T=12: {trace_seq[-1]:.4e}")
print(f"  Ratio: {trace_seq[-1] / trace_seq[0]:.4f}")

# Variance grows as T*log(N)/varphi(N) roughly (Bombieri-Vinogradov style)
print()
print("=== Bombieri-Vinogradov heuristic ===")
print(f"BV-style prediction: Var ~ const * T at fixed N.")
print(f"Empirical Var(T) / T:")
for r in results:
    print(f"  T = {r['T']:>4.1f}: Var/T = {r['trace'] / r['T']:.4f}")
