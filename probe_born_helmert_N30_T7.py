"""
Born-Helmert numerical probe at N = 30, T = 7.

Tests the Pass-5 Theorem 19.1 candidate ledger:
    y(r) = sum_{p^k = r mod N, p^k <= e^T} log(p) / p^(k/2)
on the centered primorial ledger over Z/30, computes squared character
amplitudes lambda_c = |y_hat_c|^2, and reports power sums for comparison
to folded xi cumulants ell_{n+1} = sum_k gamma_k^{-2(n+1)}.

Outputs:
  - ledger y(r) for r = 0..29
  - Helmert coordinates <y, e_k> for k = 1..29
  - character coefficients y_hat_c for c = 1..29
  - cross-check: transfer-matrix formula vs direct DFT
  - squared amplitudes lambda_c
  - power sums p_n for n = 0..10
  - comparison to ell_{n+1} from first 50 known Riemann zeros
"""

from mpmath import mp, mpf, mpc, exp, log, sqrt, pi, zeta, conj
from cmath import exp as cexp

mp.dps = 40  # 40 digit precision

N = 30
T = 7.0
e_T = exp(mpf(T))

# ----------------------------------------------------------------------
# Step 1. Enumerate primes and prime powers <= e^T
# ----------------------------------------------------------------------
def sieve(n):
    sieve_arr = [True] * (n + 1)
    sieve_arr[0] = sieve_arr[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve_arr[i]:
            for j in range(i*i, n+1, i):
                sieve_arr[j] = False
    return [i for i, v in enumerate(sieve_arr) if v]

primes = sieve(int(float(e_T)) + 1)
prime_powers = []  # (p^k, p, k)
for p in primes:
    pk = p
    k = 1
    while pk <= float(e_T):
        prime_powers.append((pk, p, k))
        pk *= p
        k += 1

print(f"=== Born-Helmert Probe at N = {N}, T = {T} ===")
print(f"e^T = {float(e_T):.4f}")
print(f"Primes p <= e^T: {len(primes)} (up to p = {primes[-1]})")
print(f"Prime powers p^k <= e^T: {len(prime_powers)}")
print()

# ----------------------------------------------------------------------
# Step 2. Build ledger y(r) = sum_{p^k = r mod N} log(p) / p^(k/2)
# ----------------------------------------------------------------------
y = [mpf(0) for _ in range(N)]
for pk, p, k in prime_powers:
    r = pk % N
    y[r] += log(mpf(p)) / mpf(p) ** (mpf(k) / 2)

# Center: tilde y(r) = y(r) - bar y
y_bar = sum(y) / N
y_tilde = [y[r] - y_bar for r in range(N)]

print("Ledger y(r) and centered y_tilde(r):")
print(f"  {'r':>3} {'y(r)':>16} {'y_tilde(r)':>18}")
for r in range(N):
    print(f"  {r:>3} {float(y[r]):>16.8f} {float(y_tilde[r]):>18.8f}")
print(f"  mean y_bar = {float(y_bar):.8f}")
print(f"  sum y_tilde = {float(sum(y_tilde)):.2e} (should be ~0)")
print()

# ----------------------------------------------------------------------
# Step 3. Compute Helmert coordinates <y_tilde, e_k>
# ----------------------------------------------------------------------
def helmert_coord(y_vec, k, N):
    """Inner product <y_vec, e_k> where e_k = h_k / sqrt(k(k+1))."""
    # h_k = (1, 1, ..., 1, -k, 0, ..., 0) with first k entries = 1, (k+1)-th = -k
    s = mpf(0)
    for i in range(k):
        s += y_vec[i]
    s -= mpf(k) * y_vec[k]
    return s / sqrt(mpf(k) * (k + 1))

helmert_coords = [helmert_coord(y_tilde, k, N) for k in range(1, N)]

# ----------------------------------------------------------------------
# Step 4. Compute character coefficients y_hat_c via direct DFT
#         y_hat_c = (1/N) sum_r y_tilde(r) e^{-2 pi i c r / N}
# (Normalized so the orthonormal characters are tilde chi_c = chi_c / sqrt(N),
#  but |y_hat_c|^2 here equals (1/N) * |<y_tilde, chi_c>_Euclidean|^2; we
#  rescale below to match the transfer-matrix Born convention.)
# ----------------------------------------------------------------------

def char_coef_dft(y_vec, c, N):
    """y_hat_c = (1/N) sum_r y_vec(r) exp(-2 pi i c r / N)."""
    val = mpc(0, 0)
    for r in range(N):
        val += y_vec[r] * exp(mpc(0, -2 * pi * c * r / N))
    return val / N

y_hat_dft = [char_coef_dft(y_tilde, c, N) for c in range(1, N)]

# Born convention from T4-Helmert-Fourier doc: amplitudes are taken w.r.t.
# Euclidean-orthonormal characters tilde chi_c = chi_c / sqrt(N).
# Relation: <y, tilde chi_c>_Euclidean = sqrt(N) * y_hat_c (the DFT version).
# So the "Born amplitude" is sqrt(N) * y_hat_c.
y_hat_born = [sqrt(mpf(N)) * yh for yh in y_hat_dft]

# ----------------------------------------------------------------------
# Step 5. Cross-check via transfer matrix
#         <y, tilde chi_c> = sum_k T_{c,k} <y, e_k>
# ----------------------------------------------------------------------
def transfer_T(c, k, N):
    """T_{c,k} = (1/sqrt(N k (k+1))) * [sum_{s=0}^{k-1} omega_c^s - k omega_c^k]"""
    omega = exp(mpc(0, 2 * pi * c / N))
    geom = mpc(0, 0)
    pw = mpc(1, 0)
    for s in range(k):
        geom += pw
        pw *= omega
    # pw is now omega^k
    bracket = geom - mpf(k) * pw
    return bracket / sqrt(mpf(N) * k * (k + 1))

# Compute y_hat_born via transfer matrix:
y_hat_via_T = []
for c in range(1, N):
    val = mpc(0, 0)
    for k in range(1, N):
        # Correct change-of-basis: alpha_c = sum_k conj(T_{c,k}) * beta_k
        # because <y, tilde_chi_c> = sum_k beta_k <e_k, tilde_chi_c> = sum_k beta_k conj(T_{c,k})
        val += conj(transfer_T(c, k, N)) * helmert_coords[k - 1]
    y_hat_via_T.append(val)

# Cross-check
print("Cross-check: direct DFT vs transfer-matrix formula")
print(f"  {'c':>3} {'|y_hat_born|':>20} {'|y_hat_via_T|':>20} {'diff':>14}")
max_diff = mpf(0)
for c in range(1, 6):  # first 5 only
    a = abs(y_hat_born[c - 1])
    b = abs(y_hat_via_T[c - 1])
    d = abs(a - b)
    if d > max_diff:
        max_diff = d
    print(f"  {c:>3} {float(a):>20.10e} {float(b):>20.10e} {float(d):>14.2e}")
# Total max diff across all c:
for c in range(1, N):
    d = abs(y_hat_born[c - 1] - y_hat_via_T[c - 1])
    if d > max_diff:
        max_diff = d
print(f"  Max |diff| across all c = 1..{N-1}: {float(max_diff):.2e}")
print()

# ----------------------------------------------------------------------
# Step 6. Born squared amplitudes lambda_c = |y_hat_born|^2
# ----------------------------------------------------------------------
lambdas = [abs(yh) ** 2 for yh in y_hat_born]
trace = sum(lambdas)
print(f"Born squared amplitudes lambda_c = |y_hat_born_c|^2:")
print(f"  {'c':>3} {'lambda_c':>18}")
for c, lam in enumerate(lambdas, start=1):
    print(f"  {c:>3} {float(lam):>18.10e}")
print(f"  Trace = sum lambda_c = {float(trace):.10e}")
print()

# ----------------------------------------------------------------------
# Step 7. Power sums p_n = sum_c lambda_c^(n+1)
# ----------------------------------------------------------------------
power_sums = []
for n in range(11):
    p_n = sum(lam ** (n + 1) for lam in lambdas)
    power_sums.append(p_n)

print(f"Power sums p_n = sum_c lambda_c^(n+1):")
print(f"  {'n':>3} {'p_n':>22}")
for n, p in enumerate(power_sums):
    print(f"  {n:>3} {float(p):>22.10e}")
print()

# ----------------------------------------------------------------------
# Step 8. Compare to ell_{n+1} = sum_k gamma_k^{-2(n+1)} from known zeros
# ----------------------------------------------------------------------
# First 50 Riemann zeros (imaginary parts) to ~10 digits
gammas = [
    mpf("14.134725141734693790"),
    mpf("21.022039638771554993"),
    mpf("25.010857580145688763"),
    mpf("30.424876125859513210"),
    mpf("32.935061587739189691"),
    mpf("37.586178158825671257"),
    mpf("40.918719012147495187"),
    mpf("43.327073280914999519"),
    mpf("48.005150881167159728"),
    mpf("49.773832477672302182"),
    mpf("52.970321477714460644"),
    mpf("56.446247697063394804"),
    mpf("59.347044002602353079"),
    mpf("60.831778524609809844"),
    mpf("65.112544048081606660"),
    mpf("67.079810529494173714"),
    mpf("69.546401711173979253"),
    mpf("72.067157674481907583"),
    mpf("75.704690699083933168"),
    mpf("77.144840068874805373"),
    mpf("79.337375020249367922"),
    mpf("82.910380854086030183"),
    mpf("84.735492980517050106"),
    mpf("87.425274613125229407"),
    mpf("88.809111207634465423"),
    mpf("92.491899270558484296"),
    mpf("94.651344040519886967"),
    mpf("95.870634228245309831"),
    mpf("98.831194218193198281"),
    mpf("101.317851005731391228"),
    mpf("103.725538040478339416"),
    mpf("105.446623052087647076"),
    mpf("107.168611184276407515"),
    mpf("111.029535543018306543"),
    mpf("111.874659177002948212"),
    mpf("114.320220915452712780"),
    mpf("116.226680320857554382"),
    mpf("118.790782866263209222"),
    mpf("121.370125002420645918"),
    mpf("122.946829294678492525"),
    mpf("124.256818554345767565"),
    mpf("127.516683879596495124"),
    mpf("129.578704199956050985"),
    mpf("131.087688530932656723"),
    mpf("133.497737203718394113"),
    mpf("134.756509753373871136"),
    mpf("138.116042054533443200"),
    mpf("139.736208952121388017"),
    mpf("141.123707404021123761"),
    mpf("143.111845807895079352"),
]

ell = []  # ell[m] = ell_{m+1} for m = 0..10
for n in range(11):
    m = n + 1
    s = sum(mpf(1) / g ** (2 * m) for g in gammas)
    ell.append(s)

print(f"Cumulants ell_{{n+1}} = sum_k gamma_k^{{-2(n+1)}} from first {len(gammas)} zeros:")
print(f"  (Note: ell_1 converges slowly; higher ell_m converge fast.)")
print(f"  {'n':>3} {'ell_{n+1}':>22} {'p_n':>22} {'ratio p_n/ell':>16}")
for n in range(11):
    ratio = float(power_sums[n] / ell[n]) if ell[n] != 0 else float('nan')
    print(f"  {n:>3} {float(ell[n]):>22.10e} {float(power_sums[n]):>22.10e} {ratio:>16.6f}")

print()
print("=== Interpretation ===")
print("The 'prime sum' candidate ledger captures only the prime-side")
print("contribution. The full ell_{n+1} = ell_end + ell_arch + ell_zeta.")
print("The ratio p_n / ell_{n+1} indicates how much of the total cumulant")
print("the prime-only ledger captures. Deviations from 1 reveal the")
print("missing archimedean (Gamma) and endpoint pieces.")
