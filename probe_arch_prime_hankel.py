"""
Numerical probe: archimedean vs prime contribution to Apex Hankel matrices.

Test whether H_n^arch (archimedean-only cumulants) dominates with positive margin,
so H_n^prime as a "correction" can't break overall positivity (Bombieri-Lagarias hope).

Setup (Pass-5 §17.2):
  F(x) = (1/(2 sqrt(x))) * xi'/xi(1/2 + sqrt(x))
  xi'/xi(s) = A(s) + P(s)
    A(s) = 1/s + 1/(s-1) - (log pi)/2 + (1/2) psi(s/2)    (archimedean)
    P(s) = zeta'/zeta(s)                                  (prime)

  mu_k = (-1)^k * coef_{2k+1}/2  where coef_n = G^{(n)}(1/2)/n!

Fast computation strategy:
  - A: closed-form Taylor coefficients at s=1/2 (poles + polygamma series).
  - P: logarithmic-derivative recurrence
       P^{(n)}(s) = [zeta^{(n+1)}(s) - sum_{k=1}^{n-1} C(n-1,k) zeta^{(k)}(s) P^{(n-k)}(s)] / zeta(s)
     ... wait this won't work directly. Use Faa di Bruno or compute log(zeta) derivatives.

Actually the cleanest: P^{(n)}(s) = (d/ds)^n [zeta'/zeta] = (d/ds)^{n+1} log zeta.
Use the recurrence: zeta * P = zeta', so (d/ds)^n [zeta * P] = zeta^{(n+1)}.
By Leibniz: sum_{k=0}^n C(n,k) zeta^{(k)}(s) P^{(n-k)}(s) = zeta^{(n+1)}(s).
Isolate k=0: zeta(s) P^{(n)}(s) = zeta^{(n+1)}(s) - sum_{k=1}^n C(n,k) zeta^{(k)}(s) P^{(n-k)}(s).
P^{(n)}(s) = [zeta^{(n+1)}(s) - sum_{k=1}^n C(n,k) zeta^{(k)}(s) P^{(n-k)}(s)] / zeta(s).

This requires zeta^{(k)}(1/2) for k = 0, 1, ..., N+1, which mpmath gives in closed form.
"""

import sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, zeta, log, pi, matrix, binomial, factorial

mp.dps = 250   # need high precision: arch & prime cancel by ~80 digits at k=30

N_TAYLOR = 70   # need 2k+1 up to ~61 for mu_k through k=30
N_PROBE = 30

print("=" * 78)
print(" Archimedean vs prime contribution to Apex Hankel matrices")
print("=" * 78)
print(f" mpmath dps = {mp.dps}, N_taylor = {N_TAYLOR}, N_probe = {N_PROBE}")
print()

# -------------------- A(s) closed-form Taylor coefficients --------------------

# Pole pieces: 1/s + 1/(s-1) at s = 1/2 + t.
# 1/s = 1/(1/2 + t) = sum_n (-1)^n 2^{n+1} t^n
# 1/(s-1) = 1/(t - 1/2) = -sum_n 2^{n+1} t^n
# Sum: sum_n [(-1)^n - 1] 2^{n+1} t^n = -sum_{n odd} 2^{n+2} t^n  (0 for n even)

# psi(s/2)/2 at s = 1/2 + t:  psi(1/4 + t/2)/2
# Taylor coef of t^n: psi^{(n)}(1/4)/(n! * 2^{n+1})
# psi^{(n)}(s) for n >= 1: = (-1)^{n+1} n! zeta(n+1, s)  where zeta(s,a) is Hurwitz
# So coef of t^n in psi(s/2)/2 = (-1)^{n+1} zeta(n+1, 1/4) / 2^{n+1}  for n >= 1
# Constant (n=0): psi(1/4)/2

# Const piece: -log(pi)/2 contributes only to n=0.

# Total a_n for n >= 1:
#   n even:  0 (pole)  + (-1)^{n+1} zeta(n+1, 1/4)/2^{n+1} = -zeta(n+1, 1/4)/2^{n+1}
#   n odd:   -2^{n+2}  + (-1)^{n+1} zeta(n+1, 1/4)/2^{n+1} = -2^{n+2} + zeta(n+1, 1/4)/2^{n+1}

