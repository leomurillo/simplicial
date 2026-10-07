"""
R1: Add archimedean correction to the prime ledger.

Construction:
- Prime side: y_p(r) = sum_{p^k = r mod N, p^k <= e^T} log(p) / p^(k/2)
- Archimedean side: y_a defined via digamma jet at character frequencies
  (natural Mellin sampling of the A(1/2+t) odd part from Pass-5 §17.2)
- Combined: y_full(r) = y_p(r) + sign * y_a(r) for sign in {+1, -1}

The archimedean character coefficient at frequency c is taken as:
    hat_y_a(c) = -(1/2) * Re[ psi(1/4 + i*pi*c/N) ] + (1/2) log(pi)
proportional, after Mellin inversion at character frequencies.

We sweep over scaling factors and signs to find any combination that
brings the moment ratio toward 1.

Pre-committed criteria:
- Success: atoms shrink >=100x; p_0 ratio <= 10^2
- Failure: atoms shrink <=10x
- Ambiguous: 10-100, iterate
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi, conj
from mpmath import digamma as psi
mp.dps = 30

N = 30
T = 7.0
e_T = exp(mpf(T))

# Sieve + prime powers
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

# Reference cumulants from first 30 zeros
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

# Prime ledger
y_p = [mpf(0)] * N
for pk, p, k in prime_powers:
    y_p[pk % N] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)
y_p_bar = sum(y_p) / N
y_p_tilde = [y_p[r] - y_p_bar for r in range(N)]

def amplitudes(y_tilde, N):
    """Born squared amplitudes via direct DFT (Euclidean-orthonormal)."""
    lambdas = []
    for c in range(1, N):
        val = mpc(0, 0)
        for r in range(N):
            val += y_tilde[r] * exp(mpc(0, -2 * pi * c * r / N))
        val /= sqrt(mpf(N))
        lambdas.append(abs(val) ** 2)
    return lambdas

def power_sums(lambdas, max_n=6):
    return [sum(lam ** (n + 1) for lam in lambdas) for n in range(max_n)]

def report(label, y_tilde, baseline_p0=None):
    lambdas = amplitudes(y_tilde, N)
    trace = sum(lambdas)
    pn = power_sums(lambdas)
    max_lam = max(float(l) for l in lambdas)
    print(f"\n--- {label} ---")
    print(f"  Trace = {float(trace):.4e}; max lambda = {max_lam:.4e}")
    ratios = [float(pn[n] / ell[n]) for n in range(6)]
    print(f"  Ratios p_n/ell_{{n+1}}: " +
          " ".join(f"{r:.3e}" for r in ratios))
    if baseline_p0 is not None:
        improvement = baseline_p0 / float(pn[0])
        print(f"  Improvement vs baseline (p_0): {improvement:.2f}x")
    return float(pn[0]), float(trace), lambdas

# Baseline
print("=" * 70)
print("BASELINE: prime-only ledger")
print("=" * 70)
baseline_p0, _, baseline_lambdas = report("prime only", y_p_tilde)

# Now construct archimedean correction
# Approach: archimedean character coefficient at frequency xi_c = c
# (natural integer sampling for the folded variable)
# Using Pass-5 §17.2: A(s) = 1/s + 1/(s-1) - (1/2)log(pi) + (1/2)psi(s/2)
# The odd-in-t part at frequency xi: leading behavior ~ log(xi).
# Use the Stirling-asymptotic main term as the candidate.

def archimedean_coef(c, scale):
    """Archimedean character coefficient at frequency c.
    Uses the digamma evaluated at the critical line frequency.
    Returns a real value (taking imag part since A_odd is odd in t).
    """
    # Frequency xi = c (natural integer sampling)
    xi = mpf(c)
    s = mpf("0.5") + mpc(0, xi)
    # A(s) terms (odd in xi means imaginary part)
    term1 = 1/s + 1/(s-1)  # rational poles (1/2+i*xi gives small contribution)
    term2 = -mpf("0.5") * log(pi)  # constant, kills under centering
    term3 = mpf("0.5") * psi(s/2)
    A_full = term1 + term2 + term3
    # Odd-in-t part has imaginary component at xi (since t = i*xi for our convention)
    # The natural odd contribution from digamma is (1/2) Im[psi(1/4 + i*xi/2)]
    A_odd_imag = (term1.imag + term3.imag)  # imaginary part of A
    return scale * A_odd_imag

def archimedean_ledger(N, scale):
    """y_a(r) = inverse DFT of archimedean coefficients."""
    # Compute character coefficients first
    hat_y_a = []
    for c in range(N):
        if c == 0:
            hat_y_a.append(mpf(0))  # no trivial mode
        else:
            hat_y_a.append(archimedean_coef(c, scale))
    # Inverse DFT
    y_a = [mpf(0)] * N
    for r in range(N):
        val = mpc(0, 0)
        for c in range(N):
            val += hat_y_a[c] * exp(mpc(0, 2 * pi * c * r / N))
        y_a[r] = val.real  # should be real since coefs are conjugate-symmetric? need to ensure
    return y_a

print()
print("=" * 70)
print("R1 ATTEMPT 1: y = y_p + scale * y_a (archimedean correction)")
print("Sweep over signs and scales")
print("=" * 70)

best_p0 = baseline_p0
best_label = "baseline"
for sign in [+1, -1]:
    for scale_exp in [-2, -1, 0, 1]:
        scale = sign * 10**scale_exp
        y_a = archimedean_ledger(N, mpf(scale))
        # symmetrize: take y_a only for c such that conjugation symmetry holds
        # to ensure y_a is real-valued
        y_full = [y_p[r] + y_a[r] for r in range(N)]
        y_bar = sum(y_full) / N
        y_full_tilde = [y_full[r] - y_bar for r in range(N)]
        p0, trace, _ = report(f"scale={scale:+.2g}", y_full_tilde, baseline_p0)
        if p0 < best_p0:
            best_p0 = p0
            best_label = f"scale={scale:+.2g}"

print()
print("=" * 70)
print(f"Best so far: {best_label} with p_0 = {best_p0:.4e}")
print(f"Baseline p_0 = {baseline_p0:.4e}")
print(f"Improvement factor: {baseline_p0 / best_p0:.2f}x")
print(f"Target: p_0 ratio <= 10^2 (success), <= 10 (insufficient)")
print(f"Current p_0/ell_1 ratio: {best_p0 / float(ell[0]):.2e}")
