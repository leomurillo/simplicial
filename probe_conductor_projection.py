"""
Diagnostic: project prime ledger onto each conductor packet separately.
Check whether ANY conductor packet's Born squares come close to ell_n.

If yes: tells us the candidate should be restricted to that packet.
If no: tells us the conductor-additive structure is fundamentally wrong.
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi
mp.dps = 30

N = 30
T = 7.0
e_T = exp(mpf(T))

def sieve(n):
    sa = [True] * (n + 1); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5)+1):
        if sa[i]:
            for j in range(i*i, n+1, i): sa[j] = False
    return [i for i, v in enumerate(sa) if v]

primes = sieve(int(float(e_T))+1)
prime_powers = []
for p in primes:
    pk = p; k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k)); pk *= p; k += 1

y_p = [mpf(0)] * N
for pk, p, k in prime_powers:
    y_p[pk % N] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
y_p_bar = sum(y_p) / N
y_p_tilde = [y_p[r] - y_p_bar for r in range(N)]

# Character amplitudes
y_hat_born = []
for c in range(1, N):
    val = mpc(0, 0)
    for r in range(N):
        val += y_p_tilde[r] * exp(mpc(0, -2 * pi * c * r / N))
    val /= sqrt(mpf(N))
    y_hat_born.append(val)
lambdas = [abs(yh) ** 2 for yh in y_hat_born]

# Group by conductor
def cond(c, N):
    from math import gcd
    return N // gcd(c, N)

conductor_groups = {}
for c in range(1, N):
    d = cond(c, N)
    conductor_groups.setdefault(d, []).append(c)

print(f"Conductor packets at N = {N}:")
for d in sorted(conductor_groups):
    chars = conductor_groups[d]
    packet_lambdas = [lambdas[c - 1] for c in chars]
    packet_trace = sum(packet_lambdas)
    print(f"  Conductor {d}: chars {chars} (varphi(d)={len(chars)})")
    print(f"    lambdas: {[float(l) for l in packet_lambdas]}")
    print(f"    trace: {float(packet_trace):.4e}")

# Reference
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
]
ell = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas) for n in range(6)]

print(f"\nTotal trace = {float(sum(lambdas)):.4e}; ell_1 = {float(ell[0]):.4e}")
print()
print(f"Per-packet power sums vs ell_n (ratios):")
print(f"{'cond':>6} " + " ".join(f"{'p'+str(n)+'/ell':>13}" for n in range(6)))
for d in sorted(conductor_groups):
    chars = conductor_groups[d]
    packet_lambdas = [lambdas[c - 1] for c in chars]
    pn = [sum(l ** (n + 1) for l in packet_lambdas) for n in range(6)]
    ratios = [float(pn[n] / ell[n]) for n in range(6)]
    print(f"{d:>6} " + " ".join(f"{r:>13.4e}" for r in ratios))

# Find smallest power-sum packet ratio
print()
best_d = None
best_ratio = float('inf')
for d in sorted(conductor_groups):
    chars = conductor_groups[d]
    packet_lambdas = [lambdas[c - 1] for c in chars]
    pn0 = sum(packet_lambdas)
    ratio = float(pn0 / ell[0])
    if ratio < best_ratio:
        best_ratio = ratio
        best_d = d

print(f"Best single conductor packet: d = {best_d}, p_0 ratio = {best_ratio:.4e}")
print(f"Baseline (all conductors): {float(sum(lambdas) / ell[0]):.4e}")
print(f"Improvement of best packet: {float(sum(lambdas)) / best_ratio / float(ell[0]):.2f}x")
