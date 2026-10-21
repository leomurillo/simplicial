"""The dyadic ladder (Paper 53 §4.9): Castelnuovo–Severi over Q, with the prime 2 as the zoom gauge.

Packet f(x) = e^{x} 1_[0, log 2] (and its modulation f_w = e^{iwx} f); g = f * f~ is supported on [-log 2, log 2].
Weil Gram of the zooms tau_{m log 2} f, m = 0..N-1, is the Hermitian Toeplitz matrix T_N = [c_{j-k}] with
    c_0 = q_w   (archimedean only: the packet sits below the first prime),    c_m = K_w(m log 2)   (m >= 1).
RH => every T_N is positive semidefinite (Bochner on the zero side), i.e. every reflection coefficient kappa_k of
the Levinson–Szegő ladder satisfies |kappa_k| < 1: each rung is a passive 2-port.
zeta: c_m from primes (Lower-bound note eq. 8 / Ledger eq. 7). DH: c_m from its zeros (on-line ones to height 180
by sign changes, plus the four certified off-line quadruples of N7 §5.5).
"""
import numpy as np
import mpmath as mp

A_LOG2 = np.log(2.0)


def G(z):
    z = np.asarray(z, dtype=complex)
    return (5 - 4 * np.cosh(A_LOG2 * z)) / (1 - z * z)


def lambda_vm(N):
    sieve = np.ones(N + 1, bool); sieve[:2] = False
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(N + 1)
    for p in np.nonzero(sieve)[0]:
        pk = int(p)
        while pk <= N:
            lam[pk] = np.log(p); pk *= int(p)
    return lam


def g_fun(v):
    v = np.abs(v)
    return np.where(v <= A_LOG2, 2 * np.exp(-v) - 0.5 * np.exp(v), 0.0)


def q_w(w):
    """Q(f_w) = K_w(0): Ledger eq. (8), archimedean + pole only."""
    mp.mp.dps = 30
    a = mp.log(2)
    Gw = lambda z: (5 - 4 * mp.cosh(a * z)) / (1 - z * z)
    integ = mp.quad(lambda v: (mp.exp(v / 2) * (2 * mp.exp(-v) - mp.exp(v) / 2) * mp.cos(w * v) - mp.mpf(3) / 2)
                    / mp.sinh(v), [0, a])
    return float(2 * mp.re(Gw(mp.mpf(1) / 2 - 1j * w)) - mp.mpf(3) / 2 * (mp.euler + mp.log(4 * mp.pi)
                                                                      + mp.log(mp.tanh(a / 2))) - integ)


def K_prime(w, X, lam):
    """K_w(log X) = sqrt(X) G(1/2 - i w) - P_w(X) - D_w(X), X >= 2 (continuous at X = 2)."""
    n = np.arange(int(np.ceil(X / 2)), int(np.floor(2 * X)) + 1)
    v = np.log(n / X)
    P = np.sum(lam[n] / np.sqrt(n) * g_fun(v) * np.exp(-1j * w * v))
    mp.mp.dps = 20
    D = complex(mp.mpf(X) ** -2.5 * mp.quad(lambda u: (2 * mp.exp(-abs(u)) - mp.exp(abs(u)) / 2) * mp.exp((2.5 + 1j * w) * u)
                                            / (1 - mp.mpf(X) ** -2 * mp.exp(2 * u)), [-mp.log(2), 0, mp.log(2)]))
    return np.sqrt(X) * complex(G(0.5 - 1j * w)) - P - D


def ladder(c):
    """Hermitian Toeplitz T_N from c_0..c_{N-1}; returns min eigenvalue / c_0 and reflection-coefficient moduli."""
    N = len(c)
    T = np.array([[c[j - k] if j >= k else np.conj(c[k - j]) for k in range(N)] for j in range(N)])
    lmin = np.linalg.eigvalsh(T)[0].real / c[0].real
    logdet = [0.0] + [np.linalg.slogdet(T[:k, :k])[1] if np.linalg.slogdet(T[:k, :k])[0].real > 0 else np.nan
                      for k in range(1, N + 1)]
    E = np.exp(np.diff(logdet))                      # prediction errors E_0 = c_0, E_k = D_{k+1}/D_k
    kappa = np.sqrt(np.clip(1 - E[1:] / E[:-1], 0, None))
    return lmin, kappa, E / E[0]


def dh_zeros():
    from p53_third_law_curve import true_dh_online
    on = true_dh_online(0.5, 180.0, dt=0.01)
    off = [0.808517 + 85.699348j, 0.650830 + 114.163343j, 0.574356 + 166.479306j, 0.724258 + 176.702461j]
    z = [1j * g for g in on] + [-1j * g for g in on]
    for r in off:
        d, g = r.real - 0.5, r.imag
        z += [d + 1j * g, -d + 1j * g, d - 1j * g, -d - 1j * g]
    return np.array(z), len(on)


if __name__ == "__main__":
    M = 23
    lam = lambda_vm(2 ** (M + 1) + 2)
    gam = np.sort(np.load(r"C:\Projects\simplicial\empirical\zeros_cache.npy").real)
    zz = np.concatenate([1j * gam, -1j * gam])
    for w in (0.0, 14.134725, 85.699348):
        c = np.array([q_w(w)] + [K_prime(w, 2.0 ** m, lam) for m in range(1, M)])
        cz = np.array([np.sum(G(zz - 1j * w) * np.exp(zz * m * A_LOG2)) for m in range(M)])
        lmin, kap, E = ladder(c)
        print(f"zeta, w = {w:9.6f}: c_0 = {c[0].real:.6f} | max|c_m|/c_0 = {np.max(np.abs(c[1:])) / c[0].real:.4f}"
              f" | prime side vs 250-zero side, max |diff| = {np.max(np.abs(c - cz)):.4f}")
        print(f"     lambda_min(T_{M})/c_0 = {lmin:.3e} | max |kappa_k| = {np.nanmax(kap):.4f}"
              f" | prediction error E_k/c_0 at k = 1, 5, 10, 22: {E[1]:.3f} {E[5]:.3f} {E[10]:.3f} {E[22]:.3e}")
        print("     |kappa_k|:", " ".join(f"{x:.3f}" for x in kap), flush=True)
    z, n_on = dh_zeros()
    print(f"\nDH zero side: {n_on} on-line ordinates in (0.5, 180) + 4 off-line quadruples")
    for w in (0.0, 85.699348):
        c = np.array([np.sum(G(z - 1j * w) * np.exp(z * m * A_LOG2)) for m in range(M)])
        first_bad = next((N for N in range(2, M + 1) if np.linalg.eigvalsh(
            np.array([[c[j - k] if j >= k else np.conj(c[k - j]) for k in range(N)] for j in range(N)]))[0].real < 0), None)
        lmin, kap, E = ladder(c)
        print(f"DH, w = {w:9.6f}: c_0 = {c[0].real:.4f} | max|c_m|/c_0 = {np.max(np.abs(c[1:])) / c[0].real:.3f}"
              f" | first indefinite rung N = {first_bad} | lambda_min(T_{M})/c_0 = {lmin:.3e}")
        print("     |kappa_k|:", " ".join("nan" if np.isnan(x) else f"{x:.3f}" for x in kap), flush=True)
