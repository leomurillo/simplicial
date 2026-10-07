"""Probe: cross-examination of Conjecture E.7 (BC-ITPFI scaling-weight conjecture).

Three numerical checks, all elementary/deterministic:

(1) TILTED POSITIVE EIGENWEIGHT (the counterexample to E.7 as stated):
    M_sigma(x) = sigma * sum_{n<=x} Lambda(n) n^{sigma-1}.
    Claim: M_sigma(x) ~ x^sigma (PNT-tilt), hence the Banach-limit weight
    phi_tilde_sigma(f) = LIM_x x^{-sigma} * sigma * sum_{n<=x} Lambda(n) n^{sigma-1} f(n)
    is a POSITIVE theta-eigenweight of scaling modulus lambda^{sigma-1/2},
    strictly intermediate for sigma in (1/2, 1).
    Check: M_sigma(2x)/M_sigma(x) -> 2^sigma, and M_sigma(x)/x^sigma -> 1.

(2) STRICT TAIL-SUPPORTEDNESS of the tilt: the finite-block (single-prime p)
    contribution sum_k log p * p^{k(sigma-1)} is a BOUNDED constant (geometric),
    so its fraction of M_sigma(x) ~ x^sigma tends to 0: the tilted weight has
    trivial finite-block marginals exactly like R_rho (support on prime powers).

(3) QUADRATIC LEVEL SEES THE ZEROS / LINEAR CONE DOES NOT:
    V(X) = (1/X) * int_X^{2X} (psi(u)-u)^2 du.
    In the RH-true range (all small zeros on the line) V(X)/X should be
    roughly bounded (exponent of V approx 1 = "2*Theta - 1" with Theta = 1/2),
    while the LINEAR positive sum psi(x) itself is pole-dominated ~ x with the
    zero oscillation strictly subdominant (never threatening positivity).
"""
import numpy as np

N = 10_000_000

# von Mangoldt array via sieve of smallest prime factors
print("sieving up to", N)
lam = np.zeros(N + 1)
is_comp = np.zeros(N + 1, dtype=bool)
for p in range(2, N + 1):
    if not is_comp[p]:
        lp = np.log(p)
        pk = p
        while pk <= N:
            lam[pk] = lp
            pk *= p
        is_comp[2 * p::p] = True

n = np.arange(N + 1, dtype=float)
n[0] = 1.0

# ---- Check 1: tilted mass exponent ----
sigma = 0.75
tilt = lam * n ** (sigma - 1.0)
M = sigma * np.cumsum(tilt)
print("\n[1] tilted eigenweight  sigma =", sigma, "  target ratio 2^sigma =", 2 ** sigma)
for x in [10_000, 100_000, 1_000_000, 5_000_000]:
    print(f"  x={x:>9}:  M(2x)/M(x) = {M[2*x]/M[x]:.5f}   M(x)/x^sigma = {M[x]/x**sigma:.5f}")

# ---- Check 2: finite-block marginal fraction ----
print("\n[2] finite-block (p=2,3,5) mass fraction of M_sigma(x):")
for p in [2, 3, 5]:
    ks = np.arange(1, int(np.log(N) / np.log(p)) + 1)
    block = sigma * np.sum(np.log(p) * (p ** ks.astype(float)) ** (sigma - 1.0))
    print(f"  p={p}: block mass = {block:.4f}  fraction of M(N) = {block/M[N]:.3e}")

# ---- Check 3: variance (quadratic) exponent vs linear pole dominance ----
psi = np.cumsum(lam)
err = psi - n
err[0] = 0.0
print("\n[3] quadratic functional V(X) = (1/X) sum_{X<u<=2X} (psi(u)-u)^2 :")
prev = None
for X in [10_000, 40_000, 160_000, 640_000, 2_560_000]:
    V = np.mean(err[X + 1: 2 * X + 1] ** 2)
    line = f"  X={X:>8}:  V(X) = {V:12.2f}   V(X)/X = {V/X:.5f}"
    if prev is not None:
        line += f"   local exponent = {np.log(V/prev)/np.log(4):.3f}"
    prev = V
    print(line)
print("  (exponent ~ 1 = 2*Theta-1 with Theta=1/2; an off-line zero at Re rho = beta0")
print("   would force local exponent -> 2*beta0 - 1 > 1: un-cancellable Gram diagonal.)")
print("\n[3b] linear pole dominance: max_n |psi(n)-n| / n^(1/2) on dyads (oscillation")
print("     stays O(x^{1/2+eps}) << pole x, so linear positivity is never threatened):")
for X in [100_000, 1_000_000, 5_000_000]:
    w = np.max(np.abs(err[X: 2 * X]) / np.sqrt(n[X: 2 * X]))
    print(f"  X={X:>8}:  max |psi-u|/sqrt(u) = {w:.3f}   vs pole margin sqrt(u) ~ {np.sqrt(X):.0f}")