def coef_A(n):
    """Coefficient of t^n in Taylor expansion of A(1/2 + t)."""
    n = int(n)
    if n == 0:
        # psi(1/4)/2 - log(pi)/2 + (1/(1/2)) + (1/(-1/2))  -- pole values at t=0
        # 1/(1/2) = 2, 1/(-1/2) = -2, so pole sum = 0.
        from mpmath import digamma
        return digamma(mpf(1)/4)/2 - log(pi)/2
    # n >= 1
    pole = -mpf(2)**(n+2) if (n % 2 == 1) else mpf(0)
    psi_part = (-1)**(n+1) * zeta(n+1, mpf(1)/4) / mpf(2)**(n+1)
    return pole + psi_part

print("Computing A(s) Taylor coefficients (closed form)...")
t0 = time.time()
coefs_A = [coef_A(n) for n in range(N_TAYLOR)]
print(f"  Done in {time.time()-t0:.1f}s")

# -------------------- P(s) via logarithmic-derivative recurrence --------------------

# P^{(n)}(1/2) = [zeta^{(n+1)}(1/2) - sum_{k=1}^n C(n,k) zeta^{(k)}(1/2) P^{(n-k)}(1/2)] / zeta(1/2)

# Precompute zeta^{(k)}(1/2) for k = 0, ..., N_TAYLOR
print("Computing zeta^{(k)}(1/2) for k = 0..N_TAYLOR ...")
t0 = time.time()
zeta_derivs = [zeta(mpf(1)/2, derivative=k) for k in range(N_TAYLOR + 1)]
print(f"  Done in {time.time()-t0:.1f}s")
print(f"  zeta(1/2) = {mp.nstr(zeta_derivs[0], 10)}")
print(f"  zeta'(1/2) = {mp.nstr(zeta_derivs[1], 10)}")

# Now compute P^{(n)}(1/2) recursively
# P^{(0)}(1/2) = zeta'/zeta(1/2)
print("Computing P^{(n)}(1/2) via log-derivative recurrence...")
t0 = time.time()
P_derivs = [zeta_derivs[1] / zeta_derivs[0]]  # P^{(0)} = zeta'/zeta
for n in range(1, N_TAYLOR):
    # P^{(n)}(1/2) = [zeta^{(n+1)}(1/2) - sum_{k=1}^n C(n,k) zeta^{(k)}(1/2) P^{(n-k)}(1/2)] / zeta(1/2)
    s = zeta_derivs[n+1]
    for k in range(1, n+1):
        s -= binomial(n, k) * zeta_derivs[k] * P_derivs[n-k]
    P_derivs.append(s / zeta_derivs[0])
print(f"  Done in {time.time()-t0:.1f}s")

# Taylor coefficients of P at s=1/2: coef_P(n) = P^{(n)}(1/2)/n!
coefs_P = [P_derivs[n] / factorial(n) for n in range(N_TAYLOR)]

# Sanity: A(1/2) + P(1/2) should equal G(1/2) = xi'/xi(1/2) = 0 (by symmetry).
g0 = coefs_A[0] + coefs_P[0]
print(f"  Sanity: A(1/2) + P(1/2) = {mp.nstr(g0, 6)} (should be ~0)")

# -------------------- Extract mu_k --------------------

def to_mu(coefs, K):
    return [(-1)**k * coefs[2*k+1] / 2 for k in range(K)]

K_max = N_PROBE + 1
mu_arch = to_mu(coefs_A, K_max)
mu_prime = to_mu(coefs_P, K_max)
mu_total = [a + p for a, p in zip(mu_arch, mu_prime)]

# Sanity: mu_0 ~ 0.0231 (sum 1/gamma^2)
print()
print(f"mu_0 = {mp.nstr(mu_total[0], 14)} (expected ~0.0231)")
print(f"mu_0^arch  = {mp.nstr(mu_arch[0], 14)}")
print(f"mu_0^prime = {mp.nstr(mu_prime[0], 14)}")

# ============================================================
# Cumulant table
# ============================================================
print()
print("=" * 78)
print(" Cumulant decomposition mu_k = mu_k^arch + mu_k^prime")
print("=" * 78)
print(f"  {'k':>3} {'mu_k^arch':>22} {'mu_k^prime':>22} {'mu_k (sum)':>22}")
print("  " + "-" * 71)
for k in [0, 1, 2, 3, 4, 5, 8, 10, 15, 20, 25, 30]:
    if k >= K_max: break
    print(f"  {k:>3} {mp.nstr(mu_arch[k], 6):>22} {mp.nstr(mu_prime[k], 6):>22} "
          f"{mp.nstr(mu_total[k], 6):>22}")

