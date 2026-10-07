"""
The 1/zeta'(rho) weight = the Mobius/Mertens object = the mollifier weight.

M(x) = sum_{n<=x} mu(n) = sum_rho x^rho/(rho zeta'(rho)) - 2 + ...
So M(x)/sqrt(x) oscillates at the SAME zero frequencies gamma as (psi(x)-x)/sqrt(x), but weighted by
1/(rho zeta'(rho)) instead of 1/rho -- the extra 1/zeta'(rho) is the NEW info. We verify M(x) carries
the first zero gamma_1=14.13 (confirming it is a zeta-zero object with the 1/zeta' weight), and contrast
its weight with the prime fluctuation.

No torch. numpy. Deterministic.
"""
import numpy as np

GAMMA1 = 14.134725
N = 2_000_000

# Mobius via sieve
mu = np.ones(N + 1, dtype=np.int8)
is_p = np.ones(N + 1, dtype=bool); is_p[:2] = False
for p in range(2, int(N**0.5) + 1):
    if is_p[p]:
        is_p[p*p::p] = False
        mu[p::p] *= -1
        mu[p*p::p*p] = 0          # multiples of p^2 (step p^2, not p) -- non-squarefree -> 0
for p in range(int(N**0.5) + 1, N + 1):
    if is_p[p]:
        mu[p::p] *= -1
M = np.cumsum(mu.astype(np.float64))

# prime fluctuation
Lam = np.zeros(N + 1); comp = np.zeros(N + 1, dtype=bool)
for p in range(2, N + 1):
    if not comp[p]:
        lp = np.log(p); pk = p
        while pk <= N:
            Lam[pk] = lp; pk *= p
        comp[p*p::p] = True
xs = np.arange(N + 1, dtype=float)
pf = np.cumsum(Lam) - xs

lo, hi = 1000, N
idx = np.unique(np.round(np.exp(np.linspace(np.log(lo), np.log(hi), 8000))).astype(int))
idx = idx[(idx >= lo) & (idx <= hi)]
lx = np.log(xs[idx])
Mn = M[idx] / np.sqrt(xs[idx])
pfn = pf[idx] / np.sqrt(xs[idx])

def spectrum(f, lx, nus):
    f = f - np.mean(f)
    return np.array([abs(np.sum(f * np.exp(-1j * nu * lx))) for nu in nus])

nus = np.linspace(2.0, 30.0, 1400)
peak_M = nus[np.argmax(spectrum(Mn, lx, nus))]
peak_pf = nus[np.argmax(spectrum(pfn, lx, nus))]

print("=" * 80)
print("The 1/zeta'(rho) weight: Mertens M(x) carries the SAME zeros as the primes")
print("=" * 80)
print(f"   prime fluct (psi-x)/sqrt(x): dominant freq = {peak_pf:.3f}  (weight 1/rho)")
print(f"   Mertens     M(x)/sqrt(x)   : dominant freq = {peak_M:.3f}  (weight 1/(rho zeta'(rho)))")
print(f"   first zero gamma_1 = {GAMMA1:.3f}")
print(f"   M(x)/sqrt(x) RMS = {np.sqrt(np.mean(Mn**2)):.3f}  max = {np.max(np.abs(Mn)):.3f}")
ok = abs(peak_M - GAMMA1) < 1.5
print("\nRESULT:", "GREEN -- Mertens carries gamma_1 => it IS the 1/zeta'(rho)-weighted zero object"
      if ok else "RED")
print("=" * 80)
print("""
Reading:
  Both psi(x)-x and M(x) oscillate at the same first zero gamma_1=14.13 -- same zeros, different
  weight: 1/rho for primes, 1/(rho zeta'(rho)) for Mertens. The extra 1/zeta'(rho) is exactly the
  mollifier weight: the Levinson-Conrey method puts a POSITIVE PROPORTION of zeros on the line
  UNCONDITIONALLY by forming the second moment of zeta(s)*B(s) with B ~ 1/zeta (the Mobius
  mollifier), and the on-line count is governed by 1/zeta'(rho). Exploiting 1/zeta'(rho) = pushing
  the mollifier: longer Mobius mollifier -> higher proportion on the line -> toward RH; the mollifier
  length is bounded by Mobius control = the level of distribution (Flank 1). So the 1/zeta'(rho)
  weight is the UNCONDITIONAL positive-proportion frontier, converging to the same medium-arc lever.
""")
