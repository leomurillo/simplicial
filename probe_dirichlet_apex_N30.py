"""
P1: Multiplicative Dirichlet apex probe at N = 30.

Construction:
- Units U = (Z/30)^* = {1, 7, 11, 13, 17, 19, 23, 29}, |U| = phi(30) = 8.
- Generators: (Z/30)^* = <7> x <11> = Z/4 x Z/2 with g1 = 7, g2 = 11.
- 8 Dirichlet characters chi_{(a,b)} for (a,b) in Z/4 x Z/2.
- Multiplicative ledger:
    y(r) = sum_{p^k = r mod 30, p coprime to 30, p^k <= e^T} log(p)/p^(k/2)
    for r in U.
- Centered: tilde_y(r) = y(r) - mean_{r in U} y(r).
- Character coefficient:
    hat_y(chi) = (1/sqrt(|U|)) sum_{r in U} chi(r) * tilde_y(r)  [orthonormal convention]
- Born squares: lambda_chi = |hat_y(chi)|^2.
- Power sums vs ell_{n+1}.

Pre-committed criteria (same as R1):
- Success: >= 100x improvement vs additive baseline at N=30 (which had p_0 = 310)
- Failure: <= 10x improvement
- Ambiguous: 10-100, iterate
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi
mp.dps = 30

N = 30
T = 7.0
e_T = exp(mpf(T))

# Unit residues mod 30
units = [1, 7, 11, 13, 17, 19, 23, 29]
phi_N = len(units)  # = 8

# Generators of (Z/30)^* = Z/4 x Z/2 with g1=7 (order 4), g2=11 (order 2)
# Discrete log: each unit u in U expressed as g1^e1 * g2^e2 mod 30.
def disc_log(u):
    """Return (e1, e2) such that u = 7^e1 * 11^e2 mod 30."""
    for e1 in range(4):
        for e2 in range(2):
            if (pow(7, e1, 30) * pow(11, e2, 30)) % 30 == u:
                return (e1, e2)
    raise ValueError(f"unit {u} not found")

dlog_table = {u: disc_log(u) for u in units}
print("Discrete log table (u = 7^e1 * 11^e2 mod 30):")
for u in units:
    e1, e2 = dlog_table[u]
    print(f"  {u} = 7^{e1} * 11^{e2}")
print()

# Enumerate Dirichlet characters (chi(7) = i^a, chi(11) = (-1)^b) for (a,b) in Z/4 x Z/2
def dirichlet_char(a, b):
    """Return chi: U -> C defined by chi(7^e1 * 11^e2) = i^(a*e1) * (-1)^(b*e2)."""
    def chi(u):
        e1, e2 = dlog_table[u]
        return exp(mpc(0, pi * a * e1 / 2)) * mpf((-1) ** (b * e2))
    return chi

chars = [(a, b) for a in range(4) for b in range(2)]
print(f"Enumerated {len(chars)} Dirichlet characters mod {N}.")
print()

# Verify orthogonality of characters
print("Verifying character orthogonality:")
for i, (a1, b1) in enumerate(chars):
    chi1 = dirichlet_char(a1, b1)
    for j, (a2, b2) in enumerate(chars):
        chi2 = dirichlet_char(a2, b2)
        s = sum(chi1(u) * mpc(chi2(u)).conjugate() for u in units)
        s_real = abs(s) / phi_N  # should be 1 if same, 0 if different
        # Show only diagonal entries
        if i == j:
            if abs(s - phi_N) > mpf("1e-20"):
                print(f"  WARN: chi_{(a1,b1)} self-pairing = {s} (expect {phi_N})")
print("  Orthogonality OK.")
print()

# ----------------------------------------------------------------------
# Prime powers coprime to 30, <= e^T
# ----------------------------------------------------------------------
def sieve(n):
    sa = [True] * (n + 1); sa[0] = sa[1] = False
    for i in range(2, int(n**0.5)+1):
        if sa[i]:
            for j in range(i*i, n+1, i): sa[j] = False
    return [i for i, v in enumerate(sa) if v]

primes = sieve(int(float(e_T)) + 1)
primes_coprime = [p for p in primes if 30 % p != 0]  # exclude 2, 3, 5

prime_powers = []
for p in primes_coprime:
    pk = p; k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k)); pk *= p; k += 1

print(f"Primes coprime to 30, p <= e^T: {len(primes_coprime)} (from p = 7 to {primes_coprime[-1]})")
print(f"Prime powers: {len(prime_powers)}")
print()

# Build ledger on units
y = {r: mpf(0) for r in units}
for pk, p, k in prime_powers:
    r = pk % N
    if r in y:
        y[r] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)

print("Ledger y(r) for unit residues:")
for r in units:
    print(f"  y({r}) = {float(y[r]):.6f}")

# Centering on the unit subgroup
y_bar = sum(y[r] for r in units) / phi_N
y_tilde = {r: y[r] - y_bar for r in units}
print(f"\nMean y_bar = {float(y_bar):.6f}")
print(f"sum y_tilde = {float(sum(y_tilde[r] for r in units)):.2e} (should be ~0)")
print()

# Character coefficients (Euclidean-orthonormal: divide by sqrt(phi_N))
hat_y = {}
for (a, b) in chars:
    chi = dirichlet_char(a, b)
    val = mpc(0, 0)
    for r in units:
        val += y_tilde[r] * mpc(chi(r)).conjugate()
    val /= sqrt(mpf(phi_N))
    hat_y[(a, b)] = val

# Born squares
lambdas = {}
for k in chars:
    lambdas[k] = abs(hat_y[k]) ** 2

# Identify trivial vs non-trivial characters
trivial_char = (0, 0)
nontriv_chars = [c for c in chars if c != trivial_char]

print("Born squared amplitudes lambda_chi:")
for (a, b) in chars:
    marker = " (trivial — should be ~0 after centering)" if (a, b) == trivial_char else ""
    print(f"  chi_({a},{b}): lambda = {float(lambdas[(a,b)]):.6e}{marker}")

trace = sum(lambdas[k] for k in nontriv_chars)
print(f"\nTrace (non-trivial only) = {float(trace):.6e}")

# Power sums (non-trivial only)
power_sums = [sum(lambdas[k] ** (n + 1) for k in nontriv_chars) for n in range(6)]

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
]
ell = [sum(mpf(1) / g ** (2 * (n + 1)) for g in gammas) for n in range(6)]

print()
print(f"Power sums p_n vs ell_{{n+1}} (first 30 zeros):")
print(f"  {'n':>3} {'ell_{n+1}':>16} {'p_n':>16} {'ratio':>12}")
for n in range(6):
    ratio = float(power_sums[n] / ell[n])
    print(f"  {n:>3} {float(ell[n]):>16.4e} {float(power_sums[n]):>16.4e} {ratio:>12.4e}")

print()
print("=== Comparison to additive baseline ===")
additive_p0 = 309.99
mult_p0 = float(power_sums[0])
print(f"Additive baseline p_0 = {additive_p0:.2e}")
print(f"Multiplicative p_0    = {mult_p0:.4e}")
print(f"Improvement (multiplicative vs additive): {additive_p0 / mult_p0:.2f}x")
print(f"Multiplicative p_0/ell_1 ratio: {mult_p0 / float(ell[0]):.4e}")
print()
print("Pre-committed criteria:")
print(f"  Success: >= 100x improvement, p_0 ratio <= 10^2")
print(f"  Failure: <= 10x improvement")
print(f"  Ambiguous: 10-100, iterate")