def sign_pattern(seq, K):
    return "".join("+" if seq[k] > 0 else ("-" if seq[k] < 0 else "0") for k in range(K))

print()
K_show = min(N_PROBE + 1, K_max)
print(f"Sign patterns (k=0..{K_show-1}):")
print(f"  mu_k^arch : {sign_pattern(mu_arch, K_show)}")
print(f"  mu_k^prime: {sign_pattern(mu_prime, K_show)}")
print(f"  mu_k      : {sign_pattern(mu_total, K_show)}")

print()
print("Cancellation magnitude |mu_k| / max(|arch|,|prime|):")
print(f"  {'k':>3} {'|mu_k|':>16} {'max indiv':>16} {'ratio':>16}")
for k in [0, 1, 2, 5, 10, 20, 30]:
    if k >= K_max: break
    a, p, m = abs(mu_arch[k]), abs(mu_prime[k]), abs(mu_total[k])
    ratio = m / max(a, p) if max(a, p) > 0 else mpf(0)
    print(f"  {k:>3} {mp.nstr(m, 6):>16} {mp.nstr(max(a,p), 6):>16} {mp.nstr(ratio, 6):>16}")

# ============================================================
# Hankel positivity test on each component
# ============================================================
def ldl(M):
    n = M.rows
    A_ = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A_[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A_[k, k]
        diags.append(d)
        if d <= 0:
            return False, k, diags
        for i in range(k+1, n):
            f = A_[i, k] / d
            for j in range(k+1, n):
                A_[i, j] -= f * A_[k, j]
    return True, n, diags

def hankel(seq, n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j]
    return M

n_max_hankel = (K_max - 1) // 2
print()
print("=" * 78)
print(" Hankel positivity: arch-only vs prime-only vs total")
print("=" * 78)
print(f"  {'n':>3}  {'arch':>6} {'prime':>6} {'total':>6}   "
      f"{'arch_minD':>14} {'prime_minD':>14} {'total_minD':>14}")
print("  " + "-" * 88)

for n in list(range(0, 11)) + [12, 14, 15]:
    if 2*n >= K_max:
        break
    Ha = hankel(mu_arch, n)
    Hp = hankel(mu_prime, n)
    Ht = hankel(mu_total, n)
    pa, _, da = ldl(Ha); pp, _, dp = ldl(Hp); pt, _, dt = ldl(Ht)
    sa = "PSD" if pa else "FAIL"
    sp = "PSD" if pp else "FAIL"
    st = "PSD" if pt else "FAIL"
    print(f"  {n:>3}  {sa:>6} {sp:>6} {st:>6}   "
          f"{mp.nstr(min(da), 4):>14} {mp.nstr(min(dp), 4):>14} {mp.nstr(min(dt), 4):>14}")

print()
print("=" * 78)
print(" Diagnostic")
print("=" * 78)
print()
print("Q1. Sign of mu_0^arch, mu_0^prime?")
print(f"    mu_0^arch  = {mp.nstr(mu_arch[0], 6)}    "
      f"({'pos' if mu_arch[0] > 0 else 'NEG'})")
print(f"    mu_0^prime = {mp.nstr(mu_prime[0], 6)}    "
      f"({'pos' if mu_prime[0] > 0 else 'NEG'})")
print(f"    Bombieri-Lagarias hope (arch > 0 dominantly): "
      f"{'TRUE' if mu_arch[0] > abs(mu_prime[0]) else 'FALSE'}")
print()
print("Q2. Is (mu_k^arch)_k a positive Hankel sequence at sampled n?")
print("    See arch column in Hankel test above.")
print()
print("Q3. Cancellation tightness at k=0:")
ratio_0 = abs(mu_total[0]) / max(abs(mu_arch[0]), abs(mu_prime[0]))
print(f"    |mu_0|/max(|arch|,|prime|) = {mp.nstr(ratio_0, 4)}")
print(f"    (Small => tight cancellation => analytical bound must be precise.)")
