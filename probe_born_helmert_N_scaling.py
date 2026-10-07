"""
Scaling diagnostic: same prime cutoff T=7, vary N.
Check if p_n / ell_{n+1} scales cleanly with N.

If ratio = C_n * N^k for some k, the moment identity in
Pass-5 Theorem 19.1 needs a normalization patch.
If irregular, the candidate ledger needs structural correction (R1).
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi
mp.dps = 30

T = 7.0
e_T = exp(mpf(T))

# Sieve primes up to e^T
def sieve(n):
    sa = [True] * (n + 1)
    sa[0] = sa[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sa[i]:
            for j in range(i*i, n+1, i):
                sa[j] = False
    return [i for i, v in enumerate(sa) if v]

primes = sieve(int(float(e_T)) + 1)
prime_powers = []
for p in primes:
    pk = p; k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k))
        pk *= p; k += 1

print(f"Prime cutoff T = {T}, e^T = {float(e_T):.2f}")
print(f"Primes: {len(primes)}, prime powers: {len(prime_powers)}")
print()

def probe_at_N(N):
    """Compute power sums for the permissive prime ledger at this N."""
    y = [mpf(0)] * N
    for pk, p, k in prime_powers:
        y[pk % N] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
    y_bar = sum(y) / N
    y_tilde = [y[r] - y_bar for r in range(N)]

    # Born squared amplitudes via direct DFT (Euclidean-orthonormal convention)
    lambdas = []
    for c in range(1, N):
        val = mpc(0, 0)
        for r in range(N):
            val += y_tilde[r] * exp(mpc(0, -2 * pi * c * r / N))
        val /= sqrt(mpf(N))
        lambdas.append(abs(val) ** 2)

    # Power sums
    pn = []
    for n in range(6):  # n = 0..5
        pn.append(sum(lam ** (n + 1) for lam in lambdas))
    return pn, sum(lambdas)  # power sums and trace

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
]
ell = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas) for n in range(6)]

# Run at various N
Ns = [6, 10, 12, 14, 15, 21, 30, 42, 60, 105, 210]

print(f"{'N':>5} {'trace':>14} " + " ".join(f"{'p'+str(n)+'/ell'+str(n+1):>14}" for n in range(6)))
print("-" * (5 + 14 + 1 + 6 * 15))

results = {}
for N in Ns:
    pn, trace = probe_at_N(N)
    results[N] = (pn, trace)
    ratios = [float(pn[n] / ell[n]) for n in range(6)]
    print(f"{N:>5} {float(trace):>14.4e} " + " ".join(f"{r:>14.4e}" for r in ratios))

print()
print("Scaling analysis: log_N(ratio) at each n")
print(f"{'N':>5} " + " ".join(f"{'logN(p'+str(n)+'/ell)':>15}" for n in range(6)))
print("-" * (5 + 1 + 6 * 16))
for N in Ns:
    pn, _ = results[N]
    log_ratios = []
    for n in range(6):
        r = float(pn[n] / ell[n])
        if r > 0:
            log_ratios.append(log(mpf(r)) / log(mpf(N)))
        else:
            log_ratios.append(float('nan'))
    print(f"{N:>5} " + " ".join(f"{float(lr):>15.4f}" for lr in log_ratios))

print()
print("If log_N(ratio) is constant across N (for each fixed n), the scaling")
print("is N^k for k = that constant. Different rows at different n indicate")
print("the exponent k depends on n.")
