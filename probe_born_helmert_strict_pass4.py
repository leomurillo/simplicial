"""
Strict Pass-4 variant: only primes p dividing P_n = 30, i.e., p in {2, 3, 5}.
This restricts prime powers to residues sharing a factor with N=30.
Compare power sums to ell_{n+1} from known zeros.
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi, conj
mp.dps = 40

N = 30
T = 7.0
e_T = exp(mpf(T))
primes_strict = [2, 3, 5]

prime_powers = []
for p in primes_strict:
    pk = p; k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k))
        pk *= p; k += 1

print(f"=== Strict Pass-4 Variant: primes in {{2,3,5}} only ===")
print(f"Prime powers: {len(prime_powers)}")
for pk, p, k in prime_powers:
    print(f"  {p}^{k} = {pk}  (mod 30 = {pk % 30})")

y = [mpf(0)] * N
for pk, p, k in prime_powers:
    y[pk % N] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
y_bar = sum(y) / N
y_tilde = [y[r] - y_bar for r in range(N)]

print(f"\nLedger support (nonzero residues only):")
for r in range(N):
    if y[r] != 0 or abs(y_tilde[r]) > mpf("0.01"):
        print(f"  r = {r:>2}: y = {float(y[r]):>10.5f}, y_tilde = {float(y_tilde[r]):>10.5f}")

# DFT character coefficients
y_hat_born = []
for c in range(1, N):
    val = mpc(0, 0)
    for r in range(N):
        val += y_tilde[r] * exp(mpc(0, -2 * pi * c * r / N))
    val /= sqrt(mpf(N))  # Euclidean-orthonormal convention
    y_hat_born.append(val)

lambdas = [abs(yh) ** 2 for yh in y_hat_born]
trace = sum(lambdas)
print(f"\nBorn squared amplitudes:")
for c, lam in enumerate(lambdas, 1):
    print(f"  c = {c:>2}: lambda = {float(lam):.4e}")
print(f"Trace = {float(trace):.4e}")

power_sums = [sum(lam ** (n + 1) for lam in lambdas) for n in range(11)]

# Reference cumulants
gammas = [
    mpf("14.134725141734693790"), mpf("21.022039638771554993"),
    mpf("25.010857580145688763"), mpf("30.424876125859513210"),
    mpf("32.935061587739189691"), mpf("37.586178158825671257"),
    mpf("40.918719012147495187"), mpf("43.327073280914999519"),
    mpf("48.005150881167159728"), mpf("49.773832477672302182"),
]
ell = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas) for n in range(11)]

print(f"\nPower sums vs ell_{{n+1}} (first 10 zeros, strict):")
print(f"  {'n':>3} {'ell_{n+1}':>16} {'p_n (strict)':>16} {'ratio':>12}")
for n in range(11):
    ratio = float(power_sums[n] / ell[n]) if ell[n] != 0 else float("nan")
    print(f"  {n:>3} {float(ell[n]):>16.6e} {float(power_sums[n]):>16.6e} {ratio:>12.4e}")
