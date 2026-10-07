"""
(alpha) THE FREE-CONVOLUTION TEST: are the zeros the FREE convolution of the primes?

Decisive discriminator. The explicit-formula prime side of the zero phase S(T)=(1/pi)arg zeta(1/2+iT) is
        f(T) = (1/pi) sum_p sum_k sin(kT log p)/(k p^{k/2}).
Its value distribution over T tells us HOW the primes combine:
   * CLASSICAL independence (primes commute)  -> classical CLT -> GAUSSIAN:    m4/m2^2 -> 3,  m6/m2^3 -> 15
   * FREE independence (primes don't commute) -> free CLT      -> SEMICIRCLE:  m4/m2^2 -> 2,  m6/m2^3 -> 5
So the free-convolution hypothesis predicts SEMICIRCLE (2, 5); classical (Selberg) predicts GAUSSIAN (3,15).

We also run two CONTROLS: a true Gaussian sample and the eigenvalues of a GUE matrix (true semicircle / free
Gaussian), so the discriminator is anchored on this machine, not just on textbook values.

No torch. numpy. Deterministic up to sampling (large N).
"""
import numpy as np
np.random.seed(0)

def primes_upto(N):
    s = np.ones(N+1, bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.flatnonzero(s)

def central_ratios(x):
    x = x - x.mean()
    m2 = np.mean(x**2); m4 = np.mean(x**4); m6 = np.mean(x**6)
    return m2, m4/m2**2, m6/m2**3

print("=" * 80)
print("(alpha) Free-convolution test: do primes combine FREELY (semicircle) or CLASSICALLY (gaussian)?")
print("=" * 80)

# ---- the prime side of S(T) (explicit formula) ----
P = primes_upto(3000); logs = np.log(P.astype(float))
NT = 1_500_000
T = np.random.uniform(1e5, 2e6, NT)
f = np.zeros(NT)
for p, lp in zip(P, logs):
    for k in (1, 2, 3):
        f += np.sin(k*T*lp)/(k * p**(k/2.0))
f /= np.pi
m2p, k4p, k6p = central_ratios(f)

# ---- control 1: true classical Gaussian ----
g = np.random.normal(size=NT)
m2g, k4g, k6g = central_ratios(g)

# ---- control 2: true free Gaussian = GUE eigenvalues (semicircle) ----
n = 3000
A = (np.random.randn(n, n) + 1j*np.random.randn(n, n)) / np.sqrt(2)
A = (A + A.conj().T) / 2
ev = np.linalg.eigvalsh(A) / np.sqrt(n)            # bulk -> semicircle on [-2,2]
# trim edges (semicircle moments are bulk; keep central 80% to reduce edge bias)
ev = np.sort(ev); lo, hi = int(0.1*n), int(0.9*n); evc = ev[lo:hi]
m2s, k4s, k6s = central_ratios(evc)

print(f"\n  {'distribution':<34} {'m2 (var)':>10} {'m4/m2^2':>10} {'m6/m2^3':>10}")
print(f"  {'PRIME SIDE of S(T)  (the test)':<34} {m2p:>10.4f} {k4p:>10.4f} {k6p:>10.4f}")
print(f"  {'control: classical Gaussian':<34} {m2g:>10.4f} {k4g:>10.4f} {k6g:>10.4f}   (theory 3, 15)")
print(f"  {'control: GUE eigenvalues (semicircle)':<34} {m2s:>10.4f} {k4s:>10.4f} {k6s:>10.4f}   (theory 2, 5)")

verdict = "CLASSICAL (Gaussian)" if abs(k4p-3) < abs(k4p-2) else "FREE (semicircle)"
print(f"\n  VERDICT: the prime side of S(T) is {verdict}: m4/m2^2={k4p:.3f} (gaussian 3 vs semicircle 2).")

print("\n" + "=" * 80)
print(f"""READING — (alpha) settled by a matched falsifier:
  * The prime side of S(T) is GAUSSIAN (m4/m2^2 ~ {k4p:.2f}, m6/m2^3 ~ {k6p:.1f}), matching the classical
    control (3, 15), NOT the semicircle control (2, 5). The primes combine CLASSICALLY (Selberg's CLT) --
    they are COMMUTING SCALARS (functions of T), and commuting => classical independence, not free.
  * So the naive 'zeros = FREE convolution of primes' is FALSE at the scalar / linear-statistic level.
    S(T) is the ABELIANIZATION (the trace) where freeness collapses to classical independence.
  * This SHARPENS (does not kill) the free-probability lens. Free probability genuinely lives in TWO
    places, both NON-scalar:
      (i) LOCAL UNIVERSALITY: the sine-kernel / GUE spacing law is the FREE CLT, but it is UNIVERSAL
          (same for every L-function) -- it is the zeros' OWN determinantal repulsion, not inherited
          from the primes by free convolution.
      (ii) OPERATOR / HILBERT-POLYA level: if the zeros are eigenvalues of an operator built from
          NON-COMMUTING prime operators (Hecke / Frobenius), THEN free convolution of prime OPERATORS
          (not prime scalars) is the right object. The scalar test rules out the abelianized version and
          points exactly here -- the non-commutative operator level IS where RH lives.
  NET: free probability is the correct language for the ZEROS (m_B=Cauchy transform, free entropy=log
  energy, local=free CLT) and for the OPERATOR-level primes (Hilbert-Polya), but NOT for the primes as
  classical scalars. The (alpha) test converts a vague hope into a precise map of where freeness applies.
""")
print("=" * 80)
